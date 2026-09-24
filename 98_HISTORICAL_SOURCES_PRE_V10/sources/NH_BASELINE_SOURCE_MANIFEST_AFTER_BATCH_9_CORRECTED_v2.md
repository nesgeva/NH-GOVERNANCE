# N.H — BASELINE SOURCE MANIFEST (AFTER BATCH 9) — CORRECTED v2

**Status: PERMANENT PROVENANCE RECORD — provenance-correction pass. NOT a consolidation, audit, or feature-recovery ledger.**

This corrected manifest supersedes `NH_BASELINE_SOURCE_MANIFEST_AFTER_BATCH_9.md` (preserved unchanged). It separates the **Resident Source Ledger** from the **Upload Occurrence Ledger**, uses full 64-character hashes throughout, exact non-abbreviated filenames, a separate Project Knowledge section, and a machine-validation report. No cross-file comparison, feature-recovery audit, restoration, reconciliation, rewriting, or consolidation has been performed.

Generated after the explicit declaration: *"FINAL BATCH — ALL CURRENTLY LOCATED SOURCE FILES HAVE NOW BEEN SUPPLIED."*

---

## 0. STANDING RULES GOVERNING THIS MANIFEST

1. **Newer does not automatically mean more complete.** A later-numbered Master, a larger file, a file labeled "FINAL," or the adopted-authoritative file is NOT assumed to contain more or better design. Completeness is established only by direct comparison, which has NOT been done.
2. **Duplicates must never disappear from provenance.** Every upload occurrence, exact duplicate, renamed copy, copy-suffix file, reader copy, backup, and archive member keeps its own row. Identical-content files are linked by shared SHA-256 but never deleted, omitted, replaced, or collapsed.
3. **Older Masters may preserve important original features.** Material in an early Master and absent later is possibly-dropped design to recover later — never obsolete merely for being older.
4. **No design decision may be silently resolved.** Conflicts and open forks are recorded and preserved; no winner is chosen, no file adopted on Ness's behalf.
5. **No consolidation has begun.** This is provenance only.

---

## 1. RECALCULATED CUMULATIVE COUNTS (all reconcile with the two ledgers)

| Metric | Count | Definition |
|---|---|---|
| **Actual upload occurrences (Batches 1–9)** | **142** | Every `<file_path>` attachment line across the nine batch messages, including within-message and cross-batch repeats. The provenance-faithful number. |
| Per-batch occurrences | B1:15 · B2:7 · B3:11 · B4:13 · B5:19 · B6:20 · B7:18 · B8:19 · B9:20 | Counts of attachment lines per batch message. |
| **Distinct resident filenames** | **100** | Unique exact filenames currently accessible in the upload directory. |
| **Unique SHA-256 content hashes (resident, incl. ZIP container)** | **86** | Distinct file bodies among resident files. |
| Redundant physical copies (resident filenames beyond first per hash) | 14 | Resident filenames sharing a hash with an earlier-sorted filename. |
| Exact-duplicate filename groups (resident, >1 filename per hash) | 14 | Hashes carried by two or more resident filenames. |
| Archive-member occurrences (inside `files__3_.zip`) | 2 | `NH_MASTER-11.1.md` + `NH_DECISION_DEFAULTS-S10.1.md`, byte-identical to their loose copies. |
| Unreadable items | 0 | All files opened successfully. |
| Unverified occurrences | 0 | Every occurrence filename resolves to a resident file. |
| **Project Knowledge files (counted separately, NOT uploads)** | **4** | See §5. |

**Reconciliation of the earlier "133":** the first manifest's "133" summed the per-batch *headline distinct-new* counts (15+7+11+13+17+16+18+18+18). That under-counted true attachment occurrences, because several batch messages re-attached the same filename within one message (B5 listed 19 paths, B6 listed 20, B8 listed 19 with `…S12` twice, B9 listed 20 with the two new files twice). The correct upload-occurrence total is **142**. Both the old and corrected figures are recorded so nothing is hidden.

---

## 2. RESIDENT SOURCE LEDGER (A)

One row per exact resident filename. Full 64-char hashes. `Batches` = every batch the filename was attached in.

