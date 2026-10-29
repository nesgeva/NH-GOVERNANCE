# Chapter 5-e — Group C: C-CREATE

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH05-e.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`

This piece covers C-CREATE — Unified Creation Store (§14, §7G creation-aware mode), with all its sub-parts. It leaves every path except P-MAIN to CH11, and the appendices to CH12.

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Every citation resolves at the pinned commit.

<!-- BEGIN BEHAVIOR -->

### C-CREATE — Unified Creation Store (§14, §7G creation-aware mode)
Stamp: DESIGNED    Source: [V10 §7G / CREATION-AWARE MODE] [MAP C-CREATE]

ALONE
- What it is: DESIGNED — One connected store for Ness-produced designs, ideas, rules, names and decisions recognized on the live-chat creation path. [V10 §7G / CREATION-AWARE MODE] [MAP C-CREATE]
- Takes in: DESIGNED — Provisional material from the Meaning Engine's creation-aware mode, source provenance and actual confirmation evidence. [V10 §7G / CREATION-AWARE MODE] [MAP C-CREATE]
- Does: DESIGNED — Preserves creations together; permits multiple types per record and project/category views; confirms only by explicit Ness confirmation or later clear demonstrated adoption. [V10 §7G / CREATION-AWARE MODE] [MAP C-CREATE]
- Gives out: DESIGNED — Persistent provisional or validly confirmed Creation Records, available through the meaning and view owners. [V10 §7G / CREATION-AWARE MODE] [MAP C-CREATE]
- Must never: DESIGNED — Split the store by type/category, overwrite earlier creations, confirm by time alone or treat ambiguity as confirmation. [V10 §7G / CREATION-AWARE MODE] [MAP C-CREATE]
- Fails closed by: DESIGNED — Ambiguous records remain provisional, potentially forever; access observes privacy before relevance. [V10 §7G / CREATION-AWARE MODE] [MAP C-CREATE]

TOGETHER
- Fed by: ACCEPTED — C-CREATE.3 — Creation fragment detection mechanics: Receives broad source-grounded provisional detection. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Fed by: ACCEPTED — C-CREATE.6 — Derived creation current-status view: Reads current status from committed events. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fed by: DESIGNED — C-7G.7 — Creation-aware reading mode: Receives recognized Ness-produced material from the existing mode. [V10 §7G / CREATION-AWARE MODE] [MAP C-CREATE]
- Fed by: DESIGNED — C-14.3 — Creation-aware live routing: Receives material from the settled live-chat creation route. [V10 §7G / CREATION-AWARE MODE] [MAP C-CREATE]
- Gated by: ACCEPTED — C-CREATE.1 — One-store creation boundary: Uses one connected store of root-referencing creation records. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §8]
- Gated by: ACCEPTED — C-CREATE.5 — Two-route creation confirmation gate: Requires one of the two confirmation routes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.8 — Traceable provisional creation influence: Provisional wider influence requires carried status and trace. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Gated by: ACCEPTED — C-CREATE.9 — Creation fragment relationships and larger works: Preserves all original fragments in larger works. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.10 — Creation operation and recovery rules: Applies atomic, idempotent, recoverable operations. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.11 — Current creation-scope boundaries: Keeps current vocabulary and front-door scope fixed. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: ACCEPTED — C-CREATE.2 — Immutable base Creation Record: Appends creation-time facts once. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: ACCEPTED — C-CREATE.4 — Append-only creation event family: Accretes actual later events. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: ACCEPTED — C-CREATE.7 — Creation views over one store: Makes views over the one store. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: DESIGNED — C-7I — View Layer (§7I): Makes creations available through the existing view surface. [MAP C-CREATE]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-14.3 — Creation-aware live routing | Live creation fragments and source references. | Uses the unified store's immutable base and append-only events. | Captured fragments never become settled merely through use. | [V10 §7G / CREATION-AWARE MODE] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] |
| 2 · ACCEPTED | C-14.3.4 — Provisional availability and influence | Relevant provisional creation material. | Applies the store's permitted-influence boundary. | No silent adoption through retrieval or answers. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)] |
| 3 · DESIGNED | C-7G.7 — Creation-aware reading mode | Recognized creation type, material and provenance. | Appends a proper base or a linked re-evaluation for an existing fragment. | Distinct detector versions do not duplicate the creation. | [V10 §7G / CREATION-AWARE MODE] |
| 4 · DESIGNED | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G); CY-B | The settled creation-aware sub-path of a live-chat turn. | Preserves source-grounded provisional creations and confirms only through the two valid routes. | Connected creation history exists with truthful status; full chat/creation synchronization remains separately open. | [MAP CY-B] [MAP C-CREATE] |
| 5 · DESIGNED | C-7I — View Layer (§7I) | Readings in creation order with acceptance/usability status. | Supplies existing creation objects made available through the view surface. | Nothing in this card. | [MAP C-7I] [MAP C-CREATE] |
| 6 · CANDIDATE | C-19.17.12 — Idea Card and Idea Deck | A provisional creation and its source-carried status. | Supplies the owned creation and its status. | Nothing in this card. | [05/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_2.md §14.1] |

SUB-PARTS: C-CREATE.1 — One-store creation boundary; C-CREATE.2 — Immutable base Creation Record; C-CREATE.3 — Creation fragment detection mechanics; C-CREATE.4 — Append-only creation event family; C-CREATE.5 — Two-route creation confirmation gate; C-CREATE.6 — Derived creation current-status view; C-CREATE.7 — Creation views over one store; C-CREATE.8 — Traceable provisional creation influence; C-CREATE.9 — Creation fragment relationships and larger works; C-CREATE.10 — Creation operation and recovery rules; C-CREATE.11 — Current creation-scope boundaries

### C-CREATE.1 — One-store creation boundary
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §8]

ALONE
- What it is: ACCEPTED — The accepted Creation Store structure: learning records that reference existing source roots and produce no new roots. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §8]
- Takes in: ACCEPTED — Live-chat source fragments and append-only creation events. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §8]
- Does: ACCEPTED — Maintains one store; type and project/category distinctions are connected records/views, never per-type databases or a second memory. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §8]
- Gives out: ACCEPTED — Source-linked creations with derived confirmation and grouping views. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §8]
- Must never: ACCEPTED — Turn creation detection into another ingestion front door, fuse original fragments or duplicate the memory store. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §8]
- Fails closed by: ACCEPTED — Provisional Creation Records are not held pre-ingest content; their allowed use still requires carried status and traceability. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.11 — Current creation-scope boundaries: One-store structure remains confined to current creation scope. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-CREATE — Unified Creation Store (§14, §7G creation-aware mode) | Existing source fragments. | Preserves unified storage. | No extra root-producing path. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §8] |

SUB-PARTS: NONE

### C-CREATE.2 — Immutable base Creation Record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — A design-level base record containing only facts known at creation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Required creation_record_id, type_set, initial_status, provenance and schema_version; detection_record_ref is required for detector-created records. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Appends the base once; derives later confirmation, corrections, supersession and grouping from separate immutable events. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — A permanently provisional-at-creation base with exact source provenance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Store future confirmation, correction/supersession links or later view memberships on the base, or rewrite initial_status to confirmed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — An unverifiable current status is treated as provisional; uncertainty never permits a confirmation claim. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-CREATE.2.1 — creation_record_id: Requires stable creation identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-CREATE.2.2 — type_set: Requires non-empty five-type subset. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-CREATE.2.3 — initial_status: Requires immutable initial provisional status. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-CREATE.2.4 — Creation provenance: Requires original roots and exact spans. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-CREATE.2.5 — detection_record_ref: Detector-created bases require a detection reference. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-CREATE.2.6 — Creation schema_version: Requires schema version. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.3.2 — Source-grounded creation duplicate identity: Base duplication uses root plus exact span. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-CREATE — Unified Creation Store (§14, §7G creation-aware mode) | Creation identity/types/provenance. | Creates an immutable base. | Later facts remain events. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.2.3 — initial_status | Initial status. | Keeps provisional unchanged. | Current confirmation is derived. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-CREATE.4.4.1 — Creation correction and supersession links | Correction/supersession relation. | Stores them beside it. | Creation-time facts unchanged. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 4 · ACCEPTED | C-CREATE.9.1 — Larger creation record formation | Larger creation and all source refs. | Creates a proper base. | Confirmation remains a separate event. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: C-CREATE.2.1 — creation_record_id; C-CREATE.2.2 — type_set; C-CREATE.2.3 — initial_status; C-CREATE.2.4 — Creation provenance; C-CREATE.2.5 — detection_record_ref; C-CREATE.2.6 — Creation schema_version

### C-CREATE.2.1 — creation_record_id
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The required stable identity of the base Creation Record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The new record's identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Preserves creation_record_id across linked events and views. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — One stable record reference. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Replace it merely because a detector version changes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.3.2 — Source-grounded creation duplicate identity: Detector versions never change base duplicate identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.2 — Immutable base Creation Record | Record ID. | Binds the base. | One reference across events. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.8.1.1 — Provisional-use record identity | Creation record ID. | Binds the use to that record. | No second identity meaning. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.2.2 — type_set
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — A required non-empty subset of exactly design, idea, rule, name and decision. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — One or several applicable settled type values. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Carries multiple types on one record without making a separate base per type. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — A type set confined to the five-value vocabulary. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Add a sixth type, use an empty set or split one creation into type-specific databases. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Vocabulary expansion requires the separately governed future decision and versioned change. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.11.1 — Five-type expansion boundary: Only five settled values are currently permitted. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.2 — Immutable base Creation Record | Applicable type labels. | Stores one type set. | No per-type copies. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.2.3 — initial_status
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The required literal provisional on every new base Creation Record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The fact that the base is being created. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Stores provisional permanently on the immutable base. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Creation-time status distinct from the derived current status. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Change this field in place after confirmation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Later status is read from committed events, never from rewriting the base. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.2 — Immutable base Creation Record: Only creation-time facts belong on the immutable base. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.2 — Immutable base Creation Record | Creation-time state. | Stores provisional. | No later in-place flip. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.2.4 — Creation provenance
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Required provenance linking the originating root id(s) and exact fragment span(s) within them. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Existing source-root identities and offsets/locators sufficient to re-find the exact words. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Preserves source-grounded fragment identity and the original material's traceability. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — A re-findable source reference. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Replace the original fragments with an untraceable summary or a silent merged creation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Uncertain source identity cannot authorize a silent duplicate or fusion. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-CREATE.2.4.1 — Originating root references: Identifies the originating roots. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-CREATE.2.4.2 — Exact creation fragment spans: Identifies exact words within those roots. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.3.2 — Source-grounded creation duplicate identity: Base identity must remain source-grounded in exact roots and spans. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.2 — Immutable base Creation Record | Source provenance. | Preserves exact words by reference. | No lost source linkage. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.3.2 — Source-grounded creation duplicate identity | Source identities and exact words. | Derives structural identity. | No detector in key. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-CREATE.4.2.2 — Original adopted-fragment references | Original root/span references. | Preserves adopted-target identity. | No silent fusion. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 4 · ACCEPTED | C-CREATE.9 — Creation fragment relationships and larger works | Root IDs and spans. | Preserves source linkage. | No untraceable aggregation. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: C-CREATE.2.4.1 — Originating root references; C-CREATE.2.4.2 — Exact creation fragment spans

### C-CREATE.2.4.1 — Originating root references
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The root id(s) in required creation provenance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The actual existing originating roots. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — References each source root supporting the recorded creation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Traceable root identities. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Create new roots merely to store a creation or invent source references. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.2.4 — Creation provenance | Actual root IDs. | Carries provenance. | Existing sources stay distinct. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.2.4.2 — Exact creation fragment spans
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The exact fragment span(s) in required creation provenance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Offsets or locators within the identified roots. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Retains enough location detail to re-find the exact words. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Source-grounded fragment locations. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Erase original segmentation through silent fusion. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Ambiguous segmentation becomes a linked proposal/re-evaluation, not an invented identity match. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.3.6 — Detector disagreement and segmentation change: Changed segmentation needs explicit linkage. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.2.4 — Creation provenance | Offsets/locators. | Carries spans. | Re-findable fragments. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.2.5 — detection_record_ref
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — A base-record field required when the record is detector-created. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The detection record that produced the candidate. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Links the immutable base to its original detection provenance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — detection_record_ref. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Treat a newer detector version as a new base identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.3.1 — Creation detection record: Original detector provenance has a separate event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.2 — Immutable base Creation Record | Original detection event. | Links provenance. | No new base for version changes. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.2.6 — Creation schema_version
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The required base-record schema revision. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The record's design/form version. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Carries schema_version; exact serialization remains an implementation choice. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Version provenance for the base structure. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.2 — Immutable base Creation Record | Form revision. | Carries version. | Traceable structure. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.3 — Creation fragment detection mechanics
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

ALONE
- What it is: ACCEPTED — Broad provisional detection by the existing creation-aware Meaning Engine mode on live chat. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Takes in: ACCEPTED — Small fragments, partial thoughts, short phrases, unfinished sections and pieces that may later combine into a larger idea. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Does: ACCEPTED — Proposes provisional entries and records detection provenance; uses source-grounded identity to find an existing base or admit one new base. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Gives out: ACCEPTED — Preserved provisional fragments and linked detection/re-evaluation events. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Must never: ACCEPTED — Require a finished idea before broad capture, confirm through detection or invent a separate creation-filter engine. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Fails closed by: ACCEPTED — Detector disagreement or changed segmentation stays a linked proposal/re-evaluation; no silent duplication or fusion. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

TOGETHER
- Fed by: ACCEPTED — C-CREATE.3.1 — Creation detection record: Every detection carries method/source/span/basis. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.3.2 — Source-grounded creation duplicate identity: Requires source-grounded fragment identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.3.3 — Same-fragment compare-and-create: Concurrent same-fragment creation has one winner. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.3.4 — New-detector re-evaluation: New method on same candidate appends an event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.3.5 — Distinct fragment candidate: Separate base requires recorded distinct fragment identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.3.6 — Detector disagreement and segmentation change: Disagreement/segmentation change must stay explicit. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7G.7.1 — Broad provisional creation and traceable influence: Applies the already-owned broad-capture policy. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Gated by: ACCEPTED — C-CREATE.11.2 — Live-chat-only origination boundary: Current detection is live-chat only. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-CREATE — Unified Creation Store (§14, §7G creation-aware mode) | Live-chat fragments. | Resolves one base per fragment. | No detection-based confirmation. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] |
| 2 · ACCEPTED | C-CREATE.3.6 — Detector disagreement and segmentation change | Competing segmentation/result. | Records linked proposal. | No duplicate or fused base. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: C-CREATE.3.1 — Creation detection record; C-CREATE.3.2 — Source-grounded creation duplicate identity; C-CREATE.3.3 — Same-fragment compare-and-create; C-CREATE.3.4 — New-detector re-evaluation; C-CREATE.3.5 — Distinct fragment candidate; C-CREATE.3.6 — Detector disagreement and segmentation change

### C-CREATE.3.1 — Creation detection record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The append-only detection or re-evaluation record linked to a base Creation Record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Detector/method version, source root, fragment span and basis. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Records each actual detection with its method provenance; later detection of the same candidate links the existing base. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — A traceable detection event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Put detector/method version in the base's structural duplicate key. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Each operation follows the shared atomic record, duplicate and recovery rules. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-CREATE.3.1.1 — Detection method-version provenance: Carries the actual detector/method revision. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-CREATE.3.1.2 — Detection source-root reference: Carries the source root. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-CREATE.3.1.3 — Detection fragment-span reference: Carries the exact candidate span. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-CREATE.3.1.4 — Detection basis: Carries the actual detection basis. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.10.2 — Atomic creation event commitment: Detection event must commit atomically. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.2.5 — detection_record_ref | Detection reference. | Links that record. | Method version stays event provenance. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.3 — Creation fragment detection mechanics | Actual evaluation. | Appends detection provenance. | No unrecorded detector result. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-CREATE.4 — Append-only creation event family | Detector provenance. | Includes committed detection history. | No duplicate schema. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: C-CREATE.3.1.1 — Detection method-version provenance; C-CREATE.3.1.2 — Detection source-root reference; C-CREATE.3.1.3 — Detection fragment-span reference; C-CREATE.3.1.4 — Detection basis

### C-CREATE.3.1.1 — Detection method-version provenance
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The detector/method version carried on a detection or re-evaluation event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The exact method that performed the detection. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Preserves version provenance on the event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Re-evaluation provenance independent of base identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Use a version change to manufacture a second base record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.3.2 — Source-grounded creation duplicate identity: Version belongs to event provenance only. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.3.1 — Creation detection record | Method version. | Records provenance. | No identity reset. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.3.1.2 — Detection source-root reference
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The detection record's source root. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The existing root containing the candidate fragment. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Binds the detection to that source. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Source provenance on the event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Invent a source-root identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.3.1 — Creation detection record | Actual root identity. | Records source. | No fabricated provenance. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.3.1.3 — Detection fragment-span reference
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The detection record's exact candidate span. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The fragment location within its source root. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Binds the detection to the exact words it evaluated. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Span provenance on the event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Silently substitute different segmentation as the same candidate. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Changed segmentation uses a linked proposal/re-evaluation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.3.6 — Detector disagreement and segmentation change: Segmentation changes cannot silently replace the original. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.3.1 — Creation detection record | Source location. | Records span. | No silent resegmentation. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.3.1.4 — Detection basis
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The detection record's basis for proposing the fragment. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The actual grounded detection basis. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Records why the candidate was detected. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Inspectable detection provenance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Treat detection basis as confirmation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.3.1 — Creation detection record | Grounded reason. | Records basis. | No confirmation implied. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.3.2 — Source-grounded creation duplicate identity
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The base-record identity formed from source root id plus exact fragment span, independent of detector version. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The candidate's actual source-grounded fragment identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Resolves every same-fragment detection to the same base; only a recorded distinct fragment identity permits a separate base candidate. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Structural duplicate prevention. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Include detector/method version in this identity or silently equate genuinely different fragments. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Identity disagreement is recorded through linked proposal/re-evaluation without silent duplication or fusion. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-CREATE.2.4 — Creation provenance: Uses actual root-plus-span provenance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.3.6 — Detector disagreement and segmentation change: Disagreement or changed segmentation requires an explicit linked event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.2 — Immutable base Creation Record | Candidate identity. | Finds existing base first. | Detector-independent identity. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.2.1 — creation_record_id | Existing fragment key. | Retains stable base reference. | No replacement solely from version. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-CREATE.3 — Creation fragment detection mechanics | Root and exact span. | Checks duplication structurally. | No version-based new base. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 4 · ACCEPTED | C-CREATE.3.1.1 — Detection method-version provenance | New detector version. | Keeps base key unchanged. | No duplicate base. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 5 · ACCEPTED | C-CREATE.3.3 — Same-fragment compare-and-create | Concurrent same-key attempts. | Commits one winner. | Losers use existing base. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 6 · ACCEPTED | C-CREATE.3.4 — New-detector re-evaluation | Existing base identity. | Appends a new event only. | No rewritten detection. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 7 · ACCEPTED | C-CREATE.3.5 — Distinct fragment candidate | Different root/span. | Allows a separate base. | No version-only distinction. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 8 · ACCEPTED | C-CREATE.10.3 — Creation structural duplicate prevention | Candidate identity. | Checks existing base. | No version-created duplicate. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 9 · ACCEPTED | C-CREATE.2.4 — Creation provenance | Candidate provenance. | Checks the structural identity. | No silent duplicate or fusion from uncertainty. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.3.3 — Same-fragment compare-and-create
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Single-winner creation of a base for one source-grounded fragment identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Concurrent creation attempts naming the same root and exact span. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Atomically admits exactly one winner; every other attempt resolves to the existing base. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — One immutable base record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Rely on best-effort duplicate suppression or admit two bases for the same fragment. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Replays are structurally recognized and recorded as duplicate prevention. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.3.2 — Source-grounded creation duplicate identity: One source-grounded key admits one base. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.10.3 — Creation structural duplicate prevention: Duplicate prevention is structural and recorded. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.3 — Creation fragment detection mechanics | Competing attempts. | Compare-and-creates. | No double base. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.3.4 — New-detector re-evaluation
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — A later detection of the same exact candidate with a newer method/version. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The existing base and new detector provenance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Appends a detection/re-evaluation event linked to the existing record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — New event provenance without a new base. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Duplicate the base merely because the detector changed or overwrite the old detection. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — The same fragment identity remains authoritative. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.3.2 — Source-grounded creation duplicate identity: Same fragment retains its base across method versions. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.3 — Creation fragment detection mechanics | Existing base and new method. | Records re-evaluation. | No second base. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.3.5 — Distinct fragment candidate
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — A genuinely distinct candidate with a recorded distinct source-grounded fragment identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The different source root/span identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Gives that candidate a separate base under the same structural duplicate rule. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — A separately traceable provisional creation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Manufacture distinctness solely from detector version or silently merge candidates. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Unclear distinctness remains a linked proposal/re-evaluation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.3.2 — Source-grounded creation duplicate identity: Distinctness must be source-grounded and recorded. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.3 — Creation fragment detection mechanics | Different source candidate. | Preserves distinctness. | No fabricated duplication. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.3.6 — Detector disagreement and segmentation change
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — A disagreement or changed segmentation that needs explicit linkage to preserved fragments. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Competing detector results or proposed fragment boundaries. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Appends a linked proposal/re-evaluation event while preserving exact original fragments and their provenance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Visible unresolved interpretation of candidate relationships. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Silently duplicate, fuse, edit or absorb the originals. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — No silent base identity change or confirmation follows from disagreement. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.3 — Creation fragment detection mechanics: Detection uncertainty cannot silently alter records. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.2.4.2 — Exact creation fragment spans | Competing boundaries. | Preserves original spans. | No silent identity substitution. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.3 — Creation fragment detection mechanics | Competing results. | Links proposal/re-evaluation. | No silent fusion. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-CREATE.3.1.3 — Detection fragment-span reference | Different proposed span. | Uses linked re-evaluation. | Provenance preserved. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 4 · ACCEPTED | C-CREATE.3.2 — Source-grounded creation duplicate identity | Conflicting identity evidence. | Preserves uncertainty visibly. | No silent identity replacement. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.4 — Append-only creation event family
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Detection, confirmation, confirmation-proposal, challenge, correction, relationship-proposal and view-assignment records around an immutable base. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Actual later operations and their source/basis references. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Commits each event append-only as its own transaction with one operational record; current status and memberships derive from committed events. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Preserved event history without in-place changes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Add a parallel status-event truth competing with confirmation, or store later events on the base. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Recovery uses committed records; unverifiable confirmation reads provisional. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-CREATE.3.1 — Creation detection record: Reuses the same detection-event identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.10.2 — Atomic creation event commitment: Each event is an atomic append. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: ACCEPTED — C-CREATE.4.1 — Creation confirmation record: Confirmation has one canonical event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: ACCEPTED — C-CREATE.4.2 — Creation confirmation-proposal record: Possible later adoption is a proposal first. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: ACCEPTED — C-CREATE.4.3 — Creation challenge record: Challenges append beside prior history. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: ACCEPTED — C-CREATE.4.4 — Creation correction record: Corrections use new linked records. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: ACCEPTED — C-CREATE.4.5 — Creation relationship-proposal record: Relationships remain linked proposals. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: ACCEPTED — C-CREATE.4.6 — Creation view-assignment record: Grouping changes use assignment events. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-CREATE — Unified Creation Store (§14, §7G creation-aware mode) | Operation and basis. | Appends separate records. | No base overwrite. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.4.3 — Creation challenge record | Challenge basis. | Links existing history. | No rewrite. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-CREATE.4.4 — Creation correction record | Actual correction. | Preserves history. | No overwrite. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 4 · ACCEPTED | C-CREATE.6 — Derived creation current-status view | Seven event families. | Derives the current view. | No independent status store. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: C-CREATE.4.1 — Creation confirmation record; C-CREATE.4.2 — Creation confirmation-proposal record; C-CREATE.4.3 — Creation challenge record; C-CREATE.4.4 — Creation correction record; C-CREATE.4.5 — Creation relationship-proposal record; C-CREATE.4.6 — Creation view-assignment record

### C-CREATE.4.1 — Creation confirmation record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The committed event that is the one canonical source of a creation's confirmed status. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The creation, one permitted confirmation route and its actual basis. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Appends confirmation only through explicit words or a grounded later-adoption proposal that passed the accepted boundary. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — A canonical confirmation event read by the derived status view. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Create competing confirmation/status truth or alter the base's initial_status. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Unclear or competing evidence commits no confirmation; the proposal remains a proposal. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-CREATE.4.1.1 — Confirmation route: Records which legitimate route applied. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-CREATE.4.1.2 — Confirmation basis: Records actual confirmation basis. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.5 — Two-route creation confirmation gate: Only one of the two valid routes authorizes commit. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.4 — Append-only creation event family | Permitted route and basis. | Appends confirmation. | One source of confirmed status. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.5.1 — Explicit-confirmation commit | Explicit route and words. | Commits once. | Derived confirmed status. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-CREATE.5.3 — Validated-adoption confirmation commit | Accepted route/basis. | Appends event. | No parallel status truth. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 4 · ACCEPTED | C-CREATE.6.2 — Derived confirmed state | Verified event and basis. | Derives confirmed. | No parallel status event. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 5 · ACCEPTED | C-CREATE.6.4 — Status-relevant challenge and correction linkage | Linked status-relevant history. | Keeps one canonical source. | No silent base change. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: C-CREATE.4.1.1 — Confirmation route; C-CREATE.4.1.2 — Confirmation basis

### C-CREATE.4.1.1 — Confirmation route
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The confirmation record's route: explicit Ness confirmation or later clear demonstrated adoption. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The actual route that justified this event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Records which of the two permitted routes applies. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Traceable confirmation-route provenance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Add time, repeated use, confidence or another automatic route. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — No permitted route means no confirmation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.5 — Two-route creation confirmation gate: The vocabulary has exactly two legitimate routes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.4.1 — Creation confirmation record | Explicit or later-adoption route. | Carries route. | No third pathway. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.4.1.2 — Confirmation basis
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The confirmation record's referenced words or accepted later-adoption basis. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Ness's explicit words, or exact later root/action and original-fragment evidence from the validated proposal. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Retains the actual basis with the confirmation operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Grounded traceable confirmation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Substitute a mouth assertion or unrelated evidence. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Unclear/competing basis leaves the creation provisional. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.5 — Two-route creation confirmation gate: The basis must satisfy its actual route. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.4.1 — Creation confirmation record | Referenced evidence. | Carries basis. | No confidence substitute. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.4.2 — Creation confirmation-proposal record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — A grounded proposal that later words/actions clearly adopt an existing creation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Exact later roots or recorded actions and exact original fragments claimed as adopted. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Preserves the proposal and its evidence for independent acceptance before any confirmation event is committed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — A proposal, not confirmed status. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Let the proposing mouth confirm itself or equate a recorded proposal with acceptance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Unclear or competing evidence leaves the creation provisional and the proposal recorded as a proposal. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-CREATE.4.2.1 — Later adoption evidence references: Requires exact later roots/actions. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-CREATE.4.2.2 — Original adopted-fragment references: Requires exact original fragments. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.5.2 — Later-adoption proposal evaluation: A proposal cannot confirm before acceptance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.4 — Append-only creation event family | Exact later/original evidence. | Appends proposal. | No premature confirmation. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.5.2 — Later-adoption proposal evaluation | Original fragments and later roots/actions. | Checks the claimed adoption. | Proposal alone changes no status. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: C-CREATE.4.2.1 — Later adoption evidence references; C-CREATE.4.2.2 — Original adopted-fragment references

### C-CREATE.4.2.1 — Later adoption evidence references
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — References to the exact later roots or recorded actions claimed to demonstrate adoption. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Actual later evidence. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Makes the asserted adoption relation re-findable. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Later-side grounding for the proposal. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Replace evidence with model confidence or repeated retrieval counts. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Unclear evidence does not confirm. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.5.2 — Later-adoption proposal evaluation: Later evidence must support clear adoption. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.4.2 — Creation confirmation-proposal record | Recorded later evidence. | Links later side. | No invented adoption. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.4.2.2 — Original adopted-fragment references
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — References to the exact original creation fragments the proposal claims are adopted. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The preserved original fragments and provenance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Connects later evidence to the particular source material at issue. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Original-side grounding for the proposal. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Silently fuse fragments or claim adoption of unspecified material. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Unclear/competing linkage leaves the proposal unconfirmed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-CREATE.2.4 — Creation provenance: Reuses exact original fragment provenance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.5.2 — Later-adoption proposal evaluation: Original-fragment linkage must support the validated adoption claim. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.4.2 — Creation confirmation-proposal record | Original provenance. | Links original side. | No unspecified adoption target. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.4.3 — Creation challenge record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — An append-only challenge event linked to the creation and any relevant canonical confirmation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — A later challenge to the recorded creation or its status-relevant basis. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Records the challenge beside prior history. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — A linked challenge without replacing the confirmation source. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Rewrite earlier records or create a competing status-event truth. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.4 — Append-only creation event family: A challenge is append-only and cannot compete with confirmation truth. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.4 — Append-only creation event family | Challenge and related refs. | Records linkage. | No competing status truth. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.4.4 — Creation correction record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — A new linked correction event, including correction/supersession links outside the base. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Corrected material and the prior records it concerns. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Appends the new linked record and retains the original. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Traceable correction history. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Rewrite, absorb or silently delete prior creation records. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — A correction does not become a competing canonical confirmation source. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.4 — Append-only creation event family: Corrections are new linked records. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: ACCEPTED — C-CREATE.4.4.1 — Creation correction and supersession links: Stores correction/supersession links outside the base. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.4 — Append-only creation event family | Corrected material and prior refs. | Appends correction. | No rewrite. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: C-CREATE.4.4.1 — Creation correction and supersession links

### C-CREATE.4.4.1 — Creation correction and supersession links
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Links that connect new corrections or superseding material to earlier creation history. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The relevant prior and new record identities. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Stores those links only in append-only correction/challenge records. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Accretive linkage beside the immutable base. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Insert later correction/supersession links into the original base record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.2 — Immutable base Creation Record: Later links cannot live on the immutable base. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.4.4 — Creation correction record | Prior and new identities. | Appends linkage. | Earlier base untouched. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.4.5 — Creation relationship-proposal record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

ALONE
- What it is: ACCEPTED — An append-only proposal of a possible relationship among preserved creation fragments. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Takes in: ACCEPTED — The original fragment references and proposed relationship. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Does: ACCEPTED — Records the possibility with linkage; a larger creation is represented by a new record with all original fragments preserved. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Gives out: ACCEPTED — Traceable possible relationships. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Must never: ACCEPTED — Silently fuse original fragments into an adopted creation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Fails closed by: ACCEPTED — A relationship proposal alone does not confirm any fragment. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.9 — Creation fragment relationships and larger works: Possible relations never silently adopt/fuse fragments. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.4 — Append-only creation event family | Fragment refs and possible relation. | Records possibility. | No silent fusion. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.9 — Creation fragment relationships and larger works | Fragment references and relation. | Records the possibility. | No automatic adoption. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.4.6 — Creation view-assignment record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The append-only event assigning project/category view membership over the one store. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — A creation record and actual grouping/view assignment. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Records the assignment as one transaction; the membership view derives from these events. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Current grouping membership with history. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Put later membership on the immutable base or create a separate category database. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Recovery uses committed assignment events only. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.7 — Creation views over one store: Memberships are views over one store. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.4 — Append-only creation event family | Creation and grouping. | Appends assignment. | No base membership mutation. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.6.3 — Derived creation view memberships | Committed view assignments. | Computes current grouping. | No new store. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-CREATE.7.2 — Project and category creation views | View-assignment events. | Derives memberships. | No future facts on base. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.5 — Two-route creation confirmation gate
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

ALONE
- What it is: ACCEPTED — Exactly two ways to commit a canonical confirmation: explicit confirmation or clearly demonstrated later adoption. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Takes in: ACCEPTED — An actual explicit statement or a grounded later-adoption proposal. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Does: ACCEPTED — Directly records explicit confirmation; requires the applicable accepted B24 validation/grounding boundary for later-adoption proposals. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Gives out: ACCEPTED — A justified canonical confirmation or a still-provisional creation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Must never: ACCEPTED — Add any route based on time, repetition, retrieval, use, model output or confidence. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Fails closed by: ACCEPTED — Ambiguous or competing evidence remains provisional, with the proposal preserved. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.5.1 — Explicit-confirmation commit: Explicit words support direct confirmation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.5.2 — Later-adoption proposal evaluation: Later adoption requires grounded validation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.5.4 — Confirmation ambiguity preservation: Unclear/competing evidence blocks confirmation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.5.5 — Forbidden automatic confirmation inputs: Excluded substitutes never feed status. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Changes: ACCEPTED — C-CREATE.5.3 — Validated-adoption confirmation commit: Passed adoption proposal may commit confirmation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-CREATE — Unified Creation Store (§14, §7G creation-aware mode) | Explicit words or validated adoption. | Controls confirmation commit. | No automatic adoption. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.4.1 — Creation confirmation record | Actual evidence. | Checks confirmation authority. | No automatic confirmation. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-CREATE.4.1.1 — Confirmation route | Recorded route. | Preserves authority. | No time/use route. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 4 · ACCEPTED | C-CREATE.4.1.2 — Confirmation basis | Evidence references. | Checks grounding/explicit words. | No unrelated evidence. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 5 · ACCEPTED | C-CREATE.5.4 — Confirmation ambiguity preservation | Competing evidence. | Keeps provisional. | No timer-based resolution. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 6 · ACCEPTED | C-CREATE.5.5 — Forbidden automatic confirmation inputs | Excluded input. | Prevents status use. | No third pathway. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] |
| 7 · ACCEPTED | C-CREATE.9.1 — Larger creation record formation | Actual confirmation evidence. | Requires canonical event. | Aggregation never confirms itself. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: C-CREATE.5.1 — Explicit-confirmation commit; C-CREATE.5.2 — Later-adoption proposal evaluation; C-CREATE.5.3 — Validated-adoption confirmation commit; C-CREATE.5.4 — Confirmation ambiguity preservation; C-CREATE.5.5 — Forbidden automatic confirmation inputs

### C-CREATE.5.1 — Explicit-confirmation commit
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The direct confirmation route based on Ness's explicit words. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The words that explicitly confirm the creation, referenced rather than replaced by a model assertion. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Records confirmation with this route and its basis. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — A committed canonical confirmation event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Treat silence, repetition or an assistant's assertion as Ness's explicit confirmation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Without actual explicit confirmation this route authorizes nothing. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-14.3.2 — Explicit confirmation route: Consumes the existing explicit-confirmation route. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Changes: ACCEPTED — C-CREATE.4.1 — Creation confirmation record: Appends the canonical confirmation event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.5 — Two-route creation confirmation gate | Ness's actual confirmation. | Commits with route/basis. | No inferred statement. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.5.2 — Later-adoption proposal evaluation
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The grounded evaluation of later words/actions as clear adoption of exact original fragments. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — A confirmation proposal with exact later roots/recorded actions and exact original creation-fragment references. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Applies the accepted B24 validation/grounding boundary before any confirmation commit. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — An accepted basis for confirmation or a preserved unconfirmed proposal. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Bypass independent acceptance or confirm unclear/competing evidence. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Unclear or competing evidence leaves the creation provisional. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-CREATE.4.2 — Creation confirmation-proposal record: Evaluates the recorded proposal and its two-sided evidence. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: DESIGNED — C-14.3.3 — Clear demonstrated-adoption route: Consumes the existing clear-demonstrated-adoption route. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Gated by: DESIGNED — C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): Applicable accepted B24 grounding must pass before confirmation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.4.2 — Creation confirmation-proposal record | Complete grounded proposal. | Waits for boundary result. | Proposal remains distinct. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.4.2.1 — Later adoption evidence references | Exact later roots/actions. | Tests grounding. | Unclear stays provisional. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-CREATE.5 — Two-route creation confirmation gate | Exact later/original refs. | Evaluates proposal. | No self-approved adoption. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 4 · ACCEPTED | C-CREATE.5.3 — Validated-adoption confirmation commit | Acceptance result. | Commits confirmation. | No pre-validation status change. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 5 · ACCEPTED | C-CREATE.4.2.2 — Original adopted-fragment references | Exact original refs. | Checks the evidence relation. | Unclear/competing linkage cannot confirm. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.5.3 — Validated-adoption confirmation commit
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The event append after a later-adoption proposal passes the applicable grounding boundary. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The accepted proposal and its exact evidence. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Commits the canonical confirmation record with route and basis. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Confirmed status derivable from one source. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Write confirmation before the required validation passes or mutate initial_status. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Without a passed proposal no route-B confirmation commits. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.5.2 — Later-adoption proposal evaluation: Only a passed adoption proposal authorizes the event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: ACCEPTED — C-CREATE.4.1 — Creation confirmation record: Uses the one canonical confirmation record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.5 — Two-route creation confirmation gate | Accepted basis. | Appends canonical event. | No base overwrite. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.5.4 — Confirmation ambiguity preservation
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

ALONE
- What it is: ACCEPTED — The no-confirmation outcome for unclear or competing adoption evidence. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Takes in: ACCEPTED — Ambiguous words/actions or conflicting evidence. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Does: ACCEPTED — Keeps the creation provisional and preserves the proposal as a proposal. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Gives out: ACCEPTED — Honest provisional status without a forced decision. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Must never: ACCEPTED — Resolve ambiguity by time, frequency or confidence. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Fails closed by: ACCEPTED — The record may remain provisional forever; nothing is destroyed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.5 — Two-route creation confirmation gate: Ambiguity satisfies neither required confirmation route. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.5 — Two-route creation confirmation gate | Ambiguity. | Preserves provisional status. | No forced decision. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.5.5 — Forbidden automatic confirmation inputs
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]

ALONE
- What it is: ACCEPTED — Structurally excluded substitutes for either legitimate confirmation route. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Takes in: ACCEPTED — Elapsed time, repetition, retrieval frequency, system use, model output, mouth assertion, scores or confidence. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Does: ACCEPTED — Uses none of these to feed a status event; the store does not count uses to establish confirmation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Gives out: ACCEPTED — Confirmation independent of popularity or model self-belief. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Must never: ACCEPTED — Install a use counter, score or confidence input that feeds creation status. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Fails closed by: ACCEPTED — Without either valid route status remains provisional. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.5 — Two-route creation confirmation gate: Neither legitimate route is a count or confidence value. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.5 — Two-route creation confirmation gate | Time/use/repetition/confidence. | Keeps them out of confirmation. | No popularity-based truth. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] |

SUB-PARTS: NONE

### C-CREATE.6 — Derived creation current-status view
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — A view calculated from the immutable base and append-only events, covering confirmation and current view memberships. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Committed detection, confirmation, proposal, challenge, correction, relationship and view-assignment history. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Derives confirmed only from a committed confirmation record; all other cases derive provisional; current memberships derive from view-assignment records. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Current status and grouping without mutable base truth. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Store an independently competing status source or rewrite base initial_status. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — An unverifiable status reads as provisional. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-CREATE.6.1 — Derived provisional state: Uses provisional when no canonical confirmation is established. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-CREATE.6.2 — Derived confirmed state: Uses confirmed only from its canonical event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-CREATE.6.3 — Derived creation view memberships: Uses assignment events for current memberships. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-CREATE.4 — Append-only creation event family: Reads committed append-only event history. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.6.4 — Status-relevant challenge and correction linkage: Status-relevant corrections link rather than compete. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.6.5 — Unverifiable creation-status handling: Unverifiable status reads provisional. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-CREATE — Unified Creation Store (§14, §7G creation-aware mode) | Event history. | Derives status and membership. | No competing mutable truth. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.6.1 — Derived provisional state | Current event evidence. | Retains status. | No inference from time. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-CREATE.6.5 — Unverifiable creation-status handling | Unverifiable state. | Reads provisional. | No confidence-based repair. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 4 · ACCEPTED | C-CREATE.7 — Creation views over one store | Current view results. | Presents correct grouping. | No base rewrite. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 5 · ACCEPTED | C-CREATE.8.1.2 — Creation status at use time | Current event-backed view. | Carries time-of-use status. | No retroactive relabeling. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 6 · ACCEPTED | C-CREATE.6.3 — Derived creation view memberships | Durable event set. | Derives the current view. | No uncommitted grouping claim. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 7 · ACCEPTED | C-7I.8 — Existing creation-view presentation interface | Creation records and their actual derived status/view memberships. | Supplies derived creation status. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [MAP C-CREATE] |

SUB-PARTS: C-CREATE.6.1 — Derived provisional state; C-CREATE.6.2 — Derived confirmed state; C-CREATE.6.3 — Derived creation view memberships; C-CREATE.6.4 — Status-relevant challenge and correction linkage; C-CREATE.6.5 — Unverifiable creation-status handling

### C-CREATE.6.1 — Derived provisional state
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Current status where no committed confirmation record is established. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Base provisional status and available committed event history. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Keeps the creation provisional while preserving its history and permitted traceable uses. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — provisional, with no expiry requirement. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Treat passage of time or use as a state transition. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Unverifiable confirmation also reads provisional. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.6 — Derived creation current-status view: Absence of verified confirmation means provisional. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.6 — Derived creation current-status view | Committed history. | Derives provisional. | No expiry promotion. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.7.1 — Ideas-in-progress view | Provisional records. | Keeps them available. | No implied adoption. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.6.2 — Derived confirmed state
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Current status supported by the one canonical committed confirmation event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — A confirmation record from one of the two valid routes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Derives confirmed without editing the base record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — confirmed with accessible route/basis provenance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Accept a parallel contradictory status-event truth. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Unverifiable status is not asserted confirmed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.4.1 — Creation confirmation record: One committed confirmation is the canonical source. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.6 — Derived creation current-status view | Verified confirmation. | Derives confirmed. | No competing truth. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.6.3 — Derived creation view memberships
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Current project/category memberships derived from committed view-assignment events. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Append-only assignment history. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Computes the grouping view over the same store. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Current memberships plus their preserved history. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Rewrite the base or split physical stores by category. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Only committed events support the derived membership state. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-CREATE.4.6 — Creation view-assignment record: Membership truth comes from assignment events. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.6 — Derived creation current-status view: Only committed assignment history supports current membership. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.6 — Derived creation current-status view | Grouping history. | Derives memberships. | No mutable base grouping. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.6.4 — Status-relevant challenge and correction linkage
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Challenges and corrections link to canonical confirmation rather than competing with it. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — New challenge/correction events and existing confirmation references. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Retains the linked history while keeping confirmation as the single source of confirmed status. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Accretive status-relevant context. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Invent a parallel status event or silently revoke/rewrite the base from a challenge alone. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Unverifiable current status reads provisional. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.4.1 — Creation confirmation record: Challenges/corrections do not become competing confirmation truth. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.6 — Derived creation current-status view | Challenge/correction refs. | Preserves canonical source. | No silent rewriting. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.6.5 — Unverifiable creation-status handling
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The protective status-read result when confirmation cannot be verified. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Unreadable, uncertain or otherwise unverifiable status evidence. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Reads the creation as provisional without asserting a new confirmation fact. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — A provisional use context and honest uncertainty. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Guess confirmed status or mutate records to repair uncertainty. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Provisional status must remain visible and logged in any permitted use. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.6 — Derived creation current-status view: Only verified confirmation supports confirmed status. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.6 — Derived creation current-status view | Uncertain evidence. | Uses protective status. | No guessed confirmed state. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.8.1.2 — Creation status at use time | Uncertain status evidence. | Carries provisional. | No guessed confirmation. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.7 — Creation views over one store
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

ALONE
- What it is: ACCEPTED — Ideas-in-progress and project/category views over connected creation records. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Takes in: ACCEPTED — Derived status, assignment events and retained history. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Does: ACCEPTED — Keeps a clear provisional area while allowing multiple groupings over the one store. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Gives out: ACCEPTED — Navigable creation views without extra databases. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Must never: ACCEPTED — Split by project/type or hide the provisional status of unfinished ideas. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Fails closed by: ACCEPTED — Provisional records remain available with their history and status protections. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

TOGETHER
- Fed by: ACCEPTED — C-CREATE.6 — Derived creation current-status view: Uses derived status and membership. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.10.9 — Creation access ordering: Creation views remain subject to access authorization. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: ACCEPTED — C-CREATE.7.1 — Ideas-in-progress view: Keeps a clear provisional area with history. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Changes: ACCEPTED — C-CREATE.7.2 — Project and category creation views: Groups records as project/category views. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-CREATE — Unified Creation Store (§14, §7G creation-aware mode) | Status and assignments. | Provides grouped/provisional access. | No separate databases. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.4.6 — Creation view-assignment record | Grouping assignment. | Appends event. | No separate database. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-7I.8 — Existing creation-view presentation interface | Creation records and their actual derived status/view memberships. | Supplies the one-store view contract. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [MAP C-CREATE] |

SUB-PARTS: C-CREATE.7.1 — Ideas-in-progress view; C-CREATE.7.2 — Project and category creation views

### C-CREATE.7.1 — Ideas-in-progress view
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

ALONE
- What it is: ACCEPTED — A view filtered to provisional creations plus their history. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Takes in: ACCEPTED — Records whose current status is provisional. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Does: ACCEPTED — Keeps small and unfinished ideas in a clear provisional-creation area. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Gives out: ACCEPTED — Persistent ideas-in-progress availability. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Must never: ACCEPTED — Treat this area as a second store or imply that availability means adoption. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Fails closed by: ACCEPTED — Ambiguous material remains provisional even indefinitely. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.6.1 — Derived provisional state: Filter uses actual provisional status plus history. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.7 — Creation views over one store | Provisional creations. | Filters the one store. | No loss of small ideas. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] |
| 2 · ACCEPTED | C-7I.8 — Existing creation-view presentation interface | Creation records and their actual derived status/view memberships. | Supplies ideas in progress. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [MAP C-CREATE] |

SUB-PARTS: NONE

### C-CREATE.7.2 — Project and category creation views
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [V10 §7G / CREATION-AWARE MODE]

ALONE
- What it is: ACCEPTED — Groupings such as N.H project, personal and work over the same connected store. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [V10 §7G / CREATION-AWARE MODE]
- Takes in: ACCEPTED — Committed view-assignment records. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [V10 §7G / CREATION-AWARE MODE]
- Does: ACCEPTED — Presents grouped access without moving the underlying creation into a separate database. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [V10 §7G / CREATION-AWARE MODE]
- Gives out: ACCEPTED — Project/category membership views. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [V10 §7G / CREATION-AWARE MODE]
- Must never: ACCEPTED — Create isolated stores for categories or put future assignments into the base record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [V10 §7G / CREATION-AWARE MODE]
- Fails closed by: ACCEPTED — Only committed assignment history supplies the derived memberships. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [V10 §7G / CREATION-AWARE MODE]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.4.6 — Creation view-assignment record: Grouping requires committed assignment history. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.7 — Creation views over one store | Committed assignments. | Presents grouping. | No per-category database. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7I.8 — Existing creation-view presentation interface | Creation records and their actual derived status/view memberships. | Supplies project/category views. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [MAP C-CREATE] |

SUB-PARTS: NONE

### C-CREATE.8 — Traceable provisional creation influence
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]

ALONE
- What it is: ACCEPTED — Permission for relevant provisional creations to influence wider retrieval, reasoning, answers and Computed View under carried-status rules. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Takes in: ACCEPTED — A provisional record, its status at use time and the consuming operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Does: ACCEPTED — Requires the operation's own record to carry provisional_material_used; every influence is visible as provisional in the output context and traceable in that record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Gives out: ACCEPTED — Useful but explicitly provisional influence. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Must never: ACCEPTED — Present it as confirmed fact, adopted rule, final decision or settled creation, or let influence silently confirm it. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Fails closed by: ACCEPTED — Without visible carried status and operation trace, the wider use is not permitted. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]

TOGETHER
- Fed by: ACCEPTED — C-CREATE.8.1 — provisional_material_used: Every use needs its own operation entry. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.8.2 — Provisional influence in retrieval: Retrieval influence must carry status and trace. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Gated by: ACCEPTED — C-CREATE.8.3 — Provisional influence in reasoning: Reasoning influence must carry status and trace. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Gated by: ACCEPTED — C-CREATE.8.4 — Provisional influence in answers: Answer influence must carry status and trace. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Gated by: ACCEPTED — C-CREATE.8.5 — Provisional influence in Computed View: Computed View influence must carry status and trace. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Gated by: ACCEPTED — C-7G.7.1 — Broad provisional creation and traceable influence: Reuses the existing broad-capture and traceable-influence policy. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Gated by: ACCEPTED — C-CREATE.10.9 — Creation access ordering: Status permission never bypasses access authorization. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-CREATE — Unified Creation Store (§14, §7G creation-aware mode) | Consumer and record status. | Constrains every influence. | No silent confirmation. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)] |
| 2 · ACCEPTED | C-CREATE.8.1 — provisional_material_used | Use entry and output context. | Requires both protections. | No silent influence. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-CREATE.8.2 — Provisional influence in retrieval | Provisional context. | Enforces both conditions. | No silent influence. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 4 · ACCEPTED | C-CREATE.8.3 — Provisional influence in reasoning | Provisional input and trace. | Carries context honestly. | No fact relabeling. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 5 · ACCEPTED | C-CREATE.8.4 — Provisional influence in answers | Permitted material. | Carries status and trace. | No hidden dependency on a draft. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 6 · ACCEPTED | C-CREATE.8.5 — Provisional influence in Computed View | Provisional record. | Preserves marked influence. | No repeated-use confirmation. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: C-CREATE.8.1 — provisional_material_used; C-CREATE.8.2 — Provisional influence in retrieval; C-CREATE.8.3 — Provisional influence in reasoning; C-CREATE.8.4 — Provisional influence in answers; C-CREATE.8.5 — Provisional influence in Computed View

### C-CREATE.8.1 — provisional_material_used
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]

ALONE
- What it is: ACCEPTED — The entry required inside the consuming operation's own §0B record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Takes in: ACCEPTED — The creation record id and status at use time. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Does: ACCEPTED — Binds each provisional influence to its actual consumer operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Gives out: ACCEPTED — A traceable record of provisional material used. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Must never: ACCEPTED — Create an unrelated parallel log in place of the consumer's entry or drop status from output context. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]
- Fails closed by: ACCEPTED — A use without this entry cannot satisfy the permitted-influence boundary. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)]

TOGETHER
- Fed by: ACCEPTED — C-CREATE.8.1.1 — Provisional-use record identity: Identifies the exact influencing creation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-CREATE.8.1.2 — Creation status at use time: Carries actual status at use time. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.8 — Traceable provisional creation influence: Trace alone is insufficient without visible provisional context. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.8 — Traceable provisional creation influence | Record ID and status-at-use. | Traces influence. | No unlogged contribution. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.10.8 — Creation operational logging | Record ID and status. | Traces actual influence. | No separate unbound log. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-CREATE.8.1.1 — Provisional-use record identity | Record ID. | Binds the actual source. | No untraceable use. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 4 · ACCEPTED | C-7M.12 — Computed View provisional-creation influence | A provisional creation record used by an otherwise authorized view operation, its identity and status at use time. | Supplies `provisional_material_used`. | Nothing in this card. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 5 · ACCEPTED | C-LMAC.13.6 — Provisional creation-use carriage | The record identity and its provisional status at use time. | Supplies canonical provisional_material_used entry. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §14] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9] |

SUB-PARTS: C-CREATE.8.1.1 — Provisional-use record identity; C-CREATE.8.1.2 — Creation status at use time

### C-CREATE.8.1.1 — Provisional-use record identity
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The creation record id in provisional_material_used. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The exact record whose material influenced the operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Identifies that creation in the consumer's trace. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Source-linked use provenance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Substitute an untraceable fragment summary for record identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-CREATE.2.1 — creation_record_id: Reuses the existing stable base identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.8.1 — provisional_material_used: Permitted influence requires the exact creation identity in its entry. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.8.1 — provisional_material_used | Record identity. | Stores it in the operation entry. | Traceable source. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7M.12 — Computed View provisional-creation influence | A provisional creation record used by an otherwise authorized view operation, its identity and status at use time. | Supplies used record identity. | Nothing in this card. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.8.1.2 — Creation status at use time
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The actual status carried by provisional_material_used for that use. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The creation's status when the consumer used it. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Preserves provisional status in the operation trace and output context. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Time-of-use status provenance, unaffected by later confirmation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Relabel the earlier influence as confirmed merely because a later event confirms the record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Unverifiable status is used only as provisional. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-CREATE.6 — Derived creation current-status view: Uses the actual derived status when material is consumed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.6.5 — Unverifiable creation-status handling: Unverifiable status cannot be asserted confirmed at use time. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.8.1 — provisional_material_used | Current provisional status. | Stores it with identity. | Historical use remains honest. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7M.12 — Computed View provisional-creation influence | A provisional creation record used by an otherwise authorized view operation, its identity and status at use time. | Supplies creation status at use time. | Nothing in this card. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.8.2 — Provisional influence in retrieval
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Relevant retrieval use subject to the full provisional-status and trace rule. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — A permitted provisional creation and retrieval operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Carries status in retrieved/output context and records its identity/status in the operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — Explicitly provisional retrieval context. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Treat retrieval frequency as confirmation or silently admit creation records to RM-CR-01 [proposed]'s root-only candidates. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Use requires the owning retrieval mode and all access/status conditions. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.8 — Traceable provisional creation influence: Every retrieval use needs visible status and operation trace. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: DESIGNED — C-7F — Context Retrieval (§7F): Existing retrieval declaration controls candidate scope. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.8 — Traceable provisional creation influence | Retrieval operation. | Uses marked material. | No confirmation by frequency. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] |

SUB-PARTS: NONE

### C-CREATE.8.3 — Provisional influence in reasoning
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

ALONE
- What it is: ACCEPTED — Reasoning use of relevant provisional creation material with its actual status. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Takes in: ACCEPTED — The creation and reasoning operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Does: ACCEPTED — Preserves status in the reasoning/output context and logs the influence. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Gives out: ACCEPTED — Grounded provisional reasoning context. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Must never: ACCEPTED — Treat the fragment as an adopted rule or established fact. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Fails closed by: ACCEPTED — Uncarried or untraceable influence is not permitted. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.8 — Traceable provisional creation influence: Reasoning must preserve actual status. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.8 — Traceable provisional creation influence | Reasoning operation. | Preserves provisional context. | No adopted-rule relabeling. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] |

SUB-PARTS: NONE

### C-CREATE.8.4 — Provisional influence in answers
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

ALONE
- What it is: ACCEPTED — Answer generation that may use relevant provisional creations honestly. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Takes in: ACCEPTED — Permitted material and its status at use time. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Does: ACCEPTED — Makes its provisional nature visible in output context and records the actual use. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Gives out: ACCEPTED — An answer with traceable provisional influence. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Must never: ACCEPTED — Present the material as a settled creation or final decision. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Fails closed by: ACCEPTED — The answer cannot silently rely on unmarked provisional material. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.8 — Traceable provisional creation influence: Answers must expose provisional influence in context. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.8 — Traceable provisional creation influence | Answer operation. | Makes provisional nature visible. | No settled-creation relabeling. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] |

SUB-PARTS: NONE

### C-CREATE.8.5 — Provisional influence in Computed View
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

ALONE
- What it is: ACCEPTED — Computed View use of relevant provisional creations under the same status protections. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Takes in: ACCEPTED — Eligible creation material and the view operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Does: ACCEPTED — Carries provisional status in the view context and its operation record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Gives out: ACCEPTED — A traceable provisional contribution to the computed result. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Must never: ACCEPTED — Promote a fragment to fact through repeated inclusion in the view. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Fails closed by: ACCEPTED — The consuming view must satisfy the carried-status and trace condition. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.8 — Traceable provisional creation influence: View contribution has the same carried-status boundary. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: DESIGNED — C-7M — Computed View (§7M): May contribute only relevant marked provisional material. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.8 — Traceable provisional creation influence | View operation. | Preserves status in context. | No silent fact promotion. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] |
| 2 · ACCEPTED | C-7M.12 — Computed View provisional-creation influence | A provisional creation record used by an otherwise authorized view operation, its identity and status at use time. | Supplies the accepted view-influence interface. | Nothing in this card. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 3 · DESIGNED | C-7M — Computed View (§7M) | Permitted roots, readings, tellings, clashes, Ness response events, Person-Box links, themes, Living State and world-model references, and safe metadata-only pre-ingest references. | Supplies relevant marked provisional influence within its accepted boundary. | Nothing in this card. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [V10 §7M] [MAP C-7M] |

SUB-PARTS: NONE

### C-CREATE.9 — Creation fragment relationships and larger works
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

ALONE
- What it is: ACCEPTED — Explicit relations among fragments without erasing the original pieces. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Takes in: ACCEPTED — Preserved fragments, relationship proposals and any larger adopted creation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Does: ACCEPTED — Keeps possible relations as linked proposal records; represents a larger creation as a new record referencing all source fragments. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Gives out: ACCEPTED — Connected original and larger creations with intact provenance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Must never: ACCEPTED — Silently fuse, edit or absorb original fragments. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]
- Fails closed by: ACCEPTED — A proposed relation alone never confers adoption or confirmation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.2.4 — Creation provenance: All original fragments retain exact provenance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: ACCEPTED — C-CREATE.9.1 — Larger creation record formation: Larger creations use a new provenance-linked record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: ACCEPTED — C-CREATE.4.5 — Creation relationship-proposal record: Possible relations remain linked proposal events. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-CREATE — Unified Creation Store (§14, §7G creation-aware mode) | Relationships and source refs. | Keeps new records linked. | No silent fusion. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.4.5 — Creation relationship-proposal record | Proposed relationship. | Preserves originals. | No automatic confirmation. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: C-CREATE.9.1 — Larger creation record formation

### C-CREATE.9.1 — Larger creation record formation
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Formation of a new record for a larger creation, preserving every source fragment. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — All source-fragment provenance and the legitimate evidence supporting the larger creation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Creates a new base with references to all original fragments; confirmed status still derives from its canonical confirmation event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — A distinct larger record beside untouched originals. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Silently fuse originals or create a base whose initial_status is confirmed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Adoption still requires one of the two confirmation routes; source uncertainty cannot be hidden by aggregation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.2 — Immutable base Creation Record: Every new base still has immutable initial provisional status. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.5 — Two-route creation confirmation gate: Larger adopted status uses the same two routes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.9 — Creation fragment relationships and larger works | All original fragments. | Preserves separate originals. | No fusion or absorption. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.10 — Creation operation and recovery rules
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The shared accepted operation spine applied to creation, confirmation, correction/challenge, relationship proposal, view assignment and influence use. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Stable operation identity, structural keys, exact source/event references and committed state. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Commits each state change atomically with its append-only record; prevents duplicates structurally, uses bounded retry, and recovers only durable unfinished work. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — One recorded real operation and preserved prior completion. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Reconstruct missing evidence, duplicate committed effects or treat logs as truth votes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Protective uncertainty admits no unverified change and claims no false completion; unverifiable creation status reads provisional. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.10.1 — Creation operation identity: Each real operation has stable identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.10.2 — Atomic creation event commitment: State change and record commit atomically. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.10.3 — Creation structural duplicate prevention: Duplicate prevention is structural. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.10.4 — Creation bounded retry consumption: Retry follows accepted class and value bounds. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.10.5 — Creation crash recovery: Crash recovery uses committed state only. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.10.6 — Creation partial-completion recovery: Partial recovery preserves completed records. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.10.7 — Creation protective failure handling: Uncertainty keeps the protective outcome. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.10.9 — Creation access ordering: Access observes privacy before relevance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: ACCEPTED — C-CREATE.10.8 — Creation operational logging: Each real operation is logged once. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-CREATE — Unified Creation Store (§14, §7G creation-aware mode) | Durable operation evidence. | Commits and recovers under owned rules. | No false completion. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.10.1 — Creation operation identity | Stable operation reference. | Preserves lineage. | No new ID to repeat an effect. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-CREATE.10.2 — Atomic creation event commitment | Event and transaction. | Commits both together. | No claimed completion without record. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 4 · ACCEPTED | C-CREATE.10.3 — Creation structural duplicate prevention | Existing operation evidence. | Prevents duplicate effects. | No best-effort-only defense. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| 5 · ACCEPTED | C-CREATE.10.5 — Creation crash recovery | Committed checkpoint. | Resumes missing work. | No recreated source history. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 6 · ACCEPTED | C-CREATE.10.6 — Creation partial-completion recovery | Partial progress. | Resumes unfinished items. | No repeated completed effects. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 7 · ACCEPTED | C-CREATE.10.7 — Creation protective failure handling | Failure evidence. | Stops or reads provisional. | No false completion. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 8 · ACCEPTED | C-CREATE.10.8 — Creation operational logging | Operation identity/outcome. | Logs once without recursion. | No evidence-weight increase. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: C-CREATE.10.1 — Creation operation identity; C-CREATE.10.2 — Atomic creation event commitment; C-CREATE.10.3 — Creation structural duplicate prevention; C-CREATE.10.4 — Creation bounded retry consumption; C-CREATE.10.5 — Creation crash recovery; C-CREATE.10.6 — Creation partial-completion recovery; C-CREATE.10.7 — Creation protective failure handling; C-CREATE.10.8 — Creation operational logging; C-CREATE.10.9 — Creation access ordering

### C-CREATE.10.1 — Creation operation identity
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — One stable operation identity per actual creation-store operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — A distinct detection, confirmation, correction/challenge, relationship proposal, view assignment or influence-use operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Preserves its identity through transaction, logging, retries and recovery. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — An attributable operation with one operational record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Mint new identities merely to replay an already completed effect. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.10 — Creation operation and recovery rules: Identity stays with the actual operation across recovery. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.10 — Creation operation and recovery rules | Operation occurrence. | Binds its work. | No replay identity fiction. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.10.2 — Atomic creation event commitment
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Atomic commitment of each state change with its own append-only record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The operation's exact event and affected record identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Commits the change and record together, per item. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — A durable event supporting derived state. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Claim completion without committed evidence or rewrite earlier history. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Uncommitted work is not treated as complete. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.10 — Creation operation and recovery rules: Committed evidence is required for a completed change. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.3.1 — Creation detection record | Event and operation identity. | Commits append-only. | No false completed detection. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.4 — Append-only creation event family | Actual state change. | Commits with its record. | No unrecorded mutation. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-CREATE.10 — Creation operation and recovery rules | Event and identity. | Commits once. | No evidence-free completion. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.10.3 — Creation structural duplicate prevention
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Deterministic structural duplicate control, including the specific root-plus-span base identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Operation keys and committed records. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Recognizes and skips replays, recording duplicate prevention; base creation uses single-winner compare-and-create. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — No repeated effect from replay. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Use best-effort suppression or detector version as base identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Existing committed work stands; replay is skipped and recorded. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.3.2 — Source-grounded creation duplicate identity: Base records use detector-independent root-plus-span keys. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.10 — Creation operation and recovery rules: Replays must be recognized, skipped and recorded. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.3.3 — Same-fragment compare-and-create | Existing base lookup. | Skips duplicate effects. | No best-effort race. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.10 — Creation operation and recovery rules | Deterministic keys. | Skips replays. | No repeated effect. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.10.4 — Creation bounded retry consumption
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Consumption of the accepted B9 architecture and retry values for creation operations. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Actual retryable/terminal class, recorded context and durable admission authority. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Uses 3 total technical attempts; live gaps 10 then 30 seconds and 7-minute elapsed maximum, background gaps 1 then 3 minutes and 15-minute maximum; one eligible careful retry follows durable rejection, with both count/time gates, early stop and recorded-real-change continuation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Only bounded authorized attempts under the existing retry owner. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Default values, restart an exhausted episode or turn repetition alone into real change. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Terminal failures halt honestly; whichever count/time gate closes first stops further admission. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9 — B9 retry-state architecture: Consumes the existing generic retry state and admission owner. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gated by: ACCEPTED — C-7H.10 — Accepted B9 retry values and episodes: Consumes accepted bounds, episodes and real-change continuation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.10 — Creation operation and recovery rules | Failure and authority. | Uses B9 admission. | No local defaults. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.10.5 — Creation crash recovery
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Restart from committed creation and event records. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Durable operation state and last committed checkpoint. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Scans committed state only and resumes missing work; each recovery action is itself one recorded operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Recovered incomplete work without repeated committed effects. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Reconstruct absent source evidence or replay completed changes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Uncertain state remains protective; unverifiable status reads provisional. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.10 — Creation operation and recovery rules: Only durable state authorizes resumption. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.10 — Creation operation and recovery rules | Durable checkpoint. | Resumes unfinished work. | No reconstructed evidence. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.10.6 — Creation partial-completion recovery
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Per-record commitment when a larger operation only partly completes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The durable completed and incomplete record set. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Leaves completed items standing and resumes only unfinished items. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Preserved partial progress. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Roll back or duplicate completed records merely because another item failed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Completion is claimed only for durably completed items. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.10 — Creation operation and recovery rules: Completed per-item commits remain authoritative. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.10 — Creation operation and recovery rules | Per-item state. | Resumes incomplete items. | No rollback or replay. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.10.7 — Creation protective failure handling
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The protective outcome for uncertain operation state or unverifiable creation status. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Failure classification and available committed evidence. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Halts terminal failures honestly, leaves unverified changes uncommitted and reads unverifiable status as provisional. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Honest failure or provisional status, with unfinished work preserved. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Claim activation/completion/confirmation without its evidence. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Nothing unverified enters memory or activates through this operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.10 — Creation operation and recovery rules: Protective uncertainty blocks unverified claims/effects. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.10 — Creation operation and recovery rules | Unverified state. | Stops unverified effects. | No false confirmation. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.10.8 — Creation operational logging
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Exactly one operational record for each real operation, separate from canonical event/state truth. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Detection, confirmation route/basis, correction/challenge, proposal, assignment, use and failure/duplicate/recovery outcomes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Records actual operations append-only; consuming uses include provisional_material_used inside their own record; logging does not recursively log itself. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Protected auditable operation history. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Duplicate a parent's truth, treat logs as supporting evidence for their own subject or add evidential weight through logging. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Records remain subject to privacy/access and identity authorization. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-CREATE.8.1 — provisional_material_used: Consuming operations carry their own provisional-use entry. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.10 — Creation operation and recovery rules: One real operation has exactly one operational record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.10 — Creation operation and recovery rules | Actual outcome. | Appends protected record. | No log-as-evidence loop. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.10.9 — Creation access ordering
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Privacy before relevance on each retrieval, with records subject to access and identity/security authorization. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The actual request, eligible material and authorization context. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Applies the existing privacy, relevance and authorization owners before exposing or using material. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Authorized, purpose-limited creation access. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Bypass privacy because a record is provisional, confirmed or stored in a convenient view. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Protective refusal discloses no unauthorized content. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: DESIGNED — C-LMAC — Live Mechanism Access Coordinator (§26): Uses existing query routing whose operation records carry provisional influence. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §14]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): Privacy authorization precedes relevance on retrieval. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [MAP C-CREATE]
- Gated by: DESIGNED — C-7R — Attention & Relevance Control (§7R): Relevance applies only after privacy eligibility. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [MAP C-CREATE]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.8 — Traceable provisional creation influence | Request and record. | Checks privacy first. | No unauthorized influence. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.10 — Creation operation and recovery rules | Request and authorization. | Applies owners' gates. | No bypass. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-CREATE.7 — Creation views over one store | Request and eligible records. | Applies existing privacy/access owners. | No grouping-based bypass. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.11 — Current creation-scope boundaries
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Five initial creation types and the settled live-chat origination path. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — Proposed type/path scope and current accepted design. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Keeps the present vocabulary and front-door scope fixed; later expansion requires a new explicit Ness decision and a versioned design change. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — A bounded current creation design. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Expand vocabulary or front doors through mechanical implementation choices. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Future expansion remains outside present permission and does not block completion of the current scope. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.11.1 — Five-type expansion boundary: Additional types need explicit decision and versioned change. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-CREATE.11.2 — Live-chat-only origination boundary: Additional front doors need explicit decision and versioned change. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-CREATE — Unified Creation Store (§14, §7G creation-aware mode) | Type and origin. | Enforces five types and live chat. | No silent expansion. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.1 — One-store creation boundary | Record type and origin. | Checks boundaries. | No source-agnostic expansion. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-CREATE.11.1 — Five-type expansion boundary | Proposed extra type. | Retains existing set. | Future question does not block current scope. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] |
| 4 · ACCEPTED | C-CREATE.11.2 — Live-chat-only origination boundary | Originating source. | Checks scope. | Future question is not current permission. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] |

SUB-PARTS: C-CREATE.11.1 — Five-type expansion boundary; C-CREATE.11.2 — Live-chat-only origination boundary

### C-CREATE.11.1 — Five-type expansion boundary
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — A27's boundary on future additions beyond design, idea, rule, name and decision. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — A proposed additional creation type. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Requires a new explicit Ness decision and versioned design change before expansion. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — The unchanged current five-value type set. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Add types silently or treat the open future question as current permission. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Current operations remain within the five settled types. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.11 — Current creation-scope boundaries: Current vocabulary remains fixed until separately changed. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.2.2 — type_set | Proposed type set. | Rejects silent vocabulary expansion. | No sixth type. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.11 — Current creation-scope boundaries | Expansion proposal. | Keeps five current values. | No implementation-led expansion. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-CREATE.11.2 — Live-chat-only origination boundary
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — A28's boundary on creation-aware handling beyond the settled live-chat path. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — The actual originating front door. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Restricts the current creation-aware design to live chat; any other front door needs a new explicit decision and versioned change. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Current live-chat creation handling. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Assume that source-agnostic root ingestion automatically authorizes creation detection on every front door. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — No other front-door expansion is supplied by the present design. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-CREATE.11 — Current creation-scope boundaries: Current front-door permission remains live-chat-only. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-CREATE.3 — Creation fragment detection mechanics | Originating front door. | Checks current scope. | No expansion by ingestion generality. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-CREATE.11 — Current creation-scope boundaries | Proposed origin. | Keeps live-chat scope. | No silent expansion. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §6] |

SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece USED BY continuations

| Owner whose USED BY is continued | Used in | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| C-7G.7 — Creation-aware reading mode | DESIGNED — C-CREATE — Unified Creation Store (§14, §7G creation-aware mode) | Creation-aware reading result. | Preserves one-engine routing. | No separate creation filter. | [V10 §7G / CREATION-AWARE MODE] [MAP C-CREATE] |
| C-14.3 — Creation-aware live routing | DESIGNED — C-CREATE — Unified Creation Store (§14, §7G creation-aware mode) | Live message capture and provenance. | Uses the existing front door. | No new front door inferred. | [V10 §7G / CREATION-AWARE MODE] [MAP C-CREATE] |
| C-7I — View Layer (§7I) | DESIGNED — C-CREATE — Unified Creation Store (§14, §7G creation-aware mode) | Creation, status and provenance. | Exposes only permitted records. | No overwritten history. | [MAP C-CREATE] |
| C-7G.7.1 — Broad provisional creation and traceable influence | ACCEPTED — C-CREATE.3 — Creation fragment detection mechanics | Small/partial/unfinished creations. | Captures without confirming. | No need for a finished idea. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] |
| C-14.3.2 — Explicit confirmation route | ACCEPTED — C-CREATE.5.1 — Explicit-confirmation commit | Referenced Ness words. | Records the actual confirmation. | No new confirmation policy. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] |
| C-14.3.3 — Clear demonstrated-adoption route | ACCEPTED — C-CREATE.5.2 — Later-adoption proposal evaluation | Later words/actions. | Preserves clear-adoption requirement. | No ambiguous confirmation. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] |
| C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | ACCEPTED — C-CREATE.5.2 — Later-adoption proposal evaluation | Grounded proposal and exact evidence. | Uses the acceptance boundary. | Mouth assertion alone cannot confirm. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| C-7G.7.1 — Broad provisional creation and traceable influence | ACCEPTED — C-CREATE.8 — Traceable provisional creation influence | Relevant provisional material. | Applies all status protections. | No replacement policy. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] |
| C-7F — Context Retrieval (§7F) | ACCEPTED — C-CREATE.8.2 — Provisional influence in retrieval | Provisional creation reference. | Requires a suitable permitted mode. | RM-CR-01 remains root-candidates-only. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| C-7M — Computed View (§7M) | ACCEPTED — C-CREATE.8.5 — Provisional influence in Computed View | Record, status and operation trace. | Supplies permitted provisional context. | Computed result cannot relabel it settled. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] |
| C-7H.9 — B9 retry-state architecture | ACCEPTED — C-CREATE.10.4 — Creation bounded retry consumption | Source class and durable records. | Admits only eligible attempts. | No local second retry state machine. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| C-7H.10 — Accepted B9 retry values and episodes | ACCEPTED — C-CREATE.10.4 — Creation bounded retry consumption | Configuration, timing and count evidence. | Enforces both limits. | No reset from repetition or crash. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | ACCEPTED — C-CREATE.10.9 — Creation access ordering | Request and source eligibility. | Limits eligible material. | No unauthorized disclosure. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [MAP C-CREATE] |
| C-7R — Attention & Relevance Control (§7R) | ACCEPTED — C-CREATE.10.9 — Creation access ordering | Authorized material and purpose. | Controls relevant use. | No privacy-as-score substitution. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [MAP C-CREATE] |
| C-LMAC — Live Mechanism Access Coordinator (§26) | ACCEPTED — C-CREATE.10.9 — Creation access ordering | Authorized logical query. | Uses the routing owner. | No store-owned alternate access path. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §14] |

## Scope and path placement

C-CREATE is the DESIGNED Unified Creation Store, used in the settled creation-aware sub-path of CY-B. Its ACCEPTED B14 subparts supply the concrete base schema, append-only event family, source-grounded duplicate identity, confirmation machinery, derived views, provisional-use trace and operation rules. All descendants inherit the root's explicit path placement. B-CYCLE-7 is a named remaining full-cycle design dependency, not an invented new path ID or a claim that chat synchronization is complete.

The existing C-7G.7 creation-aware mode and C-14.3 live route retain their exact identities. C-7G.7.1 remains the shared broad-capture/influence policy, and the prior explicit/later-adoption route cards remain policy owners; the current cards supply their store-specific commits and records. Creation records reference already-existing roots and create no new roots. Provisional creations are not held pre-ingest content; permission to use them still requires status to be visible and traceable.


## Cross-piece TOGETHER continuations for incoming uses

| Using card | Field | Current owner | Condition / handoff | Source |
|---|---|---|---|---|
| C-14.3 — Creation-aware live routing | Changes | C-CREATE — Unified Creation Store (§14, §7G creation-aware mode) | DESIGNED — Supplies provisional creation material and actual confirmation evidence through the live route. | [V10 §7G / CREATION-AWARE MODE] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] |
| C-14.3.4 — Provisional availability and influence | Gated by | C-CREATE — Unified Creation Store (§14, §7G creation-aware mode) | DESIGNED — Every wider provisional use must carry visible status and its record/status-at-use trace. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9 / (g)] |
| C-7G.7 — Creation-aware reading mode | Changes | C-CREATE — Unified Creation Store (§14, §7G creation-aware mode) | DESIGNED — Creates provisional records in the one connected store. | [V10 §7G / CREATION-AWARE MODE] |


## Source conflicts and explicit source-scope differences

| Kind | Sources and exact difference | Preserved treatment |
|---|---|---|
| Earlier open slots versus accepted A13/B14 | V10 and Map leave schema, exact detection mechanics and provisional-influence policy open; accepted Bundle 6 supplies the design-level schema, broad detection, detector-independent duplicate identity, event lifecycle and carried-status influence rules. [V10 §7G / CREATION-AWARE MODE] [MAP C-CREATE] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] | Governing root stays DESIGNED; accepted standalone mechanics are ACCEPTED. Physical format, implementation choices and whole-cycle integration are not claimed settled. Earlier openings are not used to erase accepted design. |
| Canonical confirmation versus immutable initial status | The base initial_status always remains provisional; current confirmed status comes only from the committed confirmation event. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] | These are separate time/scope meanings, not contradictory states. Challenges/corrections link to confirmation without establishing parallel status truth; no unprovided revocation lifecycle is invented. |
| Permitted provisional influence versus root-only retrieval mode | B14 permits relevant provisional creations in wider retrieval/reasoning/answers/Computed View when marked and traced. RM-CR-01's candidate type is roots. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] | The general policy permission does not silently broaden RM-CR-01 to creation-record candidates. The exact creation-record retrieval mode/integration is open; source-root retrieval remains its existing declaration. |
| Shared root-writing spine versus creation records | Mechanical §3 supplies a general no-bypass B11 root-write boundary; the creation path in the accepted closeout expressly creates no new roots. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §8] | Creation detection references existing roots. Any source capture retains its existing C-14 → C-7E → B11 owner; no new creation-root ingestion mechanism is inferred. |
| Accepted packages versus conditional final receipt | Policy/mechanical receipts prove their respective acceptances. The final v1_1 receipt proves acceptance of closeout v1_2 but explicitly awaits its own independent audit before formal final PACKAGE_COMPLETE takes effect. [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md §0] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md §4] | Accepted source behavior is retained. No unseen receipt PASS, integration, implementation or whole-system completion is asserted. Earlier receipt wording about then-future closeout does not invalidate the later accepted source. |

No direct contradictory creation behavior is silently reconciled in this piece. The known B26 permitted-source gap and earlier explicit source-conflict registers remain carried forward; this chapter neither opens excluded historical files nor resolves those conflicts.

## Explicit remaining scope

- **Writing 1 boundary:** CH05-e is the last piece in this round. Full later groups and paths remain in the approved Writing 2/3 plan; no later round is started here.
- **C-7M / CH06-d, C-7I / CH06-e, C-7Q / CH08-a, C-7R / CH08-b and C-LMAC / CH08-c:** complete consumer/view/access/relevance/routing internals. Current provisional status, privacy-before-relevance and trace conditions are written in full; they do not substitute for those mechanisms.
- **C-7G / CH05-a and C-7H / CH05-d:** existing acceptance-facing and B9 state/value owners are reused. The complete B24 messenger/model and general parent/child mechanism remains CH10-b. No local alternative retry or validation engine is created here.
- **C-19 / CH10-e:** A13.3, the future interface idea of talking about promising fragments, remains a future non-blocking note for later interface work. No detection cadence, prompt or automatic discussion behavior is invented.
- **Other Bundle 6 sections:** B12, B17/B18, B20/B21 and B22 retain their earlier placements; full B13 research isolation remains C-8/CH10-a, B-INT-2 routing C-LMAC/CH08-c and B-INT-3 observation/reaction-window details their C-BOP/C-OOP owners. Scoped reading does not claim a whole mechanical or policy file read.
- **CH11/CH12:** complete cycle assembly, gap/conflict registers and cumulative audit reconciliation. Full B-CYCLE-7 is still open. The accepted Bundle 2 foundation's only pinned path remains prohibited 99_HISTORICAL_CANDIDATES; its missing detailed B26 source-scope coverage is retained, not described as absence of accepted design.

## Additional undecided implementation slots

| Slot | Value | Boundary / owner |
|---|---|---|
| Physical Creation Store technology, path and serialization | NOT DECIDED | B14 specifies design-level shape only; no store is created by this writing. |
| Exact detector implementation, method and thresholds | NOT DECIDED | Broad fragment capture and identity rules are settled; runtime choice is not. |
| Base operation-ID and non-base event-key encodings | NOT DECIDED | Stable operation identity/deterministic duplicate control are required; only source-root-plus-exact-span base identity is concretely supplied. |
| Additional complete serialization fields for detection/confirmation/challenge/correction/proposal/assignment events | NOT DECIDED | Every supplied field/basis/record type is placed; unspecified schema fields are not invented. |
| Exact fragment-offset or locator encoding | NOT DECIDED | Locators must re-find the exact words; physical representation is open. |
| Further challenge-resolution or confirmation-revocation lifecycle | NOT DECIDED | Challenges/corrections link to canonical confirmation; no additional states or automatic reversal are supplied. |
| Exact ordered view-membership resolution for conflicting assignment events | NOT DECIDED | Membership derives from committed assignment records; no new conflict algorithm is chosen. |
| Creation-record retrieval declaration and integrated candidate route | NOT DECIDED | General provisional-use permission does not alter roots-only RM-CR-01. |
| Full live-creation cycle synchronization and transaction wiring | NOT DECIDED | B-CYCLE-7 remains separate from completed component design. |
| A27 future vocabulary expansion | NOT DECIDED | Current five-type vocabulary stays fixed; expansion needs a new explicit decision/versioned change. |
| A28 future origination beyond live chat | NOT DECIDED | Current path is live-chat-only; other front doors are not silently enabled. |
| A13.3 promising-fragment conversation behavior | NOT DECIDED | Future interface note with its later owner; no current scheduling/UI rules. |

## Review of plain gates and empty boxes

All six base fields, nested source provenance, four detection-provenance elements, canonical confirmation route/basis, both sides of adoption evidence and both provisional-use entry elements are explicit. The seven event kinds have one identity each; detection and stable creation identity are shared where reused. Confirmation has its two source-defined routes and its ambiguity outcome; the derived provisional/confirmed distinction never rewrites initial_status. Event schemas are not padded with plausible but unsourced timestamps, enums or keys.

Source-grounded duplicate identity, one concurrent winner, new-version re-evaluation, distinct-fragment handling and segmentation/disagreement handling are separate rules. Actual detection, commit, confirmation, derivation, use and recovery steps link their owning rules. Empty independent failure/restriction boxes on identity/form carriers were checked against all other fields and USED BY cells; no absent runtime mechanism is invented. Every wider use carries visible provisional status and an entry inside its own operation record. Generic retry state and values retain C-7H.9/C-7H.10; source-boundary reads retain their declared scope and exact fingerprints.

## Appendix A carry-forward — this piece

| Part | Field or cell | Value |
|---|---|---|
| C-CREATE.1 | Fed by | NOT DECIDED |
| C-CREATE.1 | Changes | NOT DECIDED |
| C-CREATE.2 | Changes | NOT DECIDED |
| C-CREATE.2.1 | Fails closed by | NOT DECIDED |
| C-CREATE.2.1 | Fed by | NOT DECIDED |
| C-CREATE.2.1 | Changes | NOT DECIDED |
| C-CREATE.2.2 | Fed by | NOT DECIDED |
| C-CREATE.2.2 | Changes | NOT DECIDED |
| C-CREATE.2.3 | Fed by | NOT DECIDED |
| C-CREATE.2.3 | Changes | NOT DECIDED |
| C-CREATE.2.4 | Changes | NOT DECIDED |
| C-CREATE.2.4.1 | Fails closed by | NOT DECIDED |
| C-CREATE.2.4.1 | Fed by | NOT DECIDED |
| C-CREATE.2.4.1 | Gated by | NOT DECIDED |
| C-CREATE.2.4.1 | Changes | NOT DECIDED |
| C-CREATE.2.4.2 | Fed by | NOT DECIDED |
| C-CREATE.2.4.2 | Changes | NOT DECIDED |
| C-CREATE.2.5 | Fails closed by | NOT DECIDED |
| C-CREATE.2.5 | Fed by | NOT DECIDED |
| C-CREATE.2.5 | Changes | NOT DECIDED |
| C-CREATE.2.6 | Must never | NOT DECIDED |
| C-CREATE.2.6 | Fails closed by | NOT DECIDED |
| C-CREATE.2.6 | Fed by | NOT DECIDED |
| C-CREATE.2.6 | Gated by | NOT DECIDED |
| C-CREATE.2.6 | Changes | NOT DECIDED |
| C-CREATE.3 | Changes | NOT DECIDED |
| C-CREATE.3.1 | Changes | NOT DECIDED |
| C-CREATE.3.1.1 | Fails closed by | NOT DECIDED |
| C-CREATE.3.1.1 | Fed by | NOT DECIDED |
| C-CREATE.3.1.1 | Changes | NOT DECIDED |
| C-CREATE.3.1.2 | Fails closed by | NOT DECIDED |
| C-CREATE.3.1.2 | Fed by | NOT DECIDED |
| C-CREATE.3.1.2 | Gated by | NOT DECIDED |
| C-CREATE.3.1.2 | Changes | NOT DECIDED |
| C-CREATE.3.1.3 | Fed by | NOT DECIDED |
| C-CREATE.3.1.3 | Changes | NOT DECIDED |
| C-CREATE.3.1.4 | Fails closed by | NOT DECIDED |
| C-CREATE.3.1.4 | Fed by | NOT DECIDED |
| C-CREATE.3.1.4 | Gated by | NOT DECIDED |
| C-CREATE.3.1.4 | Changes | NOT DECIDED |
| C-CREATE.3.2 | Changes | NOT DECIDED |
| C-CREATE.3.3 | Fed by | NOT DECIDED |
| C-CREATE.3.3 | Changes | NOT DECIDED |
| C-CREATE.3.4 | Fed by | NOT DECIDED |
| C-CREATE.3.4 | Changes | NOT DECIDED |
| C-CREATE.3.5 | Fed by | NOT DECIDED |
| C-CREATE.3.5 | Changes | NOT DECIDED |
| C-CREATE.3.6 | Fed by | NOT DECIDED |
| C-CREATE.3.6 | Changes | NOT DECIDED |
| C-CREATE.4.1 | Changes | NOT DECIDED |
| C-CREATE.4.1.1 | Fed by | NOT DECIDED |
| C-CREATE.4.1.1 | Changes | NOT DECIDED |
| C-CREATE.4.1.2 | Fed by | NOT DECIDED |
| C-CREATE.4.1.2 | Changes | NOT DECIDED |
| C-CREATE.4.2 | Changes | NOT DECIDED |
| C-CREATE.4.2.1 | Fed by | NOT DECIDED |
| C-CREATE.4.2.1 | Changes | NOT DECIDED |
| C-CREATE.4.2.2 | Changes | NOT DECIDED |
| C-CREATE.4.3 | Fails closed by | NOT DECIDED |
| C-CREATE.4.3 | Fed by | NOT DECIDED |
| C-CREATE.4.3 | Changes | NOT DECIDED |
| C-CREATE.4.4 | Fed by | NOT DECIDED |
| C-CREATE.4.4.1 | Fails closed by | NOT DECIDED |
| C-CREATE.4.4.1 | Fed by | NOT DECIDED |
| C-CREATE.4.4.1 | Changes | NOT DECIDED |
| C-CREATE.4.5 | Fed by | NOT DECIDED |
| C-CREATE.4.5 | Changes | NOT DECIDED |
| C-CREATE.4.6 | Fed by | NOT DECIDED |
| C-CREATE.4.6 | Changes | NOT DECIDED |
| C-CREATE.5 | Fed by | NOT DECIDED |
| C-CREATE.5.1 | Fed by | NOT DECIDED |
| C-CREATE.5.2 | Changes | NOT DECIDED |
| C-CREATE.5.3 | Fed by | NOT DECIDED |
| C-CREATE.5.4 | Fed by | NOT DECIDED |
| C-CREATE.5.4 | Changes | NOT DECIDED |
| C-CREATE.5.5 | Fed by | NOT DECIDED |
| C-CREATE.5.5 | Changes | NOT DECIDED |
| C-CREATE.6 | Changes | NOT DECIDED |
| C-CREATE.6.1 | Fed by | NOT DECIDED |
| C-CREATE.6.1 | Changes | NOT DECIDED |
| C-CREATE.6.2 | Fed by | NOT DECIDED |
| C-CREATE.6.2 | Changes | NOT DECIDED |
| C-CREATE.6.3 | Changes | NOT DECIDED |
| C-CREATE.6.4 | Fed by | NOT DECIDED |
| C-CREATE.6.4 | Changes | NOT DECIDED |
| C-CREATE.6.5 | Fed by | NOT DECIDED |
| C-CREATE.6.5 | Changes | NOT DECIDED |
| C-CREATE.7.1 | Fed by | NOT DECIDED |
| C-CREATE.7.1 | Changes | NOT DECIDED |
| C-CREATE.7.2 | Fed by | NOT DECIDED |
| C-CREATE.7.2 | Changes | NOT DECIDED |
| C-CREATE.8 | Changes | NOT DECIDED |
| C-CREATE.8.1 | Changes | NOT DECIDED |
| C-CREATE.8.1.1 | Fails closed by | NOT DECIDED |
| C-CREATE.8.1.1 | Changes | NOT DECIDED |
| C-CREATE.8.1.2 | Changes | NOT DECIDED |
| C-CREATE.8.2 | Fed by | NOT DECIDED |
| C-CREATE.8.2 | Changes | NOT DECIDED |
| C-CREATE.8.3 | Fed by | NOT DECIDED |
| C-CREATE.8.3 | Changes | NOT DECIDED |
| C-CREATE.8.4 | Fed by | NOT DECIDED |
| C-CREATE.8.4 | Changes | NOT DECIDED |
| C-CREATE.8.5 | Fed by | NOT DECIDED |
| C-CREATE.9 | Fed by | NOT DECIDED |
| C-CREATE.9.1 | Fed by | NOT DECIDED |
| C-CREATE.9.1 | Changes | NOT DECIDED |
| C-CREATE.10 | Fed by | NOT DECIDED |
| C-CREATE.10.1 | Fails closed by | NOT DECIDED |
| C-CREATE.10.1 | Fed by | NOT DECIDED |
| C-CREATE.10.1 | Changes | NOT DECIDED |
| C-CREATE.10.2 | Fed by | NOT DECIDED |
| C-CREATE.10.2 | Changes | NOT DECIDED |
| C-CREATE.10.3 | Fed by | NOT DECIDED |
| C-CREATE.10.3 | Changes | NOT DECIDED |
| C-CREATE.10.4 | Fed by | NOT DECIDED |
| C-CREATE.10.4 | Changes | NOT DECIDED |
| C-CREATE.10.5 | Fed by | NOT DECIDED |
| C-CREATE.10.5 | Changes | NOT DECIDED |
| C-CREATE.10.6 | Fed by | NOT DECIDED |
| C-CREATE.10.6 | Changes | NOT DECIDED |
| C-CREATE.10.7 | Fed by | NOT DECIDED |
| C-CREATE.10.7 | Changes | NOT DECIDED |
| C-CREATE.10.8 | Changes | NOT DECIDED |
| C-CREATE.10.9 | Changes | NOT DECIDED |
| C-CREATE.11 | Fed by | NOT DECIDED |
| C-CREATE.11 | Changes | NOT DECIDED |
| C-CREATE.11.1 | Fed by | NOT DECIDED |
| C-CREATE.11.1 | Changes | NOT DECIDED |
| C-CREATE.11.2 | Fed by | NOT DECIDED |
| C-CREATE.11.2 | Changes | NOT DECIDED |

## Retained plain-gate inventory

All populated TOGETHER lines name an owning or connected card; no plain gate remains.

## Source coverage added by CH05-e

| Source | Scope read | Landing / exclusion |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: §7G including the complete creation-aware subsection, and complete §14; only creation-relevant behavior placed here. | C-CREATE and shared C-7G.7 / C-14.3 recognition/route; two confirmation routes, five types, permanence and one store. |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped: Complete C-CREATE and CY-B; related C-13/C-14/C-7G navigation and earlier use lookup. | Root identity and CY-B creation sub-path, downstream access/view owners; full B-CYCLE-7 remains open. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped: Complete §§3, 6 and 14–16; header/version-note navigation only. B14 source content is complete; remaining other-component sections retain earlier credits and later owners. | C-CREATE.1 through C-CREATE.10: every base field, event family, detection identity/re-evaluation, canonical confirmation, derived view, influence entry, fragment preservation and operation/recovery rule. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Scoped: Complete §4 A13, §§6–8 and header; no whole-file credit. | Existing shared C-7G.7.1 broad policy; current detection/use implementation and C-CREATE.11 scope; A13.3 explicitly deferred. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Scoped: Complete §5 identities, §8 creation row 5 and surrounding table navigation, §9(g) provisional-material boundary; neighboring §9(h) also read but owned by CH04-e. No whole-file credit. | C-CREATE.1 no-new-root/provisional-not-held distinction and C-CREATE.8 visible-and-traceable influence; other path mechanics not rederived here. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Scoped: §6 items 1–7 complete and start of item 8, for roots-only RM-CR-01 candidate boundary. Earlier CH05-c declaration content remains its owner. | C-CREATE.8.2 consumes C-7F without broadening the existing roots-only mode; exact creation-record retrieval integration remains open. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: Complete acceptance/identity receipt; no new behavior supplied by receipt. | Acceptance and exact source identity only. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: Complete acceptance/identity receipt; its earlier pending closeout wording is dated scope, not denial of later accepted closeout. | Acceptance and exact source identity only. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Whole: Complete final receipt including its explicit receipt-audit gate; accepted policy/mechanics/closeout distinguished from unobserved final receipt PASS. | Accepted closeout identity, independent source acceptance and conditional final receipt status only. |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Scoped: Creation/provisional keyword navigation only; no new creation-store behavior derived from this search. | EXCLUDED from current new behavior: navigation found no new relevant creation-store rule; governing authority unchanged. |
| `01_AUTHORITATIVE/cursorrules` | Scoped: Creation/provisional keyword navigation only; unrelated protected-file creation hits are not creation-store architecture. | EXCLUDED from current new behavior: navigation of unrelated file-creation rules, not a new creation-store mechanism. |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Scoped: Creation/provisional keyword navigation only; unrelated identity/governance uses are not creation-store architecture. | EXCLUDED from current new behavior: unrelated governance/identity matches; no rule inferred for C-CREATE. |

## Coverage matrix — cumulative carried inventory










The following inventory retains the preceding pieces’ placements and read status. This piece’s additional placements and deferrals are in the source-scope table above; inherited notes are not fresh whole-read claims.
### File coverage

| Row | Source | Read scope | Placement |
|---|---|---|---|
| F001 | `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped read in CH04-b: §0B; §6A SCHEMA CONSTRAINTS; §6B schema/status boundary; full §7E-TSC §§1–31. Prior read credits retained. | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.1; C-STORE.2; C-STORE.3; CY-A Chapter 3-b: C-READ and its v1 record, validator, writer, quarantine, production-boundary and operation-record sub-parts; CY-A/CY-F reading-write interfaces. Chapter 3-c: governing checks for C-READ.10; A2/firmness additions stay ACCEPTED, never BUILT. Chapter 3-d: source-status and no-production-write boundaries; governing operational living-memory rule at C-READ.11.9.4.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.3, C-ENGINE-C.3.1, C-ENGINE-C.3.2, C-ENGINE-C.3.3, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.11.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1, C-ENGINE-AB.1.1, C-ENGINE-AB.1.2, C-ENGINE-AB.1.3, C-ENGINE-AB.2, C-ENGINE-AB.2.1, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.1, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.2.4, C-ENGINE-AB.3, C-ENGINE-AB.4, C-ENGINE-AB.5, C-ENGINE-AB.6, C-ENGINE-AB.8, C-ENGINE-AB.9.; CH03-k: C-INDEX, C-INDEX.1, C-INDEX.1.1, C-INDEX.1.2, C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.1, C-INDEX.4.2, C-INDEX.4.3, C-INDEX.4.4, C-INDEX.4.5, C-INDEX.4.7, C-INDEX.4.8, C-INDEX.5, C-INDEX.6.; CH03-l: C-GOLD, C-GOLD.2, C-GOLD.2.1, C-GOLD.3, C-GOLD.3.1, C-GOLD.6, C-GOLD.6.1, C-GOLD.6.2, C-GOLD.6.3, C-GOLD.7, C-GOLD.7.4.; CH03-o: C-INGEST, C-INGEST.1, C-INGEST.2, C-INGEST.3, C-INGEST.4, C-INGEST.4.1, C-INGEST.4.2, C-INGEST.4.3, C-INGEST.4.4, C-INGEST.4.5, C-INGEST.4.6, C-INGEST.4.7, C-INGEST.4.8, C-INGEST.4.8.1, C-INGEST.4.8.2, C-INGEST.4.8.3, C-INGEST.4.8.4, C-INGEST.4.9, C-INGEST.6.; CH03-p: C-DETECT, C-DETECT.1, C-DETECT.1.1, C-DETECT.1.3, C-DETECT.2, C-DETECT.2.1, C-DETECT.2.2, C-DETECT.2.3, C-DETECT.2.4, C-DETECT.2.5, C-DETECT.3, C-DETECT.3.1, C-DETECT.3.2, C-DETECT.3.3, C-DETECT.3.4, C-DETECT.3.5, C-DETECT.3.6, C-DETECT.4.1.; CH04-a: C-7E, C-7E.1, C-7E.1.1, C-7E.1.2, C-7E.2, C-7E.3, C-7E.4, C-7E.5, C-7E.5.1, C-7E.5.2, C-7E.5.3, C-7E.5.4, C-7E.5.5, C-7E.5.6, C-7E.6, C-7E.6.1, C-7E.6.2, C-7E.6.3, C-7E.6.4, C-7E.6.5, C-7E.6.6, C-7E.6.7, C-7E.7, C-7E.8, C-7E.8.1, C-7E.8.2, C-7E.8.3, C-7E.8.4, C-7E.9, C-7E.9.1, C-7E.9.2, C-7E.9.2.1, C-7E.9.2.2, C-7E.9.2.3, C-7E.9.2.4, C-7E.9.3, C-7E.9.3.1, C-7E.9.3.2, C-7E.9.3.3, C-7E.9.3.4, C-7E.9.3.5, C-7E.9.3.6, C-7E.9.4, C-7E.10, C-7E.10.1, C-7E.10.2, C-7E.11, C-7E.12, C-7E.13, C-7E.13.1, C-7E.13.4, C-7E.13.5, C-7E.13.6. CH04-b: see the exact source-scope and landing table above.  CH04-c: scoped read; exact scope and placement in the current source table.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-c: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F002 | `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Scoped read in CH04-b: §3N; inspection conflict. Prior read credits retained. | EXCLUDED: interaction/workflow guidance under §1.3 and §2.4. NOT PLACED: remaining behavior belongs to other component groups.; Chapter 3-a: C-STORE.2.3 Chapter 3-b: C-READ.1 confidence semantics and C-READ.2 uncertainty-preserving shape gate; remaining scope retained. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.2, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.8.; CH03-l: C-GOLD, C-GOLD.2, C-GOLD.2.1, C-GOLD.3, C-GOLD.3.1, C-GOLD.4, C-GOLD.4.1, C-GOLD.4.2, C-GOLD.4.3, C-GOLD.4.4, C-GOLD.4.5, C-GOLD.4.6, C-GOLD.5, C-GOLD.6, C-GOLD.6.1, C-GOLD.6.3, C-GOLD.8.3, C-GOLD.8.5.10, C-GOLD.8.5.11.; CH04-a: C-7E, C-7E.1.2, C-7E.5.2, C-7E.6.1, C-7E.6.2, C-7E.7, C-7E.8.4, C-7E.13.3. CH04-b: see the exact source-scope and landing table above.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F003 | `01_AUTHORITATIVE/cursorrules` | Scoped reread for CH03-o; prior whole-read credit retained where previously recorded | EXCLUDED: coding-process rules under §1.3. NOT PLACED: built-code boundaries belong to store, reader and code-boundary groups. Chapter 3-b: C-READ.1.12 per-store/global-key conflict and C-READ.3 shared write boundary; workflow remains excluded. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB.5.; CH03-k: C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.6.; CH03-l: C-GOLD, C-GOLD.9.; CH03-o: C-INGEST, C-INGEST.4, C-INGEST.4.7, C-INGEST.6.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F004 | `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Scoped read in CH04-b: Embedded TSC §§15–16; conflicting inspection and failed-authorization text. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. CH04-b: see the exact source-scope and landing table above.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F005 | `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped read in CH04-b: C-TSC and CY-D; component naming and path ownership. Prior read credits retained. | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.3.4; CY-A Chapter 3-b: C-READ component name, operation logging and consumer/caller relationships; CY-A/CY-F interfaces. Chapter 3-c: component ownership/names and Group A/D boundary; accepted A2 supplies behavior. Chapter 3-d: names, Group A ownership and per-reading seam versus full CY-G boundary.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.9.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1.1, C-ENGINE-AB.1.3, C-ENGINE-AB.2.1, C-ENGINE-AB.2.4, C-ENGINE-AB.4, C-ENGINE-AB.6, C-ENGINE-AB.6.1.; CH03-k: C-INDEX, C-INDEX.2, C-INDEX.3, C-INDEX.5, C-INDEX.6, C-INDEX.6.1, C-INDEX.6.2, C-INDEX.6.3, C-INDEX.6.4, C-INDEX.6.5, C-INDEX.6.6.; CH03-l: C-GOLD, C-GOLD.4, C-GOLD.4.6, C-GOLD.6, C-GOLD.6.2, C-GOLD.7, C-GOLD.7.1, C-GOLD.7.2, C-GOLD.7.3, C-GOLD.7.4.; CH03-o: C-INGEST, C-INGEST.4.4, C-INGEST.4.7, C-INGEST.5, C-INGEST.5.1, C-INGEST.5.2, C-INGEST.5.3, C-INGEST.5.4, C-INGEST.6.; CH03-p: C-DETECT, C-DETECT.1, C-DETECT.1.1, C-DETECT.1.2, C-DETECT.1.3, C-DETECT.2, C-DETECT.2.1, C-DETECT.2.2, C-DETECT.2.3, C-DETECT.2.4, C-DETECT.2.5, C-DETECT.3, C-DETECT.3.1, C-DETECT.3.3, C-DETECT.3.4, C-DETECT.3.6, C-DETECT.4, C-DETECT.4.1, C-DETECT.4.1.1, C-DETECT.4.1.2, C-DETECT.4.2.; CH04-a: C-7E, C-7E.3, C-7E.4, C-7E.5, C-7E.5.2, C-7E.6.1, C-7E.6.4, C-7E.7, C-7E.8, C-7E.11, C-7E.13, C-7E.13.1, C-7E.13.2, C-7E.13.3, C-7E.13.4, C-7E.13.5, C-7E.13.6, C-7E.13.7. CH04-b: see the exact source-scope and landing table above.  CH04-c: scoped read; exact scope and placement in the current source table.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-c: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F006 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F007 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F008 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole read in CH04-b: Acceptance/status evidence only. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F009 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md` | Whole read in CH04-b: Event adoption §§2–7; status and source envelope. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F010 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F011 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.9 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F012 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F013 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-c: scoped read; exact scope and placement in the current source table. |
| F014 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F015 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F016 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F017 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_GOLD_CASES_MISSING_SOURCE_BLOCKER_RECORD_v1_0.md` | Scoped reread for CH03-l; prior whole-read credit retained where previously recorded | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker.; CH03-l: Status/provenance only; no behavior from this receipt or historical blocker. |
| F018 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH03-l | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker.; CH03-l: Status/provenance only; no behavior from this receipt or historical blocker. |
| F019 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md` | Scoped reread for CH03-l; prior whole-read credit retained where previously recorded | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-j: C-ENGINE-C.7.; CH03-l: C-GOLD, C-GOLD.6.1, C-GOLD.8, C-GOLD.8.1, C-GOLD.8.2, C-GOLD.8.2.1, C-GOLD.8.5.12. |
| F020 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md` | Scoped reread for CH03-l; prior whole-read credit retained where previously recorded | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker.; CH03-l: C-GOLD.8, C-GOLD.8.5.12. |
| F021 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md` | Read whole for CH03-l | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-l: C-GOLD.6.1, C-GOLD.8, C-GOLD.8.2, C-GOLD.8.2.1, C-GOLD.8.2.2, C-GOLD.8.3, C-GOLD.8.3.1, C-GOLD.8.3.2, C-GOLD.8.4, C-GOLD.8.5, C-GOLD.8.5.1, C-GOLD.8.5.2, C-GOLD.8.5.3, C-GOLD.8.5.4, C-GOLD.8.5.5, C-GOLD.8.5.6, C-GOLD.8.5.7, C-GOLD.8.5.8, C-GOLD.8.5.9, C-GOLD.8.5.10, C-GOLD.8.5.11, C-GOLD.8.5.12, C-GOLD.8.6, C-GOLD.8.6.1, C-GOLD.8.7, C-GOLD.8.7.1, C-GOLD.8.8, C-GOLD.8.8.1, C-GOLD.8.8.2, C-GOLD.8.9, C-GOLD.8.9.1, C-GOLD.8.9.2, C-GOLD.8.9.3, C-GOLD.8.10, C-GOLD.8.10.1, C-GOLD.8.10.2, C-GOLD.8.10.3, C-GOLD.8.11, C-GOLD.8.11.1, C-GOLD.8.11.2, C-GOLD.8.12, C-GOLD.8.12.1, C-GOLD.8.12.2, C-GOLD.8.13, C-GOLD.8.13.1, C-GOLD.8.13.2. |
| F022 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F023 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F024 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F025 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F026 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F027 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F028 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F029 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F030 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F031 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F032 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F033 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F034 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0 .md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F035 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md` | Scoped reread for CH04-a; prior whole-read credit retained where previously recorded | C-7B.7 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker. |
| F036 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md` | Scoped reread for CH03-j; prior whole-read credit retained where previously recorded | C-READ.10 and all A2-cited descendants: §§1–10 identity, card/preparation/event ownership, acceptance/correspondence, commit/recovery, legacy mapping, lifecycle, semantic/safety boundaries, references/rereading and logging. EXCLUDED: source revision history, acts of acceptance, implementation workflow and self-audit claims under §1.3. Other consumer mechanics remain with their owning groups.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards.; CH03-j: C-ENGINE-C, C-ENGINE-C.3.3, C-ENGINE-C.4, C-ENGINE-C.5, C-ENGINE-C.6, C-ENGINE-C.9, C-ENGINE-C.11.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F037 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_PACKAGE_COMPLETE_RECORD_v1_0.md` | Read whole for CH03-j | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker. |
| F038 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F039 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F040 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F041 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F042 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F043 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F044 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F045 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F046 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F047 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F048 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for C-STORE.4; receipt narrative excluded under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker. |
| F049 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | Scoped read in CH04-b: §13 TSC caller boundary. Prior read credits retained. | Chapter 3-a: C-STORE.4 and all descendants. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: §10 cross-batch reading reread for boundary check; no new B11 behavior written here, Chapter 3-a placement retained.; CH04-a: C-7E, C-7E.1.2, C-7E.5.6, C-7E.6.3, C-7E.6.4, C-7E.12. CH04-b: see the exact source-scope and landing table above. |
| F050 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole read in CH04-b: Acceptance/status evidence only. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F051 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md` | Whole read in CH04-b: Structural store, exact tables, constraints, transactions, recovery, archive, logging and open implementation choices. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F052 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH03-n | Status/identity checked for NHD-B16EEB; globally unique slot identifiers retained; acceptance narrative EXCLUDED by §1.3; CH03-l: Status/provenance only; no behavior from this receipt or historical blocker.; CH03-m: C-GOLD.1.8.1.5.1.; CH03-n: C-GOLD.1.10, C-GOLD.1.11, C-GOLD.1.11.1, C-GOLD.1.11.2, C-GOLD.1.11.3, C-GOLD.1.11.4, C-GOLD.1.11.5, C-GOLD.1.11.6, C-GOLD.1.11.7, C-GOLD.1.11.8, C-GOLD.1.11.9, C-GOLD.1.11.10, C-GOLD.1.11.11, C-GOLD.1.11.12, C-GOLD.1.11.13, C-GOLD.1.11.14, C-GOLD.1.11.15, C-GOLD.1.11.16, C-GOLD.1.11.17, C-GOLD.1.12, C-GOLD.1.12.1, C-GOLD.1.12.2, C-GOLD.1.12.3, C-GOLD.1.12.4, C-GOLD.1.12.5. |
| F053 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | §§2–6 establish exact accepted standalone scope and source identity. EXCLUDED from behavior: receipt history/roles/process; no mechanism sourced from receipt. |
| F054 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | C-READ.11 and every descendant: complete §§1–11 seam; §13 traces checked against the same rules. §12 external ownership and unspecified details recorded separately. EXCLUDED under §1.3: source status/history/process, self-audit and delivery narrative (§§14–15). |
| F055 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F056 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F057 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md` | Scoped reread for CH03-m; prior whole-read credit retained where previously recorded | C-READ.7.2 and its reciprocal C-READ.7 link: ACCEPTED guard from §1.2 (NHD-B24), matching FR-0608 CARRIED. Remaining B24 behavior NOT PLACED: belongs to later owning templates; no other B24 mechanism added here. Chapter 3-c C-READ.10.3.8.8 and source-conflict register: structural-disposition difference retained against A2; no new retry policy.; CH03-m: C-GOLD.1.8.1.5.2, C-GOLD.1.8.1.5.2.1, C-GOLD.1.8.1.5.2.2, C-GOLD.1.8.1.5.2.3, C-GOLD.1.8.4.3.1, C-GOLD.1.8.4.5, C-GOLD.1.8.4.8.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F058 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_PACKAGE_COMPLETE_RECORD_v1_0.md` | Newly read whole for this correction, all 132 lines; pinned Git blob verified | §§2–3, 5 and 12 establish the accepted standalone status and exact v7 identity used for C-READ.7.2; no behavior sourced from this receipt. EXCLUDED: closure history/process under §1.3; no implementation or integration claimed.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F059 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-e: exact read scope and placement in the current source table; prior credits retained. |
| F060 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F061 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F062 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F063 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F064 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1 and cited sub-parts; C-7B.7.4.7 and cited sub-parts; C-7B.7.5.3 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F065 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F066 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F067 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F068 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1.6 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F069 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F070 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_CANDIDATE_v1_4.md` | Carried through Chapter 3-a: Not yet read; whole file newly read in Chapter 3-b | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-b: EXCLUDED: status/consolidation and workflow narrative under §1.3. Used for locating later accepted owners only; it supplies no behavior in this piece.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F071 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F072 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F073 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F074 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F075 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F076 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F077 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F078 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F079 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | Scoped read in CH04-b: §5 paths 3–4; authority owner/limit cross-check. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F080 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F081 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F082 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F083 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for Bundle 6 mechanics; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F084 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped read in CH04-b: §3 held/sealed restrictions and privacy precedence. Prior read credits retained. | Chapter 3-a: C-STORE.5 / operation protections, B17, B20, B21; other component scopes NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: C-7E, C-7E.2, C-7E.8, C-7E.9.1, C-7E.11, C-7E.12. CH04-b: see the exact source-scope and landing table above.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-c: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F085 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for Origin policy; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F086 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Scoped reread for CH04-a; prior whole-read credit retained where previously recorded | Chapter 3-a: C-STORE.5 / Origin preservation policy; A3.4–A3.5 and other components NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: Navigation excerpt only; no new behavior sourced in this piece.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.7, C-ENGINE-AB.8.; CH04-a: C-7E.12.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F087 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Whole read in CH04-b: Acceptance/status evidence only. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F088 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md` | Whole read in CH04-b: Two-phase authorization/promotion, continuation, C1–C10, nine coordination record types, logging, failure and open implementation choices. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F089 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F090 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F091 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F092 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F093 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F094 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F095 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F096 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F097 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-c: whole read; exact scope and placement in the current source table. |
| F098 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-c: whole read; exact scope and placement in the current source table. |
| F099 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH03-j | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker. |
| F100 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md` | Scoped reread for CH03-j; prior whole-read credit retained where previously recorded | C-READ.10.1.11; C-READ.10.1.12 and all firmness-policy-cited descendants: §§1–6 qualitative outcomes, evidence basis, separations, revision and no-numeric-scoring. EXCLUDED: package history/process; future policy and consumer schemas not invented.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards.; CH03-j: C-ENGINE-C, C-ENGINE-C.10. |
| F101 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F102 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F103 | `05_ACTIVE_CANDIDATE/02-NH_BUNDLE_6_A3_DECISIONS_WORKING_RECORD_v1-1-.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F104 | `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWERS.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F105 | `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWER_PROVENANCE.json` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F106 | `05_ACTIVE_CANDIDATE/Music_Media_Intent_Excerpts.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F107 | `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F108 | `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F109 | `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F110 | `05_ACTIVE_CANDIDATE/NH_A19_REMAINING_HUMAN_EXPERIENCE_DESIGN_PLAN_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F111 | `05_ACTIVE_CANDIDATE/NH_A2_CURRENT_STATUS_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F112 | `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` | Read whole for CH03-n | C-GOLD.1 identities/records/currentness in 3-e; C-GOLD.1.5 operation/execution contracts in 3-f; C-GOLD.1.6 judgment chain/conditional proof in 3-g; C-GOLD.1.7 claim lifecycle/protected recovery in 3-h; derivation, applicability and remaining dependencies NOT PLACED: later pieces; CH03-l: C-GOLD.; CH03-m: C-GOLD.1.8, C-GOLD.1.8.1, C-GOLD.1.8.1.1, C-GOLD.1.8.1.2, C-GOLD.1.8.1.2.1, C-GOLD.1.8.1.2.2, C-GOLD.1.8.1.2.3, C-GOLD.1.8.1.2.4, C-GOLD.1.8.1.2.5, C-GOLD.1.8.1.3, C-GOLD.1.8.1.3.1, C-GOLD.1.8.1.3.2, C-GOLD.1.8.1.3.3, C-GOLD.1.8.1.3.4, C-GOLD.1.8.1.3.5, C-GOLD.1.8.1.4, C-GOLD.1.8.1.4.1, C-GOLD.1.8.1.4.2, C-GOLD.1.8.1.4.3, C-GOLD.1.8.1.5, C-GOLD.1.8.1.5.1, C-GOLD.1.8.1.5.2, C-GOLD.1.8.1.5.2.1, C-GOLD.1.8.1.5.2.2, C-GOLD.1.8.1.5.2.3, C-GOLD.1.8.1.5.3, C-GOLD.1.8.1.6, C-GOLD.1.8.2, C-GOLD.1.8.2.1, C-GOLD.1.8.2.2, C-GOLD.1.8.2.3, C-GOLD.1.8.2.4, C-GOLD.1.8.2.4.1, C-GOLD.1.8.2.4.2, C-GOLD.1.8.2.4.3, C-GOLD.1.8.2.5, C-GOLD.1.8.2.6, C-GOLD.1.8.2.7, C-GOLD.1.8.2.8, C-GOLD.1.8.3, C-GOLD.1.8.4, C-GOLD.1.8.4.1, C-GOLD.1.8.4.2, C-GOLD.1.8.4.2.1, C-GOLD.1.8.4.2.2, C-GOLD.1.8.4.2.3, C-GOLD.1.8.4.3, C-GOLD.1.8.4.3.1, C-GOLD.1.8.4.3.2, C-GOLD.1.8.4.4, C-GOLD.1.8.4.5, C-GOLD.1.8.4.6, C-GOLD.1.8.4.7, C-GOLD.1.8.4.8, C-GOLD.1.8.4.9, C-GOLD.1.8.5.; CH03-n: C-GOLD.1.9, C-GOLD.1.9.1, C-GOLD.1.9.2, C-GOLD.1.9.3, C-GOLD.1.9.4, C-GOLD.1.9.5, C-GOLD.1.9.6, C-GOLD.1.9.7, C-GOLD.1.9.8, C-GOLD.1.9.9, C-GOLD.1.9.10, C-GOLD.1.9.11, C-GOLD.1.9.12, C-GOLD.1.10, C-GOLD.1.11, C-GOLD.1.11.1, C-GOLD.1.11.2, C-GOLD.1.11.3, C-GOLD.1.11.4, C-GOLD.1.11.5, C-GOLD.1.11.6, C-GOLD.1.11.7, C-GOLD.1.11.8, C-GOLD.1.11.9, C-GOLD.1.11.10, C-GOLD.1.11.11, C-GOLD.1.11.12, C-GOLD.1.11.13, C-GOLD.1.11.14, C-GOLD.1.11.15, C-GOLD.1.11.16, C-GOLD.1.11.17, C-GOLD.1.12, C-GOLD.1.12.1, C-GOLD.1.12.2, C-GOLD.1.12.3, C-GOLD.1.12.4, C-GOLD.1.12.5. |
| F113 | `05_ACTIVE_CANDIDATE/NH_B24_REJECTION_CATEGORY_DECISION_2026-09-23_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F114 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F115 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read whole; NHD-B24 row searched for this correction; Chapter 3-c NHD-A2/NHD-SLF and dependency navigation searches, not a whole-file read; Chapter 3-d NHD-B16/NHD-B16EEB navigation only | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; Chapter 3-a: Navigation only: NHD-B11 and NHD-BU1; no behavior sourced from the index; this correction: NHD-B24 navigation for C-READ.7.2 Chapter 3-c: NHD-A2/NHD-SLF navigation only. Chapter 3-d: navigation only, no behavior sourced from index. |
| F116 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F117 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F118 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F119 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F120 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F121 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F122 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-c: whole read; exact scope and placement in the current source table. |
| F123 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_MODEL_CANDOR_AND_HONESTY_STACK_v1_CANDIDATE.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F124 | `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_2026-09-24_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7A.10; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F125 | `05_ACTIVE_CANDIDATE/NH_DESIGN_ANSWERS.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F126 | `05_ACTIVE_CANDIDATE/NH_PERSONAL_IDEA_NOTE_A19_VR_WORLD_ROOMS_OFFLINE_CREATION_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F127 | `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Identity/hash verified; Stage 2 reading pending except FR-0125 and FR-0608 rows checked for this correction (classification and accepted-home pointer only) | NOT PLACED: Appendix B requires Stage 2 rows by FR-ID/title only; no behavior sourced from the ledger. |
| F128 | `05_ACTIVE_CANDIDATE/Other_Future_Feature_Intent_Excerpts.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F129 | `05_ACTIVE_CANDIDATE/Thought_Branches_and_Simulation_Intent.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F130 | `05_INACTIVE_CANDIDATE/NH_FUTURE_MUSIC_UNDERSTANDING_AND_MUSIC_SERVICE_CONNECTIONS_PACKAGE_INTAKE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F131 | `05_INACTIVE_CANDIDATE/NH_ISSUE_CHANNEL_INTENT_v0_1.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F132 | `05_INACTIVE_CANDIDATE/NH_PROVENANCE_FIRST_MULTI_INDEX_MEMORY_FABRIC_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F133 | `05_INACTIVE_CANDIDATE/NH_SECURITY_STORAGE_ENCRYPTION_INTENT_v0_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F134 | `05_INACTIVE_CANDIDATE/NH_TOOLS_FOR_NH_CATEGORY_v0_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F135 | `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F136 | `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_3_CANDIDATE.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F137 | `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | C-7A.6 and cited sub-parts; C-7A.13 and cited sub-parts; C-7A.15 and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. Chapter 3-b: C-READ.7 (excluding the ACCEPTED C-READ.7.2 guard) and C-READ.8 (FR-0125–FR-0133); C-READ.1.12.1 (FR-0123); C-READ.9 (FR-0136).  CH04-c: scoped read; exact scope and placement in the current source table. |
| F138 | `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH00.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | Naming/path continuity only; no Chapters 0–2 (carried placement) behavior sourced from this chapter. |

### V10 heading coverage

| Row | V10 heading | Placement / remaining scope |
|---|---|---|
| V10-H001 | ### This is `NH_MASTER-20_CORRECTED_v10.md`, a corrected candidate in the Master 20 lineage. It is NOT YET ADOPTED. `NH_MASTER-19_CORRECTED_v7_1.md` (SHA-256: `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf`) remains the authoritative immutable Master until Ness explicitly adopts the corrected Master 20. | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H002 | ### Historical provenance (Master 19 lineage): | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H003 | ## 0. THE PREMISE — NEVER DECIDE FACTS (NEVER CLOSE THE BOOK)  [DESIGNED — the floor under every rule] | Partial placement: C-7A and cited sub-parts; C-7B.9.3. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ interpretation remains revisable. |
| V10-H004 | ## 0A. THE TWO MACHINERIES — DUMB vs SMART (psychologics)  [DESIGNED — top-level frame] | Partial placement: C-7A and cited sub-parts; C-7B.1 and cited sub-parts; C-7B.2.5; C-7B.3.2; C-7B.3.3; C-7B.9 and cited sub-parts; C-7B.11 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ record-carriage boundary; no new interpretation by the writer. |
| V10-H005 | ## 0B. FULL-TRANSPARENCY AND LIVING-RECORD LAW  [DESIGNED — foundational operating rule] | C-7A.16 and cited sub-parts; C-7A.17 and cited sub-parts; C-7B and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. Chapter 3-b: C-READ.6 operation records and health-check operation recording.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim.  CH04-b: held-access and required audit-history boundaries. |
| V10-H006 | ## 1. WHAT N.H IS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H007 | ## 1A. THE INPUT-AGNOSTIC PRINCIPLE — ONE ENGINE, MANY FRONT DOORS  [DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading.  CH04-e: C-9A and explicit shared/deferred owners. |
| V10-H008 | ## 2. HOW TO WORK WITH NESS | Chapter 1 placement retained. §2 wording is carried in the marked conflict at C-7B.8; no new C-2 behavior here. |
| V10-H009 | ### 2A. INTERACTION AND ARTIFACT DELIVERY — LOCKED | Chapter 1 placement retained. §2 wording is carried in the marked conflict at C-7B.8; no new C-2 behavior here. |
| V10-H010 | ## 3. THE EVOLUTION — OLD vs NEW (key points) | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H011 | ## 4. THE MACHINE | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H012 | ## 5. THE CODEBASE MAP | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ; C-READ.3; C-READ.4 built functions and paths. |
| V10-H013 | ## 6. WHAT'S BUILT & VERIFIED ON DISK  [BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ built reading boundary.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H014 | ## 6A. THE CODE RULES — `.cursorrules` v3.2 (DUAL-ARCHITECTURE, IN FORCE) | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ record and write constraints.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim. |
| V10-H015 | ### IDENTITY AND PERMANENT RULES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H016 | ### THE THREE-LAYER ARCHITECTURE | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H017 | ### SOVEREIGNTY BOUNDARIES BY LAYER | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.2; C-READ.3; C-READ.5. |
| V10-H018 | ### SCHEMA CONSTRAINTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1 and C-READ.2.  CH04-b: C-TSC.17.8.3 reuses the existing seven-field root-schema card. |
| V10-H019 | ### PRODUCTION READINGS AUTHORIZATION | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.5 and its protections. |
| V10-H020 | ### PROTECTED FILES AND STORES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.4/C-READ.5 destination separation; edit workflow excluded. |
| V10-H021 | ### DRY-RUN PROTOCOL | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H022 | ### §12 INCOMING — CURRENT STATUS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H023 | ## 6B. THE ACCRETIVE STORE — SCHEMA + STATE  [BUILT & VERIFIED] | Partial placement: C-7A.8 and cited sub-parts; C-7B.2.8.4 and cited sub-parts; C-7B.10.1.3; C-7B.11 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ.1 twelve-field representation; C-READ.2; C-READ.3; C-READ.4.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim.  CH04-b: C-TSC.17.8.3 reuses the existing seven-field root-schema card. |
| V10-H024 | ## 7. THE BIG DESIGN — UNIVERSAL FILTER + MEANING ENGINE  [engines A + B BUILT; §§7E–7P core-conceptually designed S17; §§7D and 7Q partially conceptually designed] | C-7A and C-7B detailed subsections follow. NOT PLACED: engine implementation behavior belongs to Group A. |
| V10-H025 | ### 7A — THE UNIVERSAL FILTER (operating rules): | C-7A and cited sub-parts; C-7B.3 and cited sub-parts; C-7B.11 and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. Chapter 3-b: C-READ reciprocal Universal Filter use; principles retained from Chapter 2. |
| V10-H026 | ### 7B — THE MEANING ENGINE (mechanism): | C-7B and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. |
| V10-H027 | ### 7C — THE FORCED BUILD ORDER (never re-fought): | EXCLUDED: forced build order under §1.3. NOT PLACED: engine implementations belong to Group A. |
| V10-H028 | ## 7D. THE LIVING STATE WEB — PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ grounded reading consumer relationship. |
| V10-H029 | ## 7E. CATALOG FRONT DOOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-d: C-14 and explicit shared/deferred owners. |
| V10-H030 | ### §7E-TSC DETAILED DESIGN  [ACCEPTED DESIGN WITH LATER CORRECTIONS — NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-b: full §§1–31 landed in C-TSC and all recursive sub-parts; §31 status evidence only. |
| V10-H031 | ## 7F. CONTEXT RETRIEVAL  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1.9 retrieval audit and genuine no-context audit; retrieval machinery remains with C-7F.  CH05-c: C-7F and explicit shared/deferred owners. |
| V10-H032 | ## 7G. MEANING ENGINE INTERIOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ acceptance/shape distinction and caller relationship; C-READ.3 new-root write handoff also cites the nested §7G-A subsection.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  CH05-a: C-7G and explicit shared/deferred owners.  CH05-b: C-7GA and explicit shared/deferred owners. |
| V10-H033 | ### §7G CREATION-AWARE MODE  [SETTLED CONCEPT — NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-d: C-14 and explicit shared/deferred owners.  CH05-a: C-7G and explicit shared/deferred owners.  CH05-e: C-CREATE and explicit shared/deferred owners. |
| V10-H034 | ## 7H. REREAD LIFECYCLE  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ reread output relationship; detailed orchestration remains with C-7H.  CH05-d: C-7H and explicit shared/deferred owners. |
| V10-H035 | ## 7I. VIEW LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ history/current-view use; view machinery remains with C-7I. |
| V10-H036 | ## 7J. CONTRADICTION AND CLASH HANDLING  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ clash-consumer relationship; clash machinery remains with C-7J. |
| V10-H037 | ## 7K. STORY LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7A.8.3; C-7B.3.1; C-7B.3.3 and cited sub-parts; C-7B.3.4. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ.1.5/1.6 speaker/perspective and embedded-v1-telling boundaries; future telling identity remains for its accepted package.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H038 | ## 7L. PERSON-BOXES  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.4. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ Person-Box consumer relationship. |
| V10-H039 | ## 7M. COMPUTED VIEW  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ current-use consumer relationship. |
| V10-H040 | ## 7N. ACTION SURFACING  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H041 | ## 7O. ACTION-RESULT RETURN PATH  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H042 | ## 7P. PERMISSION AND AUTHORITY BOUNDARIES  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H043 | ## 7Q. PRIVACY, DELETION, AND SENSITIVE-DATA HANDLING  [PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-e: C-9A and explicit shared/deferred owners. |
| V10-H044 | ## 7R. ATTENTION AND RELEVANCE CONTROL  [CORE CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H045 | ### DECISION 1 — OUTPUT FORM | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H046 | ### DECISION 2 — PRODUCER SELECTION | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H047 | ### DECISION 3 — EVALUATION TIMING | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H048 | ### DECISION 4 — TWO-TIER CONFIGURATION CONTRACT | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H049 | ### DECISION 5 — NESS'S RELATIONSHIP | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H050 | ### DECISION 6 — VALIDATION OF MOUTH-PRODUCED DIMENSIONS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H051 | ### DECISION 7 — MINIMUM SHARED VOCABULARY | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H052 | ### DECISION 8 — LIVING STATE WEB BOUNDARY | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H053 | ### DECISION 9 — TIER 1 PURPOSE FIELD | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H054 | ### DECISION 10 — UNRESOLVED DIMENSION HANDLING ACROSS THE TIER BOUNDARY | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H055 | ### DECISION 11 — DISAGREEMENT RECORD SCHEMA | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H056 | ### DECISION 12 — RELEVANCE EVENT RECORD SCHEMA | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H057 | ### DECISION 13 — PATTERN OBSERVATION CONDITIONS FOR PER-JUDGMENT OVERRIDES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H058 | ### DECISION 14 — UNRECOGNIZED PURPOSE TYPE HANDLING | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H059 | ### WHAT REMAINS OPEN FOR ATTENTION AND RELEVANCE CONTROL | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H060 | ## 8. THE RESEARCH PIPELINE  [DESIGNED — Brave not wired] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H061 | ## 9. DESIGNED, NOT BUILT — THE REST  [DESIGNED or CONCEPTUALLY DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H062 | ### §9 RECOVERED ACCESS AND AUTHENTICATION MODEL  [RECOVERED ACCEPTED DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H063 | ### §9 RECOVERED VOICE INPUT/OUTPUT PIPELINE  [RECOVERED PARTIAL DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H064 | ### §9 FIVE PHONE-SIDE MODES  [RECOVERED NAMES ONLY — BEHAVIOR NOT DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H065 | ### §9 PERSONALITY-RELATED CONVERSATION REHEARSAL  [RECOVERED PARTIAL DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H066 | ## 9A. IMAGE INGEST — FIRST WORKED FRONT-DOOR EXAMPLE  [DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading.  CH04-e: C-9A and explicit shared/deferred owners. |
| V10-H067 | ## 10. ORIGINALITY (honest calibration) | Partial placement: C-7B.9.3. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H068 | ## 11. WHAT'S OPEN / NEXT (priority order) | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ foundation status and quarantine/production boundary; restored details use the decision record plus named archive, not the compressed V10 line. |
| V10-H069 | ## 11-SETTLED. (condensed) | EXCLUDED: condensed decision/session narrative under §1.3; repeated runtime rules are represented by their detailed owning sections. |
| V10-H070 | ## 12. SESSION 6 — THE DATA-RESCUE OPERATION  [recovery done; ingest FROZEN] | EXCLUDED: history, provenance or build/process narrative under contract §1.3.  CH04-e: C-9A and explicit shared/deferred owners. |
| V10-H071 | ## 13. THE LIVE LOOP  [DESIGNED — not built] | Partial placement: C-7B.9; C-7B.10.1 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-c: live-loop surface and model boundary in C-13; remaining chat/model internals retain their later owners.  CH04-d: C-14 and explicit shared/deferred owners. |
| V10-H072 | ## 14. THE CHAT FRONT DOOR  [PARTIALLY SETTLED, PARTIALLY OPEN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading.  CH04-c: live-loop surface and model boundary in C-13; remaining chat/model internals retain their later owners.  CH04-d: C-14 and explicit shared/deferred owners.  CH05-e: C-CREATE and explicit shared/deferred owners. |
| V10-H073 | ## 15. SESSION 10 — BOOT HYGIENE + SIGN-IN + .CURSORRULES  [housekeeping done] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H074 | ## 16. THE MODEL LAYER — THE BORROWED MOUTH + THE SEARCH MODEL  [DESIGNED + partly on disk] | Partial placement: C-7B.6. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-c: live-loop surface and model boundary in C-13; remaining chat/model internals retain their later owners. |
| V10-H075 | ## 17. S16 CORRECTION LOG — WHAT THE S16 CORRECTION PASS CHANGED (historical) | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H076 | ## 18. S17 CONSOLIDATION AND CORRECTION LOG | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H077 | ## 19. INTERFACE, WORLD, AND INTERACTION SYSTEM  [IN-PROGRESS DESIGN, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H078 | ### 19A. SETTLED INTERFACE DECISIONS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H079 | ### 19B. PROVISIONAL CONCEPTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H080 | ### 19C. UNANSWERED QUESTIONS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H081 | ### 19D. PAUSED DESIGN POINTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H082 | ### 19E. OPEN DEPENDENCIES (cross-audit results) | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H083 | ### TRUEST SINGLE SENTENCE | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H084 | ## 20. S18 CONSOLIDATION AND CHANGE LOG  [HISTORICAL SESSION SNAPSHOT — June 24 2026] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H085 | ## 21. S19 CONSOLIDATION AND CHANGE LOG  [HISTORICAL SESSION SNAPSHOT — June 25 2026] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H086 | ## 22. WELLBEING AND BEHAVIORAL BASELINE SYSTEM  [DESIGNED — full spec restored S19, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H087 | ## 23. MOBILE APP — THREE-MODE COMPANION  [DESIGNED — full spec restored S19, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H088 | ## 24. CONNECTION CAPABILITY  [CONCEPTUALLY DESIGNED (S19), NOT BUILT] | Partial placement: C-7B.10.6.2.2; C-7B.10.6.2.3; C-7B.10.6.3.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H089 | ## 25. VOICE SECURITY AND IDENTITY SYSTEM  [ACCEPTED DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H090 | ### Build-Time Implementation Settings | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H091 | ### 25.1. BOP — Behavioral Observation Processing | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H092 | ### 25.2. Other-Speaker / Guest / Known-Person Architecture | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H093 | ### 25.3. SIA — Speaker Identity Assessment | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H094 | ### 25.4. SACL — Speaker Access-Control Layer | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H095 | ### 25.5. Wellbeing / Identity / Security Separation Rules | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H096 | ### 25.6. BAI — Biometric Authorization Interface | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H097 | ### One-Time Authorization Token | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H098 | ### Top-Security Biometric Lease | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H099 | ### 25.7. Initial Owner-Phone Pairing | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H100 | ### 25.8. Recovery-Code Lifecycle | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H101 | ### 25.9. Future-Phone Replacement Flow | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H102 | ### 25.10. Atomic Emergency Recovery Flow | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H103 | ### 25.11. Initial Ness Voice-Profile Enrollment Bootstrap | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H104 | ### 25.12. Formally Adopted Vocabulary Additions | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H105 | ### 25.13. BGMM — Biometric-Gated Maintenance Mode | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H106 | ## 26. PERSONAL LEARNING AND ADAPTATION SYSTEM  [ACCEPTED DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H107 | ## 27. HISTORICAL RECOVERY AND CORRECTION LOG — JUNE 25 2026 | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |

### Additional READ-folder files at this source pin

| File | Placement |
|---|---|
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md` | NOT PLACED: outside this evaluation-evidence piece; no content borrowed. |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH01.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH02.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-a.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-b.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-c.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-d.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |

