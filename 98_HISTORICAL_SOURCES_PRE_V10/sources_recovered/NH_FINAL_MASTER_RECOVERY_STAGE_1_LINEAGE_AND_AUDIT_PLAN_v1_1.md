# N.H — FINAL-MASTER RECOVERY — STAGE 1: LINEAGE AND AUDIT PLAN v1.1

**This is the corrected successor to v1.** It applies only planning- and classification-level
corrections (see the Correction Ledger at the end). No architecture, source content, comparison
evidence, hash, byte count, or settled N.H decision was altered.

**Scope of this file.** This is a *planning and lineage* document only. It establishes what exists,
how the versions descend from one another, how the files separate by role, the exact order in which
they must later be compared, and a *provisional Stage-1* feature-category map of the N.H architecture.

**This file performs NO recovery.** It does not merge, restore, rewrite, reconcile, adopt any
candidate, resolve any conflict, fill any gap, or ask any architecture question. Those are later
stages and require Ness. Where evidence does not settle a point, the point is left open and labeled.

**Authority is unchanged.** The four adopted authority files remain authoritative. The preservation
package (handoff, reader index, Parts 01–11) is **evidence and recovery material only**; presence in
it confers no authority.

---

## 0. PRESERVED GOVERNING RULES (carried into every later stage)

These rules from Ness's protocol govern the entire recovery and are restated here so they travel with
the plan:

1. Newer does not automatically mean more complete.
2. Later absence does not prove rejection.
3. A summary does not replace a full mechanism.
4. "Not built" does not mean "not accepted."
5. Companion files may contain accepted designs not yet integrated into the Master.
6. Conflicting designs must never be silently combined.
7. Ness decides every critical functional, architectural, privacy, security, memory, cognition, and
   control decision.
8. Source order in the Preservation Master implies nothing about authority, recency, or completeness.

---

## 1. ACCESSIBILITY CONFIRMATION

Every file required for Stage 1 was opened directly in this environment (not inferred from a summary).
The four authority files were hash-checked against the preservation record; all 11 reader parts were
hash-checked against the reader index. **All hashes matched exactly.**

**The accessible working set is 17 files:**
- 4 current authority-set files (Master, Decision Defaults, Cursor Rules v3.2, governance companion);
- 1 preservation handoff (`NH_NEW_CHAT_HANDOFF_AFTER_FULL_PROJECT_PRESERVATION_v1.md`);
- 1 reader index (`NH_COMPLETE_PROJECT_PRESERVATION_MASTER_v1_INDEX.md`);
- 11 reader parts (`…PART_01.md` through `…PART_11.md`).

(4 + 1 + 1 + 11 = 17. v1 mis-stated this as 16; corrected here and in the verification report.)

### 1.1 Authority files (all accessible; live hash = preservation-recorded hash)

| Role | File | SHA-256 (verified live) | Match |
|---|---|---|---|
| Authoritative Master | `NH_MASTER-19_CORRECTED_v7_1.md` | `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf` | ✓ |
| Authoritative Decision Defaults | `NH_DECISION_DEFAULTS-S19_v2_2.md` | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` | ✓ |
| Code ruleset (Cursor Rules v3.2) | `cursorrules__1_` | `5050d08825b93acd72a79d07946e43c8cbe537e079517ccfe66bcae8e30e96e9` | ✓ |
| Governance/archive companion | `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | `cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb` | ✓ |

**These four are not interchangeable authorities. Each is authoritative only within its declared scope:**
- `NH_MASTER-19_CORRECTED_v7_1.md` — **architectural authority** (the system design).
- `NH_DECISION_DEFAULTS-S19_v2_2.md` — **behavioral / defaults authority** (how design and build
  sessions behave).
- Cursor Rules v3.2 (`cursorrules__1_`) — **operational coding authority** (the code ruleset in force).
- `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` — **governance, accepted-design, and provenance
  authority within its declared scope; explicitly NOT an independent architectural authority.** Where
  it records accepted designs, those carry Master authority only after being patched into the Master
  through the patch-only protocol.

### 1.2 Handoff and reader index (accessible)

- `NH_NEW_CHAT_HANDOFF_AFTER_FULL_PROJECT_PRESERVATION_v1.md` — read in full.
- `NH_COMPLETE_PROJECT_PRESERVATION_MASTER_v1_INDEX.md` — read in full.

### 1.3 Reader Parts 01–11 (accessible; live hash = index-declared hash)

**Line-range convention (corrected):** ranges are **inclusive, zero-based** `[start, end]`, contiguous
(each part's start = the previous part's end + 1). The full file is 42,177 lines, so the last
zero-based line index is **42176**; the final range therefore ends at 42176, not 42177. (The reader
index labels the final range "39879–42177"; that endpoint reflects a one-based line *count*, not a
zero-based inclusive index. Only the range label is corrected here — no file, hash, byte count, line
count, or reconstructed content is altered.)

| Part | Live SHA-256 | Match | Source blocks | Full-file line range |
|---|---|---|---|---|
| 01 | `2a7e7cd3156d42f106c47d7bf7e66cea28c4c6cd6842aab1211ac6959cfcbf22` | ✓ | SRC-001–012 | 0–4344 |
| 02 | `1b7c789d3f2d39ae51353af64849c0ed37d99dbc8a52185656e4cfd6b5e86705` | ✓ | SRC-013–027 | 4345–8320 |
| 03 | `07071cef27fc8aea92edc41b8ca0164ddade79294cf872066f25eb456da41e96` | ✓ | SRC-028–038 | 8321–12532 |
| 04 | `d4932ddee259400b681a7e5ee84bd0cb8c219a1e4d423babc0450532123d83d8` | ✓ | SRC-039–040 | 12533–15176 |
| 05 | `d53cb55c0a6b7152031dcf0e2e067c401bbcd404d14c25c15b2b6fe68168cbf0` | ✓ | SRC-041–042 | 15177–18897 |
| 06 | `ab4308aeaf393c9908ea5a4711fb90dbcfca17370001765f0e74a974609cf3f9` | ✓ | SRC-043–044 | 18898–22775 |
| 07 | `931f5913936db2db1b88aae63a65e2d7027d621b364cdef41cfb116a3f988de1` | ✓ | SRC-045–051 | 22776–26601 |
| 08 | `7f1faebdbec81c34ce2c217f01184cd28874a3b4af8b8a422c1e3fe065decba7` | ✓ | SRC-052–069 | 26602–30471 |
| 09 | `cdf34b2c483bc7bbb267eb0964fd19cd2493d8396d24a509dc330e2f67ae69b1` | ✓ | SRC-070–086 | 30472–34282 |
| 10 | `5cf908f551a7db8ba9f7c28f556718d3703465889ec3d116b8312e8185b7eb11` | ✓ | SRC-087 | 34283–39878 |
| 11 | `5aa54c04567ef141bfef7d2a04660ae1649bdb59d4db7fd695256c495cb01b43` | ✓ | SRC-088–092 | 39879–42176 |

