"""
nh_probe_truth.py - GROUND-TRUTH speaker probe for gpt_purified (N.H §11 item 2b)
=================================================================================
The store dropped the [NESS]:/[AI_RECALL]: marker. The SOURCE file still has it.
This probe re-reads the source (read-only), keeps the real speaker, and answers two
questions the store alone can't:

  1. TRUE alternation - do turns actually alternate, or double up? (now with real labels)
  2. CALIBRATION - if you threw the marker away and guessed speaker from SHAPE alone
     (length / ends-with-question / has-answer-structure), how often would you be RIGHT?

That second answer settles the schema question (issue 3 / item 2a): if shape recovers
speaker reliably, the reading-layer can re-derive it; if not, the schema must CARRY role
(back-filled from this source). Read-only: reads gpt_purified_history.txt, writes nothing.

  python nh_probe_truth.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from statistics import median

BASE = Path(__file__).parent
SEED_FILE = BASE / "gpt_purified_history.txt"

STREAM_RE = re.compile(r"^=== COGNITIVE STREAM:\s*(.+?)\s*===$")
NESS_RE = re.compile(r"^\[NESS\]:\s*(.*)$")
AI_RE = re.compile(r"^\[AI_RECALL\]:\s*(.*)$")

# same shape thresholds as nh_probe, so the guess is identical - now scored vs truth
AI_MIN_WORDS = 60
NESS_MAX_WORDS = 25
STRUCT_RE = re.compile(r'(\*\*|^#{1,6}\s|^\s*[-*]\s+|^\s*\d+\.\s+|```)', re.M)
QMARKS = ("?", "\uFF1F")


def _ends_q(t: str) -> bool:
    return t.rstrip().endswith(QMARKS)


def _struct(t: str) -> bool:
    return bool(STRUCT_RE.search(t))


def shape_guess(text: str) -> str:
    t = text.strip()
    words = len(t.split())
    s = _struct(t)
    q = _ends_q(t)
    if (s or words >= AI_MIN_WORDS) and not q:
        return "AI"
    if (q or words <= NESS_MAX_WORDS) and not s and words < AI_MIN_WORDS:
        return "NESS"
    return "AMBIG"


def parse_turns(path: Path):
    """Yield (stream_index, role, text) keeping the REAL marker. Mirrors the ingest parse."""
    turns = []
    stream_idx = -1
    role = None
    parts: list[str] = []

    def flush():
        nonlocal role, parts
        if role is None:
            parts = []
            return
        text = "\n".join(parts).strip()
        r = role
        role = None
        parts = []
        if text and stream_idx >= 0:
            turns.append((stream_idx, r, text))

    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            sm = STREAM_RE.match(line.strip())
            if sm:
                flush()
                stream_idx += 1
                continue
            nm = NESS_RE.match(line)
            am = AI_RE.match(line)
            if nm or am:
                flush()
                role = "NESS" if nm else "AI"
                first = (nm or am).group(1)
                parts = [first] if first else []
                continue
            if role is not None:
                parts.append(line)
    flush()
    return turns, stream_idx + 1


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    if not SEED_FILE.exists():
        print(f"source not found: {SEED_FILE}")
        return

    turns, n_streams = parse_turns(SEED_FILE)
    total = len(turns)
    n_ness = sum(1 for _, r, _ in turns if r == "NESS")
    n_ai = sum(1 for _, r, _ in turns if r == "AI")

    print(f"\n=== nh_probe_truth  ·  source = {SEED_FILE.name} (read-only) ===\n")
    print("GROUND TRUTH (from the real marker)")
    print(f"  streams : {n_streams:,}   (store/ingest expects 223)")
    print(f"  turns   : {total:,}   (store has 5,687)")
    print(f"  NESS    : {n_ness:,}   (doc 2,803)")
    print(f"  AI      : {n_ai:,}   (doc 2,884)\n")

    # ---- true alternation within streams ----
    pairs = flips = dbl_ness = dbl_ai = 0
    by_stream: dict[int, list[str]] = {}
    for idx, role, _ in turns:
        by_stream.setdefault(idx, []).append(role)
    for roles in by_stream.values():
        for a, b in zip(roles, roles[1:]):
            pairs += 1
            if a != b:
                flips += 1
            elif a == "NESS":
                dbl_ness += 1
            else:
                dbl_ai += 1
    print("TRUE ALTERNATION (consecutive turns within a stream)")
    print(f"  pairs           : {pairs:,}")
    if pairs:
        print(f"  FLIP            : {flips:,}  ({flips/pairs:5.1%})")
        print(f"  double NESS,NESS: {dbl_ness:,}  ({dbl_ness/pairs:5.1%})   <- Ness twice in a row")
        print(f"  double AI,AI    : {dbl_ai:,}  ({dbl_ai/pairs:5.1%})   <- answer split")
    print()

    # ---- length by true speaker ----
    ness_w = [len(t.split()) for _, r, t in turns if r == "NESS"]
    ai_w = [len(t.split()) for _, r, t in turns if r == "AI"]

    def p(vals, q):
        s = sorted(vals)
        return s[min(len(s) - 1, int(q * len(s)))] if s else 0

    print("LENGTH BY TRUE SPEAKER (words)")
    print(f"  NESS : median {median(ness_w):>4}   p90 {p(ness_w,0.9):>5}   max {max(ness_w):>6}")
    print(f"  AI   : median {median(ai_w):>4}   p90 {p(ai_w,0.9):>5}   max {max(ai_w):>6}")
    print()

    # ---- single-feature reliability (precision of each tell) ----
    struct_total = sum(1 for _, _, t in turns if _struct(t))
    struct_ai = sum(1 for _, r, t in turns if _struct(t) and r == "AI")
    q_total = sum(1 for _, _, t in turns if _ends_q(t))
    q_ness = sum(1 for _, r, t in turns if _ends_q(t) and r == "NESS")
    long_total = sum(1 for _, _, t in turns if len(t.split()) >= AI_MIN_WORDS)
    long_ai = sum(1 for _, r, t in turns if len(t.split()) >= AI_MIN_WORDS and r == "AI")
    short_total = sum(1 for _, _, t in turns if len(t.split()) <= NESS_MAX_WORDS)
    short_ness = sum(1 for _, r, t in turns if len(t.split()) <= NESS_MAX_WORDS and r == "NESS")

    def pct(a, b):
        return f"{a/b:5.1%}" if b else "  n/a"

    print("SINGLE-FEATURE RELIABILITY (does the tell actually predict the speaker?)")
    print(f"  has-structure -> AI   : {struct_ai:,}/{struct_total:,} = {pct(struct_ai, struct_total)}")
    print(f"  ends-with-?   -> NESS : {q_ness:,}/{q_total:,} = {pct(q_ness, q_total)}")
    print(f"  words>={AI_MIN_WORDS}     -> AI   : {long_ai:,}/{long_total:,} = {pct(long_ai, long_total)}")
    print(f"  words<={NESS_MAX_WORDS}     -> NESS : {short_ness:,}/{short_total:,} = {pct(short_ness, short_total)}")
    print()

    # ---- full confusion: shape guess vs truth ----
    cm = {("AI", "AI"): 0, ("AI", "NESS"): 0, ("AI", "AMBIG"): 0,
          ("NESS", "AI"): 0, ("NESS", "NESS"): 0, ("NESS", "AMBIG"): 0}
    for _, role, text in turns:
        cm[(role, shape_guess(text))] += 1
    print("SHAPE-GUESS vs TRUTH  (throw away the marker, guess from shape)")
    print(f"                 guess AI   guess NESS   guess AMBIG")
    print(f"  true AI    :   {cm[('AI','AI')]:>7,}   {cm[('AI','NESS')]:>9,}   {cm[('AI','AMBIG')]:>10,}")
    print(f"  true NESS  :   {cm[('NESS','AI')]:>7,}   {cm[('NESS','NESS')]:>9,}   {cm[('NESS','AMBIG')]:>10,}")
    correct = cm[("AI", "AI")] + cm[("NESS", "NESS")]
    wrong = cm[("AI", "NESS")] + cm[("NESS", "AI")]
    amb = cm[("AI", "AMBIG")] + cm[("NESS", "AMBIG")]
    decided = correct + wrong
    print()
    print(f"  correct : {correct:,}  ({correct/total:5.1%} of all turns)")
    print(f"  wrong   : {wrong:,}  ({wrong/total:5.1%})")
    print(f"  ambig   : {amb:,}  ({amb/total:5.1%})")
    if decided:
        print(f"  accuracy on the turns it dared guess: {correct/decided:5.1%}")
    print()

    # ---- verdict for the schema ----
    acc = correct / decided if decided else 0
    amb_rate = amb / total if total else 0
    if acc >= 0.95 and amb_rate <= 0.15:
        v = "shape recovers speaker well -> re-derivation viable; schema MAY skip carrying role."
    elif acc >= 0.9:
        v = "shape mostly works but leaves a real ambiguous pile -> SAFEST to carry role (back-fill from source)."
    else:
        v = "shape is unreliable -> schema MUST carry role; do NOT re-derive from shape."
    print(f"  read for schema (item 2a): {v}\n")


if __name__ == "__main__":
    main()
