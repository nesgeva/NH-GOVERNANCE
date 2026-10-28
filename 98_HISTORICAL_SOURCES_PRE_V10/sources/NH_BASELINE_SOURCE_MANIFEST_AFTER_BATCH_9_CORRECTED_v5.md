# N.H — BASELINE SOURCE MANIFEST (AFTER BATCH 9) — CORRECTED v5

**Status: PERMANENT PROVENANCE RECORD — fourth provenance-correction pass. NOT a consolidation, audit, or feature-recovery ledger.**

Supersedes v1 (SHA-256 dc189254f51206809ab5affdae97a61f7df6196a2e43a03b02a630716b1941b8), v2 (SHA-256 e7bdfeeb47c2151d64473c764bc2decb8e6c6f221f0b9a6b5ef3ae0d5632ccfb), v3 (SHA-256 01e0af2b3f08004483c191670e56142fb2c62de65f293594c625907f86b731b5), and v4 (SHA-256 814c4b725cf5c7e0cada23216757a4bdae65b3084ebd57a62ca1f0851ef0d73c), all preserved unchanged. The substantive provenance ledgers (Resident Source Ledger, Upload Occurrence Ledger, Project Knowledge Ledger) are carried forward from v4 unchanged. This v5 makes only these reporting/consistency corrections: (1) §1 splits the unverified metric into "unresolved resident-file mappings" and "occurrence identities marked UNVERIFIED"; (2) the Batch 3 appendix (now §11) retitled "Batch 3 evidence and contradiction appendix" (the literal Batch 3 path list was not recoverable, so it is not described as verbatim); (3) §1 Batch 3 wording corrected (total 16 verified; 11 distinct-new verified; 5 repeat identities unverified); (4) the placeholder check reworded to exclude quoted explanatory examples; (5) backticked-hash count recomputed from the completed v5 body; (6) continuous section numbering restored. No source row, occurrence identity, hash, authority status, feature status, or design content was changed.

Generated after: *"FINAL BATCH — ALL CURRENTLY LOCATED SOURCE FILES HAVE NOW BEEN SUPPLIED."*

---

## 0. STANDING RULES

1. **Newer ≠ more complete.** Later/larger/"FINAL"/adopted is not assumed more complete; only direct comparison (not done) establishes that.
2. **Duplicates never disappear.** Every upload occurrence, exact duplicate, copy-suffix file, reader copy, backup, and archive member keeps its own row; linked by shared SHA-256, never collapsed.
3. **Older Masters may preserve original features.** Early-and-absent-later material is possibly-dropped design to recover later.
4. **No design decision silently resolved.** Conflicts/forks recorded and preserved.
5. **No consolidation begun.** Provenance only.

---

## 1. RECALCULATED CUMULATIVE COUNTS (reconcile with the ledgers)

