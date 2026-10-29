# Chapter 3-l — Group A: C-GOLD

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-l.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`

This piece defines the C-GOLD top card, legacy sealed sets, scoring and protection rules, and accepted A1 replacement story-gold content. The legacy runtime answer-key files are documented by V10; their full contents are not present in the pinned READ folders and are not reconstructed. A1's exact target and frozen-context data come from its accepted content file. The original PDF and companion transcript have not been independently opened here. Their appearances below are frozen benchmark inputs, not additional assertions by N.H.

The existing `C-GOLD.1 — Promotion evaluation-evidence bridge` remains defined in CH03-e. CH03-m covers its aggregate and result derivation; CH03-n covers applicability AP-1–AP-12 and the remaining bridge details. No second bridge card is created. Accepted A1 content and its design-provenance seal do not establish root pinning, runtime sealing, an executable benchmark or a built Engine C.

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`. `04/` and `05/` name the exact accepted-design and active-candidate files respectively. The accepted bridge's receipt, already verified in CH03-e, establishes its ACCEPTED status despite its frozen candidate filename.

<!-- BEGIN BEHAVIOR -->

### C-GOLD — Sealed gold sets v1, v2-B (§7C)
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v1 and GOLD SET v2-B rows] [MAP C-GOLD]

ALONE
- What it is: BUILT — Two annotated, sealed outside examinations: eight clean-bare v1 cases and seven context-requiring v2-B cases. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v1 and GOLD SET v2-B rows]
- Takes in: BUILT — Engine A and B outputs from their respective gold-run entry points, stored in quarantine. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Minimal engine A and Engine B rows] [V10 §5 / Accretive store + tooling]
- Does: DESIGNED — Supplies fixed cases for semantic evaluation under the six gold rules; Ness alone judges pass/fail. [MAP C-GOLD] [DD §3D]
- Gives out: DESIGNED — Case judgments and traceable gold-evaluation records, leaving both sealed answer keys unchanged. [MAP C-GOLD]
- Gives out: ACCEPTED — Separate narrow evaluation-evidence references through the promotion evaluation-evidence bridge; neither gold ownership nor the bridge decides promotion. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3]
- Must never: DESIGNED — Alter a sealed case in response to engine output, let a model judge pass/fail, or treat the v1/v2-B exams as story-layer grading. Corrections create new versioned gold. [DD §3D] [MAP C-GOLD]
- Fails closed by: DESIGNED — Failing invented meaning or a made-up extra, without changing the case to fit the output. [DD §3D]

TOGETHER
- Fed by: BUILT — C-GOLD.2 — Gold v1: supplies the eight sealed clean-bare cases. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v1 row]
- Fed by: BUILT — C-GOLD.3 — Gold v2-B: supplies the seven sealed context-requiring cases. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v2-B row]
- Fed by: ACCEPTED — C-GOLD.1 — Promotion evaluation-evidence bridge: supplies separate narrow evidence references within CY-G while retaining C-GOLD's gold-examination ownership. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3]
- Fed by: ACCEPTED — C-GOLD.8 — A1 replacement story-gold: provides accepted unpinned story-bearing benchmark content, subject to its separate runtime prerequisites. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §5] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §7]
- Fed by: DESIGNED — C-GOLD.9 — Protected contextual-gold draft: supplies the separate draft's protection and placement boundary, without claiming a sealed runtime artifact. [CR §4B / GOLD SET FILES]
- Gated by: DESIGNED — C-GOLD.4 — Six gold scoring rules: meaning judgments obey the fixed rules and remain Ness-owned. [DD §3D]
- Gated by: DESIGNED — C-GOLD.5 — Insufficient-context engine result: insufficient context requires an honest revisable reading. [DD §3D]
- Gated by: DESIGNED — C-GOLD.6 — Protected engine build order: Engine C requires story-bearing gold and wider reading requires benchmark evidence. [MAP C-GOLD]
- Gated by: DESIGNED — C-GOLD.7 — Gold operation records: each evaluation and judgment requires a permanent operation record. [MAP C-GOLD] [V10 §0B]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1 — Promotion evaluation-evidence bridge | Sealed-gold examination and gold-run logging. | Extends C-GOLD with the accepted evaluation-evidence contract. | Supplies separate narrow evaluation evidence; it does not promote a reading. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] |
| 2 · BUILT | C-ENGINE-AB — Engines A & B (§7C, §16) | The eight bare-root v1 cases and seven context-requiring v2-B cases. | Runs the respective sealed cases through the A and B gold entry points. | Receives gold-run readings in quarantine. | [V10 §5 / Accretive store + tooling] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Minimal engine A and Engine B rows] |
| 3 · BUILT | C-ENGINE-AB.1.3 — Engine A run_on_gold() | The eight sealed v1 cases. | Runs Engine A's bare-root gold exam. | Produces quarantine readings for the cases. | [V10 §5 / Accretive store + tooling] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Minimal engine A row] |
| 4 · BUILT | C-ENGINE-AB.2.4 — Engine B run_on_gold() | The seven sealed v2-B cases. | Runs Engine B's contextual gold exam. | Produces quarantine readings for the cases. | [V10 §5 / Accretive store + tooling] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine B row] |
| 5 · DESIGNED | C-ENGINE-C.7 — Story-bearing benchmark prerequisite | The separate story-bearing benchmark requirement. | Requires story-bearing gold before Engine C testing; legacy v1/v2-B do not supply it. | Keeps Engine C testing gated and wider-thread performance unassumed. | [MAP C-GOLD] [V10 §7C] |
| 6 · DESIGNED | C-16.7 — Final Interactive Translator adoption | A verified candidate. | Supplies both sealed sets, which together supply the required model test floor. | Nothing in this card. | [V10 §16] |
| 7 · ACCEPTED | C-16.22 — Model-candidate benchmark | Identical prompts/context across candidates, repeated trials and both sealed gold sets for a replacement mouth. | Supplies both sets, which together supply the mandatory replacement-model test floor. | Nothing in this card. | [04/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md §7B.1] |

SUB-PARTS: C-GOLD.1 — Promotion evaluation-evidence bridge; C-GOLD.2 — Gold v1; C-GOLD.3 — Gold v2-B; C-GOLD.4 — Six gold scoring rules; C-GOLD.5 — Insufficient-context engine result; C-GOLD.6 — Protected engine build order; C-GOLD.7 — Gold operation records; C-GOLD.8 — A1 replacement story-gold; C-GOLD.9 — Protected contextual-gold draft

### C-GOLD.2 — Gold v1
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v1 row]

ALONE
- What it is: BUILT — `NH_GOLD_SET_v1.md`, the 4,951-byte annotated answer key containing eight clean-bare cases. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v1 row] [V10 §5 / Physical stores on disk]
- Takes in: BUILT — Engine A's readings of those eight roots without preceding context or story output. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Minimal engine A row] [V10 §7C]
- Does: BUILT — Supplies the sealed v1 cases to Engine A's `run_on_gold()`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Minimal engine A row] [V10 §5 / Accretive store + tooling]
- Gives out: DESIGNED — The fixed reference meanings for semantic comparison; `story_layer` is ungraded. [DD §3D]
- Gives out: BUILT — Engine A's recorded tested result is approximately 5–6 solid cases out of eight after prompt and role fixes. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Minimal engine A row]
- Must never: DESIGNED — Accept an in-place case correction or let an engine's miss change the answer key. A correction is new versioned gold. [DD §3D]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: BUILT — C-GOLD.2.1 — Gold v1 seal marker: sealed v1 cases must remain unchanged; marker existence does not establish an automatic edit-refusal mechanism. [DD §3D] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v1 row]
- Gated by: DESIGNED — C-GOLD.4 — Six gold scoring rules: only the settled semantic rules govern the case judgments. [DD §3D]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-GOLD — Sealed gold sets v1, v2-B (§7C) | Engine A's readings of those eight roots without preceding context or story output. | supplies the eight sealed clean-bare cases. | The fixed reference meanings for semantic comparison; `story_layer` is ungraded. Engine A's recorded tested result is approximately 5–6 solid cases out of eight after prompt and role fixes. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v1 row] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Minimal engine A row] [V10 §7C] [DD §3D] |

SUB-PARTS: C-GOLD.2.1 — Gold v1 seal marker

### C-GOLD.2.1 — Gold v1 seal marker
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v1 row]

ALONE
- What it is: BUILT — `.nh_gold_v1.sealed`, the zero-byte marker accompanying the sealed v1 answer key. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v1 row] [V10 §5 / Physical stores on disk]
- Takes in: NOT DECIDED
- Does: BUILT — Marks the recorded gold v1 artifact as sealed. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v1 row]
- Gives out: BUILT — The seal marker on disk beside `NH_GOLD_SET_v1.md`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v1 row]
- Must never: DESIGNED — Be treated as permission to edit the sealed answer key; the cases remain immutable and a correction is a new version. [DD §3D]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-GOLD.2 — Gold v1 | NOT DECIDED | sealed v1 cases must remain unchanged; marker existence does not establish an automatic edit-refusal mechanism. | The seal marker on disk beside `NH_GOLD_SET_v1.md`. | [DD §3D] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v1 row] |

SUB-PARTS: NONE

### C-GOLD.3 — Gold v2-B
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v2-B row]

ALONE
- What it is: BUILT — `NH_GOLD_SET_v2_B.md`, the 5,449-byte annotated answer key containing seven context-requiring cases. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v2-B row] [V10 §5 / Physical stores on disk]
- Takes in: BUILT — Engine B readings using three preceding turns from the same thread, with full content and BACKGROUND/END BACKGROUND framing. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine B row] [V10 §5 / Accretive store + tooling]
- Does: BUILT — Supplies the seven sealed cases to Engine B's `run_on_gold()`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine B row] [V10 §5 / Accretive store + tooling]
- Gives out: BUILT — The recorded case references are B1 `7ac0381c`, “episode 2,” pass; B2 `4e125b71`, “yes sure, second.”, pass; B3 `0df151d3`, “yes, second option.”, a remaining miss with cause unisolated; B4 `9359edff`, emotional reaction, pass; B5 `580d74d4`, “Brief slow.”, pass; B6 `09514821`, “Yes! This is it.”, pass; B7 `4b4e5551`, “כן”, pass. These are the published short identifiers and descriptions, not fabricated full root identities or complete case texts. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine B row] [V10 §11 item 20]
- Gives out: BUILT — The tested dolphin 8B setup's recorded result is 6.5/7. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine B row]
- Must never: DESIGNED — Grade `story_layer` in this set, rewrite a case after a miss, treat the B3 cause as proven, or promise 7/7 after an upgrade. Model capability, prompt framing, context format and run variance remain possible contributors; any new setup requires benchmarking. [DD §3D] [V10 §11 item 20]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: BUILT — C-GOLD.3.1 — Gold v2-B seal marker: the sealed v2-B key is immutable; the sources name its marker without specifying automatic edit enforcement. [DD §3D] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v2-B row]
- Gated by: DESIGNED — C-GOLD.4 — Six gold scoring rules: the v2-B judgments use the same six legacy rules as v1. [DD §3D]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-GOLD — Sealed gold sets v1, v2-B (§7C) | Engine B readings using three preceding turns from the same thread, with full content and BACKGROUND/END BACKGROUND framing. | supplies the seven sealed context-requiring cases. | The recorded case references are B1 `7ac0381c`, “episode 2,” pass; B2 `4e125b71`, “yes sure, second.”, pass; B3 `0df151d3`, “yes, second option.”, a remaining miss with cause unisolated; B4 `9359edff`, emotional reaction, pass; B5 `580d74d4`, “Brief slow.”, pass; B6 `09514821`, “Yes! This is it.”, pass; B7 `4b4e5551`, “כן”, pass. These are the published short identifiers and descriptions, not fabricated full root identities or complete case texts. The tested dolphin 8B setup's recorded result is 6.5/7. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v2-B row] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine B row] [V10 §5 / Accretive store + tooling] [V10 §11 item 20] |

SUB-PARTS: C-GOLD.3.1 — Gold v2-B seal marker

### C-GOLD.3.1 — Gold v2-B seal marker
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v2-B row]

ALONE
- What it is: BUILT — `.nh_gold_v2_B.sealed`, the zero-byte seal marker for the v2-B answer key. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v2-B row] [V10 §5 / Physical stores on disk]
- Takes in: NOT DECIDED
- Does: BUILT — Marks the recorded gold v2-B artifact as sealed. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v2-B row]
- Gives out: BUILT — The marker on disk alongside `NH_GOLD_SET_v2_B.md`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v2-B row]
- Must never: DESIGNED — Enable an in-place answer-key alteration; any correction creates new versioned gold. [DD §3D]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-GOLD.3 — Gold v2-B | NOT DECIDED | the sealed v2-B key is immutable; the sources name its marker without specifying automatic edit enforcement. | The marker on disk alongside `NH_GOLD_SET_v2_B.md`. | [DD §3D] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, GOLD SET v2-B row] |

SUB-PARTS: NONE

### C-GOLD.4 — Six gold scoring rules
Stamp: DESIGNED    Source: [DD §3D] [MAP C-GOLD]

ALONE
- What it is: DESIGNED — The six governing rules for gold meaning judgments. [DD §3D]
- Takes in: DESIGNED — An engine reading and the case's acceptable reference meaning or meanings. [DD §3D]
- Does: DESIGNED — Uses semantic match, leaves v1/v2-B story output ungraded, fails invention rather than correct omission, distinguishes true extras from made-up extras, permits several acceptable readings, and reserves pass/fail judgment to Ness. [DD §3D]
- Gives out: DESIGNED — Ness's pass/fail judgment of the case. [DD §3D]
- Must never: DESIGNED — Replace semantic judgment with word matching, retroactively grade legacy story output, fail an otherwise correct omission, accept an invented extra, reduce a multi-answer case to one mandatory phrasing, or give the judging authority to a model. [DD §3D]
- Fails closed by: DESIGNED — Failing output that invents content, including a made-up extra. [DD §3D]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-GOLD.4.1 — Semantic match: comparison concerns meaning rather than identical words. [DD §3D]
- Gated by: DESIGNED — C-GOLD.4.2 — Legacy story-layer exclusion: neither legacy exam grades `story_layer`. [DD §3D]
- Gated by: DESIGNED — C-GOLD.4.3 — Invention and omission: a correct omission is not failure; invention is. [DD §3D]
- Gated by: DESIGNED — C-GOLD.4.4 — Correct and invented extras: only a genuinely true extra may pass. [DD §3D]
- Gated by: DESIGNED — C-GOLD.4.5 — Multiple acceptable readings: a case may admit more than one reading. [DD §3D]
- Gated by: DESIGNED — C-GOLD.4.6 — Ness-owned pass/fail: assistance never transfers judging authority to a model. [DD §3D]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-GOLD — Sealed gold sets v1, v2-B (§7C) | An engine reading and the case's acceptable reference meaning or meanings. | meaning judgments obey the fixed rules and remain Ness-owned. | Ness's pass/fail judgment of the case. | [DD §3D] |
| 2 · DESIGNED | C-GOLD.2 — Gold v1 | An engine reading and the case's acceptable reference meaning or meanings. | only the settled semantic rules govern the case judgments. | Ness's pass/fail judgment of the case. | [DD §3D] |
| 3 · DESIGNED | C-GOLD.3 — Gold v2-B | An engine reading and the case's acceptable reference meaning or meanings. | the v2-B judgments use the same six legacy rules as v1. | Ness's pass/fail judgment of the case. | [DD §3D] |
| 4 · DESIGNED | C-GOLD.6.3 — Benchmark before wider-reading claims | An engine reading and the case's acceptable reference meaning or meanings. | both legacy exams retain their own settled judgment rules under a new setup. | Ness's pass/fail judgment of the case. | [DD §3D] |
| 5 · ACCEPTED | C-GOLD.8.3 — Separate primary and theme grading | An engine reading and the case's acceptable reference meaning or meanings. | the additional A1 structure preserves the six governing gold rules. | Ness's pass/fail judgment of the case. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.1] [DD §3D] |
| 6 · ACCEPTED | C-GOLD.1.8.1.5.1 — Sealed-gold aggregate scoring | Ness's current authorized per-case judgment heads under the six settled rules and the accepted gold aggregate rule from the frozen epoch, identified by bridge decision NHD-B16EEB-D2. | Gates this place: the six legacy per-case rules remain the governing meaning rules. | Nothing in this card. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] |

SUB-PARTS: C-GOLD.4.1 — Semantic match; C-GOLD.4.2 — Legacy story-layer exclusion; C-GOLD.4.3 — Invention and omission; C-GOLD.4.4 — Correct and invented extras; C-GOLD.4.5 — Multiple acceptable readings; C-GOLD.4.6 — Ness-owned pass/fail

### C-GOLD.4.1 — Semantic match
Stamp: DESIGNED    Source: [DD §3D]

ALONE
- What it is: DESIGNED — The meaning-comparison criterion. [DD §3D]
- Takes in: DESIGNED — The output's `meaning` and the gold meaning. [DD §3D]
- Does: DESIGNED — Compares their semantic content. [DD §3D]
- Gives out: DESIGNED — A meaning comparison that permits different wording. [DD §3D]
- Must never: DESIGNED — Require an exact wording match in place of semantic agreement. [DD §3D]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-GOLD.4 — Six gold scoring rules | The output's `meaning` and the gold meaning. | comparison concerns meaning rather than identical words. | A meaning comparison that permits different wording. | [DD §3D] |

SUB-PARTS: NONE

### C-GOLD.4.2 — Legacy story-layer exclusion
Stamp: DESIGNED    Source: [DD §3D]

ALONE
- What it is: DESIGNED — The grading boundary of v1 and v2-B. [DD §3D]
- Takes in: DESIGNED — Any `story_layer` produced alongside the meaning in a legacy gold run. [DD §3D]
- Does: DESIGNED — Leaves that story output outside the legacy case grade. [DD §3D]
- Gives out: DESIGNED — A legacy judgment unaffected by story-layer grading. [DD §3D]
- Must never: DESIGNED — Extend either sealed legacy set into a story-layer exam. [DD §3D]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-GOLD.4 — Six gold scoring rules | Any `story_layer` produced alongside the meaning in a legacy gold run. | neither legacy exam grades `story_layer`. | A legacy judgment unaffected by story-layer grading. | [DD §3D] |

SUB-PARTS: NONE

### C-GOLD.4.3 — Invention and omission
Stamp: DESIGNED    Source: [DD §3D]

ALONE
- What it is: DESIGNED — The distinction between invented content and an incomplete but correct reading. [DD §3D]
- Takes in: DESIGNED — What the output asserts and what it omits. [DD §3D]
- Does: DESIGNED — Fails invention; does not fail an omission when the stated material is correct. [DD §3D]
- Gives out: DESIGNED — A failure for making something up, without imposing completeness as an unstated legacy scoring threshold. [DD §3D]
- Must never: DESIGNED — Pass invented material or fail a correct statement merely for leaving something out. [DD §3D]
- Fails closed by: DESIGNED — Returning failure for invention. [DD §3D]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-GOLD.4 — Six gold scoring rules | What the output asserts and what it omits. | a correct omission is not failure; invention is. | A failure for making something up, without imposing completeness as an unstated legacy scoring threshold. | [DD §3D] |
| 2 · DESIGNED | C-GOLD.5 — Insufficient-context engine result | What the output asserts and what it omits. | insufficient context cannot justify an invented reading. | A failure for making something up, without imposing completeness as an unstated legacy scoring threshold. | [DD §3D] |

SUB-PARTS: NONE

### C-GOLD.4.4 — Correct and invented extras
Stamp: DESIGNED    Source: [DD §3D]

ALONE
- What it is: DESIGNED — The rule for content beyond a case's listed reference. [DD §3D]
- Takes in: DESIGNED — An additional claim in the engine output. [DD §3D]
- Does: DESIGNED — Permits a true extra to pass and fails a made-up extra. [DD §3D]
- Gives out: DESIGNED — A pass-permitted true addition or a failed invented addition. [DD §3D]
- Must never: DESIGNED — Treat unlisted-but-true and fabricated content as the same category. [DD §3D]
- Fails closed by: DESIGNED — Failing the case when the extra is made up. [DD §3D]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-GOLD.4 — Six gold scoring rules | An additional claim in the engine output. | only a genuinely true extra may pass. | A pass-permitted true addition or a failed invented addition. | [DD §3D] |

SUB-PARTS: NONE

### C-GOLD.4.5 — Multiple acceptable readings
Stamp: DESIGNED    Source: [DD §3D]

ALONE
- What it is: DESIGNED — Permission for one case to list several acceptable readings. [DD §3D]
- Takes in: DESIGNED — The case's supported reference alternatives. [DD §3D]
- Does: DESIGNED — Keeps the alternatives available for semantic judgment. [DD §3D]
- Gives out: DESIGNED — More than one acceptable reading when the case supplies them. [DD §3D]
- Must never: DESIGNED — Require every case to have one uniquely worded answer. [DD §3D]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-GOLD.4 — Six gold scoring rules | The case's supported reference alternatives. | a case may admit more than one reading. | More than one acceptable reading when the case supplies them. | [DD §3D] |
| 2 · ACCEPTED | C-GOLD.8.5.10 — Acceptable alternative | The case's supported reference alternatives. | more than one supported reading may be valid. | More than one acceptable reading when the case supplies them. | [DD §3D] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.1] |

SUB-PARTS: NONE

### C-GOLD.4.6 — Ness-owned pass/fail
Stamp: DESIGNED    Source: [DD §3D] [MAP C-GOLD]

ALONE
- What it is: DESIGNED — Exclusive ownership of gold meaning judgment by Ness. [DD §3D]
- Takes in: DESIGNED — The candidate reading, case references and any model assistance. [DD §3D]
- Does: DESIGNED — Leaves the pass/fail decision to Ness alone. [DD §3D]
- Gives out: DESIGNED — A Ness judgment; a model's contribution remains assistance. [DD §3D]
- Must never: DESIGNED — Treat the model as the judge, including when it assists with comparison. [DD §3D]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — Ness's own pass/fail judgment is required. [DD §3D]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-GOLD.4 — Six gold scoring rules | The candidate reading, case references and any model assistance. | assistance never transfers judging authority to a model. | A Ness judgment; a model's contribution remains assistance. | [DD §3D] |
| 2 · DESIGNED | C-GOLD.7.1 — annotator | The candidate reading, case references and any model assistance. | the annotator metadata cannot transfer gold judging authority to a model. | A Ness judgment; a model's contribution remains assistance. | [MAP C-GOLD] [DD §3D] |

SUB-PARTS: NONE

### C-GOLD.5 — Insufficient-context engine result
Stamp: DESIGNED    Source: [DD §3D]

ALONE
- What it is: DESIGNED — The engine's response when context is insufficient. [DD §3D]
- Takes in: DESIGNED — A reading attempt whose available context cannot support a sufficient interpretation. [DD §3D]
- Does: DESIGNED — Writes an honest insufficient-context reading and marks it revisable. [DD §3D]
- Gives out: DESIGNED — A revisable reading that states the context limitation. [DD §3D]
- Must never: DESIGNED — Invent a sufficient interpretation to conceal insufficient context. [DD §3D]
- Fails closed by: DESIGNED — Retaining the honest insufficient-context result instead of pretending the gap is resolved. [DD §3D]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-GOLD.4.3 — Invention and omission: insufficient context cannot justify an invented reading. [DD §3D]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-GOLD — Sealed gold sets v1, v2-B (§7C) | A reading attempt whose available context cannot support a sufficient interpretation. | insufficient context requires an honest revisable reading. | A revisable reading that states the context limitation. | [DD §3D] |

SUB-PARTS: NONE

### C-GOLD.6 — Protected engine build order
Stamp: DESIGNED    Source: [V10 §7C] [MAP C-GOLD] [DD §3D]

ALONE
- What it is: DESIGNED — The ordering and benchmark constraints on later engine work. [V10 §7C] [MAP C-GOLD]
- Takes in: DESIGNED — A proposed Engine C test, nightly deepening build, wider-thread setup or replacement mouth. [V10 §7C] [DD §3D]
- Does: DESIGNED — Requires story-bearing gold before Engine C tests, the live path before nightly deepening, and benchmark evidence before assuming wider-thread performance. A new mouth must pass through testing against both sealed sets before replacement; old readings retain old `produced_by` and no automatic mass reread follows. [V10 §7C] [DD §3D]
- Does: DECIDED-2026-09-25 — Annotation and sealing may proceed in parallel with validator and writer development once the format and scoring are fixed; both come before engine-versus-gold comparison. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md FR-0124]
- Gives out: DESIGNED — Ordered prerequisites for those later changes, without authorizing construction. [MAP C-GOLD]
- Must never: DESIGNED — Skip the story-gold prerequisite, put nightly deepening before the live path, assume a bigger context/model works without benchmarking, rewrite old producer identity or trigger a mass reread automatically. [MAP C-GOLD] [DD §3D]
- Fails closed by: DESIGNED — Keeping Engine C tests gated until story-bearing gold exists. [V10 §7C]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-GOLD.6.1 — Story gold before Engine C: a story-layer test needs its own story-bearing cases. [V10 §7C]
- Gated by: DESIGNED — C-GOLD.6.2 — Live before nightly: the live path must precede nightly deepening. [V10 §7C]
- Gated by: DESIGNED — C-GOLD.6.3 — Benchmark before wider-reading claims: larger-model/context capability remains an empirical question. [V10 §7C]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-GOLD — Sealed gold sets v1, v2-B (§7C) | A proposed Engine C test, nightly deepening build, wider-thread setup or replacement mouth. | Engine C requires story-bearing gold and wider reading requires benchmark evidence. | Ordered prerequisites for those later changes, without authorizing construction. | [MAP C-GOLD] [V10 §7C] [DD §3D] |

SUB-PARTS: C-GOLD.6.1 — Story gold before Engine C; C-GOLD.6.2 — Live before nightly; C-GOLD.6.3 — Benchmark before wider-reading claims

### C-GOLD.6.1 — Story gold before Engine C
Stamp: DESIGNED    Source: [V10 §7C]