The reader index declares the full Preservation Master as 42,177 lines / 5,195,926 bytes /
SHA-256 `6f458f8b330a05fe6094afc7b39b117e52147f290be0d288245b7e07bff390b6`, reconstructible by
concatenating Parts 01–11 after stripping each part's banner. **This Stage 1 pass did not
re-run that concatenation reconstruction** (the index records it as already independently verified);
it verified the integrity of each part file by hash instead. This is the one verification step
delegated rather than re-performed, and it is flagged here so it is not mistaken for a fresh check.

### 1.4 What is NOT present (named in the package, not physically supplied)

These cannot be examined in any later stage until supplied. They are out of scope for comparison
until then and **must not be treated as rejected merely because they are absent** (Rule 2).

- **Unadopted candidates:** `NH_MASTER-19_CORRECTED_v8.md`, `NH_DECISION_DEFAULTS-S19_v2_3.md`,
  `cursorrules_v3_3`.
- **Masters referenced but absent:** `NH_MASTER-9.1`, `NH_MASTER-9.3`, `NH_MASTER-12`,
  `NH_MASTER-15`, `NH_MASTER-16`, `NH_MASTER-16_FINAL_CORRECTED.md`, `NH_MASTER-17_DRAFT.md`,
  `NH_MASTER-19_v7`, `NH_MASTER-19_CORRECTED_v2`, `NH_MASTER-19_v4`, `NH_MASTER-19_v5`.
- **Decision Defaults absent:** `NH_DECISION_DEFAULTS-S17_DRAFT.md`,
  `NH_DECISION_DEFAULTS-S19_v2_1.md`.
- **Gold sets absent:** `NH_GOLD_SET_v1.md`, `NH_GOLD_SET_v2_B.md`, `NH_GOLD_SET_CONTEXT_v1.md`.
- **Unrecoverable historical body:** the **Batch-1 body** of `NH_Meaning_Engine_Design.md`
  (historical SHA `18185908…`, 12,474 B / 137 lines) — overwritten on disk by the Batch-5 body
  (`15c2786…`, SRC-058). The B5 body is preserved separately and was **not** substituted. The B1
  body is classified **UNRECOVERABLE HISTORICAL SOURCE BODY — CONTENT CLASSIFICATION UNCLEAR**: its
  bytes are unavailable, so its content or design role cannot be inferred or examined.
- Ingest stores, several runtime `.py`, prototype/output HTML, and other design/handoff files named
  in Preservation §7 but not supplied.

---

## 2. MASTER LINEAGE (reconstructed from filenames, sizes, and declared content)

**Reconstruction basis.** This lineage is built from filename version tokens, byte/line sizes
(evidence, not verdict), and the preservation provenance. **It is a provisional ordering for the
comparison plan, not a decision about which body wins.** Where ordering between near-siblings cannot
be settled from filenames/sizes alone, it is marked **UNCLEAR — confirm by content in audit.**

### 2.1 The corrected/numbered Master spine (oldest → newest by version token)

| Step | File | SRC | Bytes | Lines | Lineage classification (file-level) |
|---|---|---|---|---|---|
| 1 | `NH_MASTER-5.md` | SRC-046 | 32,737 | 223 | HISTORICAL EXPLANATION ONLY (predecessor) |
| 2 | `NH_MASTER-6.md` | SRC-047 | 45,407 | 273 | HISTORICAL EXPLANATION ONLY |
| 2b | `NH_MASTER-6__1_.md` | SRC-048 | 54,506 | 315 | UNCLEAR (variant of MASTER-6 — order vs SRC-047 not settled by filename) |
| 3 | `NH_MASTER-7.md` | SRC-049 | 60,439 | 332 | HISTORICAL EXPLANATION ONLY |
| 4 | `NH_MASTER-8.md` | SRC-050 | 80,833 | 423 | HISTORICAL EXPLANATION ONLY |
| 5 | `NH_MASTER-9.md` | SRC-051 | 89,479 | 442 | HISTORICAL EXPLANATION ONLY |
| 5b | `NH_MASTER-9_2.md` | SRC-052 | 127,717 | 513 | UNCLEAR (9-series variant ordering) |
| 5c | `NH_MASTER-9_4.md` | SRC-053 | 149,631 | 580 | UNCLEAR (9-series variant ordering; 9.1/9.3 absent) |
| 6 | `NH_MASTER-10.md` | SRC-022 | 74,496 | 406 | HISTORICAL EXPLANATION ONLY |
| 6b | `NH_MASTER-10__1_.md` | SRC-023 | 75,898 | 407 | UNCLEAR (10-variant ordering) |
| 7 | `NH_MASTER-11.md` | SRC-024 | 91,643 | 443 | UNCLEAR (note: 11 is LARGER than 11_1) |
| 7b | `NH_MASTER-11_1.md` | SRC-025 | 80,040 | 482 | UNCLEAR (11_1 fewer bytes / more lines than 11 — size is not order) |
| 8 | `NH_MASTER-13.md` | SRC-026 | 46,704 | 318 | UNCLEAR (MASTER-12 absent; large size drop from 11 — verify nature) |
| 9 | `NH_MASTER-14.md` | SRC-027 | 54,589 | 340 | HISTORICAL EXPLANATION ONLY |
| 9-cluster | `NH_MASTER-14__1_/__2_/__3_/__4_` | SRC-031/032/033/034 | 66,566 / 67,323 / 70,277 / 71,138 | 379/379/389/389 | UNCLEAR (14-variant ordering — settle by content) |
| 9-final | `NH_MASTER-14_FINAL` | SRC-028 | 94,146 | 427 | UNCLEAR (relation of FINAL to __N_ variants) |
| 9-final | `NH_MASTER-14_FINAL__2_` | SRC-029 | 101,638 | 434 | UNCLEAR |
| 9-final | `NH_MASTER-14_FINAL__4_` | SRC-030 | 102,115 | 434 | UNCLEAR |
| 10 | `NH_MASTER-17_*` (split set) | SRC-035/036/037/038 | 26,966 / 23,998 / 76,345 / 40,994 | 184/216/548/255 | UNCLEAR (4-file split: INDEX_STATUS, FOUNDATION_BUILT, CONCEPTUAL_ARCHITECTURE, ROADMAP — relationship to FULL_DRAFT must be settled; MASTER-15, 16 absent) |
| 10-full | `NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md` | SRC-039 | 165,109 | 1,148 | UNCLEAR (whether this supersedes the split set) |
| 11 | `NH_MASTER-18_FULL_DRAFT_v1.md` | SRC-040 | 206,696 | 1,464 | HISTORICAL EXPLANATION ONLY (predecessor to 19) |
| 12 | `NH_MASTER-19_CORRECTED_v1.md` | SRC-041 | 262,683 | 1,779 | HISTORICAL EXPLANATION ONLY — earlier lineage body; current authority is later (pending content audit) |
| 13 | `NH_MASTER-19_CORRECTED_v3.md` | SRC-042 | 283,033 | 1,910 | HISTORICAL EXPLANATION ONLY — earlier lineage body; current authority is later; v2/v4/v5 absent (pending content audit) |
| 14 | `NH_MASTER-19_CORRECTED_v6__1_.md` | SRC-043 | 283,081 | 1,908 | EXPLICITLY SUPERSEDED (declared predecessor in handoff) |
| 15 | `NH_MASTER-19_CORRECTED_v7_1.md` | SRC-044 | 291,811 | 1,937 | **CONFIRMED CURRENT** (adopted authoritative Master) |