| # | Exact Filename | Source | Batches | SHA-256 (64 hex) | Bytes | Lines | Read | First heading / first line | Description | Declared status | Dup-group | Related-version family | Authority |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM__1_.md` | upload directory | B3 | `fb36bf8e55026ed7d79e4a5264be17f2577dda3276c4b2d2dc320018931f16f5` | 71936 | 1724 | YES | # NH ACCEPTED SECURITY/IDENTITY DESIGNS AFTER BGMM | Companion record, declared NOT authoritative; 'not yet patched into Master v6.' | Companion, NOT authoritative | G-ACCSEC | - | Companion (declared non-authoritative) |
| 2 | `NH_ACCEPTED_TSC_DESIGN_v1__1_.md` | upload directory | B3 | `1da2e296d4345d11dcec5f197aa9a42883349526275c5aa32b0bb07d1ca44658` | 43237 | 956 | YES | # NH ACCEPTED TSC DESIGN v1 | Companion record (Temporary Session Cache), declared NOT authoritative. | Companion, NOT authoritative | G-ACCTSC | - | Companion (declared non-authoritative) |
| 3 | `NH_Build_Checklist.md` | upload directory | B5 | `e4d1436a3e5655ce4b09135c65424a2a672157731441f48f954044aa5d1aea40` | 4325 | 95 | YES | # N.H — SIMPLE BUILD CHECKLIST | V/X built-vs-unbuilt snapshot (June 20 2026). | Status snapshot | G-CHECKLIST | - | Historical status |
| 4 | `NH_CHAT_HANDOFF_AFTER_BGMM__1_.md` | upload directory | B3 | `f524f7cdd4dd2f1b897177e0e7f0843d1c8a7767341e4a010da9ab066414a562` | 8081 | 171 | YES | # NH CHAT HANDOFF AFTER BGMM | Handoff: authority order Master v6->DD v1->roles; 13 accepted security/identity/BGMM components. | Handoff record | G-HANDOFF1 | - | Handoff record |
| 5 | `NH_CURSOR_BRIEF_reading_validator.md` | upload directory | B9 | `d80065191b04f26d3b0834cd1e861fda68a28d6c61f80d2bd458fce37ac70ba9` | 9455 | 86 | YES | # CURSOR BRIEF — Reading Validator + Reading-Shaped Writer | Build spec: 12-field reading contract + reading-shaped writer. Spec only, not approved code. | Build spec, not approved | G-CURSORBRIEF | - | Build spec |
| 6 | `NH_Canvas_Design_Spec.md` | upload directory | B4 | `20444814d0ac1cf5ff49a927862b0025c9c069760e425999dbff7a2893e1d5b5` | 4995 | 78 | YES | # N.H — Canvas Design Spec | Canvas design spec. | Spec | G-CANVAS | - | Design source |
| 7 | `NH_DECISION_DEFAULTS-S10_1.md` | upload directory | B7 | `b018ae48f8863c223a2a345c7747877722e1c6b108bab754c78c9182e774968c` | 10874 | 88 | YES | # N.H — DECISION DEFAULTS | S10.1 Decision Defaults (matches MASTER-11.1): 2a two-file structure; Helper-not-Decider. Also a member inside files__3_.zip. | Decision Defaults, historical | G-DDS101 | Decision Defaults lineage | Historical companion |
| 8 | `NH_DECISION_DEFAULTS-S12.md` | upload directory | B7,B8 | `da329e8652ba0f35a4b2d864ade986ca7c61c1324240d84804ffc808c944cfa8` | 12602 | 103 | YES | # N.H — DECISION DEFAULTS | S12: store BUILT & clean (5,521 roots, 7-field w/ role); disk-verify-[BUILT]-claims lesson. | Decision Defaults, historical | G-DDS12 | Decision Defaults lineage | Historical companion |
| 9 | `NH_DECISION_DEFAULTS-S13.md` | upload directory | B7,B8,B9 | `eaea2e2ccb3118d50a44d06bda5f12f94bb436ea1cde5411b98370334cd9644a` | 18133 | 121 | YES | # N.H — DECISION DEFAULTS | S13 Decision Defaults family — smallest (121 lines). | Decision Defaults, historical | G-DDS13 | DD-S13 family | Historical companion |
| 10 | `NH_DECISION_DEFAULTS-S13__1_.md` | upload directory | B7,B8,B9 | `0ff6dd4ce29b7001596db5dd4862fa66d976efe64430653850a735db06f9e2f0` | 19065 | 123 | YES | # N.H — DECISION DEFAULTS | S13 Decision Defaults family (123 lines). | Decision Defaults, historical | G-DDS131 | DD-S13 family | Historical companion |
| 11 | `NH_DECISION_DEFAULTS-S13__2_.md` | upload directory | B7,B8,B9 | `0ff6dd4ce29b7001596db5dd4862fa66d976efe64430653850a735db06f9e2f0` | 19065 | 123 | YES | # N.H — DECISION DEFAULTS | S13 Decision Defaults family (123 lines). | Decision Defaults, historical | G-DDS131 | DD-S13 family | Historical companion |
| 12 | `NH_DECISION_DEFAULTS-S13__3_.md` | upload directory | B7,B8,B9 | `f6358c44db6e115309e2b1d25a818fe2f02d86a79cea6fefa9daa31bfeead4f1` | 22527 | 124 | YES | # N.H — DECISION DEFAULTS | S13 Decision Defaults family (124 lines). | Decision Defaults, historical | G-DDS133 | DD-S13 family | Historical companion |
| 13 | `NH_DECISION_DEFAULTS-S13__4_.md` | upload directory | B8,B9 | `8acc713871d9c9160143014ebd5823df61df7082fd37ed27e3d20c4b4314f86d` | 23616 | 125 | YES | # N.H — DECISION DEFAULTS | S13 Decision Defaults family — largest (125 lines). | Decision Defaults, historical | G-DDS134 | DD-S13 family | Historical companion |
| 14 | `NH_DECISION_DEFAULTS-S13__6_.md` | upload directory | B8,B9 | `8acc713871d9c9160143014ebd5823df61df7082fd37ed27e3d20c4b4314f86d` | 23616 | 125 | YES | # N.H — DECISION DEFAULTS | S13 Decision Defaults family — largest (125 lines). | Decision Defaults, historical | G-DDS134 | DD-S13 family | Historical companion |
| 15 | `NH_DECISION_DEFAULTS-S17_AUDITED_v1.md` | upload directory | B2 | `a0df064a0f4dce25825282e67619ff0c3e0319c37916ca463539b4d1390f69fe` | 26274 | 390 | YES | # N.H — DECISION DEFAULTS (S17 AUDITED v1) | S17 audited Decision Defaults; titled DRAFT / derived-not-authority. | Decision Defaults, titled DRAFT | G-DDS17 | Decision Defaults lineage | Historical companion / draft |
| 16 | `NH_DECISION_DEFAULTS-S19_v1__1___1_.md` | upload directory | B3 | `ecea9224163681f9fc1d29327b0453c5e7ead42fd178786ab9dc6a6d4e1baaa6` | 33328 | 298 | YES | # N.H — DECISION DEFAULTS (S19 v1) | S19_v1 Decision Defaults — synced to Master v6. | Decision Defaults, candidate | G-DDS19V1 | Decision Defaults lineage | Historical companion / candidate |
| 17 | `NH_DECISION_DEFAULTS-S19_v2_2__1_.md` | upload directory | B3 | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` | 37048 | 314 | YES | # N.H — DECISION DEFAULTS (S19 v2_2) | ADOPTED AUTHORITATIVE Decision Defaults. Identical to Project Knowledge copy. | ADOPTED AUTHORITATIVE | G-DDS19V22 | Decision Defaults lineage | ADOPTED AUTHORITATIVE (explicit) |
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
| 41 | `NH_MASTER-17_00_INDEX_STATUS.md` | upload directory | B1 | `b7c794561d102eb682f219937c0c5b1551b338ed76a902e43d32101649fb96c9` | 26966 | 184 | YES | # N.H — MASTER-17 · 00 INDEX/STATUS | Derived reader copy (do-not-edit) of MASTER-17. | DERIVED READER COPY | G-M17-00 | MASTER-17 reader slices | Reader copy (derived) |
| 42 | `NH_MASTER-17_01_FOUNDATION_BUILT.md` | upload directory | B1 | `da261935d739e30e8c8a2f4cdcdcbce47c29948511ad2fb7f9f48a6d52b9a008` | 23998 | 216 | YES | # N.H — MASTER-17 · 01 FOUNDATION BUILT | Derived reader copy of MASTER-17. | DERIVED READER COPY | G-M17-01 | MASTER-17 reader slices | Reader copy (derived) |
| 43 | `NH_MASTER-17_02_CONCEPTUAL_ARCHITECTURE.md` | upload directory | B1 | `186717c1ba60f60c1a511231820d6d45805161966f93d8c26cbeeb8c5c24d341` | 76345 | 548 | YES | # N.H — MASTER-17 · 02 CONCEPTUAL ARCHITECTURE | Derived reader copy of MASTER-17. | DERIVED READER COPY | G-M17-02 | MASTER-17 reader slices | Reader copy (derived) |
| 44 | `NH_MASTER-17_03_ROADMAP_INTERFACE_HISTORY.md` | upload directory | B1 | `0a64a524d7325e5408fe591080ddec93bca2c9ae98ff4557cece6379dd53d5a9` | 40994 | 255 | YES | # N.H — MASTER-17 · 03 ROADMAP/INTERFACE/HISTORY | Derived reader copy of MASTER-17. | DERIVED READER COPY | G-M17-03 | MASTER-17 reader slices | Reader copy (derived) |
| 45 | `NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md` | upload directory | B1,B2 | `cfdaefe9b0b6c134a911f102ae6479fb845662165a1cf216aec465ff816ce152` | 165109 | 1148 | YES | # N.H — MASTER-17 ... | MASTER-17 full draft (corrected v2). Source of the four reader slices. | Full draft Master, candidate | G-MASTER17 | MASTER-19 lineage | Historical Master |
| 46 | `NH_MASTER-18_FULL_DRAFT_v1.md` | upload directory | B2 | `2f63734c600f4f8ea212b15c99c81f0a00a415dd525afb7d5176168c9edb5397` | 206696 | 1464 | YES | # N.H — MASTER-18 ... | MASTER-18 full draft. | Full draft Master, candidate | G-MASTER18 | MASTER-19 lineage | Historical Master |
| 47 | `NH_MASTER-19_CORRECTED_v1.md` | upload directory | B2 | `0287015be938212d8065e5f2d3ac9b952a1f8943a043864ef63614d1670beffb` | 262683 | 1779 | YES | # N.H — MASTER-19 CORRECTED v1 | MASTER-19 corrected v1 (1779 lines). | Corrected Master, candidate | G-M19V1 | MASTER-19 lineage | Historical Master / candidate |
| 48 | `NH_MASTER-19_CORRECTED_v3.md` | upload directory | B1 | `e38c37e97491d7f13310fb9d5d961e86111aad9c917612ccb3ea12e27e127a7b` | 283033 | 1910 | YES | # N.H — MASTER-19 CORRECTED v3 | MASTER-19 corrected v3 (1910 lines). Header names §8 security-rules drop 5->17 / restore S19. | Corrected Master, candidate | G-M19V3 | MASTER-19 lineage | Historical Master / candidate |
| 49 | `NH_MASTER-19_CORRECTED_v6__1_.md` | upload directory | B3 | `8165f4bed94d2d57140d49e93d3c85b8e2b259053e0b30ac4c675fa7463a1bf9` | 283081 | 1908 | YES | # N.H — MASTER-19 CORRECTED v6 | MASTER-19 v6 — declared predecessor of v7_1; matches AFTER_BGMM handoff. | Corrected Master, declared predecessor of authoritative | G-M19V6 | MASTER-19 lineage | Declared predecessor of authoritative |
| 50 | `NH_MASTER-19_CORRECTED_v7_1__1_.md` | upload directory | B3 | `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf` | 291811 | 1937 | YES | # N.H — MASTER-19 CORRECTED v7_1 | ADOPTED AUTHORITATIVE Master (1937 lines). Identical to Project Knowledge copy. | ADOPTED AUTHORITATIVE | G-M19V71 | MASTER-19 lineage | ADOPTED AUTHORITATIVE (explicit) |
| 51 | `NH_MASTER-19_FULL.md` | upload directory | B2 | `bc498fda2fea592fbb08fd7d1b1ded23f13d8522bfb1f2dc324095df5259caec` | 245244 | 1706 | YES | # N.H — MASTER-19 (FULL) | MASTER-19 full. Hardware row still RTX 5060 Ti (pre-3090). | Full Master, candidate | G-MASTER19F | MASTER-19 lineage | Historical Master |
| 52 | `NH_MASTER-5.md` | upload directory | B5 | `f91fdf682bac232b468c95ac99b8af4e0e385afe5e532108bdd2721026d0692c` | 32737 | 223 | YES | # N.H — MASTER (complete, consolidated) | Earliest numbered Master (session 2). Names §3D security fixes BUILT; lower bound named in v3 header for the §8 rules drop/restore. | Consolidated Master, candidate | G-MASTER5 | MASTER-5 | Historical Master |
| 53 | `NH_MASTER-6.md` | upload directory | B5 | `63a64d0895e5ee4cebfc9b8a2399356afe1c505ecdf04ca8ee45f2d6079948cc` | 45407 | 273 | YES | # N.H — MASTER (complete, self-contained) | Master-6, shorter of two copies; rules+meaning-engine written in full. | Self-contained Master, candidate | G-MASTER6A | MASTER-6 family | Historical Master |
| 54 | `NH_MASTER-6__1_.md` | upload directory | B5 | `3e978e036871c1188400409bfa439380f5cce02e2afd4bbb2830d85b15fe7633` | 54506 | 315 | YES | # N.H — MASTER (complete, self-contained) | Master-6, longer copy (315 lines). | Self-contained Master, candidate | G-MASTER6B | MASTER-6 family | Historical Master |
| 55 | `NH_MASTER-7.md` | upload directory | B5 | `6868507ca073051860daadf80554e5e064b8d3d1b293427d28fede746ba135c4` | 60439 | 332 | YES | # N.H — MASTER (complete, self-contained, full depth) | Master-7. | Self-contained Master, candidate | G-MASTER7 | MASTER lineage | Historical Master |
| 56 | `NH_MASTER-8.md` | upload directory | B5 | `13675a34e039d726cd845bde8a7177e1f260dadb3a19b9b6ba4c7b2c87bde48a` | 80833 | 423 | YES | # N.H — MASTER (complete, self-contained, full depth) | Master-8. | Self-contained Master, candidate | G-MASTER8 | MASTER lineage | Historical Master |
| 57 | `NH_MASTER-9.md` | upload directory | B5 | `e6bf27a4d4c81ba7e9e9351014397c7668fb1a114f2aa32d6babbaccaae7a813` | 89479 | 442 | YES | # N.H — MASTER (complete, self-contained, full depth) | Master-9. | Self-contained Master, candidate | G-MASTER9 | MASTER-9 family | Historical Master |
| 58 | `NH_MASTER-9_2.md` | upload directory | B5 | `052731353b4a221d358133219c5c280aa2e4ada98a1445657aec17b6ce13107e` | 127717 | 513 | YES | # N.H — MASTER (complete, self-contained, full depth) | Master-9.2 revision (513 lines). | Self-contained Master, candidate | G-MASTER92 | MASTER-9 family | Historical Master |
| 59 | `NH_MASTER-9_2__1_.md` | upload directory | B5,B6 | `052731353b4a221d358133219c5c280aa2e4ada98a1445657aec17b6ce13107e` | 127717 | 513 | YES | # N.H — MASTER (complete, self-contained, full depth) | Master-9.2 revision (513 lines). | Self-contained Master, candidate | G-MASTER92 | MASTER-9 family | Historical Master |
| 60 | `NH_MASTER-9_4.md` | upload directory | B6 | `9bbc28dc31c7825d5f3927169526a23bfd0abff9f5a994ce3dc4fd6f7cf1e8dd` | 149631 | 580 | YES | # N.H — MASTER (complete, self-contained, full depth) | MASTER-9.4 (session 8): adds §13 live loop + §14 chat-front-door sketch. Header states nothing on disk changed (store 11,374/4 groups). | Self-contained Master, candidate | G-MASTER94 | MASTER lineage | Historical Master |
| 61 | `NH_MASTER_CONTEXT.md` | upload directory | B1 | `e6ae68b37a375d90ea04d6000e311cca7d4199c715e51bd6873f99d8f169f099` | 22765 | 323 | YES | # N.H — MASTER CONTEXT | Old context file. Mandates 'Nes' spelling (conflicts with corrected 'Ness'). | Context file, historical | G-CONTEXT | - | Historical (conflict source) |
| 62 | `NH_MASTER_FILE_COMPLETE.md` | upload directory | B4 | `80a6143e9857ee77e9cf75ebd1c55724938f23bd04aae8b9b761160171bfcd02` | 17065 | 156 | YES | # N.H — COMPLETE STANDALONE MASTER FILE | Bare COMPLETE master (156 lines). 'Supersedes...' | COMPLETE master, candidate | G-COMPLETE0 | MASTER_FILE_COMPLETE family | Historical Master |
| 63 | `NH_MASTER_FILE_COMPLETE__1_.md` | upload directory | B4,B5 | `06f69672fa89800f060c70864bf1fd87532aff4359f3e538c48b087f08d8daed` | 29203 | 257 | YES | # N.H — COMPLETE STANDALONE MASTER FILE | Standalone COMPLETE master (257 lines). | COMPLETE master, candidate | G-COMPLETE1 | MASTER_FILE_COMPLETE family | Historical Master |
| 64 | `NH_MASTER_FILE_COMPLETE__2_.md` | upload directory | B5 | `06f69672fa89800f060c70864bf1fd87532aff4359f3e538c48b087f08d8daed` | 29203 | 257 | YES | # N.H — COMPLETE STANDALONE MASTER FILE | Standalone COMPLETE master (257 lines). | COMPLETE master, candidate | G-COMPLETE1 | MASTER_FILE_COMPLETE family | Historical Master |
| 65 | `NH_MASTER_section13_ADD.md` | upload directory | B5,B6 | `91d82ed52bcbf497fc12a5c61d479ab5f8fb83f9fc341f878165c446238d68b9` | 7590 | 35 | YES | # N.H — ADD TO MASTER AS §13 | §13 live-loop add-on (fire-and-let-go). | Add-on fragment | G-S13ADD | Master add-ons | Historical fragment |
| 66 | `NH_Meaning_Engine_Design.md` | upload directory | B1,B5 | `15c2786003463fff73b22dd4bf49cf36df3da30ed27ef57e78663605d2e59a89` | 12479 | 138 | YES | # N.H — THE MEANING ENGINE | Meaning-engine mechanism (8 parts). Separator-formatting variant of the B1 copy. | Design (mechanism) | G-MEANING | Meaning Engine family | Design source |
| 67 | `NH_Mobile_App_Design_Spec.md` | upload directory | B1 | `023c82babd4231d0b6fc8235396454e4d07e06d9a769797a4a31c9867885812c` | 5438 | 82 | YES | # N.H — Mobile App Design Spec | Mobile app design spec. | Spec | G-MOBILE | - | Design source |
| 68 | `NH_RECENT_CONTINUITY_NOTE_POST_MASTER17-3.md` | upload directory | B2 | `7d614546710c9aa66ff02f87449fe30505cb5a0d6d929462a4e719a71fe082e3` | 8861 | 239 | YES | # NH RECENT CONTINUITY NOTE POST-MASTER17-3 | Continuity note post-MASTER17. | Continuity note | G-CONTINUITY | - | Continuity note |
| 69 | `NH_SHARED_CHAT_HANDOFF_BEFORE_CONSOLIDATION_v1__1_.md` | upload directory | B3 | `47e6a8ba71fa7e90e8bb8ba671cad22291c950c2770d78e82eea6d331ca7d865` | 6590 | 185 | YES | # NH SHARED CHAT HANDOFF BEFORE CONSOLIDATION v1 | Names authoritative pair + hashes. | Handoff record | G-HANDOFF2 | - | Handoff record |
| 70 | `NH_Universal_Filter_Design.md` | upload directory | B4 | `3df666eb4ff4d90e5a5a299f7f7d52361638a27feb1e727894f0e0658c421020` | 5740 | 88 | YES | # N.H — Universal Filter Design | Bare UF design — no Keystone, no Membrane. | Design sketch | G-UFD0 | Universal Filter Design family | Design source |
| 71 | `NH_Universal_Filter_Design__1_.md` | upload directory | B1,B4 | `7dce7058c991dc1aeb583e7455234a6721c7fea089626fcccecf529f5b48b1c7` | 10321 | 131 | YES | # N.H — Universal Filter Design | UF design + Keystone. | Design sketch | G-UFD1 | Universal Filter Design family | Design source |
| 72 | `NH_Universal_Filter_Design__2_.md` | upload directory | B4 | `c8938d370efdd072912cabb4adf844dba4cc581095d68fca7022cff30710be15` | 13755 | 155 | YES | # N.H — Universal Filter Design | UF design + Keystone + MEMBRANE (Membrane section exists ONLY here among design copies). | Design sketch | G-UFD2 | Universal Filter Design family | Design source |
| 73 | `NH_Universal_Filter_RULES.md` | upload directory | B5 | `c0fb4528a332f4014782afacee63d167407e31cc88b1502ec8783900588b3a37` | 11828 | 178 | YES | # N.H UNIVERSAL FILTER — OPERATING RULES FOR ANY AI | 12-rule operating ruleset. Rule 6 (memory only adds), Rule 7 (the membrane), Rule 11 (steerer-not-clerk). | Ruleset (design) | G-UFRULES | Universal Filter | Design source |
| 74 | `NH_WORKING_ROLES.md` | upload directory | B2 | `a0281060abd7e7da791bb56a97316ab9ec41ab88fdd7884fac4c6434fa487619` | 3015 | 49 | YES | # N.H — WORKING ROLES | Role division (Ness owns meaning / Claude architects+audits / Cursor codes). | Roles governance | G-ROLES | - | Governance |
| 75 | `NH_WORKING_ROLES__2_.md` | upload directory | B3 | `a0281060abd7e7da791bb56a97316ab9ec41ab88fdd7884fac4c6434fa487619` | 3015 | 49 | YES | # N.H — WORKING ROLES | Role division (Ness owns meaning / Claude architects+audits / Cursor codes). | Roles governance | G-ROLES | - | Governance |
| 76 | `NH_chat_frontdoor_design_sketch.md` | upload directory | B1,B6 | `757b6dd889aedf4af840ecfa190e0404c79ccf609d37607a105dca85f0af0112` | 13532 | 105 | YES | # N.H — THE CHAT FRONT DOOR & THE LIVE SYSTEM | §14 chat front-door working sketch (explicitly unconfirmed). | Design sketch, unconfirmed | G-FRONTDOOR | Chat front-door | Design source (unconfirmed) |
| 77 | `NH_chat_frontdoor_design_sketch__1_.md` | upload directory | B6 | `757b6dd889aedf4af840ecfa190e0404c79ccf609d37607a105dca85f0af0112` | 13532 | 105 | YES | # N.H — THE CHAT FRONT DOOR & THE LIVE SYSTEM | §14 chat front-door working sketch (explicitly unconfirmed). | Design sketch, unconfirmed | G-FRONTDOOR | Chat front-door | Design source (unconfirmed) |
| 78 | `NH_honest_calibration_note.md` | upload directory | B1 | `4096cc357b1e8cd5d8d3cfc83a688946fa5a3145c9edbe83198d03ad5d28f6ac` | 5346 | 48 | YES | # N.H — honest calibration note | Honest-calibration note. | Note | G-CALIB | - | Note |
| 79 | `NH_live_mechanism.html` | upload directory | B6 | `b329a5e4cf24b8ccbbb13e876da05e5b5542efb8aed2476420e08cbb053d6bb8` | 18314 | 316 | YES | (N.H live mechanism HTML) | Live-mechanism interactive HTML (shorter, 316 lines). | Prototype (HTML) | G-LIVEMECH0 | live_mechanism HTML family | Prototype |
| 80 | `NH_live_mechanism__1_.html` | upload directory | B6 | `a4465293961004e802cfa660e454d3aa2550bf136a94da5a8b7b2fa163fd7071` | 21576 | 332 | YES | (N.H live mechanism HTML) | Live-mechanism interactive HTML (longer, 332 lines). | Prototype (HTML) | G-LIVEMECH1 | live_mechanism HTML family | Prototype |
| 81 | `NH_live_mechanism_picture.svg` | upload directory | B1,B6 | `4a9bd78d4f49bea70954e91aeeb07f46f135c731b994f439d6e8486bea7cb42b` | 5697 | 79 | YES | (N.H live mechanism SVG diagram) | Live-mechanism SVG diagram. | Diagram (SVG) | G-LIVESVG | - | Diagram |
| 82 | `NH_live_mechanism_picture__1_.svg` | upload directory | B6 | `4a9bd78d4f49bea70954e91aeeb07f46f135c731b994f439d6e8486bea7cb42b` | 5697 | 79 | YES | (N.H live mechanism SVG diagram) | Live-mechanism SVG diagram. | Diagram (SVG) | G-LIVESVG | - | Diagram |
| 83 | `NH_risk_review_and_openrouter.md` | upload directory | B4 | `3864a2eb1a8f97bf433bd7ebaf0a9d4d85ba6e09bbd26c9c39d1371d5fe6d598` | 5245 | 63 | YES | # N.H — risk review & openrouter | Risk review (bare). | Risk review | G-RISK0 | Risk review family | Design source |
| 84 | `NH_risk_review_and_openrouter__1_.md` | upload directory | B4 | `6fa53662b406edb1b410d56bb43560027fb7a7d6f9042db5233a6b5f60f710c7` | 8384 | 85 | YES | # N.H — risk review & openrouter | Risk review + boot-error/silent-auto-start resolution. | Risk review | G-RISK1 | Risk review family | Design source |
| 85 | `NH_wellbeing_baseline_system.md` | upload directory | B1 | `afb1bad3c1edad3e86e76c5a1cb278b1a1e03c750d4fa1af6f54ad804bcc098c` | 7926 | 140 | YES | # N.H — wellbeing baseline system | Behavioral-baseline wellbeing engine design. | Spec | G-WELLBEING | - | Design source |
| 86 | `NH_wellbeing_baseline_system__1_.md` | upload directory | B3 | `afb1bad3c1edad3e86e76c5a1cb278b1a1e03c750d4fa1af6f54ad804bcc098c` | 7926 | 140 | YES | # N.H — wellbeing baseline system | Behavioral-baseline wellbeing engine design. | Spec | G-WELLBEING | - | Design source |
| 87 | `N_H__Personal_AI__Sovereignty-First_Architecture_with_Mandatory_REALITY_SIMULATION_Gate_Surveyed_Against_the_Field.pdf` | upload directory | B4 | `ba98f5c9e2f073aacbb4999363d0a2e44fd9d90149665b49ee42d07c49eaf19a` | 470408 | N/A — binary/PDF (wc -l on raw bytes = 9992 newline bytes) | YES | (PDF binary — 8-page field survey) | 8-page field-survey PDF: N.H combination genuinely novel vs the field. | Field-survey PDF | G-PDF | - | External survey |
| 88 | `N_H__Personal_AI__Sovereignty-First_Architecture_with_Mandatory_REALITY_SIMULATION_Gate_Surveyed_Against_the_Field__1_.pdf` | upload directory | B4 | `ba98f5c9e2f073aacbb4999363d0a2e44fd9d90149665b49ee42d07c49eaf19a` | 470408 | N/A — binary/PDF (wc -l on raw bytes = 9992 newline bytes) | YES | (PDF binary — 8-page field survey) | 8-page field-survey PDF: N.H combination genuinely novel vs the field. | Field-survey PDF | G-PDF | - | External survey |
| 89 | `cursorrules__1_` | upload directory | B3 | `5050d08825b93acd72a79d07946e43c8cbe537e079517ccfe66bcae8e30e96e9` | 34821 | 717 | YES | (.cursorrules code ruleset, no markdown heading) | In-force code ruleset (.cursorrules v3.1). Identical to Project Knowledge copy. | ADOPTED AUTHORITATIVE (code ruleset) | G-CURSORRULES | - | ADOPTED AUTHORITATIVE (explicit) |
| 90 | `files__3_.zip` | upload directory | B7 | `a32e34c91ebb986e4fa1ba12bc6397bcdda91266b87f3427aa0e6e08c9543291` | 37097 | N/A — binary/archive (wc -l on raw bytes = 128 newline bytes; archive members listed separately) | YES | (ZIP archive container) | ZIP container. Members byte-identical to loose NH_MASTER-11_1.md + NH_DECISION_DEFAULTS-S10_1.md. | Archive container | G-ZIP | - | Archive container |
| 91 | `nh_2a_prototype.html` | upload directory | B7 | `b3abcbb47273fefdbcc61f07cbeccc7b0945f981ff770121fbb174271a05f164` | 13062 | 259 | YES | <title>N.H — 2a prototype: roots & readings</title> | Interactive 2a roots/readings two-store prototype. | Prototype (HTML) | G-2APROTO | - | Prototype |
| 92 | `nh_architecture_canvas.html` | upload directory | B5 | `971833b6c4b3c6f1c57c094d40d0e3a9b27254087832d29ae46d3338cad90cf2` | 8819 | 174 | YES | <title>N.H — Architecture Canvas</title> | Draggable-node architecture canvas prototype. | Prototype (HTML) | G-ARCHCANVAS | - | Prototype |
| 93 | `nh_icon_combined.html` | upload directory | B4 | `6e194dfdd6c876e5b033cde9696e7b5ab11e8370268410e237b1e863bf90bc6a` | 6089 | 117 | YES | (N.H icon prototype HTML) | Combined icon prototype. | Prototype (HTML) | G-ICON | - | Prototype |
| 94 | `nh_ingest_chatgpt__1_.py` | upload directory | B7 | `b8af9f1d36d93d73bb43daf60786aaa0e36e0313aa85c50b8812d04dd4cb3201` | 5128 | 148 | YES | """nh_ingest_chatgpt.py — clean ingest ... | Clean ChatGPT-export ingest; role carried, not guessed; DRY_RUN default. | Code (ingest pipeline) | G-NHINGEST | - | Code |
| 95 | `nh_log.py` | upload directory | B6 | `63eaf052295b63b7545cdf44c135a6cdad75d3c57c57d545839f25061b1f8d5e` | 17941 | 481 | YES | """nh_log.py - the read-only HTML log / "mirror" ... | Read-only HTML log/"mirror" generator (§7B Part 7). | Code (read-only tool) | G-NHLOG | - | Code |
| 96 | `nh_probe.py` | upload directory | B6 | `2dc08d4e89688b529f468f06348db10e31fcefad1ae0a4dbd5aa5092c18ec6f3` | 7234 | 188 | YES | """nh_probe.py - read-only boundary-signal probe ... | Read-only boundary-signal probe over the store. | Code (read-only tool) | G-NHPROBE | - | Code |
| 97 | `nh_probe_truth.py` | upload directory | B6 | `8716a5014c1fbe4215a888e1f4b8249755c2e8f4a9bf23f5c06be764327ce9b9` | 8301 | 213 | YES | """nh_probe_truth.py - GROUND-TRUTH speaker probe ... | Ground-truth speaker probe (reads gpt_purified_history.txt). | Code (read-only tool) | G-NHPROBET | - | Code |
| 98 | `nh_research_architecture_explained.md` | upload directory | B4 | `d19a3c22091441a65d23f9d3285adf3ed91bf0d98ec3473714444679f5998a06` | 10089 | 176 | YES | # N.H — research architecture explained | Research architecture explainer. | Explainer | G-RESEARCHARCH | - | Design source |
| 99 | `nh_research_architecture_explained__1_.md` | upload directory | B4 | `d19a3c22091441a65d23f9d3285adf3ed91bf0d98ec3473714444679f5998a06` | 10089 | 176 | YES | # N.H — research architecture explained | Research architecture explainer. | Explainer | G-RESEARCHARCH | - | Design source |
| 100 | `nh_search_pipeline_security_decisions.md` | upload directory | B1 | `0550cea1aaca73b681cdb1293c2e1903a6c754c75241a8f663435400022b82a2` | 4506 | 38 | YES | # N.H — search pipeline security decisions | Search-pipeline security decisions. | Security decisions | G-SEARCHSEC | - | Design source |

**Resident Source Ledger row count: 100.**

---

## 3. UPLOAD OCCURRENCE LEDGER (B)

One row per actual attachment occurrence across Batches 1–9, in batch order. Repeated uploads of the same filename — within a batch or across batches — each get their own row. Reconstructed from the batch-message `<file_path>` attachment lists.

| Occ # | Batch | Exact Filename | SHA-256 of resident body (64 hex) |
|---|---|---|---|
| 1 | B1 | `NH_MASTER-17_00_INDEX_STATUS.md` | `b7c794561d102eb682f219937c0c5b1551b338ed76a902e43d32101649fb96c9` |
| 2 | B1 | `NH_MASTER-17_01_FOUNDATION_BUILT.md` | `da261935d739e30e8c8a2f4cdcdcbce47c29948511ad2fb7f9f48a6d52b9a008` |
| 3 | B1 | `NH_MASTER-17_02_CONCEPTUAL_ARCHITECTURE.md` | `186717c1ba60f60c1a511231820d6d45805161966f93d8c26cbeeb8c5c24d341` |
| 4 | B1 | `NH_MASTER-17_03_ROADMAP_INTERFACE_HISTORY.md` | `0a64a524d7325e5408fe591080ddec93bca2c9ae98ff4557cece6379dd53d5a9` |
| 5 | B1 | `NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md` | `cfdaefe9b0b6c134a911f102ae6479fb845662165a1cf216aec465ff816ce152` |
| 6 | B1 | `NH_MASTER-19_CORRECTED_v3.md` | `e38c37e97491d7f13310fb9d5d961e86111aad9c917612ccb3ea12e27e127a7b` |
| 7 | B1 | `NH_MASTER_CONTEXT.md` | `e6ae68b37a375d90ea04d6000e311cca7d4199c715e51bd6873f99d8f169f099` |
| 8 | B1 | `NH_Meaning_Engine_Design.md` | `15c2786003463fff73b22dd4bf49cf36df3da30ed27ef57e78663605d2e59a89` |
| 9 | B1 | `NH_Mobile_App_Design_Spec.md` | `023c82babd4231d0b6fc8235396454e4d07e06d9a769797a4a31c9867885812c` |
| 10 | B1 | `NH_Universal_Filter_Design__1_.md` | `7dce7058c991dc1aeb583e7455234a6721c7fea089626fcccecf529f5b48b1c7` |
| 11 | B1 | `NH_chat_frontdoor_design_sketch.md` | `757b6dd889aedf4af840ecfa190e0404c79ccf609d37607a105dca85f0af0112` |
| 12 | B1 | `NH_honest_calibration_note.md` | `4096cc357b1e8cd5d8d3cfc83a688946fa5a3145c9edbe83198d03ad5d28f6ac` |
| 13 | B1 | `NH_live_mechanism_picture.svg` | `4a9bd78d4f49bea70954e91aeeb07f46f135c731b994f439d6e8486bea7cb42b` |
| 14 | B1 | `NH_wellbeing_baseline_system.md` | `afb1bad3c1edad3e86e76c5a1cb278b1a1e03c750d4fa1af6f54ad804bcc098c` |
| 15 | B1 | `nh_search_pipeline_security_decisions.md` | `0550cea1aaca73b681cdb1293c2e1903a6c754c75241a8f663435400022b82a2` |
| 16 | B2 | `NH_DECISION_DEFAULTS-S17_AUDITED_v1.md` | `a0df064a0f4dce25825282e67619ff0c3e0319c37916ca463539b4d1390f69fe` |
| 17 | B2 | `NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md` | `cfdaefe9b0b6c134a911f102ae6479fb845662165a1cf216aec465ff816ce152` |
| 18 | B2 | `NH_MASTER-18_FULL_DRAFT_v1.md` | `2f63734c600f4f8ea212b15c99c81f0a00a415dd525afb7d5176168c9edb5397` |
| 19 | B2 | `NH_MASTER-19_CORRECTED_v1.md` | `0287015be938212d8065e5f2d3ac9b952a1f8943a043864ef63614d1670beffb` |
| 20 | B2 | `NH_MASTER-19_FULL.md` | `bc498fda2fea592fbb08fd7d1b1ded23f13d8522bfb1f2dc324095df5259caec` |
| 21 | B2 | `NH_RECENT_CONTINUITY_NOTE_POST_MASTER17-3.md` | `7d614546710c9aa66ff02f87449fe30505cb5a0d6d929462a4e719a71fe082e3` |
| 22 | B2 | `NH_WORKING_ROLES.md` | `a0281060abd7e7da791bb56a97316ab9ec41ab88fdd7884fac4c6434fa487619` |
| 23 | B3 | `NH_MASTER-19_CORRECTED_v6__1_.md` | `8165f4bed94d2d57140d49e93d3c85b8e2b259053e0b30ac4c675fa7463a1bf9` |
| 24 | B3 | `NH_MASTER-19_CORRECTED_v7_1__1_.md` | `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf` |
| 25 | B3 | `cursorrules__1_` | `5050d08825b93acd72a79d07946e43c8cbe537e079517ccfe66bcae8e30e96e9` |
| 26 | B3 | `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM__1_.md` | `fb36bf8e55026ed7d79e4a5264be17f2577dda3276c4b2d2dc320018931f16f5` |
| 27 | B3 | `NH_ACCEPTED_TSC_DESIGN_v1__1_.md` | `1da2e296d4345d11dcec5f197aa9a42883349526275c5aa32b0bb07d1ca44658` |
| 28 | B3 | `NH_DECISION_DEFAULTS-S19_v1__1___1_.md` | `ecea9224163681f9fc1d29327b0453c5e7ead42fd178786ab9dc6a6d4e1baaa6` |
| 29 | B3 | `NH_DECISION_DEFAULTS-S19_v2_2__1_.md` | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` |
| 30 | B3 | `NH_SHARED_CHAT_HANDOFF_BEFORE_CONSOLIDATION_v1__1_.md` | `47e6a8ba71fa7e90e8bb8ba671cad22291c950c2770d78e82eea6d331ca7d865` |
| 31 | B3 | `NH_wellbeing_baseline_system__1_.md` | `afb1bad3c1edad3e86e76c5a1cb278b1a1e03c750d4fa1af6f54ad804bcc098c` |
| 32 | B3 | `NH_WORKING_ROLES__2_.md` | `a0281060abd7e7da791bb56a97316ab9ec41ab88fdd7884fac4c6434fa487619` |
| 33 | B3 | `NH_CHAT_HANDOFF_AFTER_BGMM__1_.md` | `f524f7cdd4dd2f1b897177e0e7f0843d1c8a7767341e4a010da9ab066414a562` |
| 34 | B4 | `N_H__Personal_AI__Sovereignty-First_Architecture_with_Mandatory_REALITY_SIMULATION_Gate_Surveyed_Against_the_Field.pdf` | `ba98f5c9e2f073aacbb4999363d0a2e44fd9d90149665b49ee42d07c49eaf19a` |
| 35 | B4 | `N_H__Personal_AI__Sovereignty-First_Architecture_with_Mandatory_REALITY_SIMULATION_Gate_Surveyed_Against_the_Field__1_.pdf` | `ba98f5c9e2f073aacbb4999363d0a2e44fd9d90149665b49ee42d07c49eaf19a` |
| 36 | B4 | `NH_MASTER_FILE_COMPLETE.md` | `80a6143e9857ee77e9cf75ebd1c55724938f23bd04aae8b9b761160171bfcd02` |
| 37 | B4 | `NH_MASTER_FILE_COMPLETE__1_.md` | `06f69672fa89800f060c70864bf1fd87532aff4359f3e538c48b087f08d8daed` |
| 38 | B4 | `nh_icon_combined.html` | `6e194dfdd6c876e5b033cde9696e7b5ab11e8370268410e237b1e863bf90bc6a` |
| 39 | B4 | `NH_Canvas_Design_Spec.md` | `20444814d0ac1cf5ff49a927862b0025c9c069760e425999dbff7a2893e1d5b5` |
| 40 | B4 | `NH_risk_review_and_openrouter.md` | `3864a2eb1a8f97bf433bd7ebaf0a9d4d85ba6e09bbd26c9c39d1371d5fe6d598` |
| 41 | B4 | `NH_risk_review_and_openrouter__1_.md` | `6fa53662b406edb1b410d56bb43560027fb7a7d6f9042db5233a6b5f60f710c7` |
| 42 | B4 | `nh_research_architecture_explained.md` | `d19a3c22091441a65d23f9d3285adf3ed91bf0d98ec3473714444679f5998a06` |
| 43 | B4 | `nh_research_architecture_explained__1_.md` | `d19a3c22091441a65d23f9d3285adf3ed91bf0d98ec3473714444679f5998a06` |
| 44 | B4 | `NH_Universal_Filter_Design.md` | `3df666eb4ff4d90e5a5a299f7f7d52361638a27feb1e727894f0e0658c421020` |
| 45 | B4 | `NH_Universal_Filter_Design__1_.md` | `7dce7058c991dc1aeb583e7455234a6721c7fea089626fcccecf529f5b48b1c7` |
| 46 | B4 | `NH_Universal_Filter_Design__2_.md` | `c8938d370efdd072912cabb4adf844dba4cc581095d68fca7022cff30710be15` |
| 47 | B5 | `NH_MASTER-5.md` | `f91fdf682bac232b468c95ac99b8af4e0e385afe5e532108bdd2721026d0692c` |
| 48 | B5 | `NH_MASTER_FILE_COMPLETE__2_.md` | `06f69672fa89800f060c70864bf1fd87532aff4359f3e538c48b087f08d8daed` |
| 49 | B5 | `NH_MASTER_FILE_COMPLETE__1_.md` | `06f69672fa89800f060c70864bf1fd87532aff4359f3e538c48b087f08d8daed` |
| 50 | B5 | `NH_MASTER-8.md` | `13675a34e039d726cd845bde8a7177e1f260dadb3a19b9b6ba4c7b2c87bde48a` |
| 51 | B5 | `NH_MASTER-7.md` | `6868507ca073051860daadf80554e5e064b8d3d1b293427d28fede746ba135c4` |
| 52 | B5 | `NH_MASTER-6__1_.md` | `3e978e036871c1188400409bfa439380f5cce02e2afd4bbb2830d85b15fe7633` |
| 53 | B5 | `NH_MASTER-6.md` | `63a64d0895e5ee4cebfc9b8a2399356afe1c505ecdf04ca8ee45f2d6079948cc` |
| 54 | B5 | `NH_MASTER-9_2__1_.md` | `052731353b4a221d358133219c5c280aa2e4ada98a1445657aec17b6ce13107e` |
| 55 | B5 | `NH_MASTER-9_2.md` | `052731353b4a221d358133219c5c280aa2e4ada98a1445657aec17b6ce13107e` |
| 56 | B5 | `NH_MASTER-9.md` | `e6bf27a4d4c81ba7e9e9351014397c7668fb1a114f2aa32d6babbaccaae7a813` |
| 57 | B5 | `NH_Build_Checklist.md` | `e4d1436a3e5655ce4b09135c65424a2a672157731441f48f954044aa5d1aea40` |
| 58 | B5 | `NH_Meaning_Engine_Design.md` | `15c2786003463fff73b22dd4bf49cf36df3da30ed27ef57e78663605d2e59a89` |
| 59 | B5 | `NH_Universal_Filter_RULES.md` | `c0fb4528a332f4014782afacee63d167407e31cc88b1502ec8783900588b3a37` |
| 60 | B5 | `nh_architecture_canvas.html` | `971833b6c4b3c6f1c57c094d40d0e3a9b27254087832d29ae46d3338cad90cf2` |
| 61 | B5 | `NH_DECISION_DEFAULTS_ADD__1_.md` | `32b1172159b60afe231f29e132c6c7a39c7eaaf2faf8ced9ec7c7ed473e52bab` |
| 62 | B5 | `NH_DECISION_DEFAULTS_ADD.md` | `32b1172159b60afe231f29e132c6c7a39c7eaaf2faf8ced9ec7c7ed473e52bab` |
| 63 | B5 | `NH_MASTER_section13_ADD.md` | `91d82ed52bcbf497fc12a5c61d479ab5f8fb83f9fc341f878165c446238d68b9` |
| 64 | B5 | `NH_DECISION_DEFAULTS.md` | `2abb2e4570f77a63ef087cfa2fc10cb08210cadb01e9bd304d84d2555249b047` |
| 65 | B5 | `NH_DECISION_DEFAULTS__1_.md` | `45ec88c440456ce7aa99babe8b58ed088786ed342d5197ab4fef8b69d24d3e29` |
| 66 | B6 | `nh_log.py` | `63eaf052295b63b7545cdf44c135a6cdad75d3c57c57d545839f25061b1f8d5e` |
| 67 | B6 | `NH_live_mechanism__1_.html` | `a4465293961004e802cfa660e454d3aa2550bf136a94da5a8b7b2fa163fd7071` |
| 68 | B6 | `NH_MASTER-9_4.md` | `9bbc28dc31c7825d5f3927169526a23bfd0abff9f5a994ce3dc4fd6f7cf1e8dd` |
| 69 | B6 | `NH_live_mechanism.html` | `b329a5e4cf24b8ccbbb13e876da05e5b5542efb8aed2476420e08cbb053d6bb8` |
| 70 | B6 | `NH_live_mechanism_picture__1_.svg` | `4a9bd78d4f49bea70954e91aeeb07f46f135c731b994f439d6e8486bea7cb42b` |
| 71 | B6 | `NH_live_mechanism_picture.svg` | `4a9bd78d4f49bea70954e91aeeb07f46f135c731b994f439d6e8486bea7cb42b` |
| 72 | B6 | `NH_MASTER-9_2__1_.md` | `052731353b4a221d358133219c5c280aa2e4ada98a1445657aec17b6ce13107e` |
| 73 | B6 | `NH_MASTER-10__1_.md` | `f9e783601b1816f797bf82c8bebd70745335b6d5b837a62186c6c6ad6659b804` |
| 74 | B6 | `NH_MASTER-10.md` | `4ee57d298f11a8ad14ea820f157a4c523d4ed16b8532aa14da9cf418ad6fb7d8` |
| 75 | B6 | `NH_MASTER-11.md` | `10771ea4e9cb7a72596efaf0ac52a95d6b7805c215f637ca1e8e3063e050e3ba` |
| 76 | B6 | `nh_probe_truth.py` | `8716a5014c1fbe4215a888e1f4b8249755c2e8f4a9bf23f5c06be764327ce9b9` |
| 77 | B6 | `nh_probe.py` | `2dc08d4e89688b529f468f06348db10e31fcefad1ae0a4dbd5aa5092c18ec6f3` |
| 78 | B6 | `NH_INSIGHT__the_line_under_all_the_lines.md` | `77b5932819a653504cfb1493bf6e9ba94b6c95696a802627cdbdb2589d548ab1` |
| 79 | B6 | `NH_chat_frontdoor_design_sketch__1_.md` | `757b6dd889aedf4af840ecfa190e0404c79ccf609d37607a105dca85f0af0112` |
| 80 | B6 | `NH_chat_frontdoor_design_sketch.md` | `757b6dd889aedf4af840ecfa190e0404c79ccf609d37607a105dca85f0af0112` |
| 81 | B6 | `NH_DECISION_DEFAULTS__1_.md` | `45ec88c440456ce7aa99babe8b58ed088786ed342d5197ab4fef8b69d24d3e29` |
| 82 | B6 | `NH_DECISION_DEFAULTS_ADD__1_.md` | `32b1172159b60afe231f29e132c6c7a39c7eaaf2faf8ced9ec7c7ed473e52bab` |
| 83 | B6 | `NH_DECISION_DEFAULTS_ADD.md` | `32b1172159b60afe231f29e132c6c7a39c7eaaf2faf8ced9ec7c7ed473e52bab` |
| 84 | B6 | `NH_MASTER_section13_ADD.md` | `91d82ed52bcbf497fc12a5c61d479ab5f8fb83f9fc341f878165c446238d68b9` |
| 85 | B6 | `NH_DECISION_DEFAULTS__2_.md` | `11f71f447c17ea48a269adf9c206aa8f23d88a1207ae7388fafb6d9a94004bdc` |
| 86 | B7 | `NH_MASTER-14__4_.md` | `ea4bcbdde17cd2bf802e37259565803ac32ecb9e4ff9120b1a7da579d69bb5ee` |
| 87 | B7 | `NH_MASTER-14__3_.md` | `1dec9fe0cc4fccea1a8951441ca3f6a81b54784712a3ed2da7fb0b56a1e07fd6` |
| 88 | B7 | `NH_MASTER-14__2_.md` | `f9dd9d957d459cb3abb32071338032a0d62c2c9434dce75d68e86ccbbfbbfbb3` |
| 89 | B7 | `NH_MASTER-14__1_.md` | `9a3f2b1eaa63b22c32734252a66d30e0b098ed9dac5686a5952562b43fb10766` |
| 90 | B7 | `NH_MASTER-14.md` | `493f50b8f85516e19b7b566f9603c0b5ce45c36f7a6c4a820a8b3d4a2ae10be4` |
| 91 | B7 | `NH_MASTER-13__1_.md` | `e2c0f9152349e38331c529417ac0638cdd707b09ad6e9f39a69b4aaf3ef8c2ae` |
| 92 | B7 | `NH_MASTER-13.md` | `e2c0f9152349e38331c529417ac0638cdd707b09ad6e9f39a69b4aaf3ef8c2ae` |
| 93 | B7 | `NH_MASTER-11_1.md` | `7270cc48fd9af8afb2b0cb3157cb0549107a3467fa94172afe239367c6e7448c` |
| 94 | B7 | `files__3_.zip` | `a32e34c91ebb986e4fa1ba12bc6397bcdda91266b87f3427aa0e6e08c9543291` |
| 95 | B7 | `NH_DECISION_DEFAULTS-S13__3_.md` | `f6358c44db6e115309e2b1d25a818fe2f02d86a79cea6fefa9daa31bfeead4f1` |
| 96 | B7 | `NH_DECISION_DEFAULTS-S13__2_.md` | `0ff6dd4ce29b7001596db5dd4862fa66d976efe64430653850a735db06f9e2f0` |
| 97 | B7 | `NH_MASTER-14_FINAL.md` | `6dc26159e1862ec96d749581567f74d285490dd515775b77b6fbd7cb53e6f5c3` |
| 98 | B7 | `NH_DECISION_DEFAULTS-S13__1_.md` | `0ff6dd4ce29b7001596db5dd4862fa66d976efe64430653850a735db06f9e2f0` |
| 99 | B7 | `NH_DECISION_DEFAULTS-S13.md` | `eaea2e2ccb3118d50a44d06bda5f12f94bb436ea1cde5411b98370334cd9644a` |
| 100 | B7 | `NH_DECISION_DEFAULTS-S12.md` | `da329e8652ba0f35a4b2d864ade986ca7c61c1324240d84804ffc808c944cfa8` |
| 101 | B7 | `nh_ingest_chatgpt__1_.py` | `b8af9f1d36d93d73bb43daf60786aaa0e36e0313aa85c50b8812d04dd4cb3201` |
| 102 | B7 | `NH_DECISION_DEFAULTS-S10_1.md` | `b018ae48f8863c223a2a345c7747877722e1c6b108bab754c78c9182e774968c` |
| 103 | B7 | `nh_2a_prototype.html` | `b3abcbb47273fefdbcc61f07cbeccc7b0945f981ff770121fbb174271a05f164` |
| 104 | B8 | `NH_DECISION_DEFAULTS-S13__6_.md` | `8acc713871d9c9160143014ebd5823df61df7082fd37ed27e3d20c4b4314f86d` |
| 105 | B8 | `NH_MASTER-14_FINAL__4_.md` | `f632babe53640419ebcd2237d35d5d59cab393531f15a5ac0d18d28e8efba11a` |
| 106 | B8 | `NH_DECISION_DEFAULTS-S13__4_.md` | `8acc713871d9c9160143014ebd5823df61df7082fd37ed27e3d20c4b4314f86d` |
| 107 | B8 | `NH_MASTER-14_FINAL__3_.md` | `55fab7e730cb1f4b320b02411fbca954fc15259d7f13574b661af5d77c3fd720` |
| 108 | B8 | `NH_MASTER-14_FINAL__2_.md` | `55fab7e730cb1f4b320b02411fbca954fc15259d7f13574b661af5d77c3fd720` |
| 109 | B8 | `NH_MASTER-14_FINAL__1_.md` | `6dc26159e1862ec96d749581567f74d285490dd515775b77b6fbd7cb53e6f5c3` |
| 110 | B8 | `NH_DECISION_DEFAULTS-S13__3_.md` | `f6358c44db6e115309e2b1d25a818fe2f02d86a79cea6fefa9daa31bfeead4f1` |
| 111 | B8 | `NH_DECISION_DEFAULTS-S13__2_.md` | `0ff6dd4ce29b7001596db5dd4862fa66d976efe64430653850a735db06f9e2f0` |
| 112 | B8 | `NH_MASTER-14_FINAL.md` | `6dc26159e1862ec96d749581567f74d285490dd515775b77b6fbd7cb53e6f5c3` |
| 113 | B8 | `NH_DECISION_DEFAULTS-S13__1_.md` | `0ff6dd4ce29b7001596db5dd4862fa66d976efe64430653850a735db06f9e2f0` |
| 114 | B8 | `NH_DECISION_DEFAULTS-S13.md` | `eaea2e2ccb3118d50a44d06bda5f12f94bb436ea1cde5411b98370334cd9644a` |
| 115 | B8 | `NH_MASTER-14__4_.md` | `ea4bcbdde17cd2bf802e37259565803ac32ecb9e4ff9120b1a7da579d69bb5ee` |
| 116 | B8 | `NH_MASTER-14__3_.md` | `1dec9fe0cc4fccea1a8951441ca3f6a81b54784712a3ed2da7fb0b56a1e07fd6` |
| 117 | B8 | `NH_MASTER-14__2_.md` | `f9dd9d957d459cb3abb32071338032a0d62c2c9434dce75d68e86ccbbfbbfbb3` |
| 118 | B8 | `NH_MASTER-14__1_.md` | `9a3f2b1eaa63b22c32734252a66d30e0b098ed9dac5686a5952562b43fb10766` |
| 119 | B8 | `NH_MASTER-14.md` | `493f50b8f85516e19b7b566f9603c0b5ce45c36f7a6c4a820a8b3d4a2ae10be4` |
| 120 | B8 | `NH_MASTER-13__1_.md` | `e2c0f9152349e38331c529417ac0638cdd707b09ad6e9f39a69b4aaf3ef8c2ae` |
| 121 | B8 | `NH_DECISION_DEFAULTS-S12.md` | `da329e8652ba0f35a4b2d864ade986ca7c61c1324240d84804ffc808c944cfa8` |
| 122 | B8 | `NH_DECISION_DEFAULTS-S12.md` | `da329e8652ba0f35a4b2d864ade986ca7c61c1324240d84804ffc808c944cfa8` |
| 123 | B9 | `NH_DECISION_DEFAULTS-S13__6_.md` | `8acc713871d9c9160143014ebd5823df61df7082fd37ed27e3d20c4b4314f86d` |
| 124 | B9 | `NH_MASTER-14_FINAL__4_.md` | `f632babe53640419ebcd2237d35d5d59cab393531f15a5ac0d18d28e8efba11a` |
| 125 | B9 | `NH_DECISION_DEFAULTS-S13__4_.md` | `8acc713871d9c9160143014ebd5823df61df7082fd37ed27e3d20c4b4314f86d` |
| 126 | B9 | `NH_MASTER-14_FINAL__3_.md` | `55fab7e730cb1f4b320b02411fbca954fc15259d7f13574b661af5d77c3fd720` |
| 127 | B9 | `NH_MASTER-14_FINAL__2_.md` | `55fab7e730cb1f4b320b02411fbca954fc15259d7f13574b661af5d77c3fd720` |
| 128 | B9 | `NH_MASTER-14_FINAL__1_.md` | `6dc26159e1862ec96d749581567f74d285490dd515775b77b6fbd7cb53e6f5c3` |
| 129 | B9 | `NH_DECISION_DEFAULTS-S13__3_.md` | `f6358c44db6e115309e2b1d25a818fe2f02d86a79cea6fefa9daa31bfeead4f1` |
| 130 | B9 | `NH_DECISION_DEFAULTS-S13__2_.md` | `0ff6dd4ce29b7001596db5dd4862fa66d976efe64430653850a735db06f9e2f0` |
| 131 | B9 | `NH_MASTER-14_FINAL.md` | `6dc26159e1862ec96d749581567f74d285490dd515775b77b6fbd7cb53e6f5c3` |
| 132 | B9 | `NH_DECISION_DEFAULTS-S13__1_.md` | `0ff6dd4ce29b7001596db5dd4862fa66d976efe64430653850a735db06f9e2f0` |
| 133 | B9 | `NH_DECISION_DEFAULTS-S13.md` | `eaea2e2ccb3118d50a44d06bda5f12f94bb436ea1cde5411b98370334cd9644a` |
| 134 | B9 | `NH_MASTER-14__4_.md` | `ea4bcbdde17cd2bf802e37259565803ac32ecb9e4ff9120b1a7da579d69bb5ee` |
| 135 | B9 | `NH_MASTER-14__3_.md` | `1dec9fe0cc4fccea1a8951441ca3f6a81b54784712a3ed2da7fb0b56a1e07fd6` |
| 136 | B9 | `NH_MASTER-14__2_.md` | `f9dd9d957d459cb3abb32071338032a0d62c2c9434dce75d68e86ccbbfbbfbb3` |
| 137 | B9 | `NH_MASTER-14__1_.md` | `9a3f2b1eaa63b22c32734252a66d30e0b098ed9dac5686a5952562b43fb10766` |
| 138 | B9 | `NH_MASTER-14.md` | `493f50b8f85516e19b7b566f9603c0b5ce45c36f7a6c4a820a8b3d4a2ae10be4` |
| 139 | B9 | `NH_DELTA_S14.md` | `f94b5351e56242ce4f1797b417cd482bd25ec5549c73491d218fbdbffa92af9f` |
| 140 | B9 | `NH_CURSOR_BRIEF_reading_validator.md` | `d80065191b04f26d3b0834cd1e861fda68a28d6c61f80d2bd458fce37ac70ba9` |
| 141 | B9 | `NH_DELTA_S14.md` | `f94b5351e56242ce4f1797b417cd482bd25ec5549c73491d218fbdbffa92af9f` |
| 142 | B9 | `NH_CURSOR_BRIEF_reading_validator.md` | `d80065191b04f26d3b0834cd1e861fda68a28d6c61f80d2bd458fce37ac70ba9` |

