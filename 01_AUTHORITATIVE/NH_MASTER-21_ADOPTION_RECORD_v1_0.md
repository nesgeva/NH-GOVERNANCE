# NH_MASTER-21 — Adoption record, v1_0

**Status:** a record of an adoption made by Ness. It adds no decision of its own. Where it differs from Ness's own words, his words win.

**Frozen bytes:** the adopted files keep their internal wording and their names, including "Status: CANDIDATE" inside and "_CANDIDATE" in the book's name. The adoption lives in this record, not inside them.

## 1. The adoption

| | |
|---|---|
| By | Ness |
| When | 2026-10-05, shortly after 00:25 Israel time (2026-10-04, after 21:25 UTC), right after the final re-check passed |
| His words | "adopting indeed i adopt nh master 21" |
| Context | Claude had just verified the re-check PASS. It had named the joined book `C:\Users\user\Downloads\MASTER21_JOIN\out_v3\NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE.md` as Master-21 and Ness's adoption as the next step. |

## 2. Exactly what is adopted

| Item | Identity |
|---|---|
| **Master-21**, the joined book `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE.md` | SHA-256 `8d7c929c5715bb8138644f2a0a7513a89e4f98d98c6f0f05e068284f4cc5ed0d`; 44,986,552 bytes; 361,508 LF lines; 0 CR bytes |
| Its 66 source chapters (cleanup set v8) | each listed with its SHA-256 in §6; together in `NH_MASTER-21_CLEANUP_FIXED_CHAPTERS_v8_2026-10-04.zip`, SHA-256 `43957c01343121773ab5304a71471a2af84d8889eb3f9c33d568747eb4a40ef8` |
| The tool that joined them | `nh_master21_assemble_v3.py`, SHA-256 `81195e8eb4c1a31d8af14216e36f2e896432c47296be65315c46d031d91d50bc` |

Running assembler v3 on the 66 chapters reproduces the book byte for byte. This was shown twice:
- on Ness's PC (2026-10-04 21:02 UTC);
- independently by the re-checker (stage R1).

## 3. Evidence: every check passed

| Step | File(s) | SHA-256 | Result |
|---|---|---|---|
| Cleanup round 5 | `NH_MASTER-21_CLEANUP_ROUND_PASSED_RECORD_v1_2026-10-04.md` | `75b1acd6580d4afe7510e8605ab788568ac30ab5df00a4590af9babad7c06b76` (1) | PASSED. Part A ran on v4, Part B on v5 and Part C on v7; A's and B's chapters are byte-identical in v7, so all 66 passed in v7 form. |
| Passed cleanup set v7 | `NH_MASTER-21_CLEANUP_FIXED_CHAPTERS_v7_2026-10-04.zip` | `3e9fe1c35e1691096e79c24886ce4463288941d27301533019c55fbe38bd37b5` | the set the cleanup round passed |
| Set v8 | v7 plus two recorded wording fixes (CH05-a, CH05-b) and refreshed appendix fingerprints | v8 zip, above | replayed and confirmed by the final check (Stage 1) |
| Final check brief | `NH_MASTER-21_FINAL_CHECK_BRIEF_v1_2026-10-04.md` | `d387ad922f2843a460a0733b2fa1d447148cf46719355a4375a263493ee5c067` | — |
| Final check of the v2 join | `NH_MASTER-21_FINAL_CHECK_REPORT_v1_2026-10-04.md`, `NH_MASTER-21_FINAL_CHECK_FINDINGS_v1_2026-10-04.json` | `4d23ab8f1459b5c8278d8a088c92bbe08cd837b728bb46e53d7cb21a9d70f0f7`, `a4473428174acb1456813093a94c2dfce4cb0f87f289afbd2696bacb540e3795` | FAIL on two tool findings (NH21-FINAL-001 minor, NH21-FINAL-002 major); no chapter-content findings |
| Assembler v3 | `nh_master21_assemble_v3.py` | `81195e8eb4c1a31d8af14216e36f2e896432c47296be65315c46d031d91d50bc` | fixes both findings and changes nothing else |
| Re-check brief | `NH_MASTER-21_FINAL_RECHECK_BRIEF_v1_2026-10-04.md` | `91a3aa8febdfd87bf925235bb5aaab12d0fd24167b6eb0c0c824f8f6e2d2e5eb` | — |
| Re-check of the v3 join | `NH_MASTER-21_FINAL_RECHECK_REPORT_v1_2026-10-04.md`, `NH_MASTER-21_FINAL_RECHECK_FINDINGS_v1_2026-10-04.json` | `3e4058d825ca67951dd23f21a9093a8a216f73e602d237325659d6c45c0567c6`, `927f9448b64ed2bf1eaf43f96f01169e768e216c53abc9c3d1d0b45ed99c3776` | **PASS**: R0–R5 passed, both findings closed, no new findings |

