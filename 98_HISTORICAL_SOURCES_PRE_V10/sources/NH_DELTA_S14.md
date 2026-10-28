# N.H — DELTA S14
### Session 14 (June 23 2026). A DESIGN session — three open forks closed. NOTHING built; no disk writes except read-only verification. The floor is unchanged: reading record still DESIGNED-NOT-CODED, `append_reading` still root-shaped, zero real readings.

*This delta is for review before folding into a full master regen. It records decisions only. Derived from `NH_MASTER-14_FINAL.md`; on any conflict the master’s table wins until this is folded in.*

---

## WHAT HAPPENED THIS SESSION
Worked the locked §11-item-20 sequence, steps 1–6, carefully and one at a time. Step 1 verified on disk. Steps 2, 3, 6 closed the three genuinely-open forks. Step 4 was felt on real roots (proof-of-move only, nothing kept or sealed). The three forks the master deliberately left open — `confidence` representation, gold scoring rule, engine failure-behavior — are now all decided.

---

## STEP 1 — DISK VERIFY (done, floor confirmed)
Read-only checks against the live store. All matched the master’s status table exactly:
- Roots = **5521**; `.nh_roots.sealed` present (0 bytes, dated 06/22 11:05 PM); `.nh_readings_store.jsonl` **not found** → zero real readings.
- `append_reading` signature on disk = `(subject, content, re_reads, role, source_title=None, timestamp=None)` — still **root-shaped**.
- `STORE_PATH`, `READINGS_PATH`, `SEALED_MARKER` all present (not missing).
- `_validate_record` enforces the **7-field ROOT** schema only; root-vs-reading split is purely `re_reads` empty-or-not. **No reading validator, no reading writer.**
- ⚠ Inert flag (not a blocker): `_validate_record`’s docstring still references “the existing 188 seed records” — stale wording, code is correct. Note for the eventual comment/`.cursorrules` cleanup.

---

## DECISION 1 — `confidence` REPRESENTATION  (§11 item 19; was OPEN → **DECIDED**)
**Chosen: option 3 — a structured `confidence` object (a two-slot box), NOT a single field.**

The box holds, side by side, never blended into one number:
- **`interpretation_confidence`** — how sure the engine is of *this reading*. Filled on every reading.
- **`source_reliability`** — how trustworthy the source was. **Present (slot exists) from the FIRST reading, but left EMPTY/omitted until the engine can honestly judge a source** (sarcastic / fictional / copied / manipulated). Empty-when-unknown is honest (same rule as unknown story-parts); never faked.

Why the box and not the single named field: Ness needs the **slot** present from the first reading (un-retrofittable on sealed/early records), even though the **value** can’t be filled yet. The box gives both at once — slot now, value later — and is richer for distinguishing “confident read of a shaky source” from “tentative read of a solid source.”

The other two “kinds of sure” stay in their existing homes, untouched:
- **story firmness** → inside `story_layer[].firmness`, per telling.
- **retrieval relevance** → computed at search time, per query; never stored on the reading.

Constraint preserved: never one blended number; confidence never rises from copied error (no false corroboration); a reading never inherits a prior’s confidence. Level note still holds: `mode.classification_confidence` is local and separate from this top-level box.

---

## DECISION 2 — GOLD SCORING RULE  (§11 item 20; was OPEN → **DECIDED**)
The gold **format** was already settled by the master (root + frozen context + annotation; sealed; versioned; human-annotation provenance). The six **scoring** questions are now answered:

1. **`meaning`** — judged by **semantic match** (means the same, not exact words). **Ness decides** same/not-same, by hand, once, on the sealed cases. The model may show the pair but never holds the verdict (no grading-its-own-homework; gold stays an outside check).
2. **`story_layer`** — **not graded yet (loose).** Grade `meaning` now; add partial story-scoring LATER, weighted from real engine behavior (don’t invent point-weights blind before any readings exist).
3. **Missing vs inventing** — **inventing is the real fail** (the poisoning failure mode). **Leaving something out is NOT a fail**, as long as what *was* said is correct. A bare blank is honest.
4. **Correct-but-extra** — **depends**: extra that is *true* → pass; extra that is *made-up* → fail. (Same rule as #3 applied to extras — made-up content is the only real sin.)
5. **Multiple acceptable readings** — **yes, a case may list a few.** Each allowed reading carries a short note on *what makes it valid* (whose view / why it holds). Engine passes if it lands on any one; the note shows *which perspective* it took (so a match is a real read, not a lucky guess). This is the test-side mirror of `story_layer` being a list of tellings.
6. **Who decides pass/fail** — **Ness.** Model assists, never judges. (Rationale: the spec is “reads the way Ness’s mind reads,” so the only valid reference is Ness; anyone else silently changes the test into “reads like *them*.”)

Framing clarification reached this session (not a new rule, an understanding): annotating gold is **not** the forbidden manual gate and **not** deciding truth. It is recording **reactions/opinions** — “this is a fair read by my lens” — off to the side, sealed, used once. Ness stays *inside* (gives honest reactions); the machine is the *outside* (gathers reactions into the inward-mirror view). A gold answer is never a fact, can be wrong, and is corrected only as a NEW sealed version (the gold seal holds).

---

## DECISION 3 — ENGINE FAILURE-BEHAVIOR  (§11 item 20 step 6; was OPEN → **DECIDED**)
When the engine **cannot interpret** a root, it does NOT fake a minimal read (rejected) and does NOT stay silent (rejected). Instead — **options 3 + 4 together, as one move:**

- It writes an **honest `insufficient-context` reading** — a real record whose content is, in effect, “seen this, couldn’t read it — not enough context.” (“Unknown is honest,” made into an actual record.)
- That record is **marked revisable** — when more context later exists, the engine can return and add a NEW read **beside** it. The honest “couldn’t read this” record is never overwritten (only-adds holds); the later successful read accretes next to it, preserving the trace that it was once unreadable.

Deferred (named, not decided now): the **retry trigger** — *when/whether* the engine actually revisits the marked records. “Marked revisable” ≠ “churn the whole pile every night.” The pile of insufficient-context records is itself the visible, countable backlog (no hidden ever-growing queue).

---

## STEP 4 — FELT, NOT COMMITTED (no gold kept or sealed)
Pulled 8 real roots read-only; reacted to four as a proof-of-move:
- clear read (a game question) ✓ · clear read of a different *type* (assistant giving instructions) ✓ · “not enough context, too general” (honest non-read) · a bare ambiguous line correctly **rejected as an unfair test case** (unreadable without its context → would fail the engine unfairly; belongs out of a first batch, or only inside its frozen context).
Lesson banked: building gold is partly **sorting** — keep clean roots, drop unfair ones — not forcing a read on everything. No cases were written or sealed. Real step-4 annotation is a later sit-down.

---

## STATUS TABLE — ROWS THAT FLIP (for the regen)
- `Reading-record confidence representation` : **NOT DECIDED → DECIDED** (two-slot `confidence` object: `interpretation_confidence` + empty-until-knowable `source_reliability`).
- `Gold scoring rule + engine failure-behavior` : **NOT DECIDED → DECIDED** (six scoring rules above; failure = insufficient-context record, revisable).
- `Reading-record SHAPE overall` : **PROVISIONALLY SETTLED → SETTLED** (the last open piece, `confidence`, is now resolved; shape may be frozen by the validator).
- Everything else in the table is **UNCHANGED**. The floor did not move: reading validator/writer still DESIGNED-NOT-BUILT, zero real readings, `append_reading` still root-shaped.

## SECTIONS THE REGEN MUST EDIT (surgical, not a rewrite)
- **§6B** — reading schema: replace the single `confidence` field with the two-slot box; note `source_reliability` slot-present / value-deferred.
- **§11 item 19** — mark confidence resolved (two-slot box); keep the four-quantities reasoning as the rationale.
- **§11 item 20** — record the six scoring rules + the failure-behavior decision; keep the gold format/seal text as-is.
- **§7C / item 2** — no status change; reading record still uncoded. The next build (validator/writer) now has an unambiguous `confidence` shape to enforce.
- **Top delta block + version.** ⚠ If bumped to MASTER-15, the DECISION-DEFAULTS provenance pointer line must update in the same pass, or the pair goes stale. If held at 14, leave the pointer.

## STILL OPEN AFTER S14
The three forks are closed. Remaining open items are unchanged from the master and were NOT touched: multi-box architecture (item 18), the view layer (item 21), person-box mechanics/contamination (item 22), off-board affirmation seam (item 23), privacy/threat model + redaction path (item 24), go-live hardening (item 25), the deferred retry-trigger for insufficient-context records, and the Chroma rebuild + model/Hebrew forks (item 3 / §16).

---
*Decisions only — nothing built. Verify on disk before building on any “built” line. On any conflict, the master’s status table wins until this delta is folded into a full regen.*