### Carried bridge source landing map

| Bridge section | Cards in this piece |
|---|---|
| §7.13 | C-GOLD.1.7, C-GOLD.1.7.1, C-GOLD.1.7.1.1, C-GOLD.1.7.1.2, C-GOLD.1.7.1.3, C-GOLD.1.7.1.4, C-GOLD.1.7.1.5, C-GOLD.1.7.1.6, C-GOLD.1.7.1.7, C-GOLD.1.7.1.8, C-GOLD.1.7.1.8.1, C-GOLD.1.7.1.8.2, C-GOLD.1.7.1.9, C-GOLD.1.7.1.10, C-GOLD.1.7.1.11, C-GOLD.1.7.1.12, C-GOLD.1.7.1.13, C-GOLD.1.7.1.14, C-GOLD.1.7.1.15, C-GOLD.1.7.1.16, C-GOLD.1.7.2, C-GOLD.1.7.3, C-GOLD.1.7.3.1, C-GOLD.1.7.3.2, C-GOLD.1.7.3.3, C-GOLD.1.7.3.4, C-GOLD.1.7.3.4.1, C-GOLD.1.7.3.4.2, C-GOLD.1.7.3.4.3, C-GOLD.1.7.4, C-GOLD.1.7.4.1, C-GOLD.1.7.4.2, C-GOLD.1.7.4.3, C-GOLD.1.7.4.4, C-GOLD.1.7.4.4.1, C-GOLD.1.7.4.4.1.1, C-GOLD.1.7.4.4.1.2, C-GOLD.1.7.4.5, C-GOLD.1.7.4.6, C-GOLD.1.7.4.7, C-GOLD.1.7.4.7.1, C-GOLD.1.7.4.7.2, C-GOLD.1.7.4.7.3, C-GOLD.1.7.4.7.4, C-GOLD.1.7.4.7.5, C-GOLD.1.7.4.7.6, C-GOLD.1.7.4.7.7, C-GOLD.1.7.5, C-GOLD.1.7.5.1, C-GOLD.1.7.5.2, C-GOLD.1.7.5.3, C-GOLD.1.7.5.4, C-GOLD.1.7.5.5, C-GOLD.1.7.5.6, C-GOLD.1.7.6, C-GOLD.1.7.6.1, C-GOLD.1.7.6.2, C-GOLD.1.7.6.3, C-GOLD.1.7.6.4, C-GOLD.1.7.7, C-GOLD.1.7.8, C-GOLD.1.7.9, C-GOLD.1.7.9.6, C-GOLD.1.7.9.7, C-GOLD.1.7.9.8, C-GOLD.1.7.9.9, C-GOLD.1.7.9.10, C-GOLD.1.7.9.11, C-GOLD.1.7.9.12, C-GOLD.1.7.9.13, C-GOLD.1.7.9.14, C-GOLD.1.7.9.15, C-GOLD.1.7.9.16, C-GOLD.1.7.10, C-GOLD.1.7.10.3, C-GOLD.1.7.10.4, C-GOLD.1.7.10.5 |
| §13.1 | C-GOLD.1.7, C-GOLD.1.7.7, C-GOLD.1.7.7.10, C-GOLD.1.7.9, C-GOLD.1.7.9.1, C-GOLD.1.7.9.2, C-GOLD.1.7.9.3, C-GOLD.1.7.9.4, C-GOLD.1.7.9.5, C-GOLD.1.7.9.6, C-GOLD.1.7.9.7, C-GOLD.1.7.9.8, C-GOLD.1.7.9.9, C-GOLD.1.7.9.10, C-GOLD.1.7.9.11, C-GOLD.1.7.9.12, C-GOLD.1.7.9.13, C-GOLD.1.7.9.14, C-GOLD.1.7.9.15, C-GOLD.1.7.9.16 |
| §13.5 | C-GOLD.1.7, C-GOLD.1.7.7, C-GOLD.1.7.7.1, C-GOLD.1.7.7.2, C-GOLD.1.7.7.3, C-GOLD.1.7.7.4, C-GOLD.1.7.7.5, C-GOLD.1.7.7.6, C-GOLD.1.7.7.7, C-GOLD.1.7.7.8, C-GOLD.1.7.7.9, C-GOLD.1.7.7.10, C-GOLD.1.7.8, C-GOLD.1.7.8.1, C-GOLD.1.7.8.2, C-GOLD.1.7.9, C-GOLD.1.7.9.16, C-GOLD.1.7.10, C-GOLD.1.7.10.3, C-GOLD.1.7.10.4 |
| §10 | C-GOLD.1.7, C-GOLD.1.7.10, C-GOLD.1.7.10.1, C-GOLD.1.7.10.2, C-GOLD.1.7.10.3, C-GOLD.1.7.10.4, C-GOLD.1.7.10.5 |
| §5 | C-GOLD.1.7.1, C-GOLD.1.7.1.16, C-GOLD.1.7.7 |
| §13.4 | C-GOLD.1.7.1, C-GOLD.1.7.7 |
| §7.12 | C-GOLD.1.7.1.2, C-GOLD.1.7.1.3, C-GOLD.1.7.1.4, C-GOLD.1.7.1.8, C-GOLD.1.7.1.8.1, C-GOLD.1.7.1.8.2, C-GOLD.1.7.2, C-GOLD.1.7.4.7, C-GOLD.1.7.4.7.1, C-GOLD.1.7.4.7.2, C-GOLD.1.7.4.7.3, C-GOLD.1.7.4.7.4, C-GOLD.1.7.4.7.5, C-GOLD.1.7.4.7.6, C-GOLD.1.7.4.7.7, C-GOLD.1.7.6, C-GOLD.1.7.9.5, C-GOLD.1.7.9.6, C-GOLD.1.7.9.7, C-GOLD.1.7.9.8, C-GOLD.1.7.9.9, C-GOLD.1.7.9.10, C-GOLD.1.7.9.13, C-GOLD.1.7.9.14 |
| §7.11 | C-GOLD.1.7.6, C-GOLD.1.7.9, C-GOLD.1.7.9.1, C-GOLD.1.7.9.2, C-GOLD.1.7.9.3, C-GOLD.1.7.9.4, C-GOLD.1.7.9.5, C-GOLD.1.7.10.1, C-GOLD.1.7.10.2 |
| §7.2 | C-GOLD.1.7.7.1, C-GOLD.1.7.7.4 |
| §7.9 | C-GOLD.1.7.9.1, C-GOLD.1.7.9.2 |


















