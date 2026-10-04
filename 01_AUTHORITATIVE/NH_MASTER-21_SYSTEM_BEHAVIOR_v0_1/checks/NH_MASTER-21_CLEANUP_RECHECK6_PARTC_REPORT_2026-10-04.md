# Master-21 cleanup v7 — targeted independent re-check 6, Part C

**Verdict: PASS.** Stages 0–5 completed. **RECHECK5-PARTC-001 is FIXED in all 46 occurrences. No new findings:** zero must-fix, zero should-fix and zero newly identified notes. The FINDINGS file contains the empty JSON array `[]`.

Date: 2026-10-04. Scope: CH09-a–CH12-e, 20 chapters. Governing brief: `NH_MASTER-21_CLEANUP_CHECK_BRIEF_v7_2026-10-04.md`, retaining the v6 pointer rule, v4.1 decision B, v3 rules, contract v1_0 and lessons v0_4. D1, D2, Q1=A, Q3=B, back-links=A and R1=A remain in force. Per-chapter totals remain notes only under decision B; local registers remain must-pass. No source chapter or cleanup record was modified.

## Stage results

| Stage | Result | Independent evidence |
| --- | --- | --- |
| 0 — fingerprints | PASS | All three archive SHA-256 values match the request. The Stage 1 JSON exactly matches the previously delivered findings. All 132 v6/v7 chapter identities match the record, and all 12 changed-chapter pairs match brief v7. |
| 1 — prior finding | PASS | All 46 occurrences of RECHECK5-PARTC-001 now point at the previously specified and independently recomputed required line. The 46 record pointer edits are exactly the 46 prior rows, with no missing or extra repair. |
| 2 — replay | PASS | Applying all 46 body edits in record order reproduces all 61 v7 body chapters byte for byte. Each appendix differs only in seven correct chapter-fingerprint rows: 35 fingerprint replacements in total. The five appendix before/after record hashes match. No chapter line count changes. |
| 3 — every v7 change | PASS | Each pointer edit changes only its line number. All 416 named-review rows and all 22 card-based source-literal exception rows follow the v6 rule, including unchanged rows. Zero outside-card, wrong-field, wrong-first-TOGETHER or wrong-occurrence reference remains. |
| 4 — registers / structure | PASS | All local gap and review classifications match their files; the 17 plain_together rows still describe populated plain fields. All 2,755 Part C cards have the required ordered field labels, USED BY numbering is consecutive, status/citation syntax passes and all four JSON blocks parse. All appendix entries and locators recompute; 305 input fingerprints match. |
| 5 — links | PASS | No card-owned line changes from v6. All 4,558 named Part C card uses are answered: 4,505 directly and 53 by direction-correct continuations. All 5,266 relationship occurrences touching Part C have reciprocal card rows. All 87 owned path-use continuation rows match direction and path step. |

## Stage 0 — exact inputs and chapter identities

| Input | SHA-256 |
| --- | --- |
| NH_MASTER-21_CLEANUP_FIXED_CHAPTERS_v7_2026-10-04.zip | `3e9fe1c35e1691096e79c24886ce4463288941d27301533019c55fbe38bd37b5` |
| NH_MASTER-21_CLEANUP_RECHECK_KIT_v7_2026-10-04.zip | `fb626d2f78f944eba918f3a7c9d78595e694bd0efdaceb569907212b440dcab8` |
| NH_MASTER-21_CLEANUP_FIXED_CHAPTERS_v6_2026-10-04.zip | `9b1ca5d900f4c9ff0b4c751edd1cb9d2130191f0353eeb42f122299de0e38d35` |
| NH_MASTER-21_CLEANUP_RECHECK5_PARTC_FINDINGS_2026-10-04.json | `c78eeb47b243d87efc5218c889b1a0ec95c6dabe29fd64452a5e77c8104a196d` |

The v6, v4.1 and v3 briefs, contract and lessons in this kit are byte-identical to the previously read governing copies. Contract SHA-256: `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1`. Source pin: `6a7160ba688ba4e433a31899162815df7e2bab17`. The preserved complete source-tree object has that identity; all 13 locally preserved source copies used for the reconstruction still match their pinned Git blob identities.

