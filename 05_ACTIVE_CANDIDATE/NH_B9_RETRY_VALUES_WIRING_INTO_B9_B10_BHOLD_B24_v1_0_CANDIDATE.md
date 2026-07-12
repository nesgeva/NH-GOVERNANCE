# NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_0_CANDIDATE.md

## 0. STATUS BLOCK

**Status:** CANDIDATE — unaudited; awaiting ChatGPT's independent audit of
this actual file and Ness's explicit acceptance afterward. **Governed
values-wiring package only:** it maps Ness's decided retry values onto the
accepted B9 retry-state mechanics and their accepted B10/B-HOLD/B24 seams
**without rewriting, patching, replacing, or modifying any accepted
source.** Not accepted, not adopted, not authoritative, not integrated,
not implemented, not `PACKAGE_COMPLETE`. **Until this candidate is
independently audited and explicitly accepted by Ness, the accepted
defaults continue to govern: no declared budget exists, so B9's R1
admission continues to fail closed (B9 §8 row 14), and a substantively
rejected proposal remains terminal under the settled rule.** Nothing
runtime is unblocked, built, integrated, or implemented by this file.

**Date:** July 12, 2026.

**Package ID:** B9 retry-values wiring into B9, B10, B-HOLD, and B24 —
the "B9 values" gap recorded **DECIDED by Ness** in the accepted Bundle 1
normalization record §6, mapped here onto the accepted mechanics
(Bundle 1; the value-level policy gap attached to accepted B9).

