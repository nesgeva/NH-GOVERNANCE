# NH_MASTER-20_CORRECTED_v1 — CHANGE AND PROVENANCE REPORT

**Base file:** `NH_MASTER-20.md` (SHA-256: `204cf0fa13eb011a1de1781547381dbe7250e0452ae2c41f238d5802de1e95b5`, 5,640 lines)
**Output file:** `NH_MASTER-20_CORRECTED_v1.md` (draft, not adopted)

---

## CORRECTION 1 — Document Identity

**Old:** `# N.H — MASTER-19: Full Backup with All Additions`
**New:** `# N.H — MASTER-20: Complete Candidate Master` with status statement and historical provenance label.

**Old (session 18 paragraph):** "This file (NH_MASTER-19_CORRECTED_v7.md) is the adopted authoritative N.H Master"
**New:** "[Historical provenance: NH_MASTER-19_CORRECTED_v7.md was the adopted authoritative N.H Master at that time...]"

## CORRECTION 2 — Status Table Reconciliation

| Row | Old | New |
|---|---|---|
| Privacy/deletion | "five operations" | "six operations (exclusion, sealed isolation, hiding, restriction, redaction, deletion as non-destructive visibility removal)" |
| Chat front door | "DESIGN-IN-PROGRESS, NOT CONFIRMED" | "PARTIALLY SETTLED, PARTIALLY OPEN, NOT BUILT" |
| TSC (duplicate) | Two rows (old + corrected) | Consolidated into one "ACCEPTED WITH LATER CORRECTIONS" row; blocker row kept separately |
| Multi-box | "NOT DESIGNED" | "SETTLED CONCEPT, MECHANICAL ARCHITECTURE NOT DESIGNED" |
| Wonder/simulation | "CONCEPT LEVEL ONLY" | "SCRATCH-SPACE BOUNDARY SETTLED; LARGER MECHANISM NOT DESIGNED" |
| End-to-end cycle | "IDENTIFIED, NOT YET DESIGNED" | "POST-ROOT READING PATH DESIGNED (§7G-A); FULL CYCLE STILL OPEN" |
| BAI | Incorrectly included `authorization_type` | Moved to BOP where it belongs |
| BOP | Did not mention `authorization_type` | Now includes adopted vocabulary `authorization_type = "enrollment_declared"` |
| Creation Store | Not present | Added: "SETTLED CONCEPT, NOT BUILT" with confirmation rules |

## CORRECTION 3 — §7Q Deletion Behavior

**Old (Deletion operation):** "removed from ordinary visible output, retrieval, display, analysis, simulation, and use in new derivations"
**New:** "removed from ordinary visible output, display, external sharing, and any visible access path" — internal retrieval, analysis, simulation, connections, and use preserved unless Ness separately gives an influence-removal instruction.

**Old (MUST NEVER ALLOW):** "Retaining deleted material through any indirect path... Treating a deletion marker as equivalent to actual deletion"
**New:** "Accidentally resurfacing deleted material in visible output... Treating a deletion marker as equivalent to an influence-removal instruction"

**Old (DELETION AS):** "removes material from ordinary visible output, retrieval, display, analysis, simulation, and use in new derivations"
**New:** "removes material from ordinary visible output, display, external sharing, and any visible access path — but content remains preserved internally, internally retrievable, internally connected, and internally usable"

**Old (derivatives):** "removed from visible output, rebuilt without..."
**New:** "removed from visible output... Internal connections and internal usability are preserved unless Ness gives a separate influence-removal instruction."

**Old (unresolved case):** "prevented from retrieval, display, analysis, simulation, or use in new derivations"
**New:** "prevented from appearing in visible output, display, or external sharing. Internal preservation and internal connections continue unless Ness separately instructs otherwise."

## CORRECTION 4 — TSC Exclusion Handling (§17 and §25)

**§17 Old:** "raw content replaced with exclusion metadata"
**§17 New:** "excluded raw content moves to separate sealed protected storage under the applicable §7Q protection level; TSC-side and §7E pre-ingest records retain only non-reconstructive exclusion metadata, the opaque protected-record identifier, and required handling history"

**§25 Old:** Corrupted sentence "No excluded content... Excluded raw content moves... stored."
**§25 New:** Clean rewrite: "Excluded raw content must leave the active TSC database, the ordinary §7E pre-ingest record, and the retained TSC safety archive. It is not destroyed. ... excluded raw content moves to separate sealed protected storage... No excluded raw content is retained inside the active TSC, ordinary pre-ingest record, or retained archive."

**Mixed-content Old:** "excluded portion replaced with non-reconstructive metadata"
**Mixed-content New:** "excluded portion moves to separate sealed protected storage"

## CORRECTION 5 — Wonder/Simulation Scratch-Space Rule

**§11 item 30 Old:** "CONCEPT LEVEL ONLY, NOT DESIGNED. Concept in §7B; interface concepts in §19. Mechanism undesigned."
**§11 item 30 New:** "SCRATCH-SPACE BOUNDARY SETTLED; LARGER MECHANISM NOT DESIGNED. Ordinary real-reading paths may not use simulation scratch space. Wonder mode may use it. Scratch-space output cannot enter memory directly."

Status table updated to match.

## CORRECTION 6 — Multi-Box Clarification

**§11 item 18 Old:** "MULTI-BOX (sealed-batch) ARCHITECTURE — undesigned."
**§11 item 18 New:** "CONCEPT SETTLED, MECHANICAL ARCHITECTURE NOT DESIGNED. Future sealed batches remain separate immutable batches. All batches participate in one memory system. Manifest structure, identifiers, deduplication, cross-batch reading, indexing, and crash recovery remain mechanical architecture work."

Status table updated to match.

## CORRECTION 7 — Creation Store Confirmation Rule

**Old:** "a time-based provisional-to-confirmed transition rule (not yet designed)"
**New:** "Time passing alone never confirms a creation. Ambiguous records remain provisional." Only explicit confirmation or clear demonstrated adoption.

## CORRECTION 8 — Companion Wrapper Text Removed

Removed from active Master body:
- `*End of NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md*`
- `*End of NH_ACCEPTED_PERSONAL_LEARNING_DESIGN_v1.md*`
- `*It does not modify the Master...*` / `*must be formally patched...*`
- `*This file was created June 29 2026...*` (standalone file statement)

Source filenames, hashes, and integration provenance preserved in section provenance notes.

## CORRECTION 9 — TSC Audit-Event Presentation

Superseded archive-deletion event names and proposed replacement names moved outside the fenced event-list block. Active event list now contains only active vocabulary. Superseded names, corrected meanings, and proposed replacements clearly labeled in separate paragraphs below the list.

## CORRECTION 10 — §14 Heading and Status

**Old:** "## 14. THE CHAT FRONT DOOR [DESIGNED-IN-PROGRESS — explored S8, NOT confirmed, NOT built]"
**New:** "## 14. THE CHAT FRONT DOOR [PARTIALLY SETTLED, PARTIALLY OPEN — NOT BUILT]" with settled/open breakdown.
