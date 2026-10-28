# N.H — BASELINE SOURCE MANIFEST (AFTER BATCH 9)

**Status: PERMANENT PROVENANCE RECORD — NOT a consolidation, NOT an audit.**
This manifest catalogs every physically supplied source file across upload Batches 1–9 of the restarted N.H baseline source inventory. It records provenance only. No cross-file comparison, feature-recovery audit, restoration, reconciliation, rewriting, or consolidation has been performed or begun.

Generated after the explicit declaration: *"FINAL BATCH — ALL CURRENTLY LOCATED SOURCE FILES HAVE NOW BEEN SUPPLIED."* Batch 9 was the final upload batch.

---

## 0. STANDING RULES GOVERNING THIS MANIFEST

These rules are in force and must not be violated by any later step:

1. **Newer does not automatically mean more complete.** A later-numbered Master, a larger file, a file labeled "FINAL," or the adopted-authoritative file is NOT assumed to contain more or better design than an earlier one. Completeness is established only by direct comparison, which has NOT yet been done.
2. **Duplicates must never disappear from provenance.** Every physically supplied file — including exact duplicates, renamed copies, copy-suffix (`__1_`, `__2_`…) files, repeated uploads across batches, reader copies, backups, and ZIP members — keeps its own provenance entry. Identical-content files are linked into groups sharing one SHA-256, but no filename or upload occurrence is ever deleted, omitted, replaced, or collapsed.
3. **Older Masters may preserve important original features.** Material present in an early Master and absent from a later one is treated as possibly-dropped design to be recovered later — never as obsolete merely because it is older.
4. **No design decision may be silently resolved.** Where sources conflict or a question is open, it is recorded as a conflict/open item and preserved. Claude does not choose a winner, settle a fork, or adopt a file on Ness's behalf.
5. **No consolidation has begun.** This is an inventory. The permanent source manifest is a catalog, not a merged Master. Generating it does not start the audit/restoration/consolidation phase.

---

## 1. FINAL CUMULATIVE COUNTS

| Metric | Count |
|---|---|
| **Physical upload occurrences (Batches 1–9, every filename+batch event, repeats included)** | **133** |
| Per batch | B1: 15 · B2: 7 · B3: 11 · B4: 13 · B5: 17 · B6: 16 · B7: 18 · B8: 18 · B9: 18 |
| **Distinct filenames currently resident on disk** | **100** |
| **Unique content hashes (distinct file bodies, incl. ZIP container)** | **86** |
| — of which: distinct loose/document bodies | 85 |
| — plus: the ZIP container `files__3_.zip` as its own artifact | 1 |
| **Unreadable files** | **0** |

**Note on the two count framings (both true, both kept):**
- **133** counts every upload *occurrence* across batches — the provenance-faithful number (the duplicate-handling rule requires every occurrence be retained).
- **100 filenames / 86 hashes** describe what is *currently resident* on the deduplicated filesystem (same-name re-uploads across batches overwrote to one physical copy, but each occurrence remains recorded in the batch receipts above this manifest).
- Of the 86 unique hashes: 14 hashes are currently resident under **two different filenames each** (28 files), and 72 hashes under one filename each (72 files) → 86 unique among 100 resident filenames. Two of those hashes (`7270cc48…` MASTER-11.1, `b018ae48…` DD-S10.1) are ALSO present as members inside `files__3_.zip`, byte-identical to their loose copies.

---

## 2. COMPLETE FILE CATALOG (every supplied file)

Listed by category. Each entry: filename · batches supplied in · SHA-256 (first 12 + last 4) · bytes · lines · readability · description · declared status. Full 64-char hashes are in §3 (duplicate groups) and the per-batch receipts.

### 2A. AUTHORITATIVE / ADOPTED FILES (also in Project Knowledge)

| Filename | Batch(es) | SHA-256 | Bytes | Lines | Description / declared status |
|---|---|---|---|---|---|
| `NH_MASTER-19_CORRECTED_v7_1__1_.md` | B3 (≡ Project `NH_MASTER-19_CORRECTED_v7_1.md`) | `0e8b59e3ce8f…65cf` | 291,811 | 1,937 | The adopted authoritative Master. Largest, latest in the 19-lineage. NOT assumed most-complete until diffed. |
| `NH_DECISION_DEFAULTS-S19_v2_2__1_.md` | B3 (≡ Project `…S19_v2_2.md`) | `6cd09329e12b…e696` | 37,048 | 314 | The authoritative companion Decision Defaults. |
| `cursorrules__1_` | B3 (≡ Project) | `5050d08825b9…96e9` | 34,821 | 717 | In-force code ruleset (`.cursorrules`). |

### 2B. MASTER FILES — full lineage (chronology in §6)

