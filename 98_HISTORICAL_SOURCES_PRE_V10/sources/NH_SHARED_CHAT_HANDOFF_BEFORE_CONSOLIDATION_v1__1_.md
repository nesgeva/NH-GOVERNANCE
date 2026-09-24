# N.H CHAT HANDOFF — AUTHORITATIVE STATE AND NEXT TASK

**Purpose:** This file is a shared handoff for both ChatGPT and Claude so a new chat can continue safely without relying on conversation memory.

**Created:** June 28, 2026

---

## 1. CURRENT AUTHORITATIVE FILES

The following pair has been explicitly adopted by Ness and is authoritative:

### Authoritative Master
- File: `NH_MASTER-19_CORRECTED_v7_1.md`
- SHA-256: `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf`

### Authoritative Decision Defaults
- File: `NH_DECISION_DEFAULTS-S19_v2_2.md`
- SHA-256: `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696`

These two files are the current authoritative N.H pair.

Earlier Master and Decision Defaults versions remain historical backups only and are not current authority.

---

## 2. ACCEPTED STANDALONE TSC DESIGN

The complete accepted Temporary Session Cache design remains a standalone companion specification:

- File: `NH_ACCEPTED_TSC_DESIGN_v1.md`
- SHA-256: `1da2e296d4345d11dcec5f197aa9a42883349526275c5aa32b0bb07d1ca44658`
- Status: `ACCEPTED DESIGN — NOT YET BUILT`

The Master contains the TSC integration summary, but this standalone file remains the complete accepted 31-section TSC specification.

---

## 3. OTHER CURRENT PROJECT FILES

These files remain relevant but are not the current authoritative Master/Defaults pair:

- `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md`
  - Accepted security, identity, BOP, SIA, SACL, BAI, phone recovery, pairing, enrollment, and BGMM-related designs.
  - Companion/recovery source.
  - Not automatically authoritative where not yet patched into the Master.

- `NH_WORKING_ROLES.md`
  - Working-role rules for Ness, Claude, and ChatGPT.
  - Claude architects and prepares files.
  - ChatGPT independently checks contradictions, omissions, and no-loss claims.
  - Ness alone decides concept-level choices and adoption.

- Earlier Master files and earlier Decision Defaults files
  - Historical backups only.
  - Do not delete or overwrite during consolidation work.

---

## 4. VERIFIED ADOPTION HISTORY

### Master adoption
`NH_MASTER-19_CORRECTED_v7_1.md` was produced from `NH_MASTER-19_CORRECTED_v7.md` by changing only the adoption-status sentence.

Verification already completed:
- 1 line changed
- 0 lines deleted
- 0 unrelated lines changed
- Line count: 1,937
- SHA-256: `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf`

### Decision Defaults adoption
`NH_DECISION_DEFAULTS-S19_v2_2.md` was produced from `NH_DECISION_DEFAULTS-S19_v2_1.md` by changing only the Master sync, Master hash, and adoption-status header lines.

Verification already completed:
- 4 header lines changed
- 0 lines deleted
- 0 unrelated lines changed
- Line count: 314
- SHA-256: `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696`

No further adoption patch is pending.

---

## 5. CURRENT NEXT TASK

Ness wants to consolidate the current N.H project files from seven files into fewer than five files, preferably four, without losing, rewriting, weakening, or silently omitting any detail.

The next step is **proposal only**.

No file may be created, merged, modified, deleted, renamed, or replaced until Ness explicitly approves the proposal.

---

## 6. CONSOLIDATION REQUEST TO CONTINUE FROM

Use this exact task in the new chat:

> I want to consolidate the current N.H project files from seven files into fewer than five files, without losing, rewriting, or silently omitting any detail.
>
> First, inspect all current files and prepare a proposal only.
>
> Requirements:
>
> 1. Target four final files if possible.
> 2. Preserve the authoritative Master and Decision Defaults as separate files.
> 3. Identify which companion, accepted-design, working-role, and handoff files can safely be combined.
> 4. Do not merge unrelated authority levels without clearly separating them inside the combined file.
> 5. Preserve every accepted design, provenance statement, status label, hash, dependency, warning, and open question.
> 6. Show:
>    - proposed final filenames,
>    - which source files go into each,
>    - exact section order,
>    - authority status of each final file,
>    - duplication that may be removed,
>    - and any conflicts or stale references that require correction.
> 7. Do not create or modify any file yet.
> 8. Do not summarize away detailed designs.
> 9. Use a patch-only, no-loss method and preserve the original files unchanged.
>
> This is proposal-only. Wait for my explicit approval before creating consolidated files.

---

## 7. REQUIRED WORKING METHOD

For this consolidation task:

1. Inspect all relevant current files before proposing anything.
2. Verify filenames and hashes where available.
3. Treat the authoritative Master and authoritative Decision Defaults as separate and preserved.
4. Do not silently merge companion designs into authority.
5. Keep accepted-design status, historical provenance, and implementation status intact.
6. Surface stale references and conflicts instead of silently correcting them.
7. Preserve originals unchanged.
8. Produce a structural proposal first.
9. Wait for explicit Ness approval before creating any consolidated file.
10. After creation, perform a no-loss verification against every source file.

---

## 8. INTERACTION RULES FOR NESS

- Explain one step at a time.
- Use plain, everyday language first.
- Do not reopen settled design decisions.
- Do not make concept-level choices for Ness.
- Do not silently patch files.
- Do not tell Ness to move chats, stop, rest, or end a session unless he asks.
- When a file is requested, return the actual file.
- Preserve version history.
- Ness decides; Claude architects; ChatGPT checks.

---

## 9. STARTING STATE FOR A NEW CHAT

At the beginning of the new chat:

1. Confirm access to:
   - `NH_MASTER-19_CORRECTED_v7_1.md`
   - `NH_DECISION_DEFAULTS-S19_v2_2.md`
   - `NH_ACCEPTED_TSC_DESIGN_v1.md`
   - `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md`
   - `NH_WORKING_ROLES.md`
   - this handoff file
2. Confirm the authoritative hashes listed in this file.
3. Do not modify anything.
4. Begin with the consolidation proposal only.

---

## 10. AUTHORITY NOTE

This handoff file is not itself an architectural authority file.

It records:
- the current authoritative pair,
- the accepted standalone TSC design,
- the verified adoption history,
- the next requested task,
- and the safe continuation procedure.

If this handoff conflicts with the authoritative Master or Decision Defaults, the authoritative pair wins.
