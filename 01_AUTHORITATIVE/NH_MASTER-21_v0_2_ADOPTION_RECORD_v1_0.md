# NH_MASTER-21 v0_2 — Adoption record, v1_0

**Status:** a record of an adoption made by Ness. It adds no decision of its own. Where it differs from Ness's own words, his words win.

**Frozen bytes:** the adopted files keep their internal wording and their names. Inside, the book still calls itself "Master-21" with "Status: CANDIDATE", and its chapter files keep Master-21's file names (`NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CHxx.md`), because the book's own READ RECORD tables name them with these hashes. Only the joined book's file name carries `v0_2`. The adoption lives in this record, not inside them.

## 1. The adoption

| | |
|---|---|
| By | Ness |
| When | 2026-10-29, about 19:00 Israel time (about 17:00 UTC), in the chat of the Claude Code session that built v0_2 |
| His words | "מאמת את זה אני 👍", then, asked whether he meant "מאמץ" ("I adopt"), the option "כן, אני מאמץ את v0_2" ("Yes, I adopt v0_2") |
| Context | The independent check of v0_2 had just passed. Claude had named the book as Master-21 v0_2, SHA-256 `b8524a2a112cfe55a6439c2ac3af945689afcbb6faae5c506f8c3344c2ef3ea9`, and said what adoption would do: this record, v0_2 into `01_AUTHORITATIVE/`, and Master-21 into `97_HISTORICAL_AUTHORITATIVE/`, by a pull request that Ness merges. |

His words are recorded verbatim, with the question and his answer, in `OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md` (A-2026-10-29-6) of `nesgeva/nh-gap-run`, branch `claude/zealous-pascal-qr1v9t`.

## 2. Exactly what is adopted

| Item | Identity |
|---|---|
| **Master-21 v0_2**, the joined book `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_2_CANDIDATE.md` | SHA-256 `b8524a2a112cfe55a6439c2ac3af945689afcbb6faae5c506f8c3344c2ef3ea9`; 45,041,845 bytes; 361,631 LF lines; 0 CR bytes |
| Its 66 chapter files, in `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_2/` | each listed with its SHA-256 in §6 |
| The tool that joins them | `nh_master21_assemble_v3.py`, SHA-256 `81195e8eb4c1a31d8af14216e36f2e896432c47296be65315c46d031d91d50bc` (unchanged) |

Running assembler v3 on the 66 chapters reproduces the book byte for byte. The build showed it, and the independent checker showed it again with its own run.

## 3. What v0_2 is, and the evidence

v0_2 is Master-21 (SHA-256 `8d7c929c5715bb8138644f2a0a7513a89e4f98d98c6f0f05e068284f4cc5ed0d`, adopted 2026-10-05) with only these changes. Nothing else was rewritten.

- **The 262 entries** of `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` (SHA-256 `6632af58f6b92e26fffc55b13227f88e8b71d55c28459e8555545b4ebd818914`). 214 are fixes for Ness's decisions of 2026-10-15 and his answers of 2026-10-29, and 48 are build entries: new names for three cards (IDs kept) and the decision keys on 34 chapters' citation-key lines. Each entry quotes the Master-21 line it replaced.
- **The build step.** Line numbers in the appendices follow the chapters after lines were split. Appendix A lists the 49 new NOT DECIDED lines the fixes wrote. Appendices D and E were recounted with the book's own extraction rules, which first reproduce Master-21's appendices exactly.
- **30 of the 66 chapter files** are byte for byte Master-21's.

| Step | File (in `nesgeva/nh-gap-run`, `OUT/FIX/`) | SHA-256 | Result |
|---|---|---|---|
| The build | `scripts/build_draft_book.py`, with `scripts/appendix_recount.py` | `c97e454ecd0d7bf462e4e0c1b540357f4cc4a7542d14ec554c188c8abe69efb2`, `15b4d5f65ed39511ab33f5c99af9ebe530ac4df538d19401bc414f38ee4eac6e` | builds the 66 chapters and joins them |
| Candidate record | `NH_MASTER-21_v0_2_CANDIDATE_RECORD.md` | (at commit `87c60ec`) | names v0_2 and how it was made |
| Independent check, first run | `V0_2_INDEPENDENT_CHECK.md` at commit `8e91b27` | — | FAIL: 11 of 12 checks passed; one line number in CH11 had not moved. Fixed and rebuilt (ISSUES I-25). |
| Independent check, second run | `V0_2_INDEPENDENT_CHECK.md` at commit `87c60ec` | — | **PASS**: all 12 checks, on the joined book above. The checker did not recount Appendix E's continuation citation counts or Appendix A's per-kind counts and named exceptions; it compared them. |

