# Chapter 5-b — Group C: C-7GA

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH05-b.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`

This piece covers C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A), with all its sub-parts. It leaves C-7F to CH05-c, C-7H to CH05-d, C-CREATE to CH05-e, every path except P-MAIN to CH11, and the appendices to CH12.

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Every citation resolves at the pinned commit.

<!-- BEGIN BEHAVIOR -->

### C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A)
Stamp: DESIGNED    Source: [V10 §7G-A] [MAP C-7GA]

ALONE
- What it is: DESIGNED — The asynchronous post-root operation carrying a durably written new root through a reading, clash result and Computed View results to a closed job. [V10 §7G-A] [MAP C-7GA]
- Takes in: DESIGNED — A new `root_id`, its trigger, durable queue/instruction history and current purpose-specific authorizations. [V10 §7G-A] [MAP C-7GA]
- Does: DESIGNED — Releases ingestion after durable enqueue; one background worker claims the job and runs the sequential instruction, retrieval, proposal, acceptance, quarantine write, clash and view stages with checkpoints and idempotent recovery. [V10 §7G-A] [MAP C-7GA]
- Gives out: DESIGNED — A completed reading plus clash record/sentinel, zero or more profile snapshots/sentinels, and terminal job history, or the distinct failure/unfinished state. [V10 §7G-A] [MAP C-7GA]
- Must never: DESIGNED — Block root ingestion on the mouth, begin production here, run concurrent workers as a supported design, overwrite records, duplicate durable effects or treat handled technical failure as crash recovery. [V10 §7G-A] [MAP C-7GA]
- Fails closed by: DESIGNED — Stops at the actual failing boundary, preserves durable work and the proper pass/job state, and requires the owning recovery or authorized retry path. [V10 §7G-A] [MAP C-7GA]

TOGETHER
- Fed by: BUILT — C-STORE — Accretive store & sealed roots (§6B): Starts only after successful durable root append. [V10 §7G-A]
- Fed by: DESIGNED — C-7GA.3 — Queue activation and missing-job reconciliation: Startup repairs eligible durable roots lacking jobs. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Fed by: DESIGNED — C-7GA.4 — Asynchronous persistent local queue: Ingestion releases after durable enqueue while reading runs separately. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5 — Queue record family: Reads and appends the five queue record types. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.10 — thread_membership_v1: Uses the new-root assignment rule's explicit inputs and mode limits. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.11 — Worker pass sequence: Executes the ordered worker sequence with its immediate checkpoints. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fed by: DESIGNED — C-7GA.12 — Durable negative-result sentinels: Uses durable negative results as proof of completed work. [V10 §7G-A / SENTINEL RECORDS]
- Fed by: DESIGNED — C-7GA.13 — Queue-driven crash recovery: Startup follows the eight queue-driven recovery cases. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fed by: DESIGNED — C-7F — Context Retrieval (§7F): returns the permitted preceding context for the pass (CY-A). [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fed by: DESIGNED — C-LMAC — Live Mechanism Access Coordinator (§26): routes the pass-specific context request through internal-use authorization (P-MAIN step 8). [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fed by: DESIGNED — C-16 — Model Layer (§16): returns the mouth proposal for the declared mode (P-MAIN step 10). [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fed by: DESIGNED — C-READ — Reading record, validator, writer (§6B): records the reading in quarantine through the validator and writer (P-MAIN step 12). [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fed by: DESIGNED — C-7M — Computed View (§7M): processes the triggered view profiles after clash detection (P-MAIN step 15). [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-7GA.1 — Continuous live mechanism connection: Every live-state query follows current purpose-specific authorization through LMAC. [V10 §7G-A / LMAC AND THE CONTINUOUS MECHANISM CONNECTION]
- Gated by: DESIGNED — C-7GA.2 — Quarantine-only worker destination: Worker readings remain quarantine-only. [V10 §7G-A / IMPORTANT QUARANTINE BOUNDARY]
- Gated by: DESIGNED — C-7GA.6 — Atomic enqueue and new-root identity: All enqueue sources share one atomic duplicate boundary. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Gated by: DESIGNED — C-7GA.7 — Full-job OS lock and claim: An exclusive OS claim must cover every durable job operation. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gated by: DESIGNED — C-7GA.9 — Job-level reading idempotency: One reading identity spans all attempts of the new-root operation. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]
- Gated by: ACCEPTED — C-7GA.14 — Accepted retry and reread boundaries consumed by the worker: Handled failure requires explicit admission through its owning retry seam. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [V10 §7G-A]
- Gated by: DESIGNED — C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): the reading proposal passes its acceptance check before the writer step (P-MAIN step 11; CY-A). [V10 §7G] [MAP C-7G]
- Gated by: ACCEPTED — C-7B.7 — Hold-until-enough: a held root or source targeted by a reading-pass instruction is refused ordinary-reading use at the instruction path (CY-A). [04/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md §6] [MAP CY-A]
- Changes: DESIGNED — C-7GA.8 — Reading-pass instruction and log: Every attempt has a durable instruction before retrieval and a terminal history. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-STORE — Accretive store & sealed roots (§6B) | Durable root_id. | Hands the root to asynchronous post-root processing. | Ingestion releases without waiting for the mouth. | [V10 §7G-A] |
| 2 · BUILT | C-READ — Reading record, validator, writer (§6B) | Checked reading, stable key and retrieval/pass provenance. | Uses its existing validator/writer contract. | One quarantine reading per new-root operation. | [V10 §7G-A] |
| 3 · BUILT | C-ENGINE-AB — Engines A & B (§7C, §16) | Declared mode, target and separated context. | Supplies the bounded reading inputs. | Engine output remains quarantined and acceptance-gated. | [MAP C-ENGINE-AB] [V10 §7G-A] |
| 4 · DESIGNED | C-ENGINE-C.1 — Story-layer engine pass | Worker pass and operation provenance. | Uses the governed reading sequence. | No independent overwrite or production path. | [MAP C-ENGINE-C] [V10 §7G-A] |
| 5 · DESIGNED | C-ENGINE-C.9 — Inherited pass recovery | Durable job/pass/result state. | Recovers only unfinished work. | No duplicate story reading or hidden retry. | [MAP C-ENGINE-C] [V10 §7G-A / CRASH RECOVERY SEQUENCE] |
| 6 · DESIGNED | C-GOLD.6.2 — Live before nightly | Live-path readiness. | Preserves the required ordering. | Nightly activation is not implied by its trigger label. | [MAP C-ENGINE-C] |
| 7 · DESIGNED | C-13 — Live Loop (§13) | Eligible durable root. | Enqueues and releases the starter. | The reply's full synchronization remains separately open. | [MAP C-13] [V10 §7G-A] |
| 8 · DESIGNED | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | One pass's exact inputs. | Runs independent acceptance before the reading handoff. | Only governed reading material continues. | [V10 §7G-A] |
| 9 · DESIGNED | C-STORE — Accretive store & sealed roots (§6B); P-MAIN step 5 | Step 5: a successful durable new-root append. | Atomically enqueues the job and releases ingestion. | A durable async job exists without waiting for the model. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |
| 10 · DESIGNED | C-7GA.7 — Full-job OS lock and claim; P-MAIN step 6 | Step 6: one pending job. | Acquires the exclusive OS claim and records claim/in_progress. | One worker owns the job-processing interval. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 11 · DESIGNED | C-7GA.10 — thread_membership_v1; P-MAIN step 7 | Step 7: derived assignment inputs and trigger. | Runs thread_membership_v1 and writes a durable instruction. | The pass has an explicit permitted mode before retrieval. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
| 12 · DESIGNED | C-7GA.11.6 — Step 6 — Close instruction; P-MAIN step 13 | Step 13: the durable reading ID. | Closes the instruction completed while the job stays in_progress. | The reading pass is terminal and post-reading job work remains. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 13 · DESIGNED | C-7GA.7.6 — Claim release; P-MAIN step 16 | Step 16: all required durable stage checkpoints. | Appends completed job status and releases the OS lock. | A terminal completed job cannot be reselected for recovery. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 14 · DESIGNED | C-STORE — Accretive store & sealed roots (§6B); CY-A | A durably appended new root. | Runs the queue, worker, checkpoints and idempotent recovery. | One quarantine reading and completed clash/view accounting or honest failure state. | [V10 §7G-A] [MAP C-7GA] |
| 15 · DESIGNED | C-14 — Chat Front Door (§14); CY-B | The new-root asynchronous segment of a live turn. | Enqueues and processes without blocking the root-ingestion starter on the mouth. | The post-root result remains separate from the still-open full reply synchronization. | [V10 §7G-A] [MAP C-13] |
| 16 · ACCEPTED | C-ENROLL.15.15 — Recovery during partial reading completion | The reading owner's actual committed outcomes. | Supplies actual queue/read outcomes. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |
| 17 · ACCEPTED | C-ENROLL.8 — Closed-session root and reading handoff | Committed observations and a committed session-close or interruption fact. | Takes this place's change: committed roots enter its existing queue. | Committed roots enter its existing queue. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |
| 18 · ACCEPTED | C-ENROLL.8.4 — Root-identity reading enqueue | `{ root_id }`, verified from the root owner. | Gates this place: owns enqueue and reading outcomes. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 19 · ACCEPTED | C-ENROLL.6.18 — Readings pending state | Verified roots enqueued through the standard reading path. | Supplies actual enqueue truth. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 20 · ACCEPTED | C-BOP.15.5 — Frozen enrollment capture set and normal entry | Committed observations and the close/interruption fact. | Takes this place's change: committed roots enter its standard queue. | Committed roots enter its standard queue. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |
| 21 · ACCEPTED | C-ENROLL.6.19 — Readings partially completed state | The reading owner's actual partial outcomes. | Supplies committed reading outcomes. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |
| 22 · ACCEPTED | C-7GA.15 — B12 — Nightly-batch activation | A scheduled or recorded manual trigger, the one-time activation boundary, the current approved scheduler configuration and already-enqueued jobs. | Gates this place: retains the existing queue, claims, RC-1 through RC-8 recovery and idempotency as the job-progress authority. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §4] [V10 §7G-A] [MAP C-7GA] |
| 23 · ACCEPTED | C-BOP.13 — Accepted single-path observation ingestion | Authorized typed captures with the unchanged legacy subject and stable capture identity. | Takes this place's change: each committed root enters the existing reading queue. | Each committed root enters the existing reading queue. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |

SUB-PARTS: C-7GA.1 — Continuous live mechanism connection; C-7GA.2 — Quarantine-only worker destination; C-7GA.3 — Queue activation and missing-job reconciliation; C-7GA.4 — Asynchronous persistent local queue; C-7GA.5 — Queue record family; C-7GA.6 — Atomic enqueue and new-root identity; C-7GA.7 — Full-job OS lock and claim; C-7GA.8 — Reading-pass instruction and log; C-7GA.9 — Job-level reading idempotency; C-7GA.10 — thread_membership_v1; C-7GA.11 — Worker pass sequence; C-7GA.12 — Durable negative-result sentinels; C-7GA.13 — Queue-driven crash recovery; C-7GA.14 — Accepted retry and reread boundaries consumed by the worker

### C-7GA.1 — Continuous live mechanism connection
Stamp: DESIGNED    Source: [V10 §7G-A / LMAC AND THE CONTINUOUS MECHANISM CONNECTION]

ALONE
- What it is: DESIGNED — The worker's continuous connection to current N.H state through stateless LMAC. [V10 §7G-A / LMAC AND THE CONTINUOUS MECHANISM CONNECTION]
- Takes in: DESIGNED — Context requests and later purpose-specific privacy, relevance or permission queries during a pass. [V10 §7G-A / LMAC AND THE CONTINUOUS MECHANISM CONNECTION]
- Does: DESIGNED — Routes every live mechanism query through LMAC; Context Retrieval is the first such query, not the only permitted one. LMAC obtains current state at the moment of each query, routing to the owning component rather than replacing it. Every query remains subject to privacy and permission. [V10 §7G-A / LMAC AND THE CONTINUOUS MECHANISM CONNECTION]
- Gives out: DESIGNED — Current purpose-correct state throughout execution. [V10 §7G-A / LMAC AND THE CONTINUOUS MECHANISM CONNECTION]
- Must never: DESIGNED — Let LMAC own data, cache a result, accumulate a view of Ness, redefine a component's rule or use visible-output permission as the gate for an internal operation. [V10 §7G-A / LMAC AND THE CONTINUOUS MECHANISM CONNECTION]
- Fails closed by: DESIGNED — Internal-use and visible-output requests remain under their distinct owning privacy/permission gates. [V10 §7G-A / LMAC AND THE CONTINUOUS MECHANISM CONNECTION]

TOGETHER
- Fed by: DESIGNED — C-LMAC — Live Mechanism Access Coordinator (§26): Routes each query to the current owning component. [V10 §7G-A / LMAC AND THE CONTINUOUS MECHANISM CONNECTION]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): Every internal or visible query uses the privacy rule for that exact purpose. [V10 §7G-A / LMAC AND THE CONTINUOUS MECHANISM CONNECTION]
- Gated by: DESIGNED — C-7P — Permission & Authority Boundaries (§7P): Applicable permission rules govern every routed query. [V10 §7G-A / LMAC AND THE CONTINUOUS MECHANISM CONNECTION]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | Current privacy, relevance and permission state. | Keeps the worker connected throughout its pass. | No stale cached authorization. | [V10 §7G-A / LMAC AND THE CONTINUOUS MECHANISM CONNECTION] |

SUB-PARTS: NONE

### C-7GA.2 — Quarantine-only worker destination
Stamp: DESIGNED    Source: [V10 §7G-A / IMPORTANT QUARANTINE BOUNDARY]

ALONE
- What it is: DESIGNED — The worker's test-execution boundary around readings. [V10 §7G-A / IMPORTANT QUARANTINE BOUNDARY]
- Takes in: DESIGNED — Accepted reading material and the selected destination. [V10 §7G-A / IMPORTANT QUARANTINE BOUNDARY]
- Does: DESIGNED — Writes to `.nh_readings_quarantine.jsonl`. Keeps quarantine outside live production memory and outside automatic availability to every production function through LMAC. Production requires the production store, `.nh_readings_production_authorized`, the production writer path and all existing §6A/§1C protections to be formally satisfied. [V10 §7G-A / IMPORTANT QUARANTINE BOUNDARY]
- Gives out: DESIGNED — Quarantine readings without production activation. [V10 §7G-A / IMPORTANT QUARANTINE BOUNDARY]
- Must never: DESIGNED — Write production readings through this worker design, treat quarantine as live production memory or infer production permission from a successful test. [V10 §7G-A / IMPORTANT QUARANTINE BOUNDARY]
- Fails closed by: DESIGNED — Production does not begin while any required production condition is unsatisfied. [V10 §7G-A / IMPORTANT QUARANTINE BOUNDARY]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-READ.5 — Production readings authorization: Production requires the store, marker, writer and protection prerequisites. [V10 §7G-A / IMPORTANT QUARANTINE BOUNDARY]
- Changes: BUILT — C-READ.4 — Quarantine readings destination: Sends accepted test readings only to quarantine. [V10 §7G-A / IMPORTANT QUARANTINE BOUNDARY]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | Destination and production prerequisites. | Prevents production activation through testing. | No automatic live-memory exposure. | [V10 §7G-A / IMPORTANT QUARANTINE BOUNDARY] |

SUB-PARTS: NONE

### C-7GA.3 — Queue activation and missing-job reconciliation
Stamp: DESIGNED    Source: [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]

ALONE
- What it is: DESIGNED — The startup repair of a durable root write followed by a missed enqueue. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Takes in: DESIGNED — The durable activation boundary, eligible root lines after it and matching queue entries. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Does: DESIGNED — Checks each eligible root for `enqueue_key = stable_hash(root_id + "reading_job_v1")`; creates a missing job exactly once through the same atomic enqueue used by normal ingestion. Leaves append_root behavior unchanged. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Gives out: DESIGNED — Missing eligible jobs recovered without historical backfill or duplicates. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Must never: DESIGNED — Silently enqueue all historical roots, change append_root behavior or create duplicate jobs outside the enqueue critical section. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Fails closed by: DESIGNED — Missing activation metadata makes reconciliation refuse to run. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]

TOGETHER
- Fed by: DESIGNED — C-7GA.3.2 — Reconcile root-written job-missing gap: Repairs only roots after the activation cutoff with no matching job. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Gated by: DESIGNED — C-7GA.3.1 — Queue activation record: Reconciliation requires the deliberate durable activation boundary. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | Activation-scoped root/job comparison. | Reconciles through atomic enqueue. | No historical backfill or duplicate job. | [V10 §7G-A / QUEUE ACTIVATION BOUNDARY] |
| 2 · DESIGNED | C-7GA.3.1 — Queue activation record | Ness-enabled activation and actual root count. | Creates the protected boundary once. | No default full-history scan. | [V10 §7G-A / QUEUE ACTIVATION BOUNDARY] |
| 3 · ACCEPTED | C-7GA.15 — B12 — Nightly-batch activation | A scheduled or recorded manual trigger, the one-time activation boundary, the current approved scheduler configuration and already-enqueued jobs. | Gates this place: requires the existing one-time queue activation boundary to exist and validate. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §4] [V10 §7G-A / QUEUE ACTIVATION BOUNDARY] |

SUB-PARTS: C-7GA.3.1 — Queue activation record; C-7GA.3.2 — Reconcile root-written job-missing gap

### C-7GA.3.1 — Queue activation record
Stamp: DESIGNED    Source: [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]

ALONE
- What it is: DESIGNED — The protected metadata file `.nh_queue_activation.json` in `nh_engine_core`. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Takes in: DESIGNED — Ness's deliberate enabling of the queue and the root-store line count at that moment. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Does: DESIGNED — Writes the record once with `activated_at` and `activation_root_count`. Uses the count as the lower boundary of startup reconciliation. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Gives out: DESIGNED — A durable activation cutoff separating existing historical roots from eligible new roots. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Must never: DESIGNED — Treat the absence of this record as permission to scan all roots or automatically backfill pre-activation roots. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Fails closed by: DESIGNED — Without this record, reconciliation is refused; historical backfill needs separate deliberate authorization. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]

TOGETHER
- Fed by: DESIGNED — C-7GA.3.1.1 — activated_at: Records the ISO 8601 activation time. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Fed by: DESIGNED — C-7GA.3.1.2 — activation_root_count: Records the root-store line count at activation. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Fed by: DESIGNED — C-7GA.3 — Queue activation and missing-job reconciliation: Follows the deliberate activation and no-backfill contract. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Gated by: DESIGNED — Ness deliberately enables the queue before it activates. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.3 — Queue activation and missing-job reconciliation | Activation time and count. | Limits eligible roots. | Absence refuses the scan. | [V10 §7G-A / QUEUE ACTIVATION BOUNDARY] |
| 2 · DESIGNED | C-7GA.3.2 — Reconcile root-written job-missing gap | Durable cutoff. | Scans only later lines. | Missing metadata refuses reconciliation. | [V10 §7G-A / QUEUE ACTIVATION BOUNDARY] |

SUB-PARTS: C-7GA.3.1.1 — activated_at; C-7GA.3.1.2 — activation_root_count

### C-7GA.3.1.1 — activated_at
Stamp: DESIGNED    Source: [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]

ALONE
- What it is: DESIGNED — The activation record's ISO 8601 time field. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Takes in: DESIGNED — The time of deliberate queue activation. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Does: DESIGNED — Records when the feature was enabled. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Gives out: DESIGNED — `activated_at` in the durable activation record. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Must never: DESIGNED — Use a non-ISO-8601 value for activated_at. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.3.1 — Queue activation record | activated_at. | Dates deliberate activation. | Timed queue boundary. | [V10 §7G-A / QUEUE ACTIVATION BOUNDARY] |

SUB-PARTS: NONE

### C-7GA.3.1.2 — activation_root_count
Stamp: DESIGNED    Source: [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]

ALONE
- What it is: DESIGNED — The integer count of lines in `.nh_accretive_store.jsonl` at activation. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Takes in: DESIGNED — The actual root-store line count when the record is written. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Does: DESIGNED — Fixes reconciliation's first eligible line at `activation_root_count + 1`. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Gives out: DESIGNED — The durable historical/new-root cutoff. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Must never: DESIGNED — Automatically backfill roots at or before that cutoff. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.3.1 — Queue activation record | activation_root_count. | Fixes the first eligible line. | Historical roots stay outside automatic reconciliation. | [V10 §7G-A / QUEUE ACTIVATION BOUNDARY] |

SUB-PARTS: NONE

### C-7GA.3.2 — Reconcile root-written job-missing gap
Stamp: DESIGNED    Source: [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]

ALONE
- What it is: DESIGNED — The startup reconciliation step after a crash between durable append and enqueue. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Takes in: DESIGNED — Roots beginning after the activation count and their deterministic enqueue keys. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Does: DESIGNED — Scans for a matching job for each eligible root and invokes atomic enqueue only where none exists. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Gives out: DESIGNED — Exactly one job per eligible new-root identity. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Must never: DESIGNED — Infer eligibility before the activation boundary or bypass atomic duplicate checking. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Fails closed by: DESIGNED — Refuses the scan when activation metadata is absent. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7GA.3.1 — Queue activation record: Requires an existing activation count. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY]
- Changes: DESIGNED — C-7GA.6 — Atomic enqueue and new-root identity: Missing jobs use the same locked check-and-append as normal ingestion. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY] [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.3 — Queue activation and missing-job reconciliation | Eligible root and queue state. | Enqueues through the shared atomic boundary. | Missing jobs restored exactly once. | [V10 §7G-A / QUEUE ACTIVATION BOUNDARY] |

SUB-PARTS: NONE

### C-7GA.4 — Asynchronous persistent local queue
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — `.nh_reading_queue.jsonl`, a Full Protected append-only JSONL file alongside Layer 3 engine files in `nh_engine_core`. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — A successfully and durably written root followed by an enqueue request. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Writes one record per line. Ingestion enqueues and returns immediately; SMART reading runs separately. The design supports one background worker processing one job at a time; locks guard accidental concurrent startup. Code writing this protected file requires PROPOSED CHANGE dry-run approval before Cursor applies it. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — Durable jobs and appended state/stage/claim history. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: DESIGNED — Enqueue before the root is durable, enqueue after failed root write, block ingestion on reading work or treat the single-worker design as multi-worker parallelism. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fails closed by: DESIGNED — Failed root writing creates no job; failure to obtain the processing lock produces no processing. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

TOGETHER
- Fed by: DESIGNED — C-7GA.7 — Full-job OS lock and claim: A single worker holds the long processing claim. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gated by: DESIGNED — C-7GA.6 — Atomic enqueue and new-root identity: Durable roots enter through atomic enqueue. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | Persistent single-worker queue. | Processes asynchronously. | Root ingestion does not wait for the mouth. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5 — Queue record family
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The five record types in the append-only queue. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — Job creation, status transitions, stage completion, claims and stale-claim takeover. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Writes `job`, `job_status_event`, `job_stage_event`, `job_claimed` and `claim_expired` records without editing earlier entries. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — A durable queue history from which current state and completed work can be reconstructed. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: DESIGNED — Rewrite the original job or infer completed work solely from a missing checkpoint. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fails closed by: DESIGNED — Terminal completed/failed jobs are never selected for recovery. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

TOGETHER
- Fed by: DESIGNED — C-7GA.5.1 — job entry: Stores one immutable original job entry. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.2 — job_status_event: Appends job status transitions separately. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.3 — job_stage_event: Appends durable stage-completion checkpoints. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.4 — job_claimed: Records actual claim acquisition. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.5 — claim_expired: Records controlled stale-claim takeover. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | Job, state, stage and claim history. | Reconstructs actual durable progress. | No rewritten queue history. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: C-7GA.5.1 — job entry; C-7GA.5.2 — job_status_event; C-7GA.5.3 — job_stage_event; C-7GA.5.4 — job_claimed; C-7GA.5.5 — claim_expired

### C-7GA.5.1 — job entry
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The immutable queue entry written once at enqueue time. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — `entry_type`, `job_id`, `enqueue_key`, `root_id`, `trigger_source`, `trigger_declared_mode`, `trigger_override_reason` and `enqueued_at`. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Binds the new-root operation and trigger to a stable job record. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — A job with implicit pending state until its first status event. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: DESIGNED — Edit the job, alter its job_id or enqueue_key, or append a duplicate for an existing enqueue key. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fails closed by: DESIGNED — Existing matching enqueue identity returns its original job_id, regardless of status. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

TOGETHER
- Fed by: DESIGNED — C-7GA.5.1.1 — Job entry_type: Carries the fixed job discriminator. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.1.2 — Job job_id: Carries the stable uuid4 job identity. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.1.3 — Job enqueue_key: Carries the deterministic new-root duplicate key. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Fed by: DESIGNED — C-7GA.5.1.4 — Job root_id: Names the durably written target. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.1.5 — Job trigger_source: Carries the actual trigger source. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.5.1.6 — Job trigger_declared_mode: Carries the requested mode or null. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.5.1.7 — Job trigger_override_reason: Carries the trigger's actual override reason. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.5.1.8 — enqueued_at: Records enqueue time. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gated by: DESIGNED — C-7GA.6 — Atomic enqueue and new-root identity: A job is written only after locked absence checking. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5 — Queue record family | Job identity and trigger. | Preserves the new-root operation. | Pending exists before its first status event. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: C-7GA.5.1.1 — Job entry_type; C-7GA.5.1.2 — Job job_id; C-7GA.5.1.3 — Job enqueue_key; C-7GA.5.1.4 — Job root_id; C-7GA.5.1.5 — Job trigger_source; C-7GA.5.1.6 — Job trigger_declared_mode; C-7GA.5.1.7 — Job trigger_override_reason; C-7GA.5.1.8 — enqueued_at

### C-7GA.5.1.1 — Job entry_type
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The job record discriminator. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — Fixed value `job`. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Marks this entry as the original queued job. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — `entry_type = "job"`. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: DESIGNED — Use an entry_type other than job for the original queue entry. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.1 — job entry | entry_type job. | Identifies original enqueue. | Exact record type. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.1.2 — Job job_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The job's uuid4 identifier. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — The ID assigned at original enqueue. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Identifies the immutable job across queue and instruction records. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — A stable job reference. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: DESIGNED — Alter the existing job_id on duplicate enqueue or recovery. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.1 — job entry | job_id. | Identifies the job. | Immutable job reference. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.1.3 — Job enqueue_key
Stamp: DESIGNED    Source: [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]

ALONE
- What it is: DESIGNED — The deterministic string identity of one new-root operation. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Takes in: DESIGNED — The root_id and literal `reading_job_v1`. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Does: DESIGNED — Stores `stable_hash(root_id + "reading_job_v1")` permanently. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Gives out: DESIGNED — A duplicate-prevention identity shared by normal enqueue and reconciliation. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Must never: DESIGNED — Modify the stored key or reuse this new-root identity for a reread operation. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Fails closed by: DESIGNED — Existing identity absorbs duplicate enqueue regardless of current job status. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.1 — job entry | enqueue_key. | Binds canonical identity. | Duplicate enqueue returns the existing job. | [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE] |
| 2 · DESIGNED | C-7GA.9 — Job-level reading idempotency | Canonical new-root operation key. | Computes one stable reading key. | Random job IDs do not create duplicate readings. | [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] |

SUB-PARTS: NONE

### C-7GA.5.1.4 — Job root_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The reference to the already durably written target root. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — That root's identity. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Binds the queue job to its target. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — The worker's target-root reference. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: DESIGNED — Enqueue a job before its root write succeeds durably. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fails closed by: DESIGNED — Failed root write supplies no queued job. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.1 — job entry | root_id. | Links the job to its root. | No job after failed root write. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.1.5 — Job trigger_source
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The triggering process classification passed to mode assignment. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — `manual`, `live_ingestion`, `nightly_batch`, `reread_trigger` or an unrecognized source. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Carries the actual source into the instruction's override/default evaluation. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — A recorded trigger source without implicit permission to activate nightly or reread processing. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Treat recognition of nightly_batch as authorization to activate it or apply the new-root rule to rereads. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — Unrecognized-source declared overrides are rejected by the mode rule. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.1 — job entry | trigger_source. | Supplies source-specific mode evaluation. | Recognition grants no activation authority. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.5.1.6 — Job trigger_declared_mode
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The mode declaration, if supplied, carried by the trigger. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — The actual declared value or null. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Passes it unchanged to the override gate. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — A declaration evaluated under source-specific rules. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Treat a supplied declaration as automatically accepted. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — Disallowed or unrecognized declarations are rejected and the default rule follows. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.1 — job entry | trigger_declared_mode. | Supplies the override gate. | Declaration is not acceptance. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.5.1.7 — Job trigger_override_reason
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The trigger's reason for requesting an override. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — The actual reason, including null or empty input. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Carries it to the override gate; live_ingestion narrowing to bare requires a non-empty reason. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — Recorded override justification. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Accept a live_ingestion bare override with null or empty reason. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — That missing-reason override is rejected and default assignment follows. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.1 — job entry | trigger_override_reason. | Preserves justification for checking. | No fabricated narrowing permission. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.5.1.8 — enqueued_at
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The job enqueue time field. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — The time the job is enqueued. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Dates the original queue entry. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — `enqueued_at` provenance. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.1 — job entry | enqueued_at. | Dates the original job. | Timed queue history. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.2 — job_status_event
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — An appended record for each job lifecycle status transition. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — `entry_type = "job_status_event"`, `job_id`, `status`, `event_at` and `note`. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Records in_progress, completed or failed. Pending is implicit before any status event. Handled potentially retryable technical failure leaves the existing in_progress status unchanged. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — Append-only job state with terminal completed/failed outcomes. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: DESIGNED — Edit a status, append terminal failed for a merely handled retryable technical failure or select terminal jobs for recovery. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fails closed by: DESIGNED — Actual substantive rejection or an explicitly non-retryable condition ends in failed; retryable technical failure preserves unfinished work. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

TOGETHER
- Fed by: DESIGNED — C-7GA.5.2.1 — Status-event entry_type: Carries the status-event discriminator. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.2.2 — Status-event job_id: Names the affected job. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.2.3 — Job status: Carries the actual lifecycle status. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.2.4 — Status-event event_at: Dates the transition. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.2.5 — Status-event note: Preserves the transition note. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: Every job_status_event append needs matching claim identity. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5 — Queue record family | Actual lifecycle outcome. | Reconstructs current job state. | No in-place status edit. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |
| 2 · DESIGNED | C-7GA.11.7.4 — Step 7C — Close job | Complete job state. | Ends selection eligibility. | No later recovery selection. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |

SUB-PARTS: C-7GA.5.2.1 — Status-event entry_type; C-7GA.5.2.2 — Status-event job_id; C-7GA.5.2.3 — Job status; C-7GA.5.2.4 — Status-event event_at; C-7GA.5.2.5 — Status-event note

### C-7GA.5.2.1 — Status-event entry_type
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The status-event discriminator. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — Fixed value `job_status_event`. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Identifies the record as a job status transition. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — The exact entry_type. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: DESIGNED — Use a different discriminator for a job status event. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.2 — job_status_event | entry_type. | Identifies the transition record. | Exact record family. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.2.2 — Status-event job_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The job reference of a lifecycle transition. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — The owning job's stable ID. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Binds the appended status to that job. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — Job-specific state history. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.2 — job_status_event | job_id. | Binds its status. | Job-specific history. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.2.3 — Job status
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The three-value explicit status enum with implicit pending before its first event. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — `in_progress`, `completed` or `failed`, according to the actual transition. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Derives current job state from the latest status event; completed and failed are terminal. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — The state used for normal selection and recovery eligibility. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: DESIGNED — Re-select a completed or failed job for crash recovery. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fails closed by: DESIGNED — Terminal states exclude the job from recovery selection. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

TOGETHER
- Fed by: DESIGNED — C-7GA.5.2.3.1 — Implicit pending job: Absence of status means implicit pending. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.2.3.2 — in_progress job: in_progress retains unfinished work. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.2.3.3 — completed job: completed requires all stages. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.2.3.4 — failed job: failed records confirmed terminal failure. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.2 — job_status_event | in_progress, completed or failed. | Reconstructs current state. | Terminal jobs are excluded from recovery. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: C-7GA.5.2.3.1 — Implicit pending job; C-7GA.5.2.3.2 — in_progress job; C-7GA.5.2.3.3 — completed job; C-7GA.5.2.3.4 — failed job

### C-7GA.5.2.3.1 — Implicit pending job
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / CRASH RECOVERY SEQUENCE]

ALONE
- What it is: DESIGNED — A queued job with no status event yet. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Takes in: DESIGNED — An immutable job entry lacking status history. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Does: DESIGNED — Treats it as pending and eligible for normal startup after acquiring the exclusive claim. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Gives out: DESIGNED — A job ready for claim and in_progress transition. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Must never: DESIGNED — Treat missing status as proof that the root lacks a job or write a duplicate enqueue. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fails closed by: DESIGNED — No claim lock means no processing. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / CRASH RECOVERY SEQUENCE]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7GA.7.2 — Claim acquisition: Pending work starts only after exclusive claim acquisition. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.2.3 — Job status | Original job with no status event. | Allows normal claim/start. | No duplicate enqueue inferred. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.2.3.2 — in_progress job
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The nonterminal job state during reading and post-reading work. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — A successful claim followed by an appended in_progress event. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Preserves in_progress through reading_written, instruction completion and all unfinished post-reading stages. A handled technical pass failure leaves this state unchanged. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — Recoverable unfinished job state with separate pass outcome. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Treat a completed reading instruction as a completed queue job or silently turn a technical failure into a terminal job. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — Handled technical failure is excluded from automatic crash replay and awaits its authorized retry path. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7GA.11 — Worker pass sequence: Remains open through reading and unfinished post-reading stages. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.2.3 — Job status | Actual started job. | Preserves state through incomplete stages. | Technical pass failure does not close the job. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.2.3.3 — completed job
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The terminal state after all required reading and post-reading checkpoints exist. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — reading_written, clash_detection_completed and computed_view_completed, with every triggered profile accounted for. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Appends completed after claim validation and releases the OS lock. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — A terminal fully processed job. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Re-select the job or declare it completed before its required durable checkpoints. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — Missing checkpoints prevent this completion path. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7GA.11.7.4 — Step 7C — Close job: Completion requires the final checkpoint-verified close step. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.2.3 — Job status | Complete durable checkpoints. | Ends selection eligibility. | No replay of completed work. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.2.3.4 — failed job
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The terminal job outcome for confirmed non-retryable failure. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — A substantively rejected proposal or a condition expressly declared non-retryable under an adopted policy. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Appends failed, preserves the rejected attempt and releases the lock. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — A terminal failed job that crash recovery cannot select. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Use this state for a merely handled retryable technical failure or silently reopen it through crash recovery. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — The failed job is terminal; a separately authorized fresh-attempt design does not rewrite this record. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7GA.11.4 — Step 4 — Acceptance and fallback routing: Substantive rejection follows the terminal worker branch. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.2.3 — Job status | Substantive or explicitly non-retryable outcome. | Ends crash-recovery eligibility. | No automatic reopening. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.2.4 — Status-event event_at
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The time of a job lifecycle transition. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — The actual status-event time. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Dates the appended transition. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — `event_at` in status history. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.2 — job_status_event | event_at. | Records event time. | Timed state history. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.2.5 — Status-event note
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The note field accompanying the job transition. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — The note associated with that event. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Preserves it beside the status and time. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — Transition-note provenance. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.2 — job_status_event | note. | Retains event context. | Inspectable transition provenance. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.3 — job_stage_event
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — A durable checkpoint of completed reading or post-reading work. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — `entry_type`, `job_id`, `stage`, `event_at`, `operation_key` and the stage-specific fields. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Appends reading_written, then clash_detection_completed, then computed_view_completed, preserving durable results for recovery. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — A checkpoint that identifies already completed work. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Infer that an operation did not happen merely because its checkpoint is missing, or aggregate profiles before all are accounted for. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — Recovery checks the destination's durable result identity before repeating work. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7GA.5.3.1 — Stage-event entry_type: Carries the checkpoint discriminator. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.3.2 — Stage-event job_id: Names the owning job. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.3.3 — Stage-event stage: Names the completed stage. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.3.4 — Stage-event event_at: Records checkpoint time. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.3.5 — Stage-event operation_key: Carries the applicable operation identity or aggregate null. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.3.6 — Checkpoint reading_id: reading_written carries the actual reading identity. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.3.7 — clash_found: The clash checkpoint carries its actual boolean result. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.3.8 — Checkpoint clash_id: The clash checkpoint carries the actual ID or null. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.3.9 — all_profiles_complete: The view aggregate requires complete profile accounting. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.3.10 — profile_results: The view aggregate carries every triggered profile result. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: Every checkpoint append requires matching claim identity. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5 — Queue record family | Reading/clash/view results. | Records completed work. | Recovery can skip proven effects. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: C-7GA.5.3.1 — Stage-event entry_type; C-7GA.5.3.2 — Stage-event job_id; C-7GA.5.3.3 — Stage-event stage; C-7GA.5.3.4 — Stage-event event_at; C-7GA.5.3.5 — Stage-event operation_key; C-7GA.5.3.6 — Checkpoint reading_id; C-7GA.5.3.7 — clash_found; C-7GA.5.3.8 — Checkpoint clash_id; C-7GA.5.3.9 — all_profiles_complete; C-7GA.5.3.10 — profile_results

### C-7GA.5.3.1 — Stage-event entry_type
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The checkpoint discriminator. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — Fixed value `job_stage_event`. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Identifies a stage-completion entry. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — The exact entry_type. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: DESIGNED — Use a different discriminator for a stage event. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3 — job_stage_event | entry_type job_stage_event. | Identifies stage history. | Exact record family. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.3.2 — Stage-event job_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The owning-job reference of a checkpoint. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — The stable job ID. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Binds completed work to that job. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — Job-scoped stage history. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3 — job_stage_event | job_id. | Binds the checkpoint. | Job-specific progress. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.3.3 — Stage-event stage
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The three-value checkpoint-stage field. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — `reading_written`, `clash_detection_completed` or `computed_view_completed`. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Names the completed stage, in that sequence. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — Stage-specific recovery position. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: DESIGNED — Treat one stage's completion as completion of a later stage. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7GA.5.3.3.1 — reading_written checkpoint: reading_written records durable reading completion. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.3.3.2 — clash_detection_completed checkpoint: clash_detection_completed precedes view processing. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.3.3.3 — computed_view_completed checkpoint: computed_view_completed records all-profile completion. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3 — job_stage_event | stage. | Records its sequence position. | No later-stage inference. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: C-7GA.5.3.3.1 — reading_written checkpoint; C-7GA.5.3.3.2 — clash_detection_completed checkpoint; C-7GA.5.3.3.3 — computed_view_completed checkpoint

### C-7GA.5.3.3.1 — reading_written checkpoint
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The checkpoint for a durably existing reading. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — Its `reading_id`, recovered or freshly written. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Appends the stage event after claim validation; the job remains in_progress. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — Durable reading-stage completion without closing the queue job. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Rewrite an existing reading to repair a missing checkpoint. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — A missing checkpoint is restored from verified reading identity. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7GA.11.5.1 — Step 5A — Record reading checkpoint: Follows the immediate post-reading checkpoint rule. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: the processing claim is validated before this append. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3.3 — Stage-event stage | Verified reading_id. | Marks the reading stage. | Job remains in_progress. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |
| 2 · DESIGNED | C-7GA.11.5.1 — Step 5A — Record reading checkpoint | Durable reading_id. | Records the stage after validation. | No premature job completion. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.3.3.2 — clash_detection_completed checkpoint
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The checkpoint for durable clash detection or its no-clash sentinel. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — `clash_found` boolean, `clash_id` or null, and the exact operation_key. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Appends the result after claim validation and before Computed View processing. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — Durable proof the clash stage completed. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Begin view computation without this checkpoint or rerun detection when its operation-keyed result exists. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — Recovery restores the checkpoint from the durable clash record or sentinel. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7GA.11.7.1 — Step 7A — Record clash checkpoint: Follows the post-clash checkpoint rule. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: the processing claim is validated before this append. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3.3 — Stage-event stage | Keyed clash result. | Marks clash completion. | View work waits for this checkpoint. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |
| 2 · DESIGNED | C-7GA.11.7.1 — Step 7A — Record clash checkpoint | Durable clash result and key. | Records completion after claim validation. | View processing gains its predecessor checkpoint. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.3.3.3 — computed_view_completed checkpoint
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The aggregate checkpoint after every triggered profile has a durable result. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — `all_profiles_complete = true`, complete `profile_results`, and `operation_key = null`. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Appends once after all triggered profiles are accounted for. Zero triggered profiles produces an empty list. Recovery reconstructs the list from operation-keyed snapshots/sentinels. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — A completed view stage ready for job close. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Append incremental aggregate completion or rerun an already durably completed profile. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — Missing profile results keep the aggregate incomplete and the job in_progress. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7GA.11.7.3 — Step 7B checkpoint — Record complete profile accounting: Requires complete durable profile accounting before append. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3.3 — Stage-event stage | Complete result list and null aggregate key. | Marks view completion. | Job close may follow. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |
| 2 · DESIGNED | C-7GA.11.7.3 — Step 7B checkpoint — Record complete profile accounting | All profiles accounted for. | Writes true completion with null aggregate key. | Empty list only when none triggered. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.3.4 — Stage-event event_at
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The checkpoint event time field. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — The actual checkpoint time. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Dates the appended stage event. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — Timed stage history. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3 — job_stage_event | event_at. | Dates progress. | Timed stage history. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.3.5 — Stage-event operation_key
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The operation-identity field for a stage checkpoint. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — The clash operation key, or null for the computed-view aggregate; the reading_written variant names only its reading_id as its specific payload. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Preserves the applicable durable-result identity and the explicit aggregate null. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — A stage-appropriate operation reference without an invented aggregate operation key. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Substitute one profile's key for the aggregate null or infer a new reading-stage key format. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3 — job_stage_event | operation_key. | Links durable stage evidence. | No invented aggregate key. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.3.6 — Checkpoint reading_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The reading reference carried by reading_written. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — The ID of the reading already durably present. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Links the checkpoint to that reading. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — A recoverable reading-result reference. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: DESIGNED — Manufacture a reading ID when no durable reading exists. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3 — job_stage_event | reading_id. | Links the durable reading. | No duplicate write to repair history. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.3.7 — clash_found
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The boolean clash result in its checkpoint. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — The actual detection result or recovered no-clash sentinel. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Records whether a clash was found. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — A durable true/false clash finding. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: DESIGNED — Infer false merely because the checkpoint or clash_id is absent. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3 — job_stage_event | clash_found. | Records found or not found. | Missing data is not false. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.3.8 — Checkpoint clash_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The clash ID or null in the clash-stage checkpoint. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — The existing/new clash identity, or the no-clash result. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Records the actual clash_id, using null for no clash. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — Exact result linkage. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Create a new clash object when the same-clash rule identifies an existing one. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3 — job_stage_event | clash_id. | Links the result. | Same clash retains its identity. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.3.9 — all_profiles_complete
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The boolean indicating complete accounting of triggered view profiles. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — The actual durable results for every triggered profile. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Uses true only when the computed_view_completed aggregate is ready to append. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — A complete-stage flag. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Append the aggregate with a missing triggered-profile result. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — Missing results prevent aggregate completion. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3 — job_stage_event | all_profiles_complete. | Records true only on completion. | No partial aggregate. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.3.10 — profile_results
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The list of results for all triggered Computed View profiles. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — Each profile's durable snapshot or no-update sentinel. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Includes one entry per triggered profile; reconstructs completed entries by operation-key lookup; permits an empty list when none were triggered. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — A complete profile-result list for the aggregate checkpoint. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Drop a triggered profile, rerun an already committed profile or append an incomplete aggregate list. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — The aggregate waits until every triggered profile is accounted for. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7GA.5.3.10.1 — Result view_profile_id: Identifies each triggered profile. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.3.10.2 — Profile result: Carries the actual profile outcome. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.3.10.3 — Profile snapshot_id: Preserves the result's snapshot reference. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.3.10.4 — Profile operation_key: Preserves the exact per-profile operation key. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3 — job_stage_event | profile_results. | Accounts for completed profiles. | Empty list only when none triggered. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: C-7GA.5.3.10.1 — Result view_profile_id; C-7GA.5.3.10.2 — Profile result; C-7GA.5.3.10.3 — Profile snapshot_id; C-7GA.5.3.10.4 — Profile operation_key

### C-7GA.5.3.10.1 — Result view_profile_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The profile identity in one profile-results entry. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — The triggered view profile's ID. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Identifies which profile the result belongs to. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — Profile-specific result provenance. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3.10 — profile_results | view_profile_id. | Binds its result. | Profile-specific accounting. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.3.10.2 — Profile result
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The two-value per-profile result field. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — `snapshot_created` or `no_update`. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Records whether computation produced a snapshot or the durable no-update result. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — The actual profile outcome. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: DESIGNED — Treat a missing result as no_update. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fails closed by: DESIGNED — A durable snapshot or sentinel is required for completed accounting. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

TOGETHER
- Fed by: DESIGNED — C-7GA.5.3.10.2.1 — snapshot_created profile result: snapshot_created requires a committed snapshot result. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.3.10.2.2 — no_update profile result: no_update requires a committed negative result. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3.10 — profile_results | snapshot_created or no_update. | Records completed work. | Missing result cannot count as complete. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: C-7GA.5.3.10.2.1 — snapshot_created profile result; C-7GA.5.3.10.2.2 — no_update profile result

### C-7GA.5.3.10.2.1 — snapshot_created profile result
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The per-profile result when the triggered update durably creates a snapshot. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — The profile's committed snapshot and operation key. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Records result snapshot_created with the recovered snapshot identity in profile_results. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — A durably completed profile entry. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Record a created snapshot without its durable destination result or recompute a completed keyed profile. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — Recovery returns the existing snapshot result instead of rerunning the update. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7GA.11.7.2 — Step 7B — Process triggered view profiles: Uses the actual profile-update result. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3.10.2 — Profile result | Actual snapshot identity. | Records the positive outcome. | No false snapshot claim. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.3.10.2.2 — no_update profile result
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS]

ALONE
- What it is: DESIGNED — The per-profile result when a triggered update durably produces no update. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS]
- Takes in: DESIGNED — The profile's committed no_update_sentinel. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS]
- Does: DESIGNED — Records result no_update from the exact operation-keyed sentinel and counts the profile as accounted for. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS]
- Gives out: DESIGNED — A completed no-update profile entry. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS]
- Must never: DESIGNED — Treat missing data as no_update or rerun a completed negative result. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS]
- Fails closed by: DESIGNED — A durable sentinel is required to recover this no-update outcome. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS]

TOGETHER
- Fed by: DESIGNED — C-7GA.12.2 — no_update_sentinel: Uses the profile's durable no-update proof. [V10 §7G-A / SENTINEL RECORDS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3.10.2 — Profile result | no_update_sentinel. | Records completed no-update work. | Missing data is not completion. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.3.10.3 — Profile snapshot_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The snapshot-reference field in a profile result. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — The value recovered from that profile's durable snapshot or sentinel record. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Preserves the exact result's snapshot_id. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — A profile-result reference. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: DESIGNED — Invent a snapshot identity when the operation produced no snapshot. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3.10 — profile_results | snapshot_id. | Links the durable result. | No invented snapshot. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.3.10.4 — Profile operation_key
Stamp: DESIGNED    Source: [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The durable identity of one triggered profile operation. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — job_id, reading_id and view_profile_id. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Uses `{job_id}::{reading_id}::computed_view::{view_profile_id}`. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — The key used to recover that profile without recomputing it. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Use the aggregate null in place of a profile's operation key or commit the same key twice. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — Existing operation-keyed records are recovered instead of rerun. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3.10 — profile_results | Profile-specific key. | Recovers completed work. | No duplicate profile effect. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |

SUB-PARTS: NONE

### C-7GA.5.4 — job_claimed
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

ALONE
- What it is: DESIGNED — The appended event recording a worker's acquired claim. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Takes in: DESIGNED — `entry_type = "job_claimed"`, `job_id`, `claim_id`, `worker_id`, `claimed_at` and `expires_at`. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Does: DESIGNED — Records the claim only after non-blocking exclusive OS-lock acquisition. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gives out: DESIGNED — Durable worker/claim/job provenance with diagnostic expiry. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Must never: DESIGNED — Treat expires_at alone as concurrency authority or record successful claim acquisition while another worker holds the OS lock. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Fails closed by: DESIGNED — Failed lock acquisition produces no processing and the worker exits. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

TOGETHER
- Fed by: DESIGNED — C-7GA.5.4.1 — Claimed-event entry_type: Carries the claim-event discriminator. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.4.2 — Claimed-event job_id: Names the claimed job. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.4.3 — Claimed-event claim_id: Names the acquired uuid4 claim. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.4.4 — Claimed-event worker_id: Names the actual worker. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.4.5 — claimed_at: Dates acquisition using the literal schema field. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.4.6 — Claimed-event expires_at: Carries diagnostic intended expiry. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gated by: DESIGNED — C-7GA.7.2 — Claim acquisition: Successful OS-lock acquisition must precede the event. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5 — Queue record family | Acquired worker/claim identity. | Preserves claim provenance. | Expiry remains diagnostic. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: C-7GA.5.4.1 — Claimed-event entry_type; C-7GA.5.4.2 — Claimed-event job_id; C-7GA.5.4.3 — Claimed-event claim_id; C-7GA.5.4.4 — Claimed-event worker_id; C-7GA.5.4.5 — claimed_at; C-7GA.5.4.6 — Claimed-event expires_at

### C-7GA.5.4.1 — Claimed-event entry_type
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The claim-acquisition event discriminator. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — Fixed value `job_claimed`. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Identifies the appended claim event. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — The exact entry_type. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: DESIGNED — Use a different discriminator for a claim-acquisition event. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.4 — job_claimed | entry_type job_claimed. | Identifies acquisition. | Exact record family. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.4.2 — Claimed-event job_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The job reference in a claim event. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — The claimed job's ID. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Binds the claim to that job. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — Job-specific claim history. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.4 — job_claimed | job_id. | Links the event. | Job-scoped claim history. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.4.3 — Claimed-event claim_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

ALONE
- What it is: DESIGNED — The uuid4 identity assigned to the acquired claim. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Takes in: DESIGNED — The new claim's UUID. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Does: DESIGNED — Records the identity used for defensive validation before durable work. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gives out: DESIGNED — A stable reference to this claim. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Must never: DESIGNED — Commit job work under a mismatched claim_id. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Fails closed by: DESIGNED — Claim mismatch cannot authorize a durable job operation. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.4 — job_claimed | claim_id. | Preserves defensive identity. | Commits stay claim-bound. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.4.4 — Claimed-event worker_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The identity of the worker holding the claim. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — The actual worker identity. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Records the holder with the claim and job. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — Worker-specific claim provenance. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.4 — job_claimed | worker_id. | Records the holder. | Worker-scoped provenance. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.4.5 — claimed_at
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The acquisition-time field named in the literal job_claimed schema. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — The time the claim was acquired. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Dates the appended acquisition event. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — `claimed_at` provenance. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.4 — job_claimed | claimed_at. | Records the event time. | Timed claim history. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.4.6 — Claimed-event expires_at
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

ALONE
- What it is: DESIGNED — Diagnostic claim-expiry metadata in the acquisition event. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Takes in: DESIGNED — The intended claim-expiry time. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Does: DESIGNED — Records the intended duration for monitoring without replacing the OS-held lock. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gives out: DESIGNED — Diagnostic expiry provenance. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Must never: DESIGNED — Take over merely because this timestamp passes while a process still holds the OS lock. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Fails closed by: DESIGNED — A live held OS lock prevents takeover regardless of expiry metadata. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.4 — job_claimed | expires_at. | Supports monitoring. | Expiry alone authorizes no takeover. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.5 — claim_expired
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

ALONE
- What it is: DESIGNED — The appended stale-claim takeover event after successful acquisition of the existing lock file. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Takes in: DESIGNED — `entry_type = "claim_expired"`, `job_id`, old `claim_id`, `expired_at`, `taken_over_by_worker_id` and `taken_over_by_claim_id`. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Does: DESIGNED — Links the stale claim to the newly acquired worker/claim, followed by the new job_claimed event. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gives out: DESIGNED — Traceable takeover history. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Must never: DESIGNED — Delete/re-create the lock file to force takeover or expire a claim while its process holds the lock. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Fails closed by: DESIGNED — Failed non-blocking OS-lock acquisition makes takeover refuse and the recovery worker exit. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

TOGETHER
- Fed by: DESIGNED — C-7GA.5.5.1 — Expired-event entry_type: Carries the stale-claim discriminator. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.5.2 — Expired-event job_id: Names the affected job. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.5.3 — Expired-event claim_id: Names the stale predecessor claim. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.5.4 — expired_at: Dates takeover recording. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.5.5 — taken_over_by_worker_id: Names the successor worker. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fed by: DESIGNED — C-7GA.5.5.6 — taken_over_by_claim_id: Names the successor claim. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gated by: DESIGNED — C-7GA.7.7 — Stale-claim takeover: Takeover must acquire the existing OS lock successfully. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5 — Queue record family | Old and new claim identities. | Links replacement ownership. | No forced lock-file replacement. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: C-7GA.5.5.1 — Expired-event entry_type; C-7GA.5.5.2 — Expired-event job_id; C-7GA.5.5.3 — Expired-event claim_id; C-7GA.5.5.4 — expired_at; C-7GA.5.5.5 — taken_over_by_worker_id; C-7GA.5.5.6 — taken_over_by_claim_id

### C-7GA.5.5.1 — Expired-event entry_type
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The stale-claim event discriminator. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — Fixed value `claim_expired`. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Identifies the appended takeover event. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — The exact entry_type. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: DESIGNED — Use a different discriminator for a claim-expired event. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.5 — claim_expired | entry_type claim_expired. | Identifies takeover history. | Exact record family. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.5.2 — Expired-event job_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The job reference in the takeover record. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — The affected job's stable identity. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Links the stale and replacement claim history to that job. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — Job-scoped takeover provenance. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.5 — claim_expired | job_id. | Links the transition. | Job-specific takeover history. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.5.3 — Expired-event claim_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The stale claim identity recorded as expired. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — The prior claim_id read from the existing lock metadata. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Preserves which claim was replaced. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — Traceable prior-claim reference. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.5 — claim_expired | claim_id. | Preserves replaced identity. | No lost claim lineage. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.5.4 — expired_at
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The time of recording the stale claim's expiry/takeover. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — The actual event time. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Dates the claim_expired event. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — Timed takeover history. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.5 — claim_expired | expired_at. | Records the actual event time. | Timed claim history. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.5.5 — taken_over_by_worker_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The successor worker identity in the takeover event. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — The worker that acquired the existing OS lock. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Identifies the new holder. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — Successor-worker provenance. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.5 — claim_expired | taken_over_by_worker_id. | Identifies new ownership. | Checkable holder lineage. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.5.5.6 — taken_over_by_claim_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]

ALONE
- What it is: DESIGNED — The successor claim identity in the takeover event. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Takes in: DESIGNED — The newly assigned claim_id. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Does: DESIGNED — Links the old claim to its replacement. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gives out: DESIGNED — Successor-claim provenance. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.5 — claim_expired | taken_over_by_claim_id. | Links replacement identity. | Checkable claim lineage. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] |

SUB-PARTS: NONE

### C-7GA.6 — Atomic enqueue and new-root identity
Stamp: DESIGNED    Source: [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]

ALONE
- What it is: DESIGNED — The short critical section protecting one deterministic new-root enqueue identity. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Takes in: DESIGNED — A durably written root and `enqueue_key = stable_hash(root_id + "reading_job_v1")`. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Does: DESIGNED — Acquires the exclusive OS lock on `.nh_enqueue.lock`; scans for any job with that key; appends and flushes one job if absent or returns the existing job_id if present; releases the lock immediately. Normal ingestion and startup reconciliation use exactly this boundary. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Gives out: DESIGNED — One immutable queued job per new-root operation identity. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Must never: DESIGNED — Hold the enqueue lock through reading work, change an existing key/job ID, duplicate an entry because its status is terminal or reuse the new-root key for rereads. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Fails closed by: DESIGNED — An existing matching job absorbs the enqueue in every status. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]

TOGETHER
- Fed by: DESIGNED — C-7GA.6.1 — Enqueue lock target: Uses the separate short enqueue lock target. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Fed by: DESIGNED — C-7GA.6.3 — Existing enqueue lookup: Checks every existing job for the exact key. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Gated by: DESIGNED — C-7GA.6.2 — Enqueue lock acquisition: Exclusive acquisition must precede lookup/append. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Changes: DESIGNED — C-7GA.6.4 — Missing enqueue commit: Appends and flushes only after locked absence. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Changes: DESIGNED — C-7GA.6.5 — Enqueue lock release: Releases immediately after the enqueue result. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | Deterministic root operation key. | Finds or creates exactly one job. | Reconciliation cannot duplicate ingestion enqueue. | [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE] |
| 2 · DESIGNED | C-7GA.3.2 — Reconcile root-written job-missing gap | Eligible root and enqueue key. | Reconciles exactly once. | No duplicate job effect. | [V10 §7G-A / QUEUE ACTIVATION BOUNDARY] [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE] |
| 3 · DESIGNED | C-7GA.4 — Asynchronous persistent local queue | Confirmed root and key. | Appends or absorbs the job. | No queue-before-root ordering. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE] |
| 4 · DESIGNED | C-7GA.5.1 — job entry | Exact enqueue identity and root durability. | Appends once or returns existing. | No duplicate original entry. | [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE] |
| 5 · DESIGNED | C-7GA.6.2 — Enqueue lock acquisition | New-root enqueue request. | Acquires before all checks and writes. | No race between lookup and append. | [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE] |
| 6 · DESIGNED | C-7GA.6.5 — Enqueue lock release | Durable result or existing ID. | Releases immediately. | No long-lived enqueue claim. | [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE] |

SUB-PARTS: C-7GA.6.1 — Enqueue lock target; C-7GA.6.2 — Enqueue lock acquisition; C-7GA.6.3 — Existing enqueue lookup; C-7GA.6.4 — Missing enqueue commit; C-7GA.6.5 — Enqueue lock release

### C-7GA.6.1 — Enqueue lock target
Stamp: DESIGNED    Source: [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]

ALONE
- What it is: DESIGNED — `.nh_enqueue.lock`, a short-lived mechanical queue-safety file in nh_engine_core. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Takes in: DESIGNED — The enqueue check-and-append operation. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Does: DESIGNED — Provides an OS-level exclusive lock target only during enqueue; remains distinct from `.nh_queue.lock`. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Gives out: DESIGNED — A brief mutually exclusive enqueue boundary. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Must never: DESIGNED — Use it as a long claim or hold it during job processing. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.6 — Atomic enqueue and new-root identity | The `.nh_enqueue.lock` target. | Protects only check-and-append. | Reading work never holds this lock. | [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE] |

SUB-PARTS: NONE

### C-7GA.6.2 — Enqueue lock acquisition
Stamp: DESIGNED    Source: [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]

ALONE
- What it is: DESIGNED — The first action in the enqueue critical section. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Takes in: DESIGNED — The enqueue lock target and proposed deterministic key. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Does: DESIGNED — Acquires exclusive OS locking before scanning or appending. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Gives out: DESIGNED — Exclusive ownership of the check-and-append interval. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Must never: DESIGNED — Check and append outside that mutual-exclusion boundary. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Fails closed by: DESIGNED — No unprotected enqueue is authorized. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]

TOGETHER
- Fed by: DESIGNED — C-7GA.6 — Atomic enqueue and new-root identity: Follows the owning atomic enqueue sequence. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.6 — Atomic enqueue and new-root identity | Acquired short lock. | Establishes the atomic interval. | No unprotected enqueue. | [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE] |
| 2 · DESIGNED | C-7GA.6.3 — Existing enqueue lookup | Acquired critical section. | Searches the exact identity. | Locked absence is trustworthy for append. | [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE] |

SUB-PARTS: NONE

### C-7GA.6.3 — Existing enqueue lookup
Stamp: DESIGNED    Source: [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]

ALONE
- What it is: DESIGNED — The duplicate pre-check while the short lock is held. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Takes in: DESIGNED — Queue job entries and the exact enqueue_key. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Does: DESIGNED — Searches for entry_type job with that key; a match in any status returns the original job_id and writes no new job. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Gives out: DESIGNED — The original identity or verified absence within the critical section. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Must never: DESIGNED — Ignore terminal-status matches or alter the existing job identity. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Fails closed by: DESIGNED — A matching entry prevents a duplicate job append. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7GA.6.2 — Enqueue lock acquisition: Looks up while the exclusive short lock is held. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.6 — Atomic enqueue and new-root identity | Existing identity or locked absence. | Absorbs duplicates in any status. | No duplicate original job. | [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE] |
| 2 · DESIGNED | C-7GA.6.4 — Missing enqueue commit | Verified absence. | Appends and flushes once. | Existing job identity absorbs duplicates. | [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE] |

SUB-PARTS: NONE

### C-7GA.6.4 — Missing enqueue commit
Stamp: DESIGNED    Source: [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]

ALONE
- What it is: DESIGNED — The append-and-flush action after the locked lookup finds no matching job. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Takes in: DESIGNED — The new immutable job entry and confirmed key absence. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Does: DESIGNED — Appends and flushes that entry before releasing the short lock. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Gives out: DESIGNED — One durable queued job. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Must never: DESIGNED — Append after finding an existing key or release the critical section before its required append/flush completes. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Fails closed by: DESIGNED — Existing identity takes the return-existing branch instead. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7GA.6.3 — Existing enqueue lookup: Commits only when the locked lookup found no matching job. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.6 — Atomic enqueue and new-root identity | New job and verified absence. | Commits one queue effect. | Durable enqueue before release. | [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE] |

SUB-PARTS: NONE

### C-7GA.6.5 — Enqueue lock release
Stamp: DESIGNED    Source: [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]

ALONE
- What it is: DESIGNED — The immediate end of the short enqueue critical section. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Takes in: DESIGNED — Completed append/flush or existing-job return. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Does: DESIGNED — Releases the enqueue OS lock without waiting for mouth or reading work. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Gives out: DESIGNED — Ingestion free of the long worker claim. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Must never: DESIGNED — Keep this lock for the job-processing duration. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7GA.6 — Atomic enqueue and new-root identity: Ends the owning critical section as soon as enqueue completes. [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.6 — Atomic enqueue and new-root identity | Completed append or existing-job return. | Ends short locking. | Ingestion remains independent of reading duration. | [V10 §7G-A / ENQUEUE-LEVEL IDEMPOTENCY AND ATOMIC ENQUEUE] |

SUB-PARTS: NONE

### C-7GA.7 — Full-job OS lock and claim
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

ALONE
- What it is: DESIGNED — `.nh_queue.lock`, the process-scoped concurrency authority held for an entire job claim. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Takes in: DESIGNED — One candidate job, worker identity and claim metadata. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Does: DESIGNED — Requires non-blocking exclusive OS-lock acquisition and holds it continuously through processing and clean failure/completion. Process exit or crash automatically releases the OS lock. POSIX flock(LOCK_EX plus LOCK_NB), Windows msvcrt.locking or LockFileEx, or an equivalent may satisfy the contract; the exact API is a build-time choice. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gives out: DESIGNED — One worker authorized to commit job work at a time, with diagnostic metadata and defensive identity checks. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Must never: DESIGNED — Release/reacquire between stages, use expires_at as concurrency authority, support multi-worker parallelism through this design or use O_CREAT plus O_EXCL on this lock file. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Fails closed by: DESIGNED — If the OS lock cannot be acquired, no processing or takeover occurs and the worker exits. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

TOGETHER
- Fed by: DESIGNED — C-7GA.7.1 — Lock claim metadata: Carries the current claim metadata without substituting it for locking. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Fed by: DESIGNED — C-7GA.7.7 — Stale-claim takeover: Stale takeover acquires the existing file's OS lock. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Fed by: DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): supplies the pending job this card claims (P-MAIN step 6). [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-7GA.7.2 — Claim acquisition: Requires non-blocking exclusive acquisition. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gated by: DESIGNED — C-7GA.7.3 — Continuous claim holding: Holds continuously through the whole claim. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: Every named durable operation requires matching claim identity. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Changes: DESIGNED — C-7GA.7.4 — Diagnostic claim renewal: Renews diagnostic expiry during processing. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Changes: DESIGNED — C-7GA.7.6 — Claim release: Releases on completion, clean handled failure or process exit. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | Acquired processing lock. | Holds and validates the claim. | No concurrent committer. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 2 · DESIGNED | C-7GA.4 — Asynchronous persistent local queue | Exclusive OS-lock result. | Prevents accidental concurrent processing. | No multi-worker design implied. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 3 · DESIGNED | C-7GA.7.2 — Claim acquisition | Candidate job and worker. | Acquires and records the claim. | Only one committer enters. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 4 · DESIGNED | C-7GA.7.3 — Continuous claim holding | Acquired claim. | Holds without interruption. | Every durable stage remains exclusive. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 5 · DESIGNED | C-7GA.7.6 — Claim release | Actual job/pass stop state. | Releases or relies on OS crash release. | No live stale-process authority. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 6 · DESIGNED | C-7GA.11 — Worker pass sequence | Acquired job claim. | Executes all durable work under it. | No between-stage concurrency gap. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 7 · DESIGNED | C-7GA.13 — Queue-driven crash recovery | Actual OS-lock result. | Holds the recovery claim. | Live holder prevents takeover. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |

SUB-PARTS: C-7GA.7.1 — Lock claim metadata; C-7GA.7.2 — Claim acquisition; C-7GA.7.3 — Continuous claim holding; C-7GA.7.4 — Diagnostic claim renewal; C-7GA.7.5 — Validate claim before durable work; C-7GA.7.6 — Claim release; C-7GA.7.7 — Stale-claim takeover

### C-7GA.7.1 — Lock claim metadata
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

ALONE
- What it is: DESIGNED — The metadata stored in the existing processing lock file. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Takes in: DESIGNED — `worker_id`, `claim_id`, `job_id`, `locked_at` and `expires_at`. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Does: DESIGNED — Records the current worker, claim and job with acquisition/expiry times; renews diagnostic expiry while the OS lock remains held. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gives out: DESIGNED — A monitorable claim with a defensive identity reference. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Must never: DESIGNED — Treat metadata or elapsed expiry as a replacement for the held OS lock. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Fails closed by: DESIGNED — Metadata cannot authorize takeover while another process retains the lock. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

TOGETHER
- Fed by: DESIGNED — C-7GA.7.1.1 — Lock worker_id: Records the actual worker. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Fed by: DESIGNED — C-7GA.7.1.2 — Lock claim_id: Records the current defensive claim identity. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Fed by: DESIGNED — C-7GA.7.1.3 — Lock job_id: Names the job under the claim. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Fed by: DESIGNED — C-7GA.7.1.4 — locked_at: Records lock acquisition time. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Fed by: DESIGNED — C-7GA.7.1.5 — Lock expires_at: Records renewable diagnostic expiry. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gated by: DESIGNED — C-7GA.7.3 — Continuous claim holding: the exclusive OS lock remains continuously held. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.7 — Full-job OS lock and claim | Worker, claim, job and diagnostic times. | Supports validation and monitoring. | The OS lock remains authority. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 2 · DESIGNED | C-7GA.7.5 — Validate claim before durable work | Exact claim_id values. | Validates before durable operations. | No mismatched-claim commit. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |

SUB-PARTS: C-7GA.7.1.1 — Lock worker_id; C-7GA.7.1.2 — Lock claim_id; C-7GA.7.1.3 — Lock job_id; C-7GA.7.1.4 — locked_at; C-7GA.7.1.5 — Lock expires_at

### C-7GA.7.1.1 — Lock worker_id
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

ALONE
- What it is: DESIGNED — The current claim holder's identity in the lock file. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Takes in: DESIGNED — The worker that acquired the OS lock. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Does: DESIGNED — Records the actual holder. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gives out: DESIGNED — Worker-specific lock provenance. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.7.1 — Lock claim metadata | worker_id. | Identifies the holder. | Worker-scoped metadata. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |

SUB-PARTS: NONE

### C-7GA.7.1.2 — Lock claim_id
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

ALONE
- What it is: DESIGNED — The claim identity checked before each durable job operation. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Takes in: DESIGNED — The acquired claim's ID. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Does: DESIGNED — Records it in the lock metadata and compares it with the worker's held claim before every governed commit. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gives out: DESIGNED — A defensive same-claim check. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Must never: DESIGNED — Commit durable job work under a mismatched claim or treat this comparison as the concurrency authority itself. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Fails closed by: DESIGNED — Mismatch does not authorize a durable operation. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.7.1 — Lock claim metadata | claim_id. | Supports before-commit comparison. | Mismatched claims cannot commit. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |

SUB-PARTS: NONE

### C-7GA.7.1.3 — Lock job_id
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

ALONE
- What it is: DESIGNED — The job identity associated with the processing claim. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Takes in: DESIGNED — The claimed job's stable ID. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Does: DESIGNED — Records which job the worker holds. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gives out: DESIGNED — Job-specific lock metadata. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.7.1 — Lock claim metadata | job_id. | Binds claim scope. | Job-specific ownership. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |

SUB-PARTS: NONE

### C-7GA.7.1.4 — locked_at
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

ALONE
- What it is: DESIGNED — The acquisition-time field named in the lock metadata. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Takes in: DESIGNED — The time this claim acquired the lock. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Does: DESIGNED — Dates the processing claim in that file. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gives out: DESIGNED — `locked_at` diagnostic provenance. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.7.1 — Lock claim metadata | locked_at. | Dates current metadata. | Timed ownership provenance. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |

SUB-PARTS: NONE

### C-7GA.7.1.5 — Lock expires_at
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

ALONE
- What it is: DESIGNED — The renewable diagnostic intended-expiry time. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Takes in: DESIGNED — The configured claim duration and renewal activity. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Does: DESIGNED — Updates expires_at periodically as a liveness signal, without changing the authority of the continuously held OS lock. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gives out: DESIGNED — Monitoring metadata for the current claim. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Must never: DESIGNED — Authorize takeover from elapsed expiry alone. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Fails closed by: DESIGNED — A live OS lock prevents takeover regardless of the timestamp. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.7.1 — Lock claim metadata | expires_at. | Supports monitoring. | Expiry is not takeover permission. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |

SUB-PARTS: NONE

### C-7GA.7.2 — Claim acquisition
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

ALONE
- What it is: DESIGNED — Non-blocking acquisition of the long processing lock. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Takes in: DESIGNED — `.nh_queue.lock`, one job and the new worker/claim identity. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Does: DESIGNED — Opens the file and acquires exclusive OS locking; on success writes the complete claim metadata and appends job_claimed. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gives out: DESIGNED — A recorded live claim preceding in_progress and worker steps. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Must never: DESIGNED — Record successful acquisition or process work when the lock is held elsewhere. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Fails closed by: DESIGNED — Failed acquisition makes the worker exit with no processing. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

TOGETHER
- Fed by: DESIGNED — C-7GA.7 — Full-job OS lock and claim: Follows the process-scoped, non-blocking exclusive-lock rule. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.2.3.1 — Implicit pending job | Lock result. | Begins normal processing. | No work without claim. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] [V10 §7G-A / CRASH RECOVERY SEQUENCE] |
| 2 · DESIGNED | C-7GA.5.4 — job_claimed | Actual exclusive lock. | Records the acquired claim. | No falsely claimed ownership. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 3 · DESIGNED | C-7GA.7 — Full-job OS lock and claim | OS-lock result. | Permits one holder. | Failed acquisition exits. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 4 · DESIGNED | C-7GA.7.7 — Stale-claim takeover | Non-blocking OS-lock result. | Replaces metadata and appends takeover events. | Another holder makes recovery exit. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 5 · DESIGNED | C-7GA.13.2 — RC-1 — Job with no status | The pending job and exclusive processing lock. | Proceeds only when the exclusive processing lock is acquired first. | Nothing in this card. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] |

SUB-PARTS: NONE

### C-7GA.7.3 — Continuous claim holding
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

ALONE
- What it is: DESIGNED — The requirement to retain exclusive OS locking across every job stage. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Takes in: DESIGNED — The acquired claim from startup to completed or cleanly failed work. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Does: DESIGNED — Holds the OS lock without interruption while all durable job operations execute. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gives out: DESIGNED — One concurrency authority throughout the claim. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Must never: DESIGNED — Release and reacquire between steps or let diagnostic expiry permit a second committer. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Fails closed by: DESIGNED — Another worker cannot acquire the live lock and therefore cannot process the job. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

TOGETHER
- Fed by: DESIGNED — C-7GA.7 — Full-job OS lock and claim: Applies the whole-duration lock contract. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.7 — Full-job OS lock and claim | Live exclusive lock. | Covers every durable operation. | No release/reacquire race. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 2 · DESIGNED | C-7GA.7.4 — Diagnostic claim renewal | Live processing state. | Updates expires_at diagnostically. | Renewal never replaces OS locking. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 3 · DESIGNED | C-7GA.7.1 — Lock claim metadata | `worker_id`, `claim_id`, `job_id`, `locked_at` and `expires_at`. | Proceeds only when the exclusive OS lock remains continuously held. | Nothing in this card. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 4 · DESIGNED | C-7GA.7.5 — Validate claim before durable work | The worker's held claim_id and the lock file's current claim_id. | Proceeds only when the exclusive OS lock remains continuously held. | Nothing in this card. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |

SUB-PARTS: NONE

### C-7GA.7.4 — Diagnostic claim renewal
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

ALONE
- What it is: DESIGNED — Periodic expiry renewal while the worker continues processing. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Takes in: DESIGNED — The live held claim and configured renewal/expiry values. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Does: DESIGNED — Updates expires_at in the lock file as a liveness signal. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gives out: DESIGNED — Fresh diagnostic metadata with unchanged OS-lock authority. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Must never: DESIGNED — Invent a fixed renewal interval or expiry window, or use renewal metadata to weaken locking. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7GA.7.3 — Continuous claim holding: Renews only while the worker continues under its held claim. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.7 — Full-job OS lock and claim | Current claim and configured interval. | Updates monitoring metadata. | No new concurrency authority. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |

SUB-PARTS: NONE

### C-7GA.7.5 — Validate claim before durable work
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

ALONE
- What it is: DESIGNED — The defensive same-claim condition on each durable job operation. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Takes in: DESIGNED — The worker's held claim_id and the lock file's current claim_id. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Does: DESIGNED — Requires equality before append_reading; idempotency lookups causing a commit; clash-record writes/updates; detection-history appends; no_clash_sentinel; view snapshot and no_update_sentinel writes; every job_stage_event, pass_lifecycle_event and job_status_event append. Instruction creation also performs the specified validation before its append. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gives out: DESIGNED — Claim-validated commits while the exclusive OS lock remains held. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Must never: DESIGNED — Perform any named durable operation with a mismatched claim or mistake metadata validation for concurrency exclusion. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Fails closed by: DESIGNED — No durable operation is authorized by a mismatched claim. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

TOGETHER
- Fed by: DESIGNED — C-7GA.7.1 — Lock claim metadata: Compares current lock metadata with the held claim. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gated by: DESIGNED — C-7GA.7.3 — Continuous claim holding: the exclusive OS lock remains continuously held. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.2 — job_status_event | Held and stored claim IDs. | Validates before commit. | No mismatched-claim transition. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 2 · DESIGNED | C-7GA.5.3 — job_stage_event | Held and stored claim IDs. | Validates before append. | No mismatched-claim progress record. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 3 · DESIGNED | C-7GA.7 — Full-job OS lock and claim | Held and recorded claim IDs. | Validates defensively before commit. | No mismatched-claim write. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 4 · DESIGNED | C-7GA.8 — Reading-pass instruction and log | Matching claim evidence. | Writes under the held lock. | No invalid-owner pass record. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 5 · DESIGNED | C-7GA.8.2 — pass_lifecycle_event | Matching held/stored claim identity. | Commits under the exclusive lock. | No invalid-owner terminal. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 6 · DESIGNED | C-7GA.9 — Job-level reading idempotency | Matching claim evidence. | Recovers under the exclusive lock. | No unowned checkpoint repair. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 7 · DESIGNED | C-7GA.11.1 — Step 1 — Create instruction | Matching claim identity. | Makes the instruction durable. | No unowned pass creation. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 8 · DESIGNED | C-7GA.11.5 — Step 5 — Idempotent quarantine reading write | Held/stored claim agreement. | Validates before each durable effect. | No mismatched-claim write. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 9 · DESIGNED | C-7GA.13.6 — RC-5 — Reading exists without completion records | Held/stored claim agreement. | Appends missing history safely. | No invalid-owner repair. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 10 · DESIGNED | C-7GA.5.3.3.1 — reading_written checkpoint | Its `reading_id`, recovered or freshly written. | Proceeds only when the processing claim is validated before this append. | Nothing in this card. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 11 · DESIGNED | C-7GA.5.3.3.2 — clash_detection_completed checkpoint | `clash_found` boolean, `clash_id` or null, and the exact operation_key. | Proceeds only when the processing claim is validated before this append. | Nothing in this card. | [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 12 · DESIGNED | C-7GA.8.1 — reading_pass_instruction | Its identity, job/target links, assigned mode, rule/version, assignment_inputs, trigger/reason, recovery link, schema version and creation time. | Proceeds only when the processing claim is validated before this append. | Nothing in this card. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |
| 13 · DESIGNED | C-7GA.8.2.3.1 — completed pass | The verified outcome_reading_id. | Proceeds only when the processing claim is validated before this append. | Nothing in this card. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 14 · DESIGNED | C-7GA.11.5.1 — Step 5A — Record reading checkpoint | The verified reading_id. | Proceeds only when the processing claim is validated before this append. | Nothing in this card. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 15 · DESIGNED | C-7GA.11.7.1 — Step 7A — Record clash checkpoint | clash_found, clash_id or null, and the clash operation_key. | Proceeds only when the processing claim is validated before this append. | Nothing in this card. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 16 · DESIGNED | C-7GA.11.7.3 — Step 7B checkpoint — Record complete profile accounting | The complete profile_results list, including an empty list when no profiles were triggered. | Proceeds only when the processing claim is validated before this append. | Nothing in this card. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 17 · DESIGNED | C-7GA.12.1 — no_clash_sentinel | The exact clash operation key, reading_id, job_id and timestamp. | Proceeds only when the processing claim is validated before this append. | Nothing in this card. | [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 18 · DESIGNED | C-7GA.12.2 — no_update_sentinel | The exact profile operation key, reading_id, job_id and timestamp. | Proceeds only when the processing claim is validated before this append. | Nothing in this card. | [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 19 · DESIGNED | C-7GA.13.4 — RC-3 — in_progress without instruction | The job and current derived assignment inputs. | Proceeds only when the processing claim is validated before this append. | Nothing in this card. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] |
| 20 · DESIGNED | C-7GA.13.5 — RC-4 — Interrupted instruction without lifecycle | An instruction without terminal event and the job-level reading idempotency key. | Proceeds only when the processing claim is validated before this append. | Nothing in this card. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] |
| 21 · DESIGNED | C-7GA.13.7 — RC-6 — Reading checkpoint without clash checkpoint | reading_written and the exact clash operation key. | Proceeds only when the processing claim is validated before this append. | Nothing in this card. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] |
| 22 · DESIGNED | C-7GA.13.8 — RC-7 — Clash checkpoint without complete view checkpoint | clash_detection_completed and each triggered profile's operation key. | Proceeds only when the processing claim is validated before this append. | Nothing in this card. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] |
| 23 · DESIGNED | C-7GA.13.9 — RC-8 — All checkpoints without job close | All three durable stage checkpoints. | Proceeds only when the processing claim is validated before this append. | Nothing in this card. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] |
| 24 · DESIGNED | C-7J.5.2 — Triggered-operation recovery boundary | `operation_key = {job_id}::{reading_id}::clash_detection`, the new reading, any previously committed result, and the worker's validated claim. | Gates this place: validates the held claim before every durable operation. | Nothing in this card. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS] |

SUB-PARTS: NONE

### C-7GA.7.6 — Claim release
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

ALONE
- What it is: DESIGNED — Clean release after completed work or handled technical failure, and automatic release after crash. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Takes in: DESIGNED — A completed job event, a handled technical pass failure with job in_progress, or process exit. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Does: DESIGNED — Releases the OS lock after terminal job completion and may delete the file then. Releases cleanly after a handled technical failure. On crash the OS releases the lock and stale metadata remains on disk. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gives out: DESIGNED — No live lock held by a completed, cleanly stopped or crashed process. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Must never: DESIGNED — Retain the lock after clean stop or treat remaining file existence alone as a live process claim. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Fails closed by: DESIGNED — Crash leaves stale metadata for controlled takeover rather than authority for blind processing. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

TOGETHER
- Fed by: DESIGNED — C-7GA.7 — Full-job OS lock and claim: Follows the owning completion/failure/crash release contract. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Fed by: DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): supplies the completed stage checkpoints before the claim is released (P-MAIN step 16). [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.7 — Full-job OS lock and claim | Actual terminal/stop state. | Ends live ownership. | Crash metadata remains recoverable. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |

SUB-PARTS: NONE

### C-7GA.7.7 — Stale-claim takeover
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

ALONE
- What it is: DESIGNED — Recovery acquisition of the existing lock file after the prior process no longer holds its OS lock. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Takes in: DESIGNED — The existing file with stale claim metadata. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Does: DESIGNED — Attempts non-blocking exclusive acquisition. On success reads the old metadata, overwrites with the new claim's worker_id, claim_id, job_id, locked_at and expires_at, appends claim_expired and a new job_claimed, then begins recovery. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gives out: DESIGNED — A new live claim with append-only old-to-new takeover history. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Must never: DESIGNED — Delete/re-create the file, use O_CREAT plus O_EXCL to force ownership or take over while another process holds its lock. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Fails closed by: DESIGNED — Failed acquisition means another holder remains; recovery exits without takeover. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7GA.7.2 — Claim acquisition: Takeover requires successful exclusive acquisition of the existing file. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.5 — claim_expired | Exact stale/new claim transition. | Records controlled replacement. | No expiry-only or delete/re-create takeover. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 2 · DESIGNED | C-7GA.7 — Full-job OS lock and claim | Stale metadata and successful acquisition. | Records controlled successor claim. | No delete/re-create shortcut. | [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |
| 3 · DESIGNED | C-7GA.13.3 — RC-2 — Claimed before in_progress | Acquired replacement claim. | Continues into RC-3. | No takeover while a live holder remains. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] |

SUB-PARTS: NONE

### C-7GA.8 — Reading-pass instruction and log
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

ALONE
- What it is: DESIGNED — `.nh_reading_pass_log.jsonl`, Full Protected append-only JSONL for instruction and outcome records. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Takes in: DESIGNED — Every successful, failed or abandoned pass attempt. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Does: DESIGNED — Writes one durable immutable instruction before Context Retrieval begins; appends terminal pass_lifecycle_event separately. Requires no production-marker gate because this log records instructions/outcomes rather than reading records. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Gives out: DESIGNED — Durable pass provenance distinct from queue job state. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Must never: DESIGNED — Begin retrieval before the instruction is durable, edit an instruction or treat logging as permission to write production readings. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fails closed by: DESIGNED — A pass cannot silently disappear from its instruction/outcome history. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

TOGETHER
- Fed by: DESIGNED — C-7GA.8.1 — reading_pass_instruction: Records one immutable instruction before retrieval. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fed by: DESIGNED — C-7GA.8.2 — pass_lifecycle_event: Records the pass terminal separately. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: Instruction and lifecycle appends follow claim validation. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | Pass identity, assignment and actual outcome. | Appends protected pass records. | Traceable attempt lifecycle. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: C-7GA.8.1 — reading_pass_instruction; C-7GA.8.2 — pass_lifecycle_event

### C-7GA.8.1 — reading_pass_instruction
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

ALONE
- What it is: DESIGNED — The immutable instruction entry governing one pass attempt. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Takes in: DESIGNED — Its identity, job/target links, assigned mode, rule/version, assignment_inputs, trigger/reason, recovery link, schema version and creation time. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Does: DESIGNED — Writes entry_type instruction once before retrieval. Derives classification/count inputs at creation time without adding fields to sealed roots. Links a replacement to its abandoned predecessor and retains the same job_id. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Gives out: DESIGNED — An exact reproducible mode-assignment and pass record. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Must never: DESIGNED — Mutate the instruction, add source_title_type to the sealed root schema or reuse a predecessor pass_id for a replacement attempt. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fails closed by: DESIGNED — Replacement work gets a new instruction and explicit recovery_of_pass_id. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

TOGETHER
- Fed by: DESIGNED — C-7GA.8.1.1 — Instruction entry_type: Carries the instruction discriminator. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fed by: DESIGNED — C-7GA.8.1.2 — Instruction pass_id: Carries a new uuid4 pass identity. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fed by: DESIGNED — C-7GA.8.1.3 — Instruction job_id: Links the owning queue job. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fed by: DESIGNED — C-7GA.8.1.4 — target_root_id: Names the target root. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fed by: DESIGNED — C-7GA.8.1.5 — assigned_mode: Carries the actually assigned permitted mode. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.8.1.6 — mode_rule_id: Records the governing rule identity. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.8.1.7 — mode_rule_version: Records rule version 1. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.8.1.8 — assignment_inputs: Records every actual assignment input and override result. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.8.1.9 — Instruction trigger_source: Records the actual trigger source. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fed by: DESIGNED — C-7GA.8.1.10 — assignment_reason: Records the assignment explanation and required warnings. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.8.1.11 — recovery_of_pass_id: Links a recovery replacement to its abandoned predecessor. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fed by: DESIGNED — C-7GA.8.1.12 — Instruction schema_version: Declares the fixed instruction schema. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fed by: DESIGNED — C-7GA.8.1.13 — Instruction created_at: Dates instruction creation. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fed by: DESIGNED — C-7GA.11.1 — Step 1 — Create instruction: Is made durable by the instruction-creation step. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: the processing claim is validated before this append. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8 — Reading-pass instruction and log | Pass identity and assignment inputs. | Preserves the exact attempt contract. | No unrecorded context pass. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |
| 2 · DESIGNED | C-7GA.11.2 — Step 2 — Retrieve context through LMAC | Recorded pass mode. | Selects bare or positional context. | No retrieval before the pass contract. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |
| 3 · DESIGNED | C-7GA.13.5 — RC-4 — Interrupted instruction without lifecycle | Abandoned pass reference and fresh mode inputs. | Writes the new instruction. | One operation retains its reading identity. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: C-7GA.8.1.1 — Instruction entry_type; C-7GA.8.1.2 — Instruction pass_id; C-7GA.8.1.3 — Instruction job_id; C-7GA.8.1.4 — target_root_id; C-7GA.8.1.5 — assigned_mode; C-7GA.8.1.6 — mode_rule_id; C-7GA.8.1.7 — mode_rule_version; C-7GA.8.1.8 — assignment_inputs; C-7GA.8.1.9 — Instruction trigger_source; C-7GA.8.1.10 — assignment_reason; C-7GA.8.1.11 — recovery_of_pass_id; C-7GA.8.1.12 — Instruction schema_version; C-7GA.8.1.13 — Instruction created_at

### C-7GA.8.1.1 — Instruction entry_type
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

ALONE
- What it is: DESIGNED — The instruction record discriminator. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Takes in: DESIGNED — Fixed value `instruction`. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Does: DESIGNED — Identifies this immutable pass instruction. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Gives out: DESIGNED — The exact entry_type. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Must never: DESIGNED — Use a different discriminator for the instruction entry. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1 — reading_pass_instruction | entry_type instruction. | Identifies the record. | Exact instruction family. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: NONE

### C-7GA.8.1.2 — Instruction pass_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

ALONE
- What it is: DESIGNED — The uuid4 identity of this pass attempt. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Takes in: DESIGNED — A newly assigned attempt ID. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Does: DESIGNED — Identifies the instruction and its terminal lifecycle event. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Gives out: DESIGNED — A stable pass reference also carried by produced_by.config.pass_id. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Must never: DESIGNED — Reuse an abandoned attempt's pass_id for its recovery replacement. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1 — reading_pass_instruction | pass_id. | Identifies this attempt. | Replacement attempts stay distinct. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: NONE

### C-7GA.8.1.3 — Instruction job_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

ALONE
- What it is: DESIGNED — The queue-job reference in the instruction. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Takes in: DESIGNED — The job that created the pass. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Does: DESIGNED — Links the instruction to that job across normal and replacement attempts. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Gives out: DESIGNED — Stable job-to-pass lineage. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Must never: DESIGNED — Change the owning job merely because a new recovery pass is needed. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1 — reading_pass_instruction | job_id. | Preserves job-to-pass lineage. | Recovery retains the same job. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: NONE

### C-7GA.8.1.4 — target_root_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

ALONE
- What it is: DESIGNED — The target-root reference in the pass instruction. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Takes in: DESIGNED — The root named by the owning job. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Does: DESIGNED — Records the target read by this attempt. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Gives out: DESIGNED — Target-specific pass provenance. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1 — reading_pass_instruction | target_root_id. | Records what is read. | Target-specific provenance. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: NONE

### C-7GA.8.1.5 — assigned_mode
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The instruction mode field with schema values bare, local-context, associative and combined. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — The outcome of the governing mode rule. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Stores the assigned reading mode; thread_membership_v1 permits only bare or local-context despite the wider schema vocabulary. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — An explicit pass mode. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Let this rule assign associative or combined merely because the schema lists them. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — A path producing either prohibited mode falls back to bare and records an implementation error. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1 — reading_pass_instruction | assigned_mode. | Declares the pass's reading mode. | Wider schema vocabulary grants no prohibited mode. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.8.1.6 — mode_rule_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The identity of the rule used to assign this new-root pass. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — `thread_membership_v1`. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Records the actual governing rule. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — Mode-assignment provenance. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Apply this new-root rule to a reread pass. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1 — reading_pass_instruction | mode_rule_id. | Binds assignment to thread_membership_v1. | No reread policy inferred. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.8.1.7 — mode_rule_version
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The mode-rule version recorded with the instruction. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — Rule version `1`. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Preserves the version governing this assignment. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — Version-specific mode provenance. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Relax this version's unconditional mode prohibition. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1 — reading_pass_instruction | mode_rule_version. | Preserves version-specific policy. | Its permanent prohibition remains. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.8.1.8 — assignment_inputs
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The object storing all derived inputs and override outcomes used for assignment. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — source_title_type, thread_present, thread_root_count, trigger_declared_mode, trigger_override_reason, override_accepted, override_rejected, override_source, override_declared_mode, override_rejection_reason and override_reason. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Captures the exact values at instruction creation, including accepted and rejected override outcomes. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — A durable account of why the rule chose its mode. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Use raw source_title text as the assignment decision or silently discard unrecognized input values. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — Unknown or missing grouping classification takes the safe bare default with its reason. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: DESIGNED — C-7GA.8.1.8.1 — source_title_type: Carries the derived grouping classification. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.8.1.8.2 — thread_present: Carries deterministic other-root presence. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.8.1.8.3 — thread_root_count: Carries the count excluding the target. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.8.1.8.4 — Assignment trigger_declared_mode: Captures the input mode declaration. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.8.1.8.5 — Assignment trigger_override_reason: Captures the actual trigger reason. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.8.1.8.6 — override_accepted: Records actual accepted-override outcome. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.8.1.8.7 — override_rejected: Records actual rejected-override outcome. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.8.1.8.8 — override_source: Records the override's source. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.8.1.8.9 — override_declared_mode: Records the evaluated declaration. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.8.1.8.10 — override_rejection_reason: Records why an override failed. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.8.1.8.11 — override_reason: Preserves the override's actual justification. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1 — reading_pass_instruction | assignment_inputs object. | Preserves reproducible reasoning inputs. | No raw-title mode guess. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
| 2 · DESIGNED | C-7GA.10 — thread_membership_v1 | Classification, counts and trigger values. | Assigns from those recorded inputs. | No raw-title decision or hidden input. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: C-7GA.8.1.8.1 — source_title_type; C-7GA.8.1.8.2 — thread_present; C-7GA.8.1.8.3 — thread_root_count; C-7GA.8.1.8.4 — Assignment trigger_declared_mode; C-7GA.8.1.8.5 — Assignment trigger_override_reason; C-7GA.8.1.8.6 — override_accepted; C-7GA.8.1.8.7 — override_rejected; C-7GA.8.1.8.8 — override_source; C-7GA.8.1.8.9 — override_declared_mode; C-7GA.8.1.8.10 — override_rejection_reason; C-7GA.8.1.8.11 — override_reason

### C-7GA.8.1.8.1 — source_title_type
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — A pass-local deterministic grouping classification derived through the Catalog source-title rule. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — The root's existing source_title and its established source grouping. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Records real_thread for a source-provided real thread, untitled_session for a confirmed grouping such as untitled:paste:<id>, singleton for an isolated item, or thread_unresolved for genuinely uncertain grouping. Records an unrecognized value as-is. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — The derived classification used with the count inputs. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Add this field to the sealed root record, infer mode from title text alone or invent grouping from a string match. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — Unrecognized, missing or uncertain grouping defaults to bare. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: DESIGNED — C-7E.8 — Source-title and thread resolution: Derives classification using the existing source-title/grouping rule. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1.8 — assignment_inputs | source_title_type. | Preserves confirmed/uncertain/unknown distinction. | No root-schema addition. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.8.1.8.2 — thread_present
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — A boolean from deterministic count lookup at assignment time. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — Other roots in the sealed store sharing the target's source_title. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Records whether at least one such other root exists. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — The rule's recorded grouping-presence input. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Treat title matching alone as confirmed grouping or silently replace this count input with a guessed semantic relationship. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — local-context still requires a confirmed grouping and the declared preceding-context condition. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1.8 — assignment_inputs | thread_present. | Records the count lookup finding. | Title matching alone is insufficient. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.8.1.8.3 — thread_root_count
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The integer count of other roots sharing the target's source_title, excluding the target. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — The deterministic store lookup at assignment time. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Records the count; it is zero when thread_present is false. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — A captured count input to the mode rule. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Count the target itself or silently redefine the source's other-root count as a different schema field. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — The local-context default requires thread_present true and count at least one with confirmed grouping. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1.8 — assignment_inputs | thread_root_count. | Preserves the actual derived count. | No target self-count. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.8.1.8.4 — Assignment trigger_declared_mode
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The trigger's declared mode captured in assignment_inputs. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — The actual declared value or null. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Preserves the input evaluated by the override gate. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — An inspectable declaration. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Treat recorded input as proof that the override was accepted. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1.8 — assignment_inputs | trigger_declared_mode. | Preserves the requested value. | Recording is not acceptance. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.8.1.8.5 — Assignment trigger_override_reason
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The trigger's justification captured in assignment_inputs. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — Its actual reason, including null or empty content. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Preserves the value used by the live-ingestion narrowing gate. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — Override-input provenance. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Replace an absent reason with a fabricated one to obtain acceptance. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — Null or empty reason cannot authorize a live_ingestion bare override. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1.8 — assignment_inputs | trigger_override_reason. | Preserves narrowing justification. | Missing reasons are not invented. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.8.1.8.6 — override_accepted
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The recorded accepted-override result. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — The actual source-specific override-gate outcome. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Records acceptance when that gate permits the requested override. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — A durable accepted-override trace. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Mark a disallowed override accepted. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1.8 — assignment_inputs | override_accepted. | Preserves gate success. | No disallowed acceptance. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.8.1.8.7 — override_rejected
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The recorded rejected-override result. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — The actual rejected declaration. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Preserves the rejection before default assignment proceeds. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — A durable rejection trace. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Silently omit a rejected override. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — Rejection proceeds to the default step rather than accepting the declaration. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1.8 — assignment_inputs | override_rejected. | Preserves the rejection. | Default follows honestly. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.8.1.8.8 — override_source
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The source classification associated with the evaluated override. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — The requesting trigger source. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Records which source's override rules applied. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — Source-specific override provenance. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1.8 — assignment_inputs | override_source. | Identifies the applied source rule. | Source-specific provenance. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.8.1.8.9 — override_declared_mode
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The declaration recorded as part of the override outcome. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — The actual requested mode. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Preserves which declaration was accepted or rejected. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — An exact override-outcome reference. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1.8 — assignment_inputs | override_declared_mode. | Identifies accepted/rejected request. | Exact request lineage. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.8.1.8.10 — override_rejection_reason
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The reason recorded when an override is rejected. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — The actual disallowed source, mode, missing reason or unrecognized-value condition. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Records why the override did not pass. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — Distinct rejection reasoning alongside default assignment. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Hide the rejected override's cause. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1.8 — assignment_inputs | override_rejection_reason. | Preserves the actual cause. | No hidden rejection. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.8.1.8.11 — override_reason
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The reason field retained with the override result. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — The actual reason associated with that override evaluation. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Preserves its justification in assignment_inputs. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — Inspectable override reasoning. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Invent a justification absent from the trigger and rule evaluation. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1.8 — assignment_inputs | override_reason. | Records its reasoning. | No invented justification. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.8.1.9 — Instruction trigger_source
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The triggering-process field on the instruction. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — The job's actual trigger_source. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Preserves the source used by mode assignment. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — Pass-level trigger provenance. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Treat a reread_trigger as permission to use the new-root mode rule for rereads. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — Reread-trigger misuse takes the specified rejection/warning path. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1 — reading_pass_instruction | trigger_source. | Preserves trigger provenance. | A label grants no activation permission. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: NONE

### C-7GA.8.1.10 — assignment_reason
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The explanation of the final mode assignment. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — The override/default rule's actual finding, including any configuration warning. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Records why the chosen mode was assigned; a reread_trigger with null declared mode records its configuration warning here. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — Inspectable assignment reasoning. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Silently suppress a rule-required warning or implementation error. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — Unrecognized/missing grouping yields bare with its safe-fallback reason. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1 — reading_pass_instruction | assignment_reason. | Explains the chosen mode. | No silent warning suppression. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.8.1.11 — recovery_of_pass_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]

ALONE
- What it is: DESIGNED — The predecessor link for a replacement recovery instruction. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Takes in: DESIGNED — An abandoned interrupted pass_id, or null on a first attempt. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Does: DESIGNED — Records which pass this new instruction replaces while keeping the same job_id and assigning a new pass_id. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Gives out: DESIGNED — Explicit recovery lineage. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Must never: DESIGNED — Overwrite the abandoned instruction or repurpose this field as the reading idempotency key. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1 — reading_pass_instruction | recovery_of_pass_id or initial null. | Preserves attempt lineage. | No predecessor overwrite. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE] |

SUB-PARTS: NONE

### C-7GA.8.1.12 — Instruction schema_version
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

ALONE
- What it is: DESIGNED — The instruction schema identifier. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Takes in: DESIGNED — Fixed value `rpi_v1`. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Does: DESIGNED — Records the declared instruction schema version. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Gives out: DESIGNED — Versioned instruction shape. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Must never: DESIGNED — Use an unadopted instruction schema identifier in place of rpi_v1. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1 — reading_pass_instruction | rpi_v1. | Versions the record shape. | No silent schema substitution. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: NONE

### C-7GA.8.1.13 — Instruction created_at
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

ALONE
- What it is: DESIGNED — The instruction creation time. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Takes in: DESIGNED — The time this pass instruction is created. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Does: DESIGNED — Dates the immutable entry. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Gives out: DESIGNED — Timed pass provenance. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1 — reading_pass_instruction | created_at. | Records attempt timing. | Timed pass provenance. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: NONE

### C-7GA.8.2 — pass_lifecycle_event
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

ALONE
- What it is: DESIGNED — The appended terminal record for one pass attempt. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Takes in: DESIGNED — entry_type, pass_id, event_type, event_at, outcome_reading_id, failure_outcome or null, and abandonment_reason. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Does: DESIGNED — Records completed, failed or abandoned separately from the queue's job status. A completed pass names its reading; failures retain stage, reason, proposal-preservation and technical classification. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Gives out: DESIGNED — A durable attempt terminal. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Must never: DESIGNED — Mutate the instruction or equate a completed reading pass with a fully completed queue job. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fails closed by: DESIGNED — Actual failures remain failed with their classification; recovery abandonment precedes a replacement pass. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

TOGETHER
- Fed by: DESIGNED — C-7GA.8.2.1 — Lifecycle entry_type: Carries the lifecycle discriminator. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fed by: DESIGNED — C-7GA.8.2.2 — Lifecycle pass_id: Names the actual closing attempt. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fed by: DESIGNED — C-7GA.8.2.3 — Pass event_type: Records completed, failed or abandoned distinctly. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fed by: DESIGNED — C-7GA.8.2.4 — Lifecycle event_at: Dates the terminal event. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fed by: DESIGNED — C-7GA.8.2.5 — outcome_reading_id: Completed events name the durable reading. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fed by: DESIGNED — C-7GA.8.2.6 — failure_outcome: Preserves the failure object or null. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fed by: DESIGNED — C-7GA.8.2.7 — abandonment_reason: Explains an abandoned interruption. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: Every lifecycle append requires defensive claim validation. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8 — Reading-pass instruction and log | Actual outcome and failure/abandonment detail. | Closes the attempt without editing instruction. | Queue state stays separate. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |
| 2 · DESIGNED | C-7GA.11.6 — Step 6 — Close instruction | Actual reading ID and matching claim. | Closes the instruction. | Queue state remains independent. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: C-7GA.8.2.1 — Lifecycle entry_type; C-7GA.8.2.2 — Lifecycle pass_id; C-7GA.8.2.3 — Pass event_type; C-7GA.8.2.4 — Lifecycle event_at; C-7GA.8.2.5 — outcome_reading_id; C-7GA.8.2.6 — failure_outcome; C-7GA.8.2.7 — abandonment_reason

### C-7GA.8.2.1 — Lifecycle entry_type
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

ALONE
- What it is: DESIGNED — The pass-terminal record discriminator. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Takes in: DESIGNED — Fixed value `pass_lifecycle_event`. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Does: DESIGNED — Identifies the appended lifecycle entry. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Gives out: DESIGNED — The exact entry_type. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Must never: DESIGNED — Use a different discriminator for a pass lifecycle event. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.2 — pass_lifecycle_event | entry_type pass_lifecycle_event. | Identifies the terminal record. | Exact record family. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: NONE

### C-7GA.8.2.2 — Lifecycle pass_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

ALONE
- What it is: DESIGNED — The reference to the instruction whose attempt is closing. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Takes in: DESIGNED — The exact pass_id. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Does: DESIGNED — Binds the terminal event to that attempt. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Gives out: DESIGNED — Pass-specific outcome history. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Must never: DESIGNED — Attribute the terminal to a replacement pass instead of its actual predecessor. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.2 — pass_lifecycle_event | pass_id. | Links its terminal. | No predecessor/replacement confusion. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: NONE

### C-7GA.8.2.3 — Pass event_type
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]

ALONE
- What it is: DESIGNED — The three-value terminal enum for a pass. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Takes in: DESIGNED — `completed`, `failed` or `abandoned`. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Does: DESIGNED — Preserves completion with reading ID, failure with its actual class, or abandonment before an interrupted attempt is replaced. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Gives out: DESIGNED — The attempt's terminal state. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Must never: DESIGNED — Relabel handled failure as a crash-interrupted attempt or rewrite an earlier terminal as later success. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fails closed by: DESIGNED — Handled technical failure does not enter automatic crash replacement. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]

TOGETHER
- Fed by: DESIGNED — C-7GA.8.2.3.1 — completed pass: completed requires a durable reading result. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fed by: DESIGNED — C-7GA.8.2.3.2 — failed pass: failed preserves actual stage and retry classification. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fed by: DESIGNED — C-7GA.8.2.3.3 — abandoned pass: abandoned preserves an interrupted predecessor before replacement. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.2 — pass_lifecycle_event | event_type. | Preserves the actual terminal class. | No automatic failure-to-crash relabel. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: C-7GA.8.2.3.1 — completed pass; C-7GA.8.2.3.2 — failed pass; C-7GA.8.2.3.3 — abandoned pass

### C-7GA.8.2.3.1 — completed pass
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The terminal of a pass whose reading durably exists. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — The verified outcome_reading_id. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Appends completed after claim validation; the queue job still remains in_progress for post-reading work. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — A closed instruction linked to its reading. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Close the queue job solely because this pass is completed. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — A reading must exist before completion can name it. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7GA.11.6 — Step 6 — Close instruction: Follows the explicit instruction-close step. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: the processing claim is validated before this append. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.2.3 — Pass event_type | Verified reading_id. | Closes the pass. | Job stays open for post-reading work. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: NONE

### C-7GA.8.2.3.2 — failed pass
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The terminal of a pass that fails at its actual stage. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — failure_stage, failure_reason, proposal_preserved and is_technical_and_potentially_retryable. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Records the distinction between potentially retryable technical failure and substantive rejection. Preserves the queue's class-correct separate state. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — A failed attempt with its exact reason and retry classification. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Conceal the failure, merge technical and substantive causes or assume retry permission from the technical flag alone. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — Technical handling stops and releases the lock; substantive rejection terminates the job under the stated worker rule. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7GA.11 — Worker pass sequence: Uses the actual failing worker stage's prescribed handling. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.2.3 — Pass event_type | Failure outcome object. | Closes the failed attempt. | Queue state remains class-correct. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: NONE

### C-7GA.8.2.3.3 — abandoned pass
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]

ALONE
- What it is: DESIGNED — The terminal of an interrupted instruction being replaced after recovery proves no reading exists. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Takes in: DESIGNED — The interrupted pass and its idempotency lookup proving no reading for the operation. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Does: DESIGNED — Appends abandoned with the reason `interrupted by shutdown or crash; replaced by recovery pass`, then creates a new instruction linked by recovery_of_pass_id. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Gives out: DESIGNED — Preserved abandoned-attempt history and explicit replacement lineage. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Must never: DESIGNED — Abandon on a missing checkpoint alone or create the replacement before terminally recording the interrupted pass. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fails closed by: DESIGNED — If a reading exists, recovery restores its checkpoints instead of re-reading. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7GA.13.5 — RC-4 — Interrupted instruction without lifecycle: Requires the interrupted-pass branch to prove no keyed reading exists. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.2.3 — Pass event_type | No-reading lookup and abandonment reason. | Closes the old instruction. | Recovery uses a new pass identity. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |
| 2 · DESIGNED | C-7GA.13.5 — RC-4 — Interrupted instruction without lifecycle | Interrupted pass and exact reason. | Closes the predecessor. | Recovery lineage remains explicit. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] |

SUB-PARTS: NONE

### C-7GA.8.2.4 — Lifecycle event_at
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

ALONE
- What it is: DESIGNED — The pass-terminal event time. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Takes in: DESIGNED — The actual terminal record time. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Does: DESIGNED — Dates the completion, failure or abandonment event. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Gives out: DESIGNED — Timed attempt history. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.2 — pass_lifecycle_event | event_at. | Preserves event timing. | Timed outcome history. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: NONE

### C-7GA.8.2.5 — outcome_reading_id
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

ALONE
- What it is: DESIGNED — The reading reference present on a completed lifecycle event. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Takes in: DESIGNED — The reading produced or recovered for the operation. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Does: DESIGNED — Records its ID when event_type is completed. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Gives out: DESIGNED — Exact completed-pass result linkage. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Must never: DESIGNED — Claim completion through a reading ID that has no durable result. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.2 — pass_lifecycle_event | outcome_reading_id. | Links actual success. | No invented result reference. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: NONE

### C-7GA.8.2.6 — failure_outcome
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

ALONE
- What it is: DESIGNED — The failure-detail object, or null, in the lifecycle event. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Takes in: DESIGNED — failure_stage, failure_reason, proposal_preserved and is_technical_and_potentially_retryable for an actual failure. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Does: DESIGNED — Preserves the failure location, cause, audit-preservation fact and technical/substantive distinction. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Gives out: DESIGNED — Machine-readable failure provenance. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Must never: DESIGNED — Replace distinct failure causes with a generic success or classify acceptance rejection as technical recovery. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fails closed by: DESIGNED — The recorded class governs the separate job/recovery treatment. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

TOGETHER
- Fed by: DESIGNED — C-7GA.8.2.6.1 — failure_stage: Identifies the actual failing stage. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fed by: DESIGNED — C-7GA.8.2.6.2 — failure_reason: Preserves the distinct failure cause. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fed by: DESIGNED — C-7GA.8.2.6.3 — proposal_preserved: Records actual audit preservation. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fed by: DESIGNED — C-7GA.8.2.6.4 — is_technical_and_potentially_retryable: Records the technical/substantive distinction. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.2 — pass_lifecycle_event | failure_outcome. | Records stage, reason and classification. | No hidden or generic false success. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: C-7GA.8.2.6.1 — failure_stage; C-7GA.8.2.6.2 — failure_reason; C-7GA.8.2.6.3 — proposal_preserved; C-7GA.8.2.6.4 — is_technical_and_potentially_retryable

### C-7GA.8.2.6.1 — failure_stage
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The failing-stage identifier. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — The actual stage, including `context_retrieval`, `mouth_proposal`, `acceptance_check` or `write` on the specified pass-failure paths. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Records where the pass failed. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — Stage-specific recovery/diagnostic provenance. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Invent a successful later stage after this failure. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.2.6 — failure_outcome | failure_stage. | Preserves its location. | No invented later success. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: NONE

### C-7GA.8.2.6.2 — failure_reason
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The specific cause of the recorded pass failure. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — The actual system failure or distinct acceptance-rejection reason. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Preserves that cause separately from insufficient context. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — Inspectable failure reasoning. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Relabel fabrication, mode violation or malformed output as context insufficiency. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.2.6 — failure_outcome | failure_reason. | Records actual rejection/system reason. | No insufficiency relabeling. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: NONE

### C-7GA.8.2.6.3 — proposal_preserved
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

ALONE
- What it is: DESIGNED — The boolean recording whether the failed proposal was preserved for audit. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Takes in: DESIGNED — The actual proposal-preservation state. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Does: DESIGNED — Records whether the proposal remains in its audit context. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Gives out: DESIGNED — Honest preservation provenance. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Must never: DESIGNED — Treat a preserved rejected proposal as an accepted reading. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.2.6 — failure_outcome | proposal_preserved. | Retains that boolean fact. | Rejected content stays rejected. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: NONE

### C-7GA.8.2.6.4 — is_technical_and_potentially_retryable
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / CRASH RECOVERY SEQUENCE]

ALONE
- What it is: DESIGNED — The boolean `failure_outcome.is_technical_and_potentially_retryable`, distinguishing a potentially retryable system failure from substantive rejection. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Takes in: DESIGNED — The actual failure classification. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Does: DESIGNED — Records true for the stated retrieval, mouth or write technical failures; false for substantive acceptance rejection. A true failed lifecycle event excludes that job from crash-replacement handling. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Gives out: DESIGNED — Explicit routing evidence for the retry/recovery boundary. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Must never: DESIGNED — Infer a retry authorization from true alone or automatically replay a handled technical failure as if it were a crash. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fails closed by: DESIGNED — The worker releases the lock and leaves a technically failed job in_progress pending its governed retry path. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / CRASH RECOVERY SEQUENCE]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.2.6 — failure_outcome | is_technical_and_potentially_retryable. | Supplies recovery exclusion evidence. | Technical flag is not retry admission. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |
| 2 · DESIGNED | C-7GA.13.1 — Handled technical failure exclusion | failed lifecycle with true technical flag. | Releases and skips this candidate. | No replacement pass through RC-4. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |

SUB-PARTS: NONE

### C-7GA.8.2.7 — abandonment_reason
Stamp: DESIGNED    Source: [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]

ALONE
- What it is: DESIGNED — The reason recorded when an interrupted pass is abandoned. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Takes in: DESIGNED — The actual interruption and recovery replacement finding. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Does: DESIGNED — Records `interrupted by shutdown or crash; replaced by recovery pass` for the specified RC-4 branch. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Gives out: DESIGNED — Explicit abandonment provenance. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Must never: DESIGNED — Omit the predecessor's terminal explanation before creating its replacement. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.2 — pass_lifecycle_event | abandonment_reason. | Records replacement provenance. | Predecessor closes before replacement. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / CRASH RECOVERY SEQUENCE] |

SUB-PARTS: NONE

### C-7GA.9 — Job-level reading idempotency
Stamp: DESIGNED    Source: [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]

ALONE
- What it is: DESIGNED — Stable reading identity across all attempts of one new-root operation, including accidental duplicate jobs. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]
- Takes in: DESIGNED — The deterministic enqueue_key, not random job_id. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]
- Does: DESIGNED — Computes `reading_idempotency_key = stable_hash(enqueue_key + "reading_v1")` and passes it into the existing reading-record field `idempotency_key`. Keeps produced_by.config.pass_id as separate attempt provenance. Before a recovery write, finds an existing reading by this key, recovers its reading_id and restores missing checkpoints without rewriting the reading. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]
- Gives out: DESIGNED — At most one committed reading for the new-root operation and recoverable pass provenance. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]
- Must never: DESIGNED — Derive the key from random job_id, add a thirteenth reading field, rewrite an existing reading or alter recovery_of_pass_id to replace the key. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]
- Fails closed by: DESIGNED — An existing keyed reading is recovered rather than written again. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]

TOGETHER
- Fed by: DESIGNED — C-7GA.5.1.3 — Job enqueue_key: Derives reading identity from deterministic enqueue_key. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: Idempotency recovery causing a commit requires claim validation. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Changes: DESIGNED — C-READ.1.12 — reading.idempotency_key: Supplies the worker value to the existing idempotency_key field. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | Stable enqueue-derived reading key. | Recovers existing readings before writing. | No duplicate reading on restart. | [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] |
| 2 · DESIGNED | C-7GA.11.5 — Step 5 — Idempotent quarantine reading write | Stable reading identity. | Recovers an existing reading or writes once. | No duplicate across attempts. | [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 3 · DESIGNED | C-7GA.13.5 — RC-4 — Interrupted instruction without lifecycle | Exact keyed reading lookup. | Branches on proven durable result. | Missing checkpoint does not prove absence. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] |
| 4 · DESIGNED | C-7GA.13.6 — RC-5 — Reading exists without completion records | Recovered reading_id. | Repairs missing records only. | No rewritten reading. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] |

SUB-PARTS: NONE

### C-7GA.10 — thread_membership_v1
Stamp: DESIGNED    Source: [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The deterministic new-root mode-assignment rule, rule_id thread_membership_v1 and rule_version 1. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — Derived source_title_type, thread_present and thread_root_count, plus trigger_source, trigger_declared_mode and trigger_override_reason at instruction creation. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Runs the source-specific override gate first. An accepted override stops assignment; otherwise runs the grouping default. Records inputs, every accepted/rejected override and assignment_reason. Uses source_title only as a grouping key, never its raw string as the mode decision. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — bare or local-context with reproducible rule and input provenance. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Assign associative or combined under this version, use title matching alone as confirmed grouping or apply this rule to rereads. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — Any path producing a prohibited mode falls back to bare and records the implementation error; unknown grouping takes the safe bare default. [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: DESIGNED — C-7GA.8.1.8 — assignment_inputs: Uses the derived inputs captured at instruction creation. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.10.1 — Override gate: Evaluates overrides before defaults. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.10.2 — Grouping context default: Uses the grouping default only after no override was accepted. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): supplies the derived assignment inputs and trigger (P-MAIN step 7). [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gated by: DESIGNED — C-7GA.10.3 — Permanent associative and combined prohibition: Associative and combined are permanently prohibited under this version. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | Trigger and derived grouping/count inputs. | Assigns bare or local-context. | No associative/combined mode under version 1. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
| 2 · DESIGNED | C-7GA.10.1 — Override gate | Exact recorded trigger inputs. | Stops only on accepted override. | All outcomes remain recorded. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
| 3 · DESIGNED | C-7GA.10.3 — Permanent associative and combined prohibition | Proposed assigned mode. | Converts prohibited path to bare and records error. | No exception for associative/combined. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
| 4 · DESIGNED | C-7GA.11.1 — Step 1 — Create instruction | Derived grouping/count and trigger inputs. | Creates the declared pass. | No prohibited mode or raw-title guess. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
| 5 · DESIGNED | C-7F.2 — Conceptual channel combinations | The explicitly designed reading mode. | Gates this place: new-root use still follows the job's mode restrictions. | Nothing in this card. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: C-7GA.10.1 — Override gate; C-7GA.10.2 — Grouping context default; C-7GA.10.3 — Permanent associative and combined prohibition

### C-7GA.10.1 — Override gate
Stamp: DESIGNED    Source: [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The first mode-assignment step, before any context default. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — The triggering process's source, declared mode and reason. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Applies the five source-specific cases; records both acceptance and rejection outcomes. An accepted override fixes the mode; a rejection proceeds to the default. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — An accepted bare/local-context override or a recorded rejection followed by Step 2. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Accept a declaration outside its source-specific allowance or silently discard a rejected override. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — Disallowed or unrecognized requests are rejected and do not determine the mode. [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: DESIGNED — C-7GA.10.1.1 — Manual new-root override: Applies the manual-source allowance. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.10.1.2 — Live-ingestion narrowing override: Applies the live-ingestion narrowing condition. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.10.1.3 — Nightly-batch override rejection: Rejects nightly-source declared overrides. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.10.1.4 — Reread-trigger scope rejection: Preserves reread-trigger scope rejection/warning. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.10.1.5 — Unrecognized-source override rejection: Rejects unknown-source declarations. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.10 — thread_membership_v1: Runs as the rule's first step. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.10 — thread_membership_v1 | Actual source/mode/reason. | Accepts only the permitted override. | Rejection continues to Step 2. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
| 2 · DESIGNED | C-7GA.10.1.1 — Manual new-root override | Manual source and declared value. | Evaluates the two allowed modes. | Rejection preserves default routing. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
| 3 · DESIGNED | C-7GA.10.1.2 — Live-ingestion narrowing override | Live source, mode and reason. | Requires bare plus non-empty reason. | No widened context override. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
| 4 · DESIGNED | C-7GA.10.1.3 — Nightly-batch override rejection | Nightly declaration. | Records rejection and continues. | No implied activation. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
| 5 · DESIGNED | C-7GA.10.1.4 — Reread-trigger scope rejection | Reread trigger and declaration state. | Records rejection or the null-declaration warning. | Separate reread policy remains required. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
| 6 · DESIGNED | C-7GA.10.1.5 — Unrecognized-source override rejection | Unknown source and declared value. | Records rejection. | No assumed manual authority. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
| 7 · DESIGNED | C-7GA.10.2 — Grouping context default | Recorded override outcome. | Applies the grouping cases. | Accepted override already fixes the mode. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: C-7GA.10.1.1 — Manual new-root override; C-7GA.10.1.2 — Live-ingestion narrowing override; C-7GA.10.1.3 — Nightly-batch override rejection; C-7GA.10.1.4 — Reread-trigger scope rejection; C-7GA.10.1.5 — Unrecognized-source override rejection

### C-7GA.10.1.1 — Manual new-root override
Stamp: DESIGNED    Source: [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The override case for trigger_source manual. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — The requested new-root mode. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Accepts bare or local-context; rejects associative, combined and any unrecognized value. Acceptance stops assignment; rejection continues to the default. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — Recorded manual override outcome. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Accept associative, combined or an unrecognized manual mode under this rule. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — Invalid manual declarations are rejected. [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: DESIGNED — C-7GA.10.1 — Override gate: Uses the source-specific first-step rule. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.10.1 — Override gate | Manual declared mode. | Accepts bare/local-context only. | Invalid requests fall through to default. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.10.1.2 — Live-ingestion narrowing override
Stamp: DESIGNED    Source: [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The override case for trigger_source live_ingestion. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — A declared mode and trigger_override_reason. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Accepts only bare with a non-empty reason, narrowing context use. Rejects bare with null/empty reason and every other mode. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — A recorded narrowing override or rejection followed by the default. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Widen live-ingestion retrieval through an override or accept a missing-reason narrowing. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — A missing reason or non-bare mode fails the override gate. [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: DESIGNED — C-7GA.10.1 — Override gate: Uses the rule's narrowing-only live case. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.10.1 — Override gate | bare request and non-empty reason. | Allows only justified narrowing. | Other overrides fail. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.10.1.3 — Nightly-batch override rejection
Stamp: DESIGNED    Source: [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The rule's treatment of trigger_source nightly_batch. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — Any declared mode from that source. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Rejects the declared override and proceeds to the default step. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — A recorded rejection without nightly activation permission. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Treat nightly_batch's recognized name as an accepted override or an activation decision. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — No nightly declared mode passes this override gate. [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: DESIGNED — C-7GA.10.1 — Override gate: Uses the rule's nightly-source rejection. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.10.1 — Override gate | nightly_batch request. | Continues to the default. | No activation permission. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.10.1.4 — Reread-trigger scope rejection
Stamp: DESIGNED    Source: [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — Detection of a reread trigger presented to the new-root assignment rule. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — trigger_source reread_trigger with a declared mode or null. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Rejects every declared override. When the declaration is null, records a configuration warning in assignment_reason. Proceeds to Step 2 within the stated rule behavior without adopting this rule for rereads. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — A recorded rejection/warning preserving the separate reread-mode owner. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Use thread_membership_v1 as the reread mode policy. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — No reread declared override is accepted here. [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: DESIGNED — C-7GA.10.1 — Override gate: Uses the rule's new-root scope boundary. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.10.1 — Override gate | Reread declaration or null. | Records the actual misuse. | New-root rule does not become reread policy. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.10.1.5 — Unrecognized-source override rejection
Stamp: DESIGNED    Source: [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The override case for an unrecognized trigger_source. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — Any declared mode associated with that source. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Rejects the override and proceeds to the default. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — Explicit source/mode rejection provenance. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Treat an unknown trigger source as manual or otherwise authorize its declaration by guessing. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — The unrecognized-source override cannot pass. [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: DESIGNED — C-7GA.10.1 — Override gate: Uses the unknown-source rejection rule. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.10.1 — Override gate | Unrecognized trigger and mode. | Continues to default. | No guessed override authority. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.10.2 — Grouping context default
Stamp: DESIGNED    Source: [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — Step 2, reached only when Step 1 did not accept an override. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — The recorded grouping classification and deterministic count inputs. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Chooses local-context only for real_thread or untitled_session with thread_present true and thread_root_count at least 1, under the stated preceding-root condition. First roots, singleton, uncertain and missing/unrecognized classifications choose bare with their distinct reasons. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — A safe default mode with its assignment_reason. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Infer confirmed grouping solely from a matching title string or allow associative/combined through the default. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — Unsupported grouping falls back to bare. [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: DESIGNED — C-7GA.10.2.1 — Confirmed real-thread context: Confirmed real-thread context can select local-context. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.10.2.2 — First real-thread root: First real-thread root selects bare. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.10.2.3 — Confirmed untitled-session context: Confirmed untitled-session context can select local-context. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.10.2.4 — First untitled-session root: First untitled-session root selects bare. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.10.2.5 — Singleton default: Singleton selects bare. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.10.2.6 — Unresolved-thread default: Unresolved grouping selects bare. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DESIGNED — C-7GA.10.2.7 — Missing or unrecognized classification default: Missing/unknown grouping selects bare with review reason. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gated by: DESIGNED — C-7GA.10.1 — Override gate: Runs only if no override was accepted. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.10 — thread_membership_v1 | Confirmed grouping and count inputs. | Assigns the safe default. | No title-only local-context mode. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
| 2 · DESIGNED | C-7GA.10.2.1 — Confirmed real-thread context | Exact classification and count inputs. | Chooses local-context only on the stated case. | No string-match shortcut. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
| 3 · DESIGNED | C-7GA.10.2.2 — First real-thread root | Confirmed real group without other roots. | Chooses bare. | No fictional preceding turn. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
| 4 · DESIGNED | C-7GA.10.2.3 — Confirmed untitled-session context | Exact session and count inputs. | Chooses local-context on the stated case. | No unconfirmed grouping. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
| 5 · DESIGNED | C-7GA.10.2.4 — First untitled-session root | Confirmed session without other roots. | Chooses bare. | No fictional preceding context. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
| 6 · DESIGNED | C-7GA.10.2.5 — Singleton default | singleton classification. | Chooses bare. | No unrelated positional import. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
| 7 · DESIGNED | C-7GA.10.2.6 — Unresolved-thread default | thread_unresolved. | Chooses bare. | Uncertainty does not authorize context. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
| 8 · DESIGNED | C-7GA.10.2.7 — Missing or unrecognized classification default | Actual unknown input. | Chooses bare with the recorded review reason. | No guessed classification. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: C-7GA.10.2.1 — Confirmed real-thread context; C-7GA.10.2.2 — First real-thread root; C-7GA.10.2.3 — Confirmed untitled-session context; C-7GA.10.2.4 — First untitled-session root; C-7GA.10.2.5 — Singleton default; C-7GA.10.2.6 — Unresolved-thread default; C-7GA.10.2.7 — Missing or unrecognized classification default

### C-7GA.10.2.1 — Confirmed real-thread context
Stamp: DESIGNED    Source: [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The default case for an established source-provided real thread with context. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — source_title_type real_thread, thread_present true and thread_root_count at least 1. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Assigns local-context, recording confirmed real thread with at least one preceding root. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — A positional-context mode for that confirmed grouping. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Assign this default from a title match without confirmed grouping and the required context condition. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — Without the stated conditions this local-context branch is unavailable. [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: DESIGNED — C-7GA.10.2 — Grouping context default: Uses the confirmed-group/context default condition. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.10.2 — Grouping context default | real_thread, true presence and count at least one. | Records the preceding-context reason. | All declared conditions remain required. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.10.2.2 — First real-thread root
Stamp: DESIGNED    Source: [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The confirmed real-thread case with no other grouped root present. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — source_title_type real_thread and thread_present false. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Assigns bare, recording confirmed real thread but first root with no preceding context. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — An honestly context-free default. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Invent preceding context for the first root. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — Returns bare. [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: DESIGNED — C-7GA.10.2 — Grouping context default: Uses the first-real-root default. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.10.2 — Grouping context default | real_thread with false presence. | Records no preceding context. | No invented background. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.10.2.3 — Confirmed untitled-session context
Stamp: DESIGNED    Source: [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The default case for a confirmed untitled-session grouping with context. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — source_title_type untitled_session, thread_present true and thread_root_count at least 1. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Assigns local-context, recording confirmed untitled-session grouping with at least one preceding root. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — A positional-context mode for the confirmed grouping. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Substitute an arbitrary untitled label for established grouping evidence. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — Missing required grouping/context conditions cannot authorize this branch. [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: DESIGNED — C-7GA.10.2 — Grouping context default: Uses the confirmed-session/context default. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.10.2 — Grouping context default | Confirmed session, true presence and count at least one. | Records the preceding-context reason. | No arbitrary untitled grouping. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.10.2.4 — First untitled-session root
Stamp: DESIGNED    Source: [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The confirmed untitled-session case without other grouped roots. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — source_title_type untitled_session and thread_present false. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Assigns bare, recording that this is the first root in that grouping. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — An honest target-only default. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Invent preceding context for the first grouped root. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — Returns bare. [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: DESIGNED — C-7GA.10.2 — Grouping context default: Uses the first-session-root default. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.10.2 — Grouping context default | Confirmed session with false presence. | Records first-root reason. | No invented context. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.10.2.5 — Singleton default
Stamp: DESIGNED    Source: [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The default for an isolated item with no grouping. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — source_title_type singleton. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Assigns bare with the isolated-item reason. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — No unrelated positional context. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Treat the isolated item as a confirmed thread. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — Returns bare. [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: DESIGNED — C-7GA.10.2 — Grouping context default: Uses the isolated-item default. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.10.2 — Grouping context default | Isolated-item classification. | Records no grouping. | No unrelated context. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.10.2.6 — Unresolved-thread default
Stamp: DESIGNED    Source: [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The safe default where grouping is genuinely uncertain. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — source_title_type thread_unresolved. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Assigns bare with the uncertain-grouping reason, preventing unrelated positional context. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — A target-only pass without guessed grouping. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Resolve uncertain grouping by title similarity or import unrelated turns. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — Returns bare. [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: DESIGNED — C-7GA.10.2 — Grouping context default: Uses the uncertain-grouping default. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.10.2 — Grouping context default | thread_unresolved. | Records uncertainty. | No guessed thread. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.10.2.7 — Missing or unrecognized classification default
Stamp: DESIGNED    Source: [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The fallback for absent or unknown source_title_type. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — The missing value or unrecognized value recorded as-is. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Assigns bare and records the safe-fallback reason that the pass should be reviewed. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — An honestly limited mode with review-signaling provenance. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Guess a recognized grouping class or silently erase the unknown value. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — Returns bare. [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: DESIGNED — C-7GA.10.2 — Grouping context default: Uses the missing/unknown safe default. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.10.2 — Grouping context default | Missing or unrecognized value. | Records safe fallback. | Unknown inputs remain visible in provenance. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.10.3 — Permanent associative and combined prohibition
Stamp: DESIGNED    Source: [V10 §7G-A / MODE-ASSIGNMENT RULE:]

ALONE
- What it is: DESIGNED — The unconditional mode limit for thread_membership_v1 version 1. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DESIGNED — Any override/default path that would yield associative or combined. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DESIGNED — Treats that path as an implementation error, records it and falls back to bare. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gives out: DESIGNED — A permitted mode with the error visible in its record. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Must never: DESIGNED — Allow either prohibited mode under any condition in this rule version. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DESIGNED — Forces the safe bare fallback rather than issuing the prohibited mode. [V10 §7G-A / MODE-ASSIGNMENT RULE:]

TOGETHER
- Fed by: DESIGNED — C-7GA.10 — thread_membership_v1: Enforces the owning version's unconditional two-mode limit. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.10 — thread_membership_v1 | Proposed mode. | Falls back to bare on a prohibited path. | Error is recorded. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: NONE

### C-7GA.11 — Worker pass sequence
Stamp: DESIGNED    Source: [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — Seven ordered primary steps with immediate checkpoint substeps 5A, 7A, 7B and 7C. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — A pending job acquired under the full-job OS claim, recorded job_claimed and in_progress. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Runs instruction creation, retrieval through LMAC, mouth proposal, independent acceptance, idempotent quarantine write, instruction completion, then clash/view processing and job close. Holds the OS lock continuously and validates the claim before every specified durable operation. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — A complete reading and post-reading operation or its distinct durable failure state. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Run the primary steps in parallel, count checkpoints as independent primary work, skip claim validation or close the job before all stages finish. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — Stops at the actual failure, preserves durable work and follows the stage's stated pass/job handling. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7GA.11.1 — Step 1 — Create instruction: Makes the instruction durable first. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fed by: DESIGNED — C-7GA.11.2 — Step 2 — Retrieve context through LMAC: Retrieves only the mode's permitted context. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fed by: DESIGNED — C-7GA.11.3 — Step 3 — Prompt and mouth proposal: Obtains a proposal under the declared mode. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fed by: DESIGNED — C-7GA.11.5 — Step 5 — Idempotent quarantine reading write: Writes or recovers exactly one quarantine reading. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fed by: DESIGNED — C-7GA.11.7 — Step 7 — Clash detection: Performs ordered clash/view/job-close work after instruction completion. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-7GA.7 — Full-job OS lock and claim: The exclusive claim remains held across the sequential pass. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gated by: DESIGNED — C-7GA.11.4 — Step 4 — Acceptance and fallback routing: Independent acceptance precedes any reading write. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: DESIGNED — C-7GA.11.6 — Step 6 — Close instruction: Closes the instruction after reading completion. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | Claimed job and instruction. | Produces reading, clash and view results. | Only complete required work closes the job. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 2 · DESIGNED | C-7GA.5.2.3.2 — in_progress job | Actual worker progress. | Retains nonterminal state. | Pass completion is not job completion. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 3 · DESIGNED | C-7GA.8.2.3.2 — failed pass | Stage, cause and technical flag. | Records the failed attempt. | No fabricated success. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 4 · DESIGNED | C-7GA.13.2 — RC-1 — Job with no status | Pending job under its acquired claim. | Records started state and creates instruction. | No separate recovery engine. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |

SUB-PARTS: C-7GA.11.1 — Step 1 — Create instruction; C-7GA.11.2 — Step 2 — Retrieve context through LMAC; C-7GA.11.3 — Step 3 — Prompt and mouth proposal; C-7GA.11.4 — Step 4 — Acceptance and fallback routing; C-7GA.11.5 — Step 5 — Idempotent quarantine reading write; C-7GA.11.6 — Step 6 — Close instruction; C-7GA.11.7 — Step 7 — Clash detection

### C-7GA.11.1 — Step 1 — Create instruction
Stamp: DESIGNED    Source: [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The worker step making pass identity and mode assignment durable. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — Target source-title classification, deterministic thread count and trigger inputs. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Derives all inputs, runs thread_membership_v1, validates the claim and appends the instruction to `.nh_reading_pass_log.jsonl` before retrieval. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — A durable rpi_v1 instruction. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Retrieve context before this instruction exists or add derived assignment inputs to the sealed root. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — No undurable instruction authorizes retrieval. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7GA.10 — thread_membership_v1: Runs the exact new-root mode-assignment rule. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: Instruction append requires claim validation. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.1 — reading_pass_instruction | Derived inputs and assigned mode. | Appends before retrieval. | The pass has a reproducible contract. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 2 · DESIGNED | C-7GA.11 — Worker pass sequence | Assignment inputs and rule result. | Establishes the pass contract. | Retrieval waits for instruction. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 3 · DESIGNED | C-7GA.13.4 — RC-3 — in_progress without instruction | Actual target and trigger inputs. | Runs fresh assignment and appends instruction. | No context before durable instruction. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |

SUB-PARTS: NONE

### C-7GA.11.2 — Step 2 — Retrieve context through LMAC
Stamp: DESIGNED    Source: [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — Mode-directed retrieval using the instruction's assigned_mode. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — bare or local-context and current purpose-specific authorization. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — bare returns an empty package immediately without retrieval. local-context asks LMAC to route to positional retrieval of immediately preceding roots in the same confirmed grouping, with provenance and a section separate from the target. Uses the per-mode limit; Engine B's n=3 belongs only to its built experiment. Empty positional results are normal and continue target-only. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — Authorized positional context or an honest empty package. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Treat hidden/restricted/redacted/deleted-from-view status alone as an internal-use refusal, bypass influence-removal or compartment rules, expose Level 1 raw content outside an authorized protected-boundary function or use blocked TSC material. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — Index error, timeout or unreachable service closes the pass failed at context_retrieval with the technical flag true, leaves the job in_progress, releases the OS lock cleanly and stops. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-LMAC — Live Mechanism Access Coordinator (§26): Routes the request through current purpose-specific internal-use state. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fed by: DESIGNED — C-7F — Context Retrieval (§7F): Receives immediately preceding roots in the confirmed grouping or an empty package. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-7GA.8.1 — reading_pass_instruction: Retrieval requires the durable instruction and its assigned_mode. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): Requires internal-use permission, including protected-boundary and influence-removal rules. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.11 — Worker pass sequence | Authorized positional or empty package. | Supplies separated background. | Empty context is a normal condition. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 2 · DESIGNED | C-7GA.11.3 — Step 3 — Prompt and mouth proposal | Target and authorized background. | Builds the bounded prompt. | No unsupplied context is inferred. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |

SUB-PARTS: NONE

### C-7GA.11.3 — Step 3 — Prompt and mouth proposal
Stamp: DESIGNED    Source: [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The proposal-producing step after retrieval. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — Target root content and role, positional context if any, and the declared mode. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Frames positional context in a BACKGROUND/END BACKGROUND block separate from the target; instructs the local mouth to read what the role is doing, not describe, answer or invent; receives its proposal. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — A mouth proposal awaiting independent acceptance. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Mix background with the target or treat the mouth's output as an already accepted reading. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — Model unavailability or timeout closes the pass failed at mouth_proposal with the technical flag true, keeps the job in_progress, releases the lock and stops. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7GA.11.2 — Step 2 — Retrieve context through LMAC: Uses the actual separated context returned for this pass. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-16 — Model Layer (§16): Requests only a proposal from the local mouth. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.11 — Worker pass sequence | Target, role and separate background. | Sends the bounded prompt. | Mouth output remains unaccepted. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |

SUB-PARTS: NONE

### C-7GA.11.4 — Step 4 — Acceptance and fallback routing
Stamp: DESIGNED    Source: [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The independent boundary between mouth proposal and reading record. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — The proposal, declared mode and exact supplied root/context. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Checks valid fields, grounding, no invention, channel separation, honest uncertainty, evidence consistency and mode compliance. Accepted content proceeds to writing. Genuine context insufficiency produces a separate honest revisable fallback reading without the rejected proposal's unsupported conclusions; that is a valid completed reading outcome. A substantively rejected proposal records its distinct reason and follows the failed-job branch. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — Accepted reading material, a separately authorized honest fallback, or a recorded substantive rejection. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Use a rejected proposal as the reading, disguise malformed/fabricated/mode-violating content as insufficient context or treat honest insufficiency as refusal to write. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — Substantive rejection closes the pass failed at acceptance_check with the technical flag false, appends job failed, releases the lock and stops under the worker contract; the accepted retry seam remains separately governed. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): All seven checks and honest-insufficiency distinctions apply. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: ACCEPTED — C-7G.9 — B9 acceptance retry and fallback boundary: A careful retry or insufficiency fallback uses its accepted separate admission boundary. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.2.3.4 — failed job | Recorded acceptance rejection. | Records failed and releases the claim. | No crash retry of a rejected job. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 2 · DESIGNED | C-7GA.11 — Worker pass sequence | Actual checks and outcome. | Permits accepted/honest-fallback material only. | Substantive rejection stops its branch. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 3 · DESIGNED | C-7GA.11.5 — Step 5 — Idempotent quarantine reading write | Governed reading material. | Writes a valid reading result. | Rejected conclusions stay excluded. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |

SUB-PARTS: NONE

### C-7GA.11.5 — Step 5 — Idempotent quarantine reading write
Stamp: DESIGNED    Source: [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]

ALONE
- What it is: DESIGNED — The reading-store write or recovery step after acceptance. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]
- Takes in: DESIGNED — The accepted or honest fallback material, enqueue_key, pass_id and retrieval audit trail. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]
- Does: DESIGNED — Computes the stable reading key, validates the claim and checks the reading store. If present, recovers reading_id. Otherwise assembles the existing 12-field record, sets idempotency_key to the computed reading_idempotency_key, produced_by.config.pass_id to this pass and produced_by.retrieval_inputs to the retrieval trace; validates the claim and calls append_reading to quarantine. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]
- Gives out: DESIGNED — One existing or newly committed reading_id for checkpoint 5A. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]
- Must never: DESIGNED — Add a thirteenth field, write production, overwrite a keyed reading or lose the retrieval audit trail. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]
- Fails closed by: DESIGNED — Write failure closes the pass failed at write with the technical flag true, leaves the job in_progress, releases the lock and stops. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]

TOGETHER
- Fed by: DESIGNED — C-7GA.9 — Job-level reading idempotency: Uses the enqueue-derived reading key and lookup-first recovery. [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-7GA.11.4 — Step 4 — Acceptance and fallback routing: Only accepted or separately honest fallback material reaches writing. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: Lookup commits and writes require claim validation. [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: BUILT — C-READ.3 — append_reading: Calls the existing writer with its 12-field contract and quarantine destination. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: DESIGNED — C-7GA.11.5.1 — Step 5A — Record reading checkpoint: Follows durable reading with the immediate checkpoint. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.11 — Worker pass sequence | Accepted material and stable reading key. | Obtains durable reading_id. | No duplicate or production write. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |

SUB-PARTS: C-7GA.11.5.1 — Step 5A — Record reading checkpoint

### C-7GA.11.5.1 — Step 5A — Record reading checkpoint
Stamp: DESIGNED    Source: [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The immediate checkpoint after a reading is durably written or recovered. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — The verified reading_id. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Validates the claim and appends reading_written in the queue; leaves the job in_progress. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — A durable checkpoint before instruction closure. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Close the job at this checkpoint or write the reading again to repair it. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — Missing checkpoint recovery uses the durable keyed reading. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7GA.5.3.3.1 — reading_written checkpoint: Uses the reading-written checkpoint contract. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: the processing claim is validated before this append. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3.3.1 — reading_written checkpoint | Durable reading_id. | Appends reading_written. | No early job close. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 2 · DESIGNED | C-7GA.11.5 — Step 5 — Idempotent quarantine reading write | Verified reading_id. | Appends reading_written. | Job stays in_progress. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 3 · DESIGNED | C-7GA.11.6 — Step 6 — Close instruction | Verified reading completion. | Appends completed pass lifecycle. | Post-reading job work remains. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |

SUB-PARTS: NONE

### C-7GA.11.6 — Step 6 — Close instruction
Stamp: DESIGNED    Source: [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The pass-completion step after the reading checkpoint. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — The verified outcome reading_id and current claim. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Validates the claim and appends pass_lifecycle_event completed with outcome_reading_id. The instruction is closed while the job remains in_progress. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — A terminal pass ready for post-reading stages. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Treat instruction completion as completion of clash/view work. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — Post-reading failure does not erase the completed reading or instruction. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): supplies the durable reading ID that closes the instruction (P-MAIN step 13). [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-7GA.11.5.1 — Step 5A — Record reading checkpoint: Normal sequence closes the instruction after the reading checkpoint. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: DESIGNED — C-7GA.8.2 — pass_lifecycle_event: Writes the completed terminal with outcome_reading_id. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.2.3.1 — completed pass | Verified reading result. | Records completed. | Post-reading job work remains outstanding. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 2 · DESIGNED | C-7GA.11 — Worker pass sequence | Verified reading_id. | Appends completed lifecycle. | Queue remains open for post-reading work. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 3 · DESIGNED | C-7GA.11.7 — Step 7 — Clash detection | Durable completed pass and reading. | Begins clash detection. | No deletion of completed work on later failure. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |

SUB-PARTS: NONE

### C-7GA.11.7 — Step 7 — Clash detection
Stamp: DESIGNED    Source: [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The operation-keyed clash stage after instruction completion. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — The new reading, authorized comparison readings and `{job_id}::{reading_id}::clash_detection`. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Obtains current internal-use authorization through LMAC. Checks the clash store for this operation_key; recovers existing clash_found/clash_id and skips rerunning if found. Otherwise compares same-root, same-thread and explicitly related readings; same-clash matching appends detection/history to the existing clash rather than creating another. Writes the result or no_clash_sentinel with claim validation before every write. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — A durable clash result or proof that detection found none. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Use visible-output eligibility as this internal gate, bypass Level 1/TSC/influence-removal restrictions, create a duplicate clash or rerun a durable operation-key result. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — System failure stops with job in_progress; recovery resumes this stage from its durable evidence. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7GA.12.1 — no_clash_sentinel: A no-clash result needs its first-class durable sentinel. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fed by: DESIGNED — C-7GA.11.7.2 — Step 7B — Process triggered view profiles: Processes the triggered view profiles after clash completion. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-7GA.11.6 — Step 6 — Close instruction: Post-reading stages follow instruction completion. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): Internal-use authorization applies before clash work. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: DESIGNED — C-7J — Clash Handling (§7J): Runs authorized same-root, same-thread and explicitly related comparison with same-clash matching. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: DESIGNED — C-7GA.11.7.1 — Step 7A — Record clash checkpoint: Checkpoints the completed clash result before view computation. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: DESIGNED — C-7GA.11.7.3 — Step 7B checkpoint — Record complete profile accounting: Records the aggregate only after all profiles are accounted for. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: DESIGNED — C-7GA.11.7.4 — Step 7C — Close job: Closes the job after all required checkpoints. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.11 — Worker pass sequence; P-MAIN step 14 | Durable reading and current internal permissions. | Accounts for every triggered result. | Only then closes the job. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 2 · DESIGNED | C-7GA.13.7 — RC-6 — Reading checkpoint without clash checkpoint | Durable result or verified missing work. | Recovers or completes detection, then checkpoints. | No duplicate clash. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 3 · DESIGNED | C-7J.5.2 — Triggered-operation recovery boundary | `operation_key = {job_id}::{reading_id}::clash_detection`, the new reading, any previously committed result, and the worker's validated claim. | Supplies the reading and detection operation key. | Nothing in this card. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS] |
| 4 · DESIGNED | C-7J — Clash Handling (§7J) | New readings, their exact root references and related readings. | Supplies what this place relies on: the new reading and its operation key after the reading is durable. | Nothing in this card. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |

SUB-PARTS: C-7GA.11.7.1 — Step 7A — Record clash checkpoint; C-7GA.11.7.2 — Step 7B — Process triggered view profiles; C-7GA.11.7.3 — Step 7B checkpoint — Record complete profile accounting; C-7GA.11.7.4 — Step 7C — Close job

### C-7GA.11.7.1 — Step 7A — Record clash checkpoint
Stamp: DESIGNED    Source: [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The checkpoint after a durable clash result or sentinel exists. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — clash_found, clash_id or null, and the clash operation_key. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Validates the claim and appends clash_detection_completed before starting Computed View processing. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — The required predecessor checkpoint for view computation. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Start view computation before this checkpoint exists. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — A missing checkpoint is reconstructed from the keyed result before later work. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7GA.5.3.3.2 — clash_detection_completed checkpoint: Uses the clash-checkpoint contract. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: the processing claim is validated before this append. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3.3.2 — clash_detection_completed checkpoint | Actual clash result and key. | Appends clash_detection_completed. | View computation can begin. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 2 · DESIGNED | C-7GA.11.7 — Step 7 — Clash detection | Found flag, clash ID/null and key. | Appends stage completion. | View ordering is enforced. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 3 · DESIGNED | C-7GA.11.7.2 — Step 7B — Process triggered view profiles | Durable clash_detection_completed. | Begins triggered profile work. | No out-of-order view update. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 4 · DESIGNED | C-7J.5.2 — Triggered-operation recovery boundary | `operation_key = {job_id}::{reading_id}::clash_detection`, the new reading, any previously committed result, and the worker's validated claim. | Takes this place's change: supplies recovered or newly recorded `clash_found`, `clash_id` or null and `operation_key` for the checkpoint. | Supplies recovered or newly recorded `clash_found`, `clash_id` or null and `operation_key` for the checkpoint. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / SENTINEL RECORDS] |

SUB-PARTS: NONE

### C-7GA.11.7.2 — Step 7B — Process triggered view profiles
Stamp: DESIGNED    Source: [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — Per-profile internal snapshot computation following the clash checkpoint. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — Zero, one or multiple materially triggered profiles, current internal-use permission and purpose-appropriate relevance mode through LMAC. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — For each profile uses its exact operation key, recovers an existing snapshot/sentinel result when present, otherwise validates the claim, applies current internal-use authorization, runs the update, validates again and writes snapshot or no_update_sentinel. Builds profile_results from durable records. Visible-output eligibility and pre-output review run only on actual surfacing or deliberate inspection, not merely snapshot computation. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — Durable per-profile results without duplicate computation. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Skip the clash checkpoint, bypass Level 1/TSC/influence-removal or compartment rules, use internal computation as visible permission or invent open trigger/significance thresholds. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — A system failure during any profile stops with job in_progress; completed profiles remain recoverable and only missing profiles may run later. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7GA.12.2 — no_update_sentinel: Recovers no-update profiles from durable sentinels. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-7GA.11.7.1 — Step 7A — Record clash checkpoint: Clash checkpoint must exist before any view computation. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): Each computation needs current internal-use authorization. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-7R — Attention & Relevance Control (§7R): Uses the relevance mode appropriate to view assembly. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: DESIGNED — C-7M — Computed View (§7M): Requests each triggered internal profile update under its operation key. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3.10.2.1 — snapshot_created profile result | Committed snapshot and key. | Adds the recovered result to accounting. | Completed profiles are not rerun. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 2 · DESIGNED | C-7GA.11.7 — Step 7 — Clash detection | Authorized profile triggers and durable results. | Accounts for each update. | Completed profiles are recovered. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 3 · DESIGNED | C-7GA.13.8 — RC-7 — Clash checkpoint without complete view checkpoint | Existing and missing profile results. | Runs only incomplete profiles. | Complete profiles are preserved. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 4 · DESIGNED | C-7M — Computed View (§7M) | Permitted roots, readings, tellings, clashes, Ness response events, Person-Box links, themes, Living State and world-model references, and safe metadata-only pre-ingest references. | Supplies triggered internal profile-update requests in CY-A. | Nothing in this card. | [MAP C-7M] [V10 §7M] [V10 §7G-A] |

SUB-PARTS: NONE

### C-7GA.11.7.3 — Step 7B checkpoint — Record complete profile accounting
Stamp: DESIGNED    Source: [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The aggregate checkpoint after all triggered profiles have results. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — The complete profile_results list, including an empty list when no profiles were triggered. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Validates the claim and appends computed_view_completed with all_profiles_complete true and operation_key null, once all profiles are accounted for. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — Durable view-stage completion. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Append this aggregate incrementally or before the last required profile result. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — Incomplete profile accounting keeps the job open. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7GA.5.3.3.3 — computed_view_completed checkpoint: Uses the complete-view aggregate contract. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: the processing claim is validated before this append. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3.3.3 — computed_view_completed checkpoint | All triggered-profile results. | Writes the aggregate once. | Incomplete profiles keep the job open. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 2 · DESIGNED | C-7GA.11.7 — Step 7 — Clash detection | Complete profile_results. | Appends computed_view_completed. | No partial aggregate. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 3 · DESIGNED | C-7GA.11.7.4 — Step 7C — Close job | Complete view-stage evidence alongside prior stages. | Closes the job after validation. | No early terminal. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 4 · DESIGNED | C-7GA.13.8 — RC-7 — Clash checkpoint without complete view checkpoint | Complete durable profile_results. | Restores the final stage checkpoint. | No partial completion. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |

SUB-PARTS: NONE

### C-7GA.11.7.4 — Step 7C — Close job
Stamp: DESIGNED    Source: [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The final worker action after all three stage checkpoints. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — Durable reading, clash and complete-view checkpoint evidence. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Validates the claim, appends job_status_event completed and releases the OS lock. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — A terminal completed queue job. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Close before all required durable results or re-select the completed job afterward. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — Missing stage completion prevents this terminal path. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7GA.11.7.3 — Step 7B checkpoint — Record complete profile accounting: Requires the last complete aggregate checkpoint. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: DESIGNED — C-7GA.5.2 — job_status_event: Appends the terminal completed status. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.2.3.3 — completed job | All stage evidence. | Records terminal completed. | Missing checkpoints block close. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 2 · DESIGNED | C-7GA.11.7 — Step 7 — Clash detection | Complete durable stage history. | Appends completed and releases the lock. | Job becomes terminal. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 3 · DESIGNED | C-7GA.13.9 — RC-8 — All checkpoints without job close | All three checkpoints. | Appends completed and releases. | No repeated work to repair a close event. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |

SUB-PARTS: NONE

### C-7GA.12 — Durable negative-result sentinels
Stamp: DESIGNED    Source: [V10 §7G-A / SENTINEL RECORDS]

ALONE
- What it is: DESIGNED — First-class no-result records in the clash and Computed View stores. [V10 §7G-A / SENTINEL RECORDS]
- Takes in: DESIGNED — A completed detection/update operation that produces no clash or no update. [V10 §7G-A / SENTINEL RECORDS]
- Does: DESIGNED — Writes no_clash_sentinel or no_update_sentinel with operation_key, reading_id, job_id and timestamp. Each destination rejects duplicate commits for the same operation_key. A sentinel is positive durable proof that the operation ran and found nothing. [V10 §7G-A / SENTINEL RECORDS]
- Gives out: DESIGNED — Recoverable no-clash/no-update outcomes. [V10 §7G-A / SENTINEL RECORDS]
- Must never: DESIGNED — Interpret an absent checkpoint as a sentinel, infer a no-result outcome from missing data or commit the same operation key twice. [V10 §7G-A / SENTINEL RECORDS]
- Fails closed by: DESIGNED — Existing keyed records are recovered instead of re-executed. [V10 §7G-A / SENTINEL RECORDS]

TOGETHER
- Fed by: DESIGNED — C-7GA.12.1 — no_clash_sentinel: Uses the clash store's durable no-result record. [V10 §7G-A / SENTINEL RECORDS]
- Fed by: DESIGNED — C-7GA.12.2 — no_update_sentinel: Uses the view store's durable no-result record. [V10 §7G-A / SENTINEL RECORDS]
- Fed by: DESIGNED — C-7GA.12.3 — Sentinel operation_key: Carries the destination-enforced operation identity. [V10 §7G-A / SENTINEL RECORDS]
- Fed by: DESIGNED — C-7GA.12.4 — Sentinel reading_id: Carries the processed reading reference. [V10 §7G-A / SENTINEL RECORDS]
- Fed by: DESIGNED — C-7GA.12.5 — Sentinel job_id: Carries the owning job reference. [V10 §7G-A / SENTINEL RECORDS]
- Fed by: DESIGNED — C-7GA.12.6 — Sentinel timestamp: Dates the result record. [V10 §7G-A / SENTINEL RECORDS]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | Operation-keyed no-clash/no-update sentinels. | Recovers completed negative outcomes. | Missing records cannot masquerade as no result. | [V10 §7G-A / SENTINEL RECORDS] |

SUB-PARTS: C-7GA.12.1 — no_clash_sentinel; C-7GA.12.2 — no_update_sentinel; C-7GA.12.3 — Sentinel operation_key; C-7GA.12.4 — Sentinel reading_id; C-7GA.12.5 — Sentinel job_id; C-7GA.12.6 — Sentinel timestamp

### C-7GA.12.1 — no_clash_sentinel
Stamp: DESIGNED    Source: [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The first-class clash-store record proving detection completed with no clash. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — The exact clash operation key, reading_id, job_id and timestamp. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Commits the negative detection result under the same duplicate key used for positive clash results. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — Durable clash_found false with no clash_id, recoverable into the checkpoint. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Substitute absence of a clash object for proof that detection ran. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — Duplicate operation-key commits are rejected. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7GA.12.3 — Sentinel operation_key: Uses the exact clash operation key. [V10 §7G-A / SENTINEL RECORDS]
- Fed by: DESIGNED — C-7GA.12.4 — Sentinel reading_id: Names the reading examined. [V10 §7G-A / SENTINEL RECORDS]
- Fed by: DESIGNED — C-7GA.12.5 — Sentinel job_id: Names the owning queue job. [V10 §7G-A / SENTINEL RECORDS]
- Fed by: DESIGNED — C-7GA.12.6 — Sentinel timestamp: Dates the no-clash record. [V10 §7G-A / SENTINEL RECORDS]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: the processing claim is validated before this append. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.11.7 — Step 7 — Clash detection | Exact operation-keyed negative result. | Preserves proof detection ran. | No absent-record inference. | [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 2 · DESIGNED | C-7GA.12 — Durable negative-result sentinels | no_clash_sentinel. | Preserves negative detection proof. | No missing-record inference. | [V10 §7G-A / SENTINEL RECORDS] |

SUB-PARTS: NONE

### C-7GA.12.2 — no_update_sentinel
Stamp: DESIGNED    Source: [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The first-class Computed View store record proving a profile update ran but produced no snapshot update. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — The exact profile operation key, reading_id, job_id and timestamp. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Commits the no_update result for that profile under its duplicate-prevention identity. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — A durable completed-profile result for later accounting. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Rerun that profile merely because no new snapshot exists. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — Duplicate operation-key commits are rejected. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: DESIGNED — C-7GA.12.3 — Sentinel operation_key: Uses the exact per-profile operation key. [V10 §7G-A / SENTINEL RECORDS]
- Fed by: DESIGNED — C-7GA.12.4 — Sentinel reading_id: Names the reading driving the update. [V10 §7G-A / SENTINEL RECORDS]
- Fed by: DESIGNED — C-7GA.12.5 — Sentinel job_id: Names the owning queue job. [V10 §7G-A / SENTINEL RECORDS]
- Fed by: DESIGNED — C-7GA.12.6 — Sentinel timestamp: Dates the no-update record. [V10 §7G-A / SENTINEL RECORDS]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: the processing claim is validated before this append. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.5.3.10.2.2 — no_update profile result | Operation-keyed sentinel. | Accounts for the completed profile. | Negative results survive restart. | [V10 §7G-A / SENTINEL RECORDS] |
| 2 · DESIGNED | C-7GA.11.7.2 — Step 7B — Process triggered view profiles | Exact per-profile operation result. | Includes completed negative outcomes. | No unnecessary recomputation. | [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 3 · DESIGNED | C-7GA.12 — Durable negative-result sentinels | no_update_sentinel. | Preserves completed negative profile work. | No repeated no-update computation. | [V10 §7G-A / SENTINEL RECORDS] |

SUB-PARTS: NONE

### C-7GA.12.3 — Sentinel operation_key
Stamp: DESIGNED    Source: [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

ALONE
- What it is: DESIGNED — The destination-enforced unique key of a sentinel or positive operation result. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DESIGNED — The clash key `{job_id}::{reading_id}::clash_detection` or profile key `{job_id}::{reading_id}::computed_view::{view_profile_id}`. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DESIGNED — Identifies one durable operation effect for pre-check and duplicate rejection. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DESIGNED — A stable recovery key across checkpoint loss. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Must never: DESIGNED — Commit two results for the same operation_key or switch keys while claiming the same completed operation. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fails closed by: DESIGNED — The destination rejects duplicate commits for the key. [V10 §7G-A / SENTINEL RECORDS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.12 — Durable negative-result sentinels | operation_key. | Supports lookup and duplicate rejection. | One durable effect per key. | [V10 §7G-A / SENTINEL RECORDS] |
| 2 · DESIGNED | C-7GA.12.1 — no_clash_sentinel | Keyed detection identity. | Commits one negative result. | Duplicate commits fail. | [V10 §7G-A / SENTINEL RECORDS] |
| 3 · DESIGNED | C-7GA.12.2 — no_update_sentinel | Keyed profile identity. | Commits one negative update result. | Duplicate commits fail. | [V10 §7G-A / SENTINEL RECORDS] |

SUB-PARTS: NONE

### C-7GA.12.4 — Sentinel reading_id
Stamp: DESIGNED    Source: [V10 §7G-A / SENTINEL RECORDS]

ALONE
- What it is: DESIGNED — The reading reference in each sentinel. [V10 §7G-A / SENTINEL RECORDS]
- Takes in: DESIGNED — The reading whose post-processing produced the result. [V10 §7G-A / SENTINEL RECORDS]
- Does: DESIGNED — Links the negative result to that reading. [V10 §7G-A / SENTINEL RECORDS]
- Gives out: DESIGNED — Reading-scoped no-result provenance. [V10 §7G-A / SENTINEL RECORDS]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.12 — Durable negative-result sentinels | reading_id. | Binds the negative result. | Reading-scoped provenance. | [V10 §7G-A / SENTINEL RECORDS] |
| 2 · DESIGNED | C-7GA.12.1 — no_clash_sentinel | reading_id. | Preserves result scope. | Reading-specific negative proof. | [V10 §7G-A / SENTINEL RECORDS] |
| 3 · DESIGNED | C-7GA.12.2 — no_update_sentinel | reading_id. | Preserves result scope. | Reading-specific profile proof. | [V10 §7G-A / SENTINEL RECORDS] |

SUB-PARTS: NONE

### C-7GA.12.5 — Sentinel job_id
Stamp: DESIGNED    Source: [V10 §7G-A / SENTINEL RECORDS]

ALONE
- What it is: DESIGNED — The queue-job reference in each sentinel. [V10 §7G-A / SENTINEL RECORDS]
- Takes in: DESIGNED — The job owning the operation. [V10 §7G-A / SENTINEL RECORDS]
- Does: DESIGNED — Links the negative result to that job. [V10 §7G-A / SENTINEL RECORDS]
- Gives out: DESIGNED — Job-scoped recovery evidence. [V10 §7G-A / SENTINEL RECORDS]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.12 — Durable negative-result sentinels | job_id. | Binds recovery evidence. | Job-scoped provenance. | [V10 §7G-A / SENTINEL RECORDS] |
| 2 · DESIGNED | C-7GA.12.1 — no_clash_sentinel | job_id. | Links recovery history. | Job-specific result. | [V10 §7G-A / SENTINEL RECORDS] |
| 3 · DESIGNED | C-7GA.12.2 — no_update_sentinel | job_id. | Links recovery history. | Job-specific profile result. | [V10 §7G-A / SENTINEL RECORDS] |

SUB-PARTS: NONE

### C-7GA.12.6 — Sentinel timestamp
Stamp: DESIGNED    Source: [V10 §7G-A / SENTINEL RECORDS]

ALONE
- What it is: DESIGNED — The sentinel's recorded time. [V10 §7G-A / SENTINEL RECORDS]
- Takes in: DESIGNED — The time of the no-result record. [V10 §7G-A / SENTINEL RECORDS]
- Does: DESIGNED — Dates the completed operation evidence. [V10 §7G-A / SENTINEL RECORDS]
- Gives out: DESIGNED — Timed no-result provenance. [V10 §7G-A / SENTINEL RECORDS]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.12 — Durable negative-result sentinels | timestamp. | Records completed-operation time. | Timed proof of no result. | [V10 §7G-A / SENTINEL RECORDS] |
| 2 · DESIGNED | C-7GA.12.1 — no_clash_sentinel | timestamp. | Preserves completion time. | Timed negative proof. | [V10 §7G-A / SENTINEL RECORDS] |
| 3 · DESIGNED | C-7GA.12.2 — no_update_sentinel | timestamp. | Preserves completion time. | Timed negative profile proof. | [V10 §7G-A / SENTINEL RECORDS] |

SUB-PARTS: NONE

### C-7GA.13 — Queue-driven crash recovery
Stamp: DESIGNED    Source: [V10 §7G-A / CRASH RECOVERY SEQUENCE]

ALONE
- What it is: DESIGNED — Startup recovery from durable job, instruction, reading and post-reading records. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Takes in: DESIGNED — Jobs with no status or latest status in_progress, exclusive OS-lock acquisition and instruction-log history. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Does: DESIGNED — Excludes completed/failed jobs and handled technical failures before entering RC-1 through RC-8. Uses the applicable idempotency pre-check before repeating any durable write; missing checkpoint never proves missing effect. Restores only absent records or incomplete stages. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Gives out: DESIGNED — Recovered work, honest replacement lineage and eventual class-correct terminal without duplicate readings or post-processing effects. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Must never: DESIGNED — Automatically replay handled technical failures, select terminal jobs, infer absence from a missing checkpoint or proceed without the exclusive claim. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fails closed by: DESIGNED — Unavailable OS lock prevents recovery; handled technical failure releases the lock and moves to the next candidate without replacement or rerun. [V10 §7G-A / CRASH RECOVERY SEQUENCE]

TOGETHER
- Fed by: DESIGNED — C-7GA.13.2 — RC-1 — Job with no status: RC-1 starts a never-claimed job with no status normally. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fed by: DESIGNED — C-7GA.13.3 — RC-2 — Claimed before in_progress: RC-2 repairs missing in_progress after stale claim. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fed by: DESIGNED — C-7GA.13.4 — RC-3 — in_progress without instruction: RC-3 creates a missing instruction. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fed by: DESIGNED — C-7GA.13.5 — RC-4 — Interrupted instruction without lifecycle: RC-4 checks reading identity before replacement. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fed by: DESIGNED — C-7GA.13.6 — RC-5 — Reading exists without completion records: RC-5 repairs completion records around an existing reading. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fed by: DESIGNED — C-7GA.13.7 — RC-6 — Reading checkpoint without clash checkpoint: RC-6 recovers or runs only missing clash work. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fed by: DESIGNED — C-7GA.13.8 — RC-7 — Clash checkpoint without complete view checkpoint: RC-7 recovers completed profiles and runs only missing ones. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fed by: DESIGNED — C-7GA.13.9 — RC-8 — All checkpoints without job close: RC-8 appends only the missing final close. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Gated by: DESIGNED — C-7GA.7 — Full-job OS lock and claim: Recovery requires exclusive acquisition before any candidate processing. [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Gated by: DESIGNED — C-7GA.13.1 — Handled technical failure exclusion: Handled technical failures are excluded before all RC cases. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Gated by: DESIGNED — C-7GA.13.10 — Independent no-repeat guards: All independent no-repeat guards remain active. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | Durable checkpoints and actual pass history. | Repairs only unfinished work. | No handled-failure replay loop. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] |
| 2 · DESIGNED | C-7GA.13.10 — Independent no-repeat guards | Terminal states, abandoned-pass records, reading key and technical exclusion. | Preserves all guards together. | No infinite restart replay. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] |

SUB-PARTS: C-7GA.13.1 — Handled technical failure exclusion; C-7GA.13.2 — RC-1 — Job with no status; C-7GA.13.3 — RC-2 — Claimed before in_progress; C-7GA.13.4 — RC-3 — in_progress without instruction; C-7GA.13.5 — RC-4 — Interrupted instruction without lifecycle; C-7GA.13.6 — RC-5 — Reading exists without completion records; C-7GA.13.7 — RC-6 — Reading checkpoint without clash checkpoint; C-7GA.13.8 — RC-7 — Clash checkpoint without complete view checkpoint; C-7GA.13.9 — RC-8 — All checkpoints without job close; C-7GA.13.10 — Independent no-repeat guards

### C-7GA.13.1 — Handled technical failure exclusion
Stamp: DESIGNED    Source: [V10 §7G-A / CRASH RECOVERY SEQUENCE]

ALONE
- What it is: DESIGNED — The pre-RC distinction between a recorded failure and an interrupted pass. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Takes in: DESIGNED — The latest lifecycle event for the candidate job. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Does: DESIGNED — If it is failed with is_technical_and_potentially_retryable true, treats it as a handled failure awaiting its retry policy, creates no replacement instruction, reruns nothing, releases the OS lock and moves to the next candidate. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Gives out: DESIGNED — Preserved in_progress job and recorded technical failure outside crash replay. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Must never: DESIGNED — Treat repeated startup as a retry scheduler or erase the handled failure to enter RC-4. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fails closed by: DESIGNED — Stops automatic recovery for that candidate; a separately authorized retry admission remains required. [V10 §7G-A / CRASH RECOVERY SEQUENCE]

TOGETHER
- Fed by: DESIGNED — C-7GA.8.2.6.4 — is_technical_and_potentially_retryable: Uses the latest recorded technical-failure flag. [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.13 — Queue-driven crash recovery | Latest lifecycle classification. | Skips without replacement or rerun. | Startup cannot become retry scheduling. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] |

SUB-PARTS: NONE

### C-7GA.13.2 — RC-1 — Job with no status
Stamp: DESIGNED    Source: [V10 §7G-A / CRASH RECOVERY SEQUENCE]

ALONE
- What it is: DESIGNED — Recovery of a job with no status event that has never been claimed or started. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Takes in: DESIGNED — The pending job and exclusive processing lock. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Does: DESIGNED — Writes claim metadata, appends job_claimed and in_progress, then starts the full worker sequence at Step 1. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Gives out: DESIGNED — A normally started pending job. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Must never: DESIGNED — Enqueue a duplicate because the status is absent or process without the lock. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fails closed by: DESIGNED — No lock acquisition means no recovery processing. [V10 §7G-A / CRASH RECOVERY SEQUENCE]

TOGETHER
- Fed by: DESIGNED — C-7GA.11 — Worker pass sequence: Starts the ordinary worker sequence at Step 1. [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-7GA.7.2 — Claim acquisition: the exclusive processing lock is acquired first. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.13 — Queue-driven crash recovery | Pending job. | Claims and appends in_progress. | Instruction sequence begins once. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] |

SUB-PARTS: NONE

### C-7GA.13.3 — RC-2 — Claimed before in_progress
Stamp: DESIGNED    Source: [V10 §7G-A / CRASH RECOVERY SEQUENCE]

ALONE
- What it is: DESIGNED — Recovery after a claim was recorded but startup crashed before in_progress. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Takes in: DESIGNED — Existing job_claimed with no in_progress, stale metadata and completed OS-lock takeover. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Does: DESIGNED — Uses the takeover's claim_expired and new job_claimed records, appends in_progress and proceeds to RC-3. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Gives out: DESIGNED — A durably started job under the replacement claim. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Must never: DESIGNED — Skip the exclusive takeover or duplicate the root/reading operation. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fails closed by: DESIGNED — A live held lock blocks takeover. [V10 §7G-A / CRASH RECOVERY SEQUENCE]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7GA.7.7 — Stale-claim takeover: Requires stale takeover and its events before repairing in_progress. [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.13 — Queue-driven crash recovery | Taken-over claim history. | Appends missing started state. | No duplicate work identity. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] |

SUB-PARTS: NONE

### C-7GA.13.4 — RC-3 — in_progress without instruction
Stamp: DESIGNED    Source: [V10 §7G-A / CRASH RECOVERY SEQUENCE]

ALONE
- What it is: DESIGNED — Recovery when the queue started but no instruction entry exists for the job. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Takes in: DESIGNED — The job and current derived assignment inputs. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Does: DESIGNED — Runs thread_membership_v1 fresh, validates the claim, appends a durable instruction and proceeds to RC-4. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Gives out: DESIGNED — An explicitly governed pass ready for the next recovery check. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Must never: DESIGNED — Retrieve before writing the instruction or reuse a nonexistent pass identity. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fails closed by: DESIGNED — Instruction creation must complete before context work. [V10 §7G-A / CRASH RECOVERY SEQUENCE]

TOGETHER
- Fed by: DESIGNED — C-7GA.11.1 — Step 1 — Create instruction: Uses the ordinary instruction-creation rule. [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: the processing claim is validated before this append. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.13 — Queue-driven crash recovery | Started job and current assignment inputs. | Runs the mode rule fresh. | Durable pass contract before retrieval. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] |

SUB-PARTS: NONE

### C-7GA.13.5 — RC-4 — Interrupted instruction without lifecycle
Stamp: DESIGNED    Source: [V10 §7G-A / CRASH RECOVERY SEQUENCE]

ALONE
- What it is: DESIGNED — Recovery of a pass interrupted during retrieval, proposal, acceptance or writing. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Takes in: DESIGNED — An instruction without terminal event and the job-level reading idempotency key. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Does: DESIGNED — Looks for the keyed reading first. If it exists, proceeds to RC-5. Otherwise validates the claim, appends abandoned with the exact interruption/replacement reason, creates a new instruction with new pass_id, same job_id and recovery_of_pass_id pointing to the abandoned pass, runs fresh mode assignment and resumes the worker at Step 2. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Gives out: DESIGNED — Restored existing-reading work or a recorded replacement attempt under the same reading identity. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Must never: DESIGNED — Treat a missing lifecycle/checkpoint as proof that no reading committed or start replacement before abandoning its predecessor. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fails closed by: DESIGNED — Existing reading absorbs the write path; handled technical failure was excluded before this case. [V10 §7G-A / CRASH RECOVERY SEQUENCE]

TOGETHER
- Fed by: DESIGNED — C-7GA.9 — Job-level reading idempotency: Checks the stable reading key before abandoning or replacing. [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: the processing claim is validated before this append. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Changes: DESIGNED — C-7GA.8.2.3.3 — abandoned pass: Records abandonment before an authorized replacement when no reading exists. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Changes: DESIGNED — C-7GA.8.1 — reading_pass_instruction: Creates replacement with new pass_id, same job_id and predecessor link. [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.8.2.3.3 — abandoned pass | Recovery lookup result. | Records abandonment before replacement. | Existing reading avoids rerun. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] |
| 2 · DESIGNED | C-7GA.13 — Queue-driven crash recovery | Interrupted instruction and keyed lookup. | Recovers existing reading or abandons and replaces. | No duplicate reading from a missing lifecycle. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] |

SUB-PARTS: NONE

### C-7GA.13.6 — RC-5 — Reading exists without completion records
Stamp: DESIGNED    Source: [V10 §7G-A / CRASH RECOVERY SEQUENCE]

ALONE
- What it is: DESIGNED — Recovery of a durable reading whose checkpoint/lifecycle records were interrupted. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Takes in: DESIGNED — reading_id recovered by the exact idempotency lookup. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Does: DESIGNED — Validates the claim and appends completed lifecycle if missing; validates again and appends the missing reading_written checkpoint with the recovered ID; proceeds to RC-6. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Gives out: DESIGNED — Repaired instruction and reading-stage completion without another reading. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Must never: DESIGNED — Rewrite the reading or duplicate an already present lifecycle/checkpoint record. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fails closed by: DESIGNED — Durable reading identity is required for the repaired references. [V10 §7G-A / CRASH RECOVERY SEQUENCE]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7GA.9 — Job-level reading idempotency: Requires the exact durable keyed reading. [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: Each lifecycle/checkpoint repair requires claim validation. [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.13 — Queue-driven crash recovery | Verified durable reading_id. | Appends only missing lifecycle/checkpoint records. | Reading bytes are untouched. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] |

SUB-PARTS: NONE

### C-7GA.13.7 — RC-6 — Reading checkpoint without clash checkpoint
Stamp: DESIGNED    Source: [V10 §7G-A / CRASH RECOVERY SEQUENCE]

ALONE
- What it is: DESIGNED — Recovery of the next missing post-reading stage. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Takes in: DESIGNED — reading_written and the exact clash operation key. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Does: DESIGNED — Checks the clash store before detection; records a found durable result without rerunning, or executes missing detection under claim validation and same-clash matching. Appends clash_detection_completed and proceeds to RC-7. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Gives out: DESIGNED — A repaired or newly completed clash checkpoint. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Must never: DESIGNED — Create a duplicate clash or rerun a completed keyed operation. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fails closed by: DESIGNED — A system failure preserves the in_progress job and durable prior work. [V10 §7G-A / CRASH RECOVERY SEQUENCE]

TOGETHER
- Fed by: DESIGNED — C-7GA.11.7 — Step 7 — Clash detection: Uses the existing clash operation and same-clash contract. [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: the processing claim is validated before this append. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.13 — Queue-driven crash recovery | Reading checkpoint and clash key. | Restores the clash checkpoint. | No duplicate detection effect. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] |

SUB-PARTS: NONE

### C-7GA.13.8 — RC-7 — Clash checkpoint without complete view checkpoint
Stamp: DESIGNED    Source: [V10 §7G-A / CRASH RECOVERY SEQUENCE]

ALONE
- What it is: DESIGNED — Recovery of incomplete Computed View profile processing. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Takes in: DESIGNED — clash_detection_completed and each triggered profile's operation key. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Does: DESIGNED — Recovers completed profiles, runs only missing profiles with validation before each write, reconstructs profile_results from durable records and appends computed_view_completed only when all profiles are accounted for; proceeds to RC-8. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Gives out: DESIGNED — Complete profile accounting without repeated successful updates. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Must never: DESIGNED — Discard or rerun a completed profile or append an incomplete aggregate. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fails closed by: DESIGNED — Failure leaves completed profiles recoverable and the job in_progress. [V10 §7G-A / CRASH RECOVERY SEQUENCE]

TOGETHER
- Fed by: DESIGNED — C-7GA.11.7.2 — Step 7B — Process triggered view profiles: Uses per-profile key checks and authorized update rules. [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: the processing claim is validated before this append. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Changes: DESIGNED — C-7GA.11.7.3 — Step 7B checkpoint — Record complete profile accounting: Appends the aggregate only after reconstructed full accounting. [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.13 — Queue-driven crash recovery | Clash checkpoint and profile keys. | Restores complete aggregate accounting. | No repeated successful profile work. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] |

SUB-PARTS: NONE

### C-7GA.13.9 — RC-8 — All checkpoints without job close
Stamp: DESIGNED    Source: [V10 §7G-A / CRASH RECOVERY SEQUENCE]

ALONE
- What it is: DESIGNED — Recovery after all required work committed but the terminal job event did not. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Takes in: DESIGNED — All three durable stage checkpoints. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Does: DESIGNED — Validates the claim, appends job_status_event completed and releases the OS lock. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Gives out: DESIGNED — A terminal completed job without repeated reading or post-processing. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Must never: DESIGNED — Re-execute completed stages to repair only the missing close event. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fails closed by: DESIGNED — Missing required checkpoint excludes this completion-only case. [V10 §7G-A / CRASH RECOVERY SEQUENCE]

TOGETHER
- Fed by: DESIGNED — C-7GA.11.7.4 — Step 7C — Close job: Uses the normal verified job-close rule. [V10 §7G-A / CRASH RECOVERY SEQUENCE] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gated by: DESIGNED — C-7GA.7.5 — Validate claim before durable work: the processing claim is validated before this append. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.13 — Queue-driven crash recovery | All three stage checkpoints. | Completes and releases. | No rerun of finished stages. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] |

SUB-PARTS: NONE

### C-7GA.13.10 — Independent no-repeat guards
Stamp: DESIGNED    Source: [V10 §7G-A / CRASH RECOVERY SEQUENCE]

ALONE
- What it is: DESIGNED — The combined guards preventing repeated startup from replaying already resolved work. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Takes in: DESIGNED — Terminal job states, pass terminals, stable reading identity and handled-failure classification. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Does: DESIGNED — Keeps recovery queue-driven; never reselects terminal jobs; records every abandoned instruction before replacement; uses one reading key across all attempts; excludes handled technical failures from crash recovery. Each guard remains independently necessary. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Gives out: DESIGNED — Restart-safe recovery with no automatic technical-retry loop. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Must never: DESIGNED — Rely on only one guard while dropping another, erase prior state or create duplicate readings across attempts. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Fails closed by: DESIGNED — Terminal jobs and handled failures are excluded before repeat work begins. [V10 §7G-A / CRASH RECOVERY SEQUENCE]

TOGETHER
- Fed by: DESIGNED — C-7GA.13 — Queue-driven crash recovery: Enforces the owning queue-driven recovery contract. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.13 — Queue-driven crash recovery | Job/pass states and stable keys. | Excludes terminal and handled-failure replay. | No restart loop. | [V10 §7G-A / CRASH RECOVERY SEQUENCE] |

SUB-PARTS: NONE

### C-7GA.14 — Accepted retry and reread boundaries consumed by the worker
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — The accepted B9 consumption boundary around the existing worker operation. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2]
- Takes in: ACCEPTED — The source operation's own durable outcome, canonical enqueue identity, retry configuration and case authorization where required. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2]
- Does: ACCEPTED — Treats retry as another admitted attempt to complete the same operation, through its own boundaries and duplicate defenses. Keeps a completed reading, including honest insufficient_context, terminal_success and never retries it; later re-examination requires B10's separately recorded new reread trigger. A live hold blocks both paths; indeterminate work requires source recovery first. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2]
- Gives out: ACCEPTED — An absorbed, refused or expressly admitted same-identity attempt, without a new reading layer from retry. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2]
- Must never: ACCEPTED — Turn retry into reread, bypass held/privacy-refused/indeterminate states, invent defaults, infer retry permission from a crash or rewrite terminal source history. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2]
- Fails closed by: ACCEPTED — No committed B9 admission means no execution under retry authority; terminal success absorbs against the committed result. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2]

TOGETHER
- Fed by: ACCEPTED — C-7GA.14.1 — Technical-retry admission boundary: Consumes exact technical admission and dual bounds. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Fed by: ACCEPTED — C-7GA.14.3 — Substantive retry and fallback handoff: Consumes the recorded-first substantive seam separately. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]
- Fed by: DESIGNED — C-7H — Reread Lifecycle (§7H): Uses the generic retry/reread owner's canonical identities and admission records. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2]
- Gated by: ACCEPTED — C-7GA.14.2 — Later technical-episode first-attempt boundary: A later same-identity episode needs committed real-change consumption and unchanged canonical inputs. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7B.7 — Hold-until-enough: A live hold on source or inputs blocks admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | Durable outcome and canonical identity. | Separates recovery, retry and reread. | No hidden re-execution. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [V10 §7G-A] |
| 2 · ACCEPTED | C-7GA.15 — B12 — Nightly-batch activation | A scheduled or recorded manual trigger, the one-time activation boundary, the current approved scheduler configuration and already-enqueued jobs. | Gates this place: retains accepted retry admission separately from queue crash recovery. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2] |

SUB-PARTS: C-7GA.14.1 — Technical-retry admission boundary; C-7GA.14.2 — Later technical-episode first-attempt boundary; C-7GA.14.3 — Substantive retry and fallback handoff

### C-7GA.14.1 — Technical-retry admission boundary
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — Consumption of B9's declared dual-bound admission for a handled technical failure. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — technical_retryable durable outcome, no live group attempt or hold, readable exact budget version and reconstructed episode evidence. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Requires at most 3 total technical attempts per episode, including its original attempt, plus an open elapsed deadline: 7 minutes live chat or 15 minutes background/nightly from the episode's first durable failure. Minimum gaps before ordinals 2/3 are 10/30 seconds live or 1/3 minutes background; gap readiness and both bounds must permit before admission. B9 atomically binds the exact group, permanent attempt number, attempt ID, episode, ordinal and evidence; one winner, losers append nothing. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — A bounded admitted same-identity attempt or truthful refusal/exhaustion. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Reset the episode by restart, use gap sums as the deadline, admit after either bound closes or silently choose the source operation's execution timeout. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Deadline expiry while waiting stops admission; expiry during an admitted attempt forces no cancellation and overrides no source timeout, but permits no further retry afterward. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §4] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7H — Reread Lifecycle (§7H): Execution requires the owning B9 compare-and-commit admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7GA.14 — Accepted retry and reread boundaries consumed by the worker | Durable class, budget and episode evidence. | Admits only a bounded attempt. | No default retry. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7GA.14.2 — Later technical-episode first-attempt boundary
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The special admission boundary for ordinal 1 of a later same-identity technical episode. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Takes in: ACCEPTED — A committed real-change consumption authorization and source confirmation that canonical inputs are unchanged. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Does: ACCEPTED — Requires a new bounded episode with the next unused permanent attempt number and ordinal 1, binding exact budget/version, consumption record, and the proposed durable states no_gap_before_ordinal_1 and deadline_pending_from_first_durable_failure. Creates no actual gap or deadline evidence yet. Success ends normally; durable technical failure establishes the new deadline, fixed schedule_class and gap anchor; protected outcomes retain their own routes. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Gives out: ACCEPTED — An honestly admitted fresh episode without resetting permanent history or inventing a pre-failure deadline. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Must never: ACCEPTED — Recount predecessor episodes as this episode, start its failure clock early, manufacture a technical deadline from a protected outcome or change canonical inputs while pretending identity is unchanged. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Without the real-change consumption authorization and unchanged-input confirmation, this later same-identity opening is unavailable. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7H — Reread Lifecycle (§7H): Later episode opening requires the owning committed consumption record and identity check. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7GA.14 — Accepted retry and reread boundaries consumed by the worker | New episode authorization. | Uses explicit ordinal-1 pending states. | No reset or premature deadline. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7GA.14.3 — Substantive retry and fallback handoff
Stamp: ACCEPTED    Source: [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The worker's consumption of the separately defined careful-retry acceptance seam. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — The durable B24 rejection of the exact case, adopted retry-policy reference, case-authorization reference and open episode bounds. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Permits the one careful fresh attempt only through the acceptance owner's recorded-first boundary, preserving the rejected attempt and supplying its rejection reason as context. Keeps fallback separate from a rejected proposal and from protected failures. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — An authorized careful attempt or terminal refusal without rewriting the original queue/pass history. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Use crash recovery to bypass the substantive retry boundary or turn the rejected proposal into the final reading. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Missing rejection, policy, case authorization, allowance or deadline prevents admission. [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7G.9 — B9 acceptance retry and fallback boundary: Uses the accepted one-careful-retry/fallback boundary already defined by acceptance. [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7GA.14 — Accepted retry and reread boundaries consumed by the worker | Exact B24 rejection and bounded authorization. | Preserves rejected history while evaluating fresh work. | No fallback from protected failure. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13] |

SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece USED BY continuations

| Owner whose USED BY is continued | Used in | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| C-STORE — Accretive store & sealed roots (§6B) | DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | New root_id and durable write. | Enqueues asynchronous reading work. | The root gains a governed post-root job. | [V10 §7G-A] |
| C-LMAC — Live Mechanism Access Coordinator (§26) | DESIGNED — C-7GA.1 — Continuous live mechanism connection | Live purpose-specific request. | Obtains current state without caching. | Continuous mechanism connection. | [V10 §7G-A / LMAC AND THE CONTINUOUS MECHANISM CONNECTION] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED — C-7GA.1 — Continuous live mechanism connection | Current privacy authorization. | Preserves internal-use versus visible-output separation. | No weakened privacy gate. | [V10 §7G-A / LMAC AND THE CONTINUOUS MECHANISM CONNECTION] |
| C-7P — Permission & Authority Boundaries (§7P) | DESIGNED — C-7GA.1 — Continuous live mechanism connection | Current permission state. | Keeps queries within authorization. | No mid-pass permission bypass. | [V10 §7G-A / LMAC AND THE CONTINUOUS MECHANISM CONNECTION] |
| C-READ.4 — Quarantine readings destination | DESIGNED — C-7GA.2 — Quarantine-only worker destination | Worker reading material. | Preserves the separate test destination. | Production remains unactivated. | [V10 §7G-A / IMPORTANT QUARANTINE BOUNDARY] |
| C-READ.5 — Production readings authorization | DESIGNED — C-7GA.2 — Quarantine-only worker destination | Production authorization state. | Withholds production execution until every condition holds. | Successful quarantine tests do not grant permission. | [V10 §7G-A / IMPORTANT QUARANTINE BOUNDARY] |
| C-7E.8 — Source-title and thread resolution | DESIGNED — C-7GA.8.1.8.1 — source_title_type | Established source provenance and grouping. | Records pass-local source_title_type. | A raw string is not a mode decision. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
| C-READ.1.12 — reading.idempotency_key | DESIGNED — C-7GA.9 — Job-level reading idempotency | reading_idempotency_key. | Binds the reading to the source operation. | No thirteenth reading field. | [V10 §7G-A / JOB-LEVEL READING IDEMPOTENCY] |
| C-LMAC — Live Mechanism Access Coordinator (§26) | DESIGNED — C-7GA.11.2 — Step 2 — Retrieve context through LMAC | Authorized live retrieval request. | Obtains current component results. | No cached global view. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| C-7F — Context Retrieval (§7F) | DESIGNED — C-7GA.11.2 — Step 2 — Retrieve context through LMAC | Positional results and provenance. | Keeps background separate from target. | No empirical limit invented from Engine B. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED — C-7GA.11.2 — Step 2 — Retrieve context through LMAC | Current purpose-specific authorization. | Returns only eligible context. | Visible eligibility is not substituted. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| C-16 — Model Layer (§16) | DESIGNED — C-7GA.11.3 — Step 3 — Prompt and mouth proposal | Target role/content, mode and background. | Instructs reading rather than answering or inventing. | Independent acceptance remains required. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | DESIGNED — C-7GA.11.4 — Step 4 — Acceptance and fallback routing | Proposal and exact supplied evidence. | Accepts or records the distinct failure/fallback route. | Rejected content never becomes the reading. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| C-7G.9 — B9 acceptance retry and fallback boundary | DESIGNED — C-7GA.11.4 — Step 4 — Acceptance and fallback routing | Durable rejection and bounded authorization. | Preserves attempt terminals and five outcome classes. | No crash-based substantive retry. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13] |
| C-READ.3 — append_reading | DESIGNED — C-7GA.11.5 — Step 5 — Idempotent quarantine reading write | Accepted reading, provenance and idempotency_key. | Appends through the protected writer. | One reading without a thirteenth field. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| C-7J — Clash Handling (§7J) | DESIGNED — C-7GA.11.7 — Step 7 — Clash detection | New reading and clash operation key. | Recovers or records one clash result/history. | No duplicate clash object. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED — C-7GA.11.7 — Step 7 — Clash detection | Current permitted-use state through LMAC. | Preserves protected/influence-removal boundaries. | Visible-output gating is not substituted. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| C-7M — Computed View (§7M) | DESIGNED — C-7GA.11.7.2 — Step 7B — Process triggered view profiles | Reading, profile and authorized current state. | Recovers or creates snapshot/no-update results. | No repeat of completed profile work. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED — C-7GA.11.7.2 — Step 7B — Process triggered view profiles | Purpose-specific privacy state through LMAC. | Applies Level 1, TSC and influence-removal restrictions. | No visible-output authority inferred. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| C-7R — Attention & Relevance Control (§7R) | DESIGNED — C-7GA.11.7.2 — Step 7B — Process triggered view profiles | Current purpose-appropriate relevance state. | Bounds the profile operation. | No mode guessed from visible-surface rules. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| C-7H — Reread Lifecycle (§7H) | ACCEPTED — C-7GA.14 — Accepted retry and reread boundaries consumed by the worker | B9 state or separately recorded B10 trigger. | Keeps retry and reread distinct. | Completed readings are never retried. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2] |
| C-7B.7 — Hold-until-enough | ACCEPTED — C-7GA.14 — Accepted retry and reread boundaries consumed by the worker | Actual hold state. | Refuses retry and waits on governed release. | No queue-around or invented release. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md §2] |
| C-7H — Reread Lifecycle (§7H) | ACCEPTED — C-7GA.14.1 — Technical-retry admission boundary | Exact durable budget, episode, ordinal and class evidence. | Admits one winner only. | No source execution without committed admission. | [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| C-7H — Reread Lifecycle (§7H) | ACCEPTED — C-7GA.14.2 — Later technical-episode first-attempt boundary | Real-change authorization and unchanged inputs. | Binds the next permanent attempt and explicit pending states. | No inferred earlier clock or counter reset. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] |
| C-7G.9 — B9 acceptance retry and fallback boundary | ACCEPTED — C-7GA.14.3 — Substantive retry and fallback handoff | Durable case rejection and both open bounds. | Requests fresh bounded work only. | Rejected content and protected failures keep their classifications. | [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §7] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13] |
| C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | The step-11 mouth proposal, supplied evidence and declared mode. | Checks validity, grounding, uncertainty, evidence consistency, channels and mode. | An accepted reading handoff or the distinct rejection/honest-fallback path. | [V10 §7G] [MAP C-7G] |
| C-7F — Context Retrieval (§7F) | DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | The worker context-assembly step with bare/local-context restriction. | Retrieves eligible preceding material or honestly returns none. | The downstream pass keeps actual context provenance and technical failure separate. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| C-LMAC — Live Mechanism Access Coordinator (§26) | DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | The pass-specific context request. | Route the pass-specific context request through internal-use authorization before any context root is returned; held pre-ingest material and protected-boundary restrictions remain in force. | Nothing in this card. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| C-16 — Model Layer (§16) | DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | The target content, role, declared mode and any separate background context. | Receive the target content and role, declared mode, and any separate BACKGROUND context with the instruction to read what the role is doing rather than answer or invent; return a proposal for checking. | Nothing in this card. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| C-READ — Reading record, validator, writer (§6B) | DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | The pass's reading and its operation key. | Recover an existing reading with the operation’s idempotency key, or validate and append the 12-field reading to quarantine; record reading_written without promoting it into production. | The quarantine readings file. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| C-7M — Computed View (§7M) | DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | Each triggered view profile after clash detection. | After clash detection completes, process each triggered view profile under internal-use authorization and relevance rules; recover or record its snapshot or no-update result, then account for all triggered profiles. | The view snapshots and no-update results. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |

## Scope and path placement

C-7GA owns the designed post-root queue, mode assignment, worker sequence, job/pass records, locks, idempotency and crash recovery. Its 14 primary groups retain the source's ordering. The current chapter does not activate a queue, create an engine store, select an implementation API or authorize production.

The root has separate USED BY rows for its five P-MAIN placements (steps 5, 6, 7, 13 and 16), CY-A and the asynchronous segment of CY-B. Every descendant inherits those placements through the sub-part tree. Full side-path assembly remains CH11, and full chat-response synchronization remains outside this post-root design. The wider instruction schema vocabulary does not weaken thread_membership_v1's permanent bare/local-context restriction.

Existing reading ID, idempotency, quarantine and writer contracts keep their earlier C-READ identities. The shared sentinel fields have one current identity reused by both negative-result records. C-7G and C-7G.9 remain the independent acceptance and careful-retry/fallback owners; C-7H is the named later owner for full B9/B10 machinery.


## Cross-piece TOGETHER continuations for incoming uses

| Using card | Field | Current owner | Condition / handoff | Source |
|---|---|---|---|---|
| C-STORE — Accretive store & sealed roots (§6B) | Changes | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | DESIGNED — A successful durable new-root append triggers atomic enqueue. | [V10 §7G-A] |
| C-READ — Reading record, validator, writer (§6B) | Fed by | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | DESIGNED — Receives reading material through the worker's idempotent quarantine-write step. | [V10 §7G-A] |
| C-ENGINE-AB — Engines A & B (§7C, §16) | Fed by | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | DESIGNED — The designed worker is an upstream user of the existing bare/positional engine modes. | [MAP C-ENGINE-AB] [V10 §7G-A] |
| C-ENGINE-C.1 — Story-layer engine pass | Fed by | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | DESIGNED — Story-layer passes inherit the async operation route and its identity. | [MAP C-ENGINE-C] [V10 §7G-A] |
| C-ENGINE-C.9 — Inherited pass recovery | Fed by | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | DESIGNED — Inherits the async path's operation identity, idempotency and crash recovery. | [MAP C-ENGINE-C] [V10 §7G-A / CRASH RECOVERY SEQUENCE] |
| C-GOLD.6.2 — Live before nightly | Gated by | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | DESIGNED — Live-path construction precedes nightly deepening under the protected build-order constraint. | [MAP C-ENGINE-C] |
| C-13 — Live Loop (§13) | Changes | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | DESIGNED — Routes newly captured durable roots into asynchronous reading. | [MAP C-13] [V10 §7G-A] |
| C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | Fed by | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | DESIGNED — Receives the worker's declared target, context and proposal. | [V10 §7G-A] |


## Source conflicts and explicit source-scope differences

| Kind | Sources and exact difference | Preserved treatment |
|---|---|---|
| [SOURCE CONFLICT] | V10 §7G-A names one fixed `.nh_accretive_store.jsonl` line-count activation scan and describes newly appended roots in the sealed store. The governing sealed-batch boundary and Map C-STORE prohibit further appends to the sealed batch and require the separate B11 active writable-batch route for future roots. [V10 §7G-A / QUEUE ACTIVATION BOUNDARY] [MAP C-STORE] | The literal activation record/count/scan is preserved, as is the immutable sealed-batch boundary already carried in CH00/CH03-a. No cross-batch activation cursor, migration or permission to reopen the sealed batch is invented. The integrated reconciliation addressing remains an explicit gap. |
| [SOURCE CONFLICT] | The literal job_claimed record uses `claimed_at`; the later claim-metadata paragraph says `locked_at` is recorded both in the lock file and in job_claimed. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / JOB-PROCESSING LOCK AND CLAIM MECHANISM] | The literal event schema retains claimed_at and the lock metadata retains locked_at. The conflicting event-field assertion remains unresolved; no silent rename, duplicate field or alias is adopted. |
| [SOURCE CONFLICT] | Mode-rule input definitions count all other roots with the same source_title, excluding the target. The default conditions and reasons require at least one preceding root. Those tests are not equivalent when a count includes later roots. [V10 §7G-A / MODE-ASSIGNMENT RULE:] | Both the exact derived-count definition and the preceding-context condition remain recorded. No alternative counter or eligibility algorithm is invented. The relationship between these inputs and predecessor eligibility remains for explicit reconciliation. |
| [SOURCE CONFLICT] | Map C-7GA generalizes system failure at any stage as closing the pass technical-failed. V10 Step 6 has already closed the instruction completed before the Step 7 clash/view stages; Step 7 system failures instead stop with job in_progress and recover the unfinished stage. [MAP C-7GA] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] | V10's stage-specific behavior governs. Completed pass history is preserved; no second failed terminal is appended to reinterpret its completed reading merely because later post-processing failed. The Map's broader wording is retained as a source conflict. |
| [SOURCE CONFLICT] | V10's substantive-rejection branch appends terminal job failed, and terminal jobs are never reselected. Later accepted B9 values permit one recorded-first careful fresh attempt through the same source seam and canonical identity. The sources do not provide an integrated queue transition that reconciles that fresh attempt with the already terminal queue job. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [04/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §13] | Both contracts are explicit. No terminal job is reopened through crash recovery, and no local retry implementation bypasses the source seam. The integration transition remains undecided; standalone retry acceptance does not implement it. |
| Accepted design versus old open slot | V10/Map and historical B9/coordination text leave retry values and several policy slots open. The B9 values acceptance receipt establishes the later standalone values package, while C-7G.9 already places its full acceptance-specific consumption. [MAP C-7GA] [04/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md §3] | Three total technical attempts, 7/15-minute elapsed limits and 10/30-second or 1/3-minute gaps are accepted design values. Integration, execution timeouts and source-seam boundaries are not silently closed. Complete generic records and remaining accepted A25/B10 scope belong to CH05-d. |
| Worker routing versus acceptance outcome | V10 Step 4 describes accepted material, a separate honest insufficient-context fallback, and substantive rejection as worker routes. C-7G's acceptance remains pass/fail; insufficient_context is a separately written honest revisable reading, not a peer validator outcome. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] | The worker branches retain their effects and the rejected proposal is never reused. The current acceptance owner's committed external insufficiency assessment and bounded fallback admission remain required. |
| Earlier-piece scope-label finding | CH05-a's remaining-scope paragraph calls C-7R the conflict-policy owner; its exact component scope is Attention & Relevance Control. Full clash handling belongs to C-7J, CH06-a. | CH05-a remains frozen. The manifest records this incorrect scope label for correction in a later whole-piece version; current view processing correctly consumes C-7R relevance. |

## Explicit remaining scope

- **CH05-c, C-7F:** full retrieval contract, parameter schema and empirically unresolved quantities. Current worker behavior includes its own bare/positional routes, empty-result handling, authorization, provenance and technical-failure response. Engine B's n=3 remains experiment-specific.
- **CH05-d, C-7H:** complete B9 outcome/identity/record architecture, R0–R4, nine duplicate-prevention points, nineteen recovery cases, all fail-closed/log-event records, full budget/episode/attempt-number/schedule/real-change schemas, exhaustion and later-episode lifecycle; complete B10 reread identity and accepted A25 mode/compatibility wiring. Current C-7GA.14 only consumes these contracts around the worker. The coordination note's complete ownership/protection boundaries are assigned there; project workflow and audit procedures are excluded.
- **CH05-a, C-7G:** complete independent acceptance, B24 validation records/criteria, A31 grounding and careful-retry/fallback consumption already delivered. Its recorded source conflicts and candidate-only category corrections remain unchanged. The current worker does not repeat those schemas or choose their open provider/disagreement configuration.
- **CH06-a, C-7J:** complete clash-object and detection-history schema, matching and policy. **CH06-d, C-7M:** complete view-profile/snapshot schema, significance thresholds and trigger policy. Current worker owns their invocation order, operation-key duplicate boundary, sentinels, complete-profile accounting and restart behavior only.
- **CH08-a, C-7Q; CH08-b, C-7R; CH08-c, C-LMAC; CH07-c, C-7P:** complete privacy, relevance, live coordination and permission mechanisms. Current worker's explicit internal-use/visible-output distinction, Level 1 protected-boundary limits, influence removal, compartment restrictions and TSC exclusion are already present.
- **CH03-a/b and accepted source owners:** sealed roots/active batches, the twelve-field reading contract and quarantine/production boundaries remain unchanged. Full cross-batch reconciliation integration is not supplied here. **CH11:** complete CY-A/CY-B and other side paths; **CH12:** accumulated gaps, coverage and conflicts. Nightly activation, full chat synchronization, full action-result flow, world model and Wonder mechanism remain outside this post-root chapter.

## Additional undecided implementation slots

| Slot | Value | Boundary / owner |
|---|---|---|
| Fixed-file activation scan versus multi-batch reconciliation addressing | NOT DECIDED | Explicit source conflict; no sealed batch reopening or invented cross-batch cursor. |
| job_claimed acquisition-time field reconciliation: claimed_at versus locked_at | NOT DECIDED | Literal schema and conflicting paragraph retained without an alias. |
| All-other-root count versus preceding-root eligibility reconciliation | NOT DECIDED | The original input definition and semantic condition both remain. |
| Queue integration for an accepted careful fresh attempt after terminal failed job | NOT DECIDED | B9/B24 standalone acceptance does not supply a terminal-job rewrite. |
| Stage-event operation_key value for reading_written | NOT DECIDED | Generic event shape names operation_key; reading-specific payload names only reading_id; no value invented. |
| Per-profile snapshot_id value-form on no_update | NOT DECIDED | Source gives the field but does not fix its null/sentinel representation. |
| Exact OS locking API | NOT DECIDED | Non-blocking, process-scoped exclusivity and automatic crash release are required; no specific implementation selected. |
| Claim-renewal interval and intended-expiry window | NOT DECIDED | Diagnostic configuration only; no invented time value. |
| Specific mismatch-recovery sequence after defensive claim validation fails | NOT DECIDED | Mismatch cannot authorize commit; exact recovery steps are not supplied. |
| Nightly-batch activation | NOT DECIDED | Recognized trigger_source does not authorize activation. |
| Final empirically tested positional/per-mode retrieval quantities | NOT DECIDED | C-7F; Engine B's n=3 is not adopted as the worker limit. |
| Exact view significance thresholds, profile triggers and complete snapshot schema | NOT DECIDED | C-7M full source placement in CH06-d. |
| Whole chat-response synchronization with the async job | NOT DECIDED | CY-B / CH11; no reply wait is claimed. |
| Source-operation execution timeouts | NOT DECIDED | Existing seam owners; B9's retry deadline neither supplies nor changes these. |

## Review of plain gates and empty boxes

Each populated TOGETHER line names the actual connected rule, field, state or owner. Explicit enqueue, claim, instruction, lifecycle, mode-case, worker, sentinel and recovery steps link their rules; actual conditions remain gates rather than outputs relabeled as conditions. Atomic timestamps, identity fields and record discriminators have no invented failure mechanism. Fixed values and source-stated preservation/prohibition conditions are written directly where decided.

The current fields and USED BY cells were checked against the complete source section and accepted boundary sections, including every empty restriction/failure/gate box. The distinct locks, schema-versus-rule mode vocabulary, protected internal-use conditions, checkpoint order, no-result evidence, technical-failure exclusion and all RC cases were checked. BUILT relationships target only existing store/writer/quarantine components supported by V10's status table; the worker and instruction log remain DESIGNED.

## Appendix A carry-forward — this piece

| Part | Field or cell | Value |
|---|---|---|
| C-7GA.1 | Changes | NOT DECIDED |
| C-7GA.2 | Fed by | NOT DECIDED |
| C-7GA.3 | Changes | NOT DECIDED |
| C-7GA.3.1 | Changes | NOT DECIDED |
| C-7GA.3.1.1 | Fails closed by | NOT DECIDED |
| C-7GA.3.1.1 | Fed by | NOT DECIDED |
| C-7GA.3.1.1 | Gated by | NOT DECIDED |
| C-7GA.3.1.1 | Changes | NOT DECIDED |
| C-7GA.3.1.2 | Fails closed by | NOT DECIDED |
| C-7GA.3.1.2 | Fed by | NOT DECIDED |
| C-7GA.3.1.2 | Gated by | NOT DECIDED |
| C-7GA.3.1.2 | Changes | NOT DECIDED |
| C-7GA.3.2 | Fed by | NOT DECIDED |
| C-7GA.4 | Changes | NOT DECIDED |
| C-7GA.5 | Gated by | NOT DECIDED |
| C-7GA.5 | Changes | NOT DECIDED |
| C-7GA.5.1 | Changes | NOT DECIDED |
| C-7GA.5.1.1 | Fails closed by | NOT DECIDED |
| C-7GA.5.1.1 | Fed by | NOT DECIDED |
| C-7GA.5.1.1 | Gated by | NOT DECIDED |
| C-7GA.5.1.1 | Changes | NOT DECIDED |
| C-7GA.5.1.2 | Fails closed by | NOT DECIDED |
| C-7GA.5.1.2 | Fed by | NOT DECIDED |
| C-7GA.5.1.2 | Gated by | NOT DECIDED |
| C-7GA.5.1.2 | Changes | NOT DECIDED |
| C-7GA.5.1.3 | Fed by | NOT DECIDED |
| C-7GA.5.1.3 | Gated by | NOT DECIDED |
| C-7GA.5.1.3 | Changes | NOT DECIDED |
| C-7GA.5.1.4 | Fed by | NOT DECIDED |
| C-7GA.5.1.4 | Gated by | NOT DECIDED |
| C-7GA.5.1.4 | Changes | NOT DECIDED |
| C-7GA.5.1.5 | Fed by | NOT DECIDED |
| C-7GA.5.1.5 | Gated by | NOT DECIDED |
| C-7GA.5.1.5 | Changes | NOT DECIDED |
| C-7GA.5.1.6 | Fed by | NOT DECIDED |
| C-7GA.5.1.6 | Gated by | NOT DECIDED |
| C-7GA.5.1.6 | Changes | NOT DECIDED |
| C-7GA.5.1.7 | Fed by | NOT DECIDED |
| C-7GA.5.1.7 | Gated by | NOT DECIDED |
| C-7GA.5.1.7 | Changes | NOT DECIDED |
| C-7GA.5.1.8 | Must never | NOT DECIDED |
| C-7GA.5.1.8 | Fails closed by | NOT DECIDED |
| C-7GA.5.1.8 | Fed by | NOT DECIDED |
| C-7GA.5.1.8 | Gated by | NOT DECIDED |
| C-7GA.5.1.8 | Changes | NOT DECIDED |
| C-7GA.5.2 | Changes | NOT DECIDED |
| C-7GA.5.2.1 | Fails closed by | NOT DECIDED |
| C-7GA.5.2.1 | Fed by | NOT DECIDED |
| C-7GA.5.2.1 | Gated by | NOT DECIDED |
| C-7GA.5.2.1 | Changes | NOT DECIDED |
| C-7GA.5.2.2 | Must never | NOT DECIDED |
| C-7GA.5.2.2 | Fails closed by | NOT DECIDED |
| C-7GA.5.2.2 | Fed by | NOT DECIDED |
| C-7GA.5.2.2 | Gated by | NOT DECIDED |
| C-7GA.5.2.2 | Changes | NOT DECIDED |
| C-7GA.5.2.3 | Gated by | NOT DECIDED |
| C-7GA.5.2.3 | Changes | NOT DECIDED |
| C-7GA.5.2.3.1 | Fed by | NOT DECIDED |
| C-7GA.5.2.3.1 | Changes | NOT DECIDED |
| C-7GA.5.2.3.2 | Gated by | NOT DECIDED |
| C-7GA.5.2.3.2 | Changes | NOT DECIDED |
| C-7GA.5.2.3.3 | Fed by | NOT DECIDED |
| C-7GA.5.2.3.3 | Changes | NOT DECIDED |
| C-7GA.5.2.3.4 | Gated by | NOT DECIDED |
| C-7GA.5.2.3.4 | Changes | NOT DECIDED |
| C-7GA.5.2.4 | Must never | NOT DECIDED |
| C-7GA.5.2.4 | Fails closed by | NOT DECIDED |
| C-7GA.5.2.4 | Fed by | NOT DECIDED |
| C-7GA.5.2.4 | Gated by | NOT DECIDED |
| C-7GA.5.2.4 | Changes | NOT DECIDED |
| C-7GA.5.2.5 | Must never | NOT DECIDED |
| C-7GA.5.2.5 | Fails closed by | NOT DECIDED |
| C-7GA.5.2.5 | Fed by | NOT DECIDED |
| C-7GA.5.2.5 | Gated by | NOT DECIDED |
| C-7GA.5.2.5 | Changes | NOT DECIDED |
| C-7GA.5.3 | Changes | NOT DECIDED |
| C-7GA.5.3.1 | Fails closed by | NOT DECIDED |
| C-7GA.5.3.1 | Fed by | NOT DECIDED |
| C-7GA.5.3.1 | Gated by | NOT DECIDED |
| C-7GA.5.3.1 | Changes | NOT DECIDED |
| C-7GA.5.3.2 | Must never | NOT DECIDED |
| C-7GA.5.3.2 | Fails closed by | NOT DECIDED |
| C-7GA.5.3.2 | Fed by | NOT DECIDED |
| C-7GA.5.3.2 | Gated by | NOT DECIDED |
| C-7GA.5.3.2 | Changes | NOT DECIDED |
| C-7GA.5.3.3 | Fails closed by | NOT DECIDED |
| C-7GA.5.3.3 | Gated by | NOT DECIDED |
| C-7GA.5.3.3 | Changes | NOT DECIDED |
| C-7GA.5.3.3.1 | Changes | NOT DECIDED |
| C-7GA.5.3.3.2 | Changes | NOT DECIDED |
| C-7GA.5.3.3.3 | Fed by | NOT DECIDED |
| C-7GA.5.3.3.3 | Changes | NOT DECIDED |
| C-7GA.5.3.4 | Must never | NOT DECIDED |
| C-7GA.5.3.4 | Fails closed by | NOT DECIDED |
| C-7GA.5.3.4 | Fed by | NOT DECIDED |
| C-7GA.5.3.4 | Gated by | NOT DECIDED |
| C-7GA.5.3.4 | Changes | NOT DECIDED |
| C-7GA.5.3.5 | Fails closed by | NOT DECIDED |
| C-7GA.5.3.5 | Fed by | NOT DECIDED |
| C-7GA.5.3.5 | Gated by | NOT DECIDED |
| C-7GA.5.3.5 | Changes | NOT DECIDED |
| C-7GA.5.3.6 | Fails closed by | NOT DECIDED |
| C-7GA.5.3.6 | Fed by | NOT DECIDED |
| C-7GA.5.3.6 | Gated by | NOT DECIDED |
| C-7GA.5.3.6 | Changes | NOT DECIDED |
| C-7GA.5.3.7 | Fails closed by | NOT DECIDED |
| C-7GA.5.3.7 | Fed by | NOT DECIDED |
| C-7GA.5.3.7 | Gated by | NOT DECIDED |
| C-7GA.5.3.7 | Changes | NOT DECIDED |
| C-7GA.5.3.8 | Fails closed by | NOT DECIDED |
| C-7GA.5.3.8 | Fed by | NOT DECIDED |
| C-7GA.5.3.8 | Gated by | NOT DECIDED |
| C-7GA.5.3.8 | Changes | NOT DECIDED |
| C-7GA.5.3.9 | Fed by | NOT DECIDED |
| C-7GA.5.3.9 | Gated by | NOT DECIDED |
| C-7GA.5.3.9 | Changes | NOT DECIDED |
| C-7GA.5.3.10 | Gated by | NOT DECIDED |
| C-7GA.5.3.10 | Changes | NOT DECIDED |
| C-7GA.5.3.10.1 | Must never | NOT DECIDED |
| C-7GA.5.3.10.1 | Fails closed by | NOT DECIDED |
| C-7GA.5.3.10.1 | Fed by | NOT DECIDED |
| C-7GA.5.3.10.1 | Gated by | NOT DECIDED |
| C-7GA.5.3.10.1 | Changes | NOT DECIDED |
| C-7GA.5.3.10.2 | Gated by | NOT DECIDED |
| C-7GA.5.3.10.2 | Changes | NOT DECIDED |
| C-7GA.5.3.10.2.1 | Gated by | NOT DECIDED |
| C-7GA.5.3.10.2.1 | Changes | NOT DECIDED |
| C-7GA.5.3.10.2.2 | Gated by | NOT DECIDED |
| C-7GA.5.3.10.2.2 | Changes | NOT DECIDED |
| C-7GA.5.3.10.3 | Fails closed by | NOT DECIDED |
| C-7GA.5.3.10.3 | Fed by | NOT DECIDED |
| C-7GA.5.3.10.3 | Gated by | NOT DECIDED |
| C-7GA.5.3.10.3 | Changes | NOT DECIDED |
| C-7GA.5.3.10.4 | Fed by | NOT DECIDED |
| C-7GA.5.3.10.4 | Gated by | NOT DECIDED |
| C-7GA.5.3.10.4 | Changes | NOT DECIDED |
| C-7GA.5.4 | Changes | NOT DECIDED |
| C-7GA.5.4.1 | Fails closed by | NOT DECIDED |
| C-7GA.5.4.1 | Fed by | NOT DECIDED |
| C-7GA.5.4.1 | Gated by | NOT DECIDED |
| C-7GA.5.4.1 | Changes | NOT DECIDED |
| C-7GA.5.4.2 | Must never | NOT DECIDED |
| C-7GA.5.4.2 | Fails closed by | NOT DECIDED |
| C-7GA.5.4.2 | Fed by | NOT DECIDED |
| C-7GA.5.4.2 | Gated by | NOT DECIDED |
| C-7GA.5.4.2 | Changes | NOT DECIDED |
| C-7GA.5.4.3 | Fed by | NOT DECIDED |
| C-7GA.5.4.3 | Gated by | NOT DECIDED |
| C-7GA.5.4.3 | Changes | NOT DECIDED |
| C-7GA.5.4.4 | Must never | NOT DECIDED |
| C-7GA.5.4.4 | Fails closed by | NOT DECIDED |
| C-7GA.5.4.4 | Fed by | NOT DECIDED |
| C-7GA.5.4.4 | Gated by | NOT DECIDED |
| C-7GA.5.4.4 | Changes | NOT DECIDED |
| C-7GA.5.4.5 | Must never | NOT DECIDED |
| C-7GA.5.4.5 | Fails closed by | NOT DECIDED |
| C-7GA.5.4.5 | Fed by | NOT DECIDED |
| C-7GA.5.4.5 | Gated by | NOT DECIDED |
| C-7GA.5.4.5 | Changes | NOT DECIDED |
| C-7GA.5.4.6 | Fed by | NOT DECIDED |
| C-7GA.5.4.6 | Gated by | NOT DECIDED |
| C-7GA.5.4.6 | Changes | NOT DECIDED |
| C-7GA.5.5 | Changes | NOT DECIDED |
| C-7GA.5.5.1 | Fails closed by | NOT DECIDED |
| C-7GA.5.5.1 | Fed by | NOT DECIDED |
| C-7GA.5.5.1 | Gated by | NOT DECIDED |
| C-7GA.5.5.1 | Changes | NOT DECIDED |
| C-7GA.5.5.2 | Must never | NOT DECIDED |
| C-7GA.5.5.2 | Fails closed by | NOT DECIDED |
| C-7GA.5.5.2 | Fed by | NOT DECIDED |
| C-7GA.5.5.2 | Gated by | NOT DECIDED |
| C-7GA.5.5.2 | Changes | NOT DECIDED |
| C-7GA.5.5.3 | Must never | NOT DECIDED |
| C-7GA.5.5.3 | Fails closed by | NOT DECIDED |
| C-7GA.5.5.3 | Fed by | NOT DECIDED |
| C-7GA.5.5.3 | Gated by | NOT DECIDED |
| C-7GA.5.5.3 | Changes | NOT DECIDED |
| C-7GA.5.5.4 | Must never | NOT DECIDED |
| C-7GA.5.5.4 | Fails closed by | NOT DECIDED |
| C-7GA.5.5.4 | Fed by | NOT DECIDED |
| C-7GA.5.5.4 | Gated by | NOT DECIDED |
| C-7GA.5.5.4 | Changes | NOT DECIDED |
| C-7GA.5.5.5 | Must never | NOT DECIDED |
| C-7GA.5.5.5 | Fails closed by | NOT DECIDED |
| C-7GA.5.5.5 | Fed by | NOT DECIDED |
| C-7GA.5.5.5 | Gated by | NOT DECIDED |
| C-7GA.5.5.5 | Changes | NOT DECIDED |
| C-7GA.5.5.6 | Must never | NOT DECIDED |
| C-7GA.5.5.6 | Fails closed by | NOT DECIDED |
| C-7GA.5.5.6 | Fed by | NOT DECIDED |
| C-7GA.5.5.6 | Gated by | NOT DECIDED |
| C-7GA.5.5.6 | Changes | NOT DECIDED |
| C-7GA.6.1 | Fails closed by | NOT DECIDED |
| C-7GA.6.1 | Fed by | NOT DECIDED |
| C-7GA.6.1 | Gated by | NOT DECIDED |
| C-7GA.6.1 | Changes | NOT DECIDED |
| C-7GA.6.2 | Gated by | NOT DECIDED |
| C-7GA.6.2 | Changes | NOT DECIDED |
| C-7GA.6.3 | Fed by | NOT DECIDED |
| C-7GA.6.3 | Changes | NOT DECIDED |
| C-7GA.6.4 | Fed by | NOT DECIDED |
| C-7GA.6.4 | Changes | NOT DECIDED |
| C-7GA.6.5 | Fails closed by | NOT DECIDED |
| C-7GA.6.5 | Gated by | NOT DECIDED |
| C-7GA.6.5 | Changes | NOT DECIDED |
| C-7GA.7.1 | Changes | NOT DECIDED |
| C-7GA.7.1.1 | Must never | NOT DECIDED |
| C-7GA.7.1.1 | Fails closed by | NOT DECIDED |
| C-7GA.7.1.1 | Fed by | NOT DECIDED |
| C-7GA.7.1.1 | Gated by | NOT DECIDED |
| C-7GA.7.1.1 | Changes | NOT DECIDED |
| C-7GA.7.1.2 | Fed by | NOT DECIDED |
| C-7GA.7.1.2 | Gated by | NOT DECIDED |
| C-7GA.7.1.2 | Changes | NOT DECIDED |
| C-7GA.7.1.3 | Must never | NOT DECIDED |
| C-7GA.7.1.3 | Fails closed by | NOT DECIDED |
| C-7GA.7.1.3 | Fed by | NOT DECIDED |
| C-7GA.7.1.3 | Gated by | NOT DECIDED |
| C-7GA.7.1.3 | Changes | NOT DECIDED |
| C-7GA.7.1.4 | Must never | NOT DECIDED |
| C-7GA.7.1.4 | Fails closed by | NOT DECIDED |
| C-7GA.7.1.4 | Fed by | NOT DECIDED |
| C-7GA.7.1.4 | Gated by | NOT DECIDED |
| C-7GA.7.1.4 | Changes | NOT DECIDED |
| C-7GA.7.1.5 | Fed by | NOT DECIDED |
| C-7GA.7.1.5 | Gated by | NOT DECIDED |
| C-7GA.7.1.5 | Changes | NOT DECIDED |
| C-7GA.7.2 | Gated by | NOT DECIDED |
| C-7GA.7.2 | Changes | NOT DECIDED |
| C-7GA.7.3 | Gated by | NOT DECIDED |
| C-7GA.7.3 | Changes | NOT DECIDED |
| C-7GA.7.4 | Fails closed by | NOT DECIDED |
| C-7GA.7.4 | Fed by | NOT DECIDED |
| C-7GA.7.4 | Changes | NOT DECIDED |
| C-7GA.7.5 | Changes | NOT DECIDED |
| C-7GA.7.6 | Gated by | NOT DECIDED |
| C-7GA.7.6 | Changes | NOT DECIDED |
| C-7GA.7.7 | Fed by | NOT DECIDED |
| C-7GA.7.7 | Changes | NOT DECIDED |
| C-7GA.8 | Changes | NOT DECIDED |
| C-7GA.8.1 | Changes | NOT DECIDED |
| C-7GA.8.1.1 | Fails closed by | NOT DECIDED |
| C-7GA.8.1.1 | Fed by | NOT DECIDED |
| C-7GA.8.1.1 | Gated by | NOT DECIDED |
| C-7GA.8.1.1 | Changes | NOT DECIDED |
| C-7GA.8.1.2 | Fails closed by | NOT DECIDED |
| C-7GA.8.1.2 | Fed by | NOT DECIDED |
| C-7GA.8.1.2 | Gated by | NOT DECIDED |
| C-7GA.8.1.2 | Changes | NOT DECIDED |
| C-7GA.8.1.3 | Fails closed by | NOT DECIDED |
| C-7GA.8.1.3 | Fed by | NOT DECIDED |
| C-7GA.8.1.3 | Gated by | NOT DECIDED |
| C-7GA.8.1.3 | Changes | NOT DECIDED |
| C-7GA.8.1.4 | Must never | NOT DECIDED |
| C-7GA.8.1.4 | Fails closed by | NOT DECIDED |
| C-7GA.8.1.4 | Fed by | NOT DECIDED |
| C-7GA.8.1.4 | Gated by | NOT DECIDED |
| C-7GA.8.1.4 | Changes | NOT DECIDED |
| C-7GA.8.1.5 | Fed by | NOT DECIDED |
| C-7GA.8.1.5 | Gated by | NOT DECIDED |
| C-7GA.8.1.5 | Changes | NOT DECIDED |
| C-7GA.8.1.6 | Fails closed by | NOT DECIDED |
| C-7GA.8.1.6 | Fed by | NOT DECIDED |
| C-7GA.8.1.6 | Gated by | NOT DECIDED |
| C-7GA.8.1.6 | Changes | NOT DECIDED |
| C-7GA.8.1.7 | Fails closed by | NOT DECIDED |
| C-7GA.8.1.7 | Fed by | NOT DECIDED |
| C-7GA.8.1.7 | Gated by | NOT DECIDED |
| C-7GA.8.1.7 | Changes | NOT DECIDED |
| C-7GA.8.1.8 | Gated by | NOT DECIDED |
| C-7GA.8.1.8 | Changes | NOT DECIDED |
| C-7GA.8.1.8.1 | Gated by | NOT DECIDED |
| C-7GA.8.1.8.1 | Changes | NOT DECIDED |
| C-7GA.8.1.8.2 | Fed by | NOT DECIDED |
| C-7GA.8.1.8.2 | Gated by | NOT DECIDED |
| C-7GA.8.1.8.2 | Changes | NOT DECIDED |
| C-7GA.8.1.8.3 | Fed by | NOT DECIDED |
| C-7GA.8.1.8.3 | Gated by | NOT DECIDED |
| C-7GA.8.1.8.3 | Changes | NOT DECIDED |
| C-7GA.8.1.8.4 | Fails closed by | NOT DECIDED |
| C-7GA.8.1.8.4 | Fed by | NOT DECIDED |
| C-7GA.8.1.8.4 | Gated by | NOT DECIDED |
| C-7GA.8.1.8.4 | Changes | NOT DECIDED |
| C-7GA.8.1.8.5 | Fed by | NOT DECIDED |
| C-7GA.8.1.8.5 | Gated by | NOT DECIDED |
| C-7GA.8.1.8.5 | Changes | NOT DECIDED |
| C-7GA.8.1.8.6 | Fails closed by | NOT DECIDED |
| C-7GA.8.1.8.6 | Fed by | NOT DECIDED |
| C-7GA.8.1.8.6 | Gated by | NOT DECIDED |
| C-7GA.8.1.8.6 | Changes | NOT DECIDED |
| C-7GA.8.1.8.7 | Fed by | NOT DECIDED |
| C-7GA.8.1.8.7 | Gated by | NOT DECIDED |
| C-7GA.8.1.8.7 | Changes | NOT DECIDED |
| C-7GA.8.1.8.8 | Must never | NOT DECIDED |
| C-7GA.8.1.8.8 | Fails closed by | NOT DECIDED |
| C-7GA.8.1.8.8 | Fed by | NOT DECIDED |
| C-7GA.8.1.8.8 | Gated by | NOT DECIDED |
| C-7GA.8.1.8.8 | Changes | NOT DECIDED |
| C-7GA.8.1.8.9 | Must never | NOT DECIDED |
| C-7GA.8.1.8.9 | Fails closed by | NOT DECIDED |
| C-7GA.8.1.8.9 | Fed by | NOT DECIDED |
| C-7GA.8.1.8.9 | Gated by | NOT DECIDED |
| C-7GA.8.1.8.9 | Changes | NOT DECIDED |
| C-7GA.8.1.8.10 | Fails closed by | NOT DECIDED |
| C-7GA.8.1.8.10 | Fed by | NOT DECIDED |
| C-7GA.8.1.8.10 | Gated by | NOT DECIDED |
| C-7GA.8.1.8.10 | Changes | NOT DECIDED |
| C-7GA.8.1.8.11 | Fails closed by | NOT DECIDED |
| C-7GA.8.1.8.11 | Fed by | NOT DECIDED |
| C-7GA.8.1.8.11 | Gated by | NOT DECIDED |
| C-7GA.8.1.8.11 | Changes | NOT DECIDED |
| C-7GA.8.1.9 | Fed by | NOT DECIDED |
| C-7GA.8.1.9 | Gated by | NOT DECIDED |
| C-7GA.8.1.9 | Changes | NOT DECIDED |
| C-7GA.8.1.10 | Fed by | NOT DECIDED |
| C-7GA.8.1.10 | Gated by | NOT DECIDED |
| C-7GA.8.1.10 | Changes | NOT DECIDED |
| C-7GA.8.1.11 | Fails closed by | NOT DECIDED |
| C-7GA.8.1.11 | Fed by | NOT DECIDED |
| C-7GA.8.1.11 | Gated by | NOT DECIDED |
| C-7GA.8.1.11 | Changes | NOT DECIDED |
| C-7GA.8.1.12 | Fails closed by | NOT DECIDED |
| C-7GA.8.1.12 | Fed by | NOT DECIDED |
| C-7GA.8.1.12 | Gated by | NOT DECIDED |
| C-7GA.8.1.12 | Changes | NOT DECIDED |
| C-7GA.8.1.13 | Must never | NOT DECIDED |
| C-7GA.8.1.13 | Fails closed by | NOT DECIDED |
| C-7GA.8.1.13 | Fed by | NOT DECIDED |
| C-7GA.8.1.13 | Gated by | NOT DECIDED |
| C-7GA.8.1.13 | Changes | NOT DECIDED |
| C-7GA.8.2 | Changes | NOT DECIDED |
| C-7GA.8.2.1 | Fails closed by | NOT DECIDED |
| C-7GA.8.2.1 | Fed by | NOT DECIDED |
| C-7GA.8.2.1 | Gated by | NOT DECIDED |
| C-7GA.8.2.1 | Changes | NOT DECIDED |
| C-7GA.8.2.2 | Fails closed by | NOT DECIDED |
| C-7GA.8.2.2 | Fed by | NOT DECIDED |
| C-7GA.8.2.2 | Gated by | NOT DECIDED |
| C-7GA.8.2.2 | Changes | NOT DECIDED |
| C-7GA.8.2.3 | Gated by | NOT DECIDED |
| C-7GA.8.2.3 | Changes | NOT DECIDED |
| C-7GA.8.2.3.1 | Changes | NOT DECIDED |
| C-7GA.8.2.3.2 | Gated by | NOT DECIDED |
| C-7GA.8.2.3.2 | Changes | NOT DECIDED |
| C-7GA.8.2.3.3 | Fed by | NOT DECIDED |
| C-7GA.8.2.3.3 | Changes | NOT DECIDED |
| C-7GA.8.2.4 | Must never | NOT DECIDED |
| C-7GA.8.2.4 | Fails closed by | NOT DECIDED |
| C-7GA.8.2.4 | Fed by | NOT DECIDED |
| C-7GA.8.2.4 | Gated by | NOT DECIDED |
| C-7GA.8.2.4 | Changes | NOT DECIDED |
| C-7GA.8.2.5 | Fails closed by | NOT DECIDED |
| C-7GA.8.2.5 | Fed by | NOT DECIDED |
| C-7GA.8.2.5 | Gated by | NOT DECIDED |
| C-7GA.8.2.5 | Changes | NOT DECIDED |
| C-7GA.8.2.6 | Gated by | NOT DECIDED |
| C-7GA.8.2.6 | Changes | NOT DECIDED |
| C-7GA.8.2.6.1 | Fails closed by | NOT DECIDED |
| C-7GA.8.2.6.1 | Fed by | NOT DECIDED |
| C-7GA.8.2.6.1 | Gated by | NOT DECIDED |
| C-7GA.8.2.6.1 | Changes | NOT DECIDED |
| C-7GA.8.2.6.2 | Fails closed by | NOT DECIDED |
| C-7GA.8.2.6.2 | Fed by | NOT DECIDED |
| C-7GA.8.2.6.2 | Gated by | NOT DECIDED |
| C-7GA.8.2.6.2 | Changes | NOT DECIDED |
| C-7GA.8.2.6.3 | Fails closed by | NOT DECIDED |
| C-7GA.8.2.6.3 | Fed by | NOT DECIDED |
| C-7GA.8.2.6.3 | Gated by | NOT DECIDED |
| C-7GA.8.2.6.3 | Changes | NOT DECIDED |
| C-7GA.8.2.6.4 | Fed by | NOT DECIDED |
| C-7GA.8.2.6.4 | Gated by | NOT DECIDED |
| C-7GA.8.2.6.4 | Changes | NOT DECIDED |
| C-7GA.8.2.7 | Fails closed by | NOT DECIDED |
| C-7GA.8.2.7 | Fed by | NOT DECIDED |
| C-7GA.8.2.7 | Gated by | NOT DECIDED |
| C-7GA.8.2.7 | Changes | NOT DECIDED |
| C-7GA.10 | Changes | NOT DECIDED |
| C-7GA.10.1 | Gated by | NOT DECIDED |
| C-7GA.10.1 | Changes | NOT DECIDED |
| C-7GA.10.1.1 | Gated by | NOT DECIDED |
| C-7GA.10.1.1 | Changes | NOT DECIDED |
| C-7GA.10.1.2 | Gated by | NOT DECIDED |
| C-7GA.10.1.2 | Changes | NOT DECIDED |
| C-7GA.10.1.3 | Gated by | NOT DECIDED |
| C-7GA.10.1.3 | Changes | NOT DECIDED |
| C-7GA.10.1.4 | Gated by | NOT DECIDED |
| C-7GA.10.1.4 | Changes | NOT DECIDED |
| C-7GA.10.1.5 | Gated by | NOT DECIDED |
| C-7GA.10.1.5 | Changes | NOT DECIDED |
| C-7GA.10.2 | Changes | NOT DECIDED |
| C-7GA.10.2.1 | Gated by | NOT DECIDED |
| C-7GA.10.2.1 | Changes | NOT DECIDED |
| C-7GA.10.2.2 | Gated by | NOT DECIDED |
| C-7GA.10.2.2 | Changes | NOT DECIDED |
| C-7GA.10.2.3 | Gated by | NOT DECIDED |
| C-7GA.10.2.3 | Changes | NOT DECIDED |
| C-7GA.10.2.4 | Gated by | NOT DECIDED |
| C-7GA.10.2.4 | Changes | NOT DECIDED |
| C-7GA.10.2.5 | Gated by | NOT DECIDED |
| C-7GA.10.2.5 | Changes | NOT DECIDED |
| C-7GA.10.2.6 | Gated by | NOT DECIDED |
| C-7GA.10.2.6 | Changes | NOT DECIDED |
| C-7GA.10.2.7 | Gated by | NOT DECIDED |
| C-7GA.10.2.7 | Changes | NOT DECIDED |
| C-7GA.10.3 | Gated by | NOT DECIDED |
| C-7GA.10.3 | Changes | NOT DECIDED |
| C-7GA.11.1 | Changes | NOT DECIDED |
| C-7GA.11.2 | Changes | NOT DECIDED |
| C-7GA.11.3 | Gated by | NOT DECIDED |
| C-7GA.11.4 | Fed by | NOT DECIDED |
| C-7GA.11.4 | Changes | NOT DECIDED |
| C-7GA.11.5.1 | Changes | NOT DECIDED |
| C-7GA.11.7.1 | Changes | NOT DECIDED |
| C-7GA.11.7.3 | Changes | NOT DECIDED |
| C-7GA.11.7.4 | Fed by | NOT DECIDED |
| C-7GA.12 | Gated by | NOT DECIDED |
| C-7GA.12 | Changes | NOT DECIDED |
| C-7GA.12.1 | Changes | NOT DECIDED |
| C-7GA.12.2 | Changes | NOT DECIDED |
| C-7GA.12.3 | Fed by | NOT DECIDED |
| C-7GA.12.3 | Gated by | NOT DECIDED |
| C-7GA.12.3 | Changes | NOT DECIDED |
| C-7GA.12.4 | Must never | NOT DECIDED |
| C-7GA.12.4 | Fails closed by | NOT DECIDED |
| C-7GA.12.4 | Fed by | NOT DECIDED |
| C-7GA.12.4 | Gated by | NOT DECIDED |
| C-7GA.12.4 | Changes | NOT DECIDED |
| C-7GA.12.5 | Must never | NOT DECIDED |
| C-7GA.12.5 | Fails closed by | NOT DECIDED |
| C-7GA.12.5 | Fed by | NOT DECIDED |
| C-7GA.12.5 | Gated by | NOT DECIDED |
| C-7GA.12.5 | Changes | NOT DECIDED |
| C-7GA.12.6 | Must never | NOT DECIDED |
| C-7GA.12.6 | Fails closed by | NOT DECIDED |
| C-7GA.12.6 | Fed by | NOT DECIDED |
| C-7GA.12.6 | Gated by | NOT DECIDED |
| C-7GA.12.6 | Changes | NOT DECIDED |
| C-7GA.13 | Changes | NOT DECIDED |
| C-7GA.13.1 | Gated by | NOT DECIDED |
| C-7GA.13.1 | Changes | NOT DECIDED |
| C-7GA.13.2 | Changes | NOT DECIDED |
| C-7GA.13.3 | Fed by | NOT DECIDED |
| C-7GA.13.3 | Changes | NOT DECIDED |
| C-7GA.13.4 | Changes | NOT DECIDED |
| C-7GA.13.6 | Fed by | NOT DECIDED |
| C-7GA.13.6 | Changes | NOT DECIDED |
| C-7GA.13.7 | Changes | NOT DECIDED |
| C-7GA.13.9 | Changes | NOT DECIDED |
| C-7GA.13.10 | Gated by | NOT DECIDED |
| C-7GA.13.10 | Changes | NOT DECIDED |
| C-7GA.14 | Changes | NOT DECIDED |
| C-7GA.14.1 | Fed by | NOT DECIDED |
| C-7GA.14.1 | Changes | NOT DECIDED |
| C-7GA.14.2 | Fed by | NOT DECIDED |
| C-7GA.14.2 | Changes | NOT DECIDED |
| C-7GA.14.3 | Fed by | NOT DECIDED |
| C-7GA.14.3 | Changes | NOT DECIDED |

## Retained plain-gate inventory

All populated TOGETHER lines name an owning or connected card except one plain gate: C-7GA.3.1's Gated by line, under which Ness deliberately enables the queue before it activates, a source-defined personal activation condition.

## Source coverage added by CH05-b

| Source | Scope read | Landing / exclusion |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: §7G-A in full, all 387 lines including record shapes, mode cases, worker substeps, sentinels and RC-1–RC-8; authoritative status table for exact BUILT targets. | C-7GA.1–13, all queue/pass/activation/claim/sentinel fields, states, mode cases, ordered worker and recovery; exact source discrepancies preserved. |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped: Complete C-7GA, C-STORE, C-READ, C-ENGINE-AB, C-ENGINE-C and C-13 paragraphs. | Root handoffs, eight incoming continuations, seven path-use rows, protected build order and explicit Map/V10 failure wording conflict. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md` | Scoped: §§1–11 in full; §§12–14 not credited. Current placement is worker-consumed scope and interfaces; complete generic machinery deferred to CH05-d. | C-7GA.14 and consumed identity/admission/held/recovery boundaries; full R0–R4, records, classes, recovery and logging CH05-d. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: Standalone acceptance, identity and scope evidence only. | Receipt identity/acceptance evidence; project workflow excluded. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md` | Scoped: §§3,4,7,13 in full; current technical/substantive admission consumption and accepted-value status, full generic records CH05-d. | C-7GA.14.1–3 and shared C-7G.9, both technical bounds/gaps and later-episode ordinal-1 conditions; complete versioned config and episode records CH05-d. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: Current standalone design acceptance and identity evidence, not integration or runtime permission. | Receipt identity/status evidence; no runtime or integration claim. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md` | Whole: Complete coordination note; current worker boundaries use §2, full generic ownership/protection placement CH05-d, project workflow excluded. | C-7GA.14 retry versus reread and held/terminal boundaries; complete generic coordination with CH05-d; workflow/audit procedures excluded. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: Standalone acceptance and identity evidence; no independent architecture inferred from the receipt. | Receipt identity/acceptance evidence; no separate mechanism or runtime permission. |