## READ RECORD

Each current source identity was checked against its pinned Git blob. Whole-file credit is limited to rows marked Whole; all other reading is scoped. Contract §§5–11 and the complete lessons were reopened before writing; §11.3 is reopened after writing.

| Source file | Reading credit | SHA-256 |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: §7G including the complete creation-aware subsection, and complete §14; only creation-relevant behavior placed here. | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped: Complete C-CREATE and CY-B; related C-13/C-14/C-7G navigation and earlier use lookup. | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped: Complete §§3, 6 and 14–16; header/version-note navigation only. B14 source content is complete; remaining other-component sections retain earlier credits and later owners. | `bc1095955525fcea56cb4d16057c93bfb15eec42a83a1b644baf0e87a473f64e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Scoped: Complete §4 A13, §§6–8 and header; no whole-file credit. | `b37f965a343dbf86130f96591d58de9288ad0a746a68e8ae8fdd7b66208a63da` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Scoped: Complete §5 identities, §8 creation row 5 and surrounding table navigation, §9(g) provisional-material boundary; neighboring §9(h) also read but owned by CH04-e. No whole-file credit. | `5797a2ac51328985e479d2bc101f310b96d2d75976acfaf5f066c529b31d309b` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Scoped: §6 items 1–7 complete and start of item 8, for roots-only RM-CR-01 candidate boundary. Earlier CH05-c declaration content remains its owner. | `b2a5b3fbea75f7123a16c8a45c0fb096f4c4565585a4a0c7b7709e70f27d000e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: Complete acceptance/identity receipt; no new behavior supplied by receipt. | `4b37668ea3a95463e49bc27ada107be78cd807e3cbf8455a06b912901b4346f6` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: Complete acceptance/identity receipt; its earlier pending closeout wording is dated scope, not denial of later accepted closeout. | `c5e379f508f3d2c498dfcecfe567db20db4362872de4feff4c7da57d4ff7de79` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Whole: Complete final receipt including its explicit receipt-audit gate; accepted policy/mechanics/closeout distinguished from unobserved final receipt PASS. | `e397a787911d72533fa0d6245f6331d8d176ea07a21a306d1296b41593dae9c4` |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Scoped: Creation/provisional keyword navigation only; no new creation-store behavior derived from this search. | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` |
| `01_AUTHORITATIVE/cursorrules` | Scoped: Creation/provisional keyword navigation only; unrelated protected-file creation hits are not creation-store architecture. | `5050d08825b93acd72a79d07946e43c8cbe537e079517ccfe66bcae8e30e96e9` |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Scoped: Creation/provisional keyword navigation only; unrelated identity/governance uses are not creation-store architecture. | `cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb` |

Instruction fingerprints:

- Contract v1_0: `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1`.
- Writer lessons v0_1: `635be95b861c181efb3b7bc1b2a8405ab706f864068a0b88f31fb91971adf3e6`.
- Run instructions v0_2: `93431167c0fb03fe1216ebbc12655ac640d71bcb7a59659cd123f51e72a54611`.

### Earlier chapter identities preserved

| Piece | SHA-256 |
|---|---|
| CH00 | `d01e8ec370be9c8e50fbb293c863c95ddaf6f82af5700877bf1a57276a1f4998` |
| CH01 | `f86342e90f8789a5b825fbe73f4bc42041c6537498a32a01980287ad32d47544` |
| CH02 | `22168ca6a6a54a2d142dcc7e1d068ca1ab7270b28a90e8e10c2a0106b595d19a` |
| CH03-a | `3b0ba1cb3ea3415ef71c5343702fd2c7ddcd44675aa8f0b4bf5e7aeab2aa80db` |
| CH03-b | `ba62fb68b050b3840afeabec299b2aa0baac17ba2f79869c1fc031dbc195d8b5` |
| CH03-c | `20d022f2d237cf0a29e4128eae510e0cf153505a2ffd0c64ff512fed9cb06fa6` |
| CH03-d | `9444e60b0b4cb09c1efd5d03c06579af4864f7437a10555fdeca54e50687195c` |
| CH03-e | `a33e27d89548e57f16e8c17b489ca971f3f992101e7664a0260954494f572aa2` |
| CH03-f | `567d566a000971890c22771cbaa9e6fee2669383f02975206013d440e4fb2347` |
| CH03-g | `59f8d76f64e95da500e86644e79a2a9e9cdec6dedd384b0cb5d1536ee1ca2e7f` |
| CH03-h | `af59933e649a92dc1b58dd679fbffad86fa999c2b6ffc36259eda227fea3f582` |
| CH03-i | `bb128e4e4ef9fba5889ee54b90268962d02162e51cb1ff9e5eb6a7e089e3c47f` |
| CH03-j | `0b2bb5079af523e3f101705704316b1092f4a536575eff11ff020bd1eaa13a20` |
| CH03-k | `51c6e87ed42d6bd341dc58a24ef11fb6baaf58bb2e93f7d4a435622382fd1ce3` |
| CH03-l | `b63bcb9f9b411fc79e36b84ddbeb7e87646e651d0ad7b410fbd3d0b9d268e81f` |
| CH03-m | `5354b6bd7903fa4c6e3e3632f6d09a304624da076f49b7fb14e1b1f3b837e2b2` |
| CH03-n | `0cace48ca710e471078de69f5da65c1a26728b7be07b65b15893158546218762` |
| CH03-o | `a531204f2ac54dda00f76f3434e6bd294fab0bb7908a12457f44a09fc1749f5c` |
| CH03-p | `6c43976354a4d2e897112ebd41b935c5a207c2f2f92ed64fa79b24040de6d42d` |
| CH04-a | `1d2bb9e3a3c66f08de6b3d8fb12d5dbad6ae0b1dcc70d395c26dd5e156e12769` |
| CH04-b | `2af41d1f927be32406737cdde4d8d4c3928cf91b7eaa062ffd9810fe6b033bbc` |
| CH04-c | `7176edd53af6853fc9e1e76e7f80204000527196dc2d96283eb6aed02870204b` |
| CH04-d | `901d6eb6474e79a4c14fd2ab096e07fc4e538d2a40c181b07c68ebf70cb2b736` |
| CH04-e | `b4c432cb115b379b300d21c826ce5ea80f10c843af2e13e8b28a2f6b60b88695` |
| CH05-a | `a6bf0cbce2d92e412ad3af4a27909e8cfeb8f15ad0d9b4913c5708eeeed34dd9` |
| CH05-b | `af89c86e7991cdd4c0bb821cd5861abc01e80c9750e6de954062088eaa37b8b9` |
| CH05-c | `dd7e5b17cd4e8e7dae2125d45d30ebdfdcbe349b1f80767c3a8442f5448e0e6d` |
| CH05-d | `67d59453a923647e7616898801e2dcc8ea1ff741d04617886411ad309344285d` |

### READ-folder files not yet read whole

70 inherited pending files remain. Scoped reads do not remove whole-file obligations; previous read credits and source placements remain.

- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/02-NH_BUNDLE_6_A3_DECISIONS_WORKING_RECORD_v1-1-.md`
- `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWERS.md`
- `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWER_PROVENANCE.json`
- `05_ACTIVE_CANDIDATE/Music_Media_Intent_Excerpts.md`
- `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_0.md`
- `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_1.md`
- `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_2.md`
- `05_ACTIVE_CANDIDATE/NH_A19_REMAINING_HUMAN_EXPERIENCE_DESIGN_PLAN_v1_0.md`
- `05_ACTIVE_CANDIDATE/NH_A2_CURRENT_STATUS_v1_1.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_0.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_2.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md`
- `05_ACTIVE_CANDIDATE/NH_DESIGN_ANSWERS.md`
- `05_ACTIVE_CANDIDATE/NH_PERSONAL_IDEA_NOTE_A19_VR_WORLD_ROOMS_OFFLINE_CREATION_v1.md`
- `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/Other_Future_Feature_Intent_Excerpts.md`
- `05_ACTIVE_CANDIDATE/Thought_Branches_and_Simulation_Intent.md`
- `05_INACTIVE_CANDIDATE/NH_FUTURE_MUSIC_UNDERSTANDING_AND_MUSIC_SERVICE_CONNECTIONS_PACKAGE_INTAKE_v1_0_CANDIDATE.md`
- `05_INACTIVE_CANDIDATE/NH_PROVENANCE_FIRST_MULTI_INDEX_MEMORY_FABRIC_MECHANICAL_DESIGN_v1_4_CANDIDATE.md`
- `05_INACTIVE_CANDIDATE/NH_SECURITY_STORAGE_ENCRYPTION_INTENT_v0_1.md`
- `05_INACTIVE_CANDIDATE/NH_TOOLS_FOR_NH_CATEGORY_v0_1.md`
- `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_1.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md`

