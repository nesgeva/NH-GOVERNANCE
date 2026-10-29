# NH_MASTER-21 — Final check after the join

**Verdict: FAIL.** All stages 0–5 completed. Two findings: one major locator defect and one minor whitespace-preservation defect. The independently generated join matches Ness’s exact fingerprint. No chapter or assembler was modified.

Checked on 2026-10-04 against `NH_MASTER-21_FINAL_CHECK_BRIEF_v1_2026-10-04.md`. This is the requested light final check of the supplied files, not a renewed audit of the underlying source repository. Ness retains all adoption and remediation decisions.

| Stage | Result | Evidence |
|---|---|---|
| 0 | **PASS** | all three archives, both assemblers, seven brief hash pairs, and all 66 record hash pairs match. |
| 1 | **PASS** | all seven record items replay to all 66 v8 chapters; both new plain-gate statements are true. |
| 2 | **PASS** | fresh assembler v2 run matches the exact joined SHA-256, byte count, line count and locator row count. |
| 3 | **FAIL** | all nonblank body text and all moved blocks survive; two additional blank lines are removed without being reported. |
| 4 | **PASS** | 726 of 726 independently recounted totals match (66 chapters × 11 totals). |
| 5 | **FAIL** | locator IDs/titles are complete and unique, but chapter mapping is defective. B2 notes, pins, contents, and the three-change tool diff pass. |

**Stage 0 — fingerprints: PASS**

| Input | Verified SHA-256 |
|---|---|
| `NH_MASTER-21_CLEANUP_FIXED_CHAPTERS_v7_2026-10-04(1).zip` | `3e9fe1c35e1691096e79c24886ce4463288941d27301533019c55fbe38bd37b5` |
| `NH_MASTER-21_CLEANUP_FIXED_CHAPTERS_v8_2026-10-04.zip` | `43957c01343121773ab5304a71471a2af84d8889eb3f9c33d568747eb4a40ef8` |
| `NH_MASTER-21_FINAL_CHECK_KIT_v1_2026-10-04.zip` | `6c810b49320af16b96fdfae354466002c4323c88bdebda0463fe266e3e80b957` |
| `nh_master21_assemble.py` | `a7c4049204272eba11392cf632a093805440f51d61fe03610fe9ec5e14cfed9b` |
| `nh_master21_assemble_v2.py` | `de0b5feafb2ec8f5dbdce7ec4a200974276565560035c8951d65dda63a8a71c2` |

The v7 attachment’s local filename has the suffix `(1)`; its bytes match the expected v7 archive. Both sets contain exactly the same 66 chapter filenames. All 66 v7/v8 hash pairs in the v8 record match. The seven changed chapter pairs also match the brief:

| Chapter | Verified v7 SHA-256 | Verified v8 SHA-256 |
|---|---|---|
| CH05-a | `e166db889442419d771cbe5c2dd5fe054755a2d8cb151d52e9ef5f81b5218c36` | `8727c0611054eedc59bd56fa655e503267052cc34939c7f471cf954e73430797` |
| CH05-b | `2b3cfb5c50a4af1b923fedddbe34a51aabdfa6479a1dbd92b1106da153ce92a5` | `6a533174a3569b06d38652be23ad11abd418595a5c89743bb84b5acba75fe673` |
| CH12-a | `6e8eaf8816673cb007bc36b82045a6e33a86e0e94d6548d2cf69c77482ec619f` | `98d9028f5040c6f730bb983efd5f856bf02817fdd5132fb7dc8aa4cd45c6be80` |
| CH12-b | `5b2181e411417b531ad81f3db1f5d98861bdbe27c2839c0da5f134bde0677bd2` | `b7661a928436bbf37b410692c8726e8595b314fabb48e7f12484f0e611f21d7e` |
| CH12-c | `640043e45771a9211035eacfad5d9a11669e10fbef48d6f3ddf37b5c4dc92df5` | `748cc70adc8595eb6400eb433729d9a605e8f32d4e64a0fe2de1fe8d5852c8fd` |
| CH12-d | `6eda8e8c44be0bb2d6e6cd0bda66a0e064190f6d8085bfc175341d242aa3340e` | `d19cc5a79d6c7c25272d1063954dbd8e16f082fcc61d5cbe3ee17224b20fef47` |
| CH12-e | `8b8c4e523582d4a2703e3d37fb35e808a9c38d929c38fb3c13260f9bbf88e6d5` | `74fe84ed14c945c2a49291ad6ac8e7b0468a38c22964b981d44c702cc847d896` |