### 2.2 The "FULL / standalone" Master family (off-spine — relationship UNCLEAR)

These carry the "Master" name but are not cleanly on the numbered spine. Their relationship to the
spine is a **feature-recovery question**, not settled here.

| File | SRC | Bytes | Lines | Note |
|---|---|---|---|---|
| `NH_MASTER-19_FULL.md` | SRC-045 | 245,244 | 1,706 | UNCLEAR — "FULL" standalone; smaller than CORRECTED_v1. v7_1's own title is "MASTER-19: Full Backup with All Additions," so the FULL ↔ CORRECTED relationship must be traced, not assumed. |
| `NH_MASTER_FILE_COMPLETE.md` | SRC-055 | 17,065 | 156 | UNCLEAR — early "complete file" snapshot; far smaller. |
| `NH_MASTER_FILE_COMPLETE__1_.md` | SRC-056 | 29,203 | 257 | UNCLEAR — variant of the above. |
| `NH_MASTER_CONTEXT.md` | SRC-054 | 22,765 | 323 | **CONFLICTING** — mandates the spelling "Nes / never Ness," which conflicts with the Masters and current preferences. Conflict preserved, not resolved. |
| `NH_MASTER_section13_ADD.md` | SRC-057 | 7,590 | 35 | HISTORICAL EXPLANATION ONLY — a §13 addendum fragment. |

---

## 3. DECISION-DEFAULTS LINEAGE

Same basis and same caution as §2. Provisional ordering for the comparison plan only.

| Step | File | SRC | Bytes | Lines | Lineage classification (file-level) |
|---|---|---|---|---|---|
| 1 | `NH_DECISION_DEFAULTS.md` | SRC-016 | 4,304 | 58 | HISTORICAL EXPLANATION ONLY (bare original) |
| 1b | `NH_DECISION_DEFAULTS__1_.md` | SRC-018 | 5,388 | 65 | UNCLEAR (no session token — order within the bare cluster unsettled) |
| 1c | `NH_DECISION_DEFAULTS__2_.md` | SRC-019 | 7,205 | 74 | UNCLEAR (bare cluster) |
| 1d | `NH_DECISION_DEFAULTS_ADD.md` | SRC-017 | 1,355 | 12 | HISTORICAL EXPLANATION ONLY (addendum fragment) |
| 2 | `NH_DECISION_DEFAULTS-S10_1.md` | SRC-007 | 10,874 | 88 | HISTORICAL EXPLANATION ONLY (also present as zip member `S10.1`, EXACT DUPLICATE) |
| 3 | `NH_DECISION_DEFAULTS-S12.md` | SRC-008 | 12,602 | 103 | HISTORICAL EXPLANATION ONLY |
| 4 | `NH_DECISION_DEFAULTS-S13.md` | SRC-009 | 18,133 | 121 | HISTORICAL EXPLANATION ONLY |
| 4b | `NH_DECISION_DEFAULTS-S13__1_.md` | SRC-010 | 19,065 | 123 | UNCLEAR (S13 variant; `__2_` is EXACT DUPLICATE of this) |
| 4c | `NH_DECISION_DEFAULTS-S13__3_.md` | SRC-011 | 22,527 | 124 | UNCLEAR (S13 variant ordering) |
| 4d | `NH_DECISION_DEFAULTS-S13__4_.md` | SRC-012 | 23,616 | 125 | UNCLEAR (S13 variant; `__6_` is EXACT DUPLICATE of this) |
| 5 | `NH_DECISION_DEFAULTS-S17_AUDITED_v1.md` | SRC-013 | 26,274 | 390 | **CONFLICTING** — filename says "AUDITED_v1" but the body is titled internally "(S17 — DRAFT)." Status mismatch preserved. (S17_DRAFT file itself absent.) |
| 6 | `NH_DECISION_DEFAULTS-S19_v1__1___1_.md` | SRC-014 | 33,328 | 298 | HISTORICAL EXPLANATION ONLY — earlier lineage body; current authority is later; v2_1 absent (pending content audit) |
| 7 | `NH_DECISION_DEFAULTS-S19_v2_2.md` | SRC-015 | 37,048 | 314 | **CONFIRMED CURRENT** (adopted authoritative Decision Defaults; upload copy `__1_` is EXACT DUPLICATE) |

