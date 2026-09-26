# Chapter 3-d — Group A: C-READ, quarantine-to-production promotion

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-d.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `855459fc6674dfe3a1f310f3d1690a9e7db59405`

This piece continues C-READ after Chapter 3-c. It carries the complete per-reading B16 v1.0 promotion seam: identity, lifecycle, reservation/fence, nine-input evidence snapshot, eligibility commit, ten idempotency points, twenty recovery cases, ten fail-closed classes, operational logs and boundaries. Evaluation-result generation and its later applicability bridge, the connected full CY-G flow, and the remaining Group A components are not completed by this piece. No missing outside mechanism is invented here.

Authority order: V10 → Decision Defaults v2_2 → cursorrules → Companion v1; the Working Map is subordinate. B16 behavior is ACCEPTED through its exact-source acceptance receipt; this is not a build claim. The governing V10 living-record rule is DESIGNED. No new B16 mechanism is stamped BUILT. The corrected Chapter 3-b and completed Chapter 3-c remain separate files; joining pieces concatenates their text without editing or merging cards.

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`. NHD-B16 is a navigation identifier; the cited source sections supply behavior.

Template convention: record-member and rule cards describe their containing record/operation, not separate services. Fed by / USED BY pairs record containment or stated operation relationships; Gated by names an actual decided constraint. All B16 names marked proposed in the source remain proposed names; none selects a serialization, algorithm, physical store, threshold or implementation. Repeated event words are qualified as state, phase or operation-log uses so these distinct source concepts are not silently merged.

<!-- BEGIN CHAPTER 3-d BEHAVIOR -->

### C-READ.11 — Quarantine-to-production promotion seam
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [NHD-B16]

ALONE
- What it is: ACCEPTED — The per-reading mechanical promotion boundary: it derives usability from verified recorded evidence without interpreting the reading or rewriting it. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [NHD-B16]
- Takes in: ACCEPTED — A quarantined reading identity, a promotion request, its permanent claim and attempt identities, the required evidence, production protections, privacy authorization and hold/dependency status. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Does: ACCEPTED — Looks up prior state, admits at most one reservation, verifies and freezes the complete evidence snapshot, wins and rechecks the commit fence, commits at most one production-eligibility record, and records the parent outcome before acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — A derived committed, duplicate-absorbed, rejected, interrupted, held or indeterminate outcome with its traceable records; the reading stays in place. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Interpret or score content, decide what passes, create or write a production store, mutate roots/readings, bypass privacy, duplicate promotion, or let quarantine silently influence production. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Fails closed by: ACCEPTED — Withholds commit and production influence on missing, failed, unauthorized, unreadable or contradictory evidence; no partial pass, guessed state or false success. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.4 — Quarantine readings destination: Supplies the quarantined reading by identity, without moving or rewriting it. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.1 — Promotion reading identity: Binds permanent reading identity, store-unique operation key, complete-record integrity and read-only root existence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.2 — promotion_claim: Establishes one deterministic claim before any eligibility record; every later attempt uses this same claim and checks its bound reading integrity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.3 — Promotion operation identities: Assigns an attempt-specific parent identity; each child uses a stable unique child identity referencing that parent. Recovery uses recovery_run_id with lookup-first action identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.4 — Derived promotion lifecycle: Derives the current state without adding a mutable status field to the reading; only the complete committed trail makes the reading production-eligible. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.6 — Promotion reservation phases and legal transitions: Compares and commits on the same authoritative phase; exactly one fence/release action wins. A durable fence excludes ordinary release and second reservation; terminal release permanently excludes commit for that reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.5 — Promotion transaction boundaries: Orders lookup → reservation → evidence-snapshot commit → fenced eligibility commit → parent terminal before acknowledgement; rebuildable post-commit material is independent of success. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.7 — promotion_evidence_snapshot: Verifies presence, integrity, authorization and binding, never evidence content; freezes the complete reference set so B16-3 cannot swap checked evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.5.4.1 — production_eligibility_record: Appends once at B16-3; only a valid complete claim/snapshot/eligibility trail derives promotion_committed. It never moves or copies the quarantined reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.8 — Promotion idempotency points: Uses each boundary’s own identity and authoritative compare-and-commit or lookup-first result; an attempt identity never replaces the permanent claim. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.9 — Production-consumption gate: Admits a reading only when the complete validated trail proves promotion_committed; requested, reserved, evidence-checked, rejected, held, interrupted and indeterminate candidates are excluded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10 — Promotion recovery matrix: Inspects committed events first; resolves by append-only actions under the same permanent claim; never changes the quarantined reading, roots or committed evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.11 — Promotion fail-closed conditions: Applies the source-defined outcome per failure class and records the named condition; missing inputs never produce a partial pass. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12 — Promotion operation records: Logs each real operation once under its own identity. Canonical claim events, phase events, snapshots and eligibility records establish machine state but are not additional §0B logs. B16-4 is the sole parent terminal; no log-about-logging chain is generated. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.13 — Promotion boundaries: Keeps mechanical state/evidence checks separate from semantic judgment; respects privacy/access order; preserves root/reading and quarantine/production separation; never exposes sealed TSC contents. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Gated by: ACCEPTED — C-READ.5 — Production readings authorization: Both production protections are mandatory; marker presence alone never authorizes promotion. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Gated by: ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): Internal-use authorization and privacy restrictions apply before relevance; unauthorized operations fail closed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Gated by: ACCEPTED — C-SACL — Speaker Access-Control Layer (§25.4): Applicable identity/access scope must permit the operation; refusal cannot be bypassed or retried around. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.5 — Promotion transaction boundaries: Each required boundary must complete in order before promotion can acknowledge success. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Changes: ACCEPTED — C-READ.11.9 — Production-consumption gate: Changes only derived production-use eligibility after a valid commit; all other outcomes keep the reading excluded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ — Reading record, validator, writer (§6B) / CY-G | A quarantined reading proposed for production use. | Applies the per-reading promotion seam and records its derived eligibility. | Only a validated committed promotion can pass production consumption; the reading itself is unchanged. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |

SUB-PARTS: C-READ.11.1 — Promotion reading identity; C-READ.11.2 — promotion_claim; C-READ.11.3 — Promotion operation identities; C-READ.11.4 — Derived promotion lifecycle; C-READ.11.5 — Promotion transaction boundaries; C-READ.11.6 — Promotion reservation phases and legal transitions; C-READ.11.7 — promotion_evidence_snapshot; C-READ.11.8 — Promotion idempotency points; C-READ.11.9 — Production-consumption gate; C-READ.11.10 — Promotion recovery matrix; C-READ.11.11 — Promotion fail-closed conditions; C-READ.11.12 — Promotion operation records; C-READ.11.13 — Promotion boundaries

### C-READ.11.1 — Promotion reading identity
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]

ALONE
- What it is: ACCEPTED — The immutable identity and integrity context of the reading under consideration. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Takes in: ACCEPTED — The stored quarantined reading and its reads list. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Does: ACCEPTED — Binds permanent reading identity, store-unique operation key, complete-record integrity and read-only root existence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Gives out: ACCEPTED — Identity evidence matched to the claim. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Must never: ACCEPTED — Copy or change root/reading content, invent a replacement reading, or confuse operation identity with reading identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Fails closed by: ACCEPTED — Missing or unreadable reading makes recovery indeterminate; unverifiable root identity rejects the attempt or leaves verification indeterminate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.1.1 — reading_id: Identifies the one reading to which this claim and every promotion attempt apply. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.1.2 — reading_idempotency_key: Carries corroborating identity evidence separately from the permanent reading id. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.1.3 — reading_integrity_ref: Detects damaged, swapped or altered reading bytes and must match the claim-bound value. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.1.4 — reads identity verification: Verifies existence by identity in its sealed or B11-governed owning batch, read-only; it consumes no root content. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: This operation and its records remain subject to internal-use authorization, privacy visibility and applicable SACL scope. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11 — Quarantine-to-production promotion seam | The stored quarantined reading and its reads list. | Binds permanent reading identity, store-unique operation key, complete-record integrity and read-only root existence. | Identity evidence matched to the claim. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16] |

SUB-PARTS: C-READ.11.1.1 — reading_id; C-READ.11.1.2 — reading_idempotency_key; C-READ.11.1.3 — reading_integrity_ref; C-READ.11.1.4 — reads identity verification

### C-READ.11.1.1 — reading_id
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]

ALONE
- What it is: ACCEPTED — The reading_id member of Promotion reading identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Takes in: ACCEPTED — The reading’s permanent id, unchanged across locations and lifecycle states. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Does: ACCEPTED — Identifies the one reading to which this claim and every promotion attempt apply. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Gives out: ACCEPTED — The reading’s permanent id, unchanged across locations and lifecycle states. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Must never: ACCEPTED — Give the same reading a second identity on promotion. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Fails closed by: ACCEPTED — Cannot establish valid promotion evidence when this required identity/integrity reference is missing, unreadable or inconsistent; no substitute is reconstructed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.7.1 — Reading identity and integrity: This required reference must verify before the snapshot can commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.1 — Promotion reading identity | The reading’s permanent id, unchanged across locations and lifecycle states. | Identifies the one reading to which this claim and every promotion attempt apply. | The reading’s permanent id, unchanged across locations and lifecycle states. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.1.2 — reading_idempotency_key
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]

ALONE
- What it is: ACCEPTED — The reading_idempotency_key member of Promotion reading identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Takes in: ACCEPTED — The reading’s store-unique operation key. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Does: ACCEPTED — Carries corroborating identity evidence separately from the permanent reading id. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Gives out: ACCEPTED — The reading’s store-unique operation key. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Must never: ACCEPTED — Use the operation key as a replacement for the permanent reading id. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Fails closed by: ACCEPTED — Cannot establish valid promotion evidence when this required identity/integrity reference is missing, unreadable or inconsistent; no substitute is reconstructed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.7.1 — Reading identity and integrity: This required reference must verify before the snapshot can commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.1 — Promotion reading identity | The reading’s store-unique operation key. | Carries corroborating identity evidence separately from the permanent reading id. | The reading’s store-unique operation key. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.1.3 — reading_integrity_ref
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]

ALONE
- What it is: ACCEPTED — The reading_integrity_ref member of Promotion reading identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Takes in: ACCEPTED — An external integrity reference over the complete immutable reading as stored in quarantine; proposed name. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Does: ACCEPTED — Detects damaged, swapped or altered reading bytes and must match the claim-bound value. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gives out: ACCEPTED — An external integrity reference over the complete immutable reading as stored in quarantine; proposed name. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Must never: ACCEPTED — Insert a new integrity field into the immutable reading or accept changed bytes as the same bound record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Fails closed by: ACCEPTED — Cannot establish valid promotion evidence when this required identity/integrity reference is missing, unreadable or inconsistent; no substitute is reconstructed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.7.1 — Reading identity and integrity: This required reference must verify before the snapshot can commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.1 — Promotion reading identity | An external integrity reference over the complete immutable reading as stored in quarantine; proposed name. | Detects damaged, swapped or altered reading bytes and must match the claim-bound value. | An external integrity reference over the complete immutable reading as stored in quarantine; proposed name. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.1.4 — reads identity verification
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]

ALONE
- What it is: ACCEPTED — The reads identity verification member of Promotion reading identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Takes in: ACCEPTED — Every root id in the existing reads list. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Does: ACCEPTED — Verifies existence by identity in its sealed or B11-governed owning batch, read-only; it consumes no root content. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Gives out: ACCEPTED — Every root id in the existing reads list. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Must never: ACCEPTED — Create, repair, guess, change or read root content through this identity-only check. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16]
- Fails closed by: ACCEPTED — Cannot establish valid promotion evidence when this required identity/integrity reference is missing, unreadable or inconsistent; no substitute is reconstructed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.7.2 — Read-only root references: This required reference must verify before the snapshot can commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.1 — Promotion reading identity | Every root id in the existing reads list. | Verifies existence by identity in its sealed or B11-governed owning batch, read-only; it consumes no root content. | Every root id in the existing reads list. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.2 — promotion_claim
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — One permanent promotion claim per reading_id; the source’s record and field names are proposed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Takes in: ACCEPTED — reading_id, the single promotion operation type and the reading integrity reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Does: ACCEPTED — Establishes one deterministic claim before any eligibility record; every later attempt uses this same claim and checks its bound reading integrity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Gives out: ACCEPTED — A canonical claim with append-only status/reservation events and later bound snapshot/committed references. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Must never: ACCEPTED — Create a second claim for the same reading, edit claim history or swap its bound integrity reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Fails closed by: ACCEPTED — Unreadable or contradictory claim evidence makes derived status unprovable and blocks reservation, commit and production consumption. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.2.1 — promotion_claim_key: Converges all attempts for the reading on the same permanent claim. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.2.2 — reading_integrity_ref: Every later attempt is checked against this exact bound value. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.2.3 — claim_status_events: Derives effective promotion state from the preserved event history; it never mutates reading fields. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.2.4 — reservation_events: Carries the single-winner reservation and its legal phase transitions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.2.5 — evidence_snapshot_ref: Points to the immutable snapshot for the reservation; checked evidence cannot be swapped afterward. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.2.6 — production_eligibility_ref / committed refs: Names the one committed eligibility record and its complete trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: This operation and its records remain subject to internal-use authorization, privacy visibility and applicable SACL scope. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11 — Quarantine-to-production promotion seam | reading_id, the single promotion operation type and the reading integrity reference. | Establishes one deterministic claim before any eligibility record; every later attempt uses this same claim and checks its bound reading integrity. | A canonical claim with append-only status/reservation events and later bound snapshot/committed references. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.5.1 — B16-0 — Promotion-status lookup | reading_id, the single promotion operation type and the reading integrity reference. | Looks up this permanent claim’s derived status before any reservation. | A canonical claim with append-only status/reservation events and later bound snapshot/committed references. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.8.1 — Promotion claim duplicate prevention | reading_id, the single promotion operation type and the reading integrity reference. | The source-defined permanent or operation identity and its existing committed result determine whether this action may create a new record. | A canonical claim with append-only status/reservation events and later bound snapshot/committed references. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.10.8 — Recovery 8 — Promotion rejected | reading_id, the single promotion operation type and the reading integrity reference. | Any later policy-permitted request uses the same permanent claim and its recorded history. | A canonical claim with append-only status/reservation events and later bound snapshot/committed references. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 5 · ACCEPTED | C-READ.11.10.6.3 — Rejected or held history | reading_id, the single promotion operation type and the reading integrity reference. | Rejected/held history remains on the one permanent claim and cannot be bypassed by a second claim. | A canonical claim with append-only status/reservation events and later bound snapshot/committed references. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: C-READ.11.2.1 — promotion_claim_key; C-READ.11.2.2 — reading_integrity_ref; C-READ.11.2.3 — claim_status_events; C-READ.11.2.4 — reservation_events; C-READ.11.2.5 — evidence_snapshot_ref; C-READ.11.2.6 — production_eligibility_ref / committed refs

### C-READ.11.2.1 — promotion_claim_key
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_claim_key member of promotion_claim. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Takes in: ACCEPTED — Immutable deterministic reading_id + the single promotion operation type. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Does: ACCEPTED — Converges all attempts for the reading on the same permanent claim. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Gives out: ACCEPTED — Immutable deterministic reading_id + the single promotion operation type. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Must never: ACCEPTED — Rewrite the bound member or its prior events, duplicate its identity, or replace its committed reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Fails closed by: ACCEPTED — Unprovable or inconsistent binding prevents a valid committed trail and leaves production consumption excluded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.9.1 — Complete committed-trail requirement: The preserved binding must participate in the complete validated claim/snapshot/eligibility trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.2 — promotion_claim | Immutable deterministic reading_id + the single promotion operation type. | Converges all attempts for the reading on the same permanent claim. | Immutable deterministic reading_id + the single promotion operation type. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.2.2 — reading_integrity_ref
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The reading_integrity_ref member of promotion_claim. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Takes in: ACCEPTED — The integrity reference bound at claim establishment. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Does: ACCEPTED — Every later attempt is checked against this exact bound value. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Gives out: ACCEPTED — The integrity reference bound at claim establishment. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Must never: ACCEPTED — Rewrite the bound member or its prior events, duplicate its identity, or replace its committed reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Fails closed by: ACCEPTED — Unprovable or inconsistent binding prevents a valid committed trail and leaves production consumption excluded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.9.1 — Complete committed-trail requirement: The preserved binding must participate in the complete validated claim/snapshot/eligibility trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.2 — promotion_claim | The integrity reference bound at claim establishment. | Every later attempt is checked against this exact bound value. | The integrity reference bound at claim establishment. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.2.3 — claim_status_events
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The claim_status_events member of promotion_claim. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Takes in: ACCEPTED — Append-only status events. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Does: ACCEPTED — Derives effective promotion state from the preserved event history; it never mutates reading fields. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Gives out: ACCEPTED — Append-only status events. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Must never: ACCEPTED — Rewrite the bound member or its prior events, duplicate its identity, or replace its committed reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Fails closed by: ACCEPTED — Unprovable or inconsistent binding prevents a valid committed trail and leaves production consumption excluded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.9.1 — Complete committed-trail requirement: The preserved binding must participate in the complete validated claim/snapshot/eligibility trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.2 — promotion_claim | Append-only status events. | Derives effective promotion state from the preserved event history; it never mutates reading fields. | Append-only status events. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.2.4 — reservation_events
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The reservation_events member of promotion_claim. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Takes in: ACCEPTED — Append-only reservation and phase events. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Does: ACCEPTED — Carries the single-winner reservation and its legal phase transitions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Gives out: ACCEPTED — Append-only reservation and phase events. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Must never: ACCEPTED — Rewrite the bound member or its prior events, duplicate its identity, or replace its committed reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Fails closed by: ACCEPTED — Unprovable or inconsistent binding prevents a valid committed trail and leaves production consumption excluded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.9.1 — Complete committed-trail requirement: The preserved binding must participate in the complete validated claim/snapshot/eligibility trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.2 — promotion_claim | Append-only reservation and phase events. | Carries the single-winner reservation and its legal phase transitions. | Append-only reservation and phase events. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.2.5 — evidence_snapshot_ref
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The evidence_snapshot_ref member of promotion_claim. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Takes in: ACCEPTED — Reference bound when B16-2 commits. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Does: ACCEPTED — Points to the immutable snapshot for the reservation; checked evidence cannot be swapped afterward. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gives out: ACCEPTED — Reference bound when B16-2 commits. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Must never: ACCEPTED — Rewrite the bound member or its prior events, duplicate its identity, or replace its committed reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Fails closed by: ACCEPTED — Unprovable or inconsistent binding prevents a valid committed trail and leaves production consumption excluded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.9.1 — Complete committed-trail requirement: The preserved binding must participate in the complete validated claim/snapshot/eligibility trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.2 — promotion_claim | Reference bound when B16-2 commits. | Points to the immutable snapshot for the reservation; checked evidence cannot be swapped afterward. | Reference bound when B16-2 commits. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.2.6 — production_eligibility_ref / committed refs
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The production_eligibility_ref / committed refs member of promotion_claim. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Takes in: ACCEPTED — References bound once at the terminal committed transition. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Does: ACCEPTED — Names the one committed eligibility record and its complete trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Gives out: ACCEPTED — References bound once at the terminal committed transition. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Must never: ACCEPTED — Rewrite the bound member or its prior events, duplicate its identity, or replace its committed reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16]
- Fails closed by: ACCEPTED — Unprovable or inconsistent binding prevents a valid committed trail and leaves production consumption excluded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.9.1 — Complete committed-trail requirement: The preserved binding must participate in the complete validated claim/snapshot/eligibility trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.2 — promotion_claim | References bound once at the terminal committed transition. | Names the one committed eligibility record and its complete trail. | References bound once at the terminal committed transition. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.3 — Promotion operation identities
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16]

ALONE
- What it is: ACCEPTED — Separate identities for the caller invocation and each real internal operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Takes in: ACCEPTED — One promotion invocation, its permanent claim, and separately executed internal operations. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Does: ACCEPTED — Assigns an attempt-specific parent identity; each child uses a stable unique child identity referencing that parent. Recovery uses recovery_run_id with lookup-first action identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Gives out: ACCEPTED — Traceable identities for one parent log and one log per child. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Must never: ACCEPTED — Use an attempt id as the duplicate-prevention claim, reuse the parent id as a child id, or log twice under one operation id. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fails closed by: ACCEPTED — A retry finds an existing operation log by identity and does not append a second log. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.3.1 — promotion_operation_id: Identifies one invocation, never the permanent claim or a child operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.3.2 — promotion_child_op_id: Identifies each genuinely separate lookup/establishment, reservation, evidence check, commit, release/cancellation or recovery resolution. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: Repeated recovery returns committed findings without duplicate release, terminal or re-execution. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.8 — Promotion idempotency points: The operation/claim identities retain their stated uniqueness and separation; an existing log or recovery result is reused, never duplicated. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11 — Quarantine-to-production promotion seam | One promotion invocation, its permanent claim, and separately executed internal operations. | Assigns an attempt-specific parent identity; each child uses a stable unique child identity referencing that parent. Recovery uses recovery_run_id with lookup-first action identity. | Traceable identities for one parent log and one log per child. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |

SUB-PARTS: C-READ.11.3.1 — promotion_operation_id; C-READ.11.3.2 — promotion_child_op_id; C-READ.11.3.3 — recovery_run_id

### C-READ.11.3.1 — promotion_operation_id
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_operation_id member of Promotion operation identities. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Takes in: ACCEPTED — Attempt-specific parent invocation identity; proposed name. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Does: ACCEPTED — Identifies one invocation, never the permanent claim or a child operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Gives out: ACCEPTED — Attempt-specific parent invocation identity; proposed name. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Must never: ACCEPTED — Use this parent id for child logs or duplicate-prevention across attempts. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fails closed by: ACCEPTED — An existing terminal under this parent id is returned without writing a second terminal. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.8.8 — Parent terminal log (B16-4) duplicate prevention: The operation/claim identities retain their stated uniqueness and separation; an existing log or recovery result is reused, never duplicated. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.3 — Promotion operation identities | Attempt-specific parent invocation identity; proposed name. | Identifies one invocation, never the permanent claim or a child operation. | Attempt-specific parent invocation identity; proposed name. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.5.5 — B16-4 — Parent terminal log commit | Attempt-specific parent invocation identity; proposed name. | Uses the parent operation identity for exactly one terminal record. | Attempt-specific parent invocation identity; proposed name. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.3.2 — promotion_child_op_id
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_child_op_id member of Promotion operation identities. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Takes in: ACCEPTED — Stable unique child operation identity referencing the parent; proposed name. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Does: ACCEPTED — Identifies each genuinely separate lookup/establishment, reservation, evidence check, commit, release/cancellation or recovery resolution. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Gives out: ACCEPTED — Stable unique child operation identity referencing the parent; proposed name. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Must never: ACCEPTED — Reuse the parent id as the child id or give one child two operational logs. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fails closed by: ACCEPTED — Retries locate the existing child log by identity and reuse its recorded outcome. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.8.9 — Child-operation log duplicate prevention: The operation/claim identities retain their stated uniqueness and separation; an existing log or recovery result is reused, never duplicated. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.3 — Promotion operation identities | Stable unique child operation identity referencing the parent; proposed name. | Identifies each genuinely separate lookup/establishment, reservation, evidence check, commit, release/cancellation or recovery resolution. | Stable unique child operation identity referencing the parent; proposed name. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.5.1 — B16-0 — Promotion-status lookup | Stable unique child operation identity referencing the parent; proposed name. | Uses its own stable child operation identity referencing the parent. | Stable unique child operation identity referencing the parent; proposed name. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.5.2 — B16-1 — Atomic promotion reservation | Stable unique child operation identity referencing the parent; proposed name. | Uses its own stable child operation identity referencing the parent. | Stable unique child operation identity referencing the parent; proposed name. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.5.3 — B16-2 — Evidence-snapshot verification commit | Stable unique child operation identity referencing the parent; proposed name. | Uses its own stable child operation identity referencing the parent. | Stable unique child operation identity referencing the parent; proposed name. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |
| 5 · ACCEPTED | C-READ.11.5.4 — B16-3 — Production-eligibility commit | Stable unique child operation identity referencing the parent; proposed name. | Uses its own stable child operation identity referencing the parent. | Stable unique child operation identity referencing the parent; proposed name. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |
| 6 · ACCEPTED | C-READ.11.5.6 — B16-PR — Post-commit indexes and coverage | Stable unique child operation identity referencing the parent; proposed name. | Uses its own stable child operation identity referencing the parent. | Stable unique child operation identity referencing the parent; proposed name. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |
| 7 · ACCEPTED | C-READ.11.8.9 — Child-operation log duplicate prevention | Stable unique child operation identity referencing the parent; proposed name. | The source-defined permanent or operation identity and its existing committed result determine whether this action may create a new record. | Stable unique child operation identity referencing the parent; proposed name. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.3.3 — recovery_run_id
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

ALONE
- What it is: ACCEPTED — The recovery_run_id member of Promotion operation identities. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Takes in: ACCEPTED — Recovery-run identity with per-action lookup-first checks. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Does: ACCEPTED — Repeated recovery returns committed findings without duplicate release, terminal or re-execution. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Gives out: ACCEPTED — Recovery-run identity with per-action lookup-first checks. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Must never: ACCEPTED — Create a second resolution for the same completed recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fails closed by: ACCEPTED — An already resolved action is a no-op returning the committed finding. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.8.10 — Recovery run duplicate prevention: The operation/claim identities retain their stated uniqueness and separation; an existing log or recovery result is reused, never duplicated. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.3 — Promotion operation identities | Recovery-run identity with per-action lookup-first checks. | Repeated recovery returns committed findings without duplicate release, terminal or re-execution. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.10.1 — Recovery 1 — Crash before any promotion claim/request exists | Recovery-run identity with per-action lookup-first checks. | Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.10.2 — Recovery 2 — Claim/request durable, evidence check absent (reservation may or may not exist) | Recovery-run identity with per-action lookup-first checks. | Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.10.3 — Recovery 3 — Evidence snapshot committed, production commit absent | Recovery-run identity with per-action lookup-first checks. | Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 5 · ACCEPTED | C-READ.11.10.4 — Recovery 4 — Production-eligibility record present, parent terminal log absent | Recovery-run identity with per-action lookup-first checks. | Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 6 · ACCEPTED | C-READ.11.10.5 — Recovery 5 — Terminal log present, acknowledgement absent | Recovery-run identity with per-action lookup-first checks. | Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 7 · ACCEPTED | C-READ.11.10.6 — Recovery 6 — Duplicate promotion attempt (same reading, any time) | Recovery-run identity with per-action lookup-first checks. | Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 8 · ACCEPTED | C-READ.11.10.7 — Recovery 7 — Conflicting promotion attempts (race) | Recovery-run identity with per-action lookup-first checks. | Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 9 · ACCEPTED | C-READ.11.10.8 — Recovery 8 — Promotion rejected | Recovery-run identity with per-action lookup-first checks. | Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 10 · ACCEPTED | C-READ.11.10.9 — Recovery 9 — Promotion held / dependency-blocked | Recovery-run identity with per-action lookup-first checks. | Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 11 · ACCEPTED | C-READ.11.10.10 — Recovery 10 — Quarantined reading missing or unreadable | Recovery-run identity with per-action lookup-first checks. | Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 12 · ACCEPTED | C-READ.11.10.11 — Recovery 11 — Root reference missing or unreadable (a reads id cannot be verified) | Recovery-run identity with per-action lookup-first checks. | Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 13 · ACCEPTED | C-READ.11.10.12 — Recovery 12 — B24 acceptance evidence (gold-set / held-out results) missing or failed | Recovery-run identity with per-action lookup-first checks. | Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 14 · ACCEPTED | C-READ.11.10.13 — Recovery 13 — Contradictory evidence (any two bound inputs disagree; snapshot integrity mismatch) | Recovery-run identity with per-action lookup-first checks. | Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 15 · ACCEPTED | C-READ.11.10.14 — Recovery 14 — Privacy/access block | Recovery-run identity with per-action lookup-first checks. | Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 16 · ACCEPTED | C-READ.11.10.15 — Recovery 15 — Production-eligibility record present without complete promotion evidence (orphan) | Recovery-run identity with per-action lookup-first checks. | Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 17 · ACCEPTED | C-READ.11.10.16 — Recovery 16 — Promotion evidence present without a production record (snapshot committed, no eligibility record) | Recovery-run identity with per-action lookup-first checks. | Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 18 · ACCEPTED | C-READ.11.10.17 — Recovery 17 — Post-commit index/coverage incomplete (B16-PR) | Recovery-run identity with per-action lookup-first checks. | Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 19 · ACCEPTED | C-READ.11.10.18 — Recovery 18 — Duplicate recovery run | Recovery-run identity with per-action lookup-first checks. | Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 20 · ACCEPTED | C-READ.11.10.19 — Recovery 19 — Attempted promotion of an already production-committed reading | Recovery-run identity with per-action lookup-first checks. | Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 21 · ACCEPTED | C-READ.11.10.20 — Recovery 20 — Attempted use of a quarantined reading before promotion | Recovery-run identity with per-action lookup-first checks. | Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 22 · ACCEPTED | C-READ.11.8.10 — Recovery run duplicate prevention | Recovery-run identity with per-action lookup-first checks. | The source-defined permanent or operation identity and its existing committed result determine whether this action may create a new record. | Recovery-run identity with per-action lookup-first checks. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.4 — Derived promotion lifecycle
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]

ALONE
- What it is: ACCEPTED — Nine effective lifecycle states derived from the claim’s append-only events. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Takes in: ACCEPTED — The claim, reservation, evidence snapshot and validated committed eligibility trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Does: ACCEPTED — Derives the current state without adding a mutable status field to the reading; only the complete committed trail makes the reading production-eligible. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Gives out: ACCEPTED — One of quarantined, promotion_requested, promotion_reserved, promotion_evidence_checked, promotion_committed, promotion_rejected, dependency_blocked_held, promotion_interrupted, indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Must never: ACCEPTED — Treat waiting, requested/reserved/evidence-checked status or an orphan record as production commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Fails closed by: ACCEPTED — Unprovable status is indeterminate and excluded from production; rejected and held attempts stay quarantined. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.4.1 — quarantined: Baseline. The reading exists in quarantine with no committed promotion. Not a B16-created record — it is the derived absence of one. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.4.2 — promotion_requested: A durable promotion request event exists for the claim; no reservation, no rights, no production effect. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.4.3 — promotion_reserved: Exactly one live reservation exists. No production effect. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.4.4 — promotion_evidence_checked: The immutable evidence snapshot is committed and bound to the claim and reservation. Still no production effect. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.4.5 — promotion_committed: Terminal, absorbing, idempotent success: the production-eligibility record exists with its complete matching trail. Repeats return duplicate_absorbed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.4.6 — promotion_rejected: Attempt-terminal with recorded cause (evidence failure, decision refusal, integrity conflict). The reading remains quarantined and never becomes production through this attempt. Whether and when a new attempt is permitted is policy owned elsewhere (A29 / B9, §12); mechanically, a later attempt is a new request under the same permanent claim, lookup-first over the recorded history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.4.7 — dependency_blocked_held: Non-terminal waiting: a required dependency (hold condition, missing authorization, A29-gated readiness) blocks progress. Fail-closed: a held candidate never becomes production by waiting. Hold lifecycle, release mechanics, and release policy are B-HOLD / A29 — B16 defines only this fail-closed waiting semantic and the recorded blocked event. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.4.8 — promotion_interrupted: The attempt ended before B16-3 with durable evidence of non-commit (crash, lost race, released reservation). Safe technical re-attempt under the same claim; substantive retry policy remains B9's. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.4.9 — indeterminate_recovery_required: Evidence unreadable or contradictory. No reservation, no commit, no production effect; resolution only through §8 — never by guessing. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.9.1 — Complete committed-trail requirement: Only the complete validated committed trail can establish promotion_committed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11 — Quarantine-to-production promotion seam | The claim, reservation, evidence snapshot and validated committed eligibility trail. | Derives the current state without adding a mutable status field to the reading; only the complete committed trail makes the reading production-eligible. | One of quarantined, promotion_requested, promotion_reserved, promotion_evidence_checked, promotion_committed, promotion_rejected, dependency_blocked_held, promotion_interrupted, indeterminate_recovery_required. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.4.1 — quarantined | The claim, reservation, evidence snapshot and validated committed eligibility trail. | This state is derived from the claim’s preserved append-only events, never a mutable field on the reading. | One of quarantined, promotion_requested, promotion_reserved, promotion_evidence_checked, promotion_committed, promotion_rejected, dependency_blocked_held, promotion_interrupted, indeterminate_recovery_required. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.4.2 — promotion_requested | The claim, reservation, evidence snapshot and validated committed eligibility trail. | This state is derived from the claim’s preserved append-only events, never a mutable field on the reading. | One of quarantined, promotion_requested, promotion_reserved, promotion_evidence_checked, promotion_committed, promotion_rejected, dependency_blocked_held, promotion_interrupted, indeterminate_recovery_required. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.4.3 — promotion_reserved | The claim, reservation, evidence snapshot and validated committed eligibility trail. | This state is derived from the claim’s preserved append-only events, never a mutable field on the reading. | One of quarantined, promotion_requested, promotion_reserved, promotion_evidence_checked, promotion_committed, promotion_rejected, dependency_blocked_held, promotion_interrupted, indeterminate_recovery_required. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] |
| 5 · ACCEPTED | C-READ.11.4.4 — promotion_evidence_checked | The claim, reservation, evidence snapshot and validated committed eligibility trail. | This state is derived from the claim’s preserved append-only events, never a mutable field on the reading. | One of quarantined, promotion_requested, promotion_reserved, promotion_evidence_checked, promotion_committed, promotion_rejected, dependency_blocked_held, promotion_interrupted, indeterminate_recovery_required. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] |
| 6 · ACCEPTED | C-READ.11.4.5 — promotion_committed | The claim, reservation, evidence snapshot and validated committed eligibility trail. | This state is derived from the claim’s preserved append-only events, never a mutable field on the reading. | One of quarantined, promotion_requested, promotion_reserved, promotion_evidence_checked, promotion_committed, promotion_rejected, dependency_blocked_held, promotion_interrupted, indeterminate_recovery_required. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] |
| 7 · ACCEPTED | C-READ.11.4.6 — promotion_rejected | The claim, reservation, evidence snapshot and validated committed eligibility trail. | This state is derived from the claim’s preserved append-only events, never a mutable field on the reading. | One of quarantined, promotion_requested, promotion_reserved, promotion_evidence_checked, promotion_committed, promotion_rejected, dependency_blocked_held, promotion_interrupted, indeterminate_recovery_required. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] |
| 8 · ACCEPTED | C-READ.11.4.7 — dependency_blocked_held | The claim, reservation, evidence snapshot and validated committed eligibility trail. | This state is derived from the claim’s preserved append-only events, never a mutable field on the reading. | One of quarantined, promotion_requested, promotion_reserved, promotion_evidence_checked, promotion_committed, promotion_rejected, dependency_blocked_held, promotion_interrupted, indeterminate_recovery_required. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] |
| 9 · ACCEPTED | C-READ.11.4.8 — promotion_interrupted | The claim, reservation, evidence snapshot and validated committed eligibility trail. | This state is derived from the claim’s preserved append-only events, never a mutable field on the reading. | One of quarantined, promotion_requested, promotion_reserved, promotion_evidence_checked, promotion_committed, promotion_rejected, dependency_blocked_held, promotion_interrupted, indeterminate_recovery_required. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] |
| 10 · ACCEPTED | C-READ.11.4.9 — indeterminate_recovery_required | The claim, reservation, evidence snapshot and validated committed eligibility trail. | This state is derived from the claim’s preserved append-only events, never a mutable field on the reading. | One of quarantined, promotion_requested, promotion_reserved, promotion_evidence_checked, promotion_committed, promotion_rejected, dependency_blocked_held, promotion_interrupted, indeterminate_recovery_required. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] |
| 11 · ACCEPTED | C-READ.11.5.1 — B16-0 — Promotion-status lookup | The claim, reservation, evidence snapshot and validated committed eligibility trail. | Claim-derived status must be provable; unreadable events yield indeterminate_recovery_required before any reservation. | One of quarantined, promotion_requested, promotion_reserved, promotion_evidence_checked, promotion_committed, promotion_rejected, dependency_blocked_held, promotion_interrupted, indeterminate_recovery_required. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 12 · ACCEPTED | C-READ.11.9.2 — Non-committed states excluded | The claim, reservation, evidence snapshot and validated committed eligibility trail. | The claim-derived non-committed state excludes the reading from production use. | One of quarantined, promotion_requested, promotion_reserved, promotion_evidence_checked, promotion_committed, promotion_rejected, dependency_blocked_held, promotion_interrupted, indeterminate_recovery_required. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |

SUB-PARTS: C-READ.11.4.1 — quarantined; C-READ.11.4.2 — promotion_requested; C-READ.11.4.3 — promotion_reserved; C-READ.11.4.4 — promotion_evidence_checked; C-READ.11.4.5 — promotion_committed; C-READ.11.4.6 — promotion_rejected; C-READ.11.4.7 — dependency_blocked_held; C-READ.11.4.8 — promotion_interrupted; C-READ.11.4.9 — indeterminate_recovery_required

### C-READ.11.4.1 — quarantined
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]

ALONE
- What it is: ACCEPTED — The quarantined derived promotion state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Takes in: ACCEPTED — Baseline. The reading exists in quarantine with no committed promotion. Not a B16-created record — it is the derived absence of one. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Does: ACCEPTED — Baseline. The reading exists in quarantine with no committed promotion. Not a B16-created record — it is the derived absence of one. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Gives out: ACCEPTED — Derived state quarantined; no reading bytes change. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Must never: ACCEPTED — Grant production eligibility from this state without a complete validated committed trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Fails closed by: ACCEPTED — Production consumption remains excluded while the reading is not validly promotion_committed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.4 — Derived promotion lifecycle: This state is derived from the claim’s preserved append-only events, never a mutable field on the reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.4 — Derived promotion lifecycle | Baseline. The reading exists in quarantine with no committed promotion. Not a B16-created record — it is the derived absence of one. | Baseline. The reading exists in quarantine with no committed promotion. Not a B16-created record — it is the derived absence of one. | Derived state quarantined; no reading bytes change. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.4.2 — promotion_requested
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_requested derived promotion state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Takes in: ACCEPTED — A durable promotion request event exists for the claim; no reservation, no rights, no production effect. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Does: ACCEPTED — A durable promotion request event exists for the claim; no reservation, no rights, no production effect. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Gives out: ACCEPTED — Derived state promotion_requested; no reading bytes change. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Must never: ACCEPTED — Grant production eligibility from this state without a complete validated committed trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Fails closed by: ACCEPTED — Production consumption remains excluded while the reading is not validly promotion_committed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.4 — Derived promotion lifecycle: This state is derived from the claim’s preserved append-only events, never a mutable field on the reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.4 — Derived promotion lifecycle | A durable promotion request event exists for the claim; no reservation, no rights, no production effect. | A durable promotion request event exists for the claim; no reservation, no rights, no production effect. | Derived state promotion_requested; no reading bytes change. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.9.2.1 — promotion_requested consumption exclusion | A durable promotion request event exists for the claim; no reservation, no rights, no production effect. | The claim-derived state determines that this reading has not completed promotion. | Derived state promotion_requested; no reading bytes change. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.4.3 — promotion_reserved
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_reserved derived promotion state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Takes in: ACCEPTED — Exactly one live reservation exists. No production effect. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Does: ACCEPTED — Exactly one live reservation exists. No production effect. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Gives out: ACCEPTED — Derived state promotion_reserved; no reading bytes change. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Must never: ACCEPTED — Grant production eligibility from this state without a complete validated committed trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Fails closed by: ACCEPTED — Production consumption remains excluded while the reading is not validly promotion_committed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.4 — Derived promotion lifecycle: This state is derived from the claim’s preserved append-only events, never a mutable field on the reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.4 — Derived promotion lifecycle | Exactly one live reservation exists. No production effect. | Exactly one live reservation exists. No production effect. | Derived state promotion_reserved; no reading bytes change. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.9.2.2 — promotion_reserved consumption exclusion | Exactly one live reservation exists. No production effect. | The claim-derived state determines that this reading has not completed promotion. | Derived state promotion_reserved; no reading bytes change. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.4.4 — promotion_evidence_checked
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_evidence_checked derived promotion state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Takes in: ACCEPTED — The immutable evidence snapshot is committed and bound to the claim and reservation. Still no production effect. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Does: ACCEPTED — The immutable evidence snapshot is committed and bound to the claim and reservation. Still no production effect. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Gives out: ACCEPTED — Derived state promotion_evidence_checked; no reading bytes change. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Must never: ACCEPTED — Grant production eligibility from this state without a complete validated committed trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Fails closed by: ACCEPTED — Production consumption remains excluded while the reading is not validly promotion_committed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.4 — Derived promotion lifecycle: This state is derived from the claim’s preserved append-only events, never a mutable field on the reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.4 — Derived promotion lifecycle | The immutable evidence snapshot is committed and bound to the claim and reservation. Still no production effect. | The immutable evidence snapshot is committed and bound to the claim and reservation. Still no production effect. | Derived state promotion_evidence_checked; no reading bytes change. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.9.2.3 — promotion_evidence_checked consumption exclusion | The immutable evidence snapshot is committed and bound to the claim and reservation. Still no production effect. | The claim-derived state determines that this reading has not completed promotion. | Derived state promotion_evidence_checked; no reading bytes change. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.4.5 — promotion_committed
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_committed derived promotion state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Takes in: ACCEPTED — Terminal, absorbing, idempotent success: the production-eligibility record exists with its complete matching trail. Repeats return duplicate_absorbed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Does: ACCEPTED — Terminal, absorbing, idempotent success: the production-eligibility record exists with its complete matching trail. Repeats return duplicate_absorbed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Gives out: ACCEPTED — Derived state promotion_committed; no reading bytes change. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Must never: ACCEPTED — Reopen the absorbing committed state or commit another eligibility record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Fails closed by: ACCEPTED — Duplicate attempts return duplicate_absorbed with the existing committed reference; an unvalidated trail cannot establish this state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.4 — Derived promotion lifecycle: This state is derived from the claim’s preserved append-only events, never a mutable field on the reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.4 — Derived promotion lifecycle | Terminal, absorbing, idempotent success: the production-eligibility record exists with its complete matching trail. Repeats return duplicate_absorbed. | Terminal, absorbing, idempotent success: the production-eligibility record exists with its complete matching trail. Repeats return duplicate_absorbed. | Derived state promotion_committed; no reading bytes change. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.4.6 — promotion_rejected
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_rejected derived promotion state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Takes in: ACCEPTED — Attempt-terminal with recorded cause (evidence failure, decision refusal, integrity conflict). The reading remains quarantined and never becomes production through this attempt. Whether and when a new attempt is permitted is policy owned elsewhere (A29 / B9, §12); mechanically, a later attempt is a new request under the same permanent claim, lookup-first over the recorded history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Does: ACCEPTED — Attempt-terminal with recorded cause (evidence failure, decision refusal, integrity conflict). The reading remains quarantined and never becomes production through this attempt. Whether and when a new attempt is permitted is policy owned elsewhere (A29 / B9, §12); mechanically, a later attempt is a new request under the same permanent claim, lookup-first over the recorded history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Gives out: ACCEPTED — Derived state promotion_rejected; no reading bytes change. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Must never: ACCEPTED — Grant production eligibility from this state without a complete validated committed trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Fails closed by: ACCEPTED — Production consumption remains excluded while the reading is not validly promotion_committed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.4 — Derived promotion lifecycle: This state is derived from the claim’s preserved append-only events, never a mutable field on the reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.4 — Derived promotion lifecycle | Attempt-terminal with recorded cause (evidence failure, decision refusal, integrity conflict). The reading remains quarantined and never becomes production through this attempt. Whether and when a new attempt is permitted is policy owned elsewhere (A29 / B9, §12); mechanically, a later attempt is a new request under the same permanent claim, lookup-first over the recorded history. | Attempt-terminal with recorded cause (evidence failure, decision refusal, integrity conflict). The reading remains quarantined and never becomes production through this attempt. Whether and when a new attempt is permitted is policy owned elsewhere (A29 / B9, §12); mechanically, a later attempt is a new request under the same permanent claim, lookup-first over the recorded history. | Derived state promotion_rejected; no reading bytes change. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.9.2.4 — promotion_rejected consumption exclusion | Attempt-terminal with recorded cause (evidence failure, decision refusal, integrity conflict). The reading remains quarantined and never becomes production through this attempt. Whether and when a new attempt is permitted is policy owned elsewhere (A29 / B9, §12); mechanically, a later attempt is a new request under the same permanent claim, lookup-first over the recorded history. | The claim-derived state determines that this reading has not completed promotion. | Derived state promotion_rejected; no reading bytes change. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.4.7 — dependency_blocked_held
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]

ALONE
- What it is: ACCEPTED — The dependency_blocked_held derived promotion state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Takes in: ACCEPTED — Non-terminal waiting: a required dependency (hold condition, missing authorization, A29-gated readiness) blocks progress. Fail-closed: a held candidate never becomes production by waiting. Hold lifecycle, release mechanics, and release policy are B-HOLD / A29 — B16 defines only this fail-closed waiting semantic and the recorded blocked event. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Does: ACCEPTED — Non-terminal waiting: a required dependency (hold condition, missing authorization, A29-gated readiness) blocks progress. Fail-closed: a held candidate never becomes production by waiting. Hold lifecycle, release mechanics, and release policy are B-HOLD / A29 — B16 defines only this fail-closed waiting semantic and the recorded blocked event. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Gives out: ACCEPTED — Derived state dependency_blocked_held; no reading bytes change. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Must never: ACCEPTED — Grant production eligibility from this state without a complete validated committed trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Fails closed by: ACCEPTED — Production consumption remains excluded while the reading is not validly promotion_committed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.4 — Derived promotion lifecycle: This state is derived from the claim’s preserved append-only events, never a mutable field on the reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.4 — Derived promotion lifecycle | Non-terminal waiting: a required dependency (hold condition, missing authorization, A29-gated readiness) blocks progress. Fail-closed: a held candidate never becomes production by waiting. Hold lifecycle, release mechanics, and release policy are B-HOLD / A29 — B16 defines only this fail-closed waiting semantic and the recorded blocked event. | Non-terminal waiting: a required dependency (hold condition, missing authorization, A29-gated readiness) blocks progress. Fail-closed: a held candidate never becomes production by waiting. Hold lifecycle, release mechanics, and release policy are B-HOLD / A29 — B16 defines only this fail-closed waiting semantic and the recorded blocked event. | Derived state dependency_blocked_held; no reading bytes change. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.9.2.5 — dependency_blocked_held consumption exclusion | Non-terminal waiting: a required dependency (hold condition, missing authorization, A29-gated readiness) blocks progress. Fail-closed: a held candidate never becomes production by waiting. Hold lifecycle, release mechanics, and release policy are B-HOLD / A29 — B16 defines only this fail-closed waiting semantic and the recorded blocked event. | The claim-derived state determines that this reading has not completed promotion. | Derived state dependency_blocked_held; no reading bytes change. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.4.8 — promotion_interrupted
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_interrupted derived promotion state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Takes in: ACCEPTED — The attempt ended before B16-3 with durable evidence of non-commit (crash, lost race, released reservation). Safe technical re-attempt under the same claim; substantive retry policy remains B9's. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Does: ACCEPTED — The attempt ended before B16-3 with durable evidence of non-commit (crash, lost race, released reservation). Safe technical re-attempt under the same claim; substantive retry policy remains B9's. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Gives out: ACCEPTED — Derived state promotion_interrupted; no reading bytes change. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Must never: ACCEPTED — Grant production eligibility from this state without a complete validated committed trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Fails closed by: ACCEPTED — Production consumption remains excluded while the reading is not validly promotion_committed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.4 — Derived promotion lifecycle: This state is derived from the claim’s preserved append-only events, never a mutable field on the reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.4 — Derived promotion lifecycle | The attempt ended before B16-3 with durable evidence of non-commit (crash, lost race, released reservation). Safe technical re-attempt under the same claim; substantive retry policy remains B9's. | The attempt ended before B16-3 with durable evidence of non-commit (crash, lost race, released reservation). Safe technical re-attempt under the same claim; substantive retry policy remains B9's. | Derived state promotion_interrupted; no reading bytes change. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.9.2.6 — promotion_interrupted consumption exclusion | The attempt ended before B16-3 with durable evidence of non-commit (crash, lost race, released reservation). Safe technical re-attempt under the same claim; substantive retry policy remains B9's. | The claim-derived state determines that this reading has not completed promotion. | Derived state promotion_interrupted; no reading bytes change. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.4.9 — indeterminate_recovery_required
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]

ALONE
- What it is: ACCEPTED — The indeterminate_recovery_required derived promotion state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Takes in: ACCEPTED — Evidence unreadable or contradictory. No reservation, no commit, no production effect; resolution only through §8 — never by guessing. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Does: ACCEPTED — Evidence unreadable or contradictory. No reservation, no commit, no production effect; resolution only through §8 — never by guessing. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Gives out: ACCEPTED — Derived state indeterminate_recovery_required; no reading bytes change. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Must never: ACCEPTED — Grant production eligibility from this state without a complete validated committed trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Fails closed by: ACCEPTED — No reservation, commit or production effect is permitted while the evidence is unreadable or contradictory; no outcome is guessed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.4 — Derived promotion lifecycle: This state is derived from the claim’s preserved append-only events, never a mutable field on the reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.4 — Derived promotion lifecycle | Evidence unreadable or contradictory. No reservation, no commit, no production effect; resolution only through §8 — never by guessing. | Evidence unreadable or contradictory. No reservation, no commit, no production effect; resolution only through §8 — never by guessing. | Derived state indeterminate_recovery_required; no reading bytes change. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.9.2.7 — indeterminate_recovery_required consumption exclusion | Evidence unreadable or contradictory. No reservation, no commit, no production effect; resolution only through §8 — never by guessing. | The claim-derived state determines that this reading has not completed promotion. | Derived state indeterminate_recovery_required; no reading bytes change. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.5 — Promotion transaction boundaries
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

ALONE
- What it is: ACCEPTED — The B16-0 through B16-4 boundaries and rebuildable B16-PR material. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Takes in: ACCEPTED — The promotion invocation, permanent claim and recorded evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Does: ACCEPTED — Orders lookup → reservation → evidence-snapshot commit → fenced eligibility commit → parent terminal before acknowledgement; rebuildable post-commit material is independent of success. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — An explicit terminal outcome and its complete machine-state and operation records. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Acknowledge success before the parent terminal, bypass a preceding required boundary or use an index as authority. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fails closed by: ACCEPTED — Refuses progress at the failed boundary; a committed record with missing terminal waits for idempotent terminal recovery. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.5.1 — B16-0 — Promotion-status lookup: Performs the read-only, side-effect-free status lookup first. Committed returns duplicate_absorbed and the existing eligibility ref without reservation or new canonical records. Another live reservation returns promotion_interrupted and the claim ref; held/blocked returns dependency_blocked_held. If no claim exists, establishment appends the durable request event, granting no rights. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.5.2 — B16-1 — Atomic promotion reservation: One compare-and-commit binds promotion_claim_key, reading_id, reading_integrity_ref, promotion_operation_id and child ID in phase reserved. Exactly one concurrent winner; losers observe and append no reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.5.3 — B16-2 — Evidence-snapshot verification commit: Verifies every required input, commits one immutable promotion_evidence_snapshot with its own integrity reference bound to claim/reservation, and compare-and-commits reserved → evidence_checked. B16-3 may use only that checked snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.5.4 — B16-3 — Production-eligibility commit: Wins evidence_checked → commit_fenced on one compare-and-commit, rechecks the durable fence immediately before committing, and appends one production_eligibility_record. Binds the claim’s terminal promotion_committed transition to that commit; recovery can finish the transition from commit evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.5.5 — B16-4 — Parent terminal log commit: Appends exactly one durable parent terminal before acknowledgement: promotion_committed, promotion_duplicate_absorbed, promotion_rejected, promotion_interrupted, promotion_blocked_held or promotion_indeterminate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.5.6 — B16-PR — Post-commit indexes and coverage: Rebuilds production-eligibility indexes and coverage idempotently; these are neither duplicate-prevention nor status authority and never gate success. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.12.13 — Parent terminal outcome: Success acknowledgement waits until the one parent terminal is durable after the child operations and canonical records resolve. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11 — Quarantine-to-production promotion seam | The promotion invocation, permanent claim and recorded evidence. | Orders lookup → reservation → evidence-snapshot commit → fenced eligibility commit → parent terminal before acknowledgement; rebuildable post-commit material is independent of success. Each required boundary must complete in order before promotion can acknowledge success. | An explicit terminal outcome and its complete machine-state and operation records. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |

SUB-PARTS: C-READ.11.5.1 — B16-0 — Promotion-status lookup; C-READ.11.5.2 — B16-1 — Atomic promotion reservation; C-READ.11.5.3 — B16-2 — Evidence-snapshot verification commit; C-READ.11.5.4 — B16-3 — Production-eligibility commit; C-READ.11.5.5 — B16-4 — Parent terminal log commit; C-READ.11.5.6 — B16-PR — Post-commit indexes and coverage

### C-READ.11.5.1 — B16-0 — Promotion-status lookup
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

ALONE
- What it is: ACCEPTED — The B16-0 — Promotion-status lookup boundary. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Takes in: ACCEPTED — Claim events and the caller request. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Does: ACCEPTED — Performs the read-only, side-effect-free status lookup first. Committed returns duplicate_absorbed and the existing eligibility ref without reservation or new canonical records. Another live reservation returns promotion_interrupted and the claim ref; held/blocked returns dependency_blocked_held. If no claim exists, establishment appends the durable request event, granting no rights. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — Current derived status, existing committed ref, or a newly established request. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Reserve again after committed success, duplicate a permanent claim, or invent an outcome from unreadable events. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fails closed by: ACCEPTED — Unreadable claim status returns indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.3.2 — promotion_child_op_id: Uses its own stable child operation identity referencing the parent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.2 — promotion_claim: Looks up this permanent claim’s derived status before any reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.4 — Derived promotion lifecycle: Claim-derived status must be provable; unreadable events yield indeterminate_recovery_required before any reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.5 — Promotion transaction boundaries | Claim events and the caller request. | Performs the read-only, side-effect-free status lookup first. Committed returns duplicate_absorbed and the existing eligibility ref without reservation or new canonical records. Another live reservation returns promotion_interrupted and the claim ref; held/blocked returns dependency_blocked_held. If no claim exists, establishment appends the durable request event, granting no rights. | Current derived status, existing committed ref, or a newly established request. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.8.2 — Request event duplicate prevention | Claim events and the caller request. | The source-defined permanent or operation identity and its existing committed result determine whether this action may create a new record. | Current derived status, existing committed ref, or a newly established request. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.10.1 — Recovery 1 — Crash before any promotion claim/request exists | Claim events and the caller request. | The next attempt begins with lookup-first status resolution; no absent history is reconstructed. | Current derived status, existing committed ref, or a newly established request. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.10.6 — Recovery 6 — Duplicate promotion attempt (same reading, any time) | Claim events and the caller request. | The existing committed, live-reserved, rejected or held state is looked up before any new action. | Current derived status, existing committed ref, or a newly established request. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 5 · ACCEPTED | C-READ.11.10.19 — Recovery 19 — Attempted promotion of an already production-committed reading | Claim events and the caller request. | An already committed promotion is absorbed before any new reservation. | Current derived status, existing committed ref, or a newly established request. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 6 · ACCEPTED | C-READ.11.10.6.1 — Committed duplicate | Claim events and the caller request. | A validated committed promotion is absorbed at lookup; no new reservation. | Current derived status, existing committed ref, or a newly established request. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.5.2 — B16-1 — Atomic promotion reservation
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

ALONE
- What it is: ACCEPTED — The B16-1 — Atomic promotion reservation boundary. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Takes in: ACCEPTED — A claim with no live reservation and its reading/operation identities. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Does: ACCEPTED — One compare-and-commit binds promotion_claim_key, reading_id, reading_integrity_ref, promotion_operation_id and child ID in phase reserved. Exactly one concurrent winner; losers observe and append no reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — One discoverable reservation; no production right. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Admit two live reservations or let a losing attempt append a competing reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fails closed by: ACCEPTED — No committed reservation means no evidence check or commit; another live reservation refuses this attempt. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.5.2.1 — Reservation binding: Binds promotion_claim_key, reading_id, reading_integrity_ref, promotion_operation_id and child ID in phase reserved. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.3.2 — promotion_child_op_id: Uses its own stable child operation identity referencing the parent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.6 — Promotion reservation phases and legal transitions: Requires no live reservation; compare-and-commit admits exactly one winner. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.5 — Promotion transaction boundaries | A claim with no live reservation and its reading/operation identities. | One compare-and-commit binds promotion_claim_key, reading_id, reading_integrity_ref, promotion_operation_id and child ID in phase reserved. Exactly one concurrent winner; losers observe and append no reservation. | One discoverable reservation; no production right. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.5.3 — B16-2 — Evidence-snapshot verification commit | A claim with no live reservation and its reading/operation identities. | No evidence check or snapshot commit without the committed reservation. | One discoverable reservation; no production right. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.7 — promotion_evidence_snapshot | A claim with no live reservation and its reading/operation identities. | Snapshot verification/commit requires the one live reservation bound to this claim. | One discoverable reservation; no production right. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.5.2.1 — Reservation binding | A claim with no live reservation and its reading/operation identities. | The exact claim, reading, integrity and operation identities must be bound by the single-winner reservation commit. | One discoverable reservation; no production right. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 5 · ACCEPTED | C-READ.11.5.2.1.1 — promotion_claim_key | A claim with no live reservation and its reading/operation identities. | The exact claim, reading, integrity and operation identities must be bound by the single-winner reservation commit. | One discoverable reservation; no production right. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 6 · ACCEPTED | C-READ.11.5.2.1.2 — reading_id | A claim with no live reservation and its reading/operation identities. | The exact claim, reading, integrity and operation identities must be bound by the single-winner reservation commit. | One discoverable reservation; no production right. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 7 · ACCEPTED | C-READ.11.5.2.1.3 — reading_integrity_ref | A claim with no live reservation and its reading/operation identities. | The exact claim, reading, integrity and operation identities must be bound by the single-winner reservation commit. | One discoverable reservation; no production right. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 8 · ACCEPTED | C-READ.11.5.2.1.4 — promotion_operation_id | A claim with no live reservation and its reading/operation identities. | The exact claim, reading, integrity and operation identities must be bound by the single-winner reservation commit. | One discoverable reservation; no production right. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 9 · ACCEPTED | C-READ.11.5.2.1.5 — child ID | A claim with no live reservation and its reading/operation identities. | The exact claim, reading, integrity and operation identities must be bound by the single-winner reservation commit. | One discoverable reservation; no production right. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 10 · ACCEPTED | C-READ.11.8.3 — Reservation (B16-1) duplicate prevention | A claim with no live reservation and its reading/operation identities. | The source-defined permanent or operation identity and its existing committed result determine whether this action may create a new record. | One discoverable reservation; no production right. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |
| 11 · ACCEPTED | C-READ.11.10.2.1 — No reservation | A claim with no live reservation and its reading/operation identities. | No live reservation is required before B16-1 can admit one winner. | One discoverable reservation; no production right. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 12 · ACCEPTED | C-READ.11.10.6.2 — Live reservation duplicate | A claim with no live reservation and its reading/operation identities. | Another live reservation excludes a second reservation winner. | One discoverable reservation; no production right. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 13 · ACCEPTED | C-READ.11.10.7.1 — Reservation race loser | A claim with no live reservation and its reading/operation identities. | Exactly one reservation compare-and-commit wins. | One discoverable reservation; no production right. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: C-READ.11.5.2.1 — Reservation binding

### C-READ.11.5.2.1 — Reservation binding
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Reservation binding rule within B16-1 — Atomic promotion reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Takes in: ACCEPTED — One winning reservation and the exact claim/reading/operation identities. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Does: ACCEPTED — Binds promotion_claim_key, reading_id, reading_integrity_ref, promotion_operation_id and child ID in phase reserved. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — A discoverable, uniquely owned reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Omit or swap a required binding or turn reservation into production permission. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fails closed by: ACCEPTED — Missing or inconsistent binding cannot establish a valid reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.5.2.1.1 — promotion_claim_key: The permanent claim being reserved. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.5.2.1.2 — reading_id: The exact reading being considered. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.5.2.1.3 — reading_integrity_ref: The claim-matching integrity reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.5.2.1.4 — promotion_operation_id: The parent invocation owning this attempt. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.5.2.1.5 — child ID: The stable identity of this reservation operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.5.2 — B16-1 — Atomic promotion reservation: The exact claim, reading, integrity and operation identities must be bound by the single-winner reservation commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.5.2 — B16-1 — Atomic promotion reservation | One winning reservation and the exact claim/reading/operation identities. | Binds promotion_claim_key, reading_id, reading_integrity_ref, promotion_operation_id and child ID in phase reserved. | A discoverable, uniquely owned reservation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |

SUB-PARTS: C-READ.11.5.2.1.1 — promotion_claim_key; C-READ.11.5.2.1.2 — reading_id; C-READ.11.5.2.1.3 — reading_integrity_ref; C-READ.11.5.2.1.4 — promotion_operation_id; C-READ.11.5.2.1.5 — child ID

### C-READ.11.5.2.1.1 — promotion_claim_key
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_claim_key member of Reservation binding. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Takes in: ACCEPTED — Required identity bound by the atomic reservation; proposed representation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Does: ACCEPTED — The permanent claim being reserved. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — Required identity bound by the atomic reservation; proposed representation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Omit, swap or mismatch the required reservation identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fails closed by: ACCEPTED — Without the exact binding no valid reservation/evidence/commit trail can be established. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.2 — B16-1 — Atomic promotion reservation: The exact claim, reading, integrity and operation identities must be bound by the single-winner reservation commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.5.2.1 — Reservation binding | Required identity bound by the atomic reservation; proposed representation. | The permanent claim being reserved. | Required identity bound by the atomic reservation; proposed representation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.5.2.1.2 — reading_id
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

ALONE
- What it is: ACCEPTED — The reading_id member of Reservation binding. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Takes in: ACCEPTED — Required identity bound by the atomic reservation; proposed representation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Does: ACCEPTED — The exact reading being considered. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — Required identity bound by the atomic reservation; proposed representation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Omit, swap or mismatch the required reservation identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fails closed by: ACCEPTED — Without the exact binding no valid reservation/evidence/commit trail can be established. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.2 — B16-1 — Atomic promotion reservation: The exact claim, reading, integrity and operation identities must be bound by the single-winner reservation commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.5.2.1 — Reservation binding | Required identity bound by the atomic reservation; proposed representation. | The exact reading being considered. | Required identity bound by the atomic reservation; proposed representation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.5.2.1.3 — reading_integrity_ref
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

ALONE
- What it is: ACCEPTED — The reading_integrity_ref member of Reservation binding. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Takes in: ACCEPTED — Required identity bound by the atomic reservation; proposed representation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Does: ACCEPTED — The claim-matching integrity reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — Required identity bound by the atomic reservation; proposed representation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Omit, swap or mismatch the required reservation identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fails closed by: ACCEPTED — Without the exact binding no valid reservation/evidence/commit trail can be established. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.2 — B16-1 — Atomic promotion reservation: The exact claim, reading, integrity and operation identities must be bound by the single-winner reservation commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.5.2.1 — Reservation binding | Required identity bound by the atomic reservation; proposed representation. | The claim-matching integrity reference. | Required identity bound by the atomic reservation; proposed representation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.5.2.1.4 — promotion_operation_id
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_operation_id member of Reservation binding. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Takes in: ACCEPTED — Required identity bound by the atomic reservation; proposed representation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Does: ACCEPTED — The parent invocation owning this attempt. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — Required identity bound by the atomic reservation; proposed representation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Omit, swap or mismatch the required reservation identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fails closed by: ACCEPTED — Without the exact binding no valid reservation/evidence/commit trail can be established. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.2 — B16-1 — Atomic promotion reservation: The exact claim, reading, integrity and operation identities must be bound by the single-winner reservation commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.5.2.1 — Reservation binding | Required identity bound by the atomic reservation; proposed representation. | The parent invocation owning this attempt. | Required identity bound by the atomic reservation; proposed representation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.5.2.1.5 — child ID
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

ALONE
- What it is: ACCEPTED — The child ID member of Reservation binding. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Takes in: ACCEPTED — Required identity bound by the atomic reservation; proposed representation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Does: ACCEPTED — The stable identity of this reservation operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — Required identity bound by the atomic reservation; proposed representation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Omit, swap or mismatch the required reservation identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fails closed by: ACCEPTED — Without the exact binding no valid reservation/evidence/commit trail can be established. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.2 — B16-1 — Atomic promotion reservation: The exact claim, reading, integrity and operation identities must be bound by the single-winner reservation commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.5.2.1 — Reservation binding | Required identity bound by the atomic reservation; proposed representation. | The stable identity of this reservation operation. | Required identity bound by the atomic reservation; proposed representation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.5.3 — B16-2 — Evidence-snapshot verification commit
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

ALONE
- What it is: ACCEPTED — The B16-2 — Evidence-snapshot verification commit boundary. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Takes in: ACCEPTED — A valid reserved claim and all nine required evidence inputs. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Does: ACCEPTED — Verifies every required input, commits one immutable promotion_evidence_snapshot with its own integrity reference bound to claim/reservation, and compare-and-commits reserved → evidence_checked. B16-3 may use only that checked snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — One complete immutable bound snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Commit a partial snapshot, substitute unchecked evidence, or swap evidence after checking. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fails closed by: ACCEPTED — Missing, unreadable, unauthorized, integrity-failed or contradictory inputs resolve rejected, held or indeterminate by their named class; no partial pass. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.3.2 — promotion_child_op_id: Uses its own stable child operation identity referencing the parent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.7 — promotion_evidence_snapshot: Verifies and commits this complete nine-input immutable evidence set. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.5.2 — B16-1 — Atomic promotion reservation: No evidence check or snapshot commit without the committed reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.5 — Promotion transaction boundaries | A valid reserved claim and all nine required evidence inputs. | Verifies every required input, commits one immutable promotion_evidence_snapshot with its own integrity reference bound to claim/reservation, and compare-and-commits reserved → evidence_checked. B16-3 may use only that checked snapshot. | One complete immutable bound snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.7.1 — Reading identity and integrity | A valid reserved claim and all nine required evidence inputs. | Presence, integrity, authorization and exact claim/reservation binding must verify before this input is frozen into the snapshot. | One complete immutable bound snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.7.2 — Read-only root references | A valid reserved claim and all nine required evidence inputs. | Presence, integrity, authorization and exact claim/reservation binding must verify before this input is frozen into the snapshot. | One complete immutable bound snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.7.3 — Gold-set results evidence reference | A valid reserved claim and all nine required evidence inputs. | Presence, integrity, authorization and exact claim/reservation binding must verify before this input is frozen into the snapshot. | One complete immutable bound snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 5 · ACCEPTED | C-READ.11.7.4 — Held-out set results evidence reference | A valid reserved claim and all nine required evidence inputs. | Presence, integrity, authorization and exact claim/reservation binding must verify before this input is frozen into the snapshot. | One complete immutable bound snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 6 · ACCEPTED | C-READ.11.7.5 — Manual-inspection record reference | A valid reserved claim and all nine required evidence inputs. | Presence, integrity, authorization and exact claim/reservation binding must verify before this input is frozen into the snapshot. | One complete immutable bound snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 7 · ACCEPTED | C-READ.11.7.6 — promotion_decision_ref | A valid reserved claim and all nine required evidence inputs. | Presence, integrity, authorization and exact claim/reservation binding must verify before this input is frozen into the snapshot. | One complete immutable bound snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 8 · ACCEPTED | C-READ.11.7.7 — Dual production-authorization evidence | A valid reserved claim and all nine required evidence inputs. | Presence, integrity, authorization and exact claim/reservation binding must verify before this input is frozen into the snapshot. | One complete immutable bound snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 9 · ACCEPTED | C-READ.11.7.8 — Privacy and access authorization | A valid reserved claim and all nine required evidence inputs. | Presence, integrity, authorization and exact claim/reservation binding must verify before this input is frozen into the snapshot. | One complete immutable bound snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 10 · ACCEPTED | C-READ.11.7.9 — Hold and dependency check | A valid reserved claim and all nine required evidence inputs. | Presence, integrity, authorization and exact claim/reservation binding must verify before this input is frozen into the snapshot. | One complete immutable bound snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 11 · ACCEPTED | C-READ.11.7.10 — Snapshot integrity reference | A valid reserved claim and all nine required evidence inputs. | Presence, integrity, authorization and exact claim/reservation binding must verify before this input is frozen into the snapshot. | One complete immutable bound snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 12 · ACCEPTED | C-READ.11.7.1.1 — reading_id | A valid reserved claim and all nine required evidence inputs. | The exact reading identity and integrity binding must verify before snapshot commit. | One complete immutable bound snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 13 · ACCEPTED | C-READ.11.7.1.2 — reading_idempotency_key | A valid reserved claim and all nine required evidence inputs. | The exact reading identity and integrity binding must verify before snapshot commit. | One complete immutable bound snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 14 · ACCEPTED | C-READ.11.7.1.3 — reading_integrity_ref | A valid reserved claim and all nine required evidence inputs. | The exact reading identity and integrity binding must verify before snapshot commit. | One complete immutable bound snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 15 · ACCEPTED | C-READ.11.8.4 — Evidence snapshot (B16-2) duplicate prevention | A valid reserved claim and all nine required evidence inputs. | The source-defined permanent or operation identity and its existing committed result determine whether this action may create a new record. | One complete immutable bound snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.5.4 — B16-3 — Production-eligibility commit
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

ALONE
- What it is: ACCEPTED — The B16-3 — Production-eligibility commit boundary. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Takes in: ACCEPTED — The matching claim, immutable snapshot and reservation in evidence_checked. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Does: ACCEPTED — Wins evidence_checked → commit_fenced on one compare-and-commit, rechecks the durable fence immediately before committing, and appends one production_eligibility_record. Binds the claim’s terminal promotion_committed transition to that commit; recovery can finish the transition from commit evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — One eligibility record and derived promotion_committed, without moving, editing, deleting, copying or rewriting the quarantined reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Commit without the durable fence, commit a mismatched snapshot/claim, or create/write a production store. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fails closed by: ACCEPTED — A lost fence, released reservation or mismatched trail refuses commit and is logged; no uncommitted outcome is acknowledged as success. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.3.2 — promotion_child_op_id: Uses its own stable child operation identity referencing the parent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.7 — promotion_evidence_snapshot: Consumes exactly the verified immutable snapshot, never replacement evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.6.9 — Durable fence recheck: Immediately before commit, verifies the durable commit_fenced phase. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Changes: ACCEPTED — C-READ.11.5.4.1 — production_eligibility_record: Appends the one eligibility record under the permanent claim and binds the absorbing committed transition. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.5 — Promotion transaction boundaries | The matching claim, immutable snapshot and reservation in evidence_checked. | Wins evidence_checked → commit_fenced on one compare-and-commit, rechecks the durable fence immediately before committing, and appends one production_eligibility_record. Binds the claim’s terminal promotion_committed transition to that commit; recovery can finish the transition from commit evidence. | One eligibility record and derived promotion_committed, without moving, editing, deleting, copying or rewriting the quarantined reading. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.5.4.1.1 — reading_id | The matching claim, immutable snapshot and reservation in evidence_checked. | This member must be bound to the one fenced eligibility commit and its exact claim/snapshot trail. | One eligibility record and derived promotion_committed, without moving, editing, deleting, copying or rewriting the quarantined reading. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.5.4.1.2 — promotion_claim_key | The matching claim, immutable snapshot and reservation in evidence_checked. | This member must be bound to the one fenced eligibility commit and its exact claim/snapshot trail. | One eligibility record and derived promotion_committed, without moving, editing, deleting, copying or rewriting the quarantined reading. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.5.4.1.3 — evidence_snapshot_ref | The matching claim, immutable snapshot and reservation in evidence_checked. | This member must be bound to the one fenced eligibility commit and its exact claim/snapshot trail. | One eligibility record and derived promotion_committed, without moving, editing, deleting, copying or rewriting the quarantined reading. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 5 · ACCEPTED | C-READ.11.5.4.1.4 — Parent operation ID | The matching claim, immutable snapshot and reservation in evidence_checked. | This member must be bound to the one fenced eligibility commit and its exact claim/snapshot trail. | One eligibility record and derived promotion_committed, without moving, editing, deleting, copying or rewriting the quarantined reading. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 6 · ACCEPTED | C-READ.11.5.4.1.5 — Child operation ID | The matching claim, immutable snapshot and reservation in evidence_checked. | This member must be bound to the one fenced eligibility commit and its exact claim/snapshot trail. | One eligibility record and derived promotion_committed, without moving, editing, deleting, copying or rewriting the quarantined reading. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 7 · ACCEPTED | C-READ.11.5.4.1.6 — timestamp | The matching claim, immutable snapshot and reservation in evidence_checked. | This member must be bound to the one fenced eligibility commit and its exact claim/snapshot trail. | One eligibility record and derived promotion_committed, without moving, editing, deleting, copying or rewriting the quarantined reading. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 8 · ACCEPTED | C-READ.11.5.4.1.7 — record schema version | The matching claim, immutable snapshot and reservation in evidence_checked. | This member must be bound to the one fenced eligibility commit and its exact claim/snapshot trail. | One eligibility record and derived promotion_committed, without moving, editing, deleting, copying or rewriting the quarantined reading. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 9 · ACCEPTED | C-READ.11.10.3.1 — Snapshot validates before fencing | The matching claim, immutable snapshot and reservation in evidence_checked. | The snapshot must still validate and the commit fence must be won before commit. | One eligibility record and derived promotion_committed, without moving, editing, deleting, copying or rewriting the quarantined reading. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: C-READ.11.5.4.1 — production_eligibility_record

### C-READ.11.5.4.1 — production_eligibility_record
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

ALONE
- What it is: ACCEPTED — The single external append-only eligibility record per promotion claim; proposed record/field names. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Takes in: ACCEPTED — The exact reading/claim/snapshot identities, parent/child operation identities, timestamp and record schema version under a durable commit fence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Does: ACCEPTED — Appends once at B16-3; only a valid complete claim/snapshot/eligibility trail derives promotion_committed. It never moves or copies the quarantined reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — One durable eligibility record from which effective production status is derived. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Write a second record under the claim, add status to the reading, copy/move the reading, or treat an orphan as valid. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — An orphan grants nothing: consumption stays excluded, an append-only invalidation event records cause, and recovery remains indeterminate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.5.4.1.1 — reading_id: The unchanged permanent reading identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.5.4.1.2 — promotion_claim_key: The permanent claim; permits only one eligibility record ever. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.5.4.1.3 — evidence_snapshot_ref: The exact immutable checked snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.5.4.1.4 — Parent operation ID: The promotion_operation_id of the caller invocation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.5.4.1.5 — Child operation ID: The promotion_child_op_id of the fenced commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.5.4.1.6 — timestamp: The eligibility record’s timestamp; exact representation not supplied. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.5.4.1.7 — record schema version: The eligibility record’s own schema version, separate from the immutable reading’s schema_version. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.6.9 — Durable fence recheck: The durable fence and exact claim/snapshot binding must hold at commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: This operation and its records remain subject to internal-use authorization, privacy visibility and applicable SACL scope. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11 — Quarantine-to-production promotion seam | The exact reading/claim/snapshot identities, parent/child operation identities, timestamp and record schema version under a durable commit fence. | Appends once at B16-3; only a valid complete claim/snapshot/eligibility trail derives promotion_committed. It never moves or copies the quarantined reading. | One durable eligibility record from which effective production status is derived. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.5.4 — B16-3 — Production-eligibility commit | The exact reading/claim/snapshot identities, parent/child operation identities, timestamp and record schema version under a durable commit fence. | Appends the one eligibility record under the permanent claim and binds the absorbing committed transition. | One durable eligibility record from which effective production status is derived. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.5.6 — B16-PR — Post-commit indexes and coverage | The exact reading/claim/snapshot identities, parent/child operation identities, timestamp and record schema version under a durable commit fence. | Rebuilds non-authoritative index/coverage material from valid committed eligibility records. | One durable eligibility record from which effective production status is derived. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.9.1 — Complete committed-trail requirement | The exact reading/claim/snapshot identities, parent/child operation identities, timestamp and record schema version under a durable commit fence. | Supplies the external committed eligibility record to validate alongside its claim and snapshot. | One durable eligibility record from which effective production status is derived. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |
| 5 · ACCEPTED | C-READ.11.8.6 — Production-eligibility record (B16-3) duplicate prevention | The exact reading/claim/snapshot identities, parent/child operation identities, timestamp and record schema version under a durable commit fence. | The source-defined permanent or operation identity and its existing committed result determine whether this action may create a new record. | One durable eligibility record from which effective production status is derived. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |
| 6 · ACCEPTED | C-READ.11.10.17 — Recovery 17 — Post-commit index/coverage incomplete (B16-PR) | The exact reading/claim/snapshot identities, parent/child operation identities, timestamp and record schema version under a durable commit fence. | Validated committed eligibility remains the authority; incomplete rebuildable indexes cannot invalidate it. | One durable eligibility record from which effective production status is derived. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: C-READ.11.5.4.1.1 — reading_id; C-READ.11.5.4.1.2 — promotion_claim_key; C-READ.11.5.4.1.3 — evidence_snapshot_ref; C-READ.11.5.4.1.4 — Parent operation ID; C-READ.11.5.4.1.5 — Child operation ID; C-READ.11.5.4.1.6 — timestamp; C-READ.11.5.4.1.7 — record schema version

### C-READ.11.5.4.1.1 — reading_id
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

ALONE
- What it is: ACCEPTED — The reading_id member of production_eligibility_record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Takes in: ACCEPTED — Required content of the external eligibility record; source-defined name/form. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Does: ACCEPTED — The unchanged permanent reading identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — Required content of the external eligibility record; source-defined name/form. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Omit, swap or mismatch the required committed-record content. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fails closed by: ACCEPTED — Without a complete matching claim/evidence trail this record cannot confer valid production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.4 — B16-3 — Production-eligibility commit: This member must be bound to the one fenced eligibility commit and its exact claim/snapshot trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.5.4.1 — production_eligibility_record | Required content of the external eligibility record; source-defined name/form. | The unchanged permanent reading identity. | Required content of the external eligibility record; source-defined name/form. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.5.4.1.2 — promotion_claim_key
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_claim_key member of production_eligibility_record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Takes in: ACCEPTED — Required content of the external eligibility record; source-defined name/form. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Does: ACCEPTED — The permanent claim; permits only one eligibility record ever. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — Required content of the external eligibility record; source-defined name/form. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Omit, swap or mismatch the required committed-record content. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fails closed by: ACCEPTED — Without a complete matching claim/evidence trail this record cannot confer valid production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.4 — B16-3 — Production-eligibility commit: This member must be bound to the one fenced eligibility commit and its exact claim/snapshot trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.5.4.1 — production_eligibility_record | Required content of the external eligibility record; source-defined name/form. | The permanent claim; permits only one eligibility record ever. | Required content of the external eligibility record; source-defined name/form. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.5.4.1.3 — evidence_snapshot_ref
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

ALONE
- What it is: ACCEPTED — The evidence_snapshot_ref member of production_eligibility_record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Takes in: ACCEPTED — Required content of the external eligibility record; source-defined name/form. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Does: ACCEPTED — The exact immutable checked snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — Required content of the external eligibility record; source-defined name/form. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Omit, swap or mismatch the required committed-record content. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fails closed by: ACCEPTED — Without a complete matching claim/evidence trail this record cannot confer valid production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.4 — B16-3 — Production-eligibility commit: This member must be bound to the one fenced eligibility commit and its exact claim/snapshot trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.5.4.1 — production_eligibility_record | Required content of the external eligibility record; source-defined name/form. | The exact immutable checked snapshot. | Required content of the external eligibility record; source-defined name/form. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.5.4.1.4 — Parent operation ID
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Parent operation ID member of production_eligibility_record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Takes in: ACCEPTED — Required content of the external eligibility record; source-defined name/form. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Does: ACCEPTED — The promotion_operation_id of the caller invocation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — Required content of the external eligibility record; source-defined name/form. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Omit, swap or mismatch the required committed-record content. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fails closed by: ACCEPTED — Without a complete matching claim/evidence trail this record cannot confer valid production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.4 — B16-3 — Production-eligibility commit: This member must be bound to the one fenced eligibility commit and its exact claim/snapshot trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.5.4.1 — production_eligibility_record | Required content of the external eligibility record; source-defined name/form. | The promotion_operation_id of the caller invocation. | Required content of the external eligibility record; source-defined name/form. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.5.4.1.5 — Child operation ID
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Child operation ID member of production_eligibility_record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Takes in: ACCEPTED — Required content of the external eligibility record; source-defined name/form. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Does: ACCEPTED — The promotion_child_op_id of the fenced commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — Required content of the external eligibility record; source-defined name/form. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Omit, swap or mismatch the required committed-record content. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fails closed by: ACCEPTED — Without a complete matching claim/evidence trail this record cannot confer valid production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.4 — B16-3 — Production-eligibility commit: This member must be bound to the one fenced eligibility commit and its exact claim/snapshot trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.5.4.1 — production_eligibility_record | Required content of the external eligibility record; source-defined name/form. | The promotion_child_op_id of the fenced commit. | Required content of the external eligibility record; source-defined name/form. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.5.4.1.6 — timestamp
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

ALONE
- What it is: ACCEPTED — The timestamp member of production_eligibility_record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Takes in: ACCEPTED — Required content of the external eligibility record; source-defined name/form. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Does: ACCEPTED — The eligibility record’s timestamp; exact representation not supplied. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — Required content of the external eligibility record; source-defined name/form. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Omit, swap or mismatch the required committed-record content. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fails closed by: ACCEPTED — Without a complete matching claim/evidence trail this record cannot confer valid production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.4 — B16-3 — Production-eligibility commit: This member must be bound to the one fenced eligibility commit and its exact claim/snapshot trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.5.4.1 — production_eligibility_record | Required content of the external eligibility record; source-defined name/form. | The eligibility record’s timestamp; exact representation not supplied. | Required content of the external eligibility record; source-defined name/form. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.5.4.1.7 — record schema version
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

ALONE
- What it is: ACCEPTED — The record schema version member of production_eligibility_record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Takes in: ACCEPTED — Required content of the external eligibility record; source-defined name/form. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Does: ACCEPTED — The eligibility record’s own schema version, separate from the immutable reading’s schema_version. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — Required content of the external eligibility record; source-defined name/form. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Omit, swap or mismatch the required committed-record content. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fails closed by: ACCEPTED — Without a complete matching claim/evidence trail this record cannot confer valid production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.4 — B16-3 — Production-eligibility commit: This member must be bound to the one fenced eligibility commit and its exact claim/snapshot trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.5.4.1 — production_eligibility_record | Required content of the external eligibility record; source-defined name/form. | The eligibility record’s own schema version, separate from the immutable reading’s schema_version. | Required content of the external eligibility record; source-defined name/form. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.5.5 — B16-4 — Parent terminal log commit
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

ALONE
- What it is: ACCEPTED — The B16-4 — Parent terminal log commit boundary. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Takes in: ACCEPTED — Resolved child operations and canonical records for promotion_operation_id. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Does: ACCEPTED — Appends exactly one durable parent terminal before acknowledgement: promotion_committed, promotion_duplicate_absorbed, promotion_rejected, promotion_interrupted, promotion_blocked_held or promotion_indeterminate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — One permanent parent terminal and then the caller acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Acknowledge success before this terminal or write a second terminal for the same parent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fails closed by: ACCEPTED — When commit exists but the terminal is absent, withholds acknowledgement and recovery adds only the missing terminal; logging failure never invalidates the committed eligibility record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.3.1 — promotion_operation_id: Uses the parent operation identity for exactly one terminal record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.13 — Parent terminal outcome: Commits the single parent outcome only after child operations and canonical records resolve. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.12.13 — Parent terminal outcome: Exactly one parent terminal becomes durable before acknowledgement; a missing terminal is recovered without invalidating a committed eligibility record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.5 — Promotion transaction boundaries | Resolved child operations and canonical records for promotion_operation_id. | Appends exactly one durable parent terminal before acknowledgement: promotion_committed, promotion_duplicate_absorbed, promotion_rejected, promotion_interrupted, promotion_blocked_held or promotion_indeterminate. | One permanent parent terminal and then the caller acknowledgement. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.5.6 — B16-PR — Post-commit indexes and coverage
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

ALONE
- What it is: ACCEPTED — The B16-PR — Post-commit indexes and coverage boundary. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Takes in: ACCEPTED — Committed promotion records and rebuildable derived lookup/coverage material. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Does: ACCEPTED — Rebuilds production-eligibility indexes and coverage idempotently; these are neither duplicate-prevention nor status authority and never gate success. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gives out: ACCEPTED — Rebuildable indexes/coverage over valid committed promotions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Must never: ACCEPTED — Invalidate a committed promotion because rebuildable material is incomplete, or use index state as status authority. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Fails closed by: ACCEPTED — Incomplete indexes/coverage leave committed promotions valid; the rebuildable material is repaired idempotently. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.3.2 — promotion_child_op_id: Uses its own stable child operation identity referencing the parent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.5.4.1 — production_eligibility_record: Rebuilds non-authoritative index/coverage material from valid committed eligibility records. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.5 — Promotion transaction boundaries | Committed promotion records and rebuildable derived lookup/coverage material. | Rebuilds production-eligibility indexes and coverage idempotently; these are neither duplicate-prevention nor status authority and never gate success. | Rebuildable indexes/coverage over valid committed promotions. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.6 — Promotion reservation phases and legal transitions
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The authoritative reservation phase and the three legal append-only transition paths. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Takes in: ACCEPTED — One reservation, its claim/snapshot binding, and competing fence, release or recovery actions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Does: ACCEPTED — Compares and commits on the same authoritative phase; exactly one fence/release action wins. A durable fence excludes ordinary release and second reservation; terminal release permanently excludes commit for that reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gives out: ACCEPTED — reserved, evidence_checked, commit_fenced, committed, released or recovery_released_no_commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Must never: ACCEPTED — Commit from stale phase observations, release after a fence normally, create another live reservation while fenced, or revive a released reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fails closed by: ACCEPTED — Refuses a losing fence/release or stale executor commit; strict recovery with any proof missing becomes indeterminate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.6.1 — reserved reservation phase: One live reservation has been won; it may proceed to evidence checking or legally release. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.6.2 — evidence_checked reservation phase: The complete immutable snapshot is committed; fencing or normal pre-fence release may compete. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.6.3 — commit_fenced reservation phase: The durable exclusive commit fence is held; only completion or the strict recovery-only no-commit release can proceed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.6.4 — committed reservation phase: The eligibility commit completed for this fenced reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.6.5 — released reservation phase: Normal release won from reserved or evidence_checked; fencing and commit are permanently forbidden for this reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.6.6 — recovery_released_no_commit reservation phase: The strict recovery-only release is committed with all four proofs; fencing and commit are permanently forbidden for this reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.6.7 — Three legal reservation paths: Permits normal pre-fence release, successful fenced commit, or strict recovery-only release proving non-commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.6.8 — Fence versus release single winner: Admits exactly one winner; the losing action has no commit right. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.6.9 — Durable fence recheck: Checks the durable commit_fenced phase immediately before committing. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.6.7 — Three legal reservation paths: Only the three legal append-only reservation paths may change the authoritative phase. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11 — Quarantine-to-production promotion seam | One reservation, its claim/snapshot binding, and competing fence, release or recovery actions. | Compares and commits on the same authoritative phase; exactly one fence/release action wins. A durable fence excludes ordinary release and second reservation; terminal release permanently excludes commit for that reservation. | reserved, evidence_checked, commit_fenced, committed, released or recovery_released_no_commit. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.5.2 — B16-1 — Atomic promotion reservation | One reservation, its claim/snapshot binding, and competing fence, release or recovery actions. | Requires no live reservation; compare-and-commit admits exactly one winner. | reserved, evidence_checked, commit_fenced, committed, released or recovery_released_no_commit. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.6.8 — Fence versus release single winner | One reservation, its claim/snapshot binding, and competing fence, release or recovery actions. | The authoritative phase, rather than a stale observation, governs the winning fence/release transition. | reserved, evidence_checked, commit_fenced, committed, released or recovery_released_no_commit. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.10.2 — Recovery 2 — Claim/request durable, evidence check absent (reservation may or may not exist) | One reservation, its claim/snapshot binding, and competing fence, release or recovery actions. | The durable reservation phase decides whether B16-1 may reserve, B16-2 may resume or pre-fence release is legal. | reserved, evidence_checked, commit_fenced, committed, released or recovery_released_no_commit. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 5 · ACCEPTED | C-READ.11.10.2.2 — Live reserved attempt | One reservation, its claim/snapshot binding, and competing fence, release or recovery actions. | Only a live reserved attempt may resume evidence checking; normal release remains pre-fence. | reserved, evidence_checked, commit_fenced, committed, released or recovery_released_no_commit. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 6 · ACCEPTED | C-READ.11.10.16.1 — Evidence-checked resume or release | One reservation, its claim/snapshot binding, and competing fence, release or recovery actions. | Only evidence_checked permits ordinary resume or pre-fence release; the snapshot must still validate. | reserved, evidence_checked, commit_fenced, committed, released or recovery_released_no_commit. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: C-READ.11.6.1 — reserved reservation phase; C-READ.11.6.2 — evidence_checked reservation phase; C-READ.11.6.3 — commit_fenced reservation phase; C-READ.11.6.4 — committed reservation phase; C-READ.11.6.5 — released reservation phase; C-READ.11.6.6 — recovery_released_no_commit reservation phase; C-READ.11.6.7 — Three legal reservation paths; C-READ.11.6.8 — Fence versus release single winner; C-READ.11.6.9 — Durable fence recheck

### C-READ.11.6.1 — reserved reservation phase
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The reserved reservation phase rule within Promotion reservation phases and legal transitions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Takes in: ACCEPTED — The reservation’s authoritative append-only phase history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Does: ACCEPTED — One live reservation has been won; it may proceed to evidence checking or legally release. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gives out: ACCEPTED — Derived reservation phase reserved. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Must never: ACCEPTED — Do not claim evidence_checked or production eligibility merely from reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fails closed by: ACCEPTED — An illegal or unproved transition is refused; missing strict-recovery proof leaves indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.6.7 — Three legal reservation paths: Only one of the three legal phase paths may establish this reservation phase. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.6 — Promotion reservation phases and legal transitions | The reservation’s authoritative append-only phase history. | One live reservation has been won; it may proceed to evidence checking or legally release. | Derived reservation phase reserved. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.6.2 — evidence_checked reservation phase
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The evidence_checked reservation phase rule within Promotion reservation phases and legal transitions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Takes in: ACCEPTED — The reservation’s authoritative append-only phase history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Does: ACCEPTED — The complete immutable snapshot is committed; fencing or normal pre-fence release may compete. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gives out: ACCEPTED — Derived reservation phase evidence_checked. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Must never: ACCEPTED — Do not treat snapshot commitment as production commitment or swap its evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fails closed by: ACCEPTED — An illegal or unproved transition is refused; missing strict-recovery proof leaves indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.6.7 — Three legal reservation paths: Only one of the three legal phase paths may establish this reservation phase. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.6 — Promotion reservation phases and legal transitions | The reservation’s authoritative append-only phase history. | The complete immutable snapshot is committed; fencing or normal pre-fence release may compete. | Derived reservation phase evidence_checked. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.6.3 — commit_fenced reservation phase
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The commit_fenced reservation phase rule within Promotion reservation phases and legal transitions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Takes in: ACCEPTED — The reservation’s authoritative append-only phase history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Does: ACCEPTED — The durable exclusive commit fence is held; only completion or the strict recovery-only no-commit release can proceed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gives out: ACCEPTED — Derived reservation phase commit_fenced. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Must never: ACCEPTED — Do not allow ordinary release or a second reservation after the fence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fails closed by: ACCEPTED — An illegal or unproved transition is refused; missing strict-recovery proof leaves indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.6.7 — Three legal reservation paths: Only one of the three legal phase paths may establish this reservation phase. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.6 — Promotion reservation phases and legal transitions | The reservation’s authoritative append-only phase history. | The durable exclusive commit fence is held; only completion or the strict recovery-only no-commit release can proceed. | Derived reservation phase commit_fenced. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.6.9 — Durable fence recheck | The reservation’s authoritative append-only phase history. | Commit requires the durable commit_fenced phase immediately before the append. | Derived reservation phase commit_fenced. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.6.4 — committed reservation phase
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The committed reservation phase rule within Promotion reservation phases and legal transitions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Takes in: ACCEPTED — The reservation’s authoritative append-only phase history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Does: ACCEPTED — The eligibility commit completed for this fenced reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gives out: ACCEPTED — Derived reservation phase committed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Must never: ACCEPTED — Do not commit another eligibility record or reopen this reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fails closed by: ACCEPTED — An illegal or unproved transition is refused; missing strict-recovery proof leaves indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.6.7 — Three legal reservation paths: Only one of the three legal phase paths may establish this reservation phase. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.6 — Promotion reservation phases and legal transitions | The reservation’s authoritative append-only phase history. | The eligibility commit completed for this fenced reservation. | Derived reservation phase committed. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.6.5 — released reservation phase
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The released reservation phase rule within Promotion reservation phases and legal transitions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Takes in: ACCEPTED — The reservation’s authoritative append-only phase history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Does: ACCEPTED — Normal release won from reserved or evidence_checked; fencing and commit are permanently forbidden for this reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gives out: ACCEPTED — Derived reservation phase released. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Must never: ACCEPTED — Fence or commit this released reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fails closed by: ACCEPTED — An illegal or unproved transition is refused; missing strict-recovery proof leaves indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.6.7 — Three legal reservation paths: Only one of the three legal phase paths may establish this reservation phase. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.6 — Promotion reservation phases and legal transitions | The reservation’s authoritative append-only phase history. | Normal release won from reserved or evidence_checked; fencing and commit are permanently forbidden for this reservation. | Derived reservation phase released. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.6.6 — recovery_released_no_commit reservation phase
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The recovery_released_no_commit reservation phase rule within Promotion reservation phases and legal transitions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Takes in: ACCEPTED — The reservation’s authoritative append-only phase history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Does: ACCEPTED — The strict recovery-only release is committed with all four proofs; fencing and commit are permanently forbidden for this reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gives out: ACCEPTED — Derived reservation phase recovery_released_no_commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Must never: ACCEPTED — Commit this released reservation, omit a recovery proof or treat ordinary release as this outcome. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fails closed by: ACCEPTED — An illegal or unproved transition is refused; missing strict-recovery proof leaves indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.6.7 — Three legal reservation paths: Only one of the three legal phase paths may establish this reservation phase. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.6 — Promotion reservation phases and legal transitions | The reservation’s authoritative append-only phase history. | The strict recovery-only release is committed with all four proofs; fencing and commit are permanently forbidden for this reservation. | Derived reservation phase recovery_released_no_commit. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.6.7 — Three legal reservation paths
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Three legal reservation paths rule within Promotion reservation phases and legal transitions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Takes in: ACCEPTED — The authoritative starting phase and transition request. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Does: ACCEPTED — Permits normal pre-fence release, successful fenced commit, or strict recovery-only release proving non-commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gives out: ACCEPTED — A legal appended phase transition or refusal. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Must never: ACCEPTED — Invent another path, edit phase history, or cross a terminal-release fence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fails closed by: ACCEPTED — Refuses transitions outside the three legal paths. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.6.7.1 — Normal reservation release: Appends released only if release wins the compare-and-commit against fencing. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.6.7.2 — Successful reservation commit: Transitions reserved → evidence_checked → commit_fenced → committed; immediately before commit, checks the durable fence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.6.7.3 — Strict recovery-only release: Permits commit_fenced → recovery_released_no_commit only with exclusive recovery authority, no possible live executor, exact claim/snapshot checks and conclusive commit non-existence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.6.8 — Fence versus release single winner: Fencing and release compete on the same authoritative phase; exactly one wins. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.6 — Promotion reservation phases and legal transitions | The authoritative starting phase and transition request. | Permits normal pre-fence release, successful fenced commit, or strict recovery-only release proving non-commit. Only the three legal append-only reservation paths may change the authoritative phase. | A legal appended phase transition or refusal. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.6.1 — reserved reservation phase | The authoritative starting phase and transition request. | Only one of the three legal phase paths may establish this reservation phase. | A legal appended phase transition or refusal. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.6.2 — evidence_checked reservation phase | The authoritative starting phase and transition request. | Only one of the three legal phase paths may establish this reservation phase. | A legal appended phase transition or refusal. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.6.3 — commit_fenced reservation phase | The authoritative starting phase and transition request. | Only one of the three legal phase paths may establish this reservation phase. | A legal appended phase transition or refusal. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |
| 5 · ACCEPTED | C-READ.11.6.4 — committed reservation phase | The authoritative starting phase and transition request. | Only one of the three legal phase paths may establish this reservation phase. | A legal appended phase transition or refusal. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |
| 6 · ACCEPTED | C-READ.11.6.5 — released reservation phase | The authoritative starting phase and transition request. | Only one of the three legal phase paths may establish this reservation phase. | A legal appended phase transition or refusal. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |
| 7 · ACCEPTED | C-READ.11.6.6 — recovery_released_no_commit reservation phase | The authoritative starting phase and transition request. | Only one of the three legal phase paths may establish this reservation phase. | A legal appended phase transition or refusal. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |

SUB-PARTS: C-READ.11.6.7.1 — Normal reservation release; C-READ.11.6.7.2 — Successful reservation commit; C-READ.11.6.7.3 — Strict recovery-only release

### C-READ.11.6.7.1 — Normal reservation release
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Normal reservation release rule within Three legal reservation paths. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Takes in: ACCEPTED — A reservation in reserved or evidence_checked. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Does: ACCEPTED — Appends released only if release wins the compare-and-commit against fencing. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gives out: ACCEPTED — released; later fencing/commit forbidden for that reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Must never: ACCEPTED — Release normally from commit_fenced. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fails closed by: ACCEPTED — If the fence already won, ordinary release is refused. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.6.8 — Fence versus release single winner: Release must win against fencing on the same authoritative phase. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.6.7 — Three legal reservation paths | A reservation in reserved or evidence_checked. | Appends released only if release wins the compare-and-commit against fencing. | released; later fencing/commit forbidden for that reservation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.10.3.2 — Pre-fence release | A reservation in reserved or evidence_checked. | Normal release is legal only before the fence and permanently bars that reservation from commit. | released; later fencing/commit forbidden for that reservation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.6.7.2 — Successful reservation commit
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Successful reservation commit rule within Three legal reservation paths. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Takes in: ACCEPTED — reserved followed by valid snapshot commitment. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Does: ACCEPTED — Transitions reserved → evidence_checked → commit_fenced → committed; immediately before commit, checks the durable fence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gives out: ACCEPTED — One committed production-eligibility record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Must never: ACCEPTED — Commit without a current durable fence or after terminal release. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fails closed by: ACCEPTED — Losing the fence or failing its durable check prevents commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.6.9 — Durable fence recheck: A stale executor cannot commit; the durable fence must still hold immediately before commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.6.7 — Three legal reservation paths | reserved followed by valid snapshot commitment. | Transitions reserved → evidence_checked → commit_fenced → committed; immediately before commit, checks the durable fence. | One committed production-eligibility record. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.6.7.3 — Strict recovery-only release
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Strict recovery-only release rule within Three legal reservation paths. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Takes in: ACCEPTED — reserved/evidence_checked → commit_fenced with an incomplete operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Does: ACCEPTED — Permits commit_fenced → recovery_released_no_commit only with exclusive recovery authority, no possible live executor, exact claim/snapshot checks and conclusive commit non-existence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gives out: ACCEPTED — An append-only recovery terminal; a later attempt needs a new request/reservation under the same claim. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Must never: ACCEPTED — Guess non-commit or permit an old executor to commit after recovery release. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fails closed by: ACCEPTED — If any of the four proofs is missing, returns indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.6.7.3.1 — Exclusive recovery authority: Exclusive recovery authority is active. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.6.7.3.2 — No live executor can complete: No live executor can still complete this operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.6.7.3.3 — Exact claim and snapshot checked: The exact claim and snapshot identities were checked. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.6.7.3.4 — Conclusive commit non-existence: Non-existence of the commit is conclusively proven. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.6.7 — Three legal reservation paths | reserved/evidence_checked → commit_fenced with an incomplete operation. | Permits commit_fenced → recovery_released_no_commit only with exclusive recovery authority, no possible live executor, exact claim/snapshot checks and conclusive commit non-existence. | An append-only recovery terminal; a later attempt needs a new request/reservation under the same claim. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.10.3 — Recovery 3 — Evidence snapshot committed, production commit absent | reserved/evidence_checked → commit_fenced with an incomplete operation. | A fenced non-commit release requires all four strict proofs; otherwise recovery stays indeterminate. | An append-only recovery terminal; a later attempt needs a new request/reservation under the same claim. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.10.16 — Recovery 16 — Promotion evidence present without a production record (snapshot committed, no eligibility record) | reserved/evidence_checked → commit_fenced with an incomplete operation. | A fenced non-commit release requires all four strict proofs; otherwise recovery stays indeterminate. | An append-only recovery terminal; a later attempt needs a new request/reservation under the same claim. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.8.7 — Recovery release duplicate prevention | reserved/evidence_checked → commit_fenced with an incomplete operation. | The source-defined permanent or operation identity and its existing committed result determine whether this action may create a new record. | An append-only recovery terminal; a later attempt needs a new request/reservation under the same claim. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |
| 5 · ACCEPTED | C-READ.11.10.3.3 — Already fenced recovery | reserved/evidence_checked → commit_fenced with an incomplete operation. | Fenced recovery without commit requires all four strict release proofs or stays indeterminate. | An append-only recovery terminal; a later attempt needs a new request/reservation under the same claim. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 6 · ACCEPTED | C-READ.11.10.16.2 — Fenced snapshot without eligibility | reserved/evidence_checked → commit_fenced with an incomplete operation. | A fenced no-commit release requires all four conclusive proofs; otherwise recovery stays indeterminate. | An append-only recovery terminal; a later attempt needs a new request/reservation under the same claim. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: C-READ.11.6.7.3.1 — Exclusive recovery authority; C-READ.11.6.7.3.2 — No live executor can complete; C-READ.11.6.7.3.3 — Exact claim and snapshot checked; C-READ.11.6.7.3.4 — Conclusive commit non-existence

### C-READ.11.6.7.3.1 — Exclusive recovery authority
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Exclusive recovery authority rule within Strict recovery-only release. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Takes in: ACCEPTED — The recovery authority, executor state and durable identity/commit evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Does: ACCEPTED — Exclusive recovery authority is active. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gives out: ACCEPTED — A satisfied mandatory recovery-release condition. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Must never: ACCEPTED — Substitute assumption for this mandatory proof. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fails closed by: ACCEPTED — Missing or unprovable condition leaves indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.6.7.3 — Strict recovery-only release | The recovery authority, executor state and durable identity/commit evidence. | Exclusive recovery authority is active. | A satisfied mandatory recovery-release condition. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.6.7.3.2 — No live executor can complete
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The No live executor can complete rule within Strict recovery-only release. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Takes in: ACCEPTED — The recovery authority, executor state and durable identity/commit evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Does: ACCEPTED — No live executor can still complete this operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gives out: ACCEPTED — A satisfied mandatory recovery-release condition. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Must never: ACCEPTED — Substitute assumption for this mandatory proof. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fails closed by: ACCEPTED — Missing or unprovable condition leaves indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.6.7.3 — Strict recovery-only release | The recovery authority, executor state and durable identity/commit evidence. | No live executor can still complete this operation. | A satisfied mandatory recovery-release condition. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.6.7.3.3 — Exact claim and snapshot checked
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Exact claim and snapshot checked rule within Strict recovery-only release. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Takes in: ACCEPTED — The recovery authority, executor state and durable identity/commit evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Does: ACCEPTED — The exact claim and snapshot identities were checked. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gives out: ACCEPTED — A satisfied mandatory recovery-release condition. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Must never: ACCEPTED — Substitute assumption for this mandatory proof. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fails closed by: ACCEPTED — Missing or unprovable condition leaves indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.6.7.3 — Strict recovery-only release | The recovery authority, executor state and durable identity/commit evidence. | The exact claim and snapshot identities were checked. | A satisfied mandatory recovery-release condition. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.6.7.3.4 — Conclusive commit non-existence
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Conclusive commit non-existence rule within Strict recovery-only release. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Takes in: ACCEPTED — The recovery authority, executor state and durable identity/commit evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Does: ACCEPTED — Non-existence of the commit is conclusively proven. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gives out: ACCEPTED — A satisfied mandatory recovery-release condition. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Must never: ACCEPTED — Substitute assumption for this mandatory proof. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fails closed by: ACCEPTED — Missing or unprovable condition leaves indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.6.7.3 — Strict recovery-only release | The recovery authority, executor state and durable identity/commit evidence. | Non-existence of the commit is conclusively proven. | A satisfied mandatory recovery-release condition. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.6.8 — Fence versus release single winner
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Fence versus release single winner rule within Promotion reservation phases and legal transitions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Takes in: ACCEPTED — Competing fence and release against the same authoritative reservation phase. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Does: ACCEPTED — Admits exactly one winner; the losing action has no commit right. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gives out: ACCEPTED — One winning phase transition. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Must never: ACCEPTED — Allow fence and release both to win. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fails closed by: ACCEPTED — Refuses the losing action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.6 — Promotion reservation phases and legal transitions: The authoritative phase, rather than a stale observation, governs the winning fence/release transition. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.6 — Promotion reservation phases and legal transitions | Competing fence and release against the same authoritative reservation phase. | Admits exactly one winner; the losing action has no commit right. | One winning phase transition. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.6.7.1 — Normal reservation release | Competing fence and release against the same authoritative reservation phase. | Release must win against fencing on the same authoritative phase. | One winning phase transition. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.6.7 — Three legal reservation paths | Competing fence and release against the same authoritative reservation phase. | Fencing and release compete on the same authoritative phase; exactly one wins. | One winning phase transition. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.8.5 — Commit fence (B16-3 entry) duplicate prevention | Competing fence and release against the same authoritative reservation phase. | The source-defined permanent or operation identity and its existing committed result determine whether this action may create a new record. | One winning phase transition. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |
| 5 · ACCEPTED | C-READ.11.10.7 — Recovery 7 — Conflicting promotion attempts (race) | Competing fence and release against the same authoritative reservation phase. | One compare-and-commit winner is required; contradictory records never select a guessed winner. | One winning phase transition. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 6 · ACCEPTED | C-READ.11.10.7.2 — Fence-release race loser | Competing fence and release against the same authoritative reservation phase. | Fence and release have exactly one authoritative winner. | One winning phase transition. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.6.9 — Durable fence recheck
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Durable fence recheck rule within Promotion reservation phases and legal transitions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Takes in: ACCEPTED — A delayed executor holding any prior phase observation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Does: ACCEPTED — Checks the durable commit_fenced phase immediately before committing. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gives out: ACCEPTED — Commit may continue only under the still-valid durable fence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Must never: ACCEPTED — Commit on a stale pre-fence observation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fails closed by: ACCEPTED — Refuses commit if the fence is not durable and current. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.6.3 — commit_fenced reservation phase: Commit requires the durable commit_fenced phase immediately before the append. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.6 — Promotion reservation phases and legal transitions | A delayed executor holding any prior phase observation. | Checks the durable commit_fenced phase immediately before committing. | Commit may continue only under the still-valid durable fence. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.6.7.2 — Successful reservation commit | A delayed executor holding any prior phase observation. | A stale executor cannot commit; the durable fence must still hold immediately before commit. | Commit may continue only under the still-valid durable fence. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.5.4 — B16-3 — Production-eligibility commit | A delayed executor holding any prior phase observation. | Immediately before commit, verifies the durable commit_fenced phase. | Commit may continue only under the still-valid durable fence. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.5.4.1 — production_eligibility_record | A delayed executor holding any prior phase observation. | The durable fence and exact claim/snapshot binding must hold at commit. | Commit may continue only under the still-valid durable fence. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.7 — promotion_evidence_snapshot
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]

ALONE
- What it is: ACCEPTED — One immutable append-only snapshot containing all nine required evidence inputs by reference plus its own integrity reference; names proposed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Takes in: ACCEPTED — The complete nine-input set for the claim and winning reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Does: ACCEPTED — Verifies presence, integrity, authorization and binding, never evidence content; freezes the complete reference set so B16-3 cannot swap checked evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gives out: ACCEPTED — A complete claim/reservation-bound snapshot with its own integrity reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Must never: ACCEPTED — Interpret or score evidence, fabricate a missing input, substitute B24 validator success for production trust, or commit a partial snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — Missing/failed inputs reject or hold if pending; unreadable or contradictory inputs become indeterminate; unauthorized inputs are refused; no partial pass. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.7.1 — Reading identity and integrity: Verifies the reading and complete-record integrity against the claim-bound value. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.7.2 — Read-only root references: Verifies each exists by identity through the sealed/B11-governed owner, without consuming root content or touching a batch. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.7.3 — Gold-set results evidence reference: Verifies the required gold-results evidence reference, preserving the evidence producer’s mechanics; it performs no gold scoring. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.7.4 — Held-out set results evidence reference: Verifies the second required evidence source by presence, integrity, authorization and binding; it does not define or score a held-out set. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.7.5 — Manual-inspection record reference: Verifies the recorded inspection and its binding; B16 never performs or scores the inspection. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.7.6 — promotion_decision_ref: Verifies the decision exists, is intact and binds this reading; the meaning of passing is not chosen by the mechanical gate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.7.7 — Dual production-authorization evidence: Requires both protections: a Ness-only physical marker verification event and the matching approved PROPOSED CHANGE dry-run reference; neither substitutes for the other. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.7.8 — Privacy and access authorization: Requires privacy authorization before relevance and honors the applicable access scope. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.7.9 — Hold and dependency check: If a block exists, resolves dependency_blocked_held; hold release and policy remain with their own governing owners. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.7.10 — Snapshot integrity reference: Protects the one immutable claim/reservation-bound reference set against replacement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.5.2 — B16-1 — Atomic promotion reservation: Snapshot verification/commit requires the one live reservation bound to this claim. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: This operation and its records remain subject to internal-use authorization, privacy visibility and applicable SACL scope. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11 — Quarantine-to-production promotion seam | The complete nine-input set for the claim and winning reservation. | Verifies presence, integrity, authorization and binding, never evidence content; freezes the complete reference set so B16-3 cannot swap checked evidence. | A complete claim/reservation-bound snapshot with its own integrity reference. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.5.3 — B16-2 — Evidence-snapshot verification commit | The complete nine-input set for the claim and winning reservation. | Verifies and commits this complete nine-input immutable evidence set. | A complete claim/reservation-bound snapshot with its own integrity reference. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.5.4 — B16-3 — Production-eligibility commit | The complete nine-input set for the claim and winning reservation. | Consumes exactly the verified immutable snapshot, never replacement evidence. | A complete claim/reservation-bound snapshot with its own integrity reference. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.9.1 — Complete committed-trail requirement | The complete nine-input set for the claim and winning reservation. | The bound complete snapshot must verify alongside the claim and eligibility record; an isolated record grants nothing. | A complete claim/reservation-bound snapshot with its own integrity reference. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |
| 5 · ACCEPTED | C-READ.11.10.13 — Recovery 13 — Contradictory evidence (any two bound inputs disagree; snapshot integrity mismatch) | The complete nine-input set for the claim and winning reservation. | Contradictory bound inputs or snapshot integrity mismatch cannot establish a valid evidence set. | A complete claim/reservation-bound snapshot with its own integrity reference. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 6 · ACCEPTED | C-READ.11.10.7.3 — Contradictory race evidence | The complete nine-input set for the claim and winning reservation. | Contradictory evidence prevents a provable snapshot/commit result. | A complete claim/reservation-bound snapshot with its own integrity reference. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 7 · ACCEPTED | C-READ.11.10.12.1 — Missing or failed results | The complete nine-input set for the claim and winning reservation. | The complete mandatory evidence set must verify; missing or failed results cannot pass. | A complete claim/reservation-bound snapshot with its own integrity reference. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: C-READ.11.7.1 — Reading identity and integrity; C-READ.11.7.2 — Read-only root references; C-READ.11.7.3 — Gold-set results evidence reference; C-READ.11.7.4 — Held-out set results evidence reference; C-READ.11.7.5 — Manual-inspection record reference; C-READ.11.7.6 — promotion_decision_ref; C-READ.11.7.7 — Dual production-authorization evidence; C-READ.11.7.8 — Privacy and access authorization; C-READ.11.7.9 — Hold and dependency check; C-READ.11.7.10 — Snapshot integrity reference

### C-READ.11.7.1 — Reading identity and integrity
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Reading identity and integrity rule within promotion_evidence_snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Takes in: ACCEPTED — reading_id, reading_idempotency_key and reading_integrity_ref. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Does: ACCEPTED — Verifies the reading and complete-record integrity against the claim-bound value. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gives out: ACCEPTED — One verified bound evidence input; all nine are needed for a snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Must never: ACCEPTED — Omit or fabricate this required input, treat it as independently sufficient, or substitute unbound evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — A missing or unreadable reading is indeterminate; no reconstruction or substitute record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.7.1.1 — reading_id: Identifies the exact quarantined reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.7.1.2 — reading_idempotency_key: Corroborates its per-store operation identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.7.1.3 — reading_integrity_ref: Matches the complete immutable stored reading and the claim-bound reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.5.3 — B16-2 — Evidence-snapshot verification commit: Presence, integrity, authorization and exact claim/reservation binding must verify before this input is frozen into the snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.7 — promotion_evidence_snapshot | reading_id, reading_idempotency_key and reading_integrity_ref. | Verifies the reading and complete-record integrity against the claim-bound value. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.1.1 — reading_id | reading_id, reading_idempotency_key and reading_integrity_ref. | This required reference must verify before the snapshot can commit. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.1.2 — reading_idempotency_key | reading_id, reading_idempotency_key and reading_integrity_ref. | This required reference must verify before the snapshot can commit. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.1.3 — reading_integrity_ref | reading_id, reading_idempotency_key and reading_integrity_ref. | This required reference must verify before the snapshot can commit. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 5 · ACCEPTED | C-READ.11.10.10 — Recovery 10 — Quarantined reading missing or unreadable | reading_id, reading_idempotency_key and reading_integrity_ref. | A missing or unreadable quarantined reading cannot supply verified identity/integrity evidence. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: C-READ.11.7.1.1 — reading_id; C-READ.11.7.1.2 — reading_idempotency_key; C-READ.11.7.1.3 — reading_integrity_ref

### C-READ.11.7.1.1 — reading_id
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]

ALONE
- What it is: ACCEPTED — The reading_id member of Reading identity and integrity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Takes in: ACCEPTED — Required identity evidence by reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Does: ACCEPTED — Identifies the exact quarantined reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gives out: ACCEPTED — Required identity evidence by reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Must never: ACCEPTED — Omit or substitute this reading identity binding. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — Invalid identity or integrity prevents snapshot commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.3 — B16-2 — Evidence-snapshot verification commit: The exact reading identity and integrity binding must verify before snapshot commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.7.1 — Reading identity and integrity | Required identity evidence by reference. | Identifies the exact quarantined reading. | Required identity evidence by reference. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.7.1.2 — reading_idempotency_key
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]

ALONE
- What it is: ACCEPTED — The reading_idempotency_key member of Reading identity and integrity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Takes in: ACCEPTED — Required identity evidence by reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Does: ACCEPTED — Corroborates its per-store operation identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gives out: ACCEPTED — Required identity evidence by reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Must never: ACCEPTED — Omit or substitute this reading identity binding. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — Invalid identity or integrity prevents snapshot commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.3 — B16-2 — Evidence-snapshot verification commit: The exact reading identity and integrity binding must verify before snapshot commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.7.1 — Reading identity and integrity | Required identity evidence by reference. | Corroborates its per-store operation identity. | Required identity evidence by reference. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.7.1.3 — reading_integrity_ref
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]

ALONE
- What it is: ACCEPTED — The reading_integrity_ref member of Reading identity and integrity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Takes in: ACCEPTED — Required identity evidence by reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Does: ACCEPTED — Matches the complete immutable stored reading and the claim-bound reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gives out: ACCEPTED — Required identity evidence by reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Must never: ACCEPTED — Omit or substitute this reading identity binding. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — Invalid identity or integrity prevents snapshot commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.3 — B16-2 — Evidence-snapshot verification commit: The exact reading identity and integrity binding must verify before snapshot commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.7.1 — Reading identity and integrity | Required identity evidence by reference. | Matches the complete immutable stored reading and the claim-bound reference. | Required identity evidence by reference. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.7.2 — Read-only root references
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Read-only root references rule within promotion_evidence_snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Takes in: ACCEPTED — Every root ID in the reading’s reads list. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Does: ACCEPTED — Verifies each exists by identity through the sealed/B11-governed owner, without consuming root content or touching a batch. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gives out: ACCEPTED — One verified bound evidence input; all nine are needed for a snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Must never: ACCEPTED — Omit or fabricate this required input, treat it as independently sufficient, or substitute unbound evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — An unverifiable root rejects with cause; unreadable verification is indeterminate; no root is invented or repaired. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.3 — B16-2 — Evidence-snapshot verification commit: Presence, integrity, authorization and exact claim/reservation binding must verify before this input is frozen into the snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.7 — promotion_evidence_snapshot | Every root ID in the reading’s reads list. | Verifies each exists by identity through the sealed/B11-governed owner, without consuming root content or touching a batch. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.1.4 — reads identity verification | Every root ID in the reading’s reads list. | This required reference must verify before the snapshot can commit. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.10.11 — Recovery 11 — Root reference missing or unreadable (a reads id cannot be verified) | Every root ID in the reading’s reads list. | Each referenced root must verify by identity; missing or unreadable verification cannot pass. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.10.11.1 — Unverifiable root identity | Every root ID in the reading’s reads list. | All root references must be verified by identity. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 5 · ACCEPTED | C-READ.11.10.11.2 — Unreadable root verification | Every root ID in the reading’s reads list. | Unreadable root verification cannot pass as established existence. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 6 · ACCEPTED | C-READ.11.13.3 — Read-only root and reading boundary | Every root ID in the reading’s reads list. | Root existence is checked read-only by identity; no missing reference can be repaired or guessed by B16. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.7.3 — Gold-set results evidence reference
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Gold-set results evidence reference rule within promotion_evidence_snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Takes in: ACCEPTED — The recorded results for the applicable gold-set run. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Does: ACCEPTED — Verifies the required gold-results evidence reference, preserving the evidence producer’s mechanics; it performs no gold scoring. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gives out: ACCEPTED — One verified bound evidence input; all nine are needed for a snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Must never: ACCEPTED — Omit or fabricate this required input, treat it as independently sufficient, or substitute unbound evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — Missing or failed results reject; pending results may hold; no results are fabricated, inferred or substituted. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.3 — B16-2 — Evidence-snapshot verification commit: Presence, integrity, authorization and exact claim/reservation binding must verify before this input is frozen into the snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.7 — promotion_evidence_snapshot | The recorded results for the applicable gold-set run. | Verifies the required gold-results evidence reference, preserving the evidence producer’s mechanics; it performs no gold scoring. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.10.12 — Recovery 12 — B24 acceptance evidence (gold-set / held-out results) missing or failed | The recorded results for the applicable gold-set run. | Required gold-results evidence must exist and pass the source-defined verification; missing/failed/pending states retain their distinct outcomes. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.7.4 — Held-out set results evidence reference
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Held-out set results evidence reference rule within promotion_evidence_snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Takes in: ACCEPTED — The recorded held-out results reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Does: ACCEPTED — Verifies the second required evidence source by presence, integrity, authorization and binding; it does not define or score a held-out set. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gives out: ACCEPTED — One verified bound evidence input; all nine are needed for a snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Must never: ACCEPTED — Omit or fabricate this required input, treat it as independently sufficient, or substitute unbound evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — Missing or failed results reject; pending results may hold; no substitute evidence is fabricated. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.3 — B16-2 — Evidence-snapshot verification commit: Presence, integrity, authorization and exact claim/reservation binding must verify before this input is frozen into the snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.7 — promotion_evidence_snapshot | The recorded held-out results reference. | Verifies the second required evidence source by presence, integrity, authorization and binding; it does not define or score a held-out set. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.10.12 — Recovery 12 — B24 acceptance evidence (gold-set / held-out results) missing or failed | The recorded held-out results reference. | Held-out evidence is independently required; gold evidence does not substitute for it. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.7.5 — Manual-inspection record reference
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Manual-inspection record reference rule within promotion_evidence_snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Takes in: ACCEPTED — The recorded manual-inspection outcome under the authorized decision authority. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Does: ACCEPTED — Verifies the recorded inspection and its binding; B16 never performs or scores the inspection. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gives out: ACCEPTED — One verified bound evidence input; all nine are needed for a snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Must never: ACCEPTED — Omit or fabricate this required input, treat it as independently sufficient, or substitute unbound evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — Missing, unreadable, unauthorized or contradictory inspection evidence cannot pass snapshot verification. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.3 — B16-2 — Evidence-snapshot verification commit: Presence, integrity, authorization and exact claim/reservation binding must verify before this input is frozen into the snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.7 — promotion_evidence_snapshot | The recorded manual-inspection outcome under the authorized decision authority. | Verifies the recorded inspection and its binding; B16 never performs or scores the inspection. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.7.6 — promotion_decision_ref
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_decision_ref rule within promotion_evidence_snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Takes in: ACCEPTED — The recorded passing promotion decision under Ness’s authority, bound to this reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Does: ACCEPTED — Verifies the decision exists, is intact and binds this reading; the meaning of passing is not chosen by the mechanical gate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gives out: ACCEPTED — One verified bound evidence input; all nine are needed for a snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Must never: ACCEPTED — Omit or fabricate this required input, treat it as independently sufficient, or substitute unbound evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — An absent or refusing decision cannot pass; missing/pending evidence follows the rejected/held distinction. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.3 — B16-2 — Evidence-snapshot verification commit: Presence, integrity, authorization and exact claim/reservation binding must verify before this input is frozen into the snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.7 — promotion_evidence_snapshot | The recorded passing promotion decision under Ness’s authority, bound to this reading. | Verifies the decision exists, is intact and binds this reading; the meaning of passing is not chosen by the mechanical gate. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.13.2 — Mechanical gate versus semantic judgment | The recorded passing promotion decision under Ness’s authority, bound to this reading. | The mechanical seam requires the recorded passing decision and cannot make the semantic decision itself. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.7.7 — Dual production-authorization evidence
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Dual production-authorization evidence rule within promotion_evidence_snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Takes in: ACCEPTED — Marker-presence verification and the approved specific production-write record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Does: ACCEPTED — Requires both protections: a Ness-only physical marker verification event and the matching approved PROPOSED CHANGE dry-run reference; neither substitutes for the other. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gives out: ACCEPTED — One verified bound evidence input; all nine are needed for a snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Must never: ACCEPTED — Omit or fabricate this required input, treat it as independently sufficient, or substitute unbound evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — Either protection absent means no commit; fail closed with the missing protection named. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.7.7.1 — Marker-presence verification event: Carries the marker check as evidence; the marker is necessary and never sufficient. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.7.7.2 — Approved production-change reference: Carries the second independent protection alongside marker verification. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.5.3 — B16-2 — Evidence-snapshot verification commit: Presence, integrity, authorization and exact claim/reservation binding must verify before this input is frozen into the snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gated by: ACCEPTED — C-READ.5 — Production readings authorization: The marker and specific approval are both required evidence, never substitutes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.7 — promotion_evidence_snapshot | Marker-presence verification and the approved specific production-write record. | Requires both protections: a Ness-only physical marker verification event and the matching approved PROPOSED CHANGE dry-run reference; neither substitutes for the other. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.13.4 — Quarantine and production boundary | Marker-presence verification and the approved specific production-write record. | Both production protections are mandatory; absence of either blocks commit. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |

SUB-PARTS: C-READ.11.7.7.1 — Marker-presence verification event; C-READ.11.7.7.2 — Approved production-change reference

### C-READ.11.7.7.1 — Marker-presence verification event
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Marker-presence verification event member of Dual production-authorization evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Takes in: ACCEPTED — Verification that .nh_readings_production_authorized is physically present. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Does: ACCEPTED — Carries the marker check as evidence; the marker is necessary and never sufficient. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gives out: ACCEPTED — Verification that .nh_readings_production_authorized is physically present. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Must never: ACCEPTED — Create the marker automatically or substitute its presence for specific approval. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — Marker absence prevents promotion commit; the missing protection is named. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.5.1 — Physical production marker: Requires the deliberately created physical production marker; absence blocks commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.7.7 — Dual production-authorization evidence | Verification that .nh_readings_production_authorized is physically present. | Carries the marker check as evidence; the marker is necessary and never sufficient. | Verification that .nh_readings_production_authorized is physically present. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.7.7.2 — Approved production-change reference
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Approved production-change reference member of Dual production-authorization evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Takes in: ACCEPTED — Reference to the approved PROPOSED CHANGE dry-run covering the production write. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Does: ACCEPTED — Carries the second independent protection alongside marker verification. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gives out: ACCEPTED — Reference to the approved PROPOSED CHANGE dry-run covering the production write. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Must never: ACCEPTED — Infer specific approval from the marker or reuse an approval outside its scope. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — Absent approval prevents promotion commit; the missing protection is named. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.5.2 — Specific production-write approval: Requires the approved specific production change; marker presence cannot replace it. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.7.7 — Dual production-authorization evidence | Reference to the approved PROPOSED CHANGE dry-run covering the production write. | Carries the second independent protection alongside marker verification. | Reference to the approved PROPOSED CHANGE dry-run covering the production write. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.7.8 — Privacy and access authorization
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Privacy and access authorization rule within promotion_evidence_snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Takes in: ACCEPTED — The §7Q internal-use authorization for this operation and applicable SACL scope. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Does: ACCEPTED — Requires privacy authorization before relevance and honors the applicable access scope. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gives out: ACCEPTED — One verified bound evidence input; all nine are needed for a snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Must never: ACCEPTED — Omit or fabricate this required input, treat it as independently sufficient, or substitute unbound evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — Unauthorized access rejects or holds according to refusal class; it is never bypassed or retried around. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.3 — B16-2 — Evidence-snapshot verification commit: Presence, integrity, authorization and exact claim/reservation binding must verify before this input is frozen into the snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.7 — promotion_evidence_snapshot | The §7Q internal-use authorization for this operation and applicable SACL scope. | Requires privacy authorization before relevance and honors the applicable access scope. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.7.9 — Hold and dependency check
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Hold and dependency check rule within promotion_evidence_snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Takes in: ACCEPTED — The recorded hold/dependency status of this reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Does: ACCEPTED — If a block exists, resolves dependency_blocked_held; hold release and policy remain with their own governing owners. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gives out: ACCEPTED — One verified bound evidence input; all nine are needed for a snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Must never: ACCEPTED — Omit or fabricate this required input, treat it as independently sufficient, or substitute unbound evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — A held candidate never becomes production by waiting; a block prevents commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.3 — B16-2 — Evidence-snapshot verification commit: Presence, integrity, authorization and exact claim/reservation binding must verify before this input is frozen into the snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.7 — promotion_evidence_snapshot | The recorded hold/dependency status of this reading. | If a block exists, resolves dependency_blocked_held; hold release and policy remain with their own governing owners. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.10.9 — Recovery 9 — Promotion held / dependency-blocked | The recorded hold/dependency status of this reading. | A recorded hold/dependency block prevents promotion; waiting does not clear it. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.10.12.2 — Results pending | The recorded hold/dependency status of this reading. | Pending evidence may hold the attempt; the dependency must actually clear before progress. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.7.10 — Snapshot integrity reference
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Snapshot integrity reference member of promotion_evidence_snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Takes in: ACCEPTED — The snapshot’s own integrity reference; exact field spelling and algorithm not specified. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Does: ACCEPTED — Protects the one immutable claim/reservation-bound reference set against replacement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Gives out: ACCEPTED — The snapshot’s own integrity reference; exact field spelling and algorithm not specified. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Must never: ACCEPTED — Swap evidence after checking or accept a partial/mismatched snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — Integrity mismatch or contradictory bound evidence becomes indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.3 — B16-2 — Evidence-snapshot verification commit: Presence, integrity, authorization and exact claim/reservation binding must verify before this input is frozen into the snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.7 — promotion_evidence_snapshot | The snapshot’s own integrity reference; exact field spelling and algorithm not specified. | Protects the one immutable claim/reservation-bound reference set against replacement. | The snapshot’s own integrity reference; exact field spelling and algorithm not specified. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.8 — Promotion idempotency points
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

ALONE
- What it is: ACCEPTED — Ten distinct duplicate-prevention boundaries. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Takes in: ACCEPTED — Repeated claims, requests, reservations, snapshots, fences, commits, releases, logs and recovery actions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Does: ACCEPTED — Uses each boundary’s own identity and authoritative compare-and-commit or lookup-first result; an attempt identity never replaces the permanent claim. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Gives out: ACCEPTED — At most the one allowed durable result per boundary identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Must never: ACCEPTED — Duplicate a claim, live reservation winner, snapshot, fence winner, eligibility record, recovery release or operation log. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fails closed by: ACCEPTED — An already committed result is absorbed or returned by identity; losing concurrent attempts acquire no second winner. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.8.1 — Promotion claim duplicate prevention: promotion_claim_key — one permanent claim per reading, ever; establishment converges, never duplicates [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.8.2 — Request event duplicate prevention: claim + request identity — repeat requests are lookup-first no-ops returning current derived status [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.8.3 — Reservation (B16-1) duplicate prevention: claim + one compare-and-commit from no-live-reservation; exactly one winner; at most one live reservation per claim [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.8.4 — Evidence snapshot (B16-2) duplicate prevention: claim + reservation identity — one snapshot per reservation; repeat verification finds the committed snapshot [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.8.5 — Commit fence (B16-3 entry) duplicate prevention: reservation identity + one compare-and-commit evidence_checked → commit_fenced; competes with release; exactly one winner ever [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.8.6 — Production-eligibility record (B16-3) duplicate prevention: promotion_claim_key — one record ever per claim; duplicate commit attempts absorb against it [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.8.7 — Recovery release duplicate prevention: reservation identity — at most one recovery_released_no_commit ever; duplicate recovery is a no-op [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.8.8 — Parent terminal log (B16-4) duplicate prevention: promotion_operation_id — exactly one terminal record per parent; child logs are never second parent logs [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.8.9 — Child-operation log duplicate prevention: promotion_child_op_id — exactly one operational log per child; retries locate the existing log by identity [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.8.10 — Recovery run duplicate prevention: recovery_run_id + per-action lookup-first — every repeat is a no-op returning committed findings [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11 — Quarantine-to-production promotion seam | Repeated claims, requests, reservations, snapshots, fences, commits, releases, logs and recovery actions. | Uses each boundary’s own identity and authoritative compare-and-commit or lookup-first result; an attempt identity never replaces the permanent claim. | At most the one allowed durable result per boundary identity. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.3 — Promotion operation identities | Repeated claims, requests, reservations, snapshots, fences, commits, releases, logs and recovery actions. | The operation/claim identities retain their stated uniqueness and separation; an existing log or recovery result is reused, never duplicated. | At most the one allowed durable result per boundary identity. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |

SUB-PARTS: C-READ.11.8.1 — Promotion claim duplicate prevention; C-READ.11.8.2 — Request event duplicate prevention; C-READ.11.8.3 — Reservation (B16-1) duplicate prevention; C-READ.11.8.4 — Evidence snapshot (B16-2) duplicate prevention; C-READ.11.8.5 — Commit fence (B16-3 entry) duplicate prevention; C-READ.11.8.6 — Production-eligibility record (B16-3) duplicate prevention; C-READ.11.8.7 — Recovery release duplicate prevention; C-READ.11.8.8 — Parent terminal log (B16-4) duplicate prevention; C-READ.11.8.9 — Child-operation log duplicate prevention; C-READ.11.8.10 — Recovery run duplicate prevention

### C-READ.11.8.1 — Promotion claim duplicate prevention
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Promotion claim duplicate prevention rule within Promotion idempotency points. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Takes in: ACCEPTED — The proposed boundary action and its existing authoritative identity/history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Does: ACCEPTED — promotion_claim_key — one permanent claim per reading, ever; establishment converges, never duplicates [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Gives out: ACCEPTED — The existing committed result or the single permitted new result. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Must never: ACCEPTED — Commit a second durable result for this same duplicate-prevention identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fails closed by: ACCEPTED — Repeated establishment converges on the one existing permanent claim; it never creates another claim for the reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.2 — promotion_claim: The source-defined permanent or operation identity and its existing committed result determine whether this action may create a new record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.8 — Promotion idempotency points | The proposed boundary action and its existing authoritative identity/history. | promotion_claim_key — one permanent claim per reading, ever; establishment converges, never duplicates | The existing committed result or the single permitted new result. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.8.2 — Request event duplicate prevention
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Request event duplicate prevention rule within Promotion idempotency points. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Takes in: ACCEPTED — The proposed boundary action and its existing authoritative identity/history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Does: ACCEPTED — claim + request identity — repeat requests are lookup-first no-ops returning current derived status [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Gives out: ACCEPTED — The existing committed result or the single permitted new result. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Must never: ACCEPTED — Commit a second durable result for this same duplicate-prevention identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fails closed by: ACCEPTED — Repeated requests look up the existing request identity and return current derived status as a no-op. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.1 — B16-0 — Promotion-status lookup: The source-defined permanent or operation identity and its existing committed result determine whether this action may create a new record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.8 — Promotion idempotency points | The proposed boundary action and its existing authoritative identity/history. | claim + request identity — repeat requests are lookup-first no-ops returning current derived status | The existing committed result or the single permitted new result. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.8.3 — Reservation (B16-1) duplicate prevention
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Reservation (B16-1) duplicate prevention rule within Promotion idempotency points. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Takes in: ACCEPTED — The proposed boundary action and its existing authoritative identity/history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Does: ACCEPTED — claim + one compare-and-commit from no-live-reservation; exactly one winner; at most one live reservation per claim [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Gives out: ACCEPTED — The existing committed result or the single permitted new result. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Must never: ACCEPTED — Commit a second durable result for this same duplicate-prevention identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fails closed by: ACCEPTED — The compare-and-commit admits one reservation winner; losers acquire no second live reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.2 — B16-1 — Atomic promotion reservation: The source-defined permanent or operation identity and its existing committed result determine whether this action may create a new record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.8 — Promotion idempotency points | The proposed boundary action and its existing authoritative identity/history. | claim + one compare-and-commit from no-live-reservation; exactly one winner; at most one live reservation per claim | The existing committed result or the single permitted new result. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.8.4 — Evidence snapshot (B16-2) duplicate prevention
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Evidence snapshot (B16-2) duplicate prevention rule within Promotion idempotency points. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Takes in: ACCEPTED — The proposed boundary action and its existing authoritative identity/history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Does: ACCEPTED — claim + reservation identity — one snapshot per reservation; repeat verification finds the committed snapshot [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Gives out: ACCEPTED — The existing committed result or the single permitted new result. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Must never: ACCEPTED — Commit a second durable result for this same duplicate-prevention identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fails closed by: ACCEPTED — Repeat verification finds the committed snapshot for the same claim and reservation; it does not write another snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.3 — B16-2 — Evidence-snapshot verification commit: The source-defined permanent or operation identity and its existing committed result determine whether this action may create a new record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.8 — Promotion idempotency points | The proposed boundary action and its existing authoritative identity/history. | claim + reservation identity — one snapshot per reservation; repeat verification finds the committed snapshot | The existing committed result or the single permitted new result. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.8.5 — Commit fence (B16-3 entry) duplicate prevention
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Commit fence (B16-3 entry) duplicate prevention rule within Promotion idempotency points. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Takes in: ACCEPTED — The proposed boundary action and its existing authoritative identity/history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Does: ACCEPTED — reservation identity + one compare-and-commit evidence_checked → commit_fenced; competes with release; exactly one winner ever [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Gives out: ACCEPTED — The existing committed result or the single permitted new result. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Must never: ACCEPTED — Commit a second durable result for this same duplicate-prevention identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fails closed by: ACCEPTED — Fence and release compete on one authoritative phase; exactly one wins and the losing action cannot commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.6.8 — Fence versus release single winner: The source-defined permanent or operation identity and its existing committed result determine whether this action may create a new record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.8 — Promotion idempotency points | The proposed boundary action and its existing authoritative identity/history. | reservation identity + one compare-and-commit evidence_checked → commit_fenced; competes with release; exactly one winner ever | The existing committed result or the single permitted new result. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.8.6 — Production-eligibility record (B16-3) duplicate prevention
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Production-eligibility record (B16-3) duplicate prevention rule within Promotion idempotency points. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Takes in: ACCEPTED — The proposed boundary action and its existing authoritative identity/history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Does: ACCEPTED — promotion_claim_key — one record ever per claim; duplicate commit attempts absorb against it [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Gives out: ACCEPTED — The existing committed result or the single permitted new result. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Must never: ACCEPTED — Commit a second durable result for this same duplicate-prevention identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fails closed by: ACCEPTED — Duplicate commit attempts absorb against the one existing eligibility record for the permanent claim. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.4.1 — production_eligibility_record: The source-defined permanent or operation identity and its existing committed result determine whether this action may create a new record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.8 — Promotion idempotency points | The proposed boundary action and its existing authoritative identity/history. | promotion_claim_key — one record ever per claim; duplicate commit attempts absorb against it | The existing committed result or the single permitted new result. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.8.7 — Recovery release duplicate prevention
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery release duplicate prevention rule within Promotion idempotency points. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Takes in: ACCEPTED — The proposed boundary action and its existing authoritative identity/history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Does: ACCEPTED — reservation identity — at most one recovery_released_no_commit ever; duplicate recovery is a no-op [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Gives out: ACCEPTED — The existing committed result or the single permitted new result. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Must never: ACCEPTED — Commit a second durable result for this same duplicate-prevention identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fails closed by: ACCEPTED — Duplicate recovery release is a no-op; at most one recovery_released_no_commit exists per reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.6.7.3 — Strict recovery-only release: The source-defined permanent or operation identity and its existing committed result determine whether this action may create a new record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.8 — Promotion idempotency points | The proposed boundary action and its existing authoritative identity/history. | reservation identity — at most one recovery_released_no_commit ever; duplicate recovery is a no-op | The existing committed result or the single permitted new result. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.8.8 — Parent terminal log (B16-4) duplicate prevention
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Parent terminal log (B16-4) duplicate prevention rule within Promotion idempotency points. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Takes in: ACCEPTED — The proposed boundary action and its existing authoritative identity/history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Does: ACCEPTED — promotion_operation_id — exactly one terminal record per parent; child logs are never second parent logs [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Gives out: ACCEPTED — The existing committed result or the single permitted new result. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Must never: ACCEPTED — Commit a second durable result for this same duplicate-prevention identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fails closed by: ACCEPTED — An existing parent terminal is reused; child logs never become a second terminal for the parent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.12.13 — Parent terminal outcome: The source-defined permanent or operation identity and its existing committed result determine whether this action may create a new record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.8 — Promotion idempotency points | The proposed boundary action and its existing authoritative identity/history. | promotion_operation_id — exactly one terminal record per parent; child logs are never second parent logs | The existing committed result or the single permitted new result. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.3.1 — promotion_operation_id | The proposed boundary action and its existing authoritative identity/history. | The operation/claim identities retain their stated uniqueness and separation; an existing log or recovery result is reused, never duplicated. | The existing committed result or the single permitted new result. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.12.13.1 — promotion_committed parent outcome | The proposed boundary action and its existing authoritative identity/history. | One terminal under this parent operation identity is permitted, with the matching durable outcome before acknowledgement. | The existing committed result or the single permitted new result. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.12.13.2 — promotion_duplicate_absorbed parent outcome | The proposed boundary action and its existing authoritative identity/history. | One terminal under this parent operation identity is permitted, with the matching durable outcome before acknowledgement. | The existing committed result or the single permitted new result. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |
| 5 · ACCEPTED | C-READ.11.12.13.3 — promotion_rejected parent outcome | The proposed boundary action and its existing authoritative identity/history. | One terminal under this parent operation identity is permitted, with the matching durable outcome before acknowledgement. | The existing committed result or the single permitted new result. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |
| 6 · ACCEPTED | C-READ.11.12.13.4 — promotion_interrupted parent outcome | The proposed boundary action and its existing authoritative identity/history. | One terminal under this parent operation identity is permitted, with the matching durable outcome before acknowledgement. | The existing committed result or the single permitted new result. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |
| 7 · ACCEPTED | C-READ.11.12.13.5 — promotion_blocked_held parent outcome | The proposed boundary action and its existing authoritative identity/history. | One terminal under this parent operation identity is permitted, with the matching durable outcome before acknowledgement. | The existing committed result or the single permitted new result. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |
| 8 · ACCEPTED | C-READ.11.12.13.6 — promotion_indeterminate parent outcome | The proposed boundary action and its existing authoritative identity/history. | One terminal under this parent operation identity is permitted, with the matching durable outcome before acknowledgement. | The existing committed result or the single permitted new result. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.8.9 — Child-operation log duplicate prevention
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Child-operation log duplicate prevention rule within Promotion idempotency points. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Takes in: ACCEPTED — The proposed boundary action and its existing authoritative identity/history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Does: ACCEPTED — promotion_child_op_id — exactly one operational log per child; retries locate the existing log by identity [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Gives out: ACCEPTED — The existing committed result or the single permitted new result. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Must never: ACCEPTED — Commit a second durable result for this same duplicate-prevention identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fails closed by: ACCEPTED — Retries locate the child’s existing operational log by promotion_child_op_id and do not append another. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.3.2 — promotion_child_op_id: The source-defined permanent or operation identity and its existing committed result determine whether this action may create a new record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.8 — Promotion idempotency points | The proposed boundary action and its existing authoritative identity/history. | promotion_child_op_id — exactly one operational log per child; retries locate the existing log by identity | The existing committed result or the single permitted new result. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.3.2 — promotion_child_op_id | The proposed boundary action and its existing authoritative identity/history. | The operation/claim identities retain their stated uniqueness and separation; an existing log or recovery result is reused, never duplicated. | The existing committed result or the single permitted new result. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.8.10 — Recovery run duplicate prevention
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery run duplicate prevention rule within Promotion idempotency points. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Takes in: ACCEPTED — The proposed boundary action and its existing authoritative identity/history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Does: ACCEPTED — recovery_run_id + per-action lookup-first — every repeat is a no-op returning committed findings [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Gives out: ACCEPTED — The existing committed result or the single permitted new result. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Must never: ACCEPTED — Commit a second durable result for this same duplicate-prevention identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Fails closed by: ACCEPTED — Repeated recovery returns committed per-action findings as a no-op; it performs no second release, terminal or re-execution. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: The source-defined permanent or operation identity and its existing committed result determine whether this action may create a new record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.8 — Promotion idempotency points | The proposed boundary action and its existing authoritative identity/history. | recovery_run_id + per-action lookup-first — every repeat is a no-op returning committed findings | The existing committed result or the single permitted new result. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.3.3 — recovery_run_id | The proposed boundary action and its existing authoritative identity/history. | The operation/claim identities retain their stated uniqueness and separation; an existing log or recovery result is reused, never duplicated. | The existing committed result or the single permitted new result. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.10.18 — Recovery 18 — Duplicate recovery run | The proposed boundary action and its existing authoritative identity/history. | The same recovery_run_id and per-action committed findings make repeated recovery a no-op. | The existing committed result or the single permitted new result. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.9 — Production-consumption gate
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

ALONE
- What it is: ACCEPTED — The fail-closed boundary on production reasoning, retrieval, state and output use of readings. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Takes in: ACCEPTED — The reading’s derived status and its integrity-checked claim, snapshot and eligibility record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Does: ACCEPTED — Admits a reading only when the complete validated trail proves promotion_committed; requested, reserved, evidence-checked, rejected, held, interrupted and indeterminate candidates are excluded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Gives out: ACCEPTED — Production-use eligibility for a valid committed reading, still subject to privacy and authority. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Must never: ACCEPTED — Allow provisional/partial quarantine influence or infer eligibility from a snapshot, log, index or request. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Fails closed by: ACCEPTED — Excludes non-committed or unprovable candidates by default; a premature use attempt is refused and logged. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.9.3 — Telling promotion inherits by reference: Permits telling production eligibility only through the parent’s committed status; the telling has no independent promotion state and cannot become more promoted than the parent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.9.4 — Promotion records do not establish content truth: Uses the trail as machine-state evidence that promotion occurred; the trail supplies no independent evidence that the reading’s interpretation is correct. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.9.1 — Complete committed-trail requirement: Requires the complete validated trail to derive promotion_committed; no isolated record is sufficient. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.9.2 — Non-committed states excluded: Excludes it from every production reasoning, retrieval, state or output use. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11 — Quarantine-to-production promotion seam | The reading’s derived status and its integrity-checked claim, snapshot and eligibility record. | Admits a reading only when the complete validated trail proves promotion_committed; requested, reserved, evidence-checked, rejected, held, interrupted and indeterminate candidates are excluded. Changes only derived production-use eligibility after a valid commit; all other outcomes keep the reading excluded. | Production-use eligibility for a valid committed reading, still subject to privacy and authority. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.9.3 — Telling promotion inherits by reference | The reading’s derived status and its integrity-checked claim, snapshot and eligibility record. | The parent reading must have valid committed production eligibility before its telling can inherit it. | Production-use eligibility for a valid committed reading, still subject to privacy and authority. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.10.20 — Recovery 20 — Attempted use of a quarantined reading before promotion | The reading’s derived status and its integrity-checked claim, snapshot and eligibility record. | Quarantine remains excluded until the parent’s committed trail validates. | Production-use eligibility for a valid committed reading, still subject to privacy and authority. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: C-READ.11.9.1 — Complete committed-trail requirement; C-READ.11.9.2 — Non-committed states excluded; C-READ.11.9.3 — Telling promotion inherits by reference; C-READ.11.9.4 — Promotion records do not establish content truth

### C-READ.11.9.1 — Complete committed-trail requirement
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Complete committed-trail requirement rule within Production-consumption gate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Takes in: ACCEPTED — Claim + snapshot + production-eligibility record, with each identity and integrity check. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Does: ACCEPTED — Requires the complete validated trail to derive promotion_committed; no isolated record is sufficient. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Gives out: ACCEPTED — Proven committed status or excluded use. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Must never: ACCEPTED — Treat an orphan eligibility record or a snapshot alone as promotion. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Fails closed by: ACCEPTED — Any unreadable, inconsistent or absent required trail keeps consumption excluded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.5.4.1 — production_eligibility_record: Supplies the external committed eligibility record to validate alongside its claim and snapshot. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.7 — promotion_evidence_snapshot: The bound complete snapshot must verify alongside the claim and eligibility record; an isolated record grants nothing. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.9 — Production-consumption gate | Claim + snapshot + production-eligibility record, with each identity and integrity check. | Requires the complete validated trail to derive promotion_committed; no isolated record is sufficient. | Proven committed status or excluded use. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.2.1 — promotion_claim_key | Claim + snapshot + production-eligibility record, with each identity and integrity check. | The preserved binding must participate in the complete validated claim/snapshot/eligibility trail. | Proven committed status or excluded use. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.2.2 — reading_integrity_ref | Claim + snapshot + production-eligibility record, with each identity and integrity check. | The preserved binding must participate in the complete validated claim/snapshot/eligibility trail. | Proven committed status or excluded use. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.2.3 — claim_status_events | Claim + snapshot + production-eligibility record, with each identity and integrity check. | The preserved binding must participate in the complete validated claim/snapshot/eligibility trail. | Proven committed status or excluded use. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |
| 5 · ACCEPTED | C-READ.11.2.4 — reservation_events | Claim + snapshot + production-eligibility record, with each identity and integrity check. | The preserved binding must participate in the complete validated claim/snapshot/eligibility trail. | Proven committed status or excluded use. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |
| 6 · ACCEPTED | C-READ.11.2.5 — evidence_snapshot_ref | Claim + snapshot + production-eligibility record, with each identity and integrity check. | The preserved binding must participate in the complete validated claim/snapshot/eligibility trail. | Proven committed status or excluded use. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |
| 7 · ACCEPTED | C-READ.11.2.6 — production_eligibility_ref / committed refs | Claim + snapshot + production-eligibility record, with each identity and integrity check. | The preserved binding must participate in the complete validated claim/snapshot/eligibility trail. | Proven committed status or excluded use. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |
| 8 · ACCEPTED | C-READ.11.4 — Derived promotion lifecycle | Claim + snapshot + production-eligibility record, with each identity and integrity check. | Only the complete validated committed trail can establish promotion_committed. | Proven committed status or excluded use. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |
| 9 · ACCEPTED | C-READ.11.10.15 — Recovery 15 — Production-eligibility record present without complete promotion evidence (orphan) | Claim + snapshot + production-eligibility record, with each identity and integrity check. | An orphan lacks the complete validated trail and cannot establish production eligibility. | Proven committed status or excluded use. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 10 · ACCEPTED | C-READ.11.10.15.1 — Orphan invalidation event | Claim + snapshot + production-eligibility record, with each identity and integrity check. | An orphan fails the complete-trail requirement and grants no production eligibility. | Proven committed status or excluded use. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 11 · ACCEPTED | C-READ.11.10.15.1.1 — Invalidation cause | Claim + snapshot + production-eligibility record, with each identity and integrity check. | The absent matching trail determines the orphan invalidation cause; it cannot be guessed away. | Proven committed status or excluded use. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 12 · ACCEPTED | C-READ.11.13.6 — No loss or false production result | Claim + snapshot + production-eligibility record, with each identity and integrity check. | Only the complete validated committed trail can establish production eligibility; no false success or guessed record. | Proven committed status or excluded use. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.9.2 — Non-committed states excluded
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Non-committed states excluded rule within Production-consumption gate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Takes in: ACCEPTED — A reading with requested, reserved, evidence-checked, rejected, held, interrupted or indeterminate promotion state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Does: ACCEPTED — Excludes it from every production reasoning, retrieval, state or output use. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Gives out: ACCEPTED — No partial or provisional production influence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Must never: ACCEPTED — Let waiting or repetition of a request promote a reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Fails closed by: ACCEPTED — Refuses and logs the attempted premature use. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.9.2.1 — promotion_requested consumption exclusion: Keeps the reading outside production consumption while in this state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.9.2.2 — promotion_reserved consumption exclusion: Keeps the reading outside production consumption while in this state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.9.2.3 — promotion_evidence_checked consumption exclusion: Keeps the reading outside production consumption while in this state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.9.2.4 — promotion_rejected consumption exclusion: Keeps the reading outside production consumption while in this state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.9.2.5 — dependency_blocked_held consumption exclusion: Keeps the reading outside production consumption while in this state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.9.2.6 — promotion_interrupted consumption exclusion: Keeps the reading outside production consumption while in this state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.9.2.7 — indeterminate_recovery_required consumption exclusion: Keeps the reading outside production consumption while in this state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.4 — Derived promotion lifecycle: The claim-derived non-committed state excludes the reading from production use. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.9 — Production-consumption gate | A reading with requested, reserved, evidence-checked, rejected, held, interrupted or indeterminate promotion state. | Excludes it from every production reasoning, retrieval, state or output use. | No partial or provisional production influence. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |

SUB-PARTS: C-READ.11.9.2.1 — promotion_requested consumption exclusion; C-READ.11.9.2.2 — promotion_reserved consumption exclusion; C-READ.11.9.2.3 — promotion_evidence_checked consumption exclusion; C-READ.11.9.2.4 — promotion_rejected consumption exclusion; C-READ.11.9.2.5 — dependency_blocked_held consumption exclusion; C-READ.11.9.2.6 — promotion_interrupted consumption exclusion; C-READ.11.9.2.7 — indeterminate_recovery_required consumption exclusion

### C-READ.11.9.2.1 — promotion_requested consumption exclusion
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_requested consumption exclusion rule within Non-committed states excluded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Takes in: ACCEPTED — A reading whose derived state is promotion_requested. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Does: ACCEPTED — Keeps the reading outside production consumption while in this state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Gives out: ACCEPTED — Refused use with no production influence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Must never: ACCEPTED — Treat this non-committed state as production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Fails closed by: ACCEPTED — The attempted use is refused and logged. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.4.2 — promotion_requested: The claim-derived state determines that this reading has not completed promotion. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.9.2 — Non-committed states excluded | A reading whose derived state is promotion_requested. | Keeps the reading outside production consumption while in this state. | Refused use with no production influence. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.9.2.2 — promotion_reserved consumption exclusion
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_reserved consumption exclusion rule within Non-committed states excluded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Takes in: ACCEPTED — A reading whose derived state is promotion_reserved. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Does: ACCEPTED — Keeps the reading outside production consumption while in this state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Gives out: ACCEPTED — Refused use with no production influence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Must never: ACCEPTED — Treat this non-committed state as production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Fails closed by: ACCEPTED — The attempted use is refused and logged. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.4.3 — promotion_reserved: The claim-derived state determines that this reading has not completed promotion. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.9.2 — Non-committed states excluded | A reading whose derived state is promotion_reserved. | Keeps the reading outside production consumption while in this state. | Refused use with no production influence. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.9.2.3 — promotion_evidence_checked consumption exclusion
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_evidence_checked consumption exclusion rule within Non-committed states excluded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Takes in: ACCEPTED — A reading whose derived state is promotion_evidence_checked. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Does: ACCEPTED — Keeps the reading outside production consumption while in this state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Gives out: ACCEPTED — Refused use with no production influence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Must never: ACCEPTED — Treat this non-committed state as production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Fails closed by: ACCEPTED — The attempted use is refused and logged. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.4.4 — promotion_evidence_checked: The claim-derived state determines that this reading has not completed promotion. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.9.2 — Non-committed states excluded | A reading whose derived state is promotion_evidence_checked. | Keeps the reading outside production consumption while in this state. | Refused use with no production influence. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.9.2.4 — promotion_rejected consumption exclusion
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_rejected consumption exclusion rule within Non-committed states excluded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Takes in: ACCEPTED — A reading whose derived state is promotion_rejected. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Does: ACCEPTED — Keeps the reading outside production consumption while in this state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Gives out: ACCEPTED — Refused use with no production influence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Must never: ACCEPTED — Treat this non-committed state as production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Fails closed by: ACCEPTED — The attempted use is refused and logged. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.4.6 — promotion_rejected: The claim-derived state determines that this reading has not completed promotion. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.9.2 — Non-committed states excluded | A reading whose derived state is promotion_rejected. | Keeps the reading outside production consumption while in this state. | Refused use with no production influence. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.9.2.5 — dependency_blocked_held consumption exclusion
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

ALONE
- What it is: ACCEPTED — The dependency_blocked_held consumption exclusion rule within Non-committed states excluded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Takes in: ACCEPTED — A reading whose derived state is dependency_blocked_held. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Does: ACCEPTED — Keeps the reading outside production consumption while in this state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Gives out: ACCEPTED — Refused use with no production influence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Must never: ACCEPTED — Treat this non-committed state as production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Fails closed by: ACCEPTED — The attempted use is refused and logged. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.4.7 — dependency_blocked_held: The claim-derived state determines that this reading has not completed promotion. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.9.2 — Non-committed states excluded | A reading whose derived state is dependency_blocked_held. | Keeps the reading outside production consumption while in this state. | Refused use with no production influence. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.9.2.6 — promotion_interrupted consumption exclusion
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_interrupted consumption exclusion rule within Non-committed states excluded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Takes in: ACCEPTED — A reading whose derived state is promotion_interrupted. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Does: ACCEPTED — Keeps the reading outside production consumption while in this state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Gives out: ACCEPTED — Refused use with no production influence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Must never: ACCEPTED — Treat this non-committed state as production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Fails closed by: ACCEPTED — The attempted use is refused and logged. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.4.8 — promotion_interrupted: The claim-derived state determines that this reading has not completed promotion. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.9.2 — Non-committed states excluded | A reading whose derived state is promotion_interrupted. | Keeps the reading outside production consumption while in this state. | Refused use with no production influence. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.9.2.7 — indeterminate_recovery_required consumption exclusion
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

ALONE
- What it is: ACCEPTED — The indeterminate_recovery_required consumption exclusion rule within Non-committed states excluded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Takes in: ACCEPTED — A reading whose derived state is indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Does: ACCEPTED — Keeps the reading outside production consumption while in this state. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Gives out: ACCEPTED — Refused use with no production influence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Must never: ACCEPTED — Treat this non-committed state as production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Fails closed by: ACCEPTED — The attempted use is refused and logged. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.4.9 — indeterminate_recovery_required: The claim-derived state determines that this reading has not completed promotion. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.9.2 — Non-committed states excluded | A reading whose derived state is indeterminate_recovery_required. | Keeps the reading outside production consumption while in this state. | Refused use with no production influence. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.9.3 — Telling promotion inherits by reference
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Telling promotion inherits by reference rule within Production-consumption gate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Takes in: ACCEPTED — A telling and its parent reading’s derived committed status. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Does: ACCEPTED — Permits telling production eligibility only through the parent’s committed status; the telling has no independent promotion state and cannot become more promoted than the parent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Gives out: ACCEPTED — Parent-bound production eligibility without mutating the telling. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Must never: ACCEPTED — Promote a telling independently or before its parent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Fails closed by: ACCEPTED — A non-promoted or unprovable parent keeps telling production use excluded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.10.9 — Telling lifecycle subordination: Carries the parent-derived telling lifecycle contract; no mutable or independent telling promotion state is created. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.9 — Production-consumption gate: The parent reading must have valid committed production eligibility before its telling can inherit it. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.9 — Production-consumption gate | A telling and its parent reading’s derived committed status. | Permits telling production eligibility only through the parent’s committed status; the telling has no independent promotion state and cannot become more promoted than the parent. | Parent-bound production eligibility without mutating the telling. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.9.4 — Promotion records do not establish content truth
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Promotion records do not establish content truth rule within Production-consumption gate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Takes in: ACCEPTED — The claim, snapshot, eligibility record and logs. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Does: ACCEPTED — Uses the trail as machine-state evidence that promotion occurred; the trail supplies no independent evidence that the reading’s interpretation is correct. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Does: DESIGNED — Operational logs remain permanent connected living memory available for authorized retrieval, interpretation and triggered self-examination; their existence never bypasses access restrictions or adds evidential weight. [SOURCE CONFLICT: 04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7 says promotion records are never inputs to interpretation; V10 §0B permits authorized internal retrieval, interpretation and triggered self-examination of operational records] [V10 §0B]
- Gives out: ACCEPTED — Inspectable promotion provenance with no added content certainty. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Must never: ACCEPTED — Count promotion, logging or repeated trail references as independent support for the reading’s content. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]
- Fails closed by: ACCEPTED — Withholds any production-trust shortcut based on mere record existence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: Authorized examination and visible output remain subject to privacy, identity and access restrictions; record existence grants no bypass. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.9 — Production-consumption gate | The claim, snapshot, eligibility record and logs. | Uses the trail as machine-state evidence that promotion occurred; the trail supplies no independent evidence that the reading’s interpretation is correct. | Inspectable promotion provenance with no added content certainty. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10 — Promotion recovery matrix
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — Twenty lookup-first crash/partial-completion and failure cases. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — recovery_run_id and the claim’s committed append-only records, current reservation phase and exact identity/integrity evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Inspects committed events first; resolves by append-only actions under the same permanent claim; never changes the quarantined reading, roots or committed evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — A recovered existing outcome, legal resumed step/release, rejected/held result or indeterminate outcome. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Rewrite or reconstruct a reading/root, delete conflicting evidence, guess success, or duplicate a prior recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Unreadable or contradictory evidence stays indeterminate; non-commit must be proved before strict recovery release; missing terminal prevents success acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.10.1 — Recovery 1 — Crash before any promotion claim/request exists: Nothing to undo; no derived status changed; the next attempt runs B16-0 normally [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.2 — Recovery 2 — Claim/request durable, evidence check absent (reservation may or may not exist): Lookup-first: no reservation → status promotion_requested, next attempt proceeds via B16-1; live reservation in reserved → resume B16-2 under it or release it (legal path 1) and resolve promotion_interrupted [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.3 — Recovery 3 — Evidence snapshot committed, production commit absent: In evidence_checked, resume B16-3 (fence then commit) if the snapshot still validates, or release before fencing and resolve promotion_interrupted. If already commit_fenced, complete from commit evidence or use strict recovery release only with exclusive recovery authority, no possible live executor, checked exact claim/snapshot identities and conclusively proven commit non-existence; any missing proof leaves indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.4 — Recovery 4 — Production-eligibility record present, parent terminal log absent: No success acknowledgement yet. Complete the claim's terminal promotion_committed transition from the record evidence idempotently, then append exactly one missing parent terminal (B16-4); only then acknowledge [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.5 — Recovery 5 — Terminal log present, acknowledgement absent: The outcome is durable and committed: recovery returns the recorded terminal outcome to the caller; nothing is re-executed; no second terminal is written [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.6 — Recovery 6 — Duplicate promotion attempt (same reading, any time): B16-0 absorbs: committed → duplicate_absorbed with the existing eligibility ref; live reservation → promotion_interrupted (claim ref); rejected/held history → returned as derived status; no second claim, reservation-winner, or eligibility record can exist [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.7 — Recovery 7 — Conflicting promotion attempts (race): The B16-1 compare-and-commit admits exactly one reservation winner; losers observe and append nothing; at the commit point, fence-vs-release admits exactly one; conflicting evidence (contradictory records for one claim) → indeterminate_recovery_required, fail closed — no winner guessed [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.8 — Recovery 8 — Promotion rejected: Attempt-terminal with recorded cause; reservation released; the reading remains quarantined; derived status shows the rejection; re-attempt permission is policy (A29/B9, §12) — mechanically a later new request under the same claim, lookup-first [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.9 — Recovery 9 — Promotion held / dependency-blocked: dependency_blocked_held recorded; reservation released or never granted per where the block surfaced; waiting never becomes production; release mechanics/policy stay B-HOLD/A29 [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.10 — Recovery 10 — Quarantined reading missing or unreadable: Fail closed: indeterminate_recovery_required; no commit, no reconstruction, no substitute record; the condition is surfaced; the claim's history is preserved [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.11 — Recovery 11 — Root reference missing or unreadable (a reads id cannot be verified): Evidence check fails → promotion_rejected (recorded cause: unverifiable root reference) or indeterminate_recovery_required if the verification itself cannot be safely read; no root is created, repaired, or guessed; B11's authorities are consulted read-only [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.12 — Recovery 12 — B24 acceptance evidence (gold-set / held-out results) missing or failed: Evidence check fails closed → promotion_rejected with recorded cause, or dependency_blocked_held where the evidence is pending rather than failed; B24's records are never fabricated, inferred, or substituted [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.13 — Recovery 13 — Contradictory evidence (any two bound inputs disagree; snapshot integrity mismatch): indeterminate_recovery_required; fail closed; both versions preserved append-only; no guessing which is correct [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.14 — Recovery 14 — Privacy/access block: Fail closed: the attempt resolves promotion_rejected (cause: unauthorized) or dependency_blocked_held per the refusal class; never bypassed, never retried around the gate; the block event is logged under §7Q's own visibility rules [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.15 — Recovery 15 — Production-eligibility record present without complete promotion evidence (orphan): The record is invalid and grants nothing: derived status is not promotion_committed; production consumption stays excluded; the orphan is marked by an append-only invalidation event with cause; indeterminate_recovery_required pending resolution; nothing is deleted — history preserved [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.16 — Recovery 16 — Promotion evidence present without a production record (snapshot committed, no eligibility record): A committed snapshot alone grants nothing. In evidence_checked, resume B16-3 only if the snapshot still validates, or release before fencing and resolve promotion_interrupted. If already commit_fenced, complete from commit evidence or use strict recovery release only with all four proofs; otherwise indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.17 — Recovery 17 — Post-commit index/coverage incomplete (B16-PR): Committed promotions remain fully valid; rebuild the rebuildable material idempotently; never treat index state as status authority [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.18 — Recovery 18 — Duplicate recovery run: recovery_run_id + lookup-first over append-only events: every repeat is a no-op returning committed findings — no second release, no second terminal, no re-execution [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.19 — Recovery 19 — Attempted promotion of an already production-committed reading: B16-0 absorbs (duplicate_absorbed); no new reservation; the committed record and trail are returned; nothing is re-committed [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.20 — Recovery 20 — Attempted use of a quarantined reading before promotion: The production-consumption gate excludes it fail-closed; the attempt is refused and logged; no partial or provisional influence occurs [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: This operation and its records remain subject to internal-use authorization, privacy visibility and applicable SACL scope. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11 — Quarantine-to-production promotion seam | recovery_run_id and the claim’s committed append-only records, current reservation phase and exact identity/integrity evidence. | Inspects committed events first; resolves by append-only actions under the same permanent claim; never changes the quarantined reading, roots or committed evidence. | A recovered existing outcome, legal resumed step/release, rejected/held result or indeterminate outcome. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: C-READ.11.10.1 — Recovery 1 — Crash before any promotion claim/request exists; C-READ.11.10.2 — Recovery 2 — Claim/request durable, evidence check absent (reservation may or may not exist); C-READ.11.10.3 — Recovery 3 — Evidence snapshot committed, production commit absent; C-READ.11.10.4 — Recovery 4 — Production-eligibility record present, parent terminal log absent; C-READ.11.10.5 — Recovery 5 — Terminal log present, acknowledgement absent; C-READ.11.10.6 — Recovery 6 — Duplicate promotion attempt (same reading, any time); C-READ.11.10.7 — Recovery 7 — Conflicting promotion attempts (race); C-READ.11.10.8 — Recovery 8 — Promotion rejected; C-READ.11.10.9 — Recovery 9 — Promotion held / dependency-blocked; C-READ.11.10.10 — Recovery 10 — Quarantined reading missing or unreadable; C-READ.11.10.11 — Recovery 11 — Root reference missing or unreadable (a reads id cannot be verified); C-READ.11.10.12 — Recovery 12 — B24 acceptance evidence (gold-set / held-out results) missing or failed; C-READ.11.10.13 — Recovery 13 — Contradictory evidence (any two bound inputs disagree; snapshot integrity mismatch); C-READ.11.10.14 — Recovery 14 — Privacy/access block; C-READ.11.10.15 — Recovery 15 — Production-eligibility record present without complete promotion evidence (orphan); C-READ.11.10.16 — Recovery 16 — Promotion evidence present without a production record (snapshot committed, no eligibility record); C-READ.11.10.17 — Recovery 17 — Post-commit index/coverage incomplete (B16-PR); C-READ.11.10.18 — Recovery 18 — Duplicate recovery run; C-READ.11.10.19 — Recovery 19 — Attempted promotion of an already production-committed reading; C-READ.11.10.20 — Recovery 20 — Attempted use of a quarantined reading before promotion

### C-READ.11.10.1 — Recovery 1 — Crash before any promotion claim/request exists
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery 1 — Crash before any promotion claim/request exists rule within Promotion recovery matrix. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Crash before any promotion claim/request exists. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Nothing to undo; no derived status changed; the next attempt runs B16-0 normally [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — The stated recovered outcome; no reading/root history changes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Invent a different result, bypass the stated phase/proof requirement, rewrite preserved history or repeat an already committed recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Nothing to undo; no derived status changed; the next attempt runs B16-0 normally [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.5.1 — B16-0 — Promotion-status lookup: The next attempt begins with lookup-first status resolution; no absent history is reconstructed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10 — Promotion recovery matrix | Crash before any promotion claim/request exists. | Nothing to undo; no derived status changed; the next attempt runs B16-0 normally | The stated recovered outcome; no reading/root history changes. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.2 — Recovery 2 — Claim/request durable, evidence check absent (reservation may or may not exist)
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery 2 — Claim/request durable, evidence check absent (reservation may or may not exist) rule within Promotion recovery matrix. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Claim/request durable, evidence check absent (reservation may or may not exist). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Lookup-first: no reservation → status promotion_requested, next attempt proceeds via B16-1; live reservation in reserved → resume B16-2 under it or release it (legal path 1) and resolve promotion_interrupted [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — The stated recovered outcome; no reading/root history changes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Invent a different result, bypass the stated phase/proof requirement, rewrite preserved history or repeat an already committed recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Lookup-first: no reservation → status promotion_requested, next attempt proceeds via B16-1; live reservation in reserved → resume B16-2 under it or release it (legal path 1) and resolve promotion_interrupted [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.10.2.1 — No reservation: Derives promotion_requested; the next attempt proceeds through B16-1. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.2.2 — Live reserved attempt: Resumes B16-2 under that reservation, or releases legally before fencing and resolves promotion_interrupted. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.6 — Promotion reservation phases and legal transitions: The durable reservation phase decides whether B16-1 may reserve, B16-2 may resume or pre-fence release is legal. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10 — Promotion recovery matrix | Claim/request durable, evidence check absent (reservation may or may not exist). | Lookup-first: no reservation → status promotion_requested, next attempt proceeds via B16-1; live reservation in reserved → resume B16-2 under it or release it (legal path 1) and resolve promotion_interrupted | The stated recovered outcome; no reading/root history changes. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: C-READ.11.10.2.1 — No reservation; C-READ.11.10.2.2 — Live reserved attempt

### C-READ.11.10.2.1 — No reservation
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The No reservation rule within Recovery 2 — Claim/request durable, evidence check absent (reservation may or may not exist). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — The request is durable and no reservation exists. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Derives promotion_requested; the next attempt proceeds through B16-1. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — Derives promotion_requested; the next attempt proceeds through B16-1. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Bypass the recorded outcome, invent missing evidence or mutate existing reading/root history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Derives promotion_requested; the next attempt proceeds through B16-1. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.2 — B16-1 — Atomic promotion reservation: No live reservation is required before B16-1 can admit one winner. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10.2 — Recovery 2 — Claim/request durable, evidence check absent (reservation may or may not exist) | The request is durable and no reservation exists. | Derives promotion_requested; the next attempt proceeds through B16-1. | Derives promotion_requested; the next attempt proceeds through B16-1. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.2.2 — Live reserved attempt
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Live reserved attempt rule within Recovery 2 — Claim/request durable, evidence check absent (reservation may or may not exist). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — A live reservation is in reserved. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Resumes B16-2 under that reservation, or releases legally before fencing and resolves promotion_interrupted. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — Resumes B16-2 under that reservation, or releases legally before fencing and resolves promotion_interrupted. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Bypass the recorded outcome, invent missing evidence or mutate existing reading/root history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Resumes B16-2 under that reservation, or releases legally before fencing and resolves promotion_interrupted. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.6 — Promotion reservation phases and legal transitions: Only a live reserved attempt may resume evidence checking; normal release remains pre-fence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10.2 — Recovery 2 — Claim/request durable, evidence check absent (reservation may or may not exist) | A live reservation is in reserved. | Resumes B16-2 under that reservation, or releases legally before fencing and resolves promotion_interrupted. | Resumes B16-2 under that reservation, or releases legally before fencing and resolves promotion_interrupted. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.3 — Recovery 3 — Evidence snapshot committed, production commit absent
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery 3 — Evidence snapshot committed, production commit absent rule within Promotion recovery matrix. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Evidence snapshot committed, production commit absent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — In evidence_checked, resume B16-3 (fence then commit) if the snapshot still validates, or release before fencing and resolve promotion_interrupted. If already commit_fenced, complete from commit evidence or use strict recovery release only with exclusive recovery authority, no possible live executor, checked exact claim/snapshot identities and conclusively proven commit non-existence; any missing proof leaves indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gives out: ACCEPTED — The stated recovered outcome; no reading/root history changes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Invent a different result, bypass the stated phase/proof requirement, rewrite preserved history or repeat an already committed recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — In evidence_checked, resume B16-3 (fence then commit) if the snapshot still validates, or release before fencing and resolve promotion_interrupted. If already commit_fenced, complete from commit evidence or use strict recovery release only with exclusive recovery authority, no possible live executor, checked exact claim/snapshot identities and conclusively proven commit non-existence; any missing proof leaves indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.10.3.1 — Snapshot validates before fencing: Resumes B16-3 by winning the fence before commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.3.2 — Pre-fence release: Appends released and resolves promotion_interrupted; that reservation can never commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.3.3 — Already fenced recovery: Completes from existing commit evidence; otherwise only the strict four-proof recovery release is legal, and any missing proof leaves indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.6.7.3 — Strict recovery-only release: A fenced non-commit release requires all four strict proofs; otherwise recovery stays indeterminate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10 — Promotion recovery matrix | Evidence snapshot committed, production commit absent. | In evidence_checked, resume B16-3 (fence then commit) if the snapshot still validates, or release before fencing and resolve promotion_interrupted. If already commit_fenced, complete from commit evidence or use strict recovery release only with exclusive recovery authority, no possible live executor, checked exact claim/snapshot identities and conclusively proven commit non-existence; any missing proof leaves indeterminate_recovery_required. | The stated recovered outcome; no reading/root history changes. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |

SUB-PARTS: C-READ.11.10.3.1 — Snapshot validates before fencing; C-READ.11.10.3.2 — Pre-fence release; C-READ.11.10.3.3 — Already fenced recovery

### C-READ.11.10.3.1 — Snapshot validates before fencing
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Snapshot validates before fencing rule within Recovery 3 — Evidence snapshot committed, production commit absent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — The reservation is evidence_checked and its snapshot still validates. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Resumes B16-3 by winning the fence before commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — Resumes B16-3 by winning the fence before commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Bypass the recorded outcome, invent missing evidence or mutate existing reading/root history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Resumes B16-3 by winning the fence before commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.4 — B16-3 — Production-eligibility commit: The snapshot must still validate and the commit fence must be won before commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10.3 — Recovery 3 — Evidence snapshot committed, production commit absent | The reservation is evidence_checked and its snapshot still validates. | Resumes B16-3 by winning the fence before commit. | Resumes B16-3 by winning the fence before commit. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.3.2 — Pre-fence release
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Pre-fence release rule within Recovery 3 — Evidence snapshot committed, production commit absent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — The reservation is evidence_checked and normal release wins. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Appends released and resolves promotion_interrupted; that reservation can never commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — Appends released and resolves promotion_interrupted; that reservation can never commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Bypass the recorded outcome, invent missing evidence or mutate existing reading/root history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Appends released and resolves promotion_interrupted; that reservation can never commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.6.7.1 — Normal reservation release: Normal release is legal only before the fence and permanently bars that reservation from commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10.3 — Recovery 3 — Evidence snapshot committed, production commit absent | The reservation is evidence_checked and normal release wins. | Appends released and resolves promotion_interrupted; that reservation can never commit. | Appends released and resolves promotion_interrupted; that reservation can never commit. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.3.3 — Already fenced recovery
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Already fenced recovery rule within Recovery 3 — Evidence snapshot committed, production commit absent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — The reservation is commit_fenced. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Completes from existing commit evidence; otherwise only the strict four-proof recovery release is legal, and any missing proof leaves indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gives out: ACCEPTED — Completes from existing commit evidence; otherwise only the strict four-proof recovery release is legal, and any missing proof leaves indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Must never: ACCEPTED — Bypass the recorded outcome, invent missing evidence or mutate existing reading/root history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Completes from existing commit evidence; otherwise only the strict four-proof recovery release is legal, and any missing proof leaves indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.6.7.3 — Strict recovery-only release: Fenced recovery without commit requires all four strict release proofs or stays indeterminate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10.3 — Recovery 3 — Evidence snapshot committed, production commit absent | The reservation is commit_fenced. | Completes from existing commit evidence; otherwise only the strict four-proof recovery release is legal, and any missing proof leaves indeterminate_recovery_required. | Completes from existing commit evidence; otherwise only the strict four-proof recovery release is legal, and any missing proof leaves indeterminate_recovery_required. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.4 — Recovery 4 — Production-eligibility record present, parent terminal log absent
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery 4 — Production-eligibility record present, parent terminal log absent rule within Promotion recovery matrix. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Production-eligibility record present, parent terminal log absent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — No success acknowledgement yet. Complete the claim's terminal promotion_committed transition from the record evidence idempotently, then append exactly one missing parent terminal (B16-4); only then acknowledge [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — The stated recovered outcome; no reading/root history changes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Invent a different result, bypass the stated phase/proof requirement, rewrite preserved history or repeat an already committed recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — No success acknowledgement yet. Complete the claim's terminal promotion_committed transition from the record evidence idempotently, then append exactly one missing parent terminal (B16-4); only then acknowledge [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.12.13 — Parent terminal outcome: The missing parent terminal must become durable before success acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10 — Promotion recovery matrix | Production-eligibility record present, parent terminal log absent. | No success acknowledgement yet. Complete the claim's terminal promotion_committed transition from the record evidence idempotently, then append exactly one missing parent terminal (B16-4); only then acknowledge | The stated recovered outcome; no reading/root history changes. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.5 — Recovery 5 — Terminal log present, acknowledgement absent
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery 5 — Terminal log present, acknowledgement absent rule within Promotion recovery matrix. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Terminal log present, acknowledgement absent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — The outcome is durable and committed: recovery returns the recorded terminal outcome to the caller; nothing is re-executed; no second terminal is written [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — The stated recovered outcome; no reading/root history changes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Invent a different result, bypass the stated phase/proof requirement, rewrite preserved history or repeat an already committed recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — The outcome is durable and committed: recovery returns the recorded terminal outcome to the caller; nothing is re-executed; no second terminal is written [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.12.13 — Parent terminal outcome: Only the already durable terminal outcome is returned; no operation or second terminal is recreated. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10 — Promotion recovery matrix | Terminal log present, acknowledgement absent. | The outcome is durable and committed: recovery returns the recorded terminal outcome to the caller; nothing is re-executed; no second terminal is written | The stated recovered outcome; no reading/root history changes. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.6 — Recovery 6 — Duplicate promotion attempt (same reading, any time)
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery 6 — Duplicate promotion attempt (same reading, any time) rule within Promotion recovery matrix. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Duplicate promotion attempt (same reading, any time). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — B16-0 absorbs: committed → duplicate_absorbed with the existing eligibility ref; live reservation → promotion_interrupted (claim ref); rejected/held history → returned as derived status; no second claim, reservation-winner, or eligibility record can exist [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — The stated recovered outcome; no reading/root history changes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Invent a different result, bypass the stated phase/proof requirement, rewrite preserved history or repeat an already committed recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — B16-0 absorbs: committed → duplicate_absorbed with the existing eligibility ref; live reservation → promotion_interrupted (claim ref); rejected/held history → returned as derived status; no second claim, reservation-winner, or eligibility record can exist [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.10.6.1 — Committed duplicate: Returns duplicate_absorbed with the existing eligibility reference; no new reservation or eligibility record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.6.2 — Live reservation duplicate: Returns promotion_interrupted with the claim reference; no second reservation winner. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.6.3 — Rejected or held history: Returns the derived status; any later permitted attempt remains lookup-first under this same claim. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.5.1 — B16-0 — Promotion-status lookup: The existing committed, live-reserved, rejected or held state is looked up before any new action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10 — Promotion recovery matrix | Duplicate promotion attempt (same reading, any time). | B16-0 absorbs: committed → duplicate_absorbed with the existing eligibility ref; live reservation → promotion_interrupted (claim ref); rejected/held history → returned as derived status; no second claim, reservation-winner, or eligibility record can exist | The stated recovered outcome; no reading/root history changes. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: C-READ.11.10.6.1 — Committed duplicate; C-READ.11.10.6.2 — Live reservation duplicate; C-READ.11.10.6.3 — Rejected or held history

### C-READ.11.10.6.1 — Committed duplicate
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Committed duplicate rule within Recovery 6 — Duplicate promotion attempt (same reading, any time). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — The same reading is already committed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Returns duplicate_absorbed with the existing eligibility reference; no new reservation or eligibility record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — Returns duplicate_absorbed with the existing eligibility reference; no new reservation or eligibility record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Bypass the recorded outcome, invent missing evidence or mutate existing reading/root history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Returns duplicate_absorbed with the existing eligibility reference; no new reservation or eligibility record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.1 — B16-0 — Promotion-status lookup: A validated committed promotion is absorbed at lookup; no new reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10.6 — Recovery 6 — Duplicate promotion attempt (same reading, any time) | The same reading is already committed. | Returns duplicate_absorbed with the existing eligibility reference; no new reservation or eligibility record. | Returns duplicate_absorbed with the existing eligibility reference; no new reservation or eligibility record. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.6.2 — Live reservation duplicate
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Live reservation duplicate rule within Recovery 6 — Duplicate promotion attempt (same reading, any time). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Another live reservation owns the claim. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Returns promotion_interrupted with the claim reference; no second reservation winner. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — Returns promotion_interrupted with the claim reference; no second reservation winner. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Bypass the recorded outcome, invent missing evidence or mutate existing reading/root history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Returns promotion_interrupted with the claim reference; no second reservation winner. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.2 — B16-1 — Atomic promotion reservation: Another live reservation excludes a second reservation winner. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10.6 — Recovery 6 — Duplicate promotion attempt (same reading, any time) | Another live reservation owns the claim. | Returns promotion_interrupted with the claim reference; no second reservation winner. | Returns promotion_interrupted with the claim reference; no second reservation winner. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.6.3 — Rejected or held history
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Rejected or held history rule within Recovery 6 — Duplicate promotion attempt (same reading, any time). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — The permanent claim carries rejected or held history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Returns the derived status; any later permitted attempt remains lookup-first under this same claim. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — Returns the derived status; any later permitted attempt remains lookup-first under this same claim. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Bypass the recorded outcome, invent missing evidence or mutate existing reading/root history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Returns the derived status; any later permitted attempt remains lookup-first under this same claim. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.2 — promotion_claim: Rejected/held history remains on the one permanent claim and cannot be bypassed by a second claim. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10.6 — Recovery 6 — Duplicate promotion attempt (same reading, any time) | The permanent claim carries rejected or held history. | Returns the derived status; any later permitted attempt remains lookup-first under this same claim. | Returns the derived status; any later permitted attempt remains lookup-first under this same claim. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.7 — Recovery 7 — Conflicting promotion attempts (race)
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery 7 — Conflicting promotion attempts (race) rule within Promotion recovery matrix. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Conflicting promotion attempts (race). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — The B16-1 compare-and-commit admits exactly one reservation winner; losers observe and append nothing; at the commit point, fence-vs-release admits exactly one; conflicting evidence (contradictory records for one claim) → indeterminate_recovery_required, fail closed — no winner guessed [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — The stated recovered outcome; no reading/root history changes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Invent a different result, bypass the stated phase/proof requirement, rewrite preserved history or repeat an already committed recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — The B16-1 compare-and-commit admits exactly one reservation winner; losers observe and append nothing; at the commit point, fence-vs-release admits exactly one; conflicting evidence (contradictory records for one claim) → indeterminate_recovery_required, fail closed — no winner guessed [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.10.7.1 — Reservation race loser: Exactly one reservation wins; losers observe and append no competing reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.7.2 — Fence-release race loser: Exactly one wins; the losing action has no commit right. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.7.3 — Contradictory race evidence: Returns indeterminate_recovery_required, preserves both records and guesses no winner. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.6.8 — Fence versus release single winner: One compare-and-commit winner is required; contradictory records never select a guessed winner. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10 — Promotion recovery matrix | Conflicting promotion attempts (race). | The B16-1 compare-and-commit admits exactly one reservation winner; losers observe and append nothing; at the commit point, fence-vs-release admits exactly one; conflicting evidence (contradictory records for one claim) → indeterminate_recovery_required, fail closed — no winner guessed | The stated recovered outcome; no reading/root history changes. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: C-READ.11.10.7.1 — Reservation race loser; C-READ.11.10.7.2 — Fence-release race loser; C-READ.11.10.7.3 — Contradictory race evidence

### C-READ.11.10.7.1 — Reservation race loser
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Reservation race loser rule within Recovery 7 — Conflicting promotion attempts (race). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Two attempts race B16-1. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Exactly one reservation wins; losers observe and append no competing reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — Exactly one reservation wins; losers observe and append no competing reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Bypass the recorded outcome, invent missing evidence or mutate existing reading/root history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Exactly one reservation wins; losers observe and append no competing reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.5.2 — B16-1 — Atomic promotion reservation: Exactly one reservation compare-and-commit wins. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10.7 — Recovery 7 — Conflicting promotion attempts (race) | Two attempts race B16-1. | Exactly one reservation wins; losers observe and append no competing reservation. | Exactly one reservation wins; losers observe and append no competing reservation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.7.2 — Fence-release race loser
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Fence-release race loser rule within Recovery 7 — Conflicting promotion attempts (race). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Fencing and release compete on the authoritative phase. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Exactly one wins; the losing action has no commit right. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — Exactly one wins; the losing action has no commit right. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Bypass the recorded outcome, invent missing evidence or mutate existing reading/root history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Exactly one wins; the losing action has no commit right. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.6.8 — Fence versus release single winner: Fence and release have exactly one authoritative winner. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10.7 — Recovery 7 — Conflicting promotion attempts (race) | Fencing and release compete on the authoritative phase. | Exactly one wins; the losing action has no commit right. | Exactly one wins; the losing action has no commit right. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.7.3 — Contradictory race evidence
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Contradictory race evidence rule within Recovery 7 — Conflicting promotion attempts (race). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Records for the same claim contradict each other. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Returns indeterminate_recovery_required, preserves both records and guesses no winner. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — Returns indeterminate_recovery_required, preserves both records and guesses no winner. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Bypass the recorded outcome, invent missing evidence or mutate existing reading/root history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Returns indeterminate_recovery_required, preserves both records and guesses no winner. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.7 — promotion_evidence_snapshot: Contradictory evidence prevents a provable snapshot/commit result. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10.7 — Recovery 7 — Conflicting promotion attempts (race) | Records for the same claim contradict each other. | Returns indeterminate_recovery_required, preserves both records and guesses no winner. | Returns indeterminate_recovery_required, preserves both records and guesses no winner. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.8 — Recovery 8 — Promotion rejected
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery 8 — Promotion rejected rule within Promotion recovery matrix. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Promotion rejected. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Attempt-terminal with recorded cause; reservation released; the reading remains quarantined; derived status shows the rejection; re-attempt permission is policy (A29/B9, §12) — mechanically a later new request under the same claim, lookup-first [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — The stated recovered outcome; no reading/root history changes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Invent a different result, bypass the stated phase/proof requirement, rewrite preserved history or repeat an already committed recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Attempt-terminal with recorded cause; reservation released; the reading remains quarantined; derived status shows the rejection; re-attempt permission is policy (A29/B9, §12) — mechanically a later new request under the same claim, lookup-first [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.2 — promotion_claim: Any later policy-permitted request uses the same permanent claim and its recorded history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10 — Promotion recovery matrix | Promotion rejected. | Attempt-terminal with recorded cause; reservation released; the reading remains quarantined; derived status shows the rejection; re-attempt permission is policy (A29/B9, §12) — mechanically a later new request under the same claim, lookup-first | The stated recovered outcome; no reading/root history changes. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.9 — Recovery 9 — Promotion held / dependency-blocked
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery 9 — Promotion held / dependency-blocked rule within Promotion recovery matrix. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Promotion held / dependency-blocked. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — dependency_blocked_held recorded; reservation released or never granted per where the block surfaced; waiting never becomes production; release mechanics/policy stay B-HOLD/A29 [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — The stated recovered outcome; no reading/root history changes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Invent a different result, bypass the stated phase/proof requirement, rewrite preserved history or repeat an already committed recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — dependency_blocked_held recorded; reservation released or never granted per where the block surfaced; waiting never becomes production; release mechanics/policy stay B-HOLD/A29 [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.7.9 — Hold and dependency check: A recorded hold/dependency block prevents promotion; waiting does not clear it. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10 — Promotion recovery matrix | Promotion held / dependency-blocked. | dependency_blocked_held recorded; reservation released or never granted per where the block surfaced; waiting never becomes production; release mechanics/policy stay B-HOLD/A29 | The stated recovered outcome; no reading/root history changes. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.10 — Recovery 10 — Quarantined reading missing or unreadable
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery 10 — Quarantined reading missing or unreadable rule within Promotion recovery matrix. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Quarantined reading missing or unreadable. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Fail closed: indeterminate_recovery_required; no commit, no reconstruction, no substitute record; the condition is surfaced; the claim's history is preserved [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — The stated recovered outcome; no reading/root history changes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Invent a different result, bypass the stated phase/proof requirement, rewrite preserved history or repeat an already committed recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Fail closed: indeterminate_recovery_required; no commit, no reconstruction, no substitute record; the condition is surfaced; the claim's history is preserved [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.7.1 — Reading identity and integrity: A missing or unreadable quarantined reading cannot supply verified identity/integrity evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10 — Promotion recovery matrix | Quarantined reading missing or unreadable. | Fail closed: indeterminate_recovery_required; no commit, no reconstruction, no substitute record; the condition is surfaced; the claim's history is preserved | The stated recovered outcome; no reading/root history changes. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.11 — Recovery 11 — Root reference missing or unreadable (a reads id cannot be verified)
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery 11 — Root reference missing or unreadable (a reads id cannot be verified) rule within Promotion recovery matrix. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Root reference missing or unreadable (a reads id cannot be verified). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Evidence check fails → promotion_rejected (recorded cause: unverifiable root reference) or indeterminate_recovery_required if the verification itself cannot be safely read; no root is created, repaired, or guessed; B11's authorities are consulted read-only [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — The stated recovered outcome; no reading/root history changes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Invent a different result, bypass the stated phase/proof requirement, rewrite preserved history or repeat an already committed recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Evidence check fails → promotion_rejected (recorded cause: unverifiable root reference) or indeterminate_recovery_required if the verification itself cannot be safely read; no root is created, repaired, or guessed; B11's authorities are consulted read-only [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.10.11.1 — Unverifiable root identity: Rejects promotion with cause unverifiable root reference; no root is created, repaired or guessed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.11.2 — Unreadable root verification: Returns indeterminate_recovery_required; B11 authorities remain read-only. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.7.2 — Read-only root references: Each referenced root must verify by identity; missing or unreadable verification cannot pass. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10 — Promotion recovery matrix | Root reference missing or unreadable (a reads id cannot be verified). | Evidence check fails → promotion_rejected (recorded cause: unverifiable root reference) or indeterminate_recovery_required if the verification itself cannot be safely read; no root is created, repaired, or guessed; B11's authorities are consulted read-only | The stated recovered outcome; no reading/root history changes. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: C-READ.11.10.11.1 — Unverifiable root identity; C-READ.11.10.11.2 — Unreadable root verification

### C-READ.11.10.11.1 — Unverifiable root identity
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Unverifiable root identity rule within Recovery 11 — Root reference missing or unreadable (a reads id cannot be verified). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — A referenced root cannot be verified to exist. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Rejects promotion with cause unverifiable root reference; no root is created, repaired or guessed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — Rejects promotion with cause unverifiable root reference; no root is created, repaired or guessed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Bypass the recorded outcome, invent missing evidence or mutate existing reading/root history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Rejects promotion with cause unverifiable root reference; no root is created, repaired or guessed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.7.2 — Read-only root references: All root references must be verified by identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10.11 — Recovery 11 — Root reference missing or unreadable (a reads id cannot be verified) | A referenced root cannot be verified to exist. | Rejects promotion with cause unverifiable root reference; no root is created, repaired or guessed. | Rejects promotion with cause unverifiable root reference; no root is created, repaired or guessed. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.11.2 — Unreadable root verification
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Unreadable root verification rule within Recovery 11 — Root reference missing or unreadable (a reads id cannot be verified). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — The verification itself cannot be safely read. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Returns indeterminate_recovery_required; B11 authorities remain read-only. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — Returns indeterminate_recovery_required; B11 authorities remain read-only. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Bypass the recorded outcome, invent missing evidence or mutate existing reading/root history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Returns indeterminate_recovery_required; B11 authorities remain read-only. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.7.2 — Read-only root references: Unreadable root verification cannot pass as established existence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10.11 — Recovery 11 — Root reference missing or unreadable (a reads id cannot be verified) | The verification itself cannot be safely read. | Returns indeterminate_recovery_required; B11 authorities remain read-only. | Returns indeterminate_recovery_required; B11 authorities remain read-only. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.12 — Recovery 12 — B24 acceptance evidence (gold-set / held-out results) missing or failed
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery 12 — B24 acceptance evidence (gold-set / held-out results) missing or failed rule within Promotion recovery matrix. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — B24 acceptance evidence (gold-set / held-out results) missing or failed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Evidence check fails closed → promotion_rejected with recorded cause, or dependency_blocked_held where the evidence is pending rather than failed; B24's records are never fabricated, inferred, or substituted [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — The stated recovered outcome; no reading/root history changes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Invent a different result, bypass the stated phase/proof requirement, rewrite preserved history or repeat an already committed recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Evidence check fails closed → promotion_rejected with recorded cause, or dependency_blocked_held where the evidence is pending rather than failed; B24's records are never fabricated, inferred, or substituted [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.10.12.1 — Missing or failed results: Fails closed as promotion_rejected with the recorded cause; no fabricated or substituted evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.12.2 — Results pending: May resolve dependency_blocked_held; waiting grants no production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.7.3 — Gold-set results evidence reference: Required gold-results evidence must exist and pass the source-defined verification; missing/failed/pending states retain their distinct outcomes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.7.4 — Held-out set results evidence reference: Held-out evidence is independently required; gold evidence does not substitute for it. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10 — Promotion recovery matrix | B24 acceptance evidence (gold-set / held-out results) missing or failed. | Evidence check fails closed → promotion_rejected with recorded cause, or dependency_blocked_held where the evidence is pending rather than failed; B24's records are never fabricated, inferred, or substituted | The stated recovered outcome; no reading/root history changes. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: C-READ.11.10.12.1 — Missing or failed results; C-READ.11.10.12.2 — Results pending

### C-READ.11.10.12.1 — Missing or failed results
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Missing or failed results rule within Recovery 12 — B24 acceptance evidence (gold-set / held-out results) missing or failed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Required gold/held-out results are missing or failed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Fails closed as promotion_rejected with the recorded cause; no fabricated or substituted evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — Fails closed as promotion_rejected with the recorded cause; no fabricated or substituted evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Bypass the recorded outcome, invent missing evidence or mutate existing reading/root history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Fails closed as promotion_rejected with the recorded cause; no fabricated or substituted evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.7 — promotion_evidence_snapshot: The complete mandatory evidence set must verify; missing or failed results cannot pass. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10.12 — Recovery 12 — B24 acceptance evidence (gold-set / held-out results) missing or failed | Required gold/held-out results are missing or failed. | Fails closed as promotion_rejected with the recorded cause; no fabricated or substituted evidence. | Fails closed as promotion_rejected with the recorded cause; no fabricated or substituted evidence. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.12.2 — Results pending
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Results pending rule within Recovery 12 — B24 acceptance evidence (gold-set / held-out results) missing or failed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — The required evidence is pending rather than failed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — May resolve dependency_blocked_held; waiting grants no production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — May resolve dependency_blocked_held; waiting grants no production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Bypass the recorded outcome, invent missing evidence or mutate existing reading/root history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — May resolve dependency_blocked_held; waiting grants no production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.7.9 — Hold and dependency check: Pending evidence may hold the attempt; the dependency must actually clear before progress. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10.12 — Recovery 12 — B24 acceptance evidence (gold-set / held-out results) missing or failed | The required evidence is pending rather than failed. | May resolve dependency_blocked_held; waiting grants no production eligibility. | May resolve dependency_blocked_held; waiting grants no production eligibility. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.13 — Recovery 13 — Contradictory evidence (any two bound inputs disagree; snapshot integrity mismatch)
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery 13 — Contradictory evidence (any two bound inputs disagree; snapshot integrity mismatch) rule within Promotion recovery matrix. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Contradictory evidence (any two bound inputs disagree; snapshot integrity mismatch). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — indeterminate_recovery_required; fail closed; both versions preserved append-only; no guessing which is correct [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — The stated recovered outcome; no reading/root history changes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Invent a different result, bypass the stated phase/proof requirement, rewrite preserved history or repeat an already committed recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — indeterminate_recovery_required; fail closed; both versions preserved append-only; no guessing which is correct [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.7 — promotion_evidence_snapshot: Contradictory bound inputs or snapshot integrity mismatch cannot establish a valid evidence set. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10 — Promotion recovery matrix | Contradictory evidence (any two bound inputs disagree; snapshot integrity mismatch). | indeterminate_recovery_required; fail closed; both versions preserved append-only; no guessing which is correct | The stated recovered outcome; no reading/root history changes. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.14 — Recovery 14 — Privacy/access block
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery 14 — Privacy/access block rule within Promotion recovery matrix. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Privacy/access block. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Fail closed: the attempt resolves promotion_rejected (cause: unauthorized) or dependency_blocked_held per the refusal class; never bypassed, never retried around the gate; the block event is logged under §7Q's own visibility rules [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — The stated recovered outcome; no reading/root history changes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Invent a different result, bypass the stated phase/proof requirement, rewrite preserved history or repeat an already committed recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Fail closed: the attempt resolves promotion_rejected (cause: unauthorized) or dependency_blocked_held per the refusal class; never bypassed, never retried around the gate; the block event is logged under §7Q's own visibility rules [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.10.14.1 — Unauthorized rejection: Records promotion_rejected with unauthorized cause; the block event obeys §7Q visibility rules. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.14.2 — Unauthorized held outcome: Records dependency_blocked_held; no bypass or retry around the privacy/access gate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: The §7Q/SACL refusal class controls rejection or held waiting; the gate is never bypassed or retried around. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10 — Promotion recovery matrix | Privacy/access block. | Fail closed: the attempt resolves promotion_rejected (cause: unauthorized) or dependency_blocked_held per the refusal class; never bypassed, never retried around the gate; the block event is logged under §7Q's own visibility rules | The stated recovered outcome; no reading/root history changes. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: C-READ.11.10.14.1 — Unauthorized rejection; C-READ.11.10.14.2 — Unauthorized held outcome

### C-READ.11.10.14.1 — Unauthorized rejection
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Unauthorized rejection rule within Recovery 14 — Privacy/access block. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — The §7Q/SACL refusal class requires rejection. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Records promotion_rejected with unauthorized cause; the block event obeys §7Q visibility rules. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — Records promotion_rejected with unauthorized cause; the block event obeys §7Q visibility rules. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Bypass the recorded outcome, invent missing evidence or mutate existing reading/root history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Records promotion_rejected with unauthorized cause; the block event obeys §7Q visibility rules. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: The privacy/access refusal class requires rejection with its protected block record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10.14 — Recovery 14 — Privacy/access block | The §7Q/SACL refusal class requires rejection. | Records promotion_rejected with unauthorized cause; the block event obeys §7Q visibility rules. | Records promotion_rejected with unauthorized cause; the block event obeys §7Q visibility rules. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.14.2 — Unauthorized held outcome
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Unauthorized held outcome rule within Recovery 14 — Privacy/access block. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — The refusal class requires a dependency hold. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Records dependency_blocked_held; no bypass or retry around the privacy/access gate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — Records dependency_blocked_held; no bypass or retry around the privacy/access gate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Bypass the recorded outcome, invent missing evidence or mutate existing reading/root history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Records dependency_blocked_held; no bypass or retry around the privacy/access gate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: The privacy/access refusal class may hold the attempt; no retry bypass exists. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10.14 — Recovery 14 — Privacy/access block | The refusal class requires a dependency hold. | Records dependency_blocked_held; no bypass or retry around the privacy/access gate. | Records dependency_blocked_held; no bypass or retry around the privacy/access gate. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.15 — Recovery 15 — Production-eligibility record present without complete promotion evidence (orphan)
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery 15 — Production-eligibility record present without complete promotion evidence (orphan) rule within Promotion recovery matrix. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Production-eligibility record present without complete promotion evidence (orphan). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — The record is invalid and grants nothing: derived status is not promotion_committed; production consumption stays excluded; the orphan is marked by an append-only invalidation event with cause; indeterminate_recovery_required pending resolution; nothing is deleted — history preserved [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — The stated recovered outcome; no reading/root history changes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Invent a different result, bypass the stated phase/proof requirement, rewrite preserved history or repeat an already committed recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — The record is invalid and grants nothing: derived status is not promotion_committed; production consumption stays excluded; the orphan is marked by an append-only invalidation event with cause; indeterminate_recovery_required pending resolution; nothing is deleted — history preserved [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.10.15.1 — Orphan invalidation event: Appends an invalidation event with the orphan cause; retains the orphan and every earlier record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.9.1 — Complete committed-trail requirement: An orphan lacks the complete validated trail and cannot establish production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10 — Promotion recovery matrix | Production-eligibility record present without complete promotion evidence (orphan). | The record is invalid and grants nothing: derived status is not promotion_committed; production consumption stays excluded; the orphan is marked by an append-only invalidation event with cause; indeterminate_recovery_required pending resolution; nothing is deleted — history preserved | The stated recovered outcome; no reading/root history changes. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: C-READ.11.10.15.1 — Orphan invalidation event

### C-READ.11.10.15.1 — Orphan invalidation event
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Orphan invalidation event rule within Recovery 15 — Production-eligibility record present without complete promotion evidence (orphan). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — An eligibility record without its complete matching promotion trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Appends an invalidation event with the orphan cause; retains the orphan and every earlier record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — Invalid eligibility, no production consumption and indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Delete the orphan or let it establish promotion_committed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — The record grants nothing and production consumption stays excluded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.10.15.1.1 — Invalidation cause: Explains why this orphan grants nothing without deleting it. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.9.1 — Complete committed-trail requirement: An orphan fails the complete-trail requirement and grants no production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10.15 — Recovery 15 — Production-eligibility record present without complete promotion evidence (orphan) | An eligibility record without its complete matching promotion trail. | Appends an invalidation event with the orphan cause; retains the orphan and every earlier record. | Invalid eligibility, no production consumption and indeterminate_recovery_required. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: C-READ.11.10.15.1.1 — Invalidation cause

### C-READ.11.10.15.1.1 — Invalidation cause
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Invalidation cause member of Orphan invalidation event. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — The recorded cause that the eligibility record lacks its complete claim/evidence trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Explains why this orphan grants nothing without deleting it. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — The recorded cause that the eligibility record lacks its complete claim/evidence trail. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Omit the cause or replace the incomplete trail with guessed evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — The orphan remains invalid and recovery indeterminate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.9.1 — Complete committed-trail requirement: The absent matching trail determines the orphan invalidation cause; it cannot be guessed away. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10.15.1 — Orphan invalidation event | The recorded cause that the eligibility record lacks its complete claim/evidence trail. | Explains why this orphan grants nothing without deleting it. | The recorded cause that the eligibility record lacks its complete claim/evidence trail. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.16 — Recovery 16 — Promotion evidence present without a production record (snapshot committed, no eligibility record)
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery 16 — Promotion evidence present without a production record (snapshot committed, no eligibility record) rule within Promotion recovery matrix. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Promotion evidence present without a production record (snapshot committed, no eligibility record). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — A committed snapshot alone grants nothing. In evidence_checked, resume B16-3 only if the snapshot still validates, or release before fencing and resolve promotion_interrupted. If already commit_fenced, complete from commit evidence or use strict recovery release only with all four proofs; otherwise indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gives out: ACCEPTED — The stated recovered outcome; no reading/root history changes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Invent a different result, bypass the stated phase/proof requirement, rewrite preserved history or repeat an already committed recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — A committed snapshot alone grants nothing. In evidence_checked, resume B16-3 only if the snapshot still validates, or release before fencing and resolve promotion_interrupted. If already commit_fenced, complete from commit evidence or use strict recovery release only with all four proofs; otherwise indeterminate_recovery_required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.10.16.1 — Evidence-checked resume or release: Resumes fenced commit only while the snapshot remains valid, or releases before fencing and resolves promotion_interrupted. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.10.16.2 — Fenced snapshot without eligibility: Uses commit evidence if it exists; otherwise requires all four strict recovery-release proofs, or stays indeterminate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.6.7.3 — Strict recovery-only release: A fenced non-commit release requires all four strict proofs; otherwise recovery stays indeterminate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10 — Promotion recovery matrix | Promotion evidence present without a production record (snapshot committed, no eligibility record). | A committed snapshot alone grants nothing. In evidence_checked, resume B16-3 only if the snapshot still validates, or release before fencing and resolve promotion_interrupted. If already commit_fenced, complete from commit evidence or use strict recovery release only with all four proofs; otherwise indeterminate_recovery_required. | The stated recovered outcome; no reading/root history changes. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |

SUB-PARTS: C-READ.11.10.16.1 — Evidence-checked resume or release; C-READ.11.10.16.2 — Fenced snapshot without eligibility

### C-READ.11.10.16.1 — Evidence-checked resume or release
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Evidence-checked resume or release rule within Recovery 16 — Promotion evidence present without a production record (snapshot committed, no eligibility record). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — A complete snapshot exists in evidence_checked with no eligibility record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Resumes fenced commit only while the snapshot remains valid, or releases before fencing and resolves promotion_interrupted. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — Resumes fenced commit only while the snapshot remains valid, or releases before fencing and resolves promotion_interrupted. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Bypass the recorded outcome, invent missing evidence or mutate existing reading/root history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Resumes fenced commit only while the snapshot remains valid, or releases before fencing and resolves promotion_interrupted. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.6 — Promotion reservation phases and legal transitions: Only evidence_checked permits ordinary resume or pre-fence release; the snapshot must still validate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10.16 — Recovery 16 — Promotion evidence present without a production record (snapshot committed, no eligibility record) | A complete snapshot exists in evidence_checked with no eligibility record. | Resumes fenced commit only while the snapshot remains valid, or releases before fencing and resolves promotion_interrupted. | Resumes fenced commit only while the snapshot remains valid, or releases before fencing and resolves promotion_interrupted. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.16.2 — Fenced snapshot without eligibility
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Fenced snapshot without eligibility rule within Recovery 16 — Promotion evidence present without a production record (snapshot committed, no eligibility record). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — A snapshot exists and the reservation is commit_fenced. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Uses commit evidence if it exists; otherwise requires all four strict recovery-release proofs, or stays indeterminate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Gives out: ACCEPTED — Uses commit evidence if it exists; otherwise requires all four strict recovery-release proofs, or stays indeterminate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Must never: ACCEPTED — Bypass the recorded outcome, invent missing evidence or mutate existing reading/root history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Uses commit evidence if it exists; otherwise requires all four strict recovery-release proofs, or stays indeterminate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.6.7.3 — Strict recovery-only release: A fenced no-commit release requires all four conclusive proofs; otherwise recovery stays indeterminate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10.16 — Recovery 16 — Promotion evidence present without a production record (snapshot committed, no eligibility record) | A snapshot exists and the reservation is commit_fenced. | Uses commit evidence if it exists; otherwise requires all four strict recovery-release proofs, or stays indeterminate. | Uses commit evidence if it exists; otherwise requires all four strict recovery-release proofs, or stays indeterminate. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.17 — Recovery 17 — Post-commit index/coverage incomplete (B16-PR)
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery 17 — Post-commit index/coverage incomplete (B16-PR) rule within Promotion recovery matrix. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Post-commit index/coverage incomplete (B16-PR). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Committed promotions remain fully valid; rebuild the rebuildable material idempotently; never treat index state as status authority [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — The stated recovered outcome; no reading/root history changes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Invent a different result, bypass the stated phase/proof requirement, rewrite preserved history or repeat an already committed recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — Committed promotions remain fully valid; rebuild the rebuildable material idempotently; never treat index state as status authority [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.5.4.1 — production_eligibility_record: Validated committed eligibility remains the authority; incomplete rebuildable indexes cannot invalidate it. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10 — Promotion recovery matrix | Post-commit index/coverage incomplete (B16-PR). | Committed promotions remain fully valid; rebuild the rebuildable material idempotently; never treat index state as status authority | The stated recovered outcome; no reading/root history changes. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.18 — Recovery 18 — Duplicate recovery run
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery 18 — Duplicate recovery run rule within Promotion recovery matrix. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Duplicate recovery run. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — recovery_run_id + lookup-first over append-only events: every repeat is a no-op returning committed findings — no second release, no second terminal, no re-execution [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — The stated recovered outcome; no reading/root history changes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Invent a different result, bypass the stated phase/proof requirement, rewrite preserved history or repeat an already committed recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — recovery_run_id + lookup-first over append-only events: every repeat is a no-op returning committed findings — no second release, no second terminal, no re-execution [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.8.10 — Recovery run duplicate prevention: The same recovery_run_id and per-action committed findings make repeated recovery a no-op. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10 — Promotion recovery matrix | Duplicate recovery run. | recovery_run_id + lookup-first over append-only events: every repeat is a no-op returning committed findings — no second release, no second terminal, no re-execution | The stated recovered outcome; no reading/root history changes. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.19 — Recovery 19 — Attempted promotion of an already production-committed reading
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery 19 — Attempted promotion of an already production-committed reading rule within Promotion recovery matrix. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Attempted promotion of an already production-committed reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — B16-0 absorbs (duplicate_absorbed); no new reservation; the committed record and trail are returned; nothing is re-committed [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — The stated recovered outcome; no reading/root history changes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Invent a different result, bypass the stated phase/proof requirement, rewrite preserved history or repeat an already committed recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — B16-0 absorbs (duplicate_absorbed); no new reservation; the committed record and trail are returned; nothing is re-committed [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.5.1 — B16-0 — Promotion-status lookup: An already committed promotion is absorbed before any new reservation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10 — Promotion recovery matrix | Attempted promotion of an already production-committed reading. | B16-0 absorbs (duplicate_absorbed); no new reservation; the committed record and trail are returned; nothing is re-committed | The stated recovered outcome; no reading/root history changes. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.10.20 — Recovery 20 — Attempted use of a quarantined reading before promotion
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Recovery 20 — Attempted use of a quarantined reading before promotion rule within Promotion recovery matrix. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Attempted use of a quarantined reading before promotion. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — The production-consumption gate excludes it fail-closed; the attempt is refused and logged; no partial or provisional influence occurs [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — The stated recovered outcome; no reading/root history changes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Invent a different result, bypass the stated phase/proof requirement, rewrite preserved history or repeat an already committed recovery action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fails closed by: ACCEPTED — The production-consumption gate excludes it fail-closed; the attempt is refused and logged; no partial or provisional influence occurs [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.3.3 — recovery_run_id: Uses recovery_run_id and per-action lookup-first checks; duplicate recovery returns committed findings. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.9 — Production-consumption gate: Quarantine remains excluded until the parent’s committed trail validates. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.10 — Promotion recovery matrix | Attempted use of a quarantined reading before promotion. | The production-consumption gate excludes it fail-closed; the attempt is refused and logged; no partial or provisional influence occurs | The stated recovered outcome; no reading/root history changes. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.11 — Promotion fail-closed conditions
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

ALONE
- What it is: ACCEPTED — Ten named conditions that prevent unsafe snapshot, commit or production consumption. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Takes in: ACCEPTED — Required evidence, authorization, dependency and durable-state checks. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Does: ACCEPTED — Applies the source-defined outcome per failure class and records the named condition; missing inputs never produce a partial pass. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Gives out: ACCEPTED — Rejection, held waiting, indeterminate state, refused commit or excluded use, as applicable. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Must never: ACCEPTED — Treat an absent or unprovable condition as passed, bypass access, or create production as a side effect. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — Fails closed at the affected snapshot/commit/use boundary with the named cause. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.11.1 — Evidence missing (any §5.3 input absent): No snapshot; promotion_rejected (recorded cause) or dependency_blocked_held where pending; never a partial pass [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.11.2 — Evidence contradictory: indeterminate_recovery_required; no guessing [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.11.3 — Evidence unreadable: indeterminate_recovery_required; fail closed until provable [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.11.4 — Evidence unauthorized: Refuses the unauthorized operation; resolves promotion_rejected with unauthorized cause or dependency_blocked_held according to refusal class. Never bypasses or retries around the gate; the block log obeys §7Q visibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.11.5 — Hold / dependency block recorded: dependency_blocked_held; waiting never becomes production [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.11.6 — Dual authorization incomplete (marker absent or dry-run approval absent): No commit — MUST-NEVER; fail closed with the missing protection named [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.11.7 — Claim events / snapshot / eligibility record unreadable: Derived status unprovable → indeterminate_recovery_required; production consumption stays excluded [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.11.8 — Orphan production-eligibility record: The orphan is invalid and grants nothing; production consumption remains excluded, an append-only invalidation event records the cause, and recovery is indeterminate; history remains preserved. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.11.9 — Commit attempted without durable fence, or with claim/snapshot mismatch: Refused and logged; nothing commits [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.11.10 — Production store absent (it is, by design): B16 never creates, writes to, or authorizes it; eligibility is a record, not a store write [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11 — Quarantine-to-production promotion seam | Required evidence, authorization, dependency and durable-state checks. | Applies the source-defined outcome per failure class and records the named condition; missing inputs never produce a partial pass. | Rejection, held waiting, indeterminate state, refused commit or excluded use, as applicable. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.11.1 — Evidence missing (any §5.3 input absent) | Required evidence, authorization, dependency and durable-state checks. | The named missing/failed condition determines its fail-closed outcome; it cannot be treated as passed. | Rejection, held waiting, indeterminate state, refused commit or excluded use, as applicable. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.11.2 — Evidence contradictory | Required evidence, authorization, dependency and durable-state checks. | The named missing/failed condition determines its fail-closed outcome; it cannot be treated as passed. | Rejection, held waiting, indeterminate state, refused commit or excluded use, as applicable. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.11.3 — Evidence unreadable | Required evidence, authorization, dependency and durable-state checks. | The named missing/failed condition determines its fail-closed outcome; it cannot be treated as passed. | Rejection, held waiting, indeterminate state, refused commit or excluded use, as applicable. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] |
| 5 · ACCEPTED | C-READ.11.11.4 — Evidence unauthorized | Required evidence, authorization, dependency and durable-state checks. | The named missing/failed condition determines its fail-closed outcome; it cannot be treated as passed. | Rejection, held waiting, indeterminate state, refused commit or excluded use, as applicable. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] |
| 6 · ACCEPTED | C-READ.11.11.5 — Hold / dependency block recorded | Required evidence, authorization, dependency and durable-state checks. | The named missing/failed condition determines its fail-closed outcome; it cannot be treated as passed. | Rejection, held waiting, indeterminate state, refused commit or excluded use, as applicable. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] |
| 7 · ACCEPTED | C-READ.11.11.6 — Dual authorization incomplete (marker absent or dry-run approval absent) | Required evidence, authorization, dependency and durable-state checks. | The named missing/failed condition determines its fail-closed outcome; it cannot be treated as passed. | Rejection, held waiting, indeterminate state, refused commit or excluded use, as applicable. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] |
| 8 · ACCEPTED | C-READ.11.11.7 — Claim events / snapshot / eligibility record unreadable | Required evidence, authorization, dependency and durable-state checks. | The named missing/failed condition determines its fail-closed outcome; it cannot be treated as passed. | Rejection, held waiting, indeterminate state, refused commit or excluded use, as applicable. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] |
| 9 · ACCEPTED | C-READ.11.11.8 — Orphan production-eligibility record | Required evidence, authorization, dependency and durable-state checks. | The named missing/failed condition determines its fail-closed outcome; it cannot be treated as passed. | Rejection, held waiting, indeterminate state, refused commit or excluded use, as applicable. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] |
| 10 · ACCEPTED | C-READ.11.11.9 — Commit attempted without durable fence, or with claim/snapshot mismatch | Required evidence, authorization, dependency and durable-state checks. | The named missing/failed condition determines its fail-closed outcome; it cannot be treated as passed. | Rejection, held waiting, indeterminate state, refused commit or excluded use, as applicable. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] |

SUB-PARTS: C-READ.11.11.1 — Evidence missing (any §5.3 input absent); C-READ.11.11.2 — Evidence contradictory; C-READ.11.11.3 — Evidence unreadable; C-READ.11.11.4 — Evidence unauthorized; C-READ.11.11.5 — Hold / dependency block recorded; C-READ.11.11.6 — Dual authorization incomplete (marker absent or dry-run approval absent); C-READ.11.11.7 — Claim events / snapshot / eligibility record unreadable; C-READ.11.11.8 — Orphan production-eligibility record; C-READ.11.11.9 — Commit attempted without durable fence, or with claim/snapshot mismatch; C-READ.11.11.10 — Production store absent (it is, by design)

### C-READ.11.11.1 — Evidence missing (any §5.3 input absent)
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Evidence missing (any §5.3 input absent) rule within Promotion fail-closed conditions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Takes in: ACCEPTED — Evidence missing (any §5.3 input absent). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Does: ACCEPTED — No snapshot; promotion_rejected (recorded cause) or dependency_blocked_held where pending; never a partial pass [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Gives out: ACCEPTED — No snapshot; promotion_rejected (recorded cause) or dependency_blocked_held where pending; never a partial pass [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Must never: ACCEPTED — Treat this failing condition as successful, guess missing evidence or bypass the required protection. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — No snapshot; promotion_rejected (recorded cause) or dependency_blocked_held where pending; never a partial pass [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.11 — Promotion fail-closed conditions: The named missing/failed condition determines its fail-closed outcome; it cannot be treated as passed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.11 — Promotion fail-closed conditions | Evidence missing (any §5.3 input absent). | No snapshot; promotion_rejected (recorded cause) or dependency_blocked_held where pending; never a partial pass | No snapshot; promotion_rejected (recorded cause) or dependency_blocked_held where pending; never a partial pass | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.11.2 — Evidence contradictory
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Evidence contradictory rule within Promotion fail-closed conditions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Takes in: ACCEPTED — Evidence contradictory. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Does: ACCEPTED — indeterminate_recovery_required; no guessing [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Gives out: ACCEPTED — indeterminate_recovery_required; no guessing [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Must never: ACCEPTED — Treat this failing condition as successful, guess missing evidence or bypass the required protection. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — indeterminate_recovery_required; no guessing [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.11 — Promotion fail-closed conditions: The named missing/failed condition determines its fail-closed outcome; it cannot be treated as passed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.11 — Promotion fail-closed conditions | Evidence contradictory. | indeterminate_recovery_required; no guessing | indeterminate_recovery_required; no guessing | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.11.3 — Evidence unreadable
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Evidence unreadable rule within Promotion fail-closed conditions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Takes in: ACCEPTED — Evidence unreadable. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Does: ACCEPTED — indeterminate_recovery_required; fail closed until provable [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Gives out: ACCEPTED — indeterminate_recovery_required; fail closed until provable [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Must never: ACCEPTED — Treat this failing condition as successful, guess missing evidence or bypass the required protection. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — indeterminate_recovery_required; fail closed until provable [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.11 — Promotion fail-closed conditions: The named missing/failed condition determines its fail-closed outcome; it cannot be treated as passed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.11 — Promotion fail-closed conditions | Evidence unreadable. | indeterminate_recovery_required; fail closed until provable | indeterminate_recovery_required; fail closed until provable | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.11.4 — Evidence unauthorized
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Evidence unauthorized rule within Promotion fail-closed conditions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Evidence unauthorized. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — Refuses the unauthorized operation; resolves promotion_rejected with unauthorized cause or dependency_blocked_held according to refusal class. Never bypasses or retries around the gate; the block log obeys §7Q visibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — Refuses the unauthorized operation; resolves promotion_rejected with unauthorized cause or dependency_blocked_held according to refusal class. Never bypasses or retries around the gate; the block log obeys §7Q visibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Treat this failing condition as successful, guess missing evidence or bypass the required protection. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — Refuses the unauthorized operation; resolves promotion_rejected with unauthorized cause or dependency_blocked_held according to refusal class. Never bypasses or retries around the gate; the block log obeys §7Q visibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.11 — Promotion fail-closed conditions: The named missing/failed condition determines its fail-closed outcome; it cannot be treated as passed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.11 — Promotion fail-closed conditions | Evidence unauthorized. | Refuses the unauthorized operation; resolves promotion_rejected with unauthorized cause or dependency_blocked_held according to refusal class. Never bypasses or retries around the gate; the block log obeys §7Q visibility. | Refuses the unauthorized operation; resolves promotion_rejected with unauthorized cause or dependency_blocked_held according to refusal class. Never bypasses or retries around the gate; the block log obeys §7Q visibility. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.11.5 — Hold / dependency block recorded
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Hold / dependency block recorded rule within Promotion fail-closed conditions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Takes in: ACCEPTED — Hold / dependency block recorded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Does: ACCEPTED — dependency_blocked_held; waiting never becomes production [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Gives out: ACCEPTED — dependency_blocked_held; waiting never becomes production [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Must never: ACCEPTED — Treat this failing condition as successful, guess missing evidence or bypass the required protection. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — dependency_blocked_held; waiting never becomes production [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.11 — Promotion fail-closed conditions: The named missing/failed condition determines its fail-closed outcome; it cannot be treated as passed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.11 — Promotion fail-closed conditions | Hold / dependency block recorded. | dependency_blocked_held; waiting never becomes production | dependency_blocked_held; waiting never becomes production | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.11.6 — Dual authorization incomplete (marker absent or dry-run approval absent)
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Dual authorization incomplete (marker absent or dry-run approval absent) rule within Promotion fail-closed conditions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Takes in: ACCEPTED — Dual authorization incomplete (marker absent or dry-run approval absent). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Does: ACCEPTED — No commit — MUST-NEVER; fail closed with the missing protection named [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Gives out: ACCEPTED — No commit — MUST-NEVER; fail closed with the missing protection named [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Must never: ACCEPTED — Treat this failing condition as successful, guess missing evidence or bypass the required protection. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — No commit — MUST-NEVER; fail closed with the missing protection named [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.11 — Promotion fail-closed conditions: The named missing/failed condition determines its fail-closed outcome; it cannot be treated as passed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.11 — Promotion fail-closed conditions | Dual authorization incomplete (marker absent or dry-run approval absent). | No commit — MUST-NEVER; fail closed with the missing protection named | No commit — MUST-NEVER; fail closed with the missing protection named | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.11.7 — Claim events / snapshot / eligibility record unreadable
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Claim events / snapshot / eligibility record unreadable rule within Promotion fail-closed conditions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Takes in: ACCEPTED — Claim events / snapshot / eligibility record unreadable. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Does: ACCEPTED — Derived status unprovable → indeterminate_recovery_required; production consumption stays excluded [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Gives out: ACCEPTED — Derived status unprovable → indeterminate_recovery_required; production consumption stays excluded [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Must never: ACCEPTED — Treat this failing condition as successful, guess missing evidence or bypass the required protection. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — Derived status unprovable → indeterminate_recovery_required; production consumption stays excluded [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.11 — Promotion fail-closed conditions: The named missing/failed condition determines its fail-closed outcome; it cannot be treated as passed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.11 — Promotion fail-closed conditions | Claim events / snapshot / eligibility record unreadable. | Derived status unprovable → indeterminate_recovery_required; production consumption stays excluded | Derived status unprovable → indeterminate_recovery_required; production consumption stays excluded | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.11.8 — Orphan production-eligibility record
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Orphan production-eligibility record rule within Promotion fail-closed conditions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Takes in: ACCEPTED — Orphan production-eligibility record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Does: ACCEPTED — The orphan is invalid and grants nothing; production consumption remains excluded, an append-only invalidation event records the cause, and recovery is indeterminate; history remains preserved. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Gives out: ACCEPTED — The orphan is invalid and grants nothing; production consumption remains excluded, an append-only invalidation event records the cause, and recovery is indeterminate; history remains preserved. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]
- Must never: ACCEPTED — Treat this failing condition as successful, guess missing evidence or bypass the required protection. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — The orphan is invalid and grants nothing; production consumption remains excluded, an append-only invalidation event records the cause, and recovery is indeterminate; history remains preserved. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.11 — Promotion fail-closed conditions: The named missing/failed condition determines its fail-closed outcome; it cannot be treated as passed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.11 — Promotion fail-closed conditions | Orphan production-eligibility record. | The orphan is invalid and grants nothing; production consumption remains excluded, an append-only invalidation event records the cause, and recovery is indeterminate; history remains preserved. | The orphan is invalid and grants nothing; production consumption remains excluded, an append-only invalidation event records the cause, and recovery is indeterminate; history remains preserved. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.11.9 — Commit attempted without durable fence, or with claim/snapshot mismatch
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Commit attempted without durable fence, or with claim/snapshot mismatch rule within Promotion fail-closed conditions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Takes in: ACCEPTED — Commit attempted without durable fence, or with claim/snapshot mismatch. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Does: ACCEPTED — Refused and logged; nothing commits [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Gives out: ACCEPTED — Refused and logged; nothing commits [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Must never: ACCEPTED — Treat this failing condition as successful, guess missing evidence or bypass the required protection. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — Refused and logged; nothing commits [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.11 — Promotion fail-closed conditions: The named missing/failed condition determines its fail-closed outcome; it cannot be treated as passed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.11 — Promotion fail-closed conditions | Commit attempted without durable fence, or with claim/snapshot mismatch. | Refused and logged; nothing commits | Refused and logged; nothing commits | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.11.10 — Production store absent (it is, by design)
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Production store absent (it is, by design) rule within Promotion fail-closed conditions. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Takes in: ACCEPTED — Production store absent (it is, by design). [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Does: ACCEPTED — B16 never creates, writes to, or authorizes it; eligibility is a record, not a store write [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Gives out: ACCEPTED — B16 never creates, writes to, or authorizes it; eligibility is a record, not a store write [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Must never: ACCEPTED — Create, write to or authorize a production store through B16; an eligibility record is not a production-store write. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]
- Fails closed by: ACCEPTED — B16 never creates, writes to, or authorizes it; eligibility is a record, not a store write [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.13.4 — Quarantine and production boundary: B16 has no production-store creation/write authority; recording eligibility does not cross that boundary. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.11 — Promotion fail-closed conditions | Production store absent (it is, by design). | B16 never creates, writes to, or authorizes it; eligibility is a record, not a store write | B16 never creates, writes to, or authorizes it; eligibility is a record, not a store write | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12 — Promotion operation records
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — One permanent append-only operational log per real operation, distinct from canonical transaction/state records. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — The stable parent or child operation identity and structural claim/reading/snapshot/result references. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — Logs each real operation once under its own identity. Canonical claim events, phase events, snapshots and eligibility records establish machine state but are not additional §0B logs. B16-4 is the sole parent terminal; no log-about-logging chain is generated. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — Connected operation history, with no copied root/reading payload or extra evidential votes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Use a child log as a second parent log, log twice under one operation id, copy content, bypass privacy or strengthen the interpretation merely by logging. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — A missing parent terminal withholds acknowledgement until recovery appends that one terminal; existing logs are located by identity instead of duplicated. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.12.1 — promotion_requested operation log: Records the durable request event under the lookup/establishment child identity where that operation acts. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.2 — promotion_claim_reserved operation log: Records the single winning B16-1 reservation grant; losing observations resolve into the losers’ own parent terminals. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.3 — promotion_evidence_checked operation log: Records the B16-2 snapshot commit once, carrying all bound references. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.4 — promotion_committed operation log: Records the B16-3 fence win, eligibility-record append and claim terminal together as one atomic operation with one child log. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.5 — promotion_rejected operation log: Records the rejection outcome and its cause class. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.6 — promotion_interrupted operation log: Records pre-commit termination with durable evidence of non-commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.7 — promotion_indeterminate operation log: Records the fail-closed indeterminate resolution. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.8 — promotion_blocked_held operation log: Records the dependency/hold block; its release policy remains with the hold/dependency owner. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.9 — promotion_duplicate_absorbed operation log: Records B16-0 absorption against an already committed promotion. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.10 — recovery_applied operation log: Records applied append-only recovery actions under recovery_run_id and the stable recovery child identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.11 — recovery_noop operation log: Records lookup-only recovery resolution returning committed findings without re-executing an already resolved action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.12 — fail_closed_event operation log: Records the fail-closed occurrence with its named missing or failed condition. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.13 — Parent terminal outcome: Durably records exactly one of promotion_committed, promotion_duplicate_absorbed, promotion_rejected, promotion_interrupted, promotion_blocked_held, promotion_indeterminate, before acknowledging the caller. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.14 — Operation-record identity and payload boundary: Links by operation, claim and reading identities only; never copies root or reading content. Active/cold lifecycle follows the governing living-record law. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.15 — No recursive logs or double evidence: One real operation receives one log. Creating that log generates none; a genuinely separate later operation may receive its own. State/log repetition never strengthens the reading’s meaning or truth. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: This operation and its records remain subject to internal-use authorization, privacy visibility and applicable SACL scope. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11 — Quarantine-to-production promotion seam | The stable parent or child operation identity and structural claim/reading/snapshot/result references. | Logs each real operation once under its own identity. Canonical claim events, phase events, snapshots and eligibility records establish machine state but are not additional §0B logs. B16-4 is the sole parent terminal; no log-about-logging chain is generated. | Connected operation history, with no copied root/reading payload or extra evidential votes. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: C-READ.11.12.1 — promotion_requested operation log; C-READ.11.12.2 — promotion_claim_reserved operation log; C-READ.11.12.3 — promotion_evidence_checked operation log; C-READ.11.12.4 — promotion_committed operation log; C-READ.11.12.5 — promotion_rejected operation log; C-READ.11.12.6 — promotion_interrupted operation log; C-READ.11.12.7 — promotion_indeterminate operation log; C-READ.11.12.8 — promotion_blocked_held operation log; C-READ.11.12.9 — promotion_duplicate_absorbed operation log; C-READ.11.12.10 — recovery_applied operation log; C-READ.11.12.11 — recovery_noop operation log; C-READ.11.12.12 — fail_closed_event operation log; C-READ.11.12.13 — Parent terminal outcome; C-READ.11.12.14 — Operation-record identity and payload boundary; C-READ.11.12.15 — No recursive logs or double evidence

### C-READ.11.12.1 — promotion_requested operation log
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_requested operation log rule within Promotion operation records. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — The real operation’s stable identity, parent/claim/reading references and recorded outcome. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — Records the durable request event under the lookup/establishment child identity where that operation acts. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — Exactly one permanent operational record for that operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Duplicate the operation log, confuse canonical state with an extra log, copy private payload or count the log as new content evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — Refuses unauthorized use or disclosure of the log under the applicable privacy/access rules; retries locate its existing operation log instead of writing a duplicate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12 — Promotion operation records | The real operation’s stable identity, parent/claim/reading references and recorded outcome. | Records the durable request event under the lookup/establishment child identity where that operation acts. | Exactly one permanent operational record for that operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12.2 — promotion_claim_reserved operation log
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_claim_reserved operation log rule within Promotion operation records. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — The real operation’s stable identity, parent/claim/reading references and recorded outcome. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — Records the single winning B16-1 reservation grant; losing observations resolve into the losers’ own parent terminals. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — Exactly one permanent operational record for that operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Duplicate the operation log, confuse canonical state with an extra log, copy private payload or count the log as new content evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — Refuses unauthorized use or disclosure of the log under the applicable privacy/access rules; retries locate its existing operation log instead of writing a duplicate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12 — Promotion operation records | The real operation’s stable identity, parent/claim/reading references and recorded outcome. | Records the single winning B16-1 reservation grant; losing observations resolve into the losers’ own parent terminals. | Exactly one permanent operational record for that operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12.3 — promotion_evidence_checked operation log
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_evidence_checked operation log rule within Promotion operation records. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — The real operation’s stable identity, parent/claim/reading references and recorded outcome. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — Records the B16-2 snapshot commit once, carrying all bound references. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — Exactly one permanent operational record for that operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Duplicate the operation log, confuse canonical state with an extra log, copy private payload or count the log as new content evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — Refuses unauthorized use or disclosure of the log under the applicable privacy/access rules; retries locate its existing operation log instead of writing a duplicate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12 — Promotion operation records | The real operation’s stable identity, parent/claim/reading references and recorded outcome. | Records the B16-2 snapshot commit once, carrying all bound references. | Exactly one permanent operational record for that operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12.4 — promotion_committed operation log
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_committed operation log rule within Promotion operation records. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — The real operation’s stable identity, parent/claim/reading references and recorded outcome. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — Records the B16-3 fence win, eligibility-record append and claim terminal together as one atomic operation with one child log. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — Exactly one permanent operational record for that operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Duplicate the operation log, confuse canonical state with an extra log, copy private payload or count the log as new content evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — Refuses unauthorized use or disclosure of the log under the applicable privacy/access rules; retries locate its existing operation log instead of writing a duplicate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12 — Promotion operation records | The real operation’s stable identity, parent/claim/reading references and recorded outcome. | Records the B16-3 fence win, eligibility-record append and claim terminal together as one atomic operation with one child log. | Exactly one permanent operational record for that operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12.5 — promotion_rejected operation log
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_rejected operation log rule within Promotion operation records. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — The real operation’s stable identity, parent/claim/reading references and recorded outcome. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — Records the rejection outcome and its cause class. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — Exactly one permanent operational record for that operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Duplicate the operation log, confuse canonical state with an extra log, copy private payload or count the log as new content evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — Records the rejection outcome and its cause class. The recorded failed, blocked or indeterminate outcome is not presented as committed production success; unauthorized log use/disclosure remains refused. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12 — Promotion operation records | The real operation’s stable identity, parent/claim/reading references and recorded outcome. | Records the rejection outcome and its cause class. | Exactly one permanent operational record for that operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12.6 — promotion_interrupted operation log
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_interrupted operation log rule within Promotion operation records. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — The real operation’s stable identity, parent/claim/reading references and recorded outcome. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — Records pre-commit termination with durable evidence of non-commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — Exactly one permanent operational record for that operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Duplicate the operation log, confuse canonical state with an extra log, copy private payload or count the log as new content evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — Records pre-commit termination with durable evidence of non-commit. The recorded failed, blocked or indeterminate outcome is not presented as committed production success; unauthorized log use/disclosure remains refused. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12 — Promotion operation records | The real operation’s stable identity, parent/claim/reading references and recorded outcome. | Records pre-commit termination with durable evidence of non-commit. | Exactly one permanent operational record for that operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12.7 — promotion_indeterminate operation log
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_indeterminate operation log rule within Promotion operation records. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — The real operation’s stable identity, parent/claim/reading references and recorded outcome. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — Records the fail-closed indeterminate resolution. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — Exactly one permanent operational record for that operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Duplicate the operation log, confuse canonical state with an extra log, copy private payload or count the log as new content evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — Records the fail-closed indeterminate resolution. The recorded failed, blocked or indeterminate outcome is not presented as committed production success; unauthorized log use/disclosure remains refused. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12 — Promotion operation records | The real operation’s stable identity, parent/claim/reading references and recorded outcome. | Records the fail-closed indeterminate resolution. | Exactly one permanent operational record for that operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12.8 — promotion_blocked_held operation log
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_blocked_held operation log rule within Promotion operation records. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — The real operation’s stable identity, parent/claim/reading references and recorded outcome. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — Records the dependency/hold block; its release policy remains with the hold/dependency owner. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — Exactly one permanent operational record for that operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Duplicate the operation log, confuse canonical state with an extra log, copy private payload or count the log as new content evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — Records the dependency/hold block; its release policy remains with the hold/dependency owner. The recorded failed, blocked or indeterminate outcome is not presented as committed production success; unauthorized log use/disclosure remains refused. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12 — Promotion operation records | The real operation’s stable identity, parent/claim/reading references and recorded outcome. | Records the dependency/hold block; its release policy remains with the hold/dependency owner. | Exactly one permanent operational record for that operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12.9 — promotion_duplicate_absorbed operation log
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_duplicate_absorbed operation log rule within Promotion operation records. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — The real operation’s stable identity, parent/claim/reading references and recorded outcome. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — Records B16-0 absorption against an already committed promotion. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — Exactly one permanent operational record for that operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Duplicate the operation log, confuse canonical state with an extra log, copy private payload or count the log as new content evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — Refuses unauthorized use or disclosure of the log under the applicable privacy/access rules; retries locate its existing operation log instead of writing a duplicate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12 — Promotion operation records | The real operation’s stable identity, parent/claim/reading references and recorded outcome. | Records B16-0 absorption against an already committed promotion. | Exactly one permanent operational record for that operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12.10 — recovery_applied operation log
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The recovery_applied operation log rule within Promotion operation records. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — The real operation’s stable identity, parent/claim/reading references and recorded outcome. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — Records applied append-only recovery actions under recovery_run_id and the stable recovery child identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — Exactly one permanent operational record for that operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Duplicate the operation log, confuse canonical state with an extra log, copy private payload or count the log as new content evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — Refuses unauthorized use or disclosure of the log under the applicable privacy/access rules; retries locate its existing operation log instead of writing a duplicate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12 — Promotion operation records | The real operation’s stable identity, parent/claim/reading references and recorded outcome. | Records applied append-only recovery actions under recovery_run_id and the stable recovery child identity. | Exactly one permanent operational record for that operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12.11 — recovery_noop operation log
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The recovery_noop operation log rule within Promotion operation records. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — The real operation’s stable identity, parent/claim/reading references and recorded outcome. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — Records lookup-only recovery resolution returning committed findings without re-executing an already resolved action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — Exactly one permanent operational record for that operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Duplicate the operation log, confuse canonical state with an extra log, copy private payload or count the log as new content evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — Refuses unauthorized use or disclosure of the log under the applicable privacy/access rules; retries locate its existing operation log instead of writing a duplicate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12 — Promotion operation records | The real operation’s stable identity, parent/claim/reading references and recorded outcome. | Records lookup-only recovery resolution returning committed findings without re-executing an already resolved action. | Exactly one permanent operational record for that operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12.12 — fail_closed_event operation log
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The fail_closed_event operation log rule within Promotion operation records. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — The real operation’s stable identity, parent/claim/reading references and recorded outcome. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — Records the fail-closed occurrence with its named missing or failed condition. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — Exactly one permanent operational record for that operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Duplicate the operation log, confuse canonical state with an extra log, copy private payload or count the log as new content evidence. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — Records the fail-closed occurrence with its named missing or failed condition. The recorded failed, blocked or indeterminate outcome is not presented as committed production success; unauthorized log use/disclosure remains refused. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12 — Promotion operation records | The real operation’s stable identity, parent/claim/reading references and recorded outcome. | Records the fail-closed occurrence with its named missing or failed condition. | Exactly one permanent operational record for that operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12.13 — Parent terminal outcome
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Parent terminal outcome rule within Promotion operation records. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — Resolved children and canonical records under one promotion_operation_id. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — Durably records exactly one of promotion_committed, promotion_duplicate_absorbed, promotion_rejected, promotion_interrupted, promotion_blocked_held, promotion_indeterminate, before acknowledging the caller. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — One terminal for the parent; all child logs retain distinct child identities. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Acknowledge before durability, duplicate a terminal or count a child as another parent terminal. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — Withholds acknowledgement if the parent terminal is missing; recovery adds only that missing record without invalidating an existing commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.12.13.1 — promotion_committed parent outcome: The matching fenced eligibility commit and trail exist. The terminal is durable before acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.13.2 — promotion_duplicate_absorbed parent outcome: An existing committed promotion absorbed this attempt. The terminal is durable before acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.13.3 — promotion_rejected parent outcome: The attempt was rejected with recorded cause. The terminal is durable before acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.13.4 — promotion_interrupted parent outcome: The attempt terminated before commit with durable non-commit evidence. The terminal is durable before acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.13.5 — promotion_blocked_held parent outcome: A recorded hold/dependency prevents progress. The terminal is durable before acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.13.6 — promotion_indeterminate parent outcome: Evidence is unprovable, unreadable or contradictory. The terminal is durable before acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12 — Promotion operation records | Resolved children and canonical records under one promotion_operation_id. | Durably records exactly one of promotion_committed, promotion_duplicate_absorbed, promotion_rejected, promotion_interrupted, promotion_blocked_held, promotion_indeterminate, before acknowledging the caller. | One terminal for the parent; all child logs retain distinct child identities. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.5.5 — B16-4 — Parent terminal log commit | Resolved children and canonical records under one promotion_operation_id. | Commits the single parent outcome only after child operations and canonical records resolve. Exactly one parent terminal becomes durable before acknowledgement; a missing terminal is recovered without invalidating a committed eligibility record. | One terminal for the parent; all child logs retain distinct child identities. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.10.4 — Recovery 4 — Production-eligibility record present, parent terminal log absent | Resolved children and canonical records under one promotion_operation_id. | The missing parent terminal must become durable before success acknowledgement. | One terminal for the parent; all child logs retain distinct child identities. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.5 — Promotion transaction boundaries | Resolved children and canonical records under one promotion_operation_id. | Success acknowledgement waits until the one parent terminal is durable after the child operations and canonical records resolve. | One terminal for the parent; all child logs retain distinct child identities. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] |
| 5 · ACCEPTED | C-READ.11.8.8 — Parent terminal log (B16-4) duplicate prevention | Resolved children and canonical records under one promotion_operation_id. | The source-defined permanent or operation identity and its existing committed result determine whether this action may create a new record. | One terminal for the parent; all child logs retain distinct child identities. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] |
| 6 · ACCEPTED | C-READ.11.10.5 — Recovery 5 — Terminal log present, acknowledgement absent | Resolved children and canonical records under one promotion_operation_id. | Only the already durable terminal outcome is returned; no operation or second terminal is recreated. | One terminal for the parent; all child logs retain distinct child identities. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |

SUB-PARTS: C-READ.11.12.13.1 — promotion_committed parent outcome; C-READ.11.12.13.2 — promotion_duplicate_absorbed parent outcome; C-READ.11.12.13.3 — promotion_rejected parent outcome; C-READ.11.12.13.4 — promotion_interrupted parent outcome; C-READ.11.12.13.5 — promotion_blocked_held parent outcome; C-READ.11.12.13.6 — promotion_indeterminate parent outcome

### C-READ.11.12.13.1 — promotion_committed parent outcome
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_committed parent outcome rule within Parent terminal outcome. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — The resolved outcome for this parent invocation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — The matching fenced eligibility commit and trail exist. The terminal is durable before acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — One parent terminal with outcome promotion_committed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Use this label without the matching recorded outcome, or write a second terminal for the parent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — No acknowledgement until the terminal is durable; a missing terminal is recovered once by identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.8.8 — Parent terminal log (B16-4) duplicate prevention: One terminal under this parent operation identity is permitted, with the matching durable outcome before acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12.13 — Parent terminal outcome | The resolved outcome for this parent invocation. | The matching fenced eligibility commit and trail exist. The terminal is durable before acknowledgement. | One parent terminal with outcome promotion_committed. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12.13.2 — promotion_duplicate_absorbed parent outcome
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_duplicate_absorbed parent outcome rule within Parent terminal outcome. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — The resolved outcome for this parent invocation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — An existing committed promotion absorbed this attempt. The terminal is durable before acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — One parent terminal with outcome promotion_duplicate_absorbed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Use this label without the matching recorded outcome, or write a second terminal for the parent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — No acknowledgement until the terminal is durable; a missing terminal is recovered once by identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.8.8 — Parent terminal log (B16-4) duplicate prevention: One terminal under this parent operation identity is permitted, with the matching durable outcome before acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12.13 — Parent terminal outcome | The resolved outcome for this parent invocation. | An existing committed promotion absorbed this attempt. The terminal is durable before acknowledgement. | One parent terminal with outcome promotion_duplicate_absorbed. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12.13.3 — promotion_rejected parent outcome
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_rejected parent outcome rule within Parent terminal outcome. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — The resolved outcome for this parent invocation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — The attempt was rejected with recorded cause. The terminal is durable before acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — One parent terminal with outcome promotion_rejected. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Use this label without the matching recorded outcome, or write a second terminal for the parent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Present this outcome as committed production success. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — No acknowledgement until the terminal is durable; a missing terminal is recovered once by identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.8.8 — Parent terminal log (B16-4) duplicate prevention: One terminal under this parent operation identity is permitted, with the matching durable outcome before acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12.13 — Parent terminal outcome | The resolved outcome for this parent invocation. | The attempt was rejected with recorded cause. The terminal is durable before acknowledgement. | One parent terminal with outcome promotion_rejected. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12.13.4 — promotion_interrupted parent outcome
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_interrupted parent outcome rule within Parent terminal outcome. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — The resolved outcome for this parent invocation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — The attempt terminated before commit with durable non-commit evidence. The terminal is durable before acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — One parent terminal with outcome promotion_interrupted. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Use this label without the matching recorded outcome, or write a second terminal for the parent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Present this outcome as committed production success. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — No acknowledgement until the terminal is durable; a missing terminal is recovered once by identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.8.8 — Parent terminal log (B16-4) duplicate prevention: One terminal under this parent operation identity is permitted, with the matching durable outcome before acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12.13 — Parent terminal outcome | The resolved outcome for this parent invocation. | The attempt terminated before commit with durable non-commit evidence. The terminal is durable before acknowledgement. | One parent terminal with outcome promotion_interrupted. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12.13.5 — promotion_blocked_held parent outcome
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_blocked_held parent outcome rule within Parent terminal outcome. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — The resolved outcome for this parent invocation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — A recorded hold/dependency prevents progress. The terminal is durable before acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — One parent terminal with outcome promotion_blocked_held. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Use this label without the matching recorded outcome, or write a second terminal for the parent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Present this outcome as committed production success. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — No acknowledgement until the terminal is durable; a missing terminal is recovered once by identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.8.8 — Parent terminal log (B16-4) duplicate prevention: One terminal under this parent operation identity is permitted, with the matching durable outcome before acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12.13 — Parent terminal outcome | The resolved outcome for this parent invocation. | A recorded hold/dependency prevents progress. The terminal is durable before acknowledgement. | One parent terminal with outcome promotion_blocked_held. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12.13.6 — promotion_indeterminate parent outcome
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The promotion_indeterminate parent outcome rule within Parent terminal outcome. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — The resolved outcome for this parent invocation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — Evidence is unprovable, unreadable or contradictory. The terminal is durable before acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — One parent terminal with outcome promotion_indeterminate. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Use this label without the matching recorded outcome, or write a second terminal for the parent. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Present this outcome as committed production success. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — No acknowledgement until the terminal is durable; a missing terminal is recovered once by identity. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.8.8 — Parent terminal log (B16-4) duplicate prevention: One terminal under this parent operation identity is permitted, with the matching durable outcome before acknowledgement. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12.13 — Parent terminal outcome | The resolved outcome for this parent invocation. | Evidence is unprovable, unreadable or contradictory. The terminal is durable before acknowledgement. | One parent terminal with outcome promotion_indeterminate. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12.14 — Operation-record identity and payload boundary
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Operation-record identity and payload boundary rule within Promotion operation records. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — An operational log about a promotion action. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — Links by operation, claim and reading identities only; never copies root or reading content. Active/cold lifecycle follows the governing living-record law. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — Retrievable operation provenance without copied payload or new support for content. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Copy payload, bypass the access boundary, or count repeated log/state records as independent votes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — Access or visibility refusal remains binding on each log, including privacy-block records. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.12.14.1 — Operation identity: Identifies the one parent or child operation recorded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.14.2 — Claim identity: Links to the permanent claim without copying evidence content. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.12.14.3 — Reading identity: Links to the immutable reading without copying its content. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12 — Promotion operation records | An operational log about a promotion action. | Links by operation, claim and reading identities only; never copies root or reading content. Active/cold lifecycle follows the governing living-record law. | Retrievable operation provenance without copied payload or new support for content. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: C-READ.11.12.14.1 — Operation identity; C-READ.11.12.14.2 — Claim identity; C-READ.11.12.14.3 — Reading identity

### C-READ.11.12.14.1 — Operation identity
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Operation identity member of Operation-record identity and payload boundary. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — Structural identifier reference only; exact serialized field name not chosen here. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — Identifies the one parent or child operation recorded. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — Structural identifier reference only; exact serialized field name not chosen here. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Copy root/reading content in place of this structural reference or bypass access rules through the reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — Unauthorized access to the referenced material remains refused; record existence grants no access. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: Structural references never authorize access or disclosure; the applicable privacy and access restrictions remain binding. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12.14 — Operation-record identity and payload boundary | Structural identifier reference only; exact serialized field name not chosen here. | Identifies the one parent or child operation recorded. | Structural identifier reference only; exact serialized field name not chosen here. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12.14.2 — Claim identity
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Claim identity member of Operation-record identity and payload boundary. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — Structural identifier reference only; exact serialized field name not chosen here. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — Links to the permanent claim without copying evidence content. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — Structural identifier reference only; exact serialized field name not chosen here. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Copy root/reading content in place of this structural reference or bypass access rules through the reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — Unauthorized access to the referenced material remains refused; record existence grants no access. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: Structural references never authorize access or disclosure; the applicable privacy and access restrictions remain binding. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12.14 — Operation-record identity and payload boundary | Structural identifier reference only; exact serialized field name not chosen here. | Links to the permanent claim without copying evidence content. | Structural identifier reference only; exact serialized field name not chosen here. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12.14.3 — Reading identity
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Reading identity member of Operation-record identity and payload boundary. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — Structural identifier reference only; exact serialized field name not chosen here. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — Links to the immutable reading without copying its content. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — Structural identifier reference only; exact serialized field name not chosen here. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Copy root/reading content in place of this structural reference or bypass access rules through the reference. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — Unauthorized access to the referenced material remains refused; record existence grants no access. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: Structural references never authorize access or disclosure; the applicable privacy and access restrictions remain binding. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12.14 — Operation-record identity and payload boundary | Structural identifier reference only; exact serialized field name not chosen here. | Links to the immutable reading without copying its content. | Structural identifier reference only; exact serialized field name not chosen here. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.12.15 — No recursive logs or double evidence
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

ALONE
- What it is: ACCEPTED — The No recursive logs or double evidence rule within Promotion operation records. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Takes in: ACCEPTED — A canonical transaction/state record, an operation log, or a later real operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Does: ACCEPTED — One real operation receives one log. Creating that log generates none; a genuinely separate later operation may receive its own. State/log repetition never strengthens the reading’s meaning or truth. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Gives out: ACCEPTED — Preserved connected history with separated operation identities. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Must never: ACCEPTED — Create an automatic log-about-log chain or multiply evidential votes for one underlying reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]
- Fails closed by: ACCEPTED — Withholds duplicate operational logs and any unsupported evidential increase. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.12 — Promotion operation records | A canonical transaction/state record, an operation log, or a later real operation. | One real operation receives one log. Creating that log generates none; a genuinely separate later operation may receive its own. State/log repetition never strengthens the reading’s meaning or truth. | Preserved connected history with separated operation identities. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.13 — Promotion boundaries
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

ALONE
- What it is: ACCEPTED — The permanent privacy, ownership, provenance and non-destructive boundaries of the promotion seam. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Takes in: ACCEPTED — Every promotion operation, record, log and proposed consumption. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Does: ACCEPTED — Keeps mechanical state/evidence checks separate from semantic judgment; respects privacy/access order; preserves root/reading and quarantine/production separation; never exposes sealed TSC contents. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Gives out: ACCEPTED — A bounded mechanical promotion operation and preserved history. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Must never: ACCEPTED — Interpret or score the reading, change its history, bypass access, create a production store, inspect sealed TSC or turn derived material into independent support. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Fails closed by: ACCEPTED — Unauthorized actions fail closed; non-committed candidates stay excluded; roots/readings and prior records remain preserved. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

TOGETHER
- Fed by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: Applies §7Q before §7R; visible-output ordering is §7Q first, SACL second; applicable SACL scope precedes retrieval. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.13.2 — Mechanical gate versus semantic judgment: Establishes only machine-state/provenance facts; it never decides meaning, truth, passing or enough. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.13.3 — Read-only root and reading boundary: Keeps root evidence and prior-reading context separate; checks root identity read-only; leaves roots, batches, seals, indexes and reading bytes untouched. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.13.4 — Quarantine and production boundary: Derives status from external append-only records; the reading never moves or mutates; both production protections remain required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.13.5 — TSC remains a separate seam: Keeps TSC authorization/promotion separate; B16 creates no TSC inspection path and reads no sealed TSC content. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Fed by: ACCEPTED — C-READ.11.13.6 — No loss or false production result: Preserves history and allows only the source-defined committed result and complete trail to establish production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Gated by: ACCEPTED — C-READ.11.13.1 — Privacy before relevance: Every promotion operation, record and log obeys the stated privacy/access ordering and authorization. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11 — Quarantine-to-production promotion seam | Every promotion operation, record, log and proposed consumption. | Keeps mechanical state/evidence checks separate from semantic judgment; respects privacy/access order; preserves root/reading and quarantine/production separation; never exposes sealed TSC contents. | A bounded mechanical promotion operation and preserved history. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |

SUB-PARTS: C-READ.11.13.1 — Privacy before relevance; C-READ.11.13.2 — Mechanical gate versus semantic judgment; C-READ.11.13.3 — Read-only root and reading boundary; C-READ.11.13.4 — Quarantine and production boundary; C-READ.11.13.5 — TSC remains a separate seam; C-READ.11.13.6 — No loss or false production result

### C-READ.11.13.1 — Privacy before relevance
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Privacy before relevance rule within Promotion boundaries. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Takes in: ACCEPTED — Every operation, record and log. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Does: ACCEPTED — Applies §7Q before §7R; visible-output ordering is §7Q first, SACL second; applicable SACL scope precedes retrieval. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Gives out: ACCEPTED — The stated boundary remains binding for this promotion operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Must never: ACCEPTED — Use relevance or record existence as permission. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Fails closed by: ACCEPTED — A privacy refusal is a fail-closed result, never a bypassable obstacle. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): §7Q precedes relevance and visible-output SACL checks; internal-use authorization remains mandatory. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Gated by: ACCEPTED — C-SACL — Speaker Access-Control Layer (§25.4): Applicable access scope must clear before retrieval; visible-output ordering keeps §7Q first. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.13 — Promotion boundaries | Every operation, record and log. | Applies §7Q before §7R; visible-output ordering is §7Q first, SACL second; applicable SACL scope precedes retrieval. Every promotion operation, record and log obeys the stated privacy/access ordering and authorization. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.7 — promotion_evidence_snapshot | Every operation, record and log. | This operation and its records remain subject to internal-use authorization, privacy visibility and applicable SACL scope. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 3 · ACCEPTED | C-READ.11.1 — Promotion reading identity | Every operation, record and log. | This operation and its records remain subject to internal-use authorization, privacy visibility and applicable SACL scope. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 4 · ACCEPTED | C-READ.11.2 — promotion_claim | Every operation, record and log. | This operation and its records remain subject to internal-use authorization, privacy visibility and applicable SACL scope. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 5 · ACCEPTED | C-READ.11.5.4.1 — production_eligibility_record | Every operation, record and log. | This operation and its records remain subject to internal-use authorization, privacy visibility and applicable SACL scope. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 6 · ACCEPTED | C-READ.11.10 — Promotion recovery matrix | Every operation, record and log. | This operation and its records remain subject to internal-use authorization, privacy visibility and applicable SACL scope. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 7 · ACCEPTED | C-READ.11.12 — Promotion operation records | Every operation, record and log. | This operation and its records remain subject to internal-use authorization, privacy visibility and applicable SACL scope. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 8 · ACCEPTED | C-READ.11.12.1 — promotion_requested operation log | Every operation, record and log. | Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 9 · ACCEPTED | C-READ.11.12.2 — promotion_claim_reserved operation log | Every operation, record and log. | Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 10 · ACCEPTED | C-READ.11.12.3 — promotion_evidence_checked operation log | Every operation, record and log. | Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 11 · ACCEPTED | C-READ.11.12.4 — promotion_committed operation log | Every operation, record and log. | Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 12 · ACCEPTED | C-READ.11.12.5 — promotion_rejected operation log | Every operation, record and log. | Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 13 · ACCEPTED | C-READ.11.12.6 — promotion_interrupted operation log | Every operation, record and log. | Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 14 · ACCEPTED | C-READ.11.12.7 — promotion_indeterminate operation log | Every operation, record and log. | Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 15 · ACCEPTED | C-READ.11.12.8 — promotion_blocked_held operation log | Every operation, record and log. | Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 16 · ACCEPTED | C-READ.11.12.9 — promotion_duplicate_absorbed operation log | Every operation, record and log. | Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 17 · ACCEPTED | C-READ.11.12.10 — recovery_applied operation log | Every operation, record and log. | Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 18 · ACCEPTED | C-READ.11.12.11 — recovery_noop operation log | Every operation, record and log. | Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 19 · ACCEPTED | C-READ.11.12.12 — fail_closed_event operation log | Every operation, record and log. | Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 20 · ACCEPTED | C-READ.11.12.13 — Parent terminal outcome | Every operation, record and log. | Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 21 · ACCEPTED | C-READ.11.12.14 — Operation-record identity and payload boundary | Every operation, record and log. | Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 22 · ACCEPTED | C-READ.11.12.15 — No recursive logs or double evidence | Every operation, record and log. | Log existence grants no access; privacy, visibility, identity and authority restrictions govern use. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 23 · ACCEPTED | C-READ.11.9.4 — Promotion records do not establish content truth | Every operation, record and log. | Authorized examination and visible output remain subject to privacy, identity and access restrictions; record existence grants no bypass. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 24 · ACCEPTED | C-READ.11.10.14 — Recovery 14 — Privacy/access block | Every operation, record and log. | The §7Q/SACL refusal class controls rejection or held waiting; the gate is never bypassed or retried around. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 25 · ACCEPTED | C-READ.11.10.14.1 — Unauthorized rejection | Every operation, record and log. | The privacy/access refusal class requires rejection with its protected block record. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 26 · ACCEPTED | C-READ.11.10.14.2 — Unauthorized held outcome | Every operation, record and log. | The privacy/access refusal class may hold the attempt; no retry bypass exists. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] |
| 27 · ACCEPTED | C-READ.11.12.14.1 — Operation identity | Every operation, record and log. | Structural references never authorize access or disclosure; the applicable privacy and access restrictions remain binding. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |
| 28 · ACCEPTED | C-READ.11.12.14.2 — Claim identity | Every operation, record and log. | Structural references never authorize access or disclosure; the applicable privacy and access restrictions remain binding. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |
| 29 · ACCEPTED | C-READ.11.12.14.3 — Reading identity | Every operation, record and log. | Structural references never authorize access or disclosure; the applicable privacy and access restrictions remain binding. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.13.2 — Mechanical gate versus semantic judgment
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Mechanical gate versus semantic judgment rule within Promotion boundaries. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Takes in: ACCEPTED — Evidence, the recorded promotion decision and a reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Does: ACCEPTED — Establishes only machine-state/provenance facts; it never decides meaning, truth, passing or enough. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Gives out: ACCEPTED — The stated boundary remains binding for this promotion operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Must never: ACCEPTED — Perform inspection/scoring, invent pass policy or turn the recorded decision into a semantic judgment by B16. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Fails closed by: ACCEPTED — Cannot substitute a mechanical validation pass for a missing recorded passing promotion decision. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.7.6 — promotion_decision_ref: The mechanical seam requires the recorded passing decision and cannot make the semantic decision itself. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.13 — Promotion boundaries | Evidence, the recorded promotion decision and a reading. | Establishes only machine-state/provenance facts; it never decides meaning, truth, passing or enough. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.13.3 — Read-only root and reading boundary
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Read-only root and reading boundary rule within Promotion boundaries. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Takes in: ACCEPTED — Root identities, prior-reading context and the quarantined reading. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Does: ACCEPTED — Keeps root evidence and prior-reading context separate; checks root identity read-only; leaves roots, batches, seals, indexes and reading bytes untouched. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Gives out: ACCEPTED — The stated boundary remains binding for this promotion operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Must never: ACCEPTED — Change root, batch, seal, index or reading history; combine root evidence and prior-reading context into one evidential block. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Fails closed by: ACCEPTED — Cannot repair or guess a missing/unreadable referenced root or reading; it fails closed. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.7.2 — Read-only root references: Root existence is checked read-only by identity; no missing reference can be repaired or guessed by B16. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.13 — Promotion boundaries | Root identities, prior-reading context and the quarantined reading. | Keeps root evidence and prior-reading context separate; checks root identity read-only; leaves roots, batches, seals, indexes and reading bytes untouched. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.13.4 — Quarantine and production boundary
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

ALONE
- What it is: ACCEPTED — The Quarantine and production boundary rule within Promotion boundaries. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Takes in: ACCEPTED — A quarantined reading and the proposed production-eligibility transition. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Does: ACCEPTED — Derives status from external append-only records; the reading never moves or mutates; both production protections remain required. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Gives out: ACCEPTED — The stated boundary remains binding for this promotion operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Must never: ACCEPTED — Create/write/authorize production storage as a promotion side effect or promote without both protections. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Fails closed by: ACCEPTED — Missing either protection prevents commit; uncommitted material is excluded from production. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.7.7 — Dual production-authorization evidence: Both production protections are mandatory; absence of either blocks commit. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.13 — Promotion boundaries | A quarantined reading and the proposed production-eligibility transition. | Derives status from external append-only records; the reading never moves or mutates; both production protections remain required. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| 2 · ACCEPTED | C-READ.11.11.10 — Production store absent (it is, by design) | A quarantined reading and the proposed production-eligibility transition. | B16 has no production-store creation/write authority; recording eligibility does not cross that boundary. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.13.5 — TSC remains a separate seam
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

ALONE
- What it is: ACCEPTED — The TSC remains a separate seam rule within Promotion boundaries. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Takes in: ACCEPTED — TSC-held or sealed session material and a B16 promotion request. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Does: ACCEPTED — Keeps TSC authorization/promotion separate; B16 creates no TSC inspection path and reads no sealed TSC content. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Gives out: ACCEPTED — The stated boundary remains binding for this promotion operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Must never: ACCEPTED — Inspect sealed TSC or use B16 as a path around TSC authorization. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Fails closed by: ACCEPTED — Provides no access to sealed TSC contents through this seam. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.13 — Promotion boundaries | TSC-held or sealed session material and a B16 promotion request. | Keeps TSC authorization/promotion separate; B16 creates no TSC inspection path and reads no sealed TSC content. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |

SUB-PARTS: NONE

### C-READ.11.13.6 — No loss or false production result
Stamp: ACCEPTED    Source: [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]

ALONE
- What it is: ACCEPTED — The No loss or false production result rule within Promotion boundaries. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Takes in: ACCEPTED — Claims, reading/root history, evidence and outcomes. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Does: ACCEPTED — Preserves history and allows only the source-defined committed result and complete trail to establish production eligibility. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Gives out: ACCEPTED — The stated boundary remains binding for this promotion operation. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Must never: ACCEPTED — Rewrite history, duplicate promotion, silently admit quarantine influence or fabricate success. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Fails closed by: ACCEPTED — A failed or indeterminate attempt grants no production influence and loses no existing record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-READ.11.9.1 — Complete committed-trail requirement: Only the complete validated committed trail can establish production eligibility; no false success or guessed record. [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-READ.11.13 — Promotion boundaries | Claims, reading/root history, evidence and outcomes. | Preserves history and allows only the source-defined committed result and complete trail to establish production eligibility. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |

SUB-PARTS: NONE

<!-- END CHAPTER 3-d BEHAVIOR -->

## Cross-piece continuation and reciprocal uses

These entries are recorded here. The join only concatenates text; it does not edit or merge these entries into an earlier or future card. All earlier card text remains unchanged.

| Existing card | Field | Entry recorded here | Source |
|---|---|---|---|
| C-READ — Reading record, validator, writer (§6B) | SUB-PARTS | ACCEPTED — C-READ.11 — Quarantine-to-production promotion seam follows C-READ.10 in the continuing C-READ tree. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [NHD-B16] |
| C-READ — Reading record, validator, writer (§6B) | Fed by | ACCEPTED — C-READ.11 — Quarantine-to-production promotion seam: supplies the per-reading derived promotion result in CY-G, without rewriting the reading. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |

| Endpoint owner | USED BY | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| C-READ.4 — Quarantine readings destination | C-READ.11 — Quarantine-to-production promotion seam | ACCEPTED — A quarantined reading identity, a promotion request, its permanent claim and attempt identities, the required evidence, production protections, privacy authorization and hold/dependency status. | Supplies the quarantined reading by identity, without moving or rewriting it. | A derived committed, duplicate-absorbed, rejected, interrupted, held or indeterminate outcome with its traceable records; the reading stays in place. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16] |
| C-READ.5 — Production readings authorization | C-READ.11 — Quarantine-to-production promotion seam | ACCEPTED — A quarantined reading identity, a promotion request, its permanent claim and attempt identities, the required evidence, production protections, privacy authorization and hold/dependency status. | Both production protections are mandatory; marker presence alone never authorizes promotion. | A derived committed, duplicate-absorbed, rejected, interrupted, held or indeterminate outcome with its traceable records; the reading stays in place. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-READ.11 — Quarantine-to-production promotion seam | ACCEPTED — A quarantined reading identity, a promotion request, its permanent claim and attempt identities, the required evidence, production protections, privacy authorization and hold/dependency status. | Internal-use authorization and privacy restrictions apply before relevance; unauthorized operations fail closed. | A derived committed, duplicate-absorbed, rejected, interrupted, held or indeterminate outcome with its traceable records; the reading stays in place. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-READ.11 — Quarantine-to-production promotion seam | ACCEPTED — A quarantined reading identity, a promotion request, its permanent claim and attempt identities, the required evidence, production protections, privacy authorization and hold/dependency status. | Applicable identity/access scope must permit the operation; refusal cannot be bypassed or retried around. | A derived committed, duplicate-absorbed, rejected, interrupted, held or indeterminate outcome with its traceable records; the reading stays in place. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| C-READ.10.9 — Telling lifecycle subordination | C-READ.11.9.3 — Telling promotion inherits by reference | ACCEPTED — A telling and its parent reading’s derived committed status. | Carries the parent-derived telling lifecycle contract; no mutable or independent telling promotion state is created. | Parent-bound production eligibility without mutating the telling. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [NHD-B16] [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] |
| C-READ.5 — Production readings authorization | C-READ.11.7.7 — Dual production-authorization evidence | ACCEPTED — Marker-presence verification and the approved specific production-write record. | The marker and specific approval are both required evidence, never substitutes. | One verified bound evidence input; all nine are needed for a snapshot. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-READ.11.13.1 — Privacy before relevance | ACCEPTED — Every operation, record and log. | §7Q precedes relevance and visible-output SACL checks; internal-use authorization remains mandatory. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-READ.11.13.1 — Privacy before relevance | ACCEPTED — Every operation, record and log. | Applicable access scope must clear before retrieval; visible-output ordering keeps §7Q first. | The stated boundary remains binding for this promotion operation. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] |
| C-READ.5.1 — Physical production marker | C-READ.11.7.7.1 — Marker-presence verification event | ACCEPTED — Verification that .nh_readings_production_authorized is physically present. | Requires the deliberately created physical production marker; absence blocks commit. | Verification that .nh_readings_production_authorized is physically present. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |
| C-READ.5.2 — Specific production-write approval | C-READ.11.7.7.2 — Approved production-change reference | ACCEPTED — Reference to the approved PROPOSED CHANGE dry-run covering the production write. | Requires the approved specific production change; marker presence cannot replace it. | Reference to the approved PROPOSED CHANGE dry-run covering the production write. | [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] |

All 189 new cards descend from C-READ.11 and participate through that seam in CY-G. The source defines the per-reading transaction order, not an invented end-to-end batch cycle. Record members, state values, recovery branches and constraints are used through their containing operation; they are not additional compulsory main-path steps.

## Chapter 3-d register contributions

### NOT DECIDED register

| Part | Field or scoped detail | Status |
|---|---|---|
| C-READ.11.1 | Changes | NOT DECIDED |
| C-READ.11.1.1 | Fed by | NOT DECIDED |
| C-READ.11.1.1 | Changes | NOT DECIDED |
| C-READ.11.1.2 | Fed by | NOT DECIDED |
| C-READ.11.1.2 | Changes | NOT DECIDED |
| C-READ.11.1.3 | Fed by | NOT DECIDED |
| C-READ.11.1.3 | Changes | NOT DECIDED |
| C-READ.11.1.4 | Fed by | NOT DECIDED |
| C-READ.11.1.4 | Changes | NOT DECIDED |
| C-READ.11.2 | Changes | NOT DECIDED |
| C-READ.11.2.1 | Fed by | NOT DECIDED |
| C-READ.11.2.1 | Changes | NOT DECIDED |
| C-READ.11.2.2 | Fed by | NOT DECIDED |
| C-READ.11.2.2 | Changes | NOT DECIDED |
| C-READ.11.2.3 | Fed by | NOT DECIDED |
| C-READ.11.2.3 | Changes | NOT DECIDED |
| C-READ.11.2.4 | Fed by | NOT DECIDED |
| C-READ.11.2.4 | Changes | NOT DECIDED |
| C-READ.11.2.5 | Fed by | NOT DECIDED |
| C-READ.11.2.5 | Changes | NOT DECIDED |
| C-READ.11.2.6 | Fed by | NOT DECIDED |
| C-READ.11.2.6 | Changes | NOT DECIDED |
| C-READ.11.3 | Changes | NOT DECIDED |
| C-READ.11.3.1 | Fed by | NOT DECIDED |
| C-READ.11.3.1 | Changes | NOT DECIDED |
| C-READ.11.3.2 | Fed by | NOT DECIDED |
| C-READ.11.3.2 | Changes | NOT DECIDED |
| C-READ.11.3.3 | Fed by | NOT DECIDED |
| C-READ.11.3.3 | Changes | NOT DECIDED |
| C-READ.11.4 | Changes | NOT DECIDED |
| C-READ.11.4.1 | Fed by | NOT DECIDED |
| C-READ.11.4.1 | Changes | NOT DECIDED |
| C-READ.11.4.2 | Fed by | NOT DECIDED |
| C-READ.11.4.2 | Changes | NOT DECIDED |
| C-READ.11.4.3 | Fed by | NOT DECIDED |
| C-READ.11.4.3 | Changes | NOT DECIDED |
| C-READ.11.4.4 | Fed by | NOT DECIDED |
| C-READ.11.4.4 | Changes | NOT DECIDED |
| C-READ.11.4.5 | Fed by | NOT DECIDED |
| C-READ.11.4.5 | Changes | NOT DECIDED |
| C-READ.11.4.6 | Fed by | NOT DECIDED |
| C-READ.11.4.6 | Changes | NOT DECIDED |
| C-READ.11.4.7 | Fed by | NOT DECIDED |
| C-READ.11.4.7 | Changes | NOT DECIDED |
| C-READ.11.4.8 | Fed by | NOT DECIDED |
| C-READ.11.4.8 | Changes | NOT DECIDED |
| C-READ.11.4.9 | Fed by | NOT DECIDED |
| C-READ.11.4.9 | Changes | NOT DECIDED |
| C-READ.11.5 | Changes | NOT DECIDED |
| C-READ.11.5.1 | Changes | NOT DECIDED |
| C-READ.11.5.2 | Changes | NOT DECIDED |
| C-READ.11.5.2.1 | Changes | NOT DECIDED |
| C-READ.11.5.2.1.1 | Fed by | NOT DECIDED |
| C-READ.11.5.2.1.1 | Changes | NOT DECIDED |
| C-READ.11.5.2.1.2 | Fed by | NOT DECIDED |
| C-READ.11.5.2.1.2 | Changes | NOT DECIDED |
| C-READ.11.5.2.1.3 | Fed by | NOT DECIDED |
| C-READ.11.5.2.1.3 | Changes | NOT DECIDED |
| C-READ.11.5.2.1.4 | Fed by | NOT DECIDED |
| C-READ.11.5.2.1.4 | Changes | NOT DECIDED |
| C-READ.11.5.2.1.5 | Fed by | NOT DECIDED |
| C-READ.11.5.2.1.5 | Changes | NOT DECIDED |
| C-READ.11.5.3 | Changes | NOT DECIDED |
| C-READ.11.5.4.1 | Changes | NOT DECIDED |
| C-READ.11.5.4.1.1 | Fed by | NOT DECIDED |
| C-READ.11.5.4.1.1 | Changes | NOT DECIDED |
| C-READ.11.5.4.1.2 | Fed by | NOT DECIDED |
| C-READ.11.5.4.1.2 | Changes | NOT DECIDED |
| C-READ.11.5.4.1.3 | Fed by | NOT DECIDED |
| C-READ.11.5.4.1.3 | Changes | NOT DECIDED |
| C-READ.11.5.4.1.4 | Fed by | NOT DECIDED |
| C-READ.11.5.4.1.4 | Changes | NOT DECIDED |
| C-READ.11.5.4.1.5 | Fed by | NOT DECIDED |
| C-READ.11.5.4.1.5 | Changes | NOT DECIDED |
| C-READ.11.5.4.1.6 | Fed by | NOT DECIDED |
| C-READ.11.5.4.1.6 | Changes | NOT DECIDED |
| C-READ.11.5.4.1.7 | Fed by | NOT DECIDED |
| C-READ.11.5.4.1.7 | Changes | NOT DECIDED |
| C-READ.11.5.5 | Changes | NOT DECIDED |
| C-READ.11.5.6 | Gated by | NOT DECIDED |
| C-READ.11.5.6 | Changes | NOT DECIDED |
| C-READ.11.6 | Changes | NOT DECIDED |
| C-READ.11.6.1 | Fed by | NOT DECIDED |
| C-READ.11.6.1 | Changes | NOT DECIDED |
| C-READ.11.6.2 | Fed by | NOT DECIDED |
| C-READ.11.6.2 | Changes | NOT DECIDED |
| C-READ.11.6.3 | Fed by | NOT DECIDED |
| C-READ.11.6.3 | Changes | NOT DECIDED |
| C-READ.11.6.4 | Fed by | NOT DECIDED |
| C-READ.11.6.4 | Changes | NOT DECIDED |
| C-READ.11.6.5 | Fed by | NOT DECIDED |
| C-READ.11.6.5 | Changes | NOT DECIDED |
| C-READ.11.6.6 | Fed by | NOT DECIDED |
| C-READ.11.6.6 | Changes | NOT DECIDED |
| C-READ.11.6.7 | Changes | NOT DECIDED |
| C-READ.11.6.7.1 | Fed by | NOT DECIDED |
| C-READ.11.6.7.1 | Changes | NOT DECIDED |
| C-READ.11.6.7.2 | Fed by | NOT DECIDED |
| C-READ.11.6.7.2 | Changes | NOT DECIDED |
| C-READ.11.6.7.3 | Fed by | NOT DECIDED |
| C-READ.11.6.7.3 | Changes | NOT DECIDED |
| C-READ.11.6.7.3.1 | Fed by | NOT DECIDED |
| C-READ.11.6.7.3.1 | Gated by | NOT DECIDED |
| C-READ.11.6.7.3.1 | Changes | NOT DECIDED |
| C-READ.11.6.7.3.2 | Fed by | NOT DECIDED |
| C-READ.11.6.7.3.2 | Gated by | NOT DECIDED |
| C-READ.11.6.7.3.2 | Changes | NOT DECIDED |
| C-READ.11.6.7.3.3 | Fed by | NOT DECIDED |
| C-READ.11.6.7.3.3 | Gated by | NOT DECIDED |
| C-READ.11.6.7.3.3 | Changes | NOT DECIDED |
| C-READ.11.6.7.3.4 | Fed by | NOT DECIDED |
| C-READ.11.6.7.3.4 | Gated by | NOT DECIDED |
| C-READ.11.6.7.3.4 | Changes | NOT DECIDED |
| C-READ.11.6.8 | Fed by | NOT DECIDED |
| C-READ.11.6.8 | Changes | NOT DECIDED |
| C-READ.11.6.9 | Fed by | NOT DECIDED |
| C-READ.11.6.9 | Changes | NOT DECIDED |
| C-READ.11.7 | Changes | NOT DECIDED |
| C-READ.11.7.1 | Changes | NOT DECIDED |
| C-READ.11.7.1.1 | Fed by | NOT DECIDED |
| C-READ.11.7.1.1 | Changes | NOT DECIDED |
| C-READ.11.7.1.2 | Fed by | NOT DECIDED |
| C-READ.11.7.1.2 | Changes | NOT DECIDED |
| C-READ.11.7.1.3 | Fed by | NOT DECIDED |
| C-READ.11.7.1.3 | Changes | NOT DECIDED |
| C-READ.11.7.2 | Fed by | NOT DECIDED |
| C-READ.11.7.2 | Changes | NOT DECIDED |
| C-READ.11.7.3 | Fed by | NOT DECIDED |
| C-READ.11.7.3 | Changes | NOT DECIDED |
| C-READ.11.7.4 | Fed by | NOT DECIDED |
| C-READ.11.7.4 | Changes | NOT DECIDED |
| C-READ.11.7.5 | Fed by | NOT DECIDED |
| C-READ.11.7.5 | Changes | NOT DECIDED |
| C-READ.11.7.6 | Fed by | NOT DECIDED |
| C-READ.11.7.6 | Changes | NOT DECIDED |
| C-READ.11.7.7 | Changes | NOT DECIDED |
| C-READ.11.7.7.1 | Fed by | NOT DECIDED |
| C-READ.11.7.7.1 | Changes | NOT DECIDED |
| C-READ.11.7.7.2 | Fed by | NOT DECIDED |
| C-READ.11.7.7.2 | Changes | NOT DECIDED |
| C-READ.11.7.8 | Fed by | NOT DECIDED |
| C-READ.11.7.8 | Changes | NOT DECIDED |
| C-READ.11.7.9 | Fed by | NOT DECIDED |
| C-READ.11.7.9 | Changes | NOT DECIDED |
| C-READ.11.7.10 | Fed by | NOT DECIDED |
| C-READ.11.7.10 | Changes | NOT DECIDED |
| C-READ.11.8 | Gated by | NOT DECIDED |
| C-READ.11.8 | Changes | NOT DECIDED |
| C-READ.11.8.1 | Fed by | NOT DECIDED |
| C-READ.11.8.1 | Changes | NOT DECIDED |
| C-READ.11.8.2 | Fed by | NOT DECIDED |
| C-READ.11.8.2 | Changes | NOT DECIDED |
| C-READ.11.8.3 | Fed by | NOT DECIDED |
| C-READ.11.8.3 | Changes | NOT DECIDED |
| C-READ.11.8.4 | Fed by | NOT DECIDED |
| C-READ.11.8.4 | Changes | NOT DECIDED |
| C-READ.11.8.5 | Fed by | NOT DECIDED |
| C-READ.11.8.5 | Changes | NOT DECIDED |
| C-READ.11.8.6 | Fed by | NOT DECIDED |
| C-READ.11.8.6 | Changes | NOT DECIDED |
| C-READ.11.8.7 | Fed by | NOT DECIDED |
| C-READ.11.8.7 | Changes | NOT DECIDED |
| C-READ.11.8.8 | Fed by | NOT DECIDED |
| C-READ.11.8.8 | Changes | NOT DECIDED |
| C-READ.11.8.9 | Fed by | NOT DECIDED |
| C-READ.11.8.9 | Changes | NOT DECIDED |
| C-READ.11.8.10 | Fed by | NOT DECIDED |
| C-READ.11.8.10 | Changes | NOT DECIDED |
| C-READ.11.9 | Changes | NOT DECIDED |
| C-READ.11.9.1 | Changes | NOT DECIDED |
| C-READ.11.9.2 | Changes | NOT DECIDED |
| C-READ.11.9.2.1 | Fed by | NOT DECIDED |
| C-READ.11.9.2.1 | Changes | NOT DECIDED |
| C-READ.11.9.2.2 | Fed by | NOT DECIDED |
| C-READ.11.9.2.2 | Changes | NOT DECIDED |
| C-READ.11.9.2.3 | Fed by | NOT DECIDED |
| C-READ.11.9.2.3 | Changes | NOT DECIDED |
| C-READ.11.9.2.4 | Fed by | NOT DECIDED |
| C-READ.11.9.2.4 | Changes | NOT DECIDED |
| C-READ.11.9.2.5 | Fed by | NOT DECIDED |
| C-READ.11.9.2.5 | Changes | NOT DECIDED |
| C-READ.11.9.2.6 | Fed by | NOT DECIDED |
| C-READ.11.9.2.6 | Changes | NOT DECIDED |
| C-READ.11.9.2.7 | Fed by | NOT DECIDED |
| C-READ.11.9.2.7 | Changes | NOT DECIDED |
| C-READ.11.9.3 | Changes | NOT DECIDED |
| C-READ.11.9.4 | Fed by | NOT DECIDED |
| C-READ.11.9.4 | Changes | NOT DECIDED |
| C-READ.11.10 | Changes | NOT DECIDED |
| C-READ.11.10.1 | Changes | NOT DECIDED |
| C-READ.11.10.2 | Changes | NOT DECIDED |
| C-READ.11.10.2.1 | Fed by | NOT DECIDED |
| C-READ.11.10.2.1 | Changes | NOT DECIDED |
| C-READ.11.10.2.2 | Fed by | NOT DECIDED |
| C-READ.11.10.2.2 | Changes | NOT DECIDED |
| C-READ.11.10.3 | Changes | NOT DECIDED |
| C-READ.11.10.3.1 | Fed by | NOT DECIDED |
| C-READ.11.10.3.1 | Changes | NOT DECIDED |
| C-READ.11.10.3.2 | Fed by | NOT DECIDED |
| C-READ.11.10.3.2 | Changes | NOT DECIDED |
| C-READ.11.10.3.3 | Fed by | NOT DECIDED |
| C-READ.11.10.3.3 | Changes | NOT DECIDED |
| C-READ.11.10.4 | Changes | NOT DECIDED |
| C-READ.11.10.5 | Changes | NOT DECIDED |
| C-READ.11.10.6 | Changes | NOT DECIDED |
| C-READ.11.10.6.1 | Fed by | NOT DECIDED |
| C-READ.11.10.6.1 | Changes | NOT DECIDED |
| C-READ.11.10.6.2 | Fed by | NOT DECIDED |
| C-READ.11.10.6.2 | Changes | NOT DECIDED |
| C-READ.11.10.6.3 | Fed by | NOT DECIDED |
| C-READ.11.10.6.3 | Changes | NOT DECIDED |
| C-READ.11.10.7 | Changes | NOT DECIDED |
| C-READ.11.10.7.1 | Fed by | NOT DECIDED |
| C-READ.11.10.7.1 | Changes | NOT DECIDED |
| C-READ.11.10.7.2 | Fed by | NOT DECIDED |
| C-READ.11.10.7.2 | Changes | NOT DECIDED |
| C-READ.11.10.7.3 | Fed by | NOT DECIDED |
| C-READ.11.10.7.3 | Changes | NOT DECIDED |
| C-READ.11.10.8 | Changes | NOT DECIDED |
| C-READ.11.10.9 | Changes | NOT DECIDED |
| C-READ.11.10.10 | Changes | NOT DECIDED |
| C-READ.11.10.11 | Changes | NOT DECIDED |
| C-READ.11.10.11.1 | Fed by | NOT DECIDED |
| C-READ.11.10.11.1 | Changes | NOT DECIDED |
| C-READ.11.10.11.2 | Fed by | NOT DECIDED |
| C-READ.11.10.11.2 | Changes | NOT DECIDED |
| C-READ.11.10.12 | Changes | NOT DECIDED |
| C-READ.11.10.12.1 | Fed by | NOT DECIDED |
| C-READ.11.10.12.1 | Changes | NOT DECIDED |
| C-READ.11.10.12.2 | Fed by | NOT DECIDED |
| C-READ.11.10.12.2 | Changes | NOT DECIDED |
| C-READ.11.10.13 | Changes | NOT DECIDED |
| C-READ.11.10.14 | Changes | NOT DECIDED |
| C-READ.11.10.14.1 | Fed by | NOT DECIDED |
| C-READ.11.10.14.1 | Changes | NOT DECIDED |
| C-READ.11.10.14.2 | Fed by | NOT DECIDED |
| C-READ.11.10.14.2 | Changes | NOT DECIDED |
| C-READ.11.10.15 | Changes | NOT DECIDED |
| C-READ.11.10.15.1 | Changes | NOT DECIDED |
| C-READ.11.10.15.1.1 | Fed by | NOT DECIDED |
| C-READ.11.10.15.1.1 | Changes | NOT DECIDED |
| C-READ.11.10.16 | Changes | NOT DECIDED |
| C-READ.11.10.16.1 | Fed by | NOT DECIDED |
| C-READ.11.10.16.1 | Changes | NOT DECIDED |
| C-READ.11.10.16.2 | Fed by | NOT DECIDED |
| C-READ.11.10.16.2 | Changes | NOT DECIDED |
| C-READ.11.10.17 | Changes | NOT DECIDED |
| C-READ.11.10.18 | Changes | NOT DECIDED |
| C-READ.11.10.19 | Changes | NOT DECIDED |
| C-READ.11.10.20 | Changes | NOT DECIDED |
| C-READ.11.11 | Gated by | NOT DECIDED |
| C-READ.11.11 | Changes | NOT DECIDED |
| C-READ.11.11.1 | Fed by | NOT DECIDED |
| C-READ.11.11.1 | Changes | NOT DECIDED |
| C-READ.11.11.2 | Fed by | NOT DECIDED |
| C-READ.11.11.2 | Changes | NOT DECIDED |
| C-READ.11.11.3 | Fed by | NOT DECIDED |
| C-READ.11.11.3 | Changes | NOT DECIDED |
| C-READ.11.11.4 | Fed by | NOT DECIDED |
| C-READ.11.11.4 | Changes | NOT DECIDED |
| C-READ.11.11.5 | Fed by | NOT DECIDED |
| C-READ.11.11.5 | Changes | NOT DECIDED |
| C-READ.11.11.6 | Fed by | NOT DECIDED |
| C-READ.11.11.6 | Changes | NOT DECIDED |
| C-READ.11.11.7 | Fed by | NOT DECIDED |
| C-READ.11.11.7 | Changes | NOT DECIDED |
| C-READ.11.11.8 | Fed by | NOT DECIDED |
| C-READ.11.11.8 | Changes | NOT DECIDED |
| C-READ.11.11.9 | Fed by | NOT DECIDED |
| C-READ.11.11.9 | Changes | NOT DECIDED |
| C-READ.11.11.10 | Fed by | NOT DECIDED |
| C-READ.11.11.10 | Changes | NOT DECIDED |
| C-READ.11.12 | Changes | NOT DECIDED |
| C-READ.11.12.1 | Fed by | NOT DECIDED |
| C-READ.11.12.1 | Changes | NOT DECIDED |
| C-READ.11.12.2 | Fed by | NOT DECIDED |
| C-READ.11.12.2 | Changes | NOT DECIDED |
| C-READ.11.12.3 | Fed by | NOT DECIDED |
| C-READ.11.12.3 | Changes | NOT DECIDED |
| C-READ.11.12.4 | Fed by | NOT DECIDED |
| C-READ.11.12.4 | Changes | NOT DECIDED |
| C-READ.11.12.5 | Fed by | NOT DECIDED |
| C-READ.11.12.5 | Changes | NOT DECIDED |
| C-READ.11.12.6 | Fed by | NOT DECIDED |
| C-READ.11.12.6 | Changes | NOT DECIDED |
| C-READ.11.12.7 | Fed by | NOT DECIDED |
| C-READ.11.12.7 | Changes | NOT DECIDED |
| C-READ.11.12.8 | Fed by | NOT DECIDED |
| C-READ.11.12.8 | Changes | NOT DECIDED |
| C-READ.11.12.9 | Fed by | NOT DECIDED |
| C-READ.11.12.9 | Changes | NOT DECIDED |
| C-READ.11.12.10 | Fed by | NOT DECIDED |
| C-READ.11.12.10 | Changes | NOT DECIDED |
| C-READ.11.12.11 | Fed by | NOT DECIDED |
| C-READ.11.12.11 | Changes | NOT DECIDED |
| C-READ.11.12.12 | Fed by | NOT DECIDED |
| C-READ.11.12.12 | Changes | NOT DECIDED |
| C-READ.11.12.13 | Changes | NOT DECIDED |
| C-READ.11.12.13.1 | Fed by | NOT DECIDED |
| C-READ.11.12.13.1 | Changes | NOT DECIDED |
| C-READ.11.12.13.2 | Fed by | NOT DECIDED |
| C-READ.11.12.13.2 | Changes | NOT DECIDED |
| C-READ.11.12.13.3 | Fed by | NOT DECIDED |
| C-READ.11.12.13.3 | Changes | NOT DECIDED |
| C-READ.11.12.13.4 | Fed by | NOT DECIDED |
| C-READ.11.12.13.4 | Changes | NOT DECIDED |
| C-READ.11.12.13.5 | Fed by | NOT DECIDED |
| C-READ.11.12.13.5 | Changes | NOT DECIDED |
| C-READ.11.12.13.6 | Fed by | NOT DECIDED |
| C-READ.11.12.13.6 | Changes | NOT DECIDED |
| C-READ.11.12.14 | Changes | NOT DECIDED |
| C-READ.11.12.14.1 | Fed by | NOT DECIDED |
| C-READ.11.12.14.1 | Changes | NOT DECIDED |
| C-READ.11.12.14.2 | Fed by | NOT DECIDED |
| C-READ.11.12.14.2 | Changes | NOT DECIDED |
| C-READ.11.12.14.3 | Fed by | NOT DECIDED |
| C-READ.11.12.14.3 | Changes | NOT DECIDED |
| C-READ.11.12.15 | Fed by | NOT DECIDED |
| C-READ.11.12.15 | Changes | NOT DECIDED |
| C-READ.11.13 | Changes | NOT DECIDED |
| C-READ.11.13.1 | Fed by | NOT DECIDED |
| C-READ.11.13.1 | Changes | NOT DECIDED |
| C-READ.11.13.2 | Fed by | NOT DECIDED |
| C-READ.11.13.2 | Changes | NOT DECIDED |
| C-READ.11.13.3 | Fed by | NOT DECIDED |
| C-READ.11.13.3 | Changes | NOT DECIDED |
| C-READ.11.13.4 | Fed by | NOT DECIDED |
| C-READ.11.13.4 | Changes | NOT DECIDED |
| C-READ.11.13.5 | Fed by | NOT DECIDED |
| C-READ.11.13.5 | Gated by | NOT DECIDED |
| C-READ.11.13.5 | Changes | NOT DECIDED |
| C-READ.11.13.6 | Fed by | NOT DECIDED |
| C-READ.11.13.6 | Changes | NOT DECIDED |
| C-READ.11.1.1 | Exact serialization and integrity algorithm, where not specified by the existing referenced record | NOT DECIDED |
| C-READ.11.1.2 | Exact serialization and integrity algorithm, where not specified by the existing referenced record | NOT DECIDED |
| C-READ.11.1.3 | Exact serialization and integrity algorithm, where not specified by the existing referenced record | NOT DECIDED |
| C-READ.11.1.4 | Exact serialization and integrity algorithm, where not specified by the existing referenced record | NOT DECIDED |
| C-READ.11.2.1 | Exact physical record/field serialization; the source supplies the semantic member and proposed name only | NOT DECIDED |
| C-READ.11.2.2 | Exact physical record/field serialization; the source supplies the semantic member and proposed name only | NOT DECIDED |
| C-READ.11.2.3 | Exact physical record/field serialization; the source supplies the semantic member and proposed name only | NOT DECIDED |
| C-READ.11.2.4 | Exact physical record/field serialization; the source supplies the semantic member and proposed name only | NOT DECIDED |
| C-READ.11.2.5 | Exact physical record/field serialization; the source supplies the semantic member and proposed name only | NOT DECIDED |
| C-READ.11.2.6 | Exact physical record/field serialization; the source supplies the semantic member and proposed name only | NOT DECIDED |
| C-READ.11.3.1 | Exact identity encoding/generation algorithm beyond the source-defined stability, separation and uniqueness | NOT DECIDED |
| C-READ.11.3.2 | Exact identity encoding/generation algorithm beyond the source-defined stability, separation and uniqueness | NOT DECIDED |
| C-READ.11.3.3 | Exact identity encoding/generation algorithm beyond the source-defined stability, separation and uniqueness | NOT DECIDED |
| C-READ.11.7.10 | Exact integrity-reference field spelling, algorithm and serialization | NOT DECIDED |
| C-READ.11.7.3 | Exact external evidence-record format/location and policy values, where not specified by its owning package; no value supplied here | NOT DECIDED |
| C-READ.11.7.4 | Exact external evidence-record format/location and policy values, where not specified by its owning package; no value supplied here | NOT DECIDED |
| C-READ.11.7.5 | Exact external evidence-record format/location and policy values, where not specified by its owning package; no value supplied here | NOT DECIDED |
| C-READ.11.7.6 | Exact external evidence-record format/location and policy values, where not specified by its owning package; no value supplied here | NOT DECIDED |
| C-READ.11.5.4.1.1 | Exact serialization/type beyond the source-defined identity or record member | NOT DECIDED |
| C-READ.11.5.4.1.2 | Exact serialization/type beyond the source-defined identity or record member | NOT DECIDED |
| C-READ.11.5.4.1.3 | Exact serialization/type beyond the source-defined identity or record member | NOT DECIDED |
| C-READ.11.5.4.1.4 | Exact serialization/type beyond the source-defined identity or record member | NOT DECIDED |
| C-READ.11.5.4.1.5 | Exact serialization/type beyond the source-defined identity or record member | NOT DECIDED |
| C-READ.11.5.4.1.6 | Exact serialization/type beyond the source-defined identity or record member | NOT DECIDED |
| C-READ.11.5.4.1.7 | Exact serialization/type beyond the source-defined identity or record member | NOT DECIDED |
| C-READ.11.7.6 | Policy defining a passing per-reading promotion decision / evidence-combination rule | NOT DECIDED |
| C-READ.11.7.5 | Exact manual-inspection content/scoring threshold beyond the required recorded outcome | NOT DECIDED |
| C-READ.11.1 | Exact reading_integrity_ref algorithm and encoding | NOT DECIDED |
| C-READ.11.6 | Physical compare-and-commit/fence storage mechanism; logical atomicity and legal paths are specified | NOT DECIDED |
| C-READ.11.5.4.1 | Physical representation/location of the external eligibility record; no production store selected | NOT DECIDED |
| C-READ.11.7 | Exact physical evidence-record formats/locations and calibration values not specified by this seam | NOT DECIDED |

### Source-conflict register

| Location | Governing behavior | Lower-source wording retained |
|---|---|---|
| C-READ.11.9.4 | DESIGNED — V10 §0B: authorized operational-record retrieval, interpretation and triggered self-examination remain possible; privacy/access and no-double-evidence still bind. | ACCEPTED source B16 §7 says promotion records are never inputs to interpretation. This broader prohibition is preserved in the behavior-line SOURCE CONFLICT marker; it does not override V10 or license ordinary unrestricted use. |

### Outside this piece’s scope

| Matter | Disposition |
|---|---|
| B16 promotion evaluation-evidence bridge | NOT PLACED here: the distinct accepted v1.7 package defines evidence-result generation and later exact applicability checks. The source and receipt were checked for identity, standing and the frozen B16 boundary; their complete behavior belongs to a subsequent piece. Gold/held-out evidence is still required; nothing here fabricates a passing result. |
| B16 §5.3 input-3 source wording | The frozen base calls it recorded B24-architecture acceptance evidence for the applicable gold-set run. The later bridge receipt identifies this as an undrawn connection supplied by the distinct bridge. This piece records the required gold-results reference without asserting a B24 per-run record exists or treating B24 system eligibility as gold-results evidence. |
| B16 §12 external dependencies | NOT PLACED here: hold/release policy and mechanics, B9 retry policy/values, B10 reread identity/recovery, the connected B-CYCLE-6 flow, and B1/B26 retrieval behavior remain with their owning packages and chapters. A base-package open note is not treated as proof that a later accepted owner is still undecided. |
| Production marker enforcement and physical storage | No build claim: the marker check is designed in V10, and B16 selects no production store, migration or physical backend. C2 and implementation remain outside this behavior piece. |
| Restored bootstrap and memory-health rules | Remain in corrected Chapter 3-b with DECIDED-2026-09-25 stamps; no scheduler, threshold or modification of checked memory is introduced here. |
| Remaining Group A components | C-ENGINE-AB, C-ENGINE-C, C-INDEX, C-GOLD, C-INGEST and C-DETECT remain for later Chapter 3 pieces. |

## Coverage matrix — Chapter 3-d contribution

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
| F052 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | §§3–7, 9 and 13 checked for the distinct bridge’s accepted source standing, conditional closure, fixed identity and no-reopen B16 boundary. NOT PLACED: bridge behavior; receipt is not used to manufacture evidence results or replace the full source. |
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
| F112 | `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` | Carried through Chapter 3-a: Earlier Chapter 0 read only; not reread at this pin; Chapter 3-d scoped §§9 and 12 check only; no whole-read credit | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-d scope check: later evidence applicability is distinct and remains NOT PLACED; no bridge mechanism reconstructed from excerpts. |
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

### B16 detailed landing map

| Source section | Complete landing |
|---|---|
| [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §1] [NHD-B16] | C-READ.11 |
| [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.1] [NHD-B16] | C-READ.11.1, C-READ.11.1.1, C-READ.11.1.2, C-READ.11.1.3, C-READ.11.1.4 |
| [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.2] [NHD-B16] | C-READ.11.2, C-READ.11.2.1, C-READ.11.2.2, C-READ.11.2.3, C-READ.11.2.4, C-READ.11.2.5, C-READ.11.2.6 |
| [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §3.3] [NHD-B16] | C-READ.11.3, C-READ.11.3.1, C-READ.11.3.2 |
| [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §6] [NHD-B16] | C-READ.11.3.3, C-READ.11.8, C-READ.11.8.1, C-READ.11.8.2, C-READ.11.8.3, C-READ.11.8.4, C-READ.11.8.5, C-READ.11.8.6, C-READ.11.8.7, C-READ.11.8.8, C-READ.11.8.9, C-READ.11.8.10 |
| [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §4] [NHD-B16] | C-READ.11.4, C-READ.11.4.1, C-READ.11.4.2, C-READ.11.4.3, C-READ.11.4.4, C-READ.11.4.5, C-READ.11.4.6, C-READ.11.4.7, C-READ.11.4.8, C-READ.11.4.9 |
| [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.2] [NHD-B16] | C-READ.11.6, C-READ.11.6.1, C-READ.11.6.2, C-READ.11.6.3, C-READ.11.6.4, C-READ.11.6.5, C-READ.11.6.6, C-READ.11.6.7, C-READ.11.6.7.1, C-READ.11.6.7.2, C-READ.11.6.7.3, C-READ.11.6.7.3.1, C-READ.11.6.7.3.2, C-READ.11.6.7.3.3, C-READ.11.6.7.3.4, C-READ.11.6.8, C-READ.11.6.9 |
| [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5] [NHD-B16] | C-READ.11.5, C-READ.11.5.1, C-READ.11.5.2, C-READ.11.5.3, C-READ.11.5.4, C-READ.11.5.5, C-READ.11.5.6, C-READ.11.5.2.1, C-READ.11.5.2.1.1, C-READ.11.5.2.1.2, C-READ.11.5.2.1.3, C-READ.11.5.2.1.4, C-READ.11.5.2.1.5, C-READ.11.5.4.1, C-READ.11.5.4.1.1, C-READ.11.5.4.1.2, C-READ.11.5.4.1.3, C-READ.11.5.4.1.4, C-READ.11.5.4.1.5, C-READ.11.5.4.1.6, C-READ.11.5.4.1.7 |
| [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3] [NHD-B16] | C-READ.11.7, C-READ.11.7.1, C-READ.11.7.2, C-READ.11.7.3, C-READ.11.7.4, C-READ.11.7.5, C-READ.11.7.6, C-READ.11.7.7, C-READ.11.7.8, C-READ.11.7.9, C-READ.11.7.1.1, C-READ.11.7.1.2, C-READ.11.7.1.3, C-READ.11.7.7.1, C-READ.11.7.7.2, C-READ.11.7.10 |
| [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §7] [NHD-B16] | C-READ.11.9, C-READ.11.9.1, C-READ.11.9.2, C-READ.11.9.2.1, C-READ.11.9.2.2, C-READ.11.9.2.3, C-READ.11.9.2.4, C-READ.11.9.2.5, C-READ.11.9.2.6, C-READ.11.9.2.7, C-READ.11.9.3, C-READ.11.9.4 |
| [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §8] [NHD-B16] | C-READ.11.10, C-READ.11.10.1, C-READ.11.10.2, C-READ.11.10.3, C-READ.11.10.4, C-READ.11.10.5, C-READ.11.10.6, C-READ.11.10.7, C-READ.11.10.8, C-READ.11.10.9, C-READ.11.10.10, C-READ.11.10.11, C-READ.11.10.12, C-READ.11.10.13, C-READ.11.10.14, C-READ.11.10.15, C-READ.11.10.16, C-READ.11.10.17, C-READ.11.10.18, C-READ.11.10.19, C-READ.11.10.20, C-READ.11.10.2.1, C-READ.11.10.2.2, C-READ.11.10.3.1, C-READ.11.10.3.2, C-READ.11.10.3.3, C-READ.11.10.6.1, C-READ.11.10.6.2, C-READ.11.10.6.3, C-READ.11.10.7.1, C-READ.11.10.7.2, C-READ.11.10.7.3, C-READ.11.10.11.1, C-READ.11.10.11.2, C-READ.11.10.12.1, C-READ.11.10.12.2, C-READ.11.10.14.1, C-READ.11.10.14.2, C-READ.11.10.16.1, C-READ.11.10.16.2, C-READ.11.10.15.1, C-READ.11.10.15.1.1 |
| [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §9] [NHD-B16] | C-READ.11.11, C-READ.11.11.1, C-READ.11.11.2, C-READ.11.11.3, C-READ.11.11.4, C-READ.11.11.5, C-READ.11.11.6, C-READ.11.11.7, C-READ.11.11.8, C-READ.11.11.9, C-READ.11.11.10 |
| [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §10] [NHD-B16] | C-READ.11.12, C-READ.11.12.1, C-READ.11.12.2, C-READ.11.12.3, C-READ.11.12.4, C-READ.11.12.5, C-READ.11.12.6, C-READ.11.12.7, C-READ.11.12.8, C-READ.11.12.9, C-READ.11.12.10, C-READ.11.12.11, C-READ.11.12.12, C-READ.11.12.13, C-READ.11.12.13.1, C-READ.11.12.13.2, C-READ.11.12.13.3, C-READ.11.12.13.4, C-READ.11.12.13.5, C-READ.11.12.13.6, C-READ.11.12.14, C-READ.11.12.14.1, C-READ.11.12.14.2, C-READ.11.12.14.3, C-READ.11.12.15 |
| [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §11] [NHD-B16] | C-READ.11.13, C-READ.11.13.1, C-READ.11.13.2, C-READ.11.13.3, C-READ.11.13.4, C-READ.11.13.5, C-READ.11.13.6 |
| [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §12] [NHD-B16] | Scoped gaps and outside-owner table; no external policy or implementation invented. |
| [04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §13] [NHD-B16] | Trace coverage: 1 snapshot gate; 2 reservation/fence race; 3 precommit crash exclusion; 4 orphan invalidation; 5 absorbing duplicate/recovery; 6 rejection/hold exclusion; 7 no rewrite; 8 parent/child logs before acknowledgement. These introduce no separate runtime part beyond the complete cards above. |

## READ RECORD

### Files read whole for this piece

- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`

