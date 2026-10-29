# NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE

**Status: CANDIDATE until Ness adopts it.** Target folder: `05_ACTIVE_CANDIDATE/` of `NH-GOVERNANCE`. Written 2026-10-29 by the Claude Code worker of job `NH_MASTER-21_BIG_RULES_FIX_JOB_v0_5` (repository `nh-gap-run`, branch `claude/zealous-pascal-qr1v9t`).

**Master-21 is not edited; each entry replaces the quoted line when the final master is built.**

## 1. What this file fixes

Master-21 (`01_AUTHORITATIVE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE.md`, adopted 2026-10-05) has SHA-256 `8d7c929c5715bb8138644f2a0a7513a89e4f98d98c6f0f05e068284f4cc5ed0d`. Every line number below is a line of one of its 66 chapter files in `01_AUTHORITATIVE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1/`. The chapters this file changes, with their SHA-256:

| Chapter | SHA-256 | Entries |
|---|---|---|
| CH00 | `c3754d69149cc4ac3c34fd457124eccaffb3b2d465e25fc4bb97f74c5c9eb712` | 3 |
| CH02 | `4b138714ed59b023f7919cc9ad6bb707025973730dee9fde0dfa5f1d37b988c7` | 12 |
| CH03-c | `d28e5b380195b8814ee3f7eb82ae330abee007ea1981107a68b529b55862b71a` | 5 |
| CH03-p | `35ad0e72eeabc8aba94a6017b69a5c96388dff06f8b0f038ffc2797c40953df2` | 14 |
| CH04-a | `6208d08770d9483775c7721d5d04c8d5356967e4d0d7777e7fbcab59c0af365b` | 14 |
| CH04-d | `d50c597cc27846b7717e20206ad0f5f255a6058adacf7df9cfdaeb458999b564` | 2 |
| CH04-e | `98d61845784becec6914d1ea2e9ef6d6a7c9854ddb742c21271c98690a398b17` | 9 |
| CH05-b | `6a533174a3569b06d38652be23ad11abd418595a5c89743bb84b5acba75fe673` | 34 |
| CH05-c | `2212276c93f0e30a764995c853f29920c28ecf6862dcd7beb715d07a937a3c57` | 7 |
| CH08-a | `7675c180ba5e3c762af0c38285a2194fd3472371e5f715b3de0712266024ff19` | 31 |
| CH08-b | `78e57e64c9befe00e0f5bf1ea8600d2c33a7070c2e671ee10b8856adc18ad83a` | 3 |
| CH08-c | `0fb5af3d493c4d758d55687f9e4529ea0441c077cc87d01a11c820f3c2149960` | 3 |
| CH08-d | `8aa021d2eed9189c9491826e537ff58fae4b9daa39374eb4d9a682f617229427` | 3 |
| CH08-e | `c54991e8b3fa02b2b95d79505f31aeb894ce2008ae23965d37379b4bb698abe1` | 3 |
| CH08-f | `e8fa22abdfb98c7a395dd6169c56b92f862140118d31290aa4f1790055c57760` | 3 |
| CH08-g | `7054b9d5a084dc2a9e59d54ce9f9d5df97fbd8b15439b2511c711318b73ea4cd` | 3 |
| CH09-a | `f451c47b7b09d6285c251a595a06d69fdc0af4d3c779e5df973bfdf0deecf9f4` | 3 |
| CH09-b | `b3cf98fa9ba312ad2d402802de9960438769c9290e03ae80c4efdc1fc137a739` | 9 |
| CH09-c | `b9b9d850cdf0167c72fb95c11334f67ac04cef4a31d56724ce744ead53993126` | 4 |
| CH09-d | `69fe3bd8d18d16993b39713aea379ecea9b1d47b0409929d9712352262263743` | 4 |
| CH09-e | `28bd602f1846f313cdb4c3bde5eafa980b60dba29ce4408d5a1e7288948c73f8` | 4 |
| CH09-f | `9e80c078a30d37dcea40c5d4024cebb0f08fcdad0ac747373d528a19f12c9cd6` | 4 |
| CH09-g | `a4861468f9182c2f829711c5f8c1c2544813f82fa0b423ead9d642f73b77dced` | 4 |
| CH09-h | `229de6895db7e8fd96112073fa557bdd9dc7f301c659bd7a2a82ba6536b6b993` | 4 |
| CH09-i | `4f707f000c575ea1a8bf818de7c27d4db15718e4de506180d8eba49879dcacc8` | 4 |
| CH10-a | `7888db915ea59899e6184240845671bc96d267e7614107da7d07fce624994ac9` | 4 |
| CH10-b | `7cc97074f212e29b674a6de7dbc71149836641fd04a4225218a12bb1f94354ae` | 4 |
| CH10-c | `33a26651b2e31733d270c04abfdf21d02ba8623a2a6a09db847309a3cd537dff` | 20 |
| CH10-d | `6b731de81a7c8f913b143294ba8b68a76d48af9f03c91f2c01b42d12af8bcdd7` | 5 |
| CH10-e | `813b64e52c1b856fe43df9d7fb36b6d218312db5462fb735400e72f56ab3ae92` | 5 |
| CH11 | `0a6b2e3602ec4d3924967385d9242332b436bbb76ac421f48a1261f5522ae3c8` | 20 |
| CH12-a | `98d9028f5040c6f730bb983efd5f856bf02817fdd5132fb7dc8aa4cd45c6be80` | 1 |
| CH12-d | `d19cc5a79d6c7c25272d1063954dbd8e16f082fcc61d5cbe3ee17224b20fef47` | 12 |
| CH12-e | `74fe84ed14c945c2a49291ad6ac8e7b0468a38c22964b981d44c702cc847d896` | 2 |

It holds 262 entries at 262 places in 34 chapters. The job read every line of Master-21 and listed every line that makes Ness ask, approve, wait or click item by item, or reads too narrowly. Each such line that must change under one of Ness's decisions below has one entry here. Lines that disagree in words but need no change (for example the description of version 1 of a replaced rule, or an Appendix A row of a box that stays NOT DECIDED) stay as written; the job lists each one with its reason in `clash_no_change.jsonl`.

48 of the entries are build entries, which Ness approved on 2026-10-29 with the draft's open problems (A-2026-10-29-3): 14 lines that name three cards get the cards' new names, and 34 chapters' citation-key lines get the keys of Ness's decisions. Four fixes also carry a new card name in their new text.

## 2. The decisions applied

Ness gave three decisions in chat on 2026-10-15 (Asia/Jerusalem), recorded in Claude's decisions log of that day (OCT15, `NH_CHATGPT_CHECK_REQUEST_2026-10-15_v0_1.md`, Appendix B). He put the second and third on hold until an independent check (OCT15:525-526); this job was that check. On 2026-10-29 he answered the job's questions and gave his one approval (`NESS_ANSWERS_2026-10-29_v0_1.md` in the job's output, his words quoted exactly).

| Decision | When | Ness's words, verbatim | What it means here | Entries |
|---|---|---|---|---|
| D-2026-10-15-01 | 2026-10-15, 12:38 and 12:39 | "In my opinion, b" and then "Because the more context there is, the more info there is, no?" (OCT15:386) | Option B: "N.H never asks. It always sets those items aside, and only the source can settle who said what." (OCT15:389). It covers both who spoke and which conversation (OCT15:392). Ness may still settle a held item himself, unasked (OCT15:400). | 33 |
| D-2026-10-15-02 | 2026-10-15, 16:55 | "Q 1- yes." (OCT15:439) | The places that make Ness a clerk or read too narrowly follow his big rules, as Claude's per-topic list read them and Ness changed none (OCT15:444-477). T1 is not applied: on 2026-10-29 Ness chose the later rule of 2026-10-21 for that place (D-2026-10-29-01). Topics with entries: T2 50, T3 8, T4 102. | 160 |
| D-2026-10-15-03 | 2026-10-15, 16:55 | "Q2 - a" (OCT15:483) | Option (a) as offered: "Let it slow or freeze, and drop the 'only advice' part". Tier 3 slows and Tier 4 pauses REALITY promotion automatically. Ness read it wide on 2026-10-29 (D-2026-10-29-03). | 12 |
| D-2026-10-29-01 | 2026-10-29 | "הוא רשאי לשאול שאלה ממוקדת 1, ושופ דבר ל4 נעצר זה "1"." | Q1, option b: the 2026-10-21 rule governs (patch 0001:231, "If impact is unclear, ask one focused question while independent work continues."). The 16 T1 entries were withdrawn; those lines stay as Master-21 has them. | 0 |
| D-2026-10-29-02 | 2026-10-29 | "2. כן." | Q2: the 2026-10-15 "yes" is the "new model is active" statement for research and phone material (V10:523; cursorrules:687). In practice it starts once the Layer-2 retirement mechanics (A24) are designed. No line here changes. | 0 |
| D-2026-10-29-03 | 2026-10-29 | "רחבה 3." | Q3, the wide reading of D-2026-10-15-03: the baseline engine's whole advisory condition goes ("cannot diagnose, prescribe, or act autonomously", DD:185). | 19 |
| D-2026-10-29-04 | 2026-10-29 | "4. כן, הכללים מתאימים." | Q4, option a: operation 2, recording what another person said or did, needs only the existing capture and third-party rules (A7 §6.1). | 15 |
| D-2026-10-29-05 | 2026-10-29 | "5. אני בעצמי." | Q5: Ness himself inspects a new model's readings. Whether a sample check comes first was not answered and stays open. | 0 |
| D-2026-10-29-06 | 2026-10-29 | "6. זה לא משנה, זה יכול להחעשות בדרכים גמישות." | Q6: no fixed route for this file to reach GitHub. | 0 |
| A-2026-10-29 | 2026-10-29 | "מאשר את מה שעניתי" | The one approval, applied with his answers: every entry that was `held-for-approval` is now `ready`. | 181 |
| A-2026-10-29-2 | 2026-10-29 | "אז אני מאשר" | Build a draft copy of the book with every entry applied, for reading (`DRAFT_MASTER-21_WITH_FIXES/` in the job's output). Not an adoption. | 0 |
| A-2026-10-29-3 | 2026-10-29 | "סבבה, אז תסדר את הבעיות." / "מאשר" | Fix the draft's open problems: the citation keys, the appendix counts and three card names. It does not approve the gap-run answers (section 6). Not an adoption. | 52 |

**Citation key.** A line whose content rests on one of these decisions carries the stamp `DECIDED-2026-10-15` or `DECIDED-2026-10-29` and the citation `[D-2026-10-15-01]`, `[D-2026-10-15-02 Tn]`, `[D-2026-10-15-03]`, `[D-2026-10-29-03]` or `[D-2026-10-29-04]`, following the precedent `DECIDED-2026-09-24` with `[DR §…]`. Each chapter that names one of these keys gets one sentence on its citation-key line pointing at this section, as a build entry.

## 3. How to read an entry

- Each entry gives its ID, the chapter and line, the box, its status, the rule it rests on (with the quote), its source, the approval, the line it replaces (verbatim), and the new text.
- When the new text has two or more lines, the one Master-21 line becomes that many: an unchanged part keeps its old stamp, and each decided part gets `DECIDED-2026-10-15` or `DECIDED-2026-10-29`.
- A new text that starts with "(row N removed)" removes that Appendix D row: the line it copied no longer carries a `[SOURCE CONFLICT]` mark.
- Cards keep their IDs. Three cards whose names stated a removed behavior get new names by build entries: C-7B.8.4 "Live catalog exception" becomes "Live catalog boundary", C-DETECT.2.3 "Live speaker question" becomes "Live speaker hold", and C-22.9.4 "Advisory and non-diagnostic boundary" becomes "Removed advisory boundary". The names were chosen by the worker.
- "Stays open" names what the entry leaves NOT DECIDED or NOT DESIGNED. Nothing in this file fills a hole by guessing.

All 262 entries are `ready`. The 16 withdrawn T1 entries are not listed; the job's `fixes.jsonl` keeps them with the reason.

## 4. The entries, by chapter and card in book order

### CH00

#### Chapter header

**F-CH00-00011** · CH00:11 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Every citation resolves at the pinned commit.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Every citation resolves at the pinned commit. Decision key `D-2026-10-15-02 T2`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### P-MAIN — End-to-end main path

**F-CH00-00037** · CH00:37 · Steps · `ready`

Place: P-MAIN step 7 in CH00 (path, not a card); the step names C-7GA.

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
7. C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) — DESIGNED — Derive the assignment inputs, assign bare or local-context through thread_membership_v1, and then append the durable instruction; associative and combined modes are prohibited for this new-root rule. [V10 §7G-A / MODE-ASSIGNMENT RULE: thread_membership_v1] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
```

With:

```text
7. C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) — DESIGNED — Derive the assignment inputs, assign the pass's mode through the new-root mode-assignment rule, and then append the durable instruction. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
   DECIDED-2026-10-15 — The first reading follows R4, the largest accumulated context available; thread_membership_v1 (version 1, bare or local-context only) no longer governs it. The successor rule version that assigns the first reading's mode is NOT DECIDED. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

**F-CH00-00039** · CH00:39 · Steps · `ready`

Place: P-MAIN step 9 in CH00 (path, not a card); the step names C-7F.

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
9. C-7F — Context Retrieval (§7F) — DESIGNED — Return empty context for bare mode, or permitted preceding roots from the same confirmed grouping for local-context; keep that positional context and its provenance separate from the target. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
```

With:

```text
9. C-7F — Context Retrieval (§7F) — DESIGNED — Return the context the pass's mode permits; keep that context and its provenance separate from the target. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
   DECIDED-2026-10-15 — For a first reading the permitted context is the largest accumulated context available (R4), not only empty or same-grouping preceding roots; which retrieval the successor rule version selects is NOT DECIDED. A genuinely empty result stays a normal, context-limited reading. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

### CH02

#### Chapter header

**F-CH02-00010** · CH02:10 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DR = `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_2026-09-24_v0_1_CANDIDATE.md`. The `04/`, `05/` and `98/` prefixes expand to `04_ACCEPTED_STANDALONE_DESIGNS/`, `05_ACTIVE_CANDIDATE/` and `98_HISTORICAL_SOURCES_PRE_V10/`.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DR = `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_2026-09-24_v0_1_CANDIDATE.md`. The `04/`, `05/` and `98/` prefixes expand to `04_ACCEPTED_STANDALONE_DESIGNS/`, `05_ACTIVE_CANDIDATE/` and `98_HISTORICAL_SOURCES_PRE_V10/`. Decision key `D-2026-10-15-01`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7B.8 — Unfillable-web handling

**F-CH02-06438** · CH02:6438 · Gated by · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:575, "Part 6 can't-fill→inform-don't-ask (live: catalog MAY ask)".
- Stays open: The [SOURCE CONFLICT: V10 §2 says otherwise] marks on C-7B.8 Does and C-7B.8.1 (CH02:6430 and Appendix D, CH02:11339-11341) stay: V10 §2's text is unchanged, and D-01 decides that conflict for the live catalog. Whether the final build cites D-01 beside the mark is left open. Clear-evidence rule for speakers and conversations: open (OCT15:418).

Replaces:

```text
- Gated by: DESIGNED — C-8 — Research Pipeline / Knowledge Catcher (§8): The rule applies after research inward and outward cannot fill the web; live catalog capture may ask where its capture requirements require clarification. [V10 §7B] [MAP C-7B]
```

With:

```text
- Gated by: DESIGNED — C-8 — Research Pipeline / Knowledge Catcher (§8): The rule applies after research inward and outward cannot fill the web. [V10 §7B] [MAP C-7B]
```

**F-CH02-06439** · CH02:6439 · Gated by · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:575, "Part 6 can't-fill→inform-don't-ask (live: catalog MAY ask)".
- Stays open: The [SOURCE CONFLICT: V10 §2 says otherwise] marks on C-7B.8 Does and C-7B.8.1 (CH02:6430 and Appendix D, CH02:11339-11341) stay: V10 §2's text is unchanged, and D-01 decides that conflict for the live catalog. Whether the final build cites D-01 beside the mark is left open. Clear-evidence rule for speakers and conversations: open (OCT15:418).

Replaces:

```text
- Gated by: DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): The rule applies after research inward and outward cannot fill the web; live catalog capture may ask where its capture requirements require clarification. [V10 §7B] [MAP C-7B]
```

With:

```text
- Gated by: DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): The rule applies after research inward and outward cannot fill the web. [V10 §7B] [MAP C-7B]
```

**F-CH02-11867** · CH02:11867 · USED BY · `ready`

Place: Cross-piece USED BY continuation row in CH02's back matter, for C-7B.8's Gated by line CH02:6438; the reader recorded card_id C-8 (the row's first column).

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:575, "Part 6 can't-fill→inform-don't-ask (live: catalog MAY ask)".
- Stays open: The [SOURCE CONFLICT: V10 §2 says otherwise] marks on C-7B.8 Does and C-7B.8.1 (CH02:6430 and Appendix D, CH02:11339-11341) stay: V10 §2's text is unchanged, and D-01 decides that conflict for the live catalog. Whether the final build cites D-01 beside the mark is left open. Clear-evidence rule for speakers and conversations: open (OCT15:418).

Replaces:

```text
| C-8 — Research Pipeline / Knowledge Catcher (§8) | DESIGNED | C-7B.8 — Unfillable-web handling | The named web, the piece, and exactly what information remains missing. | The rule applies after research inward and outward cannot fill the web; live catalog capture may ask where its capture requirements require clarification. | A named gap that is honest, valid and re-checkable; a later filling is a new layer rather than an overwrite. | [V10 §7B] [MAP C-7B] |
```

With:

```text
| C-8 — Research Pipeline / Knowledge Catcher (§8) | DESIGNED | C-7B.8 — Unfillable-web handling | The named web, the piece, and exactly what information remains missing. | The rule applies after research inward and outward cannot fill the web. | A named gap that is honest, valid and re-checkable; a later filling is a new layer rather than an overwrite. | [V10 §7B] [MAP C-7B] |
```

**F-CH02-11868** · CH02:11868 · USED BY · `ready`

Place: Cross-piece USED BY continuation row for C-7B.8's Gated by line CH02:6439; the reader recorded card_id C-7E.

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:575, "Part 6 can't-fill→inform-don't-ask (live: catalog MAY ask)".
- Stays open: The [SOURCE CONFLICT: V10 §2 says otherwise] marks on C-7B.8 Does and C-7B.8.1 (CH02:6430 and Appendix D, CH02:11339-11341) stay: V10 §2's text is unchanged, and D-01 decides that conflict for the live catalog. Whether the final build cites D-01 beside the mark is left open. Clear-evidence rule for speakers and conversations: open (OCT15:418).

Replaces:

```text
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | DESIGNED | C-7B.8 — Unfillable-web handling | The named web, the piece, and exactly what information remains missing. | The rule applies after research inward and outward cannot fill the web; live catalog capture may ask where its capture requirements require clarification. | A named gap that is honest, valid and re-checkable; a later filling is a new layer rather than an overwrite. | [V10 §7B] [MAP C-7B] |
```

With:

```text
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | DESIGNED | C-7B.8 — Unfillable-web handling | The named web, the piece, and exactly what information remains missing. | The rule applies after research inward and outward cannot fill the web. | A named gap that is honest, valid and re-checkable; a later filling is a new layer rather than an overwrite. | [V10 §7B] [MAP C-7B] |
```

#### C-7B.8.4 — Live catalog exception (new name: Live catalog boundary)

**F-CH02-06449** · CH02:6449 · card name · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: D-2026-10-15-01, which the card's fixed text follows.
- Source: `REPO/01_AUTHORITATIVE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH02.md`:6520, "### C-7B.8.4 — Live catalog exception".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The card keeps its ID C-7B.8.4. The new name was chosen by the worker and not shown to Ness one by one; he can change it.

Replaces:

```text
SUB-PARTS: C-7B.8.1 — Named gap; C-7B.8.2 — Continue without solicitation; C-7B.8.3 — Later answer layer; C-7B.8.4 — Live catalog exception
```

With:

```text
SUB-PARTS: C-7B.8.1 — Named gap; C-7B.8.2 — Continue without solicitation; C-7B.8.3 — Later answer layer; C-7B.8.4 — Live catalog boundary
```

**F-CH02-06520** · CH02:6520 · card name · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: D-2026-10-15-01, which the card's fixed text follows.
- Source: `REPO/01_AUTHORITATIVE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH02.md`:6520, "### C-7B.8.4 — Live catalog exception".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The card keeps its ID C-7B.8.4. The new name was chosen by the worker and not shown to Ness one by one; he can change it.

Replaces:

```text
### C-7B.8.4 — Live catalog exception
```

With:

```text
### C-7B.8.4 — Live catalog boundary
```

**F-CH02-06524** · CH02:6524 · What it is · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:689, "Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`.".
- Stays open: C-7B.8.4 keeps its ID; after D-01 it is the catalog boundary with no exception, and its name becomes "Live catalog boundary" (A-2026-10-29-3). Its TOGETHER boxes stay NOT DECIDED (Appendix A rows CH02:10812-10814 unchanged; nothing here fills them). Whether to write a clear-evidence rule for speakers and conversations like Bundle 3 A5 stays open (OCT15:418). C-DETECT.2.5's authorized resolution rule stays NOT DECIDED.

Replaces:

```text
- What it is: DESIGNED — The permission for live capture clarification at the catalog boundary. [V10 §7B] [V10 §7E]
```

With:

```text
- What it is: DECIDED-2026-10-15 — The catalog boundary for a live capture whose speaker or thread grouping cannot be resolved from its source: there is no live exception, and the capture is set aside as in unattended processing. [D-2026-10-15-01] [V10 §7E]
```

**F-CH02-06526** · CH02:6526 · Does · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:689, "Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`.".
- Stays open: C-7B.8.4 keeps its ID; after D-01 it is the catalog boundary with no exception, and its name becomes "Live catalog boundary" (A-2026-10-29-3). Its TOGETHER boxes stay NOT DECIDED (Appendix A rows CH02:10812-10814 unchanged; nothing here fills them). Whether to write a clear-evidence rule for speakers and conversations like Bundle 3 A5 stays open (OCT15:418). C-DETECT.2.5's authorized resolution rule stays NOT DECIDED.

Replaces:

```text
- Does: DESIGNED — Permits the catalog to ask Ness for required capture clarification. Unattended unresolved speaker or thread remains held rather than guessed. [V10 §7B] [V10 §7E]
```

With:

```text
- Does: DECIDED-2026-10-15 — Never asks Ness who spoke or which conversation the capture belongs to, live or unattended. An unresolved speaker or thread remains held rather than guessed. [D-2026-10-15-01] [V10 §7E]
```

**F-CH02-06527** · CH02:6527 · Gives out · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:689, "Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`.".
- Stays open: C-7B.8.4 keeps its ID; after D-01 it is the catalog boundary with no exception, and its name becomes "Live catalog boundary" (A-2026-10-29-3). Its TOGETHER boxes stay NOT DECIDED (Appendix A rows CH02:10812-10814 unchanged; nothing here fills them). Whether to write a clear-evidence rule for speakers and conversations like Bundle 3 A5 stays open (OCT15:418). C-DETECT.2.5's authorized resolution rule stays NOT DECIDED.

Replaces:

```text
- Gives out: DESIGNED — Capture clarification, or a held unresolved capture. [V10 §7B] [V10 §7E]
```

With:

```text
- Gives out: DECIDED-2026-10-15 — A held unresolved capture, with no clarification request to Ness. [D-2026-10-15-01] [V10 §7E]
```

**F-CH02-06529** · CH02:6529 · Fails closed by · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:689, "Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`.".
- Stays open: C-7B.8.4 keeps its ID; after D-01 it is the catalog boundary with no exception, and its name becomes "Live catalog boundary" (A-2026-10-29-3). Its TOGETHER boxes stay NOT DECIDED (Appendix A rows CH02:10812-10814 unchanged; nothing here fills them). Whether to write a clear-evidence rule for speakers and conversations like Bundle 3 A5 stays open (OCT15:418). C-DETECT.2.5's authorized resolution rule stays NOT DECIDED.

Replaces:

```text
- Fails closed by: DESIGNED — Permits the catalog to ask Ness for required capture clarification. Unattended unresolved speaker or thread remains held rather than guessed. [V10 §7B] [V10 §7E]
```

With:

```text
- Fails closed by: DECIDED-2026-10-15 — Holds the capture as an unresolved speaker or thread instead of asking Ness or guessing. [D-2026-10-15-01] [V10 §7E]
```

**F-CH02-06539** · CH02:6539 · USED BY · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:689, "Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`.".
- Stays open: C-7B.8.4 keeps its ID; after D-01 it is the catalog boundary with no exception, and its name becomes "Live catalog boundary" (A-2026-10-29-3). Its TOGETHER boxes stay NOT DECIDED (Appendix A rows CH02:10812-10814 unchanged; nothing here fills them). Whether to write a clear-evidence rule for speakers and conversations like Bundle 3 A5 stays open (OCT15:418). C-DETECT.2.5's authorized resolution rule stays NOT DECIDED.

Replaces:

```text
| 1 · DESIGNED | C-7E; CY-B | A live capture whose necessary speaker or genuinely uncertain thread grouping cannot be resolved from its source. | Permits the catalog to ask Ness for required capture clarification. Unattended unresolved speaker or thread remains held rather than guessed. | Capture clarification, or a held unresolved capture. | [V10 §7B] [V10 §7E] [MAP CY-B] |
```

With:

```text
| 1 · DECIDED-2026-10-15 | C-7E; CY-B | A live capture whose necessary speaker or genuinely uncertain thread grouping cannot be resolved from its source. | Never asks Ness who spoke or which conversation the capture belongs to, live or unattended. An unresolved speaker or thread remains held rather than guessed. | A held unresolved capture, with no clarification request to Ness. | [D-2026-10-15-01] [V10 §7E] [MAP CY-B] |
```

### CH03-c

#### Chapter header

**F-CH03-c-00012** · CH03-c:12 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`. NHD-A2 and NHD-SLF are navigation IDs only; behavior comes from the cited accepted source sections.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`. NHD-A2 and NHD-SLF are navigation IDs only; behavior comes from the cited accepted source sections. Decision key `D-2026-10-15-02 T2`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-READ.10.7.1 — No instruction

**F-CH03-c-04654** · CH03-c:4654 · What it is · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- What it is: ACCEPTED — RC-3 creates the instruction: run thread_membership_v1 fresh, validate and append the instruction, then proceed. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §4.4] [NHD-A2]
```

With:

```text
- What it is: ACCEPTED — RC-3 creates the instruction: run the new-root mode-assignment rule fresh, validate and append the instruction, then proceed. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §4.4] [NHD-A2]
- What it is: DECIDED-2026-10-15 — The rule run fresh is the successor version of thread_membership_v1 (NOT DECIDED); thread_membership_v1 (version 1, bare or local-context only) no longer governs it. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

**F-CH03-c-04656** · CH03-c:4656 · Does · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Does: ACCEPTED — RC-3 creates the instruction: run thread_membership_v1 fresh, validate and append the instruction, then proceed. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §4.4] [NHD-A2]
```

With:

```text
- Does: ACCEPTED — RC-3 creates the instruction: run the new-root mode-assignment rule fresh, validate and append the instruction, then proceed. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §4.4] [NHD-A2]
- Does: DECIDED-2026-10-15 — The rule run fresh is the successor version of thread_membership_v1 (NOT DECIDED); thread_membership_v1 (version 1, bare or local-context only) no longer governs it. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

