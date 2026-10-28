#!/usr/bin/env python3
"""
NH Master-21 assembler, version 2 (2026-10-04).

Joins the Master-21 chapter files into one candidate document.

Changes from version 1 (07_TOOLS/nh_master21_assemble.py, SHA-256
a7c4049204272eba11392cf632a093805440f51d61fe03610fe9ec5e14cfed9b):
  1. The part locator recognizes part IDs with hyphens and lower-case
     letters (C-ENGINE-AB, C-WIS-SEP, C-NEW-...); version 1 cut them short.
  2. Ness's decision B2 (2026-10-04): each CONTRACT CHECK block is still
     moved to the appendix word for word, now preceded by a GENERATED note
     that its counts are the writer's counts at writing time, and followed by
     a GENERATED table of current totals computed from the chapter text.
  3. Output files are written with plain newline line endings on every
     system. Version 1 wrote in text mode, which on Windows turns each line
     ending into two characters, so the same content got a different
     fingerprint there. Now the fingerprint is the same on every machine.
Nothing else changes: no chapter sentence is written, reworded or reordered.

Design rule: this script never writes prose. It only (a) concatenates,
(b) removes lines that match an explicit metadata whitelist, (c) moves
CONTRACT CHECK blocks to an appendix, (d) emits generated navigation
(front matter, table of contents, part locator) that is clearly marked
as generated. Every removal and every move is reported line by line,
and the script proves that all surviving body bytes are unchanged.

Usage:
    python3 nh_master21_assemble_v2.py <chapters_dir> <out_dir>
"""

import sys, os, glob, re, hashlib, datetime

# --- Lines removed from a chapter's header zone. Metadata only, never prose.
META_PATTERNS = [
    re.compile(r'^Status:\s'),
    re.compile(r'^Repository:\s'),
    re.compile(r'^\*\*Document:\*\*'),
    re.compile(r'^\*\*Status:\*\*'),
    re.compile(r'^\*\*Source repository:\*\*'),
    re.compile(r'^\*\*Source commit:\*\*'),
]
HEADER_ZONE = 12          # metadata is only ever stripped within this many lines
COMMIT_RE = re.compile(r'`([0-9a-f]{7,40})`')

# --- Counting rules for the GENERATED current-totals tables (decision B2).
CARD_RE = re.compile(r'^### (C-[A-Za-z0-9][A-Za-z0-9\-]*(?:\.[0-9A-Za-z]+)*) — (.*)$')
BOX_RE = re.compile(r'^- (What it is|Takes in|Does|Gives out|Must never|Fails closed by|Fed by|Gated by|Changes):\s?(.*)$')
ROW_RE = re.compile(r'^\| (\d+) · ([A-Z0-9\-]+(?: [A-Z]+)?) \| (.*)$')
NAME_RE = re.compile(r'(?<![A-Za-z0-9\.\-])(C-[A-Za-z0-9][A-Za-z0-9\-]*(?:\.[0-9A-Za-z]+)*) — ')
CITE_RE = re.compile(r'\[(?:V10|DD|CR|COMP|MAP|DR|04/|05/|05i/|98/|NHD-)[^\]]*\]')
PART_ID_RE = re.compile(r'^((?:C|CY|P)-[A-Za-z0-9][A-Za-z0-9\-]*(?:\.[0-9A-Za-z]+)*)')
TOGETHER = ('Fed by', 'Gated by', 'Changes')
TOTAL_RULES = [
    ('cards', 'headings of the form "### C-<id> — <title>"'),
    ('field_lines', 'box lines ("- What it is:" to "- Changes:") inside cards'),
    ('populated_field_lines', 'field lines whose value is not exactly NOT DECIDED'),
    ('not_decided_field_lines', 'field lines whose value is exactly NOT DECIDED'),
    ('used_by_rows', 'numbered rows ("| n · STAMP |") under a card\'s USED BY header'),
    ('together_lines_naming_a_card', 'populated Fed by / Gated by / Changes lines naming at least one card'),
    ('plain_together_lines', 'populated Fed by / Gated by / Changes lines naming no card'),
    ('named_together_endpoints', 'card names in Fed by / Gated by / Changes lines (a name is a card ID followed by " — " and that card\'s exact title)'),
    ('cross_chapter_endpoints', 'named endpoints whose card is defined in another chapter'),
    ('distinct_citations', 'distinct bracketed source citations ([V10 ...], [MAP ...], [04/...] and the other source forms) in the chapter text'),
    ('source_conflict_lines', 'lines carrying a [SOURCE CONFLICT marker'),
]