| Chapter | v6 SHA-256 | v7 SHA-256 | v7 items | Result |
| --- | --- | --- | --- | --- |
| CH09-a | `ab86b82b67c63f61454f20aad99f4fda74f3cb1e8d8af0d6f816f94bb678347b` | `f451c47b7b09d6285c251a595a06d69fdc0af4d3c779e5df973bfdf0deecf9f4` | 1 | PASS |
| CH09-b | `283706c41b3d9e18751a24ee20f2406b52f9af043e675d1f838542a47aeb2f2d` | `b3cf98fa9ba312ad2d402802de9960438769c9290e03ae80c4efdc1fc137a739` | 3 | PASS |
| CH09-c | `b9b9d850cdf0167c72fb95c11334f67ac04cef4a31d56724ce744ead53993126` | `b9b9d850cdf0167c72fb95c11334f67ac04cef4a31d56724ce744ead53993126` | 0 | PASS |
| CH09-d | `69fe3bd8d18d16993b39713aea379ecea9b1d47b0409929d9712352262263743` | `69fe3bd8d18d16993b39713aea379ecea9b1d47b0409929d9712352262263743` | 0 | PASS |
| CH09-e | `28bd602f1846f313cdb4c3bde5eafa980b60dba29ce4408d5a1e7288948c73f8` | `28bd602f1846f313cdb4c3bde5eafa980b60dba29ce4408d5a1e7288948c73f8` | 0 | PASS |
| CH09-f | `3b125f6143b829211667113b51b12a35ddaa37c4624f9630b68932946b020059` | `9e80c078a30d37dcea40c5d4024cebb0f08fcdad0ac747373d528a19f12c9cd6` | 3 | PASS |
| CH09-g | `a4861468f9182c2f829711c5f8c1c2544813f82fa0b423ead9d642f73b77dced` | `a4861468f9182c2f829711c5f8c1c2544813f82fa0b423ead9d642f73b77dced` | 0 | PASS |
| CH09-h | `96ecfc604372812a53a76bac829f79ae861f8923a6bd1f57db3430bf49a5ba7f` | `229de6895db7e8fd96112073fa557bdd9dc7f301c659bd7a2a82ba6536b6b993` | 8 | PASS |
| CH09-i | `4f707f000c575ea1a8bf818de7c27d4db15718e4de506180d8eba49879dcacc8` | `4f707f000c575ea1a8bf818de7c27d4db15718e4de506180d8eba49879dcacc8` | 0 | PASS |
| CH10-a | `7888db915ea59899e6184240845671bc96d267e7614107da7d07fce624994ac9` | `7888db915ea59899e6184240845671bc96d267e7614107da7d07fce624994ac9` | 0 | PASS |
| CH10-b | `7cc97074f212e29b674a6de7dbc71149836641fd04a4225218a12bb1f94354ae` | `7cc97074f212e29b674a6de7dbc71149836641fd04a4225218a12bb1f94354ae` | 0 | PASS |
| CH10-c | `2b34e45d3591c283b574f9122b16a5d87791aee3e6fe879e8b2bd55e3c578a48` | `33a26651b2e31733d270c04abfdf21d02ba8623a2a6a09db847309a3cd537dff` | 7 | PASS |
| CH10-d | `30b6f7b5810f30450880a934112033261c5fe63739d5b2504724604344558997` | `6b731de81a7c8f913b143294ba8b68a76d48af9f03c91f2c01b42d12af8bcdd7` | 2 | PASS |
| CH10-e | `ae2a0266d1ee9e49d4cccef71dfe246ee75892913e88428676a88c6eece4262a` | `813b64e52c1b856fe43df9d7fb36b6d218312db5462fb735400e72f56ab3ae92` | 22 | PASS |
| CH11 | `0a6b2e3602ec4d3924967385d9242332b436bbb76ac421f48a1261f5522ae3c8` | `0a6b2e3602ec4d3924967385d9242332b436bbb76ac421f48a1261f5522ae3c8` | 0 | PASS |
| CH12-a | `7b2a62203b75dff9dc83eb00cacc9701b5b83b72eca4698edfbab70bc19a236f` | `6e8eaf8816673cb007bc36b82045a6e33a86e0e94d6548d2cf69c77482ec619f` | 1 | PASS |
| CH12-b | `b107e569a357847cb0fff9e9a08d1ca0566d3162de2002f88dfd13e65030a373` | `5b2181e411417b531ad81f3db1f5d98861bdbe27c2839c0da5f134bde0677bd2` | 1 | PASS |
| CH12-c | `e88001c5e20529e198171adf7bfb5ec57cc6086410a4ccd980ee46c9c7280dc7` | `640043e45771a9211035eacfad5d9a11669e10fbef48d6f3ddf37b5c4dc92df5` | 1 | PASS |
| CH12-d | `b8b3e9f5382e17916a60b543db0d4ae6d4a7423b6a4c962eea5d71c9cce5fbd9` | `6eda8e8c44be0bb2d6e6cd0bda66a0e064190f6d8085bfc175341d242aa3340e` | 1 | PASS |
| CH12-e | `0774d0fd9d26e73bfe6914e6951672786b333121cb3cd2f35b4246cd668a0625` | `8b8c4e523582d4a2703e3d37fb35e808a9c38d929c38fb3c13260f9bbf88e6d5` | 1 | PASS |