## 4. What follows from the adoption

- **Master-21 v0_2 is the authoritative Master, in place of Master-21.**
- **Master-21 is preserved history, retained and unedited.** It moves, with its 66 chapters and its adoption record, to `97_HISTORICAL_AUTHORITATIVE/`.
- **Authority order:** Master-21 v0_2 → `NH_DECISION_DEFAULTS-S19_v2_2.md` → `cursorrules` → `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`. The Working Map stays subordinate; the decision index stays navigation only.
- **Decision Defaults and cursorrules still carry the advisory condition** ("cannot diagnose, prescribe, or act autonomously", DD:185; cursorrules:697) that Ness's wide answer to Q3 removed. v0_2 is above them in the order. They change only through new versions.
- **NOT DECIDED stays binding.** Adoption supplies none of those answers and lets no one invent them. Nothing is designed onward from, or built on, an unresolved hole. The gap run's 2,362 filled-in answers stay proposals until the second review and Ness's approval (gap job v0_4 Part D).
- **Adoption does not authorize building.** Building needs Ness's separate explicit authorization.
- **Still to do:** the registers inside CH00, CH03-c, CH05-b, CH05-c and CH11 do not yet list the 49 new NOT DECIDED lines that Appendix A lists (nh-gap-run ISSUES I-22).

## 5. What this record does not do

- It edits no file. The pull request that adds it also adds v0_2 and moves Master-21, as Ness approved; nothing is renamed or changed inside.
- It allocates no ID, answers no NOT DECIDED entry, and changes no runtime behavior.
- Other files may still name Master-21 or its path as the authority. That wording is stale from this adoption on. It is fixed only through new versions, never by editing in place.

## 6. The 66 adopted chapters

The SHA-256 values below are those of the files built and checked (`DRAFT_MASTER-21_WITH_FIXES/_build.json` in nh-gap-run).