| Filename | Batch(es) | SHA-256 | Bytes | Lines | Notes |
|---|---|---|---|---|---|
| `NH_MASTER-5.md` | B5 | `f91fdf682bac…692c` | 32,737 | 223 | Earliest numbered Master. Names §3D security fixes BUILT. Lower bound named in v3 header for "§8 rules dropped 5→17, restored S19." |
| `NH_MASTER-6.md` | B5 | `63a64d0895e5…48cc` | 45,407 | 273 | Master-6 (shorter of two). |
| `NH_MASTER-6__1_.md` | B5 | `3e978e036871…7633` | 54,506 | 315 | Master-6 (longer). Related version of above. |
| `NH_MASTER-7.md` | B5 | `6868507ca073…35c4` | 60,439 | 332 | |
| `NH_MASTER-8.md` | B5 | `13675a34e039…e48a` | 80,833 | 423 | |
| `NH_MASTER-9.md` | B5 | `e6bf27a4d4c8…a813` | 89,479 | 442 | |
| `NH_MASTER-9_2.md` | B5 | `052731353b4a…107e` | 127,717 | 513 | Master-9 "9_2" revision. |
| `NH_MASTER-9_2__1_.md` | B5, B6 | `052731353b4a…107e` | 127,717 | 513 | Exact dup of `NH_MASTER-9_2.md`. |
| `NH_MASTER-9_4.md` | B6 | `9bbc28dc31c7…e8dd` | 149,631 | 580 | MASTER-9.4: adds §13 live loop + §14 chat front-door sketch. Header: nothing on disk changed (store 11,374/4 groups). |
| `NH_MASTER-10.md` | B6 | `4ee57d298f11…b7d8` | 74,496 | 406 | MASTER-10 (session 9): adds §0 PREMISE; reality/sim reworked in design. |
| `NH_MASTER-10__1_.md` | B6 | `f9e783601b18…b804` | 75,898 | 407 | Near-dup of MASTER-10 (~1.4 KB larger, same header). |
| `NH_MASTER-11.md` | B6 | `10771ea4e9cb…e3ba` | 91,643 | 443 | MASTER-11 (session 10): "reality-layer" REPLACED by "per-person STORY-layer." Load-bearing re-souling. |
| `NH_MASTER-11_1.md` | B7 (loose + in `files__3_.zip`) | `7270cc48fd9a…448c` | 80,040 | 482 | MASTER-11.1 (session 10 evening): 2a reading-record shape; six-part STORY-layer; DUMB/SMART frame (§0A). |
| `NH_MASTER-13.md` | B7 | `e2c0f9152349…c2ae` | 46,704 | 318 | MASTER-13: model layer, person-boxes, tape, DUMB/SMART frame. (MASTER-12 not supplied.) |
| `NH_MASTER-13__1_.md` | B7, B8 | `e2c0f9152349…c2ae` | 46,704 | 318 | Exact dup of `NH_MASTER-13.md`. |
| `NH_MASTER-14.md` | B7, B8, B9 | `493f50b8f855…0be4` | 54,589 | 340 | MASTER-14 family — smallest body. |
| `NH_MASTER-14__1_.md` | B7, B8, B9 | `9a3f2b1eaa63…0766` | 66,566 | 379 | |
| `NH_MASTER-14__2_.md` | B7, B8, B9 | `f9dd9d957d45…fbb3` | 67,323 | 379 | Near-dup of __1_ (same lines, +760 B). |
| `NH_MASTER-14__3_.md` | B7, B8, B9 | `1dec9fe0cc4f…7fd6` | 70,277 | 389 | |
| `NH_MASTER-14__4_.md` | B7, B8, B9 | `ea4bcbdde17c…b5ee` | 71,138 | 389 | Near-dup of __3_ (same lines, +860 B). |
| `NH_MASTER-14_FINAL.md` | B7, B8, B9 | `6dc26159e186…f5c3` | 94,146 | 427 | FINAL base. "FINAL" tag NOT assumed most-complete. |
| `NH_MASTER-14_FINAL__1_.md` | B8, B9 | `6dc26159e186…f5c3` | 94,146 | 427 | Exact dup of FINAL base. |
| `NH_MASTER-14_FINAL__2_.md` | B8, B9 | `55fab7e730cb…d720` | 101,638 | 434 | Larger FINAL (434 lines). |
| `NH_MASTER-14_FINAL__3_.md` | B8, B9 | `55fab7e730cb…d720` | 101,638 | 434 | Exact dup of FINAL__2_. |
| `NH_MASTER-14_FINAL__4_.md` | B8, B9 | `f632babe5364…a11a` | 102,115 | 434 | Near-dup of FINAL__2_/__3_ (+480 B). |
| `NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md` | B1, B2, B3 | `cfdaefe9b0b6…e152` | 165,109 | 1,148 | MASTER-17 full draft (corrected v2). Source of the four reader slices below. |
| `NH_MASTER-17_00_INDEX_STATUS.md` | B1 | `b7c794561d10…96c9` | 26,966 | 184 | Derived reader copy (do-not-edit) of MASTER-17. |
| `NH_MASTER-17_01_FOUNDATION_BUILT.md` | B1 | `da261935d739…a008` | 23,998 | 216 | Derived reader copy of MASTER-17. |
| `NH_MASTER-17_02_CONCEPTUAL_ARCHITECTURE.md` | B1 | `186717c1ba60…d341` | 76,345 | 548 | Derived reader copy of MASTER-17. |
| `NH_MASTER-17_03_ROADMAP_INTERFACE_HISTORY.md` | B1 | `0a64a524d732…d5a9` | 40,994 | 255 | Derived reader copy of MASTER-17. |
| `NH_MASTER-18_FULL_DRAFT_v1.md` | B2 | `2f63734c600f…5397` | 206,696 | 1,464 | MASTER-18 full draft. |
| `NH_MASTER-19_FULL.md` | B2 | `bc498fda2fea…caec` | 245,244 | 1,706 | MASTER-19 full. Hardware row still RTX 5060 Ti (pre-3090). |
| `NH_MASTER-19_CORRECTED_v1.md` | B2 | `0287015be938…effb` | 262,683 | 1,779 | MASTER-19 corrected v1. |
| `NH_MASTER-19_CORRECTED_v3.md` | B1 | `e38c37e97491…a7be`* | 283,033 | 1,910 | MASTER-19 corrected v3. (*hash full: `e38c37e9…127a7b`) |
| `NH_MASTER-19_CORRECTED_v6__1_.md` | B3 | `8165f4bed94d…1bf9` | 283,081 | 1,908 | MASTER-19 v6 — predecessor of v7_1; matches AFTER_BGMM handoff. |
| `NH_MASTER-19_CORRECTED_v7_1__1_.md` | B3 | `0e8b59e3ce8f…65cf` | 291,811 | 1,937 | **ADOPTED AUTHORITATIVE** (see §2A). |

