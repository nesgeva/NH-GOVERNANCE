# NH_MASTER-20_CORRECTED_v6 — CHANGE AND PROVENANCE REPORT

**Base file:** `NH_MASTER-20_CORRECTED_v5.md` (SHA-256: `3d40edfb7bcb1e22cced1983cad837e0e85fa31cc63d14e3b768efc149eb4648`)

---

## Document Identity
**Old:** `NH_MASTER-20_CORRECTED_v5.md`
**New:** `NH_MASTER-20_CORRECTED_v6.md`

## 1 — Living State Web Privacy Wording

**Old:** "Pre-retrieval eligibility and pre-output review apply when Living State Web content is shown."
**New:** "Internal Living State Web retrieval, evaluation, reasoning, and assembly use §7Q internal-use authorization. Visible presentation of Living State Web material uses §7Q visible-output eligibility and pre-output review. Level 1 restrictions, TSC blockers, compartment rules, and influence-removal instructions still apply."

## 2 — BOP Privacy Wording

**Old:** "§7Q's sensitivity levels, deletion framework, and pre-output review apply to BOP roots identically to any other root."
**New:** "BOP roots follow the same sensitivity, deletion, protection-level, and no-destruction rules as other roots. Internal BOP retrieval, analysis, identity assessment, and other internal processing use §7Q internal-use authorization. §7Q visible-output eligibility and pre-output review apply only when BOP or BOP-derived information is actually surfaced visibly, exported, shared, or included in a notification. Level 1 and TSC restrictions remain intact."

## 3 — LMAC Dependency-List Wording

**Old:** "§7Q — Privacy eligibility pre-check (LMAC enforces §7Q, does not replace it)"
**New:** "§7Q — Purpose-specific privacy authorization pre-check (LMAC routes the applicable §7Q authorization and does not choose, redefine, weaken, enforce independently, or replace it). Internal purposes... use internal-use authorization. Visible responses, exports, sharing, notifications, and visible presentation use visible-output authorization and pre-output review."

## 4A — §17 Phase 3 Lifecycle Transition

**Old:** "session → 'promoted'; promotion_completed_at = now; cache_promotion_completed written; retained safety archive created."
**New:** Added after archive creation: "tsc_retained_archive_created written; session → 'archived'. The session does not remain in 'promoted' after a retained archive is successfully created."

## 4B — §23 State Definitions

**Old:** "promoted — all items resolved; retained archive exists"
**New:** "promoted — all items resolved; archive transition not yet completed"

**Old:** "archived — retained archive only; active TSC structural database sealed and rendered read-only/inaccessible (not deleted)"
**New:** "archived — retained archive created; active TSC structural database sealed and rendered read-only/inaccessible; normal terminal operational state"

**Old:** "permanently_sealed — archive permanently sealed (not deleted); history record written..."
**New:** "permanently_sealed — separately authorized permanent seal; history record written...; permanent sealing never happens automatically"

Added: "No `deleted` lifecycle state exists. Archives are never deleted."

## 4C — §27 Startup Recovery

**Old:** "lifecycle_status = 'promoted' and retained archive exists: normal terminal state. No action."
**New:** Four distinct recovery states: `promoted` without archive → create archive + transition; `promoted` with archive but missing transition → idempotent repair to `archived`; `archived` → normal terminal; `permanently_sealed` → normal terminal.

## V5 Report-Count Correction

V5 no-loss report stated "12 passages" but the named list contained 14: identity, 1a, 1b, 2a, 2b, 3a, 3b, 3c, 4a, 4b, 5a, 5b, 5c, 5d.