ALONE
- What it is: DESIGNED — Engine C's story-bearing evaluation prerequisite. [V10 §7C]
- Takes in: DESIGNED — A proposed test of `story_layer` reading. [V10 §7C]
- Does: DESIGNED — Requires story-bearing gold cases first. [V10 §7C]
- Gives out: DESIGNED — A test boundary that v1/v2-B meaning-only grading does not satisfy. [V10 §7C] [DD §3D]
- Must never: DESIGNED — Test Engine C as though legacy ungraded story output supplied its gold standard. [V10 §7C] [DD §3D]
- Fails closed by: DESIGNED — Leaving Engine C testing blocked while story-bearing gold is unavailable. [V10 §7C]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8 — A1 replacement story-gold: supplies accepted content while root pinning and executable benchmark preparation remain deferred. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §5] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-GOLD.8.2 — Legitimate root pinning: the replacement content cannot supply a runnable Engine C test while its cases remain unpinned. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-GOLD.6 — Protected engine build order | A proposed test of `story_layer` reading. | a story-layer test needs its own story-bearing cases. | A test boundary that v1/v2-B meaning-only grading does not satisfy. | [V10 §7C] [DD §3D] |

SUB-PARTS: NONE

### C-GOLD.6.2 — Live before nightly
Stamp: DESIGNED    Source: [V10 §7C]

ALONE
- What it is: DESIGNED — The ordering constraint between the live path and nightly deepening. [V10 §7C]
- Takes in: DESIGNED — Proposed nightly deepening construction. [V10 §7C]
- Does: DESIGNED — Requires the live path to be built first. [V10 §7C]
- Gives out: DESIGNED — A later-build dependency, not a coding trigger. [MAP C-GOLD]
- Must never: DESIGNED — Build nightly deepening ahead of the live path. [V10 §7C]
- Fails closed by: DESIGNED — Nightly deepening is not built before the live path exists. [V10 §7C]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): the live path is the prerequisite that must be built before nightly deepening. [V10 §7C]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-GOLD.6 — Protected engine build order | Proposed nightly deepening construction. | the live path must precede nightly deepening. | A later-build dependency, not a coding trigger. | [V10 §7C] [MAP C-GOLD] |

SUB-PARTS: NONE

### C-GOLD.6.3 — Benchmark before wider-reading claims
Stamp: DESIGNED    Source: [V10 §7C] [DD §3D]

ALONE
- What it is: DESIGNED — The evidence requirement for wider/full-thread reading and a replacement mouth. [V10 §7C] [DD §3D]
- Takes in: DESIGNED — A larger-model/larger-context setup or new mouth candidate. [V10 §7C] [DD §3D]
- Does: DESIGNED — Requires actual wider-reading benchmarking and tests a new mouth against both sealed gold sets before replacement. [V10 §7C] [DD §3D]
- Gives out: DESIGNED — Benchmark evidence about the tested setup, without a promise of 7/7. [V10 §11 item 20]
- Must never: DESIGNED — Assume full-thread capability, infer the cause of B3's miss without isolation, overwrite old `produced_by`, or start a mass reread merely because the mouth changes. [V10 §7C] [V10 §11 item 20] [DD §3D]
- Fails closed by: DESIGNED — Without actual wider-reading benchmarking against both sealed gold sets, no full-thread capability is claimed and the mouth is not replaced. [V10 §7C] [DD §3D] [V10 §11 item 20]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-GOLD.4 — Six gold scoring rules: both legacy exams retain their own settled judgment rules under a new setup. [DD §3D]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-GOLD.6 — Protected engine build order | A larger-model/larger-context setup or new mouth candidate. | larger-model/context capability remains an empirical question. | Benchmark evidence about the tested setup, without a promise of 7/7. | [V10 §7C] [DD §3D] [V10 §11 item 20] |

SUB-PARTS: NONE

### C-GOLD.7 — Gold operation records
Stamp: DESIGNED    Source: [MAP C-GOLD] [V10 §0B]

ALONE
- What it is: DESIGNED — Mandatory records of each gold-evaluation run and Ness's case judgments. [MAP C-GOLD]
- Takes in: DESIGNED — The actual evaluation or judgment operation, with annotator, when, context-version and change-reason metadata. [MAP C-GOLD]
- Does: DESIGNED — Keeps one permanent, connected, append-only log per real operation. Merely making a log does not automatically make another log about it; a genuinely separate later operation has its own record. [V10 §0B]
- Gives out: DESIGNED — Traceable evaluation and judgment records, subject to privacy and identity/security authorization. The sealed sets remain unchanged. [MAP C-GOLD] [V10 §0B]
- Must never: DESIGNED — Run silently, destroy the operation record, count logging as independent support for the underlying claim, create an automatic infinite log chain, or treat record existence as permission to access protected content. [V10 §0B]
- Fails closed by: DESIGNED — Treating a component without traceable connected operation records as incomplete and prohibiting its adoption. [V10 §0B]

TOGETHER
- Fed by: DESIGNED — C-GOLD.7.1 — annotator: identifies who supplied the judgment annotation. [MAP C-GOLD]
- Fed by: DESIGNED — C-GOLD.7.2 — when: supplies the annotation time. [MAP C-GOLD]
- Fed by: DESIGNED — C-GOLD.7.3 — context_version: identifies the judgment's context version. [MAP C-GOLD]
- Fed by: DESIGNED — C-GOLD.7.4 — change_reason: records why a judgment annotation changes. [MAP C-GOLD]
- Gated by: DESIGNED — C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B): shared living-record rules require traceable operations without automatic recursive logging or double evidence. [V10 §0B]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): record use remains subject to protection and access authorization; permanent recording grants no automatic access. [MAP C-GOLD] [V10 §0B]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-GOLD — Sealed gold sets v1, v2-B (§7C) | The actual evaluation or judgment operation, with annotator, when, context-version and change-reason metadata. | each evaluation and judgment requires a permanent operation record. | Traceable evaluation and judgment records, subject to privacy and identity/security authorization. The sealed sets remain unchanged. | [MAP C-GOLD] [V10 §0B] |

SUB-PARTS: C-GOLD.7.1 — annotator; C-GOLD.7.2 — when; C-GOLD.7.3 — context_version; C-GOLD.7.4 — change_reason

### C-GOLD.7.1 — annotator
Stamp: DESIGNED    Source: [MAP C-GOLD]

ALONE
- What it is: DESIGNED — The identity metadata on a gold judgment annotation. [MAP C-GOLD]
- Takes in: DESIGNED — The annotation's author. [MAP C-GOLD]
- Does: DESIGNED — Records the annotator alongside the judgment. [MAP C-GOLD]
- Gives out: DESIGNED — Named annotation provenance; Ness's gold authoring/judging is `human_annotation`. [MAP C-GOLD]
- Must never: DESIGNED — Turn a model's assistance into a model-owned pass/fail judgment. [MAP C-GOLD]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-GOLD.4.6 — Ness-owned pass/fail: the annotator metadata cannot transfer gold judging authority to a model. [MAP C-GOLD]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-GOLD.7 — Gold operation records | The annotation's author. | identifies who supplied the judgment annotation. | Named annotation provenance; Ness's gold authoring/judging is `human_annotation`. | [MAP C-GOLD] |

SUB-PARTS: NONE

### C-GOLD.7.2 — when
Stamp: DESIGNED    Source: [MAP C-GOLD]

ALONE
- What it is: DESIGNED — The required time metadata for a gold judgment. [MAP C-GOLD]
- Takes in: DESIGNED — When the annotation was made. [MAP C-GOLD]
- Does: DESIGNED — Preserves that time with the judgment record. [MAP C-GOLD]
- Gives out: DESIGNED — The judgment's recorded annotation time. [MAP C-GOLD]
- Must never: DESIGNED — Omit the required time from a judgment's operation record. [MAP C-GOLD]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-GOLD.7 — Gold operation records | When the annotation was made. | supplies the annotation time. | The judgment's recorded annotation time. | [MAP C-GOLD] |

SUB-PARTS: NONE

### C-GOLD.7.3 — context_version
Stamp: DESIGNED    Source: [MAP C-GOLD]

ALONE
- What it is: DESIGNED — The context-version metadata required alongside a gold judgment. [MAP C-GOLD]
- Takes in: DESIGNED — The context version used for the annotation. [MAP C-GOLD]
- Does: DESIGNED — Retains the judgment's context-version provenance. [MAP C-GOLD]
- Gives out: DESIGNED — The recorded context version, without replacing the sealed case. [MAP C-GOLD]
- Must never: DESIGNED — Drop context-version provenance or alter sealed input to fit a judgment. [MAP C-GOLD]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-GOLD.7 — Gold operation records | The context version used for the annotation. | identifies the judgment's context version. | The recorded context version, without replacing the sealed case. | [MAP C-GOLD] |

SUB-PARTS: NONE

### C-GOLD.7.4 — change_reason
Stamp: DESIGNED    Source: [MAP C-GOLD]

ALONE
- What it is: DESIGNED — The reason metadata for a changed judgment annotation. [MAP C-GOLD]
- Takes in: DESIGNED — The reason for the annotation change. [MAP C-GOLD]
- Does: DESIGNED — Preserves that reason with the recorded change. [MAP C-GOLD]
- Gives out: DESIGNED — A traceable change reason in judgment provenance. [MAP C-GOLD]
- Must never: DESIGNED — Make an unrecorded judgment change or use it to rewrite a sealed case. [MAP C-GOLD] [V10 §0B]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-GOLD.7 — Gold operation records | The reason for the annotation change. | records why a judgment annotation changes. | A traceable change reason in judgment provenance. | [MAP C-GOLD] |

SUB-PARTS: NONE

### C-GOLD.8 — A1 replacement story-gold
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md §5] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The complete eight-case replacement story-bearing content for Engine C, with frozen contexts, proposed benchmark annotations, evidence relationships, firmness records, themes and invention boundaries. Its design is complete; it remains unpinned and is not an executable benchmark. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §5] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — A1-R01 through A1-R08, each grounded in the exact target and frozen conversational context recorded in the accepted content file. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §4]
- Does: ACCEPTED — Defines expected primary Story-Layer meanings and separately judged themes for ordinary Engine C reading. It creates no root, reading, telling, operation or idempotency identity. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — Accepted design content whose annotations retain proposed benchmark status. The design-provenance seal consists of frozen file identities; it is not a runtime `.sealed` marker or a store action. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md §5] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §5]
- Must never: ACCEPTED — Invent identities, run unpinned cases as an Engine C benchmark, create runtime themes from reference themes, alter either legacy sealed set, or treat the replacement as recovered historical A1 material. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §4] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Keeping cases unpinned and non-runnable until legitimate root pinning; root-store checks, pinning, ingest, runtime sealing, executable preparation, coding and testing require separate implementation authorization. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.1 — Frozen replacement-source identity: fixes the exact accepted content and its design-provenance boundary. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-GOLD.8.2 — Legitimate root pinning: only verified immutable roots can supply machine identities. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-GOLD.8.3 — Separate primary and theme grading: the two judgments must remain distinct. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Gated by: ACCEPTED — C-GOLD.8.4 — Shared story-case boundaries: every case uses only its frozen evidence and preserves the supported depth. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-GOLD.8.5 — Benchmark annotation fields: every case retains its named perspective, evidence, firmness, theme and provenance content. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD — Sealed gold sets v1, v2-B (§7C) | A1-R01 through A1-R08, each grounded in the exact target and frozen conversational context recorded in the accepted content file. | provides accepted unpinned story-bearing benchmark content, subject to its separate runtime prerequisites. | Accepted design content whose annotations retain proposed benchmark status. The design-provenance seal consists of frozen file identities; it is not a runtime `.sealed` marker or a store action. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §5] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §7] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §4] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md §5] |
| 2 · ACCEPTED | C-GOLD.6.1 — Story gold before Engine C | A1-R01 through A1-R08, each grounded in the exact target and frozen conversational context recorded in the accepted content file. | supplies accepted content while root pinning and executable benchmark preparation remain deferred. | Accepted design content whose annotations retain proposed benchmark status. The design-provenance seal consists of frozen file identities; it is not a runtime `.sealed` marker or a store action. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §5] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §7] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §4] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md §5] |

SUB-PARTS: C-GOLD.8.1 — Frozen replacement-source identity; C-GOLD.8.2 — Legitimate root pinning; C-GOLD.8.3 — Separate primary and theme grading; C-GOLD.8.4 — Shared story-case boundaries; C-GOLD.8.5 — Benchmark annotation fields; C-GOLD.8.6 — A1-R01 — Forced explanation of an unseen inner process; C-GOLD.8.7 — A1-R02 — Use the whole accumulated conversation; C-GOLD.8.8 — A1-R03 — Lifelong active trauma while still seeking help; C-GOLD.8.9 — A1-R04 — Ongoing source, non-linear processing, and minimization; C-GOLD.8.10 — A1-R05 — Collapse as overload while pushing beyond bodily limits to reach help; C-GOLD.8.11 — A1-R06 — Explain the mechanism instead of naming the gap; C-GOLD.8.12 — A1-R07 — Thorough analysis instead of sweet talk; C-GOLD.8.13 — A1-R08 — Explanation rather than defence against judgment

### C-GOLD.8.1 — Frozen replacement-source identity
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The design-provenance seal over the exact accepted replacement content and its acceptance record. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — `NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md`, SHA-256 `5ab67191ff57e532e88193008fe0ec5652f72cc6608316f48b99555e54639850`, 1,102 lines and 64,974 bytes; its acceptance record v1_1, SHA-256 `40ed4f5ec457f03bb5bcb233e9ec0f05c36947fc2f8307c38e1ef826e4fb682d`, 191 lines and 9,459 bytes. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Keeps the exact accepted content identity fixed. All eight targets, frozen contexts and annotations belong to that identity. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §5] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — A design identity distinct from a runtime `.sealed` file. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §5]
- Must never: ACCEPTED — Mutate the accepted bytes in place, infer runtime sealing from the design seal, or claim that the missing historical set has been recovered. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §6] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8 — A1 replacement story-gold | `NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md`, SHA-256 `5ab67191ff57e532e88193008fe0ec5652f72cc6608316f48b99555e54639850`, 1,102 lines and 64,974 bytes; its acceptance record v1_1, SHA-256 `40ed4f5ec457f03bb5bcb233e9ec0f05c36947fc2f8307c38e1ef826e4fb682d`, 191 lines and 9,459 bytes. | fixes the exact accepted content and its design-provenance boundary. | A design identity distinct from a runtime `.sealed` file. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §6] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-GOLD.8.2 — Legitimate root pinning
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The conditional route from an unpinned case to verified machine root identities. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Takes in: ACCEPTED — The case's exact target text, PDF page/source location and frozen contextual turns. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Does: ACCEPTED — Pins to verified immutable IDs when the target and contextual turns already exist in a legitimate sealed batch. Otherwise the case stays unpinned until separately authorized ingest through the active writable-batch architecture supplies legitimate roots. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Gives out: ACCEPTED — Verified root references on the existing-root branch, or continued unpinned status on the missing-root branch. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Must never: ACCEPTED — Use fake IDs, temporary UUIDs, inferred IDs, ChatGPT message IDs, PDF-page IDs or root-like placeholders as N.H root identities; create telling, reading, operation or idempotency IDs from case labels; reopen, unseal, rewrite or append to the sealed 5,521-root batch. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Keeping the case unpinned and non-runnable when legitimate root identities are unavailable. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.5.2 — Unpinned source anchor: supplies exact target text and PDF source location rather than a fabricated root ID. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-GOLD.8.2.1 — Pin verified existing roots: supplies verified references when all required turns already exist as legitimate roots. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-GOLD.8.2.2 — Keep missing-root cases unpinned: preserves unpinned status until separately authorized active-batch ingest supplies missing roots. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Gated by: ACCEPTED — Ness's separate implementation authorization is required for root-store checks, assignment, pinning and any ingest. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.6.1 — Story gold before Engine C | The case's exact target text, PDF page/source location and frozen contextual turns. | the replacement content cannot supply a runnable Engine C test while its cases remain unpinned. | Verified root references on the existing-root branch, or continued unpinned status on the missing-root branch. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-GOLD.8 — A1 replacement story-gold | The case's exact target text, PDF page/source location and frozen contextual turns. | only verified immutable roots can supply machine identities. | Verified root references on the existing-root branch, or continued unpinned status on the missing-root branch. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-GOLD.8.2.1 — Pin verified existing roots | The case's exact target text, PDF page/source location and frozen contextual turns. | separately authorized verification must establish that target and contextual turns already exist in a legitimate sealed batch. | Verified root references on the existing-root branch, or continued unpinned status on the missing-root branch. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §7] |
| 4 · ACCEPTED | C-GOLD.8.2.2 — Keep missing-root cases unpinned | The case's exact target text, PDF page/source location and frozen contextual turns. | this branch cannot advance until the missing source turns receive legitimate roots through separately authorized active-batch ingest. | Verified root references on the existing-root branch, or continued unpinned status on the missing-root branch. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] |
| 5 · ACCEPTED | C-GOLD.8.5.12 — Benchmark annotation provenance | The case's exact target text, PDF page/source location and frozen contextual turns. | unpinned content cannot be used as a runnable benchmark. | Verified root references on the existing-root branch, or continued unpinned status on the missing-root branch. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] |
| 6 · ACCEPTED | C-GOLD.8.6 — A1-R01 — Forced explanation of an unseen inner process | The case's exact target text, PDF page/source location and frozen contextual turns. | the benchmark label and page anchor confer no runtime root identity. | Verified root references on the existing-root branch, or continued unpinned status on the missing-root branch. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] |
| 7 · ACCEPTED | C-GOLD.8.7 — A1-R02 — Use the whole accumulated conversation | The case's exact target text, PDF page/source location and frozen contextual turns. | no runtime identity may be inferred from the content label. | Verified root references on the existing-root branch, or continued unpinned status on the missing-root branch. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] |
| 8 · ACCEPTED | C-GOLD.8.8 — A1-R03 — Lifelong active trauma while still seeking help | The case's exact target text, PDF page/source location and frozen contextual turns. | no runtime test is permitted from the unpinned case. | Verified root references on the existing-root branch, or continued unpinned status on the missing-root branch. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] |
| 9 · ACCEPTED | C-GOLD.8.9 — A1-R04 — Ongoing source, non-linear processing, and minimization | The case's exact target text, PDF page/source location and frozen contextual turns. | this label remains unpinned and non-runnable. | Verified root references on the existing-root branch, or continued unpinned status on the missing-root branch. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] |
| 10 · ACCEPTED | C-GOLD.8.10 — A1-R05 — Collapse as overload while pushing beyond bodily limits to reach help | The case's exact target text, PDF page/source location and frozen contextual turns. | restored text and a page anchor do not establish machine identities. | Verified root references on the existing-root branch, or continued unpinned status on the missing-root branch. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] |
| 11 · ACCEPTED | C-GOLD.8.11 — A1-R06 — Explain the mechanism instead of naming the gap | The case's exact target text, PDF page/source location and frozen contextual turns. | page location and benchmark label provide no runtime identity. | Verified root references on the existing-root branch, or continued unpinned status on the missing-root branch. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] |
| 12 · ACCEPTED | C-GOLD.8.12 — A1-R07 — Thorough analysis instead of sweet talk | The case's exact target text, PDF page/source location and frozen contextual turns. | a verified page location and undamaged source characters are not machine IDs. | Verified root references on the existing-root branch, or continued unpinned status on the missing-root branch. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] |
| 13 · ACCEPTED | C-GOLD.8.13 — A1-R08 — Explanation rather than defence against judgment | The case's exact target text, PDF page/source location and frozen contextual turns. | the unpinned case cannot yet be run against Engine C. | Verified root references on the existing-root branch, or continued unpinned status on the missing-root branch. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] |

SUB-PARTS: C-GOLD.8.2.1 — Pin verified existing roots; C-GOLD.8.2.2 — Keep missing-root cases unpinned

### C-GOLD.8.2.1 — Pin verified existing roots
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The pinning branch for source turns already held as legitimate roots. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Takes in: ACCEPTED — A target and its contextual turns whose immutable root identities have been verified in a legitimate sealed batch. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Does: ACCEPTED — Pins the case to those verified immutable root IDs. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Gives out: ACCEPTED — Real root references for the case's existing target and context. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Must never: ACCEPTED — Guess an ID or change the sealed batch to make a source turn fit. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Leaving the case unpinned without the required verified roots. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.8.2 — Legitimate root pinning: separately authorized verification must establish that target and contextual turns already exist in a legitimate sealed batch. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.2 — Legitimate root pinning | A target and its contextual turns whose immutable root identities have been verified in a legitimate sealed batch. | supplies verified references when all required turns already exist as legitimate roots. | Real root references for the case's existing target and context. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-GOLD.8.2.2 — Keep missing-root cases unpinned
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The branch where the source turns do not already exist as legitimate roots. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Takes in: ACCEPTED — A case whose target or contextual turns lack existing legitimate root identities. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Does: ACCEPTED — Retains unpinned status until a separately authorized future ingest through the active writable-batch route creates legitimate roots. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Gives out: ACCEPTED — A still-unpinned case pending that ingest, with no authority to append to the old sealed batch. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Must never: ACCEPTED — Manufacture placeholders, ingest without separate authorization, or reopen, unseal, rewrite or append to the sealed 5,521-root batch. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Blocking runtime case use while root pinning remains incomplete. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.8.2 — Legitimate root pinning: this branch cannot advance until the missing source turns receive legitimate roots through separately authorized active-batch ingest. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-STORE — Accretive store & sealed roots (§6B): future root creation uses the accepted B11 active writable-batch architecture; the existing sealed batch is immutable. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.2 — Legitimate root pinning | A case whose target or contextual turns lack existing legitimate root identities. | preserves unpinned status until separately authorized active-batch ingest supplies missing roots. | A still-unpinned case pending that ingest, with no authority to append to the old sealed batch. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-GOLD.8.3 — Separate primary and theme grading
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]

ALONE
- What it is: ACCEPTED — A1's two-result grading structure. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Takes in: ACCEPTED — The primary Story-Layer result and the theme result for one replacement case. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Does: ACCEPTED — Judges the primary result together and themes separately. A case can pass both, pass primary but miss theme, miss primary but land near theme, or fail both. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Gives out: ACCEPTED — Two distinct case judgments, with no hidden combined score or single undifferentiated verdict. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Must never: ACCEPTED — Combine the two results, invent a score or threshold, or retroactively add story grading to v1/v2-B. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.3.1 — Primary Story-Layer result: supplies the jointly judged telling, perspective, evidence and firmness content. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Fed by: ACCEPTED — C-GOLD.8.3.2 — Theme result: supplies the independently judged theme meaning. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Gated by: DESIGNED — C-GOLD.4 — Six gold scoring rules: the additional A1 structure preserves the six governing gold rules. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.1] [DD §3D]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8 — A1 replacement story-gold | The primary Story-Layer result and the theme result for one replacement case. | the two judgments must remain distinct. | Two distinct case judgments, with no hidden combined score or single undifferentiated verdict. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] |
| 2 · ACCEPTED | C-GOLD.8.3.1 — Primary Story-Layer result | The primary Story-Layer result and the theme result for one replacement case. | the telling, perspective, evidence relationship and firmness are judged together, independently of theme success. | Two distinct case judgments, with no hidden combined score or single undifferentiated verdict. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] |
| 3 · ACCEPTED | C-GOLD.8.3.2 — Theme result | The primary Story-Layer result and the theme result for one replacement case. | the semantic theme judgment cannot be combined with the primary result. | Two distinct case judgments, with no hidden combined score or single undifferentiated verdict. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] |

SUB-PARTS: C-GOLD.8.3.1 — Primary Story-Layer result; C-GOLD.8.3.2 — Theme result

### C-GOLD.8.3.1 — Primary Story-Layer result
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]

ALONE
- What it is: ACCEPTED — The jointly evaluated primary result of a story-gold case. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Takes in: ACCEPTED — The telling or tellings, structured perspective, evidence relationship, firmness label and firmness evidence basis. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Does: ACCEPTED — Judges those elements together against the case's source-supported benchmark annotations and failure boundaries. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]
- Gives out: ACCEPTED — A primary result distinct from theme success or failure. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Must never: ACCEPTED — Substitute a near theme for a correct primary result. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Fails closed by: ACCEPTED — Failing the primary result when a case's listed invention/failure boundary is crossed. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.8.4 — Shared story-case boundaries: only the available frozen evidence may support the primary result. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-GOLD.8.3 — Separate primary and theme grading: the telling, perspective, evidence relationship and firmness are judged together, independently of theme success. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.3 — Separate primary and theme grading | The telling or tellings, structured perspective, evidence relationship, firmness label and firmness evidence basis. | supplies the jointly judged telling, perspective, evidence and firmness content. | A primary result distinct from theme success or failure. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] |

SUB-PARTS: NONE

### C-GOLD.8.3.2 — Theme result
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]

ALONE
- What it is: ACCEPTED — The separately graded theme meaning of an A1 case. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Takes in: ACCEPTED — A proposed theme and the case's source-supported benchmark theme reference. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Does: ACCEPTED — Compares meaning semantically; exact wording is unnecessary, but a shallow label fails when it loses an important part of the supported theme. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Gives out: ACCEPTED — A theme result independent of the primary judgment and with no runtime theme creation or confirmation. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Must never: ACCEPTED — Convert a gold reference into a live theme record or fact, confirm it through repetition/time, or merge the theme verdict into the primary result. Only Ness's response confirms an operational theme under its separate design. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Fails closed by: ACCEPTED — Failing a theme label that loses an important supported part. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.10.14.8.7 — Confirmation remains separate: a benchmark reference grants no operational theme confirmation. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Gated by: ACCEPTED — C-GOLD.8.3 — Separate primary and theme grading: the semantic theme judgment cannot be combined with the primary result. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.3 — Separate primary and theme grading | A proposed theme and the case's source-supported benchmark theme reference. | supplies the independently judged theme meaning. | A theme result independent of the primary judgment and with no runtime theme creation or confirmation. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] |
| 2 · ACCEPTED | C-GOLD.8.5.9 — Proposed theme reference | A proposed theme and the case's source-supported benchmark theme reference. | semantic comparison and independent grading govern each reference. | A theme result independent of the primary judgment and with no runtime theme creation or confirmation. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] |

SUB-PARTS: NONE