### 2C. "MASTER_FILE_COMPLETE" parallel family

| Filename | Batch(es) | SHA-256 | Bytes | Lines | Notes |
|---|---|---|---|---|---|
| `NH_MASTER_FILE_COMPLETE.md` | B4 | `80a6143e9857…cd02` | 17,065 | 156 | Bare "COMPLETE" master (156 lines). "Supersedes…" |
| `NH_MASTER_FILE_COMPLETE__1_.md` | B4 | `06f69672fa89…daed` | 29,203 | 257 | Standalone COMPLETE master (257 lines). |
| `NH_MASTER_FILE_COMPLETE__2_.md` | B5 | `06f69672fa89…daed` | 29,203 | 257 | Exact dup of `__1_`. |

### 2D. DECISION DEFAULTS — full lineage (chronology in §6)

| Filename | Batch(es) | SHA-256 | Bytes | Lines | Notes |
|---|---|---|---|---|---|
| `NH_DECISION_DEFAULTS.md` | B5 | `2abb2e4570f7…b047` | 4,304 | 58 | Earliest bare Decision Defaults (no DESIGN COMPASS). |
| `NH_DECISION_DEFAULTS__1_.md` | B5, B6 | `45ec88c44045…3e29` | 5,388 | 65 | Adds DESIGN COMPASS block. |
| `NH_DECISION_DEFAULTS__2_.md` | B6 | `11f71f447c17…4bdc` | 7,205 | 74 | Session-9 generation: §0 premise, per-person STORY reading, carry-the-speaker, open-forks list. |
| `NH_DECISION_DEFAULTS_ADD.md` | B5, B6 | `32b1172159b6…2bab` | 1,355 | 12 | Standalone DESIGN COMPASS add-on fragment. |
| `NH_DECISION_DEFAULTS_ADD__1_.md` | B5, B6 | `32b1172159b6…2bab` | 1,355 | 12 | Exact dup of `_ADD`. |
| `NH_DECISION_DEFAULTS-S10_1.md` | B7 (loose + in `files__3_.zip`) | `b018ae48f886…968c` | 10,874 | 88 | S10.1: matches MASTER-11.1; 2a two-file structure; Helper-not-Decider. |
| `NH_DECISION_DEFAULTS-S12.md` | B7, B8, B9 | `da329e8652ba…cfa8` | 12,602 | 103 | S12: store BUILT & clean (5,521 roots, 7-field w/ `role`); disk-verify-[BUILT]-claims lesson. |
| `NH_DECISION_DEFAULTS-S13.md` | B7, B8, B9 | `eaea2e2ccb31…644a` | 18,133 | 121 | S13 family — smallest. |
| `NH_DECISION_DEFAULTS-S13__1_.md` | B7, B8, B9 | `0ff6dd4ce29b…e2f0` | 19,065 | 123 | |
| `NH_DECISION_DEFAULTS-S13__2_.md` | B7, B8, B9 | `0ff6dd4ce29b…e2f0` | 19,065 | 123 | Exact dup of S13__1_. |
| `NH_DECISION_DEFAULTS-S13__3_.md` | B7, B8, B9 | `f6358c44db6e…d4f1` | 22,527 | 124 | |
| `NH_DECISION_DEFAULTS-S13__4_.md` | B8, B9 | `8acc713871d9…f86d` | 23,616 | 125 | Largest S13 variant. |
| `NH_DECISION_DEFAULTS-S13__6_.md` | B8, B9 | `8acc713871d9…f86d` | 23,616 | 125 | Exact dup of S13__4_. (Suffix `__5_` never supplied.) |
| `NH_DECISION_DEFAULTS-S17_AUDITED_v1.md` | B2 | `a0df064a0f4d…f69e` | 26,274 | 390 | Titled DRAFT / derived-not-authority. |
| `NH_DECISION_DEFAULTS-S19_v1__1___1_.md` | B3 | `ecea9224163681…aaa6` | 33,328 | 298 | S19_v1 — synced to Master v6. |
| `NH_DECISION_DEFAULTS-S19_v2_2__1_.md` | B3 | `6cd09329e12b…e696` | 37,048 | 314 | **AUTHORITATIVE** (see §2A). |

