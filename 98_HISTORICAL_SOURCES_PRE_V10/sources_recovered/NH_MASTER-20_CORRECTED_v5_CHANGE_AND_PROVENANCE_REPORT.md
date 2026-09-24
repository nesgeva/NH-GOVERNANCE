# NH_MASTER-20_CORRECTED_v5 — CHANGE AND PROVENANCE REPORT

**Base file:** `NH_MASTER-20_CORRECTED_v4.md` (SHA-256: `a084644aaf26f311796b9501d2ff5eb735adb2c4a5907e95421e8878954a579f`)

---

## Document Identity
**Old:** `NH_MASTER-20_CORRECTED_v4.md`
**New:** `NH_MASTER-20_CORRECTED_v5.md`

## 1. Creation Filter

### 1a — Diagram description (§14)
**Old:** "*Reading the diagram:* chat (right) → cache → loop·starter → deep side (creation filter → meaning filter) → memory → log·mirror (left)..."
**New:** "*Reading the diagram [HISTORICAL — the two-box 'creation filter → meaning filter' layout shown in the SVG is superseded as literal current architecture. The settled current wiring is: chat → cache → loop starter → Meaning Engine running creation-aware mode when applicable → memory and log...]..."

### 1b — THE TWO FILTERS paragraph (§14)
**Old:** "THE TWO FILTERS (explored S8 — creation filter now settled). Chat on the right, N.H on the left, two filters in the middle: (1) AI creation filter... (2) meaning filter... Path: chat → AI creation filter → meaning filter..."
**New:** "THE TWO FILTERS (explored S8 — two-box layout superseded). [HISTORICAL — the original S8 exploration described two separate filters... This two-box layout is superseded as literal current architecture.] SETTLED: there is ONE Meaning Engine. The creation filter is a creation-aware mode inside that single Meaning Engine..."

## 2. TSC Lifecycle

### 2a — Session lifecycle_status enum (§4 schema)
**Old:** `"active" | "sealed" | "authorized" | "promoting" | "promoted" | "promotion_failed" | "interrupted"`
**New:** Added `"archived" | "permanently_sealed"`

### 2b — Session lifecycle path (§12)
**Old:** Only described path to `promoted` or `promotion_failed`
**New:** Added: `promoted → archived` after retained-archive creation; `archived → permanently_sealed` after separate authorization; permanent sealing requires separate authorization; no `deleted` lifecycle state exists.

## 3. TSC source_metadata

### 3a — Session-context metadata paragraph (§4)
**Old:** "They flow through to the sealed root via the `source_metadata` provenance fields that §7E already carries..."
**New:** "They do NOT physically enter the sealed seven-field root... Session provenance remains durably linked through identifiers: the §7E pre-ingest record records the resulting `root_id`; the TSC structural record retains `preingest_capture_id` and `promoted_root_id`."

### 3b — BOP timing relationship (§9)
**Old:** "preserved in the §7E pre-ingest record's `source_metadata`, which flows into the sealed root as provenance. This is not carried as new fields..."
**New:** "preserved in the §7E pre-ingest record's `source_metadata` and in the TSC structural records. This metadata does not physically enter the sealed seven-field root — the durable link is maintained through `capture_id`, `root_id`, `preingest_capture_id`, and `promoted_root_id`."

### 3c — SIA event links (§9)
**Old:** "through the `source_metadata` provenance on relevant promoted roots."
**New:** "through the `source_metadata` field in the §7E pre-ingest records of the relevant promoted items. The promoted roots themselves remain exactly seven fields..."

## 4. Privacy Authorization

### 4a — LMAC (§7G-A)
**Old:** "a current §7Q eligibility confirmation before Computed View processing"
**New:** "a current §7Q purpose-specific authorization check before Computed View processing"
Also added: "LMAC routes either §7Q internal-use authorization (for internal operations) or §7Q visible-output authorization (for visible responses, exports, external sharing), depending on the exact purpose. LMAC does not choose, redefine, weaken, or replace the §7Q rule."

### 4b — Camera/VR (§19)
**Old:** "subject to the capture exclusion rules in §7Q, including the pre-retrieval eligibility rules and the non-negotiable core exclusion layer"
**New:** "subject to capture exclusion rules and protected pre-ingest handling under the applicable §7Q protection level. Later internal processing uses §7Q internal-use authorization. Later visible surfacing uses §7Q visible-output eligibility and pre-output review."

## 5. Historical Logs

### 5a — §20 heading
**Old:** `## 20. S18 CONSOLIDATION AND CHANGE LOG`
**New:** `## 20. S18 CONSOLIDATION AND CHANGE LOG  [HISTORICAL SESSION SNAPSHOT — June 24 2026]` with historical disclaimer paragraph.

### 5b — §21 heading
**Old:** `## 21. S19 CONSOLIDATION AND CHANGE LOG`
**New:** `## 21. S19 CONSOLIDATION AND CHANGE LOG  [HISTORICAL SESSION SNAPSHOT — June 25 2026]` with historical disclaimer paragraph.

### 5c — §27 heading
**Old:** `## 27. RECOVERY AND CORRECTION LOG — CURRENT SESSION (June 25 2026)`
**New:** `## 27. HISTORICAL RECOVERY AND CORRECTION LOG — JUNE 25 2026` with historical disclaimer paragraph.

### 5d — Decision Defaults reference in §27
**Old:** "Still pending after this session: The Decision Defaults companion file (NH_DECISION_DEFAULTS-S17_AUDITED_v1.md)..."
**New:** "[HISTORICAL — describes state at June 25 2026]" label added; NH_DECISION_DEFAULTS-S17_AUDITED_v1.md marked as "[HISTORICAL — this filename is superseded; the current authoritative Decision Defaults are `NH_DECISION_DEFAULTS-S19_v2_2.md`...]"

## V4 Report-Count Correction
The V4 change report stated "7 corrections" but the actual V4 work contained 8 corrected passages: 1, 2, 3a, 3b, 3c, 3d, 4a, 4b. This is noted as a factual correction.