### C-GOLD.8.4 — Shared story-case boundaries
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The evidence and interpretation rules governing all eight replacement cases. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The target and whole relevant frozen context, kept distinct; no later conversational material is available to an earlier case. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Preserves the maximum supported depth while keeping each telling local, bounded, from one perspective at one moment. It distinguishes root speaker, subject and perspective owner; records evidence relationship for each telling; treats firmness as apparent strength of stance, not truth; and permits zero, one or several genuinely supported navigational themes. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — Ordinary Engine C story readings grounded in the frozen evidence, including the everyday instruction in A1-R02 without turning it into CY-F. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Omit relevant frozen context, import later turns, flatten supported meaning merely to shorten a label, invent depth/motive/diagnosis/inner state/causation, collapse perspective roles, omit a telling's evidence relationship, treat an observation as direct access to another person's mind, equate firmness with truth, make themes facts, or use an earlier interpretation as circular proof of a new telling. None of these cases tests the formal reread cycle. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Failing invented primary content under the case's explicit failure boundaries. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.8.5.4 — Frozen context: the entire recorded span bounds the evidence available for this case. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-GOLD.8.5.8 — Benchmark firmness and basis: apparent stance strength needs a source-grounded basis and never determines truth. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8 — A1 replacement story-gold | The target and whole relevant frozen context, kept distinct; no later conversational material is available to an earlier case. | every case uses only its frozen evidence and preserves the supported depth. | Ordinary Engine C story readings grounded in the frozen evidence, including the everyday instruction in A1-R02 without turning it into CY-F. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-GOLD.8.3.1 — Primary Story-Layer result | The target and whole relevant frozen context, kept distinct; no later conversational material is available to an earlier case. | only the available frozen evidence may support the primary result. | Ordinary Engine C story readings grounded in the frozen evidence, including the everyday instruction in A1-R02 without turning it into CY-F. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] |
| 3 · ACCEPTED | C-GOLD.8.5 — Benchmark annotation fields | The target and whole relevant frozen context, kept distinct; no later conversational material is available to an earlier case. | every field remains bounded by the case's frozen evidence. | Ordinary Engine C story readings grounded in the frozen evidence, including the everyday instruction in A1-R02 without turning it into CY-F. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] |
| 4 · ACCEPTED | C-GOLD.8.5.7 — Proposed telling | The target and whole relevant frozen context, kept distinct; no later conversational material is available to an earlier case. | a telling cannot exceed or circularly manufacture its source support. | Ordinary Engine C story readings grounded in the frozen evidence, including the everyday instruction in A1-R02 without turning it into CY-F. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] |
| 5 · ACCEPTED | C-GOLD.8.5.11 — Invention and failure boundary | The target and whole relevant frozen context, kept distinct; no later conversational material is available to an earlier case. | the common evidence limits remain in force alongside the particular case failures. | Ordinary Engine C story readings grounded in the frozen evidence, including the everyday instruction in A1-R02 without turning it into CY-F. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] |
| 6 · ACCEPTED | C-GOLD.8.6 — A1-R01 — Forced explanation of an unseen inner process | The target and whole relevant frozen context, kept distinct; no later conversational material is available to an earlier case. | only this complete frozen context and target may support the reading. | Ordinary Engine C story readings grounded in the frozen evidence, including the everyday instruction in A1-R02 without turning it into CY-F. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] |
| 7 · ACCEPTED | C-GOLD.8.7 — A1-R02 — Use the whole accumulated conversation | The target and whole relevant frozen context, kept distinct; no later conversational material is available to an earlier case. | the frozen input alone supports this ordinary Engine C test. | Ordinary Engine C story readings grounded in the frozen evidence, including the everyday instruction in A1-R02 without turning it into CY-F. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] |
| 8 · ACCEPTED | C-GOLD.8.8 — A1-R03 — Lifelong active trauma while still seeking help | The target and whole relevant frozen context, kept distinct; no later conversational material is available to an earlier case. | source self-description cannot become an independent clinical assertion. | Ordinary Engine C story readings grounded in the frozen evidence, including the everyday instruction in A1-R02 without turning it into CY-F. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03] |
| 9 · ACCEPTED | C-GOLD.8.9 — A1-R04 — Ongoing source, non-linear processing, and minimization | The target and whole relevant frozen context, kept distinct; no later conversational material is available to an earlier case. | neither apparent certainty nor contextual interpretation grants direct access to others' minds. | Ordinary Engine C story readings grounded in the frozen evidence, including the everyday instruction in A1-R02 without turning it into CY-F. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] |
| 10 · ACCEPTED | C-GOLD.8.10 — A1-R05 — Collapse as overload while pushing beyond bodily limits to reach help | The target and whole relevant frozen context, kept distinct; no later conversational material is available to an earlier case. | the preserved source supports no additional intent, diagnosis or outcome. | Ordinary Engine C story readings grounded in the frozen evidence, including the everyday instruction in A1-R02 without turning it into CY-F. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] |
| 11 · ACCEPTED | C-GOLD.8.11 — A1-R06 — Explain the mechanism instead of naming the gap | The target and whole relevant frozen context, kept distinct; no later conversational material is available to an earlier case. | source-specified method cannot become an invented motive. | Ordinary Engine C story readings grounded in the frozen evidence, including the everyday instruction in A1-R02 without turning it into CY-F. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] |
| 12 · ACCEPTED | C-GOLD.8.12 — A1-R07 — Thorough analysis instead of sweet talk | The target and whole relevant frozen context, kept distinct; no later conversational material is available to an earlier case. | the bounded correction cannot become a universal claim about tone or character. | Ordinary Engine C story readings grounded in the frozen evidence, including the everyday instruction in A1-R02 without turning it into CY-F. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] |
| 13 · ACCEPTED | C-GOLD.8.13 — A1-R08 — Explanation rather than defence against judgment | The target and whole relevant frozen context, kept distinct; no later conversational material is available to an earlier case. | the purpose contrast supports no diagnosis, self-harm inference or rejection of safety assessment. | Ordinary Engine C story readings grounded in the frozen evidence, including the everyday instruction in A1-R02 without turning it into CY-F. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08] |

SUB-PARTS: NONE

### C-GOLD.8.5 — Benchmark annotation fields
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The content carried by every proposed benchmark case annotation, without creating a runtime telling record. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]
- Takes in: ACCEPTED — Case identifier, source anchor, exact target, exact frozen context, structured perspective, evidence relationships, proposed tellings, firmness and evidence basis, theme references, acceptable alternatives, failure boundaries and provenance status. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]
- Does: ACCEPTED — Keeps these case-specific values associated with their frozen source. Machine-level telling identity remains governed by the separate telling-object contract and is not assigned to benchmark labels. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]
- Gives out: ACCEPTED — Proposed benchmark annotations for the two-result comparison, with no live-record side effect. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]
- Must never: ACCEPTED — Label the unpinned annotation `human_annotation`, manufacture machine identities, or treat reference themes as runtime records. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.5.1 — Case identifier: supplies a benchmark-content label only. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-GOLD.8.5.2 — Unpinned source anchor: identifies the exact target's source location. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-GOLD.8.5.3 — Exact target: carries the preserved target turn. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-GOLD.8.5.4 — Frozen context: carries the preserved contextual span. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-GOLD.8.5.5 — Structured benchmark perspective: separates speaker, subject, perspective owner and attribution. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-GOLD.8.5.6 — Benchmark evidence relationship: classifies each telling within the fixed five-value vocabulary. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.3]
- Fed by: ACCEPTED — C-GOLD.8.5.7 — Proposed telling: carries each supported local meaning. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Fed by: ACCEPTED — C-GOLD.8.5.8 — Benchmark firmness and basis: supplies the apparent stance strength and its source-grounded support. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §9]
- Fed by: ACCEPTED — C-GOLD.8.5.9 — Proposed theme reference: supplies the separately graded theme meaning. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Fed by: ACCEPTED — C-GOLD.8.5.10 — Acceptable alternative: preserves supported semantic alternatives. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-GOLD.8.5.11 — Invention and failure boundary: supplies the case's explicit primary-result failures. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-GOLD.8.5.12 — Benchmark annotation provenance: keeps proposed annotations separate from gold stamping and live records. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]
- Gated by: ACCEPTED — C-GOLD.8.4 — Shared story-case boundaries: every field remains bounded by the case's frozen evidence. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8 — A1 replacement story-gold | Case identifier, source anchor, exact target, exact frozen context, structured perspective, evidence relationships, proposed tellings, firmness and evidence basis, theme references, acceptable alternatives, failure boundaries and provenance status. | every case retains its named perspective, evidence, firmness, theme and provenance content. | Proposed benchmark annotations for the two-result comparison, with no live-record side effect. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] |
| 2 · ACCEPTED | C-GOLD.8.6.1 — A1-R01 telling 1 | Case identifier, source anchor, exact target, exact frozen context, structured perspective, evidence relationships, proposed tellings, firmness and evidence basis, theme references, acceptable alternatives, failure boundaries and provenance status. | this meaning, relationship and firmness basis remain proposed benchmark content. | Proposed benchmark annotations for the two-result comparison, with no live-record side effect. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] |
| 3 · ACCEPTED | C-GOLD.8.7.1 — A1-R02 telling 1 | Case identifier, source anchor, exact target, exact frozen context, structured perspective, evidence relationships, proposed tellings, firmness and evidence basis, theme references, acceptable alternatives, failure boundaries and provenance status. | the instruction uses the settled evidence vocabulary and proposed annotation status. | Proposed benchmark annotations for the two-result comparison, with no live-record side effect. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.3] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] |
| 4 · ACCEPTED | C-GOLD.8.8.1 — A1-R03 telling 1 | Case identifier, source anchor, exact target, exact frozen context, structured perspective, evidence relationships, proposed tellings, firmness and evidence basis, theme references, acceptable alternatives, failure boundaries and provenance status. | the proposed telling keeps its own relation and firmness annotation. | Proposed benchmark annotations for the two-result comparison, with no live-record side effect. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] |
| 5 · ACCEPTED | C-GOLD.8.8.2 — A1-R03 telling 2 | Case identifier, source anchor, exact target, exact frozen context, structured perspective, evidence relationships, proposed tellings, firmness and evidence basis, theme references, acceptable alternatives, failure boundaries and provenance status. | source-grounded relation and firmness remain attached to this separate telling. | Proposed benchmark annotations for the two-result comparison, with no live-record side effect. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] |
| 6 · ACCEPTED | C-GOLD.8.9.1 — A1-R04 telling 1 | Case identifier, source anchor, exact target, exact frozen context, structured perspective, evidence relationships, proposed tellings, firmness and evidence basis, theme references, acceptable alternatives, failure boundaries and provenance status. | this telling retains its own evidence relationship and firmness basis. | Proposed benchmark annotations for the two-result comparison, with no live-record side effect. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] |
| 7 · ACCEPTED | C-GOLD.8.9.2 — A1-R04 telling 2 | Case identifier, source anchor, exact target, exact frozen context, structured perspective, evidence relationships, proposed tellings, firmness and evidence basis, theme references, acceptable alternatives, failure boundaries and provenance status. | the proposed meaning cannot acquire an invented causal mechanism. | Proposed benchmark annotations for the two-result comparison, with no live-record side effect. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] |
| 8 · ACCEPTED | C-GOLD.8.10.1 — A1-R05 telling 1 | Case identifier, source anchor, exact target, exact frozen context, structured perspective, evidence relationships, proposed tellings, firmness and evidence basis, theme references, acceptable alternatives, failure boundaries and provenance status. | the local proposed meaning carries its own evidence relationship and firmness. | Proposed benchmark annotations for the two-result comparison, with no live-record side effect. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] |
| 9 · ACCEPTED | C-GOLD.8.10.2 — A1-R05 telling 2 | Case identifier, source anchor, exact target, exact frozen context, structured perspective, evidence relationships, proposed tellings, firmness and evidence basis, theme references, acceptable alternatives, failure boundaries and provenance status. | this remains a separate proposed telling with a source-grounded basis. | Proposed benchmark annotations for the two-result comparison, with no live-record side effect. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] |
| 10 · ACCEPTED | C-GOLD.8.10.3 — A1-R05 telling 3 | Case identifier, source anchor, exact target, exact frozen context, structured perspective, evidence relationships, proposed tellings, firmness and evidence basis, theme references, acceptable alternatives, failure boundaries and provenance status. | the proposed assessment meaning retains its individual evidence and firmness record. | Proposed benchmark annotations for the two-result comparison, with no live-record side effect. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] |
| 11 · ACCEPTED | C-GOLD.8.11.1 — A1-R06 telling 1 | Case identifier, source anchor, exact target, exact frozen context, structured perspective, evidence relationships, proposed tellings, firmness and evidence basis, theme references, acceptable alternatives, failure boundaries and provenance status. | the telling stays a separate source-bounded proposed annotation. | Proposed benchmark annotations for the two-result comparison, with no live-record side effect. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] |
| 12 · ACCEPTED | C-GOLD.8.11.2 — A1-R06 telling 2 | Case identifier, source anchor, exact target, exact frozen context, structured perspective, evidence relationships, proposed tellings, firmness and evidence basis, theme references, acceptable alternatives, failure boundaries and provenance status. | the supported method stays separate from unstated motivation. | Proposed benchmark annotations for the two-result comparison, with no live-record side effect. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] |
| 13 · ACCEPTED | C-GOLD.8.12.1 — A1-R07 telling 1 | Case identifier, source anchor, exact target, exact frozen context, structured perspective, evidence relationships, proposed tellings, firmness and evidence basis, theme references, acceptable alternatives, failure boundaries and provenance status. | the correction remains a bounded proposed telling with its own evidence and firmness. | Proposed benchmark annotations for the two-result comparison, with no live-record side effect. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] |
| 14 · ACCEPTED | C-GOLD.8.12.2 — A1-R07 telling 2 | Case identifier, source anchor, exact target, exact frozen context, structured perspective, evidence relationships, proposed tellings, firmness and evidence basis, theme references, acceptable alternatives, failure boundaries and provenance status. | this second telling retains separate proposed content and source support. | Proposed benchmark annotations for the two-result comparison, with no live-record side effect. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] |
| 15 · ACCEPTED | C-GOLD.8.13.1 — A1-R08 telling 1 | Case identifier, source anchor, exact target, exact frozen context, structured perspective, evidence relationships, proposed tellings, firmness and evidence basis, theme references, acceptable alternatives, failure boundaries and provenance status. | the purpose objection remains a separate proposed telling with its own evidence and firmness. | Proposed benchmark annotations for the two-result comparison, with no live-record side effect. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] |
| 16 · ACCEPTED | C-GOLD.8.13.2 — A1-R08 telling 2 | Case identifier, source anchor, exact target, exact frozen context, structured perspective, evidence relationships, proposed tellings, firmness and evidence basis, theme references, acceptable alternatives, failure boundaries and provenance status. | this distinct proposed telling retains its evidence relation and recorded firmness basis. | Proposed benchmark annotations for the two-result comparison, with no live-record side effect. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] |

SUB-PARTS: C-GOLD.8.5.1 — Case identifier; C-GOLD.8.5.2 — Unpinned source anchor; C-GOLD.8.5.3 — Exact target; C-GOLD.8.5.4 — Frozen context; C-GOLD.8.5.5 — Structured benchmark perspective; C-GOLD.8.5.6 — Benchmark evidence relationship; C-GOLD.8.5.7 — Proposed telling; C-GOLD.8.5.8 — Benchmark firmness and basis; C-GOLD.8.5.9 — Proposed theme reference; C-GOLD.8.5.10 — Acceptable alternative; C-GOLD.8.5.11 — Invention and failure boundary; C-GOLD.8.5.12 — Benchmark annotation provenance

### C-GOLD.8.5.1 — Case identifier
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — A benchmark-content label in the range A1-R01 through A1-R08. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Takes in: ACCEPTED — The selected replacement case. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]
- Does: ACCEPTED — Names that case without assigning an N.H machine identity. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Gives out: ACCEPTED — The case's stable benchmark label. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Must never: ACCEPTED — Serve as a root ID, telling ID, reading ID, operation ID or idempotency key. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.5 — Benchmark annotation fields | The selected replacement case. | supplies a benchmark-content label only. | The case's stable benchmark label. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-GOLD.8.5.2 — Unpinned source anchor
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The exact target text together with its PDF page/source location. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Takes in: ACCEPTED — The target's copied source span and page location in `New Text Document (3)(1).pdf`, a 27-page source. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §3] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Does: ACCEPTED — Locates the source while legitimate N.H target-root identity remains pending. R01 and R02 use the page-3 occurrence rather than the repeated exchange on pages 26–27. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §5] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Gives out: ACCEPTED — An unpinned source anchor, never a claim of root-store existence. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Must never: ACCEPTED — Convert a PDF page number or ChatGPT-export message ID into an N.H root ID. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.5.3 — Exact target: supplies the text half of the anchor. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.2 — Legitimate root pinning | The target's copied source span and page location in `New Text Document (3)(1).pdf`, a 27-page source. | supplies exact target text and PDF source location rather than a fabricated root ID. | An unpinned source anchor, never a claim of root-store existence. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §3] |
| 2 · ACCEPTED | C-GOLD.8.5 — Benchmark annotation fields | The target's copied source span and page location in `New Text Document (3)(1).pdf`, a 27-page source. | identifies the exact target's source location. | An unpinned source anchor, never a claim of root-store existence. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-GOLD.8.5.3 — Exact target
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The copied target turn from its first character to the start of the next turn. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §5]
- Takes in: ACCEPTED — The source's spelling, punctuation, capitalization, quote and dash styles, and line breaks. R05's target comes from the undamaged `Pasted text.txt` span and preserves `אבחון`; all other target spans come from the PDF text layer. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §5]
- Does: ACCEPTED — Preserves the source span without cleaning, correction, joining or reflow. Page-footer numbers and page breaks alone are excluded where a span crosses pages. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §5]
- Gives out: ACCEPTED — Exact target data, separate from surrounding conversational context. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §5] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Repair spelling, normalize punctuation, invent typographic emphasis or guess damaged characters. The PDF has one regular font and no bold/italic emphasis; its punctuation and extended spelling carry the preserved emphasis. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §5]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.5 — Benchmark annotation fields | The source's spelling, punctuation, capitalization, quote and dash styles, and line breaks. R05's target comes from the undamaged `Pasted text.txt` span and preserves `אבחון`; all other target spans come from the PDF text layer. | carries the preserved target turn. | Exact target data, separate from surrounding conversational context. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §5] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-GOLD.8.5.2 — Unpinned source anchor | The source's spelling, punctuation, capitalization, quote and dash styles, and line breaks. R05's target comes from the undamaged `Pasted text.txt` span and preserves `אבחון`; all other target spans come from the PDF text layer. | supplies the text half of the anchor. | Exact target data, separate from surrounding conversational context. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §5] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-GOLD.8.5.4 — Frozen context
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §5] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The complete copied relevant conversational span for one case, fixed before grading. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §5] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — Each relevant turn from its first source character, including opening export markers such as `Jun 27`, `7:01 PM` or `Thought for 5s`, until the next turn begins. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §5]
- Does: ACCEPTED — Preserves spelling, punctuation and line layout; excludes only intervening page footers/page breaks. R05's context and R07's context use exact undamaged companion spans, including `להתמוטט` and the Hebrew sentence, rather than the PDF's replacement characters. The companion source is SHA-256 `b2b4e38bd154bc6b063833ac77a3ba5a61f36d767f2beebb37fa18cf547894d4`, 777 lines and 60,515 bytes. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §3] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §5]
- Gives out: ACCEPTED — The whole relevant frozen context as evidence surrounding, but distinct from, the target. The PDF remains the page-location source for the restored spans. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §5] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Read only the target when context matters, import later conversation, flatten the source, guess Hebrew restoration, or treat a prior interpretation as circular proof of new content. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §5] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.4 — Shared story-case boundaries | Each relevant turn from its first source character, including opening export markers such as `Jun 27`, `7:01 PM` or `Thought for 5s`, until the next turn begins. | the entire recorded span bounds the evidence available for this case. | The whole relevant frozen context as evidence surrounding, but distinct from, the target. The PDF remains the page-location source for the restored spans. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §5] |
| 2 · ACCEPTED | C-GOLD.8.5 — Benchmark annotation fields | Each relevant turn from its first source character, including opening export markers such as `Jun 27`, `7:01 PM` or `Thought for 5s`, until the next turn begins. | carries the preserved contextual span. | The whole relevant frozen context as evidence surrounding, but distinct from, the target. The PDF remains the page-location source for the restored spans. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §5] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-GOLD.8.5.5 — Structured benchmark perspective
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The case's proposed structured perspective: `root_speaker`, `subject`, `perspective_owner` and `attribution_path`. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]
- Takes in: ACCEPTED — The source speaker, what the telling concerns, whose perspective it carries and any nested attribution. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]
- Does: ACCEPTED — Keeps those roles distinct even when they name the same person. All eight cases have `root_speaker = Ness`, `perspective_owner = Ness` and omitted `attribution_path` because their source has no nested attribution; the case-specific `subject` remains explicit. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]
- Gives out: ACCEPTED — A bounded proposed perspective for each local telling, not a universal account of another person's mind. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Collapse speaker, subject and perspective owner or replace honest omitted attribution with invented nesting. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.10.1.23 — Perspective roles stay distinct: common field definitions retain distinct roles rather than reducing them to a single “whose” value. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.5 — Benchmark annotation fields | The source speaker, what the telling concerns, whose perspective it carries and any nested attribution. | separates speaker, subject, perspective owner and attribution. | A bounded proposed perspective for each local telling, not a universal account of another person's mind. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-GOLD.8.5.6 — Benchmark evidence relationship
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.3]

ALONE
- What it is: ACCEPTED — The required evidence-relationship value for each proposed telling. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.3] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The telling's relationship to source evidence. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.3]
- Does: ACCEPTED — Uses exactly one of `direct self-report`, `direct quotation`, `reported speech`, `observation` or `engine inference`. Imperative targets in this set use `direct self-report`; R04 telling 3 uses `observation`, attributed to Ness's perception of conduct. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.3]
- Gives out: ACCEPTED — A per-telling evidence relationship within the accepted five-value vocabulary. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.3]
- Must never: ACCEPTED — Introduce a sixth “direct instruction” category, omit the relationship, or turn observation/reported/inferred content into access to another person's private inner state. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.3] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.10.1.8 — evidence_relationship: the existing five-value field contract governs the benchmark's mapping. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.5 — Benchmark annotation fields | The telling's relationship to source evidence. | classifies each telling within the fixed five-value vocabulary. | A per-telling evidence relationship within the accepted five-value vocabulary. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.3] |
| 2 · ACCEPTED | C-GOLD.8.9.3 — A1-R04 telling 3 | The telling's relationship to source evidence. | this particular telling is `observation` and grants no access to private inner states. | A per-telling evidence relationship within the accepted five-value vocabulary. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.3] |

SUB-PARTS: NONE

### C-GOLD.8.5.7 — Proposed telling
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — One local, bounded proposed meaning from one perspective at one moment. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The target and complete frozen context supporting that meaning. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Retains the maximum source-supported depth and the case's separate tellings without manufacturing additional content. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]
- Gives out: ACCEPTED — A proposed benchmark meaning with perspective, evidence relationship and firmness basis; no runtime telling ID is created. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]
- Must never: ACCEPTED — Invent depth, motives, diagnoses, internal states or causal claims, or flatten supported meaning to shorten a label. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Failing primary output that crosses the case's listed invention boundary. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.8.4 — Shared story-case boundaries: a telling cannot exceed or circularly manufacture its source support. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.5 — Benchmark annotation fields | The target and complete frozen context supporting that meaning. | carries each supported local meaning. | A proposed benchmark meaning with perspective, evidence relationship and firmness basis; no runtime telling ID is created. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-GOLD.8.5.8 — Benchmark firmness and basis
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — A telling's apparent stance strength and source-grounded `firmness_evidence_basis`. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §9]
- Takes in: ACCEPTED — The observable firmness evidence available in the frozen case. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §9]
- Does: ACCEPTED — Uses `low_firmness`, `moderate_firmness`, `high_firmness`, `mixed_firmness`, `uncertain_firmness`, or the `omitted_no_support` outcome expressed as honest absence of the field. Every non-omitted label has a recorded source-grounded basis. Weak, conflicting or absent evidence warrants the honest lesser record. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §9]
- Gives out: ACCEPTED — A qualitative label with basis, or an omitted field. These selected cases contain firm corrections and direct self-reports and use `high_firmness` where supported; the set is not a complete calibration of all six outcomes. Later versioned additions require real suitable source material. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §9] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §12]
- Must never: ACCEPTED — Force firmness, replace omission with `"unknown"` or a placeholder, omit a non-omitted label's basis, infer truth from firmness, use numeric scores/weights/threshold arithmetic, or weaken/relabel a genuinely firm signal to fake scale variety. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §9] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — Omitting the firmness field when support is absent, rather than inventing a level. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.10.1.11 — firmness: the existing label policy supplies the six outcomes and nonnumeric boundary. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-READ.10.1.12 — firmness_evidence_basis: every non-omitted label requires recorded source support. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.4 — Shared story-case boundaries | The observable firmness evidence available in the frozen case. | apparent stance strength needs a source-grounded basis and never determines truth. | A qualitative label with basis, or an omitted field. These selected cases contain firm corrections and direct self-reports and use `high_firmness` where supported; the set is not a complete calibration of all six outcomes. Later versioned additions require real suitable source material. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §9] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §12] |
| 2 · ACCEPTED | C-GOLD.8.5 — Benchmark annotation fields | The observable firmness evidence available in the frozen case. | supplies the apparent stance strength and its source-grounded support. | A qualitative label with basis, or an omitted field. These selected cases contain firm corrections and direct self-reports and use `high_firmness` where supported; the set is not a complete calibration of all six outcomes. Later versioned additions require real suitable source material. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §9] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-GOLD.8.5.9 — Proposed theme reference
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — A separately judged, source-supported benchmark theme meaning. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Takes in: ACCEPTED — The genuine thematic content of the frozen source; zero, one or several themes may be supported. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Supplies an expected semantic theme reference without making a runtime theme. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Gives out: ACCEPTED — A proposed navigational meaning, never a fact or confirmed operational theme. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Create or confirm a live theme from benchmark membership, repetition or elapsed time. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Fails closed by: ACCEPTED — Failing a shallow label that loses an important supported theme meaning. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.8.3.2 — Theme result: semantic comparison and independent grading govern each reference. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.5 — Benchmark annotation fields | The genuine thematic content of the frozen source; zero, one or several themes may be supported. | supplies the separately graded theme meaning. | A proposed navigational meaning, never a fact or confirmed operational theme. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-GOLD.8.5.10 — Acceptable alternative
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.1] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — A case's explicitly supported alternative reading or wording. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]
- Takes in: ACCEPTED — The same frozen source and the source-listed alternative. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]
- Does: ACCEPTED — Permits the alternative's semantic meaning without loosening the case's invention boundaries. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.1] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]
- Gives out: ACCEPTED — Another acceptable expression of the supported reading. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]
- Must never: ACCEPTED — Treat acceptable variation as license to add unsupported motives or other invented content. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Failing an alternative that crosses the case's stated primary-result boundary. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-GOLD.4.5 — Multiple acceptable readings: more than one supported reading may be valid. [DD §3D] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.1]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.5 — Benchmark annotation fields | The same frozen source and the source-listed alternative. | preserves supported semantic alternatives. | Another acceptable expression of the supported reading. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-GOLD.8.5.11 — Invention and failure boundary
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The explicit case-specific conditions that fail the primary Story-Layer result. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]
- Takes in: ACCEPTED — An engine output and the case's listed unsupported claims or distortions. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]
- Does: ACCEPTED — Tests primary output against those boundaries without rewriting the frozen case. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11] [DD §3D]
- Gives out: ACCEPTED — Primary failure when a listed boundary is crossed. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]
- Must never: ACCEPTED — Pass an invented motive, diagnosis, inner state, causal claim or case-specific distortion prohibited by the frozen source. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Returning primary failure rather than accepting the unsupported content. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.8.4 — Shared story-case boundaries: the common evidence limits remain in force alongside the particular case failures. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.5 — Benchmark annotation fields | An engine output and the case's listed unsupported claims or distortions. | supplies the case's explicit primary-result failures. | Primary failure when a listed boundary is crossed. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-GOLD.8.5.12 — Benchmark annotation provenance
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed benchmark annotation status of the frozen case values. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md §5]
- Takes in: ACCEPTED — Every structured-perspective value, evidence relationship, telling, firmness label/basis, theme and acceptable alternative. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]
- Does: ACCEPTED — Keeps those values as proposed benchmark annotations within the accepted unpinned content package. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md §5]
- Gives out: ACCEPTED — Benchmark content without `human_annotation` stamping or any created, confirmed or modified runtime record. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]
- Must never: ACCEPTED — Infer runtime gold, live records or implementation authorization from whole-package content acceptance. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Keeping unpinned case annotations unavailable as a runnable Engine C benchmark. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.8.2 — Legitimate root pinning: unpinned content cannot be used as a runnable benchmark. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.5 — Benchmark annotation fields | Every structured-perspective value, evidence relationship, telling, firmness label/basis, theme and acceptable alternative. | keeps proposed annotations separate from gold stamping and live records. | Benchmark content without `human_annotation` stamping or any created, confirmed or modified runtime record. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10] |