**Intended repository placement:** `05_ACTIVE_CANDIDATE/`
(the physical move into the repository is Ness's action).

## 1. GOVERNING AUTHORITY ORDER

1. `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`
   (adopted by Ness June 29, 2026; governing)
2. `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`
3. `01_AUTHORITATIVE/cursorrules`
4. `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`

The current Design and Wiring Map is subordinate to these files.

## 2. SOURCES READ — IDENTITIES RECALCULATED BEFORE WRITING

All read from the governance repository snapshot at branch `main`, commit
`db13036a8d786f2384a02cb7aef0eefe00c412f6`, byte-verified July 12, 2026:

- **Accepted B9:** `NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md`
  — SHA-256
  `78c5d0b74d91e9390d9ebdf4d1c6ae04dd2632ad86c8efa83f01cfbd9974e606`;
  351 lines; 25,308 bytes — **recalculated; matched exactly; read in
  full** (§3 classes, §4 identities and declared inputs, §5 R0–R4, §6,
  §7 seams, §8 rows 1–19, §9, §10, §12). Its closure receipt
  (`2f9fa7df2d190bf6defae31e8e8a10f78df71a0ef8cb22fc8150f413f7e3c30e`)
  — read.
- **Accepted B10:** `NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md`
  — SHA-256
  `215b74841321656a8b7fb1cbf4b9ac9b43259315864cd9f85f5ce86b43d10001`;
  329 lines; 23,681 bytes — **recalculated; matched exactly; read in
  full.** Its closure receipt
  (`da62a1e8216924f9e9f3182f925e7a1e5063355418a7302eb58f86eee54adeea`)
  — read.
- **Accepted B-HOLD:** `NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md`
  — SHA-256
  `406ab00f640eaae013902782e9ec6ca652ea680c10b0f68699d56391a9e1efce`;
  317 lines; 21,649 bytes — **recalculated; matched exactly; read in
  full.** Its closure receipt
  (`4774720eab9ce276e09a3dde20abf59f71e562a462ad7b4fbe2462dccf14e6c9`)
  — read.
- **Accepted B24:** `NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md`
  — SHA-256
  `7f5762e5bc3d7d0fa554ad41426d2cc2f14fb7753a79b67fbd675f6c6b8a2171`;
  1,938 lines; 137,507 bytes — **recalculated; matched exactly**; read
  targeted in the sections this wiring touches: §2.8/§2.10 (the
  insufficiency assessment and its B9-authorized fallback point),
  §3.3/§3.3B/§3.4 (settled rejection categories; boundary-reason
  separation), §5.3 (reject / retry slot / deterministic fallback), and
  §5.4 (the permanently distinct outcomes). Its closure record
  (`83d79db9f5edcad85d603f7cfe93ea3afeeebec6a60f6f4aa64db632b7e5d7e0`)
  — read.
- **Coordination note** (accepted):
  `NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md` —
  SHA-256
  `95491b9b621a814a8ac96fb5dba2cb4a9dc6b53ab519111a1aa067c1bbb1ef8c`
  (the `04_` and `05_` copies are byte-identical) — **read in full.**
  Its closure record
  (`6defb8d417f8da26d86d48918ac6098c07abadd6826f2ec35ac2d00d1931efef`)
  — read.
- **Bundle 1 normalization record v1_1** (accepted for its recording
  scope):
  `NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_CANDIDATE_v1_1.md`
  — SHA-256
  `6828b9bd88cf867d20bfee31b67d13e97e0c573316b43d2298e4764785abeec3` —
  **§6 (the B9 normalized decision record) read verbatim and preserved
  in §3 below.** Its acceptance record
  (`d759d99d6d01cfe0371c5f4261912f2a4e11cabc10ec3fd8cc249bd5d522d7f7`)
  — read.
- **Accepted A29** (where B-HOLD consumes it):
  `NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md` — SHA-256
  `31d5a12455d1532effe7df2216223942da1a555f38910929ff4b6761d0015d65` —
  the automatic track/check/release rule and the A29/B-HOLD ownership
  split, consumed unchanged for the §12 seam.
- **Master V10** (SHA-256
  `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c`),
  **Defaults v2_2**
  (`6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696`),
  **cursorrules**
  (`5050d08825b93acd72a79d07946e43c8cbe537e079517ccfe66bcae8e30e96e9`),
  **Companion**
  (`cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb`)
  — present, consulted, governing. **Map v1_6**
  (`33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865`)
  and the **eight-bundle plan**
  (`2d6483d133bb3992ba079db43e7d663e8016cf8bf693f7b4c9c98005bcb88415`)
  — read, subordinate.

## 3. NESS-APPROVED VALUES — PRESERVED EXACTLY

**Ness-approved decision, recorded in the accepted Bundle 1
normalization record v1_1 §6 and carried identically by the governing
task instruction; preserved verbatim:**

> - N.H uses both a time limit and an attempt limit; whichever is reached
>   first stops the retry.
> - Technical failures get up to 3 total attempts: original try + 2
>   retries.
> - Bad/unsafe/unsupported answer drafts must be recorded as rejected/bad
>   attempts with the rejection reason, then get 1 careful retry.
> - Extra retries after the normal limit are allowed only if something
>   real changed, such as new memory, new instruction from Ness, better
>   context, fixed missing evidence, repaired tool/file/search problem, or
>   a solved blocker.
> - Live chat technical retry gaps: 10 seconds, then 30 seconds.
> - Background/nightly technical retry gaps: 1 minute, then 3 minutes.
> - Bad/unsafe answer draft retry happens carefully right away after
>   recording the rejected draft and reason.
> - N.H may stop early if retrying is clearly useless or unsafe.
> - If retries are used up and N.H still cannot finish safely, it must
>   stop, say why, keep the work record, and save the unfinished state so
>   it can continue later only if something real changes.
> - No fake success, no hidden failure, no endless retry, no turning a
>   rejected draft into the final answer.

The governing task instruction carries the same decision with the
real-change categories enumerated as: **new memory, a new instruction
from Ness, better context, fixed missing evidence, a repaired
tool/file/search problem, or a solved blocker** — the same six
categories named in the recorded decision. **No retry count, delay, or
wall-clock number beyond these explicit values exists anywhere in this
package, and none is invented.**

## 4. THE RETRY-BUDGET CONFIGURATION RECORD — VERSIONED, DECLARED

**The record:** `b9_retry_budget_config` [proposed] — the declared,
versioned configuration record that accepted B9's existing
`retry_budget_ref` (and, for the substantive rule, `retry_policy_ref`)
references at R1. Append-only and versioned: a change is a **new
version record**, never an edit; every admission binds the exact
version it used; no silent change is possible.

**Record shape [all field names proposed — value carriage only]:**

| Field | Content |
|---|---|
| `config_id` / `config_version` / `schema_version` | The record's identity and version |
| `technical_max_total_attempts` | `3` — total attempts including the original (§5) |
| `technical_gap_schedule.live_chat` | `[10 seconds, 30 seconds]` — gap before attempt 2, gap before attempt 3 |
| `technical_gap_schedule.background_nightly` | `[1 minute, 3 minutes]` — gap before attempt 2, gap before attempt 3 |
| `substantive_careful_retry_limit` | `1` — exactly one careful retry per rejected draft/proposal episode |
| `substantive_retry_timing` | `immediate_after_durable_rejection_record` — no gap; the durable record is the prerequisite (§7) |
| `early_stop_permitted` | `true` — recorded early stop per §8 |
| `continuation_rule` | `real_change_record_required` — per §10 |
| `real_change_categories` | Exactly the six §3 categories, as the closed enumeration §10 consumes |

**How these values provide the accepted dual bound (mechanical
explanation, required):** the retry is bounded by **both** an attempt
limit and a time limit, and whichever is reached first stops it —
realized as two independent admission gates that must **both** permit
(§7). The **attempt gate** is the count bound: durable attempt records
< `technical_max_total_attempts`. The **time gate** is the schedule
bound: each admissible retry has exactly one durable not-before anchor
derived from the previous attempt's recorded outcome plus the scheduled
gap for its recorded class (§6) — admission before the anchor is
refused, and the schedule is **finite**: it contains exactly the two
gaps Ness declared, one per admissible retry, so no anchor exists beyond
the last permitted attempt and the schedule can never extend attempts
past the count. The episode's total span is therefore bounded by the
finite declared gaps plus the attempts' own executions; a stop by either
gate ends admission for the episode. **The execution duration of a
source operation is bounded by that operation's own existing timeout
rules, which remain with their existing owner — this package neither
sets nor changes any source-operation execution timeout.**

## 5. ATTEMPT-COUNT SEMANTICS — THE ORIGINAL COUNTS AS ATTEMPT 1

- **The original attempt is attempt 1.** It is the source seam's own
  first execution — never a B9 admission. When its durable outcome
  classifies `technical_retryable`, B9's group records it by reference
  (R0 group establishment / R3-pattern recording), and it occupies
  attempt number 1 in the count.
- **B9-admitted technical retries are attempts 2 and 3** — at most 2
  retries, exactly as decided. `attempt_id = {retry_group_id, attempt
  number}` per accepted B9, unchanged.
- **Counting is derived from durable records only:** the attempt gate
  counts committed attempt entries and the recorded original outcome,
  lookup-first — never an in-memory counter, never a guess.
- **At most one live attempt per group** — accepted B9 R1, consumed
  unchanged; no value in this package weakens it.
- **The classes are bounded separately, exactly as decided:** the one
  careful substantive retry is a single admitted attempt in its own
  bounded substantive sequence (limit 1); it neither consumes nor
  extends the technical schedule, and technical attempts never consume
  the careful-retry allowance.

## 6. SCHEDULE IDENTIFICATION AND DURABLE CLOCK ANCHORS

- **`schedule_class`** [proposed] ∈ {`live_chat`,
  `background_nightly`} — recorded on each durable attempt-outcome
  record **at the moment the outcome is durably recorded**, taken from
  the source operation's own recorded execution context (the live-chat
  front door versus background/nightly processing, per the seam/cycle
  that ran it). B9 consumes the recorded class; it never guesses one. A
  missing or unreadable class → **no admission; fail closed; no default
  class** (§15).
