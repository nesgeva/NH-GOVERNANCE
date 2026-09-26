# Chapter 3-f — Group A: C-GOLD, evaluation operations, trial execution and concurrency

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-f.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`

This piece extends the Group A evaluation-evidence connection. C-GOLD owns the evaluation machinery; C-READ.11 retains per-reading promotion. Chapter 3-e defines the bridge identities, record contracts and currentness; Chapter 3-f defines the operation catalog, trial execution, twelve boundary contracts, concurrency and unresolved-attempt recovery. The protected judgment claim/authority lifecycle, complete aggregate/result derivation and applicability decomposition remain for later pieces. This pair does not complete C-GOLD, the bridge or Group A.

Authority order: V10 → Decision Defaults v2_2 → cursorrules → Companion v1; the Map is subordinate. Every behavior line in this pair is ACCEPTED, sourced from the exact accepted bridge v1.7. Its source remains in 05_ACTIVE_CANDIDATE; receipt §§3–5 records acceptance of SHA-256 `04dd5abc42e59afb61b4d280a0bb69d647d187fd0da385bc5c567eddbca81a41`. The frozen candidate header does not erase that acceptance. No bridge behavior or link is stamped BUILT.

Citation keys: `05/` = `05_ACTIVE_CANDIDATE/`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = the current Design and Wiring Map v1.6. NHD-B16EEB names this accepted bridge, distinct from NHD-B16. Source-local D-labels are expanded to the receipt’s globally unique NHD-B16EEB-D… identifiers; no slot value is selected.

All bridge field, record, state, event and operation names remain proposed as in the accepted source. No serialization, storage, algorithm, framework or lock is selected. A field card describes a member of its containing record, not a separate service. Record-level failure consequences are labelled as such. Relation and reciprocal entries written here stay here; concatenation never edits or merges an earlier chapter.

<!-- BEGIN CHAPTER 3-f BEHAVIOR -->

### C-GOLD.1.5 — Evaluation operations and trial execution
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The operation and trial lifecycle, its canonical boundaries and concurrency rules. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Takes in: ACCEPTED — Registered setup, opened runs, planned trials and durable canonical state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Does: ACCEPTED — Executes under one-terminal/one-log ownership, output uniqueness, B9 admission and lookup-first recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Gives out: ACCEPTED — Traceable canonical effects and honest operation outcomes. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Must never: ACCEPTED — Retry completed or unknown outputs, duplicate terminals/logs or acknowledge before required terminal and log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unknown effects stay unresolved; refused domain preconditions are not machine-retried; exhausted append attempts leave the requester pending. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: Keeps state records separate from operational logs; emits exactly one append-only §0B log per real operation at its terminal, before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2 — Operation terminal catalog: Gives each operation one terminal and one log; pending work has no invented terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.3 — Run closing conditions: Allows E8 only after all started attempts have a terminal and no planned-trial attempt is live or admitted-unstarted. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.4 — Frozen terminal set: Freezes and digests the set; E10 computes from precisely this set plus later E7r records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.5 — One output per planned trial: Derives planned_trial_output_key deterministically; uses it as the reading’s idempotency_key; at most one output commits. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.6 — B9-governed technical re-attempts: Routes each outcome by its accepted retry class; every ordinal ≥ 2 needs B9 admission under unchanged canonical identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.7 — Actual execution-context classification: Uses B9 background/nightly classification unless evaluation executed through the live-chat front door. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.6] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.8 — Concurrent heads and deterministic identities: Admits only the current predecessor and identical canonical content; preserves contradictions and refuses stale domain preconditions. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.9 — Evaluation transaction boundaries: Applies the owning record and rule contracts before each durable transition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.10 — Evaluation idempotency keys: Uses the source-defined key for each record kind; identical repeats absorb where specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.11 — Unresolved-attempt resolution semantics: Derives effective attempt and run states without rewriting E7/E8; permits at most one conclusive E7r. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12 — Run and concurrency recovery: Finds committed effects, fills missing records/logs only from evidence, and keeps unknown effects blocked. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.13 — Requesting operation after append exhaustion: Keeps the requesting domain operation honestly open/pending with no terminal because its record has not committed; B9 records the stopping gate and preserved state. Only a new B9 episode with consumed real-change and unchanged inputs may continue. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1 — Promotion evaluation-evidence bridge | Registered setup, opened runs, planned trials and durable canonical state. | Executes under one-terminal/one-log ownership, output uniqueness, B9 admission and lookup-first recovery. | Traceable canonical effects and honest operation outcomes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.1 — Canonical records and operation-owned logs; C-GOLD.1.5.2 — Operation terminal catalog; C-GOLD.1.5.3 — Run closing conditions; C-GOLD.1.5.4 — Frozen terminal set; C-GOLD.1.5.5 — One output per planned trial; C-GOLD.1.5.6 — B9-governed technical re-attempts; C-GOLD.1.5.7 — Actual execution-context classification; C-GOLD.1.5.8 — Concurrent heads and deterministic identities; C-GOLD.1.5.9 — Evaluation transaction boundaries; C-GOLD.1.5.10 — Evaluation idempotency keys; C-GOLD.1.5.11 — Unresolved-attempt resolution semantics; C-GOLD.1.5.12 — Run and concurrency recovery; C-GOLD.1.5.13 — Requesting operation after append exhaustion

### C-GOLD.1.5.1 — Canonical records and operation-owned logs
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Canonical records and operation-owned logs rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [NHD-B16EEB]
- Takes in: ACCEPTED — A canonical state record or a real operation reaching its terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [NHD-B16EEB]
- Does: ACCEPTED — Keeps state records separate from operational logs; emits exactly one append-only §0B log per real operation at its terminal, before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [NHD-B16EEB]
- Gives out: ACCEPTED — One operation-owned log, without extra evidentiary votes. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [NHD-B16EEB]
- Must never: ACCEPTED — Count canonical records as operational logs or duplicate B9’s own retry-request logs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement waits for the operation’s terminal log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5 — Evaluation operations and trial execution | A canonical state record or a real operation reaching its terminal. | Keeps state records separate from operational logs; emits exactly one append-only §0B log per real operation at its terminal, before acknowledgement. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.2.1 — O-SUITE | A canonical state record or a real operation reaching its terminal. | One terminal and one operation-owned log must be durable before acknowledgement. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.2.1.1 — O-SUITE registered | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.2.1.2 — O-SUITE refused | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.5.2.2 — O-SETUP | A canonical state record or a real operation reaching its terminal. | One terminal and one operation-owned log must be durable before acknowledgement. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.5.2.2.1 — O-SETUP registered | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.5.2.2.2 — O-SETUP refused | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.5.2.3 — O-RUN | A canonical state record or a real operation reaching its terminal. | One terminal and one operation-owned log must be durable before acknowledgement. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 9 · ACCEPTED | C-GOLD.1.5.2.3.1 — O-RUN run_completed | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 10 · ACCEPTED | C-GOLD.1.5.2.3.2 — O-RUN run_closed_incomplete | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 11 · ACCEPTED | C-GOLD.1.5.2.3.3 — O-RUN run_indeterminate | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 12 · ACCEPTED | C-GOLD.1.5.2.4 — O-ATTEMPT | A canonical state record or a real operation reaching its terminal. | One terminal and one operation-owned log must be durable before acknowledgement. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 13 · ACCEPTED | C-GOLD.1.5.2.4.1 — O-ATTEMPT attempt_completed | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 14 · ACCEPTED | C-GOLD.1.5.2.4.2 — O-ATTEMPT attempt_failed | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 15 · ACCEPTED | C-GOLD.1.5.2.4.3 — O-ATTEMPT attempt_interrupted_abandoned | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 16 · ACCEPTED | C-GOLD.1.5.2.4.4 — O-ATTEMPT attempt_unresolved | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 17 · ACCEPTED | C-GOLD.1.5.2.5 — O-RESOLVE-ATTEMPT | A canonical state record or a real operation reaching its terminal. | One terminal and one operation-owned log must be durable before acknowledgement. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 18 · ACCEPTED | C-GOLD.1.5.2.5.1 — O-RESOLVE-ATTEMPT resolution_committed | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 19 · ACCEPTED | C-GOLD.1.5.2.5.2 — O-RESOLVE-ATTEMPT refused | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 20 · ACCEPTED | C-GOLD.1.5.2.6 — O-JUDGE | A canonical state record or a real operation reaching its terminal. | One terminal and one operation-owned log must be durable before acknowledgement. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 21 · ACCEPTED | C-GOLD.1.5.2.6.1 — O-JUDGE judgment_committed | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 22 · ACCEPTED | C-GOLD.1.5.2.6.2 — O-JUDGE judgment_absorbed | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 23 · ACCEPTED | C-GOLD.1.5.2.6.3 — O-JUDGE judgment_refused_stale_head | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 24 · ACCEPTED | C-GOLD.1.5.2.6.4 — O-JUDGE judgment_refused_authority | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 25 · ACCEPTED | C-GOLD.1.5.2.6.5 — O-JUDGE judgment_refused_mode_mismatch | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 26 · ACCEPTED | C-GOLD.1.5.2.6.6 — O-JUDGE judgment_refused_output_invalid | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 27 · ACCEPTED | C-GOLD.1.5.2.6.7 — O-JUDGE judgment_claim_lost | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 28 · ACCEPTED | C-GOLD.1.5.2.6.8 — O-JUDGE judgment_authorization_failed | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 29 · ACCEPTED | C-GOLD.1.5.2.7 — O-AGGREGATE | A canonical state record or a real operation reaching its terminal. | One terminal and one operation-owned log must be durable before acknowledgement. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 30 · ACCEPTED | C-GOLD.1.5.2.7.1 — O-AGGREGATE aggregate_committed | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 31 · ACCEPTED | C-GOLD.1.5.2.7.2 — O-AGGREGATE aggregate_absorbed | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 32 · ACCEPTED | C-GOLD.1.5.2.7.3 — O-AGGREGATE aggregate_refused_stale_head | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 33 · ACCEPTED | C-GOLD.1.5.2.8 — O-RESULT | A canonical state record or a real operation reaching its terminal. | One terminal and one operation-owned log must be durable before acknowledgement. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 34 · ACCEPTED | C-GOLD.1.5.2.8.1 — O-RESULT result_committed | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 35 · ACCEPTED | C-GOLD.1.5.2.8.2 — O-RESULT result_absorbed | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 36 · ACCEPTED | C-GOLD.1.5.2.8.3 — O-RESULT result_contradiction | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 37 · ACCEPTED | C-GOLD.1.5.2.9 — O-EVREF | A canonical state record or a real operation reaching its terminal. | One terminal and one operation-owned log must be durable before acknowledgement. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 38 · ACCEPTED | C-GOLD.1.5.2.9.1 — O-EVREF issued | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 39 · ACCEPTED | C-GOLD.1.5.2.9.2 — O-EVREF refused | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 40 · ACCEPTED | C-GOLD.1.5.2.10 — O-INVALIDITY | A canonical state record or a real operation reaching its terminal. | One terminal and one operation-owned log must be durable before acknowledgement. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 41 · ACCEPTED | C-GOLD.1.5.2.10.1 — O-INVALIDITY committed | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 42 · ACCEPTED | C-GOLD.1.5.2.10.2 — O-INVALIDITY refused | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 43 · ACCEPTED | C-GOLD.1.5.2.11 — O-CONFLICT | A canonical state record or a real operation reaching its terminal. | One terminal and one operation-owned log must be durable before acknowledgement. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 44 · ACCEPTED | C-GOLD.1.5.2.11.1 — O-CONFLICT committed | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 45 · ACCEPTED | C-GOLD.1.5.2.11.2 — O-CONFLICT refused | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 46 · ACCEPTED | C-GOLD.1.5.2.12 — O-RECOVERY | A canonical state record or a real operation reaching its terminal. | One terminal and one operation-owned log must be durable before acknowledgement. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 47 · ACCEPTED | C-GOLD.1.5.2.12.1 — O-RECOVERY recovery_applied | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 48 · ACCEPTED | C-GOLD.1.5.2.12.2 — O-RECOVERY recovery_noop | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 49 · ACCEPTED | C-GOLD.1.5.2.13 — O-APPEND | A canonical state record or a real operation reaching its terminal. | One terminal and one operation-owned log must be durable before acknowledgement. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 50 · ACCEPTED | C-GOLD.1.5.2.13.1 — O-APPEND appended | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 51 · ACCEPTED | C-GOLD.1.5.2.13.2 — O-APPEND absorbed | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 52 · ACCEPTED | C-GOLD.1.5.2.13.3 — O-APPEND lost_race_technical | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 53 · ACCEPTED | C-GOLD.1.5.2.13.4 — O-APPEND refused_domain_precondition | A canonical state record or a real operation reaching its terminal. | The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 54 · ACCEPTED | C-GOLD.1.5.12.8 — CR-8 — E7 present, attempt log absent | A canonical state record or a real operation reaching its terminal. | Recovery follows this rule: Keeps state records separate from operational logs; emits exactly one append-only §0B log per real operation at its terminal, before acknowledgement. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [NHD-B16EEB] |
| 55 · ACCEPTED | C-GOLD.1.5.12.10 — CR-10 — E8 present, run log absent | A canonical state record or a real operation reaching its terminal. | Recovery follows this rule: Keeps state records separate from operational logs; emits exactly one append-only §0B log per real operation at its terminal, before acknowledgement. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [NHD-B16EEB] |
| 56 · ACCEPTED | C-GOLD.1.5.9.1 — EB-1 — Suite registration | A canonical state record or a real operation reaching its terminal. | Acknowledgement waits for the owning terminal and its one operational log. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 57 · ACCEPTED | C-GOLD.1.5.9.2 — EB-2 — Setup registration | A canonical state record or a real operation reaching its terminal. | Acknowledgement waits for the owning terminal and its one operational log. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 58 · ACCEPTED | C-GOLD.1.5.9.3 — EB-3 — Run open | A canonical state record or a real operation reaching its terminal. | Acknowledgement waits for the owning terminal and its one operational log. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 59 · ACCEPTED | C-GOLD.1.5.9.4 — EB-4 — Attempt start | A canonical state record or a real operation reaching its terminal. | Acknowledgement waits for the owning terminal and its one operational log. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 60 · ACCEPTED | C-GOLD.1.5.9.5 — EB-5 — Attempt terminal | A canonical state record or a real operation reaching its terminal. | Acknowledgement waits for the owning terminal and its one operational log. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 61 · ACCEPTED | C-GOLD.1.5.9.6 — EB-6 — Attempt resolution | A canonical state record or a real operation reaching its terminal. | Acknowledgement waits for the owning terminal and its one operational log. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 62 · ACCEPTED | C-GOLD.1.5.9.7 — EB-7 — Run terminal | A canonical state record or a real operation reaching its terminal. | Acknowledgement waits for the owning terminal and its one operational log. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 63 · ACCEPTED | C-GOLD.1.5.9.8 — EB-8 — Protected judgment | A canonical state record or a real operation reaching its terminal. | Acknowledgement waits for the owning terminal and its one operational log. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 64 · ACCEPTED | C-GOLD.1.5.9.9 — EB-9 — Aggregate | A canonical state record or a real operation reaching its terminal. | Acknowledgement waits for the owning terminal and its one operational log. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 65 · ACCEPTED | C-GOLD.1.5.9.10 — EB-10 — Result derivation | A canonical state record or a real operation reaching its terminal. | Acknowledgement waits for the owning terminal and its one operational log. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 66 · ACCEPTED | C-GOLD.1.5.9.11 — EB-11 — Evidence reference | A canonical state record or a real operation reaching its terminal. | Acknowledgement waits for the owning terminal and its one operational log. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 67 · ACCEPTED | C-GOLD.1.5.9.12 — EB-12 — Invalidity or conflict | A canonical state record or a real operation reaching its terminal. | Acknowledgement waits for the owning terminal and its one operational log. | One operation-owned log, without extra evidentiary votes. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2 — Operation terminal catalog
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The named operations and their exact terminal vocabularies. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5]
- Takes in: ACCEPTED — One operation identity and its canonical record effects. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5]
- Does: ACCEPTED — Gives each operation one terminal and one log; pending work has no invented terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5]
- Gives out: ACCEPTED — A terminal from the operation’s own vocabulary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5]
- Must never: ACCEPTED — Give one operation ID two terminals or two logs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5]
- Fails closed by: ACCEPTED — A requested scope record must commit through O-APPEND before its successful requesting operation can terminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.2.1 — O-SUITE: Registers an accepted suite after its integrity, seal and acceptance checks. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.2 — O-SETUP: Registers one setup record; E3 must satisfy all required declarations. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.3 — O-RUN: Owns one evaluation run and its honest closing outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.4 — O-ATTEMPT: Owns one planned-trial attempt; B9 launches ordinal ≥ 2. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.5 — O-RESOLVE-ATTEMPT: Resolves an unresolved attempt by lookup, recording the outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.6 — O-JUDGE: Owns the protected claim → conditional BAI receipt → E9 protocol; stages are separately durable, not one atomic transaction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.7 — O-AGGREGATE: Owns one aggregate derivation against its expected prior head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.8 — O-RESULT: Derives one deterministic result at one scope ledger head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.9 — O-EVREF: Issues only a narrow valid B16 evidence reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.10 — O-INVALIDITY: Records a policy-authorized objective invalidity exclusion. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.11 — O-CONFLICT: Records a policy-authorized completed-run conflict resolution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.12 — O-RECOVERY: Uses lookup-first recovery; repeated resolved work is a no-op. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.13 — O-APPEND: Atomically commits the requested scope-relevant canonical record with its ledger entry under both head comparison and the record’s domain preconditions. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: §7Q governs these records/ledgers/logs before relevance; applicable SACL scope must allow access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5 — Evaluation operations and trial execution | One operation identity and its canonical record effects. | Gives each operation one terminal and one log; pending work has no invented terminal. | A terminal from the operation’s own vocabulary. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.2.1 — O-SUITE; C-GOLD.1.5.2.2 — O-SETUP; C-GOLD.1.5.2.3 — O-RUN; C-GOLD.1.5.2.4 — O-ATTEMPT; C-GOLD.1.5.2.5 — O-RESOLVE-ATTEMPT; C-GOLD.1.5.2.6 — O-JUDGE; C-GOLD.1.5.2.7 — O-AGGREGATE; C-GOLD.1.5.2.8 — O-RESULT; C-GOLD.1.5.2.9 — O-EVREF; C-GOLD.1.5.2.10 — O-INVALIDITY; C-GOLD.1.5.2.11 — O-CONFLICT; C-GOLD.1.5.2.12 — O-RECOVERY; C-GOLD.1.5.2.13 — O-APPEND

### C-GOLD.1.5.2.1 — O-SUITE
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-SUITE operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — E1. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Registers an accepted suite after its integrity, seal and acceptance checks. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — Exactly one of registered, refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Emit two terminals/logs under this operation identity or acknowledge before its terminal and log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No benchmark manifest without NHD-B16EEB-D15; no held-out manifest without an accepted held-out policy. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.2.1.1 — O-SUITE registered: Records registered as this operation’s terminal; emits eval_suite_registered once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.1.2 — O-SUITE refused: Records refused as this operation’s terminal; emits eval_suite_refused once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: One terminal and one operation-owned log must be durable before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.2 — evaluation_suite_manifest (E1): Registers only after integrity, seal and acceptance checks; benchmark suites additionally require an accepted concrete suite; held-out requires its accepted policy. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.2 — evaluation_suite_manifest (E1): appends the E1 canonical record when its stated commit conditions hold; earlier records remain unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2 — Operation terminal catalog | E1. | Registers an accepted suite after its integrity, seal and acceptance checks. | Exactly one of registered, refused. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.2.1.1 — O-SUITE registered; C-GOLD.1.5.2.1.2 — O-SUITE refused

### C-GOLD.1.5.2.1.1 — O-SUITE registered
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-SUITE registered rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-SUITE ending with registered. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records registered as this operation’s terminal; emits eval_suite_registered once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal registered and log eval_suite_registered. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.1 — O-SUITE | O-SUITE ending with registered. | Records registered as this operation’s terminal; emits eval_suite_registered once. | One terminal registered and log eval_suite_registered. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.1.2 — O-SUITE refused
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-SUITE refused rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-SUITE ending with refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records refused as this operation’s terminal; emits eval_suite_refused once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal refused and log eval_suite_refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.1 — O-SUITE | O-SUITE ending with refused. | Records refused as this operation’s terminal; emits eval_suite_refused once. | One terminal refused and log eval_suite_refused. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.2 — O-SETUP
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-SETUP operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — one E2e / E3 / E4 / E4S. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Registers one setup record; E3 must satisfy all required declarations. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — Exactly one of registered, refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Emit two terminals/logs under this operation identity or acknowledge before its terminal and log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Any of the four missing-coverage conditions refuses registration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Incomplete or non-current epoch blocks evidentiary run opening and execution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.2.2.1 — O-SETUP registered: Records registered as this operation’s terminal; emits eval_setup_registered once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.2.2 — O-SETUP refused: Records refused as this operation’s terminal; emits eval_setup_refused once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: One terminal and one operation-owned log must be durable before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.4.4 — Coverage profile registration gate: When registering this setup record kind: Refuses omitted family, omitted scope, undeclared measurement or absent gold cell. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.2.3 — policy_epoch (E2e): When registering this setup record kind: Binds every required current accepted version; currentness lasts only while every named policy is current. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.2.1 — model_evaluation_profile (E4): When registering this setup record kind: Binds gold v1 to Engine A and gold v2-B to Engine B; each binding carries its own configuration digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.2.2 — system_candidate_profile (E4S): When registering this setup record kind: Binds both roles and the complete handoff as one system candidate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.2.3 — policy_epoch (E2e): For this requested record kind, appends the E2e canonical record when its stated commit conditions hold; earlier records remain unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.4 — required_coverage_profile (E3): For this requested record kind, appends the E3 canonical record when its stated commit conditions hold; earlier records remain unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.2.1 — model_evaluation_profile (E4): For this requested record kind, appends the E4 canonical record when its stated commit conditions hold; earlier records remain unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.2.2 — system_candidate_profile (E4S): For this requested record kind, appends the E4S canonical record when its stated commit conditions hold; earlier records remain unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2 — Operation terminal catalog | one E2e / E3 / E4 / E4S. | Registers one setup record; E3 must satisfy all required declarations. | Exactly one of registered, refused. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.2.2.1 — O-SETUP registered; C-GOLD.1.5.2.2.2 — O-SETUP refused

### C-GOLD.1.5.2.2.1 — O-SETUP registered
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-SETUP registered rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-SETUP ending with registered. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records registered as this operation’s terminal; emits eval_setup_registered once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal registered and log eval_setup_registered. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.2 — O-SETUP | O-SETUP ending with registered. | Records registered as this operation’s terminal; emits eval_setup_registered once. | One terminal registered and log eval_setup_registered. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.2.2 — O-SETUP refused
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-SETUP refused rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-SETUP ending with refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records refused as this operation’s terminal; emits eval_setup_refused once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal refused and log eval_setup_refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.2 — O-SETUP | O-SETUP ending with refused. | Records refused as this operation’s terminal; emits eval_setup_refused once. | One terminal refused and log eval_setup_refused. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.3 — O-RUN
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-RUN operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — E5 and E8, plus E16. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Owns one evaluation run and its honest closing outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — Exactly one of run_completed, run_closed_incomplete, run_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Emit two terminals/logs under this operation identity or acknowledge before its terminal and log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unknown evidence, integrity failure or contradiction cannot yield run_completed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.2.3.1 — O-RUN run_completed: Records run_completed as this operation’s terminal; emits eval_run_terminal once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.3.2 — O-RUN run_closed_incomplete: Records run_closed_incomplete as this operation’s terminal; emits eval_run_terminal once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.3.3 — O-RUN run_indeterminate: Records run_indeterminate as this operation’s terminal; emits eval_run_terminal once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: One terminal and one operation-owned log must be durable before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.3 — Run closing conditions: Allows E8 only after all started attempts have a terminal and no planned-trial attempt is live or admitted-unstarted. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.4 — Frozen terminal set: Freezes and digests the set; E10 computes from precisely this set plus later E7r records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.5 — evaluation_run_open (E5): appends the E5 canonical record when its stated commit conditions hold; earlier records remain unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.9 — evaluation_run_terminal (E8): appends the E8 canonical record when its stated commit conditions hold; earlier records remain unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2 — Operation terminal catalog | E5 and E8, plus E16. | Owns one evaluation run and its honest closing outcome. | Exactly one of run_completed, run_closed_incomplete, run_indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.2.3.1 — O-RUN run_completed; C-GOLD.1.5.2.3.2 — O-RUN run_closed_incomplete; C-GOLD.1.5.2.3.3 — O-RUN run_indeterminate

### C-GOLD.1.5.2.3.1 — O-RUN run_completed
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-RUN run_completed rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-RUN ending with run_completed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records run_completed as this operation’s terminal; emits eval_run_terminal once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal run_completed and log eval_run_terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.9 — evaluation_run_terminal (E8): Records this run’s single terminal in E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.3 — O-RUN | O-RUN ending with run_completed. | Records run_completed as this operation’s terminal; emits eval_run_terminal once. | One terminal run_completed and log eval_run_terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.3.2 — O-RUN run_closed_incomplete
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-RUN run_closed_incomplete rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-RUN ending with run_closed_incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records run_closed_incomplete as this operation’s terminal; emits eval_run_terminal once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal run_closed_incomplete and log eval_run_terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.9 — evaluation_run_terminal (E8): Records this run’s single terminal in E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.3 — O-RUN | O-RUN ending with run_closed_incomplete. | Records run_closed_incomplete as this operation’s terminal; emits eval_run_terminal once. | One terminal run_closed_incomplete and log eval_run_terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.3.3 — O-RUN run_indeterminate
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-RUN run_indeterminate rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-RUN ending with run_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records run_indeterminate as this operation’s terminal; emits eval_run_terminal once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal run_indeterminate and log eval_run_terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.9 — evaluation_run_terminal (E8): Records this run’s single terminal in E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.3 — O-RUN | O-RUN ending with run_indeterminate. | Records run_indeterminate as this operation’s terminal; emits eval_run_terminal once. | One terminal run_indeterminate and log eval_run_terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.4 — O-ATTEMPT
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-ATTEMPT operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — E6 and E7, plus E16. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Owns one planned-trial attempt; B9 launches ordinal ≥ 2. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — Exactly one of attempt_completed, attempt_failed, attempt_interrupted_abandoned, attempt_unresolved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Emit two terminals/logs under this operation identity or acknowledge before its terminal and log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Completed-output retries absorb as B9 terminal_success; unknown output existence blocks retry. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No admission → no re-attempt; unadmitted E6 is the hidden-retry violation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Conflicting conclusive outcomes are indeterminate; unresolved existence blocks all new attempts for the trial. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.2.4.1 — O-ATTEMPT attempt_completed: Records attempt_completed as this operation’s terminal; emits eval_attempt_terminal once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.4.2 — O-ATTEMPT attempt_failed: Records attempt_failed as this operation’s terminal; emits eval_attempt_terminal once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.4.3 — O-ATTEMPT attempt_interrupted_abandoned: Records attempt_interrupted_abandoned as this operation’s terminal; emits eval_attempt_terminal once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.4.4 — O-ATTEMPT attempt_unresolved: Records attempt_unresolved as this operation’s terminal; emits eval_attempt_terminal once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: One terminal and one operation-owned log must be durable before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.5 — One output per planned trial: Derives planned_trial_output_key deterministically; uses it as the reading’s idempotency_key; at most one output commits. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.6.7 — Committed B9 R1 admission: For ordinal ≥ 2 only: Requires committed B9 R1 admission under accepted identity, budget, gaps, deadline, one-live-attempt and real-change rules. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.11 — Unresolved-attempt resolution semantics: If an earlier attempt is unresolved: Derives effective attempt and run states without rewriting E7/E8; permits at most one conclusive E7r. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.6 — trial_attempt_start (E6): appends the E6 canonical record when its stated commit conditions hold; earlier records remain unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.7 — trial_attempt_terminal (E7): appends the E7 canonical record when its stated commit conditions hold; earlier records remain unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2 — Operation terminal catalog | E6 and E7, plus E16. | Owns one planned-trial attempt; B9 launches ordinal ≥ 2. | Exactly one of attempt_completed, attempt_failed, attempt_interrupted_abandoned, attempt_unresolved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.2.4.1 — O-ATTEMPT attempt_completed; C-GOLD.1.5.2.4.2 — O-ATTEMPT attempt_failed; C-GOLD.1.5.2.4.3 — O-ATTEMPT attempt_interrupted_abandoned; C-GOLD.1.5.2.4.4 — O-ATTEMPT attempt_unresolved

### C-GOLD.1.5.2.4.1 — O-ATTEMPT attempt_completed
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-ATTEMPT attempt_completed rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-ATTEMPT ending with attempt_completed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records attempt_completed as this operation’s terminal; emits eval_attempt_terminal once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal attempt_completed and log eval_attempt_terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.7 — trial_attempt_terminal (E7): Records this attempt’s single terminal in E7. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.4 — O-ATTEMPT | O-ATTEMPT ending with attempt_completed. | Records attempt_completed as this operation’s terminal; emits eval_attempt_terminal once. | One terminal attempt_completed and log eval_attempt_terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.4.2 — O-ATTEMPT attempt_failed
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-ATTEMPT attempt_failed rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-ATTEMPT ending with attempt_failed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records attempt_failed as this operation’s terminal; emits eval_attempt_terminal once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal attempt_failed and log eval_attempt_terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.7 — trial_attempt_terminal (E7): Records this attempt’s single terminal in E7. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.4 — O-ATTEMPT | O-ATTEMPT ending with attempt_failed. | Records attempt_failed as this operation’s terminal; emits eval_attempt_terminal once. | One terminal attempt_failed and log eval_attempt_terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.4.3 — O-ATTEMPT attempt_interrupted_abandoned
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-ATTEMPT attempt_interrupted_abandoned rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-ATTEMPT ending with attempt_interrupted_abandoned. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records attempt_interrupted_abandoned as this operation’s terminal; emits eval_attempt_terminal once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal attempt_interrupted_abandoned and log eval_attempt_terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.7 — trial_attempt_terminal (E7): Records this attempt’s single terminal in E7. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.4 — O-ATTEMPT | O-ATTEMPT ending with attempt_interrupted_abandoned. | Records attempt_interrupted_abandoned as this operation’s terminal; emits eval_attempt_terminal once. | One terminal attempt_interrupted_abandoned and log eval_attempt_terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.4.4 — O-ATTEMPT attempt_unresolved
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-ATTEMPT attempt_unresolved rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-ATTEMPT ending with attempt_unresolved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records attempt_unresolved as this operation’s terminal; emits eval_attempt_terminal once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal attempt_unresolved and log eval_attempt_terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.7 — trial_attempt_terminal (E7): Records this attempt’s single terminal in E7. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.4 — O-ATTEMPT | O-ATTEMPT ending with attempt_unresolved. | Records attempt_unresolved as this operation’s terminal; emits eval_attempt_terminal once. | One terminal attempt_unresolved and log eval_attempt_terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.5 — O-RESOLVE-ATTEMPT
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-RESOLVE-ATTEMPT operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — E7r and E16. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Resolves an unresolved attempt by lookup, recording the outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — Exactly one of resolution_committed, refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Emit two terminals/logs under this operation identity or acknowledge before its terminal and log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Conflicting conclusive outcomes are indeterminate; unresolved existence blocks all new attempts for the trial. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Later contradiction of the conclusive outcome makes state indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.2.5.1 — O-RESOLVE-ATTEMPT resolution_committed: Records resolution_committed as this operation’s terminal; emits eval_attempt_resolved once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.5.2 — O-RESOLVE-ATTEMPT refused: Records refused as this operation’s terminal; emits eval_attempt_resolution_refused once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: One terminal and one operation-owned log must be durable before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.11 — Unresolved-attempt resolution semantics: Derives effective attempt and run states without rewriting E7/E8; permits at most one conclusive E7r. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.11.4 — One conclusive resolution per attempt: Allows at most one resolved_output_found or resolved_absence_proven; further still-undetermined resolutions use their sequence identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.8 — trial_attempt_resolution (E7r): appends the E7r canonical record when its stated commit conditions hold; earlier records remain unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2 — Operation terminal catalog | E7r and E16. | Resolves an unresolved attempt by lookup, recording the outcome. | Exactly one of resolution_committed, refused. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.2.5.1 — O-RESOLVE-ATTEMPT resolution_committed; C-GOLD.1.5.2.5.2 — O-RESOLVE-ATTEMPT refused

### C-GOLD.1.5.2.5.1 — O-RESOLVE-ATTEMPT resolution_committed
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-RESOLVE-ATTEMPT resolution_committed rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-RESOLVE-ATTEMPT ending with resolution_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records resolution_committed as this operation’s terminal; emits eval_attempt_resolved once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal resolution_committed and log eval_attempt_resolved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.5 — O-RESOLVE-ATTEMPT | O-RESOLVE-ATTEMPT ending with resolution_committed. | Records resolution_committed as this operation’s terminal; emits eval_attempt_resolved once. | One terminal resolution_committed and log eval_attempt_resolved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.5.2 — O-RESOLVE-ATTEMPT refused
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-RESOLVE-ATTEMPT refused rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-RESOLVE-ATTEMPT ending with refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records refused as this operation’s terminal; emits eval_attempt_resolution_refused once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal refused and log eval_attempt_resolution_refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.5 — O-RESOLVE-ATTEMPT | O-RESOLVE-ATTEMPT ending with refused. | Records refused as this operation’s terminal; emits eval_attempt_resolution_refused once. | One terminal refused and log eval_attempt_resolution_refused. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.6 — O-JUDGE
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-JUDGE operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — judgment-authorization claim states; E9 and E16 via O-APPEND. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Owns the protected claim → conditional BAI receipt → E9 protocol; stages are separately durable, not one atomic transaction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — Exactly one of judgment_committed, judgment_absorbed, judgment_refused_stale_head, judgment_refused_authority, judgment_refused_mode_mismatch, judgment_refused_output_invalid, judgment_claim_lost, judgment_authorization_failed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Emit two terminals/logs under this operation identity or acknowledge before its terminal and log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unaccepted NHD-B16EEB-D16 refuses every Ness judgment; stale competing heads are refused; fork or identity contradiction is judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Stale successor is judgment_refused_stale_head; a fork or different content under one E9 identity is an integrity contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.2.6.1 — O-JUDGE judgment_committed: Records judgment_committed as this operation’s terminal; emits eval_judgment_committed once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.6.2 — O-JUDGE judgment_absorbed: Records judgment_absorbed as this operation’s terminal; emits eval_judgment_absorbed once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.6.3 — O-JUDGE judgment_refused_stale_head: Records judgment_refused_stale_head as this operation’s terminal; emits eval_judgment_refused_stale_head once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.6.4 — O-JUDGE judgment_refused_authority: Records judgment_refused_authority as this operation’s terminal; emits eval_judgment_refused_authority once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.6.5 — O-JUDGE judgment_refused_mode_mismatch: Records judgment_refused_mode_mismatch as this operation’s terminal; emits eval_judgment_refused_mode_mismatch once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.6.6 — O-JUDGE judgment_refused_output_invalid: Records judgment_refused_output_invalid as this operation’s terminal; emits eval_judgment_refused_output_invalid once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.6.7 — O-JUDGE judgment_claim_lost: Records judgment_claim_lost as this operation’s terminal; emits eval_judgment_claim_lost once. The losing concurrent claim consumes nothing. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.6.8 — O-JUDGE judgment_authorization_failed: Records judgment_authorization_failed as this operation’s terminal; emits eval_judgment_authorization_failed once. Reasons are pre-receipt crash, failed/unverifiable receipt write, refusal before consumption after a claim, or head breach after a durable receipt; claim closure is the consequence, never the cause. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: One terminal and one operation-owned log must be durable before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment (E9): Appends a judgment under the current-head and accepted authority conditions; identical resubmission absorbs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.4 — CAS-3 judgment-head compare-and-extend: Commits E9 only if its expected head is still current and CAS-1 holds; identical submission absorbs; stale competing successor refuses. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment (E9): appends the E9 canonical record when its stated commit conditions hold; earlier records remain unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2 — Operation terminal catalog | judgment-authorization claim states; E9 and E16 via O-APPEND. | Owns the protected claim → conditional BAI receipt → E9 protocol; stages are separately durable, not one atomic transaction. | Exactly one of judgment_committed, judgment_absorbed, judgment_refused_stale_head, judgment_refused_authority, judgment_refused_mode_mismatch, judgment_refused_output_invalid, judgment_claim_lost, judgment_authorization_failed. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.9.8.1 — Authorization claim first | judgment-authorization claim states; E9 and E16 via O-APPEND. | Owns the protected claim → conditional BAI receipt → E9 protocol; stages are separately durable, not one atomic transaction. | Exactly one of judgment_committed, judgment_absorbed, judgment_refused_stale_head, judgment_refused_authority, judgment_refused_mode_mismatch, judgment_refused_output_invalid, judgment_claim_lost, judgment_authorization_failed. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.2.6.1 — O-JUDGE judgment_committed; C-GOLD.1.5.2.6.2 — O-JUDGE judgment_absorbed; C-GOLD.1.5.2.6.3 — O-JUDGE judgment_refused_stale_head; C-GOLD.1.5.2.6.4 — O-JUDGE judgment_refused_authority; C-GOLD.1.5.2.6.5 — O-JUDGE judgment_refused_mode_mismatch; C-GOLD.1.5.2.6.6 — O-JUDGE judgment_refused_output_invalid; C-GOLD.1.5.2.6.7 — O-JUDGE judgment_claim_lost; C-GOLD.1.5.2.6.8 — O-JUDGE judgment_authorization_failed

### C-GOLD.1.5.2.6.1 — O-JUDGE judgment_committed
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-JUDGE judgment_committed rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-JUDGE ending with judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records judgment_committed as this operation’s terminal; emits eval_judgment_committed once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal judgment_committed and log eval_judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.6 — O-JUDGE | O-JUDGE ending with judgment_committed. | Records judgment_committed as this operation’s terminal; emits eval_judgment_committed once. | One terminal judgment_committed and log eval_judgment_committed. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.6.2 — O-JUDGE judgment_absorbed
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-JUDGE judgment_absorbed rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-JUDGE ending with judgment_absorbed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records judgment_absorbed as this operation’s terminal; emits eval_judgment_absorbed once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal judgment_absorbed and log eval_judgment_absorbed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.6 — O-JUDGE | O-JUDGE ending with judgment_absorbed. | Records judgment_absorbed as this operation’s terminal; emits eval_judgment_absorbed once. | One terminal judgment_absorbed and log eval_judgment_absorbed. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.6.3 — O-JUDGE judgment_refused_stale_head
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-JUDGE judgment_refused_stale_head rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-JUDGE ending with judgment_refused_stale_head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records judgment_refused_stale_head as this operation’s terminal; emits eval_judgment_refused_stale_head once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal judgment_refused_stale_head and log eval_judgment_refused_stale_head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.6 — O-JUDGE | O-JUDGE ending with judgment_refused_stale_head. | Records judgment_refused_stale_head as this operation’s terminal; emits eval_judgment_refused_stale_head once. | One terminal judgment_refused_stale_head and log eval_judgment_refused_stale_head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.6.4 — O-JUDGE judgment_refused_authority
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-JUDGE judgment_refused_authority rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-JUDGE ending with judgment_refused_authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records judgment_refused_authority as this operation’s terminal; emits eval_judgment_refused_authority once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal judgment_refused_authority and log eval_judgment_refused_authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.6 — O-JUDGE | O-JUDGE ending with judgment_refused_authority. | Records judgment_refused_authority as this operation’s terminal; emits eval_judgment_refused_authority once. | One terminal judgment_refused_authority and log eval_judgment_refused_authority. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.6.5 — O-JUDGE judgment_refused_mode_mismatch
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-JUDGE judgment_refused_mode_mismatch rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-JUDGE ending with judgment_refused_mode_mismatch. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records judgment_refused_mode_mismatch as this operation’s terminal; emits eval_judgment_refused_mode_mismatch once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal judgment_refused_mode_mismatch and log eval_judgment_refused_mode_mismatch. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.6 — O-JUDGE | O-JUDGE ending with judgment_refused_mode_mismatch. | Records judgment_refused_mode_mismatch as this operation’s terminal; emits eval_judgment_refused_mode_mismatch once. | One terminal judgment_refused_mode_mismatch and log eval_judgment_refused_mode_mismatch. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.6.6 — O-JUDGE judgment_refused_output_invalid
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-JUDGE judgment_refused_output_invalid rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-JUDGE ending with judgment_refused_output_invalid. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records judgment_refused_output_invalid as this operation’s terminal; emits eval_judgment_refused_output_invalid once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal judgment_refused_output_invalid and log eval_judgment_refused_output_invalid. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.6 — O-JUDGE | O-JUDGE ending with judgment_refused_output_invalid. | Records judgment_refused_output_invalid as this operation’s terminal; emits eval_judgment_refused_output_invalid once. | One terminal judgment_refused_output_invalid and log eval_judgment_refused_output_invalid. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.6.7 — O-JUDGE judgment_claim_lost
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-JUDGE judgment_claim_lost rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-JUDGE ending with judgment_claim_lost. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records judgment_claim_lost as this operation’s terminal; emits eval_judgment_claim_lost once. The losing concurrent claim consumes nothing. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal judgment_claim_lost and log eval_judgment_claim_lost. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.6 — O-JUDGE | O-JUDGE ending with judgment_claim_lost. | Records judgment_claim_lost as this operation’s terminal; emits eval_judgment_claim_lost once. The losing concurrent claim consumes nothing. | One terminal judgment_claim_lost and log eval_judgment_claim_lost. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.6.8 — O-JUDGE judgment_authorization_failed
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-JUDGE judgment_authorization_failed rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-JUDGE ending with judgment_authorization_failed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records judgment_authorization_failed as this operation’s terminal; emits eval_judgment_authorization_failed once. Reasons are pre-receipt crash, failed/unverifiable receipt write, refusal before consumption after a claim, or head breach after a durable receipt; claim closure is the consequence, never the cause. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal judgment_authorization_failed and log eval_judgment_authorization_failed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.6 — O-JUDGE | O-JUDGE ending with judgment_authorization_failed. | Records judgment_authorization_failed as this operation’s terminal; emits eval_judgment_authorization_failed once. Reasons are pre-receipt crash, failed/unverifiable receipt write, refusal before consumption after a claim, or head breach after a durable receipt; claim closure is the consequence, never the cause. | One terminal judgment_authorization_failed and log eval_judgment_authorization_failed. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.7 — O-AGGREGATE
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-AGGREGATE operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — E10 and E16. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Owns one aggregate derivation against its expected prior head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — Exactly one of aggregate_committed, aggregate_absorbed, aggregate_refused_stale_head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Emit two terminals/logs under this operation identity or acknowledge before its terminal and log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Different content under one key or two successors of one head makes the run indeterminate; stale head returns aggregate_refused_stale_head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Missing judgments/measurements make incomplete; unverifiable, forked or contradictory inputs make indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.2.7.1 — O-AGGREGATE aggregate_committed: Records aggregate_committed as this operation’s terminal; emits eval_aggregate_committed once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.7.2 — O-AGGREGATE aggregate_absorbed: Records aggregate_absorbed as this operation’s terminal; emits eval_aggregate_absorbed once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.7.3 — O-AGGREGATE aggregate_refused_stale_head: Records aggregate_refused_stale_head as this operation’s terminal; emits eval_aggregate_refused_stale_head once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: One terminal and one operation-owned log must be durable before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.2 — CAS-2 aggregate-head compare-and-replace: Commits only if expected_previous_head remains current; identical key/content absorbs. A stale predecessor refuses, allowing a fresh aggregate from new state as a new operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result (E10): Binds the exact consumed sets and the run’s own suite-kind scoring rule; records actual measurements and coverage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result (E10): appends the E10 canonical record when its stated commit conditions hold; earlier records remain unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2 — Operation terminal catalog | E10 and E16. | Owns one aggregate derivation against its expected prior head. | Exactly one of aggregate_committed, aggregate_absorbed, aggregate_refused_stale_head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.2.7.1 — O-AGGREGATE aggregate_committed; C-GOLD.1.5.2.7.2 — O-AGGREGATE aggregate_absorbed; C-GOLD.1.5.2.7.3 — O-AGGREGATE aggregate_refused_stale_head

### C-GOLD.1.5.2.7.1 — O-AGGREGATE aggregate_committed
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-AGGREGATE aggregate_committed rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-AGGREGATE ending with aggregate_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records aggregate_committed as this operation’s terminal; emits eval_aggregate_committed once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal aggregate_committed and log eval_aggregate_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.7 — O-AGGREGATE | O-AGGREGATE ending with aggregate_committed. | Records aggregate_committed as this operation’s terminal; emits eval_aggregate_committed once. | One terminal aggregate_committed and log eval_aggregate_committed. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.7.2 — O-AGGREGATE aggregate_absorbed
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-AGGREGATE aggregate_absorbed rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-AGGREGATE ending with aggregate_absorbed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records aggregate_absorbed as this operation’s terminal; emits eval_aggregate_absorbed once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal aggregate_absorbed and log eval_aggregate_absorbed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.7 — O-AGGREGATE | O-AGGREGATE ending with aggregate_absorbed. | Records aggregate_absorbed as this operation’s terminal; emits eval_aggregate_absorbed once. | One terminal aggregate_absorbed and log eval_aggregate_absorbed. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.7.3 — O-AGGREGATE aggregate_refused_stale_head
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-AGGREGATE aggregate_refused_stale_head rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-AGGREGATE ending with aggregate_refused_stale_head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records aggregate_refused_stale_head as this operation’s terminal; emits eval_aggregate_refused_stale_head once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal aggregate_refused_stale_head and log eval_aggregate_refused_stale_head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.7 — O-AGGREGATE | O-AGGREGATE ending with aggregate_refused_stale_head. | Records aggregate_refused_stale_head as this operation’s terminal; emits eval_aggregate_refused_stale_head once. | One terminal aggregate_refused_stale_head and log eval_aggregate_refused_stale_head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.8 — O-RESULT
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-RESULT operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — one E11a / E11b / E12. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Derives one deterministic result at one scope ledger head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — Exactly one of result_committed, result_absorbed, result_contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Emit two terminals/logs under this operation identity or acknowledge before its terminal and log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Different state/content yields result_contradiction; preserve both, neither satisfies B16/B24, scope results remain indeterminate until lookup reconciliation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.2.8.1 — O-RESULT result_committed: Records result_committed as this operation’s terminal; emits eval_result_committed once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.8.2 — O-RESULT result_absorbed: Records result_absorbed as this operation’s terminal; emits eval_result_absorbed once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.8.3 — O-RESULT result_contradiction: Records result_contradiction as this operation’s terminal; emits eval_result_contradiction once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: One terminal and one operation-owned log must be durable before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.3 — DET-1 deterministic result identity: Pure derivation from that ledger state produces identical identity/content; repeated identical commitment absorbs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.12 — gold_evidence_result (E11a): For this requested record kind, appends the E11a canonical record when its stated commit conditions hold; earlier records remain unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.13 — held_out_evidence_result (E11b): For this requested record kind, appends the E11b canonical record when its stated commit conditions hold; earlier records remain unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.14 — b24_system_eligibility_result (E12): For this requested record kind, appends the E12 canonical record when its stated commit conditions hold; earlier records remain unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2 — Operation terminal catalog | one E11a / E11b / E12. | Derives one deterministic result at one scope ledger head. | Exactly one of result_committed, result_absorbed, result_contradiction. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.2.8.1 — O-RESULT result_committed; C-GOLD.1.5.2.8.2 — O-RESULT result_absorbed; C-GOLD.1.5.2.8.3 — O-RESULT result_contradiction

### C-GOLD.1.5.2.8.1 — O-RESULT result_committed
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-RESULT result_committed rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-RESULT ending with result_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records result_committed as this operation’s terminal; emits eval_result_committed once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal result_committed and log eval_result_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.8 — O-RESULT | O-RESULT ending with result_committed. | Records result_committed as this operation’s terminal; emits eval_result_committed once. | One terminal result_committed and log eval_result_committed. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.8.2 — O-RESULT result_absorbed
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-RESULT result_absorbed rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-RESULT ending with result_absorbed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records result_absorbed as this operation’s terminal; emits eval_result_absorbed once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal result_absorbed and log eval_result_absorbed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.8 — O-RESULT | O-RESULT ending with result_absorbed. | Records result_absorbed as this operation’s terminal; emits eval_result_absorbed once. | One terminal result_absorbed and log eval_result_absorbed. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.8.3 — O-RESULT result_contradiction
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-RESULT result_contradiction rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-RESULT ending with result_contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records result_contradiction as this operation’s terminal; emits eval_result_contradiction once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal result_contradiction and log eval_result_contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.8 — O-RESULT | O-RESULT ending with result_contradiction. | Records result_contradiction as this operation’s terminal; emits eval_result_contradiction once. | One terminal result_contradiction and log eval_result_contradiction. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.9 — O-EVREF
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-EVREF operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — E13. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Issues only a narrow valid B16 evidence reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — Exactly one of issued, refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Emit two terminals/logs under this operation identity or acknowledge before its terminal and log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Non-current evidence is unusable for a new B16 check; wrong-kind or invalid pointers cannot pass. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.2.9.1 — O-EVREF issued: Records issued as this operation’s terminal; emits eval_evidence_ref_issued once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.9.2 — O-EVREF refused: Records refused as this operation’s terminal; emits eval_evidence_ref_refused once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: One terminal and one operation-owned log must be durable before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13): Points only to E11a for input 3 or E11b for input 4. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13): appends the E13 canonical record when its stated commit conditions hold; earlier records remain unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2 — Operation terminal catalog | E13. | Issues only a narrow valid B16 evidence reference. | Exactly one of issued, refused. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.2.9.1 — O-EVREF issued; C-GOLD.1.5.2.9.2 — O-EVREF refused

### C-GOLD.1.5.2.9.1 — O-EVREF issued
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-EVREF issued rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-EVREF ending with issued. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records issued as this operation’s terminal; emits eval_evidence_ref_issued once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal issued and log eval_evidence_ref_issued. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.9 — O-EVREF | O-EVREF ending with issued. | Records issued as this operation’s terminal; emits eval_evidence_ref_issued once. | One terminal issued and log eval_evidence_ref_issued. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.9.2 — O-EVREF refused
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-EVREF refused rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-EVREF ending with refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records refused as this operation’s terminal; emits eval_evidence_ref_refused once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal refused and log eval_evidence_ref_refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.9 — O-EVREF | O-EVREF ending with refused. | Records refused as this operation’s terminal; emits eval_evidence_ref_refused once. | One terminal refused and log eval_evidence_ref_refused. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.10 — O-INVALIDITY
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-INVALIDITY operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — E14 and E16. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records a policy-authorized objective invalidity exclusion. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — Exactly one of committed, refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Emit two terminals/logs under this operation identity or acknowledge before its terminal and log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without an accepted objective rule exclusion is refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.2.10.1 — O-INVALIDITY committed: Records committed as this operation’s terminal; emits eval_invalidity_committed once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.10.2 — O-INVALIDITY refused: Records refused as this operation’s terminal; emits eval_invalidity_refused once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: One terminal and one operation-owned log must be durable before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.16 — evaluation_invalidity_record (E14): Excludes only under that accepted rule; no such rule currently exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.16 — evaluation_invalidity_record (E14): appends the E14 canonical record when its stated commit conditions hold; earlier records remain unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2 — Operation terminal catalog | E14 and E16. | Records a policy-authorized objective invalidity exclusion. | Exactly one of committed, refused. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.2.10.1 — O-INVALIDITY committed; C-GOLD.1.5.2.10.2 — O-INVALIDITY refused

### C-GOLD.1.5.2.10.1 — O-INVALIDITY committed
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-INVALIDITY committed rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-INVALIDITY ending with committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records committed as this operation’s terminal; emits eval_invalidity_committed once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal committed and log eval_invalidity_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.10 — O-INVALIDITY | O-INVALIDITY ending with committed. | Records committed as this operation’s terminal; emits eval_invalidity_committed once. | One terminal committed and log eval_invalidity_committed. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.10.2 — O-INVALIDITY refused
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-INVALIDITY refused rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-INVALIDITY ending with refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records refused as this operation’s terminal; emits eval_invalidity_refused once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal refused and log eval_invalidity_refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.10 — O-INVALIDITY | O-INVALIDITY ending with refused. | Records refused as this operation’s terminal; emits eval_invalidity_refused once. | One terminal refused and log eval_invalidity_refused. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.11 — O-CONFLICT
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-CONFLICT operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — E15 and E16. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records a policy-authorized completed-run conflict resolution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — Exactly one of committed, refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Emit two terminals/logs under this operation identity or acknowledge before its terminal and log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without accepted policy, failed or indeterminate heads retain their blocking effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.2.11.1 — O-CONFLICT committed: Records committed as this operation’s terminal; emits eval_conflict_resolution_committed once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.11.2 — O-CONFLICT refused: Records refused as this operation’s terminal; emits eval_conflict_resolution_refused once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: One terminal and one operation-owned log must be durable before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.17 — evaluation_conflict_resolution (E15): Resolves only within the accepted policy’s scope, binding every affected run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.17 — evaluation_conflict_resolution (E15): appends the E15 canonical record when its stated commit conditions hold; earlier records remain unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2 — Operation terminal catalog | E15 and E16. | Records a policy-authorized completed-run conflict resolution. | Exactly one of committed, refused. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.2.11.1 — O-CONFLICT committed; C-GOLD.1.5.2.11.2 — O-CONFLICT refused

### C-GOLD.1.5.2.11.1 — O-CONFLICT committed
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-CONFLICT committed rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-CONFLICT ending with committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records committed as this operation’s terminal; emits eval_conflict_resolution_committed once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal committed and log eval_conflict_resolution_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.11 — O-CONFLICT | O-CONFLICT ending with committed. | Records committed as this operation’s terminal; emits eval_conflict_resolution_committed once. | One terminal committed and log eval_conflict_resolution_committed. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.11.2 — O-CONFLICT refused
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-CONFLICT refused rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-CONFLICT ending with refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records refused as this operation’s terminal; emits eval_conflict_resolution_refused once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal refused and log eval_conflict_resolution_refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.11 — O-CONFLICT | O-CONFLICT ending with refused. | Records refused as this operation’s terminal; emits eval_conflict_resolution_refused once. | One terminal refused and log eval_conflict_resolution_refused. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.12 — O-RECOVERY
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-RECOVERY operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — missing items only. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Uses lookup-first recovery; repeated resolved work is a no-op. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — Exactly one of recovery_applied, recovery_noop. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Emit two terminals/logs under this operation identity or acknowledge before its terminal and log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unreadable records give indeterminate downstream; repeated recovery is a no-op. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.2.12.1 — O-RECOVERY recovery_applied: Records recovery_applied as this operation’s terminal; emits eval_recovery_applied once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.12.2 — O-RECOVERY recovery_noop: Records recovery_noop as this operation’s terminal; emits eval_recovery_noop once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: One terminal and one operation-owned log must be durable before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.12 — Run and concurrency recovery: Finds committed effects, fills missing records/logs only from evidence, and keeps unknown effects blocked. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2 — Operation terminal catalog | missing items only. | Uses lookup-first recovery; repeated resolved work is a no-op. | Exactly one of recovery_applied, recovery_noop. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.12.23 — CR-23 — Duplicate recovery | missing items only. | Recovery follows this rule: Uses lookup-first recovery; repeated resolved work is a no-op. | Exactly one of recovery_applied, recovery_noop. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.2.12.1 — O-RECOVERY recovery_applied; C-GOLD.1.5.2.12.2 — O-RECOVERY recovery_noop

### C-GOLD.1.5.2.12.1 — O-RECOVERY recovery_applied
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-RECOVERY recovery_applied rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-RECOVERY ending with recovery_applied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records recovery_applied as this operation’s terminal; emits eval_recovery_applied once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal recovery_applied and log eval_recovery_applied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.12 — O-RECOVERY | O-RECOVERY ending with recovery_applied. | Records recovery_applied as this operation’s terminal; emits eval_recovery_applied once. | One terminal recovery_applied and log eval_recovery_applied. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.12.2 — O-RECOVERY recovery_noop
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-RECOVERY recovery_noop rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-RECOVERY ending with recovery_noop. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records recovery_noop as this operation’s terminal; emits eval_recovery_noop once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal recovery_noop and log eval_recovery_noop. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.12 — O-RECOVERY | O-RECOVERY ending with recovery_noop. | Records recovery_noop as this operation’s terminal; emits eval_recovery_noop once. | One terminal recovery_noop and log eval_recovery_noop. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.13 — O-APPEND
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-APPEND operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — exactly one requested record and its E16. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Atomically commits the requested scope-relevant canonical record with its ledger entry under both head comparison and the record’s domain preconditions. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — Exactly one of appended, absorbed, lost_race_technical, refused_domain_precondition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Emit two terminals/logs under this operation identity or acknowledge before its terminal and log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A loser ends lost_race_technical with one log; only B9 may admit a new O-APPEND with new ID and unchanged canonical record; no admission means no commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No record commit means no requester terminal; run cannot close and evidence remains incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.2.13.1 — O-APPEND appended: Records appended as this operation’s terminal; emits eval_append_appended once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.13.2 — O-APPEND absorbed: Records absorbed as this operation’s terminal; emits eval_append_absorbed once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.13.3 — O-APPEND lost_race_technical: Records lost_race_technical as this operation’s terminal; emits eval_append_lost_race_technical once. Commits nothing; only a B9-admitted new O-APPEND may retry. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.2.13.4 — O-APPEND refused_domain_precondition: Records refused_domain_precondition as this operation’s terminal; emits eval_append_refused_domain_precondition once. Non-retryable domain refusal; no machine retry. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: One terminal and one operation-owned log must be durable before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append: Commits the record and E16 together only if the current head is exactly {n,d} and domain preconditions hold; the new entry uses n+1 and previous_entry_digest=d. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.13 — Requesting operation after append exhaustion: Keeps the requesting domain operation honestly open/pending with no terminal because its record has not committed; B9 records the stopping gate and preserved state. Only a new B9 episode with consumed real-change and unchanged inputs may continue. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.18 — evaluation_scope_ledger_entry (E16): Commits one E16 atomically with the requested relevant record; the ledger advances only on the successful comparison. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2 — Operation terminal catalog | exactly one requested record and its E16. | Atomically commits the requested scope-relevant canonical record with its ledger entry under both head comparison and the record’s domain preconditions. | Exactly one of appended, absorbed, lost_race_technical, refused_domain_precondition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.2.13.1 — O-APPEND appended; C-GOLD.1.5.2.13.2 — O-APPEND absorbed; C-GOLD.1.5.2.13.3 — O-APPEND lost_race_technical; C-GOLD.1.5.2.13.4 — O-APPEND refused_domain_precondition

### C-GOLD.1.5.2.13.1 — O-APPEND appended
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-APPEND appended rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-APPEND ending with appended. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records appended as this operation’s terminal; emits eval_append_appended once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal appended and log eval_append_appended. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.13 — O-APPEND | O-APPEND ending with appended. | Records appended as this operation’s terminal; emits eval_append_appended once. | One terminal appended and log eval_append_appended. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.13.2 — O-APPEND absorbed
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-APPEND absorbed rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-APPEND ending with absorbed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records absorbed as this operation’s terminal; emits eval_append_absorbed once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal absorbed and log eval_append_absorbed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.13 — O-APPEND | O-APPEND ending with absorbed. | Records absorbed as this operation’s terminal; emits eval_append_absorbed once. | One terminal absorbed and log eval_append_absorbed. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.13.3 — O-APPEND lost_race_technical
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-APPEND lost_race_technical rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-APPEND ending with lost_race_technical. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records lost_race_technical as this operation’s terminal; emits eval_append_lost_race_technical once. Commits nothing; only a B9-admitted new O-APPEND may retry. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal lost_race_technical and log eval_append_lost_race_technical. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.13 — O-APPEND | O-APPEND ending with lost_race_technical. | Records lost_race_technical as this operation’s terminal; emits eval_append_lost_race_technical once. Commits nothing; only a B9-admitted new O-APPEND may retry. | One terminal lost_race_technical and log eval_append_lost_race_technical. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.2.13.4 — O-APPEND refused_domain_precondition
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-APPEND refused_domain_precondition rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-APPEND ending with refused_domain_precondition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records refused_domain_precondition as this operation’s terminal; emits eval_append_refused_domain_precondition once. Non-retryable domain refusal; no machine retry. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One terminal refused_domain_precondition and log eval_append_refused_domain_precondition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second terminal or second log for this operation ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement is withheld until this terminal and its one log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: The terminal and matching log precede acknowledgement; recovery fills a missing log without duplicating it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.2.13 — O-APPEND | O-APPEND ending with refused_domain_precondition. | Records refused_domain_precondition as this operation’s terminal; emits eval_append_refused_domain_precondition once. Non-retryable domain refusal; no machine retry. | One terminal refused_domain_precondition and log eval_append_refused_domain_precondition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.3 — Run closing conditions
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The exact admission gate for E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Takes in: ACCEPTED — Every started attempt’s E7, planned-trial completions and B9 admitted/live state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Does: ACCEPTED — Allows E8 only after all started attempts have a terminal and no planned-trial attempt is live or admitted-unstarted. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Gives out: ACCEPTED — An honest run terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Must never: ACCEPTED — Close while an attempt is live/admitted-unstarted or start any attempt after E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unknown evidence, integrity failure or contradiction cannot yield run_completed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.3.1 — All started attempts terminal: Requires one E7 for every started attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.3.2 — No admitted-unstarted or live attempts: Requires no live attempt and no admitted-unstarted attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.3.3 — Completed run outcome: run_completed requires exactly one effectively completed attempt for every planned trial at close. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.3.4 — Deliberately incomplete run outcome: Records run_closed_incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.3.5 — Indeterminate run outcome: Records run_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.3.6 — No attempt after run terminal: Refuses every later attempt start. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.13 — Requesting operation after append exhaustion: An operation still pending after append exhaustion prevents the required closing record or completed attempt from being claimed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5 — Evaluation operations and trial execution | Every started attempt’s E7, planned-trial completions and B9 admitted/live state. | Allows E8 only after all started attempts have a terminal and no planned-trial attempt is live or admitted-unstarted. | An honest run terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.4 — Frozen terminal set | Every started attempt’s E7, planned-trial completions and B9 admitted/live state. | E8 first satisfies all closing conditions; its terminal set is then frozen. | An honest run terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.9.7 — EB-7 — Run terminal | Every started attempt’s E7, planned-trial completions and B9 admitted/live state. | Applies this defining record/rule contract: Allows E8 only after all started attempts have a terminal and no planned-trial attempt is live or admitted-unstarted. | An honest run terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.12.9 — CR-9 — All attempts terminal, none live, no E8 | Every started attempt’s E7, planned-trial completions and B9 admitted/live state. | Recovery follows this rule: Allows E8 only after all started attempts have a terminal and no planned-trial attempt is live or admitted-unstarted. | An honest run terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.5.2.3 — O-RUN | Every started attempt’s E7, planned-trial completions and B9 admitted/live state. | Allows E8 only after all started attempts have a terminal and no planned-trial attempt is live or admitted-unstarted. | An honest run terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.3.9 — evaluation_run_terminal (E8) | Every started attempt’s E7, planned-trial completions and B9 admitted/live state. | All started attempts have E7 and none are live or admitted-unstarted; the outcome reflects actual completion evidence. | An honest run terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.3.1 — All started attempts terminal; C-GOLD.1.5.3.2 — No admitted-unstarted or live attempts; C-GOLD.1.5.3.3 — Completed run outcome; C-GOLD.1.5.3.4 — Deliberately incomplete run outcome; C-GOLD.1.5.3.5 — Indeterminate run outcome; C-GOLD.1.5.3.6 — No attempt after run terminal

### C-GOLD.1.5.3.1 — All started attempts terminal
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The All started attempts terminal rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — Every E6 of the run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — Requires one E7 for every started attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — E8 admission condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Commit E8 with a started attempt missing E7. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Run remains open until every started attempt has E7. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Requires one E7 for every started attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.3 — Run closing conditions | Every E6 of the run. | Requires one E7 for every started attempt. | E8 admission condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.3.2 — No admitted-unstarted or live attempts
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The No admitted-unstarted or live attempts rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — B9 attempt state for every planned trial. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — Requires no live attempt and no admitted-unstarted attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — E8 admission condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Close the run while such an attempt exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Run cannot close while the condition is unmet. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Requires no live attempt and no admitted-unstarted attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.3 — Run closing conditions | B9 attempt state for every planned trial. | Requires no live attempt and no admitted-unstarted attempt. | E8 admission condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.3.3 — Completed run outcome
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Completed run outcome rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — The completion state of every planned trial. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — run_completed requires exactly one effectively completed attempt for every planned trial at close. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — run_completed when the complete condition holds. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Call an incomplete or unresolved trial plan run_completed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Incomplete coverage cannot yield run_completed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — run_completed requires exactly one effectively completed attempt for every planned trial at close. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.3 — Run closing conditions | The completion state of every planned trial. | run_completed requires exactly one effectively completed attempt for every planned trial at close. | run_completed when the complete condition holds. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.3.4 — Deliberately incomplete run outcome
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Deliberately incomplete run outcome rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — A run deliberately closed short of full trial completion. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — Records run_closed_incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — run_closed_incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Represent this outcome as full coverage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The incomplete run blocks passing evidence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Records run_closed_incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.3 — Run closing conditions | A run deliberately closed short of full trial completion. | Records run_closed_incomplete. | run_closed_incomplete. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.3.5 — Indeterminate run outcome
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Indeterminate run outcome rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — Unresolved attempt without conclusive resolution, integrity failure or contradiction at close. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — Records run_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — run_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Select a guessed success from unknown or contradictory evidence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Only indeterminate closure is valid for this condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Records run_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.3 — Run closing conditions | Unresolved attempt without conclusive resolution, integrity failure or contradiction at close. | Records run_indeterminate. | run_indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.3.6 — No attempt after run terminal
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The No attempt after run terminal rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — An existing E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — Refuses every later attempt start. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — No post-E8 execution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Start a new attempt after E8, including after later absence proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Post-E8 attempt start is refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Refuses every later attempt start. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.3 — Run closing conditions | An existing E8. | Refuses every later attempt start. | No post-E8 execution. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.11.1 — resolved_output_found resolution | An existing E8. | No new attempt may start after E8 even when later lookup proves absence. | No post-E8 execution. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.11.2 — resolved_absence_proven resolution | An existing E8. | No new attempt may start after E8 even when later lookup proves absence. | No post-E8 execution. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.11.3 — still_undetermined resolution | An existing E8. | No new attempt may start after E8 even when later lookup proves absence. | No post-E8 execution. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.3.6 — trial_attempt_start (E6) | An existing E8. | No attempt may start after E8. | No post-E8 execution. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.4 — Frozen terminal set
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — Every E6/E7 across every B9 episode, frozen at E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3] [NHD-B16EEB]
- Takes in: ACCEPTED — The complete set of started attempts and their terminal records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3] [NHD-B16EEB]
- Does: ACCEPTED — Freezes and digests the set; E10 computes from precisely this set plus later E7r records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3] [NHD-B16EEB]
- Gives out: ACCEPTED — One immutable terminal-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite E7 or E8 or substitute another set during aggregation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the digested terminal/resolution/judgment sets changed, the aggregate is stale; terminal records remain immutable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.3 — Run closing conditions: E8 first satisfies all closing conditions; its terminal set is then frozen. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5 — Evaluation operations and trial execution | The complete set of started attempts and their terminal records. | Freezes and digests the set; E10 computes from precisely this set plus later E7r records. | One immutable terminal-set digest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.2.3 — O-RUN | The complete set of started attempts and their terminal records. | Freezes and digests the set; E10 computes from precisely this set plus later E7r records. | One immutable terminal-set digest. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.5 — One output per planned trial
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — One canonical output key shared by every attempt of the trial. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5]
- Takes in: ACCEPTED — planned_trial_key and all attempts for that planned measurement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5]
- Does: ACCEPTED — Derives planned_trial_output_key deterministically; uses it as the reading’s idempotency_key; at most one output commits. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5]
- Gives out: ACCEPTED — One committed output ever. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5]
- Must never: ACCEPTED — Retry or replace a completed output, retry a judged failure to obtain a pass, or expose uncommitted output. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5]
- Fails closed by: ACCEPTED — Completed-output retries absorb as B9 terminal_success; unknown output existence blocks retry. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.5.1 — planned_trial_output_key: Deterministic from planned_trial_key; shared by every attempt; becomes the reading’s idempotency_key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5]
- Fed by: ACCEPTED — C-GOLD.1.5.5.2 — Output-before-visibility gate: Shows no output to operator or judge until E7 attempt_completed or E7r resolved_output_found commits. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5]
- Fed by: ACCEPTED — C-GOLD.1.5.5.3 — Judged failure is a measurement: Keeps that output final; B9 terminal_success absorbs retries. Substantive careful-retry is not an evaluation-output path; internal retries belong to the configuration under test. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5]
- Gated by: ACCEPTED — C-GOLD.1.5.5.1 — planned_trial_output_key: Every attempt shares this one deterministic output key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5]
- Gated by: ACCEPTED — C-GOLD.1.5.5.2 — Output-before-visibility gate: No output is visible before its completed E7 or found-output E7r commits. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5 — Evaluation operations and trial execution | planned_trial_key and all attempts for that planned measurement. | Derives planned_trial_output_key deterministically; uses it as the reading’s idempotency_key; at most one output commits. | One committed output ever. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.12.3 — CR-3 — E6, output found by key, no E7 | planned_trial_key and all attempts for that planned measurement. | Recovery follows this rule: Derives planned_trial_output_key deterministically; uses it as the reading’s idempotency_key; at most one output commits. | One committed output ever. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.2.4 — O-ATTEMPT | planned_trial_key and all attempts for that planned measurement. | Derives planned_trial_output_key deterministically; uses it as the reading’s idempotency_key; at most one output commits. | One committed output ever. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.5.1 — planned_trial_output_key; C-GOLD.1.5.5.2 — Output-before-visibility gate; C-GOLD.1.5.5.3 — Judged failure is a measurement

### C-GOLD.1.5.5.1 — planned_trial_output_key
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The planned_trial_output_key member of One output per planned trial. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Takes in: ACCEPTED — Deterministic from planned_trial_key; shared by every attempt; becomes the reading’s idempotency_key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Does: ACCEPTED — Deterministic from planned_trial_key; shared by every attempt; becomes the reading’s idempotency_key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Gives out: ACCEPTED — The recorded planned_trial_output_key member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Must never: ACCEPTED — Give retries a different canonical output identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A completed output makes later attempts absorb; output existence that is unknown prevents retries. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Every attempt of one planned trial shares this deterministic key; it becomes the reading idempotency_key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.5 — One output per planned trial | Deterministic from planned_trial_key; shared by every attempt; becomes the reading’s idempotency_key. | Deterministic from planned_trial_key; shared by every attempt; becomes the reading’s idempotency_key. | The recorded planned_trial_output_key member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.5 — One output per planned trial | Deterministic from planned_trial_key; shared by every attempt; becomes the reading’s idempotency_key. | Every attempt shares this one deterministic output key. | The recorded planned_trial_output_key member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.5.2 — Output-before-visibility gate
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Output-before-visibility gate rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Takes in: ACCEPTED — A produced output and its E7/E7r record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Does: ACCEPTED — Shows no output to operator or judge until E7 attempt_completed or E7r resolved_output_found commits. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Gives out: ACCEPTED — Only durably completed outputs become visible. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Must never: ACCEPTED — Display an output before its completion record commits. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Withholds visibility until durable completion proof exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — E7 attempt_completed or E7r resolved_output_found must commit before operator or judge visibility. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.5 — One output per planned trial | A produced output and its E7/E7r record. | Shows no output to operator or judge until E7 attempt_completed or E7r resolved_output_found commits. | Only durably completed outputs become visible. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.5 — One output per planned trial | A produced output and its E7/E7r record. | No output is visible before its completed E7 or found-output E7r commits. | Only durably completed outputs become visible. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.5.3 — Judged failure is a measurement
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Judged failure is a measurement rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Takes in: ACCEPTED — A completed output judged fail. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Does: ACCEPTED — Keeps that output final; B9 terminal_success absorbs retries. Substantive careful-retry is not an evaluation-output path; internal retries belong to the configuration under test. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Gives out: ACCEPTED — The actual failed measurement is retained. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Must never: ACCEPTED — Re-attempt a judged fail to change the measurement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Retry of the completed output is absorbed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The output is already completed; its judged fail is the measurement, not an uncompleted technical attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.5 — One output per planned trial | A completed output judged fail. | Keeps that output final; B9 terminal_success absorbs retries. Substantive careful-retry is not an evaluation-output path; internal retries belong to the configuration under test. | The actual failed measurement is retained. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.6 — B9-governed technical re-attempts
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — Technical re-execution of the same planned trial under accepted B9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Takes in: ACCEPTED — Durable attempt outcome, actual execution context and committed B9 R1 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Does: ACCEPTED — Routes each outcome by its accepted retry class; every ordinal ≥ 2 needs B9 admission under unchanged canonical identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Gives out: ACCEPTED — An admitted attempt or no re-attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass B9, invent a new planned trial, retry unknown/completed output or hide retry inside the bridge. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No B9 authorization means no re-attempt; exhaustion leaves the trial uncovered; resource failures remain CONSEQUENTIAL for B24. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.6.1 — attempt_completed B9 routing: Routes as terminal_success. Absorbs retries; the completed output remains final. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.6.2 — attempt_failed B9 routing: Routes as technical_retryable. May retry only after committed B9 R1 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.6.3 — attempt_interrupted_abandoned B9 routing: Routes as technical_retryable. May retry only after committed B9 R1 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.6.4 — attempt_unresolved B9 routing: Routes as indeterminate. Never retries until recovery resolves existence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.6.5 — privacy refusal B9 routing: Routes as privacy_refused. Cannot retry around the refusal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.6.6 — live hold B9 routing: Routes as dependency_blocked_held. The hold blocks execution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.6.7 — Committed B9 R1 admission: Requires committed B9 R1 admission under accepted identity, budget, gaps, deadline, one-live-attempt and real-change rules. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.6.8 — Original execution ordinal: Treats ordinal 1 as original execution by reference, with no B9 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.6.9 — Technical episode exhaustion: Leaves the trial uncovered; the run remains open or closes incomplete. Continuation is only through B9 real-change admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.6.10 — Accepted B9 episode values: Allows 3 total technical attempts per episode; minimum gaps 10 s / 30 s for live chat or 1 min / 3 min for background/nightly; elapsed deadlines 7 min / 15 min respectively. Keeps permanent attempt_number and separate per-episode ordinal; original execution is ordinal 1 by reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.7 — Actual execution-context classification: Missing/unreadable actual context admits no retry; non-live-chat evaluation uses background/nightly. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.6] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5 — Evaluation operations and trial execution | Durable attempt outcome, actual execution context and committed B9 R1 admission. | Routes each outcome by its accepted retry class; every ordinal ≥ 2 needs B9 admission under unchanged canonical identity. | An admitted attempt or no re-attempt. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.6.1 — attempt_completed B9 routing; C-GOLD.1.5.6.2 — attempt_failed B9 routing; C-GOLD.1.5.6.3 — attempt_interrupted_abandoned B9 routing; C-GOLD.1.5.6.4 — attempt_unresolved B9 routing; C-GOLD.1.5.6.5 — privacy refusal B9 routing; C-GOLD.1.5.6.6 — live hold B9 routing; C-GOLD.1.5.6.7 — Committed B9 R1 admission; C-GOLD.1.5.6.8 — Original execution ordinal; C-GOLD.1.5.6.9 — Technical episode exhaustion; C-GOLD.1.5.6.10 — Accepted B9 episode values

### C-GOLD.1.5.6.1 — attempt_completed B9 routing
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The attempt_completed B9 routing rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Takes in: ACCEPTED — The durable attempt_completed outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Does: ACCEPTED — Routes as terminal_success. Absorbs retries; the completed output remains final. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Gives out: ACCEPTED — terminal_success. Absorbs retries; the completed output remains final. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass the named B9 class. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Absorbs retries; the completed output remains final. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Routes as terminal_success. Absorbs retries; the completed output remains final. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.6 — B9-governed technical re-attempts | The durable attempt_completed outcome. | Routes as terminal_success. Absorbs retries; the completed output remains final. | terminal_success. Absorbs retries; the completed output remains final. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.6.2 — attempt_failed B9 routing
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The attempt_failed B9 routing rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Takes in: ACCEPTED — The durable attempt_failed outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Does: ACCEPTED — Routes as technical_retryable. May retry only after committed B9 R1 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Gives out: ACCEPTED — technical_retryable. May retry only after committed B9 R1 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass the named B9 class. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — May retry only after committed B9 R1 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.6.7 — Committed B9 R1 admission: Technical classification alone does not admit execution; committed B9 R1 admission is required. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.6 — B9-governed technical re-attempts | The durable attempt_failed outcome. | Routes as technical_retryable. May retry only after committed B9 R1 admission. | technical_retryable. May retry only after committed B9 R1 admission. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.6.3 — attempt_interrupted_abandoned B9 routing
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The attempt_interrupted_abandoned B9 routing rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Takes in: ACCEPTED — The durable attempt_interrupted_abandoned outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Does: ACCEPTED — Routes as technical_retryable. May retry only after committed B9 R1 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Gives out: ACCEPTED — technical_retryable. May retry only after committed B9 R1 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass the named B9 class. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — May retry only after committed B9 R1 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.6.7 — Committed B9 R1 admission: Technical classification alone does not admit execution; committed B9 R1 admission is required. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.6 — B9-governed technical re-attempts | The durable attempt_interrupted_abandoned outcome. | Routes as technical_retryable. May retry only after committed B9 R1 admission. | technical_retryable. May retry only after committed B9 R1 admission. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.6.4 — attempt_unresolved B9 routing
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The attempt_unresolved B9 routing rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Takes in: ACCEPTED — The durable attempt_unresolved outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Does: ACCEPTED — Routes as indeterminate. Never retries until recovery resolves existence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Gives out: ACCEPTED — indeterminate. Never retries until recovery resolves existence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass the named B9 class. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Never retries until recovery resolves existence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.11 — Unresolved-attempt resolution semantics: Existence must be resolved by lookup before retry can be considered. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.6 — B9-governed technical re-attempts | The durable attempt_unresolved outcome. | Routes as indeterminate. Never retries until recovery resolves existence. | indeterminate. Never retries until recovery resolves existence. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.6.5 — privacy refusal B9 routing
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The privacy refusal B9 routing rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Takes in: ACCEPTED — The durable privacy refusal outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Does: ACCEPTED — Routes as privacy_refused. Cannot retry around the refusal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Gives out: ACCEPTED — privacy_refused. Cannot retry around the refusal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass the named B9 class. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Cannot retry around the refusal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Routes as privacy_refused. Cannot retry around the refusal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.6 — B9-governed technical re-attempts | The durable privacy refusal outcome. | Routes as privacy_refused. Cannot retry around the refusal. | privacy_refused. Cannot retry around the refusal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.6.6 — live hold B9 routing
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The live hold B9 routing rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Takes in: ACCEPTED — The durable live hold outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Does: ACCEPTED — Routes as dependency_blocked_held. The hold blocks execution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Gives out: ACCEPTED — dependency_blocked_held. The hold blocks execution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass the named B9 class. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The hold blocks execution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Routes as dependency_blocked_held. The hold blocks execution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.6 — B9-governed technical re-attempts | The durable live hold outcome. | Routes as dependency_blocked_held. The hold blocks execution. | dependency_blocked_held. The hold blocks execution. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.6.7 — Committed B9 R1 admission
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Committed B9 R1 admission rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Takes in: ACCEPTED — An attempt of ordinal ≥ 2. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Does: ACCEPTED — Requires committed B9 R1 admission under accepted identity, budget, gaps, deadline, one-live-attempt and real-change rules. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One authorized later attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Must never: ACCEPTED — Start a later attempt without that admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No admission → no re-attempt; unadmitted E6 is the hidden-retry violation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.6.10 — Accepted B9 episode values: The accepted B9 context-specific budget, gaps, deadline and real-change rules bind admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.6 — B9-governed technical re-attempts | An attempt of ordinal ≥ 2. | Requires committed B9 R1 admission under accepted identity, budget, gaps, deadline, one-live-attempt and real-change rules. | One authorized later attempt. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.12.4 — CR-4 — E6, output provably absent | An attempt of ordinal ≥ 2. | Recovery follows this rule: Requires committed B9 R1 admission under accepted identity, budget, gaps, deadline, one-live-attempt and real-change rules. | One authorized later attempt. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.12.6 — CR-6 — B9 admission committed, no E6 | An attempt of ordinal ≥ 2. | Recovery follows this rule: Requires committed B9 R1 admission under accepted identity, budget, gaps, deadline, one-live-attempt and real-change rules. | One authorized later attempt. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.13 — Requesting operation after append exhaustion | An attempt of ordinal ≥ 2. | Continuation requires a new B9 episode, consumed real-change and unchanged canonical inputs. | One authorized later attempt. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.5.2.4 — O-ATTEMPT | An attempt of ordinal ≥ 2. | For ordinal ≥ 2 only: Requires committed B9 R1 admission under accepted identity, budget, gaps, deadline, one-live-attempt and real-change rules. | One authorized later attempt. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.5.9.4 — EB-4 — Attempt start | An attempt of ordinal ≥ 2. | Ordinal ≥ 2 requires committed B9 R1 admission. | One authorized later attempt. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.3.6 — trial_attempt_start (E6) | An attempt of ordinal ≥ 2. | Every later attempt requires committed B9 R1 admission. | One authorized later attempt. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.5.6.2 — attempt_failed B9 routing | An attempt of ordinal ≥ 2. | Technical classification alone does not admit execution; committed B9 R1 admission is required. | One authorized later attempt. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB] |
| 9 · ACCEPTED | C-GOLD.1.5.6.3 — attempt_interrupted_abandoned B9 routing | An attempt of ordinal ≥ 2. | Technical classification alone does not admit execution; committed B9 R1 admission is required. | One authorized later attempt. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.6.8 — Original execution ordinal
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Original execution ordinal rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Takes in: ACCEPTED — Ordinal 1 of the planned trial. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Does: ACCEPTED — Treats ordinal 1 as original execution by reference, with no B9 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Gives out: ACCEPTED — The original attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Must never: ACCEPTED — Require a later-attempt admission as if ordinal 1 were a re-attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Ordinal 1 is the original execution by reference, not a later B9-admitted attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.6 — B9-governed technical re-attempts | Ordinal 1 of the planned trial. | Treats ordinal 1 as original execution by reference, with no B9 admission. | The original attempt. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.12.2 — CR-2 — E5, no attempts | Ordinal 1 of the planned trial. | Recovery follows this rule: Treats ordinal 1 as original execution by reference, with no B9 admission. | The original attempt. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.6.9 — Technical episode exhaustion
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Technical episode exhaustion rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — An exhausted B9 trial episode. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — Leaves the trial uncovered; the run remains open or closes incomplete. Continuation is only through B9 real-change admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — No false trial coverage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Treat exhaustion as success or continue without B9 authorization. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The uncovered trial and incomplete/open run block pass. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Only consumed B9 real-change admission permits continuation after the episode is exhausted. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.6 — B9-governed technical re-attempts | An exhausted B9 trial episode. | Leaves the trial uncovered; the run remains open or closes incomplete. Continuation is only through B9 real-change admission. | No false trial coverage. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.12.7 — CR-7 — B9 episode exhausted | An exhausted B9 trial episode. | Recovery follows this rule: Leaves the trial uncovered; the run remains open or closes incomplete. Continuation is only through B9 real-change admission. | No false trial coverage. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.6.10 — Accepted B9 episode values
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Accepted B9 episode values rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Takes in: ACCEPTED — The B9 context class and episode state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Does: ACCEPTED — Allows 3 total technical attempts per episode; minimum gaps 10 s / 30 s for live chat or 1 min / 3 min for background/nightly; elapsed deadlines 7 min / 15 min respectively. Keeps permanent attempt_number and separate per-episode ordinal; original execution is ordinal 1 by reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Gives out: ACCEPTED — Context-specific B9 admission limits. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Must never: ACCEPTED — Treat trial count as retry count or reset permanent attempt numbering. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Continuation after exhaustion needs a consumed real-change record and seam-confirmed unchanged inputs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.6.10.1 — Total attempts: 3 total technical attempts per episode. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.6.10.2 — Live-chat first gap: Minimum 10 seconds before the first technical re-attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.6.10.3 — Live-chat second gap: Minimum 30 seconds before the next technical re-attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.6.10.4 — Background first gap: Minimum 1 minute before the first technical re-attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.6.10.5 — Background second gap: Minimum 3 minutes before the next technical re-attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.6.10.6 — Live-chat elapsed deadline: 7 minutes. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.6.10.7 — Background elapsed deadline: 15 minutes. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.6.10.8 — attempt_number: Permanent attempt number, separate from per-episode ordinal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.6.10.9 — Per-episode ordinal: Ordinal within the current episode; original execution is ordinal 1 by reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.6.10.10 — Real-change continuation: A consumed real-change record with seam-confirmed unchanged canonical inputs is required. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Gated by: ACCEPTED — B9 admission must obey its context-specific budget, gaps, deadline and unchanged-input continuation rules. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.6 — B9-governed technical re-attempts | The B9 context class and episode state. | Allows 3 total technical attempts per episode; minimum gaps 10 s / 30 s for live chat or 1 min / 3 min for background/nightly; elapsed deadlines 7 min / 15 min respectively. Keeps permanent attempt_number and separate per-episode ordinal; original execution is ordinal 1 by reference. | Context-specific B9 admission limits. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.6.7 — Committed B9 R1 admission | The B9 context class and episode state. | The accepted B9 context-specific budget, gaps, deadline and real-change rules bind admission. | Context-specific B9 admission limits. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.6.10.1 — Total attempts; C-GOLD.1.5.6.10.2 — Live-chat first gap; C-GOLD.1.5.6.10.3 — Live-chat second gap; C-GOLD.1.5.6.10.4 — Background first gap; C-GOLD.1.5.6.10.5 — Background second gap; C-GOLD.1.5.6.10.6 — Live-chat elapsed deadline; C-GOLD.1.5.6.10.7 — Background elapsed deadline; C-GOLD.1.5.6.10.8 — attempt_number; C-GOLD.1.5.6.10.9 — Per-episode ordinal; C-GOLD.1.5.6.10.10 — Real-change continuation

### C-GOLD.1.5.6.10.1 — Total attempts
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Total attempts rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Takes in: ACCEPTED — A B9 admission using the corresponding value. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Does: ACCEPTED — 3 total technical attempts per episode. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated B9 admission constraint. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Must never: ACCEPTED — Replace this accepted value with an invented retry setting. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without B9 admission under the applicable accepted limits, no re-attempt starts. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — 3 total technical attempts per episode. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.6.10 — Accepted B9 episode values | A B9 admission using the corresponding value. | 3 total technical attempts per episode. | The stated B9 admission constraint. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.6.10.2 — Live-chat first gap
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Live-chat first gap rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Takes in: ACCEPTED — A B9 admission using the corresponding value. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Does: ACCEPTED — Minimum 10 seconds before the first technical re-attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated B9 admission constraint. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Must never: ACCEPTED — Replace this accepted value with an invented retry setting. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without B9 admission under the applicable accepted limits, no re-attempt starts. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Minimum 10 seconds before the first technical re-attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.6.10 — Accepted B9 episode values | A B9 admission using the corresponding value. | Minimum 10 seconds before the first technical re-attempt. | The stated B9 admission constraint. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.6.10.3 — Live-chat second gap
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Live-chat second gap rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Takes in: ACCEPTED — A B9 admission using the corresponding value. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Does: ACCEPTED — Minimum 30 seconds before the next technical re-attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated B9 admission constraint. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Must never: ACCEPTED — Replace this accepted value with an invented retry setting. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without B9 admission under the applicable accepted limits, no re-attempt starts. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Minimum 30 seconds before the next technical re-attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.6.10 — Accepted B9 episode values | A B9 admission using the corresponding value. | Minimum 30 seconds before the next technical re-attempt. | The stated B9 admission constraint. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.6.10.4 — Background first gap
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Background first gap rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Takes in: ACCEPTED — A B9 admission using the corresponding value. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Does: ACCEPTED — Minimum 1 minute before the first technical re-attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated B9 admission constraint. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Must never: ACCEPTED — Replace this accepted value with an invented retry setting. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without B9 admission under the applicable accepted limits, no re-attempt starts. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Minimum 1 minute before the first technical re-attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.6.10 — Accepted B9 episode values | A B9 admission using the corresponding value. | Minimum 1 minute before the first technical re-attempt. | The stated B9 admission constraint. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.6.10.5 — Background second gap
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Background second gap rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Takes in: ACCEPTED — A B9 admission using the corresponding value. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Does: ACCEPTED — Minimum 3 minutes before the next technical re-attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated B9 admission constraint. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Must never: ACCEPTED — Replace this accepted value with an invented retry setting. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without B9 admission under the applicable accepted limits, no re-attempt starts. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Minimum 3 minutes before the next technical re-attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.6.10 — Accepted B9 episode values | A B9 admission using the corresponding value. | Minimum 3 minutes before the next technical re-attempt. | The stated B9 admission constraint. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.6.10.6 — Live-chat elapsed deadline
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Live-chat elapsed deadline rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Takes in: ACCEPTED — A B9 admission using the corresponding value. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Does: ACCEPTED — 7 minutes. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated B9 admission constraint. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Must never: ACCEPTED — Replace this accepted value with an invented retry setting. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without B9 admission under the applicable accepted limits, no re-attempt starts. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — 7 minutes. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.6.10 — Accepted B9 episode values | A B9 admission using the corresponding value. | 7 minutes. | The stated B9 admission constraint. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.6.10.7 — Background elapsed deadline
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Background elapsed deadline rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Takes in: ACCEPTED — A B9 admission using the corresponding value. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Does: ACCEPTED — 15 minutes. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated B9 admission constraint. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Must never: ACCEPTED — Replace this accepted value with an invented retry setting. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without B9 admission under the applicable accepted limits, no re-attempt starts. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — 15 minutes. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.6.10 — Accepted B9 episode values | A B9 admission using the corresponding value. | 15 minutes. | The stated B9 admission constraint. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.6.10.8 — attempt_number
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The attempt_number rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Takes in: ACCEPTED — A B9 admission using the corresponding value. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Does: ACCEPTED — Permanent attempt number, separate from per-episode ordinal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated B9 admission constraint. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Must never: ACCEPTED — Replace this accepted value with an invented retry setting. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Permanent attempt number, separate from per-episode ordinal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.6.10 — Accepted B9 episode values | A B9 admission using the corresponding value. | Permanent attempt number, separate from per-episode ordinal. | The stated B9 admission constraint. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.6.10.9 — Per-episode ordinal
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Per-episode ordinal rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Takes in: ACCEPTED — A B9 admission using the corresponding value. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Does: ACCEPTED — Ordinal within the current episode; original execution is ordinal 1 by reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated B9 admission constraint. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Must never: ACCEPTED — Replace this accepted value with an invented retry setting. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Ordinal within the current episode; original execution is ordinal 1 by reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.6.10 — Accepted B9 episode values | A B9 admission using the corresponding value. | Ordinal within the current episode; original execution is ordinal 1 by reference. | The stated B9 admission constraint. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.6.10.10 — Real-change continuation
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Real-change continuation rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Takes in: ACCEPTED — A B9 admission using the corresponding value. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Does: ACCEPTED — A consumed real-change record with seam-confirmed unchanged canonical inputs is required. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated B9 admission constraint. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Must never: ACCEPTED — Replace this accepted value with an invented retry setting. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without B9 admission under the applicable accepted limits, no re-attempt starts. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — A consumed real-change record with seam-confirmed unchanged canonical inputs is required. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.6.10 — Accepted B9 episode values | A B9 admission using the corresponding value. | A consumed real-change record with seam-confirmed unchanged canonical inputs is required. | The stated B9 admission constraint. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.3] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.7 — Actual execution-context classification
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.6] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Actual execution-context classification rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.6] [NHD-B16EEB]
- Takes in: ACCEPTED — The execution context recorded in E5. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.6] [NHD-B16EEB]
- Does: ACCEPTED — Uses B9 background/nightly classification unless evaluation executed through the live-chat front door. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.6] [NHD-B16EEB]
- Gives out: ACCEPTED — A context-bound B9 retry classification. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.6] [NHD-B16EEB]
- Must never: ACCEPTED — Assume live-chat classification for evaluations run elsewhere. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.6] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Missing or unreadable execution context admits no retry. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.6] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The actual context recorded in E5 controls retry classification; missing or unreadable context admits no retry. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.6] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5 — Evaluation operations and trial execution | The execution context recorded in E5. | Uses B9 background/nightly classification unless evaluation executed through the live-chat front door. | A context-bound B9 retry classification. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.6] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.6 — B9-governed technical re-attempts | The execution context recorded in E5. | Missing/unreadable actual context admits no retry; non-live-chat evaluation uses background/nightly. | A context-bound B9 retry classification. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.6] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.8 — Concurrent heads and deterministic identities
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The four logical compare/identity contracts, without a selected storage or lock mechanism. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Takes in: ACCEPTED — Expected ledger, aggregate or judgment head; unchanged canonical record identity; or result derivation inputs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Does: ACCEPTED — Admits only the current predecessor and identical canonical content; preserves contradictions and refuses stale domain preconditions. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gives out: ACCEPTED — One authoritative successor or deterministic result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Must never: ACCEPTED — Resolve forks by last-writer-wins, retry a domain refusal, or reuse a failed O-APPEND identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Lost ledger race commits nothing; stale domain heads refuse; contradictory identities/forks become indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append: Commits the record and E16 together only if the current head is exactly {n,d} and domain preconditions hold; the new entry uses n+1 and previous_entry_digest=d. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.8.2 — CAS-2 aggregate-head compare-and-replace: Commits only if expected_previous_head remains current; identical key/content absorbs. A stale predecessor refuses, allowing a fresh aggregate from new state as a new operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.8.3 — DET-1 deterministic result identity: Pure derivation from that ledger state produces identical identity/content; repeated identical commitment absorbs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.8.4 — CAS-3 judgment-head compare-and-extend: Commits E9 only if its expected head is still current and CAS-1 holds; identical submission absorbs; stale competing successor refuses. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — The expected head, exact canonical identity/content and record domain preconditions must satisfy the relevant comparison contract. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5 — Evaluation operations and trial execution | Expected ledger, aggregate or judgment head; unchanged canonical record identity; or result derivation inputs. | Admits only the current predecessor and identical canonical content; preserves contradictions and refuses stale domain preconditions. | One authoritative successor or deterministic result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append; C-GOLD.1.5.8.2 — CAS-2 aggregate-head compare-and-replace; C-GOLD.1.5.8.3 — DET-1 deterministic result identity; C-GOLD.1.5.8.4 — CAS-3 judgment-head compare-and-extend

### C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CAS-1 ledger compare-and-append rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Takes in: ACCEPTED — Requested record, its domain preconditions, and expected ledger head {n, d}. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Does: ACCEPTED — Commits the record and E16 together only if the current head is exactly {n,d} and domain preconditions hold; the new entry uses n+1 and previous_entry_digest=d. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gives out: ACCEPTED — Exactly one winning append; competing loser commits neither record nor entry. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Must never: ACCEPTED — Share a sequence position, reuse a failed append ID or change canonical key/content on a technical retry. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A loser ends lost_race_technical with one log; only B9 may admit a new O-APPEND with new ID and unchanged canonical record; no admission means no commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.8.1.1 — Expected head match: Compares the authoritative current head to exactly {n,d} together with domain preconditions. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.8.1.2 — Atomic record and ledger entry: Commits both in the same boundary or neither. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.8.1.3 — Unique next ledger position: Uses sequence n+1 and previous_entry_digest=d; competing appends cannot share the position. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.8.1.4 — Technical lost-race continuation: Ends that append once; B9 may admit a new O-APPEND with a new ID, unchanged canonical key, unchanged requested content and unchanged idempotency identity against the new head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.8.1.5 — Domain-precondition refusal: Ends refused_domain_precondition; privacy refusals use privacy_refused and identity/authority conflicts use terminal_substantive as applicable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gated by: ACCEPTED — Current ledger head equals expected {n,d}, and the requested record domain preconditions hold. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.18 — evaluation_scope_ledger_entry (E16): The winning entry receives n+1 and previous_entry_digest=d together with its canonical record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.8 — Concurrent heads and deterministic identities | Requested record, its domain preconditions, and expected ledger head {n, d}. | Commits the record and E16 together only if the current head is exactly {n,d} and domain preconditions hold; the new entry uses n+1 and previous_entry_digest=d. | Exactly one winning append; competing loser commits neither record nor entry. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.9.3 — EB-3 — Run open | Requested record, its domain preconditions, and expected ledger head {n, d}. | The scope-relevant record and E16 commit together under CAS-1 and the record’s domain precondition. | Exactly one winning append; competing loser commits neither record nor entry. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.9.4 — EB-4 — Attempt start | Requested record, its domain preconditions, and expected ledger head {n, d}. | The scope-relevant record and E16 commit together under CAS-1 and the record’s domain precondition. | Exactly one winning append; competing loser commits neither record nor entry. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.9.5 — EB-5 — Attempt terminal | Requested record, its domain preconditions, and expected ledger head {n, d}. | The scope-relevant record and E16 commit together under CAS-1 and the record’s domain precondition. | Exactly one winning append; competing loser commits neither record nor entry. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.5.9.6 — EB-6 — Attempt resolution | Requested record, its domain preconditions, and expected ledger head {n, d}. | The scope-relevant record and E16 commit together under CAS-1 and the record’s domain precondition. | Exactly one winning append; competing loser commits neither record nor entry. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.5.9.7 — EB-7 — Run terminal | Requested record, its domain preconditions, and expected ledger head {n, d}. | The scope-relevant record and E16 commit together under CAS-1 and the record’s domain precondition. | Exactly one winning append; competing loser commits neither record nor entry. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.5.9.8 — EB-8 — Protected judgment | Requested record, its domain preconditions, and expected ledger head {n, d}. | The scope-relevant record and E16 commit together under CAS-1 and the record’s domain precondition. | Exactly one winning append; competing loser commits neither record nor entry. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.5.9.9 — EB-9 — Aggregate | Requested record, its domain preconditions, and expected ledger head {n, d}. | The scope-relevant record and E16 commit together under CAS-1 and the record’s domain precondition. | Exactly one winning append; competing loser commits neither record nor entry. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 9 · ACCEPTED | C-GOLD.1.5.9.12 — EB-12 — Invalidity or conflict | Requested record, its domain preconditions, and expected ledger head {n, d}. | The scope-relevant record and E16 commit together under CAS-1 and the record’s domain precondition. | Exactly one winning append; competing loser commits neither record nor entry. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 10 · ACCEPTED | C-GOLD.1.5.12.11 — CR-11 — Crash inside a CAS-1 boundary | Requested record, its domain preconditions, and expected ledger head {n, d}. | Recovery follows this rule: Commits the record and E16 together only if the current head is exactly {n,d} and domain preconditions hold; the new entry uses n+1 and previous_entry_digest=d. | Exactly one winning append; competing loser commits neither record nor entry. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 11 · ACCEPTED | C-GOLD.1.5.12.12 — CR-12 — Lost CAS-1 race | Requested record, its domain preconditions, and expected ledger head {n, d}. | Recovery follows this rule: Commits the record and E16 together only if the current head is exactly {n,d} and domain preconditions hold; the new entry uses n+1 and previous_entry_digest=d. | Exactly one winning append; competing loser commits neither record nor entry. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 12 · ACCEPTED | C-GOLD.1.5.2.13 — O-APPEND | Requested record, its domain preconditions, and expected ledger head {n, d}. | Commits the record and E16 together only if the current head is exactly {n,d} and domain preconditions hold; the new entry uses n+1 and previous_entry_digest=d. | Exactly one winning append; competing loser commits neither record nor entry. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 13 · ACCEPTED | C-GOLD.1.4.1 — Scope-relevant atomic append | Requested record, its domain preconditions, and expected ledger head {n, d}. | The record and E16 append together only against the exact current ledger head and domain preconditions. | Exactly one winning append; competing loser commits neither record nor entry. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.8.1.1 — Expected head match; C-GOLD.1.5.8.1.2 — Atomic record and ledger entry; C-GOLD.1.5.8.1.3 — Unique next ledger position; C-GOLD.1.5.8.1.4 — Technical lost-race continuation; C-GOLD.1.5.8.1.5 — Domain-precondition refusal

### C-GOLD.1.5.8.1.1 — Expected head match
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Expected head match rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Current ledger head and expected {n,d}. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — Compares the authoritative current head to exactly {n,d} together with domain preconditions. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — Commit admission only on a match. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Commit against a stale ledger observation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Head mismatch commits nothing and ends lost_race_technical. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Compares the authoritative current head to exactly {n,d} together with domain preconditions. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append | Current ledger head and expected {n,d}. | Compares the authoritative current head to exactly {n,d} together with domain preconditions. | Commit admission only on a match. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.8.1.2 — Atomic record and ledger entry
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Atomic record and ledger entry rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — One requested canonical record and one E16. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — Commits both in the same boundary or neither. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — One paired durable effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Leave only the record or only the ledger entry as the committed effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Crash lookup establishes both or neither. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Commits both in the same boundary or neither. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append | One requested canonical record and one E16. | Commits both in the same boundary or neither. | One paired durable effect. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.8.1.3 — Unique next ledger position
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Unique next ledger position rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — The winning expected head {n,d}. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — Uses sequence n+1 and previous_entry_digest=d; competing appends cannot share the position. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — One new ledger head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Let two entries claim the same sequence position. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The losing boundary commits nothing. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Uses sequence n+1 and previous_entry_digest=d; competing appends cannot share the position. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append | The winning expected head {n,d}. | Uses sequence n+1 and previous_entry_digest=d; competing appends cannot share the position. | One new ledger head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.8.1.4 — Technical lost-race continuation
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Technical lost-race continuation rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — An O-APPEND ending lost_race_technical. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — Ends that append once; B9 may admit a new O-APPEND with a new ID, unchanged canonical key, unchanged requested content and unchanged idempotency identity against the new head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — Separate new append operation, one terminal/log each. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Reuse the loser ID or silently change the canonical record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without B9 admission nothing commits; recovery may fill missing records from durable evidence only, never new effects or model calls. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Ends that append once; B9 may admit a new O-APPEND with a new ID, unchanged canonical key, unchanged requested content and unchanged idempotency identity against the new head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append | An O-APPEND ending lost_race_technical. | Ends that append once; B9 may admit a new O-APPEND with a new ID, unchanged canonical key, unchanged requested content and unchanged idempotency identity against the new head. | Separate new append operation, one terminal/log each. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.8.1.5 — Domain-precondition refusal
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Domain-precondition refusal rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Stale judgment/aggregate head, attempt after E8, missing/unverifiable/mismatched authority, mode mismatch or invalid output. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — Ends refused_domain_precondition; privacy refusals use privacy_refused and identity/authority conflicts use terminal_substantive as applicable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — A non-machine-retryable refusal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Treat a domain refusal as a technical race or machine-retry the rejected record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A subsequent deliberate operation needs new content and identity, not a B9 retry. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Ends refused_domain_precondition; privacy refusals use privacy_refused and identity/authority conflicts use terminal_substantive as applicable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append | Stale judgment/aggregate head, attempt after E8, missing/unverifiable/mismatched authority, mode mismatch or invalid output. | Ends refused_domain_precondition; privacy refusals use privacy_refused and identity/authority conflicts use terminal_substantive as applicable. | A non-machine-retryable refusal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.8.2 — CAS-2 aggregate-head compare-and-replace
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CAS-2 aggregate-head compare-and-replace rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Takes in: ACCEPTED — E10, its expected prior aggregate head or none, terminal-set digest, E7r digest and judgment-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Does: ACCEPTED — Commits only if expected_previous_head remains current; identical key/content absorbs. A stale predecessor refuses, allowing a fresh aggregate from new state as a new operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gives out: ACCEPTED — One current aggregate head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Must never: ACCEPTED — Choose between forks by recency or machine-retry new aggregate content as the old operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Different content under one key or two successors of one head makes the run indeterminate; stale head returns aggregate_refused_stale_head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — expected_previous_head is the current aggregate head, or none for the first; identical key/content may absorb. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.8 — Concurrent heads and deterministic identities | E10, its expected prior aggregate head or none, terminal-set digest, E7r digest and judgment-set digest. | Commits only if expected_previous_head remains current; identical key/content absorbs. A stale predecessor refuses, allowing a fresh aggregate from new state as a new operation. | One current aggregate head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.9.9 — EB-9 — Aggregate | E10, its expected prior aggregate head or none, terminal-set digest, E7r digest and judgment-set digest. | Applies this defining record/rule contract: Commits only if expected_previous_head remains current; identical key/content absorbs. A stale predecessor refuses, allowing a fresh aggregate from new state as a new operation. | One current aggregate head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.12.13 — CR-13 — Lost CAS-2 race | E10, its expected prior aggregate head or none, terminal-set digest, E7r digest and judgment-set digest. | Recovery follows this rule: Commits only if expected_previous_head remains current; identical key/content absorbs. A stale predecessor refuses, allowing a fresh aggregate from new state as a new operation. | One current aggregate head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.12.14 — CR-14 — Aggregate fork or same-key different content found | E10, its expected prior aggregate head or none, terminal-set digest, E7r digest and judgment-set digest. | Recovery follows this rule: Commits only if expected_previous_head remains current; identical key/content absorbs. A stale predecessor refuses, allowing a fresh aggregate from new state as a new operation. | One current aggregate head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.5.2.7 — O-AGGREGATE | E10, its expected prior aggregate head or none, terminal-set digest, E7r digest and judgment-set digest. | Commits only if expected_previous_head remains current; identical key/content absorbs. A stale predecessor refuses, allowing a fresh aggregate from new state as a new operation. | One current aggregate head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.3.11 — suite_aggregate_result (E10) | E10, its expected prior aggregate head or none, terminal-set digest, E7r digest and judgment-set digest. | Aggregate commit requires the expected current aggregate head; forks make the run indeterminate. | One current aggregate head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.8.3 — DET-1 deterministic result identity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The DET-1 deterministic result identity rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Takes in: ACCEPTED — scope, bound ledger head and evaluated-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Does: ACCEPTED — Pure derivation from that ledger state produces identical identity/content; repeated identical commitment absorbs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gives out: ACCEPTED — One deterministic E11a/E11b/E12 result. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Must never: ACCEPTED — Accept different contents under the same identity or choose one by recency. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Different state/content yields result_contradiction; preserve both, neither satisfies B16/B24, scope results remain indeterminate until lookup reconciliation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — scope, bound ledger head and evaluated-set digest identify one pure derivation with one content. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.8 — Concurrent heads and deterministic identities | scope, bound ledger head and evaluated-set digest. | Pure derivation from that ledger state produces identical identity/content; repeated identical commitment absorbs. | One deterministic E11a/E11b/E12 result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.9.10 — EB-10 — Result derivation | scope, bound ledger head and evaluated-set digest. | Applies this defining record/rule contract: Pure derivation from that ledger state produces identical identity/content; repeated identical commitment absorbs. | One deterministic E11a/E11b/E12 result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.12.15 — CR-15 — Crash during E11/E12 derivation | scope, bound ledger head and evaluated-set digest. | Recovery follows this rule: Pure derivation from that ledger state produces identical identity/content; repeated identical commitment absorbs. | One deterministic E11a/E11b/E12 result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.12.16 — CR-16 — Same-identity result with different content found | scope, bound ledger head and evaluated-set digest. | Recovery follows this rule: Pure derivation from that ledger state produces identical identity/content; repeated identical commitment absorbs. | One deterministic E11a/E11b/E12 result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.5.2.8 — O-RESULT | scope, bound ledger head and evaluated-set digest. | Pure derivation from that ledger state produces identical identity/content; repeated identical commitment absorbs. | One deterministic E11a/E11b/E12 result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.3.12 — gold_evidence_result (E11a) | scope, bound ledger head and evaluated-set digest. | The same scope, head and evaluated-set digest must yield the same identity/content; contradictions satisfy no consumer. | One deterministic E11a/E11b/E12 result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.3.13 — held_out_evidence_result (E11b) | scope, bound ledger head and evaluated-set digest. | The same scope, head and evaluated-set digest must yield the same identity/content; contradictions satisfy no consumer. | One deterministic E11a/E11b/E12 result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.3.14 — b24_system_eligibility_result (E12) | scope, bound ledger head and evaluated-set digest. | The same scope, head and evaluated-set digest must yield the same identity/content; contradictions satisfy no consumer. | One deterministic E11a/E11b/E12 result. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.8.4 — CAS-3 judgment-head compare-and-extend
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CAS-3 judgment-head compare-and-extend rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Takes in: ACCEPTED — One effectively completed output’s planned_trial_output_key, expected judgment head or none, and E9 content. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Does: ACCEPTED — Commits E9 only if its expected head is still current and CAS-1 holds; identical submission absorbs; stale competing successor refuses. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gives out: ACCEPTED — At most one successor for a current judgment head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Must never: ACCEPTED — Extend a fork, select by recency or machine-retry stale competing judgments. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Stale successor is judgment_refused_stale_head; a fork or different content under one E9 identity is an integrity contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — expected_previous_judgment_head is still the current head and CAS-1 also holds; identical submission may absorb. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.8 — Concurrent heads and deterministic identities | One effectively completed output’s planned_trial_output_key, expected judgment head or none, and E9 content. | Commits E9 only if its expected head is still current and CAS-1 holds; identical submission absorbs; stale competing successor refuses. | At most one successor for a current judgment head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.9.8 — EB-8 — Protected judgment | One effectively completed output’s planned_trial_output_key, expected judgment head or none, and E9 content. | E9 must extend the still-current judgment head. | At most one successor for a current judgment head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.9.8.3 — Atomic judgment record | One effectively completed output’s planned_trial_output_key, expected judgment head or none, and E9 content. | Commits E9 only if its expected head is still current and CAS-1 holds; identical submission absorbs; stale competing successor refuses. | At most one successor for a current judgment head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.2.6 — O-JUDGE | One effectively completed output’s planned_trial_output_key, expected judgment head or none, and E9 content. | Commits E9 only if its expected head is still current and CAS-1 holds; identical submission absorbs; stale competing successor refuses. | At most one successor for a current judgment head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.3.10 — evaluation_judgment (E9) | One effectively completed output’s planned_trial_output_key, expected judgment head or none, and E9 content. | Judgment commit requires the expected head still current and CAS-1 satisfied. | At most one successor for a current judgment head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.9 — Evaluation transaction boundaries
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The twelve logical commit boundaries EB-1 through EB-12. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Takes in: ACCEPTED — The corresponding operation’s canonical record and required gate evidence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Does: ACCEPTED — Applies the owning record and rule contracts before each durable transition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Gives out: ACCEPTED — Canonical effects with their exact owner. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Must never: ACCEPTED — Treat EB-8’s protected stages as one atomic transaction or acknowledge before required logs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Refuses the transition when its stated gate fails; scope writes use O-APPEND. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.9.1 — EB-1 — Suite registration: Registers E1 only after integrity, seal and acceptance; benchmark kind also requires NHD-B16EEB-D15 approval. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.9.2 — EB-2 — Setup registration: Registers setup; E3 is refused if any required family, scope, named measurement declaration or bound gold cell is missing. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.9.3 — EB-3 — Run open: Commits E5 + E16 under CAS-1; evidentiary opening requires the complete current epoch including trial count, full plan and exact cell. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.9.4 — EB-4 — Attempt start: Commits E6 + E16; later ordinals require B9 admission; no start after E8 or while an attempt of that trial is unresolved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.9.5 — EB-5 — Attempt terminal: Commits exactly one E7 + E16. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.9.6 — EB-6 — Attempt resolution: Commits E7r + E16 under the unresolved-attempt resolution rules. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.9.7 — EB-7 — Run terminal: Commits E8 + E16 only after every started attempt has E7 and none is live/admitted-unstarted. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.9.8 — EB-8 — Protected judgment: Uses three linked separately durable stages: winning authorization claim; conditional BAI consumption with flushed receipt; then atomic E9 + E16 through O-APPEND under CAS-1 and CAS-3. O-APPEND re-verifies the bound receipt, or verifies fresh valid session proof at commit. Mode must match E1; output must be effectively completed and integrity-matched. Own successful token consumption is expected, never a refusal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.9.9 — EB-9 — Aggregate: Commits E10 + E16 only against the current expected aggregate head, under CAS-2. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.9.10 — EB-10 — Result derivation: Commits E11a, E11b or E12 under DET-1. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.9.11 — EB-11 — Evidence reference: Issues E13 for E11a/E11b only. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.9.12 — EB-12 — Invalidity or conflict: Commits E14 or E15 + E16 only under the applicable accepted policy. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — Each boundary satisfies its defining record condition and its linked rule cards before its effect commits. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5 — Evaluation operations and trial execution | The corresponding operation’s canonical record and required gate evidence. | Applies the owning record and rule contracts before each durable transition. | Canonical effects with their exact owner. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.9.1 — EB-1 — Suite registration; C-GOLD.1.5.9.2 — EB-2 — Setup registration; C-GOLD.1.5.9.3 — EB-3 — Run open; C-GOLD.1.5.9.4 — EB-4 — Attempt start; C-GOLD.1.5.9.5 — EB-5 — Attempt terminal; C-GOLD.1.5.9.6 — EB-6 — Attempt resolution; C-GOLD.1.5.9.7 — EB-7 — Run terminal; C-GOLD.1.5.9.8 — EB-8 — Protected judgment; C-GOLD.1.5.9.9 — EB-9 — Aggregate; C-GOLD.1.5.9.10 — EB-10 — Result derivation; C-GOLD.1.5.9.11 — EB-11 — Evidence reference; C-GOLD.1.5.9.12 — EB-12 — Invalidity or conflict

### C-GOLD.1.5.9.1 — EB-1 — Suite registration
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The EB-1 — Suite registration rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — Suite identity, cases, scoring bindings, acceptance and privacy classification. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Registers E1 only after integrity, seal and acceptance; benchmark kind also requires NHD-B16EEB-D15 approval. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The named boundary’s canonical effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass the boundary’s stated identity, authority or policy condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No benchmark manifest without NHD-B16EEB-D15; no held-out manifest without an accepted held-out policy. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.2 — evaluation_suite_manifest (E1): Applies this defining record/rule contract: Registers only after integrity, seal and acceptance checks; benchmark suites additionally require an accepted concrete suite; held-out requires its accepted policy. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: Acknowledgement waits for the owning terminal and its one operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.2 — evaluation_suite_manifest (E1): For the corresponding requested record kind, commits E1 at this boundary only after its stated gates; existing records are not overwritten. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.9 — Evaluation transaction boundaries | Suite identity, cases, scoring bindings, acceptance and privacy classification. | Registers E1 only after integrity, seal and acceptance; benchmark kind also requires NHD-B16EEB-D15 approval. | The named boundary’s canonical effect. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.9.2 — EB-2 — Setup registration
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The EB-2 — Setup registration rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — A candidate E3 profile. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Registers setup; E3 is refused if any required family, scope, named measurement declaration or bound gold cell is missing. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The named boundary’s canonical effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass the boundary’s stated identity, authority or policy condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Any of the four missing-coverage conditions refuses registration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.4.4 — Coverage profile registration gate: Applies this defining record/rule contract: Refuses omitted family, omitted scope, undeclared measurement or absent gold cell. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: Acknowledgement waits for the owning terminal and its one operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.2.3 — policy_epoch (E2e): For the corresponding requested record kind, commits E2e at this boundary only after its stated gates; existing records are not overwritten. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.4 — required_coverage_profile (E3): For the corresponding requested record kind, commits E3 at this boundary only after its stated gates; existing records are not overwritten. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.2.1 — model_evaluation_profile (E4): For the corresponding requested record kind, commits E4 at this boundary only after its stated gates; existing records are not overwritten. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.2.2 — system_candidate_profile (E4S): For the corresponding requested record kind, commits E4S at this boundary only after its stated gates; existing records are not overwritten. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.9 — Evaluation transaction boundaries | A candidate E3 profile. | Registers setup; E3 is refused if any required family, scope, named measurement declaration or bound gold cell is missing. | The named boundary’s canonical effect. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.9.3 — EB-3 — Run open
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The EB-3 — Run open rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — Run class, scope, profile, cell, suite kind, rule, epoch, context and full plan. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Commits E5 + E16 under CAS-1; evidentiary opening requires the complete current epoch including trial count, full plan and exact cell. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The named boundary’s canonical effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass the boundary’s stated identity, authority or policy condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A subset of suite cases × trial count is refused; evidentiary opening also requires a complete current epoch. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A loser ends lost_race_technical with one log; only B9 may admit a new O-APPEND with new ID and unchanged canonical record; no admission means no commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.5 — evaluation_run_open (E5): Applies this defining record/rule contract: Freezes the run’s exact evidence context before execution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append: The scope-relevant record and E16 commit together under CAS-1 and the record’s domain precondition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: Acknowledgement waits for the owning terminal and its one operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.5 — evaluation_run_open (E5): For the corresponding requested record kind, commits E5 at this boundary only after its stated gates; existing records are not overwritten. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.9 — Evaluation transaction boundaries | Run class, scope, profile, cell, suite kind, rule, epoch, context and full plan. | Commits E5 + E16 under CAS-1; evidentiary opening requires the complete current epoch including trial count, full plan and exact cell. | The named boundary’s canonical effect. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.9.4 — EB-4 — Attempt start
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The EB-4 — Attempt start rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — run, case_id, trial_index, attempt_id and shared output key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Commits E6 + E16; later ordinals require B9 admission; no start after E8 or while an attempt of that trial is unresolved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The named boundary’s canonical effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass the boundary’s stated identity, authority or policy condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unadmitted later attempts, unresolved-existence attempts and post-E8 starts are refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A loser ends lost_race_technical with one log; only B9 may admit a new O-APPEND with new ID and unchanged canonical record; no admission means no commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.6 — trial_attempt_start (E6): Applies this defining record/rule contract: Records ordinal 1 as original execution; every later attempt binds committed B9 R1 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append: The scope-relevant record and E16 commit together under CAS-1 and the record’s domain precondition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.11 — Unresolved-attempt resolution semantics: No start while any attempt of this planned trial has unresolved output existence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.6.7 — Committed B9 R1 admission: Ordinal ≥ 2 requires committed B9 R1 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: Acknowledgement waits for the owning terminal and its one operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.6 — trial_attempt_start (E6): For the corresponding requested record kind, commits E6 at this boundary only after its stated gates; existing records are not overwritten. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.9 — Evaluation transaction boundaries | run, case_id, trial_index, attempt_id and shared output key. | Commits E6 + E16; later ordinals require B9 admission; no start after E8 or while an attempt of that trial is unresolved. | The named boundary’s canonical effect. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.9.5 — EB-5 — Attempt terminal
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The EB-5 — Attempt terminal rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — Attempt identity, terminal outcome and any deterministic findings. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Commits exactly one E7 + E16. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The named boundary’s canonical effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass the boundary’s stated identity, authority or policy condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A mismatched checker makes the finding invalid and the run head indeterminate; unresolved attempts cannot be retried. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A loser ends lost_race_technical with one log; only B9 may admit a new O-APPEND with new ID and unchanged canonical record; no admission means no commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.7 — trial_attempt_terminal (E7): Applies this defining record/rule contract: Records completed, failed, interrupted/abandoned or unresolved outcome. Deterministic findings bind the exact accepted checker. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append: The scope-relevant record and E16 commit together under CAS-1 and the record’s domain precondition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: Acknowledgement waits for the owning terminal and its one operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.7 — trial_attempt_terminal (E7): For the corresponding requested record kind, commits E7 at this boundary only after its stated gates; existing records are not overwritten. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.9 — Evaluation transaction boundaries | Attempt identity, terminal outcome and any deterministic findings. | Commits exactly one E7 + E16. | The named boundary’s canonical effect. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.9.6 — EB-6 — Attempt resolution
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The EB-6 — Attempt resolution rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — Durable lookup evidence for the attempt’s output. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Commits E7r + E16 under the unresolved-attempt resolution rules. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The named boundary’s canonical effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass the boundary’s stated identity, authority or policy condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Contradictory conclusive outcomes make state indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A loser ends lost_race_technical with one log; only B9 may admit a new O-APPEND with new ID and unchanged canonical record; no admission means no commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.8 — trial_attempt_resolution (E7r): Applies this defining record/rule contract: Records resolved_output_found, resolved_absence_proven or still_undetermined; preserves E7. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append: The scope-relevant record and E16 commit together under CAS-1 and the record’s domain precondition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: Acknowledgement waits for the owning terminal and its one operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.8 — trial_attempt_resolution (E7r): For the corresponding requested record kind, commits E7r at this boundary only after its stated gates; existing records are not overwritten. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.9 — Evaluation transaction boundaries | Durable lookup evidence for the attempt’s output. | Commits E7r + E16 under the unresolved-attempt resolution rules. | The named boundary’s canonical effect. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.9.7 — EB-7 — Run terminal
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The EB-7 — Run terminal rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — Every started attempt’s E7, planned-trial completions and B9 admitted/live state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Commits E8 + E16 only after every started attempt has E7 and none is live/admitted-unstarted. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The named boundary’s canonical effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass the boundary’s stated identity, authority or policy condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unknown evidence, integrity failure or contradiction cannot yield run_completed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A loser ends lost_race_technical with one log; only B9 may admit a new O-APPEND with new ID and unchanged canonical record; no admission means no commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.3 — Run closing conditions: Applies this defining record/rule contract: Allows E8 only after all started attempts have a terminal and no planned-trial attempt is live or admitted-unstarted. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append: The scope-relevant record and E16 commit together under CAS-1 and the record’s domain precondition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: Acknowledgement waits for the owning terminal and its one operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.9 — evaluation_run_terminal (E8): For the corresponding requested record kind, commits E8 at this boundary only after its stated gates; existing records are not overwritten. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.9 — Evaluation transaction boundaries | Every started attempt’s E7, planned-trial completions and B9 admitted/live state. | Commits E8 + E16 only after every started attempt has E7 and none is live/admitted-unstarted. | The named boundary’s canonical effect. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.9.8 — EB-8 — Protected judgment
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The EB-8 — Protected judgment rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — Output identity/integrity, expected head, scoring mode and event-time authority proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Uses three linked separately durable stages: winning authorization claim; conditional BAI consumption with flushed receipt; then atomic E9 + E16 through O-APPEND under CAS-1 and CAS-3. O-APPEND re-verifies the bound receipt, or verifies fresh valid session proof at commit. Mode must match E1; output must be effectively completed and integrity-matched. Own successful token consumption is expected, never a refusal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The named boundary’s canonical effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass the boundary’s stated identity, authority or policy condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unaccepted NHD-B16EEB-D16 refuses every Ness judgment; stale competing heads are refused; fork or identity contradiction is judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A loser ends lost_race_technical with one log; only B9 may admit a new O-APPEND with new ID and unchanged canonical record; no admission means no commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Stale successor is judgment_refused_stale_head; a fork or different content under one E9 identity is an integrity contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.9.8.1 — Authorization claim first: Commits the one-winner judgment-authorization claim first; this coordinates but grants no authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.9.8.2 — Conditional BAI receipt: Under the BAI option, BAI revalidates and consumes only the attached winning token, then flushes bai_token_consumed as the authorization commit point; claim becomes consumed_pending_commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.9.8.3 — Atomic judgment record: Commits E9 + E16 atomically under CAS-1/CAS-3, re-verifying the receipt or freshly verifying session proof; the claim becomes judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment (E9): Applies this defining record/rule contract: Appends a judgment under the current-head and accepted authority conditions; identical resubmission absorbs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append: The scope-relevant record and E16 commit together under CAS-1 and the record’s domain precondition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.4 — CAS-3 judgment-head compare-and-extend: E9 must extend the still-current judgment head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: Acknowledgement waits for the owning terminal and its one operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment (E9): For the corresponding requested record kind, commits E9 at this boundary only after its stated gates; existing records are not overwritten. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.9 — Evaluation transaction boundaries | Output identity/integrity, expected head, scoring mode and event-time authority proof. | Uses three linked separately durable stages: winning authorization claim; conditional BAI consumption with flushed receipt; then atomic E9 + E16 through O-APPEND under CAS-1 and CAS-3. O-APPEND re-verifies the bound receipt, or verifies fresh valid session proof at commit. Mode must match E1; output must be effectively completed and integrity-matched. Own successful token consumption is expected, never a refusal. | The named boundary’s canonical effect. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.9.8.1 — Authorization claim first; C-GOLD.1.5.9.8.2 — Conditional BAI receipt; C-GOLD.1.5.9.8.3 — Atomic judgment record

### C-GOLD.1.5.9.8.1 — Authorization claim first
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Authorization claim first rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — Authorization claim first stage inputs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Commits the one-winner judgment-authorization claim first; this coordinates but grants no authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — The source-defined stage effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Collapse all three stages into one transaction or trust only an earlier authority check. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Concurrent claim creation admits one winner; the loser consumes nothing and ends judgment_claim_lost. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.2.6 — O-JUDGE: Owns the protected claim → conditional BAI receipt → E9 protocol; stages are separately durable, not one atomic transaction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.9.8 — EB-8 — Protected judgment | Authorization claim first stage inputs. | Commits the one-winner judgment-authorization claim first; this coordinates but grants no authority. | The source-defined stage effect. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.9.8.2 — Conditional BAI receipt
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Conditional BAI receipt rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — Conditional BAI receipt stage inputs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Under the BAI option, BAI revalidates and consumes only the attached winning token, then flushes bai_token_consumed as the authorization commit point; claim becomes consumed_pending_commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — The source-defined stage effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Collapse all three stages into one transaction or trust only an earlier authority check. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Absent or unverifiable durable receipt proves no committed authority; failed receipt write ends judgment_authorization_failed for that token. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment (E9): Appends a judgment under the current-head and accepted authority conditions; identical resubmission absorbs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.9.8 — EB-8 — Protected judgment | Conditional BAI receipt stage inputs. | Under the BAI option, BAI revalidates and consumes only the attached winning token, then flushes bai_token_consumed as the authorization commit point; claim becomes consumed_pending_commit. | The source-defined stage effect. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.9.8.3 — Atomic judgment record
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Atomic judgment record rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — Atomic judgment record stage inputs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Commits E9 + E16 atomically under CAS-1/CAS-3, re-verifying the receipt or freshly verifying session proof; the claim becomes judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — The source-defined stage effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Collapse all three stages into one transaction or trust only an earlier authority check. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A stale expected judgment head refuses commit; a changed head contrary to a receipt fence is an integrity breach, never forced through. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.8.4 — CAS-3 judgment-head compare-and-extend: Commits E9 only if its expected head is still current and CAS-1 holds; identical submission absorbs; stale competing successor refuses. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.9.8 — EB-8 — Protected judgment | Atomic judgment record stage inputs. | Commits E9 + E16 atomically under CAS-1/CAS-3, re-verifying the receipt or freshly verifying session proof; the claim becomes judgment_committed. | The source-defined stage effect. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.9.9 — EB-9 — Aggregate
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The EB-9 — Aggregate rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — E10, its expected prior aggregate head or none, terminal-set digest, E7r digest and judgment-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Commits E10 + E16 only against the current expected aggregate head, under CAS-2. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The named boundary’s canonical effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass the boundary’s stated identity, authority or policy condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Different content under one key or two successors of one head makes the run indeterminate; stale head returns aggregate_refused_stale_head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A loser ends lost_race_technical with one log; only B9 may admit a new O-APPEND with new ID and unchanged canonical record; no admission means no commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.8.2 — CAS-2 aggregate-head compare-and-replace: Applies this defining record/rule contract: Commits only if expected_previous_head remains current; identical key/content absorbs. A stale predecessor refuses, allowing a fresh aggregate from new state as a new operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append: The scope-relevant record and E16 commit together under CAS-1 and the record’s domain precondition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: Acknowledgement waits for the owning terminal and its one operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result (E10): For the corresponding requested record kind, commits E10 at this boundary only after its stated gates; existing records are not overwritten. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.9 — Evaluation transaction boundaries | E10, its expected prior aggregate head or none, terminal-set digest, E7r digest and judgment-set digest. | Commits E10 + E16 only against the current expected aggregate head, under CAS-2. | The named boundary’s canonical effect. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.9.10 — EB-10 — Result derivation
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The EB-10 — Result derivation rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — scope, bound ledger head and evaluated-set digest. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Commits E11a, E11b or E12 under DET-1. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The named boundary’s canonical effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass the boundary’s stated identity, authority or policy condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Different state/content yields result_contradiction; preserve both, neither satisfies B16/B24, scope results remain indeterminate until lookup reconciliation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.8.3 — DET-1 deterministic result identity: Applies this defining record/rule contract: Pure derivation from that ledger state produces identical identity/content; repeated identical commitment absorbs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: Acknowledgement waits for the owning terminal and its one operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.12 — gold_evidence_result (E11a): For the corresponding requested record kind, commits E11a at this boundary only after its stated gates; existing records are not overwritten. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.13 — held_out_evidence_result (E11b): For the corresponding requested record kind, commits E11b at this boundary only after its stated gates; existing records are not overwritten. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.14 — b24_system_eligibility_result (E12): For the corresponding requested record kind, commits E12 at this boundary only after its stated gates; existing records are not overwritten. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.9 — Evaluation transaction boundaries | scope, bound ledger head and evaluated-set digest. | Commits E11a, E11b or E12 under DET-1. | The named boundary’s canonical effect. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.9.11 — EB-11 — Evidence reference
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The EB-11 — Evidence reference rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — Evidence kind, result identity/integrity, scope and bound ledger head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Issues E13 for E11a/E11b only. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The named boundary’s canonical effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass the boundary’s stated identity, authority or policy condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Non-current evidence is unusable for a new B16 check; wrong-kind or invalid pointers cannot pass. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13): Applies this defining record/rule contract: Points only to E11a for input 3 or E11b for input 4. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: Acknowledgement waits for the owning terminal and its one operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13): For the corresponding requested record kind, commits E13 at this boundary only after its stated gates; existing records are not overwritten. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.9 — Evaluation transaction boundaries | Evidence kind, result identity/integrity, scope and bound ledger head. | Issues E13 for E11a/E11b only. | The named boundary’s canonical effect. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.9.12 — EB-12 — Invalidity or conflict
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The EB-12 — Invalidity or conflict rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Takes in: ACCEPTED — Accepted objective invalidity rule and recorded objective facts. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Does: ACCEPTED — Commits E14 or E15 + E16 only under the applicable accepted policy. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Gives out: ACCEPTED — The named boundary’s canonical effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass the boundary’s stated identity, authority or policy condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without an accepted objective rule exclusion is refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A loser ends lost_race_technical with one log; only B9 may admit a new O-APPEND with new ID and unchanged canonical record; no admission means no commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without accepted policy, failed or indeterminate heads retain their blocking effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.16 — evaluation_invalidity_record (E14): Applies this defining record/rule contract: Excludes only under that accepted rule; no such rule currently exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append: The scope-relevant record and E16 commit together under CAS-1 and the record’s domain precondition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.17 — evaluation_conflict_resolution (E15): Conflict resolution requires the accepted completed-run disagreement policy and every affected run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: Acknowledgement waits for the owning terminal and its one operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.16 — evaluation_invalidity_record (E14): For the corresponding requested record kind, commits E14 at this boundary only after its stated gates; existing records are not overwritten. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.17 — evaluation_conflict_resolution (E15): For the corresponding requested record kind, commits E15 at this boundary only after its stated gates; existing records are not overwritten. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.9 — Evaluation transaction boundaries | Accepted objective invalidity rule and recorded objective facts. | Commits E14 or E15 + E16 only under the applicable accepted policy. | The named boundary’s canonical effect. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.10 — Evaluation idempotency keys
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The canonical duplicate-prevention keys, distinct from operation identities. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Takes in: ACCEPTED — An existing or repeated canonical record/operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Does: ACCEPTED — Uses the source-defined key for each record kind; identical repeats absorb where specified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Gives out: ACCEPTED — At most the permitted canonical effect. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Must never: ACCEPTED — Change the key to create a second output, terminal, conclusive resolution, successor or log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.10.1 — E1 idempotency key: name + version + integrity (same name/version, different integrity → contradiction) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.10.2 — E2e / E3 / E4 / E4S idempotency key: content digest [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.10.3 — Run idempotency key: run ID; identical repeat absorbs; different content refused [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.10.4 — Planned trial idempotency key: planned_trial_key; one B9 group [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.10.5 — Output idempotency key: planned_trial_output_key; one committed output ever [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.10.6 — Attempt start / terminal idempotency key: {planned_trial_key, attempt_id} / attempt ID [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.10.7 — Conclusive resolution idempotency key: {attempt_id, conclusive} — at most one resolved_output_found or resolved_absence_proven ever [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.10.8 — Undetermined resolution idempotency key: {attempt_id, resolution_sequence} [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.10.9 — Run terminal idempotency key: run ID [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.10.10 — Judgment idempotency key: E9 identity {judgment_chain_key, expected_previous_judgment_head, content digest}; identical re-submission absorbs; at most one committed successor per predecessor (CAS-3) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.10.11 — O-APPEND idempotency key: its own operation ID; the requested record's own idempotency key is the canonical key B9 groups on [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.10.12 — Ledger entry idempotency key: {scope, sequence_number} — CAS-1 [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.10.13 — Aggregate idempotency key: {run, expected_previous_head, terminal-set digest, E7r digest, judgment-set digest} — CAS-2 [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.10.14 — Results idempotency key: DET-1 identity [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.10.15 — E13 / E14 / E15 / logs idempotency key: result + kind / excluded run / affected-run set / operation ID [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Gated by: ACCEPTED — Each record uses its own canonical duplicate-prevention identity; operation IDs remain separate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5 — Evaluation operations and trial execution | An existing or repeated canonical record/operation. | Uses the source-defined key for each record kind; identical repeats absorb where specified. | At most the permitted canonical effect. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.10.1 — E1 idempotency key; C-GOLD.1.5.10.2 — E2e / E3 / E4 / E4S idempotency key; C-GOLD.1.5.10.3 — Run idempotency key; C-GOLD.1.5.10.4 — Planned trial idempotency key; C-GOLD.1.5.10.5 — Output idempotency key; C-GOLD.1.5.10.6 — Attempt start / terminal idempotency key; C-GOLD.1.5.10.7 — Conclusive resolution idempotency key; C-GOLD.1.5.10.8 — Undetermined resolution idempotency key; C-GOLD.1.5.10.9 — Run terminal idempotency key; C-GOLD.1.5.10.10 — Judgment idempotency key; C-GOLD.1.5.10.11 — O-APPEND idempotency key; C-GOLD.1.5.10.12 — Ledger entry idempotency key; C-GOLD.1.5.10.13 — Aggregate idempotency key; C-GOLD.1.5.10.14 — Results idempotency key; C-GOLD.1.5.10.15 — E13 / E14 / E15 / logs idempotency key

### C-GOLD.1.5.10.1 — E1 idempotency key
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The E1 idempotency key rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Takes in: ACCEPTED — A repeated E1 request. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Does: ACCEPTED — name + version + integrity (same name/version, different integrity → contradiction) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Gives out: ACCEPTED — Canonical identity: name + version + integrity (same name/version, different integrity → contradiction) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass this canonical identity by changing a retry’s key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fails closed by: ACCEPTED — name + version + integrity (same name/version, different integrity → contradiction) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — name + version + integrity (same name/version, different integrity → contradiction) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.10 — Evaluation idempotency keys | A repeated E1 request. | name + version + integrity (same name/version, different integrity → contradiction) | Canonical identity: name + version + integrity (same name/version, different integrity → contradiction) | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.10.2 — E2e / E3 / E4 / E4S idempotency key
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The E2e / E3 / E4 / E4S idempotency key rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Takes in: ACCEPTED — A repeated E2e / E3 / E4 / E4S request. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Does: ACCEPTED — content digest [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Gives out: ACCEPTED — Canonical identity: content digest [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass this canonical identity by changing a retry’s key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — content digest [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.10 — Evaluation idempotency keys | A repeated E2e / E3 / E4 / E4S request. | content digest | Canonical identity: content digest | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.10.3 — Run idempotency key
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Run idempotency key rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Takes in: ACCEPTED — A repeated Run request. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Does: ACCEPTED — run ID; identical repeat absorbs; different content refused [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Gives out: ACCEPTED — Canonical identity: run ID; identical repeat absorbs; different content refused [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass this canonical identity by changing a retry’s key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fails closed by: ACCEPTED — run ID; identical repeat absorbs; different content refused [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — run ID; identical repeat absorbs; different content refused [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.10 — Evaluation idempotency keys | A repeated Run request. | run ID; identical repeat absorbs; different content refused | Canonical identity: run ID; identical repeat absorbs; different content refused | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.10.4 — Planned trial idempotency key
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Planned trial idempotency key rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Takes in: ACCEPTED — A repeated Planned trial request. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Does: ACCEPTED — planned_trial_key; one B9 group [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Gives out: ACCEPTED — Canonical identity: planned_trial_key; one B9 group [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass this canonical identity by changing a retry’s key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Completed output is terminal_success and retries absorb; unknown existence requires recovery first. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — planned_trial_key; one B9 group [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.10 — Evaluation idempotency keys | A repeated Planned trial request. | planned_trial_key; one B9 group | Canonical identity: planned_trial_key; one B9 group | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.10.5 — Output idempotency key
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Output idempotency key rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Takes in: ACCEPTED — A repeated Output request. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Does: ACCEPTED — planned_trial_output_key; one committed output ever [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Gives out: ACCEPTED — Canonical identity: planned_trial_output_key; one committed output ever [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass this canonical identity by changing a retry’s key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fails closed by: ACCEPTED — One completed output absorbs any retry. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — planned_trial_output_key; one committed output ever [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.10 — Evaluation idempotency keys | A repeated Output request. | planned_trial_output_key; one committed output ever | Canonical identity: planned_trial_output_key; one committed output ever | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.10.6 — Attempt start / terminal idempotency key
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Attempt start / terminal idempotency key rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Takes in: ACCEPTED — A repeated Attempt start / terminal request. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Does: ACCEPTED — {planned_trial_key, attempt_id} / attempt ID [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Gives out: ACCEPTED — Canonical identity: {planned_trial_key, attempt_id} / attempt ID [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass this canonical identity by changing a retry’s key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — {planned_trial_key, attempt_id} / attempt ID [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.10 — Evaluation idempotency keys | A repeated Attempt start / terminal request. | {planned_trial_key, attempt_id} / attempt ID | Canonical identity: {planned_trial_key, attempt_id} / attempt ID | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.10.7 — Conclusive resolution idempotency key
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Conclusive resolution idempotency key rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Takes in: ACCEPTED — A repeated Conclusive resolution request. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Does: ACCEPTED — {attempt_id, conclusive} — at most one resolved_output_found or resolved_absence_proven ever [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Gives out: ACCEPTED — Canonical identity: {attempt_id, conclusive} — at most one resolved_output_found or resolved_absence_proven ever [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass this canonical identity by changing a retry’s key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A later contradictory conclusive resolution makes state indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — {attempt_id, conclusive} — at most one resolved_output_found or resolved_absence_proven ever [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.10 — Evaluation idempotency keys | A repeated Conclusive resolution request. | {attempt_id, conclusive} — at most one resolved_output_found or resolved_absence_proven ever | Canonical identity: {attempt_id, conclusive} — at most one resolved_output_found or resolved_absence_proven ever | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.10.8 — Undetermined resolution idempotency key
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Undetermined resolution idempotency key rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Takes in: ACCEPTED — A repeated Undetermined resolution request. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Does: ACCEPTED — {attempt_id, resolution_sequence} [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Gives out: ACCEPTED — Canonical identity: {attempt_id, resolution_sequence} [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass this canonical identity by changing a retry’s key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — {attempt_id, resolution_sequence} [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.10 — Evaluation idempotency keys | A repeated Undetermined resolution request. | {attempt_id, resolution_sequence} | Canonical identity: {attempt_id, resolution_sequence} | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.10.9 — Run terminal idempotency key
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Run terminal idempotency key rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Takes in: ACCEPTED — A repeated Run terminal request. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Does: ACCEPTED — run ID [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Gives out: ACCEPTED — Canonical identity: run ID [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass this canonical identity by changing a retry’s key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — run ID [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.10 — Evaluation idempotency keys | A repeated Run terminal request. | run ID | Canonical identity: run ID | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.10.10 — Judgment idempotency key
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Judgment idempotency key rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Takes in: ACCEPTED — A repeated Judgment request. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Does: ACCEPTED — E9 identity {judgment_chain_key, expected_previous_judgment_head, content digest}; identical re-submission absorbs; at most one committed successor per predecessor (CAS-3) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Gives out: ACCEPTED — Canonical identity: E9 identity {judgment_chain_key, expected_previous_judgment_head, content digest}; identical re-submission absorbs; at most one committed successor per predecessor (CAS-3) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass this canonical identity by changing a retry’s key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fails closed by: ACCEPTED — E9 identity {judgment_chain_key, expected_previous_judgment_head, content digest}; identical re-submission absorbs; at most one committed successor per predecessor (CAS-3) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — E9 identity {judgment_chain_key, expected_previous_judgment_head, content digest}; identical re-submission absorbs; at most one committed successor per predecessor (CAS-3) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.10 — Evaluation idempotency keys | A repeated Judgment request. | E9 identity {judgment_chain_key, expected_previous_judgment_head, content digest}; identical re-submission absorbs; at most one committed successor per predecessor (CAS-3) | Canonical identity: E9 identity {judgment_chain_key, expected_previous_judgment_head, content digest}; identical re-submission absorbs; at most one committed successor per predecessor (CAS-3) | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.10.11 — O-APPEND idempotency key
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-APPEND idempotency key rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Takes in: ACCEPTED — A repeated O-APPEND request. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Does: ACCEPTED — its own operation ID; the requested record's own idempotency key is the canonical key B9 groups on [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Gives out: ACCEPTED — Canonical identity: its own operation ID; the requested record's own idempotency key is the canonical key B9 groups on [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass this canonical identity by changing a retry’s key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A lost ledger race ends this operation once; only a new B9-admitted O-APPEND with unchanged record key/content may continue. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — its own operation ID; the requested record's own idempotency key is the canonical key B9 groups on [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.10 — Evaluation idempotency keys | A repeated O-APPEND request. | its own operation ID; the requested record's own idempotency key is the canonical key B9 groups on | Canonical identity: its own operation ID; the requested record's own idempotency key is the canonical key B9 groups on | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.10.12 — Ledger entry idempotency key
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Ledger entry idempotency key rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Takes in: ACCEPTED — A repeated Ledger entry request. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Does: ACCEPTED — {scope, sequence_number} — CAS-1 [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Gives out: ACCEPTED — Canonical identity: {scope, sequence_number} — CAS-1 [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass this canonical identity by changing a retry’s key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A losing ledger compare-and-append commits nothing and ends lost_race_technical. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — {scope, sequence_number} — CAS-1 [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.10 — Evaluation idempotency keys | A repeated Ledger entry request. | {scope, sequence_number} — CAS-1 | Canonical identity: {scope, sequence_number} — CAS-1 | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.10.13 — Aggregate idempotency key
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Aggregate idempotency key rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Takes in: ACCEPTED — A repeated Aggregate request. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Does: ACCEPTED — {run, expected_previous_head, terminal-set digest, E7r digest, judgment-set digest} — CAS-2 [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Gives out: ACCEPTED — Canonical identity: {run, expected_previous_head, terminal-set digest, E7r digest, judgment-set digest} — CAS-2 [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass this canonical identity by changing a retry’s key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Identical content absorbs; stale expected head refuses; fork or same-key different content is indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — {run, expected_previous_head, terminal-set digest, E7r digest, judgment-set digest} — CAS-2 [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.10 — Evaluation idempotency keys | A repeated Aggregate request. | {run, expected_previous_head, terminal-set digest, E7r digest, judgment-set digest} — CAS-2 | Canonical identity: {run, expected_previous_head, terminal-set digest, E7r digest, judgment-set digest} — CAS-2 | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.10.14 — Results idempotency key
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Results idempotency key rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Takes in: ACCEPTED — A repeated Results request. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Does: ACCEPTED — DET-1 identity [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Gives out: ACCEPTED — Canonical identity: DET-1 identity [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass this canonical identity by changing a retry’s key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Same identity and content absorbs; different content under one identity is result_contradiction and unusable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — DET-1 identity [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.10 — Evaluation idempotency keys | A repeated Results request. | DET-1 identity | Canonical identity: DET-1 identity | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.10.15 — E13 / E14 / E15 / logs idempotency key
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The E13 / E14 / E15 / logs idempotency key rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Takes in: ACCEPTED — A repeated E13 / E14 / E15 / logs request. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Does: ACCEPTED — result + kind / excluded run / affected-run set / operation ID [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Gives out: ACCEPTED — Canonical identity: result + kind / excluded run / affected-run set / operation ID [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Must never: ACCEPTED — Bypass this canonical identity by changing a retry’s key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — result + kind / excluded run / affected-run set / operation ID [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.10 — Evaluation idempotency keys | A repeated E13 / E14 / E15 / logs request. | result + kind / excluded run / affected-run set / operation ID | Canonical identity: result + kind / excluded run / affected-run set / operation ID | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.8] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.11 — Unresolved-attempt resolution semantics
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — Append-only E7r lookup resolution of immutable attempt_unresolved E7. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — Output presence/absence evidence, planned_trial_output_key and integrity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — Derives effective attempt and run states without rewriting E7/E8; permits at most one conclusive E7r. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — Found, proven-absent or still-undetermined outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Retry while existence is unknown, start after E8 or rewrite prior terminal records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Conflicting conclusive outcomes are indeterminate; unresolved existence blocks all new attempts for the trial. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.11.1 — resolved_output_found resolution: Appends E7r and advances the ledger head; effective attempt is completed. terminal_success; retries absorb. Once judged, the trial counts as covered; aggregate head is stale and a new E10 over frozen set + E7r may use it. Before E8 the run may complete; after E8 that record remains unchanged and effective run state may be completed if every unresolved attempt is now found. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.11.2 — resolved_absence_proven resolution: Appends E7r and advances the ledger head; effective attempt is interrupted/abandoned. technical_retryable; B9 consumes E7r as the durable outcome. Trial remains uncovered unless another attempt completes. Before E8 a further attempt requires B9 admission; after E8 no attempt may start and effective run state is incomplete, absent an already accepted objective-invalidity route; none exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.11.3 — still_undetermined resolution: Appends E7r and advances the ledger head; effective attempt is unresolved. indeterminate; never retried. Run aggregate head is indeterminate. Cannot become completed; before E8, closure is permitted only as run_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.11.4 — One conclusive resolution per attempt: Allows at most one resolved_output_found or resolved_absence_proven; further still-undetermined resolutions use their sequence identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.11.4 — One conclusive resolution per attempt: At most one conclusive E7r exists; contradictory resolution stays indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5 — Evaluation operations and trial execution | Output presence/absence evidence, planned_trial_output_key and integrity. | Derives effective attempt and run states without rewriting E7/E8; permits at most one conclusive E7r. | Found, proven-absent or still-undetermined outcome. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.12.5 — CR-5 — E6, existence undeterminable | Output presence/absence evidence, planned_trial_output_key and integrity. | Recovery follows this rule: Derives effective attempt and run states without rewriting E7/E8; permits at most one conclusive E7r. | Found, proven-absent or still-undetermined outcome. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.2.4 — O-ATTEMPT | Output presence/absence evidence, planned_trial_output_key and integrity. | If an earlier attempt is unresolved: Derives effective attempt and run states without rewriting E7/E8; permits at most one conclusive E7r. | Found, proven-absent or still-undetermined outcome. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.2.5 — O-RESOLVE-ATTEMPT | Output presence/absence evidence, planned_trial_output_key and integrity. | Derives effective attempt and run states without rewriting E7/E8; permits at most one conclusive E7r. | Found, proven-absent or still-undetermined outcome. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.5.9.4 — EB-4 — Attempt start | Output presence/absence evidence, planned_trial_output_key and integrity. | No start while any attempt of this planned trial has unresolved output existence. | Found, proven-absent or still-undetermined outcome. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.5.6.4 — attempt_unresolved B9 routing | Output presence/absence evidence, planned_trial_output_key and integrity. | Existence must be resolved by lookup before retry can be considered. | Found, proven-absent or still-undetermined outcome. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.11.1 — resolved_output_found resolution; C-GOLD.1.5.11.2 — resolved_absence_proven resolution; C-GOLD.1.5.11.3 — still_undetermined resolution; C-GOLD.1.5.11.4 — One conclusive resolution per attempt

### C-GOLD.1.5.11.1 — resolved_output_found resolution
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The resolved_output_found resolution rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — Output found under verified planned_trial_output_key identity and integrity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — Appends E7r and advances the ledger head; effective attempt is completed. terminal_success; retries absorb. Once judged, the trial counts as covered; aggregate head is stale and a new E10 over frozen set + E7r may use it. Before E8 the run may complete; after E8 that record remains unchanged and effective run state may be completed if every unresolved attempt is now found. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — The derived effective state and advanced ledger head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite E7/E8 or start while existence is unknown or after E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Conflicting conclusive evidence is indeterminate; the outcome’s stated execution block remains enforced. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.11.1.1 — resolved_output_found Effective attempt state: completed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.11.1.2 — resolved_output_found B9 routing: terminal_success; retries absorb. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.11.1.3 — resolved_output_found Aggregate consequence: Once judged, the trial counts as covered; aggregate head is stale and a new E10 over frozen set + E7r may use it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.11.1.4 — resolved_output_found Ledger consequence: Appends E7r; scope head advances. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.11.1.5 — resolved_output_found Run consequence: Before E8 the run may complete; after E8 that record remains unchanged and effective run state may be completed if every unresolved attempt is now found. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.8 — trial_attempt_resolution (E7r): The E7r outcome supplies the append-only resolution record; E7 remains unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.3.6 — No attempt after run terminal: No new attempt may start after E8 even when later lookup proves absence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.11.4 — One conclusive resolution per attempt: The conclusive-outcome uniqueness rule and contradiction handling apply. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.8 — trial_attempt_resolution (E7r): Appends this resolution without rewriting E7 or E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.4.2 — Scope ledger head: Its E7r ledger append advances the scope head; previous results are no longer current. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.11 — Unresolved-attempt resolution semantics | Output found under verified planned_trial_output_key identity and integrity. | Appends E7r and advances the ledger head; effective attempt is completed. terminal_success; retries absorb. Once judged, the trial counts as covered; aggregate head is stale and a new E10 over frozen set + E7r may use it. Before E8 the run may complete; after E8 that record remains unchanged and effective run state may be completed if every unresolved attempt is now found. | The derived effective state and advanced ledger head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.12.19 — CR-19 — Output found after E8 | Output found under verified planned_trial_output_key identity and integrity. | Recovery follows this rule: Appends E7r and advances the ledger head; effective attempt is completed. terminal_success; retries absorb. Once judged, the trial counts as covered; aggregate head is stale and a new E10 over frozen set + E7r may use it. Before E8 the run may complete; after E8 that record remains unchanged and effective run state may be completed if every unresolved attempt is now found. | The derived effective state and advanced ledger head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.11.1.1 — resolved_output_found Effective attempt state; C-GOLD.1.5.11.1.2 — resolved_output_found B9 routing; C-GOLD.1.5.11.1.3 — resolved_output_found Aggregate consequence; C-GOLD.1.5.11.1.4 — resolved_output_found Ledger consequence; C-GOLD.1.5.11.1.5 — resolved_output_found Run consequence

### C-GOLD.1.5.11.1.1 — resolved_output_found Effective attempt state
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The resolved_output_found Effective attempt state rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — resolved_output_found E7r. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — completed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated effective attempt state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite the original E7 or E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — This consequence applies to resolved_output_found; only lookup evidence may establish that E7r outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.11.1 — resolved_output_found resolution | resolved_output_found E7r. | completed. | The stated effective attempt state. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.11.1.2 — resolved_output_found B9 routing
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The resolved_output_found B9 routing rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — resolved_output_found E7r. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — terminal_success; retries absorb. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated b9 routing. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite the original E7 or E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Retry is absorbed under terminal_success; the found output is not regenerated. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — This consequence applies to resolved_output_found; only lookup evidence may establish that E7r outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.11.1 — resolved_output_found resolution | resolved_output_found E7r. | terminal_success; retries absorb. | The stated b9 routing. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.11.1.3 — resolved_output_found Aggregate consequence
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The resolved_output_found Aggregate consequence rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — resolved_output_found E7r. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — Once judged, the trial counts as covered; aggregate head is stale and a new E10 over frozen set + E7r may use it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated aggregate consequence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite the original E7 or E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The old aggregate head is stale; a new E10 over the frozen set plus E7r is required. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — This consequence applies to resolved_output_found; only lookup evidence may establish that E7r outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.11.1 — resolved_output_found resolution | resolved_output_found E7r. | Once judged, the trial counts as covered; aggregate head is stale and a new E10 over frozen set + E7r may use it. | The stated aggregate consequence. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.11.1.4 — resolved_output_found Ledger consequence
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The resolved_output_found Ledger consequence rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — resolved_output_found E7r. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — Appends E7r; scope head advances. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated ledger consequence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite the original E7 or E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — This consequence applies to resolved_output_found; only lookup evidence may establish that E7r outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.4.2 — Scope ledger head: The E7r append advances the ledger head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.11.1 — resolved_output_found resolution | resolved_output_found E7r. | Appends E7r; scope head advances. | The stated ledger consequence. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.11.1.5 — resolved_output_found Run consequence
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The resolved_output_found Run consequence rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — resolved_output_found E7r. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — Before E8 the run may complete; after E8 that record remains unchanged and effective run state may be completed if every unresolved attempt is now found. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated run consequence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite the original E7 or E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — E8 stays unchanged; effective completion is available only when every unresolved attempt is now found, and a new aggregate is required. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — This consequence applies to resolved_output_found; only lookup evidence may establish that E7r outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.11.1 — resolved_output_found resolution | resolved_output_found E7r. | Before E8 the run may complete; after E8 that record remains unchanged and effective run state may be completed if every unresolved attempt is now found. | The stated run consequence. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.11.2 — resolved_absence_proven resolution
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The resolved_absence_proven resolution rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — Durable lookup proves output absence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — Appends E7r and advances the ledger head; effective attempt is interrupted/abandoned. technical_retryable; B9 consumes E7r as the durable outcome. Trial remains uncovered unless another attempt completes. Before E8 a further attempt requires B9 admission; after E8 no attempt may start and effective run state is incomplete, absent an already accepted objective-invalidity route; none exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — The derived effective state and advanced ledger head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite E7/E8 or start while existence is unknown or after E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Conflicting conclusive evidence is indeterminate; the outcome’s stated execution block remains enforced. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.11.2.1 — resolved_absence_proven Effective attempt state: interrupted/abandoned. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.11.2.2 — resolved_absence_proven B9 routing: technical_retryable; B9 consumes E7r as the durable outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.11.2.3 — resolved_absence_proven Aggregate consequence: Trial remains uncovered unless another attempt completes. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.11.2.4 — resolved_absence_proven Ledger consequence: Appends E7r; scope head advances. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.11.2.5 — resolved_absence_proven Run consequence: Before E8 a further attempt requires B9 admission; after E8 no attempt may start and effective run state is incomplete, absent an already accepted objective-invalidity route; none exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.8 — trial_attempt_resolution (E7r): The E7r outcome supplies the append-only resolution record; E7 remains unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.3.6 — No attempt after run terminal: No new attempt may start after E8 even when later lookup proves absence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.11.4 — One conclusive resolution per attempt: The conclusive-outcome uniqueness rule and contradiction handling apply. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.8 — trial_attempt_resolution (E7r): Appends this resolution without rewriting E7 or E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.4.2 — Scope ledger head: Its E7r ledger append advances the scope head; previous results are no longer current. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.11 — Unresolved-attempt resolution semantics | Durable lookup proves output absence. | Appends E7r and advances the ledger head; effective attempt is interrupted/abandoned. technical_retryable; B9 consumes E7r as the durable outcome. Trial remains uncovered unless another attempt completes. Before E8 a further attempt requires B9 admission; after E8 no attempt may start and effective run state is incomplete, absent an already accepted objective-invalidity route; none exists. | The derived effective state and advanced ledger head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.12.18 — CR-18 — Absence proven after E8 | Durable lookup proves output absence. | Recovery follows this rule: Appends E7r and advances the ledger head; effective attempt is interrupted/abandoned. technical_retryable; B9 consumes E7r as the durable outcome. Trial remains uncovered unless another attempt completes. Before E8 a further attempt requires B9 admission; after E8 no attempt may start and effective run state is incomplete, absent an already accepted objective-invalidity route; none exists. | The derived effective state and advanced ledger head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.11.2.1 — resolved_absence_proven Effective attempt state; C-GOLD.1.5.11.2.2 — resolved_absence_proven B9 routing; C-GOLD.1.5.11.2.3 — resolved_absence_proven Aggregate consequence; C-GOLD.1.5.11.2.4 — resolved_absence_proven Ledger consequence; C-GOLD.1.5.11.2.5 — resolved_absence_proven Run consequence

### C-GOLD.1.5.11.2.1 — resolved_absence_proven Effective attempt state
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The resolved_absence_proven Effective attempt state rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — resolved_absence_proven E7r. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — interrupted/abandoned. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated effective attempt state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite the original E7 or E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The trial remains uncovered unless another attempt completes; before E8 only B9 may admit it, after E8 no attempt may start. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — This consequence applies to resolved_absence_proven; only lookup evidence may establish that E7r outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.11.2 — resolved_absence_proven resolution | resolved_absence_proven E7r. | interrupted/abandoned. | The stated effective attempt state. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.11.2.2 — resolved_absence_proven B9 routing
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The resolved_absence_proven B9 routing rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — resolved_absence_proven E7r. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — technical_retryable; B9 consumes E7r as the durable outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated b9 routing. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite the original E7 or E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The trial remains uncovered unless another attempt completes; before E8 only B9 may admit it, after E8 no attempt may start. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — This consequence applies to resolved_absence_proven; only lookup evidence may establish that E7r outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.11.2 — resolved_absence_proven resolution | resolved_absence_proven E7r. | technical_retryable; B9 consumes E7r as the durable outcome. | The stated b9 routing. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.11.2.3 — resolved_absence_proven Aggregate consequence
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The resolved_absence_proven Aggregate consequence rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — resolved_absence_proven E7r. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — Trial remains uncovered unless another attempt completes. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated aggregate consequence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite the original E7 or E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The trial remains uncovered unless another attempt completes; before E8 only B9 may admit it, after E8 no attempt may start. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — This consequence applies to resolved_absence_proven; only lookup evidence may establish that E7r outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.11.2 — resolved_absence_proven resolution | resolved_absence_proven E7r. | Trial remains uncovered unless another attempt completes. | The stated aggregate consequence. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.11.2.4 — resolved_absence_proven Ledger consequence
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The resolved_absence_proven Ledger consequence rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — resolved_absence_proven E7r. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — Appends E7r; scope head advances. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated ledger consequence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite the original E7 or E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The trial remains uncovered unless another attempt completes; before E8 only B9 may admit it, after E8 no attempt may start. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — This consequence applies to resolved_absence_proven; only lookup evidence may establish that E7r outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.4.2 — Scope ledger head: The E7r append advances the ledger head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.11.2 — resolved_absence_proven resolution | resolved_absence_proven E7r. | Appends E7r; scope head advances. | The stated ledger consequence. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.11.2.5 — resolved_absence_proven Run consequence
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The resolved_absence_proven Run consequence rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — resolved_absence_proven E7r. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — Before E8 a further attempt requires B9 admission; after E8 no attempt may start and effective run state is incomplete, absent an already accepted objective-invalidity route; none exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated run consequence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite the original E7 or E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The trial remains uncovered unless another attempt completes; before E8 only B9 may admit it, after E8 no attempt may start. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — This consequence applies to resolved_absence_proven; only lookup evidence may establish that E7r outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.11.2 — resolved_absence_proven resolution | resolved_absence_proven E7r. | Before E8 a further attempt requires B9 admission; after E8 no attempt may start and effective run state is incomplete, absent an already accepted objective-invalidity route; none exists. | The stated run consequence. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.11.3 — still_undetermined resolution
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The still_undetermined resolution rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — Output existence is still unprovable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — Appends E7r and advances the ledger head; effective attempt is unresolved. indeterminate; never retried. Run aggregate head is indeterminate. Cannot become completed; before E8, closure is permitted only as run_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — The derived effective state and advanced ledger head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite E7/E8 or start while existence is unknown or after E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Conflicting conclusive evidence is indeterminate; the outcome’s stated execution block remains enforced. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.11.3.1 — still_undetermined Effective attempt state: unresolved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.11.3.2 — still_undetermined B9 routing: indeterminate; never retried. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.11.3.3 — still_undetermined Aggregate consequence: Run aggregate head is indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.11.3.4 — still_undetermined Ledger consequence: Appends E7r; scope head advances. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.11.3.5 — still_undetermined Run consequence: Cannot become completed; before E8, closure is permitted only as run_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.8 — trial_attempt_resolution (E7r): The E7r outcome supplies the append-only resolution record; E7 remains unchanged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.3.6 — No attempt after run terminal: No new attempt may start after E8 even when later lookup proves absence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.11.4 — One conclusive resolution per attempt: The conclusive-outcome uniqueness rule and contradiction handling apply. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.8 — trial_attempt_resolution (E7r): Appends this resolution without rewriting E7 or E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.4.2 — Scope ledger head: Its E7r ledger append advances the scope head; previous results are no longer current. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.11 — Unresolved-attempt resolution semantics | Output existence is still unprovable. | Appends E7r and advances the ledger head; effective attempt is unresolved. indeterminate; never retried. Run aggregate head is indeterminate. Cannot become completed; before E8, closure is permitted only as run_indeterminate. | The derived effective state and advanced ledger head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.11.3.1 — still_undetermined Effective attempt state; C-GOLD.1.5.11.3.2 — still_undetermined B9 routing; C-GOLD.1.5.11.3.3 — still_undetermined Aggregate consequence; C-GOLD.1.5.11.3.4 — still_undetermined Ledger consequence; C-GOLD.1.5.11.3.5 — still_undetermined Run consequence

### C-GOLD.1.5.11.3.1 — still_undetermined Effective attempt state
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The still_undetermined Effective attempt state rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — still_undetermined E7r. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — unresolved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated effective attempt state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite the original E7 or E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The attempt remains unresolved, never retried; run head is indeterminate and cannot become completed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — This consequence applies to still_undetermined; only lookup evidence may establish that E7r outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.11.3 — still_undetermined resolution | still_undetermined E7r. | unresolved. | The stated effective attempt state. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.11.3.2 — still_undetermined B9 routing
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The still_undetermined B9 routing rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — still_undetermined E7r. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — indeterminate; never retried. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated b9 routing. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite the original E7 or E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The attempt remains unresolved, never retried; run head is indeterminate and cannot become completed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — This consequence applies to still_undetermined; only lookup evidence may establish that E7r outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.11.3 — still_undetermined resolution | still_undetermined E7r. | indeterminate; never retried. | The stated b9 routing. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.11.3.3 — still_undetermined Aggregate consequence
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The still_undetermined Aggregate consequence rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — still_undetermined E7r. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — Run aggregate head is indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated aggregate consequence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite the original E7 or E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The attempt remains unresolved, never retried; run head is indeterminate and cannot become completed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — This consequence applies to still_undetermined; only lookup evidence may establish that E7r outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.11.3 — still_undetermined resolution | still_undetermined E7r. | Run aggregate head is indeterminate. | The stated aggregate consequence. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.11.3.4 — still_undetermined Ledger consequence
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The still_undetermined Ledger consequence rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — still_undetermined E7r. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — Appends E7r; scope head advances. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated ledger consequence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite the original E7 or E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The attempt remains unresolved, never retried; run head is indeterminate and cannot become completed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — This consequence applies to still_undetermined; only lookup evidence may establish that E7r outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.4.2 — Scope ledger head: The E7r append advances the ledger head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.11.3 — still_undetermined resolution | still_undetermined E7r. | Appends E7r; scope head advances. | The stated ledger consequence. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.11.3.5 — still_undetermined Run consequence
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The still_undetermined Run consequence rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — still_undetermined E7r. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — Cannot become completed; before E8, closure is permitted only as run_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated run consequence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite the original E7 or E8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The attempt remains unresolved, never retried; run head is indeterminate and cannot become completed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — This consequence applies to still_undetermined; only lookup evidence may establish that E7r outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.11.3 — still_undetermined resolution | still_undetermined E7r. | Cannot become completed; before E8, closure is permitted only as run_indeterminate. | The stated run consequence. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.11.4 — One conclusive resolution per attempt
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The One conclusive resolution per attempt rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Takes in: ACCEPTED — Existing E7r history for one unresolved attempt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Does: ACCEPTED — Allows at most one resolved_output_found or resolved_absence_proven; further still-undetermined resolutions use their sequence identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Gives out: ACCEPTED — One conclusive resolution at most. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Must never: ACCEPTED — Accept a second contradictory conclusive outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Later contradiction of the conclusive outcome makes state indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.8 — trial_attempt_resolution (E7r): A conclusive E7r is permitted only for an unresolved attempt and only once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.11 — Unresolved-attempt resolution semantics | Existing E7r history for one unresolved attempt. | Allows at most one resolved_output_found or resolved_absence_proven; further still-undetermined resolutions use their sequence identity. | One conclusive resolution at most. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.12.17 — CR-17 — E7r conclusive outcomes contradict | Existing E7r history for one unresolved attempt. | Recovery follows this rule: Allows at most one resolved_output_found or resolved_absence_proven; further still-undetermined resolutions use their sequence identity. | One conclusive resolution at most. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.2.5 — O-RESOLVE-ATTEMPT | Existing E7r history for one unresolved attempt. | Allows at most one resolved_output_found or resolved_absence_proven; further still-undetermined resolutions use their sequence identity. | One conclusive resolution at most. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.3.8 — trial_attempt_resolution (E7r) | Existing E7r history for one unresolved attempt. | At most one conclusive resolution exists; contradiction makes effective state indeterminate. | One conclusive resolution at most. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.5.11 — Unresolved-attempt resolution semantics | Existing E7r history for one unresolved attempt. | At most one conclusive E7r exists; contradictory resolution stays indeterminate. | One conclusive resolution at most. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.5.11.1 — resolved_output_found resolution | Existing E7r history for one unresolved attempt. | The conclusive-outcome uniqueness rule and contradiction handling apply. | One conclusive resolution at most. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.5.11.2 — resolved_absence_proven resolution | Existing E7r history for one unresolved attempt. | The conclusive-outcome uniqueness rule and contradiction handling apply. | One conclusive resolution at most. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.5.11.3 — still_undetermined resolution | Existing E7r history for one unresolved attempt. | The conclusive-outcome uniqueness rule and contradiction handling apply. | One conclusive resolution at most. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12 — Run and concurrency recovery
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — Lookup-first recovery for run, attempt, append, aggregate and deterministic-result effects. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Durable records after interruption or contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — Finds committed effects, fills missing records/logs only from evidence, and keeps unknown effects blocked. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — Recovered evidence or preserved indeterminate/pending status. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Reinvoke a model after its output exists, guess unknown existence or duplicate recovered effects. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unreadable records give indeterminate downstream; repeated recovery is a no-op. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.12.1 — CR-1 — Crash before E5: No run [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.2 — CR-2 — E5, no attempts: Start ordinal 1 of planned trials [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.3 — CR-3 — E6, output found by key, no E7: E7 attempt_completed; never re-invoke [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.4 — CR-4 — E6, output provably absent: E7 attempt_interrupted_abandoned; further attempt only by B9 admission [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.5 — CR-5 — E6, existence undeterminable: E7 attempt_unresolved; no attempt for that trial; resolution only by E7r (§7.10) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.6 — CR-6 — B9 admission committed, no E6: Start the admitted attempt, or B9 records it abandoned [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.7 — CR-7 — B9 episode exhausted: Trial uncovered; run open (blocks pass) or closed incomplete (blocks pass in scope); continuation only via B9 real-change [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.8 — CR-8 — E7 present, attempt log absent: Append the missing log; then acknowledge [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.9 — CR-9 — All attempts terminal, none live, no E8: Commit E8 + E16; then the run log [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.10 — CR-10 — E8 present, run log absent: Append the missing log [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.11 — CR-11 — Crash inside a CAS-1 boundary: Atomic: record and entry both or neither; lookup finds which [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.12 — CR-12 — Lost CAS-1 race: That O-APPEND ends lost_race_technical (one terminal, one log); B9 may admit a new O-APPEND — new operation ID, unchanged canonical key and content; no B9 admission → nothing committed [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.13 — CR-13 — Lost CAS-2 race: Identical → absorbed; stale expected head → refused, fresh aggregate may be computed [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.14 — CR-14 — Aggregate fork or same-key different content found: Run indeterminate; both preserved [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.15 — CR-15 — Crash during E11/E12 derivation: Nothing committed; re-derivation at the same head yields the same identity and content [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.16 — CR-16 — Same-identity result with different content found: result_contradiction; neither usable; scope results indeterminate [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.17 — CR-17 — E7r conclusive outcomes contradict: indeterminate; all preserved [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.18 — CR-18 — Absence proven after E8: No attempt; effective run state incomplete [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.19 — CR-19 — Output found after E8: E8 preserved; effective state may become completed; new aggregate required [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.20 — CR-20 — Later E9 / E7r / E10 / E14 / E15: Head advances; earlier results not current [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.21 — CR-21 — Suite integrity mismatch: Every run on it indeterminate [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.22 — CR-22 — Unreadable record: indeterminate downstream [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.23 — CR-23 — Duplicate recovery: Lookup-first no-op [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.5.12.24 — CR-30 — O-APPEND exhausted under B9: The requested record is not committed; the requesting operation remains honestly open/pending with no terminal (§13.5); the run cannot close; scope result incomplete; continuation only via a new B9 episode under a consumed real-change record [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gated by: ACCEPTED — Durable lookup evidence, canonical identity and the linked recovery-rule card determine the outcome; no effect is guessed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5 — Evaluation operations and trial execution | Durable records after interruption or contradiction. | Finds committed effects, fills missing records/logs only from evidence, and keeps unknown effects blocked. | Recovered evidence or preserved indeterminate/pending status. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.2.12 — O-RECOVERY | Durable records after interruption or contradiction. | Finds committed effects, fills missing records/logs only from evidence, and keeps unknown effects blocked. | Recovered evidence or preserved indeterminate/pending status. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.5.12.1 — CR-1 — Crash before E5; C-GOLD.1.5.12.2 — CR-2 — E5, no attempts; C-GOLD.1.5.12.3 — CR-3 — E6, output found by key, no E7; C-GOLD.1.5.12.4 — CR-4 — E6, output provably absent; C-GOLD.1.5.12.5 — CR-5 — E6, existence undeterminable; C-GOLD.1.5.12.6 — CR-6 — B9 admission committed, no E6; C-GOLD.1.5.12.7 — CR-7 — B9 episode exhausted; C-GOLD.1.5.12.8 — CR-8 — E7 present, attempt log absent; C-GOLD.1.5.12.9 — CR-9 — All attempts terminal, none live, no E8; C-GOLD.1.5.12.10 — CR-10 — E8 present, run log absent; C-GOLD.1.5.12.11 — CR-11 — Crash inside a CAS-1 boundary; C-GOLD.1.5.12.12 — CR-12 — Lost CAS-1 race; C-GOLD.1.5.12.13 — CR-13 — Lost CAS-2 race; C-GOLD.1.5.12.14 — CR-14 — Aggregate fork or same-key different content found; C-GOLD.1.5.12.15 — CR-15 — Crash during E11/E12 derivation; C-GOLD.1.5.12.16 — CR-16 — Same-identity result with different content found; C-GOLD.1.5.12.17 — CR-17 — E7r conclusive outcomes contradict; C-GOLD.1.5.12.18 — CR-18 — Absence proven after E8; C-GOLD.1.5.12.19 — CR-19 — Output found after E8; C-GOLD.1.5.12.20 — CR-20 — Later E9 / E7r / E10 / E14 / E15; C-GOLD.1.5.12.21 — CR-21 — Suite integrity mismatch; C-GOLD.1.5.12.22 — CR-22 — Unreadable record; C-GOLD.1.5.12.23 — CR-23 — Duplicate recovery; C-GOLD.1.5.12.24 — CR-30 — O-APPEND exhausted under B9

### C-GOLD.1.5.12.1 — CR-1 — Crash before E5
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-1 — Crash before E5 rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Crash before E5 [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — No run [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — No run [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No run [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.5 — evaluation_run_open (E5): Recovery follows this rule: Freezes the run’s exact evidence context before execution. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | Crash before E5 | No run | No run | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.2 — CR-2 — E5, no attempts
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-2 — E5, no attempts rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — E5, no attempts [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — Start ordinal 1 of planned trials [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — Start ordinal 1 of planned trials [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Start ordinal 1 of planned trials [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.6.8 — Original execution ordinal: Recovery follows this rule: Treats ordinal 1 as original execution by reference, with no B9 admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | E5, no attempts | Start ordinal 1 of planned trials | Start ordinal 1 of planned trials | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.3 — CR-3 — E6, output found by key, no E7
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-3 — E6, output found by key, no E7 rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — E6, output found by key, no E7 [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — E7 attempt_completed; never re-invoke [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — E7 attempt_completed; never re-invoke [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — E7 attempt_completed; never re-invoke [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.5 — One output per planned trial: Recovery follows this rule: Derives planned_trial_output_key deterministically; uses it as the reading’s idempotency_key; at most one output commits. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | E6, output found by key, no E7 | E7 attempt_completed; never re-invoke | E7 attempt_completed; never re-invoke | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.4 — CR-4 — E6, output provably absent
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-4 — E6, output provably absent rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — E6, output provably absent [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — E7 attempt_interrupted_abandoned; further attempt only by B9 admission [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — E7 attempt_interrupted_abandoned; further attempt only by B9 admission [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — E7 attempt_interrupted_abandoned; further attempt only by B9 admission [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.6.7 — Committed B9 R1 admission: Recovery follows this rule: Requires committed B9 R1 admission under accepted identity, budget, gaps, deadline, one-live-attempt and real-change rules. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | E6, output provably absent | E7 attempt_interrupted_abandoned; further attempt only by B9 admission | E7 attempt_interrupted_abandoned; further attempt only by B9 admission | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.5 — CR-5 — E6, existence undeterminable
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-5 — E6, existence undeterminable rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — E6, existence undeterminable [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — E7 attempt_unresolved; no attempt for that trial; resolution only by E7r (§7.10) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — E7 attempt_unresolved; no attempt for that trial; resolution only by E7r (§7.10) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — E7 attempt_unresolved; no attempt for that trial; resolution only by E7r (§7.10) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.11 — Unresolved-attempt resolution semantics: Recovery follows this rule: Derives effective attempt and run states without rewriting E7/E8; permits at most one conclusive E7r. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | E6, existence undeterminable | E7 attempt_unresolved; no attempt for that trial; resolution only by E7r (§7.10) | E7 attempt_unresolved; no attempt for that trial; resolution only by E7r (§7.10) | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.6 — CR-6 — B9 admission committed, no E6
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-6 — B9 admission committed, no E6 rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — B9 admission committed, no E6 [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — Start the admitted attempt, or B9 records it abandoned [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — Start the admitted attempt, or B9 records it abandoned [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Start the admitted attempt, or B9 records it abandoned [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.6.7 — Committed B9 R1 admission: Recovery follows this rule: Requires committed B9 R1 admission under accepted identity, budget, gaps, deadline, one-live-attempt and real-change rules. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | B9 admission committed, no E6 | Start the admitted attempt, or B9 records it abandoned | Start the admitted attempt, or B9 records it abandoned | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.7 — CR-7 — B9 episode exhausted
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-7 — B9 episode exhausted rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — B9 episode exhausted [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — Trial uncovered; run open (blocks pass) or closed incomplete (blocks pass in scope); continuation only via B9 real-change [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — Trial uncovered; run open (blocks pass) or closed incomplete (blocks pass in scope); continuation only via B9 real-change [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Trial uncovered; run open (blocks pass) or closed incomplete (blocks pass in scope); continuation only via B9 real-change [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.6.9 — Technical episode exhaustion: Recovery follows this rule: Leaves the trial uncovered; the run remains open or closes incomplete. Continuation is only through B9 real-change admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | B9 episode exhausted | Trial uncovered; run open (blocks pass) or closed incomplete (blocks pass in scope); continuation only via B9 real-change | Trial uncovered; run open (blocks pass) or closed incomplete (blocks pass in scope); continuation only via B9 real-change | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.8 — CR-8 — E7 present, attempt log absent
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-8 — E7 present, attempt log absent rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — E7 present, attempt log absent [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — Append the missing log; then acknowledge [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — Append the missing log; then acknowledge [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Append the missing log; then acknowledge [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: Recovery follows this rule: Keeps state records separate from operational logs; emits exactly one append-only §0B log per real operation at its terminal, before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | E7 present, attempt log absent | Append the missing log; then acknowledge | Append the missing log; then acknowledge | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.9 — CR-9 — All attempts terminal, none live, no E8
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-9 — All attempts terminal, none live, no E8 rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — All attempts terminal, none live, no E8 [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — Commit E8 + E16; then the run log [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — Commit E8 + E16; then the run log [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Commit E8 + E16; then the run log [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.3 — Run closing conditions: Recovery follows this rule: Allows E8 only after all started attempts have a terminal and no planned-trial attempt is live or admitted-unstarted. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | All attempts terminal, none live, no E8 | Commit E8 + E16; then the run log | Commit E8 + E16; then the run log | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.10 — CR-10 — E8 present, run log absent
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-10 — E8 present, run log absent rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — E8 present, run log absent [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — Append the missing log [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — Append the missing log [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Append the missing log [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.1 — Canonical records and operation-owned logs: Recovery follows this rule: Keeps state records separate from operational logs; emits exactly one append-only §0B log per real operation at its terminal, before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.1] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | E8 present, run log absent | Append the missing log | Append the missing log | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.11 — CR-11 — Crash inside a CAS-1 boundary
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-11 — Crash inside a CAS-1 boundary rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Crash inside a CAS-1 boundary [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — Atomic: record and entry both or neither; lookup finds which [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — Atomic: record and entry both or neither; lookup finds which [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Atomic: record and entry both or neither; lookup finds which [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append: Recovery follows this rule: Commits the record and E16 together only if the current head is exactly {n,d} and domain preconditions hold; the new entry uses n+1 and previous_entry_digest=d. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | Crash inside a CAS-1 boundary | Atomic: record and entry both or neither; lookup finds which | Atomic: record and entry both or neither; lookup finds which | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.12 — CR-12 — Lost CAS-1 race
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-12 — Lost CAS-1 race rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Lost CAS-1 race [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — That O-APPEND ends lost_race_technical (one terminal, one log); B9 may admit a new O-APPEND — new operation ID, unchanged canonical key and content; no B9 admission → nothing committed [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — That O-APPEND ends lost_race_technical (one terminal, one log); B9 may admit a new O-APPEND — new operation ID, unchanged canonical key and content; no B9 admission → nothing committed [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — That O-APPEND ends lost_race_technical (one terminal, one log); B9 may admit a new O-APPEND — new operation ID, unchanged canonical key and content; no B9 admission → nothing committed [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append: Recovery follows this rule: Commits the record and E16 together only if the current head is exactly {n,d} and domain preconditions hold; the new entry uses n+1 and previous_entry_digest=d. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | Lost CAS-1 race | That O-APPEND ends lost_race_technical (one terminal, one log); B9 may admit a new O-APPEND — new operation ID, unchanged canonical key and content; no B9 admission → nothing committed | That O-APPEND ends lost_race_technical (one terminal, one log); B9 may admit a new O-APPEND — new operation ID, unchanged canonical key and content; no B9 admission → nothing committed | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.13 — CR-13 — Lost CAS-2 race
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-13 — Lost CAS-2 race rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Lost CAS-2 race [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — Identical → absorbed; stale expected head → refused, fresh aggregate may be computed [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — Identical → absorbed; stale expected head → refused, fresh aggregate may be computed [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Identical → absorbed; stale expected head → refused, fresh aggregate may be computed [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.8.2 — CAS-2 aggregate-head compare-and-replace: Recovery follows this rule: Commits only if expected_previous_head remains current; identical key/content absorbs. A stale predecessor refuses, allowing a fresh aggregate from new state as a new operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | Lost CAS-2 race | Identical → absorbed; stale expected head → refused, fresh aggregate may be computed | Identical → absorbed; stale expected head → refused, fresh aggregate may be computed | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.14 — CR-14 — Aggregate fork or same-key different content found
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-14 — Aggregate fork or same-key different content found rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Aggregate fork or same-key different content found [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — Run indeterminate; both preserved [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — Run indeterminate; both preserved [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Run indeterminate; both preserved [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.8.2 — CAS-2 aggregate-head compare-and-replace: Recovery follows this rule: Commits only if expected_previous_head remains current; identical key/content absorbs. A stale predecessor refuses, allowing a fresh aggregate from new state as a new operation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | Aggregate fork or same-key different content found | Run indeterminate; both preserved | Run indeterminate; both preserved | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.15 — CR-15 — Crash during E11/E12 derivation
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-15 — Crash during E11/E12 derivation rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Crash during E11/E12 derivation [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — Nothing committed; re-derivation at the same head yields the same identity and content [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — Nothing committed; re-derivation at the same head yields the same identity and content [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Nothing committed; re-derivation at the same head yields the same identity and content [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.8.3 — DET-1 deterministic result identity: Recovery follows this rule: Pure derivation from that ledger state produces identical identity/content; repeated identical commitment absorbs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | Crash during E11/E12 derivation | Nothing committed; re-derivation at the same head yields the same identity and content | Nothing committed; re-derivation at the same head yields the same identity and content | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.16 — CR-16 — Same-identity result with different content found
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-16 — Same-identity result with different content found rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Same-identity result with different content found [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — result_contradiction; neither usable; scope results indeterminate [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — result_contradiction; neither usable; scope results indeterminate [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — result_contradiction; neither usable; scope results indeterminate [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.8.3 — DET-1 deterministic result identity: Recovery follows this rule: Pure derivation from that ledger state produces identical identity/content; repeated identical commitment absorbs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | Same-identity result with different content found | result_contradiction; neither usable; scope results indeterminate | result_contradiction; neither usable; scope results indeterminate | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.17 — CR-17 — E7r conclusive outcomes contradict
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-17 — E7r conclusive outcomes contradict rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — E7r conclusive outcomes contradict [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — indeterminate; all preserved [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — indeterminate; all preserved [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — indeterminate; all preserved [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.11.4 — One conclusive resolution per attempt: Recovery follows this rule: Allows at most one resolved_output_found or resolved_absence_proven; further still-undetermined resolutions use their sequence identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | E7r conclusive outcomes contradict | indeterminate; all preserved | indeterminate; all preserved | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.18 — CR-18 — Absence proven after E8
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-18 — Absence proven after E8 rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Absence proven after E8 [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — No attempt; effective run state incomplete [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — No attempt; effective run state incomplete [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No attempt; effective run state incomplete [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.11.2 — resolved_absence_proven resolution: Recovery follows this rule: Appends E7r and advances the ledger head; effective attempt is interrupted/abandoned. technical_retryable; B9 consumes E7r as the durable outcome. Trial remains uncovered unless another attempt completes. Before E8 a further attempt requires B9 admission; after E8 no attempt may start and effective run state is incomplete, absent an already accepted objective-invalidity route; none exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | Absence proven after E8 | No attempt; effective run state incomplete | No attempt; effective run state incomplete | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.19 — CR-19 — Output found after E8
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-19 — Output found after E8 rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Output found after E8 [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — E8 preserved; effective state may become completed; new aggregate required [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — E8 preserved; effective state may become completed; new aggregate required [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — E8 preserved; effective state may become completed; new aggregate required [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.11.1 — resolved_output_found resolution: Recovery follows this rule: Appends E7r and advances the ledger head; effective attempt is completed. terminal_success; retries absorb. Once judged, the trial counts as covered; aggregate head is stale and a new E10 over frozen set + E7r may use it. Before E8 the run may complete; after E8 that record remains unchanged and effective run state may be completed if every unresolved attempt is now found. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | Output found after E8 | E8 preserved; effective state may become completed; new aggregate required | E8 preserved; effective state may become completed; new aggregate required | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.20 — CR-20 — Later E9 / E7r / E10 / E14 / E15
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-20 — Later E9 / E7r / E10 / E14 / E15 rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Later E9 / E7r / E10 / E14 / E15 [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — Head advances; earlier results not current [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — Head advances; earlier results not current [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Head advances; earlier results not current [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.4.3 — Authoritative current result: Recovery follows this rule: Counts as current only when its bound head equals the ledger’s current head and its epoch is current; later relevant records stale earlier results for new checks. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | Later E9 / E7r / E10 / E14 / E15 | Head advances; earlier results not current | Head advances; earlier results not current | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.21 — CR-21 — Suite integrity mismatch
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-21 — Suite integrity mismatch rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Suite integrity mismatch [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — Every run on it indeterminate [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — Every run on it indeterminate [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Every run on it indeterminate [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.2 — evaluation_suite_manifest (E1): Recovery follows this rule: Registers only after integrity, seal and acceptance checks; benchmark suites additionally require an accepted concrete suite; held-out requires its accepted policy. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | Suite integrity mismatch | Every run on it indeterminate | Every run on it indeterminate | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.22 — CR-22 — Unreadable record
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-22 — Unreadable record rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Unreadable record [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — indeterminate downstream [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — indeterminate downstream [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — indeterminate downstream [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: Recovery follows this rule: Keeps it immutable and append-only; corrections append new linked records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | Unreadable record | indeterminate downstream | indeterminate downstream | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.23 — CR-23 — Duplicate recovery
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-23 — Duplicate recovery rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Duplicate recovery [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — Lookup-first no-op [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — Lookup-first no-op [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Lookup-first no-op [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.2.12 — O-RECOVERY: Recovery follows this rule: Uses lookup-first recovery; repeated resolved work is a no-op. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | Duplicate recovery | Lookup-first no-op | Lookup-first no-op | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.12.24 — CR-30 — O-APPEND exhausted under B9
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-30 — O-APPEND exhausted under B9 rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — O-APPEND exhausted under B9 [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — The requested record is not committed; the requesting operation remains honestly open/pending with no terminal (§13.5); the run cannot close; scope result incomplete; continuation only via a new B9 episode under a consumed real-change record [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — The requested record is not committed; the requesting operation remains honestly open/pending with no terminal (§13.5); the run cannot close; scope result incomplete; continuation only via a new B9 episode under a consumed real-change record [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Guess an effect or duplicate a canonical record during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The requested record is not committed; the requesting operation remains honestly open/pending with no terminal (§13.5); the run cannot close; scope result incomplete; continuation only via a new B9 episode under a consumed real-change record [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.13 — Requesting operation after append exhaustion: A requester whose record has not committed remains pending; its run cannot close and continuation requires B9 real-change. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5.12 — Run and concurrency recovery | O-APPEND exhausted under B9 | The requested record is not committed; the requesting operation remains honestly open/pending with no terminal (§13.5); the run cannot close; scope result incomplete; continuation only via a new B9 episode under a consumed real-change record | The requested record is not committed; the requesting operation remains honestly open/pending with no terminal (§13.5); the run cannot close; scope result incomplete; continuation only via a new B9 episode under a consumed real-change record | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.5.13 — Requesting operation after append exhaustion
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Requesting operation after append exhaustion rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — Every admitted O-APPEND ended lost_race_technical and B9 exhausted or early-stopped the episode. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Keeps the requesting domain operation honestly open/pending with no terminal because its record has not committed; B9 records the stopping gate and preserved state. Only a new B9 episode with consumed real-change and unchanged inputs may continue. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — Pending operation, run unable to close, scope result incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Invent a domain exhausted terminal, false completion, hidden retry or second terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No record commit means no requester terminal; run cannot close and evidence remains incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.6.7 — Committed B9 R1 admission: Continuation requires a new B9 episode, consumed real-change and unchanged canonical inputs. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.5 — Evaluation operations and trial execution | Every admitted O-APPEND ended lost_race_technical and B9 exhausted or early-stopped the episode. | Keeps the requesting domain operation honestly open/pending with no terminal because its record has not committed; B9 records the stopping gate and preserved state. Only a new B9 episode with consumed real-change and unchanged inputs may continue. | Pending operation, run unable to close, scope result incomplete. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.2.13 — O-APPEND | Every admitted O-APPEND ended lost_race_technical and B9 exhausted or early-stopped the episode. | Keeps the requesting domain operation honestly open/pending with no terminal because its record has not committed; B9 records the stopping gate and preserved state. Only a new B9 episode with consumed real-change and unchanged inputs may continue. | Pending operation, run unable to close, scope result incomplete. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.5.3 — Run closing conditions | Every admitted O-APPEND ended lost_race_technical and B9 exhausted or early-stopped the episode. | An operation still pending after append exhaustion prevents the required closing record or completed attempt from being claimed. | Pending operation, run unable to close, scope result incomplete. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.12.24 — CR-30 — O-APPEND exhausted under B9 | Every admitted O-APPEND ended lost_race_technical and B9 exhausted or early-stopped the episode. | A requester whose record has not committed remains pending; its run cannot close and continuation requires B9 real-change. | Pending operation, run unable to close, scope result incomplete. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

<!-- END CHAPTER 3-f BEHAVIOR -->

## Continuation and reciprocal entries

These entries are recorded in this piece. Every passed chapter remains unchanged. A rule in the other new piece is named by its exact card; its USED BY row appears in that piece.

| Existing owner / endpoint | New counterpart | Relation | Behavior | Source |
|---|---|---|---|---|

### Cross-piece relationships

| Using card | Defining/supplying card | Relation | Source |
|---|---|---|---|
| C-GOLD.1.5.9.1 — EB-1 — Suite registration | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.9.2 — EB-2 — Setup registration | C-GOLD.1.3.4.4 — Coverage profile registration gate | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| C-GOLD.1.5.9.3 — EB-3 — Run open | C-GOLD.1.3.5 — evaluation_run_open (E5) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB] |
| C-GOLD.1.5.9.4 — EB-4 — Attempt start | C-GOLD.1.3.6 — trial_attempt_start (E6) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.9.5 — EB-5 — Attempt terminal | C-GOLD.1.3.7 — trial_attempt_terminal (E7) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| C-GOLD.1.5.9.6 — EB-6 — Attempt resolution | C-GOLD.1.3.8 — trial_attempt_resolution (E7r) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| C-GOLD.1.5.9.8 — EB-8 — Protected judgment | C-GOLD.1.3.10 — evaluation_judgment (E9) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.5.9.11 — EB-11 — Evidence reference | C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB] |
| C-GOLD.1.5.9.12 — EB-12 — Invalidity or conflict | C-GOLD.1.3.16 — evaluation_invalidity_record (E14) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2] [NHD-B16EEB] |
| C-GOLD.1.5.9.12 — EB-12 — Invalidity or conflict | C-GOLD.1.3.17 — evaluation_conflict_resolution (E15) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [NHD-B16EEB] |
| C-GOLD.1.5.9.8.2 — Conditional BAI receipt | C-GOLD.1.3.10 — evaluation_judgment (E9) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.5.11.1 — resolved_output_found resolution | C-GOLD.1.3.8 — trial_attempt_resolution (E7r) | ACCEPTED — Fed by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| C-GOLD.1.5.11.2 — resolved_absence_proven resolution | C-GOLD.1.3.8 — trial_attempt_resolution (E7r) | ACCEPTED — Fed by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| C-GOLD.1.5.11.3 — still_undetermined resolution | C-GOLD.1.3.8 — trial_attempt_resolution (E7r) | ACCEPTED — Fed by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| C-GOLD.1.5.12.1 — CR-1 — Crash before E5 | C-GOLD.1.3.5 — evaluation_run_open (E5) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.5] [NHD-B16EEB] |
| C-GOLD.1.5.12.20 — CR-20 — Later E9 / E7r / E10 / E14 / E15 | C-GOLD.1.4.3 — Authoritative current result | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] |
| C-GOLD.1.5.12.21 — CR-21 — Suite integrity mismatch | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.12.22 — CR-22 — Unreadable record | C-GOLD.1.3.1 — Canonical record preservation | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| C-GOLD.1.5.2.1 — O-SUITE | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.2.2 — O-SETUP | C-GOLD.1.3.4.4 — Coverage profile registration gate | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [NHD-B16EEB] |
| C-GOLD.1.5.2.2 — O-SETUP | C-GOLD.1.2.3 — policy_epoch (E2e) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.3] [NHD-B16EEB] |
| C-GOLD.1.5.2.2 — O-SETUP | C-GOLD.1.2.1 — model_evaluation_profile (E4) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |
| C-GOLD.1.5.2.2 — O-SETUP | C-GOLD.1.2.2 — system_candidate_profile (E4S) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §4.1] [NHD-B16EEB] |
| C-GOLD.1.5.2.6 — O-JUDGE | C-GOLD.1.3.10 — evaluation_judgment (E9) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.5.2.7 — O-AGGREGATE | C-GOLD.1.3.11 — suite_aggregate_result (E10) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] [NHD-B16EEB] |
| C-GOLD.1.5.2.9 — O-EVREF | C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB] |
| C-GOLD.1.5.2.10 — O-INVALIDITY | C-GOLD.1.3.16 — evaluation_invalidity_record (E14) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.11 — O-CONFLICT | C-GOLD.1.3.17 — evaluation_conflict_resolution (E15) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.3] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §17] [NHD-B16EEB] |
| C-GOLD.1.5.2.4.1 — O-ATTEMPT attempt_completed | C-GOLD.1.3.7 — trial_attempt_terminal (E7) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.4.2 — O-ATTEMPT attempt_failed | C-GOLD.1.3.7 — trial_attempt_terminal (E7) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.4.3 — O-ATTEMPT attempt_interrupted_abandoned | C-GOLD.1.3.7 — trial_attempt_terminal (E7) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.4.4 — O-ATTEMPT attempt_unresolved | C-GOLD.1.3.7 — trial_attempt_terminal (E7) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.3.1 — O-RUN run_completed | C-GOLD.1.3.9 — evaluation_run_terminal (E8) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.3.2 — O-RUN run_closed_incomplete | C-GOLD.1.3.9 — evaluation_run_terminal (E8) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.3.3 — O-RUN run_indeterminate | C-GOLD.1.3.9 — evaluation_run_terminal (E8) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5 — Evaluation operations and trial execution | C-GOLD.1.3.19 — Evaluation privacy and access | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| C-GOLD.1.5.1 — Canonical records and operation-owned logs | C-GOLD.1.3.19 — Evaluation privacy and access | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| C-GOLD.1.5.2 — Operation terminal catalog | C-GOLD.1.3.19 — Evaluation privacy and access | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| C-GOLD.1.5.11.4 — One conclusive resolution per attempt | C-GOLD.1.3.8 — trial_attempt_resolution (E7r) | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| C-GOLD.1.5.2.1 — O-SUITE | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.2 — O-SETUP | C-GOLD.1.2.3 — policy_epoch (E2e) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.2 — O-SETUP | C-GOLD.1.3.4 — required_coverage_profile (E3) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.2 — O-SETUP | C-GOLD.1.2.1 — model_evaluation_profile (E4) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.2 — O-SETUP | C-GOLD.1.2.2 — system_candidate_profile (E4S) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.3 — O-RUN | C-GOLD.1.3.5 — evaluation_run_open (E5) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.3 — O-RUN | C-GOLD.1.3.9 — evaluation_run_terminal (E8) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.4 — O-ATTEMPT | C-GOLD.1.3.6 — trial_attempt_start (E6) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.4 — O-ATTEMPT | C-GOLD.1.3.7 — trial_attempt_terminal (E7) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.5 — O-RESOLVE-ATTEMPT | C-GOLD.1.3.8 — trial_attempt_resolution (E7r) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.6 — O-JUDGE | C-GOLD.1.3.10 — evaluation_judgment (E9) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.7 — O-AGGREGATE | C-GOLD.1.3.11 — suite_aggregate_result (E10) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.8 — O-RESULT | C-GOLD.1.3.12 — gold_evidence_result (E11a) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.8 — O-RESULT | C-GOLD.1.3.13 — held_out_evidence_result (E11b) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.8 — O-RESULT | C-GOLD.1.3.14 — b24_system_eligibility_result (E12) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.9 — O-EVREF | C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.10 — O-INVALIDITY | C-GOLD.1.3.16 — evaluation_invalidity_record (E14) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.2.11 — O-CONFLICT | C-GOLD.1.3.17 — evaluation_conflict_resolution (E15) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [NHD-B16EEB] |
| C-GOLD.1.5.9.1 — EB-1 — Suite registration | C-GOLD.1.3.2 — evaluation_suite_manifest (E1) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.9.2 — EB-2 — Setup registration | C-GOLD.1.2.3 — policy_epoch (E2e) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.9.2 — EB-2 — Setup registration | C-GOLD.1.3.4 — required_coverage_profile (E3) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.9.2 — EB-2 — Setup registration | C-GOLD.1.2.1 — model_evaluation_profile (E4) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.9.2 — EB-2 — Setup registration | C-GOLD.1.2.2 — system_candidate_profile (E4S) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.9.3 — EB-3 — Run open | C-GOLD.1.3.5 — evaluation_run_open (E5) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.9.4 — EB-4 — Attempt start | C-GOLD.1.3.6 — trial_attempt_start (E6) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.9.5 — EB-5 — Attempt terminal | C-GOLD.1.3.7 — trial_attempt_terminal (E7) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.9.6 — EB-6 — Attempt resolution | C-GOLD.1.3.8 — trial_attempt_resolution (E7r) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.9.7 — EB-7 — Run terminal | C-GOLD.1.3.9 — evaluation_run_terminal (E8) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.9.8 — EB-8 — Protected judgment | C-GOLD.1.3.10 — evaluation_judgment (E9) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.9.9 — EB-9 — Aggregate | C-GOLD.1.3.11 — suite_aggregate_result (E10) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.9.10 — EB-10 — Result derivation | C-GOLD.1.3.12 — gold_evidence_result (E11a) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.9.10 — EB-10 — Result derivation | C-GOLD.1.3.13 — held_out_evidence_result (E11b) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.9.10 — EB-10 — Result derivation | C-GOLD.1.3.14 — b24_system_eligibility_result (E12) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.9.11 — EB-11 — Evidence reference | C-GOLD.1.3.15 — promotion_evaluation_evidence_ref (E13) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.9.12 — EB-12 — Invalidity or conflict | C-GOLD.1.3.16 — evaluation_invalidity_record (E14) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.9.12 — EB-12 — Invalidity or conflict | C-GOLD.1.3.17 — evaluation_conflict_resolution (E15) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.7] [NHD-B16EEB] |
| C-GOLD.1.5.2.13 — O-APPEND | C-GOLD.1.3.18 — evaluation_scope_ledger_entry (E16) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append | C-GOLD.1.3.18 — evaluation_scope_ledger_entry (E16) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| C-GOLD.1.5.11.1 — resolved_output_found resolution | C-GOLD.1.3.8 — trial_attempt_resolution (E7r) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| C-GOLD.1.5.11.1 — resolved_output_found resolution | C-GOLD.1.4.2 — Scope ledger head | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] |
| C-GOLD.1.5.11.1.4 — resolved_output_found Ledger consequence | C-GOLD.1.4.2 — Scope ledger head | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| C-GOLD.1.5.11.2 — resolved_absence_proven resolution | C-GOLD.1.3.8 — trial_attempt_resolution (E7r) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| C-GOLD.1.5.11.2 — resolved_absence_proven resolution | C-GOLD.1.4.2 — Scope ledger head | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] |
| C-GOLD.1.5.11.2.4 — resolved_absence_proven Ledger consequence | C-GOLD.1.4.2 — Scope ledger head | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| C-GOLD.1.5.11.3 — still_undetermined resolution | C-GOLD.1.3.8 — trial_attempt_resolution (E7r) | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |
| C-GOLD.1.5.11.3 — still_undetermined resolution | C-GOLD.1.4.2 — Scope ledger head | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] |
| C-GOLD.1.5.11.3.4 — still_undetermined Ledger consequence | C-GOLD.1.4.2 — Scope ledger head | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.10] [NHD-B16EEB] |

## Register contributions

### NOT DECIDED register

Every empty box is listed with its source-silence reason. Known mechanics deferred to another piece are listed separately and are not open decisions.

| Part ID | Field | Value | Why retained |
|---|---|---|---|
| C-GOLD.1.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.1.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.1.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.1.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.1.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.2.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.2.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.2.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.2.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.3.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.3.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.3.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.4.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.4.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.4.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.4.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.5.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.5.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.5.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.5.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.6.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.6.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.6.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.6.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.6.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.6.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.6.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.6.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.6.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.6.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.6.6 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.6.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.6.7 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.6.7 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.6.8 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.6.8 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.7.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.7.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.7.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.7.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.7.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.7.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.8.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.8.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.8.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.8.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.8.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.8.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.9.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.9.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.9.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.9.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.10.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.10.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.10.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.10.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.11.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.11.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.11.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.11.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.12 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.12.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.12.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.12.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.12.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.13.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.13.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.13.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.13.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.13.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.13.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.2.13.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.2.13.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.3.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.3.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.3.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.3.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.3.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.3.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.3.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.3.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.3.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.3.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.3.6 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.3.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.5.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.5.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.5.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.5.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.5.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.5.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.6.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.6.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.6.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.6.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.6.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.6.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.6.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.6.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.6.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.6.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.6.6 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.6.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.6.7 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.6.7 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.6.8 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.5.6.8 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.6.8 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.6.9 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.6.9 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.6.10 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.6.10.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.6.10.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.6.10.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.6.10.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.6.10.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.6.10.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.6.10.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.6.10.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.6.10.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.6.10.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.6.10.6 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.6.10.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.6.10.7 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.6.10.7 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.6.10.8 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.5.6.10.8 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.6.10.8 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.6.10.9 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.5.6.10.9 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.6.10.9 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.6.10.10 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.6.10.10 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.7 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.7 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.8 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.8.1.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.8.1.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.8.1.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.8.1.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.8.1.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.8.1.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.8.1.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.8.1.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.8.1.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.8.1.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.8.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.8.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.8.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.8.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.8.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.8.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.9 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.9.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.9.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.9.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.9.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.9.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.9.6 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.9.7 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.9.8.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.9.8.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.9.8.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.9.8.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.9.8.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.9.8.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.9.9 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.9.10 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.9.11 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.9.12 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.10 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.5.10 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.10.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.10.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.10.2 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.5.10.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.10.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.10.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.10.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.10.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.10.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.10.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.10.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.10.6 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.5.10.6 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.10.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.10.7 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.10.7 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.10.8 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.5.10.8 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.10.8 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.10.9 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.5.10.9 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.10.9 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.10.10 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.10.10 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.10.11 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.10.11 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.10.12 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.10.12 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.10.13 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.10.13 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.10.14 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.10.14 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.10.15 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.5.10.15 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.10.15 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.11 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.11.1.1 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.5.11.1.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.11.1.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.11.1.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.11.1.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.11.1.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.11.1.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.11.1.4 | Fails closed by | NOT DECIDED | The cited section gives this member/rule no distinct failure outcome; any explicitly applicable containing-record or operation outcome is recorded where defined. |
| C-GOLD.1.5.11.1.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.11.1.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.11.1.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.11.2.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.11.2.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.11.2.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.11.2.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.11.2.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.11.2.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.11.2.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.11.2.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.11.2.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.11.3.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.11.3.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.11.3.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.11.3.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.11.3.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.11.3.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.11.3.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.11.3.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.11.3.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.11.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.11.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.1 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.1 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.2 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.2 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.3 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.3 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.4 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.4 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.5 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.5 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.6 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.6 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.7 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.7 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.8 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.8 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.9 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.9 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.10 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.10 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.11 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.11 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.12 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.12 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.13 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.13 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.14 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.14 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.15 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.15 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.16 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.16 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.17 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.17 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.18 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.18 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.19 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.19 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.20 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.20 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.21 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.21 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.22 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.22 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.23 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.23 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.12.24 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.12.24 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.13 | Fed by | NOT DECIDED | No separate supplying part is named for this atomic member/rule; its concrete inputs are recorded in Takes in. |
| C-GOLD.1.5.13 | Changes | NOT DECIDED | No separate outward state change is assigned to this field/rule by its cited section; its stated result remains in Gives out. |
| C-GOLD.1.5.8 | Physical compare-and-append implementation | NOT DECIDED | The accepted bridge leaves ledger/CAS storage mechanics, canonicalization and integrity algorithms open (§20). |

### Source-conflict and status distinctions

No conflict is resolved by this pair. B16 v1.0 §5.3 retains its input-3 phrase “the recorded B24-architecture acceptance evidence for the applicable gold-set run”; the bridge separates E11a gold evidence from E12 system eligibility. The exact bridge contract is recorded here; the old source is not edited. [SOURCE CONFLICT: 04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3 retains the earlier input-3 wording; 04/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md §7 records its pending integration.]

### Decided material not placed in this pair

- Bridge §§7.11–7.13: full judgment-chain authority, conditional proof lifecycles, claim fields/states/transitions and their protected recovery; only the record contract, terminal catalog and EB-8 interface are present here.
- Bridge §8–§9: complete result-state precedence and per-reading AP-1…AP-12 applicability cards; this pair records the reference and currentness contracts only.
- Bridge §10, §13.1 CR-24…CR-29 and CR-31…CR-40, and §14: remaining judgment-specific invariants, recovery and failure matrix; they are known accepted material, not undecided.
- Bridge §16–§17: full dependency matrix and all seventeen policy slots; the values remain open, while their accepted slot definitions await full placement.
- Remaining Group A engines, index, sealed-gold foundation/story-gold package, ingest and detector remain for later pieces. No completion of those components is claimed.

## Coverage matrix — cumulative contribution

### File coverage

| Row | Source | Read scope | Placement |
|---|---|---|---|
| F001 | `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained; Chapter 3-c scoped reread: status table, §0/0A/0B, reading schema, §7G-A RC sequence and §7K; Chapter 3-d focused status-table, §0B and §§6A/6B checks | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.1; C-STORE.2; C-STORE.3; CY-A Chapter 3-b: C-READ and its v1 record, validator, writer, quarantine, production-boundary and operation-record sub-parts; CY-A/CY-F reading-write interfaces. Chapter 3-c: governing checks for C-READ.10; A2/firmness additions stay ACCEPTED, never BUILT. Chapter 3-d: source-status and no-production-write boundaries; governing operational living-memory rule at C-READ.11.9.4. |
| F002 | `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained; Chapter 3-c focused rule/boundary searches and excerpts, no new whole-read claim | EXCLUDED: interaction/workflow guidance under §1.3 and §2.4. NOT PLACED: remaining behavior belongs to other component groups.; Chapter 3-a: C-STORE.2.3 Chapter 3-b: C-READ.1 confidence semantics and C-READ.2 uncertainty-preserving shape gate; remaining scope retained. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. |
| F003 | `01_AUTHORITATIVE/cursorrules` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained; Chapter 3-c focused rule/boundary searches and excerpts, no new whole-read claim | EXCLUDED: coding-process rules under §1.3. NOT PLACED: built-code boundaries belong to store, reader and code-boundary groups. Chapter 3-b: C-READ.1.12 per-store/global-key conflict and C-READ.3 shared write boundary; workflow remains excluded. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. |
| F004 | `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; Chapter 3-c focused rule/boundary searches and excerpts, no new whole-read claim | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. |
| F005 | `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained; Chapter 3-c C-READ/C-7K and adjacent interfaces searched/reopened; Chapter 3-d C-READ and CY-G/B16 owner checks | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.3.4; CY-A Chapter 3-b: C-READ component name, operation logging and consumer/caller relationships; CY-A/CY-F interfaces. Chapter 3-c: component ownership/names and Group A/D boundary; accepted A2 supplies behavior. Chapter 3-d: names, Group A ownership and per-reading seam versus full CY-G boundary. |
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
| F036 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md` | Newly read whole in Chapter 3-c; exact pinned Git blob verified | C-READ.10 and all A2-cited descendants: §§1–10 identity, card/preparation/event ownership, acceptance/correspondence, commit/recovery, legacy mapping, lifecycle, semantic/safety boundaries, references/rereading and logging. EXCLUDED: source revision history, acts of acceptance, implementation workflow and self-audit claims under §1.3. Other consumer mechanics remain with their owning groups.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards. |
| F037 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_PACKAGE_COMPLETE_RECORD_v1_0.md` | Newly read whole in Chapter 3-c; exact pinned Git blob verified | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt. |
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
| F052 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole read for Chapter 3-e/3-f; exact blob verified at 6a7160b. | Status/identity checked for NHD-B16EEB; globally unique slot identifiers retained; acceptance narrative EXCLUDED by §1.3 |
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
| F099 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Newly read whole in Chapter 3-c; exact pinned Git blob verified | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt. |
| F100 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md` | Newly read whole in Chapter 3-c; exact pinned Git blob verified | C-READ.10.1.11; C-READ.10.1.12 and all firmness-policy-cited descendants: §§1–6 qualitative outcomes, evidence basis, separations, revision and no-numeric-scoring. EXCLUDED: package history/process; future policy and consumer schemas not invented.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards. |
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
| F112 | `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` | Whole read for Chapter 3-e/3-f; exact blob verified at 6a7160b. | C-GOLD.1 identities/records/currentness in 3-e; C-GOLD.1.5 operation/execution contracts in 3-f; remaining bridge behavior NOT PLACED: later pieces |
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
| §7.1 | C-GOLD.1.5, C-GOLD.1.5.1 |
| §7.2 | C-GOLD.1.5, C-GOLD.1.5.2, C-GOLD.1.5.2.1, C-GOLD.1.5.2.1.1, C-GOLD.1.5.2.1.2, C-GOLD.1.5.2.2, C-GOLD.1.5.2.2.1, C-GOLD.1.5.2.2.2, C-GOLD.1.5.2.3, C-GOLD.1.5.2.3.1, C-GOLD.1.5.2.3.2, C-GOLD.1.5.2.3.3, C-GOLD.1.5.2.4, C-GOLD.1.5.2.4.1, C-GOLD.1.5.2.4.2, C-GOLD.1.5.2.4.3, C-GOLD.1.5.2.4.4, C-GOLD.1.5.2.5, C-GOLD.1.5.2.5.1, C-GOLD.1.5.2.5.2, C-GOLD.1.5.2.6, C-GOLD.1.5.2.6.1, C-GOLD.1.5.2.6.2, C-GOLD.1.5.2.6.3, C-GOLD.1.5.2.6.4, C-GOLD.1.5.2.6.5, C-GOLD.1.5.2.6.6, C-GOLD.1.5.2.6.7, C-GOLD.1.5.2.6.8, C-GOLD.1.5.2.7, C-GOLD.1.5.2.7.1, C-GOLD.1.5.2.7.2, C-GOLD.1.5.2.7.3, C-GOLD.1.5.2.8, C-GOLD.1.5.2.8.1, C-GOLD.1.5.2.8.2, C-GOLD.1.5.2.8.3, C-GOLD.1.5.2.9, C-GOLD.1.5.2.9.1, C-GOLD.1.5.2.9.2, C-GOLD.1.5.2.10, C-GOLD.1.5.2.10.1, C-GOLD.1.5.2.10.2, C-GOLD.1.5.2.11, C-GOLD.1.5.2.11.1, C-GOLD.1.5.2.11.2, C-GOLD.1.5.2.12, C-GOLD.1.5.2.12.1, C-GOLD.1.5.2.12.2, C-GOLD.1.5.2.13, C-GOLD.1.5.2.13.1, C-GOLD.1.5.2.13.2, C-GOLD.1.5.2.13.3, C-GOLD.1.5.2.13.4, C-GOLD.1.5.3, C-GOLD.1.5.3.1, C-GOLD.1.5.3.2, C-GOLD.1.5.3.3, C-GOLD.1.5.3.4, C-GOLD.1.5.3.5, C-GOLD.1.5.3.6 |
| §13.5 | C-GOLD.1.5.2.1, C-GOLD.1.5.2.1.1, C-GOLD.1.5.2.1.2, C-GOLD.1.5.2.2, C-GOLD.1.5.2.2.1, C-GOLD.1.5.2.2.2, C-GOLD.1.5.2.3, C-GOLD.1.5.2.3.1, C-GOLD.1.5.2.3.2, C-GOLD.1.5.2.3.3, C-GOLD.1.5.2.4, C-GOLD.1.5.2.4.1, C-GOLD.1.5.2.4.2, C-GOLD.1.5.2.4.3, C-GOLD.1.5.2.4.4, C-GOLD.1.5.2.5, C-GOLD.1.5.2.5.1, C-GOLD.1.5.2.5.2, C-GOLD.1.5.2.6, C-GOLD.1.5.2.6.1, C-GOLD.1.5.2.6.2, C-GOLD.1.5.2.6.3, C-GOLD.1.5.2.6.4, C-GOLD.1.5.2.6.5, C-GOLD.1.5.2.6.6, C-GOLD.1.5.2.6.7, C-GOLD.1.5.2.6.8, C-GOLD.1.5.2.7, C-GOLD.1.5.2.7.1, C-GOLD.1.5.2.7.2, C-GOLD.1.5.2.7.3, C-GOLD.1.5.2.8, C-GOLD.1.5.2.8.1, C-GOLD.1.5.2.8.2, C-GOLD.1.5.2.8.3, C-GOLD.1.5.2.9, C-GOLD.1.5.2.9.1, C-GOLD.1.5.2.9.2, C-GOLD.1.5.2.10, C-GOLD.1.5.2.10.1, C-GOLD.1.5.2.10.2, C-GOLD.1.5.2.11, C-GOLD.1.5.2.11.1, C-GOLD.1.5.2.11.2, C-GOLD.1.5.2.12, C-GOLD.1.5.2.12.1, C-GOLD.1.5.2.12.2, C-GOLD.1.5.2.13, C-GOLD.1.5.2.13.1, C-GOLD.1.5.2.13.2, C-GOLD.1.5.2.13.3, C-GOLD.1.5.2.13.4, C-GOLD.1.5.13 |
| §7.10 | C-GOLD.1.5.3.1, C-GOLD.1.5.3.2, C-GOLD.1.5.3.3, C-GOLD.1.5.3.4, C-GOLD.1.5.3.5, C-GOLD.1.5.3.6, C-GOLD.1.5.11, C-GOLD.1.5.11.1, C-GOLD.1.5.11.1.1, C-GOLD.1.5.11.1.2, C-GOLD.1.5.11.1.3, C-GOLD.1.5.11.1.4, C-GOLD.1.5.11.1.5, C-GOLD.1.5.11.2, C-GOLD.1.5.11.2.1, C-GOLD.1.5.11.2.2, C-GOLD.1.5.11.2.3, C-GOLD.1.5.11.2.4, C-GOLD.1.5.11.2.5, C-GOLD.1.5.11.3, C-GOLD.1.5.11.3.1, C-GOLD.1.5.11.3.2, C-GOLD.1.5.11.3.3, C-GOLD.1.5.11.3.4, C-GOLD.1.5.11.3.5, C-GOLD.1.5.11.4 |
| §7.3 | C-GOLD.1.5.4 |
| §7.4 | C-GOLD.1.5.5, C-GOLD.1.5.5.1, C-GOLD.1.5.5.2, C-GOLD.1.5.5.3 |
| §7.5 | C-GOLD.1.5.6, C-GOLD.1.5.6.1, C-GOLD.1.5.6.2, C-GOLD.1.5.6.3, C-GOLD.1.5.6.4, C-GOLD.1.5.6.5, C-GOLD.1.5.6.6, C-GOLD.1.5.6.7, C-GOLD.1.5.6.8, C-GOLD.1.5.6.9 |
| §13.1 | C-GOLD.1.5.6.9, C-GOLD.1.5.8.1.1, C-GOLD.1.5.8.1.2, C-GOLD.1.5.8.1.3, C-GOLD.1.5.8.1.4, C-GOLD.1.5.8.1.5, C-GOLD.1.5.12, C-GOLD.1.5.12.1, C-GOLD.1.5.12.2, C-GOLD.1.5.12.3, C-GOLD.1.5.12.4, C-GOLD.1.5.12.5, C-GOLD.1.5.12.6, C-GOLD.1.5.12.7, C-GOLD.1.5.12.8, C-GOLD.1.5.12.9, C-GOLD.1.5.12.10, C-GOLD.1.5.12.11, C-GOLD.1.5.12.12, C-GOLD.1.5.12.13, C-GOLD.1.5.12.14, C-GOLD.1.5.12.15, C-GOLD.1.5.12.16, C-GOLD.1.5.12.17, C-GOLD.1.5.12.18, C-GOLD.1.5.12.19, C-GOLD.1.5.12.20, C-GOLD.1.5.12.21, C-GOLD.1.5.12.22, C-GOLD.1.5.12.23, C-GOLD.1.5.12.24 |
| §2.3 | C-GOLD.1.5.6.10, C-GOLD.1.5.6.10.1, C-GOLD.1.5.6.10.2, C-GOLD.1.5.6.10.3, C-GOLD.1.5.6.10.4, C-GOLD.1.5.6.10.5, C-GOLD.1.5.6.10.6, C-GOLD.1.5.6.10.7, C-GOLD.1.5.6.10.8, C-GOLD.1.5.6.10.9, C-GOLD.1.5.6.10.10 |
| §7.6 | C-GOLD.1.5.7 |
| §7.9 | C-GOLD.1.5.8, C-GOLD.1.5.8.1, C-GOLD.1.5.8.1.1, C-GOLD.1.5.8.1.2, C-GOLD.1.5.8.1.3, C-GOLD.1.5.8.1.4, C-GOLD.1.5.8.1.5, C-GOLD.1.5.8.2, C-GOLD.1.5.8.3, C-GOLD.1.5.8.4 |
| §7.7 | C-GOLD.1.5.9, C-GOLD.1.5.9.1, C-GOLD.1.5.9.2, C-GOLD.1.5.9.3, C-GOLD.1.5.9.4, C-GOLD.1.5.9.5, C-GOLD.1.5.9.6, C-GOLD.1.5.9.7, C-GOLD.1.5.9.8, C-GOLD.1.5.9.8.1, C-GOLD.1.5.9.8.2, C-GOLD.1.5.9.8.3, C-GOLD.1.5.9.9, C-GOLD.1.5.9.10, C-GOLD.1.5.9.11, C-GOLD.1.5.9.12 |
| §5 | C-GOLD.1.5.9.1, C-GOLD.1.5.9.2, C-GOLD.1.5.9.3, C-GOLD.1.5.9.4, C-GOLD.1.5.9.5, C-GOLD.1.5.9.6, C-GOLD.1.5.9.7, C-GOLD.1.5.9.8, C-GOLD.1.5.9.9, C-GOLD.1.5.9.10, C-GOLD.1.5.9.11, C-GOLD.1.5.9.12 |
| §7.12 | C-GOLD.1.5.9.8.1, C-GOLD.1.5.9.8.2, C-GOLD.1.5.9.8.3 |
| §7.8 | C-GOLD.1.5.10, C-GOLD.1.5.10.1, C-GOLD.1.5.10.2, C-GOLD.1.5.10.3, C-GOLD.1.5.10.4, C-GOLD.1.5.10.5, C-GOLD.1.5.10.6, C-GOLD.1.5.10.7, C-GOLD.1.5.10.8, C-GOLD.1.5.10.9, C-GOLD.1.5.10.10, C-GOLD.1.5.10.11, C-GOLD.1.5.10.12, C-GOLD.1.5.10.13, C-GOLD.1.5.10.14, C-GOLD.1.5.10.15 |