(1) As recorded in the 2026-10-04 night handoff; not re-hashed in this session.

Assembler lineage:
- v1 `07_TOOLS/nh_master21_assemble.py`: `a7c4049204272eba11392cf632a093805440f51d61fe03610fe9ec5e14cfed9b`
- v2: `de0b5feafb2ec8f5dbdce7ec4a200974276565560035c8951d65dda63a8a71c2`
- v3: `81195e8eb4c1a31d8af14216e36f2e896432c47296be65315c46d031d91d50bc`

## 4. What follows from the adoption

These consequences come from Ness's recorded route decisions of 2026-09-24 and 2026-09-25. Sources:
- `05_ACTIVE_CANDIDATE/NH_MASTER-21_ROUTE_AND_WORKING_METHOD_v0_4_CANDIDATE.md`, §1 and decision log;
- `03_WORKFLOW/NH_MASTER-21_TO_FINAL_SYSTEM_DESCRIPTION_ROUTE_v0_2_CANDIDATE.md`, §1, §1.1 and §4.

The consequences:
- **Master-21 is the authoritative Master, in place of V10.**
- **V10 is preserved history, retained and unedited.** At repository `main` `e339e2a1bad66c0a26a82d5f8a504a9b594d1580`, it is `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`: SHA-256 `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c`, 506,934 bytes.
- **Authority order:** Master-21 → `NH_DECISION_DEFAULTS-S19_v2_2.md` → `cursorrules` → `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`. The Working Map stays subordinate; the decision index stays navigation only.
- **NOT DECIDED stays binding.** Adoption supplies none of those answers and lets no one invent them. Nothing is designed onward from, or built on, an unresolved hole.
- **Adoption does not authorize building.** Building needs Ness's separate explicit authorization. The order of work Ness set on 2026-10-04: the gap file first, then the final master is generated, and only then does building resume.
- **Next on the route:** document 2, the gap file, under the decision-triage rule v0_3 (adopted 2026-09-28).

## 5. What this record does not do

- It edits, moves or renames no file.
- It allocates no ID, answers no NOT DECIDED entry, and changes no runtime behavior.
- Other files may still name V10 as the authority, for example the route notes or the project instructions. That wording is stale from this adoption on. It is fixed only through new versions, never by editing in place.

## 6. The 66 adopted chapters

The SHA-256 values below are the ones printed by assembler v3 on Ness's PC. They equal the v8 record as verified by the final check (Stage 0) and the re-check (R0).