**Upload Occurrence Ledger row count: 142.**

---

## 4. EXACT-DUPLICATE GROUPS (resident; every filename preserved)

Each group shares one SHA-256. All filenames retained.

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

Plus the ZIP-member duplicates (cross-location): `NH_MASTER-11.1.md` (inside `files__3_.zip`) ≡ loose `NH_MASTER-11_1.md` (`7270cc48fd9af8afb2b0cb3157cb0549107a3467fa94172afe239367c6e7448c`); `NH_DECISION_DEFAULTS-S10.1.md` (inside `files__3_.zip`) ≡ loose `NH_DECISION_DEFAULTS-S10_1.md` (`b018ae48f8863c223a2a345c7747877722e1c6b108bab754c78c9182e774968c`).

---

## 5. PROJECT KNOWLEDGE SOURCES (counted separately from uploads)

These are present in the Project Knowledge folder, NOT attached during Batches 1–9 (except where a byte-identical copy was separately uploaded, noted below). Counted separately.

| Exact Filename | SHA-256 (64 hex) | Bytes | Lines | Notes |
|---|---|---|---|---|
| `NH_DECISION_DEFAULTS-S19_v2_2.md` | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` | 37048 | 314 | ADOPTED AUTHORITATIVE Defaults. Byte-identical to uploaded `NH_DECISION_DEFAULTS-S19_v2_2__1_.md` (B3). |
| `NH_MASTER-19_CORRECTED_v7_1.md` | `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf` | 291811 | 1937 | ADOPTED AUTHORITATIVE Master. Byte-identical to uploaded `NH_MASTER-19_CORRECTED_v7_1__1_.md` (B3). |
| `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | `cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb` | 465376 | 5580 | Project companion governance/archive file. NOT part of the Batch 1–9 upload set; inventoried here directly. |
| `cursorrules__1_` | `5050d08825b93acd72a79d07946e43c8cbe537e079517ccfe66bcae8e30e96e9` | 34821 | 717 | In-force code ruleset. Byte-identical to uploaded `cursorrules__1_` (B3). |

