# NH_MASTER-21 — Final check after the join: brief (v1, 2026-10-04)

You are an independent checker. Claude was the fixer and wrote the joining tool. You verify and report; you do not fix. Ness owns every decision. This is the light final check Ness chose: minutes, not a full audit. The 66 chapters already passed the cleanup round (record `NH_MASTER-21_CLEANUP_ROUND_PASSED_RECORD_v1_2026-10-04.md`).

## 1. What is being checked

1. **v8.** v8 is the passed v7 plus two wording fixes (CH05-a and CH05-b) and refreshed appendix fingerprints. The two sentences sat outside the CONTRACT CHECK blocks, so the join could not label them; a wording fix goes back into its chapter.
2. **Assembler v2** (`nh_master21_assemble_v2.py`, SHA-256 `de0b5feafb2ec8f5dbdce7ec4a200974276565560035c8951d65dda63a8a71c2`). It is version 1 (`07_TOOLS/nh_master21_assemble.py`, SHA-256 `a7c4049204272eba11392cf632a093805440f51d61fe03610fe9ec5e14cfed9b`, in the kit) with three stated changes:
   - The part locator accepts hyphens and lower-case letters in IDs.
   - Ness's decision B2: each moved CONTRACT CHECK block keeps its text word for word, is preceded by a GENERATED note that its counts are the writer's counts at writing time, and is followed by a GENERATED table of current totals with each total's counting rule.
   - Plain newline line endings on every system.
3. **The joined file it produces from v8:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE.md`, 44,770,908 bytes, 361,506 lines, SHA-256 `24e9ccdb285a11186c76375196ec9806ecc05914f270dbcfca07dd425ed7a76a`, 9,392 part-locator rows.

## 2. Inputs

- `NH_MASTER-21_CLEANUP_FIXED_CHAPTERS_v8_2026-10-04.zip`, SHA-256 `43957c01343121773ab5304a71471a2af84d8889eb3f9c33d568747eb4a40ef8`, including `NH_MASTER-21_CLEANUP_RECORD_v8_2026-10-04.json`.
- The before set: `NH_MASTER-21_CLEANUP_FIXED_CHAPTERS_v7_2026-10-04.zip`, SHA-256 `3e9fe1c35e1691096e79c24886ce4463288941d27301533019c55fbe38bd37b5`.
- The kit: this brief, assembler v1 and v2, the passed record.

| Chapter changed by v8 | v7 SHA-256 | v8 SHA-256 |
|---|---|---|
| CH05-a | `e166db889442419d771cbe5c2dd5fe054755a2d8cb151d52e9ef5f81b5218c36` | `8727c0611054eedc59bd56fa655e503267052cc34939c7f471cf954e73430797` |
| CH05-b | `2b3cfb5c50a4af1b923fedddbe34a51aabdfa6479a1dbd92b1106da153ce92a5` | `6a533174a3569b06d38652be23ad11abd418595a5c89743bb84b5acba75fe673` |
| CH12-a | `6e8eaf8816673cb007bc36b82045a6e33a86e0e94d6548d2cf69c77482ec619f` | `98d9028f5040c6f730bb983efd5f856bf02817fdd5132fb7dc8aa4cd45c6be80` |
| CH12-b | `5b2181e411417b531ad81f3db1f5d98861bdbe27c2839c0da5f134bde0677bd2` | `b7661a928436bbf37b410692c8726e8595b314fabb48e7f12484f0e611f21d7e` |
| CH12-c | `640043e45771a9211035eacfad5d9a11669e10fbef48d6f3ddf37b5c4dc92df5` | `748cc70adc8595eb6400eb433729d9a605e8f32d4e64a0fe2de1fe8d5852c8fd` |
| CH12-d | `6eda8e8c44be0bb2d6e6cd0bda66a0e064190f6d8085bfc175341d242aa3340e` | `d19cc5a79d6c7c25272d1063954dbd8e16f082fcc61d5cbe3ee17224b20fef47` |
| CH12-e | `8b8c4e523582d4a2703e3d37fb35e808a9c38d929c38fb3c13260f9bbf88e6d5` | `74fe84ed14c945c2a49291ad6ac8e7b0468a38c22964b981d44c702cc847d896` |

## 3. Stages

**Stage 0 — fingerprints.** Check the inputs and the table above.

**Stage 1 — v8.** Applying the v8 record items to v7 reproduces v8. Each of the two new sentences is true: CH05-a and CH05-b each have exactly one populated plain TOGETHER line, the one named.

**Stage 2 — the join reproduces.** Run `python3 nh_master21_assemble_v2.py <v8 chapters dir> <out dir>`.
- The joined file's SHA-256 is `24e9ccdb…` as above.
- The report says `RESULT: ALL SOURCE TEXT PRESENT VERBATIM` and `part locator rows: 9392`.

**Stage 3 — nothing lost or altered, checked with your own code.**
- Every chapter's text after the removed metadata lines, and every CONTRACT CHECK block, appears verbatim in the joined file.
- The only removed lines are the listed header-zone metadata lines.
- The only added lines are GENERATED parts: the front matter, contents, locator, B2 notes and totals tables, and separators.

**Stage 4 — the generated totals.** For every chapter, recount the eleven totals by the counting rules printed in its table, with your own code. Every count matches.

**Stage 5 — the generated parts and the tool.**
- The locator lists each of the 9,392 card IDs once, with its chapter.
- The B2 note precedes every moved block.
- The diff from assembler v1 to v2 contains only the three stated changes.

## 4. Output

Save, as downloadable files whose names start with `NH_MASTER-21_FINAL_CHECK_`: a REPORT (verdict PASS or FAIL, each stage's result, every finding) and a FINDINGS.json. If saving fails, write the full findings in your reply as one JSON code block.