### 2E. CORE DESIGN / RULES / MEANING-ENGINE DOCUMENTS

| Filename | Batch(es) | SHA-256 | Bytes | Lines | Notes |
|---|---|---|---|---|---|
| `NH_Universal_Filter_RULES.md` | B5 | `c0fb4528a332…3a37` | 11,828 | 178 | 12-rule operating ruleset. Rule 6 (memory only adds), Rule 7 (the membrane), Rule 11 (steerer-not-clerk). |
| `NH_Universal_Filter_Design.md` | B4 | `3df666eb4ff4…1020` | 5,740 | 88 | Bare UF design — no Keystone, no Membrane. |
| `NH_Universal_Filter_Design__1_.md` | B1, B4 | `7dce7058c991…b1c7` | 10,321 | 131 | UF design + Keystone. |
| `NH_Universal_Filter_Design__2_.md` | B4 | `c8938d370efd…be15` | 13,755 | 155 | UF design + Keystone + MEMBRANE (Membrane section exists ONLY here among the design copies). |
| `NH_Meaning_Engine_Design.md` | B1, B5 | B1:`18185908…0d62` / B5:`15c2786003…9a89` | B5: 12,479 | B5: 138 | Meaning-engine mechanism (8 parts). B1 vs B5 differ by separator formatting only (near-dup). |
| `NH_MASTER_section13_ADD.md` | B5, B6 | `91d82ed52bcb…68b9` | 7,590 | 35 | §13 live-loop add-on (fire-and-let-go). |
| `NH_chat_frontdoor_design_sketch.md` | B1, B6 | `757b6dd889ae…0112` | 13,532 | 105 | §14 chat front-door working sketch (explicitly unconfirmed). |
| `NH_chat_frontdoor_design_sketch__1_.md` | B6 | `757b6dd889ae…0112` | 13,532 | 105 | Exact dup of chat_frontdoor sketch. |
| `NH_INSIGHT__the_line_under_all_the_lines.md` | B6 | `77b5932819a6…8ab1` | 2,224 | 37 | Standalone compass insight ("not-deciding is safe"). |
| `NH_DELTA_S14.md` | B9 | `f94b5351e562…af9f` | 9,612 | 88 | Session-14 delta: closes confidence/gold-scoring/failure-behavior forks. Decisions only, nothing built. |
| `NH_CURSOR_BRIEF_reading_validator.md` | B9 | `d80065191b04…0ba9` | 9,455 | 86 | Build spec: 12-field reading contract + reading-shaped writer. Spec only, not approved code. |
| `NH_Build_Checklist.md` | B5 | `e4d1436a3e56…ea40` | 4,325 | 95 | V/X built-vs-unbuilt snapshot (June 20 2026). |

### 2F. SECURITY / IDENTITY / HANDOFF / GOVERNANCE DOCUMENTS

| Filename | Batch(es) | SHA-256 | Bytes | Lines | Notes |
|---|---|---|---|---|---|
| `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM__1_.md` | B3 | `fb36bf8e5502…16f5` | 71,936 | 1,724 | Companion record, declared NOT authoritative; "not yet patched into Master v6." |
| `NH_ACCEPTED_TSC_DESIGN_v1__1_.md` | B3 | `1da2e296d434…4658` | 43,237 | 956 | Companion record (Temporary Session Cache), declared NOT authoritative. |
| `NH_CHAT_HANDOFF_AFTER_BGMM__1_.md` | B3 | `f524f7cdd4dd…a562` | 8,081 | 171 | Handoff: authority order Master v6→DD v1→roles; 13 accepted security/identity/BGMM components. |
| `NH_SHARED_CHAT_HANDOFF_BEFORE_CONSOLIDATION_v1__1_.md` | B3 | `47e6a8ba71fa…d865` | 6,590 | 185 | Names authoritative pair + hashes. |
| `NH_RECENT_CONTINUITY_NOTE_POST_MASTER17-3.md` | B2 | `7d614546710c…82e3` | 8,861 | 239 | Continuity note post-MASTER17. |
| `NH_WORKING_ROLES.md` | B2 | `a0281060abd7…7619` | 3,015 | 49 | Role division (Ness/Claude/Cursor). |
| `NH_WORKING_ROLES__2_.md` | B3 | `a0281060abd7…7619` | 3,015 | 49 | Exact dup of WORKING_ROLES. |
| `NH_MASTER_CONTEXT.md` | B1 | `e6ae68b37a37…f099` | 22,765 | 323 | Old context file. Mandates "Nes" spelling (conflicts with corrected "Ness"). |
| `nh_search_pipeline_security_decisions.md` | B1, B4 | `0550cea1aaca…b82a` | 4,506 | 38 | Search-pipeline security decisions. |
| `nh_research_architecture_explained.md` | B4 | `d19a3c220914…8a06` | 10,089 | 176 | Research architecture explainer. |
| `nh_research_architecture_explained__1_.md` | B4 | `d19a3c220914…8a06` | 10,089 | 176 | Exact dup. |
| `NH_risk_review_and_openrouter.md` | B4 | `3864a2eb1a8f…d598` | 5,245 | 63 | Risk review (bare). |
| `NH_risk_review_and_openrouter__1_.md` | B4 | `6fa53662b406…10c7` | 8,384 | 85 | Risk review + boot-error/silent-auto-start resolution (related version). |
| `NH_honest_calibration_note.md` | B1 | `4096cc357b1e…f6ac` | 5,346 | 48 | Honest-calibration note. |