**Project Knowledge row count: 4.**

---

## 6. KNOWN ESSENTIAL SOURCES REQUIRING SUPPLEMENTAL INTAKE

Named as known candidate/recovery sources but NOT physically present in this chat (uploads or Project Knowledge). Their hashes are NOT known and are NOT invented. They require a later supplemental intake before any audit.

| Filename | Class | Hash | Present in chat? | Authority note |
|---|---|---|---|---|
| `NH_MASTER-19_CORRECTED_v8.md` | Candidate / recovery source | UNKNOWN — not supplied | No | Candidate only. Does NOT change authority: v7_1 remains the adopted authoritative Master unless Ness explicitly adopts v8. |
| `NH_DECISION_DEFAULTS-S19_v2_3.md` | Candidate / recovery source | UNKNOWN — not supplied | No | Candidate only. v2_2 remains the adopted Defaults unless Ness explicitly adopts v2_3. |
| `cursorrules_v3_3` | Candidate / recovery source | UNKNOWN — not supplied | No | Candidate ruleset. Current adopted ruleset is the resident `cursorrules__1_` unless Ness explicitly adopts v3_3. |

**Present authority state (unchanged):** Master **v7_1** is the currently adopted authoritative Master; Decision Defaults **v2_2** is the currently adopted Defaults. **v8**, **v2_3**, and **cursorrules_v3_3** remain candidates pending explicit adoption by Ness.

