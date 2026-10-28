# NH_MASTER-20_CORRECTED_v3 — CHANGE AND PROVENANCE REPORT

**Base file:** `NH_MASTER-20_CORRECTED_v2.md` (SHA-256: `e1b21c4f8cc35b5ad8395f7bec6b6dd0b3ab804ce033240b062fbc6a3d70e34c`)

---

## 1A — Exclusion Operation

**Old:** "material never enters N.H at all. Filtered at the front door before capture. Cleanest boundary because there is nothing to manage afterward."
**New:** Raw content intercepted before entering ordinary visible storage; moves to sealed protected storage or protected pre-ingest hold; ordinary records receive only safe handling record and opaque identifier; nothing silently dropped or destroyed.

## 1B — Sealed Isolation

**Old:** "sealed inside a protected execution boundary (Level 1)... never displayed, analyzed, or surfaced"
**New:** Two protection levels described; Level 1 (authorized boundary functions only) and Level 2 (available to Ness after identity verification). Sealed material remains internally connected and usable under its protection rules. "Never analyzed" removed.

## 1C — Hiding and Restriction

**Old (Hiding):** "A presentation rule, not a data operation."
**New:** "A visible-presentation rule... does not automatically stop internal retrieval, internal analysis, internal connections, internal simulation, or internal influence"

**Old (Restriction):** "access is limited by explicit rules"
**New:** "visible access is limited by explicit rules... does not automatically stop internal retrieval, internal analysis, internal connections, or internal influence"

## 1D — Level 4 and Layer A

**Old (Level 4):** "Must never enter normal stores. If encountered at capture, must be excluded or immediately isolated."
**New:** "Must never enter ordinary roots, readings, indexes... intercepted and moved immediately to Level 1 sealed protected storage... Ordinary records retain only non-reconstructive metadata... Level 1 material is never destroyed."

**Old (Layer A):** "A dedicated secrets vault, if ever built, is a separate system..."
**New:** "Intercepted material moves immediately to Level 1 sealed protected storage or a Level 1 protected pre-ingest hold... Level 1 material is never destroyed." Stale secrets-vault statement removed.

## 1E — Ness-configured Exclusions and Mixed-Content

**Old (Layer B):** "fully excluded"
**New:** "excluded from ordinary capture and ordinary memory (raw content moves to sealed protected storage — not erased)"

**Old (mixed-content):** "isolate and remove the excluded portion"
**New:** "isolate the excluded portion and move it to sealed protected storage under the applicable protection level"

## 1F — Pre-retrieval Eligibility

**Old:** "Ineligible material must not be ranked, semantically compared, selected, passed to the mouth, used for simulation, or allowed to influence the response indirectly."
**New:** Renamed to "Pre-retrieval visible-output eligibility control." Distinction: deletion/hiding/restriction/sealed-isolation do not automatically remove internal influence. "Stopping internal influence requires a separate explicit influence-removal instruction from Ness with recorded scope."

## 1G — Remaining-Undesigned List

**Added:** exact Level 1 protected execution boundary design; exact sealed protected storage design; derivative discovery for sealed material; influence-removal instruction schema and scope mechanics.

## 2 — §7G Creation Mode Status

**Old:** "Exact creation-mode behavior, provisional-to-confirmed rules, and store schema remain undesigned."
**New:** "The two confirmation routes are settled: (1) explicit confirmation by Ness, (2) later words or actions clearly demonstrating adoption. Time alone never confirms a creation; ambiguous records remain provisional. Exact provisional-record detection mechanics, implementation behavior, and store schema remain undesigned."

## 3 — §11 Numerical Order

**Old order:** 32, 35, 33, 34
**New order:** 32, 33, 34, 35
Items 33 and 34 not rewritten; only moved after 32 and before 35.