### 2G. SPEC / PRODUCT / WELLBEING DOCUMENTS

| Filename | Batch(es) | SHA-256 | Bytes | Lines | Notes |
|---|---|---|---|---|---|
| `NH_Mobile_App_Design_Spec.md` | B1 | `023c82babd42…812c` | 5,438 | 82 | Mobile app design spec. |
| `NH_Canvas_Design_Spec.md` | B4 | `20444814d0ac…d5b5` | 4,995 | 78 | Canvas design spec. |
| `NH_wellbeing_baseline_system.md` | B1, B4 | `afb1bad3c1ed…c098c` | 7,926 | 140 | Behavioral-baseline wellbeing engine design. |
| `NH_wellbeing_baseline_system__1_.md` | B3 | `afb1bad3c1ed…c098c` | 7,926 | 140 | Exact dup of wellbeing. |
| `N_H…REALITY_SIMULATION_Gate_Surveyed_Against_the_Field.pdf` | B4 | `ba98f5c9e2f0…f19a` | 470,408 | 9,992 | 8-page field-survey PDF: N.H combination genuinely novel vs the field. |
| `N_H…Surveyed_Against_the_Field__1_.pdf` | B4 | `ba98f5c9e2f0…f19a` | 470,408 | 9,992 | Exact dup of the PDF. |

### 2H. CODE / PROTOTYPES / HTML / SVG / ARCHIVE

| Filename | Batch(es) | SHA-256 | Bytes | Lines | Notes |
|---|---|---|---|---|---|
| `nh_log.py` | B6 | `63eaf052295b…8d5e` | 17,941 | 481 | Read-only HTML log/"mirror" generator (§7B Part 7). |
| `nh_probe.py` | B6 | `2dc08d4e8968…ec3f` | 7,234 | 188 | Read-only boundary-signal probe over the store. |
| `nh_probe_truth.py` | B6 | `8716a5014c1f…e9b9` | 8,301 | 213 | Ground-truth speaker probe (reads `gpt_purified_history.txt`). |
| `nh_ingest_chatgpt__1_.py` | B7 | `b8af9f1d36d9…b201` | 5,128 | 148 | Clean ChatGPT-export ingest; `role` carried, not guessed; DRY_RUN default. |
| `nh_architecture_canvas.html` | B5 | `971833b6c4b3…0cf2` | 8,819 | 174 | Draggable-node architecture canvas prototype. |
| `nh_2a_prototype.html` | B7 | `b3abcbb47273…f164` | 13,062 | 259 | Interactive 2a roots/readings two-store prototype. |
| `nh_icon_combined.html` | B4 | `6e194dfdd6c8…bc6a` | 6,089 | 117 | Combined icon prototype. |
| `NH_live_mechanism.html` | B6 | `b329a5e4cf24…6bb8` | 18,314 | 316 | Live-mechanism HTML (shorter). |
| `NH_live_mechanism__1_.html` | B6 | `a446529396100…fd071` | 21,576 | 332 | Live-mechanism HTML (longer; related version). |
| `NH_live_mechanism_picture.svg` | B1, B6 | `4a9bd78d4f49…b42b` | 5,697 | 79 | Live-mechanism SVG diagram. |
| `NH_live_mechanism_picture__1_.svg` | B6 | `4a9bd78d4f49…b42b` | 5,697 | 79 | Exact dup of the SVG. |
| `files__3_.zip` | B7 | `a32e34c91ebb…3291` | 37,097 | (archive) | ZIP container. Members byte-identical to loose `NH_MASTER-11_1.md` + `NH_DECISION_DEFAULTS-S10_1.md`. |

---

## 3. EXACT-DUPLICATE GROUPS (linked; every filename preserved separately)