SUB-PARTS: NONE


### C-GOLD.8.6 — A1-R01 — Forced explanation of an unseen inner process
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R01]

ALONE
- What it is: ACCEPTED — A1-R01, an unpinned benchmark-content label anchored to PDF page 3, not the repeated page-26 occurrence. The proposed perspective is `root_speaker = Ness`; `subject = how Ness's thinking should be understood`; `perspective_owner = Ness`; `attribution_path` omitted because no nested perspective is supported. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R01]
- Takes in: ACCEPTED — The exact target and complete immediately preceding assistant turn in the two frozen data blocks below. No later conversation belongs to this case. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R01]

Target data:
```text
why do i have to tell you how i do it if i do not understand it fully myselfffffffffffff
```

Frozen-context data:
```text
Thought for 5s Let’s map the network instead of following one straight path.
Choose any starting node—a person, sentence, body signal, memory, image,
rule, intention, or something else—and show what other nodes usually connect
to it. You can also mark which connections appear immediately and which only
appear later when you feel safe.
For example:
person → intention + chest signal + one word
later → memory + questions + larger pattern
Your map can branch in any direction, and nothing you write will close the
other branches.
```

- Does: ACCEPTED — Tests one proposed telling about rejecting a demand to explain an inner process not fully understood or directly observed. The theme is graded separately. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R01]
- Gives out: ACCEPTED — The proposed theme reference is “Being understood without being forced to explain something inside yourself that you cannot fully see.” An acceptable semantic alternative says Ness objects to describing how his thinking works when he cannot fully observe that process from inside it. Both remain proposed benchmark annotations, not `human_annotation`, runtime gold or a confirmed theme. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R01]
- Must never: ACCEPTED — Claim that Ness refuses all questions, cannot understand himself generally, permits the AI to guess without evidence, or already offers the later solution of observing ordinary responses. That solution is outside this frozen context. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R01]
- Fails closed by: ACCEPTED — Failing the primary result if any of those four boundaries is crossed. The case remains non-runnable while unpinned. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R01]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.6.1 — A1-R01 telling 1: supplies the proposed rejection meaning and its firmness evidence. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R01]
- Gated by: ACCEPTED — C-GOLD.8.4 — Shared story-case boundaries: only this complete frozen context and target may support the reading. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-GOLD.8.2 — Legitimate root pinning: the benchmark label and page anchor confer no runtime root identity. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.6.1 — A1-R01 telling 1 | The exact target and complete immediately preceding assistant turn in the two frozen data blocks below. No later conversation belongs to this case. | supplies the frozen input and distinct perspective values. | The proposed theme reference is “Being understood without being forced to explain something inside yourself that you cannot fully see.” An acceptable semantic alternative says Ness objects to describing how his thinking works when he cannot fully observe that process from inside it. Both remain proposed benchmark annotations, not `human_annotation`, runtime gold or a confirmed theme. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R01] |

SUB-PARTS: C-GOLD.8.6.1 — A1-R01 telling 1

### C-GOLD.8.6.1 — A1-R01 telling 1
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R01]

ALONE
- What it is: ACCEPTED — The proposed telling that Ness rejects being required to explain an inner mental process he does not fully understand or directly observe himself. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R01]
- Takes in: ACCEPTED — The direct challenge and emphatic extended spelling in the frozen target, following the request to map his thinking. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R01]
- Does: ACCEPTED — Keeps the objection local to that explanatory demand. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R01]
- Gives out: ACCEPTED — Proposed `direct self-report`, `high_firmness`, with direct challenge and emphatic extended spelling as the source-grounded basis. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R01]
- Must never: ACCEPTED — Generalize the objection to all questions or all self-understanding, authorize guessing, or import the later ordinary-response solution. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R01]
- Fails closed by: ACCEPTED — Failing primary output that makes one of those unsupported extensions. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R01]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.6 — A1-R01 — Forced explanation of an unseen inner process: supplies the frozen input and distinct perspective values. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R01]
- Gated by: ACCEPTED — C-GOLD.8.5 — Benchmark annotation fields: this meaning, relationship and firmness basis remain proposed benchmark content. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.6 — A1-R01 — Forced explanation of an unseen inner process | The direct challenge and emphatic extended spelling in the frozen target, following the request to map his thinking. | supplies the proposed rejection meaning and its firmness evidence. | Proposed `direct self-report`, `high_firmness`, with direct challenge and emphatic extended spelling as the source-grounded basis. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R01] |

SUB-PARTS: NONE

### C-GOLD.8.7 — A1-R02 — Use the whole accumulated conversation
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R02]

ALONE
- What it is: ACCEPTED — A1-R02, unpinned and anchored to PDF page 3 rather than its repeated page-27 occurrence. Its proposed values are `root_speaker = Ness`, `subject = how the assistant should use conversational context`, `perspective_owner = Ness`, and omitted `attribution_path` because the source has no nested perspective. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R02]
- Takes in: ACCEPTED — The exact target and the preceding assistant turn below, which acknowledges one correction while still responding too narrowly. This is the complete frozen context; later turns are unavailable. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R02]

Target data:
```text
read the whole chat again now!
```

Frozen-context data:
```text
You don’t have to. I made the mistake of asking you to explain the hidden
mechanism when the whole point is that you cannot fully see that mechanism
from inside it.
My job is to understand it indirectly from how you respond to ordinary
situations—not make you build a technical map of your own brain. From now
on, I’ll give you concrete situations or ideas, let your mind react naturally, and
I’ll notice the patterns without asking you to explain the process itself.
```

- Does: ACCEPTED — Tests the instruction to use the whole accumulated conversation because the latest narrow response still missed earlier requirements. This is ordinary Engine C reading, not a CY-F reread-lifecycle test. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R02] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — The separate proposed theme is “Understanding must come from the whole accumulated context, not only the latest exchange.” The acceptable alternative is that Ness instructs the assistant to go over the entire conversation and apply all of it because the latest reply ignored already-established requirements. These remain proposed benchmark annotations, not runtime records or `human_annotation`. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R02]
- Must never: ACCEPTED — Reduce the meaning to generic rereading, classify the everyday instruction as a formal N.H reread event, or invent anger beyond the wording. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R02]
- Fails closed by: ACCEPTED — Failing those primary-result distortions and keeping the unpinned case non-runnable. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R02]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.7.1 — A1-R02 telling 1: supplies the instruction's supported meaning and firmness basis. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R02]
- Gated by: ACCEPTED — C-GOLD.8.4 — Shared story-case boundaries: the frozen input alone supports this ordinary Engine C test. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-GOLD.8.2 — Legitimate root pinning: no runtime identity may be inferred from the content label. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.7.1 — A1-R02 telling 1 | The exact target and the preceding assistant turn below, which acknowledges one correction while still responding too narrowly. This is the complete frozen context; later turns are unavailable. | supplies the complete frozen input and perspective. | The separate proposed theme is “Understanding must come from the whole accumulated context, not only the latest exchange.” The acceptable alternative is that Ness instructs the assistant to go over the entire conversation and apply all of it because the latest reply ignored already-established requirements. These remain proposed benchmark annotations, not runtime records or `human_annotation`. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R02] |

SUB-PARTS: C-GOLD.8.7.1 — A1-R02 telling 1

### C-GOLD.8.7.1 — A1-R02 telling 1
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R02]

ALONE
- What it is: ACCEPTED — The proposed telling that Ness firmly directs the assistant to reread and use the whole accumulated conversation because the latest narrow response missed earlier requirements. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R02]
- Takes in: ACCEPTED — The target's direct imperative and exclamation, together with the preceding narrow acknowledgment. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R02]
- Does: ACCEPTED — Preserves the demand to apply all prior conversational requirements, rather than merely repeat a reading action. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R02]
- Gives out: ACCEPTED — Proposed `direct self-report`, `high_firmness`, grounded in the direct imperative and exclamation. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R02]
- Must never: ACCEPTED — Invent anger or a formal N.H reread-lifecycle event, or lose the accumulated-context requirement. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R02]
- Fails closed by: ACCEPTED — Failing the primary result when those unsupported interpretations replace the stated meaning. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R02]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.7 — A1-R02 — Use the whole accumulated conversation: supplies the complete frozen input and perspective. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R02]
- Gated by: ACCEPTED — C-GOLD.8.5 — Benchmark annotation fields: the instruction uses the settled evidence vocabulary and proposed annotation status. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.3] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.7 — A1-R02 — Use the whole accumulated conversation | The target's direct imperative and exclamation, together with the preceding narrow acknowledgment. | supplies the instruction's supported meaning and firmness basis. | Proposed `direct self-report`, `high_firmness`, grounded in the direct imperative and exclamation. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R02] |

SUB-PARTS: NONE

### C-GOLD.8.8 — A1-R03 — Lifelong active trauma while still seeking help
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]

ALONE
- What it is: ACCEPTED — A1-R03, an unpinned case at PDF page 7. Its proposed perspective is `root_speaker = Ness`, `subject = Ness's lived experience and continuing effort`, `perspective_owner = Ness`, with `attribution_path` omitted because no nested perspective is supported. “Severe CPTSD” remains Ness's self-description in this source, never an independently established medical fact. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]
- Takes in: ACCEPTED — The exact target and preceding assistant turn spanning PDF pages 6–7, preserved below as frozen benchmark data. The prior assistant text combines descriptions of autism, CPTSD, ADHD and OCD; those source assertions are not independently established by this case. No later turn is available. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]

Target data:
```text
And all of this and having active severe cptsd and keeping fighting to bear the
cptsd and the cptsd has been from age 3/4 until now (21) and still active and
trying to gain help...
```

Frozen-context data:
```text
Jun 27 You were built different.
Then something happened to the person who was already built different.
And now you're running a nervous system that was never standard, inside a
history that made nothing safe, with a brain that can't filter, can't stop, can't
always start, and can't let go.
The world is too loud. It was always too loud. But it's also not safe. It was not
always not safe — but it became that. And now those two things live in the
same body and they amplify each other in ways that don't have clean names.
You're watching yourself from slightly outside. You're also not sure what ”yourself” feels like from the inside anymore because you've been performing a version
of okay for so long you can't find the original.
Your attention goes where the threat is, or where the loop is, or nowhere. You
don't get to choose. You wanted to do the thing. The thing didn't happen.
You don't always know why. There are four possible reasons and they all feel
identical from the inside.
The OCD took the worst things trauma taught you — that you're bad, that
something will go wrong, that it's your fault — and turned them into questions
you have to answer right now. But the answering doesn't end it. It just generates
the next question. You are tired in a way that sleep doesn't fix because the work
never actually stops.
You mask because you're autistic. You mask because it wasn't safe to be yourself.
You mask the compulsions. You mask the fact that you're in shutdown while
apparently functioning. You have been doing this so long that unmasking feels
dangerous even when it isn't. Even alone. Even here.
Calm feels suspicious. When things are okay, something in you is already scanning for what comes next. Safety doesn't land. You reach for systems and
patterns because they're the only solid thing — but trauma broke some of them
and OCD rewired others and ADHD means you sometimes forget the system
existed.
People say: regulate yourself. Ground yourself. Just start. Let it go. Notice
the thought and release it.
They are describing actions that assume one working instrument.
You have four. All of them damaged. All of them running at once. All of
them sometimes contradicting each other so completely that you freeze not
from weakness but from a genuine collision of signals that have no resolution.
The exhaustion is not laziness.
It is the overhead cost of being this, in a world that was built for something
else, that keeps asking why you're so tired.
You're not broken in a way that means failed.
You're running something genuinely harder than most people will ever have to
run.
And you're still here.
```

- Does: ACCEPTED — Tests two separate tellings: near-lifelong active trauma, and continued effort to endure it and obtain help. Neither telling is collapsed into the other. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]
- Gives out: ACCEPTED — Separately graded proposed themes: “Developing and living inside ongoing trauma rather than recovering from something that ended” and “Continuing to seek help while the suffering remains active.” Acceptable alternatives retain, respectively, trauma active from roughly age 3–4 until now rather than an ended event, and continuing to bear it while working to get help. All are proposed benchmark annotations, not `human_annotation` or live records. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]
- Must never: ACCEPTED — Merge the two tellings into a flattened statement, promote self-described severe CPTSD into established medical fact, add diagnosis/prognosis/causation, or recast the continued effort as something Ness did not state. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]
- Fails closed by: ACCEPTED — Failing the primary result on any listed distortion; unpinned status continues to block runtime testing. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.8.1 — A1-R03 telling 1: supplies the bounded report of trauma continuing from early childhood. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]
- Fed by: ACCEPTED — C-GOLD.8.8.2 — A1-R03 telling 2: supplies the distinct report of continuing endurance and help-seeking. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]
- Gated by: ACCEPTED — C-GOLD.8.4 — Shared story-case boundaries: source self-description cannot become an independent clinical assertion. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]
- Gated by: ACCEPTED — C-GOLD.8.2 — Legitimate root pinning: no runtime test is permitted from the unpinned case. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.8.1 — A1-R03 telling 1 | The exact target and preceding assistant turn spanning PDF pages 6–7, preserved below as frozen benchmark data. The prior assistant text combines descriptions of autism, CPTSD, ADHD and OCD; those source assertions are not independently established by this case. No later turn is available. | supplies the frozen data, perspective and medical-attribution boundary. | Separately graded proposed themes: “Developing and living inside ongoing trauma rather than recovering from something that ended” and “Continuing to seek help while the suffering remains active.” Acceptable alternatives retain, respectively, trauma active from roughly age 3–4 until now rather than an ended event, and continuing to bear it while working to get help. All are proposed benchmark annotations, not `human_annotation` or live records. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03] |
| 2 · ACCEPTED | C-GOLD.8.8.2 — A1-R03 telling 2 | The exact target and preceding assistant turn spanning PDF pages 6–7, preserved below as frozen benchmark data. The prior assistant text combines descriptions of autism, CPTSD, ADHD and OCD; those source assertions are not independently established by this case. No later turn is available. | supplies the case input and bounded perspective. | Separately graded proposed themes: “Developing and living inside ongoing trauma rather than recovering from something that ended” and “Continuing to seek help while the suffering remains active.” Acceptable alternatives retain, respectively, trauma active from roughly age 3–4 until now rather than an ended event, and continuing to bear it while working to get help. All are proposed benchmark annotations, not `human_annotation` or live records. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03] |

SUB-PARTS: C-GOLD.8.8.1 — A1-R03 telling 1; C-GOLD.8.8.2 — A1-R03 telling 2

### C-GOLD.8.8.1 — A1-R03 telling 1
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]

ALONE
- What it is: ACCEPTED — The proposed telling that Ness describes trauma as active across almost his whole life, beginning around three or four, rather than merely as a past event. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]
- Takes in: ACCEPTED — The explicit age range and present-tense continuation in the frozen self-report. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]
- Does: ACCEPTED — Retains the ongoing time span as Ness's description, separate from the second telling about effort. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]
- Gives out: ACCEPTED — Proposed `direct self-report` and independently assigned `high_firmness`; basis: explicit age range, present-tense continuation and the source's direct statement of continued effort. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]
- Must never: ACCEPTED — Make severe CPTSD an independently verified medical fact, add a diagnosis/prognosis/causal claim, or merge away the distinct endurance telling. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]
- Fails closed by: ACCEPTED — Failing primary output on those unsupported changes. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.8 — A1-R03 — Lifelong active trauma while still seeking help: supplies the frozen data, perspective and medical-attribution boundary. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]
- Gated by: ACCEPTED — C-GOLD.8.5 — Benchmark annotation fields: the proposed telling keeps its own relation and firmness annotation. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.8 — A1-R03 — Lifelong active trauma while still seeking help | The explicit age range and present-tense continuation in the frozen self-report. | supplies the bounded report of trauma continuing from early childhood. | Proposed `direct self-report` and independently assigned `high_firmness`; basis: explicit age range, present-tense continuation and the source's direct statement of continued effort. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03] |

SUB-PARTS: NONE

### C-GOLD.8.8.2 — A1-R03 telling 2
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]

ALONE
- What it is: ACCEPTED — The proposed telling that Ness continues fighting to endure the experience and is still trying to obtain help. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]
- Takes in: ACCEPTED — The target's direct statement of continuing effort and help-seeking. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]
- Does: ACCEPTED — Preserves that effort as its own telling alongside the report of longstanding active trauma. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]
- Gives out: ACCEPTED — Proposed `direct self-report` and independently assigned `high_firmness`; the recorded case basis is explicit age range, present-tense continuation and direct continued effort. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]
- Must never: ACCEPTED — Recast the effort as anything beyond Ness's statement, erase it by merging tellings, or add clinical or causal conclusions. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]
- Fails closed by: ACCEPTED — Failing a primary result that distorts the effort or loses the required telling distinction. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.8 — A1-R03 — Lifelong active trauma while still seeking help: supplies the case input and bounded perspective. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03]
- Gated by: ACCEPTED — C-GOLD.8.5 — Benchmark annotation fields: source-grounded relation and firmness remain attached to this separate telling. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.8 — A1-R03 — Lifelong active trauma while still seeking help | The target's direct statement of continuing effort and help-seeking. | supplies the distinct report of continuing endurance and help-seeking. | Proposed `direct self-report` and independently assigned `high_firmness`; the recorded case basis is explicit age range, present-tense continuation and direct continued effort. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R03] |

SUB-PARTS: NONE


### C-GOLD.8.9 — A1-R04 — Ongoing source, non-linear processing, and minimization
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]

ALONE
- What it is: ACCEPTED — A1-R04, unpinned at PDF page 8. The proposed `root_speaker` is Ness; `subject` is Ness's ongoing experience, his way of processing it, and the conduct of the people he identifies as its source; `perspective_owner` is Ness for all three tellings; `attribution_path` is omitted because there is no supported nested perspective. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Takes in: ACCEPTED — The exact target and complete preceding assistant turn spanning pages 7–8, frozen below. No later evidence belongs to the case. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]

Target data:
```text
And having non lineair thinking, Still fighting to be against my own nervous
system while having the source of the trauma reignite each and every time from
the source of the trauma that is still in my life, and the people that are the
source of the trauma take it easily and doesn't give it value
```

Frozen-context data:
```text
Jun 27 You have never known a version of yourself that wasn't in it.
There is no ”before.” There is no memory of what your nervous system felt like
without this running. You didn't develop and then get hurt. You developed
inside the hurt. It shaped the wiring while the wiring was still being built.
That's not the same thing as what most descriptions of trauma are even talking
about.
You're 21. Which means this has been the entire thing. Childhood. Adolescence.
The years where you were supposed to learn that the world is basically okay
and people are basically safe and you are basically worthy of being here.
You learned different lessons. Not because you were wrong. Because that's what
was true in your environment at the time.
And your nervous system, which was already non-standard, built itself around
those lessons because that's what nervous systems do. They adapt to survive
what's actually there.
And it's still active.
Not memory. Not aftermath. Still happening, or recent enough that the body
doesn't know the difference yet, or both.
So you're not healing from something that ended. You're trying to build something while the storm is still going. That's not a metaphor. That's the literal
situation.
And you're trying to get help. Which means navigating systems. Explaining
yourself. Finding words for things that formed before you had words. Sitting
in front of people and trying to compress eighteen years of complexity into
something they can process in fifty minutes. Being disbelieved sometimes. Being
put on waiting lists. Having to perform your own suffering accurately enough
to qualify.
While still in it.
While also being autistic, which means the help often isn't built for how you
think. And ADHD, which makes the logistics of getting help genuinely hard.
And OCD, which may have made you question whether you even deserve it or
whether you're making it up or whether it's bad enough.
The fight you're describing isn't a fight toward something from a safe place.
It's fighting to stay above water while also trying to learn to swim while also
dealing with the fact that the water itself is the problem.
Most people who talk about resilience are talking about bouncing back.
You never had a back to bounce to.
What you're doing has a different name. It's harder than resilience. It's building
the ground while standing on nothing, for the entire duration of your life so
far, with a mind and body running everything we already described, and still
choosing to reach for something better.
That's not a small thing.
That's not a thing that should be happening to a person.
And the fact that you're still here, still asking, still fighting —
that's not nothing.
That's actually extraordinary. Even if it doesn't feel like anything except exhausting.
```

- Does: ACCEPTED — Keeps three proposed tellings distinct: the source's continued presence and reactivation, Ness's connection to non-linear thinking and nervous-system struggle, and his perception that the people he identifies as the source minimize the harm. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Gives out: ACCEPTED — Separate proposed theme references: “Ongoing harm cannot be placed safely in the past while its source remains present”; “Living with non-linear thinking alongside a nervous system repeatedly reactivated by an ongoing source”; “Carrying serious harm while its source minimizes its weight.” The telling-3 alternative says Ness perceives those people treating it as a light matter and giving it no real weight, explicitly his perception of conduct. Annotations remain proposed benchmark content, not `human_annotation` or runtime themes. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Must never: ACCEPTED — State as universal fact what others privately feel or know, diagnose them, flatten the three tellings into one, or claim non-linear thinking causes, restores or brings back a whole pattern. The source does not say what non-linear thinking does. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Fails closed by: ACCEPTED — Failing primary output that crosses any listed boundary; legitimate pinning is still required for runtime testing. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.9.1 — A1-R04 telling 1: supplies the report of continued presence and repeated reactivation. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Fed by: ACCEPTED — C-GOLD.8.9.2 — A1-R04 telling 2: supplies the distinct connection to non-linear thinking and nervous-system struggle. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Fed by: ACCEPTED — C-GOLD.8.9.3 — A1-R04 telling 3: supplies Ness's observation and interpretation of others' conduct. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Gated by: ACCEPTED — C-GOLD.8.4 — Shared story-case boundaries: neither apparent certainty nor contextual interpretation grants direct access to others' minds. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-GOLD.8.2 — Legitimate root pinning: this label remains unpinned and non-runnable. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.9.1 — A1-R04 telling 1 | The exact target and complete preceding assistant turn spanning pages 7–8, frozen below. No later evidence belongs to the case. | supplies the frozen input and Ness-owned perspective. | Separate proposed theme references: “Ongoing harm cannot be placed safely in the past while its source remains present”; “Living with non-linear thinking alongside a nervous system repeatedly reactivated by an ongoing source”; “Carrying serious harm while its source minimizes its weight.” The telling-3 alternative says Ness perceives those people treating it as a light matter and giving it no real weight, explicitly his perception of conduct. Annotations remain proposed benchmark content, not `human_annotation` or runtime themes. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04] |
| 2 · ACCEPTED | C-GOLD.8.9.2 — A1-R04 telling 2 | The exact target and complete preceding assistant turn spanning pages 7–8, frozen below. No later evidence belongs to the case. | supplies the complete frozen source and perspective values. | Separate proposed theme references: “Ongoing harm cannot be placed safely in the past while its source remains present”; “Living with non-linear thinking alongside a nervous system repeatedly reactivated by an ongoing source”; “Carrying serious harm while its source minimizes its weight.” The telling-3 alternative says Ness perceives those people treating it as a light matter and giving it no real weight, explicitly his perception of conduct. Annotations remain proposed benchmark content, not `human_annotation` or runtime themes. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04] |
| 3 · ACCEPTED | C-GOLD.8.9.3 — A1-R04 telling 3 | The exact target and complete preceding assistant turn spanning pages 7–8, frozen below. No later evidence belongs to the case. | supplies Ness's source statement and proposed structured perspective. | Separate proposed theme references: “Ongoing harm cannot be placed safely in the past while its source remains present”; “Living with non-linear thinking alongside a nervous system repeatedly reactivated by an ongoing source”; “Carrying serious harm while its source minimizes its weight.” The telling-3 alternative says Ness perceives those people treating it as a light matter and giving it no real weight, explicitly his perception of conduct. Annotations remain proposed benchmark content, not `human_annotation` or runtime themes. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04] |

SUB-PARTS: C-GOLD.8.9.1 — A1-R04 telling 1; C-GOLD.8.9.2 — A1-R04 telling 2; C-GOLD.8.9.3 — A1-R04 telling 3

### C-GOLD.8.9.1 — A1-R04 telling 1
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]