## READ RECORD

### Files read whole for this pair

- `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` — 2,018 lines, 135,956 bytes; SHA-256 `04dd5abc42e59afb61b4d280a0bb69d647d187fd0da385bc5c567eddbca81a41`; Git blob matches the verified source pin.
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` — acceptance identity/status and open-slot definitions; matched the source pin.
- Instruction: cloned `NH_MASTER-21_SYSTEM_BEHAVIOR_BUILD_CONTRACT_FOR_CHATGPT_v1_0.md`, SHA-256 `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1`.
- Instruction: `NH_MASTER-21_FIX_REQUEST_ROUND1_2026-09-25(1).md`; the all-card field-placement rule and step reciprocity remain applied.

### Scoped checks, without new whole-read credit

- V10 authoritative status table; reading/production boundaries and protected gold/engine passages. No bridge behavior is recorded as built.
- Map C-GOLD, C-READ and adjacent Group A component definitions; bridge source §3 establishes evaluation ownership.
- Decision Index v0_11 NHD-B16EEB and L.4 rows, and the actual acceptance receipt; index used for navigation only.
- GitHub tree and commit comparison: source pin is `6a7160ba688ba4e433a31899162815df7e2bab17`; the governing and accepted bridge source blobs match the local copies. Six revised chapter blobs match the supplied GitHub pin; CH00 is an earlier assembly input, not used for new behavior.

### READ-folder files not yet read whole

97 entries retain the earlier pending whole-read status. The three B16/receipt files already had older Chapter 0 reading credits and were not in that pending list; they were now reread whole at this pin. The bridge source has only its earlier credit plus the scoped current check, not a new whole read. Scoped searches/excerpts supply no whole-read credit. The ledger retains its Stage-2-only exception.

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

- `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md` — newly present at this source pin; not used for this evaluation scope.


The earlier whole-read accounting is carried forward; this pair adds whole-read credit only for the files explicitly listed above. The seven prior chapter files are preserved assembly inputs and receive no fresh whole-read credit here. No not-yet-read file supplies new behavior in this pair.

## CONTRACT CHECK

CONTRACT CHECK (against the cloned contract, SHA-256 e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1)
§1.3 no history/actions/roles/workflow in this chapter: PASS — all 177 behavior cards, field lines and reciprocal rows checked; source status and read accounting are outside behavior. Runtime judgment authority remains runtime behavior, not drafting workflow.
§1.4 every gap written as NOT DECIDED: PASS — all 531 prohibition/failure/gate boxes reviewed against their own text and cited source. 298 empty fields and 1 scoped gaps are registered with reasons. Decided material scheduled for a later piece is separately listed; it is not called undecided.
§1.5 conflicts marked, none resolved: PASS — B16 v1.0’s earlier input-3 wording is preserved in the source-conflict register; Chapter 3-e also marks the narrow E13 behavior line. No accepted source or earlier chapter is edited; V10 remains governing.
§3 exactly one stamp per line: PASS — 1529 populated field lines and 317 USED BY rows checked. All are ACCEPTED from the exact accepted bridge source. The V10 status table grants no BUILT standing to these bridge records, operations or links; none is stamped BUILT.
§4 every behavior line cited in the exact format: PASS — every populated field and reciprocal row carries exact 05/file §section citations to the accepted v1.7 source and NHD-B16EEB. All section targets resolve; record-definition citations include the actual later section where a carried outcome is defined. Receipt §§3–5 establishes accepted standing independently of folder/header.
§5.4 one name per thing: PASS — new sub-part IDs remain under the Map’s existing C-GOLD identifier; canonical endpoint names match prior chapter names. No new top-level ID or controlled NHD identifier is introduced. Proposed source names and globally unique policy-slot IDs are retained.
§6 all template fields present, in order, for every part: PASS — all 177 templates carry all nine fields in order, ALONE, TOGETHER, USED BY and SUB-PARTS; every listed child exists in this pair.
§6.3 reciprocity within this chapter: PASS — all 854 unique relationship pairs across 3-e/3-f checked in both directions. The 39 transaction/stage/recovery step cards name their defining rules with reciprocal USED BY rows. External endpoint additions are recorded here without modifying prior chapters.
§6.4 every decided detail written in, no citation used in place of content: PASS within this piece’s explicit scope — All thirteen bridge operation identities and their terminal/log vocabularies; run-closing conditions; frozen terminal set; output-before-visibility; B9 classifications and accepted limits; twelve transaction boundaries; fifteen idempotency points; CAS-1, CAS-2, DET-1 and CAS-3; three resolution outcomes with all consequences; twenty-four in-scope recovery cases. Protected judgment-specific recovery remains explicitly reserved.
§6.5 sub-parts recursed to the bottom: PASS within this piece’s explicit scope — record members, named measurement dimensions, registered enum/failure classes, operation outcomes, commit conditions and resolution consequences have cards. No unchosen policy value, storage algorithm, mechanism or authorization option is invented.
§9 coverage matrix rows added for every file used: PASS — all 145 READ-folder files at the pin are accounted for; all 107 carried V10 heading rows remain. The bridge and receipt rows reflect this whole read, with a detailed section landing map. Source/passed-chapter blob preservation checked for 52 matched local files.
§10.11 no recommendation, no sentence addressed to Ness: PASS — checked in all behavior cards and register contributions; source recommendations are not imported as decisions.
Files read whole for this chapter: `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`; the cloned contract and fix-request instructions. Scoped rereads and inherited whole-read credits remain separately identified in READ RECORD.

This is the producing assistant’s contract check, not an independent audit, acceptance, adoption or implementation authorization. The two new pieces are delivered together under the current request; all passed chapters remain unchanged.
