#!/usr/bin/env python3
"""
NH Master-21 assembler.

Joins the Master-21 chapter files into one candidate document.

Design rule: this script never writes prose. It only (a) concatenates,
(b) removes lines that match an explicit metadata whitelist, (c) moves
CONTRACT CHECK blocks to an appendix, (d) emits generated navigation
(front matter, table of contents, part locator) that is clearly marked
as generated. Every removal and every move is reported line by line,
and the script proves that all surviving body bytes are unchanged.

Usage:
    python3 nh_master21_assemble.py <chapters_dir> <out_dir>
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
    for c in chapters:
        if c['contract']:
            out.append(f"## From {c['title'].lstrip('# ').strip()}")
            out.append('')
            out.extend(c['contract'])
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
            m = re.match(r'^((?:C|CY|P)-[A-Z0-9]+(?:\.[0-9A-Z]+)*)', head)
            if m:
                pid = m.group(1).rstrip('.')
                if pid not in seen:
                    seen.add(pid)
                    loc.append(f'| {pid} | {current} | {head} |')
    out[locator_placeholder] = '\n'.join(loc)

    final = '\n'.join(out) + '\n'
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE.md')
    open(out_path, 'w', encoding='utf-8').write(final)

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
    open(rep_path, 'w', encoding='utf-8').write('\n'.join(report) + '\n')
    print('\n'.join(report))
    return 0 if all_ok else 1


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1], sys.argv[2]))
