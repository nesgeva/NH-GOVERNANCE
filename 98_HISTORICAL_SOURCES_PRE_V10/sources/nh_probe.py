"""
nh_probe.py - read-only boundary-signal probe for the accretive store (N.H §11 item 2b)
=======================================================================================
The "read-only probe FIRST" the build order calls for: it reads the store, measures the
cheap signals a future boundary detector would use, and PRINTS numbers. It writes nothing,
touches nothing, builds no records. Same read discipline as nh_peek / nh_log
(nh_accretive_store.read_by_subject only).

  python nh_probe.py                       # probes seed:gpt_purified (default)
  python nh_probe.py seed:conversations_000

What it measures, and why:
  The gpt_purified markers ([NESS]: / [AI_RECALL]:) were stripped, so speaker is not a
  field. A detector must RE-DERIVE speaker from shape. This probe tests how well shape
  separates the two, and whether turns actually alternate, by reporting:
    - turn-length distribution (the rawest signal)
    - how many turns END WITH A QUESTION (a Ness tell)
    - how many turns carry ANSWER-STRUCTURE: markdown / lists / code (an AI tell)
    - a best-effort speaker guess per turn (NESS / AI / AMBIGUOUS) from those signals
    - WITHIN EACH STREAM, how often consecutive turns FLIP speaker vs DOUBLE UP
  A clean flip rate => speaker-flip is a STRONG detector vote. Frequent doubling => weak.

  Honest caveat: the per-turn guess is INFERENCE, not ground truth (the marker is gone).
  That is the point - it measures how reliable that same inference would be inside a detector.
  Thresholds below are GUESSES, printed so they can be argued with, not trusted.
"""

from __future__ import annotations

import re
import sys
from statistics import median

from nh_accretive_store import read_by_subject

DEFAULT_SUBJECT = "seed:gpt_purified"

# --- shape thresholds (GUESSES - the probe exists to test these, not assume them) ---
AI_MIN_WORDS = 60          # this-or-longer, with no question, leans AI
NESS_MAX_WORDS = 25        # this-or-shorter leans Ness
STRUCT_RE = re.compile(r'(\*\*|^#{1,6}\s|^\s*[-*]\s+|^\s*\d+\.\s+|```)', re.M)
QMARKS = ("?", "\uFF1F")    # ascii + fullwidth question mark


def _ends_question(text: str) -> bool:
    return text.rstrip().endswith(QMARKS)


def _has_structure(text: str) -> bool:
    return bool(STRUCT_RE.search(text))


def classify(text: str) -> str:
    """Best-effort speaker from shape alone. NESS | AI | AMBIG."""
    t = text.strip()
    words = len(t.split())
    structured = _has_structure(t)
    question = _ends_question(t)

    if structured or words >= AI_MIN_WORDS:
        # long / structured and NOT a question -> AI; a long question is still ambiguous
        if not question:
            return "AI"
    if question or words <= NESS_MAX_WORDS:
        if not structured and words < AI_MIN_WORDS:
            return "NESS"
    return "AMBIG"


def _segment_streams(records: list[dict]) -> list[list[dict]]:
    """Split into streams by consecutive runs of equal source_title."""
    streams: list[list[dict]] = []
    cur: list[dict] = []
    last_title = object()  # sentinel
    for r in records:
        title = r.get("source_title")
        if title != last_title and cur:
            streams.append(cur)
            cur = []
        cur.append(r)
        last_title = title
    if cur:
        streams.append(cur)
    return streams


def _bar(n: int, total: int, width: int = 34) -> str:
    if total == 0:
        return ""
    return "#" * max(0, round(n / total * width))


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    subject = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SUBJECT
    records = read_by_subject(subject)

    print(f"\n=== nh_probe  ·  subject = {subject} ===")
    if not records:
        print("(no records for that subject)")
        return
    print(f"records: {len(records):,}   (read-only; nothing written)\n")

    # ---- per-turn features ----
    word_counts = []
    n_question = 0
    n_struct = 0
    labels = []
    for r in records:
        content = r.get("content", "") or ""
        words = len(content.split())
        word_counts.append(words)
        if _ends_question(content):
            n_question += 1
        if _has_structure(content):
            n_struct += 1
        labels.append(classify(content))

    total = len(records)

    # ---- length distribution ----
    print("TURN LENGTH (words)")
    buckets = [(0, 5), (6, 15), (16, 30), (31, 60), (61, 120), (121, 250), (251, 10**9)]
    bnames = ["0-5", "6-15", "16-30", "31-60", "61-120", "121-250", "251+"]
    for (lo, hi), name in zip(buckets, bnames):
        c = sum(1 for w in word_counts if lo <= w <= hi)
        print(f"  {name:>8} | {c:6,} {_bar(c, total)}")
    print(f"  median {median(word_counts)} words   max {max(word_counts)} words\n")

    # ---- single-signal tells ----
    print("SHAPE TELLS")
    print(f"  ends with a question : {n_question:6,}  ({n_question/total:5.1%})   <- a Ness tell")
    print(f"  has answer-structure : {n_struct:6,}  ({n_struct/total:5.1%})   <- an AI tell\n")

    # ---- speaker guess ----
    g_ness = labels.count("NESS")
    g_ai = labels.count("AI")
    g_amb = labels.count("AMBIG")
    print("SPEAKER GUESS (from shape; INFERENCE, not ground truth)")
    print(f"  NESS  : {g_ness:6,}  ({g_ness/total:5.1%})")
    print(f"  AI    : {g_ai:6,}  ({g_ai/total:5.1%})")
    print(f"  AMBIG : {g_amb:6,}  ({g_amb/total:5.1%})")
    print(f"  (doc recorded NESS 2,803 / AI 2,884 for this group - cross-check the balance)\n")

    # ---- alternation within streams ----
    streams = _segment_streams(records)
    pairs = flips = dbl_ness = dbl_ai = amb_pairs = 0
    for s in streams:
        slabels = [classify(r.get("content", "") or "") for r in s]
        for a, b in zip(slabels, slabels[1:]):
            pairs += 1
            if a == "AMBIG" or b == "AMBIG":
                amb_pairs += 1
            elif a != b:
                flips += 1
            elif a == "NESS":
                dbl_ness += 1
            else:
                dbl_ai += 1
    decided = flips + dbl_ness + dbl_ai

    print(f"STREAMS: {len(streams):,}   (doc recorded 223 - cross-check)\n")
    print("ALTERNATION (consecutive turns WITHIN a stream)")
    print(f"  pairs examined        : {pairs:6,}")
    print(f"  FLIP (NESS<->AI)      : {flips:6,}" + (f"  ({flips/decided:5.1%} of decided)" if decided else ""))
    print(f"  double NESS,NESS      : {dbl_ness:6,}   <- Ness sent two in a row")
    print(f"  double AI,AI          : {dbl_ai:6,}   <- answer continued / split")
    print(f"  pair touched AMBIG    : {amb_pairs:6,}   (couldn't judge one side)\n")

    if decided:
        rate = flips / decided
        if rate >= 0.9:
            verdict = "STRONG: near-clean alternation -> speaker-flip is a heavy detector vote."
        elif rate >= 0.7:
            verdict = "MODERATE: mostly alternates -> speaker-flip helps but can't stand alone."
        else:
            verdict = "WEAK: doubles up often -> speaker-flip is a minor vote; lean on topic/reset signals."
        print(f"  read: {verdict}")
    print()


if __name__ == "__main__":
    main()