- **Durable clock anchor:**
  `next_admission_not_before = outcome_record.committed_at +
  technical_gap_schedule[recorded class][next attempt number − 1]`
  [proposed] — computed at admission time from durable records only.
  Recovery recomputes the identical anchor from the same records; no
  in-memory timer exists to lose; **no anchor exists without a durable
  outcome record.**
- **How the 10 s / 30 s and 1 min / 3 min schedules are stored and
  consumed:** stored once, declaratively, inside the versioned §4
  configuration record; consumed by reference at each R1 admission,
  which binds the exact config version and the exact anchor evidence it
  used. Gap 1 (10 s live / 1 min background) governs admission of
  attempt 2; gap 2 (30 s live / 3 min background) governs admission of
  attempt 3. Nothing else consumes them.
- **Class recorded per anchor:** if successive outcomes of one group are
  recorded in different execution contexts, the gap consumed for the
  next admission is the one for the class recorded **on the most recent
  durable outcome — the anchor's own record.** No averaging, no third
  schedule, no invented value.

## 7. ADMISSION — BOTH GATES MUST PERMIT (WIRING ONTO B9 R0/R1)

**Technical retry admission** (class `technical_retryable`) — R1 commits
an attempt entry only when **all** of the following hold, each consumed
from accepted B9 or supplied by these values:

1. The group's latest classified outcome is `technical_retryable`
   (accepted §3 routing — held, privacy-refused, indeterminate, terminal
   classes refuse per accepted R0, unchanged).
2. **No live attempt exists for the group** (accepted R1, unchanged).
3. No live hold exists on the source or its inputs (§12; accepted
   B9/B-HOLD, unchanged).
4. **Attempt gate:** durable attempt count <
   `technical_max_total_attempts` (= 3, original included).
5. **Time gate:** now ≥ the §6 durable anchor for this admission.
6. The bound `retry_budget_ref` resolves to an existing, readable §4
   config version (accepted row 14 fail-closed, now with declared
   content).
7. The episode is neither exhausted nor early-stopped (§8–§9) — or a
   **new** episode is opened under an unconsumed real-change record
   (§10).

**Substantive careful-retry admission** (class `terminal_substantive`,
the bad/unsafe/unsupported draft or proposal rejection) — accepted B9
requires a recorded, adopted policy reference **plus** a per-case
authorization reference; this wiring **realizes — never modifies — that
slot**:

- `retry_policy_ref` → this package's decided rule content (once
  accepted): exactly **1** careful retry per rejected-draft episode.
- `retry_authorization_ref` → **the durable B24 rejection record of this
  exact case** (its identity bound at admission): the recorded rejected
  draft/proposal together with its exact distinct rejection reason
  (§13). **No durable rejection record → no admission** — the record is
  the prerequisite, exactly as decided ("recorded first").
- **Timing — immediate:** the careful retry is admissible at the first
  admission evaluation after the rejection record durably exists; no
  scheduled gap applies. "Immediate" is measured from durable readiness,
  never from a wall-clock promise, and never before the record exists.
- **Careful — mechanically carried:** the admitted careful attempt
  mandatorily references the rejection record as input context, so the
  re-attempt is made in full view of the recorded defect. How the
  producing pass uses it is the seam's own SMART work, unchanged.
- **Exactly one:** a second substantive admission for the same episode
  is refused — terminal substantive stands (§13), reopenable only per
  §10.

## 8. EARLY STOP — RECORDED, TERMINAL FOR THE EPISODE

N.H may stop early when retrying is clearly useless or unsafe: recorded
as a group disposition event [proposed: `retry_early_stopped`] carrying
the recorded cause class (`clearly_useless` / `unsafe`) and its evidence
references, followed by the accepted R4 parent terminal for the
requesting operation. An early stop **ends admission for the episode**;
it is never recorded as success, never hidden, and never disguised as
exhaustion — the disposition names the real cause. Because the episode's
own durable finding is that retrying is clearly useless or unsafe,
continuing without anything real changing would contradict that recorded
finding: **continuation after an early stop uses the same §10 gate as
exhaustion — a new bounded episode under a real recorded change.** No
new policy is created by this; it is the mechanical consequence of the
recorded cause.

## 9. EXHAUSTION — STOP, SAY WHY, KEEP THE RECORD, SAVE THE STATE

**Exhaustion** = the episode can admit no further attempt: the attempt
gate is reached, the finite schedule is consumed, the one careful retry
was rejected again, or an early stop was recorded — with no committed
success.

- **Recorded:** the group disposition event [proposed:
  `retry_episode_exhausted`] names which gate stopped it and references
  the attempts' durable outcomes; accepted B9's refusal/fail-closed
  recording (row 14 pattern: the exhausted reference is named) applies
  unchanged.
- **Says why:** the R4 parent terminal and the disposition carry the
  recorded why; surfacing to Ness follows the existing output and §7Q
  gates — no new surface is invented, and nothing is silent (no hidden
  failure).
