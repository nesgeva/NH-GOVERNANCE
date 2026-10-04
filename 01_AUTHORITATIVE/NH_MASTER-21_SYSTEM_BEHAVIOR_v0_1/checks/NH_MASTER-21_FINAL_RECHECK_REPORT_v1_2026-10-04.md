# NH_MASTER-21 — Final re-check, assembler v3

**Verdict: PASS. R0–R5 all pass. Findings: none (`[]`).**

Both prior findings are closed: NH21-FINAL-002 (locator chapter mapping) and NH21-FINAL-001 (two trailing blank lines). This is the scoped re-check requested in `NH_MASTER-21_FINAL_RECHECK_BRIEF_v1_2026-10-04.md`. No supplied chapters, assemblers, or joined books were repaired, rewritten or improved. Ness alone decides adoption.

| Stage | Result | Evidence |
|---|---|---|
| R0 | **PASS** | All six listed input fingerprints and all 66 chapter fingerprints match. |
| R1 | **PASS** | Both books reproduced with their expected fingerprints, sizes and LF counts; both runs exit 0. Every required v3 report check passes. |
| R2 | **PASS** | The complete textual diff contains exactly the 16 allowed hunks, with only their allowed content. |
| R3 | **PASS** | Exactly 9,392 locator middle cells change, plus the two permitted blank-line insertions. No other byte difference. |
| R4 | **PASS** | All 9,392 unique locator IDs have the exact title of their containing chapter; zero mismatches. All six examples pass. |
| R5 | **PASS** | All 66 bodies, including boundary blanks, and all 66 moved blocks are verbatim; only the 264 listed metadata lines are removed. No unclassified additions. |

**R0 — fingerprints**

| Input | Verified SHA-256 |
|---|---|
| `nh_master21_assemble_v3.py` | `81195e8eb4c1a31d8af14216e36f2e896432c47296be65315c46d031d91d50bc` |
| `NH_MASTER-21_CLEANUP_FIXED_CHAPTERS_v8_2026-10-04(1).zip` | `43957c01343121773ab5304a71471a2af84d8889eb3f9c33d568747eb4a40ef8` |
| `NH_MASTER-21_FINAL_CHECK_KIT_v1_2026-10-04(1).zip` | `6c810b49320af16b96fdfae354466002c4323c88bdebda0463fe266e3e80b957` |
| `NH_MASTER-21_FINAL_CHECK_REPORT_v1_2026-10-04 (1).md` | `4d23ab8f1459b5c8278d8a088c92bbe08cd837b728bb46e53d7cb21a9d70f0f7` |
| `nh_master21_assemble_v2.py` | `de0b5feafb2ec8f5dbdce7ec4a200974276565560035c8951d65dda63a8a71c2` |
| `NH_MASTER-21_FINAL_CHECK_BRIEF_v1_2026-10-04.md` | `d387ad922f2843a460a0733b2fa1d447148cf46719355a4375a263493ee5c067` |

Filename suffixes `(1)` are upload artifacts. Raw bytes determine identity. Assembler v3 is 17,270 bytes and 387 LF lines. The extracted v8 archive contains exactly 66 chapter files, and every chapter SHA-256 equals its v8-record entry. The JSON contains all 66 comparisons. R0 passed before either assembler was run.

**R1 — both fresh joins**

Both output directories were newly created and empty. Commands executed:

```bash
python3 /workspace/scratch/e5a3e6c38c97/recheck_work/kit/nh_master21_assemble_v2.py /workspace/scratch/e5a3e6c38c97/recheck_work/v8 /workspace/scratch/e5a3e6c38c97/recheck_work/v2_run
python3 /workspace/scratch/e5a3e6c38c97/upload/nh_master21_assemble_v3.py /workspace/scratch/e5a3e6c38c97/recheck_work/v8 /workspace/scratch/e5a3e6c38c97/recheck_work/v3_run
```

| Output property | v2 | v3 |
|---|---|---|
| SHA-256 | `24e9ccdb285a11186c76375196ec9806ecc05914f270dbcfca07dd425ed7a76a` | `8d7c929c5715bb8138644f2a0a7513a89e4f98d98c6f0f05e068284f4cc5ed0d` |
| Bytes | `44770908` | `44986552` |
| LF lines | `361506` | `361508` |
| CR bytes | `0` | `0` |
| Exit code | `0` | `0` |

Both runs report `RESULT: ALL SOURCE TEXT PRESENT VERBATIM` and `part locator rows: 9392`; stderr is empty. All 66 source-chapter fingerprints in each report equal the v8 record. The v3 report additionally contains:

- 66 YES lines for bodies with their line endings at their recorded places.
- 66 YES lines for rebuilding the original source bytes.
- 66 YES lines for verbatim moved CONTRACT CHECK blocks.
- `rows naming the chapter that holds the heading: 9392`.
- `rows whose heading is not inside a chapter body: 0`.
- The required assembler-v3 version line and no NO result lines.

The v3 fingerprint, size, LF count and report results independently reproduce Ness’s PC observations.

**R2 — complete tool diff**

Reviewed the complete normal-format textual diff from this command:

```bash
diff recheck_work/kit/nh_master21_assemble_v2.py upload/nh_master21_assemble_v3.py
```