Each group shares ONE SHA-256. Every physical filename + batch occurrence is retained; only one body is kept for comparison.

1. **`cfdaefe9…ce152`** — MASTER-17 FULL: `NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md` (B1, B2, B3). 3 occurrences.
2. **`0e8b59e3…65cf`** — Authoritative Master-19: `NH_MASTER-19_CORRECTED_v7_1__1_.md` (B3) ≡ Project `NH_MASTER-19_CORRECTED_v7_1.md`.
3. **`6cd09329…e696`** — Authoritative Defaults: `NH_DECISION_DEFAULTS-S19_v2_2__1_.md` (B3) ≡ Project copy.
4. **`5050d088…96e9`** — `cursorrules__1_` (B3) ≡ Project copy.
5. **`afb1bad3…c098c`** — wellbeing: `NH_wellbeing_baseline_system.md` (B1, B4) + `…__1_.md` (B3). 3 occurrences / 2 filenames.
6. **`a0281060…7619`** — working roles: `NH_WORKING_ROLES.md` (B2, B3) + `NH_WORKING_ROLES__2_.md` (B3). 2 filenames.
7. **`7dce7058…b1c7`** — `NH_Universal_Filter_Design__1_.md` (B1, B4). 2 occurrences.
8. **`ba98f5c9…f19a`** — field-survey PDF: `…Field.pdf` + `…Field__1_.pdf` (both B4). 2 filenames.
9. **`d19a3c22…8a06`** — `nh_research_architecture_explained.md` + `…__1_.md` (both B4). 2 filenames.
10. **`06f69672…daed`** — COMPLETE standalone: `NH_MASTER_FILE_COMPLETE__1_.md` (B4) + `__2_.md` (B5). 2 filenames.
11. **`052731353b4a…107e`** — MASTER-9_2: `NH_MASTER-9_2.md` (B5) + `__1_.md` (B5, B6). 3 occurrences / 2 filenames.
12. **`32b11721…2bab`** — DD ADD: `NH_DECISION_DEFAULTS_ADD.md` (B5, B6) + `…__1_.md` (B5, B6). 4 occurrences / 2 filenames.
13. **`91d82ed5…68b9`** — `NH_MASTER_section13_ADD.md` (B5, B6). 2 occurrences.
14. **`45ec88c4…3e29`** — `NH_DECISION_DEFAULTS__1_.md` (B5, B6). 2 occurrences.
15. **`4a9bd78d…b42b`** — live-mechanism SVG: `NH_live_mechanism_picture.svg` (B1, B6) + `…__1_.svg` (B6). 3 occurrences / 2 filenames.
16. **`757b6dd8…0112`** — chat front-door: `NH_chat_frontdoor_design_sketch.md` (B1, B6) + `…__1_.md` (B6). 3 occurrences / 2 filenames.
17. **`e2c0f915…c2ae`** — MASTER-13: `NH_MASTER-13.md` (B7) + `…__1_.md` (B7, B8). 3 occurrences / 2 filenames.
18. **`0ff6dd4c…e2f0`** — DD-S13__1_: `NH_DECISION_DEFAULTS-S13__1_.md` + `__2_.md` (B7, B8, B9 each). 6 occurrences / 2 filenames.
19. **`6dc26159…f5c3`** — MASTER-14_FINAL base: `NH_MASTER-14_FINAL.md` (B7, B8, B9) + `__1_.md` (B8, B9). 5 occurrences / 2 filenames.
20. **`55fab7e7…d720`** — MASTER-14_FINAL larger: `…__2_.md` + `…__3_.md` (B8, B9 each). 4 occurrences / 2 filenames.
21. **`8acc7138…f86d`** — DD-S13__4_: `…__4_.md` + `…__6_.md` (B8, B9 each). 4 occurrences / 2 filenames.
22. **`7270cc48…448c`** — MASTER-11.1: loose `NH_MASTER-11_1.md` (B7) + member inside `files__3_.zip` (B7). 2 occurrences (loose + archived).
23. **`b018ae48…968c`** — DD-S10.1: loose `NH_DECISION_DEFAULTS-S10_1.md` (B7) + member inside `files__3_.zip` (B7). 2 occurrences (loose + archived).

**Single-filename exact re-uploads across batches** (same filename re-supplied, one body): `NH_MASTER-14.md` (B7/B8/B9), `__1_`–`__4_` (B7/B8/B9), `NH_MASTER-14_FINAL__4_` (B8/B9), `NH_DECISION_DEFAULTS-S12` (B7/B8/B9), `NH_DECISION_DEFAULTS-S13` (B7/B8/B9), `NH_DECISION_DEFAULTS-S13__3_` (B7/B8/B9), `NH_MASTER_FILE_COMPLETE__2_` etc. Each occurrence is recorded in its batch receipt.

---

## 4. RELATED-VERSION (NEAR-DUPLICATE) FAMILIES — flagged for line-by-line diff; NO WINNER CHOSEN

