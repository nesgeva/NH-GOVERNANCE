# N.H Universal Filter — Theoretical Design
*Captured June 19 2026, from a live design session with Nes. This is a THEORETICAL foundation, not a build plan. Nothing is to be built until this is designed with a fresh head. The ChromaDB cleanup is intentionally ON HOLD because this filter changes how everything enters REALITY.*

---

## The problem it solves

Right now N.H has MULTIPLE different paths that decide "is this real," each with its own rule:
- The epistemic sandbox scores typed thoughts (3 axes)
- `_load_raw_sources()` tags ChatGPT/Gemini history as REALITY **by filename** — no review at all
- The research gatekeeper handles web findings
- The context router uses evidence levels

This violates the sovereignty principle. "REALITY" doesn't actually mean "Nes approved this" — for imported history it just means "was in the seed file." A new thought Nes types gets scored; an old ChatGPT message gets a free pass. Inconsistent.

---

## The core principle

**One filter. Every piece of information. No source exempt — not even ChatGPT/Gemini history.**

Every single piece is treated the same way, judged by the same standard, regardless of where it came from.

---

## What the filter does (and does NOT do)

- **It SORTS and PREPARES. It never decides "real" itself.** (Hebrew: למיין — to sort.)
- Nes remains the ONLY one who promotes anything to REALITY. The filter makes his review faster and better-organized; it never replaces his judgment.
- The moment the filter could declare something "real" on its own, it would rebuild the exact auto-approval hole the whole system exists to prevent. So: **filter sorts, human promotes. Always. No exceptions.**

---

## How it sorts — the deep structure

The filter does NOT drop each piece into one bin. The structure evolved through the session to something much richer:

### It reads the MEANING behind what was said
The first/root level isn't a surface-form check or a binary. It distinguishes **the kind of meaning/intent behind the utterance** — why the thing was said at all. The same sentence ("I'm done with this") can be a claim, an expression, or an intention depending on the meaning behind it. Catching THAT is the filter's primary job.

Candidate root meaning-types (a starting snapshot, NOT final): to state/claim, to ask, to wonder/explore, to express/feel, to intend/want, to report (relay someone else's words), to imagine/hypothesize. (~7, but explicitly open.)

### It grows in EVERY direction
- **Wide at the top:** more root meaning-types than any fixed number. The root level itself can gain new categories as Nes meets ways-of-saying nothing existing can hold.
- **Deep underneath:** each node branches into finer distinctions, and those branch again, deeper over time.
- A single piece travels DOWN A PATH through the structure, getting more precisely characterized at each level — not one label, a route to a leaf.
- New branches AND new roots sprout as reality reveals narratives the current structure can't yet name.

### Why open-ended
Real life has endless narratives. Any fixed list of categories is just today's snapshot and will always be lying a little about how meaning actually works. The structure must be built to grow — forever, in principle.

---

## The central tension (the real design problem)

**Maximally faithful to how meaning works** (infinite, open in every direction) **vs. actually usable by a tired human.**

A structure that grows infinitely with no fixed points becomes so vast that sorting into it is harder than reading the raw information — the tool meant to organize thinking becomes a second thing to organize. Open-endedness is true but expensive to live in.

### The resolution Nes reached
**Maximal-but-bounded. "The most possible."**

Grows in every direction in principle, but deliberately LIMITED in practice — pushed as wide and deep as is actually usable, with a real, chosen boundary. The boundary is itself a design choice that can be moved outward over time as Nes gets better at navigating it. Not infinite (unusable), not rigid (untrue) — the most a human can actually use, then a line.

---

## How this connects to earlier insights (same session + project)

- **"A validator can't be the same system being validated"** — the filter is a living taxonomy that keeps learning, not a frozen ruler.
- The filter is the spiritual successor / generalization of the **epistemic sandbox** — same idea (score how something is said), but applied to EVERY source instead of only typed thoughts.
- It makes the sovereignty principle ACTUALLY consistent — collapsing the 4+ separate "is this real" paths into one chokepoint every piece passes through.

---

## Build-order consequence (important)

**The ChromaDB `nh_reality_core` cleanup is ON HOLD.** Rebuilding the index right now would re-load ChatGPT/Gemini history to REALITY by the old filename rule — the exact thing this filter is meant to change. No point cleaning the index until the filter that decides what enters it is designed.

---

## Status

THEORETICAL ONLY. Designed enough to be the starting point for a fresh-head session. Nothing built. The next session should:
1. Settle the maximal-but-bounded limit concretely (how wide at root, how deep, where the line sits)
2. Decide the unit (what counts as one "piece of information" to be sorted — a sentence? a message? — the segmentation problem, especially for conversation exports)
3. Only then design the actual mechanism

The unit/segmentation question is genuinely hard and unsolved: a ChatGPT export is a conversation (questions, AI replies, tangents), not a list of claims. Something must decide what a "piece" even is before the filter can run on it.