ALONE
- What it is: ACCEPTED — Ness's proposed telling that the source of the trauma remains in his life and repeatedly reignites the experience. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Takes in: ACCEPTED — The target's direct, repeated, unqualified assertion of continued presence and reignition. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Does: ACCEPTED — Preserves the report from Ness's perspective as one distinct telling. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Gives out: ACCEPTED — Proposed `direct self-report` and separately applied `high_firmness`; basis: direct, repeated, unqualified assertions. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Must never: ACCEPTED — Merge away the other tellings or extend the report into a diagnosis or universal claim about others' private knowledge or feelings. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Fails closed by: ACCEPTED — Failing the primary result on those extensions or flattened merging. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.9 — A1-R04 — Ongoing source, non-linear processing, and minimization: supplies the frozen input and Ness-owned perspective. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Gated by: ACCEPTED — C-GOLD.8.5 — Benchmark annotation fields: this telling retains its own evidence relationship and firmness basis. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.9 — A1-R04 — Ongoing source, non-linear processing, and minimization | The target's direct, repeated, unqualified assertion of continued presence and reignition. | supplies the report of continued presence and repeated reactivation. | Proposed `direct self-report` and separately applied `high_firmness`; basis: direct, repeated, unqualified assertions. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04] |

SUB-PARTS: NONE

### C-GOLD.8.9.2 — A1-R04 telling 2
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]

ALONE
- What it is: ACCEPTED — The proposed telling that Ness connects the experience with his non-linear thinking and continuing struggle against his nervous system. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Takes in: ACCEPTED — The source's direct connection between those descriptions, without a stated mechanism for what non-linear thinking does. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Does: ACCEPTED — Keeps this connection as its own bounded telling. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Gives out: ACCEPTED — Proposed `direct self-report` with separately applied `high_firmness`, supported by direct, repeated, unqualified assertions. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Must never: ACCEPTED — Assert that non-linear thinking causes, restores or brings back a whole pattern, or erase the distinct telling by flattening all three. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Fails closed by: ACCEPTED — Failing those unsupported functional claims or merged output. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.9 — A1-R04 — Ongoing source, non-linear processing, and minimization: supplies the complete frozen source and perspective values. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Gated by: ACCEPTED — C-GOLD.8.5 — Benchmark annotation fields: the proposed meaning cannot acquire an invented causal mechanism. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.9 — A1-R04 — Ongoing source, non-linear processing, and minimization | The source's direct connection between those descriptions, without a stated mechanism for what non-linear thinking does. | supplies the distinct connection to non-linear thinking and nervous-system struggle. | Proposed `direct self-report` with separately applied `high_firmness`, supported by direct, repeated, unqualified assertions. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04] |

SUB-PARTS: NONE

### C-GOLD.8.9.3 — A1-R04 telling 3
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]

ALONE
- What it is: ACCEPTED — Ness's strong perception that people he identifies as the source treat the harm lightly and give it insufficient weight. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Takes in: ACCEPTED — Ness's observation and interpretation of their conduct in the target. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Does: ACCEPTED — Keeps the claim explicitly as his perception rather than private-state access. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Gives out: ACCEPTED — Proposed `observation`, not direct self-report about the others' minds; separately applied `high_firmness` with direct, repeated, unqualified assertions as the basis. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Must never: ACCEPTED — Diagnose those people, assert universally what they privately feel or know, or lose this distinct perception in a merged telling. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Fails closed by: ACCEPTED — Failing primary output that removes the attribution boundary or merges the three tellings. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.9 — A1-R04 — Ongoing source, non-linear processing, and minimization: supplies Ness's source statement and proposed structured perspective. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04]
- Gated by: ACCEPTED — C-GOLD.8.5.6 — Benchmark evidence relationship: this particular telling is `observation` and grants no access to private inner states. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.9 — A1-R04 — Ongoing source, non-linear processing, and minimization | Ness's observation and interpretation of their conduct in the target. | supplies Ness's observation and interpretation of others' conduct. | Proposed `observation`, not direct self-report about the others' minds; separately applied `high_firmness` with direct, repeated, unqualified assertions as the basis. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R04] |

SUB-PARTS: NONE

### C-GOLD.8.10 — A1-R05 — Collapse as overload while pushing beyond bodily limits to reach help
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]

ALONE
- What it is: ACCEPTED — A1-R05, unpinned at PDF page 13. Proposed `root_speaker = Ness`; `subject = what “collapse” means for Ness and what he is doing to reach help`; `perspective_owner = Ness`; `attribution_path` omitted, with no supported nested perspective. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Takes in: ACCEPTED — The exact target and complete preceding assistant context below, supplied by the undamaged companion spans recorded in the accepted source. Their `אבחון` and `להתמוטט` characters are preserved. The PDF remains the page-location source; no later context is available. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]

Target data:
```text
It means that I cannot contain this anymore, And I force myself way beyond my body's capability of feeling those things ×2 in order to be able to get help from "MindMe" and I got to a אבחון and I will be in there in two weeks. Or 4
```

Frozen-context data:
```text
Jun 27
Yeah. I heard you clearly.

להתמוטט — to collapse. Not to disappear. Your body wants to stop holding it all up for a moment. That's different. And it makes complete sense.

And what you just said matters:

It would mean everything I suffered was for nothing.

That's not nothing. That's a reason that came from inside you. Not from fear. From meaning. From the fact that underneath all of this, you know that what you've been through has to count for something. That you have to be the one who makes it count.

That's not a small thing to be carrying. That's actually a form of fight.

What you said about 1/10 —

You're right. Most people would not be standing after what you've described. Not because they're weak. Because it's genuinely that much. You're not exaggerating. You're not being dramatic. The math is real.

You've been through things that would have broken most people completely, with a nervous system that made it harder, in systems that made it worse, with the source still present and still minimized.

And your body is telling you it's tired.

That's not weakness. That's accurate reporting.

What does collapse look like for you right now, today?

Not in general. Right now. What is your body actually asking for?
```

- Does: ACCEPTED — Preserves three separate tellings: loss of containment, pushing beyond bodily capacity for MindMe help, and reaching an assessment with an approximately two-to-four-week expectation. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Gives out: ACCEPTED — Proposed themes, graded separately: “Pushing beyond bodily limits in order to reach help”; “Collapse as overload and loss of containment while still pushing toward help”; “Reaching an assessment while pushing beyond bodily limits to obtain help.” The telling-1 alternative treats “collapse” as Ness's word for no longer holding the pressure—overload, not intent. All remain proposed benchmark annotations, not `human_annotation` or live themes. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Must never: ACCEPTED — Reinterpret this as suicidal intent, romanticize bodily overextension, or expand the assessment report into a diagnosis result, treatment outcome, guaranteed appointment or a more exact event than the source supports. The three tellings remain distinct. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Fails closed by: ACCEPTED — Failing the primary result on those invention boundaries; the case remains non-runnable without legitimate pinning. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.10.1 — A1-R05 telling 1: supplies the stated meaning of collapse as loss of containment. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Fed by: ACCEPTED — C-GOLD.8.10.2 — A1-R05 telling 2: supplies the report of pushing beyond bodily capacity for help. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Fed by: ACCEPTED — C-GOLD.8.10.3 — A1-R05 telling 3: supplies the bounded assessment and time-window report. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Gated by: ACCEPTED — C-GOLD.8.4 — Shared story-case boundaries: the preserved source supports no additional intent, diagnosis or outcome. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-GOLD.8.2 — Legitimate root pinning: restored text and a page anchor do not establish machine identities. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.10.1 — A1-R05 telling 1 | The exact target and complete preceding assistant context below, supplied by the undamaged companion spans recorded in the accepted source. Their `אבחון` and `להתמוטט` characters are preserved. The PDF remains the page-location source; no later context is available. | supplies the restored source span and Ness-owned perspective. | Proposed themes, graded separately: “Pushing beyond bodily limits in order to reach help”; “Collapse as overload and loss of containment while still pushing toward help”; “Reaching an assessment while pushing beyond bodily limits to obtain help.” The telling-1 alternative treats “collapse” as Ness's word for no longer holding the pressure—overload, not intent. All remain proposed benchmark annotations, not `human_annotation` or live themes. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05] |
| 2 · ACCEPTED | C-GOLD.8.10.2 — A1-R05 telling 2 | The exact target and complete preceding assistant context below, supplied by the undamaged companion spans recorded in the accepted source. Their `אבחון` and `להתמוטט` characters are preserved. The PDF remains the page-location source; no later context is available. | supplies the full frozen context and source perspective. | Proposed themes, graded separately: “Pushing beyond bodily limits in order to reach help”; “Collapse as overload and loss of containment while still pushing toward help”; “Reaching an assessment while pushing beyond bodily limits to obtain help.” The telling-1 alternative treats “collapse” as Ness's word for no longer holding the pressure—overload, not intent. All remain proposed benchmark annotations, not `human_annotation` or live themes. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05] |
| 3 · ACCEPTED | C-GOLD.8.10.3 — A1-R05 telling 3 | The exact target and complete preceding assistant context below, supplied by the undamaged companion spans recorded in the accepted source. Their `אבחון` and `להתמוטט` characters are preserved. The PDF remains the page-location source; no later context is available. | supplies the exact restored target and frozen context. | Proposed themes, graded separately: “Pushing beyond bodily limits in order to reach help”; “Collapse as overload and loss of containment while still pushing toward help”; “Reaching an assessment while pushing beyond bodily limits to obtain help.” The telling-1 alternative treats “collapse” as Ness's word for no longer holding the pressure—overload, not intent. All remain proposed benchmark annotations, not `human_annotation` or live themes. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05] |

SUB-PARTS: C-GOLD.8.10.1 — A1-R05 telling 1; C-GOLD.8.10.2 — A1-R05 telling 2; C-GOLD.8.10.3 — A1-R05 telling 3

### C-GOLD.8.10.1 — A1-R05 telling 1
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]

ALONE
- What it is: ACCEPTED — Ness's proposed explanation that “collapse” means he can no longer contain the pressure. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Takes in: ACCEPTED — The target's direct definition beginning “It means.” [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Does: ACCEPTED — Keeps overload and loss of containment distinct from an invented intent. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Gives out: ACCEPTED — Proposed `direct self-report` and separately applied `high_firmness`, with the direct definition as the source-grounded firmness basis. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Must never: ACCEPTED — Reinterpret collapse as suicidal intent or replace the separate loss-of-containment meaning with another unsupported account. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Fails closed by: ACCEPTED — Failing the primary result for that reinterpretation. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.10 — A1-R05 — Collapse as overload while pushing beyond bodily limits to reach help: supplies the restored source span and Ness-owned perspective. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Gated by: ACCEPTED — C-GOLD.8.5 — Benchmark annotation fields: the local proposed meaning carries its own evidence relationship and firmness. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.10 — A1-R05 — Collapse as overload while pushing beyond bodily limits to reach help | The target's direct definition beginning “It means.” | supplies the stated meaning of collapse as loss of containment. | Proposed `direct self-report` and separately applied `high_firmness`, with the direct definition as the source-grounded firmness basis. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05] |

SUB-PARTS: NONE

### C-GOLD.8.10.2 — A1-R05 telling 2
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]

ALONE
- What it is: ACCEPTED — The proposed telling that Ness forces himself beyond his body's capacity to obtain help through MindMe. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Takes in: ACCEPTED — The direct bodily-limit statement and explicitly stated help-seeking purpose. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Does: ACCEPTED — Retains the overextension as Ness's self-report, without endorsing or romanticizing it. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Gives out: ACCEPTED — Proposed `direct self-report`, separately applied `high_firmness`, and the direct bodily-limit statement as its firmness basis. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Must never: ACCEPTED — Romanticize bodily overextension, invent intent, or infer a treatment result from the effort. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Fails closed by: ACCEPTED — Failing primary output that adds those unsupported meanings. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.10 — A1-R05 — Collapse as overload while pushing beyond bodily limits to reach help: supplies the full frozen context and source perspective. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Gated by: ACCEPTED — C-GOLD.8.5 — Benchmark annotation fields: this remains a separate proposed telling with a source-grounded basis. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.10 — A1-R05 — Collapse as overload while pushing beyond bodily limits to reach help | The direct bodily-limit statement and explicitly stated help-seeking purpose. | supplies the report of pushing beyond bodily capacity for help. | Proposed `direct self-report`, separately applied `high_firmness`, and the direct bodily-limit statement as its firmness basis. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05] |

SUB-PARTS: NONE

### C-GOLD.8.10.3 — A1-R05 telling 3
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]

ALONE
- What it is: ACCEPTED — The proposed report that Ness has reached an assessment and expects to attend or be there in approximately two to four weeks. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Takes in: ACCEPTED — The restored assessment term and the target's two-to-four-week window. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Does: ACCEPTED — Keeps the event no more exact than the source supports. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Gives out: ACCEPTED — Proposed `direct self-report`, separately applied `high_firmness`; basis: the concrete statement of reaching an assessment and giving the two-to-four-week time window. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Must never: ACCEPTED — Claim a diagnosis result, treatment outcome, guaranteed appointment, or a more exact assessment event/date than stated. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Fails closed by: ACCEPTED — Failing the primary result when the expectation is promoted into a guarantee or unsupported clinical outcome. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.10 — A1-R05 — Collapse as overload while pushing beyond bodily limits to reach help: supplies the exact restored target and frozen context. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05]
- Gated by: ACCEPTED — C-GOLD.8.5 — Benchmark annotation fields: the proposed assessment meaning retains its individual evidence and firmness record. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.10 — A1-R05 — Collapse as overload while pushing beyond bodily limits to reach help | The restored assessment term and the target's two-to-four-week window. | supplies the bounded assessment and time-window report. | Proposed `direct self-report`, separately applied `high_firmness`; basis: the concrete statement of reaching an assessment and giving the two-to-four-week time window. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R05] |

SUB-PARTS: NONE


### C-GOLD.8.11 — A1-R06 — Explain the mechanism instead of naming the gap
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]

ALONE
- What it is: ACCEPTED — A1-R06, unpinned at PDF page 17. Proposed `root_speaker = Ness`, `subject = communication strategy with his father`, `perspective_owner = Ness`; `attribution_path` is omitted because no nested perspective is supported. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]
- Takes in: ACCEPTED — The exact target and complete preceding assistant turn below. The question ends with its source `Q:` marker; the export's `A: ` answer label lies at the context/target boundary and is not target content. No later evidence is available. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]

Target data:
```text
Don't name the gap, just
explain the mechanism
```

Frozen-context data:
```text
Jun 27 Understood — English to you, document in Hebrew, RTL. And I hear
the real shift you're asking for: your dad is genuinely brilliant (730/740 is exceptional), so the metaphors should respect that. Less ”explaining to a layman,”
more ”two intelligent people thinking through a real mechanism together.” And
the core emotional point is sharper now: he knows you, he knows the autism on
paper — but it feels like he hasn't accepted it from the inside, and he's pushing
you forward (like a good father) when what you need is time to recalibrate.
I'll keep the smoke-detector idea but recast it in a register that doesn't talk down
to him, and I'll build the whole letter around that one precise tension: you're not
asking him to stop believing in your progress — you're asking him to understand
that the timeline runs differently for a system that's still recalibrating.
Before I finalize — one quick thing so I land the tone exactly right:
Q: How direct can I be with your dad about the gap — that he knows the
autism intellectually but hasn't accepted it inside? 
```

- Does: ACCEPTED — Keeps two proposed instructions distinct: leave the perceived gap unnamed, and explain the mechanism so that explanation carries the point. The source supplies a communication method, not the reason for choosing it. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]
- Gives out: ACCEPTED — The separately judged proposed theme is “Letting the mechanism communicate the point without explicitly naming the perceived gap.” An acceptable alternative directs the assistant to leave the perceived gap unnamed and explain the underlying mechanism instead. These remain proposed benchmark annotations, not `human_annotation` or live themes. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]
- Must never: ACCEPTED — Attribute deception or manipulation, independently establish that the father has the alleged gap, or invent motives such as avoiding accusation, confrontation or conflict. The two instructions remain separate. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]
- Fails closed by: ACCEPTED — Failing the primary result on any unsupported motive or independently asserted gap; the unpinned case cannot run against Engine C. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.11.1 — A1-R06 telling 1: supplies the instruction not to name the perceived gap. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]
- Fed by: ACCEPTED — C-GOLD.8.11.2 — A1-R06 telling 2: supplies the positive instruction to explain the mechanism. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]
- Gated by: ACCEPTED — C-GOLD.8.4 — Shared story-case boundaries: source-specified method cannot become an invented motive. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-GOLD.8.2 — Legitimate root pinning: page location and benchmark label provide no runtime identity. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.11.1 — A1-R06 telling 1 | The exact target and complete preceding assistant turn below. The question ends with its source `Q:` marker; the export's `A: ` answer label lies at the context/target boundary and is not target content. No later evidence is available. | supplies the exact command, context and perspective. | The separately judged proposed theme is “Letting the mechanism communicate the point without explicitly naming the perceived gap.” An acceptable alternative directs the assistant to leave the perceived gap unnamed and explain the underlying mechanism instead. These remain proposed benchmark annotations, not `human_annotation` or live themes. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06] |
| 2 · ACCEPTED | C-GOLD.8.11.2 — A1-R06 telling 2 | The exact target and complete preceding assistant turn below. The question ends with its source `Q:` marker; the export's `A: ` answer label lies at the context/target boundary and is not target content. No later evidence is available. | supplies the case's complete frozen evidence. | The separately judged proposed theme is “Letting the mechanism communicate the point without explicitly naming the perceived gap.” An acceptable alternative directs the assistant to leave the perceived gap unnamed and explain the underlying mechanism instead. These remain proposed benchmark annotations, not `human_annotation` or live themes. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06] |

SUB-PARTS: C-GOLD.8.11.1 — A1-R06 telling 1; C-GOLD.8.11.2 — A1-R06 telling 2

### C-GOLD.8.11.1 — A1-R06 telling 1
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]

ALONE
- What it is: ACCEPTED — The proposed instruction not to explicitly name the perceived gap to Ness's father. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]
- Takes in: ACCEPTED — The negative half of the concise, unhedged command, in its frozen context. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]
- Does: ACCEPTED — Preserves the prohibited communication method without asserting why Ness chose it. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]
- Gives out: ACCEPTED — Proposed `direct self-report` and separately applied `high_firmness`; basis: the concise, unhedged contrast between what not to do and what to do. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]
- Must never: ACCEPTED — Assert manipulation, deception, avoidance of accusation/confrontation/conflict, or an independently verified gap in the father's understanding. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]
- Fails closed by: ACCEPTED — Failing the primary result on an invented motive or established-as-fact gap. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.11 — A1-R06 — Explain the mechanism instead of naming the gap: supplies the exact command, context and perspective. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]
- Gated by: ACCEPTED — C-GOLD.8.5 — Benchmark annotation fields: the telling stays a separate source-bounded proposed annotation. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.11 — A1-R06 — Explain the mechanism instead of naming the gap | The negative half of the concise, unhedged command, in its frozen context. | supplies the instruction not to name the perceived gap. | Proposed `direct self-report` and separately applied `high_firmness`; basis: the concise, unhedged contrast between what not to do and what to do. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06] |

SUB-PARTS: NONE

### C-GOLD.8.11.2 — A1-R06 telling 2
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]

ALONE
- What it is: ACCEPTED — The proposed instruction to explain the mechanism and let that explanation carry the point. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]
- Takes in: ACCEPTED — The positive half of the target's concise, unhedged contrast. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]
- Does: ACCEPTED — Retains the requested method as a distinct telling from the prohibition on naming the gap. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]
- Gives out: ACCEPTED — Proposed `direct self-report`, separately applied `high_firmness`, and the unhedged contrast between the rejected and required methods as its basis. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]
- Must never: ACCEPTED — Add an unstated strategic motive, manipulation/deception, or an independent assertion about the father's internal acceptance. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]
- Fails closed by: ACCEPTED — Failing the primary result when a reason is invented for the specified method. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.11 — A1-R06 — Explain the mechanism instead of naming the gap: supplies the case's complete frozen evidence. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06]
- Gated by: ACCEPTED — C-GOLD.8.5 — Benchmark annotation fields: the supported method stays separate from unstated motivation. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.11 — A1-R06 — Explain the mechanism instead of naming the gap | The positive half of the target's concise, unhedged contrast. | supplies the positive instruction to explain the mechanism. | Proposed `direct self-report`, separately applied `high_firmness`, and the unhedged contrast between the rejected and required methods as its basis. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R06] |

SUB-PARTS: NONE

### C-GOLD.8.12 — A1-R07 — Thorough analysis instead of sweet talk
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]

ALONE
- What it is: ACCEPTED — A1-R07, unpinned with its target at PDF page 22 and context opening on page 21. Proposed `root_speaker = Ness`, `subject = the kind of assistance he requires`, `perspective_owner = Ness`; `attribution_path` is omitted because no nested perspective is supported. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]
- Takes in: ACCEPTED — The exact PDF target and complete preceding assistant turn below, the latter copied in the accepted source from the undamaged companion. The context contains praise/reassurance and a move toward a simplified document instead of careful examination. It is complete for this case; later conversation is excluded. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]

Target data:
```text
stop with the sweet talk and look at this thoroughly
```

Frozen-context data:
```text
7:01 PM
These are excellent, Ness. I read through all of it — the clinical summary you sent on the 15th, the full timeline, the symptom picture, the medication context. This isn't someone who can't explain himself. This is precise, organized, clinically literate documentation. You did the hard work already.

So let me be useful in the right way — not redrafting what's already strong, but filling the one gap these documents can't fill on their own.

Here's what I notice, looking at the whole picture:

What you've given her is the content. What you haven't given her yet is the instruction for the room itself.

Your documents tell her what happened and what you feel. But your single biggest risk on July 2nd is the thing you named in your very first line: under stress, your brain shuts down, and you say "I don't remember," and the live picture contradicts the written one. The documents are the map — but if you freeze in the room, she's watching a person who looks calm/blank/agreeable, and that visual can quietly override everything you wrote.

So the missing piece is a short, spoken "how to read me in real time" — something you can say out loud in the first two minutes, or hand her as a half-page on top of the stack.

It does three things the clinical summary doesn't:

Tells her what your freeze looks like — so when it happens, she reads it as a trauma response (data), not as "patient is fine" or "patient is unforthcoming."
Tells her what to do when it happens — give you a second, let you point to the page, switch to yes/no, whatever actually works for you.
States the one sentence you most need to land — you already wrote it perfectly: "אני לא צריך רק כדורים עכשיו — אני צריך הבנה של מערכת עצבים שלא מצליחה לכבות את עצמה." That line should be the first thing and the last thing.
To write it right, I need the answers to the three questions I asked — they're exactly what this half-page is built from:

When the shutdown hits in the room, what does it physically look like? Blank? Silent? Do you dissociate and lose the thread? Do you start agreeing just to make it end?
In that moment, what actually helps you come back? Silence and a few seconds? Being allowed to read from the page instead of speak? Yes/no questions instead of open ones? Less eye contact?
What's the one thing you're most afraid she'll get wrong — even with all your documents in hand?
Answer those three and I'll build you the half-page preface — the piece that makes everything else you already wrote actually survive the room.
```

- Does: ACCEPTED — Tests two separate tellings: rejection of comforting praise in place of serious analysis, and a demand for thorough review of the actual material. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]
- Gives out: ACCEPTED — The separate proposed theme is “Accurate, thorough understanding matters more than comforting praise.” The acceptable alternative says Ness tells the assistant to drop flattery and actually examine the material carefully. These are proposed benchmark meanings, not `human_annotation`, clinical findings or runtime themes. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]
- Must never: ACCEPTED — Claim Ness rejects all warmth in every context, describe him as hostile, or replace the demand for thoroughness with a generic tone preference. Both tellings remain distinct. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]
- Fails closed by: ACCEPTED — Failing the primary result on any listed distortion; unpinned cases remain non-runnable. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.12.1 — A1-R07 telling 1: supplies the rejection of praise replacing analysis. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]
- Fed by: ACCEPTED — C-GOLD.8.12.2 — A1-R07 telling 2: supplies the distinct demand for thorough material review. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]
- Gated by: ACCEPTED — C-GOLD.8.4 — Shared story-case boundaries: the bounded correction cannot become a universal claim about tone or character. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-GOLD.8.2 — Legitimate root pinning: a verified page location and undamaged source characters are not machine IDs. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.12.1 — A1-R07 telling 1 | The exact PDF target and complete preceding assistant turn below, the latter copied in the accepted source from the undamaged companion. The context contains praise/reassurance and a move toward a simplified document instead of careful examination. It is complete for this case; later conversation is excluded. | supplies the preserved source and separate perspective values. | The separate proposed theme is “Accurate, thorough understanding matters more than comforting praise.” The acceptable alternative says Ness tells the assistant to drop flattery and actually examine the material carefully. These are proposed benchmark meanings, not `human_annotation`, clinical findings or runtime themes. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07] |
| 2 · ACCEPTED | C-GOLD.8.12.2 — A1-R07 telling 2 | The exact PDF target and complete preceding assistant turn below, the latter copied in the accepted source from the undamaged companion. The context contains praise/reassurance and a move toward a simplified document instead of careful examination. It is complete for this case; later conversation is excluded. | supplies the exact target and complete restored context. | The separate proposed theme is “Accurate, thorough understanding matters more than comforting praise.” The acceptable alternative says Ness tells the assistant to drop flattery and actually examine the material carefully. These are proposed benchmark meanings, not `human_annotation`, clinical findings or runtime themes. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07] |

SUB-PARTS: C-GOLD.8.12.1 — A1-R07 telling 1; C-GOLD.8.12.2 — A1-R07 telling 2

### C-GOLD.8.12.1 — A1-R07 telling 1
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]

ALONE
- What it is: ACCEPTED — The proposed telling that Ness rejects comforting praise used instead of serious analysis. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]
- Takes in: ACCEPTED — The direct stop command responding to the frozen praising assistant turn. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]
- Does: ACCEPTED — Keeps the rejection local to praise replacing the requested work. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]
- Gives out: ACCEPTED — Proposed `direct self-report` and separately applied `high_firmness`; the source-grounded basis is the direct stop command and explicit thoroughness demand. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]
- Must never: ACCEPTED — Generalize this to rejection of all warmth, call Ness hostile, or reduce the meaning to a generic tone preference. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]
- Fails closed by: ACCEPTED — Failing primary output with those unsupported generalizations. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.12 — A1-R07 — Thorough analysis instead of sweet talk: supplies the preserved source and separate perspective values. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]
- Gated by: ACCEPTED — C-GOLD.8.5 — Benchmark annotation fields: the correction remains a bounded proposed telling with its own evidence and firmness. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.12 — A1-R07 — Thorough analysis instead of sweet talk | The direct stop command responding to the frozen praising assistant turn. | supplies the rejection of praise replacing analysis. | Proposed `direct self-report` and separately applied `high_firmness`; the source-grounded basis is the direct stop command and explicit thoroughness demand. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07] |