B16 v1.0 was read through all 593 lines in ranges 1–205, 197–397 and 398–593. Its receipt was read through all 166 lines. The separate bridge receipt was read through all 234 lines in overlapping ranges, including its exact accepted-source identity, conditional closure, scope and frozen-source boundary. The bridge source itself was only checked at §§9 and 12 and was not reread whole for this piece; no bridge behavior is claimed delivered. Both the base and later bridge source bytes were matched to their pinned Git blob identities; the base identity matches its acceptance receipt.

### Earlier whole-read sources reopened in scope

| File | Scope checked |
|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Status table; §0B living records, authorization and no-double-evidence; §6A protection/production authorization; §6B reading immutability and identity. No new whole-read credit. |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | §§3A–3C reading, root and quarantine/production boundaries. No new whole-read credit. |
| `01_AUTHORITATIVE/cursorrules` | §1C validation, direct-write, marker and quarantine prohibitions. No new whole-read credit. |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | C-READ/Group A names; CY-G; B16 seam versus B-CYCLE-6/C2 ownership. No new whole-read credit. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | NHD-B16 and the distinct bridge navigation pointers; not a behavior source. No new whole-read credit. |

The cloned contract was reread for §§5–11 before writing and §11.3 after writing, hash `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1`. The attached round 1 request and project instructions were read as task instructions. Earlier chapter files were inspected for IDs, names, links and coverage. No source, original chapter, completed CH03-c or round 2 chapter was edited.

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