| # | File | SHA-256 | Against Master-21 |
|---|---|---|---|
| 1 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH00.md` | `bf1296c560f847cbe20184fc163bf44ed7416388da14c2d0f4766056c6b5d7cc` | changed |
| 2 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH01.md` | `b7577363aaf7a82d51f087a36626de25dd88e318a084350ca0a0910ecc721e6c` | same as Master-21 |
| 3 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH02.md` | `7278f2714e8d23f2bfeae15dfd26b0725c81a30e13874a22399ccb7c56bbb7ad` | changed |
| 4 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-a.md` | `9fc34677d53903b43b870c98f6874f0210b88a6f3a1b92ffa74aa51c3ef10dcb` | same as Master-21 |
| 5 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-b.md` | `acdbfcaef1d2f13eff14f6d2833b9ae00543b4b84c2d6d964bef7f0d39ad70fc` | same as Master-21 |
| 6 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-c.md` | `0f180c6adc1a0b2cd1590e3eb259c9f67f22b0c34060d14ca1cb018f2e8a99dc` | changed |
| 7 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-d.md` | `4eb6b8e19f6ad0cf5bc2d16002405ea622edefcaced2efe10c4e63f1cbc653fd` | same as Master-21 |
| 8 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-e.md` | `d847cdf0ca2438551550e7116681200de3e76fdec065303db67f3fa8655d71ba` | same as Master-21 |
| 9 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-f.md` | `819e031c443f6f422d303f53de3885f18ed2de970934736d6e1c32f18358de60` | same as Master-21 |
| 10 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-g.md` | `9bf7359900a5277d81b4e3b2c41ecb5fd96bf0a006257751202ec4342fef9a36` | same as Master-21 |
| 11 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-h.md` | `994ae416ad9d2168e2a992a1960e61dbb562df70460be12b4ad9bc19b5bdb03c` | same as Master-21 |
| 12 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-i.md` | `4a71d3d559f461fa715469b8e53c54af78411bec845214aebcc06729fbfb78db` | same as Master-21 |
| 13 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-j.md` | `7ff83b73028508e4d62eac2d995d225cb1f61ca0cf4a18b6cdc7cb01f5f8160b` | same as Master-21 |
| 14 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-k.md` | `7446015e0a993937875f97c85d796b93704305d3d23393ca47cfeea106b2d133` | same as Master-21 |
| 15 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-l.md` | `0bd4fc827739381771dfc05951f4de81358acb165d44864f11f6bd9ca4e5f87c` | same as Master-21 |
| 16 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-m.md` | `83f539466728ec4ae2eae542fbf6e70a326c7296558c4bef31674e933c5af4df` | same as Master-21 |
| 17 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-n.md` | `da57bd8b1eaa0a723c2c9743b763992ab3666791839e8cbdc06a4f4643076d54` | same as Master-21 |
| 18 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-o.md` | `1b46e39b6126c27764d67c861291dfe61879bc6ff3c9931f4085e9cf8a5ca180` | same as Master-21 |
| 19 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-p.md` | `c40892658c7d0a2c49c56b4ae7e23447ab0a410b00e6b2ce1336ca75e70a71c2` | changed |
| 20 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH04-a.md` | `a660e6915db6f19826833a5c3d5587ad30304ba61572f07eaf7f1774e91cc495` | changed |
| 21 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH04-b.md` | `efbf21a5da3cfeed1012d3b3a359419b6f3fb21be26cc0df1263a221c7a7a69d` | same as Master-21 |
| 22 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH04-c.md` | `0055993433ebfe3302dfcf0cf85ffe07fc016b2508a2e63311e23966f6d96703` | same as Master-21 |
| 23 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH04-d.md` | `8f04855d8db8bc6a366ce4334623aa76cfa60a1d48b3ccd8d28b6d7327edc3d7` | changed |
| 24 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH04-e.md` | `8ed810c65530d993c0ca74f961d01c15d25d871769050f706c9e0c729229cbe6` | changed |
| 25 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH05-a.md` | `8727c0611054eedc59bd56fa655e503267052cc34939c7f471cf954e73430797` | same as Master-21 |
| 26 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH05-b.md` | `ea0ff09a560f18d5c8dccb3922633c15b5ff762c2d3d7cc8d75231a04e65a229` | changed |
| 27 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH05-c.md` | `356f0f9ffdc6557c4dcc31b58b16b3aca8b39e54b4963df672ff6aba0ba2d7a1` | changed |
| 28 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH05-d.md` | `130c81030d0b666b20ee5849e5f2f6a69336c4d2c50f141e6dd23383075fb506` | same as Master-21 |
| 29 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH05-e.md` | `3ef6911fe59bd668e129a75b6800afd399f542962281b4a8968f72dacc49be2c` | same as Master-21 |
| 30 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH06-a.md` | `4694f6c72b8637847d5ed3f395f89d7d4292d00143574cf710250546e4a9cd0f` | same as Master-21 |
| 31 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH06-b.md` | `4e6c31355cfcd4c18dcc630d7e6fa8b7739010435e57620773066acd213924db` | same as Master-21 |
| 32 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH06-c.md` | `b1ce7215e7f32068e32f7004682827edc5aeddb51424d92291730ee37d11a794` | same as Master-21 |
| 33 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH06-d.md` | `c4c3529141076e2a92663050c0dc8dd453e0391d0c16b3b72d798050745ae47f` | same as Master-21 |
| 34 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH06-e.md` | `a26e416de59696fec451ea05005a61cd6f553a3033ef249dce9f638dedd74d27` | same as Master-21 |
| 35 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH06-f.md` | `a176f93cfbac41a93412a31e62808949e6dd8dbead68356d0493a1819e126e27` | same as Master-21 |
| 36 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH06-g.md` | `87bc611b84c406d61fbbe9ae8b81c50c9cff6b700f7d2ea9126e2ddc5154267d` | same as Master-21 |
| 37 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH07-a.md` | `53bb25e7519341e44dde22d8fa4062d19e6b5776f50c4fd0dcc7dfce82dfc810` | same as Master-21 |
| 38 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH07-b.md` | `3e1871c69445a18662d8021299c4b44f0038b438fd01234de9212a775c7846ae` | same as Master-21 |
| 39 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH07-c.md` | `9a2d3455439ed3c5e657c35d94cd4aaa2a85322378d7094a76e2e4cda4567f0a` | same as Master-21 |
| 40 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH08-a.md` | `0dc954f2cfda665a7006a219bfa9f83844fcbdbd605a4842e76ff39277027656` | changed |
| 41 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH08-b.md` | `fbd67e2f3c138fdca7afbbd12c8fdbe21925e86d4caa4575f80f8d9dd28fa69b` | changed |
| 42 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH08-c.md` | `f64f5e32051e3288eec800a3aca88005308924c92052a82c61763a81b4164fa1` | changed |
| 43 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH08-d.md` | `a73566dfbd9287247f51600cdeec19ac2e925624eb284041fad86a649649cc0b` | changed |
| 44 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH08-e.md` | `cfcf5c2bbf29c7f9c2010ab9edd790b40704433acba05e3085f63aa515778b44` | changed |
| 45 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH08-f.md` | `1ee70e1343de9289dfdc6960076ea94902392b5a6bac6ee53a9ef4968f7b63c1` | changed |
| 46 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH08-g.md` | `f8ee98cec3a782f6a321bb1437fbbc08749455d8e826e3bb101b55b2754af93d` | changed |
| 47 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-a.md` | `345b78c5fe7bb185659de95b066c3acdcf460c0dee1bfb09f67e4526268eb1a6` | changed |
| 48 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-b.md` | `c95671b739a26cd0ff7b2a2d1ecc409e5b5ae7d189f77460d6ee7636a9005e5e` | changed |
| 49 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-c.md` | `48353a6fa44b2bda050539954e1d98ee7f8eb889255d46aabbdc3e762b59bc45` | changed |
| 50 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-d.md` | `be3b9dc6e675e55938d4d7d2185fcf9ed2cee97367a30df6d11ad072d8008e6d` | changed |
| 51 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-e.md` | `7870908d77c54977ce3ec581a1b09fe554e499775f453e784753d54af9f152dc` | changed |
| 52 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-f.md` | `132d0a4d1fb18b250f017b5a28d029939ad4802f374e6e147d77651fb82e30cd` | changed |
| 53 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-g.md` | `0d5ae71c2fd8c4bca838af42ad6ca4cdd72fad9853b45ea60f27066f67d599b3` | changed |
| 54 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-h.md` | `9a9bc9f2925e874546b68bb10da7e49cf21f8caae9b9c1b222d00f4898ae4400` | changed |
| 55 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-i.md` | `fa771dc14851246cc6d26c629dbef6a75b6731f15cc1e97f1e30d61fd14a7f4f` | changed |
| 56 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH10-a.md` | `58fb3c4d50843c0b97e6ddbc7cb66ddb4c315d70e337ccc47d3f78a4c19d8786` | changed |
| 57 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH10-b.md` | `feb5bbfd0d128baeab542b08b8b73d8529420b41efd655bbd0a00c5f55da1715` | changed |
| 58 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH10-c.md` | `2107d34a078ca3ef1aec7b8ffabf7bb24eda644e14012c93b5ad8e6e5bafb463` | changed |
| 59 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH10-d.md` | `fa7df886e9d6e4bbc6bd682960e1be6d58ce9dd42046018165a4b10974bc3534` | changed |
| 60 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH10-e.md` | `040c1e0ad0de12ea5318d176373333e6d5b146301ef2a11442e5c4c4d550a655` | changed |
| 61 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH11.md` | `bd0f5f638a447efacb6dbddfee9b71a235b1a6cf23632cfc68ae133743ec3ae4` | changed |
| 62 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH12-a.md` | `34d298ac9c2a0823598c9c846cbb454ded0d00e1c14008a44605cab78b58d2ae` | changed |
| 63 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH12-b.md` | `8500799130cb10544f4cee4e067fe769b285ab8346904d04229f7e24018edf50` | changed |
| 64 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH12-c.md` | `0a2b2d7fe7c1105f04602f46ceec9ec39e37e7cc90df8a2003aa8fc99952c965` | changed |
| 65 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH12-d.md` | `953d0a18f5f8cf383bb44b2ca800c13bd79cd41c87419927e406565c3c0e4aab` | changed |
| 66 | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH12-e.md` | `3e5329beae99555299e557f40ab77aac15fbae21492648ec9154afbc8991de36` | changed |