Candidate `NH_DECISION_DEFAULTS-S19_v2_3.md` is **absent** — UNCLEAR, out of scope until supplied.

---

## 4. FILE-ROLE SEPARATION (every supplied source, sorted by role)

This separates all 92 unique source bodies into the role buckets Ness named. A file's bucket does not
classify its *features* — that is the later audit. Buckets are by document role only.

**This is a non-exclusive role map; a source may appear in a document-role category and again in
duplicate/provenance metadata** (e.g., `cursorrules__1_` appears as authority in §4.1 and again in the
EXACT DUPLICATE list in §4.11; the accepted SECURITY companion appears in §4.5 and its components are
mapped again in §6.8). The role map is therefore not an exclusive partition of SRC-001–092.

### 4.1 Authority (CONFIRMED CURRENT)
- `NH_MASTER-19_CORRECTED_v7_1.md` (SRC-044)
- `NH_DECISION_DEFAULTS-S19_v2_2.md` (SRC-015)
- `cursorrules__1_` / Cursor Rules v3.2 (SRC-076)
- `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` (SRC-087)

### 4.2 Direct predecessors
- **EXPLICITLY SUPERSEDED (explicit source statement):** `NH_MASTER-19_CORRECTED_v6__1_.md` (SRC-043)
  — the handoff explicitly identifies it as v7_1's predecessor.
- **Earlier lineage bodies; current authority is later (NOT asserted as explicitly superseded —
  pending content audit):** `NH_MASTER-19_CORRECTED_v3.md` (SRC-042);
  `NH_MASTER-19_CORRECTED_v1.md` (SRC-041); `NH_DECISION_DEFAULTS-S19_v1__1___1_.md` (SRC-014).
  Version-number progression alone is not treated as explicit supersession evidence.

**No historical file-level classification (HISTORICAL EXPLANATION ONLY, earlier-lineage-body, UNCLEAR,
or otherwise) prevents that file's features from being examined in the audit for possible loss,
weakening, conflict, or omission.**

### 4.3 Historical Master candidates (HISTORICAL EXPLANATION ONLY / UNCLEAR for off-spine)
- Spine: MASTER-5, 6, 6__1_, 7, 8, 9, 9_2, 9_4, 10, 10__1_, 11, 11_1, 13, 14 (+14 variants +14_FINAL
  variants), 17 split set, 17_FULL_DRAFT_CORRECTED_v2, 18_FULL_DRAFT_v1.
  (SRC-046/047/048/049/050/051/052/053/022/023/024/025/026/027/031/032/033/034/028/029/030/035/036/037/038/039/040)
- Off-spine: MASTER-19_FULL (SRC-045), MASTER_FILE_COMPLETE (SRC-055), MASTER_FILE_COMPLETE__1_
  (SRC-056), MASTER_CONTEXT (SRC-054 — CONFLICTING), MASTER_section13_ADD (SRC-057).

### 4.4 Historical Decision-Defaults candidates (HISTORICAL EXPLANATION ONLY / CONFLICTING noted)
- bare DD (SRC-016), __1_ (SRC-018), __2_ (SRC-019), _ADD (SRC-017), S10_1 (SRC-007), S12 (SRC-008),
  S13 (SRC-009), S13__1_ (SRC-010), S13__3_ (SRC-011), S13__4_ (SRC-012),
  S17_AUDITED_v1 (SRC-013 — CONFLICTING status label).

### 4.5 Accepted companions (ACCEPTED BUT NOT YET INTEGRATED — self-declared)
- `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM__1_.md` (SRC-001) — declares
  "ACCEPTED DESIGN — NOT YET BUILT" and "must be formally patched into the Master." Contains BOP,
  Other-Speaker/Guest architecture, SIA, SACL, Wellbeing/Identity/Security separation, BAI,
  Owner-Phone Pairing, Recovery-Code Lifecycle, Future-Phone Replacement, Atomic Emergency Recovery,
  Ness Voice-Profile Enrollment Bootstrap, Vocabulary Additions, BGMM.
- `NH_ACCEPTED_TSC_DESIGN_v1__1_.md` (SRC-002) — Temporary Session Cache.
  **Note (not a decision):** v7_1 already carries a §7E-TSC section; whether SRC-002 is fully,
  partly, or not integrated is a feature-recovery question for the audit.

### 4.6 Design specs / notes (provenance + recovery material)
- `NH_Universal_Filter_Design.md` (SRC-062), `__1_` (SRC-063), `__2_` (SRC-064),
  `NH_Universal_Filter_RULES.md` (SRC-065) — three-tier Universal Filter design family.
- `NH_Meaning_Engine_Design.md` Batch-5 body (SRC-058) — Batch-1 body unrecoverable (§1.4).
- `NH_Mobile_App_Design_Spec.md` (SRC-059); `NH_Canvas_Design_Spec.md` (SRC-006);
  `NH_chat_frontdoor_design_sketch.md` (SRC-067).
- `NH_wellbeing_baseline_system.md` (SRC-074); `NH_Build_Checklist.md` (SRC-003).
- `nh_research_architecture_explained.md` (SRC-085); `nh_search_pipeline_security_decisions.md`
  (SRC-086); `NH_risk_review_and_openrouter.md` (SRC-072) and `__1_` (SRC-073).
- `NH_INSIGHT__the_line_under_all_the_lines.md` (SRC-021);
  `NH_honest_calibration_note.md` (SRC-068); `NH_DELTA_S14.md` (SRC-020, a delta record);
  `NH_DECISION_DEFAULTS_ADD.md` (SRC-017).

### 4.7 Prototypes / interface artifacts (provenance only)
- `NH_live_mechanism.html` (SRC-069), `__1_` (SRC-070); `NH_live_mechanism_picture.svg` (SRC-071);
  `nh_2a_prototype.html` (SRC-078); `nh_architecture_canvas.html` (SRC-079);
  `nh_icon_combined.html` (SRC-080).

### 4.8 Code (provenance only — read-only evidence, not authority)
- `nh_ingest_chatgpt__1_.py` (SRC-081); `nh_log.py` (SRC-082); `nh_probe.py` (SRC-083);
  `nh_probe_truth.py` (SRC-084).