### Pinned source identities checked

| File | Bytes | SHA-256 | Git blob at pin |
|---|---|---|---|
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md` | 44891 | `0da231c71c4ea17f1e960de4f5f7a117c6f20df2b63ab597e732f824ccaadfb1` | MATCH |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | 8326 | `3bcbc861ce8cd1956f985265d90cdce1d126849f54d79b7d7fa1fba85991270f` | MATCH |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | 27358 | `298de053269f4a9e93e97dfd994d33b0b879d71af636b169769264e7183d9d4c` | MATCH |
| `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` | 135956 | `04dd5abc42e59afb61b4d280a0bb69d647d187fd0da385bc5c567eddbca81a41` | MATCH |
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | 506934 | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` | MATCH |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | 37048 | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` | MATCH |
| `01_AUTHORITATIVE/cursorrules` | 34821 | `5050d08825b93acd72a79d07946e43c8cbe537e079517ccfe66bcae8e30e96e9` | MATCH |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | 465376 | `cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb` | MATCH |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | 286256 | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` | MATCH |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | 130915 | `aad8d1aeee9a331ad6f4d9ddbcfa9c42eae2a94e1ef1bccde7484079181ff7b4` | MATCH |

## CONTRACT CHECK

CONTRACT CHECK (against the cloned contract, SHA-256 e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1)
§1.3 no history/actions/roles/workflow in this chapter: PASS — all 189 behavior cards, their reciprocal rows and register contributions checked. Source history, acceptance workflow and delivery narrative are excluded from behavior; source status and reading evidence are identified separately.
§1.4 every gap written as NOT DECIDED: PASS — all 567 Must never / Fails closed by / Gated by placements reviewed. Every card carries its decided prohibition and failure outcome. Eight Gated by boxes remain empty only where no separate gate is specified for that part. All 333 empty template fields and 31 scoped unspecified details are registered; known outside owners are NOT PLACED here rather than declared globally undecided.
§1.5 conflicts marked, none resolved: PASS — C-READ.11.9.4 preserves B16 §7’s interpretation prohibition in a SOURCE CONFLICT marker against governing V10 §0B authorized living-record retrieval, interpretation and self-examination. V10 governs; privacy and no-double-evidence remain binding.
§3 exactly one stamp per line: PASS — 1550 populated field lines, 397 USED BY rows and the cross-piece entries checked. B16 behavior is ACCEPTED through its exact-source receipt; the governing V10 behavior is DESIGNED. No B16 machinery is stamped BUILT and no implementation is claimed.
§4 every behavior line cited in the exact format: PASS — all behavior fields and reciprocal entries carry source citations; all 16 distinct citation targets resolve. Record-definition citations are supplemented by the exact recovery, failure, logging or consumption section when that section supplies the carried outcome. Source identity, scope and accepted standing were checked separately from behavior.
§5.4 one name per thing: PASS — all 189 IDs and canonical names checked against the C-READ continuation and existing endpoint names. Numeric order follows first source introduction; the eligibility record is nested under its commit boundary. Identically spelled lifecycle states, reservation phases and operation-log outcomes are explicitly qualified as distinct uses.
§6 all template fields present, in order, for every part: PASS — all 189 cards contain the nine fields in order, ALONE, TOGETHER, USED BY and SUB-PARTS. Every leaf ends with SUB-PARTS: NONE; every listed child exists in the delivered text.
§6.3 reciprocity within this chapter: PASS — 396 internal relationship pairs checked in both directions; ten external pairs have explicit reciprocal entries recorded here. The existing C-READ continuation and CY-G use are recorded here without editing or merging another chapter. Commit steps name their defining rule cards and those cards name the steps in USED BY.
§6.4 every decided detail written in, no citation used in place of content: PASS — the complete per-reading seam carries record members and identities, nine lifecycle states, six reservation phases, three legal paths, four strict recovery proofs, six transaction boundaries, nine evidence inputs, ten idempotency points, all twenty recovery cases and their separate outcomes, ten failure classes, named log events and six permanent boundaries. The row-16 recovery pointer is expanded into its actual behavior. The distinct evaluation bridge and full cycle are explicitly outside this piece.
§6.5 sub-parts recursed to the bottom: PASS — required record members, nested evidence references, phase conditions, strict recovery proofs, state exclusions, recovery branches, invalidation cause, parent outcomes and log identity members are explicit cards. No serialization, threshold, retry policy, evidence result or implementation mechanism is invented.
§9 coverage matrix rows added for every file used: PASS — all 138 file rows and 107 V10 heading rows retained and relevant placements updated; a detailed B16 section landing map is included. Ten pinned source blob identities and the cloned contract hash verified. Three source/receipt files reread whole; scoped bridge and governing-file checks receive no new whole-read credit. The 97-entry pending list retains the earlier accounting.
§10.11 no recommendation, no sentence addressed to Ness: PASS — checked throughout the behavior and register text. Proposed source names remain proposed; no acceptance, execution or implementation recommendation is added.
Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`; instruction file `NH_MASTER-21_SYSTEM_BEHAVIOR_BUILD_CONTRACT_FOR_CHATGPT_v1_0.md`. Scoped rereads and earlier credits are distinguished in READ RECORD.

This is the producing assistant’s contract check, not an independent audit or adoption. The completed corrected Chapter 3-c remains byte-identical at SHA-256 `20d022f2d237cf0a29e4128eae510e0cf153505a2ffd0c64ff512fed9cb06fa6`. Round 2 is not delivered.