## CONTRACT CHECK

CONTRACT CHECK (against the cloned contract, SHA-256 e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1)
§1.3 no history/actions/roles/workflow in this chapter: PASS — 72 behavior cards reviewed; 0 project/workflow hits. Source-status and scope notes are outside the behavior cards.
§1.4 every gap written as NOT DECIDED: PASS — 130 empty fields/cells exactly match the register; 12 additional implementation slots are explicit.
§1.5 conflicts marked, none resolved: PASS — 0 explicit conflict-register rows. No direct contradictory creation behavior was silently reconciled. Older open schema/detection/influence wording is distinguished from accepted A13/B14 scope; immutable initial_status from derived status; general provisional-use permission from roots-only RM-CR-01; root-producing shared spine from non-root-producing creation records; accepted packages from the final receipt's still-conditional audit status. Earlier conflicts and the B26 source-scope gap remain explicit.
§3 exactly one stamp per line: PASS — 72 headers, 581 populated fields and 162 USED BY rows checked; 0 BUILT field lines. Relationship stamps follow the named card.
§4 every behavior line cited in the exact format: PASS — 22 distinct current citations resolve at the pin; all populated fields and relationship rows are cited. Claims were reviewed against the mapped source sections.
§5.4 one name per thing: PASS — 72 current IDs checked for duplicates, prior collisions and exact official names; shared atoms retain their previous names.
§6 all template fields present, in order, for every part: PASS — 72 templates and 711 field lines checked.
§6.3 reciprocity within this chapter: PASS — 146 internal lines cover 146 reciprocal pairs; 15 external-use continuations and 3 incoming continuations name both endpoints.
§6.4 every decided detail written in, no citation used in place of content: PASS — Complete mapped B14 content is written: all six base fields with required/conditional status and exact five-type non-empty subset; originating-root and exact-span provenance; four detection-record elements; detector-independent base identity, one concurrent winner, new-version re-evaluation, recorded distinct-fragment handling and disagreement/segmentation rules; seven append-only event families; confirmation route/basis and both later/original evidence sides; explicit direct confirmation versus validated later adoption, ambiguity preservation and all barred automatic inputs; canonical confirmation and derived provisional/confirmed/membership views; provisional permanence and ideas-in-progress availability; provisional_material_used record identity/status-at-use and all four wider consumers; relationship proposals and new larger records with untouched originals; operation identity, atomic record commit, structural duplicate prevention, accepted retry bounds, crash/partial recovery, protective failure, one-operation/one-log and authorization. Unprovided event-key encodings, serialization and challenge-resolution machinery are explicitly open rather than invented.
§6.5 sub-parts recursed to the bottom: PASS — 71 declared child/shared references and 72 owned cards checked; 51 explicit steps have 0 empty TOGETHER cases. Base records, provenance, detection records, confirmation records/proposals and use entries recurse to their supplied fields or evidence elements. The source's five labels are preserved exactly in type_set without inventing type ontologies. Shared detection and stable creation identity retain one ID each. Two confirmation routes, their commits and ambiguity outcome remain distinct; every derived view preserves immutable base history. Generic retry and broad capture/influence policy retain earlier owner IDs.
§9 coverage matrix rows added for every file used: PASS — 12 current source identities, 145 READ-folder inventory rows and 107 V10 heading rows checked; 145 named source paths exist at the pin. Earlier credits and placements remain cumulative.
§10.11 no recommendation, no sentence addressed to Ness: PASS — the behavior was reviewed as system operation and boundaries; 0 formula phrases and 0 project/workflow hits.
Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`.

Computed self-check output:

| Check | Count |
|---|---|
| cards | 72 |
| field_lines | 711 |
| populated_fields | 581 |
| not_decided_boxes | 130 |
| not_decided_fields_and_cells | 130 |
| used_by_rows | 162 |
| relationships | 161 |
| internal_relationships | 146 |
| external_relationships | 15 |
| internal_use_pairs | 146 |
| external_use_pairs | 15 |
| used_by_continuation_rows | 15 |
| incoming_continuation_rows | 3 |
| plain_gates | 0 |
| step_cards_with_empty_together | 0 |
| explicit_step_cards_checked | 51 |
| unique_citations | 22 |
| resolved_citations | 22 |
| named_source_paths_checked | 145 |
| source_identities | 12 |
| whole_read_files | 3 |
| earlier_identities | 28 |
| pending_source_paths | 70 |
| built_field_lines | 0 |
| misfiled_scan_fields | 711 |
| misfiled_scan_used_by_cells | 486 |
| empty_restriction_failure_gate_boxes | 16 |
| formula_hits | 0 |
| wording_hits | 2 |
| wording_verbatim_exceptions | 2 |
| wording_actionable_hits | 0 |
| project_workflow_hits | 0 |
| path_use_rows | 1 |
| path_covered_cards | 72 |
| subpart_references_checked | 71 |
| v10_heading_rows_checked | 107 |
| read_folder_files_covered | 145 |
| source_names_checked | 20 |
| errors | 0 |
| additional_undecided_slots | 12 |
| explicit_source_conflict_records | 0 |

All 711 fields and 486 USED BY cells were reviewed, including 16 remaining empty restriction/failure/gate boxes. Empty cases are atomic identities, form revisions, basis carriers or independent failure behavior not supplied by the sources. All 51 selected action steps have rule connections; provisional use, original-fragment grounding, structural identity, event-backed memberships and protective status reads have explicit gates. There are no plain gates, formula phrases, actionable wording hits or project-workflow content inside cards. No BUILT claim is made. Fifteen outgoing and three incoming continuations preserve earlier names and root stamps.

Two source-verbatim wording exceptions remain in inherited coverage: the A29 closure filename has a space before its extension (line 2098), and V10 heading 15 contains the literal dot-prefixed cursorrules name (line 2221). No actionable wording flags remain.

All 28 earlier completed fingerprints were rechecked and are listed in full. The final count table is compared against a recount after this block is appended. No earlier chapter, repository source or runtime code is changed.
