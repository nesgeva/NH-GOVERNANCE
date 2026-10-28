# NH_MASTER-21 — Cleanup round (round 5) targeted re-check brief (v4.1, 2026-10-04)

You are an independent checker. Claude was the fixer. You verify and report; you do not fix. Ness owns every decision. **Your message says which part is yours**: A = CH00–CH03-p (19 chapters), B = CH04-a–CH08-g (27), C = CH09-a–CH12-e (20).

**Version note.** Brief v4 (SHA-256 `b205c08110d7f3338e39ed27ececcba45adbb28bb0f8c429b19f300f19c548ba`; kept) is unchanged except for Ness's decision B below, which this version adds to §2 and Stages 3–4.

**Ness's decision B (2026-10-04).** Every per-chapter total — the count tables and the count statements in each chapter's CONTRACT CHECK and finished-file summary — will be computed and filled in by script at the joining step, so those totals are correct by construction in the joined Master-21 and are verified once, in the final check. Therefore this cleanup round no longer fails on those totals: **report any wrong per-chapter total you notice as a note (severity `note`), not as must-fix.** Everything else stays must-pass: the design content (cards, links, stamps, sources, tags, wording), every local register matching its file, structure, JSON validity, the replay, and the appendices' entries and locators.

**Why this check is targeted.** v3 passed the full checks of all three parts except for what v4 now changes: stages 0 to 3 passed in Parts A and B; Part C's links and replay passed. v4 changes only count statements, eight TOGETHER lines, four review flags, one duplicate register row and the regenerated appendices. Brief v3 (`a16463c1…`) and its rules 1 to 8 still govern.

## 1. Inputs

- `NH_MASTER-21_CLEANUP_FIXED_CHAPTERS_v4_2026-10-04.zip`, SHA-256 `9394b4da3372c322dafe6c78c8c32c03d4b4a1fb3325e6c999ffecc924607c6f`: all 66 chapters, `NH_MASTER-21_CLEANUP_CHANGED_LINES_v4_2026-10-04.md`, `NH_MASTER-21_CLEANUP_RECORD_v4_2026-10-04.json` (items R5-09891 to R5-10040; `after: null` means a removed line) and `appendix_scripts/`.
- The before set: `NH_MASTER-21_CLEANUP_FIXED_CHAPTERS_v3_2026-10-04.zip`, SHA-256 `9b5c098fa635132bcc79de9bccafcdd610cd9b4c7ebf5e81f4406c20916655a0`.
- Your own third re-check findings (your Stage 1 list) and Claude's verification of all three third re-checks (in the kit).

Chapters changed by v4 (29; the other 37 are byte-identical to v3):

