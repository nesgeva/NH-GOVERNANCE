# Chapter 6-a — Group D: C-7J

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH06-a.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`  

This piece describes Clash Handling, its six types, record contents, detection and duplicate matching, separate response events, downstream effects, and clash/named-gap presentation. Telling identity and eligibility retain their existing C-READ cards; the worker's claim, checkpoint, sentinel and restart records retain their existing C-7GA cards. Complete Story Layer, Person-Boxes, Computed View, View Layer and Living State Web mechanisms belong to CH06-b through CH06-f; action support to CH07-a; privacy, relevance, LMAC and reading affirmation internals to CH08-a, CH08-b, CH08-c and CH08-f; connected side paths to CH11.

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; NHD identifiers locate decisions in the pinned decision index and do not replace their behavior sources.

<!-- BEGIN BEHAVIOR -->

### C-7J — Clash Handling (§7J)
Stamp: DESIGNED    Source: [V10 §7J] [MAP C-7J]

ALONE
- What it is: DESIGNED — The component that detects and preserves contradictions and other differences between readings without deciding which interpretation is correct. [V10 §7J] [MAP C-7J]
- Takes in: DESIGNED — New readings, their exact root references and related readings; wider scans also examine roots, threads, people, periods and story layers. Ness's responses enter as separate events. [V10 §7J] [MAP C-7J]
- Does: DESIGNED — Records the six-type distinction, preserves each original clash and links subsequent detections and responses to it. Compares simultaneous truth under the same conditions, person, time and context without resolving the material. [V10 §7J] [MAP C-7J]
- Gives out: DESIGNED — Clash records pointing to exact sources, detection histories and separate Ness-response events. Detection mode and detection confidence do not grant authority. [V10 §7J] [MAP C-7J]
- Must never: DESIGNED — Resolve, rank or select a winner; mutate original roots or readings; create independent duplicate records for the same clash; treat every clash as an error. [V10 §7J] [MAP C-7J]
- Fails closed by: DESIGNED — On a system failure in the post-reading detection stage, stops; the queue job stays `in_progress` and resumes from that stage after restart. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — Withholds material from an unauthorized purpose; visible-output exclusion alone does not prohibit an otherwise authorized internal comparison. [V10 §7Q / TWO-STAGE OUTPUT ACCESS CONTROL]
- Fails closed by: ACCEPTED — Blocks telling-level semantic use until the complete valid telling-set and checkpoint, or legitimate zero-telling sentinel, exists. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1]

TOGETHER
- Fed by: BUILT — C-READ — Reading record, validator, writer (§6B): readings and their root references for comparison in CY-A. [V10 §6B] [V10 §7J]
- Fed by: DESIGNED — C-7GA.11.7 — Step 7 — Clash detection: the new reading and its operation key after the reading is durable. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fed by: ACCEPTED — C-READ.10.14 — Telling-reference handoff: eligible stable `telling_id` references with the parent-reading and supporting-root chain when the comparison is telling-level. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [NHD-A2]
- Fed by: DESIGNED — C-7J.1 — Six clash types: the six-type distinction; C-7J.2 — Genuine contradiction versus contextual difference: the simultaneous-truth test; C-7J.4 — Two detection modes, same record type: the detection result with its mode; C-7J.6 — Ness response as separate event: separate responses; C-7J.9 — Clash operational recordkeeping: the connected operation record. [V10 §7J] [V10 §0B]
- Fed by: ACCEPTED — C-7J.3 — Clash record: the original clash record; C-7J.5 — Clash identity and one commit path: identity matching and one commit path; C-7J.7 — Downstream effects of clashes: downstream conflict qualifications; C-7J.8 — Clash and named-gap presentation: the marker and detail presentation; C-7J.9.1 — Telling-link and semantic-gate operation records: telling-link and gate-operation provenance. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §10]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): exact-purpose internal-use authorization, including influence-removal, protected-boundary and TSC restrictions, before detection. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-LMAC — Live Mechanism Access Coordinator (§26): obtains the current internal-use authorization through the shared mechanism before the detection input is used. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: ACCEPTED — C-READ.10.10 — Telling-set semantic eligibility: telling-specific semantic use waits for the complete valid telling set and checkpoint, or legitimate zero-telling sentinel; embedded, partial or integrity-failed substitutes are prohibited. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1] [NHD-A2]
- Changes: DESIGNED — C-7D — Living State Web (§7D): supplies clash records as permitted source-evidence while preserving their grounding and uncertainty. [V10 §7D] [MAP C-7J]
- Changes: DESIGNED — C-7M — Computed View (§7M): provides clashes and separate responses for current-use assembly and presentation without altering their originals. [V10 §7M] [V10 §7J]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.11.7 — Step 7 — Clash detection, CY-A | New reading, authorized related readings and `{job_id}::{reading_id}::clash_detection`. | Recovers an existing operation result or detects, same-clash-matches and records a clash/history or a negative sentinel. | Durable detection result; no duplicated clash and no change to the input readings. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 2 · DESIGNED | C-7GA.11.7 — Step 7 — Clash detection, P-MAIN step 14 | New reading, authorized related readings and `{job_id}::{reading_id}::clash_detection`. | Recovers an existing operation result or detects, same-clash-matches and records a clash/history or a negative sentinel. | Durable detection result; no duplicated clash and no change to the input readings. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 3 · DESIGNED | C-7D — Living State Web (§7D) | Permitted clash records and their source references. | Keeps the clash available as state source-evidence without converting it into a truth verdict. | Grounded state derivation; clash and source histories remain preserved. | [V10 §7D] [MAP C-7J] |
| 4 · DESIGNED | C-7M — Computed View (§7M) | Clash records, contrary evidence and separate Ness responses. | Surfaces clashes beside their items and allows responses to affect presentation/current use. | Current picture only; original roots, readings and clashes remain unchanged. | [V10 §7M] [V10 §7J] |
| 5 · DESIGNED | C-LMAC — Live Mechanism Access Coordinator (§26) | An authorized clash-read request. | Returns the clash records and Ness-response events with their own current result and provenance. | The requesting function receives the permitted live component result. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 6 · DESIGNED | C-7J.1 — Six clash types | Compared readings and circumstances. | Supplies the material for six-type classification. | The kind of difference is preserved. | [V10 §7J / SIX CLASH TYPES] |
| 7 · DESIGNED | C-7J.2 — Genuine contradiction versus contextual difference | Two statements with their conditions. | Keeps person, time and context explicit for the simultaneous-truth test. | The distinction is recorded without resolution. | [V10 §7J / GENUINE CONTRADICTION VS CONTEXTUAL DIFFERENCE] |
| 8 · ACCEPTED | C-7J.3 — Clash record | A detection with its exact source pointers. | Carries the conflict and provenance into the common record. | One preserved original clash. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [NHD-BU3] |
| 9 · DESIGNED | C-7J.4 — Two detection modes, same record type | A new reading or wider scan request. | Makes the common clash route available to either detection mode. | Same record type, with mode provenance. | [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE] |
| 10 · ACCEPTED | C-7J.5 — Clash identity and one commit path | The conflicting-item set and particular aspect. | Preserves the detection identity for existing-clash matching. | One original per identity. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |
| 11 · DESIGNED | C-7J.6 — Ness response as separate event | Ness's response to an identified clash. | Keeps the response separate from the clash. | Accreting response history. | [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT] |
| 12 · ACCEPTED | C-7J.7 — Downstream effects of clashes | Clash-involved material for downstream use. | Supplies the clash and its linked history beside the item. | Conflict-aware use and presentation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [NHD-BU3] |
| 13 · ACCEPTED | C-7J.8 — Clash and named-gap presentation | Clash records, pointers and linked history. | Makes the settled details available for authorized presentation. | An inspectable clash, never a resolved record. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |
| 14 · DESIGNED | C-7J.9 — Clash operational recordkeeping | A real clash operation and its outcome. | Keeps the operation connected to permanent living memory. | One log per operation without extra truth weight. | [V10 §0B] [MAP C-7J] |
| 15 · ACCEPTED | C-7J.9.1 — Telling-link and semantic-gate operation records | A telling-level link or blocked/resumed use. | Preserves the operation and structural provenance. | No payload leak or duplicate semantic evidence. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.3] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §10] [NHD-A2] |
| 16 · DESIGNED | C-7M.4.3.2 — Computed View active-clash event trigger | The clash event and its preserved source references. | Supplies the new or changed active-clash information. | Nothing in this card. | [V10 §7M / UPDATE TIMING] |
| 17 · DESIGNED | C-7R.7.2.9 — active_clash_links | The linked recorded conflicts. | Supplies existing clash records. | Nothing in this card. | [V10 §7R] |
| 18 · ACCEPTED | C-7D.3.1 — Position tension links | Evidence for an actual tension. | Supplies governed clash handling where a clash exists. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §4B] |
| 19 · DESIGNED | C-OOP.5.3 — Outcome direct contradiction enters clash handling | The actual contradictory readings. | Takes this place's change: handles the direct contradiction under its established rules. | Handles the direct contradiction under its established rules. | [V10 §26.6] |
| 20 · ACCEPTED | C-LMAC.3.6 — Clash query contract | An authorized clash-read request. | Supplies clash records and Ness responses. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 21 · ACCEPTED | C-7N.13.6.9 — Action-surfacing active_clash_links dimension | Actual active clash references in the support. | Supplies preserved clash records and status. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] |
| 22 · ACCEPTED | C-7M.5.5.4 — Computed View clash references | Preserved clash record IDs and their source links. | Supplies preserved clash records. | Nothing in this card. | [V10 §7J] [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] |
| 23 · ACCEPTED | C-7D.9.13 — B6 clashes and contrary-evidence links | Actual contrary evidence and clash identities. | Supplies actual clash records. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] |

SUB-PARTS: C-7J.1 — Six clash types; C-7J.2 — Genuine contradiction versus contextual difference; C-7J.3 — Clash record; C-7J.4 — Two detection modes, same record type; C-7J.5 — Clash identity and one commit path; C-7J.6 — Ness response as separate event; C-7J.7 — Downstream effects of clashes; C-7J.8 — Clash and named-gap presentation; C-7J.9 — Clash operational recordkeeping

### C-7J.1 — Six clash types
Stamp: DESIGNED    Source: [V10 §7J / SIX CLASH TYPES]

ALONE
- What it is: DESIGNED — The six named kinds of disagreement or apparent disagreement. [V10 §7J / SIX CLASH TYPES]
- Takes in: DESIGNED — Compared readings, their evidence, times, perspectives, modes and retrieval configurations. [V10 §7J / SIX CLASH TYPES]
- Does: DESIGNED — Distinguishes direct contradiction, interpretive divergence, temporal change, perspectival difference, evidence insufficiency and context mismatch. [V10 §7J / SIX CLASH TYPES]
- Gives out: DESIGNED — A clash-type distinction that preserves why the material differs. [V10 §7J / SIX CLASH TYPES]
- Must never: DESIGNED — Collapse temporal or contextual difference into an automatic error verdict. [V10 §7J]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J — Clash Handling (§7J): the readings and comparison circumstances being classified. [V10 §7J / SIX CLASH TYPES]
- Fed by: DESIGNED — C-7J.1.1 — Direct contradiction: exclusive same-root meanings; C-7J.1.2 — Interpretive divergence: non-exclusive conclusions; C-7J.1.3 — Temporal change: different-time change; C-7J.1.4 — Perspectival difference: different framings; C-7J.1.5 — Evidence insufficiency: insufficient context; C-7J.1.6 — Context mismatch: differing modes or configurations. [V10 §7J / SIX CLASH TYPES]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J — Clash Handling (§7J) | The compared material and its circumstances. | Retains the applicable kind of difference without deciding a winner. | Recorded classification only. | [V10 §7J / SIX CLASH TYPES] |
| 2 · DESIGNED | C-7J.1.1 — Direct contradiction | Two readings of one root. | Keeps mutually exclusive meanings identifiable. | Direct contradiction remains distinguishable. | [V10 §7J / SIX CLASH TYPES] |
| 3 · DESIGNED | C-7J.1.2 — Interpretive divergence | Different conclusions from shared evidence. | Keeps the non-exclusive difference explicit. | Divergence remains distinct from exclusion. | [V10 §7J / SIX CLASH TYPES] |
| 4 · DESIGNED | C-7J.1.3 — Temporal change | Readings at different times. | Preserves the temporal context. | Possible change is not collapsed into error. | [V10 §7J / SIX CLASH TYPES] |
| 5 · DESIGNED | C-7J.1.4 — Perspectival difference | Different framings of one event. | Preserves each framing with its perspective. | The perspective difference stays visible. | [V10 §7J / SIX CLASH TYPES] |
| 6 · DESIGNED | C-7J.1.5 — Evidence insufficiency | Readings with insufficient context. | Keeps the context limitation explicit. | The conflict remains evidence-qualified. | [V10 §7J / SIX CLASH TYPES] |
| 7 · DESIGNED | C-7J.1.6 — Context mismatch | Readings from different modes or retrieval configurations. | Preserves those production circumstances. | Apparent conflict can remain context mismatch. | [V10 §7J / SIX CLASH TYPES] |

SUB-PARTS: C-7J.1.1 — Direct contradiction; C-7J.1.2 — Interpretive divergence; C-7J.1.3 — Temporal change; C-7J.1.4 — Perspectival difference; C-7J.1.5 — Evidence insufficiency; C-7J.1.6 — Context mismatch

### C-7J.1.1 — Direct contradiction
Stamp: DESIGNED    Source: [V10 §7J / SIX CLASH TYPES]

ALONE
- What it is: DESIGNED — Two readings of the same root with mutually exclusive meanings. [V10 §7J / SIX CLASH TYPES]
- Takes in: DESIGNED — The two readings and the common root. [V10 §7J / SIX CLASH TYPES]
- Does: DESIGNED — Identifies that their meanings exclude one another. [V10 §7J / SIX CLASH TYPES]
- Gives out: DESIGNED — The direct-contradiction type. [V10 §7J / SIX CLASH TYPES]
- Must never: DESIGNED — Choose a winning reading or rewrite the common root. [V10 §7J]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J.1 — Six clash types: the same-root comparison. [V10 §7J / SIX CLASH TYPES]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J.1 — Six clash types | Same-root readings with exclusive meanings. | Distinguishes direct contradiction from the other five types. | The type carried by the clash. | [V10 §7J / SIX CLASH TYPES] |

SUB-PARTS: NONE

### C-7J.1.2 — Interpretive divergence
Stamp: DESIGNED    Source: [V10 §7J / SIX CLASH TYPES]

ALONE
- What it is: DESIGNED — Different conclusions from the same evidence where neither strictly excludes the other. [V10 §7J / SIX CLASH TYPES]
- Takes in: DESIGNED — The common evidence and the different conclusions. [V10 §7J / SIX CLASH TYPES]
- Does: DESIGNED — Retains the difference without treating the conclusions as mutually exclusive. [V10 §7J / SIX CLASH TYPES]
- Gives out: DESIGNED — The interpretive-divergence type. [V10 §7J / SIX CLASH TYPES]
- Must never: DESIGNED — Turn a non-exclusive difference into a selected authoritative reading. [V10 §7J]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J.1 — Six clash types: the same-evidence comparison. [V10 §7J / SIX CLASH TYPES]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J.1 — Six clash types | Non-exclusive conclusions from shared evidence. | Records their interpretive divergence. | The kind of difference shown. | [V10 §7J / SIX CLASH TYPES] |

SUB-PARTS: NONE

### C-7J.1.3 — Temporal change
Stamp: DESIGNED    Source: [V10 §7J / SIX CLASH TYPES]

ALONE
- What it is: DESIGNED — Inconsistency between readings at different times that may reflect genuine change. [V10 §7J / SIX CLASH TYPES]
- Takes in: DESIGNED — Readings with their different time contexts. [V10 §7J / SIX CLASH TYPES]
- Does: DESIGNED — Preserves the possibility of change over time rather than declaring error. [V10 §7J / SIX CLASH TYPES]
- Gives out: DESIGNED — The temporal-change type. [V10 §7J / SIX CLASH TYPES]
- Must never: DESIGNED — Treat different-time inconsistency as proof that one reading is wrong. [V10 §7J]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J.1 — Six clash types: the time-qualified comparison. [V10 §7J / SIX CLASH TYPES]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J.1 — Six clash types | Inconsistent readings from different times. | Keeps genuine change distinguishable from error. | The temporal classification. | [V10 §7J / SIX CLASH TYPES] |

SUB-PARTS: NONE

### C-7J.1.4 — Perspectival difference
Stamp: DESIGNED    Source: [V10 §7J / SIX CLASH TYPES]

ALONE
- What it is: DESIGNED — Different speakers' or observers' framings of the same event, each accurate within its own perspective. [V10 §7J / SIX CLASH TYPES]
- Takes in: DESIGNED — The framings and the speakers or observers whose perspectives they express. [V10 §7J / SIX CLASH TYPES]
- Does: DESIGNED — Retains the perspective-specific difference. [V10 §7J / SIX CLASH TYPES]
- Gives out: DESIGNED — The perspectival-difference type. [V10 §7J / SIX CLASH TYPES]
- Must never: DESIGNED — Silently replace one perspective with another or select the correct teller. [V10 §7J]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J.1 — Six clash types: the perspective-qualified comparison. [V10 §7J / SIX CLASH TYPES]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J.1 — Six clash types | Different framings of a shared event. | Distinguishes whose framing each item carries. | The perspective difference remains visible. | [V10 §7J / SIX CLASH TYPES] |

SUB-PARTS: NONE

### C-7J.1.5 — Evidence insufficiency
Stamp: DESIGNED    Source: [V10 §7J / SIX CLASH TYPES]

ALONE
- What it is: DESIGNED — Conflict in which neither reading had enough context to be reliable. [V10 §7J / SIX CLASH TYPES]
- Takes in: DESIGNED — The conflicting readings and their insufficient context. [V10 §7J / SIX CLASH TYPES]
- Does: DESIGNED — Records the insufficiency behind the conflict. [V10 §7J / SIX CLASH TYPES]
- Gives out: DESIGNED — The evidence-insufficiency type. [V10 §7J / SIX CLASH TYPES]
- Must never: DESIGNED — Treat insufficient support as a reason to select either interpretation as correct. [V10 §7J]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J.1 — Six clash types: the context-insufficient comparison. [V10 §7J / SIX CLASH TYPES]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J.1 — Six clash types | Readings whose contexts were insufficient. | Retains evidence insufficiency as the clash type. | The stated limitation on the compared readings. | [V10 §7J / SIX CLASH TYPES] |

SUB-PARTS: NONE

### C-7J.1.6 — Context mismatch
Stamp: DESIGNED    Source: [V10 §7J / SIX CLASH TYPES]

ALONE
- What it is: DESIGNED — An apparent contradiction caused by different reading modes or retrieval configurations. [V10 §7J / SIX CLASH TYPES]
- Takes in: DESIGNED — The readings and the modes or retrieval configurations that produced them. [V10 §7J / SIX CLASH TYPES]
- Does: DESIGNED — Distinguishes that mismatch from a real conflict in the material. [V10 §7J / SIX CLASH TYPES]
- Gives out: DESIGNED — The context-mismatch type. [V10 §7J / SIX CLASH TYPES]
- Must never: DESIGNED — Erase the configuration difference or turn it into a winner selection. [V10 §7J]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J.1 — Six clash types: the mode/configuration comparison. [V10 §7J / SIX CLASH TYPES]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J.1 — Six clash types | An apparent conflict across different configurations. | Records context mismatch without resolving the source material. | The reason the comparison differs. | [V10 §7J / SIX CLASH TYPES] |

SUB-PARTS: NONE

### C-7J.2 — Genuine contradiction versus contextual difference
Stamp: DESIGNED    Source: [V10 §7J / GENUINE CONTRADICTION VS CONTEXTUAL DIFFERENCE]

ALONE
- What it is: DESIGNED — The common-conditions test for a genuine contradiction. [V10 §7J / GENUINE CONTRADICTION VS CONTEXTUAL DIFFERENCE]
- Takes in: DESIGNED — Both statements, with the same conditions, person, time and context held explicit. [V10 §7J / GENUINE CONTRADICTION VS CONTEXTUAL DIFFERENCE]
- Does: DESIGNED — Asks whether both statements could be simultaneously true under those same conditions: yes yields contextual difference; no yields genuine contradiction. [V10 §7J / GENUINE CONTRADICTION VS CONTEXTUAL DIFFERENCE]
- Gives out: DESIGNED — The recorded distinction, without a resolution. [V10 §7J / GENUINE CONTRADICTION VS CONTEXTUAL DIFFERENCE]
- Must never: DESIGNED — Resolve the contradiction after recording this distinction. [V10 §7J / GENUINE CONTRADICTION VS CONTEXTUAL DIFFERENCE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J — Clash Handling (§7J): the pair of statements with their conditions. [V10 §7J / GENUINE CONTRADICTION VS CONTEXTUAL DIFFERENCE]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J — Clash Handling (§7J) | Statements compared under the same conditions, person, time and context. | Records whether simultaneous truth is possible. | Genuine-contradiction or contextual-difference distinction. | [V10 §7J / GENUINE CONTRADICTION VS CONTEXTUAL DIFFERENCE] |

SUB-PARTS: NONE

### C-7J.3 — Clash record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [NHD-BU3]

ALONE
- What it is: ACCEPTED — The common record type for both detection modes, pointing to the original conflicting objects. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [NHD-BU3]
- Takes in: ACCEPTED — Stable `clash_id`; one of the six clash types; exact reading/root pointers and applicable `telling_id`s; conflict description; reading configurations and modes; detection mode and confidence; lifecycle state; Ness response status; timestamp. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [NHD-BU3]
- Does: ACCEPTED — Records the genuine-versus-contextual distinction with the clash type and retains exact references to the sources. Originals are pointed at rather than altered. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [NHD-BU3]
- Gives out: ACCEPTED — One permanently preserved original clash record with later history and responses linked beside it. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [NHD-BU3]
- Must never: ACCEPTED — Copy a source into a second authoritative home, rewrite originals, make confidence authoritative or create a second record for the same clash. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [NHD-BU3]
- Fails closed by: ACCEPTED — When the identity already exists, appends detection history to that clash instead of committing a duplicate original. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [NHD-BU3]

TOGETHER
- Fed by: DESIGNED — C-7J — Clash Handling (§7J): the detection result and its exact source references. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [NHD-BU3]
- Fed by: ACCEPTED — C-7J.3.1 — clash_id: the stable identifier; C-7J.3.2 — Clash-type field: the type; C-7J.3.3 — Exact conflicting-item pointers: exact item pointers; C-7J.3.4 — Specific conflict description: what specifically conflicts; C-7J.3.5 — Conflicting-reading retrieval configurations: retrieval configurations; C-7J.3.6 — Conflicting-reading modes: reading modes; C-7J.3.7 — Detection-mode field: detection mode; C-7J.3.8 — Detection confidence: detection confidence; C-7J.3.9 — Clash lifecycle state: lifecycle state; C-7J.3.10 — Ness response status: response status; C-7J.3.11 — Clash timestamp: timestamp. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gated by: ACCEPTED — C-7J.5 — Clash identity and one commit path: resolve the conflicting-item set and specific conflicting aspect against existing clashes before committing. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [NHD-BU3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J — Clash Handling (§7J) | One detected conflict with its source/configuration metadata. | Preserves its identity and content for later detection history and responses. | The clash-record collection, without rewriting input objects. | [V10 §7J] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |
| 2 · ACCEPTED | C-7J.3.1 — clash_id | The original clash identity. | Retains its stable identifier. | Later references address the same clash. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |
| 3 · ACCEPTED | C-7J.3.2 — Clash-type field | The original six-type classification. | Carries the recorded kind of difference. | Refinements remain separate linked proposals. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [V10 §7J / SIX CLASH TYPES] |
| 4 · ACCEPTED | C-7J.3.3 — Exact conflicting-item pointers | The exact readings, roots and applicable tellings. | Preserves pointers and the supporting provenance chain. | No original is copied or rewritten. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [NHD-A2] |
| 5 · ACCEPTED | C-7J.3.4 — Specific conflict description | The specific conflicting aspect. | Keeps the disagreement explicitly described. | The description stays attached to its sources. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |
| 6 · ACCEPTED | C-7J.3.5 — Conflicting-reading retrieval configurations | The conflicting readings' retrieval configurations. | Retains their configuration provenance. | The conflict remains context-qualified. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |
| 7 · ACCEPTED | C-7J.3.6 — Conflicting-reading modes | The compared readings' modes. | Keeps reading mode separate from detection mode. | Production context remains inspectable. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |
| 8 · ACCEPTED | C-7J.3.7 — Detection-mode field | The mode of detection. | Records which mode found the clash. | No additional authority attaches to a mode. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE] |
| 9 · ACCEPTED | C-7J.3.8 — Detection confidence | Detection confidence. | Retains confidence as metadata. | No truth weight is created. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |
| 10 · ACCEPTED | C-7J.3.9 — Clash lifecycle state | Recorded lifecycle information. | Preserves the original clash permanently. | Response or later detection cannot close it. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |
| 11 · ACCEPTED | C-7J.3.10 — Ness response status | The separate response history. | Keeps response status distinct from the original record. | Presentation can reflect a response without resolution. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |
| 12 · ACCEPTED | C-7J.3.11 — Clash timestamp | The original timestamp. | Retains the time on the original clash. | Later detections remain chronologically separate. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |

SUB-PARTS: C-7J.3.1 — clash_id; C-7J.3.2 — Clash-type field; C-7J.3.3 — Exact conflicting-item pointers; C-7J.3.4 — Specific conflict description; C-7J.3.5 — Conflicting-reading retrieval configurations; C-7J.3.6 — Conflicting-reading modes; C-7J.3.7 — Detection-mode field; C-7J.3.8 — Detection confidence; C-7J.3.9 — Clash lifecycle state; C-7J.3.10 — Ness response status; C-7J.3.11 — Clash timestamp

### C-7J.3.1 — clash_id
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The stable identifier of the clash. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — The identity established for that clash. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Keeps later detections and references attached to the same clash. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — The stable `clash_id`. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Create a second independent clash identity merely because the same clash was detected again. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Retains the existing clash identity on a match; no second original identifier is created for that same clash. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]

TOGETHER
- Fed by: ACCEPTED — C-7J.3 — Clash record: the original clash being identified. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gated by: ACCEPTED — C-7J.5 — Clash identity and one commit path: existing-identity matching precedes a new-record commit. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.3 — Clash record | The clash's stable identifier. | Retains the identity to which history and responses point. | Reference continuity across detections. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7J.3.2 — Clash-type field
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [V10 §7J / SIX CLASH TYPES]

ALONE
- What it is: ACCEPTED — The clash record's type from the six settled kinds. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [V10 §7J / SIX CLASH TYPES]
- Takes in: ACCEPTED — Direct contradiction, interpretive divergence, temporal change, perspectival difference, evidence insufficiency or context mismatch. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [V10 §7J / SIX CLASH TYPES]
- Does: ACCEPTED — Carries the classification, including the genuine-versus-contextual distinction. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [V10 §7J / SIX CLASH TYPES]
- Gives out: ACCEPTED — The recorded clash type. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [V10 §7J / SIX CLASH TYPES]
- Must never: ACCEPTED — Mutate the original type when later evidence merely proposes a refined classification; that proposal is a new linked event. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7J.3 — Clash record: the record's classification. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [V10 §7J / SIX CLASH TYPES]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.3 — Clash record | A classification from the settled six types. | Keeps the original classification on the record. | The visible kind of conflict, with later proposals preserved separately. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7J.3.3 — Exact conflicting-item pointers
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [NHD-A2]

ALONE
- What it is: ACCEPTED — References to the exact readings and roots involved, with `telling_id`s when the conflict is specifically between tellings. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [NHD-A2]
- Takes in: ACCEPTED — Reading and root identifiers; eligible stable telling identifiers and their provenance chain where applicable. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [NHD-A2]
- Does: ACCEPTED — Points back to the original records and preserves access from each telling to its immutable parent reading and supporting roots. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [NHD-A2]
- Gives out: ACCEPTED — Navigable references, not copied or rewritten source content. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [NHD-A2]
- Must never: ACCEPTED — Use a preparation payload, embedded substitute, partial telling set or integrity-failed card as a canonical semantic telling. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.3] [NHD-A2]
- Fails closed by: ACCEPTED — Blocks telling-level semantic use until the complete valid telling-set condition or legitimate zero-telling sentinel holds. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.3] [NHD-A2]

TOGETHER
- Fed by: ACCEPTED — C-7J.3 — Clash record: the exact items involved in the clash. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [NHD-A2]
- Gated by: ACCEPTED — C-READ.10.10 — Telling-set semantic eligibility: the telling-set semantic eligibility condition applies before any telling-level comparison or use. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.3] [NHD-A2]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.3 — Clash record | The exact conflicting objects and their identifiers. | Preserves source pointers and the telling-to-reading-to-root chain. | Traceable conflict evidence without source mutation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7J.3.4 — Specific conflict description
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The description of what specifically conflicts. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — The specific conflicting aspect of the referenced items. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Keeps the disagreement explicit alongside the pointers. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — The recorded conflict description. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Treat that description as a verdict selecting a winner. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7J.3 — Clash record: the conflict being described. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.3 — Clash record | The aspect on which the items differ. | Preserves what specifically conflicts. | An inspectable description linked to the exact items. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7J.3.5 — Conflicting-reading retrieval configurations
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The retrieval configurations of the conflicting readings. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — The configurations under which each reading was produced. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Keeps those configurations attached to the comparison. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — Recorded retrieval-configuration provenance. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Omit the conflicting readings' retrieval-configuration provenance from the clash record. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7J.3 — Clash record: the compared readings' retrieval configurations. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.3 — Clash record | Configuration provenance from the conflicting readings. | Retains the context needed to distinguish a mismatch. | The comparison remains configuration-qualified. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [V10 §7J / SIX CLASH TYPES] |

SUB-PARTS: NONE

### C-7J.3.6 — Conflicting-reading modes
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The reading modes under which the conflicting readings were produced. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — Each conflicting reading's mode. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Records mode provenance separately from detection mode. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — The conflicting readings' recorded modes. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Erase a difference in reading modes or use the modes to choose a winner. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7J.3 — Clash record: the modes of the compared readings. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.3 — Clash record | The conflicting readings' modes. | Preserves the circumstances of their production. | Mode-qualified comparison rather than an unqualified truth verdict. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [V10 §7J] |

SUB-PARTS: NONE

### C-7J.3.7 — Detection-mode field
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]

ALONE
- What it is: ACCEPTED — The mode that found the clash. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Takes in: ACCEPTED — Triggered detection or periodic/on-demand detection. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Does: ACCEPTED — States the originating detection mode on the same common record type. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Gives out: ACCEPTED — The recorded detection mode. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Must never: ACCEPTED — Give one mode greater authority or create a second clash solely because a different mode found it. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7J.3 — Clash record: the mode of the detection being recorded. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.3 — Clash record | The detection's mode. | Carries how the conflict was found. | Provenance, without an authority difference. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [V10 §7J] |

SUB-PARTS: NONE

### C-7J.3.8 — Detection confidence
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — Confidence in the detection, retained as metadata. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — The confidence associated with the detection. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Records it without turning it into authority. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — Detection-confidence metadata. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Treat confidence as authority or count re-detection as extra evidential weight. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7J.3 — Clash record: the detection's confidence. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.3 — Clash record | The recorded detection confidence. | Keeps it inspectable as metadata. | No change to the truth or authority of the compared readings. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7J.3.9 — Clash lifecycle state
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The clash's lifecycle-state information, subject to permanent preservation and non-resolution. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — The clash's recorded lifecycle state. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Preserves the original record; new evidence and responses are linked events and never close or resolve it. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — Lifecycle information with the original clash intact. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Present the clash itself as closed, resolved, erased or mutated by a later response or detection. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7J.3 — Clash record: the original record and its lifecycle information. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.3 — Clash record | Lifecycle-state information. | Keeps the permanently preserved clash distinct from presentation and response statuses. | No terminal closure or resolution is fabricated. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7J.3.10 — Ness response status
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The response-status information shown with a clash, distinct from the response event itself. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — The separate linked Ness-response events. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Allows a response status or current-presentation status to be shown while keeping the original clash unchanged. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — A response/presentation status beside the preserved clash. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Embed the response event inside the original clash or present response status as resolution. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7J.3 — Clash record: the clash whose response status is displayed. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.3 — Clash record | References to separate response events. | Keeps response information distinct from the immutable clash. | Presentation may reflect the response; the clash remains preserved. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT] |

SUB-PARTS: NONE

### C-7J.3.11 — Clash timestamp
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The timestamp on the original clash record. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — The time associated with that recorded clash. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Preserves the record's timestamp while later detections carry their own times in linked history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — The original clash timestamp. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Rewrite the original record's time to conceal a later detection. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7J.3 — Clash record: the original timestamped record. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.3 — Clash record | The original clash timestamp. | Keeps the recorded occurrence distinguishable from later history. | Preserved chronological provenance. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7J.4 — Two detection modes, same record type
Stamp: DESIGNED    Source: [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]

ALONE
- What it is: DESIGNED — Triggered comparison and wider periodic/on-demand scanning with one common clash-record type. [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Takes in: DESIGNED — A new reading or a wider scan scope across roots, threads, people, time periods and story layers. [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Does: DESIGNED — Runs the applicable comparison and records its detection mode; later detection adds linked history, evidence or a proposed refined classification. [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Gives out: DESIGNED — A clash record or linked detection-history contribution. [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Must never: DESIGNED — Give either mode authority to resolve, rank or select a winner; mutate original readings or clashes; spawn duplicate clashes. [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Fails closed by: DESIGNED — A system failure in triggered post-reading detection stops the stage and leaves the job `in_progress` for restart recovery. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7J — Clash Handling (§7J): the new-reading trigger or wider scan request. [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Fed by: DESIGNED — C-7J.4.1 — Triggered detection: new-reading comparison; C-7J.4.2 — Periodic or on-demand detection: wider periodic or on-demand comparison. [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): exact-purpose internal-use authorization applies before comparison. [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY] [V10 §7Q / TWO-STAGE OUTPUT ACCESS CONTROL]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J — Clash Handling (§7J) | A new reading or wider-scope scan. | Finds conflicts while preserving one common record type. | The detection record/history, without an authority difference between modes. | [V10 §7J] |
| 2 · DESIGNED | C-7J.4.1 — Triggered detection | A newly written reading. | Supplies same-root, same-thread and explicitly related comparison scope. | A triggered detection result. | [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE] |
| 3 · DESIGNED | C-7J.4.2 — Periodic or on-demand detection | A wider scan scope. | Keeps roots, threads, people, periods and story layers available within authorized bounds. | Wider detection history, without authority to choose a winner. | [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE] |

SUB-PARTS: C-7J.4.1 — Triggered detection; C-7J.4.2 — Periodic or on-demand detection

### C-7J.4.1 — Triggered detection
Stamp: DESIGNED    Source: [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]

ALONE
- What it is: DESIGNED — Detection started when a new reading is written. [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Takes in: DESIGNED — The new reading, readings of the same root, readings in the same thread and other explicitly related readings. [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Does: DESIGNED — Compares those readings through the common clash-handling route. [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Gives out: DESIGNED — A recorded detection result under the common record type. [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Must never: DESIGNED — Expand an explicit-relation comparison into an invented relationship or select a winning reading. [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Fails closed by: DESIGNED — Stops on system failure with the job still `in_progress`; restart resumes from the detection stage. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7J.4 — Two detection modes, same record type: a new-reading detection request. [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): internal-use authorization before the reading is used for detection. [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY] [V10 §7Q / TWO-STAGE OUTPUT ACCESS CONTROL]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J.4 — Two detection modes, same record type | The new reading and its specified related scopes. | Runs the triggered comparison. | The durable result and detection provenance. | [V10 §7J] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |

SUB-PARTS: NONE

### C-7J.4.2 — Periodic or on-demand detection
Stamp: DESIGNED    Source: [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]

ALONE
- What it is: DESIGNED — Wider scanning for slow-developing and cross-thread contradictions. [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Takes in: DESIGNED — Roots, threads, people, time periods and story layers within the scan's scope. [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Does: DESIGNED — Scans more widely; periodic scans remain bounded and configurable. New findings may append evidence or propose a refined classification through linked events. [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Gives out: DESIGNED — The same clash-record type and later linked history. [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Must never: DESIGNED — Mutate the original clash or readings, make duplicates, rank the sides or select a winner. [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J.4 — Two detection modes, same record type: the wider scan request and scope. [V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): internal-use authorization for the exact scan purpose. [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY] [V10 §7Q / TWO-STAGE OUTPUT ACCESS CONTROL]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J.4 — Two detection modes, same record type | The permitted wider scope. | Detects slow-developing and cross-thread conflicts under bounded configurable periodic scanning. | New clash records or linked history on an existing clash. | [V10 §7J] |

SUB-PARTS: NONE

### C-7J.5 — Clash identity and one commit path
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The shared identity-resolution and commit route for both detection modes. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — The set of conflicting items, the specific conflicting aspect and existing clash records. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Resolves that identity first. A match appends detection history to the existing clash; no match creates a new original clash. Re-detection adds history, never weight. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — One original record per clash identity and append-only later detection events. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Write an independent duplicate, count the same clash twice as evidence, or recover state from an uncommitted guess. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — After a crash, re-resolves identity and derives state from committed records only; idempotent commit never double-writes. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]

TOGETHER
- Fed by: DESIGNED — C-7J — Clash Handling (§7J): detection events from either mode. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Fed by: ACCEPTED — C-7J.5.1 — Detection-history event: a linked event for a matching later detection. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Fed by: DESIGNED — C-7J.5.2 — Triggered-operation recovery boundary: the live-path operation-key result or recovered durable result. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: ACCEPTED — Existing clash-identity matching precedes committing a new original clash. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J — Clash Handling (§7J) | A detected conflicting-item set and aspect. | Matches the identity and routes to original-record creation or linked history. | One identity, with no duplicate truth record or extra weight. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |
| 2 · ACCEPTED | C-7J.3 — Clash record | A proposed original clash record. | Allows a new original only when no existing identity matches. | Duplicate creation is prevented. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |
| 3 · ACCEPTED | C-7J.3.1 — clash_id | The identity proposed for a detection. | Retains an existing clash identifier when the identity matches. | Stable identity across repeated detections. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |
| 4 · ACCEPTED | C-7J.5.1 — Detection-history event | A later detection matching an existing clash. | Routes it to linked detection history. | A history event instead of a second clash. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |

SUB-PARTS: C-7J.5.1 — Detection-history event; C-7J.5.2 — Triggered-operation recovery boundary

### C-7J.5.1 — Detection-history event
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The append-only event for a later detection of the same clash. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — Existing clash identity, detection mode, time, configuration and confidence. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Adds the later detection's provenance to the existing clash history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — A linked detection-history event; the original clash remains intact. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Make a second clash or treat the repeated detection as stronger evidence. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — On recovery, committed identity/history is looked up before any idempotent commit, preventing a duplicate write. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]

TOGETHER
- Fed by: ACCEPTED — C-7J.5 — Clash identity and one commit path: a detection whose conflicting-item set and aspect match an existing clash. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Fed by: ACCEPTED — C-7J.5.1.1 — History detection mode: detection mode; C-7J.5.1.2 — History detection time: time; C-7J.5.1.3 — History detection configuration: configuration; C-7J.5.1.4 — History detection confidence: confidence. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gated by: ACCEPTED — C-7J.5 — Clash identity and one commit path: the conflicting-item set and specific aspect must match an existing clash before this history route is used. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.5 — Clash identity and one commit path | A repeated detection of an existing clash. | Records the mode, time, configuration and confidence in linked history. | Additional provenance without added evidential weight. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |
| 2 · ACCEPTED | C-7J.5.1.1 — History detection mode | The later detection mode. | Carries mode provenance in the append-only event. | The occurrence remains attributable. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |
| 3 · ACCEPTED | C-7J.5.1.2 — History detection time | The later detection time. | Carries the time in its own event. | Original clash time remains intact. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |
| 4 · ACCEPTED | C-7J.5.1.3 — History detection configuration | The later detection configuration. | Preserves configuration provenance in history. | No original field is substituted. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |
| 5 · ACCEPTED | C-7J.5.1.4 — History detection confidence | The later detection confidence. | Retains confidence as event metadata. | No second evidential vote. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |

SUB-PARTS: C-7J.5.1.1 — History detection mode; C-7J.5.1.2 — History detection time; C-7J.5.1.3 — History detection configuration; C-7J.5.1.4 — History detection confidence

### C-7J.5.1.1 — History detection mode
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The mode of this later detection. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — The mode of the matching detection event. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Records how the same clash was detected again. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — Detection-mode metadata in the history event. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Give the later mode additional authority. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7J.5.1 — Detection-history event: the later detection's mode. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.5.1 — Detection-history event | The later mode. | Retains mode provenance. | An inspectable history field. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7J.5.1.2 — History detection time
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The time of the later detection. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — The time associated with this matching detection event. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Adds that time to the linked history without rewriting the original clash. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — Detection-time metadata in the history event. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Replace the original clash timestamp with the later detection time. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7J.5.1 — Detection-history event: the later detection's time. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.5.1 — Detection-history event | The later detection time. | Keeps the subsequent occurrence chronologically distinct. | Append-only temporal history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7J.5.1.3 — History detection configuration
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The configuration associated with the later detection. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — That detection's configuration. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Records the configuration on the linked history event. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — Detection-configuration provenance. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Rewrite the original record to substitute the later configuration. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7J.5.1 — Detection-history event: the later configuration. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.5.1 — Detection-history event | The configuration of the matching detection. | Preserves it as history metadata. | The later detection remains attributable to its configuration. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7J.5.1.4 — History detection confidence
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The confidence associated with a later detection. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — The matching detection event's confidence. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Records it as metadata on that history event. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — Later detection-confidence metadata. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Count repeat detection or its confidence as a second vote for the clash's correctness. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7J.5.1 — Detection-history event: the later detection's confidence. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.5.1 — Detection-history event | The later confidence. | Keeps it inspectable without adding weight. | Metadata only. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7J.5.2 — Triggered-operation recovery boundary
Stamp: DESIGNED    Source: [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS]

ALONE
- What it is: DESIGNED — The clash-store side of the worker's operation-keyed detection stage. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS]
- Takes in: DESIGNED — `operation_key = {job_id}::{reading_id}::clash_detection`, the new reading, any previously committed result, and the worker's validated claim. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS]
- Does: DESIGNED — Checks for an existing keyed record first. If present, recovers `clash_found` and `clash_id` without re-running detection. Otherwise compares the specified readings, performs same-clash matching and commits the result with the key; no detection produces a `no_clash_sentinel`. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS]
- Gives out: DESIGNED — A keyed clash/history result or `no_clash_sentinel`, permitting the worker to append `clash_detection_completed` before Computed View processing. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS]
- Must never: DESIGNED — Commit the same `operation_key` twice, rerun an already durable result, or continue writing after the worker's claim validation fails. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS]
- Fails closed by: DESIGNED — Stops on system failure with the job still `in_progress`; recovery reads committed results before resuming the stage. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS]

TOGETHER
- Fed by: DESIGNED — C-7GA.11.7 — Step 7 — Clash detection: the reading and detection operation key. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: validates the held claim before every durable operation; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): internal-use authorization before comparison. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS]
- Changes: DESIGNED — C-7GA.11.7.1 — Step 7A — Record clash checkpoint: supplies recovered or newly recorded `clash_found`, `clash_id` or null and `operation_key` for the checkpoint. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.11.7 — Step 7 — Clash detection | The new reading and detection key. | Recovers the keyed result or makes one durable detection result. | The worker can checkpoint without duplicate detection work. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 2 · ACCEPTED | C-7J.5 — Clash identity and one commit path | A live-path detection operation with durable key. | Uses operation-key recovery alongside same-clash identity matching. | No repeated operation commit and no independent duplicate clash. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §10] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |

SUB-PARTS: NONE

### C-7J.6 — Ness response as separate event
Stamp: DESIGNED    Source: [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]

ALONE
- What it is: DESIGNED — A separately identified response event linked to a clash, never embedded in the clash record. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Takes in: DESIGNED — A stable event ID, clash ID, response type, Ness's exact statement or selection, timestamp, supplied evidence or explanation, and any requested downstream action. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Does: DESIGNED — Appends each response beside all earlier responses. Multiple responses are allowed; the current view may show the latest, with the full history available on demand. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Gives out: DESIGNED — A preserved response history and, when an action follows, a distinct action record linked both ways with its response. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Must never: DESIGNED — Erase an earlier response, delete an unchosen reading, or alter roots, readings or the original clash because Ness selected one interpretation. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J — Clash Handling (§7J): the clash and Ness's response to it. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Fed by: DESIGNED — C-7J.6.1 — Response event identifier: event identity; C-7J.6.2 — Response clash reference: clash reference; C-7J.6.3 — Response type: response type; C-7J.6.4 — Exact response statement or selection: exact statement or selection; C-7J.6.5 — Response timestamp: timestamp; C-7J.6.6 — Response evidence or explanation: supplied evidence or explanation; C-7J.6.7 — Requested downstream action: requested action and reciprocal action reference. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Fed by: ACCEPTED — C-7J.7.3 — Clash response and reading affirmation remain distinct: the distinct reading-affirmation relationship when one response concerns both a reading and a clash. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §17]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-7M — Computed View (§7M): explicit judgment may affect current use and presentation without rewriting underlying records. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J — Clash Handling (§7J) | A response to an existing clash. | Preserves the response as a separate identified event. | Response history and later presentation/current use only. | [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT] |
| 2 · DESIGNED | C-7M — Computed View (§7M) | The explicit response and its link to the clash. | May use the judgment in current presentation while preserving the complete response and source history. | The current view, never the original reading or clash. | [V10 §7J] [V10 §7M] |
| 3 · ACCEPTED | C-7J.8.2 — Clash detail pane and respond affordance | Ness's response entered through the detail pane. | Records the separate response event through the clash commit path. | A response linked to the preserved clash. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |
| 4 · DESIGNED | C-7J.6.1 — Response event identifier | The individual response. | Retains a separate stable event identity. | Each response remains addressable. | [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT] |
| 5 · DESIGNED | C-7J.6.2 — Response clash reference | The clash being addressed. | Carries its identifier on the response event. | Distinct records remain linked. | [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT] |
| 6 · DESIGNED | C-7J.6.3 — Response type | The kind of response supplied. | Preserves the response type. | The event remains distinguishable by meaning. | [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT] |
| 7 · DESIGNED | C-7J.6.4 — Exact response statement or selection | The actual statement or selection. | Keeps it exactly on its own event. | The response does not rewrite a reading. | [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT] |
| 8 · DESIGNED | C-7J.6.5 — Response timestamp | The response time. | Preserves its place in response history. | Later responses do not erase earlier dates. | [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT] |
| 9 · DESIGNED | C-7J.6.6 — Response evidence or explanation | Supplied evidence or explanation. | Keeps that basis with the response. | The supplied explanation stays inspectable. | [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT] |
| 10 · DESIGNED | C-7J.6.7 — Requested downstream action | A requested downstream action. | Preserves the request and reciprocal link to any resulting distinct action. | Action and response remain separate. | [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT] |
| 11 · ACCEPTED | C-7J.7.3 — Clash response and reading affirmation remain distinct | A clash response also addressing a reading. | Retains its independent event identity. | It can link to a separate reading-affirmation event. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §17] |
| 12 · DESIGNED | C-7M.2.1 — Computed View factor 1 — current Ness judgment | Relevant explicit Ness response or judgment events. | Supplies separate response events whose explicit judgments may affect current use. | Nothing in this card. | [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] |
| 13 · DESIGNED | C-7M.4.3.3 — Computed View Ness-response event trigger | The response and the object or clash it addresses. | Supplies the separate preserved response event. | Nothing in this card. | [V10 §7M / UPDATE TIMING] [V10 §7J] |
| 14 · ACCEPTED | C-7I.4.1 — View use of separate Ness responses | A separate Ness response or weightless specific-reading accept/reject event. | Supplies separate clash-response events. | Nothing in this card. | [V10 §7J] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §17] |
| 15 · ACCEPTED | C-7M.5.5.5 — Computed View Ness-response references | IDs of relevant separate Ness response events. | Supplies separate preserved response events. | Nothing in this card. | [V10 §7J] [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] |

SUB-PARTS: C-7J.6.1 — Response event identifier; C-7J.6.2 — Response clash reference; C-7J.6.3 — Response type; C-7J.6.4 — Exact response statement or selection; C-7J.6.5 — Response timestamp; C-7J.6.6 — Response evidence or explanation; C-7J.6.7 — Requested downstream action

### C-7J.6.1 — Response event identifier
Stamp: DESIGNED    Source: [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]

ALONE
- What it is: DESIGNED — The response event's own stable ID. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Takes in: DESIGNED — The individual response event. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Does: DESIGNED — Keeps that response separately addressable. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Gives out: DESIGNED — Its stable event ID. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Must never: DESIGNED — Collapse several responses into one event or overwrite an earlier response. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J.6 — Ness response as separate event: the individual response to be identified. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J.6 — Ness response as separate event | One response event. | Retains its independent stable identity. | The event remains separately referencable. | [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT] |

SUB-PARTS: NONE

### C-7J.6.2 — Response clash reference
Stamp: DESIGNED    Source: [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]

ALONE
- What it is: DESIGNED — The response event's pointer to the clash ID. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Takes in: DESIGNED — The identifier of the clash being addressed. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Does: DESIGNED — Links the separate response back to that clash. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Gives out: DESIGNED — A response-to-clash reference. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Must never: DESIGNED — Move the response inside the original clash record. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J.6 — Ness response as separate event: the referenced clash ID. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J.6 — Ness response as separate event | The target clash ID. | Preserves which clash the response addresses. | A navigable relationship between distinct records. | [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT] |

SUB-PARTS: NONE

### C-7J.6.3 — Response type
Stamp: DESIGNED    Source: [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]

ALONE
- What it is: DESIGNED — The kind of response recorded for the clash. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Takes in: DESIGNED — One reading accepted over another; both valid in different contexts; genuine change over time; insufficient evidence to judge; detection artifact; deferred judgment; request for reread; or another explicitly defined type. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Does: DESIGNED — Records the response as the specified kind without making it a change to the original readings or clash. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Gives out: DESIGNED — The response-type field. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Must never: DESIGNED — Treat choosing a reading as deletion of the other or as machine resolution of the clash. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J.6 — Ness response as separate event: the response's stated kind. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Gated by: DESIGNED — A further response type must be explicitly defined. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J.6 — Ness response as separate event | The response's kind. | Preserves the type together with the exact statement or selection. | An interpretable response event without a rewritten clash. | [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT] |

SUB-PARTS: NONE

### C-7J.6.4 — Exact response statement or selection
Stamp: DESIGNED    Source: [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]

ALONE
- What it is: DESIGNED — Ness's exact statement or selection in this response. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Takes in: DESIGNED — The statement or selection Ness actually supplied. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Does: DESIGNED — Records it on the separate response event. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Gives out: DESIGNED — The preserved exact response content. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Must never: DESIGNED — Replace earlier responses or rewrite the source readings to agree with this statement. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J.6 — Ness response as separate event: the actual statement or selection. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J.6 — Ness response as separate event | Ness's actual statement or selection. | Retains it exactly as the response content. | A preserved judgment event, not an edited reading. | [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT] |

SUB-PARTS: NONE

### C-7J.6.5 — Response timestamp
Stamp: DESIGNED    Source: [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]

ALONE
- What it is: DESIGNED — The timestamp of the response event. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Takes in: DESIGNED — The time associated with that response. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Does: DESIGNED — Keeps the response's place in the complete history. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Gives out: DESIGNED — The recorded response timestamp. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Must never: DESIGNED — Erase earlier response times when a later response arrives. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J.6 — Ness response as separate event: the response's time. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J.6 — Ness response as separate event | The response time. | Retains chronological history across repeated responses. | Current presentation can distinguish the latest event without losing earlier ones. | [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT] |

SUB-PARTS: NONE

### C-7J.6.6 — Response evidence or explanation
Stamp: DESIGNED    Source: [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]

ALONE
- What it is: DESIGNED — The evidence or explanation supplied with a response. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Takes in: DESIGNED — What Ness supplied as evidence or explanation. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Does: DESIGNED — Records it with that response event. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Gives out: DESIGNED — The supplied basis linked to the response. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Must never: DESIGNED — Use the response's basis to overwrite the original root, reading or clash. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J.6 — Ness response as separate event: the evidence or explanation accompanying the response. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J.6 — Ness response as separate event | The supplied basis for the response. | Preserves it as part of the separate event. | An inspectable response basis without source mutation. | [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT] |

SUB-PARTS: NONE

### C-7J.6.7 — Requested downstream action
Stamp: DESIGNED    Source: [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]

ALONE
- What it is: DESIGNED — Any downstream action requested in the response, with the resulting action recorded separately. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Takes in: DESIGNED — The request and, if an action follows, its distinct action record. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Does: DESIGNED — Records the request on the response; response and triggered action point to each other as separate records. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Gives out: DESIGNED — A requested-action entry and reciprocal links to any resulting action record. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Must never: DESIGNED — Collapse an action and its response into one record or alter the underlying readings as a consequence of the judgment. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J.6 — Ness response as separate event: the downstream action requested by Ness. [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J.6 — Ness response as separate event | An action request attached to the response. | Preserves the request and the two-way link to a distinct resulting action. | Traceable response/action provenance. | [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT] |

SUB-PARTS: NONE

### C-7J.7 — Downstream effects of clashes
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [NHD-BU3]

ALONE
- What it is: ACCEPTED — The effect an active clash has on how material is used and shown, without changing that material. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [NHD-BU3]
- Takes in: ACCEPTED — Clash-involved items, the active clash and separate responses or later evidence. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [NHD-BU3]
- Does: ACCEPTED — Keeps the clash beside the item in the View Layer, Person-Box view, Computed View, retrieval-labeled context, Living State Web evidence use and action-suggestion support. Handles the support as conflicted; too much conflict permits no clear current view. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [NHD-BU3]
- Gives out: ACCEPTED — Conflict-aware use and presentation with every original preserved. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [NHD-BU3]
- Must never: ACCEPTED — Block recording merely because material clashes; silently treat conflicted support as clean; close or resolve a clash through a response, newer evidence or re-detection. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [NHD-BU3]
- Fails closed by: ACCEPTED — Withholds or clearly labels weak, conflicted, stale or insufficient material wherever strength matters, rather than silently using it as uncontested support. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [NHD-BU3]

TOGETHER
- Fed by: DESIGNED — C-7J — Clash Handling (§7J): the active clash and its linked records. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [NHD-BU3]
- Fed by: ACCEPTED — C-7J.7.1 — Permanent clash and separate refinements: immutable clash history with separate refinements; C-7J.7.2 — Conflicted support stays qualified: qualified or withheld conflicted support. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-7M — Computed View (§7M): active clashes and contrary evidence stay beside the item; responses may affect current use without selecting a machine winner. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [NHD-BU3]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J — Clash Handling (§7J) | Clash-involved material entering downstream use. | Preserves the conflict and its qualified evidence status. | Use and presentation, never the original material. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] |
| 2 · DESIGNED | C-7M — Computed View (§7M) | Conflicted material and responses. | Surfaces the clash beside the item and allows no clear current view when support is too conflicted. | An honest current presentation without forced resolution. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [V10 §7M] |
| 3 · ACCEPTED | C-7J.7.1 — Permanent clash and separate refinements | An original clash with later events. | Keeps the original and later history distinct. | Permanent preservation without closure. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] |
| 4 · ACCEPTED | C-7J.7.2 — Conflicted support stays qualified | A conflicted support basis. | Carries the conflict into downstream evidence use. | Withheld or clearly labeled support. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] |
| 5 · DESIGNED | C-7M.2.6 — Computed View factor 6 — clashes and uncertainty | The source item's clashes, contrary support and unresolved uncertainty. | Supplies preserved clash effects and qualification rules. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] |

SUB-PARTS: C-7J.7.1 — Permanent clash and separate refinements; C-7J.7.2 — Conflicted support stays qualified; C-7J.7.3 — Clash response and reading affirmation remain distinct

### C-7J.7.1 — Permanent clash and separate refinements
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The original clash's permanent preservation despite later responses or evidence. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Takes in: ACCEPTED — The original clash, newer evidence, later detections and Ness responses. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Does: ACCEPTED — Appends detection history, supporting material or a proposed refined classification as new linked events. May show response or current-presentation status separately. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Gives out: ACCEPTED — The unchanged original and an accreting linked history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Must never: ACCEPTED — Close, resolve, mutate or erase the original clash, select a winner inside it, or display it as erased or resolved. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7J.7 — Downstream effects of clashes: the clash with its later events. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.7 — Downstream effects of clashes | Later evidence, detections and responses. | Adds linked history without changing the original clash. | Current presentation may change; the original never closes. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7J.7.2 — Conflicted support stays qualified
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The evidence-use boundary for material involved in an active clash. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Takes in: ACCEPTED — Weak, conflicted, stale or insufficient material wherever evidence strength matters. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Does: ACCEPTED — Withholds it or labels it clearly. Action suggestions retain the existing current-support and stricter action rules; no additional threshold is introduced. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Gives out: ACCEPTED — An honestly qualified support basis or withheld support. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Must never: ACCEPTED — Silently treat clash-involved material as clean, uncontested evidence or force a current winner. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Withholds or clearly labels the material when the support is weak, conflicted, stale or insufficient. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]

TOGETHER
- Fed by: ACCEPTED — C-7J.7 — Downstream effects of clashes: material whose clash affects downstream support. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.7 — Downstream effects of clashes | A conflicted evidence basis. | Keeps its conflict explicit or withholds the support. | No silent evidential upgrade. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7J.7.3 — Clash response and reading affirmation remain distinct
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §17]

ALONE
- What it is: ACCEPTED — The separation between a clash response and a reading-specific accept/reject event. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §17]
- Takes in: ACCEPTED — A reaction that concerns both a specific reading and an existing clash. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §17]
- Does: ACCEPTED — Preserves the B-AFFIRM reading event and the §7J response as separate records, linking them where appropriate. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §17]
- Gives out: ACCEPTED — Two properly scoped records connected by reference where the response concerns both. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §17]
- Must never: ACCEPTED — Collapse the records into one, change a reading's confidence/evidence/firmness/truth status, or treat rejection as proof that the opposite reading is correct. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §17]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J.6 — Ness response as separate event: the separate clash response. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §17]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-AFFIRM — Off-board Affirmation Feedback Seam (§11 item 23): any related reading accept/reject occurrence remains a distinct weightless event. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §17]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J.6 — Ness response as separate event | A response also accepting or rejecting a specific reading. | Keeps the clash event separate from reading affirmation and links them where appropriate. | Linked occurrences without merged identities or added truth weight. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §17] |
| 2 · DESIGNED | C-AFFIRM — Off-board Affirmation Feedback Seam (§11 item 23) | A reading accept/reject event related to an existing clash. | Retains its own identity beside the distinct clash response. | No rewriting of reading or clash. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §17] |
| 3 · ACCEPTED | C-AFFIRM.7.4 — Clash response stays separate from affirmation | A response that also concerns an existing clash. | Supplies canonical separate-event linkage. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §17] |

SUB-PARTS: NONE

### C-7J.8 — Clash and named-gap presentation
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Clash markers, inspectable clash details and labeled absence slots on presentation surfaces. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — Surfaced clash-involved items; exact clash/history/response references; an explicit gap record from an owning layer where one exists. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Shows a clash marker beside its item, opens full details on demand, and presents a recorded absence as a named empty slot. Uses plain main-surface wording and precise grading vocabulary in side-drawer notes. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — Simple-by-default, complete-on-demand presentation without overstated certainty. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Reorder, hide or resolve a clash through its marker; provide a resolve button; infer content from a gap or treat absence as evidence. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Fails closed by: DESIGNED — On output failure, withholds affected content for the unauthorized purpose; a safer version may be produced when possible. [V10 §7Q / TWO-STAGE OUTPUT ACCESS CONTROL]

TOGETHER
- Fed by: DESIGNED — C-7J — Clash Handling (§7J): the preserved clash and separate response/history records. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Fed by: ACCEPTED — C-7J.8.1 — Visible clash marker: the visible marker; C-7J.8.2 — Clash detail pane and respond affordance: full details and respond controls; C-7J.8.3 — Recorded named absence: an explicitly recorded named absence; C-7J.9.2 — Clash presentation and response operation records: the presentation-operation record. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy authorization before surfacing; C-SACL — Speaker Access-Control Layer (§25.4): applicable identity/access authorization before visible output. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §20]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J — Clash Handling (§7J) | A surfaced clash or explicit recorded gap. | Presents markers, details and honest named absence. | Visible presentation without changes to the source records. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §20] |
| 2 · DESIGNED | C-7I — View Layer (§7I) | Clash-involved items in a main surface. | Shows the clash beside the item with details on demand. | Conflict-aware presentation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |
| 3 · DESIGNED | C-7L — Person-Boxes (§7L) | Clash and gap records shown in a Person-Box. | Keeps the marker, pointers and details attached to the displayed record. | Presentation only, with distinct evidential statuses. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |
| 4 · ACCEPTED | C-7J.8.1 — Visible clash marker | An active-clash item being surfaced. | Keeps the marker beside its item. | The clash remains visible. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |
| 5 · ACCEPTED | C-7J.8.2 — Clash detail pane and respond affordance | A clash opened for inspection. | Supplies type, pointers, conflict description, history, lifecycle and response status. | Details and respond controls, without a resolve operation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |
| 6 · ACCEPTED | C-7J.8.3 — Recorded named absence | An explicit owning-layer gap record. | Preserves its name and absence kind on the surface. | A labeled empty slot rather than inferred content. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |
| 7 · ACCEPTED | C-7J.9.2 — Clash presentation and response operation records | A real presentation, named gap, filter or history switch. | Keeps the presented snapshot/version and occurrence traceable. | One append-only presentation record. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19] |
| 8 · DESIGNED | C-7M.2.6 — Computed View factor 6 — clashes and uncertainty | The source item's clashes, contrary support and unresolved uncertainty. | Supplies beside-item clash presentation and response detail. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] |
| 9 · ACCEPTED | C-7L.5.4 — Person-Box clashes section | Linked clash records and their owner-provided type and status. | Supplies compact clash markers and full detail/response presentation. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |

SUB-PARTS: C-7J.8.1 — Visible clash marker; C-7J.8.2 — Clash detail pane and respond affordance; C-7J.8.3 — Recorded named absence

### C-7J.8.1 — Visible clash marker
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — The visible clash marker beside every surfaced item involved in an active clash. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — The item and its active-clash reference. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Places the marker beside the item in main surfaces and in the Person-Box view. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A visible indication that the item participates in a clash. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Use the marker to reorder, hide or resolve the clash. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7J.8 — Clash and named-gap presentation: the surfaced item and its active-clash link. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.8 — Clash and named-gap presentation | An item with an active clash. | Displays its marker beside it. | Conflict visibility without an ordering or truth change. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |
| 2 · ACCEPTED | C-7I.1.3 — Current conflict presentation | A displayed item involved in an active clash and its preserved clash record. | Supplies existing marker. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-7J.8.2 — Clash detail pane and respond affordance
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — The expanded clash details and the response controls. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — Clash type; exact conflicting-item pointers; what specifically conflicts; detection history; lifecycle and response status. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Shows those details with navigable pointers. A response emits the separate §7J event through the B2 commit path, linked to a related B-AFFIRM event where appropriate. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — Inspectable details and a separate recorded response. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Offer a resolve button, erase or resolve the clash through a response, or collapse a clash response with reading affirmation. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7J.8 — Clash and named-gap presentation: the original clash and linked history/status information. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-7J.6 — Ness response as separate event: records the response as its own identified event. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.8 — Clash and named-gap presentation | A request to open a clash's details. | Shows all settled details and offers respond, never resolve. | Inspection and separately recorded responses. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |
| 2 · ACCEPTED | C-7I.1.3 — Current conflict presentation | A displayed item involved in an active clash and its preserved clash record. | Supplies existing detail/respond affordance and its separate event path. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-7J.8.3 — Recorded named absence
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — A named empty slot displaying an absence explicitly recorded by its owning layer. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — A gap record naming what is absent and the absence kind defined by that layer. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Presents that recorded absence with a clear label, simple by default and complete on demand. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A visible named gap, without inferred content. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Invent missing content, present the gap silently or treat absence of information as evidence. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7J.8 — Clash and named-gap presentation: the owning layer's explicit gap record. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Gated by: ACCEPTED — The owning layer must have recorded the absence explicitly; its own absence kind is used. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.8 — Clash and named-gap presentation | An explicit gap record from an owning layer. | Displays the named absence under that layer's absence-kind definition. | Honest presentation of the missing information. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |
| 2 · ACCEPTED | C-7I.6 — View named-gap presentation | A gap record naming the absent item and the absence kind supplied by that layer. | Supplies the existing named-gap presentation atom. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |
| 3 · ACCEPTED | C-7L.5.7 — Person-Box unresolved-identity section | Separate pending anchors and proposals with their evidence and unmet identity questions. | Supplies recorded named absences shown as labeled empty slots without evidence weight. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-7J.9 — Clash operational recordkeeping
Stamp: DESIGNED    Source: [V10 §0B] [MAP C-7J]

ALONE
- What it is: DESIGNED — The mandatory append-only living-memory record of clash operations. [V10 §0B] [MAP C-7J]
- Takes in: DESIGNED — Each detection run, created clash, appended detection history, `no_clash_sentinel`, response event, internal use, non-use, omission and failure. [V10 §0B] [MAP C-7J]
- Does: DESIGNED — Leaves one record per real operation, connected and retrievable as living memory. Logging does not recursively create an automatic log of itself or increase the underlying evidence's weight. [V10 §0B] [MAP C-7J]
- Gives out: DESIGNED — Traceable permanent operation records under the applicable access and authorization boundaries. [V10 §0B] [MAP C-7J]
- Must never: DESIGNED — Operate silently, destroy the history, leak protected content through logs, or count one underlying record as several independent votes. [V10 §0B] [MAP C-7J]
- Fails closed by: DESIGNED — Blocks unauthorized use of protected records; permanent preservation does not grant ordinary runtime access. [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY] [V10 §7Q / TWO-STAGE OUTPUT ACCESS CONTROL]

TOGETHER
- Fed by: DESIGNED — C-7J — Clash Handling (§7J): its real internal operations and their outcomes. [V10 §0B] [MAP C-7J]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): purpose-specific use, protected-boundary, influence-removal and TSC restrictions apply to operational records too; C-SACL — Speaker Access-Control Layer (§25.4): applicable identity/security authorization for access. [V10 §0B] [MAP C-7J]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J — Clash Handling (§7J) | A real clash operation, including a negative or failed result. | Preserves one connected append-only record under §0B. | Living operational history, never increased certainty of an interpretation. | [V10 §0B] [MAP C-7J] |

SUB-PARTS: C-7J.9.1 — Telling-link and semantic-gate operation records; C-7J.9.2 — Clash presentation and response operation records

### C-7J.9.1 — Telling-link and semantic-gate operation records
Stamp: ACCEPTED    Source: [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.3] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §10] [NHD-A2]

ALONE
- What it is: ACCEPTED — Structural provenance for a telling-level clash link and for blocked or resumed telling-specific use. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.3] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §10] [NHD-A2]
- Takes in: ACCEPTED — What was linked, the component establishing the link, provenance pointer, `schema_version` and producer-version provenance; structural identifiers and result states for block, recovery, idempotent skip and resumed fan-out. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.3] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §10] [NHD-A2]
- Does: ACCEPTED — Records each real operation once without private payload. A rejected or blocked downstream use remains visible as an operation; completed telling-set recovery resumes consumers idempotently without double work or double evidence. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.3] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §10] [NHD-A2]
- Gives out: ACCEPTED — Inspectable link, block, recovery, no-op and resume records. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.3] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §10] [NHD-A2]
- Must never: ACCEPTED — Log private payload, use a partial telling as canonical evidence or make repeated preparation/use/link logs strengthen the telling's correctness. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.3] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §10] [NHD-A2]
- Fails closed by: ACCEPTED — Keeps telling-level semantic fan-out blocked after card-stage failure until complete valid telling-set evidence or a legitimate zero-telling sentinel exists. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.3] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §10] [NHD-A2]

TOGETHER
- Fed by: DESIGNED — C-7J — Clash Handling (§7J): the telling-level link or attempted semantic use. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.3] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §10] [NHD-A2]
- Gated by: ACCEPTED — C-READ.10.10 — Telling-set semantic eligibility: the semantic gate controls telling-specific use, while properly authorized safety discovery remains separate and unblocked by that gate. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.3] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §10] [NHD-A2]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7J — Clash Handling (§7J) | A telling link or attempted telling-level clash use. | Preserves structural provenance and each block/resume/skip without payload leakage. | Traceable operations, without additional evidential weight. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.3] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7J.9.2 — Clash presentation and response operation records
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — The append-only records of clash presentation, named-gap presentation and clash responses. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Takes in: ACCEPTED — Which snapshot/version was presented, filters applied, history switches, each named-gap presentation and each separate clash-response occurrence. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Does: ACCEPTED — Records one real presentation or response operation once under privacy/access and applicable identity/security authorization. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Gives out: ACCEPTED — Connected presentation and response history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Must never: ACCEPTED — Leave presentations or responses silent, make their logs truth evidence or let repetition add certainty. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7J.8 — Clash and named-gap presentation: the presentation or named-gap occurrence. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the applicable privacy/access authorization remains required for these records. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7J.8 — Clash and named-gap presentation | A real presentation event, filter or history switch, or named gap shown. | Records the occurrence with the presented snapshot/version where applicable. | One append-only presentation record per real operation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19] |

SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece USED BY continuations

These rows add the reciprocal USED BY entries to the named external cards at assembly. They preserve the delivered cards; every row names both ends. The relationship wording is carried from the current TOGETHER field.

| Current card | Field | External card receiving USED BY row | Stamp | Relationship and condition | Source |
|---|---|---|---|---|---|
| C-7J — Clash Handling (§7J) | Fed by | C-READ — Reading record, validator, writer (§6B) | BUILT | C-READ — Reading record, validator, writer (§6B): readings and their root references for comparison in CY-A. | [V10 §6B] [V10 §7J] |
| C-7J — Clash Handling (§7J) | Fed by | C-7GA.11.7 — Step 7 — Clash detection | DESIGNED | C-7GA.11.7 — Step 7 — Clash detection: the new reading and its operation key after the reading is durable. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| C-7J — Clash Handling (§7J) | Fed by | C-READ.10.14 — Telling-reference handoff | ACCEPTED | C-READ.10.14 — Telling-reference handoff: eligible stable `telling_id` references with the parent-reading and supporting-root chain when the comparison is telling-level. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [NHD-A2] |
| C-7J — Clash Handling (§7J) | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): exact-purpose internal-use authorization, including influence-removal, protected-boundary and TSC restrictions, before detection. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| C-7J — Clash Handling (§7J) | Gated by | C-LMAC — Live Mechanism Access Coordinator (§26) | DESIGNED | C-LMAC — Live Mechanism Access Coordinator (§26): obtains the current internal-use authorization through the shared mechanism before the detection input is used. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| C-7J — Clash Handling (§7J) | Gated by | C-READ.10.10 — Telling-set semantic eligibility | ACCEPTED | C-READ.10.10 — Telling-set semantic eligibility: telling-specific semantic use waits for the complete valid telling set and checkpoint, or legitimate zero-telling sentinel; embedded, partial or integrity-failed substitutes are prohibited. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1] [NHD-A2] |
| C-7J — Clash Handling (§7J) | Changes | C-7D — Living State Web (§7D) | DESIGNED | C-7D — Living State Web (§7D): supplies clash records as permitted source-evidence while preserving their grounding and uncertainty. | [V10 §7D] [MAP C-7J] |
| C-7J — Clash Handling (§7J) | Changes | C-7M — Computed View (§7M) | DESIGNED | C-7M — Computed View (§7M): provides clashes and separate responses for current-use assembly and presentation without altering their originals. | [V10 §7M] [V10 §7J] |
| C-7J.3.3 — Exact conflicting-item pointers | Gated by | C-READ.10.10 — Telling-set semantic eligibility | ACCEPTED | C-READ.10.10 — Telling-set semantic eligibility: the telling-set semantic eligibility condition applies before any telling-level comparison or use. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.3] [NHD-A2] |
| C-7J.4 — Two detection modes, same record type | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): exact-purpose internal-use authorization applies before comparison. | [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY] [V10 §7Q / TWO-STAGE OUTPUT ACCESS CONTROL] |
| C-7J.4.1 — Triggered detection | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): internal-use authorization before the reading is used for detection. | [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY] [V10 §7Q / TWO-STAGE OUTPUT ACCESS CONTROL] |
| C-7J.4.2 — Periodic or on-demand detection | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): internal-use authorization for the exact scan purpose. | [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY] [V10 §7Q / TWO-STAGE OUTPUT ACCESS CONTROL] |
| C-7J.5.2 — Triggered-operation recovery boundary | Fed by | C-7GA.11.7 — Step 7 — Clash detection | DESIGNED | C-7GA.11.7 — Step 7 — Clash detection: the reading and detection operation key. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS] |
| C-7J.5.2 — Triggered-operation recovery boundary | Gated by | C-7GA.7.5 — Validate claim before durable work | DESIGNED | C-7GA.7.5 — Validate claim before durable work: validates the held claim before every durable operation; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): internal-use authorization before comparison. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS] |
| C-7J.5.2 — Triggered-operation recovery boundary | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7GA.7.5 — Validate claim before durable work: validates the held claim before every durable operation; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): internal-use authorization before comparison. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS] |
| C-7J.5.2 — Triggered-operation recovery boundary | Changes | C-7GA.11.7.1 — Step 7A — Record clash checkpoint | DESIGNED | C-7GA.11.7.1 — Step 7A — Record clash checkpoint: supplies recovered or newly recorded `clash_found`, `clash_id` or null and `operation_key` for the checkpoint. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS] |
| C-7J.6 — Ness response as separate event | Changes | C-7M — Computed View (§7M) | DESIGNED | C-7M — Computed View (§7M): explicit judgment may affect current use and presentation without rewriting underlying records. | [V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT] |
| C-7J.7 — Downstream effects of clashes | Changes | C-7M — Computed View (§7M) | DESIGNED | C-7M — Computed View (§7M): active clashes and contrary evidence stay beside the item; responses may affect current use without selecting a machine winner. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [NHD-BU3] |
| C-7J.7.3 — Clash response and reading affirmation remain distinct | Changes | C-AFFIRM — Off-board Affirmation Feedback Seam (§11 item 23) | DESIGNED | C-AFFIRM — Off-board Affirmation Feedback Seam (§11 item 23): any related reading accept/reject occurrence remains a distinct weightless event. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §17] |
| C-7J.8 — Clash and named-gap presentation | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy authorization before surfacing; C-SACL — Speaker Access-Control Layer (§25.4): applicable identity/access authorization before visible output. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |
| C-7J.8 — Clash and named-gap presentation | Gated by | C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy authorization before surfacing; C-SACL — Speaker Access-Control Layer (§25.4): applicable identity/access authorization before visible output. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |
| C-7J.9 — Clash operational recordkeeping | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): purpose-specific use, protected-boundary, influence-removal and TSC restrictions apply to operational records too; C-SACL — Speaker Access-Control Layer (§25.4): applicable identity/security authorization for access. | [V10 §0B] [MAP C-7J] |
| C-7J.9 — Clash operational recordkeeping | Gated by | C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): purpose-specific use, protected-boundary, influence-removal and TSC restrictions apply to operational records too; C-SACL — Speaker Access-Control Layer (§25.4): applicable identity/security authorization for access. | [V10 §0B] [MAP C-7J] |
| C-7J.9.1 — Telling-link and semantic-gate operation records | Gated by | C-READ.10.10 — Telling-set semantic eligibility | ACCEPTED | C-READ.10.10 — Telling-set semantic eligibility: the semantic gate controls telling-specific use, while properly authorized safety discovery remains separate and unblocked by that gate. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.3] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §10] [NHD-A2] |
| C-7J.9.2 — Clash presentation and response operation records | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the applicable privacy/access authorization remains required for these records. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19] |

## Cross-piece TOGETHER continuations for incoming uses

These are the reciprocal uses represented in the current USED BY tables. Their external owners retain their full mechanisms in their assigned pieces.

| Current card supplying use | External using card | Takes in there | Does there | Changes there | Stamp | Source |
|---|---|---|---|---|---|---|
| C-7J — Clash Handling (§7J) | C-7GA.11.7 — Step 7 — Clash detection | New reading, authorized related readings and `{job_id}::{reading_id}::clash_detection`. | Recovers an existing operation result or detects, same-clash-matches and records a clash/history or a negative sentinel. | Durable detection result; no duplicated clash and no change to the input readings. | DESIGNED | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| C-7J — Clash Handling (§7J) | C-7D — Living State Web (§7D) | Permitted clash records and their source references. | Keeps the clash available as state source-evidence without converting it into a truth verdict. | Grounded state derivation; clash and source histories remain preserved. | DESIGNED | [V10 §7D] [MAP C-7J] |
| C-7J — Clash Handling (§7J) | C-7M — Computed View (§7M) | Clash records, contrary evidence and separate Ness responses. | Surfaces clashes beside their items and allows responses to affect presentation/current use. | Current picture only; original roots, readings and clashes remain unchanged. | DESIGNED | [V10 §7M] [V10 §7J] |
| C-7J — Clash Handling (§7J) | C-LMAC — Live Mechanism Access Coordinator (§26) | An authorized clash-read request. | Returns the clash records and Ness-response events with their own current result and provenance. | The requesting function receives the permitted live component result. | DESIGNED | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| C-7J.5.2 — Triggered-operation recovery boundary | C-7GA.11.7 — Step 7 — Clash detection | The new reading and detection key. | Recovers the keyed result or makes one durable detection result. | The worker can checkpoint without duplicate detection work. | DESIGNED | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| C-7J.6 — Ness response as separate event | C-7M — Computed View (§7M) | The explicit response and its link to the clash. | May use the judgment in current presentation while preserving the complete response and source history. | The current view, never the original reading or clash. | DESIGNED | [V10 §7J] [V10 §7M] |
| C-7J.7 — Downstream effects of clashes | C-7M — Computed View (§7M) | Conflicted material and responses. | Surfaces the clash beside the item and allows no clear current view when support is too conflicted. | An honest current presentation without forced resolution. | DESIGNED | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [V10 §7M] |
| C-7J.7.3 — Clash response and reading affirmation remain distinct | C-AFFIRM — Off-board Affirmation Feedback Seam (§11 item 23) | A reading accept/reject event related to an existing clash. | Retains its own identity beside the distinct clash response. | No rewriting of reading or clash. | DESIGNED | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §17] |
| C-7J.8 — Clash and named-gap presentation | C-7I — View Layer (§7I) | Clash-involved items in a main surface. | Shows the clash beside the item with details on demand. | Conflict-aware presentation. | DESIGNED | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |
| C-7J.8 — Clash and named-gap presentation | C-7L — Person-Boxes (§7L) | Clash and gap records shown in a Person-Box. | Keeps the marker, pointers and details attached to the displayed record. | Presentation only, with distinct evidential statuses. | DESIGNED | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |

## Scope, paths and source dispositions

CY-A and P-MAIN step 14 use the C-7J root through the already-defined worker stage. The current cards use the immutable C-READ telling-eligibility and telling-reference cards and the C-7GA claim, checkpoint and sentinel cards; no second definitions are created. Existing incoming C-READ.10.10/C-READ.10.14 and C-7GA.11.7 links are represented in the current root and continuations.

The accepted Bundle 3 receipt establishes the status of its frozen v1_2 candidate. Bundle 3 §§8, 10, 16–20 provide the clash-owned additions; §§7, 9, 11–15 and the non-clash parts of §17 retain CH06-b/c/e and CH08-f ownership. A2 §§5A, 6 and 10 supply the telling boundary already decomposed in CH03-c. Bundle 6 mechanical §12 supplies the clash-read interface; its full request, control-path and retry mechanics belong to CH08-c. Bundle 2 formal relevance declarations and Bundle 4 retain the full view, state and action consumers in CH06-d/f and CH07-a/b; those consumers do not redefine the clash record. The inherited accepted-but-excluded B26 foundation source-scope gap remains open.

Searches covered the pinned READ folders by C-7J, Clash Handling, clash, contradiction, detection and response. B24's clash-detection occurrence belongs to the reading-channel validation rules already placed in CH05-a. A2 current-status and decision-index entries are navigation/status material only. The recovery buckets' read-only contradiction check belongs to the memory-health scope, not a new clash commit rule. The recovery ledger supplies no behavior. Earlier active-index versions are superseded navigation. No source-conflict line is added for the older open-schema wording: the accepted B2 package fills its stated design scope while leaving serialization, algorithms and governed values open. No distinct contradictory clash rule was selected or reconciled.

Full privacy/protected-storage and SACL mechanisms remain CH08-a and CH09-d; relevance and LMAC remain CH08-b/c; reading affirmation remains CH08-f; side paths remain CH11; all registers are inputs to the regenerated CH12 appendices.

## Source-to-card coverage added by CH06-a

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §7J / SIX CLASH TYPES | Six exact kinds and their defining differences | C-7J.1 and C-7J.1.1–C-7J.1.6 |
| V10 §7J / GENUINE CONTRADICTION VS CONTEXTUAL DIFFERENCE | Simultaneous truth under the same conditions, person, time and context; no resolution | C-7J.2 |
| V10 §7J; Bundle 3 §10 | Original clash and all eleven fields; telling pointers and source chains | C-7J.3 and C-7J.3.1–C-7J.3.11 |
| V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE | Triggered comparison scope; wider scope; bounded/configurable periodic scanning; no authority by mode | C-7J.4, C-7J.4.1, C-7J.4.2 |
| Bundle 3 §10 | Conflicting-item set plus aspect; match/no-match; one commit path; crash recovery from committed records | C-7J.5 |
| Bundle 3 §10 | Detection-history event: mode, time, configuration, confidence; no duplicate or extra weight | C-7J.5.1 and C-7J.5.1.1–C-7J.5.1.4 |
| V10 §7G-A / claim validation, Step 7, checkpoint 7A, sentinels and RC-6/RC-7 | Operation key; recover before rerun; no_clash_sentinel; system failure keeps job in_progress; checkpoint handoff | C-7J.5.2; exact claim/checkpoint/sentinel fields remain the existing C-7GA cards in CH05-b |
| V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT | Seven response fields; eight stated type alternatives; multiple responses; separate linked downstream actions | C-7J.6 and C-7J.6.1–C-7J.6.7 |
| Bundle 3 §8 | Recording never blocked; six downstream uses; qualified support; no clear current view; permanent clash; new linked refinements | C-7J.7, C-7J.7.1, C-7J.7.2 |
| Bundle 3 §17 | Distinct weightless reading response and clash response | C-7J.7.3; full reading-affirmation mechanics left to CH08-f |
| Bundle 3 §16 | Clash marker; detail pane; respond only; explicitly recorded named absence; plain main surface and precise side notes | C-7J.8 and C-7J.8.1–C-7J.8.3 |
| V10 §0B; Bundle 3 §19 | One real operation, one record; no recursive logging or double evidence; presentation/response log contents | C-7J.9 and C-7J.9.2 |
| A2 §§5A.1, 5A.3, 6, 10 | Canonical telling identity, semantic eligibility, blocked/skip/resume provenance; no private payload or double evidence | C-7J root, C-7J.3.3, C-7J.9.1; existing C-READ.10.10 and C-READ.10.14 reused |
| V10 §7Q; Bundle 3 §20 | Purpose-specific internal-use versus visible-output boundary; protection and identity gates | Current authorization boxes; full privacy architecture left to CH08-a |
| V10 §§7D, 7M; MAP C-7J | State evidence and current-view handoffs with conflict preserved | C-7J and cross-piece continuations; full consumers left to CH06-d/f |
| Bundle 6 mechanical §12 | Authorized clash-read result contains records and Ness responses with component provenance | C-7J USED BY C-LMAC; full query protocol left to CH08-c |
| Bundle 3 acceptance receipt; A2 package-complete receipt; Bundle 6 mechanical receipt | Exact accepted package identities/status, no new behavior | READ RECORD; receipt workflow/history excluded under §1.3 |
| Decision Defaults §§3G–3H; Companion §7J | Authority comparison and repeated conceptual clash content | No independent extra mechanism; current C-7J placement follows V10 and accepted scoped additions |
| Active decision index v0_11; A2 current-status note; September 24 recovery record and September 25 buckets | Navigation, dependency and restoration-scope checks | No behavior from the index or ledger; non-clash restored memory-health scope retained for later owners |

## Additional undecided implementation slots

| Owner | Slot | State |
|---|---|---|
| C-7J.3 — Clash record | Exact serialized schema, field forms, versioning and validation beyond the named conceptual fields | NOT DECIDED |
| C-7J.1 — Six clash types | Concrete detection/classification algorithm for the six types | NOT DECIDED |
| C-7J.4.2 — Periodic or on-demand detection | Periodic schedule, configurable limits and exact scan-trigger rules | NOT DECIDED |
| C-7J.5 — Clash identity and one commit path | Algorithm and normalization for matching the conflicting-item set and specific aspect | NOT DECIDED |
| C-7J.3.8 — Detection confidence | Detection-confidence representation, scale and assignment method | NOT DECIDED |
| C-7J.3.9 — Clash lifecycle state | Lifecycle-state vocabulary and transitions beyond permanent preservation and non-resolution | NOT DECIDED |
| C-7J.3.10 — Ness response status | Response/current-presentation status vocabulary and derivation details | NOT DECIDED |
| C-7J.6 — Ness response as separate event | Response-event serialization, validation and storage recovery mechanics beyond separate append-only events | NOT DECIDED |
| C-7J.6.7 — Requested downstream action | Dispatch/recovery machinery for a requested downstream action beyond separate reciprocally linked records | NOT DECIDED |
| C-7J.8 — Clash and named-gap presentation | Concrete interface layout and implementation beyond the settled marker/detail/response behavior | NOT DECIDED |
| C-7J.8.3 — Recorded named absence | Absence-kind taxonomy supplied by each owning layer; no common taxonomy is fixed here | NOT DECIDED |
| C-7J.5.2 — Triggered-operation recovery boundary | Storage-engine atomicity and crash protocol beyond operation-key idempotence and committed-record recovery | NOT DECIDED |

## Appendix A carry-forward — this piece

| Card | Empty field | Occurrence within field | State |
|---|---|---|---|
| C-7J.1 — Six clash types | Fails closed by | 1 | NOT DECIDED |
| C-7J.1 — Six clash types | Gated by | 1 | NOT DECIDED |
| C-7J.1 — Six clash types | Changes | 1 | NOT DECIDED |
| C-7J.1.1 — Direct contradiction | Fails closed by | 1 | NOT DECIDED |
| C-7J.1.1 — Direct contradiction | Gated by | 1 | NOT DECIDED |
| C-7J.1.1 — Direct contradiction | Changes | 1 | NOT DECIDED |
| C-7J.1.2 — Interpretive divergence | Fails closed by | 1 | NOT DECIDED |
| C-7J.1.2 — Interpretive divergence | Gated by | 1 | NOT DECIDED |
| C-7J.1.2 — Interpretive divergence | Changes | 1 | NOT DECIDED |
| C-7J.1.3 — Temporal change | Fails closed by | 1 | NOT DECIDED |
| C-7J.1.3 — Temporal change | Gated by | 1 | NOT DECIDED |
| C-7J.1.3 — Temporal change | Changes | 1 | NOT DECIDED |
| C-7J.1.4 — Perspectival difference | Fails closed by | 1 | NOT DECIDED |
| C-7J.1.4 — Perspectival difference | Gated by | 1 | NOT DECIDED |
| C-7J.1.4 — Perspectival difference | Changes | 1 | NOT DECIDED |
| C-7J.1.5 — Evidence insufficiency | Fails closed by | 1 | NOT DECIDED |
| C-7J.1.5 — Evidence insufficiency | Gated by | 1 | NOT DECIDED |
| C-7J.1.5 — Evidence insufficiency | Changes | 1 | NOT DECIDED |
| C-7J.1.6 — Context mismatch | Fails closed by | 1 | NOT DECIDED |
| C-7J.1.6 — Context mismatch | Gated by | 1 | NOT DECIDED |
| C-7J.1.6 — Context mismatch | Changes | 1 | NOT DECIDED |
| C-7J.2 — Genuine contradiction versus contextual difference | Fails closed by | 1 | NOT DECIDED |
| C-7J.2 — Genuine contradiction versus contextual difference | Gated by | 1 | NOT DECIDED |
| C-7J.2 — Genuine contradiction versus contextual difference | Changes | 1 | NOT DECIDED |
| C-7J.3 — Clash record | Changes | 1 | NOT DECIDED |
| C-7J.3.1 — clash_id | Changes | 1 | NOT DECIDED |
| C-7J.3.2 — Clash-type field | Fails closed by | 1 | NOT DECIDED |
| C-7J.3.2 — Clash-type field | Gated by | 1 | NOT DECIDED |
| C-7J.3.2 — Clash-type field | Changes | 1 | NOT DECIDED |
| C-7J.3.3 — Exact conflicting-item pointers | Changes | 1 | NOT DECIDED |
| C-7J.3.4 — Specific conflict description | Fails closed by | 1 | NOT DECIDED |
| C-7J.3.4 — Specific conflict description | Gated by | 1 | NOT DECIDED |
| C-7J.3.4 — Specific conflict description | Changes | 1 | NOT DECIDED |
| C-7J.3.5 — Conflicting-reading retrieval configurations | Fails closed by | 1 | NOT DECIDED |
| C-7J.3.5 — Conflicting-reading retrieval configurations | Gated by | 1 | NOT DECIDED |
| C-7J.3.5 — Conflicting-reading retrieval configurations | Changes | 1 | NOT DECIDED |
| C-7J.3.6 — Conflicting-reading modes | Fails closed by | 1 | NOT DECIDED |
| C-7J.3.6 — Conflicting-reading modes | Gated by | 1 | NOT DECIDED |
| C-7J.3.6 — Conflicting-reading modes | Changes | 1 | NOT DECIDED |
| C-7J.3.7 — Detection-mode field | Fails closed by | 1 | NOT DECIDED |
| C-7J.3.7 — Detection-mode field | Gated by | 1 | NOT DECIDED |
| C-7J.3.7 — Detection-mode field | Changes | 1 | NOT DECIDED |
| C-7J.3.8 — Detection confidence | Fails closed by | 1 | NOT DECIDED |
| C-7J.3.8 — Detection confidence | Gated by | 1 | NOT DECIDED |
| C-7J.3.8 — Detection confidence | Changes | 1 | NOT DECIDED |
| C-7J.3.9 — Clash lifecycle state | Fails closed by | 1 | NOT DECIDED |
| C-7J.3.9 — Clash lifecycle state | Gated by | 1 | NOT DECIDED |
| C-7J.3.9 — Clash lifecycle state | Changes | 1 | NOT DECIDED |
| C-7J.3.10 — Ness response status | Fails closed by | 1 | NOT DECIDED |
| C-7J.3.10 — Ness response status | Gated by | 1 | NOT DECIDED |
| C-7J.3.10 — Ness response status | Changes | 1 | NOT DECIDED |
| C-7J.3.11 — Clash timestamp | Fails closed by | 1 | NOT DECIDED |
| C-7J.3.11 — Clash timestamp | Gated by | 1 | NOT DECIDED |
| C-7J.3.11 — Clash timestamp | Changes | 1 | NOT DECIDED |
| C-7J.4 — Two detection modes, same record type | Changes | 1 | NOT DECIDED |
| C-7J.4.1 — Triggered detection | Changes | 1 | NOT DECIDED |
| C-7J.4.2 — Periodic or on-demand detection | Fails closed by | 1 | NOT DECIDED |
| C-7J.4.2 — Periodic or on-demand detection | Changes | 1 | NOT DECIDED |
| C-7J.5 — Clash identity and one commit path | Changes | 1 | NOT DECIDED |
| C-7J.5.1 — Detection-history event | Changes | 1 | NOT DECIDED |
| C-7J.5.1.1 — History detection mode | Fails closed by | 1 | NOT DECIDED |
| C-7J.5.1.1 — History detection mode | Gated by | 1 | NOT DECIDED |
| C-7J.5.1.1 — History detection mode | Changes | 1 | NOT DECIDED |
| C-7J.5.1.2 — History detection time | Fails closed by | 1 | NOT DECIDED |
| C-7J.5.1.2 — History detection time | Gated by | 1 | NOT DECIDED |
| C-7J.5.1.2 — History detection time | Changes | 1 | NOT DECIDED |
| C-7J.5.1.3 — History detection configuration | Fails closed by | 1 | NOT DECIDED |
| C-7J.5.1.3 — History detection configuration | Gated by | 1 | NOT DECIDED |
| C-7J.5.1.3 — History detection configuration | Changes | 1 | NOT DECIDED |
| C-7J.5.1.4 — History detection confidence | Fails closed by | 1 | NOT DECIDED |
| C-7J.5.1.4 — History detection confidence | Gated by | 1 | NOT DECIDED |
| C-7J.5.1.4 — History detection confidence | Changes | 1 | NOT DECIDED |
| C-7J.6 — Ness response as separate event | Fails closed by | 1 | NOT DECIDED |
| C-7J.6 — Ness response as separate event | Gated by | 1 | NOT DECIDED |
| C-7J.6.1 — Response event identifier | Fails closed by | 1 | NOT DECIDED |
| C-7J.6.1 — Response event identifier | Gated by | 1 | NOT DECIDED |
| C-7J.6.1 — Response event identifier | Changes | 1 | NOT DECIDED |
| C-7J.6.2 — Response clash reference | Fails closed by | 1 | NOT DECIDED |
| C-7J.6.2 — Response clash reference | Gated by | 1 | NOT DECIDED |
| C-7J.6.2 — Response clash reference | Changes | 1 | NOT DECIDED |
| C-7J.6.3 — Response type | Fails closed by | 1 | NOT DECIDED |
| C-7J.6.3 — Response type | Changes | 1 | NOT DECIDED |
| C-7J.6.4 — Exact response statement or selection | Fails closed by | 1 | NOT DECIDED |
| C-7J.6.4 — Exact response statement or selection | Gated by | 1 | NOT DECIDED |
| C-7J.6.4 — Exact response statement or selection | Changes | 1 | NOT DECIDED |
| C-7J.6.5 — Response timestamp | Fails closed by | 1 | NOT DECIDED |
| C-7J.6.5 — Response timestamp | Gated by | 1 | NOT DECIDED |
| C-7J.6.5 — Response timestamp | Changes | 1 | NOT DECIDED |
| C-7J.6.6 — Response evidence or explanation | Fails closed by | 1 | NOT DECIDED |
| C-7J.6.6 — Response evidence or explanation | Gated by | 1 | NOT DECIDED |
| C-7J.6.6 — Response evidence or explanation | Changes | 1 | NOT DECIDED |
| C-7J.6.7 — Requested downstream action | Fails closed by | 1 | NOT DECIDED |
| C-7J.6.7 — Requested downstream action | Gated by | 1 | NOT DECIDED |
| C-7J.6.7 — Requested downstream action | Changes | 1 | NOT DECIDED |
| C-7J.7 — Downstream effects of clashes | Gated by | 1 | NOT DECIDED |
| C-7J.7.1 — Permanent clash and separate refinements | Fails closed by | 1 | NOT DECIDED |
| C-7J.7.1 — Permanent clash and separate refinements | Gated by | 1 | NOT DECIDED |
| C-7J.7.1 — Permanent clash and separate refinements | Changes | 1 | NOT DECIDED |
| C-7J.7.2 — Conflicted support stays qualified | Gated by | 1 | NOT DECIDED |
| C-7J.7.2 — Conflicted support stays qualified | Changes | 1 | NOT DECIDED |
| C-7J.7.3 — Clash response and reading affirmation remain distinct | Fails closed by | 1 | NOT DECIDED |
| C-7J.7.3 — Clash response and reading affirmation remain distinct | Gated by | 1 | NOT DECIDED |
| C-7J.8 — Clash and named-gap presentation | Changes | 1 | NOT DECIDED |
| C-7J.8.1 — Visible clash marker | Fails closed by | 1 | NOT DECIDED |
| C-7J.8.1 — Visible clash marker | Gated by | 1 | NOT DECIDED |
| C-7J.8.1 — Visible clash marker | Changes | 1 | NOT DECIDED |
| C-7J.8.2 — Clash detail pane and respond affordance | Fails closed by | 1 | NOT DECIDED |
| C-7J.8.2 — Clash detail pane and respond affordance | Gated by | 1 | NOT DECIDED |
| C-7J.8.3 — Recorded named absence | Fails closed by | 1 | NOT DECIDED |
| C-7J.8.3 — Recorded named absence | Changes | 1 | NOT DECIDED |
| C-7J.9 — Clash operational recordkeeping | Changes | 1 | NOT DECIDED |
| C-7J.9.1 — Telling-link and semantic-gate operation records | Changes | 1 | NOT DECIDED |
| C-7J.9.2 — Clash presentation and response operation records | Fails closed by | 1 | NOT DECIDED |
| C-7J.9.2 — Clash presentation and response operation records | Changes | 1 | NOT DECIDED |

## Plain-gate and empty-box review

All current cards, their nine fields and their USED BY rows were compared for a restriction, precondition or failure outcome misplaced in an empty box. The duplicate-original refusal, existing-identity retention, triggered-stage failure and authorization refusal were placed in their failure boxes. Remaining empty failure boxes do not acquire an invented storage-failure mechanism from a positive record-field requirement. Required record fields and comparison context are inputs or intrinsic behavior, not fabricated external gates. No step card has three empty TOGETHER fields. No BUILT behavior is claimed for clash machinery; the single BUILT incoming field names the existing built reading-record source. All other relationship stamps follow the named target's established source status. The twelve additional slots distinguish unfinished mechanics from the accepted design content. The scan output is a mechanical inventory; the semantic disposition here records the accompanying source review.

| Card | Plain gate justification |
|---|---|
| C-7J.5 — Clash identity and one commit path | A new original may be committed only after existing-identity matching. This is the commit precondition inside this card; no separate owning card is defined. |
| C-7J.6.3 — Response type | An additional response type requires explicit definition; it is an outside definition, not a machine component. |
| C-7J.8.3 — Recorded named absence | The named-gap presentation requires an explicit absence already recorded by its owning layer; no universal gap-owner card is decided. |

## Coverage matrix — cumulative carried inventory











The following inventory retains the preceding pieces’ placements and read status. This piece’s additional placements and deferrals are in the source-scope table above; inherited notes are not fresh whole-read claims.
### File coverage

| Row | Source | Read scope | Placement |
|---|---|---|---|
| F001 | `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped read in CH04-b: §0B; §6A SCHEMA CONSTRAINTS; §6B schema/status boundary; full §7E-TSC §§1–31. Prior read credits retained. | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.1; C-STORE.2; C-STORE.3; CY-A Chapter 3-b: C-READ and its v1 record, validator, writer, quarantine, production-boundary and operation-record sub-parts; CY-A/CY-F reading-write interfaces. Chapter 3-c: governing checks for C-READ.10; A2/firmness additions stay ACCEPTED, never BUILT. Chapter 3-d: source-status and no-production-write boundaries; governing operational living-memory rule at C-READ.11.9.4.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.3, C-ENGINE-C.3.1, C-ENGINE-C.3.2, C-ENGINE-C.3.3, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.11.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1, C-ENGINE-AB.1.1, C-ENGINE-AB.1.2, C-ENGINE-AB.1.3, C-ENGINE-AB.2, C-ENGINE-AB.2.1, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.1, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.2.4, C-ENGINE-AB.3, C-ENGINE-AB.4, C-ENGINE-AB.5, C-ENGINE-AB.6, C-ENGINE-AB.8, C-ENGINE-AB.9.; CH03-k: C-INDEX, C-INDEX.1, C-INDEX.1.1, C-INDEX.1.2, C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.1, C-INDEX.4.2, C-INDEX.4.3, C-INDEX.4.4, C-INDEX.4.5, C-INDEX.4.7, C-INDEX.4.8, C-INDEX.5, C-INDEX.6.; CH03-l: C-GOLD, C-GOLD.2, C-GOLD.2.1, C-GOLD.3, C-GOLD.3.1, C-GOLD.6, C-GOLD.6.1, C-GOLD.6.2, C-GOLD.6.3, C-GOLD.7, C-GOLD.7.4.; CH03-o: C-INGEST, C-INGEST.1, C-INGEST.2, C-INGEST.3, C-INGEST.4, C-INGEST.4.1, C-INGEST.4.2, C-INGEST.4.3, C-INGEST.4.4, C-INGEST.4.5, C-INGEST.4.6, C-INGEST.4.7, C-INGEST.4.8, C-INGEST.4.8.1, C-INGEST.4.8.2, C-INGEST.4.8.3, C-INGEST.4.8.4, C-INGEST.4.9, C-INGEST.6.; CH03-p: C-DETECT, C-DETECT.1, C-DETECT.1.1, C-DETECT.1.3, C-DETECT.2, C-DETECT.2.1, C-DETECT.2.2, C-DETECT.2.3, C-DETECT.2.4, C-DETECT.2.5, C-DETECT.3, C-DETECT.3.1, C-DETECT.3.2, C-DETECT.3.3, C-DETECT.3.4, C-DETECT.3.5, C-DETECT.3.6, C-DETECT.4.1.; CH04-a: C-7E, C-7E.1, C-7E.1.1, C-7E.1.2, C-7E.2, C-7E.3, C-7E.4, C-7E.5, C-7E.5.1, C-7E.5.2, C-7E.5.3, C-7E.5.4, C-7E.5.5, C-7E.5.6, C-7E.6, C-7E.6.1, C-7E.6.2, C-7E.6.3, C-7E.6.4, C-7E.6.5, C-7E.6.6, C-7E.6.7, C-7E.7, C-7E.8, C-7E.8.1, C-7E.8.2, C-7E.8.3, C-7E.8.4, C-7E.9, C-7E.9.1, C-7E.9.2, C-7E.9.2.1, C-7E.9.2.2, C-7E.9.2.3, C-7E.9.2.4, C-7E.9.3, C-7E.9.3.1, C-7E.9.3.2, C-7E.9.3.3, C-7E.9.3.4, C-7E.9.3.5, C-7E.9.3.6, C-7E.9.4, C-7E.10, C-7E.10.1, C-7E.10.2, C-7E.11, C-7E.12, C-7E.13, C-7E.13.1, C-7E.13.4, C-7E.13.5, C-7E.13.6. CH04-b: see the exact source-scope and landing table above.  CH04-c: scoped read; exact scope and placement in the current source table.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-c: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F002 | `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Scoped read in CH04-b: §3N; inspection conflict. Prior read credits retained. | EXCLUDED: interaction/workflow guidance under §1.3 and §2.4. NOT PLACED: remaining behavior belongs to other component groups.; Chapter 3-a: C-STORE.2.3 Chapter 3-b: C-READ.1 confidence semantics and C-READ.2 uncertainty-preserving shape gate; remaining scope retained. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.2, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.8.; CH03-l: C-GOLD, C-GOLD.2, C-GOLD.2.1, C-GOLD.3, C-GOLD.3.1, C-GOLD.4, C-GOLD.4.1, C-GOLD.4.2, C-GOLD.4.3, C-GOLD.4.4, C-GOLD.4.5, C-GOLD.4.6, C-GOLD.5, C-GOLD.6, C-GOLD.6.1, C-GOLD.6.3, C-GOLD.8.3, C-GOLD.8.5.10, C-GOLD.8.5.11.; CH04-a: C-7E, C-7E.1.2, C-7E.5.2, C-7E.6.1, C-7E.6.2, C-7E.7, C-7E.8.4, C-7E.13.3. CH04-b: see the exact source-scope and landing table above.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F003 | `01_AUTHORITATIVE/cursorrules` | Scoped reread for CH03-o; prior whole-read credit retained where previously recorded | EXCLUDED: coding-process rules under §1.3. NOT PLACED: built-code boundaries belong to store, reader and code-boundary groups. Chapter 3-b: C-READ.1.12 per-store/global-key conflict and C-READ.3 shared write boundary; workflow remains excluded. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB.5.; CH03-k: C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.6.; CH03-l: C-GOLD, C-GOLD.9.; CH03-o: C-INGEST, C-INGEST.4, C-INGEST.4.7, C-INGEST.6.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F004 | `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Scoped read in CH04-b: Embedded TSC §§15–16; conflicting inspection and failed-authorization text. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. CH04-b: see the exact source-scope and landing table above.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F005 | `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped read in CH04-b: C-TSC and CY-D; component naming and path ownership. Prior read credits retained. | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.3.4; CY-A Chapter 3-b: C-READ component name, operation logging and consumer/caller relationships; CY-A/CY-F interfaces. Chapter 3-c: component ownership/names and Group A/D boundary; accepted A2 supplies behavior. Chapter 3-d: names, Group A ownership and per-reading seam versus full CY-G boundary.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.9.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1.1, C-ENGINE-AB.1.3, C-ENGINE-AB.2.1, C-ENGINE-AB.2.4, C-ENGINE-AB.4, C-ENGINE-AB.6, C-ENGINE-AB.6.1.; CH03-k: C-INDEX, C-INDEX.2, C-INDEX.3, C-INDEX.5, C-INDEX.6, C-INDEX.6.1, C-INDEX.6.2, C-INDEX.6.3, C-INDEX.6.4, C-INDEX.6.5, C-INDEX.6.6.; CH03-l: C-GOLD, C-GOLD.4, C-GOLD.4.6, C-GOLD.6, C-GOLD.6.2, C-GOLD.7, C-GOLD.7.1, C-GOLD.7.2, C-GOLD.7.3, C-GOLD.7.4.; CH03-o: C-INGEST, C-INGEST.4.4, C-INGEST.4.7, C-INGEST.5, C-INGEST.5.1, C-INGEST.5.2, C-INGEST.5.3, C-INGEST.5.4, C-INGEST.6.; CH03-p: C-DETECT, C-DETECT.1, C-DETECT.1.1, C-DETECT.1.2, C-DETECT.1.3, C-DETECT.2, C-DETECT.2.1, C-DETECT.2.2, C-DETECT.2.3, C-DETECT.2.4, C-DETECT.2.5, C-DETECT.3, C-DETECT.3.1, C-DETECT.3.3, C-DETECT.3.4, C-DETECT.3.6, C-DETECT.4, C-DETECT.4.1, C-DETECT.4.1.1, C-DETECT.4.1.2, C-DETECT.4.2.; CH04-a: C-7E, C-7E.3, C-7E.4, C-7E.5, C-7E.5.2, C-7E.6.1, C-7E.6.4, C-7E.7, C-7E.8, C-7E.11, C-7E.13, C-7E.13.1, C-7E.13.2, C-7E.13.3, C-7E.13.4, C-7E.13.5, C-7E.13.6, C-7E.13.7. CH04-b: see the exact source-scope and landing table above.  CH04-c: scoped read; exact scope and placement in the current source table.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-c: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F006 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F007 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F008 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole read in CH04-b: Acceptance/status evidence only. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F009 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md` | Whole read in CH04-b: Event adoption §§2–7; status and source envelope. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F010 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F011 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.9 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F012 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F013 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-c: scoped read; exact scope and placement in the current source table. |
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
| F024 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F025 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F026 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F027 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F028 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F029 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F030 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F031 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F032 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F033 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F034 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0 .md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F035 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md` | Scoped reread for CH04-a; prior whole-read credit retained where previously recorded | C-7B.7 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker. |
| F036 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md` | Scoped reread for CH03-j; prior whole-read credit retained where previously recorded | C-READ.10 and all A2-cited descendants: §§1–10 identity, card/preparation/event ownership, acceptance/correspondence, commit/recovery, legacy mapping, lifecycle, semantic/safety boundaries, references/rereading and logging. EXCLUDED: source revision history, acts of acceptance, implementation workflow and self-audit claims under §1.3. Other consumer mechanics remain with their owning groups.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards.; CH03-j: C-ENGINE-C, C-ENGINE-C.3.3, C-ENGINE-C.4, C-ENGINE-C.5, C-ENGINE-C.6, C-ENGINE-C.9, C-ENGINE-C.11.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F037 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_PACKAGE_COMPLETE_RECORD_v1_0.md` | Read whole for CH03-j | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker. |
| F038 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F039 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F040 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F041 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F042 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F043 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F044 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F045 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F046 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F047 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F048 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for C-STORE.4; receipt narrative excluded under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker. |
| F049 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | Scoped read in CH04-b: §13 TSC caller boundary. Prior read credits retained. | Chapter 3-a: C-STORE.4 and all descendants. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: §10 cross-batch reading reread for boundary check; no new B11 behavior written here, Chapter 3-a placement retained.; CH04-a: C-7E, C-7E.1.2, C-7E.5.6, C-7E.6.3, C-7E.6.4, C-7E.12. CH04-b: see the exact source-scope and landing table above. |
| F050 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole read in CH04-b: Acceptance/status evidence only. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F051 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md` | Whole read in CH04-b: Structural store, exact tables, constraints, transactions, recovery, archive, logging and open implementation choices. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F052 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH03-n | Status/identity checked for NHD-B16EEB; globally unique slot identifiers retained; acceptance narrative EXCLUDED by §1.3; CH03-l: Status/provenance only; no behavior from this receipt or historical blocker.; CH03-m: C-GOLD.1.8.1.5.1.; CH03-n: C-GOLD.1.10, C-GOLD.1.11, C-GOLD.1.11.1, C-GOLD.1.11.2, C-GOLD.1.11.3, C-GOLD.1.11.4, C-GOLD.1.11.5, C-GOLD.1.11.6, C-GOLD.1.11.7, C-GOLD.1.11.8, C-GOLD.1.11.9, C-GOLD.1.11.10, C-GOLD.1.11.11, C-GOLD.1.11.12, C-GOLD.1.11.13, C-GOLD.1.11.14, C-GOLD.1.11.15, C-GOLD.1.11.16, C-GOLD.1.11.17, C-GOLD.1.12, C-GOLD.1.12.1, C-GOLD.1.12.2, C-GOLD.1.12.3, C-GOLD.1.12.4, C-GOLD.1.12.5. |
| F053 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | §§2–6 establish exact accepted standalone scope and source identity. EXCLUDED from behavior: receipt history/roles/process; no mechanism sourced from receipt. |
| F054 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | C-READ.11 and every descendant: complete §§1–11 seam; §13 traces checked against the same rules. §12 external ownership and unspecified details recorded separately. EXCLUDED under §1.3: source status/history/process, self-audit and delivery narrative (§§14–15). |
| F055 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F056 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F057 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md` | Scoped reread for CH03-m; prior whole-read credit retained where previously recorded | C-READ.7.2 and its reciprocal C-READ.7 link: ACCEPTED guard from §1.2 (NHD-B24), matching FR-0608 CARRIED. Remaining B24 behavior NOT PLACED: belongs to later owning templates; no other B24 mechanism added here. Chapter 3-c C-READ.10.3.8.8 and source-conflict register: structural-disposition difference retained against A2; no new retry policy.; CH03-m: C-GOLD.1.8.1.5.2, C-GOLD.1.8.1.5.2.1, C-GOLD.1.8.1.5.2.2, C-GOLD.1.8.1.5.2.3, C-GOLD.1.8.4.3.1, C-GOLD.1.8.4.5, C-GOLD.1.8.4.8.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F058 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_PACKAGE_COMPLETE_RECORD_v1_0.md` | Newly read whole for this correction, all 132 lines; pinned Git blob verified | §§2–3, 5 and 12 establish the accepted standalone status and exact v7 identity used for C-READ.7.2; no behavior sourced from this receipt. EXCLUDED: closure history/process under §1.3; no implementation or integration claimed.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F059 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-e: exact read scope and placement in the current source table; prior credits retained. |
| F060 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F061 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F062 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F063 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F064 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1 and cited sub-parts; C-7B.7.4.7 and cited sub-parts; C-7B.7.5.3 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F065 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F066 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F067 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F068 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1.6 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F069 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F070 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_CANDIDATE_v1_4.md` | Carried through Chapter 3-a: Not yet read; whole file newly read in Chapter 3-b | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-b: EXCLUDED: status/consolidation and workflow narrative under §1.3. Used for locating later accepted owners only; it supplies no behavior in this piece.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F071 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F072 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F073 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F074 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F075 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F076 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F077 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F078 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F079 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | Scoped read in CH04-b: §5 paths 3–4; authority owner/limit cross-check. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F080 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F081 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F082 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F083 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for Bundle 6 mechanics; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F084 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped read in CH04-b: §3 held/sealed restrictions and privacy precedence. Prior read credits retained. | Chapter 3-a: C-STORE.5 / operation protections, B17, B20, B21; other component scopes NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: C-7E, C-7E.2, C-7E.8, C-7E.9.1, C-7E.11, C-7E.12. CH04-b: see the exact source-scope and landing table above.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-c: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F085 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for Origin policy; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F086 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Scoped reread for CH04-a; prior whole-read credit retained where previously recorded | Chapter 3-a: C-STORE.5 / Origin preservation policy; A3.4–A3.5 and other components NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: Navigation excerpt only; no new behavior sourced in this piece.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.7, C-ENGINE-AB.8.; CH04-a: C-7E.12.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F087 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Whole read in CH04-b: Acceptance/status evidence only. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F088 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md` | Whole read in CH04-b: Two-phase authorization/promotion, continuation, C1–C10, nine coordination record types, logging, failure and open implementation choices. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F089 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F090 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F091 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F092 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F093 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F094 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F095 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F096 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F097 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-c: whole read; exact scope and placement in the current source table. |
| F098 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-c: whole read; exact scope and placement in the current source table. |
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
| F112 | `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` | Read whole for CH03-n | C-GOLD.1 identities/records/currentness in 3-e; C-GOLD.1.5 operation/execution contracts in 3-f; C-GOLD.1.6 judgment chain/conditional proof in 3-g; C-GOLD.1.7 claim lifecycle/protected recovery in 3-h; derivation, applicability and remaining dependencies NOT PLACED: later pieces; CH03-l: C-GOLD.; CH03-m: C-GOLD.1.8, C-GOLD.1.8.1, C-GOLD.1.8.1.1, C-GOLD.1.8.1.2, C-GOLD.1.8.1.2.1, C-GOLD.1.8.1.2.2, C-GOLD.1.8.1.2.3, C-GOLD.1.8.1.2.4, C-GOLD.1.8.1.2.5, C-GOLD.1.8.1.3, C-GOLD.1.8.1.3.1, C-GOLD.1.8.1.3.2, C-GOLD.1.8.1.3.3, C-GOLD.1.8.1.3.4, C-GOLD.1.8.1.3.5, C-GOLD.1.8.1.4, C-GOLD.1.8.1.4.1, C-GOLD.1.8.1.4.2, C-GOLD.1.8.1.4.3, C-GOLD.1.8.1.5, C-GOLD.1.8.1.5.1, C-GOLD.1.8.1.5.2, C-GOLD.1.8.1.5.2.1, C-GOLD.1.8.1.5.2.2, C-GOLD.1.8.1.5.2.3, C-GOLD.1.8.1.5.3, C-GOLD.1.8.1.6, C-GOLD.1.8.2, C-GOLD.1.8.2.1, C-GOLD.1.8.2.2, C-GOLD.1.8.2.3, C-GOLD.1.8.2.4, C-GOLD.1.8.2.4.1, C-GOLD.1.8.2.4.2, C-GOLD.1.8.2.4.3, C-GOLD.1.8.2.5, C-GOLD.1.8.2.6, C-GOLD.1.8.2.7, C-GOLD.1.8.2.8, C-GOLD.1.8.3, C-GOLD.1.8.4, C-GOLD.1.8.4.1, C-GOLD.1.8.4.2, C-GOLD.1.8.4.2.1, C-GOLD.1.8.4.2.2, C-GOLD.1.8.4.2.3, C-GOLD.1.8.4.3, C-GOLD.1.8.4.3.1, C-GOLD.1.8.4.3.2, C-GOLD.1.8.4.4, C-GOLD.1.8.4.5, C-GOLD.1.8.4.6, C-GOLD.1.8.4.7, C-GOLD.1.8.4.8, C-GOLD.1.8.4.9, C-GOLD.1.8.5.; CH03-n: C-GOLD.1.9, C-GOLD.1.9.1, C-GOLD.1.9.2, C-GOLD.1.9.3, C-GOLD.1.9.4, C-GOLD.1.9.5, C-GOLD.1.9.6, C-GOLD.1.9.7, C-GOLD.1.9.8, C-GOLD.1.9.9, C-GOLD.1.9.10, C-GOLD.1.9.11, C-GOLD.1.9.12, C-GOLD.1.10, C-GOLD.1.11, C-GOLD.1.11.1, C-GOLD.1.11.2, C-GOLD.1.11.3, C-GOLD.1.11.4, C-GOLD.1.11.5, C-GOLD.1.11.6, C-GOLD.1.11.7, C-GOLD.1.11.8, C-GOLD.1.11.9, C-GOLD.1.11.10, C-GOLD.1.11.11, C-GOLD.1.11.12, C-GOLD.1.11.13, C-GOLD.1.11.14, C-GOLD.1.11.15, C-GOLD.1.11.16, C-GOLD.1.11.17, C-GOLD.1.12, C-GOLD.1.12.1, C-GOLD.1.12.2, C-GOLD.1.12.3, C-GOLD.1.12.4, C-GOLD.1.12.5. |
| F113 | `05_ACTIVE_CANDIDATE/NH_B24_REJECTION_CATEGORY_DECISION_2026-09-23_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F114 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F115 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read whole; NHD-B24 row searched for this correction; Chapter 3-c NHD-A2/NHD-SLF and dependency navigation searches, not a whole-file read; Chapter 3-d NHD-B16/NHD-B16EEB navigation only | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; Chapter 3-a: Navigation only: NHD-B11 and NHD-BU1; no behavior sourced from the index; this correction: NHD-B24 navigation for C-READ.7.2 Chapter 3-c: NHD-A2/NHD-SLF navigation only. Chapter 3-d: navigation only, no behavior sourced from index. |
| F116 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F117 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F118 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F119 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F120 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F121 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F122 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-c: whole read; exact scope and placement in the current source table. |
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
| F137 | `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | C-7A.6 and cited sub-parts; C-7A.13 and cited sub-parts; C-7A.15 and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. Chapter 3-b: C-READ.7 (excluding the ACCEPTED C-READ.7.2 guard) and C-READ.8 (FR-0125–FR-0133); C-READ.1.12.1 (FR-0123); C-READ.9 (FR-0136).  CH04-c: scoped read; exact scope and placement in the current source table. |
| F138 | `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH00.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | Naming/path continuity only; no Chapters 0–2 (carried placement) behavior sourced from this chapter. |

### V10 heading coverage

| Row | V10 heading | Placement / remaining scope |
|---|---|---|
| V10-H001 | ### This is `NH_MASTER-20_CORRECTED_v10.md`, a corrected candidate in the Master 20 lineage. It is NOT YET ADOPTED. `NH_MASTER-19_CORRECTED_v7_1.md` (SHA-256: `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf`) remains the authoritative immutable Master until Ness explicitly adopts the corrected Master 20. | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H002 | ### Historical provenance (Master 19 lineage): | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H003 | ## 0. THE PREMISE — NEVER DECIDE FACTS (NEVER CLOSE THE BOOK)  [DESIGNED — the floor under every rule] | Partial placement: C-7A and cited sub-parts; C-7B.9.3. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ interpretation remains revisable. |
| V10-H004 | ## 0A. THE TWO MACHINERIES — DUMB vs SMART (psychologics)  [DESIGNED — top-level frame] | Partial placement: C-7A and cited sub-parts; C-7B.1 and cited sub-parts; C-7B.2.5; C-7B.3.2; C-7B.3.3; C-7B.9 and cited sub-parts; C-7B.11 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ record-carriage boundary; no new interpretation by the writer. |
| V10-H005 | ## 0B. FULL-TRANSPARENCY AND LIVING-RECORD LAW  [DESIGNED — foundational operating rule] | C-7A.16 and cited sub-parts; C-7A.17 and cited sub-parts; C-7B and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. Chapter 3-b: C-READ.6 operation records and health-check operation recording.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim.  CH04-b: held-access and required audit-history boundaries. |
| V10-H006 | ## 1. WHAT N.H IS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H007 | ## 1A. THE INPUT-AGNOSTIC PRINCIPLE — ONE ENGINE, MANY FRONT DOORS  [DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading.  CH04-e: C-9A and explicit shared/deferred owners. |
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
| V10-H018 | ### SCHEMA CONSTRAINTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1 and C-READ.2.  CH04-b: C-TSC.17.8.3 reuses the existing seven-field root-schema card. |
| V10-H019 | ### PRODUCTION READINGS AUTHORIZATION | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.5 and its protections. |
| V10-H020 | ### PROTECTED FILES AND STORES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.4/C-READ.5 destination separation; edit workflow excluded. |
| V10-H021 | ### DRY-RUN PROTOCOL | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H022 | ### §12 INCOMING — CURRENT STATUS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H023 | ## 6B. THE ACCRETIVE STORE — SCHEMA + STATE  [BUILT & VERIFIED] | Partial placement: C-7A.8 and cited sub-parts; C-7B.2.8.4 and cited sub-parts; C-7B.10.1.3; C-7B.11 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ.1 twelve-field representation; C-READ.2; C-READ.3; C-READ.4.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim.  CH04-b: C-TSC.17.8.3 reuses the existing seven-field root-schema card. |
| V10-H024 | ## 7. THE BIG DESIGN — UNIVERSAL FILTER + MEANING ENGINE  [engines A + B BUILT; §§7E–7P core-conceptually designed S17; §§7D and 7Q partially conceptually designed] | C-7A and C-7B detailed subsections follow. NOT PLACED: engine implementation behavior belongs to Group A. |
| V10-H025 | ### 7A — THE UNIVERSAL FILTER (operating rules): | C-7A and cited sub-parts; C-7B.3 and cited sub-parts; C-7B.11 and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. Chapter 3-b: C-READ reciprocal Universal Filter use; principles retained from Chapter 2. |
| V10-H026 | ### 7B — THE MEANING ENGINE (mechanism): | C-7B and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. |
| V10-H027 | ### 7C — THE FORCED BUILD ORDER (never re-fought): | EXCLUDED: forced build order under §1.3. NOT PLACED: engine implementations belong to Group A. |
| V10-H028 | ## 7D. THE LIVING STATE WEB — PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ grounded reading consumer relationship. |
| V10-H029 | ## 7E. CATALOG FRONT DOOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-d: C-14 and explicit shared/deferred owners. |
| V10-H030 | ### §7E-TSC DETAILED DESIGN  [ACCEPTED DESIGN WITH LATER CORRECTIONS — NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-b: full §§1–31 landed in C-TSC and all recursive sub-parts; §31 status evidence only. |
| V10-H031 | ## 7F. CONTEXT RETRIEVAL  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1.9 retrieval audit and genuine no-context audit; retrieval machinery remains with C-7F.  CH05-c: C-7F and explicit shared/deferred owners. |
| V10-H032 | ## 7G. MEANING ENGINE INTERIOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ acceptance/shape distinction and caller relationship; C-READ.3 new-root write handoff also cites the nested §7G-A subsection.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  CH05-a: C-7G and explicit shared/deferred owners.  CH05-b: C-7GA and explicit shared/deferred owners. |
| V10-H033 | ### §7G CREATION-AWARE MODE  [SETTLED CONCEPT — NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-d: C-14 and explicit shared/deferred owners.  CH05-a: C-7G and explicit shared/deferred owners.  CH05-e: C-CREATE and explicit shared/deferred owners. |
| V10-H034 | ## 7H. REREAD LIFECYCLE  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ reread output relationship; detailed orchestration remains with C-7H.  CH05-d: C-7H and explicit shared/deferred owners. |
| V10-H035 | ## 7I. VIEW LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ history/current-view use; view machinery remains with C-7I. |
| V10-H036 | ## 7J. CONTRADICTION AND CLASH HANDLING  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ clash-consumer relationship; clash machinery remains with C-7J. |
| V10-H037 | ## 7K. STORY LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7A.8.3; C-7B.3.1; C-7B.3.3 and cited sub-parts; C-7B.3.4. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ.1.5/1.6 speaker/perspective and embedded-v1-telling boundaries; future telling identity remains for its accepted package.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H038 | ## 7L. PERSON-BOXES  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.4. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ Person-Box consumer relationship. |
| V10-H039 | ## 7M. COMPUTED VIEW  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ current-use consumer relationship. |
| V10-H040 | ## 7N. ACTION SURFACING  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H041 | ## 7O. ACTION-RESULT RETURN PATH  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H042 | ## 7P. PERMISSION AND AUTHORITY BOUNDARIES  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H043 | ## 7Q. PRIVACY, DELETION, AND SENSITIVE-DATA HANDLING  [PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-e: C-9A and explicit shared/deferred owners. |
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
| V10-H066 | ## 9A. IMAGE INGEST — FIRST WORKED FRONT-DOOR EXAMPLE  [DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading.  CH04-e: C-9A and explicit shared/deferred owners. |
| V10-H067 | ## 10. ORIGINALITY (honest calibration) | Partial placement: C-7B.9.3. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H068 | ## 11. WHAT'S OPEN / NEXT (priority order) | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ foundation status and quarantine/production boundary; restored details use the decision record plus named archive, not the compressed V10 line. |
| V10-H069 | ## 11-SETTLED. (condensed) | EXCLUDED: condensed decision/session narrative under §1.3; repeated runtime rules are represented by their detailed owning sections. |
| V10-H070 | ## 12. SESSION 6 — THE DATA-RESCUE OPERATION  [recovery done; ingest FROZEN] | EXCLUDED: history, provenance or build/process narrative under contract §1.3.  CH04-e: C-9A and explicit shared/deferred owners. |
| V10-H071 | ## 13. THE LIVE LOOP  [DESIGNED — not built] | Partial placement: C-7B.9; C-7B.10.1 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-c: live-loop surface and model boundary in C-13; remaining chat/model internals retain their later owners.  CH04-d: C-14 and explicit shared/deferred owners. |
| V10-H072 | ## 14. THE CHAT FRONT DOOR  [PARTIALLY SETTLED, PARTIALLY OPEN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading.  CH04-c: live-loop surface and model boundary in C-13; remaining chat/model internals retain their later owners.  CH04-d: C-14 and explicit shared/deferred owners.  CH05-e: C-CREATE and explicit shared/deferred owners. |
| V10-H073 | ## 15. SESSION 10 — BOOT HYGIENE + SIGN-IN + .CURSORRULES  [housekeeping done] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H074 | ## 16. THE MODEL LAYER — THE BORROWED MOUTH + THE SEARCH MODEL  [DESIGNED + partly on disk] | Partial placement: C-7B.6. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-c: live-loop surface and model boundary in C-13; remaining chat/model internals retain their later owners. |
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

### Carried bridge source landing map

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

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.

## READ RECORD

Source bytes are pinned to 6a7160ba688ba4e433a31899162815df7e2bab17. Whole credit is limited to the rows labeled Whole. All other rows record scoped reading or search; they do not remove whole-file obligations. The governing contract §§5–11 and lessons were reopened before writing; the cloned §11.3 was reopened for the after-writing check. The complete route note, contract, lessons v0_2 and run instructions v0_3 were read as instructions, never used as behavior sources.

| Source file | Reading scope / whole-file credit | SHA-256 |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: complete §§0, 0A, 0B, 1, 7J and 7Q; complete worker claim/validation block, Step 7/7A–7C, sentinels and RC-6/RC-7; state/view handoff references and status comparison. | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped: full C-7J and Group D card table; CY-A/P-MAIN ownership navigation. | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Scoped: §§3G–3H and status/open boundaries; clash-topic navigation. | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Scoped: complete §7J duplicate conceptual text; no source narrative imported. | `cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md` | Whole: all sections; only clash-owned rules placed here; other owner scopes named above. | `3566cf0f917fb4f7eb329d9089f6e238fe4afbacbae2c73c8b2716e3397e7c2e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Whole: acceptance and exact source identity. | `405717e5528df74b9842dee6da8b3de69b82a738e478d06c2e1025243ae56a16` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md` | Scoped: complete §5A, §6 and §10 for downstream semantic eligibility, identity and logging; existing atomic owners retained. | `f91da6426817031cf2c0b14fb467a3e1d97d2ea3c67d27a07d8b1831f9895a55` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_PACKAGE_COMPLETE_RECORD_v1_0.md` | Whole: accepted scope, exact identity and remaining dependencies. | `ce05634aea94f229346ee7b7fbbede3d83113c7c37292e50085d38597233ca64` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped: complete §12 LMAC query contracts; only clash query result/interface placed here. | `bc1095955525fcea56cb4d16057c93bfb15eec42a83a1b644baf0e87a473f64e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: acceptance and exact mechanical-package identity; dated unrelated dependencies do not alter the clash interface. | `c5e379f508f3d2c498dfcecfe567db20db4362872de4feff4c7da57d4ff7de79` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Scoped: clash consumer search; full declarations left to their view/state/action owners. | `b2a5b3fbea75f7123a16c8a45c0fb096f4c4565585a4a0c7b7709e70f27d000e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` | Scoped: clash consumer search; full node/snapshot/action mechanics left to CH06-d/f and CH07-a/b. | `0c9a201130d5811c838fea0d5655c8a98aac909afdc60024830204a690e77f97` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md` | Scoped: clash-detection occurrence in validation-facing channel scope; existing CH05-a ownership. | `7f5762e5bc3d7d0fa554ad41426d2cc2f14fb7753a79b67fbd675f6c6b8a2171` |
| `05_ACTIVE_CANDIDATE/NH_A2_CURRENT_STATUS_v1_1.md` | Scoped: telling/clash interface status navigation, not a replacement for the accepted A2 package. | `35d1a10af9a16685515a6b668cfe5a0b3be3fe80abef901e3277b4901d22b167` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Scoped: NHD-M7J, NHD-BU3 and NHD-A2 navigation plus clash-topic search; no behavior derived from the index. | `aad8d1aeee9a331ad6f4d9ddbcfa9c42eae2a94e1ef1bccde7484079181ff7b4` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_2026-09-24_v0_1_CANDIDATE.md` | Whole: restoration scope/precedence checked; no extra clash mechanism extracted. | `b6643a6b208a0aa6167d032769a1ea5be4f64f672289a16fc216ef23b56c2fe0` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Scoped: Group 6 read-only memory-health contradiction check, retained for its later owner; no archive opened for current clash behavior. | `9f6f9cac1e07ab14f0c6f3ed834b8260265dac6f6a430fa12be5c6e4c3f0b59f` |

### Instruction and artifact identities

| File | SHA-256 |
|---|---|
| `NH_MASTER-21_SYSTEM_BEHAVIOR_BUILD_CONTRACT_FOR_CHATGPT_v1_0.md` | `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1` |
| `NH_MASTER-21_WRITER_LESSONS_FROM_AUDITS_v0_2.md` | `dae584222798cc8626e8abf1b1f184b7e65a463617932ce3e76f1265b80fa819` |
| `NH_MASTER-21_WRITER_RUN_INSTRUCTIONS_v0_3.md` | `96cd87e5e7049bf492e1a498d63fd38d002b538a9650f85d1e15b7c7d68f09e2` |
| `NH_MASTER-21_WRITING_1_MANIFEST.md` | `e0cb5fc488c075a22e836961ed2d13b602207a66b34063cdfa796956bb5c04bd` |
| `NH_MASTER-21_ROUTE_AND_WORKING_METHOD_v0_1_CANDIDATE.md` | `fbd0378c4fd2ba55710ec76ec98f68bf7daa574f5857078dcf70835d8fd30a89` |

### Earlier chapter identities preserved

| Piece | SHA-256 |
|---|---|
| CH01 | `f86342e90f8789a5b825fbe73f4bc42041c6537498a32a01980287ad32d47544` |
| CH02 | `22168ca6a6a54a2d142dcc7e1d068ca1ab7270b28a90e8e10c2a0106b595d19a` |
| CH03-a | `3b0ba1cb3ea3415ef71c5343702fd2c7ddcd44675aa8f0b4bf5e7aeab2aa80db` |
| CH03-e | `a33e27d89548e57f16e8c17b489ca971f3f992101e7664a0260954494f572aa2` |
| CH03-f | `567d566a000971890c22771cbaa9e6fee2669383f02975206013d440e4fb2347` |
| CH03-g | `59f8d76f64e95da500e86644e79a2a9e9cdec6dedd384b0cb5d1536ee1ca2e7f` |
| CH03-h | `af59933e649a92dc1b58dd679fbffad86fa999c2b6ffc36259eda227fea3f582` |
| CH03-i | `bb128e4e4ef9fba5889ee54b90268962d02162e51cb1ff9e5eb6a7e089e3c47f` |
| CH03-j | `0b2bb5079af523e3f101705704316b1092f4a536575eff11ff020bd1eaa13a20` |
| CH03-k | `51c6e87ed42d6bd341dc58a24ef11fb6baaf58bb2e93f7d4a435622382fd1ce3` |
| CH03-l | `b63bcb9f9b411fc79e36b84ddbeb7e87646e651d0ad7b410fbd3d0b9d268e81f` |
| CH03-m | `5354b6bd7903fa4c6e3e3632f6d09a304624da076f49b7fb14e1b1f3b837e2b2` |
| CH03-n | `0cace48ca710e471078de69f5da65c1a26728b7be07b65b15893158546218762` |
| CH03-o | `a531204f2ac54dda00f76f3434e6bd294fab0bb7908a12457f44a09fc1749f5c` |
| CH03-p | `6c43976354a4d2e897112ebd41b935c5a207c2f2f92ed64fa79b24040de6d42d` |
| CH04-a | `1d2bb9e3a3c66f08de6b3d8fb12d5dbad6ae0b1dcc70d395c26dd5e156e12769` |
| CH04-b | `2af41d1f927be32406737cdde4d8d4c3928cf91b7eaa062ffd9810fe6b033bbc` |
| CH04-c | `7176edd53af6853fc9e1e76e7f80204000527196dc2d96283eb6aed02870204b` |
| CH04-d | `901d6eb6474e79a4c14fd2ab096e07fc4e538d2a40c181b07c68ebf70cb2b736` |
| CH04-e | `b4c432cb115b379b300d21c826ce5ea80f10c843af2e13e8b28a2f6b60b88695` |
| CH05-a | `a6bf0cbce2d92e412ad3af4a27909e8cfeb8f15ad0d9b4913c5708eeeed34dd9` |
| CH05-b | `af89c86e7991cdd4c0bb821cd5861abc01e80c9750e6de954062088eaa37b8b9` |
| CH05-c | `dd7e5b17cd4e8e7dae2125d45d30ebdfdcbe349b1f80767c3a8442f5448e0e6d` |
| CH05-d | `67d59453a923647e7616898801e2dcc8ea1ff741d04617886411ad309344285d` |
| CH05-e | `e526f830db5a71a0a60c7c7e0a50ef0344f81f46bce4355e1a27480d6d0076cd` |
| CH00 | `d01e8ec370be9c8e50fbb293c863c95ddaf6f82af5700877bf1a57276a1f4998` |
| CH03-b | `ba62fb68b050b3840afeabec299b2aa0baac17ba2f79869c1fc031dbc195d8b5` |
| CH03-c | `20d022f2d237cf0a29e4128eae510e0cf153505a2ffd0c64ff512fed9cb06fa6` |
| CH03-d | `9444e60b0b4cb09c1efd5d03c06579af4864f7437a10555fdeca54e50687195c` |

Round 4A later changed Chapters 0, 1, 2, 3-a to 3-d and 6-a to 6-g; the identities above are those preserved when this chapter was written, and the round 4A identities are listed in the round 4A delivery manifest.

### READ-folder files not yet read whole

68 inherited pending files remain. Scoped reading receives no new whole-file credit.

- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md`
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
§1.3 no history/actions/roles/workflow in this chapter: PASS — 50 behavior cards reviewed; 0 project/workflow/advice hits. Required delivery metadata is outside behavior.
§1.4 every gap written as NOT DECIDED: PASS — 114 empty fields exactly match 114 register rows; 12 additional mechanical slots are registered.
§1.5 conflicts marked, none resolved: PASS — no new conflicting clash rule found in the mapped scope; inherited conflict and source-scope records remain in the round manifest. Accepted scoped additions are distinguished from undecided implementation.
§3 exactly one stamp per line: PASS — 50 headers, 355 populated field lines and 131 USED BY rows checked. The 1 BUILT field names the existing C-READ source; no clash implementation is stamped BUILT.
§4 every behavior line cited in the exact format: PASS — 37 distinct citations, 37 resolved inside the named pinned sections; populated fields and use rows carry citations. Source-claim review accompanies the mechanical resolution check.
§5.4 one name per thing: PASS — 50 unique current IDs, no collisions with prior cards; 457 named-card mentions checked across behavior and continuations.
§6 all template fields present, in order, for every part: PASS — 50 templates and 469 field lines checked.
§6.3 reciprocity within this chapter: PASS — 101 internal relationship occurrences checked; 25 outgoing and 10 incoming continuation rows name both ends; no missing reciprocal. Prior cards remain unchanged.
§6.4 every decided detail written in, no citation used in place of content: PASS — 19 source-to-card rows reviewed; 42 source-name literals present, no missing literal; shared atomic owners and later scopes are explicit.
§6.5 sub-parts recursed to the bottom: PASS — six types, eleven clash fields, four history fields and seven response fields carry their own templates; named gates, detection modes, recovery, downstream effects, presentation and logging are decomposed. 0 cards have all three TOGETHER fields empty.
§9 coverage matrix rows added for every file used: PASS — the carried inventory contains all 145 pinned READ-folder file paths, with current source-map additions and 17 current READ RECORD fingerprints. Shared-package scope remains partial where stated.
§10.11 no recommendation, no sentence addressed to Ness: PASS — all 50 behavior cards reviewed; no recommendation or addressed instruction.
Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_PACKAGE_COMPLETE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`; `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_2026-09-24_v0_1_CANDIDATE.md`.

### Computed self-check results

The full-file validator returned zero errors. These are writer checks, not an independent audit or adoption. The misfiled-box inventory was reviewed against all other fields and the stated source; it does not equate a prerequisite with an invented runtime refusal.

| Check | Count |
|---|---|
| cards | 50 |
| field_lines | 469 |
| used_by_rows | 131 |
| empty_fields | 114 |
| internal_relationships | 101 |
| external_relationships | 25 |
| distinct_citations | 37 |
| resolved_citations | 37 |
| named_card_mentions_checked | 457 |
| misfiled_box_fields_scanned | 469 |
| restriction_failure_gate_slots_reviewed | 154 |
| registered_empty_fields | 114 |
| cross_piece_continuations_checked | 25 |
| covered_read_file_paths | 145 |
| read_fingerprints_checked | 17 |
| source_names_checked | 42 |
| built_field_lines | 1 |
| behavior_workflow_hits | 0 |
| plain_gates_justified | 3 |
| empty_together_cards | 0 |
| formula_hits | 0 |
| wording_hits | 0 |
| source_names_missing | 0 |
| errors | 0 |
| outgoing_continuations | 25 |
| incoming_continuations | 10 |
| additional_gaps | 12 |
| pending_source_paths | 68 |
| source_map_rows | 19 |
| read_record_rows | 17 |

The recount after this block was appended matched every reported metric; no validator error remained.