def parse_cards(lines):
    cards, cur = [], None
    for s in lines:
        m = CARD_RE.match(s)
        if m:
            cur = {'id': m.group(1), 'title': m.group(2), 'boxes': [], 'rows': 0, 'ub': False}
            cards.append(cur)
            continue
        if cur is None:
            continue
        if s.startswith('## ') or s.startswith('<!-- END'):
            cur = None
            continue
        bm = BOX_RE.match(s)
        if bm:
            cur['boxes'].append((bm.group(1), bm.group(2)))
            continue
        if s.startswith('USED BY'):
            cur['ub'] = True
        if cur['ub'] and ROW_RE.match(s):
            cur['rows'] += 1
    return cards


def names_in(text, index):
    out, t = [], text.replace('`', '')
    for m in NAME_RE.finditer(t):
        c = index.get(m.group(1))
        if c and t[m.end():].startswith(c[1].replace('`', '')):
            out.append(m.group(1))
    return out


def current_totals(lines, chapter, index):
    cards = parse_cards(lines)
    t = dict.fromkeys([k for k, _ in TOTAL_RULES], 0)
    t['cards'] = len(cards)
    for c in cards:
        t['used_by_rows'] += c['rows']
        for box, val in c['boxes']:
            t['field_lines'] += 1
            if val.strip() == 'NOT DECIDED':
                t['not_decided_field_lines'] += 1
                continue
            t['populated_field_lines'] += 1
            if box in TOGETHER:
                names = names_in(val, index)
                if names:
                    t['together_lines_naming_a_card'] += 1
                else:
                    t['plain_together_lines'] += 1
                t['named_together_endpoints'] += len(names)
                t['cross_chapter_endpoints'] += sum(1 for n in names if index[n][0] != chapter)
    t['distinct_citations'] = len(set(m.group(0) for s in lines for m in CITE_RE.finditer(s)))
    t['source_conflict_lines'] = sum(1 for s in lines if '[SOURCE CONFLICT' in s)
    return t


def sha(b):
    return hashlib.sha256(b).hexdigest()


def split_contract_check(lines):
    """Return (body_lines, contract_lines). Never drops anything."""
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip() == '## CONTRACT CHECK':
            return lines[:i], lines[i:]
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].startswith('CONTRACT CHECK (') :
            j = i - 1
            while j >= 0 and not lines[j].startswith('```'):
                j -= 1
            if j >= 0:
                return lines[:j], lines[j:]
    return lines, []