**F-CH03-c-04658** · CH03-c:4658 · Must never · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Must never: ACCEPTED — Proceed as though an instruction exists before fresh thread_membership_v1, validation and instruction append. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §4.4] [NHD-A2] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §4.4.1] [NHD-A2] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §4.9] [NHD-A2]
```

With:

```text
- Must never: ACCEPTED — Proceed as though an instruction exists before a fresh run of the new-root mode-assignment rule, validation and instruction append. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §4.4] [NHD-A2] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §4.4.1] [NHD-A2] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §4.9] [NHD-A2]
- Must never: DECIDED-2026-10-15 — Run thread_membership_v1 version 1 as that rule for a first reading; its successor version is NOT DECIDED. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

**F-CH03-c-04659** · CH03-c:4659 · Fails closed by · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Fails closed by: ACCEPTED — RC-3 creates the instruction: run thread_membership_v1 fresh, validate and append the instruction, then proceed. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §4.4] [NHD-A2]
```

With:

```text
- Fails closed by: ACCEPTED — RC-3 creates the instruction: run the new-root mode-assignment rule fresh, validate and append the instruction, then proceed. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §4.4] [NHD-A2]
- Fails closed by: DECIDED-2026-10-15 — The rule run fresh is the successor version of thread_membership_v1 (NOT DECIDED); thread_membership_v1 (version 1, bare or local-context only) no longer governs it. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

### CH03-p

#### Chapter header

**F-CH03-p-00010** · CH03-p:10 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`. Decision key `D-2026-10-15-01`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-DETECT.2 — Settled speaker rule

**F-CH03-p-00143** · CH03-p:143 · Does · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:689, "Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`.".
- Stays open: C-DETECT.2.3 keeps its ID; after D-01 it records that no live question exists, and its name becomes "Live speaker hold" (A-2026-10-29-3). C-DETECT.2.4 still names its hold for "unattended material" (CH03-p:243 ff.); after D-01 live material with an unresolved speaker enters the same `speaker_unresolved` hold, and the final build may widen that card's wording to match. C-DETECT.2.5's authorized resolution rule stays NOT DECIDED (OCT15:398, :417), and so does the clear-evidence rule for speakers (OCT15:418). Ness may still confirm a speaker unasked (OCT15:400).

Replaces:

```text
- Does: DESIGNED — Gives source-carried attribution priority; permits only uncertain fallback proposals; asks Ness in live use when a necessary speaker cannot be identified; holds unresolved unattended material. [V10 §7E / SPEAKER RESOLUTION RULE] [MAP C-DETECT]
```

With:

```text
- Does: DESIGNED — Gives source-carried attribution priority; permits only uncertain fallback proposals; holds unresolved unattended material. [V10 §7E / SPEAKER RESOLUTION RULE] [MAP C-DETECT]
- Does: DECIDED-2026-10-15 — Never asks Ness who spoke, even in live use; live material whose necessary speaker cannot be identified is held as `speaker_unresolved`, as unattended material is. [D-2026-10-15-01] [V10 §7E / SPEAKER RESOLUTION RULE]
```

**F-CH03-p-00153** · CH03-p:153 · Changes · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:689, "Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`.".
- Approved: Card name: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: C-DETECT.2.3 keeps its ID; after D-01 it records that no live question exists, and its name becomes "Live speaker hold" (A-2026-10-29-3). C-DETECT.2.4 still names its hold for "unattended material" (CH03-p:243 ff.); after D-01 live material with an unresolved speaker enters the same `speaker_unresolved` hold, and the final build may widen that card's wording to match. C-DETECT.2.5's authorized resolution rule stays NOT DECIDED (OCT15:398, :417), and so does the clear-evidence rule for speakers (OCT15:418). Ness may still confirm a speaker unasked (OCT15:400).

Replaces:

```text
- Changes: DESIGNED — C-DETECT.2.3 — Live speaker question: permits asking Ness when a necessary speaker is not identifiable. [V10 §7E / SPEAKER RESOLUTION RULE]
```

With:

```text
- Changes: DECIDED-2026-10-15 — C-DETECT.2.3 — Live speaker hold: asks Ness nothing; live material whose necessary speaker is not identifiable is held as `speaker_unresolved`. [D-2026-10-15-01] [V10 §7E / SPEAKER RESOLUTION RULE]
```

**F-CH03-p-00661** · CH03-p:661 · table row · `ready`

Place: Source-coverage row in CH03-p's back matter for the C-DETECT.2 tree.

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:689, "Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`.".
- Stays open: C-DETECT.2.3 keeps its ID; after D-01 it records that no live question exists, and its name becomes "Live speaker hold" (A-2026-10-29-3). C-DETECT.2.4 still names its hold for "unattended material" (CH03-p:243 ff.); after D-01 live material with an unresolved speaker enters the same `speaker_unresolved` hold, and the final build may widen that card's wording to match. C-DETECT.2.5's authorized resolution rule stays NOT DECIDED (OCT15:398, :417), and so does the clear-evidence rule for speakers (OCT15:418). Ness may still confirm a speaker unasked (OCT15:400).

Replaces:

```text
| V10 §7E SPEAKER RESOLUTION RULE: whole paragraph | C-DETECT.2 and descendants | Source attribution, no guessed role, separate raw capture/root eligibility, live question, unattended hold and confirmation. |
```

With:

```text
| V10 §7E SPEAKER RESOLUTION RULE: whole paragraph | C-DETECT.2 and descendants | Source attribution, no guessed role, separate raw capture/root eligibility, unattended hold and confirmation; the live question is removed by D-2026-10-15-01 and live material is held. |
```

#### C-DETECT.2.3 — Live speaker question (new name: Live speaker hold)

**F-CH03-p-00165** · CH03-p:165 · card name · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: D-2026-10-15-01, which the card's fixed text follows.
- Source: `REPO/01_AUTHORITATIVE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-p.md`:213, "### C-DETECT.2.3 — Live speaker question".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The card keeps its ID C-DETECT.2.3. The new name was chosen by the worker and not shown to Ness one by one; he can change it.

Replaces:

```text
SUB-PARTS: C-DETECT.2.1 — Source-attribution priority; C-DETECT.2.2 — No direct role write; C-DETECT.2.3 — Live speaker question; C-DETECT.2.4 — Unattended speaker hold; C-DETECT.2.5 — Speaker confirmation authority
```

With:

```text
SUB-PARTS: C-DETECT.2.1 — Source-attribution priority; C-DETECT.2.2 — No direct role write; C-DETECT.2.3 — Live speaker hold; C-DETECT.2.4 — Unattended speaker hold; C-DETECT.2.5 — Speaker confirmation authority
```

**F-CH03-p-00213** · CH03-p:213 · card name · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: D-2026-10-15-01, which the card's fixed text follows.
- Source: `REPO/01_AUTHORITATIVE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-p.md`:213, "### C-DETECT.2.3 — Live speaker question".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The card keeps its ID C-DETECT.2.3. The new name was chosen by the worker and not shown to Ness one by one; he can change it.

Replaces:

```text
### C-DETECT.2.3 — Live speaker question
```

With:

```text
### C-DETECT.2.3 — Live speaker hold
```

**F-CH03-p-00217** · CH03-p:217 · What it is · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:689, "Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`.".
- Stays open: C-DETECT.2.3 keeps its ID; after D-01 it records that no live question exists, and its name becomes "Live speaker hold" (A-2026-10-29-3). C-DETECT.2.4 still names its hold for "unattended material" (CH03-p:243 ff.); after D-01 live material with an unresolved speaker enters the same `speaker_unresolved` hold, and the final build may widen that card's wording to match. C-DETECT.2.5's authorized resolution rule stays NOT DECIDED (OCT15:398, :417), and so does the clear-evidence rule for speakers (OCT15:418). Ness may still confirm a speaker unasked (OCT15:400).

Replaces:

```text
- What it is: DESIGNED — The live interactive speaker-resolution question. [V10 §7E / SPEAKER RESOLUTION RULE]
```

With:

```text
- What it is: DECIDED-2026-10-15 — The live case of speaker resolution, in which N.H asks Ness no speaker question. [D-2026-10-15-01] [V10 §7E / SPEAKER RESOLUTION RULE]
```

**F-CH03-p-00219** · CH03-p:219 · Does · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:689, "Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`.".
- Stays open: C-DETECT.2.3 keeps its ID; after D-01 it records that no live question exists, and its name becomes "Live speaker hold" (A-2026-10-29-3). C-DETECT.2.4 still names its hold for "unattended material" (CH03-p:243 ff.); after D-01 live material with an unresolved speaker enters the same `speaker_unresolved` hold, and the final build may widen that card's wording to match. C-DETECT.2.5's authorized resolution rule stays NOT DECIDED (OCT15:398, :417), and so does the clear-evidence rule for speakers (OCT15:418). Ness may still confirm a speaker unasked (OCT15:400).

Replaces:

```text
- Does: DESIGNED — Asks Ness for speaker resolution in that situation. [V10 §7E / SPEAKER RESOLUTION RULE]
```

With:

```text
- Does: DECIDED-2026-10-15 — Does not ask Ness; holds the material as `speaker_unresolved`, as C-DETECT.2.4 holds unattended material. [D-2026-10-15-01] [V10 §7E / SPEAKER RESOLUTION RULE]
```

**F-CH03-p-00220** · CH03-p:220 · Gives out · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:689, "Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`.".
- Stays open: C-DETECT.2.3 keeps its ID; after D-01 it records that no live question exists, and its name becomes "Live speaker hold" (A-2026-10-29-3). C-DETECT.2.4 still names its hold for "unattended material" (CH03-p:243 ff.); after D-01 live material with an unresolved speaker enters the same `speaker_unresolved` hold, and the final build may widen that card's wording to match. C-DETECT.2.5's authorized resolution rule stays NOT DECIDED (OCT15:398, :417), and so does the clear-evidence rule for speakers (OCT15:418). Ness may still confirm a speaker unasked (OCT15:400).

Replaces:

```text
- Gives out: DESIGNED — A request for confirmation, with the candidate still only a proposal until confirmed. [V10 §7E / SPEAKER RESOLUTION RULE]
```

With:

```text
- Gives out: DECIDED-2026-10-15 — A `speaker_unresolved` hold, with any detector candidate still only a proposal; no request to Ness. [D-2026-10-15-01] [V10 §7E / SPEAKER RESOLUTION RULE]
```

**F-CH03-p-00221** · CH03-p:221 · Must never · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:689, "Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`.".
- Stays open: C-DETECT.2.3 keeps its ID; after D-01 it records that no live question exists, and its name becomes "Live speaker hold" (A-2026-10-29-3). C-DETECT.2.4 still names its hold for "unattended material" (CH03-p:243 ff.); after D-01 live material with an unresolved speaker enters the same `speaker_unresolved` hold, and the final build may widen that card's wording to match. C-DETECT.2.5's authorized resolution rule stays NOT DECIDED (OCT15:398, :417), and so does the clear-evidence rule for speakers (OCT15:418). Ness may still confirm a speaker unasked (OCT15:400).

Replaces:

```text
- Must never: DESIGNED — Treat asking the question as confirmation or silently fill `role` from the uncertain candidate. [V10 §7E / SPEAKER RESOLUTION RULE]
```

With:

```text
- Must never: DESIGNED — Silently fill `role` from the uncertain candidate. [V10 §7E / SPEAKER RESOLUTION RULE]
- Must never: DECIDED-2026-10-15 — Ask Ness who spoke, live or unattended. [D-2026-10-15-01]
```

**F-CH03-p-00232** · CH03-p:232 · USED BY · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:689, "Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`.".
- Stays open: C-DETECT.2.3 keeps its ID; after D-01 it records that no live question exists, and its name becomes "Live speaker hold" (A-2026-10-29-3). C-DETECT.2.4 still names its hold for "unattended material" (CH03-p:243 ff.); after D-01 live material with an unresolved speaker enters the same `speaker_unresolved` hold, and the final build may widen that card's wording to match. C-DETECT.2.5's authorized resolution rule stays NOT DECIDED (OCT15:398, :417), and so does the clear-evidence rule for speakers (OCT15:418). Ness may still confirm a speaker unasked (OCT15:400).

Replaces:

```text
| 1 · DESIGNED | C-DETECT.2 — Settled speaker rule | Live material whose speaker is necessary and cannot be identified. | permits asking Ness when a necessary speaker is not identifiable. | A request for confirmation, with the candidate still only a proposal until confirmed. | [V10 §7E / SPEAKER RESOLUTION RULE] |
```

With:

```text
| 1 · DECIDED-2026-10-15 | C-DETECT.2 — Settled speaker rule | Live material whose speaker is necessary and cannot be identified. | asks Ness nothing; the material is held as `speaker_unresolved`. | A `speaker_unresolved` hold, with any detector candidate still only a proposal; no request to Ness. | [D-2026-10-15-01] [V10 §7E / SPEAKER RESOLUTION RULE] |
```

**F-CH03-p-00611** · CH03-p:611 · card name · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: D-2026-10-15-01, which the card's fixed text follows.
- Source: `REPO/01_AUTHORITATIVE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-p.md`:213, "### C-DETECT.2.3 — Live speaker question".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The card keeps its ID C-DETECT.2.3. The new name was chosen by the worker and not shown to Ness one by one; he can change it.

Replaces:

```text
| C-DETECT.2.3 — Live speaker question | Fed by | 1 | NOT DECIDED |
```

With:

```text
| C-DETECT.2.3 — Live speaker hold | Fed by | 1 | NOT DECIDED |
```

**F-CH03-p-00612** · CH03-p:612 · card name · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: D-2026-10-15-01, which the card's fixed text follows.
- Source: `REPO/01_AUTHORITATIVE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-p.md`:213, "### C-DETECT.2.3 — Live speaker question".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The card keeps its ID C-DETECT.2.3. The new name was chosen by the worker and not shown to Ness one by one; he can change it.

Replaces:

```text
| C-DETECT.2.3 — Live speaker question | Changes | 1 | NOT DECIDED |
```

With:

```text
| C-DETECT.2.3 — Live speaker hold | Changes | 1 | NOT DECIDED |
```

**F-CH03-p-00613** · CH03-p:613 · card name · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: D-2026-10-15-01, which the card's fixed text follows.
- Source: `REPO/01_AUTHORITATIVE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-p.md`:213, "### C-DETECT.2.3 — Live speaker question".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The card keeps its ID C-DETECT.2.3. The new name was chosen by the worker and not shown to Ness one by one; he can change it.

Replaces:

```text
| C-DETECT.2.3 — Live speaker question | Gated by | 1 | NOT DECIDED |
```

With:

```text
| C-DETECT.2.3 — Live speaker hold | Gated by | 1 | NOT DECIDED |
```

### CH04-a

#### Chapter header

**F-CH04-a-00010** · CH04-a:10 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Every citation resolves at the pinned commit.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Every citation resolves at the pinned commit. Decision key `D-2026-10-15-01`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7E — Catalog Front Door + pre-ingest holding (§7E)

**F-CH04-a-00049** · CH04-a:49 · Gated by · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:689, "Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`.".
- Approved: Card name: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: C-7E.7 Fails closed by (CH04-a:718), C-7E.8.4 Fails closed by (CH04-a:838) and C-7E.8.4 What it is still say "unattended"; after D-01 live material with an unresolved speaker or grouping enters the same hold, and the final build may widen those words. C-7E.8.4's TOGETHER boxes stay NOT DECIDED (its Appendix A rows unchanged). C-DETECT.2.5's authorized resolution rule and a clear-evidence rule for speakers and conversations stay open (OCT15:418).

Replaces:

```text
- Gated by: DESIGNED — C-7B.8.4 — Live catalog exception: permits the catalog to ask Ness for required capture clarification. Unattended unresolved speaker or thread remains held rather than guessed (CY-B). [V10 §7B] [V10 §7E] [MAP CY-B]
```

With:

```text
- Gated by: DECIDED-2026-10-15 — C-7B.8.4 — Live catalog boundary: the catalog never asks Ness who spoke or which conversation a capture belongs to; an unresolved speaker or thread remains held rather than guessed, live or unattended (CY-B). [D-2026-10-15-01] [V10 §7E] [MAP CY-B]
```

**F-CH04-a-00058** · CH04-a:58 · USED BY · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:689, "Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`.".
- Stays open: C-7E.7 Fails closed by (CH04-a:718), C-7E.8.4 Fails closed by (CH04-a:838) and C-7E.8.4 What it is still say "unattended"; after D-01 live material with an unresolved speaker or grouping enters the same hold, and the final build may widen those words. C-7E.8.4's TOGETHER boxes stay NOT DECIDED (its Appendix A rows unchanged). C-DETECT.2.5's authorized resolution rule and a clear-evidence rule for speakers and conversations stay open (OCT15:418).

Replaces:

```text
| 3 · DESIGNED | C-7B.8 — Unfillable-web handling | A live capture requiring speaker or grouping clarification. | May ask Ness under the specific live catalog rules. | Preserves unresolved material until its actual catalog requirement is resolved. | [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] |
```

With:

```text
| 3 · DECIDED-2026-10-15 | C-7B.8 — Unfillable-web handling | A live capture whose speaker or grouping cannot be resolved from its source. | Asks Ness nothing; holds the capture as an unresolved speaker or thread. | Preserves unresolved material until its actual catalog requirement is resolved. | [D-2026-10-15-01] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] |
```

**F-CH04-a-01611** · CH04-a:1611 · table row · `ready`

Place: Back-matter reciprocity table of CH04-a (under the heading of C-7E.13.7, the last card); the row is about C-7E's link with C-7B.8.

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:689, "Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`.".
- Stays open: C-7E.7 Fails closed by (CH04-a:718), C-7E.8.4 Fails closed by (CH04-a:838) and C-7E.8.4 What it is still say "unattended"; after D-01 live material with an unresolved speaker or grouping enters the same hold, and the final build may widen those words. C-7E.8.4's TOGETHER boxes stay NOT DECIDED (its Appendix A rows unchanged). C-DETECT.2.5's authorized resolution rule and a clear-evidence rule for speakers and conversations stay open (OCT15:418).

Replaces:

```text
| C-7B.8 — Unfillable-web handling | C-7E — Catalog Front Door + pre-ingest holding (§7E) | DESIGNED — Reciprocates the existing CH02 live-catalog exception in unfillable-web handling. | [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] |
```

With:

```text
| C-7B.8 — Unfillable-web handling | C-7E — Catalog Front Door + pre-ingest holding (§7E) | DECIDED-2026-10-15 — Reciprocates CH02's C-7B.8.4 boundary in unfillable-web handling: the live catalog asks Ness nothing and holds an unresolved speaker or grouping. | [D-2026-10-15-01] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] |
```

#### C-7E.7 — Catalog speaker resolution

**F-CH04-a-00714** · CH04-a:714 · Does · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:689, "Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`.".
- Stays open: C-7E.7 Fails closed by (CH04-a:718), C-7E.8.4 Fails closed by (CH04-a:838) and C-7E.8.4 What it is still say "unattended"; after D-01 live material with an unresolved speaker or grouping enters the same hold, and the final build may widen those words. C-7E.8.4's TOGETHER boxes stay NOT DECIDED (its Appendix A rows unchanged). C-DETECT.2.5's authorized resolution rule and a clear-evidence rule for speakers and conversations stay open (OCT15:418).

Replaces:

```text
- Does: DESIGNED — Carries the source speaker without guessing; in live use asks Ness when a necessary speaker cannot be identified, and in unattended use holds the item as `speaker_unresolved`. [V10 §7E / SPEAKER RESOLUTION RULE]
```

With:

```text
- Does: DESIGNED — Carries the source speaker without guessing; in unattended use holds the item as `speaker_unresolved` when a necessary speaker cannot be identified. [V10 §7E / SPEAKER RESOLUTION RULE]
- Does: DECIDED-2026-10-15 — In live use too, never asks Ness who spoke; a necessary speaker that cannot be identified leaves the item held as `speaker_unresolved`. [D-2026-10-15-01] [V10 §7E / SPEAKER RESOLUTION RULE]
```

**F-CH04-a-01750** · CH04-a:1750 · table row · `ready`

Place: Source-coverage row in CH04-a's back matter for C-7E.7 and the C-DETECT.2 tree.

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:689, "Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`.".
- Stays open: C-7E.7 Fails closed by (CH04-a:718), C-7E.8.4 Fails closed by (CH04-a:838) and C-7E.8.4 What it is still say "unattended"; after D-01 live material with an unresolved speaker or grouping enters the same hold, and the final build may widen those words. C-7E.8.4's TOGETHER boxes stay NOT DECIDED (its Appendix A rows unchanged). C-DETECT.2.5's authorized resolution rule and a clear-evidence rule for speakers and conversations stay open (OCT15:418).

Replaces:

```text
| V10 §7E SPEAKER RESOLUTION RULE; MAP C-DETECT whole card | C-7E.7; existing C-DETECT.2 and descendants | The source-attribution, uncertain-fallback, live-question, unattended-hold and authorized-confirmation rules reuse CH03-p's cards. |
```

With:

```text
| V10 §7E SPEAKER RESOLUTION RULE; MAP C-DETECT whole card | C-7E.7; existing C-DETECT.2 and descendants | The source-attribution, uncertain-fallback, unattended-hold and authorized-confirmation rules reuse CH03-p's cards; the live question is removed by D-2026-10-15-01 and live material is held. |
```

#### C-7E.8 — Source-title and thread resolution

**F-CH04-a-00738** · CH04-a:738 · Does · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:691, "(4) Grouping genuinely uncertain → live: ask Ness; unattended: hold as `thread_unresolved`.".
- Stays open: C-7E.7 Fails closed by (CH04-a:718), C-7E.8.4 Fails closed by (CH04-a:838) and C-7E.8.4 What it is still say "unattended"; after D-01 live material with an unresolved speaker or grouping enters the same hold, and the final build may widen those words. C-7E.8.4's TOGETHER boxes stay NOT DECIDED (its Appendix A rows unchanged). C-DETECT.2.5's authorized resolution rule and a clear-evidence rule for speakers and conversations stay open (OCT15:418).

Replaces:

```text
- Does: DESIGNED — Carries a real thread identifier exactly; assigns one unique non-semantic capture-session placeholder to provably grouped untitled material; assigns a unique singleton placeholder to an isolated item; asks Ness live or holds unattended material when grouping is uncertain. [V10 §7E / SOURCE TITLE RULE]
```

With:

```text
- Does: DESIGNED — Carries a real thread identifier exactly; assigns one unique non-semantic capture-session placeholder to provably grouped untitled material; assigns a unique singleton placeholder to an isolated item; holds unattended material as `thread_unresolved` when grouping is uncertain. [V10 §7E / SOURCE TITLE RULE]
- Does: DECIDED-2026-10-15 — When grouping is uncertain in live use, never asks Ness which conversation the material belongs to; holds it as `thread_unresolved`. [D-2026-10-15-01] [V10 §7E / SOURCE TITLE RULE]
```

**F-CH04-a-00741** · CH04-a:741 · Fails closed by · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:691, "(4) Grouping genuinely uncertain → live: ask Ness; unattended: hold as `thread_unresolved`.".
- Stays open: C-7E.7 Fails closed by (CH04-a:718), C-7E.8.4 Fails closed by (CH04-a:838) and C-7E.8.4 What it is still say "unattended"; after D-01 live material with an unresolved speaker or grouping enters the same hold, and the final build may widen those words. C-7E.8.4's TOGETHER boxes stay NOT DECIDED (its Appendix A rows unchanged). C-DETECT.2.5's authorized resolution rule and a clear-evidence rule for speakers and conversations stay open (OCT15:418).

Replaces:

```text
- Fails closed by: DESIGNED — Holds unattended uncertain grouping as `thread_unresolved`; live use asks Ness rather than inventing a group. [V10 §7E / SOURCE TITLE RULE]
```

With:

```text
- Fails closed by: DESIGNED — Holds unattended uncertain grouping as `thread_unresolved` rather than inventing a group. [V10 §7E / SOURCE TITLE RULE]
- Fails closed by: DECIDED-2026-10-15 — Holds live uncertain grouping as `thread_unresolved` too, rather than asking Ness or inventing a group. [D-2026-10-15-01] [V10 §7E / SOURCE TITLE RULE]
```

**F-CH04-a-00747** · CH04-a:747 · Gated by · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:691, "(4) Grouping genuinely uncertain → live: ask Ness; unattended: hold as `thread_unresolved`.".
- Stays open: C-7E.7 Fails closed by (CH04-a:718), C-7E.8.4 Fails closed by (CH04-a:838) and C-7E.8.4 What it is still say "unattended"; after D-01 live material with an unresolved speaker or grouping enters the same hold, and the final build may widen those words. C-7E.8.4's TOGETHER boxes stay NOT DECIDED (its Appendix A rows unchanged). C-DETECT.2.5's authorized resolution rule and a clear-evidence rule for speakers and conversations stay open (OCT15:418).

Replaces:

```text
- Gated by: DESIGNED — C-7E.8.4 — Uncertain grouping: genuine uncertainty requires live clarification or unattended holding. [V10 §7E / SOURCE TITLE RULE]
```

With:

```text
- Gated by: DECIDED-2026-10-15 — C-7E.8.4 — Uncertain grouping: genuine uncertainty leaves the material held as `thread_unresolved`, live or unattended; Ness is not asked. [D-2026-10-15-01] [V10 §7E / SOURCE TITLE RULE]
```

#### C-7E.8.2 — Untitled capture-session grouping

**F-CH04-a-00792** · CH04-a:792 · Fails closed by · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:691, "(4) Grouping genuinely uncertain → live: ask Ness; unattended: hold as `thread_unresolved`.".
- Stays open: C-7E.7 Fails closed by (CH04-a:718), C-7E.8.4 Fails closed by (CH04-a:838) and C-7E.8.4 What it is still say "unattended"; after D-01 live material with an unresolved speaker or grouping enters the same hold, and the final build may widen those words. C-7E.8.4's TOGETHER boxes stay NOT DECIDED (its Appendix A rows unchanged). C-DETECT.2.5's authorized resolution rule and a clear-evidence rule for speakers and conversations stay open (OCT15:418).

Replaces:

```text
- Fails closed by: DESIGNED — Genuinely uncertain grouping requires live clarification or unattended `thread_unresolved` holding. [V10 §7E / SOURCE TITLE RULE]
```

With:

```text
- Fails closed by: DECIDED-2026-10-15 — Genuinely uncertain grouping is held as `thread_unresolved`, live or unattended; Ness is not asked. [D-2026-10-15-01] [V10 §7E / SOURCE TITLE RULE]
```

#### C-7E.8.4 — Uncertain grouping

**F-CH04-a-00835** · CH04-a:835 · Does · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:691, "(4) Grouping genuinely uncertain → live: ask Ness; unattended: hold as `thread_unresolved`.".
- Stays open: C-7E.7 Fails closed by (CH04-a:718), C-7E.8.4 Fails closed by (CH04-a:838) and C-7E.8.4 What it is still say "unattended"; after D-01 live material with an unresolved speaker or grouping enters the same hold, and the final build may widen those words. C-7E.8.4's TOGETHER boxes stay NOT DECIDED (its Appendix A rows unchanged). C-DETECT.2.5's authorized resolution rule and a clear-evidence rule for speakers and conversations stay open (OCT15:418).

Replaces:

```text
- Does: DESIGNED — Asks Ness in live use; holds unattended material as `thread_unresolved`. [V10 §7E / SOURCE TITLE RULE]
```

With:

```text
- Does: DESIGNED — Holds unattended material as `thread_unresolved`. [V10 §7E / SOURCE TITLE RULE]
- Does: DECIDED-2026-10-15 — Holds live material as `thread_unresolved` too; never asks Ness which conversation it belongs to. [D-2026-10-15-01] [V10 §7E / SOURCE TITLE RULE]
```

**F-CH04-a-00836** · CH04-a:836 · Gives out · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:691, "(4) Grouping genuinely uncertain → live: ask Ness; unattended: hold as `thread_unresolved`.".
- Stays open: C-7E.7 Fails closed by (CH04-a:718), C-7E.8.4 Fails closed by (CH04-a:838) and C-7E.8.4 What it is still say "unattended"; after D-01 live material with an unresolved speaker or grouping enters the same hold, and the final build may widen those words. C-7E.8.4's TOGETHER boxes stay NOT DECIDED (its Appendix A rows unchanged). C-DETECT.2.5's authorized resolution rule and a clear-evidence rule for speakers and conversations stay open (OCT15:418).

Replaces:

```text
- Gives out: DESIGNED — A live clarification request or an unresolved-thread hold. [V10 §7E / SOURCE TITLE RULE]
```

With:

```text
- Gives out: DECIDED-2026-10-15 — An unresolved-thread hold, with no clarification request to Ness. [D-2026-10-15-01] [V10 §7E / SOURCE TITLE RULE]
```

**F-CH04-a-00848** · CH04-a:848 · USED BY · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:691, "(4) Grouping genuinely uncertain → live: ask Ness; unattended: hold as `thread_unresolved`.".
- Stays open: C-7E.7 Fails closed by (CH04-a:718), C-7E.8.4 Fails closed by (CH04-a:838) and C-7E.8.4 What it is still say "unattended"; after D-01 live material with an unresolved speaker or grouping enters the same hold, and the final build may widen those words. C-7E.8.4's TOGETHER boxes stay NOT DECIDED (its Appendix A rows unchanged). C-DETECT.2.5's authorized resolution rule and a clear-evidence rule for speakers and conversations stay open (OCT15:418).

Replaces:

```text
| 1 · DESIGNED | C-7E.5.2 — Blocker list | Material whose grouping is genuinely uncertain. | identifies `thread_unresolved` when unattended grouping cannot be established. | A live clarification request or an unresolved-thread hold. | [V10 §7E / SOURCE TITLE RULE] |
```

With:

```text
| 1 · DECIDED-2026-10-15 | C-7E.5.2 — Blocker list | Material whose grouping is genuinely uncertain. | identifies `thread_unresolved` when grouping cannot be established, live or unattended. | An unresolved-thread hold, with no clarification request to Ness. | [D-2026-10-15-01] [V10 §7E / SOURCE TITLE RULE] |
```

**F-CH04-a-00849** · CH04-a:849 · USED BY · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:691, "(4) Grouping genuinely uncertain → live: ask Ness; unattended: hold as `thread_unresolved`.".
- Stays open: C-7E.7 Fails closed by (CH04-a:718), C-7E.8.4 Fails closed by (CH04-a:838) and C-7E.8.4 What it is still say "unattended"; after D-01 live material with an unresolved speaker or grouping enters the same hold, and the final build may widen those words. C-7E.8.4's TOGETHER boxes stay NOT DECIDED (its Appendix A rows unchanged). C-DETECT.2.5's authorized resolution rule and a clear-evidence rule for speakers and conversations stay open (OCT15:418).

Replaces:

```text
| 2 · DESIGNED | C-7E.8 — Source-title and thread resolution | Material whose grouping is genuinely uncertain. | genuine uncertainty requires live clarification or unattended holding. | A live clarification request or an unresolved-thread hold. | [V10 §7E / SOURCE TITLE RULE] |
```

With:

```text
| 2 · DECIDED-2026-10-15 | C-7E.8 — Source-title and thread resolution | Material whose grouping is genuinely uncertain. | genuine uncertainty leaves the material held as `thread_unresolved`, live or unattended; Ness is not asked. | An unresolved-thread hold, with no clarification request to Ness. | [D-2026-10-15-01] [V10 §7E / SOURCE TITLE RULE] |
```

### CH04-d

#### Chapter header

**F-CH04-d-00010** · CH04-d:10 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Every citation resolves at the pinned commit.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Every citation resolves at the pinned commit. Decision key `D-2026-10-15-01`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-14.1 — Automatic live-turn capture

**F-CH04-d-00055** · CH04-d:55 · Does · `ready`

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:689, "Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`.".
- Stays open: C-7E.7 Fails closed by (CH04-a:718), C-7E.8.4 Fails closed by (CH04-a:838) and C-7E.8.4 What it is still say "unattended"; after D-01 live material with an unresolved speaker or grouping enters the same hold, and the final build may widen those words. C-7E.8.4's TOGETHER boxes stay NOT DECIDED (its Appendix A rows unchanged). C-DETECT.2.5's authorized resolution rule and a clear-evidence rule for speakers and conversations stay open (OCT15:418).

Replaces:

```text
- Does: DESIGNED — Captures automatically, then hands identifiable material to Catalog for completeness and resolution. Supplies stable unique `capture_id`, exact raw payload or immutable reference, capture timestamp, front-door/source type, media type, source metadata without reinterpretation and traceable capture provenance. Live Catalog may ask for necessary speaker or genuinely uncertain grouping clarification; unattended handling holds unresolved material and never asks. [V10 §14] [MAP C-14] [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE]
```

With:

```text
- Does: DESIGNED — Captures automatically, then hands identifiable material to Catalog for completeness and resolution. Supplies stable unique `capture_id`, exact raw payload or immutable reference, capture timestamp, front-door/source type, media type, source metadata without reinterpretation and traceable capture provenance. Unattended handling holds unresolved material and never asks. [V10 §14] [MAP C-14] [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE]
- Does: DECIDED-2026-10-15 — Live Catalog never asks for speaker or grouping clarification either; an unresolved speaker or genuinely uncertain grouping is held as unattended material is. [D-2026-10-15-01] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE]
```

### CH04-e

#### Chapter header

**F-CH04-e-00010** · CH04-e:10 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Every citation resolves at the pinned commit.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Every citation resolves at the pinned commit. Decision keys `D-2026-10-15-02 T3` and `D-2026-10-15-02 T4`, added after the pinned commit, name Ness's decisions quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-9A — Image ingest front door (§9A)

**F-CH04-e-00020** · CH04-e:20 · Does · `ready`

- Rule: D-2026-10-15-02 T3, "option A. Root first; the context-meaning stays a proposal beside it; Ness's" (OCT15:453).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:2843, "Metadata → plain-description → context-meaning → Ness confirms.".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The schema of a separate image confirmation or rejection event stays NOT DECIDED (STANDING T3). How the optional confirmation is surfaced (its notice form) is not designed. Unchanged: the meaning never becomes fact without Ness (C-9A.4 stays a prohibition), WhatsApp media stays frozen, live-camera help never stores automatically, in-world camera/VR keeps per-device approval (H1744).

Replaces:

```text
- Does: DESIGNED — Runs metadata → plain description → context-meaning proposal → Ness confirmation, then the Catalog route to an eligible root. Uses the same engine as text, video and audio; a new input type adds a front door. [V10 §9A] [MAP C-9A] [V10 §1A]
```

With:

```text
- Does: DESIGNED — Runs metadata → plain description → context-meaning proposal, and the Catalog route to an eligible root. Uses the same engine as text, video and audio; a new input type adds a front door. [V10 §9A] [MAP C-9A] [V10 §1A]
- Does: DECIDED-2026-10-15 — The image becomes a root through the Catalog route without waiting for Ness's confirmation; the context-meaning stays a proposal beside it. His confirmation is optional: it is surfaced, never asked. [D-2026-10-15-02 T3] [V10 §9A]
```

**F-CH04-e-00042** · CH04-e:42 · USED BY · `ready`

- Rule: D-2026-10-15-02 T3, "option A. Root first; the context-meaning stays a proposal beside it; Ness's" (OCT15:453).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:2843, "Metadata → plain-description → context-meaning → Ness confirms.".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The schema of a separate image confirmation or rejection event stays NOT DECIDED (STANDING T3). How the optional confirmation is surfaced (its notice form) is not designed. Unchanged: the meaning never becomes fact without Ness (C-9A.4 stays a prohibition), WhatsApp media stays frozen, live-camera help never stores automatically, in-world camera/VR keeps per-device approval (H1744).

Replaces:

```text
| 5 · DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E); P-MAIN step 1 | An image at the front door. | Runs the image proposal/confirmation sequence and common Catalog intake. | Eligible image material enters the main root path; the frozen WhatsApp branch remains disabled. | [V10 §1A] [MAP C-9A] |
```

With:

```text
| 5 · DECIDED-2026-10-15 | C-7E — Catalog Front Door + pre-ingest holding (§7E); P-MAIN step 1 | An image at the front door. | Runs the image proposal sequence and common Catalog intake; the image becomes a root without waiting for Ness's confirmation, which stays optional, surfaced and never asked. | Eligible image material enters the main root path; the frozen WhatsApp branch remains disabled. | [D-2026-10-15-02 T3] [V10 §1A] [MAP C-9A] |
```

**F-CH04-e-01540** · CH04-e:1540 · table row · `ready`

Place: Source-coverage row in CH04-e's back matter for the C-9A tree.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485). The [SOURCE CONFLICT: V10 §7Q prescribes stronger default restrictions ...] mark on C-9A.7.1.4 Does (CH04-e:427) stays visible (contract §1.5); D-02 T4 decides that conflict.

Replaces:

```text
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: §1A, §9A and §12 whole; §7Q whole, placing only current image/privacy boundaries and the age-default conflict. | C-9A and C-9A.1–5; frozen path in C-9A.7; privacy conflict retained; remaining §7Q owned by CH08-a. |
```

With:

```text
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: §1A, §9A and §12 whole; §7Q whole, placing only current image/privacy boundaries and the age-default question, decided by D-2026-10-15-02 T4 for A7 and A30. | C-9A and C-9A.1–5; frozen path in C-9A.7; privacy conflict decided for A30; remaining §7Q owned by CH08-a. |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH04-e-00425** · CH04-e:425 · What it is · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485). The [SOURCE CONFLICT: V10 §7Q prescribes stronger default restrictions ...] mark on C-9A.7.1.4 Does (CH04-e:427) stays visible (contract §1.5); D-02 T4 decides that conflict.

Replaces:

```text
- What it is: ACCEPTED — The accepted A30 ordinary privacy and third-party handling target, with the governing age-default disagreement explicitly retained. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30]
```

With:

```text
- What it is: ACCEPTED — The accepted A30 ordinary privacy and third-party handling target. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30]
- What it is: DECIDED-2026-10-15 — The V10 age default no longer governs it: A7 removed that rule, so A30's target governs. [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.2]
```

**F-CH04-e-00428** · CH04-e:428 · Gives out · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485). The [SOURCE CONFLICT: V10 §7Q prescribes stronger default restrictions ...] mark on C-9A.7.1.4 Does (CH04-e:427) stays visible (contract §1.5); D-02 T4 decides that conflict.

Replaces:

```text
- Gives out: ACCEPTED — Material subject to all ordinary protections, with no claim that the opposing age-default rules have been integrated or reconciled. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30]
```

With:

```text
- Gives out: ACCEPTED — Material subject to all ordinary protections. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30]
- Gives out: DECIDED-2026-10-15 — No automatic age or vulnerability restriction is added; the V10 age default no longer applies. [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.2]
```

**F-CH04-e-00434** · CH04-e:434 · Gated by · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485). The [SOURCE CONFLICT: V10 §7Q prescribes stronger default restrictions ...] mark on C-9A.7.1.4 Does (CH04-e:427) stays visible (contract §1.5); D-02 T4 decides that conflict.

Replaces:

```text
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy, compartment and external-use authorization must hold; the V10 age-default conflict remains explicit. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30] [V10 §7Q / THIRD-PARTY DATA RULES]
```

With:

```text
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy, compartment and external-use authorization must hold. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30] [V10 §7Q / THIRD-PARTY DATA RULES]
- Gated by: DECIDED-2026-10-15 — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the V10 age default no longer applies; A7 and A30 govern. [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.2]
```

**F-CH04-e-00440** · CH04-e:440 · USED BY · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485). The [SOURCE CONFLICT: V10 §7Q prescribes stronger default restrictions ...] mark on C-9A.7.1.4 Does (CH04-e:427) stays visible (contract §1.5); D-02 T4 decides that conflict.

Replaces:

```text
| 1 · ACCEPTED | C-9A.7.1 — Five-stage WhatsApp pipeline | Third-party handling requirements. | Preserves the applicable privacy boundary and explicit source disagreement. | No age-policy reconciliation is silently invented. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30] |
```

With:

```text
| 1 · DECIDED-2026-10-15 | C-9A.7.1 — Five-stage WhatsApp pipeline | Third-party handling requirements. | Preserves the applicable privacy boundary under A30; the age-policy disagreement is decided for A7 and A30. | No automatic age restriction is added. | [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.2] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30] |
```

**F-CH04-e-01401** · CH04-e:1401 · register row · `ready`

Place: Source-conflict table row in CH04-e's back matter for C-9A.7.1.4.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485). The [SOURCE CONFLICT: V10 §7Q prescribes stronger default restrictions ...] mark on C-9A.7.1.4 Does (CH04-e:427) stays visible (contract §1.5); D-02 T4 decides that conflict.

Replaces:

```text
| [SOURCE CONFLICT] | V10 §7Q / THIRD-PARTY DATA RULES requires stronger default restriction for minors and highly vulnerable people. Bundle 6 policy §4 A30 and mechanical §11 B22 prohibit automatic stronger restriction, block, weakened analysis or special simulation prohibition solely for age or vulnerability. | V10 remains governing. The accepted opposing target is preserved explicitly in C-9A.7.1.4; no reconciliation or hidden integration is chosen. |
```

With:

```text
| [SOURCE CONFLICT] | V10 §7Q / THIRD-PARTY DATA RULES requires stronger default restriction for minors and highly vulnerable people. Bundle 6 policy §4 A30 and mechanical §11 B22 prohibit automatic stronger restriction, block, weakened analysis or special simulation prohibition solely for age or vulnerability. | Decided by D-2026-10-15-02 T4: A7 removed the V10 rule (A7 §6.2), so the A30 target in C-9A.7.1.4 governs. |
```

### CH05-b

#### Chapter header

**F-CH05-b-00010** · CH05-b:10 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Every citation resolves at the pinned commit.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Every citation resolves at the pinned commit. Decision key `D-2026-10-15-02 T2`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A)

**F-CH05-b-00030** · CH05-b:30 · Fed by · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Fed by: DESIGNED — C-7GA.10 — thread_membership_v1: Uses the new-root assignment rule's explicit inputs and mode limits. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
```

With:

```text
- Fed by: DESIGNED — C-7GA.10 — thread_membership_v1: Uses the new-root assignment rule's explicit inputs. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DECIDED-2026-10-15 — The first reading's mode follows R4 (the largest accumulated context available); version 1's bare or local-context limit no longer governs it, and the successor rule version is NOT DECIDED. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

**F-CH05-b-00062** · CH05-b:62 · USED BY · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
| 11 · DESIGNED | C-7GA.10 — thread_membership_v1; P-MAIN step 7 | Step 7: derived assignment inputs and trigger. | Runs thread_membership_v1 and writes a durable instruction. | The pass has an explicit permitted mode before retrieval. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
```

With:

```text
| 11 · DECIDED-2026-10-15 | C-7GA.10 — thread_membership_v1; P-MAIN step 7 | Step 7: derived assignment inputs and trigger. | Runs the new-root mode-assignment rule, whose successor version is NOT DECIDED (version 1 no longer governs the first reading, which follows R4), and writes a durable instruction. | The pass has an explicit permitted mode before retrieval. | [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9] [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
```

**F-CH05-b-04391** · CH05-b:4391 · other · `ready`

Place: Prose paragraph in CH05-b's back matter about the C-7GA tree.

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
The root has separate USED BY rows for its five P-MAIN placements (steps 5, 6, 7, 13 and 16), CY-A and the asynchronous segment of CY-B. Every descendant inherits those placements through the sub-part tree. Full side-path assembly remains CH11, and full chat-response synchronization remains outside this post-root design. The wider instruction schema vocabulary does not weaken thread_membership_v1's permanent bare/local-context restriction.
```

With:

```text
The root has separate USED BY rows for its five P-MAIN placements (steps 5, 6, 7, 13 and 16), CY-A and the asynchronous segment of CY-B. Every descendant inherits those placements through the sub-part tree. Full side-path assembly remains CH11, and full chat-response synchronization remains outside this post-root design. thread_membership_v1's bare/local-context restriction belongs to version 1, which no longer governs the first reading (R4; D-2026-10-15-02 T2); the successor rule version is NOT DECIDED.
```

**F-CH05-b-04425** · CH05-b:4425 · other · `ready`

Place: Remaining-scope prose bullet in CH05-b's back matter, pointing to CH05-c's C-7F.

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- **CH05-c, C-7F:** full retrieval contract, parameter schema and empirically unresolved quantities. Current worker behavior includes its own bare/positional routes, empty-result handling, authorization, provenance and technical-failure response. Engine B's n=3 remains experiment-specific.
```

With:

```text
- **CH05-c, C-7F:** full retrieval contract, parameter schema and empirically unresolved quantities. Current worker behavior includes its own context routes (for a first reading they follow R4, D-2026-10-15-02 T2; the successor rule version is NOT DECIDED), empty-result handling, authorization, provenance and technical-failure response. Engine B's n=3 remains experiment-specific.
```

#### C-7GA.5.1.7 — Job trigger_override_reason

**F-CH05-b-00470** · CH05-b:470 · Does · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Does: DESIGNED — Carries it to the override gate; live_ingestion narrowing to bare requires a non-empty reason. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
```

With:

```text
- Does: DESIGNED — Carries it to the new-root mode-assignment rule. Under version 1, live_ingestion narrowing to bare requires a non-empty reason. [V10 §7G-A / THE ASYNCHRONOUS PERSISTENT LOCAL READING QUEUE] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DECIDED-2026-10-15 — Version 1 no longer governs the first reading; how the successor rule version uses this reason is NOT DECIDED. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

#### C-7GA.8.1 — reading_pass_instruction

**F-CH05-b-02095** · CH05-b:2095 · Fed by · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1920, "rule_version: 1".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Fed by: DESIGNED — C-7GA.8.1.7 — mode_rule_version: Records rule version 1. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
```

With:

```text
- Fed by: DESIGNED — C-7GA.8.1.7 — mode_rule_version: Records the version of the rule that assigned the mode: 1 for version 1. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DECIDED-2026-10-15 — C-7GA.8.1.7 — mode_rule_version: The version of the successor rule that governs first readings under R4 is NOT DECIDED. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

**F-CH05-b-02110** · CH05-b:2110 · USED BY · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
| 2 · DESIGNED | C-7GA.11.2 — Step 2 — Retrieve context through LMAC | Recorded pass mode. | Selects bare or positional context. | No retrieval before the pass contract. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |
```

With:

```text
| 2 · DECIDED-2026-10-15 | C-7GA.11.2 — Step 2 — Retrieve context through LMAC | Recorded pass mode. | Selects the context the recorded mode permits; for a first reading that follows R4, and the successor rule version's retrieval is NOT DECIDED. | No retrieval before the pass contract. | [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] |
```

#### C-7GA.8.1.5 — assigned_mode

**F-CH05-b-02213** · CH05-b:2213 · Does · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Does: DESIGNED — Stores the assigned reading mode; thread_membership_v1 permits only bare or local-context despite the wider schema vocabulary. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
```

With:

```text
- Does: DESIGNED — Stores the assigned reading mode. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Does: DECIDED-2026-10-15 — Which modes may be assigned to a first reading belongs to the successor version of thread_membership_v1 and is NOT DECIDED; version 1's bare or local-context limit no longer governs the first reading, which follows R4. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

**F-CH05-b-02215** · CH05-b:2215 · Must never · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Must never: DESIGNED — Let this rule assign associative or combined merely because the schema lists them. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
```

With:

```text
- Must never: DESIGNED — Under version 1, let thread_membership_v1 assign associative or combined merely because the schema lists them. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
```

**F-CH05-b-02216** · CH05-b:2216 · Fails closed by · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Fails closed by: DESIGNED — A path producing either prohibited mode falls back to bare and records an implementation error. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
```

With:

```text
- Fails closed by: DESIGNED — Under version 1, a path producing associative or combined falls back to bare and records an implementation error. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DECIDED-2026-10-15 — The successor rule version's fallback for a first reading is NOT DECIDED. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

**F-CH05-b-02226** · CH05-b:2226 · USED BY · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
| 1 · DESIGNED | C-7GA.8.1 — reading_pass_instruction | assigned_mode. | Declares the pass's reading mode. | Wider schema vocabulary grants no prohibited mode. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
```

With:

```text
| 1 · DECIDED-2026-10-15 | C-7GA.8.1 — reading_pass_instruction | assigned_mode. | Declares the pass's reading mode. | Wider schema vocabulary grants no mode by itself; which modes a first reading may receive is NOT DECIDED (successor rule version under R4). | [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9] [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
```

#### C-7GA.8.1.6 — mode_rule_id

**F-CH05-b-02235** · CH05-b:2235 · Takes in · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Takes in: DESIGNED — `thread_membership_v1`. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
```

With:

```text
- Takes in: DESIGNED — The rule_id of the new-root mode-assignment rule that assigned the mode: `thread_membership_v1` for version 1. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DECIDED-2026-10-15 — The rule_id of the successor version that governs first readings under R4 is NOT DECIDED. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

**F-CH05-b-02249** · CH05-b:2249 · USED BY · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
| 1 · DESIGNED | C-7GA.8.1 — reading_pass_instruction | mode_rule_id. | Binds assignment to thread_membership_v1. | No reread policy inferred. | [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
```

With:

```text
| 1 · DECIDED-2026-10-15 | C-7GA.8.1 — reading_pass_instruction | mode_rule_id. | Binds assignment to the rule that assigned it: thread_membership_v1 for version 1; the successor version for first readings is NOT DECIDED. | No reread policy inferred. | [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9] [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
```

#### C-7GA.8.1.7 — mode_rule_version

**F-CH05-b-02258** · CH05-b:2258 · Takes in · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1920, "rule_version: 1".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Takes in: DESIGNED — Rule version `1`. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
```

With:

```text
- Takes in: DESIGNED — The version of the new-root mode-assignment rule that assigned the mode: `1` for version 1. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Takes in: DECIDED-2026-10-15 — The version of the successor rule that governs first readings under R4 is NOT DECIDED. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

#### C-7GA.8.1.8 — assignment_inputs

**F-CH05-b-02285** · CH05-b:2285 · Fails closed by · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Fails closed by: DESIGNED — Unknown or missing grouping classification takes the safe bare default with its reason. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
```

With:

```text
- Fails closed by: DESIGNED — Under version 1, unknown or missing grouping classification takes the safe bare default with its reason. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DECIDED-2026-10-15 — The successor rule version's handling of unknown or missing grouping for a first reading is NOT DECIDED. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

#### C-7GA.8.1.8.1 — source_title_type

**F-CH05-b-02319** · CH05-b:2319 · Fails closed by · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Fails closed by: DESIGNED — Unrecognized, missing or uncertain grouping defaults to bare. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
```

With:

```text
- Fails closed by: DESIGNED — Under version 1, unrecognized, missing or uncertain grouping defaults to bare. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DECIDED-2026-10-15 — The successor rule version's default for a first reading is NOT DECIDED. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

#### C-7GA.8.1.8.2 — thread_present

**F-CH05-b-02342** · CH05-b:2342 · Fails closed by · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Fails closed by: DESIGNED — local-context still requires a confirmed grouping and the declared preceding-context condition. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
```

With:

```text
- Fails closed by: DESIGNED — Under version 1, local-context still requires a confirmed grouping and the declared preceding-context condition. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DECIDED-2026-10-15 — Whether the successor rule version uses this condition for a first reading is NOT DECIDED. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

#### C-7GA.8.1.8.3 — thread_root_count

**F-CH05-b-02365** · CH05-b:2365 · Fails closed by · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Fails closed by: DESIGNED — The local-context default requires thread_present true and count at least one with confirmed grouping. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
```

With:

```text
- Fails closed by: DESIGNED — Under version 1, the local-context default requires thread_present true and count at least one with confirmed grouping. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DECIDED-2026-10-15 — Whether the successor rule version uses this count for a first reading is NOT DECIDED. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

#### C-7GA.8.1.10 — assignment_reason

**F-CH05-b-02595** · CH05-b:2595 · Fails closed by · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Fails closed by: DESIGNED — Unrecognized/missing grouping yields bare with its safe-fallback reason. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
```

With:

```text
- Fails closed by: DESIGNED — Under version 1, unrecognized or missing grouping yields bare with its safe-fallback reason. [V10 §7G-A / THE READING-PASS INSTRUCTION AND LOG] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fails closed by: DECIDED-2026-10-15 — The successor rule version's reasons for a first reading are NOT DECIDED. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

#### C-7GA.10 — thread_membership_v1

**F-CH05-b-03067** · CH05-b:3067 · What it is · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- What it is: DESIGNED — The deterministic new-root mode-assignment rule, rule_id thread_membership_v1 and rule_version 1. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
```

With:

```text
- What it is: DESIGNED — The deterministic new-root mode-assignment rule, rule_id thread_membership_v1 and rule_version 1. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- What it is: DECIDED-2026-10-15 — Version 1 no longer governs the first reading of a new root: R4 governs it (the largest accumulated context available). The successor rule version is NOT DECIDED, and the build blocker on the first reading stays until it is designed. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

**F-CH05-b-03085** · CH05-b:3085 · USED BY · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
| 1 · DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | Trigger and derived grouping/count inputs. | Assigns bare or local-context. | No associative/combined mode under version 1. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
```

With:

```text
| 1 · DECIDED-2026-10-15 | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | Trigger and derived grouping/count inputs. | Version 1 (bare or local-context) no longer assigns the first reading's mode; the successor rule version under R4 is NOT DECIDED. | No first-reading mode is assigned until the successor version exists. | [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9] [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
```

**F-CH05-b-03088** · CH05-b:3088 · USED BY · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
| 4 · DESIGNED | C-7GA.11.1 — Step 1 — Create instruction | Derived grouping/count and trigger inputs. | Creates the declared pass. | No prohibited mode or raw-title guess. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
```

With:

```text
| 4 · DECIDED-2026-10-15 | C-7GA.11.1 — Step 1 — Create instruction | Derived grouping/count and trigger inputs. | Creates the declared pass with the mode the successor rule version assigns (NOT DECIDED); version 1 no longer governs the first reading. | No raw-title guess. | [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
```

**F-CH05-b-03089** · CH05-b:3089 · USED BY · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
| 5 · DESIGNED | C-7F.2 — Conceptual channel combinations | The explicitly designed reading mode. | Gates this place: new-root use still follows the job's mode restrictions. | Nothing in this card. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
```

With:

```text
| 5 · DECIDED-2026-10-15 | C-7F.2 — Conceptual channel combinations | The explicitly designed reading mode. | Gates this place: new-root use follows the mode the new-root rule assigns; version 1's restriction no longer governs the first reading, and the successor version is NOT DECIDED. | Nothing in this card. | [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9] [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
```

#### C-7GA.11.1 — Step 1 — Create instruction

**F-CH05-b-03499** · CH05-b:3499 · Does · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Does: DESIGNED — Derives all inputs, runs thread_membership_v1, validates the claim and appends the instruction to `.nh_reading_pass_log.jsonl` before retrieval. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
```

