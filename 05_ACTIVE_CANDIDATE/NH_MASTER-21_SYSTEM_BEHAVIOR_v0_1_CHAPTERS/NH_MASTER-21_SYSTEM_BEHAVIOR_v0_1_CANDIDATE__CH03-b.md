# Chapter 3-b — Group A: C-READ, record and write foundation

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-b.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `855459fc6674dfe3a1f310f3d1690a9e7db59405`

This Chapter 3 piece covers the v1 reading record, shape validator, writer, quarantine destination, production-authorization boundary, operation records, restored bootstrap-reading rules and read-only memory-health checks. It also carries the restored optional content-hash distinction and interpretation-integrity constraint. The accepted telling-identity and promotion/evaluation packages remain for subsequent pieces; this file does not claim that all of C-READ or Group A is complete.

Authority order: V10 → Decision Defaults v2_2 → cursorrules → Companion v1. The Working Map is subordinate. BUILT marks only capabilities identified as built by V10’s status table. It is a source-status claim, not a fresh examination of the N.H machine. DECIDED-2026-09-25 marks restored decision content, not implementation.

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Every citation resolves at the pinned commit.

Record-member templates describe stored values, not separate runtime services. Their Fed by/USED BY pairs describe membership in the containing representation. Procedure links describe actual operations; Gated by is reserved for stated constraints. Existing canonical IDs for the stored mode object, its two members, pointer-shown why and the common helper remain unchanged. An unspecified JSON form is not supplied by an example or inferred from a different record.

<!-- BEGIN CHAPTER 3-b BEHAVIOR -->

### C-READ — Reading record, validator, writer (§6B)
Stamp: BUILT    Source: [V10 §6B / READING record schema] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]

ALONE
- What it is: BUILT — The reading-shaped record, `_validate_reading()` and `append_reading()` in `nh_accretive_store.py`, with a separate quarantine destination. [V10 §6B / READING record schema] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Takes in: BUILT — A 12-field reading, references to roots, an operation identity, and a destination path. [V10 §6B / READING record schema] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Does: BUILT — Checks shape, verifies referenced roots, checks committed operation keys, and appends the reading atomically to the supplied readings path. [V10 §6B / READING record schema] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Does: DESIGNED — Interpretation stays revisable; a reread adds a separate reading without overwriting the earlier reading. [V10 §6B / READING record schema] [V10 §7H]
- Gives out: BUILT — A reading beside the roots; the built engines’ output is in `.nh_readings_quarantine.jsonl`. [V10 §6B / READING record schema] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Must never: BUILT — Treat a structurally valid uncertain reading as malformed merely because it is uncertain. [V10 §6B / READING record schema] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Must never: DESIGNED — Copy root text into the reading, blend confidence into a single number, or insert the placeholder string `"unknown"` into optional story fields. [V10 §6A / SCHEMA CONSTRAINTS] [V10 §6B / READING record schema]
- Must never: DESIGNED — Create the production readings store or write production output merely because a path argument selects it; the separate production protections still apply. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Fails closed by: BUILT — Refuses malformed records, nonexistent referenced roots, and already-committed operation keys before append. [V10 §6B / READING record schema] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]

TOGETHER
- Fed by: BUILT — C-STORE — Accretive store & sealed roots (§6B): supplies the roots addressed by `reads`; each ID must exist before commit. [V10 §6A / SCHEMA CONSTRAINTS] [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-7B.2.8.4 — Stored mode object: supplies `mode = {label, classification_confidence}`; `label` is open and confidence is local. [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-7B.2.8.4.1 — label: supplies the open register word, including `chat`, `composed`, `story`, `question` as examples, never a closed menu. [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-7B.2.8.4.2 — classification_confidence: supplies local confidence in naming the register, distinct from top-level reading confidence. [V10 §6B / READING record schema]
- Fed by: BUILT — C-ENGINE-AB — Engines A & B (§7C, §16): supplies reading material to the validated reading write boundary. [V10 §5] [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K): supplies reading material to the validated reading write boundary. [MAP C-ENGINE-C] [V10 §7G]
- Fed by: DESIGNED — C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): supplies reading material to the validated reading write boundary. [MAP C-7G] [V10 §7G]
- Fed by: DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): supplies reading material to the validated reading write boundary. [MAP C-7GA] [V10 §7G]
- Fed by: DESIGNED — C-7H — Reread Lifecycle (§7H): supplies reading material to the validated reading write boundary. [V10 §7H]
- Fed by: DESIGNED — C-READ.1 — Twelve-field reading representation v1: supplies the twelve-field reading representation. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Fed by: BUILT — C-READ.3 — append_reading: supplies the committed reading or refusal from the shared boundary. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Fed by: BUILT — C-READ.4 — Quarantine readings destination: holds the built engines’ preserved test readings. [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B]
- Fed by: DESIGNED — C-READ.6 — Reading operation records: supplies the traceable operation record. [MAP C-READ] [V10 §0B]
- Fed by: DECIDED-2026-09-25 — C-READ.8 — Read-only memory-health checks: supplies surfaced health findings without changing memory records. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Gated by: BUILT — C-STORE.3.1 — _check_common: checks reading `id` and `timestamp` through the same shared helper used by roots. [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §5]
- Gated by: DESIGNED — C-7B.11.2 — Pointer-shown why: the why is shown through pointers; no `reason` or `why` field is added to this record. [V10 §6B]
- Gated by: BUILT — C-READ.2 — _validate_reading: schema validation is mandatory before append. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6B / READING record schema]
- Gated by: DESIGNED — C-READ.5 — Production readings authorization: production remains prohibited without both protections. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Gated by: DECIDED-2026-09-25 — C-READ.7 — Bootstrap reading context: constrains context used to produce early readings. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Gated by: DECIDED-2026-09-25 — C-READ.9 — Interpretation-integrity constraint: interpretations remain traceable and challengeable as inference grows. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-ENGINE-AB — Engines A & B (§7C, §16) | A reading to preserve beside its source roots. | Validates and appends the reading through the shared writer. | A separate reading or a refused append; roots and earlier readings remain intact. | [V10 §5] [V10 §6B / READING record schema] |
| 2 · DESIGNED | C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K), CY-A | A reading to preserve beside its source roots. | Validates and appends the reading through the shared writer. | A separate reading or a refused append; roots and earlier readings remain intact. | [MAP C-ENGINE-C] [V10 §7G] |
| 3 · DESIGNED | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G), CY-A | A reading to preserve beside its source roots. | Validates and appends the reading through the shared writer. | A separate reading or a refused append; roots and earlier readings remain intact. | [MAP C-7G] [V10 §7G] |
| 4 · DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A), CY-A | A reading to preserve beside its source roots. | Validates and appends the reading through the shared writer. | A separate reading or a refused append; roots and earlier readings remain intact. | [MAP C-7GA] [V10 §7G] |
| 5 · DESIGNED | C-7H — Reread Lifecycle (§7H), CY-F | A reading to preserve beside its source roots. | Validates and appends the reading through the shared writer. | A separate reading or a refused append; roots and earlier readings remain intact. | [V10 §7H] |
| 6 · DESIGNED | C-7A — Universal Filter (§7A), CY-A | A reading produced under the one-reader, memory-only-adds rules. | Lays the reading beside the root and preserves the original. | An added reading, never an edit of the source or earlier reading. | [V10 §7A] [MAP C-7A] |
| 7 · DESIGNED | C-7J — Clash Handling (§7J), CY-A | Readings and their root references. | Compares readings and surfaces clashes without rewriting them. | The consuming view or links; the stored reading remains unchanged. | [MAP C-READ] [V10 §7J] |
| 8 · DESIGNED | C-7K — Story Layer (§7K) | Embedded tellings and their reading/root references. | Receives tellings and organizes them without alteration. | The consuming view or links; the stored reading remains unchanged. | [MAP C-READ] [V10 §7K] |
| 9 · DESIGNED | C-7L — Person-Boxes (§7L) | Readings and their provenance. | Links readings into a Person-Box without copying or synthesizing the source. | The consuming view or links; the stored reading remains unchanged. | [MAP C-READ] [V10 §7L] |
| 10 · DESIGNED | C-7M — Computed View (§7M), CY-A | Readings, evidence, and current-use information. | Uses the readings to compute an ordered current-use view without editing history. | The consuming view or links; the stored reading remains unchanged. | [MAP C-READ] [V10 §7M] |
| 11 · DESIGNED | C-7D — Living State Web (§7D) | Grounded readings and source references. | Uses readings as grounding for the Living State Web without converting interpretations to facts. | The consuming view or links; the stored reading remains unchanged. | [MAP C-READ] [V10 §7D] |
| 12 · DESIGNED | C-7I — View Layer (§7I) | Readings in creation order and their usability status. | Shows a current view or full chronological history without deleting or overwriting readings. | The consuming view or links; the stored reading remains unchanged. | [MAP C-READ] [V10 §7I] |

SUB-PARTS: C-READ.1 — Twelve-field reading representation v1; C-READ.2 — _validate_reading; C-READ.3 — append_reading; C-READ.4 — Quarantine readings destination; C-READ.5 — Production readings authorization; C-READ.6 — Reading operation records; C-READ.7 — Bootstrap reading context; C-READ.8 — Read-only memory-health checks; C-READ.9 — Interpretation-integrity constraint