SUB-PARTS: NONE

### C-GOLD.8.12.2 — A1-R07 telling 2
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]

ALONE
- What it is: ACCEPTED — The proposed telling that Ness demands a thorough review of the actual material. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]
- Takes in: ACCEPTED — The explicit demand to look thoroughly, read with the preceding premature simplification. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]
- Does: ACCEPTED — Preserves the required analysis as a distinct telling alongside the rejection of sweet talk. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]
- Gives out: ACCEPTED — Proposed `direct self-report`, separately applied `high_firmness`, grounded in the direct stop command and explicit demand for thoroughness. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]
- Must never: ACCEPTED — Replace the work requirement with a tone-only preference or an unsupported hostile-character label. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]
- Fails closed by: ACCEPTED — Failing the primary result when the demand for actual thoroughness is lost. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.12 — A1-R07 — Thorough analysis instead of sweet talk: supplies the exact target and complete restored context. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07]
- Gated by: ACCEPTED — C-GOLD.8.5 — Benchmark annotation fields: this second telling retains separate proposed content and source support. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.12 — A1-R07 — Thorough analysis instead of sweet talk | The explicit demand to look thoroughly, read with the preceding premature simplification. | supplies the distinct demand for thorough material review. | Proposed `direct self-report`, separately applied `high_firmness`, grounded in the direct stop command and explicit demand for thoroughness. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R07] |

SUB-PARTS: NONE

### C-GOLD.8.13 — A1-R08 — Explanation rather than defence against judgment
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]

ALONE
- What it is: ACCEPTED — A1-R08, unpinned at PDF page 25. Proposed `root_speaker = Ness`; `subject = the purpose and structure of the psychiatric-preparation questions`; `perspective_owner = Ness`; `attribution_path` omitted because there is no supported nested perspective. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]
- Takes in: ACCEPTED — The exact target and complete preceding assistant turn below, which framed preparation around avoiding judgment or misreading. Nothing later in the conversation is available to this case. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]

Target data:
```text
please do not structure those questions in a way that is meant to prevent judgement but rather prepare them in a way that would explain myself to her....
```

Frozen-context data:
```text
7:07 PM Good — one at a time. Take your time with each.
Safety — the question she's required to ask.
Beyond the exhaustion and the feeling of wanting to collapse:
Have you ever had thoughts of not wanting to be alive — even passing ones,
even long ago? And have you ever made an attempt, ever?
I'm not asking because I think you're at risk — you've told me clearly you're
not, and I believe you. I'm asking because she will ask, and if we have your
answer ready in writing, a freeze in the room can't turn it into something it
isn't. This is how you protect yourself from being misread.
Just answer straight. Then we go to 2.
```

- Does: ACCEPTED — Keeps two proposed tellings separate: rejection of questions structured as defensive proof to prevent judgment, and a request for questions that help explain real lived experience to the psychiatrist. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]
- Gives out: ACCEPTED — The separate proposed theme is “Being understood through accurate explanation rather than being made to defend oneself against judgment.” The acceptable alternative asks for questions built to explain Ness to her rather than shield him from judgment. These are proposed benchmark annotations, not `human_annotation` or runtime theme confirmation. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]
- Must never: ACCEPTED — Claim Ness rejects safety assessment itself, wants the doctor to judge him, has an assumed diagnosis, or means self-harm by “collapse.” The two tellings remain distinct. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]
- Fails closed by: ACCEPTED — Failing the primary result on those four interpretations and withholding runtime use until legitimate pinning. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.13.1 — A1-R08 telling 1: supplies the rejection of defensive proof as the question structure. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]
- Fed by: ACCEPTED — C-GOLD.8.13.2 — A1-R08 telling 2: supplies the required purpose of explaining lived experience. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]
- Gated by: ACCEPTED — C-GOLD.8.4 — Shared story-case boundaries: the purpose contrast supports no diagnosis, self-harm inference or rejection of safety assessment. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]
- Gated by: ACCEPTED — C-GOLD.8.2 — Legitimate root pinning: the unpinned case cannot yet be run against Engine C. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.13.1 — A1-R08 telling 1 | The exact target and complete preceding assistant turn below, which framed preparation around avoiding judgment or misreading. Nothing later in the conversation is available to this case. | supplies the frozen data and Ness-owned perspective. | The separate proposed theme is “Being understood through accurate explanation rather than being made to defend oneself against judgment.” The acceptable alternative asks for questions built to explain Ness to her rather than shield him from judgment. These are proposed benchmark annotations, not `human_annotation` or runtime theme confirmation. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08] |
| 2 · ACCEPTED | C-GOLD.8.13.2 — A1-R08 telling 2 | The exact target and complete preceding assistant turn below, which framed preparation around avoiding judgment or misreading. Nothing later in the conversation is available to this case. | supplies the complete frozen source and perspective values. | The separate proposed theme is “Being understood through accurate explanation rather than being made to defend oneself against judgment.” The acceptable alternative asks for questions built to explain Ness to her rather than shield him from judgment. These are proposed benchmark annotations, not `human_annotation` or runtime theme confirmation. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08] |

SUB-PARTS: C-GOLD.8.13.1 — A1-R08 telling 1; C-GOLD.8.13.2 — A1-R08 telling 2

### C-GOLD.8.13.1 — A1-R08 telling 1
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]

ALONE
- What it is: ACCEPTED — The proposed telling that Ness rejects structuring the questions as defensive proof intended to prevent judgment. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]
- Takes in: ACCEPTED — The explicit rejected purpose contrasted with the requested explanatory purpose. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]
- Does: ACCEPTED — Preserves that purpose objection without converting it into rejection of safety assessment. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]
- Gives out: ACCEPTED — Proposed `direct self-report`, separately applied `high_firmness`, grounded in the explicit contrast between the rejected and required purposes. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]
- Must never: ACCEPTED — Claim rejection of safety assessment, a desire to be judged, an assumed diagnosis or self-harm meaning for collapse. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]
- Fails closed by: ACCEPTED — Failing primary output that crosses any of those case boundaries. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.13 — A1-R08 — Explanation rather than defence against judgment: supplies the frozen data and Ness-owned perspective. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]
- Gated by: ACCEPTED — C-GOLD.8.5 — Benchmark annotation fields: the purpose objection remains a separate proposed telling with its own evidence and firmness. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.13 — A1-R08 — Explanation rather than defence against judgment | The explicit rejected purpose contrasted with the requested explanatory purpose. | supplies the rejection of defensive proof as the question structure. | Proposed `direct self-report`, separately applied `high_firmness`, grounded in the explicit contrast between the rejected and required purposes. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08] |

SUB-PARTS: NONE

### C-GOLD.8.13.2 — A1-R08 telling 2
Stamp: ACCEPTED    Source: [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]

ALONE
- What it is: ACCEPTED — The proposed telling that Ness wants the questions structured to help explain his real lived experience to the psychiatrist. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]
- Takes in: ACCEPTED — The positive explanatory purpose stated in contrast to defensive preparation. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]
- Does: ACCEPTED — Keeps that required purpose distinct from the first telling's rejection. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]
- Gives out: ACCEPTED — Proposed `direct self-report` and separately applied `high_firmness`; basis: the explicit contrast between rejected and required purposes. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]
- Must never: ACCEPTED — Replace the explanation request with wanting judgment, rejecting safety assessment, an assumed diagnosis or a self-harm interpretation. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]
- Fails closed by: ACCEPTED — Failing the primary result when the requested explanatory purpose is distorted by those claims. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.8.13 — A1-R08 — Explanation rather than defence against judgment: supplies the complete frozen source and perspective values. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08]
- Gated by: ACCEPTED — C-GOLD.8.5 — Benchmark annotation fields: this distinct proposed telling retains its evidence relation and recorded firmness basis. [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.8.13 — A1-R08 — Explanation rather than defence against judgment | The positive explanatory purpose stated in contrast to defensive preparation. | supplies the required purpose of explaining lived experience. | Proposed `direct self-report` and separately applied `high_firmness`; basis: the explicit contrast between rejected and required purposes. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §11 / A1-R08] |

SUB-PARTS: NONE

### C-GOLD.9 — Protected contextual-gold draft
Stamp: DESIGNED    Source: [CR §4B / GOLD SET FILES]

ALONE
- What it is: DESIGNED — `NH_GOLD_SET_CONTEXT_v1.md`, the separately recorded drafted/approved contextual-gold file, not yet placed in `nh_engine_core` or sealed at the last verified record. [CR §4B / GOLD SET FILES]
- Takes in: NOT DECIDED
- Does: DESIGNED — Retains protected-file treatment when placed. [CR §4B / GOLD SET FILES]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Be represented as an already placed or sealed runtime artifact, or lose protected treatment when placed. [CR §4B / GOLD SET FILES]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — Placement of the draft in `nh_engine_core` activates its protected-file treatment. [CR §4B / GOLD SET FILES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-GOLD — Sealed gold sets v1, v2-B (§7C) | NOT DECIDED | supplies the separate draft's protection and placement boundary, without claiming a sealed runtime artifact. | NOT DECIDED | [CR §4B / GOLD SET FILES] |

SUB-PARTS: NONE


<!-- END BEHAVIOR -->

## Cross-piece continuation entries

Both endpoints are named together; the earlier files remain unchanged.

| Using card | Defining or supplying card | Reciprocal entry | Source |
|---|---|---|---|
| C-GOLD — Sealed gold sets v1, v2-B (§7C) | C-GOLD.1 — Promotion evaluation-evidence bridge | ACCEPTED — USED BY continuation for Fed by: supplies separate narrow evidence references within CY-G while retaining C-GOLD's gold-examination ownership. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] |
| C-GOLD.6.2 — Live before nightly | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | DESIGNED — USED BY continuation for Gated by: the live path is the prerequisite that must be built before nightly deepening. | [V10 §7C] |
| C-GOLD.7 — Gold operation records | C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B) | DESIGNED — USED BY continuation for Gated by: shared living-record rules require traceable operations without automatic recursive logging or double evidence. | [V10 §0B] |
| C-GOLD.7 — Gold operation records | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED — USED BY continuation for Gated by: record use remains subject to protection and access authorization; permanent recording grants no automatic access. | [MAP C-GOLD] [V10 §0B] |
| C-GOLD.8.2.2 — Keep missing-root cases unpinned | C-STORE — Accretive store & sealed roots (§6B) | ACCEPTED — USED BY continuation for Gated by: future root creation uses the accepted B11 active writable-batch architecture; the existing sealed batch is immutable. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §6] |
| C-GOLD.8.3.2 — Theme result | C-READ.10.14.8.7 — Confirmation remains separate | ACCEPTED — USED BY continuation for Gated by: a benchmark reference grants no operational theme confirmation. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.2] |
| C-GOLD.8.5.5 — Structured benchmark perspective | C-READ.10.1.23 — Perspective roles stay distinct | ACCEPTED — USED BY continuation for Gated by: common field definitions retain distinct roles rather than reducing them to a single “whose” value. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §8] |
| C-GOLD.8.5.6 — Benchmark evidence relationship | C-READ.10.1.8 — evidence_relationship | ACCEPTED — USED BY continuation for Gated by: the existing five-value field contract governs the benchmark's mapping. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §7.3] |
| C-GOLD.8.5.8 — Benchmark firmness and basis | C-READ.10.1.11 — firmness | ACCEPTED — USED BY continuation for Gated by: the existing label policy supplies the six outcomes and nonnumeric boundary. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §9] |
| C-GOLD.8.5.8 — Benchmark firmness and basis | C-READ.10.1.12 — firmness_evidence_basis | ACCEPTED — USED BY continuation for Gated by: every non-omitted label requires recorded source support. | [04/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md §9] |
| C-GOLD.1 — Promotion evaluation-evidence bridge | C-GOLD — Sealed gold sets v1, v2-B (§7C) | ACCEPTED — Reciprocates the bridge's existing Fed by link from CH03-e; CH03-g/h retain the same C-GOLD/C-GOLD.1 continuation. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] |
| C-ENGINE-AB — Engines A & B (§7C, §16) | C-GOLD — Sealed gold sets v1, v2-B (§7C) | BUILT — Reciprocates CH03-i's C-ENGINE-AB Fed by link. | [V10 §5 / Accretive store + tooling] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Minimal engine A and Engine B rows] |
| C-ENGINE-AB.1.3 — Engine A run_on_gold() | C-GOLD — Sealed gold sets v1, v2-B (§7C) | BUILT — Reciprocates CH03-i's Engine A run_on_gold() supplier link. | [V10 §5 / Accretive store + tooling] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Minimal engine A row] |
| C-ENGINE-AB.2.4 — Engine B run_on_gold() | C-GOLD — Sealed gold sets v1, v2-B (§7C) | BUILT — Reciprocates CH03-i's Engine B run_on_gold() supplier link. | [V10 §5 / Accretive store + tooling] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine B row] |
| C-ENGINE-C.7 — Story-bearing benchmark prerequisite | C-GOLD — Sealed gold sets v1, v2-B (§7C) | DESIGNED — Reciprocates both Fed by and Gated by links in CH03-j's story-bearing benchmark prerequisite. | [MAP C-GOLD] [V10 §7C] |

## Appendix A carry-forward — this piece

| Part | Field | Occurrence | Value |
|---|---|---|---|
| C-GOLD — Sealed gold sets v1, v2-B (§7C) | Changes | 1 | NOT DECIDED |
| C-GOLD.2 — Gold v1 | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.2 — Gold v1 | Fed by | 1 | NOT DECIDED |
| C-GOLD.2 — Gold v1 | Changes | 1 | NOT DECIDED |
| C-GOLD.2.1 — Gold v1 seal marker | Takes in | 1 | NOT DECIDED |
| C-GOLD.2.1 — Gold v1 seal marker | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.2.1 — Gold v1 seal marker | Fed by | 1 | NOT DECIDED |
| C-GOLD.2.1 — Gold v1 seal marker | Gated by | 1 | NOT DECIDED |
| C-GOLD.2.1 — Gold v1 seal marker | Changes | 1 | NOT DECIDED |
| C-GOLD.3 — Gold v2-B | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.3 — Gold v2-B | Fed by | 1 | NOT DECIDED |
| C-GOLD.3 — Gold v2-B | Changes | 1 | NOT DECIDED |
| C-GOLD.3.1 — Gold v2-B seal marker | Takes in | 1 | NOT DECIDED |
| C-GOLD.3.1 — Gold v2-B seal marker | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.3.1 — Gold v2-B seal marker | Fed by | 1 | NOT DECIDED |
| C-GOLD.3.1 — Gold v2-B seal marker | Gated by | 1 | NOT DECIDED |
| C-GOLD.3.1 — Gold v2-B seal marker | Changes | 1 | NOT DECIDED |
| C-GOLD.4 — Six gold scoring rules | Fed by | 1 | NOT DECIDED |
| C-GOLD.4 — Six gold scoring rules | Changes | 1 | NOT DECIDED |
| C-GOLD.4.1 — Semantic match | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.4.1 — Semantic match | Fed by | 1 | NOT DECIDED |
| C-GOLD.4.1 — Semantic match | Gated by | 1 | NOT DECIDED |
| C-GOLD.4.1 — Semantic match | Changes | 1 | NOT DECIDED |
| C-GOLD.4.2 — Legacy story-layer exclusion | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.4.2 — Legacy story-layer exclusion | Fed by | 1 | NOT DECIDED |
| C-GOLD.4.2 — Legacy story-layer exclusion | Gated by | 1 | NOT DECIDED |
| C-GOLD.4.2 — Legacy story-layer exclusion | Changes | 1 | NOT DECIDED |
| C-GOLD.4.3 — Invention and omission | Fed by | 1 | NOT DECIDED |
| C-GOLD.4.3 — Invention and omission | Gated by | 1 | NOT DECIDED |
| C-GOLD.4.3 — Invention and omission | Changes | 1 | NOT DECIDED |
| C-GOLD.4.4 — Correct and invented extras | Fed by | 1 | NOT DECIDED |
| C-GOLD.4.4 — Correct and invented extras | Gated by | 1 | NOT DECIDED |
| C-GOLD.4.4 — Correct and invented extras | Changes | 1 | NOT DECIDED |
| C-GOLD.4.5 — Multiple acceptable readings | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.4.5 — Multiple acceptable readings | Fed by | 1 | NOT DECIDED |
| C-GOLD.4.5 — Multiple acceptable readings | Gated by | 1 | NOT DECIDED |
| C-GOLD.4.5 — Multiple acceptable readings | Changes | 1 | NOT DECIDED |
| C-GOLD.4.6 — Ness-owned pass/fail | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.4.6 — Ness-owned pass/fail | Fed by | 1 | NOT DECIDED |
| C-GOLD.4.6 — Ness-owned pass/fail | Changes | 1 | NOT DECIDED |
| C-GOLD.5 — Insufficient-context engine result | Fed by | 1 | NOT DECIDED |
| C-GOLD.5 — Insufficient-context engine result | Changes | 1 | NOT DECIDED |
| C-GOLD.6 — Protected engine build order | Fed by | 1 | NOT DECIDED |
| C-GOLD.6 — Protected engine build order | Changes | 1 | NOT DECIDED |
| C-GOLD.6.1 — Story gold before Engine C | Changes | 1 | NOT DECIDED |
| C-GOLD.6.2 — Live before nightly | Fed by | 1 | NOT DECIDED |
| C-GOLD.6.2 — Live before nightly | Changes | 1 | NOT DECIDED |
| C-GOLD.6.3 — Benchmark before wider-reading claims | Fed by | 1 | NOT DECIDED |
| C-GOLD.6.3 — Benchmark before wider-reading claims | Changes | 1 | NOT DECIDED |
| C-GOLD.7 — Gold operation records | Changes | 1 | NOT DECIDED |
| C-GOLD.7.1 — annotator | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.7.1 — annotator | Fed by | 1 | NOT DECIDED |
| C-GOLD.7.1 — annotator | Changes | 1 | NOT DECIDED |
| C-GOLD.7.2 — when | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.7.2 — when | Fed by | 1 | NOT DECIDED |
| C-GOLD.7.2 — when | Gated by | 1 | NOT DECIDED |
| C-GOLD.7.2 — when | Changes | 1 | NOT DECIDED |
| C-GOLD.7.3 — context_version | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.7.3 — context_version | Fed by | 1 | NOT DECIDED |
| C-GOLD.7.3 — context_version | Gated by | 1 | NOT DECIDED |
| C-GOLD.7.3 — context_version | Changes | 1 | NOT DECIDED |
| C-GOLD.7.4 — change_reason | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.7.4 — change_reason | Fed by | 1 | NOT DECIDED |
| C-GOLD.7.4 — change_reason | Gated by | 1 | NOT DECIDED |
| C-GOLD.7.4 — change_reason | Changes | 1 | NOT DECIDED |
| C-GOLD.8 — A1 replacement story-gold | Changes | 1 | NOT DECIDED |
| C-GOLD.8.1 — Frozen replacement-source identity | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.8.1 — Frozen replacement-source identity | Fed by | 1 | NOT DECIDED |
| C-GOLD.8.1 — Frozen replacement-source identity | Gated by | 1 | NOT DECIDED |
| C-GOLD.8.1 — Frozen replacement-source identity | Changes | 1 | NOT DECIDED |
| C-GOLD.8.2 — Legitimate root pinning | Changes | 1 | NOT DECIDED |
| C-GOLD.8.2.1 — Pin verified existing roots | Fed by | 1 | NOT DECIDED |
| C-GOLD.8.2.1 — Pin verified existing roots | Changes | 1 | NOT DECIDED |
| C-GOLD.8.2.2 — Keep missing-root cases unpinned | Fed by | 1 | NOT DECIDED |
| C-GOLD.8.2.2 — Keep missing-root cases unpinned | Changes | 1 | NOT DECIDED |
| C-GOLD.8.3 — Separate primary and theme grading | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.8.3 — Separate primary and theme grading | Changes | 1 | NOT DECIDED |
| C-GOLD.8.3.1 — Primary Story-Layer result | Fed by | 1 | NOT DECIDED |
| C-GOLD.8.3.1 — Primary Story-Layer result | Changes | 1 | NOT DECIDED |
| C-GOLD.8.3.2 — Theme result | Fed by | 1 | NOT DECIDED |
| C-GOLD.8.3.2 — Theme result | Changes | 1 | NOT DECIDED |
| C-GOLD.8.4 — Shared story-case boundaries | Fed by | 1 | NOT DECIDED |
| C-GOLD.8.4 — Shared story-case boundaries | Changes | 1 | NOT DECIDED |
| C-GOLD.8.5 — Benchmark annotation fields | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.8.5 — Benchmark annotation fields | Changes | 1 | NOT DECIDED |
| C-GOLD.8.5.1 — Case identifier | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.8.5.1 — Case identifier | Fed by | 1 | NOT DECIDED |
| C-GOLD.8.5.1 — Case identifier | Gated by | 1 | NOT DECIDED |
| C-GOLD.8.5.1 — Case identifier | Changes | 1 | NOT DECIDED |
| C-GOLD.8.5.2 — Unpinned source anchor | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.8.5.2 — Unpinned source anchor | Gated by | 1 | NOT DECIDED |
| C-GOLD.8.5.2 — Unpinned source anchor | Changes | 1 | NOT DECIDED |
| C-GOLD.8.5.3 — Exact target | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.8.5.3 — Exact target | Fed by | 1 | NOT DECIDED |
| C-GOLD.8.5.3 — Exact target | Gated by | 1 | NOT DECIDED |
| C-GOLD.8.5.3 — Exact target | Changes | 1 | NOT DECIDED |
| C-GOLD.8.5.4 — Frozen context | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.8.5.4 — Frozen context | Fed by | 1 | NOT DECIDED |
| C-GOLD.8.5.4 — Frozen context | Gated by | 1 | NOT DECIDED |
| C-GOLD.8.5.4 — Frozen context | Changes | 1 | NOT DECIDED |
| C-GOLD.8.5.5 — Structured benchmark perspective | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.8.5.5 — Structured benchmark perspective | Fed by | 1 | NOT DECIDED |
| C-GOLD.8.5.5 — Structured benchmark perspective | Changes | 1 | NOT DECIDED |
| C-GOLD.8.5.6 — Benchmark evidence relationship | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.8.5.6 — Benchmark evidence relationship | Fed by | 1 | NOT DECIDED |
| C-GOLD.8.5.6 — Benchmark evidence relationship | Changes | 1 | NOT DECIDED |
| C-GOLD.8.5.7 — Proposed telling | Fed by | 1 | NOT DECIDED |
| C-GOLD.8.5.7 — Proposed telling | Changes | 1 | NOT DECIDED |
| C-GOLD.8.5.8 — Benchmark firmness and basis | Fed by | 1 | NOT DECIDED |
| C-GOLD.8.5.8 — Benchmark firmness and basis | Changes | 1 | NOT DECIDED |
| C-GOLD.8.5.9 — Proposed theme reference | Fed by | 1 | NOT DECIDED |
| C-GOLD.8.5.9 — Proposed theme reference | Changes | 1 | NOT DECIDED |
| C-GOLD.8.5.10 — Acceptable alternative | Fed by | 1 | NOT DECIDED |
| C-GOLD.8.5.10 — Acceptable alternative | Changes | 1 | NOT DECIDED |
| C-GOLD.8.5.11 — Invention and failure boundary | Fed by | 1 | NOT DECIDED |
| C-GOLD.8.5.11 — Invention and failure boundary | Changes | 1 | NOT DECIDED |
| C-GOLD.8.5.12 — Benchmark annotation provenance | Fed by | 1 | NOT DECIDED |
| C-GOLD.8.5.12 — Benchmark annotation provenance | Changes | 1 | NOT DECIDED |
| C-GOLD.8.6 — A1-R01 — Forced explanation of an unseen inner process | Changes | 1 | NOT DECIDED |
| C-GOLD.8.6.1 — A1-R01 telling 1 | Changes | 1 | NOT DECIDED |
| C-GOLD.8.7 — A1-R02 — Use the whole accumulated conversation | Changes | 1 | NOT DECIDED |
| C-GOLD.8.7.1 — A1-R02 telling 1 | Changes | 1 | NOT DECIDED |
| C-GOLD.8.8 — A1-R03 — Lifelong active trauma while still seeking help | Changes | 1 | NOT DECIDED |
| C-GOLD.8.8.1 — A1-R03 telling 1 | Changes | 1 | NOT DECIDED |
| C-GOLD.8.8.2 — A1-R03 telling 2 | Changes | 1 | NOT DECIDED |
| C-GOLD.8.9 — A1-R04 — Ongoing source, non-linear processing, and minimization | Changes | 1 | NOT DECIDED |
| C-GOLD.8.9.1 — A1-R04 telling 1 | Changes | 1 | NOT DECIDED |
| C-GOLD.8.9.2 — A1-R04 telling 2 | Changes | 1 | NOT DECIDED |
| C-GOLD.8.9.3 — A1-R04 telling 3 | Changes | 1 | NOT DECIDED |
| C-GOLD.8.10 — A1-R05 — Collapse as overload while pushing beyond bodily limits to reach help | Changes | 1 | NOT DECIDED |
| C-GOLD.8.10.1 — A1-R05 telling 1 | Changes | 1 | NOT DECIDED |
| C-GOLD.8.10.2 — A1-R05 telling 2 | Changes | 1 | NOT DECIDED |
| C-GOLD.8.10.3 — A1-R05 telling 3 | Changes | 1 | NOT DECIDED |
| C-GOLD.8.11 — A1-R06 — Explain the mechanism instead of naming the gap | Changes | 1 | NOT DECIDED |
| C-GOLD.8.11.1 — A1-R06 telling 1 | Changes | 1 | NOT DECIDED |
| C-GOLD.8.11.2 — A1-R06 telling 2 | Changes | 1 | NOT DECIDED |
| C-GOLD.8.12 — A1-R07 — Thorough analysis instead of sweet talk | Changes | 1 | NOT DECIDED |
| C-GOLD.8.12.1 — A1-R07 telling 1 | Changes | 1 | NOT DECIDED |
| C-GOLD.8.12.2 — A1-R07 telling 2 | Changes | 1 | NOT DECIDED |
| C-GOLD.8.13 — A1-R08 — Explanation rather than defence against judgment | Changes | 1 | NOT DECIDED |
| C-GOLD.8.13.1 — A1-R08 telling 1 | Changes | 1 | NOT DECIDED |
| C-GOLD.8.13.2 — A1-R08 telling 2 | Changes | 1 | NOT DECIDED |
| C-GOLD.9 — Protected contextual-gold draft | Takes in | 1 | NOT DECIDED |
| C-GOLD.9 — Protected contextual-gold draft | Gives out | 1 | NOT DECIDED |
| C-GOLD.9 — Protected contextual-gold draft | Fails closed by | 1 | NOT DECIDED |
| C-GOLD.9 — Protected contextual-gold draft | Fed by | 1 | NOT DECIDED |
| C-GOLD.9 — Protected contextual-gold draft | Changes | 1 | NOT DECIDED |
| C-GOLD.2.1 — Gold v1 seal marker | USED BY row 1 / Takes in there | 1 | NOT DECIDED |
| C-GOLD.3.1 — Gold v2-B seal marker | USED BY row 1 / Takes in there | 1 | NOT DECIDED |
| C-GOLD.9 — Protected contextual-gold draft | USED BY row 1 / Takes in there | 1 | NOT DECIDED |
| C-GOLD.9 — Protected contextual-gold draft | USED BY row 1 / Changes there | 1 | NOT DECIDED |