---

## 6B. REFERENCED-BUT-NOT-SUPPLIED SOURCES (named inside supplied files; never provided)

Carried forward unchanged from the v1 manifest so nothing disappears. These are named inside supplied files but were never attached in Batches 1–9 and are not in Project Knowledge. Hashes UNKNOWN — not invented.

**Ingest sources / stores (code-referenced):** `gpt_purified_history.txt`; `cleaned_history (1).txt` (declared damaged / not ingested); `conversations-000.json`; `conversations-001.json`; `conversations-002.json`; `nh_accretive_store.py` (imported by `nh_probe.py`, `nh_ingest_chatgpt.py`, the Cursor brief target); `.nh_accretive_store.jsonl` / `.nh_roots.sealed` / `.nh_readings_store.jsonl` (runtime stores); `ingest_seeds.py`.

**Masters referenced but absent:** `NH_MASTER-9.1`, `NH_MASTER-9.3` (named in 9.4 header), `NH_MASTER-12` (S12 defaults sync to MASTER-13; a 12 was generated), `NH_MASTER-15` (named as DELTA_S14 regen target), `NH_MASTER-16`, `NH_MASTER-19_v7`, `NH_MASTER-19_v2`, `NH_MASTER-19_v4`, `NH_MASTER-19_v5`.