| Metric | Count | Definition |
|---|---|---|
| **Actual upload occurrences (Batches 1–9)** | **154** | Every `<file_path>` attachment line across the nine batch messages, including within-message and cross-batch repeats. |
| Per-batch occurrences | B1:15 · B2:14 · B3:16 · B4:13 · B5:19 · B6:20 · B7:18 · B8:19 · B9:20 | B2 = 7 filenames each listed twice (14). For B3: the total of 16 paths is VERIFIED from the Batch 3 receipt, and the 11 distinct-new filenames are VERIFIED; the exact identity of the 5 repeat occurrences is UNVERIFIED (the literal Batch 3 path list was not recoverable). Not all Batch 3 identities were verified from a literal path list. See §3A and the Batch 3 evidence and contradiction appendix in §11. |
| **Loose resident filenames** | **100** | Distinct exact filenames in the upload directory. |
| **Archive-member source records** | **2** | Members inside `files__3_.zip` (not extra uploads). |
| **Total resident/archive source-record rows (Ledger A)** | **102** | 100 loose + 2 archive members. |
| **Unique SHA-256 content hashes (loose resident, incl. ZIP container)** | **86** | Distinct loose bodies. |
| Redundant physical copies (loose, beyond first per hash) | 14 | |
| Exact-duplicate filename groups (loose, >1 filename per hash) | 14 | |
| Unreadable items | 0 | |
| Unresolved resident-file mappings | 0 | All 154 occurrence rows resolve to a known content hash (a resident loose file, the ZIP container, or — for the B1 Meaning Engine row — a recorded historical body). No occurrence points to an unknown/unresolved file. |
| Occurrence identities marked UNVERIFIED | 5 | All 154 occurrence rows resolve to known content hashes, but the exact filenames of the five Batch 3 repeat occurrences (occ #41–45) remain unverified — the original Batch 3 `<uploaded_files>` block was not recoverable and the Batch 3 receipt is internally contradictory. See §3 and §11. |
| **Project Knowledge files (separate from uploads)** | **4** | See §5. |

**Correction trail:** v1 reported 133 (sum of headline distinct-new). v2 reported 142 (attachment lines, but B2/B3 were taken from the deduplicated lists, undercounting). v3 and v4 report **154**, rebuilt from the literal batch-message path lists with B2=14 and B3=16 restored. All three figures are recorded; none hidden.

---

## 2. RESIDENT SOURCE LEDGER (A) — 100 loose files + 2 archive members

Full 64-char hashes; literal first headings (extracted programmatically from each file); exact filenames.

### 2A.1 — Loose resident files

| # | Exact Filename | Source | Batches | SHA-256 (64 hex) | Bytes | Lines | Read | Literal first heading / first meaningful line | Description | Declared status | Dup-group | Related-version family | Authority |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM__1_.md` | upload directory | B3 | `fb36bf8e55026ed7d79e4a5264be17f2577dda3276c4b2d2dc320018931f16f5` | 71936 | 1724 | YES | # NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md | Companion record, declared NOT authoritative; 'not yet patched into Master v6.' | Companion, NOT authoritative | G-ACCSEC | - | Companion (declared non-authoritative) |
| 2 | `NH_ACCEPTED_TSC_DESIGN_v1__1_.md` | upload directory | B3 | `1da2e296d4345d11dcec5f197aa9a42883349526275c5aa32b0bb07d1ca44658` | 43237 | 956 | YES | # Temporary Session Cache (TSC) — Final Accepted Design | Companion record (Temporary Session Cache), declared NOT authoritative. | Companion, NOT authoritative | G-ACCTSC | - | Companion (declared non-authoritative) |
| 3 | `NH_Build_Checklist.md` | upload directory | B5 | `e4d1436a3e5655ce4b09135c65424a2a672157731441f48f954044aa5d1aea40` | 4325 | 95 | YES | # N.H — SIMPLE BUILD CHECKLIST | V/X built-vs-unbuilt snapshot (June 20 2026). | Status snapshot | G-CHECKLIST | - | Historical status |
| 4 | `NH_CHAT_HANDOFF_AFTER_BGMM__1_.md` | upload directory | B3 | `f524f7cdd4dd2f1b897177e0e7f0843d1c8a7767341e4a010da9ab066414a562` | 8081 | 171 | YES | # NH_CHAT_HANDOFF_AFTER_BGMM.md | Handoff: authority order Master v6->DD v1->roles; 13 accepted security/identity/BGMM components. | Handoff record | G-HANDOFF1 | - | Handoff record |
| 5 | `NH_CURSOR_BRIEF_reading_validator.md` | upload directory | B9 | `d80065191b04f26d3b0834cd1e861fda68a28d6c61f80d2bd458fce37ac70ba9` | 9455 | 86 | YES | # CURSOR BRIEF — Reading Validator + Reading-Shaped Writer | Build spec: 12-field reading contract + reading-shaped writer. Spec only, not approved code. | Build spec, not approved | G-CURSORBRIEF | - | Build spec |
| 6 | `NH_Canvas_Design_Spec.md` | upload directory | B4 | `20444814d0ac1cf5ff49a927862b0025c9c069760e425999dbff7a2893e1d5b5` | 4995 | 78 | YES | # N.H Interactive Architecture Canvas — Design Spec | Canvas design spec. | Spec | G-CANVAS | - | Design source |
| 7 | `NH_DECISION_DEFAULTS-S10_1.md` | upload directory | B7 | `b018ae48f8863c223a2a345c7747877722e1c6b108bab754c78c9182e774968c` | 10874 | 88 | YES | # N.H — DECISION DEFAULTS | S10.1 Decision Defaults (matches MASTER-11.1): 2a two-file structure; Helper-not-Decider. Also a member inside files__3_.zip. | Decision Defaults, historical | G-DDS101 | Decision Defaults lineage | Historical companion |
| 8 | `NH_DECISION_DEFAULTS-S12.md` | upload directory | B7,B8 | `da329e8652ba0f35a4b2d864ade986ca7c61c1324240d84804ffc808c944cfa8` | 12602 | 103 | YES | # N.H — DECISION DEFAULTS | S12: store BUILT & clean (5,521 roots, 7-field w/ role); disk-verify-[BUILT]-claims lesson. | Decision Defaults, historical | G-DDS12 | Decision Defaults lineage | Historical companion |
| 9 | `NH_DECISION_DEFAULTS-S13.md` | upload directory | B7,B8,B9 | `eaea2e2ccb3118d50a44d06bda5f12f94bb436ea1cde5411b98370334cd9644a` | 18133 | 121 | YES | # N.H — DECISION DEFAULTS | S13 Decision Defaults family — smallest (121 lines). | Decision Defaults, historical | G-DDS13 | DD-S13 family | Historical companion |
| 10 | `NH_DECISION_DEFAULTS-S13__1_.md` | upload directory | B7,B8,B9 | `0ff6dd4ce29b7001596db5dd4862fa66d976efe64430653850a735db06f9e2f0` | 19065 | 123 | YES | # N.H — DECISION DEFAULTS | S13 Decision Defaults family (123 lines). | Decision Defaults, historical | G-DDS131 | DD-S13 family | Historical companion |
| 11 | `NH_DECISION_DEFAULTS-S13__2_.md` | upload directory | B7,B8,B9 | `0ff6dd4ce29b7001596db5dd4862fa66d976efe64430653850a735db06f9e2f0` | 19065 | 123 | YES | # N.H — DECISION DEFAULTS | S13 Decision Defaults family (123 lines). | Decision Defaults, historical | G-DDS131 | DD-S13 family | Historical companion |
| 12 | `NH_DECISION_DEFAULTS-S13__3_.md` | upload directory | B7,B8,B9 | `f6358c44db6e115309e2b1d25a818fe2f02d86a79cea6fefa9daa31bfeead4f1` | 22527 | 124 | YES | # N.H — DECISION DEFAULTS | S13 Decision Defaults family (124 lines). | Decision Defaults, historical | G-DDS133 | DD-S13 family | Historical companion |
| 13 | `NH_DECISION_DEFAULTS-S13__4_.md` | upload directory | B8,B9 | `8acc713871d9c9160143014ebd5823df61df7082fd37ed27e3d20c4b4314f86d` | 23616 | 125 | YES | # N.H — DECISION DEFAULTS | S13 Decision Defaults family — largest (125 lines). | Decision Defaults, historical | G-DDS134 | DD-S13 family | Historical companion |
| 14 | `NH_DECISION_DEFAULTS-S13__6_.md` | upload directory | B8,B9 | `8acc713871d9c9160143014ebd5823df61df7082fd37ed27e3d20c4b4314f86d` | 23616 | 125 | YES | # N.H — DECISION DEFAULTS | S13 Decision Defaults family — largest (125 lines). | Decision Defaults, historical | G-DDS134 | DD-S13 family | Historical companion |
| 15 | `NH_DECISION_DEFAULTS-S17_AUDITED_v1.md` | upload directory | B2 | `a0df064a0f4dce25825282e67619ff0c3e0319c37916ca463539b4d1390f69fe` | 26274 | 390 | YES | # N.H — DECISION DEFAULTS (S17 — DRAFT) | S17 audited Decision Defaults; titled DRAFT / derived-not-authority. | Decision Defaults, titled DRAFT | G-DDS17 | Decision Defaults lineage | Historical companion / draft |
| 16 | `NH_DECISION_DEFAULTS-S19_v1__1___1_.md` | upload directory | B3 | `ecea9224163681f9fc1d29327b0453c5e7ead42fd178786ab9dc6a6d4e1baaa6` | 33328 | 298 | YES | # N.H — DECISION DEFAULTS (S19) | S19_v1 Decision Defaults — synced to Master v6. | Decision Defaults, candidate | G-DDS19V1 | Decision Defaults lineage | Historical companion / candidate |
| 17 | `NH_DECISION_DEFAULTS-S19_v2_2__1_.md` | upload directory | B3 | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` | 37048 | 314 | YES | # N.H — DECISION DEFAULTS (S19) | ADOPTED AUTHORITATIVE Decision Defaults. Identical to Project Knowledge copy. | ADOPTED AUTHORITATIVE | G-DDS19V22 | Decision Defaults lineage | ADOPTED AUTHORITATIVE (explicit) |
| 18 | `NH_DECISION_DEFAULTS.md` | upload directory | B5 | `2abb2e4570f77a63ef087cfa2fc10cb08210cadb01e9bd304d84d2555249b047` | 4304 | 58 | YES | # N.H — DECISION DEFAULTS | Earliest bare Decision Defaults (no DESIGN COMPASS). | Decision Defaults, historical | G-DD0 | Decision Defaults early lineage | Historical companion |
| 19 | `NH_DECISION_DEFAULTS_ADD.md` | upload directory | B5,B6 | `32b1172159b60afe231f29e132c6c7a39c7eaaf2faf8ced9ec7c7ed473e52bab` | 1355 | 12 | YES | # N.H — ADD TO DECISION_DEFAULTS | Standalone DESIGN COMPASS add-on fragment. | Add-on fragment | G-DDADD | Decision Defaults add-ons | Historical fragment |
| 20 | `NH_DECISION_DEFAULTS_ADD__1_.md` | upload directory | B5,B6 | `32b1172159b60afe231f29e132c6c7a39c7eaaf2faf8ced9ec7c7ed473e52bab` | 1355 | 12 | YES | # N.H — ADD TO DECISION_DEFAULTS | Standalone DESIGN COMPASS add-on fragment. | Add-on fragment | G-DDADD | Decision Defaults add-ons | Historical fragment |
| 21 | `NH_DECISION_DEFAULTS__1_.md` | upload directory | B5,B6 | `45ec88c440456ce7aa99babe8b58ed088786ed342d5197ab4fef8b69d24d3e29` | 5388 | 65 | YES | # N.H — DECISION DEFAULTS | Decision Defaults + DESIGN COMPASS block folded in. | Decision Defaults, historical | G-DD1 | Decision Defaults early lineage | Historical companion |
| 22 | `NH_DECISION_DEFAULTS__2_.md` | upload directory | B6 | `11f71f447c17ea48a269adf9c206aa8f23d88a1207ae7388fafb6d9a94004bdc` | 7205 | 74 | YES | # N.H — DECISION DEFAULTS | Session-9 Decision Defaults: §0 premise, per-person STORY reading, carry-the-speaker, open-forks list. | Decision Defaults, historical | G-DD2 | Decision Defaults early lineage | Historical companion |
| 23 | `NH_DELTA_S14.md` | upload directory | B9 | `f94b5351e56242ce4f1797b417cd482bd25ec5549c73491d218fbdbffa92af9f` | 9612 | 88 | YES | # N.H — DELTA S14 | Session-14 delta: closes confidence/gold-scoring/failure-behavior forks. Decisions only, nothing built. | Delta, decisions-only | G-DELTAS14 | - | Historical delta |
| 24 | `NH_INSIGHT__the_line_under_all_the_lines.md` | upload directory | B6 | `77b5932819a653504cfb1493bf6e9ba94b6c95696a802627cdbdb2589d548ab1` | 2224 | 37 | YES | # N.H — THE LINE UNDER ALL THE LINES | Standalone compass insight ('not-deciding is safe'). | Standalone insight | G-INSIGHT | - | Design compass |
| 25 | `NH_MASTER-10.md` | upload directory | B6 | `4ee57d298f11a8ad14ea820f157a4c523d4ed16b8532aa14da9cf418ad6fb7d8` | 74496 | 406 | YES | # N.H — MASTER (complete, self-contained, full depth) | MASTER-10 (session 9): adds §0 PREMISE; reality/simulation reworked in design. | Self-contained Master, candidate | G-MASTER10 | MASTER-10 family | Historical Master |
| 26 | `NH_MASTER-10__1_.md` | upload directory | B6 | `f9e783601b1816f797bf82c8bebd70745335b6d5b837a62186c6c6ad6659b804` | 75898 | 407 | YES | # N.H — MASTER (complete, self-contained, full depth) | MASTER-10 near-duplicate (407 lines, ~1.4KB larger, same header). | Self-contained Master, candidate | G-MASTER10B | MASTER-10 family | Historical Master |
| 27 | `NH_MASTER-11.md` | upload directory | B6 | `10771ea4e9cb7a72596efaf0ac52a95d6b7805c215f637ca1e8e3063e050e3ba` | 91643 | 443 | YES | # N.H — MASTER (complete, self-contained, full depth) | MASTER-11 (session 10): 'reality-layer' REPLACED by 'per-person STORY-layer'. Load-bearing re-souling. | Self-contained Master, candidate | G-MASTER11 | MASTER lineage | Historical Master |
| 28 | `NH_MASTER-11_1.md` | upload directory | B7 | `7270cc48fd9af8afb2b0cb3157cb0549107a3467fa94172afe239367c6e7448c` | 80040 | 482 | YES | # N.H — MASTER (complete, self-contained, full depth) | MASTER-11.1 (session 10 eve): 2a reading-record shape; six-part STORY-layer; DUMB/SMART frame (§0A). Also a member inside files__3_.zip. | Self-contained Master, candidate | G-MASTER111 | MASTER lineage | Historical Master |
| 29 | `NH_MASTER-13.md` | upload directory | B7 | `e2c0f9152349e38331c529417ac0638cdd707b09ad6e9f39a69b4aaf3ef8c2ae` | 46704 | 318 | YES | # N.H — MASTER (complete, self-contained, full depth) | MASTER-13: model layer, person-boxes, tape, DUMB/SMART frame. (MASTER-12 not supplied.) | Self-contained Master, candidate | G-MASTER13 | MASTER lineage | Historical Master |
| 30 | `NH_MASTER-13__1_.md` | upload directory | B7,B8 | `e2c0f9152349e38331c529417ac0638cdd707b09ad6e9f39a69b4aaf3ef8c2ae` | 46704 | 318 | YES | # N.H — MASTER (complete, self-contained, full depth) | MASTER-13: model layer, person-boxes, tape, DUMB/SMART frame. (MASTER-12 not supplied.) | Self-contained Master, candidate | G-MASTER13 | MASTER lineage | Historical Master |
| 31 | `NH_MASTER-14.md` | upload directory | B7,B8,B9 | `493f50b8f85516e19b7b566f9603c0b5ce45c36f7a6c4a820a8b3d4a2ae10be4` | 54589 | 340 | YES | # N.H — MASTER (complete, self-contained, full depth) | MASTER-14 family, smallest body (340 lines). | Self-contained Master, candidate | G-MASTER14 | MASTER-14 family | Historical Master |
| 32 | `NH_MASTER-14_FINAL.md` | upload directory | B7,B8,B9 | `6dc26159e1862ec96d749581567f74d285490dd515775b77b6fbd7cb53e6f5c3` | 94146 | 427 | YES | # N.H — MASTER (complete, self-contained, full depth) | MASTER-14_FINAL base (427 lines). 'FINAL' tag NOT assumed most-complete. | Self-contained Master, candidate | G-MASTER14F | MASTER-14_FINAL family | Historical Master |
| 33 | `NH_MASTER-14_FINAL__1_.md` | upload directory | B8,B9 | `6dc26159e1862ec96d749581567f74d285490dd515775b77b6fbd7cb53e6f5c3` | 94146 | 427 | YES | # N.H — MASTER (complete, self-contained, full depth) | MASTER-14_FINAL base (427 lines). 'FINAL' tag NOT assumed most-complete. | Self-contained Master, candidate | G-MASTER14F | MASTER-14_FINAL family | Historical Master |
| 34 | `NH_MASTER-14_FINAL__2_.md` | upload directory | B8,B9 | `55fab7e730cb1f4b320b02411fbca954fc15259d7f13574b661af5d77c3fd720` | 101638 | 434 | YES | # N.H — MASTER (complete, self-contained, full depth) | MASTER-14_FINAL larger (434 lines). | Self-contained Master, candidate | G-MASTER14F2 | MASTER-14_FINAL family | Historical Master |
| 35 | `NH_MASTER-14_FINAL__3_.md` | upload directory | B8,B9 | `55fab7e730cb1f4b320b02411fbca954fc15259d7f13574b661af5d77c3fd720` | 101638 | 434 | YES | # N.H — MASTER (complete, self-contained, full depth) | MASTER-14_FINAL larger (434 lines). | Self-contained Master, candidate | G-MASTER14F2 | MASTER-14_FINAL family | Historical Master |
| 36 | `NH_MASTER-14_FINAL__4_.md` | upload directory | B8,B9 | `f632babe53640419ebcd2237d35d5d59cab393531f15a5ac0d18d28e8efba11a` | 102115 | 434 | YES | # N.H — MASTER (complete, self-contained, full depth) | MASTER-14_FINAL near-dup of larger (434 lines, +480B). | Self-contained Master, candidate | G-MASTER14F4 | MASTER-14_FINAL family | Historical Master |
| 37 | `NH_MASTER-14__1_.md` | upload directory | B7,B8,B9 | `9a3f2b1eaa63b22c32734252a66d30e0b098ed9dac5686a5952562b43fb10766` | 66566 | 379 | YES | # N.H — MASTER (complete, self-contained, full depth) | MASTER-14 family body (379 lines). | Self-contained Master, candidate | G-MASTER141 | MASTER-14 family | Historical Master |
| 38 | `NH_MASTER-14__2_.md` | upload directory | B7,B8,B9 | `f9dd9d957d459cb3abb32071338032a0d62c2c9434dce75d68e86ccbbfbbfbb3` | 67323 | 379 | YES | # N.H — MASTER (complete, self-contained, full depth) | MASTER-14 family body (379 lines, near-dup of __1_, +760B). | Self-contained Master, candidate | G-MASTER142 | MASTER-14 family | Historical Master |
| 39 | `NH_MASTER-14__3_.md` | upload directory | B7,B8,B9 | `1dec9fe0cc4fccea1a8951441ca3f6a81b54784712a3ed2da7fb0b56a1e07fd6` | 70277 | 389 | YES | # N.H — MASTER (complete, self-contained, full depth) | MASTER-14 family body (389 lines). | Self-contained Master, candidate | G-MASTER143 | MASTER-14 family | Historical Master |
| 40 | `NH_MASTER-14__4_.md` | upload directory | B7,B8,B9 | `ea4bcbdde17cd2bf802e37259565803ac32ecb9e4ff9120b1a7da579d69bb5ee` | 71138 | 389 | YES | # N.H — MASTER (complete, self-contained, full depth) | MASTER-14 family body (389 lines, near-dup of __3_, +860B). | Self-contained Master, candidate | G-MASTER144 | MASTER-14 family | Historical Master |
| 41 | `NH_MASTER-17_00_INDEX_STATUS.md` | upload directory | B1,B3 | `b7c794561d102eb682f219937c0c5b1551b338ed76a902e43d32101649fb96c9` | 26966 | 184 | YES | # DERIVED READER COPY — DO NOT EDIT INDEPENDENTLY | Derived reader copy (do-not-edit) of MASTER-17. | DERIVED READER COPY | G-M17-00 | MASTER-17 reader slices | Reader copy (derived) |
| 42 | `NH_MASTER-17_01_FOUNDATION_BUILT.md` | upload directory | B1,B3 | `da261935d739e30e8c8a2f4cdcdcbce47c29948511ad2fb7f9f48a6d52b9a008` | 23998 | 216 | YES | # DERIVED READER COPY — DO NOT EDIT INDEPENDENTLY | Derived reader copy of MASTER-17. | DERIVED READER COPY | G-M17-01 | MASTER-17 reader slices | Reader copy (derived) |
| 43 | `NH_MASTER-17_02_CONCEPTUAL_ARCHITECTURE.md` | upload directory | B1,B3 | `186717c1ba60f60c1a511231820d6d45805161966f93d8c26cbeeb8c5c24d341` | 76345 | 548 | YES | # DERIVED READER COPY — DO NOT EDIT INDEPENDENTLY | Derived reader copy of MASTER-17. | DERIVED READER COPY | G-M17-02 | MASTER-17 reader slices | Reader copy (derived) |
| 44 | `NH_MASTER-17_03_ROADMAP_INTERFACE_HISTORY.md` | upload directory | B1,B3 | `0a64a524d7325e5408fe591080ddec93bca2c9ae98ff4557cece6379dd53d5a9` | 40994 | 255 | YES | # DERIVED READER COPY — DO NOT EDIT INDEPENDENTLY | Derived reader copy of MASTER-17. | DERIVED READER COPY | G-M17-03 | MASTER-17 reader slices | Reader copy (derived) |
| 45 | `NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md` | upload directory | B1,B2,B3 | `cfdaefe9b0b6c134a911f102ae6479fb845662165a1cf216aec465ff816ce152` | 165109 | 1148 | YES | # N.H — MASTER-17 (complete, self-contained, full S17 draft) | MASTER-17 full draft (corrected v2). Source of the four reader slices. | Full draft Master, candidate | G-MASTER17 | MASTER-19 lineage | Historical Master |
| 46 | `NH_MASTER-18_FULL_DRAFT_v1.md` | upload directory | B2 | `2f63734c600f4f8ea212b15c99c81f0a00a415dd525afb7d5176168c9edb5397` | 206696 | 1464 | YES | # N.H — MASTER-18 (complete, self-contained, full S18 candidate) | MASTER-18 full draft. | Full draft Master, candidate | G-MASTER18 | MASTER-19 lineage | Historical Master |
| 47 | `NH_MASTER-19_CORRECTED_v1.md` | upload directory | B2 | `0287015be938212d8065e5f2d3ac9b952a1f8943a043864ef63614d1670beffb` | 262683 | 1779 | YES | # N.H — MASTER-19: Full Backup with All Additions | MASTER-19 corrected v1 (1779 lines). | Corrected Master, candidate | G-M19V1 | MASTER-19 lineage | Historical Master / candidate |
| 48 | `NH_MASTER-19_CORRECTED_v3.md` | upload directory | B1 | `e38c37e97491d7f13310fb9d5d961e86111aad9c917612ccb3ea12e27e127a7b` | 283033 | 1910 | YES | # N.H — MASTER-19: Full Backup with All Additions | MASTER-19 corrected v3 (1910 lines). Header names §8 security-rules drop 5->17 / restore S19. | Corrected Master, candidate | G-M19V3 | MASTER-19 lineage | Historical Master / candidate |
| 49 | `NH_MASTER-19_CORRECTED_v6__1_.md` | upload directory | B3 | `8165f4bed94d2d57140d49e93d3c85b8e2b259053e0b30ac4c675fa7463a1bf9` | 283081 | 1908 | YES | # N.H — MASTER-19: Full Backup with All Additions | MASTER-19 v6 — declared predecessor of v7_1; matches AFTER_BGMM handoff. | Corrected Master, declared predecessor of authoritative | G-M19V6 | MASTER-19 lineage | Declared predecessor of authoritative |
| 50 | `NH_MASTER-19_CORRECTED_v7_1__1_.md` | upload directory | B3 | `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf` | 291811 | 1937 | YES | # N.H — MASTER-19: Full Backup with All Additions | ADOPTED AUTHORITATIVE Master (1937 lines). Identical to Project Knowledge copy. | ADOPTED AUTHORITATIVE | G-M19V71 | MASTER-19 lineage | ADOPTED AUTHORITATIVE (explicit) |
| 51 | `NH_MASTER-19_FULL.md` | upload directory | B2 | `bc498fda2fea592fbb08fd7d1b1ded23f13d8522bfb1f2dc324095df5259caec` | 245244 | 1706 | YES | # N.H — MASTER-19: Full Backup with All Additions | MASTER-19 full. Hardware row still RTX 5060 Ti (pre-3090). | Full Master, candidate | G-MASTER19F | MASTER-19 lineage | Historical Master |
| 52 | `NH_MASTER-5.md` | upload directory | B5 | `f91fdf682bac232b468c95ac99b8af4e0e385afe5e532108bdd2721026d0692c` | 32737 | 223 | YES | # N.H — MASTER (complete, consolidated) | Earliest numbered Master (session 2). Names §3D security fixes BUILT; lower bound named in v3 header for the §8 rules drop/restore. | Consolidated Master, candidate | G-MASTER5 | MASTER-5 | Historical Master |
| 53 | `NH_MASTER-6.md` | upload directory | B5 | `63a64d0895e5ee4cebfc9b8a2399356afe1c505ecdf04ca8ee45f2d6079948cc` | 45407 | 273 | YES | # N.H — MASTER (complete, self-contained) | Master-6, shorter of two copies; rules+meaning-engine written in full. | Self-contained Master, candidate | G-MASTER6A | MASTER-6 family | Historical Master |
| 54 | `NH_MASTER-6__1_.md` | upload directory | B5 | `3e978e036871c1188400409bfa439380f5cce02e2afd4bbb2830d85b15fe7633` | 54506 | 315 | YES | # N.H — MASTER (complete, self-contained) | Master-6, longer copy (315 lines). | Self-contained Master, candidate | G-MASTER6B | MASTER-6 family | Historical Master |
| 55 | `NH_MASTER-7.md` | upload directory | B5 | `6868507ca073051860daadf80554e5e064b8d3d1b293427d28fede746ba135c4` | 60439 | 332 | YES | # N.H — MASTER (complete, self-contained, full depth) | Master-7. | Self-contained Master, candidate | G-MASTER7 | MASTER lineage | Historical Master |
| 56 | `NH_MASTER-8.md` | upload directory | B5 | `13675a34e039d726cd845bde8a7177e1f260dadb3a19b9b6ba4c7b2c87bde48a` | 80833 | 423 | YES | # N.H — MASTER (complete, self-contained, full depth) | Master-8. | Self-contained Master, candidate | G-MASTER8 | MASTER lineage | Historical Master |
| 57 | `NH_MASTER-9.md` | upload directory | B5 | `e6bf27a4d4c81ba7e9e9351014397c7668fb1a114f2aa32d6babbaccaae7a813` | 89479 | 442 | YES | # N.H — MASTER (complete, self-contained, full depth) | Master-9. | Self-contained Master, candidate | G-MASTER9 | MASTER-9 family | Historical Master |
| 58 | `NH_MASTER-9_2.md` | upload directory | B5 | `052731353b4a221d358133219c5c280aa2e4ada98a1445657aec17b6ce13107e` | 127717 | 513 | YES | # N.H — MASTER (complete, self-contained, full depth) | Master-9.2 revision (513 lines). | Self-contained Master, candidate | G-MASTER92 | MASTER-9 family | Historical Master |
| 59 | `NH_MASTER-9_2__1_.md` | upload directory | B5,B6 | `052731353b4a221d358133219c5c280aa2e4ada98a1445657aec17b6ce13107e` | 127717 | 513 | YES | # N.H — MASTER (complete, self-contained, full depth) | Master-9.2 revision (513 lines). | Self-contained Master, candidate | G-MASTER92 | MASTER-9 family | Historical Master |
| 60 | `NH_MASTER-9_4.md` | upload directory | B6 | `9bbc28dc31c7825d5f3927169526a23bfd0abff9f5a994ce3dc4fd6f7cf1e8dd` | 149631 | 580 | YES | # N.H — MASTER (complete, self-contained, full depth) | MASTER-9.4 (session 8): adds §13 live loop + §14 chat-front-door sketch. Header states nothing on disk changed (store 11,374/4 groups). | Self-contained Master, candidate | G-MASTER94 | MASTER lineage | Historical Master |
| 61 | `NH_MASTER_CONTEXT.md` | upload directory | B1 | `e6ae68b37a375d90ea04d6000e311cca7d4199c715e51bd6873f99d8f169f099` | 22765 | 323 | YES | # N.H — Master Project Context | Old context file. Mandates 'Nes' spelling (conflicts with corrected 'Ness'). | Context file, historical | G-CONTEXT | - | Historical (conflict source) |
| 62 | `NH_MASTER_FILE_COMPLETE.md` | upload directory | B4 | `80a6143e9857ee77e9cf75ebd1c55724938f23bd04aae8b9b761160171bfcd02` | 17065 | 156 | YES | # N.H — COMPLETE MASTER FILE | Bare COMPLETE master (156 lines). 'Supersedes...' | COMPLETE master, candidate | G-COMPLETE0 | MASTER_FILE_COMPLETE family | Historical Master |
| 63 | `NH_MASTER_FILE_COMPLETE__1_.md` | upload directory | B4,B5 | `06f69672fa89800f060c70864bf1fd87532aff4359f3e538c48b087f08d8daed` | 29203 | 257 | YES | # N.H — COMPLETE STANDALONE MASTER FILE | Standalone COMPLETE master (257 lines). | COMPLETE master, candidate | G-COMPLETE1 | MASTER_FILE_COMPLETE family | Historical Master |
| 64 | `NH_MASTER_FILE_COMPLETE__2_.md` | upload directory | B5 | `06f69672fa89800f060c70864bf1fd87532aff4359f3e538c48b087f08d8daed` | 29203 | 257 | YES | # N.H — COMPLETE STANDALONE MASTER FILE | Standalone COMPLETE master (257 lines). | COMPLETE master, candidate | G-COMPLETE1 | MASTER_FILE_COMPLETE family | Historical Master |
| 65 | `NH_MASTER_section13_ADD.md` | upload directory | B5,B6 | `91d82ed52bcbf497fc12a5c61d479ab5f8fb83f9fc341f878165c446238d68b9` | 7590 | 35 | YES | # N.H — ADD TO MASTER AS §13 | §13 live-loop add-on (fire-and-let-go). | Add-on fragment | G-S13ADD | Master add-ons | Historical fragment |
| 66 | `NH_Meaning_Engine_Design.md` | upload directory | B1,B5 | `15c2786003463fff73b22dd4bf49cf36df3da30ed27ef57e78663605d2e59a89` | 12479 | 138 | YES | # N.H — THE MEANING ENGINE | Meaning-engine mechanism (8 parts). Separator-formatting variant of the B1 copy. | Design (mechanism) | G-MEANING | Meaning Engine family | Design source |
| 67 | `NH_Mobile_App_Design_Spec.md` | upload directory | B1 | `023c82babd4231d0b6fc8235396454e4d07e06d9a769797a4a31c9867885812c` | 5438 | 82 | YES | # N.H Mobile Companion App — Design Spec (v3, final structure) | Mobile app design spec. | Spec | G-MOBILE | - | Design source |
| 68 | `NH_RECENT_CONTINUITY_NOTE_POST_MASTER17-3.md` | upload directory | B2 | `7d614546710c9aa66ff02f87449fe30505cb5a0d6d929462a4e719a71fe082e3` | 8861 | 239 | YES | # N.H RECENT CONTINUITY NOTE — POST MASTER-17 | Continuity note post-MASTER17. | Continuity note | G-CONTINUITY | - | Continuity note |
| 69 | `NH_SHARED_CHAT_HANDOFF_BEFORE_CONSOLIDATION_v1__1_.md` | upload directory | B3 | `47e6a8ba71fa7e90e8bb8ba671cad22291c950c2770d78e82eea6d331ca7d865` | 6590 | 185 | YES | # N.H CHAT HANDOFF — AUTHORITATIVE STATE AND NEXT TASK | Names authoritative pair + hashes. | Handoff record | G-HANDOFF2 | - | Handoff record |
| 70 | `NH_Universal_Filter_Design.md` | upload directory | B4 | `3df666eb4ff4d90e5a5a299f7f7d52361638a27feb1e727894f0e0658c421020` | 5740 | 88 | YES | # N.H Universal Filter — Theoretical Design | Bare UF design — no Keystone, no Membrane. | Design sketch | G-UFD0 | Universal Filter Design family | Design source |
| 71 | `NH_Universal_Filter_Design__1_.md` | upload directory | B1,B4 | `7dce7058c991dc1aeb583e7455234a6721c7fea089626fcccecf529f5b48b1c7` | 10321 | 131 | YES | # N.H Universal Filter — Theoretical Design | UF design + Keystone. | Design sketch | G-UFD1 | Universal Filter Design family | Design source |
| 72 | `NH_Universal_Filter_Design__2_.md` | upload directory | B4 | `c8938d370efdd072912cabb4adf844dba4cc581095d68fca7022cff30710be15` | 13755 | 155 | YES | # N.H Universal Filter — Theoretical Design | UF design + Keystone + MEMBRANE (Membrane section exists ONLY here among design copies). | Design sketch | G-UFD2 | Universal Filter Design family | Design source |
| 73 | `NH_Universal_Filter_RULES.md` | upload directory | B5 | `c0fb4528a332f4014782afacee63d167407e31cc88b1502ec8783900588b3a37` | 11828 | 178 | YES | # N.H UNIVERSAL FILTER — OPERATING RULES FOR ANY AI | 12-rule operating ruleset. Rule 6 (memory only adds), Rule 7 (the membrane), Rule 11 (steerer-not-clerk). | Ruleset (design) | G-UFRULES | Universal Filter | Design source |
| 74 | `NH_WORKING_ROLES.md` | upload directory | B2 | `a0281060abd7e7da791bb56a97316ab9ec41ab88fdd7884fac4c6434fa487619` | 3015 | 49 | YES | # N.H — WORKING ROLES | Role division (Ness owns meaning / Claude architects+audits / Cursor codes). | Roles governance | G-ROLES | - | Governance |
| 75 | `NH_WORKING_ROLES__2_.md` | upload directory | B3 | `a0281060abd7e7da791bb56a97316ab9ec41ab88fdd7884fac4c6434fa487619` | 3015 | 49 | YES | # N.H — WORKING ROLES | Role division (Ness owns meaning / Claude architects+audits / Cursor codes). | Roles governance | G-ROLES | - | Governance |
| 76 | `NH_chat_frontdoor_design_sketch.md` | upload directory | B1,B6 | `757b6dd889aedf4af840ecfa190e0404c79ccf609d37607a105dca85f0af0112` | 13532 | 105 | YES | # N.H — THE CHAT FRONT DOOR & THE LIVE SYSTEM | §14 chat front-door working sketch (explicitly unconfirmed). | Design sketch, unconfirmed | G-FRONTDOOR | Chat front-door | Design source (unconfirmed) |
| 77 | `NH_chat_frontdoor_design_sketch__1_.md` | upload directory | B6 | `757b6dd889aedf4af840ecfa190e0404c79ccf609d37607a105dca85f0af0112` | 13532 | 105 | YES | # N.H — THE CHAT FRONT DOOR & THE LIVE SYSTEM | §14 chat front-door working sketch (explicitly unconfirmed). | Design sketch, unconfirmed | G-FRONTDOOR | Chat front-door | Design source (unconfirmed) |
| 78 | `NH_honest_calibration_note.md` | upload directory | B1 | `4096cc357b1e8cd5d8d3cfc83a688946fa5a3145c9edbe83198d03ad5d28f6ac` | 5346 | 48 | YES | # N.H — Honest Calibration Note (Novelty & Reflection) | Honest-calibration note. | Note | G-CALIB | - | Note |
| 79 | `NH_live_mechanism.html` | upload directory | B6 | `b329a5e4cf24b8ccbbb13e876da05e5b5542efb8aed2476420e08cbb053d6bb8` | 18314 | 316 | YES | <title>N.H — the live mechanism (working sketch)</title> | Live-mechanism interactive HTML (shorter, 316 lines). | Prototype (HTML) | G-LIVEMECH0 | live_mechanism HTML family | Prototype |
| 80 | `NH_live_mechanism__1_.html` | upload directory | B6 | `a4465293961004e802cfa660e454d3aa2550bf136a94da5a8b7b2fa163fd7071` | 21576 | 332 | YES | <title>N.H — the live mechanism</title> | Live-mechanism interactive HTML (longer, 332 lines). | Prototype (HTML) | G-LIVEMECH1 | live_mechanism HTML family | Prototype |
| 81 | `NH_live_mechanism_picture.svg` | upload directory | B1,B6 | `4a9bd78d4f49bea70954e91aeeb07f46f135c731b994f439d6e8486bea7cb42b` | 5697 | 79 | YES | <svg xmlns="http://www.w3.org/2000/svg" width="880" height="600" viewBox="0 0 880 600" font-family="Inter, system-ui, -apple-system, sans-serif"> | Live-mechanism SVG diagram. | Diagram (SVG) | G-LIVESVG | - | Diagram |
| 82 | `NH_live_mechanism_picture__1_.svg` | upload directory | B6 | `4a9bd78d4f49bea70954e91aeeb07f46f135c731b994f439d6e8486bea7cb42b` | 5697 | 79 | YES | <svg xmlns="http://www.w3.org/2000/svg" width="880" height="600" viewBox="0 0 880 600" font-family="Inter, system-ui, -apple-system, sans-serif"> | Live-mechanism SVG diagram. | Diagram (SVG) | G-LIVESVG | - | Diagram |
| 83 | `NH_risk_review_and_openrouter.md` | upload directory | B4 | `3864a2eb1a8f97bf433bd7ebaf0a9d4d85ba6e09bbd26c9c39d1371d5fe6d598` | 5245 | 63 | YES | # N.H — Risk Review & OpenRouter Clarification | Risk review (bare). | Risk review | G-RISK0 | Risk review family | Design source |
| 84 | `NH_risk_review_and_openrouter__1_.md` | upload directory | B4 | `6fa53662b406edb1b410d56bb43560027fb7a7d6f9042db5233a6b5f60f710c7` | 8384 | 85 | YES | # N.H — Risk Review & OpenRouter Clarification | Risk review + boot-error/silent-auto-start resolution. | Risk review | G-RISK1 | Risk review family | Design source |
| 85 | `NH_wellbeing_baseline_system.md` | upload directory | B1 | `afb1bad3c1edad3e86e76c5a1cb278b1a1e03c750d4fa1af6f54ad804bcc098c` | 7926 | 140 | YES | # N.H — Wellbeing & Behavioral Baseline System | Behavioral-baseline wellbeing engine design. | Spec | G-WELLBEING | - | Design source |
| 86 | `NH_wellbeing_baseline_system__1_.md` | upload directory | B3 | `afb1bad3c1edad3e86e76c5a1cb278b1a1e03c750d4fa1af6f54ad804bcc098c` | 7926 | 140 | YES | # N.H — Wellbeing & Behavioral Baseline System | Behavioral-baseline wellbeing engine design. | Spec | G-WELLBEING | - | Design source |
| 87 | `N_H__Personal_AI__Sovereignty-First_Architecture_with_Mandatory_REALITY_SIMULATION_Gate_Surveyed_Against_the_Field.pdf` | upload directory | B4 | `ba98f5c9e2f073aacbb4999363d0a2e44fd9d90149665b49ee42d07c49eaf19a` | 470408 | N/A — binary/PDF (newline-byte count 9992) | YES | (binary PDF — no text heading) | 8-page field-survey PDF: N.H combination genuinely novel vs the field. | Field-survey PDF | G-PDF | - | External survey |
| 88 | `N_H__Personal_AI__Sovereignty-First_Architecture_with_Mandatory_REALITY_SIMULATION_Gate_Surveyed_Against_the_Field__1_.pdf` | upload directory | B4 | `ba98f5c9e2f073aacbb4999363d0a2e44fd9d90149665b49ee42d07c49eaf19a` | 470408 | N/A — binary/PDF (newline-byte count 9992) | YES | (binary PDF — no text heading) | 8-page field-survey PDF: N.H combination genuinely novel vs the field. | Field-survey PDF | G-PDF | - | External survey |
| 89 | `cursorrules__1_` | upload directory | B3 | `5050d08825b93acd72a79d07946e43c8cbe537e079517ccfe66bcae8e30e96e9` | 34821 | 717 | YES | # N.H System — Cursor Rules v3.2 | In-force code ruleset (.cursorrules v3.2). Identical to Project Knowledge copy. | ADOPTED AUTHORITATIVE (code ruleset) | G-CURSORRULES | - | ADOPTED AUTHORITATIVE (explicit) |
| 90 | `files__3_.zip` | upload directory | B7 | `a32e34c91ebb986e4fa1ba12bc6397bcdda91266b87f3427aa0e6e08c9543291` | 37097 | N/A — binary/archive (newline-byte count 128; members listed in 2A.2) | YES | (binary ZIP archive — no text heading) | ZIP container. Members byte-identical to loose NH_MASTER-11_1.md + NH_DECISION_DEFAULTS-S10_1.md. | Archive container | G-ZIP | - | Archive container |
| 91 | `nh_2a_prototype.html` | upload directory | B7 | `b3abcbb47273fefdbcc61f07cbeccc7b0945f981ff770121fbb174271a05f164` | 13062 | 259 | YES | <title>N.H — 2a prototype: roots & readings</title> | Interactive 2a roots/readings two-store prototype. | Prototype (HTML) | G-2APROTO | - | Prototype |
| 92 | `nh_architecture_canvas.html` | upload directory | B5 | `971833b6c4b3c6f1c57c094d40d0e3a9b27254087832d29ae46d3338cad90cf2` | 8819 | 174 | YES | <title>N.H — Architecture Canvas</title> | Draggable-node architecture canvas prototype. | Prototype (HTML) | G-ARCHCANVAS | - | Prototype |
| 93 | `nh_icon_combined.html` | upload directory | B4 | `6e194dfdd6c876e5b033cde9696e7b5ab11e8370268410e237b1e863bf90bc6a` | 6089 | 117 | YES | <title>N.H — Combined Icon Style</title> | Combined icon prototype. | Prototype (HTML) | G-ICON | - | Prototype |
| 94 | `nh_ingest_chatgpt__1_.py` | upload directory | B7 | `b8af9f1d36d93d73bb43daf60786aaa0e36e0313aa85c50b8812d04dd4cb3201` | 5128 | 148 | YES | nh_ingest_chatgpt.py — clean ingest of ChatGPT-export JSON into the accretive store. | Clean ChatGPT-export ingest; role carried, not guessed; DRY_RUN default. | Code (ingest pipeline) | G-NHINGEST | - | Code |
| 95 | `nh_log.py` | upload directory | B6 | `63eaf052295b63b7545cdf44c135a6cdad75d3c57c57d545839f25061b1f8d5e` | 17941 | 481 | YES | nh_log.py - the read-only HTML log / "mirror" of the accretive store (N.H §7B Part 7) | Read-only HTML log/"mirror" generator (§7B Part 7). | Code (read-only tool) | G-NHLOG | - | Code |
| 96 | `nh_probe.py` | upload directory | B6 | `2dc08d4e89688b529f468f06348db10e31fcefad1ae0a4dbd5aa5092c18ec6f3` | 7234 | 188 | YES | nh_probe.py - read-only boundary-signal probe for the accretive store (N.H §11 item 2b) | Read-only boundary-signal probe over the store. | Code (read-only tool) | G-NHPROBE | - | Code |
| 97 | `nh_probe_truth.py` | upload directory | B6 | `8716a5014c1fbe4215a888e1f4b8249755c2e8f4a9bf23f5c06be764327ce9b9` | 8301 | 213 | YES | nh_probe_truth.py - GROUND-TRUTH speaker probe for gpt_purified (N.H §11 item 2b) | Ground-truth speaker probe (reads gpt_purified_history.txt). | Code (read-only tool) | G-NHPROBET | - | Code |
| 98 | `nh_research_architecture_explained.md` | upload directory | B4 | `d19a3c22091441a65d23f9d3285adf3ed91bf0d98ec3473714444679f5998a06` | 10089 | 176 | YES | # N.H Research Pipeline — Full Breakdown (Old vs New) | Research architecture explainer. | Explainer | G-RESEARCHARCH | - | Design source |
| 99 | `nh_research_architecture_explained__1_.md` | upload directory | B4 | `d19a3c22091441a65d23f9d3285adf3ed91bf0d98ec3473714444679f5998a06` | 10089 | 176 | YES | # N.H Research Pipeline — Full Breakdown (Old vs New) | Research architecture explainer. | Explainer | G-RESEARCHARCH | - | Design source |
| 100 | `nh_search_pipeline_security_decisions.md` | upload directory | B1 | `0550cea1aaca73b681cdb1293c2e1903a6c754c75241a8f663435400022b82a2` | 4506 | 38 | YES | # N.H Search Pipeline — Security & Source Decisions | Search-pipeline security decisions. | Security decisions | G-SEARCHSEC | - | Design source |

**Loose resident rows: 100.**

### 2A.2 — Archive-member source records (inside `files__3_.zip`)

Each is byte-identical to a loose copy; recorded separately as an archive member. NOT counted as an additional upload attachment beyond the single ZIP upload (B7).

| # | Archive-member Filename | Source | SHA-256 (64 hex) | Bytes | Lines | Read | Literal first heading | Description | Declared status | Dup-group | Related-version family | Authority | Exact relationship to loose copy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `NH_DECISION_DEFAULTS-S10.1.md` | archive member inside files__3_.zip | `b018ae48f8863c223a2a345c7747877722e1c6b108bab754c78c9182e774968c` | 10874 | 88 | YES | # N.H — DECISION DEFAULTS | S10.1 Decision Defaults (matches MASTER-11.1): 2a two-file structure; Helper-not-Decider. | Decision Defaults, historical | G-DDS101 | Decision Defaults lineage | Historical companion | Byte-identical (same SHA-256) to loose `NH_DECISION_DEFAULTS-S10_1.md` (B7). The loose file uses an underscore (`S10_1`); the archive member uses a dot (`S10.1`). Same content; the dot/underscore filename difference is a packaging artifact. |
| 2 | `NH_MASTER-11.1.md` | archive member inside files__3_.zip | `7270cc48fd9af8afb2b0cb3157cb0549107a3467fa94172afe239367c6e7448c` | 80040 | 482 | YES | # N.H — MASTER (complete, self-contained, full depth) | MASTER-11.1 (session 10 eve): 2a reading-record shape; six-part STORY-layer; DUMB/SMART frame (§0A). | Self-contained Master, candidate | G-MASTER111 | MASTER lineage | Historical Master | Byte-identical (same SHA-256) to loose `NH_MASTER-11_1.md` (B7). The loose file uses an underscore (`11_1`); the archive member uses a dot (`11.1`). Same content; the dot/underscore filename difference is a packaging artifact. |

**Archive-member rows: 2.**  **Total Ledger A rows: 102.**

---

## 3. UPLOAD OCCURRENCE LEDGER (B) — one row per attachment occurrence

Rebuilt from the literal `<file_path>` lists in each batch message, including within-message and cross-batch repeats. Each row carries **that occurrence's historical hash**: where an earlier upload's body was later overwritten on disk, the original hash is used and the row is marked HISTORICAL.

**Batch 3 caveat (occ #41–45):** the Batch 3 total of 16 paths and its 11 distinct-new files are VERIFIED, but the exact identity of the 5 repeat occurrences is **UNVERIFIED** — the original Batch 3 `<uploaded_files>` block is not preserved in the available records, and the Batch 3 receipt is internally contradictory (its prose says "four paths" while it lists five MASTER-17 filenames, and it separately states the wellbeing path appeared twice). The 5 repeat rows below show the best-evidence candidates (the five MASTER-17 re-uploads) but are flagged UNVERIFIED. See the Batch 3 evidence and contradiction appendix in §11.

| Occ # | Batch | Exact Filename | SHA-256 of THIS occurrence (64 hex) | Note |
|---|---|---|---|---|
| 1 | B1 | `NH_MASTER-17_00_INDEX_STATUS.md` | `b7c794561d102eb682f219937c0c5b1551b338ed76a902e43d32101649fb96c9` | - |
| 2 | B1 | `NH_MASTER-17_01_FOUNDATION_BUILT.md` | `da261935d739e30e8c8a2f4cdcdcbce47c29948511ad2fb7f9f48a6d52b9a008` | - |
| 3 | B1 | `NH_MASTER-17_02_CONCEPTUAL_ARCHITECTURE.md` | `186717c1ba60f60c1a511231820d6d45805161966f93d8c26cbeeb8c5c24d341` | - |
| 4 | B1 | `NH_MASTER-17_03_ROADMAP_INTERFACE_HISTORY.md` | `0a64a524d7325e5408fe591080ddec93bca2c9ae98ff4557cece6379dd53d5a9` | - |
| 5 | B1 | `NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md` | `cfdaefe9b0b6c134a911f102ae6479fb845662165a1cf216aec465ff816ce152` | - |
| 6 | B1 | `NH_MASTER-19_CORRECTED_v3.md` | `e38c37e97491d7f13310fb9d5d961e86111aad9c917612ccb3ea12e27e127a7b` | - |
| 7 | B1 | `NH_MASTER_CONTEXT.md` | `e6ae68b37a375d90ea04d6000e311cca7d4199c715e51bd6873f99d8f169f099` | - |
| 8 | B1 | `NH_Meaning_Engine_Design.md` | `18185908fecd4a2a00587a57fc10437f5e5a6003731ec61d4d7f39e37dcf0d62` | HISTORICAL OCCURRENCE — BODY NO LONGER RESIDENT (12474 B / 137 lines) |
| 9 | B1 | `NH_Mobile_App_Design_Spec.md` | `023c82babd4231d0b6fc8235396454e4d07e06d9a769797a4a31c9867885812c` | - |
| 10 | B1 | `NH_Universal_Filter_Design__1_.md` | `7dce7058c991dc1aeb583e7455234a6721c7fea089626fcccecf529f5b48b1c7` | - |
| 11 | B1 | `NH_chat_frontdoor_design_sketch.md` | `757b6dd889aedf4af840ecfa190e0404c79ccf609d37607a105dca85f0af0112` | - |
| 12 | B1 | `NH_honest_calibration_note.md` | `4096cc357b1e8cd5d8d3cfc83a688946fa5a3145c9edbe83198d03ad5d28f6ac` | - |
| 13 | B1 | `NH_live_mechanism_picture.svg` | `4a9bd78d4f49bea70954e91aeeb07f46f135c731b994f439d6e8486bea7cb42b` | - |
| 14 | B1 | `NH_wellbeing_baseline_system.md` | `afb1bad3c1edad3e86e76c5a1cb278b1a1e03c750d4fa1af6f54ad804bcc098c` | - |
| 15 | B1 | `nh_search_pipeline_security_decisions.md` | `0550cea1aaca73b681cdb1293c2e1903a6c754c75241a8f663435400022b82a2` | - |
| 16 | B2 | `NH_DECISION_DEFAULTS-S17_AUDITED_v1.md` | `a0df064a0f4dce25825282e67619ff0c3e0319c37916ca463539b4d1390f69fe` | - |
| 17 | B2 | `NH_DECISION_DEFAULTS-S17_AUDITED_v1.md` | `a0df064a0f4dce25825282e67619ff0c3e0319c37916ca463539b4d1390f69fe` | - |
| 18 | B2 | `NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md` | `cfdaefe9b0b6c134a911f102ae6479fb845662165a1cf216aec465ff816ce152` | - |
| 19 | B2 | `NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md` | `cfdaefe9b0b6c134a911f102ae6479fb845662165a1cf216aec465ff816ce152` | - |
| 20 | B2 | `NH_MASTER-18_FULL_DRAFT_v1.md` | `2f63734c600f4f8ea212b15c99c81f0a00a415dd525afb7d5176168c9edb5397` | - |
| 21 | B2 | `NH_MASTER-18_FULL_DRAFT_v1.md` | `2f63734c600f4f8ea212b15c99c81f0a00a415dd525afb7d5176168c9edb5397` | - |
| 22 | B2 | `NH_MASTER-19_CORRECTED_v1.md` | `0287015be938212d8065e5f2d3ac9b952a1f8943a043864ef63614d1670beffb` | - |
| 23 | B2 | `NH_MASTER-19_CORRECTED_v1.md` | `0287015be938212d8065e5f2d3ac9b952a1f8943a043864ef63614d1670beffb` | - |
| 24 | B2 | `NH_MASTER-19_FULL.md` | `bc498fda2fea592fbb08fd7d1b1ded23f13d8522bfb1f2dc324095df5259caec` | - |
| 25 | B2 | `NH_MASTER-19_FULL.md` | `bc498fda2fea592fbb08fd7d1b1ded23f13d8522bfb1f2dc324095df5259caec` | - |
| 26 | B2 | `NH_RECENT_CONTINUITY_NOTE_POST_MASTER17-3.md` | `7d614546710c9aa66ff02f87449fe30505cb5a0d6d929462a4e719a71fe082e3` | - |
| 27 | B2 | `NH_RECENT_CONTINUITY_NOTE_POST_MASTER17-3.md` | `7d614546710c9aa66ff02f87449fe30505cb5a0d6d929462a4e719a71fe082e3` | - |
| 28 | B2 | `NH_WORKING_ROLES.md` | `a0281060abd7e7da791bb56a97316ab9ec41ab88fdd7884fac4c6434fa487619` | - |
| 29 | B2 | `NH_WORKING_ROLES.md` | `a0281060abd7e7da791bb56a97316ab9ec41ab88fdd7884fac4c6434fa487619` | - |
| 30 | B3 | `NH_MASTER-19_CORRECTED_v6__1_.md` | `8165f4bed94d2d57140d49e93d3c85b8e2b259053e0b30ac4c675fa7463a1bf9` | - |
| 31 | B3 | `NH_MASTER-19_CORRECTED_v7_1__1_.md` | `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf` | - |
| 32 | B3 | `cursorrules__1_` | `5050d08825b93acd72a79d07946e43c8cbe537e079517ccfe66bcae8e30e96e9` | - |
| 33 | B3 | `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM__1_.md` | `fb36bf8e55026ed7d79e4a5264be17f2577dda3276c4b2d2dc320018931f16f5` | - |
| 34 | B3 | `NH_ACCEPTED_TSC_DESIGN_v1__1_.md` | `1da2e296d4345d11dcec5f197aa9a42883349526275c5aa32b0bb07d1ca44658` | - |
| 35 | B3 | `NH_DECISION_DEFAULTS-S19_v1__1___1_.md` | `ecea9224163681f9fc1d29327b0453c5e7ead42fd178786ab9dc6a6d4e1baaa6` | - |
| 36 | B3 | `NH_DECISION_DEFAULTS-S19_v2_2__1_.md` | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` | - |
| 37 | B3 | `NH_SHARED_CHAT_HANDOFF_BEFORE_CONSOLIDATION_v1__1_.md` | `47e6a8ba71fa7e90e8bb8ba671cad22291c950c2770d78e82eea6d331ca7d865` | - |
| 38 | B3 | `NH_wellbeing_baseline_system__1_.md` | `afb1bad3c1edad3e86e76c5a1cb278b1a1e03c750d4fa1af6f54ad804bcc098c` | - |
| 39 | B3 | `NH_WORKING_ROLES__2_.md` | `a0281060abd7e7da791bb56a97316ab9ec41ab88fdd7884fac4c6434fa487619` | - |
| 40 | B3 | `NH_CHAT_HANDOFF_AFTER_BGMM__1_.md` | `f524f7cdd4dd2f1b897177e0e7f0843d1c8a7767341e4a010da9ab066414a562` | - |
| 41 | B3 | `NH_MASTER-17_00_INDEX_STATUS.md` | `b7c794561d102eb682f219937c0c5b1551b338ed76a902e43d32101649fb96c9` | UNVERIFIED — B3 repeat identity (see §11) |
| 42 | B3 | `NH_MASTER-17_01_FOUNDATION_BUILT.md` | `da261935d739e30e8c8a2f4cdcdcbce47c29948511ad2fb7f9f48a6d52b9a008` | UNVERIFIED — B3 repeat identity (see §11) |
| 43 | B3 | `NH_MASTER-17_02_CONCEPTUAL_ARCHITECTURE.md` | `186717c1ba60f60c1a511231820d6d45805161966f93d8c26cbeeb8c5c24d341` | UNVERIFIED — B3 repeat identity (see §11) |
| 44 | B3 | `NH_MASTER-17_03_ROADMAP_INTERFACE_HISTORY.md` | `0a64a524d7325e5408fe591080ddec93bca2c9ae98ff4557cece6379dd53d5a9` | UNVERIFIED — B3 repeat identity (see §11) |
| 45 | B3 | `NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md` | `cfdaefe9b0b6c134a911f102ae6479fb845662165a1cf216aec465ff816ce152` | UNVERIFIED — B3 repeat identity (see §11) |
| 46 | B4 | `N_H__Personal_AI__Sovereignty-First_Architecture_with_Mandatory_REALITY_SIMULATION_Gate_Surveyed_Against_the_Field.pdf` | `ba98f5c9e2f073aacbb4999363d0a2e44fd9d90149665b49ee42d07c49eaf19a` | - |
| 47 | B4 | `N_H__Personal_AI__Sovereignty-First_Architecture_with_Mandatory_REALITY_SIMULATION_Gate_Surveyed_Against_the_Field__1_.pdf` | `ba98f5c9e2f073aacbb4999363d0a2e44fd9d90149665b49ee42d07c49eaf19a` | - |
| 48 | B4 | `NH_MASTER_FILE_COMPLETE.md` | `80a6143e9857ee77e9cf75ebd1c55724938f23bd04aae8b9b761160171bfcd02` | - |
| 49 | B4 | `NH_MASTER_FILE_COMPLETE__1_.md` | `06f69672fa89800f060c70864bf1fd87532aff4359f3e538c48b087f08d8daed` | - |
| 50 | B4 | `nh_icon_combined.html` | `6e194dfdd6c876e5b033cde9696e7b5ab11e8370268410e237b1e863bf90bc6a` | - |
| 51 | B4 | `NH_Canvas_Design_Spec.md` | `20444814d0ac1cf5ff49a927862b0025c9c069760e425999dbff7a2893e1d5b5` | - |
| 52 | B4 | `NH_risk_review_and_openrouter.md` | `3864a2eb1a8f97bf433bd7ebaf0a9d4d85ba6e09bbd26c9c39d1371d5fe6d598` | - |
| 53 | B4 | `NH_risk_review_and_openrouter__1_.md` | `6fa53662b406edb1b410d56bb43560027fb7a7d6f9042db5233a6b5f60f710c7` | - |
| 54 | B4 | `nh_research_architecture_explained.md` | `d19a3c22091441a65d23f9d3285adf3ed91bf0d98ec3473714444679f5998a06` | - |
| 55 | B4 | `nh_research_architecture_explained__1_.md` | `d19a3c22091441a65d23f9d3285adf3ed91bf0d98ec3473714444679f5998a06` | - |
| 56 | B4 | `NH_Universal_Filter_Design.md` | `3df666eb4ff4d90e5a5a299f7f7d52361638a27feb1e727894f0e0658c421020` | - |
| 57 | B4 | `NH_Universal_Filter_Design__1_.md` | `7dce7058c991dc1aeb583e7455234a6721c7fea089626fcccecf529f5b48b1c7` | - |
| 58 | B4 | `NH_Universal_Filter_Design__2_.md` | `c8938d370efdd072912cabb4adf844dba4cc581095d68fca7022cff30710be15` | - |
| 59 | B5 | `NH_MASTER-5.md` | `f91fdf682bac232b468c95ac99b8af4e0e385afe5e532108bdd2721026d0692c` | - |
| 60 | B5 | `NH_MASTER_FILE_COMPLETE__2_.md` | `06f69672fa89800f060c70864bf1fd87532aff4359f3e538c48b087f08d8daed` | - |
| 61 | B5 | `NH_MASTER_FILE_COMPLETE__1_.md` | `06f69672fa89800f060c70864bf1fd87532aff4359f3e538c48b087f08d8daed` | - |
| 62 | B5 | `NH_MASTER-8.md` | `13675a34e039d726cd845bde8a7177e1f260dadb3a19b9b6ba4c7b2c87bde48a` | - |
| 63 | B5 | `NH_MASTER-7.md` | `6868507ca073051860daadf80554e5e064b8d3d1b293427d28fede746ba135c4` | - |
| 64 | B5 | `NH_MASTER-6__1_.md` | `3e978e036871c1188400409bfa439380f5cce02e2afd4bbb2830d85b15fe7633` | - |
| 65 | B5 | `NH_MASTER-6.md` | `63a64d0895e5ee4cebfc9b8a2399356afe1c505ecdf04ca8ee45f2d6079948cc` | - |
| 66 | B5 | `NH_MASTER-9_2__1_.md` | `052731353b4a221d358133219c5c280aa2e4ada98a1445657aec17b6ce13107e` | - |
| 67 | B5 | `NH_MASTER-9_2.md` | `052731353b4a221d358133219c5c280aa2e4ada98a1445657aec17b6ce13107e` | - |
| 68 | B5 | `NH_MASTER-9.md` | `e6bf27a4d4c81ba7e9e9351014397c7668fb1a114f2aa32d6babbaccaae7a813` | - |
| 69 | B5 | `NH_Build_Checklist.md` | `e4d1436a3e5655ce4b09135c65424a2a672157731441f48f954044aa5d1aea40` | - |
| 70 | B5 | `NH_Meaning_Engine_Design.md` | `15c2786003463fff73b22dd4bf49cf36df3da30ed27ef57e78663605d2e59a89` | - |
| 71 | B5 | `NH_Universal_Filter_RULES.md` | `c0fb4528a332f4014782afacee63d167407e31cc88b1502ec8783900588b3a37` | - |
| 72 | B5 | `nh_architecture_canvas.html` | `971833b6c4b3c6f1c57c094d40d0e3a9b27254087832d29ae46d3338cad90cf2` | - |
| 73 | B5 | `NH_DECISION_DEFAULTS_ADD__1_.md` | `32b1172159b60afe231f29e132c6c7a39c7eaaf2faf8ced9ec7c7ed473e52bab` | - |
| 74 | B5 | `NH_DECISION_DEFAULTS_ADD.md` | `32b1172159b60afe231f29e132c6c7a39c7eaaf2faf8ced9ec7c7ed473e52bab` | - |
| 75 | B5 | `NH_MASTER_section13_ADD.md` | `91d82ed52bcbf497fc12a5c61d479ab5f8fb83f9fc341f878165c446238d68b9` | - |
| 76 | B5 | `NH_DECISION_DEFAULTS.md` | `2abb2e4570f77a63ef087cfa2fc10cb08210cadb01e9bd304d84d2555249b047` | - |
| 77 | B5 | `NH_DECISION_DEFAULTS__1_.md` | `45ec88c440456ce7aa99babe8b58ed088786ed342d5197ab4fef8b69d24d3e29` | - |
| 78 | B6 | `nh_log.py` | `63eaf052295b63b7545cdf44c135a6cdad75d3c57c57d545839f25061b1f8d5e` | - |
| 79 | B6 | `NH_live_mechanism__1_.html` | `a4465293961004e802cfa660e454d3aa2550bf136a94da5a8b7b2fa163fd7071` | - |
| 80 | B6 | `NH_MASTER-9_4.md` | `9bbc28dc31c7825d5f3927169526a23bfd0abff9f5a994ce3dc4fd6f7cf1e8dd` | - |
| 81 | B6 | `NH_live_mechanism.html` | `b329a5e4cf24b8ccbbb13e876da05e5b5542efb8aed2476420e08cbb053d6bb8` | - |
| 82 | B6 | `NH_live_mechanism_picture__1_.svg` | `4a9bd78d4f49bea70954e91aeeb07f46f135c731b994f439d6e8486bea7cb42b` | - |
| 83 | B6 | `NH_live_mechanism_picture.svg` | `4a9bd78d4f49bea70954e91aeeb07f46f135c731b994f439d6e8486bea7cb42b` | - |
| 84 | B6 | `NH_MASTER-9_2__1_.md` | `052731353b4a221d358133219c5c280aa2e4ada98a1445657aec17b6ce13107e` | - |
| 85 | B6 | `NH_MASTER-10__1_.md` | `f9e783601b1816f797bf82c8bebd70745335b6d5b837a62186c6c6ad6659b804` | - |
| 86 | B6 | `NH_MASTER-10.md` | `4ee57d298f11a8ad14ea820f157a4c523d4ed16b8532aa14da9cf418ad6fb7d8` | - |
| 87 | B6 | `NH_MASTER-11.md` | `10771ea4e9cb7a72596efaf0ac52a95d6b7805c215f637ca1e8e3063e050e3ba` | - |
| 88 | B6 | `nh_probe_truth.py` | `8716a5014c1fbe4215a888e1f4b8249755c2e8f4a9bf23f5c06be764327ce9b9` | - |
| 89 | B6 | `nh_probe.py` | `2dc08d4e89688b529f468f06348db10e31fcefad1ae0a4dbd5aa5092c18ec6f3` | - |
| 90 | B6 | `NH_INSIGHT__the_line_under_all_the_lines.md` | `77b5932819a653504cfb1493bf6e9ba94b6c95696a802627cdbdb2589d548ab1` | - |
| 91 | B6 | `NH_chat_frontdoor_design_sketch__1_.md` | `757b6dd889aedf4af840ecfa190e0404c79ccf609d37607a105dca85f0af0112` | - |
| 92 | B6 | `NH_chat_frontdoor_design_sketch.md` | `757b6dd889aedf4af840ecfa190e0404c79ccf609d37607a105dca85f0af0112` | - |
| 93 | B6 | `NH_DECISION_DEFAULTS__1_.md` | `45ec88c440456ce7aa99babe8b58ed088786ed342d5197ab4fef8b69d24d3e29` | - |
| 94 | B6 | `NH_DECISION_DEFAULTS_ADD__1_.md` | `32b1172159b60afe231f29e132c6c7a39c7eaaf2faf8ced9ec7c7ed473e52bab` | - |
| 95 | B6 | `NH_DECISION_DEFAULTS_ADD.md` | `32b1172159b60afe231f29e132c6c7a39c7eaaf2faf8ced9ec7c7ed473e52bab` | - |
| 96 | B6 | `NH_MASTER_section13_ADD.md` | `91d82ed52bcbf497fc12a5c61d479ab5f8fb83f9fc341f878165c446238d68b9` | - |
| 97 | B6 | `NH_DECISION_DEFAULTS__2_.md` | `11f71f447c17ea48a269adf9c206aa8f23d88a1207ae7388fafb6d9a94004bdc` | - |
| 98 | B7 | `NH_MASTER-14__4_.md` | `ea4bcbdde17cd2bf802e37259565803ac32ecb9e4ff9120b1a7da579d69bb5ee` | - |
| 99 | B7 | `NH_MASTER-14__3_.md` | `1dec9fe0cc4fccea1a8951441ca3f6a81b54784712a3ed2da7fb0b56a1e07fd6` | - |
| 100 | B7 | `NH_MASTER-14__2_.md` | `f9dd9d957d459cb3abb32071338032a0d62c2c9434dce75d68e86ccbbfbbfbb3` | - |
| 101 | B7 | `NH_MASTER-14__1_.md` | `9a3f2b1eaa63b22c32734252a66d30e0b098ed9dac5686a5952562b43fb10766` | - |
| 102 | B7 | `NH_MASTER-14.md` | `493f50b8f85516e19b7b566f9603c0b5ce45c36f7a6c4a820a8b3d4a2ae10be4` | - |
| 103 | B7 | `NH_MASTER-13__1_.md` | `e2c0f9152349e38331c529417ac0638cdd707b09ad6e9f39a69b4aaf3ef8c2ae` | - |
| 104 | B7 | `NH_MASTER-13.md` | `e2c0f9152349e38331c529417ac0638cdd707b09ad6e9f39a69b4aaf3ef8c2ae` | - |
| 105 | B7 | `NH_MASTER-11_1.md` | `7270cc48fd9af8afb2b0cb3157cb0549107a3467fa94172afe239367c6e7448c` | - |
| 106 | B7 | `files__3_.zip` | `a32e34c91ebb986e4fa1ba12bc6397bcdda91266b87f3427aa0e6e08c9543291` | - |
| 107 | B7 | `NH_DECISION_DEFAULTS-S13__3_.md` | `f6358c44db6e115309e2b1d25a818fe2f02d86a79cea6fefa9daa31bfeead4f1` | - |
| 108 | B7 | `NH_DECISION_DEFAULTS-S13__2_.md` | `0ff6dd4ce29b7001596db5dd4862fa66d976efe64430653850a735db06f9e2f0` | - |
| 109 | B7 | `NH_MASTER-14_FINAL.md` | `6dc26159e1862ec96d749581567f74d285490dd515775b77b6fbd7cb53e6f5c3` | - |
| 110 | B7 | `NH_DECISION_DEFAULTS-S13__1_.md` | `0ff6dd4ce29b7001596db5dd4862fa66d976efe64430653850a735db06f9e2f0` | - |
| 111 | B7 | `NH_DECISION_DEFAULTS-S13.md` | `eaea2e2ccb3118d50a44d06bda5f12f94bb436ea1cde5411b98370334cd9644a` | - |
| 112 | B7 | `NH_DECISION_DEFAULTS-S12.md` | `da329e8652ba0f35a4b2d864ade986ca7c61c1324240d84804ffc808c944cfa8` | - |
| 113 | B7 | `nh_ingest_chatgpt__1_.py` | `b8af9f1d36d93d73bb43daf60786aaa0e36e0313aa85c50b8812d04dd4cb3201` | - |
| 114 | B7 | `NH_DECISION_DEFAULTS-S10_1.md` | `b018ae48f8863c223a2a345c7747877722e1c6b108bab754c78c9182e774968c` | - |
| 115 | B7 | `nh_2a_prototype.html` | `b3abcbb47273fefdbcc61f07cbeccc7b0945f981ff770121fbb174271a05f164` | - |
| 116 | B8 | `NH_DECISION_DEFAULTS-S13__6_.md` | `8acc713871d9c9160143014ebd5823df61df7082fd37ed27e3d20c4b4314f86d` | - |
| 117 | B8 | `NH_MASTER-14_FINAL__4_.md` | `f632babe53640419ebcd2237d35d5d59cab393531f15a5ac0d18d28e8efba11a` | - |
| 118 | B8 | `NH_DECISION_DEFAULTS-S13__4_.md` | `8acc713871d9c9160143014ebd5823df61df7082fd37ed27e3d20c4b4314f86d` | - |
| 119 | B8 | `NH_MASTER-14_FINAL__3_.md` | `55fab7e730cb1f4b320b02411fbca954fc15259d7f13574b661af5d77c3fd720` | - |
| 120 | B8 | `NH_MASTER-14_FINAL__2_.md` | `55fab7e730cb1f4b320b02411fbca954fc15259d7f13574b661af5d77c3fd720` | - |
| 121 | B8 | `NH_MASTER-14_FINAL__1_.md` | `6dc26159e1862ec96d749581567f74d285490dd515775b77b6fbd7cb53e6f5c3` | - |
| 122 | B8 | `NH_DECISION_DEFAULTS-S13__3_.md` | `f6358c44db6e115309e2b1d25a818fe2f02d86a79cea6fefa9daa31bfeead4f1` | - |
| 123 | B8 | `NH_DECISION_DEFAULTS-S13__2_.md` | `0ff6dd4ce29b7001596db5dd4862fa66d976efe64430653850a735db06f9e2f0` | - |
| 124 | B8 | `NH_MASTER-14_FINAL.md` | `6dc26159e1862ec96d749581567f74d285490dd515775b77b6fbd7cb53e6f5c3` | - |
| 125 | B8 | `NH_DECISION_DEFAULTS-S13__1_.md` | `0ff6dd4ce29b7001596db5dd4862fa66d976efe64430653850a735db06f9e2f0` | - |
| 126 | B8 | `NH_DECISION_DEFAULTS-S13.md` | `eaea2e2ccb3118d50a44d06bda5f12f94bb436ea1cde5411b98370334cd9644a` | - |
| 127 | B8 | `NH_MASTER-14__4_.md` | `ea4bcbdde17cd2bf802e37259565803ac32ecb9e4ff9120b1a7da579d69bb5ee` | - |
| 128 | B8 | `NH_MASTER-14__3_.md` | `1dec9fe0cc4fccea1a8951441ca3f6a81b54784712a3ed2da7fb0b56a1e07fd6` | - |
| 129 | B8 | `NH_MASTER-14__2_.md` | `f9dd9d957d459cb3abb32071338032a0d62c2c9434dce75d68e86ccbbfbbfbb3` | - |
| 130 | B8 | `NH_MASTER-14__1_.md` | `9a3f2b1eaa63b22c32734252a66d30e0b098ed9dac5686a5952562b43fb10766` | - |
| 131 | B8 | `NH_MASTER-14.md` | `493f50b8f85516e19b7b566f9603c0b5ce45c36f7a6c4a820a8b3d4a2ae10be4` | - |
| 132 | B8 | `NH_MASTER-13__1_.md` | `e2c0f9152349e38331c529417ac0638cdd707b09ad6e9f39a69b4aaf3ef8c2ae` | - |
| 133 | B8 | `NH_DECISION_DEFAULTS-S12.md` | `da329e8652ba0f35a4b2d864ade986ca7c61c1324240d84804ffc808c944cfa8` | - |
| 134 | B8 | `NH_DECISION_DEFAULTS-S12.md` | `da329e8652ba0f35a4b2d864ade986ca7c61c1324240d84804ffc808c944cfa8` | - |
| 135 | B9 | `NH_DECISION_DEFAULTS-S13__6_.md` | `8acc713871d9c9160143014ebd5823df61df7082fd37ed27e3d20c4b4314f86d` | - |
| 136 | B9 | `NH_MASTER-14_FINAL__4_.md` | `f632babe53640419ebcd2237d35d5d59cab393531f15a5ac0d18d28e8efba11a` | - |
| 137 | B9 | `NH_DECISION_DEFAULTS-S13__4_.md` | `8acc713871d9c9160143014ebd5823df61df7082fd37ed27e3d20c4b4314f86d` | - |
| 138 | B9 | `NH_MASTER-14_FINAL__3_.md` | `55fab7e730cb1f4b320b02411fbca954fc15259d7f13574b661af5d77c3fd720` | - |
| 139 | B9 | `NH_MASTER-14_FINAL__2_.md` | `55fab7e730cb1f4b320b02411fbca954fc15259d7f13574b661af5d77c3fd720` | - |
| 140 | B9 | `NH_MASTER-14_FINAL__1_.md` | `6dc26159e1862ec96d749581567f74d285490dd515775b77b6fbd7cb53e6f5c3` | - |
| 141 | B9 | `NH_DECISION_DEFAULTS-S13__3_.md` | `f6358c44db6e115309e2b1d25a818fe2f02d86a79cea6fefa9daa31bfeead4f1` | - |
| 142 | B9 | `NH_DECISION_DEFAULTS-S13__2_.md` | `0ff6dd4ce29b7001596db5dd4862fa66d976efe64430653850a735db06f9e2f0` | - |
| 143 | B9 | `NH_MASTER-14_FINAL.md` | `6dc26159e1862ec96d749581567f74d285490dd515775b77b6fbd7cb53e6f5c3` | - |
| 144 | B9 | `NH_DECISION_DEFAULTS-S13__1_.md` | `0ff6dd4ce29b7001596db5dd4862fa66d976efe64430653850a735db06f9e2f0` | - |
| 145 | B9 | `NH_DECISION_DEFAULTS-S13.md` | `eaea2e2ccb3118d50a44d06bda5f12f94bb436ea1cde5411b98370334cd9644a` | - |
| 146 | B9 | `NH_MASTER-14__4_.md` | `ea4bcbdde17cd2bf802e37259565803ac32ecb9e4ff9120b1a7da579d69bb5ee` | - |
| 147 | B9 | `NH_MASTER-14__3_.md` | `1dec9fe0cc4fccea1a8951441ca3f6a81b54784712a3ed2da7fb0b56a1e07fd6` | - |
| 148 | B9 | `NH_MASTER-14__2_.md` | `f9dd9d957d459cb3abb32071338032a0d62c2c9434dce75d68e86ccbbfbbfbb3` | - |
| 149 | B9 | `NH_MASTER-14__1_.md` | `9a3f2b1eaa63b22c32734252a66d30e0b098ed9dac5686a5952562b43fb10766` | - |
| 150 | B9 | `NH_MASTER-14.md` | `493f50b8f85516e19b7b566f9603c0b5ce45c36f7a6c4a820a8b3d4a2ae10be4` | - |
| 151 | B9 | `NH_DELTA_S14.md` | `f94b5351e56242ce4f1797b417cd482bd25ec5549c73491d218fbdbffa92af9f` | - |
| 152 | B9 | `NH_CURSOR_BRIEF_reading_validator.md` | `d80065191b04f26d3b0834cd1e861fda68a28d6c61f80d2bd458fce37ac70ba9` | - |
| 153 | B9 | `NH_DELTA_S14.md` | `f94b5351e56242ce4f1797b417cd482bd25ec5549c73491d218fbdbffa92af9f` | - |
| 154 | B9 | `NH_CURSOR_BRIEF_reading_validator.md` | `d80065191b04f26d3b0834cd1e861fda68a28d6c61f80d2bd458fce37ac70ba9` | - |

**Upload Occurrence Ledger rows: 154.**

Per-batch reconciliation: B1=15 · B2=14 · B3=16 · B4=13 · B5=19 · B6=20 · B7=18 · B8=19 · B9=20 → **154 total**.

---

## 4. HISTORICAL-OCCURRENCE / OVERWRITTEN-BODY RECORD

Same-filename uploads whose body changed between batches (later upload overwrote the earlier on the deduplicated filesystem). Both bodies are preserved in the record; the historical body is no longer resident.

| Filename | Earlier occurrence | Earlier hash (64 hex) | Earlier size | Later/resident occurrence | Later/resident hash (64 hex) | Later size | Resident now |
|---|---|---|---|---|---|---|---|
| `NH_Meaning_Engine_Design.md` | B1 | `18185908fecd4a2a00587a57fc10437f5e5a6003731ec61d4d7f39e37dcf0d62` | 12,474 B / 137 lines | B5 | `15c2786003463fff73b22dd4bf49cf36df3da30ed27ef57e78663605d2e59a89` | 12,479 B / 138 lines | B5 body (HISTORICAL B1 body no longer resident) |

**Check for other same-filename hash changes between batches:** every other filename re-uploaded across batches was verified to carry an identical hash on each upload (e.g. `NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md` B1=B2=B3, `NH_wellbeing_baseline_system*` B1=B3/B4, `NH_chat_frontdoor_design_sketch*` B1=B6, the MASTER-14 / DD-S13 families across B7/B8/B9). **`NH_Meaning_Engine_Design.md` is the ONLY same-filename body that changed between batches.**

---

## 5. PROJECT KNOWLEDGE SOURCE LEDGER (counted separately from uploads)

Full metadata for every Project Knowledge file. NOT part of the Batch 1–9 upload counts.

| # | Exact Filename | Source | SHA-256 (64 hex) | Bytes | Lines | Read | Literal first heading | Description | Declared status | Dup-group | Related-version family | Authority |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `NH_DECISION_DEFAULTS-S19_v2_2.md` | Project Knowledge | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` | 37048 | 314 | YES | # N.H — DECISION DEFAULTS (S19) | ADOPTED AUTHORITATIVE Defaults; byte-identical to uploaded `NH_DECISION_DEFAULTS-S19_v2_2__1_.md` (B3). | ADOPTED AUTHORITATIVE | G-DDS19V22 | Decision Defaults lineage | ADOPTED AUTHORITATIVE (explicit) |
| 2 | `NH_MASTER-19_CORRECTED_v7_1.md` | Project Knowledge | `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf` | 291811 | 1937 | YES | # N.H — MASTER-19: Full Backup with All Additions | ADOPTED AUTHORITATIVE Master; byte-identical to uploaded `NH_MASTER-19_CORRECTED_v7_1__1_.md` (B3). | ADOPTED AUTHORITATIVE | G-M19V71 | MASTER-19 lineage | ADOPTED AUTHORITATIVE (explicit) |
| 3 | `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Project Knowledge | `cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb` | 465376 | 5580 | YES | # N.H PROJECT COMPANION — GOVERNANCE, ACCEPTED DESIGNS, AND ARCHIVE | Project companion governance/archive file. NOT part of the Batch 1–9 upload set; inventoried here directly. Not present among uploads. | Project companion (governance/archive) | G-PKGOV | - | Project companion (not an upload) |
| 4 | `cursorrules__1_` | Project Knowledge | `5050d08825b93acd72a79d07946e43c8cbe537e079517ccfe66bcae8e30e96e9` | 34821 | 717 | YES | # N.H System — Cursor Rules v3.2 | In-force code ruleset (.cursorrules v3.2); byte-identical to uploaded `cursorrules__1_` (B3). | ADOPTED AUTHORITATIVE (code ruleset) | G-CURSORRULES | - | ADOPTED AUTHORITATIVE (explicit) |

**Project Knowledge rows: 4.**

---

## 6. KNOWN ESSENTIAL SOURCES REQUIRING SUPPLEMENTAL INTAKE

Named candidate/recovery sources NOT physically present (uploads or Project Knowledge). Hashes UNKNOWN — not invented.

| Filename | Class | Hash | Present? | Authority note |
|---|---|---|---|---|
| `NH_MASTER-19_CORRECTED_v8.md` | Candidate / recovery | UNKNOWN — not supplied | No | Candidate only; v7_1 remains adopted unless Ness adopts v8. |
| `NH_DECISION_DEFAULTS-S19_v2_3.md` | Candidate / recovery | UNKNOWN — not supplied | No | Candidate only; v2_2 remains adopted unless Ness adopts v2_3. |
| `cursorrules_v3_3` | Candidate / recovery | UNKNOWN — not supplied | No | Candidate; resident `cursorrules__1_` (v3.2) remains current unless Ness adopts v3_3. |

**Present authority state (unchanged):** Master **v7_1** adopted; Decision Defaults **v2_2** adopted. **v8 / v2_3 / cursorrules_v3_3** remain candidates pending explicit adoption by Ness.

---

## 6B. REFERENCED-BUT-NOT-SUPPLIED SOURCES (named inside supplied files; never provided)

Carried forward so nothing disappears. Hashes UNKNOWN — not invented.

**Ingest sources / stores:** `gpt_purified_history.txt`; `cleaned_history (1).txt` (declared damaged/not ingested); `conversations-000.json`; `conversations-001.json`; `conversations-002.json`; `nh_accretive_store.py`; `.nh_accretive_store.jsonl` / `.nh_roots.sealed` / `.nh_readings_store.jsonl`; `ingest_seeds.py`.

**Masters referenced but absent:** `NH_MASTER-9.1`, `NH_MASTER-9.3`, `NH_MASTER-12`, `NH_MASTER-15`, `NH_MASTER-16` (and `NH_MASTER-16_FINAL_CORRECTED.md`), `NH_MASTER-17_DRAFT.md`, `NH_MASTER-19_v7`, `NH_MASTER-19_CORRECTED_v2`, `NH_MASTER-19_v4`, `NH_MASTER-19_v5`.

**Decision Defaults absent:** `NH_DECISION_DEFAULTS-S17_DRAFT.md`, `NH_DECISION_DEFAULTS-S19_v2_1.md`.

**Gold sets:** `NH_GOLD_SET_v1.md`, `NH_GOLD_SET_v2_B.md`, `NH_GOLD_SET_CONTEXT_v1.md`.

**Other design / handoff docs:** `NH_INTERFACE_WORLD_DESIGN_LOG.md`, `NH_CHATGPT_PROJECT_HANDOFF_CLAUDE_S17.md`.

**Prototype / output HTML:** `nh_canvas_test.html`, `nh_icon_styles.html`, `nh_log.html`.

**Other runtime code named in files:** `nh_sovereignty_sync.py`, `nh_service.py`, `nh_peek.py`, `nh_clinical_report.py`, `nh_lawyer_simulator.py`, `nh_nightly.py`, `nh_vector_memory.py`, `nh_engine_minimal.py`, `nh_engine_b.py`, `nh_baseline_engine.py`, `nh_auth.py`, `test_brave.py`.

---

## 7. EXACT-DUPLICATE GROUPS (loose resident; every filename preserved)

1. `0ff6dd4ce29b7001596db5dd4862fa66d976efe64430653850a735db06f9e2f0` — `NH_DECISION_DEFAULTS-S13__1_.md` ; `NH_DECISION_DEFAULTS-S13__2_.md`
2. `8acc713871d9c9160143014ebd5823df61df7082fd37ed27e3d20c4b4314f86d` — `NH_DECISION_DEFAULTS-S13__4_.md` ; `NH_DECISION_DEFAULTS-S13__6_.md`
3. `32b1172159b60afe231f29e132c6c7a39c7eaaf2faf8ced9ec7c7ed473e52bab` — `NH_DECISION_DEFAULTS_ADD.md` ; `NH_DECISION_DEFAULTS_ADD__1_.md`
4. `e2c0f9152349e38331c529417ac0638cdd707b09ad6e9f39a69b4aaf3ef8c2ae` — `NH_MASTER-13.md` ; `NH_MASTER-13__1_.md`
5. `6dc26159e1862ec96d749581567f74d285490dd515775b77b6fbd7cb53e6f5c3` — `NH_MASTER-14_FINAL.md` ; `NH_MASTER-14_FINAL__1_.md`
6. `55fab7e730cb1f4b320b02411fbca954fc15259d7f13574b661af5d77c3fd720` — `NH_MASTER-14_FINAL__2_.md` ; `NH_MASTER-14_FINAL__3_.md`
7. `052731353b4a221d358133219c5c280aa2e4ada98a1445657aec17b6ce13107e` — `NH_MASTER-9_2.md` ; `NH_MASTER-9_2__1_.md`
8. `06f69672fa89800f060c70864bf1fd87532aff4359f3e538c48b087f08d8daed` — `NH_MASTER_FILE_COMPLETE__1_.md` ; `NH_MASTER_FILE_COMPLETE__2_.md`
9. `a0281060abd7e7da791bb56a97316ab9ec41ab88fdd7884fac4c6434fa487619` — `NH_WORKING_ROLES.md` ; `NH_WORKING_ROLES__2_.md`
10. `757b6dd889aedf4af840ecfa190e0404c79ccf609d37607a105dca85f0af0112` — `NH_chat_frontdoor_design_sketch.md` ; `NH_chat_frontdoor_design_sketch__1_.md`
11. `4a9bd78d4f49bea70954e91aeeb07f46f135c731b994f439d6e8486bea7cb42b` — `NH_live_mechanism_picture.svg` ; `NH_live_mechanism_picture__1_.svg`
12. `afb1bad3c1edad3e86e76c5a1cb278b1a1e03c750d4fa1af6f54ad804bcc098c` — `NH_wellbeing_baseline_system.md` ; `NH_wellbeing_baseline_system__1_.md`
13. `ba98f5c9e2f073aacbb4999363d0a2e44fd9d90149665b49ee42d07c49eaf19a` — `N_H__Personal_AI__Sovereignty-First_Architecture_with_Mandatory_REALITY_SIMULATION_Gate_Surveyed_Against_the_Field.pdf` ; `N_H__Personal_AI__Sovereignty-First_Architecture_with_Mandatory_REALITY_SIMULATION_Gate_Surveyed_Against_the_Field__1_.pdf`
14. `d19a3c22091441a65d23f9d3285adf3ed91bf0d98ec3473714444679f5998a06` — `nh_research_architecture_explained.md` ; `nh_research_architecture_explained__1_.md`

**Cross-location archive duplicates:** `NH_MASTER-11.1.md` (zip member) ≡ loose `NH_MASTER-11_1.md` (`7270cc48fd9af8afb2b0cb3157cb0549107a3467fa94172afe239367c6e7448c`); `NH_DECISION_DEFAULTS-S10.1.md` (zip member) ≡ loose `NH_DECISION_DEFAULTS-S10_1.md` (`b018ae48f8863c223a2a345c7747877722e1c6b108bab754c78c9182e774968c`).

---

## 8. RELATED-VERSION (NEAR-DUPLICATE) FAMILIES — flagged; NO WINNER CHOSEN

- **Universal Filter Design (3 tiers):** `3df666eb4ff4d90e5a5a299f7f7d52361638a27feb1e727894f0e0658c421020` (bare) → `7dce7058c991dc1aeb583e7455234a6721c7fea089626fcccecf529f5b48b1c7` (+Keystone) → `c8938d370efdd072912cabb4adf844dba4cc581095d68fca7022cff30710be15` (+Keystone +MEMBRANE).
- **Meaning Engine Design:** B1 body `18185908fecd4a2a00587a57fc10437f5e5a6003731ec61d4d7f39e37dcf0d62` (137L, no longer resident) vs resident B5 body `15c2786003463fff73b22dd4bf49cf36df3da30ed27ef57e78663605d2e59a89` (138L).
- **Risk review:** `3864a2eb1a8f97bf433bd7ebaf0a9d4d85ba6e09bbd26c9c39d1371d5fe6d598` (bare) vs `6fa53662b406edb1b410d56bb43560027fb7a7d6f9042db5233a6b5f60f710c7` (+boot-error resolution).
- **MASTER_FILE_COMPLETE:** `80a6143e9857ee77e9cf75ebd1c55724938f23bd04aae8b9b761160171bfcd02` (156L, heading `# N.H — COMPLETE MASTER FILE`) vs `06f69672fa89800f060c70864bf1fd87532aff4359f3e538c48b087f08d8daed` (257L, heading `# N.H — COMPLETE STANDALONE MASTER FILE`).
- **MASTER-6:** `63a64d0895e5ee4cebfc9b8a2399356afe1c505ecdf04ca8ee45f2d6079948cc` (273L) vs `3e978e036871c1188400409bfa439380f5cce02e2afd4bbb2830d85b15fe7633` (315L).
- **MASTER-9 / 9_2:** `e6bf27a4d4c81ba7e9e9351014397c7668fb1a114f2aa32d6babbaccaae7a813` (442L) vs `052731353b4a221d358133219c5c280aa2e4ada98a1445657aec17b6ce13107e` (513L).
- **MASTER-10:** `4ee57d298f11a8ad14ea820f157a4c523d4ed16b8532aa14da9cf418ad6fb7d8` (406L) vs `f9e783601b1816f797bf82c8bebd70745335b6d5b837a62186c6c6ad6659b804` (407L).
- **MASTER-14 family (5 bodies):** `493f50b8f85516e19b7b566f9603c0b5ce45c36f7a6c4a820a8b3d4a2ae10be4` (340L) · `9a3f2b1eaa63b22c32734252a66d30e0b098ed9dac5686a5952562b43fb10766` (379L) · `f9dd9d957d459cb3abb32071338032a0d62c2c9434dce75d68e86ccbbfbbfbb3` (379L) · `1dec9fe0cc4fccea1a8951441ca3f6a81b54784712a3ed2da7fb0b56a1e07fd6` (389L) · `ea4bcbdde17cd2bf802e37259565803ac32ecb9e4ff9120b1a7da579d69bb5ee` (389L).
- **MASTER-14_FINAL family (3 bodies):** `6dc26159e1862ec96d749581567f74d285490dd515775b77b6fbd7cb53e6f5c3` (427L) · `55fab7e730cb1f4b320b02411fbca954fc15259d7f13574b661af5d77c3fd720` (434L) · `f632babe53640419ebcd2237d35d5d59cab393531f15a5ac0d18d28e8efba11a` (434L).
- **DD-S13 family (4 bodies):** `eaea2e2ccb3118d50a44d06bda5f12f94bb436ea1cde5411b98370334cd9644a` (121L) · `0ff6dd4ce29b7001596db5dd4862fa66d976efe64430653850a735db06f9e2f0` (123L) · `f6358c44db6e115309e2b1d25a818fe2f02d86a79cea6fefa9daa31bfeead4f1` (124L) · `8acc713871d9c9160143014ebd5823df61df7082fd37ed27e3d20c4b4314f86d` (125L).
- **Live-mechanism HTML:** `b329a5e4cf24b8ccbbb13e876da05e5b5542efb8aed2476420e08cbb053d6bb8` (316L) vs `a4465293961004e802cfa660e454d3aa2550bf136a94da5a8b7b2fa163fd7071` (332L).
- **MASTER-19 lineage:** `0287015be938212d8065e5f2d3ac9b952a1f8943a043864ef63614d1670beffb` (v1) → `e38c37e97491d7f13310fb9d5d961e86111aad9c917612ccb3ea12e27e127a7b` (v3) → `8165f4bed94d2d57140d49e93d3c85b8e2b259053e0b30ac4c675fa7463a1bf9` (v6) → `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf` (v7_1), plus `bc498fda2fea592fbb08fd7d1b1ded23f13d8522bfb1f2dc324095df5259caec` (FULL) and four reader slices.
- **Decision Defaults early lineage:** `2abb2e4570f77a63ef087cfa2fc10cb08210cadb01e9bd304d84d2555249b047` (bare) → `45ec88c440456ce7aa99babe8b58ed088786ed342d5197ab4fef8b69d24d3e29` (+compass) → `11f71f447c17ea48a269adf9c206aa8f23d88a1207ae7388fafb6d9a94004bdc` (session-9).

---

## 9. MASTER CHRONOLOGY & AUTHORITY HISTORY (chronology only)

**Master lineage:** MASTER-5 → 6 (×2) → 7 → 8 → 9 → 9_2 → 9_4 → 10 → 10__1_ → 11 → 11.1 → [12 MISSING] → 13 → 14 family (8 bodies incl. 3 FINAL sub-versions) → [DELTA_S14 + Cursor brief: post-14, pre-15] → [15, 16 MISSING] → 17_FULL_v2 (+4 reader slices) → 18_FULL_v1 → 19_FULL → 19_v1 → 19_v3 → 19_v6 → 19_v7_1 (ADOPTED AUTHORITATIVE).

**Parallel early family:** `NH_MASTER_FILE_COMPLETE` (156L `# N.H — COMPLETE MASTER FILE`) and standalone (257L `# N.H — COMPLETE STANDALONE MASTER FILE`).

**Decision Defaults lineage:** bare → +compass → session-9 → S10.1 → S12 → S13 family (4 bodies) → [S17_AUDITED_v1 (literal heading `# N.H — DECISION DEFAULTS (S17 — DRAFT)`); S17_DRAFT missing] → S19_v1 → S19_v2_2 (ADOPTED AUTHORITATIVE).

**Authority state (declared, not re-judged):** Authoritative pair = `NH_MASTER-19_CORRECTED_v7_1.md` + `NH_DECISION_DEFAULTS-S19_v2_2.md`, governed by `cursorrules` (v3.2). `NH_MASTER-19_CORRECTED_v6` declared predecessor. Accepted-design companions (SECURITY_IDENTITY_AFTER_BGMM, TSC_DESIGN_v1) declare themselves NOT-yet-patched into the Master. Candidates v8 / v2_3 / cursorrules_v3_3 not present, not adopted.

---

## 10. VALIDATION ERRORS & SURFACED MISMATCHES (not silently corrected)

- **Occurrence count:** v1=133, v2=142 (B2/B3 undercounted from deduplicated lists), v3 and v4=**154** (B2=14, B3=16 restored from literal batch-message path lists). Surfaced.
- **`NH_Meaning_Engine_Design.md` body change:** B1 body `18185908fecd4a2a00587a57fc10437f5e5a6003731ec61d4d7f39e37dcf0d62` (137L) overwritten by B5 body `15c2786003463fff73b22dd4bf49cf36df3da30ed27ef57e78663605d2e59a89` (138L). B1 occurrence row now carries its historical hash and the HISTORICAL marker; the resident-ledger row shows the B5 body. Surfaced in §3 and §4.
- **`cursorrules` version:** v2 description said v3.1; the literal heading is `# N.H System — Cursor Rules v3.2`. Corrected to v3.2.
- **`MASTER_FILE_COMPLETE` headings differ between the two bodies** (`# N.H — COMPLETE MASTER FILE` 156L vs `# N.H — COMPLETE STANDALONE MASTER FILE` 257L) — both recorded literally.
- **`NH_MASTER-19_CORRECTED_v3.md` hash** is the full correct `e38c37e97491d7f13310fb9d5d961e86111aad9c917612ccb3ea12e27e127a7b` (matches disk and the Batch-1 receipt). The v1 manifest's abbreviation was a display artifact only.
- **No other same-filename hash changes** were found across batches (see §4). No other mismatch silently corrected.

---

## 11. BATCH 3 EVIDENCE AND CONTRADICTION APPENDIX

**Finding: the Batch 3 total of 16 paths is VERIFIED; the exact identity of the 5 repeat occurrences (occ #41–45) is UNVERIFIED.**

What is provable from the available records:
- The Batch 3 receipt states verbatim: *"The message listed 16 paths."* (total VERIFIED).
- 11 distinct-new-to-disk filenames are enumerated and hashed in the Batch 3 processing (VERIFIED): `NH_MASTER-19_CORRECTED_v6__1_.md`, `NH_MASTER-19_CORRECTED_v7_1__1_.md`, `cursorrules__1_`, `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM__1_.md`, `NH_ACCEPTED_TSC_DESIGN_v1__1_.md`, `NH_DECISION_DEFAULTS-S19_v1__1___1_.md`, `NH_DECISION_DEFAULTS-S19_v2_2__1_.md`, `NH_SHARED_CHAT_HANDOFF_BEFORE_CONSOLIDATION_v1__1_.md`, `NH_wellbeing_baseline_system__1_.md`, `NH_WORKING_ROLES__2_.md`, `NH_CHAT_HANDOFF_AFTER_BGMM__1_.md`.

Why the remaining 5 repeat paths are UNVERIFIED:
- The **original Batch 3 `<uploaded_files>` block is not preserved** in the available records, so the literal repeat paths cannot be reproduced verbatim.
- The Batch 3 receipt is **internally contradictory**: its duplicate section's prose says *"These four paths…"* but then **lists five** MASTER-17 filenames (`NH_MASTER-17_00_INDEX_STATUS.md`, `NH_MASTER-17_01_FOUNDATION_BUILT.md`, `NH_MASTER-17_02_CONCEPTUAL_ARCHITECTURE.md`, `NH_MASTER-17_03_ROADMAP_INTERFACE_HISTORY.md`, `NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md`); and separately, B3-10 states `NH_wellbeing_baseline_system__1_` was *"listed twice within this message's paths."*
- The arithmetic does not uniquely resolve: 11 + 5 MASTER-17 + 1 wellbeing = 17 (over 16); 11 + 4 MASTER-17 + 1 wellbeing = 16 (fits); 11 + 5 MASTER-17 + 0 second-wellbeing = 16 (also fits). Two distinct compositions both satisfy the verified total of 16, and the literal evidence needed to choose between them is absent.

**Resolution applied:** per the standing rule "if the exact original path list cannot be recovered, mark it UNVERIFIED and explain why," occurrence rows #41–45 are flagged **UNVERIFIED — B3 repeat identity** in §3. The best-evidence candidate identities (the five MASTER-17 re-uploads) are shown for continuity, but the manifest does not assert them as proven. The Batch 3 total (16) and the 11 distinct-new files remain VERIFIED, so the cumulative occurrence total (154) is unaffected — it depends only on the verified per-batch counts, not on the unverified repeat identities.

**This is a surfaced provenance contradiction, not a silently resolved one.**

---

## 12. MACHINE-VALIDATION REPORT (embedded)

Every check was computed programmatically against this file's own text and the on-disk source files. Methods are stated per row. Any UNVERIFIED item is marked as such with its reason; it does not block the PASS items but is reported honestly.

| # | Check | State | Expected | Measured | Method |
|---|---|---|---|---|---|
| 1 | Loose resident rows (Ledger A.1) | PASS | 100 | 100 | Regex count of `^\| \d+ \| \`` rows in §2A.1 |
| 2 | Archive-member rows (Ledger A.2) | PASS | 2 | 2 | Regex count of rows in §2A.2 |
| 3 | Upload occurrence rows (Ledger B) | PASS | 154 | 154 | Regex count of `^\| \d+ \| B\d \|` rows in §3 |
| 4 | Project Knowledge rows (Ledger PK) | PASS | 4 | 4 | Regex count of rows in §5 |
| 5 | Continuous occurrence numbering 1..154 | PASS | 1..154 no gaps | sequential, no gaps/dupes | Parse occ # column, assert == range(1,155) |
| 6 | Per-batch occurrence totals sum to total | PASS | 15+14+16+13+19+20+18+19+20 = 154 | 154 | Sum counts per batch from Ledger B rows |
| 7 | All backticked hashes match `^[0-9a-f]{64}$` | PASS | 0 malformed | 0 malformed of 319 (recomputed on the completed v5 body) | Regex extract + fullmatch each |
| 8 | No truncated hash tokens (`xxxx…`) in backticks | PASS | 0 | 0 | Regex scan for `\`[0-9a-f]{6,40}…` |
| 9 | No abbreviated filenames | PASS | 0 | 0 of 331 filename tokens | Regex extract filename tokens; assert no `…`/`...` |
| 10 | Both full PDF filenames present | PASS | 2 | 2 | Substring search for full PDF names |
| 11 | Literal-heading extraction (all 96 text files) | PASS | 96 present | 96 present (4 binary N/A) | For each resident text file, assert its on-disk literal heading appears in the file |
| 12 | Duplicate groups each contain exactly one hash | PASS | 14 single-hash groups | 14 | Group resident filenames by hash; assert each §7 group lists one hash |
| 13 | Unique-hash + redundant arithmetic = 100 | PASS | 86 + 14 = 100 | 86 + 14 = 100 | Count distinct resident hashes + redundant copies |
| 14 | Historical occurrence preserved (not replaced) | PASS | B1 Meaning Engine uses `18185908fecd4a2a00587a57fc10437f5e5a6003731ec61d4d7f39e37dcf0d62`; marked HISTORICAL | found + marked | Substring check of occ row + HISTORICAL marker |
| 15 | v2-to-v5 source preservation | PASS | every v2 source filename present | all present (excl. manifest self-names) | Extract v2 filename tokens; assert each in v5 |
| 16 | v3-to-v5 and v4-to-v5 source preservation | PASS | every v3 and v4 source filename present | all present (excl. manifest self-names) | Extract v3 and v4 filename tokens; assert each in v5 |
| 17 | Unresolved placeholders outside quoted explanatory examples | PASS | 0 operational placeholders | 0 | Strip all backtick-quoted code spans (which legitimately contain `%d`/`%s`/`{}`/`TODO` as documented examples of what was fixed), then regex-scan the remaining prose for live `%d`/`%s`/`{}`/`TODO` template tokens. The literal token strings that survive in the file appear only inside quoted explanatory examples and historical-discussion backticks, not as operational/template placeholders. |
| 18 | Batch 3 repeat-occurrence identity | UNVERIFIED | (literal path list) | not recoverable (see §11) | Original `<uploaded_files>` block absent; receipt internally contradictory. Total (16) and 11 distinct-new VERIFIED; 5 repeat identities UNVERIFIED. |

**Overall: 17 PASS, 1 UNVERIFIED (Batch 3 repeat identity, §11). 0 FAIL.** No check is marked PASS while a placeholder or unresolved provenance contradiction remains; the Batch 3 contradiction is explicitly carried as UNVERIFIED rather than hidden inside a PASS.

---

## 13. WHAT HAS NOT BEEN DONE

No Feature Recovery and Decision Ledger · no Master comparison · no feature-recovery audit · no restoration · no reconciliation · no rewriting · no consolidation · no final self-contained Master · no Decision-Defaults regeneration · no adoption of any candidate · no overwrite of any prior manifest (v1, v2, v3) or Master. Provenance only.

---

*Corrected manifest v5. Upload occurrences: 154. Loose resident: 100. Archive members: 2. Ledger A rows: 102. Unique loose hashes: 86. Project Knowledge: 4 (separate). Unreadable: 0.*
