# Chapter 6-c — Group D: C-7L

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH06-c.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`  

This piece covers Person-Box identity anchors, links, qualitative identity tests, proposals, joins and corrections, Ness's box, seven-section presentation, cross-batch provenance, Holding, metadata-only held-material references, and the Person-Box ends of permission, voice, enrollment and connection interfaces. Existing telling and Holding atoms retain their delivered owners. Computed View, View Layer, Living State Web and full Connection Capability remain CH06-d/e/f/g; authority, privacy and LMAC remain CH07-c and CH08-a/c; the full known-person, SIA, SACL and enrollment mechanisms remain CH09-b/c/d/h; world presentation remains CH10-e.

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; NHD identifiers locate decisions in the pinned index and do not replace behavior citations.

<!-- BEGIN BEHAVIOR -->

### C-7L — Person-Boxes (§7L)
Stamp: DESIGNED    Source: [V10 §7L] [MAP C-7L]

ALONE
- What it is: DESIGNED — The stable identity anchor and linked gather for a person; it records how that person appears across preserved material over time. [V10 §7L] [MAP C-7L]
- Takes in: DESIGNED — Roots where the person appears, is mentioned or quoted, readings and tellings in any perspective role, themes with confirmation status, clashes, relevant Ness response events, other Person-Boxes with proposed or confirmed identity connections, and permitted metadata-only pre-ingest references. [V10 §7L] [MAP C-7L]
- Does: DESIGNED — Links original objects in place, records the basis and certainty of each connection, keeps uncertain identities separate and shows changes over time. Holds what was observed or told, by whom, with what certainty and at what time. [V10 §7L] [MAP C-7L]
- Gives out: DESIGNED — A stable identity view with inspectable original objects, unresolved identity questions, uncertain links and preserved clashes. [V10 §7L] [MAP C-7L]
- Must never: DESIGNED — Synthesize a summary, personality profile, diagnosis, fixed character or closed identity; promote frequency to fact; equate a report about someone with their own perspective; merge uncertain references without explicit resolution; treat absence as evidence; resolve contradictions; make one perspective authoritative; invent unsupported connections; claim to describe what a person is like. [V10 §7L] [MAP C-7L]
- Fails closed by: ACCEPTED — Leaves an unclear mention as an unconfirmed pending anchor and a less-than-definite join as a pending merge proposal; both can remain unresolved indefinitely. Telling-specific semantic links remain blocked until complete-set eligibility holds. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1]

TOGETHER
- Fed by: BUILT — C-READ — Reading record, validator, writer (§6B): immutable readings and their source-root references. [V10 §6B] [V10 §7L]
- Fed by: DESIGNED — C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B): person-related material gathered during CY-A; C-7B.4 — Person-Box gather: the Person-Box gather; C-7K — Story Layer (§7K): perspective-separated tellings; C-7E — Catalog Front Door + pre-ingest holding (§7E): authorized source references and source-carried attribution. [MAP C-7B] [MAP CY-A] [MAP C-7L]
- Fed by: ACCEPTED — C-READ.10.14 — Telling-reference handoff: integrity-valid first-class telling references; C-7K.7 — Holding through separate linked objects: Holding through separate linked objects; C-7J.8 — Clash and named-gap presentation: clash presentation with responses kept distinct. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] [V10 §7L]
- Fed by: DESIGNED — C-7E.11 — Held-content access boundary: safe source-carried held metadata, lifecycle state and blockers only. [V10 §7L] [V10 §7E]
- Fed by: ACCEPTED — C-7L.1 — Person-Box link record: the five-field link record; C-7L.2 — Uncertain identity anchor: uncertain anchors; C-7L.3 — Person-Box proposal and identity events: proposal and event mechanics; C-7L.4 — Ness's confirmed Person-Box: Ness's confirmed box; C-7L.5 — Seven-section Person-Box view: seven-section presentation; C-7L.6 — Person-Box cross-batch identity links: cross-batch provenance; C-7L.7 — Person-Box Holding through linked objects: separated Holding; C-7L.11 — Provisional enrollment Person-Box link: provisional enrollment link truth; C-7L.12 — Person-Box generic-connection use boundary: separately valid connection references; C-7L.13 — Authorized Person-Box query interface: authorized query results; C-7L.14 — Person-Box operation and presentation records: append-only operation records. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12]
- Fed by: DESIGNED — C-7L.8 — Person-Box held-material metadata boundary: metadata-only pre-ingest references; C-7L.9 — Person-Box permission-boundary read interface: permission-boundary read interface; C-7L.10 — Voice-profile Person-Box linking boundary: voice-profile link prerequisites and separate identity authority. [V10 §7L] [V10 §25.2] [V10 §25.3] [V10 §25.4]
- Gated by: ACCEPTED — C-READ.10.10 — Telling-set semantic eligibility: a complete valid telling set or legitimate zero-telling result is required before telling-specific use; C-7B.9.11 — Forbidden Wonder evidence uses: Wonder possibilities never become observed reality about a person. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1] [04/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md §7]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): actual internal use and visible output require their own privacy authorization; C-7P — Permission & Authority Boundaries (§7P): link and query actions stay within their authority; C-SACL — Speaker Access-Control Layer (§25.4): applicable speaker access gates disclosure. [V10 §7Q] [V10 §7P] [V10 §25.2] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §20]
- Changes: DESIGNED — C-7M — Computed View (§7M): supplies identity-linked source objects for the current picture; C-7D — Living State Web (§7D): supplies stable person identity anchors without adding evidence; C-SIA — Speaker Identity Assessment (§25.3): supplies permitted profile-reading links; C-SACL — Speaker Access-Control Layer (§25.4): supplies PBR references through the authorized query route. [V10 §7L] [MAP C-7L]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B), in CY-A | A person reference and preserved source objects. | Gathers linked person material without interpreting a personality. | Person-related navigation and reference context. | [MAP C-7B] [MAP CY-A] |
| 2 · DESIGNED | C-7K — Story Layer (§7K) | Person identity references for tellings. | Keeps perspective roles linked to their identity anchors. | Identity navigation without narrative synthesis. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [V10 §7L] |
| 3 · ACCEPTED | C-7K.7 — Holding through separate linked objects | Separate person-related objects and links. | Holds each perspective and Ness's understanding distinctly. | Linked Holding without a second memory store. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] |
| 4 · DESIGNED | C-7M — Computed View (§7M) | Person-linked sources. | Assembles under its own derivation and privacy rules. | Current presentation, never the original records. | [MAP C-7L] |
| 5 · DESIGNED | C-7D — Living State Web (§7D) | Stable person identity anchors. | Grounds person-related state under its own rules. | State identity references, not added support. | [MAP C-7L] |
| 6 · DESIGNED | C-SIA — Speaker Identity Assessment (§25.3) | Permitted profile-reading links. | Consumes them under identity and training rules. | Independent identity assessment inputs. | [V10 §25.3 / Voice Profile Architecture] |
| 7 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4) | Active PBR reference obtained through LMAC. | Checks permission categories at output time. | Speaker-bounded disclosure. | [V10 §25.4 / Permission Boundary Enforcement] |
| 8 · DESIGNED | C-9.4.4 — Rehearsal compatibility boundary | NOT DECIDED | Gates this place: the existing person/evidence boundary. | Nothing in this card. | [V10 §9] |
| 9 · DESIGNED | C-9.4 — Conversation-rehearsal constraints | NOT DECIDED | Gates this place: person-Box evidence and identity boundaries. | Nothing in this card. | [V10 §9] |
| 10 · DESIGNED | C-SIA.17 — Unknown-speaker linking evidence | Attributed voice material across authorized sessions, capture-time certainty, spoofing flags, promotion provenance, supporting readings and the §7L proposal rules. | Takes this place's change: supplies eligible identity evidence without granting silent-link authority. | Supplies eligible identity evidence without granting silent-link authority. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| 11 · DESIGNED | C-SIA.20.6 — Enrollment association strengthening | Later SIA evidence, repeated authorized sessions, anti-spoofing-clean material, candidate separation and accepted profile-integrity rules. | Takes this place's change: later evidence can strengthen the provisional association under accepted profile-integrity and linking rules. | Later evidence can strengthen the provisional association under accepted profile-integrity and linking rules. | [V10 §25.11 / §7L Integration] |
| 12 · ACCEPTED | C-BAI.19.2 — Enrollment prerequisite revalidation | Six owner facts: final permanent trusted-owner phone status (BAI state 4). | Supplies confirmed Ness Person-Box truth. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] |
| 13 · DESIGNED | C-7D.5 — Relationship state edge | Ness's experienced relationship state, a Person-Box anchor and attributed references to the other person's words/actions. | Supplies identity anchor under confirmation and merge-proposal rules. | Nothing in this card. | [V10 §7D] |
| 14 · DESIGNED | C-OTHER — Other-Speaker / Guest / Known-Person Architecture (§25.2) | Speaker assessments, the current access level, person-specific permission boundaries and attributed third-party session material. | Takes this place's change: authorized third-party readings may support person proposals without collapsing attribution into truth. | Authorized third-party readings may support person proposals without collapsing attribution into truth. | [MAP C-OTHER] [V10 §25.2 / Fingerprint-Authorized Batch Promotion] |
| 15 · ACCEPTED | C-7M.5.5.6 — Computed View Person-Box-link references | IDs of person-related links with their actual certainty and provenance. | Supplies stable identity anchors and provenance-bearing person links. | Nothing in this card. | [V10 §7L] [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 16 · ACCEPTED | C-7Q.11.7 — Meaning, derived-store and simulation privacy interface | Authorized inputs, explicit influence-removal scope, third-party separation and any simulation approval. | Takes this place's change to Person-Box assembly: internal purpose and the influence set are checked, and third-party separation and labels are carried in. | Person-Box assembly keeps its privacy and third-party constraints intact. | [04/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md §16] |
| 17 · ACCEPTED | C-7D.16.3.9 — World model and third-party-profile separation | Third-party identity anchors and attributed conditions. | Supplies identity anchors. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §4D] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §6] |
| 18 · DESIGNED | C-SIA.9 — Independent voice profiles | Sets of profile readings linked through §7L. | Supplies independently linked reading sets. | Nothing in this card. | [V10 §25.3 / Voice Profile Architecture] |
| 19 · ACCEPTED | C-ENROLL.7 — Mid-session protective stop | Trust loss/replacement/revocation, invalid recovery/setup, QR/secret contradiction, medium-or-higher spoofing, missing/contradictory Person-Box, BAI/session integrity failure, privacy exclusion or restart. | Supplies prerequisite changes. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] |
| 20 · DESIGNED | C-SIA.18 — Compact inference representation | The source profile readings. | Supplies the linked authoritative profile-reading set. | Nothing in this card. | [V10 §25.3 / Voice Profile Architecture] [V10 §25.3 / Compact Profile Representation] |
| 21 · ACCEPTED | C-ENROLL.7.5 — Person-Box prerequisite safety change | The Person-Box owner's current fact. | Supplies the changed prerequisite truth. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] |

SUB-PARTS: C-7L.1 — Person-Box link record; C-7L.2 — Uncertain identity anchor; C-7L.3 — Person-Box proposal and identity events; C-7L.4 — Ness's confirmed Person-Box; C-7L.5 — Seven-section Person-Box view; C-7L.6 — Person-Box cross-batch identity links; C-7L.7 — Person-Box Holding through linked objects; C-7L.8 — Person-Box held-material metadata boundary; C-7L.9 — Person-Box permission-boundary read interface; C-7L.10 — Voice-profile Person-Box linking boundary; C-7L.11 — Provisional enrollment Person-Box link; C-7L.12 — Person-Box generic-connection use boundary; C-7L.13 — Authorized Person-Box query interface; C-7L.14 — Person-Box operation and presentation records

### C-7L.1 — Person-Box link record
Stamp: ACCEPTED    Source: [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The provenance-bearing reference connecting a Person-Box to an original object; the five settled fields also accompany link-family events. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — A linkable object and the source-grounded basis for connecting it to the person. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Records what it connects, why, who or what established it, certainty and timestamp. Keeps the original where it is; an automatic identity link or join includes the evidence meeting its qualitative test. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — A reference with per-element provenance, no copied object and no additional evidential weight. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Copy an original into a second authoritative home; omit the evidence basis of an automatic link or join; make a link prove a telling true or resolve a clash. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7L.1.1 — Person-Box link what it connects: the endpoints; C-7L.1.2 — Person-Box link why: the basis; C-7L.1.3 — Person-Box link who established: the establishing actor; C-7L.1.4 — Person-Box identity-test certainty: the applicable identity-test outcome; C-7L.1.5 — Person-Box link timestamp: the time. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gated by: ACCEPTED — C-7L.3.4 — Completely-clear mention test: a mention links automatically only when the source makes identity completely clear; C-7L.3.5 — Definite same-person test: an automatic join requires definite same-person evidence. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Changes: ACCEPTED — C-7L.3.7 — Person-Box append-only event family: supplies the settled fields for every link-family event. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L — Person-Boxes (§7L) | Original object references with all five fields. | Links rather than copies and exposes provenance. | The person's navigable gather. | [V10 §7L] |
| 2 · ACCEPTED | C-7L.3.7 — Person-Box append-only event family | Five settled link fields. | Carries them on append-only events. | Traceable link history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 3 · ACCEPTED | C-7L.1.3 — Person-Box link who established | The required actor provenance. | Identifies who or what established the connection. | The who-established field. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 4 · ACCEPTED | C-7L.1.5 — Person-Box link timestamp | The link's temporal provenance requirement. | Carries the timestamp with the connection. | The timestamp field. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: C-7L.1.1 — Person-Box link what it connects; C-7L.1.2 — Person-Box link why; C-7L.1.3 — Person-Box link who established; C-7L.1.4 — Person-Box identity-test certainty; C-7L.1.5 — Person-Box link timestamp

### C-7L.1.1 — Person-Box link what it connects
Stamp: ACCEPTED    Source: [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The required link endpoints. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — The person anchor and original root, reading, telling, theme, clash, response, other box or permitted metadata reference. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Identifies the connected objects by reference; telling targets use telling_id. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — Inspectable pointers to the originals. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Replace a linked object with a copied authoritative payload. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-READ.10.14.2 — Person-Box references: stable telling_id references and preserved five-field link provenance. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.1 — Person-Box link record | Object endpoints. | States what the link connects. | Resolvable link identity. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.1.2 — Person-Box link why
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The required explanation and source-grounded evidence basis of a link. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — Source evidence connecting the material to the person. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Records why the link was established; an automatic link or join records the evidence that met its test. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — A reviewable connection basis. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Substitute name similarity, repetition or the link's existence for the required source evidence. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7L.3.4 — Completely-clear mention test: a mention's source basis must meet completely clear; C-7L.3.5 — Definite same-person test: an automatic join's combined evidence must meet definite. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.1 — Person-Box link record | The connection's source evidence. | Stores why it was made. | Auditable link provenance. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7L.1.3 — Person-Box link who established
Stamp: ACCEPTED    Source: [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The required identity of who or what established the connection. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — The human or mechanism responsible for the link. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Preserves the establishing actor with the link. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — Attributable link provenance. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Omit who or what established the link. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.1 — Person-Box link record: supplies the establishing actor. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.1 — Person-Box link record | Who or what made the connection. | Keeps establishment attributable. | The link's provenance. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.1.4 — Person-Box identity-test certainty
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The required qualitative certainty outcome of the ordinary identity tests. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Takes in: ACCEPTED — The source-based mention or same-person test result. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Does: ACCEPTED — Records exactly completely clear, pending-unclear, definite or pending-not-definite. This is a test outcome, never a number. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Gives out: ACCEPTED — A qualitative identity status that distinguishes a clear link from an unresolved anchor and a definite join from a pending proposal. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Must never: ACCEPTED — Assign a score; turn similar names into identity evidence; promote pending status through age or repetition. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — An unmet mention test stays pending-unclear; an unmet same-person test stays pending-not-definite. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]

TOGETHER
- Fed by: ACCEPTED — C-7L.1.4.1 — Person-Box completely clear outcome: clear mention; C-7L.1.4.2 — Person-Box pending-unclear outcome: unclear mention; C-7L.1.4.3 — Person-Box definite outcome: definite join; C-7L.1.4.4 — Person-Box pending-not-definite outcome: less-than-definite join. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.1 — Person-Box link record | The applicable qualitative outcome. | Keeps certainty visible in link provenance. | No numeric identity score. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] |
| 2 · ACCEPTED | C-7L.2.5 — Uncertain anchor current test outcome | The qualitative identity-test vocabulary. | Records the current pending outcome without a score. | The anchor's certainty field. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: C-7L.1.4.1 — Person-Box completely clear outcome; C-7L.1.4.2 — Person-Box pending-unclear outcome; C-7L.1.4.3 — Person-Box definite outcome; C-7L.1.4.4 — Person-Box pending-not-definite outcome

### C-7L.1.4.1 — Person-Box completely clear outcome
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The completely clear mention-link outcome. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Takes in: ACCEPTED — Source material unambiguously identifying the person. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Does: ACCEPTED — Allows automatic linking to the existing identity with the recorded evidence basis. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Gives out: ACCEPTED — A completely clear link without a manual-approval step. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Must never: ACCEPTED — Use name similarity alone or invent ordinary-case manual approval. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7L.3.4 — Completely-clear mention test: the source must make the person's identity unambiguous. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.1.4 — Person-Box identity-test certainty | A met mention test. | Records completely clear. | The link certainty label. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7L.1.4.2 — Person-Box pending-unclear outcome
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The pending-unclear outcome for an insufficiently clear mention. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Takes in: ACCEPTED — A mention whose identity is less than completely clear. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Does: ACCEPTED — Keeps an unresolved identity anchor unconfirmed, indefinitely if necessary. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Gives out: ACCEPTED — A pending-unclear anchor. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Must never: ACCEPTED — Silently confirm the anchor or let waiting time count as evidence. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Withholds a confirmed identity link while the test is unmet. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7L.3.4 — Completely-clear mention test: failure to meet completely clear requires this pending result. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.1.4 — Person-Box identity-test certainty | An unmet mention test. | Records pending-unclear. | Explicit unresolved certainty. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7L.1.4.3 — Person-Box definite outcome
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The definite same-person outcome. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Takes in: ACCEPTED — Combined source-grounded evidence leaving no genuine identity question. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Does: ACCEPTED — Permits N.H to join the records automatically while preserving all originals. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Gives out: ACCEPTED — A definite join with its evidence basis. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Must never: ACCEPTED — Require invented manual approval for an ordinary definite join or rewrite constituent records. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7L.3.5 — Definite same-person test: combined evidence must identify the records as definitely the same person. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.1.4 — Person-Box identity-test certainty | A met same-person test. | Records definite. | A qualitative join result. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7L.1.4.4 — Person-Box pending-not-definite outcome
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The pending-not-definite same-person outcome. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Takes in: ACCEPTED — A possible identity connection with a genuine question still open. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Does: ACCEPTED — Creates a pending merge proposal and keeps its records separate. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Gives out: ACCEPTED — An indefinitely unresolved proposal when evidence remains insufficient. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Must never: ACCEPTED — Silently merge or turn similarity and repetition into definiteness. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Withholds the join; a later join requires a met definite test or Ness's confirmation of the pending proposal. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7L.3.5 — Definite same-person test: anything less than definite follows the pending branch. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.1.4 — Person-Box identity-test certainty | An unmet same-person test. | Records pending-not-definite. | Explicit unresolved join status. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.1.5 — Person-Box link timestamp
Stamp: ACCEPTED    Source: [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The required timestamp on a link or link-family event. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — When the connection or event was recorded. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Carries time with the link's provenance. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — Chronologically inspectable link history. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Omit the link timestamp. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.1 — Person-Box link record: supplies the timestamp. [V10 §7L / LINKABLE OBJECT TYPES] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.1 — Person-Box link record | The connection's time. | Preserves its temporal provenance. | Time-bearing link records. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.2 — Uncertain identity anchor
Stamp: ACCEPTED    Source: [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — A reference anchor for an uncertain identity, which is a normal state rather than an error to conceal. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — The label/name used, where it appeared, when, connecting evidence and current test outcome. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Keeps possible same-person references separate until an authorized resolution; multiple anchors may coexist indefinitely. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — An unconfirmed, provenance-bearing pending anchor. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Treat the proposed anchor as a confirmed Person-Box or merge uncertainty silently. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — Stays pending when the mention test is not completely clear. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

TOGETHER
- Fed by: ACCEPTED — C-7L.2.1 — Uncertain anchor label or name: observed label; C-7L.2.2 — Uncertain anchor appearance location: appearance location; C-7L.2.3 — Uncertain anchor appearance time: appearance time; C-7L.2.4 — Uncertain anchor connecting evidence: connecting evidence; C-7L.2.5 — Uncertain anchor current test outcome: current test outcome. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gated by: ACCEPTED — C-7L.3.3 — Person-Box search before propose: search confirmed boxes, unresolved anchors, aliases and prior merge proposals before creation. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Changes: ACCEPTED — C-7L.3.7.2 — Person-Box pending-anchor creation event: supplies the content of the pending-anchor creation event. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L — Person-Boxes (§7L) | Uncertain person references. | Keeps unresolved identity explicit. | Separate pending anchors in the identity view. | [V10 §7L] |
| 2 · ACCEPTED | C-7L.3.7.2 — Person-Box pending-anchor creation event | The five anchor fields. | Records a new pending anchor append-only. | Preserved uncertain-reference history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 3 · ACCEPTED | C-7L.2.1 — Uncertain anchor label or name | The uncertain anchor's label requirement. | Preserves the source name or label. | The label field. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 4 · ACCEPTED | C-7L.2.2 — Uncertain anchor appearance location | The anchor's source-location requirement. | Records where the reference appeared. | Appearance-location provenance. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 5 · ACCEPTED | C-7L.2.3 — Uncertain anchor appearance time | The anchor's temporal requirement. | Records when the reference appeared. | Appearance-time provenance. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 6 · ACCEPTED | C-7L.2.4 — Uncertain anchor connecting evidence | The anchor's evidence requirement. | Carries actual support and motivation-only similarity. | The connecting-evidence field. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 7 · ACCEPTED | C-7L.5.7 — Person-Box unresolved-identity section | Unresolved anchors and their provenance. | Shows pending identity questions with their actual status. | Visible unresolved references. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |

SUB-PARTS: C-7L.2.1 — Uncertain anchor label or name; C-7L.2.2 — Uncertain anchor appearance location; C-7L.2.3 — Uncertain anchor appearance time; C-7L.2.4 — Uncertain anchor connecting evidence; C-7L.2.5 — Uncertain anchor current test outcome

### C-7L.2.1 — Uncertain anchor label or name
Stamp: ACCEPTED    Source: [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The label or name used in the uncertain reference. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — The source-carried reference wording. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Records the label without making it a stable identity or proof of sameness. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — The anchor's observed name or label. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Treat similar labels alone as sufficient identity evidence. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.2 — Uncertain identity anchor: supplies the label or name used. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.2 — Uncertain identity anchor | The observed reference label. | Preserves how the person was named. | Traceable reference wording. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.2.2 — Uncertain anchor appearance location
Stamp: ACCEPTED    Source: [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The source location where the uncertain reference appeared. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — The original appearance reference. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Keeps the anchor connected to where the name or label occurred. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — An inspectable appearance location. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Omit where the uncertain reference appeared. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.2 — Uncertain identity anchor: supplies where the reference appeared. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.2 — Uncertain identity anchor | The source location. | Retains where the reference arose. | Location-bearing anchor provenance. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.2.3 — Uncertain anchor appearance time
Stamp: ACCEPTED    Source: [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — When the uncertain person reference appeared. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — The appearance time carried with the reference. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Records when the name or label occurred. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — Temporal anchor provenance. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Omit when the uncertain reference appeared. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.2 — Uncertain identity anchor: supplies the reference's appearance time. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.2 — Uncertain identity anchor | When the reference appeared. | Keeps temporal provenance. | A dated uncertain reference. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.2.4 — Uncertain anchor connecting evidence
Stamp: ACCEPTED    Source: [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The evidence connecting an uncertain reference to a possible person. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — Source-grounded connection evidence and any name-similarity motivation. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Records actual support; marks mere name or label similarity as motivation-only evidence. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — A basis whose limitations remain inspectable. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Invent support or count similar names alone as a met identity test. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.2 — Uncertain identity anchor: supplies the connection evidence and its limitation. [V10 §7L / UNCERTAIN IDENTITY] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.2 — Uncertain identity anchor | The evidence and any motivation-only similarity. | Keeps support distinct from suggestion. | An honest uncertain-anchor basis. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.2.5 — Uncertain anchor current test outcome
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The anchor's current qualitative identity certainty. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — The applicable source-grounded test outcome. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Records pending-unclear while the mention remains less than completely clear; resolution is a new event. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — Visible pending certainty. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Replace qualitative certainty with a score or rewrite an earlier event to pretend it was confirmed. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — An unclear reference stays unconfirmed. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

TOGETHER
- Fed by: ACCEPTED — C-7L.1.4 — Person-Box identity-test certainty: the qualitative ordinary identity-test vocabulary. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.2 — Uncertain identity anchor | The current identity outcome. | Keeps uncertainty visible. | The anchor's certainty record. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.3 — Person-Box proposal and identity events
Stamp: ACCEPTED    Source: [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The proposal-based identity mechanism with explicit qualitative resolution and append-only history. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — A person reference encountered through a front door, root, reading, telling or another authorized source; existing anchors and identity evidence. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Searches before creating an anchor or proposal. Links completely clear mentions automatically; joins definitely identical person records automatically. Keeps less-clear mentions as unconfirmed anchors and less-definite joins as pending proposals. Records resolutions and corrections as new events. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — Stable identity views with distinct constituent records and inspectable proposal, join and correction history. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Create a confirmed identity silently under uncertainty; use name similarity as proof; require extra manual approval for ordinary clear cases; copy originals or rewrite history. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — An unmet mention test leaves a pending unresolved anchor; an unmet join test leaves a pending merge proposal. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

TOGETHER
- Fed by: ACCEPTED — C-7L.3.1 — Person-Box stable system ID: stable ID; C-7L.3.2 — Person-Box names labels and roles: separate mutable labels; C-7L.3.6 — Ness Person-Box responses: Ness's available responses; C-7L.3.7 — Person-Box append-only event family: append-only event family. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gated by: ACCEPTED — C-7L.3.3 — Person-Box search before propose: mandatory search before an anchor or proposal; C-7L.3.4 — Completely-clear mention test: completely-clear mention criterion; C-7L.3.5 — Definite same-person test: definite same-person criterion. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L — Person-Boxes (§7L) | Proposed and resolved identity references. | Maintains stable identities without silent uncertain merging. | Person-Box link-layer history. | [V10 §7L] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 2 · ACCEPTED | C-7L.3.1 — Person-Box stable system ID | The persistent identity requirement. | Keeps system identity stable across label changes. | The stable ID. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14] |
| 3 · ACCEPTED | C-7L.3.4 — Completely-clear mention test | The ordinary mention-link resolution rule. | Routes clear evidence to automatic linking and less to pending. | The mention's link eligibility. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] |
| 4 · ACCEPTED | C-7L.3.5 — Definite same-person test | The ordinary same-person resolution rule. | Routes definite evidence to automatic joining and less to a proposal. | The join eligibility. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] |
| 5 · DESIGNED | C-7L.10.6 — Unknown-speaker Person-Box rule condition | The accepted identity tests and proposal rules. | Keeps ordinary speaker linking within Person-Box authority. | No silent unknown-speaker merge. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 6 · ACCEPTED | C-7L.12 — Person-Box generic-connection use boundary | The independent identity tests and proposal rules. | Prevents generic connection acceptance from substituting for person identity. | No connection-derived identity authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] |
| 7 · DESIGNED | C-7M.4.3.5 — Computed View identity-resolution trigger | The authorized Person-Box resolution and its append-only history. | Supplies the accepted identity resolution and event history. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [V10 §7M / UPDATE TIMING] [V10 §7L] |

SUB-PARTS: C-7L.3.1 — Person-Box stable system ID; C-7L.3.2 — Person-Box names labels and roles; C-7L.3.3 — Person-Box search before propose; C-7L.3.4 — Completely-clear mention test; C-7L.3.5 — Definite same-person test; C-7L.3.6 — Ness Person-Box responses; C-7L.3.7 — Person-Box append-only event family

### C-7L.3.1 — Person-Box stable system ID
Stamp: ACCEPTED    Source: [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The stable system-generated identifier of a Person-Box. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Takes in: ACCEPTED — A person identity anchor. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Does: ACCEPTED — Keeps the same identity reference while separately attached names, labels and roles may change; cross-batch links point to this ID. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Gives out: ACCEPTED — One stable Person-Box ID for the identity view. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Must never: ACCEPTED — Treat a mutable name as the stable system identity. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.3 — Person-Box proposal and identity events: supplies stable identity independent of labels. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3 — Person-Box proposal and identity events | The stable ID. | Anchors identity events and links. | Persistent person reference. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-7L.4 — Ness's confirmed Person-Box | The stable system-generated ID. | Anchors Ness's existing confirmed box. | Stable Ness identity. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] |
| 3 · ACCEPTED | C-7L.6.2 — Person-Box cross-batch identity tag | The stable Person-Box ID. | Ties separately valid links to one person across batches. | The cross-batch identity tag. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7L.3.2 — Person-Box names labels and roles
Stamp: ACCEPTED    Source: [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — Human-readable names, labels and roles attached separately from the stable ID. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — The person's source labels and later authorized naming changes. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Keeps names and labels as separately attached alias records; changes append new history rather than editing earlier references. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — Readable labels without identity reassignment. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Rewrite an old label in place or treat similar wording alone as proof of identity. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7L.3.7.7 — Person-Box alias record: append-only alias records. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3 — Person-Box proposal and identity events | Separately attached names, labels and roles. | Presents the stable anchor through mutable labels. | Naming history without identity rewrite. | [V10 §7L] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 2 · ACCEPTED | C-7L.3.7.7 — Person-Box alias record | The separate-name and stable-ID boundary. | Adds aliases without editing old labels. | New alias history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-7L.3.3 — Person-Box search before propose
Stamp: ACCEPTED    Source: [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The mandatory search before any new identity anchor or proposal is created. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — A new reference or possible duplicate, including name similarity as motivation only. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Searches confirmed boxes, unresolved anchors, aliases and prior merge proposals; records that the search occurred and its scope on the resulting event. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — A recorded search scope preceding proposal or anchor creation. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Skip a search scope; convert similarity into a met identity test; omit occurrence and scope from the resulting event. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7L.3.3.1 — Confirmed Person-Box search scope: confirmed boxes; C-7L.3.3.2 — Unresolved identity-anchor search scope: unresolved anchors; C-7L.3.3.3 — Person-Box alias search scope: aliases; C-7L.3.3.4 — Prior Person-Box merge-proposal search scope: prior merge proposals. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.2 — Uncertain identity anchor | The four search scopes and occurrence. | Searches before creating an uncertain anchor. | An anchor grounded in an inspected identity inventory. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 2 · ACCEPTED | C-7L.3 — Person-Box proposal and identity events | Search-before-propose results. | Requires the search before new anchors or proposals. | Recorded occurrence and scope. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 3 · ACCEPTED | C-7L.3.7 — Person-Box append-only event family | Search occurrence and scope. | Carries the search record on resulting events where required. | Inspectable creation provenance. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 4 · ACCEPTED | C-7L.3.3.1 — Confirmed Person-Box search scope | The four-scope search requirement. | Includes existing confirmed boxes. | Confirmed-box search coverage. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 5 · ACCEPTED | C-7L.3.3.2 — Unresolved identity-anchor search scope | The four-scope search requirement. | Includes unresolved identity anchors. | Pending-anchor search coverage. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 6 · ACCEPTED | C-7L.3.3.3 — Person-Box alias search scope | The four-scope search requirement. | Includes separately attached aliases. | Alias search coverage. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 7 · ACCEPTED | C-7L.3.3.4 — Prior Person-Box merge-proposal search scope | The four-scope search requirement. | Includes previous merge proposals. | Prior-proposal search coverage. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 8 · ACCEPTED | C-7L.3.7.2 — Person-Box pending-anchor creation event | Completed search occurrence and scope. | Records them on the new pending anchor. | Creation provenance. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 9 · ACCEPTED | C-7L.3.7.4 — Person-Box merge-proposal record | Completed search occurrence and scope. | Preserves them on the new merge proposal. | Proposal creation provenance. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: C-7L.3.3.1 — Confirmed Person-Box search scope; C-7L.3.3.2 — Unresolved identity-anchor search scope; C-7L.3.3.3 — Person-Box alias search scope; C-7L.3.3.4 — Prior Person-Box merge-proposal search scope

### C-7L.3.3.1 — Confirmed Person-Box search scope
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The confirmed-box scope of the mandatory identity search. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — Existing confirmed Person-Boxes. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Searches them before a new anchor or proposal. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — The confirmed-box portion of the recorded search scope. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Omit confirmed boxes from the search-before-propose step. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.3.3 — Person-Box search before propose: supplies the confirmed-box scope. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3.3 — Person-Box search before propose | Confirmed-box search coverage. | Includes it in the mandatory search. | The recorded search scope. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.3.3.2 — Unresolved identity-anchor search scope
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The unresolved-anchor scope of the mandatory identity search. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — Existing unresolved identity anchors. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Searches pending references before proposing another anchor or connection. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — The unresolved-anchor portion of the recorded search scope. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Ignore unresolved anchors merely because they are not confirmed. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.3.3 — Person-Box search before propose: supplies the unresolved-anchor scope. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3.3 — Person-Box search before propose | Unresolved-anchor search coverage. | Includes pending identities in the search. | The recorded search scope. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.3.3.3 — Person-Box alias search scope
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The alias scope of the mandatory identity search. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — Names and labels attached through alias records. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Searches aliases before proposing a new anchor or proposal. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — The alias portion of the recorded search scope. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Treat an alias match alone as satisfying an identity test. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.3.3 — Person-Box search before propose: supplies the alias scope. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3.3 — Person-Box search before propose | Alias search coverage. | Includes separately attached names and labels. | The recorded search scope. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.3.3.4 — Prior Person-Box merge-proposal search scope
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The prior-merge-proposal scope of the mandatory identity search. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — Previous proposals concerning possible same-person references. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Searches prior merge proposals before creating another anchor or proposal. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — The prior-proposal portion of the recorded search scope. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Omit previous merge proposals from the required search. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.3.3 — Person-Box search before propose: supplies the prior-merge-proposal scope. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3.3 — Person-Box search before propose | Prior-proposal search coverage. | Includes earlier identity questions. | The recorded search scope. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.3.4 — Completely-clear mention test
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The qualitative test for linking a mention to an existing identity. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Takes in: ACCEPTED — The mention's source material and its evidence of who the person is. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Does: ACCEPTED — Finds completely clear only when the source itself makes the person's identity unambiguous. A met test links automatically with its evidence recorded; anything less creates an unconfirmed pending unresolved anchor. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Gives out: ACCEPTED — A completely clear link or a pending-unclear reference. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Must never: ACCEPTED — Use a score or similar names alone; silently confirm ambiguity; add manual approval to an ordinary completely-clear case. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Keeps less-than-clear material pending and unconfirmed, indefinitely if needed. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.3 — Person-Box proposal and identity events: determines the ordinary mention's clear or pending route. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.1 — Person-Box link record | Source evidence for a mention. | Requires the clear test for automatic linking. | Permitted link or pending anchor. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] |
| 2 · ACCEPTED | C-7L.1.2 — Person-Box link why | Evidence supporting the mention. | Records why the test was met. | Mandatory basis for automatic links. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-7L.1.4.1 — Person-Box completely clear outcome | An unambiguous source identity. | Allows the completely clear outcome. | Automatic link eligibility. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] |
| 4 · ACCEPTED | C-7L.1.4.2 — Person-Box pending-unclear outcome | Less-than-clear identity. | Keeps the outcome pending-unclear. | An unconfirmed anchor. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] |
| 5 · ACCEPTED | C-7L.3 — Person-Box proposal and identity events | The qualitative mention result. | Selects automatic linking or pending reference. | Identity link-layer state. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] |
| 6 · ACCEPTED | C-7L.3.7.1 — Person-Box mention-link event | The completely-clear test result. | Allows an automatic mention-link event only when met. | The link or pending outcome. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 7 · ACCEPTED | C-7L.3.7.3 — Person-Box anchor-confirmation event | Completely-clear source identity. | Allows automatic mention resolution under the authorized rule. | New confirmation history without rewriting pending history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 8 · ACCEPTED | C-7L.4 — Ness's confirmed Person-Box | The clear-source mention test. | Links clearly attributed Ness material automatically and leaves ambiguous material pending. | Honest attribution in Ness's box. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] |

SUB-PARTS: NONE

### C-7L.3.5 — Definite same-person test
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The qualitative test for joining two person records or boxes. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — Combined source-grounded evidence about the candidate pair. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Finds definitely identifiable as the same person only when no genuine identity question remains. A met test produces an automatic join; anything less stays a pending merge proposal. A pending proposal may later join on Ness's confirmation. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — A definite join or pending-not-definite proposal. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Treat similar labels as sufficient; invent a numerical threshold or ordinary-case manual approval; overwrite originals. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — Withholds an automatic join whenever the evidence is less than definite. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.3 — Person-Box proposal and identity events: determines the automatic-join or pending-proposal route. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.1 — Person-Box link record | The combined identity evidence. | Gates automatic joining. | A join only when definite. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] |
| 2 · ACCEPTED | C-7L.1.2 — Person-Box link why | Source evidence for the candidate pair. | Records why the join test was met. | Reviewable join provenance. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-7L.1.4.3 — Person-Box definite outcome | A met same-person test. | Allows definite. | Automatic join eligibility. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] |
| 4 · ACCEPTED | C-7L.1.4.4 — Person-Box pending-not-definite outcome | A remaining identity question. | Keeps pending-not-definite. | No silent join. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] |
| 5 · ACCEPTED | C-7L.3 — Person-Box proposal and identity events | The qualitative same-person result. | Selects automatic join or pending proposal. | Preserved identity history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 6 · ACCEPTED | C-7L.3.7.4.3 — Person-Box merge unmet-definite gap | The definite same-person criterion. | Identifies the remaining unmet identity question. | The named gap in the proposal. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 7 · ACCEPTED | C-7L.3.7.5 — Person-Box join event | A met definite test. | Permits an automatic join without additional approval. | One link-layer identity view. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 8 · ACCEPTED | C-7L.4 — Ness's confirmed Person-Box | The ordinary definite join test. | Applies it to stray anchors that may be Ness. | No special approval or certainty regime. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] |
| 9 · ACCEPTED | C-7L.6 — Person-Box cross-batch identity links | The unchanged definite same-person rule. | Applies it across sealed-batch boundaries. | Definite joins or pending proposals. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7L.3.6 — Ness Person-Box responses
Stamp: ACCEPTED    Source: [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The six available human responses to a person reference or identity proposal. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — Ness's explicit choice concerning an anchor, label, existing box or possible merge. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Records confirm, reject, rename, keep unresolved, link to an existing Person-Box or propose a merge through append-only events or links. These options remain available without becoming required for ordinary clear cases. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — A preserved response and any separately supported identity consequence. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Infer a response from silence; require a response for every clear link; rewrite earlier records or links. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7L.3.6.1 — Ness Person-Box confirmation: confirmation; C-7L.3.6.2 — Ness Person-Box rejection: rejection; C-7L.3.6.3 — Ness Person-Box rename: rename; C-7L.3.6.4 — Ness Person-Box keep unresolved: unresolved choice; C-7L.3.6.5 — Ness link to existing Person-Box: existing-box link; C-7L.3.6.6 — Ness Person-Box merge proposal: merge proposal. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gated by: ACCEPTED — Ness's actual response supplies the human choice; no approval is inferred. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3 — Person-Box proposal and identity events | Ness's identity response. | Records the response without replacing the clear-case tests. | New identity events or links. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 2 · ACCEPTED | C-7L.3.6.1 — Ness Person-Box confirmation | Ness's actual confirmation response. | Records confirmation without rewriting the pending history. | A new identity confirmation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 3 · ACCEPTED | C-7L.3.6.2 — Ness Person-Box rejection | Ness's actual rejection response. | Records rejection while preserving originals. | A new response event. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18] |
| 4 · ACCEPTED | C-7L.3.6.3 — Ness Person-Box rename | Ness's requested rename. | Adds a label change separately from stable identity. | New naming history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18] |
| 5 · ACCEPTED | C-7L.3.6.4 — Ness Person-Box keep unresolved | The option to leave the identity unresolved. | Retains pending status indefinitely. | No forced confirmation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] |
| 6 · ACCEPTED | C-7L.3.6.5 — Ness link to existing Person-Box | Ness's actual existing-box linking choice. | Records a new provenance-bearing link. | The reference's identity association. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 7 · ACCEPTED | C-7L.3.6.6 — Ness Person-Box merge proposal | Ness's proposal of a possible merge. | Keeps proposal separate from confirmation. | A new identity proposal. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 8 · ACCEPTED | C-AFFIRM.7.3 — Person-Box events retain their owner | The actual Person-Box response/event. | Supplies canonical Person-Box response handling. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §17] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: C-7L.3.6.1 — Ness Person-Box confirmation; C-7L.3.6.2 — Ness Person-Box rejection; C-7L.3.6.3 — Ness Person-Box rename; C-7L.3.6.4 — Ness Person-Box keep unresolved; C-7L.3.6.5 — Ness link to existing Person-Box; C-7L.3.6.6 — Ness Person-Box merge proposal

### C-7L.3.6.1 — Ness Person-Box confirmation
Stamp: ACCEPTED    Source: [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — Ness's explicit confirmation of an anchor or pending identity proposal. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — The exact anchor or pending proposal and Ness's confirmation. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Records confirmation; a join of a pending proposal follows as a distinct join event with constituent history preserved. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — An anchor-confirmation event or confirmed proposal followed by a join event. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Erase the uncertain history or silently treat a different proposal as confirmed. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7L.3.6 — Ness Person-Box responses: a real confirmation response is required for this human-response branch. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3.6 — Ness Person-Box responses | An explicit confirmation. | Preserves the choice and its target. | Recorded identity confirmation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 2 · ACCEPTED | C-7L.3.7.3 — Person-Box anchor-confirmation event | Ness's confirmation of the anchor. | Preserves that basis on a new confirmation event. | Anchor confirmation history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 3 · ACCEPTED | C-7L.3.7.5 — Person-Box join event | Ness's confirmation of a pending proposal. | Permits its join while preserving constituent history. | An authorized join event. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.3.6.2 — Ness Person-Box rejection
Stamp: ACCEPTED    Source: [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — Ness's rejection of a proposed identity connection. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — The rejected anchor or proposal and Ness's response. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Preserves the rejection as new history without deleting the underlying material. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — A recorded rejection. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Rewrite history or erase the rejected source reference. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7L.3.6 — Ness Person-Box responses: the rejection branch requires Ness's rejection. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3.6 — Ness Person-Box responses | The rejection response. | Keeps it distinct from a machine identity judgment. | Append-only response history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-7L.3.6.3 — Ness Person-Box rename
Stamp: ACCEPTED    Source: [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — A name or label change requested by Ness. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — The identity reference and the replacement human-readable label. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Adds naming history separately from the stable ID; earlier references remain intact. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — A new label or alias association. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Rename historical objects in place or change stable identity through wording alone. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7L.3.6 — Ness Person-Box responses: the rename branch follows Ness's requested name change. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3.6 — Ness Person-Box responses | The requested rename. | Preserves a new naming event. | Readable labels without historical rewrite. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-7L.3.6.4 — Ness Person-Box keep unresolved
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The option to leave an identity question unresolved. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Takes in: ACCEPTED — A pending identity anchor or merge proposal. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Does: ACCEPTED — Allows it to remain separate and unresolved indefinitely, including when Ness chooses no resolution. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Gives out: ACCEPTED — Continued pending identity state. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Must never: ACCEPTED — Treat waiting, repetition or silence as confirmation. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — No resolved identity or join is manufactured from an unresolved choice. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7L.3.6 — Ness Person-Box responses: the human-response options preserve indefinite nonresolution. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3.6 — Ness Person-Box responses | An unresolved identity question. | Keeps pending status available indefinitely. | No forced resolution. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7L.3.6.5 — Ness link to existing Person-Box
Stamp: ACCEPTED    Source: [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — Ness's explicit choice to link a reference to an existing Person-Box. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — The reference, the chosen existing box and Ness's response. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Records the new link with its provenance while leaving source objects and prior links intact. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — A link to the existing stable identity. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Copy the source or rewrite earlier uncertain-reference history. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7L.3.6 — Ness Person-Box responses: this response branch requires Ness's actual linking choice. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3.6 — Ness Person-Box responses | The selected existing identity. | Records the chosen connection. | A new provenance-bearing link. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.3.6.6 — Ness Person-Box merge proposal
Stamp: ACCEPTED    Source: [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — Ness's option to propose a possible identity merge. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — The candidate identities and the proposed connection. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Creates a separate proposal; proposing is not itself a confirmed join. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — A provenance-bearing merge proposal with the identity question preserved. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Treat the act of proposing as proof that the records are one person. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — The records remain separate until the join's authorized condition holds. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7L.3.6 — Ness Person-Box responses: this response branch follows Ness's proposal. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3.6 — Ness Person-Box responses | The proposed identity connection. | Keeps proposal distinct from confirmation. | A new pending identity question. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.3.7 — Person-Box append-only event family
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — The append-only records for links, anchor creation, confirmation, merge proposals, joins, corrections and aliases. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Takes in: ACCEPTED — The identity operation, its source evidence and the five settled link fields. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Does: ACCEPTED — Writes the corresponding event while preserving every original record and historical link. Records search occurrence and scope on resulting anchor/proposal events. Every real operation leaves exactly one append-only operation record. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Gives out: ACCEPTED — Inspectable identity history whose organization carries no extra evidential weight. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Must never: ACCEPTED — Edit, merge in storage, erase or rename historical records in place; promote an event to truth evidence; use logs or repeated events to raise certainty. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7L.1 — Person-Box link record: the five settled link fields; C-7L.3.7.1 — Person-Box mention-link event: mention link; C-7L.3.7.2 — Person-Box pending-anchor creation event: pending-anchor creation; C-7L.3.7.3 — Person-Box anchor-confirmation event: anchor confirmation; C-7L.3.7.4 — Person-Box merge-proposal record: merge proposal; C-7L.3.7.5 — Person-Box join event: join; C-7L.3.7.6 — Person-Box wrong-join correction event: correction; C-7L.3.7.7 — Person-Box alias record: alias. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Gated by: ACCEPTED — C-7L.3.3 — Person-Box search before propose: new anchors and proposals require the four-scope search recorded on the resulting event. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3 — Person-Box proposal and identity events | Append-only identity events. | Maintains link-layer state through preserved history. | Person-Box organization without evidence inflation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 2 · ACCEPTED | C-7L.1 — Person-Box link record | The event family's required link provenance. | Carries the five settled fields into each event. | The link record's event use. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 3 · ACCEPTED | C-7L.4 — Ness's confirmed Person-Box | The ordinary append-only event rules. | Maintains Ness's box through the same non-destructive history. | Ness's link and correction history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] |
| 4 · ACCEPTED | C-7L.14 — Person-Box operation and presentation records | The link-family operations and provenance. | Keeps one append-only record per real operation. | Inspectable identity-operation history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19] |

SUB-PARTS: C-7L.3.7.1 — Person-Box mention-link event; C-7L.3.7.2 — Person-Box pending-anchor creation event; C-7L.3.7.3 — Person-Box anchor-confirmation event; C-7L.3.7.4 — Person-Box merge-proposal record; C-7L.3.7.5 — Person-Box join event; C-7L.3.7.6 — Person-Box wrong-join correction event; C-7L.3.7.7 — Person-Box alias record

### C-7L.3.7.1 — Person-Box mention-link event
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The append-only event linking a root, reading or telling mention to a box. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — The original object, target box, source-grounded identity basis and settled link fields. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Records the connection; an automatic link carries the evidence satisfying completely clear. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — A mention-link event pointing to the original and stable identity. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Copy material or hide the basis of an automatic link. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — An unclear mention is kept as a pending anchor instead of a confirmed automatic link. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7L.3.4 — Completely-clear mention test: an automatic mention link needs the completely-clear source test. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3.7 — Person-Box append-only event family | A new mention connection. | Preserves its fields and evidence. | Append-only mention-link history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.3.7.2 — Person-Box pending-anchor creation event
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The append-only creation event for a pending identity anchor. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — The label/name, where, when, connecting evidence, current test outcome, link fields and recorded search scope. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Creates an unconfirmed anchor without asserting a resolved Person-Box identity. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — A preserved pending-anchor creation event. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Silently convert the anchor to a confirmed identity. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — Keeps the anchor pending while completely-clear identity is absent. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

TOGETHER
- Fed by: ACCEPTED — C-7L.2 — Uncertain identity anchor: all five uncertain-anchor fields. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gated by: ACCEPTED — C-7L.3.3 — Person-Box search before propose: the mandatory search must precede creation. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3.7 — Person-Box append-only event family | The new uncertain reference. | Records its creation and search provenance. | Append-only pending-anchor history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 2 · ACCEPTED | C-7L.2 — Uncertain identity anchor | The pending creation event's anchor content. | Supplies label, where, when, evidence and current outcome. | The pending anchor's recorded representation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.3.7.3 — Person-Box anchor-confirmation event
Stamp: ACCEPTED    Source: [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — A new event confirming a previously uncertain identity anchor under an authorized resolution. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — The anchor, confirmation basis and settled link fields. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Adds confirmation history without rewriting the prior uncertain reference. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — An anchor-confirmation event with its provenance. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Pretend an earlier pending anchor was always confirmed. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — Keeps the anchor unconfirmed when no authorized identity resolution is established. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

TOGETHER
- Fed by: ACCEPTED — C-7L.3.6.1 — Ness Person-Box confirmation: Ness's explicit confirmation where that response supplies the resolution. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gated by: ACCEPTED — C-7L.3.4 — Completely-clear mention test: automatic mention resolution requires completely-clear source identity. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3.7 — Person-Box append-only event family | An authorized anchor confirmation. | Preserves it as a new event. | Confirmation history beside the pending history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.3.7.4 — Person-Box merge-proposal record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The separate record proposing that two identity records may be the same person. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — Candidate pair, evidence gathered, named unmet-definite gap, settled link fields and search occurrence/scope. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Keeps the identity question pending without joining the records; name similarity remains motivation-only evidence. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — A pending merge proposal with an explicit unresolved gap. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Silently merge its candidates or treat the proposal as evidence of its own correctness. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — Less-than-definite evidence stays pending indefinitely unless an authorized resolution follows. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

TOGETHER
- Fed by: ACCEPTED — C-7L.3.7.4.1 — Person-Box merge candidate pair: candidate pair; C-7L.3.7.4.2 — Person-Box merge gathered evidence: gathered evidence; C-7L.3.7.4.3 — Person-Box merge unmet-definite gap: unmet-definite gap. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gated by: ACCEPTED — C-7L.3.3 — Person-Box search before propose: search before creating the proposal. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3.7 — Person-Box append-only event family | A possible identity join. | Preserves the proposal separately from any later join. | Pending identity history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 2 · ACCEPTED | C-7L.3.7.4.1 — Person-Box merge candidate pair | The merge proposal's pair requirement. | Names both candidate identities. | The candidate-pair field. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 3 · ACCEPTED | C-7L.3.7.4.2 — Person-Box merge gathered evidence | The proposal's source-evidence requirement. | Preserves gathered support without promoting similarity. | The gathered-evidence field. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 4 · ACCEPTED | C-7L.5.7 — Person-Box unresolved-identity section | Merge proposals and their named gaps. | Shows pending proposals without manufacturing certainty. | Visible identity questions. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |

SUB-PARTS: C-7L.3.7.4.1 — Person-Box merge candidate pair; C-7L.3.7.4.2 — Person-Box merge gathered evidence; C-7L.3.7.4.3 — Person-Box merge unmet-definite gap

### C-7L.3.7.4.1 — Person-Box merge candidate pair
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The two candidate identities in a merge proposal. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — References to the records or anchors being compared. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Names both candidates without modifying either. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — The proposal's candidate pair. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Combine candidate records merely by naming them together. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.3.7.4 — Person-Box merge-proposal record: supplies the candidate pair. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3.7.4 — Person-Box merge-proposal record | The two candidate references. | Identifies the proposed connection. | An unambiguous proposal target. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.3.7.4.2 — Person-Box merge gathered evidence
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The evidence gathered for a proposed same-person connection. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — Source-grounded support and any similarity-only motivation. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Preserves the evidence with its source basis; similar names stay motivation-only. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — Inspectable evidence for the candidate pair. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Turn similarity, age or repetition into sufficient identity proof. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.3.7.4 — Person-Box merge-proposal record: supplies the gathered evidence. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3.7.4 — Person-Box merge-proposal record | The gathered source evidence. | Shows what supports the proposal. | An auditable, non-self-validating basis. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.3.7.4.3 — Person-Box merge unmet-definite gap
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The named reason the proposal has not met the definite test. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — The genuine identity question remaining after the evidence is gathered. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Records the unmet-definite gap explicitly. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — A visible reason the records remain separate. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Conceal the unresolved gap or manufacture certainty to remove it. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — No automatic join occurs while the definite test remains unmet. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7L.3.5 — Definite same-person test: the definite criterion determines the remaining identity gap. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3.7.4 — Person-Box merge-proposal record | The unresolved identity question. | States the unmet-definite gap. | An honestly pending proposal. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.3.7.5 — Person-Box join event
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The append-only event joining identity anchors under one stable identity view. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — The candidate anchors, definite evidence or Ness's confirmation of a pending proposal, and settled link fields. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Joins automatically on a met definite test; otherwise joins only following Ness's confirmation of the pending proposal. Every constituent record, link and history remains where it is. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — One identity view with preserved constituent provenance. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Merge original storage, rewrite historical links or invent a manual-approval stage for a definite automatic join. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — An unmet definite test without Ness's confirmation leaves the proposal pending. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

TOGETHER
- Fed by: ACCEPTED — C-7L.3.6.1 — Ness Person-Box confirmation: confirmation of a pending proposal when that is the resolution basis. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gated by: ACCEPTED — C-7L.3.5 — Definite same-person test: automatic joining requires the definite same-person test. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3.7 — Person-Box append-only event family | The authorized identity join. | Records the unified view at the link layer. | New join history, originals unchanged. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 2 · ACCEPTED | C-7L.3.7.6 — Person-Box wrong-join correction event | The earlier mistaken join. | Re-separates the identity view through new events or links. | Correction history, originals preserved. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.3.7.6 — Person-Box wrong-join correction event
Stamp: ACCEPTED    Source: [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — A new event or link correcting a join later found wrong. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Takes in: ACCEPTED — The mistaken join and the correction identifying the needed separation. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Does: ACCEPTED — Re-separates the identity view through new events or links while keeping all earlier records and history. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gives out: ACCEPTED — A corrected current identity view with the mistaken join still inspectable. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Must never: ACCEPTED — Delete the wrong join, erase evidence or rewrite historical links. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7L.3.7.5 — Person-Box join event: the earlier join whose identity view is being corrected. [V10 §7L / PROPOSAL-BASED CREATION] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3.7 — Person-Box append-only event family | A correction to a mistaken join. | Appends the separation event or link. | Correction history without deletion. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.3.7.7 — Person-Box alias record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — An append-only name or label association separate from stable identity. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18]
- Takes in: ACCEPTED — A name or label and its Person-Box identity reference. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18]
- Does: ACCEPTED — Attaches the label separately; later naming changes add history rather than replacing old records. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18]
- Gives out: ACCEPTED — Alias history available to the mandatory identity search. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18]
- Must never: ACCEPTED — Rewrite old names in place or use a matching alias alone to prove identity. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.3.2 — Person-Box names labels and roles: supplies separately attached naming records. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.3.2 — Person-Box names labels and roles | Alias records. | Keeps readable names independent of the stable ID. | Mutable naming through preserved history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| 2 · ACCEPTED | C-7L.3.7 — Person-Box append-only event family | A new label association. | Preserves its append-only event. | Alias provenance. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.4 — Ness's confirmed Person-Box
Stamp: ACCEPTED    Source: [V10 §7L / SETTLED FACT] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Ness's existing confirmed Person-Box, anchored by a stable system-generated ID. [V10 §7L / SETTLED FACT] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9]
- Takes in: ACCEPTED — The settled fact that the box exists, clear source-identified Ness material, ambiguous references and later identity evidence. [V10 §7L / SETTLED FACT] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9]
- Does: ACCEPTED — Records the settled fact itself as confirmation provenance. Automatically links Ness's authored messages, source-resolved streams and clear first-person material. Leaves an unattributed I inside pasted third-party material pending. Applies the same fields, search, tests, correction history and seven-section view as other boxes. [V10 §7L / SETTLED FACT] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9]
- Gives out: ACCEPTED — A confirmed stable Ness identity with inspectable links and pending references where identity is unclear. [V10 §7L / SETTLED FACT] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9]
- Must never: ACCEPTED — Make its creation proposal-based or require an extra approval; assume every first-person statement is Ness; become a self-profile, diagnosis or personality model. [V10 §7L / SETTLED FACT] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Ambiguous first-person material follows the same pending-anchor rule as any unclear mention. [V10 §7L / SETTLED FACT] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9]

TOGETHER
- Fed by: DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): source and speaker/thread resolution for material attributed to Ness. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [V10 §7E]
- Fed by: ACCEPTED — C-7L.3.1 — Person-Box stable system ID: stable ID; C-7L.3.7 — Person-Box append-only event family: non-destructive identity history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-7L.3.4 — Completely-clear mention test: clear-source identity gates automatic links; C-7L.3.5 — Definite same-person test: later joins use the same definite test. [V10 §7L / SETTLED FACT] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9]
- Changes: DESIGNED — C-7D — Living State Web (§7D): supplies Ness's stable identity anchor under state rules; C-7M — Computed View (§7M): supplies permitted person-focused source links under its own derivation rules. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [MAP C-7L]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L — Person-Boxes (§7L) | Ness's confirmed anchor and linked source material. | Maintains it without a special approval regime. | Ness's identity view with preserved uncertainty. | [V10 §7L] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] |
| 2 · ACCEPTED | C-7L.11.7 — Enrollment confirmed Ness-box reference | Ness's confirmed stable identity. | Uses it as the provisional association's destination. | The confirmed-box reference. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 3 · DESIGNED | C-7D — Living State Web (§7D) | Permitted readings, tellings, clashes, Ness-response events and result evidence with root provenance. | Supplies the stable Ness anchor. | Nothing in this card. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §4B] [V10 §7D] [MAP C-7D] [V10 §7O] |
| 4 · ACCEPTED | C-ENROLL.2.6 — Confirmed Ness-box prerequisite | The actual Person-Box owner's confirmed identity reference. | Supplies the confirmed identity fact. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] |
| 5 · ACCEPTED | C-ENROLL.2 — Six-owner prerequisite check | I2 request `{ operation_ref }` and each real owner's `{ owner_ref, owner_version, satisfied }` response. | Supplies confirmed-box truth. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] |
| 6 · ACCEPTED | C-7D.15 — Proposed temporal-identity continuity link | Evidence linking states, positions, capacities, needs or relationship conditions across time, anchored to Ness's stable Person-Box. | Supplies stable Ness anchor. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §4B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §7] |
| 7 · DESIGNED | C-7M — Computed View (§7M) | Permitted roots, readings, tellings, clashes, Ness response events, Person-Box links, themes, Living State and world-model references, and safe metadata-only pre-ingest references. | Supplies Ness's confirmed person anchor. | Nothing in this card. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [V10 §7M] [MAP C-7M] |

SUB-PARTS: NONE

### C-7L.5 — Seven-section Person-Box view
Stamp: ACCEPTED    Source: [V10 §7L / DEFAULT VIEW] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — The seven separately headed sections of the Person-Box's default view. [V10 §7L / DEFAULT VIEW] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Takes in: ACCEPTED — Linked roots, readings, story tellings, clashes, Ness response events, themes, and unresolved identity anchors and merge proposals, with their owning-layer status labels. [V10 §7L / DEFAULT VIEW] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Does: ACCEPTED — Opens every section with its contents and evidential-status line. Shows compact lists by default and expands each item or section to full records and chains. Uses newest usable first where applicable; usable means acceptance passed, not rejected and not insufficient_context. Keeps other items visibly labeled, active clashes beside the item, and original chronology reachable. Groups reading modes separately when helpful; broader best-supported claims use Computed View ordering. Ness responses and newer-evidence-changed/replaced supersession labels affect grouping and labels only; preservation and clash records take precedence over grouping convenience. [V10 §7L / DEFAULT VIEW] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Gives out: ACCEPTED — A simple default view and complete on-demand records; one full-chronology switch across sections; visibly active composable filters. [V10 §7L / DEFAULT VIEW] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Must never: ACCEPTED — Flatten sections into equivalent claims; make section order, repetition or recency imply truth, importance or reliability; add a synthesis line, summary paragraph, personality strip or per-person score; recompute another layer's labels; hide a clash or rewrite an original. [V10 §7L / DEFAULT VIEW] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Fails closed by: ACCEPTED — For a hiding instruction covering Person-Box visible surfacing, the scoped targets remain withheld at evaluation on an unverified surface, including partially_enforced, blocked or failed enforcement; the surface supplies its acknowledgment and verification. Visible suppression alone does not remove internal influence. [04/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md §15]

TOGETHER
- Fed by: ACCEPTED — C-7L.5.1 — Person-Box roots section: roots; C-7L.5.2 — Person-Box readings section: readings; C-7L.5.3 — Person-Box story-tellings section: story tellings; C-7L.5.4 — Person-Box clashes section: clashes; C-7L.5.5 — Person-Box Ness-response section: Ness responses; C-7L.5.6 — Person-Box themes section: themes; C-7L.5.7 — Person-Box unresolved-identity section: unresolved identities and merge proposals; C-7L.5.8 — Person-Box view filters: filters; C-7L.5.9 — Person-Box full-chronology toggle: full chronology; C-7L.5.10 — Person-Box owning-layer status labels: owner-provided labels; C-7L.5.11 — Person-Box original-record cross-links: original-record cross-links. [V10 §7L / DEFAULT VIEW] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): visible use must be authorized before surfacing; C-SACL — Speaker Access-Control Layer (§25.4): applicable speaker restrictions remain in force. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §20] [V10 §25.2]
- Gated by: DESIGNED — C-7I — View Layer (§7I): its Current/History discipline governs the surface; C-7M — Computed View (§7M): any best-supported ordering follows its seven factors, with recency only a limited tie-breaker. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [MAP C-7I] [V10 §7M]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L — Person-Boxes (§7L) | Seven separate source-object sections. | Shows contents and evidence status without synthesizing a person. | Navigable identity view. | [V10 §7L] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |
| 2 · ACCEPTED | C-7L.5.1 — Person-Box roots section | Seven-section separation and contents/status lines. | Shows roots as their own source-object section. | The roots section. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |
| 3 · ACCEPTED | C-7L.5.2 — Person-Box readings section | Separate evidence statuses and current/history discipline. | Shows readings with their actual status and accessible chronology. | The readings section. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |
| 4 · ACCEPTED | C-7L.5.3 — Person-Box story-tellings section | The separate-telling presentation rule. | Shows perspective-owned tellings with owner-provided firmness. | The story-tellings section. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |
| 5 · ACCEPTED | C-7L.5.4 — Person-Box clashes section | The explicit conflict-surfacing rule. | Keeps clash type/status and detail visible. | The clashes section. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |
| 6 · ACCEPTED | C-7L.5.5 — Person-Box Ness-response section | The separate-response presentation rule. | Shows responses without treating them as rewritten evidence. | The Ness-response section. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |
| 7 · ACCEPTED | C-7L.5.6 — Person-Box themes section | The separate-theme presentation rule. | Shows theme confirmation status as navigation only. | The themes section. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |
| 8 · ACCEPTED | C-7L.5.7 — Person-Box unresolved-identity section | The separate unresolved-identity section rule. | Keeps anchors and proposals distinct and inspectable. | The unresolved-identity section. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |
| 9 · ACCEPTED | C-7L.5.9 — Person-Box full-chronology toggle | The always-available chronology requirement. | Supplies complete strict history one switch away. | Full chronological inspection. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |
| 10 · ACCEPTED | C-7L.5.10 — Person-Box owning-layer status labels | The distinct owning-layer evidence-status rule. | Shows every item's actual label without recomputation. | Visible evidential distinctions. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |
| 11 · ACCEPTED | C-7L.5.11 — Person-Box original-record cross-links | The pointer-only complete-on-demand rule. | Opens full original records and chains. | Inspectable source links. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |
| 12 · ACCEPTED | C-7L.14 — Person-Box operation and presentation records | Presented snapshot/version, active filters and history switches. | Records each view presentation. | Weightless presentation history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19] |
| 13 · ACCEPTED | C-7I.5 — View discipline in Person-Box presentation | The Person-Box's separately headed sections, actual evidence labels, filters and source pointers. | Supplies existing seven-section layout. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [MAP C-7I] |
| 14 · DESIGNED | C-7I — View Layer (§7I) | Readings in creation order with acceptance/usability status. | Supplies the Person-Box surface governed by the same presentation discipline. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] [V10 §7I] [MAP C-7I] |

SUB-PARTS: C-7L.5.1 — Person-Box roots section; C-7L.5.2 — Person-Box readings section; C-7L.5.3 — Person-Box story-tellings section; C-7L.5.4 — Person-Box clashes section; C-7L.5.5 — Person-Box Ness-response section; C-7L.5.6 — Person-Box themes section; C-7L.5.7 — Person-Box unresolved-identity section; C-7L.5.8 — Person-Box view filters; C-7L.5.9 — Person-Box full-chronology toggle; C-7L.5.10 — Person-Box owning-layer status labels; C-7L.5.11 — Person-Box original-record cross-links

### C-7L.5.1 — Person-Box roots section
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — Section 1, roots. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Takes in: ACCEPTED — Links to original roots concerning the person. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Does: ACCEPTED — States that the section contains roots and states their evidential status; keeps each original reachable and supports compact or expanded inspection. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Gives out: ACCEPTED — A separately headed roots list. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Must never: ACCEPTED — Flatten roots into equivalent claims with interpretations or imply authority from section order. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.5 — Seven-section Person-Box view: supplies the roots section. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.5 — Seven-section Person-Box view | Original-root pointers. | Renders the distinct roots section. | Source inspection without copies. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7L.5.2 — Person-Box readings section
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — Section 2, readings. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Takes in: ACCEPTED — Linked readings with their acceptance, rejected, revisable or insufficient_context labels. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Does: ACCEPTED — States contents and evidential status; surfaces newest usable first where applicable while alternatives remain labeled and full chronology reachable. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Gives out: ACCEPTED — A separate readings list with original records and active clashes visible. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Must never: ACCEPTED — Make a reading a fact through placement, hide rejected or insufficient-context history, or equate newest with best-supported. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.5 — Seven-section Person-Box view: supplies the readings section. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.5 — Seven-section Person-Box view | Readings with owner statuses. | Renders them distinctly from roots and tellings. | Inspectable interpretations and history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7L.5.3 — Person-Box story-tellings section
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Section 3, story tellings. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]
- Takes in: ACCEPTED — First-class telling_id references, their perspective roles and owning-layer firmness labels. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]
- Does: ACCEPTED — States contents and evidential status, displays each telling's actual perspective and firmness and links to its original record. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]
- Gives out: ACCEPTED — A distinct story-tellings list. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]
- Must never: ACCEPTED — Present a report as the subject's own perspective, recompute firmness or copy tellings into a second store. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Telling-specific use remains blocked until complete-set semantic eligibility holds. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-READ.10.14.2 — Person-Box references: stable telling references with preserved link provenance. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-READ.10.10.8 — Person-Box semantic links eligibility: complete valid telling-set eligibility before Person-Box semantic linking. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]
- Changes: ACCEPTED — C-7L.5 — Seven-section Person-Box view: supplies the tellings section. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.5 — Seven-section Person-Box view | Eligible perspective-owned tellings. | Displays their source status and firmness. | Separate narrative perspectives. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7L.5.4 — Person-Box clashes section
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Section 4, clashes. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — Linked clash records and their owner-provided type and status. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — States contents and evidential status. Opening the detail pane shows clash type, exact conflicting items as navigable pointers, what specifically conflicts, detection history, lifecycle and response status. Respond creates separate linked Ness-response events through the clash commit path, with a related reading affirmation event linked where appropriate; no resolve button exists. Clashes also remain beside affected items. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A separate conflict list with inspectable detail. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Resolve a clash, select its winner or hide it through grouping. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7J.8 — Clash and named-gap presentation: compact clash markers and full detail/response presentation. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.5 — Seven-section Person-Box view: supplies the clashes section. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.5 — Seven-section Person-Box view | Clash links with type/status labels. | Renders conflicts distinctly. | Visible unresolved disagreement. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |

SUB-PARTS: NONE

### C-7L.5.5 — Person-Box Ness-response section
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — Section 5, Ness-response events. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Takes in: ACCEPTED — Relevant separate Ness response-event references. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Does: ACCEPTED — States contents and evidential status; keeps judgments and responses distinct from original evidence, tellings and clashes. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Gives out: ACCEPTED — An inspectable response history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Must never: ACCEPTED — Treat Ness's response as a rewrite of a source or silently replace other perspectives. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.5 — Seven-section Person-Box view: supplies the Ness-response section. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.5 — Seven-section Person-Box view | Separate response records. | Displays the responses as their own evidence type. | Judgment distinguished from underlying history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7L.5.6 — Person-Box themes section
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — Section 6, themes. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Takes in: ACCEPTED — Linked themes with their proposed or confirmed status. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Does: ACCEPTED — States contents and evidential status and displays the owner-provided confirmation label as navigation rather than fact. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Gives out: ACCEPTED — A separate theme list with source links. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Must never: ACCEPTED — Confirm a theme through view order, recurrence or a Person-Box association. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7K.6.1 — Theme record: stable theme records and their status/version history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.5 — Seven-section Person-Box view: supplies the themes section. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.5 — Seven-section Person-Box view | Proposed and confirmed themes. | Shows navigational categories with status. | Theme navigation without factual promotion. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7L.5.7 — Person-Box unresolved-identity section
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — Section 7, unresolved identity anchors and merge proposals. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Takes in: ACCEPTED — Separate pending anchors and proposals with their evidence and unmet identity questions. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Does: ACCEPTED — States contents and evidential status, displays pending labels and makes the full anchor/proposal records and chains available on demand. Where an owning layer records an explicit absence, displays a named empty slot with what is absent and the owner-defined absence kind; it never infers content from the gap. Main wording stays plain, with precise grading vocabulary in side-drawer-grade notes. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Gives out: ACCEPTED — A visible list of unresolved identity questions. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Must never: ACCEPTED — Hide uncertainty in a summary, silently merge pending references, force a resolution to simplify the view, infer content from a recorded gap or treat absence as evidence. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — Pending identities can remain separate indefinitely. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: ACCEPTED — C-7L.2 — Uncertain identity anchor: unresolved anchors; C-7L.3.7.4 — Person-Box merge-proposal record: merge proposals with named unmet-definite gaps. C-7J.8.3 — Recorded named absence: recorded named absences shown as labeled empty slots without evidence weight. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.5 — Seven-section Person-Box view: supplies the unresolved-identity section. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.5 — Seven-section Person-Box view | Pending anchors and merge proposals. | Keeps their status and basis visible. | Honest unresolved identity presentation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7L.5.8 — Person-Box view filters
Stamp: ACCEPTED    Source: [V10 §7L / DEFAULT VIEW] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — The five composable filters of the Person-Box view. [V10 §7L / DEFAULT VIEW] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Takes in: ACCEPTED — Time, perspective role, theme, source/thread, and lifecycle or confirmation status selections. [V10 §7L / DEFAULT VIEW] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Does: ACCEPTED — Composes filters, keeps every active filter visibly indicated, and restores the default when filters are cleared. [V10 §7L / DEFAULT VIEW] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Gives out: ACCEPTED — A filtered or reorganized presentation with its active conditions visible. [V10 §7L / DEFAULT VIEW] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Must never: ACCEPTED — Rewrite records, conceal active filters or turn a filtered view into evidence that excluded material does not exist. [V10 §7L / DEFAULT VIEW] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7L.5.8.1 — Person-Box time filter: time; C-7L.5.8.2 — Person-Box perspective-role filter: perspective role; C-7L.5.8.3 — Person-Box theme filter: theme; C-7L.5.8.4 — Person-Box source-thread filter: source/thread; C-7L.5.8.5 — Person-Box lifecycle-confirmation filter: lifecycle or confirmation status. [V10 §7L / DEFAULT VIEW] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.5 — Seven-section Person-Box view | Visibly active filter selections. | Filters presentation without rewriting originals. | Reversible view organization. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |
| 2 · ACCEPTED | C-7L.5.8.1 — Person-Box time filter | The visible, composable, non-rewriting filter rule. | Applies the time scope to presentation. | The active time filter. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |
| 3 · ACCEPTED | C-7L.5.8.2 — Person-Box perspective-role filter | The visible, composable, non-rewriting filter rule. | Applies the perspective-role selection. | The active role filter. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |
| 4 · ACCEPTED | C-7L.5.8.3 — Person-Box theme filter | The visible, composable, non-rewriting filter rule. | Applies the theme selection without confirmation. | The active theme filter. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |
| 5 · ACCEPTED | C-7L.5.8.4 — Person-Box source-thread filter | The visible, composable, non-rewriting filter rule. | Applies source or thread selection. | The active source/thread filter. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |
| 6 · ACCEPTED | C-7L.5.8.5 — Person-Box lifecycle-confirmation filter | The visible, composable, non-rewriting filter rule. | Applies existing lifecycle or confirmation status. | The active status filter. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |
| 7 · ACCEPTED | C-7I.5 — View discipline in Person-Box presentation | The Person-Box's separately headed sections, actual evidence labels, filters and source pointers. | Supplies existing filter set and behavior. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [MAP C-7I] |

SUB-PARTS: C-7L.5.8.1 — Person-Box time filter; C-7L.5.8.2 — Person-Box perspective-role filter; C-7L.5.8.3 — Person-Box theme filter; C-7L.5.8.4 — Person-Box source-thread filter; C-7L.5.8.5 — Person-Box lifecycle-confirmation filter

### C-7L.5.8.1 — Person-Box time filter
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — The time selection in the Person-Box filter set. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Takes in: ACCEPTED — A requested time scope. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Does: ACCEPTED — Restricts presentation by time, visibly and in composition with other filters. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Gives out: ACCEPTED — Time-scoped displayed records. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Must never: ACCEPTED — Change timestamps or use recency as silent reliability. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.5.8 — Person-Box view filters: supplies the time selection. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.5.8 — Person-Box view filters | A time scope. | Applies it as a visible presentation filter. | Time-scoped navigation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7L.5.8.2 — Person-Box perspective-role filter
Stamp: ACCEPTED    Source: [V10 §7L / DEFAULT VIEW] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — The perspective-role selection in the Person-Box filter set. [V10 §7L / DEFAULT VIEW] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Takes in: ACCEPTED — The requested role in which a person occurs. [V10 §7L / DEFAULT VIEW] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Does: ACCEPTED — Filters by perspective role without equating speaker, subject and perspective owner. [V10 §7L / DEFAULT VIEW] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Gives out: ACCEPTED — Role-scoped displayed records. [V10 §7L / DEFAULT VIEW] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Must never: ACCEPTED — Change perspective attribution through filtering. [V10 §7L / DEFAULT VIEW] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.5.8 — Person-Box view filters: supplies the perspective-role selection. [V10 §7L / DEFAULT VIEW] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.5.8 — Person-Box view filters | A perspective-role selection. | Keeps it visibly active and composable. | Role-aware navigation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7L.5.8.3 — Person-Box theme filter
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — The theme selection in the Person-Box filter set. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Takes in: ACCEPTED — The requested theme scope and existing memberships. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Does: ACCEPTED — Filters displayed objects by their linked theme while preserving proposed or confirmed status. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Gives out: ACCEPTED — Theme-scoped navigation. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Must never: ACCEPTED — Confirm a theme or alter membership because a filter was applied. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.5.8 — Person-Box view filters: supplies the theme selection. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.5.8 — Person-Box view filters | A theme selection. | Applies it without rewriting records. | A visibly filtered theme view. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7L.5.8.4 — Person-Box source-thread filter
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — The source/thread selection in the Person-Box filter set. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Takes in: ACCEPTED — The requested source or thread scope. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Does: ACCEPTED — Uses preserved source/thread provenance to filter presentation. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Gives out: ACCEPTED — Source- or thread-scoped records. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Must never: ACCEPTED — Rewrite provenance or merge threads through view reorganization. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.5.8 — Person-Box view filters: supplies the source/thread selection. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.5.8 — Person-Box view filters | A source or thread scope. | Keeps the scope visible while active. | Provenance-aware navigation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7L.5.8.5 — Person-Box lifecycle-confirmation filter
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — The lifecycle or confirmation-status selection in the Person-Box filter set. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Takes in: ACCEPTED — Owner-provided lifecycle or confirmation labels. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Does: ACCEPTED — Filters by actual recorded status without recomputing or changing it. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Gives out: ACCEPTED — Status-scoped displayed objects. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Must never: ACCEPTED — Promote pending to confirmed or rewrite a lifecycle through filtering. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.5.8 — Person-Box view filters: supplies the lifecycle/confirmation selection. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.5.8 — Person-Box view filters | A status selection. | Applies it visibly and reversibly. | Status-aware navigation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |

SUB-PARTS: NONE

### C-7L.5.9 — Person-Box full-chronology toggle
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — The always-available single switch to full chronology across sections. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Takes in: ACCEPTED — The linked records' complete temporal history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Does: ACCEPTED — Shows strict, complete chronology one switch away from Current grouping. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Gives out: ACCEPTED — The full historical view. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Must never: ACCEPTED — Delete, permanently hide or overwrite history; make a filtered current arrangement replace chronological access. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.5 — Seven-section Person-Box view: supplies one-switch full history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.5 — Seven-section Person-Box view | Complete linked chronology. | Makes it available on demand. | History access beside compact current presentation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |
| 2 · ACCEPTED | C-7I.5 — View discipline in Person-Box presentation | The Person-Box's separately headed sections, actual evidence labels, filters and source pointers. | Supplies full chronology. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [MAP C-7I] |

SUB-PARTS: NONE

### C-7L.5.10 — Person-Box owning-layer status labels
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — The evidence-status labels supplied by each displayed item's actual owner. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Takes in: ACCEPTED — Reading statuses; firmness labels on tellings; theme proposed/confirmed; clash type and status; anchor/proposal pending status; Bundle 2 strength labels where retrieval supplied the item. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Does: ACCEPTED — Displays the labels as supplied and keeps different evidential statuses visually separate. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Gives out: ACCEPTED — An actual status label on every item. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Must never: ACCEPTED — Recompute firmness, strength, identity certainty or any other owning-layer label in the view. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.5 — Seven-section Person-Box view: supplies distinct evidence-status presentation. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.5 — Seven-section Person-Box view | The item's owner-provided status. | Displays without recomputation. | Visible evidence-type distinctions. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |
| 2 · ACCEPTED | C-7I.5 — View discipline in Person-Box presentation | The Person-Box's separately headed sections, actual evidence labels, filters and source pointers. | Supplies owning-layer labels. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [MAP C-7I] |
| 3 · ACCEPTED | C-AFFIRM.5.2 — Response-aware grouping and labels | The separate response record and existing view rules. | Supplies owner-supplied status labels. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §17] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-7L.5.11 — Person-Box original-record cross-links
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — The pointer-only route from displayed items to full original records and chains. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Takes in: ACCEPTED — Root, reading, telling, clash and response references. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Does: ACCEPTED — Lets each item or section expand and collapse to expose full records and chains; every item points back to its original. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Gives out: ACCEPTED — Complete on-demand inspection without a second object copy. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Must never: ACCEPTED — Copy originals into the view or make presentation an authoritative replacement. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.5 — Seven-section Person-Box view: supplies original-record inspection links. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.5 — Seven-section Person-Box view | Pointers to original records. | Exposes full detail on demand. | Traceable presentation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |
| 2 · ACCEPTED | C-7I.5 — View discipline in Person-Box presentation | The Person-Box's separately headed sections, actual evidence labels, filters and source pointers. | Supplies pointer-only complete-on-demand expansion. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [MAP C-7I] |

SUB-PARTS: NONE

### C-7L.6 — Person-Box cross-batch identity links
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The link-layer identity view over records in multiple distinct sealed batches. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Takes in: ACCEPTED — Person anchors and links carrying per-element batch identity and a cross-batch identity tag. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Does: ACCEPTED — Keeps link records beside the batches and pointing in. Connects the same person's links to one stable Person-Box ID while every element shows its batch provenance. Applies joins and corrections only at the link layer. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Gives out: ACCEPTED — One identity view with distinct batch-scoped originals. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Must never: ACCEPTED — Write into a sealed batch, merge content across seals, drop batch provenance or lower identity tests at a batch boundary. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — Across batches, less-than-definite identity stays a pending proposal; definite identity may join automatically. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]

TOGETHER
- Fed by: ACCEPTED — C-7L.6.1 — Person-Box per-element batch identity: per-element batch identity; C-7L.6.2 — Person-Box cross-batch identity tag: cross-batch identity tag. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Gated by: ACCEPTED — C-7L.3.5 — Definite same-person test: same-person joins across batches require the ordinary definite test or the authorized pending-proposal resolution. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L — Person-Boxes (§7L) | Batch-scoped person links. | Presents one identity without merging sealed content. | Cross-batch navigation and preserved provenance. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14] [V10 §7L] |
| 2 · ACCEPTED | C-7L.6.1 — Person-Box per-element batch identity | The per-element provenance requirement. | Keeps each element's batch identity visible. | Batch-scoped provenance. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14] |
| 3 · ACCEPTED | C-7L.6.2 — Person-Box cross-batch identity tag | The beside-the-batches link-layer boundary. | Connects batch-scoped links without merging content. | A cross-batch identity view. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14] |

SUB-PARTS: C-7L.6.1 — Person-Box per-element batch identity; C-7L.6.2 — Person-Box cross-batch identity tag

### C-7L.6.1 — Person-Box per-element batch identity
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The batch identity on each person anchor and link. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Takes in: ACCEPTED — The sealed batch from which the element came. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Does: ACCEPTED — Preserves that batch identity as per-element provenance and displays it in the identity view. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Gives out: ACCEPTED — An inspectable source-batch reference for every element. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Must never: ACCEPTED — Lose batch provenance when links are joined across batches. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.6 — Person-Box cross-batch identity links: supplies each element's batch identity. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.6 — Person-Box cross-batch identity links | The source-batch identity. | Keeps every element attributable to its batch. | Cross-batch provenance. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7L.6.2 — Person-Box cross-batch identity tag
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The tag tying the same person's links across batches to one stable Person-Box ID. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Takes in: ACCEPTED — Separately valid identity links and their stable person reference. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Does: ACCEPTED — Connects the batch-scoped links through records beside the batches. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Gives out: ACCEPTED — A cross-batch person identity reference. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Must never: ACCEPTED — Become a content merge across seals or substitute for the identity tests. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7L.3.1 — Person-Box stable system ID: the stable system-generated person ID. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.6 — Person-Box cross-batch identity links: supplies the cross-batch identity tag. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.6 — Person-Box cross-batch identity links | The tag and stable identity. | Organizes same-person links across batches. | One identity view without seal writes. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7L.7 — Person-Box Holding through linked objects
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The Person-Box use of Holding through existing, separate linked objects. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — Original roots, readings, perspective-owned tellings, Ness response events, clashes, themes, unresolved identity anchors and merge proposals. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Keeps Ness's understanding visibly separate from original evidence and other people's perspectives. Holds the understanding through links, retaining each object's own provenance and uncertainty. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — A linked person-related understanding without a replacement memory. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Create a separate profile, summary, fact-box or second memory store; turn an understanding into settled fact because it is repeated, recent or strongly held. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7K.7 — Holding through separate linked objects: the accepted shared Holding boundary and separate-object structure. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L — Person-Boxes (§7L) | Separate person-related understanding objects. | Maintains their distinct perspectives and provenance. | Holding within the linked gather. | [V10 §7L] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7L.8 — Person-Box held-material metadata boundary
Stamp: DESIGNED    Source: [V10 §7L / LINKABLE OBJECT TYPES] [MAP C-7L]

ALONE
- What it is: DESIGNED — The metadata-only link boundary for pre-ingest records concerning a person. [V10 §7L / LINKABLE OBJECT TYPES] [MAP C-7L]
- Takes in: DESIGNED — Safe source-carried metadata, lifecycle state and blocker information from held records. [V10 §7L / LINKABLE OBJECT TYPES] [MAP C-7L]
- Does: DESIGNED — Links only permitted metadata while held raw content remains invisible to Person-Box semantic analysis. A later explicitly authorized inspection design would be required for any general held-content inspection possibility. [V10 §7L / LINKABLE OBJECT TYPES] [MAP C-7L]
- Gives out: DESIGNED — A reference to the held record's safe metadata and status. [V10 §7L / LINKABLE OBJECT TYPES] [MAP C-7L]
- Must never: DESIGNED — Use held raw content for person interpretation or identity evidence; infer permission to inspect from the existence of a metadata link. Open a sealed TSC through the general future-inspection possibility or use its retained archive as ordinary memory. [V10 §7L / LINKABLE OBJECT TYPES] [MAP C-7L]
- Fails closed by: DESIGNED — Keeps held raw content outside Person-Box semantic analysis. [V10 §7L / LINKABLE OBJECT TYPES] [MAP C-7L]

TOGETHER
- Fed by: DESIGNED — C-7E.11 — Held-content access boundary: safe source-carried held metadata, lifecycle state and blockers, with raw content unavailable to this semantic consumer. [V10 §7L] [V10 §7E]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): metadata linking still requires the actual purpose's privacy authorization; C-TSC — Temporary Session Cache (§7E-TSC): sealed TSC content has no inspection path and remains inaccessible to Person-Boxes. [V10 §7Q] [04/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L — Person-Boxes (§7L) | Metadata-only pre-ingest references. | Keeps held contents outside semantic person analysis. | Safe status navigation only. | [V10 §7L] |

SUB-PARTS: NONE

### C-7L.9 — Person-Box permission-boundary read interface
Stamp: DESIGNED    Source: [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement]

ALONE
- What it is: DESIGNED — The Person-Box path through which authorized consumers read a person's active Permission Boundary Record (PBR). [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement]
- Takes in: DESIGNED — A person reference, active PBR, permission_categories, any ness_presence_required condition and the record's current version. [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement]
- Does: DESIGNED — Supplies PBR references through LMAC to SACL; SACL checks categories at output time and refreshes its recently-used PBR cache when the PBR version changes. PBR maintenance is informed by Ness's expressed boundaries and learned evidence under protected authority. [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement]
- Gives out: DESIGNED — An authorized active-PBR result for the requesting consumer. [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement]
- Must never: DESIGNED — Give another person authority over PBRs; transfer one person's permissions to another; treat a person link as disclosure permission; allow anyone to override the protected core. [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement]
- Fails closed by: DESIGNED — On PBR query failure, SACL Gate 3 fails closed and the stream becomes guest. [V10 §25.4 / Failure, Stale Assessments, Fail-Closed] [V10 §25.4 / Permission Boundary Enforcement]

TOGETHER
- Fed by: DESIGNED — C-7L.9.1 — Person-Box permission categories: permission categories; C-7L.9.2 — Person-Box Ness-presence permission condition: Ness-presence condition; C-7L.9.3 — Person-Box visibility restriction: Person-Box visibility restriction; C-7L.9.4 — Separate parent Person-Box identities: separate parent identities. [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement]
- Gated by: DESIGNED — C-7P — Permission & Authority Boundaries (§7P): protected authority governs PBR maintenance; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the actual query and use require privacy authorization. [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement]
- Changes: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): supplies the active PBR via the LMAC route for final category enforcement. [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L — Person-Boxes (§7L) | Permission-boundary references attached to separate identities. | Exposes only authorized PBR reads. | Person-specific permission inputs. | [V10 §25.2] [V10 §25.4] |
| 2 · DESIGNED | C-LMAC — Live Mechanism Access Coordinator (§26) | A PBR read for the requested person. | Routes it under privacy and authority results. | An authorized SACL input. | [V10 §25.4 / Permission Boundary Enforcement] |
| 3 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4) | The active PBR and current version. | Checks output categories and refreshes its cache on a version change. | Speaker-bounded disclosure. | [V10 §25.4 / Permission Boundary Enforcement] |
| 4 · DESIGNED | C-7L.9.1 — Person-Box permission categories | The active PBR's category contract. | Carries the permitted categories for output-time enforcement. | The category interface field. | [V10 §25.4 / Permission Boundary Enforcement] |
| 5 · DESIGNED | C-7L.9.2 — Person-Box Ness-presence permission condition | The active PBR's presence condition. | Preserves the Ness-stream requirement. | The presence-condition interface field. | [V10 §25.4 / Multi-Speaker Sessions] |
| 6 · DESIGNED | C-7L.9.3 — Person-Box visibility restriction | The privacy-bounded PBR/person read. | Restricts disclosure to current access without full-box inspection. | Person-Box visibility. | [V10 §25.2 / Person-Box Visibility] |
| 7 · DESIGNED | C-7L.9.4 — Separate parent Person-Box identities | Independently scoped person permissions. | Keeps both parent identities and their records separate. | No combined parent permission identity. | [V10 §25.2 / Separate Parent Identities] |
| 8 · DESIGNED | C-OTHER.3.3 — Known-person level | A confirmed non-Ness Person-Box recognized at threshold and a valid active PBR. | Supplies the active person's permission record. | Nothing in this card. | [V10 §25.2 / Access Levels] [V10 §25.4 / Permission Boundary Enforcement] |
| 9 · DESIGNED | C-SACL.9.3 — Version-refreshed PBR cache | Recently used PBRs and their version changes. | Supplies versioned PBR truth through LMAC. | Nothing in this card. | [V10 §25.4 / Permission Boundary Enforcement] |
| 10 · DESIGNED | C-OTHER.5 — Known-person permission boundaries | Ness's expressed boundaries, learned evidence and the active PBR's `permission_categories`. | Supplies what this place relies on: the active version is obtained through LMAC. | Nothing in this card. | [V10 §25.4 / Permission Boundary Enforcement] |
| 11 · DESIGNED | C-SACL.4.4.3 — Valid active non-revoked PBR | The applicable Permission Boundary Record. | Supplies PBR obtained through LMAC. | Nothing in this card. | [V10 §25.4 / Permission Boundary Enforcement] |
| 12 · ACCEPTED | C-SACL.20.11 — Handoff PBR references and categories | The current PBR references and permitted categories. | Supplies canonical PBR owner interface. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §13] [V10 §25.4 / Permission Boundary Enforcement] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §5] |
| 13 · DESIGNED | C-SACL.9.1 — Gate 3 PBR read route | The speaker's applicable PBR query. | Supplies PBR authority at the destination. | Nothing in this card. | [V10 §25.4 / Permission Boundary Enforcement] |
| 14 · DESIGNED | C-SACL.4.4 — Gate 3 known-person qualification | Confirmed non-Ness person reference, certainty, separation, active PBR, required-presence result and disqualifiers. | Supplies active PBR through LMAC. | Nothing in this card. | [V10 §25.4 / Permission Boundary Enforcement] |
| 15 · DESIGNED | C-OTHER — Other-Speaker / Guest / Known-Person Architecture (§25.2) | Speaker assessments, the current access level, person-specific permission boundaries and attributed third-party session material. | Supplies the active person's PBR reference. | Nothing in this card. | [V10 §25.2] [MAP C-OTHER] |
| 16 · ACCEPTED | C-LMAC.3.4 — Person-Box and PBR query contract | A box reference and the authorized requester/purpose. | Supplies the PBR object read for SACL. | Nothing in this card. | [V10 §25.4 / Permission Boundary Enforcement] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |

SUB-PARTS: C-7L.9.1 — Person-Box permission categories; C-7L.9.2 — Person-Box Ness-presence permission condition; C-7L.9.3 — Person-Box visibility restriction; C-7L.9.4 — Separate parent Person-Box identities

### C-7L.9.1 — Person-Box permission categories
Stamp: DESIGNED    Source: [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement]

ALONE
- What it is: DESIGNED — The permission_categories supplied by the active PBR. [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement]
- Takes in: DESIGNED — An open-ended category vocabulary, initially family_information, health_information, nh_project_information, creative_projects, current_plans, shared_memories and practical_information. [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement]
- Does: DESIGNED — Carries the person's currently permitted categories to the output-time SACL check. [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement]
- Gives out: DESIGNED — Category-bounded disclosure permissions. [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement]
- Must never: DESIGNED — Surface content outside the active permitted categories or treat a listed vocabulary category as an automatic grant. [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement]
- Fails closed by: DESIGNED — Content outside permitted categories is not surfaced to the known-person speaker. [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-7L.9 — Person-Box permission-boundary read interface: supplies the active permission_categories. [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L.9 — Person-Box permission-boundary read interface | The active category permissions. | Returns them for output-time enforcement. | Person-specific disclosure bounds. | [V10 §25.4 / Permission Boundary Enforcement] |
| 2 · DESIGNED | C-SACL.9.2 — Output-time PBR categories | The intended output and `permission_categories` in the active PBR. | Supplies the active PBR category list. | Nothing in this card. | [V10 §25.4 / Permission Boundary Enforcement] |
| 3 · DESIGNED | C-OTHER.7.5 — Private translation context and bounded disclosure | Private Ness context relevant to understanding the requested interaction and the parent's active PBR categories. | Supplies the parent's permitted categories. | Nothing in this card. | [V10 §25.2 / Parent Translation] |
| 4 · DESIGNED | C-OTHER.5 — Known-person permission boundaries | Ness's expressed boundaries, learned evidence and the active PBR's `permission_categories`. | Supplies the person's actual permitted category values. | Nothing in this card. | [V10 §25.4 / Permission Boundary Enforcement] |

SUB-PARTS: NONE

### C-7L.9.2 — Person-Box Ness-presence permission condition
Stamp: DESIGNED    Source: [V10 §25.4 / Multi-Speaker Sessions]

ALONE
- What it is: DESIGNED — The PBR condition ness_presence_required = true. [V10 §25.4 / Multi-Speaker Sessions]
- Takes in: DESIGNED — The known person's PBR and whether a Ness stream is active at recognized_ness or above. [V10 §25.4 / Multi-Speaker Sessions]
- Does: DESIGNED — Allows the known person's elevated access only while the qualifying Ness stream remains active. [V10 §25.4 / Multi-Speaker Sessions]
- Gives out: DESIGNED — A presence condition supplied to SACL. [V10 §25.4 / Multi-Speaker Sessions]
- Must never: DESIGNED — Continue elevated known-person access after the required Ness stream drops below recognized_ness. [V10 §25.4 / Multi-Speaker Sessions]
- Fails closed by: DESIGNED — When the qualifying Ness stream drops, the known-person stream drops to guest simultaneously. [V10 §25.4 / Multi-Speaker Sessions]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-7L.9 — Person-Box permission-boundary read interface: supplies the presence requirement with the PBR. [V10 §25.4 / Multi-Speaker Sessions]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L.9 — Person-Box permission-boundary read interface | The active presence requirement. | Preserves it in the PBR result. | A condition SACL enforces on access. | [V10 §25.4 / Multi-Speaker Sessions] |
| 2 · DESIGNED | C-SACL.4.4.4 — PBR-required Ness presence | The PBR's ness_presence_required value and current Ness stream. | Supplies the canonical PBR presence requirement. | Nothing in this card. | [V10 §25.4 / Multi-Speaker Sessions] |
| 3 · DESIGNED | C-SACL.8.3 — Simultaneous presence-loss downgrade | `ness_presence_required = true` and an active Ness stream's access. | Supplies whether this dependency applies. | Nothing in this card. | [V10 §25.4 / Multi-Speaker Sessions] |
| 4 · ACCEPTED | C-OTHER.13.2 — PBR and Ness-presence revalidation | The active PBR categories and whether the required Ness stream still has qualifying access. | Gates this place: the PBR's required Ness presence must still hold. | Nothing in this card. | [V10 §25.4 / Multi-Speaker Sessions] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13] |
| 5 · ACCEPTED | C-SACL.20.12 — Handoff required Ness presence | The presence requirement and qualifying Ness-stream authorization. | Supplies whether the dependency applies. | Nothing in this card. | [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §13] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7L.9.3 — Person-Box visibility restriction
Stamp: DESIGNED    Source: [V10 §25.2 / Person-Box Visibility]

ALONE
- What it is: DESIGNED — The disclosure boundary protecting a Person-Box from inspection by another person. [V10 §25.2 / Person-Box Visibility]
- Takes in: DESIGNED — A request concerning that person's linked material and the current speaker access level. [V10 §25.2 / Person-Box Visibility]
- Does: DESIGNED — Answers only from what the current access level permits. [V10 §25.2 / Person-Box Visibility]
- Gives out: DESIGNED — Permitted content without indirect disclosure of stored private material. [V10 §25.2 / Person-Box Visibility]
- Must never: DESIGNED — Allow another person to inspect their full Person-Box, hidden readings, private observations, internal relationship models or stored security information; reveal how much is stored or how recognition works. [V10 §25.2 / Person-Box Visibility]
- Fails closed by: DESIGNED — Withholds material outside current access without signaling that hidden material exists. [V10 §25.2 / Person-Box Visibility]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): current speaker access bounds the answer; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): disclosure requires privacy authorization. [V10 §25.2 / Person-Box Visibility]
- Changes: DESIGNED — C-7L.9 — Person-Box permission-boundary read interface: preserves the visibility boundary of person-related reads. [V10 §25.2 / Person-Box Visibility]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L.9 — Person-Box permission-boundary read interface | A request for person-related material. | Keeps full-box inspection unavailable to another person. | Only permitted disclosure. | [V10 §25.2 / Person-Box Visibility] |
| 2 · DESIGNED | C-OTHER.9 — Person-Box visibility for other speakers | The person's request and current speaker access level. | Supplies the canonical person-information disclosure boundary. | Nothing in this card. | [V10 §25.2 / Person-Box Visibility] |

SUB-PARTS: NONE

### C-7L.9.4 — Separate parent Person-Box identities
Stamp: DESIGNED    Source: [V10 §25.2 / Separate Parent Identities]

ALONE
- What it is: DESIGNED — The requirement that each parent remains a separate person identity. [V10 §25.2 / Separate Parent Identities]
- Takes in: DESIGNED — Each parent's Person-Box, voice profile, behavioral pattern readings, PBR, relationship context and translation behavior history. [V10 §25.2 / Separate Parent Identities]
- Does: DESIGNED — Keeps all of those structures fully separate for each parent. [V10 §25.2 / Separate Parent Identities]
- Gives out: DESIGNED — Independent parent identities and their associated records. [V10 §25.2 / Separate Parent Identities]
- Must never: DESIGNED — Treat parents as one combined person or transfer one parent's permissions or identity authority to the other. [V10 §25.2 / Separate Parent Identities]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-7L.9 — Person-Box permission-boundary read interface: supplies separately scoped parent identities and permission records. [V10 §25.2 / Separate Parent Identities]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L.9 — Person-Box permission-boundary read interface | Each parent's own identity and PBR. | Maintains independent permission scope. | Separate person-bound reads. | [V10 §25.2 / Separate Parent Identities] |
| 2 · DESIGNED | C-OTHER.6 — Separate parent records | Each parent's own Person-Box, voice profile, behavioral pattern readings, PBR, relationship context in the Living State Web and translation behavior history. | Supplies the canonical independently scoped parent identities and associated records. | Nothing in this card. | [V10 §25.2 / Separate Parent Identities] |

SUB-PARTS: NONE

### C-7L.10 — Voice-profile Person-Box linking boundary
Stamp: DESIGNED    Source: [V10 §25.3 / Voice Profile Architecture] [V10 §25.3 / Minimum Evidence for Person-Box Linking]

ALONE
- What it is: DESIGNED — The Person-Box identity-link boundary for ordinary voice-profile material and previously unknown speakers. [V10 §25.3 / Voice Profile Architecture] [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Takes in: DESIGNED — Profile readings in the shared store and the six required evidence conditions for linking an unknown speaker. [V10 §25.3 / Voice Profile Architecture] [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Does: DESIGNED — Links readings through the person identity without a separate profile store. Keeps identity authority independent despite a common technical embedding space. Before an unknown speaker link, requires sufficient attributed material, capture-time certainty, no spoofing flags, authorized promotion and processing, sufficient reading confidence and the Person-Box identity rules. [V10 §25.3 / Voice Profile Architecture] [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Gives out: DESIGNED — Separately attributable profile-reading links. [V10 §25.3 / Voice Profile Architecture] [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Must never: DESIGNED — Merge profiles, share identity authority, silently reassign identity or interpret a common embedding space as shared identity. [V10 §25.3 / Voice Profile Architecture] [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Fails closed by: DESIGNED — An unknown speaker link does not proceed unless all six evidence requirements hold. [V10 §25.3 / Voice Profile Architecture] [V10 §25.3 / Minimum Evidence for Person-Box Linking]

TOGETHER
- Fed by: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): profile readings and the identity-assessment facts it owns. [V10 §25.3 / Voice Profile Architecture] [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Gated by: DESIGNED — C-7L.10.1 — Unknown-speaker attributed-material minimum: material quantity; C-7L.10.2 — Unknown-speaker capture-time certainty minimum: capture-time certainty; C-7L.10.3 — Unknown-speaker no-spoofing condition: spoofing absence; C-7L.10.4 — Unknown-speaker authorized-promotion condition: authorized promotion and processing; C-7L.10.5 — Unknown-speaker reading-confidence minimum: reading confidence; C-7L.10.6 — Unknown-speaker Person-Box rule condition: identity-link rules. [V10 §25.3 / Voice Profile Architecture] [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Changes: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): supplies permitted links to separate person identities. [V10 §25.3 / Voice Profile Architecture] [V10 §25.3 / Minimum Evidence for Person-Box Linking]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L — Person-Boxes (§7L) | Voice-related readings with the linking prerequisites. | Maintains independently grounded identity links. | Profile references without silent reassignment. | [V10 §25.3] |
| 2 · DESIGNED | C-SIA — Speaker Identity Assessment (§25.3) | Separate Person-Box links. | Uses the source readings under its own profile rules. | Independent identity assessments. | [V10 §25.3 / Voice Profile Architecture] |
| 3 · DESIGNED | C-7L.10.1 — Unknown-speaker attributed-material minimum | The ordinary unknown-speaker linking prerequisites. | Requires the minimum quantity across authorized sessions. | The quantity condition. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| 4 · DESIGNED | C-7L.10.2 — Unknown-speaker capture-time certainty minimum | The capture-time evidence prerequisite. | Requires certainty above the minimum at capture. | The attribution condition. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| 5 · DESIGNED | C-7L.10.3 — Unknown-speaker no-spoofing condition | The clean attributed-material prerequisite. | Requires no spoofing flags. | The spoofing condition. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| 6 · DESIGNED | C-7L.10.4 — Unknown-speaker authorized-promotion condition | The authorized material-path prerequisite. | Requires fingerprint-authorized promotion and completed processing. | The promotion/processing condition. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| 7 · DESIGNED | C-7L.10.5 — Unknown-speaker reading-confidence minimum | The reading-support prerequisite. | Requires support above the minimum reading confidence. | The reading-confidence condition. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| 8 · DESIGNED | C-7L.10.6 — Unknown-speaker Person-Box rule condition | The Person-Box-rule prerequisite. | Requires valid identity resolution without a silent merge. | The identity-rule condition. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| 9 · DESIGNED | C-SIA.9 — Independent voice profiles | Sets of profile readings linked through §7L. | Gates this place: unknown-speaker linkage must satisfy the decided minimum evidence and proposal rules. | Nothing in this card. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |

SUB-PARTS: C-7L.10.1 — Unknown-speaker attributed-material minimum; C-7L.10.2 — Unknown-speaker capture-time certainty minimum; C-7L.10.3 — Unknown-speaker no-spoofing condition; C-7L.10.4 — Unknown-speaker authorized-promotion condition; C-7L.10.5 — Unknown-speaker reading-confidence minimum; C-7L.10.6 — Unknown-speaker Person-Box rule condition

### C-7L.10.1 — Unknown-speaker attributed-material minimum
Stamp: DESIGNED    Source: [V10 §25.3 / Minimum Evidence for Person-Box Linking]

ALONE
- What it is: DESIGNED — The required minimum quantity of attributed voice material across authorized sessions. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Takes in: DESIGNED — The attributed voice material and its session authorization. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Does: DESIGNED — Requires the source-defined minimum quantity before linking an unknown speaker. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Gives out: DESIGNED — A quantity prerequisite for the identity link. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Must never: DESIGNED — Count material from unauthorized sessions toward this requirement. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Fails closed by: DESIGNED — The unknown-speaker link remains blocked without the required quantity. [V10 §25.3 / Minimum Evidence for Person-Box Linking]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-7L.10 — Voice-profile Person-Box linking boundary: supplies the attributed-material quantity condition. [V10 §25.3 / Minimum Evidence for Person-Box Linking]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L.10 — Voice-profile Person-Box linking boundary | Attributed authorized-session material. | Requires the minimum before linking. | Quantity-bounded link eligibility. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| 2 · DESIGNED | C-SIA.17 — Unknown-speaker linking evidence | Attributed voice material across authorized sessions, capture-time certainty, spoofing flags, promotion provenance, supporting readings and the §7L proposal rules. | Gates this place: minimum quantity across authorized sessions. | Nothing in this card. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |

SUB-PARTS: NONE

### C-7L.10.2 — Unknown-speaker capture-time certainty minimum
Stamp: DESIGNED    Source: [V10 §25.3 / Minimum Evidence for Person-Box Linking]

ALONE
- What it is: DESIGNED — The requirement for attribution certainty above the minimum at capture time. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Takes in: DESIGNED — The attributed material's certainty when captured. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Does: DESIGNED — Uses capture-time certainty for the prerequisite, rather than a later assumption about who spoke. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Gives out: DESIGNED — A capture-time attribution condition. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Must never: DESIGNED — Substitute retrospective certainty for the required capture-time attribution. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Fails closed by: DESIGNED — The unknown-speaker link remains blocked when this minimum is not met. [V10 §25.3 / Minimum Evidence for Person-Box Linking]

TOGETHER
- Fed by: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): the capture-time attribution assessment. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-7L.10 — Voice-profile Person-Box linking boundary: supplies the capture-time certainty condition. [V10 §25.3 / Minimum Evidence for Person-Box Linking]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L.10 — Voice-profile Person-Box linking boundary | Capture-time attribution certainty. | Requires it above the minimum. | Evidence-bounded link eligibility. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| 2 · DESIGNED | C-SIA.17 — Unknown-speaker linking evidence | Attributed voice material across authorized sessions, capture-time certainty, spoofing flags, promotion provenance, supporting readings and the §7L proposal rules. | Gates this place: certainty above minimum at capture. | Nothing in this card. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |

SUB-PARTS: NONE

### C-7L.10.3 — Unknown-speaker no-spoofing condition
Stamp: DESIGNED    Source: [V10 §25.3 / Minimum Evidence for Person-Box Linking]

ALONE
- What it is: DESIGNED — The absence of spoofing flags on attributed material used for an unknown-speaker link. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Takes in: DESIGNED — The attributed material's spoofing flags. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Does: DESIGNED — Requires that the material has no spoofing flags. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Gives out: DESIGNED — A clean-spoofing-condition prerequisite. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Must never: DESIGNED — Use flagged material to satisfy this requirement. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Fails closed by: DESIGNED — The unknown-speaker link remains blocked when spoofing flags are present. [V10 §25.3 / Minimum Evidence for Person-Box Linking]

TOGETHER
- Fed by: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): the spoofing assessment for the attributed material. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-7L.10 — Voice-profile Person-Box linking boundary: supplies the no-spoofing condition. [V10 §25.3 / Minimum Evidence for Person-Box Linking]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L.10 — Voice-profile Person-Box linking boundary | The material's spoofing status. | Requires no spoofing flags. | Protected identity-link eligibility. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| 2 · DESIGNED | C-SIA.17 — Unknown-speaker linking evidence | Attributed voice material across authorized sessions, capture-time certainty, spoofing flags, promotion provenance, supporting readings and the §7L proposal rules. | Gates this place: no spoofing flags on the material. | Nothing in this card. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |

SUB-PARTS: NONE

### C-7L.10.4 — Unknown-speaker authorized-promotion condition
Stamp: DESIGNED    Source: [V10 §25.3 / Minimum Evidence for Person-Box Linking]

ALONE
- What it is: DESIGNED — The requirement that the material passed fingerprint-authorized TSC promotion and meaning processing. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Takes in: DESIGNED — The TSC promotion authorization and completed reading-path evidence. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Does: DESIGNED — Requires promotion through the fingerprint-authorized path and processing by the Meaning Engine before the unknown-speaker link. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Gives out: DESIGNED — A promoted-and-processed material prerequisite. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Must never: DESIGNED — Use unpromoted TSC material or bypass the required fingerprint-authorized path. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Fails closed by: DESIGNED — Without the authorized promotion and processing, the link does not proceed. [V10 §25.3 / Minimum Evidence for Person-Box Linking]

TOGETHER
- Fed by: DESIGNED — C-TSC — Temporary Session Cache (§7E-TSC): fingerprint-authorized promotion evidence; C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): completed processing and reading evidence. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-7L.10 — Voice-profile Person-Box linking boundary: supplies the authorized-promotion and processing condition. [V10 §25.3 / Minimum Evidence for Person-Box Linking]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L.10 — Voice-profile Person-Box linking boundary | Authorized promotion and completed processing. | Requires both before linking. | A link grounded only in eligible processed material. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| 2 · DESIGNED | C-SIA.17 — Unknown-speaker linking evidence | Attributed voice material across authorized sessions, capture-time certainty, spoofing flags, promotion provenance, supporting readings and the §7L proposal rules. | Gates this place: fingerprint-authorized promotion and §7G processing. | Nothing in this card. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |

SUB-PARTS: NONE

### C-7L.10.5 — Unknown-speaker reading-confidence minimum
Stamp: DESIGNED    Source: [V10 §25.3 / Minimum Evidence for Person-Box Linking]

ALONE
- What it is: DESIGNED — The requirement that meaning readings support the identity connection above the minimum reading confidence. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Takes in: DESIGNED — The relevant reading support and confidence. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Does: DESIGNED — Requires support above the minimum before linking an unknown speaker. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Gives out: DESIGNED — A reading-evidence prerequisite. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Must never: DESIGNED — Invent a confidence value or treat insufficient support as a met requirement. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Fails closed by: DESIGNED — The unknown-speaker link remains blocked when sufficient reading support is absent. [V10 §25.3 / Minimum Evidence for Person-Box Linking]

TOGETHER
- Fed by: DESIGNED — C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): the reading and its confidence/support evidence. [V10 §25.3 / Minimum Evidence for Person-Box Linking]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-7L.10 — Voice-profile Person-Box linking boundary: supplies the reading-support condition. [V10 §25.3 / Minimum Evidence for Person-Box Linking]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L.10 — Voice-profile Person-Box linking boundary | Reading support for the connection. | Requires confidence above the minimum. | Evidence-bounded link eligibility. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| 2 · DESIGNED | C-SIA.17 — Unknown-speaker linking evidence | Attributed voice material across authorized sessions, capture-time certainty, spoofing flags, promotion provenance, supporting readings and the §7L proposal rules. | Gates this place: reading support above minimum confidence. | Nothing in this card. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |

SUB-PARTS: NONE

### C-7L.10.6 — Unknown-speaker Person-Box rule condition
Stamp: DESIGNED    Source: [V10 §25.3 / Minimum Evidence for Person-Box Linking] [V10 §7L]

ALONE
- What it is: DESIGNED — The requirement that an unknown-speaker link satisfies Person-Box identity rules without a silent merge. [V10 §25.3 / Minimum Evidence for Person-Box Linking] [V10 §7L]
- Takes in: DESIGNED — The speaker reference and applicable proposal, evidence and resolution basis. [V10 §25.3 / Minimum Evidence for Person-Box Linking] [V10 §7L]
- Does: DESIGNED — Keeps uncertain references under proposal-based creation and requires the authorized identity resolution. [V10 §25.3 / Minimum Evidence for Person-Box Linking] [V10 §7L]
- Gives out: DESIGNED — A link only within Person-Box identity authority. [V10 §25.3 / Minimum Evidence for Person-Box Linking] [V10 §7L]
- Must never: DESIGNED — Use voice-profile convenience to bypass the clear/unclear distinction or silently merge identities. [V10 §25.3 / Minimum Evidence for Person-Box Linking] [V10 §7L]
- Fails closed by: DESIGNED — An unsupported identity remains unresolved. [V10 §25.3 / Minimum Evidence for Person-Box Linking] [V10 §7L]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7L.3 — Person-Box proposal and identity events: the accepted search, qualitative evidence and non-destructive identity rules govern resolution. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Changes: DESIGNED — C-7L.10 — Voice-profile Person-Box linking boundary: supplies the Person-Box identity-rule condition. [V10 §25.3 / Minimum Evidence for Person-Box Linking] [V10 §7L]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L.10 — Voice-profile Person-Box linking boundary | The identity-rule result. | Requires valid Person-Box resolution. | No silent identity merge. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| 2 · DESIGNED | C-SIA.17 — Unknown-speaker linking evidence | Attributed voice material across authorized sessions, capture-time certainty, spoofing flags, promotion provenance, supporting readings and the §7L proposal rules. | Gates this place: proposal rules and no silent merge. | Nothing in this card. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |

SUB-PARTS: NONE

### C-7L.11 — Provisional enrollment Person-Box link
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — The provisional material link owned and committed by Person-Boxes after the enrollment component proposes it. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — link_type = enrollment_material_provisional; certainty = enrollment_provisional; provisional_link_proposal_id; the proposed enrollment_profile_input_bundle reference; confirmed Ness Person-Box; operation/session references; exact eligible reading set; exact eligibility decisions; prerequisite and authorization evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Records that material came through Ness's authorized enrollment flow, not that the voice was confirmed as Ness. Owns the proposal outcome and actual link state. Uses one stable proposal ID so replay cannot create a duplicate; recovery queries Person-Boxes with that ID. Only current committed link truth permits the later SIA profile handoff. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — A recorded proposal and later COMMITTED link truth, refused or pending result; the enrollment_provisional_link_proposed audit marks the proposal only. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Let the enrollment coordinator approve, merge or become identity authority; treat a proposal or acknowledgment as a committed link; reference an already-created SIA profile instead of the frozen proposed input bundle; convert enrollment provenance into voice identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: ACCEPTED — Refused, pending, stale, contradictory or unverifiable link results block SIA profile creation. The link must come before the profile. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): the provisional-link proposal and exact frozen input references; the coordinator only proposes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fed by: ACCEPTED — C-7L.11.1 — Enrollment provisional link type: link type; C-7L.11.2 — Enrollment provisional link certainty: provisional certainty; C-7L.11.3 — Enrollment provisional link proposal ID: stable proposal ID; C-7L.11.4 — Enrollment provisional link meaning: provenance meaning; C-7L.11.5 — Enrollment provisional link basis: authorization basis; C-7L.11.6 — Enrollment proposed input-bundle reference: proposed input-bundle reference; C-7L.11.7 — Enrollment confirmed Ness-box reference: confirmed-box reference; C-7L.11.8 — Enrollment link operation reference: operation reference; C-7L.11.9 — Enrollment link session reference: session reference; C-7L.11.10 — Enrollment link eligible-reading references: eligible reading set; C-7L.11.11 — Enrollment link eligibility-decision references: eligibility decisions; C-7L.11.12 — Enrollment link prerequisite-evidence references: prerequisite/authorization evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gated by: ACCEPTED — C-7L.11.13 — Enrollment committed-link handoff gate: a current Person-Box-owned committed link is required before SIA profile creation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Changes: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): releases the linked reading set for its own profile rules only after current committed link truth; C-ENROLL — Initial Ness voice-profile enrollment (§25.11): supplies the actual proposal outcome and link state for recovery. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L — Person-Boxes (§7L) | The provisional enrollment link proposal. | Owns its outcome and committed link truth. | A provenance-only provisional material association. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 2 · DESIGNED | C-SIA — Speaker Identity Assessment (§25.3) | Current committed link truth and linked reading references. | Consumes readings as one input, then may commit the actual provisional profile under its own rules. | No profile before the link. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |
| 3 · DESIGNED | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | The actual owner-returned link result. | Queries by proposal ID after uncertainty and waits for committed truth. | Coordination state without identity authority. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 4 · ACCEPTED | C-7L.11.1 — Enrollment provisional link type | The provisional-material link contract. | Names enrollment_material_provisional as its link type. | The link_type field. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 5 · ACCEPTED | C-7L.11.2 — Enrollment provisional link certainty | The provenance-only certainty contract. | Carries enrollment_provisional without voice confirmation. | The certainty field. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 6 · ACCEPTED | C-7L.11.3 — Enrollment provisional link proposal ID | The replay-safe proposal identity requirement. | Preserves one provisional_link_proposal_id for lookup. | Idempotent proposal identity. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 7 · ACCEPTED | C-7L.11.4 — Enrollment provisional link meaning | The required explicit provenance meaning. | States authorized collection without identifying the voice. | The link's meaning statement. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 8 · ACCEPTED | C-7L.11.5 — Enrollment provisional link basis | The narrow owner-held enrollment basis. | References consumed token, phone trust and declared enrollment attribution. | The basis field. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 9 · ACCEPTED | C-7L.11.6 — Enrollment proposed input-bundle reference | The frozen-input, link-before-profile requirement. | Points to the proposed input bundle, not a prior profile. | The proposed input-bundle reference. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 10 · ACCEPTED | C-7L.11.7 — Enrollment confirmed Ness-box reference | The confirmed destination requirement. | References the existing Ness box. | The box-target field. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 11 · ACCEPTED | C-7L.11.8 — Enrollment link operation reference | The enrollment provenance requirements. | Carries the exact operation reference. | Operation provenance. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 12 · ACCEPTED | C-7L.11.9 — Enrollment link session reference | The enrollment provenance requirements. | Carries the exact session reference. | Session provenance. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 13 · ACCEPTED | C-7L.11.10 — Enrollment link eligible-reading references | The exact-input requirement. | References the frozen eligible reading set. | The eligible-reading reference field. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 14 · ACCEPTED | C-7L.11.11 — Enrollment link eligibility-decision references | The eligibility-provenance requirement. | References the exact eligibility decisions. | The eligibility-decision field. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 15 · ACCEPTED | C-7L.11.12 — Enrollment link prerequisite-evidence references | The owner-evidence requirement. | Keeps prerequisite and authorization references. | The prerequisite-evidence field. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 16 · ACCEPTED | C-ENROLL.15.17 — Recovery after link-proposal submission | `enrollment_provisional_link_proposed` and the stable `provisional_link_proposal_id` [proposed]. | Owns the queried outcome. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |
| 17 · ACCEPTED | C-ENROLL.6.22 — Provisional link proposed state | `enrollment_provisional_link_proposed`. | Supplies the owner-returned proposal status. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 18 · ACCEPTED | C-ENROLL.6.25 — Completed parent state | All four facts: Person-Box-owned committed link, SIA-owned committed profile, `enrollment_provisional_link_proposed` and `enrollment_provisional_profile_created`. | Supplies link commitment. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |
| 19 · ACCEPTED | C-ENROLL.6 — Enrollment process lifecycle | Actual committed facts from each stage's owner. | Supplies link truth. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] |
| 20 · ACCEPTED | C-ENROLL.11.1 — Stable link-proposal recovery identity | The operation's exact frozen proposal inputs. | Supplies actual query result. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 21 · ACCEPTED | C-ENROLL.15 — Enrollment crash recovery | The real interruption point and authoritative committed owner facts. | Supplies actual link truth. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |

SUB-PARTS: C-7L.11.1 — Enrollment provisional link type; C-7L.11.2 — Enrollment provisional link certainty; C-7L.11.3 — Enrollment provisional link proposal ID; C-7L.11.4 — Enrollment provisional link meaning; C-7L.11.5 — Enrollment provisional link basis; C-7L.11.6 — Enrollment proposed input-bundle reference; C-7L.11.7 — Enrollment confirmed Ness-box reference; C-7L.11.8 — Enrollment link operation reference; C-7L.11.9 — Enrollment link session reference; C-7L.11.10 — Enrollment link eligible-reading references; C-7L.11.11 — Enrollment link eligibility-decision references; C-7L.11.12 — Enrollment link prerequisite-evidence references; C-7L.11.13 — Enrollment committed-link handoff gate

### C-7L.11.1 — Enrollment provisional link type
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The link_type field of the enrollment proposal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Takes in: ACCEPTED — The literal enrollment_material_provisional. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Does: ACCEPTED — Identifies the proposed link as an enrollment-material association. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gives out: ACCEPTED — link_type = enrollment_material_provisional. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Must never: ACCEPTED — Treat this type as a confirmed voice identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: supplies the enrollment link_type. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.11 — Provisional enrollment Person-Box link | The provisional enrollment type. | Keeps the association's purpose explicit. | A typed provisional material link. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-ENROLL.11 — Provisional link and profile coordination | The immutable input bundle, confirmed Ness Person-Box, operation/session references, exact eligible reading set, eligibility decisions and prerequisite/authorization evidence. | Supplies exact type. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7L.11.2 — Enrollment provisional link certainty
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The enrollment link's certainty value, separate from ordinary identity-test outcomes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Takes in: ACCEPTED — The literal enrollment_provisional. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Does: ACCEPTED — Records provisional enrollment provenance without asserting that the captured voice is Ness. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gives out: ACCEPTED — certainty = enrollment_provisional. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Must never: ACCEPTED — Convert the value into completely clear or definite merely because the flow was authorized. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: supplies the provisional certainty value. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.11 — Provisional enrollment Person-Box link | The enrollment_provisional value. | Preserves the provenance-only certainty. | No voice-identity confirmation. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-ENROLL.11 — Provisional link and profile coordination | The immutable input bundle, confirmed Ness Person-Box, operation/session references, exact eligible reading set, eligibility decisions and prerequisite/authorization evidence. | Supplies provisional certainty. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7L.11.3 — Enrollment provisional link proposal ID
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — The stable provisional_link_proposal_id. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — The logical enrollment link proposal identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Keeps the same identity on replay; recovery queries the Person-Box owner using it. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — One identifiable proposal and its owner-returned link outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Create a duplicate link on replay or infer committed truth from an acknowledgment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: supplies idempotent proposal identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.11 — Provisional enrollment Person-Box link | The stable proposal ID. | Uses it for replay and recovery lookup. | Duplicate-free logical link identity. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 2 · ACCEPTED | C-ENROLL.11.1 — Stable link-proposal recovery identity | The operation's exact frozen proposal inputs. | Supplies canonical proposal identity. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 3 · ACCEPTED | C-ENROLL.11 — Provisional link and profile coordination | The immutable input bundle, confirmed Ness Person-Box, operation/session references, exact eligible reading set, eligibility decisions and prerequisite/authorization evidence. | Supplies stable query identity. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7L.11.4 — Enrollment provisional link meaning
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The explicit meaning stated in the provisional link. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Takes in: ACCEPTED — The fact that material was collected through Ness's authorized enrollment flow. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Does: ACCEPTED — States that provenance and explicitly denies that it confirms the captured voice as Ness. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gives out: ACCEPTED — An inspectable provenance statement. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Must never: ACCEPTED — Present enrollment authorization as voice recognition. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: supplies the link's provenance-only meaning. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.11 — Provisional enrollment Person-Box link | The authorized-flow provenance. | Records exactly what the link means. | Enrollment origin kept separate from identity. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-ENROLL.11 — Provisional link and profile coordination | The immutable input bundle, confirmed Ness Person-Box, operation/session references, exact eligible reading set, eligibility decisions and prerequisite/authorization evidence. | Supplies collection provenance. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7L.11.5 — Enrollment provisional link basis
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The authorization basis carried by the provisional link proposal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Takes in: ACCEPTED — Confirmed bai_token_consumed for voice_enrollment_ness; owner-phone trust / bai_initial_setup_finalized; authorization_type = enrollment_declared. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Does: ACCEPTED — References those owner-held authorization facts as the basis for the enrollment association. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gives out: ACCEPTED — A provenance-bearing enrollment authorization basis. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Must never: ACCEPTED — Treat biometric success or declared enrollment attribution as a voice-identity conclusion. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BAI — Biometric Authorization Interface (§25.6): durable consumed-token and initial-setup authorization facts; C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): owner-phone trust facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: supplies the enrollment authorization basis. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.11 — Provisional enrollment Person-Box link | The owner-held authorization references. | Keeps the link's provenance inspectable. | A narrow enrollment basis, no identity grant. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-ENROLL.11 — Provisional link and profile coordination | The immutable input bundle, confirmed Ness Person-Box, operation/session references, exact eligible reading set, eligibility decisions and prerequisite/authorization evidence. | Supplies actual authorization basis. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7L.11.6 — Enrollment proposed input-bundle reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The link's proposed enrollment_profile_input_bundle reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Takes in: ACCEPTED — The exact immutable frozen enrollment input set. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Does: ACCEPTED — References the coordination-only bundle so the link precedes any actual SIA profile. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gives out: ACCEPTED — A pointer to the frozen eligible proposed input bundle. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Must never: ACCEPTED — Reference an already-created SIA profile as the proposal input; treat the bundle as another profile store or identity evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): the immutable coordination-only proposed input bundle. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: supplies the proposed input-bundle reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.11 — Provisional enrollment Person-Box link | The frozen proposed input-bundle reference. | Links the exact material before profile creation. | Preserved input identity. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-ENROLL.10.5 — Immutable enrollment input bundle | Only exact eligible accepted reading references, eligibility-decision references, operation/session references, prerequisite/authorization evidence and the readiness reference. | Takes this place's change: receives the exact immutable bundle reference. | Receives the exact immutable bundle reference. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 3 · ACCEPTED | C-ENROLL.11 — Provisional link and profile coordination | The immutable input bundle, confirmed Ness Person-Box, operation/session references, exact eligible reading set, eligibility decisions and prerequisite/authorization evidence. | Supplies exact frozen input pointer. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7L.11.7 — Enrollment confirmed Ness-box reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The confirmed Ness Person-Box reference in the enrollment proposal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Takes in: ACCEPTED — Ness's existing confirmed Person-Box identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Does: ACCEPTED — Targets that confirmed box while the material association remains provisional. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gives out: ACCEPTED — A confirmed destination identity for the provisional link. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Must never: ACCEPTED — Treat a provisional material link as creating or approving Ness's identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7L.4 — Ness's confirmed Person-Box: Ness's existing confirmed stable identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: supplies the confirmed Ness-box reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.11 — Provisional enrollment Person-Box link | The confirmed Ness identity. | Keeps the target distinct from the provisional material. | A correctly scoped enrollment link. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-ENROLL.11 — Provisional link and profile coordination | The immutable input bundle, confirmed Ness Person-Box, operation/session references, exact eligible reading set, eligibility decisions and prerequisite/authorization evidence. | Supplies confirmed destination. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7L.11.8 — Enrollment link operation reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The enrollment operation reference attached to the link proposal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Takes in: ACCEPTED — The exact enrollment operation identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Does: ACCEPTED — Preserves which operation produced the linked material and proposal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gives out: ACCEPTED — An inspectable operation reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Must never: ACCEPTED — Omit the enrollment operation reference from the proposal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): the enrollment operation reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: supplies operation provenance. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.11 — Provisional enrollment Person-Box link | The enrollment operation identity. | Retains the operation provenance. | A traceable link proposal. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-ENROLL.11 — Provisional link and profile coordination | The immutable input bundle, confirmed Ness Person-Box, operation/session references, exact eligible reading set, eligibility decisions and prerequisite/authorization evidence. | Supplies the parent operation reference, which preserves which operation produced the linked material and proposal. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7L.11.9 — Enrollment link session reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The enrollment session reference attached to the link proposal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Takes in: ACCEPTED — The exact enrollment session identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Does: ACCEPTED — Keeps the collection session identifiable independently of the operation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gives out: ACCEPTED — An inspectable session reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Must never: ACCEPTED — Omit the enrollment session reference from the proposal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): the enrollment session reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: supplies session provenance. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.11 — Provisional enrollment Person-Box link | The enrollment session identity. | Retains the collection-session reference. | Session-specific link provenance. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-ENROLL.11 — Provisional link and profile coordination | The immutable input bundle, confirmed Ness Person-Box, operation/session references, exact eligible reading set, eligibility decisions and prerequisite/authorization evidence. | Keeps the collection session identifiable independently of the operation. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7L.11.10 — Enrollment link eligible-reading references
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The exact eligible reading set referenced by the provisional link. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Takes in: ACCEPTED — The frozen set of eligible accepted enrollment readings. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Does: ACCEPTED — Identifies the material proposed for linking without copying its payload or adding evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gives out: ACCEPTED — Exact reading references for the later owner-controlled handoff. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Must never: ACCEPTED — Substitute a different reading set or treat the reference list as another evidence vote. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): the exact eligible reading-set references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: supplies the linked reading-set identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.11 — Provisional enrollment Person-Box link | The exact eligible readings. | Keeps the material association fixed and inspectable. | No hidden input substitution. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-ENROLL.11 — Provisional link and profile coordination | The immutable input bundle, confirmed Ness Person-Box, operation/session references, exact eligible reading set, eligibility decisions and prerequisite/authorization evidence. | Supplies exact reading set. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7L.11.11 — Enrollment link eligibility-decision references
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The exact eligibility decisions referenced by the provisional link. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Takes in: ACCEPTED — The recorded eligibility decisions for the frozen reading set. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Does: ACCEPTED — Keeps the link traceable to why each referenced segment was eligible. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gives out: ACCEPTED — Inspectable eligibility-decision references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Must never: ACCEPTED — Treat a proposal acknowledgment as proof that eligibility was established. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): the exact eligibility-decision references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: supplies the eligibility-decision provenance. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.11 — Provisional enrollment Person-Box link | The exact eligibility decisions. | Preserves their references with the proposed material. | A reviewable eligibility chain. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-ENROLL.11 — Provisional link and profile coordination | The immutable input bundle, confirmed Ness Person-Box, operation/session references, exact eligible reading set, eligibility decisions and prerequisite/authorization evidence. | Supplies the eligibility decisions, keeping the link traceable to why each referenced segment was eligible. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7L.11.12 — Enrollment link prerequisite-evidence references
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The prerequisite and authorization evidence referenced by the provisional link. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Takes in: ACCEPTED — The owner-held facts establishing the enrollment flow's prerequisites and authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Does: ACCEPTED — Preserves those references with the proposal without becoming their authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gives out: ACCEPTED — An inspectable prerequisite and authorization chain. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Must never: ACCEPTED — Replace owner-held facts with coordinator assertions or turn the chain into voice identity proof. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): prerequisite and authorization references whose underlying truth stays with the respective owners. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: supplies the prerequisite/authorization evidence references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.11 — Provisional enrollment Person-Box link | The prerequisite and authorization chain. | Keeps the proposal's basis inspectable. | No duplicated authority. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-ENROLL.11 — Provisional link and profile coordination | The immutable input bundle, confirmed Ness Person-Box, operation/session references, exact eligible reading set, eligibility decisions and prerequisite/authorization evidence. | Supplies owner evidence. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7L.11.13 — Enrollment committed-link handoff gate
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — The requirement for current Person-Box-owned committed link truth before SIA creates a provisional profile. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — The actual owner-returned link result, linked readings, proposed input bundle and build identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Permits the profile handoff only after a current committed link confirms that the provisional material is linked to Ness's confirmed box. SIA then consumes the readings as one input under its own rules; the enrollment component records profile creation only after SIA commits. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — A permitted SIA handoff or a blocked profile creation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Proceed on a proposal, acknowledgment, stale state or unverifiable link; invert the link-before-profile order; let enrollment decide access. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: ACCEPTED — Refused, pending, stale, contradictory and unverifiable link results each block profile creation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-7L.11.13.1 — Enrollment current committed-link result: current committed truth; C-7L.11.13.2 — Enrollment refused-link result: refused result; C-7L.11.13.3 — Enrollment pending-link result: pending result; C-7L.11.13.4 — Enrollment stale-link result: stale result; C-7L.11.13.5 — Enrollment contradictory-link result: contradictory result; C-7L.11.13.6 — Enrollment unverifiable-link result: unverifiable result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): blocks profile creation until the committed-link prerequisite holds. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.11 — Provisional enrollment Person-Box link | The current actual link result. | Allows handoff only on committed truth. | Profile creation after the link. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-7L.11.13.1 — Enrollment current committed-link result | The current committed-link prerequisite. | Allows only the link-first handoff to SIA. | The eligible result branch. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |
| 3 · ACCEPTED | C-7L.11.13.2 — Enrollment refused-link result | The refusal outcome rule. | Blocks profile creation on refusal. | The refused result branch. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 4 · ACCEPTED | C-7L.11.13.3 — Enrollment pending-link result | The pending outcome rule. | Blocks profile creation on pending state. | The pending result branch. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 5 · ACCEPTED | C-7L.11.13.4 — Enrollment stale-link result | The stale-result rule. | Blocks profile creation on stale state. | The stale result branch. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 6 · ACCEPTED | C-7L.11.13.5 — Enrollment contradictory-link result | The contradictory-result rule. | Blocks profile creation without choosing a convenient result. | The contradictory result branch. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 7 · ACCEPTED | C-7L.11.13.6 — Enrollment unverifiable-link result | The unverifiable-result rule. | Blocks profile creation without current verified commitment. | The unverifiable result branch. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 8 · ACCEPTED | C-ENROLL.11 — Provisional link and profile coordination | The immutable input bundle, confirmed Ness Person-Box, operation/session references, exact eligible reading set, eligibility decisions and prerequisite/authorization evidence. | Gates this place: current committed link required. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |
| 9 · ACCEPTED | C-ENROLL.11.2 — Provisional profile-build identity | The committed link and its exact linked reading set. | Gates this place: current committed linkage before any build. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 10 · ACCEPTED | C-SIA.20 — Provisional enrollment profile handoff | Current §7L-owned committed link truth, the linked eligible accepted reading set, the proposed `enrollment_profile_input_bundle` and the build identity. | Gates this place: current §7L-owned committed link to Ness's confirmed Person-Box is required before profile creation. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |
| 11 · ACCEPTED | C-ENROLL.15.18 — Recovery after link commit before profile creation | The actual committed link and its linked reading set. | Gates this place: current committed truth. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |

SUB-PARTS: C-7L.11.13.1 — Enrollment current committed-link result; C-7L.11.13.2 — Enrollment refused-link result; C-7L.11.13.3 — Enrollment pending-link result; C-7L.11.13.4 — Enrollment stale-link result; C-7L.11.13.5 — Enrollment contradictory-link result; C-7L.11.13.6 — Enrollment unverifiable-link result

### C-7L.11.13.1 — Enrollment current committed-link result
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — Current Person-Box-owned COMMITTED link truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Takes in: ACCEPTED — An actual committed link joining the provisional material to Ness's confirmed Person-Box. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Does: ACCEPTED — Satisfies the link prerequisite for SIA to consume the readings as one input and then create its own provisional profile. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Gives out: ACCEPTED — An eligible handoff, not an access grant. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Must never: ACCEPTED — Treat committed enrollment provenance as confirmed voice identity or automatic recognized_ness access. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.11.13 — Enrollment committed-link handoff gate: supplies current committed link truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.11.13 — Enrollment committed-link handoff gate | The current committed link. | Allows the SIA handoff under SIA's own rules. | Link-first profile creation. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-ENROLL.6.23 — Provisional link committed state | Current Person-Box-owned committed link truth. | Supplies actual owner truth. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7L.11.13.2 — Enrollment refused-link result
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — A refused provisional-link result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Takes in: ACCEPTED — The Person-Box owner's refusal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Does: ACCEPTED — Keeps SIA profile creation blocked. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gives out: ACCEPTED — No profile creation from the refused link. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Must never: ACCEPTED — Proceed on the earlier proposal or acknowledgment after refusal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Refusal blocks the profile handoff. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.11.13 — Enrollment committed-link handoff gate: supplies the refused result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.11.13 — Enrollment committed-link handoff gate | A refused result. | Blocks profile creation. | No unauthorized profile handoff. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7L.11.13.3 — Enrollment pending-link result
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — A pending provisional-link result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Takes in: ACCEPTED — A recorded proposal without current committed link truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Does: ACCEPTED — Keeps SIA profile creation blocked while the link remains pending. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gives out: ACCEPTED — A pending association with no profile handoff. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Must never: ACCEPTED — Treat the proposal's existence or acknowledgment as commitment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Pending link state blocks profile creation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.11.13 — Enrollment committed-link handoff gate: supplies the pending result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.11.13 — Enrollment committed-link handoff gate | A pending result. | Withholds the SIA handoff. | No profile before commitment. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7L.11.13.4 — Enrollment stale-link result
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — A stale provisional-link result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Takes in: ACCEPTED — Link information that does not establish current owner truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Does: ACCEPTED — Blocks SIA profile creation rather than using stale link state. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gives out: ACCEPTED — No profile handoff from stale information. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Must never: ACCEPTED — Use an old affirmative result as current commitment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Stale link state blocks profile creation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.11.13 — Enrollment committed-link handoff gate: supplies the stale result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.11.13 — Enrollment committed-link handoff gate | A stale result. | Requires current committed truth instead. | Blocked stale-state handoff. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7L.11.13.5 — Enrollment contradictory-link result
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — A contradictory provisional-link result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Takes in: ACCEPTED — Conflicting link information. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Does: ACCEPTED — Blocks profile creation without selecting a convenient affirmative result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gives out: ACCEPTED — No SIA handoff from contradictory link truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Must never: ACCEPTED — Resolve the contradiction by assuming commitment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Contradictory results block profile creation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.11.13 — Enrollment committed-link handoff gate: supplies the contradictory result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.11.13 — Enrollment committed-link handoff gate | A contradictory result. | Withholds profile creation. | No guessed commitment. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7L.11.13.6 — Enrollment unverifiable-link result
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — An unverifiable provisional-link result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Takes in: ACCEPTED — A result that cannot establish the required owner-held committed link. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Does: ACCEPTED — Blocks SIA profile creation until current committed truth can be established. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gives out: ACCEPTED — No handoff from unverifiable link state. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Must never: ACCEPTED — Treat lack of verification as successful commitment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Unverifiable results block profile creation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7L.11.13 — Enrollment committed-link handoff gate: supplies the unverifiable result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.11.13 — Enrollment committed-link handoff gate | An unverifiable result. | Withholds the SIA handoff. | No profile based on unverified linkage. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7L.12 — Person-Box generic-connection use boundary
Stamp: ACCEPTED    Source: [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]

ALONE
- What it is: ACCEPTED — The Person-Box consumer boundary for generic accepted connections. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]
- Takes in: ACCEPTED — One provenance-bearing relationship reference after current-use resolution, route-level privacy authorization and separately valid person identity linking. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]
- Does: ACCEPTED — Keeps generic connections separate from identity links, anchors, merge proposals and joins. A direct attachment or transcript relationship may organize material only after its identity link is independently valid. Cross-references distinct records when evidence matters to both systems. Requires resolution of the exact accepted ID/version, later correction/clarification/dispute/supersession events, integrity and owner/authority references, applicable relationship version, proposed current_use_state, separate original certainty, current privacy authorization and influence-removal status. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]
- Gives out: ACCEPTED — An eligible relationship reference under its actual certainty and current-use result; no added identity authority. Under proposed current-use state current, the resolved version may be considered with its basis and source labels. Under proposed current-use state disputed, the dispute accompanies every use and materially affected output states uncertainty. Under proposed current-use state corrected_or_superseded_for_current_use, the earlier record remains history; any replacement requires its own checks. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]
- Must never: ACCEPTED — Let a generic connection prove an endpoint's identity, combine two people's boxes, replace the clear/unclear tests, duplicate identity proposals in the generic waiting area or merge state machines; let a pending generic connection create an identity link, anchor, merge or join; rewrite the other system's history on correction; use a stale accepted version merely because it still exists; widen permissions or bypass influence removal. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]
- Fails closed by: ACCEPTED — An unresolved, contradictory, unavailable or corrupt current-use chain prevents connection use, identity consequences, stronger claims, recommendation/action support and hidden disclosure. Separately influence-removed material is not used. A withheld relationship gives no signal that hidden material exists. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]

TOGETHER
- Fed by: DESIGNED — C-24 — Connection Capability (§24): a relationship reference whose current-use chain and exact eligible version have been resolved, with certainty distinct from decision/current-use status. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14]
- Gated by: ACCEPTED — C-7L.3 — Person-Box proposal and identity events: identity linking and joining must satisfy their own accepted rules. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): route-level internal-use authorization must hold for the handoff itself, including current influence-removal status; C-SACL — Speaker Access-Control Layer (§25.4): visible output remains within the current access boundary after privacy review. [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L — Person-Boxes (§7L) | An eligible generic relationship reference. | Uses it only after separately valid identity linkage. | Organization without identity or permission expansion. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] |
| 2 · DESIGNED | C-24 — Connection Capability (§24) | Person-Box's separate identity-use result. | Keeps the connection and identity histories distinct. | Cross-references without shared state machines. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] |
| 3 · ACCEPTED | C-24.19.8 — Connection I8 Person-Box interface | Currently applicable relationship/version, endpoints, type, certainty, basis, source/evidence, privacy/access and resolved state/chain. | Supplies existing identity rules and ten-rule generic-use boundary, including its own clear/unclear test. | Nothing in this card. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 4 · ACCEPTED | C-24.15 — Connection Person-Box handoff | The currently applicable relationship/version, endpoints, type, certainty, basis, source/evidence, privacy/access and resolved current-use state/chain. | Supplies existing ten-rule generic-connection identity-use boundary. | Nothing in this card. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-7L.13 — Authorized Person-Box query interface
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The Person-Box read interface coordinated by LMAC. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12]
- Takes in: ACCEPTED — A box reference and obtained privacy/authority decisions for the exact requester and purpose; PBR reads for SACL use this path too. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12]
- Does: ACCEPTED — Returns linked objects under their actual certainty after the required decisions; control-path authorization queries carry only the minimum metadata needed to decide, never protected content before authorization. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12]
- Gives out: ACCEPTED — Authorized linked-object or PBR results with their actual uncertainty. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12]
- Must never: ACCEPTED — Bypass identity, access, purpose or logging rules; make a query grant permission to reveal its results. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — Protected content is not released before the authorization result returns. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12]

TOGETHER
- Fed by: DESIGNED — C-LMAC — Live Mechanism Access Coordinator (§26): the exact authorized requester, purpose and box reference. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the obtained privacy decision must permit the actual query; C-7P — Permission & Authority Boundaries (§7P): the obtained authority result must permit routing. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12]
- Changes: DESIGNED — C-LMAC — Live Mechanism Access Coordinator (§26): returns the permitted linked objects and PBR result, not a new identity or truth claim. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L — Person-Boxes (§7L) | An authorized Person-Box read. | Supplies linked objects at their actual certainty. | Purpose-bounded query results. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 2 · DESIGNED | C-LMAC — Live Mechanism Access Coordinator (§26) | The permitted Person-Box result. | Routes it without expanding authorization. | Linked-object or PBR access under owner rules. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 3 · ACCEPTED | C-LMAC.3.4 — Person-Box and PBR query contract | A box reference and the authorized requester/purpose. | Supplies the canonical live Person-Box interface. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |

SUB-PARTS: NONE

### C-7L.14 — Person-Box operation and presentation records
Stamp: ACCEPTED    Source: [V10 §0B] [MAP C-7L] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — The append-only record obligations for Person-Box operations and view presentations. [V10 §0B] [MAP C-7L] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Takes in: ACCEPTED — Each link established with why/who/certainty; each proposed or uncertain-reference anchor; each merge proposal and resolution; join/correction/alias operations; each view presentation with snapshot/version, filters and history switches. [V10 §0B] [MAP C-7L] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Does: ACCEPTED — Leaves exactly one append-only record per real operation; includes the source-grounded basis and search-before-propose occurrence/scope where required. Keeps view presentations attributable to the displayed snapshot/version and active filters/history choice. [V10 §0B] [MAP C-7L] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Gives out: ACCEPTED — Permanent operation and presentation history under privacy and applicable identity authorization. [V10 §0B] [MAP C-7L] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Must never: ACCEPTED — Run a silent internal operation; count a log, repetition or duplicate event as extra identity evidence; let records bypass privacy. [V10 §0B] [MAP C-7L] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7L.3.7 — Person-Box append-only event family: link-family event history; C-7L.5 — Seven-section Person-Box view: the presented view version, filters and chronology choice. [V10 §0B] [MAP C-7L] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): records and their use remain subject to access and authorization; C-SACL — Speaker Access-Control Layer (§25.4): applicable speaker authorization governs exposure. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L — Person-Boxes (§7L) | Per-operation records and view history. | Makes internal identity organization inspectable. | A weightless audit trail. | [MAP C-7L] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19] |

SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece USED BY continuations

These rows add the reciprocal USED BY entries to the named external cards at assembly. They preserve the delivered cards; every row names both ends. The relationship wording is carried from the current TOGETHER field.

| Current card | Field | External card receiving USED BY row | Stamp | Relationship and condition | Source |
|---|---|---|---|---|---|
| C-7L — Person-Boxes (§7L) | Fed by | C-READ — Reading record, validator, writer (§6B) | BUILT | C-READ — Reading record, validator, writer (§6B): immutable readings and their source-root references. | [V10 §6B] [V10 §7L] |
| C-7L — Person-Boxes (§7L) | Fed by | C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B) | DESIGNED | C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B): person-related material gathered during CY-A; C-7B.4 — Person-Box gather: the Person-Box gather; C-7K — Story Layer (§7K): perspective-separated tellings; C-7E — Catalog Front Door + pre-ingest holding (§7E): authorized source references and source-carried attribution. | [MAP C-7B] [MAP CY-A] [MAP C-7L] |
| C-7L — Person-Boxes (§7L) | Fed by | C-7B.4 — Person-Box gather | DESIGNED | C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B): person-related material gathered during CY-A; C-7B.4 — Person-Box gather: the Person-Box gather; C-7K — Story Layer (§7K): perspective-separated tellings; C-7E — Catalog Front Door + pre-ingest holding (§7E): authorized source references and source-carried attribution. | [MAP C-7B] [MAP CY-A] [MAP C-7L] |
| C-7L — Person-Boxes (§7L) | Fed by | C-7K — Story Layer (§7K) | DESIGNED | C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B): person-related material gathered during CY-A; C-7B.4 — Person-Box gather: the Person-Box gather; C-7K — Story Layer (§7K): perspective-separated tellings; C-7E — Catalog Front Door + pre-ingest holding (§7E): authorized source references and source-carried attribution. | [MAP C-7B] [MAP CY-A] [MAP C-7L] |
| C-7L — Person-Boxes (§7L) | Fed by | C-7E — Catalog Front Door + pre-ingest holding (§7E) | DESIGNED | C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B): person-related material gathered during CY-A; C-7B.4 — Person-Box gather: the Person-Box gather; C-7K — Story Layer (§7K): perspective-separated tellings; C-7E — Catalog Front Door + pre-ingest holding (§7E): authorized source references and source-carried attribution. | [MAP C-7B] [MAP CY-A] [MAP C-7L] |
| C-7L — Person-Boxes (§7L) | Fed by | C-READ.10.14 — Telling-reference handoff | ACCEPTED | C-READ.10.14 — Telling-reference handoff: integrity-valid first-class telling references; C-7K.7 — Holding through separate linked objects: Holding through separate linked objects; C-7J.8 — Clash and named-gap presentation: clash presentation with responses kept distinct. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] [V10 §7L] |
| C-7L — Person-Boxes (§7L) | Fed by | C-7K.7 — Holding through separate linked objects | ACCEPTED | C-READ.10.14 — Telling-reference handoff: integrity-valid first-class telling references; C-7K.7 — Holding through separate linked objects: Holding through separate linked objects; C-7J.8 — Clash and named-gap presentation: clash presentation with responses kept distinct. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] [V10 §7L] |
| C-7L — Person-Boxes (§7L) | Fed by | C-7J.8 — Clash and named-gap presentation | ACCEPTED | C-READ.10.14 — Telling-reference handoff: integrity-valid first-class telling references; C-7K.7 — Holding through separate linked objects: Holding through separate linked objects; C-7J.8 — Clash and named-gap presentation: clash presentation with responses kept distinct. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] [V10 §7L] |
| C-7L — Person-Boxes (§7L) | Fed by | C-7E.11 — Held-content access boundary | DESIGNED | C-7E.11 — Held-content access boundary: safe source-carried held metadata, lifecycle state and blockers only. | [V10 §7L] [V10 §7E] |
| C-7L — Person-Boxes (§7L) | Gated by | C-READ.10.10 — Telling-set semantic eligibility | ACCEPTED | C-READ.10.10 — Telling-set semantic eligibility: a complete valid telling set or legitimate zero-telling result is required before telling-specific use; C-7B.9.11 — Forbidden Wonder evidence uses: Wonder possibilities never become observed reality about a person. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1] [04/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md §7] |
| C-7L — Person-Boxes (§7L) | Gated by | C-7B.9.11 — Forbidden Wonder evidence uses | ACCEPTED | C-READ.10.10 — Telling-set semantic eligibility: a complete valid telling set or legitimate zero-telling result is required before telling-specific use; C-7B.9.11 — Forbidden Wonder evidence uses: Wonder possibilities never become observed reality about a person. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1] [04/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md §7] |
| C-7L — Person-Boxes (§7L) | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): actual internal use and visible output require their own privacy authorization; C-7P — Permission & Authority Boundaries (§7P): link and query actions stay within their authority; C-SACL — Speaker Access-Control Layer (§25.4): applicable speaker access gates disclosure. | [V10 §7Q] [V10 §7P] [V10 §25.2] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §20] |
| C-7L — Person-Boxes (§7L) | Gated by | C-7P — Permission & Authority Boundaries (§7P) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): actual internal use and visible output require their own privacy authorization; C-7P — Permission & Authority Boundaries (§7P): link and query actions stay within their authority; C-SACL — Speaker Access-Control Layer (§25.4): applicable speaker access gates disclosure. | [V10 §7Q] [V10 §7P] [V10 §25.2] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §20] |
| C-7L — Person-Boxes (§7L) | Gated by | C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): actual internal use and visible output require their own privacy authorization; C-7P — Permission & Authority Boundaries (§7P): link and query actions stay within their authority; C-SACL — Speaker Access-Control Layer (§25.4): applicable speaker access gates disclosure. | [V10 §7Q] [V10 §7P] [V10 §25.2] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §20] |
| C-7L — Person-Boxes (§7L) | Changes | C-7M — Computed View (§7M) | DESIGNED | C-7M — Computed View (§7M): supplies identity-linked source objects for the current picture; C-7D — Living State Web (§7D): supplies stable person identity anchors without adding evidence; C-SIA — Speaker Identity Assessment (§25.3): supplies permitted profile-reading links; C-SACL — Speaker Access-Control Layer (§25.4): supplies PBR references through the authorized query route. | [V10 §7L] [MAP C-7L] |
| C-7L — Person-Boxes (§7L) | Changes | C-7D — Living State Web (§7D) | DESIGNED | C-7M — Computed View (§7M): supplies identity-linked source objects for the current picture; C-7D — Living State Web (§7D): supplies stable person identity anchors without adding evidence; C-SIA — Speaker Identity Assessment (§25.3): supplies permitted profile-reading links; C-SACL — Speaker Access-Control Layer (§25.4): supplies PBR references through the authorized query route. | [V10 §7L] [MAP C-7L] |
| C-7L — Person-Boxes (§7L) | Changes | C-SIA — Speaker Identity Assessment (§25.3) | DESIGNED | C-7M — Computed View (§7M): supplies identity-linked source objects for the current picture; C-7D — Living State Web (§7D): supplies stable person identity anchors without adding evidence; C-SIA — Speaker Identity Assessment (§25.3): supplies permitted profile-reading links; C-SACL — Speaker Access-Control Layer (§25.4): supplies PBR references through the authorized query route. | [V10 §7L] [MAP C-7L] |
| C-7L — Person-Boxes (§7L) | Changes | C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED | C-7M — Computed View (§7M): supplies identity-linked source objects for the current picture; C-7D — Living State Web (§7D): supplies stable person identity anchors without adding evidence; C-SIA — Speaker Identity Assessment (§25.3): supplies permitted profile-reading links; C-SACL — Speaker Access-Control Layer (§25.4): supplies PBR references through the authorized query route. | [V10 §7L] [MAP C-7L] |
| C-7L.1.1 — Person-Box link what it connects | Fed by | C-READ.10.14.2 — Person-Box references | ACCEPTED | C-READ.10.14.2 — Person-Box references: stable telling_id references and preserved five-field link provenance. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] |
| C-7L.4 — Ness's confirmed Person-Box | Fed by | C-7E — Catalog Front Door + pre-ingest holding (§7E) | DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E): source and speaker/thread resolution for material attributed to Ness. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [V10 §7E] |
| C-7L.4 — Ness's confirmed Person-Box | Changes | C-7D — Living State Web (§7D) | DESIGNED | C-7D — Living State Web (§7D): supplies Ness's stable identity anchor under state rules; C-7M — Computed View (§7M): supplies permitted person-focused source links under its own derivation rules. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [MAP C-7L] |
| C-7L.4 — Ness's confirmed Person-Box | Changes | C-7M — Computed View (§7M) | DESIGNED | C-7D — Living State Web (§7D): supplies Ness's stable identity anchor under state rules; C-7M — Computed View (§7M): supplies permitted person-focused source links under its own derivation rules. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [MAP C-7L] |
| C-7L.5 — Seven-section Person-Box view | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): visible use must be authorized before surfacing; C-SACL — Speaker Access-Control Layer (§25.4): applicable speaker restrictions remain in force. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §20] [V10 §25.2] |
| C-7L.5 — Seven-section Person-Box view | Gated by | C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): visible use must be authorized before surfacing; C-SACL — Speaker Access-Control Layer (§25.4): applicable speaker restrictions remain in force. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §20] [V10 §25.2] |
| C-7L.5 — Seven-section Person-Box view | Changes | C-7I — View Layer (§7I) | DESIGNED | C-7I — View Layer (§7I): follows its Current/History discipline; C-7M — Computed View (§7M): delegates any best-supported ordering to its seven factors, with recency only a limited tie-breaker. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [MAP C-7I] [V10 §7M] |
| C-7L.5 — Seven-section Person-Box view | Changes | C-7M — Computed View (§7M) | DESIGNED | C-7I — View Layer (§7I): follows its Current/History discipline; C-7M — Computed View (§7M): delegates any best-supported ordering to its seven factors, with recency only a limited tie-breaker. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] [MAP C-7I] [V10 §7M] |
| C-7L.5.3 — Person-Box story-tellings section | Fed by | C-READ.10.14.2 — Person-Box references | ACCEPTED | C-READ.10.14.2 — Person-Box references: stable telling references with preserved link provenance. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] |
| C-7L.5.3 — Person-Box story-tellings section | Gated by | C-READ.10.10.8 — Person-Box semantic links eligibility | ACCEPTED | C-READ.10.10.8 — Person-Box semantic links eligibility: complete valid telling-set eligibility before Person-Box semantic linking. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] |
| C-7L.5.4 — Person-Box clashes section | Fed by | C-7J.8 — Clash and named-gap presentation | ACCEPTED | C-7J.8 — Clash and named-gap presentation: compact clash markers and full detail/response presentation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |
| C-7L.5.6 — Person-Box themes section | Fed by | C-7K.6.1 — Theme record | ACCEPTED | C-7K.6.1 — Theme record: stable theme records and their status/version history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |
| C-7L.5.7 — Person-Box unresolved-identity section | Fed by | C-7J.8.3 — Recorded named absence | ACCEPTED | C-7L.2 — Uncertain identity anchor: unresolved anchors; C-7L.3.7.4 — Person-Box merge-proposal record: merge proposals with named unmet-definite gaps. C-7J.8.3 — Recorded named absence: recorded named absences shown as labeled empty slots without evidence weight. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |
| C-7L.7 — Person-Box Holding through linked objects | Fed by | C-7K.7 — Holding through separate linked objects | ACCEPTED | C-7K.7 — Holding through separate linked objects: the accepted shared Holding boundary and separate-object structure. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] |
| C-7L.8 — Person-Box held-material metadata boundary | Fed by | C-7E.11 — Held-content access boundary | DESIGNED | C-7E.11 — Held-content access boundary: safe source-carried held metadata, lifecycle state and blockers, with raw content unavailable to this semantic consumer. | [V10 §7L] [V10 §7E] |
| C-7L.8 — Person-Box held-material metadata boundary | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): metadata linking still requires the actual purpose's privacy authorization; C-TSC — Temporary Session Cache (§7E-TSC): sealed TSC content has no inspection path and remains inaccessible to Person-Boxes. | [V10 §7Q] [04/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md §11] |
| C-7L.8 — Person-Box held-material metadata boundary | Gated by | C-TSC — Temporary Session Cache (§7E-TSC) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): metadata linking still requires the actual purpose's privacy authorization; C-TSC — Temporary Session Cache (§7E-TSC): sealed TSC content has no inspection path and remains inaccessible to Person-Boxes. | [V10 §7Q] [04/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md §11] |
| C-7L.9 — Person-Box permission-boundary read interface | Gated by | C-7P — Permission & Authority Boundaries (§7P) | DESIGNED | C-7P — Permission & Authority Boundaries (§7P): protected authority governs PBR maintenance; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the actual query and use require privacy authorization. | [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement] |
| C-7L.9 — Person-Box permission-boundary read interface | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7P — Permission & Authority Boundaries (§7P): protected authority governs PBR maintenance; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the actual query and use require privacy authorization. | [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement] |
| C-7L.9 — Person-Box permission-boundary read interface | Changes | C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4): supplies the active PBR via the LMAC route for final category enforcement. | [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement] |
| C-7L.9.3 — Person-Box visibility restriction | Gated by | C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4): current speaker access bounds the answer; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): disclosure requires privacy authorization. | [V10 §25.2 / Person-Box Visibility] |
| C-7L.9.3 — Person-Box visibility restriction | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4): current speaker access bounds the answer; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): disclosure requires privacy authorization. | [V10 §25.2 / Person-Box Visibility] |
| C-7L.10 — Voice-profile Person-Box linking boundary | Fed by | C-SIA — Speaker Identity Assessment (§25.3) | DESIGNED | C-SIA — Speaker Identity Assessment (§25.3): profile readings and the identity-assessment facts it owns. | [V10 §25.3 / Voice Profile Architecture] [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| C-7L.10 — Voice-profile Person-Box linking boundary | Changes | C-SIA — Speaker Identity Assessment (§25.3) | DESIGNED | C-SIA — Speaker Identity Assessment (§25.3): supplies permitted links to separate person identities. | [V10 §25.3 / Voice Profile Architecture] [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| C-7L.10.2 — Unknown-speaker capture-time certainty minimum | Fed by | C-SIA — Speaker Identity Assessment (§25.3) | DESIGNED | C-SIA — Speaker Identity Assessment (§25.3): the capture-time attribution assessment. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| C-7L.10.3 — Unknown-speaker no-spoofing condition | Fed by | C-SIA — Speaker Identity Assessment (§25.3) | DESIGNED | C-SIA — Speaker Identity Assessment (§25.3): the spoofing assessment for the attributed material. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| C-7L.10.4 — Unknown-speaker authorized-promotion condition | Fed by | C-TSC — Temporary Session Cache (§7E-TSC) | DESIGNED | C-TSC — Temporary Session Cache (§7E-TSC): fingerprint-authorized promotion evidence; C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): completed processing and reading evidence. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| C-7L.10.4 — Unknown-speaker authorized-promotion condition | Fed by | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | DESIGNED | C-TSC — Temporary Session Cache (§7E-TSC): fingerprint-authorized promotion evidence; C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): completed processing and reading evidence. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| C-7L.10.5 — Unknown-speaker reading-confidence minimum | Fed by | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | DESIGNED | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): the reading and its confidence/support evidence. | [V10 §25.3 / Minimum Evidence for Person-Box Linking] |
| C-7L.11 — Provisional enrollment Person-Box link | Fed by | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | DESIGNED | C-ENROLL — Initial Ness voice-profile enrollment (§25.11): the provisional-link proposal and exact frozen input references; the coordinator only proposes. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| C-7L.11 — Provisional enrollment Person-Box link | Changes | C-SIA — Speaker Identity Assessment (§25.3) | DESIGNED | C-SIA — Speaker Identity Assessment (§25.3): releases the linked reading set for its own profile rules only after current committed link truth; C-ENROLL — Initial Ness voice-profile enrollment (§25.11): supplies the actual proposal outcome and link state for recovery. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| C-7L.11 — Provisional enrollment Person-Box link | Changes | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | DESIGNED | C-SIA — Speaker Identity Assessment (§25.3): releases the linked reading set for its own profile rules only after current committed link truth; C-ENROLL — Initial Ness voice-profile enrollment (§25.11): supplies the actual proposal outcome and link state for recovery. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| C-7L.11.5 — Enrollment provisional link basis | Fed by | C-BAI — Biometric Authorization Interface (§25.6) | DESIGNED | C-BAI — Biometric Authorization Interface (§25.6): durable consumed-token and initial-setup authorization facts; C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): owner-phone trust facts. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| C-7L.11.5 — Enrollment provisional link basis | Fed by | C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10) | DESIGNED | C-BAI — Biometric Authorization Interface (§25.6): durable consumed-token and initial-setup authorization facts; C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): owner-phone trust facts. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| C-7L.11.6 — Enrollment proposed input-bundle reference | Fed by | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | DESIGNED | C-ENROLL — Initial Ness voice-profile enrollment (§25.11): the immutable coordination-only proposed input bundle. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] |
| C-7L.11.8 — Enrollment link operation reference | Fed by | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | DESIGNED | C-ENROLL — Initial Ness voice-profile enrollment (§25.11): the enrollment operation reference. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| C-7L.11.9 — Enrollment link session reference | Fed by | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | DESIGNED | C-ENROLL — Initial Ness voice-profile enrollment (§25.11): the enrollment session reference. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| C-7L.11.10 — Enrollment link eligible-reading references | Fed by | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | DESIGNED | C-ENROLL — Initial Ness voice-profile enrollment (§25.11): the exact eligible reading-set references. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| C-7L.11.11 — Enrollment link eligibility-decision references | Fed by | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | DESIGNED | C-ENROLL — Initial Ness voice-profile enrollment (§25.11): the exact eligibility-decision references. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| C-7L.11.12 — Enrollment link prerequisite-evidence references | Fed by | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | DESIGNED | C-ENROLL — Initial Ness voice-profile enrollment (§25.11): prerequisite and authorization references whose underlying truth stays with the respective owners. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| C-7L.11.13 — Enrollment committed-link handoff gate | Changes | C-SIA — Speaker Identity Assessment (§25.3) | DESIGNED | C-SIA — Speaker Identity Assessment (§25.3): blocks profile creation until the committed-link prerequisite holds. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| C-7L.12 — Person-Box generic-connection use boundary | Fed by | C-24 — Connection Capability (§24) | DESIGNED | C-24 — Connection Capability (§24): a relationship reference whose current-use chain and exact eligible version have been resolved, with certainty distinct from decision/current-use status. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §12C] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] |
| C-7L.12 — Person-Box generic-connection use boundary | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): route-level internal-use authorization must hold for the handoff itself, including current influence-removal status; C-SACL — Speaker Access-Control Layer (§25.4): visible output remains within the current access boundary after privacy review. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15] |
| C-7L.12 — Person-Box generic-connection use boundary | Gated by | C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): route-level internal-use authorization must hold for the handoff itself, including current influence-removal status; C-SACL — Speaker Access-Control Layer (§25.4): visible output remains within the current access boundary after privacy review. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §15] |
| C-7L.13 — Authorized Person-Box query interface | Fed by | C-LMAC — Live Mechanism Access Coordinator (§26) | DESIGNED | C-LMAC — Live Mechanism Access Coordinator (§26): the exact authorized requester, purpose and box reference. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| C-7L.13 — Authorized Person-Box query interface | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the obtained privacy decision must permit the actual query; C-7P — Permission & Authority Boundaries (§7P): the obtained authority result must permit routing. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| C-7L.13 — Authorized Person-Box query interface | Gated by | C-7P — Permission & Authority Boundaries (§7P) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the obtained privacy decision must permit the actual query; C-7P — Permission & Authority Boundaries (§7P): the obtained authority result must permit routing. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| C-7L.13 — Authorized Person-Box query interface | Changes | C-LMAC — Live Mechanism Access Coordinator (§26) | DESIGNED | C-LMAC — Live Mechanism Access Coordinator (§26): returns the permitted linked objects and PBR result, not a new identity or truth claim. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| C-7L.14 — Person-Box operation and presentation records | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): records and their use remain subject to access and authorization; C-SACL — Speaker Access-Control Layer (§25.4): applicable speaker authorization governs exposure. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19] |
| C-7L.14 — Person-Box operation and presentation records | Gated by | C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): records and their use remain subject to access and authorization; C-SACL — Speaker Access-Control Layer (§25.4): applicable speaker authorization governs exposure. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19] |

## Cross-piece TOGETHER continuations for incoming uses

These are the reciprocal uses represented in the current USED BY tables. Their external owners retain their full mechanisms in their assigned pieces.

| Current card supplying use | External using card | Takes in there | Does there | Changes there | Stamp | Source |
|---|---|---|---|---|---|---|
| C-7L — Person-Boxes (§7L) | C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B) | A person reference and preserved source objects. | Gathers linked person material without interpreting a personality. | Person-related navigation and reference context. | DESIGNED | [MAP C-7B] [MAP CY-A] |
| C-7L — Person-Boxes (§7L) | C-7K — Story Layer (§7K) | Person identity references for tellings. | Keeps perspective roles linked to their identity anchors. | Identity navigation without narrative synthesis. | DESIGNED | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [V10 §7L] |
| C-7L — Person-Boxes (§7L) | C-7K.7 — Holding through separate linked objects | Separate person-related objects and links. | Holds each perspective and Ness's understanding distinctly. | Linked Holding without a second memory store. | ACCEPTED | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] |
| C-7L — Person-Boxes (§7L) | C-7M — Computed View (§7M) | Person-linked sources. | Assembles under its own derivation and privacy rules. | Current presentation, never the original records. | DESIGNED | [MAP C-7L] |
| C-7L — Person-Boxes (§7L) | C-7D — Living State Web (§7D) | Stable person identity anchors. | Grounds person-related state under its own rules. | State identity references, not added support. | DESIGNED | [MAP C-7L] |
| C-7L — Person-Boxes (§7L) | C-SIA — Speaker Identity Assessment (§25.3) | Permitted profile-reading links. | Consumes them under identity and training rules. | Independent identity assessment inputs. | DESIGNED | [V10 §25.3 / Voice Profile Architecture] |
| C-7L — Person-Boxes (§7L) | C-SACL — Speaker Access-Control Layer (§25.4) | Active PBR reference obtained through LMAC. | Checks permission categories at output time. | Speaker-bounded disclosure. | DESIGNED | [V10 §25.4 / Permission Boundary Enforcement] |
| C-7L.9 — Person-Box permission-boundary read interface | C-LMAC — Live Mechanism Access Coordinator (§26) | A PBR read for the requested person. | Routes it under privacy and authority results. | An authorized SACL input. | DESIGNED | [V10 §25.4 / Permission Boundary Enforcement] |
| C-7L.9 — Person-Box permission-boundary read interface | C-SACL — Speaker Access-Control Layer (§25.4) | The active PBR and current version. | Checks output categories and refreshes its cache on a version change. | Speaker-bounded disclosure. | DESIGNED | [V10 §25.4 / Permission Boundary Enforcement] |
| C-7L.10 — Voice-profile Person-Box linking boundary | C-SIA — Speaker Identity Assessment (§25.3) | Separate Person-Box links. | Uses the source readings under its own profile rules. | Independent identity assessments. | DESIGNED | [V10 §25.3 / Voice Profile Architecture] |
| C-7L.11 — Provisional enrollment Person-Box link | C-SIA — Speaker Identity Assessment (§25.3) | Current committed link truth and linked reading references. | Consumes readings as one input, then may commit the actual provisional profile under its own rules. | No profile before the link. | DESIGNED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |
| C-7L.11 — Provisional enrollment Person-Box link | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | The actual owner-returned link result. | Queries by proposal ID after uncertainty and waits for committed truth. | Coordination state without identity authority. | DESIGNED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| C-7L.12 — Person-Box generic-connection use boundary | C-24 — Connection Capability (§24) | Person-Box's separate identity-use result. | Keeps the connection and identity histories distinct. | Cross-references without shared state machines. | DESIGNED | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §14] |
| C-7L.13 — Authorized Person-Box query interface | C-LMAC — Live Mechanism Access Coordinator (§26) | The permitted Person-Box result. | Routes it without expanding authorization. | Linked-object or PBR access under owner rules. | DESIGNED | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |

## Scope, paths and source dispositions

C-7L participates in CY-A through C-7B's person gather. The current root reciprocates the earlier gather, Story Layer, complete-telling eligibility, Wonder and metadata-only held-content uses. The C-7E.11 consumer boundary is explicitly present here, with that card's DESIGNED status. Existing C-READ.10.14.2 and C-READ.10.10.8 retain telling-reference and semantic-eligibility ownership. Existing C-7K.7 retains shared Holding ownership. C-7J.8 and C-7J.8.3 retain clash/named-gap presentation atoms. No existing card is redefined.

Direct Person-Box scope is V10 §7L, MAP C-7L, Bundle 3 §§7/9/12–16/18–20, A2's complete-set and reference contracts, Bundle 6 A3.5 and its query boundary, the applicable V10 §§25.2–25.4 person/PBR/profile-link interfaces, and B-INT-7 §13 with its §12A/14/19 interfaces and B-INT-8 §14 with its §12C/15 preconditions. The four ordinary certainty outcomes and enrollment_provisional have different meanings and are explicitly scoped; no numerical identity score or new approval rule is chosen. The accepted receipts establish the package identities, while their own receipt-audit conditions are not represented as observed PASS.

Source discovery searched pinned permitted 04/05 files by C-7L, Person-Box, person_box, identity links, Holding and PBR. Bundle 4's time-bounded state identity and source-link snapshots remain CH06-f/d. Bundle 2's same-person retrieval dimension remains C-7F.6.6.4.1 and CH08-b, and its Computed View declaration remains CH06-d. A4 cannot merge identities. The inherited B26 source-scope gap remains open. B11's store/batch mechanics retain C-STORE; only Bundle 3's beside-the-batches identity linking is written here. B15/A16 archive isolation retains C-TSC; the consumer no-inspection boundary is carried here. A7/B7 protection mechanisms remain CH08-a; current Person-Box gates do not recreate privacy records or their lifecycle.

A26 and B-INT-5 own authenticated Personal Mode, PBR-version/stream fences and access truth outside this piece; the source's pbr_version and ness_presence_satisfied in those records remain CH09 ownership. B-INT-7's enrollment coordinator, input-bundle internals, session/capture/eligibility state machines and SIA profile commit remain CH09-h/c. The current piece writes the complete §7L-owned link proposal fields, idempotency, actual owner outcome and link-before-profile gate. It does not copy coordinator records marked proposed or claim their authority. B-INT-8's full connection recordkeeper, proposed current-use state atoms, correction-chain records, CRK and authority events remain CH06-g; the complete consumer checks and no-identity-consequence boundary are explicit here. Bundle 5 closeout confirms those divisions. The operation kernel's identity registry adds no Person-Box link authority.

A19 room/card/UE5 presentation stays CH10-e; its visual handles cannot rewrite Person-Boxes or create a second store. The Five Framework package's entity/Person-Box reference index remains a derived index direction under C-INDEX, not a new Person-Box identity mechanism. Thought-branch and other future-feature material remains intent/dependency scope, not a source for a new identity fact. Active indices and A2/A3 working status notes serve discovery only; stale open-slot wording does not override accepted Bundle 3. The September 25 restored thin-evidence memory-health query retains C-READ.8.6; no historical text is newly opened and no ledger text supplies behavior. No new conflict resolution, runtime authorization, implementation name or empirical value is introduced.

## Source-to-card coverage added by CH06-c

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

## Additional undecided implementation slots

| Owner | Slot | State |
|---|---|---|
| C-7L.1 — Person-Box link record | Concrete serialization, field types and storage-failure protocol for the link/event family beyond the accepted fields and non-destructive rules | NOT DECIDED |
| C-7L.3.1 — Person-Box stable system ID | Stable system-ID generation implementation and concrete wire form | NOT DECIDED |
| C-7L.3.3 — Person-Box search before propose | Search implementation and search-failure result beyond the mandatory occurrence/scope requirement | NOT DECIDED |
| C-7L.3.6 — Ness Person-Box responses | Exact response-event schema and wire representation for every identity action | NOT DECIDED |
| C-7L.5 — Seven-section Person-Box view | Concrete visual implementation beyond the accepted seven-section, filter, label and expansion mechanics | NOT DECIDED |
| C-7L.6 — Person-Box cross-batch identity links | Wire representation of per-element batch identity and cross-batch identity tags | NOT DECIDED |
| C-7L.7 — Person-Box Holding through linked objects | Exact Holding record/link layout beyond separate existing objects | NOT DECIDED |
| C-7L.9 — Person-Box permission-boundary read interface | Full PBR schema and maintenance implementation beyond the explicitly written read interface; complete authority/access owners remain later pieces | NOT DECIDED |
| C-7L.10.1 — Unknown-speaker attributed-material minimum | Empirical minimum quantity of attributed voice material | NOT DECIDED |
| C-7L.10.2 — Unknown-speaker capture-time certainty minimum | Empirical minimum attribution certainty at capture | NOT DECIDED |
| C-7L.10.5 — Unknown-speaker reading-confidence minimum | Empirical minimum reading confidence for ordinary unknown-speaker linking | NOT DECIDED |
| C-7L.11 — Provisional enrollment Person-Box link | Concrete serialization and implementation of owner-held provisional-link truth beyond stable proposal identity, required references and blocking outcomes | NOT DECIDED |
| C-7L.14 — Person-Box operation and presentation records | Exact operation/presentation log wire schemas and storage-failure protocol beyond one-record, authorization and preservation requirements | NOT DECIDED |

## Appendix A carry-forward — this piece

| Card | Empty field | Occurrence within field | State |
|---|---|---|---|
| C-7L — Person-Boxes (§7L) | USED BY row 8 / Takes in there | 1 | NOT DECIDED |
| C-7L — Person-Boxes (§7L) | USED BY row 9 / Takes in there | 1 | NOT DECIDED |
| C-7L.1 — Person-Box link record | Fails closed by | 1 | NOT DECIDED |
| C-7L.1.1 — Person-Box link what it connects | Fails closed by | 1 | NOT DECIDED |
| C-7L.1.1 — Person-Box link what it connects | Gated by | 1 | NOT DECIDED |
| C-7L.1.1 — Person-Box link what it connects | Changes | 1 | NOT DECIDED |
| C-7L.1.2 — Person-Box link why | Fails closed by | 1 | NOT DECIDED |
| C-7L.1.2 — Person-Box link why | Fed by | 1 | NOT DECIDED |
| C-7L.1.2 — Person-Box link why | Changes | 1 | NOT DECIDED |
| C-7L.1.3 — Person-Box link who established | Fails closed by | 1 | NOT DECIDED |
| C-7L.1.3 — Person-Box link who established | Fed by | 1 | NOT DECIDED |
| C-7L.1.3 — Person-Box link who established | Gated by | 1 | NOT DECIDED |
| C-7L.1.4 — Person-Box identity-test certainty | Gated by | 1 | NOT DECIDED |
| C-7L.1.4 — Person-Box identity-test certainty | Changes | 1 | NOT DECIDED |
| C-7L.1.4.1 — Person-Box completely clear outcome | Fails closed by | 1 | NOT DECIDED |
| C-7L.1.4.1 — Person-Box completely clear outcome | Fed by | 1 | NOT DECIDED |
| C-7L.1.4.1 — Person-Box completely clear outcome | Changes | 1 | NOT DECIDED |
| C-7L.1.4.2 — Person-Box pending-unclear outcome | Fed by | 1 | NOT DECIDED |
| C-7L.1.4.2 — Person-Box pending-unclear outcome | Changes | 1 | NOT DECIDED |
| C-7L.1.4.3 — Person-Box definite outcome | Fails closed by | 1 | NOT DECIDED |
| C-7L.1.4.3 — Person-Box definite outcome | Fed by | 1 | NOT DECIDED |
| C-7L.1.4.3 — Person-Box definite outcome | Changes | 1 | NOT DECIDED |
| C-7L.1.4.4 — Person-Box pending-not-definite outcome | Fed by | 1 | NOT DECIDED |
| C-7L.1.4.4 — Person-Box pending-not-definite outcome | Changes | 1 | NOT DECIDED |
| C-7L.1.5 — Person-Box link timestamp | Fails closed by | 1 | NOT DECIDED |
| C-7L.1.5 — Person-Box link timestamp | Fed by | 1 | NOT DECIDED |
| C-7L.1.5 — Person-Box link timestamp | Gated by | 1 | NOT DECIDED |
| C-7L.2.1 — Uncertain anchor label or name | Fails closed by | 1 | NOT DECIDED |
| C-7L.2.1 — Uncertain anchor label or name | Fed by | 1 | NOT DECIDED |
| C-7L.2.1 — Uncertain anchor label or name | Gated by | 1 | NOT DECIDED |
| C-7L.2.2 — Uncertain anchor appearance location | Fails closed by | 1 | NOT DECIDED |
| C-7L.2.2 — Uncertain anchor appearance location | Fed by | 1 | NOT DECIDED |
| C-7L.2.2 — Uncertain anchor appearance location | Gated by | 1 | NOT DECIDED |
| C-7L.2.3 — Uncertain anchor appearance time | Fails closed by | 1 | NOT DECIDED |
| C-7L.2.3 — Uncertain anchor appearance time | Fed by | 1 | NOT DECIDED |
| C-7L.2.3 — Uncertain anchor appearance time | Gated by | 1 | NOT DECIDED |
| C-7L.2.4 — Uncertain anchor connecting evidence | Fails closed by | 1 | NOT DECIDED |
| C-7L.2.4 — Uncertain anchor connecting evidence | Fed by | 1 | NOT DECIDED |
| C-7L.2.4 — Uncertain anchor connecting evidence | Gated by | 1 | NOT DECIDED |
| C-7L.2.5 — Uncertain anchor current test outcome | Gated by | 1 | NOT DECIDED |
| C-7L.2.5 — Uncertain anchor current test outcome | Changes | 1 | NOT DECIDED |
| C-7L.3 — Person-Box proposal and identity events | Changes | 1 | NOT DECIDED |
| C-7L.3.1 — Person-Box stable system ID | Fails closed by | 1 | NOT DECIDED |
| C-7L.3.1 — Person-Box stable system ID | Fed by | 1 | NOT DECIDED |
| C-7L.3.1 — Person-Box stable system ID | Gated by | 1 | NOT DECIDED |
| C-7L.3.2 — Person-Box names labels and roles | Fails closed by | 1 | NOT DECIDED |
| C-7L.3.2 — Person-Box names labels and roles | Gated by | 1 | NOT DECIDED |
| C-7L.3.2 — Person-Box names labels and roles | Changes | 1 | NOT DECIDED |
| C-7L.3.3 — Person-Box search before propose | Fails closed by | 1 | NOT DECIDED |
| C-7L.3.3 — Person-Box search before propose | Gated by | 1 | NOT DECIDED |
| C-7L.3.3 — Person-Box search before propose | Changes | 1 | NOT DECIDED |
| C-7L.3.3.1 — Confirmed Person-Box search scope | Fails closed by | 1 | NOT DECIDED |
| C-7L.3.3.1 — Confirmed Person-Box search scope | Fed by | 1 | NOT DECIDED |
| C-7L.3.3.1 — Confirmed Person-Box search scope | Gated by | 1 | NOT DECIDED |
| C-7L.3.3.2 — Unresolved identity-anchor search scope | Fails closed by | 1 | NOT DECIDED |
| C-7L.3.3.2 — Unresolved identity-anchor search scope | Fed by | 1 | NOT DECIDED |
| C-7L.3.3.2 — Unresolved identity-anchor search scope | Gated by | 1 | NOT DECIDED |
| C-7L.3.3.3 — Person-Box alias search scope | Fails closed by | 1 | NOT DECIDED |
| C-7L.3.3.3 — Person-Box alias search scope | Fed by | 1 | NOT DECIDED |
| C-7L.3.3.3 — Person-Box alias search scope | Gated by | 1 | NOT DECIDED |
| C-7L.3.3.4 — Prior Person-Box merge-proposal search scope | Fails closed by | 1 | NOT DECIDED |
| C-7L.3.3.4 — Prior Person-Box merge-proposal search scope | Fed by | 1 | NOT DECIDED |
| C-7L.3.3.4 — Prior Person-Box merge-proposal search scope | Gated by | 1 | NOT DECIDED |
| C-7L.3.4 — Completely-clear mention test | Fed by | 1 | NOT DECIDED |
| C-7L.3.4 — Completely-clear mention test | Gated by | 1 | NOT DECIDED |
| C-7L.3.5 — Definite same-person test | Fed by | 1 | NOT DECIDED |
| C-7L.3.5 — Definite same-person test | Gated by | 1 | NOT DECIDED |
| C-7L.3.6 — Ness Person-Box responses | Fails closed by | 1 | NOT DECIDED |
| C-7L.3.6 — Ness Person-Box responses | Changes | 1 | NOT DECIDED |
| C-7L.3.6.1 — Ness Person-Box confirmation | Fails closed by | 1 | NOT DECIDED |
| C-7L.3.6.1 — Ness Person-Box confirmation | Fed by | 1 | NOT DECIDED |
| C-7L.3.6.1 — Ness Person-Box confirmation | Changes | 1 | NOT DECIDED |
| C-7L.3.6.2 — Ness Person-Box rejection | Fails closed by | 1 | NOT DECIDED |
| C-7L.3.6.2 — Ness Person-Box rejection | Fed by | 1 | NOT DECIDED |
| C-7L.3.6.2 — Ness Person-Box rejection | Changes | 1 | NOT DECIDED |
| C-7L.3.6.3 — Ness Person-Box rename | Fails closed by | 1 | NOT DECIDED |
| C-7L.3.6.3 — Ness Person-Box rename | Fed by | 1 | NOT DECIDED |
| C-7L.3.6.3 — Ness Person-Box rename | Changes | 1 | NOT DECIDED |
| C-7L.3.6.4 — Ness Person-Box keep unresolved | Fed by | 1 | NOT DECIDED |
| C-7L.3.6.4 — Ness Person-Box keep unresolved | Changes | 1 | NOT DECIDED |
| C-7L.3.6.5 — Ness link to existing Person-Box | Fails closed by | 1 | NOT DECIDED |
| C-7L.3.6.5 — Ness link to existing Person-Box | Fed by | 1 | NOT DECIDED |
| C-7L.3.6.5 — Ness link to existing Person-Box | Changes | 1 | NOT DECIDED |
| C-7L.3.6.6 — Ness Person-Box merge proposal | Fed by | 1 | NOT DECIDED |
| C-7L.3.6.6 — Ness Person-Box merge proposal | Changes | 1 | NOT DECIDED |
| C-7L.3.7 — Person-Box append-only event family | Fails closed by | 1 | NOT DECIDED |
| C-7L.3.7 — Person-Box append-only event family | Changes | 1 | NOT DECIDED |
| C-7L.3.7.1 — Person-Box mention-link event | Fed by | 1 | NOT DECIDED |
| C-7L.3.7.1 — Person-Box mention-link event | Changes | 1 | NOT DECIDED |
| C-7L.3.7.2 — Person-Box pending-anchor creation event | Changes | 1 | NOT DECIDED |
| C-7L.3.7.3 — Person-Box anchor-confirmation event | Changes | 1 | NOT DECIDED |
| C-7L.3.7.4 — Person-Box merge-proposal record | Changes | 1 | NOT DECIDED |
| C-7L.3.7.4.1 — Person-Box merge candidate pair | Fails closed by | 1 | NOT DECIDED |
| C-7L.3.7.4.1 — Person-Box merge candidate pair | Fed by | 1 | NOT DECIDED |
| C-7L.3.7.4.1 — Person-Box merge candidate pair | Gated by | 1 | NOT DECIDED |
| C-7L.3.7.4.2 — Person-Box merge gathered evidence | Fails closed by | 1 | NOT DECIDED |
| C-7L.3.7.4.2 — Person-Box merge gathered evidence | Fed by | 1 | NOT DECIDED |
| C-7L.3.7.4.2 — Person-Box merge gathered evidence | Gated by | 1 | NOT DECIDED |
| C-7L.3.7.4.3 — Person-Box merge unmet-definite gap | Fed by | 1 | NOT DECIDED |
| C-7L.3.7.4.3 — Person-Box merge unmet-definite gap | Changes | 1 | NOT DECIDED |
| C-7L.3.7.5 — Person-Box join event | Changes | 1 | NOT DECIDED |
| C-7L.3.7.6 — Person-Box wrong-join correction event | Fails closed by | 1 | NOT DECIDED |
| C-7L.3.7.6 — Person-Box wrong-join correction event | Gated by | 1 | NOT DECIDED |
| C-7L.3.7.6 — Person-Box wrong-join correction event | Changes | 1 | NOT DECIDED |
| C-7L.3.7.7 — Person-Box alias record | Fails closed by | 1 | NOT DECIDED |
| C-7L.3.7.7 — Person-Box alias record | Fed by | 1 | NOT DECIDED |
| C-7L.3.7.7 — Person-Box alias record | Gated by | 1 | NOT DECIDED |
| C-7L.5 — Seven-section Person-Box view | Changes | 1 | NOT DECIDED |
| C-7L.5.1 — Person-Box roots section | Fails closed by | 1 | NOT DECIDED |
| C-7L.5.1 — Person-Box roots section | Fed by | 1 | NOT DECIDED |
| C-7L.5.1 — Person-Box roots section | Gated by | 1 | NOT DECIDED |
| C-7L.5.2 — Person-Box readings section | Fails closed by | 1 | NOT DECIDED |
| C-7L.5.2 — Person-Box readings section | Fed by | 1 | NOT DECIDED |
| C-7L.5.2 — Person-Box readings section | Gated by | 1 | NOT DECIDED |
| C-7L.5.4 — Person-Box clashes section | Fails closed by | 1 | NOT DECIDED |
| C-7L.5.4 — Person-Box clashes section | Gated by | 1 | NOT DECIDED |
| C-7L.5.5 — Person-Box Ness-response section | Fails closed by | 1 | NOT DECIDED |
| C-7L.5.5 — Person-Box Ness-response section | Fed by | 1 | NOT DECIDED |
| C-7L.5.5 — Person-Box Ness-response section | Gated by | 1 | NOT DECIDED |
| C-7L.5.6 — Person-Box themes section | Fails closed by | 1 | NOT DECIDED |
| C-7L.5.6 — Person-Box themes section | Gated by | 1 | NOT DECIDED |
| C-7L.5.7 — Person-Box unresolved-identity section | Gated by | 1 | NOT DECIDED |
| C-7L.5.8 — Person-Box view filters | Fails closed by | 1 | NOT DECIDED |
| C-7L.5.8 — Person-Box view filters | Gated by | 1 | NOT DECIDED |
| C-7L.5.8 — Person-Box view filters | Changes | 1 | NOT DECIDED |
| C-7L.5.8.1 — Person-Box time filter | Fails closed by | 1 | NOT DECIDED |
| C-7L.5.8.1 — Person-Box time filter | Fed by | 1 | NOT DECIDED |
| C-7L.5.8.1 — Person-Box time filter | Gated by | 1 | NOT DECIDED |
| C-7L.5.8.2 — Person-Box perspective-role filter | Fails closed by | 1 | NOT DECIDED |
| C-7L.5.8.2 — Person-Box perspective-role filter | Fed by | 1 | NOT DECIDED |
| C-7L.5.8.2 — Person-Box perspective-role filter | Gated by | 1 | NOT DECIDED |
| C-7L.5.8.3 — Person-Box theme filter | Fails closed by | 1 | NOT DECIDED |
| C-7L.5.8.3 — Person-Box theme filter | Fed by | 1 | NOT DECIDED |
| C-7L.5.8.3 — Person-Box theme filter | Gated by | 1 | NOT DECIDED |
| C-7L.5.8.4 — Person-Box source-thread filter | Fails closed by | 1 | NOT DECIDED |
| C-7L.5.8.4 — Person-Box source-thread filter | Fed by | 1 | NOT DECIDED |
| C-7L.5.8.4 — Person-Box source-thread filter | Gated by | 1 | NOT DECIDED |
| C-7L.5.8.5 — Person-Box lifecycle-confirmation filter | Fails closed by | 1 | NOT DECIDED |
| C-7L.5.8.5 — Person-Box lifecycle-confirmation filter | Fed by | 1 | NOT DECIDED |
| C-7L.5.8.5 — Person-Box lifecycle-confirmation filter | Gated by | 1 | NOT DECIDED |
| C-7L.5.9 — Person-Box full-chronology toggle | Fails closed by | 1 | NOT DECIDED |
| C-7L.5.9 — Person-Box full-chronology toggle | Fed by | 1 | NOT DECIDED |
| C-7L.5.9 — Person-Box full-chronology toggle | Gated by | 1 | NOT DECIDED |
| C-7L.5.10 — Person-Box owning-layer status labels | Fails closed by | 1 | NOT DECIDED |
| C-7L.5.10 — Person-Box owning-layer status labels | Fed by | 1 | NOT DECIDED |
| C-7L.5.10 — Person-Box owning-layer status labels | Gated by | 1 | NOT DECIDED |
| C-7L.5.11 — Person-Box original-record cross-links | Fails closed by | 1 | NOT DECIDED |
| C-7L.5.11 — Person-Box original-record cross-links | Fed by | 1 | NOT DECIDED |
| C-7L.5.11 — Person-Box original-record cross-links | Gated by | 1 | NOT DECIDED |
| C-7L.6 — Person-Box cross-batch identity links | Changes | 1 | NOT DECIDED |
| C-7L.6.1 — Person-Box per-element batch identity | Fails closed by | 1 | NOT DECIDED |
| C-7L.6.1 — Person-Box per-element batch identity | Fed by | 1 | NOT DECIDED |
| C-7L.6.1 — Person-Box per-element batch identity | Gated by | 1 | NOT DECIDED |
| C-7L.6.2 — Person-Box cross-batch identity tag | Fails closed by | 1 | NOT DECIDED |
| C-7L.6.2 — Person-Box cross-batch identity tag | Gated by | 1 | NOT DECIDED |
| C-7L.7 — Person-Box Holding through linked objects | Fails closed by | 1 | NOT DECIDED |
| C-7L.7 — Person-Box Holding through linked objects | Gated by | 1 | NOT DECIDED |
| C-7L.7 — Person-Box Holding through linked objects | Changes | 1 | NOT DECIDED |
| C-7L.8 — Person-Box held-material metadata boundary | Changes | 1 | NOT DECIDED |
| C-7L.9.1 — Person-Box permission categories | Fed by | 1 | NOT DECIDED |
| C-7L.9.1 — Person-Box permission categories | Gated by | 1 | NOT DECIDED |
| C-7L.9.2 — Person-Box Ness-presence permission condition | Fed by | 1 | NOT DECIDED |
| C-7L.9.2 — Person-Box Ness-presence permission condition | Gated by | 1 | NOT DECIDED |
| C-7L.9.3 — Person-Box visibility restriction | Fed by | 1 | NOT DECIDED |
| C-7L.9.4 — Separate parent Person-Box identities | Fails closed by | 1 | NOT DECIDED |
| C-7L.9.4 — Separate parent Person-Box identities | Fed by | 1 | NOT DECIDED |
| C-7L.9.4 — Separate parent Person-Box identities | Gated by | 1 | NOT DECIDED |
| C-7L.10.1 — Unknown-speaker attributed-material minimum | Fed by | 1 | NOT DECIDED |
| C-7L.10.1 — Unknown-speaker attributed-material minimum | Gated by | 1 | NOT DECIDED |
| C-7L.10.2 — Unknown-speaker capture-time certainty minimum | Gated by | 1 | NOT DECIDED |
| C-7L.10.3 — Unknown-speaker no-spoofing condition | Gated by | 1 | NOT DECIDED |
| C-7L.10.4 — Unknown-speaker authorized-promotion condition | Gated by | 1 | NOT DECIDED |
| C-7L.10.5 — Unknown-speaker reading-confidence minimum | Gated by | 1 | NOT DECIDED |
| C-7L.10.6 — Unknown-speaker Person-Box rule condition | Fed by | 1 | NOT DECIDED |
| C-7L.11.1 — Enrollment provisional link type | Fails closed by | 1 | NOT DECIDED |
| C-7L.11.1 — Enrollment provisional link type | Fed by | 1 | NOT DECIDED |
| C-7L.11.1 — Enrollment provisional link type | Gated by | 1 | NOT DECIDED |
| C-7L.11.2 — Enrollment provisional link certainty | Fails closed by | 1 | NOT DECIDED |
| C-7L.11.2 — Enrollment provisional link certainty | Fed by | 1 | NOT DECIDED |
| C-7L.11.2 — Enrollment provisional link certainty | Gated by | 1 | NOT DECIDED |
| C-7L.11.3 — Enrollment provisional link proposal ID | Fails closed by | 1 | NOT DECIDED |
| C-7L.11.3 — Enrollment provisional link proposal ID | Fed by | 1 | NOT DECIDED |
| C-7L.11.3 — Enrollment provisional link proposal ID | Gated by | 1 | NOT DECIDED |
| C-7L.11.4 — Enrollment provisional link meaning | Fails closed by | 1 | NOT DECIDED |
| C-7L.11.4 — Enrollment provisional link meaning | Fed by | 1 | NOT DECIDED |
| C-7L.11.4 — Enrollment provisional link meaning | Gated by | 1 | NOT DECIDED |
| C-7L.11.5 — Enrollment provisional link basis | Fails closed by | 1 | NOT DECIDED |
| C-7L.11.5 — Enrollment provisional link basis | Gated by | 1 | NOT DECIDED |
| C-7L.11.6 — Enrollment proposed input-bundle reference | Fails closed by | 1 | NOT DECIDED |
| C-7L.11.6 — Enrollment proposed input-bundle reference | Gated by | 1 | NOT DECIDED |
| C-7L.11.7 — Enrollment confirmed Ness-box reference | Fails closed by | 1 | NOT DECIDED |
| C-7L.11.7 — Enrollment confirmed Ness-box reference | Gated by | 1 | NOT DECIDED |
| C-7L.11.8 — Enrollment link operation reference | Fails closed by | 1 | NOT DECIDED |
| C-7L.11.8 — Enrollment link operation reference | Gated by | 1 | NOT DECIDED |
| C-7L.11.9 — Enrollment link session reference | Fails closed by | 1 | NOT DECIDED |
| C-7L.11.9 — Enrollment link session reference | Gated by | 1 | NOT DECIDED |
| C-7L.11.10 — Enrollment link eligible-reading references | Fails closed by | 1 | NOT DECIDED |
| C-7L.11.10 — Enrollment link eligible-reading references | Gated by | 1 | NOT DECIDED |
| C-7L.11.11 — Enrollment link eligibility-decision references | Fails closed by | 1 | NOT DECIDED |
| C-7L.11.11 — Enrollment link eligibility-decision references | Gated by | 1 | NOT DECIDED |
| C-7L.11.12 — Enrollment link prerequisite-evidence references | Fails closed by | 1 | NOT DECIDED |
| C-7L.11.12 — Enrollment link prerequisite-evidence references | Gated by | 1 | NOT DECIDED |
| C-7L.11.13 — Enrollment committed-link handoff gate | Gated by | 1 | NOT DECIDED |
| C-7L.11.13.1 — Enrollment current committed-link result | Fails closed by | 1 | NOT DECIDED |
| C-7L.11.13.1 — Enrollment current committed-link result | Fed by | 1 | NOT DECIDED |
| C-7L.11.13.1 — Enrollment current committed-link result | Gated by | 1 | NOT DECIDED |
| C-7L.11.13.2 — Enrollment refused-link result | Fed by | 1 | NOT DECIDED |
| C-7L.11.13.2 — Enrollment refused-link result | Gated by | 1 | NOT DECIDED |
| C-7L.11.13.3 — Enrollment pending-link result | Fed by | 1 | NOT DECIDED |
| C-7L.11.13.3 — Enrollment pending-link result | Gated by | 1 | NOT DECIDED |
| C-7L.11.13.4 — Enrollment stale-link result | Fed by | 1 | NOT DECIDED |
| C-7L.11.13.4 — Enrollment stale-link result | Gated by | 1 | NOT DECIDED |
| C-7L.11.13.5 — Enrollment contradictory-link result | Fed by | 1 | NOT DECIDED |
| C-7L.11.13.5 — Enrollment contradictory-link result | Gated by | 1 | NOT DECIDED |
| C-7L.11.13.6 — Enrollment unverifiable-link result | Fed by | 1 | NOT DECIDED |
| C-7L.11.13.6 — Enrollment unverifiable-link result | Gated by | 1 | NOT DECIDED |
| C-7L.12 — Person-Box generic-connection use boundary | Changes | 1 | NOT DECIDED |
| C-7L.14 — Person-Box operation and presentation records | Fails closed by | 1 | NOT DECIDED |
| C-7L.14 — Person-Box operation and presentation records | Changes | 1 | NOT DECIDED |

## Plain-gate and empty-box review

Every current ALONE field, TOGETHER field and USED BY row was reviewed against its source and neighboring boxes. Required actor/time/location/enrollment-reference fields now have direct omission prohibitions. The ordinary clear/unclear and definite/pending tests are distinct from enrollment provenance; no numerical score or manual-approval stage is added. Unknown-speaker voice-link minima remain named preconditions with no invented values. The held-content source card retains its actual DESIGNED stamp. View details carry actual clash/gap behavior, and another layer's labels are displayed without recomputation. Enrollment result classes all block profile creation unless current owner-held commitment exists. The generic-connection consumer writes its checks and consequences while leaving its proposed record/state atoms to CH06-g. Empty wire-level failure slots are not converted into invented enforcement. Prior cards remain immutable, with the new CH02 C-7B.9.11 target-stamp issue carried in the manifest.

| Card | Plain gate justification |
|---|---|
| C-7L.3.6 — Ness Person-Box responses | Ness's actual identity response is a human act; the ordinary completely-clear and definite paths do not acquire an approval requirement. |

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

## READ RECORD

Behavior remains pinned to 6a7160ba688ba4e433a31899162815df7e2bab17. Whole-file credit below is limited to files actually read in full during this piece; scoped reopens preserve prior cumulative credits without inventing new ones. Contract §§5–11 and lessons were reopened before writing; contract §11.3 is reopened after writing. Source discovery preceded the card map. The discovery rows identify partial review and later ownership honestly; no shared-package-wide completion is claimed.

| Source file | Reading scope / whole-file credit | SHA-256 |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: complete §7L; §§25.2 through Person-Box Visibility, 25.3 Voice Profile Architecture and Minimum Evidence for Person-Box Linking, 25.4 PBR/multi-speaker/failure interfaces; earlier §0B/7Q authorization rules reused. | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped: complete C-7L and adjoining Group D/CY-A relationship checks. | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Scoped: DUMB gather and §3G Person-Box status for authority comparison. | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Scoped: complete §7L compared with V10. | `cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md` | Scoped reopen: §§7/9/12–16/18–20 in full; whole-file credit retained from CH06-a. | `3566cf0f917fb4f7eb329d9089f6e238fe4afbacbae2c73c8b2716e3397e7c2e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Prior whole-file credit retained; accepted identity reused. | `405717e5528df74b9842dee6da8b3de69b82a738e478d06c2e1025243ae56a16` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md` | Scoped: full §6 reopened; §5A complete-set semantic gate and existing telling-reference owners reused. | `f91da6426817031cf2c0b14fb467a3e1d97d2ea3c67d27a07d8b1831f9895a55` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Scoped: complete A3.5 Holding subsection in §4. | `b37f965a343dbf86130f96591d58de9288ad0a746a68e8ae8fdd7b66208a63da` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped reopen: §12 Person-Box/PBR query and authorization-control boundary; prior full §12 reading retained. | `bc1095955525fcea56cb4d16057c93bfb15eec42a83a1b644baf0e87a473f64e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Scoped: §9 held-pre-ingest boundary and source/dependency identity references; no full-file credit. | `5797a2ac51328985e479d2bc101f310b96d2d75976acfaf5f066c529b31d309b` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` | Scoped: complete §§12A/13/14 and §19 I12/I13 with adjoining owner interfaces; full enrollment deferred to CH09-h. | `184a63cf7dfbefdd73ea84c02506e3478374a48df2d9a2e174ed9a38305cacb6` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: acceptance, exact source identity, committed-link scope and receipt-audit condition; receipt itself is not treated as independently passed. | `df028286c89b7c0a4bea3bb1403d910b11f993bac010d03320f55eeec71d636a` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md` | Scoped: complete §§12C/14/15 and interface/discovery matches; full connection state machines remain CH06-g. | `6a3b7cf71546ed237507b34b1a24a759d34ca683216b255c91ac4add679b1bfd` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: acceptance, exact source identity, Person-Box separation and preserved receipt-audit condition. | `699b9e64e1bbd485dfd7f78bd65e0e8de275c0242f3d1da9474e30e9d77c74a1` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md` | Scoped reuse: §7 real-person possibility boundary with existing C-7B.9.11 owner. | `1a4d8b9a24f15ce371dd49b28bde7bf9888e0fe114ec4bdab6e6446af495bf8d` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md` | Scoped: Person-Box surface coverage, purpose/privacy, influence-removal and third-party boundary; full owner CH08-a. | `3deacafbd7fb840404d59f05b0f314199467889735dcb9f6243f7ef14078d6f5` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md` | Scoped: §15.4 hiding and per-surface acknowledgment/failure boundary; full privacy record/lifecycle atoms remain CH08-a. | `7fda28e994336a7ea0d17e217025cb71c116ec42ce3ecde3d8c9110783b52aad` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md` | Scoped: §11 retained-archive no-read/no-inspection boundary; source record schemas remain existing C-TSC ownership. | `46cf463389ea339bb3a908177dda8d1548095e21da6abebcd2efeb6a8a54c0ff` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md` | Scoped: retained archive never active/queryable by Person-Boxes; no new archive behavior introduced. | `1b539f57a7d31daba7c8da15d0dcdf988eba2e560c5d9532e3db42a28bcf96e6` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | Scoped discovery: B23 dependency and per-batch provenance ownership; no store mechanics rewritten. | `baca06e562027a080dab4384943bfb87947c6f598b36776f1016fa8472384a87` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` | Scoped: state identity continuity, no third-party psychological world profile and Person-Box source-reference snapshot fields; current scope left to CH06-f/d. | `0c9a201130d5811c838fea0d5655c8a98aac909afdc60024830204a690e77f97` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Scoped: same-Person-Box explicit_links in retrieval and Person-Box candidate family in RM-CV-01; owning declarations remain CH05-c/CH06-d/CH08-b. | `b2a5b3fbea75f7123a16c8a45c0fb096f4c4565585a4a0c7b7709e70f27d000e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md` | Scoped: §6 relevance never merges Person-Boxes or alters evidence. | `c754b27e44cdb578e1cc25e7de681c9d2afd68fedc6e974cc45c8aa6c83d553f` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | Scoped: connection/third-party consistency and archive/privacy ownership; no new Person-Box mechanism derived. | `b20d4ee944d5a575b307d70485e5c074c4b298f43a3082ddd760159aa61d924d` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md` | Scoped: §4.4 separate top-security/Person-Box condition; full identity/access owner remains CH09. | `41e1f67d635a0e07a73ad572e8931bceaffd3cf6f44d88c3eaea9872818d339b` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` | Scoped: same-committed-state stream entries, person_box_id, pbr_version and ness_presence_satisfied; ownership remains SACL/access wiring. | `c449728139f732d5aefe5efd7ca1a0d251937c64bd73504ff8527cc3ec01b305` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` | Scoped: identity registry distinguishes connection identity from Person-Box link authority; no kernel mechanism copied. | `1f9ea714f1a182c0857e80399850a3aeebcf4a50a32d5a200fce57a5d5f47ae3` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md` | Scoped: complete §6 boundaries/non-effects, especially presentation does not change Person-Boxes; room mechanics remain CH10-e. | `fa42d8ff4295c08df0634978107e555d6244f7e4c033d5f8bc4a7588deac3af0` |
| `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_2.md` | Scoped: §§13.1/13.2 complete general-card and pointer-only boundaries; full interface remains CH10-e. | `c56829dddef3c5ec37b7b13a263b407c2e7a4374c800cce3a78db983cce3031d` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md` | Scoped discovery: Person-Box non-fact/no-second-store boundaries; interface/world scope remains CH10-e. | `114a118c242ea553b11488eb6380da1458f3788084c4f86332ba45b9a6896273` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` | Scoped: §§15–18 complete derived multi-index direction; entity reference index belongs with index/retrieval, not a new Person-Box identity system. | `1386091a0977ac79588f22a9f85213579203637e493dbb2d75be3d893326aa28` |
| `05_ACTIVE_CANDIDATE/Thought_Branches_and_Simulation_Intent.md` | Scoped: predicted branches cannot become Person-Box facts; no mechanism taken from intent. | `91c4bc2ec40812491dcfc45a397c5a0812b45858c11d2ced7f604dfd8a2f2f92` |
| `05_ACTIVE_CANDIDATE/Other_Future_Feature_Intent_Excerpts.md` | Scoped discovery: Person-Box navigation/search dependency only; no new behavior derived. | `efc6809ea43def73b949ea3843b98be23b2f1c4f20a4c3589012fa8d55901951` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Scoped: Group 6/FR-0131 thin-evidence memory-health query; existing C-READ.8.6 retained; no archive opened. | `9f6f9cac1e07ab14f0c6f3ed834b8260265dac6f6a430fa12be5c6e4c3f0b59f` |
| `05_ACTIVE_CANDIDATE/02-NH_BUNDLE_6_A3_DECISIONS_WORKING_RECORD_v1-1-.md` | Scoped discovery: A3.5 Holding; accepted policy supplies behavior. | `1bbf4af0f6437255113c7efd32b8c57718a37a8ae379350327463a72e451922f` |
| `05_ACTIVE_CANDIDATE/NH_A2_CURRENT_STATUS_v1_1.md` | Scoped discovery: A5/B4 dependency wording; accepted Bundle 3 now supplies their scoped design. | `35d1a10af9a16685515a6b668cfe5a0b3be3fe80abef901e3277b4901d22b167` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | Scoped discovery: Person-Box/Bundle 3/A19 navigation, not behavior authority. | `457c6f43562a92cd82076640af44a58ea412335284c0e61da3c38f3ba63f24b9` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | Scoped discovery: Person-Box/Bundle 3/A19 navigation, not behavior authority. | `3f1b95da77f620597e9ba862568f4247d1eb4d50f73c620888637dfcde03e3c9` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Scoped discovery: Person-Box/Bundle 3/A19 navigation, not behavior authority. | `aafc7abe6522f4c7ece23f40560e648866188e1b5401ed6cd298809d15ed0f7b` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Scoped discovery: current index ownership and source identity; no behavior derived from index text. | `aad8d1aeee9a331ad6f4d9ddbcfa9c42eae2a94e1ef1bccde7484079181ff7b4` |

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