**Gold sets:** `NH_GOLD_SET_v1.md`, `NH_GOLD_SET_v2_B.md`, `NH_GOLD_SET_CONTEXT_v1.md`.

**Other design / handoff docs:** `NH_INTERFACE_WORLD_DESIGN_LOG.md`, `NH_CHATGPT_PROJECT_HANDOFF_CLAUDE_S17.md`, `NH_DECISION_DEFAULTS-S17_DRAFT.md` (distinct from the supplied S17_AUDITED_v1).

**Prototype / output HTML:** `nh_canvas_test.html`, `nh_icon_styles.html`, `nh_log.html` (output of `nh_log.py`).

**Other runtime code named in files:** `nh_sovereignty_sync.py`, `nh_service.py`, `nh_peek.py`, `nh_clinical_report.py`, `nh_lawyer_simulator.py`, `nh_nightly.py`, `nh_vector_memory.py`, `test_brave.py`.

---

## 7. RELATED-VERSION (NEAR-DUPLICATE) FAMILIES — flagged for later diff; NO WINNER CHOSEN

Distinct hashes requiring line-by-line comparison later. None judged more complete now.

- **Universal Filter Design (3 tiers):** `3df666eb4ff4d90e5a5a299f7f7d52361638a27feb1e727894f0e0658c421020` (bare, no Keystone/Membrane) → `7dce7058c991dc1aeb583e7455234a6721c7fea089626fcccecf529f5b48b1c7` (+Keystone) → `c8938d370efdd072912cabb4adf844dba4cc581095d68fca7022cff30710be15` (+Keystone +MEMBRANE). Membrane design section exists ONLY in the third.
- **Meaning Engine Design:** resident `15c2786003463fff73b22dd4bf49cf36df3da30ed27ef57e78663605d2e59a89` (B5) vs the Batch-1 copy `18185908fecd4a2a00587a57fc10437f5e5a6003731ec61d4d7f39e37dcf0d62` (separator-formatting variant; B1 copy overwritten on disk by the B5 re-upload of a different body — see Validation Errors §9).
- **Risk review:** `3864a2eb1a8f97bf433bd7ebaf0a9d4d85ba6e09bbd26c9c39d1371d5fe6d598` (bare) vs `6fa53662b406edb1b410d56bb43560027fb7a7d6f9042db5233a6b5f60f710c7` (+boot-error/silent-auto-start resolution).
- **MASTER_FILE_COMPLETE:** `80a6143e9857ee77e9cf75ebd1c55724938f23bd04aae8b9b761160171bfcd02` (156 lines) vs `06f69672fa89800f060c70864bf1fd87532aff4359f3e538c48b087f08d8daed` (257 lines).
- **MASTER-6:** `63a64d0895e5ee4cebfc9b8a2399356afe1c505ecdf04ca8ee45f2d6079948cc` (273L) vs `3e978e036871c1188400409bfa439380f5cce02e2afd4bbb2830d85b15fe7633` (315L).
- **MASTER-9 / 9_2:** `e6bf27a4d4c81ba7e9e9351014397c7668fb1a114f2aa32d6babbaccaae7a813` (442L) vs `052731353b4a221d358133219c5c280aa2e4ada98a1445657aec17b6ce13107e` (513L).
- **MASTER-10:** `4ee57d298f11a8ad14ea820f157a4c523d4ed16b8532aa14da9cf418ad6fb7d8` (406L) vs `f9e783601b1816f797bf82c8bebd70745335b6d5b837a62186c6c6ad6659b804` (407L).
- **MASTER-14 family (5 distinct bodies):** `493f50b8f85516e19b7b566f9603c0b5ce45c36f7a6c4a820a8b3d4a2ae10be4` (340L) · `9a3f2b1eaa63b22c32734252a66d30e0b098ed9dac5686a5952562b43fb10766` (379L) · `f9dd9d957d459cb3abb32071338032a0d62c2c9434dce75d68e86ccbbfbbfbb3` (379L) · `1dec9fe0cc4fccea1a8951441ca3f6a81b54784712a3ed2da7fb0b56a1e07fd6` (389L) · `ea4bcbdde17cd2bf802e37259565803ac32ecb9e4ff9120b1a7da579d69bb5ee` (389L).
- **MASTER-14_FINAL family (3 distinct bodies):** `6dc26159e1862ec96d749581567f74d285490dd515775b77b6fbd7cb53e6f5c3` (427L) · `55fab7e730cb1f4b320b02411fbca954fc15259d7f13574b661af5d77c3fd720` (434L) · `f632babe53640419ebcd2237d35d5d59cab393531f15a5ac0d18d28e8efba11a` (434L).
- **DD-S13 family (4 distinct bodies):** `eaea2e2ccb3118d50a44d06bda5f12f94bb436ea1cde5411b98370334cd9644a` (121L) · `0ff6dd4ce29b7001596db5dd4862fa66d976efe64430653850a735db06f9e2f0` (123L) · `f6358c44db6e115309e2b1d25a818fe2f02d86a79cea6fefa9daa31bfeead4f1` (124L) · `8acc713871d9c9160143014ebd5823df61df7082fd37ed27e3d20c4b4314f86d` (125L).
- **Live-mechanism HTML:** `b329a5e4cf24b8ccbbb13e876da05e5b5542efb8aed2476420e08cbb053d6bb8` (316L) vs `a4465293961004e802cfa660e454d3aa2550bf136a94da5a8b7b2fa163fd7071` (332L).
- **MASTER-19 lineage:** `0287015be938212d8065e5f2d3ac9b952a1f8943a043864ef63614d1670beffb` (v1) → `e38c37e97491d7f13310fb9d5d961e86111aad9c917612ccb3ea12e27e127a7b` (v3) → `8165f4bed94d2d57140d49e93d3c85b8e2b259053e0b30ac4c675fa7463a1bf9` (v6) → `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf` (v7_1), plus `bc498fda2fea592fbb08fd7d1b1ded23f13d8522bfb1f2dc324095df5259caec` (FULL) and the four reader slices.
- **Decision Defaults early lineage:** `2abb2e4570f77a63ef087cfa2fc10cb08210cadb01e9bd304d84d2555249b047` (bare) → `45ec88c440456ce7aa99babe8b58ed088786ed342d5197ab4fef8b69d24d3e29` (+compass) → `11f71f447c17ea48a269adf9c206aa8f23d88a1207ae7388fafb6d9a94004bdc` (session-9).