With:

```text
- Does: DESIGNED — Derives all inputs, runs the new-root mode-assignment rule, validates the claim and appends the instruction to `.nh_reading_pass_log.jsonl` before retrieval. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DECIDED-2026-10-15 — The rule it runs for a first reading is the successor version of thread_membership_v1 (NOT DECIDED); thread_membership_v1 (version 1, bare or local-context only) no longer governs it. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

**F-CH05-b-03505** · CH05-b:3505 · Fed by · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Fed by: DESIGNED — C-7GA.10 — thread_membership_v1: Runs the exact new-root mode-assignment rule. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
```

With:

```text
- Fed by: DESIGNED — C-7GA.10 — thread_membership_v1: Runs the exact new-root mode-assignment rule. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Fed by: DECIDED-2026-10-15 — For a first reading that rule is the successor version (NOT DECIDED); thread_membership_v1 (version 1, bare or local-context only) no longer governs it. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

#### C-7GA.11.2 — Step 2 — Retrieve context through LMAC

**F-CH05-b-03523** · CH05-b:3523 · Takes in · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Takes in: DESIGNED — bare or local-context and current purpose-specific authorization. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
```

With:

```text
- Takes in: DESIGNED — The pass's recorded mode and current purpose-specific authorization. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Takes in: DECIDED-2026-10-15 — For a first reading the mode follows R4; which modes the successor rule version assigns is NOT DECIDED, so the input is not limited to bare or local-context. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

**F-CH05-b-03524** · CH05-b:3524 · Does · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Does: DESIGNED — bare returns an empty package immediately without retrieval. local-context asks LMAC to route to positional retrieval of immediately preceding roots in the same confirmed grouping, with provenance and a section separate from the target. Uses the per-mode limit; Engine B's n=3 belongs only to its built experiment. Empty positional results are normal and continue target-only. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
```

With:

```text
- Does: DESIGNED — bare returns an empty package immediately without retrieval. local-context asks LMAC to route to positional retrieval of immediately preceding roots in the same confirmed grouping, with provenance and a section separate from the target. Uses the per-mode limit; Engine B's n=3 belongs only to its built experiment. Empty positional results are normal and continue target-only. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Does: DECIDED-2026-10-15 — For a first reading, retrieval follows R4 (the largest accumulated context available) instead of being limited to these two modes; the retrieval the successor rule version selects is NOT DECIDED. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

**F-CH05-b-03525** · CH05-b:3525 · Gives out · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Gives out: DESIGNED — Authorized positional context or an honest empty package. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
```

With:

```text
- Gives out: DESIGNED — Authorized context with provenance, or an honest empty package. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Gives out: DECIDED-2026-10-15 — For a first reading the authorized context is the widest accumulated context the successor rule version retrieves (NOT DECIDED), not only positional context. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

**F-CH05-b-03531** · CH05-b:3531 · Fed by · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Fed by: DESIGNED — C-7F — Context Retrieval (§7F): Receives immediately preceding roots in the confirmed grouping or an empty package. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
```

With:

```text
- Fed by: DESIGNED — C-7F — Context Retrieval (§7F): Receives the context the pass's mode permits, or an empty package. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
- Fed by: DECIDED-2026-10-15 — For a first reading that context follows R4, not only immediately preceding roots in the confirmed grouping; the successor rule version is NOT DECIDED. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

**F-CH05-b-03539** · CH05-b:3539 · USED BY · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
| 1 · DESIGNED | C-7GA.11 — Worker pass sequence | Authorized positional or empty package. | Supplies separated background. | Empty context is a normal condition. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
```

With:

```text
| 1 · DECIDED-2026-10-15 | C-7GA.11 — Worker pass sequence | Authorized context or empty package; for a first reading the context follows R4 (successor rule version NOT DECIDED). | Supplies separated background. | Empty context is a normal condition. | [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
```

#### C-7GA.13.4 — RC-3 — in_progress without instruction

**F-CH05-b-04095** · CH05-b:4095 · Does · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Does: DESIGNED — Runs thread_membership_v1 fresh, validates the claim, appends a durable instruction and proceeds to RC-4. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
```

With:

```text
- Does: DESIGNED — Runs the new-root mode-assignment rule fresh, validates the claim, appends a durable instruction and proceeds to RC-4. [V10 §7G-A / CRASH RECOVERY SEQUENCE]
- Does: DECIDED-2026-10-15 — For a first reading that rule is the successor version of thread_membership_v1 (NOT DECIDED); thread_membership_v1 (version 1, bare or local-context only) no longer governs it. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

#### C-7F — Context Retrieval (§7F)

**F-CH05-b-04364** · CH05-b:4364 · USED BY · `ready`

Place: Cross-piece USED BY continuation row in CH05-b's back matter: C-7F supplying C-7GA.11.2.

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
| C-7F — Context Retrieval (§7F) | DESIGNED — C-7GA.11.2 — Step 2 — Retrieve context through LMAC | Positional results and provenance. | Keeps background separate from target. | No empirical limit invented from Engine B. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
```

With:

```text
| C-7F — Context Retrieval (§7F) | DECIDED-2026-10-15 | C-7GA.11.2 — Step 2 — Retrieve context through LMAC | Context results and provenance; for a first reading the context follows R4 (successor rule version NOT DECIDED), not only positional results. | Keeps background separate from target. | No empirical limit invented from Engine B. | [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
```

**F-CH05-b-04381** · CH05-b:4381 · USED BY · `ready`

Place: Cross-piece USED BY continuation row in CH05-b's back matter: C-7F supplying C-7GA.

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
| C-7F — Context Retrieval (§7F) | DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | The worker context-assembly step with bare/local-context restriction. | Retrieves eligible preceding material or honestly returns none. | The downstream pass keeps actual context provenance and technical failure separate. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
```

With:

```text
| C-7F — Context Retrieval (§7F) | DECIDED-2026-10-15 | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | The worker context-assembly step; for a first reading it follows R4, and the successor rule version that replaces version 1's bare/local-context restriction is NOT DECIDED. | Retrieves eligible material or honestly returns none. | The downstream pass keeps actual context provenance and technical failure separate. | [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
```

### CH05-c

#### Chapter header

**F-CH05-c-00010** · CH05-c:10 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Every citation resolves at the pinned commit.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Every citation resolves at the pinned commit. Decision key `D-2026-10-15-02 T2`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7F — Context Retrieval (§7F)

**F-CH05-c-00056** · CH05-c:56 · USED BY · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
| 12 · DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A); CY-A | The worker context-assembly step with bare/local-context restriction. | Retrieves eligible preceding material or honestly returns none. | The downstream pass keeps actual context provenance and technical failure separate. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
```

With:

```text
| 12 · DECIDED-2026-10-15 | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A); CY-A | The worker context-assembly step; for a first reading it follows R4 (successor rule version NOT DECIDED), not version 1's bare/local-context restriction. | Retrieves eligible material or honestly returns none. | The downstream pass keeps actual context provenance and technical failure separate. | [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
```

**F-CH05-c-03144** · CH05-c:3144 · other · `ready`

Place: Prose paragraph in CH05-c's back matter about C-7F.

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
The B1 mode and audit structures are accepted designs with proposed field names and final serialization open. Every bound and ceiling value remains empirical and open. The four conceptual channel categories do not override the new-root worker's permanent bare/local-context restriction. Engine B n=3 is not a general default. A4's eight required fields are concretely supplied by the declaration's component identity, purpose, selected mode, reason, uncertainty behavior, allowed use, audit and fail-closed rules; shared structure retains the same current IDs where reused.
```

With:

```text
The B1 mode and audit structures are accepted designs with proposed field names and final serialization open. Every bound and ceiling value remains empirical and open. The four conceptual channel categories are not limited for a first reading by version 1's bare/local-context restriction, which no longer governs it (R4; D-2026-10-15-02 T2); the successor rule version is NOT DECIDED. Engine B n=3 is not a general default. A4's eight required fields are concretely supplied by the declaration's component identity, purpose, selected mode, reason, uncertainty behavior, allowed use, audit and fail-closed rules; shared structure retains the same current IDs where reused.
```

#### C-7F.2 — Conceptual channel combinations

**F-CH05-c-00220** · CH05-c:220 · Gated by · `ready`

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
- Gated by: DESIGNED — C-7GA.10 — thread_membership_v1: New-root use still follows the job's mode restrictions. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
```

With:

```text
- Gated by: DESIGNED — C-7GA.10 — thread_membership_v1: New-root use follows the mode the new-root rule assigns. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Gated by: DECIDED-2026-10-15 — For a first reading that mode follows R4; version 1's restriction no longer governs it, and the successor rule version is NOT DECIDED. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

#### C-7GA.10 — thread_membership_v1

**F-CH05-c-03130** · CH05-c:3130 · USED BY · `ready`

