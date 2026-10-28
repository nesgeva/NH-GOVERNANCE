# 98_HISTORICAL_SOURCES_PRE_V10 — historical archive (adopts nothing)

**Status:** HISTORICAL ARCHIVE. Non-authoritative. Everything in this folder predates the adoption of
`NH_MASTER-20_CORRECTED_v10.md` (adopted by Ness on 2026-06-29) and is superseded by it. Nothing here is
current, accepted, or adopted by being present. Folder placement creates no acceptance.

**Authority order is unchanged:** `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` →
`NH_DECISION_DEFAULTS-S19_v2_2.md` → `cursorrules` → `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`.
If anything in this folder disagrees with those files, those files win.

**Known stale statement inside the album:** `NH_COMPLETE_PROJECT_PRESERVATION_MASTER_v1.md` §2 says
`NH_MASTER-19_CORRECTED_v7_1.md` is the authoritative Master. That was true when the album was made and is
no longer true. Do not cite v7_1, or any older Master here, as current.

## What is in this folder

- `NH_COMPLETE_PROJECT_PRESERVATION_MASTER_v1.md` — "the album": the preservation master exactly as it was
  produced (5,195,926 bytes; SHA-256 `6f458f8b330a05fe6094afc7b39b117e52147f290be0d288245b7e07bff390b6`).
  It embeds 90 verbatim source bodies plus 2 binary metadata records, with provenance indexes (album §4–§9).
- `sources/` — the same 90 bodies unpacked into separate files, one per unique SHA-256, so each old Master,
  Decision Defaults version, design sketch, note, prototype and script can be opened, searched and cited on
  its own. Filenames are exactly the "Exact filename" recorded in the album (upload suffixes such as `__1_`
  kept on purpose, so every file matches the album's index). `INDEX.md` maps SOURCE ID → file → logical name.
- `INDEX.md` — generated table of every unpacked body with size, line count, SHA-256 and the status the album
  recorded for it. Data only.
- `sources_recovered/` — bodies recovered from Ness's PC after the album was made; exact original filenames kept.
  Sixty-plus files across three batches. Three from the first batch: the Batch-1 `NH_Meaning_Engine_Design.md` (SHA-256 `18185908…`, 137 lines) that the album §8 recorded
  as unrecoverable (matches the album's historical record exactly); `NH_ACCEPTED_PERSONAL_LEARNING_DESIGN_v1.md`
  (pre-V10 accepted standalone design whose SHA-256 Master V10 cites); and `NH_SESSION_REFERENCE_June29_2026.md`
  (session reference compiled against Master v7_1 on the day V10 was adopted). Eleven from the second batch: the
  2026-06-28 Final-Master Recovery stage set (Stage 1 → 2 → 3A → 3B → final no-loss check), which also records the exact
  SHA-256 of the three candidate files still missing (Master-19 v8, Decision Defaults v2_3, cursorrules v3_3). Third batch, from a whole-drive search: those three candidates themselves
  (fingerprint-verified), Masters 15/16/16_FINAL_CORRECTED/17_DRAFT/19_v2, Decision Defaults S17_DRAFT and S19_v2_1, the S17
  ChatGPT handoff, the interface-world design log, and the complete Master-20 lineage v1–v9 with every change/provenance and
  no-loss report. See INDEX.md.
- `NH_FEATURE_AND_DESIGN_PRESERVATION_MASTER_v1.md` — pre-V10 feature-and-design catalogue from the v7_1 era,
  supplied by Ness on 2026-09-24. Not in the album. Historical; adopts nothing.
- `NH_COMPLETE_PROJECT_ORIGINAL_FILES_ARCHIVE_v1.zip` — the album's companion ZIP of byte-exact originals (112 members, verified
  against the album's hashes), including the survey PDF and `files__3_.zip` that the album could only describe.
- `SHA256SUMS.txt` — SHA-256 of every file in this folder except itself (see the line count in the file).

## How it was produced

Unpacked mechanically by Claude on 2026-09-24 from the album above (the album was supplied by Ness as an
upload). Every unpacked body was written byte-for-byte from the text between the album's
`----- VERBATIM CONTENT BEGINS/ENDS -----` markers and verified against the SHA-256 and byte count the
album records for it: 90 of 90 verified, 0 mismatches. Nothing was edited, reformatted, renamed, merged, or
reconciled.

Cross-check against this repository at commit `9df2196`: 3 of the 90 bodies already existed byte-identical
(`NH_DECISION_DEFAULTS-S19_v2_2.md`, `cursorrules`, `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`);
the other 87 existed nowhere in the repository or its git history before this folder was added.

## What is NOT here

- Files the album lists as referenced-but-never-supplied (album §7), e.g. `NH_MASTER-12`, `-15`, `-16`,
  `-16_FINAL_CORRECTED`, `NH_MASTER-19_CORRECTED_v8`, `NH_DECISION_DEFAULTS-S19_v2_3`, `cursorrules_v3_3`.
  Most of these were found on 2026-09-24 and now sit in `sources_recovered/`; the ones still absent are listed at the end of
  INDEX.md. If any are found later, they are added here as new files, never by editing existing ones.

## Rules for this folder

- Never edit, rename, reformat, or delete anything here. Additions only, as new files, with `SHA256SUMS.txt`
  extended in the same commit.
- Cite files here as history: "pre-V10, SOURCE ID SRC-nnn, section …". Never as current design.
- A feature-recovery audit (which ideas from these sources are carried, compressed, dropped, or contradicted
  in Master V10 and the accepted packages) is a separate, later artifact. The album itself records (§13) that
  no such audit had been performed. This folder performs none.