These have DISTINCT hashes and require comparison later. None is yet judged more complete.

- **Universal Filter Design (3 tiers):** bare (`3df666eb`, no Keystone/Membrane) → `__1_` (`7dce7058`, +Keystone) → `__2_` (`c8938d37`, +Keystone +MEMBRANE). The Membrane section exists ONLY in `__2_` among the *design* copies (full ruleset form is separately in `NH_Universal_Filter_RULES.md`).
- **Meaning Engine Design:** B1 (`18185908…0d62`) vs B5 (`15c27860…9a89`) — separator-formatting variant.
- **Risk review:** bare (`3864a2eb`) vs `__1_` (`6fa53662`, +boot-error/silent-auto-start resolution).
- **MASTER_FILE_COMPLETE:** bare 156-line (`80a6143e`) vs standalone 257-line (`06f69672`).
- **MASTER-6:** `63a64d08` (273L) vs `__1_` (`3e978e03`, 315L).
- **MASTER-9 / 9_2:** `e6bf27a4` (442L) vs `052731353b4a` (513L).
- **MASTER-10:** `4ee57d29` (406L) vs `__1_` (`f9e78360`, 407L).
- **MASTER-14 family (5 distinct bodies):** `493f50b8` (340L) · `9a3f2b1e` (379L) · `f9dd9d95` (379L) · `1dec9fe0` (389L) · `ea4bcbdd` (389L).
- **MASTER-14_FINAL family (3 distinct bodies):** `6dc26159` (427L) · `55fab7e7` (434L) · `f632babe` (434L).
- **DD-S13 family (4 distinct bodies):** `eaea2e2c` (121L) · `0ff6dd4c` (123L) · `f6358c44` (124L) · `8acc7138` (125L).
- **Live-mechanism HTML:** `b329a5e4` (316L) vs `__1_` (`a4465293`, 332L).
- **MASTER-19 lineage:** v1 (`0287015b`) → v3 (`e38c37e9`) → v6 (`8165f4be`) → v7_1 (`0e8b59e3`), plus FULL (`bc498fda`) and the four reader slices.
- **Decision Defaults early lineage:** bare (`2abb2e45`) → `__1_` compass (`45ec88c4`) → `__2_` session-9 (`11f71f44`).

---

## 5. REFERENCED-BUT-NOT-SUPPLIED SOURCE LIST

Named inside supplied files but never provided as physical files:

**Ingest sources / stores (code-referenced):**
- `gpt_purified_history.txt` (source the probes + ground-truth probe read)
- `cleaned_history (1).txt` (declared damaged / not ingested)
- `conversations-000.json`, `conversations-001.json`, `conversations-002.json` (ChatGPT-export ingest sources)
- `nh_accretive_store.py` (imported by `nh_probe.py`, `nh_ingest_chatgpt.py`, the Cursor brief target)
- `.nh_accretive_store.jsonl` / `.nh_roots` / `.nh_readings_store.jsonl` / `.nh_roots.sealed` (runtime stores)
- `ingest_seeds.py`

**Masters referenced but absent:** MASTER-9.1, MASTER-9.3 (named in 9.4 header), MASTER-12 (S12 defaults sync to MASTER-13; a 12 was generated), MASTER-15 (named as DELTA_S14 regen target), MASTER-16, MASTER-19_v7, MASTER-19_v2 / v4 / v5.

**Gold sets:** `NH_GOLD_SET_v1.md`, `NH_GOLD_SET_v2_B.md`, `NH_GOLD_SET_CONTEXT_v1.md`.

**Other design / handoff docs:** `NH_INTERFACE_WORLD_DESIGN_LOG.md`, `NH_CHATGPT_PROJECT_HANDOFF_CLAUDE_S17.md`, `NH_DECISION_DEFAULTS-S17_DRAFT.md` (distinct from the supplied S17_AUDITED_v1).

**Prototype / output HTML:** `nh_canvas_test.html`, `nh_icon_styles.html`, `nh_log.html` (output of `nh_log.py`).

**Other runtime code named in files:** `nh_sovereignty_sync.py`, `nh_service.py`, `nh_peek.py`, `nh_clinical_report.py`, `nh_lawyer_simulator.py`, `nh_nightly.py`, `nh_vector_memory.py`, `test_brave.py`.

*(Note: the Project Knowledge folder also holds `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`, which is a project file, not part of the uploaded baseline batches.)*

---

## 6. CURRENTLY EVIDENCED MASTER CHRONOLOGY & AUTHORITY HISTORY

By internal evidence (headers, deltas, session markers). Chronology only — **NOT a completeness ranking.**

**Master numeric lineage:**
`MASTER-5 (session 2) → 6 (two copies) → 7 → 8 → 9 → 9_2 → 9_4 (session 8: +§13, +§14 sketch) → 10 (session 9: +§0 premise; reality reworked) → 11 (session 10: reality→STORY re-souling) → 11.1 (session 10 eve: +§0A DUMB/SMART, 2a shape) → [12 MISSING] → 13 (store built & clean) → 14 family (8 bodies, incl. 3 FINAL sub-versions) → [DELTA_S14 + Cursor brief: post-14, pre-15] → [15, 16 MISSING] → 17_FULL_v2 (+4 reader slices) → 18_FULL_v1 → 19_FULL (RTX 5060 Ti) → 19_v1 → 19_v3 → 19_v6 → 19_v7_1 (ADOPTED AUTHORITATIVE)`

