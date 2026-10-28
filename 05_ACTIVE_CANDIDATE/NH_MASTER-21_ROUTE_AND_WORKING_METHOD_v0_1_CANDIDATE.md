# NH_MASTER-21_ROUTE_AND_WORKING_METHOD_v0_1_CANDIDATE.md

**What this file is.** A plain record of the route Ness chose for the next Master: which three documents come next, in what order, what "done" means for each, and how the work is run and checked. It is for any ChatGPT or Claude chat joining the work.

Prepared by Claude on 2026-09-27 at Ness's request, from Ness's own decisions of 2026-09-24 to 2026-09-27 (dated in §8).

**Status: CANDIDATE** until Ness adopts it. It creates no new decision. If it disagrees with an authoritative file or an accepted record, that file wins, and this note gets a new version. It is never edited in place.

**This is not a behavior source.** It describes the project's route and working method, not how N.H behaves. No Master-21 card may cite it (contract §1.3: no history, actions, roles or workflow in cards).

---

## 1. The route: three documents, one after the other

Think of a map of N.H with blank spots.

| # | Document | What it is | Done when |
|---|---|---|---|
| 1 | **Master-21** (being written now) | The whole machine as decided **today**. Every line carries a stamp saying how real it is (BUILT, DESIGNED, ACCEPTED, CANDIDATE, INTENT, DECIDED-2026-09-24, DECIDED-2026-09-25), and every hole is written **NOT DECIDED**. The map, with the blank spots marked. | All chapters are written, audited and fixed, the appendices are rebuilt, the chapters are joined into one file, and **Ness adopts it**. It then becomes the new authority in place of V10, and V10 becomes history. |
| 2 | **The gap file** (name not chosen yet) | One big file that answers every blank spot, worked out by Ness with Claude and ChatGPT. Each answer names its exact part, so related answers are easy to find. It is saved to GitHub, with a new version each time and never edited in place. Master-21's Appendix A (the complete NOT DECIDED register) lists the holes it answers. | Every hole has Ness's answer |
| 3 | **The final master** (name not chosen yet) | The finished system as a whole, the way Ness wants it, **without** the build stamps. | Written from Master-21 plus the gap file, and adopted by Ness |

**Building waits.** Real building, including Claude Code's first real stage, waits until Master-21 is complete.

## 2. Master-21 in detail

- **What it describes:** N.H as one operating machine. The main path P-MAIN, plus the side paths (CY-…) for when something changes: new information, a clash, a failure, a permission block, another speaker, a re-read. Paths are made of parts, and parts are made of smaller parts.
- **Each part (a "card") says:**
  - ALONE: what it is, takes in, does, gives out, must never, fails closed by
  - TOGETHER: fed by, gated by, changes
  - USED BY: every place it appears in the machine
  - SUB-PARTS
- **What it is built from:** only what Ness has already decided (V10, the accepted packages in `04_`, candidates and decision records in `05_`, the bundles). Every line points at its source. Where nothing is decided, it says NOT DECIDED and stops.
- **Where the chapters live:** `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/`, named `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__<piece>.md`.
- **Size:** 66 chapter files in total.
  - 11 already written: CH00 to CH03-h.
  - 55 planned in three writing rounds (the plan Ness approved on 2026-09-26):
    - Writing 1: 18 pieces (the rest of Chapter 3, then Chapters 4–5)
    - Writing 2: 17 pieces (Chapters 6–8)
    - Writing 3: 20 pieces (Chapters 9–10, CH11 with every path except P-MAIN, and CH12-a to CH12-e with Appendices A–E)

  All 52 parts are covered exactly once.
- **Joining:** `07_TOOLS/nh_master21_assemble.py` glues the chapter files in order into one document. It copies text; it writes nothing new.
- **Appendices** (CH12): built by script from the finished chapters, and rebuilt after the audit fixes, because fixes change what they list.

## 3. How the work is run