## Coverage matrix — cumulative carried inventory







The following inventory retains the preceding pieces’ placements and read status. This piece’s additional placements and deferrals are in the source-scope table above; inherited notes are not fresh whole-read claims.
### File coverage

| Row | Source | Read scope | Placement |
|---|---|---|---|
| F001 | `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped read in CH04-b: §0B; §6A SCHEMA CONSTRAINTS; §6B schema/status boundary; full §7E-TSC §§1–31. Prior read credits retained. | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.1; C-STORE.2; C-STORE.3; CY-A Chapter 3-b: C-READ and its v1 record, validator, writer, quarantine, production-boundary and operation-record sub-parts; CY-A/CY-F reading-write interfaces. Chapter 3-c: governing checks for C-READ.10; A2/firmness additions stay ACCEPTED, never BUILT. Chapter 3-d: source-status and no-production-write boundaries; governing operational living-memory rule at C-READ.11.9.4.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.3, C-ENGINE-C.3.1, C-ENGINE-C.3.2, C-ENGINE-C.3.3, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.11.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1, C-ENGINE-AB.1.1, C-ENGINE-AB.1.2, C-ENGINE-AB.1.3, C-ENGINE-AB.2, C-ENGINE-AB.2.1, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.1, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.2.4, C-ENGINE-AB.3, C-ENGINE-AB.4, C-ENGINE-AB.5, C-ENGINE-AB.6, C-ENGINE-AB.8, C-ENGINE-AB.9.; CH03-k: C-INDEX, C-INDEX.1, C-INDEX.1.1, C-INDEX.1.2, C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.1, C-INDEX.4.2, C-INDEX.4.3, C-INDEX.4.4, C-INDEX.4.5, C-INDEX.4.7, C-INDEX.4.8, C-INDEX.5, C-INDEX.6.; CH03-l: C-GOLD, C-GOLD.2, C-GOLD.2.1, C-GOLD.3, C-GOLD.3.1, C-GOLD.6, C-GOLD.6.1, C-GOLD.6.2, C-GOLD.6.3, C-GOLD.7, C-GOLD.7.4.; CH03-o: C-INGEST, C-INGEST.1, C-INGEST.2, C-INGEST.3, C-INGEST.4, C-INGEST.4.1, C-INGEST.4.2, C-INGEST.4.3, C-INGEST.4.4, C-INGEST.4.5, C-INGEST.4.6, C-INGEST.4.7, C-INGEST.4.8, C-INGEST.4.8.1, C-INGEST.4.8.2, C-INGEST.4.8.3, C-INGEST.4.8.4, C-INGEST.4.9, C-INGEST.6.; CH03-p: C-DETECT, C-DETECT.1, C-DETECT.1.1, C-DETECT.1.3, C-DETECT.2, C-DETECT.2.1, C-DETECT.2.2, C-DETECT.2.3, C-DETECT.2.4, C-DETECT.2.5, C-DETECT.3, C-DETECT.3.1, C-DETECT.3.2, C-DETECT.3.3, C-DETECT.3.4, C-DETECT.3.5, C-DETECT.3.6, C-DETECT.4.1.; CH04-a: C-7E, C-7E.1, C-7E.1.1, C-7E.1.2, C-7E.2, C-7E.3, C-7E.4, C-7E.5, C-7E.5.1, C-7E.5.2, C-7E.5.3, C-7E.5.4, C-7E.5.5, C-7E.5.6, C-7E.6, C-7E.6.1, C-7E.6.2, C-7E.6.3, C-7E.6.4, C-7E.6.5, C-7E.6.6, C-7E.6.7, C-7E.7, C-7E.8, C-7E.8.1, C-7E.8.2, C-7E.8.3, C-7E.8.4, C-7E.9, C-7E.9.1, C-7E.9.2, C-7E.9.2.1, C-7E.9.2.2, C-7E.9.2.3, C-7E.9.2.4, C-7E.9.3, C-7E.9.3.1, C-7E.9.3.2, C-7E.9.3.3, C-7E.9.3.4, C-7E.9.3.5, C-7E.9.3.6, C-7E.9.4, C-7E.10, C-7E.10.1, C-7E.10.2, C-7E.11, C-7E.12, C-7E.13, C-7E.13.1, C-7E.13.4, C-7E.13.5, C-7E.13.6. CH04-b: see the exact source-scope and landing table above.  CH04-c: scoped read; exact scope and placement in the current source table.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained. |
| F002 | `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Scoped read in CH04-b: §3N; inspection conflict. Prior read credits retained. | EXCLUDED: interaction/workflow guidance under §1.3 and §2.4. NOT PLACED: remaining behavior belongs to other component groups.; Chapter 3-a: C-STORE.2.3 Chapter 3-b: C-READ.1 confidence semantics and C-READ.2 uncertainty-preserving shape gate; remaining scope retained. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.2, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.8.; CH03-l: C-GOLD, C-GOLD.2, C-GOLD.2.1, C-GOLD.3, C-GOLD.3.1, C-GOLD.4, C-GOLD.4.1, C-GOLD.4.2, C-GOLD.4.3, C-GOLD.4.4, C-GOLD.4.5, C-GOLD.4.6, C-GOLD.5, C-GOLD.6, C-GOLD.6.1, C-GOLD.6.3, C-GOLD.8.3, C-GOLD.8.5.10, C-GOLD.8.5.11.; CH04-a: C-7E, C-7E.1.2, C-7E.5.2, C-7E.6.1, C-7E.6.2, C-7E.7, C-7E.8.4, C-7E.13.3. CH04-b: see the exact source-scope and landing table above. |
| F003 | `01_AUTHORITATIVE/cursorrules` | Scoped reread for CH03-o; prior whole-read credit retained where previously recorded | EXCLUDED: coding-process rules under §1.3. NOT PLACED: built-code boundaries belong to store, reader and code-boundary groups. Chapter 3-b: C-READ.1.12 per-store/global-key conflict and C-READ.3 shared write boundary; workflow remains excluded. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB.5.; CH03-k: C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.6.; CH03-l: C-GOLD, C-GOLD.9.; CH03-o: C-INGEST, C-INGEST.4, C-INGEST.4.7, C-INGEST.6. |
| F004 | `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Scoped read in CH04-b: Embedded TSC §§15–16; conflicting inspection and failed-authorization text. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. CH04-b: see the exact source-scope and landing table above. |
| F005 | `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped read in CH04-b: C-TSC and CY-D; component naming and path ownership. Prior read credits retained. | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.3.4; CY-A Chapter 3-b: C-READ component name, operation logging and consumer/caller relationships; CY-A/CY-F interfaces. Chapter 3-c: component ownership/names and Group A/D boundary; accepted A2 supplies behavior. Chapter 3-d: names, Group A ownership and per-reading seam versus full CY-G boundary.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.9.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1.1, C-ENGINE-AB.1.3, C-ENGINE-AB.2.1, C-ENGINE-AB.2.4, C-ENGINE-AB.4, C-ENGINE-AB.6, C-ENGINE-AB.6.1.; CH03-k: C-INDEX, C-INDEX.2, C-INDEX.3, C-INDEX.5, C-INDEX.6, C-INDEX.6.1, C-INDEX.6.2, C-INDEX.6.3, C-INDEX.6.4, C-INDEX.6.5, C-INDEX.6.6.; CH03-l: C-GOLD, C-GOLD.4, C-GOLD.4.6, C-GOLD.6, C-GOLD.6.2, C-GOLD.7, C-GOLD.7.1, C-GOLD.7.2, C-GOLD.7.3, C-GOLD.7.4.; CH03-o: C-INGEST, C-INGEST.4.4, C-INGEST.4.7, C-INGEST.5, C-INGEST.5.1, C-INGEST.5.2, C-INGEST.5.3, C-INGEST.5.4, C-INGEST.6.; CH03-p: C-DETECT, C-DETECT.1, C-DETECT.1.1, C-DETECT.1.2, C-DETECT.1.3, C-DETECT.2, C-DETECT.2.1, C-DETECT.2.2, C-DETECT.2.3, C-DETECT.2.4, C-DETECT.2.5, C-DETECT.3, C-DETECT.3.1, C-DETECT.3.3, C-DETECT.3.4, C-DETECT.3.6, C-DETECT.4, C-DETECT.4.1, C-DETECT.4.1.1, C-DETECT.4.1.2, C-DETECT.4.2.; CH04-a: C-7E, C-7E.3, C-7E.4, C-7E.5, C-7E.5.2, C-7E.6.1, C-7E.6.4, C-7E.7, C-7E.8, C-7E.11, C-7E.13, C-7E.13.1, C-7E.13.2, C-7E.13.3, C-7E.13.4, C-7E.13.5, C-7E.13.6, C-7E.13.7. CH04-b: see the exact source-scope and landing table above.  CH04-c: scoped read; exact scope and placement in the current source table.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained. |
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
| F035 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md` | Scoped reread for CH04-a; prior whole-read credit retained where previously recorded | C-7B.7 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker. |
| F036 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md` | Scoped reread for CH03-j; prior whole-read credit retained where previously recorded | C-READ.10 and all A2-cited descendants: §§1–10 identity, card/preparation/event ownership, acceptance/correspondence, commit/recovery, legacy mapping, lifecycle, semantic/safety boundaries, references/rereading and logging. EXCLUDED: source revision history, acts of acceptance, implementation workflow and self-audit claims under §1.3. Other consumer mechanics remain with their owning groups.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards.; CH03-j: C-ENGINE-C, C-ENGINE-C.3.3, C-ENGINE-C.4, C-ENGINE-C.5, C-ENGINE-C.6, C-ENGINE-C.9, C-ENGINE-C.11.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F037 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_PACKAGE_COMPLETE_RECORD_v1_0.md` | Read whole for CH03-j | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker. |
| F038 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F039 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F040 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F041 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F042 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F043 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F044 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F045 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F046 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F047 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F048 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for C-STORE.4; receipt narrative excluded under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker. |
| F049 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | Scoped read in CH04-b: §13 TSC caller boundary. Prior read credits retained. | Chapter 3-a: C-STORE.4 and all descendants. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: §10 cross-batch reading reread for boundary check; no new B11 behavior written here, Chapter 3-a placement retained.; CH04-a: C-7E, C-7E.1.2, C-7E.5.6, C-7E.6.3, C-7E.6.4, C-7E.12. CH04-b: see the exact source-scope and landing table above. |
| F050 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole read in CH04-b: Acceptance/status evidence only. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F051 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md` | Whole read in CH04-b: Structural store, exact tables, constraints, transactions, recovery, archive, logging and open implementation choices. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F052 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH03-n | Status/identity checked for NHD-B16EEB; globally unique slot identifiers retained; acceptance narrative EXCLUDED by §1.3; CH03-l: Status/provenance only; no behavior from this receipt or historical blocker.; CH03-m: C-GOLD.1.8.1.5.1.; CH03-n: C-GOLD.1.10, C-GOLD.1.11, C-GOLD.1.11.1, C-GOLD.1.11.2, C-GOLD.1.11.3, C-GOLD.1.11.4, C-GOLD.1.11.5, C-GOLD.1.11.6, C-GOLD.1.11.7, C-GOLD.1.11.8, C-GOLD.1.11.9, C-GOLD.1.11.10, C-GOLD.1.11.11, C-GOLD.1.11.12, C-GOLD.1.11.13, C-GOLD.1.11.14, C-GOLD.1.11.15, C-GOLD.1.11.16, C-GOLD.1.11.17, C-GOLD.1.12, C-GOLD.1.12.1, C-GOLD.1.12.2, C-GOLD.1.12.3, C-GOLD.1.12.4, C-GOLD.1.12.5. |
| F053 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | §§2–6 establish exact accepted standalone scope and source identity. EXCLUDED from behavior: receipt history/roles/process; no mechanism sourced from receipt. |
| F054 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | C-READ.11 and every descendant: complete §§1–11 seam; §13 traces checked against the same rules. §12 external ownership and unspecified details recorded separately. EXCLUDED under §1.3: source status/history/process, self-audit and delivery narrative (§§14–15). |
| F055 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F056 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F057 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md` | Scoped reread for CH03-m; prior whole-read credit retained where previously recorded | C-READ.7.2 and its reciprocal C-READ.7 link: ACCEPTED guard from §1.2 (NHD-B24), matching FR-0608 CARRIED. Remaining B24 behavior NOT PLACED: belongs to later owning templates; no other B24 mechanism added here. Chapter 3-c C-READ.10.3.8.8 and source-conflict register: structural-disposition difference retained against A2; no new retry policy.; CH03-m: C-GOLD.1.8.1.5.2, C-GOLD.1.8.1.5.2.1, C-GOLD.1.8.1.5.2.2, C-GOLD.1.8.1.5.2.3, C-GOLD.1.8.4.3.1, C-GOLD.1.8.4.5, C-GOLD.1.8.4.8.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F058 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_PACKAGE_COMPLETE_RECORD_v1_0.md` | Newly read whole for this correction, all 132 lines; pinned Git blob verified | §§2–3, 5 and 12 establish the accepted standalone status and exact v7 identity used for C-READ.7.2; no behavior sourced from this receipt. EXCLUDED: closure history/process under §1.3; no implementation or integration claimed.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F059 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-e: exact read scope and placement in the current source table; prior credits retained. |
| F060 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F061 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-b: exact read scope and placement in the current source table; prior credits retained. |
| F062 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained. |
| F063 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained. |
| F064 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1 and cited sub-parts; C-7B.7.4.7 and cited sub-parts; C-7B.7.5.3 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained. |
| F065 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F066 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F067 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3.  CH05-b: exact read scope and placement in the current source table; prior credits retained. |
| F068 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1.6 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.  CH05-b: exact read scope and placement in the current source table; prior credits retained. |
| F069 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F070 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_CANDIDATE_v1_4.md` | Carried through Chapter 3-a: Not yet read; whole file newly read in Chapter 3-b | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-b: EXCLUDED: status/consolidation and workflow narrative under §1.3. Used for locating later accepted owners only; it supplies no behavior in this piece.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F071 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F072 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F073 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F074 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F075 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F076 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F077 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F078 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F079 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | Scoped read in CH04-b: §5 paths 3–4; authority owner/limit cross-check. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F080 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F081 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-d: exact read scope and placement in the current source table; prior credits retained. |
| F082 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-d: exact read scope and placement in the current source table; prior credits retained. |
| F083 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for Bundle 6 mechanics; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained. |
| F084 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped read in CH04-b: §3 held/sealed restrictions and privacy precedence. Prior read credits retained. | Chapter 3-a: C-STORE.5 / operation protections, B17, B20, B21; other component scopes NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: C-7E, C-7E.2, C-7E.8, C-7E.9.1, C-7E.11, C-7E.12. CH04-b: see the exact source-scope and landing table above.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained. |
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
| V10-H031 | ## 7F. CONTEXT RETRIEVAL  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1.9 retrieval audit and genuine no-context audit; retrieval machinery remains with C-7F. |
| V10-H032 | ## 7G. MEANING ENGINE INTERIOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ acceptance/shape distinction and caller relationship; C-READ.3 new-root write handoff also cites the nested §7G-A subsection.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  CH05-a: C-7G and explicit shared/deferred owners.  CH05-b: C-7GA and explicit shared/deferred owners. |
| V10-H033 | ### §7G CREATION-AWARE MODE  [SETTLED CONCEPT — NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-d: C-14 and explicit shared/deferred owners.  CH05-a: C-7G and explicit shared/deferred owners. |
| V10-H034 | ## 7H. REREAD LIFECYCLE  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ reread output relationship; detailed orchestration remains with C-7H. |
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
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: §7G-A in full, all 387 lines including record shapes, mode cases, worker substeps, sentinels and RC-1–RC-8; authoritative status table for exact BUILT targets. | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped: Complete C-7GA, C-STORE, C-READ, C-ENGINE-AB, C-ENGINE-C and C-13 paragraphs. | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md` | Scoped: §§1–11 in full; §§12–14 not credited. Current placement is worker-consumed scope and interfaces; complete generic machinery deferred to CH05-d. | `78c5d0b74d91e9390d9ebdf4d1c6ae04dd2632ad86c8efa83f01cfbd9974e606` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: Standalone acceptance, identity and scope evidence only. | `2f9fa7df2d190bf6defae31e8e8a10f78df71a0ef8cb22fc8150f413f7e3c30e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md` | Scoped: §§3,4,7,13 in full; current technical/substantive admission consumption and accepted-value status, full generic records CH05-d. | `e8f4c3debe65d258519f07a71b221802297596e2f9ef86148d2ad1a5800b0814` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: Current standalone design acceptance and identity evidence, not integration or runtime permission. | `d401d8c59695962d4b85608fc0ab88105474c6333af7581cf5189f8e0670bda8` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md` | Whole: Complete coordination note; current worker boundaries use §2, full generic ownership/protection placement CH05-d, project workflow excluded. | `95491b9b621a814a8ac96fb5dba2cb4a9dc6b53ab519111a1aa067c1bbb1ef8c` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: Standalone acceptance and identity evidence; no independent architecture inferred from the receipt. | `6defb8d417f8da26d86d48918ac6098c07abadd6826f2ec35ac2d00d1931efef` |

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

### READ-folder files not yet read whole

81 inherited pending files remain. Scoped reads do not remove whole-file obligations; previous read credits and source placements remain.

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
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md`
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
§1.3 no history/actions/roles/workflow in this chapter: PASS — 175 behavior cards reviewed; 0 project/workflow hits. Source-status and scope notes are outside the behavior cards.
§1.4 every gap written as NOT DECIDED: PASS — 457 empty fields/cells exactly match the register; 14 additional implementation slots are explicit.
§1.5 conflicts marked, none resolved: PASS — 5 explicit conflict-register rows. Five source conflicts remain explicit: fixed-file activation versus the immutable-batch/future-writable route; claimed_at versus locked_at in job_claimed; all-other-root counting versus preceding-root eligibility; the Map's any-stage failed-pass generalization versus V10's completed instruction before post-reading failure; and terminal failed queue jobs versus the later accepted same-identity careful fresh attempt. V10's detailed rules govern without inventing integration. Accepted-design status is distinguished from runtime authority.
§3 exactly one stamp per line: PASS — 175 headers, 1286 populated fields and 317 USED BY rows checked; 3 BUILT field lines. Relationship stamps follow the named card.
§4 every behavior line cited in the exact format: PASS — 38 distinct current citations resolve at the pin; all populated fields and relationship rows are cited. Claims were reviewed against the mapped source sections.
§5.4 one name per thing: PASS — 175 current IDs checked for duplicates, prior collisions and exact official names; shared atoms retain their previous names.
§6 all template fields present, in order, for every part: PASS — 175 templates and 1743 field lines checked.
§6.3 reciprocity within this chapter: PASS — 290 internal lines cover 290 reciprocal pairs; 31 external-use continuations and 8 incoming continuations name both endpoints.
§6.4 every decided detail written in, no citation used in place of content: PASS — The full V10 post-root section is placed: continuous LMAC connection and purpose-specific gates; quarantine/production limits; activation metadata and reconciliation; asynchronous single-worker queue; all five queue record types and their fields; job states, stage variants and per-profile fields/outcomes; exact atomic enqueue and both lock roles; all claim metadata and acquisition/renewal/validation/release/takeover rules; instruction and assignment-input fields; lifecycle states, failure object and exact stage causes; stable reading idempotency and schema mapping; every override/default mode case and permanent prohibition; all primary worker steps and checkpoint substeps; no-clash/no-update sentinels and fields; handled-failure exclusion and RC-1 through RC-8. Accepted B9 admission consumption includes exact technical bounds/gaps, later-episode ordinal-1 pending states and shared substantive admission. Complete generic B9/B10 records and later clash/view/retrieval mechanisms have named owners.
§6.5 sub-parts recursed to the bottom: PASS — 174 declared child/shared references and 175 owned cards checked; 78 explicit steps have 0 empty TOGETHER cases. Records recurse to fields; status enums and stage variants recurse to their states and effects; profile outcomes have distinct atoms; mode assignment has all five override cases and seven default cases; enqueue and claim operations have their individual steps; worker stages and checkpoint substeps remain separate; recovery cases preserve their conditions and written results. Shared reading contracts and sentinel fields retain one identity.
§9 coverage matrix rows added for every file used: PASS — 8 current source identities, 145 READ-folder inventory rows and 107 V10 heading rows checked; 145 named source paths exist at the pin. Earlier credits and placements remain cumulative.
§10.11 no recommendation, no sentence addressed to Ness: PASS — the behavior was reviewed as system operation and boundaries; 0 formula phrases and 0 project/workflow hits.
Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`.

Computed self-check output:

| Check | Count |
|---|---|
| cards | 175 |
| field_lines | 1743 |
| populated_fields | 1286 |
| not_decided_boxes | 457 |
| not_decided_fields_and_cells | 457 |
| used_by_rows | 317 |
| relationships | 322 |
| internal_relationships | 290 |
| external_relationships | 32 |
| internal_use_pairs | 290 |
| external_use_pairs | 32 |
| used_by_continuation_rows | 31 |
| incoming_continuation_rows | 8 |
| plain_gates | 1 |
| step_cards_with_empty_together | 0 |
| explicit_step_cards_checked | 78 |
| unique_citations | 38 |
| resolved_citations | 38 |
| named_source_paths_checked | 145 |
| source_identities | 8 |
| whole_read_files | 4 |
| earlier_identities | 25 |
| pending_source_paths | 81 |
| built_field_lines | 3 |
| misfiled_scan_fields | 1743 |
| misfiled_scan_used_by_cells | 951 |
| empty_restriction_failure_gate_boxes | 202 |
| formula_hits | 0 |
| wording_hits | 2 |
| wording_verbatim_exceptions | 2 |
| wording_actionable_hits | 0 |
| project_workflow_hits | 0 |
| path_use_rows | 8 |
| path_covered_cards | 175 |
| subpart_references_checked | 174 |
| v10_heading_rows_checked | 107 |
| read_folder_files_covered | 145 |
| source_names_checked | 93 |
| errors | 0 |
| additional_undecided_slots | 14 |
| explicit_source_conflict_records | 5 |

All card fields, USED BY cells and empty restriction/failure/gate boxes were reviewed against the full mapped source section and accepted consumption boundaries. Explicit actions and transitions link their actual rules, and gates state conditions rather than repeating outputs. Fixed discriminators and version values carry direct prohibitions; record fields without a specified independent failure mechanism remain empty rather than gaining invented recovery. The three BUILT field lines target only the V10-verified root store, quarantine store and append_reading writer. All six P-MAIN placements and both cycle uses have separate rows. The final count table is recounted after this block is appended.

Two source-verbatim wording exceptions remain in inherited coverage: the A29 closure filename has a space before its extension (line 4961), and V10 heading 15 contains the literal dot-prefixed cursorrules name (line 5084). No actionable wording flags remain.

All 25 earlier completed fingerprints were rechecked and are listed in full. The final count table is compared against a recount after this block is appended. No earlier chapter, repository source or runtime code is changed.