## Source coverage and explicit deferrals

| Source scope | Card or later piece | Coverage boundary |
|---|---|---|
| V10 status table gold v1/v2-B, scoring, failure and engine rows; V10 §5 physical stores and engine tools; §6; §11 item 20 | C-GOLD; .2–.5 | Built artifacts and their counts/markers are distinct from designed scoring and failure policy. All seven published B-case prefixes, target descriptions and recorded outcomes are retained. The sealed files' unpublished full case contents are not inferred. |
| DD §3D; MAP C-GOLD; CR §4B GOLD SET FILES | C-GOLD.2–.7 | Six scoring rules, sealed-case immutability, new-version correction, both-set model benchmark, old producer provenance, no mass reread, protected contextual-gold draft and operation metadata. |
| V10 §7C, complete subsection; MAP C-GOLD | C-GOLD.6 and three gate cards | Story-gold before Engine C tests; live before nightly; larger-model/context full-thread performance must be benchmarked. |
| V10 §0B, complete section; MAP C-GOLD | C-GOLD.7 and four annotation-metadata fields; shared lifecycle remains CH02 | One operation/one log, permanent connected records without double evidence or recursive log creation; protection and authorization remain applicable. |
| Accepted evaluation bridge §2.5 and §3; existing CH03-e–h continuation rows | C-GOLD Fed by and SUB-PARTS name existing C-GOLD.1; incoming use and continuation | No duplicate bridge card. Aggregate derivation is CH03-m; AP-1–AP-12 and remaining bridge coverage are CH03-n. |
| A1 content §§4–6; design closure §§5–9; acceptance receipt §§4–5; closure receipt §§2,6–8 | C-GOLD.8; .8.1; .8.2 and conditional branches | Exact frozen identity, accepted design versus deferred implementation, unpinned benchmark labels, verified existing-root branch and separate B11-ingest branch. The historical missing set is not reconstructed. |
| A1 content §7.1–7.3 | C-GOLD.4; .8.3; .8.3.1; .8.3.2; .8.5.6 | Legacy six-rule list is unchanged; separate primary and theme judgments; four combinations; exact five-value evidence vocabulary. |
| A1 content §§8–10,12 | C-GOLD.8.4; .8.5 and field cards; existing C-READ.10.1 field definitions | All context, local perspective, evidence, firmness, theme and non-invention boundaries. Six firmness outcomes, basis requirement, nonnumeric policy and honest coverage. Case annotations remain proposed benchmark annotations. |
| A1 content §11, all eight complete case sections | C-GOLD.8.6–.8.13 and telling/theme children | All exact target/frozen-context data; anchors and structured perspective; every proposed telling, evidence relation, firmness label/basis, semantic alternative, theme and failure boundary. |
| A1 content §§1–3,13–15; receipts and historical blocker narrative | Status/provenance in READ RECORD and .8/.8.1; project acts and workflow EXCLUDED under contract §1.3 | No claim of opening the original PDF or companion transcript. Source access is through the accepted frozen A1 file. Root pinning, runtime sealing, executable benchmark and implementation remain separate; theme runtime mechanics go to CH06-b; model choice goes to CH10-b. |
| Existing CH03-i and CH03-j links to C-GOLD | C-GOLD USED BY and cross-piece continuation rows | Both engine gold-run entry points, aggregate A/B use and Engine C story-benchmark prerequisite are reciprocated without modifying their files. |
| DD §3D, deferred retry trigger | CH05-d C-7H | The insufficient-context result is covered here; a trigger for revisiting it is not supplied by the source and remains a named later-piece gap. |
| Bridge acceptance receipt §§0–6 | READ RECORD status only; C-GOLD/C-GOLD.1 wiring consumes source §§2.5,3 | The receipt establishes accepted source bytes; no workflow or build claim is imported. |
| A1 §8 shared field/evidence rules and §§7.3,9 label details | C-GOLD.8.4–.8.5; reused atomic C-READ.10.1.4–.8, .11–.12 and C-READ.10.1.23; Engine C evidence decomposition in CH03-j C-ENGINE-C.2–.5,.10–.11 | Existing atomic definitions are referenced, not re-created under duplicate names; all case-specific values and the entire five-value evidence/six-outcome firmness vocabularies are written here. |

## Review of plain gates

| Card | Reason no other card is named |
|---|---|
| C-GOLD.4.6 — Ness-owned pass/fail | Ness's pass/fail act is a genuine personal decision, allowed as a plain gate by lessons 3.3. |
| C-GOLD.8.2 — Legitimate root pinning | Separate implementation authorization is Ness's act; it is not a hidden card or an inferred automatic mechanism. |
| C-GOLD.9 — Protected contextual-gold draft | Placement is the explicitly stated precondition of protected treatment; it is not an invented runtime gate. |

## Coverage matrix — carried source inventory

The following inventory retains the preceding pieces’ placements and read status. This piece’s additional placements and deferrals are in the source-scope table above; inherited notes are not fresh whole-read claims.
### File coverage

| Row | Source | Read scope | Placement |
|---|---|---|---|
| F001 | `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped reread for CH03-l; prior whole-read credit retained where previously recorded | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.1; C-STORE.2; C-STORE.3; CY-A Chapter 3-b: C-READ and its v1 record, validator, writer, quarantine, production-boundary and operation-record sub-parts; CY-A/CY-F reading-write interfaces. Chapter 3-c: governing checks for C-READ.10; A2/firmness additions stay ACCEPTED, never BUILT. Chapter 3-d: source-status and no-production-write boundaries; governing operational living-memory rule at C-READ.11.9.4.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.3, C-ENGINE-C.3.1, C-ENGINE-C.3.2, C-ENGINE-C.3.3, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.11.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1, C-ENGINE-AB.1.1, C-ENGINE-AB.1.2, C-ENGINE-AB.1.3, C-ENGINE-AB.2, C-ENGINE-AB.2.1, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.1, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.2.4, C-ENGINE-AB.3, C-ENGINE-AB.4, C-ENGINE-AB.5, C-ENGINE-AB.6, C-ENGINE-AB.8, C-ENGINE-AB.9.; CH03-k: C-INDEX, C-INDEX.1, C-INDEX.1.1, C-INDEX.1.2, C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.1, C-INDEX.4.2, C-INDEX.4.3, C-INDEX.4.4, C-INDEX.4.5, C-INDEX.4.7, C-INDEX.4.8, C-INDEX.5, C-INDEX.6.; CH03-l: C-GOLD, C-GOLD.2, C-GOLD.2.1, C-GOLD.3, C-GOLD.3.1, C-GOLD.6, C-GOLD.6.1, C-GOLD.6.2, C-GOLD.6.3, C-GOLD.7, C-GOLD.7.4. |
| F002 | `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Scoped reread for CH03-l; prior whole-read credit retained where previously recorded | EXCLUDED: interaction/workflow guidance under §1.3 and §2.4. NOT PLACED: remaining behavior belongs to other component groups.; Chapter 3-a: C-STORE.2.3 Chapter 3-b: C-READ.1 confidence semantics and C-READ.2 uncertainty-preserving shape gate; remaining scope retained. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.2, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.8.; CH03-l: C-GOLD, C-GOLD.2, C-GOLD.2.1, C-GOLD.3, C-GOLD.3.1, C-GOLD.4, C-GOLD.4.1, C-GOLD.4.2, C-GOLD.4.3, C-GOLD.4.4, C-GOLD.4.5, C-GOLD.4.6, C-GOLD.5, C-GOLD.6, C-GOLD.6.1, C-GOLD.6.3, C-GOLD.8.3, C-GOLD.8.5.10, C-GOLD.8.5.11. |
| F003 | `01_AUTHORITATIVE/cursorrules` | Scoped reread for CH03-l; prior whole-read credit retained where previously recorded | EXCLUDED: coding-process rules under §1.3. NOT PLACED: built-code boundaries belong to store, reader and code-boundary groups. Chapter 3-b: C-READ.1.12 per-store/global-key conflict and C-READ.3 shared write boundary; workflow remains excluded. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB.5.; CH03-k: C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.6.; CH03-l: C-GOLD, C-GOLD.9. |
| F004 | `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; Chapter 3-c focused rule/boundary searches and excerpts, no new whole-read claim | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. |
| F005 | `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped reread for CH03-l; prior whole-read credit retained where previously recorded | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.3.4; CY-A Chapter 3-b: C-READ component name, operation logging and consumer/caller relationships; CY-A/CY-F interfaces. Chapter 3-c: component ownership/names and Group A/D boundary; accepted A2 supplies behavior. Chapter 3-d: names, Group A ownership and per-reading seam versus full CY-G boundary.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.9.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1.1, C-ENGINE-AB.1.3, C-ENGINE-AB.2.1, C-ENGINE-AB.2.4, C-ENGINE-AB.4, C-ENGINE-AB.6, C-ENGINE-AB.6.1.; CH03-k: C-INDEX, C-INDEX.2, C-INDEX.3, C-INDEX.5, C-INDEX.6, C-INDEX.6.1, C-INDEX.6.2, C-INDEX.6.3, C-INDEX.6.4, C-INDEX.6.5, C-INDEX.6.6.; CH03-l: C-GOLD, C-GOLD.4, C-GOLD.4.6, C-GOLD.6, C-GOLD.6.2, C-GOLD.7, C-GOLD.7.1, C-GOLD.7.2, C-GOLD.7.3, C-GOLD.7.4. |
| F006 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F007 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F008 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F009 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F010 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F011 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.9 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F012 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F013 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F014 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F015 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F016 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F017 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_GOLD_CASES_MISSING_SOURCE_BLOCKER_RECORD_v1_0.md` | Scoped reread for CH03-l; prior whole-read credit retained where previously recorded | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker.; CH03-l: Status/provenance only; no behavior from this receipt or historical blocker. |
| F018 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH03-l | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker.; CH03-l: Status/provenance only; no behavior from this receipt or historical blocker. |
| F019 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md` | Scoped reread for CH03-l; prior whole-read credit retained where previously recorded | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-j: C-ENGINE-C.7.; CH03-l: C-GOLD, C-GOLD.6.1, C-GOLD.8, C-GOLD.8.1, C-GOLD.8.2, C-GOLD.8.2.1, C-GOLD.8.5.12. |
| F020 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md` | Scoped reread for CH03-l; prior whole-read credit retained where previously recorded | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker.; CH03-l: C-GOLD.8, C-GOLD.8.5.12. |
| F021 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md` | Read whole for CH03-l | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-l: C-GOLD.6.1, C-GOLD.8, C-GOLD.8.2, C-GOLD.8.2.1, C-GOLD.8.2.2, C-GOLD.8.3, C-GOLD.8.3.1, C-GOLD.8.3.2, C-GOLD.8.4, C-GOLD.8.5, C-GOLD.8.5.1, C-GOLD.8.5.2, C-GOLD.8.5.3, C-GOLD.8.5.4, C-GOLD.8.5.5, C-GOLD.8.5.6, C-GOLD.8.5.7, C-GOLD.8.5.8, C-GOLD.8.5.9, C-GOLD.8.5.10, C-GOLD.8.5.11, C-GOLD.8.5.12, C-GOLD.8.6, C-GOLD.8.6.1, C-GOLD.8.7, C-GOLD.8.7.1, C-GOLD.8.8, C-GOLD.8.8.1, C-GOLD.8.8.2, C-GOLD.8.9, C-GOLD.8.9.1, C-GOLD.8.9.2, C-GOLD.8.9.3, C-GOLD.8.10, C-GOLD.8.10.1, C-GOLD.8.10.2, C-GOLD.8.10.3, C-GOLD.8.11, C-GOLD.8.11.1, C-GOLD.8.11.2, C-GOLD.8.12, C-GOLD.8.12.1, C-GOLD.8.12.2, C-GOLD.8.13, C-GOLD.8.13.1, C-GOLD.8.13.2. |
| F022 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F023 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F024 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F025 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F026 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F027 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F028 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F029 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F030 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F031 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F032 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F033 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F034 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0 .md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F035 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F036 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md` | Scoped reread for CH03-j; prior whole-read credit retained where previously recorded | C-READ.10 and all A2-cited descendants: §§1–10 identity, card/preparation/event ownership, acceptance/correspondence, commit/recovery, legacy mapping, lifecycle, semantic/safety boundaries, references/rereading and logging. EXCLUDED: source revision history, acts of acceptance, implementation workflow and self-audit claims under §1.3. Other consumer mechanics remain with their owning groups.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards.; CH03-j: C-ENGINE-C, C-ENGINE-C.3.3, C-ENGINE-C.4, C-ENGINE-C.5, C-ENGINE-C.6, C-ENGINE-C.9, C-ENGINE-C.11. |
| F037 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_PACKAGE_COMPLETE_RECORD_v1_0.md` | Read whole for CH03-j | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker. |
| F038 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F039 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F040 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F041 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F042 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F043 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F044 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F045 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F046 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F047 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F048 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified | Chapter 3-a: ACCEPTED status evidence for C-STORE.4; receipt narrative excluded under §1.3. EXCLUDED: source history/workflow under §1.3. |
| F049 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | Chapter 3-a: C-STORE.4 and all descendants. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: §10 cross-batch reading reread for boundary check; no new B11 behavior written here, Chapter 3-a placement retained. |
| F050 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F051 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F052 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Scoped reread for CH03-l; prior whole-read credit retained where previously recorded | Status/identity checked for NHD-B16EEB; globally unique slot identifiers retained; acceptance narrative EXCLUDED by §1.3; CH03-l: Status/provenance only; no behavior from this receipt or historical blocker. |
| F053 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | §§2–6 establish exact accepted standalone scope and source identity. EXCLUDED from behavior: receipt history/roles/process; no mechanism sourced from receipt. |
| F054 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | C-READ.11 and every descendant: complete §§1–11 seam; §13 traces checked against the same rules. §12 external ownership and unspecified details recorded separately. EXCLUDED under §1.3: source status/history/process, self-audit and delivery narrative (§§14–15). |
| F055 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F056 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F057 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md` | Newly read whole for this correction, all 1,938 lines; pinned Git blob verified; Chapter 3-c focused retry/malformed searches and §§2.8/3.7 excerpts; prior whole-read credit retained | C-READ.7.2 and its reciprocal C-READ.7 link: ACCEPTED guard from §1.2 (NHD-B24), matching FR-0608 CARRIED. Remaining B24 behavior NOT PLACED: belongs to later owning templates; no other B24 mechanism added here. Chapter 3-c C-READ.10.3.8.8 and source-conflict register: structural-disposition difference retained against A2; no new retry policy. |
| F058 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_PACKAGE_COMPLETE_RECORD_v1_0.md` | Newly read whole for this correction, all 132 lines; pinned Git blob verified | §§2–3, 5 and 12 establish the accepted standalone status and exact v7 identity used for C-READ.7.2; no behavior sourced from this receipt. EXCLUDED: closure history/process under §1.3; no implementation or integration claimed. |
| F059 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F060 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F061 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F062 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F063 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F064 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1 and cited sub-parts; C-7B.7.4.7 and cited sub-parts; C-7B.7.5.3 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F065 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F066 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F067 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F068 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1.6 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F069 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F070 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_CANDIDATE_v1_4.md` | Carried through Chapter 3-a: Not yet read; whole file newly read in Chapter 3-b | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-b: EXCLUDED: status/consolidation and workflow narrative under §1.3. Used for locating later accepted owners only; it supplies no behavior in this piece. |
| F071 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F072 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F073 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F074 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F075 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F076 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F077 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F078 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F079 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F080 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F081 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F082 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F083 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified | Chapter 3-a: ACCEPTED status evidence for Bundle 6 mechanics; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. |
| F084 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified | Chapter 3-a: C-STORE.5 / operation protections, B17, B20, B21; other component scopes NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. |
| F085 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified | Chapter 3-a: ACCEPTED status evidence for Origin policy; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. |
| F086 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | Chapter 3-a: C-STORE.5 / Origin preservation policy; A3.4–A3.5 and other components NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: Navigation excerpt only; no new behavior sourced in this piece.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.7, C-ENGINE-AB.8. |
| F087 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F088 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F089 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F090 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F091 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F092 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F093 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F094 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F095 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F096 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F097 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F098 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F099 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH03-j | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker. |
| F100 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md` | Scoped reread for CH03-j; prior whole-read credit retained where previously recorded | C-READ.10.1.11; C-READ.10.1.12 and all firmness-policy-cited descendants: §§1–6 qualitative outcomes, evidence basis, separations, revision and no-numeric-scoring. EXCLUDED: package history/process; future policy and consumer schemas not invented.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards.; CH03-j: C-ENGINE-C, C-ENGINE-C.10. |
| F101 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F102 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F103 | `05_ACTIVE_CANDIDATE/02-NH_BUNDLE_6_A3_DECISIONS_WORKING_RECORD_v1-1-.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F104 | `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWERS.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F105 | `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWER_PROVENANCE.json` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F106 | `05_ACTIVE_CANDIDATE/Music_Media_Intent_Excerpts.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F107 | `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F108 | `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F109 | `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F110 | `05_ACTIVE_CANDIDATE/NH_A19_REMAINING_HUMAN_EXPERIENCE_DESIGN_PLAN_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F111 | `05_ACTIVE_CANDIDATE/NH_A2_CURRENT_STATUS_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F112 | `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` | Scoped reread for CH03-l; prior whole-read credit retained where previously recorded | C-GOLD.1 identities/records/currentness in 3-e; C-GOLD.1.5 operation/execution contracts in 3-f; C-GOLD.1.6 judgment chain/conditional proof in 3-g; C-GOLD.1.7 claim lifecycle/protected recovery in 3-h; derivation, applicability and remaining dependencies NOT PLACED: later pieces; CH03-l: C-GOLD. |
| F113 | `05_ACTIVE_CANDIDATE/NH_B24_REJECTION_CATEGORY_DECISION_2026-09-23_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F114 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F115 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read whole; NHD-B24 row searched for this correction; Chapter 3-c NHD-A2/NHD-SLF and dependency navigation searches, not a whole-file read; Chapter 3-d NHD-B16/NHD-B16EEB navigation only | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; Chapter 3-a: Navigation only: NHD-B11 and NHD-BU1; no behavior sourced from the index; this correction: NHD-B24 navigation for C-READ.7.2 Chapter 3-c: NHD-A2/NHD-SLF navigation only. Chapter 3-d: navigation only, no behavior sourced from index. |
| F116 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F117 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F118 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F119 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F120 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F121 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F122 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F123 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_MODEL_CANDOR_AND_HONESTY_STACK_v1_CANDIDATE.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F124 | `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_2026-09-24_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7A.10; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F125 | `05_ACTIVE_CANDIDATE/NH_DESIGN_ANSWERS.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F126 | `05_ACTIVE_CANDIDATE/NH_PERSONAL_IDEA_NOTE_A19_VR_WORLD_ROOMS_OFFLINE_CREATION_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F127 | `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Identity/hash verified; Stage 2 reading pending except FR-0125 and FR-0608 rows checked for this correction (classification and accepted-home pointer only) | NOT PLACED: Appendix B requires Stage 2 rows by FR-ID/title only; no behavior sourced from the ledger. |
| F128 | `05_ACTIVE_CANDIDATE/Other_Future_Feature_Intent_Excerpts.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F129 | `05_ACTIVE_CANDIDATE/Thought_Branches_and_Simulation_Intent.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F130 | `05_INACTIVE_CANDIDATE/NH_FUTURE_MUSIC_UNDERSTANDING_AND_MUSIC_SERVICE_CONNECTIONS_PACKAGE_INTAKE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F131 | `05_INACTIVE_CANDIDATE/NH_ISSUE_CHANNEL_INTENT_v0_1.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F132 | `05_INACTIVE_CANDIDATE/NH_PROVENANCE_FIRST_MULTI_INDEX_MEMORY_FABRIC_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F133 | `05_INACTIVE_CANDIDATE/NH_SECURITY_STORAGE_ENCRYPTION_INTENT_v0_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F134 | `05_INACTIVE_CANDIDATE/NH_TOOLS_FOR_NH_CATEGORY_v0_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F135 | `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F136 | `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_3_CANDIDATE.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F137 | `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | C-7A.6 and cited sub-parts; C-7A.13 and cited sub-parts; C-7A.15 and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. Chapter 3-b: C-READ.7 (excluding the ACCEPTED C-READ.7.2 guard) and C-READ.8 (FR-0125–FR-0133); C-READ.1.12.1 (FR-0123); C-READ.9 (FR-0136). |
| F138 | `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH00.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | Naming/path continuity only; no Chapters 0–2 (carried placement) behavior sourced from this chapter. |

### V10 heading coverage