**Stage 1 — v8 replay and the two sentences: PASS**

Replayed R5-10488 and R5-10489 at their specified v7 line numbers after checking the exact before text. For R5-10490–R5-10494, refreshed only the two CH05-a/CH05-b fingerprints in each appendix, as the record specifies. Each old fingerprint occurs once in each appendix. The resulting bytes match all 66 v8 chapters: two wording changes, five appendix fingerprint refreshes, and 59 unchanged chapters. No replay files replaced the supplied sources.

| Chapter | Revised statement line | Sole populated plain TOGETHER line | Source line |
|---|---:|---|---:|
| CH05-a | 6776 | C-7G.7 — Gated by | 517 |
| CH05-b | 4921 | C-7GA.3.1 — Gated by | 165 |

CH05-a’s gate requires Ness’s explicit confirmation or later words/actions demonstrating adoption; provisional capture needs neither. CH05-b’s gate requires Ness deliberately enabling the queue before activation. The revised summaries accurately describe these lines.

**Stage 2 — reproduced join: PASS**

Ran the supplied, fingerprint-verified assembler v2 locally on the extracted v8 chapter directory. Process exit code: 0.

```text
python3 nh_master21_assemble_v2.py <v8 chapters dir> <out dir>
```

| Joined output property | Independently observed |
|---|---|
| Filename | `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE.md` |
| SHA-256 | `24e9ccdb285a11186c76375196ec9806ecc05914f270dbcfca07dd425ed7a76a` |
| Bytes | 44,770,908 |
| LF line endings | 361,506 |
| CR bytes | 0 |
| Locator rows | 9,392 |

The assembler report contains `RESULT: ALL SOURCE TEXT PRESENT VERBATIM` and `part locator rows: 9392`. The separate Stage 3 check below tests the original source text, including whitespace, rather than accepting that claim as proof.

**Stage 3 — preservation and generated additions: FAIL**

The independent checker matches all 66 chapter bodies in order, checks the 264 permitted metadata removals against the assembler’s removal list, and checks all 66 moved CONTRACT CHECK blocks byte for byte. All nonblank body text and internal whitespace survive. 64 complete bodies, including their trailing blank lines, survive verbatim; two lose one trailing blank line each (NH21-FINAL-001).

Output additions are confined to the generated front matter, 66 source-pin rows, 718 contents entries, 9,392 locator rows, chapter separators, the contract appendix heading/introduction and wrappers, 66 B2 notes, and 66 totals tables. No unclassified added prose was found.

**Stage 4 — generated totals: PASS**

All **726 comparisons match**. A separate checker built its own card registry and parsed Markdown card sections, field labels, USED BY table cells, named endpoints, citations and conflict markers; it did not import the assembler or use its parsing/counting functions. Counts exclude moved writer checks, as each generated table states. Every table carries the same eleven printed counting rules.