- **Keeps the work record; saves the unfinished state:** the source
  seam's own durable state **is** the preserved unfinished state —
  accepted B9's settled facts stand: the failed job stays `in_progress`
  with its recorded pass failure; terminal jobs are never re-selected;
  nothing is deleted or rewritten (true destruction remains prohibited).
  This wiring adds only that the exhaustion disposition **references**
  that preserved seam state, so a later continuation finds everything
  lookup-first.
- **No fake success, no hidden failure, no endless retry, and a rejected
  draft never becomes the final answer** — carried as absolute here and
  in §13.

## 10. THE REAL-CHANGE RECORD AND NEW BOUNDED EPISODES

**The record:** `b9_real_change_record` [proposed] — the durable record
without which no continuation after exhaustion or early stop exists.

| Field [proposed] | Content |
|---|---|
| `change_record_id` | Stable identity |
| `change_category` | Exactly one of the closed six: `new_memory` / `new_ness_instruction` / `better_context` / `fixed_missing_evidence` / `repaired_tool_file_search` / `solved_blocker` — any other value is malformed |
| `change_evidence_refs` | References to the real change's own durable records (the new memory's identity, the recorded Ness instruction, the repaired tool's recovery record, …) — references only, never copies, never re-scored |
| `target_group_ref` | The exhausted/early-stopped retry group this record may reopen |
| `recorded_at` / `schema_version` | Timestamp; schema version |
| `consumed_by_episode_ref` | Empty at creation; bound once at consumption (below) |

- **Single consumption — reuse prevented mechanically:** one real-change
  record authorizes **at most one** new bounded episode for its target
  group. Consumption is bound in the new episode's first R1 admission by
  one compare-and-commit on `consumed_by_episode_ref`; exactly one
  winner; a consumed record can never authorize again; a reuse attempt
  is **refused and logged.** Every further continuation requires its own
  **new, unconsumed** real-change record — which is what prevents a
  single change from becoming endless authorization.
- **A new bounded episode, never an extension:** the new episode carries
  `episode_number`, `predecessor_episode_ref`, and
  `authorizing_change_ref` [proposed], and receives a **fresh bounded
  budget under the same §4 values** — the exhausted episode's records
  stand untouched and are never reopened, recounted, or extended. The
  bound is preserved because every episode is itself bounded and every
  episode after the first requires its own consumed change record.
- **Boundaries preserved:** a real-change record is admission
  authorization only. It is never evidence (no re-scoring, no double
  evidence — repetition and change records add no certainty to any
  outcome); it is **not** a bypass of the other accepted classes — a
  live hold still refuses (§12), `privacy_refused` still requires the
  gate's own recorded changed-authorization state (accepted B9 §3,
  unchanged; that record belongs to the gate, not to this record type),
  and `indeterminate` still resolves only through the seam's own
  recovery.

## 11. SEAM — B10 (RETRY IS NEVER A REREAD)

Consumed exactly as accepted B9 §7, B10 §3, and the coordination note
state — no value in this package changes it:

- A B9 retry re-attempts the **same incomplete canonical operation**
  under the seam's own identity to complete its one outcome. **It never
  creates a reread trigger, a reread claim, or a reading layer** — and
  mechanically cannot: the seam's canonical identity admits at most the
  one committed result.
- **A completed reading — including the honest `insufficient_context`
  fallback — can be examined again only through B10**, under a recorded
  §7H trigger. B9 refuses a "retry" request naming a completed reading
  and says so in its refusal record without creating a trigger.
- §7H's scheduled-automatic-retry trigger class remains served by B9's
  technical retry **only while the original operation is open and
  incomplete**; these values give that service its bounds and nothing
  more.

## 12. SEAM — B-HOLD (NO RETRY AROUND A HOLD; RELEASE MANUFACTURES NOTHING)

- **A live hold refuses admission:** class `dependency_blocked_held`
  (accepted B9 §3/R0; accepted B-HOLD §6/§9 row 17) — the retry request
  while held is **refused and recorded** (`retry_refused`), never
  silently queued around the hold.
- **The refusal is free of side effects on both sides:** it consumes
  **no** attempt count, starts **no** gap anchor, opens **no** episode,
  and touches **no** hold record — so hold time never silently expands,
  resets, or consumes a hidden retry budget, and the retry budget is
  never silently drained by a hold.