### C-READ.1 — Twelve-field reading representation v1
Stamp: DESIGNED    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: DESIGNED — The interpretation record with exactly these twelve top-level members: `id`, `reads`, `meaning`, `confidence`, `role`, `story_layer`, `mode`, `timestamp`, `produced_by`, `schema_version`, `derived_from`, `idempotency_key`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: DESIGNED — The twelve named members, including their nested values. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: DESIGNED — Preserves one immutable reading beside the roots. `reads` points to roots; `derived_from` points to prior readings; producer provenance and operation identity remain distinct. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: DESIGNED — A reading representation whose data contract is checked before append. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: DESIGNED — Copy root text; add a `reason` or `why` field; rewrite a prior reading to turn it into a new interpretation. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-READ.1.1 — reading.id: carries this member as part of the containing record. [V10 §6B / READING record schema] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Fed by: DESIGNED — C-READ.1.2 — reading.reads: carries this member as part of the containing record. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Fed by: DESIGNED — C-READ.1.3 — reading.meaning: carries this member as part of the containing record. [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-READ.1.4 — reading.confidence: carries this member as part of the containing record. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Fed by: DESIGNED — C-READ.1.5 — reading.role: carries this member as part of the containing record. [V10 §6B / READING record schema] [V10 §7K / STRUCTURED PERSPECTIVE MODEL]
- Fed by: DESIGNED — C-READ.1.6 — reading.story_layer: carries this member as part of the containing record. [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-READ.1.7 — reading.mode binding: carries this member as part of the containing record. [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-READ.1.8 — reading.timestamp: carries this member as part of the containing record. [V10 §6B / READING record schema] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Fed by: DESIGNED — C-READ.1.9 — reading.produced_by: carries this member as part of the containing record. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Fed by: DESIGNED — C-READ.1.10 — reading.schema_version: carries this member as part of the containing record. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Fed by: DESIGNED — C-READ.1.11 — reading.derived_from: carries this member as part of the containing record. [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-READ.1.12 — reading.idempotency_key: carries this member as part of the containing record. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ — Reading record, validator, writer (§6B) | The twelve reading members. | Carries the reading representation to validation and writing. | A proposed reading, not authorization to write production. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |
| 2 · BUILT | C-READ.2 — _validate_reading | The reading representation. | Checks the supplied record against its contract. | A validated record or refusal. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |
| 3 · BUILT | C-READ.3 — append_reading | The reading members. | Preserves their reading/root/provenance distinctions. | The representation supplied for append. | [V10 §6B / READING record schema] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] |

SUB-PARTS: C-READ.1.1 — reading.id; C-READ.1.2 — reading.reads; C-READ.1.3 — reading.meaning; C-READ.1.4 — reading.confidence; C-READ.1.5 — reading.role; C-READ.1.6 — reading.story_layer; C-READ.1.7 — reading.mode binding; C-READ.1.8 — reading.timestamp; C-READ.1.9 — reading.produced_by; C-READ.1.10 — reading.schema_version; C-READ.1.11 — reading.derived_from; C-READ.1.12 — reading.idempotency_key

### C-READ.1.1 — reading.id
Stamp: DESIGNED    Source: [V10 §6B / READING record schema] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]

ALONE
- What it is: DESIGNED — The reading.id member or named content item carried within Twelve-field reading representation v1. [V10 §6B / READING record schema] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Takes in: DESIGNED — Required reading identity. [V10 §6B / READING record schema] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Does: DESIGNED — Identifies the reading record; the operation identity is separate in `idempotency_key`. Shared common validation checks this member. [V10 §6B / READING record schema] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Gives out: DESIGNED — Required reading identity. [V10 §6B / READING record schema] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Must never: DESIGNED — Omit the required member. [V10 §6B / READING record schema] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1 — Twelve-field reading representation v1 | Required reading identity. | Identifies the reading record; the operation identity is separate in `idempotency_key`. Shared common validation checks this member. | Required reading identity. | [V10 §6B / READING record schema] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] |

SUB-PARTS: NONE

### C-READ.1.2 — reading.reads
Stamp: DESIGNED    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: DESIGNED — The reading.reads member or named content item carried within Twelve-field reading representation v1. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: DESIGNED — Required, non-empty list of root IDs. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: DESIGNED — Points to source roots instead of copying their text. Every referenced root must exist in the sealed store before commit. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: DESIGNED — Required, non-empty list of root IDs. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: DESIGNED — Use an empty list or invent a root reference. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1 — Twelve-field reading representation v1 | Required, non-empty list of root IDs. | Points to source roots instead of copying their text. Every referenced root must exist in the sealed store before commit. | Required, non-empty list of root IDs. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.1.3 — reading.meaning
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — The reading.meaning member or named content item carried within Twelve-field reading representation v1. [V10 §6B / READING record schema]
- Takes in: DESIGNED — Required string. [V10 §6B / READING record schema]
- Does: DESIGNED — Carries the interpretation. An honest insufficient-context meaning is valid; inability to interpret is recorded honestly and remains revisable. [V10 §6B / READING record schema]
- Gives out: DESIGNED — Required string. [V10 §6B / READING record schema]
- Must never: DESIGNED — Treat honest inability to interpret as an absent or invalid meaning solely because it is uncertain. [V10 §6B / READING record schema]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1 — Twelve-field reading representation v1 | Required string. | Carries the interpretation. An honest insufficient-context meaning is valid; inability to interpret is recorded honestly and remains revisable. | Required string. | [V10 §6B / READING record schema] |

SUB-PARTS: NONE

### C-READ.1.4 — reading.confidence
Stamp: DESIGNED    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: DESIGNED — The reading.confidence member or named content item carried within Twelve-field reading representation v1. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: DESIGNED — Required two-slot object `{interpretation_confidence, source_reliability}`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: DESIGNED — Keeps interpretation confidence and source reliability separate; both keys exist on every reading. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: DESIGNED — Required two-slot object `{interpretation_confidence, source_reliability}`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: DESIGNED — Replace the object with one blended score. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-READ.1.4.1 — reading.confidence.interpretation_confidence: carries this member as part of the containing record. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Fed by: DESIGNED — C-READ.1.4.2 — reading.confidence.source_reliability: carries this member as part of the containing record. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: DESIGNED — C-READ.1.4.3 — No copied-error confidence growth: Does not increase confidence because the error was repeated. [V10 §6B / READING record schema]
- Gated by: DESIGNED — C-READ.1.4.4 — No confidence inheritance: Does not silently copy the earlier confidence into the new reading. [V10 §6B / READING record schema]
- Gated by: DESIGNED — C-READ.1.4.5 — Confidence dimensions remain separate: Keeps `story_layer[].firmness` within the telling; computes retrieval relevance at search time and never stores it as reading confidence; keeps `mode.classification_confidence` local. [V10 §6B / READING record schema]
- Gated by: DESIGNED — C-READ.1.4.6 — Confidence is not acceptance authority: Does not accept a reading solely because the model claims certainty; grounding and explicit evidence govern acceptance. [V10 §7G]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1 — Twelve-field reading representation v1 | Required two-slot object `{interpretation_confidence, source_reliability}`. | Keeps interpretation confidence and source reliability separate; both keys exist on every reading. | Required two-slot object `{interpretation_confidence, source_reliability}`. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: C-READ.1.4.1 — reading.confidence.interpretation_confidence; C-READ.1.4.2 — reading.confidence.source_reliability; C-READ.1.4.3 — No copied-error confidence growth; C-READ.1.4.4 — No confidence inheritance; C-READ.1.4.5 — Confidence dimensions remain separate; C-READ.1.4.6 — Confidence is not acceptance authority

### C-READ.1.4.1 — reading.confidence.interpretation_confidence
Stamp: DESIGNED    Source: [V10 §6B / READING record schema] [DD §3A. The reading record]

ALONE
- What it is: DESIGNED — The reading.confidence.interpretation_confidence member or named content item carried within reading.confidence. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Takes in: DESIGNED — Required, filled value; value-form deliberately loose. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Does: DESIGNED — Expresses how sure the engine is of this reading. Presence/non-emptiness is checked without choosing a numeric scale. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Gives out: DESIGNED — Required, filled value; value-form deliberately loose. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Must never: DESIGNED — Omit the required member. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.4 — reading.confidence | Required, filled value; value-form deliberately loose. | Expresses how sure the engine is of this reading. Presence/non-emptiness is checked without choosing a numeric scale. | Required, filled value; value-form deliberately loose. | [V10 §6B / READING record schema] [DD §3A. The reading record] |

SUB-PARTS: NONE

### C-READ.1.4.2 — reading.confidence.source_reliability
Stamp: DESIGNED    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: DESIGNED — The reading.confidence.source_reliability member or named content item carried within reading.confidence. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: DESIGNED — Required key from the first reading. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: DESIGNED — Expresses how trustworthy the source was. The value representation when that is not yet knowable is unverified; no sentinel is selected. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: DESIGNED — Required key from the first reading. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: DESIGNED — Invent null, an empty string, `"unknown"`, an empty object, or another sentinel as the unverified not-yet-knowable representation. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.4 — reading.confidence | Required key from the first reading. | Expresses how trustworthy the source was. The value representation when that is not yet knowable is unverified; no sentinel is selected. | Required key from the first reading. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.1.4.3 — No copied-error confidence growth
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — Does not increase confidence because the error was repeated. [V10 §6B / READING record schema]
- Takes in: DESIGNED — Readings that repeat an earlier error. [V10 §6B / READING record schema]
- Does: DESIGNED — Does not increase confidence because the error was repeated. [V10 §6B / READING record schema]
- Gives out: DESIGNED — Repetition supplies no confidence increase. [V10 §6B / READING record schema]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.4 — reading.confidence | Readings that repeat an earlier error. | Does not increase confidence because the error was repeated. | Repetition supplies no confidence increase. | [V10 §6B / READING record schema] |

SUB-PARTS: NONE

### C-READ.1.4.4 — No confidence inheritance
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — Does not silently copy the earlier confidence into the new reading. [V10 §6B / READING record schema]
- Takes in: DESIGNED — An earlier reading and a new reading. [V10 §6B / READING record schema]
- Does: DESIGNED — Does not silently copy the earlier confidence into the new reading. [V10 §6B / READING record schema]
- Gives out: DESIGNED — Each reading retains its own confidence assessment. [V10 §6B / READING record schema]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.4 — reading.confidence | An earlier reading and a new reading. | Does not silently copy the earlier confidence into the new reading. | Each reading retains its own confidence assessment. | [V10 §6B / READING record schema] |

SUB-PARTS: NONE

### C-READ.1.4.5 — Confidence dimensions remain separate
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — Keeps `story_layer[].firmness` within the telling; computes retrieval relevance at search time and never stores it as reading confidence; keeps `mode.classification_confidence` local. [V10 §6B / READING record schema]
- Takes in: DESIGNED — Reading confidence, story firmness, retrieval relevance and local mode confidence. [V10 §6B / READING record schema]
- Does: DESIGNED — Keeps `story_layer[].firmness` within the telling; computes retrieval relevance at search time and never stores it as reading confidence; keeps `mode.classification_confidence` local. [V10 §6B / READING record schema]
- Gives out: DESIGNED — Distinct dimensions, without a blended confidence number. [V10 §6B / READING record schema]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.4 — reading.confidence | Reading confidence, story firmness, retrieval relevance and local mode confidence. | Keeps `story_layer[].firmness` within the telling; computes retrieval relevance at search time and never stores it as reading confidence; keeps `mode.classification_confidence` local. | Distinct dimensions, without a blended confidence number. | [V10 §6B / READING record schema] |

SUB-PARTS: NONE

### C-READ.1.4.6 — Confidence is not acceptance authority
Stamp: DESIGNED    Source: [V10 §7G]

ALONE
- What it is: DESIGNED — Does not accept a reading solely because the model claims certainty; grounding and explicit evidence govern acceptance. [V10 §7G]
- Takes in: DESIGNED — A model’s confidence claim. [V10 §7G]
- Does: DESIGNED — Does not accept a reading solely because the model claims certainty; grounding and explicit evidence govern acceptance. [V10 §7G]
- Gives out: DESIGNED — Model confidence remains metadata. [V10 §7G]
- Must never: DESIGNED — Use model confidence as an independent truth or acceptance authority. [V10 §7G]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.4 — reading.confidence | A model’s confidence claim. | Does not accept a reading solely because the model claims certainty; grounding and explicit evidence govern acceptance. | Model confidence remains metadata. | [V10 §7G] |

SUB-PARTS: NONE

### C-READ.1.5 — reading.role
Stamp: DESIGNED    Source: [V10 §6B / READING record schema] [V10 §7K / STRUCTURED PERSPECTIVE MODEL]

ALONE
- What it is: DESIGNED — The reading.role member or named content item carried within Twelve-field reading representation v1. [V10 §6B / READING record schema] [V10 §7K / STRUCTURED PERSPECTIVE MODEL]
- Takes in: DESIGNED — Required source-carried speaker attribution. [V10 §6B / READING record schema] [V10 §7K / STRUCTURED PERSPECTIVE MODEL]
- Does: DESIGNED — Carries who spoke from the root. This is not the person whose perspective a telling represents. [V10 §6B / READING record schema] [V10 §7K / STRUCTURED PERSPECTIVE MODEL]
- Gives out: DESIGNED — Required source-carried speaker attribution. [V10 §6B / READING record schema] [V10 §7K / STRUCTURED PERSPECTIVE MODEL]
- Must never: DESIGNED — Assume that speaker, subject and perspective owner are the same person. [V10 §6B / READING record schema] [V10 §7K / STRUCTURED PERSPECTIVE MODEL]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1 — Twelve-field reading representation v1 | Required source-carried speaker attribution. | Carries who spoke from the root. This is not the person whose perspective a telling represents. | Required source-carried speaker attribution. | [V10 §6B / READING record schema] [V10 §7K / STRUCTURED PERSPECTIVE MODEL] |

SUB-PARTS: NONE

### C-READ.1.6 — reading.story_layer
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — The reading.story_layer member or named content item carried within Twelve-field reading representation v1. [V10 §6B / READING record schema]
- Takes in: DESIGNED — Required list of embedded tellings; `[]` is valid. [V10 §6B / READING record schema]
- Does: DESIGNED — Keeps tellings alongside one another, including conflict. The six v1 optional members are `whose`, `stance`, `firmness`, `telling`, `theme`, `when`. Unknown optional values are omitted. [V10 §6B / READING record schema]
- Gives out: DESIGNED — Required list of embedded tellings; `[]` is valid. [V10 §6B / READING record schema]
- Must never: DESIGNED — Pick a winning telling, merge conflicting tellings, or fill an unknown optional member with `"unknown"`. [V10 §6B / READING record schema]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-READ.1.6.1 — reading.story_layer[].whose: carries this member as part of the containing record. [V10 §6B / READING record schema] [V10 §7K]
- Fed by: DESIGNED — C-READ.1.6.2 — reading.story_layer[].stance: carries this member as part of the containing record. [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-READ.1.6.3 — reading.story_layer[].firmness: carries this member as part of the containing record. [V10 §6B / READING record schema] [V10 §7K]
- Fed by: DESIGNED — C-READ.1.6.4 — reading.story_layer[].telling: carries this member as part of the containing record. [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-READ.1.6.5 — reading.story_layer[].theme: carries this member as part of the containing record. [V10 §6B / READING record schema] [V10 §7K]
- Fed by: DESIGNED — C-READ.1.6.6 — reading.story_layer[].when: carries this member as part of the containing record. [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-READ.1.6.7 — Empty story_layer: Keeps `story_layer=[]` valid. [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-READ.1.6.8 — Embedded v1 telling boundary: Keeps the telling embedded in its immutable parent reading; the v1 built schema does not establish a standalone first-class telling store. [V10 §7K / OBJECT-IDENTITY SEAM — EXPLICITLY UNRESOLVED]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1 — Twelve-field reading representation v1 | Required list of embedded tellings; `[]` is valid. | Keeps tellings alongside one another, including conflict. The six v1 optional members are `whose`, `stance`, `firmness`, `telling`, `theme`, `when`. Unknown optional values are omitted. | Required list of embedded tellings; `[]` is valid. | [V10 §6B / READING record schema] |

SUB-PARTS: C-READ.1.6.1 — reading.story_layer[].whose; C-READ.1.6.2 — reading.story_layer[].stance; C-READ.1.6.3 — reading.story_layer[].firmness; C-READ.1.6.4 — reading.story_layer[].telling; C-READ.1.6.5 — reading.story_layer[].theme; C-READ.1.6.6 — reading.story_layer[].when; C-READ.1.6.7 — Empty story_layer; C-READ.1.6.8 — Embedded v1 telling boundary

### C-READ.1.6.1 — reading.story_layer[].whose
Stamp: DESIGNED    Source: [V10 §6B / READING record schema] [V10 §7K]

ALONE
- What it is: DESIGNED — The reading.story_layer[].whose member or named content item carried within reading.story_layer. [V10 §6B / READING record schema] [V10 §7K]
- Takes in: DESIGNED — Optional member; omitted when unknown. [V10 §6B / READING record schema] [V10 §7K]
- Does: DESIGNED — Carries the telling’s perspective attribution; this is separate from the reading’s source speaker in `role`. [V10 §6B / READING record schema] [V10 §7K]
- Gives out: DESIGNED — Optional member; omitted when unknown. [V10 §6B / READING record schema] [V10 §7K]
- Must never: DESIGNED — Substitute `"unknown"` for an omitted unknown value. [V10 §6B / READING record schema] [V10 §7K]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.6 — reading.story_layer | Optional member; omitted when unknown. | Carries the telling’s perspective attribution; this is separate from the reading’s source speaker in `role`. | Optional member; omitted when unknown. | [V10 §6B / READING record schema] [V10 §7K] |

SUB-PARTS: NONE

### C-READ.1.6.2 — reading.story_layer[].stance
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — The reading.story_layer[].stance member or named content item carried within reading.story_layer. [V10 §6B / READING record schema]
- Takes in: DESIGNED — Optional member; omitted when unknown. [V10 §6B / READING record schema]
- Does: DESIGNED — Carries the stance in the telling when supported. [V10 §6B / READING record schema]
- Gives out: DESIGNED — Optional member; omitted when unknown. [V10 §6B / READING record schema]
- Must never: DESIGNED — Substitute `"unknown"` for an omitted unknown value. [V10 §6B / READING record schema]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.6 — reading.story_layer | Optional member; omitted when unknown. | Carries the stance in the telling when supported. | Optional member; omitted when unknown. | [V10 §6B / READING record schema] |

SUB-PARTS: NONE

### C-READ.1.6.3 — reading.story_layer[].firmness
Stamp: DESIGNED    Source: [V10 §6B / READING record schema] [V10 §7K]

ALONE
- What it is: DESIGNED — The reading.story_layer[].firmness member or named content item carried within reading.story_layer. [V10 §6B / READING record schema] [V10 §7K]
- Takes in: DESIGNED — Optional member; omitted when unknown. [V10 §6B / READING record schema] [V10 §7K]
- Does: DESIGNED — Carries how strongly the perspective owner appears to hold the stance; this is separate from the engine’s confidence in its interpretation. [V10 §6B / READING record schema] [V10 §7K]
- Gives out: DESIGNED — Optional member; omitted when unknown. [V10 §6B / READING record schema] [V10 §7K]
- Must never: DESIGNED — Substitute `"unknown"` for an omitted unknown value. [V10 §6B / READING record schema] [V10 §7K]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.6 — reading.story_layer | Optional member; omitted when unknown. | Carries how strongly the perspective owner appears to hold the stance; this is separate from the engine’s confidence in its interpretation. | Optional member; omitted when unknown. | [V10 §6B / READING record schema] [V10 §7K] |

SUB-PARTS: NONE

### C-READ.1.6.4 — reading.story_layer[].telling
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — The reading.story_layer[].telling member or named content item carried within reading.story_layer. [V10 §6B / READING record schema]
- Takes in: DESIGNED — Optional member; omitted when unknown. [V10 §6B / READING record schema]
- Does: DESIGNED — Carries the telling inside its parent reading’s list. [V10 §6B / READING record schema]
- Gives out: DESIGNED — Optional member; omitted when unknown. [V10 §6B / READING record schema]
- Must never: DESIGNED — Substitute `"unknown"` for an omitted unknown value. [V10 §6B / READING record schema]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.6 — reading.story_layer | Optional member; omitted when unknown. | Carries the telling inside its parent reading’s list. | Optional member; omitted when unknown. | [V10 §6B / READING record schema] |

SUB-PARTS: NONE

### C-READ.1.6.5 — reading.story_layer[].theme
Stamp: DESIGNED    Source: [V10 §6B / READING record schema] [V10 §7K]

ALONE
- What it is: DESIGNED — The reading.story_layer[].theme member or named content item carried within reading.story_layer. [V10 §6B / READING record schema] [V10 §7K]
- Takes in: DESIGNED — Optional member; omitted when unknown. [V10 §6B / READING record schema] [V10 §7K]
- Does: DESIGNED — Carries theme membership when present; the Story Layer keeps navigation categories separate from facts. [V10 §6B / READING record schema] [V10 §7K]
- Gives out: DESIGNED — Optional member; omitted when unknown. [V10 §6B / READING record schema] [V10 §7K]
- Must never: DESIGNED — Substitute `"unknown"` for an omitted unknown value. [V10 §6B / READING record schema] [V10 §7K]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.6 — reading.story_layer | Optional member; omitted when unknown. | Carries theme membership when present; the Story Layer keeps navigation categories separate from facts. | Optional member; omitted when unknown. | [V10 §6B / READING record schema] [V10 §7K] |

SUB-PARTS: NONE

### C-READ.1.6.6 — reading.story_layer[].when
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — The reading.story_layer[].when member or named content item carried within reading.story_layer. [V10 §6B / READING record schema]
- Takes in: DESIGNED — Optional member; omitted when unknown. [V10 §6B / READING record schema]
- Does: DESIGNED — Carries the telling’s temporal member when known; it is distinct from the reading’s creation timestamp. [V10 §6B / READING record schema]
- Gives out: DESIGNED — Optional member; omitted when unknown. [V10 §6B / READING record schema]
- Must never: DESIGNED — Substitute `"unknown"` for an omitted unknown value. [V10 §6B / READING record schema]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.6 — reading.story_layer | Optional member; omitted when unknown. | Carries the telling’s temporal member when known; it is distinct from the reading’s creation timestamp. | Optional member; omitted when unknown. | [V10 §6B / READING record schema] |

SUB-PARTS: NONE

### C-READ.1.6.7 — Empty story_layer
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — Keeps `story_layer=[]` valid. [V10 §6B / READING record schema]
- Takes in: DESIGNED — A reading with no supported telling. [V10 §6B / READING record schema]
- Does: DESIGNED — Keeps `story_layer=[]` valid. [V10 §6B / READING record schema]
- Gives out: DESIGNED — The reading remains structurally writable. [V10 §6B / READING record schema]
- Must never: DESIGNED — Reject the reading solely because the list is empty. [V10 §6B / READING record schema]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.6 — reading.story_layer | A reading with no supported telling. | Keeps `story_layer=[]` valid. | The reading remains structurally writable. | [V10 §6B / READING record schema] |

SUB-PARTS: NONE

### C-READ.1.6.8 — Embedded v1 telling boundary
Stamp: DESIGNED    Source: [V10 §7K / OBJECT-IDENTITY SEAM — EXPLICITLY UNRESOLVED]

ALONE
- What it is: DESIGNED — Keeps the telling embedded in its immutable parent reading; the v1 built schema does not establish a standalone first-class telling store. [V10 §7K / OBJECT-IDENTITY SEAM — EXPLICITLY UNRESOLVED]
- Takes in: DESIGNED — An entry in the v1 `story_layer` list. [V10 §7K / OBJECT-IDENTITY SEAM — EXPLICITLY UNRESOLVED]
- Does: DESIGNED — Keeps the telling embedded in its immutable parent reading; the v1 built schema does not establish a standalone first-class telling store. [V10 §7K / OBJECT-IDENTITY SEAM — EXPLICITLY UNRESOLVED]
- Gives out: DESIGNED — An embedded telling in the parent reading. [V10 §7K / OBJECT-IDENTITY SEAM — EXPLICITLY UNRESOLVED]
- Must never: DESIGNED — Claim that standalone telling storage is built. [V10 §7K / OBJECT-IDENTITY SEAM — EXPLICITLY UNRESOLVED]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.6 — reading.story_layer | An entry in the v1 `story_layer` list. | Keeps the telling embedded in its immutable parent reading; the v1 built schema does not establish a standalone first-class telling store. | An embedded telling in the parent reading. | [V10 §7K / OBJECT-IDENTITY SEAM — EXPLICITLY UNRESOLVED] |

SUB-PARTS: NONE

### C-READ.1.7 — reading.mode binding
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — The reading.mode binding member or named content item carried within Twelve-field reading representation v1. [V10 §6B / READING record schema]
- Takes in: DESIGNED — Required object `{label, classification_confidence}`. [V10 §6B / READING record schema]
- Does: DESIGNED — Carries the existing Stored mode object without changing its open register vocabulary or local confidence semantics. [V10 §6B / READING record schema]
- Does: DESIGNED — `label` is an open word with examples `chat`, `composed`, `story`, `question`; `classification_confidence` is local confidence in that label, never top-level reading confidence. [V10 §6B / READING record schema]
- Gives out: DESIGNED — Required object `{label, classification_confidence}`. [V10 §6B / READING record schema]
- Must never: DESIGNED — Treat the open register label as the closed retrieval-mode vocabulary `bare`, `local-context`, `associative`, `combined`. [V10 §6B / READING record schema]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1 — Twelve-field reading representation v1 | Required object `{label, classification_confidence}`. | Carries the existing Stored mode object without changing its open register vocabulary or local confidence semantics. | Required object `{label, classification_confidence}`. | [V10 §6B / READING record schema] |

SUB-PARTS: NONE

### C-READ.1.8 — reading.timestamp
Stamp: DESIGNED    Source: [V10 §6B / READING record schema] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]

ALONE
- What it is: DESIGNED — The reading.timestamp member or named content item carried within Twelve-field reading representation v1. [V10 §6B / READING record schema] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Takes in: DESIGNED — Required creation timestamp. [V10 §6B / READING record schema] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Does: DESIGNED — Records when this reading was created, not source time, event time or ingest time; shared `_check_common` validation checks it. [V10 §6B / READING record schema] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Gives out: DESIGNED — Required creation timestamp. [V10 §6B / READING record schema] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Must never: DESIGNED — Omit the required member. [V10 §6B / READING record schema] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1 — Twelve-field reading representation v1 | Required creation timestamp. | Records when this reading was created, not source time, event time or ingest time; shared `_check_common` validation checks it. | Required creation timestamp. | [V10 §6B / READING record schema] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] |

SUB-PARTS: NONE

### C-READ.1.9 — reading.produced_by
Stamp: DESIGNED    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: DESIGNED — The reading.produced_by member or named content item carried within Twelve-field reading representation v1. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: DESIGNED — Required reproducibility-grade producer provenance. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: DESIGNED — Requires `origin`. Engine readings carry model, digest, engine_version, prompt_version, config and retrieval_inputs; human annotations carry annotator, when, context_version and change_reason. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: DESIGNED — The source’s abbreviated names `digest` and `when` are preserved here as provenance member labels; they do not select an unverified runtime key spelling. [V10 §6B / READING record schema]
- Gives out: DESIGNED — Required reproducibility-grade producer provenance. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: DESIGNED — Omit the required member. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-READ.1.9.1 — reading.produced_by.origin: carries this member as part of the containing record. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Fed by: DESIGNED — C-READ.1.9.2 — reading.produced_by.model: carries this member as part of the containing record. [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-READ.1.9.3 — reading.produced_by.digest: carries this member as part of the containing record. [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-READ.1.9.4 — reading.produced_by.engine_version: carries this member as part of the containing record. [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-READ.1.9.5 — reading.produced_by.prompt_version: carries this member as part of the containing record. [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-READ.1.9.6 — reading.produced_by.config: carries this member as part of the containing record. [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-READ.1.9.7 — reading.produced_by.retrieval_inputs: carries this member as part of the containing record. [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-READ.1.9.8 — human_annotation.annotator: carries this member as part of the containing record. [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-READ.1.9.9 — human_annotation.when: carries this member as part of the containing record. [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-READ.1.9.10 — human_annotation.context_version: carries this member as part of the containing record. [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-READ.1.9.11 — human_annotation.change_reason: carries this member as part of the containing record. [V10 §6B / READING record schema]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1 — Twelve-field reading representation v1 | Required reproducibility-grade producer provenance. | Requires `origin`. Engine readings carry model, digest, engine_version, prompt_version, config and retrieval_inputs; human annotations carry annotator, when, context_version and change_reason. | Required reproducibility-grade producer provenance. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: C-READ.1.9.1 — reading.produced_by.origin; C-READ.1.9.2 — reading.produced_by.model; C-READ.1.9.3 — reading.produced_by.digest; C-READ.1.9.4 — reading.produced_by.engine_version; C-READ.1.9.5 — reading.produced_by.prompt_version; C-READ.1.9.6 — reading.produced_by.config; C-READ.1.9.7 — reading.produced_by.retrieval_inputs; C-READ.1.9.8 — human_annotation.annotator; C-READ.1.9.9 — human_annotation.when; C-READ.1.9.10 — human_annotation.context_version; C-READ.1.9.11 — human_annotation.change_reason

### C-READ.1.9.1 — reading.produced_by.origin
Stamp: DESIGNED    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: DESIGNED — The reading.produced_by.origin member or named content item carried within reading.produced_by. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: DESIGNED — Required member; one of `observed`, `imported`, `simulated`, `generated`, `reaction`, `human_annotation`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: DESIGNED — Records the information-path origin using the six-member controlled vocabulary. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: DESIGNED — Required member; one of `observed`, `imported`, `simulated`, `generated`, `reaction`, `human_annotation`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: DESIGNED — Treat an allowed origin value as authorization for that material to enter ordinary memory. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-READ.1.9.1.1 — origin=observed: Allows the exact vocabulary member `observed`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Fed by: DESIGNED — C-READ.1.9.1.2 — origin=imported: Allows the exact vocabulary member `imported`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Fed by: DESIGNED — C-READ.1.9.1.3 — origin=simulated: Allows the exact vocabulary member `simulated`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Fed by: DESIGNED — C-READ.1.9.1.4 — origin=generated: Allows the exact vocabulary member `generated`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Fed by: DESIGNED — C-READ.1.9.1.5 — origin=reaction: Allows the exact vocabulary member `reaction`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Fed by: DESIGNED — C-READ.1.9.1.6 — origin=human_annotation: Allows the exact vocabulary member `human_annotation`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9 — reading.produced_by | Required member; one of `observed`, `imported`, `simulated`, `generated`, `reaction`, `human_annotation`. | Records the information-path origin using the six-member controlled vocabulary. | Required member; one of `observed`, `imported`, `simulated`, `generated`, `reaction`, `human_annotation`. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: C-READ.1.9.1.1 — origin=observed; C-READ.1.9.1.2 — origin=imported; C-READ.1.9.1.3 — origin=simulated; C-READ.1.9.1.4 — origin=generated; C-READ.1.9.1.5 — origin=reaction; C-READ.1.9.1.6 — origin=human_annotation

### C-READ.1.9.1.1 — origin=observed
Stamp: DESIGNED    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: DESIGNED — Allows the exact vocabulary member `observed`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: DESIGNED — The `origin` member. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: DESIGNED — Allows the exact vocabulary member `observed`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: DESIGNED — `origin="observed"` as provenance, not a trust grant. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9.1 — reading.produced_by.origin | The `origin` member. | Allows the exact vocabulary member `observed`. | `origin="observed"` as provenance, not a trust grant. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.1.9.1.2 — origin=imported
Stamp: DESIGNED    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: DESIGNED — Allows the exact vocabulary member `imported`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: DESIGNED — The `origin` member. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: DESIGNED — Allows the exact vocabulary member `imported`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: DESIGNED — `origin="imported"` as provenance, not a trust grant. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9.1 — reading.produced_by.origin | The `origin` member. | Allows the exact vocabulary member `imported`. | `origin="imported"` as provenance, not a trust grant. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.1.9.1.3 — origin=simulated
Stamp: DESIGNED    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: DESIGNED — Allows the exact vocabulary member `simulated`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: DESIGNED — The `origin` member. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: DESIGNED — Allows the exact vocabulary member `simulated`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: DESIGNED — `origin="simulated"` as provenance, not a trust grant. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9.1 — reading.produced_by.origin | The `origin` member. | Allows the exact vocabulary member `simulated`. | `origin="simulated"` as provenance, not a trust grant. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.1.9.1.4 — origin=generated
Stamp: DESIGNED    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: DESIGNED — Allows the exact vocabulary member `generated`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: DESIGNED — The `origin` member. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: DESIGNED — Allows the exact vocabulary member `generated`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: DESIGNED — `origin="generated"` as provenance, not a trust grant. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9.1 — reading.produced_by.origin | The `origin` member. | Allows the exact vocabulary member `generated`. | `origin="generated"` as provenance, not a trust grant. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.1.9.1.5 — origin=reaction
Stamp: DESIGNED    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: DESIGNED — Allows the exact vocabulary member `reaction`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: DESIGNED — The `origin` member. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: DESIGNED — Allows the exact vocabulary member `reaction`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: DESIGNED — `origin="reaction"` as provenance, not a trust grant. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9.1 — reading.produced_by.origin | The `origin` member. | Allows the exact vocabulary member `reaction`. | `origin="reaction"` as provenance, not a trust grant. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.1.9.1.6 — origin=human_annotation
Stamp: DESIGNED    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: DESIGNED — Allows the exact vocabulary member `human_annotation`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: DESIGNED — The `origin` member. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: DESIGNED — Allows the exact vocabulary member `human_annotation`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: DESIGNED — `origin="human_annotation"` as provenance, not a trust grant. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9.1 — reading.produced_by.origin | The `origin` member. | Allows the exact vocabulary member `human_annotation`. | `origin="human_annotation"` as provenance, not a trust grant. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.1.9.2 — reading.produced_by.model
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — The reading.produced_by.model member or named content item carried within reading.produced_by. [V10 §6B / READING record schema]
- Takes in: DESIGNED — Engine provenance member. [V10 §6B / READING record schema]
- Does: DESIGNED — Carries the model identity. [V10 §6B / READING record schema]
- Gives out: DESIGNED — Engine provenance member. [V10 §6B / READING record schema]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9 — reading.produced_by | Engine provenance member. | Carries the model identity. | Engine provenance member. | [V10 §6B / READING record schema] |

SUB-PARTS: NONE

### C-READ.1.9.3 — reading.produced_by.digest
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — The reading.produced_by.digest member or named content item carried within reading.produced_by. [V10 §6B / READING record schema]
- Takes in: DESIGNED — Engine provenance member. [V10 §6B / READING record schema]
- Does: DESIGNED — Carries the producer digest; a model name alone is not the full producer provenance. [V10 §6B / READING record schema]
- Gives out: DESIGNED — Engine provenance member. [V10 §6B / READING record schema]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9 — reading.produced_by | Engine provenance member. | Carries the producer digest; a model name alone is not the full producer provenance. | Engine provenance member. | [V10 §6B / READING record schema] |

SUB-PARTS: NONE

### C-READ.1.9.4 — reading.produced_by.engine_version
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — The reading.produced_by.engine_version member or named content item carried within reading.produced_by. [V10 §6B / READING record schema]
- Takes in: DESIGNED — Engine provenance member. [V10 §6B / READING record schema]
- Does: DESIGNED — Carries the engine version that produced the reading. [V10 §6B / READING record schema]
- Gives out: DESIGNED — Engine provenance member. [V10 §6B / READING record schema]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9 — reading.produced_by | Engine provenance member. | Carries the engine version that produced the reading. | Engine provenance member. | [V10 §6B / READING record schema] |

SUB-PARTS: NONE

### C-READ.1.9.5 — reading.produced_by.prompt_version
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — The reading.produced_by.prompt_version member or named content item carried within reading.produced_by. [V10 §6B / READING record schema]
- Takes in: DESIGNED — Engine provenance member. [V10 §6B / READING record schema]
- Does: DESIGNED — Carries the prompt version that produced the reading. [V10 §6B / READING record schema]
- Gives out: DESIGNED — Engine provenance member. [V10 §6B / READING record schema]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9 — reading.produced_by | Engine provenance member. | Carries the prompt version that produced the reading. | Engine provenance member. | [V10 §6B / READING record schema] |

SUB-PARTS: NONE

### C-READ.1.9.6 — reading.produced_by.config
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — The reading.produced_by.config member or named content item carried within reading.produced_by. [V10 §6B / READING record schema]
- Takes in: DESIGNED — Engine provenance member. [V10 §6B / READING record schema]
- Does: DESIGNED — Carries the engine configuration used for this reading. [V10 §6B / READING record schema]
- Gives out: DESIGNED — Engine provenance member. [V10 §6B / READING record schema]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-READ.1.9.6.1 — produced_by.config.pass_id: carries this member as part of the containing record. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9 — reading.produced_by | Engine provenance member. | Carries the engine configuration used for this reading. | Engine provenance member. | [V10 §6B / READING record schema] |

SUB-PARTS: C-READ.1.9.6.1 — produced_by.config.pass_id

### C-READ.1.9.7 — reading.produced_by.retrieval_inputs
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — The reading.produced_by.retrieval_inputs member or named content item carried within reading.produced_by. [V10 §6B / READING record schema]
- Takes in: DESIGNED — Engine provenance member. [V10 §6B / READING record schema]
- Does: DESIGNED — Carries the retrieved inputs supplied for this reading. [V10 §6B / READING record schema]
- Gives out: DESIGNED — Engine provenance member. [V10 §6B / READING record schema]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-READ.1.9.7.1 — retrieval audit — reading mode: carries this member as part of the containing record. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Fed by: DESIGNED — C-READ.1.9.7.2 — retrieval audit — configured parameters: carries this member as part of the containing record. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Fed by: DESIGNED — C-READ.1.9.7.3 — retrieval audit — retrieval system/model/index version: carries this member as part of the containing record. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Fed by: DESIGNED — C-READ.1.9.7.4 — retrieval audit — exact roots supplied: carries this member as part of the containing record. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Fed by: DESIGNED — C-READ.1.9.7.5 — retrieval audit — scores or positions: carries this member as part of the containing record. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Fed by: DESIGNED — C-READ.1.9.7.6 — retrieval audit — exclusions or truncation caused by limits: carries this member as part of the containing record. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Fed by: DESIGNED — C-READ.1.9.7.7 — retrieval audit — execution timestamp: carries this member as part of the containing record. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Fed by: DESIGNED — C-READ.1.9.7.8 — Genuine empty-context audit: Records which channel returned nothing, why, bare fallback, and the context-limited/revisable status; proceeds from the target root only. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9 — reading.produced_by | Engine provenance member. | Carries the retrieved inputs supplied for this reading. | Engine provenance member. | [V10 §6B / READING record schema] |

SUB-PARTS: C-READ.1.9.7.1 — retrieval audit — reading mode; C-READ.1.9.7.2 — retrieval audit — configured parameters; C-READ.1.9.7.3 — retrieval audit — retrieval system/model/index version; C-READ.1.9.7.4 — retrieval audit — exact roots supplied; C-READ.1.9.7.5 — retrieval audit — scores or positions; C-READ.1.9.7.6 — retrieval audit — exclusions or truncation caused by limits; C-READ.1.9.7.7 — retrieval audit — execution timestamp; C-READ.1.9.7.8 — Genuine empty-context audit

### C-READ.1.9.8 — human_annotation.annotator
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — The human_annotation.annotator member or named content item carried within reading.produced_by. [V10 §6B / READING record schema]
- Takes in: DESIGNED — Human-annotation provenance member. [V10 §6B / READING record schema]
- Does: DESIGNED — Identifies the human annotator. [V10 §6B / READING record schema]
- Gives out: DESIGNED — Human-annotation provenance member. [V10 §6B / READING record schema]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9 — reading.produced_by | Human-annotation provenance member. | Identifies the human annotator. | Human-annotation provenance member. | [V10 §6B / READING record schema] |

SUB-PARTS: NONE

### C-READ.1.9.9 — human_annotation.when
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — The human_annotation.when member or named content item carried within reading.produced_by. [V10 §6B / READING record schema]
- Takes in: DESIGNED — Human-annotation provenance member. [V10 §6B / READING record schema]
- Does: DESIGNED — Records when the annotation was made. [V10 §6B / READING record schema]
- Gives out: DESIGNED — Human-annotation provenance member. [V10 §6B / READING record schema]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9 — reading.produced_by | Human-annotation provenance member. | Records when the annotation was made. | Human-annotation provenance member. | [V10 §6B / READING record schema] |

SUB-PARTS: NONE

### C-READ.1.9.10 — human_annotation.context_version
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — The human_annotation.context_version member or named content item carried within reading.produced_by. [V10 §6B / READING record schema]
- Takes in: DESIGNED — Human-annotation provenance member. [V10 §6B / READING record schema]
- Does: DESIGNED — Identifies the annotation’s source/context version. [V10 §6B / READING record schema]
- Gives out: DESIGNED — Human-annotation provenance member. [V10 §6B / READING record schema]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9 — reading.produced_by | Human-annotation provenance member. | Identifies the annotation’s source/context version. | Human-annotation provenance member. | [V10 §6B / READING record schema] |

SUB-PARTS: NONE

### C-READ.1.9.11 — human_annotation.change_reason
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — The human_annotation.change_reason member or named content item carried within reading.produced_by. [V10 §6B / READING record schema]
- Takes in: DESIGNED — Human-annotation provenance member. [V10 §6B / READING record schema]
- Does: DESIGNED — Records why the annotation changed between versions. [V10 §6B / READING record schema]
- Gives out: DESIGNED — Human-annotation provenance member. [V10 §6B / READING record schema]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9 — reading.produced_by | Human-annotation provenance member. | Records why the annotation changed between versions. | Human-annotation provenance member. | [V10 §6B / READING record schema] |

SUB-PARTS: NONE

### C-READ.1.9.6.1 — produced_by.config.pass_id
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]

ALONE
- What it is: DESIGNED — The produced_by.config.pass_id member or named content item carried within reading.produced_by.config. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]
- Takes in: DESIGNED — The particular pass attempt’s `pass_id`. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]
- Does: DESIGNED — Identifies the pass attempt, separately from the stable job-level reading idempotency key. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]
- Gives out: DESIGNED — The particular pass attempt’s `pass_id`. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9.6 — reading.produced_by.config | The particular pass attempt’s `pass_id`. | Identifies the pass attempt, separately from the stable job-level reading idempotency key. | The particular pass attempt’s `pass_id`. | [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] |

SUB-PARTS: NONE

### C-READ.1.9.7.1 — retrieval audit — reading mode
Stamp: DESIGNED    Source: [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]

ALONE
- What it is: DESIGNED — The retrieval audit — reading mode member or named content item carried within reading.produced_by.retrieval_inputs. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Takes in: DESIGNED — Required audit content; source prose name, not a selected new JSON key. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Does: DESIGNED — The declared reading mode used by the pass. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Gives out: DESIGNED — Required audit content; source prose name, not a selected new JSON key. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Must never: DESIGNED — Omit the required member. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9.7 — reading.produced_by.retrieval_inputs | Required audit content; source prose name, not a selected new JSON key. | The declared reading mode used by the pass. | Required audit content; source prose name, not a selected new JSON key. | [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record] |

SUB-PARTS: NONE

### C-READ.1.9.7.2 — retrieval audit — configured parameters
Stamp: DESIGNED    Source: [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]

ALONE
- What it is: DESIGNED — The retrieval audit — configured parameters member or named content item carried within reading.produced_by.retrieval_inputs. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Takes in: DESIGNED — Required audit content; source prose name, not a selected new JSON key. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Does: DESIGNED — The configured retrieval parameters used by the pass. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Gives out: DESIGNED — Required audit content; source prose name, not a selected new JSON key. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Must never: DESIGNED — Omit the required member. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9.7 — reading.produced_by.retrieval_inputs | Required audit content; source prose name, not a selected new JSON key. | The configured retrieval parameters used by the pass. | Required audit content; source prose name, not a selected new JSON key. | [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record] |

SUB-PARTS: NONE

### C-READ.1.9.7.3 — retrieval audit — retrieval system/model/index version
Stamp: DESIGNED    Source: [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]

ALONE
- What it is: DESIGNED — The retrieval audit — retrieval system/model/index version member or named content item carried within reading.produced_by.retrieval_inputs. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Takes in: DESIGNED — Required audit content; source prose name, not a selected new JSON key. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Does: DESIGNED — The retrieval system, model and index versions used. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Gives out: DESIGNED — Required audit content; source prose name, not a selected new JSON key. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Must never: DESIGNED — Omit the required member. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9.7 — reading.produced_by.retrieval_inputs | Required audit content; source prose name, not a selected new JSON key. | The retrieval system, model and index versions used. | Required audit content; source prose name, not a selected new JSON key. | [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record] |

SUB-PARTS: NONE

### C-READ.1.9.7.4 — retrieval audit — exact roots supplied
Stamp: DESIGNED    Source: [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]

ALONE
- What it is: DESIGNED — The retrieval audit — exact roots supplied member or named content item carried within reading.produced_by.retrieval_inputs. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Takes in: DESIGNED — Required audit content; source prose name, not a selected new JSON key. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Does: DESIGNED — The exact source roots supplied as context. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Gives out: DESIGNED — Required audit content; source prose name, not a selected new JSON key. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Must never: DESIGNED — Omit the required member. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9.7 — reading.produced_by.retrieval_inputs | Required audit content; source prose name, not a selected new JSON key. | The exact source roots supplied as context. | Required audit content; source prose name, not a selected new JSON key. | [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record] |

SUB-PARTS: NONE

### C-READ.1.9.7.5 — retrieval audit — scores or positions
Stamp: DESIGNED    Source: [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]

ALONE
- What it is: DESIGNED — The retrieval audit — scores or positions member or named content item carried within reading.produced_by.retrieval_inputs. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Takes in: DESIGNED — Required audit content; source prose name, not a selected new JSON key. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Does: DESIGNED — The retrieval scores or positions, as applicable. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Gives out: DESIGNED — Required audit content; source prose name, not a selected new JSON key. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Must never: DESIGNED — Omit the required member. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9.7 — reading.produced_by.retrieval_inputs | Required audit content; source prose name, not a selected new JSON key. | The retrieval scores or positions, as applicable. | Required audit content; source prose name, not a selected new JSON key. | [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record] |

SUB-PARTS: NONE

### C-READ.1.9.7.6 — retrieval audit — exclusions or truncation caused by limits
Stamp: DESIGNED    Source: [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]

ALONE
- What it is: DESIGNED — The retrieval audit — exclusions or truncation caused by limits member or named content item carried within reading.produced_by.retrieval_inputs. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Takes in: DESIGNED — Required audit content; source prose name, not a selected new JSON key. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Does: DESIGNED — What configured limits excluded or truncated. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Gives out: DESIGNED — Required audit content; source prose name, not a selected new JSON key. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Must never: DESIGNED — Omit the required member. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9.7 — reading.produced_by.retrieval_inputs | Required audit content; source prose name, not a selected new JSON key. | What configured limits excluded or truncated. | Required audit content; source prose name, not a selected new JSON key. | [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record] |

SUB-PARTS: NONE

### C-READ.1.9.7.7 — retrieval audit — execution timestamp
Stamp: DESIGNED    Source: [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]

ALONE
- What it is: DESIGNED — The retrieval audit — execution timestamp member or named content item carried within reading.produced_by.retrieval_inputs. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Takes in: DESIGNED — Required audit content; source prose name, not a selected new JSON key. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Does: DESIGNED — When retrieval executed. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Gives out: DESIGNED — Required audit content; source prose name, not a selected new JSON key. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Must never: DESIGNED — Omit the required member. [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9.7 — reading.produced_by.retrieval_inputs | Required audit content; source prose name, not a selected new JSON key. | When retrieval executed. | Required audit content; source prose name, not a selected new JSON key. | [V10 §7F / AUDIT TRAIL] [V10 §7G-A / Step 5 — Write the reading record] |

SUB-PARTS: NONE

### C-READ.1.9.7.8 — Genuine empty-context audit
Stamp: DESIGNED    Source: [V10 §7F / GENUINE NO-CONTEXT HANDLING]

ALONE
- What it is: DESIGNED — Records which channel returned nothing, why, bare fallback, and the context-limited/revisable status; proceeds from the target root only. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Takes in: DESIGNED — A channel with no relevant context: a first root in its thread or no semantic results above threshold. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Does: DESIGNED — Records which channel returned nothing, why, bare fallback, and the context-limited/revisable status; proceeds from the target root only. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Gives out: DESIGNED — An honest no-context reading audit. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Must never: DESIGNED — Invent context, lower thresholds silently, substitute unrelated memories, or label retrieval failure as successful empty retrieval. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-READ.1.9.7.8.1 — Empty-context audit — empty channel: carries this member as part of the containing record. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Fed by: DESIGNED — C-READ.1.9.7.8.2 — Empty-context audit — empty-result reason: carries this member as part of the containing record. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Fed by: DESIGNED — C-READ.1.9.7.8.3 — Empty-context audit — bare fallback used: carries this member as part of the containing record. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Fed by: DESIGNED — C-READ.1.9.7.8.4 — Empty-context audit — context-limited and revisable: carries this member as part of the containing record. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9.7 — reading.produced_by.retrieval_inputs | A channel with no relevant context: a first root in its thread or no semantic results above threshold. | Records which channel returned nothing, why, bare fallback, and the context-limited/revisable status; proceeds from the target root only. | An honest no-context reading audit. | [V10 §7F / GENUINE NO-CONTEXT HANDLING] |

SUB-PARTS: C-READ.1.9.7.8.1 — Empty-context audit — empty channel; C-READ.1.9.7.8.2 — Empty-context audit — empty-result reason; C-READ.1.9.7.8.3 — Empty-context audit — bare fallback used; C-READ.1.9.7.8.4 — Empty-context audit — context-limited and revisable

### C-READ.1.9.7.8.1 — Empty-context audit — empty channel
Stamp: DESIGNED    Source: [V10 §7F / GENUINE NO-CONTEXT HANDLING]

ALONE
- What it is: DESIGNED — The Empty-context audit — empty channel member or named content item carried within Genuine empty-context audit. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Takes in: DESIGNED — Required no-context audit content; JSON key not selected. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Does: DESIGNED — Identifies which channel returned nothing. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Gives out: DESIGNED — Required no-context audit content; JSON key not selected. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Must never: DESIGNED — Omit the required member. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9.7.8 — Genuine empty-context audit | Required no-context audit content; JSON key not selected. | Identifies which channel returned nothing. | Required no-context audit content; JSON key not selected. | [V10 §7F / GENUINE NO-CONTEXT HANDLING] |

SUB-PARTS: NONE

### C-READ.1.9.7.8.2 — Empty-context audit — empty-result reason
Stamp: DESIGNED    Source: [V10 §7F / GENUINE NO-CONTEXT HANDLING]

ALONE
- What it is: DESIGNED — The Empty-context audit — empty-result reason member or named content item carried within Genuine empty-context audit. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Takes in: DESIGNED — Required no-context audit content; JSON key not selected. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Does: DESIGNED — Records why no relevant context exists. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Gives out: DESIGNED — Required no-context audit content; JSON key not selected. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Must never: DESIGNED — Omit the required member. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9.7.8 — Genuine empty-context audit | Required no-context audit content; JSON key not selected. | Records why no relevant context exists. | Required no-context audit content; JSON key not selected. | [V10 §7F / GENUINE NO-CONTEXT HANDLING] |

SUB-PARTS: NONE

### C-READ.1.9.7.8.3 — Empty-context audit — bare fallback used
Stamp: DESIGNED    Source: [V10 §7F / GENUINE NO-CONTEXT HANDLING]

ALONE
- What it is: DESIGNED — The Empty-context audit — bare fallback used member or named content item carried within Genuine empty-context audit. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Takes in: DESIGNED — Required no-context audit content; JSON key not selected. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Does: DESIGNED — Records that the pass fell back to the target root alone. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Gives out: DESIGNED — Required no-context audit content; JSON key not selected. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Must never: DESIGNED — Omit the required member. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9.7.8 — Genuine empty-context audit | Required no-context audit content; JSON key not selected. | Records that the pass fell back to the target root alone. | Required no-context audit content; JSON key not selected. | [V10 §7F / GENUINE NO-CONTEXT HANDLING] |

SUB-PARTS: NONE

### C-READ.1.9.7.8.4 — Empty-context audit — context-limited and revisable
Stamp: DESIGNED    Source: [V10 §7F / GENUINE NO-CONTEXT HANDLING]

ALONE
- What it is: DESIGNED — The Empty-context audit — context-limited and revisable member or named content item carried within Genuine empty-context audit. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Takes in: DESIGNED — Required no-context audit content; JSON key not selected. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Does: DESIGNED — Keeps both qualifications explicit. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Gives out: DESIGNED — Required no-context audit content; JSON key not selected. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Must never: DESIGNED — Omit the required member. [V10 §7F / GENUINE NO-CONTEXT HANDLING]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.9.7.8 — Genuine empty-context audit | Required no-context audit content; JSON key not selected. | Keeps both qualifications explicit. | Required no-context audit content; JSON key not selected. | [V10 §7F / GENUINE NO-CONTEXT HANDLING] |

SUB-PARTS: NONE

### C-READ.1.10 — reading.schema_version
Stamp: DESIGNED    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: DESIGNED — The reading.schema_version member or named content item carried within Twelve-field reading representation v1. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: DESIGNED — Required on every new reading; first reading schema is `v1`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: DESIGNED — Identifies the contract under which the record was written; it cannot be retrofitted into immutable old records. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: DESIGNED — Required on every new reading; first reading schema is `v1`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: DESIGNED — Change an older reading in place to give it a newer schema_version. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1 — Twelve-field reading representation v1 | Required on every new reading; first reading schema is `v1`. | Identifies the contract under which the record was written; it cannot be retrofitted into immutable old records. | Required on every new reading; first reading schema is `v1`. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.1.11 — reading.derived_from
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — The reading.derived_from member or named content item carried within Twelve-field reading representation v1. [V10 §6B / READING record schema]
- Takes in: DESIGNED — Required list of parent reading IDs; `[]` when fresh directly from roots. [V10 §6B / READING record schema]
- Does: DESIGNED — Names prior readings from which this reading derives; roots themselves are referenced in `reads`. [V10 §6B / READING record schema]
- Gives out: DESIGNED — Required list of parent reading IDs; `[]` when fresh directly from roots. [V10 §6B / READING record schema]
- Must never: DESIGNED — Confuse parent reading IDs with source root IDs. [V10 §6B / READING record schema]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-READ.1.11.1 — Fresh-from-roots lineage: Stores the empty list in `derived_from`; the roots remain identified by `reads`. [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-READ.1.11.2 — Parent-reading lineage: Carries the parent reading IDs in `derived_from`. [V10 §6B / READING record schema]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1 — Twelve-field reading representation v1 | Required list of parent reading IDs; `[]` when fresh directly from roots. | Names prior readings from which this reading derives; roots themselves are referenced in `reads`. | Required list of parent reading IDs; `[]` when fresh directly from roots. | [V10 §6B / READING record schema] |

SUB-PARTS: C-READ.1.11.1 — Fresh-from-roots lineage; C-READ.1.11.2 — Parent-reading lineage

### C-READ.1.11.1 — Fresh-from-roots lineage
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — Stores the empty list in `derived_from`; the roots remain identified by `reads`. [V10 §6B / READING record schema]
- Takes in: DESIGNED — A reading produced directly from roots without parent readings. [V10 §6B / READING record schema]
- Does: DESIGNED — Stores the empty list in `derived_from`; the roots remain identified by `reads`. [V10 §6B / READING record schema]
- Gives out: DESIGNED — `derived_from=[]`. [V10 §6B / READING record schema]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.11 — reading.derived_from | A reading produced directly from roots without parent readings. | Stores the empty list in `derived_from`; the roots remain identified by `reads`. | `derived_from=[]`. | [V10 §6B / READING record schema] |

SUB-PARTS: NONE

### C-READ.1.11.2 — Parent-reading lineage
Stamp: DESIGNED    Source: [V10 §6B / READING record schema]

ALONE
- What it is: DESIGNED — Carries the parent reading IDs in `derived_from`. [V10 §6B / READING record schema]
- Takes in: DESIGNED — A reading derived from earlier readings. [V10 §6B / READING record schema]
- Does: DESIGNED — Carries the parent reading IDs in `derived_from`. [V10 §6B / READING record schema]
- Gives out: DESIGNED — The reading’s prior-reading lineage is inspectable. [V10 §6B / READING record schema]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1.11 — reading.derived_from | A reading derived from earlier readings. | Carries the parent reading IDs in `derived_from`. | The reading’s prior-reading lineage is inspectable. | [V10 §6B / READING record schema] |

SUB-PARTS: NONE

### C-READ.1.12 — reading.idempotency_key
Stamp: DESIGNED    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: DESIGNED — The reading.idempotency_key member or named content item carried within Twelve-field reading representation v1. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: DESIGNED — Required operation identity, separate from record `id`; unique per store. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: DESIGNED — The writer rejects a key already committed in the target store. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: DESIGNED — Uniqueness is per store under V10. [SOURCE CONFLICT: CR §1C — ACCRETIVE STORE PROHIBITIONS forbids reuse of a key already committed to any readings store; V10 §6A / SCHEMA CONSTRAINTS specifies uniqueness per store] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: DESIGNED — Required operation identity, separate from record `id`; unique per store. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: DESIGNED — Omit the key or substitute record identity for operation identity. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DECIDED-2026-09-25 — C-READ.1.12.1 — Optional reading-content hash: a content hash cannot replace operation identity. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.1 — Twelve-field reading representation v1 | Required operation identity, separate from record `id`; unique per store. | The writer rejects a key already committed in the target store. | Required operation identity, separate from record `id`; unique per store. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: C-READ.1.12.1 — Optional reading-content hash

### C-READ.1.12.1 — Optional reading-content hash
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key]

ALONE
- What it is: DECIDED-2026-09-25 — An optional exact-duplicate/integrity aid over `reads` + `meaning` + `produced_by` + `schema_version`. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key]
- Takes in: DECIDED-2026-09-25 — Those four content/provenance members. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key]
- Does: DECIDED-2026-09-25 — May detect exact duplicate payloads or integrity changes; it does not supply the retry guarantee. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key]
- Gives out: DECIDED-2026-09-25 — An optional content-hash result. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key]
- Must never: DECIDED-2026-09-25 — Use a content hash as the operation key: a mouth can rephrase on replay, and legitimate independent readings can have identical payloads. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DECIDED-2026-09-25 — C-READ.1.12.1.1 — Rephrased replay: A changed content hash can miss a replay duplicate. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key]
- Gated by: DECIDED-2026-09-25 — C-READ.1.12.1.2 — Independent identical payloads: A matching content hash can falsely collapse independent readings. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ.1.12 — reading.idempotency_key | An attempted content-hash retry identity. | Keeps exact-content identity separate from operation identity. | Retries remain keyed by the operation key. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key] |

SUB-PARTS: C-READ.1.12.1.1 — Rephrased replay; C-READ.1.12.1.2 — Independent identical payloads

### C-READ.1.12.1.1 — Rephrased replay
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key]

ALONE
- What it is: DECIDED-2026-09-25 — A changed content hash can miss a replay duplicate. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key]
- Takes in: DECIDED-2026-09-25 — The same operation retried with rephrased `meaning`. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key]
- Does: DECIDED-2026-09-25 — A changed content hash can miss a replay duplicate. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key]
- Gives out: DECIDED-2026-09-25 — Content hashing remains an integrity/duplicate aid only. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key]
- Must never: DECIDED-2026-09-25 — Replace the stable operation key with the content hash. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ.1.12.1 — Optional reading-content hash | The same operation retried with rephrased `meaning`. | A changed content hash can miss a replay duplicate. | Content hashing remains an integrity/duplicate aid only. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key] |