| # | File | SHA-256 |
|---|---|---|
| 1 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH00.md` | `c3754d69149cc4ac3c34fd457124eccaffb3b2d465e25fc4bb97f74c5c9eb712` |
| 2 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH01.md` | `b7577363aaf7a82d51f087a36626de25dd88e318a084350ca0a0910ecc721e6c` |
| 3 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH02.md` | `4b138714ed59b023f7919cc9ad6bb707025973730dee9fde0dfa5f1d37b988c7` |
| 4 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-a.md` | `9fc34677d53903b43b870c98f6874f0210b88a6f3a1b92ffa74aa51c3ef10dcb` |
| 5 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-b.md` | `acdbfcaef1d2f13eff14f6d2833b9ae00543b4b84c2d6d964bef7f0d39ad70fc` |
| 6 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-c.md` | `d28e5b380195b8814ee3f7eb82ae330abee007ea1981107a68b529b55862b71a` |
| 7 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-d.md` | `4eb6b8e19f6ad0cf5bc2d16002405ea622edefcaced2efe10c4e63f1cbc653fd` |
| 8 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-e.md` | `d847cdf0ca2438551550e7116681200de3e76fdec065303db67f3fa8655d71ba` |
| 9 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-f.md` | `819e031c443f6f422d303f53de3885f18ed2de970934736d6e1c32f18358de60` |
| 10 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-g.md` | `9bf7359900a5277d81b4e3b2c41ecb5fd96bf0a006257751202ec4342fef9a36` |
| 11 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-h.md` | `994ae416ad9d2168e2a992a1960e61dbb562df70460be12b4ad9bc19b5bdb03c` |
| 12 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-i.md` | `4a71d3d559f461fa715469b8e53c54af78411bec845214aebcc06729fbfb78db` |
| 13 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-j.md` | `7ff83b73028508e4d62eac2d995d225cb1f61ca0cf4a18b6cdc7cb01f5f8160b` |
| 14 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-k.md` | `7446015e0a993937875f97c85d796b93704305d3d23393ca47cfeea106b2d133` |
| 15 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-l.md` | `0bd4fc827739381771dfc05951f4de81358acb165d44864f11f6bd9ca4e5f87c` |
| 16 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-m.md` | `83f539466728ec4ae2eae542fbf6e70a326c7296558c4bef31674e933c5af4df` |
| 17 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-n.md` | `da57bd8b1eaa0a723c2c9743b763992ab3666791839e8cbdc06a4f4643076d54` |
| 18 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-o.md` | `1b46e39b6126c27764d67c861291dfe61879bc6ff3c9931f4085e9cf8a5ca180` |
| 19 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-p.md` | `35ad0e72eeabc8aba94a6017b69a5c96388dff06f8b0f038ffc2797c40953df2` |
| 20 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH04-a.md` | `6208d08770d9483775c7721d5d04c8d5356967e4d0d7777e7fbcab59c0af365b` |
| 21 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH04-b.md` | `efbf21a5da3cfeed1012d3b3a359419b6f3fb21be26cc0df1263a221c7a7a69d` |
| 22 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH04-c.md` | `0055993433ebfe3302dfcf0cf85ffe07fc016b2508a2e63311e23966f6d96703` |
| 23 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH04-d.md` | `d50c597cc27846b7717e20206ad0f5f255a6058adacf7df9cfdaeb458999b564` |
| 24 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH04-e.md` | `98d61845784becec6914d1ea2e9ef6d6a7c9854ddb742c21271c98690a398b17` |
| 25 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH05-a.md` | `8727c0611054eedc59bd56fa655e503267052cc34939c7f471cf954e73430797` |
| 26 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH05-b.md` | `6a533174a3569b06d38652be23ad11abd418595a5c89743bb84b5acba75fe673` |
| 27 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH05-c.md` | `2212276c93f0e30a764995c853f29920c28ecf6862dcd7beb715d07a937a3c57` |
| 28 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH05-d.md` | `130c81030d0b666b20ee5849e5f2f6a69336c4d2c50f141e6dd23383075fb506` |
| 29 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH05-e.md` | `3ef6911fe59bd668e129a75b6800afd399f542962281b4a8968f72dacc49be2c` |
| 30 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH06-a.md` | `4694f6c72b8637847d5ed3f395f89d7d4292d00143574cf710250546e4a9cd0f` |
| 31 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH06-b.md` | `4e6c31355cfcd4c18dcc630d7e6fa8b7739010435e57620773066acd213924db` |
| 32 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH06-c.md` | `b1ce7215e7f32068e32f7004682827edc5aeddb51424d92291730ee37d11a794` |
| 33 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH06-d.md` | `c4c3529141076e2a92663050c0dc8dd453e0391d0c16b3b72d798050745ae47f` |
| 34 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH06-e.md` | `a26e416de59696fec451ea05005a61cd6f553a3033ef249dce9f638dedd74d27` |
| 35 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH06-f.md` | `a176f93cfbac41a93412a31e62808949e6dd8dbead68356d0493a1819e126e27` |
| 36 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH06-g.md` | `87bc611b84c406d61fbbe9ae8b81c50c9cff6b700f7d2ea9126e2ddc5154267d` |
| 37 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH07-a.md` | `53bb25e7519341e44dde22d8fa4062d19e6b5776f50c4fd0dcc7dfce82dfc810` |
| 38 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH07-b.md` | `3e1871c69445a18662d8021299c4b44f0038b438fd01234de9212a775c7846ae` |
| 39 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH07-c.md` | `9a2d3455439ed3c5e657c35d94cd4aaa2a85322378d7094a76e2e4cda4567f0a` |
| 40 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH08-a.md` | `7675c180ba5e3c762af0c38285a2194fd3472371e5f715b3de0712266024ff19` |
| 41 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH08-b.md` | `78e57e64c9befe00e0f5bf1ea8600d2c33a7070c2e671ee10b8856adc18ad83a` |
| 42 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH08-c.md` | `0fb5af3d493c4d758d55687f9e4529ea0441c077cc87d01a11c820f3c2149960` |
| 43 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH08-d.md` | `8aa021d2eed9189c9491826e537ff58fae4b9daa39374eb4d9a682f617229427` |
| 44 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH08-e.md` | `c54991e8b3fa02b2b95d79505f31aeb894ce2008ae23965d37379b4bb698abe1` |
| 45 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH08-f.md` | `e8fa22abdfb98c7a395dd6169c56b92f862140118d31290aa4f1790055c57760` |
| 46 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH08-g.md` | `7054b9d5a084dc2a9e59d54ce9f9d5df97fbd8b15439b2511c711318b73ea4cd` |
| 47 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-a.md` | `f451c47b7b09d6285c251a595a06d69fdc0af4d3c779e5df973bfdf0deecf9f4` |
| 48 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-b.md` | `b3cf98fa9ba312ad2d402802de9960438769c9290e03ae80c4efdc1fc137a739` |
| 49 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-c.md` | `b9b9d850cdf0167c72fb95c11334f67ac04cef4a31d56724ce744ead53993126` |
| 50 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-d.md` | `69fe3bd8d18d16993b39713aea379ecea9b1d47b0409929d9712352262263743` |
| 51 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-e.md` | `28bd602f1846f313cdb4c3bde5eafa980b60dba29ce4408d5a1e7288948c73f8` |
| 52 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-f.md` | `9e80c078a30d37dcea40c5d4024cebb0f08fcdad0ac747373d528a19f12c9cd6` |
| 53 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-g.md` | `a4861468f9182c2f829711c5f8c1c2544813f82fa0b423ead9d642f73b77dced` |
| 54 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-h.md` | `229de6895db7e8fd96112073fa557bdd9dc7f301c659bd7a2a82ba6536b6b993` |
| 55 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-i.md` | `4f707f000c575ea1a8bf818de7c27d4db15718e4de506180d8eba49879dcacc8` |
| 56 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH10-a.md` | `7888db915ea59899e6184240845671bc96d267e7614107da7d07fce624994ac9` |
| 57 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH10-b.md` | `7cc97074f212e29b674a6de7dbc71149836641fd04a4225218a12bb1f94354ae` |
| 58 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH10-c.md` | `33a26651b2e31733d270c04abfdf21d02ba8623a2a6a09db847309a3cd537dff` |
| 59 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH10-d.md` | `6b731de81a7c8f913b143294ba8b68a76d48af9f03c91f2c01b42d12af8bcdd7` |
| 60 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH10-e.md` | `813b64e52c1b856fe43df9d7fb36b6d218312db5462fb735400e72f56ab3ae92` |
| 61 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH11.md` | `0a6b2e3602ec4d3924967385d9242332b436bbb76ac421f48a1261f5522ae3c8` |
| 62 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH12-a.md` | `98d9028f5040c6f730bb983efd5f856bf02817fdd5132fb7dc8aa4cd45c6be80` |
| 63 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH12-b.md` | `b7661a928436bbf37b410692c8726e8595b314fabb48e7f12484f0e611f21d7e` |
| 64 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH12-c.md` | `748cc70adc8595eb6400eb433729d9a605e8f32d4e64a0fe2de1fe8d5852c8fd` |
| 65 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH12-d.md` | `d19cc5a79d6c7c25272d1063954dbd8e16f082fcc61d5cbe3ee17224b20fef47` |
| 66 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH12-e.md` | `74fe84ed14c945c2a49291ad6ac8e7b0468a38c22964b981d44c702cc847d896` |