- **Release alone manufactures nothing:** B-HOLD's release is its own
  evidence-verified interface under accepted A29's automatic
  track/check/release rule — consumed, untouched. After release, no
  success exists that did not commit, and **no automatic retry fires
  from the release event itself**: any later admission is a fresh R0/R1
  evaluation under the group's recorded state — attempt counts stand,
  anchors stand, exhaustion and early stops stand, and a real-change
  record is still required where §10 requires one.

## 13. SEAM — B24 (RECORD FIRST; ONE CAREFUL RETRY; DISTINCTIONS PRESERVED)

- **Durable record first:** the bad/unsafe/unsupported draft or proposal
  and its **exact distinct rejection reason** — B24's settled categories
  (`fabrication_invention`; `malformed_output`; `incomplete_output`;
  `unsupported_certainty`; `positional_semantic_confusion`;
  `reading_mode_violation`; `evidence_self_contradiction`), populated
  only on `rejected` — are durably recorded through B24's own records
  **before** the one careful retry can be admitted; the admission binds
  that record as its per-case authorization (§7). **The rejected draft
  never becomes the answer** — no path promotes it, exactly as accepted.
- **If the careful retry passes B24:** normal processing continues
  through the seam unchanged — B9 records the outcome; nothing else
  happens under B9's name.
- **If it is rejected again:** the episode is **terminal substantive** —
  it stays terminal unless a later real recorded change authorizes a new
  bounded episode (§10). Nothing else reopens it; B-HOLD is never a way
  to park it (coordination note §2.3, consumed).
- **`insufficient_context` only through the governed path:** it may be
  produced **only** through B24's governed insufficiency-assessment path
  (§2.10) on an externally adjudicated, committed
  `genuine_insufficiency_confirmed` — never otherwise. **Technical retry
  exhaustion, provider failure, malformed validation configuration, or
  an unsafe/rejected draft is never relabeled `insufficient_context`**:
  technical stays `technical_failure`; privacy/relevance stays
  `authorization_failed`; an invalid validator configuration stays
  `indeterminate_unvalidated` with its `validation_boundary_reasons`; a
  proposal defect stays `rejected`. Rejection count is never proof of
  insufficiency (accepted B24, consumed).
- **The authorized fallback point [proposed — filling exactly the slot
  accepted B24 §2.10/§5.3 defers to B9]:** B24's governed insufficiency
  assessment and deterministic fallback may run **only when the bounded
  episode can admit no further attempt under these values** — both-gate
  stop, the careful retry consumed or rejected again, a recorded early
  stop, or a class B9 never retries — and only through B24's own
  unchanged mechanics and invocation conditions. Reaching the fallback
  point is a **timing fact, never evidence**: it preserves, and never
  converts between, B24's accepted five-way distinction — **proposal
  rejection / technical failure / authorization failure /
  validation-boundary failure / genuine insufficiency.** No new fallback
  meaning exists or is invented.

## 14. IDENTITY, IDEMPOTENCY, CONCURRENCY, CRASH RECOVERY, PARTIAL COMPLETION

**Consumed unchanged from accepted B9:** `retry_group_id`, `attempt_id`,
`retry_request_op_id`, the retry-state record set, R0–R4, the nine
idempotency points, and all nineteen §8 recovery rows.

**Added by this wiring [all proposed]:**

- **Identities:** the §4 config record identity {`config_id`,
  `config_version`}; the §10 change record identity; the episode
  identity `retry_episode_id = {retry_group_id, episode_number}`,
  derived from the durable disposition chain — never from memory.
- **Idempotency:** each admission binds {config version, anchor
  evidence, episode}; a repeat identical admission finds the committed
  entry (accepted point, now with bound values); change-record
  consumption is one compare-and-commit with exactly one winner; config
  and change records are append-only — repeats converge, edits do not
  exist.
- **Concurrency:** accepted single-winner R1 unchanged; racing
  consumptions of one change record admit exactly one new episode;
  losers observe and append nothing.
