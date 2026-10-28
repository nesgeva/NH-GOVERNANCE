# N.H — ROUTE FROM MASTER-21 TO THE FINISHED SYSTEM DESCRIPTION

**File:** `03_WORKFLOW/NH_MASTER-21_TO_FINAL_SYSTEM_DESCRIPTION_ROUTE_v0_1_CANDIDATE.md`
**Status:** CANDIDATE — not accepted, not adopted. Pending independent audit and Ness's acceptance.
**Repository:** `nesgeva/NH-GOVERNANCE`
**Source commit read:** `33350b94e536e0e4f1557dccd4ae255ef33a3861`
**Authority order (unchanged by this file):** `NH_MASTER-20_CORRECTED_v10.md` → `NH_DECISION_DEFAULTS-S19_v2_2.md` → `cursorrules` → `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`. The Working Map remains subordinate.

---

## 0. What this file is, and what it is not

This file records the route Ness has stated for moving from the Master-21 system-behavior document to a finished description of N.H as a completed system.

It **records** that route. It does not execute it.

Specifically, this file:

- performs no adoption, and does not move, edit, retire, or supersede `NH_MASTER-20_CORRECTED_v10.md` or any other authoritative file;
- answers no design gap and settles no concept decision;
- creates no gap-decisions file and no finished description;
- authorizes no building, no code, no store or seal change;
- allocates no new controlled IDs and performs no Master or Map integration;
- changes neither the authority order above nor N.H's runtime behavior.

This file is not architectural authority. Every stage below is a **planned** step. None of the events described here has occurred as of this file's creation.

---

## 1. Stage 1 — Master-21 becomes authority through Ness's explicit adoption

The route begins when the Master-21 system-behavior document is complete and audited, and Ness explicitly adopts it, identifying it by its exact version and SHA-256 hash.

On that adoption, and only then:

- Master-21 becomes the authoritative Master;
- `NH_MASTER-20_CORRECTED_v10.md` becomes preserved history, retained and unedited.

Until that adoption occurs, V10 remains authoritative. This follows V10 §2A's version-safety rule: a new versioned file is created and never silently overwrites the previous authoritative master, which stays authoritative until Ness reviews and adopts the new one.

### 1.1 `NOT DECIDED` is binding on adoption

Master-21 may contain `NOT DECIDED` entries when it is adopted. These entries are binding statements that the corresponding design is unresolved.

Adoption does **not** supply the missing answers and does not permit any assistant, auditor, or builder to invent them. Nothing may be designed onward from, or built on, an unresolved hole.

### 1.2 Scope of that restriction

The preceding rule is a design-and-build restriction on the people and assistants doing this work. It is **not** a change to N.H's runtime rules for handling uncertain or incomplete evidence, which remain exactly as the governing sources define them.

### 1.3 Planned, not performed

The adoption described in this stage is a planned step belonging to Ness alone. Creating this workflow file performs no part of it.

---

## 2. Stage 2 — Ness resolves the holes through one growing gap-decisions file

Every `NOT DECIDED` entry and every other recorded gap in the adopted Master-21 is resolved by Ness, and the resolutions are recorded in one cumulative logical document.

### 2.1 Shape of the record

- **One cumulative document**, not one file per hole.
- **Grouped by Master-21's existing part and sub-part IDs.** Controlled IDs are used as they are; none is renamed, and no owning part is invented for a gap whose ownership Master-21 leaves unassigned. Explicitly unassigned ownership is preserved as unassigned.
- **Each entry points to its exact gap location** in Master-21, and path references are preserved as written.

### 2.2 Versioning

Each recorded answer or correction produces a **new versioned file containing the accumulated record**. An earlier version is never edited in place. Earlier decisions and their evidence are preserved. Any revision Ness authorizes records what it supersedes.

### 2.3 Recovery check — required before any hole is presented or answered

Before a hole is put to Ness, and before any answer is recorded, these are checked:

- `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_2026-09-24_v0_1_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md`

Relevant FR-IDs are followed to their cited source passages, and later decisions or supersession are checked. Master-21 itself and the relevant accepted decisions are checked alongside them.

The recovery precedence rule is preserved as recorded on 2026-09-24: a feature completed before V10 stays chosen unless a later recorded decision put a different feature in its place; silent dropping or compression is not replacement.

An answer that already exists is **recovered with its source**, not presented to Ness as a fresh choice and not silently replaced.

The recovery records' own distinctions are preserved and not flattened: restored behavior; names kept for the historical register only; tool names held as candidates; intents; and genuinely undecided matters. The ledger alone does not authorize restoration.

