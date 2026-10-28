# NH_MASTER-21 — Final re-check brief (assembler v3), v1, 2026-10-04

**Status:** brief for an independent re-check. It decides nothing. Ness alone decides adoption.

## 0. In plain words

The final check of the joined book (`NH_MASTER-21_FINAL_CHECK_REPORT_v1_2026-10-04.md`, verdict FAIL) found two tool problems and no chapter-content problems:

- **NH21-FINAL-002 (major):** the part locator's "described in" column showed section headings (8,375 rows said "READ RECORD") instead of each card's chapter.
- **NH21-FINAL-001 (minor):** CH12-b and CH12-e each lost one trailing blank line without it being reported.

Assembler v3 fixes both. It was written and tested by Claude in a sandbox: made-up chapters, deliberately broken copies, and 11 older real chapters from the repository. It was run on the real v8 chapters only on Ness's PC. Your v3 run in R1 is the second witness.

This re-check checks only what v3 changed. The chapters are the same v8 chapters you already checked.

## 1. Rules

1. Report only. Do not repair, rewrite or improve any file.
2. Use your own code for R3–R5. Do not import the assembler or reuse its functions.
3. If any input fingerprint does not match, stop at R0 and report.
4. Any difference not allowed by R2 or R3 is a finding.
5. Keep it light, as Ness decided for the final check on 2026-10-04. Do not repeat checks that R3 proves are unaffected (see "Carry-over").

## 2. Inputs (SHA-256 of the raw bytes)

| File | SHA-256 | Note |
|---|---|---|
| `nh_master21_assemble_v3.py` | `81195e8eb4c1a31d8af14216e36f2e896432c47296be65315c46d031d91d50bc` | 17,270 bytes, 387 lines |
| `NH_MASTER-21_CLEANUP_FIXED_CHAPTERS_v8_2026-10-04.zip` | `43957c01343121773ab5304a71471a2af84d8889eb3f9c33d568747eb4a40ef8` | the 66 chapters and their v8 record |
| `NH_MASTER-21_FINAL_CHECK_KIT_v1_2026-10-04.zip` | `6c810b49320af16b96fdfae354466002c4323c88bdebda0463fe266e3e80b957` | contains assembler v2, assembler v1, brief v1, the passed record |
| `nh_master21_assemble_v2.py` (inside the kit) | `de0b5feafb2ec8f5dbdce7ec4a200974276565560035c8951d65dda63a8a71c2` | |
| `NH_MASTER-21_FINAL_CHECK_BRIEF_v1_2026-10-04.md` (inside the kit) | `d387ad922f2843a460a0733b2fa1d447148cf46719355a4375a263493ee5c067` | holds the requirements quoted in R4 and R5 |
| `NH_MASTER-21_FINAL_CHECK_REPORT_v1_2026-10-04.md` | `4d23ab8f1459b5c8278d8a088c92bbe08cd837b728bb46e53d7cb21a9d70f0f7` | the previous verdict and both findings |

A local filename suffix such as `(1)` is an upload artifact; the bytes decide.

## 3. Results observed on Ness's PC (2026-10-04, 21:02 UTC)

The v3 run printed the following:
- Every report line YES: 66 bodies at their place with their line endings, 66 rebuild checks and 66 contract blocks. The exit code was not printed; R1 checks it.
- `PART LOCATOR CHECK`: 9,392 rows naming the chapter that holds the heading, and 0 rows not inside a chapter body.
- `RESULT: ALL SOURCE TEXT PRESENT VERBATIM`.
- `part locator rows: 9392`.
- All 66 source-chapter fingerprints equal the v8 record.

The v3 book is `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE.md`:
- SHA-256 `8d7c929c5715bb8138644f2a0a7513a89e4f98d98c6f0f05e068284f4cc5ed0d`
- 44,986,552 bytes
- 361,508 LF lines

The v2 book is unchanged since the final check: `24e9ccdb285a11186c76375196ec9806ecc05914f270dbcfca07dd425ed7a76a`.

Ness also compared the two books with a separate line-by-line script:
- 9,392 locator cells changed, all in one contiguous block;
- 2 blank lines added, one in CH12-b and one in CH12-e;
- no other difference;
- per-chapter locator row counts equal `affected_chapters` in the previous FINDINGS;
- the six examples in R4 map correctly.

## 4. Stages

**R0 — Fingerprints.**
- Verify every input in §2.
- Extract the v8 zip, then verify all 66 chapter files against the v8 record inside it.