**Who does what**
- **Ness** decides, approves plans, adopts, moves files, and uploads to GitHub. Nothing is adopted without him.
- **The ChatGPT writer chat** (GPT-6 Astra, Max effort) writes the chapter files.
- **An independent ChatGPT auditor chat** (fresh chat, Max effort, never the writer's chat) checks them.
- **Claude** checks deliveries on entry, verifies audit findings against the repository, writes fix requests and instruction files, and checks plans for completeness.

**Rhythm** (Ness, 2026-09-26)
1. Write the remaining 55 pieces in three big rounds.
2. Then run three audit rounds at the end: Audit 1 covers round 3C, CH00, CH03-b to d, and Writing 1; Audit 2 covers Writing 2; Audit 3 covers Writing 3 plus the whole document.
3. Fix what the audits find: a fix request goes to the writer, which returns corrected chapters, each with a changed-lines file. The fixes are then checked again.

**The writer's way of working**
- One piece at a time.
- After each piece: a checkpoint, an updated round manifest, and the file saved to Ness's ChatGPT Library.
- A stalled chat is replaced by a fresh chat that is given the rules, the manifest and the needed chapters.

**Files and fingerprints**
- Every file is identified by its SHA-256, never by its name. Old and new versions often share a name.
- Ness keeps each round's files in their own folder, `WRITING_1`, `WRITING_2` and `WRITING_3`.

**GitHub**
- A chapter goes to GitHub only after it passes.
- Uploads replace the old version under the same name, and history keeps the old one.
- Every upload is verified from a fresh clone.

## 4. The working files

These govern how the work is done. They decide nothing about N.H.

| File | Role |
|---|---|
| `NH_MASTER-21_SYSTEM_BEHAVIOR_BUILD_CONTRACT_FOR_CHATGPT_v1_0.md` (SHA-256 `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1`) | How chapters are written: template, stamps, citations, the 52 part IDs, chapter order, CONTRACT CHECK |
| `NH_MASTER-21_WRITER_LESSONS_FROM_AUDITS_v0_1.md` | Every mistake the audits found, turned into rules for the writer |
| `NH_MASTER-21_WRITER_RUN_INSTRUCTIONS_v0_2.md` | How a writing round runs: the approved 55-piece plan, the exact-name rule, the per-piece loop, checkpoints, manifests, the current chapter set |
| `NH_MASTER-21_INDEPENDENT_AUDIT_BRIEF_v0_3.md` | How an audit runs: modes (NEW / FIX / EXISTING), every check, the stages and checkpoints, the evidence rules, the report format |
| `NH_MASTER-21_FIX_REQUEST_ROUND3_2026-09-26.md`, `NH_MASTER-21_FIX_REQUEST_ROUND3C_2026-09-26.md` | The latest fix requests |
| `NH_MASTER-21_WRITING_1_MANIFEST.md` (then `…WRITING_2…`, `…WRITING_3…`) | Progress: every finished piece with its SHA-256, plus every problem found in earlier pieces |

Ness keeps these files; uploading them to GitHub is his call. A newer version of any of them replaces the older one for new work.

## 5. Rules that never change

- **Authority order:** V10 (`01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`) → Decision Defaults S19 v2_2 → cursorrules → Companion v1. The Working Map is subordinate; the decision index is navigation only.
- **Source pin** for new pieces: `6a7160ba688ba4e433a31899162815df7e2bab17`. Older chapters name `855459f…`; no cited source differs between the two. The pin moves only when Ness says so.
- **BUILT** only where V10's status table says that exact behavior is built.
- **Fill a box** only from the card's own text or its cited source. **NOT DECIDED** only where the sources are silent.
- **Source conflicts** are marked, never resolved by the writer or an auditor.
- **Nothing is edited in place.** Every change is a new version.
- **Quality is never lowered.** Filing errors get fixed, never parked on a list.

## 6. State on 2026-09-27 (a snapshot; the latest manifest is always newer)

**On GitHub** (HEAD `3407d2d`):
- CH00 `d01e8ec3…`, CH03-b `ba62fb68…`, CH03-c `20d022f2…`, CH03-d `9444e60b…`
- Older versions of CH01, CH02, CH03-a, CH03-e and CH03-f

**Passed but not yet uploaded:** round 3A. CH03-e `a33e27d8…`, CH03-f `567d566a…`, CH03-g `59f8d76f…`, CH03-h `af59933e…`.

**Accepted for now, audited in Audit 1:** round 3C. CH01 `f86342e9…`, CH02 `22168ca6…`, CH03-a `3b0ba1cb…`.

**Writing 1:** 11 of 18 pieces done (CH03-i to CH04-c). Every finished piece and every problem found so far is listed in the Writing 1 manifest.

**Known open items** (details in the manifest; for Audit 1):
- CH00 cites an older contract hash (`58673ab7…`).
- The lessons-1.2 candidates: possible wrongly empty boxes in finished pieces.
- CH04-c's A32/B18 source-review gap. The content is carried into CH04-d.
- Four findings in CH03-a.
- CH03-m's bare decision labels.
- The new source conflicts recorded in CH03-n, CH04-a, CH04-b and CH04-c.

## 7. How a new chat should start

1. Read this note, then the contract, the lessons sheet, and either the run instructions (writing) or the audit brief (auditing), then the latest manifest.
2. Check every file you are given by SHA-256 before using it. If anything differs or is missing, stop and say which.
3. Don't ask Ness again about anything settled here or in the files above. Ask only what is truly missing.
4. Work in the plainest possible language with Ness. Precise details belong in the files.

## 8. Ness's decisions behind this route

- **2026-09-24:** a "new full master": N.H as one machine in paths → parts → USED BY, with no history, sessions, roles or workflow, built only from decided material, every line pointing at its source, NOT DECIDED where nothing was decided. It starts as a candidate; if adopted, it becomes the new Master and V10 becomes history.
- **2026-09-25:** the two-master route. Master-21 shows what is not decided and not designed, and becomes the authority in place of V10. Then every blank is filled with Claude and ChatGPT, and the answers are saved to GitHub in one big file, with each part named explicitly and a new version each time. Only when all decisions are complete comes a final master without the build stamps.
- **2026-09-25:** building (including Claude Code's first real stage) waits for the full Master-21.
- **2026-09-26:**
  - The rest of Master-21 is written in three big rounds, then audited in three rounds at the end.
  - The 55-piece plan is approved, with Claude's corrections (exact names, current chapter set, C-GOLD and appendix rules).
  - Audits are run by a fresh, independent ChatGPT chat at Max effort, and Claude verifies the findings.
- **2026-09-26:** quality is not lowered, and the cleanup-list approach is rejected: filing errors are fixed, not parked.