Round 4A later changed Chapters 0, 1, 2, 3-a to 3-d and 6-a to 6-g; the identities above are those preserved when this chapter was written, and the round 4A identities are listed in the round 4A delivery manifest.

### READ-folder files not yet read whole

66 inherited pending files remain. Scoped reading receives no new whole-file credit.

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
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md`
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
§1.3 no history/actions/roles/workflow in this chapter: PASS — 103 behavior cards reviewed; 0 workflow/advice hits. Delivery metadata remains outside behavior.
§1.4 every gap written as NOT DECIDED: PASS — 217 empty fields and 2 empty USED BY cells match 219 register rows; 13 additional mechanical slots are explicit.
§1.5 conflicts marked, none resolved: PASS — no new conflict resolution. Accepted Bundle 3 fills the open A5/A14/B4/B23/B25 slots. Ordinary identity certainty, voice-evidence prerequisites and provisional enrollment provenance remain distinct. Inherited conflicts and the B26 source-scope gap stay in the manifest.
§3 exactly one stamp per line: PASS — 103 headers, 720 populated fields and 302 USED BY rows checked. 1 BUILT field lines name only the existing built reading-record source; no new machinery is stamped BUILT.
§4 every behavior line cited in the exact format: PASS — 82 distinct citations; 82 resolve within the named pinned sections. Populated fields and use rows are cited; the source-to-claim review accompanies mechanical resolution.
§5.4 one name per thing: PASS — 103 unique current IDs without prior collisions; 1078 named-card mentions checked. Shared atoms retain their established IDs and names.
§6 all template fields present, in order, for every part: PASS — 103 templates and 937 field lines checked.
§6.3 reciprocity within this chapter: PASS — 207 internal relationship occurrences checked; 68 outgoing and 14 incoming continuation rows name both ends. No missing reciprocal; prior files remain unchanged.
§6.4 every decided detail written in, no citation used in place of content: PASS — 24 source-to-card rows reviewed; 59 expected source-name literals present. Existing atomic owners and remaining scopes are explicit.
§6.5 sub-parts recursed to the bottom: PASS — link and anchor fields, ordinary test outcomes, four search scopes, six human responses, event kinds and proposal fields, seven sections and five filters, cross-batch provenance, ordinary voice-link conditions, enrollment fields and six handoff outcomes have templates. Existing telling/Holding/clash-gap atoms retain their owners; current-use and full access state machines have explicit later ownership. 0 current cards have all three TOGETHER fields empty.
§9 coverage matrix rows added for every file used: PASS — all 145 pinned READ-folder file paths remain in the carried inventory; current additions and 40 current READ RECORD fingerprints are present. Shared-package coverage remains partial where stated.
§10.11 no recommendation, no sentence addressed to Ness: PASS — all 103 behavior cards reviewed; no recommendation or addressed instruction.
Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`.