Place: Cross-piece USED BY continuation row in CH05-c's back matter: C-7GA.10 gating C-7F.2.

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
| C-7GA.10 — thread_membership_v1 | DESIGNED — C-7F.2 — Conceptual channel combinations | New-root assignment. | Limits this trigger to bare or local-context. | No associative/combined bypass. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
```

With:

```text
| C-7GA.10 — thread_membership_v1 | DECIDED-2026-10-15 | C-7F.2 — Conceptual channel combinations | New-root assignment. | Version 1 limited this trigger to bare or local-context; it no longer governs the first reading, which follows R4, and the successor rule version is NOT DECIDED. | No first-reading mode limit comes from version 1. | [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9] [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
```

**F-CH05-c-03169** · CH05-c:3169 · other · `ready`

Place: Boundary table row in CH05-c's back matter about C-7GA.10 and C-7F.

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
| Abstract combinations versus trigger permission | V10 §7F names four conceptual combinations. The new-root thread_membership_v1 rule permanently prohibits associative/combined and falls back to bare with an implementation-error record if either is produced. [V10 §7F] [V10 §7G-A / MODE-ASSIGNMENT RULE:] | The four categories remain conceptual; the worker-specific restriction continues unchanged under C-7GA.10. No semantic retrieval is enabled for that trigger by this chapter. |
```

With:

```text
| Abstract combinations versus trigger permission | V10 §7F names four conceptual combinations. Version 1 of the new-root rule thread_membership_v1 prohibits associative/combined and falls back to bare with an implementation-error record if either is produced; version 1 no longer governs the first reading, which follows R4 (D-2026-10-15-02 T2). [V10 §7F] [V10 §7G-A / MODE-ASSIGNMENT RULE:] | The four categories remain conceptual; the successor rule version for the first reading is NOT DECIDED. No semantic retrieval is enabled for that trigger by this chapter. |
```

#### C-7GA.11.2 — Step 2 — Retrieve context through LMAC

**F-CH05-c-03159** · CH05-c:3159 · USED BY · `ready`

Place: Cross-piece link table row in CH05-c's back matter for C-7GA.11.2's Fed by.

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
| C-7GA.11.2 — Step 2 — Retrieve context through LMAC | Fed by | C-7F — Context Retrieval (§7F) | DESIGNED — Receives authorized preceding context or an honest empty outcome under the new-root mode rule. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
```

With:

```text
| C-7GA.11.2 — Step 2 — Retrieve context through LMAC | Fed by | C-7F — Context Retrieval (§7F) | DECIDED-2026-10-15 — Receives authorized context or an honest empty outcome under the new-root mode rule; for a first reading the context follows R4, and the successor rule version is NOT DECIDED. | [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
```

### CH08-a

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH08-a-00012** · CH08-a:12 · other · `ready`

Place: Chapter header SOURCE CONFLICT paragraph of CH08-a, before the first card (the C-7Q tree).

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules.

Replaces:

```text
[SOURCE CONFLICT] V10 §7Q requires stronger authorization at each later third-party operation. Accepted A7 §§4.5/4.6/6.1 and B7 §§3/17 permit ordinary bounded interpretation without separate permission. V10 governs; compatible interpretation labels and full-simulation approval remain explicit.
```

With:

```text
[SOURCE CONFLICT] V10 §7Q requires stronger authorization at each later third-party operation. Accepted A7 §§4.5/4.6/6.1 and B7 §§3/17 permit ordinary bounded interpretation without separate permission. By D-2026-10-15-02 T4, A7 governs: ordinary bounded interpretation (operation 3) needs no separate permission, and a constructed model of the person (operation 4) is the full simulation that needs Ness's clear prior approval. Compatible interpretation labels remain explicit. Operation 2 (recording what another person said or did) needs only the existing capture and third-party rules, by Ness's answer of 2026-10-29 (D-2026-10-29-04).
```

**F-CH08-a-00014** · CH08-a:14 · other · `ready`

Place: Chapter header SOURCE CONFLICT paragraph of CH08-a, before the first card (the C-7Q tree).

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
[SOURCE CONFLICT] V10 §7Q requires stronger defaults for minors and vulnerable people. Accepted A7 §§4.7/6.2, B7 §§3/17 and Bundle 6 A30 remove automatic age/vulnerability restrictions. Bundle 5 §8 calls the V10 sentence frozen predecision wording and the accepted policy a settled slot; that competing explanation is preserved. Under build-contract §1.5 V10 still governs. CH04-e’s existing marked disagreement is carried forward.
```

With:

```text
[SOURCE CONFLICT] V10 §7Q requires stronger defaults for minors and vulnerable people. Accepted A7 §§4.7/6.2, B7 §§3/17 and Bundle 6 A30 remove automatic age/vulnerability restrictions. Bundle 5 §8 calls the V10 sentence frozen predecision wording and the accepted policy a settled slot. By D-2026-10-15-02 T4 the automatic minors/vulnerable rule is removed: A7 governs, age or vulnerability alone change nothing, and only Ness's explicit person- or group-specific configuration gives different handling. CH04-e's marked disagreement is decided the same way.
```

**F-CH08-a-12144** · CH08-a:12144 · other · `ready`

Place: Scope paragraph in CH08-a's back matter about the C-7Q tree.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
Third-party handling retains the universal floor, contextual factors, stricter-only controls, the four-operation ladder, hypothetical labels, full-simulation approval and import/public limits. Three source conflicts are marked in the header and affected cards: destructive/five-operation/older-outcome wording, the interpretation authorization ladder, and the minor/vulnerable default. Bundle 5’s own explanation that the last is frozen predecision wording is preserved as losing wording under the contract’s V10 precedence. No conflict has been silently reconciled. A7’s compatible natural-language pause/reopening, actual-words scope, one-short-clarification rule, truthful transformation and normal longitudinal use remain explicit.
```

With:

```text
Third-party handling retains the universal floor, contextual factors, stricter-only controls, the four-operation ladder, hypothetical labels, full-simulation approval and import/public limits. Three source conflicts are marked in the header and affected cards: destructive/five-operation/older-outcome wording, the interpretation authorization ladder, and the minor/vulnerable default. By D-2026-10-15-02 T4, A7 governs the last two: ordinary bounded interpretation needs no separate permission, and no automatic minor/vulnerable restriction exists; Bundle 5's explanation of the minor default as frozen predecision wording agrees. The first conflict is still not reconciled. A7’s compatible natural-language pause/reopening, actual-words scope, one-short-clarification rule, truthful transformation and normal longitudinal use remain explicit.
```

**F-CH08-a-12164** · CH08-a:12164 · table row · `ready`

Place: Source-coverage row in CH08-a's back matter for the C-7Q tree.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### Chapter header

**F-CH08-a-00016** · CH08-a:16 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`, used only for the F9 passage expressly restored through FR-0108 by the cited September 25 decision record. NHD identifiers locate decisions and do not replace behavior citations.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`, used only for the F9 passage expressly restored through FR-0108 by the cited September 25 decision record. NHD identifiers locate decisions and do not replace behavior citations. Decision keys `D-2026-10-15-02 T4` and `D-2026-10-29-04`, added after the pinned commit, name Ness's decisions quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH08-a-00062** · CH08-a:62 · USED BY · `ready`

Place: USED BY row of the C-7Q root card naming C-9A.7.1.4 (the reader recorded the named card).

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| 21 · ACCEPTED | C-9A.7.1.4 — WhatsApp privacy stage | Privacy, compartment and external-use authorization. | Preserves the governing V10 age-default conflict. | Deferred intake cannot silently choose a weaker default. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [V10 §7Q / THIRD-PARTY DATA RULES] |
```

With:

```text
| 21 · DECIDED-2026-10-15 | C-9A.7.1.4 — WhatsApp privacy stage | Privacy, compartment and external-use authorization. | Applies A30's ordinary privacy and third-party target; the V10 age default no longer governs. | Deferred intake keeps every ordinary protection and adds no automatic age restriction. | [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.2] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] |
```

**F-CH08-a-11978** · CH08-a:11978 · USED BY · `ready`

Place: Cross-piece USED BY continuation row in CH08-a's back matter: C-7Q gating C-9A.7.1.4.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-9A.7.1.4 — WhatsApp privacy stage | Privacy, compartment and external-use authorization. | Preserves the governing V10 age-default conflict. | Deferred intake cannot silently choose a weaker default. | ACCEPTED | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [V10 §7Q / THIRD-PARTY DATA RULES] |
```

With:

```text
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-9A.7.1.4 — WhatsApp privacy stage | Privacy, compartment and external-use authorization. | Applies A30's ordinary privacy and third-party target; the V10 age default no longer governs. | Deferred intake keeps every ordinary protection and adds no automatic age restriction. | DECIDED-2026-10-15 | [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.2] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] |
```

**F-CH08-a-12176** · CH08-a:12176 · table row · `ready`

Place: Source-coverage row in CH08-a's back matter for C-9A.7.1.4.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-7Q.5 — Third-party data baseline

**F-CH08-a-01753** · CH08-a:1753 · Fed by · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
- Fed by: DESIGNED — C-7Q.5.1 — Context-sensitive third-party handling: contextual factors; C-7Q.5.2 — Stricter person and group controls: stricter person/group controls; C-7Q.5.3 — Four-operation third-party authorization ladder: the four-operation authorization ladder; C-7Q.5.4 — Third-party simulation boundary: simulation labeling and approval; C-7Q.5.5 — Stronger minor and vulnerable-person defaults: stronger minor/vulnerable defaults; C-7Q.5.6 — Large-import and public-source limits: import/public limits. [V10 §7Q]
```

With:

```text
- Fed by: DESIGNED — C-7Q.5.1 — Context-sensitive third-party handling: contextual factors; C-7Q.5.2 — Stricter person and group controls: stricter person/group controls; C-7Q.5.3 — Four-operation third-party authorization ladder: the four-operation authorization ladder; C-7Q.5.4 — Third-party simulation boundary: simulation labeling and approval; C-7Q.5.6 — Large-import and public-source limits: import/public limits. [V10 §7Q]
- Fed by: DECIDED-2026-10-15 — C-7Q.5.5 — Stronger minor and vulnerable-person defaults: no automatic restriction for minors or highly vulnerable people; the universal baseline and Ness's explicit person or group rules apply to them as to anyone. [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.2]
```

**F-CH08-a-01767** · CH08-a:1767 · USED BY · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| 8 · DESIGNED | C-7Q.5.5 — Stronger minor and vulnerable-person defaults | The universal third-party baseline and governing V10 boundaries. | Preserves another person’s protection while applying the specific use rule. | Relationship context or material availability never removes the baseline. | [V10 §7Q] |
```

With:

```text
| 8 · DECIDED-2026-10-15 | C-7Q.5.5 — Stronger minor and vulnerable-person defaults | The universal third-party baseline. | Preserves another person's protection for minors and highly vulnerable people without an automatic category restriction. | Relationship context or material availability never removes the baseline. | [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.2] [V10 §7Q] |
```

#### C-7Q.5.1 — Context-sensitive third-party handling

**F-CH08-a-01778** · CH08-a:1778 · Takes in · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:486, "Within the §7Q context-sensitive variance list, "age or vulnerability"".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
- Takes in: DESIGNED — Relationship to Ness; data amount and frequency; sensitivity; source/front door; direct speech versus another person’s description; private/public/forwarded/recorded/inferred origin; age/vulnerability; intended use. [V10 §7Q]
```

With:

```text
- Takes in: DESIGNED — Relationship to Ness; data amount and frequency; sensitivity; source/front door; direct speech versus another person’s description; private/public/forwarded/recorded/inferred origin; intended use. [V10 §7Q]
- Takes in: DECIDED-2026-10-15 — Age or vulnerability is not an automatic driver: those facts alone change nothing, and Ness's explicit person- or group-specific configuration is the only path to different handling. [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.2]
```

#### C-7Q.5.3 — Four-operation third-party authorization ladder

**F-CH08-a-01826** · CH08-a:1826 · Does · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules.

Replaces:

```text
- Does: DESIGNED — Normally permits the first activity; each later activity needs stronger authorization. [SOURCE CONFLICT: NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §§4.5/4.6/6.1 and NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md §3 allow ordinary bounded interpretation without separate permission.] [V10 §7Q]
```

With:

```text
- Does: DESIGNED — Normally permits the first activity. [V10 §7Q]
- Does: DECIDED-2026-10-15 — Ordinary bounded interpretation (the third activity) needs no separate permission; constructing a model of the person (the fourth) is the full simulation that needs Ness's clear prior approval. [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.1] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §4.6]
- Does: DECIDED-2026-10-29 — The second activity needs only the existing capture and third-party rules; no stronger authorization is added. [D-2026-10-29-04] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.1]
```

**F-CH08-a-01827** · CH08-a:1827 · Gives out · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules.

Replaces:

```text
- Gives out: DESIGNED — An operation-specific authorization requirement. [V10 §7Q]
```

With:

```text
- Gives out: DECIDED-2026-10-15 — The operation's own requirement: none beyond the baseline for the first and third activities, and Ness's clear prior approval for the fourth. [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.1]
- Gives out: DECIDED-2026-10-29 — For the second activity, the existing capture and third-party rules; no stronger authorization is added. [D-2026-10-29-04] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.1]
```

**F-CH08-a-01829** · CH08-a:1829 · Fails closed by · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules.

Replaces:

```text
- Fails closed by: DESIGNED — Withholds a later activity lacking its required stronger authorization. [V10 §7Q]
```

With:

```text
- Fails closed by: DECIDED-2026-10-15 — Withholds a full simulation (the fourth activity) that lacks Ness's clear prior approval; ordinary bounded interpretation is never withheld for lack of permission. [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.1] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §4.6]
```

**F-CH08-a-01839** · CH08-a:1839 · USED BY · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules.

Replaces:

```text
| 1 · DESIGNED | C-7Q.5 — Third-party data baseline | The actual third-party operation. | Requires the appropriate authorization. | Different depths of use remain distinct. | [V10 §7Q] |
```

With:

```text
| 1 · DECIDED-2026-10-29 | C-7Q.5 — Third-party data baseline | The actual third-party operation. | Applies each operation's own rule: the first is normally permitted, ordinary bounded interpretation needs no separate permission, and a constructed model needs Ness's clear prior approval; the second needs only the existing capture and third-party rules. | Different depths of use remain distinct. | [D-2026-10-15-02 T4] [D-2026-10-29-04] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.1] [V10 §7Q] |
```

**F-CH08-a-01840** · CH08-a:1840 · USED BY · `ready`

- Rule: D-2026-10-29-04, "4. כן, הכללים מתאימים." (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:477, "Operation 2 remains governed by the existing".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. C-7Q.5.3.2's Fed by and Changes stay NOT DECIDED (wiring).

Replaces:

```text
| 2 · DESIGNED | C-7Q.5.3.2 — Recording another person’s words or actions | The four-operation third-party authorization ladder. | Keeps later operations under V10’s stronger authorization rule with the losing accepted wording marked. | A lower operation never silently authorizes a later one. | [V10 §7Q] |
```

With:

```text
| 2 · DECIDED-2026-10-29 | C-7Q.5.3.2 — Recording another person’s words or actions | The four-operation third-party authorization ladder. | Keeps the second activity under the existing capture and third-party rules; no stronger authorization is added. | A lower operation never silently authorizes a later one. | [D-2026-10-29-04] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.1] [V10 §7Q] |
```

**F-CH08-a-01841** · CH08-a:1841 · USED BY · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules.

Replaces:

```text
| 3 · DESIGNED | C-7Q.5.3.3 — Interpreting another person’s possible meaning | The four-operation third-party authorization ladder. | Keeps later operations under V10’s stronger authorization rule with the losing accepted wording marked. | A lower operation never silently authorizes a later one. | [V10 §7Q] |
```

With:

```text
| 3 · DECIDED-2026-10-15 | C-7Q.5.3.3 — Interpreting another person’s possible meaning | The four-operation third-party authorization ladder. | Lets ordinary bounded interpretation proceed without separate permission; its labels, uncertainty and non-hardening rules stay. | A lower operation never silently authorizes a later one. | [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.1] [V10 §7Q] |
```

**F-CH08-a-01843** · CH08-a:1843 · USED BY · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules.

Replaces:

```text
| 5 · DESIGNED | C-OTHER.7.1 — Interpret a parent's statement for Ness | The parent's statement and Ness's request to understand it. | Gates this place: V10's stronger-authorization requirement applies to interpretation. | Nothing in this card. | [V10 §25.2 / Parent Translation] [V10 §7Q] [SOURCE CONFLICT: A7 §§4.5/6.1 and B7 §3 allow ordinary bounded interpretation without separate permission.] |
```

With:

```text
| 5 · DECIDED-2026-10-15 | C-OTHER.7.1 — Interpret a parent's statement for Ness | The parent's statement and Ness's request to understand it. | Gates this place: interpreting the parent's statement is ordinary bounded interpretation and needs no separate permission. | Nothing in this card. | [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.1] [V10 §25.2 / Parent Translation] |
```

#### C-7Q.5.3.2 — Recording another person’s words or actions

**F-CH08-a-01876** · CH08-a:1876 · Does · `ready`

- Rule: D-2026-10-29-04, "4. כן, הכללים מתאימים." (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:477, "Operation 2 remains governed by the existing".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. C-7Q.5.3.2's Fed by and Changes stay NOT DECIDED (wiring).

Replaces:

```text
- Does: DESIGNED — Records it with source and speaker under stronger authorization than self-understanding. [V10 §7Q]
```

With:

```text
- Does: DESIGNED — Records it with source and speaker. [V10 §7Q]
- Does: DECIDED-2026-10-29 — The recording needs only the existing capture and third-party rules; no stronger authorization is added. [D-2026-10-29-04] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.1]
```

**F-CH08-a-01879** · CH08-a:1879 · Fails closed by · `ready`

- Rule: D-2026-10-29-04, "4. כן, הכללים מתאימים." (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:477, "Operation 2 remains governed by the existing".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. C-7Q.5.3.2's Fed by and Changes stay NOT DECIDED (wiring).

Replaces:

```text
- Fails closed by: DESIGNED — Withholds unauthorized recording. [V10 §7Q]
```

With:

```text
- Fails closed by: DECIDED-2026-10-29 — Withholds a recording that the existing capture and third-party rules do not permit. [D-2026-10-29-04] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.1] [V10 §7Q]
```

**F-CH08-a-01883** · CH08-a:1883 · Gated by · `ready`

- Rule: D-2026-10-29-04, "4. כן, הכללים מתאימים." (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:477, "Operation 2 remains governed by the existing".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. C-7Q.5.3.2's Fed by and Changes stay NOT DECIDED (wiring).

Replaces:

```text
- Gated by: DESIGNED — C-7Q.5.3 — Four-operation third-party authorization ladder: this later activity requires stronger authorization. [V10 §7Q]
```

With:

```text
- Gated by: DECIDED-2026-10-29 — C-7Q.5.3 — Four-operation third-party authorization ladder: this activity needs only the existing capture and third-party rules; no stronger authorization is added. [D-2026-10-29-04] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.1] [V10 §7Q]
```

**F-CH08-a-01889** · CH08-a:1889 · USED BY · `ready`

- Rule: D-2026-10-29-04, "4. כן, הכללים מתאימים." (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:477, "Operation 2 remains governed by the existing".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. C-7Q.5.3.2's Fed by and Changes stay NOT DECIDED (wiring).

Replaces:

```text
| 1 · DESIGNED | C-7Q.5.3 — Four-operation third-party authorization ladder | Actual third-party words or actions. | Applies the second activity’s authorization. | Recording remains distinct from understanding Ness’s experience. | [V10 §7Q] |
```

With:

```text
| 1 · DECIDED-2026-10-29 | C-7Q.5.3 — Four-operation third-party authorization ladder | Actual third-party words or actions. | Applies the existing capture and third-party rules; no stronger authorization is added. | Recording remains distinct from understanding Ness’s experience. | [D-2026-10-29-04] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.1] [V10 §7Q] |
```

#### C-7Q.5.3.3 — Interpreting another person’s possible meaning

**F-CH08-a-01899** · CH08-a:1899 · Does · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules.

Replaces:

```text
- Does: DESIGNED — Requires the stronger authorization in V10. [SOURCE CONFLICT: NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §§4.5/6.1 and NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md §3 say ordinary bounded interpretation needs no separate permission.] Keeps permitted interpretations as possibilities, with alternatives and missing information visible. [V10 §7Q] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §4.5]
```

With:

```text
- Does: DECIDED-2026-10-15 — Needs no separate permission: N.H interprets naturally. [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.1]
- Does: DESIGNED — Keeps permitted interpretations as possibilities, with alternatives and missing information visible. [V10 §7Q] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §4.5]
```

**F-CH08-a-01902** · CH08-a:1902 · Fails closed by · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules.

Replaces:

```text
- Fails closed by: DESIGNED — Withholds the activity when its governing authorization is absent. [V10 §7Q] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §4.5]
```

With:

```text
- Fails closed by: DECIDED-2026-10-15 — Withholds nothing for lack of permission; an interpretation that cannot stay a labeled possibility is not given as one. [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.1] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §4.5]
```

**F-CH08-a-01906** · CH08-a:1906 · Gated by · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules.

Replaces:

```text
- Gated by: DESIGNED — C-7Q.5.3 — Four-operation third-party authorization ladder: the third activity retains V10’s stronger authorization; C-7Q.5 — Third-party data baseline: inferred private states remain nonfactual. [V10 §7Q] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §4.5]
```

With:

```text
- Gated by: DECIDED-2026-10-15 — C-7Q.5.3 — Four-operation third-party authorization ladder: the third activity needs no separate permission. [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.1]
- Gated by: DESIGNED — C-7Q.5 — Third-party data baseline: inferred private states remain nonfactual. [V10 §7Q] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §4.5]
```

**F-CH08-a-01912** · CH08-a:1912 · USED BY · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules.

Replaces:

```text
| 1 · DESIGNED | C-7Q.5.3 — Four-operation third-party authorization ladder | A proposed interpretation. | Keeps its authorization and uncertainty explicit. | Interpretation cannot become unqualified person knowledge. | [V10 §7Q] |
```

With:

```text
| 1 · DECIDED-2026-10-15 | C-7Q.5.3 — Four-operation third-party authorization ladder | A proposed interpretation. | Keeps its uncertainty explicit; no separate permission is needed. | Interpretation cannot become unqualified person knowledge. | [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.1] [V10 §7Q] |
```

#### C-7Q.5.4 — Third-party simulation boundary

**F-CH08-a-01945** · CH08-a:1945 · Does · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:321, "intended, or believed, including a brief "they might respond X or Y"".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules.

Replaces:

```text
- Does: DESIGNED — Labels the model as hypothetical, limited, uncertain and not the person. Full/detailed simulation includes extended roleplay, dialogue in the person’s voice or manner, detailed multi-branch predictions and an interactive hypothetical model of thinking; these need clear prior approval. A brief own-voice possibility such as X or Y is distinct from full simulation; its interpretation permission still follows the marked V10 ladder. [V10 §7Q] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §4.6]
```

With:

```text
- Does: DESIGNED — Labels the model as hypothetical, limited, uncertain and not the person. Full/detailed simulation includes extended roleplay, dialogue in the person’s voice or manner, detailed multi-branch predictions and an interactive hypothetical model of thinking; these need clear prior approval. [V10 §7Q] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §4.6]
- Does: DECIDED-2026-10-15 — A brief own-voice possibility such as X or Y is distinct from full simulation and needs no permission. [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §4.6] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.1]
```

#### C-7Q.5.5 — Stronger minor and vulnerable-person defaults

**F-CH08-a-01969** · CH08-a:1969 · What it is · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
- What it is: DESIGNED — V10’s stronger default restriction for minors and highly vulnerable people. [V10 §7Q]
```

With:

```text
- What it is: DECIDED-2026-10-15 — The removed rule: there is no automatic stronger restriction for minors or highly vulnerable people. [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.2]
```

**F-CH08-a-01971** · CH08-a:1971 · Does · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
- Does: DESIGNED — Applies the stronger default. [SOURCE CONFLICT: NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §§4.7/6.2, NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md §3, NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4/A30, NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11 and NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md §§5/8 remove automatic age/vulnerability restrictions; Bundle 5 calls V10’s sentence frozen predecision wording.] [V10 §7Q]
```

With:

```text
- Does: DECIDED-2026-10-15 — Adds no automatic restriction, block, weakened analysis or simulation ban based only on age, minority, disability, distress, dependence or a vulnerability label; the universal baseline and Ness's explicit person or group rules apply. [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.2] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §4.7]
```

**F-CH08-a-01972** · CH08-a:1972 · Gives out · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
- Gives out: DESIGNED — The governing stronger default with the opposing accepted policy kept visible. [V10 §7Q]
```

With:

```text
- Gives out: DECIDED-2026-10-15 — Third-party material involving those people handled under the same baseline as anyone's. [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.2]
```

**F-CH08-a-01984** · CH08-a:1984 · USED BY · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| 1 · DESIGNED | C-7Q.5 — Third-party data baseline | Minor or highly vulnerable third-party material. | Preserves the governing default restriction. | The conflicting accepted removal is not silently substituted. | [V10 §7Q] |
```

With:

```text
| 1 · DECIDED-2026-10-15 | C-7Q.5 — Third-party data baseline | Minor or highly vulnerable third-party material. | Applies the same baseline as for anyone, with no automatic category restriction. | Only Ness's explicit person or group rules change the handling. | [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.2] [V10 §7Q] |
```

### CH08-b

#### Chapter header

**F-CH08-b-00012** · CH08-b:12 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; NHD identifiers locate decisions in the pinned index and do not replace behavior citations.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; NHD identifiers locate decisions in the pinned index and do not replace behavior citations. Decision key `D-2026-10-15-02 T4`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH08-b-06626** · CH08-b:6626 · table row · `ready`

Place: Carried source-placement row, identical to CH08-a:12164; same change as F-CH08-a-12164.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH08-b-06638** · CH08-b:6638 · table row · `ready`

Place: Carried source-placement row, identical to CH08-a:12176; same change as F-CH08-a-12176.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

### CH08-c

#### Chapter header

**F-CH08-c-00010** · CH08-c:10 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; NHD identifiers locate decisions in the pinned index and do not replace behavior citations.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; NHD identifiers locate decisions in the pinned index and do not replace behavior citations. Decision key `D-2026-10-15-02 T4`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH08-c-02907** · CH08-c:2907 · table row · `ready`

Place: Carried source-placement row, identical to CH08-a:12164; same change as F-CH08-a-12164.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH08-c-02919** · CH08-c:2919 · table row · `ready`

Place: Carried source-placement row, identical to CH08-a:12176; same change as F-CH08-a-12176.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

### CH08-d

#### Chapter header

**F-CH08-d-00012** · CH08-d:12 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; NHD identifiers locate decisions in the pinned index and do not replace behavior citations.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; NHD identifiers locate decisions in the pinned index and do not replace behavior citations. Decision key `D-2026-10-15-02 T4`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH08-d-05622** · CH08-d:5622 · table row · `ready`

Place: Carried source-placement row, identical to CH08-a:12164; same change as F-CH08-a-12164.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH08-d-05634** · CH08-d:5634 · table row · `ready`

Place: Carried source-placement row, identical to CH08-a:12176; same change as F-CH08-a-12176.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

### CH08-e

#### Chapter header

**F-CH08-e-00010** · CH08-e:10 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; NHD identifiers locate decisions in the pinned index and do not replace behavior citations.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; NHD identifiers locate decisions in the pinned index and do not replace behavior citations. Decision key `D-2026-10-15-02 T4`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH08-e-01935** · CH08-e:1935 · table row · `ready`

Place: Carried source-placement row, identical to CH08-a:12164; same change as F-CH08-a-12164.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH08-e-01947** · CH08-e:1947 · table row · `ready`

Place: Carried source-placement row, identical to CH08-a:12176; same change as F-CH08-a-12176.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

### CH08-f

#### Chapter header

**F-CH08-f-00010** · CH08-f:10 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; NHD identifiers locate decisions in the pinned index and do not replace behavior citations.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; NHD identifiers locate decisions in the pinned index and do not replace behavior citations. Decision key `D-2026-10-15-02 T4`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH08-f-01375** · CH08-f:1375 · table row · `ready`

Place: Carried source-placement row, identical to CH08-a:12164; same change as F-CH08-a-12164.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH08-f-01387** · CH08-f:1387 · table row · `ready`

Place: Carried source-placement row, identical to CH08-a:12176; same change as F-CH08-a-12176.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

### CH08-g

#### Chapter header

**F-CH08-g-00010** · CH08-g:10 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; NHD identifiers locate decisions in the pinned index and do not replace behavior citations.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; NHD identifiers locate decisions in the pinned index and do not replace behavior citations. Decision key `D-2026-10-15-02 T4`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH08-g-02455** · CH08-g:2455 · table row · `ready`

Place: Carried source-placement row, identical to CH08-a:12164; same change as F-CH08-a-12164.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH08-g-02467** · CH08-g:2467 · table row · `ready`

Place: Carried source-placement row, identical to CH08-a:12176; same change as F-CH08-a-12176.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

### CH09-a

#### Chapter header

**F-CH09-a-00012** · CH09-a:12 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; CR = `01_AUTHORITATIVE/cursorrules`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; CR = `01_AUTHORITATIVE/cursorrules`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`. Decision key `D-2026-10-15-02 T4`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH09-a-01136** · CH09-a:1136 · table row · `ready`

Place: Carried source-placement row, identical to CH08-a:12164; same change as F-CH08-a-12164.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH09-a-01148** · CH09-a:1148 · table row · `ready`

Place: Carried source-placement row, identical to CH08-a:12176; same change as F-CH08-a-12176.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

### CH09-b

#### C-OTHER — Other-Speaker / Guest / Known-Person Architecture (§25.2)

**F-CH09-b-00014** · CH09-b:14 · other · `ready`

Place: Chapter header SOURCE CONFLICT paragraph of CH09-b, before its first card (the C-OTHER tree).

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
[SOURCE CONFLICT: V10 §7Q requires increasingly stronger authorization for later third-party operations and stronger default restrictions for minors/highly vulnerable people. A7 §§4.5–4.7/6 and B7 §3 permit ordinary bounded interpretation without separate permission and remove automatic category restrictions; Bundle 5 §8 calls the V10 wording frozen pre-decision text. V10 governs this candidate under the build contract. Existing CH08-a conflicts remain open.]
```

With:

```text
[SOURCE CONFLICT: V10 §7Q requires increasingly stronger authorization for later third-party operations and stronger default restrictions for minors/highly vulnerable people. A7 §§4.5–4.7/6 and B7 §3 permit ordinary bounded interpretation without separate permission and remove automatic category restrictions; Bundle 5 §8 calls the V10 wording frozen pre-decision text. By D-2026-10-15-02 T4, A7 governs both: ordinary bounded interpretation needs no separate permission, and no automatic minor/vulnerable restriction exists. Operation 2 needs only the existing capture and third-party rules, by Ness's answer of 2026-10-29 (D-2026-10-29-04), as in CH08-a.]
```

#### Chapter header

**F-CH09-b-00018** · CH09-b:18 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`. Decision keys `D-2026-10-15-02 T4` and `D-2026-10-29-04`, added after the pinned commit, name Ness's decisions quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-OTHER.7.1 — Interpret a parent's statement for Ness

**F-CH09-b-00317** · CH09-b:317 · Fails closed by · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules.

Replaces:

```text
- Fails closed by: DESIGNED — Waits for the translation request and applicable third-party authorization. [V10 §25.2 / Parent Translation] [V10 §7Q]
```

With:

```text
- Fails closed by: DESIGNED — Waits for the translation request. [V10 §25.2 / Parent Translation]
- Fails closed by: DECIDED-2026-10-15 — Needs no separate third-party permission: interpreting the parent's statement is ordinary bounded interpretation. [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.1]
```

**F-CH09-b-00321** · CH09-b:321 · Gated by · `ready`

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules.

Replaces:

```text
- Gated by: DESIGNED — C-OTHER.7 — Request-driven parent translation: Ness must request this branch; C-7Q.5.3 — Four-operation third-party authorization ladder: V10's stronger-authorization requirement applies to interpretation. [V10 §25.2 / Parent Translation] [V10 §7Q] [SOURCE CONFLICT: A7 §§4.5/6.1 and B7 §3 allow ordinary bounded interpretation without separate permission.]
```

With:

```text
- Gated by: DESIGNED — C-OTHER.7 — Request-driven parent translation: Ness must request this branch. [V10 §25.2 / Parent Translation]
- Gated by: DECIDED-2026-10-15 — C-7Q.5.3 — Four-operation third-party authorization ladder: the interpretation is ordinary bounded interpretation and needs no separate permission. [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.1] [V10 §7Q]
```

**F-CH09-b-00835** · CH09-b:835 · table row · `ready`

Place: Cross-piece TOGETHER continuation row in CH09-b's back matter copying C-OTHER.7.1's Gated by line (CH09-b:321); split into two rows like that line.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules.

Replaces:

```text
| C-7Q.5.3 — Four-operation third-party authorization ladder | C-OTHER.7.1 — Interpret a parent's statement for Ness | Gated by | DESIGNED — C-OTHER.7 — Request-driven parent translation: Ness must request this branch; C-7Q.5.3 — Four-operation third-party authorization ladder: V10's stronger-authorization requirement applies to interpretation. [V10 §25.2 / Parent Translation] [V10 §7Q] [SOURCE CONFLICT: A7 §§4.5/6.1 and B7 §3 allow ordinary bounded interpretation without separate permission.] | Pending endpoint placement |
```

With:

```text
| C-7Q.5.3 — Four-operation third-party authorization ladder | C-OTHER.7.1 — Interpret a parent's statement for Ness | Gated by | DESIGNED — C-OTHER.7 — Request-driven parent translation: Ness must request this branch. [V10 §25.2 / Parent Translation] | Pending endpoint placement |
| C-7Q.5.3 — Four-operation third-party authorization ladder | C-OTHER.7.1 — Interpret a parent's statement for Ness | Gated by | DECIDED-2026-10-15 — C-7Q.5.3 — Four-operation third-party authorization ladder: the interpretation needs no separate permission. [D-2026-10-15-02 T4] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §6.1] [V10 §7Q] | Pending endpoint placement |
```

#### C-7Q.5 — Third-party data baseline

**F-CH09-b-00923** · CH09-b:923 · table row · `ready`

Place: Source-placement row in CH09-b's back matter about C-7Q.5.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. Stronger-authorization and minor/vulnerable-default conflicts retained consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

With:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. The stronger-authorization (operation 3) and minor/vulnerable-default conflicts are decided for A7 by D-2026-10-15-02 T4, consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

**F-CH09-b-01751** · CH09-b:1751 · table row · `ready`

Place: Carried source-placement row, identical to CH09-b:923; same change as F-CH09-b-00923.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. Stronger-authorization and minor/vulnerable-default conflicts retained consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

With:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. The stronger-authorization (operation 3) and minor/vulnerable-default conflicts are decided for A7 by D-2026-10-15-02 T4, consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH09-b-01593** · CH09-b:1593 · table row · `ready`

Place: Carried source-placement row, identical to CH08-a:12164; same change as F-CH08-a-12164.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH09-b-01605** · CH09-b:1605 · table row · `ready`

Place: Carried source-placement row, identical to CH08-a:12176; same change as F-CH08-a-12176.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

### CH09-c

#### Chapter header

**F-CH09-c-00014** · CH09-c:14 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`. Decision key `D-2026-10-15-02 T4`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH09-c-03215** · CH09-c:3215 · table row · `ready`

Place: Carried source-placement row, identical to CH08-a:12164; same change as F-CH08-a-12164.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH09-c-03227** · CH09-c:3227 · table row · `ready`

Place: Carried source-placement row, identical to CH08-a:12176; same change as F-CH08-a-12176.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-7Q.5 — Third-party data baseline

**F-CH09-c-03373** · CH09-c:3373 · table row · `ready`

Place: Carried source-placement row, identical to CH09-b:923; same change as F-CH09-b-00923.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. Stronger-authorization and minor/vulnerable-default conflicts retained consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

With:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. The stronger-authorization (operation 3) and minor/vulnerable-default conflicts are decided for A7 by D-2026-10-15-02 T4, consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

### CH09-d

#### Chapter header

**F-CH09-d-00018** · CH09-d:18 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`. Decision key `D-2026-10-15-02 T4`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH09-d-07096** · CH09-d:7096 · table row · `ready`

Place: Carried source-placement row, identical to CH08-a:12164; same change as F-CH08-a-12164.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH09-d-07108** · CH09-d:7108 · table row · `ready`

Place: Carried source-placement row, identical to CH08-a:12176; same change as F-CH08-a-12176.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-7Q.5 — Third-party data baseline

**F-CH09-d-07254** · CH09-d:7254 · table row · `ready`

Place: Carried source-placement row, identical to CH09-b:923; same change as F-CH09-b-00923.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. Stronger-authorization and minor/vulnerable-default conflicts retained consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

With:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. The stronger-authorization (operation 3) and minor/vulnerable-default conflicts are decided for A7 by D-2026-10-15-02 T4, consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

### CH09-e

#### Chapter header

**F-CH09-e-00012** · CH09-e:12 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`, restricted to expressly restored text.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`, restricted to expressly restored text. Decision key `D-2026-10-15-02 T4`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH09-e-04115** · CH09-e:4115 · table row · `ready`

Place: Carried row, identical to CH08-a:12164; same change as F-CH08-a-12164.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH09-e-04127** · CH09-e:4127 · table row · `ready`

Place: Carried row, identical to CH08-a:12176; same change as F-CH08-a-12176.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-7Q.5 — Third-party data baseline

**F-CH09-e-04273** · CH09-e:4273 · table row · `ready`

Place: Carried row, identical to CH09-b:923; same change as F-CH09-b-00923.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. Stronger-authorization and minor/vulnerable-default conflicts retained consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

With:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. The stronger-authorization (operation 3) and minor/vulnerable-default conflicts are decided for A7 by D-2026-10-15-02 T4, consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

### CH09-f

#### Chapter header

**F-CH09-f-00014** · CH09-f:14 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`. Decision key `D-2026-10-15-02 T4`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH09-f-04479** · CH09-f:4479 · table row · `ready`

Place: Carried row, identical to CH08-a:12164; same change as F-CH08-a-12164.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH09-f-04491** · CH09-f:4491 · table row · `ready`

Place: Carried row, identical to CH08-a:12176; same change as F-CH08-a-12176.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-7Q.5 — Third-party data baseline

**F-CH09-f-04637** · CH09-f:4637 · table row · `ready`

Place: Carried row, identical to CH09-b:923; same change as F-CH09-b-00923.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. Stronger-authorization and minor/vulnerable-default conflicts retained consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

With:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. The stronger-authorization (operation 3) and minor/vulnerable-default conflicts are decided for A7 by D-2026-10-15-02 T4, consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

### CH09-g

#### Chapter header

**F-CH09-g-00012** · CH09-g:12 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`. Decision key `D-2026-10-15-02 T4`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH09-g-02981** · CH09-g:2981 · table row · `ready`

Place: Carried row, identical to CH08-a:12164; same change as F-CH08-a-12164.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH09-g-02993** · CH09-g:2993 · table row · `ready`

Place: Carried row, identical to CH08-a:12176; same change as F-CH08-a-12176.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-7Q.5 — Third-party data baseline

**F-CH09-g-03139** · CH09-g:3139 · table row · `ready`

Place: Carried row, identical to CH09-b:923; same change as F-CH09-b-00923.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. Stronger-authorization and minor/vulnerable-default conflicts retained consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

With:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. The stronger-authorization (operation 3) and minor/vulnerable-default conflicts are decided for A7 by D-2026-10-15-02 T4, consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

### CH09-h

#### Chapter header

**F-CH09-h-00012** · CH09-h:12 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`. Decision key `D-2026-10-15-02 T4`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH09-h-05897** · CH09-h:5897 · table row · `ready`

Place: Carried row, identical to CH08-a:12164; same change as F-CH08-a-12164.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH09-h-05909** · CH09-h:5909 · table row · `ready`

Place: Carried row, identical to CH08-a:12176; same change as F-CH08-a-12176.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-7Q.5 — Third-party data baseline

**F-CH09-h-06055** · CH09-h:6055 · table row · `ready`

Place: Carried row, identical to CH09-b:923; same change as F-CH09-b-00923.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. Stronger-authorization and minor/vulnerable-default conflicts retained consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

With:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. The stronger-authorization (operation 3) and minor/vulnerable-default conflicts are decided for A7 by D-2026-10-15-02 T4, consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

### CH09-i

#### Chapter header

**F-CH09-i-00014** · CH09-i:14 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Decision key `D-2026-10-15-02 T4`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH09-i-10070** · CH09-i:10070 · table row · `ready`

Place: Carried row, identical to CH08-a:12164; same change as F-CH08-a-12164.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH09-i-10082** · CH09-i:10082 · table row · `ready`

Place: Carried row, identical to CH08-a:12176; same change as F-CH08-a-12176.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-7Q.5 — Third-party data baseline

**F-CH09-i-10228** · CH09-i:10228 · table row · `ready`

Place: Carried row, identical to CH09-b:923; same change as F-CH09-b-00923.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. Stronger-authorization and minor/vulnerable-default conflicts retained consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

With:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. The stronger-authorization (operation 3) and minor/vulnerable-default conflicts are decided for A7 by D-2026-10-15-02 T4, consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

### CH10-a

#### Chapter header

**F-CH10-a-00016** · CH10-a:16 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Decision key `D-2026-10-15-02 T4`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH10-a-02942** · CH10-a:2942 · table row · `ready`

Place: Carried row, identical to CH08-a:12164; same change as F-CH08-a-12164.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH10-a-02954** · CH10-a:2954 · table row · `ready`

Place: Carried row, identical to CH08-a:12176; same change as F-CH08-a-12176.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-7Q.5 — Third-party data baseline

**F-CH10-a-03100** · CH10-a:3100 · table row · `ready`

Place: Carried row, identical to CH09-b:923; same change as F-CH09-b-00923.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. Stronger-authorization and minor/vulnerable-default conflicts retained consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

With:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. The stronger-authorization (operation 3) and minor/vulnerable-default conflicts are decided for A7 by D-2026-10-15-02 T4, consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

### CH10-b

#### Chapter header

**F-CH10-b-00020** · CH10-b:20 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`. Decision key `D-2026-10-15-02 T4`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH10-b-23791** · CH10-b:23791 · table row · `ready`

Place: Carried row, identical to CH08-a:12164; same change as F-CH08-a-12164.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH10-b-23803** · CH10-b:23803 · table row · `ready`

Place: Carried row, identical to CH08-a:12176; same change as F-CH08-a-12176.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-7Q.5 — Third-party data baseline

**F-CH10-b-23949** · CH10-b:23949 · table row · `ready`

Place: Carried row, identical to CH09-b:923; same change as F-CH09-b-00923.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. Stronger-authorization and minor/vulnerable-default conflicts retained consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

With:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. The stronger-authorization (operation 3) and minor/vulnerable-default conflicts are decided for A7 by D-2026-10-15-02 T4, consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

### CH10-c

#### C-22 — Wellbeing & Behavioral Baseline (§22)

**F-CH10-c-00010** · CH10-c:10 · other · `ready`

Place: Chapter preamble line above the first card; it names C-22, the chapter's card group.

- Rule: D-2026-10-15-03, "Ness's words, verbatim: "Q2 - a"" (OCT15:483).
- Also rests on: D-2026-10-29-03, Ness's wide reading: "רחבה 3." (NESS_ANSWERS_2026-10-29_v0_1.md:11).
- Source: `REPO/01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`:185, "(4) system remains advisory — cannot diagnose, prescribe, or act autonomously;".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged and still open: the tier selection and transition logic and the thresholds (C-22.6.5, NOT DECIDED); the unlock is the appointment record (DD:184). "cannot diagnose, prescribe" goes too: Ness chose the wide reading on 2026-10-29 (D-2026-10-29-03). Nothing here designs a diagnosing or prescribing function. The creation gate stays: Ness's "CONFIRMED: create nh_baseline_engine.py", the dry-run protocol and the prerequisites other than (4), the advisory condition, which goes (DD:185). The wording of DD §3K and cursorrules §12D changes later by new versioned files, never in place (OCT15:492). How the baseline reads REALITY promotions once T6's steer-not-file model applies (V10:3184) is a design slot (OCT15:497-498). C-22.9.4 keeps its ID; its name becomes "Removed advisory boundary" (A-2026-10-29-3).

Replaces:

```text
[SOURCE CONFLICT] V10 §22 specifies tier-triggered REALITY promotion throttling and freezing. DD §3K and CR §12D require the system to remain advisory and not act autonomously. Both statements are preserved; this piece does not invent a reconciliation or an autonomous-action exception. [V10 §22] [DD §3K] [CR §12D]
```

With:

```text
[DECIDED-2026-10-29] V10 §22's tier-triggered REALITY promotion throttling (Tier 3) and freezing (Tier 4) stand and run automatically. DD §3K's and CR §12D's advisory requirement (the system cannot diagnose, prescribe or act autonomously) no longer applies to the baseline engine. Nothing here designs a diagnosing or prescribing function. [D-2026-10-15-03] [D-2026-10-29-03] [V10 §22] [DD §3K] [CR §12D]
```

#### Chapter header

**F-CH10-c-00014** · CH10-c:14 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Decision keys `D-2026-10-15-02 T4`, `D-2026-10-15-03` and `D-2026-10-29-03`, added after the pinned commit, name Ness's decisions quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-22.9 — Deferred protected baseline engine

**F-CH10-c-00749** · CH10-c:749 · Must never · `ready`

- Rule: D-2026-10-15-03, "Ness's words, verbatim: "Q2 - a"" (OCT15:483).
- Also rests on: D-2026-10-29-03, Ness's wide reading: "רחבה 3." (NESS_ANSWERS_2026-10-29_v0_1.md:11).
- Source: `REPO/01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`:185, "(4) system remains advisory — cannot diagnose, prescribe, or act autonomously;".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged and still open: the tier selection and transition logic and the thresholds (C-22.6.5, NOT DECIDED); the unlock is the appointment record (DD:184). "cannot diagnose, prescribe" goes too: Ness chose the wide reading on 2026-10-29 (D-2026-10-29-03). Nothing here designs a diagnosing or prescribing function. The creation gate stays: Ness's "CONFIRMED: create nh_baseline_engine.py", the dry-run protocol and the prerequisites other than (4), the advisory condition, which goes (DD:185). The wording of DD §3K and cursorrules §12D changes later by new versioned files, never in place (OCT15:492). How the baseline reads REALITY promotions once T6's steer-not-file model applies (V10:3184) is a design slot (OCT15:497-498). C-22.9.4 keeps its ID; its name becomes "Removed advisory boundary" (A-2026-10-29-3).

Replaces:

```text
- Must never: DESIGNED — Diagnose, prescribe, act autonomously or silently write wellbeing output into roots, production readings or the legacy REALITY store. [DD §3K] [CR §12D]
```

With:

```text
- Must never: DESIGNED — Silently write wellbeing output into roots, production readings or the legacy REALITY store. [DD §3K] [CR §12D]
- Must never: DECIDED-2026-10-29 — The advisory prohibitions (diagnose, prescribe, act autonomously) no longer apply to this engine; the Tier 3 slowing and Tier 4 pausing of REALITY promotion run automatically. [D-2026-10-15-03] [D-2026-10-29-03] [V10 §22]
```

**F-CH10-c-00763** · CH10-c:763 · USED BY · `ready`

- Rule: D-2026-10-15-03, "Ness's words, verbatim: "Q2 - a"" (OCT15:483).
- Also rests on: D-2026-10-29-03, Ness's wide reading: "רחבה 3." (NESS_ANSWERS_2026-10-29_v0_1.md:11).
- Source: `REPO/01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`:185, "(4) system remains advisory — cannot diagnose, prescribe, or act autonomously;".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18); card name: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: Unchanged and still open: the tier selection and transition logic and the thresholds (C-22.6.5, NOT DECIDED); the unlock is the appointment record (DD:184). "cannot diagnose, prescribe" goes too: Ness chose the wide reading on 2026-10-29 (D-2026-10-29-03). Nothing here designs a diagnosing or prescribing function. The creation gate stays: Ness's "CONFIRMED: create nh_baseline_engine.py", the dry-run protocol and the prerequisites other than (4), the advisory condition, which goes (DD:185). The wording of DD §3K and cursorrules §12D changes later by new versioned files, never in place (OCT15:492). How the baseline reads REALITY promotions once T6's steer-not-file model applies (V10:3184) is a design slot (OCT15:497-498). C-22.9.4 keeps its ID; its name becomes "Removed advisory boundary" (A-2026-10-29-3).

Replaces:

```text
| 4 · DESIGNED | C-22.9.4 — Advisory and non-diagnostic boundary | The baseline engine's proposed behavior. [DD §3K] | Keeps diagnosis, prescription and autonomous action outside the stated advisory scope. [DD §3K] | An advisory limitation alongside V10's preserved tier effects. [DD §3K] | [DD §3K] |
```

With:

```text
| 4 · DECIDED-2026-10-29 | C-22.9.4 — Removed advisory boundary | The baseline engine's proposed behavior. [DD §3K] | Sets no advisory limit: the prohibitions on diagnosing, prescribing and autonomous action are removed, and the Tier 3 slowing and Tier 4 pausing of REALITY promotion run automatically. [D-2026-10-15-03] [D-2026-10-29-03] [DD §3K] | No advisory limitation; V10's tier effects run. [D-2026-10-29-03] | [D-2026-10-15-03] [D-2026-10-29-03] [DD §3K] |
```

**F-CH10-c-01201** · CH10-c:1201 · table row · `ready`

Place: Source-to-card coverage row placing V10 §22's limitation and DD §3K/CR §12D on C-22.8 and C-22.9; changed with C-22.9 (job B5).

- Rule: D-2026-10-15-03, "Ness's words, verbatim: "Q2 - a"" (OCT15:483).
- Also rests on: D-2026-10-29-03, Ness's wide reading: "רחבה 3." (NESS_ANSWERS_2026-10-29_v0_1.md:11).
- Source: `REPO/01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`:185, "(4) system remains advisory — cannot diagnose, prescribe, or act autonomously;".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged and still open: the tier selection and transition logic and the thresholds (C-22.6.5, NOT DECIDED); the unlock is the appointment record (DD:184). "cannot diagnose, prescribe" goes too: Ness chose the wide reading on 2026-10-29 (D-2026-10-29-03). Nothing here designs a diagnosing or prescribing function. The creation gate stays: Ness's "CONFIRMED: create nh_baseline_engine.py", the dry-run protocol and the prerequisites other than (4), the advisory condition, which goes (DD:185). The wording of DD §3K and cursorrules §12D changes later by new versioned files, never in place (OCT15:492). How the baseline reads REALITY promotions once T6's steer-not-file model applies (V10:3184) is a design slot (OCT15:497-498). C-22.9.4 keeps its ID; its name becomes "Removed advisory boundary" (A-2026-10-29-3).

Replaces:

```text
| V10 §22 limitation / architecture / build gate; DD §3K; CR §12D | C-22.8 limitation, C-22.9 build prerequisites and protected-file boundary. Preserve advisory/no-diagnosis/no-prescription/no-autonomous-action and no silent writes; exclude coding-workflow confirmation rituals. Mark the advisory-versus-promotion-control wording tension without resolving it. |
```

With:

```text
| V10 §22 limitation / architecture / build gate; DD §3K; CR §12D | C-22.8 limitation, C-22.9 build prerequisites and protected-file boundary. Preserve no silent writes; the advisory/no-diagnosis/no-prescription/no-autonomous-action condition is removed, and Tier 3/4 slow and pause REALITY promotion automatically (DECIDED-2026-10-29, [D-2026-10-15-03] [D-2026-10-29-03]); exclude coding-workflow confirmation rituals. |
```

**F-CH10-c-02574** · CH10-c:2574 · table row · `ready`

Place: Source-to-card coverage row placing V10 §22's limitation and DD §3K/CR §12D on C-22.8 and C-22.9; changed with C-22.9 (job B5).

- Rule: D-2026-10-15-03, "Ness's words, verbatim: "Q2 - a"" (OCT15:483).
- Also rests on: D-2026-10-29-03, Ness's wide reading: "רחבה 3." (NESS_ANSWERS_2026-10-29_v0_1.md:11).
- Source: `REPO/01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`:185, "(4) system remains advisory — cannot diagnose, prescribe, or act autonomously;".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged and still open: the tier selection and transition logic and the thresholds (C-22.6.5, NOT DECIDED); the unlock is the appointment record (DD:184). "cannot diagnose, prescribe" goes too: Ness chose the wide reading on 2026-10-29 (D-2026-10-29-03). Nothing here designs a diagnosing or prescribing function. The creation gate stays: Ness's "CONFIRMED: create nh_baseline_engine.py", the dry-run protocol and the prerequisites other than (4), the advisory condition, which goes (DD:185). The wording of DD §3K and cursorrules §12D changes later by new versioned files, never in place (OCT15:492). How the baseline reads REALITY promotions once T6's steer-not-file model applies (V10:3184) is a design slot (OCT15:497-498). C-22.9.4 keeps its ID; its name becomes "Removed advisory boundary" (A-2026-10-29-3).

Replaces:

```text
| V10 §22 limitation / architecture / build gate; DD §3K; CR §12D | C-22.8 limitation, C-22.9 build prerequisites and protected-file boundary. Preserve advisory/no-diagnosis/no-prescription/no-autonomous-action and no silent writes; exclude coding-workflow confirmation rituals. Mark the advisory-versus-promotion-control wording tension without resolving it. |
```

With:

```text
| V10 §22 limitation / architecture / build gate; DD §3K; CR §12D | C-22.8 limitation, C-22.9 build prerequisites and protected-file boundary. Preserve no silent writes; the advisory/no-diagnosis/no-prescription/no-autonomous-action condition is removed, and Tier 3/4 slow and pause REALITY promotion automatically (DECIDED-2026-10-29, [D-2026-10-15-03] [D-2026-10-29-03]); exclude coding-workflow confirmation rituals. |
```

#### C-22.9.4 — Advisory and non-diagnostic boundary (new name: Removed advisory boundary)

**F-CH10-c-00767** · CH10-c:767 · card name · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: D-2026-10-29-03, which the card's fixed text follows.
- Source: `REPO/01_AUTHORITATIVE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH10-c.md`:835, "### C-22.9.4 — Advisory and non-diagnostic boundary".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The card keeps its ID C-22.9.4. The new name was chosen by the worker and not shown to Ness one by one; he can change it.

Replaces:

```text
SUB-PARTS: C-22.9.1 — Stable pipeline prerequisite; C-22.9.2 — Healthy review queue for one month; C-22.9.3 — Defined baseline sources and consent boundaries; C-22.9.4 — Advisory and non-diagnostic boundary; C-22.9.5 — Named input and write boundaries; C-22.9.6 — No silent wellbeing writes
```

With:

```text
SUB-PARTS: C-22.9.1 — Stable pipeline prerequisite; C-22.9.2 — Healthy review queue for one month; C-22.9.3 — Defined baseline sources and consent boundaries; C-22.9.4 — Removed advisory boundary; C-22.9.5 — Named input and write boundaries; C-22.9.6 — No silent wellbeing writes
```

**F-CH10-c-00835** · CH10-c:835 · card name · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: D-2026-10-29-03, which the card's fixed text follows.
- Source: `REPO/01_AUTHORITATIVE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH10-c.md`:835, "### C-22.9.4 — Advisory and non-diagnostic boundary".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The card keeps its ID C-22.9.4. The new name was chosen by the worker and not shown to Ness one by one; he can change it.

Replaces:

```text
### C-22.9.4 — Advisory and non-diagnostic boundary
```

With:

```text
### C-22.9.4 — Removed advisory boundary
```

**F-CH10-c-00839** · CH10-c:839 · What it is · `ready`

- Rule: D-2026-10-29-03, "רחבה 3." (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:11).
- Source: `REPO/01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`:185, "cannot diagnose, prescribe, or act autonomously".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the creation gate (Ness's "CONFIRMED: create nh_baseline_engine.py", the dry-run protocol and the other prerequisites, DD:185), no silent wellbeing writes, and the appointment-record unlock (DD:184). Nothing here designs a diagnosing or prescribing function. The wording of DD §3K and cursorrules §12D changes later by new versioned files, never in place (OCT15:492). C-22.9.4 keeps its ID; its name becomes "Removed advisory boundary" (A-2026-10-29-3); its Fed by and Gated by stay NOT DECIDED.

Replaces:

```text
- What it is: DESIGNED — The advisory-only requirement carried by the baseline creation rules. [DD §3K]
```

With:

```text
- What it is: DECIDED-2026-10-29 — The removed advisory-only requirement: the baseline creation rules' condition that the system cannot diagnose, prescribe or act autonomously no longer applies. [D-2026-10-15-03] [D-2026-10-29-03] [DD §3K]
```

**F-CH10-c-00841** · CH10-c:841 · Does · `ready`

- Rule: D-2026-10-15-03, "Ness's words, verbatim: "Q2 - a"" (OCT15:483).
- Also rests on: D-2026-10-29-03, Ness's wide reading: "רחבה 3." (NESS_ANSWERS_2026-10-29_v0_1.md:11).
- Source: `REPO/01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`:185, "(4) system remains advisory — cannot diagnose, prescribe, or act autonomously;".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged and still open: the tier selection and transition logic and the thresholds (C-22.6.5, NOT DECIDED); the unlock is the appointment record (DD:184). "cannot diagnose, prescribe" goes too: Ness chose the wide reading on 2026-10-29 (D-2026-10-29-03). Nothing here designs a diagnosing or prescribing function. The creation gate stays: Ness's "CONFIRMED: create nh_baseline_engine.py", the dry-run protocol and the prerequisites other than (4), the advisory condition, which goes (DD:185). The wording of DD §3K and cursorrules §12D changes later by new versioned files, never in place (OCT15:492). How the baseline reads REALITY promotions once T6's steer-not-file model applies (V10:3184) is a design slot (OCT15:497-498). C-22.9.4 keeps its ID; its name becomes "Removed advisory boundary" (A-2026-10-29-3).

Replaces:

```text
- Does: DESIGNED — Keeps diagnosis, prescription and autonomous action outside the stated advisory scope. [DD §3K]
```

With:

```text
- Does: DECIDED-2026-10-29 — Sets no advisory limit: the advisory condition (no diagnosis, no prescription, no autonomous action) is removed, and the Tier 3 slowing and Tier 4 pausing of REALITY promotion run automatically. Nothing here adds a diagnosing or prescribing function. [D-2026-10-15-03] [D-2026-10-29-03] [DD §3K] [V10 §22]
```

**F-CH10-c-00842** · CH10-c:842 · Gives out · `ready`

- Rule: D-2026-10-29-03, "רחבה 3." (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:11).
- Source: `REPO/01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`:185, "cannot diagnose, prescribe, or act autonomously".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the creation gate (Ness's "CONFIRMED: create nh_baseline_engine.py", the dry-run protocol and the other prerequisites, DD:185), no silent wellbeing writes, and the appointment-record unlock (DD:184). Nothing here designs a diagnosing or prescribing function. The wording of DD §3K and cursorrules §12D changes later by new versioned files, never in place (OCT15:492). C-22.9.4 keeps its ID; its name becomes "Removed advisory boundary" (A-2026-10-29-3); its Fed by and Gated by stay NOT DECIDED.

Replaces:

```text
- Gives out: DESIGNED — An advisory limitation alongside V10's preserved tier effects. [DD §3K]
```

With:

```text
- Gives out: DECIDED-2026-10-29 — No advisory limitation; V10's tier effects run automatically. [D-2026-10-15-03] [D-2026-10-29-03] [DD §3K] [V10 §22]
```

**F-CH10-c-00843** · CH10-c:843 · Must never · `ready`

- Rule: D-2026-10-15-03, "Ness's words, verbatim: "Q2 - a"" (OCT15:483).
- Also rests on: D-2026-10-29-03, Ness's wide reading: "רחבה 3." (NESS_ANSWERS_2026-10-29_v0_1.md:11).
- Source: `REPO/01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`:185, "(4) system remains advisory — cannot diagnose, prescribe, or act autonomously;".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged and still open: the tier selection and transition logic and the thresholds (C-22.6.5, NOT DECIDED); the unlock is the appointment record (DD:184). "cannot diagnose, prescribe" goes too: Ness chose the wide reading on 2026-10-29 (D-2026-10-29-03). Nothing here designs a diagnosing or prescribing function. The creation gate stays: Ness's "CONFIRMED: create nh_baseline_engine.py", the dry-run protocol and the prerequisites other than (4), the advisory condition, which goes (DD:185). The wording of DD §3K and cursorrules §12D changes later by new versioned files, never in place (OCT15:492). How the baseline reads REALITY promotions once T6's steer-not-file model applies (V10:3184) is a design slot (OCT15:497-498). C-22.9.4 keeps its ID; its name becomes "Removed advisory boundary" (A-2026-10-29-3).

Replaces:

```text
- Must never: DESIGNED — Diagnose, prescribe or act autonomously. [CR §12D]
```

With:

```text
- Must never: DECIDED-2026-10-29 — No advisory prohibition remains: this boundary no longer forbids diagnosing, prescribing or autonomous action. [D-2026-10-15-03] [D-2026-10-29-03] [CR §12D]
```

**F-CH10-c-00844** · CH10-c:844 · Fails closed by · `ready`

- Rule: D-2026-10-29-03, "רחבה 3." (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:11).
- Source: `REPO/01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`:185, "cannot diagnose, prescribe, or act autonomously".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the creation gate (Ness's "CONFIRMED: create nh_baseline_engine.py", the dry-run protocol and the other prerequisites, DD:185), no silent wellbeing writes, and the appointment-record unlock (DD:184). Nothing here designs a diagnosing or prescribing function. The wording of DD §3K and cursorrules §12D changes later by new versioned files, never in place (OCT15:492). C-22.9.4 keeps its ID; its name becomes "Removed advisory boundary" (A-2026-10-29-3); its Fed by and Gated by stay NOT DECIDED.

Replaces:

```text
- Fails closed by: DESIGNED — Creation requires the advisory boundary to be defined and preserved. [DD §3K]
```

With:

```text
- Fails closed by: DECIDED-2026-10-29 — Creation no longer requires an advisory boundary; the other creation prerequisites stay. [D-2026-10-15-03] [D-2026-10-29-03] [DD §3K]
```

**F-CH10-c-00849** · CH10-c:849 · Changes · `ready`

- Rule: D-2026-10-29-03, "רחבה 3." (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:11).
- Source: `REPO/01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`:185, "cannot diagnose, prescribe, or act autonomously".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the creation gate (Ness's "CONFIRMED: create nh_baseline_engine.py", the dry-run protocol and the other prerequisites, DD:185), no silent wellbeing writes, and the appointment-record unlock (DD:184). Nothing here designs a diagnosing or prescribing function. The wording of DD §3K and cursorrules §12D changes later by new versioned files, never in place (OCT15:492). C-22.9.4 keeps its ID; its name becomes "Removed advisory boundary" (A-2026-10-29-3); its Fed by and Gated by stay NOT DECIDED.

Replaces:

```text
- Changes: DESIGNED — C-22.9 — Deferred protected baseline engine: limits the engine to the stated advisory scope. [DD §3K]
```

With:

```text
- Changes: DECIDED-2026-10-29 — C-22.9 — Deferred protected baseline engine: sets no advisory limit on the engine. [D-2026-10-15-03] [D-2026-10-29-03] [DD §3K]
```

**F-CH10-c-01311** · CH10-c:1311 · card name · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: D-2026-10-29-03, which the card's fixed text follows.
- Source: `REPO/01_AUTHORITATIVE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH10-c.md`:835, "### C-22.9.4 — Advisory and non-diagnostic boundary".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The card keeps its ID C-22.9.4. The new name was chosen by the worker and not shown to Ness one by one; he can change it.

Replaces:

```text
| C-22.9.4 — Advisory and non-diagnostic boundary | Fed by |
```

With:

```text
| C-22.9.4 — Removed advisory boundary | Fed by |
```

**F-CH10-c-01312** · CH10-c:1312 · card name · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: D-2026-10-29-03, which the card's fixed text follows.
- Source: `REPO/01_AUTHORITATIVE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH10-c.md`:835, "### C-22.9.4 — Advisory and non-diagnostic boundary".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The card keeps its ID C-22.9.4. The new name was chosen by the worker and not shown to Ness one by one; he can change it.

Replaces:

```text
| C-22.9.4 — Advisory and non-diagnostic boundary | Gated by |
```

With:

```text
| C-22.9.4 — Removed advisory boundary | Gated by |
```

**F-CH10-c-01368** · CH10-c:1368 · table row · `ready`

Place: Named review disposition row for C-22.9.4; changed with the card (job B5).

- Rule: D-2026-10-15-03, "Ness's words, verbatim: "Q2 - a"" (OCT15:483).
- Also rests on: D-2026-10-29-03, Ness's wide reading: "רחבה 3." (NESS_ANSWERS_2026-10-29_v0_1.md:11).
- Source: `REPO/01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`:185, "(4) system remains advisory — cannot diagnose, prescribe, or act autonomously;".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18); card name: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: Unchanged and still open: the tier selection and transition logic and the thresholds (C-22.6.5, NOT DECIDED); the unlock is the appointment record (DD:184). "cannot diagnose, prescribe" goes too: Ness chose the wide reading on 2026-10-29 (D-2026-10-29-03). Nothing here designs a diagnosing or prescribing function. The creation gate stays: Ness's "CONFIRMED: create nh_baseline_engine.py", the dry-run protocol and the prerequisites other than (4), the advisory condition, which goes (DD:185). The wording of DD §3K and cursorrules §12D changes later by new versioned files, never in place (OCT15:492). How the baseline reads REALITY promotions once T6's steer-not-file model applies (V10:3184) is a design slot (OCT15:497-498). C-22.9.4 keeps its ID; its name becomes "Removed advisory boundary" (A-2026-10-29-3).

Replaces:

```text
| C-22.9.4 — Advisory and non-diagnostic boundary; line 848 | prerequisite_review / Gated by | The advisory restriction is the condition being defined; its failure line requires that boundary. The unresolved source tension remains marked rather than converted into a new gate. |
```

With:

```text
| C-22.9.4 — Removed advisory boundary; line 848 | prerequisite_review / Gated by | The advisory restriction this card defined is removed by D-2026-10-15-03 as Ness read it on 2026-10-29 (DECIDED-2026-10-29): Tier 3 and Tier 4 act automatically, and no gate is added. [D-2026-10-15-03] [D-2026-10-29-03] |
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH10-c-01977** · CH10-c:1977 · table row · `ready`

Place: Carried row, identical to CH08-a:12164; same change as F-CH08-a-12164.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH10-c-01989** · CH10-c:1989 · table row · `ready`

Place: Carried row, identical to CH08-a:12176; same change as F-CH08-a-12176.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-7Q.5 — Third-party data baseline

**F-CH10-c-02135** · CH10-c:2135 · table row · `ready`

Place: Carried row, identical to CH09-b:923; same change as F-CH09-b-00923.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. Stronger-authorization and minor/vulnerable-default conflicts retained consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

With:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. The stronger-authorization (operation 3) and minor/vulnerable-default conflicts are decided for A7 by D-2026-10-15-02 T4, consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

### CH10-d

#### Chapter header

**F-CH10-d-00016** · CH10-d:16 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`. Decision keys `D-2026-10-15-02 T4`, `D-2026-10-15-03` and `D-2026-10-29-03`, added after the pinned commit, name Ness's decisions quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH10-d-01630** · CH10-d:1630 · table row · `ready`

Place: Carried row, identical to CH08-a:12164; same change as F-CH08-a-12164.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH10-d-01642** · CH10-d:1642 · table row · `ready`

Place: Carried row, identical to CH08-a:12176; same change as F-CH08-a-12176.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-7Q.5 — Third-party data baseline

**F-CH10-d-01788** · CH10-d:1788 · table row · `ready`

Place: Carried row, identical to CH09-b:923; same change as F-CH09-b-00923.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. Stronger-authorization and minor/vulnerable-default conflicts retained consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

With:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. The stronger-authorization (operation 3) and minor/vulnerable-default conflicts are decided for A7 by D-2026-10-15-02 T4, consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

#### C-22.9 — Deferred protected baseline engine

**F-CH10-d-02227** · CH10-d:2227 · table row · `ready`

Place: Carried row, identical to CH10-c:1201; same change as F-CH10-c-01201.

- Rule: D-2026-10-15-03, "Ness's words, verbatim: "Q2 - a"" (OCT15:483).
- Also rests on: D-2026-10-29-03, Ness's wide reading: "רחבה 3." (NESS_ANSWERS_2026-10-29_v0_1.md:11).
- Source: `REPO/01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`:185, "(4) system remains advisory — cannot diagnose, prescribe, or act autonomously;".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged and still open: the tier selection and transition logic and the thresholds (C-22.6.5, NOT DECIDED); the unlock is the appointment record (DD:184). "cannot diagnose, prescribe" goes too: Ness chose the wide reading on 2026-10-29 (D-2026-10-29-03). Nothing here designs a diagnosing or prescribing function. The creation gate stays: Ness's "CONFIRMED: create nh_baseline_engine.py", the dry-run protocol and the prerequisites other than (4), the advisory condition, which goes (DD:185). The wording of DD §3K and cursorrules §12D changes later by new versioned files, never in place (OCT15:492). How the baseline reads REALITY promotions once T6's steer-not-file model applies (V10:3184) is a design slot (OCT15:497-498). C-22.9.4 keeps its ID; its name becomes "Removed advisory boundary" (A-2026-10-29-3).

Replaces:

```text
| V10 §22 limitation / architecture / build gate; DD §3K; CR §12D | C-22.8 limitation, C-22.9 build prerequisites and protected-file boundary. Preserve advisory/no-diagnosis/no-prescription/no-autonomous-action and no silent writes; exclude coding-workflow confirmation rituals. Mark the advisory-versus-promotion-control wording tension without resolving it. |
```

With:

```text
| V10 §22 limitation / architecture / build gate; DD §3K; CR §12D | C-22.8 limitation, C-22.9 build prerequisites and protected-file boundary. Preserve no silent writes; the advisory/no-diagnosis/no-prescription/no-autonomous-action condition is removed, and Tier 3/4 slow and pause REALITY promotion automatically (DECIDED-2026-10-29, [D-2026-10-15-03] [D-2026-10-29-03]); exclude coding-workflow confirmation rituals. |
```

### CH10-e

#### Chapter header

**F-CH10-e-00024** · CH10-e:24 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`. Decision keys `D-2026-10-15-02 T4`, `D-2026-10-15-03` and `D-2026-10-29-03`, added after the pinned commit, name Ness's decisions quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH10-e-11131** · CH10-e:11131 · table row · `ready`

Place: Carried row, identical to CH08-a:12164; same change as F-CH08-a-12164.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH10-e-11143** · CH10-e:11143 · table row · `ready`

Place: Carried row, identical to CH08-a:12176; same change as F-CH08-a-12176.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-7Q.5 — Third-party data baseline

**F-CH10-e-11289** · CH10-e:11289 · table row · `ready`

Place: Carried row, identical to CH09-b:923; same change as F-CH09-b-00923.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. Stronger-authorization and minor/vulnerable-default conflicts retained consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

With:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. The stronger-authorization (operation 3) and minor/vulnerable-default conflicts are decided for A7 by D-2026-10-15-02 T4, consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

#### C-22.9 — Deferred protected baseline engine

**F-CH10-e-11728** · CH10-e:11728 · table row · `ready`

Place: Carried row, identical to CH10-c:1201; same change as F-CH10-c-01201.

- Rule: D-2026-10-15-03, "Ness's words, verbatim: "Q2 - a"" (OCT15:483).
- Also rests on: D-2026-10-29-03, Ness's wide reading: "רחבה 3." (NESS_ANSWERS_2026-10-29_v0_1.md:11).
- Source: `REPO/01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`:185, "(4) system remains advisory — cannot diagnose, prescribe, or act autonomously;".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged and still open: the tier selection and transition logic and the thresholds (C-22.6.5, NOT DECIDED); the unlock is the appointment record (DD:184). "cannot diagnose, prescribe" goes too: Ness chose the wide reading on 2026-10-29 (D-2026-10-29-03). Nothing here designs a diagnosing or prescribing function. The creation gate stays: Ness's "CONFIRMED: create nh_baseline_engine.py", the dry-run protocol and the prerequisites other than (4), the advisory condition, which goes (DD:185). The wording of DD §3K and cursorrules §12D changes later by new versioned files, never in place (OCT15:492). How the baseline reads REALITY promotions once T6's steer-not-file model applies (V10:3184) is a design slot (OCT15:497-498). C-22.9.4 keeps its ID; its name becomes "Removed advisory boundary" (A-2026-10-29-3).

Replaces:

```text
| V10 §22 limitation / architecture / build gate; DD §3K; CR §12D | C-22.8 limitation, C-22.9 build prerequisites and protected-file boundary. Preserve advisory/no-diagnosis/no-prescription/no-autonomous-action and no silent writes; exclude coding-workflow confirmation rituals. Mark the advisory-versus-promotion-control wording tension without resolving it. |
```

With:

```text
| V10 §22 limitation / architecture / build gate; DD §3K; CR §12D | C-22.8 limitation, C-22.9 build prerequisites and protected-file boundary. Preserve no silent writes; the advisory/no-diagnosis/no-prescription/no-autonomous-action condition is removed, and Tier 3/4 slow and pause REALITY promotion automatically (DECIDED-2026-10-29, [D-2026-10-15-03] [D-2026-10-29-03]); exclude coding-workflow confirmation rituals. |
```

### CH11

#### Chapter header

**F-CH11-00036** · CH11:36 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Decision keys `D-2026-10-15-01`, `D-2026-10-15-02 T2`, `D-2026-10-15-02 T3`, `D-2026-10-15-02 T4`, `D-2026-10-15-03` and `D-2026-10-29-03`, added after the pinned commit, name Ness's decisions quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### CY-A — New-root reading path

**F-CH11-00049** · CH11:49 · Steps · `ready`

Place: Path CY-A (CH11:42), step 4, which uses C-7GA.10; changed with F-CH00-00037 (P-MAIN step 7).

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
4. C-7GA.10 — thread_membership_v1 — DESIGNED — Takes in: Derived source_title_type, thread_present, thread_root_count and the trigger's declared mode and reason. Does: Run thread_membership_v1. Manual bare/local-context overrides are allowed; live_ingestion may narrow only to bare with a nonempty reason. Reject other declared overrides. Without an accepted override, a confirmed real_thread or untitled_session with preceding context receives local-context; first-in-group, singleton, unresolved, missing or unrecognized classification receives bare. Never assign associative or combined: fall back to bare and record any implementation error. The raw title string never assigns the mode. Changes: The instruction records the assignment inputs, accepted or rejected override and actual reason. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
```

With:

```text
4. C-7GA.10 — thread_membership_v1 — DESIGNED — Takes in: Derived source_title_type, thread_present, thread_root_count and the trigger's declared mode and reason. Does: Run the new-root mode-assignment rule. The raw title string never assigns the mode. Changes: The instruction records the assignment inputs, accepted or rejected override and actual reason. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
   DECIDED-2026-10-15 — The first reading follows R4, the largest accumulated context available; thread_membership_v1 (version 1, bare or local-context only) no longer governs it. The successor rule version that assigns the first reading's mode, with its inputs, overrides and fallbacks, is NOT DECIDED. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

**F-CH11-00053** · CH11:53 · Steps · `ready`

Place: Path CY-A (CH11:42), step 8, which uses C-7F and C-7GA.11.2; changed with F-CH05-b-02110.

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
8. C-7F — Context Retrieval (§7F) — DESIGNED — Takes in: The committed bare or local-context instruction. Does: For bare, return an empty context package without retrieval. For local-context, return only the authorized immediately preceding roots in the confirmed grouping, carrying provenance in a separate background section. Empty positional results are normal. Engine B's n=3 experiment is not a final live-path parameter. Changes: Target and positional context remain separate; retrieval system failure stops the pass as technical-failed. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
```

With:

```text
8. C-7F — Context Retrieval (§7F) — DESIGNED — Takes in: The committed pass instruction and its mode. Does: Return the context the committed mode permits, carrying provenance in a separate background section. Empty results are normal. Engine B's n=3 experiment is not a final live-path parameter. Changes: Target and positional context remain separate; retrieval system failure stops the pass as technical-failed. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS]
   DECIDED-2026-10-15 — For a first reading the context follows R4, the largest accumulated context available, not only bare or local context; the successor rule version's retrieval is NOT DECIDED. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9]
```

#### P-NEW-capture — Non-chat capture → Catalog → root

**F-CH11-00263** · CH11:263 · Trigger · `ready`

Place: Path P-NEW-capture (CH11:261), Trigger; changed with F-CH04-e-00020.

- Rule: D-2026-10-15-02 T3, "option A. Root first; the context-meaning stays a proposal beside it; Ness's" (OCT15:453).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:2843, "Metadata → plain-description → context-meaning → Ness confirms.".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The schema of a separate image confirmation or rejection event stays NOT DECIDED (STANDING T3). How the optional confirmation is surfaced (its notice form) is not designed. Unchanged: the meaning never becomes fact without Ness (C-9A.4 stays a prohibition), WhatsApp media stays frozen, live-camera help never stores automatically, in-world camera/VR keeps per-device approval (H1744).

Replaces:

```text
Trigger: DESIGNED — An eligible non-chat source supplies a capture through its own front door. An image follows its separate confirmation sequence; an already frozen import source is not silently reopened. [V10 §7E] [V10 §9A] [MAP C-INGEST]
```

With:

```text
Trigger: DESIGNED — An eligible non-chat source supplies a capture through its own front door; an already frozen import source is not silently reopened. [V10 §7E] [MAP C-INGEST]
Trigger: DECIDED-2026-10-15 — An image follows its proposal sequence and becomes a root without waiting for Ness's confirmation, which stays optional, surfaced and never asked. [D-2026-10-15-02 T3] [V10 §9A]
```

**F-CH11-00266** · CH11:266 · Steps · `ready`

Place: Path P-NEW-capture (CH11:261), step 2, which uses C-9A; changed with F-CH04-e-00020.

- Rule: D-2026-10-15-02 T3, "option A. Root first; the context-meaning stays a proposal beside it; Ness's" (OCT15:453).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:2843, "Metadata → plain-description → context-meaning → Ness confirms.".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The schema of a separate image confirmation or rejection event stays NOT DECIDED (STANDING T3). How the optional confirmation is surfaced (its notice form) is not designed. Unchanged: the meaning never becomes fact without Ness (C-9A.4 stays a prohibition), WhatsApp media stays frozen, live-camera help never stores automatically, in-world camera/VR keeps per-device approval (H1744).

Replaces:

```text
2. C-9A — Image ingest front door (§9A) — DESIGNED — Takes in: An image and its source metadata. Does: For the image branch, proceed metadata → proposed plain description → proposed context meaning → Ness confirmation. Do not install model-inferred context as a catalog fact. Changes: The image has a confirmed front-door result or remains unresolved. [V10 §9A] [V10 §7E]
```

With:

```text
2. C-9A — Image ingest front door (§9A) — DESIGNED — Takes in: An image and its source metadata. Does: For the image branch, proceed metadata → proposed plain description → proposed context meaning. Do not install model-inferred context as a catalog fact. Changes: The image has a front-door result and continues to Catalog. [V10 §9A] [V10 §7E]
   DECIDED-2026-10-15 — The image does not wait for Ness's confirmation; its context meaning stays a proposal, and his confirmation stays optional, surfaced and never asked. [D-2026-10-15-02 T3] [V10 §9A]
```

**F-CH11-00268** · CH11:268 · Steps · `ready`

Place: Path P-NEW-capture (CH11:261), step 4, which uses C-DETECT; changed with F-CH03-p-00143.

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:689, "Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`.".
- Stays open: C-DETECT.2.3 keeps its ID; after D-01 it records that no live question exists, and its name becomes "Live speaker hold" (A-2026-10-29-3). C-DETECT.2.4 still names its hold for "unattended material" (CH03-p:243 ff.); after D-01 live material with an unresolved speaker enters the same `speaker_unresolved` hold, and the final build may widen that card's wording to match. C-DETECT.2.5's authorized resolution rule stays NOT DECIDED (OCT15:398, :417), and so does the clear-evidence rule for speakers (OCT15:418). Ness may still confirm a speaker unasked (OCT15:400).

Replaces:

```text
4. C-DETECT — Speaker detector (fallback; investigated, not deployed) (§11) — DESIGNED — Takes in: A capture whose speaker cannot be established from source. Does: Offer only an uncertain candidate if the fallback detector is used. Live interaction asks for necessary attribution; unattended work remains speaker_unresolved. Never silently copy a prediction into role. Changes: Only source-supported or confirmed speaker attribution can clear the blocker. [V10 §7E] [MAP C-DETECT]
```

With:

```text
4. C-DETECT — Speaker detector (fallback; investigated, not deployed) (§11) — DESIGNED — Takes in: A capture whose speaker cannot be established from source. Does: Offer only an uncertain candidate if the fallback detector is used; unattended work remains speaker_unresolved. Never silently copy a prediction into role. Changes: Only source-supported or confirmed speaker attribution can clear the blocker. [V10 §7E] [MAP C-DETECT]
   DECIDED-2026-10-15 — N.H never asks Ness who spoke, even in live interaction; live material whose necessary speaker cannot be established is held as speaker_unresolved, as unattended material is. [D-2026-10-15-01] [V10 §7E]
```

**F-CH11-02154** · CH11:2154 · table row · `ready`

Place: CH00 path-table continuation row for path P-NEW-capture (CH11:2148-2156); changed with C-9A (F-CH04-e-00020).

- Rule: D-2026-10-15-02 T3, "option A. Root first; the context-meaning stays a proposal beside it; Ness's" (OCT15:453).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:2843, "Metadata → plain-description → context-meaning → Ness confirms.".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The schema of a separate image confirmation or rejection event stays NOT DECIDED (STANDING T3). How the optional confirmation is surfaced (its notice form) is not designed. Unchanged: the meaning never becomes fact without Ness (C-9A.4 stays a prohibition), WhatsApp media stays frozen, live-camera help never stores automatically, in-world camera/VR keeps per-device approval (H1744).

Replaces:

```text
| P-NEW-capture | Non-chat capture → Catalog → root | NOT DECIDED | DESIGNED — An eligible non-chat source supplies a capture through its own front door. An image follows its separate confirmation sequence; an already frozen import source is not silently reopened. [V10 §7E] [V10 §9A] [MAP C-INGEST] |
```

With:

```text
| P-NEW-capture | Non-chat capture → Catalog → root | NOT DECIDED | DESIGNED — An eligible non-chat source supplies a capture through its own front door; an already frozen import source is not silently reopened. DECIDED-2026-10-15 — An image follows its proposal sequence and becomes a root without waiting for Ness's confirmation, which stays optional, surfaced and never asked. [D-2026-10-15-02 T3] [V10 §7E] [V10 §9A] [MAP C-INGEST] |
```

#### C-7GA.10 — thread_membership_v1

**F-CH11-02202** · CH11:2202 · USED BY · `ready`

Place: Row of "USED BY continuation for C-7GA.10 — thread_membership_v1" (CH11:2198): C-7GA.10's use in CY-A step 4; changed with F-CH05-b-00062.

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
| C-7GA.10 — thread_membership_v1 | 1 · DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A), in CY-A — New-root reading path (step 4) | Derived source_title_type, thread_present, thread_root_count and the trigger's declared mode and reason. [V10 §7G-A / MODE-ASSIGNMENT RULE:] [V10 §7G-A] [MAP C-7GA] | Run thread_membership_v1. Manual bare/local-context overrides are allowed; live_ingestion may narrow only to bare with a nonempty reason. Reject other declared overrides. Without an accepted override, a confirmed real_thread or untitled_session with preceding context receives local-context; first-in-group, singleton, unresolved, missing or unrecognized classification receives bare. Never assign associative or combined: fall back to bare and record any implementation error. The raw title string never assigns the mode. [V10 §7G-A / MODE-ASSIGNMENT RULE:] [V10 §7G-A] [MAP C-7GA] | The instruction records the assignment inputs, accepted or rejected override and actual reason. [V10 §7G-A / MODE-ASSIGNMENT RULE:] [V10 §7G-A] [MAP C-7GA] | [V10 §7G-A / MODE-ASSIGNMENT RULE:] [V10 §7G-A] [MAP C-7GA] |
```

With:

```text
| C-7GA.10 — thread_membership_v1 | 1 · DECIDED-2026-10-15 | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A), in CY-A — New-root reading path (step 4) | Derived source_title_type, thread_present, thread_root_count and the trigger's declared mode and reason. [V10 §7G-A / MODE-ASSIGNMENT RULE:] [V10 §7G-A] [MAP C-7GA] | Run the new-root mode-assignment rule for the first reading. The first reading follows R4, the largest accumulated context available; thread_membership_v1 (version 1, bare or local-context only) no longer governs it. The successor rule version's inputs, overrides and fallbacks are NOT DECIDED. The raw title string never assigns the mode. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9] [V10 §7G-A / MODE-ASSIGNMENT RULE:] [V10 §7G-A] [MAP C-7GA] | The instruction records the assignment inputs, accepted or rejected override and actual reason. [V10 §7G-A / MODE-ASSIGNMENT RULE:] [V10 §7G-A] [MAP C-7GA] | [V10 §7G-A / MODE-ASSIGNMENT RULE:] [V10 §7G-A] [MAP C-7GA] |
```

#### C-7F — Context Retrieval (§7F)

**F-CH11-02226** · CH11:2226 · USED BY · `ready`

Place: Row of "USED BY continuation for C-7F — Context Retrieval (§7F)" (CH11:2222): C-7GA.11.2's use in CY-A step 8; changed with F-CH05-b-02110.

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
| C-7F — Context Retrieval (§7F) | 1 · DESIGNED | C-7GA.11.2 — Step 2 — Retrieve context through LMAC, in CY-A — New-root reading path (step 8) | The committed bare or local-context instruction. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] | For bare, return an empty context package without retrieval. For local-context, return only the authorized immediately preceding roots in the confirmed grouping, carrying provenance in a separate background section. Empty positional results are normal. Engine B's n=3 experiment is not a final live-path parameter. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] | Target and positional context remain separate; retrieval system failure stops the pass as technical-failed. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
```

With:

```text
| C-7F — Context Retrieval (§7F) | 1 · DECIDED-2026-10-15 | C-7GA.11.2 — Step 2 — Retrieve context through LMAC, in CY-A — New-root reading path (step 8) | The committed pass instruction and its mode. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] | Return the context the committed mode permits; for a first reading that follows R4, and the successor rule version's retrieval is NOT DECIDED. Carry provenance in a separate background section. Empty results are normal. Engine B's n=3 experiment is not a final live-path parameter. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] | Target and positional context remain separate; retrieval system failure stops the pass as technical-failed. [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
```

#### C-9A — Image ingest front door (§9A)

**F-CH11-02828** · CH11:2828 · USED BY · `ready`

Place: Row of "USED BY continuation for C-9A — Image ingest front door (§9A)" (CH11:2824): C-9A's use in P-NEW-capture step 2; changed with F-CH04-e-00020.

- Rule: D-2026-10-15-02 T3, "option A. Root first; the context-meaning stays a proposal beside it; Ness's" (OCT15:453).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:2843, "Metadata → plain-description → context-meaning → Ness confirms.".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The schema of a separate image confirmation or rejection event stays NOT DECIDED (STANDING T3). How the optional confirmation is surfaced (its notice form) is not designed. Unchanged: the meaning never becomes fact without Ness (C-9A.4 stays a prohibition), WhatsApp media stays frozen, live-camera help never stores automatically, in-world camera/VR keeps per-device approval (H1744).

Replaces:

```text
| C-9A — Image ingest front door (§9A) | 1 · DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E), in P-NEW-capture — Non-chat capture → Catalog → root (step 2) | An image and its source metadata. [V10 §9A] [V10 §7E] [V10 §7E] [MAP C-7E] | For the image branch, proceed metadata → proposed plain description → proposed context meaning → Ness confirmation. Do not install model-inferred context as a catalog fact. [V10 §9A] [V10 §7E] [V10 §7E] [MAP C-7E] | The image has a confirmed front-door result or remains unresolved. [V10 §9A] [V10 §7E] [V10 §7E] [MAP C-7E] | [V10 §9A] [V10 §7E] [V10 §7E] [MAP C-7E] |
```

With:

```text
| C-9A — Image ingest front door (§9A) | 1 · DECIDED-2026-10-15 | C-7E — Catalog Front Door + pre-ingest holding (§7E), in P-NEW-capture — Non-chat capture → Catalog → root (step 2) | An image and its source metadata. [V10 §9A] [V10 §7E] [V10 §7E] [MAP C-7E] | For the image branch, proceed metadata → proposed plain description → proposed context meaning; the image does not wait for Ness's confirmation, which stays optional, surfaced and never asked. Do not install model-inferred context as a catalog fact. [V10 §9A] [V10 §7E] [V10 §7E] [MAP C-7E] | The image has a front-door result and continues to Catalog; its context meaning stays a proposal until Ness confirms it, if he chooses. [D-2026-10-15-02 T3] [V10 §9A] [V10 §7E] [V10 §7E] [MAP C-7E] | [V10 §9A] [V10 §7E] [V10 §7E] [MAP C-7E] |
```

#### C-DETECT — Speaker detector (fallback; investigated, not deployed) (§11)

**F-CH11-02834** · CH11:2834 · USED BY · `ready`

Place: Row of "USED BY continuation for C-DETECT — Speaker detector" (CH11:2830): C-DETECT's use in P-NEW-capture step 4; changed with F-CH03-p-00143.

- Rule: D-2026-10-15-01, ""In my opinion, b"" (OCT15:386).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:689, "Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`.".
- Stays open: C-DETECT.2.3 keeps its ID; after D-01 it records that no live question exists, and its name becomes "Live speaker hold" (A-2026-10-29-3). C-DETECT.2.4 still names its hold for "unattended material" (CH03-p:243 ff.); after D-01 live material with an unresolved speaker enters the same `speaker_unresolved` hold, and the final build may widen that card's wording to match. C-DETECT.2.5's authorized resolution rule stays NOT DECIDED (OCT15:398, :417), and so does the clear-evidence rule for speakers (OCT15:418). Ness may still confirm a speaker unasked (OCT15:400).

Replaces:

```text
| C-DETECT — Speaker detector (fallback; investigated, not deployed) (§11) | 1 · DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E), in P-NEW-capture — Non-chat capture → Catalog → root (step 4) | A capture whose speaker cannot be established from source. [V10 §7E] [MAP C-DETECT] [V10 §7E] [MAP C-7E] | Offer only an uncertain candidate if the fallback detector is used. Live interaction asks for necessary attribution; unattended work remains speaker_unresolved. Never silently copy a prediction into role. [V10 §7E] [MAP C-DETECT] [V10 §7E] [MAP C-7E] | Only source-supported or confirmed speaker attribution can clear the blocker. [V10 §7E] [MAP C-DETECT] [V10 §7E] [MAP C-7E] | [V10 §7E] [MAP C-DETECT] [V10 §7E] [MAP C-7E] |
```

With:

```text
| C-DETECT — Speaker detector (fallback; investigated, not deployed) (§11) | 1 · DECIDED-2026-10-15 | C-7E — Catalog Front Door + pre-ingest holding (§7E), in P-NEW-capture — Non-chat capture → Catalog → root (step 4) | A capture whose speaker cannot be established from source. [V10 §7E] [MAP C-DETECT] [V10 §7E] [MAP C-7E] | Offer only an uncertain candidate if the fallback detector is used. N.H never asks Ness who spoke, live or unattended; a capture whose necessary speaker cannot be established remains speaker_unresolved. [D-2026-10-15-01] Never silently copy a prediction into role. [V10 §7E] [MAP C-DETECT] [V10 §7E] [MAP C-7E] | Only source-supported or confirmed speaker attribution can clear the blocker. [V10 §7E] [MAP C-DETECT] [V10 §7E] [MAP C-7E] | [V10 §7E] [MAP C-DETECT] [V10 §7E] [MAP C-7E] |
```

#### C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A)

**F-CH11-03272** · CH11:3272 · table row · `ready`

Place: Row of the "Cross-piece TOGETHER continuations — path uses" table (CH11:3263): C-7GA's Fed by in CY-A step 4; changed with F-CH05-b-03505.

- Rule: D-2026-10-15-02 T2, "option B. R4 (widest accumulated context) governs" (OCT15:450).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:1983, "**Hard prohibition — permanent for this rule version:**".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl).

Replaces:

```text
| C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | Fed by | DESIGNED — C-7GA.10 — thread_membership_v1: The instruction records the assignment inputs, accepted or rejected override and actual reason. | CY-A / 4 | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
```

With:

```text
| C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | Fed by | DESIGNED — C-7GA.10 — thread_membership_v1: The instruction records the assignment inputs, accepted or rejected override and actual reason. DECIDED-2026-10-15 — For a first reading the assigning rule is the successor version (NOT DECIDED); thread_membership_v1 (version 1, bare or local-context only) no longer governs it. [D-2026-10-15-02 T2] FR-0158 [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9] | CY-A / 4 | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
```

#### C-7E — Catalog Front Door + pre-ingest holding (§7E)

**F-CH11-03385** · CH11:3385 · table row · `ready`

Place: Row of the "Cross-piece TOGETHER continuations — path uses" table (CH11:3263): C-7E's Fed by from C-9A in P-NEW-capture step 2; changed with F-CH04-e-00020.

- Rule: D-2026-10-15-02 T3, "option A. Root first; the context-meaning stays a proposal beside it; Ness's" (OCT15:453).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:2843, "Metadata → plain-description → context-meaning → Ness confirms.".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The schema of a separate image confirmation or rejection event stays NOT DECIDED (STANDING T3). How the optional confirmation is surfaced (its notice form) is not designed. Unchanged: the meaning never becomes fact without Ness (C-9A.4 stays a prohibition), WhatsApp media stays frozen, live-camera help never stores automatically, in-world camera/VR keeps per-device approval (H1744).

Replaces:

```text
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | Fed by | DESIGNED — C-9A — Image ingest front door (§9A): The image has a confirmed front-door result or remains unresolved. | P-NEW-capture / 2 | [V10 §9A] [V10 §7E] |
```

With:

```text
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | Fed by | DESIGNED — C-9A — Image ingest front door (§9A): The image has a front-door result. DECIDED-2026-10-15 — It continues to Catalog without waiting for Ness's confirmation, which stays optional, surfaced and never asked; its context meaning stays a proposal. [D-2026-10-15-02 T3] | P-NEW-capture / 2 | [V10 §9A] [V10 §7E] |
```

#### C-7B.8.4 — Live catalog exception (new name: Live catalog boundary)

**F-CH11-03998** · CH11:3998 · card name · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: D-2026-10-15-01, which the card's fixed text follows.
- Source: `REPO/01_AUTHORITATIVE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH02.md`:6520, "### C-7B.8.4 — Live catalog exception".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The card keeps its ID C-7B.8.4. The new name was chosen by the worker and not shown to Ness one by one; he can change it.

Replaces:

```text
| C-7B.8.4 — Live catalog exception | CY-J step 4 | Through C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B) |
```

With:

```text
| C-7B.8.4 — Live catalog boundary | CY-J step 4 | Through C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B) |
```

#### C-DETECT.2.3 — Live speaker question (new name: Live speaker hold)

**F-CH11-06428** · CH11:6428 · card name · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: D-2026-10-15-01, which the card's fixed text follows.
- Source: `REPO/01_AUTHORITATIVE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-p.md`:213, "### C-DETECT.2.3 — Live speaker question".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The card keeps its ID C-DETECT.2.3. The new name was chosen by the worker and not shown to Ness one by one; he can change it.

Replaces:

```text
| C-DETECT.2.3 — Live speaker question | P-NEW-capture step 4 | Through C-DETECT — Speaker detector (fallback; investigated, not deployed) (§11) |
```

With:

```text
| C-DETECT.2.3 — Live speaker hold | P-NEW-capture step 4 | Through C-DETECT — Speaker detector (fallback; investigated, not deployed) (§11) |
```

#### C-22.9.4 — Advisory and non-diagnostic boundary (new name: Removed advisory boundary)

**F-CH11-12578** · CH11:12578 · card name · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: D-2026-10-29-03, which the card's fixed text follows.
- Source: `REPO/01_AUTHORITATIVE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH10-c.md`:835, "### C-22.9.4 — Advisory and non-diagnostic boundary".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The card keeps its ID C-22.9.4. The new name was chosen by the worker and not shown to Ness one by one; he can change it.

Replaces:

```text
| C-22.9.4 — Advisory and non-diagnostic boundary | P-NEW-learning step 6 | Through C-22 — Wellbeing & Behavioral Baseline (§22) |
```

With:

```text
| C-22.9.4 — Removed advisory boundary | P-NEW-learning step 6 | Through C-22 — Wellbeing & Behavioral Baseline (§22) |
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH11-14030** · CH11:14030 · table row · `ready`

Place: Carried row, identical to CH08-a:12164; same change as F-CH08-a-12164.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation ladder with A7's interpretation rule (D-2026-10-15-02 T4), hypothetical simulation, no automatic minor/vulnerable restriction and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH11-14042** · CH11:14042 · table row · `ready`

Place: Carried row, identical to CH08-a:12176; same change as F-CH08-a-12176.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

With:

```text
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry A30's target, which D-2026-10-15-02 T4 lets govern (no automatic minor restriction); deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
```

#### C-7Q.5 — Third-party data baseline

**F-CH11-14188** · CH11:14188 · table row · `ready`

Place: Carried row, identical to CH09-b:923; same change as F-CH09-b-00923.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. Stronger-authorization and minor/vulnerable-default conflicts retained consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

With:

```text
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. The stronger-authorization (operation 3) and minor/vulnerable-default conflicts are decided for A7 by D-2026-10-15-02 T4, consistently with CH08-a; no new simulation or fixed-profile mechanism |
```

#### C-22.9 — Deferred protected baseline engine

**F-CH11-14627** · CH11:14627 · table row · `ready`

Place: Carried row, identical to CH10-c:1201; same change as F-CH10-c-01201.

- Rule: D-2026-10-15-03, "Ness's words, verbatim: "Q2 - a"" (OCT15:483).
- Also rests on: D-2026-10-29-03, Ness's wide reading: "רחבה 3." (NESS_ANSWERS_2026-10-29_v0_1.md:11).
- Source: `REPO/01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`:185, "(4) system remains advisory — cannot diagnose, prescribe, or act autonomously;".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged and still open: the tier selection and transition logic and the thresholds (C-22.6.5, NOT DECIDED); the unlock is the appointment record (DD:184). "cannot diagnose, prescribe" goes too: Ness chose the wide reading on 2026-10-29 (D-2026-10-29-03). Nothing here designs a diagnosing or prescribing function. The creation gate stays: Ness's "CONFIRMED: create nh_baseline_engine.py", the dry-run protocol and the prerequisites other than (4), the advisory condition, which goes (DD:185). The wording of DD §3K and cursorrules §12D changes later by new versioned files, never in place (OCT15:492). How the baseline reads REALITY promotions once T6's steer-not-file model applies (V10:3184) is a design slot (OCT15:497-498). C-22.9.4 keeps its ID; its name becomes "Removed advisory boundary" (A-2026-10-29-3).

Replaces:

```text
| V10 §22 limitation / architecture / build gate; DD §3K; CR §12D | C-22.8 limitation, C-22.9 build prerequisites and protected-file boundary. Preserve advisory/no-diagnosis/no-prescription/no-autonomous-action and no silent writes; exclude coding-workflow confirmation rituals. Mark the advisory-versus-promotion-control wording tension without resolving it. |
```

With:

```text
| V10 §22 limitation / architecture / build gate; DD §3K; CR §12D | C-22.8 limitation, C-22.9 build prerequisites and protected-file boundary. Preserve no silent writes; the advisory/no-diagnosis/no-prescription/no-autonomous-action condition is removed, and Tier 3/4 slow and pause REALITY promotion automatically (DECIDED-2026-10-29, [D-2026-10-15-03] [D-2026-10-29-03]); exclude coding-workflow confirmation rituals. |
```

### CH12-a

#### Chapter header

**F-CH12-a-00012** · CH12-a:12 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; DR = `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_2026-09-24_v0_1_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `05i/` = `05_INACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`; `[NHD-…]` tags are preserved source identifiers. Chapter codes and one-based line/cell locators refer to the exact files in the READ RECORD.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; DR = `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_2026-09-24_v0_1_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `05i/` = `05_INACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`; `[NHD-…]` tags are preserved source identifiers. Chapter codes and one-based line/cell locators refer to the exact files in the READ RECORD. Decision key `D-2026-10-15-02 T2`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

### CH12-d

#### Chapter header

**F-CH12-d-00012** · CH12-d:12 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; DR = `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_2026-09-24_v0_1_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `05i/` = `05_INACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`; `[NHD-…]` tags are preserved source identifiers. Chapter codes and one-based line/cell locators refer to the exact files in the READ RECORD.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; DR = `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_2026-09-24_v0_1_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `05i/` = `05_INACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`; `[NHD-…]` tags are preserved source identifiers. Chapter codes and one-based line/cell locators refer to the exact files in the READ RECORD. Decision keys `D-2026-10-15-02 T4` and `D-2026-10-29-04`, added after the pinned commit, name Ness's decisions quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### C-9A.7.1.4 — WhatsApp privacy stage

**F-CH12-d-00088** · CH12-d:88 · register row · `ready`

Place: Appendix D (source-conflict register) row 68, an exact copy of CH04-e:1401; changed with F-CH04-e-01401 (job B5: appendix rows change with their card). The fixed line keeps its [SOURCE CONFLICT] mark and states the decision, so the row carries the fixed line.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485). The [SOURCE CONFLICT: V10 §7Q prescribes stronger default restrictions ...] mark on C-9A.7.1.4 Does (CH04-e:427) stays visible (contract §1.5); D-02 T4 decides that conflict.

Replaces:

```text
| 68 | CH04-e:1401 | Source conflicts and explicit source-scope differences | \| [SOURCE CONFLICT] \| V10 §7Q / THIRD-PARTY DATA RULES requires stronger default restriction for minors and highly vulnerable people. Bundle 6 policy §4 A30 and mechanical §11 B22 prohibit automatic stronger restriction, block, weakened analysis or special simulation prohibition solely for age or vulnerability. \| V10 remains governing. The accepted opposing target is preserved explicitly in C-9A.7.1.4; no reconciliation or hidden integration is chosen. \| |
```

With:

```text
| 68 | CH04-e:1401 | Source conflicts and explicit source-scope differences | \| [SOURCE CONFLICT] \| V10 §7Q / THIRD-PARTY DATA RULES requires stronger default restriction for minors and highly vulnerable people. Bundle 6 policy §4 A30 and mechanical §11 B22 prohibit automatic stronger restriction, block, weakened analysis or special simulation prohibition solely for age or vulnerability. \| Decided by D-2026-10-15-02 T4: A7 removed the V10 rule (A7 §6.2), so the A30 target in C-9A.7.1.4 governs. \| |
```

#### C-7Q — Privacy, Deletion, Sensitive-data (§7Q)

**F-CH12-d-00104** · CH12-d:104 · register row · `ready`

Place: Appendix D (source-conflict register) row 84, an exact copy of CH08-a:12; changed with F-CH08-a-00012 (job B5: appendix rows change with their card). The fixed line keeps its [SOURCE CONFLICT] mark and states the decision, so the row carries the fixed line.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules.

Replaces:

```text
| 84 | CH08-a:12 | Chapter 8-a — Group F: C-7Q | [SOURCE CONFLICT] V10 §7Q requires stronger authorization at each later third-party operation. Accepted A7 §§4.5/4.6/6.1 and B7 §§3/17 permit ordinary bounded interpretation without separate permission. V10 governs; compatible interpretation labels and full-simulation approval remain explicit. |
```

With:

```text
| 84 | CH08-a:12 | Chapter 8-a — Group F: C-7Q | [SOURCE CONFLICT] V10 §7Q requires stronger authorization at each later third-party operation. Accepted A7 §§4.5/4.6/6.1 and B7 §§3/17 permit ordinary bounded interpretation without separate permission. By D-2026-10-15-02 T4, A7 governs: ordinary bounded interpretation (operation 3) needs no separate permission, and a constructed model of the person (operation 4) is the full simulation that needs Ness's clear prior approval. Compatible interpretation labels remain explicit. Operation 2 (recording what another person said or did) needs only the existing capture and third-party rules, by Ness's answer of 2026-10-29 (D-2026-10-29-04). |
```

**F-CH12-d-00105** · CH12-d:105 · register row · `ready`

Place: Appendix D (source-conflict register) row 85, an exact copy of CH08-a:14; changed with F-CH08-a-00014 (job B5: appendix rows change with their card). The fixed line keeps its [SOURCE CONFLICT] mark and states the decision, so the row carries the fixed line.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| 85 | CH08-a:14 | Chapter 8-a — Group F: C-7Q | [SOURCE CONFLICT] V10 §7Q requires stronger defaults for minors and vulnerable people. Accepted A7 §§4.7/6.2, B7 §§3/17 and Bundle 6 A30 remove automatic age/vulnerability restrictions. Bundle 5 §8 calls the V10 sentence frozen predecision wording and the accepted policy a settled slot; that competing explanation is preserved. Under build-contract §1.5 V10 still governs. CH04-e’s existing marked disagreement is carried forward. |
```

With:

```text
| 85 | CH08-a:14 | Chapter 8-a — Group F: C-7Q | [SOURCE CONFLICT] V10 §7Q requires stronger defaults for minors and vulnerable people. Accepted A7 §§4.7/6.2, B7 §§3/17 and Bundle 6 A30 remove automatic age/vulnerability restrictions. Bundle 5 §8 calls the V10 sentence frozen predecision wording and the accepted policy a settled slot. By D-2026-10-15-02 T4 the automatic minors/vulnerable rule is removed: A7 governs, age or vulnerability alone change nothing, and only Ness's explicit person- or group-specific configuration gives different handling. CH04-e's marked disagreement is decided the same way. |
```

#### C-7Q.5.3 — Four-operation third-party authorization ladder

**F-CH12-d-00115** · CH12-d:115 · register row · `ready`

Place: Appendix D (source-conflict register) row 95, an exact copy of CH08-a:1826; changed with F-CH08-a-01826 (job B5: appendix rows change with their card). The fixed line carries no [SOURCE CONFLICT] mark, so the row leaves the register.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules.

Replaces:

```text
| 95 | CH08-a:1826 | C-7Q.5.3 | - Does: DESIGNED — Normally permits the first activity; each later activity needs stronger authorization. [SOURCE CONFLICT: NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §§4.5/4.6/6.1 and NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md §3 allow ordinary bounded interpretation without separate permission.] [V10 §7Q] |
```

With:

```text
(row 95 removed) The marked line it copies, CH08-a:1826, is replaced by F-CH08-a-01826 and carries no [SOURCE CONFLICT] mark after that fix, so Appendix D no longer lists it.
```

**F-CH12-d-00116** · CH12-d:116 · register row · `ready`

Place: Appendix D (source-conflict register) row 96, an exact copy of CH08-a:1843; changed with F-CH08-a-01843 (job B5: appendix rows change with their card). The fixed line carries no [SOURCE CONFLICT] mark, so the row leaves the register.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules.

Replaces:

```text
| 96 | CH08-a:1843 | C-7Q.5.3 | \| 5 · DESIGNED \| C-OTHER.7.1 — Interpret a parent's statement for Ness \| The parent's statement and Ness's request to understand it. \| Gates this place: V10's stronger-authorization requirement applies to interpretation. \| Nothing in this card. \| [V10 §25.2 / Parent Translation] [V10 §7Q] [SOURCE CONFLICT: A7 §§4.5/6.1 and B7 §3 allow ordinary bounded interpretation without separate permission.] \| |
```

With:

```text
(row 96 removed) The marked line it copies, CH08-a:1843, is replaced by F-CH08-a-01843 and carries no [SOURCE CONFLICT] mark after that fix, so Appendix D no longer lists it.
```

#### C-7Q.5.3.3 — Interpreting another person’s possible meaning

**F-CH12-d-00117** · CH12-d:117 · register row · `ready`

Place: Appendix D (source-conflict register) row 97, an exact copy of CH08-a:1899; changed with F-CH08-a-01899 (job B5: appendix rows change with their card). The fixed line carries no [SOURCE CONFLICT] mark, so the row leaves the register.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules.

Replaces:

```text
| 97 | CH08-a:1899 | C-7Q.5.3.3 | - Does: DESIGNED — Requires the stronger authorization in V10. [SOURCE CONFLICT: NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §§4.5/6.1 and NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md §3 say ordinary bounded interpretation needs no separate permission.] Keeps permitted interpretations as possibilities, with alternatives and missing information visible. [V10 §7Q] [04/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §4.5] |
```

With:

```text
(row 97 removed) The marked line it copies, CH08-a:1899, is replaced by F-CH08-a-01899 and carries no [SOURCE CONFLICT] mark after that fix, so Appendix D no longer lists it.
```

#### C-7Q.5.5 — Stronger minor and vulnerable-person defaults

**F-CH12-d-00118** · CH12-d:118 · register row · `ready`

Place: Appendix D (source-conflict register) row 98, an exact copy of CH08-a:1971; changed with F-CH08-a-01971 (job B5: appendix rows change with their card). The fixed line carries no [SOURCE CONFLICT] mark, so the row leaves the register.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:483, "that sentence is superseded and the rule removed: no automatic".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| 98 | CH08-a:1971 | C-7Q.5.5 | - Does: DESIGNED — Applies the stronger default. [SOURCE CONFLICT: NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md §§4.7/6.2, NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md §3, NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4/A30, NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11 and NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md §§5/8 remove automatic age/vulnerability restrictions; Bundle 5 calls V10’s sentence frozen predecision wording.] [V10 §7Q] |
```

With:

```text
(row 98 removed) The marked line it copies, CH08-a:1971, is replaced by F-CH08-a-01971 and carries no [SOURCE CONFLICT] mark after that fix, so Appendix D no longer lists it.
```

#### C-OTHER — Other-Speaker / Guest / Known-Person Architecture (§25.2)

**F-CH12-d-00131** · CH12-d:131 · register row · `ready`

Place: Appendix D (source-conflict register) row 111, an exact copy of CH09-b:14; changed with F-CH09-b-00014 (job B5: appendix rows change with their card). The fixed line keeps its [SOURCE CONFLICT] mark and states the decision, so the row carries the fixed line.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485).

Replaces:

```text
| 111 | CH09-b:14 | Chapter 9-b — Group G: C-OTHER | [SOURCE CONFLICT: V10 §7Q requires increasingly stronger authorization for later third-party operations and stronger default restrictions for minors/highly vulnerable people. A7 §§4.5–4.7/6 and B7 §3 permit ordinary bounded interpretation without separate permission and remove automatic category restrictions; Bundle 5 §8 calls the V10 wording frozen pre-decision text. V10 governs this candidate under the build contract. Existing CH08-a conflicts remain open.] |
```

With:

```text
| 111 | CH09-b:14 | Chapter 9-b — Group G: C-OTHER | [SOURCE CONFLICT: V10 §7Q requires increasingly stronger authorization for later third-party operations and stronger default restrictions for minors/highly vulnerable people. A7 §§4.5–4.7/6 and B7 §3 permit ordinary bounded interpretation without separate permission and remove automatic category restrictions; Bundle 5 §8 calls the V10 wording frozen pre-decision text. By D-2026-10-15-02 T4, A7 governs both: ordinary bounded interpretation needs no separate permission, and no automatic minor/vulnerable restriction exists. Operation 2 needs only the existing capture and third-party rules, by Ness's answer of 2026-10-29 (D-2026-10-29-04), as in CH08-a.] |
```

#### C-OTHER.7.1 — Interpret a parent's statement for Ness

**F-CH12-d-00134** · CH12-d:134 · register row · `ready`

Place: Appendix D (source-conflict register) row 114, an exact copy of CH09-b:321; changed with F-CH09-b-00321 (job B5: appendix rows change with their card). The fixed line carries no [SOURCE CONFLICT] mark, so the row leaves the register.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules.

Replaces:

```text
| 114 | CH09-b:321 | C-OTHER.7.1 | - Gated by: DESIGNED — C-OTHER.7 — Request-driven parent translation: Ness must request this branch; C-7Q.5.3 — Four-operation third-party authorization ladder: V10's stronger-authorization requirement applies to interpretation. [V10 §25.2 / Parent Translation] [V10 §7Q] [SOURCE CONFLICT: A7 §§4.5/6.1 and B7 §3 allow ordinary bounded interpretation without separate permission.] |
```

With:

```text
(row 114 removed) The marked line it copies, CH09-b:321, is replaced by F-CH09-b-00321 and carries no [SOURCE CONFLICT] mark after that fix, so Appendix D no longer lists it.
```

**F-CH12-d-00136** · CH12-d:136 · register row · `ready`

Place: Appendix D (source-conflict register) row 116, an exact copy of CH09-b:835; changed with F-CH09-b-00835 (job B5: appendix rows change with their card). The fixed line carries no [SOURCE CONFLICT] mark, so the row leaves the register.

- Rule: D-2026-10-15-02 T4, "accepted A7 (2026-07-13) governs over V10 §7Q" (OCT15:456).
- Also rests on: D-2026-10-29-04, operation 2 needs only the existing capture and third-party rules: "4. כן, הכללים מתאימים." (NESS_ANSWERS_2026-10-29_v0_1.md:12).
- Source: `REPO/04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`:472, "stronger-authorization requirement is superseded **for operation 3 as".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules.

Replaces:

```text
| 116 | CH09-b:835 | Cross-piece USED BY continuations | \| C-7Q.5.3 — Four-operation third-party authorization ladder \| C-OTHER.7.1 — Interpret a parent's statement for Ness \| Gated by \| DESIGNED — C-OTHER.7 — Request-driven parent translation: Ness must request this branch; C-7Q.5.3 — Four-operation third-party authorization ladder: V10's stronger-authorization requirement applies to interpretation. [V10 §25.2 / Parent Translation] [V10 §7Q] [SOURCE CONFLICT: A7 §§4.5/6.1 and B7 §3 allow ordinary bounded interpretation without separate permission.] \| Pending endpoint placement \| |
```

With:

```text
(row 116 removed) The marked line it copies, CH09-b:835, is replaced by F-CH09-b-00835 and carries no [SOURCE CONFLICT] mark after that fix, so Appendix D no longer lists it.
```

#### C-22 — Wellbeing & Behavioral Baseline (§22)

**F-CH12-d-00160** · CH12-d:160 · register row · `ready`

Place: Appendix D (source-conflict register) row 140, an exact copy of CH10-c:10; changed with F-CH10-c-00010 (job B5: appendix rows change with their card). The fixed line carries no [SOURCE CONFLICT] mark, so the row leaves the register.

- Rule: D-2026-10-15-03, "Ness's words, verbatim: "Q2 - a"" (OCT15:483).
- Also rests on: D-2026-10-29-03, Ness's wide reading: "רחבה 3." (NESS_ANSWERS_2026-10-29_v0_1.md:11).
- Source: `REPO/01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`:185, "(4) system remains advisory — cannot diagnose, prescribe, or act autonomously;".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: Unchanged and still open: the tier selection and transition logic and the thresholds (C-22.6.5, NOT DECIDED); the unlock is the appointment record (DD:184). "cannot diagnose, prescribe" goes too: Ness chose the wide reading on 2026-10-29 (D-2026-10-29-03). Nothing here designs a diagnosing or prescribing function. The creation gate stays: Ness's "CONFIRMED: create nh_baseline_engine.py", the dry-run protocol and the prerequisites other than (4), the advisory condition, which goes (DD:185). The wording of DD §3K and cursorrules §12D changes later by new versioned files, never in place (OCT15:492). How the baseline reads REALITY promotions once T6's steer-not-file model applies (V10:3184) is a design slot (OCT15:497-498). C-22.9.4 keeps its ID; its name becomes "Removed advisory boundary" (A-2026-10-29-3).

Replaces:

```text
| 140 | CH10-c:10 | Chapter 10-c — Group H: C-22 | [SOURCE CONFLICT] V10 §22 specifies tier-triggered REALITY promotion throttling and freezing. DD §3K and CR §12D require the system to remain advisory and not act autonomously. Both statements are preserved; this piece does not invent a reconciliation or an autonomous-action exception. [V10 §22] [DD §3K] [CR §12D] |
```

With:

```text
(row 140 removed) The marked line it copies, CH10-c:10, is replaced by F-CH10-c-00010 and carries no [SOURCE CONFLICT] mark after that fix, so Appendix D no longer lists it.
```

### CH12-e

#### Chapter header

**F-CH12-e-00012** · CH12-e:12 · citation keys · `ready`

- Rule: A-2026-10-29-3, "סבבה, אז תסדר את הבעיות. מאשר" (OUT/FIX/NESS_ANSWERS_2026-10-29_v0_1.md:38).
- Also rests on: Contract §4: every behavior line is cited in the exact format, and a citation key names the file it points at.
- Source: `OUT/FIX/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md`, "## 2. The decisions applied".
- Approved: A-2026-10-29-3: Ness, "סבבה, אז תסדר את הבעיות. מאשר" (NESS_ANSWERS_2026-10-29_v0_1.md:38-39).
- Stays open: The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet.

Replaces:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; DR = `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_2026-09-24_v0_1_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `05i/` = `05_INACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`; `[NHD-…]` tags are preserved source identifiers. Chapter codes and one-based line/cell locators refer to the exact files in the READ RECORD.
```

With:

```text
Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; DR = `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_2026-09-24_v0_1_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `05i/` = `05_INACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`; `[NHD-…]` tags are preserved source identifiers. Chapter codes and one-based line/cell locators refer to the exact files in the READ RECORD. Decision key `D-2026-10-15-02 T3`, added after the pinned commit, names Ness's decision quoted in `05_ACTIVE_CANDIDATE/NH_MASTER-21_BIG_RULES_FIXES_v0_1_CANDIDATE.md` §2.
```

#### P-NEW-capture — Non-chat capture → Catalog → root

**F-CH12-e-00672** · CH12-e:672 · table row · `ready`

Place: Appendix E copy of the CH11:2154 path-table row (CH12-e:660-688 copy the CH00 naming and path-table rows); changed with F-CH11-02154.

- Rule: D-2026-10-15-02 T3, "option A. Root first; the context-meaning stays a proposal beside it; Ness's" (OCT15:453).
- Source: `REPO/97_HISTORICAL_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`:2843, "Metadata → plain-description → context-meaning → Ness confirms.".
- Approved: A-2026-10-29: Ness, "מאשר את מה שעניתי" (NESS_ANSWERS_2026-10-29_v0_1.md:18).
- Stays open: The schema of a separate image confirmation or rejection event stays NOT DECIDED (STANDING T3). How the optional confirmation is surfaced (its notice form) is not designed. Unchanged: the meaning never becomes fact without Ness (C-9A.4 stays a prohibition), WhatsApp media stays frozen, live-camera help never stores automatically, in-world camera/VR keeps per-device approval (H1744).

Replaces:

```text
| CH11:2154 | \| P-NEW-capture \| Non-chat capture → Catalog → root \| NOT DECIDED \| DESIGNED — An eligible non-chat source supplies a capture through its own front door. An image follows its separate confirmation sequence; an already frozen import source is not silently reopened. [V10 §7E] [V10 §9A] [MAP C-INGEST] \| |
```

With:

```text
| CH11:2154 | \| P-NEW-capture \| Non-chat capture → Catalog → root \| NOT DECIDED \| DESIGNED — An eligible non-chat source supplies a capture through its own front door; an already frozen import source is not silently reopened. DECIDED-2026-10-15 — An image follows its proposal sequence and becomes a root without waiting for Ness's confirmation, which stays optional, surfaced and never asked. [D-2026-10-15-02 T3] [V10 §7E] [V10 §9A] [MAP C-INGEST] \| |
```

## 5. Open slots

Each entry's "Stays open" note is above. Gathered here, by decision, without repeats:

**A-2026-10-29-3**

- The card keeps its ID C-7B.8.4. The new name was chosen by the worker and not shown to Ness one by one; he can change it. (F-CH02-06449)
- The card keeps its ID C-DETECT.2.3. The new name was chosen by the worker and not shown to Ness one by one; he can change it. (F-CH03-p-00165)
- The card keeps its ID C-22.9.4. The new name was chosen by the worker and not shown to Ness one by one; he can change it. (F-CH10-c-00767)
- The file is in the job's output until Ness uploads it to `05_ACTIVE_CANDIDATE/`; until then the keys point at a file the repository does not have yet. (F-CH00-00011)

**D-01**

- The [SOURCE CONFLICT: V10 §2 says otherwise] marks on C-7B.8 Does and C-7B.8.1 (CH02:6430 and Appendix D, CH02:11339-11341) stay: V10 §2's text is unchanged, and D-01 decides that conflict for the live catalog. Whether the final build cites D-01 beside the mark is left open. Clear-evidence rule for speakers and conversations: open (OCT15:418). (F-CH02-06438)
- C-7B.8.4 keeps its ID; after D-01 it is the catalog boundary with no exception, and its name becomes "Live catalog boundary" (A-2026-10-29-3). Its TOGETHER boxes stay NOT DECIDED (Appendix A rows CH02:10812-10814 unchanged; nothing here fills them). Whether to write a clear-evidence rule for speakers and conversations like Bundle 3 A5 stays open (OCT15:418). C-DETECT.2.5's authorized resolution rule stays NOT DECIDED. (F-CH02-06524)
- C-DETECT.2.3 keeps its ID; after D-01 it records that no live question exists, and its name becomes "Live speaker hold" (A-2026-10-29-3). C-DETECT.2.4 still names its hold for "unattended material" (CH03-p:243 ff.); after D-01 live material with an unresolved speaker enters the same `speaker_unresolved` hold, and the final build may widen that card's wording to match. C-DETECT.2.5's authorized resolution rule stays NOT DECIDED (OCT15:398, :417), and so does the clear-evidence rule for speakers (OCT15:418). Ness may still confirm a speaker unasked (OCT15:400). (F-CH03-p-00143)
- C-7E.7 Fails closed by (CH04-a:718), C-7E.8.4 Fails closed by (CH04-a:838) and C-7E.8.4 What it is still say "unattended"; after D-01 live material with an unresolved speaker or grouping enters the same hold, and the final build may widen those words. C-7E.8.4's TOGETHER boxes stay NOT DECIDED (its Appendix A rows unchanged). C-DETECT.2.5's authorized resolution rule and a clear-evidence rule for speakers and conversations stay open (OCT15:418). (F-CH04-a-00049)

**D-02 T2**

- The successor version of thread_membership_v1 is NOT DESIGNED: which modes it assigns for a first reading, its inputs, its override cases and its fallbacks. This line waits for that design. Until it exists, the build blocker on the first reading stays (OCT15:451-452). Retrieval bounds and their values stay open (B1); values are tested later, and gold pass/fail stays Ness's (DD:90). The version-1 card C-7GA.10 and its sub-cards stay as the description of version 1 (see clash_no_change.jsonl). (F-CH00-00037)

**D-02 T3**

- The schema of a separate image confirmation or rejection event stays NOT DECIDED (STANDING T3). How the optional confirmation is surfaced (its notice form) is not designed. Unchanged: the meaning never becomes fact without Ness (C-9A.4 stays a prohibition), WhatsApp media stays frozen, live-camera help never stores automatically, in-world camera/VR keeps per-device approval (H1744). (F-CH04-e-00020)

**D-02 T4**

- Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. (F-CH08-a-00012)
- Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485). (F-CH08-a-00014)
- Operation 2 (recording what another person actually said or did) needs only the existing capture and third-party rules (A7:477-478): D-02 T4 did not cover it (OCT15:459-460), and Ness settled it on 2026-10-29 (D-2026-10-29-04). Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485). (F-CH08-a-12144)
- Unchanged: the universal third-party baseline applies to everyone, including minors and highly vulnerable people; Ness may set stricter person or group rules (the only path to different handling). The WhatsApp archive stays frozen, and its intake scope, including child-related material, waits for Ness's own decision (later patch 0007:78). The related "minor-data specific rules" slot is closed as rejected (A7:484-485). The [SOURCE CONFLICT: V10 §7Q prescribes stronger default restrictions ...] mark on C-9A.7.1.4 Does (CH04-e:427) stays visible (contract §1.5); D-02 T4 decides that conflict. (F-CH04-e-00425)

**D-03**

- Unchanged and still open: the tier selection and transition logic and the thresholds (C-22.6.5, NOT DECIDED); the unlock is the appointment record (DD:184). "cannot diagnose, prescribe" goes too: Ness chose the wide reading on 2026-10-29 (D-2026-10-29-03). Nothing here designs a diagnosing or prescribing function. The creation gate stays: Ness's "CONFIRMED: create nh_baseline_engine.py", the dry-run protocol and the prerequisites other than (4), the advisory condition, which goes (DD:185). The wording of DD §3K and cursorrules §12D changes later by new versioned files, never in place (OCT15:492). How the baseline reads REALITY promotions once T6's steer-not-file model applies (V10:3184) is a design slot (OCT15:497-498). C-22.9.4 keeps its ID; its name becomes "Removed advisory boundary" (A-2026-10-29-3). (F-CH10-c-00010)

**D-2026-10-29-03**

- Unchanged: the creation gate (Ness's "CONFIRMED: create nh_baseline_engine.py", the dry-run protocol and the other prerequisites, DD:185), no silent wellbeing writes, and the appointment-record unlock (DD:184). Nothing here designs a diagnosing or prescribing function. The wording of DD §3K and cursorrules §12D changes later by new versioned files, never in place (OCT15:492). C-22.9.4 keeps its ID; its name becomes "Removed advisory boundary" (A-2026-10-29-3); its Fed by and Gated by stay NOT DECIDED. (F-CH10-c-00839)

**D-2026-10-29-04**

- Unchanged: possibilities never become facts; the full simulation needs Ness's clear prior approval; no harm, illegal use or outside disclosure; Ness may set stricter person or group rules. C-7Q.5.3.2's Fed by and Changes stay NOT DECIDED (wiring). (F-CH08-a-01840)

## 6. Notes for the final build

- Line numbers. Where an entry turns one line into two or three, or removes an Appendix D row, the later lines of that chapter move. The final build moves every `CHxx:n` reference in the appendices to the new numbers; no entry does it by hand.
- Appendices. The final build regenerates Appendix A (the NOT DECIDED register) and Appendix E (citation coverage), and recounts Appendix D's checks, from the built chapters, with the book's own extraction rules. The job's `scripts/appendix_recount.py` restates those rules and reproduces Master-21's Appendices A, D and E exactly from Master-21's chapters. No entry fills a NOT DECIDED box, but some entries write a new NOT DECIDED (the successor rule version of thread_membership_v1 under T2); Appendix A then lists each one.
- The job's draft (`DRAFT_MASTER-21_WITH_FIXES/` in its output) is Master-21 with every entry applied and these build steps run.
- The 16 T1 entries were withdrawn on Ness's answer to Q1 (D-2026-10-29-01); those lines stay as Master-21 has them.
- DD §3K and cursorrules §12D still carry the advisory condition (DD:185; cursorrules:697). Under D-2026-10-29-03 they change by new versioned files, never in place (OCT15:492); that is outside this file.
- The gap-run answers are not in this file or in the book. They are proposals: ChatGPT's second review and Ness's approve-all lists come first (gap job v0_4 Part D), and only approved answers go into the gap file (D5; route v0_2 §2.4). The job's check of them against Ness's decisions is in `gap_answers.jsonl` and `waiting_gaps.jsonl`.