- **Crash recovery (lookup-first, on top of accepted rows 1–19):**
  counts, anchors, episode state, and consumption bindings are all
  recomputed from durable records; a crash between the durable rejection
  record and the careful-retry admission leaves the unconsumed rejection
  record findable — the admission may then proceed (row 2 pattern); a
  crash between change-record creation and consumption leaves it
  unconsumed and findable; a crash mid-attempt resolves through the
  seam's own recovery first (accepted row 3), with no admission while
  the attempt is live.
- **Partial completion:** per accepted rows 2–5 and 17 — the seam's
  durable terminal is authoritative; B9's records complete idempotently
  from that evidence; nothing re-runs.

## 15. FAIL-CLOSED MATRIX (VALUES LAYER, ON TOP OF ACCEPTED B9 §9)

| Condition | Behavior |
|---|---|
| §4 config record missing, unreadable, or version-unbound | No admission; no default; fail-closed event naming the reference (accepted row 14, unchanged) |
| `schedule_class` missing or unreadable on the anchor record | No admission; fail closed; **no default class** |
| Anchor evidence missing (no durable outcome record) | No admission; no anchor exists to satisfy |
| Attempt gate reached / schedule consumed | Exhaustion disposition (§9); further requests refused with recorded status |
| Careful retry requested without a durable rejection record | Refused — the per-case authorization is missing (accepted R1, unchanged) |
| Second substantive admission for one episode | Refused — terminal substantive stands |
| Real-change record missing, already consumed, category-invalid, or evidence-unbound | Refused; no new episode; reuse attempts logged |
| Contradictory episode or consumption evidence | `indeterminate`, surfaced, never guessed (accepted row 16 pattern) |
| Any attempt to bypass R1, a hold, a privacy gate, or the acceptance boundary | Refused + violation log (accepted row 19; B-HOLD row 20; gates unchanged) |

## 16. §0B OPERATIONAL LOGGING (VALUES LAYER)

Accepted B9's §10 log set is consumed unchanged (`retry_requested` /
`retry_absorbed` / `retry_refused`; `retry_attempt_admitted` — now
binding the exact config version and anchor evidence;
`retry_attempt_outcome_recorded`; `retry_group_disposition`;
`retry_terminal`; `recovery_applied` / `recovery_noop` /
`fail_closed_event`). Added canonical state/disposition events
[proposed]: `retry_budget_config_recorded` (each config version);
`real_change_recorded`; `real_change_consumed` (with the consuming
episode bound); `retry_early_stopped`; `retry_episode_exhausted`. One
append-only log per real operation; canonical state records are never
operational logs and never extra evidential votes; **no double
evidence** — a change record, a config record, or any amount of
repetition never makes an outcome more true; §7Q governs access to every
record; no silent internal operation.

## 17. RELEASE CONDITION — DESIGN-LEVEL ONLY

**Until this candidate is independently audited and explicitly accepted
by Ness, the accepted defaults stand unchanged:** R1 fails closed with
no declared budget (accepted row 14), the substantive rule's terminal
stays terminal, and every accepted fail-closed boundary governs. Once
accepted, this package's values are the declared configuration and
adopted-rule content that accepted B9's `retry_budget_ref` /
`retry_policy_ref` slots reference — **at design level only.** Master,
map, Defaults, and cursorrules integration, and every implementation,
remain open and separately authorized; nothing runtime is unblocked,
built, integrated, or implemented by this file.

## 18. MUST REMAIN OPEN (NONE CLOSED OR BIASED HERE)

- **Source-operation execution timeouts** — with their existing owners,
  untouched (§4).
- **B1/B26** retrieval quantities, system-failure stop/retry/degraded
  design — open with their owners.
- **A25, A29, A31, and every other Ness policy** — consumed only where
  accepted; nothing decided, reopened, or biased.
- **The A25/B10 manual-reread compatibility path and B10's mode slot** —
  not this package's; open under its own governed work.
- **B-CYCLE-8, the final Bundle 1 audit, Bundle 1 completion, and
  whole-system wiring** — open (including where each cycle's activation
  actually runs; these values give the bounds and gaps, not the cycle
  wiring).
- **Master V10 / map / Defaults / cursorrules integration** — open;
  later, separately authorized, Ness-accepted work.
- **The sealed 5,521-root batch** — untouched; never reopened, changed,
  or appended to.
- **All coding, migration, runtime, PC, store, marker, production, and
  implementation work** — unauthorized; awaiting Ness's separate
  implementation authorization.