Exactly twelve chapters change: seven Part C body chapters and five appendices. The other 54 chapters are byte-identical to v6, including all Part A and B chapters. All 66 chapter line counts are unchanged.

## Stage 1 — disposition and all 46 repaired occurrences

| Prior finding | Disposition | Result |
| --- | --- | --- |
| RECHECK5-PARTC-001 | FIXED | 46 of 46 references match both the prior required line and an independent application of the pointer rule to v7. All were changed only at the printed line number. |

| v7 item | Register row | Card | v6 pointer | v7 / required line | Result |
| --- | --- | --- | --- | --- | --- |
| R5-10437 | CH09-a:522 | C-WIS-SEP | 16 | 28 | FIXED |
| R5-10438 | CH09-b:983 | C-OTHER.1 | 47 | 56 | FIXED |
| R5-10439 | CH09-b:984 | C-OTHER.3 | 93 | 106 | FIXED |
| R5-10440 | CH09-b:985 | C-OTHER.7 | 280 | 293 | FIXED |
| R5-10441 | CH09-f:3843 | C-BGMM.1 | 52 | 64 | FIXED |
| R5-10442 | CH09-f:3844 | C-BGMM.1 | 52 | 65 | FIXED |
| R5-10443 | CH09-f:3845 | C-BGMM.2 | 75 | 88 | FIXED |
| R5-10444 | CH09-h:5264 | C-ENROLL.2 | 86 | 101 | FIXED |
| R5-10445 | CH09-h:5265 | C-ENROLL.2.2 | 142 | 155 | FIXED |
| R5-10446 | CH09-h:5266 | C-ENROLL.2.3 | 165 | 178 | FIXED |
| R5-10447 | CH09-h:5267 | C-ENROLL.3.1 | 521 | 534 | FIXED |
| R5-10448 | CH09-h:5268 | C-ENROLL.3.3 | 575 | 588 | FIXED |
| R5-10449 | CH09-h:5269 | C-ENROLL.4.3 | 724 | 737 | FIXED |
| R5-10450 | CH09-h:5270 | C-ENROLL.4.5 | 1033 | 1046 | FIXED |
| R5-10451 | CH09-h:5271 | C-ENROLL.4.6 | 1240 | 1253 | FIXED |
| R5-10452 | CH10-c:1363 | C-22.4.1 | 345 | 357 | FIXED |
| R5-10453 | CH10-c:1364 | C-22.5.1 | 395 | 404 | FIXED |
| R5-10454 | CH10-c:1365 | C-22.5.3 | 439 | 448 | FIXED |
| R5-10455 | CH10-c:1366 | C-22.6.5 | 627 | 639 | FIXED |
| R5-10456 | CH10-c:1367 | C-22.9.2 | 792 | 804 | FIXED |
| R5-10457 | CH10-c:1368 | C-22.9.4 | 836 | 848 | FIXED |
| R5-10458 | CH10-c:1369 | C-22.13.3 | 1128 | 1139 | FIXED |
| R5-10459 | CH10-d:1014 | C-23.5.1 | 318 | 331 | FIXED |
| R5-10460 | CH10-d:1015 | C-23.6.2 | 430 | 443 | FIXED |
| R5-10461 | CH10-e:10449 | C-19.2.3 | 391 | 390 | FIXED |
| R5-10462 | CH10-e:10450 | C-19.8 | 730 | 728 | FIXED |
| R5-10463 | CH10-e:10451 | C-19.10.1 | 842 | 840 | FIXED |
| R5-10464 | CH10-e:10452 | C-19.14 | 1094 | 1104 | FIXED |
| R5-10465 | CH10-e:10453 | C-19.14.1 | 1116 | 1126 | FIXED |
| R5-10466 | CH10-e:10454 | C-19.14.2 | 1138 | 1148 | FIXED |
| R5-10467 | CH10-e:10455 | C-19.14.3 | 1160 | 1170 | FIXED |
| R5-10468 | CH10-e:10456 | C-19.14.4 | 1182 | 1192 | FIXED |
| R5-10469 | CH10-e:10457 | C-19.14.5 | 1204 | 1214 | FIXED |
| R5-10470 | CH10-e:10458 | C-19.14.6 | 1226 | 1236 | FIXED |
| R5-10471 | CH10-e:10459 | C-19.14.7 | 1248 | 1258 | FIXED |
| R5-10472 | CH10-e:10460 | C-19.15.7 | 1432 | 1442 | FIXED |
| R5-10473 | CH10-e:10461 | C-19.16.7 | 1615 | 1622 | FIXED |
| R5-10474 | CH10-e:10462 | C-19.16.8 | 1637 | 1644 | FIXED |
| R5-10475 | CH10-e:10463 | C-19.16.10 | 1682 | 1689 | FIXED |
| R5-10476 | CH10-e:10464 | C-19.17.14 | 2044 | 2037 | FIXED |
| R5-10477 | CH10-e:10465 | C-19.17.18.1 | 2168 | 2161 | FIXED |
| R5-10478 | CH10-e:10466 | C-19.17.18.2 | 2190 | 2183 | FIXED |
| R5-10479 | CH10-e:10467 | C-19.17.18.4 | 2234 | 2227 | FIXED |
| R5-10480 | CH10-e:10468 | C-19.17.23 | 2380 | 2385 | FIXED |
| R5-10481 | CH10-e:10469 | C-19.17.24 | 2402 | 2407 | FIXED |
| R5-10482 | CH10-e:10471 | C-19.19.3.1 | 2897 | 2895 | FIXED |

