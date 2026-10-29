# Chapter 6-g — Group D: C-24

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH06-g.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`  

This piece covers the two-part connection capability, waiting, the three acceptance bases, certainty/source types, proposed record schemas and identities, atomic commitment, current-use correction history, all twenty-two crash cases, eleven interface contracts and operation records. It reuses the delivered Person-Box identity-use boundary and B9/logging owners. Full action/authority mechanics remain CH07; privacy, relevance and LMAC CH08; identity/access and visible-output machinery CH09; card presentation CH10-e; assembled side paths CH11. The exact type registry, certainty/new-evidence thresholds, serialization, waiting presentation/scheduling and new-rule creation policy remain gaps.

[SOURCE CONFLICT] The accepted B-INT-8 direct-source route (§5A/§7A) calls its proposed basis `direct_source_relationship`, while its proposed accepted-record and authority-event schemas (§11) enumerate `direct_source`. Both source-specific labels are preserved. Their exact serialization mapping is not decided here; neither spelling silently replaces the other. V10 governs the conceptual direct-recorded-relationship basis without supplying that mechanical label.

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; NHD identifiers locate decisions in the pinned index and do not replace behavior citations.

<!-- BEGIN BEHAVIOR -->

### C-24 — Connection Capability (§24)
Stamp: DESIGNED    Source: [V10 §24] [MAP C-24]

ALONE
- What it is: DESIGNED — The conceptually designed, unbuilt capability for connecting text, voice recordings, images and documents that belong to the same situation or help explain one another, while keeping their originals separate; one ability with an internal two-part split. [V10 §24] [MAP C-24]
- Takes in: DESIGNED — Preserved endpoints, direct recorded relationships, explicit Ness confirmation or a narrowly authorized rule. [V10 §24] [MAP C-24]
- Does: DESIGNED — Keeps a lasting connection record and a current-operation retrieval responsibility, with a waiting area for undecided proposals. [V10 §24]
- Does: ACCEPTED — Uses owner verification, atomic acceptance, separate decision and certainty namespaces, immutable correction history and fresh current-use resolution. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Gives out: DESIGNED — Deliberately accepted relationships or pending investigation guidance, with separate source types and uncertainty. [V10 §24] [MAP C-24]
- Must never: DESIGNED — Merge originals; create a connection from similarity, timing, shared themes, model interpretation or co-retrieval; let acceptance increase certainty. [V10 §24] [MAP C-24]
- Fails closed by: ACCEPTED — Without an approved, verifiable basis, leaves the relationship unknown and unlinked. Failure never gives a proposal factual, identity, recommendation or action force. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

TOGETHER
- Fed by: DESIGNED — C-24.1 — Lasting connection record: accepted records; C-24.2 — Connection retrieval role: retrieval role; C-24.3 — Connection waiting area: waiting; C-24.4 — Connection acceptance bases: acceptance bases; C-24.5 — Connection certainty: certainty; C-24.6 — Connection source-type distinctions: source types. [V10 §24]
- Fed by: ACCEPTED — C-7L.12 — Person-Box generic-connection use boundary: separately governed identity-use result; C-24.7 — Proposed Connection Capability Recordkeeper (CCR): proposed recordkeeper; C-24.8 — Proposed connection type-and-direction contract: proposed type contract; C-24.9 — Connection atomic compare-and-commit: atomic commit; C-24.10 — Connection duplicate identities: proposed relationship and authority keys; C-24.11 — Connection rejection and new-evidence suppression: rejection suppression; C-24.12 — Proposed connection mechanical records: proposed records; C-24.13 — Connection operation lifecycle: lifecycle; C-24.14 — Connection current-use resolution: current use; C-24.15 — Connection Person-Box handoff: identity handoff; C-24.16 — Connection privacy and visible-output boundary: privacy/output boundary; C-24.17 — Connection crash and restart recovery: recovery; C-24.18 — Connection technical retry boundary: retry; C-24.19 — Connection interface contracts: interfaces; C-24.20 — Connection operational recordkeeping: operational records; C-24.21 — Connection fail-closed outcomes: failures. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §3] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §17] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Fed by: ACCEPTED — C-24.22 — Connection-owned durable-operation coordination boundary: connection-owned reference-only coordination boundary. [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §T]
- Fed by: ACCEPTED — C-7B.9.12 — Later-real-evidence separation: supplies Wonder material and later real evidence, under the existing connection, provenance and certainty rules. [04/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md §8] [MAP C-24]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current purpose-specific privacy; C-7P — Permission & Authority Boundaries (§7P): explicit authority for rules and action-related use. [V10 §24] [MAP C-24]
- Changes: DESIGNED — C-7F — Context Retrieval (§7F): provides bounded relationship context and investigation guidance without creating a retrieval-side acceptance authority. [V10 §24] [MAP C-24]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7B.10.6.2.2 — Semantic cold-retrieval fallback | A proposed associative relationship. | Applies the three approved connection bases. | No acceptance from similarity. | [V10 §24] |
| 2 · DESIGNED | C-7B.10.6.3.2 — Valid-link reactivation condition | A proposed new relationship for cold reactivation. | Requires a valid connection before treating it as a new link. | No similarity-only reactivation. | [V10 §24] |
| 3 · ACCEPTED | C-7L.12 — Person-Box generic-connection use boundary | One provenance-bearing generic relationship. | Keeps identity authority and current-use checks separate. | No automatic identity consequence. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] |
| 4 · DESIGNED | C-7F — Context Retrieval (§7F) | Accepted relationships and pending hints. | Keeps the current retrieval operation separate from lasting acceptance. | Bounded context. | [V10 §24] |
| 5 · DESIGNED | C-24.1 — Lasting connection record | The lasting-record responsibility. | Preserves deliberately accepted relationships. | Separate originals. | [V10 §24] |
| 6 · DESIGNED | C-24.2 — Connection retrieval role | The retrieval responsibility. | Gathers current-operation context. | No retrieval acceptance. | [V10 §24] |
| 7 · DESIGNED | C-24.3 — Connection waiting area | The waiting responsibility. | Keeps undecided proposals without force. | Indefinite waiting. | [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6] |
| 8 · DESIGNED | C-24.4 — Connection acceptance bases | The approved-basis boundary. | Limits acceptance to three routes. | No similarity basis. | [V10 §24] |
| 9 · DESIGNED | C-24.5 — Connection certainty | The uncertainty boundary. | Keeps certainty independent of acceptance. | No certainty promotion. | [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |
| 10 · DESIGNED | C-24.6 — Connection source-type distinctions | The source distinctions. | Preserves five separate types. | No source promotion. | [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |
| 11 · ACCEPTED | C-24.7 — Proposed Connection Capability Recordkeeper (CCR) | The recordkeeping scope. | Maintains records without owning authority. | Owner decisions retained. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §3] |
| 12 · ACCEPTED | C-24.8 — Proposed connection type-and-direction contract | Relationship type scope. | Keeps separate versioned types. | No combined relationship. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] |
| 13 · ACCEPTED | C-24.9 — Connection atomic compare-and-commit | The acceptance boundary. | Commits record and proof together. | Recoverable accepted truth. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] |
| 14 · ACCEPTED | C-24.10 — Connection duplicate identities | Logical relationship scope. | Converges duplicates by stable keys. | One relationship history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] |
| 15 · ACCEPTED | C-24.11 — Connection rejection and new-evidence suppression | Rejection history. | Suppresses repetition until genuine new evidence. | No automatic reopening. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10] |
| 16 · ACCEPTED | C-24.12 — Proposed connection mechanical records | Reference-only record requirements. | Preserves distinct immutable records. | No copied content. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 17 · ACCEPTED | C-24.13 — Connection operation lifecycle | Operation progress. | Keeps lifecycle separate from decisions. | No intermediate acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |
| 18 · ACCEPTED | C-24.14 — Connection current-use resolution | Accepted history and later events. | Resolves current-use eligibility. | No stale use. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |
| 19 · ACCEPTED | C-24.15 — Connection Person-Box handoff | Generic relationship provenance. | Hands it to the identity owner. | No identity proof. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 20 · ACCEPTED | C-24.16 — Connection privacy and visible-output boundary | Connection purposes and output. | Applies current owner permissions. | No unauthorized disclosure. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 21 · ACCEPTED | C-24.17 — Connection crash and restart recovery | Interrupted operation truth. | Recovers actual committed records. | No invented authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 22 · ACCEPTED | C-24.18 — Connection technical retry boundary | Technical recovery scope. | Reuses stable identity without decisions. | No retry-made consent. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §17] |
| 23 · ACCEPTED | C-24.19 — Connection interface contracts | Connection boundary requirements. | Keeps all eleven interfaces explicit. | Owner authority retained. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 24 · ACCEPTED | C-24.20 — Connection operational recordkeeping | Real operation history. | Records one parent and actual children. | No log-derived evidence. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |
| 25 · ACCEPTED | C-24.21 — Connection fail-closed outcomes | Unsafe operation facts. | Stops dependent commitment or use. | Honest uncertainty. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20] |
| 26 · ACCEPTED | C-24.22 — Connection-owned durable-operation coordination boundary | Connection-owned claims and effects. | Keeps generic coordination reference-only. | No transferred acceptance authority. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K] |
| 27 · DESIGNED | C-7B.10.6.2.3 — Labeled links to cold originals | A proposed new labeled link to an unchanged cold original. | Applies the §24 connection rules before the link is made. | Nothing in the connection rules. | [V10 §0B] [V10 §24] |
| 28 · CANDIDATE | C-19.17.17 — Deliberate card-to-text association | Ness's selected conversational target and placed card. | Gates this place: retains accepted-connection requirements. | Nothing in this card. | [05/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_2.md §16.3] |
| 29 · ACCEPTED | C-19.21.6 — Wonder and later real evidence | A Wonder item and separately sourced supporting/contradicting real evidence. | Gates this place: governs any accepted connection without identity merging. | Nothing in this card. | [04/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md §8] |
| 30 · ACCEPTED | C-7N.12.3.4 — Surfacing cold-record reactivation | One of those two real triggers. | Gates this place: a triggering link must be valid under its actual connection route and applicable approval rules. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 31 · ACCEPTED | C-7O.13 — Result-return coordination ownership boundary | Typed references to the actual action, root, connection, permission, retry and component outcome records. | Supplies what this place relies on: connection identity, decisions and current-use correction remain component-owned. | Nothing in this card. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §U] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §V.2] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §W] |

SUB-PARTS: C-24.1 — Lasting connection record; C-24.2 — Connection retrieval role; C-24.3 — Connection waiting area; C-24.4 — Connection acceptance bases; C-24.5 — Connection certainty; C-24.6 — Connection source-type distinctions; C-24.7 — Proposed Connection Capability Recordkeeper (CCR); C-24.8 — Proposed connection type-and-direction contract; C-24.9 — Connection atomic compare-and-commit; C-24.10 — Connection duplicate identities; C-24.11 — Connection rejection and new-evidence suppression; C-24.12 — Proposed connection mechanical records; C-24.13 — Connection operation lifecycle; C-24.14 — Connection current-use resolution; C-24.15 — Connection Person-Box handoff; C-24.16 — Connection privacy and visible-output boundary; C-24.17 — Connection crash and restart recovery; C-24.18 — Connection technical retry boundary; C-24.19 — Connection interface contracts; C-24.20 — Connection operational recordkeeping; C-24.21 — Connection fail-closed outcomes; C-24.22 — Connection-owned durable-operation coordination boundary

### C-24.1 — Lasting connection record
Stamp: DESIGNED    Source: [V10 §24]

ALONE
- What it is: DESIGNED — The lasting side of the capability, holding only deliberately accepted connections. [V10 §24]
- Takes in: DESIGNED — Exactly linked endpoints, type, decision status, certainty, confirmer or other acceptance authority, evidence and correction history. [V10 §24]
- Does: DESIGNED — Retains originals and separate relationship types; keeps the acceptance authority distinct from supporting evidence. [V10 §24]
- Gives out: DESIGNED — An inspectable lasting relationship, with certainty independent of acceptance. [V10 §24]
- Must never: DESIGNED — Combine transcript-of, attachment-to, same-source/conversation, same-event, before/after and correction-of types into one relationship. [V10 §24]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.1.1 — Proposed accepted_connection_record: proposed accepted-record schema. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24 — Connection Capability (§24): supplies the preserved accepted relationship. [V10 §24]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | Accepted connection records. | Preserves exact links and their uncertainty. | Lasting relationships. | [V10 §24] |
| 2 · ACCEPTED | C-24.1.1 — Proposed accepted_connection_record | The accepted-record requirement. | Defines its proposed immutable schema. | Inspectable lasting history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: C-24.1.1 — Proposed accepted_connection_record

### C-24.1.1 — Proposed accepted_connection_record
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The append-only proposed accepted_connection_record, containing references rather than copied endpoint content. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Proposed accepted_connection_id; proposed canonical_relationship_key; exact endpoint refs; type and direction; accepted decision status; preserved certainty; acceptance basis; exact authority refs; evidence refs; source labels; accepted-at; known correction/dispute links; schema/record version; integrity reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Commits with recoverable authority proof. The proposed correction/dispute links contain only events known at commit; later events point back to this immutable record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — One accepted version without rewriting its proposal, authority or earlier history. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Add future links by editing the record; count authority or operational records as evidence; copy protected endpoint content. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — An accepted record without its recoverable authority event is not a valid accepted commit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-24.1.1.1 — Proposed accepted_connection_id: proposed accepted identity; C-24.10.1 — Proposed canonical_relationship_key (CRK): proposed relationship key; C-24.12.1 — Proposed connection_endpoint_ref: proposed endpoint refs; C-24.8 — Proposed connection type-and-direction contract: proposed type contract; C-24.3.2 — Connection decision status: decision status; C-24.1.1.2 — Proposed connection acceptance-basis field: basis; C-24.1.1.3 — Proposed connection authority references: authority refs; C-24.1.1.4 — Proposed connection supporting-evidence references: evidence refs; C-24.1.1.5 — Proposed connection accepted-at: accepted-at; C-24.1.1.6 — Proposed accepted-record known correction links: known links; C-24.1.1.7 — Proposed accepted-record schema and record version: versions; C-24.1.1.8 — Proposed connection integrity reference: integrity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fed by: DESIGNED — C-24.5 — Connection certainty: certainty; C-24.6 — Connection source-type distinctions: source types. [V10 §24]
- Gated by: ACCEPTED — C-24.9 — Connection atomic compare-and-commit: the accepted record and authority proof commit as one logical operation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Changes: DESIGNED — C-24.1 — Lasting connection record: supplies the concrete conceptual record shape. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24.1 — Lasting connection record | The proposed accepted record. | Preserves the relationship beside unchanged originals. | Inspectable lasting history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.1.1.1 — Proposed accepted_connection_id | Accepted-record identity scope. | Supplies the stable proposed ID. | Exact addressing. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.1.1.2 — Proposed connection acceptance-basis field | Acceptance provenance slot. | Names the source-specific route basis. | No authority relabeling. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-24.1.1.3 — Proposed connection authority references | Acceptance-authority slot. | Preserves actual authority references. | Recoverable proof. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 5 · ACCEPTED | C-24.1.1.4 — Proposed connection supporting-evidence references | Support-reference slot. | Keeps evidence distinct from authority. | Traceable support. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 6 · ACCEPTED | C-24.1.1.5 — Proposed connection accepted-at | Acceptance timing slot. | Records the actual accepted-at value. | Dated history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 7 · ACCEPTED | C-24.1.1.6 — Proposed accepted-record known correction links | Commit-time correction links. | Retains only already-known events. | Immutable old links. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 8 · ACCEPTED | C-24.1.1.7 — Proposed accepted-record schema and record version | Schema and record identities. | Preserves both version dimensions. | Exact historical form. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 9 · ACCEPTED | C-24.1.1.8 — Proposed connection integrity reference | Record integrity slot. | Carries the integrity reference. | No assumed validity. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 10 · ACCEPTED | C-24.3.2 — Connection decision status | Accepted status slot. | Keeps accepted distinct from certain. | No status conflation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B] |
| 11 · DESIGNED | C-24.5 — Connection certainty | Original certainty. | Preserves the qualitative label. | No acceptance increase. | [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |
| 12 · DESIGNED | C-24.6 — Connection source-type distinctions | Support classification slots. | Keeps exactly one source type per item. | No promoted sources. | [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |
| 13 · ACCEPTED | C-24.8 — Proposed connection type-and-direction contract | Exact relationship type/direction. | Retains the versioned type contract. | Distinct relationship kinds. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] |
| 14 · ACCEPTED | C-24.9 — Connection atomic compare-and-commit | Record commitment requirement. | Binds accepted truth to proof. | No orphan record. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] |
| 15 · ACCEPTED | C-24.10.1 — Proposed canonical_relationship_key (CRK) | Logical relationship identity. | Keys the accepted relationship. | Duplicate convergence. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] |
| 16 · ACCEPTED | C-24.12.1 — Proposed connection_endpoint_ref | Endpoint-reference requirement. | Identifies exact immutable endpoints. | No merged originals. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 17 · ACCEPTED | C-24.22 — Connection-owned durable-operation coordination boundary | Accepted-record and authority-proof references. | Keeps their atomic truth inseparable. | Reference-only recovery. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K] |

SUB-PARTS: C-24.1.1.1 — Proposed accepted_connection_id; C-24.1.1.2 — Proposed connection acceptance-basis field; C-24.1.1.3 — Proposed connection authority references; C-24.1.1.4 — Proposed connection supporting-evidence references; C-24.1.1.5 — Proposed connection accepted-at; C-24.1.1.6 — Proposed accepted-record known correction links; C-24.1.1.7 — Proposed accepted-record schema and record version; C-24.1.1.8 — Proposed connection integrity reference

### C-24.1.1.1 — Proposed accepted_connection_id
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The stable identity of a proposed accepted_connection_record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The accepted relationship reserved or committed under its canonical key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Identifies that accepted record independently of proposal, input and authority-event identities. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A proposed accepted_connection_id. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Re-mint the identity on recovery. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.1.1 — Proposed accepted_connection_record: addresses the accepted record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.1.1 — Proposed accepted_connection_record | The accepted-record identity. | Resolves the exact immutable record. | Stable recovery target. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.1.1.2 — Proposed connection acceptance-basis field
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed record slot naming the approved acceptance route. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Exactly direct_source, ness_confirmation or authorized_rule in the proposed schema. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Separates route authority from certainty and supporting evidence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — The exact source-specific basis label and authority references. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Relabel owner verification as Ness confirmation or a failed source check as supporting authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — A missing or unverified basis cannot establish acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.1.1 — Proposed accepted_connection_record: records why the relationship was accepted. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.1.1 — Proposed accepted_connection_record | The approved route label. | Distinguishes the source, Ness and rule bases. | Explicit acceptance provenance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.1.1.3 — Proposed connection authority references
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed exact references identifying who or what supplied acceptance authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The actual source owner, explicit Ness decision or authorized rule and version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Keeps the authority reference distinct from supporting evidence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Recoverable exact authority references. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Treat a recordkeeper assertion as authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Unrecoverable authority prevents acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.1.1 — Proposed accepted_connection_record: binds acceptance to its actual authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.1.1 — Proposed accepted_connection_record | Exact authority references. | Retains the source of permission to accept. | Auditable basis. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.1.1.4 — Proposed connection supporting-evidence references
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed references to the evidence or reason supporting a relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Immutable source material or explicitly typed support items. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Carries references separately from the confirmer and from the acceptance route. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Supporting-evidence references without copied endpoint content. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Count logs, repeated retrieval or repeated authority proof as additional support. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.1.1 — Proposed accepted_connection_record: preserves evidentiary support; C-24.3.1 — Proposed connection_proposal_record: preserves proposal support. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.1.1 — Proposed accepted_connection_record | Evidence references. | Keeps evidence separate from authority. | Traceable accepted support. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.3.1 — Proposed connection_proposal_record | Proposal evidence references. | Retains the proposed relationship basis for examination. | No evidence from waiting. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.1.1.5 — Proposed connection accepted-at
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed time of acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The successful atomic acceptance event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records when the relationship was accepted. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — The proposed accepted-at value. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Use elapsed time as increased certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.1.1 — Proposed accepted_connection_record: dates acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.1.1 — Proposed accepted_connection_record | Acceptance time. | Keeps the event situated in history. | Dated acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.1.1.6 — Proposed accepted-record known correction links
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed correction/dispute links known when an accepted record commits. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Only already-known correction or dispute event references. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Stores those references immutably; subsequent events point back from new records. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Commit-time correction/dispute links. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Mutate the old list to append later corrections. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.1.1 — Proposed accepted_connection_record: preserves exactly the history known at commit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.1.1 — Proposed accepted_connection_record | Commit-time event links. | Retains an immutable historical snapshot. | No retroactive rewriting. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.1.1.7 — Proposed accepted-record schema and record version
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed version pair distinguishing schema shape and immutable accepted-record version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The schema version and record version at commit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Makes the exact historical form and relationship version addressable. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed schema and record version values. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Substitute a stale accepted version because its original still exists. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.1.1.7.1 — Proposed accepted-record schema version: proposed schema version; C-24.1.1.7.2 — Proposed accepted-record version: proposed record version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.1.1 — Proposed accepted_connection_record: identifies the exact version being preserved. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.1.1 — Proposed accepted_connection_record | Schema and record versions. | Distinguishes successive immutable representations. | Exact version addressing. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.1.1.7.1 — Proposed accepted-record schema version | Schema-version slot. | Identifies the representation shape. | Separate schema identity. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.1.1.7.2 — Proposed accepted-record version | Record-version slot. | Identifies the accepted history version. | Exact immutable version. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: C-24.1.1.7.1 — Proposed accepted-record schema version; C-24.1.1.7.2 — Proposed accepted-record version

### C-24.1.1.7.1 — Proposed accepted-record schema version
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed schema version identifying the conceptual record shape. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The schema version at acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records the representation version independently of the relationship record version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed schema version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.1.1.7 — Proposed accepted-record schema and record version: identifies the record shape. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.1.1.7 — Proposed accepted-record schema and record version | Schema version. | Keeps format identity distinct. | Inspectable schema provenance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.1.1.7.2 — Proposed accepted-record version
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed immutable version of an accepted relationship record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The record version at its commitment. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Makes the accepted version exactly addressable through correction history. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed record version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Overwrite the old version with a correction. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.1.1.7 — Proposed accepted-record schema and record version: identifies the historical relationship version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.1.1.7 — Proposed accepted-record schema and record version | Record version. | Keeps historical versions distinct. | Immutable accepted history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.1.1.8 — Proposed connection integrity reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed integrity reference used by connection records and later resolution. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The integrity evidence for the exact record or event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Carries a reference rather than claiming validity from presence alone. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — An inspectable integrity reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Reconstruct missing integrity proof. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Unavailable or corrupt integrity blocks the dependent commitment or use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.1.1 — Proposed accepted_connection_record: preserves accepted-record integrity; C-24.12.3 — Proposed ness_decision_input: preserves durable-input integrity; C-24.12.6 — Proposed connection_correction_event: preserves correction integrity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.1.1 — Proposed accepted_connection_record | The record integrity reference. | Supports exact-record validation. | No assumed integrity. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.12.3 — Proposed ness_decision_input | The input integrity reference. | Validates the durable selection. | No invented Ness input. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.12.6 — Proposed connection_correction_event | The event integrity reference. | Keeps later corrections verifiable. | Checkable correction chain. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.2 — Connection retrieval role
Stamp: DESIGNED    Source: [V10 §24]

ALONE
- What it is: DESIGNED — The current-operation side of the capability. [V10 §24]
- Takes in: DESIGNED — Accepted connections or pending investigation hints and the current retrieval purpose. [V10 §24]
- Does: DESIGNED — Gathers material while preserving the provenance of what was retrieved and why. [V10 §24]
- Gives out: DESIGNED — Context for this operation without independently creating a lasting relationship. [V10 §24]
- Must never: DESIGNED — Turn co-retrieval into a connection or proposal. [V10 §24]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.2.1 — Accepted-connection retrieval route: accepted-use route; C-24.2.2 — Pending-connection investigation route: investigation-only route; C-24.2.3 — Connection candidate-report retrieval route: candidate-report route; C-24.12.7 — Proposed connection_use_event: proposed use audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13]
- Gated by: DESIGNED — C-7F — Context Retrieval (§7F): its own retrieval rules remain binding. [V10 §24]
- Changes: DESIGNED — C-24 — Connection Capability (§24): supplies operation-scoped context without taking acceptance authority. [V10 §24]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | The retrieval-side result. | Keeps context gathering distinct from record acceptance. | No lasting link from retrieval. | [V10 §24] |
| 2 · ACCEPTED | C-24.2.1 — Accepted-connection retrieval route | Accepted-context responsibility. | Supplies freshly resolved relationship context. | Bounded accepted use. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 3 · ACCEPTED | C-24.2.2 — Pending-connection investigation route | Investigative responsibility. | Supplies separated search guidance. | No evidentiary force. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B] |
| 4 · ACCEPTED | C-24.2.3 — Connection candidate-report retrieval route | Direct-source reporting role. | Submits immutable source references. | No retrieval acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13C] |
| 5 · ACCEPTED | C-24.12.7 — Proposed connection_use_event | Retrieval audit requirement. | Records exact use and non-use. | Inspectable context influence. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D] |

SUB-PARTS: C-24.2.1 — Accepted-connection retrieval route; C-24.2.2 — Pending-connection investigation route; C-24.2.3 — Connection candidate-report retrieval route

### C-24.2.1 — Accepted-connection retrieval route
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — The accepted relationship route through LMAC to Context Retrieval. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — The exact accepted ID/version, purpose and scope, current-use result, certainty, source types and accepted relevance configuration. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Retrieves the currently applicable version and marks accepted status, exact type, certainty, basis, evidence, resolved state, chain consulted and material uncertainty limits in the context package. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — A provenance-bearing context package and proposed connection_use_event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Override or repair positional context, widen access, harden certainty or prove identity from a Person-Box endpoint. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — An unresolved, unavailable, corrupt or contradictory chain, or an unvalidated replacement, produces no use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

TOGETHER
- Fed by: DESIGNED — C-LMAC — Live Mechanism Access Coordinator (§26): stateless routing; C-7F — Context Retrieval (§7F): the actual retrieval operation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A]
- Gated by: ACCEPTED — C-24.14 — Connection current-use resolution: a fresh complete current-use resolution before every use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current internal-use authorization; C-7R — Attention & Relevance Control (§7R): purpose-scoped relevance configuration. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A]
- Changes: DESIGNED — C-24.2 — Connection retrieval role: supplies accepted relationship context. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24.2 — Connection retrieval role | Accepted relationship context. | Carries the exact current-use limits. | Bounded accepted-use route. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A] |
| 2 · ACCEPTED | C-24.14 — Connection current-use resolution | The accepted-use boundary. | Requires fresh current-use resolution. | No stale context. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |
| 3 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual accepted retrieval use. | Records that named child kind. | No added support. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-24.2.2 — Pending-connection investigation route
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]

ALONE
- What it is: ACCEPTED — An investigation-only search route without evidentiary force. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]
- Takes in: ACCEPTED — Exact proposal ID/version, candidate endpoints, investigated type, certainty and the proposed investigation_only_pending_connection marker. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]
- Does: ACCEPTED — Searches, retrieves, compares and checks for genuine source evidence. Keeps returned results separate from evidentiary context; may reach actual owner verification, genuine new evidence or continued unknown status. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]
- Does: DESIGNED — May remain silent while only guiding search; material uncertainty affecting a later claim, interpretation, person statement, recommendation or action is made clear. [V10 §24]
- Gives out: ACCEPTED — Investigation guidance and its audit, with the proposal still undecided. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]
- Must never: ACCEPTED — Support a factual claim, lasting understanding, person/event/cause/intention judgment, important recommendation or external action from the pending link; receive an evaluated-and-set-aside report. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]
- Fails closed by: ACCEPTED — Absent authorization or marker, or guidance confused with evidence, the use stops without accepting or advancing the proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]

TOGETHER
- Fed by: ACCEPTED — C-24.2.2.1 — Proposed investigation_only_pending_connection marker: proposed investigation-only marker; C-24.4.1.3 — Verification-unavailable relationship outcome: an unavailable report enters only when explicitly unverified and separated. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current internal-use authorization. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]
- Gated by: ACCEPTED — C-24.2.2.1 — Proposed investigation_only_pending_connection marker: explicit investigation-only marker; C-24.4.1.3 — Verification-unavailable relationship outcome: unavailable reports require all four exposure conditions. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]
- Changes: DESIGNED — C-24.2 — Connection retrieval role: supplies separated investigation guidance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24.2 — Connection retrieval role | Investigation-only results. | Keeps the possible relationship out of evidentiary context. | No proposal advancement. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B] |
| 2 · ACCEPTED | C-24.2.2.1 — Proposed investigation_only_pending_connection marker | Investigation scope. | Marks the request explicitly investigation-only. | No fact promotion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B] |
| 3 · ACCEPTED | C-24.4.1.3 — Verification-unavailable relationship outcome | Unavailable verification material. | Allows only explicitly unverified guidance. | No verified-source claim. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B] |
| 4 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual investigative use. | Records the investigation child. | No proposal advancement. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: C-24.2.2.1 — Proposed investigation_only_pending_connection marker

### C-24.2.2.1 — Proposed investigation_only_pending_connection marker
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]

ALONE
- What it is: ACCEPTED — The explicit proposed investigation_only_pending_connection scope marker. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]
- Takes in: ACCEPTED — A pending relationship request with exact proposal version and uncertainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]
- Does: ACCEPTED — Marks every downstream use as investigative rather than established fact. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]
- Gives out: ACCEPTED — An explicit proposed investigation_only_pending_connection marker. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]
- Must never: ACCEPTED — Let the prompt or a consumer receive the pending relationship as a fact. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]
- Fails closed by: ACCEPTED — Without the marker the investigation route is not eligible. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.2.2 — Pending-connection investigation route: limits the search guide to investigation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.2.2 — Pending-connection investigation route | The explicit marker. | Keeps search guidance separated from evidence. | No factual force. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B] |

SUB-PARTS: NONE

### C-24.2.3 — Connection candidate-report retrieval route
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13C]

ALONE
- What it is: ACCEPTED — The submission route for a relationship apparently recorded directly in source. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13C]
- Takes in: ACCEPTED — Exact immutable source references and how retrieval encountered them. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13C]
- Does: ACCEPTED — Reports the apparent direct relationship to the proposed recordkeeper for actual source-owner verification. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13C]
- Gives out: ACCEPTED — A separate proposed connection_candidate_report_id. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13C]
- Must never: ACCEPTED — Infer direct provenance from similarity or timing; accept the relationship; automatically turn the report into a proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13C]
- Fails closed by: ACCEPTED — A failed verification leaves no proposal on the failed basis. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13C]

TOGETHER
- Fed by: ACCEPTED — C-24.12.2 — Proposed connection_candidate_report: proposed candidate-report record; C-24.4.1 — Direct recorded relationship route: source-owner verification. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13C]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24.2 — Connection retrieval role: reports a candidate without accepting it. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24.2 — Connection retrieval role | A separate candidate report. | Preserves the encountered references and routes verification to the owner. | No retrieval-side acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13C] |
| 2 · ACCEPTED | C-24.12.2 — Proposed connection_candidate_report | The candidate submission. | Preserves report identity and encounter. | Separate report object. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.3 — Connection waiting area
Stamp: DESIGNED    Source: [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6]

ALONE
- What it is: DESIGNED — The location of proposals awaiting decision, separate from decision status. [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6]
- Takes in: DESIGNED — An undecided proposal admitted through an approved basis. [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6]
- Does: DESIGNED — Waits indefinitely without gaining certainty, factual force or identity force. [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6]
- Gives out: DESIGNED — An undecided relationship that may guide investigation. [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6]
- Must never: DESIGNED — Age waiting into acceptance; change lasting understanding; authorize Person-Box linking/merging or a recommendation/action. [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Without a durable proposal record no proposal exists. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: ACCEPTED — C-24.3.1 — Proposed connection_proposal_record: proposed proposal schema; C-24.3.2 — Connection decision status: three decision states; C-24.13.2 — Connection candidate-report lifecycle: separate candidate-report lifecycle. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24 — Connection Capability (§24): preserves pending uncertainty without force. [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | Pending proposals. | Preserves indefinite undecided status. | No expiry into acceptance. | [V10 §24] |
| 2 · ACCEPTED | C-24.3.1 — Proposed connection_proposal_record | Durable waiting proposal. | Preserves its exact proposed schema. | No report/proposal collapse. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.3.2 — Connection decision status | The waiting decision. | Keeps location out of the status set. | Exactly three statuses. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B] |
| 4 · ACCEPTED | C-24.13.2 — Connection candidate-report lifecycle | Separate report waiting state. | Removes set-aside reports from active waiting. | No failed-basis proposal. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |

SUB-PARTS: C-24.3.1 — Proposed connection_proposal_record; C-24.3.2 — Connection decision status

### C-24.3.1 — Proposed connection_proposal_record
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The append-only proposed connection_proposal_record, separate from a candidate report. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Proposed connection_proposal_id and version; operation ID; canonical key; endpoint refs; type/direction; proposed basis route; evidence refs; source labels; certainty; decision status; optional prior rejection and new delta refs; created-at/source-owner versions; privacy/authority refs; separate candidate-report provenance where applicable. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Preserves proposal versions without in-place edits. Candidate-report provenance remains provenance, never an automatic proposal conversion. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A durable proposed relationship whose undecided status has no force. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Create or preserve a proposal solely on not_verified direct-source evidence; silently inherit an old Ness decision on a new version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — No durable record means no proposal; unverified new evidence is not appended. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-24.3.1.1 — Proposed connection_proposal_id and version: proposed identity/version; C-24.12.9 — Proposed connection_operation: proposed operation; C-24.10.1 — Proposed canonical_relationship_key (CRK): proposed canonical key; C-24.12.1 — Proposed connection_endpoint_ref: proposed endpoint refs; C-24.8 — Proposed connection type-and-direction contract: proposed type; C-24.3.1.2 — Proposed proposal acceptance-basis route: proposed basis route; C-24.1.1.4 — Proposed connection supporting-evidence references: proposed evidence refs; C-24.3.2 — Connection decision status: decision; C-24.3.1.3 — Proposed prior rejected-proposal reference: prior rejection; C-24.3.1.4 — Proposed connection new-evidence delta reference: new delta; C-24.3.1.5 — Proposed proposal created-at and source-owner versions: creation/owner versions; C-24.3.1.6 — Proposed proposal privacy and authority references: privacy/authority refs; C-24.3.1.7 — Proposed proposal candidate-report provenance: candidate-report provenance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fed by: DESIGNED — C-24.5 — Connection certainty: certainty; C-24.6 — Connection source-type distinctions: source-type distinctions. [V10 §24]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): route-level authorization immediately before proposal commit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Changes: DESIGNED — C-24.3 — Connection waiting area: supplies the durable proposal distinct from a report. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24.3 — Connection waiting area | The proposed durable proposal. | Keeps waiting and report identity separate. | An actual undecided object. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.1.1.4 — Proposed connection supporting-evidence references | Proposal support slot. | Carries immutable evidence references. | No support from waiting. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.3.1.1 — Proposed connection_proposal_id and version | Proposal identity/version slot. | Fixes the exact proposed relationship. | Version-specific decisions. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-24.3.1.2 — Proposed proposal acceptance-basis route | Candidate basis slot. | Names an approved route under examination. | No premature authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 5 · ACCEPTED | C-24.3.1.3 — Proposed prior rejected-proposal reference | Prior rejection slot. | Preserves the predecessor backlink. | Visible rejected history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 6 · ACCEPTED | C-24.3.1.4 — Proposed connection new-evidence delta reference | New-evidence slot. | Specifies the exact genuine delta. | No repeated evidence. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 7 · ACCEPTED | C-24.3.1.5 — Proposed proposal created-at and source-owner versions | Creation provenance slots. | Records time and source-owner versions. | Exact origin history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 8 · ACCEPTED | C-24.3.1.6 — Proposed proposal privacy and authority references | Authorization context slots. | Carries privacy and authority references. | No self-permission. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 9 · ACCEPTED | C-24.3.1.7 — Proposed proposal candidate-report provenance | Originating report slot. | Preserves separate report provenance. | No identity conversion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 10 · ACCEPTED | C-24.3.2 — Connection decision status | Proposal decision status. | Retains the actual three-way decision. | No waiting status. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B] |
| 11 · DESIGNED | C-24.5 — Connection certainty | Displayed proposal certainty. | Keeps uncertainty separate from decision. | No acceptance increase. | [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |
| 12 · DESIGNED | C-24.6 — Connection source-type distinctions | Proposal support types. | Preserves the five classifications. | No source promotion. | [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |
| 13 · ACCEPTED | C-24.8 — Proposed connection type-and-direction contract | Proposed type and direction. | Defines the exact relationship at issue. | Separate type semantics. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] |
| 14 · ACCEPTED | C-24.10.1 — Proposed canonical_relationship_key (CRK) | Logical proposal identity. | Keys the relationship history. | No competing duplicate. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] |
| 15 · ACCEPTED | C-24.12.1 — Proposed connection_endpoint_ref | Candidate endpoint slots. | References exact original objects. | No copied endpoint content. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 16 · ACCEPTED | C-24.12.9 — Proposed connection_operation | Parent-operation reference. | Links the proposal to its real operation. | One parent history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: C-24.3.1.1 — Proposed connection_proposal_id and version; C-24.3.1.2 — Proposed proposal acceptance-basis route; C-24.3.1.3 — Proposed prior rejected-proposal reference; C-24.3.1.4 — Proposed connection new-evidence delta reference; C-24.3.1.5 — Proposed proposal created-at and source-owner versions; C-24.3.1.6 — Proposed proposal privacy and authority references; C-24.3.1.7 — Proposed proposal candidate-report provenance

### C-24.3.1.1 — Proposed connection_proposal_id and version
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed stable proposal identity paired with its exact immutable version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The particular proposal and its append-only version chain. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Separates proposal identity from report identity; a genuinely new post-rejection proposal has a new ID. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — An exact proposed connection_proposal_id and version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Recover a report as a proposal or bind an old Ness input silently to a newer version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Stale or superseded versions cannot be silently accepted. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-24.3.1.1.1 — Proposed connection_proposal_id: proposed proposal ID; C-24.3.1.1.2 — Proposed connection proposal version: proposed proposal version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.3.1 — Proposed connection_proposal_record: identifies the exact proposed relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.3.1 — Proposed connection_proposal_record | Exact ID and version. | Keeps decision binding and recovery version-specific. | No silent rebinding. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.3.1.1.1 — Proposed connection_proposal_id | Stable proposal identity slot. | Identifies the proposal separately. | No report ID reuse. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.3.1.1.2 — Proposed connection proposal version | Immutable version slot. | Distinguishes successor evidence versions. | No inherited decision. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-24.12.3.1 — Proposed Ness-input exact proposal binding | Exact proposal identity and version. | Binds durable input to the actual target. | No silent rebinding. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: C-24.3.1.1.1 — Proposed connection_proposal_id; C-24.3.1.1.2 — Proposed connection proposal version

### C-24.3.1.1.1 — Proposed connection_proposal_id
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed stable proposal identity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The actual proposed relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Retains identity across append-only versions; a new post-rejection proposal has a new identity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed connection_proposal_id. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Use a candidate-report ID as the proposal ID. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.3.1.1 — Proposed connection_proposal_id and version: identifies the distinct proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.3.1.1 — Proposed connection_proposal_id and version | Stable proposal ID. | Distinguishes report and proposal. | One proposal identity. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.3.1.1.2 — Proposed connection proposal version
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed exact immutable version of a proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The current or historical proposal version being referenced. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Separates newly appended evidence from the preceding version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed proposal version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Carry an old decision input automatically to the new version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.3.1.1 — Proposed connection_proposal_id and version: makes proposal decisions version-specific. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.3.1.1 — Proposed connection_proposal_id and version | Exact proposal version. | Preserves precise decision binding. | No inherited choice. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.3.1.2 — Proposed proposal acceptance-basis route
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed route slot on an unaccepted proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — An approved direct-source, Ness-confirmation or authorized-rule route under examination. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Names the route without asserting that acceptance has occurred. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A proposed acceptance-basis route. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Use a model judgment, theme, timing or similarity as a fourth basis. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — No approved basis leaves the relationship unknown and unlinked. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.3.1 — Proposed connection_proposal_record: states the route requiring verification. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.3.1 — Proposed connection_proposal_record | The proposed route. | Separates a candidate basis from committed authority. | No premature acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.3.1.3 — Proposed prior rejected-proposal reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed optional backlink from a new proposal to the rejected predecessor. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The earlier rejected proposal where applicable. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Preserves the rejection while linking a genuinely new proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A prior rejected-proposal reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Hide or rewrite the rejection; count predecessor and successor as two votes. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.3.1 — Proposed connection_proposal_record: carries the rejection history. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.3.1 — Proposed connection_proposal_record | The prior rejection reference. | Keeps the old decision visible. | Linked rather than erased history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.3.1.4 — Proposed connection new-evidence delta reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed reference specifying genuinely new evidence where applicable. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The exact new evidence verified by its accepted source/evidence owner. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — States what changed beyond the old rejected basis. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A proposed new-evidence delta reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Treat reformatting, model rewording, reretrieval, repeated similarity, time passing or repeated co-retrieval as a new delta. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — An unestablished genuine delta cannot create a new post-rejection proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.3.1 — Proposed connection_proposal_record: supplies the explicit new basis. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.3.1 — Proposed connection_proposal_record | Verified delta reference. | Preserves exactly what is newly supported. | No repetitive resurfacing. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.11 — Connection rejection and new-evidence suppression | The owner-verified genuine delta. | Requires it before a new post-rejection proposal. | No repetitive reopening. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10] |
| 3 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual new-evidence evaluation. | Records the named child operation. | No new evidence from logs. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-24.3.1.5 — Proposed proposal created-at and source-owner versions
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed creation timestamp and source-owner versions. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The proposal creation event and the actual versions supplying source facts. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Dates the proposal and binds its provenance to the owners used. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed created-at and source-owner version references. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Treat a changed owner version as still verified for commit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Owner-version changes require the route revalidation and block unverified commitment. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-24.3.1.5.1 — Proposed proposal created-at: proposed created-at; C-24.3.1.5.2 — Proposed proposal source-owner versions: proposed source-owner versions. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.3.1 — Proposed connection_proposal_record: preserves creation and source provenance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.3.1 — Proposed connection_proposal_record | Creation time and owner versions. | Retains the provenance applicable to this proposal. | Version-specific history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.3.1.5.1 — Proposed proposal created-at | Creation timestamp slot. | Dates the actual proposal creation. | No age authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.3.1.5.2 — Proposed proposal source-owner versions | Source-owner version slots. | Preserves consulted owner versions. | Checkable provenance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: C-24.3.1.5.1 — Proposed proposal created-at; C-24.3.1.5.2 — Proposed proposal source-owner versions

### C-24.3.1.5.1 — Proposed proposal created-at
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed timestamp of proposal creation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The actual creation event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Dates the proposal without giving age evidentiary force. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed created-at. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Raise certainty from elapsed waiting time. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.3.1.5 — Proposed proposal created-at and source-owner versions: preserves the creation time. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.3.1.5 — Proposed proposal created-at and source-owner versions | Creation time. | Keeps proposal history dated. | No age-based certainty. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.3.1.5.2 — Proposed proposal source-owner versions
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed exact source-owner versions supplying proposal facts. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The owner-held versions consulted. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Preserves those versions for final route revalidation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed source-owner version references. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Assume an owner version stayed unchanged. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.3.1.5 — Proposed proposal created-at and source-owner versions: fixes source provenance versions. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.3.1.5 — Proposed proposal created-at and source-owner versions | Owner versions. | Identifies the actual consulted truth. | Version-specific provenance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.3.1.6 — Proposed proposal privacy and authority references
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed references to current privacy and authority facts relevant to a proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Purpose-specific privacy authorization and the actual authority owner references. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Carries references without copying or manufacturing authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed privacy and authority references. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Make proposal existence grant endpoint access. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Absent or invalid authorization prevents the dependent operation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-24.3.1.6.1 — Proposed proposal privacy references: proposed privacy references; C-24.3.1.6.2 — Proposed proposal authority references: proposed authority references. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.3.1 — Proposed connection_proposal_record: records the authorization context. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.3.1 — Proposed connection_proposal_record | Privacy and authority references. | Preserves applicable authorization provenance. | No self-authorizing proposal. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.3.1.6.1 — Proposed proposal privacy references | Privacy-reference slot. | Carries purpose-specific privacy provenance. | No enduring permission. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.3.1.6.2 — Proposed proposal authority references | Authority-reference slot. | Carries actual route authority provenance. | No committed proof by reference alone. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: C-24.3.1.6.1 — Proposed proposal privacy references; C-24.3.1.6.2 — Proposed proposal authority references

### C-24.3.1.6.1 — Proposed proposal privacy references
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed references to the proposal privacy context. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Purpose-specific privacy owner facts. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Preserves references without making them perpetual permission. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed privacy references. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Grant endpoint access merely from proposal existence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.3.1.6 — Proposed proposal privacy and authority references: preserves privacy provenance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.3.1.6 — Proposed proposal privacy and authority references | Privacy references. | Keeps purpose authorization traceable. | No standing access grant. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.3.1.6.2 — Proposed proposal authority references
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed authority references carried on an undecided proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Actual source, Ness or rule authority references applicable to the route. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Keeps candidate authority provenance separate from committed acceptance proof. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed authority references. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Claim acceptance from a reference alone. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.3.1.6 — Proposed proposal privacy and authority references: preserves route authority provenance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.3.1.6 — Proposed proposal privacy and authority references | Authority references. | Keeps actual ownership visible. | No self-authorizing proposal. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.3.1.7 — Proposed proposal candidate-report provenance
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed optional connection_candidate_report_id provenance slot. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The separate originating Route A-2 report, where one exists. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Cross-references the report without merging its identity or lifecycle with the proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A proposed report reference carried as provenance only. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Make a report automatically become a proposal; preserve a failed direct-source basis as an active proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.3.1 — Proposed connection_proposal_record: retains separate report provenance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.3.1 — Proposed connection_proposal_record | The originating report reference. | Preserves distinct identities. | No automatic promotion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.3.2 — Connection decision status
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]

ALONE
- What it is: ACCEPTED — The three-value decision namespace, separate from certainty and location. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]
- Takes in: ACCEPTED — Exactly undecided, accepted or rejected. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]
- Does: ACCEPTED — Keeps waiting location out of the value set; preserves status through restarts unless an actual decision commits. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]
- Gives out: ACCEPTED — The exact decision status. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]
- Must never: ACCEPTED — Create a fourth waiting status or equate accepted with certain. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]
- Fails closed by: ACCEPTED — No durable decision leaves the proposal undecided. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]

TOGETHER
- Fed by: ACCEPTED — C-24.3.2.1 — Undecided connection decision: undecided; C-24.3.2.2 — Accepted connection decision: accepted; C-24.3.2.3 — Rejected connection decision: rejected. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24.3 — Connection waiting area: distinguishes waiting from decision. [V10 §24]
- Changes: ACCEPTED — C-24.3.1 — Proposed connection_proposal_record: proposal status; C-24.1.1 — Proposed accepted_connection_record: accepted-record status. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24.3 — Connection waiting area | The three-state decision. | Keeps waiting location separate. | No fourth status. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-24.3.1 — Proposed connection_proposal_record | Proposal decision status. | Preserves the actual decision. | No aging into acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.1.1 — Proposed accepted_connection_record | The accepted status. | Records acceptance separately from certainty. | No truth promotion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-24.3.2.1 — Undecided connection decision | The undecided value. | Preserves indefinite unresolved choice. | No force from waiting. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B] |
| 5 · ACCEPTED | C-24.3.2.2 — Accepted connection decision | The accepted value. | Records only complete accepted truth. | No input-only acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B] |
| 6 · ACCEPTED | C-24.3.2.3 — Rejected connection decision | The rejected value. | Preserves rejection and suppression. | No erased decision. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10] |

SUB-PARTS: C-24.3.2.1 — Undecided connection decision; C-24.3.2.2 — Accepted connection decision; C-24.3.2.3 — Rejected connection decision

### C-24.3.2.1 — Undecided connection decision
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]

ALONE
- What it is: ACCEPTED — The undecided value in the decision namespace. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]
- Takes in: ACCEPTED — A durable proposal with no accepted or rejected decision. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]
- Does: ACCEPTED — Waits indefinitely and may guide investigation only. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]
- Gives out: ACCEPTED — The unchanged undecided decision. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]
- Must never: ACCEPTED — Expire into acceptance or gain force from waiting. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.3.2 — Connection decision status: preserves an unresolved decision. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.3.2 — Connection decision status | The undecided value. | Keeps the choice open without force. | Indefinite waiting. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.3.2.2 — Accepted connection decision
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]

ALONE
- What it is: ACCEPTED — The accepted value established by an approved route. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]
- Takes in: ACCEPTED — The complete atomic accepted commit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]
- Does: ACCEPTED — Records acceptance without increasing certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]
- Gives out: ACCEPTED — The accepted decision event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]
- Must never: ACCEPTED — Treat selected input or an intermediate checkpoint as acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]
- Fails closed by: ACCEPTED — Missing recoverable authority prevents accepted truth. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.3.2 — Connection decision status: records the deliberate accepted outcome. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12B]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.3.2 — Connection decision status | The accepted decision. | Separates commitment from certainty. | Accepted does not mean certain. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.3.2.3 — Rejected connection decision
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The rejected value preserved with its decision history. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — A durable valid rejection decision. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Keeps rejection recorded and suppresses repetitive resurfacing; genuine new evidence may justify a new linked proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — The rejected decision and suppression registration. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Delete rejection history, reverse it from silence or auto-retry the decision. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.3.2 — Connection decision status: retains the rejected outcome. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.3.2 — Connection decision status | The rejected decision. | Preserves history and repeat suppression. | No decision erasure. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.4 — Connection acceptance bases
Stamp: DESIGNED    Source: [V10 §24]

ALONE
- What it is: DESIGNED — The three and only three bases for a lasting connection. [V10 §24]
- Takes in: DESIGNED — A direct recorded relationship, Ness explicitly stating/confirming it, or a narrow rule explicitly authorized by Ness. [V10 §24]
- Does: DESIGNED — Keeps each basis distinct and leaves unsupported relationships unknown and unlinked. [V10 §24]
- Gives out: DESIGNED — An approved route requiring its own actual authority. [V10 §24]
- Must never: DESIGNED — Use similarity, timing, theme overlap, interpretation or co-retrieval as acceptance. [V10 §24]
- Fails closed by: DESIGNED — Leaves any relationship without one of the three bases unknown and unlinked. [V10 §24]

TOGETHER
- Fed by: ACCEPTED — C-24.4.1 — Direct recorded relationship route: direct source; C-24.4.2 — Explicit Ness connection decision route: explicit Ness decision; C-24.4.3 — Existing authorized connection-rule route: existing narrow rule. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24 — Connection Capability (§24): limits lasting acceptance to the three bases. [V10 §24]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | An approved acceptance basis. | Keeps ordinary search association from creating lasting truth. | Unknown remains unlinked. | [V10 §24] |
| 2 · ACCEPTED | C-24.4.1 — Direct recorded relationship route | The direct-source basis. | Requires actual owner verification. | No semantic substitute. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] |
| 3 · ACCEPTED | C-24.4.2 — Explicit Ness connection decision route | The Ness-confirmation basis. | Requires exact explicit choice. | No silence consent. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5B] |
| 4 · ACCEPTED | C-24.4.3 — Existing authorized connection-rule route | The narrow-rule basis. | Consumes existing exact authorization. | No broad rule creation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] |

SUB-PARTS: C-24.4.1 — Direct recorded relationship route; C-24.4.2 — Explicit Ness connection decision route; C-24.4.3 — Existing authorized connection-rule route

### C-24.4.1 — Direct recorded relationship route
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A]

ALONE
- What it is: ACCEPTED — The owner-verified source/provenance route, including direct submission and retrieval reporting. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A]
- Takes in: ACCEPTED — A directly attached message attachment or directly generated audio transcript, or another directly verifiable structural relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A]
- Does: ACCEPTED — A-1 receives actual owner verification; A-2 receives a separate retrieval report for owner verification. Only verified_self_establishing may proceed atomically and bypass waiting. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A]
- Gives out: ACCEPTED — Owner verification with exactly one of three outcomes; successful acceptance uses proposed direct_source_relationship, never Ness confirmation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A]
- Must never: ACCEPTED — Let the proposed recordkeeper, retrieval or a model verify in place of the source owner. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A]
- Fails closed by: ACCEPTED — Unavailable verification has no force; not_verified or contradictory results are set aside without a proposal on the failed basis. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A]

TOGETHER
- Fed by: ACCEPTED — C-24.4.1.1 — Connection source-owner verification: actual-owner verification; C-24.4.1.2 — Verified self-establishing relationship outcome: verified outcome; C-24.4.1.3 — Verification-unavailable relationship outcome: unavailable outcome; C-24.4.1.4 — Not-verified relationship outcome: failed outcome. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A]
- Gated by: ACCEPTED — C-24.9.1 — Atomic direct-source commitment: exact precommit revalidation and atomic direct-source commitment. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A]
- Changes: DESIGNED — C-24.4 — Connection acceptance bases: supplies the independently verified structural basis. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24.4 — Connection acceptance bases | Direct source verification. | Allows a self-establishing relationship without manual confirmation. | Distinct source basis. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] |
| 2 · ACCEPTED | C-24.2.3 — Connection candidate-report retrieval route | The actual owner verification route. | Processes a retrieval report without making retrieval an authority. | Three explicit outcomes. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.4.1.1 — Connection source-owner verification | Verification ownership. | Obtains deterministic actual-owner truth. | No substitute verifier. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 4 · ACCEPTED | C-24.4.1.2 — Verified self-establishing relationship outcome | The verified outcome. | Enables the atomic direct route. | No verification-only commitment. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A] |
| 5 · ACCEPTED | C-24.4.1.3 — Verification-unavailable relationship outcome | The unavailable outcome. | Preserves a pending or blocked report. | No factual force. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B] |
| 6 · ACCEPTED | C-24.4.1.4 — Not-verified relationship outcome | The failed outcome. | Sets aside without active proposal. | Unknown and unlinked. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] |
| 7 · ACCEPTED | C-24.9.1 — Atomic direct-source commitment | Verified direct-route facts. | Revalidates immediately before commitment. | One atomic source result. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A] |

SUB-PARTS: C-24.4.1.1 — Connection source-owner verification; C-24.4.1.2 — Verified self-establishing relationship outcome; C-24.4.1.3 — Verification-unavailable relationship outcome; C-24.4.1.4 — Not-verified relationship outcome

### C-24.4.1.1 — Connection source-owner verification
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — Deterministic verification by the actual source/provenance owner. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — Exact immutable evidence and endpoint references, owner identity and owner version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Determines the source relationship rather than an interpretive resemblance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — A durable owner result bound to the submitted report. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Use similarity, timing, theme overlap, model interpretation or co-retrieval as verification. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — No owner result leaves the report unchanged with no force. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.4.1 — Direct recorded relationship route: supplies the only direct-source verification authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.4.1 — Direct recorded relationship route | The actual owner result. | Distinguishes structural provenance from inference. | No substitute verifier. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.9.1 — Atomic direct-source commitment | Actual source-owner verification. | Binds proof to the direct-source commit. | No manufactured verification. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A] |
| 3 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual verification operation. | Records the source-verification child. | No extra evidence. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-24.4.1.2 — Verified self-establishing relationship outcome
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A]

ALONE
- What it is: ACCEPTED — The exact verified_self_establishing verification outcome. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A]
- Takes in: ACCEPTED — Direct deterministic verification by the actual owner. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A]
- Does: ACCEPTED — Hands the relationship to the atomic direct-source route, with immediate precommit revalidation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A]
- Gives out: ACCEPTED — Eligibility for atomic direct-source acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A]
- Must never: ACCEPTED — Treat the verification result alone as an accepted record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A]
- Fails closed by: ACCEPTED — Before the atomic commit no accepted connection exists. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-24.9.1 — Atomic direct-source commitment: the verified result reaches acceptance only through final atomic-route checks. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A]
- Changes: ACCEPTED — C-24.4.1 — Direct recorded relationship route: enables the verified branch. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.4.1 — Direct recorded relationship route | verified_self_establishing. | Continues only through atomic acceptance. | No intermediate accepted truth. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.4.1.3 — Verification-unavailable relationship outcome
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]

ALONE
- What it is: ACCEPTED — The exact verification_unavailable result, distinct from a failed verification. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]
- Takes in: ACCEPTED — An owner verification that is technically unavailable. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]
- Does: ACCEPTED — Preserves the report as verification-pending or technically blocked. Exposes guidance only when explicitly unverified, explicitly investigation-only, separated from evidence and currently privacy-authorized. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]
- Gives out: ACCEPTED — A preserved candidate report without factual, identity, recommendation or action force. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]
- Must never: ACCEPTED — Present it as verified direct evidence or automatically convert it into a normal proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]
- Fails closed by: ACCEPTED — No acceptance occurs and no technical retry invents success. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current internal-use permission for any investigation exposure. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]
- Changes: ACCEPTED — C-24.4.1 — Direct recorded relationship route: retains the unavailable branch; C-24.2.2 — Pending-connection investigation route: permits only explicitly limited guidance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.4.1 — Direct recorded relationship route | verification_unavailable. | Keeps technical uncertainty distinct from authority. | A report with no force. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.2.2 — Pending-connection investigation route | Explicitly unverified investigation-only material. | Keeps it separate from evidentiary context. | No accepted relationship. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Unavailable verification outcome. | Records its own child kind. | No false verified result. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-24.4.1.4 — Not-verified relationship outcome
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A]

ALONE
- What it is: ACCEPTED — The exact not_verified result or a contradictory source-owner result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A]
- Takes in: ACCEPTED — The report and actual negative or contradictory owner result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A]
- Does: ACCEPTED — Preserves both, marks evaluated_and_set_aside and removes the report from active waiting. A later route requires genuine new direct evidence, separate explicit Ness confirmation or a separately valid narrow rule, preserving this failure history. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A]
- Gives out: ACCEPTED — Unknown, unlinked relationship and preserved failure history. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A]
- Must never: ACCEPTED — Create or preserve a proposal solely on the failed basis, repeatedly resurface it, admit it to pending investigation or convert failure to uncertainty evidence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A]
- Fails closed by: ACCEPTED — No direct-source acceptance and no proposal on the failed basis. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.4.1 — Direct recorded relationship route: terminates the failed-source branch. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.4.1 — Direct recorded relationship route | not_verified or contradictory outcome. | Sets aside the failed basis while preserving it. | No active proposal from failed verification. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Not-verified/set-aside outcome. | Records failure without creating a proposal. | No uncertainty evidence. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-24.4.2 — Explicit Ness connection decision route
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5B]

ALONE
- What it is: ACCEPTED — The route for Ness explicitly stating or confirming a relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5B]
- Takes in: ACCEPTED — Exact proposal ID/version, endpoints, connection type, currently displayed certainty and decision-surface version; valid explicit durable Ness input under current identity/access authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5B]
- Does: ACCEPTED — Binds the decision to exactly what was shown. Preserves certainty unless Ness separately explicitly states a different certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5B]
- Gives out: ACCEPTED — An accepted or rejected decision only through its corresponding commit route. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5B]
- Must never: ACCEPTED — Treat silence, inactivity, no answer, continued conversation or opening the proposal as consent; invent a fingerprint, PIN or Personal Mode requirement. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5B]
- Fails closed by: ACCEPTED — A stale proposal fails closed and the current version is surfaced through the accepted output chain. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5B]

TOGETHER
- Fed by: ACCEPTED — C-24.12.3 — Proposed ness_decision_input: proposed durable input; C-24.9.2 — Atomic Ness acceptance commitment: Ness acceptance commit; C-24.9.4 — Connection rejection commitment: rejection commit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5B]
- Gated by: ACCEPTED — C-24.9.2.1 — Ness decision forward-completion gate: all ten recovery conditions for forward-completion. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5B]
- Changes: DESIGNED — C-24.4 — Connection acceptance bases: supplies the explicit Ness basis. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5B]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24.4 — Connection acceptance bases | Explicit Ness choice. | Keeps personal confirmation separate from direct-source verification. | Bounded Ness authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5B] |
| 2 · ACCEPTED | C-24.9.2 — Atomic Ness acceptance commitment | The exact explicit choice. | Binds input and authority in one commit. | No stale acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| 3 · ACCEPTED | C-24.9.2.1 — Ness decision forward-completion gate | Interrupted decision eligibility. | Requires every recovery condition. | Fresh decision on failure. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| 4 · ACCEPTED | C-24.9.4 — Connection rejection commitment | Explicit rejection input. | Commits the actual rejection separately. | No input-only finality. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D] |
| 5 · ACCEPTED | C-24.12.3 — Proposed ness_decision_input | The durable-choice evidence requirement. | Preserves exact selected input. | Separate input identity. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.4.3 — Existing authorized connection-rule route
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]

ALONE
- What it is: ACCEPTED — The route consuming a narrow rule already explicitly authorized by Ness. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Takes in: ACCEPTED — Stable rule_id, exact rule_version, Ness authorization reference, scope, eligible endpoint types, eligible connection types, source/provenance conditions, activation, revocation/supersession and current exact applicability. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Does: ACCEPTED — Matches every declared item and records the match without creating or expanding a rule. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Gives out: ACCEPTED — An applicable or not_applicable result under the actual rule owner. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Must never: ACCEPTED — Treat broad permission to connect related things as sufficient; let a model, similarity score or retrieval create or widen the rule. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Fails closed by: ACCEPTED — Missing, revoked, superseded, out-of-scope or nonmatching rules produce no acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]

TOGETHER
- Fed by: ACCEPTED — C-24.4.3.1 — Connection-rule stable identity and exact version: exact rule identity/version; C-24.4.3.2 — Connection-rule Ness authorization reference: Ness authorization; C-24.4.3.3 — Connection-rule declared scope: declared scope; C-24.4.3.4 — Connection-rule eligible endpoint types: endpoint types; C-24.4.3.5 — Connection-rule eligible connection types: connection types; C-24.4.3.6 — Connection-rule source and provenance conditions: source conditions; C-24.4.3.7 — Connection-rule activation state: activation; C-24.4.3.8 — Connection-rule revocation and supersession state: revocation/supersession; C-24.4.3.9 — Connection-rule exact current applicability: current applicability. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Gated by: DESIGNED — C-7P — Permission & Authority Boundaries (§7P): the existing rule’s proper authority owner. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Gated by: ACCEPTED — C-24.9.3 — Atomic authorized-rule commitment: final exact-rule revalidation and atomic acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Changes: DESIGNED — C-24.4 — Connection acceptance bases: supplies only an already-authorized narrow basis. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24.4 — Connection acceptance bases | A verified narrow rule match. | Retains the rule owner and Ness authorization provenance. | No rule creation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] |
| 2 · ACCEPTED | C-24.4.3.1 — Connection-rule stable identity and exact version | Rule identity requirement. | Preserves exact rule ID/version. | No floating authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C] |
| 3 · ACCEPTED | C-24.4.3.2 — Connection-rule Ness authorization reference | Ness authorization requirement. | References explicit prior permission. | No inferred authorization. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] |
| 4 · ACCEPTED | C-24.4.3.3 — Connection-rule declared scope | Scope requirement. | Requires exact declared scope. | No scope widening. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] |
| 5 · ACCEPTED | C-24.4.3.4 — Connection-rule eligible endpoint types | Endpoint eligibility. | Checks both endpoint types. | No type substitution. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] |
| 6 · ACCEPTED | C-24.4.3.5 — Connection-rule eligible connection types | Relationship-type eligibility. | Checks the exact connection type. | No combined-type permission. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] |
| 7 · ACCEPTED | C-24.4.3.6 — Connection-rule source and provenance conditions | Source conditions. | Verifies actual source/provenance matches. | No similarity proof. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C] |
| 8 · ACCEPTED | C-24.4.3.7 — Connection-rule activation state | Activation requirement. | Checks current active state. | No stale activation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C] |
| 9 · ACCEPTED | C-24.4.3.8 — Connection-rule revocation and supersession state | Invalidation requirement. | Rejects revoked or superseded authority. | No obsolete rule. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C] |
| 10 · ACCEPTED | C-24.4.3.9 — Connection-rule exact current applicability | Current applicability. | Requires the full exact match now. | No cached permission. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C] |
| 11 · ACCEPTED | C-24.9.3 — Atomic authorized-rule commitment | The matched rule route. | Revalidates immediately and commits atomically. | No revoked acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C] |
| 12 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual rule matching. | Records the rule-match child. | No rule authority from a log. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |
| 13 · ACCEPTED | C-7P.14.2 — Existing narrow connection-rule authority interface | Stable rule_id, exact rule_version, Ness authorization reference, scope, eligible endpoint types, eligible connection types, source/provenance conditions, activation, revocation/supersession and current exact applicability. | Supplies the canonical existing authorized-rule route and all required terms. | Nothing in this card. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: C-24.4.3.1 — Connection-rule stable identity and exact version; C-24.4.3.2 — Connection-rule Ness authorization reference; C-24.4.3.3 — Connection-rule declared scope; C-24.4.3.4 — Connection-rule eligible endpoint types; C-24.4.3.5 — Connection-rule eligible connection types; C-24.4.3.6 — Connection-rule source and provenance conditions; C-24.4.3.7 — Connection-rule activation state; C-24.4.3.8 — Connection-rule revocation and supersession state; C-24.4.3.9 — Connection-rule exact current applicability

### C-24.4.3.1 — Connection-rule stable identity and exact version
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]

ALONE
- What it is: ACCEPTED — The rule_id and rule_version required for an authorized-rule match. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Takes in: ACCEPTED — The existing owner’s stable rule ID and exact version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Does: ACCEPTED — Binds the match to that version and revalidates it before acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Gives out: ACCEPTED — Exact rule identity/version references. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Must never: ACCEPTED — Use a changed or superseded version as though it were the matched rule. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Fails closed by: ACCEPTED — An unverifiable version gives no acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]

TOGETHER
- Fed by: ACCEPTED — C-24.4.3.1.1 — Connection-rule rule_id: rule_id; C-24.4.3.1.2 — Connection-rule rule_version: rule_version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.4.3 — Existing authorized connection-rule route: identifies the actual rule. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.4.3 — Existing authorized connection-rule route | Exact rule ID and version. | Retains version-specific authority. | No floating rule match. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.4.3.1.1 — Connection-rule rule_id | Stable rule ID slot. | Locates the actual existing rule. | No invented rule. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] |
| 3 · ACCEPTED | C-24.4.3.1.2 — Connection-rule rule_version | Exact rule version slot. | Fixes the authority version. | No obsolete match. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] |

SUB-PARTS: C-24.4.3.1.1 — Connection-rule rule_id; C-24.4.3.1.2 — Connection-rule rule_version

### C-24.4.3.1.1 — Connection-rule rule_id
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]

ALONE
- What it is: ACCEPTED — The stable rule_id assigned by the actual rule owner. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Takes in: ACCEPTED — The existing authorized rule identity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Does: ACCEPTED — Identifies that rule separately from a proposed connection. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Gives out: ACCEPTED — rule_id. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Must never: ACCEPTED — Invent a rule identity for broad permission. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.4.3.1 — Connection-rule stable identity and exact version: identifies the existing rule. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.4.3.1 — Connection-rule stable identity and exact version | rule_id. | Locates actual existing authority. | No invented rule. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.4.3.1.2 — Connection-rule rule_version
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]

ALONE
- What it is: ACCEPTED — The exact rule_version supplied by the rule owner. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Takes in: ACCEPTED — The current authorized version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Does: ACCEPTED — Preserves exact version identity for matching and final revalidation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Gives out: ACCEPTED — rule_version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Must never: ACCEPTED — Use a superseded version as current authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.4.3.1 — Connection-rule stable identity and exact version: binds the match to a version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.4.3.1 — Connection-rule stable identity and exact version | rule_version. | Keeps authority version-specific. | No stale rule. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.4.3.2 — Connection-rule Ness authorization reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]

ALONE
- What it is: ACCEPTED — The reference to Ness explicitly authorizing the existing rule. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Takes in: ACCEPTED — The owner’s durable explicit authorization reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Does: ACCEPTED — Traces the rule force to that authorization. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Gives out: ACCEPTED — A verifiable Ness authorization reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Must never: ACCEPTED — Infer authorization from broad conversational permission. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Fails closed by: ACCEPTED — Unverified authorization blocks acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.4.3 — Existing authorized connection-rule route: establishes the rule authority provenance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.4.3 — Existing authorized connection-rule route | Ness authorization provenance. | Checks the existing rule authority. | No new permission. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] |

SUB-PARTS: NONE

### C-24.4.3.3 — Connection-rule declared scope
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]

ALONE
- What it is: ACCEPTED — The explicitly authorized scope of the rule. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Takes in: ACCEPTED — The existing rule scope and this exact relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Does: ACCEPTED — Requires an exact scope match. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Gives out: ACCEPTED — A scope-match fact. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Must never: ACCEPTED — Widen scope from resemblance or usefulness. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Fails closed by: ACCEPTED — Out-of-scope relationships are not accepted. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.4.3 — Existing authorized connection-rule route: bounds the matched relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.4.3 — Existing authorized connection-rule route | The exact scope match. | Rejects scope expansion. | Narrow applicability. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] |

SUB-PARTS: NONE

### C-24.4.3.4 — Connection-rule eligible endpoint types
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]

ALONE
- What it is: ACCEPTED — The rule-declared endpoint-type eligibility. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Takes in: ACCEPTED — Both actual endpoint types and the eligible types. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Does: ACCEPTED — Matches endpoints against the authorized type scope. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Gives out: ACCEPTED — An endpoint-type match result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Must never: ACCEPTED — Substitute a similar endpoint category. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Fails closed by: ACCEPTED — Ineligible endpoint types block acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.4.3 — Existing authorized connection-rule route: checks endpoint eligibility. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.4.3 — Existing authorized connection-rule route | Endpoint-type eligibility. | Confines the match to allowed objects. | No type widening. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] |

SUB-PARTS: NONE

### C-24.4.3.5 — Connection-rule eligible connection types
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]

ALONE
- What it is: ACCEPTED — The connection-type set explicitly covered by the rule. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Takes in: ACCEPTED — The actual relationship type and authorized eligible types. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Does: ACCEPTED — Requires the exact relationship type to be eligible. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Gives out: ACCEPTED — A connection-type match result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Must never: ACCEPTED — Combine different relationship types under a broad rule. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]
- Fails closed by: ACCEPTED — An ineligible connection type gives no acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.4.3 — Existing authorized connection-rule route: checks relationship-type eligibility. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.4.3 — Existing authorized connection-rule route | Eligible relationship type. | Keeps the rule type-specific. | No combined-type authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] |

SUB-PARTS: NONE

### C-24.4.3.6 — Connection-rule source and provenance conditions
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]

ALONE
- What it is: ACCEPTED — The source/provenance requirements in the authorized rule. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Takes in: ACCEPTED — The declared conditions and exact immutable source evidence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Does: ACCEPTED — Checks those source conditions before final rule revalidation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Gives out: ACCEPTED — A source-condition match. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Must never: ACCEPTED — Replace provenance conditions with semantic similarity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Fails closed by: ACCEPTED — Unmatched conditions prevent acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.4.3 — Existing authorized connection-rule route: supplies the required source-condition result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.4.3 — Existing authorized connection-rule route | Source-condition evidence. | Verifies the rule conditions on this relationship. | No inferred provenance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] |

SUB-PARTS: NONE

### C-24.4.3.7 — Connection-rule activation state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]

ALONE
- What it is: ACCEPTED — The current active state of the existing rule. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Takes in: ACCEPTED — The actual rule owner activation record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Does: ACCEPTED — Requires currently active authorization, including final revalidation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Gives out: ACCEPTED — The current activation fact. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Must never: ACCEPTED — Treat an inactive rule as active from cached history. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Fails closed by: ACCEPTED — Inactive authorization cannot accept a relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.4.3 — Existing authorized connection-rule route: checks current activation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.4.3 — Existing authorized connection-rule route | Activation state. | Requires an active rule now. | No stale activation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] |

SUB-PARTS: NONE

### C-24.4.3.8 — Connection-rule revocation and supersession state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]

ALONE
- What it is: ACCEPTED — The owner-held revocation or supersession state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Takes in: ACCEPTED — The current rule status immediately before commit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Does: ACCEPTED — Checks that no revocation or replacement invalidates the match. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Gives out: ACCEPTED — A current revocation/supersession result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Must never: ACCEPTED — Use a rule revoked or superseded before commitment. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Fails closed by: ACCEPTED — Either invalidating state prevents acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.4.3 — Existing authorized connection-rule route: blocks stale rule authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.4.3 — Existing authorized connection-rule route | Current invalidation state. | Rejects revoked or superseded rules. | No obsolete authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] |

SUB-PARTS: NONE

### C-24.4.3.9 — Connection-rule exact current applicability
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]

ALONE
- What it is: ACCEPTED — The final applicability of the existing rule to this relationship now. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Takes in: ACCEPTED — All scope, type, source, activation and invalidation facts for the exact relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Does: ACCEPTED — Requires every item to match and revalidates on any doubt before commitment. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Gives out: ACCEPTED — Applicable or not_applicable. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Must never: ACCEPTED — Carry a historical match forward as current authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Fails closed by: ACCEPTED — Uncertain applicability means no acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.4.3 — Existing authorized connection-rule route: supplies the current exact-match result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.4.3 — Existing authorized connection-rule route | Current applicability. | Limits the rule to this exact relationship. | No broad permission. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] |

SUB-PARTS: NONE

### C-24.5 — Connection certainty
Stamp: DESIGNED    Source: [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]

ALONE
- What it is: DESIGNED — The certainty dimension, kept entirely separate from decision status. [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Takes in: DESIGNED — Exactly possible, likely, uncertain, disputed or near-certain. [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Does: DESIGNED — Controls use and how uncertainty is expressed. Near-certain direct recorded relationships ordinarily need no announcement; material uncertainty affecting a claim, interpretation, person statement, recommendation or action must be made clear. [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Gives out: DESIGNED — Preserved qualitative certainty, with no numeric mapping or invented evidence-to-label thresholds. [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Must never: DESIGNED — Raise certainty through acceptance or silently support a certain conclusion with an uncertain link. [V10 §24]
- Must never: ACCEPTED — Raise certainty through repetition, logging or a current-use status. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.5.1 — Possible connection certainty: possible; C-24.5.2 — Likely connection certainty: likely; C-24.5.3 — Uncertain connection certainty: uncertain; C-24.5.4 — Disputed connection certainty: disputed; C-24.5.5 — Near-certain connection certainty: near-certain. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24 — Connection Capability (§24): keeps certainty independent of accepted status. [V10 §24]
- Changes: ACCEPTED — C-24.1.1 — Proposed accepted_connection_record: preserves accepted certainty; C-24.3.1 — Proposed connection_proposal_record: carries proposal certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | Qualitative certainty. | Limits the force and presentation of a relationship. | No acceptance-to-certainty promotion. | [V10 §24] |
| 2 · ACCEPTED | C-24.1.1 — Proposed accepted_connection_record | Unchanged certainty. | Retains proposal or supplied-authority certainty. | No commit-induced increase. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.3.1 — Proposed connection_proposal_record | Proposal certainty. | Keeps the displayed uncertainty distinct from decision. | Explicit tentative scope. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-24.5.1 — Possible connection certainty | The possible label. | Preserves tentative certainty. | No automatic strengthening. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |
| 5 · ACCEPTED | C-24.5.2 — Likely connection certainty | The likely label. | Keeps qualitative likelihood. | No numeric mapping. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |
| 6 · ACCEPTED | C-24.5.3 — Uncertain connection certainty | The uncertain label. | Retains material uncertainty. | No certain conclusion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |
| 7 · ACCEPTED | C-24.5.4 — Disputed connection certainty | The disputed certainty label. | Keeps it separate from use status. | Distinct namespaces. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |
| 8 · ACCEPTED | C-24.5.5 — Near-certain connection certainty | The near-certain label. | Preserves bounded structural certainty. | No wider proof. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |

SUB-PARTS: C-24.5.1 — Possible connection certainty; C-24.5.2 — Likely connection certainty; C-24.5.3 — Uncertain connection certainty; C-24.5.4 — Disputed connection certainty; C-24.5.5 — Near-certain connection certainty

### C-24.5.1 — Possible connection certainty
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The possible certainty label. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Takes in: ACCEPTED — A relationship carrying possible certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Does: ACCEPTED — Preserves this exact qualitative label through acceptance and use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Gives out: ACCEPTED — possible. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Must never: ACCEPTED — Promote possibility from repeated use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24.5 — Connection certainty: supplies a permitted certainty value. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24.5 — Connection certainty | possible. | Retains the tentative label. | No automatic strengthening. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-24.5.2 — Likely connection certainty
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The likely certainty label. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Takes in: ACCEPTED — A relationship carrying likely certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Does: ACCEPTED — Keeps likely separate from accepted and from near-certain. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Gives out: ACCEPTED — likely. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Must never: ACCEPTED — Translate the label into an invented numeric probability. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24.5 — Connection certainty: supplies the likely value. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24.5 — Connection certainty | likely. | Preserves the qualitative value. | No numerical invention. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-24.5.3 — Uncertain connection certainty
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The uncertain certainty label. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Takes in: ACCEPTED — A relationship carrying uncertain certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Does: ACCEPTED — Keeps material uncertainty available to every affected output. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Gives out: ACCEPTED — uncertain. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Must never: ACCEPTED — Silently use the relationship for a certain conclusion. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24.5 — Connection certainty: carries explicit uncertainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24.5 — Connection certainty | uncertain. | Preserves uncertainty in use. | No certain conclusion from the label. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-24.5.4 — Disputed connection certainty
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

ALONE
- What it is: ACCEPTED — The disputed value in the certainty field. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Takes in: ACCEPTED — A relationship whose certainty is disputed. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Does: ACCEPTED — Preserves the certainty namespace separately from the proposed current_use_state disputed value. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Gives out: ACCEPTED — certainty = disputed. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Must never: ACCEPTED — Read a current-use dispute event as this certainty value or vice versa. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24.5 — Connection certainty: carries the disputed certainty value. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24.5 — Connection certainty | certainty = disputed. | Keeps the two namespaces distinct. | No status conflation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |

SUB-PARTS: NONE

### C-24.5.5 — Near-certain connection certainty
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The near-certain certainty label. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Takes in: ACCEPTED — A relationship supplied with near-certain certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Does: ACCEPTED — Preserves the label without generalizing structural provenance beyond its evidence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Gives out: ACCEPTED — near-certain. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Must never: ACCEPTED — Treat direct structural verification as unlimited factual authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24.5 — Connection certainty: supplies the near-certain label. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24.5 — Connection certainty | near-certain. | Keeps evidence scope bounded. | No wider certainty. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-24.6 — Connection source-type distinctions
Stamp: DESIGNED    Source: [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]

ALONE
- What it is: DESIGNED — The five separate source types carried inside a possibility or connection. [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Takes in: DESIGNED — Source material, prior interpretation, assumption, unknown or invented simulation material. [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Does: DESIGNED — Keeps each type separate from certainty, decision, route, relevance, identity and access. [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Gives out: ACCEPTED — Exactly one source-type label per evidence or support item. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Must never: DESIGNED — Collapse types or silently promote one into another. [V10 §24] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.6.1 — Connection source_material label: source_material; C-24.6.2 — Connection prior_interpretation label: prior_interpretation; C-24.6.3 — Connection assumption label: assumption; C-24.6.4 — Connection unknown label: unknown; C-24.6.5 — Connection invented_simulation_material label: invented_simulation_material. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24 — Connection Capability (§24): preserves the five-way source distinction. [V10 §24]
- Changes: ACCEPTED — C-24.1.1 — Proposed accepted_connection_record: labels accepted support; C-24.3.1 — Proposed connection_proposal_record: labels proposal support. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | Distinct source types. | Keeps interpretation and invention separate from source. | No source promotion. | [V10 §24] |
| 2 · ACCEPTED | C-24.1.1 — Proposed accepted_connection_record | Exactly one type per support item. | Preserves evidence classification. | Typed accepted support. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.3.1 — Proposed connection_proposal_record | Exactly one type per support item. | Keeps proposal material distinguishable. | Typed tentative support. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-24.6.1 — Connection source_material label | Original-source classification. | Labels preserved source material. | No derived-source conflation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |
| 5 · ACCEPTED | C-24.6.2 — Connection prior_interpretation label | Interpretation classification. | Labels readings and tellings. | No original-evidence claim. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |
| 6 · ACCEPTED | C-24.6.3 — Connection assumption label | Exploratory-premise classification. | Labels temporary assumptions. | No confirmation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |
| 7 · ACCEPTED | C-24.6.4 — Connection unknown label | Missing-knowledge classification. | Keeps unknown facts unfilled. | No invented content. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |
| 8 · ACCEPTED | C-24.6.5 — Connection invented_simulation_material label | Simulation classification. | Keeps invention visibly simulated. | No real-world relationship proof. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |

SUB-PARTS: C-24.6.1 — Connection source_material label; C-24.6.2 — Connection prior_interpretation label; C-24.6.3 — Connection assumption label; C-24.6.4 — Connection unknown label; C-24.6.5 — Connection invented_simulation_material label

### C-24.6.1 — Connection source_material label
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The source_material label for actual Origins or preserved records. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Takes in: ACCEPTED — Actual preserved source material. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Does: ACCEPTED — Marks the item as original source rather than a later interpretation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Gives out: ACCEPTED — source_material. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Must never: ACCEPTED — Relabel a reading as original evidence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24.6 — Connection source-type distinctions: identifies preserved source material. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24.6 — Connection source-type distinctions | source_material. | Keeps original evidence identifiable. | Source attribution. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-24.6.2 — Connection prior_interpretation label
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The prior_interpretation label for readings or tellings. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Takes in: ACCEPTED — A visibly interpretive derived record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Does: ACCEPTED — Retains its interpretation status inside the connection. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Gives out: ACCEPTED — prior_interpretation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Must never: ACCEPTED — Present the interpretation as original evidence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24.6 — Connection source-type distinctions: identifies derived interpretation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24.6 — Connection source-type distinctions | prior_interpretation. | Preserves derivation rather than source identity. | No evidence promotion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-24.6.3 — Connection assumption label
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The assumption label for a premise temporarily accepted for exploration. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Takes in: ACCEPTED — An explicit exploratory premise. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Does: ACCEPTED — Keeps the premise tentative and separate from a confirmed relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Gives out: ACCEPTED — assumption. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Must never: ACCEPTED — Treat exploration as confirmation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24.6 — Connection source-type distinctions: marks temporary premises. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24.6 — Connection source-type distinctions | assumption. | Keeps the exploratory premise visible. | No confirmed relationship. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-24.6.4 — Connection unknown label
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The unknown label for what is not known. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Takes in: ACCEPTED — An unresolved source fact. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Does: ACCEPTED — Leaves the slot unknown without filling it in. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Gives out: ACCEPTED — unknown. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Must never: ACCEPTED — Invent material to complete the relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24.6 — Connection source-type distinctions: preserves missing knowledge. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24.6 — Connection source-type distinctions | unknown. | Leaves the fact unfilled. | No invented completion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-24.6.5 — Connection invented_simulation_material label
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The invented_simulation_material label for material created only inside a simulation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Takes in: ACCEPTED — Explicitly simulated invention. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Does: ACCEPTED — Keeps simulation origin visibly attached to the item. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Gives out: ACCEPTED — invented_simulation_material. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Must never: ACCEPTED — Silently establish a real-world relationship from invented simulation material. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24.6 — Connection source-type distinctions: distinguishes simulated invention. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24.6 — Connection source-type distinctions | invented_simulation_material. | Preserves the simulation boundary. | No invented real-world link. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-24.7 — Proposed Connection Capability Recordkeeper (CCR)
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The proposed Connection Capability Recordkeeper (CCR), an implementation-neutral record owner. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §3]
- Takes in: ACCEPTED — Owner-supplied source verification, explicit Ness decisions, valid rule matches and properly authorized correction/use requests. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §3]
- Does: ACCEPTED — Owns proposal and accepted-connection records and its own operational state and logs. Records decisions made by their actual owners. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §3]
- Gives out: ACCEPTED — Append-only coordination and relationship records. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §3]
- Must never: ACCEPTED — Own source verification, Person-Box identity, privacy, access, rule creation, certainty judgment or evidence weight. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — An owner contradiction blocks the proposed recordkeeper; the actual owner record wins. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24 — Connection Capability (§24): maintains the connection records without acquiring their authorities. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §3]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | Proposed recordkeeping service. | Commits only owner-supported relationships. | No substitute authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-24.8 — Proposed connection type-and-direction contract
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The proposed versioned contract for an individual connection type. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4]
- Takes in: ACCEPTED — Proposed connection_type_id, type_version and directionality, with directional or symmetric directionality. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4]
- Does: ACCEPTED — Keeps transcript-of, attachment-to, same-source/conversation, same-event, before/after and correction-of relationships distinct. The list is illustrative; the type registry is externally owned and future additions remain open. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4]
- Gives out: ACCEPTED — One explicit type/direction contract per relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4]
- Must never: ACCEPTED — Merge different types into one giant relationship or choose an implementation serialization. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.8.1 — Proposed connection_type_id: proposed type identity; C-24.8.2 — Proposed connection type_version: proposed type version; C-24.8.3 — Proposed connection directionality: proposed directionality. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24 — Connection Capability (§24): preserves separate relationship types. [V10 §24]
- Changes: ACCEPTED — C-24.1.1 — Proposed accepted_connection_record: accepted type/direction; C-24.3.1 — Proposed connection_proposal_record: proposal type/direction. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | The proposed type contract. | Distinguishes the relationship kinds. | No merged types. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] |
| 2 · ACCEPTED | C-24.1.1 — Proposed accepted_connection_record | Exact type and direction. | Keeps the accepted relationship typed. | Versioned type semantics. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.3.1 — Proposed connection_proposal_record | The proposed type and direction. | States the relationship being decided. | Exact decision subject. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-24.8.1 — Proposed connection_type_id | Type identity slot. | Names the exact relationship kind. | Distinct types. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] |
| 5 · ACCEPTED | C-24.8.2 — Proposed connection type_version | Type version slot. | Preserves versioned meaning. | No silent type change. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |
| 6 · ACCEPTED | C-24.8.3 — Proposed connection directionality | Directionality slot. | Distinguishes symmetric and directed contracts. | Correct relationship geometry. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] |
| 7 · ACCEPTED | C-24.10.1 — Proposed canonical_relationship_key (CRK) | Type, directionality and version. | Builds the proposed canonical key. | Correct duplicate scope. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] |

SUB-PARTS: C-24.8.1 — Proposed connection_type_id; C-24.8.2 — Proposed connection type_version; C-24.8.3 — Proposed connection directionality

### C-24.8.1 — Proposed connection_type_id
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The proposed connection_type_id identifying one relationship kind. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4]
- Takes in: ACCEPTED — The external registry identity for the exact type. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4]
- Does: ACCEPTED — Retains distinct type identities even for the same endpoints. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4]
- Gives out: ACCEPTED — A proposed connection_type_id. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4]
- Must never: ACCEPTED — Combine multiple types because their endpoints coincide. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.8 — Proposed connection type-and-direction contract: identifies the relationship kind. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.8 — Proposed connection type-and-direction contract | Type identity. | Keeps kinds separate. | One explicit type. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.8.2 — Proposed connection type_version
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

ALONE
- What it is: ACCEPTED — The proposed type_version of the relationship contract. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Takes in: ACCEPTED — The exact externally owned type version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Does: ACCEPTED — Preserves versioned type meaning in the canonical key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Gives out: ACCEPTED — A proposed type_version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Must never: ACCEPTED — Mutate an old key when type version changes. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.8 — Proposed connection type-and-direction contract: fixes the type semantics used. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.8 — Proposed connection type-and-direction contract | Type version. | Identifies the contract applicable to this record. | No silent type change. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-24.8.3 — Proposed connection directionality
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — The proposed directionality field with exactly directional or symmetric values. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Takes in: ACCEPTED — The type contract and ordered or symmetric endpoint relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Does: ACCEPTED — Preserves A-to-B versus B-to-A for directional types; symmetric types permit deterministic endpoint-order normalization. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Gives out: ACCEPTED — Proposed directionality = directional or symmetric. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Must never: ACCEPTED — Collapse opposite directional relationships. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.8.3.1 — Proposed directional connection type: proposed directional value; C-24.8.3.2 — Proposed symmetric connection type: proposed symmetric value. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.8 — Proposed connection type-and-direction contract: supplies the type direction rule. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.8 — Proposed connection type-and-direction contract | The directionality rule. | Distinguishes directed and symmetric relationships. | Correct key geometry. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] |
| 2 · ACCEPTED | C-24.8.3.1 — Proposed directional connection type | Directed relationship semantics. | Preserves endpoint order. | Different reverse relationship. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] |
| 3 · ACCEPTED | C-24.8.3.2 — Proposed symmetric connection type | Symmetric relationship semantics. | Normalizes endpoint ordering. | One symmetric key. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] |

SUB-PARTS: C-24.8.3.1 — Proposed directional connection type; C-24.8.3.2 — Proposed symmetric connection type

### C-24.8.3.1 — Proposed directional connection type
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — The proposed directional directionality value. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Takes in: ACCEPTED — A directed type and ordered endpoints. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Does: ACCEPTED — Preserves direction so A-to-B and B-to-A have different relationship keys. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Gives out: ACCEPTED — Proposed directional type semantics. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Must never: ACCEPTED — Normalize opposite directions into one relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.8.3 — Proposed connection directionality: supplies directed identity semantics. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.8.3 — Proposed connection directionality | Proposed directional. | Preserves endpoint direction. | Different reverse relationship. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-24.8.3.2 — Proposed symmetric connection type
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — The proposed symmetric directionality value. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Takes in: ACCEPTED — A symmetric type and its endpoint identities. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Does: ACCEPTED — Normalizes endpoint order deterministically so reversed presentation yields one key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Gives out: ACCEPTED — Proposed symmetric type semantics. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Must never: ACCEPTED — Create duplicate relationships from reversed endpoint presentation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.8.3 — Proposed connection directionality: supplies symmetric identity semantics. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §4] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.8.3 — Proposed connection directionality | Proposed symmetric. | Normalizes endpoint ordering. | One symmetric relationship. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-24.9 — Connection atomic compare-and-commit
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The one implementation-neutral recoverable acceptance boundary, keyed by the proposed canonical_relationship_key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7]
- Takes in: ACCEPTED — The exact accepted record, authority proof, proposed authority_event_key, final proposal-decision event where a proposal exists, and parent checkpoint. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7]
- Does: ACCEPTED — Makes duplicate comparison, accepted-record creation and authority-event writing the same logical operation. Proof is durable before authority takes effect or durably included in that commit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7]
- Gives out: ACCEPTED — One complete accepted commitment and its recoverable proof. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7]
- Must never: ACCEPTED — Expose intermediate coordination as acceptance, race duplicate checking against commitment, or leave an accepted connection without proof. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Partial, contradictory or unknown commitment blocks acceptance until exact identities resolve it. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7]

TOGETHER
- Fed by: ACCEPTED — C-24.9.1 — Atomic direct-source commitment: direct route; C-24.9.2 — Atomic Ness acceptance commitment: Ness route; C-24.9.3 — Atomic authorized-rule commitment: rule route; C-24.9.4 — Connection rejection commitment: separate rejection route; C-24.10 — Connection duplicate identities: proposed duplicate identities. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24 — Connection Capability (§24): establishes recoverable acceptance. [V10 §24]
- Changes: ACCEPTED — C-24.1.1 — Proposed accepted_connection_record: binds the proposed accepted record to its proof. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | The complete atomic outcome. | Recognizes accepted truth only with recoverable authority. | No split acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] |
| 2 · ACCEPTED | C-24.1.1 — Proposed accepted_connection_record | Atomic commitment and proof. | Keeps the proposed record valid only as part of the complete commit. | No orphan accepted record. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.9.1 — Atomic direct-source commitment | The shared atomic boundary. | Commits direct-source proof and record together. | One source-authorized result. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A] |
| 4 · ACCEPTED | C-24.9.2 — Atomic Ness acceptance commitment | The shared atomic boundary. | Commits Ness input, final decision and proof together. | One Ness-authorized result. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| 5 · ACCEPTED | C-24.9.3 — Atomic authorized-rule commitment | The shared atomic boundary. | Commits exact rule authority and record together. | One rule-authorized result. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C] |
| 6 · ACCEPTED | C-24.9.4 — Connection rejection commitment | The separate rejection boundary. | Preserves final rejection and suppression. | No accepted relationship. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D] |
| 7 · ACCEPTED | C-24.10 — Connection duplicate identities | The compare-and-commit identity scope. | Prevents duplicate racing results. | Stable relationship history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] |

SUB-PARTS: C-24.9.1 — Atomic direct-source commitment; C-24.9.2 — Atomic Ness acceptance commitment; C-24.9.3 — Atomic authorized-rule commitment; C-24.9.4 — Connection rejection commitment

### C-24.9.1 — Atomic direct-source commitment
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A]

ALONE
- What it is: ACCEPTED — The ordered commit route after verified_self_establishing owner verification. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A]
- Takes in: ACCEPTED — Immutable evidence and the actual source-owner verification. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A]
- Does: ACCEPTED — Revalidates immediately before commit: exact owner, owner version, immutable evidence refs, verification result, current privacy, canonical-key duplicate state and authority-event identity. Commits or durably references all verification, owner identity/version, evidence, proposed direct_source_relationship basis, exact authority-event ID, accepted record and key result; then completes the operation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A]
- Gives out: ACCEPTED — One direct-source accepted record with its authority proof. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A]
- Must never: ACCEPTED — Add a Ness-confirmation label or append the same authority event on recovery. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A]
- Fails closed by: ACCEPTED — Crash before commit leaves no accepted connection; after commit recovery finds the complete existing one. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A]

TOGETHER
- Fed by: ACCEPTED — C-24.4.1.1 — Connection source-owner verification: actual owner verification. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): immediately-before-commit internal-use authorization. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A]
- Changes: ACCEPTED — C-24.9 — Connection atomic compare-and-commit: supplies a source-authorized atomic result; C-24.4.1 — Direct recorded relationship route: enforces the direct route commit boundary. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.9 — Connection atomic compare-and-commit | The source-authorized atomic result. | Preserves proof and record together. | No split source acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.4.1 — Direct recorded relationship route | The final direct-source checks. | Requires owner verification and exact revalidation. | No premature accepted state. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A] |
| 3 · ACCEPTED | C-24.17.10 — Connection crash after verified source before commit | Final direct-route revalidation. | Repeats exact checks after interruption. | No precommit acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 4 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual direct-source commitment. | Records the commitment child. | No new confirmation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |
| 5 · ACCEPTED | C-24.4.1.2 — Verified self-establishing relationship outcome | The atomic direct-route boundary. | Requires final revalidation after verified status. | No verification-only accepted truth. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A] |

SUB-PARTS: NONE

### C-24.9.2 — Atomic Ness acceptance commitment
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

ALONE
- What it is: ACCEPTED — The ordered acceptance route binding an explicit Ness choice to the exact current proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Takes in: ACCEPTED — Current decision-eligible proposal version and valid durable Ness input under current accepted identity/access rules. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Does: ACCEPTED — Immediately verifies proposal ID/version, endpoints, type/direction, displayed certainty, surface version/integrity, input, current authority, privacy, proposal/key duplicate state and absence of conflicting decision/correction/rejection/supersession. One atomic commit binds that version, input, authority context, accepted record, final accepted event, Ness-confirmation authority event and key result; then completes the operational log. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Gives out: ACCEPTED — The accepted record, authority proof and final accepted decision as one recoverable logical commit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Must never: ACCEPTED — Confuse durable input, final decision, accepted record or authority event; silently rebind stale input or inherit it on a corrected/new-evidence version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Fails closed by: ACCEPTED — A failed recovery condition preserves the old input as history, keeps or marks the stale/superseded version, blocks completion and requires a fresh decision on the current version through the output chain. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

TOGETHER
- Fed by: ACCEPTED — C-24.12.3 — Proposed ness_decision_input: proposed durable input; C-24.12.4 — Proposed connection_decision_event: proposed final decision event; C-24.12.5 — Proposed connection_authority_event: proposed authority event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Gated by: ACCEPTED — C-24.9.2.1 — Ness decision forward-completion gate: all ten forward-completion conditions. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): route-level authorization immediately before the final commit; C-9 — Access/authentication model + voice I/O + phone modes (§9): current accepted identity/access authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Changes: ACCEPTED — C-24.9 — Connection atomic compare-and-commit: supplies the Ness-authorized commit; C-24.4.2 — Explicit Ness connection decision route: binds explicit acceptance to the displayed proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.9 — Connection atomic compare-and-commit | The Ness-authorized atomic result. | Recovers all commitment parts together. | No input-only acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.4.2 — Explicit Ness connection decision route | Exact final commit. | Keeps the explicit choice bound to its version. | No stale acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| 3 · ACCEPTED | C-24.9.2.1 — Ness decision forward-completion gate | The interrupted acceptance boundary. | Checks all ten recovery conditions. | No stale completion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| 4 · ACCEPTED | C-24.12.3 — Proposed ness_decision_input | Required durable input. | Preserves actual selection separately. | No input-only acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 5 · ACCEPTED | C-24.12.4 — Proposed connection_decision_event | Required final decision. | Records the actual committed proposal status. | Separate final truth. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 6 · ACCEPTED | C-24.12.5 — Proposed connection_authority_event | Required authority proof. | Preserves the exact Ness-confirmation event. | Recoverable atomic proof. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: C-24.9.2.1 — Ness decision forward-completion gate

### C-24.9.2.1 — Ness decision forward-completion gate
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

ALONE
- What it is: ACCEPTED — The conjunction of ten conditions required to finish a durable Ness input after interruption. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Takes in: ACCEPTED — The exact input, current proposal, integrity, authority, surface facts and committed history. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Does: ACCEPTED — Allows completion only while every condition remains true; otherwise preserves history and requires a fresh decision on the current visible version through the accepted output chain. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Gives out: ACCEPTED — Allowed idempotent completion or fresh-decision-required. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Must never: ACCEPTED — Silently rebind the input to a newer version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Fails closed by: ACCEPTED — Any failed condition prevents forward-completion. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-24.9.2.1.1 — Forward-completion exact proposal binding: exact binding; C-24.9.2.1.2 — Forward-completion current decision eligibility: eligible current version; C-24.9.2.1.3 — Forward-completion input integrity: integrity; C-24.9.2.1.4 — Forward-completion recovery authority: recovery authority; C-24.9.2.1.5 — Forward-completion surface and certainty match: display match; C-24.9.2.1.6 — Forward-completion no conflicting acceptance: no conflicting acceptance; C-24.9.2.1.7 — Forward-completion no committed rejection: no rejection; C-24.9.2.1.8 — Forward-completion no correction-caused staleness: no correction staleness; C-24.9.2.1.9 — Forward-completion no superseding proposal: no superseding version; C-24.9.2.1.10 — Forward-completion no current authority or privacy block: no authority/privacy block. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Changes: ACCEPTED — C-24.9.2 — Atomic Ness acceptance commitment: governs interrupted acceptance; C-24.4.2 — Explicit Ness connection decision route: prevents old decisions from authorizing new versions. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.9.2 — Atomic Ness acceptance commitment | The ten-condition result. | Completes only an unchanged valid decision. | No invalid recovery. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| 2 · ACCEPTED | C-24.4.2 — Explicit Ness connection decision route | Recovery eligibility. | Preserves the explicit-choice boundary. | Fresh decision when required. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| 3 · ACCEPTED | C-24.9.2.1.1 — Forward-completion exact proposal binding | Exact binding requirement. | Checks proposal ID and version. | No rebinding. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| 4 · ACCEPTED | C-24.9.2.1.2 — Forward-completion current decision eligibility | Current eligibility requirement. | Checks the still-current decision subject. | No stale completion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| 5 · ACCEPTED | C-24.9.2.1.3 — Forward-completion input integrity | Integrity requirement. | Validates durable input integrity. | No fabricated selection. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| 6 · ACCEPTED | C-24.9.2.1.4 — Forward-completion recovery authority | Recovery authority requirement. | Checks actual identity/access validity. | No reconstructed authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| 7 · ACCEPTED | C-24.9.2.1.5 — Forward-completion surface and certainty match | Displayed-facts requirement. | Matches surface version and certainty. | No changed presentation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| 8 · ACCEPTED | C-24.9.2.1.6 — Forward-completion no conflicting acceptance | Acceptance-conflict requirement. | Checks committed acceptance history. | No conflicting recovery. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| 9 · ACCEPTED | C-24.9.2.1.7 — Forward-completion no committed rejection | Rejection-absence requirement. | Honors any committed rejection. | No reversed choice. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| 10 · ACCEPTED | C-24.9.2.1.8 — Forward-completion no correction-caused staleness | Correction-staleness requirement. | Checks later correction effects. | No obsolete proposal. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| 11 · ACCEPTED | C-24.9.2.1.9 — Forward-completion no superseding proposal | Supersession requirement. | Checks the proposal version chain. | No inherited decision. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| 12 · ACCEPTED | C-24.9.2.1.10 — Forward-completion no current authority or privacy block | Current permission requirement. | Checks present authority and privacy. | No recovery bypass. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| 13 · ACCEPTED | C-24.17.6 — Connection crash after durable Ness input | All ten condition results. | Allows only justified forward-completion. | Fresh decision when required. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 14 · ACCEPTED | C-24.19.4 — Connection I4 Ness-decision interface | All ten condition results. | Constrains interface recovery of durable input. | No auto-retried choice. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: C-24.9.2.1.1 — Forward-completion exact proposal binding; C-24.9.2.1.2 — Forward-completion current decision eligibility; C-24.9.2.1.3 — Forward-completion input integrity; C-24.9.2.1.4 — Forward-completion recovery authority; C-24.9.2.1.5 — Forward-completion surface and certainty match; C-24.9.2.1.6 — Forward-completion no conflicting acceptance; C-24.9.2.1.7 — Forward-completion no committed rejection; C-24.9.2.1.8 — Forward-completion no correction-caused staleness; C-24.9.2.1.9 — Forward-completion no superseding proposal; C-24.9.2.1.10 — Forward-completion no current authority or privacy block

### C-24.9.2.1.1 — Forward-completion exact proposal binding
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

ALONE
- What it is: ACCEPTED — The requirement that input remains bound to the exact proposal ID and version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Takes in: ACCEPTED — The durable input binding. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Does: ACCEPTED — Checks the original exact identity/version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Gives out: ACCEPTED — An exact-binding result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Must never: ACCEPTED — Substitute another proposal or version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Fails closed by: ACCEPTED — Mismatch requires a fresh decision. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.9.2.1 — Ness decision forward-completion gate: supplies condition 1. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.9.2.1 — Ness decision forward-completion gate | Exact binding. | Rejects any rebinding. | Version-specific completion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.9.2.1.2 — Forward-completion current decision eligibility
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

ALONE
- What it is: ACCEPTED — The requirement that the bound version is still current and decision-eligible. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Takes in: ACCEPTED — The current proposal version state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Does: ACCEPTED — Checks present eligibility rather than mere historical existence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Gives out: ACCEPTED — A current-eligibility result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Must never: ACCEPTED — Complete a stale version because it once was visible. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Fails closed by: ACCEPTED — Ineligible currentness requires a fresh decision. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.9.2.1 — Ness decision forward-completion gate: supplies condition 2. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.9.2.1 — Ness decision forward-completion gate | Current eligibility. | Rejects stale decision subjects. | No historical eligibility carryover. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |

SUB-PARTS: NONE

### C-24.9.2.1.3 — Forward-completion input integrity
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

ALONE
- What it is: ACCEPTED — The requirement for valid integrity of the durable decision input. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Takes in: ACCEPTED — The exact input integrity reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Does: ACCEPTED — Validates the durable selection. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Gives out: ACCEPTED — An integrity result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Must never: ACCEPTED — Reconstruct a missing selection. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Fails closed by: ACCEPTED — Invalid integrity prevents completion. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.9.2.1 — Ness decision forward-completion gate: supplies condition 3. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.9.2.1 — Ness decision forward-completion gate | Valid input integrity. | Keeps recovery tied to durable evidence. | No fabricated input. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.9.2.1.4 — Forward-completion recovery authority
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

ALONE
- What it is: ACCEPTED — The requirement that accepted identity/access authority remains valid for recovery. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Takes in: ACCEPTED — The B-INT-5 authority context reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Does: ACCEPTED — Consumes current owner validity without inventing an identity factor. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Gives out: ACCEPTED — The authority-valid-for-recovery result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Must never: ACCEPTED — Treat a past context as current authorization. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Fails closed by: ACCEPTED — Invalid recovery authority requires a fresh decision. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): accepted identity/access authority ownership. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Changes: ACCEPTED — C-24.9.2.1 — Ness decision forward-completion gate: supplies condition 4. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.9.2.1 — Ness decision forward-completion gate | Owner-validated recovery authority. | Blocks obsolete authority contexts. | No authority recreation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |

SUB-PARTS: NONE

### C-24.9.2.1.5 — Forward-completion surface and certainty match
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

ALONE
- What it is: ACCEPTED — The required match between the durable input and what was displayed. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Takes in: ACCEPTED — Decision-surface version and displayed certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Does: ACCEPTED — Checks both facts against the input. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Gives out: ACCEPTED — A matching-surface-and-certainty result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Must never: ACCEPTED — Accept a different presentation or uncertainty level silently. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Fails closed by: ACCEPTED — Mismatch requires a fresh visible decision. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.9.2.1 — Ness decision forward-completion gate: supplies condition 5. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.9.2.1 — Ness decision forward-completion gate | The matching display facts. | Preserves what Ness actually selected. | No changed decision surface. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.9.2.1.6 — Forward-completion no conflicting acceptance
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

ALONE
- What it is: ACCEPTED — The absence of a conflicting committed acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Takes in: ACCEPTED — Committed acceptance history. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Does: ACCEPTED — Checks for an already conflicting accepted outcome. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Gives out: ACCEPTED — An acceptance-conflict check. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Must never: ACCEPTED — Overwrite or ignore a competing committed decision. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Fails closed by: ACCEPTED — A conflict blocks completion. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.9.2.1 — Ness decision forward-completion gate: supplies condition 6. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.9.2.1 — Ness decision forward-completion gate | Acceptance-conflict result. | Preserves committed truth. | No overwrite by recovery. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |

SUB-PARTS: NONE

### C-24.9.2.1.7 — Forward-completion no committed rejection
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

ALONE
- What it is: ACCEPTED — The absence of a committed rejection. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Takes in: ACCEPTED — The proposal decision history. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Does: ACCEPTED — Checks that rejection has not committed. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Gives out: ACCEPTED — A rejection-absence result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Must never: ACCEPTED — Recover an old acceptance input over rejection. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Fails closed by: ACCEPTED — Committed rejection blocks completion. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.9.2.1 — Ness decision forward-completion gate: supplies condition 7. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.9.2.1 — Ness decision forward-completion gate | Rejection check. | Honors the actual rejected outcome. | No recovery reversal. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |

SUB-PARTS: NONE

### C-24.9.2.1.8 — Forward-completion no correction-caused staleness
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

ALONE
- What it is: ACCEPTED — The requirement that no correction made the proposal version stale. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Takes in: ACCEPTED — The later correction chain for the exact proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Does: ACCEPTED — Checks correction effects on decision eligibility. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Gives out: ACCEPTED — A correction-staleness result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Must never: ACCEPTED — Ignore a correction merely because the old input remains durable. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Fails closed by: ACCEPTED — Correction-caused staleness requires a fresh decision. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.9.2.1 — Ness decision forward-completion gate: supplies condition 8. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.9.2.1 — Ness decision forward-completion gate | Correction-staleness check. | Keeps current corrections binding. | No stale acceptance input. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |

SUB-PARTS: NONE

### C-24.9.2.1.9 — Forward-completion no superseding proposal
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

ALONE
- What it is: ACCEPTED — The absence of a committed superseding proposal version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Takes in: ACCEPTED — The append-only proposal version chain. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Does: ACCEPTED — Checks whether a newer version superseded the bound one. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Gives out: ACCEPTED — A supersession result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Must never: ACCEPTED — Let a new evidence version inherit an old choice. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Fails closed by: ACCEPTED — Supersession prevents forward-completion. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.9.2.1 — Ness decision forward-completion gate: supplies condition 9. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.9.2.1 — Ness decision forward-completion gate | Version-chain check. | Keeps decisions attached to their original version. | No inherited consent. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.9.2.1.10 — Forward-completion no current authority or privacy block
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

ALONE
- What it is: ACCEPTED — The requirement that no current authority or privacy rule blocks completion. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Takes in: ACCEPTED — Current route-level authorization. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Does: ACCEPTED — Rechecks the operation under the now-applicable rules. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Gives out: ACCEPTED — An authorization-block result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Must never: ACCEPTED — Treat recovery as exemption from current privacy. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Fails closed by: ACCEPTED — Any present block prevents completion. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current privacy; C-7P — Permission & Authority Boundaries (§7P): applicable authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Changes: ACCEPTED — C-24.9.2.1 — Ness decision forward-completion gate: supplies condition 10. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.9.2.1 — Ness decision forward-completion gate | Current permission result. | Stops now-forbidden completion. | No recovery bypass. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |

SUB-PARTS: NONE

### C-24.9.3 — Atomic authorized-rule commitment
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]

ALONE
- What it is: ACCEPTED — The exact-match acceptance route for an already-authorized rule. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Takes in: ACCEPTED — Exact rule version, active authorization, exact scope and source-condition matches. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Does: ACCEPTED — Immediately revalidates actual rule owner/version, active state, revocation/supersession, scope, eligible endpoint/connection types, source conditions, current applicability, privacy, key/duplicate state and authority identity. Atomically binds the rule ID/version, final validation, Ness authorization, scope/source matches, accepted record, rule-authority event and key result; completes the operation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Gives out: ACCEPTED — One rule-authorized accepted commitment. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Must never: ACCEPTED — Use a rule revoked or superseded before commit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Fails closed by: ACCEPTED — Any doubt triggers revalidation again; failed validation gives no acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current route-level privacy; C-7P — Permission & Authority Boundaries (§7P): actual rule authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]
- Changes: ACCEPTED — C-24.9 — Connection atomic compare-and-commit: supplies the rule-authorized atomic result; C-24.4.3 — Existing authorized connection-rule route: enforces final exact-match validity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.9 — Connection atomic compare-and-commit | Rule-authorized atomic result. | Binds proof and accepted record. | No stale rule acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.4.3 — Existing authorized connection-rule route | Final rule validation. | Requires current exact applicability before commitment. | No widening or revoked rule. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C] |
| 3 · ACCEPTED | C-24.17.13 — Connection crash after rule revalidation | Final rule checks. | Revalidates on any post-check doubt. | Current authority only. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 4 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual final revalidation. | Records the named rule-validation child. | No proof from logs. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |
| 5 · ACCEPTED | C-7P.14.2 — Existing narrow connection-rule authority interface | Stable rule_id, exact rule_version, Ness authorization reference, scope, eligible endpoint types, eligible connection types, source/provenance conditions, activation, revocation/supersession and current exact applicability. | Supplies the atomic route-specific final revalidation and authority event. | Nothing in this card. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-24.9.4 — Connection rejection commitment
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D]

ALONE
- What it is: ACCEPTED — The durable rejection route, distinct from the selected rejection input. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D]
- Takes in: ACCEPTED — Exact current proposal and valid explicit durable Ness rejection input. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D]
- Does: ACCEPTED — Immediately verifies current proposal ID/version, input, authority context, privacy, surface integrity, no conflicting committed outcome and suppression identity. Commits the final rejection event, registers repeat suppression and completes the operation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D]
- Gives out: ACCEPTED — Durable rejection plus suppression, with no lasting accepted relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D]
- Must never: ACCEPTED — Treat rejection input alone as the committed rejection or erase the proposal history. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D]
- Fails closed by: ACCEPTED — No committed decision leaves the proposal undecided. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current route-level internal-use permission; C-9 — Access/authentication model + voice I/O + phone modes (§9): current identity/access authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D]
- Changes: ACCEPTED — C-24.9 — Connection atomic compare-and-commit: supplies the separate rejected outcome; C-24.4.2 — Explicit Ness connection decision route: preserves exact explicit rejection. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.9 — Connection atomic compare-and-commit | Durable rejection and suppression. | Keeps input and final outcome distinct. | No accepted relationship. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.4.2 — Explicit Ness connection decision route | The explicit final rejection. | Preserves the current decision subject. | No input-only finality. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual final rejection. | Records rejection as its own child. | No lost rejected outcome. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-24.10 — Connection duplicate identities
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — The proposed relationship and authority-event identities governing duplicate absorption. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Takes in: ACCEPTED — Exact relationship geometry and exact acceptance authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Does: ACCEPTED — Keeps one logical proposal/accepted relationship per identical endpoints/type/direction; links pending and accepted records as one operation history. Racing source, Ness or rule routes converge with one winner and an absorbed duplicate. Distinct valid bases may add separate authority events without adding certainty or duplicate relationships. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Gives out: ACCEPTED — One relationship history and nonrepeating authority proofs. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Must never: ACCEPTED — Create another accepted record on retry or merge different types. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Unknown identity/commit results are resolved before retry. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]

TOGETHER
- Fed by: ACCEPTED — C-24.10.1 — Proposed canonical_relationship_key (CRK): proposed canonical_relationship_key; C-24.10.2 — Proposed authority_event_key: proposed authority_event_key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24 — Connection Capability (§24): prevents duplicate relationships. [V10 §24]
- Changes: ACCEPTED — C-24.9 — Connection atomic compare-and-commit: supplies stable compare-and-commit identities. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | Duplicate control. | Keeps one logical relationship per key. | No repeated support. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] |
| 2 · ACCEPTED | C-24.9 — Connection atomic compare-and-commit | Stable relationship and authority keys. | Absorbs races inside the same logical commit. | No duplicate window. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.10.1 — Proposed canonical_relationship_key (CRK) | Relationship duplicate scope. | Defines the proposed canonical key. | One logical relationship. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] |
| 4 · ACCEPTED | C-24.10.2 — Proposed authority_event_key | Authority-proof duplicate scope. | Defines the stable proposed event key. | No repeated proof support. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] |

SUB-PARTS: C-24.10.1 — Proposed canonical_relationship_key (CRK); C-24.10.2 — Proposed authority_event_key

### C-24.10.1 — Proposed canonical_relationship_key (CRK)
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — The proposed canonical_relationship_key (CRK) identifying a logical relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Takes in: ACCEPTED — At minimum endpoint identities, endpoint versions or immutable provenance where required, connection type, directionality and type version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Does: ACCEPTED — Deterministically normalizes endpoint ordering for symmetric types; preserves direction for directional types. A-to-B and B-to-A therefore stay different when directional. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Gives out: ACCEPTED — One proposed CRK for the exact logical relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Must never: ACCEPTED — Mutate an old key for changed endpoints, type, direction or type version; create a separate key just because the acceptance route differs. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.12.1 — Proposed connection_endpoint_ref: exact proposed endpoint references; C-24.8 — Proposed connection type-and-direction contract: proposed type/direction contract. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.10 — Connection duplicate identities: identifies the logical duplicate scope; C-24.1.1 — Proposed accepted_connection_record: keys acceptance; C-24.3.1 — Proposed connection_proposal_record: keys the proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.10 — Connection duplicate identities | The proposed CRK. | Converges identical logical relationships. | One duplicate scope. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.1.1 — Proposed accepted_connection_record | The relationship key. | Links the accepted version to its logical relationship. | Stable accepted identity scope. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.3.1 — Proposed connection_proposal_record | The relationship key. | Links pending and eventual accepted history. | No competing duplicate proposal. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-24.12.1 — Proposed connection_endpoint_ref | Endpoint key inputs. | Preserves exact endpoint identities and provenance. | Correct relationship key. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 5 · ACCEPTED | C-24.22 — Connection-owned durable-operation coordination boundary | The proposed owner relationship key. | Carries it without deriving or replacing it. | Owner duplicate scope retained. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K] |

SUB-PARTS: NONE

### C-24.10.2 — Proposed authority_event_key
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — The proposed stable authority_event_key for an individual acceptance proof. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Takes in: ACCEPTED — At minimum accepted-connection ID or proposed CRK, acceptance-basis type, exact authority/source/rule reference and exact authority/source/rule version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Does: ACCEPTED — Recovers the existing event or absorbs a repeat attempt. Preserves genuinely different valid bases as separate events. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Gives out: ACCEPTED — A stable proposed authority_event_key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Must never: ACCEPTED — Append repeated copies of the same proof, count them as support or increase certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.10 — Connection duplicate identities: prevents repeated authority proofs; C-24.12.5 — Proposed connection_authority_event: identifies the proposed authority event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.10 — Connection duplicate identities | Authority proof identity. | Distinguishes genuine bases from duplicates. | No repeated support. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.12.5 — Proposed connection_authority_event | The stable authority key. | Recovers or absorbs rather than reappending. | One proof event per exact basis. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.22 — Connection-owned durable-operation coordination boundary | The proposed owner authority-event key. | Carries the exact proof identity. | No duplicate proof. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §T] |

SUB-PARTS: NONE

### C-24.11 — Connection rejection and new-evidence suppression
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The append-only suppression rule for rejected relationships. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — A rejection and any later owner-verified genuine new-evidence delta. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Preserves the rejected proposal/event and suppresses repeat surfacing. A genuine new delta permits a new proposal ID with backlink and explicit delta, retaining the same proposed CRK for the same logical relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — Preserved rejection or one new linked proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Delete, hide or rewrite rejection; take silence as reversal; retry the old decision; count old and new as two votes. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Where accepted source/evidence owners cannot establish genuineness, no new proposal is created. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]

TOGETHER
- Fed by: ACCEPTED — C-24.11.1 — Proposed connection_rejection_suppression_registry: proposed suppression registry; C-24.3.1.4 — Proposed connection new-evidence delta reference: exact genuine delta. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24 — Connection Capability (§24): prevents repetitive rejected proposals. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | Rejection suppression and valid new proposals. | Keeps rejection durable without sealing out genuine new evidence. | No repeated decision pressure. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10] |
| 2 · ACCEPTED | C-24.11.1 — Proposed connection_rejection_suppression_registry | The standing rejection. | Maintains proposed key-based suppression. | No repetitive resurfacing. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10] |

SUB-PARTS: C-24.11.1 — Proposed connection_rejection_suppression_registry

### C-24.11.1 — Proposed connection_rejection_suppression_registry
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The proposed connection_rejection_suppression_registry keyed by the proposed CRK. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]
- Takes in: ACCEPTED — A durable rejection and the owner-verified delta for any later linked proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]
- Does: ACCEPTED — Records that rejection stands and suppresses repeat surfacing until a linked genuine delta is verified. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]
- Gives out: ACCEPTED — An idempotent suppression registration. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]
- Must never: ACCEPTED — Treat formatting changes, model rewording, same-evidence retrieval, repeated similarity, time or repeated co-retrieval as a verified new basis. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — No verified delta leaves suppression in effect. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.11 — Connection rejection and new-evidence suppression: maintains the rejection suppression state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §10]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.11 — Connection rejection and new-evidence suppression | The proposed suppression registration. | Keeps repetition from reopening the same decision. | Suppressed repeated surfacing. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual suppression registration. | Records rejection suppression. | No repeated decision pressure. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-24.12 — Proposed connection mechanical records
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed append-only conceptual record family, with references instead of copied endpoint content. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Exact record identities, immutable endpoint/source versions, decisions, authority references and operational facts. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Preserves distinct identities and provenance without making any record an authority or a new unit of evidence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed reference-bearing records. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Copy raw protected endpoint content, add evidence weight or replace an actual owner. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.12.1 — Proposed connection_endpoint_ref: proposed endpoint reference; C-24.12.2 — Proposed connection_candidate_report: proposed candidate report; C-24.12.3 — Proposed ness_decision_input: proposed durable input; C-24.12.4 — Proposed connection_decision_event: proposed decision event; C-24.12.5 — Proposed connection_authority_event: proposed authority event; C-24.12.6 — Proposed connection_correction_event: proposed correction event; C-24.12.7 — Proposed connection_use_event: proposed use event; C-24.12.8 — Proposed connection_duplicate_absorbed: proposed duplicate event; C-24.12.9 — Proposed connection_operation: proposed parent operation; C-24.12.10 — Proposed connection_recovery_event: proposed recovery event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24 — Connection Capability (§24): preserves the distinct connection record identities. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | The proposed record family. | Keeps source, choice, authority and history separate. | Inspectable immutable provenance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.12.1 — Proposed connection_endpoint_ref | Reference-only endpoint requirements. | Defines the proposed endpoint record. | Exact protected reference. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.12.2 — Proposed connection_candidate_report | Separate report requirements. | Defines the proposed candidate record. | No proposal conversion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-24.12.3 — Proposed ness_decision_input | Durable-choice requirements. | Defines the proposed selection input. | No finality from input. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 5 · ACCEPTED | C-24.12.4 — Proposed connection_decision_event | Final-decision requirements. | Defines the proposed decision event. | Actual committed status. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 6 · ACCEPTED | C-24.12.5 — Proposed connection_authority_event | Authority-proof requirements. | Defines the proposed proof event. | Recoverable authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 7 · ACCEPTED | C-24.12.6 — Proposed connection_correction_event | Correction-history requirements. | Defines the proposed later event. | Immutable earlier history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 8 · ACCEPTED | C-24.12.7 — Proposed connection_use_event | Use-audit requirements. | Defines the proposed use/non-use record. | No extra vote. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D] |
| 9 · ACCEPTED | C-24.12.8 — Proposed connection_duplicate_absorbed | Duplicate-history requirements. | Defines the proposed absorbed event. | No duplicate support. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 10 · ACCEPTED | C-24.12.9 — Proposed connection_operation | One-parent requirements. | Defines the proposed operation record. | One real operation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |
| 11 · ACCEPTED | C-24.12.10 — Proposed connection_recovery_event | Recovery-history requirements. | Defines the proposed recovery event. | No reconstructed truth. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: C-24.12.1 — Proposed connection_endpoint_ref; C-24.12.2 — Proposed connection_candidate_report; C-24.12.3 — Proposed ness_decision_input; C-24.12.4 — Proposed connection_decision_event; C-24.12.5 — Proposed connection_authority_event; C-24.12.6 — Proposed connection_correction_event; C-24.12.7 — Proposed connection_use_event; C-24.12.8 — Proposed connection_duplicate_absorbed; C-24.12.9 — Proposed connection_operation; C-24.12.10 — Proposed connection_recovery_event

### C-24.12.1 — Proposed connection_endpoint_ref
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed reference identifying an endpoint without copying its content. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Object type, stable object ID, needed store/source provenance, immutable version/reference and privacy classification reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Preserves exact endpoint identity and protection context. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A proposed connection_endpoint_ref. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Copy endpoint content or fill missing identity by inference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Missing or contradictory endpoint identity blocks the relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-24.12.1.1 — Proposed endpoint object_type: proposed object type; C-24.12.1.2 — Proposed endpoint stable object ID: proposed stable ID; C-24.12.1.3 — Proposed endpoint batch/store or source provenance: proposed provenance; C-24.12.1.4 — Proposed endpoint immutable version/reference: proposed immutable version; C-24.12.1.5 — Proposed endpoint privacy classification reference: proposed privacy classification. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12 — Proposed connection mechanical records: supplies reference-only endpoints; C-24.1.1 — Proposed accepted_connection_record: identifies accepted endpoints; C-24.3.1 — Proposed connection_proposal_record: identifies proposal endpoints; C-24.10.1 — Proposed canonical_relationship_key (CRK): grounds the proposed canonical key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12 — Proposed connection mechanical records | The proposed endpoint reference. | Carries exact identity without raw content. | Protected provenance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.1.1 — Proposed accepted_connection_record | Exact endpoint references. | Preserves exactly what the accepted record links. | Separate originals. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.3.1 — Proposed connection_proposal_record | Exact candidate endpoints. | States what the decision concerns. | Bounded proposal. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-24.10.1 — Proposed canonical_relationship_key (CRK) | Endpoint identity and immutable provenance. | Builds the relationship duplicate scope. | Correct proposed CRK. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 5 · ACCEPTED | C-24.12.1.1 — Proposed endpoint object_type | Object-kind slot. | Records the actual endpoint type. | Typed reference. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 6 · ACCEPTED | C-24.12.1.2 — Proposed endpoint stable object ID | Stable-identity slot. | References the original object. | No name-based substitution. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 7 · ACCEPTED | C-24.12.1.3 — Proposed endpoint batch/store or source provenance | Provenance slot. | Carries needed source/store location. | Inspectable origin. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 8 · ACCEPTED | C-24.12.1.4 — Proposed endpoint immutable version/reference | Version slot. | Fixes the immutable endpoint reference. | No floating object. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 9 · ACCEPTED | C-24.12.1.5 — Proposed endpoint privacy classification reference | Privacy-classification slot. | Carries the protection reference. | No access grant. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: C-24.12.1.1 — Proposed endpoint object_type; C-24.12.1.2 — Proposed endpoint stable object ID; C-24.12.1.3 — Proposed endpoint batch/store or source provenance; C-24.12.1.4 — Proposed endpoint immutable version/reference; C-24.12.1.5 — Proposed endpoint privacy classification reference

### C-24.12.1.1 — Proposed endpoint object_type
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed object_type field of an endpoint reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The actual endpoint object kind. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Carries its type without changing the object. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed object_type. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Invent an endpoint type to fit a rule. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.1 — Proposed connection_endpoint_ref: identifies the endpoint kind. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.1 — Proposed connection_endpoint_ref | Object type. | Preserves the actual endpoint kind. | Typed reference. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.1.2 — Proposed endpoint stable object ID
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed stable ID of the referenced endpoint. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The original owner-held object identity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — References that object independently of display wording. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A proposed stable object ID. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Replace stable identity with a similar name. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.1 — Proposed connection_endpoint_ref: addresses the original endpoint. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.1 — Proposed connection_endpoint_ref | Stable object ID. | Keeps the original separately addressable. | No endpoint merge. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.1.3 — Proposed endpoint batch/store or source provenance
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed provenance slot used where needed to locate an endpoint. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The endpoint batch/store or source provenance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Carries sufficient original provenance for the reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed batch/store or source provenance where needed. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Use a copy stripped of its source identity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.1 — Proposed connection_endpoint_ref: locates the referenced source. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.1 — Proposed connection_endpoint_ref | Needed provenance. | Retains source location and origin. | Inspectable endpoint reference. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.1.4 — Proposed endpoint immutable version/reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed exact immutable endpoint version or reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The owner-supplied immutable endpoint reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Keeps the relationship bound to its actual version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A proposed immutable version/reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Silently substitute a changed endpoint. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.1 — Proposed connection_endpoint_ref: fixes the endpoint version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.1 — Proposed connection_endpoint_ref | Immutable version. | Preserves the exact referenced object. | No floating endpoint. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.1.5 — Proposed endpoint privacy classification reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed reference to endpoint privacy classification. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The owner’s classification reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Carries classification without granting access or copying protected content. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A proposed privacy classification reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Treat classification presence as authorization. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.1 — Proposed connection_endpoint_ref: carries the endpoint protection context. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.1 — Proposed connection_endpoint_ref | Privacy classification. | Retains protection metadata at the boundary. | No access grant. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.2 — Proposed connection_candidate_report
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed retrieval submission, with an identity separate from every proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Proposed connection_candidate_report_id, exact immutable source refs, encounter description, verification outcome and report lifecycle state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Preserves how a potential direct relationship was found and what the owner actually verified. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A proposed connection_candidate_report. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Convert the report automatically into a proposal or recover one identity as the other. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.12.2.1 — Proposed connection_candidate_report_id: proposed report identity; C-24.12.2.2 — Proposed candidate immutable source references: proposed immutable source refs; C-24.12.2.3 — Proposed candidate encounter description: proposed encounter description; C-24.12.2.4 — Proposed candidate verification-outcome field: proposed verification outcome; C-24.13.2 — Connection candidate-report lifecycle: candidate lifecycle. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12 — Proposed connection mechanical records: preserves the separate proposed report; C-24.2.3 — Connection candidate-report retrieval route: records the retrieval submission. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12 — Proposed connection mechanical records | The proposed candidate report. | Keeps reporting separate from proposing. | Distinct provenance object. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.2.3 — Connection candidate-report retrieval route | The separate report identity. | Submits source references without accepting. | No automatic proposal. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.12.2.1 — Proposed connection_candidate_report_id | Report identity slot. | Keeps its own proposed ID. | Separate report identity. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-24.12.2.2 — Proposed candidate immutable source references | Source-reference slot. | Carries exact immutable source refs. | Owner-verifiable provenance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 5 · ACCEPTED | C-24.12.2.3 — Proposed candidate encounter description | Encounter slot. | Records how retrieval found the candidate. | No co-retrieval basis. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 6 · ACCEPTED | C-24.12.2.4 — Proposed candidate verification-outcome field | Owner-outcome slot. | Records the exact three-way result. | No invented verification. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 7 · ACCEPTED | C-24.13.2 — Connection candidate-report lifecycle | Report lifecycle slot. | Keeps report states separate from proposals. | No automatic promotion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |
| 8 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual candidate report. | Records the report child. | No proposal merely to log it. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: C-24.12.2.1 — Proposed connection_candidate_report_id; C-24.12.2.2 — Proposed candidate immutable source references; C-24.12.2.3 — Proposed candidate encounter description; C-24.12.2.4 — Proposed candidate verification-outcome field

### C-24.12.2.1 — Proposed connection_candidate_report_id
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed stable report identity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — A Route A-2 candidate submission. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Identifies the report separately from proposed connection_proposal_id. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed connection_candidate_report_id. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Reuse it as a proposal identity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.2 — Proposed connection_candidate_report: identifies the report. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.2 — Proposed connection_candidate_report | Report ID. | Keeps the report independently recoverable. | No identity collapse. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.2.2 — Proposed candidate immutable source references
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed references to the exact source encountered by retrieval. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Immutable source records supporting the apparent direct relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Preserves exact references for the actual owner verification. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed immutable source references. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Substitute an inferred relationship for recorded source provenance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.2 — Proposed connection_candidate_report: preserves the candidate source basis. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.2 — Proposed connection_candidate_report | Exact source references. | Supplies the owner-verifiable material. | No inferred provenance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.2.3 — Proposed candidate encounter description
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed record of how retrieval encountered the apparent relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The actual retrieval encounter. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records encounter provenance without turning it into acceptance evidence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A proposed how-encountered description. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Treat co-retrieval as an acceptance basis. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.2 — Proposed connection_candidate_report: records the discovery context. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.2 — Proposed connection_candidate_report | Encounter provenance. | Explains the submission origin. | No co-retrieval authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.2.4 — Proposed candidate verification-outcome field
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed slot carrying the exact owner outcome. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Exactly verified_self_establishing, verification_unavailable or not_verified. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Keeps successful, unavailable and failed verification distinct. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — The actual three-way owner result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Translate unavailable into verified or failed into uncertainty evidence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.2 — Proposed connection_candidate_report: records the owner result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.2 — Proposed connection_candidate_report | The verification outcome. | Preserves the actual branch. | No manufactured success. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.3 — Proposed ness_decision_input
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed durable evidence that Ness explicitly chose accept or reject. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Exact bound proposal ID/version, decision-surface version/displayed certainty, current authority context reference and integrity reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Proves what Ness selected while retaining a separate identity from the final decision, accepted record and authority event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A durable proposed ness_decision_input. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Treat the input as final proposal status, an accepted connection, authority event or completed logical commit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Invalid or stale input cannot be silently completed or rebound. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-24.12.3.1 — Proposed Ness-input exact proposal binding: proposed exact proposal binding; C-24.12.3.2 — Proposed Ness-input surface and displayed certainty: proposed surface/certainty facts; C-24.12.3.3 — Proposed Ness-input authority context reference: proposed authority context; C-24.1.1.8 — Proposed connection integrity reference: proposed integrity reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12 — Proposed connection mechanical records: preserves the selected input; C-24.4.2 — Explicit Ness connection decision route: supplies explicit-choice evidence; C-24.9.2 — Atomic Ness acceptance commitment: supplies the durable input for atomic acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12 — Proposed connection mechanical records | The proposed durable input. | Keeps selection distinct from completion. | No input-only finality. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.4.2 — Explicit Ness connection decision route | Durable explicit choice. | Binds the route to actual selection. | No inferred consent. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.9.2 — Atomic Ness acceptance commitment | Valid input and exact binding. | Includes the selection in the atomic result. | Recoverable choice provenance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-24.1.1.8 — Proposed connection integrity reference | Durable-input integrity slot. | Carries a verifiable reference. | No fabricated selection. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 5 · ACCEPTED | C-24.12.3.1 — Proposed Ness-input exact proposal binding | Decision-subject slot. | Binds exact proposal ID/version. | No successor rebinding. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 6 · ACCEPTED | C-24.12.3.2 — Proposed Ness-input surface and displayed certainty | Decision-presentation slots. | Preserves surface and shown certainty. | Exact selected presentation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 7 · ACCEPTED | C-24.12.3.3 — Proposed Ness-input authority context reference | Authority-context slot. | References the actual identity/access owner. | No invented factor. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 8 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual durable selection input. | Records the distinct input child. | No input/final-event conflation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: C-24.12.3.1 — Proposed Ness-input exact proposal binding; C-24.12.3.2 — Proposed Ness-input surface and displayed certainty; C-24.12.3.3 — Proposed Ness-input authority context reference

### C-24.12.3.1 — Proposed Ness-input exact proposal binding
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed binding to the exact proposal ID and version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The proposal version Ness was deciding. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Stores that exact target with the durable input. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A proposed exact proposal binding. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Silently bind the choice to a successor version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.3.1.1 — Proposed connection_proposal_id and version: exact proposed identity/version to which the input remains bound. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.3 — Proposed ness_decision_input: fixes the input subject. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.3 — Proposed ness_decision_input | Exact proposal binding. | Preserves the decision subject. | No inherited input. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.3.2 — Proposed Ness-input surface and displayed certainty
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed decision-surface version and displayed certainty facts. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The exact surface and uncertainty shown when Ness selected. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Preserves both for later integrity and recovery matching. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed surface version and displayed certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Replace displayed certainty with a later value during recovery. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.12.3.2.1 — Proposed Ness-input decision-surface version: proposed decision-surface version; C-24.12.3.2.2 — Proposed Ness-input displayed certainty: proposed displayed certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.3 — Proposed ness_decision_input: preserves the actual decision presentation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.3 — Proposed ness_decision_input | Surface and certainty facts. | Retains what was shown. | Checkable explicit choice. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.12.3.2.1 — Proposed Ness-input decision-surface version | Surface-version slot. | Preserves the shown surface. | Exact display history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.12.3.2.2 — Proposed Ness-input displayed certainty | Displayed-certainty slot. | Preserves the shown uncertainty. | No silent change. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: C-24.12.3.2.1 — Proposed Ness-input decision-surface version; C-24.12.3.2.2 — Proposed Ness-input displayed certainty

### C-24.12.3.2.1 — Proposed Ness-input decision-surface version
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed exact version of the decision surface shown. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The surface present when Ness explicitly chose. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records the shown version for later integrity matching. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed decision-surface version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Substitute a newer surface during recovery. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.3.2 — Proposed Ness-input surface and displayed certainty: identifies the displayed surface. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.3.2 — Proposed Ness-input surface and displayed certainty | Surface version. | Preserves the selection presentation. | Exact display provenance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.3.2.2 — Proposed Ness-input displayed certainty
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed certainty value actually shown during the choice. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The displayed proposal certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records what Ness saw without changing it through acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed displayed certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Replace shown certainty with an undisplayed later value. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.3.2 — Proposed Ness-input surface and displayed certainty: preserves the displayed uncertainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.3.2 — Proposed Ness-input surface and displayed certainty | Displayed certainty. | Keeps recovery matched to the actual choice. | No silent certainty change. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.3.3 — Proposed Ness-input authority context reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed reference to the accepted identity/access context. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The current authority supplied by the identity/access owners. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — References that authority without choosing a new authentication factor. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A proposed authority context reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Let another speaker decide as Ness. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Unverifiable Ness authority blocks acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.3 — Proposed ness_decision_input: carries the choice authority provenance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.3 — Proposed ness_decision_input | The actual authority reference. | Keeps Ness authority owner-governed. | No copied authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.4 — Proposed connection_decision_event
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed final decision event, distinct from durable input. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — An exact accepted, rejected or still-undecided fact and the applicable proposal version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records the actual committed proposal decision. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A proposed connection_decision_event with its own identity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Make a durable input itself the final status. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.12.4.1 — Proposed connection decision-event fact: proposed decision fact; C-24.12.4.2 — Proposed connection decision-event proposal version: proposed applicable version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12 — Proposed connection mechanical records: preserves final decision truth; C-24.9.2 — Atomic Ness acceptance commitment: binds accepted decision to the complete atomic result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12 — Proposed connection mechanical records | The proposed final event. | Distinguishes commitment from selected input. | Actual decision truth. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.9.2 — Atomic Ness acceptance commitment | Final accepted decision event. | Recovers it with accepted record and authority. | One logical commit. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.12.4.1 — Proposed connection decision-event fact | Decision-fact slot. | Records accepted, rejected or undecided. | No inferred choice. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-24.12.4.2 — Proposed connection decision-event proposal version | Applicable-version slot. | Binds the final decision to its version. | No cross-version consent. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 5 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual final proposal decision. | Records the separate decision-event child. | No lost decision truth. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: C-24.12.4.1 — Proposed connection decision-event fact; C-24.12.4.2 — Proposed connection decision-event proposal version

### C-24.12.4.1 — Proposed connection decision-event fact
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed exact decision fact. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — accepted, rejected or still-undecided. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records the actual decision without a waiting-location status. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — The exact three-way decision value. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Infer acceptance from display or elapsed time. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.4 — Proposed connection_decision_event: supplies the decision fact. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.4 — Proposed connection_decision_event | The decision fact. | Preserves actual status. | No inferred decision. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.4.2 — Proposed connection decision-event proposal version
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed version to which the final decision applies. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The exact proposal version committed in the decision. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Keeps decision applicability version-specific. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — An exact proposed proposal-version reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Apply it automatically to a corrected version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.4 — Proposed connection_decision_event: bounds the decision applicability. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.4 — Proposed connection_decision_event | Applicable proposal version. | Keeps the decision attached to its subject. | No cross-version consent. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.5 — Proposed connection_authority_event
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed durable proof of an acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Basis type, exact authority/source/rule reference/version, accepted ID or proposed CRK and stable proposed authority_event_key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Commits within the same atomic logical commit as the accepted record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Recoverable proposed connection_authority_event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Allow an accepted relationship with no recoverable authority event or add duplicate proof weight. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Missing or unbound proof means no valid accepted commitment. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-24.12.5.1 — Proposed authority-event acceptance-basis type: proposed basis type; C-24.12.5.2 — Proposed authority-event exact reference and version: proposed exact authority/version; C-24.12.5.3 — Proposed authority-event relationship target: proposed relationship target; C-24.10.2 — Proposed authority_event_key: proposed authority key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12 — Proposed connection mechanical records: preserves acceptance proof; C-24.9.2 — Atomic Ness acceptance commitment: binds the Ness-confirmation event to the atomic result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12 — Proposed connection mechanical records | The proposed authority event. | Keeps proof recoverable with the relationship. | No authority from record presence. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.9.2 — Atomic Ness acceptance commitment | Ness-confirmation authority proof. | Commits it with the decision and record. | No split proof. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.10.2 — Proposed authority_event_key | Authority-event identity slot. | Carries a stable duplicate key. | No reappended proof. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] |
| 4 · ACCEPTED | C-24.12.5.1 — Proposed authority-event acceptance-basis type | Basis-type slot. | Types the actual authority. | No relabeled confirmation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 5 · ACCEPTED | C-24.12.5.2 — Proposed authority-event exact reference and version | Authority-source slots. | Preserves exact reference and version. | Verifiable proof. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 6 · ACCEPTED | C-24.12.5.3 — Proposed authority-event relationship target | Relationship-target slot. | Binds proof to accepted ID or proposed key. | No transferable authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 7 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual authority event. | Records the named proof child. | No repeated support. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: C-24.12.5.1 — Proposed authority-event acceptance-basis type; C-24.12.5.2 — Proposed authority-event exact reference and version; C-24.12.5.3 — Proposed authority-event relationship target

### C-24.12.5.1 — Proposed authority-event acceptance-basis type
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed authority-event basis field. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Exactly direct_source, ness_confirmation or authorized_rule in the proposed record schema. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Identifies the kind of actual acceptance authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A proposed acceptance-basis type. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Relabel one authority kind as another. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.5 — Proposed connection_authority_event: types the proof. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.5 — Proposed connection_authority_event | Basis type. | Distinguishes the source of authority. | Exact proof classification. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.5.2 — Proposed authority-event exact reference and version
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed exact reference/version pair for authority, source or rule. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The actual authority object and version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Binds the proof to an exact owner-held authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed authority/source/rule reference and version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Treat changed authority as the same proof. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Unverifiable authority cannot support acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-24.12.5.2.1 — Proposed authority-event exact authority reference: proposed exact authority reference; C-24.12.5.2.2 — Proposed authority-event exact authority version: proposed exact authority version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.5 — Proposed connection_authority_event: locates the exact proof source. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.5 — Proposed connection_authority_event | Exact authority reference/version. | Keeps the proof verifiable. | No floating authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.12.5.2.1 — Proposed authority-event exact authority reference | Authority-reference slot. | Locates the actual proof source. | Owner provenance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.12.5.2.2 — Proposed authority-event exact authority version | Authority-version slot. | Fixes the exact proof version. | No duplicate basis. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: C-24.12.5.2.1 — Proposed authority-event exact authority reference; C-24.12.5.2.2 — Proposed authority-event exact authority version

### C-24.12.5.2.1 — Proposed authority-event exact authority reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed exact authority, source or rule reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The actual owner-held authority object. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Locates the proof source for this relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed exact authority/source/rule reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Replace actual authority with recordkeeper assertions. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.5.2 — Proposed authority-event exact reference and version: identifies the proof source. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.5.2 — Proposed authority-event exact reference and version | Authority reference. | Keeps proof source-specific. | Recoverable actual authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.5.2.2 — Proposed authority-event exact authority version
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed exact version of the authority, source or rule. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The version supplying the proof. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Distinguishes changed authority for idempotency and validation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed exact authority/source/rule version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Treat repeated copies of one version as different support. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.5.2 — Proposed authority-event exact reference and version: fixes the proof version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.5.2 — Proposed authority-event exact reference and version | Authority version. | Keeps proofs version-specific. | No duplicate support. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.5.3 — Proposed authority-event relationship target
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed accepted-connection ID or proposed CRK to which proof applies. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The exact accepted record or logical relationship key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Scopes the authority event to its actual relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A proposed accepted-ID-or-CRK reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Reuse proof for another relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.5 — Proposed connection_authority_event: binds proof to its target. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.5 — Proposed connection_authority_event | Relationship target. | Keeps authority relationship-specific. | No transferable proof. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.6 — Proposed connection_correction_event
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — The proposed append-only correction, clarification, dispute, replacement or supersession event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — Exact target record/version, correction content refs, basis, owner/authority refs and integrity refs. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Points back to the immutable old record. Changes to endpoints, type, direction or type version create a new proposal/accepted version and new correct key, with an append-only link to both old and new. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — A proposed correction_event_id and later-event history controlling current use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Edit the earlier record, mutate the old key or invent destructive removal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — Missing exact target or failed route authorization prevents the correction event; the old record remains untouched. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

TOGETHER
- Fed by: ACCEPTED — C-24.12.6.1 — Proposed correction exact target and version: proposed target/version; C-24.12.6.2 — Proposed correction content references: proposed content refs; C-24.12.6.3 — Proposed correction basis: proposed basis; C-24.12.6.4 — Proposed correction owner and authority references: proposed correcting authority; C-24.1.1.8 — Proposed connection integrity reference: proposed integrity; C-24.12.6.5 — Proposed correction_event_id: proposed correction identity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current internal-use authorization immediately before correction commit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Changes: ACCEPTED — C-24.12 — Proposed connection mechanical records: preserves later correction history. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12 — Proposed connection mechanical records | The proposed correction event. | Keeps history immutable while changing applicable use. | Append-only correction. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.1.1.8 — Proposed connection integrity reference | Correction integrity slot. | Carries event integrity proof. | Verifiable later history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 3 · ACCEPTED | C-24.12.6.1 — Proposed correction exact target and version | Correction-target slots. | Identifies exact prior history. | No old-record edit. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 4 · ACCEPTED | C-24.12.6.2 — Proposed correction content references | Correction-content slot. | References actual correcting material. | No copied protected content. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 5 · ACCEPTED | C-24.12.6.3 — Proposed correction basis | Correction-basis slot. | Preserves why later information applies. | No inferred replacement. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 6 · ACCEPTED | C-24.12.6.4 — Proposed correction owner and authority references | Correcting-authority slots. | Keeps authority with the actual source. | No recordkeeper override. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 7 · ACCEPTED | C-24.12.6.5 — Proposed correction_event_id | Event-identity slot. | Keys correction recovery and idempotency. | No duplicate append. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 8 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual correction or dispute. | Records each as its own actual child kind. | No rewritten history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: C-24.12.6.1 — Proposed correction exact target and version; C-24.12.6.2 — Proposed correction content references; C-24.12.6.3 — Proposed correction basis; C-24.12.6.4 — Proposed correction owner and authority references; C-24.12.6.5 — Proposed correction_event_id

### C-24.12.6.1 — Proposed correction exact target and version
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — The proposed exact ID/version of the correction target. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — The existing immutable proposal or accepted record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Points the later event back to that exact historical record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — A proposed target ID/version reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Edit the target to add its future event link. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — Missing target existence prevents commit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

TOGETHER
- Fed by: ACCEPTED — C-24.12.6.1.1 — Proposed correction target record ID: proposed exact target ID; C-24.12.6.1.2 — Proposed correction target record version: proposed exact target version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.6 — Proposed connection_correction_event: identifies what is corrected. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.6 — Proposed connection_correction_event | Exact correction target. | Preserves back-referenced history. | No destructive rewrite. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.12.6.1.1 — Proposed correction target record ID | Target-ID slot. | Points to the exact prior record. | Unambiguous correction. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 3 · ACCEPTED | C-24.12.6.1.2 — Proposed correction target record version | Target-version slot. | Fixes the corrected historical version. | Version-specific backlink. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: C-24.12.6.1.1 — Proposed correction target record ID; C-24.12.6.1.2 — Proposed correction target record version

### C-24.12.6.1.1 — Proposed correction target record ID
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — The proposed exact identity of the record being corrected. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — The existing proposal or accepted-record ID. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Points back to that preserved original. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — Proposed target record ID. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Replace the target with a similar record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.6.1 — Proposed correction exact target and version: identifies the correction subject. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.6.1 — Proposed correction exact target and version | Target ID. | Keeps the backlink exact. | No ambiguous correction. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.6.1.2 — Proposed correction target record version
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — The proposed exact version of the correction subject. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — The targeted immutable version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Binds the later event to that historical version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — Proposed target record version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Rewrite the target version in place. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.6.1 — Proposed correction exact target and version: scopes the correction to its exact history. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.6.1 — Proposed correction exact target and version | Target version. | Preserves version-specific correction. | No historical mutation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.6.2 — Proposed correction content references
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — The proposed references to correction or dispute information. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — The correcting source content under its own authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Preserves references without copying protected endpoint content. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — Proposed correction/dispute content refs. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Copy protected endpoint content into the correction references. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.6 — Proposed connection_correction_event: supplies the correction information. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.6 — Proposed connection_correction_event | Content references. | Keeps the correction inspectable and protected. | Reference-based correction. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.6.3 — Proposed correction basis
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — The proposed basis explaining a correction or dispute event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — The correcting source basis. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Records why the later information applies. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — A proposed correction basis. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Infer a replacement merely because the earlier record was disputed. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.6 — Proposed connection_correction_event: records the later event basis. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.6 — Proposed connection_correction_event | Correction basis. | Distinguishes actual correction from inferred replacement. | No guessed successor. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-24.12.6.4 — Proposed correction owner and authority references
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — The proposed authority references for the correcting source. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — Ness, the actual owner or another authorized source under its own authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Keeps correction authority with the source; the proposed recordkeeper only records. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — Proposed owner/authority references. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Resolve an owner contradiction in the proposed recordkeeper favor. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — Unverifiable correction authority blocks the dependent use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.6 — Proposed connection_correction_event: preserves the correcting authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.6 — Proposed connection_correction_event | Actual correcting authority. | Records rather than assumes permission. | Owner-governed correction. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-24.12.6.5 — Proposed correction_event_id
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — The proposed stable identity of the correction event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — The real append-only correction or dispute event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Provides the idempotency and recovery key for that event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — Proposed correction_event_id. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Append duplicates from retrying the same correction. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.6 — Proposed connection_correction_event: identifies the later event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.6 — Proposed connection_correction_event | Correction identity. | Recovers the actual append once. | No duplicate correction. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-24.12.7 — Proposed connection_use_event
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]

ALONE
- What it is: ACCEPTED — The proposed audit of use or non-use, never another vote for a relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Takes in: ACCEPTED — Consumer operation/purpose; original accepted ID/version; chain/resolution; actual used version; consulted events; accepted-versus-investigation status; certainty preservation; output uncertainty; non-use reason; result/failure; source types, eligibility, changed search scope, retrieved material, later claim effect, omission/truncation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Does: ACCEPTED — Records exactly what retrieval or another consumer used and why, including non-use after dispute, correction, supersession or unresolved history. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Gives out: ACCEPTED — A proposed connection_use_event with bounded uncertainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Must never: ACCEPTED — Increase certainty, evidence weight or currentness through logs. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.12.7.1 — Proposed connection-use operation and purpose: proposed operation/purpose; C-24.12.7.2 — Proposed connection-use original accepted ID and version: proposed original identity/version; C-24.12.7.3 — Proposed connection-use chain and resolution result: proposed chain/result; C-24.12.7.4 — Proposed connection-use actual version: proposed actual used version; C-24.12.7.5 — Proposed connection-use consulted correction events: proposed consulted events; C-24.12.7.6 — Proposed connection-use accepted or investigation class: proposed use class; C-24.12.7.7 — Proposed connection-use certainty preservation: proposed certainty preservation; C-24.12.7.8 — Proposed connection-use output uncertainty behavior: proposed output uncertainty; C-24.12.7.9 — Proposed connection-use non-use and reason: proposed non-use reason; C-24.12.7.10 — Proposed connection-use result or failure reference: proposed result/failure; C-24.12.7.11 — Proposed connection retrieval-audit additions: proposed retrieval audit additions. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12 — Proposed connection mechanical records: preserves actual use provenance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Changes: DESIGNED — C-24.2 — Connection retrieval role: audits the retrieval-side relationship use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12 — Proposed connection mechanical records | The proposed use audit. | Preserves use and non-use without adding support. | No log-derived certainty. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · DESIGNED | C-24.2 — Connection retrieval role | Exact retrieval-use history. | Keeps retrieval purpose and relationship status inspectable. | No invisible promotion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D] |
| 3 · ACCEPTED | C-24.12.7.1 — Proposed connection-use operation and purpose | Use-identity and purpose slots. | Records whose use and why. | Scoped operation history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-24.12.7.2 — Proposed connection-use original accepted ID and version | Original accepted-record slots. | Preserves the starting ID/version. | No lost predecessor. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 5 · ACCEPTED | C-24.12.7.3 — Proposed connection-use chain and resolution result | Current-resolution slots. | Records consulted chain and result. | Inspectable current use. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 6 · ACCEPTED | C-24.12.7.4 — Proposed connection-use actual version | Actual-used-version slot. | Identifies the supplied record. | No version ambiguity. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 7 · ACCEPTED | C-24.12.7.5 — Proposed connection-use consulted correction events | Later-event slots. | Lists consulted correction/dispute/supersession refs. | Traceable later history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 8 · ACCEPTED | C-24.12.7.6 — Proposed connection-use accepted or investigation class | Use-class slot. | Separates accepted context from investigation. | No guidance promotion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 9 · ACCEPTED | C-24.12.7.7 — Proposed connection-use certainty preservation | Certainty-preservation slots. | Records original limit and handling. | No silent strengthening. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 10 · ACCEPTED | C-24.12.7.8 — Proposed connection-use output uncertainty behavior | Output-uncertainty slots. | Records required and actual surfacing. | Auditable visible limit. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 11 · ACCEPTED | C-24.12.7.9 — Proposed connection-use non-use and reason | Non-use slots. | Records omission and reason. | Inspectable protective outcome. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 12 · ACCEPTED | C-24.12.7.10 — Proposed connection-use result or failure reference | Result/failure slot. | References the real operation outcome. | No false success. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 13 · ACCEPTED | C-24.12.7.11 — Proposed connection retrieval-audit additions | Retrieval-specific audit slots. | Records scope, returned material and limits. | Complete retrieval history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D] |

SUB-PARTS: C-24.12.7.1 — Proposed connection-use operation and purpose; C-24.12.7.2 — Proposed connection-use original accepted ID and version; C-24.12.7.3 — Proposed connection-use chain and resolution result; C-24.12.7.4 — Proposed connection-use actual version; C-24.12.7.5 — Proposed connection-use consulted correction events; C-24.12.7.6 — Proposed connection-use accepted or investigation class; C-24.12.7.7 — Proposed connection-use certainty preservation; C-24.12.7.8 — Proposed connection-use output uncertainty behavior; C-24.12.7.9 — Proposed connection-use non-use and reason; C-24.12.7.10 — Proposed connection-use result or failure reference; C-24.12.7.11 — Proposed connection retrieval-audit additions

### C-24.12.7.1 — Proposed connection-use operation and purpose
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed consumer identity and purpose slots. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The consuming operation and its actual purpose. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records whose operation used the relationship and why. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed consuming operation and purpose. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Make one authorized purpose authorize another. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.12.7.1.1 — Proposed connection-use consuming operation: proposed consuming operation; C-24.12.7.1.2 — Proposed connection-use purpose: proposed purpose. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7 — Proposed connection_use_event: identifies the consuming use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7 — Proposed connection_use_event | Consumer operation and purpose. | Preserves the scoped use identity. | Purpose-specific audit. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.12.7.1.1 — Proposed connection-use consuming operation | Consumer-identity slot. | Records the actual consuming operation. | Attributable use. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.12.7.1.2 — Proposed connection-use purpose | Purpose slot. | Records why it was used. | Scoped use. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: C-24.12.7.1.1 — Proposed connection-use consuming operation; C-24.12.7.1.2 — Proposed connection-use purpose

### C-24.12.7.1.1 — Proposed connection-use consuming operation
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed identity of the actual consumer operation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The retrieval or other consuming operation ID. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Links the use event to that real operation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed consuming-operation reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7.1 — Proposed connection-use operation and purpose: identifies whose use is recorded. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7.1 — Proposed connection-use operation and purpose | Consumer operation. | Keeps the use attributable. | Exact use identity. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.7.1.2 — Proposed connection-use purpose
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed purpose of the actual use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The operation declared purpose. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records why the relationship was requested. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed use purpose. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Treat a use purpose as evidence supporting the relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7.1 — Proposed connection-use operation and purpose: scopes the recorded use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7.1 — Proposed connection-use operation and purpose | Use purpose. | Preserves why the consumer requested the relationship. | Purpose-specific history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.7.2 — Proposed connection-use original accepted ID and version
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed original accepted-record identity/version slots. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The original immutable accepted record consulted. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Preserves original history even where current-use resolution follows later events. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed original accepted-record ID/version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Substitute the current record and erase the original reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.12.7.2.1 — Proposed connection-use original accepted-record ID: proposed original ID; C-24.12.7.2.2 — Proposed connection-use original accepted-record version: proposed original version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7 — Proposed connection_use_event: preserves the original accepted record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7 — Proposed connection_use_event | Original record identity/version. | Makes the starting history inspectable. | No lost provenance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.12.7.2.1 — Proposed connection-use original accepted-record ID | Original-ID slot. | Preserves the accepted history identity. | Exact starting record. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.12.7.2.2 — Proposed connection-use original accepted-record version | Original-version slot. | Keeps the original immutable version. | No lost provenance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: C-24.12.7.2.1 — Proposed connection-use original accepted-record ID; C-24.12.7.2.2 — Proposed connection-use original accepted-record version

### C-24.12.7.2.1 — Proposed connection-use original accepted-record ID
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed original accepted identity consulted before current-use resolution. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The original accepted record ID. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Keeps the historical starting record in the audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed original accepted-record ID. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7.2 — Proposed connection-use original accepted ID and version: preserves the starting identity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7.2 — Proposed connection-use original accepted ID and version | Original accepted ID. | Retains the historical anchor. | Traceable starting record. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.7.2.2 — Proposed connection-use original accepted-record version
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed original version consulted. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The original immutable accepted version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Keeps the initial historical version distinct from the actual used replacement. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed original accepted-record version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Erase the old reference when using a valid replacement. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7.2 — Proposed connection-use original accepted ID and version: preserves the starting version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7.2 — Proposed connection-use original accepted ID and version | Original version. | Retains exact historical provenance. | No lost predecessor. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.7.3 — Proposed connection-use chain and resolution result
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed consulted current-use chain and its resolution result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The complete chain inspected before use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records both what was consulted and the outcome of resolution. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed chain references and current-use result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Treat the old accepted record alone as a fresh resolution. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.12.7.3.1 — Proposed connection-use consulted chain: proposed consulted chain; C-24.12.7.3.2 — Proposed connection-use resolution result: proposed resolution result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7 — Proposed connection_use_event: records the current-use decision context. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7 — Proposed connection_use_event | Chain and resolution. | Explains why the exact version was eligible or unused. | Inspectable currentness resolution. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.12.7.3.1 — Proposed connection-use consulted chain | Consulted-chain slot. | Records what history was inspected. | Actual resolution provenance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.12.7.3.2 — Proposed connection-use resolution result | Resolution-result slot. | Records current applicability. | No status/certainty merger. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: C-24.12.7.3.1 — Proposed connection-use consulted chain; C-24.12.7.3.2 — Proposed connection-use resolution result

### C-24.12.7.3.1 — Proposed connection-use consulted chain
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed current-use chain consulted by the operation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — All references actually inspected for the resolution. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records the chain used in determining current applicability. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed current-use-chain references. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Claim a chain was checked when it was not. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7.3 — Proposed connection-use chain and resolution result: preserves the consulted history. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7.3 — Proposed connection-use chain and resolution result | Consulted chain. | Makes current-use reasoning inspectable. | No unrecorded resolution. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.7.3.2 — Proposed connection-use resolution result
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed outcome of that current-use resolution. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The actual current, disputed, corrected/superseded or unresolved result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records the resolved status independently of original certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed current-use resolution result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Convert status into stronger certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7.3 — Proposed connection-use chain and resolution result: records what the chain resolved. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7.3 — Proposed connection-use chain and resolution result | Resolution result. | Explains use or non-use. | Status remains separate. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.7.4 — Proposed connection-use actual version
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed exact connection or proposal version actually used. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The record version supplied to the consumer. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records the actual used version independently of the original accepted identity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A proposed actual-use version reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Claim use of a current version while supplying a stale one. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7 — Proposed connection_use_event: identifies the actual material used. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7 — Proposed connection_use_event | Actual version. | Keeps use history exact. | No version ambiguity. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.7.5 — Proposed connection-use consulted correction events
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed correction, dispute and supersession event references consulted. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — All such events used in the current-use resolution. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Lists the later-event references separately from the original record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed consulted-event references. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Omit an applicable later dispute from the audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7 — Proposed connection_use_event: records the later history considered. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7 — Proposed connection_use_event | Consulted events. | Preserves the correction/dispute trail. | Traceable resolution. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.7.6 — Proposed connection-use accepted or investigation class
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed distinction between accepted evidence/context and pending investigation guidance only. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The actual route used. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Marks the audit with that route class. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed accepted-versus-investigation-only status. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Present pending guidance as accepted evidentiary context. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7 — Proposed connection_use_event: records the force of the use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7 — Proposed connection_use_event | Use class. | Keeps investigation separate from acceptance. | No evidentiary promotion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.7.7 — Proposed connection-use certainty preservation
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed preserved certainty and how-preserved slots. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The original certainty and the consumer handling. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records the label and how it remained bounded during use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed certainty and preservation explanation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Increase certainty through the use event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.12.7.7.1 — Proposed connection-use preserved certainty: proposed preserved certainty; C-24.12.7.7.2 — Proposed connection-use how-certainty-was-preserved: proposed preservation account. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7 — Proposed connection_use_event: records uncertainty preservation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7 — Proposed connection_use_event | Preserved certainty and handling. | Keeps the consumer accountable to the original limit. | No log-based strengthening. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.12.7.7.1 — Proposed connection-use preserved certainty | Certainty-value slot. | Preserves the original label. | No use-based increase. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.12.7.7.2 — Proposed connection-use how-certainty-was-preserved | Preservation-account slot. | Explains actual uncertainty handling. | Auditable limitation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: C-24.12.7.7.1 — Proposed connection-use preserved certainty; C-24.12.7.7.2 — Proposed connection-use how-certainty-was-preserved

### C-24.12.7.7.1 — Proposed connection-use preserved certainty
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed certainty value carried through use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The original qualitative relationship certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records the unchanged limit on the relationship claim. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed preserved certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Raise the label through repeated use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7.7 — Proposed connection-use certainty preservation: preserves the actual certainty value. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7.7 — Proposed connection-use certainty preservation | Preserved certainty. | Keeps the consumer inside the original limit. | No use-based promotion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.7.7.2 — Proposed connection-use how-certainty-was-preserved
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed explanation of how the consumer preserved uncertainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The actual uncertainty handling during the operation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records the treatment alongside the unchanged label. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed certainty-preservation account. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Claim preservation while silently strengthening the conclusion. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7.7 — Proposed connection-use certainty preservation: explains the consumer uncertainty behavior. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7.7 — Proposed connection-use certainty preservation | Preservation account. | Makes the limitation handling auditable. | No hidden strengthening. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.7.8 — Proposed connection-use output uncertainty behavior
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed material-uncertainty surfacing requirement and actual output behavior. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Whether uncertainty materially affected an output and how the accepted output chain handled it. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records whether uncertainty had to be surfaced and what happened. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed surfacing-required and output-uncertainty facts. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Silently support a certain output from a disputed or uncertain link. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.12.7.8.1 — Proposed connection-use uncertainty-surfacing requirement: proposed surfacing requirement; C-24.12.7.8.2 — Proposed connection-use actual output uncertainty: proposed actual output behavior. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7 — Proposed connection_use_event: audits affected visible output. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7 — Proposed connection_use_event | Required and actual uncertainty behavior. | Preserves the output limitation. | No silent hardening. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.12.7.8.1 — Proposed connection-use uncertainty-surfacing requirement | Surfacing-requirement slot. | Records material output uncertainty. | No hidden obligation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.12.7.8.2 — Proposed connection-use actual output uncertainty | Actual-output slot. | Records delivered or withheld uncertainty behavior. | No assumed disclosure. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: C-24.12.7.8.1 — Proposed connection-use uncertainty-surfacing requirement; C-24.12.7.8.2 — Proposed connection-use actual output uncertainty

### C-24.12.7.8.1 — Proposed connection-use uncertainty-surfacing requirement
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed fact of whether uncertainty had to be surfaced. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Material effect on a claim, interpretation, person statement, recommendation or action. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records whether the output was required to state uncertainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed surfacing-required fact. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Suppress material uncertainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7.8 — Proposed connection-use output uncertainty behavior: records the output obligation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7.8 — Proposed connection-use output uncertainty behavior | Surfacing requirement. | Identifies the necessary output limit. | Visible uncertainty when material. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.7.8.2 — Proposed connection-use actual output uncertainty
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed record of actual output uncertainty behavior where applicable. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — What the accepted output chain delivered or withheld. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records how uncertainty was expressed in the output. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed output-uncertainty behavior. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7.8 — Proposed connection-use output uncertainty behavior: records the actual visible handling. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7.8 — Proposed connection-use output uncertainty behavior | Actual output handling. | Keeps the observed response auditable. | No assumed surfacing. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.7.9 — Proposed connection-use non-use and reason
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed record that evaluated material was not used, with its reason. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Non-use after dispute, staleness, correction, supersession, unresolved history or another failure. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Preserves the omitted relationship and why it was withheld from use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed non-use and reason. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Make evaluated-but-unused material invisible to the operation audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.12.7.9.1 — Proposed connection-use non-use fact: proposed non-use; C-24.12.7.9.2 — Proposed connection-use non-use reason: proposed reason. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7 — Proposed connection_use_event: records deliberate or failed non-use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7 — Proposed connection_use_event | Non-use reason. | Explains why the relationship did not affect the result. | Inspectable omission. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.12.7.9.1 — Proposed connection-use non-use fact | Non-use slot. | Records the omitted relationship. | Exact use outcome. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.12.7.9.2 — Proposed connection-use non-use reason | Reason slot. | Preserves the actual omission basis. | Inspectable failure or exclusion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual dispute/staleness non-use. | Records the named non-use child. | No hidden omission. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: C-24.12.7.9.1 — Proposed connection-use non-use fact; C-24.12.7.9.2 — Proposed connection-use non-use reason

### C-24.12.7.9.1 — Proposed connection-use non-use fact
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed fact that evaluated connection material was not used. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — An actual non-use outcome after evaluation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records that the relationship did not enter the result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed non-use fact. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Report evaluated material as used. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7.9 — Proposed connection-use non-use and reason: preserves the omitted-use outcome. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7.9 — Proposed connection-use non-use and reason | Non-use. | Keeps evaluated-but-unused material visible. | Exact operation outcome. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.7.9.2 — Proposed connection-use non-use reason
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed explanation for non-use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Dispute, correction, supersession, staleness, unresolved history or actual other failure. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records why the relationship was not used. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proposed non-use reason. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7.9 — Proposed connection-use non-use and reason: explains the protective omission. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7.9 — Proposed connection-use non-use and reason | Non-use reason. | Preserves the actual failure or exclusion basis. | Inspectable omission. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.7.10 — Proposed connection-use result or failure reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed result/failure reference of the consuming use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The actual operation result or failure record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Links the audit to the observed outcome. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A proposed result or failure reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Claim success without its committed result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7 — Proposed connection_use_event: links use to outcome. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7 — Proposed connection_use_event | Result or failure. | Preserves actual operation truth. | No assumed success. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.7.11 — Proposed connection retrieval-audit additions
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]

ALONE
- What it is: ACCEPTED — The proposed retrieval-specific audit slots supplementing the common use event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Takes in: ACCEPTED — Source-type labels, eligibility reason, changed search scope, what was retrieved, effect on a later claim, failure, omission and truncation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Does: ACCEPTED — Preserves the retrieval selection and downstream effect without making the log evidence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Gives out: ACCEPTED — The complete proposed retrieval audit additions. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Must never: ACCEPTED — Count retrieval or repeated logs as confirmation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.12.7.11.1 — Proposed retrieval-audit source-type labels: proposed source labels; C-24.12.7.11.2 — Proposed retrieval-audit eligibility reason: proposed eligibility reason; C-24.12.7.11.3 — Proposed retrieval-audit search-scope effect: proposed scope effect; C-24.12.7.11.4 — Proposed retrieval-audit retrieved material: proposed retrieved material; C-24.12.7.11.5 — Proposed retrieval-audit later-claim effect: proposed claim effect; C-24.12.7.11.6 — Proposed retrieval-audit failure: proposed failure; C-24.12.7.11.7 — Proposed retrieval-audit omission: proposed omission; C-24.12.7.11.8 — Proposed retrieval-audit truncation: proposed truncation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7 — Proposed connection_use_event: completes the retrieval-side use audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7 — Proposed connection_use_event | Retrieval scope, result and limitation facts. | Explains what the connection changed about search. | No hidden context promotion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D] |
| 2 · ACCEPTED | C-24.12.7.11.1 — Proposed retrieval-audit source-type labels | Source-classification slots. | Records the exact used labels. | No source promotion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D] |
| 3 · ACCEPTED | C-24.12.7.11.2 — Proposed retrieval-audit eligibility reason | Eligibility-reason slot. | Records why the use was allowed. | No unexplained admission. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D] |
| 4 · ACCEPTED | C-24.12.7.11.3 — Proposed retrieval-audit search-scope effect | Search-scope slot. | Records the actual scope change. | No lasting acceptance from search. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D] |
| 5 · ACCEPTED | C-24.12.7.11.4 — Proposed retrieval-audit retrieved material | Returned-material slot. | Records actual retrieved references. | Exact result scope. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D] |
| 6 · ACCEPTED | C-24.12.7.11.5 — Proposed retrieval-audit later-claim effect | Claim-effect slot. | Records later claim influence. | No hidden support. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D] |
| 7 · ACCEPTED | C-24.12.7.11.6 — Proposed retrieval-audit failure | Failure slot. | Records retrieval failure. | No false completeness. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D] |
| 8 · ACCEPTED | C-24.12.7.11.7 — Proposed retrieval-audit omission | Omission slot. | Records missing returned material. | No assumed inspection. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D] |
| 9 · ACCEPTED | C-24.12.7.11.8 — Proposed retrieval-audit truncation | Truncation slot. | Records the returned-content boundary. | No false full source. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D] |

SUB-PARTS: C-24.12.7.11.1 — Proposed retrieval-audit source-type labels; C-24.12.7.11.2 — Proposed retrieval-audit eligibility reason; C-24.12.7.11.3 — Proposed retrieval-audit search-scope effect; C-24.12.7.11.4 — Proposed retrieval-audit retrieved material; C-24.12.7.11.5 — Proposed retrieval-audit later-claim effect; C-24.12.7.11.6 — Proposed retrieval-audit failure; C-24.12.7.11.7 — Proposed retrieval-audit omission; C-24.12.7.11.8 — Proposed retrieval-audit truncation

### C-24.12.7.11.1 — Proposed retrieval-audit source-type labels
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]

ALONE
- What it is: ACCEPTED — The proposed source labels carried in the retrieval audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Takes in: ACCEPTED — The exact five-way classification of each support item. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Does: ACCEPTED — Preserves the source types actually used. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Gives out: ACCEPTED — Proposed source-type audit labels. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Must never: ACCEPTED — Promote interpretation or simulation to source evidence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7.11 — Proposed connection retrieval-audit additions: records the used material types. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7.11 — Proposed connection retrieval-audit additions | Source-type labels. | Keeps input classification visible. | No source promotion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D] |

SUB-PARTS: NONE

### C-24.12.7.11.2 — Proposed retrieval-audit eligibility reason
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]

ALONE
- What it is: ACCEPTED — The proposed record of why the relationship was eligible. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Takes in: ACCEPTED — The actual purpose, route and current authorization/resolution facts. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Does: ACCEPTED — Records the eligibility basis of this retrieval. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Gives out: ACCEPTED — Proposed eligibility reason. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Must never: ACCEPTED — Treat relevance as authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7.11 — Proposed connection retrieval-audit additions: explains admitted use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7.11 — Proposed connection retrieval-audit additions | Eligibility reason. | Makes the permitted use inspectable. | No unexplained admission. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D] |

SUB-PARTS: NONE

### C-24.12.7.11.3 — Proposed retrieval-audit search-scope effect
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]

ALONE
- What it is: ACCEPTED — The proposed record of what the relationship changed about search scope. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Takes in: ACCEPTED — The actual change in retrieval search scope. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Does: ACCEPTED — Records that effect without asserting a new relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Gives out: ACCEPTED — Proposed search-scope effect. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Must never: ACCEPTED — Treat expanded search as acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7.11 — Proposed connection retrieval-audit additions: preserves the retrieval effect. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7.11 — Proposed connection retrieval-audit additions | Search-scope change. | Explains the relationship role in retrieval. | No lasting effect from searching. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D] |

SUB-PARTS: NONE

### C-24.12.7.11.4 — Proposed retrieval-audit retrieved material
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]

ALONE
- What it is: ACCEPTED — The proposed record of what was actually retrieved. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Takes in: ACCEPTED — The real returned material references. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Does: ACCEPTED — Keeps the retrieved result identifiable. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Gives out: ACCEPTED — Proposed retrieved-material references. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Must never: ACCEPTED — Claim retrieval of omitted material. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7.11 — Proposed connection retrieval-audit additions: preserves the actual retrieval result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7.11 — Proposed connection retrieval-audit additions | Retrieved material. | Keeps returned context inspectable. | Exact retrieval history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D] |

SUB-PARTS: NONE

### C-24.12.7.11.5 — Proposed retrieval-audit later-claim effect
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]

ALONE
- What it is: ACCEPTED — The proposed fact of whether the relationship affected a later claim. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Takes in: ACCEPTED — The actual downstream claim use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Does: ACCEPTED — Records whether the retrieved connection influenced that claim. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Gives out: ACCEPTED — Proposed later-claim effect. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Must never: ACCEPTED — Hide a material relationship influence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7.11 — Proposed connection retrieval-audit additions: records downstream claim use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7.11 — Proposed connection retrieval-audit additions | Later-claim effect. | Makes downstream influence inspectable. | No hidden claim support. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D] |

SUB-PARTS: NONE

### C-24.12.7.11.6 — Proposed retrieval-audit failure
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]

ALONE
- What it is: ACCEPTED — The proposed retrieval failure slot. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Takes in: ACCEPTED — Any actual failure of the retrieval operation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Does: ACCEPTED — Records the failure alongside relationship-use facts. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Gives out: ACCEPTED — Proposed failure record/reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Must never: ACCEPTED — Claim complete successful retrieval on failure. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7.11 — Proposed connection retrieval-audit additions: preserves retrieval failure. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7.11 — Proposed connection retrieval-audit additions | Retrieval failure. | Retains actual result limitations. | No false success. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D] |

SUB-PARTS: NONE

### C-24.12.7.11.7 — Proposed retrieval-audit omission
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]

ALONE
- What it is: ACCEPTED — The proposed record of retrieval omission. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Takes in: ACCEPTED — Material actually omitted from the retrieval result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Does: ACCEPTED — Records the omission as a limitation on available context. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Gives out: ACCEPTED — Proposed omission record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Must never: ACCEPTED — Treat omitted context as inspected evidence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7.11 — Proposed connection retrieval-audit additions: preserves missing-result scope. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7.11 — Proposed connection retrieval-audit additions | Omission. | Keeps context limitations explicit. | No assumed completeness. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D] |

SUB-PARTS: NONE

### C-24.12.7.11.8 — Proposed retrieval-audit truncation
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]

ALONE
- What it is: ACCEPTED — The proposed record of retrieval truncation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Takes in: ACCEPTED — Any truncation affecting the returned material. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Does: ACCEPTED — Records that limitation in the audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Gives out: ACCEPTED — Proposed truncation record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Must never: ACCEPTED — Present truncated context as a full source. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.7.11 — Proposed connection retrieval-audit additions: preserves the result boundary. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.7.11 — Proposed connection retrieval-audit additions | Truncation. | Keeps the actual extent of context visible. | No false full context. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13D] |

SUB-PARTS: NONE

### C-24.12.8 — Proposed connection_duplicate_absorbed
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The proposed duplicate-suppression event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — A repeated relationship or authority attempt under its stable key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records absorption of a duplicate without creating another relationship or proof. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A proposed connection_duplicate_absorbed event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Add evidence weight or certainty from duplicate attempts. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12 — Proposed connection mechanical records: preserves duplicate handling. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12 — Proposed connection mechanical records | The proposed absorbed duplicate. | Keeps retry history without repeated support. | One logical result. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual duplicate absorption. | Records the absorbed child event. | No added evidence. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-24.12.9 — Proposed connection_operation
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — The one proposed parent connection_operation per real connection operation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Takes in: ACCEPTED — The stable proposed connection_operation_id and the operation children. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Does: ACCEPTED — Keeps proposal, verification, decision, authority and recovery work in one logical operation history. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Gives out: ACCEPTED — A proposed parent operation and checkpoint. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Must never: ACCEPTED — Substitute this identity for visible-output or delivery identities. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.12.9.1 — Proposed connection_operation_id: proposed stable connection operation ID. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12 — Proposed connection mechanical records: identifies the connection parent; C-24.3.1 — Proposed connection_proposal_record: binds the proposal to its operation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12 — Proposed connection mechanical records | The proposed parent operation. | Keeps one real operation history. | No duplicate parent. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.3.1 — Proposed connection_proposal_record | The parent operation ID. | Links the proposal to its actual operation. | Stable provenance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.12.9.1 — Proposed connection_operation_id | Parent-identity slot. | Supplies the stable operation ID. | One logical parent. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 4 · ACCEPTED | C-24.20 — Connection operational recordkeeping | The actual proposed parent. | Keeps one log per real operation. | No duplicate parent. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: C-24.12.9.1 — Proposed connection_operation_id

### C-24.12.9.1 — Proposed connection_operation_id
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — The proposed stable identity of the real connection operation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — The operation being recorded and recovered. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Keys the one parent history without replacing consumer or delivery identities. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — Proposed connection_operation_id. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Re-mint it to create duplicate accepted results. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12.9 — Proposed connection_operation: identifies the single parent operation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12.9 — Proposed connection_operation | Stable connection operation ID. | Keeps operation recovery exact. | One logical parent. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.12.10 — Proposed connection_recovery_event
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — The proposed record of recovery outcomes and uncertainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — Actual durable owner/record facts at a crash boundary. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Records recovery, forward-completion, fresh-decision requirements, unknown outcomes or owner contradictions without recreating missing authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A proposed connection_recovery_event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Let recovery change certainty, grant access or promote a pending relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.12 — Proposed connection mechanical records: preserves the recovery audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.12 — Proposed connection mechanical records | The proposed recovery event. | Retains what recovery actually established. | No reconstructed decision. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual recovery work. | Records the recovery child. | No recovery-derived authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-24.13 — Connection operation lifecycle
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The parent operational lifecycle, separate from decision status and report status. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Takes in: ACCEPTED — Actual verification, Ness decision, rule validity, privacy, record commitment and Person-Box owner outcomes. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Does: ACCEPTED — Moves requested_or_detected through source_facts_gathered, approved_basis_check, duplicate_check, proposal_preparation, proposal_committed and waiting_undecided to the applicable verification/decision pending stage, acceptance_prepared and a terminal result. Self-establishing direct-source relationships may bypass proposal/waiting stages after source facts, basis and duplicate checks. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Gives out: ACCEPTED — An operational state without independent acceptance authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Must never: ACCEPTED — Infer consent from operational progress or merge candidate and proposal lifecycles. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.13.1 — Connection parent states and transitions: parent states and transitions; C-24.13.2 — Connection candidate-report lifecycle: candidate-report states. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24 — Connection Capability (§24): maintains explicit operation progress. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | Operation lifecycle. | Separates progress from accepted truth. | No intermediate acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |
| 2 · ACCEPTED | C-24.13.1 — Connection parent states and transitions | The parent progression. | Preserves sixteen operational states. | No intermediate decision. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |
| 3 · ACCEPTED | C-24.13.2 — Connection candidate-report lifecycle | The report progression. | Keeps five separate report states. | No proposal confusion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |

SUB-PARTS: C-24.13.1 — Connection parent states and transitions; C-24.13.2 — Connection candidate-report lifecycle

### C-24.13.1 — Connection parent states and transitions
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The sixteen named parent states and their source-governed transitions. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Takes in: ACCEPTED — Verification from the actual source owner, explicit decision from Ness, validity from the rule owner, privacy from its owner, record commits from the proposed recordkeeper and identity consequences solely from Person-Boxes. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Does: ACCEPTED — Uses the normal listed order and the direct-source bypass; terminal states do not manufacture any missing decision or authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Gives out: ACCEPTED — The exact parent state and committed checkpoint. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Must never: ACCEPTED — Let a terminal state manufacture a missing decision or authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.13.1.1 — Connection requested_or_detected state: requested_or_detected; C-24.13.1.2 — Connection source_facts_gathered state: source_facts_gathered; C-24.13.1.3 — Connection approved_basis_check state: approved_basis_check; C-24.13.1.4 — Connection duplicate_check state: duplicate_check; C-24.13.1.5 — Connection proposal_preparation state: proposal_preparation; C-24.13.1.6 — Connection proposal_committed state: proposal_committed; C-24.13.1.7 — Connection waiting_undecided state: waiting_undecided; C-24.13.1.8 — Connection direct_source_verification_pending state: direct_source_verification_pending; C-24.13.1.9 — Connection ness_decision_pending state: ness_decision_pending; C-24.13.1.10 — Connection authorized_rule_verification_pending state: authorized_rule_verification_pending; C-24.13.1.11 — Connection acceptance_prepared state: acceptance_prepared; C-24.13.1.12 — Connection accepted_commit state: accepted_commit; C-24.13.1.13 — Connection rejected_commit state: rejected_commit; C-24.13.1.14 — Connection blocked state: blocked; C-24.13.1.15 — Connection failed state: failed; C-24.13.1.16 — Connection completed state: completed. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13 — Connection operation lifecycle: supplies the parent transition vocabulary. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13 — Connection operation lifecycle | The exact state progression. | Records operational progress under the actual decision owners. | No substitute authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |
| 2 · ACCEPTED | C-24.13.1.1 — Connection requested_or_detected state | The start state. | Begins a real detected/requested operation. | No relationship from detection. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |
| 3 · ACCEPTED | C-24.13.1.2 — Connection source_facts_gathered state | The gathered-facts state. | Passes actual facts to basis checks. | No verification from gathering. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |
| 4 · ACCEPTED | C-24.13.1.3 — Connection approved_basis_check state | The approved-basis stage. | Checks the three-route boundary. | No fourth basis. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |
| 5 · ACCEPTED | C-24.13.1.4 — Connection duplicate_check state | The duplicate-check stage. | Keeps key convergence atomic. | No racing duplicate. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |
| 6 · ACCEPTED | C-24.13.1.5 — Connection proposal_preparation state | The preparation stage. | Separates readiness from durable proposal. | No phantom proposal. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 7 · ACCEPTED | C-24.13.1.6 — Connection proposal_committed state | The committed-proposal stage. | Establishes actual undecided truth. | No automatic choice. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 8 · ACCEPTED | C-24.13.1.7 — Connection waiting_undecided state | The waiting stage. | Preserves indefinite undecided status. | No expiry into acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 9 · ACCEPTED | C-24.13.1.8 — Connection direct_source_verification_pending state | The source-verification wait. | Awaits actual owner verification. | No substitute verifier. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |
| 10 · ACCEPTED | C-24.13.1.9 — Connection ness_decision_pending state | The Ness-decision wait. | Awaits explicit choice. | No silence consent. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5B] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |
| 11 · ACCEPTED | C-24.13.1.10 — Connection authorized_rule_verification_pending state | The rule-verification wait. | Awaits current exact applicability. | No invented rule. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |
| 12 · ACCEPTED | C-24.13.1.11 — Connection acceptance_prepared state | The prepared-acceptance stage. | Keeps readiness nonauthoritative. | No precommit acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |
| 13 · ACCEPTED | C-24.13.1.12 — Connection accepted_commit state | The accepted terminal result. | Recognizes the complete atomic commit. | Recoverable proof. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |
| 14 · ACCEPTED | C-24.13.1.13 — Connection rejected_commit state | The rejected terminal result. | Preserves rejection and suppression. | No accepted relationship. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |
| 15 · ACCEPTED | C-24.13.1.14 — Connection blocked state | The blocked terminal result. | Stops unresolved unsafe work. | Honest uncertainty. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20] |
| 16 · ACCEPTED | C-24.13.1.15 — Connection failed state | The failed terminal result. | Records failure without authority. | No fabricated success. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20] |
| 17 · ACCEPTED | C-24.13.1.16 — Connection completed state | The completed terminal result. | Closes real operation progress. | No new confirmation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: C-24.13.1.1 — Connection requested_or_detected state; C-24.13.1.2 — Connection source_facts_gathered state; C-24.13.1.3 — Connection approved_basis_check state; C-24.13.1.4 — Connection duplicate_check state; C-24.13.1.5 — Connection proposal_preparation state; C-24.13.1.6 — Connection proposal_committed state; C-24.13.1.7 — Connection waiting_undecided state; C-24.13.1.8 — Connection direct_source_verification_pending state; C-24.13.1.9 — Connection ness_decision_pending state; C-24.13.1.10 — Connection authorized_rule_verification_pending state; C-24.13.1.11 — Connection acceptance_prepared state; C-24.13.1.12 — Connection accepted_commit state; C-24.13.1.13 — Connection rejected_commit state; C-24.13.1.14 — Connection blocked state; C-24.13.1.15 — Connection failed state; C-24.13.1.16 — Connection completed state

### C-24.13.1.1 — Connection requested_or_detected state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The requested_or_detected starting state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Takes in: ACCEPTED — A real connection request or detection. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Does: ACCEPTED — Begins source-fact gathering under one operation identity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Gives out: ACCEPTED — Transition toward source_facts_gathered. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Must never: ACCEPTED — Create a proposal from detection alone. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13.1 — Connection parent states and transitions: starts the parent lifecycle. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13.1 — Connection parent states and transitions | requested_or_detected. | Begins the actual operation. | No relationship from detection. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |

SUB-PARTS: NONE

### C-24.13.1.2 — Connection source_facts_gathered state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The source_facts_gathered state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Takes in: ACCEPTED — Gathered immutable source facts. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Does: ACCEPTED — Passes the gathered facts to approved_basis_check; the verified direct-source bypass starts here. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Gives out: ACCEPTED — Source facts ready for basis examination. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Must never: ACCEPTED — Treat gathering as source-owner verification. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13.1 — Connection parent states and transitions: supplies the gathered-facts stage. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13.1 — Connection parent states and transitions | source_facts_gathered. | Advances to basis checking. | No acceptance from collection. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |

SUB-PARTS: NONE

### C-24.13.1.3 — Connection approved_basis_check state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The approved_basis_check state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Takes in: ACCEPTED — The actual source, Ness or rule route. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Does: ACCEPTED — Checks for one of the three approved bases before duplicate comparison. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Gives out: ACCEPTED — Progress to duplicate_check if the route is valid. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Must never: ACCEPTED — Invent a fourth basis. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Fails closed by: ACCEPTED — No approved basis leaves the relationship unknown and unlinked. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13.1 — Connection parent states and transitions: marks basis examination. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13.1 — Connection parent states and transitions | approved_basis_check. | Requires an approved route. | No similarity basis. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |

SUB-PARTS: NONE

### C-24.13.1.4 — Connection duplicate_check state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The duplicate_check stage. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Takes in: ACCEPTED — The exact proposed relationship and authority identities. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Does: ACCEPTED — Checks duplicate state within the same atomic boundary as any later acceptance; normally proceeds to proposal preparation, or to direct accepted_commit for a verified self-establishing source. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Gives out: ACCEPTED — Duplicate convergence or the next eligible route stage. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Must never: ACCEPTED — Separate the duplicate check into a racing acceptance window. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13.1 — Connection parent states and transitions: marks canonical duplicate examination. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13.1 — Connection parent states and transitions | duplicate_check. | Keeps race control bound to commitment. | One logical relationship. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |

SUB-PARTS: NONE

### C-24.13.1.5 — Connection proposal_preparation state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — The proposal_preparation stage. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — A properly based relationship after duplicate checking. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Prepares the exact reference-bearing proposal for durable commitment. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A prepared proposal, not yet a durable proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Treat preparation or ID reservation as proposal existence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — No durable proposal record means no proposal exists. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13.1 — Connection parent states and transitions: separates preparation from proposal truth. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13.1 — Connection parent states and transitions | proposal_preparation. | Prepares without claiming commitment. | No provisional proposal truth. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |

SUB-PARTS: NONE

### C-24.13.1.6 — Connection proposal_committed state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — The proposal_committed stage. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — The durable proposal record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Establishes the actual proposal and enters waiting_undecided. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A durable undecided proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Auto-decide the committed proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13.1 — Connection parent states and transitions: records durable proposal creation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13.1 — Connection parent states and transitions | proposal_committed. | Recognizes the durable proposal only. | Undecided waiting. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |
| 2 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual proposal creation. | Records the creation child. | Durable proposal history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-24.13.1.7 — Connection waiting_undecided state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — The waiting_undecided operational state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — A durable proposal without a decision. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Waits indefinitely for the applicable direct verification, Ness decision or authorized-rule verification. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A still-undecided proposal and applicable pending route. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Age into acceptance or automatically re-ask after restart. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13.1 — Connection parent states and transitions: preserves indefinite waiting. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13.1 — Connection parent states and transitions | waiting_undecided. | Keeps the proposal without force. | No pressure or expiry. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |
| 2 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual waiting outcome. | Records waiting without promotion. | No time-based force. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-24.13.1.8 — Connection direct_source_verification_pending state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The direct_source_verification_pending route state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Takes in: ACCEPTED — The actual source owner verification request. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Does: ACCEPTED — Waits for the owner result and continues only through the verified direct-source route. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Gives out: ACCEPTED — Pending source verification or its actual outcome. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Must never: ACCEPTED — Let a model or the proposed recordkeeper substitute for the owner. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Fails closed by: ACCEPTED — Unavailable or failed verification cannot produce accepted commitment. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13.1 — Connection parent states and transitions: marks the source-verification wait. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13.1 — Connection parent states and transitions | direct_source_verification_pending. | Keeps owner verification explicit. | No invented result. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |

SUB-PARTS: NONE

### C-24.13.1.9 — Connection ness_decision_pending state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5B] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The ness_decision_pending route state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5B] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Takes in: ACCEPTED — The exact current proposal shown under accepted output and access rules. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5B] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Does: ACCEPTED — Waits for an explicit valid Ness decision. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5B] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Gives out: ACCEPTED — Pending choice or durable explicit input. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5B] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Must never: ACCEPTED — Treat seeing, silence or continued conversation as consent. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5B] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Fails closed by: ACCEPTED — No actual decision leaves the proposal undecided. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5B] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13.1 — Connection parent states and transitions: marks the explicit-decision wait. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5B] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13.1 — Connection parent states and transitions | ness_decision_pending. | Retains actual Ness choice as the decision source. | No inferred consent. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |

SUB-PARTS: NONE

### C-24.13.1.10 — Connection authorized_rule_verification_pending state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The authorized_rule_verification_pending route state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Takes in: ACCEPTED — An existing narrow rule and its actual owner facts. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Does: ACCEPTED — Waits for exact current match and final revalidation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Gives out: ACCEPTED — Verified applicability or no acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Must never: ACCEPTED — Invent, widen or revive a rule. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Fails closed by: ACCEPTED — Missing or invalid authority blocks the rule route. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13.1 — Connection parent states and transitions: marks rule-verification progress. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13.1 — Connection parent states and transitions | authorized_rule_verification_pending. | Keeps current rule validity explicit. | No broad authorization. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |

SUB-PARTS: NONE

### C-24.13.1.11 — Connection acceptance_prepared state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The acceptance_prepared stage before the final atomic outcome. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Takes in: ACCEPTED — The eligible route facts and prepared record/proof. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Does: ACCEPTED — Prepares the complete commitment subject to the final route checks. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Gives out: ACCEPTED — Prepared acceptance without committed accepted truth. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Must never: ACCEPTED — Treat preparation as acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Fails closed by: ACCEPTED — Any failed final condition blocks commitment. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13.1 — Connection parent states and transitions: separates readiness from accepted_commit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13.1 — Connection parent states and transitions | acceptance_prepared. | Keeps provisional progress nonauthoritative. | No premature accepted state. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |

SUB-PARTS: NONE

### C-24.13.1.12 — Connection accepted_commit state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The terminal accepted_commit result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Takes in: ACCEPTED — The complete atomic accepted record, proof and applicable final decision. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Does: ACCEPTED — Records accepted commitment under the route authority and stable key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Gives out: ACCEPTED — One recoverable accepted result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Must never: ACCEPTED — Recover only the record while manufacturing its missing proof. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Fails closed by: ACCEPTED — Partial or contradictory truth remains blocked. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13.1 — Connection parent states and transitions: records terminal acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13.1 — Connection parent states and transitions | accepted_commit. | Recognizes the complete recoverable truth. | No split commitment. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |
| 2 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual atomic acceptance. | Records the complete accepted child. | No extra vote. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-24.13.1.13 — Connection rejected_commit state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The terminal rejected_commit result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Takes in: ACCEPTED — A durable final rejection. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Does: ACCEPTED — Preserves rejection and idempotent suppression registration. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Gives out: ACCEPTED — The rejected outcome with no accepted connection. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Must never: ACCEPTED — Erase or retry the rejected decision. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13.1 — Connection parent states and transitions: records terminal rejection. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13.1 — Connection parent states and transitions | rejected_commit. | Keeps the actual rejected history. | No lasting accepted link. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |

SUB-PARTS: NONE

### C-24.13.1.14 — Connection blocked state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — The terminal blocked operational result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Takes in: ACCEPTED — An unresolved identity, authority, privacy, integrity or owner contradiction. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Does: ACCEPTED — Stops the dependent operation without strengthening the relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Gives out: ACCEPTED — A blocked outcome and reason. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Must never: ACCEPTED — Resolve a contradiction in favor of the proposed recordkeeper. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Fails closed by: ACCEPTED — No new acceptance, use, identity consequence or disclosure is authorized. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13.1 — Connection parent states and transitions: records a protective blocked outcome. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13.1 — Connection parent states and transitions | blocked. | Preserves uncertainty without force. | No unsafe progress. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |

SUB-PARTS: NONE

### C-24.13.1.15 — Connection failed state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — The terminal failed operational result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Takes in: ACCEPTED — The actual failed operation and failure reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Does: ACCEPTED — Records failure without manufacturing an accepted relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Gives out: ACCEPTED — A failed outcome retaining history and certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Must never: ACCEPTED — Let failure promote pending status or grant access. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Fails closed by: ACCEPTED — The dependent effect does not proceed. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13.1 — Connection parent states and transitions: records actual failure. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13.1 — Connection parent states and transitions | failed. | Keeps the failure visible. | No false success. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |

SUB-PARTS: NONE

### C-24.13.1.16 — Connection completed state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — The terminal completed operational result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Takes in: ACCEPTED — The completed real operation and its required records. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Does: ACCEPTED — Closes operational progress without adding authority or evidence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Gives out: ACCEPTED — A completed parent outcome. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Must never: ACCEPTED — Treat operational completion as a new confirmation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13.1 — Connection parent states and transitions: records completion only. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13.1 — Connection parent states and transitions | completed. | Ends the recorded operation. | No added evidence weight. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |

SUB-PARTS: NONE

### C-24.13.2 — Connection candidate-report lifecycle
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The separate lifecycle for a Route A-2 candidate report. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Takes in: ACCEPTED — Submitted report and actual owner verification. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Does: ACCEPTED — Moves submitted to verification_pending or technically_blocked, then to verified_self_establishing or evaluated_and_set_aside. Unavailable verification stays pending/blocked with no force. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Gives out: ACCEPTED — The report state, independently of proposal status. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Must never: ACCEPTED — Recover a candidate report as a proposal or leave not_verified material active. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Fails closed by: ACCEPTED — Unavailable verification has no force; a failed or contradictory result creates and preserves no proposal on that failed basis. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

TOGETHER
- Fed by: ACCEPTED — C-24.13.2.1 — Candidate-report submitted state: submitted; C-24.13.2.2 — Candidate-report verification_pending state: verification_pending; C-24.13.2.3 — Candidate-report technically_blocked state: technically_blocked; C-24.13.2.4 — Candidate-report verified_self_establishing terminal state: verified_self_establishing; C-24.13.2.5 — Candidate-report evaluated_and_set_aside terminal state: evaluated_and_set_aside. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13 — Connection operation lifecycle: keeps report progress separate. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Changes: DESIGNED — C-24.3 — Connection waiting area: prevents waiting-area identity collapse. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6]
- Changes: ACCEPTED — C-24.12.2 — Proposed connection_candidate_report: supplies the proposed report lifecycle field. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13 — Connection operation lifecycle | Separate report state machine. | Retains report/proposal separation. | No automatic proposal. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · DESIGNED | C-24.3 — Connection waiting area | Report status distinction. | Keeps failed reports out of proposal waiting. | No failed-basis proposal. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-24.12.2 — Proposed connection_candidate_report | Report lifecycle state. | Records actual verification progress. | A distinct report object. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-24.13.2.1 — Candidate-report submitted state | The submitted state. | Preserves a report-only start. | No accepted record. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 5 · ACCEPTED | C-24.13.2.2 — Candidate-report verification_pending state | The pending state. | Waits without force. | No proposal promotion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |
| 6 · ACCEPTED | C-24.13.2.3 — Candidate-report technically_blocked state | The blocked state. | Keeps technical failure explicit. | No manufactured success. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |
| 7 · ACCEPTED | C-24.13.2.4 — Candidate-report verified_self_establishing terminal state | The verified terminal state. | Hands off to atomic acceptance. | No report-only acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |
| 8 · ACCEPTED | C-24.13.2.5 — Candidate-report evaluated_and_set_aside terminal state | The set-aside terminal state. | Leaves active waiting after failure. | No failed-basis proposal. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] |

SUB-PARTS: C-24.13.2.1 — Candidate-report submitted state; C-24.13.2.2 — Candidate-report verification_pending state; C-24.13.2.3 — Candidate-report technically_blocked state; C-24.13.2.4 — Candidate-report verified_self_establishing terminal state; C-24.13.2.5 — Candidate-report evaluated_and_set_aside terminal state

### C-24.13.2.1 — Candidate-report submitted state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — The submitted report state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — A durable report with exact immutable refs and authorized submission. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Enters owner verification without committing a proposal or accepted record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — submitted. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Treat submission as acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13.2 — Connection candidate-report lifecycle: starts the report lifecycle. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13.2 — Connection candidate-report lifecycle | submitted. | Preserves the received report only. | No proposal creation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.13.2.2 — Candidate-report verification_pending state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The verification_pending report state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Takes in: ACCEPTED — A report awaiting an available owner result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Does: ACCEPTED — Preserves the report without factual, identity, recommendation or action force. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Gives out: ACCEPTED — verification_pending. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Must never: ACCEPTED — Turn technical waiting into normal proposal status. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13.2 — Connection candidate-report lifecycle: retains pending verification. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13.2 — Connection candidate-report lifecycle | verification_pending. | Waits for actual owner facts. | No force. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.13.2.3 — Candidate-report technically_blocked state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The technically_blocked report state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Takes in: ACCEPTED — Unavailable source verification. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Does: ACCEPTED — Retains the report while technical recovery follows accepted retry rules. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Gives out: ACCEPTED — technically_blocked. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Must never: ACCEPTED — Invent verification success on retry. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Fails closed by: ACCEPTED — No accepted connection or verified evidence is supplied while source verification remains unavailable. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13.2 — Connection candidate-report lifecycle: records the technical obstacle. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13.2 — Connection candidate-report lifecycle | technically_blocked. | Preserves unavailable verification honestly. | No fabricated owner result. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.13.2.4 — Candidate-report verified_self_establishing terminal state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The successful terminal report state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Takes in: ACCEPTED — An actual owner verified_self_establishing result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Does: ACCEPTED — Hands the relationship to the atomic direct-source route. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Gives out: ACCEPTED — verified_self_establishing report result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Must never: ACCEPTED — Confuse terminal report success with accepted-record commitment. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13.2 — Connection candidate-report lifecycle: closes verified reporting and hands off. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13.2 — Connection candidate-report lifecycle | verified_self_establishing. | Continues through final atomic acceptance. | No direct report-to-acceptance shortcut. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.13.2.5 — Candidate-report evaluated_and_set_aside terminal state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The failed or contradictory verification terminal state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Takes in: ACCEPTED — not_verified or contradictory owner result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Does: ACCEPTED — Preserves the report/result and removes it from active waiting and repeated surfacing. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Gives out: ACCEPTED — evaluated_and_set_aside. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Must never: ACCEPTED — Preserve a proposal solely on the failed basis or expose this report as pending guidance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]
- Fails closed by: ACCEPTED — No proposal on the failed basis and no uncertainty evidence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.13.2 — Connection candidate-report lifecycle: ends the active failed-report path. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.13.2 — Connection candidate-report lifecycle | evaluated_and_set_aside. | Keeps failure history without continuing force. | Unknown and unlinked. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.14 — Connection current-use resolution
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

ALONE
- What it is: ACCEPTED — The implementation-neutral resolution required before every accepted relationship use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Takes in: ACCEPTED — Exact accepted identity/version and all later correction, clarification, dispute and supersession events with integrity, authority, current applicable version, separate certainty, current privacy and influence-removal facts. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Does: ACCEPTED — Discovers later events by reverse lookup or a derived view without making that view an authority. Preserves original proposal, accepted record, final decision and authority proof immutably. Resolves the nine inputs before any retrieval, identity handoff, visible output, recommendation, action-related or other downstream reasoning use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Gives out: ACCEPTED — The currently applicable version and proposed current_use_state, or a no-use result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Must never: ACCEPTED — Use stale accepted history merely because it exists, rewrite old links or invent final truth closure. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Fails closed by: ACCEPTED — Unresolved, contradictory, unavailable or corrupt chains permit no use, strengthened claim, identity consequence, recommendation, action support or hidden disclosure. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

TOGETHER
- Fed by: ACCEPTED — C-24.14.1 — Connection current-use resolution requirements: nine resolution requirements; C-24.14.2 — Proposed connection current_use_state: proposed current_use_state and outcomes. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current authorization and separate influence-removal status. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Changes: DESIGNED — C-24 — Connection Capability (§24): controls all present use of accepted history. [V10 §24]
- Changes: ACCEPTED — C-24.2.1 — Accepted-connection retrieval route: authorizes only a freshly resolved retrieval version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | Current-use resolution. | Keeps correction history binding without rewriting originals. | No stale use. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |
| 2 · ACCEPTED | C-24.2.1 — Accepted-connection retrieval route | Fresh current version and chain. | Limits retrieval to the resolved authorized relationship. | No original-record shortcut. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-24.14.1 — Connection current-use resolution requirements | The complete resolution contract. | Requires all nine current facts. | No partial-chain use. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |
| 4 · ACCEPTED | C-24.14.2 — Proposed connection current_use_state | The separate status namespace. | Keeps present applicability distinct. | No certainty conflation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |
| 5 · ACCEPTED | C-24.15 — Connection Person-Box handoff | Fresh applicable relationship and chain. | Requires them before identity handoff. | No stale identity context. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 6 · ACCEPTED | C-24.17.19 — Connection crash during accepted retrieval use | Fresh resolution after retrieval interruption. | Re-runs current-use checks. | No stale recovered use. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 7 · ACCEPTED | C-24.19.7 — Connection I7 accepted-use interface | Fresh resolution for every retrieval. | Returns the currently applicable version. | Bounded accepted context. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 8 · ACCEPTED | C-24.19.8 — Connection I8 Person-Box interface | Fresh resolution for every handoff. | Keeps later corrections binding. | No stale identity consequence. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 9 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual current-use resolution. | Records the resolution child. | No increased currentness. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |
| 10 · ACCEPTED | C-24.22 — Connection-owned durable-operation coordination boundary | The required fresh current-use resolution. | Preserves owner checks beyond generic admission. | No per-use bypass. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §T] |
| 11 · ACCEPTED | C-24.14.2.3 — Proposed connection corrected_or_superseded_for_current_use state | Fresh full resolution of a replacement. | Requires the replacement own integrity, authority and current permission. | No guessed or unvalidated successor. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |
| 12 · ACCEPTED | C-LMAC.14.1 — Fresh accepted-connection use through retrieval | Exact connection identity/version, current purpose/scope and a fresh completed current-use resolution. | Supplies canonical per-use resolution. | Nothing in this card. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 13 · ACCEPTED | C-7N.12.3.1.5 — Surfacing valid-new-link log protection | A new link established under the governing connection rules. | Gates this place: accepted-connection use requires current-use resolution. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |
| 14 · DESIGNED | C-7N — Action Surfacing (§7N) | An explicit request or authorized proactive occasion, permitted source support, a current picture and the recorded response history. | Gates this place: before consuming an accepted connection, current-use resolution must authorize that use. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [V10 §7N] [MAP C-7N] |
| 15 · ACCEPTED | C-NEW-UDOK.13.11 — I-11 — B-INT-8 reference interface [proposed] | CRK, authority_event_key, accepted-record/authority-proof and §12C current-use resolution. | Supplies the §12C current-use resolution. | Nothing in this card. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §T] |
| 16 · DESIGNED | C-7O.5.3 — Separate action-result connection object | The proposal and separate Ness response/dispute history. | Gates this place: if consumed as an accepted connection, its current-use correction/dispute resolution must pass; this does not replace result-specific Ness confirmation. | Nothing in this card. | [V10 §7O] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.2] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |
| 17 · ACCEPTED | C-7R.16.8 — Quiet automatic relevance use and material disclosure | A recorded connection and the relevance declaration governing its use. | Supplies canonical current-use rules for connections. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] |
| 18 · ACCEPTED | C-7N.13.6.5 — Action-surfacing explicit_links dimension | Permitted explicit connection references. | Gates this place: any accepted connection consumed must pass current-use resolution. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |
| 19 · ACCEPTED | C-7Q.11.9 — Backup and durable-coordination privacy boundary | Backup restores, current connection uses and recorded operation state. | Supplies connection current-use authorization. | Nothing in this card. | [04/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md §11] [04/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md §16] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md §15] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §U] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §V.2] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §W] |

SUB-PARTS: C-24.14.1 — Connection current-use resolution requirements; C-24.14.2 — Proposed connection current_use_state

### C-24.14.1 — Connection current-use resolution requirements
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

ALONE
- What it is: ACCEPTED — The nine facts every accepted-use resolution must establish. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Takes in: ACCEPTED — The original record, later events and current owner permissions. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Does: ACCEPTED — Resolves every required fact together before downstream use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Gives out: ACCEPTED — A complete resolution or protective non-use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Must never: ACCEPTED — Treat a partially resolved chain as adequate. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Fails closed by: ACCEPTED — Any unresolved or contradictory requirement blocks use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-24.14.1.1 — Current-use exact accepted-record identity: exact accepted ID/version; C-24.14.1.2 — Current-use complete later-event chain: every later event; C-24.14.1.3 — Current-use event integrity: integrity; C-24.14.1.4 — Current-use event owner and authority: authority; C-24.14.1.5 — Current-use applicable relationship version: applicable version; C-24.14.1.6 — Current-use proposed state resolution: proposed current-use state; C-24.14.1.7 — Current-use original certainty preservation: original certainty; C-24.14.1.8 — Current-use privacy authorization: current privacy; C-24.14.1.9 — Current-use influence-removal check: influence removal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Changes: ACCEPTED — C-24.14 — Connection current-use resolution: supplies the complete per-use resolution. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.14 — Connection current-use resolution | All nine resolved facts. | Requires a complete current-use basis. | No partial-chain use. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.14.1.1 — Current-use exact accepted-record identity | Accepted identity requirement. | Resolves exact ID/version. | No ambiguous record. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |
| 3 · ACCEPTED | C-24.14.1.2 — Current-use complete later-event chain | Later-history requirement. | Finds every applicable correction event. | No ignored dispute. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |
| 4 · ACCEPTED | C-24.14.1.3 — Current-use event integrity | Integrity requirement. | Validates consulted history. | No corrupt-chain use. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |
| 5 · ACCEPTED | C-24.14.1.4 — Current-use event owner and authority | Authority requirement. | Resolves actual owner references. | No recordkeeper override. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |
| 6 · ACCEPTED | C-24.14.1.5 — Current-use applicable relationship version | Applicable-version requirement. | Finds a validated current version. | No guessed replacement. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |
| 7 · ACCEPTED | C-24.14.1.6 — Current-use proposed state resolution | Current-use-state requirement. | Resolves the separate proposed namespace. | No certainty merger. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |
| 8 · ACCEPTED | C-24.14.1.7 — Current-use original certainty preservation | Original-certainty requirement. | Preserves the original label. | No currentness promotion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |
| 9 · ACCEPTED | C-24.14.1.8 — Current-use privacy authorization | Current-privacy requirement. | Checks purpose permission now. | No historic access grant. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15] |
| 10 · ACCEPTED | C-24.14.1.9 — Current-use influence-removal check | Influence-removal requirement. | Honors separate exclusion instructions. | No removed influence. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15] |

SUB-PARTS: C-24.14.1.1 — Current-use exact accepted-record identity; C-24.14.1.2 — Current-use complete later-event chain; C-24.14.1.3 — Current-use event integrity; C-24.14.1.4 — Current-use event owner and authority; C-24.14.1.5 — Current-use applicable relationship version; C-24.14.1.6 — Current-use proposed state resolution; C-24.14.1.7 — Current-use original certainty preservation; C-24.14.1.8 — Current-use privacy authorization; C-24.14.1.9 — Current-use influence-removal check

### C-24.14.1.1 — Current-use exact accepted-record identity
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

ALONE
- What it is: ACCEPTED — The exact accepted ID and version required for resolution. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Takes in: ACCEPTED — The requested immutable accepted relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Does: ACCEPTED — Resolves that exact historical object. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Gives out: ACCEPTED — A verified accepted-record identity/version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Must never: ACCEPTED — Substitute a similar record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Fails closed by: ACCEPTED — Missing identity prevents use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.14.1 — Connection current-use resolution requirements: supplies requirement 1. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.14.1 — Connection current-use resolution requirements | Exact record identity/version. | Anchors the resolution. | No ambiguous starting record. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.14.1.2 — Current-use complete later-event chain
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

ALONE
- What it is: ACCEPTED — Every later correction, clarification, dispute and supersession event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Takes in: ACCEPTED — All events pointing back to the accepted history. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Does: ACCEPTED — Finds the complete applicable later chain without editing the original record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Gives out: ACCEPTED — The consulted later-event set. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Must never: ACCEPTED — Ignore a later dispute because the old record is immutable. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Fails closed by: ACCEPTED — Unresolved or contradictory history blocks use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.14.1 — Connection current-use resolution requirements: supplies requirement 2. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.14.1 — Connection current-use resolution requirements | Complete later history. | Makes corrections binding on present use. | No stale history shortcut. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual correction/dispute lookup. | Records the consulted-chain child. | No extra support. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-24.14.1.3 — Current-use event integrity
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

ALONE
- What it is: ACCEPTED — The integrity of the record and consulted later events. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Takes in: ACCEPTED — Their integrity references. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Does: ACCEPTED — Resolves validity before the relationship is used. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Gives out: ACCEPTED — A current integrity result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Must never: ACCEPTED — Assume integrity from record presence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Fails closed by: ACCEPTED — Unavailable or corrupt integrity blocks use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.14.1 — Connection current-use resolution requirements: supplies requirement 3. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.14.1 — Connection current-use resolution requirements | Integrity results. | Keeps corrupt history from supporting use. | Protective non-use. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.14.1.4 — Current-use event owner and authority
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

ALONE
- What it is: ACCEPTED — The actual owner/authority references governing the later history. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Takes in: ACCEPTED — The source and correcting authority references. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Does: ACCEPTED — Resolves their authority rather than adopting a derived-view assertion. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Gives out: ACCEPTED — Verified owner/authority facts. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Must never: ACCEPTED — Prefer the proposed recordkeeper over the actual owner. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Fails closed by: ACCEPTED — An unresolved authority contradiction blocks use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.14.1 — Connection current-use resolution requirements: supplies requirement 4. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.14.1 — Connection current-use resolution requirements | Owner/authority validity. | Keeps actual owners authoritative. | No recordkeeper override. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.14.1.5 — Current-use applicable relationship version
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

ALONE
- What it is: ACCEPTED — The relationship version currently applicable after corrections. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Takes in: ACCEPTED — The complete authorized correction/supersession chain. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Does: ACCEPTED — Resolves the exact applicable version; any replacement passes its own integrity, authority, privacy, access and current-use checks. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Gives out: ACCEPTED — The applicable exact version or no valid replacement. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Must never: ACCEPTED — Infer replacement merely from a dispute. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Fails closed by: ACCEPTED — No validated applicable version means no use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.14.1 — Connection current-use resolution requirements: supplies requirement 5. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.14.1 — Connection current-use resolution requirements | Applicable version. | Rejects stale or guessed replacements. | Exact present relationship. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.14.1.6 — Current-use proposed state resolution
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

ALONE
- What it is: ACCEPTED — The resolution of the proposed current_use_state namespace. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Takes in: ACCEPTED — Append-only current, disputed or corrected_or_superseded_for_current_use events. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Does: ACCEPTED — Determines the present-use state separately from certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Gives out: ACCEPTED — A resolved proposed current_use_state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Must never: ACCEPTED — Conflate the disputed status with disputed certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Fails closed by: ACCEPTED — Contradictory or unavailable state blocks use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.14.1 — Connection current-use resolution requirements: supplies requirement 6. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.14.1 — Connection current-use resolution requirements | Resolved proposed state. | Separates status and certainty. | No namespace confusion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.14.1.7 — Current-use original certainty preservation
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

ALONE
- What it is: ACCEPTED — The original certainty required in every current-use resolution. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Takes in: ACCEPTED — The accepted relationship certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Does: ACCEPTED — Carries it unchanged and separately from the proposed current-use state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Gives out: ACCEPTED — The original qualitative certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Must never: ACCEPTED — Raise certainty because the current-use state is current. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.14.1 — Connection current-use resolution requirements: supplies requirement 7. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.14.1 — Connection current-use resolution requirements | Original certainty. | Retains the relationship evidence limit. | No currentness-to-certainty promotion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.14.1.8 — Current-use privacy authorization
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — The current purpose-specific privacy result for this use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]
- Takes in: ACCEPTED — The present privacy owner decision. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]
- Does: ACCEPTED — Resolves permission inside the current-use check, not only at original acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]
- Gives out: ACCEPTED — Current privacy authorization or refusal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]
- Must never: ACCEPTED — Treat accepted status as access permission. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]
- Fails closed by: ACCEPTED — Refusal prevents the use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current internal-use authorization. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]
- Changes: ACCEPTED — C-24.14.1 — Connection current-use resolution requirements: supplies requirement 8. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.14.1 — Connection current-use resolution requirements | Current privacy result. | Limits use to its permitted purpose. | No old permission carryover. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.14.1.9 — Current-use influence-removal check
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — The separate current influence-removal status. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]
- Takes in: ACCEPTED — Any Ness instruction removing the relationship influence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]
- Does: ACCEPTED — Excludes the relationship from use regardless of its proposed current-use state when influence is separately removed. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]
- Gives out: ACCEPTED — An influence-eligible or excluded result. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]
- Must never: ACCEPTED — Let a connection record or log bypass influence removal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]
- Fails closed by: ACCEPTED — Removed influence prevents use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): separate influence-removal authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]
- Changes: ACCEPTED — C-24.14.1 — Connection current-use resolution requirements: supplies requirement 9. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.14.1 — Connection current-use resolution requirements | Influence-removal status. | Honors the separate exclusion instruction. | No influence bypass. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.14.2 — Proposed connection current_use_state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

ALONE
- What it is: ACCEPTED — The proposed current_use_state namespace with append-only status events. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Takes in: ACCEPTED — current, disputed or corrected_or_superseded_for_current_use, independently of certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Does: ACCEPTED — Keeps later status controlling present use while preserving all earlier records. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Gives out: ACCEPTED — One resolved proposed current-use state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Must never: ACCEPTED — Invent final truth closure or read certainty disputed as this status. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.14.2.1 — Proposed connection current use state: proposed current; C-24.14.2.2 — Proposed connection disputed use state: proposed disputed; C-24.14.2.3 — Proposed connection corrected_or_superseded_for_current_use state: proposed corrected_or_superseded_for_current_use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.14 — Connection current-use resolution: supplies the resolved present-use outcome. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.14 — Connection current-use resolution | The proposed current-use result. | Separates present applicability from original certainty. | History remains preserved. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-24.14.2.1 — Proposed connection current use state | The proposed current outcome. | Allows bounded authorized use. | No wider certainty. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |
| 3 · ACCEPTED | C-24.14.2.2 — Proposed connection disputed use state | The proposed disputed outcome. | Carries dispute through every use. | No silent certain claim. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |
| 4 · ACCEPTED | C-24.14.2.3 — Proposed connection corrected_or_superseded_for_current_use state | The proposed superseded outcome. | Keeps old history out of current use. | Validated replacement only. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |

SUB-PARTS: C-24.14.2.1 — Proposed connection current use state; C-24.14.2.2 — Proposed connection disputed use state; C-24.14.2.3 — Proposed connection corrected_or_superseded_for_current_use state

### C-24.14.2.1 — Proposed connection current use state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

ALONE
- What it is: ACCEPTED — The proposed current value in the current-use namespace. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Takes in: ACCEPTED — The exact resolved accepted version with current authorization. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Does: ACCEPTED — Allows the version within preserved certainty, privacy/access, exact acceptance basis, source labels and its current correction/dispute chain. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Gives out: ACCEPTED — The exact eligible current relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Must never: ACCEPTED — Use current status to increase certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.14.2 — Proposed connection current_use_state: supplies the bounded current outcome. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.14.2 — Proposed connection current_use_state | Proposed current. | Allows only the authorized exact version. | No unbounded authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.14.2.2 — Proposed connection disputed use state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

ALONE
- What it is: ACCEPTED — The proposed disputed current-use state caused by a later dispute. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Takes in: ACCEPTED — The accepted relationship and its applicable dispute. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Does: ACCEPTED — Carries the dispute with every use; materially affected output surfaces uncertainty through the accepted output chain. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Gives out: ACCEPTED — Dispute-qualified use within all other current checks. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Must never: ACCEPTED — Treat this as an undisputed accepted relationship or silently support a certain conclusion. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.14.2 — Proposed connection current_use_state: supplies the dispute-qualified outcome. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.14.2 — Proposed connection current_use_state | Proposed disputed status. | Keeps the dispute attached to every use. | No silent certainty. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.14.2.3 — Proposed connection corrected_or_superseded_for_current_use state
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

ALONE
- What it is: ACCEPTED — The proposed corrected_or_superseded_for_current_use state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Takes in: ACCEPTED — The earlier accepted record and an applicable correction/replacement chain. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Does: ACCEPTED — Keeps the old record as preserved history; follows an exact replacement only after its own complete integrity, authority, privacy, access and current-use checks. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Gives out: ACCEPTED — Preserved old history and, when validated, the replacement version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Must never: ACCEPTED — Use the earlier record as the current relationship or infer a replacement from dispute alone. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Fails closed by: ACCEPTED — An unvalidated replacement gives no current relationship use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-24.14 — Connection current-use resolution: the replacement must pass its own complete fresh current-use resolution, including integrity, authority, current privacy/access and influence-removal checks. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Changes: ACCEPTED — C-24.14.2 — Proposed connection current_use_state: supplies the superseded-history outcome. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.14.2 — Proposed connection current_use_state | Proposed corrected or superseded status. | Preserves history while preventing stale use. | No guessed replacement. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-24.15 — Connection Person-Box handoff
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — The connection-owned handoff of one provenance-bearing generic relationship reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — The currently applicable relationship/version, endpoints, type, certainty, basis, source/evidence, privacy/access and resolved current-use state/chain. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Supplies the generic relationship to the separately authoritative identity owner; cross-references distinct records when evidence matters to both systems. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — The Person-Box owner decision, under its own operation identity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Create a link, unresolved identity anchor, merge or join; duplicate identity proposals in generic waiting; combine people from a generic connection; rewrite either history through correction. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — No current resolution or route-level authorization means no handoff or identity consequence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

TOGETHER
- Fed by: ACCEPTED — C-7L.12 — Person-Box generic-connection use boundary: existing ten-rule generic-connection identity-use boundary. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gated by: ACCEPTED — C-24.14 — Connection current-use resolution: fresh resolution before the first or any repeated handoff. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current route-level authorization for this handoff. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14]
- Changes: DESIGNED — C-24 — Connection Capability (§24): offers bounded provenance without acquiring identity authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | The identity-owner handoff outcome. | Retains the Person-Box owner rules. | No generic-connection identity proof. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-24.17.21 — Connection crash during Person-Box consumption | The identity-handoff requirements. | Repeats only after fresh checks. | No connection-side identity write. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 3 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual Person-Box handoff. | Records the handoff child. | No identity proof from logging. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-24.16 — Connection privacy and visible-output boundary
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — The consumer boundary for privacy, access and visible connection output. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — Current purpose authorization, current access/fence facts and visible proposal/decision/status/uncertainty content refs. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Requires internal-use permission before retrieval/use and immediately before proposal, accepted, rejection and correction commits or identity handoff. Visible output passes privacy first, SACL second, then current fence/owner revalidation before delivery. Shared/observable output uses the shared ceiling; Level-1 endpoints use opaque protected references only. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — Authorized internal work or separately authorized delivered/withheld output. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Copy raw protected content, grant endpoint access from a record, widen Person-Box permission, let another speaker act as Ness, conflate influence removal/hiding/restriction/redaction/deletion-from-view, or signal hidden material through a withheld relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — Withheld content gives no indirect clue that hidden material exists; invalid authorization or influence removal prevents the dependent use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

TOGETHER
- Fed by: ACCEPTED — C-24.16.1 — Proposed connection-output output_operation_id reference: proposed output-operation identity; C-24.16.2 — Proposed connection-output delivery_idempotency_key reference: proposed stable delivery key; C-24.16.3 — Proposed connection-output delivery_attempt_id reference: proposed attempt identity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy and influence-removal decisions; C-SACL — Speaker Access-Control Layer (§25.4): current output access; C-9 — Access/authentication model + voice I/O + phone modes (§9): current identity/access fence and owner facts. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Changes: DESIGNED — C-24 — Connection Capability (§24): confines connection use and disclosure to authorized purposes. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | Privacy and output result. | Preserves access ceilings and nondisclosure. | No access from a connection. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15] |
| 2 · ACCEPTED | C-24.16.1 — Proposed connection-output output_operation_id reference | Output-parent reference requirement. | Preserves the separate stable proposed parent. | No re-minted output. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A] |
| 3 · ACCEPTED | C-24.16.2 — Proposed connection-output delivery_idempotency_key reference | Delivery-key requirement. | Preserves the request/destination duplicate scope. | No mutable key. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A] |
| 4 · ACCEPTED | C-24.16.3 — Proposed connection-output delivery_attempt_id reference | Attempt-reference requirement. | Attaches current facts to each attempt. | No key/attempt conflation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A] |

SUB-PARTS: C-24.16.1 — Proposed connection-output output_operation_id reference; C-24.16.2 — Proposed connection-output delivery_idempotency_key reference; C-24.16.3 — Proposed connection-output delivery_attempt_id reference

### C-24.16.1 — Proposed connection-output output_operation_id reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]

ALONE
- What it is: ACCEPTED — The consumed proposed B-INT-6 output_operation_id, one stable parent for the visible output. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]
- Takes in: ACCEPTED — The output owner stable logical operation identity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]
- Does: ACCEPTED — Keeps this identity distinct from the connection operation and delivery duplicate key; never re-mints it on safe retry. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]
- Gives out: ACCEPTED — A proposed output_operation_id reference owned by the accepted output chain. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]
- Must never: ACCEPTED — Replace it with the connection operation ID or claim a new delivery identity system. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.16 — Connection privacy and visible-output boundary: identifies the visible-output parent. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.16 — Connection privacy and visible-output boundary | Stable output parent reference. | Retains the output owner identity contract. | No re-minted output. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 2 · ACCEPTED | C-24.19.10 — Connection I10 visible-output interface | The stable proposed output parent. | Uses the accepted output owner identity. | No replacement by connection ID. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-24.16.2 — Proposed connection-output delivery_idempotency_key reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]

ALONE
- What it is: ACCEPTED — The consumed proposed B-INT-6 delivery_idempotency_key, distinct from the output parent. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]
- Takes in: ACCEPTED — The request identity and destination. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]
- Does: ACCEPTED — Uses the same stable logical delivery token across every safe retry of that output. Excludes mode epoch/generation and privacy, SACL, PBR, observability, owner and fence versions. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]
- Gives out: ACCEPTED — A proposed stable delivery duplicate-prevention key reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]
- Must never: ACCEPTED — Let a fresh gate pass, generation, claim or attempt create permission for a second visible copy. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]
- Fails closed by: ACCEPTED — Unknown delivery follows the output owner recovery; exactly-once visibility is promised only where the channel has verified idempotency on this token, otherwise no blind resend or automatic duplicate attempt. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.16 — Connection privacy and visible-output boundary: retains the delivery owner duplicate scope. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.16 — Connection privacy and visible-output boundary | The stable delivery key. | Prevents identity drift across safe retries. | No duplicate output token. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 2 · ACCEPTED | C-24.19.10 — Connection I10 visible-output interface | The stable proposed delivery token. | Preserves duplicate scope across safe retries. | No second-copy permission. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-24.16.3 — Proposed connection-output delivery_attempt_id reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]

ALONE
- What it is: ACCEPTED — The consumed proposed B-INT-6 delivery_attempt_id for one actual attempt. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]
- Takes in: ACCEPTED — An individual attempt under the stable output parent and stable delivery key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]
- Does: ACCEPTED — Attaches the current mode_runtime_epoch_id [proposed], current_committed_mode_generation [proposed], privacy-decision version, SACL state version, PBR version, observability version and delivery-fence reference to this attempt rather than to the stable duplicate key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]
- Gives out: ACCEPTED — A separate proposed attempt identity and current validation facts. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]
- Must never: ACCEPTED — Make mutable authorization facts part of the stable delivery key or invent connection-owned output retry rules. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.16 — Connection privacy and visible-output boundary: preserves per-attempt validation separately. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6A]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.16 — Connection privacy and visible-output boundary | Attempt identity and current facts. | Keeps authorization freshness distinct from duplicate identity. | No mutable key. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 2 · ACCEPTED | C-24.19.10 — Connection I10 visible-output interface | The proposed individual attempt reference. | Keeps mutable facts on the attempt. | Stable delivery identity. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-24.17 — Connection crash and restart recovery
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — The twenty-two crash boundaries governing durable connection truth. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — Actual committed source, proposal, input, decision, authority and consumer records. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Queries unknown accepted outcomes by operation ID, proposed CRK, proposal ID/version, reserved accepted-record ID, proposed authority_event_key and final decision-event identity before retry. Recovers complete commits rather than recreating them; no durable proposal means none exists. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — The recovered exact state, blocked uncertainty or a justified idempotent continuation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Reconstruct missing evidence/choice/authority, promote waiting, change certainty, grant access or identity effects, re-ask automatically, or recover a report as a proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — Unknown or contradictory truth remains blocked; actual owners prevail. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: ACCEPTED — C-24.17.1 — Connection crash before proposal reservation: pre-reservation; C-24.17.2 — Connection crash after identity reservation: reserved-only; C-24.17.3 — Connection crash after proposal commitment: proposal committed; C-24.17.4 — Connection crash during undecided waiting: waiting; C-24.17.5 — Connection crash after proposal display: displayed; C-24.17.6 — Connection crash after durable Ness input: durable input; C-24.17.7 — Connection crash after acceptance before checkpoint: accepted before checkpoint; C-24.17.8 — Connection unknown accepted-commit outcome: unknown commit; C-24.17.9 — Connection crash during source verification: source verification; C-24.17.10 — Connection crash after verified source before commit: verified before commit; C-24.17.11 — Connection crash during rule match: rule match; C-24.17.12 — Connection crash before final rule revalidation: before rule revalidation; C-24.17.13 — Connection crash after rule revalidation: after rule revalidation; C-24.17.14 — Connection crash during rejection: rejection; C-24.17.15 — Connection crash after rejection before suppression checkpoint: suppression checkpoint; C-24.17.16 — Connection crash while adding pending new evidence: pending new evidence; C-24.17.17 — Connection crash while creating a linked post-rejection proposal: linked post-rejection proposal; C-24.17.18 — Connection crash during correction or dispute: correction; C-24.17.19 — Connection crash during accepted retrieval use: accepted retrieval; C-24.17.20 — Connection crash during pending investigation use: pending investigation; C-24.17.21 — Connection crash during Person-Box consumption: identity handoff; C-24.17.22 — Connection record and actual-owner contradiction: owner contradiction. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24 — Connection Capability (§24): preserves exact committed truth through interruption. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | Recovered operation state. | Keeps authority and records inseparable. | No crash-induced acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 2 · ACCEPTED | C-24.17.1 — Connection crash before proposal reservation | Pre-reservation crash truth. | Recovers nothing and permits detection. | No proposal. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 3 · ACCEPTED | C-24.17.2 — Connection crash after identity reservation | Reserved-only crash truth. | Reuses or abandons the reserved ID. | No durable proposal claim. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 4 · ACCEPTED | C-24.17.3 — Connection crash after proposal commitment | Committed-proposal crash truth. | Preserves undecided status. | No auto-decision. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 5 · ACCEPTED | C-24.17.4 — Connection crash during undecided waiting | Waiting crash truth. | Preserves indefinite waiting. | No age-based acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 6 · ACCEPTED | C-24.17.5 — Connection crash after proposal display | Display-only crash truth. | Requires fresh action for a later decision. | No consent from seeing. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 7 · ACCEPTED | C-24.17.6 — Connection crash after durable Ness input | Durable-input crash truth. | Revalidates all ten conditions. | No silent rebinding. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 8 · ACCEPTED | C-24.17.7 — Connection crash after acceptance before checkpoint | Complete accepted-commit truth. | Finishes only the missing checkpoint. | No recreated acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 9 · ACCEPTED | C-24.17.8 — Connection unknown accepted-commit outcome | Unknown commit truth. | Queries exact identities before retry. | No blind acceptance retry. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 10 · ACCEPTED | C-24.17.9 — Connection crash during source verification | Source-verification crash truth. | Re-asks the actual owner. | No report/proposal collapse. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 11 · ACCEPTED | C-24.17.10 — Connection crash after verified source before commit | Verified-before-commit truth. | Revalidates and atomically commits once. | No verification-only acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 12 · ACCEPTED | C-24.17.11 — Connection crash during rule match | Interrupted rule match. | Re-matches the current version. | No stale rule. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 13 · ACCEPTED | C-24.17.12 — Connection crash before final rule revalidation | Matched-before-revalidation truth. | Rechecks rule validity. | No revoked acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 14 · ACCEPTED | C-24.17.13 — Connection crash after rule revalidation | Revalidated-before-commit truth. | Rechecks doubt and commits once. | No detached proof. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 15 · ACCEPTED | C-24.17.14 — Connection crash during rejection | Interrupted rejection truth. | Completes only actual durable rejection. | Undecided if uncommitted. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 16 · ACCEPTED | C-24.17.15 — Connection crash after rejection before suppression checkpoint | Rejected-before-suppression truth. | Restores suppression idempotently. | No reopened choice. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 17 · ACCEPTED | C-24.17.16 — Connection crash while adding pending new evidence | Pending-evidence append truth. | Creates a new version only. | No inherited decision. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 18 · ACCEPTED | C-24.17.17 — Connection crash while creating a linked post-rejection proposal | New linked proposal crash truth. | Preserves rejection and exact new delta. | No two-vote counting. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 19 · ACCEPTED | C-24.17.18 — Connection crash during correction or dispute | Correction/dispute crash truth. | Appends backward links and new keys where required. | No old-key mutation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 20 · ACCEPTED | C-24.17.19 — Connection crash during accepted retrieval use | Accepted-retrieval crash truth. | Re-runs current-use resolution. | No stale context. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 21 · ACCEPTED | C-24.17.20 — Connection crash during pending investigation use | Investigation-use crash truth. | Keeps the proposal undecided. | No guidance promotion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 22 · ACCEPTED | C-24.17.21 — Connection crash during Person-Box consumption | Person-Box consumption truth. | Defers consequences to the identity owner. | No generic identity action. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |
| 23 · ACCEPTED | C-24.17.22 — Connection record and actual-owner contradiction | Owner contradiction truth. | Blocks in favor of actual owner records. | No coordination override. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: C-24.17.1 — Connection crash before proposal reservation; C-24.17.2 — Connection crash after identity reservation; C-24.17.3 — Connection crash after proposal commitment; C-24.17.4 — Connection crash during undecided waiting; C-24.17.5 — Connection crash after proposal display; C-24.17.6 — Connection crash after durable Ness input; C-24.17.7 — Connection crash after acceptance before checkpoint; C-24.17.8 — Connection unknown accepted-commit outcome; C-24.17.9 — Connection crash during source verification; C-24.17.10 — Connection crash after verified source before commit; C-24.17.11 — Connection crash during rule match; C-24.17.12 — Connection crash before final rule revalidation; C-24.17.13 — Connection crash after rule revalidation; C-24.17.14 — Connection crash during rejection; C-24.17.15 — Connection crash after rejection before suppression checkpoint; C-24.17.16 — Connection crash while adding pending new evidence; C-24.17.17 — Connection crash while creating a linked post-rejection proposal; C-24.17.18 — Connection crash during correction or dispute; C-24.17.19 — Connection crash during accepted retrieval use; C-24.17.20 — Connection crash during pending investigation use; C-24.17.21 — Connection crash during Person-Box consumption; C-24.17.22 — Connection record and actual-owner contradiction

### C-24.17.1 — Connection crash before proposal reservation
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 1, before proposal identity reservation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — Authoritative truth: nothing; no idempotency key or duplicate-prevention rule applies. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Recovers nothing and allows normal detection retry; no fresh Ness action is required. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — An operation-failed audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Recover a nonexistent proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — No proposal exists. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: preserves the empty pre-reservation outcome. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | Nothing durably reserved. | Re-detects normally. | No phantom proposal. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.17.2 — Connection crash after identity reservation
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 2, after reservation but before the proposal record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — Only the reserved proposed connection_proposal_id is authoritative and is the idempotency key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Reuses or abandons the ID; retry is permitted without fresh Ness action. The reserved ID cannot become a second proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — An operation-failed audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Treat a reservation as a durable proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — No proposal exists. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: preserves reserved-only truth. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | The reserved ID only. | Avoids duplicate proposal creation. | No proposal before record. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.17.3 — Connection crash after proposal commitment
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 3, after durable proposal commitment. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — The proposal record; duplicate key is proposed CRK plus proposal ID. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Recovers the proposal as undecided; no decision retry and no fresh Ness action. Canonical-key convergence prevents duplication. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A proposal-committed audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Auto-decide the recovered proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — The proposal waits. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: retains committed undecided truth. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | The durable proposal. | Recovers the existing undecided record. | No crash-generated decision. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.17.4 — Connection crash during undecided waiting
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 4, while an undecided proposal waits. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — The proposal, keyed by proposed CRK. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Preserves indefinite undecided status; no retry or fresh Ness action. No additional duplicate or audit event is specified for this idle boundary. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — The same waiting proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Age it into acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — It waits without force. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: keeps waiting unchanged. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | Existing waiting proposal. | Preserves its status through restart. | No time-based acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.17.5 — Connection crash after proposal display
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 5, after Ness sees a proposal but before deciding. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — Only the display event; identity is exact proposal ID plus version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Remains undecided and does not re-ask on restart. There is no decision retry; any later decision requires fresh Ness action bound to the then-current version. No additional duplicate rule applies. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A display-logged event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Treat seeing as consent or a now-stale display as authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — The decision stays undecided. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: preserves display without consent. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | A display event without decision. | Requires an actual later choice. | No inferred acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.17.6 — Connection crash after durable Ness input
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 6, after durable input but before atomic acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — Only the proposed durable Ness input, bound to exact proposal/version and authority context; key is proposed CRK plus proposal ID/version plus proposed authority_event_key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Revalidates all ten conditions before idempotent forward-completion. Any failure requires fresh Ness action; keeps old input as history, stale/superseded version marked or preserved and current version visible only through the output chain. Duplicate control remains inside the one canonical atomic commit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A forward-completion or fresh-decision-required audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Treat input as final decision, accepted record or authority event; silently rebind it. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — No acceptance and no silent rebinding. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-24.9.2.1 — Ness decision forward-completion gate: all ten conditions remain required. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: recovers a selected choice without assuming commitment. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | The durable input only. | Completes only a still-valid exact choice. | Fresh decision on failed conditions. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.17.7 — Connection crash after acceptance before checkpoint
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 7, after the atomic accepted commit but before the parent checkpoint. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — The complete commit: accepted record, proof and final accepted event where a proposal exists; key is accepted ID or proposed CRK plus proposed authority_event_key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Recovers every part together and completes the parent checkpoint idempotently. Retry is allowed, no fresh Ness action; the existing commit absorbs duplication. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A checkpoint-completed audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Recreate the record or manufacture missing authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — Partial or contradictory state remains blocked until operation ID and canonical key resolve it. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: completes bookkeeping around existing accepted truth. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | The complete atomic commit. | Recovers rather than recreates. | One accepted result. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.17.8 — Connection unknown accepted-commit outcome
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 8, where accepted-commit truth is unknown. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — Unknown result; duplicate identities are proposed CRK plus proposed authority_event_key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Before retry queries operation ID, canonical key, proposal ID/version, reserved accepted ID, authority-event key and final decision-event identity. Recovers a complete present commit; if absent reruns route checks, including all ten Ness conditions where applicable. Fresh Ness action is required only when a Ness condition fails. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — An uncertainty-recorded audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Blind-retry acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — Blocked until resolved; canonical and authority-event idempotency prevent duplicates. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-24.17 — Connection crash and restart recovery: lookup by every stated recovery identity precedes any retry. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: retains unknown truth until queried. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | Unknown commitment. | Queries exact identities first. | No blind duplicate acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.17.9 — Connection crash during source verification
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 9, during actual owner verification. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — Whatever the source owner committed; key is proposed report ID plus operation ID. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Re-asks the owner under technical B9 retries, with no fresh Ness action. verified_self_establishing enters atomic acceptance; verification_unavailable stays pending/blocked with no force; not_verified or contradiction is set aside, without a proposal or resurfacing. A report never recovers as a proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A verification-outcome audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Verify for the owner or invent successful verification on retry. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — No acceptance; a failed basis never waits as a proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: preserves the actual owner verification branch. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | Source-owner committed truth. | Requeries the actual owner. | No report/proposal collapse. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.17.10 — Connection crash after verified source before commit
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 10, after verified_self_establishing but before acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — The owner verification only; key is proposed CRK plus proposed authority_event_key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Revalidates owner, owner version, evidence refs, verification result, privacy, key/duplicate state and authority identity immediately before one atomic source commitment. Retry is allowed without fresh Ness action; both keys absorb duplication. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A direct-source authority-event audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Treat verification alone as commitment. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — Before the commit no accepted connection exists. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-24.9.1 — Atomic direct-source commitment: complete direct-route final revalidation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: resumes verified source work without premature acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | Owner verification. | Commits record and proof once after revalidation. | No accepted record before atomic truth. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.17.11 — Connection crash during rule match
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 11, during an authorized-rule match. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — The rule own state; key is operation ID. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Re-matches from the current rule version. Retry is allowed, with no fresh Ness action and no additional duplicate rule specified. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A rule-match-failed audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Reuse obsolete rule state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — No acceptance from the interrupted match. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: restarts matching from actual current authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | Current rule state. | Re-matches the current version. | No cached rule authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.17.12 — Connection crash before final rule revalidation
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 12, after rule matching but before final revalidation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — The match record; key is operation ID. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Revalidates activation, revocation, supersession and scope. Retry is allowed without fresh Ness action; no additional duplicate rule is specified. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A rule-revalidation audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Treat the match record as current permission. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — Revoked or superseded rules produce no acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: preserves final rule validation as necessary. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | The prior match. | Checks current rule validity again. | No stale acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.17.13 — Connection crash after rule revalidation
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 13, after revalidation but before commit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — The revalidation result; key is proposed CRK plus proposed authority_event_key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Commits accepted record, rule-authority proof, exact rule ID/version and Ness authorization together once. Any doubt repeats revalidation, including privacy and duplicate state. Retry is allowed with no fresh Ness action; both stable keys prevent duplicates. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A rule-authority-event audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Let doubt or a changed rule bypass revalidation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — No acceptance until the valid atomic commit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-24.9.3 — Atomic authorized-rule commitment: the complete final rule route. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: resumes only a current rule-authorized commit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | Rule revalidation truth. | Rechecks doubt and commits once. | No detached rule proof. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.17.14 — Connection crash during rejection
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 14, during rejection commitment. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — The decision event if durable; key is proposal ID plus version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Completes rejection and suppression idempotently where committed. Retry is allowed without fresh Ness action; no additional duplicate rule applies. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A rejection audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Treat an uncommitted input as a final rejection. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — If nothing committed the proposal remains undecided. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: recovers the actual rejection truth. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | Durable rejection if present. | Completes the actual committed decision. | Undecided when nothing committed. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.17.15 — Connection crash after rejection before suppression checkpoint
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 15, after rejection but before suppression checkpoint. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — The rejection; key is proposed CRK. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Keeps rejected status and registers suppression idempotently. Retry is allowed without fresh Ness action; no additional duplicate rule or failure outcome is specified. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A suppression-registered audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Reopen rejection because suppression bookkeeping was interrupted. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: restores suppression around existing rejection. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | The durable rejected outcome. | Completes suppression once. | No reopened decision. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.17.16 — Connection crash while adding pending new evidence
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 16, while appending genuinely new evidence to a pending proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — The committed proposal version; key is proposal ID plus version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Creates a new append-only version, with the version chain preventing duplicates. Retry is allowed; any decision on the new version needs fresh Ness action. Certainty is not raised by the append. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — An evidence-appended audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Edit in place or let the new version inherit earlier Ness input. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — Unverified evidence is not appended. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: preserves new-version boundaries. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | The committed proposal version. | Appends only verified new evidence as a successor version. | No inherited decision. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.17.17 — Connection crash while creating a linked post-rejection proposal
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 17, during creation of a new proposal linked to rejection. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — The old rejection; key is proposed CRK plus new proposal ID. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Keeps rejection and creates the new proposal once with exact delta and backlink. Retry is allowed without fresh Ness action; canonical key and suppression registry prevent duplication. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A new-linked-proposal audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Count old and new proposals as two votes. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — No verified genuine delta means no new proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: preserves rejection through valid new proposal creation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | The rejected predecessor. | Creates only the justified linked successor. | No repetition disguised as evidence. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.17.18 — Connection crash during correction or dispute
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 18, during a correction/dispute append. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — Whatever actually committed; key is correction ID. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Appends the later event, pointing back to unchanged old history. Geometry/type/direction/type-version changes create a new record/proposal version, new key and links to both. Retry is allowed, no fresh Ness action; the old canonical key is never mutated. No additional failure outcome is specified. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A correction/dispute audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Edit earlier records or their commit-time link lists. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: preserves append-only correction recovery. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | Committed correction truth. | Appends or recovers the event idempotently. | Immutable earlier history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.17.19 — Connection crash during accepted retrieval use
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 19, while Context Retrieval uses an accepted relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — The retrieval own committed state; key is retrieval operation ID. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Re-retrieves under current authorization and a fresh current-use resolution; the connection itself does not change. Retry is allowed without fresh Ness action; no additional duplicate rule applies. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A use-event audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Use a stale accepted version because it still exists. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — Use fails closed and leaves the connection untouched; an unresolved or contradictory chain gives no use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-24.14 — Connection current-use resolution: fresh complete current-use resolution. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: resumes retrieval without altering connection truth. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | Retrieval committed truth. | Repeats only an authorized current use. | No stale context. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.17.20 — Connection crash during pending investigation use
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 20, while a pending proposal guides retrieval. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — The proposal, still undecided; key is retrieval operation ID. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Re-runs under current authorization without advancing the proposal. Retry is allowed without fresh Ness action; no additional duplicate rule applies. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — An investigation-use audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Treat guidance as evidence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — The failed use creates no proposal or acceptance; the existing proposal remains unchanged. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: preserves investigative scope through recovery. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | The still-undecided proposal. | Repeats only the bounded investigation. | No promotion from recovery. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.17.21 — Connection crash during Person-Box consumption
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 21, while Person-Boxes consume an accepted connection. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — The Person-Box owner committed state; key is its own operation ID. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Leaves identity decisions with that owner and repeats the handoff only after fresh current-use resolution and route-level privacy. Retry is allowed without fresh Ness action; no additional duplicate rule applies. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A Person-Box-handoff audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Create a link, anchor, merge or join in the proposed connection recordkeeper. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — No identity consequence from unresolved handoff. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-24.15 — Connection Person-Box handoff: the current authorized identity handoff boundary. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: preserves the identity owner committed truth. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | Person-Box owner truth. | Repeats only the valid handoff. | No connection-side identity action. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.17.22 — Connection record and actual-owner contradiction
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Crash boundary 22, contradiction between the proposed recordkeeper and actual source, authority or Person-Box owner. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — The actual owner record is authoritative, always; no idempotency key or extra duplicate rule is specified. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — Records the contradiction, blocks and surfaces uncertainty honestly. No retry; fresh Ness action may be required only as the actual owner decides. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A contradiction-recorded audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Resolve the contradiction in favor of the proposed recordkeeper. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — Blocked. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.17 — Connection crash and restart recovery: preserves owner precedence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.17 — Connection crash and restart recovery | The owner contradiction. | Stops with honest uncertainty. | No coordination override. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-24.18 — Connection technical retry boundary
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §17]

ALONE
- What it is: ACCEPTED — The bounded technical retry policy consuming accepted B9 classifications and values. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §17]
- Takes in: ACCEPTED — A real technical failure and the same stable operation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §17]
- Does: ACCEPTED — Retries only where no authority or decision is recreated. Recovers existing authority events or absorbs duplicates; new Ness decisions require fresh action and rejected relationships require genuine new evidence plus a new linked proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §17]
- Gives out: ACCEPTED — An idempotent technical continuation or no automatic retry. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §17]
- Must never: ACCEPTED — Automatically retry a Ness decision request, undecided proposal, rejected proposal, invalid/revoked rule, failed source verification as success, semantic/model judgment to manufacture a basis, stale acceptance, failed forward-completion or an authority append whose proposed key already exists. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §17]
- Fails closed by: ACCEPTED — A forbidden automatic retry does not execute; missing authority is not reconstructed. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §17]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7H.9 — B9 retry-state architecture: accepted technical retry admission and classifications; C-7H.10 — Accepted B9 retry values and episodes: accepted retry values, without inventing new counts, gaps, timeouts or backoff. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §17]
- Changes: DESIGNED — C-24 — Connection Capability (§24): permits technical recovery without creating authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §17]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | Bounded technical retries. | Reuses actual operation identity without repeating decisions. | No retry-made acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §17] |
| 2 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual permitted technical retry. | Records the retry child. | No retry-derived authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-24.19 — Connection interface contracts
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — The eleven connection boundaries, each preserving its own authority, identities, authorization and recovery truth. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — The per-boundary requests, responses, stable operation/idempotency identities, prerequisites, precommit checks, committed success/failure, retry/crash behavior and audit identities. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Keeps explicit not-applicable cells distinct from omissions; preserves privacy classification/authorization, access reference and current-use requirements on every boundary. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — The exact boundary result under its actual owner. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Exercise an interface without required committed truth or recovery identity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — Missing required truth, identity or authorization stops the boundary. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

TOGETHER
- Fed by: ACCEPTED — C-24.19.1 — Connection I1 direct-source interface: I1 source; C-24.19.2 — Connection I2 candidate-report interface: I2 report; C-24.19.3 — Connection I3 source-verification interface: I3 verification; C-24.19.4 — Connection I4 Ness-decision interface: I4 Ness; C-24.19.5 — Connection I5 authorized-rule interface: I5 rule; C-24.19.6 — Connection I6 investigation-guidance interface: I6 investigation; C-24.19.7 — Connection I7 accepted-use interface: I7 accepted use; C-24.19.8 — Connection I8 Person-Box interface: I8 identity; C-24.19.9 — Connection I9 correction-dispute interface: I9 correction; C-24.19.10 — Connection I10 visible-output interface: I10 output; C-24.19.11 — Connection I11 operational-record interface: I11 logs. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24 — Connection Capability (§24): keeps each authority boundary explicit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | The complete interface results. | Retains exact owner and recovery contracts. | No authority duplication. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 2 · ACCEPTED | C-24.19.1 — Connection I1 direct-source interface | The I1 boundary contract. | Preserves source-owner authority and atomic truth. | Direct-source acceptance or refusal. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 3 · ACCEPTED | C-24.19.2 — Connection I2 candidate-report interface | The I2 boundary contract. | Preserves a separate retrieval report. | No automatic proposal. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 4 · ACCEPTED | C-24.19.3 — Connection I3 source-verification interface | The I3 boundary contract. | Preserves three actual verification outcomes. | No substitute verification. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 5 · ACCEPTED | C-24.19.4 — Connection I4 Ness-decision interface | The I4 boundary contract. | Preserves exact Ness choice and recovery. | No stale acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 6 · ACCEPTED | C-24.19.5 — Connection I5 authorized-rule interface | The I5 boundary contract. | Preserves current narrow-rule authority. | No new rule creation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 7 · ACCEPTED | C-24.19.6 — Connection I6 investigation-guidance interface | The I6 boundary contract. | Preserves investigation-only scope. | No evidentiary promotion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 8 · ACCEPTED | C-24.19.7 — Connection I7 accepted-use interface | The I7 boundary contract. | Requires current resolved accepted context. | No stale use. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 9 · ACCEPTED | C-24.19.8 — Connection I8 Person-Box interface | The I8 boundary contract. | Retains Person-Box authority. | No generic identity proof. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 10 · ACCEPTED | C-24.19.9 — Connection I9 correction-dispute interface | The I9 boundary contract. | Preserves append-only correction truth. | No old-record mutation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 11 · ACCEPTED | C-24.19.10 — Connection I10 visible-output interface | The I10 boundary contract. | Retains output owners and stable identities. | No disclosure bypass. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 12 · ACCEPTED | C-24.19.11 — Connection I11 operational-record interface | The I11 boundary contract. | Preserves required durable operation records. | No silent success. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: C-24.19.1 — Connection I1 direct-source interface; C-24.19.2 — Connection I2 candidate-report interface; C-24.19.3 — Connection I3 source-verification interface; C-24.19.4 — Connection I4 Ness-decision interface; C-24.19.5 — Connection I5 authorized-rule interface; C-24.19.6 — Connection I6 investigation-guidance interface; C-24.19.7 — Connection I7 accepted-use interface; C-24.19.8 — Connection I8 Person-Box interface; C-24.19.9 — Connection I9 correction-dispute interface; C-24.19.10 — Connection I10 visible-output interface; C-24.19.11 — Connection I11 operational-record interface

### C-24.19.1 — Connection I1 direct-source interface
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — I1: source/provenance owner calls the proposed recordkeeper; that source owner alone owns verification. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — Immutable endpoint refs, type/direction/type version, immutable direct evidence, owner verification and owner ID/version; proposed connection_operation_id; duplicate key proposed CRK plus proposed authority_event_key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Requires deterministic verified_self_establishing by the owner. Immediately revalidates exact owner/version, evidence, result, route privacy, key/duplicate state and authority identity. Uses technical B9 retries idempotently; crash recovery covers unknown commit, interrupted verification and verified-before-commit cases. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — Response: proposed accepted_connection_id or refused. Success: one accepted record plus proposed direct_source_relationship authority event and canonical compare-and-commit result. Audit: direct-source authority event and operation children. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Let retrieval, a model or the proposed recordkeeper verify. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — Failure truth: no accepted record and no authority event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): references-only classification with endpoint privacy carried; route-level precommit authorization. Access-factor reference is not applicable to this machine route; source-owner authority applies without inventing a Ness factor. Current-use check is not applicable at creation, but mandatory for every later use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Changes: ACCEPTED — C-24.19 — Connection interface contracts: supplies the exact owner-verified creation boundary. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.19 — Connection interface contracts | I1 committed result. | Preserves deterministic source authority. | Atomic source acceptance or refusal. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-24.19.2 — Connection I2 candidate-report interface
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — I2: Context Retrieval submits to the proposed recordkeeper; no acceptance authority exists at this boundary and verification belongs to the actual source owner. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — Exact immutable source refs, how encountered, endpoint refs and apparent type/direction; proposed connection_operation_id; duplicate key proposed candidate-report ID plus proposed CRK. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Requires exact immutable references and internal-use permission before submission. Pre-acceptance revalidation is not applicable because neither a proposal nor accepted record commits here. Retries follow B9 idempotently on report identity; interrupted verification follows the report recovery branch. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — Response: proposed connection_candidate_report_id, never a proposal ID. Success: durable report in submitted state. Audit: candidate detection. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Accept or automatically create a proposal through report submission. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — Failure truth: refused with no report, proposal or acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

TOGETHER
- Fed by: DESIGNED — C-7F — Context Retrieval (§7F): the caller supplies encountered source references. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): references-only classification; internal-use authorization before submission. Identity/access factor and accepted-current-use resolution are not applicable here. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Changes: ACCEPTED — C-24.19 — Connection interface contracts: supplies the separate reporting boundary. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.19 — Connection interface contracts | I2 report outcome. | Keeps the report separate from lasting commitment. | No acceptance authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-24.19.3 — Connection I3 source-verification interface
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — I3: the proposed recordkeeper requests verification from the actual source/provenance owner, which retains decision authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — Proposed report ID, endpoint refs, claimed direct relationship and immutable evidence; operation ID; duplicate key report ID plus owner plus owner version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Requires exact immutable refs. Recordkeeper precommit checks are not applicable: the actual owner verifies. Technical B9 retries never invent success; recovery re-asks that owner. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — Exactly verified_self_establishing, verification_unavailable or not_verified. Success truth is the durable owner result bound to the report: verified enters atomic acceptance; unavailable stays pending/blocked with no force and only explicitly unverified investigative exposure; failed/contradictory is set aside without proposal or resurfacing. Audit: verification outcome. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Convert failure into uncertainty evidence or verify for the owner. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — No owner result leaves the report unchanged and without force. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): references-only classification and internal-use authorization. Access-factor reference and accepted-current-use resolution are not applicable. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Changes: ACCEPTED — C-24.19 — Connection interface contracts: supplies actual three-way owner verification. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.19 — Connection interface contracts | I3 actual verification result. | Preserves all three branches distinctly. | No fabricated successful basis. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-24.19.4 — Connection I4 Ness-decision interface
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — I4: the Ness decision surface, delivered through the accepted output chain, calls the proposed recordkeeper; Ness owns the choice and accepted identity/access owners own its authority context. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — Proposal ID/version, endpoints, type/direction, displayed certainty, surface version/integrity, explicit durable input and authority context; operation ID plus proposed ness_decision_input identity; key proposal ID/version and, for acceptance, proposed CRK plus proposed authority_event_key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Requires the exact current decision-eligible version and explicit choice. Immediately verifies proposal/version, endpoints/type/direction, display certainty/surface/integrity, input, current authority/privacy, duplicate state and absence of conflicting decision/correction/rejection/supersession. Forward-completion alone may retry under all ten conditions; the decision request never auto-retries. Recovery covers display, durable input, complete/unknown acceptance and new evidence versions. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — Response accepted, rejected or refused-stale, with current version surfaced only through the output chain. Success is the complete atomic accepted result or durable rejection plus suppression. Audits separately identify durable input, final decision, authority, completion or fresh-decision requirement. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Invent an identity factor or treat silence as consent. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — Stale, conflicting or blocked input gives no acceptance; preserves input as history and requires a fresh decision on the current version. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): current accepted identity/access authority; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): route-level precommit privacy, with visible-surface privacy first; C-SACL — Speaker Access-Control Layer (§25.4): surface access second, with current fence revalidated. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gated by: ACCEPTED — C-24.9.2.1 — Ness decision forward-completion gate: all ten completion conditions, including correction-caused staleness. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B]
- Changes: ACCEPTED — C-24.19 — Connection interface contracts: preserves exact-choice authority and recovery. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.19 — Connection interface contracts | I4 exact decision outcome. | Keeps input, final choice and authority separate. | No stale acceptance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-24.19.5 — Connection I5 authorized-rule interface
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — I5: the actual permission/rule owner calls the proposed recordkeeper; rule validity remains with that owner and force traces to Ness explicit prior authorization. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — Rule ID/version, Ness authorization, scope, endpoint/connection types, source conditions, activation, revocation/supersession and exact applicability; operation ID; key proposed CRK plus proposed authority_event_key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Requires an already-existing rule and exact match on every item. Immediately revalidates owner/version, activation/invalidation, all scope/type/source/applicability facts, privacy, duplicate state and authority-event identity. B9 retry is idempotent and any doubt revalidates again; recovery covers unknown commit and all three rule interruption stages. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — Response applicable or not_applicable. Success truth is the complete atomic accepted record, rule authority event, exact rule ID/version, Ness authorization and key result. Audits: rule match, final revalidation and rule-authority event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Create or widen a rule or accept broad permission as exact match. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — No acceptance on invalid or nonmatching authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

TOGETHER
- Fed by: DESIGNED — C-7P — Permission & Authority Boundaries (§7P): actual rule owner and Ness-authorization provenance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): references-only classification and route-level final authorization. Access reference is the rule Ness-authorization provenance; current-use resolution is not applicable at creation but required on later use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Changes: ACCEPTED — C-24.19 — Connection interface contracts: supplies the existing-rule boundary. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.19 — Connection interface contracts | I5 exact applicability and commit. | Retains current rule ownership. | No new rule authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-24.19.6 — Connection I6 investigation-guidance interface
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — I6: Context Retrieval queries the proposed recordkeeper waiting-area read surface; retrieval owns the investigation under privacy and never advances the proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — Proposal ID/version, endpoints, type, certainty and explicit proposed investigation_only_pending_connection marker; retrieval operation ID is both operation and idempotency identity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Requires internal-use authorization and the marker. Unavailable report material enters only explicitly unverified, investigation-only and separated; set-aside reports never enter. Precommit revalidation is not applicable because this boundary accepts nothing. B9 retries use current permission; recovery retains the still-undecided proposal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — Response: search/compare results separated from evidence. Success truth: an investigation-use audit and unchanged undecided proposal. Audit identity: investigation use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Let guidance accept a relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — No results on failure; proposal unchanged. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

TOGETHER
- Fed by: DESIGNED — C-7F — Context Retrieval (§7F): owns the actual retrieval investigation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): internal-use classification and authorization before use. Access-factor reference is not applicable; accepted-current-use resolution is not applicable to pending material. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Changes: ACCEPTED — C-24.19 — Connection interface contracts: preserves guidance without evidence force. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.19 — Connection interface contracts | I6 investigation outcome. | Keeps returned results separated. | No proposal advancement. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-24.19.7 — Connection I7 accepted-use interface
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — I7: Context Retrieval through LMAC requests accepted records; retrieval owns the operation, relevance configuration and failure behavior retain their accepted owners. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — Accepted ID/version and purpose; retrieval operation ID is both operation identity and idempotency key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Requires current internal-use permission and complete current-use resolution for the currently applicable version. Performs fresh resolution and privacy checks per use. Re-retrieval requires those fresh checks; crash recovery follows retrieval own committed truth. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — Context marked accepted, with type, certainty, basis, evidence, resolved state/chain and uncertainty limits. Success truth: a proposed connection_use_event carrying the complete current-use fields. Audit identity: use event. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Override or repair positional context, widen access, harden certainty or prove identity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — Unresolved, contradictory or unavailable history, or supersession without validated replacement, gives no use. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

TOGETHER
- Fed by: DESIGNED — C-7F — Context Retrieval (§7F): retrieval owner; C-LMAC — Live Mechanism Access Coordinator (§26): stateless route; C-7R — Attention & Relevance Control (§7R): accepted purpose/relevance configuration. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): references-only internal-use classification and permission before use and within resolution; access-factor reference is not applicable. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gated by: ACCEPTED — C-24.14 — Connection current-use resolution: mandatory fresh correction/dispute resolution; dispute travels with use and material uncertainty reaches the output chain. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Changes: ACCEPTED — C-24.19 — Connection interface contracts: supplies bounded accepted context. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.19 — Connection interface contracts | I7 authorized resolved context. | Uses the current exact relationship only. | No stale accepted shortcut. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 2 · ACCEPTED | C-LMAC.14.1 — Fresh accepted-connection use through retrieval | Exact connection identity/version, current purpose/scope and a fresh completed current-use resolution. | Supplies accepted-connection use interface. | Nothing in this card. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-24.19.8 — Connection I8 Person-Box interface
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — I8: the proposed recordkeeper calls Person-Boxes, whose own identity authority always decides. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — Currently applicable relationship/version, endpoints, type, certainty, basis, source/evidence, privacy/access and resolved state/chain; identity and idempotency are accepted-connection ID plus the Person-Box operation ID. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Requires complete current-use resolution and route-level privacy for the handoff. Repeats only after both fresh checks. Recovery follows the Person-Box own committed state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — Response: the Person-Box owner decision. Success truth: that owner committed state, consuming the generic connection as one provenance-bearing reference. Audit: Person-Box handoff. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Prove endpoint identity or create any link, anchor, merge or join from generic acceptance. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — Failure truth: no identity consequence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

TOGETHER
- Fed by: ACCEPTED — C-7L.12 — Person-Box generic-connection use boundary: existing identity rules and ten-rule generic-use boundary, including its own clear/unclear test. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): references-only internal-use classification and authorization before handoff; identity/access retains the accepted Person-Box rules. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gated by: ACCEPTED — C-24.14 — Connection current-use resolution: fresh mandatory correction/dispute resolution before handoff or repetition. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C]
- Changes: ACCEPTED — C-24.19 — Connection interface contracts: preserves Person-Box ownership of consequences. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.19 — Connection interface contracts | I8 owner decision. | Keeps generic provenance distinct from identity proof. | No connection-owned merge. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-24.19.9 — Connection I9 correction-dispute interface
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — I9: Ness, an owner or an authorized correcting source calls the proposed recordkeeper; the correcting source retains authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — Exact target ID/version, content refs, basis, owner/authority refs and integrity; operation ID; idempotency key correction ID. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Requires exact target identity/version and current internal-use permission. Immediately revalidates target existence and route privacy. Appends a backward-pointing event; geometry/type/direction/type-version changes create a new version/key with links to both records. Retry is idempotent by correction ID; recovery preserves append-only history. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — Response: proposed correction_event_id. Success truth: the immutable back-linked event. Audit: correction/dispute. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Edit old links or mutate the old canonical key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — No correction event on failure; earlier record untouched. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): references-only classification and route-level precommit authorization. Access reference is the correcting source authority. The new event enters every subsequent current-use resolution and controls use without rewriting history. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Changes: ACCEPTED — C-24.19 — Connection interface contracts: supplies the append-only correction boundary. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.19 — Connection interface contracts | I9 committed correction. | Makes later information binding through new records. | No historical rewrite. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-24.19.10 — Connection I10 visible-output interface
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — I10: the proposed recordkeeper calls the accepted output chain; privacy, access and identity/fence owners retain every decision. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — Visible proposal/decision/status/uncertainty content refs and resolved current-use state where material; stable proposed output_operation_id, separate stable proposed delivery_idempotency_key from request plus destination, and proposed delivery_attempt_id per actual attempt. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Requires privacy first, SACL second, then current identity/fence/owner-version revalidation; revalidates those owners immediately before writing. Consumes the output owner retry and crash lifecycle rather than defining another. Mutable epoch, generation, privacy, SACL, PBR, observability and fence facts attach to attempts, never the stable key. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — Response delivered or withheld. Success truth: the output owner delivery record. Audit: visible-output child. The connection itself does not change. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Replace output/delivery identities with the connection operation; put epoch, generation, privacy, SACL, PBR, observability, owner or fence versions into the stable key; create new output retry or duplicate rules. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — Withheld output gives no indirect disclosure or signal that hidden material exists. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

TOGETHER
- Fed by: ACCEPTED — C-24.16.1 — Proposed connection-output output_operation_id reference: proposed output parent; C-24.16.2 — Proposed connection-output delivery_idempotency_key reference: proposed delivery key; C-24.16.3 — Proposed connection-output delivery_attempt_id reference: proposed attempt reference. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): visible-output classification and first privacy factor; C-SACL — Speaker Access-Control Layer (§25.4): second access factor; C-9 — Access/authentication model + voice I/O + phone modes (§9): revalidated fence and owner facts. Materially affected disputed current-use status must surface its uncertainty through this chain. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Changes: ACCEPTED — C-24.19 — Connection interface contracts: supplies authorized output without new delivery authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.19 — Connection interface contracts | I10 delivered/withheld result. | Retains the accepted output owners and identities. | No connection-side delivery bypass. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-24.19.11 — Connection I11 operational-record interface
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — I11: the proposed recordkeeper calls the operational-record system under the full-transparency law. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — One parent log per real operation and required children; identity is the parent operation ID, with one parent per real operation and stable child identities as duplicate scope. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Requires a real operation and forbids silent internal work. Precommit revalidation is not applicable here. Appends idempotently; duplicates are absorbed without support. Recovery uses actual operation identities and does not read logs as truth evidence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — Response durable append. Success truth: one append-only parent and its children. The audit identity is the event itself, with no recursive log-about-logging. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Make current-use logs increase certainty or currentness. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — If a required audit event cannot commit, the operation fails closed. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

TOGETHER
- Fed by: DESIGNED — C-7B.10.5 — Real-operation and evidence boundaries: one-real-operation logging law; C-7B.10.8 — Operational-record access boundary: normal log access. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): log access classification and authorization; C-9 — Access/authentication model + voice I/O + phone modes (§9): identity/access and compartment restrictions. Current-use logs record outcomes without becoming authority. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]
- Changes: ACCEPTED — C-24.19 — Connection interface contracts: preserves complete operational accountability. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.19 — Connection interface contracts | I11 durable operational records. | Keeps complete audit without extra evidence. | No silent operation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-24.20 — Connection operational recordkeeping
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — One parent operational log per real connection operation, with twenty-eight named child kinds. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Takes in: ACCEPTED — Candidate report; source verification; verification unavailable; not verified/evaluated and set aside; proposal creation; duplicate absorption; waiting; durable Ness decision input; final proposal-decision event; authority event; atomic accepted commit; direct-source commitment; rejection; rejection suppression; rule matching; final rule revalidation; new-evidence evaluation; current-use resolution; correction/dispute chain lookup; non-use due to dispute or staleness; retrieval investigation use; retrieval accepted-connection use; Person-Box handoff; correction; dispute; failure; retry; recovery. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Does: ACCEPTED — Records accepted, rejected, undecided, used and not-used outcomes. Records evaluated/set-aside candidates without inventing proposals. Keeps records append-only, with active/cold behavior under the existing operational-log law. Cold reactivation requires actual use or a valid new link. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Gives out: ACCEPTED — One parent and the real operation children, including proposed record identities already defined. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Must never: ACCEPTED — Recurse into log-about-logging, add evidence weight or certainty/currentness, count repeated logs as confirmation, reactivate from similarity, grant endpoint access or bypass influence removal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Fails closed by: ACCEPTED — A required uncommitted audit event prevents operation completion. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-24.20.1 — Connection operational child-kind placement: child-kind placement; C-24.12.9 — Proposed connection_operation: proposed parent operation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Gated by: DESIGNED — C-7B.10.5 — Real-operation and evidence boundaries: one parent per real operation; C-7B.10.8 — Operational-record access boundary: ordinary authorized log access; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy and influence removal; C-9 — Access/authentication model + voice I/O + phone modes (§9): access/compartment rules. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Changes: DESIGNED — C-24 — Connection Capability (§24): preserves observable operation history without extra support. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | Operational history. | Keeps every actual outcome and use inspectable. | No log-derived truth. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |
| 2 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | The twenty-eight child kinds. | Maps each kind to its actual operation. | No fabricated log evidence. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: C-24.20.1 — Connection operational child-kind placement

### C-24.20.1 — Connection operational child-kind placement
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — The association of each named operational child with its actual fact or operation. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Takes in: ACCEPTED — The actual occurrence of one of the twenty-eight child kinds. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Does: ACCEPTED — Records each child under the same real parent; the child is evidence of its operation only, never another vote for the relationship. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Gives out: ACCEPTED — Stable child events for actual occurrences. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Must never: ACCEPTED — Duplicate authority proofs as new support or create proposals to log failed candidates. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-24.12.2 — Proposed connection_candidate_report: candidate report; C-24.4.1.1 — Connection source-owner verification: source verification; C-24.4.1.3 — Verification-unavailable relationship outcome: verification unavailable; C-24.4.1.4 — Not-verified relationship outcome: not verified/evaluated and set aside; C-24.13.1.6 — Connection proposal_committed state: proposal creation; C-24.12.8 — Proposed connection_duplicate_absorbed: duplicate absorption; C-24.13.1.7 — Connection waiting_undecided state: waiting; C-24.12.3 — Proposed ness_decision_input: durable Ness decision input; C-24.12.4 — Proposed connection_decision_event: final proposal-decision event; C-24.12.5 — Proposed connection_authority_event: authority event; C-24.13.1.12 — Connection accepted_commit state: atomic accepted commit; C-24.9.1 — Atomic direct-source commitment: direct-source commitment; C-24.9.4 — Connection rejection commitment: rejection; C-24.11.1 — Proposed connection_rejection_suppression_registry: rejection suppression; C-24.4.3 — Existing authorized connection-rule route: rule matching; C-24.9.3 — Atomic authorized-rule commitment: final rule revalidation; C-24.3.1.4 — Proposed connection new-evidence delta reference: new-evidence evaluation; C-24.14 — Connection current-use resolution: current-use resolution; C-24.14.1.2 — Current-use complete later-event chain: correction/dispute chain lookup; C-24.12.7.9 — Proposed connection-use non-use and reason: non-use due to dispute or staleness; C-24.2.2 — Pending-connection investigation route: investigation use; C-24.2.1 — Accepted-connection retrieval route: accepted-connection use; C-24.15 — Connection Person-Box handoff: Person-Box handoff; C-24.12.6 — Proposed connection_correction_event: correction and dispute as separate actual child kinds; C-24.21 — Connection fail-closed outcomes: failure; C-24.18 — Connection technical retry boundary: retry; C-24.12.10 — Proposed connection_recovery_event: recovery. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.20 — Connection operational recordkeeping: supplies the complete child-kind inventory. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.20 — Connection operational recordkeeping | Actual named child events. | Keeps the complete event vocabulary tied to real operations. | No invented or weighted event. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-24.21 — Connection fail-closed outcomes
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — The protective outcome for every named connection authority, integrity or use failure. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Takes in: ACCEPTED — No approved/verifiable basis; stale/superseded proposal; conflicting decision/rejection/correction/supersession; stale input or failed completion condition; missing/contradictory endpoint; invalid type/direction; missing source label; missing/invalid certainty; unverifiable Ness authority; missing/revoked/superseded/out-of-scope rule; changed owner/rule/source version; unavailable/contradictory source; not_verified result; report/proposal confusion; unresolved/contradictory/unavailable chain; stale accepted-use request; unbound proof; unknown authority-event or accepted-commit result; final privacy/access failure; unavailable store/owner; guidance/evidence confusion; generic-connection identity proof; owner contradiction; missing interface truth/recovery identity; uncommittable audit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Does: ACCEPTED — Preserves history and certainty while stopping the dependent commitment or use; retains actual owner truth. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Gives out: ACCEPTED — A recorded failure or non-use with honest uncertainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Must never: ACCEPTED — Create lasting acceptance, give pending force, use stale relationships, link/merge a person, strengthen factual claims, support a recommendation/external action or disclose hidden material through failure. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Fails closed by: ACCEPTED — No dependent acceptance, stale use, identity consequence, recommendation/action support or hidden disclosure proceeds. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

TOGETHER
- Fed by: ACCEPTED — C-24.21.1 — Invalid connection record contract failure: invalid relationship contract; C-24.21.2 — Unavailable connection store or source owner failure: unavailable record/source owner; C-24.21.3 — Missing connection interface truth or recovery identity failure: missing interface truth/identity; C-24.21.4 — Connection required-audit commitment failure: required audit failure. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-24 — Connection Capability (§24): prevents unsafe commitment and influence. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | The protective failure result. | Preserves uncertainty without force. | No manufactured relationship. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20] |
| 2 · ACCEPTED | C-24.20.1 — Connection operational child-kind placement | Actual operation failure. | Records the failure child. | No silent unsafe result. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |
| 3 · ACCEPTED | C-24.21.1 — Invalid connection record contract failure | Invalid record-contract facts. | Stops rather than fills gaps. | No fabricated completeness. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20] |
| 4 · ACCEPTED | C-24.21.2 — Unavailable connection store or source owner failure | Unavailable owner/store facts. | Preserves uncertainty pending real recovery. | No invented verification. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20] |
| 5 · ACCEPTED | C-24.21.3 — Missing connection interface truth or recovery identity failure | Missing boundary truth or identity. | Blocks the dependent interface. | No assumed commitment. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20] |
| 6 · ACCEPTED | C-24.21.4 — Connection required-audit commitment failure | Uncommittable required audit. | Prevents successful completion. | No silent operation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20] |

SUB-PARTS: C-24.21.1 — Invalid connection record contract failure; C-24.21.2 — Unavailable connection store or source owner failure; C-24.21.3 — Missing connection interface truth or recovery identity failure; C-24.21.4 — Connection required-audit commitment failure

### C-24.21.1 — Invalid connection record contract failure
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — Failure from missing/contradictory endpoint identity, invalid type/direction, missing source label or missing/invalid certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Takes in: ACCEPTED — The incomplete or invalid relationship contract. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Does: ACCEPTED — Rejects the dependent relationship operation rather than filling in the missing fact. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Gives out: ACCEPTED — A recorded invalid-contract failure. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Must never: ACCEPTED — Infer missing identity, source classification or certainty. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Fails closed by: ACCEPTED — No lasting record, claim strengthening or identity consequence proceeds. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.21 — Connection fail-closed outcomes: supplies the invalid-contract failure class. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.21 — Connection fail-closed outcomes | Invalid record facts. | Stops instead of inventing fields. | No fabricated completeness. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20] |

SUB-PARTS: NONE

### C-24.21.2 — Unavailable connection store or source owner failure
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — Failure where the connection store or actual source owner is unavailable. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Takes in: ACCEPTED — An unavailable dependency. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Does: ACCEPTED — Preserves uncertainty and current committed history until the applicable technical recovery resolves the dependency. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Gives out: ACCEPTED — An availability failure record. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Must never: ACCEPTED — Treat unavailable facts as successful verification. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Fails closed by: ACCEPTED — No dependent acceptance or use occurs. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.21 — Connection fail-closed outcomes: supplies the unavailable-dependency failure. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.21 — Connection fail-closed outcomes | Unavailable owner or store. | Preserves actual truth without reconstruction. | No fabricated success. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20] |

SUB-PARTS: NONE

### C-24.21.3 — Missing connection interface truth or recovery identity failure
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — Failure from exercising a boundary without its required committed truth or stable recovery identity. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Takes in: ACCEPTED — The incomplete boundary contract. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Does: ACCEPTED — Blocks the interface until actual records and identities establish its state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Gives out: ACCEPTED — A recorded interface failure. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Must never: ACCEPTED — Guess a committed result from coordination progress. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Fails closed by: ACCEPTED — No downstream effect is authorized. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.21 — Connection fail-closed outcomes: supplies the interface-contract failure. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.21 — Connection fail-closed outcomes | Missing truth or identity. | Stops an unrecoverable boundary action. | No assumed commitment. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20] |

SUB-PARTS: NONE

### C-24.21.4 — Connection required-audit commitment failure
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — Failure where a required operational audit event cannot commit. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Takes in: ACCEPTED — The failed required audit append. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Does: ACCEPTED — Keeps the operation failed closed instead of declaring silent success. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Gives out: ACCEPTED — The operation failure state. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Must never: ACCEPTED — Complete a required-audit operation silently. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]
- Fails closed by: ACCEPTED — The operation does not complete successfully. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-24.21 — Connection fail-closed outcomes: supplies the audit-failure class. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-24.21 — Connection fail-closed outcomes | Uncommittable required audit. | Prevents false completed truth. | No silent operation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20] |

SUB-PARTS: NONE

### C-24.22 — Connection-owned durable-operation coordination boundary
Stamp: ACCEPTED    Source: [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §T] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §U]

ALONE
- What it is: ACCEPTED — The connection-owned interface to reference-only durable-operation coordination. [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §T] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §U]
- Takes in: ACCEPTED — Proposed CRK, proposed authority_event_key, accepted-record and authority-proof references, and the per-use resolution reference where required. [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §T] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §U]
- Does: ACCEPTED — Retains relationship identity, waiting, accepted/rejected/undecided routes, current-use correction and connection terminals with the connection owner. Coordination checks that the owner-required per-use resolution reference exists; it does not replace that fresh resolution. Connection claims and fences run at the connection seam in full. [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §T] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §U]
- Gives out: ACCEPTED — References to actual connection truth for lookup-first recovery, never transferred effect authority. [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §T] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §U]
- Must never: ACCEPTED — Let a generic coordination claim authorize an unapproved connection effect, replace or normalize owner keys, split record from proof, perform/replay/reissue/rollback a connection effect, or treat a reference as permission to act. [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §T] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §U]
- Fails closed by: ACCEPTED — Absent owner authorization or required current-use resolution, coordination cannot authorize the dependent connection effect. [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §T] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §U]

TOGETHER
- Fed by: ACCEPTED — C-24.10.1 — Proposed canonical_relationship_key (CRK): proposed relationship key; C-24.10.2 — Proposed authority_event_key: proposed authority-event identity; C-24.1.1 — Proposed accepted_connection_record: proposed accepted record and proof-bound history. [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §T] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §U]
- Gated by: ACCEPTED — C-24.14 — Connection current-use resolution: the actual fresh owner resolution remains required before each use. [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §T] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §U]
- Changes: DESIGNED — C-24 — Connection Capability (§24): preserves connection effect ownership across generic coordination. [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §T] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §U]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-24 — Connection Capability (§24) | Reference-only coordination support. | Keeps component claims and per-use checks authoritative. | No generic effect permission. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §K] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §T] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §U] |
| 2 · ACCEPTED | C-7Q.11.9 — Backup and durable-coordination privacy boundary | Backup restores, current connection uses and recorded operation state. | Supplies owner-preserving durable coordination. | Nothing in this card. | [04/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md §11] [04/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md §16] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md §15] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §U] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §V.2] [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §W] |

SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece USED BY continuations

These rows add the reciprocal USED BY entries to the named external cards at assembly. They preserve the delivered cards; every row names both ends. The relationship wording is carried from the current TOGETHER field.

| Current card | Field | External card receiving USED BY row | Stamp | Relationship and condition | Source |
|---|---|---|---|---|---|
| C-24 — Connection Capability (§24) | Fed by | C-7L.12 — Person-Box generic-connection use boundary | ACCEPTED | C-7L.12 — Person-Box generic-connection use boundary: separately governed identity-use result; C-24.7 — Proposed Connection Capability Recordkeeper (CCR): proposed recordkeeper; C-24.8 — Proposed connection type-and-direction contract: proposed type contract; C-24.9 — Connection atomic compare-and-commit: atomic commit; C-24.10 — Connection duplicate identities: proposed relationship and authority keys; C-24.11 — Connection rejection and new-evidence suppression: rejection suppression; C-24.12 — Proposed connection mechanical records: proposed records; C-24.13 — Connection operation lifecycle: lifecycle; C-24.14 — Connection current-use resolution: current use; C-24.15 — Connection Person-Box handoff: identity handoff; C-24.16 — Connection privacy and visible-output boundary: privacy/output boundary; C-24.17 — Connection crash and restart recovery: recovery; C-24.18 — Connection technical retry boundary: retry; C-24.19 — Connection interface contracts: interfaces; C-24.20 — Connection operational recordkeeping: operational records; C-24.21 — Connection fail-closed outcomes: failures. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §3] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §9] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §16] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §17] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §20] |
| C-24 — Connection Capability (§24) | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current purpose-specific privacy; C-7P — Permission & Authority Boundaries (§7P): explicit authority for rules and action-related use. | [V10 §24] [MAP C-24] |
| C-24 — Connection Capability (§24) | Gated by | C-7P — Permission & Authority Boundaries (§7P) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current purpose-specific privacy; C-7P — Permission & Authority Boundaries (§7P): explicit authority for rules and action-related use. | [V10 §24] [MAP C-24] |
| C-24 — Connection Capability (§24) | Changes | C-7F — Context Retrieval (§7F) | DESIGNED | C-7F — Context Retrieval (§7F): provides bounded relationship context and investigation guidance without creating a retrieval-side acceptance authority. | [V10 §24] [MAP C-24] |
| C-24.2 — Connection retrieval role | Gated by | C-7F — Context Retrieval (§7F) | DESIGNED | C-7F — Context Retrieval (§7F): its own retrieval rules remain binding. | [V10 §24] |
| C-24.2.1 — Accepted-connection retrieval route | Fed by | C-LMAC — Live Mechanism Access Coordinator (§26) | DESIGNED | C-LMAC — Live Mechanism Access Coordinator (§26): stateless routing; C-7F — Context Retrieval (§7F): the actual retrieval operation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A] |
| C-24.2.1 — Accepted-connection retrieval route | Fed by | C-7F — Context Retrieval (§7F) | DESIGNED | C-LMAC — Live Mechanism Access Coordinator (§26): stateless routing; C-7F — Context Retrieval (§7F): the actual retrieval operation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A] |
| C-24.2.1 — Accepted-connection retrieval route | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current internal-use authorization; C-7R — Attention & Relevance Control (§7R): purpose-scoped relevance configuration. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A] |
| C-24.2.1 — Accepted-connection retrieval route | Gated by | C-7R — Attention & Relevance Control (§7R) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current internal-use authorization; C-7R — Attention & Relevance Control (§7R): purpose-scoped relevance configuration. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A] |
| C-24.2.2 — Pending-connection investigation route | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current internal-use authorization. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B] |
| C-24.3.1 — Proposed connection_proposal_record | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): route-level authorization immediately before proposal commit. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] |
| C-24.4.1.3 — Verification-unavailable relationship outcome | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current internal-use permission for any investigation exposure. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5A] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13B] |
| C-24.4.3 — Existing authorized connection-rule route | Gated by | C-7P — Permission & Authority Boundaries (§7P) | DESIGNED | C-7P — Permission & Authority Boundaries (§7P): the existing rule’s proper authority owner. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §5C] |
| C-24.9.1 — Atomic direct-source commitment | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): immediately-before-commit internal-use authorization. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7A] |
| C-24.9.2 — Atomic Ness acceptance commitment | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): route-level authorization immediately before the final commit; C-9 — Access/authentication model + voice I/O + phone modes (§9): current accepted identity/access authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| C-24.9.2 — Atomic Ness acceptance commitment | Gated by | C-9 — Access/authentication model + voice I/O + phone modes (§9) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): route-level authorization immediately before the final commit; C-9 — Access/authentication model + voice I/O + phone modes (§9): current accepted identity/access authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| C-24.9.2.1.4 — Forward-completion recovery authority | Gated by | C-9 — Access/authentication model + voice I/O + phone modes (§9) | DESIGNED | C-9 — Access/authentication model + voice I/O + phone modes (§9): accepted identity/access authority ownership. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| C-24.9.2.1.10 — Forward-completion no current authority or privacy block | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current privacy; C-7P — Permission & Authority Boundaries (§7P): applicable authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| C-24.9.2.1.10 — Forward-completion no current authority or privacy block | Gated by | C-7P — Permission & Authority Boundaries (§7P) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current privacy; C-7P — Permission & Authority Boundaries (§7P): applicable authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7B] |
| C-24.9.3 — Atomic authorized-rule commitment | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current route-level privacy; C-7P — Permission & Authority Boundaries (§7P): actual rule authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C] |
| C-24.9.3 — Atomic authorized-rule commitment | Gated by | C-7P — Permission & Authority Boundaries (§7P) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current route-level privacy; C-7P — Permission & Authority Boundaries (§7P): actual rule authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7C] |
| C-24.9.4 — Connection rejection commitment | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current route-level internal-use permission; C-9 — Access/authentication model + voice I/O + phone modes (§9): current identity/access authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D] |
| C-24.9.4 — Connection rejection commitment | Gated by | C-9 — Access/authentication model + voice I/O + phone modes (§9) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current route-level internal-use permission; C-9 — Access/authentication model + voice I/O + phone modes (§9): current identity/access authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §7D] |
| C-24.12.6 — Proposed connection_correction_event | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current internal-use authorization immediately before correction commit. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §11] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.14 — Connection current-use resolution | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current authorization and separate influence-removal status. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] |
| C-24.14.1.8 — Current-use privacy authorization | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current internal-use authorization. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15] |
| C-24.14.1.9 — Current-use influence-removal check | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): separate influence-removal authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15] |
| C-24.15 — Connection Person-Box handoff | Fed by | C-7L.12 — Person-Box generic-connection use boundary | ACCEPTED | C-7L.12 — Person-Box generic-connection use boundary: existing ten-rule generic-connection identity-use boundary. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.15 — Connection Person-Box handoff | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current route-level authorization for this handoff. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] |
| C-24.16 — Connection privacy and visible-output boundary | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy and influence-removal decisions; C-SACL — Speaker Access-Control Layer (§25.4): current output access; C-9 — Access/authentication model + voice I/O + phone modes (§9): current identity/access fence and owner facts. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.16 — Connection privacy and visible-output boundary | Gated by | C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy and influence-removal decisions; C-SACL — Speaker Access-Control Layer (§25.4): current output access; C-9 — Access/authentication model + voice I/O + phone modes (§9): current identity/access fence and owner facts. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.16 — Connection privacy and visible-output boundary | Gated by | C-9 — Access/authentication model + voice I/O + phone modes (§9) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy and influence-removal decisions; C-SACL — Speaker Access-Control Layer (§25.4): current output access; C-9 — Access/authentication model + voice I/O + phone modes (§9): current identity/access fence and owner facts. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.18 — Connection technical retry boundary | Gated by | C-7H.9 — B9 retry-state architecture | ACCEPTED | C-7H.9 — B9 retry-state architecture: accepted technical retry admission and classifications; C-7H.10 — Accepted B9 retry values and episodes: accepted retry values, without inventing new counts, gaps, timeouts or backoff. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §17] |
| C-24.18 — Connection technical retry boundary | Gated by | C-7H.10 — Accepted B9 retry values and episodes | ACCEPTED | C-7H.9 — B9 retry-state architecture: accepted technical retry admission and classifications; C-7H.10 — Accepted B9 retry values and episodes: accepted retry values, without inventing new counts, gaps, timeouts or backoff. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §17] |
| C-24.19.1 — Connection I1 direct-source interface | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): references-only classification with endpoint privacy carried; route-level precommit authorization. Access-factor reference is not applicable to this machine route; source-owner authority applies without inventing a Ness factor. Current-use check is not applicable at creation, but mandatory for every later use. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.2 — Connection I2 candidate-report interface | Fed by | C-7F — Context Retrieval (§7F) | DESIGNED | C-7F — Context Retrieval (§7F): the caller supplies encountered source references. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.2 — Connection I2 candidate-report interface | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): references-only classification; internal-use authorization before submission. Identity/access factor and accepted-current-use resolution are not applicable here. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.3 — Connection I3 source-verification interface | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): references-only classification and internal-use authorization. Access-factor reference and accepted-current-use resolution are not applicable. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.4 — Connection I4 Ness-decision interface | Gated by | C-9 — Access/authentication model + voice I/O + phone modes (§9) | DESIGNED | C-9 — Access/authentication model + voice I/O + phone modes (§9): current accepted identity/access authority; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): route-level precommit privacy, with visible-surface privacy first; C-SACL — Speaker Access-Control Layer (§25.4): surface access second, with current fence revalidated. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.4 — Connection I4 Ness-decision interface | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-9 — Access/authentication model + voice I/O + phone modes (§9): current accepted identity/access authority; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): route-level precommit privacy, with visible-surface privacy first; C-SACL — Speaker Access-Control Layer (§25.4): surface access second, with current fence revalidated. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.4 — Connection I4 Ness-decision interface | Gated by | C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED | C-9 — Access/authentication model + voice I/O + phone modes (§9): current accepted identity/access authority; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): route-level precommit privacy, with visible-surface privacy first; C-SACL — Speaker Access-Control Layer (§25.4): surface access second, with current fence revalidated. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.5 — Connection I5 authorized-rule interface | Fed by | C-7P — Permission & Authority Boundaries (§7P) | DESIGNED | C-7P — Permission & Authority Boundaries (§7P): actual rule owner and Ness-authorization provenance. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.5 — Connection I5 authorized-rule interface | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): references-only classification and route-level final authorization. Access reference is the rule Ness-authorization provenance; current-use resolution is not applicable at creation but required on later use. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.6 — Connection I6 investigation-guidance interface | Fed by | C-7F — Context Retrieval (§7F) | DESIGNED | C-7F — Context Retrieval (§7F): owns the actual retrieval investigation. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.6 — Connection I6 investigation-guidance interface | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): internal-use classification and authorization before use. Access-factor reference is not applicable; accepted-current-use resolution is not applicable to pending material. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.7 — Connection I7 accepted-use interface | Fed by | C-7F — Context Retrieval (§7F) | DESIGNED | C-7F — Context Retrieval (§7F): retrieval owner; C-LMAC — Live Mechanism Access Coordinator (§26): stateless route; C-7R — Attention & Relevance Control (§7R): accepted purpose/relevance configuration. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.7 — Connection I7 accepted-use interface | Fed by | C-LMAC — Live Mechanism Access Coordinator (§26) | DESIGNED | C-7F — Context Retrieval (§7F): retrieval owner; C-LMAC — Live Mechanism Access Coordinator (§26): stateless route; C-7R — Attention & Relevance Control (§7R): accepted purpose/relevance configuration. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.7 — Connection I7 accepted-use interface | Fed by | C-7R — Attention & Relevance Control (§7R) | DESIGNED | C-7F — Context Retrieval (§7F): retrieval owner; C-LMAC — Live Mechanism Access Coordinator (§26): stateless route; C-7R — Attention & Relevance Control (§7R): accepted purpose/relevance configuration. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.7 — Connection I7 accepted-use interface | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): references-only internal-use classification and permission before use and within resolution; access-factor reference is not applicable. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.8 — Connection I8 Person-Box interface | Fed by | C-7L.12 — Person-Box generic-connection use boundary | ACCEPTED | C-7L.12 — Person-Box generic-connection use boundary: existing identity rules and ten-rule generic-use boundary, including its own clear/unclear test. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.8 — Connection I8 Person-Box interface | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): references-only internal-use classification and authorization before handoff; identity/access retains the accepted Person-Box rules. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.9 — Connection I9 correction-dispute interface | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): references-only classification and route-level precommit authorization. Access reference is the correcting source authority. The new event enters every subsequent current-use resolution and controls use without rewriting history. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.10 — Connection I10 visible-output interface | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): visible-output classification and first privacy factor; C-SACL — Speaker Access-Control Layer (§25.4): second access factor; C-9 — Access/authentication model + voice I/O + phone modes (§9): revalidated fence and owner facts. Materially affected disputed current-use status must surface its uncertainty through this chain. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.10 — Connection I10 visible-output interface | Gated by | C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): visible-output classification and first privacy factor; C-SACL — Speaker Access-Control Layer (§25.4): second access factor; C-9 — Access/authentication model + voice I/O + phone modes (§9): revalidated fence and owner facts. Materially affected disputed current-use status must surface its uncertainty through this chain. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.10 — Connection I10 visible-output interface | Gated by | C-9 — Access/authentication model + voice I/O + phone modes (§9) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): visible-output classification and first privacy factor; C-SACL — Speaker Access-Control Layer (§25.4): second access factor; C-9 — Access/authentication model + voice I/O + phone modes (§9): revalidated fence and owner facts. Materially affected disputed current-use status must surface its uncertainty through this chain. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.11 — Connection I11 operational-record interface | Fed by | C-7B.10.5 — Real-operation and evidence boundaries | DESIGNED | C-7B.10.5 — Real-operation and evidence boundaries: one-real-operation logging law; C-7B.10.8 — Operational-record access boundary: normal log access. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.11 — Connection I11 operational-record interface | Fed by | C-7B.10.8 — Operational-record access boundary | DESIGNED | C-7B.10.5 — Real-operation and evidence boundaries: one-real-operation logging law; C-7B.10.8 — Operational-record access boundary: normal log access. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.11 — Connection I11 operational-record interface | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): log access classification and authorization; C-9 — Access/authentication model + voice I/O + phone modes (§9): identity/access and compartment restrictions. Current-use logs record outcomes without becoming authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.19.11 — Connection I11 operational-record interface | Gated by | C-9 — Access/authentication model + voice I/O + phone modes (§9) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): log access classification and authorization; C-9 — Access/authentication model + voice I/O + phone modes (§9): identity/access and compartment restrictions. Current-use logs record outcomes without becoming authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-24.20 — Connection operational recordkeeping | Gated by | C-7B.10.5 — Real-operation and evidence boundaries | DESIGNED | C-7B.10.5 — Real-operation and evidence boundaries: one parent per real operation; C-7B.10.8 — Operational-record access boundary: ordinary authorized log access; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy and influence removal; C-9 — Access/authentication model + voice I/O + phone modes (§9): access/compartment rules. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |
| C-24.20 — Connection operational recordkeeping | Gated by | C-7B.10.8 — Operational-record access boundary | DESIGNED | C-7B.10.5 — Real-operation and evidence boundaries: one parent per real operation; C-7B.10.8 — Operational-record access boundary: ordinary authorized log access; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy and influence removal; C-9 — Access/authentication model + voice I/O + phone modes (§9): access/compartment rules. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |
| C-24.20 — Connection operational recordkeeping | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7B.10.5 — Real-operation and evidence boundaries: one parent per real operation; C-7B.10.8 — Operational-record access boundary: ordinary authorized log access; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy and influence removal; C-9 — Access/authentication model + voice I/O + phone modes (§9): access/compartment rules. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |
| C-24.20 — Connection operational recordkeeping | Gated by | C-9 — Access/authentication model + voice I/O + phone modes (§9) | DESIGNED | C-7B.10.5 — Real-operation and evidence boundaries: one parent per real operation; C-7B.10.8 — Operational-record access boundary: ordinary authorized log access; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy and influence removal; C-9 — Access/authentication model + voice I/O + phone modes (§9): access/compartment rules. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §19] |
| C-24 — Connection Capability (§24) | Fed by | C-7B.9.12 — Later-real-evidence separation | ACCEPTED | C-7B.9.12 — Later-real-evidence separation: supplies Wonder material and later real evidence, under the existing connection, provenance and certainty rules. | [04/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md §8] [MAP C-24] |

## Cross-piece TOGETHER continuations for incoming uses

These are the reciprocal uses represented in the current USED BY tables. Their external owners retain their full mechanisms in their assigned pieces.

| Current card supplying use | External using card | Takes in there | Does there | Changes there | Stamp | Source |
|---|---|---|---|---|---|---|
| C-24 — Connection Capability (§24) | C-7B.10.6.2.2 — Semantic cold-retrieval fallback | A proposed associative relationship. | Applies the three approved connection bases. | No acceptance from similarity. | DESIGNED | [V10 §24] |
| C-24 — Connection Capability (§24) | C-7B.10.6.3.2 — Valid-link reactivation condition | A proposed new relationship for cold reactivation. | Requires a valid connection before treating it as a new link. | No similarity-only reactivation. | DESIGNED | [V10 §24] |
| C-24 — Connection Capability (§24) | C-7L.12 — Person-Box generic-connection use boundary | One provenance-bearing generic relationship. | Keeps identity authority and current-use checks separate. | No automatic identity consequence. | ACCEPTED | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] |
| C-24 — Connection Capability (§24) | C-7F — Context Retrieval (§7F) | Accepted relationships and pending hints. | Keeps the current retrieval operation separate from lasting acceptance. | Bounded context. | DESIGNED | [V10 §24] |

## Scope, paths and source dispositions

The V10/Map two-part capability and waiting rules are placed before the accepted B-INT-8 mechanics. The proposed recordkeeper is only a record owner; source verification, Ness choice, rule validity, identity, privacy, relevance and output authority remain with their actual owners. Generic connections consume the already delivered C-7L.12 identity-use boundary and never duplicate its identity state machine. Existing B9 classifications/values and one-operation/log-access atoms are reused. The generic operation kernel receives references and retains no connection effect authority; its general lifecycle remains outside this connection-owned boundary.

All twenty-two crash rows and all eleven interface rows are placed, including every source column and explicit not-applicable judgments. The three output identities remain separate; the connection-owned consumer cards record their B-INT-6 reference contract while the full output mechanism remains with later identity/access/output owners. The source schema pairs are split into atomic slots; shared record inputs are referenced rather than renamed. The twenty-eight operational child kinds are mapped to the already written actual operations, including correction and dispute as distinct child kinds sharing an append-only event schema.

The exact proposed direct-source route spelling and schema spelling differ within the same accepted package. The header marks that source conflict; no serialization mapping is chosen. Older V10/Map open integration wording is compared with the later accepted B-INT-8 completion and receipts, not used to remove accepted conceptual mechanics. Their historical audit/workflow prose is excluded from behavior.

Discovery reviewed Connection Capability, C-24, B-INT-8, waiting, acceptance and connection-record terminology across accepted packages, active candidates and decision records. Bundle 5 closeout confirms connection/output authority separation. Kernel sections retain component claims, keys, per-use checks and terminals with the owner. B7 and B-INT-5/6 are reopened for actual consumer contracts. Other Future Feature Intent and A19 card-experience references remain future search/presentation scope; deliberate card association is not a new acceptance route. Five Framework Capabilities remains index/interface direction, not a new connection authority. Matches for an 'accepted connection' between A25 and B10 in the compatibility/closure packages and earlier bundle closeouts concern that design-package linkage, not C-24, and supply no new connection behavior. No excluded Bundle 2 foundation body is read or treated as an absent accepted design.

The four active decision indices are navigation under full NHD-M24 and NHD-BINT8 identifiers. Recovery-ledger rows FR-0336, FR-0401, FR-0416 and FR-0417 are restoration tracking only for Appendix B; none supplies behavior. Existing source conflicts and all earlier-file findings remain unchanged. The known CH06-d grouped USED BY finding remains open; every current USED BY row names one place.

Connection use does not relax the C-7GA.10.3 permanent live-path associative/combined prohibition. The general connection capability and its permitted retrieval uses retain the actual consumer's path restrictions. Full action/authority remains CH07, privacy/relevance/LMAC CH08, identity/access and output implementation CH09, card experience CH10-e, side-path assembly CH11 and final register regeneration CH12.

## Source-to-card coverage added by CH06-g

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §24; MAP C-24; DD §3J; Companion §24 | Two responsibilities, originals separate, waiting, three bases, one-way retrieval, uncertainty, five types, pending silent investigation | C-24 and .1–.6; source-specific accepted mechanics retain their own stamps |
| B-INT-8 §§3–4 | Proposed recordkeeper scope; separate accepted record and retrieval; illustrative type list; proposed versioned type/direction contract | C-24.1/.2/.7/.8 and three contract fields with two directionality values |
| B-INT-8 §5A | Two direct-source entries; actual owner verification; exactly three outcomes and their consequences; failed-history-preserving later routes | C-24.4.1 and .1–.4; C-24.2.3; candidate/report distinction |
| B-INT-8 §5B; §7B | Exact explicit Ness choice, no implied consent, four identities, five route steps, complete precommit set and all ten forward-completion conditions | C-24.4.2; .9.2/.9.2.1 and ten condition cards; .12.3–.5 |
| B-INT-8 §5C; §7C | Existing narrow rule, ten verifiable facts, exact match, current final validation and atomic rule proof | C-24.4.3 and its rule ID/version plus remaining fields; .9.3 |
| B-INT-8 §6; §12A–B | Waiting location versus three decision values; sixteen parent states with transitions and direct bypass; five candidate states and three owner outcomes | C-24.3/.3.2; .13/.13.1/.13.2 and state cards |
| B-INT-8 §§7/7A/7D | One atomic compare-and-commit, durable proof/checkpoint, exact direct-route validation, separate rejection input/final event and suppression | C-24.9/.9.1/.9.4; crash cases and interface boundaries |
| B-INT-8 §8 | Five certainty labels, five exact source-type labels, no numeric mapping, authority/evidence/status separation and material output uncertainty | C-24.5/.6 and value cards; proposed schema consumers |
| B-INT-8 §9 | Proposed CRK minimum fields, symmetric normalization, directional distinction, separate types, racing routes, proposed authority-event key and same-proof idempotency | C-24.10/.10.1/.10.2; .8 and endpoint/authority atoms reused |
| B-INT-8 §10 | Rejected history, verified genuine delta/new ID/backlink/same key, six non-deltas, owner judgment and proposed suppression registry | C-24.11/.11.1; .3.1.3/.3.1.4; crash 17 |
| B-INT-8 §11 | All proposed endpoint, proposal, accepted, durable-input, final-decision, authority, correction, use, duplicate, parent, candidate, suppression and recovery records and slots | C-24.1.1; .3.1; .12 and field children; .10/.11/.13/.14 shared atoms |
| B-INT-8 §12C | Immutable history, backwards correction links, nine per-use resolution inputs, separate proposed state namespace, three outcomes and fail-closed, changed-geometry new version/key/both-links | C-24.14/.14.1/.14.2 and children; .12.6; retrieval/identity/output consumers |
| B-INT-8 §13A–D | Accepted use through LMAC, pending investigation marker and separation, candidate submission, complete retrieval audit additions | C-24.2.1–.2.3; .2.2.1; .12.7 with field-level audit additions |
| B-INT-8 §14; prior Bundle 3 identity rules | All ten generic-connection/identity rules, clear/unclear and definite/less-than-definite owner tests retained without duplicate identity approval; fresh current-use/privacy before handoff | C-24.15 and I8; existing C-7L.12 reused in full |
| B-INT-8 §15; B7 §16; B-INT-5 §13 | Privacy before all internal operations/commits, influence removal separate, no endpoint permission, opaque Level-1 references, shared output ceiling and no hidden signal | C-24.16; route gates and I1–I11 authorization columns |
| B-INT-8 §16 | All twenty-two crash boundaries and all nine descriptive columns: truth, recovery, key, retry, fresh action, duplicate rule, failure and audit | C-24.17.1–.17.22; common lookup-first and no-authority-reconstruction rules |
| B-INT-8 §17 | B9 by reference, same-operation technical-only retry, nine forbidden automatic retry classes and fresh decision/new evidence distinctions | C-24.18; existing C-7H.9/.10 |
| B-INT-8 §18 | All eleven interfaces and nineteen source columns including explicit n/a judgments, request/response schemas, owner truth, identity, authorization, recovery and current-use | C-24.19.1–.19.11; existing schema atoms reused |
| B-INT-8 I10; B-INT-6 §§3–5/6A | Separate stable output parent, separate request-plus-destination delivery token excluding mutable versions, per-attempt identity/facts, full output-chain ownership and honest duplicate scope | C-24.16.1–.16.3; .19.10; later full output mechanism remains CH09 |
| B-INT-8 §19 | One parent, all twenty-eight child kinds, all decision/use outcomes, no recursive/weighted logs, actual-use/valid-link cold reactivation, authorized log access | C-24.20/.20.1; existing C-7B logging/access atoms reused |
| B-INT-8 §§20–22 | All named fail-closed classes and outcomes; exact open mechanical slots and must-nevers | C-24.21 and four additional failure cards; route/status/recovery owners; gap register |
| Durable Operation Kernel §K; §T I-11; §U connection owner; scoped AF-6/AF-9 and R-33 | Generic coordination cannot replace connection claims/keys, split proof, perform/replay effects or substitute for fresh per-use resolution; connection terminals stay local | C-24.22 reference-only consumer boundary; general kernel mechanisms remain separate |
| B-INT-8 receipt; Bundle 5 closeout/receipt; active indices; recovery ledger | Exact accepted package, authority/output identity consistency and restoration-only navigation | READ RECORD; no workflow imported; Appendix B tracking carried |
| Active A19 §§13.2/13.3/16.2/16.3; future-feature intent; framework direction | Cards remain references and deliberate association does not silently accept; future unified search/index direction | Later C-19/CH10-e presentation and search owners; no invented current acceptance machinery |

## Additional undecided implementation slots

| Owner | Slot | State |
|---|---|---|
| C-24 — Connection Capability (§24) | Implementation, empirical values, model/provider choices and exact technology beyond accepted conceptual mechanics | NOT DECIDED |
| C-24.1.1.2 — Proposed connection acceptance-basis field | Exact serialization mapping between proposed direct_source_relationship route wording and proposed direct_source schema enum; source conflict remains unresolved | NOT DECIDED |
| C-24.3 — Connection waiting area | Exact waiting-area UI layout/wording and scheduling or surfacing policy for undecided proposals | NOT DECIDED |
| C-24.4.3 — Existing authorized connection-rule route | Future authorized-rule creation policy beyond already-authorized narrow rules | NOT DECIDED |
| C-24.5 — Connection certainty | Numeric certainty mapping and evidence-to-label thresholds; no rule choosing labels is invented | NOT DECIDED |
| C-24.8 — Proposed connection type-and-direction contract | Full closed type vocabulary, concrete external type-registry implementation and future type additions | NOT DECIDED |
| C-24.11 — Connection rejection and new-evidence suppression | Exact empirical threshold for genuine new evidence beyond actual source/evidence owner judgment | NOT DECIDED |
| C-24.12 — Proposed connection mechanical records | Final serialization, finalized field names, storage technology and database choice for the proposed schemas | NOT DECIDED |

## Appendix A carry-forward — this piece

| Card | Empty field | Occurrence within field | State |
|---|---|---|---|
| C-24.1 — Lasting connection record | Fails closed by | 1 | NOT DECIDED |
| C-24.1 — Lasting connection record | Gated by | 1 | NOT DECIDED |
| C-24.1.1.1 — Proposed accepted_connection_id | Fails closed by | 1 | NOT DECIDED |
| C-24.1.1.1 — Proposed accepted_connection_id | Fed by | 1 | NOT DECIDED |
| C-24.1.1.1 — Proposed accepted_connection_id | Gated by | 1 | NOT DECIDED |
| C-24.1.1.2 — Proposed connection acceptance-basis field | Fed by | 1 | NOT DECIDED |
| C-24.1.1.2 — Proposed connection acceptance-basis field | Gated by | 1 | NOT DECIDED |
| C-24.1.1.3 — Proposed connection authority references | Fed by | 1 | NOT DECIDED |
| C-24.1.1.3 — Proposed connection authority references | Gated by | 1 | NOT DECIDED |
| C-24.1.1.4 — Proposed connection supporting-evidence references | Fails closed by | 1 | NOT DECIDED |
| C-24.1.1.4 — Proposed connection supporting-evidence references | Fed by | 1 | NOT DECIDED |
| C-24.1.1.4 — Proposed connection supporting-evidence references | Gated by | 1 | NOT DECIDED |
| C-24.1.1.5 — Proposed connection accepted-at | Fails closed by | 1 | NOT DECIDED |
| C-24.1.1.5 — Proposed connection accepted-at | Fed by | 1 | NOT DECIDED |
| C-24.1.1.5 — Proposed connection accepted-at | Gated by | 1 | NOT DECIDED |
| C-24.1.1.6 — Proposed accepted-record known correction links | Fails closed by | 1 | NOT DECIDED |
| C-24.1.1.6 — Proposed accepted-record known correction links | Fed by | 1 | NOT DECIDED |
| C-24.1.1.6 — Proposed accepted-record known correction links | Gated by | 1 | NOT DECIDED |
| C-24.1.1.7 — Proposed accepted-record schema and record version | Fails closed by | 1 | NOT DECIDED |
| C-24.1.1.7 — Proposed accepted-record schema and record version | Gated by | 1 | NOT DECIDED |
| C-24.1.1.7.1 — Proposed accepted-record schema version | Must never | 1 | NOT DECIDED |
| C-24.1.1.7.1 — Proposed accepted-record schema version | Fails closed by | 1 | NOT DECIDED |
| C-24.1.1.7.1 — Proposed accepted-record schema version | Fed by | 1 | NOT DECIDED |
| C-24.1.1.7.1 — Proposed accepted-record schema version | Gated by | 1 | NOT DECIDED |
| C-24.1.1.7.2 — Proposed accepted-record version | Fails closed by | 1 | NOT DECIDED |
| C-24.1.1.7.2 — Proposed accepted-record version | Fed by | 1 | NOT DECIDED |
| C-24.1.1.7.2 — Proposed accepted-record version | Gated by | 1 | NOT DECIDED |
| C-24.1.1.8 — Proposed connection integrity reference | Fed by | 1 | NOT DECIDED |
| C-24.1.1.8 — Proposed connection integrity reference | Gated by | 1 | NOT DECIDED |
| C-24.2 — Connection retrieval role | Fails closed by | 1 | NOT DECIDED |
| C-24.2.2.1 — Proposed investigation_only_pending_connection marker | Fed by | 1 | NOT DECIDED |
| C-24.2.2.1 — Proposed investigation_only_pending_connection marker | Gated by | 1 | NOT DECIDED |
| C-24.2.3 — Connection candidate-report retrieval route | Gated by | 1 | NOT DECIDED |
| C-24.3 — Connection waiting area | Gated by | 1 | NOT DECIDED |
| C-24.3.1.1 — Proposed connection_proposal_id and version | Gated by | 1 | NOT DECIDED |
| C-24.3.1.1.1 — Proposed connection_proposal_id | Fails closed by | 1 | NOT DECIDED |
| C-24.3.1.1.1 — Proposed connection_proposal_id | Fed by | 1 | NOT DECIDED |
| C-24.3.1.1.1 — Proposed connection_proposal_id | Gated by | 1 | NOT DECIDED |
| C-24.3.1.1.2 — Proposed connection proposal version | Fails closed by | 1 | NOT DECIDED |
| C-24.3.1.1.2 — Proposed connection proposal version | Fed by | 1 | NOT DECIDED |
| C-24.3.1.1.2 — Proposed connection proposal version | Gated by | 1 | NOT DECIDED |
| C-24.3.1.2 — Proposed proposal acceptance-basis route | Fed by | 1 | NOT DECIDED |
| C-24.3.1.2 — Proposed proposal acceptance-basis route | Gated by | 1 | NOT DECIDED |
| C-24.3.1.3 — Proposed prior rejected-proposal reference | Fails closed by | 1 | NOT DECIDED |
| C-24.3.1.3 — Proposed prior rejected-proposal reference | Fed by | 1 | NOT DECIDED |
| C-24.3.1.3 — Proposed prior rejected-proposal reference | Gated by | 1 | NOT DECIDED |
| C-24.3.1.4 — Proposed connection new-evidence delta reference | Fed by | 1 | NOT DECIDED |
| C-24.3.1.4 — Proposed connection new-evidence delta reference | Gated by | 1 | NOT DECIDED |
| C-24.3.1.5 — Proposed proposal created-at and source-owner versions | Gated by | 1 | NOT DECIDED |
| C-24.3.1.5.1 — Proposed proposal created-at | Fails closed by | 1 | NOT DECIDED |
| C-24.3.1.5.1 — Proposed proposal created-at | Fed by | 1 | NOT DECIDED |
| C-24.3.1.5.1 — Proposed proposal created-at | Gated by | 1 | NOT DECIDED |
| C-24.3.1.5.2 — Proposed proposal source-owner versions | Fails closed by | 1 | NOT DECIDED |
| C-24.3.1.5.2 — Proposed proposal source-owner versions | Fed by | 1 | NOT DECIDED |
| C-24.3.1.5.2 — Proposed proposal source-owner versions | Gated by | 1 | NOT DECIDED |
| C-24.3.1.6 — Proposed proposal privacy and authority references | Gated by | 1 | NOT DECIDED |
| C-24.3.1.6.1 — Proposed proposal privacy references | Fails closed by | 1 | NOT DECIDED |
| C-24.3.1.6.1 — Proposed proposal privacy references | Fed by | 1 | NOT DECIDED |
| C-24.3.1.6.1 — Proposed proposal privacy references | Gated by | 1 | NOT DECIDED |
| C-24.3.1.6.2 — Proposed proposal authority references | Fails closed by | 1 | NOT DECIDED |
| C-24.3.1.6.2 — Proposed proposal authority references | Fed by | 1 | NOT DECIDED |
| C-24.3.1.6.2 — Proposed proposal authority references | Gated by | 1 | NOT DECIDED |
| C-24.3.1.7 — Proposed proposal candidate-report provenance | Fails closed by | 1 | NOT DECIDED |
| C-24.3.1.7 — Proposed proposal candidate-report provenance | Fed by | 1 | NOT DECIDED |
| C-24.3.1.7 — Proposed proposal candidate-report provenance | Gated by | 1 | NOT DECIDED |
| C-24.3.2 — Connection decision status | Gated by | 1 | NOT DECIDED |
| C-24.3.2.1 — Undecided connection decision | Fails closed by | 1 | NOT DECIDED |
| C-24.3.2.1 — Undecided connection decision | Fed by | 1 | NOT DECIDED |
| C-24.3.2.1 — Undecided connection decision | Gated by | 1 | NOT DECIDED |
| C-24.3.2.2 — Accepted connection decision | Fed by | 1 | NOT DECIDED |
| C-24.3.2.2 — Accepted connection decision | Gated by | 1 | NOT DECIDED |
| C-24.3.2.3 — Rejected connection decision | Fails closed by | 1 | NOT DECIDED |
| C-24.3.2.3 — Rejected connection decision | Fed by | 1 | NOT DECIDED |
| C-24.3.2.3 — Rejected connection decision | Gated by | 1 | NOT DECIDED |
| C-24.4 — Connection acceptance bases | Gated by | 1 | NOT DECIDED |
| C-24.4.1.1 — Connection source-owner verification | Fed by | 1 | NOT DECIDED |
| C-24.4.1.1 — Connection source-owner verification | Gated by | 1 | NOT DECIDED |
| C-24.4.1.2 — Verified self-establishing relationship outcome | Fed by | 1 | NOT DECIDED |
| C-24.4.1.3 — Verification-unavailable relationship outcome | Fed by | 1 | NOT DECIDED |
| C-24.4.1.4 — Not-verified relationship outcome | Fed by | 1 | NOT DECIDED |
| C-24.4.1.4 — Not-verified relationship outcome | Gated by | 1 | NOT DECIDED |
| C-24.4.3.1 — Connection-rule stable identity and exact version | Gated by | 1 | NOT DECIDED |
| C-24.4.3.1.1 — Connection-rule rule_id | Fails closed by | 1 | NOT DECIDED |
| C-24.4.3.1.1 — Connection-rule rule_id | Fed by | 1 | NOT DECIDED |
| C-24.4.3.1.1 — Connection-rule rule_id | Gated by | 1 | NOT DECIDED |
| C-24.4.3.1.2 — Connection-rule rule_version | Fails closed by | 1 | NOT DECIDED |
| C-24.4.3.1.2 — Connection-rule rule_version | Fed by | 1 | NOT DECIDED |
| C-24.4.3.1.2 — Connection-rule rule_version | Gated by | 1 | NOT DECIDED |
| C-24.4.3.2 — Connection-rule Ness authorization reference | Fed by | 1 | NOT DECIDED |
| C-24.4.3.2 — Connection-rule Ness authorization reference | Gated by | 1 | NOT DECIDED |
| C-24.4.3.3 — Connection-rule declared scope | Fed by | 1 | NOT DECIDED |
| C-24.4.3.3 — Connection-rule declared scope | Gated by | 1 | NOT DECIDED |
| C-24.4.3.4 — Connection-rule eligible endpoint types | Fed by | 1 | NOT DECIDED |
| C-24.4.3.4 — Connection-rule eligible endpoint types | Gated by | 1 | NOT DECIDED |
| C-24.4.3.5 — Connection-rule eligible connection types | Fed by | 1 | NOT DECIDED |
| C-24.4.3.5 — Connection-rule eligible connection types | Gated by | 1 | NOT DECIDED |
| C-24.4.3.6 — Connection-rule source and provenance conditions | Fed by | 1 | NOT DECIDED |
| C-24.4.3.6 — Connection-rule source and provenance conditions | Gated by | 1 | NOT DECIDED |
| C-24.4.3.7 — Connection-rule activation state | Fed by | 1 | NOT DECIDED |
| C-24.4.3.7 — Connection-rule activation state | Gated by | 1 | NOT DECIDED |
| C-24.4.3.8 — Connection-rule revocation and supersession state | Fed by | 1 | NOT DECIDED |
| C-24.4.3.8 — Connection-rule revocation and supersession state | Gated by | 1 | NOT DECIDED |
| C-24.4.3.9 — Connection-rule exact current applicability | Fed by | 1 | NOT DECIDED |
| C-24.4.3.9 — Connection-rule exact current applicability | Gated by | 1 | NOT DECIDED |
| C-24.5 — Connection certainty | Fails closed by | 1 | NOT DECIDED |
| C-24.5 — Connection certainty | Gated by | 1 | NOT DECIDED |
| C-24.5.1 — Possible connection certainty | Fails closed by | 1 | NOT DECIDED |
| C-24.5.1 — Possible connection certainty | Fed by | 1 | NOT DECIDED |
| C-24.5.1 — Possible connection certainty | Gated by | 1 | NOT DECIDED |
| C-24.5.2 — Likely connection certainty | Fails closed by | 1 | NOT DECIDED |
| C-24.5.2 — Likely connection certainty | Fed by | 1 | NOT DECIDED |
| C-24.5.2 — Likely connection certainty | Gated by | 1 | NOT DECIDED |
| C-24.5.3 — Uncertain connection certainty | Fails closed by | 1 | NOT DECIDED |
| C-24.5.3 — Uncertain connection certainty | Fed by | 1 | NOT DECIDED |
| C-24.5.3 — Uncertain connection certainty | Gated by | 1 | NOT DECIDED |
| C-24.5.4 — Disputed connection certainty | Fails closed by | 1 | NOT DECIDED |
| C-24.5.4 — Disputed connection certainty | Fed by | 1 | NOT DECIDED |
| C-24.5.4 — Disputed connection certainty | Gated by | 1 | NOT DECIDED |
| C-24.5.5 — Near-certain connection certainty | Fails closed by | 1 | NOT DECIDED |
| C-24.5.5 — Near-certain connection certainty | Fed by | 1 | NOT DECIDED |
| C-24.5.5 — Near-certain connection certainty | Gated by | 1 | NOT DECIDED |
| C-24.6 — Connection source-type distinctions | Fails closed by | 1 | NOT DECIDED |
| C-24.6 — Connection source-type distinctions | Gated by | 1 | NOT DECIDED |
| C-24.6.1 — Connection source_material label | Fails closed by | 1 | NOT DECIDED |
| C-24.6.1 — Connection source_material label | Fed by | 1 | NOT DECIDED |
| C-24.6.1 — Connection source_material label | Gated by | 1 | NOT DECIDED |
| C-24.6.2 — Connection prior_interpretation label | Fails closed by | 1 | NOT DECIDED |
| C-24.6.2 — Connection prior_interpretation label | Fed by | 1 | NOT DECIDED |
| C-24.6.2 — Connection prior_interpretation label | Gated by | 1 | NOT DECIDED |
| C-24.6.3 — Connection assumption label | Fails closed by | 1 | NOT DECIDED |
| C-24.6.3 — Connection assumption label | Fed by | 1 | NOT DECIDED |
| C-24.6.3 — Connection assumption label | Gated by | 1 | NOT DECIDED |
| C-24.6.4 — Connection unknown label | Fails closed by | 1 | NOT DECIDED |
| C-24.6.4 — Connection unknown label | Fed by | 1 | NOT DECIDED |
| C-24.6.4 — Connection unknown label | Gated by | 1 | NOT DECIDED |
| C-24.6.5 — Connection invented_simulation_material label | Fails closed by | 1 | NOT DECIDED |
| C-24.6.5 — Connection invented_simulation_material label | Fed by | 1 | NOT DECIDED |
| C-24.6.5 — Connection invented_simulation_material label | Gated by | 1 | NOT DECIDED |
| C-24.7 — Proposed Connection Capability Recordkeeper (CCR) | Fed by | 1 | NOT DECIDED |
| C-24.7 — Proposed Connection Capability Recordkeeper (CCR) | Gated by | 1 | NOT DECIDED |
| C-24.8 — Proposed connection type-and-direction contract | Fails closed by | 1 | NOT DECIDED |
| C-24.8 — Proposed connection type-and-direction contract | Gated by | 1 | NOT DECIDED |
| C-24.8.1 — Proposed connection_type_id | Fails closed by | 1 | NOT DECIDED |
| C-24.8.1 — Proposed connection_type_id | Fed by | 1 | NOT DECIDED |
| C-24.8.1 — Proposed connection_type_id | Gated by | 1 | NOT DECIDED |
| C-24.8.2 — Proposed connection type_version | Fails closed by | 1 | NOT DECIDED |
| C-24.8.2 — Proposed connection type_version | Fed by | 1 | NOT DECIDED |
| C-24.8.2 — Proposed connection type_version | Gated by | 1 | NOT DECIDED |
| C-24.8.3 — Proposed connection directionality | Fails closed by | 1 | NOT DECIDED |
| C-24.8.3 — Proposed connection directionality | Gated by | 1 | NOT DECIDED |
| C-24.8.3.1 — Proposed directional connection type | Fails closed by | 1 | NOT DECIDED |
| C-24.8.3.1 — Proposed directional connection type | Fed by | 1 | NOT DECIDED |
| C-24.8.3.1 — Proposed directional connection type | Gated by | 1 | NOT DECIDED |
| C-24.8.3.2 — Proposed symmetric connection type | Fails closed by | 1 | NOT DECIDED |
| C-24.8.3.2 — Proposed symmetric connection type | Fed by | 1 | NOT DECIDED |
| C-24.8.3.2 — Proposed symmetric connection type | Gated by | 1 | NOT DECIDED |
| C-24.9 — Connection atomic compare-and-commit | Gated by | 1 | NOT DECIDED |
| C-24.9.2.1 — Ness decision forward-completion gate | Fed by | 1 | NOT DECIDED |
| C-24.9.2.1.1 — Forward-completion exact proposal binding | Fed by | 1 | NOT DECIDED |
| C-24.9.2.1.1 — Forward-completion exact proposal binding | Gated by | 1 | NOT DECIDED |
| C-24.9.2.1.2 — Forward-completion current decision eligibility | Fed by | 1 | NOT DECIDED |
| C-24.9.2.1.2 — Forward-completion current decision eligibility | Gated by | 1 | NOT DECIDED |
| C-24.9.2.1.3 — Forward-completion input integrity | Fed by | 1 | NOT DECIDED |
| C-24.9.2.1.3 — Forward-completion input integrity | Gated by | 1 | NOT DECIDED |
| C-24.9.2.1.4 — Forward-completion recovery authority | Fed by | 1 | NOT DECIDED |
| C-24.9.2.1.5 — Forward-completion surface and certainty match | Fed by | 1 | NOT DECIDED |
| C-24.9.2.1.5 — Forward-completion surface and certainty match | Gated by | 1 | NOT DECIDED |
| C-24.9.2.1.6 — Forward-completion no conflicting acceptance | Fed by | 1 | NOT DECIDED |
| C-24.9.2.1.6 — Forward-completion no conflicting acceptance | Gated by | 1 | NOT DECIDED |
| C-24.9.2.1.7 — Forward-completion no committed rejection | Fed by | 1 | NOT DECIDED |
| C-24.9.2.1.7 — Forward-completion no committed rejection | Gated by | 1 | NOT DECIDED |
| C-24.9.2.1.8 — Forward-completion no correction-caused staleness | Fed by | 1 | NOT DECIDED |
| C-24.9.2.1.8 — Forward-completion no correction-caused staleness | Gated by | 1 | NOT DECIDED |
| C-24.9.2.1.9 — Forward-completion no superseding proposal | Fed by | 1 | NOT DECIDED |
| C-24.9.2.1.9 — Forward-completion no superseding proposal | Gated by | 1 | NOT DECIDED |
| C-24.9.2.1.10 — Forward-completion no current authority or privacy block | Fed by | 1 | NOT DECIDED |
| C-24.9.3 — Atomic authorized-rule commitment | Fed by | 1 | NOT DECIDED |
| C-24.9.4 — Connection rejection commitment | Fed by | 1 | NOT DECIDED |
| C-24.10 — Connection duplicate identities | Gated by | 1 | NOT DECIDED |
| C-24.10.1 — Proposed canonical_relationship_key (CRK) | Fails closed by | 1 | NOT DECIDED |
| C-24.10.1 — Proposed canonical_relationship_key (CRK) | Gated by | 1 | NOT DECIDED |
| C-24.10.2 — Proposed authority_event_key | Fails closed by | 1 | NOT DECIDED |
| C-24.10.2 — Proposed authority_event_key | Fed by | 1 | NOT DECIDED |
| C-24.10.2 — Proposed authority_event_key | Gated by | 1 | NOT DECIDED |
| C-24.11 — Connection rejection and new-evidence suppression | Gated by | 1 | NOT DECIDED |
| C-24.11.1 — Proposed connection_rejection_suppression_registry | Fed by | 1 | NOT DECIDED |
| C-24.11.1 — Proposed connection_rejection_suppression_registry | Gated by | 1 | NOT DECIDED |
| C-24.12 — Proposed connection mechanical records | Fails closed by | 1 | NOT DECIDED |
| C-24.12 — Proposed connection mechanical records | Gated by | 1 | NOT DECIDED |
| C-24.12.1 — Proposed connection_endpoint_ref | Gated by | 1 | NOT DECIDED |
| C-24.12.1.1 — Proposed endpoint object_type | Fails closed by | 1 | NOT DECIDED |
| C-24.12.1.1 — Proposed endpoint object_type | Fed by | 1 | NOT DECIDED |
| C-24.12.1.1 — Proposed endpoint object_type | Gated by | 1 | NOT DECIDED |
| C-24.12.1.2 — Proposed endpoint stable object ID | Fails closed by | 1 | NOT DECIDED |
| C-24.12.1.2 — Proposed endpoint stable object ID | Fed by | 1 | NOT DECIDED |
| C-24.12.1.2 — Proposed endpoint stable object ID | Gated by | 1 | NOT DECIDED |
| C-24.12.1.3 — Proposed endpoint batch/store or source provenance | Fails closed by | 1 | NOT DECIDED |
| C-24.12.1.3 — Proposed endpoint batch/store or source provenance | Fed by | 1 | NOT DECIDED |
| C-24.12.1.3 — Proposed endpoint batch/store or source provenance | Gated by | 1 | NOT DECIDED |
| C-24.12.1.4 — Proposed endpoint immutable version/reference | Fails closed by | 1 | NOT DECIDED |
| C-24.12.1.4 — Proposed endpoint immutable version/reference | Fed by | 1 | NOT DECIDED |
| C-24.12.1.4 — Proposed endpoint immutable version/reference | Gated by | 1 | NOT DECIDED |
| C-24.12.1.5 — Proposed endpoint privacy classification reference | Fails closed by | 1 | NOT DECIDED |
| C-24.12.1.5 — Proposed endpoint privacy classification reference | Fed by | 1 | NOT DECIDED |
| C-24.12.1.5 — Proposed endpoint privacy classification reference | Gated by | 1 | NOT DECIDED |
| C-24.12.2 — Proposed connection_candidate_report | Fails closed by | 1 | NOT DECIDED |
| C-24.12.2 — Proposed connection_candidate_report | Gated by | 1 | NOT DECIDED |
| C-24.12.2.1 — Proposed connection_candidate_report_id | Fails closed by | 1 | NOT DECIDED |
| C-24.12.2.1 — Proposed connection_candidate_report_id | Fed by | 1 | NOT DECIDED |
| C-24.12.2.1 — Proposed connection_candidate_report_id | Gated by | 1 | NOT DECIDED |
| C-24.12.2.2 — Proposed candidate immutable source references | Fails closed by | 1 | NOT DECIDED |
| C-24.12.2.2 — Proposed candidate immutable source references | Fed by | 1 | NOT DECIDED |
| C-24.12.2.2 — Proposed candidate immutable source references | Gated by | 1 | NOT DECIDED |
| C-24.12.2.3 — Proposed candidate encounter description | Fails closed by | 1 | NOT DECIDED |
| C-24.12.2.3 — Proposed candidate encounter description | Fed by | 1 | NOT DECIDED |
| C-24.12.2.3 — Proposed candidate encounter description | Gated by | 1 | NOT DECIDED |
| C-24.12.2.4 — Proposed candidate verification-outcome field | Fails closed by | 1 | NOT DECIDED |
| C-24.12.2.4 — Proposed candidate verification-outcome field | Fed by | 1 | NOT DECIDED |
| C-24.12.2.4 — Proposed candidate verification-outcome field | Gated by | 1 | NOT DECIDED |
| C-24.12.3 — Proposed ness_decision_input | Gated by | 1 | NOT DECIDED |
| C-24.12.3.1 — Proposed Ness-input exact proposal binding | Fails closed by | 1 | NOT DECIDED |
| C-24.12.3.1 — Proposed Ness-input exact proposal binding | Gated by | 1 | NOT DECIDED |
| C-24.12.3.2 — Proposed Ness-input surface and displayed certainty | Fails closed by | 1 | NOT DECIDED |
| C-24.12.3.2 — Proposed Ness-input surface and displayed certainty | Gated by | 1 | NOT DECIDED |
| C-24.12.3.2.1 — Proposed Ness-input decision-surface version | Fails closed by | 1 | NOT DECIDED |
| C-24.12.3.2.1 — Proposed Ness-input decision-surface version | Fed by | 1 | NOT DECIDED |
| C-24.12.3.2.1 — Proposed Ness-input decision-surface version | Gated by | 1 | NOT DECIDED |
| C-24.12.3.2.2 — Proposed Ness-input displayed certainty | Fails closed by | 1 | NOT DECIDED |
| C-24.12.3.2.2 — Proposed Ness-input displayed certainty | Fed by | 1 | NOT DECIDED |
| C-24.12.3.2.2 — Proposed Ness-input displayed certainty | Gated by | 1 | NOT DECIDED |
| C-24.12.3.3 — Proposed Ness-input authority context reference | Fed by | 1 | NOT DECIDED |
| C-24.12.3.3 — Proposed Ness-input authority context reference | Gated by | 1 | NOT DECIDED |
| C-24.12.4 — Proposed connection_decision_event | Fails closed by | 1 | NOT DECIDED |
| C-24.12.4 — Proposed connection_decision_event | Gated by | 1 | NOT DECIDED |
| C-24.12.4.1 — Proposed connection decision-event fact | Fails closed by | 1 | NOT DECIDED |
| C-24.12.4.1 — Proposed connection decision-event fact | Fed by | 1 | NOT DECIDED |
| C-24.12.4.1 — Proposed connection decision-event fact | Gated by | 1 | NOT DECIDED |
| C-24.12.4.2 — Proposed connection decision-event proposal version | Fails closed by | 1 | NOT DECIDED |
| C-24.12.4.2 — Proposed connection decision-event proposal version | Fed by | 1 | NOT DECIDED |
| C-24.12.4.2 — Proposed connection decision-event proposal version | Gated by | 1 | NOT DECIDED |
| C-24.12.5 — Proposed connection_authority_event | Gated by | 1 | NOT DECIDED |
| C-24.12.5.1 — Proposed authority-event acceptance-basis type | Fails closed by | 1 | NOT DECIDED |
| C-24.12.5.1 — Proposed authority-event acceptance-basis type | Fed by | 1 | NOT DECIDED |
| C-24.12.5.1 — Proposed authority-event acceptance-basis type | Gated by | 1 | NOT DECIDED |
| C-24.12.5.2 — Proposed authority-event exact reference and version | Gated by | 1 | NOT DECIDED |
| C-24.12.5.2.1 — Proposed authority-event exact authority reference | Fails closed by | 1 | NOT DECIDED |
| C-24.12.5.2.1 — Proposed authority-event exact authority reference | Fed by | 1 | NOT DECIDED |
| C-24.12.5.2.1 — Proposed authority-event exact authority reference | Gated by | 1 | NOT DECIDED |
| C-24.12.5.2.2 — Proposed authority-event exact authority version | Fails closed by | 1 | NOT DECIDED |
| C-24.12.5.2.2 — Proposed authority-event exact authority version | Fed by | 1 | NOT DECIDED |
| C-24.12.5.2.2 — Proposed authority-event exact authority version | Gated by | 1 | NOT DECIDED |
| C-24.12.5.3 — Proposed authority-event relationship target | Fails closed by | 1 | NOT DECIDED |
| C-24.12.5.3 — Proposed authority-event relationship target | Fed by | 1 | NOT DECIDED |
| C-24.12.5.3 — Proposed authority-event relationship target | Gated by | 1 | NOT DECIDED |
| C-24.12.6.1 — Proposed correction exact target and version | Gated by | 1 | NOT DECIDED |
| C-24.12.6.1.1 — Proposed correction target record ID | Fails closed by | 1 | NOT DECIDED |
| C-24.12.6.1.1 — Proposed correction target record ID | Fed by | 1 | NOT DECIDED |
| C-24.12.6.1.1 — Proposed correction target record ID | Gated by | 1 | NOT DECIDED |
| C-24.12.6.1.2 — Proposed correction target record version | Fails closed by | 1 | NOT DECIDED |
| C-24.12.6.1.2 — Proposed correction target record version | Fed by | 1 | NOT DECIDED |
| C-24.12.6.1.2 — Proposed correction target record version | Gated by | 1 | NOT DECIDED |
| C-24.12.6.2 — Proposed correction content references | Fails closed by | 1 | NOT DECIDED |
| C-24.12.6.2 — Proposed correction content references | Fed by | 1 | NOT DECIDED |
| C-24.12.6.2 — Proposed correction content references | Gated by | 1 | NOT DECIDED |
| C-24.12.6.3 — Proposed correction basis | Fails closed by | 1 | NOT DECIDED |
| C-24.12.6.3 — Proposed correction basis | Fed by | 1 | NOT DECIDED |
| C-24.12.6.3 — Proposed correction basis | Gated by | 1 | NOT DECIDED |
| C-24.12.6.4 — Proposed correction owner and authority references | Fed by | 1 | NOT DECIDED |
| C-24.12.6.4 — Proposed correction owner and authority references | Gated by | 1 | NOT DECIDED |
| C-24.12.6.5 — Proposed correction_event_id | Fails closed by | 1 | NOT DECIDED |
| C-24.12.6.5 — Proposed correction_event_id | Fed by | 1 | NOT DECIDED |
| C-24.12.6.5 — Proposed correction_event_id | Gated by | 1 | NOT DECIDED |
| C-24.12.7 — Proposed connection_use_event | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7 — Proposed connection_use_event | Gated by | 1 | NOT DECIDED |
| C-24.12.7.1 — Proposed connection-use operation and purpose | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.1 — Proposed connection-use operation and purpose | Gated by | 1 | NOT DECIDED |
| C-24.12.7.1.1 — Proposed connection-use consuming operation | Must never | 1 | NOT DECIDED |
| C-24.12.7.1.1 — Proposed connection-use consuming operation | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.1.1 — Proposed connection-use consuming operation | Fed by | 1 | NOT DECIDED |
| C-24.12.7.1.1 — Proposed connection-use consuming operation | Gated by | 1 | NOT DECIDED |
| C-24.12.7.1.2 — Proposed connection-use purpose | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.1.2 — Proposed connection-use purpose | Fed by | 1 | NOT DECIDED |
| C-24.12.7.1.2 — Proposed connection-use purpose | Gated by | 1 | NOT DECIDED |
| C-24.12.7.2 — Proposed connection-use original accepted ID and version | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.2 — Proposed connection-use original accepted ID and version | Gated by | 1 | NOT DECIDED |
| C-24.12.7.2.1 — Proposed connection-use original accepted-record ID | Must never | 1 | NOT DECIDED |
| C-24.12.7.2.1 — Proposed connection-use original accepted-record ID | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.2.1 — Proposed connection-use original accepted-record ID | Fed by | 1 | NOT DECIDED |
| C-24.12.7.2.1 — Proposed connection-use original accepted-record ID | Gated by | 1 | NOT DECIDED |
| C-24.12.7.2.2 — Proposed connection-use original accepted-record version | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.2.2 — Proposed connection-use original accepted-record version | Fed by | 1 | NOT DECIDED |
| C-24.12.7.2.2 — Proposed connection-use original accepted-record version | Gated by | 1 | NOT DECIDED |
| C-24.12.7.3 — Proposed connection-use chain and resolution result | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.3 — Proposed connection-use chain and resolution result | Gated by | 1 | NOT DECIDED |
| C-24.12.7.3.1 — Proposed connection-use consulted chain | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.3.1 — Proposed connection-use consulted chain | Fed by | 1 | NOT DECIDED |
| C-24.12.7.3.1 — Proposed connection-use consulted chain | Gated by | 1 | NOT DECIDED |
| C-24.12.7.3.2 — Proposed connection-use resolution result | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.3.2 — Proposed connection-use resolution result | Fed by | 1 | NOT DECIDED |
| C-24.12.7.3.2 — Proposed connection-use resolution result | Gated by | 1 | NOT DECIDED |
| C-24.12.7.4 — Proposed connection-use actual version | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.4 — Proposed connection-use actual version | Fed by | 1 | NOT DECIDED |
| C-24.12.7.4 — Proposed connection-use actual version | Gated by | 1 | NOT DECIDED |
| C-24.12.7.5 — Proposed connection-use consulted correction events | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.5 — Proposed connection-use consulted correction events | Fed by | 1 | NOT DECIDED |
| C-24.12.7.5 — Proposed connection-use consulted correction events | Gated by | 1 | NOT DECIDED |
| C-24.12.7.6 — Proposed connection-use accepted or investigation class | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.6 — Proposed connection-use accepted or investigation class | Fed by | 1 | NOT DECIDED |
| C-24.12.7.6 — Proposed connection-use accepted or investigation class | Gated by | 1 | NOT DECIDED |
| C-24.12.7.7 — Proposed connection-use certainty preservation | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.7 — Proposed connection-use certainty preservation | Gated by | 1 | NOT DECIDED |
| C-24.12.7.7.1 — Proposed connection-use preserved certainty | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.7.1 — Proposed connection-use preserved certainty | Fed by | 1 | NOT DECIDED |
| C-24.12.7.7.1 — Proposed connection-use preserved certainty | Gated by | 1 | NOT DECIDED |
| C-24.12.7.7.2 — Proposed connection-use how-certainty-was-preserved | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.7.2 — Proposed connection-use how-certainty-was-preserved | Fed by | 1 | NOT DECIDED |
| C-24.12.7.7.2 — Proposed connection-use how-certainty-was-preserved | Gated by | 1 | NOT DECIDED |
| C-24.12.7.8 — Proposed connection-use output uncertainty behavior | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.8 — Proposed connection-use output uncertainty behavior | Gated by | 1 | NOT DECIDED |
| C-24.12.7.8.1 — Proposed connection-use uncertainty-surfacing requirement | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.8.1 — Proposed connection-use uncertainty-surfacing requirement | Fed by | 1 | NOT DECIDED |
| C-24.12.7.8.1 — Proposed connection-use uncertainty-surfacing requirement | Gated by | 1 | NOT DECIDED |
| C-24.12.7.8.2 — Proposed connection-use actual output uncertainty | Must never | 1 | NOT DECIDED |
| C-24.12.7.8.2 — Proposed connection-use actual output uncertainty | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.8.2 — Proposed connection-use actual output uncertainty | Fed by | 1 | NOT DECIDED |
| C-24.12.7.8.2 — Proposed connection-use actual output uncertainty | Gated by | 1 | NOT DECIDED |
| C-24.12.7.9 — Proposed connection-use non-use and reason | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.9 — Proposed connection-use non-use and reason | Gated by | 1 | NOT DECIDED |
| C-24.12.7.9.1 — Proposed connection-use non-use fact | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.9.1 — Proposed connection-use non-use fact | Fed by | 1 | NOT DECIDED |
| C-24.12.7.9.1 — Proposed connection-use non-use fact | Gated by | 1 | NOT DECIDED |
| C-24.12.7.9.2 — Proposed connection-use non-use reason | Must never | 1 | NOT DECIDED |
| C-24.12.7.9.2 — Proposed connection-use non-use reason | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.9.2 — Proposed connection-use non-use reason | Fed by | 1 | NOT DECIDED |
| C-24.12.7.9.2 — Proposed connection-use non-use reason | Gated by | 1 | NOT DECIDED |
| C-24.12.7.10 — Proposed connection-use result or failure reference | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.10 — Proposed connection-use result or failure reference | Fed by | 1 | NOT DECIDED |
| C-24.12.7.10 — Proposed connection-use result or failure reference | Gated by | 1 | NOT DECIDED |
| C-24.12.7.11 — Proposed connection retrieval-audit additions | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.11 — Proposed connection retrieval-audit additions | Gated by | 1 | NOT DECIDED |
| C-24.12.7.11.1 — Proposed retrieval-audit source-type labels | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.11.1 — Proposed retrieval-audit source-type labels | Fed by | 1 | NOT DECIDED |
| C-24.12.7.11.1 — Proposed retrieval-audit source-type labels | Gated by | 1 | NOT DECIDED |
| C-24.12.7.11.2 — Proposed retrieval-audit eligibility reason | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.11.2 — Proposed retrieval-audit eligibility reason | Fed by | 1 | NOT DECIDED |
| C-24.12.7.11.2 — Proposed retrieval-audit eligibility reason | Gated by | 1 | NOT DECIDED |
| C-24.12.7.11.3 — Proposed retrieval-audit search-scope effect | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.11.3 — Proposed retrieval-audit search-scope effect | Fed by | 1 | NOT DECIDED |
| C-24.12.7.11.3 — Proposed retrieval-audit search-scope effect | Gated by | 1 | NOT DECIDED |
| C-24.12.7.11.4 — Proposed retrieval-audit retrieved material | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.11.4 — Proposed retrieval-audit retrieved material | Fed by | 1 | NOT DECIDED |
| C-24.12.7.11.4 — Proposed retrieval-audit retrieved material | Gated by | 1 | NOT DECIDED |
| C-24.12.7.11.5 — Proposed retrieval-audit later-claim effect | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.11.5 — Proposed retrieval-audit later-claim effect | Fed by | 1 | NOT DECIDED |
| C-24.12.7.11.5 — Proposed retrieval-audit later-claim effect | Gated by | 1 | NOT DECIDED |
| C-24.12.7.11.6 — Proposed retrieval-audit failure | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.11.6 — Proposed retrieval-audit failure | Fed by | 1 | NOT DECIDED |
| C-24.12.7.11.6 — Proposed retrieval-audit failure | Gated by | 1 | NOT DECIDED |
| C-24.12.7.11.7 — Proposed retrieval-audit omission | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.11.7 — Proposed retrieval-audit omission | Fed by | 1 | NOT DECIDED |
| C-24.12.7.11.7 — Proposed retrieval-audit omission | Gated by | 1 | NOT DECIDED |
| C-24.12.7.11.8 — Proposed retrieval-audit truncation | Fails closed by | 1 | NOT DECIDED |
| C-24.12.7.11.8 — Proposed retrieval-audit truncation | Fed by | 1 | NOT DECIDED |
| C-24.12.7.11.8 — Proposed retrieval-audit truncation | Gated by | 1 | NOT DECIDED |
| C-24.12.8 — Proposed connection_duplicate_absorbed | Fails closed by | 1 | NOT DECIDED |
| C-24.12.8 — Proposed connection_duplicate_absorbed | Fed by | 1 | NOT DECIDED |
| C-24.12.8 — Proposed connection_duplicate_absorbed | Gated by | 1 | NOT DECIDED |
| C-24.12.9 — Proposed connection_operation | Fails closed by | 1 | NOT DECIDED |
| C-24.12.9 — Proposed connection_operation | Gated by | 1 | NOT DECIDED |
| C-24.12.9.1 — Proposed connection_operation_id | Fails closed by | 1 | NOT DECIDED |
| C-24.12.9.1 — Proposed connection_operation_id | Fed by | 1 | NOT DECIDED |
| C-24.12.9.1 — Proposed connection_operation_id | Gated by | 1 | NOT DECIDED |
| C-24.12.10 — Proposed connection_recovery_event | Fails closed by | 1 | NOT DECIDED |
| C-24.12.10 — Proposed connection_recovery_event | Fed by | 1 | NOT DECIDED |
| C-24.12.10 — Proposed connection_recovery_event | Gated by | 1 | NOT DECIDED |
| C-24.13 — Connection operation lifecycle | Fails closed by | 1 | NOT DECIDED |
| C-24.13 — Connection operation lifecycle | Gated by | 1 | NOT DECIDED |
| C-24.13.1 — Connection parent states and transitions | Fails closed by | 1 | NOT DECIDED |
| C-24.13.1 — Connection parent states and transitions | Gated by | 1 | NOT DECIDED |
| C-24.13.1.1 — Connection requested_or_detected state | Fails closed by | 1 | NOT DECIDED |
| C-24.13.1.1 — Connection requested_or_detected state | Fed by | 1 | NOT DECIDED |
| C-24.13.1.1 — Connection requested_or_detected state | Gated by | 1 | NOT DECIDED |
| C-24.13.1.2 — Connection source_facts_gathered state | Fails closed by | 1 | NOT DECIDED |
| C-24.13.1.2 — Connection source_facts_gathered state | Fed by | 1 | NOT DECIDED |
| C-24.13.1.2 — Connection source_facts_gathered state | Gated by | 1 | NOT DECIDED |
| C-24.13.1.3 — Connection approved_basis_check state | Fed by | 1 | NOT DECIDED |
| C-24.13.1.3 — Connection approved_basis_check state | Gated by | 1 | NOT DECIDED |
| C-24.13.1.4 — Connection duplicate_check state | Fails closed by | 1 | NOT DECIDED |
| C-24.13.1.4 — Connection duplicate_check state | Fed by | 1 | NOT DECIDED |
| C-24.13.1.4 — Connection duplicate_check state | Gated by | 1 | NOT DECIDED |
| C-24.13.1.5 — Connection proposal_preparation state | Fed by | 1 | NOT DECIDED |
| C-24.13.1.5 — Connection proposal_preparation state | Gated by | 1 | NOT DECIDED |
| C-24.13.1.6 — Connection proposal_committed state | Fails closed by | 1 | NOT DECIDED |
| C-24.13.1.6 — Connection proposal_committed state | Fed by | 1 | NOT DECIDED |
| C-24.13.1.6 — Connection proposal_committed state | Gated by | 1 | NOT DECIDED |
| C-24.13.1.7 — Connection waiting_undecided state | Fails closed by | 1 | NOT DECIDED |
| C-24.13.1.7 — Connection waiting_undecided state | Fed by | 1 | NOT DECIDED |
| C-24.13.1.7 — Connection waiting_undecided state | Gated by | 1 | NOT DECIDED |
| C-24.13.1.8 — Connection direct_source_verification_pending state | Fed by | 1 | NOT DECIDED |
| C-24.13.1.8 — Connection direct_source_verification_pending state | Gated by | 1 | NOT DECIDED |
| C-24.13.1.9 — Connection ness_decision_pending state | Fed by | 1 | NOT DECIDED |
| C-24.13.1.9 — Connection ness_decision_pending state | Gated by | 1 | NOT DECIDED |
| C-24.13.1.10 — Connection authorized_rule_verification_pending state | Fed by | 1 | NOT DECIDED |
| C-24.13.1.10 — Connection authorized_rule_verification_pending state | Gated by | 1 | NOT DECIDED |
| C-24.13.1.11 — Connection acceptance_prepared state | Fed by | 1 | NOT DECIDED |
| C-24.13.1.11 — Connection acceptance_prepared state | Gated by | 1 | NOT DECIDED |
| C-24.13.1.12 — Connection accepted_commit state | Fed by | 1 | NOT DECIDED |
| C-24.13.1.12 — Connection accepted_commit state | Gated by | 1 | NOT DECIDED |
| C-24.13.1.13 — Connection rejected_commit state | Fails closed by | 1 | NOT DECIDED |
| C-24.13.1.13 — Connection rejected_commit state | Fed by | 1 | NOT DECIDED |
| C-24.13.1.13 — Connection rejected_commit state | Gated by | 1 | NOT DECIDED |
| C-24.13.1.14 — Connection blocked state | Fed by | 1 | NOT DECIDED |
| C-24.13.1.14 — Connection blocked state | Gated by | 1 | NOT DECIDED |
| C-24.13.1.15 — Connection failed state | Fed by | 1 | NOT DECIDED |
| C-24.13.1.15 — Connection failed state | Gated by | 1 | NOT DECIDED |
| C-24.13.1.16 — Connection completed state | Fails closed by | 1 | NOT DECIDED |
| C-24.13.1.16 — Connection completed state | Fed by | 1 | NOT DECIDED |
| C-24.13.1.16 — Connection completed state | Gated by | 1 | NOT DECIDED |
| C-24.13.2 — Connection candidate-report lifecycle | Gated by | 1 | NOT DECIDED |
| C-24.13.2.1 — Candidate-report submitted state | Fails closed by | 1 | NOT DECIDED |
| C-24.13.2.1 — Candidate-report submitted state | Fed by | 1 | NOT DECIDED |
| C-24.13.2.1 — Candidate-report submitted state | Gated by | 1 | NOT DECIDED |
| C-24.13.2.2 — Candidate-report verification_pending state | Fails closed by | 1 | NOT DECIDED |
| C-24.13.2.2 — Candidate-report verification_pending state | Fed by | 1 | NOT DECIDED |
| C-24.13.2.2 — Candidate-report verification_pending state | Gated by | 1 | NOT DECIDED |
| C-24.13.2.3 — Candidate-report technically_blocked state | Fed by | 1 | NOT DECIDED |
| C-24.13.2.3 — Candidate-report technically_blocked state | Gated by | 1 | NOT DECIDED |
| C-24.13.2.4 — Candidate-report verified_self_establishing terminal state | Fails closed by | 1 | NOT DECIDED |
| C-24.13.2.4 — Candidate-report verified_self_establishing terminal state | Fed by | 1 | NOT DECIDED |
| C-24.13.2.4 — Candidate-report verified_self_establishing terminal state | Gated by | 1 | NOT DECIDED |
| C-24.13.2.5 — Candidate-report evaluated_and_set_aside terminal state | Fed by | 1 | NOT DECIDED |
| C-24.13.2.5 — Candidate-report evaluated_and_set_aside terminal state | Gated by | 1 | NOT DECIDED |
| C-24.14.1 — Connection current-use resolution requirements | Fed by | 1 | NOT DECIDED |
| C-24.14.1.1 — Current-use exact accepted-record identity | Fed by | 1 | NOT DECIDED |
| C-24.14.1.1 — Current-use exact accepted-record identity | Gated by | 1 | NOT DECIDED |
| C-24.14.1.2 — Current-use complete later-event chain | Fed by | 1 | NOT DECIDED |
| C-24.14.1.2 — Current-use complete later-event chain | Gated by | 1 | NOT DECIDED |
| C-24.14.1.3 — Current-use event integrity | Fed by | 1 | NOT DECIDED |
| C-24.14.1.3 — Current-use event integrity | Gated by | 1 | NOT DECIDED |
| C-24.14.1.4 — Current-use event owner and authority | Fed by | 1 | NOT DECIDED |
| C-24.14.1.4 — Current-use event owner and authority | Gated by | 1 | NOT DECIDED |
| C-24.14.1.5 — Current-use applicable relationship version | Fed by | 1 | NOT DECIDED |
| C-24.14.1.5 — Current-use applicable relationship version | Gated by | 1 | NOT DECIDED |
| C-24.14.1.6 — Current-use proposed state resolution | Fed by | 1 | NOT DECIDED |
| C-24.14.1.6 — Current-use proposed state resolution | Gated by | 1 | NOT DECIDED |
| C-24.14.1.7 — Current-use original certainty preservation | Fails closed by | 1 | NOT DECIDED |
| C-24.14.1.7 — Current-use original certainty preservation | Fed by | 1 | NOT DECIDED |
| C-24.14.1.7 — Current-use original certainty preservation | Gated by | 1 | NOT DECIDED |
| C-24.14.1.8 — Current-use privacy authorization | Fed by | 1 | NOT DECIDED |
| C-24.14.1.9 — Current-use influence-removal check | Fed by | 1 | NOT DECIDED |
| C-24.14.2 — Proposed connection current_use_state | Fails closed by | 1 | NOT DECIDED |
| C-24.14.2 — Proposed connection current_use_state | Gated by | 1 | NOT DECIDED |
| C-24.14.2.1 — Proposed connection current use state | Fails closed by | 1 | NOT DECIDED |
| C-24.14.2.1 — Proposed connection current use state | Fed by | 1 | NOT DECIDED |
| C-24.14.2.1 — Proposed connection current use state | Gated by | 1 | NOT DECIDED |
| C-24.14.2.2 — Proposed connection disputed use state | Fails closed by | 1 | NOT DECIDED |
| C-24.14.2.2 — Proposed connection disputed use state | Fed by | 1 | NOT DECIDED |
| C-24.14.2.2 — Proposed connection disputed use state | Gated by | 1 | NOT DECIDED |
| C-24.14.2.3 — Proposed connection corrected_or_superseded_for_current_use state | Fed by | 1 | NOT DECIDED |
| C-24.16.1 — Proposed connection-output output_operation_id reference | Fails closed by | 1 | NOT DECIDED |
| C-24.16.1 — Proposed connection-output output_operation_id reference | Fed by | 1 | NOT DECIDED |
| C-24.16.1 — Proposed connection-output output_operation_id reference | Gated by | 1 | NOT DECIDED |
| C-24.16.2 — Proposed connection-output delivery_idempotency_key reference | Fed by | 1 | NOT DECIDED |
| C-24.16.2 — Proposed connection-output delivery_idempotency_key reference | Gated by | 1 | NOT DECIDED |
| C-24.16.3 — Proposed connection-output delivery_attempt_id reference | Fails closed by | 1 | NOT DECIDED |
| C-24.16.3 — Proposed connection-output delivery_attempt_id reference | Fed by | 1 | NOT DECIDED |
| C-24.16.3 — Proposed connection-output delivery_attempt_id reference | Gated by | 1 | NOT DECIDED |
| C-24.17 — Connection crash and restart recovery | Gated by | 1 | NOT DECIDED |
| C-24.17.1 — Connection crash before proposal reservation | Fed by | 1 | NOT DECIDED |
| C-24.17.1 — Connection crash before proposal reservation | Gated by | 1 | NOT DECIDED |
| C-24.17.2 — Connection crash after identity reservation | Fed by | 1 | NOT DECIDED |
| C-24.17.2 — Connection crash after identity reservation | Gated by | 1 | NOT DECIDED |
| C-24.17.3 — Connection crash after proposal commitment | Fed by | 1 | NOT DECIDED |
| C-24.17.3 — Connection crash after proposal commitment | Gated by | 1 | NOT DECIDED |
| C-24.17.4 — Connection crash during undecided waiting | Fed by | 1 | NOT DECIDED |
| C-24.17.4 — Connection crash during undecided waiting | Gated by | 1 | NOT DECIDED |
| C-24.17.5 — Connection crash after proposal display | Fed by | 1 | NOT DECIDED |
| C-24.17.5 — Connection crash after proposal display | Gated by | 1 | NOT DECIDED |
| C-24.17.6 — Connection crash after durable Ness input | Fed by | 1 | NOT DECIDED |
| C-24.17.7 — Connection crash after acceptance before checkpoint | Fed by | 1 | NOT DECIDED |
| C-24.17.7 — Connection crash after acceptance before checkpoint | Gated by | 1 | NOT DECIDED |
| C-24.17.8 — Connection unknown accepted-commit outcome | Fed by | 1 | NOT DECIDED |
| C-24.17.9 — Connection crash during source verification | Fed by | 1 | NOT DECIDED |
| C-24.17.9 — Connection crash during source verification | Gated by | 1 | NOT DECIDED |
| C-24.17.10 — Connection crash after verified source before commit | Fed by | 1 | NOT DECIDED |
| C-24.17.11 — Connection crash during rule match | Fed by | 1 | NOT DECIDED |
| C-24.17.11 — Connection crash during rule match | Gated by | 1 | NOT DECIDED |
| C-24.17.12 — Connection crash before final rule revalidation | Fed by | 1 | NOT DECIDED |
| C-24.17.12 — Connection crash before final rule revalidation | Gated by | 1 | NOT DECIDED |
| C-24.17.13 — Connection crash after rule revalidation | Fed by | 1 | NOT DECIDED |
| C-24.17.14 — Connection crash during rejection | Fed by | 1 | NOT DECIDED |
| C-24.17.14 — Connection crash during rejection | Gated by | 1 | NOT DECIDED |
| C-24.17.15 — Connection crash after rejection before suppression checkpoint | Fails closed by | 1 | NOT DECIDED |
| C-24.17.15 — Connection crash after rejection before suppression checkpoint | Fed by | 1 | NOT DECIDED |
| C-24.17.15 — Connection crash after rejection before suppression checkpoint | Gated by | 1 | NOT DECIDED |
| C-24.17.16 — Connection crash while adding pending new evidence | Fed by | 1 | NOT DECIDED |
| C-24.17.16 — Connection crash while adding pending new evidence | Gated by | 1 | NOT DECIDED |
| C-24.17.17 — Connection crash while creating a linked post-rejection proposal | Fed by | 1 | NOT DECIDED |
| C-24.17.17 — Connection crash while creating a linked post-rejection proposal | Gated by | 1 | NOT DECIDED |
| C-24.17.18 — Connection crash during correction or dispute | Fails closed by | 1 | NOT DECIDED |
| C-24.17.18 — Connection crash during correction or dispute | Fed by | 1 | NOT DECIDED |
| C-24.17.18 — Connection crash during correction or dispute | Gated by | 1 | NOT DECIDED |
| C-24.17.19 — Connection crash during accepted retrieval use | Fed by | 1 | NOT DECIDED |
| C-24.17.20 — Connection crash during pending investigation use | Fed by | 1 | NOT DECIDED |
| C-24.17.20 — Connection crash during pending investigation use | Gated by | 1 | NOT DECIDED |
| C-24.17.21 — Connection crash during Person-Box consumption | Fed by | 1 | NOT DECIDED |
| C-24.17.22 — Connection record and actual-owner contradiction | Fed by | 1 | NOT DECIDED |
| C-24.17.22 — Connection record and actual-owner contradiction | Gated by | 1 | NOT DECIDED |
| C-24.18 — Connection technical retry boundary | Fed by | 1 | NOT DECIDED |
| C-24.19 — Connection interface contracts | Gated by | 1 | NOT DECIDED |
| C-24.19.1 — Connection I1 direct-source interface | Fed by | 1 | NOT DECIDED |
| C-24.19.3 — Connection I3 source-verification interface | Fed by | 1 | NOT DECIDED |
| C-24.19.4 — Connection I4 Ness-decision interface | Fed by | 1 | NOT DECIDED |
| C-24.19.9 — Connection I9 correction-dispute interface | Fed by | 1 | NOT DECIDED |
| C-24.20.1 — Connection operational child-kind placement | Fails closed by | 1 | NOT DECIDED |
| C-24.20.1 — Connection operational child-kind placement | Gated by | 1 | NOT DECIDED |
| C-24.21 — Connection fail-closed outcomes | Gated by | 1 | NOT DECIDED |
| C-24.21.1 — Invalid connection record contract failure | Fed by | 1 | NOT DECIDED |
| C-24.21.1 — Invalid connection record contract failure | Gated by | 1 | NOT DECIDED |
| C-24.21.2 — Unavailable connection store or source owner failure | Fed by | 1 | NOT DECIDED |
| C-24.21.2 — Unavailable connection store or source owner failure | Gated by | 1 | NOT DECIDED |
| C-24.21.3 — Missing connection interface truth or recovery identity failure | Fed by | 1 | NOT DECIDED |
| C-24.21.3 — Missing connection interface truth or recovery identity failure | Gated by | 1 | NOT DECIDED |
| C-24.21.4 — Connection required-audit commitment failure | Fed by | 1 | NOT DECIDED |
| C-24.21.4 — Connection required-audit commitment failure | Gated by | 1 | NOT DECIDED |

## Plain-gate and empty-box review

Each card was compared with its own adjacent boxes and source scope. Explicit prohibitions, actual failures and source gates remain distinct; required record fields are not invented authorization gates. Indefinite waiting and pure record slots have no fabricated failure or external gate. The source's real not-applicable interface/recovery cells remain explicit. Final route privacy/authority, investigation marking, source verification, all ten Ness recovery conditions and all nine current-use requirements are named where they actually gate behavior. Direct proof, selected input, final decision, accepted record and use log remain different facts. Proposed qualifiers accompany proposed names; output identities are consumed references with their owner retained. Every internal edge and reverse USED BY entry is checked, and each row names one place. Earlier incoming C-7B/C-7L relations are matched without editing those files. No component is newly stamped BUILT. All empty restriction/failure/gate boxes are reviewed against surrounding source-derived behavior. The source spelling conflict is retained explicitly rather than normalized.

| Card | Plain gate justification |
|---|---|

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

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH06-a

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §7J / SIX CLASH TYPES | Six exact kinds and their defining differences | C-7J.1 and C-7J.1.1–C-7J.1.6 |
| V10 §7J / GENUINE CONTRADICTION VS CONTEXTUAL DIFFERENCE | Simultaneous truth under the same conditions, person, time and context; no resolution | C-7J.2 |
| V10 §7J; Bundle 3 §10 | Original clash and all eleven fields; telling pointers and source chains | C-7J.3 and C-7J.3.1–C-7J.3.11 |
| V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE | Triggered comparison scope; wider scope; bounded/configurable periodic scanning; no authority by mode | C-7J.4, C-7J.4.1, C-7J.4.2 |
| Bundle 3 §10 | Conflicting-item set plus aspect; match/no-match; one commit path; crash recovery from committed records | C-7J.5 |
| Bundle 3 §10 | Detection-history event: mode, time, configuration, confidence; no duplicate or extra weight | C-7J.5.1 and C-7J.5.1.1–C-7J.5.1.4 |
| V10 §7G-A / claim validation, Step 7, checkpoint 7A, sentinels and RC-6/RC-7 | Operation key; recover before rerun; no_clash_sentinel; system failure keeps job in_progress; checkpoint handoff | C-7J.5.2; exact claim/checkpoint/sentinel fields remain the existing C-7GA cards in CH05-b |
| V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT | Seven response fields; eight stated type alternatives; multiple responses; separate linked downstream actions | C-7J.6 and C-7J.6.1–C-7J.6.7 |
| Bundle 3 §8 | Recording never blocked; six downstream uses; qualified support; no clear current view; permanent clash; new linked refinements | C-7J.7, C-7J.7.1, C-7J.7.2 |
| Bundle 3 §17 | Distinct weightless reading response and clash response | C-7J.7.3; full reading-affirmation mechanics left to CH08-f |
| Bundle 3 §16 | Clash marker; detail pane; respond only; explicitly recorded named absence; plain main surface and precise side notes | C-7J.8 and C-7J.8.1–C-7J.8.3 |
| V10 §0B; Bundle 3 §19 | One real operation, one record; no recursive logging or double evidence; presentation/response log contents | C-7J.9 and C-7J.9.2 |
| A2 §§5A.1, 5A.3, 6, 10 | Canonical telling identity, semantic eligibility, blocked/skip/resume provenance; no private payload or double evidence | C-7J root, C-7J.3.3, C-7J.9.1; existing C-READ.10.10 and C-READ.10.14 reused |
| V10 §7Q; Bundle 3 §20 | Purpose-specific internal-use versus visible-output boundary; protection and identity gates | Current authorization boxes; full privacy architecture left to CH08-a |
| V10 §§7D, 7M; MAP C-7J | State evidence and current-view handoffs with conflict preserved | C-7J and cross-piece continuations; full consumers left to CH06-d/f |
| Bundle 6 mechanical §12 | Authorized clash-read result contains records and Ness responses with component provenance | C-7J USED BY C-LMAC; full query protocol left to CH08-c |
| Bundle 3 acceptance receipt; A2 package-complete receipt; Bundle 6 mechanical receipt | Exact accepted package identities/status, no new behavior | READ RECORD; receipt workflow/history excluded under §1.3 |
| Decision Defaults §§3G–3H; Companion §7J | Authority comparison and repeated conceptual clash content | No independent extra mechanism; current C-7J placement follows V10 and accepted scoped additions |
| Active decision index v0_11; A2 current-status note; September 24 recovery record and September 25 buckets | Navigation, dependency and restoration-scope checks | No behavior from the index or ledger; non-clash restored memory-health scope retained for later owners |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH06-b

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §7K responsibilities and must-nevers; MAP C-7K | Unaltered receipt, perspective/theme/time organization, query scope, no narrative synthesis or winner | C-7K |
| V10 §7K / TELLING VS ONGOING STORY | One pass/root/perspective/moment; collection with agreements, shifts, contradictions and silences | C-7K.1 |
| V10 §7K / CONNECTIONS ACROSS TIME; A2 §8 | Five shared-attribute routes; labeled basis and root/reading pointers; temporal change distinct from contradiction | C-7K.2 |
| V10 §7K / STRUCTURED PERSPECTIVE MODEL; A2 §3 | Three required roles, optional attribution chain, five evidence relationships, unresolved attribution, separate engine lens, v1 whose compatibility | C-7K.3; shared field cards C-READ.10.1.4–C-READ.10.1.8 retained |
| A2 §§5A–6 and §8 | Immutable telling_id, Story Layer ownership, complete-set gate, zero-telling, no embedded/partial substitute, new IDs on reread | C-7K.4 and current interface fields; existing C-READ persistence/recovery atoms retained |
| V10 §7K / FIRMNESS RULE; firmness policy §§1–6 | Six qualitative outcomes with criteria, mandatory basis and hierarchy, no score, independent reading confidence, less-claiming/omission/revision rules | C-7K.5; existing C-READ.10.1.11 and C-READ.10.1.12 atoms retained |
| V10 §7K / HYBRID THEME SYSTEM | Engine proposes, only Ness confirms; indefinite unresolved status, no circularity or confirmation by repetition/time | C-7K.6 |
| Bundle 3 §11 / Theme record | Stable ID, vocabulary label, status, proposer, creation time, append-only versions | C-7K.6.1 and six field cards; two status cards under C-7K.6.1.3 |
| V10 §7K / HYBRID THEME SYSTEM | Each proposal's root IDs, telling/reading IDs, proposer, why connected, timestamp and uncertainty | C-7K.6.2 and four support atoms; proposer/time reuse C-7K.6.1.4–C-7K.6.1.5 |
| A2 §7; Bundle 3 §11 / Membership links | Non-exclusive telling_id membership and five provenance fields; no copy/move/fact; legacy unconfirmed | C-7K.6.3; existing C-READ.10.14.8 and its atoms retained |
| Bundle 3 §11 / Grouping and Aliases | Member sets, alias families, root support, no circularity, bidirectional new alias records | C-7K.6.4 and C-7K.6.5 |
| Bundle 3 §11 / Theme actions | Confirm, reject, rename, merge, split, leave unresolved; event inputs/results and preservation boundaries | C-7K.6.6 and C-7K.6.6.1–C-7K.6.6.6 |
| V10 §7K; A2 §7; Bundle 3 §11 / Influence honesty | Actual influence recorded in why-admitted retrieval provenance; no policy invented; later reading free to disagree | C-7K.6.7; full retrieval owner CH05-c and full relevance owner CH08-b |
| Bundle 6 policy §4 A3.5 | Holding through linked separate objects; Ness understanding visibly distinct; no second profile/store or fact by strength | C-7K.7; Person-Box implementation scope left to CH06-c |
| V10 §0B; MAP C-7K; Bundle 3 §§18–20 | Per-operation logging, immutable records, privacy/identity authorization, no double evidence | C-7K.8 and current gates; full protection mechanisms left to CH08-a/CH09-d |
| A17 §7; Bundle 6 mechanical §12 | Wonder possibility cannot enter stories as observed reality; LMAC returns perspective-owned tellings with clashes | C-7K boundary and USED BY interface; full Wonder remains C-7B and full LMAC remains CH08-c |
| Accepted firmness, Bundle 3, A2 and Bundle 6 receipts; A17 receipt | Exact package identities and accepted scoped status; no new behavior | READ RECORD; receipt workflow/history excluded under §1.3 |
| DD §3G; Companion §7K; Bundle 1 normalization firmness identity; active indices and A3 working record | Authority/status and dependency comparison | Current behavior follows V10 plus accepted scope; no index/working-note mechanism imported |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH06-c

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §7L responsibilities, must-nevers and link types; MAP C-7L | Stable identity gather, eight source families, provenance, no profile/fact/closure and CY-A use | C-7L |
| V10 §7L link fields; Bundle 3 §§7/12 | What, why, who established, certainty, timestamp; four ordinary qualitative outcomes | C-7L.1 and field/outcome children |
| V10 §7L uncertain identity; Bundle 3 §§7/12 | Label/name, where, when, evidence, current outcome; indefinite unconfirmed anchors | C-7L.2 and five field cards |
| V10 §7L proposal-based creation; Bundle 3 §§7/12 | Stable ID; separate names/labels/roles; four search scopes with occurrence/scope recorded | C-7L.3.1–C-7L.3.3.4 |
| Bundle 3 §7 | Completely clear and definitely identifiable as the same person; automatic met-test action, pending unmet-test action, no scores or added manual approval | C-7L.3.4 and C-7L.3.5; outcome atoms under C-7L.1.4 |
| V10 §7L; Bundle 3 §§7/12/18 | Confirm, reject, rename, keep unresolved, link to existing, propose merge; preserve history | C-7L.3.6 and six response cards |
| Bundle 3 §12 | Seven append-only event kinds; candidate pair, gathered evidence, named gap; non-destructive joins and wrong-join corrections | C-7L.3.7 and event/proposal-field children |
| Bundle 3 §9 | Ness's confirmed stable ID, settled-fact provenance, clear first-person source links, ambiguous pasted-I pending, ordinary maintenance | C-7L.4 |
| V10 §7L default view; Bundle 3 §§13/15 | Seven headed sections with contents/status lines; compact and expandable records; newest usable; chronology; grouping-only responses/supersession; best-supported delegation | C-7L.5 and seven section cards; full Current/History owner CH06-e |
| Bundle 3 §15 | Five visibly active composable filters, clear-to-default, one-switch chronology, owner labels and pointer-only expansion | C-7L.5.8–C-7L.5.11 with filter atoms |
| Bundle 3 §16 | Clash marker/detail/respond, separate events; named absent item/kind, no inferred content; plain main wording and side notes | C-7L.5.4 and C-7L.5.7; shared C-7J.8/C-7J.8.3 retained |
| Bundle 3 §14 | Per-element batch identity, cross-batch identity tag, one ID view, no seal writes, ordinary tests across batches | C-7L.6 and two provenance fields |
| Bundle 6 policy §4 A3.5 | Holding through separate existing objects; Ness's understanding distinct; no fact by repetition, recency or strength | C-7L.7; existing C-7K.7 retained; exact layout still open |
| V10 §7L; Bundle 6 closeout §9; B15 §11; A16 retained archive boundary | Safe held metadata/state/blockers only; raw content excluded; sealed TSC has no inspection path | C-7L.8 and current C-7E.11 reciprocal; full archive owner C-TSC retained |
| V10 §§25.2/25.4; Bundle 6 mechanical §12 | PBR path through LMAC, seven initial categories, presence condition, version refresh and query failure to guest; separate parents and visibility | C-7L.9 and four interface cards; full PBR/access lifecycle CH09-b/d |
| V10 §25.3 voice-profile architecture and minimum linking evidence | Separate identity authority and six ordinary unknown-speaker prerequisites; empirical minima remain open | C-7L.10 and six prerequisite cards; full SIA CH09-c |
| B-INT-7 §§12A/13/14/19 | Provisional enrollment type, certainty, stable proposal ID, meaning, basis and exact reference fields; owner commit; replay lookup; six handoff outcomes | C-7L.11 and field/result children; full enrollment/SIA internals CH09-h/c |
| B-INT-8 §§12C/14/15 | Ten identity-separation rules; nine current-use checks; three proposed current-use result meanings; fail closed; route privacy and influence removal | C-7L.12 consumer boundary; full current-use records/states remain CH06-g |
| Bundle 6 mechanical §12 | Authorized box-ref query and actual certainty; PBR route; minimum authorization metadata before protected release | C-7L.13; full LMAC CH08-c |
| V10 §0B; MAP C-7L; Bundle 3 §§18–20 | One append-only record per real operation, search/evidence basis, presentation version/filters/history, no evidence inflation | C-7L.14 and current gates |
| A2 §§5A/6; A17 §7 | Complete telling-set semantic gate; first-class telling_id references; Wonder cannot become observed reality about a person | C-7L current root and telling interfaces; existing C-READ and C-7B owners retained |
| A7/B7 current-surface privacy; A26/B-INT-5 identity/access; Bundle 5 closeout | Purpose-bound privacy and visibility, per-surface hiding obligation, PBR read boundary; no imported access or privacy authority | Current gates and C-7L.5 failure boundary; complete mechanisms retain CH08-a/CH09 ownership |
| DD §3G; Companion §7L; accepted receipts; active indices/working records; September 25 Group 6 | Authority/status comparison and identity checks; restored thin-evidence query retains its existing owner | READ RECORD and source dispositions; no workflow or index text used as behavior |
| Bundle 4; Bundle 2; A19; Five Framework; operation kernel; future/intent notes | Other-owner links, derived presentation and identity-authority boundaries | Named later ownership in scope dispositions; no full package-completion claim |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH06-d

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §7M; MAP C-7M | Internal current-picture purpose, source preservation, quiet use, deliberate inspection, honest no-clear-view, current/history and downstream direction | C-7M/C-7M.1 with existing C-7A/C-7I/C-7N relationships |
| V10 §7M seven-factor priority order | Seven ordered factors, direct support over frequency/confidence, context provenance, beside-item conflict, recency last, no collapsed score | C-7M.2 and seven factor children |
| Bundle 4 §8.1 | Nineteen conceptual profile fields, immutable versions, exact tier references, declared rules/triggers/invalidation, version/time/log history | C-7M.3 and field/rule children |
| V10 §7M update timing; Bundle 4 §8; Bundle 2 §7 | Opening, manual refresh and materially relevant event routes; six material-event kinds; no unrelated global update | C-7M.4 with trigger children; C-7M.10.7 |
| Bundle 4 §8.2 | Immutable snapshot fields, ten source-reference families, direct-root pointers, separate factors, omissions/reasons, prior/change/why, committed completeness, privacy/log references | C-7M.5 and fields; exact profile/version/derivation/time/log atoms reused from C-7M.3 |
| Bundle 4 §§8.3–8.4 | Eleven refresh-event fields; standing/staleness from latest valid applicable events only; five outcomes and their distinct consequences | C-7M.6/C-7M.7 and children; shared operation_id/created_at/log references reused |
| Bundle 4 §§8.5–8.6 and §13 | Operation plus source/version identity, at most one snapshot, event-only null/failure/incomplete, six crash/recovery cases, technical retries by reference | C-7M.8/C-7M.9 with six recovery cases; existing B9 owners retained |
| Bundle 2 §§5.1–5.2 and §7; A4 §3 | Proposed declaration identity/version, controlled purpose, target, candidate families, tier ownership and complete validity | C-7M.10.1–C-7M.10.3 and root; candidate family field reused; C-7F.6.14 validity retained |
| Bundle 2 §7 | Deterministic object-type gate, conditional declared-time gate; no universal thread/precedence gates | C-7M.10.4 and two gate children |
| Bundle 2 §§5.2–5.3 and §7 | All nine dimensions with producers, version provenance and applicability; honest missing/inapplicable outcomes | C-7M.10.5 and nine selection children; shared absence atom retained |
| Bundle 2 §§5.3/7 | Explicit none mouth authorization; future dimension-specific version/validation conditions; no precompute or continuous evaluation | C-7M.10.6/C-7M.10.7; full validation architecture remains CH08-b |
| Bundle 2 §7 Tier 2; §4 quiet-use/material-uncertainty rules | Factor 4 only, attached uncertainty/source/older-pattern labels, honest fallback, quiet internal use and downstream uncertainty disclosure | C-7M.10.8/C-7M.10.9 and consequence children |
| Bundle 2 §5.3 proposed shared uncertainty rule | Validated is interpretation; failed unused; weak unresolved/disputed clues; seven prohibited sole consequences; checks allowed; disagreement record; honest absence | C-7M.10.9.4 with existing C-7F.6.10.5.1–.5 outcome owners |
| Bundle 2 §§5.5–5.7 and §7; Bundle 4 §§11–12 | Privacy-first authorized families, no feedback into state, no self-evidence/access widening; evaluation record; no snapshot for invalid profile/declaration; unknown-purpose halt | C-7M.10.10–C-7M.10.12; full relevance record/vocabulary ownership CH08-b |
| Bundle 4 §14.1; V10 §0B; September 25 Group 10 | One connected operation log, actual evaluated/used/unused/omitted/outcome/retry/recovery/prior-use/result content, no recursive logging or extra evidence | C-7M.11/C-7M.11.1; existing C-7B.10.2/.3/.5/.8 retained |
| Bundle 4 §§9.1/13/14.1 | Domain operation keeps its physical-effect level; log append separate linked Level 2 under same identity, no merged accounting | C-7M.11.2 |
| Bundle 4 §14.2 | Initial active without exception; five active protections; absence not sufficient to cool; fixed component-owned versioned rule; future change evidence and Ness approval | C-7M.11.3.1 with five protection children; C-7M.11.3.2; existing generic rule-change atoms retained |
| Bundle 4 §14.2 | Both cooling conditions, priority-only change, exact retrieval preserved; actual-use/valid-link reactivation only; uncertain evaluation preserves prior state | C-7M.11.3.3–C-7M.11.3.5; existing C-7B.10.6 condition atoms retained |
| Bundle 4 §§14.3–14.4 | Fourteen lifecycle-event fields, active/cold only, initial previous_status empty, failed evaluation not a third status; three distinct record kinds | C-7M.11.4 fields plus shared operation/time/log atoms; C-7M.11.5 |
| Bundle 4 §§7.2/8/11–12/14 | Evidence family counts one independent event, all members individually preserved, logs no extra vote; strict state-to-view-to-action direction | C-7M.2.2/current boundaries; full evidence-family schema CH06-f |
| Bundle 6 policy §4 A13.2; mechanical §6 | Relevant provisional influence only through own operation's provisional_material_used entry; visible provisional context, exact record/status-at-use, no confirmation by repetition | C-7M.12; existing C-CREATE.8.1/.8.5 owners retained; fixed-family representation remains an explicit gap |
| V10 §7M; Bundle 2 §7; Bundle 6 closeout §9; B15/A16 archive isolation | Safe held metadata/state/blockers only; no raw influence/ranking/snapshot/output or TSC inspection | C-7M.13 and C-7M.5.5.10; C-7E.11 source reciprocal present |
| A2 §§5A/6; Bundle 3 §§8/13/16 | Complete-set telling eligibility, first-class reference use, conflicted support and requested best-supported person picture | Current root and factor/source interfaces; existing telling/clash/person atomic owners retained |
| A4; B7; B-INT-5/B-INT-7; AIC; Bundle receipts; DD/Companion; active indices; recovery ledger | Current scope and authority comparison, protected-surface/identity limits, package status, other-owner snapshot terms, ledger-only tracking | READ RECORD and scoped dispositions; no unrelated authority/session snapshot mechanism imported |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH06-e

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §7I; MAP C-7I | Two views, simple/default and complete/on-demand, source preservation, newest-usable versus best-supported, output-to-Ness destination | C-7I root and Current/History cards |
| Bundle 3 §13 current usable | Acceptance passed AND not rejected AND not insufficient_context; usable is not true/final | C-7I.1.1 with three condition atoms; acceptance mechanism retains C-7G |
| Bundle 3 §13 Current grouping | Newest usable first per root and applicable person/theme grouping; three visible status kinds | C-7I.1/C-7I.1.2 and three label cards; C-7I.3 grouping scope |
| Bundle 3 §§8/13/16 | Conflict beside item, qualified/withheld weak support, exact detail and respond-only path, no winner or suppression | C-7I.1.3; existing C-7J.8.1/.8.2 retained |
| V10 §7I; Bundle 3 §13 | Best-supported or broader current-picture claim invokes seven factors, recency limited to tie-break | C-7I.1.4; current C-7M/C-7M.2 references |
| V10 §7I; Bundle 3 §13 | Complete strict chronology, always available, one switch away; optional mode grouping cannot hide history | C-7I.2/C-7I.2.1/C-7I.3 |
| Bundle 3 §§8/13/17 | Responses and changed/replaced flags alter grouping/labels only; separate weightless responses, no response means no change/block; changed judgment new event; dismissal current-use route | C-7I.4 with two input children; full B-AFFIRM event fields remain CH08-f |
| Bundle 3 §15; MAP C-7I | Shared seven-section discipline, filters visible/composable/clear-to-default, chronology and owning-layer labels, complete-on-demand pointers, no synthesis/person score | C-7I.5; existing C-7L.5 and descendants retained |
| Bundle 3 §16 | Explicit named absence and owning-layer kind only, no inferred content or proof; plain main wording and precise side notes | C-7I.6/C-7I.7; named-gap atom remains C-7J.8.3 |
| MAP C-CREATE; Bundle 6 mechanical §6 | Store-backed creation views, provisional-plus-history ideas in progress, no display-derived confirmation, unverifiable status provisional | C-7I.8; existing C-CREATE status/view owners retained |
| MAP C-7I; Bundle 3 §19; V10 §0B | One log per real view/named-gap presentation; snapshot/version, filters, History switches; no evidence inflation; access gates | C-7I.9 with three record-content fields; existing general Log atoms retained |
| Bundle 3 §20; B7 §15.4 | Privacy before surfacing, normal-inspection surface hiding, protective unverified/blocked/failed/partial withholding, visible suppression distinct from influence removal | C-7I.10 and root failure boundary; complete B7 record/lifecycle/verification/restoration owners remain CH08-a |
| B10 §5 proposed RR-PR | Post-commit view/index projection consumes a new layer, rebuildable idempotently, never gates success or owns status | C-7I root current-use boundary; C-7H.3.7 retained |
| DD §3G; Companion §7I; Bundle 3 receipt; active indices; recovery ledger; future-feature note | Status/authority comparison, acceptance identity, current scope and later intent/pending-restoration navigation | READ RECORD and source dispositions only; no history or workflow imported as behavior |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH06-f

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §7D; MAP C-7D; DD §3G; Companion §7D | Eight structural families, grounding and independent currency, inputs/governors/downstream uses, privacy, no path choice, exact open slots | Root and C-7D.1–.8; currentness/common contract; later-owner boundaries |
| Bundle 4 §4A | Four qualitative A31 labels and less-claiming discipline | C-7D.9.5/.9.20; existing C-7G.8 labels reused |
| Bundle 4 §4B decisions NHD-A6-1/NHD-A6-2/NHD-A6-3; §5; §7 | Automatic permitted observation, direct-self-report/several-sign inference, evidence/materiality separation, routine currency without manual approval | C-7D.1/.10/.11 and their condition/transition cards |
| Bundle 4 §4B decisions NHD-A6-4/NHD-A6-5; §7 | Separate simultaneous positions, grounded tension, causal hypotheses, alternatives and separately grounded chain links | C-7D.2/.3/.6 and field children |
| Bundle 4 §4B decision NHD-A6-6; §5; §7 | Core vocabulary, automatic grounded precise description, broader category, search-before-create | C-7D.12 and three fields; C-7D.11.10 matching |
| Bundle 4 §4B decision NHD-A6-7; §7 | Needs/fears careful possibilities, several signs, stronger protected-boundary basis and protection marker, scoped practical constraints | C-7D.8.1–.8.4 and schema fields |
| Bundle 4 §4B decision NHD-A6-8; §7 | Five separate grounded/currentness capacity slots, optional supported overall summary and supporting-dimension list; no emotion/wellbeing/identity conflation | C-7D.13 and dimensional/summary fields |
| Bundle 4 §4B decision NHD-A6-9; §5; §7 | Six currency states, five aging factors, dated reasoned events, assessments, no hidden decay/time-only ending | C-7D.10 with states/events/aging factors/assessment fields |
| Bundle 4 §4B decision NHD-A6-10; §5; §7; Bundle 2 §10 | Review prompt versus inspected evidence, recorded reason, uncertain suggestion, no blanket reread, exact authorization remains open | C-7D.14/.14.1 and trigger fields; C-7D.11.4 |
| Bundle 4 §4B decision NHD-A6-11; §7; accepted A17 §7 | Automatic internal hypothetical paths, four purposes, evidence/assumptions/marker/flag, no self-evidence/action permission/history rewrite, simulation approval boundary | C-7D.7 and five fields; later simulation scope preserved |
| Bundle 4 §4B mechanical domains; §7 | Relationship/safety attribution, stable Ness identity, proposed cross-time continuity, movement separate from cause/ending/supersession | C-7D.5/.5.1/.15; transition and hypothesis structures |
| Bundle 4 §7 common contract | All common provenance/time/grounding/currency/uncertainty/history/authority/operation fields | C-7D.9.1–.9.17; C-7D.10; existing C-7M.5.2 reused |
| Bundle 4 §7 evidence family and grounding chain | Separate preserved same-event members, one independent unit per family, every chain link retained, no operational second vote | C-7D.9.18 and identifier/member/count atoms; C-7D.9.19 |
| Bundle 4 §7 state lifecycle | Creation, accumulation, review, reassessment, promotion, stale/unknown, end/supersession, new-version reactivation, linked correction, five episode-match outcomes, incomplete and omission failures | C-7D.11 and lifecycle/matching children; C-7D.9.20; C-7D.17 recovery |
| Bundle 4 §4D; §6; §7 | Layered active core/wider knowledge, nine structural distinctions, nine grouped qualifying basis kinds, multiple independent bases, world entity/condition/self↔world families | C-7D.16.1–.16.4/.16.7 and boundary/basis children |
| Bundle 4 §6; §7 membership event/lifecycle | All fifteen membership fields, two policy states, separate dimension, grounded activation, cessation plus no other basis, idempotency, precommit/missing-log/unsafe outcomes | C-7D.16.5/.16.6; existing operation/time/log fields reused |
| Bundle 2 complete §10; shared §5.1–§5.7 | Proposed RM-LS-01 v1_0, thirteen declaration fields, six candidate families, selected gates and six producers, no mouth/currentness dimension, on-demand timing, Tier 2 and three failure classes | C-7D.14.2 and children; existing A4 validity, gate and proposed T2-UNRES-SHARED atoms retained |
| Bundle 4 §§11–12; A2 §§5A/6; B3 identity/firmness interfaces; A7/B7 consumer boundary | Permitted evidence fan-in, target telling IDs and complete-set gate, governors not evidence, held-raw/TSC exclusion, internal/visible authorization and third-party rules | Root and common grounding, relation/person/telling interfaces; full privacy remains CH08-a |
| Bundle 4 §§13–14 | Stable identity/source version/idempotent commitment, startup/partial/reconciliation/retry/uncertainty, one log per operation, separate level accounting, five active protections, two cooling conditions, use/link reactivation, fourteen event fields and three record kinds | C-7D.17 and current consumer cards; existing B9 and shared C-7M log/lifecycle atoms retained |
| Accepted room-start §6; active UE5 §2.3; branch/simulation intent §3B.6; framework §§18–21 | Presentation cannot rewrite Living State; actual/history versus simulation distinction; future index/interface scope | C-7D.16.3.7 non-effect; other mechanisms left to their named later owners |
| Acceptance/closure receipts; active A2 status and decision indices; recovery ledger | Accepted package identities and older-open-slot navigation, intent status and restoration-only tracking | READ RECORD and dispositions; no workflow or recovered historical behavior imported |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.

## READ RECORD

The source pin remains 6a7160ba688ba4e433a31899162815df7e2bab17. Contract/lessons/run instructions were reopened, including the full header and delivery/check requirements. The B-INT-8 primary package and closure receipt were read whole; the other entries are accurately scoped reopens or retained prior credits. Earlier chapter fingerprints remain recorded below.

| Source file | Reading scope / whole-file credit | SHA-256 |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: complete §24, including every responsibility, route, pending-use and five-source-type paragraph; no full-Master credit. | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped: complete C-24 and B-INT-8 integration entry; bounded R8 and existing live-path scope retained. | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Scoped: complete §3J connection capability and older integration status comparison. | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Scoped: complete §24 conceptual connection responsibility and certainty/source distinctions. | `cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md` | Whole: all 1,287 lines, including complete schemas, three routes, ten recovery conditions, current-use rules, twenty-two crash rows, eleven interfaces and final sweep. | `6a3b7cf71546ed237507b34b1a24a759d34ca683216b255c91ac4add679b1bfd` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: complete receipt through closing; prior whole credit retained, accepted package identity and full scope checked. | `699b9e64e1bbd485dfd7f78bd65e0e8de275c0242f3d1da9474e30e9d77c74a1` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | Scoped: full B-INT-8 package entry in §4, full Path 8 in §5, connection authority rows in §6 and connection/output identity rows in §7; no whole-file credit. | `b20d4ee944d5a575b307d70485e5c074c4b298f43a3082ddd760159aa61d924d` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Scoped: connection/package-scope receipt matches and previously read acceptance context; no new whole-file credit. | `d62ec6e4d61495147729241331733f81982792440148f624551fe64d9346fa44` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md` | Scoped: full §16 consumer boundary reopened; existing privacy/authorization ownership retained. | `7fda28e994336a7ea0d17e217025cb71c116ec42ce3ecde3d8c9110783b52aad` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` | Scoped: full §13 current multi-speaker/fence handoff and its output boundary; full identity/mode mechanism remains later. | `c449728139f732d5aefe5efd7ca1a0d251937c64bd73504ff8527cc3ec01b305` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md` | Scoped: complete §§3–5 and §6A; exact output/delivery/attempt identity separation, mutable attempt facts and honest delivery guarantee retained. | `4edaaadc57854b711e7f750ed897e6f4a6eaa0c0ae3734b4614167e6c58afe48` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` | Scoped: full §K, connection rows/owner boundaries in §T and §U, AF-6/AF-9, R-33 and reference-only identity matches; no whole-file credit. | `1f9ea714f1a182c0857e80399850a3aeebcf4a50a32d5a200fce57a5d5f47ae3` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md` | Prior whole credit retained; existing C-7L.12 ten-rule generic connection/Person-Box boundary and actual identity-owner rules reused. | `3566cf0f917fb4f7eb329d9089f6e238fe4afbacbae2c73c8b2716e3397e7c2e` |
| `05_ACTIVE_CANDIDATE/Other_Future_Feature_Intent_Excerpts.md` | Scoped: unified-search connection object/list/navigation matches; future intent only, no new acceptance mechanism. | `efc6809ea43def73b949ea3843b98be23b2f1c4f20a4c3589012fa8d55901951` |
| `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_2.md` | Scoped: complete §§13.2/13.3 and §§16.2/16.3, plus discovered card/connection matches; exact schema and acceptance remain owner-governed, later presentation scope. | `c56829dddef3c5ec37b7b13a263b407c2e7a4374c800cce3a78db983cce3031d` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` | Scoped: prior full §§18–21 reading retained and connection/index/authority matches rechecked; no new present connection authority. | `1386091a0977ac79588f22a9f85213579203637e493dbb2d75be3d893326aa28` |
| `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md` | Scoped: exact FR-0336, FR-0401, FR-0416, FR-0417 connection rows and index; Appendix B tracking only, no historical behavior imported. | `fc014bbab36c87495d534ade8bb78f8de4197efa9408f5abb908743601a21522` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | Scoped: full NHD-M24/NHD-BINT8 rows and June 25 conceptual-design status navigation; body packages govern behavior. | `457c6f43562a92cd82076640af44a58ea412335284c0e61da3c38f3ba63f24b9` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | Scoped: full NHD-M24/NHD-BINT8 rows and June 25 conceptual-design status navigation; body packages govern behavior. | `3f1b95da77f620597e9ba862568f4247d1eb4d50f73c620888637dfcde03e3c9` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Scoped: full NHD-M24/NHD-BINT8 rows and June 25 conceptual-design status navigation; body packages govern behavior. | `aafc7abe6522f4c7ece23f40560e648866188e1b5401ed6cd298809d15ed0f7b` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Scoped: full NHD-M24/NHD-BINT8 rows and June 25 conceptual-design status navigation; body packages govern behavior. | `aad8d1aeee9a331ad6f4d9ddbcfa9c42eae2a94e1ef1bccde7484079181ff7b4` |

### Instruction and artifact identities

| File | SHA-256 |
|---|---|
| `NH_MASTER-21_SYSTEM_BEHAVIOR_BUILD_CONTRACT_FOR_CHATGPT_v1_0.md` | `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1` |
| `NH_MASTER-21_WRITER_LESSONS_FROM_AUDITS_v0_2.md` | `dae584222798cc8626e8abf1b1f184b7e65a463617932ce3e76f1265b80fa819` |
| `NH_MASTER-21_WRITER_RUN_INSTRUCTIONS_v0_3.md` | `96cd87e5e7049bf492e1a498d63fd38d002b538a9650f85d1e15b7c7d68f09e2` |
| `NH_MASTER-21_WRITING_1_MANIFEST.md` | `e0cb5fc488c075a22e836961ed2d13b602207a66b34063cdfa796956bb5c04bd` |
| `NH_MASTER-21_ROUTE_AND_WORKING_METHOD_v0_1_CANDIDATE.md` | `fbd0378c4fd2ba55710ec76ec98f68bf7daa574f5857078dcf70835d8fd30a89` |

### Earlier chapter identities preserved

| Piece | SHA-256 |
|---|---|
| CH01 | `f86342e90f8789a5b825fbe73f4bc42041c6537498a32a01980287ad32d47544` |
| CH02 | `22168ca6a6a54a2d142dcc7e1d068ca1ab7270b28a90e8e10c2a0106b595d19a` |
| CH03-a | `3b0ba1cb3ea3415ef71c5343702fd2c7ddcd44675aa8f0b4bf5e7aeab2aa80db` |
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
| CH05-e | `e526f830db5a71a0a60c7c7e0a50ef0344f81f46bce4355e1a27480d6d0076cd` |
| CH00 | `d01e8ec370be9c8e50fbb293c863c95ddaf6f82af5700877bf1a57276a1f4998` |
| CH03-b | `ba62fb68b050b3840afeabec299b2aa0baac17ba2f79869c1fc031dbc195d8b5` |
| CH03-c | `20d022f2d237cf0a29e4128eae510e0cf153505a2ffd0c64ff512fed9cb06fa6` |
| CH03-d | `9444e60b0b4cb09c1efd5d03c06579af4864f7437a10555fdeca54e50687195c` |
| CH06-a | `b604ac8293119ad8cf6f3686089f256cf5aa5fbbff1ac431edec62c2799a3571` |
| CH06-b | `fc426658bf22d37555d20eccf9a56949fb06704bf7a80fb36ee7c5cb8ce61c7d` |
| CH06-c | `05ba5405d963b66d3c75e26255f2932f146adf5f7098c4b6bf612caf539286ff` |
| CH06-d | `a79bc0af9ed246a30a4c526edf7f291b14d7b9b570c88bf94df5d7cbf9ce7dc3` |
| CH06-e | `79068327ad5315666eda0e78dda23fce1bf903f1fed0a5a84d80d3c021889692` |
| CH06-f | `da69614a03fecdf985ec8b2451849cfe282b6acadfd8257a1c7de0b4b7ecb952` |

Round 4A later changed Chapters 0, 1, 2, 3-a to 3-d and 6-a to 6-g; the identities above are those preserved when this chapter was written, and the round 4A identities are listed in the round 4A delivery manifest.

### READ-folder files not yet read whole

64 inherited pending files remain. Scoped reading receives no new whole-file credit.

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
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md`
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
§1.3 no history/actions/roles/workflow in this chapter: PASS — 255 behavior cards reviewed; 0 workflow/advice hits. Delivery metadata remains outside behavior.
§1.4 every gap written as NOT DECIDED: PASS — 525 empty fields match 525 register rows; 8 additional mechanical slots are explicit.
§1.5 conflicts marked, none resolved: PASS — the proposed direct-source basis label conflict is marked in the header and gap register; both source-specific spellings remain. Prior source conflicts and the accepted-but-excluded foundation gap are carried; no source conflict is resolved.
§3 exactly one stamp per line: PASS — 255 headers, 1796 populated fields and 650 USED BY rows checked. 0 BUILT field lines name only existing built reading/store sources; no new machinery is stamped BUILT.
§4 every behavior line cited in the exact format: PASS — 53 distinct citations; 53 resolve within the named pinned sections. Populated fields and use rows are cited; the source-to-claim review accompanies mechanical resolution.
§5.4 one name per thing: PASS — 255 unique current IDs without prior collisions; 2126 named-card mentions checked. Shared atoms retain their established IDs and names.
§6 all template fields present, in order, for every part: PASS — 255 templates and 2321 field lines checked.
§6.3 reciprocity within this chapter: PASS — 632 internal relationship occurrences checked; 64 outgoing and 4 incoming continuation rows name both ends. No missing reciprocal; prior files remain unchanged.
§6.4 every decided detail written in, no citation used in place of content: PASS — 24 source-to-card rows reviewed; 75 expected source-name literals present. Existing atomic owners and remaining scopes are explicit.
§6.5 sub-parts recursed to the bottom: PASS — the two responsibilities, three decision states, five certainty labels, five source labels, all proposed record slots, type/direction/key fields, three acceptance routes, ten recovery conditions, sixteen parent states, five report states, nine current-use requirements and three outcomes, twenty-two crash classes, eleven complete interfaces and twenty-eight child kinds are placed. Shared slots and existing Person-Box/B9/logging atoms keep their canonical owners. Pair fields are split to their source-defined atomic slots; later-owner mechanisms remain explicit. 0 current cards have all three TOGETHER fields empty.
§9 coverage matrix rows added for every file used: PASS — all 145 pinned READ-folder file paths remain in the carried inventory; current additions and 21 current READ RECORD fingerprints are present. Shared-package coverage remains partial where stated.
§10.11 no recommendation, no sentence addressed to Ness: PASS — all 255 behavior cards reviewed; no recommendation or addressed instruction.
Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`.

### Computed self-check results

Writer checks and the accompanying manual source/box review returned no unresolved current-file errors. They are not an independent audit or adoption. Plain human/precondition gates are justified in the inventory above.

| Check | Count |
|---|---|
| cards | 255 |
| field_lines | 2321 |
| used_by_rows | 650 |
| empty_fields | 525 |
| internal_relationships | 632 |
| external_relationships | 64 |
| distinct_citations | 53 |
| resolved_citations | 53 |
| empty_together_cards | 0 |
| plain_together_lines | 0 |
| formula_hits | 0 |
| wording_hits | 0 |
| errors | 0 |
| named_card_mentions_checked | 2126 |
| misfiled_box_fields_scanned | 2321 |
| restriction_failure_gate_slots_reviewed | 774 |
| registered_empty_fields | 525 |
| cross_piece_continuations_checked | 64 |
| covered_read_file_paths | 145 |
| read_fingerprints_checked | 21 |
| source_names_checked | 75 |
| source_names_missing | 0 |
| built_field_lines | 0 |
| behavior_workflow_hits | 0 |
| plain_gates_justified | 0 |
| outgoing_continuations | 64 |
| incoming_continuations | 4 |
| registered_fields | 525 |
| additional_gaps | 8 |
| pending_source_paths | 64 |
| source_map_rows | 24 |
| read_record_rows | 21 |

The delivery recount compares these metrics with the finished file.