| Chapter | v3 SHA-256 | v4 SHA-256 |
|---|---|---|
| CH02 | `ccfc5111fc6b55b24882597b9fd78f3a706aadda4e855b5bcfb4cc8338f757ec` | `4b138714ed59b023f7919cc9ad6bb707025973730dee9fde0dfa5f1d37b988c7` |
| CH04-a | `b3b9414c1d699c616861fa96e73e1b760d6f036ec632e305ac7f7afdccc5f32e` | `6208d08770d9483775c7721d5d04c8d5356967e4d0d7777e7fbcab59c0af365b` |
| CH04-b | `7bb6843b7917da0ad42a3664df31f2f90b0e1e2b940176b617059efd4db960aa` | `c015ee7c497810d2e9918ad688ba30ad7b262e65fa4298b7133cf8cd469aa6d3` |
| CH04-c | `e1e611e53ea030f869339bfec82594c53982897e355eae220517274daf80c8ba` | `0055993433ebfe3302dfcf0cf85ffe07fc016b2508a2e63311e23966f6d96703` |
| CH04-d | `7485a07b2fcc581538082503cd246026f9bf09daa90bb08ac6131405ee3147ca` | `d50c597cc27846b7717e20206ad0f5f255a6058adacf7df9cfdaeb458999b564` |
| CH04-e | `0a0dc2c72de41c951d00232d455fc3f0d0dc993f8cde99f49f488fa6baa2d3e2` | `98d61845784becec6914d1ea2e9ef6d6a7c9854ddb742c21271c98690a398b17` |
| CH05-a | `c4e4b2624a1993f04aab2a7d014932b5b6d904c84b3589a14837562c6a11e559` | `e166db889442419d771cbe5c2dd5fe054755a2d8cb151d52e9ef5f81b5218c36` |
| CH05-b | `b9c23c12bb297838a02fee31555e9a9f1dc1a83e94e568d7c4ea3087df641fda` | `2b3cfb5c50a4af1b923fedddbe34a51aabdfa6479a1dbd92b1106da153ce92a5` |
| CH05-c | `d3e010828f88b21f7c7aff3145bb2392de2eeb1aca37bb626d0bd63f832ade40` | `2212276c93f0e30a764995c853f29920c28ecf6862dcd7beb715d07a937a3c57` |
| CH05-d | `76319ae69f8273e106d453e7adf8291c8a9ccacc4481b45a003863f350be6892` | `130c81030d0b666b20ee5849e5f2f6a69336c4d2c50f141e6dd23383075fb506` |
| CH05-e | `3e3371710f54e3a2070977a8a60dc4df1eeff3deced84d1251bc21038ff21779` | `3ef6911fe59bd668e129a75b6800afd399f542962281b4a8968f72dacc49be2c` |
| CH07-a | `ea7b7a4158298b85f8d4aa4fadfca0a91fa9ae6936eb42cb6b5a6e976196d3cb` | `53bb25e7519341e44dde22d8fa4062d19e6b5776f50c4fd0dcc7dfce82dfc810` |
| CH08-a | `9a8fc55349f8ade552f4b77252dbb8cf0760bcfb1b53bcb2fd49ce0c5d739656` | `7675c180ba5e3c762af0c38285a2194fd3472371e5f715b3de0712266024ff19` |
| CH09-a | `004f3f462fd416b47b27122d4cce118eb4025054742881383f9c1f6f5094c25d` | `be04223df013afb3cbc41b2fe67cff191dc7c5bb4d0efe506c05d350b8495f28` |
| CH09-c | `260dca078f6a121866ca4a5f6c0e490855ec724ba282e8bdcd68f4462efa7a7a` | `4ab9f788a10d80235b4c79f9aa314936d8141f55ef57b39aeb6079b9bf02c426` |
| CH09-d | `e0a08c173a135513c1a65cff92a8783309bcd7e5a3811cc397912353e0d05280` | `c458dd94d0427aa7833ca0c4c3ca200090081f08870825cf7c29a6bb715e9d31` |
| CH09-e | `b4b9285fbb99be4fa8f9b068e04bb82836c62250c389cb6d9db92f27c9c530bd` | `d45ddb6fe5bfcee49b6e3515724ac41f29ab0c41dad4505c51214a3612de0057` |
| CH09-f | `ff319dea6705a06d519e5eb91daaf036628390cc49a7bcc45d531e3bb24d1aa4` | `81a175f518062095f46385e29486daf57270f1ff940cbc7216c409c9b30e30fb` |
| CH09-g | `507f40705832e7a7d7417da6249a859e42a159663b07b1c169c01371fc7308e9` | `bc7cb58dac9a02135c1205a04a8d0eb1048e8225e84b143b258cf7efd47aec91` |
| CH09-h | `a545760f784d3532540252fc826f0e5391b3b3ae4fd0c1ed5a1989321e0660ea` | `1d51e4ed3c9bb30c24c90d292762ea864fb27fcfe718a685867d41672d0a9481` |
| CH09-i | `82370a51d3162847ac9417d873d669affd9987a3da375b87da7d585682d04f0f` | `75761473d2a8b9a5b2ee749377662eba349e08787a6df79778eda16df0f7434d` |
| CH10-a | `b2df16a0cb1826fa7612fdfd344db1ec916615a3d684249a3770e7df351c4bc7` | `6ad795b00066cacaf8005dbe427491ffa980cd210e9c6da1664f637b793dd077` |
| CH10-b | `beaf1d76259217c94d213bf5ab77f132e584aac257869fd5bea1eb3cc97740f7` | `0cf3fdb1786a609121337898276f49cbb18e78054814745d9e9b3f5877eeef27` |
| CH10-d | `02dc94fabdf937198ade41c322d89e0360afafddf4aee451132d653a678a049d` | `6e45e6e2d81b34ab374d7895f3c16a1023ee7dc2d7f0846092a591fb190a9dc4` |
| CH12-a | `882594a03d1eb9f46e993c06fe785bb75bee5d999260fc618ca2712be2cae701` | `f390d47783bd8a52b7976c638e45b64cbadd018eab19b7ec19399d6899e88d14` |
| CH12-b | `ba74e19c2b84fceab9f037e0c151f12b0db27c9a015b40b80e60da5ce6deb2c2` | `d394a1b36ab6a289f86388063cac5c29731ec8259bf30a4cff7d88b7a6d0619e` |
| CH12-c | `f7be7b7adccda080d9be4f7d3dcfb240651af88f0e55e9a8f7738c5a246af108` | `aecb0f70e52a6025f8ea25123fb4ea65e26023a1f442a652dc153861f24f0868` |
| CH12-d | `3d09662639c5e8ec6217a49571b201b803932e30a1368bd8365ea850c46e3977` | `7223ff6055765654ff6c939c33ec6bbba5b4f0ed74bace4c4a580083d295fe88` |
| CH12-e | `11e8a752bde731ad850eaa4986d768ef5294c8d70f85a3a210d8f90ef9931aa6` | `72b95b179ef4263b8613781104046bd751b4683cf9c746d8df75b2e0b4584c5f` |

## 2. Stages

**Stage 0 — fingerprints.** The v4 zip and the v3/v4 fingerprints above.

**Stage 1 — your third re-check findings.** Each is fixed in v4, or Claude's verification says why not. Check each against the files.

**Stage 2 — replay.** For CH00–CH11 in your part, applying the v4 items in order to the v3 chapters reproduces v4 byte for byte (an item with `after: null` removes its line; several insertions at one anchor follow record order). For CH12 (Part C), check by recomputation.

**Stage 3 — each v4 change is correct.** The eight TOGETHER lines (rule 6: box, stamp per lessons 2.3 and 2.1, the row's own words and sources), the four review flags and the removed duplicate register row are must-pass. Recount items are checked as notes only (decision B).

**Stage 4 — structure and registers.** Nine boxes in order, consecutive USED BY numbering, one stamp per line, every local register matching its file, every JSON block valid. Per-chapter totals: notes only (decision B). Part C also recomputes the five appendices from the v4 chapters (their entries and locators are must-pass).

**Stage 5 — links.** Every USED BY row in your part is answered by its using card's own TOGETHER line or a direction-correct continuation (rule 6).

## 3. Output

Save, as downloadable files whose names start with `NH_MASTER-21_CLEANUP_RECHECK4_PART<your letter>_`: a REPORT (verdict PASS or FAIL, each stage's result, every finding, a line per Stage 1 finding) and a FINDINGS.json (`id`, `chapter`, `line`, `item`, `stage`, `problem`, `rule`, `evidence`, `severity`). If saving fails, write the full findings in your reply as one JSON code block.