---

## 8. CURRENTLY EVIDENCED MASTER CHRONOLOGY & AUTHORITY HISTORY (chronology only — NOT a completeness ranking)

**Master numeric lineage:** MASTER-5 (session 2) → 6 (two copies) → 7 → 8 → 9 → 9_2 → 9_4 (session 8: +§13, +§14 sketch) → 10 (session 9: +§0 premise; reality reworked) → 11 (session 10: reality→STORY) → 11.1 (session 10 eve: +§0A DUMB/SMART, 2a shape) → [12 MISSING] → 13 → 14 family (8 bodies incl. 3 FINAL sub-versions) → [DELTA_S14 + Cursor brief: post-14, pre-15] → [15, 16 MISSING] → 17_FULL_v2 (+4 reader slices) → 18_FULL_v1 → 19_FULL → 19_v1 → 19_v3 → 19_v6 → 19_v7_1 (ADOPTED AUTHORITATIVE).

**Parallel early family:** `NH_MASTER_FILE_COMPLETE` (156L) and standalone (257L) sit around the Master-5/6 era.

**Decision Defaults lineage:** bare → +compass → session-9 → S10.1 → S12 → S13 family (4 bodies) → [S17_AUDITED_v1; S17_DRAFT missing] → S19_v1 → S19_v2_2 (ADOPTED AUTHORITATIVE).