- No other open Register-A/B item is closed or biased by this candidate.

## 19. DESIGN-COMPLETE CONDITION FOR THIS CANDIDATE

This candidate is design-complete **for the B9 retry-values wiring**
when: Ness's values are preserved exactly with their recorded provenance
and no invented number (§3); the versioned budget/configuration record
is defined and consumed by reference (§4) with the dual bound explained
mechanically and source-operation timeouts left with their owner; the
attempt-count semantics fix the original as attempt 1 (§5); schedule
identification and durable clock anchors are defined with the declared
gap storage and consumption (§6); admission requires both gates plus the
accepted rules, and the careful retry realizes B9's policy+authorization
slot with the durable rejection record as the per-case reference (§7);
early stop (§8), exhaustion with unfinished-state preservation and
recorded why (§9), and the single-consumption real-change record opening
a new bounded episode rather than an extension (§10) are all defined;
the B10, B-HOLD, and B24 seams carry every stated requirement, including
the preserved five-way distinction and the authorized fallback point
(§11–§13); identity, idempotency, concurrency, crash recovery, and
partial completion are answered lookup-first (§14); the fail-closed
matrix and §0B set are defined (§15–§16); the release condition stays
design-level behind audit and acceptance (§17); and every §18 item
remains open — subject to ChatGPT's independent audit and Ness's
explicit acceptance.

## 20. CHANGE REPORT AND SELF-AUDIT

**File created:**
`NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_0_CANDIDATE.md` —
the only file created by this task item. **Nothing existing was
modified:** accepted B9, B10, B-HOLD, and B24 and their closure records,
the coordination note, the normalization record and its acceptance
record, accepted A29, accepted A25 and the accepted connection chain,
Master V10, Defaults, `cursorrules`, the Companion, the map, the plan,
and every accepted, closure, active-candidate, and historical file — all
preserved byte-identically; nothing committed, pushed, moved, renamed,
overwritten, or deleted.

**Self-audit:** authority order preserved — PASS. Ness's values
preserved verbatim from the accepted normalization §6 and the governing
instruction; no retry count, delay, or wall-clock number invented beyond
them; source-operation timeouts left with their owner — PASS. Dual bound
explained mechanically from the explicit attempt limits and finite gap
schedules; both gates required — PASS. Original attempt counts as
attempt 1; at most 2 technical retries; counts and anchors from durable
records only — PASS. Careful retry: durable rejection record first;
exactly one; immediate from durable readiness; realizes — never
modifies — B9's policy+authorization slot; a rejected draft never
promoted — PASS. Early stop and exhaustion recorded with real causes;
unfinished state preserved in the seam's own durable records; says why
through existing gates; no fake success, no hidden failure — PASS.
Real-change record: closed six-category enumeration; single consumption
by compare-and-commit; a new bounded episode, never an extension; never
evidence; never a bypass of hold/privacy/indeterminate classes — PASS.
B10 seam: same-operation re-attempt only; no trigger, claim, or layer
created; completed readings only via B10 — PASS. B-HOLD seam: refused
and recorded, never queued around; no count, anchor, or hold record side
effects; release manufactures no success and no automatic retry — PASS.
B24 seam: five-way distinction preserved with accepted vocabulary; no
relabeling into `insufficient_context`; the authorized fallback point is
a timing fact only, through B24's unchanged mechanics — PASS. One live
attempt per group; accepted identities, boundaries, and all nineteen
recovery rows consumed unchanged; additions idempotent and lookup-first —
PASS. Fail-closed with no defaults anywhere a reference or class is
missing — PASS. §0B one-operation/one-log with no double evidence —
PASS. Candidate status; nothing accepted, adopted, integrated,
implemented, or `PACKAGE_COMPLETE`; no closure receipt created; all §18
items open; sealed batch protected — PASS.

---

*End of `NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_0_CANDIDATE.md`
— CANDIDATE, unaudited, awaiting ChatGPT's independent audit and Ness's
explicit acceptance. Accepted B9, B10, B-HOLD, and B24 are not modified;
until acceptance the accepted fail-closed defaults continue to govern and
a substantively rejected proposal remains terminal; nothing is
integrated, implemented, or unblocked at runtime by this file.*
