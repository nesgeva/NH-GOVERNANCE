# NH_B24_REJECTION_CATEGORY_DECISION_2026-09-23_v0_1_CANDIDATE.md

**Status:** DECISION RECORD + CORRECTION CANDIDATE — records a decision Ness made on 2026-09-23; proposes the matching textual correction to the accepted B24 v7 §3.2 table. Not adopted into any authoritative file; edits nothing in place; creates no v8 of B24. Placement in the repository is Ness's action (intended: `05_ACTIVE_CANDIDATE/`).

**Date:** 2026-09-23.

**Authority order:** Master V10 (adopted 2026-06-29) → Decision Defaults S19 v2_2 → cursorrules → Companion. Accepted standalone B24 v7 governs its scope (package-complete record v1_0, 2026-07-03). This record changes nothing above it.

---

## 1. The gap

Accepted `NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md` §3.2 assigns a settled Master §7G rejection category to each semantic reason code. Four cells carry only the word **"substantive"**, which is not one of the seven settled categories that §2.9 and §3.3A require for `rejection_categories`:

| Criterion | Reason | §3.2 cell (as accepted) |
|---|---|---|
| `S-POSSIBILITY-BASIS` | `POSSIBILITY_BASIS_UNSOUND` | substantive |
| `S-CIRCULAR-SUPPORT` | `CIRCULAR_SUPPORT` | substantive |
| `S-SPEAKER-AGENCY` | `SPEAKER_AGENCY_CHANGE` | substantive (terminal) |
| `S-LANE-INTEGRITY` | `LANE_CONTAMINATION` | substantive (terminal) |

Gap audit Part 8 row **P8-U10** found the built validator copies the literal word and required that the mapping be reconciled against accepted sources, never invented. Two independent reads of the full governance repo at `07505fb` (Claude; ChatGPT, 161 files) confirmed **no accepted or authoritative source assigns a category to any of the four**. The Master (§7G 1690–1694) names the failure modes and six reason families; B24 added the seventh (`evidence_self_contradiction`); neither maps these four codes. The reason codes and the rejection itself are settled; only the category label was missing.

## 2. Ness's decision (2026-09-23)

Made in chat after both reads, on the plain-language statement of each case:

| Reason | Category decided | Ness's stated basis |
|---|---|---|
| `POSSIBILITY_BASIS_UNSOUND` | **`unsupported_certainty`** | A31 (accepted 2026-07-07) §4: "an un-linked guess is not a possibility; it is an unsupported claim"; "claiming-beyond-support → `not_grounded_enough`". B24 §7C already lists "basis unsound" among CONSEQUENTIAL (counted) failures, while fabrication is CRITICAL; the label now agrees with the accepted benchmark treatment. |
| `CIRCULAR_SUPPORT` | **`unsupported_certainty`** | Master §7G 1704: "a reading cannot become true merely because later readings repeat it"; A31 §4: repetition "adds no certainty and raises no status". Repetition does not necessarily invent a new fact. |
| `SPEAKER_AGENCY_CHANGE` | **`evidence_self_contradiction`** | B24 §3.2: "who-did-what is preserved exactly relative to the sources"; Master §7G 1690: "does not contradict its own evidence". The proposal disagrees with its own cited source about who did what. §7C already treats it as CRITICAL; unchanged. |
| `LANE_CONTAMINATION` | **DEFERRED** | One code covers two directions (possibility written as fact; fact written as possibility). "Too sure" describes only the first. Ness declined a single label for both; the code keeps the design cell's word until a later decision (possibly a split into two reasons). Rejection and the §7C CRITICAL treatment are unchanged. |

Effect on runtime behavior: none today. All four still commit `rejected`; the specific reason is still recorded; B9's careful-retry seam does not read the category. The label changes what reports, the issue channel, and future counting group together.

## 3. Proposed textual correction to B24 v7 §3.2 (for the future consolidation candidate; not applied here)

Replace the "Settled category" cells:
- `S-POSSIBILITY-BASIS` row: `substantive` → `` `unsupported_certainty` ``
- `S-CIRCULAR-SUPPORT` row: `substantive` → `` `unsupported_certainty` ``
- `S-SPEAKER-AGENCY` row: `substantive (terminal)` → `` `evidence_self_contradiction` (terminal) ``
- `S-LANE-INTEGRITY` row: unchanged, with an explicit note "category assignment deferred by Ness 2026-09-23".

§3.7 severity classes, §3.3A mapping, §3.4 vocabulary, §7C benchmark lists: unchanged.

## 4. Implementation status

The three settled cells are carried into the engine's `nh_b24_validator.py` `_SEMANTIC_REJECTION` table under `NH_BUNDLE1_FIX_ROUND8_BUILD_CONTRACT_v1.md` (direct build loop). The deferred cell is unchanged in code. Code follows the decision; it does not establish it.

## 5. Related open item raised on the same day (not decided)

Whether a possibility refused from a brief may still be written to N.H's own NOTE (Master R5.5: "N.H not a teller, its view a weightless NOTE"; §7B Part 7.5). The NOTE's mechanics are undesigned; this belongs to the NOTE's design round, not to B24.

## 6. No-loss

No authoritative file, accepted package, or historical candidate edited or moved. B24 v7 bytes untouched (`7f5762e5…2171`). Nothing adopted by this record; the decision above is Ness's, recorded here for provenance; the §3.2 correction becomes governing only through the normal versioned route and Ness's explicit acceptance.

*Decision record and correction candidate only. Creates no architecture; changes no file; closes no other open dependency.*