**R1 — Reproduce both books.**
- Run `python3 nh_master21_assemble_v2.py <v8 chapters dir> <empty dir A>` and `python3 nh_master21_assemble_v3.py <v8 chapters dir> <empty dir B>`.
- v2 must give `24e9ccdb…d7a76a`.
- v3 must give the book and report results in §3: fingerprint, bytes, lines, 0 CR bytes, exit code, report lines.

**R2 — Tool diff, v2 → v3.** Review the complete textual diff. Only these 16 hunks are allowed (`diff` positions, v2 → v3):

| Hunks | Allowed content |
|---|---|
| `3c3`, `6a7,23`, `29c46` | Docstring: version line; a new "Changes from version 2" paragraph naming both findings; usage line. v2's "Changes from version 1" text stays unchanged. |
| `152a170` | Report line `assembler: nh_master21_assemble_v3.py (version 3)`. |
| `179,180c197,203`, `184c207,208` | NH21-FINAL-001: the trailing-blank trim (`while body and body[-1].strip() == '': body.pop()`) is removed. A rebuild check is added: body + moved block + reported removals put back at their line numbers must equal the source file's bytes. The result is stored as `rebuild_ok`. |
| `217a242`, `219c244,246` | Join loop: each body's output line range is recorded. The blank line before the `---` separator is added only when the body is empty or its last line is not blank. Markdown needs that blank line, and bodies ending in one blank line join byte-identically to v2. |
| `268c295,303`, `271d305`, `272a307`, `275,276d309`, `284c317,321` | NH21-FINAL-002: the locator's "described in" value comes from the recorded body ranges (the chapter's `# ` title line without `# `). The `current` / `## `-heading tracking is removed. A part heading outside every chapter body is listed as `(not inside a chapter body)` and fails the run. |
| `308,309c345,347`, `311,312c349,353`, `318a360,366` | Integrity proof: each body is checked with its line endings, both as text and at its exact place in the output. The rebuild result is reported. A `PART LOCATOR CHECK` block is added. The overall result fails if any rebuild check fails or any locator heading is outside a chapter body. |

**R3 — Book diff, v2 book → v3 book.** Compare line by line. Only two kinds of difference are allowed:
- Exactly 9,392 locator rows (`| part ID | described in | heading |`) whose first and third cells are unchanged and whose middle cell changed.
- Exactly two inserted blank lines: one at the end of CH12-b's body and one at the end of CH12-e's body, each immediately before that chapter's generated `---` separator.

Everything else must be byte-identical: front matter, source pins, contents, every chapter body, the appendix, the B2 notes, the moved blocks and the current-totals tables. Report the first and last locator-row line numbers and the line numbers of the two inserted blank lines.

**R4 — Closure of NH21-FINAL-002.** Brief v1's requirement: "The locator lists each of the 9,392 card IDs once, with its chapter."
- With your own code, find for each card ID the chapter file containing its `### C-<id> — <title>` heading.
- For all 9,392 rows, the "described in" cell must equal that chapter's title (line 1 of the chapter file, without `# `). List every mismatch.
- Re-check the six examples from the previous report: C-STORE → CH03-a, C-ENGINE-AB → CH03-i, C-7G → CH05-a, C-WIS-SEP → CH09-a, C-16 → CH10-b, C-7GA.15 → CH11.

**R5 — Closure of NH21-FINAL-001.** Brief v1's requirement: "Only listed header-zone metadata lines may be removed; each chapter body must appear verbatim." Repeat the previous Stage 3 on the v3 book:
- All 66 chapter bodies are present verbatim, including their trailing blank lines (CH12-b: 2, CH12-e: 2, the other 64: 1).
- Only the 264 listed metadata lines are removed.
- All 66 CONTRACT CHECK blocks are verbatim.
- There is no unclassified added content.

**Carry-over (no recount).** If R3 passes, every line other than the 9,392 locator rows and the two blank lines is byte-identical to the v2 book that passed the previous Stages 4 and 5. Those results therefore carry over without a recount: 726 totals, B2 notes, totals tables, source pins and 718 contents entries. State this in the report. If R3 fails, report and stop.

## 5. Verdict and delivery

- **PASS** only if R0–R5 all pass.
- Deliver two files:
  - `NH_MASTER-21_FINAL_RECHECK_REPORT_v1_2026-10-04.md`: verdict, each stage's result, the commands used, evidence.
  - `NH_MASTER-21_FINAL_RECHECK_FINDINGS_v1_2026-10-04.json`: verdict, stage results, findings with exact locations; an empty findings list if there are none.
- Number any findings NH21-RECHECK-001, -002, and so on.
- Make no fixes.