### 4.9 Handoffs / continuity (provenance only)
- `NH_CHAT_HANDOFF_AFTER_BGMM__1_.md` (SRC-004);
  `NH_SHARED_CHAT_HANDOFF_BEFORE_CONSOLIDATION_v1__1_.md` (SRC-061);
  `NH_RECENT_CONTINUITY_NOTE_POST_MASTER17-3.md` (SRC-060);
  `NH_CURSOR_BRIEF_reading_validator.md` (SRC-005).
- (The new-chat handoff `NH_NEW_CHAT_HANDOFF_AFTER_FULL_PROJECT_PRESERVATION_v1.md` itself is a
  handoff, declared non-authoritative.)

### 4.10 Provenance-only manifests and binaries
- Manifests v1–v5: `…AFTER_BATCH_9.md` (SRC-088), `_CORRECTED_v2/v3/v4/v5`
  (SRC-089/090/091/092). These establish provenance; they do NOT establish which features are
  canonical (handoff §"NO FEATURE RECOVERY").
- Binaries: survey PDF (SRC-075) with separately-marked extracted text; `files__3_.zip` (SRC-077).
  Exact bytes live only in the companion archive ZIP, not in the Markdown parts.

### 4.11 EXACT DUPLICATE filename records (19; bodies embedded once)
Per Preservation §6: SRC-007, 010, 012, 015, 017, 025, 026, 028, 029, 044, 052, 056, 066, 067, 071,
074, 075, 076, 085 each have ≥1 duplicate filename pointing to the same body. No duplicate filename
is dropped; none needs feature comparison (identical bytes).

---

## 5. PAIRWISE COMPARISON ORDER FOR THE LATER FEATURE-RECOVERY AUDIT

This is the *route* the later audit will walk. It is oldest → newest along each spine, with
variant-clusters resolved internally **before** the cluster is compared to the next spine node. Every
step traces add / weaken / drop / change — never "newer wins" (Rules 1–3). **EXACT DUPLICATE pairs are
skipped** (no content delta possible).

### 5.1 Master spine walk (primary)
Order of adjacent comparisons:

1. MASTER-5 → MASTER-6 *(then resolve 6 vs 6__1_ internally — UNCLEAR)*
2. MASTER-6(final) → MASTER-7
3. MASTER-7 → MASTER-8
4. MASTER-8 → MASTER-9 *(then resolve 9 / 9_2 / 9_4 internally — UNCLEAR; 9.1, 9.3 absent → gap note)*
5. MASTER-9(final) → MASTER-10 *(then resolve 10 vs 10__1_)*
6. MASTER-10(final) → MASTER-11 *(then resolve 11 vs 11_1 — note 11 > 11_1 in bytes)*
7. MASTER-11(final) → MASTER-13 *(MASTER-12 absent → gap note; large size drop → inspect)*
8. MASTER-13 → MASTER-14 *(then resolve the 14 cluster: 14, 14__1_..__4_, 14_FINAL, 14_FINAL__2_,
   14_FINAL__4_ — all UNCLEAR; settle the FINAL-vs-variant relationship by content)*
9. MASTER-14(final) → MASTER-17 split set *(MASTER-15, 16, 16_FINAL_CORRECTED absent → gap note;
   resolve the 4 split files into one MASTER-17 picture first)*
10. MASTER-17 split → MASTER-17_FULL_DRAFT_CORRECTED_v2 *(does FULL_DRAFT supersede the split?)*
11. MASTER-17_FULL_DRAFT_CORRECTED_v2 → MASTER-18_FULL_DRAFT_v1
12. MASTER-18_FULL_DRAFT_v1 → MASTER-19_CORRECTED_v1
13. MASTER-19_CORRECTED_v1 → v3 *(v2 absent → gap note)*
14. MASTER-19_CORRECTED_v3 → v6 *(v4, v5 absent → gap note)*
15. MASTER-19_CORRECTED_v6 → **v7_1 (CONFIRMED CURRENT — terminal node)**

### 5.2 Off-spine reconciliation passes (after the spine walk)
- A. `NH_MASTER-19_FULL` ↔ the CORRECTED_v1→v7_1 chain — determine whether FULL is an ancestor,
  sibling, or alternate consolidation. (No silent combining — Rule 6.)
- B. `NH_MASTER_FILE_COMPLETE` and `__1_` ↔ earliest spine nodes — place as early snapshots.
- C. `NH_MASTER_CONTEXT` (CONFLICTING "Nes") — surface, do not resolve; spelling is Ness's call.
- D. `NH_MASTER_section13_ADD` ↔ whichever Master's §13 it addends.

### 5.3 Decision-Defaults spine walk (parallel)
1. bare DD → __1_ → __2_ *(bare cluster ordering UNCLEAR — settle internally)*
2. bare-cluster(final) + _ADD → S10_1
3. S10_1 → S12 → S13 *(then resolve S13 / S13__1_ / S13__3_ / S13__4_ internally)*
4. S13(final) → S17_AUDITED_v1 *(CONFLICTING label; S17_DRAFT absent → gap note)*
5. S17_AUDITED_v1 → S19_v1 *(v2_1 absent → gap note)*
6. S19_v1 → **S19_v2_2 (CONFIRMED CURRENT — terminal node)**

### 5.4 Companion integration passes (after both spine walks)
- E. SECURITY_IDENTITY_AFTER_BGMM (SRC-001) feature-by-feature ↔ v7_1 — find what is, is partly, or
  is not present in the Master. Output: a per-component integration map. (No patching in the audit.)
- F. TSC (SRC-002) ↔ v7_1 §7E-TSC — find whether the accepted TSC equals, exceeds, or conflicts with
  the Master's TSC text.
- G. Design specs (Universal Filter ×3+RULES, Meaning Engine B5, Mobile, Canvas, chat-frontdoor,
  wellbeing baseline, research architecture, search-pipeline security) ↔ their Master sections — find
  full mechanisms the Master may only summarize (Rule 3).

---

## 6. PROVISIONAL STAGE-1 FEATURE-CATEGORY MAP (entire N.H architecture)