The Stage 1 list contains one finding, with 46 occurrences. Every listed occurrence was checked; none was waived or deferred. The v7 record names exactly the same set of chapter/row locations.

## Stage 2 — replay and appendix-only fingerprint refresh

The record contains 51 consecutive items, R5-10437–R5-10487: 46 FIX_REGISTER_POINTER and five REGENERATE_APPENDIX. Every body item’s before value matches the supplied v6 file, and the resulting files match v7 byte for byte. There are no inserted, removed, unrecorded or unexplained body lines.

| Changed body chapter | Pointer edits | Replay |
| --- | --- | --- |
| CH09-a | 1 | PASS |
| CH09-b | 3 | PASS |
| CH09-f | 3 | PASS |
| CH09-h | 8 | PASS |
| CH10-c | 7 | PASS |
| CH10-d | 2 | PASS |
| CH10-e | 22 | PASS |

For each appendix, every differing line was required to retain the same chapter ID and exact filename and to replace only the input SHA-256 with the recomputed v7 value. All seven changed input chapters occur exactly once in each appendix. No other appendix byte changes.

| Appendix | Record item | Changed fingerprint rows | Other changes | Result |
| --- | --- | --- | --- | --- |
| CH12-a | R5-10483 | 7 | 0 | PASS |
| CH12-b | R5-10484 | 7 | 0 | PASS |
| CH12-c | R5-10485 | 7 | 0 | PASS |
| CH12-d | R5-10486 | 7 | 0 | PASS |
| CH12-e | R5-10487 | 7 | 0 | PASS |

The seven refreshed inputs are CH09-a, CH09-b, CH09-f, CH09-h, CH10-c, CH10-d and CH10-e. Gap text, citation text, conflict text, locations, row order and all appendix data tables are preserved exactly from v6.

## Stage 3 — pointer rule applied to every row

Card IDs and field lines were parsed from the current chapters. For a `<flag> / <field>` row, the selected line is the one naming a card named in the reason, otherwise the first line of that field. For empty_together it is the first TOGETHER field. Literal exception occurrences are assigned in reading order within the full card, including headings and SUB-PARTS. Distinct occurrences on the same line retain separate character positions.

| Chapter | Named-review rows | Card exception rows | Following the rule |
| --- | --- | --- | --- |
| CH09-a | 7 | 0 | 7 |
| CH09-b | 3 | 0 | 3 |
| CH09-c | 10 | 0 | 10 |
| CH09-d | 106 | 0 | 106 |
| CH09-e | 47 | 0 | 47 |
| CH09-f | 29 | 0 | 29 |
| CH09-g | 15 | 0 | 15 |
| CH09-h | 26 | 0 | 26 |
| CH09-i | 13 | 0 | 13 |
| CH10-a | 4 | 0 | 4 |
| CH10-b | 85 | 0 | 85 |
| CH10-c | 7 | 0 | 7 |
| CH10-d | 10 | 0 | 10 |
| CH10-e | 44 | 22 | 66 |
| CH11 | 10 | 0 | 10 |

All **438** card-based rows pass: 416 named-review rows and 22 exception rows. The separate CH11 path exception at register line 13100 still identifies P-NEW-capture step 1 at line 265. All names, flags and reasons remain unchanged by v7.