**Parallel early family:** `NH_MASTER_FILE_COMPLETE` (bare 156L) and standalone (257L) sit around the Master-5/6 era.

**Decision Defaults lineage:**
`bare → __1_ (DESIGN COMPASS) → __2_ (session 9) → S10.1 → S12 → S13 family (4 bodies) → [S17_AUDITED_v1 / S17_DRAFT missing] → S19_v1 → S19_v2_2 (AUTHORITATIVE)`

**Authority state (as declared by handoff files, not re-judged):**
- Authoritative pair = `NH_MASTER-19_CORRECTED_v7_1.md` + `NH_DECISION_DEFAULTS-S19_v2_2.md`, governed by `cursorrules`.
- `NH_MASTER-19_CORRECTED_v6` is the declared predecessor; v1/v3 are candidates.
- The two big accepted-design companions (SECURITY_IDENTITY_AFTER_BGMM, TSC_DESIGN_v1) declare themselves NOT-yet-patched into the Master.

---

## 7. UNRESOLVED CONFLICTS, MISSING-FEATURE WARNINGS & RECOVERY FLAGS (recorded, NOT acted on)

1. **§8 research-pipeline security rules:** MASTER-19_v3 header states these were "dropped between Master-5 and Master-17, restored S19." Master-5 is now in hand → the drop/restore is checkable later. **Possible-dropped-feature flag.**
2. **THE MEMBRANE (Rule 7):** full ruleset form in `NH_Universal_Filter_RULES.md`; design form ONLY in `Universal_Filter_Design__2_` (absent from bare and `__1_`). Check survival into later Masters. **Recovery flag.**
3. **Reality → STORY re-souling:** MASTER-10 uses the reality model; MASTER-11 replaces it with per-person STORY-layer. Load-bearing conceptual shift to track across the 11→13→14→17→19 chain. **Conflict-to-track.**
4. **Name spelling conflict:** old `NH_MASTER_CONTEXT.md` mandates "Nes"; the COMPLETE masters and most later files use "Ness." **Unresolved wording conflict.**
5. **Accepted-but-unpatched design:** `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM` and `NH_ACCEPTED_TSC_DESIGN_v1` declare themselves companion-records not yet folded into Master v6 → substantial accepted design may be absent or summarized-only in the authoritative v7_1. **Completeness flag.**
6. **Schema evolution 8→12 fields:** earlier files describe an "8-field reading record"; `NH_DELTA_S14` + the Cursor brief expand it to a 12-field reading contract. Track which the authoritative Master reflects. **Schema-detail flag.**
7. **S12 hard-won safeguards:** "disk-verify every [BUILT] claim" (five false-built claims fell in one session), backup-before-destructive, watch-Cursor's-agent for unsolicited launcher/`.bat`/tunnel artifacts. Check survival into S19 defaults. **Recovery flag.**
8. **MASTER-14_FINAL "FINAL" label vs three sub-versions:** three increasingly-large bodies all carry "FINAL." The label does not establish which is most complete. **No-winner flag.**
9. **`cleaned_history` deliberately not ingested:** declared damaged/redundant (S12). Recorded as a deliberate exclusion, not a gap. **Status note.**
10. **Hardware row drift:** `NH_MASTER-19_FULL.md` still shows RTX 5060 Ti; later context is RTX 3090. Track which Masters carry which. **Wording-drift note.**
11. **MASTER-12, 15, 16 and several DD/S17 variants missing:** lineage gaps where transitions can't yet be traced through a physical file. **Gap flag.**

**Genuinely-open design forks recorded in supplied files (NOT to be resolved here):** is-N.H-a-perspective (closed by S10.1/S11 era per the defaults, but recorded historically); Llama vs Qwen on real Hebrew (test required before locking); the confidence value-form (deliberately unfrozen); the insufficient-context retry-trigger (deferred); multi-box / person-box mechanics; clash/gap-read UI surfacing; the §0A DUMB/SMART section's final placement; the chat-front-door always-on-vs-deliberate-keep capture question.

---

## 8. WHAT HAS NOT BEEN DONE (explicit)

No full Master comparison · no feature-recovery audit · no restoration · no reconciliation · no rewriting · no consolidation · no final self-contained Master · no Decision-Defaults regeneration · no adoption of any candidate · no overwrite of any prior Master. This manifest is provenance only. The next phase begins only on Ness's explicit instruction.

---

*Manifest generated after Batch 9 (final). All 133 upload occurrences across 9 batches preserved in the batch receipts; 100 filenames / 86 unique content hashes currently resident; 0 unreadable. Every duplicate retained in the provenance record.*