| Allowed hunks, v2 → v3 | Observed content |
|---|---|
| `3c3`, `6a7,23`, `29c46` | Version, v2 change history and usage documentation; v1 change history is unchanged. |
| `152a170` | Assembler-v3 report identification. |
| `179,180c197,203`, `184c207,208` | Remove trailing-blank trimming; add and store the source rebuild check. |
| `217a242`, `219c244,246` | Record body ranges; add a separator blank only when the body does not already end in one. |
| `268c295,303`, `271d305`, `272a307`, `275,276d309`, `284c317,321` | Assign locator chapter titles from body ranges; remove H2 tracking; record out-of-body headings. |
| `308,309c345,347`, `311,312c349,353`, `318a360,366` | Strengthen body/rebuild proof and add the locator check and failure conditions. |

Exactly these 16 hunks occur. No unrelated difference was found. The full diff is included in the JSON evidence.

**R3 — complete book comparison**

Compared raw byte lines, preserving their line endings. All locator first and third cells are unchanged; every middle cell changes. There are exactly two inserted blank lines and no other difference.

| Locator row range, one-based and inclusive | First | Last | Rows |
|---|---:|---:|---:|
| v2 and v3 books | 803 | 10194 | 9,392 |

| Chapter | v2 separator line | Inserted blank line in v3 | v3 separator line |
|---|---:|---:|---:|
| CH12-b | 355461 | 355461 | 355462 |
| CH12-e | 356746 | 356747 | 356748 |

Restoring the old locator rows and removing only those two blank lines reproduces the complete v2 byte sequence exactly, with SHA-256 `24e9ccdb285a11186c76375196ec9806ecc05914f270dbcfca07dd425ed7a76a`. Thus front matter, source pins, contents, all other chapter bytes, the appendix, B2 notes, moved blocks and totals tables are byte-identical. R3 passes, so the stop condition does not apply.

**R4 — NH21-FINAL-002 closed**

Independent code built a registry from each source file’s literal `### C-<id> — <title>` headings and line-1 chapter title. All 9,392 IDs are unique and appear once in the locator. All 9,392 “described in” cells equal the exact owning chapter title with `# ` removed. There are no missing IDs, extra IDs, duplicate IDs, chapter mismatches or heading mismatches.

| Card | Correct chapter | Source heading line | Joined locator line | Exact “described in” value |
|---|---|---:|---:|---|
| C-STORE | CH03-a | 17 | 1261 | Chapter 3-a — Group A: C-STORE |
| C-ENGINE-AB | CH03-i | 14 | 3286 | Chapter 3-i — Group A: C-ENGINE-AB |
| C-7G | CH05-a | 14 | 4286 | Chapter 5-a — Group C: C-7G |
| C-WIS-SEP | CH09-a | 16 | 7440 | Chapter 9-a — Group G: C-WIS-SEP |
| C-16 | CH10-b | 36 | 8762 | Chapter 10-b — Group H: C-16 |
| C-7GA.15 | CH11 | 486 | 10128 | Chapter 11 — The side paths |

Every one of the six required examples passes. All per-chapter locator row counts are recorded in the JSON.

**R5 — NH21-FINAL-001 closed**

Independent code retained original source line endings and removed only the explicit metadata whitelist within the first twelve lines. It then checked full bodies sequentially at their actual output positions, verified the generated separators, reconstructed source bytes by reinserting the listed metadata, and checked every complete moved block inside its corresponding appendix section.

| Check | Result |
|---|---|
| Complete bodies, including trailing blanks, verbatim at their exact output positions | 66 / 66 |
| Independent source rebuilds equal original bytes | 66 / 66 |
| Complete CONTRACT CHECK blocks verbatim | 66 / 66 |
| Listed whitelist metadata lines removed | 264, matching the report exactly |
| Other source removals | 0 |
| CH12-b trailing blank lines retained | 2 |
| CH12-e trailing blank lines retained | 2 |
| Other 64 chapters’ trailing blank lines retained | 1 each |
| Unclassified added content | 0 |

All bodies and their separators are accounted for in order. R3 proves the remaining generated material is unchanged from the previously classified v2 output, except the verified locator cells. The entire appendix is also byte-identical to v2. Per-chapter source/output locations, byte counts, contract hashes and all 264 metadata removals are included in the JSON.

**Carry-over — no recount**

Because R3 passes and the freshly reproduced v2 fingerprint equals the previously checked book, the unaffected results carry over: **726 totals, 66 B2 notes, 66 totals tables, 66 source-pin rows and 718 contents entries**. These were not recounted. The carry-over is grounded in byte equality and the fingerprint-verified previous report; it does not treat the previous overall Stage 5 FAIL as a PASS. The locator requirement was re-checked separately in R4.

**Independent-check method and delivery**

R3–R5 used separate checker code; no assembler module was imported and no assembler function was reused. Checker command:

```bash
python3 recheck_work/independent_recheck.py
```

Checker SHA-256: `f421091e0d4cc7edc510ce136cee89c11720cbe055676e0c7882ffbf6407b431`.

New findings: **none**. Both previous findings are closed for this v3 output. No fixes were made.

- `NH_MASTER-21_FINAL_RECHECK_REPORT_v1_2026-10-04.md`
- `NH_MASTER-21_FINAL_RECHECK_FINDINGS_v1_2026-10-04.json`