**Authority state (declared, not re-judged):** Authoritative pair = `NH_MASTER-19_CORRECTED_v7_1.md` + `NH_DECISION_DEFAULTS-S19_v2_2.md`, governed by `cursorrules`. `NH_MASTER-19_CORRECTED_v6` is declared predecessor. The two accepted-design companions (SECURITY_IDENTITY_AFTER_BGMM, TSC_DESIGN_v1) declare themselves NOT-yet-patched into the Master. Candidates v8 / v2_3 / cursorrules_v3_3 are NOT present and NOT adopted (see §6).

---

## 9. VALIDATION ERRORS & SURFACED MISMATCHES (not silently corrected)

- **`NH_MASTER-19_CORRECTED_v3.md` hash:** The Batch-1 *receipt* recorded the full correct hash `e38c37e97491d7f13310fb9d5d961e86111aad9c917612ccb3ea12e27e127a7b`, which matches the disk exactly. The FIRST manifest (v1) displayed it abbreviated as e38c37e9…a7be (shown here without backticks as it is a quoted artifact, not a ledger hash) with a footnote — that abbreviation was a display artifact in the v1 manifest, not an error in the original receipt. Corrected here to the full 64-char hash. No underlying data was wrong.
- **Meaning Engine Design B1 vs B5:** Two different bodies were uploaded under the same filename `NH_Meaning_Engine_Design.md` — B1 body `18185908fecd4a2a00587a57fc10437f5e5a6003731ec61d4d7f39e37dcf0d62` (12,474 B / 137 lines) and B5 body `15c2786003463fff73b22dd4bf49cf36df3da30ed27ef57e78663605d2e59a89` (12,479 B / 138 lines). The later upload overwrote the earlier on the deduplicated filesystem, so only the B5 body is resident. The B1 body's full hash is preserved in the Batch-1 receipt; it is recorded here as a related-version that is no longer resident. This is surfaced, not silently resolved.
- **Occurrence-count correction:** v1 manifest stated 133 occurrences; corrected to 142 (see §1). Surfaced, not hidden.
- **No other mismatches were found or silently corrected.**

---

## 10. WHAT HAS NOT BEEN DONE (explicit)

No full Master comparison · no feature-recovery audit · no Feature Recovery and Decision Ledger · no restoration · no reconciliation · no rewriting · no consolidation · no final self-contained Master · no Decision-Defaults regeneration · no adoption of any candidate · no overwrite of any prior Master or the v1 manifest. Provenance only.

---

*Corrected manifest v2. Upload occurrences: 142 across 9 batches. Resident filenames: 100. Unique content hashes: 86. Project Knowledge files: 4 (separate). Unreadable: 0. Every duplicate and occurrence retained.*
