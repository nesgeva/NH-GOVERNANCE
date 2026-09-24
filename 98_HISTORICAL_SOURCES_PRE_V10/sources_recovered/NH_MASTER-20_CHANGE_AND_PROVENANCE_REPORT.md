# NH_MASTER-20 — CHANGE AND PROVENANCE REPORT

**Base file:** `NH_MASTER-19_CORRECTED_v7_1.md` (SHA-256: `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf`, 1,937 lines)
**Output file:** `NH_MASTER-20.md` (draft, not adopted)
**Integration plan:** `NH_INTEGRATION_LEDGER_AND_PATCH_PLAN_v5.md`

---

## INSERTED SECTIONS

| New section | Lines | Source |
|---|---|---|
| §0B Full-Transparency and Living-Record Law | ~30 | v8 candidate + v2_3 Defaults + V5 Step 1.2 |
| §7E-TSC Detailed Design (31 sections) | ~852 | `NH_ACCEPTED_TSC_DESIGN_v1.md` with V5 Step 3 corrections |
| §7G Creation-Aware Mode | ~12 | V5 Step 7 |
| §7G-A Input Cycle | ~385 | `NH_RECOVERED_INPUT_CYCLE_PATCH_SOURCE_MAP_v4.md` design content |
| §25 Voice Security and Identity System | ~1,673 | `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md` with V5 Step 2 corrections |
| §26 Personal Learning and Adaptation System | ~720 | `NH_ACCEPTED_PERSONAL_LEARNING_DESIGN_v1.md` |
| §9 Recovered features (4 subsections) | ~30 | V5 Step 9 |
| §7M Computed View internal-only rule | ~2 | V5 Step 10 |
| §7N Gentle-question rule | ~3 | V5 Step 11 |
| §8 Screenshot-not-reasoning-source note | ~2 | V5 Step 8.1 |
| Status table: 23 new rows | ~23 | V5 Step 12 |
| §11-SETTLED: post-S19 entry | ~1 | V5 Step 5 |
| §6A Input Cycle protected files | ~1 | V5 Step 5.6 |

## CORRECTED SECTIONS (old → new)

### §0A — Pure tape paragraph
**Old:** "★ THE PURE TAPE NEEDS A REDACTION/DESTRUCTION PATH (safety)... cryptographic erasure... TOMBSTONE..."
**New:** "★ THE PURE TAPE PRESERVES eligible events append-only — subject to capture exclusions and two protection levels... True destruction is permanently prohibited... history record (not a tombstone)..."
**Source:** V5 Step 1.1
**Reason:** No-destruction law; two-protection-levels model replaces destruction/tombstone model

### §1 — Root change description
**Old:** "The only change a root can undergo is deliberate, audited destruction (§7Q)."
**New:** "The only change a root can undergo is non-destructive visibility removal (§7Q) — the root remains preserved internally."
**Source:** V5 Step 1.6

### §7Q — Six operations (was five)
**Old:** "FIVE OPERATIONS — DISTINCT, NOT INTERCHANGEABLE." (Exclusion, Hiding, Restriction, Redaction with tombstone, Deletion as destruction)
**New:** "SIX OPERATIONS — DISTINCT, NOT INTERCHANGEABLE." (Exclusion, Sealed isolation [NEW], Hiding, Restriction, Redaction with history record, Deletion as non-destructive visibility removal)
**Source:** V5 Step 1.3

### §7Q — Deletion outcomes
**Old:** `verified_complete`, `completed_with_declared_limits`; "content-free tombstone"
**New:** `protected_complete`, `protected_with_declared_limits`; "history record"; "DELETION AS NON-DESTRUCTIVE VISIBILITY REMOVAL"
**Source:** V5 Step 1.3

### §7Q — Undesigned list
**Old:** Included "cryptographic erasure mechanisms"
**New:** Removed "cryptographic erasure mechanisms"
**Source:** V5 Step 1.7d

### §7B — Part 0 reference
**Old:** "capture-exclusions + audited redaction — §0A"
**New:** "capture-exclusions + two protection levels — §0A, §0B"
**Source:** V5 Step 1.7e

### §8 — Fallback paragraph
**Old:** "N.H must not treat it as fully preserved or assign it the same confidence... require corroboration..."
**New:** "A missing screenshot does not lower the textual source's evidential confidence and does not automatically create a corroboration requirement."
**Source:** V5 Step 8.2

### §8 — Academic source
**Old:** "★ ACADEMIC SOURCE — STILL OPEN (S19)... Decision pending"
**New:** "★ ACADEMIC SOURCE — DECIDED (settled June 29 2026)... Both Semantic Scholar and OpenAlex will be used."
**Source:** V5 Step 8.3