CH09-b:985 now points to Gated by at line 293, the first line of that field, as the rule requires when the reason selects no named-card line. Its second Gated by line retains the plain personal-authorization condition, so the plain_together classification remains valid. The two previously reclassified rows remain correct: C-BGMM.6.5 points at 1151 and C-19.18.7 at 2597, each describing its existing named gates.

The 22 source-literal exception assignments are unchanged and all still pass. In particular, C-19.16’s workflow tokens 4–8 resolve to 1458, 1460, 1472, 1472 and 1476; its fifth ChatGPT occurrence is on the SUB-PARTS line. Repeated line numbers refer to different occurrences, not duplicate claims on one token.

## Stage 4 — local registers, structure and appendices

All 6,140 Part C empty card fields have local register entries. No missing field entry, duplicate field entry, or stale entry for a filled field was found. All review classifications match: 178 empty_together; 48 prerequisite_review / Fails closed by; 163 prerequisite_review / Gated by; 10 prerequisite_review / Must never; and 17 plain_together / Gated by. Every empty_together card has empty TOGETHER fields, and each plain_together row has a populated plain line in its named field.

All 2,755 Part C cards retain the nine field labels in order, allowing repeated labels. USED BY numbering is consecutive; all populated card fields have valid leading status stamps and source citations; no repeated status stamp remains after quoted source headings are excluded; no card lists itself as a sub-part. The JSON blocks in CH10-b, CH10-c, CH10-d and CH10-e all parse. Decision B remains in force; no new Part C total discrepancy was identified.

| Appendix | Result | Independent check |
| --- | --- | --- |
| A | PASS | 26,865 unique gap locations: 24,786 part fields (including 22 partial), 707 wholly empty USED BY tables, 847 use cells, 17 continuation cells, 72 path fields and 436 additional/named details. All copied values resolve to their indicated line/cell; no card gap or empty use cell is missing. All 24,788 card/field reference checks match; 26,137 local-register locations are linked. |
| B | PASS | 1,233 pinned Stage 2 ledger rows contain 87 DROPPED + 51 COMPRESSED + 20 CONTRADICTED = 158 eligible rows. Subtract 138 bucket-covered IDs and DR FR-0094/0103/0104: the remaining 17 pending CONTRADICTED IDs and exact titles match. |
| C | PASS | All seven inactive-file slots match the pinned tree and chapter inventory locations; all five explicit INTENT slots match their current text and lines. All 33 literal INTENT lines and all five meaning-web exception locations remain accounted for. |
| D | PASS | All 163 marked conflict-line occurrences match exactly (160 distinct texts), as do all six separately indexed unmarked local-register rows. No missing or extra marked line. |
| E | PASS | All 145 READ-file paths/Git blobs, 12 extra cited files, 107 literal V10 headings, 39 extra V10 anchors, 292 continuation sections (5,226 nonempty lines) and 21 CH00 rows match. All 20 explicit landing-method owner sets and all 24 landing locations match, including the C-9.3 phone-mode scope. |

All **305** appendix input fingerprints match v7. The chapter extraction still contains 321,144 lines under the appendices’ split-on-newline convention, including the terminal empty segment of each body file. Source-citation occurrences remain 136,225; 11,412 occur within the indexed continuation ranges. Independent reconstruction agrees with the unchanged appendix content, in addition to the exact fingerprint-only comparison. The writer’s appendix scripts were not used to establish these results.

## Stage 5 — preserved card content and links

Every card-owned line is byte-identical to v6, including headings, stamp/source lines, behavior fields, USED BY rows and SUB-PARTS. The link scan confirms all 5,266 named TOGETHER relationship occurrences touching Part C have reciprocal card rows. All 4,558 named Part C card uses are answered by the using endpoint: 4,505 directly and 53 by direction-correct continuations. Opposite-role continuations are not credited. The 87 explicit path-use continuation rows owned by Part C cards match both direction and path step.

All 2,755 Part C cards remain in the canonical part-to-path placement index, which contains all 9,392 cards exactly once. No new used-in name mismatch or multiple-path-in-one-row issue was found. The two retained coarse stamp/header comparisons at CH10-d:54 and 56 are supported by the using cards’ actual ACCEPTED fields and own accepted sources, as in the prior check.

## Scope and retained decisions

This is the requested targeted cleanup check, not a new whole-design audit or adoption decision. The record’s existing not_done items and Part B totals deferred to the join were not reopened. The older BUILT assertions, accepted Changes-link wording, CH03-c’s older landing-map layout and the separate joining-tool locator routine remain as already recorded. None is a new v7 finding.

No open finding remains in this Part C re-check. The accompanying FINDINGS JSON is `[]`; the prior finding’s complete repair evidence is recorded above. Acceptance and adoption remain with Ness.