def main(chapters_dir, out_dir):
    files = sorted(glob.glob(os.path.join(chapters_dir, '*__CH*.md')))
    if not files:
        sys.exit('no chapter files found in ' + chapters_dir)

    report = []
    report.append('NH MASTER-21 ASSEMBLY REPORT')
    report.append('generated ' + datetime.datetime.now(datetime.timezone.utc)
                  .strftime('%Y-%m-%d %H:%M UTC'))
    report.append('')
    report.append('SOURCE CHAPTERS')

    chapters, pins, removed_all = [], [], []

    for path in files:
        raw = open(path, 'rb').read()
        name = os.path.basename(path)
        lines = raw.decode('utf-8').split('\n')
        report.append(f'  {name}  {len(raw)} bytes  sha256 {sha(raw)}  {len(lines)} lines')

        title = lines[0] if lines and lines[0].startswith('# ') else '# (untitled)'

        kept, removed, commit = [], [], None
        for idx, line in enumerate(lines):
            if idx < HEADER_ZONE and any(p.match(line) for p in META_PATTERNS):
                removed.append((idx + 1, line))
                m = COMMIT_RE.findall(line)
                if m:
                    commit = max(m, key=len)
                continue
            kept.append(line)

        body, contract = split_contract_check(kept)
        while body and body[-1].strip() == '':
            body.pop()

        chapters.append({'name': name, 'title': title, 'body': body,
                         'contract': contract, 'commit': commit,
                         'sha': sha(raw), 'bytes': len(raw)})
        pins.append((title, commit or '(none found)'))
        removed_all.append((name, removed, len(contract)))

    # ---------- generated navigation ----------
    out = []
    out.append('# N.H Master-21 — System Behavior')
    out.append('')
    out.append('Status: CANDIDATE')
    out.append('')
    out.append('This document is the assembled form of the Master-21 chapter files. '
               'It was produced mechanically by joining those chapters; no sentence of '
               'chapter text was written, reworded, or reordered during assembly. '
               'Sections marked GENERATED below are navigation added by the assembler.')
    out.append('')
    out.append('## Source chapters and pins  [GENERATED]')
    out.append('')
    out.append('| chapter | source commit | SHA-256 of chapter file |')
    out.append('|---|---|---|')
    for c in chapters:
        out.append(f"| {c['title'].lstrip('# ').strip()} | `{c['commit'] or '—'}` | `{c['sha']}` |")
    out.append('')

    toc_placeholder = len(out)
    out.append('@@TOC@@')
    out.append('')
    locator_placeholder = len(out)
    out.append('@@LOCATOR@@')
    out.append('')
    out.append('---')
    out.append('')

    body_start_marker = len(out)
    for c in chapters:
        out.extend(c['body'])
        out.append('')
        out.append('---')
        out.append('')

    out.append('# Appendix — Chapter contract checks  [MOVED, NOT EDITED]')
    out.append('')
    out.append('Each block below was delivered at the end of its chapter file and is '
               'reproduced here unchanged.')
    out.append('')
    # decision B2: the document-wide card index, then each chapter's current totals
    index = {}
    for c in chapters:
        for card in parse_cards(c['body']):
            index.setdefault(card['id'], (c['name'], card['title']))
    for c in chapters:
        c['totals'] = current_totals(c['body'], c['name'], index)
    for c in chapters:
        if c['contract']:
            ctitle = c['title'].lstrip('# ').strip()
            out.append(f"## From {ctitle}")
            out.append('')
            out.append('> **[GENERATED]** The block below is this chapter\'s writer check, kept '
                       'word for word. Its counts are the writer\'s counts at writing time and '
                       'are not maintained. The current totals are in the GENERATED table after '
                       'it (Ness\'s decision B2, 2026-10-04).')
            out.append('')
            out.extend(c['contract'])
            out.append('')
            out.append(f"### Current totals for {ctitle}  [GENERATED]")
            out.append('')
            out.append('Counted by the assembler from this chapter\'s text (the writer check '
                       'above excluded).')
            out.append('')
            out.append('| total | count | counting rule |')
            out.append('|---|---|---|')
            for k, rule in TOTAL_RULES:
                out.append(f"| {k} | {c['totals'][k]} | {rule} |")
            out.append('')

    # table of contents from ## headings in the joined body
    toc = ['## Contents  [GENERATED]', '']
    for i in range(body_start_marker, len(out)):
        line = out[i]
        if line.startswith('# ') and not line.startswith('## '):
            toc.append(f'- **{line[2:].strip()}**')
        elif line.startswith('## '):
            toc.append(f'  - {line[3:].strip()}')
    out[toc_placeholder] = '\n'.join(toc)

    # part locator: ### headings whose first token looks like a part ID
    loc = ['## Part locator  [GENERATED]', '',
           '| part ID | described in | heading |', '|---|---|---|']
    current = ''
    seen = set()
    for i in range(body_start_marker, len(out)):
        line = out[i]
        if line.startswith('## ') and not line.startswith('### '):
            current = line[3:].strip()
        if line.startswith('### '):
            head = line[4:].strip()
            m = PART_ID_RE.match(head)
            if m:
                pid = m.group(1).rstrip('.-')
                if pid not in seen:
                    seen.add(pid)
                    loc.append(f'| {pid} | {current} | {head} |')
    out[locator_placeholder] = '\n'.join(loc)

    final = '\n'.join(out) + '\n'
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE.md')
    open(out_path, 'w', encoding='utf-8', newline='\n').write(final)

    # ---------- proof ----------
    report.append('')
    report.append('LINES REMOVED (metadata only, header zone only)')
    for name, removed, ncontract in removed_all:
        report.append(f'  {name}')
        if not removed:
            report.append('    (none)')
        for ln, text in removed:
            report.append(f'    line {ln}: {text}')
        report.append(f'    CONTRACT CHECK block moved to appendix: {ncontract} lines')

    report.append('')
    report.append('BODY INTEGRITY PROOF')
    final_text = final
    all_ok = True
    for c in chapters:
        chunk = '\n'.join(c['body'])
        present = chunk in final_text
        all_ok &= present
        report.append(f"  {c['name']}: body block of {len(chunk)} chars "
                      f"present verbatim in output: {'YES' if present else 'NO'}")
        contract_chunk = '\n'.join(c['contract'])
        if contract_chunk:
            ok = contract_chunk in final_text
            all_ok &= ok
            report.append(f"    contract block of {len(contract_chunk)} chars "
                          f"present verbatim: {'YES' if ok else 'NO'}")
    report.append('')
    report.append('  RESULT: ' + ('ALL SOURCE TEXT PRESENT VERBATIM'
                                  if all_ok else '*** INTEGRITY FAILURE ***'))

    report.append('')
    report.append('OUTPUT')
    report.append(f'  {os.path.basename(out_path)}')
    report.append(f'  {len(final.encode())} bytes, {final.count(chr(10))} lines')
    report.append(f'  SHA-256 {sha(final.encode())}')
    report.append(f'  part locator rows: {len(seen)}')

    rep_path = os.path.join(out_dir, 'NH_MASTER-21_ASSEMBLY_REPORT.txt')
    open(rep_path, 'w', encoding='utf-8', newline='\n').write('\n'.join(report) + '\n')
    print('\n'.join(report))
    return 0 if all_ok else 1


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1], sys.argv[2]))