SUB-PARTS: NONE

### C-READ.1.12.1.2 — Independent identical payloads
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key]

ALONE
- What it is: DECIDED-2026-09-25 — A matching content hash can falsely collapse independent readings. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key]
- Takes in: DECIDED-2026-09-25 — Two genuinely independent readings with matching content payloads. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key]
- Does: DECIDED-2026-09-25 — A matching content hash can falsely collapse independent readings. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key]
- Gives out: DECIDED-2026-09-25 — Content hashing remains an integrity/duplicate aid only. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key]
- Must never: DECIDED-2026-09-25 — Replace the stable operation key with the content hash. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ.1.12.1 — Optional reading-content hash | Two genuinely independent readings with matching content payloads. | A matching content hash can falsely collapse independent readings. | Content hashing remains an integrity/duplicate aid only. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §6B / idempotency_key] |

SUB-PARTS: NONE

### C-READ.2 — _validate_reading
Stamp: BUILT    Source: [V10 §6B / READING record schema] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]

ALONE
- What it is: BUILT — The twelve-field reading shape gate in the shared store module. [V10 §6B / READING record schema] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Takes in: BUILT — A proposed reading with all twelve members and nested values. [V10 §6B / READING record schema] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Does: BUILT — Validates the reading shape, using `_check_common` for `id` and `timestamp`; rejects malformed data without judging interpretive certainty. [V10 §6B / READING record schema] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Gives out: BUILT — A shape-valid record or a validation refusal. [V10 §6B / READING record schema] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Must never: BUILT — Certify interpretive truth, reject honest uncertainty, or replace the Reading Proposal Acceptance Check. [V10 §6B / READING record schema] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Fails closed by: BUILT — Rejects malformed readings before any append. [V10 §6B / READING record schema] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]

TOGETHER
- Fed by: BUILT — C-READ.1 — Twelve-field reading representation v1: receives the twelve-field representation to check. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Fed by: BUILT — C-READ.2.14 — Low confidence remains valid: Allows the reading through the shape gate and keeps its low-confidence marking. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Fed by: BUILT — C-READ.2.15 — Weak interpretation remains valid: Allows the reading through the shape gate and keeps the weakness visible. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Fed by: BUILT — C-READ.2.16 — Empty story remains valid: Allows the empty story list. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Fed by: BUILT — C-READ.2.17 — Insufficient-context meaning remains valid: Allows the honest reading, marked revisable. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Gated by: BUILT — C-READ.2.1 — Required twelve-field shape: Requires `id`, `reads`, `meaning`, `confidence`, `role`, `story_layer`, `mode`, `timestamp`, `produced_by`, `schema_version`, `derived_from`, `idempotency_key`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: BUILT — C-READ.2.2 — Non-empty reads list: Requires a non-empty list of root IDs. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: BUILT — C-READ.2.3 — String meaning: Requires the interpretation string; an honest insufficient-context meaning is valid. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: BUILT — C-READ.2.4 — Two-slot confidence shape: Requires an object with both `interpretation_confidence` and `source_reliability`; never accepts a bare blended number. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: BUILT — C-READ.2.5 — Interpretation-confidence presence: Checks presence and non-emptiness without imposing a fixed numeric scale. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: BUILT — C-READ.2.6 — Source-reliability key presence: Requires the key; does not resolve the unverified not-yet-knowable value form. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: BUILT — C-READ.2.7 — Story list shape: Requires a list and permits the empty list. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: BUILT — C-READ.2.8 — Story omission rule: Keeps unknown optional members omitted instead of filled with `"unknown"`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: BUILT — C-READ.2.9 — Mode object shape: Carries `label` as an open word and `classification_confidence` as its local confidence. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: BUILT — C-READ.2.10 — Origin vocabulary: Requires one of `observed`, `imported`, `simulated`, `generated`, `reaction`, `human_annotation`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: BUILT — C-READ.2.11 — Schema-version presence: Requires the contract-version member on every new reading. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: BUILT — C-READ.2.12 — Parent-reading list: Carries the parent reading IDs as a list and permits `[]` when fresh from roots. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: BUILT — C-READ.2.13 — Operation-key presence: Requires the operation identity for the reading. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ — Reading record, validator, writer (§6B) | A proposed reading. | Checks the required twelve-field shape. | Malformed data is refused; well-formed uncertain data can proceed. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6B / READING record schema] |
| 2 · BUILT | C-READ.3 — append_reading | The assembled record. | Runs `_validate_reading()`. | Invalid shape stops the append. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] |

SUB-PARTS: C-READ.2.1 — Required twelve-field shape; C-READ.2.2 — Non-empty reads list; C-READ.2.3 — String meaning; C-READ.2.4 — Two-slot confidence shape; C-READ.2.5 — Interpretation-confidence presence; C-READ.2.6 — Source-reliability key presence; C-READ.2.7 — Story list shape; C-READ.2.8 — Story omission rule; C-READ.2.9 — Mode object shape; C-READ.2.10 — Origin vocabulary; C-READ.2.11 — Schema-version presence; C-READ.2.12 — Parent-reading list; C-READ.2.13 — Operation-key presence; C-READ.2.14 — Low confidence remains valid; C-READ.2.15 — Weak interpretation remains valid; C-READ.2.16 — Empty story remains valid; C-READ.2.17 — Insufficient-context meaning remains valid

### C-READ.2.1 — Required twelve-field shape
Stamp: BUILT    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Requires `id`, `reads`, `meaning`, `confidence`, `role`, `story_layer`, `mode`, `timestamp`, `produced_by`, `schema_version`, `derived_from`, `idempotency_key`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — The record’s top-level members. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Requires `id`, `reads`, `meaning`, `confidence`, `role`, `story_layer`, `mode`, `timestamp`, `produced_by`, `schema_version`, `derived_from`, `idempotency_key`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — This portion of the shape contract passes, or the malformed record is refused. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Rejects a malformed reading before append. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: BUILT — C-READ.2.1.1 — Required twelve-field shape refusal: Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2 — _validate_reading | The record’s top-level members. | Requires `id`, `reads`, `meaning`, `confidence`, `role`, `story_layer`, `mode`, `timestamp`, `produced_by`, `schema_version`, `derived_from`, `idempotency_key`. | This portion of the shape contract passes, or the malformed record is refused. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: C-READ.2.1.1 — Required twelve-field shape refusal

### C-READ.2.1.1 — Required twelve-field shape refusal
Stamp: BUILT    Source: [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — The record’s top-level members. that violates the stated shape constraint. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — No reading append from that malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Stops this append. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2.1 — Required twelve-field shape | The record’s top-level members. that violates the stated shape constraint. | Refuses the malformed record. | No reading append from that malformed record. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.2.2 — Non-empty reads list
Stamp: BUILT    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Requires a non-empty list of root IDs. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `reads`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Requires a non-empty list of root IDs. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — This portion of the shape contract passes, or the malformed record is refused. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Rejects a malformed reading before append. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: BUILT — C-READ.2.2.1 — Non-empty reads list refusal: Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2 — _validate_reading | `reads`. | Requires a non-empty list of root IDs. | This portion of the shape contract passes, or the malformed record is refused. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: C-READ.2.2.1 — Non-empty reads list refusal

### C-READ.2.2.1 — Non-empty reads list refusal
Stamp: BUILT    Source: [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `reads`. that violates the stated shape constraint. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — No reading append from that malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Stops this append. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2.2 — Non-empty reads list | `reads`. that violates the stated shape constraint. | Refuses the malformed record. | No reading append from that malformed record. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.2.3 — String meaning
Stamp: BUILT    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Requires the interpretation string; an honest insufficient-context meaning is valid. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `meaning`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Requires the interpretation string; an honest insufficient-context meaning is valid. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — This portion of the shape contract passes, or the malformed record is refused. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Rejects a malformed reading before append. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: BUILT — C-READ.2.3.1 — String meaning refusal: Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2 — _validate_reading | `meaning`. | Requires the interpretation string; an honest insufficient-context meaning is valid. | This portion of the shape contract passes, or the malformed record is refused. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: C-READ.2.3.1 — String meaning refusal

### C-READ.2.3.1 — String meaning refusal
Stamp: BUILT    Source: [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `meaning`. that violates the stated shape constraint. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — No reading append from that malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Stops this append. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2.3 — String meaning | `meaning`. that violates the stated shape constraint. | Refuses the malformed record. | No reading append from that malformed record. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.2.4 — Two-slot confidence shape
Stamp: BUILT    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Requires an object with both `interpretation_confidence` and `source_reliability`; never accepts a bare blended number. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `confidence`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Requires an object with both `interpretation_confidence` and `source_reliability`; never accepts a bare blended number. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — This portion of the shape contract passes, or the malformed record is refused. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Rejects a malformed reading before append. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: BUILT — C-READ.2.4.1 — Two-slot confidence shape refusal: Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2 — _validate_reading | `confidence`. | Requires an object with both `interpretation_confidence` and `source_reliability`; never accepts a bare blended number. | This portion of the shape contract passes, or the malformed record is refused. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: C-READ.2.4.1 — Two-slot confidence shape refusal

### C-READ.2.4.1 — Two-slot confidence shape refusal
Stamp: BUILT    Source: [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `confidence`. that violates the stated shape constraint. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — No reading append from that malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Stops this append. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2.4 — Two-slot confidence shape | `confidence`. that violates the stated shape constraint. | Refuses the malformed record. | No reading append from that malformed record. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.2.5 — Interpretation-confidence presence
Stamp: BUILT    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Checks presence and non-emptiness without imposing a fixed numeric scale. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `confidence.interpretation_confidence`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Checks presence and non-emptiness without imposing a fixed numeric scale. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — This portion of the shape contract passes, or the malformed record is refused. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Rejects a malformed reading before append. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: BUILT — C-READ.2.5.1 — Interpretation-confidence presence refusal: Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2 — _validate_reading | `confidence.interpretation_confidence`. | Checks presence and non-emptiness without imposing a fixed numeric scale. | This portion of the shape contract passes, or the malformed record is refused. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: C-READ.2.5.1 — Interpretation-confidence presence refusal

### C-READ.2.5.1 — Interpretation-confidence presence refusal
Stamp: BUILT    Source: [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `confidence.interpretation_confidence`. that violates the stated shape constraint. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — No reading append from that malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Stops this append. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2.5 — Interpretation-confidence presence | `confidence.interpretation_confidence`. that violates the stated shape constraint. | Refuses the malformed record. | No reading append from that malformed record. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.2.6 — Source-reliability key presence
Stamp: BUILT    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Requires the key; does not resolve the unverified not-yet-knowable value form. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `confidence.source_reliability`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Requires the key; does not resolve the unverified not-yet-knowable value form. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — This portion of the shape contract passes, or the malformed record is refused. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Rejects a malformed reading before append. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: BUILT — C-READ.2.6.1 — Source-reliability key presence refusal: Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2 — _validate_reading | `confidence.source_reliability`. | Requires the key; does not resolve the unverified not-yet-knowable value form. | This portion of the shape contract passes, or the malformed record is refused. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: C-READ.2.6.1 — Source-reliability key presence refusal

### C-READ.2.6.1 — Source-reliability key presence refusal
Stamp: BUILT    Source: [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `confidence.source_reliability`. that violates the stated shape constraint. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — No reading append from that malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Stops this append. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2.6 — Source-reliability key presence | `confidence.source_reliability`. that violates the stated shape constraint. | Refuses the malformed record. | No reading append from that malformed record. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.2.7 — Story list shape
Stamp: BUILT    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Requires a list and permits the empty list. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `story_layer`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Requires a list and permits the empty list. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — This portion of the shape contract passes, or the malformed record is refused. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Rejects a malformed reading before append. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: BUILT — C-READ.2.7.1 — Story list shape refusal: Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2 — _validate_reading | `story_layer`. | Requires a list and permits the empty list. | This portion of the shape contract passes, or the malformed record is refused. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: C-READ.2.7.1 — Story list shape refusal

### C-READ.2.7.1 — Story list shape refusal
Stamp: BUILT    Source: [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `story_layer`. that violates the stated shape constraint. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — No reading append from that malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Stops this append. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2.7 — Story list shape | `story_layer`. that violates the stated shape constraint. | Refuses the malformed record. | No reading append from that malformed record. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.2.8 — Story omission rule
Stamp: BUILT    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Keeps unknown optional members omitted instead of filled with `"unknown"`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — Optional members in a story entry. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Keeps unknown optional members omitted instead of filled with `"unknown"`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — This portion of the shape contract passes, or the malformed record is refused. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Rejects a malformed reading before append. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: BUILT — C-READ.2.8.1 — Story omission rule refusal: Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2 — _validate_reading | Optional members in a story entry. | Keeps unknown optional members omitted instead of filled with `"unknown"`. | This portion of the shape contract passes, or the malformed record is refused. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: C-READ.2.8.1 — Story omission rule refusal

### C-READ.2.8.1 — Story omission rule refusal
Stamp: BUILT    Source: [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — Optional members in a story entry. that violates the stated shape constraint. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — No reading append from that malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Stops this append. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2.8 — Story omission rule | Optional members in a story entry. that violates the stated shape constraint. | Refuses the malformed record. | No reading append from that malformed record. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.2.9 — Mode object shape
Stamp: BUILT    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Carries `label` as an open word and `classification_confidence` as its local confidence. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `mode`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Carries `label` as an open word and `classification_confidence` as its local confidence. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — This portion of the shape contract passes, or the malformed record is refused. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Rejects a malformed reading before append. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: BUILT — C-READ.2.9.1 — Mode object shape refusal: Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2 — _validate_reading | `mode`. | Carries `label` as an open word and `classification_confidence` as its local confidence. | This portion of the shape contract passes, or the malformed record is refused. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: C-READ.2.9.1 — Mode object shape refusal

### C-READ.2.9.1 — Mode object shape refusal
Stamp: BUILT    Source: [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `mode`. that violates the stated shape constraint. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — No reading append from that malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Stops this append. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2.9 — Mode object shape | `mode`. that violates the stated shape constraint. | Refuses the malformed record. | No reading append from that malformed record. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.2.10 — Origin vocabulary
Stamp: BUILT    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Requires one of `observed`, `imported`, `simulated`, `generated`, `reaction`, `human_annotation`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `produced_by.origin`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Requires one of `observed`, `imported`, `simulated`, `generated`, `reaction`, `human_annotation`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — This portion of the shape contract passes, or the malformed record is refused. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Rejects a malformed reading before append. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: BUILT — C-READ.2.10.1 — Origin vocabulary refusal: Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2 — _validate_reading | `produced_by.origin`. | Requires one of `observed`, `imported`, `simulated`, `generated`, `reaction`, `human_annotation`. | This portion of the shape contract passes, or the malformed record is refused. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: C-READ.2.10.1 — Origin vocabulary refusal

### C-READ.2.10.1 — Origin vocabulary refusal
Stamp: BUILT    Source: [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `produced_by.origin`. that violates the stated shape constraint. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — No reading append from that malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Stops this append. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2.10 — Origin vocabulary | `produced_by.origin`. that violates the stated shape constraint. | Refuses the malformed record. | No reading append from that malformed record. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.2.11 — Schema-version presence
Stamp: BUILT    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Requires the contract-version member on every new reading. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `schema_version`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Requires the contract-version member on every new reading. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — This portion of the shape contract passes, or the malformed record is refused. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Rejects a malformed reading before append. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: BUILT — C-READ.2.11.1 — Schema-version presence refusal: Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2 — _validate_reading | `schema_version`. | Requires the contract-version member on every new reading. | This portion of the shape contract passes, or the malformed record is refused. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: C-READ.2.11.1 — Schema-version presence refusal

### C-READ.2.11.1 — Schema-version presence refusal
Stamp: BUILT    Source: [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `schema_version`. that violates the stated shape constraint. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — No reading append from that malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Stops this append. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2.11 — Schema-version presence | `schema_version`. that violates the stated shape constraint. | Refuses the malformed record. | No reading append from that malformed record. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.2.12 — Parent-reading list
Stamp: BUILT    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Carries the parent reading IDs as a list and permits `[]` when fresh from roots. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `derived_from`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Carries the parent reading IDs as a list and permits `[]` when fresh from roots. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — This portion of the shape contract passes, or the malformed record is refused. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Rejects a malformed reading before append. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: BUILT — C-READ.2.12.1 — Parent-reading list refusal: Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2 — _validate_reading | `derived_from`. | Carries the parent reading IDs as a list and permits `[]` when fresh from roots. | This portion of the shape contract passes, or the malformed record is refused. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: C-READ.2.12.1 — Parent-reading list refusal

### C-READ.2.12.1 — Parent-reading list refusal
Stamp: BUILT    Source: [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `derived_from`. that violates the stated shape constraint. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — No reading append from that malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Stops this append. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2.12 — Parent-reading list | `derived_from`. that violates the stated shape constraint. | Refuses the malformed record. | No reading append from that malformed record. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.2.13 — Operation-key presence
Stamp: BUILT    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Requires the operation identity for the reading. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `idempotency_key`. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Requires the operation identity for the reading. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — This portion of the shape contract passes, or the malformed record is refused. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Rejects a malformed reading before append. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: BUILT — C-READ.2.13.1 — Operation-key presence refusal: Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2 — _validate_reading | `idempotency_key`. | Requires the operation identity for the reading. | This portion of the shape contract passes, or the malformed record is refused. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: C-READ.2.13.1 — Operation-key presence refusal

### C-READ.2.13.1 — Operation-key presence refusal
Stamp: BUILT    Source: [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — `idempotency_key`. that violates the stated shape constraint. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Refuses the malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — No reading append from that malformed record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Stops this append. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2.13 — Operation-key presence | `idempotency_key`. that violates the stated shape constraint. | Refuses the malformed record. | No reading append from that malformed record. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.2.14 — Low confidence remains valid
Stamp: BUILT    Source: [V10 §6B / READING record schema] [DD §3A. The reading record]

ALONE
- What it is: BUILT — Allows the reading through the shape gate and keeps its low-confidence marking. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Takes in: BUILT — A well-formed reading with low confidence. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Does: BUILT — Allows the reading through the shape gate and keeps its low-confidence marking. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Gives out: BUILT — A shape-valid reading can be written, subject to the writer’s other checks. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Must never: BUILT — Reject solely for this honest uncertainty. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2 — _validate_reading | A well-formed reading with low confidence. | Allows the reading through the shape gate and keeps its low-confidence marking. | A shape-valid reading can be written, subject to the writer’s other checks. | [V10 §6B / READING record schema] [DD §3A. The reading record] |

SUB-PARTS: NONE

### C-READ.2.15 — Weak interpretation remains valid
Stamp: BUILT    Source: [V10 §6B / READING record schema] [DD §3A. The reading record]

ALONE
- What it is: BUILT — Allows the reading through the shape gate and keeps the weakness visible. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Takes in: BUILT — A well-formed weak reading. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Does: BUILT — Allows the reading through the shape gate and keeps the weakness visible. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Gives out: BUILT — A shape-valid reading can be written, subject to the writer’s other checks. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Must never: BUILT — Reject solely for this honest uncertainty. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2 — _validate_reading | A well-formed weak reading. | Allows the reading through the shape gate and keeps the weakness visible. | A shape-valid reading can be written, subject to the writer’s other checks. | [V10 §6B / READING record schema] [DD §3A. The reading record] |

SUB-PARTS: NONE

### C-READ.2.16 — Empty story remains valid
Stamp: BUILT    Source: [V10 §6B / READING record schema] [DD §3A. The reading record]

ALONE
- What it is: BUILT — Allows the empty story list. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Takes in: BUILT — A well-formed reading with `story_layer=[]`. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Does: BUILT — Allows the empty story list. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Gives out: BUILT — A shape-valid reading can be written, subject to the writer’s other checks. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Must never: BUILT — Reject solely for this honest uncertainty. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2 — _validate_reading | A well-formed reading with `story_layer=[]`. | Allows the empty story list. | A shape-valid reading can be written, subject to the writer’s other checks. | [V10 §6B / READING record schema] [DD §3A. The reading record] |

SUB-PARTS: NONE

### C-READ.2.17 — Insufficient-context meaning remains valid
Stamp: BUILT    Source: [V10 §6B / READING record schema] [DD §3A. The reading record]

ALONE
- What it is: BUILT — Allows the honest reading, marked revisable. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Takes in: BUILT — A well-formed honest insufficient-context reading. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Does: BUILT — Allows the honest reading, marked revisable. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Gives out: BUILT — A shape-valid reading can be written, subject to the writer’s other checks. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Must never: BUILT — Reject solely for this honest uncertainty. [V10 §6B / READING record schema] [DD §3A. The reading record]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.2 — _validate_reading | A well-formed honest insufficient-context reading. | Allows the honest reading, marked revisable. | A shape-valid reading can be written, subject to the writer’s other checks. | [V10 §6B / READING record schema] [DD §3A. The reading record] |

SUB-PARTS: NONE

### C-READ.3 — append_reading
Stamp: BUILT    Source: [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema] [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]

ALONE
- What it is: BUILT — The reading writer within `nh_accretive_store.py`. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema] [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]
- Takes in: BUILT — `reads`, `meaning`, `confidence`, `role`, `story_layer`, `mode`, `produced_by`, `schema_version`, `derived_from`, `idempotency_key`, `record_id`, `timestamp`; the destination is selected by the supplied path argument. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema] [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]
- Does: BUILT — Validates shape; verifies every root reference; checks operation-key uniqueness; appends atomically with flush and fsync, append-only, to the supplied target path. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema] [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]
- Gives out: BUILT — A committed reading in the selected readings file, or a refused append. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema] [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]
- Must never: BUILT — Bypass validation, root verification or idempotency; directly write into a root file. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema] [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]
- Fails closed by: BUILT — Refuses malformed input, missing referenced roots and already-committed keys before append. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema] [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]

TOGETHER
- Fed by: BUILT — C-READ.1 — Twelve-field reading representation v1: receives reading data in the twelve-field representation. [V10 §6B / READING record schema] [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Fed by: BUILT — C-READ.3.1 — Reading writer arguments: supplies the reading-shaped invocation arguments. [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]
- Fed by: BUILT — C-READ.3.4 — Atomic append: Appends atomically, with flush and fsync, preserving append-only records. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema] [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]
- Fed by: BUILT — C-READ.3.5 — Destination routing: Routes the append to the chosen readings destination; the built A/B output target is quarantine. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema]
- Fed by: DESIGNED — C-READ.3.7 — New-root worker reading-write handoff: supplies the stable-key new-root reading attempt or recovers its existing outcome. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record]
- Gated by: BUILT — C-READ.2 — _validate_reading: requires a shape-valid record before commit. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]
- Gated by: BUILT — C-READ.3.2 — Referenced-root verification: Verifies each ID exists in the sealed roots before commit. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema]
- Gated by: BUILT — C-READ.3.3 — Committed-key rejection: Rejects an already-committed key; the operation key is separate from record ID. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema]
- Gated by: DESIGNED — C-READ.3.6 — Shared write boundary: Uses `append_reading()` and the validated functions in `nh_accretive_store.py`; direct opens for append or overwrite are prohibited. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [CR §1C — ACCRETIVE STORE PROHIBITIONS]
- Gated by: DESIGNED — C-READ.5 — Production readings authorization: the designed additional production gate is separate from built path routing. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Changes: BUILT — C-READ.4 — Quarantine readings destination: appends the validated test reading to this destination. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §5]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ — Reading record, validator, writer (§6B) | Reading members, operation key and path. | Validates and commits through `append_reading()`. | One committed reading or a refusal. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] |

