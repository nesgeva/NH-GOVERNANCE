# NH_MASTER-20_CORRECTED_v4 — CHANGE AND PROVENANCE REPORT

**Base file:** `NH_MASTER-20_CORRECTED_v3.md` (SHA-256: `749a0907ee243bc87f17717b97e5601e7aea1102e703249e9dff5a2002ffe062`)

---

## 1 — Document Identity

**Old:** `NH_MASTER-20_CORRECTED_v2.md`
**New:** `NH_MASTER-20_CORRECTED_v4.md`

## 2 — §0B Access Boundary

**Old:** STATUS line immediately followed §0B content with no access-boundary clarification.
**New:** New ACCESS AND AUTHORIZATION BOUNDARY paragraph inserted before STATUS, stating: permanent recording does not by itself grant ordinary runtime access; all use remains subject to §7Q protection rules, Level 1 restrictions, identity/security authorization, TSC blockers, compartment rules, and influence-removal instructions; TSC-held material unavailable until blockers clear; Level 1 raw content only inside authorized boundary functions.

## 3a — §7G-A Context Retrieval

**Old:** "§7Q pre-retrieval eligibility applies via LMAC before any root is returned."
**New:** "§7Q internal-use authorization applies via LMAC before any root is returned: hidden, restricted, redacted, or deleted-from-view material remains internally eligible unless Ness issued a separate influence-removal instruction or another explicit compartment rule blocks that use; Level 1 raw content may be accessed only inside an authorized protected-boundary function; TSC-held or otherwise blocked pre-ingest material remains unavailable until its blockers clear. Visible-output eligibility is not the gate for this internal reading pass."

## 3b — §7G-A Clash Detection

**Old:** "§7Q Layer-1 eligibility applies via LMAC before clash detection operates on the reading."
**New:** "§7Q internal-use authorization applies via LMAC before clash detection operates on the reading: hidden, restricted, or deleted-from-view material may still participate in clash detection unless a separate influence-removal instruction or another explicit rule blocks it; Level 1 and TSC restrictions still apply. Clash detection is an internal operation — visible-output eligibility is not the governing gate."

## 3c — §7G-A Computed View

**Old:** "§7Q Layer-1 eligibility applies via LMAC before any Computed View operation. The §7R relevance mode appropriate to the view-assembly purpose is applied via LMAC."
**New:** "§7Q internal-use authorization applies via LMAC before any Computed View operation: hidden, restricted, or deleted-from-view material may participate in internal snapshot computation unless a separate influence-removal instruction or another explicit rule blocks it... Computed View snapshot creation is an internal operation — visible-output eligibility and pre-output review do not run merely because a snapshot is being computed. Visible-output eligibility and pre-output review apply only when information derived from the Computed View is actually being surfaced..."

## 3d — §7G-A Per-Profile Snapshot Step

**Old:** "apply §7Q Layer-2 pre-output review; run the triggered update"
**New:** "apply §7Q internal-use authorization; run the triggered update... (§7Q visible-output review applies later, only when snapshot-derived information is surfaced in a visible response.)"

## 4a — §7R External Prerequisite

**Old:** "§7Q's privacy and deletion eligibility gate runs before Attention and Relevance Control receives any candidates. Attention and Relevance Control operates only on already-eligible material."
**New:** "§7Q authorization runs before Attention and Relevance Control receives any candidates. The type of §7Q authorization is purpose-specific: for visible presentation, exports, external sharing, notifications, or a visible response, §7Q visible-output eligibility runs first; for internal retrieval, internal relevance evaluation, internal reasoning, clash detection, and Computed View assembly, §7Q internal-use authorization applies... Attention and Relevance Control operates only on material authorized for the exact current purpose."

## 4b — §7R Relevance Judgment Prerequisite

**Old:** "produced after §7Q eligibility has been established"
**New:** "produced after §7Q authorization for the current purpose has been established"