| Row | V10 heading | Placement / remaining scope |
|---|---|---|
| V10-H001 | ### This is `NH_MASTER-20_CORRECTED_v10.md`, a corrected candidate in the Master 20 lineage. It is NOT YET ADOPTED. `NH_MASTER-19_CORRECTED_v7_1.md` (SHA-256: `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf`) remains the authoritative immutable Master until Ness explicitly adopts the corrected Master 20. | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H002 | ### Historical provenance (Master 19 lineage): | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H003 | ## 0. THE PREMISE — NEVER DECIDE FACTS (NEVER CLOSE THE BOOK)  [DESIGNED — the floor under every rule] | Partial placement: C-7A and cited sub-parts; C-7B.9.3. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ interpretation remains revisable. |
| V10-H004 | ## 0A. THE TWO MACHINERIES — DUMB vs SMART (psychologics)  [DESIGNED — top-level frame] | Partial placement: C-7A and cited sub-parts; C-7B.1 and cited sub-parts; C-7B.2.5; C-7B.3.2; C-7B.3.3; C-7B.9 and cited sub-parts; C-7B.11 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ record-carriage boundary; no new interpretation by the writer. |
| V10-H005 | ## 0B. FULL-TRANSPARENCY AND LIVING-RECORD LAW  [DESIGNED — foundational operating rule] | C-7A.16 and cited sub-parts; C-7A.17 and cited sub-parts; C-7B and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. Chapter 3-b: C-READ.6 operation records and health-check operation recording.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim. |
| V10-H006 | ## 1. WHAT N.H IS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H007 | ## 1A. THE INPUT-AGNOSTIC PRINCIPLE — ONE ENGINE, MANY FRONT DOORS  [DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H008 | ## 2. HOW TO WORK WITH NESS | Chapter 1 placement retained. §2 wording is carried in the marked conflict at C-7B.8; no new C-2 behavior here. |
| V10-H009 | ### 2A. INTERACTION AND ARTIFACT DELIVERY — LOCKED | Chapter 1 placement retained. §2 wording is carried in the marked conflict at C-7B.8; no new C-2 behavior here. |
| V10-H010 | ## 3. THE EVOLUTION — OLD vs NEW (key points) | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H011 | ## 4. THE MACHINE | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H012 | ## 5. THE CODEBASE MAP | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ; C-READ.3; C-READ.4 built functions and paths. |
| V10-H013 | ## 6. WHAT'S BUILT & VERIFIED ON DISK  [BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ built reading boundary.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H014 | ## 6A. THE CODE RULES — `.cursorrules` v3.2 (DUAL-ARCHITECTURE, IN FORCE) | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ record and write constraints.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim. |
| V10-H015 | ### IDENTITY AND PERMANENT RULES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H016 | ### THE THREE-LAYER ARCHITECTURE | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H017 | ### SOVEREIGNTY BOUNDARIES BY LAYER | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.2; C-READ.3; C-READ.5. |
| V10-H018 | ### SCHEMA CONSTRAINTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1 and C-READ.2. |
| V10-H019 | ### PRODUCTION READINGS AUTHORIZATION | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.5 and its protections. |
| V10-H020 | ### PROTECTED FILES AND STORES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.4/C-READ.5 destination separation; edit workflow excluded. |
| V10-H021 | ### DRY-RUN PROTOCOL | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H022 | ### §12 INCOMING — CURRENT STATUS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H023 | ## 6B. THE ACCRETIVE STORE — SCHEMA + STATE  [BUILT & VERIFIED] | Partial placement: C-7A.8 and cited sub-parts; C-7B.2.8.4 and cited sub-parts; C-7B.10.1.3; C-7B.11 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ.1 twelve-field representation; C-READ.2; C-READ.3; C-READ.4.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim. |
| V10-H024 | ## 7. THE BIG DESIGN — UNIVERSAL FILTER + MEANING ENGINE  [engines A + B BUILT; §§7E–7P core-conceptually designed S17; §§7D and 7Q partially conceptually designed] | C-7A and C-7B detailed subsections follow. NOT PLACED: engine implementation behavior belongs to Group A. |
| V10-H025 | ### 7A — THE UNIVERSAL FILTER (operating rules): | C-7A and cited sub-parts; C-7B.3 and cited sub-parts; C-7B.11 and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. Chapter 3-b: C-READ reciprocal Universal Filter use; principles retained from Chapter 2. |
| V10-H026 | ### 7B — THE MEANING ENGINE (mechanism): | C-7B and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. |
| V10-H027 | ### 7C — THE FORCED BUILD ORDER (never re-fought): | EXCLUDED: forced build order under §1.3. NOT PLACED: engine implementations belong to Group A. |
| V10-H028 | ## 7D. THE LIVING STATE WEB — PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ grounded reading consumer relationship. |
| V10-H029 | ## 7E. CATALOG FRONT DOOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H030 | ### §7E-TSC DETAILED DESIGN  [ACCEPTED DESIGN WITH LATER CORRECTIONS — NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H031 | ## 7F. CONTEXT RETRIEVAL  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1.9 retrieval audit and genuine no-context audit; retrieval machinery remains with C-7F. |
| V10-H032 | ## 7G. MEANING ENGINE INTERIOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ acceptance/shape distinction and caller relationship; C-READ.3 new-root write handoff also cites the nested §7G-A subsection.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H033 | ### §7G CREATION-AWARE MODE  [SETTLED CONCEPT — NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H034 | ## 7H. REREAD LIFECYCLE  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ reread output relationship; detailed orchestration remains with C-7H. |
| V10-H035 | ## 7I. VIEW LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ history/current-view use; view machinery remains with C-7I. |
| V10-H036 | ## 7J. CONTRADICTION AND CLASH HANDLING  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ clash-consumer relationship; clash machinery remains with C-7J. |
| V10-H037 | ## 7K. STORY LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7A.8.3; C-7B.3.1; C-7B.3.3 and cited sub-parts; C-7B.3.4. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ.1.5/1.6 speaker/perspective and embedded-v1-telling boundaries; future telling identity remains for its accepted package.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H038 | ## 7L. PERSON-BOXES  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.4. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ Person-Box consumer relationship. |
| V10-H039 | ## 7M. COMPUTED VIEW  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ current-use consumer relationship. |
| V10-H040 | ## 7N. ACTION SURFACING  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H041 | ## 7O. ACTION-RESULT RETURN PATH  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H042 | ## 7P. PERMISSION AND AUTHORITY BOUNDARIES  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H043 | ## 7Q. PRIVACY, DELETION, AND SENSITIVE-DATA HANDLING  [PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H044 | ## 7R. ATTENTION AND RELEVANCE CONTROL  [CORE CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H045 | ### DECISION 1 — OUTPUT FORM | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H046 | ### DECISION 2 — PRODUCER SELECTION | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H047 | ### DECISION 3 — EVALUATION TIMING | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H048 | ### DECISION 4 — TWO-TIER CONFIGURATION CONTRACT | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H049 | ### DECISION 5 — NESS'S RELATIONSHIP | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H050 | ### DECISION 6 — VALIDATION OF MOUTH-PRODUCED DIMENSIONS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H051 | ### DECISION 7 — MINIMUM SHARED VOCABULARY | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H052 | ### DECISION 8 — LIVING STATE WEB BOUNDARY | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H053 | ### DECISION 9 — TIER 1 PURPOSE FIELD | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H054 | ### DECISION 10 — UNRESOLVED DIMENSION HANDLING ACROSS THE TIER BOUNDARY | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H055 | ### DECISION 11 — DISAGREEMENT RECORD SCHEMA | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H056 | ### DECISION 12 — RELEVANCE EVENT RECORD SCHEMA | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H057 | ### DECISION 13 — PATTERN OBSERVATION CONDITIONS FOR PER-JUDGMENT OVERRIDES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H058 | ### DECISION 14 — UNRECOGNIZED PURPOSE TYPE HANDLING | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H059 | ### WHAT REMAINS OPEN FOR ATTENTION AND RELEVANCE CONTROL | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H060 | ## 8. THE RESEARCH PIPELINE  [DESIGNED — Brave not wired] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H061 | ## 9. DESIGNED, NOT BUILT — THE REST  [DESIGNED or CONCEPTUALLY DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H062 | ### §9 RECOVERED ACCESS AND AUTHENTICATION MODEL  [RECOVERED ACCEPTED DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H063 | ### §9 RECOVERED VOICE INPUT/OUTPUT PIPELINE  [RECOVERED PARTIAL DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H064 | ### §9 FIVE PHONE-SIDE MODES  [RECOVERED NAMES ONLY — BEHAVIOR NOT DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H065 | ### §9 PERSONALITY-RELATED CONVERSATION REHEARSAL  [RECOVERED PARTIAL DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H066 | ## 9A. IMAGE INGEST — FIRST WORKED FRONT-DOOR EXAMPLE  [DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H067 | ## 10. ORIGINALITY (honest calibration) | Partial placement: C-7B.9.3. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H068 | ## 11. WHAT'S OPEN / NEXT (priority order) | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ foundation status and quarantine/production boundary; restored details use the decision record plus named archive, not the compressed V10 line. |
| V10-H069 | ## 11-SETTLED. (condensed) | EXCLUDED: condensed decision/session narrative under §1.3; repeated runtime rules are represented by their detailed owning sections. |
| V10-H070 | ## 12. SESSION 6 — THE DATA-RESCUE OPERATION  [recovery done; ingest FROZEN] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H071 | ## 13. THE LIVE LOOP  [DESIGNED — not built] | Partial placement: C-7B.9; C-7B.10.1 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H072 | ## 14. THE CHAT FRONT DOOR  [PARTIALLY SETTLED, PARTIALLY OPEN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H073 | ## 15. SESSION 10 — BOOT HYGIENE + SIGN-IN + .CURSORRULES  [housekeeping done] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H074 | ## 16. THE MODEL LAYER — THE BORROWED MOUTH + THE SEARCH MODEL  [DESIGNED + partly on disk] | Partial placement: C-7B.6. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H075 | ## 17. S16 CORRECTION LOG — WHAT THE S16 CORRECTION PASS CHANGED (historical) | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H076 | ## 18. S17 CONSOLIDATION AND CORRECTION LOG | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H077 | ## 19. INTERFACE, WORLD, AND INTERACTION SYSTEM  [IN-PROGRESS DESIGN, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H078 | ### 19A. SETTLED INTERFACE DECISIONS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H079 | ### 19B. PROVISIONAL CONCEPTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H080 | ### 19C. UNANSWERED QUESTIONS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H081 | ### 19D. PAUSED DESIGN POINTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H082 | ### 19E. OPEN DEPENDENCIES (cross-audit results) | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H083 | ### TRUEST SINGLE SENTENCE | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H084 | ## 20. S18 CONSOLIDATION AND CHANGE LOG  [HISTORICAL SESSION SNAPSHOT — June 24 2026] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H085 | ## 21. S19 CONSOLIDATION AND CHANGE LOG  [HISTORICAL SESSION SNAPSHOT — June 25 2026] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H086 | ## 22. WELLBEING AND BEHAVIORAL BASELINE SYSTEM  [DESIGNED — full spec restored S19, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H087 | ## 23. MOBILE APP — THREE-MODE COMPANION  [DESIGNED — full spec restored S19, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H088 | ## 24. CONNECTION CAPABILITY  [CONCEPTUALLY DESIGNED (S19), NOT BUILT] | Partial placement: C-7B.10.6.2.2; C-7B.10.6.2.3; C-7B.10.6.3.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H089 | ## 25. VOICE SECURITY AND IDENTITY SYSTEM  [ACCEPTED DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H090 | ### Build-Time Implementation Settings | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H091 | ### 25.1. BOP — Behavioral Observation Processing | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H092 | ### 25.2. Other-Speaker / Guest / Known-Person Architecture | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H093 | ### 25.3. SIA — Speaker Identity Assessment | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H094 | ### 25.4. SACL — Speaker Access-Control Layer | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H095 | ### 25.5. Wellbeing / Identity / Security Separation Rules | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H096 | ### 25.6. BAI — Biometric Authorization Interface | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H097 | ### One-Time Authorization Token | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H098 | ### Top-Security Biometric Lease | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H099 | ### 25.7. Initial Owner-Phone Pairing | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H100 | ### 25.8. Recovery-Code Lifecycle | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H101 | ### 25.9. Future-Phone Replacement Flow | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H102 | ### 25.10. Atomic Emergency Recovery Flow | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H103 | ### 25.11. Initial Ness Voice-Profile Enrollment Bootstrap | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H104 | ### 25.12. Formally Adopted Vocabulary Additions | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H105 | ### 25.13. BGMM — Biometric-Gated Maintenance Mode | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H106 | ## 26. PERSONAL LEARNING AND ADAPTATION SYSTEM  [ACCEPTED DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H107 | ## 27. HISTORICAL RECOVERY AND CORRECTION LOG — JUNE 25 2026 | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |

### Additional READ-folder files at this source pin

| File | Placement |
|---|---|
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md` | NOT PLACED: outside this evaluation-evidence piece; no content borrowed. |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH01.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH02.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-a.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-b.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-c.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-d.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |

### Detailed source landing map

| Bridge section | Cards in this piece |
|---|---|
| §7.13 | C-GOLD.1.7, C-GOLD.1.7.1, C-GOLD.1.7.1.1, C-GOLD.1.7.1.2, C-GOLD.1.7.1.3, C-GOLD.1.7.1.4, C-GOLD.1.7.1.5, C-GOLD.1.7.1.6, C-GOLD.1.7.1.7, C-GOLD.1.7.1.8, C-GOLD.1.7.1.8.1, C-GOLD.1.7.1.8.2, C-GOLD.1.7.1.9, C-GOLD.1.7.1.10, C-GOLD.1.7.1.11, C-GOLD.1.7.1.12, C-GOLD.1.7.1.13, C-GOLD.1.7.1.14, C-GOLD.1.7.1.15, C-GOLD.1.7.1.16, C-GOLD.1.7.2, C-GOLD.1.7.3, C-GOLD.1.7.3.1, C-GOLD.1.7.3.2, C-GOLD.1.7.3.3, C-GOLD.1.7.3.4, C-GOLD.1.7.3.4.1, C-GOLD.1.7.3.4.2, C-GOLD.1.7.3.4.3, C-GOLD.1.7.4, C-GOLD.1.7.4.1, C-GOLD.1.7.4.2, C-GOLD.1.7.4.3, C-GOLD.1.7.4.4, C-GOLD.1.7.4.4.1, C-GOLD.1.7.4.4.1.1, C-GOLD.1.7.4.4.1.2, C-GOLD.1.7.4.5, C-GOLD.1.7.4.6, C-GOLD.1.7.4.7, C-GOLD.1.7.4.7.1, C-GOLD.1.7.4.7.2, C-GOLD.1.7.4.7.3, C-GOLD.1.7.4.7.4, C-GOLD.1.7.4.7.5, C-GOLD.1.7.4.7.6, C-GOLD.1.7.4.7.7, C-GOLD.1.7.5, C-GOLD.1.7.5.1, C-GOLD.1.7.5.2, C-GOLD.1.7.5.3, C-GOLD.1.7.5.4, C-GOLD.1.7.5.5, C-GOLD.1.7.5.6, C-GOLD.1.7.6, C-GOLD.1.7.6.1, C-GOLD.1.7.6.2, C-GOLD.1.7.6.3, C-GOLD.1.7.6.4, C-GOLD.1.7.7, C-GOLD.1.7.8, C-GOLD.1.7.9, C-GOLD.1.7.9.6, C-GOLD.1.7.9.7, C-GOLD.1.7.9.8, C-GOLD.1.7.9.9, C-GOLD.1.7.9.10, C-GOLD.1.7.9.11, C-GOLD.1.7.9.12, C-GOLD.1.7.9.13, C-GOLD.1.7.9.14, C-GOLD.1.7.9.15, C-GOLD.1.7.9.16, C-GOLD.1.7.10, C-GOLD.1.7.10.3, C-GOLD.1.7.10.4, C-GOLD.1.7.10.5 |
| §13.1 | C-GOLD.1.7, C-GOLD.1.7.7, C-GOLD.1.7.7.10, C-GOLD.1.7.9, C-GOLD.1.7.9.1, C-GOLD.1.7.9.2, C-GOLD.1.7.9.3, C-GOLD.1.7.9.4, C-GOLD.1.7.9.5, C-GOLD.1.7.9.6, C-GOLD.1.7.9.7, C-GOLD.1.7.9.8, C-GOLD.1.7.9.9, C-GOLD.1.7.9.10, C-GOLD.1.7.9.11, C-GOLD.1.7.9.12, C-GOLD.1.7.9.13, C-GOLD.1.7.9.14, C-GOLD.1.7.9.15, C-GOLD.1.7.9.16 |
| §13.5 | C-GOLD.1.7, C-GOLD.1.7.7, C-GOLD.1.7.7.1, C-GOLD.1.7.7.2, C-GOLD.1.7.7.3, C-GOLD.1.7.7.4, C-GOLD.1.7.7.5, C-GOLD.1.7.7.6, C-GOLD.1.7.7.7, C-GOLD.1.7.7.8, C-GOLD.1.7.7.9, C-GOLD.1.7.7.10, C-GOLD.1.7.8, C-GOLD.1.7.8.1, C-GOLD.1.7.8.2, C-GOLD.1.7.9, C-GOLD.1.7.9.16, C-GOLD.1.7.10, C-GOLD.1.7.10.3, C-GOLD.1.7.10.4 |
| §10 | C-GOLD.1.7, C-GOLD.1.7.10, C-GOLD.1.7.10.1, C-GOLD.1.7.10.2, C-GOLD.1.7.10.3, C-GOLD.1.7.10.4, C-GOLD.1.7.10.5 |
| §5 | C-GOLD.1.7.1, C-GOLD.1.7.1.16, C-GOLD.1.7.7 |
| §13.4 | C-GOLD.1.7.1, C-GOLD.1.7.7 |
| §7.12 | C-GOLD.1.7.1.2, C-GOLD.1.7.1.3, C-GOLD.1.7.1.4, C-GOLD.1.7.1.8, C-GOLD.1.7.1.8.1, C-GOLD.1.7.1.8.2, C-GOLD.1.7.2, C-GOLD.1.7.4.7, C-GOLD.1.7.4.7.1, C-GOLD.1.7.4.7.2, C-GOLD.1.7.4.7.3, C-GOLD.1.7.4.7.4, C-GOLD.1.7.4.7.5, C-GOLD.1.7.4.7.6, C-GOLD.1.7.4.7.7, C-GOLD.1.7.6, C-GOLD.1.7.9.5, C-GOLD.1.7.9.6, C-GOLD.1.7.9.7, C-GOLD.1.7.9.8, C-GOLD.1.7.9.9, C-GOLD.1.7.9.10, C-GOLD.1.7.9.13, C-GOLD.1.7.9.14 |
| §7.11 | C-GOLD.1.7.6, C-GOLD.1.7.9, C-GOLD.1.7.9.1, C-GOLD.1.7.9.2, C-GOLD.1.7.9.3, C-GOLD.1.7.9.4, C-GOLD.1.7.9.5, C-GOLD.1.7.10.1, C-GOLD.1.7.10.2 |
| §7.2 | C-GOLD.1.7.7.1, C-GOLD.1.7.7.4 |
| §7.9 | C-GOLD.1.7.9.1, C-GOLD.1.7.9.2 |




## READ RECORD

The source files below match their Git blobs at `6a7160ba688ba4e433a31899162815df7e2bab17`. The full A1 content file and its design-closure receipt were read. The other covered source sections are listed in the source map. The original PDF, companion transcript and runtime legacy gold files are not repository source files opened for this piece; their recorded properties and quoted material are supplied only by the pinned sources identified below. Contract §§5–11 were reopened before writing; §11.3 is reopened after writing for the checks below. The lessons sheet and run instructions were read in full.

| Source file | SHA-256 |
|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `01_AUTHORITATIVE/cursorrules` | `5050d08825b93acd72a79d07946e43c8cbe537e079517ccfe66bcae8e30e96e9` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` |
| `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` | `04dd5abc42e59afb61b4d280a0bb69d647d187fd0da385bc5c567eddbca81a41` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_GOLD_CASES_MISSING_SOURCE_BLOCKER_RECORD_v1_0.md` | `8de0e340b6781f0d5bb31032d190bbd2eeedf58e9a4e98868c3d99a5d165716a` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md` | `40ed4f5ec457f03bb5bcb233e9ec0f05c36947fc2f8307c38e1ef826e4fb682d` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md` | `6b5c6bcfd8ea7ddf73c85c60725146638345f8261da79c3c6b214b999a939709` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | `a495871fba20ca03c19c024e77d1561cc90877ffa290c2ee19966c7026a21b2d` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md` | `5ab67191ff57e532e88193008fe0ec5652f72cc6608316f48b99555e54639850` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | `298de053269f4a9e93e97dfd994d33b0b879d71af636b169769264e7183d9d4c` |

Instruction fingerprints:
- `NH_MASTER-21_SYSTEM_BEHAVIOR_BUILD_CONTRACT_FOR_CHATGPT_v1_0.md` — SHA-256 `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1`.
- `NH_MASTER-21_WRITER_LESSONS_FROM_AUDITS_v0_1.md` — SHA-256 `635be95b861c181efb3b7bc1b2a8405ab706f864068a0b88f31fb91971adf3e6`.
- `NH_MASTER-21_WRITER_RUN_INSTRUCTIONS_v0_2.md` — SHA-256 `93431167c0fb03fe1216ebbc12655ac640d71bcb7a59659cd123f51e72a54611`.

### Earlier chapter identities preserved

| Piece | SHA-256 |
|---|---|
| CH00 | `d01e8ec370be9c8e50fbb293c863c95ddaf6f82af5700877bf1a57276a1f4998` |
| CH01 | `f86342e90f8789a5b825fbe73f4bc42041c6537498a32a01980287ad32d47544` |
| CH02 | `22168ca6a6a54a2d142dcc7e1d068ca1ab7270b28a90e8e10c2a0106b595d19a` |
| CH03-a | `3b0ba1cb3ea3415ef71c5343702fd2c7ddcd44675aa8f0b4bf5e7aeab2aa80db` |
| CH03-b | `ba62fb68b050b3840afeabec299b2aa0baac17ba2f79869c1fc031dbc195d8b5` |
| CH03-c | `20d022f2d237cf0a29e4128eae510e0cf153505a2ffd0c64ff512fed9cb06fa6` |
| CH03-d | `9444e60b0b4cb09c1efd5d03c06579af4864f7437a10555fdeca54e50687195c` |
| CH03-e | `a33e27d89548e57f16e8c17b489ca971f3f992101e7664a0260954494f572aa2` |
| CH03-f | `567d566a000971890c22771cbaa9e6fee2669383f02975206013d440e4fb2347` |
| CH03-g | `59f8d76f64e95da500e86644e79a2a9e9cdec6dedd384b0cb5d1536ee1ca2e7f` |
| CH03-h | `af59933e649a92dc1b58dd679fbffad86fa999c2b6ffc36259eda227fea3f582` |
| CH03-i | `bb128e4e4ef9fba5889ee54b90268962d02162e51cb1ff9e5eb6a7e089e3c47f` |
| CH03-j | `0b2bb5079af523e3f101705704316b1092f4a536575eff11ff020bd1eaa13a20` |
| CH03-k | `51c6e87ed42d6bd341dc58a24ef11fb6baaf58bb2e93f7d4a435622382fd1ce3` |

### READ-folder files not yet read whole

The pending list contains 93 files after the whole-read updates recorded for this piece. Scoped rereads do not remove a pending entry; the ledger retains its Stage-2-only exception.

- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/02-NH_BUNDLE_6_A3_DECISIONS_WORKING_RECORD_v1-1-.md`
- `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWERS.md`
- `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWER_PROVENANCE.json`
- `05_ACTIVE_CANDIDATE/Music_Media_Intent_Excerpts.md`
- `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_0.md`
- `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_1.md`
- `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_2.md`
- `05_ACTIVE_CANDIDATE/NH_A19_REMAINING_HUMAN_EXPERIENCE_DESIGN_PLAN_v1_0.md`
- `05_ACTIVE_CANDIDATE/NH_A2_CURRENT_STATUS_v1_1.md`
- `05_ACTIVE_CANDIDATE/NH_B24_REJECTION_CATEGORY_DECISION_2026-09-23_v0_1_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_0.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_2.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md`
- `05_ACTIVE_CANDIDATE/NH_DESIGN_ANSWERS.md`
- `05_ACTIVE_CANDIDATE/NH_PERSONAL_IDEA_NOTE_A19_VR_WORLD_ROOMS_OFFLINE_CREATION_v1.md`
- `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/Other_Future_Feature_Intent_Excerpts.md`
- `05_ACTIVE_CANDIDATE/Thought_Branches_and_Simulation_Intent.md`
- `05_INACTIVE_CANDIDATE/NH_FUTURE_MUSIC_UNDERSTANDING_AND_MUSIC_SERVICE_CONNECTIONS_PACKAGE_INTAKE_v1_0_CANDIDATE.md`
- `05_INACTIVE_CANDIDATE/NH_PROVENANCE_FIRST_MULTI_INDEX_MEMORY_FABRIC_MECHANICAL_DESIGN_v1_4_CANDIDATE.md`
- `05_INACTIVE_CANDIDATE/NH_SECURITY_STORAGE_ENCRYPTION_INTENT_v0_1.md`
- `05_INACTIVE_CANDIDATE/NH_TOOLS_FOR_NH_CATEGORY_v0_1.md`
- `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_1.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md`

## CONTRACT CHECK

CONTRACT CHECK (against the cloned contract, SHA-256 e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1)
§1.3 no history/actions/roles/workflow in this chapter: PASS — all 69 behavior cards reviewed; delivery and source-status records remain outside behavior boxes.
§1.4 every gap written as NOT DECIDED: PASS — 151 empty fields/cells and exactly matching register entries.
§1.5 conflicts marked, none resolved: PASS — 0 new conflicts; earlier conflict records unchanged.
§3 exactly one stamp per line: PASS — 69 headers, 536 populated fields and 139 USED BY rows checked; empty boxes use only NOT DECIDED.
§4 every behavior line cited in the exact format: PASS — 47 distinct citations resolve in pinned sections; all populated fields and USED BY rows cited; support reviewed manually.
§5.4 one name per thing: PASS — 69 non-colliding IDs, official names and established sub-part names checked.
§6 all template fields present, in order, for every part: PASS — 69 templates and 683 field lines checked.
§6.3 reciprocity within this chapter: PASS — 131 internal links reciprocated; 10 outward links and 5 documented incoming uses covered by 15 rows naming both ends.
§6.4 every decided detail written in, no citation used in place of content: PASS — Both legacy file/marker identities, sizes/counts, seven B-case references and recorded outcomes, all six scoring rules, three build-order constraints and four judgment metadata fields are present. All eight A1 targets and full frozen contexts match the accepted source byte for byte. Sixteen separate proposed tellings retain every case-specific perspective, evidence value, firmness label/basis, semantic alternative, theme and failure boundary. Common perspective/evidence/firmness field definitions reuse the existing atomic C-READ cards; no runtime schema, root ID, benchmark execution mechanic, score or threshold is invented. Full bridge derivation/applicability is assigned to CH03-m/n; the deferred insufficient-context revisit trigger goes to CH05-d.
§6.5 sub-parts recursed to the bottom: PASS — 69 cards; source-map scope and reuse of established atomic cards manually reviewed.
§9 coverage matrix rows added for every file used: PASS — 11 pinned source identities and corresponding coverage entries checked; current placement/deferral table included.
§10.11 no recommendation, no sentence addressed to Ness: PASS — all behavior boxes reviewed; source-defined approval conditions are descriptions of the system boundary.
Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`. The lessons sheet and run instructions were read in full; contract §§5–11 were reopened before writing and §11.3 afterward. Other source reads are the scoped sections in the source map, without a new whole-file claim.

Computed self-check output:

| Check | Count |
|---|---|
| cards | 69 |
| field_lines | 683 |
| populated_fields | 536 |
| not_decided_fields_and_cells | 151 |
| used_by_rows | 139 |
| relationships | 141 |
| internal_relationships | 131 |
| external_relationships | 10 |
| continuation_rows | 15 |
| plain_gates | 3 |
| step_cards | 8 |
| source_names_checked | 43 |
| unique_citations | 47 |
| source_identities | 11 |
| earlier_identities | 14 |
| pending_source_paths | 93 |
| built_field_lines | 21 |
| misfiled_scan_fields | 683 |
| empty_restriction_failure_gate_boxes_reviewed | 37 |
| formula_hits | 0 |
| wording_hits | 0 |
| errors | 0 at writing; audit 1B later confirmed errors, corrected in round 4B |
| verbatim_input_blocks | 16 |
| verbatim_wording_hits_preserved | 2 |

Manual review accompanying the mechanical scan:

- Reviewed all boxes against the scoped sources and accepted status receipts. BUILT is restricted to the legacy artifacts, marker existence and documented A/B gold runs/results. Seal immutability, scoring, logging, engine failure behavior and future-build conditions are DESIGNED; marker existence is not claimed to prove automatic enforcement. A1 content and bridge wiring remain ACCEPTED design, with no runtime completion inferred.
- Reviewed every field and USED BY row, including every empty restriction/failure/gate box. Filled the source-explicit no-adoption outcome for unlogged operations, the unpinned-runtime block, the story-test pinning gate, and the contextual draft placement condition. Remaining blank failure fields lack a stated failure mechanism; fixed data and rule definitions do not acquire invented execution gates. The marker input interface and contextual draft input/output interfaces are unspecified.
- Both legacy file/marker identities, sizes/counts, seven B-case references and recorded outcomes, all six scoring rules, three build-order constraints and four judgment metadata fields are present. All eight A1 targets and full frozen contexts match the accepted source byte for byte. Sixteen separate proposed tellings retain every case-specific perspective, evidence value, firmness label/basis, semantic alternative, theme and failure boundary. Common perspective/evidence/firmness field definitions reuse the existing atomic C-READ cards; no runtime schema, root ID, benchmark execution mechanic, score or threshold is invented. Full bridge derivation/applicability is assigned to CH03-m/n; the deferred insufficient-context revisit trigger goes to CH05-d.
- Scanned the whole file. Two punctuation hits occur only in byte-identical frozen target data: the R03 ellipsis and R08 repeated periods. They are preserved and counted separately, not silently normalized. No formula sentences or unreviewed generated box text remain. Sixteen frozen input blocks contain source quotations; they are benchmark data, not a Master-21 recommendation, medical assertion or address to Ness. All behavioral prohibitions are written directly.
- Checked exact names, all preserved chapter fingerprints, source pin, source identity hashes, section anchors, reciprocal rows and the complete source-input comparison. C-GOLD names the existing C-GOLD.1 in Fed by and SUB-PARTS. Continuations cover the existing CH03-e–h bridge pair and CH03-i/j suppliers/gates. No new C-GOLD.1 or colliding sub-ID is created. Runtime paths are documented names, not claims of a live filesystem inspection; accepted A1 design closure is distinguished from runtime sealing and pinning.

All named source paths were checked at the fixed pin. Runtime/store names are checked against source documentation; this is not a live N.H filesystem check. P-MAIN has no direct C-GOLD step. Gold evaluation belongs to CY-G; the bridge's existing CY-G use is retained. Full side-path assembly remains CH11. The wording scan covers the whole file. The count table is compared with a final recount after this block is appended.
