# NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md

**Status:** DESIGN CANDIDATE — proposal only — NOT ACCEPTED — NOT ADOPTED —
NOT AUTHORITATIVE — NOT INTEGRATED — NOT IMPLEMENTED — NOT
`PACKAGE_COMPLETE`. Requires ChatGPT's independent audit and Ness's explicit
acceptance. Creates no acceptance record, closure record, controlled NHD
identifier, implementation instruction, code, store, or runtime artifact.

**Intended repository location:** `05_ACTIVE_CANDIDATE/` (placement is
Ness's action; nothing here is committed, pushed, moved, or uploaded).

**Date:** September 22, 2026.

**Corrects:** `NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_6_CANDIDATE.md`
(SHA-256 `cb8b07dd67a9a407f21b879aaf93c1c2735b3a436f8a657f68f0a61c0949f85d`,
125,853 bytes, 1,881 lines); v1.5 (`2fbb66a1504a8793e8b0b43e8179458bee081611c8533af7a4138fc3716027f4`). **v1.0** (`793671295feb5e33e329a0114bda24485905e831c32a9ca211c0a78f7aafb87d`),
**v1.1** (`a2f090604019e2cfc50be32c55ab16c2a9d31edea5b0b5bd9a78997918579164`),
**v1.2** (`6c4730286c49e9496bfcc887b9b5992cc37781dbbc14b3c5b0f0ec20c895d512`),
**v1.3** (`5bf79b5c5e18112042c159457b74cc4e1144cb28d98cf68e74661576def0a3d7`),
**v1.4** (`9d4d0d5e6bce58d38bee6463d32629d58ffb989667858872516ec7279e7c8cb3`),
**v1.5**, and **v1.6** are preserved unchanged as historical candidate
provenance. v1.7 applies exactly the two state-machine consistency
corrections in ChatGPT's audit of v1.6 (§22 maps each), retains every
confirmed earlier rule unchanged, and re-runs the required audits. v1.7 is
**self-contained**.

**Scope in one line:** the mechanical evidence contract connecting C-GOLD
gold evaluations, B24's benchmark and severity rules, a separately defined
held-out evaluation source, accepted B9 retry rules, and B16 §5.3 evidence
inputs 3 and 4 — without modifying, restating, or replacing any accepted
package.

**Every new name is marked `[proposed]` at first use** (whole tables are
marked in their headers). No field name, record name, state name,
serialization, storage location, database, file format, transport, lock
mechanism, canonicalization, integrity algorithm, or framework is chosen.

---

## §0 — Plain meaning

B16 is the door between quarantine and production. Two of its nine
required pieces of evidence point at a paper nobody ever drew. This file
draws three separate papers:

1. **Gold evidence** — did this exact model, through its approved engines,
   pass the sealed gold exams? (B16 input 3)
2. **Held-out evidence** — did it pass an unseen exam? (B16 input 4; not yet
   defined, so blank)
3. **B24 system eligibility** — did the whole two-model system pass B24's
   entire driving test? (not a B16 input)

The rules that keep the papers honest:

- **A plan is not a pass.** Listing every required test proves nothing.
  Every required test must actually be taken, completed, graded, and
  passed — and every named measurement must actually be measured. Zero
  exams taken means "incomplete," never "pass."
- **Every real exam counts.** A newer exam never hides an older bad one.
  Inside each exam, every answer has exactly **one current grade** — the
  single, authorized, uncontested latest grade in that answer's grade
  chain. Two competing grades for the same answer make it unusable; the
  newer one does not simply win.
- **Only the right grader can grade.** Sealed gold answers and B24
  meaning-cases are graded by Ness only — proven through the accepted
  identity system, not just a typed name. Mechanical checks are done only by
  the exact checker the approved test names. A model may help, but never
  grades. How Ness's identity must be proven for grading is not yet decided
  (D16) — so, for now, no Ness grade can be recorded at all. Whatever Ness
  chooses, the paper keeps the **receipt** that the proof was used at the
  moment of grading: a spent one-time token is the normal sign of success,
  never a reason to reject the grade, and an ordinary session ending later
  never erases a grade that was valid when it was recorded.
- **Gold exams are always graded by gold rules,** even when they are also
  used inside the B24 driving test. B24's own tolerance can never rescue a
  failed gold exam.
- **Each exam question is answered once.** Crashes before an answer exists
  follow the accepted retry rules (B9); once an answer exists, it is final.
  If the machine cannot tell whether an answer exists, nothing is retried
  until it can.
- **No two clerks can write in the same line of the logbook.** Every
  logbook line, every grade summary, and every result paper has exactly one
  place and one content; two different versions of the same paper make it
  unusable.
- **B24's actual test questions don't exist yet.** B24 says which kinds of
  tests are needed; nobody has written or approved the real questions. That
  is now its own visible item for you.
- **Rules are fixed before the exam; a pass is impossible while any rule is
  missing; B16 accepts only a current matching paper; a promoted reading
  stays promoted.**

---

## §1 — Authority and sources

**Governing authority order (unchanged):**
1. `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` — `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` (adopted by Ness June 29, 2026; governing)
2. `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` — `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696`
3. `01_AUTHORITATIVE/cursorrules` — `5050d08825b93acd72a79d07946e43c8cbe537e079517ccfe66bcae8e30e96e9`
4. `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` — `cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb`

The Design and Wiring Map is subordinate. The decision index is a
navigation map only.

**Complete source list** (repository head `1160fbd`, cloned and hashed;
files in `04_ACCEPTED_STANDALONE_DESIGNS/` unless noted):

| Source | SHA-256 | Read |
|---|---|---|
| **Master V10 §25.4 SACL and §25.6 BAI** (lines 3918–4343) | as above | The accepted identity/security authority for Ness: `recognized_ness` session identity (SACL) and purpose-bound one-time authorization artifacts with the `extended:<purpose_id>` purpose form (BAI) |
| **Master V10 §25.6 BAI consumption, audit, crash, and protected-core rules** (lines 4260–4343) | as above | One-time tokens: created → delivered → consumed before the protected action → permanently unusable; purpose verified on every consume; consumed/expired tokens never reused; BAI state in-memory only, cleared on restart; consumption recorded in the security audit log |
| **B-INT-4** `NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md` (1,173 lines, 81,902 bytes) | `f722ac9599c8c88bb019220764266985aac2fe820068e20f5368dbcc9c229ef8` | §§4.1–4.5 in full (requirement, failure and success paths, the session claim and durable-receipt protocol A0–A4, authoritative record at every crash point); §8 record catalog records 1–2 (`tsc_authorization_claim`, `tsc_authorization_operation`); §9 full-transparency logging; §10 fail-closed requirements. **Consumed by reference; not changed.** |
| B-INT-4 closure record v1_1 | `8fd19489e40f66105eb657fdbceeb320091493da2ff25c917964e11454dedf64` | In full |
| **Bundle 5 closeout** `NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` (853 lines) + closure record | `b20d4ee944d5a575b307d70485e5c074c4b298f43a3082ddd760159aa61d924d` / `d62ec6e4d61495147729241331733f81982792440148f624551fe64d9346fa44` | §6 cross-package authority table; **B-INT-4 entry (lines 274–288): the accepted durable chain claim → flushed `bai_token_consumed` receipt → committed transaction, the flushed receipt being "the authorization commit point and the sole durable post-crash proof that token consumption succeeded"**; searched for any evaluation-judgment row — none |
| **AIC** `NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` + closure record | `b39654a60744982d0e2f16c2bc3cd7a33f6ae47ff55b63b5b1dfffada719d709` / `937b90913bfd2578e5a195e33fb7e3e5f7523cd0a3c58d9124d412d85c1411fe` | §1–§4 — governs **artifact** authority (files, statuses), not person identity; consulted and found not to be the applicable judgment-identity authority |
| **Dual-model handoff** `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md` (206 lines, 8,571 bytes; the project-file copy `NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1__2_.md` is byte-identical — the suffix is an upload artifact) | `024a81aeb2c7104e99ceaa3b881a024e38cf700169e37179ac0fb1f358b0d46e` | §§1–9 in full |
| B9 `NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md` (351 lines, 25,308 bytes) | `78c5d0b74d91e9390d9ebdf4d1c6ae04dd2632ad86c8efa83f01cfbd9974e606` | In full |
| B9 closure record | `2f9fa7df2d190bf6defae31e8e8a10f78df71a0ef8cb22fc8150f413f7e3c30e` | In full |
| B9 values `NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md` (1,192 lines, 72,543 bytes) | `e8f4c3debe65d258519f07a71b221802297596e2f9ef86148d2ad1a5800b0814` | In full |
| B9 values closure record | `d401d8c59695962d4b85608fc0ab88105474c6333af7581cf5189f8e0670bda8` | In full |
| Coordination note `NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md` (86 lines) | `95491b9b621a814a8ac96fb5dba2cb4a9dc6b53ab519111a1aa067c1bbb1ef8c` | In full |
| Coordination note closure record | `6defb8d417f8da26d86d48918ac6098c07abadd6826f2ec35ac2d00d1931efef` | In full |
| B16 v1.0 (593 lines, 44,891 bytes) | `0da231c71c4ea17f1e960de4f5f7a117c6f20df2b63ab597e732f824ccaadfb1` | In full |
| B16 closure record | `3bcbc861ce8cd1956f985265d90cdce1d126849f54d79b7d7fa1fba85991270f` | In full |
| B24 v7 (1,938 lines, 137,507 bytes) | `7f5762e5bc3d7d0fa554ad41426d2cc2f14fb7753a79b67fbd675f6c6b8a2171` | In full, incl. §§3.3–7.4, §7B–§7C, §§11–12 |
| B24 package-complete record | `83d79db9f5edcad85d603f7cfe93ea3afeeebec6a60f6f4aa64db632b7e5d7e0` | In full |
| Master V10 | as above | 42–46, 128–135, 146, 359–362, 372–373, 388–391, 404–500 (§6A), 543, 624–629, 2873–2882 |
| Defaults / cursorrules / Companion | as above | Defaults §3D (85–108); cursorrules §1C (102–182), §3B (276–296), §7 (488–495); Companion gold/held-out passages |
| `02_WORKING_MAP/…_MAP_v1_6_CANDIDATE.md` | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` | C-READ, C-ENGINE-AB, C-GOLD, C-7G, C-16, CY-G, B9, B16, B24, B-CYCLE-6, C2 |
| `03_WORKFLOW/NH_FULL_DESIGN_COMPLETION_WORKFLOW_v1_0.md` | `053d0bb70959a97dbd5584c882874fcf00e01fbaaa79ee8570051170cb241509` | Phases 21–22 |
| `05_ACTIVE_CANDIDATE/…DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | `aafc7abe6522f4c7ece23f40560e648866188e1b5401ed6cd298809d15ed0f7b` | Header; Part A; NHD-B16, NHD-B24, NHD-B9, NHD-B9W, NHD-BU1, NHD-M11-20/26, NHD-A1, NHD-UDOK |
| A29 v1.0 + closure | `31d5a12455d1532effe7df2216223942da1a555f38910929ff4b6761d0015d65` / `7d8ab6a96c16f8c93d50223eab6ca2b8e6c94ea9e25d54b72b519bfebd2ba64c` | §0, §6; closure §7 |
| A31 v1.0 + closure | `65de6d5f42d3aa7b117cddc0d5b8e6c3b0c51bed637ea67e804dd01bf8cf03b5` / `b71426d6132246d6f9de65bf8a8b9fc4d14fcf39b99db92bcf1ba2edd92296a7` | §0–§2, §10 |
| Bundle 1 v1_4 + acceptance + closure | `5ebddb536201e8d39794297088752ba4c2925a1be706ff29c55e1a45b42ea6fa` / `d759d99d6d01cfe0371c5f4261912f2a4e11cabc10ec3fd8cc249bd5d522d7f7` / `c20d023277010173ed3bbb7e333fd725d8327c5eb6d8e18589e8bc14cc30436a` | Composition; lines 366, 444 |
| UDOK closure record | `91c52869fb1616f25a5193a5eeca7e70ba0bf0fa755c8ce5648719efae8f9b11` | UDOK v1.9 status block, §1, B16/B24 refs only — for non-conflict |

---

## §2 — Source and gap audit

### §2.1 B16 (accepted; unchanged)

§5.3 input 3 (lines 234–236): gold-set results evidence reference — "the
recorded B24-architecture acceptance evidence for the applicable gold-set
run". Input 4 (line 237): held-out set results evidence reference. B16
verifies presence, integrity, authorization, binding — never content. §8
row 12: missing/failed evidence fails closed; never fabricated, inferred, or
substituted. §4/§5.1: `promotion_committed` is terminal, absorbing,
idempotent. §12 / closure §9: evidence-record formats and thresholds open.

### §2.2 B24 (accepted; unchanged)

§2.9 per-brief validation result; §6–§7 parent/child architecture, T1–T11,
lookup-first recovery, one terminal per child and parent, one
operation-owned stream per operation; §7B rules 1–8; **eight suite
families** (§7B.2: language fidelity; evidence integrity; structured
output; multilingual status preservation; operation behavior; output-gate
behavior; stability/operational; failure/recovery); **three measurement
scopes with named measurements** (§7B.3 — analyst: depth, evidence
fidelity, channel/scope discipline, lane separation, refusal to fabricate;
messenger: live usability, warmth, translation fidelity incl. Hebrew,
strict bounded obedience, distortion resistance; combined pair/system:
handoff reliability, total latency, memory/GPU behavior, whether the heavy
model must run every turn); §7C severity (any single CRITICAL blocks
eligibility; tolerance, latency, trial count, hardware open).

### §2.3 B9, B9 values, coordination note (accepted; consumed)

B9 governs retry state for N.H operations that fail, time out, crash, are
interrupted, rejected, blocked, or indeterminate (§1); one retry group per
source-operation duplicate-prevention identity (§4); attempts run under the
seam's own canonical identity — "the sole duplicate-execution defense;
unlimited attempts can commit at most the one result" (§5 R2, §6); classes
(§3): `terminal_success` absorbs; `technical_retryable` (including "lost
races") only through R1; `indeterminate` never retried, recovery first;
hidden retry refused (§8 row 19). B9 values v1_4: 3 total technical attempts
per episode; minimum gaps 10 s / 30 s (live chat) or 1 min / 3 min
(background/nightly); elapsed deadline 7 / 15 min; permanent
`attempt_number` + per-episode ordinal; original execution is ordinal 1 by
reference; continuation only via a consumed real-change record with
seam-confirmed unchanged inputs. Coordination note: retry ≠ reread; held
blocks both; terminal stays terminal; one log per real operation.

### §2.4 §2.9 is not benchmark-run evidence

Never read as gold, held-out, or eligibility evidence.

### §2.5 C-GOLD already owns gold-run logging

Map C-GOLD (189); Master 543; C-ENGINE-AB (180). This bridge extends C-GOLD.

### §2.6 Accepted execution paths

Gold v1 → **Engine A** (`nh_engine_minimal.py`, `read_root()`,
`run_on_gold()`, bare). Gold v2-B → **Engine B** (`nh_engine_b.py`,
`read_root_b()`, `_get_preceding_turns(n=3)`, BACKGROUND prompt,
`run_on_gold()`). Both use `MOUTH_MODEL` (unadopted test candidate
`dolphin-llama3`). Benchmark-affecting changes need Ness's authorization and
a re-run of both sets (Master 45–46, 134–135, 372–373, 477, 627–628; Map
C-ENGINE-AB; cursorrules 287–289, 488–495).

### §2.7 Repository search (unchanged conclusion)

No accepted held-out definition; no accepted gold, held-out, or benchmark
result schema. B24's held-out search hits (127, 1555, 1579) were false
positives on "withheld output". Every evaluation/benchmark-result hit in
the accepted folder is a filename or package reference to B16. Bundle 1 v1_4
(366, 444) records benchmark tuning as outside its closure.

### §2.8 Classification and safety state

Unfinished mechanical bridge work inside a dependency B16 left open — not a
retroactive invalidation. The built B16 treats inputs 3/4 as always-missing
(per the 2026-09-22 build handoff; not re-verified here): fail-closed,
safe, not promotion-ready.

### §2.9 The concrete B24 benchmark-suite gap (added v1.3)

B24 defines **suite families and measurement requirements**, not concrete
versioned benchmark cases or prompts, scoring bindings, or suite
identities. No accepted source anywhere in the repository supplies them.
The D9 role mapping decides **who** is tested on each family; it is **not**
test content. Therefore **no B24 benchmark E1 may register** until a
concrete suite manifest, its cases, its scoring bindings, its measurement
declarations, its integrity identity, and its acceptance source exist
(§5 E1; §17 D15). Nothing here invents or approves cases. The sealed gold
sets v1 and v2-B exist and are accepted for gold coverage only.

### §2.10 The judgment-authority sources (added v1.4)

- **Who judges** is settled by accepted sources: Ness for sealed gold cases
  (Master line 146 rule 6; Defaults §3D) and for meaning-dependent B24 cases
  (§7B.1 rule 1); models assist and never judge.
- **How Ness's identity is proven** belongs to the accepted identity/security
  authority, **Master V10 §25**: SACL (§25.4) carries session identity
  (`recognized_ness`); BAI (§25.6) issues purpose-bound, one-time
  authorization artifacts, with a declared purpose vocabulary that includes
  the `extended:<purpose_id>` form. Bundle 5's cross-package authority
  table (§6) shows how accepted Ness-owned acts bind those mechanisms
  (e.g. TSC authorization: "BAI (token truth) + SACL (recognized-Ness) +
  Ness's action"; voice enrollment: "Ness's explicit begin + BAI token").
- **No accepted source defines which §25 artifact, or combination, is
  required to record an evaluation judgment.** Bundle 5's table has no such
  row. AIC governs artifact authority, not person identity. This bridge
  therefore binds every Ness judgment to a §25 artifact **by reference**,
  invents no authentication method, and leaves the required proof as a
  visible open decision (§17 D16). **Until D16 is accepted, no Ness
  judgment can be recorded** (fail closed).

---

## §3 — Ownership boundary

| Owner | Owns | Does not own |
|---|---|---|
| **C-GOLD** | Sealed gold sets; gold examination; gold-run logging; per-case judgments under the six settled rules | Held-out; eligibility policy; promotion |
| **B24 v7** | Benchmark rules, families, named measurements, severity, eligibility rule | Concrete suites (D15); result records; every policy value |
| **B9 + values** | Every technical re-attempt: admission, identity, budget, gaps, deadline, exhaustion, continuation, recovery — including lost commit races | Planned trial counts; evaluation meaning |
| **This bridge** | Record family, scopes, ledgers, currentness, concurrency rules, identities, operations, terminals, derivation, the applicability contract | Any judgment, policy value, suite content, held-out definition, mapping, or promotion decision |
| **B16 v1.0** | Per-reading verification in B16-2; every promotion outcome; absorbing `promotion_committed` | Evaluation content and criteria |
| **B-CYCLE-6 / C2** | Connected promotion flow and batch wiring / marker-gate implementation | — |
| **Held-out set; concrete B24 suites** | No accepted owner or content; none assigned | — |

**Judgment ownership (enforced mechanically, §7.11):** each E1 case's
accepted scoring binding names its judgment mode. Sealed gold meaning
judgments: **Ness only**, under the six settled gold rules. B24
meaning-dependent cases: **Ness only** (§7B.1 rule 1). Mechanically
decidable findings: **only** the deterministic checker configuration the
accepted E1 binding declares. Model assistance: reference only, **no
authority**. Held-out: **unset** until an accepted held-out policy defines
it. An annotator name alone never establishes authority.

---

## §4 — Identity model

### §4.1 Candidate profiles

- **`model_evaluation_profile`** `[proposed]` (E4): one model identity plus
  explicit **execution-path bindings** `[proposed]`, each binding one suite
  version to one approved path (engine identity + version + code integrity,
  prompt, context/retrieval configuration, validator configuration or
  `not_in_path`, other benchmark-protected configuration), each with its
  own `path_configuration_digest` `[proposed]`. Gold v1 → Engine A and gold
  v2-B → Engine B need not share an engine identity.
- **`system_candidate_profile`** `[proposed]` (E4S): the analyst component
  (its E4), the messenger component (its E4), and the combined pair/system
  handoff configuration (brief schema version, B24 validator configuration,
  payload and messenger contracts, gate configuration references, the
  dual-model handoff arrangement of the accepted handoff package §§1–4),
  with its own `system_configuration_digest` `[proposed]`.

### §4.2 Policy epoch

A **policy epoch** `[proposed]` (E2e) binds the exact versions of every
pass-bearing policy a family depends on (§16): trial count,
tolerance/acceptance rule **for every suite kind the scope's cells use**
(so a B24 epoch whose coverage includes sealed-gold cells also binds the
D2 gold aggregate rule), required-coverage profile (incl. the B24 role
mapping), measured-dimension budgets where applicable, the accepted D16
judgment-authority requirement where Ness judgments are needed, and, for
held-out, the held-out policy. Current only while every named record is the current
accepted version. Invoked-only policies (invalidity rule, disagreement
policy) are cited in the records that invoke them. Accepted B9 values are
not epoch members; B9 admissions bind their own budget-config versions.

### §4.3 Run class and the complete epoch freeze (retained; confirmed)

Evidentiary `[proposed]` or exploratory `[proposed]`, fixed at open.
Evidentiary runs open only when the family's complete epoch is current
(including trial count), plus an accepted suite manifest and a registered
profile; the epoch is frozen into the run. **No evidentiary run can open
or execute while `trial_count_policy_ref` is unset.** Exploratory runs are
permanently `non_evidentiary`. The complete-epoch freeze is retained as
confirmed by the v1.1 audit.

### §4.4 Evaluation scope; one target family per run

Scope `[proposed]` = `{target family, candidate profile digest (E4 or E4S),
role/system, policy epoch}`. Families: `gold_evidence`,
`held_out_evidence`, `b24_system_eligibility` `[all proposed]`. One run,
one scope, one family.

### §4.5 Planned trials versus retry attempts

A **planned trial** `[proposed]` is `{run, case_id, trial_index}`; planned
trials are the measurement units (§7B.1 rule 4). A retry attempt is a
B9-governed re-execution of the same planned trial after a technical
failure; it never creates or replaces a planned trial or a completed
output. Each planned trial is one B9 source operation with canonical
identity `planned_trial_key` `[proposed]` and one B9 retry group. **The
run's trial plan must equal the suite's complete case list × the epoch's
trial count** — a subset plan is refused at E5.

### §4.6 Coverage cells and named measurements (added v1.3)

- A **coverage cell** `[proposed]` is the exact tuple `{concrete suite
  manifest + version, §7B.2 family (or `sealed_gold_rule_8` for gold
  cells), §7B.3 measurement scope, execution binding}`. For gold-family
  scopes the cell is `{gold suite + version, path binding}`.
- **Named measurements** `[proposed]` — fourteen, from §7B.3, labelled:
  analyst M-A1 depth, M-A2 evidence fidelity, M-A3 channel/scope
  discipline, M-A4 lane separation, M-A5 refusal to fabricate; messenger
  M-M1 live usability, M-M2 warmth, M-M3 translation fidelity incl.
  Hebrew, M-M4 strict bounded obedience, M-M5 distortion resistance;
  combined M-C1 handoff reliability, M-C2 total latency, M-C3 memory/GPU
  behavior, M-C4 whether the heavy model must run every turn.
- A **required-coverage profile** (E3) lists every required cell. **A cell
  is satisfied only by at least one complete, current, passed evidentiary
  run whose E5 matches the cell exactly** and whose trial plan is the full
  suite × trial count. **A measurement is satisfied only when at least one
  satisfied cell whose suite declares that measurement has recorded that
  measurement's results** in its current aggregate head — and, where §7C
  gives it a budget (latency M-C2; memory/GPU M-C3), those results are
  within the epoch's budget. M-C4 has no §7C budget: it must be measured and
  recorded, and its result is reported in E12, not pass/fail.
- **Naming a cell or a measurement in E3 satisfies nothing.** Missing runs
  or missing measurements yield `incomplete`, never `eligible`.

---

## §5 — Record family [all names proposed]

All records append-only and immutable; corrections are new linked records;
each carries integrity reference, `schema_version`, creating operation
identity; no gold-case, root, or reading text is copied.

| Code | Record | Purpose |
|---|---|---|
| E1 | `evaluation_suite_manifest` | Frozen suite version: kind (`sealed_gold` / `held_out` / `benchmark_family`), name, version, integrity, seal reference, ordered case identities + integrity, governing scoring-rules reference, `acceptance_source_ref`, §7Q classification. **Every case carries a scoring binding** `[proposed]`: its **judgment mode** — `ness_meaning_judgment` / `deterministic_checker` (with the exact checker configuration identity + version) — and its **governing scoring-rule reference**. The §7C category mapping is part of the binding **only for `benchmark_family` cases**. **`sealed_gold`: every case is `ness_meaning_judgment` under the six settled gold rules, aggregated by the accepted D2 gold rule; no §7C category exists on a gold case, and no §7C label may ever change or supplement gold scoring.** **`held_out`: cases use only their future accepted held-out policy; none exists.** **For `benchmark_family`: the §7B.2 family, the named measurements it declares, per-case scoring bindings including each finding's §7C category, and an acceptance source recording Ness's approval of that concrete suite (D15). None exists; no benchmark E1 can register.** Held-out → must cite an accepted held-out policy that also defines judgment authority |
| E2 | `benchmark_policy_reference` | Pointer to a Ness-approved policy record; missing or unaccepted → unset. No policy record created here |
| E2e | `policy_epoch` | §4.2 |
| E3 | `required_coverage_profile` | The required cells (§4.6) per family and role/system; for B24 the role mapping of cells to scopes; required policy kinds. **Registration refused if any §7B.2 family has no cell, any §7B.3 scope has no cell, any of the fourteen named measurements is declared by no required cell's suite, or gold v1 and gold v2-B are not each in a cell through their bound paths.** Content otherwise a Ness decision (D8a, D8b, D9); no instance exists |
| E4 / E4S | profiles | §4.1 |
| E5 | `evaluation_run_open` | Before any trial: run ID, class, scope, profile ref, **the exact coverage cell it serves**, **the E1 suite kind and its governing scoring-rule reference** (§8.1), frozen epoch ref, recorded execution context (§7.6), runtime/hardware configuration, comparability group, full trial plan, operator, `opened_at`. Refused if the plan is not the suite's full case list × trial count |
| E6 | `trial_attempt_start` | `{run, case_id, trial_index, attempt_id, planned_trial_output_key}`; ordinal 1 has no B9 admission; **every later attempt carries its committed B9 R1 admission reference** |
| E7 | `trial_attempt_terminal` | Exactly one per attempt: `attempt_completed` / `attempt_failed` (`technical` / `resource` / `timeout`) / `attempt_interrupted_abandoned` / `attempt_unresolved`. Deterministic findings recorded here bind the exact checker configuration the E1 binding declares; any other checker → finding invalid → run head `indeterminate` |
| E7r | `trial_attempt_resolution` | For an `attempt_unresolved` only: `resolved_output_found` / `resolved_absence_proven` / `still_undetermined` (§7.10) |
| E8 | `evaluation_run_terminal` | Exactly one per run: `run_completed` / `run_closed_incomplete` / `run_indeterminate`, with the frozen terminal-set digest |
| E9 | `evaluation_judgment` | One link in the judgment chain of one effectively completed output (§7.11): `judgment_chain_key` (= that output's `planned_trial_output_key`), **`expected_previous_judgment_head`** (or `none` for the first), output ref + integrity, judgment mode (must equal the E1 case binding), **`judgment_authority_ref`** — for Ness judgments, the **event-time proof** required by the accepted D16 option (§7.12): the durable **token-consumption receipt** (BAI option), and/or an **immutable event-time session-state reference** (SACL option) — never the reusable presence of a token, never a bare name; for deterministic judgments, the declared checker configuration + its execution record, `pass` / `fail`, §7C classification, `human_annotation` provenance (annotator/when/context_version), `change_reason` (required when superseding), optional `model_assist_ref` (no authority). Identity = `{judgment_chain_key, expected_previous_judgment_head, content digest}` |
| E10 | `suite_aggregate_result` | Per run, chained by `expected_previous_head` (§7.9 CAS-2): terminal-set digest, E7r digest, **the set of current judgment heads it consumed** (one per meaning-dependent effectively completed output) and their digest, the suite kind and scoring rule applied, findings, **recorded named-measurement results**, coverage, state |
| E11a / E11b | `gold_evidence_result` / `held_out_evidence_result` | Narrow results for B16 inputs 3 / 4; deterministic identity (§7.9 DET-1) |
| E12 | `b24_system_eligibility_result` | System-level B24 eligibility; deterministic identity; **not a B16 input** |
| E13 | `promotion_evaluation_evidence_ref` | Pointer B16 verifies: `{evidence_kind, result_ref (E11a/E11b only) + integrity, scope, bound ledger head}`; never → E12 |
| E14 | `evaluation_invalidity_record` | Excludes a run only under an accepted objective invalidity rule with recorded objective facts |
| E15 | `evaluation_conflict_resolution` | Resolves conflicting completed judged runs only under an accepted disagreement policy; binds every affected run |
| E16 | `evaluation_scope_ledger_entry` | §6; compare-and-append only, committed through O-APPEND (§7.9 CAS-1) |

---

## §6 — Currentness: the scope ledger

### §6.1 The ledger

Each scope has one append-only **scope ledger** of E16 entries
`{scope, sequence_number, record_ref, record_integrity,
previous_entry_digest}`. **Every relevant canonical record commits in the
same boundary as its E16 entry, through one O-APPEND operation, and that
boundary is a compare-and-append against the exact previous head (§7.9
CAS-1)** plus the record's own domain precondition (e.g. the judgment head
for an E9, the aggregate head for an E10, "no attempt after E8" for an
E6). Relevant records: every E5,
E6, E7, E7r, E8, E9, E10 of every evidentiary run in the scope, and every
E14/E15 naming such a run. Results (E11a, E11b, E12, E13) never append.
Exploratory runs append nothing. The **ledger head** is `{latest
sequence_number, latest entry digest}`.

### §6.2 The authoritative current result

Every E11a/E11b/E12 binds the scope's ledger head at derivation and the
digest of the exact relevant-record set it evaluated. It is the
**authoritative current result** only while its bound head equals the
current head and its epoch is current. Any later relevant record advances
the head and makes earlier results **not current for new checks**. Nothing
is edited. An E13 whose result is not current is unusable for a new check.

### §6.3 Prior-scope disclosure (retained; confirmed)

Every result carries a mandatory, mechanically computed disclosure of every
other scope sharing its family, model identity (or component identities),
and role/system, with each scope's epoch, head, and state. **Confirmed by
the v1.2 audit:** prior scopes are disclosed but do **not** automatically
block a genuinely different profile or epoch.

### §6.4 B16 absorbing terminal

`promotion_committed` is absorbing and never retroactively undone; evidence
changes affect only new checks. Changing that is a versioned B16
reconsideration, outside this bridge.

---

## §7 — Operations, lifecycle, logs, terminals, retries, concurrency

### §7.1 Canonical records versus operational logs

Canonical records (E1–E16) are state records, never §0B logs, never extra
votes. **Every real operation emits exactly one append-only §0B log, once,
at its terminal, before any acknowledgement.** B9's retry-request
operations keep their own logs; nothing is duplicated.

### §7.2 Operations `[all proposed]`

| Operation | Canonical records | Exactly one terminal |
|---|---|---|
| O-SUITE | E1 | `registered` / `refused` |
| O-SETUP (each E2e / E3 / E4 / E4S) | one of those | `registered` / `refused` |
| **O-RUN** (parent) | E5 …, E8 (+E16) | `run_completed` / `run_closed_incomplete` / `run_indeterminate` |
| **O-ATTEMPT** (child; the seam operation B9 launches for ordinal ≥ 2) | E6, E7 (+E16) | `attempt_completed` / `attempt_failed` / `attempt_interrupted_abandoned` / `attempt_unresolved` |
| O-RESOLVE-ATTEMPT | E7r (+E16) | `resolution_committed` (with outcome) / `refused` |
| **O-JUDGE** (protected parent protocol: claim → [BAI consumption + receipt] → E9+E16 via O-APPEND) | `judgment_authorization_claim` states (child canonical records); E9 (+E16) via O-APPEND | `judgment_committed` / `judgment_absorbed` / `judgment_refused_stale_head` / `judgment_refused_authority` / `judgment_refused_mode_mismatch` / `judgment_refused_output_invalid` / **`judgment_claim_lost`** (losing concurrent claim; consumed nothing) / **`judgment_authorization_failed`** (pre-receipt crash; failed or unverifiable receipt write; refusal before consumption after a claim; **head breach after a durable receipt**) — one terminal per O-JUDGE, ever. The claim's closure (`released` for no-receipt cases; `closed_after_breach` for the breach case) is a **consequence** of this terminal, never its cause (§7.13) |
| O-AGGREGATE | E10 (+E16) | `aggregate_committed` / `aggregate_absorbed` / `aggregate_refused_stale_head` |
| O-RESULT (each E11a / E11b / E12) | one result | `result_committed` / `result_absorbed` / `result_contradiction` |
| O-EVREF | E13 | `issued` / `refused` |
| O-INVALIDITY / O-CONFLICT | E14 / E15 (+E16) | `committed` / `refused` |
| O-RECOVERY | missing items only | `recovery_applied` / `recovery_noop` |
| **O-APPEND** (commits exactly one requested scope-relevant record + its E16) | the requested record + E16 | `appended` / `absorbed` (identical record already committed) / **`lost_race_technical`** (ledger head moved; B9 `technical_retryable`) / **`refused_domain_precondition`** (e.g. stale judgment or aggregate head, attempt after E8, authority failure — **non-retryable**) |
| B9 retry request (B9's own) | B9 records | B9 R4 terminal |

**Terminal rules.** Every attempt ends in exactly one E7; every run in
exactly one E8. E8 commits only when every started attempt has an E7 and no
B9 attempt for the run's planned trials is admitted-unstarted or live; **no
attempt may start after E8.** `run_completed` = every planned trial has
exactly one effectively completed attempt at close; `run_closed_incomplete`
= deliberately closed short of that; `run_indeterminate` = any unresolved
attempt without conclusive resolution, integrity failure, or contradiction
at close. Acknowledgement only after the terminal record and its log;
missing logs are appended by recovery before acknowledgement. **Every
scope-relevant record is committed by an O-APPEND;** the requesting domain
operation (O-RUN, O-ATTEMPT, O-JUDGE, …) reaches its terminal only once its
terminal record's O-APPEND has ended `appended` or `absorbed`. **No
operation ID ever receives two terminals or two logs** — including every
O-APPEND, each of which has its own ID, one terminal, and one log.

### §7.3 Frozen terminal set

At E8 the run's terminal set (every E6/E7 across every B9 episode) is
frozen and digested. E10 computes from exactly this set plus E7r records.
E8 and every E7 are never rewritten.

### §7.4 One output per planned trial; output-before-visibility (retained; confirmed)

`planned_trial_output_key` `[proposed]` is deterministic from
`planned_trial_key`, shared by every attempt, and becomes the reading's
`idempotency_key` — B9's canonical identity: at most one committed output
per planned trial. `attempt_completed` = B9 `terminal_success`; retries
absorb. A judged `fail` is the measurement, never re-attempted; B9's
substantive careful-retry path does not apply to evaluation outputs; any
internal retry inside the evaluated path is part of the configuration under
test. **Output-before-visibility** — no output is shown to any operator or
judge before its E7 `attempt_completed` (or E7r `resolved_output_found`)
commits — is retained as **confirmed by the v1.2 audit**.

### §7.5 Technical re-attempts under accepted B9

Ordinal 1 is the original execution by reference. B9 classes (B9 §3):
`attempt_completed` → `terminal_success`; `attempt_failed` and
`attempt_interrupted_abandoned` → `technical_retryable`;
`attempt_unresolved` → `indeterminate` (never retried; recovery first);
privacy refusal → `privacy_refused`; live hold → `dependency_blocked_held`.
**Every later attempt requires a committed B9 R1 admission** under B9's
accepted admission, identity, budget, gaps, deadline, one-live-attempt, and
real-change rules. **No B9 authorization → no re-attempt.** An ordinal ≥ 2
E6 without admission is refused as B9's hidden-retry violation (§8 row 19).
Exhaustion leaves the trial uncovered. For the B24 family, recorded
resource failures remain CONSEQUENTIAL findings.

### §7.6 Execution context (retained; confirmed)

E5 records the actual execution context. **Confirmed by the v1.2 audit:**
an evaluation run not executed through the live-chat front door uses B9's
**background/nightly** classification (B9 values §6); a missing or
unreadable context admits no retry.

### §7.7 Transaction boundaries `[all proposed]`

| # | Boundary | Rule |
|---|---|---|
| EB-1 | Suite registration | E1 after integrity, seal, acceptance; benchmark kind additionally needs the D15 acceptance source |
| EB-2 | Setup registration | E3 refused per §5 E3 conditions |
| EB-3 | Run open | E5 + E16 (CAS-1); evidentiary needs a current epoch incl. trial count; full plan; exact cell |
| EB-4 | Attempt start | E6 + E16; ordinal ≥ 2 only with B9 admission; never after E8; never while an attempt of that trial is unresolved |
| EB-5 | Attempt terminal | E7 + E16 |
| EB-6 | Attempt resolution | E7r + E16 (§7.10) |
| EB-7 | Run terminal | E8 + E16 under §7.2 conditions |
| EB-8 | Judgment (protected parent protocol, three linked stages — **not one atomic transaction**) | **Stage 1** — the judgment-authorization claim commits (one winner; §7.13). **Stage 2 (BAI option)** — BAI re-validates the attached token and consumes it; the flushed `bai_token_consumed` receipt is the **authorization commit point**; claim → `consumed_pending_commit`. **Stage 3** — E9 + E16 commit **atomically through O-APPEND** under CAS-1 and **CAS-3** (expected judgment head still current); O-APPEND re-verifies the bound receipt (or, SACL option, verifies the session state fresh and valid at this commit and binds its immutable reference); refused unless the judgment mode equals the E1 case binding and the output is effectively completed with matching integrity; claim → `judgment_committed`. A token's post-consumption `consumed` state is the success state, not a refusal. Each stage is separately durable and recoverable (§7.12, §7.13). |
| EB-9 | Aggregate | E10 + E16, CAS-2 against the run's current aggregate head |
| EB-10 | Result derivation | E11a / E11b / E12 under DET-1 |
| EB-11 | Evidence reference | E13 |
| EB-12 | Invalidity / conflict | E14 / E15 + E16 |

### §7.8 Idempotency and duplicate prevention

| Point | Key |
|---|---|
| E1 | name + version + integrity (same name/version, different integrity → contradiction) |
| E2e / E3 / E4 / E4S | content digest |
| Run | run ID; identical repeat absorbs; different content refused |
| Planned trial | `planned_trial_key`; one B9 group |
| Output | `planned_trial_output_key`; one committed output ever |
| Attempt start / terminal | `{planned_trial_key, attempt_id}` / attempt ID |
| Conclusive resolution | `{attempt_id, conclusive}` — at most one `resolved_output_found` or `resolved_absence_proven` ever |
| Undetermined resolution | `{attempt_id, resolution_sequence}` |
| Run terminal | run ID |
| Judgment | E9 identity `{judgment_chain_key, expected_previous_judgment_head, content digest}`; identical re-submission absorbs; **at most one committed successor per predecessor** (CAS-3) |
| O-APPEND | its own operation ID; the requested record's own idempotency key is the canonical key B9 groups on |
| Ledger entry | `{scope, sequence_number}` — CAS-1 |
| Aggregate | `{run, expected_previous_head, terminal-set digest, E7r digest, judgment-set digest}` — CAS-2 |
| Results | DET-1 identity |
| E13 / E14 / E15 / logs | result + kind / excluded run / affected-run set / operation ID |

### §7.9 Concurrency-safe heads (added v1.3; CAS-1 corrected and CAS-3 added v1.4)

- **CAS-1 — ledger compare-and-append (via O-APPEND).** An O-APPEND commits
  its requested record and E16 entry in one boundary **only if** the
  scope's current head equals its expected previous head `{n, d}` (and the
  record's domain precondition holds); the entry takes sequence `n+1` and
  `previous_entry_digest = d`. **Two entries can never claim the same
  sequence position:** of competing O-APPENDs with the same expected head,
  exactly one wins; the loser's boundary commits nothing.
  - **The losing O-APPEND ends with one durable terminal,
    `lost_race_technical`, and one log.** It is B9 `technical_retryable`
    ("lost races", B9 §3).
  - **B9 may then admit a new attempt.** Per accepted B9 (§4, §5 R2), the
    retry group is keyed on the **source duplicate-prevention identity** —
    here the requested record's own idempotency key — and **each admitted
    attempt launches a new seam parent operation with its own operation
    ID**: a **new O-APPEND**, carrying the **unchanged canonical key,
    unchanged requested record content, and unchanged idempotency
    identity**, against the new head, with its own one terminal and one log.
  - **No operation ID receives two terminals or two logs.** The failed
    O-APPEND is never re-used; the requesting domain operation (e.g.
    O-JUDGE) keeps its own single identity and terminal, reached when one of
    its O-APPENDs ends `appended` or `absorbed`.
  - If B9 does not admit a new attempt, nothing is committed; lookup-first
    recovery may later complete a missing record only from durable evidence
    (B9 §8 row 17 pattern) — never a new effect, never a model
    re-invocation.
  - **A technical lost race is distinct from non-retryable refusals.**
    `refused_domain_precondition` — a stale judgment head (CAS-3), a stale
    aggregate head (CAS-2), an attempt after E8, a missing, unverifiable, or
    mismatched judgment authority, a mode mismatch, an invalid output — is
    **never machine-retried**: it routes through B9's non-retryable classes
    (e.g. `privacy_refused` for a §7Q/SACL refusal; `terminal_substantive`
    for identity conflicts or mismatched authority). A new record after such
    a refusal is a new, deliberate operation with new content — never a B9
    retry of the refused one.
- **CAS-2 — aggregate-head compare-and-replace.** An E10 names the run's
  aggregate head it expects to supersede (or `none` for the first). It
  commits **only if** that is still the current head. A competing aggregate
  with the **identical** key and content **absorbs**; one whose expected
  head is no longer current is **refused** (`aggregate_refused_stale_head`)
  — a fresh O-AGGREGATE may then compute from the new state (new content,
  new operation, not a retry). **Different content under the same key, or
  two committed aggregates superseding the same head (a fork), is an
  integrity contradiction → the run is `indeterminate`; never
  last-writer-wins.**
- **DET-1 — deterministic results.** E11a / E11b / E12 identity =
  deterministic from `{scope, bound ledger head, evaluated-set digest}`.
  Derivation is a pure function of the ledger state at that head, so every
  derivation at the same head yields the same identity and content: a
  second commit **absorbs**. **Different content or state under the same
  identity is an integrity contradiction** (`result_contradiction`): both
  are preserved, neither satisfies B16 or B24, and the scope's results are
  `indeterminate` until reconciled by lookup (AP-2).
- **CAS-3 — judgment-head compare-and-extend.** Each effectively completed
  output has one **judgment chain** keyed by its `planned_trial_output_key`.
  An E9 names the chain's head it expects to extend (or `none` for the
  first). Its O-APPEND commits **only if** that expected head is still the
  chain's current head (and CAS-1 holds). **Identical re-submission
  absorbs; a stale competing successor is refused**
  (`judgment_refused_stale_head`, non-retryable). **Two different committed
  successors of the same predecessor (a fork), or different content under
  the same E9 identity, are an integrity contradiction.**
- **E13** is one per `{result, evidence kind}`.

### §7.10 Unresolved attempts and E7r semantics (added v1.3)

An `attempt_unresolved` E7 is preserved forever. Later resolution is only
append-only E7r, by lookup, with exactly these outcomes:

| E7r outcome | Effective attempt state | B9 routing | Aggregate | Ledger | Run |
|---|---|---|---|---|---|
| `resolved_output_found` — output with verified `planned_trial_output_key` identity and integrity | **completed** (via the E7r; the E7 stays `attempt_unresolved`) | `terminal_success` — any retry absorbs | The trial counts as covered once judged; the run's aggregate head is stale; a new E10 over frozen set + E7r may use it | E7r appends; head advances | Before E8: the run may reach `run_completed`. After E8: E8 stays; the **effective run state** `[proposed]` is derived from E8 + E7r records and may be completed if every unresolved attempt is now found |
| `resolved_absence_proven` | **interrupted/abandoned** | `technical_retryable`; B9 consumes the E7r as that attempt's durable outcome | The trial is uncovered unless another attempt completes | E7r appends; head advances | Before E8: a further attempt only by B9 admission. **After E8: no attempt can start; the trial stays uncovered; effective run state `incomplete`** — permanently, unless an already-accepted rule (an E14 under an accepted objective invalidity rule) permits another path; none exists |
| `still_undetermined` | still unresolved | `indeterminate` — **never retried** | Run head `indeterminate` | E7r appends; head advances | Cannot become completed; before E8 E8 may commit only as `run_indeterminate` |

**Rules:** at most one conclusive E7r per attempt; a later E7r contradicting
a conclusive one → integrity contradiction → `indeterminate`. **No attempt
is started while existence is unknown. No attempt is started after E8.** E7
and E8 are never rewritten; effective states are derived.

### §7.11 Judgment chains and judgment authority (added v1.4)

**One chain, one current head, per effectively completed output.**

- The chain is keyed by the output's `planned_trial_output_key`; it exists
  once the output is effectively completed (E7 `attempt_completed`, or E7r
  `resolved_output_found`).
- The **current judgment head** `[proposed]` is the unique committed E9 in
  that chain with no committed successor — **defined only while the chain
  has no fork and no contradiction**. The first E9 names `none`; every later
  E9 names exactly the current head it extends (CAS-3).
- **A valid correction** is a new authorized E9 whose expected head is the
  single current head, carrying a `change_reason`; the previous judgment is
  preserved byte-identically and simply stops being the head.
- **A fork** (two committed successors of one predecessor) or **a
  contradiction** (different content under one E9 identity, or a record
  whose bytes do not match its identity) makes the chain's **judgment state
  `judgment_indeterminate`** `[proposed]`: that trial, its run's aggregate
  head, and every downstream result are `indeterminate`. **Recency never
  chooses between conflicting judgments.** No further E9 can extend a forked
  chain (it has no single head), and **no fork-resolution procedure is
  defined here** — it stays open and fails closed (§20); it is **not**
  covered by D10 or D11.
- **E10 consumes, for every meaning-dependent effectively completed output
  in the run, exactly its current judgment head**, and records the set it
  consumed. A missing head → `incomplete`; a forked, contradictory,
  unverifiable-authority, or integrity-failed chain → `indeterminate`. No
  other judgment ever contributes to `passed` or `eligible`.

**Judgment authority, enforced at O-JUDGE / EB-8.** Every E9 binds a
`judgment_authority_ref` that must match the E1 case's scoring binding:

| E1 judgment mode | Required authority | Refused when |
|---|---|---|
| `ness_meaning_judgment` — **all sealed gold cases** (six settled rules) and **B24 meaning-dependent cases** (§7B.1 rule 1) | The event-time proof the accepted **D16** option requires (§7.12), issued under the accepted **Master §25** mechanisms (SACL §25.4 session identity and/or a BAI §25.6 purpose-bound one-time artifact), proving Ness performed **this** recorded judgment act: for BAI, the **durable consumption receipt** of a token that was valid, unexpired, unrevoked, unconsumed, purpose-matched, and bound to this judgment (or the D16-approved judging scope) **at consume time**; for SACL, an **immutable reference proving the required recognized-Ness state was fresh and valid when O-JUDGE committed** | Absent; unverifiable; not of the D16-required kind; not Ness; token expired, revoked, purpose-mismatched, or **already consumed before this judgment's own consumption** (replay/reuse); consumption receipt missing, unreadable, mismatched, or contradictory; session state not fresh/valid **at commit time**; **D16 not yet accepted (today: every Ness judgment is refused)**. **A token's `consumed` state resulting from this judgment's own successful consumption is the expected success state and is never a refusal ground** |
| `deterministic_checker` | The exact checker configuration identity + version declared in the accepted E1 binding, plus that check's execution record | Any other checker, version, or configuration; missing execution record |
| held-out cases | **Unset** until an accepted held-out policy defines it (D7) | Always, today |

- **Model assistance** may be referenced (`model_assist_ref`) and carries
  **no judgment authority**: an E9 whose only authority is a model is
  refused (`judgment_refused_authority`).
- **An annotator name alone is never authority.** The `human_annotation`
  provenance fields are recorded **in addition to** the verified reference.
- This bridge **invents no authentication method**; it binds by reference to
  the accepted §25 authority and verifies what that authority issues.

### §7.12 D16 authority-proof lifecycle — conditional mechanics for every option (added v1.5; D16 remains open)

D16 is Ness's choice (§17). This section states, **without selecting**, what
the bridge does under each option. It invents no BAI purpose identifier, no
per-judgment vs per-session scope, and no authentication policy; where D16
names a scope, the bridge follows it.

**The protected judgment protocol (corrected v1.6).** O-JUDGE is the
**protected parent protocol**, not one atomic transaction. Its stages are
**linked and recoverable, never falsely described as one transaction**:
(1) the **judgment-authorization claim** (§7.13) is committed first;
(2) **BAI separately** performs and durably records token consumption —
the **flushed receipt is the authorization commit point**; (3) **E9 + E16
are then committed atomically through O-APPEND** under CAS-1 and CAS-3.
**O-APPEND is responsible only for its actual E9 + E16 atomic commit**;
it neither consumes nor verifies authority for the first time. Nothing
about the proof is "checked in advance and trusted later": the token's
validity is re-checked by BAI immediately before consumption, and O-APPEND
re-verifies the bound receipt (or session reference) before committing
E9. Under the SACL-only option there is no stage 2; the event-time
verification happens at stage 3's commit.

**Option A — D16 selects a one-time BAI artifact (§25.6).** The accepted
pattern is consumed unchanged: **claim → flushed `bai_token_consumed`
receipt → committed transaction**, where the flushed receipt is the
authorization commit point and the sole durable post-crash proof that
consumption succeeded (Bundle 5 B-INT-4; Master §25.6).

1. **Before the judgment:** the token must be `valid`, unexpired, unrevoked,
   **unconsumed**, purpose-matched to the D16-declared judging purpose, and
   bound (by its BAI pending record / challenge) to **this exact judgment
   operation** or to the **D16-approved judging scope** — nothing wider.
   **Both checks are re-run by BAI immediately before consumption** (B-INT-4
   §4.1 pattern), never trusted from an earlier check.
2. **Consumption** happens under accepted BAI rules (purpose verified on
   every consume call; single use; permanently unusable afterward). The
   order is: O-JUDGE commits the **judgment-authorization claim** (§7.13,
   state `claimed`, one winner); attaches the token to the winning claim;
   BAI consumes **only the token attached to the winning claim** and
   commits + flushes the `bai_token_consumed` receipt (**consumption is not
   reported successful until the receipt is durable**); the claim moves to
   `consumed_pending_commit`; then O-APPEND commits E9 (binding the
   receipt) + E16; then the claim moves to `judgment_committed`.
3. **E9 binds the durable consumption receipt** (`bai_token_consumed`
   identity + integrity + the claim it was consumed for) — **never** the
   reusable presence of the original token.
4. **After successful consumption, `consumed` is the expected success
   state.** It never refuses the committed judgment and never later
   invalidates it. Currentness (§6, AP-3) is about ledger heads, not token
   state.
5. **One token, one judgment** — unless D16 explicitly selects a separately
   defined session-scoped mechanism (a §25.6 lease or a D16-defined scoped
   artifact); the bridge does not define one.
6. **Replay / reuse:** a second O-JUDGE presenting a token whose receipt
   already exists, or a token BAI reports consumed/expired/revoked, is
   refused (`judgment_refused_authority`, non-retryable) and logged; BAI's
   own duplicate/delayed rejections apply.
7. **Crash before the durable receipt (incl. after the claim, after
   validation, and during or immediately after an in-memory
   consumption) — corrected v1.6, per B-INT-4 §4.5 and Master §25.6:**
   BAI state is in-memory only; **after restart the original token no
   longer exists** and must never be reconstructed, resurrected, or
   treated as reusable. An absent or unverifiable durable receipt means
   **no authority was ever committed**. Therefore recovery **never**
   proceeds to consumption with the original token; the judgment
   authorization operation (O-JUDGE) reaches the honest non-success
   terminal **`judgment_authorization_failed`** (one terminal, one log,
   §7.2/§13.5); its claim becomes **`released`** through an append-only
   linked record; **a later attempt requires a new authorization flow and
   a new token**, under a new O-JUDGE identity, taking over only through
   an append-only linked supersession of the released claim. Recovery
   records the reason through **its own** stage/recovery records only —
   it **never creates or backfills a BAI-owned event** (e.g.
   `bai_token_consume_blocked`) that BAI did not itself write during a
   live consume; a genuinely pre-existing BAI event may be referenced
   only; missing BAI history is never proof that a consume attempt
   occurred.
7a. **Receipt-write failure inside the same running process (no crash):**
   the same fail-closed rule. **It is terminal for that token, including
   when in-memory consumption may have occurred**: the uncertain token is
   **never retried**; O-JUDGE ends `judgment_authorization_failed`; the
   claim is `released`; a new token and a new O-JUDGE are required; BAI
   state is never reconstructed from bridge records.
8. **Crash after the durable (flushed) receipt but before E9 commits:**
   the receipt is authoritative — **authority was granted and survives the
   restart**. The claim is in `consumed_pending_commit` and is **fenced**
   (§7.13): recovery verifies the receipt (chain, expected head, E9 content
   identity, purpose/scope, token, integrity) and **forward-completes
   exactly the E9 the winning claim names**, once, through O-APPEND —
   **without consuming again, without fabricating a judgment, and without
   losing, duplicating, or redirecting the authorization**. If unrelated
   ledger movement makes the O-APPEND lose its CAS-1 race, a new
   B9-admitted O-APPEND (new ID, unchanged E9 key and content) retries the
   commit; the authorization is not re-established. If the **judgment head
   has already changed contrary to the fence** (an integrity breach), the
   stale E9 is **not forced through**: the contradiction is recorded, the
   chain becomes `judgment_indeterminate`, and the claim ends
   **`closed_after_breach`** (§7.13; linked to the contradiction record) —
   a **receipt-bearing, non-replaceable** closure: no new claim may be
   admitted and no other token may be consumed for that scope, and the
   indeterminate chain cannot be extended, unless a future accepted
   resolution policy expressly permits it (§20). A receipt whose
   claim is absent or does not match it is recorded as an **orphaned
   receipt**: nothing commits, the judgment is unavailable, and no other
   judgment may use it. An unreadable or contradictory receipt →
   indeterminate until lookup resolves it.
9. **Unreadable, mismatched, contradictory, or missing consumption proof**
   at any later time makes that judgment **unavailable** (never committed)
   or, if already committed, **`judgment_indeterminate`** for its chain
   until verified by lookup (CR-28).

**Option B — D16 selects SACL recognized-Ness session proof (§25.4).**

1. **At O-JUDGE commit**, inside the EB-8 boundary, verify that the
   required identity/session state (as D16 names it — e.g. a fresh,
   non-stale `recognized_ness` assessment for the Ness stream, with no
   invalidating condition of the accepted §25 kind: speaker change, stale
   SIA, spoofing suspicion, session end, security event) **was fresh and
   valid at that moment**.
2. **Record an immutable event-time reference** `[proposed]` in E9: the
   SACL/SIA assessment identity, its version, and the commit timestamp it
   was verified against — proving the event-time fact.
3. **Ordinary later expiry, session closure, or the passage of time never
   retroactively erases** a validly recorded judgment; a judgment's validity
   is a fact about its commit moment.
4. **Later discovery** that the original proof was unreadable, mismatched,
   contradictory, or **invalid at judgment time** (e.g. a security event
   recorded as effective before the commit) **fails closed**: the chain is
   `judgment_indeterminate` (CR-28).

**Option C — D16 selects both.** Both sets of requirements apply to the same
judgment, in the same boundary: the token consumed and receipt bound (A)
and the session state verified and referenced (B). Either failing → refused
or indeterminate as above.

**In every option:** a bare annotator name is never proof; model assistance
never adds authority; the required proof kind, scope, and purpose come from
accepted D16, not from this file; and until D16 is accepted every Ness
judgment is refused.

### §7.13 The judgment-authorization claim (added v1.6; mirrors accepted B-INT-4 record 1 by reference)

**Record: `judgment_authorization_claim`** `[proposed]` — the one-winner
serialization slot for one judgment authorization scope. **Coordination
only: it grants no authority, is not a second authorization authority, and
never substitutes for the durable receipt.** It serializes access to BAI's
accepted authority (and, under the SACL option, to the single judgment
commit). Canonical state record, not an operational log.

**Ownership:** this bridge (coordinator role), exactly as B-INT-4 owns
`tsc_authorization_claim`; BAI owns token truth and the receipt; the
judgment chain (§7.11) owns the head; O-APPEND owns the E9 + E16 commit.

| Field `[all proposed]` | Content |
|---|---|
| `judgment_claim_id` | Stable, unique |
| `judgment_chain_key` | The output's `planned_trial_output_key` |
| `expected_previous_judgment_head` | The exact head this judgment intends to extend (`none` for the first) |
| `e9_content_identity` | Digest of the exact E9 content to be committed |
| `d16_purpose_scope_ref` | The D16-declared purpose / scope reference (per-judgment or D16-approved judging scope) — value from D16, not chosen here |
| `judging_operation_id` | The O-JUDGE identity |
| `attached_token_ref` | Where applicable: the BAI token reference attached at attach time (**only this token may be consumed**) |
| `durable_receipt_ref` | From consumption: the flushed `bai_token_consumed` receipt identity + integrity |
| `state` | current-state, append-only transitions: `claimed` → `consumed_pending_commit` → `judgment_committed`; `claimed` → `released` → (optionally) `superseded`; `consumed_pending_commit` → **`closed_after_breach`**. `released` and `superseded` are **no-receipt states only**; `closed_after_breach` is the **only** terminal state of a receipt-bearing claim other than `judgment_committed` |
| `supersedes_claim_ref` / `superseded_by_claim_ref` / `linked_contradiction_ref` | Append-only explicit links for every release, supersession, or breach |
| `created_at`, `terminal_at`, `schema_version` | — |

**Identity and uniqueness.** The **judgment authorization scope** is
`{judgment_chain_key, expected_previous_judgment_head}` (plus the D16
scope reference where D16 defines a wider scope). **At most one
active-or-successful claim per scope** (`claimed`,
`consumed_pending_commit`, `judgment_committed`). Concurrent claim
creation admits **exactly one winner**; a **losing claim consumes
nothing** and its O-JUDGE ends `judgment_claim_lost` (one terminal, one
log). An identical duplicate creation request (same scope, same O-JUDGE,
same content) **absorbs**; any other duplicate is refused.

**Lifecycle rules.**
- `claimed`: written **before any token is touched**; grants nothing.
- **Only the token attached to the winning claim may be consumed.** A
  second token presented for a scope already claimed or committed is never
  consumed: the request returns the existing reference or fails closed.
- `consumed_pending_commit`: entered when a durable receipt bound to this
  claim exists. **Fenced:** while in this state, no other O-JUDGE for the
  same scope may consume a token, win a claim, or commit a competing
  successor; recovery must forward-complete exactly the named E9 (§7.12 A
  item 8).
- `judgment_committed`: entered when the named E9 + E16 have committed
  (O-APPEND `appended`/`absorbed`). The O-JUDGE reaches
  `judgment_committed`.
- `released`: entered **only after** the owning O-JUDGE has reached an
  applicable durable non-success terminal (`judgment_authorization_failed`
  or `judgment_claim_lost`, §7.2) **and** there is **positive proof that
  no valid durable receipt exists** for this claim (no `durable_receipt_ref`
  on the claim, and no verified `bai_token_consumed` receipt bound to this
  claim in the security-audit history). A pending O-JUDGE never has a
  released claim.
- `superseded`: a `released` (no-receipt) claim later replaced by a new
  linked claim (`superseded_by_claim_ref`). It is **never** the state of a
  receipt-bearing claim.
- **`closed_after_breach`** `[proposed]`: a **receipt-bearing** claim
  (`consumed_pending_commit`) closed because a judgment-head integrity
  breach made its named E9 unusable (`linked_contradiction_ref`). The
  receipt is preserved and **never re-applied**; the chain is
  `judgment_indeterminate`; **no replacement claim may be admitted and no
  other token may be consumed for that scope**, unless a future accepted
  resolution policy expressly permits it — none exists (§20).
- **A claim with a durable consumed receipt may never be replaced by
  another claim or by consuming another token for the same judgment
  scope — including after a breach.**
- **Replacement rule (admission of a new claim for a scope):** a new claim
  may be admitted **only** when the prior claim is `released` or
  `superseded` **and** the admitting operation has positive proof that no
  valid durable receipt exists for that prior claim — never while
  `claimed` (a pending owner), `consumed_pending_commit`,
  `judgment_committed`, or `closed_after_breach`.
- **Contradictory claim or receipt evidence** (two winning claims for one
  scope; a receipt naming a claim that does not exist or does not match;
  two receipts for one claim) → the scope and its chain are
  `judgment_indeterminate`; all records preserved.

**Fence versus new judgments (one coherent rule, v1.7).**
- A new deliberate O-JUDGE for a scope may be admitted **only** when the
  scope has no owning claim, or its prior claim is `released` /
  `superseded` **with positive proof that no valid durable receipt exists**
  (the prior O-JUDGE having reached `judgment_authorization_failed` or
  `judgment_claim_lost`). It then needs a new claim, a new token, a new
  O-JUDGE.
- A `claimed` claim whose O-JUDGE is **still pending** (e.g. O-APPEND
  exhaustion under B9 before any consumption, §13.5) **keeps the scope**:
  the one-winner fence holds, a competing O-JUDGE cannot win, and
  continuation is only a new B9 episode and new O-APPEND **under that same
  O-JUDGE**.
- A `consumed_pending_commit` claim **blocks** every other O-JUDGE until
  forward completion (→ `judgment_committed`) or a recorded breach
  (→ `closed_after_breach`, which blocks permanently absent an accepted
  resolution policy).
- **No operation is ever simultaneously pending and durably
  non-successful** (INV-26).

**Recovery (lookup-first):** the claim tells recovery **which single
operation owns the scope**; it never substitutes for the receipt. No
receipt → operation `judgment_authorization_failed`, claim `released`,
no BAI event created. Receipt → forward-complete the named E9 exactly
once, then `judgment_committed`. Receipt without matching claim →
orphaned; nothing commits.

**Logging:** the claim's state transitions are **canonical state records**
(child events of the O-JUDGE), not operational logs; O-JUDGE's single
operational log names the claim and its final state (§13.5). No new
decision slot is added: purpose, scope, and authentication kind remain
D16's.

---

## §8 — Derivation rules

### §8.1 Suite aggregate (E10) states

`passed` / `failed` / `incomplete` / `stale` / `indeterminate` /
`non_evidentiary` `[all proposed]`, computed over **effective** attempt and
run states and, for meaning-dependent outputs, **only their current
judgment heads** (§7.11). **Each E10 applies the scoring rule of its own
run's E1 suite kind** (bound in E5) — never the scope family's:

1. Exploratory → `non_evidentiary`.
2. Unreadable input, integrity failure, fork, contradiction, or any
   effectively unresolved attempt → `indeterminate`.
3. Run not terminal; effective run state `incomplete`; any planned trial
   without an effectively completed attempt; any meaning-dependent completed
   attempt without a current E9; **any declared named measurement not
   recorded** → `incomplete`.
4. Epoch not current, suite/profile/binding superseded, or digested sets
   changed → `stale`.
5. Otherwise the run's own suite-kind rule, from its frozen epoch:
   - **`sealed_gold` runs — always** the six settled gold per-case rules
     (Ness's current authorized judgment heads) **plus the accepted D2 gold
     aggregate rule, including when the run contributes to an E12 scope.**
   - **`benchmark_family` runs** — their accepted E1 case scoring bindings
     and §7C: any CRITICAL → `failed`; CONSEQUENTIAL findings (incl.
     resource failures) against the B24 tolerance; budgeted measurements
     against budgets.
   - **`held_out` runs** — only the future accepted held-out rule; none
     exists.
   - **Placing a sealed-gold cell inside a B24 coverage profile never turns
     it into a benchmark-family suite and never changes how it is graded.**
6. Precedence: `indeterminate` > `failed` > `stale` > `incomplete` >
   `passed`.

### §8.2 Gold evidence result (E11a)

For one gold scope, R = **every** evidentiary run in the scope ledger,
minus only E14-excluded runs; evaluate only each run's current aggregate
head (none or not current → `incomplete`).

- **Zero runs, or any required gold cell with no satisfying run →
  `incomplete`** (no vacuous pass).
- Any run open, effectively incomplete, unjudged (a meaning-dependent
  output without a current authorized judgment head), or with head
  `incomplete`/`stale` → `incomplete`.
- Any head `failed` → `failed` (unless an accepted E15).
- Any head `indeterminate` → `indeterminate`.
- `passed` only when every run in R has a current `passed` head **and**
  every required gold cell is satisfied.

A passed run never hides another run. E11a binds the head, carries the
disclosure, and is never labelled eligibility.

### §8.3 Held-out evidence result (E11b)

Same rule; no held-out E1 can register; no E11b can be produced.

### §8.4 B24 system eligibility (E12) — actual coverage (v1.3; scoring order added v1.4)

For one E4S scope and the current B24 epoch, E12 is `eligible`
`[proposed]` only when **all** hold; otherwise `not_eligible` /
`incomplete` / `stale` / `indeterminate` `[proposed]` with named reasons:

1. **Every run counts:** the §8.2 rule over all runs of the scope.
2. **Every required cell is actually satisfied** (§4.6): for every E3 cell
   `{suite + version, family, scope, binding}`, at least one complete,
   current, passed evidentiary run whose E5 names that exact cell and whose
   plan is the full suite × trial count. Analyst-scope cells bind the E4S
   analyst component exactly; messenger-scope cells the messenger component;
   combined-scope cells the full `system_configuration_digest`.
3. **Every one of the fourteen named measurements is actually satisfied**
   (§4.6): recorded results in a satisfied covering cell's current head;
   budgeted measurements within budget; M-C4 recorded and reported.
4. **Both sealed gold sets** have actual current passed runs through their
   mapped cells and bound paths (§7B.1 rule 8) — **each scored by the gold
   rules (six per-case rules + D2 gold aggregate rule), never by B24
   tolerance** (§8.1 rule 5).
5. Trial count, tolerance, and every §7C budget are set in the epoch and
   met; no CRITICAL anywhere.
6a. **Order of evaluation:** every component run head is first scored by its
   own suite kind's rule (§8.1); **only then** does E12 apply B24's overall
   eligibility rule (items 1–5) over those correctly scored heads. B24's
   overall rule never re-grades a component head.
6. **Zero runs, any unsatisfied cell, or any unsatisfied measurement →
   `incomplete`.** The E3 mapping alone never produces `eligible`.

E12 binds the head, carries the disclosure, reports every measurement
result (including M-C4), and means only §7B.1 rule 7 — never adopted.
E11a/E11b remain the narrow B16 results; E12 is never merged with them.
**Today no benchmark E1 can register (§2.9, D15), so no E12 can be
`eligible`.**

### §8.5 What derivation never does

Invent a value, suite, or case; treat confidence or self-review as
judgment; let a model judge where Ness is assigned; assume gold rules for
held-out; turn gold into eligibility; select a favourable run; count a stale
aggregate; ignore an open run; treat a named cell or measurement as
satisfied without runs; retry a completed or unknown output; resolve a
contradiction by recency; count any judgment other than the current
authorized head; accept a judgment without verified matching authority;
grade a sealed-gold run by anything but the gold rules.

---

## §9 — Applicability to one B16 reading

Inside B16-2, as B16's own verification (row labels `[proposed]`). Given
reading R and pointer E (E13, matching kind), every row must pass:

| # | Check | Fails as |
|---|---|---|
| AP-1 | E exists, verifies, points at E11a (input 3) or E11b (input 4) — never E12 | missing / indeterminate |
| AP-2 | The result exists, verifies, is not excluded, and **no conflicting record exists under its DET-1 identity** | indeterminate / not available |
| AP-3 | **Currentness:** bound ledger head = the scope's current head | not available |
| AP-4 | State `passed` | `failed` → applicable failed; `indeterminate` → indeterminate; other → not available |
| AP-5 | Epoch current | not available |
| AP-6 | R's model identity + digest = the profile's | not applicable |
| AP-7 | R's role/system = the scope's | not applicable |
| AP-8 | R's engine path, prompt, configuration (`produced_by`) match exactly one binding by `path_configuration_digest` | not applicable |
| AP-9 | Every suite the E3 profile requires for readings of that path is satisfied by current passed run heads, each through its own bound path | not available |
| AP-10 | R's `produced_by` complete for every bound field | not applicable |
| AP-11 | Each engine version maps to exactly one code-integrity reference | indeterminate |
| AP-12 | §7Q authorization for E, the result, and its records | unauthorized |

Evidence for a different model, role/system, path, prompt, configuration,
suite, epoch, or head is never accepted; evidence is profile-level, applied
by exact binding; readings keep their `produced_by`; manual inspection and
the promotion decision stay separate per-reading evidence. Result classes
to B16 `[proposed]`: `applicable_passed`, `applicable_failed`,
`not_available`, `not_applicable`, `indeterminate`, `unauthorized`; mapping
into B16 outcomes is B16's, unchanged; no hold is created.

---

## §10 — Invariants

- **INV-1** No `passed`/`eligible` unless the complete epoch was current at
  every contributing run's open and at derivation.
- **INV-2** No evidentiary run without a trial-count policy; no subset plan.
- **INV-3** Exploratory runs contribute nothing.
- **INV-4** E13 never → E12; E11a/E11b never carry eligibility.
- **INV-5** Every evidentiary run of a scope counts; only E14 under an
  accepted objective rule removes one.
- **INV-6** Only current aggregate heads are evaluated.
- **INV-7** Open, incomplete, unjudged, failed, or indeterminate runs block
  `passed`.
- **INV-8** A result serves a new B16 check only at the current head.
- **INV-9** One committed output per planned trial; completed outputs never
  retried or replaced.
- **INV-10** Every re-attempt carries a B9 admission; no authorization → no
  re-attempt; no attempt while existence is unknown; none after E8.
- **INV-11** One terminal per attempt and run; no early acknowledgement.
- **INV-12** Counts and digests from one frozen terminal set plus E7r; E7
  and E8 never rewritten.
- **INV-13** E12 binds analyst, messenger, and combined identities exactly.
- **INV-14** Nothing edited or deleted; no committed B16 record altered.
- **INV-15** **No cell is satisfied without an actual complete, current,
  passed, full-plan run; zero runs → `incomplete`.**
- **INV-16** **No named measurement is satisfied without recorded results;
  missing → `incomplete`.**
- **INV-17** **Ledger positions are unique (CAS-1); no two entries share a
  sequence number.**
- **INV-18** **Aggregate heads change only by CAS-2; forks and same-key
  conflicts are `indeterminate`.**
- **INV-19** **One deterministic result per scope + head + evaluated set;
  conflicting content under one identity satisfies nothing.**
- **INV-20** **At most one conclusive E7r per attempt.**
- **INV-21** **No benchmark E1 without an accepted concrete suite (D15).**
- **INV-22** **Each effectively completed output has at most one current
  judgment head; heads change only by CAS-3; a fork or contradiction makes
  the chain `judgment_indeterminate`; recency never decides.**
- **INV-23** **No E9 commits without a present, verifiable, authorized
  authority reference matching its E1 judgment mode; model assistance never
  counts; no Ness judgment before D16 is accepted.**
- **INV-24** **Every run is scored by its own suite kind's rule; sealed-gold
  runs are always graded by the gold rules, including inside E12.**
- **INV-25** **Every operation ID — including every O-APPEND — has exactly
  one terminal and one log; a lost race yields a new O-APPEND with a new ID
  and the unchanged canonical key and content.**
- **INV-26** **No operation is simultaneously pending and durably
  non-successful: a claim is `released` only after its O-JUDGE's durable
  non-success terminal; a pending O-JUDGE's claim stays owned and fenced.**
- **INV-27** **A claim with a durable consumption receipt is never
  replaced by another claim or another consumed token for the same scope
  — `judgment_committed` or `closed_after_breach` are its only closures;
  `released`/`superseded` are no-receipt states only; a new claim is
  admitted only with positive proof that no valid receipt exists.**

---

## §11 — Held-out boundary

Mechanics generic; nothing about held-out content, sampling, size, scoring,
judge, secrecy, or threshold is invented; gold rules not assumed; judgment
authority unset; input 4 `not_available` until decided.

**Recommendation for Ness (labelled; not decided):** a separately versioned
and protected held-out set not used to tune the evaluated configuration,
with provenance proving its relationship to the tuning process.

---

## §12 — B16 promotion-policy boundary

`promotion_decision_ref` preserved. A29 did not settle B16 promotion policy
(A29 §0, §6; closure §7); A31 §10 lists it open. Not decided: evidence
combination; batch coverage; case promotability. `promotion_committed`
absorbing (§6.4).

---

## §13 — Mechanical safety

### §13.1 Recovery (lookup-first; row labels `[proposed]`)

| # | Condition | Resolution |
|---|---|---|
| CR-1 | Crash before E5 | No run |
| CR-2 | E5, no attempts | Start ordinal 1 of planned trials |
| CR-3 | E6, output found by key, no E7 | E7 `attempt_completed`; never re-invoke |
| CR-4 | E6, output provably absent | E7 `attempt_interrupted_abandoned`; further attempt only by B9 admission |
| CR-5 | E6, existence undeterminable | E7 `attempt_unresolved`; no attempt for that trial; resolution only by E7r (§7.10) |
| CR-6 | B9 admission committed, no E6 | Start the admitted attempt, or B9 records it abandoned |
| CR-7 | B9 episode exhausted | Trial uncovered; run open (blocks pass) or closed incomplete (blocks pass in scope); continuation only via B9 real-change |
| CR-8 | E7 present, attempt log absent | Append the missing log; then acknowledge |
| CR-9 | All attempts terminal, none live, no E8 | Commit E8 + E16; then the run log |
| CR-10 | E8 present, run log absent | Append the missing log |
| CR-11 | Crash inside a CAS-1 boundary | Atomic: record and entry both or neither; lookup finds which |
| CR-12 | Lost CAS-1 race | That O-APPEND ends `lost_race_technical` (one terminal, one log); B9 may admit a new O-APPEND — new operation ID, unchanged canonical key and content; no B9 admission → nothing committed |
| CR-13 | Lost CAS-2 race | Identical → absorbed; stale expected head → refused, fresh aggregate may be computed |
| CR-14 | Aggregate fork or same-key different content found | Run `indeterminate`; both preserved |
| CR-15 | Crash during E11/E12 derivation | Nothing committed; re-derivation at the same head yields the same identity and content |
| CR-16 | Same-identity result with different content found | `result_contradiction`; neither usable; scope results `indeterminate` |
| CR-17 | E7r conclusive outcomes contradict | `indeterminate`; all preserved |
| CR-18 | Absence proven after E8 | No attempt; effective run state `incomplete` |
| CR-19 | Output found after E8 | E8 preserved; effective state may become completed; new aggregate required |
| CR-20 | Later E9 / E7r / E10 / E14 / E15 | Head advances; earlier results not current |
| CR-21 | Suite integrity mismatch | Every run on it `indeterminate` |
| CR-22 | Unreadable record | `indeterminate` downstream |
| CR-23 | Duplicate recovery | Lookup-first no-op |
| CR-24 | Two O-JUDGEs extend the same head concurrently | One wins (CAS-3); the other's O-APPEND ends `refused_domain_precondition` / O-JUDGE `judgment_refused_stale_head` — non-retryable; Ness may deliberately judge again against the new head |
| CR-25 | Identical E9 re-submitted | `absorbed` |
| CR-26 | Fork found (two committed successors of one predecessor) | Chain `judgment_indeterminate`; trial, run head, and results `indeterminate`; both preserved; no resolution defined (§20) |
| CR-27 | E9 bytes do not match its identity, or same identity with different content | Contradiction; as CR-26 |
| CR-28 | A committed E9's authority proof later found unreadable, mismatched, contradictory, or invalid **at judgment time** | That chain `judgment_indeterminate` until verified by lookup. **Not** triggered by a token being `consumed` (the success state), by ordinary later session expiry or closure, or by the passage of time |
| CR-31 | BAI option: crash before the durable receipt (after claim, after validation, or during/after in-memory consumption) | Original token gone after restart (BAI in-memory only); no receipt → no authority; recovery never consumes with the original token and never backfills a BAI event; O-JUDGE → `judgment_authorization_failed` (one terminal, one log); claim → `released` (linked); a new O-JUDGE with a new token and new claim is required (§7.12 A item 7) |
| CR-32 | BAI option: crash after flushed receipt, before E9 commit | Claim `consumed_pending_commit` (fenced); recovery verifies the receipt and forward-completes exactly the named E9 once via O-APPEND; no re-consumption; no fabrication; no competing O-JUDGE may consume or commit for that scope meanwhile; orphaned receipt (no matching claim) → nothing commits |
| CR-33 | BAI option: replay / reuse of a consumed, expired, or revoked token | Refused (`judgment_refused_authority`), non-retryable, logged |
| CR-34 | SACL option: session later expires or closes | Committed judgment unaffected |
| CR-35 | BAI option: receipt-write failure in-process (possible in-memory consumption) | Terminal for that token; never retried; O-JUDGE → `judgment_authorization_failed`; claim → `released`; new token + new O-JUDGE required; BAI state never reconstructed from bridge records |
| CR-36 | Two concurrent claims for one scope | One wins; the loser's O-JUDGE → `judgment_claim_lost`, its token untouched (never consumed); only the winner's attached token may be consumed |
| CR-37 | Competing O-JUDGE while the scope is `consumed_pending_commit` | Refused before any consumption (`judgment_refused_stale_head` or claim refused); the fence holds until forward completion or breach |
| CR-38 | Unrelated ledger movement during forward completion | The forward-completing O-APPEND may lose CAS-1 → `lost_race_technical`; B9 admits a new O-APPEND (new ID, unchanged E9 key/content); the receipt is not re-established |
| CR-39 | Judgment head changed contrary to the fence (integrity breach) during forward completion | Do not force the stale E9; record the contradiction; chain `judgment_indeterminate`; claim → **`closed_after_breach`** (receipt-bearing, non-replaceable, linked to the contradiction); receipt preserved, never re-applied; **no replacement claim, no second token consumption, no chain extension** absent an accepted resolution policy |
| CR-40 | New deliberate O-JUDGE after a prior claim | Admitted **only** when the prior claim is `released`/`superseded` **and** positive proof exists that no valid durable receipt is bound to it (prior O-JUDGE at `judgment_authorization_failed` or `judgment_claim_lost`); new claim links `supersedes_claim_ref`; new token; new O-JUDGE ID. Refused while the prior claim is `claimed` (pending owner), `consumed_pending_commit`, `judgment_committed`, or `closed_after_breach` |
| CR-29 | Crash between O-JUDGE's O-APPEND commit and O-JUDGE's log | Append O-JUDGE's missing log; then acknowledge |
| CR-30 | O-APPEND exhausted under B9 | The requested record is not committed; the requesting operation remains honestly open/pending with no terminal (§13.5); the run cannot close; scope result `incomplete`; continuation only via a new B9 episode under a consumed real-change record |

### §13.2 Adverse-result retention

E14 only under an accepted objective invalidity rule with recorded facts;
none exists (D10); no run can currently be excluded; never "because another
run passed."

### §13.3 Conflicting completed judged runs

Any `failed` head → `failed`; else any `indeterminate` → `indeterminate`;
only an accepted D11 policy can resolve, through an E15 binding every
affected run. Open, incomplete, and unjudged runs block directly (§8.2).

### §13.4 Privacy and access

§7Q governs every record, ledger, and log; §7Q before §7R; SACL where
applicable; identities and integrity references only; access failure is
`unauthorized`.

### §13.5 §0B logging

One operation → one log at its terminal, one-to-one with that operation's
terminal vocabulary. Log names `[all proposed]`:

| Operation | Log (one per terminal; one log per operation ID) |
|---|---|
| O-SUITE / O-SETUP | `eval_suite_registered` / `eval_suite_refused`; `eval_setup_registered` / `eval_setup_refused` |
| O-RUN | `eval_run_terminal` (carrying `run_completed` / `run_closed_incomplete` / `run_indeterminate`) |
| O-ATTEMPT | `eval_attempt_terminal` (carrying the E7 outcome) |
| O-RESOLVE-ATTEMPT | `eval_attempt_resolved` / `eval_attempt_resolution_refused` |
| **O-JUDGE** | `eval_judgment_committed` / `eval_judgment_absorbed` / `eval_judgment_refused_stale_head` / `eval_judgment_refused_authority` / `eval_judgment_refused_mode_mismatch` / `eval_judgment_refused_output_invalid` / **`eval_judgment_claim_lost`** / **`eval_judgment_authorization_failed`** (carrying the exact reason: pre-receipt crash; failed/unverifiable receipt write; refusal before consumption; head breach after receipt) — one per O-JUDGE, naming its claim and the claim's resulting closure state |
| Judgment-authorization claim transitions (`claimed` / `consumed_pending_commit` / `judgment_committed` / `released` / `superseded` / `closed_after_breach`) | **Canonical state records** (child events of the O-JUDGE), not operational logs; never a second O-JUDGE log |
| BAI events (`bai_token_consumed` receipt; any live `bai_token_consume_blocked`; BAI audit) | **BAI's own**, written only by BAI during live operations; referenced by E9 and the claim; **never created, backfilled, or duplicated by this bridge or by recovery** |
| O-AGGREGATE | `eval_aggregate_committed` / `eval_aggregate_absorbed` / `eval_aggregate_refused_stale_head` |
| O-RESULT | `eval_result_committed` / `eval_result_absorbed` / `eval_result_contradiction` |
| O-EVREF | `eval_evidence_ref_issued` / `eval_evidence_ref_refused` |
| O-INVALIDITY / O-CONFLICT | `eval_invalidity_committed` / `eval_invalidity_refused`; `eval_conflict_resolution_committed` / `eval_conflict_resolution_refused` |
| **O-APPEND** | `eval_append_appended` / `eval_append_absorbed` / `eval_append_lost_race_technical` / `eval_append_refused_domain_precondition` — each O-APPEND (including every B9-admitted new O-APPEND) has its own operation ID and exactly one of these |
| O-RECOVERY | `eval_recovery_applied` / `eval_recovery_noop` |

**No duplicate logs across O-JUDGE, O-APPEND, and B9:** O-JUDGE logs its own
terminal once (naming the O-APPEND that committed or refused its E9);
each O-APPEND logs its own terminal once; **B9 logs only its own retry-request
operations** (R0–R4, under B9 §10) and references the O-APPEND identities —
it never re-logs an O-APPEND's terminal. BAI's own security-audit events
(§25.6) belong to BAI and are referenced by E9, never copied. B16 logs its
own verification under B16 §10. Nothing adds certainty.

**Requesting operation after O-APPEND exhaustion (CR-30, stated
exactly).** When every B9-admitted O-APPEND for a requested record has ended
`lost_race_technical` and B9's episode is exhausted (attempt gate or
deadline) or early-stopped, **the requesting domain operation (e.g. O-JUDGE,
O-ATTEMPT's terminal commit, O-RUN's E8 commit) has not committed its
record and therefore has not reached its terminal: it remains honestly
open/pending** — exactly as accepted B9 keeps a failed job `in_progress`
with its recorded pass failure (B9 §1 settled facts; B9 values §9). B9's
exhaustion disposition names the stopping gate and references the
preserved state. **No second terminal, no false completion, no hidden
retry, no invented "exhausted" terminal for the domain operation.**
Continuation is only a new B9 episode through a consumed real-change record
with unchanged canonical inputs (B9 values §10). While the domain operation
is pending, its run cannot close (E8 requires every started attempt's E7 and
no live attempt), so the scope result is `incomplete`; if the pending
operation is O-JUDGE, the output has no current head → `incomplete`.

**Two distinct pending situations for O-JUDGE (corrected v1.7 — one
coherent rule):**
- **Ordinary O-APPEND exhaustion before any authority consumption** (in
  practice the SACL-only option, where O-JUDGE's only durable stage is the
  O-APPEND commit): the O-JUDGE **remains pending** under accepted B9
  exhaustion semantics with no terminal; **its claim stays `claimed` and
  owned — it is not released**; the one-winner fence holds; **a competing
  O-JUDGE for the same scope cannot win**; continuation occurs **only**
  through the permitted new B9 episode (consumed real-change record,
  unchanged canonical inputs) and a new O-APPEND **under that same
  O-JUDGE**. While pending, the output has no current head → `incomplete`.
- **`consumed_pending_commit`** (a durable receipt exists, E9 not yet
  committed): the scope is **fenced**; no other O-JUDGE may consume a
  token or commit a competing successor; the pending O-JUDGE is
  **forward-recoverable only** — recovery completes exactly its named E9
  (via B9-admitted O-APPENDs if the ledger moved), or, on a head breach,
  records the contradiction and closes the claim `closed_after_breach`
  (non-replaceable). The authorization is never lost, duplicated,
  redirected, or applied to another judgment.

**Release is permitted only after the owning O-JUDGE has reached an
applicable durable non-success terminal** (`judgment_authorization_failed`
— pre-receipt crash, failed/unverifiable receipt write, refusal before
consumption; or `judgment_claim_lost`) **and no valid receipt exists.**
Then, and only then, the no-receipt claim is `released` and a new O-JUDGE
with a new token may begin (CR-40). A pending operation and a released
claim never coexist; a released claim and a durable receipt never coexist
(INV-26, INV-27).

---

## §14 — Fail-closed matrix

| Condition | Behavior |
|---|---|
| Trial-count or other epoch policy unset | No evidentiary run; no pass |
| No accepted concrete B24 suite (D15) | No benchmark E1; no E12 `eligible` |
| E3 names cells/measurements but runs missing | `incomplete` |
| Zero runs in scope | `incomplete` |
| Judgment authority absent, unverifiable, unauthorized, mismatched, model-only, or D16 unaccepted | E9 refused; output unjudged → `incomplete` |
| Held-out judgment authority unset | No held-out E9 |
| Stale competing judgment | Refused (non-retryable) |
| Judgment fork or contradiction | `judgment_indeterminate` → trial, run, results `indeterminate` |
| Sealed-gold run fails the gold rule | Gold head `failed`; B24 tolerance never rescues it |
| Lost ledger race | `lost_race_technical`; new O-APPEND only by B9 admission |
| Named measurement not recorded | `incomplete` |
| Subset trial plan | E5 refused |
| B9 does not authorize a re-attempt | No re-attempt |
| Attempt requested while existence unknown, or after E8 | Refused |
| Retry of a completed output | Absorbed |
| Open / incomplete / unjudged / failed run in scope | Blocks pass |
| Lost ledger or aggregate race | Nothing committed / absorbed / refused |
| Fork, same-key or same-identity conflict | `indeterminate`; unusable |
| Result head not current | Not available for new checks |
| Held-out undefined | Input 4 not available |
| Binding mismatch | Not applicable / not available |
| Exclusion without an accepted objective rule | Refused |
| Unauthorized access | Unauthorized |

---

## §15 — Traces (examples; no values chosen)

**T-1 — Two engines, one profile.** P: model M; A = gold v1 → Engine A;
B = gold v2-B → Engine B. RA, RB complete, judged, current heads `passed`;
no other run. E11a(P) `passed` at head h. An Engine-B reading matching B →
`applicable_passed`.

**T-2 — Unlisted path.** Engine C reading → `not_applicable`.

**T-3 — Prompt changed.** New prompt version → no binding → `not_applicable`.

**T-4 — Adverse result kept.** One passed and one failed completed RB →
`failed`; an E14 "because the other passed" is refused.

**T-5 — Crash after output.** CR-3 → completed; no second model call.

**T-6 — Crash before output, B9 retry.** CR-4 → B9 admits ordinal 2 within
gap and deadline → same planned-trial key; both attempts in the frozen set.

**T-7 — Rules moved after results.** New epoch → old result stale; new
scope discloses the old one.

**T-8 — Exploratory.** `non_evidentiary`; uncitable.

**T-9 — Gold is not eligibility.** E11a `passed`; no E12 can be eligible;
input 3 can still be satisfied.

**T-10 — Absorbing promotion.** Later adverse evidence; R stays promoted.

**T-11 — Abandon-and-repeat impossible.** Within scope S, stopping, closing,
failing, leaving unjudged, re-running, excluding without an objective rule,
retrying completed outputs, and killing attempts before commit each leave S
without a pass while R1's record stands; only a recorded new epoch or a
genuinely different configuration opens a new, disclosed scope.

**T-12 — Later evidence stales an old pass.** New run R3 → head h+1 →
AP-3 fails → a fresh derivation sees R3 open → `incomplete`.

**T-13 — No retry-until-pass.** A judged-`fail` output → B9
`terminal_success` → retry absorbed; `fail` stands.

**T-14 — B9 exhaustion.** Trial uncovered → `incomplete`; real-change
continuation completes it.

**T-15 — Multi-role E12.** E4S = analyst A1 + messenger M1 + handoff H;
every required cell and measurement satisfied → `eligible`; swapping M1 →
new scope.

**T-16 — Omitted family refused.** An E3 with no cell for
"failure/recovery" → EB-2 refuses.

**T-17 — Zero runs, no vacuous pass (v1.3).** A valid E3 lists
every required cell and all fourteen measurements; no run has opened. E12
derivation: every cell unsatisfied → `incomplete`. E11a for a gold scope
with zero runs: gold cells unsatisfied → `incomplete`.

**T-18 — Partial coverage.** Every cell except one "multilingual status
preservation" messenger cell has a passed run → that cell unsatisfied →
E12 `incomplete`, naming the cell.

**T-19 — Missing measurement.** Every cell passed, but no current head
records M-M3 (translation fidelity incl. Hebrew) → `incomplete`, naming
M-M3. Every cell passed and M-C2 recorded above the latency budget → the
covering head is `failed` → E12 `not_eligible`.

**T-20 — Gold unmet in E12.** All benchmark cells pass; the gold v2-B cell
has no current passed B24-family run through Engine B → `incomplete`.

**T-21 — Ledger race (CAS-1), operation IDs exact.** Two judgments of two
*different* outputs in one scope: O-JUDGE J1 requests O-APPEND A1; O-JUDGE
J2 requests O-APPEND A2; both expect ledger head `{n, d}`. A1 commits J1's
E9 as `n+1` and ends `appended`; J1 then ends `judgment_committed`. A2
commits nothing and ends **`lost_race_technical`** — one terminal, one log.
B9 classifies A2 `technical_retryable` and admits a new attempt, which
launches **a new O-APPEND A3 with a new operation ID**, the **same**
canonical key (J2's E9 idempotency key), and the **same** E9 content,
against `{n+1, d′}` → `n+2`, ending `appended`; J2 then ends
`judgment_committed`. A2 is never reused; no ID has two terminals or logs;
no sequence number is shared. (Had J1 and J2 judged the **same** output
against the same judgment head, A2 would instead end
`refused_domain_precondition` — see T-29 — which B9 never retries.)

**T-22 — Aggregate race (CAS-2).** Two O-AGGREGATE operations both expect
head H0. With identical inputs, the second absorbs. If J2 arrived between
them, the later one's inputs differ but it still expects H0 → refused;
a fresh aggregate over the new judgment set expects H1 and commits. A
discovered fork (two committed E10s superseding H0) → run `indeterminate`.

**T-23 — Result collision (DET-1).** Two derivations of E11a at head h and
set digest s produce the same identity: identical content → absorbed.
Different content under that identity → `result_contradiction` → AP-2 fails
→ B16 gets `indeterminate`; no pass is usable until reconciled by lookup.

**T-24 — Crash mid-append.** Power fails during a CAS-1 boundary → CR-11:
either the record and its entry both exist or neither does.

**T-25 — Unresolved attempt resolved.** Attempt a1 ends `attempt_unresolved`
before E8; no attempt for that trial starts. (i) E7r `resolved_output_found`
→ effective completed; judged; the run can complete. (ii) E7r
`resolved_absence_proven` → B9 may admit ordinal 2 within limits. (iii)
`still_undetermined` → nothing starts; the run can close only as
`run_indeterminate`.

**T-26 — Resolution after E8.** Run closed `run_indeterminate` because a1
was unresolved. (i) Output found → E8 preserved; effective run state
completed; a new aggregate may pass. (ii) Absence proven → no attempt can
start; effective run state `incomplete`; the scope cannot pass while this
run stands (no accepted rule permits another path).

**T-27 — Unauthorized judge, no false pass.** A gold output is "judged"
`pass` by (i) a model, (ii) a typed name with no §25 artifact, (iii) a §25
artifact that is not of the D16-required kind, (iv) anything today, since
D16 is unaccepted. Each O-JUDGE is refused (`judgment_refused_authority`);
no E9 commits; the output has no current head → run head `incomplete` →
E11a `incomplete`. No path to `passed` exists without verified Ness
authority.

**T-28 — Competing initial judgments.** Output o has no judgment. Two
O-JUDGEs both name expected head `none`. One commits (CAS-3); the other is
refused `judgment_refused_stale_head` (non-retryable). If both carried the
identical E9 (same identity and content), the second **absorbs** instead.
The chain has exactly one head.

**T-29 — Competing corrections.** Chain head is J1. Ness submits
correction J2 (expected head J1) while another correction J3 (expected
head J1) is in flight. J2 commits; J3 is refused as stale. J1 and J2 are
both preserved; J2 is the head. To change J2, Ness makes a new deliberate
correction naming J2. Nothing is retried automatically; the later-arriving
correction does not win by recency.

**T-30 — Fork found.** An integrity audit finds J2 and J3 **both**
committed with expected head J1 (a CAS breach). Chain o →
`judgment_indeterminate`; o's run head → `indeterminate`; E11a/E12 over
that scope → `indeterminate`; B16 AP-2/AP-4 fail. No E9 can extend the
chain; no resolution procedure is defined (§20). Neither J2 nor J3 is
chosen.

**T-31 — Gold inside E12 is graded by gold rules.** An E12 scope includes a
gold v2-B cell. The B24 epoch binds the D2 gold rule (say, zero failed
cases — a placeholder here, not a chosen value) and a B24 tolerance that
would allow one CONSEQUENTIAL failure. The gold v2-B run has one case
Ness-judged `fail` (made-up extra, gold rule 4). The gold case carries no
§7C category (E1, v1.5): the failure is a **gold** failure, not a
"CONSEQUENTIAL" one. E10 for that run applies the **gold** rule → head
`failed`. The gold cell is unsatisfied → E12 `not_eligible`. B24's tolerance
is applied only to benchmark-family heads and never re-grades the gold head;
the run cannot pass under B24 tolerance, and no §7C label was ever attached
to the gold case to make that possible.

**T-32 — BAI option: consumption is the proof (§7.12 A).** D16 (assumed here
only for the trace) selects one BAI token per judgment. Ness judges output
o. O-JUDGE records the claim {E9 identity, token t}; verifies t valid,
unexpired, unrevoked, unconsumed, purpose-matched, bound to this judgment;
consumes t under BAI rules; the `bai_token_consumed` receipt is flushed;
E9 binds the receipt and commits with E16. t is now `consumed` — the
success state. A later check of E9 sees a consumed token and a matching
receipt → valid. No refusal, no invalidation.

**T-33 — Replay.** After T-32 an O-JUDGE presents t again (or presents a
token whose receipt already exists) → refused `judgment_refused_authority`,
non-retryable; BAI additionally rejects the consume; logged. One token never
authorizes two judgments (absent a D16-selected session-scoped mechanism).

**T-34 — Pre-receipt crash, then restart (corrected v1.6).** Claim C1
(`claimed`, token t attached); power dies before the receipt is durable —
whether before the consume call or during in-memory consumption. On
restart BAI's state is cleared: **t no longer exists**. Recovery finds C1
with no receipt → no authority was committed; it never reconstructs t and
never proceeds to consume; O-JUDGE J1 ends **`judgment_authorization_failed`**
(reason: pre-receipt crash) with one log; C1 → `released` (linked). No
BAI event is created. Ness later judges again: new O-JUDGE J2, new BAI
flow, new token t2, new claim C2 (`supersedes_claim_ref` = C1). Nothing
was granted by C1; nothing is lost.

**T-35 — Crash after flushed receipt, before E9.** Receipt flushed; C1 →
`consumed_pending_commit`; power dies before E9 + E16 commit. Recovery
finds the receipt and C1 → forward-completes exactly the E9 C1 names (same
content identity, same expected head) via O-APPEND; **no second
consumption**; C1 → `judgment_committed`; J1 ends `judgment_committed`.
The authorization is not lost or duplicated. A receipt found with no
matching claim → orphaned; no judgment is created from it.

**T-38 — Receipt-write failure after possible in-memory consumption
(no crash).** BAI's consume call runs; the receipt write fails or cannot
be verified. **Terminal for t**: t is never retried, whether or not BAI's
memory shows it consumed; J1 → `judgment_authorization_failed` (reason:
receipt write failed); C1 → `released`; no BAI event is written by the
bridge; a new token and new O-JUDGE are required.

**T-39 — Two concurrent claims, two tokens.** J1 (token t1) and J2 (token
t2) both attempt to claim scope {chain o, head J0}. The claim's uniqueness
constraint admits one — say J1's C1. J2 ends **`judgment_claim_lost`**; t2
is **never consumed**. Only t1 (attached to C1) may be consumed. One scope
can never hold two receipts.

**T-40 — Competing O-JUDGE while `consumed_pending_commit`.** C1 holds a
durable receipt; E9 not yet committed. J3 tries to judge scope {o, J0}:
the fence refuses J3 before any consumption (`judgment_refused_stale_head`);
J3's token is untouched. Recovery forward-completes C1's E9; J3 may then
judge against the new head with a new claim.

**T-41 — Unrelated ledger movement during forward completion.** While
recovery forward-completes C1's E9, another judgment of a different output
advances the scope ledger. C1's O-APPEND loses CAS-1 → `lost_race_technical`;
B9 admits a new O-APPEND (new ID; unchanged E9 key, content, receipt
binding) → `appended`. The receipt was consumed once and used once.

**T-42 — Head breached during forward completion (v1.7).** Recovery finds
C1 (`consumed_pending_commit`, expected head J0, durable receipt R1) but
the chain's head is now J9, committed without a claim (an integrity
breach). The stale E9 is **not** forced through: the contradiction is
recorded; chain o → `judgment_indeterminate`; C1 → **`closed_after_breach`**
(linked to the contradiction); O-JUDGE J1 → `judgment_authorization_failed`
(reason: head breach; one terminal, one log); R1 is preserved and never
re-applied. **Afterwards:** Ness tries to judge o again with token t2 →
the scope's claim is `closed_after_breach`, which is not `released`/
`superseded` and has a receipt → admission refused; **t2 is never
consumed**; no new claim exists. Any attempt to extend the chain (any E9
naming J0 or J9) is refused: the chain has no single head. Only a future
accepted resolution policy — none exists — could reopen the scope. No
replacement claim, no second token consumption, no chain extension.

**T-44 — Receipt + breach: no replacement (v1.7, adverse).** Same setup
as T-42. An operator argues "the receipt's judgment is unusable, so release
C1 and let a fresh token authorize a new judgment." Refused mechanically:
`released` requires positive proof that no valid receipt exists, and R1
exists and verifies; `closed_after_breach` admits no successor. The
scope stays indeterminate; one token was consumed for it, ever.

**T-45 — SACL-only O-APPEND exhaustion (v1.7, adverse).** SACL-only
option. O-JUDGE J1 claims scope {o, J0} (C1 `claimed`); its E9 O-APPENDs
lose three ledger races and B9's episode is exhausted. J1 **remains
pending** (no terminal); **C1 remains `claimed` and owned**; the output has
no current head → `incomplete`. A competing O-JUDGE J2 for {o, J0} →
admission refused (scope owned; C1 not released). A real change (repaired
ledger contention) is recorded and consumed → B9 opens a new episode → a
new O-APPEND **under J1** commits E9 → J1 `judgment_committed`; C1
`judgment_committed`. J2 never won.

**T-46 — Pre-receipt crash / unverifiable receipt (v1.7, adverse).** BAI
option. C1 `claimed`, token t1; crash before the receipt (or the receipt
write cannot be verified). J1 → `judgment_authorization_failed` (durable
non-success terminal, one log). Positive proof: no `durable_receipt_ref`,
and no verified `bai_token_consumed` for C1 in the audit history → C1 →
`released` (linked). Only now may J2 begin: new BAI flow, new token t2,
new claim C2 (`supersedes_claim_ref` = C1). t1 is never reused.

**T-47 — Never pending and non-successful at once (v1.7, adverse).**
Walk every O-JUDGE state: pending (no terminal) ↔ claim `claimed` or
`consumed_pending_commit`; terminal `judgment_committed` ↔ claim
`judgment_committed`; terminal `judgment_authorization_failed` /
`judgment_claim_lost` ↔ claim `released` (or `closed_after_breach` on a
breach); terminal refusals before a claim ↔ no claim. No row pairs a
pending operation with a released claim, and no row pairs a durable
non-success terminal with an owned pending claim (INV-26).

**T-43 — One operation, one terminal, one log across the chain.** For
one successful judgment: the claim's states are canonical child records
(no log of their own); BAI writes its own receipt/audit (not duplicated);
O-JUDGE J1 has one terminal (`judgment_committed`) and one log; its
O-APPEND A1 has one terminal (`appended`) and one log; if A1 lost a race,
A1 has one terminal (`lost_race_technical`) and one log, B9 logs its own
R0–R4 request once, and the new O-APPEND A2 has its own one terminal and
one log. No ID appears twice; no event is written by two owners. **Under
v1.7 the same holds for every new outcome:** a pending J1 has no terminal
and no log until it ends; a breached J1 has exactly one terminal
(`judgment_authorization_failed`) and one log; claim closures
(`released`, `superseded`, `closed_after_breach`) are canonical child
records, never a second log.

**T-36 — SACL option: later expiry does not erase (§7.12 B).** D16
(assumed for the trace) selects fresh recognized-Ness session proof. At
O-JUDGE commit the SACL state is verified fresh and valid; E9 binds the
immutable event-time reference. An hour later the session closes and the
lease is revoked. E9 stays valid: its truth is about its commit moment.
CR-28 is not triggered.

**T-37 — SACL option: invalid at judgment time.** Later lookup shows a
security event (speaker change) recorded as effective **before** the E9
commit timestamp, contradicting the bound reference → CR-28: chain
`judgment_indeterminate`; the run head and results `indeterminate`; fail
closed; nothing chosen.

---

## §16 — Dependency matrix

"Req" = required to reach `passed`/`eligible`/committed; "—" = not a
dependency.

| Accepted reference | Gold evidence (E11a → input 3) | Held-out evidence (E11b → input 4) | B24 system eligibility (E12) | Final B16 promotion |
|---|---|---|---|---|
| Sealed gold v1 + v2-B (settled) | Req (as E3 selects) | — | Req (rule 8) | via input 3 |
| Approved execution paths (settled) | Req | per held-out policy | Req (where mapped) | via inputs |
| Accepted B9 + values (settled; NHD-B9, NHD-B9W) | Consumed | Consumed | Consumed (incl. lost races) | — |
| D1 planned trial count | Req | Req (unless D7 defines its own) | Req | via inputs |
| D2 tolerance / acceptance rule | Req (gold) | Req (via D7) | Req (§7C) | via inputs |
| D3 latency budget(s) | — | — | Req | only if D12 requires E12 |
| D4 GPU/RAM / coexistence limits | — | — | Req | only if D12 requires E12 |
| D5 hardware-need / purchase criteria | — | — | Req | only if D12 requires E12 |
| D6 held-out definition | — | Req | — | via input 4 |
| D7 held-out judgment and scoring | — | Req | — | via input 4 |
| D8a gold coverage profile | Req | — | — | via input 3 |
| D8b held-out coverage profile | — | Req | — | via input 4 |
| D9 B24 role mapping (constrained) | — | — | Req | only if D12 requires E12 |
| **D15 concrete B24 benchmark suites** | — | — | **Req** | only if D12 requires E12 |
| **D16 judgment-authority proof (§25 artifact kind)** | **Req** (every gold case is a Ness judgment) | per D7 (only if the held-out policy assigns Ness) | **Req** (gold cells + B24 meaning-dependent cases) | via inputs |
| D10 objective invalidity rule | Only to exclude | same | same | — |
| D11 completed-run disagreement policy | Only to resolve a conflict | same | same | — |
| D12 promotion combination | — | — | — | Req |
| D13 batch applicability | — | — | — | Only for batches |
| D14 case promotability | — | — | — | Only for case-output readings |
| Other B16 inputs | — | — | — | Req (B16 §5.3) |

Input 3 can become satisfiable once D1, D2 (gold), D8a, and **D16** are
accepted and real, complete, authorized-judged gold runs exist — it does not
wait for held-out, budgets, D9, D15, or promotion decisions. E12
additionally needs D3, D4, D5, D9, and D15.

---

## §17 — Ness decision register (seventeen slots; independently selectable)

Settled → choice → effect → labelled recommendation → why not mechanical.
Retry attempts, gaps, deadlines, and continuation are settled by B9.

**D1 — Planned trial count.** Settled: repeated trials (rule 4).
*Recommendation:* fixed count per case, at least three, identical for every
candidate. Not mechanical: confidence vs time.

**D2 — Tolerance / acceptance rule (gold; B24).** *Recommendation:*
absolute counts per suite, zero on the sealed gold floor, any-CRITICAL
mirrored for gold. Not mechanical: risk tolerance.

**D3 — Latency budget(s).** *Recommendation:* strict for the messenger;
looser for analyst and asynchronous paths. Not mechanical: waiting
preference.

**D4 — GPU/RAM, coexistence limits.** *Recommendation:* against the RTX
3090 24GB direction, coexistence measured. Not mechanical: envelope.

**D5 — Hardware-need / purchase criteria.** No recommendation. Not
mechanical: money.

**D6 — Held-out definition.** *Recommendation:* §11's. Not mechanical:
defines "unseen."

**D7 — Held-out judgment and scoring.** No recommendation. Not mechanical:
authority.

**D8a / D8b — Gold / held-out coverage profiles.** *Recommendation (D8a):*
both sealed sets through their bound paths for every reading-mouth path.
Not mechanical: what counts as enough.

**D9 — B24 role mapping.** Settled: eight families, three scopes, fourteen
measurements, gold — none may be omitted. Choice: which scope runs each
family. **It is not suite content.** No recommendation. Not mechanical:
test design.

**D10 — Objective invalidity rule.** *Recommendation:* only conditions
provable from recorded integrity or fault records. Not mechanical: what
counts as a broken test.

**D11 — Completed-run disagreement policy.** Scope unchanged: conflicting
**completed, judged runs** of one scope. It does **not** cover judgment
forks or disagreement between judgments of one output (those fail closed;
§7.11, §20). No recommendation. Not mechanical: evidentiary judgment.

**D12 — Promotion combination.** *Recommendation:* per reading, applicable
gold, applicable held-out, manual inspection, and a decision. Not
mechanical: trust.

**D13 — Batch applicability.** *Recommendation:* every reading named. Not
mechanical: trust scope.

**D14 — Evaluation-case promotability.** No recommendation. Not mechanical:
policy.

**D15 — Concrete B24 benchmark suites (new).** Settled: the eight §7B.2
families, the fourteen §7B.3 measurements, §7C severity, and rules 1–8 —
but no concrete suites. Choice: approve, per family, concrete versioned
cases/prompts, their scoring bindings (DUMB-decided vs Ness-judged; §7C
category mapping), their declared measurements, and their integrity
identity. Effect: without it no benchmark E1 registers and no E12 can ever
be `eligible`. *Recommendation (labelled):* version and seal each family's
suite like the gold sets, so any change is a new version requiring new runs;
authoring follows the normal design route before Ness approves. Not
mechanical: what the test actually asks.

**D16 — Judgment-authority proof (new).** Settled: Ness alone judges sealed
gold and B24 meaning-dependent cases; the accepted identity/security
authority is Master §25 (SACL `recognized_ness`; BAI purpose-bound artifacts,
incl. the `extended:<purpose_id>` form); Bundle 5 shows how other Ness-owned
acts bind them. **No accepted source says which §25 artifact, or
combination, proves Ness performed a recorded evaluation judgment.** Choice:
that requirement (e.g. a recognized-Ness session only; a BAI purpose-bound
artifact under a declared `extended:` purpose; both; per judgment or per
judging session). Effect: until accepted, **no Ness judgment can be
recorded**, so no gold or B24 meaning-dependent output can ever be judged.
*Recommendation (labelled):* reuse an existing accepted pattern rather than
inventing one — the lightest §25 combination that proves Ness himself
performed this specific recorded act, matching how Bundle 5 treats other
Ness-owned acts. Not mechanical: a security-posture choice about Ness's own
authority.

**Open item without a slot (visible, fail-closed):** a **judgment-fork
resolution procedure** — what, if anything, may ever turn a forked or
contradictory judgment chain back into one with a single head. No accepted
source defines one; resolving it may need new Ness policy. Until then the
chain stays `judgment_indeterminate`. It is not folded into D10 or D11.

---

## §18 — Boundaries and status

- DUMB/SMART: bridge machinery DUMB; models SMART; Ness judges where
  assigned; held-out authority unset.
- Quarantine/production, root/reading, sealed gold, benchmark protection:
  unchanged.
- **B16 v1.0, B24 v7, B9 v1.0, B9 values v1_4, the coordination note, and
  every other cited package remain accepted and `PACKAGE_COMPLETE`** for
  their scopes; the gap is an open bridge, not proof an acceptance was
  false.
- **Confirmed rules retained from the v1.2 audit:** output-before-
  visibility (§7.4); prior scopes disclosed, not auto-blocking (§6.3);
  non-live-chat evaluation uses B9 background/nightly classification (§7.6).
- **Confirmed rule retained unchanged from the v1.3 audit:** M-C4 ("whether
  the heavy model must run every turn") must be measured, recorded, and
  reported; it is not pass/fail because B24 §7C supplies no budget for it,
  and none is invented (§4.6).
- The fail-closed implementation is safe but not promotion-ready. **No
  benchmark-eligibility PASS and no promotion-readiness PASS may be
  claimed** until approved policies, approved suites, and real evidence
  exist.
- No implementation, adoption, integration, promotion, model selection, or
  production authorization occurs.

---

## §19 — Observations recorded, not decided

1. Build handoff reports sealed gold v3-B / v3-C and a Context v1 set on
   disk; governance records only v1 and v2-B as sealed and Context v1 as not
   placed/sealed (Master 493). **Not admitted.** Not verified on disk.
2. Historical gold runs have no pre-frozen epoch or ledger: history only.
3. Memory-health architecture (Map B16; Workflow Phase 22): not addressed.
4. A31's no-numbers rule governs `grounding_status` only.
5. Master's production dry-run must name "the promotion-review evidence"
   (§6A); E13 is a natural citation. Not decided.
6. Whether a promotion policy should weigh prior scopes is part of D12.
7. Whether sealed gold material could also serve as concrete content for a
   §7B.2 family (e.g. language fidelity) is part of D15/D9; not assumed.

---

## §20 — Open dependencies and design-complete condition

**Open:** D1–D16; the **judgment-fork resolution procedure** (no slot;
fail closed; §7.11, §17); the first accepted E3; the concrete B24 suites
(D15) and their authoring route; B-CYCLE-6; C2; B16's own input 3/4 verifier
following §9 (Register C); B24's other open items; canonicalization,
integrity algorithms, ledger and CAS storage mechanics; Master/Map
integration; all code/disk/runtime work.

**Design-complete (mechanical scope) when:** §§4–16 are defined; ownership,
judgment authority, B9 consumption, and concurrency rules are explicit;
every policy value and all suite content are open named decisions; nothing
accepted changes. **Design-complete never means evidence-ready.**

---

## §21 — Re-run audits

- **False PASS:** requires current frozen epoch, every run counted, current
  heads only, current ledger head, exact binding, actual cell and
  measurement coverage, no contradiction (INV-1, 5–8, 15–19). None found.
- **Missing run:** zero runs or any unsatisfied cell → `incomplete`
  (T-17, T-18, T-20; INV-15).
- **Missing measurement:** unrecorded named measurement → `incomplete`;
  over-budget → `failed` (T-19; INV-16).
- **Concurrent heads:** CAS-1 prevents shared sequence numbers; a losing
  O-APPEND ends `lost_race_technical`; a B9-admitted new O-APPEND carries a
  new ID and the unchanged key and content (T-21; INV-17, INV-25).
- **Aggregate fork:** CAS-2; identical absorbs, stale refused, fork
  `indeterminate` (T-22; INV-18).
- **Result collision:** DET-1; identical absorbs, different content →
  contradiction, unusable (T-23; INV-19; AP-2).
- **Unresolved attempts:** three E7r outcomes with defined effects; no
  attempt while unknown or after E8; E7/E8 preserved (T-25, T-26; INV-20).
- **B9:** every re-attempt admitted, including lost races; completed
  outputs absorb; no authorization → nothing (T-6, T-13, T-14, T-21).
- **Crash recovery:** CR-1–CR-40 (CR-39/CR-40 rewritten v1.7) incl. CAS boundaries, judgment races,
  forks, O-APPEND exhaustion, derivations, and post-E8 resolutions; no
  double record, lost record, or early acknowledgement.
- **B16 currentness:** AP-2 identity integrity + AP-3 head currentness;
  committed promotions untouched (T-10, T-12, T-23).
- **Unauthorized-judge false pass (new):** model-only, name-only,
  wrong-kind, or pre-D16 judgments are refused; unjudged outputs block
  `passed` (T-27; INV-23). No path found.
- **Competing initial judgments (new):** CAS-3 admits one; identical
  absorbs; the other is refused, non-retryable (T-28; INV-22).
- **Competing corrections (new):** only the correction naming the single
  current head commits; the stale one is refused; recency never wins
  (T-29).
- **Judgment fork / contradiction (new):** chain `judgment_indeterminate`;
  trial, run, and results `indeterminate`; no resolution defined; nothing
  chosen (T-30; CR-26, CR-27).
- **Gold scoring inside E12 (new):** each run scored by its suite kind;
  gold runs always by gold rules; E12's overall rule applied only after;
  a gold failure cannot pass under B24 tolerance (T-31; INV-24).
- **CAS lost-race operation IDs (new):** one terminal and one log per ID,
  including every O-APPEND; lost race technical and B9-retryable with a new
  ID; domain-precondition refusals non-retryable (T-21; CR-12; INV-25).
- **All earlier v1.3 audits** (false-PASS, missing-run, missing-measurement,
  concurrent-head, aggregate-fork, result-collision, unresolved-attempt,
  B9, crash-recovery, B16-currentness) re-run above against the v1.4
  changes: unchanged results.
- **BAI consumption and replay (v1.5):** the receipt, not token presence,
  is the proof; `consumed` after this judgment's own consumption is the
  success state and never refuses or invalidates; replay/reuse refused,
  non-retryable (T-32, T-33; CR-33; §7.12 A). No path to an unauthorized or
  double-authorized judgment found.
- **Crash before / after consumption (v1.5):** before → nothing granted,
  claim abandoned; after flushed receipt → exactly the claimed E9 completed
  once, no re-consumption, no fabrication, orphaned receipts create nothing
  (T-34, T-35; CR-31, CR-32).
- **Later SACL/session expiry (v1.5):** ordinary expiry/closure never erases
  a validly recorded judgment; proof invalid at judgment time fails closed
  (T-36, T-37; CR-28, CR-34).
- **E1 suite-kind scoring (v1.5):** only benchmark-family cases carry §7C
  categories; gold cases carry none and are graded by the six rules + D2;
  held-out only by its future policy; T-31 re-run under the corrected
  wording — a gold failure still cannot pass under B24 tolerance and no §7C
  label can reach a gold case (INV-24).
- **O-APPEND / O-JUDGE / B9 one-operation-one-log (v1.5):** every O-APPEND
  terminal has exactly one log; every O-JUDGE terminal (incl. absorbed and
  each refusal) has exactly one log; B9 logs only its own R0–R4 operations
  and never re-logs O-APPEND terminals; BAI audit events stay BAI's (§13.5).
  No duplicate found.
- **CR-30 terminal/pending state (v1.5):** after O-APPEND exhaustion the
  requesting operation remains honestly open/pending with no terminal, per
  accepted B9's incomplete-operation rule; no second terminal, no false
  completion, no hidden retry; continuation only via B9 real-change (§13.5,
  CR-30).
- **All v1.4 audits** (unauthorized judge, competing initial judgments,
  competing corrections, fork/contradiction, gold inside E12, CAS lost-race
  IDs) re-run against the v1.5 changes: unchanged results.
- **Two concurrent claims, two tokens (v1.6):** one winner; loser consumes
  nothing; one scope never holds two receipts (T-39; CR-36).
- **Pre-receipt crash + restart (v1.6):** token gone; never reconstructed;
  O-JUDGE `judgment_authorization_failed`; claim released; new flow
  required; no BAI event backfilled (T-34; CR-31; §7.12 A item 7).
- **Receipt-write failure after possible in-memory consumption (v1.6):**
  terminal for that token; never retried (T-38; CR-35; item 7a).
- **Crash after durable receipt before E9 (v1.6):** fenced; forward-
  completed exactly once; no re-consumption (T-35; CR-32).
- **Competing O-JUDGE during `consumed_pending_commit` (v1.6):** refused
  before consumption; fence holds (T-40; CR-37).
- **Unrelated ledger movement during forward completion (v1.6):** B9-
  admitted new O-APPEND, unchanged E9 key/content/receipt (T-41; CR-38).
- **Head breach during forward completion (v1.6):** stale E9 not forced;
  contradiction recorded; chain indeterminate; claim superseded (T-42;
  CR-39).
- **Claim release/supersession before a new token (v1.6):** new claim only
  after durable release/supersession, linked; never while a receipt exists
  (T-34, CR-40; §7.13 replacement rule).
- **One operation / one terminal / one log across claim, BAI, O-JUDGE,
  O-APPEND, B9 (v1.6):** claim transitions are canonical child records;
  BAI events BAI's own; each O-JUDGE, O-APPEND, and B9 request has one
  terminal and one log (T-43; §13.5). No duplicate found.
- **All v1.5 audits** (BAI consumption/replay, crash before/after
  consumption, later SACL expiry, E1 suite-kind scoring, one-log, CR-30)
  re-run against the v1.6 changes: unchanged results, with CR-30 now
  distinguishing pre-consumption exhaustion from `consumed_pending_commit`.
- **Receipt + head breach → non-replaceable (v1.7):** claim
  `closed_after_breach`; no new claim, no second token, no chain extension
  absent an accepted policy (T-42, T-44; CR-39, CR-40; INV-27). No path to
  a second consumption for one scope found.
- **SACL-only O-APPEND exhaustion (v1.7):** O-JUDGE pending, claim owned
  and not released, fence holds, competing O-JUDGE cannot win,
  continuation only under the same O-JUDGE (T-45; §13.5). No path to a
  competing winner found.
- **Pre-receipt crash / unverifiable receipt (v1.7):** durable
  non-success terminal first, then no-receipt release with positive proof,
  then a new flow (T-46; CR-31, CR-35, CR-40).
- **Pending vs durably non-successful (v1.7):** every O-JUDGE state pairs
  with exactly one claim state; none is both (T-47; INV-26).
- **One terminal, one log per O-JUDGE (v1.7):** re-walked with the
  breach terminal and the pending case (T-43; INV-25).
- **Whole-candidate sweep (v1.7):** every statement that treated a
  `released`/`superseded` claim as replaceable now requires positive
  no-receipt proof; `superseded` is confined to no-receipt claims;
  terminal-reason cells no longer cite claim release as a cause. All
  earlier v1.6 audits re-run: unchanged results.

---

## §22 — Correction map (v1.6 → v1.7)

| # | v1.6 audit correction | Where applied |
|---|---|---|
| 1 | Consumed-receipt supersession | New claim state `closed_after_breach` (§7.13 state field and lifecycle); `released`/`superseded` confined to no-receipt claims; replacement rule requires positive no-receipt proof; §7.12 A item 8; CR-39, CR-40 rewritten; §7.2 and §13.5 terminal-reason cells; INV-27; T-42 rewritten; T-44; §20 fork/breach note unchanged (no resolution policy defined) |
| 2 | Pending operation versus released claim | §7.13 `released` definition (only after a durable non-success terminal + positive no-receipt proof) and fence rule; §13.5 two pending situations rewritten (pending O-JUDGE keeps its claim owned; competing O-JUDGE cannot win; continuation only under the same O-JUDGE via B9 episode); release rule paragraph; INV-26; T-45, T-46, T-47; T-43 extended |
| — | Whole-candidate sweep | Every "released or superseded permits a new O-JUDGE" phrasing corrected; §7.2 and §13.5 reason cells corrected so release is a consequence of the terminal, never its cause |

**Prior correction map (v1.5 → v1.6), retained for provenance:**

| # | v1.5 audit correction | Where applied |
|---|---|---|
| 1 | Pre-receipt crash and receipt-write failure | §7.12 A items 7, 7a (token gone after restart; never reconstructed/reused; O-JUDGE `judgment_authorization_failed`; claim released via linked record; new flow + new token; no BAI event backfilled; receipt-write failure terminal for the token); CR-31, CR-35; T-34, T-38; O-JUDGE terminals (§7.2); §13.5 logs |
| 2 | Judgment-authorization claim fully defined | §7.13 record contract (identity, fields, scope uniqueness, one winner, only attached token consumed, grants nothing, replacement rule, no replacement after a receipt, duplicate absorb/refuse, contradiction → indeterminate, ownership, lifecycle, recovery, logging); no new decision slot |
| 3 | Protected-boundary wording | §7.12 protocol paragraph (three linked stages, not one atomic transaction; O-APPEND only commits E9+E16); EB-8 rewritten; §7.12 A item 2 ordering; recovery wording; traces |
| 4 | Fence for `consumed_pending_commit` | §7.13 fence rules; §7.12 A item 8; §13.5 two pending situations (CR-30 corrected); CR-37–CR-39; T-40–T-42 |
| 5 | Honest terminals and logs for new failure kinds | O-JUDGE `judgment_claim_lost` / `judgment_authorization_failed` (§7.2); §13.5 rows incl. canonical-vs-log statement; CR-36, CR-40; T-43 |
| 6 | Retained unchanged | D16 open; no authentication option; receipt as proof; SACL later expiry; E1 §7C only for benchmark; gold rules; CAS-3; O-APPEND identity/logging; M-C4; forks fail closed; all earlier protections |
| 7 | Traces and audits | T-34, T-35 rewritten; T-38–T-43; §21 |

**Prior correction map (v1.4 → v1.5), retained for provenance:**

| # | v1.4 audit correction | Where applied |
|---|---|---|
| 1 | D16 authority-proof lifecycle without choosing D16 | §7.12 (Options A, B, C: pre-judgment validity, consumption at the protected boundary via claim → flushed receipt → commit, E9 binds the receipt, `consumed` = success, one token one judgment, replay refused, crash before/after consumption, SACL event-time reference, later expiry never erases, invalid-at-time fails closed); E9 field (§5); §7.11 refusal row; EB-8; CR-28 corrected; CR-31–CR-34; T-32–T-37; §0 bullet; no new decision slot |
| 2 | E1 scoring-binding wording | E1 row (§5): judgment mode + governing rule per case; §7C mapping only for `benchmark_family`; gold = six rules + D2, no §7C; held-out = future policy only; T-31 re-run |
| 3 | O-APPEND operational logging | §13.5 log table (four O-APPEND logs; six O-JUDGE logs; no duplicates with B9/BAI); CR-30 pending-state statement |
| 4 | Valid v1.4 work retained unchanged | CAS-3, authority enforcement, D16 open, gold inside E12, B9 retry identities, M-C4, fork fail-closed, all v1.3 protections — untouched |
| 5 | Audits | §21 |

**Prior correction map (v1.3 → v1.4), retained for provenance:**

| # | v1.3 audit correction | Where applied |
|---|---|---|
| 1 | One authoritative current judgment per completed output | E9 fields and identity (§5); CAS-3 (§7.9); §7.11 chain/head rules; O-JUDGE terminals (§7.2); EB-8; idempotency (§7.8); E10 consumes heads (§5, §8.1); §8.2 unjudged; INV-22; CR-24–CR-29; fail-closed rows; T-28–T-30 |
| 2 | Judgment authority enforced mechanically | §2.10 sources (Master §25, Bundle 5, AIC); §3; E1 scoring bindings with judgment mode; E7 checker binding; §7.11 authority table; EB-8 refusals; INV-23; T-27; **new D16** (seventeen slots) |
| 3 | Gold scoring inside E12 | E5 binds suite kind + scoring rule; §4.2 epoch binds the gold rule for gold cells; §8.1 rule 5 per suite kind; §8.4 items 4 and 6a; INV-24; T-31 |
| 4 | B9 lost-race operation identity | O-APPEND (§6.1, §7.2); CAS-1 rewritten (§7.9); CR-12, CR-30; T-21; INV-25; technical vs non-retryable refusals |
| 5 | §0 wording | §0 bullets rewritten |
| 6 | M-C4 retained unchanged | §4.6 unchanged; §18 note |
| 7 | Audits re-run | §21 |

**Prior correction maps (v1.0→v1.1, v1.1→v1.2, v1.2→v1.3)** remain in the
preserved earlier versions.

---

## §23 — Self-audit and delivery

| Check | Result |
|---|---|
| Authority, index status, no adoption | Met |
| All cited accepted files byte-identical and not restated as replacements | Met |
| No trial count, tolerance, budget, benchmark case, held-out definition, role mapping, invalidity, disagreement, promotion policy, or authentication method chosen | Met |
| Judgment authority bound by reference to accepted Master §25; required proof left open (D16); fail closed | Met |
| Judgment fork resolution left open without broadening D10/D11 | Met |
| Any CRITICAL blocks B24 eligibility | Preserved |
| E11a/E11b narrow; E12 separate | Met |
| v3-B/v3-C not admitted | Met |
| No implementation | Met |

**Residual notes (non-blocking):** all names `[proposed]`; canonical form,
integrity algorithms, and CAS/ledger storage open. **Flagged for the
auditor:** (a) the `judgment_authorization_claim` (§7.13) follows accepted
B-INT-4 record 1 mechanically — same one-winner slot, same "grants no
authority" character, same released/superseded claim states versus a
`failed` operation terminal — and adds no decision; (b) O-JUDGE's
`judgment_authorization_failed` is the operation terminal for every
no-valid-receipt outcome, mirroring B-INT-4's operation `failed` while
`released`/`superseded` remain claim states, never operation states.

**v1.7 note:** `closed_after_breach` is a mechanical distinction between a
receipt-bearing closure and a no-receipt release, needed so that the
accepted "a consumed token is never replaced" rule holds under a head
breach; it defines no resolution policy for the breached chain (that stays
open, §20) and selects no D16 option.

**Created:** exactly one new file — this v1.7 candidate. **Changed:**
nothing. v1.0–v1.6, every accepted design (B-INT-4 included), authoritative
file, Master, map, index, code, store, seal, marker, runtime state, and Git
history are untouched; nothing was committed or implemented.

---

*`NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` — DESIGN
CANDIDATE — proposal only. A judgment-authorization claim following
accepted B-INT-4 by reference — one winner, grants nothing, fenced once a
durable receipt exists, closed non-replaceably after a head breach,
released only after its operation's durable non-success with positive
proof that no receipt exists, and owned by a pending operation until it
ends — with
the original token never reused after a crash or a failed receipt write and
no BAI event ever backfilled. Three separate result families; coverage that
must actually be run, completed, judged, passed, and measured; one
concurrency-safe current judgment head per output, bound to event-time
authority proof under whichever D16 option Ness chooses — a spent one-time
token's receipt being the proof, never a refusal; every run graded by its
own suite kind's rules with §7C categories confined to benchmark suites;
compare-and-append ledgers through single-terminal, singly-logged O-APPEND
operations with B9-governed retries under new operation IDs and honest
pending state on exhaustion; and seventeen open Ness decision slots plus one
visible fail-closed open item — with B16's absorbing promotion terminal and
every accepted file untouched. Awaiting ChatGPT's independent audit and
Ness's explicit acceptance.*