### §14 — Creation filter
**Old:** "OPEN QUESTION: is the creation filter a genuinely distinct mechanism..."
**New:** "SETTLED (June 29 2026): the creation filter is a creation-aware mode..."
**Source:** V5 Step 7

### §14 — Always-capture
**Old:** "Is the live chat captured always or deliberately kept (the one-way-door question, never resolved)?"
**New:** "Always-capture: SETTLED — every live-chat message is captured automatically"
**Source:** V5 Step 6

### §11 item 9 — Academic source
**Old:** "OPEN"
**New:** "SETTLED June 29 2026... Both Semantic Scholar API and OpenAlex will be used."
**Source:** V5 Step 8.3

### §11 item 32 — End-to-end cycle
**Old:** "IDENTIFIED, NOT YET DESIGNED"
**New:** "POST-ROOT READING PATH NOW DESIGNED (§7G-A); FULL CYCLE STILL OPEN"
**Source:** V5 Step 5

### Status table — Pure tape row
**Old:** "Pure-tape redaction/destruction path... tombstone rule, cryptographic erasure"
**New:** "Pure-tape preservation path (two protection levels)... six operations, two protection levels, no-destruction law, history-record model"
**Source:** V5 Step 1.4

### Closing principles
**Old:** "audited redaction" and "DELETION IS BLOCKING AND VERIFICATION-BASED... tombstone only"
**New:** "two protection levels" and "DELETION IS NON-DESTRUCTIVE VISIBILITY REMOVAL... history record, not tombstone"
**Source:** V5 Steps 1.7e

### Recovery Log
**Old:** "## 25. RECOVERY AND CORRECTION LOG"
**New:** "## 27. RECOVERY AND CORRECTION LOG"
**Reason:** Renumbered after insertion of §25 (Security/Identity) and §26 (Personal Learning)

## SUPERSEDED ITEMS (retained in provenance only)

| Item | Location | Reason |
|---|---|---|
| TSC §15 (Private Ness Inspection Without Promotion) | §7E-TSC Detailed Design §15 | June 29 2026 inspection prohibition |
| `tsc_inspection_requested` audit event | §7E-TSC §26 | Inspection prohibited |
| `tsc_inspection_bai_token_consumed` audit event | §7E-TSC §26 | Inspection prohibited |
| `tsc_inspection_started` audit event | §7E-TSC §26 | Inspection prohibited |
| `tsc_inspection_ended` audit event | §7E-TSC §26 | Inspection prohibited |
| `tsc_archive_deletion_authorized` event name | §7E-TSC §26 | No-destruction law; proposed replacement `tsc_archive_seal_authorized` pending review |
| `tsc_archive_deleted` event name | §7E-TSC §26 | No-destruction law; proposed replacement `tsc_archive_sealed` pending review |
| TSC `deleted` lifecycle state | §7E-TSC §23 | No-destruction law; replaced with `permanently_sealed` |
| TSC §26 dual-cluster explanation | §7E-TSC §26 | Only promotion cluster remains |
| TSC §29 inspection BAI/SACL references | §7E-TSC §29 | Inspection prohibited |
| TSC §30 inspection-specific prohibitions | §7E-TSC §30 | Replaced with blanket prohibition |
| TSC §31 "inspection mechanism settled" | §7E-TSC §31 | Corrected to note supersession |

## SECURITY/IDENTITY NO-DESTRUCTION CORRECTIONS

| Location | Old wording | New wording |
|---|---|---|
| §7 QR state 2 | "permanently destroyed" | "rendered permanently inert and sealed" |
| §7 "What is destroyed when" | "Destroyed at" | "Rendered permanently inert at" |
| §8 rotation failure | "new code destroyed" | "new code rendered permanently inert" |
| §8 phone copy | "Phone immediately erases" | "Phone immediately renders inaccessible and seals" |
| §10 rollback | "All provisional new material destroyed" | "sealed and rendered permanently inert" |
| §7 QR at pairing | "destroyed at pairing" | "rendered permanently inert at pairing" |
| BGMM temp files | "deleted only after..." | "sealed and rendered inaccessible after..." |
| BGMM rollback | "package securely deleted" | "sealed and permanently inaccessible" |
| BGMM completion | "deleted after successful completion" | "sealed and rendered inaccessible" |

## PENDING ITEMS PRESERVED

- `acoustic_condition_notes` BOP amendment (PENDING SEPARATE REVIEW)
- Personal Learning D1 (authorization boundary)
- Personal Learning D2 (13 area names)
- Personal Learning D3 (voice observation scope)
- TSC proposed replacement event names (`tsc_archive_seal_authorized`, `tsc_archive_sealed`)
- Phone-side mode behavior (5 names recovered, no behavior designed)
- Personality simulation mechanism details
- Creation Mode implementation details
- Bounded retry policy for technical failures
- Reread mode-assignment rule
- Final retrieval parameters