SUB-PARTS: C-READ.3.1 — Reading writer arguments; C-READ.3.2 — Referenced-root verification; C-READ.3.3 — Committed-key rejection; C-READ.3.4 — Atomic append; C-READ.3.5 — Destination routing; C-READ.3.6 — Shared write boundary; C-READ.3.7 — New-root worker reading-write handoff

### C-READ.3.1 — Reading writer arguments
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]

ALONE
- What it is: BUILT — The reading-shaped writer input contract recorded in V10’s status table. [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]
- Takes in: BUILT — `reads`, `meaning`, `confidence`, `role`, `story_layer`, `mode`, `produced_by`, `schema_version`, `derived_from`, `idempotency_key`, `record_id`, `timestamp`, and a target-path selection. [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]
- Does: BUILT — Accepts the reading-shaped arguments at the shared write boundary; the path argument determines the destination. [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]
- Gives out: BUILT — Reading data, record-identity input, creation-time input and destination supplied to the writer. [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: BUILT — C-READ.3.1.1 — append_reading argument — reads: carries this member as part of the containing record. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Fed by: BUILT — C-READ.3.1.2 — append_reading argument — meaning: carries this member as part of the containing record. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Fed by: BUILT — C-READ.3.1.3 — append_reading argument — confidence: carries this member as part of the containing record. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Fed by: BUILT — C-READ.3.1.4 — append_reading argument — role: carries this member as part of the containing record. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Fed by: BUILT — C-READ.3.1.5 — append_reading argument — story_layer: carries this member as part of the containing record. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Fed by: BUILT — C-READ.3.1.6 — append_reading argument — mode: carries this member as part of the containing record. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Fed by: BUILT — C-READ.3.1.7 — append_reading argument — produced_by: carries this member as part of the containing record. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Fed by: BUILT — C-READ.3.1.8 — append_reading argument — schema_version: carries this member as part of the containing record. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Fed by: BUILT — C-READ.3.1.9 — append_reading argument — derived_from: carries this member as part of the containing record. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Fed by: BUILT — C-READ.3.1.10 — append_reading argument — idempotency_key: carries this member as part of the containing record. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Fed by: BUILT — C-READ.3.1.11 — append_reading argument — record_id: carries this member as part of the containing record. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Fed by: BUILT — C-READ.3.1.12 — append_reading argument — timestamp: carries this member as part of the containing record. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Fed by: BUILT — C-READ.3.1.13 — append_reading target-path selection: carries this member as part of the containing record. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3 — append_reading | The named writer arguments. | Carries the caller input to the shared writer. | The writer invocation data. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] |

SUB-PARTS: C-READ.3.1.1 — append_reading argument — reads; C-READ.3.1.2 — append_reading argument — meaning; C-READ.3.1.3 — append_reading argument — confidence; C-READ.3.1.4 — append_reading argument — role; C-READ.3.1.5 — append_reading argument — story_layer; C-READ.3.1.6 — append_reading argument — mode; C-READ.3.1.7 — append_reading argument — produced_by; C-READ.3.1.8 — append_reading argument — schema_version; C-READ.3.1.9 — append_reading argument — derived_from; C-READ.3.1.10 — append_reading argument — idempotency_key; C-READ.3.1.11 — append_reading argument — record_id; C-READ.3.1.12 — append_reading argument — timestamp; C-READ.3.1.13 — append_reading target-path selection

### C-READ.3.1.1 — append_reading argument — reads
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE]

ALONE
- What it is: BUILT — The append_reading argument — reads member or named content item carried within Reading writer arguments. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Takes in: BUILT — Named writer argument `reads`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Does: BUILT — Carries this input in the reading-shaped writer signature. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Gives out: BUILT — Named writer argument `reads`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3.1 — Reading writer arguments | Named writer argument `reads`. | Carries this input in the reading-shaped writer signature. | Named writer argument `reads`. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE] |

SUB-PARTS: NONE

### C-READ.3.1.2 — append_reading argument — meaning
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE]

ALONE
- What it is: BUILT — The append_reading argument — meaning member or named content item carried within Reading writer arguments. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Takes in: BUILT — Named writer argument `meaning`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Does: BUILT — Carries this input in the reading-shaped writer signature. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Gives out: BUILT — Named writer argument `meaning`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3.1 — Reading writer arguments | Named writer argument `meaning`. | Carries this input in the reading-shaped writer signature. | Named writer argument `meaning`. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE] |

SUB-PARTS: NONE

### C-READ.3.1.3 — append_reading argument — confidence
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE]

ALONE
- What it is: BUILT — The append_reading argument — confidence member or named content item carried within Reading writer arguments. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Takes in: BUILT — Named writer argument `confidence`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Does: BUILT — Carries this input in the reading-shaped writer signature. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Gives out: BUILT — Named writer argument `confidence`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3.1 — Reading writer arguments | Named writer argument `confidence`. | Carries this input in the reading-shaped writer signature. | Named writer argument `confidence`. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE] |

SUB-PARTS: NONE

### C-READ.3.1.4 — append_reading argument — role
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE]

ALONE
- What it is: BUILT — The append_reading argument — role member or named content item carried within Reading writer arguments. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Takes in: BUILT — Named writer argument `role`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Does: BUILT — Carries this input in the reading-shaped writer signature. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Gives out: BUILT — Named writer argument `role`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3.1 — Reading writer arguments | Named writer argument `role`. | Carries this input in the reading-shaped writer signature. | Named writer argument `role`. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE] |

SUB-PARTS: NONE

### C-READ.3.1.5 — append_reading argument — story_layer
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE]

ALONE
- What it is: BUILT — The append_reading argument — story_layer member or named content item carried within Reading writer arguments. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Takes in: BUILT — Named writer argument `story_layer`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Does: BUILT — Carries this input in the reading-shaped writer signature. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Gives out: BUILT — Named writer argument `story_layer`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3.1 — Reading writer arguments | Named writer argument `story_layer`. | Carries this input in the reading-shaped writer signature. | Named writer argument `story_layer`. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE] |

SUB-PARTS: NONE

### C-READ.3.1.6 — append_reading argument — mode
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE]

ALONE
- What it is: BUILT — The append_reading argument — mode member or named content item carried within Reading writer arguments. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Takes in: BUILT — Named writer argument `mode`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Does: BUILT — Carries this input in the reading-shaped writer signature. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Gives out: BUILT — Named writer argument `mode`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3.1 — Reading writer arguments | Named writer argument `mode`. | Carries this input in the reading-shaped writer signature. | Named writer argument `mode`. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE] |

SUB-PARTS: NONE

### C-READ.3.1.7 — append_reading argument — produced_by
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE]

ALONE
- What it is: BUILT — The append_reading argument — produced_by member or named content item carried within Reading writer arguments. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Takes in: BUILT — Named writer argument `produced_by`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Does: BUILT — Carries this input in the reading-shaped writer signature. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Gives out: BUILT — Named writer argument `produced_by`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3.1 — Reading writer arguments | Named writer argument `produced_by`. | Carries this input in the reading-shaped writer signature. | Named writer argument `produced_by`. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE] |

SUB-PARTS: NONE

### C-READ.3.1.8 — append_reading argument — schema_version
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE]

ALONE
- What it is: BUILT — The append_reading argument — schema_version member or named content item carried within Reading writer arguments. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Takes in: BUILT — Named writer argument `schema_version`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Does: BUILT — Carries this input in the reading-shaped writer signature. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Gives out: BUILT — Named writer argument `schema_version`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3.1 — Reading writer arguments | Named writer argument `schema_version`. | Carries this input in the reading-shaped writer signature. | Named writer argument `schema_version`. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE] |

SUB-PARTS: NONE

### C-READ.3.1.9 — append_reading argument — derived_from
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE]

ALONE
- What it is: BUILT — The append_reading argument — derived_from member or named content item carried within Reading writer arguments. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Takes in: BUILT — Named writer argument `derived_from`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Does: BUILT — Carries this input in the reading-shaped writer signature. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Gives out: BUILT — Named writer argument `derived_from`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3.1 — Reading writer arguments | Named writer argument `derived_from`. | Carries this input in the reading-shaped writer signature. | Named writer argument `derived_from`. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE] |

SUB-PARTS: NONE

### C-READ.3.1.10 — append_reading argument — idempotency_key
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE]

ALONE
- What it is: BUILT — The append_reading argument — idempotency_key member or named content item carried within Reading writer arguments. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Takes in: BUILT — Named writer argument `idempotency_key`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Does: BUILT — Carries this input in the reading-shaped writer signature. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Gives out: BUILT — Named writer argument `idempotency_key`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3.1 — Reading writer arguments | Named writer argument `idempotency_key`. | Carries this input in the reading-shaped writer signature. | Named writer argument `idempotency_key`. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE] |

SUB-PARTS: NONE

### C-READ.3.1.11 — append_reading argument — record_id
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE]

ALONE
- What it is: BUILT — The append_reading argument — record_id member or named content item carried within Reading writer arguments. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Takes in: BUILT — Named writer argument `record_id`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Does: BUILT — Carries this input in the reading-shaped writer signature. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Gives out: BUILT — Named writer argument `record_id`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3.1 — Reading writer arguments | Named writer argument `record_id`. | Carries this input in the reading-shaped writer signature. | Named writer argument `record_id`. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE] |

SUB-PARTS: NONE

### C-READ.3.1.12 — append_reading argument — timestamp
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE]

ALONE
- What it is: BUILT — The append_reading argument — timestamp member or named content item carried within Reading writer arguments. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Takes in: BUILT — Named writer argument `timestamp`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Does: BUILT — Carries this input in the reading-shaped writer signature. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Gives out: BUILT — Named writer argument `timestamp`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3.1 — Reading writer arguments | Named writer argument `timestamp`. | Carries this input in the reading-shaped writer signature. | Named writer argument `timestamp`. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE] |

SUB-PARTS: NONE

### C-READ.3.1.13 — append_reading target-path selection
Stamp: BUILT    Source: [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]

ALONE
- What it is: BUILT — The append_reading target-path selection member or named content item carried within Reading writer arguments. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]
- Takes in: BUILT — Caller-supplied destination path. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]
- Does: BUILT — Selects the quarantine or production reading path; path routing itself supplies no production authorization. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]
- Gives out: BUILT — Caller-supplied destination path. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3.1 — Reading writer arguments | Caller-supplied destination path. | Selects the quarantine or production reading path; path routing itself supplies no production authorization. | Caller-supplied destination path. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] |

SUB-PARTS: NONE

### C-READ.3.2 — Referenced-root verification
Stamp: BUILT    Source: [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema]

ALONE
- What it is: BUILT — Verifies each ID exists in the sealed roots before commit. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema]
- Takes in: BUILT — Every ID in `reads`. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema]
- Does: BUILT — Verifies each ID exists in the sealed roots before commit. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema]
- Gives out: BUILT — The references are verified or the append is refused. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: BUILT — C-READ.3.2.1 — Missing-root refusal: Refuses commit until every referenced root exists. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3 — append_reading | Every ID in `reads`. | Verifies each ID exists in the sealed roots before commit. | The references are verified or the append is refused. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema] |

SUB-PARTS: C-READ.3.2.1 — Missing-root refusal

### C-READ.3.2.1 — Missing-root refusal
Stamp: BUILT    Source: [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Refuses commit until every referenced root exists. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — A `reads` ID with no corresponding sealed root. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Refuses commit until every referenced root exists. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — No reading append with that missing reference. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Stops the append; the roots remain unchanged. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3.2 — Referenced-root verification | A `reads` ID with no corresponding sealed root. | Refuses commit until every referenced root exists. | No reading append with that missing reference. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.3.3 — Committed-key rejection
Stamp: BUILT    Source: [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema]

ALONE
- What it is: BUILT — Rejects an already-committed key; the operation key is separate from record ID. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema]
- Takes in: BUILT — `idempotency_key` and existing committed keys in the target store. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema]
- Does: BUILT — Rejects an already-committed key; the operation key is separate from record ID. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema]
- Gives out: BUILT — No second append for the committed key. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: BUILT — C-READ.3.3.1 — Already-committed-key outcome: Rejects the duplicate operation key. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3 — append_reading | `idempotency_key` and existing committed keys in the target store. | Rejects an already-committed key; the operation key is separate from record ID. | No second append for the committed key. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema] |

SUB-PARTS: C-READ.3.3.1 — Already-committed-key outcome

### C-READ.3.3.1 — Already-committed-key outcome
Stamp: BUILT    Source: [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

ALONE
- What it is: BUILT — Rejects the duplicate operation key. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Takes in: BUILT — A key already committed in the target store. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Does: BUILT — Rejects the duplicate operation key. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Gives out: BUILT — No duplicate reading appended. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]
- Must never: NOT DECIDED
- Fails closed by: BUILT — Stops this duplicate append. [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3.3 — Committed-key rejection | A key already committed in the target store. | Rejects the duplicate operation key. | No duplicate reading appended. | [V10 §6B / READING record schema] [V10 §6A / SCHEMA CONSTRAINTS] |

SUB-PARTS: NONE

### C-READ.3.4 — Atomic append
Stamp: BUILT    Source: [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema] [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]

ALONE
- What it is: BUILT — Appends atomically, with flush and fsync, preserving append-only records. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema] [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]
- Takes in: BUILT — A shape-valid reading whose root references and key have passed. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema] [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]
- Does: BUILT — Appends atomically, with flush and fsync, preserving append-only records. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema] [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]
- Gives out: BUILT — A committed reading. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema] [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: BUILT — C-READ.3.4.1 — Reading append flush: Flushes the append as part of the atomic reading write. [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]
- Fed by: BUILT — C-READ.3.4.2 — Reading append fsync: Uses fsync as part of the atomic reading write. [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3 — append_reading | A shape-valid reading whose root references and key have passed. | Appends atomically, with flush and fsync, preserving append-only records. | A committed reading. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema] [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK] |

SUB-PARTS: C-READ.3.4.1 — Reading append flush; C-READ.3.4.2 — Reading append fsync

### C-READ.3.4.1 — Reading append flush
Stamp: BUILT    Source: [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]

ALONE
- What it is: BUILT — Flushes the append as part of the atomic reading write. [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]
- Takes in: BUILT — The reading append. [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]
- Does: BUILT — Flushes the append as part of the atomic reading write. [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]
- Gives out: BUILT — The append has been flushed. [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3.4 — Atomic append | The reading append. | Flushes the append as part of the atomic reading write. | The append has been flushed. | [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK] |

SUB-PARTS: NONE

### C-READ.3.4.2 — Reading append fsync
Stamp: BUILT    Source: [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]

ALONE
- What it is: BUILT — Uses fsync as part of the atomic reading write. [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]
- Takes in: BUILT — The reading append. [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]
- Does: BUILT — Uses fsync as part of the atomic reading write. [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]
- Gives out: BUILT — The append has passed the writer’s fsync operation. [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3.4 — Atomic append | The reading append. | Uses fsync as part of the atomic reading write. | The append has passed the writer’s fsync operation. | [V10 / THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK] |

SUB-PARTS: NONE

### C-READ.3.5 — Destination routing
Stamp: BUILT    Source: [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema]

ALONE
- What it is: BUILT — Routes the append to the chosen readings destination; the built A/B output target is quarantine. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema]
- Takes in: BUILT — The supplied target path. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema]
- Does: BUILT — Routes the append to the chosen readings destination; the built A/B output target is quarantine. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema]
- Gives out: BUILT — A reading in the designated readings file, never mixed into roots. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3 — append_reading | The supplied target path. | Routes the append to the chosen readings destination; the built A/B output target is quarantine. | A reading in the designated readings file, never mixed into roots. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / READING record schema] |

SUB-PARTS: NONE

### C-READ.3.6 — Shared write boundary
Stamp: DESIGNED    Source: [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [CR §1C — ACCRETIVE STORE PROHIBITIONS]

ALONE
- What it is: DESIGNED — Uses `append_reading()` and the validated functions in `nh_accretive_store.py`; direct opens for append or overwrite are prohibited. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [CR §1C — ACCRETIVE STORE PROHIBITIONS]
- Takes in: DESIGNED — Any reading write request. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [CR §1C — ACCRETIVE STORE PROHIBITIONS]
- Does: DESIGNED — Uses `append_reading()` and the validated functions in `nh_accretive_store.py`; direct opens for append or overwrite are prohibited. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [CR §1C — ACCRETIVE STORE PROHIBITIONS]
- Gives out: DESIGNED — One designated reading write boundary. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [CR §1C — ACCRETIVE STORE PROHIBITIONS]
- Must never: DESIGNED — Use a parallel write-validation implementation or direct file writes. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [CR §1C — ACCRETIVE STORE PROHIBITIONS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.3 — append_reading | Any reading write request. | Uses `append_reading()` and the validated functions in `nh_accretive_store.py`; direct opens for append or overwrite are prohibited. | One designated reading write boundary. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [CR §1C — ACCRETIVE STORE PROHIBITIONS] |

SUB-PARTS: NONE

### C-READ.3.7 — New-root worker reading-write handoff
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record]

ALONE
- What it is: DESIGNED — The designed caller handoff from the new-root worker into the built reading writer. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record]
- Takes in: DESIGNED — The new-root operation’s `enqueue_key`, the current `pass_id`, accepted reading data or a separate honest fallback reading, and retrieval audit content. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record]
- Does: DESIGNED — Computes `reading_idempotency_key = stable_hash(enqueue_key + "reading_v1")`; checks for an existing committed reading; otherwise assembles the twelve-field record, validates it and writes quarantine. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record]
- Gives out: DESIGNED — A newly written or recovered `reading_id` for the following worker checkpoint. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record]
- Must never: DESIGNED — Derive the key from random `job_id`; add `reading_idempotency_key` as a thirteenth reading field; write production here. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-READ.3.7.1 — Stable new-root reading key: Computes `stable_hash(enqueue_key + "reading_v1")`; sets the existing reading-record `idempotency_key` to this result. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Fed by: DESIGNED — C-READ.3.7.2 — Pass-specific producer configuration: Sets `produced_by.config.pass_id` to this attempt’s `pass_id`. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Fed by: DESIGNED — C-READ.3.7.3 — Retrieval audit carriage: Sets `produced_by.retrieval_inputs` to the mode, parameters, system/model/index version, exact roots, scores/positions, exclusions/truncation and execution timestamp. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Fed by: DESIGNED — C-READ.3.7.4 — Existing-reading recovery: Recovers its `reading_id`, does not rewrite the reading, restores missing queue checkpoints with that ID, and continues at the next correct stage; `recovery_of_pass_id` is unchanged. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Fed by: DESIGNED — C-READ.3.7.5 — New-reading commit: Validates and calls `append_reading()` with the quarantine destination `.nh_readings_quarantine.jsonl`. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Fed by: DESIGNED — C-READ.3.7.6 — reading_written checkpoint: Appends `job_stage_event` with `stage="reading_written"` and `reading_id` to `.nh_reading_queue.jsonl`; the job remains `in_progress`. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Fed by: DESIGNED — C-READ.3.7.7 — Worker write failure: Closes the pass with `event_type="failed"`, `failure_stage="write"`, `is_technical_and_potentially_retryable=true`; the queue job stays `in_progress`; releases the OS lock cleanly and stops. [V10 §7G-A / Step 5 — Write the reading record]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.3 — append_reading | The stable operation key and pass-specific data. | Submits at most one reading per operation across pass attempts. | A new or recovered reading identity. | [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] |

SUB-PARTS: C-READ.3.7.1 — Stable new-root reading key; C-READ.3.7.2 — Pass-specific producer configuration; C-READ.3.7.3 — Retrieval audit carriage; C-READ.3.7.4 — Existing-reading recovery; C-READ.3.7.5 — New-reading commit; C-READ.3.7.6 — reading_written checkpoint; C-READ.3.7.7 — Worker write failure

### C-READ.3.7.1 — Stable new-root reading key
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]

ALONE
- What it is: DESIGNED — Computes `stable_hash(enqueue_key + "reading_v1")`; sets the existing reading-record `idempotency_key` to this result. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Takes in: DESIGNED — `enqueue_key`. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Does: DESIGNED — Computes `stable_hash(enqueue_key + "reading_v1")`; sets the existing reading-record `idempotency_key` to this result. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Gives out: DESIGNED — A stable key across attempts and accidental duplicate jobs. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.3.7 — New-root worker reading-write handoff | `enqueue_key`. | Computes `stable_hash(enqueue_key + "reading_v1")`; sets the existing reading-record `idempotency_key` to this result. | A stable key across attempts and accidental duplicate jobs. | [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`] |

SUB-PARTS: NONE

### C-READ.3.7.2 — Pass-specific producer configuration
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]

ALONE
- What it is: DESIGNED — Sets `produced_by.config.pass_id` to this attempt’s `pass_id`. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Takes in: DESIGNED — The current pass attempt. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Does: DESIGNED — Sets `produced_by.config.pass_id` to this attempt’s `pass_id`. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Gives out: DESIGNED — Attempt provenance separate from operation identity. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.3.7 — New-root worker reading-write handoff | The current pass attempt. | Sets `produced_by.config.pass_id` to this attempt’s `pass_id`. | Attempt provenance separate from operation identity. | [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`] |

SUB-PARTS: NONE

### C-READ.3.7.3 — Retrieval audit carriage
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]

ALONE
- What it is: DESIGNED — Sets `produced_by.retrieval_inputs` to the mode, parameters, system/model/index version, exact roots, scores/positions, exclusions/truncation and execution timestamp. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Takes in: DESIGNED — The §7F retrieval audit. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Does: DESIGNED — Sets `produced_by.retrieval_inputs` to the mode, parameters, system/model/index version, exact roots, scores/positions, exclusions/truncation and execution timestamp. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Gives out: DESIGNED — The actual retrieval provenance used for this reading. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.3.7 — New-root worker reading-write handoff | The §7F retrieval audit. | Sets `produced_by.retrieval_inputs` to the mode, parameters, system/model/index version, exact roots, scores/positions, exclusions/truncation and execution timestamp. | The actual retrieval provenance used for this reading. | [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`] |

SUB-PARTS: NONE

### C-READ.3.7.4 — Existing-reading recovery
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]

ALONE
- What it is: DESIGNED — Recovers its `reading_id`, does not rewrite the reading, restores missing queue checkpoints with that ID, and continues at the next correct stage; `recovery_of_pass_id` is unchanged. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Takes in: DESIGNED — A committed reading matching the computed key. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Does: DESIGNED — Recovers its `reading_id`, does not rewrite the reading, restores missing queue checkpoints with that ID, and continues at the next correct stage; `recovery_of_pass_id` is unchanged. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Gives out: DESIGNED — The existing reading identity and repaired missing checkpoints. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.3.7 — New-root worker reading-write handoff | A committed reading matching the computed key. | Recovers its `reading_id`, does not rewrite the reading, restores missing queue checkpoints with that ID, and continues at the next correct stage; `recovery_of_pass_id` is unchanged. | The existing reading identity and repaired missing checkpoints. | [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`] |

SUB-PARTS: NONE

### C-READ.3.7.5 — New-reading commit
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]