### Computed self-check results

Writer checks and the accompanying manual source/box review returned no unresolved current-file errors. They are not an independent audit or adoption. Plain human/precondition gates are justified in the inventory above.

| Check | Count |
|---|---|
| cards | 103 |
| field_lines | 937 |
| used_by_rows | 302 |
| empty_fields | 217 |
| internal_relationships | 207 |
| external_relationships | 68 |
| distinct_citations | 82 |
| resolved_citations | 82 |
| empty_together_cards | 0 |
| plain_together_lines | 1 |
| formula_hits | 0 |
| wording_hits | 0 |
| errors | 0 |
| named_card_mentions_checked | 1078 |
| misfiled_box_fields_scanned | 937 |
| restriction_failure_gate_slots_reviewed | 312 |
| registered_empty_fields | 217 |
| cross_piece_continuations_checked | 68 |
| covered_read_file_paths | 145 |
| read_fingerprints_checked | 40 |
| source_names_checked | 59 |
| source_names_missing | 0 |
| built_field_lines | 1 |
| behavior_workflow_hits | 0 |
| plain_gates_justified | 1 |
| outgoing_continuations | 68 |
| incoming_continuations | 14 |
| registered_fields | 217 |
| additional_gaps | 13 |
| pending_source_paths | 66 |
| source_map_rows | 24 |
| read_record_rows | 40 |

The delivery recount compares these metrics with the finished file.