### 2.4 What reaches Ness

Only the genuinely unresolved remainder is put to Ness. It is explained plainly, with the existing constraints and the consequences of each direction identified.

Assistants may investigate, gather evidence, and propose. They may not settle a new design decision. Ness's explicit answer is what is recorded.

### 2.5 What each entry retains

- the gap, as stated in Master-21;
- the affected IDs and the exact location;
- the recovery checks performed and the sources they reached;
- Ness's answer, with its date and provenance where available;
- the resulting rule;
- remaining dependencies;
- any explicit supersession.

Dates and decision evidence are never invented. Where provenance is unavailable, that is stated.

---

## 3. Stage 3 — After every hole is resolved, derive the finished system description

### 3.1 Source pair

The finished description is derived from exactly two sources: the adopted Master-21, and the accumulated gap-decisions file holding Ness's recorded answers.

### 3.2 Completeness gate before derivation

Before derivation begins, it is verified that every gap has a supported resolution and that the combined description is consistent and complete.

Deleting a `NOT DECIDED` marker, hiding an omission, or replacing it with plausible prose does not resolve it. Any missing behavior discovered at this stage returns to the Stage 2 gap-decision process.

### 3.3 What is derived

N.H described at full behavioral depth as one connected machine: its parts, inputs, outputs, paths, conditions, permissions, boundaries, failure behavior, and recovery behavior.

No build-status stamps appear in the finished description. Source traceability and decided detail are preserved. Connecting mechanisms are not invented, decisions are not silently changed, and a high-level summary is not substituted for actual behavior.

### 3.4 Scope of the no-stamp rule

The no-stamp rule applies to this later finished description only. It does not authorize removing or altering stamps in Master-21, and it does not change Master-21's current production contract.

---

## 4. Stage 4 — Intended behavior stays separate from implementation status

The finished description states how the completed system is **intended** to behave. It is not evidence that any of that behavior exists in code.

Built-versus-designed tracking and implementation verification remain separate work, governed separately.

A complete description, an accepted decision, and the adoption of a new authority do not, singly or together, grant permission to build. Building requires Ness's separate explicit authorization.

---

## 5. Relationship to `NH_FULL_DESIGN_COMPLETION_WORKFLOW_v1_0.md`

That file (2026-06-30) remains in place, unedited by this one, and is not superseded by this file.

One sequencing difference is recorded here without being resolved:

- **Workflow v1.0, Phase 18** places the decision about a new Master candidate *after* the complete design map is accepted, and lists its conditions accordingly.
- **The route recorded here** adopts Master-21 while `NOT DECIDED` entries remain inside it, and resolves those entries afterward, in Stage 2.

The route in this file is Ness's stated instruction for this work. It is recorded as such. Older workflow sequencing is not silently reversed, and this file does not amend Phase 18; any reconciliation is a separate, later act belonging to Ness.

Workflow v1.0's Phase 19 implementation-readiness gate — which requires that every blocking concept be decided and that Ness explicitly authorize implementation — is consistent with Stage 4 above and is not modified.

---

## 6. Open dependencies

- Master-21 is incomplete at the time of writing. Chapters 00, 01 and 02 exist in `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/`; later chapters, the appendices, and the joined document do not yet exist. Stage 1 cannot begin until they do.
- The gap inventory that Stage 2 consumes is produced by Master-21's own appendix work and does not exist yet.
- `NH_MASTER-21_SYSTEM_BEHAVIOR_BUILD_CONTRACT_FOR_CHATGPT_v1_0.md` is not present in this repository at the source commit. Its rules are therefore not quoted in this file, and nothing here should be read as restating them.
- The decision index candidates `v0_10` and `v0_11` contain no entry for Master-21 or for this route. Index acceptance creates no acceptance of this file, and a new index version will be needed if this route is accepted.

---

## 7. Self-audit

- All four stages recorded as instructed, in order, with their stated restrictions intact.
- Recovery checks are required before every gap decision (§2.3), ahead of Ness being asked.
- Prior versions of the gap-decisions record are immutable (§2.2).
- No planned event is reported as completed; Stage 1 adoption is marked planned in §1.3, and §0 states that none of the described events has occurred.
- No adoption declared, no authority order changed, no controlled ID allocated, no gap resolved, no file other than this one created or altered.
- Target path did not already exist at the source commit; no collision.
- One source named in the task was unavailable and is identified as such in §6 rather than claimed as read.