ALONE
- What it is: DESIGNED — Validates and calls `append_reading()` with the quarantine destination `.nh_readings_quarantine.jsonl`. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Takes in: DESIGNED — No reading with the computed key; assembled twelve-field record. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Does: DESIGNED — Validates and calls `append_reading()` with the quarantine destination `.nh_readings_quarantine.jsonl`. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Gives out: DESIGNED — A newly committed quarantine reading. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.3.7 — New-root worker reading-write handoff | No reading with the computed key; assembled twelve-field record. | Validates and calls `append_reading()` with the quarantine destination `.nh_readings_quarantine.jsonl`. | A newly committed quarantine reading. | [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`] |

SUB-PARTS: NONE

### C-READ.3.7.6 — reading_written checkpoint
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]

ALONE
- What it is: DESIGNED — Appends `job_stage_event` with `stage="reading_written"` and `reading_id` to `.nh_reading_queue.jsonl`; the job remains `in_progress`. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Takes in: DESIGNED — A new or recovered `reading_id`. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Does: DESIGNED — Appends `job_stage_event` with `stage="reading_written"` and `reading_id` to `.nh_reading_queue.jsonl`; the job remains `in_progress`. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Gives out: DESIGNED — The durable reading-written checkpoint. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-READ.3.7.6.1 — Reading-written handoff — stage: carries this member as part of the containing record. [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Fed by: DESIGNED — C-READ.3.7.6.2 — Reading-written handoff — reading_id: carries this member as part of the containing record. [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.3.7 — New-root worker reading-write handoff | A new or recovered `reading_id`. | Appends `job_stage_event` with `stage="reading_written"` and `reading_id` to `.nh_reading_queue.jsonl`; the job remains `in_progress`. | The durable reading-written checkpoint. | [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / Step 5 — Write the reading record] [V10 §7G-A / Step 5A — Checkpoint: `reading_written`] |

SUB-PARTS: C-READ.3.7.6.1 — Reading-written handoff — stage; C-READ.3.7.6.2 — Reading-written handoff — reading_id

### C-READ.3.7.6.1 — Reading-written handoff — stage
Stamp: DESIGNED    Source: [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]

ALONE
- What it is: DESIGNED — The Reading-written handoff — stage member or named content item carried within reading_written checkpoint. [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Takes in: DESIGNED — `stage="reading_written"`. [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Does: DESIGNED — Identifies the reading-written stage in the worker’s checkpoint. [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Gives out: DESIGNED — `stage="reading_written"`. [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.3.7.6 — reading_written checkpoint | `stage="reading_written"`. | Identifies the reading-written stage in the worker’s checkpoint. | `stage="reading_written"`. | [V10 §7G-A / Step 5A — Checkpoint: `reading_written`] |

SUB-PARTS: NONE

### C-READ.3.7.6.2 — Reading-written handoff — reading_id
Stamp: DESIGNED    Source: [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]

ALONE
- What it is: DESIGNED — The Reading-written handoff — reading_id member or named content item carried within reading_written checkpoint. [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Takes in: DESIGNED — The new or recovered `reading_id`. [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Does: DESIGNED — Points the checkpoint to the committed reading without writing another reading. [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Gives out: DESIGNED — The new or recovered `reading_id`. [V10 §7G-A / Step 5A — Checkpoint: `reading_written`]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.3.7.6 — reading_written checkpoint | The new or recovered `reading_id`. | Points the checkpoint to the committed reading without writing another reading. | The new or recovered `reading_id`. | [V10 §7G-A / Step 5A — Checkpoint: `reading_written`] |

SUB-PARTS: NONE

### C-READ.3.7.7 — Worker write failure
Stamp: DESIGNED    Source: [V10 §7G-A / Step 5 — Write the reading record]

ALONE
- What it is: DESIGNED — Closes the pass with `event_type="failed"`, `failure_stage="write"`, `is_technical_and_potentially_retryable=true`; the queue job stays `in_progress`; releases the OS lock cleanly and stops. [V10 §7G-A / Step 5 — Write the reading record]
- Takes in: DESIGNED — A failure writing the reading. [V10 §7G-A / Step 5 — Write the reading record]
- Does: DESIGNED — Closes the pass with `event_type="failed"`, `failure_stage="write"`, `is_technical_and_potentially_retryable=true`; the queue job stays `in_progress`; releases the OS lock cleanly and stops. [V10 §7G-A / Step 5 — Write the reading record]
- Gives out: DESIGNED — A failed pass and retained in-progress job, not a completed reading pass. [V10 §7G-A / Step 5 — Write the reading record]
- Must never: NOT DECIDED
- Fails closed by: DESIGNED — Stops this pass after recording the technical write failure. [V10 §7G-A / Step 5 — Write the reading record]

TOGETHER
- Fed by: DESIGNED — C-READ.3.7.7.1 — Write-failure event_type: carries this member as part of the containing record. [V10 §7G-A / Step 5 — Write the reading record]
- Fed by: DESIGNED — C-READ.3.7.7.2 — Write-failure failure_stage: carries this member as part of the containing record. [V10 §7G-A / Step 5 — Write the reading record]
- Fed by: DESIGNED — C-READ.3.7.7.3 — Write-failure is_technical_and_potentially_retryable: carries this member as part of the containing record. [V10 §7G-A / Step 5 — Write the reading record]
- Fed by: DESIGNED — C-READ.3.7.7.4 — Write-failure job status: carries this member as part of the containing record. [V10 §7G-A / Step 5 — Write the reading record]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.3.7 — New-root worker reading-write handoff | A failure writing the reading. | Closes the pass with `event_type="failed"`, `failure_stage="write"`, `is_technical_and_potentially_retryable=true`; the queue job stays `in_progress`; releases the OS lock cleanly and stops. | A failed pass and retained in-progress job, not a completed reading pass. | [V10 §7G-A / Step 5 — Write the reading record] |

SUB-PARTS: C-READ.3.7.7.1 — Write-failure event_type; C-READ.3.7.7.2 — Write-failure failure_stage; C-READ.3.7.7.3 — Write-failure is_technical_and_potentially_retryable; C-READ.3.7.7.4 — Write-failure job status

### C-READ.3.7.7.1 — Write-failure event_type
Stamp: DESIGNED    Source: [V10 §7G-A / Step 5 — Write the reading record]

ALONE
- What it is: DESIGNED — The Write-failure event_type member or named content item carried within Worker write failure. [V10 §7G-A / Step 5 — Write the reading record]
- Takes in: DESIGNED — `"failed"`. [V10 §7G-A / Step 5 — Write the reading record]
- Does: DESIGNED — Carries this exact write-failure outcome value. [V10 §7G-A / Step 5 — Write the reading record]
- Gives out: DESIGNED — `"failed"`. [V10 §7G-A / Step 5 — Write the reading record]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.3.7.7 — Worker write failure | `"failed"`. | Carries this exact write-failure outcome value. | `"failed"`. | [V10 §7G-A / Step 5 — Write the reading record] |

SUB-PARTS: NONE

### C-READ.3.7.7.2 — Write-failure failure_stage
Stamp: DESIGNED    Source: [V10 §7G-A / Step 5 — Write the reading record]

ALONE
- What it is: DESIGNED — The Write-failure failure_stage member or named content item carried within Worker write failure. [V10 §7G-A / Step 5 — Write the reading record]
- Takes in: DESIGNED — `"write"`. [V10 §7G-A / Step 5 — Write the reading record]
- Does: DESIGNED — Carries this exact write-failure outcome value. [V10 §7G-A / Step 5 — Write the reading record]
- Gives out: DESIGNED — `"write"`. [V10 §7G-A / Step 5 — Write the reading record]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.3.7.7 — Worker write failure | `"write"`. | Carries this exact write-failure outcome value. | `"write"`. | [V10 §7G-A / Step 5 — Write the reading record] |

SUB-PARTS: NONE

### C-READ.3.7.7.3 — Write-failure is_technical_and_potentially_retryable
Stamp: DESIGNED    Source: [V10 §7G-A / Step 5 — Write the reading record]

ALONE
- What it is: DESIGNED — The Write-failure is_technical_and_potentially_retryable member or named content item carried within Worker write failure. [V10 §7G-A / Step 5 — Write the reading record]
- Takes in: DESIGNED — `true`. [V10 §7G-A / Step 5 — Write the reading record]
- Does: DESIGNED — Carries this exact write-failure outcome value. [V10 §7G-A / Step 5 — Write the reading record]
- Gives out: DESIGNED — `true`. [V10 §7G-A / Step 5 — Write the reading record]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.3.7.7 — Worker write failure | `true`. | Carries this exact write-failure outcome value. | `true`. | [V10 §7G-A / Step 5 — Write the reading record] |

SUB-PARTS: NONE

### C-READ.3.7.7.4 — Write-failure job status
Stamp: DESIGNED    Source: [V10 §7G-A / Step 5 — Write the reading record]

ALONE
- What it is: DESIGNED — The Write-failure job status member or named content item carried within Worker write failure. [V10 §7G-A / Step 5 — Write the reading record]
- Takes in: DESIGNED — `"in_progress"`. [V10 §7G-A / Step 5 — Write the reading record]
- Does: DESIGNED — Carries this exact write-failure outcome value. [V10 §7G-A / Step 5 — Write the reading record]
- Gives out: DESIGNED — `"in_progress"`. [V10 §7G-A / Step 5 — Write the reading record]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.3.7.7 — Worker write failure | `"in_progress"`. | Carries this exact write-failure outcome value. | `"in_progress"`. | [V10 §7G-A / Step 5 — Write the reading record] |

SUB-PARTS: NONE

### C-READ.4 — Quarantine readings destination
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §5] [V10 §6B / ON DISK NOW]

ALONE
- What it is: BUILT — The separate test readings file `.nh_readings_quarantine.jsonl`. [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §5] [V10 §6B / ON DISK NOW]
- Takes in: BUILT — Validated engine A and engine B gold-run readings through the reading writer. [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §5] [V10 §6B / ON DISK NOW]
- Does: BUILT — Holds the built engines’ test output separately from the roots and the absent production readings store. [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §5] [V10 §6B / ON DISK NOW]
- Gives out: BUILT — Preserved quarantine test readings. [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §5] [V10 §6B / ON DISK NOW]
- Must never: BUILT — Treat the built quarantine store as evidence that production readings already exist. [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §5] [V10 §6B / ON DISK NOW]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-READ.4.1 — Production remains absent: Keeps `.nh_readings_store.jsonl` absent until production authorization; quarantine output does not establish production readiness. [V10 §5] [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ.3 — append_reading | A validated reading after root/key checks. | Appends through the reading writer. | A new quarantine reading. | [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] [V10 §5] |
| 2 · BUILT | C-READ — Reading record, validator, writer (§6B) | Engine A/B test readings. | Keeps test readings in the separate quarantine destination. | Inspectable quarantine output. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B] |

SUB-PARTS: C-READ.4.1 — Production remains absent

### C-READ.4.1 — Production remains absent
Stamp: DESIGNED    Source: [V10 §5] [V10 §6A / PRODUCTION READINGS AUTHORIZATION]

ALONE
- What it is: DESIGNED — Keeps `.nh_readings_store.jsonl` absent until production authorization; quarantine output does not establish production readiness. [V10 §5] [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Takes in: DESIGNED — The roots/quarantine/production file separation. [V10 §5] [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Does: DESIGNED — Keeps `.nh_readings_store.jsonl` absent until production authorization; quarantine output does not establish production readiness. [V10 §5] [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Gives out: DESIGNED — Test output remains separate. [V10 §5] [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Must never: DESIGNED — Create production as an engine-test side effect. [V10 §5] [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.4 — Quarantine readings destination | The roots/quarantine/production file separation. | Keeps `.nh_readings_store.jsonl` absent until production authorization; quarantine output does not establish production readiness. | Test output remains separate. | [V10 §5] [V10 §6A / PRODUCTION READINGS AUTHORIZATION] |

SUB-PARTS: NONE

### C-READ.5 — Production readings authorization
Stamp: DESIGNED    Source: [V10 §6A / PRODUCTION READINGS AUTHORIZATION] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]

ALONE
- What it is: DESIGNED — The two required protections before any production reading write. [V10 §6A / PRODUCTION READINGS AUTHORIZATION] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]
- Takes in: DESIGNED — The physical marker `.nh_readings_production_authorized` and explicit approval for the particular production write path/session. [V10 §6A / PRODUCTION READINGS AUTHORIZATION] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]
- Does: DESIGNED — Requires both protections. Marker presence alone is insufficient; removing it disables future production writes without changing stored readings. [V10 §6A / PRODUCTION READINGS AUTHORIZATION] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]
- Gives out: DESIGNED — Permission for the specifically approved production write scope only when both protections exist. [V10 §6A / PRODUCTION READINGS AUTHORIZATION] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]
- Must never: DESIGNED — Create the marker automatically; infer authorization from marker presence alone; silently create `.nh_readings_store.jsonl`. [V10 §6A / PRODUCTION READINGS AUTHORIZATION] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]
- Must never: DESIGNED — Treat these two authorization protections as proof that promotion evidence exists or that the C2/B16 production prerequisites have passed. [MAP C-READ] [V10 §11 item 27]
- Fails closed by: DESIGNED — The designed marker gate refuses production writing when the marker is absent; V10 does not claim that this check is already implemented. [V10 §6A / PRODUCTION READINGS AUTHORIZATION] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-READ.5.1 — Physical production marker: Requires the marker created deliberately by Ness; no automated code may create, detect-and-create or conditionally create it. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Gated by: DESIGNED — C-READ.5.2 — Specific production-write approval: Requires approval covering the production store, exact writer, source of readings, schema version, promotion-review evidence, duplicate/idempotency handling, rollback handling, and completed quarantine tests/manual inspection. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ — Reading record, validator, writer (§6B) | A production-directed write. | Checks the two required protections. | No production write outside the authorized scope. | [V10 §6A / PRODUCTION READINGS AUTHORIZATION] |
| 2 · DESIGNED | C-READ.3 — append_reading | A production-directed append. | Requires both protections before production use. | Production remains blocked when a protection is absent. | [V10 §6A / PRODUCTION READINGS AUTHORIZATION] |

SUB-PARTS: C-READ.5.1 — Physical production marker; C-READ.5.2 — Specific production-write approval

### C-READ.5.1 — Physical production marker
Stamp: DESIGNED    Source: [V10 §6A / PRODUCTION READINGS AUTHORIZATION]

ALONE
- What it is: DESIGNED — Requires the marker created deliberately by Ness; no automated code may create, detect-and-create or conditionally create it. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Takes in: DESIGNED — The presence or absence of `.nh_readings_production_authorized`. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Does: DESIGNED — Requires the marker created deliberately by Ness; no automated code may create, detect-and-create or conditionally create it. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Gives out: DESIGNED — One necessary production-write protection. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Must never: DESIGNED — Generate the marker automatically. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Fails closed by: DESIGNED — The designed production gate refuses writing if the marker is absent. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]

TOGETHER
- Fed by: DESIGNED — C-READ.5.1.1 — Marker removal: Disables future production writes and preserves readings already stored. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.5 — Production readings authorization | The presence or absence of `.nh_readings_production_authorized`. | Requires the marker created deliberately by Ness; no automated code may create, detect-and-create or conditionally create it. | One necessary production-write protection. | [V10 §6A / PRODUCTION READINGS AUTHORIZATION] |

SUB-PARTS: C-READ.5.1.1 — Marker removal

### C-READ.5.2 — Specific production-write approval
Stamp: DESIGNED    Source: [V10 §6A / PRODUCTION READINGS AUTHORIZATION]

ALONE
- What it is: DESIGNED — Requires approval covering the production store, exact writer, source of readings, schema version, promotion-review evidence, duplicate/idempotency handling, rollback handling, and completed quarantine tests/manual inspection. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Takes in: DESIGNED — Explicit approval identifying the production write scope. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Does: DESIGNED — Requires approval covering the production store, exact writer, source of readings, schema version, promotion-review evidence, duplicate/idempotency handling, rollback handling, and completed quarantine tests/manual inspection. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Gives out: DESIGNED — Approval specific to the write path and session, distinct from marker existence. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Must never: DESIGNED — Treat the marker as approval for a particular write session. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-READ.5.2.1 — Approval scope — production store: carries this member as part of the containing record. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Fed by: DESIGNED — C-READ.5.2.2 — Approval scope — exact writer function: carries this member as part of the containing record. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Fed by: DESIGNED — C-READ.5.2.3 — Approval scope — source of the readings: carries this member as part of the containing record. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Fed by: DESIGNED — C-READ.5.2.4 — Approval scope — schema version: carries this member as part of the containing record. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Fed by: DESIGNED — C-READ.5.2.5 — Approval scope — promotion-review evidence: carries this member as part of the containing record. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Fed by: DESIGNED — C-READ.5.2.6 — Approval scope — duplicate and idempotency handling: carries this member as part of the containing record. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Fed by: DESIGNED — C-READ.5.2.7 — Approval scope — rollback handling: carries this member as part of the containing record. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Fed by: DESIGNED — C-READ.5.2.8 — Approval scope — quarantine tests and manual inspection complete: carries this member as part of the containing record. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.5 — Production readings authorization | Explicit approval identifying the production write scope. | Requires approval covering the production store, exact writer, source of readings, schema version, promotion-review evidence, duplicate/idempotency handling, rollback handling, and completed quarantine tests/manual inspection. | Approval specific to the write path and session, distinct from marker existence. | [V10 §6A / PRODUCTION READINGS AUTHORIZATION] |

SUB-PARTS: C-READ.5.2.1 — Approval scope — production store; C-READ.5.2.2 — Approval scope — exact writer function; C-READ.5.2.3 — Approval scope — source of the readings; C-READ.5.2.4 — Approval scope — schema version; C-READ.5.2.5 — Approval scope — promotion-review evidence; C-READ.5.2.6 — Approval scope — duplicate and idempotency handling; C-READ.5.2.7 — Approval scope — rollback handling; C-READ.5.2.8 — Approval scope — quarantine tests and manual inspection complete

### C-READ.5.2.1 — Approval scope — production store
Stamp: DESIGNED    Source: [V10 §6A / PRODUCTION READINGS AUTHORIZATION]

ALONE
- What it is: DESIGNED — The Approval scope — production store member or named content item carried within Specific production-write approval. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Takes in: DESIGNED — Required approval scope item. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Does: DESIGNED — The approval identifies production store. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Gives out: DESIGNED — Required approval scope item. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Must never: DESIGNED — Omit the required member. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.5.2 — Specific production-write approval | Required approval scope item. | The approval identifies production store. | Required approval scope item. | [V10 §6A / PRODUCTION READINGS AUTHORIZATION] |

SUB-PARTS: NONE

### C-READ.5.2.2 — Approval scope — exact writer function
Stamp: DESIGNED    Source: [V10 §6A / PRODUCTION READINGS AUTHORIZATION]

ALONE
- What it is: DESIGNED — The Approval scope — exact writer function member or named content item carried within Specific production-write approval. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Takes in: DESIGNED — Required approval scope item. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Does: DESIGNED — The approval identifies exact writer function. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Gives out: DESIGNED — Required approval scope item. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Must never: DESIGNED — Omit the required member. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.5.2 — Specific production-write approval | Required approval scope item. | The approval identifies exact writer function. | Required approval scope item. | [V10 §6A / PRODUCTION READINGS AUTHORIZATION] |

SUB-PARTS: NONE

### C-READ.5.2.3 — Approval scope — source of the readings
Stamp: DESIGNED    Source: [V10 §6A / PRODUCTION READINGS AUTHORIZATION]

ALONE
- What it is: DESIGNED — The Approval scope — source of the readings member or named content item carried within Specific production-write approval. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Takes in: DESIGNED — Required approval scope item. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Does: DESIGNED — The approval identifies source of the readings. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Gives out: DESIGNED — Required approval scope item. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Must never: DESIGNED — Omit the required member. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.5.2 — Specific production-write approval | Required approval scope item. | The approval identifies source of the readings. | Required approval scope item. | [V10 §6A / PRODUCTION READINGS AUTHORIZATION] |

SUB-PARTS: NONE

### C-READ.5.2.4 — Approval scope — schema version
Stamp: DESIGNED    Source: [V10 §6A / PRODUCTION READINGS AUTHORIZATION]

ALONE
- What it is: DESIGNED — The Approval scope — schema version member or named content item carried within Specific production-write approval. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Takes in: DESIGNED — Required approval scope item. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Does: DESIGNED — The approval identifies schema version. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Gives out: DESIGNED — Required approval scope item. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Must never: DESIGNED — Omit the required member. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.5.2 — Specific production-write approval | Required approval scope item. | The approval identifies schema version. | Required approval scope item. | [V10 §6A / PRODUCTION READINGS AUTHORIZATION] |

SUB-PARTS: NONE

### C-READ.5.2.5 — Approval scope — promotion-review evidence
Stamp: DESIGNED    Source: [V10 §6A / PRODUCTION READINGS AUTHORIZATION]

ALONE
- What it is: DESIGNED — The Approval scope — promotion-review evidence member or named content item carried within Specific production-write approval. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Takes in: DESIGNED — Required approval scope item. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Does: DESIGNED — The approval identifies promotion-review evidence. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Gives out: DESIGNED — Required approval scope item. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Must never: DESIGNED — Omit the required member. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.5.2 — Specific production-write approval | Required approval scope item. | The approval identifies promotion-review evidence. | Required approval scope item. | [V10 §6A / PRODUCTION READINGS AUTHORIZATION] |

SUB-PARTS: NONE

### C-READ.5.2.6 — Approval scope — duplicate and idempotency handling
Stamp: DESIGNED    Source: [V10 §6A / PRODUCTION READINGS AUTHORIZATION]

ALONE
- What it is: DESIGNED — The Approval scope — duplicate and idempotency handling member or named content item carried within Specific production-write approval. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Takes in: DESIGNED — Required approval scope item. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Does: DESIGNED — The approval identifies duplicate and idempotency handling. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Gives out: DESIGNED — Required approval scope item. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Must never: DESIGNED — Omit the required member. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.5.2 — Specific production-write approval | Required approval scope item. | The approval identifies duplicate and idempotency handling. | Required approval scope item. | [V10 §6A / PRODUCTION READINGS AUTHORIZATION] |

SUB-PARTS: NONE

### C-READ.5.2.7 — Approval scope — rollback handling
Stamp: DESIGNED    Source: [V10 §6A / PRODUCTION READINGS AUTHORIZATION]

ALONE
- What it is: DESIGNED — The Approval scope — rollback handling member or named content item carried within Specific production-write approval. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Takes in: DESIGNED — Required approval scope item. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Does: DESIGNED — The approval identifies rollback handling. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Gives out: DESIGNED — Required approval scope item. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Must never: DESIGNED — Omit the required member. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.5.2 — Specific production-write approval | Required approval scope item. | The approval identifies rollback handling. | Required approval scope item. | [V10 §6A / PRODUCTION READINGS AUTHORIZATION] |

SUB-PARTS: NONE

### C-READ.5.2.8 — Approval scope — quarantine tests and manual inspection complete
Stamp: DESIGNED    Source: [V10 §6A / PRODUCTION READINGS AUTHORIZATION]

ALONE
- What it is: DESIGNED — The Approval scope — quarantine tests and manual inspection complete member or named content item carried within Specific production-write approval. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Takes in: DESIGNED — Required approval scope item. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Does: DESIGNED — The approval identifies quarantine tests and manual inspection complete. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Gives out: DESIGNED — Required approval scope item. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Must never: DESIGNED — Omit the required member. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.5.2 — Specific production-write approval | Required approval scope item. | The approval identifies quarantine tests and manual inspection complete. | Required approval scope item. | [V10 §6A / PRODUCTION READINGS AUTHORIZATION] |

SUB-PARTS: NONE

### C-READ.5.1.1 — Marker removal
Stamp: DESIGNED    Source: [V10 §6A / PRODUCTION READINGS AUTHORIZATION]

ALONE
- What it is: DESIGNED — Disables future production writes and preserves readings already stored. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Takes in: DESIGNED — A production marker that is removed. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Does: DESIGNED — Disables future production writes and preserves readings already stored. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Gives out: DESIGNED — Future production writes disabled; existing readings unchanged. [V10 §6A / PRODUCTION READINGS AUTHORIZATION]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.5.1 — Physical production marker | A production marker that is removed. | Disables future production writes and preserves readings already stored. | Future production writes disabled; existing readings unchanged. | [V10 §6A / PRODUCTION READINGS AUTHORIZATION] |

SUB-PARTS: NONE

### C-READ.6 — Reading operation records
Stamp: DESIGNED    Source: [MAP C-READ] [V10 §0B]

ALONE
- What it is: DESIGNED — Connected, append-only records of the reading boundary’s real operations. [MAP C-READ] [V10 §0B]
- Takes in: DESIGNED — Validation passes/failures, reading writes and idempotency rejections. [MAP C-READ] [V10 §0B]
- Does: DESIGNED — Records every validation pass/fail with reason, every quarantine or production write, and every idempotency rejection. Each real operation receives one log; creating that log does not recursively log itself. [MAP C-READ] [V10 §0B]
- Gives out: DESIGNED — Permanent connected operational records subject to privacy and identity authorization. [MAP C-READ] [V10 §0B]
- Must never: DESIGNED — Leave an operation silent, add evidence weight merely because it was logged, erase records, or start an automatic log-about-log chain. [MAP C-READ] [V10 §0B]
- Must never: DESIGNED — Expose raw Level 1 content or its physical location/access path; bypass identity/security authorization, TSC blockers or explicit compartment rules because a record exists. [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-READ.6.1 — Validation pass record: Records the validation pass and its reason. [MAP C-READ] [V10 §0B]
- Fed by: DESIGNED — C-READ.6.2 — Validation failure record: Records the validation failure and its reason. [MAP C-READ] [V10 §0B]
- Fed by: DESIGNED — C-READ.6.3 — Quarantine write record: Records the quarantine write. [MAP C-READ] [V10 §0B]
- Fed by: DESIGNED — C-READ.6.4 — Production write record: Records the production write; this design does not assert a built production store. [MAP C-READ] [V10 §0B]
- Fed by: DESIGNED — C-READ.6.5 — Idempotency rejection record: Records the idempotency rejection. [MAP C-READ] [V10 §0B]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): record existence does not grant access: visible-output eligibility and internal-use authorization remain separate, Level 1 stays inside its protected boundary, and separate influence-removal instructions remain binding. [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY] [MAP C-READ]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ — Reading record, validator, writer (§6B) | Reading-boundary operations. | Records each real operation once. | Connected permanent operation evidence. | [MAP C-READ] [V10 §0B] |
| 2 · DESIGNED | C-READ.8 — Read-only memory-health checks | A real memory-health examination. | Records the operation once and preserves its connections. | An operational record; inspected data remain unchanged. | [V10 §0B] |

SUB-PARTS: C-READ.6.1 — Validation pass record; C-READ.6.2 — Validation failure record; C-READ.6.3 — Quarantine write record; C-READ.6.4 — Production write record; C-READ.6.5 — Idempotency rejection record

### C-READ.6.1 — Validation pass record
Stamp: DESIGNED    Source: [MAP C-READ] [V10 §0B]

ALONE
- What it is: DESIGNED — Records the validation pass and its reason. [MAP C-READ] [V10 §0B]
- Takes in: DESIGNED — A successful reading validation. [MAP C-READ] [V10 §0B]
- Does: DESIGNED — Records the validation pass and its reason. [MAP C-READ] [V10 §0B]
- Gives out: DESIGNED — One permanent connected record of this real operation. [MAP C-READ] [V10 §0B]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.6 — Reading operation records | A successful reading validation. | Records the validation pass and its reason. | One permanent connected record of this real operation. | [MAP C-READ] [V10 §0B] |

SUB-PARTS: NONE

### C-READ.6.2 — Validation failure record
Stamp: DESIGNED    Source: [MAP C-READ] [V10 §0B]

ALONE
- What it is: DESIGNED — Records the validation failure and its reason. [MAP C-READ] [V10 §0B]
- Takes in: DESIGNED — A refused reading validation. [MAP C-READ] [V10 §0B]
- Does: DESIGNED — Records the validation failure and its reason. [MAP C-READ] [V10 §0B]
- Gives out: DESIGNED — One permanent connected record of this real operation. [MAP C-READ] [V10 §0B]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.6 — Reading operation records | A refused reading validation. | Records the validation failure and its reason. | One permanent connected record of this real operation. | [MAP C-READ] [V10 §0B] |

SUB-PARTS: NONE

### C-READ.6.3 — Quarantine write record
Stamp: DESIGNED    Source: [MAP C-READ] [V10 §0B]

ALONE
- What it is: DESIGNED — Records the quarantine write. [MAP C-READ] [V10 §0B]
- Takes in: DESIGNED — A committed quarantine reading write. [MAP C-READ] [V10 §0B]
- Does: DESIGNED — Records the quarantine write. [MAP C-READ] [V10 §0B]
- Gives out: DESIGNED — One permanent connected record of this real operation. [MAP C-READ] [V10 §0B]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.6 — Reading operation records | A committed quarantine reading write. | Records the quarantine write. | One permanent connected record of this real operation. | [MAP C-READ] [V10 §0B] |

SUB-PARTS: NONE

### C-READ.6.4 — Production write record
Stamp: DESIGNED    Source: [MAP C-READ] [V10 §0B]

ALONE
- What it is: DESIGNED — Records the production write; this design does not assert a built production store. [MAP C-READ] [V10 §0B]
- Takes in: DESIGNED — An authorized production reading write. [MAP C-READ] [V10 §0B]
- Does: DESIGNED — Records the production write; this design does not assert a built production store. [MAP C-READ] [V10 §0B]
- Gives out: DESIGNED — One permanent connected record of this real operation. [MAP C-READ] [V10 §0B]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.6 — Reading operation records | An authorized production reading write. | Records the production write; this design does not assert a built production store. | One permanent connected record of this real operation. | [MAP C-READ] [V10 §0B] |

SUB-PARTS: NONE

### C-READ.6.5 — Idempotency rejection record
Stamp: DESIGNED    Source: [MAP C-READ] [V10 §0B]

ALONE
- What it is: DESIGNED — Records the idempotency rejection. [MAP C-READ] [V10 §0B]
- Takes in: DESIGNED — An already-committed operation key rejected by the writer. [MAP C-READ] [V10 §0B]
- Does: DESIGNED — Records the idempotency rejection. [MAP C-READ] [V10 §0B]
- Gives out: DESIGNED — One permanent connected record of this real operation. [MAP C-READ] [V10 §0B]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-READ.6 — Reading operation records | An already-committed operation key rejected by the writer. | Records the idempotency rejection. | One permanent connected record of this real operation. | [MAP C-READ] [V10 §0B] |

SUB-PARTS: NONE

### C-READ.7 — Bootstrap reading context
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]

ALONE
- What it is: DECIDED-2026-09-25 — The input-side rule for early engine runs, preventing machine interpretations from automatically becoming their own corroboration. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Takes in: DECIDED-2026-09-25 — Raw roots, explicitly human-affirmed context, and any prior machine readings proposed as context. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Does: DECIDED-2026-09-25 — Early engine runs read mainly raw roots and explicitly human-affirmed material; prior machine-generated readings are excluded by default or clearly LOW-TRUST auxiliary context, never independent support. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Gives out: DECIDED-2026-09-25 — Bootstrap context with source evidence and prior interpretations kept distinguishable. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Must never: DECIDED-2026-09-25 — Automatically turn a machine reading into trusted context for the next reading and let it amplify itself. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DECIDED-2026-09-25 — C-READ.7.1 — Raw-root bootstrap basis: Uses raw roots as a main basis of early engine runs. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Fed by: DECIDED-2026-09-25 — C-READ.7.2 — Human-affirmed bootstrap context: Uses the approval only for context. The reading remains dated, weightless and revisable; affirmation is a story-layer event, not a truth button. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / WORDING GUARD]
- Fed by: DECIDED-2026-09-25 — C-READ.7.3 — Prior machine-reading treatment: Excludes them by default, or clearly marks them LOW-TRUST auxiliary context; neither branch supplies independent support. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Gated by: DECIDED-2026-09-25 — C-READ.7.4 — No automatic self-amplification: Prevents it from automatically becoming trusted context; the bootstrap rule acts before downstream lineage analysis. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ — Reading record, validator, writer (§6B) | Context proposed for an early reading. | Applies the raw-root/human-affirmed and low-trust boundaries. | Prior machine output gains no automatic independent evidential status. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE] |

SUB-PARTS: C-READ.7.1 — Raw-root bootstrap basis; C-READ.7.2 — Human-affirmed bootstrap context; C-READ.7.3 — Prior machine-reading treatment; C-READ.7.4 — No automatic self-amplification

### C-READ.7.1 — Raw-root bootstrap basis
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]

ALONE
- What it is: DECIDED-2026-09-25 — Uses raw roots as a main basis of early engine runs. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Takes in: DECIDED-2026-09-25 — Raw source roots. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Does: DECIDED-2026-09-25 — Uses raw roots as a main basis of early engine runs. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Gives out: DECIDED-2026-09-25 — Source-grounded early-reading context. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ.7 — Bootstrap reading context | Raw source roots. | Uses raw roots as a main basis of early engine runs. | Source-grounded early-reading context. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE] |

SUB-PARTS: NONE

### C-READ.7.2 — Human-affirmed bootstrap context
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / WORDING GUARD]

ALONE
- What it is: DECIDED-2026-09-25 — Uses the approval only for context. The reading remains dated, weightless and revisable; affirmation is a story-layer event, not a truth button. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / WORDING GUARD]
- Takes in: DECIDED-2026-09-25 — Material explicitly approved by Ness for use as context. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / WORDING GUARD]
- Does: DECIDED-2026-09-25 — Uses the approval only for context. The reading remains dated, weightless and revisable; affirmation is a story-layer event, not a truth button. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / WORDING GUARD]
- Gives out: DECIDED-2026-09-25 — Context-approved material that remains an interpretation. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / WORDING GUARD]
- Must never: DECIDED-2026-09-25 — Silently turn affirmed-for-context into affirmed-as-true. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / WORDING GUARD]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ.7 — Bootstrap reading context | Material explicitly approved by Ness for use as context. | Uses the approval only for context. The reading remains dated, weightless and revisable; affirmation is a story-layer event, not a truth button. | Context-approved material that remains an interpretation. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / WORDING GUARD] |

SUB-PARTS: NONE

### C-READ.7.3 — Prior machine-reading treatment
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]

ALONE
- What it is: DECIDED-2026-09-25 — Excludes them by default, or clearly marks them LOW-TRUST auxiliary context; neither branch supplies independent support. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Takes in: DECIDED-2026-09-25 — Prior machine-generated readings proposed for early-run context. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Does: DECIDED-2026-09-25 — Excludes them by default, or clearly marks them LOW-TRUST auxiliary context; neither branch supplies independent support. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Gives out: DECIDED-2026-09-25 — Excluded material or explicitly low-trust auxiliary context. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Must never: DECIDED-2026-09-25 — Count a prior machine reading as independent support for the interpretation that produced it. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DECIDED-2026-09-25 — C-READ.7.3.1 — Default exclusion: Excludes it from early-run context by default. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Fed by: DECIDED-2026-09-25 — C-READ.7.3.2 — LOW-TRUST auxiliary inclusion: Keeps it clearly LOW-TRUST and never independent support. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ.7 — Bootstrap reading context | Prior machine-generated readings proposed for early-run context. | Excludes them by default, or clearly marks them LOW-TRUST auxiliary context; neither branch supplies independent support. | Excluded material or explicitly low-trust auxiliary context. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE] |

SUB-PARTS: C-READ.7.3.1 — Default exclusion; C-READ.7.3.2 — LOW-TRUST auxiliary inclusion

### C-READ.7.3.1 — Default exclusion
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]

ALONE
- What it is: DECIDED-2026-09-25 — Excludes it from early-run context by default. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Takes in: DECIDED-2026-09-25 — A prior machine-generated reading. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Does: DECIDED-2026-09-25 — Excludes it from early-run context by default. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Gives out: DECIDED-2026-09-25 — No default inclusion. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ.7.3 — Prior machine-reading treatment | A prior machine-generated reading. | Excludes it from early-run context by default. | No default inclusion. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE] |

SUB-PARTS: NONE

### C-READ.7.3.2 — LOW-TRUST auxiliary inclusion
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]

ALONE
- What it is: DECIDED-2026-09-25 — Keeps it clearly LOW-TRUST and never independent support. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Takes in: DECIDED-2026-09-25 — A prior machine-generated reading used as auxiliary context. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Does: DECIDED-2026-09-25 — Keeps it clearly LOW-TRUST and never independent support. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Gives out: DECIDED-2026-09-25 — Explicitly low-trust auxiliary interpretation. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Must never: DECIDED-2026-09-25 — Treat auxiliary inclusion as evidence of truth. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ.7.3 — Prior machine-reading treatment | A prior machine-generated reading used as auxiliary context. | Keeps it clearly LOW-TRUST and never independent support. | Explicitly low-trust auxiliary interpretation. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE] |

SUB-PARTS: NONE

### C-READ.7.4 — No automatic self-amplification
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]

ALONE
- What it is: DECIDED-2026-09-25 — Prevents it from automatically becoming trusted context; the bootstrap rule acts before downstream lineage analysis. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Takes in: DECIDED-2026-09-25 — A machine reading that could feed the next reading. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Does: DECIDED-2026-09-25 — Prevents it from automatically becoming trusted context; the bootstrap rule acts before downstream lineage analysis. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Gives out: DECIDED-2026-09-25 — No automatic input-side corroboration loop. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Must never: DECIDED-2026-09-25 — Make repeated machine output its own independent confirmation. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ.7 — Bootstrap reading context | A machine reading that could feed the next reading. | Prevents it from automatically becoming trusted context; the bootstrap rule acts before downstream lineage analysis. | No automatic input-side corroboration loop. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / BOOTSTRAP RETRIEVAL RULE] |

SUB-PARTS: NONE

### C-READ.8 — Read-only memory-health checks
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]

ALONE
- What it is: DECIDED-2026-09-25 — Queries that make source, lineage, support and hidden contradictions inspectable. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Takes in: DECIDED-2026-09-25 — Readings and their `reads`, `derived_from`, `produced_by` and confidence; related Person-Box evidence and current-view contradictions. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Does: DECIDED-2026-09-25 — Runs read-only during quarantine and periodically afterward; surfaces six named classes of memory-health concern. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Does: DESIGNED — Each genuinely separate health-check operation is recorded once under the living-record law; read-only queries do not mutate the inspected reading, lineage or Person-Box records. [V10 §0B / ONE REAL OPERATION, ONE LOG]
- Gives out: DECIDED-2026-09-25 — Surfaced concerns about source clarity, dependency chains, single-lineage repetition, thin Person-Box evidence, unsupported confidence growth and hidden contradictions. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Must never: DECIDED-2026-09-25 — Modify readings or Person-Boxes as part of these read-only checks. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DECIDED-2026-09-25 — C-READ.8.1 — Health checks during quarantine: Runs the checks during quarantine. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Fed by: DECIDED-2026-09-25 — C-READ.8.2 — Health checks after quarantine: Runs the checks periodically afterward. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Fed by: DECIDED-2026-09-25 — C-READ.8.3 — Readings without clear sources: Surfaces readings with no clear source. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Fed by: DECIDED-2026-09-25 — C-READ.8.4 — Heavy older-reading dependence: Surfaces chains leaning heavily on older machine readings, including `derived_from` depth. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Fed by: DECIDED-2026-09-25 — C-READ.8.5 — Single-lineage false repetition: Surfaces one interpretation recurring from a single lineage. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Fed by: DECIDED-2026-09-25 — C-READ.8.6 — Thin Person-Box evidence: Surfaces Person-Boxes built from very little evidence. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Fed by: DECIDED-2026-09-25 — C-READ.8.7 — Confidence without independent roots: Surfaces readings whose confidence rose without new independent roots. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Fed by: DECIDED-2026-09-25 — C-READ.8.8 — Contradictions hidden by the current view: Surfaces contradictions the current view may be hiding. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Fed by: DESIGNED — C-READ.6 — Reading operation records: supplies the permanent record of each real checking operation, without a recursive log-about-log chain. [V10 §0B]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ — Reading record, validator, writer (§6B) | Reading and lineage/evidence relationships. | Runs the six read-only checks. | Inspectable concerns, with stored evidence unchanged. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS] |

SUB-PARTS: C-READ.8.1 — Health checks during quarantine; C-READ.8.2 — Health checks after quarantine; C-READ.8.3 — Readings without clear sources; C-READ.8.4 — Heavy older-reading dependence; C-READ.8.5 — Single-lineage false repetition; C-READ.8.6 — Thin Person-Box evidence; C-READ.8.7 — Confidence without independent roots; C-READ.8.8 — Contradictions hidden by the current view

### C-READ.8.1 — Health checks during quarantine
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]

ALONE
- What it is: DECIDED-2026-09-25 — Runs the checks during quarantine. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Takes in: DECIDED-2026-09-25 — Quarantine readings. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Does: DECIDED-2026-09-25 — Runs the checks during quarantine. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Gives out: DECIDED-2026-09-25 — Quarantine memory-health concerns are surfaced. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Must never: DECIDED-2026-09-25 — Modify or delete the checked records. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ.8 — Read-only memory-health checks | Quarantine readings. | Runs the checks during quarantine. | Quarantine memory-health concerns are surfaced. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS] |

SUB-PARTS: NONE

### C-READ.8.2 — Health checks after quarantine
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]

ALONE
- What it is: DECIDED-2026-09-25 — Runs the checks periodically afterward. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Takes in: DECIDED-2026-09-25 — The memory record after quarantine. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Does: DECIDED-2026-09-25 — Runs the checks periodically afterward. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Gives out: DECIDED-2026-09-25 — Later memory-health concerns are surfaced. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Must never: DECIDED-2026-09-25 — Modify or delete the checked records. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ.8 — Read-only memory-health checks | The memory record after quarantine. | Runs the checks periodically afterward. | Later memory-health concerns are surfaced. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS] |

SUB-PARTS: NONE

### C-READ.8.3 — Readings without clear sources
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]

ALONE
- What it is: DECIDED-2026-09-25 — Surfaces readings with no clear source. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Takes in: DECIDED-2026-09-25 — Readings and their source/provenance references. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Does: DECIDED-2026-09-25 — Surfaces readings with no clear source. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Gives out: DECIDED-2026-09-25 — Readings whose source clarity needs examination. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Must never: DECIDED-2026-09-25 — Modify or delete the checked records. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ.8 — Read-only memory-health checks | Readings and their source/provenance references. | Surfaces readings with no clear source. | Readings whose source clarity needs examination. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS] |

SUB-PARTS: NONE

### C-READ.8.4 — Heavy older-reading dependence
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]

ALONE
- What it is: DECIDED-2026-09-25 — Surfaces chains leaning heavily on older machine readings, including `derived_from` depth. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Takes in: DECIDED-2026-09-25 — Parent-reading chains in `derived_from`. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Does: DECIDED-2026-09-25 — Surfaces chains leaning heavily on older machine readings, including `derived_from` depth. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Gives out: DECIDED-2026-09-25 — Visible dependence on prior machine interpretation. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Must never: DECIDED-2026-09-25 — Modify or delete the checked records. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ.8 — Read-only memory-health checks | Parent-reading chains in `derived_from`. | Surfaces chains leaning heavily on older machine readings, including `derived_from` depth. | Visible dependence on prior machine interpretation. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS] |

SUB-PARTS: NONE

### C-READ.8.5 — Single-lineage false repetition
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]

ALONE
- What it is: DECIDED-2026-09-25 — Surfaces one interpretation recurring from a single lineage. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Takes in: DECIDED-2026-09-25 — Recurring interpretations and their lineage. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Does: DECIDED-2026-09-25 — Surfaces one interpretation recurring from a single lineage. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Gives out: DECIDED-2026-09-25 — False repetition is visible rather than counted as independent recurrence. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Must never: DECIDED-2026-09-25 — Modify or delete the checked records. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ.8 — Read-only memory-health checks | Recurring interpretations and their lineage. | Surfaces one interpretation recurring from a single lineage. | False repetition is visible rather than counted as independent recurrence. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS] |

SUB-PARTS: NONE

### C-READ.8.6 — Thin Person-Box evidence
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]

ALONE
- What it is: DECIDED-2026-09-25 — Surfaces Person-Boxes built from very little evidence. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Takes in: DECIDED-2026-09-25 — Person-Boxes and their supporting evidence. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Does: DECIDED-2026-09-25 — Surfaces Person-Boxes built from very little evidence. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Gives out: DECIDED-2026-09-25 — Thin evidence supporting a Person-Box is visible. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Must never: DECIDED-2026-09-25 — Modify or delete the checked records. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ.8 — Read-only memory-health checks | Person-Boxes and their supporting evidence. | Surfaces Person-Boxes built from very little evidence. | Thin evidence supporting a Person-Box is visible. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS] |

SUB-PARTS: NONE

### C-READ.8.7 — Confidence without independent roots
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]

ALONE
- What it is: DECIDED-2026-09-25 — Surfaces readings whose confidence rose without new independent roots. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Takes in: DECIDED-2026-09-25 — Reading confidence, source roots and reading lineage. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Does: DECIDED-2026-09-25 — Surfaces readings whose confidence rose without new independent roots. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Gives out: DECIDED-2026-09-25 — Unsupported confidence growth is visible. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Must never: DECIDED-2026-09-25 — Modify or delete the checked records. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ.8 — Read-only memory-health checks | Reading confidence, source roots and reading lineage. | Surfaces readings whose confidence rose without new independent roots. | Unsupported confidence growth is visible. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS] |

SUB-PARTS: NONE

### C-READ.8.8 — Contradictions hidden by the current view
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]

ALONE
- What it is: DECIDED-2026-09-25 — Surfaces contradictions the current view may be hiding. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Takes in: DECIDED-2026-09-25 — Contradictory readings and the current view. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Does: DECIDED-2026-09-25 — Surfaces contradictions the current view may be hiding. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Gives out: DECIDED-2026-09-25 — Contradictions obscured by presentation are visible. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Must never: DECIDED-2026-09-25 — Modify or delete the checked records. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ.8 — Read-only memory-health checks | Contradictory readings and the current view. | Surfaces contradictions the current view may be hiding. | Contradictions obscured by presentation are visible. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 6] [98/sources/NH_MASTER-14_FINAL__2_.md §11 item 27 / MEMORY-HEALTH CHECKS] |

SUB-PARTS: NONE

### C-READ.9 — Interpretation-integrity constraint
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]

ALONE
- What it is: DECIDED-2026-09-25 — The rule against interpretation becoming authority through use or presentation. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Takes in: DECIDED-2026-09-25 — An inferential reading and its traceability, challengeability and current-view treatment. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Does: DECIDED-2026-09-25 — The more inferential a reading, the easier it is to trace, challenge, suppress and replace in the current view. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Gives out: DECIDED-2026-09-25 — Traceable and contestable interpretations without rewriting the historical record. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Must never: DECIDED-2026-09-25 — Let repetition, retrieval ranking, presentation style or accumulated Person-Boxes silently turn an interpretation into authority. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DECIDED-2026-09-25 — C-READ.9.1 — Inferential reading — trace: Makes the reading easier to trace in the current view. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Fed by: DECIDED-2026-09-25 — C-READ.9.2 — Inferential reading — challenge: Makes the reading easier to challenge in the current view. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Fed by: DECIDED-2026-09-25 — C-READ.9.3 — Inferential reading — suppress: Makes the reading easier to suppress in the current view. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Fed by: DECIDED-2026-09-25 — C-READ.9.4 — Inferential reading — replace: Makes the reading easier to replace in the current view. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ — Reading record, validator, writer (§6B) | An inferential reading in current use. | Applies the increasing trace/challenge/suppress/replace requirement. | Current use cannot silently harden interpretation into authority. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT] |

SUB-PARTS: C-READ.9.1 — Inferential reading — trace; C-READ.9.2 — Inferential reading — challenge; C-READ.9.3 — Inferential reading — suppress; C-READ.9.4 — Inferential reading — replace

### C-READ.9.1 — Inferential reading — trace
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]

ALONE
- What it is: DECIDED-2026-09-25 — Makes the reading easier to trace in the current view. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Takes in: DECIDED-2026-09-25 — A reading with greater inference. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Does: DECIDED-2026-09-25 — Makes the reading easier to trace in the current view. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Gives out: DECIDED-2026-09-25 — The corresponding protection increases with inference. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Must never: DECIDED-2026-09-25 — Rewrite or delete the original reading to change its current use. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ.9 — Interpretation-integrity constraint | A reading with greater inference. | Makes the reading easier to trace in the current view. | The corresponding protection increases with inference. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT] |

SUB-PARTS: NONE

### C-READ.9.2 — Inferential reading — challenge
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]

ALONE
- What it is: DECIDED-2026-09-25 — Makes the reading easier to challenge in the current view. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Takes in: DECIDED-2026-09-25 — A reading with greater inference. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Does: DECIDED-2026-09-25 — Makes the reading easier to challenge in the current view. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Gives out: DECIDED-2026-09-25 — The corresponding protection increases with inference. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Must never: DECIDED-2026-09-25 — Rewrite or delete the original reading to change its current use. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ.9 — Interpretation-integrity constraint | A reading with greater inference. | Makes the reading easier to challenge in the current view. | The corresponding protection increases with inference. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT] |

SUB-PARTS: NONE

### C-READ.9.3 — Inferential reading — suppress
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]

ALONE
- What it is: DECIDED-2026-09-25 — Makes the reading easier to suppress in the current view. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Takes in: DECIDED-2026-09-25 — A reading with greater inference. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Does: DECIDED-2026-09-25 — Makes the reading easier to suppress in the current view. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Gives out: DECIDED-2026-09-25 — The corresponding protection increases with inference. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Must never: DECIDED-2026-09-25 — Rewrite or delete the original reading to change its current use. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ.9 — Interpretation-integrity constraint | A reading with greater inference. | Makes the reading easier to suppress in the current view. | The corresponding protection increases with inference. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT] |

SUB-PARTS: NONE

### C-READ.9.4 — Inferential reading — replace
Stamp: DECIDED-2026-09-25    Source: [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]

ALONE
- What it is: DECIDED-2026-09-25 — Makes the reading easier to replace in the current view. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Takes in: DECIDED-2026-09-25 — A reading with greater inference. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Does: DECIDED-2026-09-25 — Makes the reading easier to replace in the current view. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Gives out: DECIDED-2026-09-25 — The corresponding protection increases with inference. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Must never: DECIDED-2026-09-25 — Rewrite or delete the original reading to change its current use. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DECIDED-2026-09-25 | C-READ.9 — Interpretation-integrity constraint | A reading with greater inference. | Makes the reading easier to replace in the current view. | The corresponding protection increases with inference. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 5] [98/sources/NH_MASTER-14_FINAL.md §11 item 21 / INTERPRETATION-INTEGRITY CONSTRAINT] |

SUB-PARTS: NONE

<!-- END CHAPTER 3-b BEHAVIOR -->

## Chapter 3-b register contributions

### Appendix A — NOT DECIDED fields

| Part | Field or subdetail | Disposition |
|---|---|---|
| C-READ.1.1 | Takes in — exact reading-ID generation algorithm and JSON subtype | NOT DECIDED |
| C-READ.1.4.1 | Takes in — exact value scale, JSON type and range | NOT DECIDED |
| C-READ.1.4.2 | Takes in — exact value when source reliability is not yet knowable | NOT DECIDED |
| C-READ.1.4.2 | Takes in — exact known-reliability value scale and JSON form | NOT DECIDED |
| C-READ.1.6.1 | Takes in — v1 JSON value type and complete permitted value set | NOT DECIDED |
| C-READ.1.6.2 | Takes in — v1 JSON value type and complete permitted value set | NOT DECIDED |
| C-READ.1.6.3 | Takes in — v1 JSON value type and complete permitted value set | NOT DECIDED |
| C-READ.1.6.4 | Takes in — v1 JSON value type and complete permitted value set | NOT DECIDED |
| C-READ.1.6.5 | Takes in — v1 JSON value type and complete permitted value set | NOT DECIDED |
| C-READ.1.6.6 | Takes in — v1 JSON value type and complete permitted value set | NOT DECIDED |
| C-READ.1.7 | Takes in — exact classification_confidence JSON scale | NOT DECIDED |
| C-READ.1.8 | Takes in — exact reading timestamp serialization beyond shared timestamp validation | NOT DECIDED |
| C-READ.1.9.2 | Takes in — complete JSON serialization and nested type contract | NOT DECIDED |
| C-READ.1.9.3 | Takes in — complete JSON serialization and nested type contract | NOT DECIDED |
| C-READ.1.9.4 | Takes in — complete JSON serialization and nested type contract | NOT DECIDED |
| C-READ.1.9.5 | Takes in — complete JSON serialization and nested type contract | NOT DECIDED |
| C-READ.1.9.6 | Takes in — complete JSON serialization and nested type contract | NOT DECIDED |
| C-READ.1.9.7 | Takes in — complete JSON serialization and nested type contract | NOT DECIDED |
| C-READ.1.9.8 | Takes in — exact storage-key/JSON type contract for the human-annotation form | NOT DECIDED |
| C-READ.1.9.9 | Takes in — exact storage-key/JSON type contract for the human-annotation form | NOT DECIDED |
| C-READ.1.9.10 | Takes in — exact storage-key/JSON type contract for the human-annotation form | NOT DECIDED |
| C-READ.1.9.11 | Takes in — exact storage-key/JSON type contract for the human-annotation form | NOT DECIDED |
| C-READ.1.9.7.1 | Takes in — exact audit-content storage field/type | NOT DECIDED |
| C-READ.1.9.7.2 | Takes in — exact audit-content storage field/type | NOT DECIDED |
| C-READ.1.9.7.3 | Takes in — exact audit-content storage field/type | NOT DECIDED |
| C-READ.1.9.7.4 | Takes in — exact audit-content storage field/type | NOT DECIDED |
| C-READ.1.9.7.5 | Takes in — exact audit-content storage field/type | NOT DECIDED |
| C-READ.1.9.7.6 | Takes in — exact audit-content storage field/type | NOT DECIDED |
| C-READ.1.9.7.7 | Takes in — exact audit-content storage field/type | NOT DECIDED |
| C-READ.1.9.7.8.1 | Takes in — exact storage field/type | NOT DECIDED |
| C-READ.1.9.7.8.2 | Takes in — exact storage field/type | NOT DECIDED |
| C-READ.1.9.7.8.3 | Takes in — exact storage field/type | NOT DECIDED |
| C-READ.1.9.7.8.4 | Takes in — exact storage field/type | NOT DECIDED |
| C-READ.1.12.1 | Takes in — hash algorithm and canonical byte encoding | NOT DECIDED |
| C-READ.1.12.1 | Gives out — field name, storage home, and schema-version placement | NOT DECIDED |
| C-READ.2.6 | Does — live-validator value form when source reliability is not yet knowable | NOT DECIDED |
| C-READ.3.1.11 | Takes in — caller omission/default and exact ID generation behavior | NOT DECIDED |
| C-READ.3.1.13 | Takes in — default target-path value | NOT DECIDED |
| C-READ.3.4 | Fails closed by — exact low-level interruption/concurrency recovery algorithm in the built writer | NOT DECIDED |
| C-READ.6.1 | Gives out — exact event type label and full record schema | NOT DECIDED |
| C-READ.6.2 | Gives out — exact event type label and full record schema | NOT DECIDED |
| C-READ.6.3 | Gives out — exact event type label and full record schema | NOT DECIDED |
| C-READ.6.4 | Gives out — exact event type label and full record schema | NOT DECIDED |
| C-READ.6.5 | Gives out — exact event type label and full record schema | NOT DECIDED |
| C-READ.7 | Does — numeric meaning of mainly and duration/exit condition for early engine runs | NOT DECIDED |
| C-READ.7.3 | Does — exact selection criterion between exclusion and allowed low-trust auxiliary use | NOT DECIDED |
| C-READ.8 | Does — exact periodic interval, scheduling mechanism and query implementation | NOT DECIDED |
| C-READ.8 | Gives out — finding record schema, event labels and display layout | NOT DECIDED |
| C-READ.8.3 | Does — exact detection algorithm and any numeric threshold | NOT DECIDED |
| C-READ.8.4 | Does — exact detection algorithm and any numeric threshold | NOT DECIDED |
| C-READ.8.5 | Does — exact detection algorithm and any numeric threshold | NOT DECIDED |
| C-READ.8.6 | Does — exact detection algorithm and any numeric threshold | NOT DECIDED |
| C-READ.8.7 | Does — exact detection algorithm and any numeric threshold | NOT DECIDED |
| C-READ.8.8 | Does — exact detection algorithm and any numeric threshold | NOT DECIDED |
| C-READ.9.1 | Does — exact operational measure or implementation of easier | NOT DECIDED |
| C-READ.9.2 | Does — exact operational measure or implementation of easier | NOT DECIDED |
| C-READ.9.3 | Does — exact operational measure or implementation of easier | NOT DECIDED |
| C-READ.9.4 | Does — exact operational measure or implementation of easier | NOT DECIDED |
| C-READ | Changes | NOT DECIDED |
| C-READ.1 | Fails closed by | NOT DECIDED |
| C-READ.1 | Gated by | NOT DECIDED |
| C-READ.1 | Changes | NOT DECIDED |
| C-READ.1.1 | Fails closed by | NOT DECIDED |
| C-READ.1.1 | Fed by | NOT DECIDED |
| C-READ.1.1 | Gated by | NOT DECIDED |
| C-READ.1.1 | Changes | NOT DECIDED |
| C-READ.1.2 | Fails closed by | NOT DECIDED |
| C-READ.1.2 | Fed by | NOT DECIDED |
| C-READ.1.2 | Gated by | NOT DECIDED |
| C-READ.1.2 | Changes | NOT DECIDED |
| C-READ.1.3 | Fails closed by | NOT DECIDED |
| C-READ.1.3 | Fed by | NOT DECIDED |
| C-READ.1.3 | Gated by | NOT DECIDED |
| C-READ.1.3 | Changes | NOT DECIDED |
| C-READ.1.4 | Fails closed by | NOT DECIDED |
| C-READ.1.4 | Changes | NOT DECIDED |
| C-READ.1.4.1 | Fails closed by | NOT DECIDED |
| C-READ.1.4.1 | Fed by | NOT DECIDED |
| C-READ.1.4.1 | Gated by | NOT DECIDED |
| C-READ.1.4.1 | Changes | NOT DECIDED |
| C-READ.1.4.2 | Fails closed by | NOT DECIDED |
| C-READ.1.4.2 | Fed by | NOT DECIDED |
| C-READ.1.4.2 | Gated by | NOT DECIDED |
| C-READ.1.4.2 | Changes | NOT DECIDED |
| C-READ.1.4.3 | Must never | NOT DECIDED |
| C-READ.1.4.3 | Fails closed by | NOT DECIDED |
| C-READ.1.4.3 | Fed by | NOT DECIDED |
| C-READ.1.4.3 | Gated by | NOT DECIDED |
| C-READ.1.4.3 | Changes | NOT DECIDED |
| C-READ.1.4.4 | Must never | NOT DECIDED |
| C-READ.1.4.4 | Fails closed by | NOT DECIDED |
| C-READ.1.4.4 | Fed by | NOT DECIDED |
| C-READ.1.4.4 | Gated by | NOT DECIDED |
| C-READ.1.4.4 | Changes | NOT DECIDED |
| C-READ.1.4.5 | Must never | NOT DECIDED |
| C-READ.1.4.5 | Fails closed by | NOT DECIDED |
| C-READ.1.4.5 | Fed by | NOT DECIDED |
| C-READ.1.4.5 | Gated by | NOT DECIDED |
| C-READ.1.4.5 | Changes | NOT DECIDED |
| C-READ.1.4.6 | Fails closed by | NOT DECIDED |
| C-READ.1.4.6 | Fed by | NOT DECIDED |
| C-READ.1.4.6 | Gated by | NOT DECIDED |
| C-READ.1.4.6 | Changes | NOT DECIDED |
| C-READ.1.5 | Fails closed by | NOT DECIDED |
| C-READ.1.5 | Fed by | NOT DECIDED |
| C-READ.1.5 | Gated by | NOT DECIDED |
| C-READ.1.5 | Changes | NOT DECIDED |
| C-READ.1.6 | Fails closed by | NOT DECIDED |
| C-READ.1.6 | Gated by | NOT DECIDED |
| C-READ.1.6 | Changes | NOT DECIDED |
| C-READ.1.6.1 | Fails closed by | NOT DECIDED |
| C-READ.1.6.1 | Fed by | NOT DECIDED |
| C-READ.1.6.1 | Gated by | NOT DECIDED |
| C-READ.1.6.1 | Changes | NOT DECIDED |
| C-READ.1.6.2 | Fails closed by | NOT DECIDED |
| C-READ.1.6.2 | Fed by | NOT DECIDED |
| C-READ.1.6.2 | Gated by | NOT DECIDED |
| C-READ.1.6.2 | Changes | NOT DECIDED |
| C-READ.1.6.3 | Fails closed by | NOT DECIDED |
| C-READ.1.6.3 | Fed by | NOT DECIDED |
| C-READ.1.6.3 | Gated by | NOT DECIDED |
| C-READ.1.6.3 | Changes | NOT DECIDED |
| C-READ.1.6.4 | Fails closed by | NOT DECIDED |
| C-READ.1.6.4 | Fed by | NOT DECIDED |
| C-READ.1.6.4 | Gated by | NOT DECIDED |
| C-READ.1.6.4 | Changes | NOT DECIDED |
| C-READ.1.6.5 | Fails closed by | NOT DECIDED |
| C-READ.1.6.5 | Fed by | NOT DECIDED |
| C-READ.1.6.5 | Gated by | NOT DECIDED |
| C-READ.1.6.5 | Changes | NOT DECIDED |
| C-READ.1.6.6 | Fails closed by | NOT DECIDED |
| C-READ.1.6.6 | Fed by | NOT DECIDED |
| C-READ.1.6.6 | Gated by | NOT DECIDED |
| C-READ.1.6.6 | Changes | NOT DECIDED |
| C-READ.1.6.7 | Fails closed by | NOT DECIDED |
| C-READ.1.6.7 | Fed by | NOT DECIDED |
| C-READ.1.6.7 | Gated by | NOT DECIDED |
| C-READ.1.6.7 | Changes | NOT DECIDED |
| C-READ.1.6.8 | Fails closed by | NOT DECIDED |
| C-READ.1.6.8 | Fed by | NOT DECIDED |
| C-READ.1.6.8 | Gated by | NOT DECIDED |
| C-READ.1.6.8 | Changes | NOT DECIDED |
| C-READ.1.7 | Fails closed by | NOT DECIDED |
| C-READ.1.7 | Fed by | NOT DECIDED |
| C-READ.1.7 | Gated by | NOT DECIDED |
| C-READ.1.7 | Changes | NOT DECIDED |
| C-READ.1.8 | Fails closed by | NOT DECIDED |
| C-READ.1.8 | Fed by | NOT DECIDED |
| C-READ.1.8 | Gated by | NOT DECIDED |
| C-READ.1.8 | Changes | NOT DECIDED |
| C-READ.1.9 | Fails closed by | NOT DECIDED |
| C-READ.1.9 | Gated by | NOT DECIDED |
| C-READ.1.9 | Changes | NOT DECIDED |
| C-READ.1.9.1 | Fails closed by | NOT DECIDED |
| C-READ.1.9.1 | Gated by | NOT DECIDED |
| C-READ.1.9.1 | Changes | NOT DECIDED |
| C-READ.1.9.1.1 | Must never | NOT DECIDED |
| C-READ.1.9.1.1 | Fails closed by | NOT DECIDED |
| C-READ.1.9.1.1 | Fed by | NOT DECIDED |
| C-READ.1.9.1.1 | Gated by | NOT DECIDED |
| C-READ.1.9.1.1 | Changes | NOT DECIDED |
| C-READ.1.9.1.2 | Must never | NOT DECIDED |
| C-READ.1.9.1.2 | Fails closed by | NOT DECIDED |
| C-READ.1.9.1.2 | Fed by | NOT DECIDED |
| C-READ.1.9.1.2 | Gated by | NOT DECIDED |
| C-READ.1.9.1.2 | Changes | NOT DECIDED |
| C-READ.1.9.1.3 | Must never | NOT DECIDED |
| C-READ.1.9.1.3 | Fails closed by | NOT DECIDED |
| C-READ.1.9.1.3 | Fed by | NOT DECIDED |
| C-READ.1.9.1.3 | Gated by | NOT DECIDED |
| C-READ.1.9.1.3 | Changes | NOT DECIDED |
| C-READ.1.9.1.4 | Must never | NOT DECIDED |
| C-READ.1.9.1.4 | Fails closed by | NOT DECIDED |
| C-READ.1.9.1.4 | Fed by | NOT DECIDED |
| C-READ.1.9.1.4 | Gated by | NOT DECIDED |
| C-READ.1.9.1.4 | Changes | NOT DECIDED |
| C-READ.1.9.1.5 | Must never | NOT DECIDED |
| C-READ.1.9.1.5 | Fails closed by | NOT DECIDED |
| C-READ.1.9.1.5 | Fed by | NOT DECIDED |
| C-READ.1.9.1.5 | Gated by | NOT DECIDED |
| C-READ.1.9.1.5 | Changes | NOT DECIDED |
| C-READ.1.9.1.6 | Must never | NOT DECIDED |
| C-READ.1.9.1.6 | Fails closed by | NOT DECIDED |
| C-READ.1.9.1.6 | Fed by | NOT DECIDED |
| C-READ.1.9.1.6 | Gated by | NOT DECIDED |
| C-READ.1.9.1.6 | Changes | NOT DECIDED |
| C-READ.1.9.2 | Must never | NOT DECIDED |
| C-READ.1.9.2 | Fails closed by | NOT DECIDED |
| C-READ.1.9.2 | Fed by | NOT DECIDED |
| C-READ.1.9.2 | Gated by | NOT DECIDED |
| C-READ.1.9.2 | Changes | NOT DECIDED |
| C-READ.1.9.3 | Must never | NOT DECIDED |
| C-READ.1.9.3 | Fails closed by | NOT DECIDED |
| C-READ.1.9.3 | Fed by | NOT DECIDED |
| C-READ.1.9.3 | Gated by | NOT DECIDED |
| C-READ.1.9.3 | Changes | NOT DECIDED |
| C-READ.1.9.4 | Must never | NOT DECIDED |
| C-READ.1.9.4 | Fails closed by | NOT DECIDED |
| C-READ.1.9.4 | Fed by | NOT DECIDED |
| C-READ.1.9.4 | Gated by | NOT DECIDED |
| C-READ.1.9.4 | Changes | NOT DECIDED |
| C-READ.1.9.5 | Must never | NOT DECIDED |
| C-READ.1.9.5 | Fails closed by | NOT DECIDED |
| C-READ.1.9.5 | Fed by | NOT DECIDED |
| C-READ.1.9.5 | Gated by | NOT DECIDED |
| C-READ.1.9.5 | Changes | NOT DECIDED |
| C-READ.1.9.6 | Must never | NOT DECIDED |
| C-READ.1.9.6 | Fails closed by | NOT DECIDED |
| C-READ.1.9.6 | Gated by | NOT DECIDED |
| C-READ.1.9.6 | Changes | NOT DECIDED |
| C-READ.1.9.7 | Must never | NOT DECIDED |
| C-READ.1.9.7 | Fails closed by | NOT DECIDED |
| C-READ.1.9.7 | Gated by | NOT DECIDED |
| C-READ.1.9.7 | Changes | NOT DECIDED |
| C-READ.1.9.8 | Must never | NOT DECIDED |
| C-READ.1.9.8 | Fails closed by | NOT DECIDED |
| C-READ.1.9.8 | Fed by | NOT DECIDED |
| C-READ.1.9.8 | Gated by | NOT DECIDED |
| C-READ.1.9.8 | Changes | NOT DECIDED |
| C-READ.1.9.9 | Must never | NOT DECIDED |
| C-READ.1.9.9 | Fails closed by | NOT DECIDED |
| C-READ.1.9.9 | Fed by | NOT DECIDED |
| C-READ.1.9.9 | Gated by | NOT DECIDED |
| C-READ.1.9.9 | Changes | NOT DECIDED |
| C-READ.1.9.10 | Must never | NOT DECIDED |
| C-READ.1.9.10 | Fails closed by | NOT DECIDED |
| C-READ.1.9.10 | Fed by | NOT DECIDED |
| C-READ.1.9.10 | Gated by | NOT DECIDED |
| C-READ.1.9.10 | Changes | NOT DECIDED |
| C-READ.1.9.11 | Must never | NOT DECIDED |
| C-READ.1.9.11 | Fails closed by | NOT DECIDED |
| C-READ.1.9.11 | Fed by | NOT DECIDED |
| C-READ.1.9.11 | Gated by | NOT DECIDED |
| C-READ.1.9.11 | Changes | NOT DECIDED |
| C-READ.1.9.6.1 | Must never | NOT DECIDED |
| C-READ.1.9.6.1 | Fails closed by | NOT DECIDED |
| C-READ.1.9.6.1 | Fed by | NOT DECIDED |
| C-READ.1.9.6.1 | Gated by | NOT DECIDED |
| C-READ.1.9.6.1 | Changes | NOT DECIDED |
| C-READ.1.9.7.1 | Fails closed by | NOT DECIDED |
| C-READ.1.9.7.1 | Fed by | NOT DECIDED |
| C-READ.1.9.7.1 | Gated by | NOT DECIDED |
| C-READ.1.9.7.1 | Changes | NOT DECIDED |
| C-READ.1.9.7.2 | Fails closed by | NOT DECIDED |
| C-READ.1.9.7.2 | Fed by | NOT DECIDED |
| C-READ.1.9.7.2 | Gated by | NOT DECIDED |
| C-READ.1.9.7.2 | Changes | NOT DECIDED |
| C-READ.1.9.7.3 | Fails closed by | NOT DECIDED |
| C-READ.1.9.7.3 | Fed by | NOT DECIDED |
| C-READ.1.9.7.3 | Gated by | NOT DECIDED |
| C-READ.1.9.7.3 | Changes | NOT DECIDED |
| C-READ.1.9.7.4 | Fails closed by | NOT DECIDED |
| C-READ.1.9.7.4 | Fed by | NOT DECIDED |
| C-READ.1.9.7.4 | Gated by | NOT DECIDED |
| C-READ.1.9.7.4 | Changes | NOT DECIDED |
| C-READ.1.9.7.5 | Fails closed by | NOT DECIDED |
| C-READ.1.9.7.5 | Fed by | NOT DECIDED |
| C-READ.1.9.7.5 | Gated by | NOT DECIDED |
| C-READ.1.9.7.5 | Changes | NOT DECIDED |
| C-READ.1.9.7.6 | Fails closed by | NOT DECIDED |
| C-READ.1.9.7.6 | Fed by | NOT DECIDED |
| C-READ.1.9.7.6 | Gated by | NOT DECIDED |
| C-READ.1.9.7.6 | Changes | NOT DECIDED |
| C-READ.1.9.7.7 | Fails closed by | NOT DECIDED |
| C-READ.1.9.7.7 | Fed by | NOT DECIDED |
| C-READ.1.9.7.7 | Gated by | NOT DECIDED |
| C-READ.1.9.7.7 | Changes | NOT DECIDED |
| C-READ.1.9.7.8 | Fails closed by | NOT DECIDED |
| C-READ.1.9.7.8 | Gated by | NOT DECIDED |
| C-READ.1.9.7.8 | Changes | NOT DECIDED |
| C-READ.1.9.7.8.1 | Fails closed by | NOT DECIDED |
| C-READ.1.9.7.8.1 | Fed by | NOT DECIDED |
| C-READ.1.9.7.8.1 | Gated by | NOT DECIDED |
| C-READ.1.9.7.8.1 | Changes | NOT DECIDED |
| C-READ.1.9.7.8.2 | Fails closed by | NOT DECIDED |
| C-READ.1.9.7.8.2 | Fed by | NOT DECIDED |
| C-READ.1.9.7.8.2 | Gated by | NOT DECIDED |
| C-READ.1.9.7.8.2 | Changes | NOT DECIDED |
| C-READ.1.9.7.8.3 | Fails closed by | NOT DECIDED |
| C-READ.1.9.7.8.3 | Fed by | NOT DECIDED |
| C-READ.1.9.7.8.3 | Gated by | NOT DECIDED |
| C-READ.1.9.7.8.3 | Changes | NOT DECIDED |
| C-READ.1.9.7.8.4 | Fails closed by | NOT DECIDED |
| C-READ.1.9.7.8.4 | Fed by | NOT DECIDED |
| C-READ.1.9.7.8.4 | Gated by | NOT DECIDED |
| C-READ.1.9.7.8.4 | Changes | NOT DECIDED |
| C-READ.1.10 | Fails closed by | NOT DECIDED |
| C-READ.1.10 | Fed by | NOT DECIDED |
| C-READ.1.10 | Gated by | NOT DECIDED |
| C-READ.1.10 | Changes | NOT DECIDED |
| C-READ.1.11 | Fails closed by | NOT DECIDED |
| C-READ.1.11 | Gated by | NOT DECIDED |
| C-READ.1.11 | Changes | NOT DECIDED |
| C-READ.1.11.1 | Must never | NOT DECIDED |
| C-READ.1.11.1 | Fails closed by | NOT DECIDED |
| C-READ.1.11.1 | Fed by | NOT DECIDED |
| C-READ.1.11.1 | Gated by | NOT DECIDED |
| C-READ.1.11.1 | Changes | NOT DECIDED |
| C-READ.1.11.2 | Must never | NOT DECIDED |
| C-READ.1.11.2 | Fails closed by | NOT DECIDED |
| C-READ.1.11.2 | Fed by | NOT DECIDED |
| C-READ.1.11.2 | Gated by | NOT DECIDED |
| C-READ.1.11.2 | Changes | NOT DECIDED |
| C-READ.1.12 | Fails closed by | NOT DECIDED |
| C-READ.1.12 | Fed by | NOT DECIDED |
| C-READ.1.12 | Changes | NOT DECIDED |
| C-READ.1.12.1 | Fails closed by | NOT DECIDED |
| C-READ.1.12.1 | Fed by | NOT DECIDED |
| C-READ.1.12.1 | Changes | NOT DECIDED |
| C-READ.1.12.1.1 | Fails closed by | NOT DECIDED |
| C-READ.1.12.1.1 | Fed by | NOT DECIDED |
| C-READ.1.12.1.1 | Gated by | NOT DECIDED |
| C-READ.1.12.1.1 | Changes | NOT DECIDED |
| C-READ.1.12.1.2 | Fails closed by | NOT DECIDED |
| C-READ.1.12.1.2 | Fed by | NOT DECIDED |
| C-READ.1.12.1.2 | Gated by | NOT DECIDED |
| C-READ.1.12.1.2 | Changes | NOT DECIDED |
| C-READ.2 | Changes | NOT DECIDED |
| C-READ.2.1 | Must never | NOT DECIDED |
| C-READ.2.1 | Gated by | NOT DECIDED |
| C-READ.2.1 | Changes | NOT DECIDED |
| C-READ.2.1.1 | Must never | NOT DECIDED |
| C-READ.2.1.1 | Fed by | NOT DECIDED |
| C-READ.2.1.1 | Gated by | NOT DECIDED |
| C-READ.2.1.1 | Changes | NOT DECIDED |
| C-READ.2.2 | Must never | NOT DECIDED |
| C-READ.2.2 | Gated by | NOT DECIDED |
| C-READ.2.2 | Changes | NOT DECIDED |
| C-READ.2.2.1 | Must never | NOT DECIDED |
| C-READ.2.2.1 | Fed by | NOT DECIDED |
| C-READ.2.2.1 | Gated by | NOT DECIDED |
| C-READ.2.2.1 | Changes | NOT DECIDED |
| C-READ.2.3 | Must never | NOT DECIDED |
| C-READ.2.3 | Gated by | NOT DECIDED |
| C-READ.2.3 | Changes | NOT DECIDED |
| C-READ.2.3.1 | Must never | NOT DECIDED |
| C-READ.2.3.1 | Fed by | NOT DECIDED |
| C-READ.2.3.1 | Gated by | NOT DECIDED |
| C-READ.2.3.1 | Changes | NOT DECIDED |
| C-READ.2.4 | Must never | NOT DECIDED |
| C-READ.2.4 | Gated by | NOT DECIDED |
| C-READ.2.4 | Changes | NOT DECIDED |
| C-READ.2.4.1 | Must never | NOT DECIDED |
| C-READ.2.4.1 | Fed by | NOT DECIDED |
| C-READ.2.4.1 | Gated by | NOT DECIDED |
| C-READ.2.4.1 | Changes | NOT DECIDED |
| C-READ.2.5 | Must never | NOT DECIDED |
| C-READ.2.5 | Gated by | NOT DECIDED |
| C-READ.2.5 | Changes | NOT DECIDED |
| C-READ.2.5.1 | Must never | NOT DECIDED |
| C-READ.2.5.1 | Fed by | NOT DECIDED |
| C-READ.2.5.1 | Gated by | NOT DECIDED |
| C-READ.2.5.1 | Changes | NOT DECIDED |
| C-READ.2.6 | Must never | NOT DECIDED |
| C-READ.2.6 | Gated by | NOT DECIDED |
| C-READ.2.6 | Changes | NOT DECIDED |
| C-READ.2.6.1 | Must never | NOT DECIDED |
| C-READ.2.6.1 | Fed by | NOT DECIDED |
| C-READ.2.6.1 | Gated by | NOT DECIDED |
| C-READ.2.6.1 | Changes | NOT DECIDED |
| C-READ.2.7 | Must never | NOT DECIDED |
| C-READ.2.7 | Gated by | NOT DECIDED |
| C-READ.2.7 | Changes | NOT DECIDED |
| C-READ.2.7.1 | Must never | NOT DECIDED |
| C-READ.2.7.1 | Fed by | NOT DECIDED |
| C-READ.2.7.1 | Gated by | NOT DECIDED |
| C-READ.2.7.1 | Changes | NOT DECIDED |
| C-READ.2.8 | Must never | NOT DECIDED |
| C-READ.2.8 | Gated by | NOT DECIDED |
| C-READ.2.8 | Changes | NOT DECIDED |
| C-READ.2.8.1 | Must never | NOT DECIDED |
| C-READ.2.8.1 | Fed by | NOT DECIDED |
| C-READ.2.8.1 | Gated by | NOT DECIDED |
| C-READ.2.8.1 | Changes | NOT DECIDED |
| C-READ.2.9 | Must never | NOT DECIDED |
| C-READ.2.9 | Gated by | NOT DECIDED |
| C-READ.2.9 | Changes | NOT DECIDED |
| C-READ.2.9.1 | Must never | NOT DECIDED |
| C-READ.2.9.1 | Fed by | NOT DECIDED |
| C-READ.2.9.1 | Gated by | NOT DECIDED |
| C-READ.2.9.1 | Changes | NOT DECIDED |
| C-READ.2.10 | Must never | NOT DECIDED |
| C-READ.2.10 | Gated by | NOT DECIDED |
| C-READ.2.10 | Changes | NOT DECIDED |
| C-READ.2.10.1 | Must never | NOT DECIDED |
| C-READ.2.10.1 | Fed by | NOT DECIDED |
| C-READ.2.10.1 | Gated by | NOT DECIDED |
| C-READ.2.10.1 | Changes | NOT DECIDED |
| C-READ.2.11 | Must never | NOT DECIDED |
| C-READ.2.11 | Gated by | NOT DECIDED |
| C-READ.2.11 | Changes | NOT DECIDED |
| C-READ.2.11.1 | Must never | NOT DECIDED |
| C-READ.2.11.1 | Fed by | NOT DECIDED |
| C-READ.2.11.1 | Gated by | NOT DECIDED |
| C-READ.2.11.1 | Changes | NOT DECIDED |
| C-READ.2.12 | Must never | NOT DECIDED |
| C-READ.2.12 | Gated by | NOT DECIDED |
| C-READ.2.12 | Changes | NOT DECIDED |
| C-READ.2.12.1 | Must never | NOT DECIDED |
| C-READ.2.12.1 | Fed by | NOT DECIDED |
| C-READ.2.12.1 | Gated by | NOT DECIDED |
| C-READ.2.12.1 | Changes | NOT DECIDED |
| C-READ.2.13 | Must never | NOT DECIDED |
| C-READ.2.13 | Gated by | NOT DECIDED |
| C-READ.2.13 | Changes | NOT DECIDED |
| C-READ.2.13.1 | Must never | NOT DECIDED |
| C-READ.2.13.1 | Fed by | NOT DECIDED |
| C-READ.2.13.1 | Gated by | NOT DECIDED |
| C-READ.2.13.1 | Changes | NOT DECIDED |
| C-READ.2.14 | Fails closed by | NOT DECIDED |
| C-READ.2.14 | Fed by | NOT DECIDED |
| C-READ.2.14 | Gated by | NOT DECIDED |
| C-READ.2.14 | Changes | NOT DECIDED |
| C-READ.2.15 | Fails closed by | NOT DECIDED |
| C-READ.2.15 | Fed by | NOT DECIDED |
| C-READ.2.15 | Gated by | NOT DECIDED |
| C-READ.2.15 | Changes | NOT DECIDED |
| C-READ.2.16 | Fails closed by | NOT DECIDED |
| C-READ.2.16 | Fed by | NOT DECIDED |
| C-READ.2.16 | Gated by | NOT DECIDED |
| C-READ.2.16 | Changes | NOT DECIDED |
| C-READ.2.17 | Fails closed by | NOT DECIDED |
| C-READ.2.17 | Fed by | NOT DECIDED |
| C-READ.2.17 | Gated by | NOT DECIDED |
| C-READ.2.17 | Changes | NOT DECIDED |
| C-READ.3.1 | Must never | NOT DECIDED |
| C-READ.3.1 | Fails closed by | NOT DECIDED |
| C-READ.3.1 | Gated by | NOT DECIDED |
| C-READ.3.1 | Changes | NOT DECIDED |
| C-READ.3.1.1 | Must never | NOT DECIDED |
| C-READ.3.1.1 | Fails closed by | NOT DECIDED |
| C-READ.3.1.1 | Fed by | NOT DECIDED |
| C-READ.3.1.1 | Gated by | NOT DECIDED |
| C-READ.3.1.1 | Changes | NOT DECIDED |
| C-READ.3.1.2 | Must never | NOT DECIDED |
| C-READ.3.1.2 | Fails closed by | NOT DECIDED |
| C-READ.3.1.2 | Fed by | NOT DECIDED |
| C-READ.3.1.2 | Gated by | NOT DECIDED |
| C-READ.3.1.2 | Changes | NOT DECIDED |
| C-READ.3.1.3 | Must never | NOT DECIDED |
| C-READ.3.1.3 | Fails closed by | NOT DECIDED |
| C-READ.3.1.3 | Fed by | NOT DECIDED |
| C-READ.3.1.3 | Gated by | NOT DECIDED |
| C-READ.3.1.3 | Changes | NOT DECIDED |
| C-READ.3.1.4 | Must never | NOT DECIDED |
| C-READ.3.1.4 | Fails closed by | NOT DECIDED |
| C-READ.3.1.4 | Fed by | NOT DECIDED |
| C-READ.3.1.4 | Gated by | NOT DECIDED |
| C-READ.3.1.4 | Changes | NOT DECIDED |
| C-READ.3.1.5 | Must never | NOT DECIDED |
| C-READ.3.1.5 | Fails closed by | NOT DECIDED |
| C-READ.3.1.5 | Fed by | NOT DECIDED |
| C-READ.3.1.5 | Gated by | NOT DECIDED |
| C-READ.3.1.5 | Changes | NOT DECIDED |
| C-READ.3.1.6 | Must never | NOT DECIDED |
| C-READ.3.1.6 | Fails closed by | NOT DECIDED |
| C-READ.3.1.6 | Fed by | NOT DECIDED |
| C-READ.3.1.6 | Gated by | NOT DECIDED |
| C-READ.3.1.6 | Changes | NOT DECIDED |
| C-READ.3.1.7 | Must never | NOT DECIDED |
| C-READ.3.1.7 | Fails closed by | NOT DECIDED |
| C-READ.3.1.7 | Fed by | NOT DECIDED |
| C-READ.3.1.7 | Gated by | NOT DECIDED |
| C-READ.3.1.7 | Changes | NOT DECIDED |
| C-READ.3.1.8 | Must never | NOT DECIDED |
| C-READ.3.1.8 | Fails closed by | NOT DECIDED |
| C-READ.3.1.8 | Fed by | NOT DECIDED |
| C-READ.3.1.8 | Gated by | NOT DECIDED |
| C-READ.3.1.8 | Changes | NOT DECIDED |
| C-READ.3.1.9 | Must never | NOT DECIDED |
| C-READ.3.1.9 | Fails closed by | NOT DECIDED |
| C-READ.3.1.9 | Fed by | NOT DECIDED |
| C-READ.3.1.9 | Gated by | NOT DECIDED |
| C-READ.3.1.9 | Changes | NOT DECIDED |
| C-READ.3.1.10 | Must never | NOT DECIDED |
| C-READ.3.1.10 | Fails closed by | NOT DECIDED |
| C-READ.3.1.10 | Fed by | NOT DECIDED |
| C-READ.3.1.10 | Gated by | NOT DECIDED |
| C-READ.3.1.10 | Changes | NOT DECIDED |
| C-READ.3.1.11 | Must never | NOT DECIDED |
| C-READ.3.1.11 | Fails closed by | NOT DECIDED |
| C-READ.3.1.11 | Fed by | NOT DECIDED |
| C-READ.3.1.11 | Gated by | NOT DECIDED |
| C-READ.3.1.11 | Changes | NOT DECIDED |
| C-READ.3.1.12 | Must never | NOT DECIDED |
| C-READ.3.1.12 | Fails closed by | NOT DECIDED |
| C-READ.3.1.12 | Fed by | NOT DECIDED |
| C-READ.3.1.12 | Gated by | NOT DECIDED |
| C-READ.3.1.12 | Changes | NOT DECIDED |
| C-READ.3.1.13 | Must never | NOT DECIDED |
| C-READ.3.1.13 | Fails closed by | NOT DECIDED |
| C-READ.3.1.13 | Fed by | NOT DECIDED |
| C-READ.3.1.13 | Gated by | NOT DECIDED |
| C-READ.3.1.13 | Changes | NOT DECIDED |
| C-READ.3.2 | Must never | NOT DECIDED |
| C-READ.3.2 | Fails closed by | NOT DECIDED |
| C-READ.3.2 | Gated by | NOT DECIDED |
| C-READ.3.2 | Changes | NOT DECIDED |
| C-READ.3.2.1 | Must never | NOT DECIDED |
| C-READ.3.2.1 | Fed by | NOT DECIDED |
| C-READ.3.2.1 | Gated by | NOT DECIDED |
| C-READ.3.2.1 | Changes | NOT DECIDED |
| C-READ.3.3 | Must never | NOT DECIDED |
| C-READ.3.3 | Fails closed by | NOT DECIDED |
| C-READ.3.3 | Gated by | NOT DECIDED |
| C-READ.3.3 | Changes | NOT DECIDED |
| C-READ.3.3.1 | Must never | NOT DECIDED |
| C-READ.3.3.1 | Fed by | NOT DECIDED |
| C-READ.3.3.1 | Gated by | NOT DECIDED |
| C-READ.3.3.1 | Changes | NOT DECIDED |
| C-READ.3.4 | Must never | NOT DECIDED |
| C-READ.3.4 | Fails closed by | NOT DECIDED |
| C-READ.3.4 | Gated by | NOT DECIDED |
| C-READ.3.4 | Changes | NOT DECIDED |
| C-READ.3.4.1 | Must never | NOT DECIDED |
| C-READ.3.4.1 | Fails closed by | NOT DECIDED |
| C-READ.3.4.1 | Fed by | NOT DECIDED |
| C-READ.3.4.1 | Gated by | NOT DECIDED |
| C-READ.3.4.1 | Changes | NOT DECIDED |
| C-READ.3.4.2 | Must never | NOT DECIDED |
| C-READ.3.4.2 | Fails closed by | NOT DECIDED |
| C-READ.3.4.2 | Fed by | NOT DECIDED |
| C-READ.3.4.2 | Gated by | NOT DECIDED |
| C-READ.3.4.2 | Changes | NOT DECIDED |
| C-READ.3.5 | Must never | NOT DECIDED |
| C-READ.3.5 | Fails closed by | NOT DECIDED |
| C-READ.3.5 | Fed by | NOT DECIDED |
| C-READ.3.5 | Gated by | NOT DECIDED |
| C-READ.3.5 | Changes | NOT DECIDED |
| C-READ.3.6 | Fails closed by | NOT DECIDED |
| C-READ.3.6 | Fed by | NOT DECIDED |
| C-READ.3.6 | Gated by | NOT DECIDED |
| C-READ.3.6 | Changes | NOT DECIDED |
| C-READ.3.7 | Fails closed by | NOT DECIDED |
| C-READ.3.7 | Gated by | NOT DECIDED |
| C-READ.3.7 | Changes | NOT DECIDED |
| C-READ.3.7.1 | Must never | NOT DECIDED |
| C-READ.3.7.1 | Fails closed by | NOT DECIDED |
| C-READ.3.7.1 | Fed by | NOT DECIDED |
| C-READ.3.7.1 | Gated by | NOT DECIDED |
| C-READ.3.7.1 | Changes | NOT DECIDED |
| C-READ.3.7.2 | Must never | NOT DECIDED |
| C-READ.3.7.2 | Fails closed by | NOT DECIDED |
| C-READ.3.7.2 | Fed by | NOT DECIDED |
| C-READ.3.7.2 | Gated by | NOT DECIDED |
| C-READ.3.7.2 | Changes | NOT DECIDED |
| C-READ.3.7.3 | Must never | NOT DECIDED |
| C-READ.3.7.3 | Fails closed by | NOT DECIDED |
| C-READ.3.7.3 | Fed by | NOT DECIDED |
| C-READ.3.7.3 | Gated by | NOT DECIDED |
| C-READ.3.7.3 | Changes | NOT DECIDED |
| C-READ.3.7.4 | Must never | NOT DECIDED |
| C-READ.3.7.4 | Fails closed by | NOT DECIDED |
| C-READ.3.7.4 | Fed by | NOT DECIDED |
| C-READ.3.7.4 | Gated by | NOT DECIDED |
| C-READ.3.7.4 | Changes | NOT DECIDED |
| C-READ.3.7.5 | Must never | NOT DECIDED |
| C-READ.3.7.5 | Fails closed by | NOT DECIDED |
| C-READ.3.7.5 | Fed by | NOT DECIDED |
| C-READ.3.7.5 | Gated by | NOT DECIDED |
| C-READ.3.7.5 | Changes | NOT DECIDED |
| C-READ.3.7.6 | Must never | NOT DECIDED |
| C-READ.3.7.6 | Fails closed by | NOT DECIDED |
| C-READ.3.7.6 | Gated by | NOT DECIDED |
| C-READ.3.7.6 | Changes | NOT DECIDED |
| C-READ.3.7.6.1 | Must never | NOT DECIDED |
| C-READ.3.7.6.1 | Fails closed by | NOT DECIDED |
| C-READ.3.7.6.1 | Fed by | NOT DECIDED |
| C-READ.3.7.6.1 | Gated by | NOT DECIDED |
| C-READ.3.7.6.1 | Changes | NOT DECIDED |
| C-READ.3.7.6.2 | Must never | NOT DECIDED |
| C-READ.3.7.6.2 | Fails closed by | NOT DECIDED |
| C-READ.3.7.6.2 | Fed by | NOT DECIDED |
| C-READ.3.7.6.2 | Gated by | NOT DECIDED |
| C-READ.3.7.6.2 | Changes | NOT DECIDED |
| C-READ.3.7.7 | Must never | NOT DECIDED |
| C-READ.3.7.7 | Gated by | NOT DECIDED |
| C-READ.3.7.7 | Changes | NOT DECIDED |
| C-READ.3.7.7.1 | Must never | NOT DECIDED |
| C-READ.3.7.7.1 | Fails closed by | NOT DECIDED |
| C-READ.3.7.7.1 | Fed by | NOT DECIDED |
| C-READ.3.7.7.1 | Gated by | NOT DECIDED |
| C-READ.3.7.7.1 | Changes | NOT DECIDED |
| C-READ.3.7.7.2 | Must never | NOT DECIDED |
| C-READ.3.7.7.2 | Fails closed by | NOT DECIDED |
| C-READ.3.7.7.2 | Fed by | NOT DECIDED |
| C-READ.3.7.7.2 | Gated by | NOT DECIDED |
| C-READ.3.7.7.2 | Changes | NOT DECIDED |
| C-READ.3.7.7.3 | Must never | NOT DECIDED |
| C-READ.3.7.7.3 | Fails closed by | NOT DECIDED |
| C-READ.3.7.7.3 | Fed by | NOT DECIDED |
| C-READ.3.7.7.3 | Gated by | NOT DECIDED |
| C-READ.3.7.7.3 | Changes | NOT DECIDED |
| C-READ.3.7.7.4 | Must never | NOT DECIDED |
| C-READ.3.7.7.4 | Fails closed by | NOT DECIDED |
| C-READ.3.7.7.4 | Fed by | NOT DECIDED |
| C-READ.3.7.7.4 | Gated by | NOT DECIDED |
| C-READ.3.7.7.4 | Changes | NOT DECIDED |
| C-READ.4 | Fails closed by | NOT DECIDED |
| C-READ.4 | Fed by | NOT DECIDED |
| C-READ.4 | Changes | NOT DECIDED |
| C-READ.4.1 | Fails closed by | NOT DECIDED |
| C-READ.4.1 | Fed by | NOT DECIDED |
| C-READ.4.1 | Gated by | NOT DECIDED |
| C-READ.4.1 | Changes | NOT DECIDED |
| C-READ.5 | Fed by | NOT DECIDED |
| C-READ.5 | Changes | NOT DECIDED |
| C-READ.5.1 | Gated by | NOT DECIDED |
| C-READ.5.1 | Changes | NOT DECIDED |
| C-READ.5.2 | Fails closed by | NOT DECIDED |
| C-READ.5.2 | Gated by | NOT DECIDED |
| C-READ.5.2 | Changes | NOT DECIDED |
| C-READ.5.2.1 | Fails closed by | NOT DECIDED |
| C-READ.5.2.1 | Fed by | NOT DECIDED |
| C-READ.5.2.1 | Gated by | NOT DECIDED |
| C-READ.5.2.1 | Changes | NOT DECIDED |
| C-READ.5.2.2 | Fails closed by | NOT DECIDED |
| C-READ.5.2.2 | Fed by | NOT DECIDED |
| C-READ.5.2.2 | Gated by | NOT DECIDED |
| C-READ.5.2.2 | Changes | NOT DECIDED |
| C-READ.5.2.3 | Fails closed by | NOT DECIDED |
| C-READ.5.2.3 | Fed by | NOT DECIDED |
| C-READ.5.2.3 | Gated by | NOT DECIDED |
| C-READ.5.2.3 | Changes | NOT DECIDED |
| C-READ.5.2.4 | Fails closed by | NOT DECIDED |
| C-READ.5.2.4 | Fed by | NOT DECIDED |
| C-READ.5.2.4 | Gated by | NOT DECIDED |
| C-READ.5.2.4 | Changes | NOT DECIDED |
| C-READ.5.2.5 | Fails closed by | NOT DECIDED |
| C-READ.5.2.5 | Fed by | NOT DECIDED |
| C-READ.5.2.5 | Gated by | NOT DECIDED |
| C-READ.5.2.5 | Changes | NOT DECIDED |
| C-READ.5.2.6 | Fails closed by | NOT DECIDED |
| C-READ.5.2.6 | Fed by | NOT DECIDED |
| C-READ.5.2.6 | Gated by | NOT DECIDED |
| C-READ.5.2.6 | Changes | NOT DECIDED |
| C-READ.5.2.7 | Fails closed by | NOT DECIDED |
| C-READ.5.2.7 | Fed by | NOT DECIDED |
| C-READ.5.2.7 | Gated by | NOT DECIDED |
| C-READ.5.2.7 | Changes | NOT DECIDED |
| C-READ.5.2.8 | Fails closed by | NOT DECIDED |
| C-READ.5.2.8 | Fed by | NOT DECIDED |
| C-READ.5.2.8 | Gated by | NOT DECIDED |
| C-READ.5.2.8 | Changes | NOT DECIDED |
| C-READ.5.1.1 | Must never | NOT DECIDED |
| C-READ.5.1.1 | Fails closed by | NOT DECIDED |
| C-READ.5.1.1 | Fed by | NOT DECIDED |
| C-READ.5.1.1 | Gated by | NOT DECIDED |
| C-READ.5.1.1 | Changes | NOT DECIDED |
| C-READ.6 | Fails closed by | NOT DECIDED |
| C-READ.6 | Changes | NOT DECIDED |
| C-READ.6.1 | Must never | NOT DECIDED |
| C-READ.6.1 | Fails closed by | NOT DECIDED |
| C-READ.6.1 | Fed by | NOT DECIDED |
| C-READ.6.1 | Gated by | NOT DECIDED |
| C-READ.6.1 | Changes | NOT DECIDED |
| C-READ.6.2 | Must never | NOT DECIDED |
| C-READ.6.2 | Fails closed by | NOT DECIDED |
| C-READ.6.2 | Fed by | NOT DECIDED |
| C-READ.6.2 | Gated by | NOT DECIDED |
| C-READ.6.2 | Changes | NOT DECIDED |
| C-READ.6.3 | Must never | NOT DECIDED |
| C-READ.6.3 | Fails closed by | NOT DECIDED |
| C-READ.6.3 | Fed by | NOT DECIDED |
| C-READ.6.3 | Gated by | NOT DECIDED |
| C-READ.6.3 | Changes | NOT DECIDED |
| C-READ.6.4 | Must never | NOT DECIDED |
| C-READ.6.4 | Fails closed by | NOT DECIDED |
| C-READ.6.4 | Fed by | NOT DECIDED |
| C-READ.6.4 | Gated by | NOT DECIDED |
| C-READ.6.4 | Changes | NOT DECIDED |
| C-READ.6.5 | Must never | NOT DECIDED |
| C-READ.6.5 | Fails closed by | NOT DECIDED |
| C-READ.6.5 | Fed by | NOT DECIDED |
| C-READ.6.5 | Gated by | NOT DECIDED |
| C-READ.6.5 | Changes | NOT DECIDED |
| C-READ.7 | Fails closed by | NOT DECIDED |
| C-READ.7 | Changes | NOT DECIDED |
| C-READ.7.1 | Must never | NOT DECIDED |
| C-READ.7.1 | Fails closed by | NOT DECIDED |
| C-READ.7.1 | Fed by | NOT DECIDED |
| C-READ.7.1 | Gated by | NOT DECIDED |
| C-READ.7.1 | Changes | NOT DECIDED |
| C-READ.7.2 | Fails closed by | NOT DECIDED |
| C-READ.7.2 | Fed by | NOT DECIDED |
| C-READ.7.2 | Gated by | NOT DECIDED |
| C-READ.7.2 | Changes | NOT DECIDED |
| C-READ.7.3 | Fails closed by | NOT DECIDED |
| C-READ.7.3 | Gated by | NOT DECIDED |
| C-READ.7.3 | Changes | NOT DECIDED |
| C-READ.7.3.1 | Must never | NOT DECIDED |
| C-READ.7.3.1 | Fails closed by | NOT DECIDED |
| C-READ.7.3.1 | Fed by | NOT DECIDED |
| C-READ.7.3.1 | Gated by | NOT DECIDED |
| C-READ.7.3.1 | Changes | NOT DECIDED |
| C-READ.7.3.2 | Fails closed by | NOT DECIDED |
| C-READ.7.3.2 | Fed by | NOT DECIDED |
| C-READ.7.3.2 | Gated by | NOT DECIDED |
| C-READ.7.3.2 | Changes | NOT DECIDED |
| C-READ.7.4 | Fails closed by | NOT DECIDED |
| C-READ.7.4 | Fed by | NOT DECIDED |
| C-READ.7.4 | Gated by | NOT DECIDED |
| C-READ.7.4 | Changes | NOT DECIDED |
| C-READ.8 | Fails closed by | NOT DECIDED |
| C-READ.8 | Gated by | NOT DECIDED |
| C-READ.8 | Changes | NOT DECIDED |
| C-READ.8.1 | Fails closed by | NOT DECIDED |
| C-READ.8.1 | Fed by | NOT DECIDED |
| C-READ.8.1 | Gated by | NOT DECIDED |
| C-READ.8.1 | Changes | NOT DECIDED |
| C-READ.8.2 | Fails closed by | NOT DECIDED |
| C-READ.8.2 | Fed by | NOT DECIDED |
| C-READ.8.2 | Gated by | NOT DECIDED |
| C-READ.8.2 | Changes | NOT DECIDED |
| C-READ.8.3 | Fails closed by | NOT DECIDED |
| C-READ.8.3 | Fed by | NOT DECIDED |
| C-READ.8.3 | Gated by | NOT DECIDED |
| C-READ.8.3 | Changes | NOT DECIDED |
| C-READ.8.4 | Fails closed by | NOT DECIDED |
| C-READ.8.4 | Fed by | NOT DECIDED |
| C-READ.8.4 | Gated by | NOT DECIDED |
| C-READ.8.4 | Changes | NOT DECIDED |
| C-READ.8.5 | Fails closed by | NOT DECIDED |
| C-READ.8.5 | Fed by | NOT DECIDED |
| C-READ.8.5 | Gated by | NOT DECIDED |
| C-READ.8.5 | Changes | NOT DECIDED |
| C-READ.8.6 | Fails closed by | NOT DECIDED |
| C-READ.8.6 | Fed by | NOT DECIDED |
| C-READ.8.6 | Gated by | NOT DECIDED |
| C-READ.8.6 | Changes | NOT DECIDED |
| C-READ.8.7 | Fails closed by | NOT DECIDED |
| C-READ.8.7 | Fed by | NOT DECIDED |
| C-READ.8.7 | Gated by | NOT DECIDED |
| C-READ.8.7 | Changes | NOT DECIDED |
| C-READ.8.8 | Fails closed by | NOT DECIDED |
| C-READ.8.8 | Fed by | NOT DECIDED |
| C-READ.8.8 | Gated by | NOT DECIDED |
| C-READ.8.8 | Changes | NOT DECIDED |
| C-READ.9 | Fails closed by | NOT DECIDED |
| C-READ.9 | Gated by | NOT DECIDED |
| C-READ.9 | Changes | NOT DECIDED |
| C-READ.9.1 | Fails closed by | NOT DECIDED |
| C-READ.9.1 | Fed by | NOT DECIDED |
| C-READ.9.1 | Gated by | NOT DECIDED |
| C-READ.9.1 | Changes | NOT DECIDED |
| C-READ.9.2 | Fails closed by | NOT DECIDED |
| C-READ.9.2 | Fed by | NOT DECIDED |
| C-READ.9.2 | Gated by | NOT DECIDED |
| C-READ.9.2 | Changes | NOT DECIDED |
| C-READ.9.3 | Fails closed by | NOT DECIDED |
| C-READ.9.3 | Fed by | NOT DECIDED |
| C-READ.9.3 | Gated by | NOT DECIDED |
| C-READ.9.3 | Changes | NOT DECIDED |
| C-READ.9.4 | Fails closed by | NOT DECIDED |
| C-READ.9.4 | Fed by | NOT DECIDED |
| C-READ.9.4 | Gated by | NOT DECIDED |
| C-READ.9.4 | Changes | NOT DECIDED |

Exact wire forms in this register are unfilled in this scoped v1 account; this is not a claim that later accepted packages lack their own schemas. Accepted telling identity, firmness representation, B16 promotion and its evaluation-evidence bridge are reserved for their own complete templates, not replaced with guessed v1 fields.

### Source-conflict register

| Location | Governing source | Losing wording preserved |
|---|---|---|
| C-READ.1.12 | V10 §6A / SCHEMA CONSTRAINTS: key uniqueness per store | CR §1C: forbids key reuse already committed to any readings store. The conflict is marked on the behavior line; no new global key rule is inferred. |

### Restoration coverage

| FR-ID | Restored content | Landing |
|---|---|---|
| FR-0123 | Optional content hash is separate from operation-key retries | C-READ.1.12.1 |
| FR-0125 | Raw roots and explicitly human-affirmed bootstrap context | C-READ.7.1; C-READ.7.2 |
| FR-0126 | Prior machine readings excluded or LOW-TRUST, never independent support | C-READ.7.3 |
| FR-0127 | Read-only checks during quarantine and periodically afterward | C-READ.8 |
| FR-0128 | Unclear source | C-READ.8.3 |
| FR-0129 | Heavy older-reading dependence | C-READ.8.4 |
| FR-0130 | Single-lineage repetition | C-READ.8.5 |
| FR-0131 | Thin Person-Box evidence | C-READ.8.6 |
| FR-0132 | Confidence growth without independent roots | C-READ.8.7 |
| FR-0133 | Hidden contradiction | C-READ.8.8 |
| FR-0136 | Interpretation-integrity constraint | C-READ.9 |

### Cross-piece relationships and path placement

All new sub-parts belong to C-READ. The record/write foundation participates in CY-A and the applicable reread output in CY-F. Bootstrap context constrains early reading passes; health checks apply during quarantine and periodically afterward without an invented scheduler. They are not inserted as a compulsory ordered step in every reading pass. No new top-level component or path ID is introduced.

| Earlier endpoint | Reciprocal landing in this piece |
|---|---|
| C-STORE — Accretive store & sealed roots (§6B) | C-READ Fed by / Gated by |
| C-STORE.3.1 — _check_common | C-READ Fed by / Gated by |
| C-7B.2.8.4 — Stored mode object | C-READ Fed by / Gated by |
| C-7B.2.8.4.1 — label | C-READ Fed by / Gated by |
| C-7B.2.8.4.2 — classification_confidence | C-READ Fed by / Gated by |
| C-7B.11.2 — Pointer-shown why | C-READ Fed by / Gated by |
| C-7A — Universal Filter (§7A) | C-READ USED BY |

Future owning templates must reciprocate C-READ’s C-ENGINE-AB, C-ENGINE-C, C-7G, C-7GA and C-7H inputs/uses and the C-7J, C-7K, C-7L, C-7M, C-7D and C-7I uses. C-READ.6 also carries a C-7Q access-gate relationship for that owning template. Accepted promotion machinery and telling identity are pending placement, not declared undecided or built.

### Remaining Chapter 3 scope

C-READ’s accepted telling-identity and promotion/evaluation-evidence architecture; C-ENGINE-AB; C-ENGINE-C; C-INDEX; C-GOLD; C-INGEST; C-DETECT. Detailed Acceptance Check, retry, hold and reread orchestration remains with its owning Group C templates; the present piece records only the reading-write handoff.

## Coverage matrix — Chapter 3-b contribution

All 138 READ-folder file rows and 107 V10 heading rows retain their identifiers. Earlier placements and whole-read credit are carried forward, not claimed as fresh reading in this piece. Current additions are identified explicitly. Metadata rows preserve source headings verbatim; they are not behavior or status-table copies.

### File coverage

| Row | Source path | Read scope | Placement or reason |
|---|---|---|---|
| F001 | `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.1; C-STORE.2; C-STORE.3; CY-A Chapter 3-b: C-READ and its v1 record, validator, writer, quarantine, production-boundary and operation-record sub-parts; CY-A/CY-F reading-write interfaces. |
| F002 | `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | EXCLUDED: interaction/workflow guidance under §1.3 and §2.4. NOT PLACED: remaining behavior belongs to other component groups.; Chapter 3-a: C-STORE.2.3 Chapter 3-b: C-READ.1 confidence semantics and C-READ.2 uncertainty-preserving shape gate; remaining scope retained. |
| F003 | `01_AUTHORITATIVE/cursorrules` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | EXCLUDED: coding-process rules under §1.3. NOT PLACED: built-code boundaries belong to store, reader and code-boundary groups. Chapter 3-b: C-READ.1.12 per-store/global-key conflict and C-READ.3 shared write boundary; workflow remains excluded. |
| F004 | `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F005 | `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.3.4; CY-A Chapter 3-b: C-READ component name, operation logging and consumer/caller relationships; CY-A/CY-F interfaces. |
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
| F017 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_GOLD_CASES_MISSING_SOURCE_BLOCKER_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F018 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F019 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F020 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F021 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
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
| F036 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F037 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_PACKAGE_COMPLETE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
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
| F052 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Earlier Chapter 0 read only; not reread at this pin | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F053 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Earlier Chapter 0 read only; not reread at this pin | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F054 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Earlier Chapter 0 read only; not reread at this pin | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F055 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F056 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F057 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F058 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_PACKAGE_COMPLETE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
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
| F086 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | Chapter 3-a: C-STORE.5 / Origin preservation policy; A3.4–A3.5 and other components NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: Navigation excerpt only; no new behavior sourced in this piece. |
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
| F099 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F100 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
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
| F112 | `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` | Carried through Chapter 3-a: Earlier Chapter 0 read only; not reread at this pin | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F113 | `05_ACTIVE_CANDIDATE/NH_B24_REJECTION_CATEGORY_DECISION_2026-09-23_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F114 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F115 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; Chapter 3-a: Navigation only: NHD-B11 and NHD-BU1; no behavior sourced from the index |
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
| F127 | `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Identity/hash verified; Stage 2 reading pending | NOT PLACED: Appendix B requires Stage 2 rows by FR-ID/title only; no behavior sourced from the ledger. |
| F128 | `05_ACTIVE_CANDIDATE/Other_Future_Feature_Intent_Excerpts.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F129 | `05_ACTIVE_CANDIDATE/Thought_Branches_and_Simulation_Intent.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F130 | `05_INACTIVE_CANDIDATE/NH_FUTURE_MUSIC_UNDERSTANDING_AND_MUSIC_SERVICE_CONNECTIONS_PACKAGE_INTAKE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F131 | `05_INACTIVE_CANDIDATE/NH_ISSUE_CHANNEL_INTENT_v0_1.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F132 | `05_INACTIVE_CANDIDATE/NH_PROVENANCE_FIRST_MULTI_INDEX_MEMORY_FABRIC_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F133 | `05_INACTIVE_CANDIDATE/NH_SECURITY_STORAGE_ENCRYPTION_INTENT_v0_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F134 | `05_INACTIVE_CANDIDATE/NH_TOOLS_FOR_NH_CATEGORY_v0_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F135 | `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F136 | `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_3_CANDIDATE.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F137 | `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | C-7A.6 and cited sub-parts; C-7A.13 and cited sub-parts; C-7A.15 and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. Chapter 3-b: C-READ.7 and C-READ.8 (FR-0125–FR-0133); C-READ.1.12.1 (FR-0123); C-READ.9 (FR-0136). |
| F138 | `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH00.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | Naming/path continuity only; no Chapters 0–2 (carried placement) behavior sourced from this chapter. |

### Restored archive coverage

| Row | Source | Read scope | Placement |
|---|---|---|---|
| A-ARCH1 | `98_HISTORICAL_SOURCES_PRE_V10/sources/NH_MASTER-11.md` | Earlier whole-read credit at the same pin; not newly read whole in this piece | C-7B and cited sub-parts; all unrelated archive text excluded from behavior. |
| A-ARCH2 | `98_HISTORICAL_SOURCES_PRE_V10/sources/NH_MASTER-14_FINAL.md` | Earlier whole-read credit at the same pin; not newly read whole in this piece | C-7B.9 and cited sub-parts; all unrelated archive text excluded from behavior.  Chapter 3-b: §6B idempotency_key and §11 item 21 interpretation-integrity passages reopened; C-READ.1.12.1 and C-READ.9. |
| A-ARCH3 | `98_HISTORICAL_SOURCES_PRE_V10/sources/NH_Universal_Filter_RULES.md` | Earlier whole-read credit at the same pin; not newly read whole in this piece | C-7A.6 and cited sub-parts; C-7A.13 and cited sub-parts; C-7A.15 and cited sub-parts; all unrelated archive text excluded from behavior. |
| A-ARCH4 | `98_HISTORICAL_SOURCES_PRE_V10/sources_recovered/NH_FINAL_MASTER_RECOVERY_STAGE_3A_SUPPLEMENTAL_CANDIDATE_INTAKE_v1_1.md` | Earlier whole-read credit at the same pin; not newly read whole in this piece | C-7B.10.2 and cited sub-parts; C-7B.10.3 and cited sub-parts; C-7B.10.4 and cited sub-parts; all unrelated archive text excluded from behavior. |
| A-ARCH5 | `98_HISTORICAL_SOURCES_PRE_V10/sources_recovered/NH_MASTER-19_CORRECTED_v8(1).md` | Earlier whole-read credit at the same pin; not newly read whole in this piece | C-7B.10.2 and cited sub-parts; C-7B.10.3 and cited sub-parts; C-7B.10.4 and cited sub-parts; all unrelated archive text excluded from behavior. |
| A-ARCH6 | `98_HISTORICAL_SOURCES_PRE_V10/sources/NH_MASTER-14_FINAL__2_.md` | Newly read whole, all 434 lines; exact pinned Git blob verified | C-READ.7 and C-READ.8 from §11 item 27 only; every unrelated archive passage excluded from behavior. |

### V10 heading coverage

| Row | Exact source heading | Placement or reason |
|---|---|---|
| V10-H001 | ### This is `NH_MASTER-20_CORRECTED_v10.md`, a corrected candidate in the Master 20 lineage. It is NOT YET ADOPTED. `NH_MASTER-19_CORRECTED_v7_1.md` (SHA-256: `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf`) remains the authoritative immutable Master until Ness explicitly adopts the corrected Master 20. | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H002 | ### Historical provenance (Master 19 lineage): | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H003 | ## 0. THE PREMISE — NEVER DECIDE FACTS (NEVER CLOSE THE BOOK)  [DESIGNED — the floor under every rule] | Partial placement: C-7A and cited sub-parts; C-7B.9.3. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ interpretation remains revisable. |
| V10-H004 | ## 0A. THE TWO MACHINERIES — DUMB vs SMART (psychologics)  [DESIGNED — top-level frame] | Partial placement: C-7A and cited sub-parts; C-7B.1 and cited sub-parts; C-7B.2.5; C-7B.3.2; C-7B.3.3; C-7B.9 and cited sub-parts; C-7B.11 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ record-carriage boundary; no new interpretation by the writer. |
| V10-H005 | ## 0B. FULL-TRANSPARENCY AND LIVING-RECORD LAW  [DESIGNED — foundational operating rule] | C-7A.16 and cited sub-parts; C-7A.17 and cited sub-parts; C-7B and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. Chapter 3-b: C-READ.6 operation records and health-check operation recording. |
| V10-H006 | ## 1. WHAT N.H IS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H007 | ## 1A. THE INPUT-AGNOSTIC PRINCIPLE — ONE ENGINE, MANY FRONT DOORS  [DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H008 | ## 2. HOW TO WORK WITH NESS | Chapter 1 placement retained. §2 wording is carried in the marked conflict at C-7B.8; no new C-2 behavior here. |
| V10-H009 | ### 2A. INTERACTION AND ARTIFACT DELIVERY — LOCKED | Chapter 1 placement retained. §2 wording is carried in the marked conflict at C-7B.8; no new C-2 behavior here. |
| V10-H010 | ## 3. THE EVOLUTION — OLD vs NEW (key points) | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H011 | ## 4. THE MACHINE | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H012 | ## 5. THE CODEBASE MAP | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ; C-READ.3; C-READ.4 built functions and paths. |
| V10-H013 | ## 6. WHAT'S BUILT & VERIFIED ON DISK  [BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ built reading boundary. |
| V10-H014 | ## 6A. THE CODE RULES — `.cursorrules` v3.2 (DUAL-ARCHITECTURE, IN FORCE) | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ record and write constraints. |
| V10-H015 | ### IDENTITY AND PERMANENT RULES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H016 | ### THE THREE-LAYER ARCHITECTURE | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H017 | ### SOVEREIGNTY BOUNDARIES BY LAYER | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.2; C-READ.3; C-READ.5. |
| V10-H018 | ### SCHEMA CONSTRAINTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1 and C-READ.2. |
| V10-H019 | ### PRODUCTION READINGS AUTHORIZATION | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.5 and its protections. |
| V10-H020 | ### PROTECTED FILES AND STORES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.4/C-READ.5 destination separation; edit workflow excluded. |
| V10-H021 | ### DRY-RUN PROTOCOL | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H022 | ### §12 INCOMING — CURRENT STATUS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H023 | ## 6B. THE ACCRETIVE STORE — SCHEMA + STATE  [BUILT & VERIFIED] | Partial placement: C-7A.8 and cited sub-parts; C-7B.2.8.4 and cited sub-parts; C-7B.10.1.3; C-7B.11 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ.1 twelve-field representation; C-READ.2; C-READ.3; C-READ.4. |
| V10-H024 | ## 7. THE BIG DESIGN — UNIVERSAL FILTER + MEANING ENGINE  [engines A + B BUILT; §§7E–7P core-conceptually designed S17; §§7D and 7Q partially conceptually designed] | C-7A and C-7B detailed subsections follow. NOT PLACED: engine implementation behavior belongs to Group A. |
| V10-H025 | ### 7A — THE UNIVERSAL FILTER (operating rules): | C-7A and cited sub-parts; C-7B.3 and cited sub-parts; C-7B.11 and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. Chapter 3-b: C-READ reciprocal Universal Filter use; principles retained from Chapter 2. |
| V10-H026 | ### 7B — THE MEANING ENGINE (mechanism): | C-7B and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. |
| V10-H027 | ### 7C — THE FORCED BUILD ORDER (never re-fought): | EXCLUDED: forced build order under §1.3. NOT PLACED: engine implementations belong to Group A. |
| V10-H028 | ## 7D. THE LIVING STATE WEB — PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ grounded reading consumer relationship. |
| V10-H029 | ## 7E. CATALOG FRONT DOOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H030 | ### §7E-TSC DETAILED DESIGN  [ACCEPTED DESIGN WITH LATER CORRECTIONS — NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H031 | ## 7F. CONTEXT RETRIEVAL  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1.9 retrieval audit and genuine no-context audit; retrieval machinery remains with C-7F. |
| V10-H032 | ## 7G. MEANING ENGINE INTERIOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ acceptance/shape distinction and caller relationship; C-READ.3 new-root write handoff also cites the nested §7G-A subsection. |
| V10-H033 | ### §7G CREATION-AWARE MODE  [SETTLED CONCEPT — NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H034 | ## 7H. REREAD LIFECYCLE  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ reread output relationship; detailed orchestration remains with C-7H. |
| V10-H035 | ## 7I. VIEW LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ history/current-view use; view machinery remains with C-7I. |
| V10-H036 | ## 7J. CONTRADICTION AND CLASH HANDLING  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ clash-consumer relationship; clash machinery remains with C-7J. |
| V10-H037 | ## 7K. STORY LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7A.8.3; C-7B.3.1; C-7B.3.3 and cited sub-parts; C-7B.3.4. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ.1.5/1.6 speaker/perspective and embedded-v1-telling boundaries; future telling identity remains for its accepted package. |
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

### Detailed current-source landing map

| Source passage | Landing and scope |
|---|---|
| V10 §6B reading schema; §6A schema constraints | C-READ.1 and all twelve field bindings; mode object keeps its Chapter 2 canonical IDs. |
| V10 status table — validator, writer, shared helper, quarantine rows | BUILT eligibility for C-READ’s existing shape/write functions and quarantine; no status table is reproduced. |
| V10 §7F audit trail and genuine no-context handling | C-READ.1.9 retrieval provenance and four no-context qualifications; no retrieval policy invented. |
| V10 §7G-A job-level idempotency and Steps 5/5A | C-READ.3 new-root handoff, existing-reading recovery, exact write-failure outcome and checkpoint. |
| V10 §6A production authorization | C-READ.5 protections and approval scope; coding-process rituals excluded under §1.3. |
| MAP C-READ; V10 §0B | C-READ.6 operation classes, one-operation/one-log and access boundary. |
| September 25 record §4 Group 6; named archive §11 item 27 | C-READ.7/C-READ.8; all nine restoration rows FR-0125–FR-0133 explicitly placed. |
| September 25 record §4 Group 5; named archive §6B and §11 item 21 | C-READ.1.12.1 optional hash and C-READ.9 interpretation-integrity requirement; other hardening requirements remain for their owning scope. |

## READ RECORD

### Files newly read whole for this piece

The archive was read in consecutive ranges 1–115, 116–278, 279–377 and 378–434; only the restored §11 item 27 scope supplies behavior. The normalization file was read whole for accepted-owner navigation, not used as behavioral authority.
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_CANDIDATE_v1_4.md`
- `98_HISTORICAL_SOURCES_PRE_V10/sources/NH_MASTER-14_FINAL__2_.md`

Instruction file reopened in full at the start and reopened for the final checklist: `NH_MASTER-21_SYSTEM_BEHAVIOR_BUILD_CONTRACT_FOR_CHATGPT_v1_0.md`; verified SHA-256 `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1`. The attached project instructions, simple-explanation instructions and feasibility/simplicity handoff were read whole as working instructions, not governance behavior sources.

### Earlier whole-read files reopened in part

| File | Current scope | Whole-read credit |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Status table and reading-writer preamble; §0/0A/0B; §5/6/6A/6B; §7D/7F/7G; §7G-A job idempotency and Steps 5/5A; §7H/7I/7J/7K/7M; §7L excerpts; §11 items 18–27 and surrounding headings. | Passed Chapters 1–3-a at the same pin; no new whole-read claim. |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | §3A–3C; heading/navigation searches. | Passed Chapters 1–3-a at the same pin; no new whole-read claim. |
| `01_AUTHORITATIVE/cursorrules` | §1C in full; headings/search matches. | Passed Chapters 1–3-a at the same pin; no new whole-read claim. |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Group A cards, C-READ and neighbors; CY-A and CY-F; component naming inventory. | Passed Chapters 1–3-a at the same pin; no new whole-read claim. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | §4 Groups 5/6 and FR-0123, FR-0125–FR-0136 source pointers. | Passed Chapters 1–3-a at the same pin; no new whole-read claim. |
| `98_HISTORICAL_SOURCES_PRE_V10/sources/NH_MASTER-14_FINAL.md` | §6B optional content-hash passage and §11 item 21 interpretation-integrity passage. | Passed Chapters 1–3-a at the same pin; no new whole-read claim. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | §10 cross-batch reading/index contract; headings; boundary check only. | Passed Chapters 1–3-a at the same pin; no new whole-read claim. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Brief navigation excerpt only; no new behavior sourced. | Passed Chapters 1–3-a at the same pin; no new whole-read claim. |

The current decision index was searched only for accepted-package navigation. B16, B24 and A2 mechanisms were not reconstructed from snippets or normalization summaries. The ledger supplied no behavior. Chapter 2 and Chapter 3-a were inspected for canonical names and reciprocal relationships; their bytes were not edited.

### READ-folder files not yet read

103 READ-folder entries retain their earlier pending reading status. This carries the Chapter 3-a list forward and removes only the normalization file newly read whole; the archive is tracked separately. The ledger has the contract’s Stage-2-only exception. No scope or status summary substitutes for reading an outstanding behavior source whole.

- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_GOLD_CASES_MISSING_SOURCE_BLOCKER_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md`
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
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_PACKAGE_COMPLETE_RECORD_v1_0.md`
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
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_PACKAGE_COMPLETE_RECORD_v1_0.md`
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
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md`
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

### Pinned identities checked for this piece

| File | Bytes | SHA-256 | Git blob at pin |
|---|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | 506934 | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` | MATCH |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | 37048 | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` | MATCH |
| `01_AUTHORITATIVE/cursorrules` | 34821 | `5050d08825b93acd72a79d07946e43c8cbe537e079517ccfe66bcae8e30e96e9` | MATCH |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | 286256 | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` | MATCH |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | 75951 | `9f6f9cac1e07ab14f0c6f3ed834b8260265dac6f6a430fa12be5c6e4c3f0b59f` | MATCH |
| `98_HISTORICAL_SOURCES_PRE_V10/sources/NH_MASTER-14_FINAL.md` | 94146 | `6dc26159e1862ec96d749581567f74d285490dd515775b77b6fbd7cb53e6f5c3` | MATCH |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | 138653 | `baca06e562027a080dab4384943bfb87947c6f598b36776f1016fa8472384a87` | MATCH |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | 26884 | `b37f965a343dbf86130f96591d58de9288ad0a746a68e8ae8fdd7b66208a63da` | MATCH |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_CANDIDATE_v1_4.md` | 29919 | `5ebddb536201e8d39794297088752ba4c2925a1be706ff29c55e1a45b42ea6fa` | MATCH |
| `98_HISTORICAL_SOURCES_PRE_V10/sources/NH_MASTER-14_FINAL__2_.md` | 101638 | `55fab7e730cb1f4b320b02411fbca954fc15259d7f13574b661af5d77c3fd720` | MATCH |

## CONTRACT CHECK

CONTRACT CHECK (against the cloned contract, SHA-256 e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1)
§1.3 no history/actions/roles/workflow in this chapter: PASS — the 173 behavior templates contain operational behavior and permissions, with source histories, project roles and build rituals excluded; delivery/read metadata remains separate.
§1.4 every gap written as NOT DECIDED: PASS — 699 empty template fields and 58 finer schema/behavior gaps are registered by part and field; no unknown source-reliability sentinel or numeric health threshold is supplied.
§1.5 conflicts marked, none resolved: PASS — C-READ.1.12 preserves the V10 per-store versus cursorrules any-store key-scope conflict, with V10 governing.
§3 exactly one stamp per line: PASS — 1,007 filled behavior lines and 190 USED BY rows checked; BUILT limited to V10’s built validator/writer/helper/routing/quarantine/engine capabilities; the restored rules use DECIDED-2026-09-25.
§4 every behavior line cited in the exact format: PASS — all filled template lines and use rows cited; 43 distinct source targets checked, including both the decision record and named archive for every restored part; empty fields have no citation.
§5.4 one name per thing: PASS — C-READ uses the Map name; existing Chapter 2 mode/NOTE IDs and Chapter 3-a common-helper IDs retain their names; new stored-member bindings are identified separately from their producing concepts.
§6 all template fields present, in order, for every part: PASS — all 173 templates have the nine fields, ALONE, TOGETHER, USED BY and SUB-PARTS, in order.
§6.3 reciprocity within this chapter: PASS — all 178 internal relationship pairs checked in both directions; seven existing Chapter 2/3-a endpoint relationships reciprocated; future owning-component obligations listed explicitly.
§6.4 every decided detail written in, no citation used in place of content: PASS — scoped v1 record/write content checked against V10 §6A/6B, the writer preamble, §7F audit and §7G-A write handoff; all FR-0125–FR-0133 details, FR-0123 and FR-0136 written out. Accepted telling identity and promotion/evaluation remain explicitly pending separate pieces, not claimed complete here.
§6.5 sub-parts recursed to the bottom: PASS — twelve record members and nested provenance/values, writer arguments, shape conditions/refusal outcomes, write-failure fields, production conditions/approval scope, named operation classes, bootstrap alternatives and six health-query classes decomposed. All 173 parts belong to the C-READ tree; no new top-level part or invented path is introduced.
§9 coverage matrix rows added for every file used: PASS — all 138 READ-folder rows and 107 V10 heading rows retained, current placements added, restored archive coverage added, ten current source identities matched to the pinned Git blobs.
§10.11 no recommendation, no sentence addressed to Ness: PASS — checked throughout the behavior text and register contributions.
Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_CANDIDATE_v1_4.md`; `98_HISTORICAL_SOURCES_PRE_V10/sources/NH_MASTER-14_FINAL__2_.md`; instruction file `NH_MASTER-21_SYSTEM_BEHAVIOR_BUILD_CONTRACT_FOR_CHATGPT_v1_0.md`. Earlier whole reads and current scoped rereads are listed separately in READ RECORD.

Chapter 3-a remains byte-identical at SHA-256 `d73b9bb7a5cccfcd9cdff79ebb66ccd143de81f2ca4dc1e50558d8ff5fdf5f0d`. This check is the producing assistant’s contract check, not an independent audit or adoption of this candidate.
