# NH_MASTER-21 — Cleanup round (round 5): PASSED record (v1, 2026-10-04)

**What this file is:** the proof that the cleanup round passed, in one place. It decides nothing; Ness adopts Master-21 later, after the join and the final check.

## 1. The passed version

`NH_MASTER-21_CLEANUP_FIXED_CHAPTERS_v7_2026-10-04.zip`, SHA-256 `3e9fe1c35e1691096e79c24886ce4463288941d27301533019c55fbe38bd37b5` — all 66 chapters, the v7 record and changed lines, and the appendix scripts. This is the set to join.

## 2. The three PASS results

| Part | Chapters | Passed on | Evidence | Why it holds for v7 |
|---|---|---|---|---|
| A | CH00–CH03-p (19) | v4 | re-check 4, Part A: PASS, findings `[]` (reply text; saving failed) | all 19 chapters byte-identical v4 → v7 |
| B | CH04-a–CH08-g (27) | v5 | re-check 5, Part B: REPORT `d0e933a9bc2e8a6c21d9738d67c462f9cabd26a11872180e54e78fcace3aad47`, FINDINGS `9960e8e30e60c2421f3fdf2b5131168de382511be8c3e4ad5a6933d80570a766` (3 notes, deferred to the join) | all 27 chapters byte-identical v5 → v7 |
| C | CH09-a–CH12-e (20) | v7 | re-check 6, Part C: REPORT `afbdbb725c516b39b7efc287b8fd4141de268280cbd2a5a66890cd29ea0236b8`, FINDINGS `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` (`[]`) | checked on v7 itself |

## 3. The road here

| Version | What it fixed |
|---|---|
| v1 | about 5,002 changes from the cleanup audit |
| v2 | the three first checks |
| v3 | the three v2 re-checks |
| v4 | the three v3 re-checks: counts, eight TOGETHER lines, review flags, one duplicate register row |
| v5 | five stale CH04-b inventory rows (Part B) |
| v6 | 377 register pointers, two review rows, one summary sentence (Part C) |
| v7 | the pointer rule applied to every review row, 46 rows (Part C) |

## 4. Decisions in force

- D1, D2, Q1 = A, Q3 = B, back-links = A (Ness, 2026-10-03)
- R1 = A (Ness, 2026-10-04)
- B (Ness, 2026-10-04): every per-chapter total is computed and filled in by script at the joining step; in the cleanup re-checks, wrong per-chapter totals are notes, not must-fix
- Final check after the join: a light one, minutes long (Ness, 2026-10-04): replay of the joined file against the 66 passed chapters, recount of the script-filled totals, link check.
- Order of work: the gap file (document 2) is completed and the final master generated before building resumes (Ness, 2026-10-04).

## 5. Carried to the joining step (decision B)

- The per-chapter totals and count summaries, filled in by script. This includes Part B's notes: CH04-c 484/77, the CH05-a and CH05-b "no plain gate remains" sentences, and the 36 historical counters without a selection rule.
- The joining tool v2 (`07_TOOLS/nh_master21_assemble.py`): fix the part-locator bug that skips card IDs with hyphens (C-ENGINE-AB, C-WIS-SEP and others), as a new version.

## 6. Next steps

1. Joining tool v2.
2. The join, with the totals filled in by script.
3. The light final check.
4. Ness adopts Master-21 and uploads to GitHub; V10 moves to history as new files.
5. Route note v0_5 and writer lessons v0_5.
6. Document 2, the gap file.

## 7. Claude's errors in this round, named

- **v3:** counted continuation coverage in either direction for the CH02 promise rows.
- **v3:** recounted only the counts the checkers had named, not every count.
- **v3:** counted a table header as a data row.
- **v4:** added two C-7H lines in a different order from the record (caught by the replay before delivery).
- **v5:** the Appendix A duplicate guard looked for the old cell number (caught before delivery).
- **v6:** stated the pointer rule for every row but applied it only to the outside-card pointers (caught by Part C; fixed in v7).