**This map covers all currently identified N.H architecture domains, but it is provisional and must be
completeness-checked during the full-body feature audit.** Stage 1 consulted v7_1 headings and selected
metadata (and the security companion's contents list) — **not every historical source body in full** —
so a domain present only inside an unread historical body could still be missing from this map. The
audit must confirm coverage, not assume it.

Every domain below carries the Master-declared build status transcribed verbatim from v7_1 headings
(transcription, not judgment), and where the primary current text and the companion/recovery evidence
live. **No feature is classified CURRENT/SUPERSEDED/etc. here** — that is the audit. The
"Master status (as written)" column simply repeats the tag already on the heading.

### 6.1 Foundations and frame
| # | Category | Primary text | Master status (as written) | Companion / recovery evidence |
|---|---|---|---|---|
| F1 | The Premise — Never Decide Facts | v7_1 §0 | DESIGNED (floor under every rule) | INSIGHT note (SRC-021) |
| F2 | Two Machineries — DUMB vs SMART | v7_1 §0A | DESIGNED (top-level frame) | — |
| F3 | What N.H Is | v7_1 §1 | (definitional) | MASTER_CONTEXT (SRC-054, CONFLICTING) |
| F4 | Input-Agnostic Principle (one engine, many front doors) | v7_1 §1A | DESIGNED | — |
| F5 | How to Work With Ness / Interaction + Artifact Delivery | v7_1 §2, §2A | LOCKED | — |
| F6 | Evolution — Old vs New | v7_1 §3 | (historical frame) | — |

### 6.2 Built substrate
| # | Category | Primary text | Master status (as written) | Companion / recovery evidence |
|---|---|---|---|---|
| B1 | The Machine | v7_1 §4 | (overview) | — |
| B2 | Codebase Map | v7_1 §5 | (overview) | runtime `.py` (SRC-081–084) |
| B3 | What's Built & Verified on Disk | v7_1 §6 | BUILT | manifests v1–v5 (SRC-088–092) |
| B4 | Code Rules — Cursor Rules v3.2 | v7_1 §6A + `cursorrules` (SRC-076) | IN FORCE | — |
| B5 | Accretive Store — schema + state | v7_1 §6B | BUILT & VERIFIED | `nh_log.py` (SRC-082) |

### 6.3 The big design — Universal Filter + Meaning Engine (v7_1 §7)
| # | Category | Primary text | Master status (as written) | Companion / recovery evidence |
|---|---|---|---|---|
| E1 | Universal Filter — operating rules | §7A | engine A BUILT | UF Design ×3 + RULES (SRC-062–065) |
| E2 | Meaning Engine — mechanism | §7B | engine B BUILT | Meaning Engine Design B5 (SRC-058) |
| E3 | Forced Build Order | §7C | (rule) | Build Checklist (SRC-003) |
| E4 | Living State Web | §7D | PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT | — |
| E5 | Catalog Front Door | §7E | CONCEPTUALLY DESIGNED, NOT BUILT | chat-frontdoor sketch (SRC-067) |
| E6 | Temporary Session Cache (TSC) | §7E-TSC | CONCEPTUALLY DESIGNED, NOT BUILT | **ACCEPTED TSC (SRC-002)** — integration TBD |
| E7 | Context Retrieval | §7F | CONCEPTUALLY DESIGNED, NOT BUILT | — |
| E8 | Meaning Engine Interior | §7G | CONCEPTUALLY DESIGNED, NOT BUILT | — |
| E9 | Reread Lifecycle | §7H | CONCEPTUALLY DESIGNED, NOT BUILT | — |
| E10 | View Layer | §7I | CONCEPTUALLY DESIGNED, NOT BUILT | — |
| E11 | Contradiction and Clash Handling | §7J | CONCEPTUALLY DESIGNED, NOT BUILT | — |
| E12 | Story Layer | §7K | CONCEPTUALLY DESIGNED, NOT BUILT | — |
| E13 | Person-Boxes | §7L | CONCEPTUALLY DESIGNED, NOT BUILT | — |
| E14 | Computed View | §7M | CONCEPTUALLY DESIGNED, NOT BUILT | — |
| E15 | Action Surfacing | §7N | CONCEPTUALLY DESIGNED, NOT BUILT | — |
| E16 | Action-Result Return Path | §7O | CONCEPTUALLY DESIGNED, NOT BUILT | — |
| E17 | Permission and Authority Boundaries | §7P | CONCEPTUALLY DESIGNED, NOT BUILT | — |
| E18 | Privacy, Deletion, Sensitive-Data Handling | §7Q | PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT | search-pipeline security (SRC-086) |
| E19 | Attention and Relevance Control (Decisions 1–14) | §7R | CORE CONCEPTUALLY DESIGNED, NOT BUILT | — |

### 6.4 Research / external
| # | Category | Primary text | Master status (as written) | Companion / recovery evidence |
|---|---|---|---|---|
| R1 | Research Pipeline (Brave) | v7_1 §8 | DESIGNED — Brave not wired | research architecture (SRC-085), risk_review/openrouter (SRC-072/073), survey PDF (SRC-075) |
| R2 | Image Ingest — first worked front door | v7_1 §9A | DESIGNED | — |
| R3 | Designed-Not-Built — the rest | v7_1 §9 | DESIGNED / CONCEPTUALLY DESIGNED | — |

### 6.5 Loops, model layer, front doors
| # | Category | Primary text | Master status (as written) | Companion / recovery evidence |
|---|---|---|---|---|
| L1 | The Live Loop | v7_1 §13 | DESIGNED — not built | live_mechanism html/svg (SRC-069/070/071), 2a prototype (SRC-078) |
| L2 | Chat Front Door | v7_1 §14 | DESIGN-IN-PROGRESS — not confirmed, not built | chat-frontdoor sketch (SRC-067) |
| L3 | Boot Hygiene + Sign-in + .cursorrules | v7_1 §15 | housekeeping done | — |
| L4 | Model Layer — Borrowed Mouth + Search Model | v7_1 §16 | DESIGNED + partly on disk | risk_review/openrouter (SRC-072/073) |
| L5 | Data-Rescue Operation / ingest | v7_1 §12 | recovery done; ingest FROZEN | `nh_ingest_chatgpt` (SRC-081), DELTA_S14 (SRC-020) |

### 6.6 Interface / world / companion surfaces
| # | Category | Primary text | Master status (as written) | Companion / recovery evidence |
|---|---|---|---|---|
| I1 | Interface, World, Interaction System (19A–19E) | v7_1 §19 | IN-PROGRESS DESIGN, NOT BUILT | architecture canvas (SRC-079), Canvas Design Spec (SRC-006), icon (SRC-080) |
| I2 | Mobile App — Three-Mode Companion | v7_1 §23 | DESIGNED — full spec restored S19, NOT BUILT | Mobile App Design Spec (SRC-059) |
| I3 | Connection Capability | v7_1 §24 | CONCEPTUALLY DESIGNED (S19), NOT BUILT | — |

### 6.7 Wellbeing
| # | Category | Primary text | Master status (as written) | Companion / recovery evidence |
|---|---|---|---|---|
| W1 | Wellbeing and Behavioral Baseline System | v7_1 §22 | DESIGNED — full spec restored S19, NOT BUILT | wellbeing baseline (SRC-074); separation rules also in SECURITY companion (SRC-001) |

### 6.8 Security / identity / access (companion-resident family — integration into Master is the open question)
These are primarily in the accepted SECURITY_IDENTITY companion (SRC-001), declared
ACCEPTED — NOT YET BUILT and not yet patched. Their presence/absence in v7_1 is the central
integration audit (pass E).
| # | Category | Primary text | Status (as written) |
|---|---|---|---|
| S1 | BOP — Behavioral Observation Processing | SRC-001 | ACCEPTED — NOT YET BUILT |
| S2 | Other-Speaker / Guest / Known-Person Architecture | SRC-001 | ACCEPTED — NOT YET BUILT |
| S3 | SIA — Speaker Identity Assessment | SRC-001 | ACCEPTED — NOT YET BUILT |
| S4 | SACL — Speaker Access-Control Layer | SRC-001 | ACCEPTED — NOT YET BUILT |
| S5 | Wellbeing/Identity/Security Separation Rules | SRC-001 | ACCEPTED — NOT YET BUILT |
| S6 | BAI — Biometric Authorization Interface | SRC-001 | ACCEPTED — NOT YET BUILT |
| S7 | Initial Owner-Phone Pairing | SRC-001 | ACCEPTED — NOT YET BUILT |
| S8 | Recovery-Code Lifecycle | SRC-001 | ACCEPTED — NOT YET BUILT |
| S9 | Future-Phone Replacement Flow | SRC-001 | ACCEPTED — NOT YET BUILT |
| S10 | Atomic Emergency Recovery Flow | SRC-001 | ACCEPTED — NOT YET BUILT |
| S11 | Ness Voice-Profile Enrollment Bootstrap | SRC-001 | ACCEPTED — NOT YET BUILT |
| S12 | Formally Adopted Vocabulary Additions | SRC-001 | ACCEPTED — NOT YET BUILT |
| S13 | BGMM — Biometric-Gated Maintenance Mode | SRC-001 | ACCEPTED — NOT YET BUILT |

### 6.9 Governance, status, and change-logs (record domains)
| # | Category | Primary text | Note |
|---|---|---|---|
| G1 | Originality / honest calibration | v7_1 §10 | calibration note (SRC-068) |
| G2 | What's Open / Next + Settled | v7_1 §11, §11-SETTLED | — |
| G3 | Correction/consolidation logs (S16, S17, S18, S19, current) | v7_1 §17, §18, §20, §21, §25 | continuity note (SRC-060), handoffs (SRC-004/061) |
| G4 | Project governance / accepted-designs / archive | governance companion (SRC-087) | CONFIRMED CURRENT companion |
| G5 | Working roles | governance companion + `NH_WORKING_ROLES.md` (SRC-066) | — |

---

## 7. CLASSIFICATION LEGEND USED IN THIS FILE

- **CONFIRMED CURRENT** — adopted authority, established by Preservation §2 and the handoff.
- **ACCEPTED BUT NOT YET INTEGRATED** — companion self-declares acceptance and "not yet patched."
- **EXPLICITLY SUPERSEDED** — reserved for cases supported by an **explicit source statement**, not by
  version-number progression alone. The only file-level use in this document is
  `NH_MASTER-19_CORRECTED_v6` → v7_1, which the handoff states explicitly.
- **EXPLICITLY REJECTED** — *(none asserted at file level in Stage 1; reserved for the audit.)*
- **HISTORICAL EXPLANATION ONLY** — a predecessor/fragment kept for provenance, not current. Earlier
  numbered lineage bodies whose current authority is a later version sit here pending the content audit
  (they are not labeled EXPLICITLY SUPERSEDED).
- **EXACT DUPLICATE** — identical bytes to another record (Preservation §6).
- **POSSIBLY DROPPED** — *(reserved for the feature audit; not asserted here. Absent files are
  "absent," not "dropped" — Rule 2.)*
- **CONFLICTING** — two records disagree (e.g., "Nes" vs "Ness"; AUDITED_v1 vs internal "DRAFT").
- **UNCLEAR** — ordering or relationship not settled by filename/size; settle by content in the audit.
- **UNRECOVERABLE HISTORICAL SOURCE BODY — CONTENT CLASSIFICATION UNCLEAR** — bytes unavailable, so
  content and design role cannot be inferred (the Batch-1 Meaning Engine body).

**No historical file-level classification prevents a file's features from being examined in the audit
for possible loss, weakening, conflict, or omission.**

Note: **CONFIRMED CURRENT, ACCEPTED, SUPERSEDED, HISTORICAL, EXACT DUPLICATE, CONFLICTING, and
UNCLEAR** are the only labels applied in Stage 1, and only at the file/lineage level.
**EXPLICITLY REJECTED and POSSIBLY DROPPED are deliberately not asserted yet** — both require the
feature-by-feature audit and Ness's reading, not lineage inference.

---

## 8. VERIFICATION REPORT — SOURCE RANGES ACTUALLY CONSULTED

This records exactly what was read to produce Stage 1, so nothing here rests on memory or summary.

| Source | What was consulted | Method |
|---|---|---|
| `/mnt/project/` directory | Full listing of all 17 supplied files + sizes | `view` (directory) |
| `NH_NEW_CHAT_HANDOFF_AFTER_FULL_PROJECT_PRESERVATION_v1.md` | Entire file (lines 1–83) | `view` |
| `NH_COMPLETE_PROJECT_PRESERVATION_MASTER_v1_INDEX.md` | Entire file (lines 1–143): part metadata + full source-record map | `view` |
| `…PART_01.md` (control sections) | Lines 1–320 and 320–420: §1 purpose/limits, §2 authority, §3 candidates, §4 full source index, §5 occurrence table, §6 duplicate index, §7 missing files, §8 unrecoverable body, §9 unresolved conflicts, §10 order-implies-nothing, plus head of SRC-001 (security companion contents + status label) | `view` |
| `…PART_01.md` (index byte/line rows) | Lines 62–175 and 195–271: exact bytes/lines/SHA for every SRC | `view` |
| `NH_MASTER-19_CORRECTED_v7_1.md` | All §-level and most ###-level headings (§0 through §25) for the feature-category map | `grep` headings |
| `NH_DECISION_DEFAULTS-S19_v2_2.md` | First lines (title + sync line confirming it is synced to v7_1, June 28 2026) | `head` |
| `cursorrules__1_` | First lines (title "Cursor Rules v3.2" + v3.0 rewrite provenance) | `head` |
| `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | First lines (title + version) | `head` |
| All 4 authority files | Full-file SHA-256 | `sha256sum` |
| All 11 reader parts | Full-file SHA-256 | `sha256sum` |

### 8.1 Integrity results
- 4/4 authority-file hashes match the Preservation §2 record. ✓
- 11/11 reader-part hashes match the reader-index record. ✓
- DD v2_2 internally declares it is synced to v7_1 (consistent with adopted-authority claim). ✓

### 8.2 NOT consulted in Stage 1 (deliberately — out of scope for lineage planning)
- The **full embedded bodies** of the historical Masters / Decision Defaults / specs (only headings,
  metadata, and the security-companion's contents list were read). Reading those bodies in full is the
  **feature-recovery audit (Stage 2+)**, not Stage 1.
- The byte-level archive ZIP and the two binaries (PDF/ZIP) — not supplied as files here; their
  metadata was read from the index only.
- The fresh end-to-end reconstruction (concatenate Parts 01–11 → compare to full Preservation
  SHA `6f458f8b…`): relied on the index's prior independent verification; per-part hash integrity was
  re-checked instead. Flagged in §1.3 so it is not mistaken for a fresh reconstruction.

---

## 9. STATE AFTER STAGE 1 (nothing adopted, nothing changed)

- Authority unchanged: v7_1 / DD S19_v2_2 / Cursor Rules v3.2 / governance companion v1.
- No candidate adopted. No conflict resolved. No feature compared. No patch proposed.
- The lineages, role-separation, comparison order, and feature-category map above are the **plan** for
  the later feature-recovery audit.
- Next stage (only on Ness's instruction): begin the feature-recovery audit by walking §5, starting
  with the pass Ness chooses.

**STAGE 1 COMPLETE. AWAITING NESS.**

---

## 10. CORRECTION LEDGER (v1 → v1.1)

Each row is a planning/classification correction only. No architecture, source content, comparison
evidence, hash, byte count, line count, or settled N.H decision was changed.

| # | Where | v1 said (old) | v1.1 says (replacement) |
|---|---|---|---|
| 1 | §1 / §8 | "all 16 supplied files" | "17 files: 4 authority + 1 handoff + 1 reader index + 11 reader parts" (4+1+1+11=17) |
| 2 | §1.1 | Four files listed by role label only (implied interchangeable) | Each scoped: Master = architectural authority; Decision Defaults = behavioral/defaults authority; Cursor Rules v3.2 = operational coding authority; governance companion = governance/accepted-design/provenance authority within its declared scope, **explicitly NOT an independent architectural authority** |
| 3a | §2.1 | `MASTER-19_CORRECTED_v1` = "EXPLICITLY SUPERSEDED (by later v-tokens)" | "HISTORICAL EXPLANATION ONLY — earlier lineage body; current authority is later (pending content audit)" |
| 3b | §2.1 | `MASTER-19_CORRECTED_v3` = "EXPLICITLY SUPERSEDED (v2/v4/v5 absent)" | "HISTORICAL EXPLANATION ONLY — earlier lineage body; current authority is later; v2/v4/v5 absent (pending content audit)" |
| 3c | §3 | `DD S19_v1` = "EXPLICITLY SUPERSEDED (by v2_2; v2_1 absent)" | "HISTORICAL EXPLANATION ONLY — earlier lineage body; current authority is later; v2_1 absent (pending content audit)" |
| 3d | §4.2 / §7 | Predecessors bucket titled "(EXPLICITLY SUPERSEDED)" grouping v6, v3, v1, DD-v1 together | Split: only `v6` is EXPLICITLY SUPERSEDED (explicit handoff statement); v3, v1, DD-v1 are "earlier lineage bodies; current authority is later." Legend now reserves EXPLICITLY SUPERSEDED for explicit-source-statement cases. Added: no historical classification prevents feature examination |
| 4 | §1.4 / §7 | Batch-1 `NH_Meaning_Engine_Design.md` body = "HISTORICAL EXPLANATION ONLY and cannot be examined" | "UNRECOVERABLE HISTORICAL SOURCE BODY — CONTENT CLASSIFICATION UNCLEAR" (bytes unavailable; content/role cannot be inferred) |
| 5 | §6 (+ intro) | "COMPLETE FEATURE-CATEGORY MAP"; intro "a complete feature-category map" | "PROVISIONAL STAGE-1 FEATURE-CATEGORY MAP"; states it covers all currently identified domains but must be completeness-checked in the full-body audit, since Stage 1 read headings/selected metadata, not every historical body in full |
| 6 | §4 intro | Buckets presented without exclusivity statement | Added: "This is a non-exclusive role map; a source may appear in a document-role category and again in duplicate/provenance metadata" (with examples) |
| 7 | §1.3 | Final reader-part range "39879–42177"; no stated convention | Stated convention: inclusive, zero-based `[start, end]`, contiguous; final range corrected to "39879–42176" (file is 42,177 lines; last zero-based index is 42176). Index's "42177" noted as a one-based count. No file/hash/byte/line-count/content altered |
| 8 | §1.3 / §8.2 | "Stage 1 did not re-run the full concatenation reconstruction" | **Unchanged — preserved verbatim.** v1.1 does not claim the reconstruction was performed |

**STAGE 1 v1.1 COMPLETE. AWAITING NESS.**
