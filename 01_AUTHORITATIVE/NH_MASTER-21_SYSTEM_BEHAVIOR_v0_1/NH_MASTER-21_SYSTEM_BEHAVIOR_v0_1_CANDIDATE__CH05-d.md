# Chapter 5-d — Group C: C-7H

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH05-d.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`

This piece covers C-7H — Reread Lifecycle (§7H), with all its sub-parts. It leaves C-CREATE to CH05-e, every path except P-MAIN to CH11, and the appendices to CH12.

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Every citation resolves at the pinned commit.

<!-- BEGIN BEHAVIOR -->

### C-7H — Reread Lifecycle (§7H)
Stamp: DESIGNED    Source: [V10 §7H] [MAP C-7H]

ALONE
- What it is: DESIGNED — The lifecycle that adds a new reading beside an earlier one for an explicit recorded reason. [V10 §7H] [MAP C-7H]
- Takes in: DESIGNED — A manual request, materially relevant new information, a permitted temporary-technical trigger, or recorded rejection eligibility. [V10 §7H] [MAP C-7H]
- Does: DESIGNED — Records trigger, reason, initiator, changed evidence/condition, previous reading IDs, configuration and time; creates a new reading without changing the old one. [V10 §7H] [MAP C-7H]
- Gives out: DESIGNED — A new revisable reading and its provenance, with earlier readings still visible. [V10 §7H] [MAP C-7H]
- Must never: DESIGNED — Overwrite, edit or delete earlier readings, or treat rejection as proof of the opposite. [V10 §7H] [MAP C-7H]
- Fails closed by: DESIGNED — No reread occurs without a recorded reason; a revisable reading may remain unrevisited indefinitely without a trigger. [V10 §7H] [MAP C-7H]

TOGETHER
- Fed by: ACCEPTED — C-7H.2 — B10 reread identity and records: Uses separate reread identities. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.7 — A25 semantic reread assignment: Consumes truthful A25 relationships. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-7H.8 — Manual reread compatibility: Supports the settled manual no-information case. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Fed by: DESIGNED — C-7A.7 — R5 — Classification never locked: makes provisional classification operational through rereading (CY-F); C-7A.9 — R6 — Memory only adds: adds the reread as a new layer beside the original (CY-F). [V10 §7A] [MAP C-7A]
- Fed by: DESIGNED — C-7B.2.7 — RE-READING: operationalizes a new pass (CY-F). [MAP C-7B] [V10 §7H]
- Fed by: DESIGNED — C-READ — Reading record, validator, writer (§6B): validates and appends the reading through the shared writer (CY-F). [V10 §7H]
- Fed by: DESIGNED — C-7A — Universal Filter (§7A): makes provisional classification and accretion operational by adding the reread as a new layer (CY-F). [V10 §7A] [MAP C-7A]
- Fed by: DESIGNED — C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B): runs the chain again for a piece with materially relevant new context (CY-F). [V10 §7H] [MAP C-7B]
- Gated by: DESIGNED — C-7H.1 — Reread trigger boundaries: Requires an actual bounded trigger. [V10 §7H]
- Gated by: ACCEPTED — C-7H.3 — B10 reread transaction boundaries: Uses the canonical transaction boundaries. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Gated by: ACCEPTED — C-7H.4 — B10 eight duplicate-prevention points: Preserves duplicate defenses. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7H.5 — B10 recovery and fail-closed rules: Uses lookup-first recovery. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.9 — B9 retry-state architecture: Separates incomplete-operation retry from new layers. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §3]
- Gated by: ACCEPTED — C-7H.10 — Accepted B9 retry values and episodes: Keeps retries within accepted bounds. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3]
- Gated by: ACCEPTED — C-7H.11 — RM-RR-01 [proposed] reread relevance declaration: Evaluates only condition-based relevance here. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7H.12 — Retry, reread and hold coordination: Preserves retry/reread/hold ownership. [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2]
- Gated by: ACCEPTED — C-7B.7 — Hold-until-enough: refuse or block the reread claim at B10 RR1 (CY-F). [04/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md §6] [MAP CY-F]
- Changes: ACCEPTED — C-7H.6 — B10 operational logging: Logs actual reread operations. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7B.7.1.6 — Hold distinctions | Actual hold/source state. | Uses the proper owner boundary. | No hidden release or reread-as-retry. | [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2] |
| 2 · BUILT | C-READ — Reading record, validator, writer (§6B) | New reading and preserved prior-layer references. | Adds one layer. | No overwrite of earlier readings. | [V10 §7H] |
| 3 · ACCEPTED | C-7G.9 — B9 acceptance retry and fallback boundary | Durable attempt and episode evidence. | Applies the exact acceptance retry seam. | No alternative local retry state machine. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13] |
| 4 · ACCEPTED | C-7G.9.8 — Retry early stop and real-change continuation | Cause, evidence and actual change. | Preserves closed episodes and records continuation. | No same-episode reset. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §8] |
| 5 · ACCEPTED | C-7GA.14 — Accepted retry and reread boundaries consumed by the worker | Source completion state. | Routes retry versus reread. | No retry of a completed reading. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2] |
| 6 · ACCEPTED | C-7GA.14.1 — Technical-retry admission boundary | Technical failure and both remaining bounds. | Admits only one eligible attempt. | No execution before commitment. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| 7 · ACCEPTED | C-7GA.14.2 — Later technical-episode first-attempt boundary | Committed authorization and next permanent number. | Binds ordinal 1 with explicit no-gap/deadline-pending states. | No invented anchors or reset numbers. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| 8 · ACCEPTED | C-7F.7.3 — Accepted B26 stop-after-retry policy | Retryable technical class and exact admission evidence. | Applies only eligible bounded retries. | No degraded continuation from exhaustion. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| 9 · DESIGNED | C-7H.1 — Reread trigger boundaries; CY-F | A real recorded trigger and unchanged prior reading history. | Creates a separately identified complete reading layer through permission, context and acceptance. | The new layer is appended beside the old layers; repeat recovery creates no extra layer. | [V10 §7H] [MAP C-7H] |
| 10 · DESIGNED | C-OTHER.7.4 — Translation reading and revision | Translation output from the requested assistance branch. | Takes this place's change: the translation reading remains eligible for source-governed revision through rereading. | The translation reading remains eligible for source-governed revision through rereading. | [V10 §25.2 / Parent Translation] |
| 11 · DESIGNED | C-7O.6.1 — Confirmed-result reread handoff | The confirmed connection and new source evidence. | Gates this place: the actual reread trigger requirements must be satisfied. | Nothing in this card. | [V10 §7O] |
| 12 · DESIGNED | C-OTHER.8 — Statements about Ness retain their speaker | A third-party statement, its speaker and the session context. | Takes this place's change: later evidence may cause a new reading without altering the earlier records. | Later evidence may cause a new reading without altering the earlier records. | [V10 §25.2 / Statements About Ness] |
| 13 · ACCEPTED | C-7O.13 — Result-return coordination ownership boundary | Typed references to the actual action, root, connection, permission, retry and component outcome records. | Supplies what this place relies on: reread remains distinct from retry. | Nothing in this card. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §U] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §V.2] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §W] |
| 14 · DESIGNED | C-LEARN.6.6 — Later evidence reconnects without rewriting history | Later evidence that bears on the current interpretation of earlier material. | Supplies canonical condition-based reread path. | Nothing in this card. | [V10 §26.9] [V10 §26.11] |
| 15 · DESIGNED | C-7O — Action-Result Return Path (§7O) | An earlier action, Ness's reported result or incoming material possibly related to the action, and any separate Ness response. | Takes this place's change: a confirmed result connection may become a governed reread trigger. | A confirmed result connection may become a governed reread trigger. | [V10 §7O] [MAP C-7O] |
| 16 · DESIGNED | C-OOP.5.2 — Outcome contradiction triggers reread | The new outcome reading and the prior reading it contradicts. | Takes this place's change: its condition-based reread fires on the contradiction. | Its condition-based reread fires on the contradiction. | [V10 §26.6] |
| 17 · DESIGNED | C-LEARN.8.4.4 — Calibration rereads survive without contradiction | Rereads of patterns within the accumulated evidence base. | Owns the reread lifecycle and its preserved results. | Nothing in this card. | [V10 §26.11] |
| 18 · ACCEPTED | C-16.23 — Model-boundary retry and fallback consumption | The actual recorded failure/rejection class, source-operation identity, prior attempts and durable outcomes. | Gates this place: retains the canonical accepted B9 retry mechanics under its existing sub-parts. | Nothing in this card. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] |
| 19 · DESIGNED | C-BOP.9 — connection_anchors and later reconnection | Any available structural connection anchors. | Supplies condition-based rereads. | Nothing in this card. | [V10 §25.1] |

SUB-PARTS: C-7H.1 — Reread trigger boundaries; C-7H.2 — B10 reread identity and records; C-7H.3 — B10 reread transaction boundaries; C-7H.4 — B10 eight duplicate-prevention points; C-7H.5 — B10 recovery and fail-closed rules; C-7H.6 — B10 operational logging; C-7H.7 — A25 semantic reread assignment; C-7H.8 — Manual reread compatibility; C-7H.9 — B9 retry-state architecture; C-7H.10 — Accepted B9 retry values and episodes; C-7H.11 — RM-RR-01 [proposed] reread relevance declaration; C-7H.12 — Retry, reread and hold coordination

### C-7H.1 — Reread trigger boundaries
Stamp: DESIGNED    Source: [V10 §7H]

ALONE
- What it is: DESIGNED — Three named trigger classes and the separately stated rejection-eligibility path. [V10 §7H]
- Takes in: DESIGNED — Actual requests, relevant new information, temporary technical conditions or a recorded rejection. [V10 §7H]
- Does: DESIGNED — Requires the applicable bounded trigger rather than rereading merely because time passed. [V10 §7H]
- Gives out: DESIGNED — A real recorded reread reason. [V10 §7H]
- Must never: DESIGNED — Turn any new memory into blanket permission to reread everything. [V10 §7H]
- Fails closed by: DESIGNED — No qualifying trigger means no reread. [V10 §7H]

TOGETHER
- Fed by: DESIGNED — C-7H.1.1 — Manual reread trigger: Accepts a manual request at any time. [V10 §7H]
- Fed by: DESIGNED — C-7H.1.4 — Rejection-linked reread eligibility: Retains separate rejection eligibility. [V10 §7H]
- Fed by: DESIGNED — C-7H — Reread Lifecycle (§7H): supplies the recorded trigger and the unchanged prior reading history (CY-F). [V10 §7H] [MAP C-7H]
- Gated by: DESIGNED — C-7H.1.2 — Condition-based reread trigger: Requires materially relevant change for conditional use. [V10 §7H]
- Gated by: DESIGNED — C-7H.1.3 — Scheduled automatic technical retry trigger: Limits automatic retry to technical conditions. [V10 §7H]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7H — Reread Lifecycle (§7H) | Trigger facts. | Checks eligibility. | No reasonless reread. | [V10 §7H] |
| 2 · DESIGNED | C-7H.1.1 — Manual reread trigger | Request event. | Preserves its reason. | Traceable permission. | [V10 §7H] |
| 3 · DESIGNED | C-7H.1.2 — Condition-based reread trigger | Change evidence. | Rejects time alone. | Bounded trigger. | [V10 §7H] |
| 4 · DESIGNED | C-7H.1.3 — Scheduled automatic technical retry trigger | Failure class. | Prevents reinterpretation. | Bounded retry trigger. | [V10 §7H] |
| 5 · DESIGNED | C-7H.1.4 — Rejection-linked reread eligibility | Rejection event. | Preserves trigger requirements. | No automatic opposite reading. | [V10 §7H] |

SUB-PARTS: C-7H.1.1 — Manual reread trigger; C-7H.1.2 — Condition-based reread trigger; C-7H.1.3 — Scheduled automatic technical retry trigger; C-7H.1.4 — Rejection-linked reread eligibility

### C-7H.1.1 — Manual reread trigger
Stamp: DESIGNED    Source: [V10 §7H]

ALONE
- What it is: DESIGNED — A reread requested by Ness at any time. [V10 §7H]
- Takes in: DESIGNED — The manual request itself. [V10 §7H]
- Does: DESIGNED — Permits the request without further justification. [V10 §7H]
- Gives out: DESIGNED — A valid manual trigger. [V10 §7H]
- Must never: DESIGNED — Require additional justification for the settled manual request. [V10 §7H]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7H.1 — Reread trigger boundaries: The manual trigger must be recorded. [V10 §7H]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7H.1 — Reread trigger boundaries | Request. | Records manual trigger. | No added justification. | [V10 §7H] |

SUB-PARTS: NONE

### C-7H.1.2 — Condition-based reread trigger
Stamp: DESIGNED    Source: [V10 §7H]

ALONE
- What it is: DESIGNED — Materially relevant new information under an explicitly designed relevance rule. [V10 §7H]
- Takes in: DESIGNED — New positional context, root evidence, resolved speaker/thread information, corrected provenance or a newly available required context channel. [V10 §7H]
- Does: DESIGNED — Establishes relevance before treating the change as a reread condition. [V10 §7H]
- Gives out: DESIGNED — A condition-based trigger with its real change recorded. [V10 §7H]
- Must never: DESIGNED — Treat time alone or any new memory as a sufficient condition. [V10 §7H]
- Fails closed by: DESIGNED — Without established relevance, the condition does not trigger rereading. [V10 §7H]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7H.1 — Reread trigger boundaries: A real relevant condition is required. [V10 §7H]
- Gated by: ACCEPTED — C-7H.11 — RM-RR-01 [proposed] reread relevance declaration: Uses the condition-evaluation declaration. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7H.1 — Reread trigger boundaries | New information. | Checks designed relevance. | No blanket rereading. | [V10 §7H] |

SUB-PARTS: NONE

### C-7H.1.3 — Scheduled automatic technical retry trigger
Stamp: DESIGNED    Source: [V10 §7H]

ALONE
- What it is: DESIGNED — Bounded automatic retry for temporary system conditions only. [V10 §7H]
- Takes in: DESIGNED — Model/service timeout, unavailable or stale index, interrupted processing or another explicitly retryable technical failure. [V10 §7H]
- Does: DESIGNED — Uses bounded, idempotent retry with duplicate and endless-loop protection. [V10 §7H]
- Gives out: DESIGNED — A technical re-attempt under its permitted lifecycle. [V10 §7H]
- Must never: DESIGNED — Use the technical trigger for reinterpretation. [V10 §7H]
- Fails closed by: DESIGNED — Retry remains bounded and protected against duplicate rereads and endless loops. [V10 §7H]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7H.1 — Reread trigger boundaries: Only temporary technical conditions qualify. [V10 §7H]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7H.1 — Reread trigger boundaries | Temporary failure. | Applies bounded retry. | No reinterpretation. | [V10 §7H] |

SUB-PARTS: NONE

### C-7H.1.4 — Rejection-linked reread eligibility
Stamp: DESIGNED    Source: [V10 §7H]

ALONE
- What it is: DESIGNED — The separately stated response to Ness rejecting a reading. [V10 §7H]
- Takes in: DESIGNED — The actual rejection. [V10 §7H]
- Does: DESIGNED — Records rejection, marks the reading and may make it eligible for reread. [V10 §7H]
- Gives out: DESIGNED — A marked reading and possible reread eligibility. [V10 §7H]
- Must never: DESIGNED — Conclude that the opposite interpretation is correct. [V10 §7H]
- Fails closed by: DESIGNED — Eligibility alone does not erase the recorded-reason requirement. [V10 §7H]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7H.1 — Reread trigger boundaries: Eligibility still needs a recorded reread reason. [V10 §7H]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7H.1 — Reread trigger boundaries | Recorded rejection. | Marks eligibility. | No opposite-proof inference. | [V10 §7H] |

SUB-PARTS: NONE

### C-7H.2 — B10 reread identity and records
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §3] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — Proposed external identities distinguishing a new reading layer from a duplicate attempt. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §3] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — An already-ingested root, a recorded trigger and previous readings. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §3] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Gives each root/trigger one canonical claim and at most one new quarantine reading; uses separate caller and child operation identities. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §3] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — A trigger, claim, reading identity and external layer trail. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §3] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Reuse the new-root enqueue identity or mutate the root's sealed re_reads field as reread state. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §3] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Missing triggers and misrouted new-root identities are refused. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §3] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: ACCEPTED — C-7H.2.1 — reread_trigger_record [proposed]: Requires the trigger record first. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.2.2 — reread_claim_key [proposed]: Uses a root/trigger-specific claim. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.2.3 — reread_reading_idempotency_key [proposed]: Uses one reading key per claim. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.2.4 — reread_operation_id [proposed]: Uses caller and child identities. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7H.2.5 — reread_layer_record [proposed]: Binds the new layer externally. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7H — Reread Lifecycle (§7H) | Root and trigger. | Binds the operation. | New-layer identity. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] |
| 2 · ACCEPTED | C-NEW-UDOK.2.20 — ID-20 — B10 reread claim identity [proposed] | B10's `reread_claim_key` under its own contract. | Owns the reread identity and its distinct claim. | Nothing in this card. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §B.2] |
| 3 · ACCEPTED | C-NEW-UDOK.2.21 — ID-21 — B10 reread operation identity [proposed] | The actual reread operation reference. | Supplies the owner operation identity. | Nothing in this card. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §B.2] |
| 4 · ACCEPTED | C-NEW-UDOK.13.3 — I-3 — B10 reference interface [proposed] | Typed B10 references. | Supplies the owner identity and records. | Nothing in this card. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §T] |

SUB-PARTS: C-7H.2.1 — reread_trigger_record [proposed]; C-7H.2.2 — reread_claim_key [proposed]; C-7H.2.3 — reread_reading_idempotency_key [proposed]; C-7H.2.4 — reread_operation_id [proposed]; C-7H.2.5 — reread_layer_record [proposed]

### C-7H.2.1 — reread_trigger_record [proposed]
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — A proposed append-only prerequisite record for one real trigger occurrence. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — Trigger type, reason, initiator, evidence/condition references, previous reading IDs, configuration and timestamp. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Records the complete trigger set before reread execution. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — A stable trigger record referenced by the claim. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Fabricate a trigger or require new evidence to justify an already valid manual request. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — No trigger record means no reread. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: ACCEPTED — C-7H.2.1.1 — Reread trigger_type: Records actual trigger class. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.2.1.2 — Reread trigger reason: Requires the real reason. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.2.1.3 — Reread initiator: Records the actual initiator. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.2.1.4 — Reread changed-evidence references: References the actual changed condition. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.2.1.5 — Reread previous reading IDs: Binds prior readings by ID. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.2.1.6 — Reread configuration reference: Records the new configuration reference. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.2.1.7 — Reread trigger timestamp: Records trigger time. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.2 — B10 reread identity and records | Recorded reason set. | Binds the trigger. | No anonymous reread. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] |

SUB-PARTS: C-7H.2.1.1 — Reread trigger_type; C-7H.2.1.2 — Reread trigger reason; C-7H.2.1.3 — Reread initiator; C-7H.2.1.4 — Reread changed-evidence references; C-7H.2.1.5 — Reread previous reading IDs; C-7H.2.1.6 — Reread configuration reference; C-7H.2.1.7 — Reread trigger timestamp

### C-7H.2.1.1 — Reread trigger_type
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The proposed trigger-type field with manual, condition_based, scheduled_automatic_retry and on_rejection values. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The actual trigger class. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Carries the accepted B10 representation without changing V10's separately stated rejection path. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — trigger_type. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Use scheduled_automatic_retry for reinterpretation. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.2.1 — reread_trigger_record [proposed] | Trigger occurrence. | Stores trigger_type. | Explicit classification. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.2.1.2 — Reread trigger reason
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The real recorded reason for this reread. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The request or qualifying condition. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Records why the trigger exists. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — The trigger's reason. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Substitute a mode name for a real reason. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — No recorded reason permits no reread. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.2.1 — reread_trigger_record [proposed] | Request or condition. | Records why. | No mode as reason. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.2.1.3 — Reread initiator
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — Who or what initiated the reread. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The trigger's actual initiator. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Records initiator provenance. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — Initiator identity. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.2.1 — reread_trigger_record [proposed] | Who or what initiated. | Preserves identity. | Attributable trigger. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.2.1.4 — Reread changed-evidence references
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — References to new evidence or a changed condition. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The actual condition carried by the trigger. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Preserves its references rather than manufacturing evidence. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — Traceable changed-condition provenance. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.2.1 — reread_trigger_record [proposed] | Evidence refs. | Carries provenance. | No copied evidence. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.2.1.5 — Reread previous reading IDs
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The exact earlier readings to which the trigger relates. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Takes in: ACCEPTED — Existing reading identifiers. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Does: ACCEPTED — Binds the previous-reading evidence set by identity. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gives out: ACCEPTED — Previous reading references. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Must never: ACCEPTED — Reconstruct an unverifiable earlier reading. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Missing/unreadable prior readings cause refusal or indeterminate recovery according to store readability. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.2.1 — reread_trigger_record [proposed] | Existing reading IDs. | Preserves the evidence set. | Traceable earlier layers. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.2.1.6 — Reread configuration reference
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The new reread configuration referenced by the trigger. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The applicable configuration identity. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Records the configuration reference. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — Traceable configuration provenance. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.2.1 — reread_trigger_record [proposed] | Configuration identity. | Binds configuration. | Reproducible setup. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.2.1.7 — Reread trigger timestamp
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The time recorded for the actual trigger. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The trigger's timestamp. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Preserves that time in the append-only record. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — Trigger time provenance. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.2.1 — reread_trigger_record [proposed] | Timestamp. | Preserves time. | Temporal provenance. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.2.2 — reread_claim_key [proposed]
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — Proposed stable_hash(root_id + trigger_record_id + "reread_job_v1"). [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — One root identity and one trigger record identity. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Establishes one canonical claim per root/trigger, distinct from the new-root reading_job_v1 key. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — reread_claim_key [proposed]. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Collide with or reuse new-root enqueue_key, or create multiple claims for the same trigger/root. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — A request naming the new-root identity is refused as misrouted. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.4.2 — One canonical claim per root and trigger: One claim exists per root/trigger. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.2 — B10 reread identity and records | Root and trigger IDs. | Derives the key. | Distinct from new-root identity. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.2.3 — reread_reading_idempotency_key [proposed]
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — Proposed stable_hash(reread_claim_key + "reading_v1"). [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The canonical reread claim key. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Assigns this value to the new reading's existing idempotency_key field. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — At most one reading ever per claim across attempts. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Add a thirteenth reading-schema field or produce a second layer from a duplicate trigger. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — An existing reading under the key is recovered rather than rewritten. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.4.4 — One reread reading per claim: One reading exists per claim. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.2 — B10 reread identity and records | Claim key. | Derives idempotency. | One reading ever. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] |
| 2 · ACCEPTED | C-7H.3.5 — RR4 — Layer commit | Claim key. | Detects existing output. | No duplicate reading. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.2.4 — reread_operation_id [proposed]
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — The proposed parent identity for each caller invocation. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Takes in: ACCEPTED — The invocation and separately executed claim, snapshot, execution/acceptance, layer and recovery steps. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Does: ACCEPTED — Gives each real child its own identity/log and the parent one terminal. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Gives out: ACCEPTED — Parent/child operational references. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Must never: ACCEPTED — Duplicate child logs or acknowledge before the durable parent terminal. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Missing terminal is completed from durable evidence before acknowledgement. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.3.6 — RR5 — Reread parent terminal: Requires one durable terminal before acknowledgement. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.2 — B10 reread identity and records | Invocation. | Records operation lineage. | One terminal per request. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.2.5 — reread_layer_record [proposed]
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — A proposed external append-only identity trail beside the new reading. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — Claim, trigger, new reading_id and previous reading IDs. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Binds those references without inserting new fields into the reading. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — One layer record per claim. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Edit or replace an earlier reading or store the layer trail inside a rewritten root. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Completes a missing layer record idempotently from the reading's durable identity. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: ACCEPTED — C-7H.2.5.1 — Reread layer claim reference: Carries claim identity. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.2.5.2 — Reread layer trigger reference: Carries trigger identity. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.2.5.3 — Reread layer reading_id: Carries committed reading identity. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.2.5.4 — Reread layer previous-reading references: Carries earlier reading identities. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-7H.4.5 — One layer trail per claim: Completes only one layer record. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.2 — B10 reread identity and records | Claim, trigger and readings. | Appends layer trail. | No schema expansion. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] |
| 2 · ACCEPTED | C-7H.3.5 — RR4 — Layer commit | Reading and claim evidence. | Completes layer binding. | Recoverable provenance. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |

SUB-PARTS: C-7H.2.5.1 — Reread layer claim reference; C-7H.2.5.2 — Reread layer trigger reference; C-7H.2.5.3 — Reread layer reading_id; C-7H.2.5.4 — Reread layer previous-reading references

### C-7H.2.5.1 — Reread layer claim reference
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The layer record's canonical claim reference. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The committed reread claim. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Binds the new layer to that claim. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — Claim identity in the layer trail. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.2.5 — reread_layer_record [proposed] | Claim ref. | Binds claim. | Layer identity continuity. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.2.5.2 — Reread layer trigger reference
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The layer record's explicit trigger reference. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The claim's trigger record. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Binds the layer to its actual reason event. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — Trigger identity in the layer trail. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.2.5 — reread_layer_record [proposed] | Trigger ref. | Binds reason event. | Layer reason continuity. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.2.5.3 — Reread layer reading_id
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The layer record's exact newly committed reading identity. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The durable new reading. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Records its reading_id. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — The new layer's reading pointer. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Invent an output reading absent durable evidence. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.2.5 — reread_layer_record [proposed] | reading_id. | Binds new output. | Exact layer pointer. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.2.5.4 — Reread layer previous-reading references
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The layer record's earlier-reading identity set. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The trigger's bound previous reading IDs. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Preserves the new layer's relationship to untouched earlier readings. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — Earlier-layer provenance. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Replace or delete the earlier layers. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.2.5 — reread_layer_record [proposed] | Prior IDs. | Preserves lineage. | Untouched history. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.3 — B10 reread transaction boundaries
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — Lookup, claim, snapshot, execution, layer commit and parent terminal, followed by rebuildable indexes. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — A recorded trigger and durable source/claim evidence. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Runs RR0 through RR5 with one claim winner and one new quarantine reading; RR-PR remains nonauthoritative. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — A committed or honestly refused, blocked, interrupted or indeterminate operation. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Acknowledge before durable RR5 or let rebuildable indexes decide success. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Unreadable or contradictory evidence blocks progress rather than reconstructing facts. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: ACCEPTED — C-7H.3.1 — RR0 — Reread lookup: Starts with lookup. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-7H.3.3 — RR2 — Instruction and context snapshot: Assembles authorized bound context. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-7H.3.4 — RR3 — Execution and acceptance: Runs the existing acceptance path. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Gated by: ACCEPTED — C-7H.3.2 — RR1 — Reread claim commit: Requires one claim winner. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Changes: ACCEPTED — C-7H.3.5 — RR4 — Layer commit: Commits one new quarantine layer. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Changes: ACCEPTED — C-7H.3.6 — RR5 — Reread parent terminal: Closes the parent before acknowledgement. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Changes: ACCEPTED — C-7H.3.7 — RR-PR — Post-commit indexes and coverage: Rebuilds derived indexes after commitment. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7H — Reread Lifecycle (§7H) | Durable state. | Runs RR0–RR5. | One honest outcome. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |
| 2 · ACCEPTED | C-7H.3.1 — RR0 — Reread lookup | Existing evidence. | Absorbs or refuses. | No duplicate execution. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |
| 3 · ACCEPTED | C-7H.3.2 — RR1 — Reread claim commit | Claim inputs. | Admits one winner. | No unclaimed work. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |
| 4 · ACCEPTED | C-7H.3.3 — RR2 — Instruction and context snapshot | Committed state. | Assembles permitted context. | No invented mode. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |
| 5 · ACCEPTED | C-7H.3.4 — RR3 — Execution and acceptance | Snapshot. | Runs the existing boundary. | No alternate acceptance path. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |
| 6 · ACCEPTED | C-7H.3.5 — RR4 — Layer commit | Claim and output. | Commits once. | Quarantine append only. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |
| 7 · ACCEPTED | C-7H.3.6 — RR5 — Reread parent terminal | Actual child states. | Closes once. | No false parent success. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] |
| 8 · ACCEPTED | C-7H.3.7 — RR-PR — Post-commit indexes and coverage | Committed output. | Rebuilds idempotently. | Cannot gate success. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |

SUB-PARTS: C-7H.3.1 — RR0 — Reread lookup; C-7H.3.2 — RR1 — Reread claim commit; C-7H.3.3 — RR2 — Instruction and context snapshot; C-7H.3.4 — RR3 — Execution and acceptance; C-7H.3.5 — RR4 — Layer commit; C-7H.3.6 — RR5 — Reread parent terminal; C-7H.3.7 — RR-PR — Post-commit indexes and coverage

### C-7H.3.1 — RR0 — Reread lookup
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — Read-only lookup for the root/trigger claim. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — Trigger and claim/layer evidence. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Returns the existing reading/layer as duplicate_absorbed if committed; observes another live claim as reread_interrupted and appends nothing; refuses a missing trigger. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — Existing result, live-claim status or refusal. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Create another layer for the same trigger. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Unreadable claim evidence fails closed. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.3 — B10 reread transaction boundaries: Lookup precedes new claim work. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.3 — B10 reread transaction boundaries | Root/trigger. | Finds existing claim. | Correct duplicate routing. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.3.2 — RR1 — Reread claim commit
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — One atomic compare-and-commit establishing the canonical claim. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — reread_claim_key [proposed], root identity, trigger reference, previous reading IDs, integrity references and parent operation. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Commits exactly one winning binding; concurrent losers observe and append nothing. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — A committed claim or dependency_blocked_held with no claim when a live hold exists. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Proceed without a committed claim or queue around a hold on the root or readings. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Live holds block; no committed claim means no further execution. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.3 — B10 reread transaction boundaries: No execution before committed claim. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Gated by: ACCEPTED — C-7B.7 — Hold-until-enough: A live hold blocks the claim. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.3 — B10 reread transaction boundaries | Claim inputs. | Commits atomically. | Exclusive claim. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.3.3 — RR2 — Instruction and context snapshot
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The mode-bound, authorized context-assembly boundary. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — A committed claim and valid reread_mode_ref [proposed]. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Applies internal-use authorization through LMAC, Context Retrieval, then relevance; commits the context snapshot with honest coverage and the mode-slot reference. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — A bound snapshot for reread execution. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Invent a mode, borrow thread_membership_v1, bypass authorization or silently replace snapshot context. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — An unfilled mode slot yields dependency_blocked_held; unreadable snapshot evidence fails closed; retrieval system failure closes the pass technical-failed with job state preserved. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: DESIGNED — C-7F — Context Retrieval (§7F): Retrieves authorized context before relevance consumption. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Gated by: ACCEPTED — C-7H.3 — B10 reread transaction boundaries: Claim and mode basis precede snapshot. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Gated by: ACCEPTED — C-7H.3.3.1 — reread_mode_ref [proposed]: Requires one valid committed referent. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §6]
- Gated by: DESIGNED — C-LMAC — Live Mechanism Access Coordinator (§26): Authorization is coordinated before context. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): Privacy authorization comes first. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Gated by: DESIGNED — C-7R — Attention & Relevance Control (§7R): Relevance follows prior authorization. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.3 — B10 reread transaction boundaries | Claim and mode basis. | Commits snapshot. | Fixed context evidence. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |
| 2 · ACCEPTED | C-LMAC.14.2 — Reread context routing order | The assignment and broadest safely available clearly relevant context. | Supplies the existing reread context step. | Nothing in this card. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §7] |

SUB-PARTS: C-7H.3.3.1 — reread_mode_ref [proposed]

### C-7H.3.3.1 — reread_mode_ref [proposed]
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The proposed B10 mode-slot reference consumed before context assembly. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — Exactly one committed A25 assignment or qualifying manual compatibility record. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — References that record's stable identity in the snapshot's committed state. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — A typed, claim-bound basis for RR2. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Borrow the new-root assignment rule or select between conflicting committed referents. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Missing basis holds; unreadable, malformed or contradictory basis follows existing indeterminate recovery. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-7H.7.4 — reread_mode_assignment_record [proposed]: May reference a committed assignment. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-7H.8.1 — manual_reread_compatibility_record [proposed]: May reference qualifying manual compatibility. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.3.3 — RR2 — Instruction and context snapshot | Mode-slot ID. | Binds snapshot to record. | Typed mode basis. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.3.4 — RR3 — Execution and acceptance
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — A mouth proposal from the committed snapshot followed by the existing independent acceptance check. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — Target and committed context snapshot. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Sends accepted material or a genuinely warranted honest insufficient_context fallback to RR4; records each distinct rejection and keeps rejected proposals out of readings. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — Accepted reading material or an honest failure outcome. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Convert rejection into a reading or silently relabel it insufficient_context. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Mouth/system failure is technical-failed with claim resumable; rejection is substantive-terminal subject only to the separately accepted bounded retry rule. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.3 — B10 reread transaction boundaries: Uses the committed snapshot and normal acceptance. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Gated by: DESIGNED — C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): Proposal must pass independent acceptance. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Gated by: ACCEPTED — C-7G.9 — B9 acceptance retry and fallback boundary: Careful retry and fallback retain their exact owner. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.3 — B10 reread transaction boundaries | Snapshot. | Proposes and checks. | Honest accepted/rejected result. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.3.5 — RR4 — Layer commit
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The commit point for one new quarantine reading and its external layer record. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — A claim without a prior layer and validated reading material. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Compare-and-commits against the claim, writes through the normal validated quarantine path using existing idempotency_key/reads/derived_from/produced_by, and binds the claim terminal to durable layer evidence. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — One new reading plus reread_layer_record [proposed] beside untouched history. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Target any existing reading for overwrite, edit, deletion, movement or replacement. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Write failure is technical-failed; duplicate idempotency recovers the existing reading_id and completes only the missing layer record. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.3 — B10 reread transaction boundaries: Requires validated material and no earlier claim layer. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Gated by: ACCEPTED — C-7H.2.3 — reread_reading_idempotency_key [proposed]: Uses the stable reread reading key. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Changes: ACCEPTED — C-7H.2.5 — reread_layer_record [proposed]: Appends the external layer trail. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.3 — B10 reread transaction boundaries | Validated material. | Appends reading and trail. | New layer only. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.3.6 — RR5 — Reread parent terminal
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Exactly one durable terminal log per reread_operation_id [proposed] after children resolve. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Takes in: ACCEPTED — Truthful committed child outcomes. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Does: ACCEPTED — Appends reread_committed, reread_duplicate_absorbed, reread_rejected, reread_interrupted, reread_blocked_held or reread_indeterminate before acknowledgement. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Gives out: ACCEPTED — A single durable parent outcome. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Must never: ACCEPTED — Acknowledge before the terminal or invent a second terminal type for mode-slot failures. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Resumable conditions keep RR5 unwritten until truthful resolution; missing terminal is recovered from durable evidence. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.3 — B10 reread transaction boundaries: Children must truthfully resolve first. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.2.4 — reread_operation_id [proposed] | Resolved children. | Closes parent truthfully. | No premature acknowledgement. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |
| 2 · ACCEPTED | C-7H.3 — B10 reread transaction boundaries | Resolved outcomes. | Appends terminal. | Durable response basis. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |
| 3 · ACCEPTED | C-7H.6.6 — reread_terminal [proposed] | Resolved parent. | Appends single terminal. | No early response. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.3.7 — RR-PR — Post-commit indexes and coverage
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — Rebuildable view/index material consuming the new layer. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — The committed reading and layer trail. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Updates or rebuilds derived indexes idempotently, including newest-usable surfacing. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — Derived coverage/index material. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Gate committed success or become status authority. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Failed derived material is rebuilt idempotently. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.3 — B10 reread transaction boundaries: Derived indexes follow committed layer evidence. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.3 — B10 reread transaction boundaries | Committed layer. | Updates coverage. | No status authority. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |
| 2 · DESIGNED | C-7I — View Layer (§7I) | Readings in creation order with acceptance/usability status. | Supplies the new layer for newest-usable surfacing through the proposed RR-PR post-commit view/index material, without changing authoritative commitment. | Nothing in this card. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [V10 §7I] [MAP C-7I] |

SUB-PARTS: NONE

### C-7H.4 — B10 eight duplicate-prevention points
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The identity boundaries preventing extra triggers, claims, layers or logs. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — Durable trigger, claim, reading, parent, child and recovery identities. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Enforces one record at each named boundary and lookup-first recovery. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — Convergent repeated requests without duplicate layers. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Treat duplicate execution as a new reread. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Conflicting evidence remains indeterminate rather than guessed. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.4.1 — One record per trigger occurrence: Uses unique trigger occurrence identity. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7H.4.2 — One canonical claim per root and trigger: Uses canonical claim identity. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7H.4.3 — Single-winner reread claim admission: Uses atomic claim admission. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7H.4.4 — One reread reading per claim: Uses the reading idempotency key. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7H.4.5 — One layer trail per claim: Uses one external layer record. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7H.4.6 — One reread parent terminal: Uses one parent terminal. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7H.4.7 — One reread child log: Uses one child log. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7H.4.8 — Reread recovery-run identity: Uses recovery identity and lookup first. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7H — Reread Lifecycle (§7H) | Canonical keys. | Enforces uniqueness. | No duplicate layers. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7H.4.1 — One record per trigger occurrence | Trigger identity. | Prevents duplicates. | Canonical occurrence. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-7H.4.2 — One canonical claim per root and trigger | Root/trigger. | Converges lookup. | One claim ever. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6] |
| 4 · ACCEPTED | C-7H.4.3 — Single-winner reread claim admission | Race participants. | Rejects losing appends. | Exclusive claim. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6] |
| 5 · ACCEPTED | C-7H.4.4 — One reread reading per claim | Reading key. | Recovers existing reading. | One output. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6] |
| 6 · ACCEPTED | C-7H.4.5 — One layer trail per claim | Durable reading. | Completes once. | One trail. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6] |
| 7 · ACCEPTED | C-7H.4.6 — One reread parent terminal | Parent ID. | Reuses committed terminal. | No duplicate closure. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6] |
| 8 · ACCEPTED | C-7H.4.7 — One reread child log | Child ID. | Reuses existing log. | No duplicate evidence. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6] |
| 9 · ACCEPTED | C-7H.4.8 — Reread recovery-run identity | Recovery ID. | Converges effects. | No replayed writes. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6] |

SUB-PARTS: C-7H.4.1 — One record per trigger occurrence; C-7H.4.2 — One canonical claim per root and trigger; C-7H.4.3 — Single-winner reread claim admission; C-7H.4.4 — One reread reading per claim; C-7H.4.5 — One layer trail per claim; C-7H.4.6 — One reread parent terminal; C-7H.4.7 — One reread child log; C-7H.4.8 — Reread recovery-run identity

### C-7H.4.1 — One record per trigger occurrence
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Trigger-identity duplicate prevention. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — One actual trigger occurrence. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Preserves one append-only trigger record. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — A reusable trigger identity. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Duplicate the trigger to manufacture extra layers. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.4 — B10 eight duplicate-prevention points: One real trigger permits one record. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.4 — B10 eight duplicate-prevention points | Actual trigger. | Preserves one record. | No manufactured duplicate trigger. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.4.2 — One canonical claim per root and trigger
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Claim establishment convergence under reread_claim_key [proposed]. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — The same root/trigger pair. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Finds or establishes its one claim. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — One claim identity ever. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Mint a replacement claim for an identical pair. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.4 — B10 eight duplicate-prevention points: Claim uniqueness is permanent for the pair. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.2.2 — reread_claim_key [proposed] | Canonical pair. | Converges establishment. | No extra claim. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7H.4 — B10 eight duplicate-prevention points | Root/trigger. | Preserves one claim. | Convergent lookup. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.4.3 — Single-winner reread claim admission
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — RR1's compare-and-commit duplicate boundary. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — Concurrent claim attempts. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Admits exactly one winner; losers append nothing. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — One committed claim binding. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Admit multiple winners. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.4 — B10 eight duplicate-prevention points: Atomic claim admits one winner. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.4 — B10 eight duplicate-prevention points | Competing requests. | Admits one winner. | No race duplicates. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.4.4 — One reread reading per claim
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Reading idempotency across every attempt under a claim. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — reread_reading_idempotency_key [proposed]. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Uses the existing reading idempotency field to recover the one result. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — At most one new reading. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Create an additional layer from a retry of the same claim. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.4 — B10 eight duplicate-prevention points: A repeated key cannot create another layer. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.2.3 — reread_reading_idempotency_key [proposed] | Reading key. | Absorbs duplicates. | No extra layer. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7H.4 — B10 eight duplicate-prevention points | Claim. | Preserves one reading. | No duplicate layer. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.4.5 — One layer trail per claim
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Claim-keyed external layer-record convergence. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — Durable reading evidence and claim identity. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Completes the one missing layer record idempotently. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — One layer record. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Duplicate the layer trail. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.4 — B10 eight duplicate-prevention points: Only missing layer evidence is appended. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.2.5 — reread_layer_record [proposed] | Claim evidence. | Absorbs repeats. | No duplicate trail. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7H.4 — B10 eight duplicate-prevention points | Claim and reading. | Completes once. | No duplicate trail. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.4.6 — One reread parent terminal
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — RR5 uniqueness under reread_operation_id [proposed]. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — The parent invocation identity. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Preserves exactly one terminal. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — One durable parent outcome. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Append a second terminal for repeated acknowledgement. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.4 — B10 eight duplicate-prevention points: Parent terminal is unique. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.4 — B10 eight duplicate-prevention points | Invocation ID. | Closes once. | No double acknowledgement record. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.4.7 — One reread child log
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Child-operation log uniqueness. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — One actual child operation ID. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Locates or appends its single log. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — One child log. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Log the same child twice. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.4 — B10 eight duplicate-prevention points: Child log is unique. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.4 — B10 eight duplicate-prevention points | Child ID. | Logs once. | No duplicated operation evidence. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.4.8 — Reread recovery-run identity
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — recovery_run_id with lookup-first repeated recovery. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — Existing committed state and recovery identity. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Makes repeated recovery a no-op returning recorded findings. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — Convergent recovery without repeated effects. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Reapply committed work. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Unreadable or contradictory evidence remains fail-closed. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.4 — B10 eight duplicate-prevention points: Recovery first reads committed state. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.4 — B10 eight duplicate-prevention points | Recovery state. | Reapplies nothing committed. | Idempotent recovery. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.5 — B10 recovery and fail-closed rules
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — Seventeen lookup-first recovery cases preserving claims, snapshots and earlier readings. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §8]
- Takes in: ACCEPTED — Durable evidence at the interruption or refusal point. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §8]
- Does: ACCEPTED — Resumes only missing work, reuses committed context and refuses unprovable or forbidden writes. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §8]
- Gives out: ACCEPTED — Honest committed, interrupted, refused, held or indeterminate status. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §8]
- Must never: ACCEPTED — Reconstruct missing sources, silently change snapshots, bypass privacy or overwrite history. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Unreadable/contradictory evidence blocks; source owners remain authoritative. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §8]

TOGETHER
- Fed by: ACCEPTED — C-7H.5.1 — B10 recovery 1 — Before claim: Handles preclaim interruption. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fed by: ACCEPTED — C-7H.5.2 — B10 recovery 2 — Claim without snapshot: Handles claim without snapshot. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fed by: ACCEPTED — C-7H.5.3 — B10 recovery 3 — Snapshot without output: Handles snapshot without output. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fed by: ACCEPTED — C-7H.5.4 — B10 recovery 4 — Reading without layer record: Handles reading without trail. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fed by: ACCEPTED — C-7H.5.5 — B10 recovery 5 — Layer without parent terminal: Handles missing parent terminal. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fed by: ACCEPTED — C-7H.5.6 — B10 recovery 6 — Terminal without acknowledgement: Handles missing acknowledgement. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fed by: ACCEPTED — C-7H.5.7 — B10 recovery 7 — Same-trigger duplicate: Handles same-trigger duplicate. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fed by: ACCEPTED — C-7H.5.8 — B10 recovery 8 — New trigger: Handles genuinely new trigger. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fed by: ACCEPTED — C-7H.5.16 — B10 recovery 16 — Duplicate recovery: Handles repeated recovery. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.5.9 — B10 recovery 9 — Unverifiable prior reading: Blocks unverifiable previous readings. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.5.10 — B10 recovery 10 — Unverifiable root: Blocks unverifiable root. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.5.11 — B10 recovery 11 — Retrieval failure: Keeps retrieval failures honest. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.5.12 — B10 recovery 12 — Access refusal: Respects access refusal. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.5.13 — B10 recovery 13 — Rejected proposal: Keeps rejected proposals separate. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.5.14 — B10 recovery 14 — Live hold: Honors live holds. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.5.15 — B10 recovery 15 — Claim race or contradiction: Handles claim races and contradictions. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.5.17 — B10 recovery 17 — Overwrite attempt: Refuses old-reading overwrite. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7H — Reread Lifecycle (§7H) | Durable evidence. | Resumes missing work. | No rewritten history. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |
| 2 · ACCEPTED | C-7H.5.1 — B10 recovery 1 — Before claim | Preclaim state. | Runs lookup next. | No false output. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-7H.5.2 — B10 recovery 2 — Claim without snapshot | Claim state. | Resumes only eligible work. | Honest interruption otherwise. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |
| 4 · ACCEPTED | C-7H.5.3 — B10 recovery 3 — Snapshot without output | Snapshot. | Reuses exact context. | Stable claim inputs. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |
| 5 · ACCEPTED | C-7H.5.4 — B10 recovery 4 — Reading without layer record | Idempotency evidence. | Appends missing trail. | No rewrite. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |
| 6 · ACCEPTED | C-7H.5.5 — B10 recovery 5 — Layer without parent terminal | Layer evidence. | Completes missing terminal. | Durable response. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |
| 7 · ACCEPTED | C-7H.5.6 — B10 recovery 6 — Terminal without acknowledgement | Terminal. | Returns recorded outcome. | No second terminal. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |
| 8 · ACCEPTED | C-7H.5.7 — B10 recovery 7 — Same-trigger duplicate | Claim evidence. | Absorbs or observes. | No duplicate reread. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |
| 9 · ACCEPTED | C-7H.5.8 — B10 recovery 8 — New trigger | New trigger record. | Starts distinct claim. | Old history intact. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |
| 10 · ACCEPTED | C-7H.5.9 — B10 recovery 9 — Unverifiable prior reading | Missing evidence. | Refuses/requires recovery. | No reconstruction. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |
| 11 · ACCEPTED | C-7H.5.10 — B10 recovery 10 — Unverifiable root | Unverifiable root. | Requires recovery. | No fabrication. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |
| 12 · ACCEPTED | C-7H.5.11 — B10 recovery 11 — Retrieval failure | Failure record. | Preserves technical failure. | No degraded guess. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |
| 13 · ACCEPTED | C-7H.5.12 — B10 recovery 12 — Access refusal | Access result. | Stops unauthorized work. | Protected visibility. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |
| 14 · ACCEPTED | C-7H.5.13 — B10 recovery 13 — Rejected proposal | Proposal defect. | Preserves rejection. | No false layer. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |
| 15 · ACCEPTED | C-7H.5.14 — B10 recovery 14 — Live hold | Hold evidence. | Waits on owner. | No bypass. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |
| 16 · ACCEPTED | C-7H.5.15 — B10 recovery 15 — Claim race or contradiction | Claim evidence. | Converges or stops. | Integrity preserved. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |
| 17 · ACCEPTED | C-7H.5.16 — B10 recovery 16 — Duplicate recovery | Existing findings. | Returns no-op. | Idempotence. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |
| 18 · ACCEPTED | C-7H.5.17 — B10 recovery 17 — Overwrite attempt | Write request. | Refuses violation. | Append-only history. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |

SUB-PARTS: C-7H.5.1 — B10 recovery 1 — Before claim; C-7H.5.2 — B10 recovery 2 — Claim without snapshot; C-7H.5.3 — B10 recovery 3 — Snapshot without output; C-7H.5.4 — B10 recovery 4 — Reading without layer record; C-7H.5.5 — B10 recovery 5 — Layer without parent terminal; C-7H.5.6 — B10 recovery 6 — Terminal without acknowledgement; C-7H.5.7 — B10 recovery 7 — Same-trigger duplicate; C-7H.5.8 — B10 recovery 8 — New trigger; C-7H.5.9 — B10 recovery 9 — Unverifiable prior reading; C-7H.5.10 — B10 recovery 10 — Unverifiable root; C-7H.5.11 — B10 recovery 11 — Retrieval failure; C-7H.5.12 — B10 recovery 12 — Access refusal; C-7H.5.13 — B10 recovery 13 — Rejected proposal; C-7H.5.14 — B10 recovery 14 — Live hold; C-7H.5.15 — B10 recovery 15 — Claim race or contradiction; C-7H.5.16 — B10 recovery 16 — Duplicate recovery; C-7H.5.17 — B10 recovery 17 — Overwrite attempt

### C-7H.5.1 — B10 recovery 1 — Before claim
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — Interruption before a reread claim exists. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Takes in: ACCEPTED — Any already-written trigger record. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Does: ACCEPTED — Leaves the harmless reusable trigger and next runs RR0 then RR1. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gives out: ACCEPTED — A clean claim attempt without rollback. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Must never: ACCEPTED — Invent produced output. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.5 — B10 recovery and fail-closed rules: Source evidence remains authoritative. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.5 — B10 recovery and fail-closed rules | Trigger evidence. | Restarts lookup. | Nothing fabricated. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.5.2 — B10 recovery 2 — Claim without snapshot
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — A committed claim with no context snapshot. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Takes in: ACCEPTED — Claim and mode-slot evidence. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Does: ACCEPTED — Resumes RR2 if the mode slot permits, or releases the claim with recorded cause as reread_interrupted. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gives out: ACCEPTED — A snapshot attempt or honest interruption with nothing produced. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Must never: ACCEPTED — Invent a mode or claim an output exists. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — A blocked mode slot prevents execution. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.5 — B10 recovery and fail-closed rules: Mode slot must permit RR2. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.5 — B10 recovery and fail-closed rules | Claim. | Resumes or interrupts. | Mode gate intact. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.5.3 — B10 recovery 3 — Snapshot without output
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — A committed snapshot with no reread output. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Takes in: ACCEPTED — The exact committed snapshot. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Does: ACCEPTED — Resumes RR3 from that snapshot or closes technical-failed. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gives out: ACCEPTED — An execution attempt using fixed context or technical failure. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Must never: ACCEPTED — Silently reassemble different context under the same claim. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Context remains bound to the snapshot. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.5 — B10 recovery and fail-closed rules: Committed context cannot change silently. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.5 — B10 recovery and fail-closed rules | Fixed snapshot. | Resumes execution. | No context replacement. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.5.4 — B10 recovery 4 — Reading without layer record
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — A durable reading whose external layer trail is absent. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Takes in: ACCEPTED — The reading's idempotency_key and claim. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Does: ACCEPTED — Recovers reading_id, completes the layer record idempotently and proceeds to RR5. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gives out: ACCEPTED — The missing layer trail. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Must never: ACCEPTED — Rewrite the reading. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Only durable matching identity proves the output. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.5 — B10 recovery and fail-closed rules: Durable reading identity proves the layer. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.5 — B10 recovery and fail-closed rules | Reading identity. | Completes layer record. | No reading rewrite. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.5.5 — B10 recovery 5 — Layer without parent terminal
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — A committed layer with missing RR5. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Takes in: ACCEPTED — Durable layer evidence. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Does: ACCEPTED — Appends the one missing parent terminal before acknowledgement. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gives out: ACCEPTED — A complete terminal record. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Must never: ACCEPTED — Re-execute the reread. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — No acknowledgement until the terminal is durable. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.5 — B10 recovery and fail-closed rules: Terminal must precede acknowledgement. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.5 — B10 recovery and fail-closed rules | Committed layer. | Completes RR5. | Acknowledgement gated. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.5.6 — B10 recovery 6 — Terminal without acknowledgement
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — A durable parent outcome not yet acknowledged. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Takes in: ACCEPTED — The recorded terminal. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Does: ACCEPTED — Returns that outcome without re-execution. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gives out: ACCEPTED — The existing terminal response. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Must never: ACCEPTED — Append a second terminal. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.5 — B10 recovery and fail-closed rules: Committed terminal absorbs recovery. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.5 — B10 recovery and fail-closed rules | Existing terminal. | Returns it. | No re-execution. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.5.7 — B10 recovery 7 — Same-trigger duplicate
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — Another request for the same root/trigger. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Takes in: ACCEPTED — Committed layer or live claim evidence. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Does: ACCEPTED — RR0 absorbs the committed layer as duplicate_absorbed or observes the live claim as reread_interrupted. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gives out: ACCEPTED — The one existing layer or claim status. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Must never: ACCEPTED — Create another layer. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.5 — B10 recovery and fail-closed rules: Same trigger retains one layer. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.5 — B10 recovery and fail-closed rules | Existing claim/layer. | Absorbs or observes. | One layer. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.5.8 — B10 recovery 8 — New trigger
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — A genuinely new recorded trigger for an existing root. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Takes in: ACCEPTED — The new trigger identity. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Does: ACCEPTED — Permits RR1 to establish a new claim and append its layer beside earlier ones. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gives out: ACCEPTED — A legitimate new-layer operation. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Must never: ACCEPTED — Modify prior layers. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Normal admission gates still apply. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.5 — B10 recovery and fail-closed rules: New trigger requires normal admission. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.5 — B10 recovery and fail-closed rules | New identity. | Permits normal claim. | New layer beside old. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.5.9 — B10 recovery 9 — Unverifiable prior reading
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — A previous-reading ID that cannot be verified. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Takes in: ACCEPTED — Missing or unreadable prior-reading evidence. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Does: ACCEPTED — Refuses the attempt as reread_rejected with cause, or uses indeterminate_recovery_required when the store itself is unreadable. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gives out: ACCEPTED — A recorded refusal or recovery-required state. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Must never: ACCEPTED — Reconstruct the prior reading. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Unprovable trigger evidence cannot bind the reread. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.5 — B10 recovery and fail-closed rules: Previous-reading evidence must be verifiable. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.5 — B10 recovery and fail-closed rules | Prior IDs. | Refuses or requires recovery. | No reconstructed evidence. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.5.10 — B10 recovery 10 — Unverifiable root
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — A missing or unreadable root identity. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Takes in: ACCEPTED — Root existence evidence from B11's authorities, read-only. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Does: ACCEPTED — Fails closed as indeterminate_recovery_required. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gives out: ACCEPTED — Recovery-required status. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Must never: ACCEPTED — Fabricate or re-ingest the missing root. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Root existence-by-identity is required. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.5 — B10 recovery and fail-closed rules: Root identity must exist. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.5 — B10 recovery and fail-closed rules | Root identity. | Requires recovery. | No fabricated root. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.5.11 — B10 recovery 11 — Retrieval failure
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — Retrieval timeout or degraded-context failure during reread assembly. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Takes in: ACCEPTED — The actual retrieval failure. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Does: ACCEPTED — Records technical-failed with the claim resumable; the retrieval owner governs stop/retry/degraded refinement. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gives out: ACCEPTED — Honest failure without silently degraded execution. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Must never: ACCEPTED — Continue silently with degraded context. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Retrieval failure remains failure. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.5 — B10 recovery and fail-closed rules: Failed retrieval cannot appear successful. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7F.7.3 — Accepted B26 stop-after-retry policy: Accepted retrieval policy governs bounded retry then stop. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.5 — B10 recovery and fail-closed rules | Retrieval outcome. | Stops technically. | No silent degradation. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.5.12 — B10 recovery 12 — Access refusal
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — Privacy or access refusal at the owning gate. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Takes in: ACCEPTED — The gate's refusal class and visibility limits. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Does: ACCEPTED — Refuses as reread_rejected unauthorized or blocks according to that class, logging under the gate's visibility rules. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gives out: ACCEPTED — A protected refusal/block record. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Must never: ACCEPTED — Bypass the gate or reveal protected refusal content. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — The gate's refusal stops unauthorized use. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.5 — B10 recovery and fail-closed rules: Owning gate refusal remains binding. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.5 — B10 recovery and fail-closed rules | Gate result. | Refuses under visibility rules. | No privacy bypass. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.5.13 — B10 recovery 13 — Rejected proposal
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — Malformed or otherwise rejected reread output. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Takes in: ACCEPTED — The acceptance check's distinct rejection reason. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Does: ACCEPTED — Records substantive-terminal and keeps the rejected proposal out of readings; honest fallback remains available only when genuinely warranted through its owner. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gives out: ACCEPTED — A rejection record with no relabeled reading. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Must never: ACCEPTED — Convert rejection into insufficient_context merely to complete the operation. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — The rejected proposal never becomes a reading. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.5 — B10 recovery and fail-closed rules: Acceptance rejection cannot commit a reading. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.5 — B10 recovery and fail-closed rules | Rejection reason. | Records substantive terminal. | No relabeled reading. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.5.14 — B10 recovery 14 — Live hold
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — A live B-HOLD on the root or its readings. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Takes in: ACCEPTED — The owning hold state. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Does: ACCEPTED — Uses dependency_blocked_held at RR1/RR2 and waits for the hold owner's verified release interface. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gives out: ACCEPTED — A blocked reread. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Must never: ACCEPTED — Proceed or queue around the hold. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — No claim proceeds while the hold is live. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.5 — B10 recovery and fail-closed rules: Live hold blocks RR1/RR2. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.5 — B10 recovery and fail-closed rules | Hold state. | Blocks claim/execution. | Owner release required. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.5.15 — B10 recovery 15 — Claim race or contradiction
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — Concurrent attempts or contradictory claim evidence. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Takes in: ACCEPTED — RR1 competitors and durable claim state. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Does: ACCEPTED — Admits one compare-and-commit winner; losers append nothing; contradictory evidence becomes indeterminate_recovery_required. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gives out: ACCEPTED — One winner or an honest integrity block. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Must never: ACCEPTED — Guess between contradictory claims. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Contradictory evidence fails closed. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.5 — B10 recovery and fail-closed rules: One winner only; contradictions block. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.5 — B10 recovery and fail-closed rules | Claim evidence. | Admits one or blocks. | No guessed winner. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.5.16 — B10 recovery 16 — Duplicate recovery
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — A repeat recovery_run_id over committed evidence. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Takes in: ACCEPTED — The existing recovery and state records. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Does: ACCEPTED — Re-reads state and reapplies nothing. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gives out: ACCEPTED — A recovery no-op. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Must never: ACCEPTED — Repeat committed effects. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.5 — B10 recovery and fail-closed rules: Recovery never repeats committed effects. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.5 — B10 recovery and fail-closed rules | Committed findings. | Returns no-op. | No repeated effects. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.5.17 — B10 recovery 17 — Overwrite attempt
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — A forbidden path targeting an existing reading record. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Takes in: ACCEPTED — An attempted overwrite, edit, deletion or replacement. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Does: ACCEPTED — Refuses and logs a fail-closed violation. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Gives out: ACCEPTED — A violation record with all prior readings untouched. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Must never: ACCEPTED — Write into, edit, delete or replace an existing reading. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Only a new reading and layer record may be appended. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.5 — B10 recovery and fail-closed rules: Existing readings cannot be targets of mutation. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.5 — B10 recovery and fail-closed rules | Forbidden write. | Logs violation. | History preserved. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.6 — B10 operational logging
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — One append-only log per real child and one parent terminal, distinct from canonical state records. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Takes in: ACCEPTED — Trigger, claim, snapshot, acceptance, layer and recovery operations. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Does: ACCEPTED — Logs each under its own identity with parent references; records and logs remain machine facts rather than truth votes. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Gives out: ACCEPTED — A protected linked operational trail. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Must never: ACCEPTED — Log about logging, duplicate seam evidence or treat a new layer as proof the old one was wrong. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Privacy authorization governs every record, including privacy-block logs. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy authorization governs every record, including privacy-block logs. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Changes: ACCEPTED — C-7H.6.1 — reread_trigger_recorded [proposed]: Logs real trigger recording. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Changes: ACCEPTED — C-7H.6.2 — Reread claim events: Logs actual claim resolution. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Changes: ACCEPTED — C-7H.6.3 — reread_snapshot_committed [proposed]: Logs committed snapshot. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Changes: ACCEPTED — C-7H.6.4 — reread_acceptance_result [proposed]: Logs acceptance result. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Changes: ACCEPTED — C-7H.6.5 — reread_layer_committed [proposed]: Logs layer commitment. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Changes: ACCEPTED — C-7H.6.6 — reread_terminal [proposed]: Logs the single parent terminal. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Changes: ACCEPTED — C-7H.6.7 — B10 recovery and failure events: Logs recovery/failure resolution. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7H — Reread Lifecycle (§7H) | Operation outcomes. | Appends owned logs. | Auditable execution. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |
| 2 · ACCEPTED | C-7H.6.1 — reread_trigger_recorded [proposed] | Trigger op ID. | Appends once. | No duplicate evidence. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |
| 3 · ACCEPTED | C-7H.6.2.1 — reread_claim_committed [proposed] | Durable winning claim. | Logs once. | No false winner. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |
| 4 · ACCEPTED | C-7H.6.2.2 — reread_claim_absorbed [proposed] | Existing claim. | Logs absorption. | No false creation. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |
| 5 · ACCEPTED | C-7H.6.3 — reread_snapshot_committed [proposed] | Durable snapshot. | Logs once. | No fabricated coverage. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |
| 6 · ACCEPTED | C-7H.6.4 — reread_acceptance_result [proposed] | Actual outcome. | Logs without duplicating evidence. | Reason distinctions retained. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |
| 7 · ACCEPTED | C-7H.6.5 — reread_layer_committed [proposed] | Committed layer. | Logs once. | No double truth vote. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |
| 8 · ACCEPTED | C-7H.6.7.1 — recovery_applied [proposed] | Recovery identity. | Records applied work. | No replay. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |
| 9 · ACCEPTED | C-7H.6.7.2 — recovery_noop [proposed] | Recovery identity. | Records no-op. | No repeated effects. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |
| 10 · ACCEPTED | C-7H.6.7.3 — fail_closed_event [proposed] | Actual violation. | Logs under child identity. | No substituted RR5. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |

SUB-PARTS: C-7H.6.1 — reread_trigger_recorded [proposed]; C-7H.6.2 — Reread claim events; C-7H.6.3 — reread_snapshot_committed [proposed]; C-7H.6.4 — reread_acceptance_result [proposed]; C-7H.6.5 — reread_layer_committed [proposed]; C-7H.6.6 — reread_terminal [proposed]; C-7H.6.7 — B10 recovery and failure events

### C-7H.6.1 — reread_trigger_recorded [proposed]
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — The proposed operational event for a complete trigger record. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Takes in: ACCEPTED — The actual trigger-record operation. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Does: ACCEPTED — Logs it once. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Gives out: ACCEPTED — reread_trigger_recorded [proposed]. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Must never: ACCEPTED — Duplicate the operation log. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.6 — B10 operational logging: Logs only the real trigger operation. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.6 — B10 operational logging | Trigger operation. | Appends once. | Trigger audit. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.6.2 — Reread claim events
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Proposed reread_claim_committed and reread_claim_absorbed events. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Takes in: ACCEPTED — RR1 winner or RR0 absorption. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Does: ACCEPTED — Records the actual claim resolution once. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Gives out: ACCEPTED — The matching claim event. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Must never: ACCEPTED — Report a losing attempt as a committed winner. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7H.6.2.1 — reread_claim_committed [proposed]: Records a claim winner. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Changes: ACCEPTED — C-7H.6.2.2 — reread_claim_absorbed [proposed]: Records existing-claim absorption. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.6 — B10 operational logging | Claim outcome. | Selects matching event. | Claim audit. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |

SUB-PARTS: C-7H.6.2.1 — reread_claim_committed [proposed]; C-7H.6.2.2 — reread_claim_absorbed [proposed]

### C-7H.6.2.1 — reread_claim_committed [proposed]
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Proposed log of the RR1 winning claim operation. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Takes in: ACCEPTED — Committed claim evidence. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Does: ACCEPTED — Logs the winner once. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Gives out: ACCEPTED — reread_claim_committed [proposed]. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Must never: ACCEPTED — Log a loser as winner. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.6 — B10 operational logging: Only the claim winner is committed. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.6.2 — Reread claim events | Commit evidence. | Logs committed. | No false winner. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.6.2.2 — reread_claim_absorbed [proposed]
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Proposed log of RR0 claim absorption. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Takes in: ACCEPTED — The existing claim/result. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Does: ACCEPTED — Logs the actual absorption once. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Gives out: ACCEPTED — reread_claim_absorbed [proposed]. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Must never: ACCEPTED — Imply a new layer was created. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.6 — B10 operational logging: Absorption has no new layer. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.6.2 — Reread claim events | Absorption evidence. | Logs absorbed. | No new-layer claim. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.6.3 — reread_snapshot_committed [proposed]
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — The proposed event for an RR2 snapshot with honest coverage. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Takes in: ACCEPTED — The durable context snapshot. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Does: ACCEPTED — Logs the snapshot operation once. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Gives out: ACCEPTED — reread_snapshot_committed [proposed]. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Must never: ACCEPTED — Claim nonexistent context coverage. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.6 — B10 operational logging: Snapshot coverage must be honest. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.6 — B10 operational logging | Snapshot. | Records honest coverage. | Context audit. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.6.4 — reread_acceptance_result [proposed]
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — The proposed event carrying the RR3 outcome. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Takes in: ACCEPTED — Pass, honest fallback or distinct rejection reason from acceptance. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Does: ACCEPTED — Records the outcome while leaving the acceptance owner's records separate. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Gives out: ACCEPTED — reread_acceptance_result [proposed]. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Must never: ACCEPTED — Duplicate acceptance evidence or erase rejection distinctions. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.6 — B10 operational logging: Acceptance records remain distinct. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.6 — B10 operational logging | Outcome/reason. | Preserves distinction. | Acceptance audit. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.6.5 — reread_layer_committed [proposed]
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — One proposed log for the reading append and layer record together. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Takes in: ACCEPTED — RR4's durable commit. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Does: ACCEPTED — Records the layer commit as one actual operation. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Gives out: ACCEPTED — reread_layer_committed [proposed]. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Must never: ACCEPTED — Count reading and layer trail as two independent truth votes. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.6 — B10 operational logging: Layer append is one actual operation. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.6 — B10 operational logging | Reading and trail. | Logs once together. | Layer audit. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.6.6 — reread_terminal [proposed]
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — The proposed RR5 parent event. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Takes in: ACCEPTED — The truthfully resolved operation. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Does: ACCEPTED — Records the single parent terminal before acknowledgement. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Gives out: ACCEPTED — reread_terminal [proposed] with the existing terminal value. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Must never: ACCEPTED — Acknowledge first or append another terminal. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Missing terminal prevents acknowledgement. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.3.6 — RR5 — Reread parent terminal: RR5 is required before acknowledgement. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.6 — B10 operational logging | Resolved operation. | Closes before acknowledgement. | Durable parent audit. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.6.7 — B10 recovery and failure events
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Proposed recovery_applied, recovery_noop and fail_closed_event records. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Takes in: ACCEPTED — Recovery resolutions and every fail-closed occurrence, including overwrite violations. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Does: ACCEPTED — Records the actual resolution under its own child/recovery identity. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Gives out: ACCEPTED — One applicable event per real operation. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Must never: ACCEPTED — Substitute a child failure log for RR5. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Required parent resolution remains separate. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7H.6.7.1 — recovery_applied [proposed]: Records real applied recovery. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Changes: ACCEPTED — C-7H.6.7.2 — recovery_noop [proposed]: Records no-op recovery. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Changes: ACCEPTED — C-7H.6.7.3 — fail_closed_event [proposed]: Records the actual closed boundary. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.6 — B10 operational logging | Actual condition. | Uses matching event. | Protected recovery audit. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |
| 2 · ACCEPTED | C-7H.8.7 — Compatibility operation events | Actual condition. | Logs owned event. | RR5 remains distinct. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §11] |

SUB-PARTS: C-7H.6.7.1 — recovery_applied [proposed]; C-7H.6.7.2 — recovery_noop [proposed]; C-7H.6.7.3 — fail_closed_event [proposed]

### C-7H.6.7.1 — recovery_applied [proposed]
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed shared event for real recovery work. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Takes in: ACCEPTED — The actual recovery resolution and operation identity. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Does: ACCEPTED — Logs the applied recovery once under its owning child/recovery identity. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Gives out: ACCEPTED — recovery_applied [proposed]. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Must never: ACCEPTED — Duplicate committed recovery effects or evidence. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.6 — B10 operational logging: Actual recovery work is logged once. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.6.7 — B10 recovery and failure events | Recovery effects. | Logs once. | Recovery trace. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |
| 2 · ACCEPTED | C-7H.9.7 — B9 operational event set | Actual recovery. | Logs once. | No duplicate effects. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.6.7.2 — recovery_noop [proposed]
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed shared event for a lookup-first recovery requiring no new effects. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Takes in: ACCEPTED — Already-committed findings. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Does: ACCEPTED — Records the no-op once for the real recovery operation. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Gives out: ACCEPTED — recovery_noop [proposed]. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Must never: ACCEPTED — Reapply completed work. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.6 — B10 operational logging: Existing findings produce no-op logging. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.6.7 — B10 recovery and failure events | Existing state. | Logs no-op. | No repeated effects. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |
| 2 · ACCEPTED | C-7H.9.7 — B9 operational event set | Existing state. | Logs no-op. | No replay. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.6.7.3 — fail_closed_event [proposed]
Stamp: ACCEPTED    Source: [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — The proposed shared child/recovery log for an actual fail-closed condition. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Takes in: ACCEPTED — The exact refusal or integrity condition and its reason. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Does: ACCEPTED — Logs that condition under its own operation identity. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Gives out: ACCEPTED — fail_closed_event [proposed]. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Must never: ACCEPTED — Substitute it for the required parent terminal. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — A truthful parent terminal remains required before acknowledgement. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.6 — B10 operational logging: Child failure logs remain distinct from parent closure. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.6.7 — B10 recovery and failure events | Failure cause. | Logs child/recovery event. | RR5 remains separate. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |
| 2 · ACCEPTED | C-7H.9.7 — B9 operational event set | Actual violation/refusal. | Logs child result. | Parent remains distinct. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.7 — A25 semantic reread assignment
Stamp: ACCEPTED    Source: [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5] [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Two independently tested relationships between new information and an existing reading. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5] [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §6]
- Takes in: ACCEPTED — Actual direct bearing or material surrounding-context change. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5] [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §6]
- Does: ACCEPTED — Assigns direct, wider-context or both when their respective relationships truthfully apply. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5] [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §6]
- Gives out: ACCEPTED — A reason-bearing semantic assignment, never a third mode. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5] [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §6]
- Must never: ACCEPTED — Treat the relationships as mutually exclusive, substitute a mode for a reason or grant blanket rereading permission. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5] [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Neither relationship means no A25 assignment; no detector, threshold or materiality metric is invented. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5] [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-7H.7.1 — Direct reread relationship: Tests direct bearing independently. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-7H.7.2 — Wider-context reread relationship: Tests surrounding change independently. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-7H.7.3 — A25 dual assignment: Records both genuine relationships. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5]
- Gated by: ACCEPTED — C-7H.7.5 — Assignment commit and snapshot binding: Commits before snapshot once. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7H.7.6 — Assignment-specific checks with broad context: Uses broad relevant context for each mode. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.7.7 — Assignment failure consumption: Rejects invalid assignment evidence. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7H.7.8 — Assignment recovery: Recovers by exact reuse. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Changes: ACCEPTED — C-7H.7.4 — reread_mode_assignment_record [proposed]: Carries the assignment canonically. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7H — Reread Lifecycle (§7H) | New-information bearing. | Assigns semantic reasons. | No manufactured mode. | [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5] |
| 2 · ACCEPTED | C-7H.7.1 — Direct reread relationship | Actual bearing. | Tests independently. | Truthful mode. | [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5] |
| 3 · ACCEPTED | C-7H.7.2 — Wider-context reread relationship | Actual change. | Tests independently. | Truthful mode. | [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5] |
| 4 · ACCEPTED | C-7H.7.3 — A25 dual assignment | Dual evidence. | Keeps both meanings. | One semantic pair. | [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5] |
| 5 · ACCEPTED | C-7H.7.5 — Assignment commit and snapshot binding | Record inputs. | Commits once. | Immutable basis. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §6] |
| 6 · ACCEPTED | C-7H.7.6 — Assignment-specific checks with broad context | Assignment. | Uses all safe relevant material. | No context suppression by mode. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §7] |
| 7 · ACCEPTED | C-7H.11.7 — Relevance versus A25 assignment boundary | Actual relationship evidence. | Separates assignment from relevance. | No new assignment producer. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |

SUB-PARTS: C-7H.7.1 — Direct reread relationship; C-7H.7.2 — Wider-context reread relationship; C-7H.7.3 — A25 dual assignment; C-7H.7.4 — reread_mode_assignment_record [proposed]; C-7H.7.5 — Assignment commit and snapshot binding; C-7H.7.6 — Assignment-specific checks with broad context; C-7H.7.7 — Assignment failure consumption; C-7H.7.8 — Assignment recovery

### C-7H.7.1 — Direct reread relationship
Stamp: ACCEPTED    Source: [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — New information directly changes, corrects, limits or contradicts the old reading itself. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5]
- Takes in: ACCEPTED — Evidence bearing on the reading's own content. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5]
- Does: ACCEPTED — Assigns direct when that relationship exists. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5]
- Gives out: ACCEPTED — The direct mode, possibly alongside wider-context. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5]
- Must never: ACCEPTED — Assign direct without its actual relationship. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.7 — A25 semantic reread assignment: Only the direct relationship permits direct. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7 — A25 semantic reread assignment | New evidence. | Assigns direct truthfully. | No forced mode. | [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.7.2 — Wider-context reread relationship
Stamp: ACCEPTED    Source: [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — New information may materially change the surrounding meaning or context of the old reading. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5]
- Takes in: ACCEPTED — Actual surrounding-context change, with or without direct contradiction. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5]
- Does: ACCEPTED — Assigns wider-context independently of direct bearing. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5]
- Gives out: ACCEPTED — The wider-context mode, possibly alongside direct. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5]
- Must never: ACCEPTED — Require absence of direct bearing or invent a materiality threshold. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.7 — A25 semantic reread assignment: Only material surrounding change permits wider-context. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7 — A25 semantic reread assignment | Context change. | Assigns wider-context truthfully. | Overlap remains possible. | [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.7.3 — A25 dual assignment
Stamp: ACCEPTED    Source: [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — Both existing relationships applying in one real case. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §8]
- Takes in: ACCEPTED — Truthful direct and wider-context evidence. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §8]
- Does: ACCEPTED — Records both within one trigger, claim, snapshot, proposal path and at most one new layer. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §8]
- Gives out: ACCEPTED — One dual-assigned reread operation. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §8]
- Must never: ACCEPTED — Create a third semantic mode, hide either relationship or create two readings merely because both apply. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Normal one-claim and reading-idempotency limits remain active. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.7 — A25 semantic reread assignment: Both relationships must actually hold. [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7 — A25 semantic reread assignment | Both evidence relationships. | Uses one dual operation. | No third mode. | [04/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.7.4 — reread_mode_assignment_record [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — A proposed immutable append-only assignment record per reread claim. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Takes in: ACCEPTED — Stable identity, assigned_modes [proposed], claim and trigger references, reason, per-mode evidence, time and schema version. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Does: ACCEPTED — Carries only the accepted semantic assignment in canonical form; reread_mode_ref [proposed] points to its identity. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Gives out: ACCEPTED — One bound assignment record. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Must never: ACCEPTED — Edit a committed assignment or invent the still-open assignment producer. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Only the three canonical nonempty forms are valid. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]

TOGETHER
- Fed by: ACCEPTED — C-7H.7.4.1 — mode_assignment_id [proposed]: Carries stable record ID. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-7H.7.4.2 — assigned_modes [proposed]: Carries one canonical list. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-7H.7.4.3 — Assignment reread_claim_ref [proposed]: Binds the committed claim. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-7H.7.4.4 — Assignment trigger_record_ref [proposed]: Binds the actual trigger. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-7H.7.4.5 — assignment_reason [proposed]: Requires nonempty reason. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-7H.7.4.6 — mode_evidence [proposed]: Requires evidence for each mode. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-7H.7.4.7 — assigned_at [proposed]: Carries assignment time. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-7H.7.4.8 — Assignment schema_version [proposed]: Carries schema revision. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.3.3.1 — reread_mode_ref [proposed] | Assignment identity. | Consumes its typed basis. | Truthful A25 mode slot. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5] |
| 2 · ACCEPTED | C-7H.7 — A25 semantic reread assignment | Truthful assignment. | Creates immutable record. | Bound mode-slot basis. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5] |

SUB-PARTS: C-7H.7.4.1 — mode_assignment_id [proposed]; C-7H.7.4.2 — assigned_modes [proposed]; C-7H.7.4.3 — Assignment reread_claim_ref [proposed]; C-7H.7.4.4 — Assignment trigger_record_ref [proposed]; C-7H.7.4.5 — assignment_reason [proposed]; C-7H.7.4.6 — mode_evidence [proposed]; C-7H.7.4.7 — assigned_at [proposed]; C-7H.7.4.8 — Assignment schema_version [proposed]

### C-7H.7.4.1 — mode_assignment_id [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The proposed stable assignment-record identity. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Takes in: ACCEPTED — The committed assignment record. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Does: ACCEPTED — Supplies the identity carried by reread_mode_ref [proposed]. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Gives out: ACCEPTED — mode_assignment_id [proposed]. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7.4 — reread_mode_assignment_record [proposed] | Identity. | Binds reference. | Exact assignment pointer. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.7.4.2 — assigned_modes [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — A proposed nonempty ordered list with direct before wider-context. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Takes in: ACCEPTED — Exactly ["direct"], ["wider-context"] or ["direct", "wider-context"]. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Does: ACCEPTED — Stores one canonical form for each valid assignment. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Gives out: ACCEPTED — assigned_modes [proposed]. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Must never: ACCEPTED — Store reversed order, duplicates, an empty list, free text, renamed modes or a third mode. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Invalid forms follow assignment_malformed [proposed], assignment_empty [proposed] or assignment_unknown_mode [proposed] as applicable. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7.4 — reread_mode_assignment_record [proposed] | Assigned modes. | Checks exact form. | No ambiguous encoding. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.7.4.3 — Assignment reread_claim_ref [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The proposed reference to the committed root/trigger claim. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Takes in: ACCEPTED — Existing reread_claim_key [proposed]. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Does: ACCEPTED — Binds assignment to that one claim. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Gives out: ACCEPTED — reread_claim_ref [proposed]. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Must never: ACCEPTED — Create an assignment without a committed claim. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — No claim means no assignment. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7.4 — reread_mode_assignment_record [proposed] | Claim ref. | Preserves claim scope. | No unclaimed assignment. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.7.4.4 — Assignment trigger_record_ref [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The proposed reference to the claim's existing trigger record. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Takes in: ACCEPTED — The full B10 trigger identity. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Does: ACCEPTED — Preserves the trigger binding by reference. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Gives out: ACCEPTED — trigger_record_ref [proposed]. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Must never: ACCEPTED — Contradict the trigger's evidence. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Contradictory binding fails closed. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7.4 — reread_mode_assignment_record [proposed] | Trigger ref. | Preserves reason provenance. | No contradictory basis. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.7.4.5 — assignment_reason [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The proposed required, nonempty real reason the assignment applies. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Takes in: ACCEPTED — The actual assignment reason. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Does: ACCEPTED — Records why the relationship holds. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Gives out: ACCEPTED — assignment_reason [proposed]. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Must never: ACCEPTED — Use a mode name instead of a reason or leave it empty. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Missing required content is malformed. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7.4 — reread_mode_assignment_record [proposed] | Actual reason. | Records why. | No mode as reason. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.7.4.6 — mode_evidence [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — Proposed references showing each listed mode's relationship. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Takes in: ACCEPTED — Evidence references for every assigned mode; the same evidence may support both. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Does: ACCEPTED — Carries references only, never copies. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Gives out: ACCEPTED — mode_evidence [proposed]. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Must never: ACCEPTED — List a mode without its truthful evidence relationship. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Invalid or contradictory evidence follows the fail-closed assignment path. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7.4 — reread_mode_assignment_record [proposed] | Evidence refs. | Preserves relationship basis. | No manufactured assignment. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.7.4.7 — assigned_at [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The proposed assignment timestamp. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Takes in: ACCEPTED — Assignment time. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Does: ACCEPTED — Records that timestamp. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Gives out: ACCEPTED — assigned_at [proposed]. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7.4 — reread_mode_assignment_record [proposed] | Timestamp. | Records time. | Temporal provenance. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.7.4.8 — Assignment schema_version [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The proposed assignment-record schema revision. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Takes in: ACCEPTED — The schema version used. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Does: ACCEPTED — Records the record's form version. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Gives out: ACCEPTED — schema_version [proposed]. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7.4 — reread_mode_assignment_record [proposed] | Version. | Records form. | Schema provenance. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.7.5 — Assignment commit and snapshot binding
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — One atomic assignment commit before RR2's context snapshot. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §6]
- Takes in: ACCEPTED — A committed claim/trigger and truthful assignment content. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §6]
- Does: ACCEPTED — Uses proposed mode_assignment_key = stable_hash(reread_claim_key + "mode_assignment_v1"); identical repeats converge and the snapshot references mode_assignment_id [proposed]. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §6]
- Gives out: ACCEPTED — Exactly one immutable assignment for the claim. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §6]
- Must never: ACCEPTED — Recalculate, overwrite, merge or delete a committed assignment; a genuinely changed situation needs a new trigger and claim. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Different repeat content is refused and surfaced as conflicting evidence. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.7 — A25 semantic reread assignment: Claim and truthful assignment precede snapshot. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7 — A25 semantic reread assignment | Claim and assignment. | Binds atomically. | No recalculation. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7H.8.3 — Compatibility commit and exclusivity | Assignment evidence. | Refuses cross-type commit. | No both-types permission. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §7] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.7.6 — Assignment-specific checks with broad context
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §7] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — Each assignment's check within the broadest safely available clearly relevant context. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §7] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §8]
- Takes in: ACCEPTED — Authorized relevant context and the actual assignment. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §7] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §8]
- Does: ACCEPTED — Direct checks the old reading against direct new information; wider-context checks surrounding-story change; dual performs both in one operation. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §7] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §8]
- Gives out: ACCEPTED — One context-rich reread proposal path. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §7] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §8]
- Must never: ACCEPTED — Deliberately narrow context by mode, include unrelated information or bypass privacy, integrity, holding, authorization, relevance or safety. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §7] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Existing bounds and retrieval failure rules remain active; no numeric rule is created. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §7] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.7 — A25 semantic reread assignment: Mode explains checks, not narrower context. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7 — A25 semantic reread assignment | Authorized context. | Runs required checks. | No deliberate narrowing. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.7.7 — Assignment failure consumption
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Seven reason-bearing RR2 failures using existing B10 states and terminals. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Takes in: ACCEPTED — Missing, unreadable, malformed, empty, unknown, duplicated or contradictory assignment evidence. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Does: ACCEPTED — Emits fail_closed_event [proposed] as a child/recovery log; uses reread_blocked_held or reread_indeterminate only when the operation truthfully terminates. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Gives out: ACCEPTED — An honest existing parent terminal or a still-resumable state. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Must never: ACCEPTED — Invent a new terminal, confuse child logs with RR5 or acknowledge before durable terminal. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Resumable conditions leave RR5 unwritten until truthful resolution. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.7.7.1 — assignment_missing [proposed]: Handles absent assignment. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7H.7.7.2 — assignment_unreadable [proposed]: Handles unreadable assignment. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7H.7.7.3 — assignment_malformed [proposed]: Handles malformed assignment. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7H.7.7.4 — assignment_empty [proposed]: Handles empty mode list. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7H.7.7.5 — assignment_unknown_mode [proposed]: Handles unknown mode. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7H.7.7.6 — assignment_duplicated [proposed]: Handles duplicate commitments. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7H.7.7.7 — assignment_contradictory [proposed]: Handles conflicting evidence. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7 — A25 semantic reread assignment | Record condition. | Uses existing states. | No fabricated mode. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] |
| 2 · ACCEPTED | C-7H.7.7.1 — assignment_missing [proposed] | Missing evidence. | Records held state. | Truthful terminal timing. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] |
| 3 · ACCEPTED | C-7H.7.7.2 — assignment_unreadable [proposed] | Unreadable record. | Records recovery state. | Truthful terminal timing. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] |
| 4 · ACCEPTED | C-7H.7.7.3 — assignment_malformed [proposed] | Malformed record. | Preserves evidence. | No in-place repair. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] |
| 5 · ACCEPTED | C-7H.7.7.4 — assignment_empty [proposed] | Empty assignment. | Records recovery state. | No manufactured default. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] |
| 6 · ACCEPTED | C-7H.7.7.5 — assignment_unknown_mode [proposed] | Unknown name. | Records recovery state. | No renamed mode. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] |
| 7 · ACCEPTED | C-7H.7.7.6 — assignment_duplicated [proposed] | Duplicate records. | Records integrity stop. | No picked winner. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] |
| 8 · ACCEPTED | C-7H.7.7.7 — assignment_contradictory [proposed] | Contradictory evidence. | Records and surfaces. | No auto-repair. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] |

SUB-PARTS: C-7H.7.7.1 — assignment_missing [proposed]; C-7H.7.7.2 — assignment_unreadable [proposed]; C-7H.7.7.3 — assignment_malformed [proposed]; C-7H.7.7.4 — assignment_empty [proposed]; C-7H.7.7.5 — assignment_unknown_mode [proposed]; C-7H.7.7.6 — assignment_duplicated [proposed]; C-7H.7.7.7 — assignment_contradictory [proposed]

### C-7H.7.7.1 — assignment_missing [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — No committed assignment for the ordinary A25 path. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Takes in: ACCEPTED — The missing mode-slot evidence. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Does: ACCEPTED — Holds RR2 as dependency_blocked_held and records assignment_missing [proposed]. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Gives out: ACCEPTED — reread_blocked_held only on truthful termination. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Must never: ACCEPTED — Invent a mode or borrow thread_membership_v1. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — No context snapshot proceeds without a valid committed basis. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.7.7 — Assignment failure consumption: Missing basis blocks RR2. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7.7 — Assignment failure consumption | Missing record. | Holds RR2. | No invented basis. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.7.7.2 — assignment_unreadable [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Assignment exists but its store state is unreadable. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Takes in: ACCEPTED — Unreadable record evidence. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Does: ACCEPTED — Records assignment_unreadable [proposed] and indeterminate_recovery_required. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Gives out: ACCEPTED — reread_indeterminate on truthful termination. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Must never: ACCEPTED — Reconstruct the record. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — RR2 stops. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.7.7 — Assignment failure consumption: Unreadability blocks RR2. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7.7 — Assignment failure consumption | Unreadable evidence. | Requires recovery. | No reconstruction. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.7.7.3 — assignment_malformed [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Assignment shape violates canonical rules. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Takes in: ACCEPTED — The invalid recorded form. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Does: ACCEPTED — Preserves it as evidence, records assignment_malformed [proposed] and requires indeterminate recovery. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Gives out: ACCEPTED — reread_indeterminate on truthful termination. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Must never: ACCEPTED — Repair the record in place. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — RR2 stops. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.7.7 — Assignment failure consumption: Invalid shape blocks RR2. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7.7 — Assignment failure consumption | Invalid shape. | Requires recovery. | Evidence preserved. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.7.7.4 — assignment_empty [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — An empty assigned_modes [proposed] list. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Takes in: ACCEPTED — The empty list. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Does: ACCEPTED — Records assignment_empty [proposed] and indeterminate_recovery_required. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Gives out: ACCEPTED — reread_indeterminate on truthful termination. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Must never: ACCEPTED — Treat emptiness as a valid default mode. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — RR2 stops. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.7.7 — Assignment failure consumption: Empty list is invalid. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7.7 — Assignment failure consumption | Empty list. | Requires recovery. | No default mode. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.7.7.5 — assignment_unknown_mode [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — A mode outside direct and wider-context. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Takes in: ACCEPTED — The unknown value. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Does: ACCEPTED — Records assignment_unknown_mode [proposed] and requires indeterminate recovery. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Gives out: ACCEPTED — reread_indeterminate on truthful termination. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Must never: ACCEPTED — Coerce or guess a mode. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — RR2 stops. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.7.7 — Assignment failure consumption: Only settled mode names are valid. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7.7 — Assignment failure consumption | Unknown value. | Requires recovery. | No coercion. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.7.7.6 — assignment_duplicated [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — More than one committed assignment for one claim. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Takes in: ACCEPTED — Conflicting multiplicity evidence. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Does: ACCEPTED — Records assignment_duplicated [proposed] and indeterminate_recovery_required. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Gives out: ACCEPTED — reread_indeterminate on truthful termination. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Must never: ACCEPTED — Auto-pick or delete either record. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — RR2 stops. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.7.7 — Assignment failure consumption: One commitment per claim is required. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7.7 — Assignment failure consumption | Multiple records. | Requires recovery. | No auto-selection. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.7.7.7 — assignment_contradictory [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Differing commit content or contradiction with trigger evidence. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Takes in: ACCEPTED — The contradictory records. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Does: ACCEPTED — Surfaces and records the conflict append-only as assignment_contradictory [proposed] and indeterminate_recovery_required. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Gives out: ACCEPTED — reread_indeterminate on truthful termination. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Must never: ACCEPTED — Resolve the conflict silently. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — RR2 stops. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.7.7 — Assignment failure consumption: Conflicts remain unresolved. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7.7 — Assignment failure consumption | Contradiction. | Surfaces and stops. | No silent resolution. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.7.8 — Assignment recovery
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — Lookup-first reuse of immutable assignment evidence. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — The committed claim and assignment/snapshot state. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Resumes only the missing boundary while preserving the exact committed assignment. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — Reused assignment or an honest hold/integrity block. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Recalculate an existing assignment because a fresh evaluation would differ. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Contradictory evidence follows the assignment failure owner. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]

TOGETHER
- Fed by: ACCEPTED — C-7H.7.8.1 — Recovery before assignment commit: Handles precommit interruption. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Fed by: ACCEPTED — C-7H.7.8.2 — Recovery after assignment before snapshot: Handles committed assignment without snapshot. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Fed by: ACCEPTED — C-7H.7.8.3 — Recovery of existing assignment: Handles existing record. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Gated by: ACCEPTED — C-7H.7.8.4 — Recovery of conflicting assignment: Handles conflicting recovery evidence. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Gated by: ACCEPTED — C-7H.7.8.5 — No truthful A25 relationship: No relationship cannot manufacture an assignment. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7 — A25 semantic reread assignment | Committed assignment. | Resumes missing boundary. | Immutable basis. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10] |
| 2 · ACCEPTED | C-7H.7.8.1 — Recovery before assignment commit | Precommit state. | Keeps resumable hold. | No premature RR5. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10] |
| 3 · ACCEPTED | C-7H.7.8.2 — Recovery after assignment before snapshot | Existing assignment. | Reuses exactly. | Stable context binding. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10] |
| 4 · ACCEPTED | C-7H.7.8.3 — Recovery of existing assignment | Existing record. | Returns it. | No recalculation. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10] |
| 5 · ACCEPTED | C-7H.7.8.4 — Recovery of conflicting assignment | Conflicting evidence. | Records indeterminate. | No deletion. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10] |
| 6 · ACCEPTED | C-7H.7.8.5 — No truthful A25 relationship | Neither relationship. | Records missing-assignment hold. | No forced mode. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10] |

SUB-PARTS: C-7H.7.8.1 — Recovery before assignment commit; C-7H.7.8.2 — Recovery after assignment before snapshot; C-7H.7.8.3 — Recovery of existing assignment; C-7H.7.8.4 — Recovery of conflicting assignment; C-7H.7.8.5 — No truthful A25 relationship

### C-7H.7.8.1 — Recovery before assignment commit
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — A claim still before atomic assignment commitment. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — No committed assignment. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Waits for production and commitment of a valid assignment; absent one records assignment_missing [proposed] as resumable. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — A held pre-RR2 claim. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Claim partial assignment data exists or write RR5 before truthful resolution. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — RR2 cannot proceed. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.7.8 — Assignment recovery: Snapshot needs a committed basis. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7.8 — Assignment recovery | Claim only. | Waits for valid assignment. | No partial claim. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.7.8.2 — Recovery after assignment before snapshot
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — Assignment committed but context snapshot absent. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — The exact committed assignment. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Resumes RR2 using that assignment unchanged. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — A snapshot bound to the original assignment. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Re-evaluate into a new mode inside the same claim. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Changed situations require a new trigger/claim. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.7.8 — Assignment recovery: Committed basis is immutable. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7.8 — Assignment recovery | Committed assignment. | Resumes RR2. | Exact reuse. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.7.8.3 — Recovery of existing assignment
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — Lookup finds the assignment for this claim. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — The immutable record. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Reuses it; an identical repeat commit converges. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — The existing assignment identity. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Create a second record or silently recalculate. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.7.8 — Assignment recovery: Identical repeats converge. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7.8 — Assignment recovery | Immutable basis. | Reuses identity. | No duplicate. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.7.8.4 — Recovery of conflicting assignment
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — Lookup exposes conflicting assignment evidence. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — The conflicting records. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Records and surfaces the contradiction, stops for indeterminate recovery and uses reread_indeterminate only on truthful termination. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — A protected integrity stop. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Delete or auto-resolve the conflict. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — No acknowledgement precedes the durable terminal. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.7.8 — Assignment recovery: Contradiction requires honest stop. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7.8 — Assignment recovery | Conflict. | Requires recovery. | No silent resolution. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.7.8.5 — No truthful A25 relationship
Stamp: ACCEPTED    Source: [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — A new-information-driven trigger to which neither semantic relationship applies. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The truthful absence of both relationships. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Holds as assignment_missing [proposed] with proposed no_a25_relationship_applies; the separately valid manual no-new-information path uses its typed compatibility owner. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — No invented assignment. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Force direct, wider-context, a sentinel, default or third mode, or turn manual permission into a new policy question. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Ordinary A25 execution does not proceed without a truthful assignment. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: ACCEPTED — C-7H.8 — Manual reread compatibility: Settled manual requests have their separate compatible basis. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-7H.7.8 — Assignment recovery: Modes need their actual relationships. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.7.8 — Assignment recovery | Truthful absence. | Holds ordinary path. | Manual compatibility stays separate. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §10] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.8 — Manual reread compatibility
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The accepted typed carrier for a valid manual reread with no new-information relationship. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — A manual trigger and truthful absence of an A25 relationship. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Lets the settled request use B10's mode slot without manufacturing a semantic mode or new evidence. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — A manual_reread_compatibility_record [proposed] as the alternate referent. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Require new information, reinterpret the request as evidence or add a third A25 mode. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — A manual trigger with a genuine A25 relationship must use the assignment path instead. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: ACCEPTED — C-7H.8.1 — manual_reread_compatibility_record [proposed]: Uses a typed carrier without modes. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Gated by: ACCEPTED — C-7H.8.2 — Compatibility type and truthfulness gates: Requires truthful applicability and type. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Gated by: ACCEPTED — C-7H.8.3 — Compatibility commit and exclusivity: Commits one carrier before snapshot. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.8.4 — Manual compatibility context behavior: Keeps broad relevant context. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-7H.8.5 — Compatibility failure consumption: Rejects invalid carrier evidence. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7H.8.6 — Compatibility recovery: Recovers by immutable reuse. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Changes: ACCEPTED — C-7H.8.7 — Compatibility operation events: Logs every actual carrier operation. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7H — Reread Lifecycle (§7H) | Manual trigger. | Uses typed compatibility. | No new mode. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5] |
| 2 · ACCEPTED | C-7H.7.8.5 — No truthful A25 relationship | Manual request. | Uses typed carrier when applicable. | No new-information demand. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §4] |
| 3 · ACCEPTED | C-7H.8.2 — Compatibility type and truthfulness gates | Trigger/relationship facts. | Checks applicability. | No false absence. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5] |
| 4 · ACCEPTED | C-7H.8.3 — Compatibility commit and exclusivity | Committed claim. | Admits one winner. | No duplicate carrier. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §7] |
| 5 · ACCEPTED | C-7H.8.4 — Manual compatibility context behavior | Manual request. | Reads full relevant context. | No narrowed manual reading. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §8] |
| 6 · ACCEPTED | C-7H.8.7 — Compatibility operation events | Carrier operation. | Records once. | No double evidence. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §11] |
| 7 · ACCEPTED | C-7H.11.8 — Manual path independent of relevance | Manual trigger without information. | Preserves distinct carrier. | No fake direct/wider relationship. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5] |

SUB-PARTS: C-7H.8.1 — manual_reread_compatibility_record [proposed]; C-7H.8.2 — Compatibility type and truthfulness gates; C-7H.8.3 — Compatibility commit and exclusivity; C-7H.8.4 — Manual compatibility context behavior; C-7H.8.5 — Compatibility failure consumption; C-7H.8.6 — Compatibility recovery; C-7H.8.7 — Compatibility operation events

### C-7H.8.1 — manual_reread_compatibility_record [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — A proposed immutable append-only record containing settled manual basis, not an assigned mode. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — Its identity, fixed kind, claim/trigger refs, settled basis, reason ref, timestamp and schema version. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Carries those eight fields and no assigned_modes [proposed], mode_evidence or assignment_reason [proposed] field. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — One unambiguously typed compatibility record. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Insert manual, none, not_applicable, sentinel or empty-list values into a nonexistent assigned_modes [proposed] field. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Malformed shape or unbound references fail closed. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: ACCEPTED — C-7H.8.1.1 — manual_compatibility_id [proposed]: Carries stable identity. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-7H.8.1.3 — Compatibility reread_claim_ref [proposed]: References its committed claim. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-7H.8.1.5 — Compatibility settled_basis [proposed]: Carries settled authority. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-7H.8.1.6 — compatibility_reason [proposed]: References the request's own reason. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-7H.8.1.7 — Compatibility committed_at [proposed]: Carries commitment time. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-7H.8.1.8 — Compatibility schema_version [proposed]: Carries schema revision. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Gated by: ACCEPTED — C-7H.8.1.2 — Compatibility record_kind [proposed]: Requires the fixed kind. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Gated by: ACCEPTED — C-7H.8.1.4 — Compatibility trigger_record_ref [proposed]: Requires the manual trigger. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.3.3.1 — reread_mode_ref [proposed] | Carrier identity. | Consumes settled manual basis. | No fabricated mode. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7H.8 — Manual reread compatibility | Manual basis. | Records compatibility. | No fabricated assignment. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5] |

SUB-PARTS: C-7H.8.1.1 — manual_compatibility_id [proposed]; C-7H.8.1.2 — Compatibility record_kind [proposed]; C-7H.8.1.3 — Compatibility reread_claim_ref [proposed]; C-7H.8.1.4 — Compatibility trigger_record_ref [proposed]; C-7H.8.1.5 — Compatibility settled_basis [proposed]; C-7H.8.1.6 — compatibility_reason [proposed]; C-7H.8.1.7 — Compatibility committed_at [proposed]; C-7H.8.1.8 — Compatibility schema_version [proposed]

### C-7H.8.1.1 — manual_compatibility_id [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The proposed stable compatibility-record identity. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — The committed record. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Supplies the identity referenced by reread_mode_ref [proposed]. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — manual_compatibility_id [proposed]. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8.1 — manual_reread_compatibility_record [proposed] | Carrier ID. | Binds mode reference. | Exact pointer. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.8.1.2 — Compatibility record_kind [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The proposed fixed literal manual_no_new_information_compatibility. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — The compatibility record's type. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Carries the literal as an internal integrity discriminator. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — record_kind [proposed]. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Omit, change or cross-label the literal. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — A wrong or absent literal is malformed. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8.1 — manual_reread_compatibility_record [proposed] | Literal. | Checks type integrity. | No cross-labeling. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.8.1.3 — Compatibility reread_claim_ref [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The proposed reference to one existing committed root/trigger claim. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — That claim's identity. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Binds the carrier to one claim. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — reread_claim_ref [proposed]. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Commit without a claim. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — No claim means no compatibility record. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8.1 — manual_reread_compatibility_record [proposed] | Claim ID. | Binds record. | No claimless carrier. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.8.1.4 — Compatibility trigger_record_ref [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The proposed reference to the existing manual trigger. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — A trigger whose trigger_type is manual. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Binds the carrier to that trigger. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — trigger_record_ref [proposed]. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Consume the carrier for a nonmanual trigger. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Wrong trigger fails closed. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8.1 — manual_reread_compatibility_record [proposed] | Trigger ref. | Checks type truth. | Manual scope. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.8.1.5 — Compatibility settled_basis [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The proposed fixed literal master_v10_7H_manual. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — The settled manual authority. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Records that authority by citation rather than creating policy. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — settled_basis [proposed]. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Redefine manual permission through this field. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8.1 — manual_reread_compatibility_record [proposed] | Fixed basis. | Records reference. | No new policy. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.8.1.6 — compatibility_reason [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — A proposed reference to the manual trigger's own recorded reason. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — The valid manual request reason. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — References it without copying it. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — compatibility_reason [proposed]. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Manufacture new-information evidence from the request. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8.1 — manual_reread_compatibility_record [proposed] | Reason ref. | Preserves request basis. | No copied evidence. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.8.1.7 — Compatibility committed_at [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The proposed record commitment timestamp. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — Actual commitment time. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Records it. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — committed_at [proposed]. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8.1 — manual_reread_compatibility_record [proposed] | Timestamp. | Records time. | Temporal provenance. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.8.1.8 — Compatibility schema_version [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The proposed carrier schema revision. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — The record's schema version. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Records the form version. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — schema_version [proposed]. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8.1 — manual_reread_compatibility_record [proposed] | Version. | Records form. | Schema provenance. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.8.2 — Compatibility type and truthfulness gates
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Four independent distinctions: record shape, type-derived key, fixed kind literal and truthful trigger use. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — Exactly one committed mode-slot referent and its claim/trigger facts. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Verifies manual trigger and no truthful A25 relationship; distinguishes the carrier without retrofitting assignment records. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — One valid typed mode-slot basis. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Manufacture absence of a relationship, auto-pick between both record types or modify accepted assignment shapes. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Wrong-trigger, inapplicable or both-types evidence fails closed. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.8 — Manual reread compatibility: Only manual without truthful A25 relation qualifies. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8 — Manual reread compatibility | Trigger and relationships. | Checks both. | Valid manual path only. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.8.3 — Compatibility commit and exclusivity
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — One atomic commit before the context snapshot under proposed manual_compatibility_key = stable_hash(reread_claim_key + "manual_compat_v1"). [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §7]
- Takes in: ACCEPTED — One committed claim/manual trigger and truthful compatibility content. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §7]
- Does: ACCEPTED — Admits one winner; identical repeats converge; refuses if an assignment already exists with mode_slot_already_assigned; snapshot references the committed carrier. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §7]
- Gives out: ACCEPTED — One immutable compatibility record with a noncolliding type-derived key. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §7]
- Must never: ACCEPTED — Edit, delete, recalculate or replace its contents; concurrent losers append nothing. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Differing content is conflicting evidence; residual both-types commitment fails closed at consumption. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.8 — Manual reread compatibility: Carrier needs valid manual basis and claim. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.7.5 — Assignment commit and snapshot binding: Existing assignment prevents compatibility commitment. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §7] [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8 — Manual reread compatibility | Claim and carrier. | Enforces exclusivity. | Immutable mode-slot basis. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.8.4 — Manual compatibility context behavior
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — A fresh root reading using the broadest safely available clearly relevant context. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §8]
- Takes in: ACCEPTED — The manual request and authorized relevant context. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §8]
- Does: ACCEPTED — Applies Privacy then Retrieval then Relevance under one claim/snapshot/proposal and at most one new layer. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §8]
- Gives out: ACCEPTED — A fresh manual reread without simulated new-evidence checks. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §8]
- Must never: ACCEPTED — Deliberately narrow context, invent new evidence or bypass any access, integrity, relevance, holding or safety protection. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Existing bounds and failure rules continue unchanged. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.8 — Manual reread compatibility: Compatibility carries permission, not invented evidence. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8 — Manual reread compatibility | Authorized context. | Reads freshly. | No invented new evidence. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7H.8.5 — Compatibility failure consumption
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Seven fail-closed conditions retaining existing B10 states, parent terminals and child logs. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Takes in: ACCEPTED — Missing, unreadable, malformed, wrong-trigger, inapplicable, duplicated or contradictory evidence. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Does: ACCEPTED — Writes fail_closed_event [proposed] with the exact reason; uses reread_blocked_held or reread_indeterminate only when truthfully terminal. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Gives out: ACCEPTED — A recorded protected stop or resumable hold. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Must never: ACCEPTED — Acknowledge before durable RR5 or treat a child log as parent terminal. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Resumable conditions keep RR5 unwritten until actual resolution. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.8.5.1 — compatibility_missing [proposed]: Handles missing carrier. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7H.8.5.2 — compatibility_unreadable [proposed]: Handles unreadable carrier. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7H.8.5.3 — compatibility_malformed [proposed]: Handles malformed carrier. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7H.8.5.4 — compatibility_wrong_trigger [proposed]: Handles wrong trigger. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7H.8.5.5 — compatibility_not_applicable [proposed]: Handles inapplicable carrier. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7H.8.5.6 — compatibility_duplicated [proposed]: Handles duplicated carrier. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7H.8.5.7 — Compatibility contradictory records: Handles contradictory carrier evidence. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8 — Manual reread compatibility | Record state. | Uses existing B10 outcomes. | Honest stop. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9] |
| 2 · ACCEPTED | C-7H.8.5.1 — compatibility_missing [proposed] | Missing record. | Records held state. | Truthful RR5 timing. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9] |
| 3 · ACCEPTED | C-7H.8.5.2 — compatibility_unreadable [proposed] | Store failure. | Records indeterminate. | No reconstruction. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9] |
| 4 · ACCEPTED | C-7H.8.5.3 — compatibility_malformed [proposed] | Malformed record. | Preserves evidence. | No repair in place. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9] |
| 5 · ACCEPTED | C-7H.8.5.4 — compatibility_wrong_trigger [proposed] | Wrong type. | Records indeterminate. | No coerced trigger. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9] |
| 6 · ACCEPTED | C-7H.8.5.5 — compatibility_not_applicable [proposed] | Assignment evidence. | Refuses carrier. | Truthful mode path. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9] |
| 7 · ACCEPTED | C-7H.8.5.6 — compatibility_duplicated [proposed] | Duplicate evidence. | Records integrity stop. | No picked record. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9] |
| 8 · ACCEPTED | C-7H.8.5.7 — Compatibility contradictory records | Conflict. | Records/surfaces. | No merge or deletion. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9] |

SUB-PARTS: C-7H.8.5.1 — compatibility_missing [proposed]; C-7H.8.5.2 — compatibility_unreadable [proposed]; C-7H.8.5.3 — compatibility_malformed [proposed]; C-7H.8.5.4 — compatibility_wrong_trigger [proposed]; C-7H.8.5.5 — compatibility_not_applicable [proposed]; C-7H.8.5.6 — compatibility_duplicated [proposed]; C-7H.8.5.7 — Compatibility contradictory records

### C-7H.8.5.1 — compatibility_missing [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — A qualifying manual claim without either committed mode-slot record. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Takes in: ACCEPTED — Missing carrier evidence. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Does: ACCEPTED — Records compatibility_missing [proposed] and dependency_blocked_held at RR2. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Gives out: ACCEPTED — reread_blocked_held only on truthful termination. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Must never: ACCEPTED — Invent a semantic mode or borrow thread_membership_v1. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — No snapshot proceeds. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.8.5 — Compatibility failure consumption: No basis permits no snapshot. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8.5 — Compatibility failure consumption | Absent record. | Holds RR2. | No invented mode. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.8.5.2 — compatibility_unreadable [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — An existing carrier whose store state cannot be read. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Takes in: ACCEPTED — Unreadable evidence. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Does: ACCEPTED — Records compatibility_unreadable [proposed] and indeterminate_recovery_required. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Gives out: ACCEPTED — reread_indeterminate on truthful termination. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Must never: ACCEPTED — Reconstruct the carrier. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — RR2 stops. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.8.5 — Compatibility failure consumption: Unreadable evidence blocks. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8.5 — Compatibility failure consumption | Unreadable evidence. | Requires recovery. | No reconstruction. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.8.5.3 — compatibility_malformed [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Wrong/absent kind, missing required field, mode-carrying field or unbound reference. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Takes in: ACCEPTED — The malformed record. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Does: ACCEPTED — Keeps it visible, records compatibility_malformed [proposed] and requires indeterminate recovery. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Gives out: ACCEPTED — reread_indeterminate on truthful termination. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Must never: ACCEPTED — Repair it in place. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — RR2 stops. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.8.5 — Compatibility failure consumption: Required shape must hold. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8.5 — Compatibility failure consumption | Invalid shape. | Requires recovery. | No in-place repair. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.8.5.4 — compatibility_wrong_trigger [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — A carrier bound to a nonmanual trigger. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Takes in: ACCEPTED — The actual trigger type. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Does: ACCEPTED — Records compatibility_wrong_trigger [proposed] and indeterminate_recovery_required. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Gives out: ACCEPTED — reread_indeterminate on truthful termination. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Must never: ACCEPTED — Reinterpret the trigger as manual. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — RR2 stops. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.8.5 — Compatibility failure consumption: Manual trigger is mandatory. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8.5 — Compatibility failure consumption | Nonmanual type. | Requires recovery. | No reinterpretation. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.8.5.5 — compatibility_not_applicable [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — A manual trigger for which new information truthfully yields an A25 assignment. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Takes in: ACCEPTED — The actual relationship evidence. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Does: ACCEPTED — Refuses compatibility commitment; a residual committed carrier is indeterminate with compatibility_not_applicable [proposed]. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Gives out: ACCEPTED — Refusal or reread_indeterminate on truthful termination. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Must never: ACCEPTED — Force the no-information path. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — The truthful assignment path remains the applicable mode-slot route. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.8.5 — Compatibility failure consumption: A real relationship excludes compatibility. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8.5 — Compatibility failure consumption | Real A25 relationship. | Refuses or stops. | Assignment route preserved. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.8.5.6 — compatibility_duplicated [proposed]
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Multiple committed carriers for one claim. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Takes in: ACCEPTED — The duplicate evidence. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Does: ACCEPTED — Records compatibility_duplicated [proposed] and indeterminate_recovery_required. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Gives out: ACCEPTED — reread_indeterminate on truthful termination. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Must never: ACCEPTED — Pick or delete a record to hide the integrity breach. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — RR2 stops. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.8.5 — Compatibility failure consumption: Only one carrier can exist. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8.5 — Compatibility failure consumption | Multiple commitments. | Requires recovery. | No auto-selection. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.8.5.7 — Compatibility contradictory records
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Both record types committed, differing repeated content or contradiction with the trigger. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Takes in: ACCEPTED — The conflicting records. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Does: ACCEPTED — Surfaces and records mode_slot_conflicting_records [proposed] or compatibility_contradictory [proposed] and requires indeterminate recovery. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Gives out: ACCEPTED — reread_indeterminate on truthful termination. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Must never: ACCEPTED — Merge, delete or silently resolve the contradiction. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — RR2 stops. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.8.5 — Compatibility failure consumption: Contradiction cannot be auto-resolved. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8.5 — Compatibility failure consumption | Conflicting records. | Surfaces and stops. | No silent resolution. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.8.6 — Compatibility recovery
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — Five lookup-first cases reusing immutable carrier evidence. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Takes in: ACCEPTED — Claim, carrier, snapshot and recovery records. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Does: ACCEPTED — Resumes only the missing boundary and retains committed content. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Gives out: ACCEPTED — Idempotent recovery or an honest stop. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Must never: ACCEPTED — Recalculate a committed carrier or invent partial commitment. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Contradictions follow the carrier's fail-closed owner. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]

TOGETHER
- Fed by: ACCEPTED — C-7H.8.6.1 — Recovery before compatibility commit: Handles precommit crash. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Fed by: ACCEPTED — C-7H.8.6.2 — Recovery after compatibility before snapshot: Handles carrier before snapshot. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Fed by: ACCEPTED — C-7H.8.6.3 — Recovery of existing compatibility record: Handles existing carrier. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Fed by: ACCEPTED — C-7H.8.6.5 — Duplicate compatibility recovery: Handles repeat recovery. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Gated by: ACCEPTED — C-7H.8.6.4 — Recovery of conflicting compatibility evidence: Handles recovery conflict. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8 — Manual reread compatibility | Committed evidence. | Resumes missing work. | No recalculation. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10] |
| 2 · ACCEPTED | C-7H.8.6.1 — Recovery before compatibility commit | Missing basis. | Keeps hold resumable. | No premature terminal. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10] |
| 3 · ACCEPTED | C-7H.8.6.2 — Recovery after compatibility before snapshot | Existing carrier. | Resumes snapshot. | No recalculation. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10] |
| 4 · ACCEPTED | C-7H.8.6.3 — Recovery of existing compatibility record | Existing content. | Returns identity. | No duplication. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10] |
| 5 · ACCEPTED | C-7H.8.6.4 — Recovery of conflicting compatibility evidence | Conflict. | Records indeterminate. | No deletion. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10] |
| 6 · ACCEPTED | C-7H.8.6.5 — Duplicate compatibility recovery | Recovery ID. | Looks up first. | No-op repetition. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10] |

SUB-PARTS: C-7H.8.6.1 — Recovery before compatibility commit; C-7H.8.6.2 — Recovery after compatibility before snapshot; C-7H.8.6.3 — Recovery of existing compatibility record; C-7H.8.6.4 — Recovery of conflicting compatibility evidence; C-7H.8.6.5 — Duplicate compatibility recovery

### C-7H.8.6.1 — Recovery before compatibility commit
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — A claim before the carrier's atomic commit. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Takes in: ACCEPTED — No committed carrier. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Does: ACCEPTED — Finds the pre-RR2 claim and holds as compatibility_missing [proposed] until the record is committed. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Gives out: ACCEPTED — A resumable hold. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Must never: ACCEPTED — Write RR5 before truthful resolution. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — No snapshot proceeds. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.8.6 — Compatibility recovery: A committed carrier must precede snapshot. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8.6 — Compatibility recovery | Claim only. | Waits for carrier. | No partial commitment. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.8.6.2 — Recovery after compatibility before snapshot
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — A committed carrier with snapshot absent. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Takes in: ACCEPTED — The exact carrier record. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Does: ACCEPTED — Resumes RR2 using it unchanged. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Gives out: ACCEPTED — A snapshot bound to that carrier. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Must never: ACCEPTED — Recalculate the committed basis. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Changed situations require a new trigger and claim. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.8.6 — Compatibility recovery: Committed basis is reused exactly. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8.6 — Compatibility recovery | Committed carrier. | Resumes RR2. | Exact reuse. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.8.6.3 — Recovery of existing compatibility record
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — Lookup finds the claim's immutable carrier. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Takes in: ACCEPTED — That existing record. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Does: ACCEPTED — Reuses it; identical repeated commitment converges. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Gives out: ACCEPTED — The same record identity. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Must never: ACCEPTED — Create a second record or recalculate. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.8.6 — Compatibility recovery: Repeated identical commits converge. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8.6 — Compatibility recovery | Immutable record. | Returns it. | No second record. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.8.6.4 — Recovery of conflicting compatibility evidence
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — Recovery exposes contradictory carrier evidence. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Takes in: ACCEPTED — The conflicting durable records. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Does: ACCEPTED — Records and surfaces indeterminate_recovery_required; reread_indeterminate follows only on truthful termination. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Gives out: ACCEPTED — An honest integrity stop. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Must never: ACCEPTED — Auto-resolve or erase the conflict. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — No acknowledgement before durable RR5. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.8.6 — Compatibility recovery: Conflicting evidence stops recovery. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8.6 — Compatibility recovery | Contradiction. | Requires recovery. | No auto-resolution. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.8.6.5 — Duplicate compatibility recovery
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — Repeat recovery over the same committed state. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Takes in: ACCEPTED — The existing recovery_run_id and records. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Does: ACCEPTED — Re-reads state and reapplies nothing. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Gives out: ACCEPTED — recovery_noop [proposed]. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Must never: ACCEPTED — Repeat committed effects. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.8.6 — Compatibility recovery: Committed effects are never replayed. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8.6 — Compatibility recovery | Existing findings. | Returns no-op. | No repeated effect. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.8.7 — Compatibility operation events
Stamp: ACCEPTED    Source: [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Proposed manual_compatibility_committed and manual_compatibility_commit_refused plus existing B10 failure/recovery events. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §11]
- Takes in: ACCEPTED — Commit/refusal with claim/trigger refs and reasons, including compatibility_not_applicable [proposed], mode_slot_already_assigned or malformed request. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §11]
- Does: ACCEPTED — Logs each real operation once under B10's parent/child structure; state records remain distinct from logs. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §11]
- Gives out: ACCEPTED — Protected append-only events and unchanged recovery_applied [proposed]/recovery_noop [proposed]/fail_closed_event [proposed] use. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §11]
- Must never: ACCEPTED — Create log-about-logging, duplicate evidence or treat repetition as increased warrant. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Privacy authorization governs every record, including refusal logs. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.8 — Manual reread compatibility: Logs actual operations under the owning structure. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §11]
- Changes: ACCEPTED — C-7H.6.7 — B10 recovery and failure events: Reuses existing B10 recovery/failure events. [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.8 — Manual reread compatibility | Commit/refusal. | Appends owned event. | No silent operation. | [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-7H.9 — B9 retry-state architecture
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Mechanical bookkeeping and admission around an existing source operation, not another execution path. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §11]
- Takes in: ACCEPTED — The source seam's canonical identity and durable outcome. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §11]
- Does: ACCEPTED — Classifies, admits, records and recovers same-identity attempts through the seam's own boundaries. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §11]
- Gives out: ACCEPTED — At most the source operation's one committed result. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §11]
- Must never: ACCEPTED — Judge meaning, rescore evidence, weaken duplicate defenses or silently re-execute. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — No execution without committed admission and its required budget or authorization evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-7H.9.1 — B9 outcome classes: Consumes durable outcome classification. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fed by: ACCEPTED — C-7H.9.2 — B9 attempt kinds: Keeps attempt kinds distinct. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fed by: ACCEPTED — C-7H.9.3 — B9 identities and external state: Uses external canonical records. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-7H.9.4 — B9 R0–R4 transaction sequence: Execution requires the canonical sequence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Gated by: ACCEPTED — C-7H.9.5 — B9 nine idempotency boundaries: Preserves nine duplicate boundaries. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7H.9.6 — B9 nineteen recovery cases: Recovers through source evidence first. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-7H.10 — Accepted B9 retry values and episodes: Consumes accepted bounded values. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Changes: ACCEPTED — C-7H.9.7 — B9 operational event set: Logs actual retry operations. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7H — Reread Lifecycle (§7H) | Completion state. | Routes correctly. | No retry as reread. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §3] |
| 2 · ACCEPTED | C-NEW-AIC.6.18 — Recovery of technical failure or interrupted verification | The episode's committed claim, actual completed steps and any sealed basis. | Gates this place: owns any admissible re-attempt. | Nothing in this card. | [04/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md §12] |
| 3 · ACCEPTED | C-16.17.8 — B24 committed-boundary recovery | Destination records for capture, routing plans/effects, compatibility, brief, validation, assessment, payload, draft/post-check, final gate and delivery identity/receipt. | Gates this place: retains ownership of any permitted retry. | Nothing in this card. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md §6.4] |
| 4 · ACCEPTED | C-NEW-UDOK.2.11 — ID-11 — B9 retry-group identity [proposed] | B9's established group. | Owns group establishment and state. | Nothing in this card. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §B.2] |
| 5 · ACCEPTED | C-NEW-AIC.6 — Lookup-first recovery and partial completion | Run records, claim and attachment records, tentative or sealed basis, committed outcome and terminal evidence. | Gates this place: controls any re-execution after technical failure. | Nothing in this card. | [04/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md §12] |
| 6 · ACCEPTED | C-LMAC.10.1 — Same-query bounded transport retry | The unchanged query intent/context and technical failure. | Supplies B9 classification. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 7 · ACCEPTED | C-NEW-UDOK.13.2 — I-2 — B9 reference interface [proposed] | The owner's group and attempt. | Supplies the owner retry records. | Nothing in this card. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §T] |
| 8 · ACCEPTED | C-7Q.10 — Shared privacy-operation discipline | Committed operation state, the contract’s idempotency key, durable checkpoints and owner-defined failure class. | Supplies accepted B9 retry mechanics. | Nothing in this card. | [04/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md §15] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] |
| 9 · ACCEPTED | C-NEW-UDOK.7.4 — Changed coordination, component and authority inputs | Changed kernel coordination circumstances, changed component canonical inputs or changed/unprovable AIC inputs. | Gates this place: owns the group associated with a changed source-operation identity. | Nothing in this card. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §H.6] |
| 10 · ACCEPTED | C-7R.15.8.1 — Retrieval-system failure boundary | A retrieval-system failure, bounded B9 attempts and the terminal outcome. | Supplies b9 retry mechanics. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] |
| 11 · ACCEPTED | C-NEW-UDOK.1.17 — E17 — B9 attempt reference [proposed] | B9's own durable attempt record. | Owns attempt identity and counting. | Nothing in this card. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §A.2] |
| 12 · ACCEPTED | C-NEW-AIC.6.24 — Crash during anchor, claim or attachment commitment | Committed family, anchor, exact source references and class/version, plus actual claim, basis and attachment records. | Gates this place: controls any resumed execution after a stranded claim. | Nothing in this card. | [04/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md §12] |
| 13 · ACCEPTED | C-7D.17 — B6 operation integrity and recordkeeping | Stable identity, source/version set, declared commit boundary and actual committed outcome. | Gates this place: accepted B9 mechanics. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 14 · ACCEPTED | C-NEW-AIC.5.7 — Accepted retry values consumed by AIC | The exact accepted budget reference and the executing episode's recorded live or background schedule class. | Gates this place: decides admission, counting, scheduling and disposition. | Nothing in this card. | [04/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md §11] |
| 15 · ACCEPTED | C-24.18 — Connection technical retry boundary | A real technical failure and the same stable operation. | Gates this place: accepted technical retry admission and classifications. | Nothing in this card. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §17] |
| 16 · ACCEPTED | C-7M.9.5 — Computed View bounded technical retry | An eligible technical failure and its recorded retry references. | Gates this place: B9 mechanics. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 17 · ACCEPTED | C-7P.13.1 — Authority-record operation and recovery contract | Stable operation identity, source/version set, commit boundary and existing or interrupted outcome. | Supplies accepted B9 mechanics. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 18 · ACCEPTED | C-7N.11.6 — Surfacing technical-retry boundary | A classified failure under the stable operation identity. | Supplies accepted B9 classifications and mechanism. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 19 · ACCEPTED | C-7M.6.7 — Computed View retry_eligibility | The technical failure and the governing accepted retry rules. | Supplies accepted B9 retry architecture. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 20 · ACCEPTED | C-NEW-AIC.5 — Stop classes and retry ownership | The execution's own durable evidence of what was checked or could not be checked. | Gates this place: exclusively owns retry admission, counting, scheduling and disposition. | Nothing in this card. | [04/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md §11] |
| 21 · ACCEPTED | C-7D.17.6 — B6 bounded technical retry | A technically retryable failure and recorded accepted B9 values. | Gates this place: technical retry mechanics. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 22 · ACCEPTED | C-16.17.3.3 — Technical child failure | A truthful technical cause and recoverable committed state. | Gates this place: governs technical retry classification and admission. | Nothing in this card. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md §6.1] |
| 23 · ACCEPTED | C-NEW-UDOK.1.16 — E16 — B9 retry-group reference [proposed] | The retry group established by B9. | Establishes and owns the retry group. | Nothing in this card. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §A.2] |
| 24 · ACCEPTED | C-BOP.13.2 — BOP shared retry and committed-state recovery | Actual technical failure, committed checkpoints and per-item completion. | Supplies b9 failure classes. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 25 · ACCEPTED | C-CREATE.10.4 — Creation bounded retry consumption | Actual retryable/terminal class, recorded context and durable admission authority. | Gates this place: consumes the existing generic retry state and admission owner. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| 26 · ACCEPTED | C-7Q.11.10 — Privacy refusal and changed-authorization admission | The refused operation and any genuinely changed recorded authorization. | Supplies b9 outcome classification. | Nothing in this card. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |
| 27 · ACCEPTED | C-NEW-AIC.6.19 — Recovery when readability is restored | The recorded technical failure and whether a basis had already sealed. | Gates this place: admits the appropriate owned attempt. | Nothing in this card. | [04/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md §12] |
| 28 · ACCEPTED | C-NEW-AIC.5.2 — Technical failure without authority outcome | The failing step and actual technical evidence. | Gates this place: admits any eligible retry through its existing rules. | Nothing in this card. | [04/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md §11] |
| 29 · ACCEPTED | C-7O.10.2 — Result assessment never authorizes action retry | A partial, failed, unknown or cancelled result and any technical record-operation failure. | Supplies technical failure classification and retry ownership. | Nothing in this card. | [V10 §7O] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.2] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 30 · ACCEPTED | C-7M.9 — Computed View operation and recovery contract | The operation identity, exact source/version set, declared record-level commit boundary and observed completion state. | Gates this place: accepted B9 mechanics. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 31 · ACCEPTED | C-NEW-AIC.5.6 — Established-generation B9 retry boundary | B9 admission plus a completed read-only confirmation outside the retry execution proving the canonical generation inputs unchanged. | Gates this place: retains admission and group ownership. | Nothing in this card. | [04/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md §11] |
| 32 · ACCEPTED | C-NEW-UDOK.2.12 — ID-12 — B9 attempt identity [proposed] | The retry owner's actual attempt record. | Owns attempts and their numbering. | Nothing in this card. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §B.2] |
| 33 · ACCEPTED | C-8.16 — Research retry and committed recovery | Retryable or terminal stage failures and committed per-stage progress. | Gates this place: retry-state authority. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| 34 · ACCEPTED | C-OOP.8.3 — Bounded outcome technical retry | The actual failure class and durable prior attempt history. | Supplies b9 classification and operation rules. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |

SUB-PARTS: C-7H.9.1 — B9 outcome classes; C-7H.9.2 — B9 attempt kinds; C-7H.9.3 — B9 identities and external state; C-7H.9.4 — B9 R0–R4 transaction sequence; C-7H.9.5 — B9 nine idempotency boundaries; C-7H.9.6 — B9 nineteen recovery cases; C-7H.9.7 — B9 operational event set

### C-7H.9.1 — B9 outcome classes
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — Six proposed routing classes derived from the source's durable outcome. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — The actual source terminal evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Routes success to absorption, technical failure to bounded admission and protected/unresolved outcomes to their own refusal or recovery paths. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — A mechanical retry classification. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: ACCEPTED — Treat a class as a judgment about meaning. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Unprovable outcomes cannot authorize retry. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]

TOGETHER
- Fed by: ACCEPTED — C-7H.9.1.1 — terminal_success [proposed]: Routes committed outcomes to absorption. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fed by: ACCEPTED — C-7H.9.1.3 — technical_retryable [proposed]: Routes retryable technical outcomes to budget checks. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gated by: ACCEPTED — C-7H.9.1.2 — terminal_substantive [proposed]: Requires policy/case authority for substantive retry. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gated by: ACCEPTED — C-7H.9.1.4 — dependency_blocked_held [proposed]: Blocks held dependencies. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gated by: ACCEPTED — C-7H.9.1.5 — privacy_refused [proposed]: Blocks unchanged privacy refusal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gated by: ACCEPTED — C-7H.9.1.6 — indeterminate [proposed]: Requires source recovery for indeterminate state. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9 — B9 retry-state architecture | Source terminal. | Routes mechanically. | No meaning judgment. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: C-7H.9.1.1 — terminal_success [proposed]; C-7H.9.1.2 — terminal_substantive [proposed]; C-7H.9.1.3 — technical_retryable [proposed]; C-7H.9.1.4 — dependency_blocked_held [proposed]; C-7H.9.1.5 — privacy_refused [proposed]; C-7H.9.1.6 — indeterminate [proposed]

### C-7H.9.1.1 — terminal_success [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — Committed, duplicate_absorbed or completed source outcomes, including honest insufficient_context readings. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — The committed result. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Absorbs later requests against that result without another attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — Existing committed output. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: ACCEPTED — Retry a completed result. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — No new execution is admitted. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.1 — B9 outcome classes | Success. | Returns existing result. | No retry. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7H.9.1.2 — terminal_substantive [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — Acceptance rejection, identity conflict or permanent schema-invalid re-presentation. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — The durable distinct substantive outcome. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Keeps it terminal unless a separately accepted policy and case authorization explicitly permit the applicable class. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — Terminal status or narrowly authorized admission evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: ACCEPTED — Treat every substantive class as machine-retryable merely because B24 permits one eligible careful retry. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Missing policy or per-case authorization refuses admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.1 — B9 outcome classes | Rejection. | Preserves terminal boundary. | No automatic second chance. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7H.9.1.3 — technical_retryable [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — Recorded potentially retryable pass failures, timeouts, unavailable/stale index, interruptions, lost races or technical write failures. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — is_technical_and_potentially_retryable, B11 interrupted, B16 promotion_interrupted or equivalent source evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Allows only R1 admission under an existing declared budget. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — Budget-gated technical retry eligibility. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: ACCEPTED — Execute without admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Missing budget or unsatisfied terms prevents retry. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.1 — B9 outcome classes | Technical failure. | Requires admission. | Bounded eligibility. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7H.9.1.4 — dependency_blocked_held [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — A live hold or recorded dependency block. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — The source or input's owning block state. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Refuses and records a retry request while waiting for the owner's release interface. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — Protected blocked status. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: ACCEPTED — Retry or silently queue around the block. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — No retry while blocked. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.1 — B9 outcome classes | Live block. | Waits on owner. | No retry around hold. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7H.9.1.5 — privacy_refused [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — Refusal by privacy or access control. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — The owning gate's recorded refusal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Refuses retry unless a genuinely changed recorded authorization state supports a new admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — Gate-governed refusal or changed-authorization reference. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: ACCEPTED — Retry around the refusal or substitute a generic real-change record for authorization. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — No new attempt without the gate's changed-authorization evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.1 — B9 outcome classes | Gate evidence. | Requires changed authorization. | No privacy bypass. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7H.9.1.6 — indeterminate [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — A source seam's indeterminate_recovery_required state. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — Unresolved source evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Requires the source's own recovery before retry admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — A recovery-first block. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: ACCEPTED — Retry unresolved state. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — No admission until source recovery resolves it. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.1 — B9 outcome classes | Unresolved evidence. | Blocks admission. | Recovery first. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7H.9.2 — B9 attempt kinds
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — Technical, substantive and explicitly policy-authorized re-attempts. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — The applicable source class and authorization evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Keeps budget-based technical admission distinct from meaning-level or explicit policy authorization. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — A typed attempt under the proper admission requirements. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: ACCEPTED — Use one kind's permission to bypass another kind's requirements. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Missing declared references blocks admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]

TOGETHER
- Fed by: ACCEPTED — C-7H.9.2.1 — Technical retry kind: Uses budget for technical retries. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gated by: ACCEPTED — C-7H.9.2.2 — Substantive retry kind: Requires substantive policy and case references. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gated by: ACCEPTED — C-7H.9.2.3 — Policy-authorized retry kind: Requires recorded explicit retry authority. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9 — B9 retry-state architecture | Budget/policy evidence. | Selects requirements. | No mixed permissions. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: C-7H.9.2.1 — Technical retry kind; C-7H.9.2.2 — Substantive retry kind; C-7H.9.2.3 — Policy-authorized retry kind

### C-7H.9.2.1 — Technical retry kind
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — A same-identity attempt of technical_retryable work. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — Existing declared retry budget. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Applies budget-gated admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — A permitted technical attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: ACCEPTED — Supply silent defaults. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Unsatisfied budget prevents execution. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.3.5 — retry_budget_ref [proposed], C-7H.9.4.2 — R1 — Retry attempt admission: the attempt is admitted only within its declared budget. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.2 — B9 attempt kinds | Technical class. | Applies declared terms. | No silent default. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7H.9.2.2 — Substantive retry kind
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — A meaning-level re-attempt requiring explicit policy and case authority. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — Adopted retry policy and per-case authorization references. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Admits only what those references expressly allow. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — A bounded authorized substantive attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: ACCEPTED — Infer that rejection deserves another chance. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Either missing reference blocks execution. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.3.6 — retry_policy_ref [proposed], C-7H.9.3.7 — retry_authorization_ref [proposed]: the adopted policy and the per-case authorization both allow the attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.2 — B9 attempt kinds | Authority records. | Checks explicit permission. | No meaning judgment. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7H.9.2.3 — Policy-authorized retry kind
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — An explicitly authorized re-attempt, such as a recorded directed retry. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — The applicable policy and recorded authorization reference. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Uses the same R1 checks and canonical seam identity. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — A recorded authorized attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Bypass source gates or admission because a request exists. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Required authority references must exist and be satisfied. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.4.2 — R1 — Retry attempt admission, C-7H.9.3.6 — retry_policy_ref [proposed], C-7H.9.3.7 — retry_authorization_ref [proposed]: the R1 checks pass and the required policy and case authority exist and are satisfied. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.2 — B9 attempt kinds | Policy/case refs. | Uses R1. | No bypass. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.9.3 — B9 identities and external state
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — Proposed canonical group, attempt, request and state-record identities. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — Source canonical key/class, outcomes, attempts and authorizing references. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Keeps all retry state outside root and reading schemas and references seam records by identity. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — Durable retry bookkeeping without duplicate source evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Modify the seven-field root or twelve-field reading schema. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Required references cannot be replaced by defaults. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: ACCEPTED — C-7H.9.3.1 — retry_group_id [proposed]: Uses one canonical group. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.9.3.2 — attempt_id [proposed]: Uses deterministic attempt identity. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.9.3.3 — retry_request_op_id [proposed]: Uses parent/child request identity. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-7H.9.3.5 — retry_budget_ref [proposed]: Requires declared technical budget. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-7H.9.3.6 — retry_policy_ref [proposed]: Requires applicable policy. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-7H.9.3.7 — retry_authorization_ref [proposed]: Requires actual case authority. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Changes: ACCEPTED — C-7H.9.3.4 — retry_state_record [proposed]: Appends canonical retry state. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9 — B9 retry-state architecture | Identity and state. | Binds attempts. | No schema mutation. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: C-7H.9.3.1 — retry_group_id [proposed]; C-7H.9.3.2 — attempt_id [proposed]; C-7H.9.3.3 — retry_request_op_id [proposed]; C-7H.9.3.4 — retry_state_record [proposed]; C-7H.9.3.5 — retry_budget_ref [proposed]; C-7H.9.3.6 — retry_policy_ref [proposed]; C-7H.9.3.7 — retry_authorization_ref [proposed]

### C-7H.9.3.1 — retry_group_id [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — One proposed deterministic group per source canonical duplicate-prevention key and operation class. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — enqueue_key, ingestion claim, promotion_claim_key or reread claim as appropriate. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Establishes or finds the single group for that source identity. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — retry_group_id [proposed]. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Create another group merely to bypass its recorded state. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.3 — B9 identities and external state | Source key/class. | Identifies group. | Stable retry scope. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] |
| 2 · ACCEPTED | C-7H.10.9.4 — New retry-episode identity and lineage | Canonical source group. | Binds group plus episode_number [proposed]. | No second meaning for group identity. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.9.3.2 — attempt_id [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — Proposed deterministic identity from retry_group_id and permanent attempt number. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The group and its next unused attempt number. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Identifies the admitted attempt and links the launched seam parent operation. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — attempt_id [proposed]. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Duplicate the seam's own parent/child identities or logs. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.3 — B9 identities and external state | Group/number. | Identifies attempt. | Unique attempt. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] |
| 2 · ACCEPTED | C-7H.9.3.4.3 — Retry attempt entry | attempt_id [proposed]. | Binds entry. | Unique attempt pointer. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.9.3.3 — retry_request_op_id [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — Proposed parent identity for one lookup/admission/outcome/disposition request. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Takes in: ACCEPTED — The actual caller invocation and separately executed children. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Does: ACCEPTED — Gives children distinct operation identities/logs and the parent one terminal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Gives out: ACCEPTED — A linked request operation trail. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Must never: ACCEPTED — Acknowledge before the durable parent terminal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Missing terminal is recovered before acknowledgement. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.3 — B9 identities and external state | Invocation. | Tracks children. | One parent terminal. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.9.3.4 — retry_state_record [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — One proposed append-only canonical record set per retry group. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — Source identity/class, prior outcome references, attempt entries and dispositions. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Preserves these machine facts separately from operational logs. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — Durable retry state. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Count state records as extra evidential votes. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Unreadable or contradictory state cannot authorize admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: ACCEPTED — C-7H.9.3.4.1 — Retry source identity and class: Carries source binding. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.9.3.4.2 — Classified prior outcome references: Carries classified outcomes. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7H.9.3.4.3 — Retry attempt entry: Carries admitted attempt entries. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Changes: ACCEPTED — C-7H.9.3.4.4 — Retry disposition events: Carries disposition changes. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.3 — B9 identities and external state | Outcomes/attempts. | Preserves references. | Durable bookkeeping. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: C-7H.9.3.4.1 — Retry source identity and class; C-7H.9.3.4.2 — Classified prior outcome references; C-7H.9.3.4.3 — Retry attempt entry; C-7H.9.3.4.4 — Retry disposition events

### C-7H.9.3.4.1 — Retry source identity and class
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The state set's source-operation binding. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — Canonical key and operation class. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Preserves which seam operation the group belongs to. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — Source identity/class references. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Substitute another source identity silently. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.3.4 — retry_state_record [proposed] | Key/class. | Preserves identity. | No identity substitution. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.9.3.4.2 — Classified prior outcome references
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The state set's durable source-outcome history. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — Prior terminal evidence and mechanical classifications. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Records references rather than duplicated outcome content. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — Classified outcome references. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Guess source success. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Unreadable or contradictory evidence fails closed. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.3.4 — retry_state_record [proposed] | Durable refs. | Preserves history. | No inferred success. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.9.3.4.3 — Retry attempt entry
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The canonical state entry for an admitted attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — attempt_id [proposed], class, admission evidence, seam parent-op ref, durable outcome ref and resulting class. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Preserves the attempt's authority, execution linkage and actual resolution. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — An append-only attempt entry. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Invent a result before durable seam evidence exists. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — An attempt without a durable terminal remains unresolved. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: ACCEPTED — C-7H.9.3.2 — attempt_id [proposed]: Uses existing attempt identity. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.9.3.4.3.1 — Retry attempt class: Records attempt kind. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.9.3.4.3.3 — Retry seam parent-operation reference: Links launched seam operation. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.9.3.4.3.4 — Retry durable outcome reference: Links proven terminal evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.9.3.4.3.5 — Retry resulting class: Records resulting routing class. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-7H.9.3.4.3.2 — Retry admission evidence: Binds exact admission authority. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.3.4 — retry_state_record [proposed] | Attempt facts. | Appends state. | Traceable execution. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] |
| 2 · ACCEPTED | C-7H.9.3.4.3.3 — Retry seam parent-operation reference | Seam parent identity. | References its separate execution trail. | No copied logs. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: C-7H.9.3.4.3.1 — Retry attempt class; C-7H.9.3.4.3.2 — Retry admission evidence; C-7H.9.3.4.3.3 — Retry seam parent-operation reference; C-7H.9.3.4.3.4 — Retry durable outcome reference; C-7H.9.3.4.3.5 — Retry resulting class

### C-7H.9.3.4.3.1 — Retry attempt class
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The attempt entry's technical, substantive or policy-authorized kind. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The admitted attempt's class. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Records that class. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — Attempt-kind provenance. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.3.4.3 — Retry attempt entry | Class. | Preserves routing type. | Typed execution. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.9.3.4.3.2 — Retry admission evidence
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The exact budget or policy/authorization references bound at admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The references that permitted this attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Preserves them with the entry. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — Traceable admission authority. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Substitute later or missing authorization. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Unproven authority cannot permit execution. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.3.4.3 — Retry attempt entry | Evidence refs. | Records permission. | No hidden execution. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.9.3.4.3.3 — Retry seam parent-operation reference
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The identity of the source operation launched by the admitted attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — That seam parent operation's identity. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Links its independent parent/child execution trail. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — A source parent-op reference. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Duplicate the seam's logs. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.3.4.3 — Retry attempt entry: Binds the actual admitted source operation. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.3.4.3 — Retry attempt entry | Parent-op ref. | Preserves source lineage. | No duplicate source log. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.9.3.4.3.4 — Retry durable outcome reference
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The source terminal evidence resolving an attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — A readable durable source terminal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Records its reference lookup-first. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — Outcome evidence binding. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Infer a terminal from incomplete bookkeeping. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — No durable terminal leaves the attempt unresolved. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.3.4.3 — Retry attempt entry | Outcome ref. | Records resolution. | No invented outcome. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.9.3.4.3.5 — Retry resulting class
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The routing class of the attempt's proven outcome. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — Durable outcome classification. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Records the resulting class. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — Mechanical next-routing state. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Rescore the outcome's meaning. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Contradictory evidence becomes indeterminate. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.3.4.3 — Retry attempt entry | Classification. | Preserves next status. | No meaning rescore. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.9.3.4.4 — Retry disposition events
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — Append-only group-state changes. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — A changed group disposition. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Records the change before the request's terminal log. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — A durable disposition trail. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Rewrite prior dispositions. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Parent acknowledgement waits for its durable terminal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.3.4 — retry_state_record [proposed] | Actual change. | Appends event. | No rewrite. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.9.3.5 — retry_budget_ref [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — Proposed reference to declared count/timing/backoff configuration for class and seam. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — An existing configured budget record. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Binds its exact terms at technical admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — retry_budget_ref [proposed]. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Supply a silent default budget. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Missing, unreadable or unconfigured budget blocks admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.3 — B9 identities and external state | Budget ref. | Binds terms. | No defaults. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] |
| 2 · ACCEPTED | C-7H.9.2.1 — Technical retry kind | Existing declared retry budget. | Proceeds only when the attempt is admitted only within its declared budget. | Nothing in this card. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7H.9.3.6 — retry_policy_ref [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — Proposed reference to adopted substantive or explicit retry policy. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The applicable policy record. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Binds the policy that authorizes the retry kind. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — retry_policy_ref [proposed]. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Invent permission from an outcome alone. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Missing policy blocks admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.3 — B9 identities and external state | Policy ref. | Binds authority. | No invented permission. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] |
| 2 · ACCEPTED | C-7H.9.2.2 — Substantive retry kind | Adopted retry policy and per-case authorization references. | Proceeds only when the adopted policy and the per-case authorization both allow the attempt. | Nothing in this card. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] |
| 3 · ACCEPTED | C-7H.9.2.3 — Policy-authorized retry kind | The applicable policy and recorded authorization reference. | Proceeds only when the R1 checks pass and the required policy and case authority exist and are satisfied. | Nothing in this card. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.9.3.7 — retry_authorization_ref [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — Proposed per-case authorization reference. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — Durable authorization for the actual case. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Binds that exact authority at admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — retry_authorization_ref [proposed]. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Reuse unrelated case authority. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Missing authorization blocks admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.3 — B9 identities and external state | Authorization ref. | Binds this case. | No unrelated authority. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §4] |
| 2 · ACCEPTED | C-7H.9.2.2 — Substantive retry kind | Adopted retry policy and per-case authorization references. | Proceeds only when the adopted policy and the per-case authorization both allow the attempt. | Nothing in this card. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] |
| 3 · ACCEPTED | C-7H.9.2.3 — Policy-authorized retry kind | The applicable policy and recorded authorization reference. | Proceeds only when the R1 checks pass and the required policy and case authority exist and are satisfied. | Nothing in this card. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.9.4 — B9 R0–R4 transaction sequence
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The admitted same-operation retry sequence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — Canonical group state and source evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Looks up, atomically admits, executes through the original seam, records proven outcome, then writes disposition and parent terminal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — One honestly resolved retry request. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Execute before admission or acknowledge before terminal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Unprovable state blocks progress. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: ACCEPTED — C-7H.9.4.1 — R0 — Retry group lookup: Begins with group lookup. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-7H.9.4.4 — R3 — Retry outcome recording: Records only durable source outcome. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Gated by: ACCEPTED — C-7H.9.4.2 — R1 — Retry attempt admission: Requires single-winner admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Changes: ACCEPTED — C-7H.9.4.3 — R2 — Source-seam execution: Executes only through source boundaries. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Changes: ACCEPTED — C-7H.9.4.5 — R4 — Disposition and retry terminal: Closes request before acknowledgement. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9 — B9 retry-state architecture | Durable state. | Runs R0–R4. | No hidden retry. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] |
| 2 · ACCEPTED | C-7H.9.4.1 — R0 — Retry group lookup | Group state. | Routes R0. | Protected refusals. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] |
| 3 · ACCEPTED | C-7H.9.4.2 — R1 — Retry attempt admission | Admission evidence. | Commits once. | Exclusive execution. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] |
| 4 · ACCEPTED | C-7H.9.4.3 — R2 — Source-seam execution | R1 evidence. | Uses original seam. | No alternate path. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] |
| 5 · ACCEPTED | C-7H.9.4.4 — R3 — Retry outcome recording | Source evidence. | Records proven status. | No false terminal. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] |
| 6 · ACCEPTED | C-7H.9.4.5 — R4 — Disposition and retry terminal | Actual outcomes. | Closes once. | No premature acknowledgement. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] |

SUB-PARTS: C-7H.9.4.1 — R0 — Retry group lookup; C-7H.9.4.2 — R1 — Retry attempt admission; C-7H.9.4.3 — R2 — Source-seam execution; C-7H.9.4.4 — R3 — Retry outcome recording; C-7H.9.4.5 — R4 — Disposition and retry terminal

### C-7H.9.4.1 — R0 — Retry group lookup
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — Read-only establishment/lookup and latest-class routing. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — Canonical identity and latest outcome. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Absorbs success; refuses substantive without policy/case refs, held, indeterminate or privacy-refused without changed authorization. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — Absorption, refusal or an admissible-class candidate. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Admit on unreadable group evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Unprovable state fails closed. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.4 — B9 R0–R4 transaction sequence: Latest class and source evidence govern. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.4 — B9 R0–R4 transaction sequence | Latest state. | Absorbs/refuses/routes. | No unprovable admission. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.9.4.2 — R1 — Retry attempt admission
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — One atomic compare-and-commit before any B9 execution. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — Admissible class, no live group attempt and satisfied budget or policy/case references. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Commits one attempt with its exact admission evidence; racing losers observe and append nothing. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — One admitted attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Execute without committed admission, silently default missing policy or allow two live attempts. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Missing/unconfigured/unsatisfied references mean no attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.4 — B9 R0–R4 transaction sequence: No live attempt and satisfied references required. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.4 — B9 R0–R4 transaction sequence | Authority and live state. | Commits one attempt. | No hidden retry. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] |
| 2 · ACCEPTED | C-7H.10.4 — Technical admission under both bounds | Eligibility evidence. | Compare-and-commits admission. | No overlapping winners. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-7H.9.2.1 — Technical retry kind | Existing declared retry budget. | Proceeds only when the attempt is admitted only within its declared budget. | Nothing in this card. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] |
| 4 · ACCEPTED | C-7H.9.2.3 — Policy-authorized retry kind | The applicable policy and recorded authorization reference. | Proceeds only when the R1 checks pass and the required policy and case authority exist and are satisfied. | Nothing in this card. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.9.4.3 — R2 — Source-seam execution
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — Execution through the source's own boundaries and unchanged canonical key. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — A committed admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Launches a new seam parent operation referenced by the attempt; the seam's identity remains the sole execution duplicate defense. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — The seam's own outcome for R3. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Create an alternate execution path or reimplement the source seam. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Source refusal/failure follows its own contract. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.4 — B9 R0–R4 transaction sequence: Committed admission is mandatory. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.4 — B9 R0–R4 transaction sequence | Admitted attempt. | Launches same-identity seam. | Source duplicate defense. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.9.4.4 — R3 — Retry outcome recording
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — Lookup-first resolution from durable source terminal evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — The source terminal and attempt identity. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Appends its reference and resulting class once. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — Proven outcome or unresolved attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Guess an outcome when no terminal exists. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Contradictory/unreadable evidence makes the group indeterminate. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.4 — B9 R0–R4 transaction sequence: Only durable source terminals resolve outcomes. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.4 — B9 R0–R4 transaction sequence | Terminal evidence. | Appends resolution. | No guessed success. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.9.4.5 — R4 — Disposition and retry terminal
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — Disposition change followed by one parent terminal per retry_request_op_id [proposed]. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — Resolved child outcomes and changed group disposition. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Records disposition where changed, then appends the single terminal before acknowledgement. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — A durable resolved request. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Acknowledge before terminal or duplicate it. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Recovery appends only the missing terminal from recorded evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.4 — B9 R0–R4 transaction sequence: Children resolve before durable parent terminal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.4 — B9 R0–R4 transaction sequence | Resolved children. | Writes disposition/terminal. | Durable response. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] |
| 2 · ACCEPTED | C-7H.9.7.7 — retry_terminal [proposed] | Resolved request. | Closes once. | No duplicate terminal. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.9.5 — B9 nine idempotency boundaries
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Group, admission, execution, outcome, absorption, authority binding, parent, child and recovery uniqueness. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — Their canonical identities and committed evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Preserves one group per source, one live deterministic attempt, one seam result, one outcome record per attempt/terminal, success absorption, exact admission reference, one parent terminal, one child log and recovery_run_id lookup-first no-ops. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — Repeated calls converge without extra work or evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Treat additional attempts as additional committed results or truth votes. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Conflicting identity evidence fails closed. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.5.1 — Retry-group uniqueness: Preserves one group. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7H.9.5.2 — Retry-admission uniqueness: Preserves one live attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7H.9.5.3 — Source execution duplicate defense: Preserves source execution identity. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7H.9.5.4 — Retry-outcome append-once rule: Preserves outcome append-once. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7H.9.5.5 — Successful-group absorption: Preserves success absorption. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7H.9.5.6 — Exact admission-reference binding: Preserves exact authority binding. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7H.9.5.7 — Retry-parent terminal uniqueness: Preserves one parent terminal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7H.9.5.8 — Retry-child log uniqueness: Preserves one child log. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7H.9.5.9 — Retry-recovery uniqueness: Preserves recovery convergence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9 — B9 retry-state architecture | Canonical identities. | Converges effects. | One source result. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7H.9.5.1 — Retry-group uniqueness | Group key. | Looks up first. | One retry group. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-7H.9.5.2 — Retry-admission uniqueness | Live attempt state. | Commits once. | No overlap. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6] |
| 4 · ACCEPTED | C-7H.9.5.3 — Source execution duplicate defense | Admitted execution. | Preserves seam defense. | One source result. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6] |
| 5 · ACCEPTED | C-7H.9.5.4 — Retry-outcome append-once rule | Attempt and terminal ref. | Appends once. | No fabricated success. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6] |
| 6 · ACCEPTED | C-7H.9.5.5 — Successful-group absorption | Completed result. | Returns existing output. | No re-execution. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6] |
| 7 · ACCEPTED | C-7H.9.5.6 — Exact admission-reference binding | Exact reference. | Binds once. | No silent substitution. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6] |
| 8 · ACCEPTED | C-7H.9.5.7 — Retry-parent terminal uniqueness | Parent op ID. | Finds or appends terminal. | Acknowledgement follows. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6] |
| 9 · ACCEPTED | C-7H.9.5.8 — Retry-child log uniqueness | Child op ID. | Looks up before logging. | No duplication. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6] |
| 10 · ACCEPTED | C-7H.9.5.9 — Retry-recovery uniqueness | Recovery run ID. | Returns existing resolution. | No replay. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6] |

SUB-PARTS: C-7H.9.5.1 — Retry-group uniqueness; C-7H.9.5.2 — Retry-admission uniqueness; C-7H.9.5.3 — Source execution duplicate defense; C-7H.9.5.4 — Retry-outcome append-once rule; C-7H.9.5.5 — Successful-group absorption; C-7H.9.5.6 — Exact admission-reference binding; C-7H.9.5.7 — Retry-parent terminal uniqueness; C-7H.9.5.8 — Retry-child log uniqueness; C-7H.9.5.9 — Retry-recovery uniqueness

### C-7H.9.5.1 — Retry-group uniqueness
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — One retry_group_id [proposed] per canonical source identity. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — The source key/class. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Converges group establishment. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — One group ever. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Duplicate the group to evade state. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.5 — B9 nine idempotency boundaries: Canonical source identity governs uniqueness. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.5 — B9 nine idempotency boundaries | Source identity. | Converges group. | No state evasion. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.9.5.2 — Retry-admission uniqueness
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Single-winner compare-and-commit with deterministic attempt_id [proposed]. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — Group and live-attempt evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Admits at most one live attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — One admitted execution. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Admit another live attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Existing live work blocks admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.5 — B9 nine idempotency boundaries: Atomic admission chooses one winner. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.5 — B9 nine idempotency boundaries | Live state. | Admits one winner. | No duplicate work. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.9.5.3 — Source execution duplicate defense
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The source seam's canonical identity remains the sole execution defense. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — Every admitted same-identity attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Allows at most its one committed result across attempts. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — One source result. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Replace source idempotency with B9 bookkeeping. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Source refusal rules govern. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.5 — B9 nine idempotency boundaries: Source identity remains authoritative. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.5 — B9 nine idempotency boundaries | Canonical key. | Uses seam defense. | One source result. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.9.5.4 — Retry-outcome append-once rule
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Attempt plus durable source-terminal reference identifies outcome recording. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — Proven terminal evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Looks up first and appends once. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — One recorded outcome binding. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Duplicate or infer the terminal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Unprovable evidence remains unresolved. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.5 — B9 nine idempotency boundaries: Durable terminal must prove the outcome. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.5 — B9 nine idempotency boundaries | Attempt/terminal. | Records once. | No duplicate outcome. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.9.5.5 — Successful-group absorption
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — terminal_success absorbs every later retry request. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — The committed result. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Returns it without execution. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — Existing output. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Retry success. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — No admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.5 — B9 nine idempotency boundaries: Success absorbs later requests. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.5 — B9 nine idempotency boundaries | Committed result. | Returns it. | No re-execution. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.9.5.6 — Exact admission-reference binding
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The budget or policy/case reference actually used by admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — The exact authority record. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Stores the binding; repeated admission finds the existing entry. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — Immutable admission provenance. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Substitute another authority silently. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Missing authority prevents admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.5 — B9 nine idempotency boundaries: Actual admission authority is immutable. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.5 — B9 nine idempotency boundaries | Admission refs. | Reuses committed entry. | No substituted authority. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.9.5.7 — Retry-parent terminal uniqueness
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — One terminal per retry_request_op_id [proposed]. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — The request identity. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Finds or appends its single terminal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — One durable request outcome. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Duplicate parent closure. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — No acknowledgement before terminal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.5 — B9 nine idempotency boundaries: Each request has one terminal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.5 — B9 nine idempotency boundaries | Request ID. | Closes once. | No repeated terminal. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.9.5.8 — Retry-child log uniqueness
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — One log per actual child operation identity. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — Child op ID. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Locates the existing log on repeated bookkeeping. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — One child log. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Duplicate the operation log. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.5 — B9 nine idempotency boundaries: Each child log names its actual operation. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.5 — B9 nine idempotency boundaries | Child ID. | Logs once. | No evidence inflation. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.9.5.9 — Retry-recovery uniqueness
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — recovery_run_id and lookup-first convergence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — Durable recovery findings. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Returns committed findings without repeated effects. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — A no-op on repeated recovery. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Reapply committed changes. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Unreadable evidence remains blocked. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.5 — B9 nine idempotency boundaries: Recovery converges on committed findings. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.5 — B9 nine idempotency boundaries | Recovery ID. | Looks up first. | No repeated effects. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.9.6 — B9 nineteen recovery cases
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Lookup-first recovery around, never in place of, the source seam's authority. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §9]
- Takes in: ACCEPTED — Durable retry and source evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §9]
- Does: ACCEPTED — Completes missing records or resumes only admitted work; refusals preserve protected states. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §9]
- Gives out: ACCEPTED — Honest absorption, refusal, execution continuation or indeterminate recovery. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §9]
- Must never: ACCEPTED — Fabricate sources/outcomes, bypass admission or repeat committed results. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Unreadable or contradictory evidence blocks admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §9]

TOGETHER
- Fed by: ACCEPTED — C-7H.9.6.1 — B9 recovery 1 — Before retry state: Handles pre-state crash. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fed by: ACCEPTED — C-7H.9.6.2 — B9 recovery 2 — Admitted but unlaunched: Handles unlaunched admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fed by: ACCEPTED — C-7H.9.6.4 — B9 recovery 4 — Retry terminal absent: Handles missing retry parent log. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fed by: ACCEPTED — C-7H.9.6.5 — B9 recovery 5 — Acknowledgement absent: Handles lost acknowledgement. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fed by: ACCEPTED — C-7H.9.6.6 — B9 recovery 6 — Duplicate retry request: Handles duplicate request. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fed by: ACCEPTED — C-7H.9.6.12 — B9 recovery 12 — Timeout: Handles retryable timeout. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fed by: ACCEPTED — C-7H.9.6.17 — B9 recovery 17 — Source done, retry record incomplete: Handles source done/bookkeeping incomplete. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fed by: ACCEPTED — C-7H.9.6.18 — B9 recovery 18 — Duplicate recovery run: Handles repeat recovery. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-7H.9.6.3 — B9 recovery 3 — Source terminal absent: Handles missing source terminal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-7H.9.6.7 — B9 recovery 7 — Retry after success: Handles retry after success. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-7H.9.6.8 — B9 recovery 8 — Retry after permanent rejection: Handles permanent rejection. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-7H.9.6.9 — B9 recovery 9 — Retry while held: Handles held source. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-7H.9.6.10 — B9 recovery 10 — Indeterminate source: Handles indeterminate source. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-7H.9.6.11 — B9 recovery 11 — Privacy refusal: Handles privacy refusal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-7H.9.6.13 — B9 recovery 13 — Admission race: Handles race or contradiction. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-7H.9.6.14 — B9 recovery 14 — Unavailable or exhausted budget: Handles missing/exhausted budget. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-7H.9.6.15 — B9 recovery 15 — Missing source operation: Handles missing source identity. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-7H.9.6.16 — B9 recovery 16 — Missing or contradictory outcome: Handles missing/contradictory outcome. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-7H.9.6.19 — B9 recovery 19 — Hidden admission bypass: Handles hidden admission bypass. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9 — B9 retry-state architecture | Interrupted state. | Completes missing records. | No guessed outcome. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7H.9.6.1 — B9 recovery 1 — Before retry state | Pre-state crash. | Starts lookup. | No invented history. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |
| 3 · ACCEPTED | C-7H.9.6.2 — B9 recovery 2 — Admitted but unlaunched | Unlaunched attempt. | Launches or abandons. | No overlap. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |
| 4 · ACCEPTED | C-7H.9.6.3 — B9 recovery 3 — Source terminal absent | Unresolved source. | Blocks admission. | No guess. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |
| 5 · ACCEPTED | C-7H.9.6.4 — B9 recovery 4 — Retry terminal absent | Disposition. | Completes parent. | No rerun. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |
| 6 · ACCEPTED | C-7H.9.6.5 — B9 recovery 5 — Acknowledgement absent | Recorded outcome. | Returns it. | No second terminal. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |
| 7 · ACCEPTED | C-7H.9.6.6 — B9 recovery 6 — Duplicate retry request | Group state. | Absorbs/refuses. | One live attempt. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |
| 8 · ACCEPTED | C-7H.9.6.7 — B9 recovery 7 — Retry after success | Committed result. | Absorbs. | No execution. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |
| 9 · ACCEPTED | C-7H.9.6.8 — B9 recovery 8 — Retry after permanent rejection | Missing refs. | Refuses. | No machine retry. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |
| 10 · ACCEPTED | C-7H.9.6.9 — B9 recovery 9 — Retry while held | Owner state. | Refuses. | No queue around hold. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |
| 11 · ACCEPTED | C-7H.9.6.10 — B9 recovery 10 — Indeterminate source | Unresolved evidence. | Refuses. | No recovery bypass. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |
| 12 · ACCEPTED | C-7H.9.6.11 — B9 recovery 11 — Privacy refusal | Gate record. | Checks authority. | No privacy bypass. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |
| 13 · ACCEPTED | C-7H.9.6.12 — B9 recovery 12 — Timeout | Budget evidence. | Evaluates admission. | No automatic bypass. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |
| 14 · ACCEPTED | C-7H.9.6.13 — B9 recovery 13 — Admission race | Race/conflict. | Converges or stops. | Integrity protected. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |
| 15 · ACCEPTED | C-7H.9.6.14 — B9 recovery 14 — Unavailable or exhausted budget | Reference/state. | Refuses failure. | No default numbers. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |
| 16 · ACCEPTED | C-7H.9.6.15 — B9 recovery 15 — Missing source operation | Missing operation. | Requires recovery. | No fabrication. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |
| 17 · ACCEPTED | C-7H.9.6.16 — B9 recovery 16 — Missing or contradictory outcome | Outcome evidence. | Stops on conflict. | No guessed success. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |
| 18 · ACCEPTED | C-7H.9.6.17 — B9 recovery 17 — Source done, retry record incomplete | Completed source. | Completes bookkeeping. | No re-execution. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |
| 19 · ACCEPTED | C-7H.9.6.18 — B9 recovery 18 — Duplicate recovery run | Recovery ID. | Returns findings. | No reapplied effects. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |
| 20 · ACCEPTED | C-7H.9.6.19 — B9 recovery 19 — Hidden admission bypass | Unauthorized attempt. | Refuses/logs. | No hidden execution. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |

SUB-PARTS: C-7H.9.6.1 — B9 recovery 1 — Before retry state; C-7H.9.6.2 — B9 recovery 2 — Admitted but unlaunched; C-7H.9.6.3 — B9 recovery 3 — Source terminal absent; C-7H.9.6.4 — B9 recovery 4 — Retry terminal absent; C-7H.9.6.5 — B9 recovery 5 — Acknowledgement absent; C-7H.9.6.6 — B9 recovery 6 — Duplicate retry request; C-7H.9.6.7 — B9 recovery 7 — Retry after success; C-7H.9.6.8 — B9 recovery 8 — Retry after permanent rejection; C-7H.9.6.9 — B9 recovery 9 — Retry while held; C-7H.9.6.10 — B9 recovery 10 — Indeterminate source; C-7H.9.6.11 — B9 recovery 11 — Privacy refusal; C-7H.9.6.12 — B9 recovery 12 — Timeout; C-7H.9.6.13 — B9 recovery 13 — Admission race; C-7H.9.6.14 — B9 recovery 14 — Unavailable or exhausted budget; C-7H.9.6.15 — B9 recovery 15 — Missing source operation; C-7H.9.6.16 — B9 recovery 16 — Missing or contradictory outcome; C-7H.9.6.17 — B9 recovery 17 — Source done, retry record incomplete; C-7H.9.6.18 — B9 recovery 18 — Duplicate recovery run; C-7H.9.6.19 — B9 recovery 19 — Hidden admission bypass

### C-7H.9.6.1 — B9 recovery 1 — Before retry state
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — No retry-state record was committed. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Takes in: ACCEPTED — The unchanged authoritative source state. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Does: ACCEPTED — Next request runs R0 normally; nothing requires rollback. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gives out: ACCEPTED — Normal lookup. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Must never: ACCEPTED — Invent lost retry state. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.6 — B9 nineteen recovery cases: Source state remains authoritative. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.6 — B9 nineteen recovery cases | Source state. | Runs R0 next. | No rollback fiction. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7H.9.6.2 — B9 recovery 2 — Admitted but unlaunched
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — Admission exists without a seam parent-op reference. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Takes in: ACCEPTED — The committed attempt entry. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Does: ACCEPTED — Launches R2 under the same identity or appends attempt-abandoned with cause to release admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gives out: ACCEPTED — Source execution or recorded abandonment. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Must never: ACCEPTED — Create another live attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Source idempotency remains the duplicate defense. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.6 — B9 nineteen recovery cases: Existing admission remains unique. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.6 — B9 nineteen recovery cases | Attempt entry. | Launches or abandons. | No second live attempt. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7H.9.6.3 — B9 recovery 3 — Source terminal absent
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — An attempt launched but lacks durable terminal evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Takes in: ACCEPTED — Source operation and recovery state. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Does: ACCEPTED — Resolves through the source's own recovery first and records only what it proves. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gives out: ACCEPTED — An unresolved attempt until proven resolution. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Must never: ACCEPTED — Invent an outcome or admit another live attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Group admission remains blocked while unresolved/live. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.6 — B9 nineteen recovery cases: Seam recovery must prove outcome first. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.6 — B9 nineteen recovery cases | Source recovery. | Waits for proof. | No invented outcome. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7H.9.6.4 — B9 recovery 4 — Retry terminal absent
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — Attempt terminal exists but the retry-request parent log is missing. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Takes in: ACCEPTED — Recorded disposition and outcome evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Does: ACCEPTED — Appends the missing R4 terminal idempotently. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gives out: ACCEPTED — Completed parent terminal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Must never: ACCEPTED — Re-execute the source operation. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Acknowledgement waits for the durable terminal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.6 — B9 nineteen recovery cases: Durable evidence supports missing terminal only. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.6 — B9 nineteen recovery cases | Disposition. | Completes R4. | Acknowledgement gated. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7H.9.6.5 — B9 recovery 5 — Acknowledgement absent
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — Terminal log exists but acknowledgement was lost. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Takes in: ACCEPTED — The durable parent terminal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Does: ACCEPTED — Returns it without re-execution or another terminal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gives out: ACCEPTED — Existing outcome response. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Must never: ACCEPTED — Repeat work or terminal logging. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.6 — B9 nineteen recovery cases: Existing terminal absorbs response recovery. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.6 — B9 nineteen recovery cases | Terminal. | Returns it. | No execution repeat. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7H.9.6.6 — B9 recovery 6 — Duplicate retry request
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — A repeated request against the current group. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Takes in: ACCEPTED — Latest class and live-attempt evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Does: ACCEPTED — R0 absorbs or refuses appropriately and returns recorded status. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gives out: ACCEPTED — Current group resolution. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Must never: ACCEPTED — Admit a second live attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Existing class rules still govern. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.6 — B9 nineteen recovery cases: Latest class governs repeated requests. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.6 — B9 nineteen recovery cases | Latest class. | Absorbs/refuses. | One live attempt. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7H.9.6.7 — B9 recovery 7 — Retry after success
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — A retry request after committed success. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Takes in: ACCEPTED — The committed source result. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Does: ACCEPTED — Absorbs and returns terminal_success without another attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gives out: ACCEPTED — Existing result. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Must never: ACCEPTED — Re-execute success. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — No new attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.6 — B9 nineteen recovery cases: Success can never be retried. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.6 — B9 nineteen recovery cases | Committed result. | Absorbs. | No retry. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7H.9.6.8 — B9 recovery 8 — Retry after permanent rejection
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — Terminal substantive outcome without required policy/case authority. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Takes in: ACCEPTED — The rejection and missing authority references. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Does: ACCEPTED — Refuses, naming the missing references. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gives out: ACCEPTED — Recorded terminal refusal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Must never: ACCEPTED — Automatically retry permanent rejection. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Nothing executes. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.6 — B9 nineteen recovery cases: Permanent rejection needs policy/case authority. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.6 — B9 nineteen recovery cases | Authority absence. | Refuses. | Terminal preserved. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7H.9.6.9 — B9 recovery 9 — Retry while held
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — A live dependency hold. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Takes in: ACCEPTED — The owning hold record. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Does: ACCEPTED — Refuses and records, waiting for the release interface. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gives out: ACCEPTED — Blocked group status. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Must never: ACCEPTED — Admit around the hold. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — No attempt is admitted. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.6 — B9 nineteen recovery cases: Live hold blocks admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.6 — B9 nineteen recovery cases | Hold state. | Refuses. | Owner release required. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7H.9.6.10 — B9 recovery 10 — Indeterminate source
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — A source still requiring indeterminate recovery. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Takes in: ACCEPTED — The source's unresolved integrity state. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Does: ACCEPTED — Refuses until the source's own recovery resolves it. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gives out: ACCEPTED — Recovery-first refusal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Must never: ACCEPTED — Use retry to bypass source recovery. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — No admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.6 — B9 nineteen recovery cases: Indeterminate source needs its own recovery. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.6 — B9 nineteen recovery cases | Recovery state. | Refuses. | Recovery first. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7H.9.6.11 — B9 recovery 11 — Privacy refusal
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — A retry after an access/privacy refusal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Takes in: ACCEPTED — The gate's changed-authorization evidence, if any. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Does: ACCEPTED — Refuses absent that record and logs under the gate's visibility rules. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gives out: ACCEPTED — Protected refusal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Must never: ACCEPTED — Retry around authorization. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — No changed authorization means no attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.6 — B9 nineteen recovery cases: Changed authorization must come from gate. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.6 — B9 nineteen recovery cases | Gate record. | Refuses unless changed. | No bypass. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7H.9.6.12 — B9 recovery 12 — Timeout
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — A technical timeout outcome. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Takes in: ACCEPTED — The durable timeout and declared budget. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Does: ACCEPTED — Uses normal R1 admission under the same canonical source identity. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gives out: ACCEPTED — A bounded eligible technical retry. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Must never: ACCEPTED — Infer automatic permission without the budget. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Unsatisfied admission prevents execution. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.6 — B9 nineteen recovery cases: Timeout still needs bounded R1 permission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.6 — B9 nineteen recovery cases | Budget and failure. | Evaluates R1. | Bounded retry. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7H.9.6.13 — B9 recovery 13 — Admission race
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — Competing retry attempts or conflicting group evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Takes in: ACCEPTED — R1 competitors and committed state. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Does: ACCEPTED — Admits one winner, leaves losers without appends and routes evidence contradictions to indeterminate. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gives out: ACCEPTED — One attempt or integrity block. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Must never: ACCEPTED — Guess between conflicting evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Contradictions fail closed. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.6 — B9 nineteen recovery cases: One winner and provable state required. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.6 — B9 nineteen recovery cases | Claim evidence. | One winner or stop. | No guessed winner. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7H.9.6.14 — B9 recovery 14 — Unavailable or exhausted budget
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — A missing, unconfigured or exhausted budget under its terms. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Takes in: ACCEPTED — The required reference and recorded state. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Does: ACCEPTED — Refuses, names the missing/exhausted reference in the fail-closed event and records the disposition block. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gives out: ACCEPTED — An honest budget refusal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Must never: ACCEPTED — Invent numbers, defaults or hidden retries. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — No attempt. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.6 — B9 nineteen recovery cases: Budget must be configured and satisfied. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.6 — B9 nineteen recovery cases | Budget ref. | Refuses and records. | No default. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7H.9.6.15 — B9 recovery 15 — Missing source operation
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — A group referencing an identity unknown to the seam. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Takes in: ACCEPTED — Unverifiable source-operation reference. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Does: ACCEPTED — Records indeterminate and surfaces resolution against source records. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gives out: ACCEPTED — Integrity recovery requirement. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Must never: ACCEPTED — Fabricate a source operation. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — No admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.6 — B9 nineteen recovery cases: Source identity must be known. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.6 — B9 nineteen recovery cases | Unverifiable source. | Marks indeterminate. | No fabricated operation. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7H.9.6.16 — B9 recovery 16 — Missing or contradictory outcome
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — Unreadable outcome evidence or two claimed terminals for one identity. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Takes in: ACCEPTED — Source terminal records. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Does: ACCEPTED — Waits for readable source evidence or marks contradictory terminals indeterminate as an integrity incident. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gives out: ACCEPTED — A surfaced recovery block. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Must never: ACCEPTED — Resolve competing terminals by guessing. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — No unprovable outcome authorizes execution. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.6 — B9 nineteen recovery cases: Only readable consistent terminals prove status. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.6 — B9 nineteen recovery cases | Source evidence. | Stops for recovery. | No coin-flip resolution. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7H.9.6.17 — B9 recovery 17 — Source done, retry record incomplete
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The source completed durably but R3/R4 bookkeeping is unfinished. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Takes in: ACCEPTED — The authoritative source terminal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Does: ACCEPTED — Completes only missing outcome/disposition/terminal records idempotently. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gives out: ACCEPTED — Complete retry bookkeeping. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Must never: ACCEPTED — Re-run the source result. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Only durable source evidence is authoritative. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.6 — B9 nineteen recovery cases: Durable source terminal is authoritative. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.6 — B9 nineteen recovery cases | Durable terminal. | Completes R3/R4. | No rerun. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7H.9.6.18 — B9 recovery 18 — Duplicate recovery run
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — Repeated recovery_run_id over append-only records. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Takes in: ACCEPTED — Existing committed findings. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Does: ACCEPTED — Re-reads and reapplies nothing. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gives out: ACCEPTED — recovery_noop [proposed]. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Must never: ACCEPTED — Repeat committed effects. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.6 — B9 nineteen recovery cases: Recovery repeats are lookup-first. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.6 — B9 nineteen recovery cases | Committed findings. | Returns no-op. | No repeated effects. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7H.9.6.19 — B9 recovery 19 — Hidden admission bypass
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — An attempted automatic retry without committed authorized R1 admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Takes in: ACCEPTED — The attempted bypass. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Does: ACCEPTED — Refuses and logs a fail-closed violation. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Gives out: ACCEPTED — A violation record with no execution. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Must never: ACCEPTED — Run hidden retries without budget or authority references. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — No B9 execution path exists before admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.6 — B9 nineteen recovery cases: R1 admission cannot be bypassed. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.6 — B9 nineteen recovery cases | Unauthorized attempt. | Refuses/logs. | No execution. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7H.9.7 — B9 operational event set
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — Proposed retry_requested, retry_absorbed, retry_refused, retry_attempt_admitted, retry_attempt_outcome_recorded, retry_group_disposition and retry_terminal, plus recovery_applied/recovery_noop/fail_closed_event. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Takes in: ACCEPTED — Actual R0 resolution, R1 winner, R3 outcome, disposition change, R4 terminal or recovery/failure. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Does: ACCEPTED — Logs each real operation once under its own identity; launched seam logs stay with their owner and are referenced only. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Gives out: ACCEPTED — Protected append-only operational provenance distinct from canonical state. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Must never: ACCEPTED — Log about logging, duplicate seam records as evidence or increase certainty through repetition. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Privacy internal-use, visibility and authority restrictions govern every record. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy internal-use, visibility and authority restrictions govern every record. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Changes: ACCEPTED — C-7H.9.7.1 — retry_requested [proposed]: Logs R0 request resolution. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Changes: ACCEPTED — C-7H.9.7.2 — retry_absorbed [proposed]: Logs absorption. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Changes: ACCEPTED — C-7H.9.7.3 — retry_refused [proposed]: Logs refusal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Changes: ACCEPTED — C-7H.9.7.4 — retry_attempt_admitted [proposed]: Logs admission winner. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Changes: ACCEPTED — C-7H.9.7.5 — retry_attempt_outcome_recorded [proposed]: Logs proven outcome recording. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Changes: ACCEPTED — C-7H.9.7.6 — retry_group_disposition [proposed]: Records group disposition change. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Changes: ACCEPTED — C-7H.9.7.7 — retry_terminal [proposed]: Logs single parent terminal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Changes: ACCEPTED — C-7H.6.7.1 — recovery_applied [proposed]: Reuses the shared applied-recovery event. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Changes: ACCEPTED — C-7H.6.7.2 — recovery_noop [proposed]: Reuses the shared no-op event. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Changes: ACCEPTED — C-7H.6.7.3 — fail_closed_event [proposed]: Reuses the shared fail-closed event. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9 — B9 retry-state architecture | Operation outcomes. | Records once. | Protected audit. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] |
| 2 · ACCEPTED | C-7H.9.7.1 — retry_requested [proposed] | Request identity. | Records request. | No double evidence. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] |
| 3 · ACCEPTED | C-7H.9.7.2 — retry_absorbed [proposed] | Committed success. | Logs absorption. | No new execution. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] |
| 4 · ACCEPTED | C-7H.9.7.3 — retry_refused [proposed] | Refusal cause. | Records it. | No hidden refusal. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] |
| 5 · ACCEPTED | C-7H.9.7.4 — retry_attempt_admitted [proposed] | Bound authority. | Logs winner. | No false admission. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] |
| 6 · ACCEPTED | C-7H.9.7.5 — retry_attempt_outcome_recorded [proposed] | Source terminal. | Records binding. | No inferred result. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] |
| 7 · ACCEPTED | C-7H.9.7.6 — retry_group_disposition [proposed] | Disposition transition. | Appends state. | No truth vote. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] |

SUB-PARTS: C-7H.9.7.1 — retry_requested [proposed]; C-7H.9.7.2 — retry_absorbed [proposed]; C-7H.9.7.3 — retry_refused [proposed]; C-7H.9.7.4 — retry_attempt_admitted [proposed]; C-7H.9.7.5 — retry_attempt_outcome_recorded [proposed]; C-7H.9.7.6 — retry_group_disposition [proposed]; C-7H.9.7.7 — retry_terminal [proposed]

### C-7H.9.7.1 — retry_requested [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed R0 request-resolution event. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Takes in: ACCEPTED — Actual request class/status. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Does: ACCEPTED — Logs the real request operation once. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Gives out: ACCEPTED — retry_requested [proposed]. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Must never: ACCEPTED — Create double evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.7 — B9 operational event set: Each actual request is logged once. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.7 — B9 operational event set | Class/status. | Records request. | One operation log. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.9.7.2 — retry_absorbed [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed R0 absorption event. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Takes in: ACCEPTED — A committed source result. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Does: ACCEPTED — Records absorption without re-execution. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Gives out: ACCEPTED — retry_absorbed [proposed]. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Must never: ACCEPTED — Imply a new result was created. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.7 — B9 operational event set: Absorption returns an existing result. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.7 — B9 operational event set | Existing success. | Records absorbed. | No new result. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.9.7.3 — retry_refused [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed R0 refusal event. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Takes in: ACCEPTED — The actual class and refusal status. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Does: ACCEPTED — Records the refused request once. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Gives out: ACCEPTED — retry_refused [proposed]. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Must never: ACCEPTED — Hide the refusal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Protected visibility rules govern its record. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.7 — B9 operational event set: Refusal retains actual classification. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.7 — B9 operational event set | Refusal class. | Records refused. | No hidden failure. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.9.7.4 — retry_attempt_admitted [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — The proposed R1 winner event with exact authority/configuration and anchor bindings. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Takes in: ACCEPTED — Committed admission evidence, including special no-gap/deadline-pending states where applicable. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Does: ACCEPTED — Logs the admission once. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Gives out: ACCEPTED — retry_attempt_admitted [proposed]. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Must never: ACCEPTED — Claim nonexistent anchors or a losing admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.7 — B9 operational event set: Only committed R1 winner is admitted. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.7 — B9 operational event set | Bound evidence. | Records admission. | Exact authority trail. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] |
| 2 · ACCEPTED | C-7H.10.12 — Values-layer state events | Configuration, episode and anchor evidence. | Logs the actual winner. | No duplicate event identity. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-7H.9.7.5 — retry_attempt_outcome_recorded [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed R3 event against durable source evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Takes in: ACCEPTED — The attempt's proven source terminal. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Does: ACCEPTED — Logs outcome recording once. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Gives out: ACCEPTED — retry_attempt_outcome_recorded [proposed]. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Must never: ACCEPTED — Infer uncommitted success. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.7 — B9 operational event set: Outcome logging needs durable proof. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.7 — B9 operational event set | Durable terminal. | Records the R3 outcome. | No inferred success. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.9.7.6 — retry_group_disposition [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed canonical state event for a changed group disposition. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Takes in: ACCEPTED — The real disposition change. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Does: ACCEPTED — Appends it without rewriting prior state. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Gives out: ACCEPTED — retry_group_disposition [proposed]. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Must never: ACCEPTED — Treat the state event as extra truth evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.7 — B9 operational event set: State event requires actual change. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.7 — B9 operational event set | Actual change. | Appends state. | No rewrite. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.9.7.7 — retry_terminal [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed single R4 parent event. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Takes in: ACCEPTED — Truthfully resolved children and disposition. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Does: ACCEPTED — Appends before acknowledgement. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Gives out: ACCEPTED — retry_terminal [proposed]. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Must never: ACCEPTED — Acknowledge first or append twice. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Missing terminal prevents acknowledgement. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9.4.5 — R4 — Disposition and retry terminal: R4 parent terminal precedes acknowledgement. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.9.7 — B9 operational event set | Resolved request. | Closes R4. | Acknowledgement gated. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.10 — Accepted B9 retry values and episodes
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — Declared retry bounds applied to the existing admission machinery. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Takes in: ACCEPTED — Durable attempts, recorded execution context and exact versioned configuration. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Does: ACCEPTED — Enforces both attempt and elapsed-time bounds; the first reached stops further retry, while gaps are minimum waits only. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Gives out: ACCEPTED — Bounded technical or careful-retry episodes with preserved unfinished work. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Must never: ACCEPTED — Force-cancel an in-flight source attempt, override its timeout, hide failure or turn a rejected draft into the answer. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Missing evidence/configuration admits nothing; exhausted or early-stopped episodes require a real recorded change before a new bounded episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

TOGETHER
- Fed by: ACCEPTED — C-7H.10.1 — b9_retry_budget_config [proposed]: Requires exact declared values. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.10.3 — Durable retry scheduling anchors: Uses durable timing evidence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7H.10.2 — Retry attempt and episode numbering: Separates permanent and episode counters. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Gated by: ACCEPTED — C-7H.10.4 — Technical admission under both bounds: Applies cumulative technical gates. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.10.5 — Later-episode ordinal-1 admission: Handles a new same-identity episode's first attempt. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.10.6 — Careful-retry and B24 fallback consumption: Consumes the exact careful-retry policy. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]
- Gated by: ACCEPTED — C-7H.10.7 — Retry early stop: Permits a recorded cause-bearing early stop. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-7H.10.8 — Retry exhaustion and preserved work: Closes an exhausted episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7H.10.9 — Real-change continuation records: Requires real change before continuation. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gated by: ACCEPTED — C-7H.10.10 — Values-layer crash reconstruction: Reconstructs only durable state. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Gated by: ACCEPTED — C-7H.10.11 — Values-layer fail-closed matrix: Refuses malformed admission evidence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gated by: ACCEPTED — C-7H.10.13 — Retry and hold-release seam: Respects external hold ownership. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §12]
- Changes: ACCEPTED — C-7H.10.12 — Values-layer state events: Logs real state changes once. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7H — Reread Lifecycle (§7H) | Attempt and time evidence. | Checks both limits. | Bounded continuation. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] |
| 2 · ACCEPTED | C-7H.9 — B9 retry-state architecture | Episode state. | Checks count/time. | No unbounded admission. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-7H.10.7 — Retry early stop | Unsafe/useless evidence. | Stops admission. | No success or ordinary-exhaustion disguise. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §8] |
| 4 · ACCEPTED | C-7H.10.8 — Retry exhaustion and preserved work | Count/time/final outcome. | Preserves work. | No continuation without new authority. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §9] |
| 5 · ACCEPTED | C-7H.10.11 — Values-layer fail-closed matrix | Fourteen source conditions. | Refuses with the real reason. | No default or guessed winner. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |
| 6 · ACCEPTED | C-7H.10.13 — Retry and hold-release seam | Recorded release and current source state. | Rechecks all gates. | No queued bypass. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §12] |
| 7 · ACCEPTED | C-7D.17.6 — B6 bounded technical retry | A technically retryable failure and recorded accepted B9 values. | Gates this place: limits and recorded values. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 8 · ACCEPTED | C-BOP.13.2 — BOP shared retry and committed-state recovery | Actual technical failure, committed checkpoints and per-item completion. | Supplies exact counts/waits/deadlines. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 9 · ACCEPTED | C-CREATE.10.4 — Creation bounded retry consumption | Actual retryable/terminal class, recorded context and durable admission authority. | Gates this place: consumes accepted bounds, episodes and real-change continuation. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| 10 · ACCEPTED | C-7O.10.2 — Result assessment never authorizes action retry | A partial, failed, unknown or cancelled result and any technical record-operation failure. | Supplies recorded retry values, unchanged. | Nothing in this card. | [V10 §7O] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.2] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 11 · ACCEPTED | C-7M.9 — Computed View operation and recovery contract | The operation identity, exact source/version set, declared record-level commit boundary and observed completion state. | Gates this place: recorded B9 values. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 12 · ACCEPTED | C-7P.13.1 — Authority-record operation and recovery contract | Stable operation identity, source/version set, commit boundary and existing or interrupted outcome. | Supplies recorded retry values. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 13 · ACCEPTED | C-8.16 — Research retry and committed recovery | Retryable or terminal stage failures and committed per-stage progress. | Gates this place: exact attempts, intervals and ceilings. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| 14 · ACCEPTED | C-OOP.8.3 — Bounded outcome technical retry | The actual failure class and durable prior attempt history. | Supplies exact accepted retry values. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| 15 · ACCEPTED | C-NEW-AIC.5.5 — Pre-generation B9 retry boundary | The same shared establishment identity and anchor, exact accepted `retry_budget_ref`, recorded schedule class and B9 R1 admission. | Gates this place: supplies the accepted bounds and real-change continuation rule. | Nothing in this card. | [04/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md §11] |
| 16 · ACCEPTED | C-7Q.11.10 — Privacy refusal and changed-authorization admission | The refused operation and any genuinely changed recorded authorization. | Supplies bounded values and real-change episode rules. | Nothing in this card. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |
| 17 · ACCEPTED | C-NEW-AIC.6.20 — Recovery after exhaustion or early stopping | B9's truthful exhaustion or early-stop record and the sealed or unsealed work state. | Gates this place: owns exhaustion and real-change continuation. | Nothing in this card. | [04/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md §12] |
| 18 · ACCEPTED | C-LMAC.10.1 — Same-query bounded transport retry | The unchanged query intent/context and technical failure. | Supplies exact accepted counts, waits and deadlines. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 19 · ACCEPTED | C-7Q.10 — Shared privacy-operation discipline | Committed operation state, the contract’s idempotency key, durable checkpoints and owner-defined failure class. | Supplies already accepted retry-value wiring. | Nothing in this card. | [04/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md §15] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] |
| 20 · ACCEPTED | C-7R.15.8.1 — Retrieval-system failure boundary | A retrieval-system failure, bounded B9 attempts and the terminal outcome. | Supplies accepted retry values and real-change boundary. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] |
| 21 · ACCEPTED | C-7D.17 — B6 operation integrity and recordkeeping | Stable identity, source/version set, declared commit boundary and actual committed outcome. | Gates this place: accepted retry values and episodes. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 22 · ACCEPTED | C-NEW-AIC.5.7 — Accepted retry values consumed by AIC | The exact accepted budget reference and the executing episode's recorded live or background schedule class. | Supplies the accepted values by reference. | Nothing in this card. | [04/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md §11] |
| 23 · ACCEPTED | C-24.18 — Connection technical retry boundary | A real technical failure and the same stable operation. | Gates this place: accepted retry values, without inventing new counts, gaps, timeouts or backoff. | Nothing in this card. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §17] |
| 24 · ACCEPTED | C-7M.9.5 — Computed View bounded technical retry | An eligible technical failure and its recorded retry references. | Gates this place: accepted values and episodes. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 25 · ACCEPTED | C-7N.11.6 — Surfacing technical-retry boundary | A classified failure under the stable operation identity. | Supplies the recorded Ness retry values. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 26 · ACCEPTED | C-7M.6.7 — Computed View retry_eligibility | The technical failure and the governing accepted retry rules. | Supplies accepted B9 values and episode rules. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |

SUB-PARTS: C-7H.10.1 — b9_retry_budget_config [proposed]; C-7H.10.2 — Retry attempt and episode numbering; C-7H.10.3 — Durable retry scheduling anchors; C-7H.10.4 — Technical admission under both bounds; C-7H.10.5 — Later-episode ordinal-1 admission; C-7H.10.6 — Careful-retry and B24 fallback consumption; C-7H.10.7 — Retry early stop; C-7H.10.8 — Retry exhaustion and preserved work; C-7H.10.9 — Real-change continuation records; C-7H.10.10 — Values-layer crash reconstruction; C-7H.10.11 — Values-layer fail-closed matrix; C-7H.10.12 — Values-layer state events; C-7H.10.13 — Retry and hold-release seam

### C-7H.10.1 — b9_retry_budget_config [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — A proposed append-only versioned configuration referenced by retry_budget_ref and applicable retry_policy_ref. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Takes in: ACCEPTED — Identity/version, technical count/gaps, elapsed limits, clock start, careful-retry limit/timing, early-stop and continuation rules. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Does: ACCEPTED — Stores the accepted values once and binds each admission to the exact version. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Gives out: ACCEPTED — A declared budget/policy record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Must never: ACCEPTED — Edit an existing version or silently change admission values. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Missing, unreadable or version-unbound configuration blocks admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

TOGETHER
- Fed by: ACCEPTED — C-7H.10.1.1 — Retry config_id [proposed]: Names the exact configuration. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.10.1.2 — Retry config_version [proposed]: Binds an immutable revision. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.10.1.3 — Retry configuration schema_version [proposed]: Carries form version. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.10.1.9 — elapsed_clock_start [proposed]: Uses the durable clock origin. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7H.10.1.14 — real_change_categories: Carries truthful change classification. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gated by: ACCEPTED — C-7H.10.1.4 — technical_max_total_attempts [proposed]: Uses the three-total technical bound. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-7H.10.1.5 — technical_gap_schedule.live_chat [proposed]: Uses live-chat wait floors. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-7H.10.1.6 — technical_gap_schedule.background_nightly [proposed]: Uses background wait floors. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-7H.10.1.7 — elapsed_time_max.live_chat [proposed]: Uses the live-chat elapsed bound. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-7H.10.1.8 — elapsed_time_max.background_nightly [proposed]: Uses the background elapsed bound. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-7H.10.1.10 — substantive_careful_retry_limit [proposed]: Allows one eligible careful retry. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-7H.10.1.11 — substantive_retry_timing [proposed]: Permits evaluation after durable rejection. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-7H.10.1.12 — early_stop_permitted [proposed]: Allows truthful early stopping. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-7H.10.1.13 — continuation_rule [proposed]: Requires real change for continuation. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10 — Accepted B9 retry values and episodes | Versioned budget. | Binds configuration. | No numerical default. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] |
| 2 · ACCEPTED | C-7H.10.4 — Technical admission under both bounds | Exact config record. | Binds admission. | Reconstructible limits. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-SACL.31 — Delivery retries under current gates and B9 bounds | The original parent/key, exact immutable payload, current privacy/SACL decisions, current owner versions/fence and the actual retry class. | Gates this place: the existing value-field owners. | Nothing in this card. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §9] |

SUB-PARTS: C-7H.10.1.1 — Retry config_id [proposed]; C-7H.10.1.2 — Retry config_version [proposed]; C-7H.10.1.3 — Retry configuration schema_version [proposed]; C-7H.10.1.4 — technical_max_total_attempts [proposed]; C-7H.10.1.5 — technical_gap_schedule.live_chat [proposed]; C-7H.10.1.6 — technical_gap_schedule.background_nightly [proposed]; C-7H.10.1.7 — elapsed_time_max.live_chat [proposed]; C-7H.10.1.8 — elapsed_time_max.background_nightly [proposed]; C-7H.10.1.9 — elapsed_clock_start [proposed]; C-7H.10.1.10 — substantive_careful_retry_limit [proposed]; C-7H.10.1.11 — substantive_retry_timing [proposed]; C-7H.10.1.12 — early_stop_permitted [proposed]; C-7H.10.1.13 — continuation_rule [proposed]; C-7H.10.1.14 — real_change_categories

### C-7H.10.1.1 — Retry config_id [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The proposed stable budget configuration identity. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Takes in: ACCEPTED — The budget record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Does: ACCEPTED — Records config_id [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Gives out: ACCEPTED — Stable configuration reference. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.1 — b9_retry_budget_config [proposed] | Configuration identity. | Stores config_id [proposed]. | Stable reference. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.10.1.2 — Retry config_version [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The proposed immutable budget revision. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Takes in: ACCEPTED — The exact accepted configuration version. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Does: ACCEPTED — Binds each admission to that revision. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Gives out: ACCEPTED — config_version [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Must never: ACCEPTED — Change a version's contents in place. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Unbound version prevents admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.1 — b9_retry_budget_config [proposed] | Version. | Records revision. | No in-place change. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.10.1.3 — Retry configuration schema_version [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The proposed budget-record schema revision. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Takes in: ACCEPTED — The schema used. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Does: ACCEPTED — Records schema_version [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Gives out: ACCEPTED — Form-version provenance. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.1 — b9_retry_budget_config [proposed] | Schema revision. | Stores schema_version [proposed]. | Readable form provenance. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.10.1.4 — technical_max_total_attempts [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The accepted value 3 per technical episode, including its original/ordinal-1 execution. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Takes in: ACCEPTED — The exact episode's durable committed attempt ordinals. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Does: ACCEPTED — Allows at most ordinals 1, 2 and 3. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Gives out: ACCEPTED — A three-total-attempt bound. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Must never: ACCEPTED — Count only retries while omitting the original attempt, or recount predecessor episodes. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Three committed ordinals closes the episode's technical allowance. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.1 — b9_retry_budget_config [proposed] | Episode ordinals. | Limits attempts. | Original counts. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.10.1.5 — technical_gap_schedule.live_chat [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The accepted minimum gaps [10 seconds, 30 seconds]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Takes in: ACCEPTED — The next technical episode ordinal, 2 or 3. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Does: ACCEPTED — Applies 10 seconds before ordinal 2 and 30 seconds before ordinal 3. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Gives out: ACCEPTED — A live-chat wait floor. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Must never: ACCEPTED — Treat gaps as the total deadline or index them by permanent group number. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Admission waits until its gap floor is reached and still must precede the deadline. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.1 — b9_retry_budget_config [proposed] | Ordinal 2 or 3. | Applies 10/30 seconds. | Deadline unchanged. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.10.1.6 — technical_gap_schedule.background_nightly [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The accepted minimum gaps [1 minute, 3 minutes]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Takes in: ACCEPTED — The next technical episode ordinal, 2 or 3. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Does: ACCEPTED — Applies 1 minute before ordinal 2 and 3 minutes before ordinal 3. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Gives out: ACCEPTED — A background/nightly wait floor. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Must never: ACCEPTED — Treat gaps as a deadline extension. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Gap and deadline must both permit admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.1 — b9_retry_budget_config [proposed] | Ordinal 2 or 3. | Applies 1/3 minutes. | Deadline unchanged. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.10.1.7 — elapsed_time_max.live_chat [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The accepted 7-minute elapsed maximum. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Takes in: ACCEPTED — The episode's first durable failure/rejection record in live_chat. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Does: ACCEPTED — Sets the episode's real stop deadline from that record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Gives out: ACCEPTED — A fixed 7-minute window. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Must never: ACCEPTED — Restart or extend the clock on later attempts. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — No retry starts at or after the deadline. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.1 — b9_retry_budget_config [proposed] | First durable failure. | Applies 7 minutes. | Fixed stop deadline. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.10.1.8 — elapsed_time_max.background_nightly [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The accepted 15-minute elapsed maximum. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Takes in: ACCEPTED — The episode's first durable failure/rejection record in background_nightly. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Does: ACCEPTED — Sets the fixed deadline from that record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Gives out: ACCEPTED — A 15-minute window. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Must never: ACCEPTED — Extend the deadline by adding retry gaps. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — No retry starts at or after the deadline. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.1 — b9_retry_budget_config [proposed] | First durable failure. | Applies 15 minutes. | Fixed stop deadline. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.10.1.9 — elapsed_clock_start [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The proposed fixed value episode_first_failure_record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The durable first technical failure or substantive rejection beginning the episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Starts that episode's elapsed clock from committed_at [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — A durable reconstructible clock anchor. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Start a later episode's clock before its first durable failure. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — No anchor is invented without its outcome record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.1 — b9_retry_budget_config [proposed] | First failure record. | Binds committed_at [proposed]. | No early invented start. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.10.1.10 — substantive_careful_retry_limit [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — Exactly 1 careful retry per rejected draft/proposal episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Takes in: ACCEPTED — Durable rejection and remaining substantive allowance. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Does: ACCEPTED — Bounds the eligible careful sequence separately from technical retries. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Gives out: ACCEPTED — A one-careful-retry allowance. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Must never: ACCEPTED — Consume or extend technical allowance through the substantive count. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — A second substantive admission in the episode is refused. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.1 — b9_retry_budget_config [proposed] | Rejected proposal episode. | Counts separately. | No second careful retry. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] |
| 2 · ACCEPTED | C-7H.10.6 — Careful-retry and B24 fallback consumption | Episode history. | Checks remaining count. | No second careful attempt. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.10.1.11 — substantive_retry_timing [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — Proposed immediate_after_durable_rejection_record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — Durable rejected proposal/reason and an unexpired episode deadline. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Permits the first admission evaluation after durable readiness with no scheduled gap. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — Immediate eligibility within both bounds. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Interpret immediate as before recording, a wall-clock promise or a deadline bypass. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Deadline exhaustion before admission prevents the careful attempt. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.1 — b9_retry_budget_config [proposed] | Ready record and deadline. | Applies no scheduled gap. | No recording or deadline bypass. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.10.1.12 — early_stop_permitted [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The accepted value true for recorded early stop. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Takes in: ACCEPTED — Clearly useless or unsafe retry evidence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Does: ACCEPTED — Permits a cause-bearing stop. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Gives out: ACCEPTED — Early-stop authority. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Must never: ACCEPTED — Record the stop as success. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — The stopped episode admits no further attempt without a new real-change episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.1 — b9_retry_budget_config [proposed] | Cause evidence. | Records stop. | No false success. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.10.1.13 — continuation_rule [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The proposed value real_change_record_required. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Takes in: ACCEPTED — A proposed continuation after exhaustion or early stop. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Does: ACCEPTED — Requires a new unconsumed durable change record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Gives out: ACCEPTED — A gated continuation possibility. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Must never: ACCEPTED — Treat time or repeated desire alone as a real change. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Missing valid change evidence refuses continuation. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.1 — b9_retry_budget_config [proposed] | Unconsumed change record. | Checks authority. | No repetition-only reset. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7H.10.1.14 — real_change_categories
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — Named examples plus a truthful other_real_change catch-all. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — new_memory, new_ness_instruction, better_context, fixed_missing_evidence, repaired_tool_file_search, solved_blocker or other_real_change. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — Requires evidence references for every category and a written explanation for the catch-all. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — Honest change classification without closing the real-world example list. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: ACCEPTED — Invent an unrecognized encoding or treat repetition/passage of time alone as change. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Malformed category or missing required explanation/evidence refuses continuation. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.1 — b9_retry_budget_config [proposed] | Category, explanation and evidence. | Validates encoding. | No unsupported change claim. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.10.2 — Retry attempt and episode numbering
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — Permanent group numbers and per-episode ordinals with distinct meanings. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Takes in: ACCEPTED — Durable original outcome, attempt entries and episode bindings. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Does: ACCEPTED — Reconstructs both counters lookup-first; technical allowance and gaps use exact episode ordinals only. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Gives out: ACCEPTED — Unique permanent identities with separately bounded episodes. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Must never: ACCEPTED — Reset/reuse permanent numbers, collide ordinals inside an episode or rely on an in-memory-only counter. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Contradictory numbering evidence is indeterminate. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]

TOGETHER
- Fed by: ACCEPTED — C-7H.10.2.1 — attempt_number: Uses monotonic group numbering. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-7H.10.2.2 — episode_attempt_ordinal [proposed]: Uses episode-local ordinal. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Gated by: ACCEPTED — C-7H.10.2.3 — Initial technical episode numbering: Includes original execution by reference. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Gated by: ACCEPTED — C-7H.10.2.4 — Later same-identity episode numbering: Opens later same-identity episode correctly. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Gated by: ACCEPTED — C-7H.10.2.5 — Changed-input retry identity: Changed inputs require a new source identity. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gated by: ACCEPTED — C-7H.10.2.6 — Separate technical and substantive allowances: Keeps class allowances separate. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10 — Accepted B9 retry values and episodes | Durable history. | Counts correctly. | No allowance reset inside an episode. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5] |
| 2 · ACCEPTED | C-7H.10.2.3 — Initial technical episode numbering | Original outcome. | Records ordinal 1 by reference. | No re-admission. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5] |
| 3 · ACCEPTED | C-7H.10.2.4 — Later same-identity episode numbering | Committed consumption. | Uses next permanent number. | No number reuse. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5] |
| 4 · ACCEPTED | C-7H.10.2.5 — Changed-input retry identity | Changed source inputs. | Creates linked new group. | Old identity preserved. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5] |
| 5 · ACCEPTED | C-7H.10.2.6 — Separate technical and substantive allowances | Attempt class. | Keeps budgets independent. | No allowance transfer. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5] |

SUB-PARTS: C-7H.10.2.1 — attempt_number; C-7H.10.2.2 — episode_attempt_ordinal [proposed]; C-7H.10.2.3 — Initial technical episode numbering; C-7H.10.2.4 — Later same-identity episode numbering; C-7H.10.2.5 — Changed-input retry identity; C-7H.10.2.6 — Separate technical and substantive allowances

### C-7H.10.2.1 — attempt_number
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — Permanent monotonic group-wide number inside attempt_id [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Takes in: ACCEPTED — The group's durable attempt history across all episodes. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Does: ACCEPTED — Uses the next unused number at admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Gives out: ACCEPTED — A unique permanent attempt number. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Must never: ACCEPTED — Reset or repeat the number in a later episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Collisions fail closed. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.2 — Retry attempt and episode numbering | Group history. | Chooses unused number. | Permanent uniqueness. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.10.2.2 — episode_attempt_ordinal [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — Proposed per-episode position bound to retry_episode_id, limited to 1–3 for technical episodes. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Takes in: ACCEPTED — The exact episode's committed attempts. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Does: ACCEPTED — Applies its allowance and gap index; restarts at 1 only in a new episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Gives out: ACCEPTED — An episode-local ordinal. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Must never: ACCEPTED — Index gaps with permanent numbers or reset an ordinal within the same episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Colliding/reset ordinal evidence is indeterminate. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.2 — Retry attempt and episode numbering | Exact episode. | Counts 1–3. | Bounded local allowance. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.10.2.3 — Initial technical episode numbering
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The source's original execution is ordinal 1 by reference, never a B9 admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Takes in: ACCEPTED — Its durable technical_retryable outcome. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Does: ACCEPTED — Records original permanent number 1; B9 retries use ordinals and permanent numbers 2 and 3. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Gives out: ACCEPTED — At most two admitted retries in the initial episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Must never: ACCEPTED — Re-admit the historical original execution as an extra attempt. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — The three-total bound includes the original. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.2 — Retry attempt and episode numbering: Original belongs to the initial three-total count. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.2 — Retry attempt and episode numbering | Original durable failure. | Starts initial episode. | No extra admitted original. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.10.2.4 — Later same-identity episode numbering
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — A new bounded episode with seam-confirmed unchanged canonical inputs. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Takes in: ACCEPTED — Committed real-change consumption and existing group history. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Does: ACCEPTED — Admits its first re-attempt as ordinal 1 using the next unused permanent number; later ordinals are 2 and 3. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Gives out: ACCEPTED — A fresh local ordinal sequence without group-number reset. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Must never: ACCEPTED — Continue or extend the exhausted predecessor episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — No unchanged-input confirmation means this same-identity route is unavailable. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.2 — Retry attempt and episode numbering: Only a new episode restarts ordinals. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.2 — Retry attempt and episode numbering | Consumed change and unchanged inputs. | Restarts ordinal only. | Permanent number continues. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.10.2.5 — Changed-input retry identity
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — A new source identity and retry group when canonical inputs change. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — The source seam's input-identity determination. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — Links the new operation to the old failed operation and uses normal initial-episode semantics in the new group. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — A new canonical operation/group. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: ACCEPTED — Change inputs inside the old identity or continue/renumber its attempts. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — The source seam, not B9, decides canonical-input sameness. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.2 — Retry attempt and episode numbering: Canonical-input change is seam-owned. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.2 — Retry attempt and episode numbering | Seam determination. | Links a new group. | No mutation of old identity. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.10.2.6 — Separate technical and substantive allowances
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — Independent bounds for technical attempts and one careful substantive retry. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Takes in: ACCEPTED — The attempt's actual class. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Does: ACCEPTED — Counts each in its own bounded sequence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Gives out: ACCEPTED — Separate allowance consumption. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Must never: ACCEPTED — Let one class consume or extend the other's allowance. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Each class still obeys its own time and admission bounds. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.2 — Retry attempt and episode numbering: Actual class controls counting. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.2 — Retry attempt and episode numbering | Actual attempt kind. | Counts its own sequence. | No cross-class extension. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7H.10.3 — Durable retry scheduling anchors
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Recorded schedule class, minimum-gap floor and fixed episode deadline. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Durable outcome committed_at [proposed] and recorded execution context. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Recomputes identical anchors from records; gap class comes from the latest outcome, deadline class from the episode's first failure. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Durable reconstructible admission times. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Guess a class, average contexts, create another clock or extend a deadline. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Missing class or anchor evidence prevents ordinary timed admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-7H.10.3.1 — schedule_class [proposed]: Requires recorded execution context. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-7H.10.3.2 — next_admission_not_before: Computes the next minimum floor. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-7H.10.3.3 — episode_deadline: Uses the first-failure clock. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7H.10.3.4 — Changed execution context between outcomes: Handles differing recorded contexts. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10 — Accepted B9 retry values and episodes | Outcome timestamps and classes. | Computes anchors. | No invented clock. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7H.10.3.4 — Changed execution context between outcomes | Durable outcomes. | Reconstructs both anchors. | One fixed deadline. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-SACL.31 — Delivery retries under current gates and B9 bounds | The original parent/key, exact immutable payload, current privacy/SACL decisions, current owner versions/fence and the actual retry class. | Gates this place: durable episode timing. | Nothing in this card. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §9] |

SUB-PARTS: C-7H.10.3.1 — schedule_class [proposed]; C-7H.10.3.2 — next_admission_not_before; C-7H.10.3.3 — episode_deadline; C-7H.10.3.4 — Changed execution context between outcomes

### C-7H.10.3.1 — schedule_class [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Proposed live_chat or background_nightly, recorded when the outcome becomes durable. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The source operation's own recorded execution context. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Carries that context without guessing. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — schedule_class [proposed] on the outcome record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Default a missing or unreadable class. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — No valid class means no admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.3 — Durable retry scheduling anchors | Outcome class. | Carries schedule_class [proposed]. | No guessed default. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.10.3.2 — next_admission_not_before
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Proposed outcome_record.committed_at + technical_gap_schedule[recorded class][next episode_attempt_ordinal − 1]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The latest durable outcome and next ordinal 2 or 3. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Computes the minimum wait floor using the first or second schedule entry. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — A gap anchor, never a stop deadline. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Index with group-wide number or invent a gap before ordinal 1. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — No durable outcome means no ordinary gap anchor exists. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.3 — Durable retry scheduling anchors | Latest outcome and next ordinal. | Adds applicable gap. | No stop-deadline substitution. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.10.3.3 — episode_deadline
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Proposed episode_first_failure_record.committed_at + elapsed_time_max[deadline class]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The first durable technical failure or careful-sequence rejection. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Fixes one 7/15-minute clock and deadline class for that episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — The episode's real stop deadline. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Start a second clock, average classes or extend the deadline. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Admission requires now strictly before the deadline. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.3 — Durable retry scheduling anchors | Initial durable outcome. | Fixes deadline. | No extension. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.10.3.4 — Changed execution context between outcomes
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Different recorded contexts on successive outcomes of one group. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Latest outcome class and first-failure deadline class. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Uses the latest class for the next gap while keeping the original deadline class fixed. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Correct gap and unchanged deadline. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Invent a third schedule or average the classes. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Missing anchor class still blocks admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.3 — Durable retry scheduling anchors: Gap context may change; deadline context cannot. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.3 — Durable retry scheduling anchors | Latest and first classes. | Uses each proper anchor. | No averaged schedule. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7H.10.4 — Technical admission under both bounds
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — Eight cumulative conditions for normal technical retry admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — Latest technical_retryable class, no live attempt/hold, remaining exact-episode allowance, satisfied gap, unexpired deadline, readable bound config and an open eligible episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Checks all conditions before one compare-and-commit binding group, next permanent number, attempt_id [proposed], episode identity/ordinal, exact config, gap evidence and deadline evidence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — One winner; losers observe and append nothing. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Recount predecessor episodes, bypass either bound or infer counters from memory. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Any failed gate means no retry; time exhaustion is recorded truthfully. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.4.1 — Technical outcome admission gate: Requires technical_retryable. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.10.4.2 — No-live-attempt admission gate: Requires no live attempt. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.10.4.3 — No-live-hold admission gate: Requires no live hold. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §12]
- Gated by: ACCEPTED — C-7H.10.4.4 — Per-episode attempt gate: Requires remaining exact-episode allowance. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.10.4.5 — Minimum-gap admission gate: Requires the gap floor. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.10.4.6 — Deadline admission gate: Requires an unexpired deadline. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.10.4.7 — Readable-bound-configuration gate: Requires readable bound configuration. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.10.4.8 — Open-episode admission gate: Requires an open eligible episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.10.1 — b9_retry_budget_config [proposed]: Uses the accepted versioned quantities. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.9.4.2 — R1 — Retry attempt admission: Uses B9's one-winner R1 boundary. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10 — Accepted B9 retry values and episodes | Attempt, time and state evidence. | Admits one winner. | Both bounds enforced. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| 2 · ACCEPTED | C-7H.10.4.1 — Technical outcome admission gate | Latest class. | Checks technical eligibility. | Class alone is insufficient. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-7H.10.4.2 — No-live-attempt admission gate | Live attempt lookup. | Checks exclusivity. | No overlap. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| 4 · ACCEPTED | C-7H.10.4.3 — No-live-hold admission gate | Hold lookup. | Refuses if held. | No count consumed. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| 5 · ACCEPTED | C-7H.10.4.4 — Per-episode attempt gate | Episode ordinals. | Checks count. | No fourth attempt. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| 6 · ACCEPTED | C-7H.10.4.5 — Minimum-gap admission gate | Gap anchor. | Checks readiness. | Deadline also applies. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| 7 · ACCEPTED | C-7H.10.4.6 — Deadline admission gate | Fixed clock. | Checks time. | No late start. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| 8 · ACCEPTED | C-7H.10.4.7 — Readable-bound-configuration gate | Versioned config. | Checks readability. | No default. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| 9 · ACCEPTED | C-7H.10.4.8 — Open-episode admission gate | Episode disposition. | Checks openness. | No reopening predecessor. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| 10 · ACCEPTED | C-SACL.31 — Delivery retries under current gates and B9 bounds | The original parent/key, exact immutable payload, current privacy/SACL decisions, current owner versions/fence and the actual retry class. | Gates this place: attempt and elapsed bounds. | Nothing in this card. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §9] |

SUB-PARTS: C-7H.10.4.1 — Technical outcome admission gate; C-7H.10.4.2 — No-live-attempt admission gate; C-7H.10.4.3 — No-live-hold admission gate; C-7H.10.4.4 — Per-episode attempt gate; C-7H.10.4.5 — Minimum-gap admission gate; C-7H.10.4.6 — Deadline admission gate; C-7H.10.4.7 — Readable-bound-configuration gate; C-7H.10.4.8 — Open-episode admission gate

### C-7H.10.4.1 — Technical outcome admission gate
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The latest source class must be technical_retryable. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — The recorded latest classification. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Rejects protected, held, indeterminate and terminal classes under their own rules. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — Correct technical eligibility. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Manufacture technical status from an unrelated outcome. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Ineligible classes are not admitted technically. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.4 — Technical admission under both bounds: All eight conditions are cumulative. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.4 — Technical admission under both bounds | Latest source class. | Checks eligibility. | No class laundering. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.10.4.2 — No-live-attempt admission gate
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — At most one live attempt per group. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — Durable live-attempt state. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Checks that no live attempt exists before commitment. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — Exclusive attempt eligibility. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Admit overlapping attempts. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — A live attempt blocks admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.4 — Technical admission under both bounds: All eight conditions are cumulative. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.4 — Technical admission under both bounds | Group state. | Checks exclusivity. | One live execution. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.10.4.3 — No-live-hold admission gate
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — No hold may be live on the source or inputs. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §12]
- Takes in: ACCEPTED — The owning hold records. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §12]
- Does: ACCEPTED — Refuses and records while held, without queueing around the hold. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §12]
- Gives out: ACCEPTED — Side-effect-free retry refusal. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §12]
- Must never: ACCEPTED — Consume count, create anchor/episode or touch hold records on refusal. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — A live hold prevents admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §12]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.4 — Technical admission under both bounds: All eight conditions are cumulative. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.4 — Technical admission under both bounds | Owner hold records. | Refuses while held. | No state consumed. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7H.10.4.4 — Per-episode attempt gate
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — Fewer than three committed technical ordinals in this exact episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — Durable episode attempts. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Counts only this episode before admitting its next ordinal. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — Remaining attempt eligibility. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Count predecessor attempts or skip the original ordinal. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Reached count produces exhaustion and no attempt. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.4 — Technical admission under both bounds: All eight conditions are cumulative. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.4 — Technical admission under both bounds | Committed ordinals. | Counts before commit. | At most three. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.10.4.5 — Minimum-gap admission gate
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — now ≥ the applicable durable gap anchor. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — Next episode ordinal and recorded gap evidence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Waits until the relevant minimum floor is reached. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — Gap-ready eligibility. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Treat reaching the gap as sufficient when the deadline has expired. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Unsatisfied gap permits no timed retry. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.4 — Technical admission under both bounds: All eight conditions are cumulative. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.4 — Technical admission under both bounds | Durable next-admission anchor. | Waits until ready. | No early attempt. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.10.4.6 — Deadline admission gate
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — now < episode_deadline before each technical or careful retry. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — Fixed deadline and current admission time. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Stops unstarted work when time is exhausted; if time passes mid-attempt the source finishes under its own rules and no later retry is admitted. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — A bounded start or truthful time exhaustion. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Force-cancel the source or override its timeout/terminal rules. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Reached deadline blocks every further start. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.4 — Technical admission under both bounds: All eight conditions are cumulative. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.4 — Technical admission under both bounds | Fixed clock and now. | Stops further starts at deadline. | No source cancellation. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| 2 · ACCEPTED | C-7H.10.6 — Careful-retry and B24 fallback consumption | Durable rejection and now. | Checks the fixed elapsed bound. | No late admission. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.10.4.7 — Readable-bound-configuration gate
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — retry_budget_ref [proposed] resolves to an existing readable exact configuration version. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — The admission's bound reference. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Verifies the declared budget terms. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — Traceable configured eligibility. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Default an absent configuration. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Missing/unreadable/version-unbound config blocks admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.4 — Technical admission under both bounds: All eight conditions are cumulative. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.4 — Technical admission under both bounds | Exact version reference. | Verifies terms. | No default. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.10.4.8 — Open-episode admission gate
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The current episode is neither exhausted nor early-stopped, or a new episode is validly opened through real change. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — Durable disposition and consumption records. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Preserves closed episodes and permits only a separately authorized new bounded episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — Eligible open episode identity. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Reopen or extend the exhausted episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — No valid new consumption means no continuation. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.4 — Technical admission under both bounds: All eight conditions are cumulative. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.4 — Technical admission under both bounds | Disposition and consumption. | Checks episode identity. | No reopening exhausted work. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.10.5 — Later-episode ordinal-1 admission
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The special first admission of a same-identity continuation episode before any new failure exists. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — Committed real-change consumption and source-confirmed unchanged canonical inputs. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Atomically binds group, next permanent number, attempt_id, retry_episode_id [proposed], ordinal 1, exact config, consumption authorization and explicit no-gap/deadline-pending states. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — One ordinal-1 winner without fictitious anchor evidence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Claim a gap/deadline already exists, invent a waiting gap or start the clock early. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Missing consumption or unchanged-input confirmation refuses this admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

TOGETHER
- Fed by: ACCEPTED — C-7H.10.5.1 — no_gap_before_ordinal_1 [proposed]: Records the explicit ordinal-1 gap state. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Fed by: ACCEPTED — C-7H.10.5.2 — deadline_pending_from_first_durable_failure [proposed]: Records explicit deadline-pending state. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.10.5.3 — Later ordinal-1 success: Handles success without a failure anchor. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.10.5.4 — Later ordinal-1 technical failure: Handles first durable technical failure. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.10.5.5 — Later ordinal-1 protected outcome: Handles protected or indeterminate outcomes. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.10.9.3 — real_change_consumption_key [proposed]: Requires a committed unique consumption. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10 — Accepted B9 retry values and episodes | Real-change consumption. | Binds explicit pending anchors. | No fictitious waiting gap. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| 2 · ACCEPTED | C-7H.10.5.3 — Later ordinal-1 success | Committed source success. | Stops. | No retry. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-7H.10.5.4 — Later ordinal-1 technical failure | Durable failure. | Reconstructs gap/deadline. | No early start. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| 4 · ACCEPTED | C-7H.10.5.5 — Later ordinal-1 protected outcome | Outcome class. | Blocks ordinary technical retry. | No bypass. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |

SUB-PARTS: C-7H.10.5.1 — no_gap_before_ordinal_1 [proposed]; C-7H.10.5.2 — deadline_pending_from_first_durable_failure [proposed]; C-7H.10.5.3 — Later ordinal-1 success; C-7H.10.5.4 — Later ordinal-1 technical failure; C-7H.10.5.5 — Later ordinal-1 protected outcome

### C-7H.10.5.1 — no_gap_before_ordinal_1 [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The proposed explicit durable state replacing nonexistent gap evidence at later-episode ordinal 1. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — The first admitted continuation attempt. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Records that no scheduled gap applies before this ordinal. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — no_gap_before_ordinal_1 [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Manufacture an earlier outcome or gap anchor inside the new episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.5 — Later-episode ordinal-1 admission | First continuation attempt. | Binds no_gap_before_ordinal_1 [proposed]. | No invented waiting gap. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.10.5.2 — deadline_pending_from_first_durable_failure [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The proposed durable state before the new episode's first technical failure. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — The later episode's ordinal-1 admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Defers deadline creation until that attempt durably fails as technical_retryable. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — deadline_pending_from_first_durable_failure [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Start the 7/15-minute clock at admission or fabricate deadline evidence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.5 — Later-episode ordinal-1 admission | No failure yet. | Binds pending deadline. | Clock has not started. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.10.5.3 — Later ordinal-1 success
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The first continuation attempt commits success. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — Its durable source success. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Completes through the source seam with no episode deadline and no further retry. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — terminal_success disposition. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Create a deadline or another technical attempt after success. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — No further admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.5 — Later-episode ordinal-1 admission: Success needs no invented failure record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.5 — Later-episode ordinal-1 admission | Durable success. | Terminates the group. | No fabricated deadline. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.10.5.4 — Later ordinal-1 technical failure
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The first continuation attempt durably ends technical_retryable. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — The failure's committed_at [proposed] and schedule_class [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Uses it as deadline anchor, fixed deadline class and gap anchor for ordinal 2; later ordinals bind actual evidence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — Real deadline/gap evidence for bounded retries 2 and 3. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Start from a different clock or fabricate alternate anchors. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Normal dual-bound admission applies thereafter. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.5 — Later-episode ordinal-1 admission: Only actual first failure starts the clock. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.5 — Later-episode ordinal-1 admission | Committed failure. | Creates actual anchors. | Remaining ordinals 2 and 3 only. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.10.5.5 — Later ordinal-1 protected outcome
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — A protected, terminal, held, privacy-refused or indeterminate result. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — That durable source outcome. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Routes through its own existing rules. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — Matching protected disposition. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Manufacture a technical deadline path or further technical retry from it. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — No technical admission is created by an ineligible result. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.5 — Later-episode ordinal-1 admission: Protected classes retain their owner rules. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.5 — Later-episode ordinal-1 admission | Actual source class. | Applies its boundary. | No technical fallback fiction. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7H.10.6 — Careful-retry and B24 fallback consumption
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The generic episode connection to the existing acceptance-owned careful retry and fallback boundary. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — Exact durable rejected proposal/reason, policy reference, one unused allowance and unexpired deadline. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Binds rejection as per-case authorization and mandatory input context; permits one immediate careful attempt with no scheduled gap, then preserves its actual outcome. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — Pass, terminal repeated rejection or the separately authorized B24 insufficiency-assessment opportunity. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Convert technical_failure, authorization_failed, indeterminate_unvalidated, privacy refusal, holds or protected outcomes into insufficient_context. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Only an eligible proposal with the one careful retry consumed and rejected again can reach B24's own fallback conditions; only committed external genuine_insufficiency_confirmed permits insufficient_context. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7G.9 — B9 acceptance retry and fallback boundary: Consumes the already-owned B24 careful-retry and fallback seam. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]
- Gated by: ACCEPTED — C-7H.10.1.10 — substantive_careful_retry_limit [proposed]: Uses the separate one-careful-retry allowance. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7H.10.4.6 — Deadline admission gate: Immediate eligibility still precedes deadline. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10 — Accepted B9 retry values and episodes | Durable rejection. | Checks bounded permission. | No generic terminal bypass. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-16.14.11 — Deterministic messenger fallback | Validated scoped facts, genuine unknowns and preserved unconfirmed possibilities. | Gates this place: permits the assessment/fallback only at its authorized eligible-proposal point. | Nothing in this card. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13] [04/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md §5.3] |
| 3 · ACCEPTED | C-SACL.31 — Delivery retries under current gates and B9 bounds | The original parent/key, exact immutable payload, current privacy/SACL decisions, current owner versions/fence and the actual retry class. | Gates this place: one reason-recorded careful retry. | Nothing in this card. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §9] |
| 4 · ACCEPTED | C-16.14.10 — Messenger rejection and bounded retry | A rejected draft and its exact distinct rejection reason. | Gates this place: owns admission and the narrowly authorized fallback point. | Nothing in this card. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13] [04/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md §5.3] |

SUB-PARTS: NONE

### C-7H.10.7 — Retry early stop
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — Proposed retry_early_stopped disposition for clearly useless or unsafe further retry. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §8]
- Takes in: ACCEPTED — The cause class clearly_useless or unsafe and its evidence references. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §8]
- Does: ACCEPTED — Records the real cause and then the requesting operation's R4 terminal; closes admission for the episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §8]
- Gives out: ACCEPTED — A preserved early-stop record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §8]
- Must never: ACCEPTED — Hide it, call it success or disguise its cause as ordinary exhaustion. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Further continuation needs a new real-change-authorized bounded episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10 — Accepted B9 retry values and episodes: Early stop must retain its real cause. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10 — Accepted B9 retry values and episodes | Unsafe or useless continuation. | Stops further admission. | Failure remains visible. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-SACL.31 — Delivery retries under current gates and B9 bounds | The original parent/key, exact immutable payload, current privacy/SACL decisions, current owner versions/fence and the actual retry class. | Gates this place: unsafe/useless stop. | Nothing in this card. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.10.8 — Retry exhaustion and preserved work
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — No further eligible attempt because count, time, consumed/rejected careful retry or recorded early stop closes admission without success. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §9]
- Takes in: ACCEPTED — Durable stopping-gate evidence and source unfinished state. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §9]
- Does: ACCEPTED — Records proposed retry_episode_exhausted with the actual cause/outcome refs, states why through existing output gates and references preserved source work. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §9]
- Gives out: ACCEPTED — Honest stopped work available for lookup-first later continuation. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §9]
- Must never: ACCEPTED — Delete state, force-cancel a running source, hide failure or reopen terminal jobs. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Waiting past the deadline starts nothing; a running attempt finishes under its source and admits no later retry. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10 — Accepted B9 retry values and episodes: A reached bound closes this episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10 — Accepted B9 retry values and episodes | Reached bound or terminal result. | Preserves work and cause. | No hidden retry. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §9] |
| 2 · ACCEPTED | C-SACL.31 — Delivery retries under current gates and B9 bounds | The original parent/key, exact immutable payload, current privacy/SACL decisions, current owner versions/fence and the actual retry class. | Gates this place: retained unfinished state. | Nothing in this card. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.10.9 — Real-change continuation records
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — Immutable evidence and separate single-consumption authority for a new bounded continuation. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — A genuine change after exhaustion or early stop. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — Records the change, atomically consumes it once and selects same-identity episode or new canonical operation according to the source's input determination. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — A new bounded opportunity with prior episodes untouched. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: ACCEPTED — Treat repetition as change, mutate a change to mark consumption or use it as truth evidence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Missing/malformed/consumed evidence or protected outcome boundaries prevent continuation. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

TOGETHER
- Fed by: ACCEPTED — C-7H.10.9.1 — b9_real_change_record [proposed]: Requires immutable change evidence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gated by: ACCEPTED — C-7H.10.9.3 — real_change_consumption_key [proposed]: Consumes one change globally once. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gated by: ACCEPTED — C-7H.10.9.5 — Real-change protected-class boundary: Real change does not override protected source state. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Changes: ACCEPTED — C-7H.10.9.2 — b9_real_change_consumption_record [proposed]: Records use separately. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Changes: ACCEPTED — C-7H.10.9.4 — New retry-episode identity and lineage: Creates a separately bounded episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10 — Accepted B9 retry values and episodes | New evidence and target. | Commits one consumption. | A new bounded episode only. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |
| 2 · ACCEPTED | C-7H.10.9.3 — real_change_consumption_key [proposed] | Durable consumption lookup. | Converges on winner. | No reuse. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |
| 3 · ACCEPTED | C-7H.10.9.5 — Real-change protected-class boundary | Protected state. | Defers to owner. | No bypass. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |
| 4 · ACCEPTED | C-SACL.31 — Delivery retries under current gates and B9 bounds | The original parent/key, exact immutable payload, current privacy/SACL decisions, current owner versions/fence and the actual retry class. | Gates this place: actual changed conditions. | Nothing in this card. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §9] |

SUB-PARTS: C-7H.10.9.1 — b9_real_change_record [proposed]; C-7H.10.9.2 — b9_real_change_consumption_record [proposed]; C-7H.10.9.3 — real_change_consumption_key [proposed]; C-7H.10.9.4 — New retry-episode identity and lineage; C-7H.10.9.5 — Real-change protected-class boundary

### C-7H.10.9.1 — b9_real_change_record [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — A proposed append-only immutable real-change record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — Identity, category, explanation, evidence refs, target group, time and schema version. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — Preserves what actually changed; consumption lives in another record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — b9_real_change_record [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: ACCEPTED — Edit any field after creation or add a mutable consumed_by_episode_ref. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Invalid category or missing required evidence refuses continuation. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

TOGETHER
- Fed by: ACCEPTED — C-7H.10.9.1.1 — change_record_id [proposed]: Names the immutable change. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fed by: ACCEPTED — C-7H.10.9.1.2 — change_category [proposed]: Classifies the actual change. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fed by: ACCEPTED — C-7H.10.9.1.3 — change_explanation [proposed]: Explains what really changed. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fed by: ACCEPTED — C-7H.10.9.1.4 — change_evidence_refs [proposed]: References proof of change. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fed by: ACCEPTED — C-7H.10.9.1.5 — target_group_ref [proposed]: Targets the affected prior operation/group. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fed by: ACCEPTED — C-7H.10.9.1.6 — Real-change recorded_at [proposed]: Records when change was recorded. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fed by: ACCEPTED — C-7H.10.9.1.7 — Real-change schema_version [proposed]: Names the record form. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.9 — Real-change continuation records | Actual new condition. | Appends change record. | No invented change. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: C-7H.10.9.1.1 — change_record_id [proposed]; C-7H.10.9.1.2 — change_category [proposed]; C-7H.10.9.1.3 — change_explanation [proposed]; C-7H.10.9.1.4 — change_evidence_refs [proposed]; C-7H.10.9.1.5 — target_group_ref [proposed]; C-7H.10.9.1.6 — Real-change recorded_at [proposed]; C-7H.10.9.1.7 — Real-change schema_version [proposed]

### C-7H.10.9.1.1 — change_record_id [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed stable real-change identity. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — The actual recorded change. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — Identifies it for one-time consumption. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — change_record_id [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: ACCEPTED — Reuse it for a further continuation after consumption. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.9.1 — b9_real_change_record [proposed] | Record identity. | Stores change_record_id [proposed]. | Unique evidence record. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.10.9.1.2 — change_category [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed encoded example or catch-all classification. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — new_memory, new_ness_instruction, better_context, fixed_missing_evidence, repaired_tool_file_search, solved_blocker or other_real_change. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — Records the truthful category while retaining the example list's nonexhaustive meaning. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — change_category [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: ACCEPTED — Store an unrecognized value or classify mere repetition/time as change. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — An out-of-vocabulary value is malformed. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.9.1 — b9_real_change_record [proposed] | Category. | Stores accepted encoding. | Honest change type. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.10.9.1.3 — change_explanation [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — Required written explanation for other_real_change, optional but recordable for named examples. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — What genuinely changed. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — Preserves the explanation with the change record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — change_explanation [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: ACCEPTED — Omit it for the catch-all. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Missing required explanation refuses continuation. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.9.1 — b9_real_change_record [proposed] | Evidence-bearing explanation. | Records the difference. | Required catch-all explanation. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.10.9.1.4 — change_evidence_refs [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — Required durable evidence references for every category. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — Actual new memory/instruction/context/evidence/repair/blocker or other change records. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — References their identities without copying or rescoring them. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — change_evidence_refs [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: ACCEPTED — Treat repeated desire, a rerequest or passage of time alone as evidence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Missing genuine evidence refuses continuation. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.9.1 — b9_real_change_record [proposed] | Evidence identities. | Binds actual evidence. | No unsupported reset. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.10.9.1.5 — target_group_ref [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed exhausted or early-stopped group this change may authorize. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — The target retry group identity. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — Binds continuation authority to that group. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — target_group_ref [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: ACCEPTED — Authorize anything unrelated to the cited real change. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.9.1 — b9_real_change_record [proposed] | Canonical reference. | Binds scope. | No unrelated authorization. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.10.9.1.6 — Real-change recorded_at [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed change-record timestamp. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — Actual recording time. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — Records recorded_at [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — Time provenance. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.9.1 — b9_real_change_record [proposed] | Timestamp. | Stores recorded_at [proposed]. | Durable chronology. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.10.9.1.7 — Real-change schema_version [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed change-record schema revision. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — The used schema version. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — Records schema_version [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — Form-version provenance. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.9.1 — b9_real_change_record [proposed] | Schema revision. | Stores schema_version [proposed]. | Traceable structure. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.10.9.2 — b9_real_change_consumption_record [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — A proposed separate append-only record, never an edit of the change. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — Its identity, change ref, consumer ref, atomic claim result, time and schema version. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — Records the one successful consumption and what it opened. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — Immutable consumption evidence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: ACCEPTED — Mutate the original change record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — A previously consumed change cannot authorize another continuation. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

TOGETHER
- Fed by: ACCEPTED — C-7H.10.9.2.1 — consumption_record_id [proposed]: Names this consumption. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fed by: ACCEPTED — C-7H.10.9.2.2 — real_change_record_ref [proposed]: Binds the exact change. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fed by: ACCEPTED — C-7H.10.9.2.3 — consumer_ref [proposed]: Names the single authorized consumer. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fed by: ACCEPTED — C-7H.10.9.2.4 — Real-change claim_result [proposed]: Records the claim outcome. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fed by: ACCEPTED — C-7H.10.9.2.5 — Consumption committed_at [proposed]: Records durable use time. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fed by: ACCEPTED — C-7H.10.9.2.6 — Consumption schema_version [proposed]: Names the consumption form. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.9 — Real-change continuation records | Change and consuming episode/operation. | Appends consumption. | Change record remains immutable. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: C-7H.10.9.2.1 — consumption_record_id [proposed]; C-7H.10.9.2.2 — real_change_record_ref [proposed]; C-7H.10.9.2.3 — consumer_ref [proposed]; C-7H.10.9.2.4 — Real-change claim_result [proposed]; C-7H.10.9.2.5 — Consumption committed_at [proposed]; C-7H.10.9.2.6 — Consumption schema_version [proposed]

### C-7H.10.9.2.1 — consumption_record_id [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed stable consumption identity. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — The committed consumption operation. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — Identifies its record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — consumption_record_id [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.9.2 — b9_real_change_consumption_record [proposed] | Record identity. | Stores consumption_record_id [proposed]. | Unique use record. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.10.9.2.2 — real_change_record_ref [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed pointer to consumed change_record_id. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — The actual change identity. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — Binds consumption to that record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — real_change_record_ref [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: ACCEPTED — Substitute another change silently. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.9.2 — b9_real_change_consumption_record [proposed] | Change record identity. | Stores reference. | No substituted evidence. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.10.9.2.3 — consumer_ref [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed identity of the new retry episode or new source operation opened. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — The source-confirmed same/new canonical-input result. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — Names the actual consumer of this change. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — consumer_ref [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: ACCEPTED — Label changed canonical inputs as an old-identity continuation. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Canonical-input truth determines the consumer type. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.9.2 — b9_real_change_consumption_record [proposed] | New episode/operation. | Binds consumer_ref [proposed]. | No second continuation. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.10.9.2.4 — Real-change claim_result [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed single winner's atomic consumption commit evidence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — The successful compare-and-commit result. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — Preserves proof of the one committed winner. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — claim_result [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: ACCEPTED — Record multiple winners. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Concurrent losers observe and append nothing. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.9.2 — b9_real_change_consumption_record [proposed] | Winner or observed winner. | Stores truthful result. | No losing-winner claim. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.10.9.2.5 — Consumption committed_at [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed consumption commitment timestamp. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — Durable commit time. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — Records committed_at [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — Consumption time provenance. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.9.2 — b9_real_change_consumption_record [proposed] | Commit timestamp. | Stores committed_at [proposed]. | Reconstructible consumption. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.10.9.2.6 — Consumption schema_version [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed consumption-record schema revision. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — The version used. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — Records schema_version [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — Form-version provenance. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.9.2 — b9_real_change_consumption_record [proposed] | Schema revision. | Stores schema_version [proposed]. | Traceable structure. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.10.9.3 — real_change_consumption_key [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — Proposed stable_hash(change_record_id + "consumption_v1"). [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — One change identity. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — Enforces lookup-first atomic single consumption; racing losers append nothing and reuse requests are refused and logged. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — At most one committed consumption per change. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: ACCEPTED — Let one real change authorize endless episodes. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Further continuation needs a new unconsumed record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.9 — Real-change continuation records: One change record authorizes only one consumer. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.5 — Later-episode ordinal-1 admission | Change record and consumer. | Checks authorization. | No reused change evidence. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |
| 2 · ACCEPTED | C-7H.10.9 — Real-change continuation records | Change record ID. | Compare-and-commits. | One authorized continuation. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |
| 3 · ACCEPTED | C-7H.10.9.4 — New retry-episode identity and lineage | Committed consumption and seam-confirmed unchanged inputs. | Proceeds only when the real change's single consumption is committed and its inputs are confirmed unchanged. | Nothing in this card. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7H.10.9.4 — New retry-episode identity and lineage
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — Proposed retry_episode_id = {retry_group_id, episode_number}, with predecessor and authorizing-change references. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Takes in: ACCEPTED — Committed consumption and seam-confirmed unchanged inputs. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Does: ACCEPTED — Opens a fresh bounded episode under unchanged accepted values while preserving the closed predecessor. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Gives out: ACCEPTED — New episode identity, lineage and ordinal-1 eligibility. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Must never: ACCEPTED — Extend/recount/reopen the predecessor or reset permanent attempt numbers. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — Missing consumption/unchanged-input evidence prevents opening. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]

TOGETHER
- Fed by: ACCEPTED — C-7H.10.9.4.1 — episode_number [proposed]: Uses distinct group episode numbering. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fed by: ACCEPTED — C-7H.10.9.4.2 — predecessor_episode_ref [proposed]: Links the exhausted predecessor. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fed by: ACCEPTED — C-7H.10.9.4.3 — authorizing_change_ref [proposed]: References committed change consumption. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fed by: ACCEPTED — C-7H.9.3.1 — retry_group_id [proposed]: Reuses the same retry_group_id [proposed] in episode identity. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gated by: ACCEPTED — C-7H.10.9.3 — real_change_consumption_key [proposed]: the real change's single consumption is committed and its inputs are confirmed unchanged. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.9 — Real-change continuation records | Group history and consumption. | Binds lineage. | No extension of predecessor. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: C-7H.10.9.4.1 — episode_number [proposed]; C-7H.10.9.4.2 — predecessor_episode_ref [proposed]; C-7H.10.9.4.3 — authorizing_change_ref [proposed]

### C-7H.10.9.4.1 — episode_number [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The proposed episode number inside retry_episode_id. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Takes in: ACCEPTED — The durable episode/disposition chain. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Does: ACCEPTED — Identifies the new bounded episode within its group. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Gives out: ACCEPTED — episode_number [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Must never: ACCEPTED — Reuse an old episode to extend its allowance. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — Contradictory lineage fails closed. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.9.4 — New retry-episode identity and lineage | Existing episode history. | Identifies the new episode. | No predecessor extension. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.10.9.4.2 — predecessor_episode_ref [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed link to the earlier closed episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — The actual predecessor identity. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — Preserves continuation lineage without changing old state. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — predecessor_episode_ref [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: ACCEPTED — Reopen or rewrite the predecessor. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.9.4 — New retry-episode identity and lineage | Previous episode identity. | Preserves lineage. | No rewritten predecessor. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.10.9.4.3 — authorizing_change_ref [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed reference to the real change authorizing the new episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — The consumed change identity. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — Binds the episode to its recorded change. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — authorizing_change_ref [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: ACCEPTED — Open continuation without its committed consumption. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Missing authority prevents opening. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.9.4 — New retry-episode identity and lineage | Authorization reference. | Binds the exact authority. | No anonymous continuation. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.10.9.5 — Real-change protected-class boundary
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — Continuation authority never bypasses protected outcomes. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Takes in: ACCEPTED — Change evidence plus live hold, privacy refusal or indeterminate state. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Does: ACCEPTED — Keeps the hold release, changed gate authorization and source recovery requirements intact. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — A protected refusal until the appropriate owner resolves it. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Must never: ACCEPTED — Use change records as truth evidence or substitutes for permission/recovery. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Protected classes retain their own blocking rules. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.9 — Real-change continuation records: Consumption is not gate authorization. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.9 — Real-change continuation records | Outcome and owner authorization. | Retains hold/privacy/terminal rules. | No bypass. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7H.10.10 — Values-layer crash reconstruction
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — Lookup-first reconstruction of counters, episode state, anchors and consumption bindings. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Takes in: ACCEPTED — Durable attempt, outcome, disposition, rejection, change and consumption records. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Does: ACCEPTED — Reconstructs exact next permanent number, ordinal/count, ordinal-indexed gap and fixed deadline; completes missing records without changing evidence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Gives out: ACCEPTED — Identical recovered admission state. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Must never: ACCEPTED — Reset counters, collide identities, skip bounds or rely on lost in-memory timers. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — Source recovery resolves live/unresolved attempts before any further admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.10.1 — Recovery before careful admission: Handles crash before careful admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Gated by: ACCEPTED — C-7H.10.10.2 — Recovery before real-change consumption: Handles recorded but unconsumed change. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Gated by: ACCEPTED — C-7H.10.10.3 — Recovery after consumption before ordinal 1: Handles consumed change before first attempt. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Gated by: ACCEPTED — C-7H.10.10.4 — Recovery after ordinal-1 admission without outcome: Handles admitted ordinal 1 without outcome. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Gated by: ACCEPTED — C-7H.10.10.5 — Recovery after ordinal-1 technical failure: Handles failure with missing anchor bookkeeping. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Gated by: ACCEPTED — C-7H.10.10.6 — Recovery after ordinal-1 terminal outcome: Handles success/protected terminal recovery. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10 — Accepted B9 retry values and episodes | Committed records. | Resumes missing bookkeeping. | No new allowance from a crash. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-7H.10.10.1 — Recovery before careful admission | Durable rejection. | Rechecks current bounds. | No stale permission. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14] |
| 3 · ACCEPTED | C-7H.10.10.2 — Recovery before real-change consumption | Consumption lookup. | Claims once. | No duplicated use. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14] |
| 4 · ACCEPTED | C-7H.10.10.3 — Recovery after consumption before ordinal 1 | Committed consumer. | Resumes its first admission. | No second episode. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14] |
| 5 · ACCEPTED | C-7H.10.10.4 — Recovery after ordinal-1 admission without outcome | Source outcome evidence. | Recovers first. | No duplicate execution. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14] |
| 6 · ACCEPTED | C-7H.10.10.5 — Recovery after ordinal-1 technical failure | Committed outcome. | Reconstructs identical values. | No clock reset. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14] |
| 7 · ACCEPTED | C-7H.10.10.6 — Recovery after ordinal-1 terminal outcome | Durable outcome. | Completes bookkeeping. | No success-to-failure rewrite. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14] |

SUB-PARTS: C-7H.10.10.1 — Recovery before careful admission; C-7H.10.10.2 — Recovery before real-change consumption; C-7H.10.10.3 — Recovery after consumption before ordinal 1; C-7H.10.10.4 — Recovery after ordinal-1 admission without outcome; C-7H.10.10.5 — Recovery after ordinal-1 technical failure; C-7H.10.10.6 — Recovery after ordinal-1 terminal outcome

### C-7H.10.10.1 — Recovery before careful admission
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — Crash after durable rejection but before the one careful retry. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Takes in: ACCEPTED — The findable rejection record and fixed episode deadline. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Does: ACCEPTED — Admits only if the one allowance remains and the deadline has not passed. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Gives out: ACCEPTED — A permitted careful attempt or truthful time exhaustion. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Must never: ACCEPTED — Restart the clock because recovery took time. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — Expired deadline starts nothing. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.10 — Values-layer crash reconstruction: No admission exists until compare-and-commit. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.10 — Values-layer crash reconstruction | Rejection and absent admission. | Checks deadline before admission. | No pre-consumed count. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7H.10.10.2 — Recovery before real-change consumption
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — Change record exists but consumption was not committed. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Takes in: ACCEPTED — The immutable unconsumed change. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Does: ACCEPTED — Finds it and applies the ordinary atomic consumption check. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Gives out: ACCEPTED — A still-available change or a recovered existing consumption. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Must never: ACCEPTED — Edit the change to mark use. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — Single-consumption rules remain active. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.10 — Values-layer crash reconstruction: A change record alone is not consumed authority. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.10 — Values-layer crash reconstruction | Durable change and absent consumption. | Checks and consumes once. | No automatic episode. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7H.10.10.3 — Recovery after consumption before ordinal 1
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — Consumption committed but later-episode first admission absent. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Takes in: ACCEPTED — The committed consumption and unchanged-input confirmation. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Does: ACCEPTED — Completes that same ordinal-1 admission idempotently with no_gap_before_ordinal_1 [proposed] and deadline_pending_from_first_durable_failure [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Gives out: ACCEPTED — The missing first admission only. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Must never: ACCEPTED — Admit something else or invent actual anchors. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — Required consumption/identity evidence must remain valid. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.10 — Values-layer crash reconstruction: Existing consumption fixes the authorized episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.10 — Values-layer crash reconstruction | Existing consumption. | Completes the same authorized admission. | No second consumer. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7H.10.10.4 — Recovery after ordinal-1 admission without outcome
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The first continuation attempt is admitted but no durable source result exists. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Takes in: ACCEPTED — The source operation and live/unresolved state. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Does: ACCEPTED — Runs source-owned recovery first. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Gives out: ACCEPTED — Proven outcome or continued unresolved status. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Must never: ACCEPTED — Admit another attempt while live/unresolved. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — No further admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.10 — Values-layer crash reconstruction: Existing admission blocks another live attempt. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.10 — Values-layer crash reconstruction | Existing live attempt. | Uses source recovery. | No second ordinal 1. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7H.10.10.5 — Recovery after ordinal-1 technical failure
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — Durable technical failure exists but derived deadline/gap/B9 records are incomplete. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Takes in: ACCEPTED — That exact outcome and recorded context. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Does: ACCEPTED — Appends only missing records lookup-first with identical anchors. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Gives out: ACCEPTED — Recovered actual deadline and gap evidence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Must never: ACCEPTED — Recalculate a different clock or retry the completed outcome. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — Unreadable/contradictory evidence blocks reconstruction. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.10 — Values-layer crash reconstruction: Actual durable failure fixes missing anchors. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.10 — Values-layer crash reconstruction | Durable first technical failure. | Reconstructs exact anchors. | No altered clock or gap. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7H.10.10.6 — Recovery after ordinal-1 terminal outcome
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — Ordinal 1 has success or another terminal/protected result. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Takes in: ACCEPTED — The durable source result. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Does: ACCEPTED — Completes its matching disposition idempotently. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Gives out: ACCEPTED — The true terminal or protected state. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Must never: ACCEPTED — Create a deadline or later retry that the result does not permit. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — The outcome's own rules govern. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.10 — Values-layer crash reconstruction: Actual terminal class remains authoritative. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.10 — Values-layer crash reconstruction | Durable actual outcome. | Records its class. | No invented retryability. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7H.10.11 — Values-layer fail-closed matrix
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — Fourteen named refusal/exhaustion/integrity conditions on top of B9's base matrix. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Takes in: ACCEPTED — Config/class/anchor evidence, bounds, rejection authority, real-change validity, ordinal-1 authority/outcome and integrity state. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Does: ACCEPTED — Refuses missing/unbound config, missing class/anchor, unauthorized careful attempt, second substantive attempt, malformed/used change and unqualified ordinal-1 opening; records count/time exhaustion; routes protected outcomes correctly. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gives out: ACCEPTED — Honest refusal, exhaustion or indeterminate recovery. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Must never: ACCEPTED — Bypass R1, a hold, privacy or acceptance; force-cancel a running source; fabricate technical deadlines from protected results. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Fails closed by: ACCEPTED — Contradictory episode/consumption evidence, permanent-number collisions and within-episode ordinal resets are surfaced as indeterminate, never guessed. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10 — Accepted B9 retry values and episodes: All malformed admission and continuation evidence fails closed. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gated by: ACCEPTED — C-7H.10.11.1 — Missing retry configuration refusal: Handles unreadable/unbound budget. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gated by: ACCEPTED — C-7H.10.11.2 — Missing schedule class refusal: Handles absent schedule class. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gated by: ACCEPTED — C-7H.10.11.3 — Missing retry anchor refusal: Handles absent anchor evidence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gated by: ACCEPTED — C-7H.10.11.4 — Technical attempt-count exhaustion: Handles reached episode count. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gated by: ACCEPTED — C-7H.10.11.5 — Deadline reached while waiting: Handles deadline reached while waiting. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gated by: ACCEPTED — C-7H.10.11.6 — Careful retry requested after deadline: Handles late careful-retry request. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gated by: ACCEPTED — C-7H.10.11.7 — Deadline passes during execution: Handles expiration during execution. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gated by: ACCEPTED — C-7H.10.11.8 — Careful retry without rejection authority: Handles absent rejection authority. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gated by: ACCEPTED — C-7H.10.11.9 — Second substantive admission refusal: Handles repeated substantive admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gated by: ACCEPTED — C-7H.10.11.10 — Invalid or consumed real-change refusal: Handles invalid/used change. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gated by: ACCEPTED — C-7H.10.11.11 — Unauthorized later ordinal-1 refusal: Handles unauthorized first continuation attempt. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gated by: ACCEPTED — C-7H.10.11.12 — Protected later ordinal-1 outcome: Handles protected first-attempt outcome. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gated by: ACCEPTED — C-7H.10.11.13 — Contradictory episode integrity state: Handles contradictory episode evidence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gated by: ACCEPTED — C-7H.10.11.14 — Retry boundary bypass refusal: Handles admission/gate bypass. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10 — Accepted B9 retry values and episodes | Failure condition. | Stops and records. | No guessed permission. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |
| 2 · ACCEPTED | C-7H.10.11.1 — Missing retry configuration refusal | Bad reference. | Stops admission. | Failure remains visible. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |
| 3 · ACCEPTED | C-7H.10.11.2 — Missing schedule class refusal | Absent class. | Stops admission. | No guessed schedule. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |
| 4 · ACCEPTED | C-7H.10.11.3 — Missing retry anchor refusal | Missing evidence. | Stops timed admission. | Special ordinal-1 states remain distinct. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |
| 5 · ACCEPTED | C-7H.10.11.4 — Technical attempt-count exhaustion | Current episode count. | Refuses requests. | No predecessor recount. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |
| 6 · ACCEPTED | C-7H.10.11.5 — Deadline reached while waiting | Reached deadline. | Records exhaustion. | No retry starts. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |
| 7 · ACCEPTED | C-7H.10.11.6 — Careful retry requested after deadline | Expired deadline. | Refuses. | No reset. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |
| 8 · ACCEPTED | C-7H.10.11.7 — Deadline passes during execution | Running attempt. | Lets its seam finish. | No next admission. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |
| 9 · ACCEPTED | C-7H.10.11.8 — Careful retry without rejection authority | Absent rejection. | Refuses. | No invented authority. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |
| 10 · ACCEPTED | C-7H.10.11.9 — Second substantive admission refusal | Spent allowance. | Refuses. | No class conversion. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |
| 11 · ACCEPTED | C-7H.10.11.10 — Invalid or consumed real-change refusal | Defective/reused record. | Refuses. | No new episode. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |
| 12 · ACCEPTED | C-7H.10.11.11 — Unauthorized later ordinal-1 refusal | Missing proof. | Refuses. | No binding. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |
| 13 · ACCEPTED | C-7H.10.11.12 — Protected later ordinal-1 outcome | Protected outcome. | Routes to owner. | No technical fiction. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |
| 14 · ACCEPTED | C-7H.10.11.13 — Contradictory episode integrity state | Conflicting records. | Surfaces indeterminate. | No new attempt. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |
| 15 · ACCEPTED | C-7H.10.11.14 — Retry boundary bypass refusal | Bypass attempt. | Refuses/logs. | No hidden execution. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |

SUB-PARTS: C-7H.10.11.1 — Missing retry configuration refusal; C-7H.10.11.2 — Missing schedule class refusal; C-7H.10.11.3 — Missing retry anchor refusal; C-7H.10.11.4 — Technical attempt-count exhaustion; C-7H.10.11.5 — Deadline reached while waiting; C-7H.10.11.6 — Careful retry requested after deadline; C-7H.10.11.7 — Deadline passes during execution; C-7H.10.11.8 — Careful retry without rejection authority; C-7H.10.11.9 — Second substantive admission refusal; C-7H.10.11.10 — Invalid or consumed real-change refusal; C-7H.10.11.11 — Unauthorized later ordinal-1 refusal; C-7H.10.11.12 — Protected later ordinal-1 outcome; C-7H.10.11.13 — Contradictory episode integrity state; C-7H.10.11.14 — Retry boundary bypass refusal

### C-7H.10.11.1 — Missing retry configuration refusal
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — Refusal when the budget configuration is missing, unreadable or version-unbound. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Takes in: ACCEPTED — The exact retry_budget_ref [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Does: ACCEPTED — Admits nothing and logs the failing reference. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gives out: ACCEPTED — Explicit fail-closed event. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Must never: ACCEPTED — Supply a default configuration. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Fails closed by: ACCEPTED — No admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.11 — Values-layer fail-closed matrix: Configuration failure cannot be defaulted. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.11 — Values-layer fail-closed matrix | Configuration ref. | Refuses and logs reference. | No default. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7H.10.11.2 — Missing schedule class refusal
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — Refusal when an anchor record lacks a readable schedule_class [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Takes in: ACCEPTED — The durable anchor record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Does: ACCEPTED — Stops admission without choosing a class. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gives out: ACCEPTED — A recorded configuration/evidence failure. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Must never: ACCEPTED — Default the missing class. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Fails closed by: ACCEPTED — No admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.11 — Values-layer fail-closed matrix: Recorded class is mandatory. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.11 — Values-layer fail-closed matrix | Anchor record. | Refuses. | No guessed class. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7H.10.11.3 — Missing retry anchor refusal
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — Refusal when no durable outcome supports the required anchor. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Takes in: ACCEPTED — Outcome-record lookup. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Does: ACCEPTED — Recognizes that no ordinary timed-admission anchor exists to satisfy. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gives out: ACCEPTED — Blocked admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Must never: ACCEPTED — Fabricate a timestamp or outcome. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Fails closed by: ACCEPTED — No admission; the separately authorized later ordinal-1 case uses its explicit pending states. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.11 — Values-layer fail-closed matrix: Ordinary anchors require durable outcomes. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.11 — Values-layer fail-closed matrix | Outcome lookup. | Refuses ordinary timed admission. | No fabricated anchor. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7H.10.11.4 — Technical attempt-count exhaustion
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — Exhaustion when three ordinals are committed in the exact technical episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Takes in: ACCEPTED — Durable current-episode attempt entries. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Does: ACCEPTED — Records exhaustion and refuses further requests with that status. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gives out: ACCEPTED — Closed technical allowance. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Must never: ACCEPTED — Recount predecessor episodes or omit the original ordinal. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Fails closed by: ACCEPTED — No further attempt in the episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.11 — Values-layer fail-closed matrix: Three committed ordinals exhaust the exact episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.11 — Values-layer fail-closed matrix | Three committed ordinals. | Records exhaustion. | No next attempt. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7H.10.11.5 — Deadline reached while waiting
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — Time exhaustion while a technical or careful retry waits for admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Takes in: ACCEPTED — Fixed episode deadline and current time. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Does: ACCEPTED — Records truthful time exhaustion and does not start the next retry. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gives out: ACCEPTED — Exhaustion disposition. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Must never: ACCEPTED — Treat a satisfied gap as permission after deadline. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Fails closed by: ACCEPTED — No start. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.11 — Values-layer fail-closed matrix: Time bound also gates waiting work. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.11 — Values-layer fail-closed matrix | Fixed deadline. | Records time exhaustion. | No start. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7H.10.11.6 — Careful retry requested after deadline
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — Time exhaustion when delay, crash or recovery consumes the careful-retry window before admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Takes in: ACCEPTED — Durable rejection and fixed episode deadline. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Does: ACCEPTED — Refuses the late start and records truthful time exhaustion. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gives out: ACCEPTED — Exhaustion disposition. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Must never: ACCEPTED — Restart the clock after recovery. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Fails closed by: ACCEPTED — No careful retry starts. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.11 — Values-layer fail-closed matrix: Recovery does not extend the careful window. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.11 — Values-layer fail-closed matrix | Rejection and elapsed deadline. | Records time exhaustion. | No clock restart. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7H.10.11.7 — Deadline passes during execution
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — Expiration while the source attempt is already running. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Takes in: ACCEPTED — Existing admitted attempt and elapsed clock. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Does: ACCEPTED — Lets that attempt finish under its source seam and refuses every further retry afterward. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gives out: ACCEPTED — Actual source outcome plus closed further admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Must never: ACCEPTED — Force-cancel it or override source timeout/terminal rules. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Fails closed by: ACCEPTED — No further retry admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.11 — Values-layer fail-closed matrix: Admission bounds do not cancel source work. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.11 — Values-layer fail-closed matrix | Already-running attempt. | Preserves seam execution. | No later retry. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7H.10.11.8 — Careful retry without rejection authority
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — Missing per-case authorization when no durable rejection record exists. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Takes in: ACCEPTED — Rejection lookup. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Does: ACCEPTED — Refuses the requested careful retry. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gives out: ACCEPTED — Recorded refusal. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Must never: ACCEPTED — Invent an authorization record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Fails closed by: ACCEPTED — No admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.11 — Values-layer fail-closed matrix: Per-case rejection must exist durably. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.11 — Values-layer fail-closed matrix | Rejection lookup. | Refuses. | No invented authorization. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7H.10.11.9 — Second substantive admission refusal
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — A second requested careful retry in the same episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Takes in: ACCEPTED — The committed substantive attempt history. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Does: ACCEPTED — Refuses while the terminal substantive result stands. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gives out: ACCEPTED — Preserved rejection. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Must never: ACCEPTED — Convert it to technical retryability. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Fails closed by: ACCEPTED — No second admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.11 — Values-layer fail-closed matrix: One substantive allowance is final for the episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.11 — Values-layer fail-closed matrix | Careful-attempt history. | Refuses. | Terminal stands. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7H.10.11.10 — Invalid or consumed real-change refusal
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — Missing change, invalid category, unexplained other_real_change, absent evidence or existing committed consumption. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Takes in: ACCEPTED — Change and consumption records. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Does: ACCEPTED — Refuses to open a new episode; logs reuse attempts. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gives out: ACCEPTED — Explicit blocked continuation. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Must never: ACCEPTED — Accept repetition alone as change or reuse the same consumption. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Fails closed by: ACCEPTED — No new episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.11 — Values-layer fail-closed matrix: Real change must be valid and unconsumed. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.11 — Values-layer fail-closed matrix | Change and consumption evidence. | Refuses/logs reuse. | No new episode. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7H.10.11.11 — Unauthorized later ordinal-1 refusal
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — Missing committed consumption or missing seam confirmation of unchanged canonical inputs. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Takes in: ACCEPTED — The requested same-identity continuation's evidence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Does: ACCEPTED — Refuses before opening an episode or binding an attempt. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gives out: ACCEPTED — No admission binding. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Must never: ACCEPTED — Treat the change record alone as consumed authority. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Fails closed by: ACCEPTED — Nothing opens. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.11 — Values-layer fail-closed matrix: Consumption and unchanged inputs are mandatory. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.11 — Values-layer fail-closed matrix | Consumption and input-sameness proof. | Refuses before binding. | No opened episode. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7H.10.11.12 — Protected later ordinal-1 outcome
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — Later ordinal 1 ends protected, terminal, held, privacy-refused or indeterminate. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Takes in: ACCEPTED — The actual durable outcome class. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Does: ACCEPTED — Routes through that class's existing rules. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gives out: ACCEPTED — Correct terminal/protected/recovery state. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Must never: ACCEPTED — Manufacture a technical deadline path from it. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Fails closed by: ACCEPTED — No further technical retry from that result. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.11 — Values-layer fail-closed matrix: Actual outcome class governs. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.11 — Values-layer fail-closed matrix | Actual result. | Uses owning class rules. | No fake technical deadline. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7H.10.11.13 — Contradictory episode integrity state
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — Conflicting episode/consumption evidence, repeated permanent attempt numbers or colliding/reset ordinals within an episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Takes in: ACCEPTED — Durable identity and state records. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Does: ACCEPTED — Surfaces indeterminate state for recovery. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gives out: ACCEPTED — Explicit unresolved integrity failure. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Must never: ACCEPTED — Guess a winner or renumber evidence to fit. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Fails closed by: ACCEPTED — No admission on contradictory evidence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.11 — Values-layer fail-closed matrix: Integrity contradictions remain unresolved. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.11 — Values-layer fail-closed matrix | Identity/state records. | Surfaces indeterminate. | No guessed winner. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7H.10.11.14 — Retry boundary bypass refusal
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — An attempted bypass of R1, a hold, privacy or acceptance. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Takes in: ACCEPTED — The unauthorized attempted action. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Does: ACCEPTED — Refuses and records the violation. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Gives out: ACCEPTED — Violation log and unchanged protected state. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Must never: ACCEPTED — Grant permission through retries or change records. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Fails closed by: ACCEPTED — No bypass execution. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.11 — Values-layer fail-closed matrix: Admission never supersedes protected gates. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.11 — Values-layer fail-closed matrix | Unauthorized attempt. | Refuses and logs violation. | No execution. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7H.10.12 — Values-layer state events
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Five proposed canonical state/disposition events in addition to the existing B9 log set. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Takes in: ACCEPTED — Actual config version, real change, consumption, early stop or exhaustion. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Does: ACCEPTED — Records each real operation once while keeping canonical state separate from logs and evidence votes. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Gives out: ACCEPTED — retry_budget_config_recorded [proposed], real_change_recorded [proposed], real_change_consumed [proposed], retry_early_stopped [proposed] and retry_episode_exhausted [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Must never: ACCEPTED — Edit a change record as consumption, create double evidence or inflate certainty through repetition. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — Privacy authorization governs every record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): state-event visibility is subject to privacy and visibility authority. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Changes: ACCEPTED — C-7H.10.12.1 — retry_budget_config_recorded [proposed]: Logs each new configuration version. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Changes: ACCEPTED — C-7H.10.12.2 — real_change_recorded [proposed]: Logs actual new change evidence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Changes: ACCEPTED — C-7H.10.12.3 — real_change_consumed [proposed]: Logs one committed consumption. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Changes: ACCEPTED — C-7H.10.12.4 — retry_early_stopped [proposed]: Logs cause-bearing early stop. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Changes: ACCEPTED — C-7H.10.12.5 — retry_episode_exhausted [proposed]: Logs the closing bound or cause. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Changes: ACCEPTED — C-7H.9.7.4 — retry_attempt_admitted [proposed]: Extends the existing admission event with exact bindings. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10 — Accepted B9 retry values and episodes | Committed transitions. | Appends events. | No extra truth votes. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] |
| 2 · ACCEPTED | C-7H.10.12.1 — retry_budget_config_recorded [proposed] | Committed revision. | Appends event. | No mutable history. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] |
| 3 · ACCEPTED | C-7H.10.12.2 — real_change_recorded [proposed] | Durable evidence. | Appends event. | No truth vote. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] |
| 4 · ACCEPTED | C-7H.10.12.3 — real_change_consumed [proposed] | Consumer binding. | Appends event. | No second authority. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] |
| 5 · ACCEPTED | C-7H.10.12.4 — retry_early_stopped [proposed] | Unsafe/useless evidence. | Appends event. | No disguise. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] |
| 6 · ACCEPTED | C-7H.10.12.5 — retry_episode_exhausted [proposed] | Disposition evidence. | Appends event. | No false success. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] |

SUB-PARTS: C-7H.10.12.1 — retry_budget_config_recorded [proposed]; C-7H.10.12.2 — real_change_recorded [proposed]; C-7H.10.12.3 — real_change_consumed [proposed]; C-7H.10.12.4 — retry_early_stopped [proposed]; C-7H.10.12.5 — retry_episode_exhausted [proposed]

### C-7H.10.12.1 — retry_budget_config_recorded [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Proposed state event for each budget configuration version. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Takes in: ACCEPTED — A new immutable config version. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Does: ACCEPTED — Records its creation once. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Gives out: ACCEPTED — retry_budget_config_recorded [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Must never: ACCEPTED — Edit an earlier version. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.12 — Values-layer state events: Only a real new config version is recorded. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.12 — Values-layer state events | Committed config. | Appends state event. | No mutable revision. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-7H.10.12.2 — real_change_recorded [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Proposed state event for real-change recording. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Takes in: ACCEPTED — The immutable change record. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Does: ACCEPTED — Records its creation once. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Gives out: ACCEPTED — real_change_recorded [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Must never: ACCEPTED — Treat the event as independent evidence of truth. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.12 — Values-layer state events: Only a real change record is logged. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.12 — Values-layer state events | Committed change record. | Appends state event. | No truth vote. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-7H.10.12.3 — real_change_consumed [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Proposed state event for the separate consumption commit. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Takes in: ACCEPTED — Committed consumption with its bound consumer. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Does: ACCEPTED — Records that append-only consumption once. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Gives out: ACCEPTED — real_change_consumed [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Must never: ACCEPTED — Mutate the change record to indicate use. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — A consumed record cannot authorize another continuation. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.12 — Values-layer state events: Only committed unique consumption is logged. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.12 — Values-layer state events | Bound consumer. | Appends state event. | No second authorization. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-7H.10.12.4 — retry_early_stopped [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — Proposed state event for a cause-bearing early stop. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §8]
- Takes in: ACCEPTED — clearly_useless or unsafe evidence. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §8]
- Does: ACCEPTED — Preserves the real stopping cause. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §8]
- Gives out: ACCEPTED — retry_early_stopped [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §8]
- Must never: ACCEPTED — Hide early stop as success or ordinary exhaustion. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — The episode admits no further attempt without new authorized change. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.12 — Values-layer state events: Early stop preserves actual cause. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.12 — Values-layer state events | Actual stopping evidence. | Appends state event. | No cause disguise. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-7H.10.12.5 — retry_episode_exhausted [proposed]
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Proposed state event naming the gate closing further admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §9]
- Takes in: ACCEPTED — Attempt gate, time deadline, careful-retry rejection or recorded early stop and outcome references. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §9]
- Does: ACCEPTED — Records the actual cause with preserved source-state references. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §9]
- Gives out: ACCEPTED — retry_episode_exhausted [proposed]. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §9]
- Must never: ACCEPTED — Convert exhausted failure into success. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Continuation requires new real-change authority. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10.12 — Values-layer state events: Exhaustion records its true closing gate. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10.12 — Values-layer state events | Episode outcome and gate. | Appends state event. | Preserved failed work. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-7H.10.13 — Retry and hold-release seam
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — A live hold blocks retry without spending its budget, and release is not automatic retry authority. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §12]
- Takes in: ACCEPTED — Hold/refusal/release records and unchanged retry state. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §12]
- Does: ACCEPTED — Records retry_refused [proposed] while held with no count, gap, episode or hold-record effects; after release performs a fresh R0/R1 evaluation with all counts/anchors/dispositions intact. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §12]
- Gives out: ACCEPTED — An honest refused or newly evaluated admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §12]
- Must never: ACCEPTED — Queue around a hold, drain/reset its budget, manufacture success or fire an automatic retry from release alone. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — Exhaustion and early-stop real-change requirements survive release. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §12]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.10 — Accepted B9 retry values and episodes: Hold release merely permits a fresh admission check. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §12]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.10 — Accepted B9 retry values and episodes | Hold/release records. | Rechecks admission. | No automatic execution on release. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7H.11 — RM-RR-01 [proposed] reread relevance declaration
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — The accepted declaration for evaluating possible condition-based reread reasons. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — An existing old reading/root and authorized new-information candidates. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Evaluates purpose-scoped relevance on demand without producing an A25 assignment or launching a reread itself. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — A recorded evaluation that may inform a real trigger reason. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Gate the manual path, manufacture assignment evidence or make an unresolved clue launch a reread. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Missing or invalid declaration prevents condition-based evaluation only; failed evaluation schedules nothing. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: ACCEPTED — C-7H.11.1 — RM-RR-01 [proposed] identity and purpose: Names the exact declaration and purpose. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fed by: ACCEPTED — C-7H.11.2 — Reread relevance target and candidates: Bounds target and candidate types. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fed by: ACCEPTED — C-7H.11.4 — Reread relevance dimensions: Uses declared dimensions independently. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fed by: ACCEPTED — C-7H.11.6 — Reread relevance reason and consequence: Records why evaluation matters and what it may do. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7H.11.3 — Reread relevance context gates: Requires authorization and configured time range. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7H.11.5 — Reread relevance mouth and timing limits: Uses no mouth and on-demand evaluation only. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7H.11.7 — Relevance versus A25 assignment boundary: Keeps relevance separate from A25 assignment. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7H.11.8 — Manual path independent of relevance: Manual requests need no relevance permission. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7H.11.9 — Reread relevance use and uncertainty: Uses bounded uncertainty and separate pass context. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Changes: ACCEPTED — C-7H.11.10 — Reread relevance event and failure boundary: Records one relevance evaluation event. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7H — Reread Lifecycle (§7H) | New-information candidates. | Uses RM-RR-01 [proposed]. | Manual path unaffected. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |
| 2 · DESIGNED | C-7H.1.2 — Condition-based reread trigger | Possible material change. | Evaluates relevance. | No evaluation-only trigger. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |
| 3 · ACCEPTED | C-7H.11.5 — Reread relevance mouth and timing limits | Evaluation context. | Enforces limits. | No expansion by implementation. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |
| 4 · ACCEPTED | C-7H.11.10 — Reread relevance event and failure boundary | Declaration and result. | Preserves honest failure/log ownership. | Manual path unaffected. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |
| 5 · ACCEPTED | C-7H.11.3 — Reread relevance context gates | Type and declared time range. | Filters candidates. | No mandatory shared-thread gate. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |
| 6 · ACCEPTED | C-7H.11.6 — Reread relevance reason and consequence | Recorded relevance. | Carries reason evidence. | B10 trigger remains separate. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |
| 7 · ACCEPTED | C-7R.16.4 — Condition-based reread declaration interface | New information and a prior reading/root under reread_trigger_evaluation. | Supplies the complete canonical proposed RM-RR-01 declaration and manual/condition-based boundary. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §11] |

SUB-PARTS: C-7H.11.1 — RM-RR-01 [proposed] identity and purpose; C-7H.11.2 — Reread relevance target and candidates; C-7H.11.3 — Reread relevance context gates; C-7H.11.4 — Reread relevance dimensions; C-7H.11.5 — Reread relevance mouth and timing limits; C-7H.11.6 — Reread relevance reason and consequence; C-7H.11.7 — Relevance versus A25 assignment boundary; C-7H.11.8 — Manual path independent of relevance; C-7H.11.9 — Reread relevance use and uncertainty; C-7H.11.10 — Reread relevance event and failure boundary

### C-7H.11.1 — RM-RR-01 [proposed] identity and purpose
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Proposed RM-RR-01 v1_0 for Reread Lifecycle, with settled purpose reread_trigger_evaluation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — A request to evaluate materially relevant new information. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Uses the optional explanatory label evaluating whether materially relevant new information justifies a condition-based reread trigger. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — A versioned purpose-specific declaration binding. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Treat the label as a new trigger or mode. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Unknown purpose follows the shared halt rule. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.11 — RM-RR-01 [proposed] reread relevance declaration | Mode identity/version. | Binds evaluation. | No unknown purpose. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.11.2 — Reread relevance target and candidates
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — An existing old reading with its root as target, and new-information items as candidates. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — New roots/evidence, new positional context, resolved speaker/thread information, corrected provenance, newly available required channels or recorded Ness responses. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — References the items by identity under prior authorization. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — A purpose-authorized candidate set. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Treat candidates as already accepted A25 assignment evidence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Unverifiable or unauthorized material cannot bypass its owning boundary. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the target and candidates are purpose-authorized before intake. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.11 — RM-RR-01 [proposed] reread relevance declaration | Old reading and new information. | Selects permitted evaluation inputs. | No hidden context access. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.11.3 — Reread relevance context gates
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Deterministic object_type_matches always and within_declared_time_range only when a range is declared. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — Candidate type and any declared temporal range. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Applies those categorical gates; does not select same_thread_or_group or precedes_target_in_same_thread. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — Gate-eligible new information from any relevant source location. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Exclude potentially relevant information merely because it is outside the old reading's thread. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Failed required gates exclude candidates; time-span value remains open. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.11 — RM-RR-01 [proposed] reread relevance declaration: Only declared gates apply. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.11 — RM-RR-01 [proposed] reread relevance declaration | Allowed candidate records. | Applies selected gates. | No forbidden link prerequisite. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.11.4 — Reread relevance dimensions
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Six selected dimensions with settled producers and honest applicability. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — Gate-eligible candidate/target relations. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Uses embedding semantic_similarity and deterministic temporal_distance, positional_distance, explicit_links, ness_response_links and active_clash_links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — Separate provenance-bearing dimensions. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Select currentness_status, proposal_acceptance_outcome or reading_context_status for these new-information candidates. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Missing/inapplicable values retain the shared honest absence handling. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: ACCEPTED — C-7H.11.4.1 — Reread semantic_similarity: Carries semantic similarity as a clue. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fed by: ACCEPTED — C-7H.11.4.2 — Reread temporal_distance: Carries temporal distance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fed by: ACCEPTED — C-7H.11.4.3 — Reread positional_distance: Carries position only when available. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fed by: ACCEPTED — C-7H.11.4.4 — Reread explicit_links: Carries explicit recorded links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fed by: ACCEPTED — C-7H.11.4.5 — Reread ness_response_links: Carries real response links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fed by: ACCEPTED — C-7H.11.4.6 — Reread active_clash_links: Carries recorded active clashes. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.11 — RM-RR-01 [proposed] reread relevance declaration | Authorized context. | Builds comparison record. | No collapsed score. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |

SUB-PARTS: C-7H.11.4.1 — Reread semantic_similarity; C-7H.11.4.2 — Reread temporal_distance; C-7H.11.4.3 — Reread positional_distance; C-7H.11.4.4 — Reread explicit_links; C-7H.11.4.5 — Reread ness_response_links; C-7H.11.4.6 — Reread active_clash_links

### C-7H.11.4.1 — Reread semantic_similarity
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — The embedding-model dimension of candidate/target similarity. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — Eligible new information and the old reading target. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Produces semantic_similarity under the shared producer contract. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — A similarity dimension, not truth evidence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Treat similarity alone as a reread reason. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.11.4 — Reread relevance dimensions | Permitted candidates. | Records dimension. | No sole decision. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.11.4.2 — Reread temporal_distance
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — A deterministic temporal relation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — Candidate and target time provenance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Produces temporal_distance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — A temporal dimension. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Treat time passing alone as a trigger. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.11.4 — Reread relevance dimensions | Recorded timestamps. | Records dimension. | No time-only trigger. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.11.4.3 — Reread positional_distance
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Candidate-root versus old-reading-root distance within a shared thread. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — Their actual recorded positions when they share a thread. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Measures new positional context as a dimension rather than a universal exclusion gate. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — positional_distance where applicable. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Invent shared-thread adjacency. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Inapplicable values remain honest absence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.11.4 — Reread relevance dimensions | Position evidence. | Records value or honest state. | No fabricated relation. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.11.4.4 — Reread explicit_links
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Recorded derived_from chains, shared root IDs and theme links indicating structural bearing. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — Existing structural references. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Produces a deterministic explicit_links dimension. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — Recorded structural relation provenance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Convert theme or derivation links into independent truth evidence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.11.4 — Reread relevance dimensions | Existing link refs. | Records dimension. | No inferred link acceptance. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.11.4.5 — Reread ness_response_links
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Deterministic links to recorded Ness-response events. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — Existing response references. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Produces ness_response_links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — Recorded response-bearing structure. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Invent causality that the recorded responses do not show. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.11.4 — Reread relevance dimensions | Recorded response refs. | Records dimension. | No invented causality. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.11.4.6 — Reread active_clash_links
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — A deterministic recorded clash touching the old reading. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — Existing active clash references. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Produces active_clash_links without resolving the clash. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — A clash-bearing dimension. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Select a winner through relevance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.11.4 — Reread relevance dimensions | Existing clash refs. | Records dimension. | No new clash acceptance. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.11.5 — Reread relevance mouth and timing limits
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Explicit mouth authorization none and on-demand condition-evaluation timing only. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — A request from the settled trigger machinery. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Evaluates when asked whether material new information exists; declares no precomputation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — An evaluation, never itself a trigger. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Add, remove, rename or reclassify manual, condition_based, scheduled_automatic_retry or on_rejection. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Missing declaration does not block the independent manual path. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.11 — RM-RR-01 [proposed] reread relevance declaration: Declared permission excludes mouth and precompute. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.11 — RM-RR-01 [proposed] reread relevance declaration | Evaluation request. | Limits processing. | No direct surface. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.11.6 — Reread relevance reason and consequence
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — The declared rule form required for evaluating materially relevant new information. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — Possible changes, including weak clues and changed/replaced-pattern flags. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Permits clues to prompt evaluation; an actual reread still needs a real recorded reason and the B10 machinery. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — A flagged/evaluated possible condition, never automatic application. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Launch rereading from unresolved relevance alone or initiate blanket rereading. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — No real reason means no reread; incomplete evaluation schedules nothing. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.11 — RM-RR-01 [proposed] reread relevance declaration: Evaluation can inform but never launch a reread. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.11 — RM-RR-01 [proposed] reread relevance declaration | New-information relationship. | Informs condition trigger decision. | No automatic trigger. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.11.7 — Relevance versus A25 assignment boundary
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — RM-RR-01 [proposed] is not the still-open A25 relationship-assignment producer. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — The relevance evaluation and independently truthful semantic relationships. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Leaves direct/wider-context assignment and its evidence to that separate producer. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — No manufactured assignment. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Supply false, third, empty, sentinel or default assignment values. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — A mode slot still requires its own valid committed record. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.7 — A25 semantic reread assignment: A25 remains the semantic assignment owner. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.11 — RM-RR-01 [proposed] reread relevance declaration | Validated relevance record. | Preserves producer boundary. | No manufactured assignment. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.11.8 — Manual path independent of relevance
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Manual rereads require no relevance evaluation or further justification. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — The manual request event itself as trigger, initiator and reason. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Leaves the request on its settled B10/manual compatibility route. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — Manual eligibility unaffected by RM-RR-01 [proposed] availability. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Wait for new information, turn the request into evidence or gate manual use through this declaration. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Declaration absence blocks only condition-based evaluation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.8 — Manual reread compatibility: Uses the typed manual compatibility route. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.11 — RM-RR-01 [proposed] reread relevance declaration | Manual no-information trigger. | Keeps manual route open. | No false relationship. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.11.9 — Reread relevance use and uncertainty
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Trigger-evaluation-only use of authorized new information and the identified old reading. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — The evaluation's dimensions and uncertainty state. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Uses T2-UNRES-SHARED [proposed] v1_0; emits records with no direct surface; leaves the reread pass's context to RR2's separate Privacy→Retrieval→Relevance sequence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — A bounded uncertain/validated evaluation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Read or configure the actual reread context through this trigger-evaluation mode. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Unresolved clues alone authorize no reread; unsafe evaluation stops without scheduling. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling: Reuses T2-UNRES-SHARED [proposed] with reread-specific consequences. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.11 — RM-RR-01 [proposed] reread relevance declaration | Evaluation result. | Limits use. | No unresolved-only authorization. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.11.10 — Reread relevance event and failure boundary
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — One shared relevance-event record per evaluation, linked to any trigger it informed by identity. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — The completed evaluation and any real trigger linkage. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Preserves B10's distinct trigger, mode-slot, snapshot, acceptance, layer and single-parent logs; unknown purpose halts; RR2 failures use their existing reason/state/terminal mappings. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — Auditable evaluation without double evidence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Duplicate B10 state as relevance evidence or invent new RR5 terminal types. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Invalid declaration prevents evaluation, and the manual route remains unaffected. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.11 — RM-RR-01 [proposed] reread relevance declaration: Invalid declaration halts this evaluation only. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.11 — RM-RR-01 [proposed] reread relevance declaration | Mode/result and real linkage. | Appends audit record. | No duplicate B10 evidence. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7H.12 — Retry, reread and hold coordination
Stamp: ACCEPTED    Source: [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §1] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — Shared boundaries among same-operation retry, new-layer reread and external waiting state. [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §1] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — Source status, hold state, trigger and accepted owner decisions. [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §1] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Keeps B9 admission, B10 identity/recovery, B-HOLD release, A29 enough, A25 mode, B16 promotion, B24 acceptance and B11 writable-root ownership distinct. [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §1] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — Coordinated protected handoffs with canonical claims and append-only recovery. [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §1] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §3]
- Must never: ACCEPTED — Use a hold to park rejection until it appears fresh, or treat logs/repetition as truth votes. [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §1] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Held blocks retry and reread; substantive terminal remains terminal except the exact separately accepted policy scope. [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §1] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.12.1 — Retry versus new reading layer: Distinguishes retry from a new reading layer. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2]
- Gated by: ACCEPTED — C-7H.12.2 — Source-store and promotion preservation: Preserves immutable sources and separate promotion. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §2] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §1]
- Gated by: ACCEPTED — C-7B.7 — Hold-until-enough: A live hold blocks retry and reread until owner release. [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7H — Reread Lifecycle (§7H) | Owner states. | Coordinates boundaries. | No protected-state bypass. | [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2] |
| 2 · ACCEPTED | C-7H.12.1 — Retry versus new reading layer | Existing reading result. | Uses B9 or B10 as appropriate. | No invented trigger. | [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2] |
| 3 · ACCEPTED | C-7H.12.2 — Source-store and promotion preservation | Source and acceptance records. | Preserves append-only layering. | No ownership bypass. | [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §1] |

SUB-PARTS: C-7H.12.1 — Retry versus new reading layer; C-7H.12.2 — Source-store and promotion preservation

### C-7H.12.1 — Retry versus new reading layer
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — Retry completes one incomplete identity; reread creates a new identity per real trigger beside completed readings. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2]
- Takes in: ACCEPTED — Whether a committed reading already exists, including honest insufficient_context. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2]
- Does: ACCEPTED — Uses B9 while the original is open/incomplete; uses B10 for later re-examination; changed information requires a new valid trigger and claim. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2]
- Gives out: ACCEPTED — Correctly separated retry and reread routing. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2]
- Must never: ACCEPTED — Let B9 create a trigger, claim or reading layer, or let B10 replace an old operation's outcome. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2]
- Fails closed by: ACCEPTED — A retry request naming a completed reading is refused with the B10 boundary named, without manufacturing a trigger. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.12 — Retry, reread and hold coordination: Completion status fixes the operation boundary. [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.12 — Retry, reread and hold coordination | Committed-reading state. | Routes to proper owner. | No completion disguised as retry. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2] |

SUB-PARTS: NONE

### C-7H.12.2 — Source-store and promotion preservation
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §2] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §1]

ALONE
- What it is: ACCEPTED — Read-only root use, unchanged reading schemas and quarantine-only reread output. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §2] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §1]
- Takes in: ACCEPTED — Existing B11 roots, B24 acceptance and B16 promotion boundaries. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §2] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §1]
- Does: ACCEPTED — References roots/earlier readings by identity; appends through the existing twelve-field validated reading path and leaves promotion to its owner. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §2] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §1]
- Gives out: ACCEPTED — A new quarantine layer with untouched roots and prior readings. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §2] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §1]
- Must never: ACCEPTED — Re-ingest roots, mutate sealed re_reads, add a thirteenth reading field or promote directly. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §2] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §1]
- Fails closed by: ACCEPTED — Production eligibility remains solely the separate B16 route. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §2] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §1]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.12 — Retry, reread and hold coordination: Each existing seam retains its authority. [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §1]
- Gated by: ACCEPTED — C-READ.11 — Quarantine-to-production promotion seam: Accepted reread output remains quarantine-only until separate promotion. [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §2]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7H.12 — Retry, reread and hold coordination | Root and prior reading identities. | Appends only owned output. | No store rewrite or direct production. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §2] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §1] |

SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece USED BY continuations

| Owner whose USED BY is continued | Used in | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| C-7B.7 — Hold-until-enough | ACCEPTED — C-7H.3.2 — RR1 — Reread claim commit | Root/reading holds. | Waits for owning release. | No queue around hold. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2] |
| C-LMAC — Live Mechanism Access Coordinator (§26) | ACCEPTED — C-7H.3.3 — RR2 — Instruction and context snapshot | Purpose and target. | Routes internal-use access. | Authorized assembly. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | ACCEPTED — C-7H.3.3 — RR2 — Instruction and context snapshot | Purpose-specific access. | Limits eligible material. | No unauthorized context. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |
| C-7F — Context Retrieval (§7F) | ACCEPTED — C-7H.3.3 — RR2 — Instruction and context snapshot | Target and declared basis. | Supplies context honestly. | Provenance-bearing snapshot. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |
| C-7R — Attention & Relevance Control (§7R) | ACCEPTED — C-7H.3.3 — RR2 — Instruction and context snapshot | Authorized context. | Applies declared relevance. | Purpose-scoped input. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |
| C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | ACCEPTED — C-7H.3.4 — RR3 — Execution and acceptance | Proposed reading. | Applies the shared check. | No rejected reading. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |
| C-7G.9 — B9 acceptance retry and fallback boundary | ACCEPTED — C-7H.3.4 — RR3 — Execution and acceptance | Rejection and authority. | Preserves five distinct outcome classes. | No fallback bypass. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13] |
| C-7F.7.3 — Accepted B26 stop-after-retry policy | ACCEPTED — C-7H.5.11 — B10 recovery 11 — Retrieval failure | Technical failure. | Keeps failure honest. | No exhausted degraded continuation. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] |
| C-7G.9 — B9 acceptance retry and fallback boundary | ACCEPTED — C-7H.10.6 — Careful-retry and B24 fallback consumption | Durable rejected draft and reason. | Uses one eligible fresh attempt and honest fallback. | No duplicate policy or reuse of rejected answer. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13] |
| C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling | ACCEPTED — C-7H.11.9 — Reread relevance use and uncertainty | Validated/failed/unresolved/disagreement/absence state. | Uses only supported evidence; unresolved-only clues schedule nothing. | No competing uncertainty policy. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |
| C-7B.7 — Hold-until-enough | ACCEPTED — C-7H.12 — Retry, reread and hold coordination | Durable held/released state. | Checks without mutating holds. | Release alone does not admit work. | [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2] |
| C-READ.11 — Quarantine-to-production promotion seam | ACCEPTED — C-7H.12.2 — Source-store and promotion preservation | Validated accepted reading. | Preserves B16 ownership. | No direct production write. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §2] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | ACCEPTED — C-7H.6 — B10 operational logging | Trigger, claim, snapshot, acceptance, layer and recovery operations. | Proceeds only when privacy authorization governs every record, including privacy-block logs. | Nothing in this card. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §9] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | ACCEPTED — C-7H.9.7 — B9 operational event set | Actual R0 resolution, R1 winner, R3 outcome, disposition change, R4 terminal or recovery/failure. | Proceeds only when privacy internal-use, visibility and authority restrictions govern every record. | Nothing in this card. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §10] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | ACCEPTED — C-7H.10.12 — Values-layer state events | Actual config version, real change, consumption, early stop or exhaustion. | Proceeds only when state-event visibility is subject to privacy and visibility authority. | Nothing in this card. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | ACCEPTED — C-7H.11.2 — Reread relevance target and candidates | New roots/evidence, new positional context, resolved speaker/thread information, corrected provenance, newly available required channels or recorded Ness responses. | Proceeds only when the target and candidates are purpose-authorized before intake. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |

## Scope and path placement

C-7H is the DESIGNED reread lifecycle in CY-F. Its accepted subparts supply B10 identity, transactions, duplicate/recovery rules; A25 semantic assignment and its current connection; the distinct manual compatibility carrier; B9 retry architecture and accepted values; and RM-RR-01. Descendants inherit the explicit CY-F placement. Shared B9 is also consumed by the prior worker, acceptance and retrieval boundaries through named incoming continuations; this does not claim a completed whole-cycle assembly or an invented P-MAIN step.

The accepted designs retain proposed field and record names as proposed. Full schemas, enums, bounds and recoveries written here are design behavior, not implementation or runtime activation. A single dual assignment remains one claim, one fixed snapshot, one proposal and one output. Manual reread with no new-information relationship has a typed compatibility record and no fabricated mode. The shared uncertainty owner and B24 careful-retry/fallback owner keep their existing IDs.


## Cross-piece TOGETHER continuations for incoming uses

| Using card | Field | Current owner | Condition / handoff | Source |
|---|---|---|---|---|
| C-7B.7.1.6 — Hold distinctions | Gated by | C-7H — Reread Lifecycle (§7H) | DESIGNED — Distinguishes held waiting from new-layer reread and bounded retry. | [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2] |
| C-READ — Reading record, validator, writer (§6B) | Fed by | C-7H — Reread Lifecycle (§7H) | DESIGNED — Receives a complete new reading layer through the existing validated append path. | [V10 §7H] |
| C-7G.9 — B9 acceptance retry and fallback boundary | Fed by | C-7H — Reread Lifecycle (§7H) | DESIGNED — Uses B9 state, bounds and committed admission authority. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13] |
| C-7G.9.8 — Retry early stop and real-change continuation | Fed by | C-7H — Reread Lifecycle (§7H) | DESIGNED — Uses shared early-stop and real-change rules. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §8] |
| C-7GA.14 — Accepted retry and reread boundaries consumed by the worker | Fed by | C-7H — Reread Lifecycle (§7H) | DESIGNED — Consumes B9 admission or a separately real B10 trigger. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2] |
| C-7GA.14.1 — Technical-retry admission boundary | Gated by | C-7H — Reread Lifecycle (§7H) | DESIGNED — Requires durable configuration, episode and single-winner admission. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| C-7GA.14.2 — Later technical-episode first-attempt boundary | Gated by | C-7H — Reread Lifecycle (§7H) | DESIGNED — Requires consumed real change and unchanged canonical inputs. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| C-7F.7.3 — Accepted B26 stop-after-retry policy | Gated by | C-7H — Reread Lifecycle (§7H) | DESIGNED — Uses generic bounded retry authority; retrieval-specific exhausted failure still stops. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |


## Source conflicts and explicit source-scope differences

| Kind | Sources and exact difference | Preserved treatment |
|---|---|---|
| [SOURCE CONFLICT] | V10's worker keeps a failed queue job terminal and never reselects it. Accepted retry values permit a specifically eligible fresh careful attempt for the same canonical identity after durable rejection. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13] | The CH05-b conflict is carried forward. Source attempt/rejection remains terminal; bounded fresh admission is described only within its accepted policy scope. The exact integrated queue transition is NOT DECIDED. Neither source is silently rewritten. |
| Trigger categories and rejection eligibility | V10 names manual, condition-based and scheduled-technical triggers, then separately states rejection eligibility. B10's trigger_type enum also names on_rejection. [V10 §7H] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §4] | Both source meanings are written. No count contradiction or automatic reread permission is invented. Every real trigger still has a record and reason. |
| Earlier open slots versus later accepted design | Original B10/B9/coordination leaves A25 connection, manual compatibility or retry quantities open. Later accepted A25 v1_2, connection v1_2, manual compatibility v1_0 and values v1_4 settle their stated standalone scope. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §5] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] | Current accepted content fills those scoped openings without claiming build, integration, empirical retrieval quantities, operational scheduling or full CY-F completion. Older connection versions are superseded provenance, not current behavior sources. |
| Generic terminal classification versus exact careful-retry policy | B9 terminal_substantive requires separately declared policy and case authority; later values supply the bounded eligible B24 continuation, with one careful retry and a fixed deadline. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] | No blanket permission for all schema, identity, privacy, hold or rejection failures. Existing terminal records remain untouched; the actual eligible case requires its own durable authorization. |
| Reason state, child failure and parent terminal | Assignment/manual failure reason codes identify the failing mode-slot operation. The child fail_closed_event is not an RR5 terminal value. [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §9] [04/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md §9] | Resumable/unresolved operations wait for truthful resolution before RR5. Every actual parent invocation still needs its single terminal before acknowledgement. No reason code becomes a new parent-terminal enum. |
| Early stop and closed-episode recording | Values §8 forbids disguising early stop as success or ordinary exhaustion; §§9/16 include recorded early stop among causes that close admission. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §8] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §16] | The clearly_useless/unsafe cause and early-stop event remain explicit even when the episode is recorded closed. No cause is erased by the exhaustion umbrella. |
| Relevance does not produce assignment or gate manual reread | RM-RR-01 evaluates possible new-information reasons. A25 still requires truthful relationships and the assignment producer is not chosen by the relevance declaration. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] | Manual reread remains independent. The actual reread context follows the separate RR2 sequence. No embedding clue alone launches a reread or fills an assignment slot. |

## Explicit remaining scope

- **CH05-e / C-CREATE:** final Writing 1 piece, the unified creation store and its accepted current policy/mechanics.
- **C-7R / CH08-b:** shared relevance vocabulary, full event/disagreement schemas, validators, versions and remaining consumer declarations. RM-RR-01's complete selected content is present here; shared T2-UNRES-SHARED is reused from C-7F.6.10.5.
- **C-7Q / CH08-a and C-LMAC / CH08-c:** full privacy and access-coordination owners. Current reread/retry uses preserve their permission gates without reproducing their state machines.
- **CH10-b / B24:** full messenger, producer and parent/child acceptance mechanism. C-7G.9 already owns the exact careful-retry/fallback consumption seam; this chapter does not duplicate it.
- **C-READ.11:** the existing B16 quarantine-to-production promotion seam. Reread creates a quarantine layer only. Full-cycle promotion and marker-gated production implementation remain outside this chapter.
- **CH11/CH12:** full path assembly and cumulative audit/gap reconciliation. The accepted Bundle 2 foundation source-scope gap from CH05-c remains: its only pinned path is prohibited 99_HISTORICAL_CANDIDATES. No excluded file was opened or reconstructed from receipts.

## Additional undecided implementation slots

| Slot | Value | Boundary / owner |
|---|---|---|
| Operational scheduler/runtime/storage bindings for B9/B10 | NOT DECIDED | Accepted algorithms do not select implementation technology. |
| Final serialization and proposed field naming | NOT DECIDED | Current source names retained as proposed. |
| Source-seam timeouts and cancellation rules beyond existing sources | NOT DECIDED | Retry elapsed bounds never override the source seam. |
| Integrated queue transition for eligible fresh careful retry after terminal failed job | NOT DECIDED | Explicit V10/accepted-design conflict, carried from CH05-b. |
| A25 assignment producer and exact evaluation machinery | NOT DECIDED | Semantic relationships are settled; relevance does not appoint a producer. |
| Reread relevance time-range values | NOT DECIDED | Conditional gate exists; concrete span remains open. |
| Reread retrieval result counts, thresholds and token limits | NOT DECIDED | B1/owning retrieval modes govern structure; no borrowed new-root n=3 default. |
| Full assembled CY-F scheduling and integration | NOT DECIDED | Component designs and use rows do not claim whole-cycle implementation. |
| Retrieval-specific B9/B26 operational integration | NOT DECIDED | Generic retry authority plus stop policy is not an implemented retrieval seam. |
| Foundation-only B26 mechanics unavailable in permitted folders | NOT DECIDED | Accepted identity retained; no claim of undesigned scope. |

## Review of plain gates and empty boxes

Every relationship names its actual connected or owning rule. Action families have explicit rule connections; field identities, literal enum carriers, timestamps and versions do not acquire invented independent failure machinery. B10's seventeen recovery cases, assignment's seven failures/five recoveries, manual compatibility's seven failures/five recoveries, B9's nine duplicate points/nineteen recovery cases, values' six recovery boundaries and fourteen refusal/exhaustion cases are separately visible. The three exact assignment forms and four typed manual distinctions are explicit, as are all accepted numeric bounds and the special later ordinal-1 states.

No canonical state record is conflated with an operational log. Shared recovery events retain one identity. Attempt ID and group ID are reused in nested record structures rather than redefined. Whole-source reading and scoped receipts are distinguished in the read record; no receipt summary substitutes for mechanics. The earlier C-7B.7.1.6 outgoing C-7H stamp is retained as an inherited audit finding: the current root is DESIGNED and its accepted subparts are stamped separately. Earlier bytes remain frozen.

## Appendix A carry-forward — this piece

| Part | Field or cell | Value |
|---|---|---|
| C-7H.1 | Changes | NOT DECIDED |
| C-7H.1.1 | Fails closed by | NOT DECIDED |
| C-7H.1.1 | Fed by | NOT DECIDED |
| C-7H.1.1 | Changes | NOT DECIDED |
| C-7H.1.2 | Fed by | NOT DECIDED |
| C-7H.1.2 | Changes | NOT DECIDED |
| C-7H.1.3 | Fed by | NOT DECIDED |
| C-7H.1.3 | Changes | NOT DECIDED |
| C-7H.1.4 | Fed by | NOT DECIDED |
| C-7H.1.4 | Changes | NOT DECIDED |
| C-7H.2 | Gated by | NOT DECIDED |
| C-7H.2.1 | Gated by | NOT DECIDED |
| C-7H.2.1 | Changes | NOT DECIDED |
| C-7H.2.1.1 | Fails closed by | NOT DECIDED |
| C-7H.2.1.1 | Fed by | NOT DECIDED |
| C-7H.2.1.1 | Gated by | NOT DECIDED |
| C-7H.2.1.1 | Changes | NOT DECIDED |
| C-7H.2.1.2 | Fed by | NOT DECIDED |
| C-7H.2.1.2 | Gated by | NOT DECIDED |
| C-7H.2.1.2 | Changes | NOT DECIDED |
| C-7H.2.1.3 | Must never | NOT DECIDED |
| C-7H.2.1.3 | Fails closed by | NOT DECIDED |
| C-7H.2.1.3 | Fed by | NOT DECIDED |
| C-7H.2.1.3 | Gated by | NOT DECIDED |
| C-7H.2.1.3 | Changes | NOT DECIDED |
| C-7H.2.1.4 | Must never | NOT DECIDED |
| C-7H.2.1.4 | Fails closed by | NOT DECIDED |
| C-7H.2.1.4 | Fed by | NOT DECIDED |
| C-7H.2.1.4 | Gated by | NOT DECIDED |
| C-7H.2.1.4 | Changes | NOT DECIDED |
| C-7H.2.1.5 | Fed by | NOT DECIDED |
| C-7H.2.1.5 | Gated by | NOT DECIDED |
| C-7H.2.1.5 | Changes | NOT DECIDED |
| C-7H.2.1.6 | Must never | NOT DECIDED |
| C-7H.2.1.6 | Fails closed by | NOT DECIDED |
| C-7H.2.1.6 | Fed by | NOT DECIDED |
| C-7H.2.1.6 | Gated by | NOT DECIDED |
| C-7H.2.1.6 | Changes | NOT DECIDED |
| C-7H.2.1.7 | Must never | NOT DECIDED |
| C-7H.2.1.7 | Fails closed by | NOT DECIDED |
| C-7H.2.1.7 | Fed by | NOT DECIDED |
| C-7H.2.1.7 | Gated by | NOT DECIDED |
| C-7H.2.1.7 | Changes | NOT DECIDED |
| C-7H.2.2 | Fed by | NOT DECIDED |
| C-7H.2.2 | Changes | NOT DECIDED |
| C-7H.2.3 | Fed by | NOT DECIDED |
| C-7H.2.3 | Changes | NOT DECIDED |
| C-7H.2.4 | Fed by | NOT DECIDED |
| C-7H.2.4 | Changes | NOT DECIDED |
| C-7H.2.5 | Changes | NOT DECIDED |
| C-7H.2.5.1 | Must never | NOT DECIDED |
| C-7H.2.5.1 | Fails closed by | NOT DECIDED |
| C-7H.2.5.1 | Fed by | NOT DECIDED |
| C-7H.2.5.1 | Gated by | NOT DECIDED |
| C-7H.2.5.1 | Changes | NOT DECIDED |
| C-7H.2.5.2 | Must never | NOT DECIDED |
| C-7H.2.5.2 | Fails closed by | NOT DECIDED |
| C-7H.2.5.2 | Fed by | NOT DECIDED |
| C-7H.2.5.2 | Gated by | NOT DECIDED |
| C-7H.2.5.2 | Changes | NOT DECIDED |
| C-7H.2.5.3 | Fails closed by | NOT DECIDED |
| C-7H.2.5.3 | Fed by | NOT DECIDED |
| C-7H.2.5.3 | Gated by | NOT DECIDED |
| C-7H.2.5.3 | Changes | NOT DECIDED |
| C-7H.2.5.4 | Fails closed by | NOT DECIDED |
| C-7H.2.5.4 | Fed by | NOT DECIDED |
| C-7H.2.5.4 | Gated by | NOT DECIDED |
| C-7H.2.5.4 | Changes | NOT DECIDED |
| C-7H.3.1 | Fed by | NOT DECIDED |
| C-7H.3.1 | Changes | NOT DECIDED |
| C-7H.3.2 | Fed by | NOT DECIDED |
| C-7H.3.2 | Changes | NOT DECIDED |
| C-7H.3.3 | Changes | NOT DECIDED |
| C-7H.3.3.1 | Gated by | NOT DECIDED |
| C-7H.3.3.1 | Changes | NOT DECIDED |
| C-7H.3.4 | Fed by | NOT DECIDED |
| C-7H.3.4 | Changes | NOT DECIDED |
| C-7H.3.5 | Fed by | NOT DECIDED |
| C-7H.3.6 | Fed by | NOT DECIDED |
| C-7H.3.6 | Changes | NOT DECIDED |
| C-7H.3.7 | Fed by | NOT DECIDED |
| C-7H.3.7 | Changes | NOT DECIDED |
| C-7H.4 | Fed by | NOT DECIDED |
| C-7H.4 | Changes | NOT DECIDED |
| C-7H.4.1 | Fails closed by | NOT DECIDED |
| C-7H.4.1 | Fed by | NOT DECIDED |
| C-7H.4.1 | Changes | NOT DECIDED |
| C-7H.4.2 | Fails closed by | NOT DECIDED |
| C-7H.4.2 | Fed by | NOT DECIDED |
| C-7H.4.2 | Changes | NOT DECIDED |
| C-7H.4.3 | Fails closed by | NOT DECIDED |
| C-7H.4.3 | Fed by | NOT DECIDED |
| C-7H.4.3 | Changes | NOT DECIDED |
| C-7H.4.4 | Fails closed by | NOT DECIDED |
| C-7H.4.4 | Fed by | NOT DECIDED |
| C-7H.4.4 | Changes | NOT DECIDED |
| C-7H.4.5 | Fails closed by | NOT DECIDED |
| C-7H.4.5 | Fed by | NOT DECIDED |
| C-7H.4.5 | Changes | NOT DECIDED |
| C-7H.4.6 | Fails closed by | NOT DECIDED |
| C-7H.4.6 | Fed by | NOT DECIDED |
| C-7H.4.6 | Changes | NOT DECIDED |
| C-7H.4.7 | Fails closed by | NOT DECIDED |
| C-7H.4.7 | Fed by | NOT DECIDED |
| C-7H.4.7 | Changes | NOT DECIDED |
| C-7H.4.8 | Fed by | NOT DECIDED |
| C-7H.4.8 | Changes | NOT DECIDED |
| C-7H.5 | Changes | NOT DECIDED |
| C-7H.5.1 | Fails closed by | NOT DECIDED |
| C-7H.5.1 | Fed by | NOT DECIDED |
| C-7H.5.1 | Changes | NOT DECIDED |
| C-7H.5.2 | Fed by | NOT DECIDED |
| C-7H.5.2 | Changes | NOT DECIDED |
| C-7H.5.3 | Fed by | NOT DECIDED |
| C-7H.5.3 | Changes | NOT DECIDED |
| C-7H.5.4 | Fed by | NOT DECIDED |
| C-7H.5.4 | Changes | NOT DECIDED |
| C-7H.5.5 | Fed by | NOT DECIDED |
| C-7H.5.5 | Changes | NOT DECIDED |
| C-7H.5.6 | Fails closed by | NOT DECIDED |
| C-7H.5.6 | Fed by | NOT DECIDED |
| C-7H.5.6 | Changes | NOT DECIDED |
| C-7H.5.7 | Fails closed by | NOT DECIDED |
| C-7H.5.7 | Fed by | NOT DECIDED |
| C-7H.5.7 | Changes | NOT DECIDED |
| C-7H.5.8 | Fed by | NOT DECIDED |
| C-7H.5.8 | Changes | NOT DECIDED |
| C-7H.5.9 | Fed by | NOT DECIDED |
| C-7H.5.9 | Changes | NOT DECIDED |
| C-7H.5.10 | Fed by | NOT DECIDED |
| C-7H.5.10 | Changes | NOT DECIDED |
| C-7H.5.11 | Fed by | NOT DECIDED |
| C-7H.5.11 | Changes | NOT DECIDED |
| C-7H.5.12 | Fed by | NOT DECIDED |
| C-7H.5.12 | Changes | NOT DECIDED |
| C-7H.5.13 | Fed by | NOT DECIDED |
| C-7H.5.13 | Changes | NOT DECIDED |
| C-7H.5.14 | Fed by | NOT DECIDED |
| C-7H.5.14 | Changes | NOT DECIDED |
| C-7H.5.15 | Fed by | NOT DECIDED |
| C-7H.5.15 | Changes | NOT DECIDED |
| C-7H.5.16 | Fails closed by | NOT DECIDED |
| C-7H.5.16 | Fed by | NOT DECIDED |
| C-7H.5.16 | Changes | NOT DECIDED |
| C-7H.5.17 | Fed by | NOT DECIDED |
| C-7H.5.17 | Changes | NOT DECIDED |
| C-7H.6 | Fed by | NOT DECIDED |
| C-7H.6.1 | Fails closed by | NOT DECIDED |
| C-7H.6.1 | Fed by | NOT DECIDED |
| C-7H.6.1 | Changes | NOT DECIDED |
| C-7H.6.2 | Fails closed by | NOT DECIDED |
| C-7H.6.2 | Fed by | NOT DECIDED |
| C-7H.6.2 | Gated by | NOT DECIDED |
| C-7H.6.2.1 | Fails closed by | NOT DECIDED |
| C-7H.6.2.1 | Fed by | NOT DECIDED |
| C-7H.6.2.1 | Changes | NOT DECIDED |
| C-7H.6.2.2 | Fails closed by | NOT DECIDED |
| C-7H.6.2.2 | Fed by | NOT DECIDED |
| C-7H.6.2.2 | Changes | NOT DECIDED |
| C-7H.6.3 | Fails closed by | NOT DECIDED |
| C-7H.6.3 | Fed by | NOT DECIDED |
| C-7H.6.3 | Changes | NOT DECIDED |
| C-7H.6.4 | Fails closed by | NOT DECIDED |
| C-7H.6.4 | Fed by | NOT DECIDED |
| C-7H.6.4 | Changes | NOT DECIDED |
| C-7H.6.5 | Fails closed by | NOT DECIDED |
| C-7H.6.5 | Fed by | NOT DECIDED |
| C-7H.6.5 | Changes | NOT DECIDED |
| C-7H.6.6 | Fed by | NOT DECIDED |
| C-7H.6.6 | Changes | NOT DECIDED |
| C-7H.6.7 | Fed by | NOT DECIDED |
| C-7H.6.7 | Gated by | NOT DECIDED |
| C-7H.6.7.1 | Fails closed by | NOT DECIDED |
| C-7H.6.7.1 | Fed by | NOT DECIDED |
| C-7H.6.7.1 | Changes | NOT DECIDED |
| C-7H.6.7.2 | Fails closed by | NOT DECIDED |
| C-7H.6.7.2 | Fed by | NOT DECIDED |
| C-7H.6.7.2 | Changes | NOT DECIDED |
| C-7H.6.7.3 | Fed by | NOT DECIDED |
| C-7H.6.7.3 | Changes | NOT DECIDED |
| C-7H.7.1 | Fails closed by | NOT DECIDED |
| C-7H.7.1 | Fed by | NOT DECIDED |
| C-7H.7.1 | Changes | NOT DECIDED |
| C-7H.7.2 | Fails closed by | NOT DECIDED |
| C-7H.7.2 | Fed by | NOT DECIDED |
| C-7H.7.2 | Changes | NOT DECIDED |
| C-7H.7.3 | Fed by | NOT DECIDED |
| C-7H.7.3 | Changes | NOT DECIDED |
| C-7H.7.4 | Gated by | NOT DECIDED |
| C-7H.7.4 | Changes | NOT DECIDED |
| C-7H.7.4.1 | Must never | NOT DECIDED |
| C-7H.7.4.1 | Fails closed by | NOT DECIDED |
| C-7H.7.4.1 | Fed by | NOT DECIDED |
| C-7H.7.4.1 | Gated by | NOT DECIDED |
| C-7H.7.4.1 | Changes | NOT DECIDED |
| C-7H.7.4.2 | Fed by | NOT DECIDED |
| C-7H.7.4.2 | Gated by | NOT DECIDED |
| C-7H.7.4.2 | Changes | NOT DECIDED |
| C-7H.7.4.3 | Fed by | NOT DECIDED |
| C-7H.7.4.3 | Gated by | NOT DECIDED |
| C-7H.7.4.3 | Changes | NOT DECIDED |
| C-7H.7.4.4 | Fed by | NOT DECIDED |
| C-7H.7.4.4 | Gated by | NOT DECIDED |
| C-7H.7.4.4 | Changes | NOT DECIDED |
| C-7H.7.4.5 | Fed by | NOT DECIDED |
| C-7H.7.4.5 | Gated by | NOT DECIDED |
| C-7H.7.4.5 | Changes | NOT DECIDED |
| C-7H.7.4.6 | Fed by | NOT DECIDED |
| C-7H.7.4.6 | Gated by | NOT DECIDED |
| C-7H.7.4.6 | Changes | NOT DECIDED |
| C-7H.7.4.7 | Must never | NOT DECIDED |
| C-7H.7.4.7 | Fails closed by | NOT DECIDED |
| C-7H.7.4.7 | Fed by | NOT DECIDED |
| C-7H.7.4.7 | Gated by | NOT DECIDED |
| C-7H.7.4.7 | Changes | NOT DECIDED |
| C-7H.7.4.8 | Must never | NOT DECIDED |
| C-7H.7.4.8 | Fails closed by | NOT DECIDED |
| C-7H.7.4.8 | Fed by | NOT DECIDED |
| C-7H.7.4.8 | Gated by | NOT DECIDED |
| C-7H.7.4.8 | Changes | NOT DECIDED |
| C-7H.7.5 | Fed by | NOT DECIDED |
| C-7H.7.5 | Changes | NOT DECIDED |
| C-7H.7.6 | Fed by | NOT DECIDED |
| C-7H.7.6 | Changes | NOT DECIDED |
| C-7H.7.7 | Fed by | NOT DECIDED |
| C-7H.7.7 | Changes | NOT DECIDED |
| C-7H.7.7.1 | Fed by | NOT DECIDED |
| C-7H.7.7.1 | Changes | NOT DECIDED |
| C-7H.7.7.2 | Fed by | NOT DECIDED |
| C-7H.7.7.2 | Changes | NOT DECIDED |
| C-7H.7.7.3 | Fed by | NOT DECIDED |
| C-7H.7.7.3 | Changes | NOT DECIDED |
| C-7H.7.7.4 | Fed by | NOT DECIDED |
| C-7H.7.7.4 | Changes | NOT DECIDED |
| C-7H.7.7.5 | Fed by | NOT DECIDED |
| C-7H.7.7.5 | Changes | NOT DECIDED |
| C-7H.7.7.6 | Fed by | NOT DECIDED |
| C-7H.7.7.6 | Changes | NOT DECIDED |
| C-7H.7.7.7 | Fed by | NOT DECIDED |
| C-7H.7.7.7 | Changes | NOT DECIDED |
| C-7H.7.8 | Changes | NOT DECIDED |
| C-7H.7.8.1 | Fed by | NOT DECIDED |
| C-7H.7.8.1 | Changes | NOT DECIDED |
| C-7H.7.8.2 | Fed by | NOT DECIDED |
| C-7H.7.8.2 | Changes | NOT DECIDED |
| C-7H.7.8.3 | Fails closed by | NOT DECIDED |
| C-7H.7.8.3 | Fed by | NOT DECIDED |
| C-7H.7.8.3 | Changes | NOT DECIDED |
| C-7H.7.8.4 | Fed by | NOT DECIDED |
| C-7H.7.8.4 | Changes | NOT DECIDED |
| C-7H.7.8.5 | Changes | NOT DECIDED |
| C-7H.8.1 | Changes | NOT DECIDED |
| C-7H.8.1.1 | Must never | NOT DECIDED |
| C-7H.8.1.1 | Fails closed by | NOT DECIDED |
| C-7H.8.1.1 | Fed by | NOT DECIDED |
| C-7H.8.1.1 | Gated by | NOT DECIDED |
| C-7H.8.1.1 | Changes | NOT DECIDED |
| C-7H.8.1.2 | Fed by | NOT DECIDED |
| C-7H.8.1.2 | Gated by | NOT DECIDED |
| C-7H.8.1.2 | Changes | NOT DECIDED |
| C-7H.8.1.3 | Fed by | NOT DECIDED |
| C-7H.8.1.3 | Gated by | NOT DECIDED |
| C-7H.8.1.3 | Changes | NOT DECIDED |
| C-7H.8.1.4 | Fed by | NOT DECIDED |
| C-7H.8.1.4 | Gated by | NOT DECIDED |
| C-7H.8.1.4 | Changes | NOT DECIDED |
| C-7H.8.1.5 | Fails closed by | NOT DECIDED |
| C-7H.8.1.5 | Fed by | NOT DECIDED |
| C-7H.8.1.5 | Gated by | NOT DECIDED |
| C-7H.8.1.5 | Changes | NOT DECIDED |
| C-7H.8.1.6 | Fails closed by | NOT DECIDED |
| C-7H.8.1.6 | Fed by | NOT DECIDED |
| C-7H.8.1.6 | Gated by | NOT DECIDED |
| C-7H.8.1.6 | Changes | NOT DECIDED |
| C-7H.8.1.7 | Must never | NOT DECIDED |
| C-7H.8.1.7 | Fails closed by | NOT DECIDED |
| C-7H.8.1.7 | Fed by | NOT DECIDED |
| C-7H.8.1.7 | Gated by | NOT DECIDED |
| C-7H.8.1.7 | Changes | NOT DECIDED |
| C-7H.8.1.8 | Must never | NOT DECIDED |
| C-7H.8.1.8 | Fails closed by | NOT DECIDED |
| C-7H.8.1.8 | Fed by | NOT DECIDED |
| C-7H.8.1.8 | Gated by | NOT DECIDED |
| C-7H.8.1.8 | Changes | NOT DECIDED |
| C-7H.8.2 | Fed by | NOT DECIDED |
| C-7H.8.2 | Changes | NOT DECIDED |
| C-7H.8.3 | Fed by | NOT DECIDED |
| C-7H.8.3 | Changes | NOT DECIDED |
| C-7H.8.4 | Fed by | NOT DECIDED |
| C-7H.8.4 | Changes | NOT DECIDED |
| C-7H.8.5 | Fed by | NOT DECIDED |
| C-7H.8.5 | Changes | NOT DECIDED |
| C-7H.8.5.1 | Fed by | NOT DECIDED |
| C-7H.8.5.1 | Changes | NOT DECIDED |
| C-7H.8.5.2 | Fed by | NOT DECIDED |
| C-7H.8.5.2 | Changes | NOT DECIDED |
| C-7H.8.5.3 | Fed by | NOT DECIDED |
| C-7H.8.5.3 | Changes | NOT DECIDED |
| C-7H.8.5.4 | Fed by | NOT DECIDED |
| C-7H.8.5.4 | Changes | NOT DECIDED |
| C-7H.8.5.5 | Fed by | NOT DECIDED |
| C-7H.8.5.5 | Changes | NOT DECIDED |
| C-7H.8.5.6 | Fed by | NOT DECIDED |
| C-7H.8.5.6 | Changes | NOT DECIDED |
| C-7H.8.5.7 | Fed by | NOT DECIDED |
| C-7H.8.5.7 | Changes | NOT DECIDED |
| C-7H.8.6 | Changes | NOT DECIDED |
| C-7H.8.6.1 | Fed by | NOT DECIDED |
| C-7H.8.6.1 | Changes | NOT DECIDED |
| C-7H.8.6.2 | Fed by | NOT DECIDED |
| C-7H.8.6.2 | Changes | NOT DECIDED |
| C-7H.8.6.3 | Fails closed by | NOT DECIDED |
| C-7H.8.6.3 | Fed by | NOT DECIDED |
| C-7H.8.6.3 | Changes | NOT DECIDED |
| C-7H.8.6.4 | Fed by | NOT DECIDED |
| C-7H.8.6.4 | Changes | NOT DECIDED |
| C-7H.8.6.5 | Fails closed by | NOT DECIDED |
| C-7H.8.6.5 | Fed by | NOT DECIDED |
| C-7H.8.6.5 | Changes | NOT DECIDED |
| C-7H.8.7 | Fed by | NOT DECIDED |
| C-7H.9.1 | Changes | NOT DECIDED |
| C-7H.9.1.1 | Fed by | NOT DECIDED |
| C-7H.9.1.1 | Gated by | NOT DECIDED |
| C-7H.9.1.1 | Changes | NOT DECIDED |
| C-7H.9.1.2 | Fed by | NOT DECIDED |
| C-7H.9.1.2 | Gated by | NOT DECIDED |
| C-7H.9.1.2 | Changes | NOT DECIDED |
| C-7H.9.1.3 | Fed by | NOT DECIDED |
| C-7H.9.1.3 | Gated by | NOT DECIDED |
| C-7H.9.1.3 | Changes | NOT DECIDED |
| C-7H.9.1.4 | Fed by | NOT DECIDED |
| C-7H.9.1.4 | Gated by | NOT DECIDED |
| C-7H.9.1.4 | Changes | NOT DECIDED |
| C-7H.9.1.5 | Fed by | NOT DECIDED |
| C-7H.9.1.5 | Gated by | NOT DECIDED |
| C-7H.9.1.5 | Changes | NOT DECIDED |
| C-7H.9.1.6 | Fed by | NOT DECIDED |
| C-7H.9.1.6 | Gated by | NOT DECIDED |
| C-7H.9.1.6 | Changes | NOT DECIDED |
| C-7H.9.2 | Changes | NOT DECIDED |
| C-7H.9.2.1 | Fed by | NOT DECIDED |
| C-7H.9.2.1 | Changes | NOT DECIDED |
| C-7H.9.2.2 | Fed by | NOT DECIDED |
| C-7H.9.2.2 | Changes | NOT DECIDED |
| C-7H.9.2.3 | Fed by | NOT DECIDED |
| C-7H.9.2.3 | Changes | NOT DECIDED |
| C-7H.9.3.1 | Fails closed by | NOT DECIDED |
| C-7H.9.3.1 | Fed by | NOT DECIDED |
| C-7H.9.3.1 | Gated by | NOT DECIDED |
| C-7H.9.3.1 | Changes | NOT DECIDED |
| C-7H.9.3.2 | Fails closed by | NOT DECIDED |
| C-7H.9.3.2 | Fed by | NOT DECIDED |
| C-7H.9.3.2 | Gated by | NOT DECIDED |
| C-7H.9.3.2 | Changes | NOT DECIDED |
| C-7H.9.3.3 | Fed by | NOT DECIDED |
| C-7H.9.3.3 | Gated by | NOT DECIDED |
| C-7H.9.3.3 | Changes | NOT DECIDED |
| C-7H.9.3.4 | Gated by | NOT DECIDED |
| C-7H.9.3.4.1 | Fails closed by | NOT DECIDED |
| C-7H.9.3.4.1 | Fed by | NOT DECIDED |
| C-7H.9.3.4.1 | Gated by | NOT DECIDED |
| C-7H.9.3.4.1 | Changes | NOT DECIDED |
| C-7H.9.3.4.2 | Fed by | NOT DECIDED |
| C-7H.9.3.4.2 | Gated by | NOT DECIDED |
| C-7H.9.3.4.2 | Changes | NOT DECIDED |
| C-7H.9.3.4.3 | Changes | NOT DECIDED |
| C-7H.9.3.4.3.1 | Must never | NOT DECIDED |
| C-7H.9.3.4.3.1 | Fails closed by | NOT DECIDED |
| C-7H.9.3.4.3.1 | Fed by | NOT DECIDED |
| C-7H.9.3.4.3.1 | Gated by | NOT DECIDED |
| C-7H.9.3.4.3.1 | Changes | NOT DECIDED |
| C-7H.9.3.4.3.2 | Fed by | NOT DECIDED |
| C-7H.9.3.4.3.2 | Gated by | NOT DECIDED |
| C-7H.9.3.4.3.2 | Changes | NOT DECIDED |
| C-7H.9.3.4.3.3 | Fails closed by | NOT DECIDED |
| C-7H.9.3.4.3.3 | Fed by | NOT DECIDED |
| C-7H.9.3.4.3.3 | Changes | NOT DECIDED |
| C-7H.9.3.4.3.4 | Fed by | NOT DECIDED |
| C-7H.9.3.4.3.4 | Gated by | NOT DECIDED |
| C-7H.9.3.4.3.4 | Changes | NOT DECIDED |
| C-7H.9.3.4.3.5 | Fed by | NOT DECIDED |
| C-7H.9.3.4.3.5 | Gated by | NOT DECIDED |
| C-7H.9.3.4.3.5 | Changes | NOT DECIDED |
| C-7H.9.3.4.4 | Fed by | NOT DECIDED |
| C-7H.9.3.4.4 | Gated by | NOT DECIDED |
| C-7H.9.3.4.4 | Changes | NOT DECIDED |
| C-7H.9.3.5 | Fed by | NOT DECIDED |
| C-7H.9.3.5 | Gated by | NOT DECIDED |
| C-7H.9.3.5 | Changes | NOT DECIDED |
| C-7H.9.3.6 | Fed by | NOT DECIDED |
| C-7H.9.3.6 | Gated by | NOT DECIDED |
| C-7H.9.3.6 | Changes | NOT DECIDED |
| C-7H.9.3.7 | Fed by | NOT DECIDED |
| C-7H.9.3.7 | Gated by | NOT DECIDED |
| C-7H.9.3.7 | Changes | NOT DECIDED |
| C-7H.9.4.1 | Fed by | NOT DECIDED |
| C-7H.9.4.1 | Changes | NOT DECIDED |
| C-7H.9.4.2 | Fed by | NOT DECIDED |
| C-7H.9.4.2 | Changes | NOT DECIDED |
| C-7H.9.4.3 | Fed by | NOT DECIDED |
| C-7H.9.4.3 | Changes | NOT DECIDED |
| C-7H.9.4.4 | Fed by | NOT DECIDED |
| C-7H.9.4.4 | Changes | NOT DECIDED |
| C-7H.9.4.5 | Fed by | NOT DECIDED |
| C-7H.9.4.5 | Changes | NOT DECIDED |
| C-7H.9.5 | Fed by | NOT DECIDED |
| C-7H.9.5 | Changes | NOT DECIDED |
| C-7H.9.5.1 | Fails closed by | NOT DECIDED |
| C-7H.9.5.1 | Fed by | NOT DECIDED |
| C-7H.9.5.1 | Changes | NOT DECIDED |
| C-7H.9.5.2 | Fed by | NOT DECIDED |
| C-7H.9.5.2 | Changes | NOT DECIDED |
| C-7H.9.5.3 | Fed by | NOT DECIDED |
| C-7H.9.5.3 | Changes | NOT DECIDED |
| C-7H.9.5.4 | Fed by | NOT DECIDED |
| C-7H.9.5.4 | Changes | NOT DECIDED |
| C-7H.9.5.5 | Fed by | NOT DECIDED |
| C-7H.9.5.5 | Changes | NOT DECIDED |
| C-7H.9.5.6 | Fed by | NOT DECIDED |
| C-7H.9.5.6 | Changes | NOT DECIDED |
| C-7H.9.5.7 | Fed by | NOT DECIDED |
| C-7H.9.5.7 | Changes | NOT DECIDED |
| C-7H.9.5.8 | Fails closed by | NOT DECIDED |
| C-7H.9.5.8 | Fed by | NOT DECIDED |
| C-7H.9.5.8 | Changes | NOT DECIDED |
| C-7H.9.5.9 | Fed by | NOT DECIDED |
| C-7H.9.5.9 | Changes | NOT DECIDED |
| C-7H.9.6 | Changes | NOT DECIDED |
| C-7H.9.6.1 | Fails closed by | NOT DECIDED |
| C-7H.9.6.1 | Fed by | NOT DECIDED |
| C-7H.9.6.1 | Changes | NOT DECIDED |
| C-7H.9.6.2 | Fed by | NOT DECIDED |
| C-7H.9.6.2 | Changes | NOT DECIDED |
| C-7H.9.6.3 | Fed by | NOT DECIDED |
| C-7H.9.6.3 | Changes | NOT DECIDED |
| C-7H.9.6.4 | Fed by | NOT DECIDED |
| C-7H.9.6.4 | Changes | NOT DECIDED |
| C-7H.9.6.5 | Fails closed by | NOT DECIDED |
| C-7H.9.6.5 | Fed by | NOT DECIDED |
| C-7H.9.6.5 | Changes | NOT DECIDED |
| C-7H.9.6.6 | Fed by | NOT DECIDED |
| C-7H.9.6.6 | Changes | NOT DECIDED |
| C-7H.9.6.7 | Fed by | NOT DECIDED |
| C-7H.9.6.7 | Changes | NOT DECIDED |
| C-7H.9.6.8 | Fed by | NOT DECIDED |
| C-7H.9.6.8 | Changes | NOT DECIDED |
| C-7H.9.6.9 | Fed by | NOT DECIDED |
| C-7H.9.6.9 | Changes | NOT DECIDED |
| C-7H.9.6.10 | Fed by | NOT DECIDED |
| C-7H.9.6.10 | Changes | NOT DECIDED |
| C-7H.9.6.11 | Fed by | NOT DECIDED |
| C-7H.9.6.11 | Changes | NOT DECIDED |
| C-7H.9.6.12 | Fed by | NOT DECIDED |
| C-7H.9.6.12 | Changes | NOT DECIDED |
| C-7H.9.6.13 | Fed by | NOT DECIDED |
| C-7H.9.6.13 | Changes | NOT DECIDED |
| C-7H.9.6.14 | Fed by | NOT DECIDED |
| C-7H.9.6.14 | Changes | NOT DECIDED |
| C-7H.9.6.15 | Fed by | NOT DECIDED |
| C-7H.9.6.15 | Changes | NOT DECIDED |
| C-7H.9.6.16 | Fed by | NOT DECIDED |
| C-7H.9.6.16 | Changes | NOT DECIDED |
| C-7H.9.6.17 | Fed by | NOT DECIDED |
| C-7H.9.6.17 | Changes | NOT DECIDED |
| C-7H.9.6.18 | Fails closed by | NOT DECIDED |
| C-7H.9.6.18 | Fed by | NOT DECIDED |
| C-7H.9.6.18 | Changes | NOT DECIDED |
| C-7H.9.6.19 | Fed by | NOT DECIDED |
| C-7H.9.6.19 | Changes | NOT DECIDED |
| C-7H.9.7 | Fed by | NOT DECIDED |
| C-7H.9.7.1 | Fails closed by | NOT DECIDED |
| C-7H.9.7.1 | Fed by | NOT DECIDED |
| C-7H.9.7.1 | Changes | NOT DECIDED |
| C-7H.9.7.2 | Fails closed by | NOT DECIDED |
| C-7H.9.7.2 | Fed by | NOT DECIDED |
| C-7H.9.7.2 | Changes | NOT DECIDED |
| C-7H.9.7.3 | Fed by | NOT DECIDED |
| C-7H.9.7.3 | Changes | NOT DECIDED |
| C-7H.9.7.4 | Fails closed by | NOT DECIDED |
| C-7H.9.7.4 | Fed by | NOT DECIDED |
| C-7H.9.7.4 | Changes | NOT DECIDED |
| C-7H.9.7.5 | Fails closed by | NOT DECIDED |
| C-7H.9.7.5 | Fed by | NOT DECIDED |
| C-7H.9.7.5 | Changes | NOT DECIDED |
| C-7H.9.7.6 | Fails closed by | NOT DECIDED |
| C-7H.9.7.6 | Fed by | NOT DECIDED |
| C-7H.9.7.6 | Changes | NOT DECIDED |
| C-7H.9.7.7 | Fed by | NOT DECIDED |
| C-7H.9.7.7 | Changes | NOT DECIDED |
| C-7H.10.1 | Changes | NOT DECIDED |
| C-7H.10.1.1 | Must never | NOT DECIDED |
| C-7H.10.1.1 | Fails closed by | NOT DECIDED |
| C-7H.10.1.1 | Fed by | NOT DECIDED |
| C-7H.10.1.1 | Gated by | NOT DECIDED |
| C-7H.10.1.1 | Changes | NOT DECIDED |
| C-7H.10.1.2 | Fed by | NOT DECIDED |
| C-7H.10.1.2 | Gated by | NOT DECIDED |
| C-7H.10.1.2 | Changes | NOT DECIDED |
| C-7H.10.1.3 | Must never | NOT DECIDED |
| C-7H.10.1.3 | Fails closed by | NOT DECIDED |
| C-7H.10.1.3 | Fed by | NOT DECIDED |
| C-7H.10.1.3 | Gated by | NOT DECIDED |
| C-7H.10.1.3 | Changes | NOT DECIDED |
| C-7H.10.1.4 | Fed by | NOT DECIDED |
| C-7H.10.1.4 | Gated by | NOT DECIDED |
| C-7H.10.1.4 | Changes | NOT DECIDED |
| C-7H.10.1.5 | Fed by | NOT DECIDED |
| C-7H.10.1.5 | Gated by | NOT DECIDED |
| C-7H.10.1.5 | Changes | NOT DECIDED |
| C-7H.10.1.6 | Fed by | NOT DECIDED |
| C-7H.10.1.6 | Gated by | NOT DECIDED |
| C-7H.10.1.6 | Changes | NOT DECIDED |
| C-7H.10.1.7 | Fed by | NOT DECIDED |
| C-7H.10.1.7 | Gated by | NOT DECIDED |
| C-7H.10.1.7 | Changes | NOT DECIDED |
| C-7H.10.1.8 | Fed by | NOT DECIDED |
| C-7H.10.1.8 | Gated by | NOT DECIDED |
| C-7H.10.1.8 | Changes | NOT DECIDED |
| C-7H.10.1.9 | Fed by | NOT DECIDED |
| C-7H.10.1.9 | Gated by | NOT DECIDED |
| C-7H.10.1.9 | Changes | NOT DECIDED |
| C-7H.10.1.10 | Fed by | NOT DECIDED |
| C-7H.10.1.10 | Gated by | NOT DECIDED |
| C-7H.10.1.10 | Changes | NOT DECIDED |
| C-7H.10.1.11 | Fed by | NOT DECIDED |
| C-7H.10.1.11 | Gated by | NOT DECIDED |
| C-7H.10.1.11 | Changes | NOT DECIDED |
| C-7H.10.1.12 | Fed by | NOT DECIDED |
| C-7H.10.1.12 | Gated by | NOT DECIDED |
| C-7H.10.1.12 | Changes | NOT DECIDED |
| C-7H.10.1.13 | Fed by | NOT DECIDED |
| C-7H.10.1.13 | Gated by | NOT DECIDED |
| C-7H.10.1.13 | Changes | NOT DECIDED |
| C-7H.10.1.14 | Fed by | NOT DECIDED |
| C-7H.10.1.14 | Gated by | NOT DECIDED |
| C-7H.10.1.14 | Changes | NOT DECIDED |
| C-7H.10.2 | Changes | NOT DECIDED |
| C-7H.10.2.1 | Fed by | NOT DECIDED |
| C-7H.10.2.1 | Gated by | NOT DECIDED |
| C-7H.10.2.1 | Changes | NOT DECIDED |
| C-7H.10.2.2 | Fed by | NOT DECIDED |
| C-7H.10.2.2 | Gated by | NOT DECIDED |
| C-7H.10.2.2 | Changes | NOT DECIDED |
| C-7H.10.2.3 | Fed by | NOT DECIDED |
| C-7H.10.2.3 | Changes | NOT DECIDED |
| C-7H.10.2.4 | Fed by | NOT DECIDED |
| C-7H.10.2.4 | Changes | NOT DECIDED |
| C-7H.10.2.5 | Fed by | NOT DECIDED |
| C-7H.10.2.5 | Changes | NOT DECIDED |
| C-7H.10.2.6 | Fed by | NOT DECIDED |
| C-7H.10.2.6 | Changes | NOT DECIDED |
| C-7H.10.3 | Changes | NOT DECIDED |
| C-7H.10.3.1 | Fed by | NOT DECIDED |
| C-7H.10.3.1 | Gated by | NOT DECIDED |
| C-7H.10.3.1 | Changes | NOT DECIDED |
| C-7H.10.3.2 | Fed by | NOT DECIDED |
| C-7H.10.3.2 | Gated by | NOT DECIDED |
| C-7H.10.3.2 | Changes | NOT DECIDED |
| C-7H.10.3.3 | Fed by | NOT DECIDED |
| C-7H.10.3.3 | Gated by | NOT DECIDED |
| C-7H.10.3.3 | Changes | NOT DECIDED |
| C-7H.10.3.4 | Fed by | NOT DECIDED |
| C-7H.10.3.4 | Changes | NOT DECIDED |
| C-7H.10.4 | Fed by | NOT DECIDED |
| C-7H.10.4 | Changes | NOT DECIDED |
| C-7H.10.4.1 | Fed by | NOT DECIDED |
| C-7H.10.4.1 | Changes | NOT DECIDED |
| C-7H.10.4.2 | Fed by | NOT DECIDED |
| C-7H.10.4.2 | Changes | NOT DECIDED |
| C-7H.10.4.3 | Fed by | NOT DECIDED |
| C-7H.10.4.3 | Changes | NOT DECIDED |
| C-7H.10.4.4 | Fed by | NOT DECIDED |
| C-7H.10.4.4 | Changes | NOT DECIDED |
| C-7H.10.4.5 | Fed by | NOT DECIDED |
| C-7H.10.4.5 | Changes | NOT DECIDED |
| C-7H.10.4.6 | Fed by | NOT DECIDED |
| C-7H.10.4.6 | Changes | NOT DECIDED |
| C-7H.10.4.7 | Fed by | NOT DECIDED |
| C-7H.10.4.7 | Changes | NOT DECIDED |
| C-7H.10.4.8 | Fed by | NOT DECIDED |
| C-7H.10.4.8 | Changes | NOT DECIDED |
| C-7H.10.5 | Changes | NOT DECIDED |
| C-7H.10.5.1 | Fails closed by | NOT DECIDED |
| C-7H.10.5.1 | Fed by | NOT DECIDED |
| C-7H.10.5.1 | Gated by | NOT DECIDED |
| C-7H.10.5.1 | Changes | NOT DECIDED |
| C-7H.10.5.2 | Fails closed by | NOT DECIDED |
| C-7H.10.5.2 | Fed by | NOT DECIDED |
| C-7H.10.5.2 | Gated by | NOT DECIDED |
| C-7H.10.5.2 | Changes | NOT DECIDED |
| C-7H.10.5.3 | Fed by | NOT DECIDED |
| C-7H.10.5.3 | Changes | NOT DECIDED |
| C-7H.10.5.4 | Fed by | NOT DECIDED |
| C-7H.10.5.4 | Changes | NOT DECIDED |
| C-7H.10.5.5 | Fed by | NOT DECIDED |
| C-7H.10.5.5 | Changes | NOT DECIDED |
| C-7H.10.6 | Fed by | NOT DECIDED |
| C-7H.10.6 | Changes | NOT DECIDED |
| C-7H.10.7 | Fed by | NOT DECIDED |
| C-7H.10.7 | Changes | NOT DECIDED |
| C-7H.10.8 | Fed by | NOT DECIDED |
| C-7H.10.8 | Changes | NOT DECIDED |
| C-7H.10.9.1 | Gated by | NOT DECIDED |
| C-7H.10.9.1 | Changes | NOT DECIDED |
| C-7H.10.9.1.1 | Fails closed by | NOT DECIDED |
| C-7H.10.9.1.1 | Fed by | NOT DECIDED |
| C-7H.10.9.1.1 | Gated by | NOT DECIDED |
| C-7H.10.9.1.1 | Changes | NOT DECIDED |
| C-7H.10.9.1.2 | Fed by | NOT DECIDED |
| C-7H.10.9.1.2 | Gated by | NOT DECIDED |
| C-7H.10.9.1.2 | Changes | NOT DECIDED |
| C-7H.10.9.1.3 | Fed by | NOT DECIDED |
| C-7H.10.9.1.3 | Gated by | NOT DECIDED |
| C-7H.10.9.1.3 | Changes | NOT DECIDED |
| C-7H.10.9.1.4 | Fed by | NOT DECIDED |
| C-7H.10.9.1.4 | Gated by | NOT DECIDED |
| C-7H.10.9.1.4 | Changes | NOT DECIDED |
| C-7H.10.9.1.5 | Fails closed by | NOT DECIDED |
| C-7H.10.9.1.5 | Fed by | NOT DECIDED |
| C-7H.10.9.1.5 | Gated by | NOT DECIDED |
| C-7H.10.9.1.5 | Changes | NOT DECIDED |
| C-7H.10.9.1.6 | Must never | NOT DECIDED |
| C-7H.10.9.1.6 | Fails closed by | NOT DECIDED |
| C-7H.10.9.1.6 | Fed by | NOT DECIDED |
| C-7H.10.9.1.6 | Gated by | NOT DECIDED |
| C-7H.10.9.1.6 | Changes | NOT DECIDED |
| C-7H.10.9.1.7 | Must never | NOT DECIDED |
| C-7H.10.9.1.7 | Fails closed by | NOT DECIDED |
| C-7H.10.9.1.7 | Fed by | NOT DECIDED |
| C-7H.10.9.1.7 | Gated by | NOT DECIDED |
| C-7H.10.9.1.7 | Changes | NOT DECIDED |
| C-7H.10.9.2 | Gated by | NOT DECIDED |
| C-7H.10.9.2 | Changes | NOT DECIDED |
| C-7H.10.9.2.1 | Must never | NOT DECIDED |
| C-7H.10.9.2.1 | Fails closed by | NOT DECIDED |
| C-7H.10.9.2.1 | Fed by | NOT DECIDED |
| C-7H.10.9.2.1 | Gated by | NOT DECIDED |
| C-7H.10.9.2.1 | Changes | NOT DECIDED |
| C-7H.10.9.2.2 | Fails closed by | NOT DECIDED |
| C-7H.10.9.2.2 | Fed by | NOT DECIDED |
| C-7H.10.9.2.2 | Gated by | NOT DECIDED |
| C-7H.10.9.2.2 | Changes | NOT DECIDED |
| C-7H.10.9.2.3 | Fed by | NOT DECIDED |
| C-7H.10.9.2.3 | Gated by | NOT DECIDED |
| C-7H.10.9.2.3 | Changes | NOT DECIDED |
| C-7H.10.9.2.4 | Fed by | NOT DECIDED |
| C-7H.10.9.2.4 | Gated by | NOT DECIDED |
| C-7H.10.9.2.4 | Changes | NOT DECIDED |
| C-7H.10.9.2.5 | Must never | NOT DECIDED |
| C-7H.10.9.2.5 | Fails closed by | NOT DECIDED |
| C-7H.10.9.2.5 | Fed by | NOT DECIDED |
| C-7H.10.9.2.5 | Gated by | NOT DECIDED |
| C-7H.10.9.2.5 | Changes | NOT DECIDED |
| C-7H.10.9.2.6 | Must never | NOT DECIDED |
| C-7H.10.9.2.6 | Fails closed by | NOT DECIDED |
| C-7H.10.9.2.6 | Fed by | NOT DECIDED |
| C-7H.10.9.2.6 | Gated by | NOT DECIDED |
| C-7H.10.9.2.6 | Changes | NOT DECIDED |
| C-7H.10.9.3 | Fed by | NOT DECIDED |
| C-7H.10.9.3 | Changes | NOT DECIDED |
| C-7H.10.9.4 | Changes | NOT DECIDED |
| C-7H.10.9.4.1 | Fed by | NOT DECIDED |
| C-7H.10.9.4.1 | Gated by | NOT DECIDED |
| C-7H.10.9.4.1 | Changes | NOT DECIDED |
| C-7H.10.9.4.2 | Fails closed by | NOT DECIDED |
| C-7H.10.9.4.2 | Fed by | NOT DECIDED |
| C-7H.10.9.4.2 | Gated by | NOT DECIDED |
| C-7H.10.9.4.2 | Changes | NOT DECIDED |
| C-7H.10.9.4.3 | Fed by | NOT DECIDED |
| C-7H.10.9.4.3 | Gated by | NOT DECIDED |
| C-7H.10.9.4.3 | Changes | NOT DECIDED |
| C-7H.10.9.5 | Fed by | NOT DECIDED |
| C-7H.10.9.5 | Changes | NOT DECIDED |
| C-7H.10.10 | Fed by | NOT DECIDED |
| C-7H.10.10 | Changes | NOT DECIDED |
| C-7H.10.10.1 | Fed by | NOT DECIDED |
| C-7H.10.10.1 | Changes | NOT DECIDED |
| C-7H.10.10.2 | Fed by | NOT DECIDED |
| C-7H.10.10.2 | Changes | NOT DECIDED |
| C-7H.10.10.3 | Fed by | NOT DECIDED |
| C-7H.10.10.3 | Changes | NOT DECIDED |
| C-7H.10.10.4 | Fed by | NOT DECIDED |
| C-7H.10.10.4 | Changes | NOT DECIDED |
| C-7H.10.10.5 | Fed by | NOT DECIDED |
| C-7H.10.10.5 | Changes | NOT DECIDED |
| C-7H.10.10.6 | Fed by | NOT DECIDED |
| C-7H.10.10.6 | Changes | NOT DECIDED |
| C-7H.10.11 | Fed by | NOT DECIDED |
| C-7H.10.11 | Changes | NOT DECIDED |
| C-7H.10.11.1 | Fed by | NOT DECIDED |
| C-7H.10.11.1 | Changes | NOT DECIDED |
| C-7H.10.11.2 | Fed by | NOT DECIDED |
| C-7H.10.11.2 | Changes | NOT DECIDED |
| C-7H.10.11.3 | Fed by | NOT DECIDED |
| C-7H.10.11.3 | Changes | NOT DECIDED |
| C-7H.10.11.4 | Fed by | NOT DECIDED |
| C-7H.10.11.4 | Changes | NOT DECIDED |
| C-7H.10.11.5 | Fed by | NOT DECIDED |
| C-7H.10.11.5 | Changes | NOT DECIDED |
| C-7H.10.11.6 | Fed by | NOT DECIDED |
| C-7H.10.11.6 | Changes | NOT DECIDED |
| C-7H.10.11.7 | Fed by | NOT DECIDED |
| C-7H.10.11.7 | Changes | NOT DECIDED |
| C-7H.10.11.8 | Fed by | NOT DECIDED |
| C-7H.10.11.8 | Changes | NOT DECIDED |
| C-7H.10.11.9 | Fed by | NOT DECIDED |
| C-7H.10.11.9 | Changes | NOT DECIDED |
| C-7H.10.11.10 | Fed by | NOT DECIDED |
| C-7H.10.11.10 | Changes | NOT DECIDED |
| C-7H.10.11.11 | Fed by | NOT DECIDED |
| C-7H.10.11.11 | Changes | NOT DECIDED |
| C-7H.10.11.12 | Fed by | NOT DECIDED |
| C-7H.10.11.12 | Changes | NOT DECIDED |
| C-7H.10.11.13 | Fed by | NOT DECIDED |
| C-7H.10.11.13 | Changes | NOT DECIDED |
| C-7H.10.11.14 | Fed by | NOT DECIDED |
| C-7H.10.11.14 | Changes | NOT DECIDED |
| C-7H.10.12 | Fed by | NOT DECIDED |
| C-7H.10.12.1 | Fails closed by | NOT DECIDED |
| C-7H.10.12.1 | Fed by | NOT DECIDED |
| C-7H.10.12.1 | Changes | NOT DECIDED |
| C-7H.10.12.2 | Fails closed by | NOT DECIDED |
| C-7H.10.12.2 | Fed by | NOT DECIDED |
| C-7H.10.12.2 | Changes | NOT DECIDED |
| C-7H.10.12.3 | Fed by | NOT DECIDED |
| C-7H.10.12.3 | Changes | NOT DECIDED |
| C-7H.10.12.4 | Fed by | NOT DECIDED |
| C-7H.10.12.4 | Changes | NOT DECIDED |
| C-7H.10.12.5 | Fed by | NOT DECIDED |
| C-7H.10.12.5 | Changes | NOT DECIDED |
| C-7H.10.13 | Fed by | NOT DECIDED |
| C-7H.10.13 | Changes | NOT DECIDED |
| C-7H.11.1 | Fed by | NOT DECIDED |
| C-7H.11.1 | Gated by | NOT DECIDED |
| C-7H.11.1 | Changes | NOT DECIDED |
| C-7H.11.2 | Fed by | NOT DECIDED |
| C-7H.11.2 | Changes | NOT DECIDED |
| C-7H.11.3 | Fed by | NOT DECIDED |
| C-7H.11.3 | Changes | NOT DECIDED |
| C-7H.11.4 | Gated by | NOT DECIDED |
| C-7H.11.4 | Changes | NOT DECIDED |
| C-7H.11.4.1 | Fails closed by | NOT DECIDED |
| C-7H.11.4.1 | Fed by | NOT DECIDED |
| C-7H.11.4.1 | Gated by | NOT DECIDED |
| C-7H.11.4.1 | Changes | NOT DECIDED |
| C-7H.11.4.2 | Fails closed by | NOT DECIDED |
| C-7H.11.4.2 | Fed by | NOT DECIDED |
| C-7H.11.4.2 | Gated by | NOT DECIDED |
| C-7H.11.4.2 | Changes | NOT DECIDED |
| C-7H.11.4.3 | Fed by | NOT DECIDED |
| C-7H.11.4.3 | Gated by | NOT DECIDED |
| C-7H.11.4.3 | Changes | NOT DECIDED |
| C-7H.11.4.4 | Fails closed by | NOT DECIDED |
| C-7H.11.4.4 | Fed by | NOT DECIDED |
| C-7H.11.4.4 | Gated by | NOT DECIDED |
| C-7H.11.4.4 | Changes | NOT DECIDED |
| C-7H.11.4.5 | Fails closed by | NOT DECIDED |
| C-7H.11.4.5 | Fed by | NOT DECIDED |
| C-7H.11.4.5 | Gated by | NOT DECIDED |
| C-7H.11.4.5 | Changes | NOT DECIDED |
| C-7H.11.4.6 | Fails closed by | NOT DECIDED |
| C-7H.11.4.6 | Fed by | NOT DECIDED |
| C-7H.11.4.6 | Gated by | NOT DECIDED |
| C-7H.11.4.6 | Changes | NOT DECIDED |
| C-7H.11.5 | Fed by | NOT DECIDED |
| C-7H.11.5 | Changes | NOT DECIDED |
| C-7H.11.6 | Fed by | NOT DECIDED |
| C-7H.11.6 | Changes | NOT DECIDED |
| C-7H.11.7 | Fed by | NOT DECIDED |
| C-7H.11.7 | Changes | NOT DECIDED |
| C-7H.11.8 | Fed by | NOT DECIDED |
| C-7H.11.8 | Changes | NOT DECIDED |
| C-7H.11.9 | Fed by | NOT DECIDED |
| C-7H.11.9 | Changes | NOT DECIDED |
| C-7H.11.10 | Fed by | NOT DECIDED |
| C-7H.11.10 | Changes | NOT DECIDED |
| C-7H.12 | Fed by | NOT DECIDED |
| C-7H.12 | Changes | NOT DECIDED |
| C-7H.12.1 | Fed by | NOT DECIDED |
| C-7H.12.1 | Changes | NOT DECIDED |
| C-7H.12.2 | Fed by | NOT DECIDED |
| C-7H.12.2 | Changes | NOT DECIDED |

## Retained plain-gate inventory

All populated TOGETHER lines name an owning or connected card; no plain gate remains.

## Source coverage added by CH05-d

| Source | Scope read | Landing / exclusion |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: Complete §7H; inherited §7G-A failed-job boundary referenced through CH05-b conflict register. | C-7H and C-7H.1: complete record set, trigger classes and preservation; queue integration conflict retained. |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped: Complete C-7H, CY-F and A25/B10 entries; no whole-map credit. | Root identity, CY-F placement and planned owner boundaries. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md` | Whole: Complete accepted file, including operative structure, states, recovery and open boundaries; project workflow and author self-audit excluded from behavior. | C-7H.2 through C-7H.6: every identity, RR stage, eight duplicate points, seventeen recovery cases and logs. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md` | Whole: Complete accepted file, including operative structure, states, recovery and open boundaries; project workflow and author self-audit excluded from behavior. | C-7H.9 and C-7H.12: full generic retry classification, state, admission, nine duplicate points, nineteen recovery cases and logs. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md` | Whole: Complete accepted file, including operative structure, states, recovery and open boundaries; project workflow and author self-audit excluded from behavior. | C-7H.10: every value/configuration, episode/attempt identity, anchor, gate, special first attempt, real-change field, recovery/failure case and state event; C-7G.9 reused for B24 fallback. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md` | Whole: Complete accepted file, including operative structure, states, recovery and open boundaries; project workflow and author self-audit excluded from behavior. | C-7H.7: direct/wider semantic truth, overlap, absence and context boundaries. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md` | Whole: Complete accepted file, including operative structure, states, recovery and open boundaries; project workflow and author self-audit excluded from behavior. | C-7H.7.4 through C-7H.7.8: canonical assignment record and full commit, context, failure and recovery contract. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md` | Whole: Complete accepted file, including operative structure, states, recovery and open boundaries; project workflow and author self-audit excluded from behavior. | C-7H.8: typed manual record, exclusivity, context, seven failure conditions, five recovery cases and logs. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md` | Whole: Complete accepted file, including operative structure, states, recovery and open boundaries; project workflow and author self-audit excluded from behavior. | C-7H.12: owner/held/terminal/preservation boundaries only; no architecture created from the note. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Scoped: Complete §9 RM-RR-01; shared §§5.1–5.7 and §6 already read for CH05-c and consumed by exact existing shared IDs. Other declarations and full-file credit remain pending. | C-7H.11 supplies all thirteen declaration items; shared uncertainty remains C-7F.6.10.5 and retrieval-specific stop remains C-7F.7.3. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Scoped: Header and §§1–5 for accepted status and exact source identity; no whole-file credit this piece. | Acceptance/identity evidence only; receipt summaries supply no new mechanics. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Scoped: Header and §§1–5 for accepted status and exact source identity; no whole-file credit this piece. | Acceptance/identity evidence only; receipt summaries supply no new mechanics. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Scoped: Header and §§1–5 for accepted status and exact source identity; no whole-file credit this piece. | Acceptance/identity evidence only; receipt summaries supply no new mechanics. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Scoped: Header and §§1–5 for accepted status and exact source identity; no whole-file credit this piece. | Acceptance/identity evidence only; receipt summaries supply no new mechanics. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Scoped: Header and §§1–5 for accepted status and exact source identity; no whole-file credit this piece. | Acceptance/identity evidence only; receipt summaries supply no new mechanics. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Scoped: Header and §§1–5 for accepted status and exact source identity; no whole-file credit this piece. | Acceptance/identity evidence only; receipt summaries supply no new mechanics. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Scoped: Header and §§1–10 read for identity, accepted scope and dated open dependencies; partial repository-placement section, no whole-file credit. | Acceptance/identity evidence only; receipt summaries supply no new mechanics. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Scoped: Header and §§1–4 complete for accepted formal-declaration identity/status and conditional receipt-audit scope; no whole-file credit this piece. | Acceptance/identity evidence only; receipt summaries supply no new mechanics. |

## Coverage matrix — cumulative carried inventory









The following inventory retains the preceding pieces’ placements and read status. This piece’s additional placements and deferrals are in the source-scope table above; inherited notes are not fresh whole-read claims.
### File coverage

| Row | Source | Read scope | Placement |
|---|---|---|---|
| F001 | `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped read in CH04-b: §0B; §6A SCHEMA CONSTRAINTS; §6B schema/status boundary; full §7E-TSC §§1–31. Prior read credits retained. | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.1; C-STORE.2; C-STORE.3; CY-A Chapter 3-b: C-READ and its v1 record, validator, writer, quarantine, production-boundary and operation-record sub-parts; CY-A/CY-F reading-write interfaces. Chapter 3-c: governing checks for C-READ.10; A2/firmness additions stay ACCEPTED, never BUILT. Chapter 3-d: source-status and no-production-write boundaries; governing operational living-memory rule at C-READ.11.9.4.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.3, C-ENGINE-C.3.1, C-ENGINE-C.3.2, C-ENGINE-C.3.3, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.11.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1, C-ENGINE-AB.1.1, C-ENGINE-AB.1.2, C-ENGINE-AB.1.3, C-ENGINE-AB.2, C-ENGINE-AB.2.1, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.1, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.2.4, C-ENGINE-AB.3, C-ENGINE-AB.4, C-ENGINE-AB.5, C-ENGINE-AB.6, C-ENGINE-AB.8, C-ENGINE-AB.9.; CH03-k: C-INDEX, C-INDEX.1, C-INDEX.1.1, C-INDEX.1.2, C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.1, C-INDEX.4.2, C-INDEX.4.3, C-INDEX.4.4, C-INDEX.4.5, C-INDEX.4.7, C-INDEX.4.8, C-INDEX.5, C-INDEX.6.; CH03-l: C-GOLD, C-GOLD.2, C-GOLD.2.1, C-GOLD.3, C-GOLD.3.1, C-GOLD.6, C-GOLD.6.1, C-GOLD.6.2, C-GOLD.6.3, C-GOLD.7, C-GOLD.7.4.; CH03-o: C-INGEST, C-INGEST.1, C-INGEST.2, C-INGEST.3, C-INGEST.4, C-INGEST.4.1, C-INGEST.4.2, C-INGEST.4.3, C-INGEST.4.4, C-INGEST.4.5, C-INGEST.4.6, C-INGEST.4.7, C-INGEST.4.8, C-INGEST.4.8.1, C-INGEST.4.8.2, C-INGEST.4.8.3, C-INGEST.4.8.4, C-INGEST.4.9, C-INGEST.6.; CH03-p: C-DETECT, C-DETECT.1, C-DETECT.1.1, C-DETECT.1.3, C-DETECT.2, C-DETECT.2.1, C-DETECT.2.2, C-DETECT.2.3, C-DETECT.2.4, C-DETECT.2.5, C-DETECT.3, C-DETECT.3.1, C-DETECT.3.2, C-DETECT.3.3, C-DETECT.3.4, C-DETECT.3.5, C-DETECT.3.6, C-DETECT.4.1.; CH04-a: C-7E, C-7E.1, C-7E.1.1, C-7E.1.2, C-7E.2, C-7E.3, C-7E.4, C-7E.5, C-7E.5.1, C-7E.5.2, C-7E.5.3, C-7E.5.4, C-7E.5.5, C-7E.5.6, C-7E.6, C-7E.6.1, C-7E.6.2, C-7E.6.3, C-7E.6.4, C-7E.6.5, C-7E.6.6, C-7E.6.7, C-7E.7, C-7E.8, C-7E.8.1, C-7E.8.2, C-7E.8.3, C-7E.8.4, C-7E.9, C-7E.9.1, C-7E.9.2, C-7E.9.2.1, C-7E.9.2.2, C-7E.9.2.3, C-7E.9.2.4, C-7E.9.3, C-7E.9.3.1, C-7E.9.3.2, C-7E.9.3.3, C-7E.9.3.4, C-7E.9.3.5, C-7E.9.3.6, C-7E.9.4, C-7E.10, C-7E.10.1, C-7E.10.2, C-7E.11, C-7E.12, C-7E.13, C-7E.13.1, C-7E.13.4, C-7E.13.5, C-7E.13.6. CH04-b: see the exact source-scope and landing table above.  CH04-c: scoped read; exact scope and placement in the current source table.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-c: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F002 | `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Scoped read in CH04-b: §3N; inspection conflict. Prior read credits retained. | EXCLUDED: interaction/workflow guidance under §1.3 and §2.4. NOT PLACED: remaining behavior belongs to other component groups.; Chapter 3-a: C-STORE.2.3 Chapter 3-b: C-READ.1 confidence semantics and C-READ.2 uncertainty-preserving shape gate; remaining scope retained. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.2, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.8.; CH03-l: C-GOLD, C-GOLD.2, C-GOLD.2.1, C-GOLD.3, C-GOLD.3.1, C-GOLD.4, C-GOLD.4.1, C-GOLD.4.2, C-GOLD.4.3, C-GOLD.4.4, C-GOLD.4.5, C-GOLD.4.6, C-GOLD.5, C-GOLD.6, C-GOLD.6.1, C-GOLD.6.3, C-GOLD.8.3, C-GOLD.8.5.10, C-GOLD.8.5.11.; CH04-a: C-7E, C-7E.1.2, C-7E.5.2, C-7E.6.1, C-7E.6.2, C-7E.7, C-7E.8.4, C-7E.13.3. CH04-b: see the exact source-scope and landing table above. |
| F003 | `01_AUTHORITATIVE/cursorrules` | Scoped reread for CH03-o; prior whole-read credit retained where previously recorded | EXCLUDED: coding-process rules under §1.3. NOT PLACED: built-code boundaries belong to store, reader and code-boundary groups. Chapter 3-b: C-READ.1.12 per-store/global-key conflict and C-READ.3 shared write boundary; workflow remains excluded. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB.5.; CH03-k: C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.6.; CH03-l: C-GOLD, C-GOLD.9.; CH03-o: C-INGEST, C-INGEST.4, C-INGEST.4.7, C-INGEST.6. |
| F004 | `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Scoped read in CH04-b: Embedded TSC §§15–16; conflicting inspection and failed-authorization text. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. CH04-b: see the exact source-scope and landing table above. |
| F005 | `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped read in CH04-b: C-TSC and CY-D; component naming and path ownership. Prior read credits retained. | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.3.4; CY-A Chapter 3-b: C-READ component name, operation logging and consumer/caller relationships; CY-A/CY-F interfaces. Chapter 3-c: component ownership/names and Group A/D boundary; accepted A2 supplies behavior. Chapter 3-d: names, Group A ownership and per-reading seam versus full CY-G boundary.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.9.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1.1, C-ENGINE-AB.1.3, C-ENGINE-AB.2.1, C-ENGINE-AB.2.4, C-ENGINE-AB.4, C-ENGINE-AB.6, C-ENGINE-AB.6.1.; CH03-k: C-INDEX, C-INDEX.2, C-INDEX.3, C-INDEX.5, C-INDEX.6, C-INDEX.6.1, C-INDEX.6.2, C-INDEX.6.3, C-INDEX.6.4, C-INDEX.6.5, C-INDEX.6.6.; CH03-l: C-GOLD, C-GOLD.4, C-GOLD.4.6, C-GOLD.6, C-GOLD.6.2, C-GOLD.7, C-GOLD.7.1, C-GOLD.7.2, C-GOLD.7.3, C-GOLD.7.4.; CH03-o: C-INGEST, C-INGEST.4.4, C-INGEST.4.7, C-INGEST.5, C-INGEST.5.1, C-INGEST.5.2, C-INGEST.5.3, C-INGEST.5.4, C-INGEST.6.; CH03-p: C-DETECT, C-DETECT.1, C-DETECT.1.1, C-DETECT.1.2, C-DETECT.1.3, C-DETECT.2, C-DETECT.2.1, C-DETECT.2.2, C-DETECT.2.3, C-DETECT.2.4, C-DETECT.2.5, C-DETECT.3, C-DETECT.3.1, C-DETECT.3.3, C-DETECT.3.4, C-DETECT.3.6, C-DETECT.4, C-DETECT.4.1, C-DETECT.4.1.1, C-DETECT.4.1.2, C-DETECT.4.2.; CH04-a: C-7E, C-7E.3, C-7E.4, C-7E.5, C-7E.5.2, C-7E.6.1, C-7E.6.4, C-7E.7, C-7E.8, C-7E.11, C-7E.13, C-7E.13.1, C-7E.13.2, C-7E.13.3, C-7E.13.4, C-7E.13.5, C-7E.13.6, C-7E.13.7. CH04-b: see the exact source-scope and landing table above.  CH04-c: scoped read; exact scope and placement in the current source table.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-c: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
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
| F072 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F073 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F074 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F075 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F076 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F077 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F078 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F079 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | Scoped read in CH04-b: §5 paths 3–4; authority owner/limit cross-check. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F080 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F081 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-d: exact read scope and placement in the current source table; prior credits retained. |
| F082 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-d: exact read scope and placement in the current source table; prior credits retained. |
| F083 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for Bundle 6 mechanics; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained. |
| F084 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped read in CH04-b: §3 held/sealed restrictions and privacy precedence. Prior read credits retained. | Chapter 3-a: C-STORE.5 / operation protections, B17, B20, B21; other component scopes NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: C-7E, C-7E.2, C-7E.8, C-7E.9.1, C-7E.11, C-7E.12. CH04-b: see the exact source-scope and landing table above.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F085 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for Origin policy; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained. |
| F086 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Scoped reread for CH04-a; prior whole-read credit retained where previously recorded | Chapter 3-a: C-STORE.5 / Origin preservation policy; A3.4–A3.5 and other components NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: Navigation excerpt only; no new behavior sourced in this piece.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.7, C-ENGINE-AB.8.; CH04-a: C-7E.12.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
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
| V10-H033 | ### §7G CREATION-AWARE MODE  [SETTLED CONCEPT — NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-d: C-14 and explicit shared/deferred owners.  CH05-a: C-7G and explicit shared/deferred owners. |
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
| V10-H072 | ## 14. THE CHAT FRONT DOOR  [PARTIALLY SETTLED, PARTIALLY OPEN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading.  CH04-c: live-loop surface and model boundary in C-13; remaining chat/model internals retain their later owners.  CH04-d: C-14 and explicit shared/deferred owners. |
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

















## READ RECORD

Each current source identity was checked against its pinned Git blob. Whole-file credit is limited to rows marked Whole; all other reading is scoped. Contract §§5–11 and the complete lessons were reopened before writing; §11.3 is reopened after writing.

| Source file | Reading credit | SHA-256 |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: Complete §7H; inherited §7G-A failed-job boundary referenced through CH05-b conflict register. | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped: Complete C-7H, CY-F and A25/B10 entries; no whole-map credit. | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md` | Whole: Complete accepted file, including operative structure, states, recovery and open boundaries; project workflow and author self-audit excluded from behavior. | `215b74841321656a8b7fb1cbf4b9ac9b43259315864cd9f85f5ce86b43d10001` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md` | Whole: Complete accepted file, including operative structure, states, recovery and open boundaries; project workflow and author self-audit excluded from behavior. | `78c5d0b74d91e9390d9ebdf4d1c6ae04dd2632ad86c8efa83f01cfbd9974e606` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md` | Whole: Complete accepted file, including operative structure, states, recovery and open boundaries; project workflow and author self-audit excluded from behavior. | `e8f4c3debe65d258519f07a71b221802297596e2f9ef86148d2ad1a5800b0814` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md` | Whole: Complete accepted file, including operative structure, states, recovery and open boundaries; project workflow and author self-audit excluded from behavior. | `8a50a862b77fb3efa3d1523c570d88716d002973139d6bd47c26fce2e0246f8b` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md` | Whole: Complete accepted file, including operative structure, states, recovery and open boundaries; project workflow and author self-audit excluded from behavior. | `b5869d85ddfd8fcc611333c5e205904ae94c927b4ad4151b5955de16b04ba18d` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md` | Whole: Complete accepted file, including operative structure, states, recovery and open boundaries; project workflow and author self-audit excluded from behavior. | `a09128803d79d0ed38dd2e1f76f49d27d69c9d232e31cd623df7ff5fb0e20cd1` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md` | Whole: Complete accepted file, including operative structure, states, recovery and open boundaries; project workflow and author self-audit excluded from behavior. | `95491b9b621a814a8ac96fb5dba2cb4a9dc6b53ab519111a1aa067c1bbb1ef8c` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Scoped: Complete §9 RM-RR-01; shared §§5.1–5.7 and §6 already read for CH05-c and consumed by exact existing shared IDs. Other declarations and full-file credit remain pending. | `b2a5b3fbea75f7123a16c8a45c0fb096f4c4565585a4a0c7b7709e70f27d000e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Scoped: Header and §§1–5 for accepted status and exact source identity; no whole-file credit this piece. | `da62a1e8216924f9e9f3182f925e7a1e5063355418a7302eb58f86eee54adeea` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Scoped: Header and §§1–5 for accepted status and exact source identity; no whole-file credit this piece. | `2f9fa7df2d190bf6defae31e8e8a10f78df71a0ef8cb22fc8150f413f7e3c30e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Scoped: Header and §§1–5 for accepted status and exact source identity; no whole-file credit this piece. | `c640d3675a5c626c95e0654a8f314995930c791554cc8f6f6cf562233e1468c2` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Scoped: Header and §§1–5 for accepted status and exact source identity; no whole-file credit this piece. | `87f76711a4ba14ea2758197a9d45caff57b22f1bdd49b1a0d6b3f3767450de11` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Scoped: Header and §§1–5 for accepted status and exact source identity; no whole-file credit this piece. | `2b03cc7f1c7998b4c6fbe8e546b186af65e6f8afda1cea0735748c5ac90879de` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Scoped: Header and §§1–5 for accepted status and exact source identity; no whole-file credit this piece. | `d401d8c59695962d4b85608fc0ab88105474c6333af7581cf5189f8e0670bda8` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Scoped: Header and §§1–10 read for identity, accepted scope and dated open dependencies; partial repository-placement section, no whole-file credit. | `6defb8d417f8da26d86d48918ac6098c07abadd6826f2ec35ac2d00d1931efef` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Scoped: Header and §§1–4 complete for accepted formal-declaration identity/status and conditional receipt-audit scope; no whole-file credit this piece. | `faa88d9c991b2e4058081717a4fcbeb5a8e27d62e0f484ae6051fc061a03bac1` |

Instruction fingerprints:

- Contract v1_0: `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1`.
- Writer lessons v0_1: `635be95b861c181efb3b7bc1b2a8405ab706f864068a0b88f31fb91971adf3e6`.
- Run instructions v0_2: `93431167c0fb03fe1216ebbc12655ac640d71bcb7a59659cd123f51e72a54611`.

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

### READ-folder files not yet read whole

70 inherited pending files remain. Scoped reads do not remove whole-file obligations; previous read credits and source placements remain.

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
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md`
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
§1.3 no history/actions/roles/workflow in this chapter: PASS — 319 behavior cards reviewed; 0 project/workflow hits. Source-status and scope notes are outside the behavior cards.
§1.4 every gap written as NOT DECIDED: PASS — 782 empty fields/cells exactly match the register; 10 additional implementation slots are explicit.
§1.5 conflicts marked, none resolved: PASS — 1 explicit conflict-register rows. The existing V10 terminal-job versus later accepted bounded fresh-attempt conflict is explicitly retained; no integrated queue transition is invented. Trigger-category scope, later accepted completions, exact careful-retry eligibility, child reason versus parent terminal, early-stop cause versus closed-episode disposition, and relevance/assignment/manual boundaries remain explicit source distinctions.
§3 exactly one stamp per line: PASS — 319 headers, 2360 populated fields and 612 USED BY rows checked; 0 BUILT field lines. Relationship stamps follow the named card.
§4 every behavior line cited in the exact format: PASS — 96 distinct current citations resolve at the pin; all populated fields and relationship rows are cited. Claims were reviewed against the mapped source sections.
§5.4 one name per thing: PASS — 319 current IDs checked for duplicates, prior collisions and exact official names; shared atoms retain their previous names.
§6 all template fields present, in order, for every part: PASS — 319 templates and 3142 field lines checked.
§6.3 reciprocity within this chapter: PASS — 526 internal lines cover 526 reciprocal pairs; 16 external-use continuations and 8 incoming continuations name both endpoints; 6 further outgoing lines are answered directly by the named cards' own USED BY rows.
§6.4 every decided detail written in, no citation used in place of content: PASS — All mapped current reread/retry content is written: complete trigger/claim/reading/parent/layer identities; RR0–RR5 and RR-PR; eight B10 duplicate points, seventeen recovery cases and full logs; both semantic modes, independent/overlap/absence rules, eight assignment fields, three exact forms, immutable slot binding, seven failures and five recoveries; eight manual carrier fields, four typed distinctions, exclusivity, context, seven failures and five recoveries; six retry outcome classes, three attempt kinds, group/attempt/request/state/authority fields, R0–R4, nine duplicate points and nineteen recovery cases; all fourteen configuration fields and exact bounds; permanent and episode numbering, schedule anchors and mixed contexts, eight admission gates, the no-gap/deadline-pending first continuation attempt, protected outcomes, one careful-retry consumption, early stop/exhaustion, every change/consumption/episode field and key, six recovery boundaries, fourteen failure cases and five added state events. RM-RR-01 carries all thirteen declaration items with six dimensions, selected/excluded gates, no mouth, manual independence and shared uncertainty use. Shared B24 and uncertainty schemas retain their existing owners.
§6.5 sub-parts recursed to the bottom: PASS — 318 declared child/shared references and 319 owned cards checked; 182 explicit steps have 0 empty TOGETHER cases. Records recurse to named fields, values and bindings. Failure and recovery cases are individually named. Parent/child logs and terminal timing stay distinct; dual assignment creates one output. Shared attempt/group identities and recovery event IDs are reused rather than duplicated. Atomic timestamps and enum carriers do not acquire invented recovery machines.
§9 coverage matrix rows added for every file used: PASS — 18 current source identities, 145 READ-folder inventory rows and 107 V10 heading rows checked; 145 named source paths exist at the pin. Earlier credits and placements remain cumulative.
§10.11 no recommendation, no sentence addressed to Ness: PASS — the behavior was reviewed as system operation and boundaries; 0 formula phrases and 0 project/workflow hits.
Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md`.

Computed self-check output:

| Check | Count |
|---|---|
| cards | 319 |
| field_lines | 3142 |
| populated_fields | 2360 |
| not_decided_boxes | 782 |
| not_decided_fields_and_cells | 782 |
| used_by_rows | 612 |
| relationships | 549 |
| internal_relationships | 526 |
| external_relationships | 23 |
| internal_use_pairs | 526 |
| external_use_pairs | 23 |
| used_by_continuation_rows | 16 |
| incoming_continuation_rows | 8 |
| plain_gates | 0 |
| step_cards_with_empty_together | 0 |
| explicit_step_cards_checked | 182 |
| unique_citations | 96 |
| resolved_citations | 96 |
| named_source_paths_checked | 145 |
| source_identities | 18 |
| whole_read_files | 7 |
| earlier_identities | 27 |
| pending_source_paths | 70 |
| built_field_lines | 0 |
| misfiled_scan_fields | 3142 |
| misfiled_scan_used_by_cells | 1836 |
| empty_restriction_failure_gate_boxes | 198 |
| formula_hits | 0 |
| wording_hits | 2 |
| wording_verbatim_exceptions | 2 |
| wording_actionable_hits | 0 |
| project_workflow_hits | 0 |
| path_use_rows | 1 |
| path_covered_cards | 319 |
| subpart_references_checked | 318 |
| v10_heading_rows_checked | 107 |
| read_folder_files_covered | 145 |
| source_names_checked | 42 |
| errors | 0 |
| additional_undecided_slots | 10 |
| explicit_source_conflict_records | 1 |

The 3,142 fields and 1,836 USED BY cells were reviewed against the source-to-leaf map, including 198 empty restriction/failure/gate boxes. All 182 selected action steps have named rule connections. The 23 external uses and eight incoming continuations preserve actual owner identity; C-READ.11 remains the quarantine promotion seam and C-7B.7 the hold owner. No BUILT behavior is asserted. The inherited CH02 C-7B.7.1.6 outgoing C-7H ACCEPTED stamp differs from the current DESIGNED root; the finding is retained outside behavior and earlier bytes are unchanged.

Two source-verbatim wording exceptions remain in inherited coverage: the A29 closure filename has a space before its extension (line 8779), and V10 heading 15 contains the literal dot-prefixed cursorrules name (line 8902). No actionable wording flags remain.

All 27 earlier completed fingerprints were rechecked and are listed in full. The final count table is compared against a recount after this block is appended. No earlier chapter, repository source or runtime code is changed.