| Total | Independent counting basis |
|---|---|
| `cards` | headings of the form "### C-<id> — <title>" |
| `field_lines` | box lines ("- What it is:" to "- Changes:") inside cards |
| `populated_field_lines` | field lines whose value is not exactly NOT DECIDED |
| `not_decided_field_lines` | field lines whose value is exactly NOT DECIDED |
| `used_by_rows` | numbered rows ("\| n · STAMP \|") under a card's USED BY header |
| `together_lines_naming_a_card` | populated Fed by / Gated by / Changes lines naming at least one card |
| `plain_together_lines` | populated Fed by / Gated by / Changes lines naming no card |
| `named_together_endpoints` | card names in Fed by / Gated by / Changes lines (a name is a card ID followed by " — " and that card's exact title) |
| `cross_chapter_endpoints` | named endpoints whose card is defined in another chapter |
| `distinct_citations` | distinct bracketed source citations ([V10 ...], [MAP ...], [04/...] and the other source forms) in the chapter text |
| `source_conflict_lines` | lines carrying a [SOURCE CONFLICT marker |

Per-chapter values, all table locations and the empty mismatch list are included in the companion FINDINGS JSON. The card recount totals 9,392 unique cards.

**Stage 5 — generated navigation, B2, and tool diff: FAIL**

All 9,392 card IDs appear exactly once in the locator, with exact source card titles. There are no missing IDs, extra IDs, duplicates, or truncated hyphenated IDs. However, the “described in” cells do not identify the chapters (NH21-FINAL-002).

All 66 moved blocks have the required B2 note immediately before them and an eleven-row GENERATED totals table afterward. All 66 source pins and all 718 contents entries agree with the source/output headings.

Reviewed the complete v1 → v2 textual diff. It contains only the three stated changes and their version/usage documentation: expanded locator ID grammar; B2 counting code, notes and current-total tables; explicit LF writing for the joined output and assembly report. The trimming and chapter-mapping defects are inherited from v1, not additional v2 changes.

**NH21-FINAL-002 — Major — Stage 5: locator omits the cards’ chapters**

Requirement: “The locator lists each of the 9,392 card IDs once, with its chapter.” The ID/title portion passes, but the location column records an H2 section heading. H1 chapter headings never set or reset the locator’s current location. Thus 8,375 rows inherit “READ RECORD” from a previous chapter. The remaining rows identify sections without the containing chapter.

| “described in” value | Rows | Interpretation |
|---|---:|---|
| READ RECORD | 8,375 | Stale heading from a preceding chapter |
| 1.1 C-2 and its sub-parts | 51 | Local section in CH01 |
| Chapter 0 §0.4 naming-table continuation | 899 | Local section in CH10-b; not Chapter 0’s card location |
| B12 owner continuation | 67 | Local section in CH11 |

| Card | Joined locator line | Actual “described in” | Correct chapter | Source heading line |
|---|---:|---|---|---:|
| C-STORE | 1261 | READ RECORD | CH03-a | 17 |
| C-ENGINE-AB | 3286 | READ RECORD | CH03-i | 14 |
| C-7G | 4286 | READ RECORD | CH05-a | 14 |
| C-WIS-SEP | 7440 | READ RECORD | CH09-a | 16 |
| C-16 | 8762 | Chapter 0 §0.4 naming-table continuation | CH10-b | 36 |
| C-7GA.15 | 10128 | B12 owner continuation | CH11 | 486 |

Cause: `nh_master21_assemble_v2.py`, lines 271–284, especially 275–276, tracks only `##` headings and writes that value into the locator. This fails the chapter-location requirement even though the row count and fingerprint match. Reported only; no fix made.

**NH21-FINAL-001 — Minor — Stage 3: two unlisted blank-line removals**

Requirement: only listed header-zone metadata lines may be removed, and chapter text must appear verbatim. Two bodies have two blank lines before the original CONTRACT CHECK heading; the join retains only one blank line before its generated separator.

| Chapter | Original blank source lines | Original CONTRACT CHECK heading | Joined separator line | Net blank lines lost |
|---|---|---:|---:|---:|
| CH12-b | 160–161 | 162 | 355461 | 1 |
| CH12-e | 810–811 | 812 | 356746 | 1 |

The last body content line originally ends with three LF bytes (its terminator plus two blank lines). The joined body ends with two LF bytes before `---`. This is a whitespace-only loss; no nonblank source text or contract-block text is lost.

Cause: `nh_master21_assemble_v2.py`, lines 179–180, removes trailing blank body lines. The output then supplies a single blank line before the separator. The assembler’s integrity proof searches for the already-trimmed body, so it cannot detect this difference. These two removals are absent from its metadata-removal report. Under the brief’s strict verbatim/only-metadata rule, Stage 3 fails. Reported only; no fix made.

**Delivery and evidence**

- `NH_MASTER-21_FINAL_CHECK_REPORT_v1_2026-10-04.md` — this report, every stage result, and both findings.
- `NH_MASTER-21_FINAL_CHECK_FINDINGS_v1_2026-10-04.json` — structured verdict, both findings with locations and causes, all input/chapter hashes, replay results, preservation checks, all 726 per-chapter totals, generated-navigation checks, and the complete classified assembler diff.

All stages completed without a clarification stop. No source chapters, supplied scripts, or joined output were repaired.
