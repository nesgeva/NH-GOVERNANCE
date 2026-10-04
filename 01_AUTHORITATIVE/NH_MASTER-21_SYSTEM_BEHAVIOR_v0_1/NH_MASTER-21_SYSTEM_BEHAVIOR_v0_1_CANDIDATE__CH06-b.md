# Chapter 6-b — Group D: C-7K

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH06-b.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`  

This piece covers Story Layer organization, perspective separation, cross-time navigation, firmness use, hybrid themes and their records/actions, Holding and operation records. Existing C-READ telling-field, firmness-label, evidence-basis, semantic-eligibility and reference cards retain their IDs; the engine and reread machinery retain CH03-j and CH05-d ownership. Person-Boxes, Computed View, View Layer and Living State Web internals remain CH06-c through CH06-f; privacy, relevance, LMAC and reading affirmation remain CH08-a/b/c/f; full side paths remain CH11.

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; NHD identifiers locate decisions in the pinned index and do not replace behavior citations.

<!-- BEGIN BEHAVIOR -->

### C-7K — Story Layer (§7K)
Stamp: DESIGNED    Source: [V10 §7K] [MAP C-7K]

ALONE
- What it is: DESIGNED — The layer that receives tellings unchanged and organizes them by perspective, theme and time while keeping each person's story separate. [V10 §7K] [MAP C-7K]
- Takes in: DESIGNED — Tellings from engine passes, their roots/readings and perspective provenance, time, firmness evidence, theme proposals and Ness's theme actions. [V10 §7K] [MAP C-7K]
- Does: DESIGNED — Shows how narrative threads develop, shift or fracture across time. Preserves clashes, distinguishes temporal change from contradiction and permits inspection by person, theme or period with perspective, firmness and root support visible. [V10 §7K] [MAP C-7K]
- Gives out: DESIGNED — Navigable tellings and ongoing-story sequences; no synthesized authoritative account. [V10 §7K] [MAP C-7K]
- Must never: DESIGNED — Merge conflicting tellings; turn repetition into fact; assign one authoritative story to a person, relationship or event; invent connective tissue unsupported by roots; treat a telling gap as evidence of absence; flatten temporal change; let one perspective overwrite another; decide whose telling is correct. [V10 §7K] [MAP C-7K]
- Fails closed by: ACCEPTED — Keeps telling-specific organization blocked until a complete valid telling set with its checkpoint, or a legitimate zero-telling sentinel, exists. Authorized safety discovery remains a separate route. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.2]

TOGETHER
- Fed by: BUILT — C-READ — Reading record, validator, writer (§6B): embedded tellings and the immutable reading/root references. [V10 §6B] [V10 §7K]
- Fed by: ACCEPTED — C-READ.10.14 — Telling-reference handoff: complete integrity-valid first-class telling cards and stable reference chains. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [NHD-A2]
- Fed by: DESIGNED — C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K): story-bearing pass output; C-ENGINE-C.11 — Theme proposal boundary: proposed themes with support and uncertainty. [V10 §7K] [MAP C-7K]
- Fed by: DESIGNED — C-7K.1 — Telling and ongoing story: bounded tellings in an open sequence; C-7K.2 — Explicit connections across time: labeled cross-time connections; C-7K.3 — Structured perspective in organization: separated perspective roles; C-7K.6 — Hybrid theme system: proposed and confirmed navigational themes; C-7K.8 — Story-Layer operation records: permanent operation records. [V10 §7K] [V10 §0B]
- Fed by: ACCEPTED — C-7K.4 — First-class telling ownership and reference boundary: the accepted immutable-card identity seam; C-7K.5 — Qualitative firmness in the Story Layer: qualitative, evidence-based firmness; C-7K.7 — Holding through separate linked objects: Holding through separate linked objects. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §1] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4]
- Fed by: DESIGNED — C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B): the perspective dimension within its CY-A pass; C-7B.3 — Story-Layer Web: human perspectives preserved as separate tellings; C-7B.3.1 — Per-person perspective: the human perspective being represented; C-7B.3.2 — N.H is not a teller: the engine view kept separately as a weightless NOTE; C-7B.3.4 — Clash preservation: disagreeing tellings with clash preserved. [MAP C-7B] [MAP CY-A] [V10 §7K]
- Fed by: DESIGNED — C-7B.3.3 — Firmness reading: provisional evidence-based firmness; C-7B.3.3.1 — Evidence basis: observable signals; C-7B.3.3.2 — Separate model confidence: firmness separate from confidence; C-7B.3.3.3 — Direct certainty evidence: stronger direct self-report; C-7B.3.3.4 — Attribution strength: weaker reported or uncertain attribution; C-7B.3.3.5 — Conflicting firmness signals: conflicting signals without forced resolution; C-7B.3.3.6 — Unsupported firmness omission: unsupported firmness omitted. [V10 §7K / FIRMNESS RULE] [MAP C-7B]
- Gated by: ACCEPTED — C-READ.10.10 — Telling-set semantic eligibility: complete-set semantic eligibility must hold before telling-specific organization. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): authorize the actual internal or visible purpose before use; no link or secondary index bypasses protection. [V10 §7Q / TWO-STAGE OUTPUT ACCESS CONTROL] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §9]
- Gated by: DESIGNED — C-7A — Universal Filter (§7A): per-person perspectives and clashes remain separate; C-7A.8 — R5.5 — Per-person STORY-layer: the system's own view stays a weightless NOTE. [V10 §7A] [V10 §7K]
- Gated by: ACCEPTED — C-7B.9.11 — Forbidden Wonder evidence uses: accepted Wonder material stays possibility material and cannot enter anyone's story as observed reality. [04/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md §7]
- Changes: DESIGNED — C-7L — Person-Boxes (§7L): supplies linked tellings in each perspective role; C-7M — Computed View (§7M): supplies source tellings for current presentation; C-7D — Living State Web (§7D): supplies source objects with root support, no added evidential weight. [V10 §7K] [MAP C-7K]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7L — Person-Boxes (§7L) | Tellings and their perspective/root provenance. | Links the tellings without making a profile or replacing a source. | Organized references in the person's view. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [MAP C-7K] |
| 2 · DESIGNED | C-7M — Computed View (§7M) | Preserved telling references. | Uses them as source objects while keeping conflicting tellings distinct. | The current picture, not the source history. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [MAP C-7K] |
| 3 · DESIGNED | C-7D — Living State Web (§7D) | Tellings with direct roots and their inspectable source chain. | Retains their perspective, firmness limits and grounding. | Eligible state source references, not extra evidence weight. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [MAP C-7K] |
| 4 · DESIGNED | C-ENGINE-C.11 — Theme proposal boundary | The hybrid-theme rules and organized tellings. | Allows proposed themes with roots, telling/reading IDs, proposer, reason, time and uncertainty; only Ness can confirm. | A proposal in the Story Layer without a silent influence on future readings. | [V10 §7K / HYBRID THEME SYSTEM] |
| 5 · DESIGNED | C-LMAC — Live Mechanism Access Coordinator (§26) | An authorized story-layer query. | Returns perspective-owned tellings with clashes preserved and the component's provenance. | The requesting function receives the permitted live result. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 6 · DESIGNED | C-7K.1 — Telling and ongoing story | A telling and the surrounding sequence. | Keeps the bounded interpretation distinct from its ongoing story. | Patterns remain visible without a conclusion. | [V10 §7K / TELLING VS ONGOING STORY] |
| 7 · DESIGNED | C-7K.2 — Explicit connections across time | Tellings sharing explicit attributes. | Supplies the source references for labeled navigation across time. | No logical merge of the tellings. | [V10 §7K / CONNECTIONS ACROSS TIME] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8] |
| 8 · DESIGNED | C-7K.3 — Structured perspective in organization | The telling and its source attribution. | Carries the speaker, subject and perspective as separate roles. | No perspective is silently substituted. | [V10 §7K / STRUCTURED PERSPECTIVE MODEL] |
| 9 · ACCEPTED | C-7K.4 — First-class telling ownership and reference boundary | A complete telling card and source chain. | Keeps organization tied to the immutable first-class identity. | The source remains in its original home. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8] [NHD-A2] |
| 10 · ACCEPTED | C-7K.5 — Qualitative firmness in the Story Layer | The stance with its observable evidence. | Makes qualitative firmness available without a confidence or truth score. | A supported label or honest omission. | [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §1] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §2] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §3] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §4] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §5] |
| 11 · DESIGNED | C-7K.6 — Hybrid theme system | Tellings and proposals for their grouping. | Keeps theme navigation open to proposals and Ness's responses. | Confirmed categories remain navigation only. | [V10 §7K / HYBRID THEME SYSTEM] |
| 12 · ACCEPTED | C-7K.7 — Holding through separate linked objects | Person-related understanding and linked objects. | Preserves Ness's perspective beside evidence and other perspectives. | No profile or replacement memory. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] |
| 13 · DESIGNED | C-7K.8 — Story-Layer operation records | An actual organization, receipt, response or influence operation. | Supplies the occurrence and its provenance for one permanent record. | Connected operational history. | [V10 §0B] [MAP C-7K] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19] |
| 14 · DESIGNED | C-LEARN.4.2 — Pattern readings weighted as evidence | Patterns produced by the Meaning Engine, with confidence and firmness. | Supplies applicable firmness/evidence discipline. | Nothing in this card. | [V10 §26.7] [V10 §26.12] |
| 15 · ACCEPTED | C-LMAC.3.5 — Story Layer query contract | An authorized story-layer query. | Supplies the perspective-owned tellings. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 16 · DESIGNED | C-LEARN.9.4 — Repetition and new evidence never rewrite evidential standing | Repeated observations, new evidence and possible pattern conclusions. | Supplies firmness discipline. | Nothing in this card. | [V10 §26.12] |
| 17 · DESIGNED | C-AFFIRM — Off-board Affirmation Feedback Seam (§11 item 23) | Ness’s accept/reject response to one or more specific readings through the view/chat surface. | Takes this place's change: the separate dated event lives in the Story Layer. | The separate dated event lives in the Story Layer. | [V10 §11] [V10 §0] [MAP C-AFFIRM] |
| 18 · ACCEPTED | C-AFFIRM.7.1 — General telling responses stay in the Story Layer | A response to a telling rather than the specific-reading accept/reject event. | Owns the telling layer and its separate responses. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §17] |
| 19 · DESIGNED | C-LEARN.3.2 — Meaning Engine readings carry learning content | Shared behavioral and outcome roots. | Supplies applicable firmness discipline. | Nothing in this card. | [V10 §26.8] [V10 §26.12] |
| 20 · ACCEPTED | C-7Q.11.7 — Meaning, derived-store and simulation privacy interface | Authorized inputs, explicit influence-removal scope, third-party separation and any simulation approval. | Takes this place's change to story assembly: internal purpose and the influence set are checked, and third-party separation and labels are carried in. | Story assembly keeps its privacy and third-party constraints intact. | [04/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md §16] |

SUB-PARTS: C-7K.1 — Telling and ongoing story; C-7K.2 — Explicit connections across time; C-7K.3 — Structured perspective in organization; C-7K.4 — First-class telling ownership and reference boundary; C-7K.5 — Qualitative firmness in the Story Layer; C-7K.6 — Hybrid theme system; C-7K.7 — Holding through separate linked objects; C-7K.8 — Story-Layer operation records

### C-7K.1 — Telling and ongoing story
Stamp: DESIGNED    Source: [V10 §7K / TELLING VS ONGOING STORY]

ALONE
- What it is: DESIGNED — The distinction between one bounded interpretation and a collection of tellings across time. [V10 §7K / TELLING VS ONGOING STORY]
- Takes in: DESIGNED — A telling about one root, produced in one pass, from one perspective at one moment; other tellings across time. [V10 §7K / TELLING VS ONGOING STORY]
- Does: DESIGNED — Keeps the telling local and specific. Presents the ongoing collection with agreements, shifts, contradictions and silences so that patterns can be seen without hardening them into conclusions. [V10 §7K / TELLING VS ONGOING STORY]
- Gives out: DESIGNED — A sequence that can be surfaced, without a conclusion drawn from the sequence alone. [V10 §7K / TELLING VS ONGOING STORY]
- Must never: DESIGNED — Treat the collection as a single authoritative story or merge conflicting tellings into a synthesized narrative. [V10 §7K / TELLING VS ONGOING STORY]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7K — Story Layer (§7K): the tellings being organized. [V10 §7K / TELLING VS ONGOING STORY]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7K — Story Layer (§7K) | One telling or its surrounding sequence. | Preserves the boundary between local interpretation and ongoing story. | A visible sequence with the differences intact. | [V10 §7K] |

SUB-PARTS: NONE

### C-7K.2 — Explicit connections across time
Stamp: DESIGNED    Source: [V10 §7K / CONNECTIONS ACROSS TIME] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8]

ALONE
- What it is: DESIGNED — Navigational links among tellings with explicitly shared attributes. [V10 §7K / CONNECTIONS ACROSS TIME] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8]
- Takes in: DESIGNED — The same `whose` or `perspective_owner`, theme, thread/source, overlapping time period, or shared root IDs. [V10 §7K / CONNECTIONS ACROSS TIME] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8]
- Does: DESIGNED — Labels each connection with its basis and pointers to supporting roots/readings. Link metadata keeps temporal change distinguishable from contradiction; a later telling does not automatically defeat an earlier one. [V10 §7K / CONNECTIONS ACROSS TIME] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8]
- Gives out: DESIGNED — Inspectable cross-time connections without logical merging. [V10 §7K / CONNECTIONS ACROSS TIME] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8]
- Must never: DESIGNED — Combine tellings through a navigation link, invent support or use recency to select a truth winner. [V10 §7K / CONNECTIONS ACROSS TIME] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Blocks telling-level navigation until the complete valid set or legitimate zero-telling condition holds. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1]

TOGETHER
- Fed by: DESIGNED — C-7K — Story Layer (§7K): the tellings and explicit shared attributes. [V10 §7K / CONNECTIONS ACROSS TIME] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-READ.10.10 — Telling-set semantic eligibility: the complete valid telling-set condition applies before semantic linking. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7K — Story Layer (§7K) | Tellings with explicitly shared attributes. | Connects them with labeled navigational links and a preserved source chain. | A navigable history with temporal change and contradiction still distinct. | [V10 §7K] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7K.3 — Structured perspective in organization
Stamp: DESIGNED    Source: [V10 §7K / STRUCTURED PERSPECTIVE MODEL]

ALONE
- What it is: DESIGNED — The separate speaker, subject and perspective roles used to organize each telling. [V10 §7K / STRUCTURED PERSPECTIVE MODEL]
- Takes in: DESIGNED — Required `root_speaker`, `subject` and `perspective_owner`; optional supported `attribution_path`; the recorded `evidence_relationship`. [V10 §7K / STRUCTURED PERSPECTIVE MODEL]
- Does: DESIGNED — Keeps root producer, subject and viewpoint owner distinct even when they happen to be the same person. Records direct self-report, direct quotation, reported speech, observation or engine inference. A nested attribution chain is retained only when the root supports it; unknown attribution stays explicitly unresolved. The engine's interpretive lens stays separate from the human perspective. [V10 §7K / STRUCTURED PERSPECTIVE MODEL]
- Gives out: DESIGNED — An attributed telling, with a supported chain such as `friend → quoted by father → reported by Ness` when present. Flat `whose` may remain for v1 compatibility. [V10 §7K / STRUCTURED PERSPECTIVE MODEL]
- Must never: DESIGNED — Assume that the root speaker is the subject or perspective owner; invent an attribution chain; present reported speech as direct access to another person's internal state. [V10 §7K / STRUCTURED PERSPECTIVE MODEL]
- Fails closed by: DESIGNED — Leaves unsupported attribution unresolved instead of guessing it. [V10 §7K / STRUCTURED PERSPECTIVE MODEL]

TOGETHER
- Fed by: DESIGNED — C-7K — Story Layer (§7K): the telling to be organized. [V10 §7K]
- Fed by: ACCEPTED — C-READ.10.1.4 — root_speaker: source speaker; C-READ.10.1.5 — subject: subject; C-READ.10.1.6 — perspective_owner: perspective owner; C-READ.10.1.7 — attribution_path: optional attribution chain; C-READ.10.1.8 — evidence_relationship: evidence relationship. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7K — Story Layer (§7K) | The three perspective roles, optional chain and evidence relationship. | Organizes tellings without collapsing human perspectives or the engine's lens. | Accurate attribution and explicit unresolved identity. | [V10 §7K / STRUCTURED PERSPECTIVE MODEL] |

SUB-PARTS: NONE

### C-7K.4 — First-class telling ownership and reference boundary
Stamp: ACCEPTED    Source: [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8] [NHD-A2]

ALONE
- What it is: ACCEPTED — Story Layer ownership of separate immutable telling cards with permanent stable `telling_id`s. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8] [NHD-A2]
- Takes in: ACCEPTED — Complete, integrity-valid cards linked to their immutable parent reading and supporting roots. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8] [NHD-A2]
- Does: ACCEPTED — Holds the cards and organizes by stable handle. Other consumers hold references with their own link metadata; no copy replaces the original. Each reread creates new telling IDs in its own envelope beside earlier tellings. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8] [NHD-A2]
- Gives out: ACCEPTED — Stable telling references with access to the complete reading/root provenance chain. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8] [NHD-A2]
- Must never: ACCEPTED — Treat a preparation manifest, partial card, integrity-failed card or embedded fallback as a canonical semantic telling; rewrite an earlier telling through a mutable latest record; make addressability into authority. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8] [NHD-A2]
- Fails closed by: ACCEPTED — Blocks ordinary semantic use until complete valid set evidence or a legitimate zero-telling sentinel exists; properly authorized recovery/governance discovery is not blocked by that semantic gate. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8] [NHD-A2]

TOGETHER
- Fed by: DESIGNED — C-7K — Story Layer (§7K): the incoming telling for organization. [V10 §7K]
- Fed by: ACCEPTED — C-READ.10.14.1 — Story Layer holds cards: the accepted Story Layer ownership handoff; C-READ.10.15 — New telling identities on reread: new telling identities on reread. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-READ.10.10 — Telling-set semantic eligibility: all expected cards/events and valid completion proof, or legitimate zero telling, before semantic use. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8] [NHD-A2]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7K — Story Layer (§7K) | Complete telling cards with stable IDs. | Keeps organization reference-based and the source records immutable. | Addressable tellings with no second authoritative copy. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7K.5 — Qualitative firmness in the Story Layer
Stamp: ACCEPTED    Source: [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §1] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §2] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §3] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §4] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The provisional reading of how strongly the perspective owner appears to hold a stance, separate from truth, confidence, grounding, relevance and source reliability. [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §1] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §2] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §3] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §4] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — Observable certainty/doubt self-report, explicit certainty words, hedging, repetition, emphasis, within-root consistency, commitment, reported speech, uncertain attribution and conflicting signals. Every non-omitted value carries `firmness_evidence_basis`. [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §1] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §2] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §3] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §4] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Uses `high_firmness` for strong consistent stance support without comparably weighted conflict; `moderate_firmness` for plain maintained commitment with at most mild qualification; `low_firmness` for tentative or doubted commitment; `mixed_firmness` for genuinely conflicting signals of comparable weight; `uncertain_firmness` when relevant signals exist but are too weak, ambiguous or attribution-degraded to name a level or a genuine two-sided conflict; `omitted_no_support` when no usable firmness signal exists. Direct self-report is qualitatively stronger than tone, style or repetition alone; reported speech or uncertain attribution lowers strength. [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §1] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §2] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §3] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §4] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — A qualitative label with source-grounded evidence, or honest absence of `firmness` on the A2 card and built embedded entry for the no-support outcome. Reading-level `confidence` retains `interpretation_confidence` and `source_reliability` on the reading. A revised firmness judgment is a new reading/telling, never an edit. The no-support outcome asserts nothing and requires no evidence basis; mixed_firmness is an active conflict finding. [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §1] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §2] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §3] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §4] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Write a numeric score, percentage, weight, ranking function or hidden threshold arithmetic; force a level; claim inner-state access; turn basis logging into extra evidence; let cross-record repetition raise firmness; use a firmness label to trigger, block or release a hold or `insufficient_context` reading; fill absence with `unknown` or a literal no-support placeholder. [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §1] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §2] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §3] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §4] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Uses the less-claiming outcome when a distinction cannot honestly be made; omits unsupported firmness. A legacy value without a recorded basis receives no invented evidence basis. [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §1] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §2] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §3] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §4] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: DESIGNED — C-7K — Story Layer (§7K): the stance and its perspective. [V10 §7K / FIRMNESS RULE]
- Fed by: ACCEPTED — C-READ.10.1.11 — firmness: the existing firmness field and its atomic label rules; C-READ.10.1.12 — firmness_evidence_basis: the existing evidence-basis field and qualitative hierarchy. [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §2] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §3]
- Gated by: ACCEPTED — C-READ.10.1.11.7 — Never force a firmness level: the never-force rule requires the less-claiming supported outcome; C-READ.10.1.12 — firmness_evidence_basis: every non-omitted assignment requires source-grounded basis. [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §1] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §2] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §3] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §4] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7K — Story Layer (§7K) | The telling's firmness and evidence basis. | Shows apparent stance strength as a bounded, revisable interpretation. | Transparent qualitative stance information without added truth or authority. | [V10 §7K / FIRMNESS RULE] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §1] |

SUB-PARTS: NONE

### C-7K.6 — Hybrid theme system
Stamp: DESIGNED    Source: [V10 §7K / HYBRID THEME SYSTEM]

ALONE
- What it is: DESIGNED — Open-vocabulary navigational themes that the engine may propose freely and only Ness may confirm. [V10 §7K / HYBRID THEME SYSTEM]
- Takes in: DESIGNED — One telling or patterns across tellings, retained roots and reading/telling references, theme proposals and Ness's theme actions. [V10 §7K / HYBRID THEME SYSTEM]
- Does: DESIGNED — Keeps engine proposals `proposed`, allows zero, one or many memberships per telling, and preserves unconfirmed proposals indefinitely. Confirmed themes remain navigation categories; future readings may challenge, omit or contradict them. [V10 §7K / HYBRID THEME SYSTEM]
- Gives out: DESIGNED — Proposed or confirmed themes with inspectable support, provenance and uncertainty. [V10 §7K / HYBRID THEME SYSTEM]
- Must never: DESIGNED — Turn a theme into fact, confirm by aging or repetition, accept circular support or let a proposed theme silently shape a later reading. [V10 §7K / HYBRID THEME SYSTEM]
- Fails closed by: DESIGNED — Leaves a proposed theme unconfirmed without Ness's confirmation; neither time nor repetition changes that state. [V10 §7K / HYBRID THEME SYSTEM]

TOGETHER
- Fed by: DESIGNED — C-7K — Story Layer (§7K): tellings organized by perspective and time. [V10 §7K]
- Fed by: ACCEPTED — C-7K.6.1 — Theme record: the stable theme record; C-7K.6.3 — Theme membership links: non-exclusive membership; C-7K.6.4 — Theme navigation grouping: navigational grouping; C-7K.6.5 — Theme alias record: two-way aliases; C-7K.6.6 — Theme action events: append-only theme actions; C-7K.6.7 — Theme retrieval-influence honesty: auditable retrieval influence. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Fed by: DESIGNED — C-7K.6.2 — Theme proposal support: each proposed theme's roots, telling/reading IDs, proposer, reason, time and uncertainty. [V10 §7K / HYBRID THEME SYSTEM]
- Gated by: DESIGNED — Ness's response is required for confirmation. [V10 §7K / HYBRID THEME SYSTEM]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7K — Story Layer (§7K) | Themes and their membership/support history. | Groups tellings for navigation while retaining proposal status and differing readings. | An open organization of tellings, never a settled account. | [V10 §7K] |
| 2 · ACCEPTED | C-7K.6.1 — Theme record | The identified theme and its actions. | Keeps stable identity, vocabulary, status, proposer, time and history together. | One preserved theme object. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 3 · DESIGNED | C-7K.6.2 — Theme proposal support | An engine-proposed theme and its supporting items. | Carries root and interpretation references with reason and uncertainty. | Inspectable proposal support. | [V10 §7K / HYBRID THEME SYSTEM] |
| 4 · ACCEPTED | C-7K.6.3 — Theme membership links | A theme and an eligible telling. | Permits a membership connection with its own provenance. | A non-exclusive organizational link. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7] |
| 5 · ACCEPTED | C-7K.6.4 — Theme navigation grouping | The member set and alias-linked family. | Retains root grounding while organizing navigation. | No self-validating theme. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 6 · ACCEPTED | C-7K.6.5 — Theme alias record | Labels connected across time. | Supplies both label ends for an alias record. | Earlier labels and links remain intact. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 7 · ACCEPTED | C-7K.6.6 — Theme action events | Ness's action on an identified theme. | Keeps the resulting event separate from the source theme and prior history. | Current state derives from preserved events. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 8 · ACCEPTED | C-7K.6.7 — Theme retrieval-influence honesty | A theme actually used in context retrieval. | Carries that influence into the retrieval audit trail. | No silent influence on future readings. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7] |
| 9 · ACCEPTED | C-AFFIRM.7.2 — Theme responses stay with theme actions | A theme response or change. | Supplies the existing theme system and its action atoms. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §17] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |

SUB-PARTS: C-7K.6.1 — Theme record; C-7K.6.2 — Theme proposal support; C-7K.6.3 — Theme membership links; C-7K.6.4 — Theme navigation grouping; C-7K.6.5 — Theme alias record; C-7K.6.6 — Theme action events; C-7K.6.7 — Theme retrieval-influence honesty

### C-7K.6.1 — Theme record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The stable theme object with append-only history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — `theme_id`, label, status, proposer provenance, creation timestamp and version history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Keeps one stable identifier and a Ness-controlled vocabulary label; derives current visible state from preserved events. Relabeling adds an alias instead of rewriting history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A theme record with its complete event history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Erase an earlier label or turn current navigation status into truth. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Keeps engine-proposed status unconfirmed until a recorded Ness confirmation event exists. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: DESIGNED — C-7K.6 — Hybrid theme system: the theme being recorded. [V10 §7K / HYBRID THEME SYSTEM]
- Fed by: ACCEPTED — C-7K.6.1.1 — theme_id: identifier; C-7K.6.1.2 — Theme label: label; C-7K.6.1.3 — Theme status: status; C-7K.6.1.4 — Theme proposer provenance: proposer; C-7K.6.1.5 — Theme creation timestamp: creation time; C-7K.6.1.6 — Theme version history: preserved versions. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gated by: ACCEPTED — C-7K.6.6.1 — confirm theme: a Ness confirmation event is the only route to confirmed status. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7K.6 — Hybrid theme system | The theme's stable record and event history. | Keeps themes addressable despite relabeling or regrouping. | Navigation with retained source identities. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-7K.6.1.1 — theme_id | The theme's stable identity. | Retains the identifier for membership and action references. | One continuing identity. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-7K.6.1.2 — Theme label | The current and earlier vocabulary labels. | Preserves each label across new alias or rename events. | Naming history without in-place edits. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-7K.6.1.3 — Theme status | The proposal and recorded confirmation history. | Carries proposed or confirmed status into the derived view. | Confirmation remains traceable to Ness. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 5 · ACCEPTED | C-7K.6.1.4 — Theme proposer provenance | The engine pass or Ness as proposer. | Retains the proposal's origin. | Inspectable provenance. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 6 · ACCEPTED | C-7K.6.1.5 — Theme creation timestamp | The theme creation occurrence. | Keeps its timestamp in the preserved record. | A dated theme without confirmation by aging. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 7 · ACCEPTED | C-7K.6.1.6 — Theme version history | The theme's append-only events. | Preserves versions as the current state changes. | Complete navigable history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 8 · ACCEPTED | C-7M.5.5.7 — Computed View theme references | Theme IDs with their proposed or confirmed status and source support. | Supplies stable theme records and version/status history. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 9 · ACCEPTED | C-7L.5.6 — Person-Box themes section | Linked themes with their proposed or confirmed status. | Supplies stable theme records and their status/version history. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §15] |

SUB-PARTS: C-7K.6.1.1 — theme_id; C-7K.6.1.2 — Theme label; C-7K.6.1.3 — Theme status; C-7K.6.1.4 — Theme proposer provenance; C-7K.6.1.5 — Theme creation timestamp; C-7K.6.1.6 — Theme version history

### C-7K.6.1.1 — theme_id
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The stable identifier of a theme. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The theme being identified. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Keeps membership and theme-action events linked to the same theme. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — The stable `theme_id`. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Replace a source theme's identity to hide its history during a merge or split. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7K.6.1 — Theme record: the identified theme. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7K.6.1 — Theme record | The stable theme identifier. | Retains the target of membership and action references. | Identity continuity across the theme history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-7K.6.1.2 — Theme label
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The human-readable label drawn from Ness's open vocabulary. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The label attached to this theme. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Retains the label while later rename events add a new label or alias. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A navigational label with older labels preserved. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Rename older tellings, links or theme history in place. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7K.6.1 — Theme record: the theme's current and earlier labels. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7K.6.1 — Theme record | The vocabulary label. | Names the navigational category without fixing a closed taxonomy. | A readable label, not an evidential classification. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-7K.6.1.3 — Theme status
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The theme's `proposed` or `confirmed` status. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Preserved proposal and theme-action events. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Derives confirmation only from a recorded Ness response; rejection is reflected in presentation without deleting the proposal or inventing another schema status. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — The supported derived status beside its event history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Derive confirmation from frequency, repetition or elapsed time. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Remains proposed in the absence of a Ness confirmation event. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-7K.6.1 — Theme record: the theme history; C-7K.6.1.3.1 — proposed: proposed state; C-7K.6.1.3.2 — confirmed: confirmed state. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gated by: ACCEPTED — C-7K.6.6.1 — confirm theme: only the recorded confirmation event changes the derived status to confirmed. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7K.6.1 — Theme record | The derived status. | Distinguishes a proposal from a confirmed navigational category. | Visible confirmation state, not truth status. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-7K.6.1.3.1 — proposed | A theme with no recorded confirmation. | Keeps it proposed, including when it remains unresolved indefinitely. | No hidden status transition. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-7K.6.1.3.2 — confirmed | A theme with its recorded Ness confirmation. | Makes its confirmed navigational status explicit. | No conversion to fact. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-7K.6.6.1 — confirm theme | The current proposal status and a confirmation response. | Reflects the recorded confirmation in the derived state. | The transition to confirmed, with prior history retained. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |

SUB-PARTS: C-7K.6.1.3.1 — proposed; C-7K.6.1.3.2 — confirmed

### C-7K.6.1.3.1 — proposed
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The unconfirmed state of an engine-proposed theme. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — An engine theme proposal and any later history that supplies no confirmation. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Permits the proposal to remain unresolved indefinitely. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — An inspectable proposed theme with its support and uncertainty. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Age a proposal into confirmation or remove it because it was rejected. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Retains the proposal without hidden confirmation or aging result. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-7K.6.1.3 — Theme status: the recorded theme status. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7K.6.1.3 — Theme status | An unconfirmed proposal. | Keeps proposed status explicit until the confirmation condition holds. | No silent status upgrade. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-7K.6.1.3.2 — confirmed
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The navigational status established by a Ness confirmation event. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The theme and its recorded Ness confirmation. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Shows confirmation in the derived current state while preserving all earlier events. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A confirmed navigation category. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Make confirmation a fact verdict or let it constrain future tellings to agree. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Does not establish confirmed status without the required Ness response event. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-7K.6.1.3 — Theme status: the derived theme status. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gated by: ACCEPTED — C-7K.6.6.1 — confirm theme: the confirmation event must exist. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7K.6.1.3 — Theme status | A recorded theme confirmation. | Represents its navigational state without changing source evidence. | Confirmed status with a preserved proposal/history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-7K.6.1.4 — Theme proposer provenance
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The provenance of the theme proposer. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The engine pass or Ness that proposed the theme. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records which origin produced the proposal. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Inspectable proposer provenance. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Treat repeated proposals from the same origin as confirmation. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7K.6.1 — Theme record: the proposal origin. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7K.6.1 — Theme record | The engine-pass or Ness provenance. | Preserves who or what proposed the theme. | An attributable proposal. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 2 · DESIGNED | C-7K.6.2 — Theme proposal support | The origin of the proposed theme. | Keeps the proposal attributable to its engine pass or Ness. | The same proposer provenance accompanies the support. | [V10 §7K / HYBRID THEME SYSTEM] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-7K.6.1.5 — Theme creation timestamp
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The theme's creation time. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The timestamp associated with theme creation. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Retains the original creation timestamp in the append-only history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — The recorded creation time. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Use age as an automatic confirmation rule. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7K.6.1 — Theme record: the theme creation occurrence. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7K.6.1 — Theme record | The creation timestamp. | Keeps the theme's temporal provenance. | Chronological history without authority by age. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 2 · DESIGNED | C-7K.6.2 — Theme proposal support | The timestamp recorded for the theme. | Keeps the proposal dated without creating an aging rule. | Temporal provenance on the supported proposal. | [V10 §7K / HYBRID THEME SYSTEM] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-7K.6.1.6 — Theme version history
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The append-only version history of a theme. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Creation, label/alias changes and separate theme-action events. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Preserves older versions and derives the current visible state from their history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A complete inspectable history beside the current navigation state. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Rewrite, erase or rename earlier versions in place. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7K.6.1 — Theme record: the theme's event history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7K.6.1 — Theme record | The preserved versions and events. | Retains changes without replacing older content. | History remains available after every theme action. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-7K.6.2 — Theme proposal support
Stamp: DESIGNED    Source: [V10 §7K / HYBRID THEME SYSTEM]

ALONE
- What it is: DESIGNED — The support and provenance recorded for every engine-proposed theme. [V10 §7K / HYBRID THEME SYSTEM]
- Takes in: DESIGNED — Supporting root IDs, supporting telling/reading IDs, proposer, connection reason, timestamp and uncertainty. [V10 §7K / HYBRID THEME SYSTEM]
- Does: DESIGNED — Keeps a single-telling or pattern-derived proposal inspectable and grounded in roots. [V10 §7K / HYBRID THEME SYSTEM]
- Gives out: DESIGNED — An explicitly proposed theme with its support chain. [V10 §7K / HYBRID THEME SYSTEM]
- Must never: DESIGNED — Let a pattern-derived theme validate itself or turn repeated proposal into confirmation. [V10 §7K / HYBRID THEME SYSTEM]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7K.6 — Hybrid theme system: the new proposed theme; C-7K.6.2.1 — Theme supporting root IDs: roots; C-7K.6.2.2 — Theme supporting telling and reading IDs: tellings/readings; C-7K.6.2.3 — Theme connection reason: connection reason; C-7K.6.2.4 — Theme proposal uncertainty: uncertainty. [V10 §7K / HYBRID THEME SYSTEM]
- Fed by: ACCEPTED — C-7K.6.1.4 — Theme proposer provenance: the theme proposer provenance; C-7K.6.1.5 — Theme creation timestamp: the theme creation timestamp. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7K.6 — Hybrid theme system | The proposal's evidence and provenance. | Retains why these items appear connected without establishing a fact. | A supported, uncertain navigational proposal. | [V10 §7K / HYBRID THEME SYSTEM] |
| 2 · DESIGNED | C-7K.6.2.1 — Theme supporting root IDs | Supporting root identifiers. | Retains the original evidence behind a proposed connection. | Root-grounded proposal support. | [V10 §7K / HYBRID THEME SYSTEM] |
| 3 · DESIGNED | C-7K.6.2.2 — Theme supporting telling and reading IDs | Supporting telling and reading references. | Preserves the exact interpretations motivating the theme. | Inspectable interpretation provenance. | [V10 §7K / HYBRID THEME SYSTEM] |
| 4 · DESIGNED | C-7K.6.2.3 — Theme connection reason | Why the supported items appear connected. | Keeps the apparent connection explicit beside its evidence. | A reason that remains a proposal. | [V10 §7K / HYBRID THEME SYSTEM] |
| 5 · DESIGNED | C-7K.6.2.4 — Theme proposal uncertainty | The proposal's recorded uncertainty. | Preserves the limitation on its grouping. | No silently settled theme. | [V10 §7K / HYBRID THEME SYSTEM] |

SUB-PARTS: C-7K.6.2.1 — Theme supporting root IDs; C-7K.6.2.2 — Theme supporting telling and reading IDs; C-7K.6.2.3 — Theme connection reason; C-7K.6.2.4 — Theme proposal uncertainty

### C-7K.6.2.1 — Theme supporting root IDs
Stamp: DESIGNED    Source: [V10 §7K / HYBRID THEME SYSTEM]

ALONE
- What it is: DESIGNED — The original roots supporting a proposed theme. [V10 §7K / HYBRID THEME SYSTEM]
- Takes in: DESIGNED — The supporting root identifiers. [V10 §7K / HYBRID THEME SYSTEM]
- Does: DESIGNED — Retains root support even when the proposal comes from patterns across tellings. [V10 §7K / HYBRID THEME SYSTEM]
- Gives out: DESIGNED — Direct root references on the proposal. [V10 §7K / HYBRID THEME SYSTEM]
- Must never: DESIGNED — Substitute circular theme support for the roots. [V10 §7K / HYBRID THEME SYSTEM]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7K.6.2 — Theme proposal support: the proposal's root support. [V10 §7K / HYBRID THEME SYSTEM]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7K.6.2 — Theme proposal support | The original root IDs. | Keeps the pattern proposal grounded beyond itself. | An inspectable support chain. | [V10 §7K / HYBRID THEME SYSTEM] |

SUB-PARTS: NONE

### C-7K.6.2.2 — Theme supporting telling and reading IDs
Stamp: DESIGNED    Source: [V10 §7K / HYBRID THEME SYSTEM]

ALONE
- What it is: DESIGNED — The telling/reading identifiers supporting the theme proposal. [V10 §7K / HYBRID THEME SYSTEM]
- Takes in: DESIGNED — The supporting telling and reading IDs. [V10 §7K / HYBRID THEME SYSTEM]
- Does: DESIGNED — Preserves the interpretation objects whose pattern or individual content motivated the proposal. [V10 §7K / HYBRID THEME SYSTEM]
- Gives out: DESIGNED — Traceable telling and reading references. [V10 §7K / HYBRID THEME SYSTEM]
- Must never: DESIGNED — Make repeated reference to one underlying telling into independent evidence. [V10 §7K / HYBRID THEME SYSTEM]
- Fails closed by: ACCEPTED — Does not use a partial or integrity-failed telling as theme support. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1]

TOGETHER
- Fed by: DESIGNED — C-7K.6.2 — Theme proposal support: the supporting interpretation references. [V10 §7K / HYBRID THEME SYSTEM]
- Gated by: ACCEPTED — C-READ.10.10 — Telling-set semantic eligibility: only eligible tellings may be used semantically. [V10 §7K / HYBRID THEME SYSTEM] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7K.6.2 — Theme proposal support | Supporting telling/reading references. | Keeps the proposal tied to the specific interpretations. | A navigable, non-circular support basis. | [V10 §7K / HYBRID THEME SYSTEM] |

SUB-PARTS: NONE

### C-7K.6.2.3 — Theme connection reason
Stamp: DESIGNED    Source: [V10 §7K / HYBRID THEME SYSTEM]

ALONE
- What it is: DESIGNED — Why the proposed theme's supporting items appear connected. [V10 §7K / HYBRID THEME SYSTEM]
- Takes in: DESIGNED — The source-grounded apparent connection. [V10 §7K / HYBRID THEME SYSTEM]
- Does: DESIGNED — Records the reason with the supporting references and uncertainty. [V10 §7K / HYBRID THEME SYSTEM]
- Gives out: DESIGNED — An inspectable proposal rationale. [V10 §7K / HYBRID THEME SYSTEM]
- Must never: DESIGNED — Invent connective tissue beyond the roots or treat the reason as established fact. [V10 §7K / HYBRID THEME SYSTEM]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7K.6.2 — Theme proposal support: the apparent connection being proposed. [V10 §7K / HYBRID THEME SYSTEM]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7K.6.2 — Theme proposal support | The stated connection reason. | Explains the proposal without hardening it into a conclusion. | Visible basis for the navigation grouping. | [V10 §7K / HYBRID THEME SYSTEM] |

SUB-PARTS: NONE

### C-7K.6.2.4 — Theme proposal uncertainty
Stamp: DESIGNED    Source: [V10 §7K / HYBRID THEME SYSTEM]

ALONE
- What it is: DESIGNED — The uncertainty recorded for a theme proposal. [V10 §7K / HYBRID THEME SYSTEM]
- Takes in: DESIGNED — The uncertainty attached to its apparent connection. [V10 §7K / HYBRID THEME SYSTEM]
- Does: DESIGNED — Keeps the proposal's limitation visible with its source basis. [V10 §7K / HYBRID THEME SYSTEM]
- Gives out: DESIGNED — Explicit uncertainty on the proposed theme. [V10 §7K / HYBRID THEME SYSTEM]
- Must never: DESIGNED — Silently remove uncertainty because the proposal is frequent or old. [V10 §7K / HYBRID THEME SYSTEM]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7K.6.2 — Theme proposal support: the proposal's uncertainty. [V10 §7K / HYBRID THEME SYSTEM]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7K.6.2 — Theme proposal support | The recorded uncertainty. | Keeps the connection provisional. | A proposal that does not imply a settled category. | [V10 §7K / HYBRID THEME SYSTEM] |

SUB-PARTS: NONE

### C-7K.6.3 — Theme membership links
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — Non-exclusive theme-to-telling links by stable `telling_id`. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7]
- Takes in: ACCEPTED — A theme, an eligible telling, what the link connects, why-by-pointer, who established/proposed it, certainty or uncertainty, and timestamp. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7]
- Does: ACCEPTED — Records each membership as an additive organizational assertion. One telling can belong to no theme, one or many; the original telling stays where it is. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7]
- Gives out: ACCEPTED — A first-class membership connection with provenance, never copied telling content. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7]
- Must never: ACCEPTED — Move or copy a telling into the theme, make grouping a fact, silently confirm a legacy_theme or force exclusive membership. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Keeps telling-level linking blocked while the complete valid set or legitimate zero-telling condition is absent. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1]

TOGETHER
- Fed by: DESIGNED — C-7K.6 — Hybrid theme system: the theme and membership being organized. [V10 §7K / HYBRID THEME SYSTEM]
- Fed by: ACCEPTED — C-READ.10.14.8 — Telling-to-theme reference: the existing telling-to-theme reference and its five provenance fields. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-READ.10.10 — Telling-set semantic eligibility: semantic eligibility before linking. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7K.6 — Hybrid theme system | Theme membership references with provenance. | Organizes tellings without relocating or upgrading them. | A non-exclusive navigational member set. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-7K.6.4 — Theme navigation grouping
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — A theme's member set and families formed through aliases. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Membership links and alias relationships retaining member tellings' root chains. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Builds navigation structures while keeping pattern-derived themes tied to roots. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Inspectable theme groups with their original support. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Let a theme validate itself through repeated proposals or circular membership. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Does not accept circular support as independent root grounding. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: DESIGNED — C-7K.6 — Hybrid theme system: the theme groups and their support chains. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gated by: ACCEPTED — C-READ.10.14.8.8 — Circular theme support prohibited: pattern-derived theme support must reach the roots rather than validate itself. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7K.6 — Hybrid theme system | Member sets and alias-linked theme families. | Exposes navigation without changing source truth or firmness. | Organized groups with circular support prohibited. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-7K.6.5 — Theme alias record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — A two-way reference connecting different theme labels across time. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The labels being connected and their preserved histories. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Adds the alias as a new record pointing both ways; older tellings and links retain their labels. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Navigable label continuity without an in-place rename. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Rewrite or delete an older label, telling or membership link. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7K.6 — Hybrid theme system: theme labels connected across time. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7K.6 — Hybrid theme system | Two labels and their alias relationship. | Connects names across time without replacing earlier names. | Navigation across preserved labels. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-7K.6.6 — Theme action events
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Separate append-only theme response/change events linked to stable `theme_id`s. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Ness's confirm, reject, rename, merge, split or leave-unresolved action. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Derives current visible state from the preserved event history. Theme actions belong to theme mechanics, separately from reading accept/reject events. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Recorded theme actions and an inspectable derived navigation state. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Delete source themes or history, treat time as an action, or collapse theme changes into reading affirmation. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — A proposed theme remains proposed indefinitely when no confirmation is recorded. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: DESIGNED — C-7K.6 — Hybrid theme system: the theme and Ness's response. [V10 §7K / HYBRID THEME SYSTEM]
- Fed by: ACCEPTED — C-7K.6.6.1 — confirm theme: confirm; C-7K.6.6.2 — reject theme: reject; C-7K.6.6.3 — rename theme: rename; C-7K.6.6.4 — merge themes: merge; C-7K.6.6.5 — split theme: split; C-7K.6.6.6 — leave theme unresolved: leave unresolved. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gated by: ACCEPTED — Ness's action supplies the theme response; confirmation cannot be inferred from silence. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7K.6 — Hybrid theme system | The separate action history. | Reflects responses in navigation while preserving all underlying records. | Current presentation and organization only. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-7K.6.6.1 — confirm theme | Ness's theme-confirmation response. | Appends the confirmation event to the identified theme. | Confirmed status with a complete history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-7K.6.6.2 — reject theme | Ness's theme rejection. | Records the rejection without deleting the target or links. | Rejection is reflected in presentation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-7K.6.6.3 — rename theme | A rename action with a new label or alias. | Adds naming history without overwriting older names. | A changed current navigation label. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 5 · ACCEPTED | C-7K.6.6.4 — merge themes | Source theme IDs and the resulting grouping. | Records their merge relationship without combining storage histories. | A navigational group with all constituents preserved. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 6 · ACCEPTED | C-7K.6.6.5 — split theme | The source theme, resulting IDs and membership changes. | Appends the split relationships beside the earlier grouping. | A new organization with the full old history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 7 · ACCEPTED | C-7K.6.6.6 — leave theme unresolved | A proposed theme left unresolved. | Keeps it pending without an automatic disposition. | No hidden change from time or repetition. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |

SUB-PARTS: C-7K.6.6.1 — confirm theme; C-7K.6.6.2 — reject theme; C-7K.6.6.3 — rename theme; C-7K.6.6.4 — merge themes; C-7K.6.6.5 — split theme; C-7K.6.6.6 — leave theme unresolved

### C-7K.6.6.1 — confirm theme
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The sole transition that makes a theme's derived status `confirmed`. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Ness's confirmation response and the stable theme reference. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records a separate confirmation event; current visible state reflects that event. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Confirmed navigation status with the earlier proposal and support preserved. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Substitute repetition, frequency, elapsed time or silence for Ness's response. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Leaves confirmation absent until its required response event exists. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-7K.6.6 — Theme action events: the confirmation response. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gated by: ACCEPTED — Ness must explicitly confirm the theme. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Changes: ACCEPTED — C-7K.6.1.3 — Theme status: establishes confirmed derived status. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7K.6.6 — Theme action events | A Ness confirmation of a specific theme. | Adds its event to the preserved history. | The only recorded route to confirmation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-7K.6.1 — Theme record | The recorded confirmation event. | Supports the theme's confirmed state. | No unrecorded confirmation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-7K.6.1.3 — Theme status | The confirmation event. | Derives confirmed status from that response. | Navigation status only. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-7K.6.1.3.2 — confirmed | The recorded response authorizing confirmation. | Keeps the confirmed state traceable to Ness. | No confirmation by age or repetition. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 5 · DESIGNED | C-7M.4.3.4 — Computed View theme-confirmation trigger | The confirmed theme and its confirmation event. | Supplies Ness's recorded theme confirmation. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [V10 §7M / UPDATE TIMING] |

SUB-PARTS: NONE

### C-7K.6.6.2 — reject theme
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — A recorded Ness rejection of a proposed theme. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The rejection response and theme reference. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Adds the rejection event and reflects it in derived presentation. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Visible rejection with theme, membership links and history intact. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Delete the rejected proposal or any supporting membership link. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7K.6.6 — Theme action events: the rejection response. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gated by: ACCEPTED — Ness's rejection is required for this response event. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7K.6.6 — Theme action events | A rejection of the proposal. | Preserves it as an event without erasing its target. | The presentation reflects rejection. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-7K.6.6.3 — rename theme
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — A new label or alias recorded through a theme action. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Ness's rename action and new label or alias. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Appends the new naming event and preserves every older label. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A changed current label with a complete navigable naming history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Rename the stored source records or their old labels in place. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7K.6.6 — Theme action events: the requested name change. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gated by: ACCEPTED — Ness's rename action supplies the new label or alias. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7K.6.6 — Theme action events | The new label or alias. | Adds it through an event, preserving older names. | Current navigation naming only. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-7K.6.6.4 — merge themes
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — A recorded relationship between source themes and a resulting navigation grouping. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The source `theme_id`s and the requested resulting grouping. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Adds the merge relationship while retaining every constituent theme, old membership link and full history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — A current navigation grouping whose source themes remain separately inspectable. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Delete, copy or rewrite source themes or older membership links during merging. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7K.6.6 — Theme action events: the theme-merge action. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gated by: ACCEPTED — Ness's merge action supplies the requested grouping. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7K.6.6 — Theme action events | Source theme identifiers and the resulting group. | Records their relationship without merging their storage histories. | A navigational merge with all sources preserved. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-7K.6.6.5 — split theme
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — New events recording a source theme's split and membership changes. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The source theme, resulting `theme_id`s and changed membership links. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Records the new grouping and links without erasing the earlier grouping or its full history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Resulting navigational themes with a traceable split history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Rewrite the earlier grouping or drop its old memberships from history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7K.6.6 — Theme action events: the requested split and its resulting relationships. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gated by: ACCEPTED — Ness's split action supplies the requested separation. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7K.6.6 — Theme action events | The split source, results and membership changes. | Appends the changes as separate events. | Current navigation changes while the old grouping remains inspectable. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-7K.6.6.6 — leave theme unresolved
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — A theme remaining proposed without automatic disposition. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — The proposed theme left unresolved. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Keeps it proposed indefinitely without an automatic confirmation, rejection, aging result or hidden change. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — The preserved unresolved proposal. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Make elapsed time, silence or repetition decide its disposition. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Retains unresolved proposed status. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-7K.6.6 — Theme action events: the unchanged unresolved proposal. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7K.6.6 — Theme action events | An unresolved proposed theme. | Keeps its history and proposed status without a hidden state change. | No automatic disposition. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-7K.6.7 — Theme retrieval-influence honesty
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The audit-trail requirement when a proposed or confirmed theme influences later context retrieval. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7]
- Takes in: ACCEPTED — The actual theme use and the context admitted for a future pass. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7]
- Does: ACCEPTED — Records the influence in retrieval provenance, including the why-admitted basis. Future readings remain free to challenge, omit or contradict the theme. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7]
- Gives out: ACCEPTED — An inspectable account of the theme's actual influence. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7]
- Must never: ACCEPTED — Let a theme silently shape future readings or use its confirmation as a truth constraint. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7K.6 — Hybrid theme system: the theme used in a later pass. [V10 §7K / HYBRID THEME SYSTEM]
- Fed by: ACCEPTED — C-READ.10.14.8.9 — Retrieval influence is recorded: the existing telling-link retrieval-influence rule. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-7F — Context Retrieval (§7F): any actual theme admission into context retains the retrieval audit-trail influence; this honesty rule chooses no retrieval-influence policy. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7K.6 — Hybrid theme system | Actual theme influence on later context. | Preserves its provenance without requiring later readings to agree. | Transparent influence, no new retrieval permission. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 2 · DESIGNED | C-7F — Context Retrieval (§7F) | A theme used in a context-retrieval operation. | Records its actual influence and why the context was admitted. | An honest retrieval audit trail. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-7K.7 — Holding through separate linked objects
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — Person-related understanding held through the existing Story Layer and Person-Box objects. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — Original roots, readings, perspective-owned tellings, Ness-response events, clashes, themes, unresolved identity anchors and merge proposals. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Keeps these objects linked and separate. Ness's understanding remains visibly distinct from the original evidence and from other people's perspectives. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — Preserved understanding with its source and perspective differences visible. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Make Holding a separate profile, summary, fact-box, second memory store or replacement memory; turn repetition, recency or strongly held understanding into settled fact about the person. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7K — Story Layer (§7K): perspective-owned tellings within the linked understanding. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-7L — Person-Boxes (§7L): person-related links preserve separate evidence and perspectives without a new profile. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7K — Story Layer (§7K) | The linked understanding and its source objects. | Preserves Ness's perspective separately from evidence and other perspectives. | Held understanding without a single synthesized fact. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] |
| 2 · DESIGNED | C-7L — Person-Boxes (§7L) | Separate related objects and perspective-owned tellings. | Holds them by links within the existing architecture. | No profile or second memory store. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] |
| 3 · ACCEPTED | C-7L.7 — Person-Box Holding through linked objects | Original roots, readings, perspective-owned tellings, Ness response events, clashes, themes, unresolved identity anchors and merge proposals. | Supplies the accepted shared Holding boundary and separate-object structure. | Nothing in this card. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7K.8 — Story-Layer operation records
Stamp: DESIGNED    Source: [V10 §0B] [MAP C-7K] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]

ALONE
- What it is: DESIGNED — The permanent connected records of real Story Layer operations. [V10 §0B] [MAP C-7K] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Takes in: DESIGNED — Every telling received, theme proposed, Ness theme action, firmness assignment with basis, membership link, alias, and actual retrieval influence. [V10 §0B] [MAP C-7K] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Does: DESIGNED — Records each real operation once, append-only, under privacy/access and applicable identity/security authorization. A log records an occurrence and is part of living memory; it does not create another automatic log about itself or another vote for the source. [V10 §0B] [MAP C-7K] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Gives out: DESIGNED — Retrievable history of organization, response and influence. [V10 §0B] [MAP C-7K] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Must never: DESIGNED — Operate silently, rewrite history, leak protected material or let use/log repetition add certainty. [V10 §0B] [MAP C-7K] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Fails closed by: DESIGNED — Blocks unauthorized use of protected records; permanent preservation does not grant ordinary runtime access. [V10 §0B] [MAP C-7K] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]

TOGETHER
- Fed by: DESIGNED — C-7K — Story Layer (§7K): the real operation and its outcome. [V10 §0B] [MAP C-7K] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): purpose-specific authorization, protected-boundary, TSC and influence-removal restrictions also govern logs; C-SACL — Speaker Access-Control Layer (§25.4): applicable identity/access authorization before use or surfacing. [V10 §0B] [MAP C-7K] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7K — Story Layer (§7K) | A real Story Layer operation. | Retains one connected record with its actual basis and result. | Permanent operational history without extra truth weight. | [V10 §0B] [MAP C-7K] |

SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece USED BY continuations

These rows add the reciprocal USED BY entries to the named external cards at assembly. They preserve the delivered cards; every row names both ends. The relationship wording is carried from the current TOGETHER field.

| Current card | Field | External card receiving USED BY row | Stamp | Relationship and condition | Source |
|---|---|---|---|---|---|
| C-7K — Story Layer (§7K) | Fed by | C-READ — Reading record, validator, writer (§6B) | BUILT | C-READ — Reading record, validator, writer (§6B): embedded tellings and the immutable reading/root references. | [V10 §6B] [V10 §7K] |
| C-7K — Story Layer (§7K) | Fed by | C-READ.10.14 — Telling-reference handoff | ACCEPTED | C-READ.10.14 — Telling-reference handoff: complete integrity-valid first-class telling cards and stable reference chains. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [NHD-A2] |
| C-7K — Story Layer (§7K) | Fed by | C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | DESIGNED | C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K): story-bearing pass output; C-ENGINE-C.11 — Theme proposal boundary: proposed themes with support and uncertainty. | [V10 §7K] [MAP C-7K] |
| C-7K — Story Layer (§7K) | Fed by | C-ENGINE-C.11 — Theme proposal boundary | DESIGNED | C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K): story-bearing pass output; C-ENGINE-C.11 — Theme proposal boundary: proposed themes with support and uncertainty. | [V10 §7K] [MAP C-7K] |
| C-7K — Story Layer (§7K) | Fed by | C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B) | DESIGNED | C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B): the perspective dimension within its CY-A pass; C-7B.3 — Story-Layer Web: human perspectives preserved as separate tellings; C-7B.3.1 — Per-person perspective: the human perspective being represented; C-7B.3.2 — N.H is not a teller: the engine view kept separately as a weightless NOTE; C-7B.3.4 — Clash preservation: disagreeing tellings with clash preserved. | [MAP C-7B] [MAP CY-A] [V10 §7K] |
| C-7K — Story Layer (§7K) | Fed by | C-7B.3 — Story-Layer Web | DESIGNED | C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B): the perspective dimension within its CY-A pass; C-7B.3 — Story-Layer Web: human perspectives preserved as separate tellings; C-7B.3.1 — Per-person perspective: the human perspective being represented; C-7B.3.2 — N.H is not a teller: the engine view kept separately as a weightless NOTE; C-7B.3.4 — Clash preservation: disagreeing tellings with clash preserved. | [MAP C-7B] [MAP CY-A] [V10 §7K] |
| C-7K — Story Layer (§7K) | Fed by | C-7B.3.1 — Per-person perspective | DESIGNED | C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B): the perspective dimension within its CY-A pass; C-7B.3 — Story-Layer Web: human perspectives preserved as separate tellings; C-7B.3.1 — Per-person perspective: the human perspective being represented; C-7B.3.2 — N.H is not a teller: the engine view kept separately as a weightless NOTE; C-7B.3.4 — Clash preservation: disagreeing tellings with clash preserved. | [MAP C-7B] [MAP CY-A] [V10 §7K] |
| C-7K — Story Layer (§7K) | Fed by | C-7B.3.2 — N.H is not a teller | DESIGNED | C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B): the perspective dimension within its CY-A pass; C-7B.3 — Story-Layer Web: human perspectives preserved as separate tellings; C-7B.3.1 — Per-person perspective: the human perspective being represented; C-7B.3.2 — N.H is not a teller: the engine view kept separately as a weightless NOTE; C-7B.3.4 — Clash preservation: disagreeing tellings with clash preserved. | [MAP C-7B] [MAP CY-A] [V10 §7K] |
| C-7K — Story Layer (§7K) | Fed by | C-7B.3.4 — Clash preservation | DESIGNED | C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B): the perspective dimension within its CY-A pass; C-7B.3 — Story-Layer Web: human perspectives preserved as separate tellings; C-7B.3.1 — Per-person perspective: the human perspective being represented; C-7B.3.2 — N.H is not a teller: the engine view kept separately as a weightless NOTE; C-7B.3.4 — Clash preservation: disagreeing tellings with clash preserved. | [MAP C-7B] [MAP CY-A] [V10 §7K] |
| C-7K — Story Layer (§7K) | Fed by | C-7B.3.3 — Firmness reading | DESIGNED | C-7B.3.3 — Firmness reading: provisional evidence-based firmness; C-7B.3.3.1 — Evidence basis: observable signals; C-7B.3.3.2 — Separate model confidence: firmness separate from confidence; C-7B.3.3.3 — Direct certainty evidence: stronger direct self-report; C-7B.3.3.4 — Attribution strength: weaker reported or uncertain attribution; C-7B.3.3.5 — Conflicting firmness signals: conflicting signals without forced resolution; C-7B.3.3.6 — Unsupported firmness omission: unsupported firmness omitted. | [V10 §7K / FIRMNESS RULE] [MAP C-7B] |
| C-7K — Story Layer (§7K) | Fed by | C-7B.3.3.1 — Evidence basis | DESIGNED | C-7B.3.3 — Firmness reading: provisional evidence-based firmness; C-7B.3.3.1 — Evidence basis: observable signals; C-7B.3.3.2 — Separate model confidence: firmness separate from confidence; C-7B.3.3.3 — Direct certainty evidence: stronger direct self-report; C-7B.3.3.4 — Attribution strength: weaker reported or uncertain attribution; C-7B.3.3.5 — Conflicting firmness signals: conflicting signals without forced resolution; C-7B.3.3.6 — Unsupported firmness omission: unsupported firmness omitted. | [V10 §7K / FIRMNESS RULE] [MAP C-7B] |
| C-7K — Story Layer (§7K) | Fed by | C-7B.3.3.2 — Separate model confidence | DESIGNED | C-7B.3.3 — Firmness reading: provisional evidence-based firmness; C-7B.3.3.1 — Evidence basis: observable signals; C-7B.3.3.2 — Separate model confidence: firmness separate from confidence; C-7B.3.3.3 — Direct certainty evidence: stronger direct self-report; C-7B.3.3.4 — Attribution strength: weaker reported or uncertain attribution; C-7B.3.3.5 — Conflicting firmness signals: conflicting signals without forced resolution; C-7B.3.3.6 — Unsupported firmness omission: unsupported firmness omitted. | [V10 §7K / FIRMNESS RULE] [MAP C-7B] |
| C-7K — Story Layer (§7K) | Fed by | C-7B.3.3.3 — Direct certainty evidence | DESIGNED | C-7B.3.3 — Firmness reading: provisional evidence-based firmness; C-7B.3.3.1 — Evidence basis: observable signals; C-7B.3.3.2 — Separate model confidence: firmness separate from confidence; C-7B.3.3.3 — Direct certainty evidence: stronger direct self-report; C-7B.3.3.4 — Attribution strength: weaker reported or uncertain attribution; C-7B.3.3.5 — Conflicting firmness signals: conflicting signals without forced resolution; C-7B.3.3.6 — Unsupported firmness omission: unsupported firmness omitted. | [V10 §7K / FIRMNESS RULE] [MAP C-7B] |
| C-7K — Story Layer (§7K) | Fed by | C-7B.3.3.4 — Attribution strength | DESIGNED | C-7B.3.3 — Firmness reading: provisional evidence-based firmness; C-7B.3.3.1 — Evidence basis: observable signals; C-7B.3.3.2 — Separate model confidence: firmness separate from confidence; C-7B.3.3.3 — Direct certainty evidence: stronger direct self-report; C-7B.3.3.4 — Attribution strength: weaker reported or uncertain attribution; C-7B.3.3.5 — Conflicting firmness signals: conflicting signals without forced resolution; C-7B.3.3.6 — Unsupported firmness omission: unsupported firmness omitted. | [V10 §7K / FIRMNESS RULE] [MAP C-7B] |
| C-7K — Story Layer (§7K) | Fed by | C-7B.3.3.5 — Conflicting firmness signals | DESIGNED | C-7B.3.3 — Firmness reading: provisional evidence-based firmness; C-7B.3.3.1 — Evidence basis: observable signals; C-7B.3.3.2 — Separate model confidence: firmness separate from confidence; C-7B.3.3.3 — Direct certainty evidence: stronger direct self-report; C-7B.3.3.4 — Attribution strength: weaker reported or uncertain attribution; C-7B.3.3.5 — Conflicting firmness signals: conflicting signals without forced resolution; C-7B.3.3.6 — Unsupported firmness omission: unsupported firmness omitted. | [V10 §7K / FIRMNESS RULE] [MAP C-7B] |
| C-7K — Story Layer (§7K) | Fed by | C-7B.3.3.6 — Unsupported firmness omission | DESIGNED | C-7B.3.3 — Firmness reading: provisional evidence-based firmness; C-7B.3.3.1 — Evidence basis: observable signals; C-7B.3.3.2 — Separate model confidence: firmness separate from confidence; C-7B.3.3.3 — Direct certainty evidence: stronger direct self-report; C-7B.3.3.4 — Attribution strength: weaker reported or uncertain attribution; C-7B.3.3.5 — Conflicting firmness signals: conflicting signals without forced resolution; C-7B.3.3.6 — Unsupported firmness omission: unsupported firmness omitted. | [V10 §7K / FIRMNESS RULE] [MAP C-7B] |
| C-7K — Story Layer (§7K) | Gated by | C-READ.10.10 — Telling-set semantic eligibility | ACCEPTED | C-READ.10.10 — Telling-set semantic eligibility: complete-set semantic eligibility must hold before telling-specific organization. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1] |
| C-7K — Story Layer (§7K) | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): authorize the actual internal or visible purpose before use; no link or secondary index bypasses protection. | [V10 §7Q / TWO-STAGE OUTPUT ACCESS CONTROL] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §9] |
| C-7K — Story Layer (§7K) | Gated by | C-7A — Universal Filter (§7A) | DESIGNED | C-7A — Universal Filter (§7A): per-person perspectives and clashes remain separate; C-7A.8 — R5.5 — Per-person STORY-layer: the system's own view stays a weightless NOTE. | [V10 §7A] [V10 §7K] |
| C-7K — Story Layer (§7K) | Gated by | C-7A.8 — R5.5 — Per-person STORY-layer | DESIGNED | C-7A — Universal Filter (§7A): per-person perspectives and clashes remain separate; C-7A.8 — R5.5 — Per-person STORY-layer: the system's own view stays a weightless NOTE. | [V10 §7A] [V10 §7K] |
| C-7K — Story Layer (§7K) | Gated by | C-7B.9.11 — Forbidden Wonder evidence uses | ACCEPTED | C-7B.9.11 — Forbidden Wonder evidence uses: accepted Wonder material stays possibility material and cannot enter anyone's story as observed reality. | [04/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md §7] |
| C-7K — Story Layer (§7K) | Changes | C-7L — Person-Boxes (§7L) | DESIGNED | C-7L — Person-Boxes (§7L): supplies linked tellings in each perspective role; C-7M — Computed View (§7M): supplies source tellings for current presentation; C-7D — Living State Web (§7D): supplies source objects with root support, no added evidential weight. | [V10 §7K] [MAP C-7K] |
| C-7K — Story Layer (§7K) | Changes | C-7M — Computed View (§7M) | DESIGNED | C-7L — Person-Boxes (§7L): supplies linked tellings in each perspective role; C-7M — Computed View (§7M): supplies source tellings for current presentation; C-7D — Living State Web (§7D): supplies source objects with root support, no added evidential weight. | [V10 §7K] [MAP C-7K] |
| C-7K — Story Layer (§7K) | Changes | C-7D — Living State Web (§7D) | DESIGNED | C-7L — Person-Boxes (§7L): supplies linked tellings in each perspective role; C-7M — Computed View (§7M): supplies source tellings for current presentation; C-7D — Living State Web (§7D): supplies source objects with root support, no added evidential weight. | [V10 §7K] [MAP C-7K] |
| C-7K.2 — Explicit connections across time | Gated by | C-READ.10.10 — Telling-set semantic eligibility | ACCEPTED | C-READ.10.10 — Telling-set semantic eligibility: the complete valid telling-set condition applies before semantic linking. | [V10 §7K / CONNECTIONS ACROSS TIME] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8] |
| C-7K.3 — Structured perspective in organization | Fed by | C-READ.10.1.4 — root_speaker | ACCEPTED | C-READ.10.1.4 — root_speaker: source speaker; C-READ.10.1.5 — subject: subject; C-READ.10.1.6 — perspective_owner: perspective owner; C-READ.10.1.7 — attribution_path: optional attribution chain; C-READ.10.1.8 — evidence_relationship: evidence relationship. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3] |
| C-7K.3 — Structured perspective in organization | Fed by | C-READ.10.1.5 — subject | ACCEPTED | C-READ.10.1.4 — root_speaker: source speaker; C-READ.10.1.5 — subject: subject; C-READ.10.1.6 — perspective_owner: perspective owner; C-READ.10.1.7 — attribution_path: optional attribution chain; C-READ.10.1.8 — evidence_relationship: evidence relationship. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3] |
| C-7K.3 — Structured perspective in organization | Fed by | C-READ.10.1.6 — perspective_owner | ACCEPTED | C-READ.10.1.4 — root_speaker: source speaker; C-READ.10.1.5 — subject: subject; C-READ.10.1.6 — perspective_owner: perspective owner; C-READ.10.1.7 — attribution_path: optional attribution chain; C-READ.10.1.8 — evidence_relationship: evidence relationship. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3] |
| C-7K.3 — Structured perspective in organization | Fed by | C-READ.10.1.7 — attribution_path | ACCEPTED | C-READ.10.1.4 — root_speaker: source speaker; C-READ.10.1.5 — subject: subject; C-READ.10.1.6 — perspective_owner: perspective owner; C-READ.10.1.7 — attribution_path: optional attribution chain; C-READ.10.1.8 — evidence_relationship: evidence relationship. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3] |
| C-7K.3 — Structured perspective in organization | Fed by | C-READ.10.1.8 — evidence_relationship | ACCEPTED | C-READ.10.1.4 — root_speaker: source speaker; C-READ.10.1.5 — subject: subject; C-READ.10.1.6 — perspective_owner: perspective owner; C-READ.10.1.7 — attribution_path: optional attribution chain; C-READ.10.1.8 — evidence_relationship: evidence relationship. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §3] |
| C-7K.4 — First-class telling ownership and reference boundary | Fed by | C-READ.10.14.1 — Story Layer holds cards | ACCEPTED | C-READ.10.14.1 — Story Layer holds cards: the accepted Story Layer ownership handoff; C-READ.10.15 — New telling identities on reread: new telling identities on reread. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8] |
| C-7K.4 — First-class telling ownership and reference boundary | Fed by | C-READ.10.15 — New telling identities on reread | ACCEPTED | C-READ.10.14.1 — Story Layer holds cards: the accepted Story Layer ownership handoff; C-READ.10.15 — New telling identities on reread: new telling identities on reread. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8] |
| C-7K.4 — First-class telling ownership and reference boundary | Gated by | C-READ.10.10 — Telling-set semantic eligibility | ACCEPTED | C-READ.10.10 — Telling-set semantic eligibility: all expected cards/events and valid completion proof, or legitimate zero telling, before semantic use. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §8] [NHD-A2] |
| C-7K.5 — Qualitative firmness in the Story Layer | Fed by | C-READ.10.1.11 — firmness | ACCEPTED | C-READ.10.1.11 — firmness: the existing firmness field and its atomic label rules; C-READ.10.1.12 — firmness_evidence_basis: the existing evidence-basis field and qualitative hierarchy. | [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §2] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §3] |
| C-7K.5 — Qualitative firmness in the Story Layer | Fed by | C-READ.10.1.12 — firmness_evidence_basis | ACCEPTED | C-READ.10.1.11 — firmness: the existing firmness field and its atomic label rules; C-READ.10.1.12 — firmness_evidence_basis: the existing evidence-basis field and qualitative hierarchy. | [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §2] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §3] |
| C-7K.5 — Qualitative firmness in the Story Layer | Gated by | C-READ.10.1.11.7 — Never force a firmness level | ACCEPTED | C-READ.10.1.11.7 — Never force a firmness level: the never-force rule requires the less-claiming supported outcome; C-READ.10.1.12 — firmness_evidence_basis: every non-omitted assignment requires source-grounded basis. | [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §1] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §2] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §3] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §4] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §5] |
| C-7K.5 — Qualitative firmness in the Story Layer | Gated by | C-READ.10.1.12 — firmness_evidence_basis | ACCEPTED | C-READ.10.1.11.7 — Never force a firmness level: the never-force rule requires the less-claiming supported outcome; C-READ.10.1.12 — firmness_evidence_basis: every non-omitted assignment requires source-grounded basis. | [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §1] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §2] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §3] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §4] [04/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md §5] |
| C-7K.6.2.2 — Theme supporting telling and reading IDs | Gated by | C-READ.10.10 — Telling-set semantic eligibility | ACCEPTED | C-READ.10.10 — Telling-set semantic eligibility: only eligible tellings may be used semantically. | [V10 §7K / HYBRID THEME SYSTEM] |
| C-7K.6.3 — Theme membership links | Fed by | C-READ.10.14.8 — Telling-to-theme reference | ACCEPTED | C-READ.10.14.8 — Telling-to-theme reference: the existing telling-to-theme reference and its five provenance fields. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7] |
| C-7K.6.3 — Theme membership links | Gated by | C-READ.10.10 — Telling-set semantic eligibility | ACCEPTED | C-READ.10.10 — Telling-set semantic eligibility: semantic eligibility before linking. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7] |
| C-7K.6.4 — Theme navigation grouping | Gated by | C-READ.10.14.8.8 — Circular theme support prohibited | ACCEPTED | C-READ.10.14.8.8 — Circular theme support prohibited: pattern-derived theme support must reach the roots rather than validate itself. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| C-7K.6.7 — Theme retrieval-influence honesty | Fed by | C-READ.10.14.8.9 — Retrieval influence is recorded | ACCEPTED | C-READ.10.14.8.9 — Retrieval influence is recorded: the existing telling-link retrieval-influence rule. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7] |
| C-7K.6.7 — Theme retrieval-influence honesty | Changes | C-7F — Context Retrieval (§7F) | DESIGNED | C-7F — Context Retrieval (§7F): any actual theme admission into context retains the retrieval audit-trail influence; this honesty rule chooses no retrieval-influence policy. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7] |
| C-7K.7 — Holding through separate linked objects | Changes | C-7L — Person-Boxes (§7L) | DESIGNED | C-7L — Person-Boxes (§7L): person-related links preserve separate evidence and perspectives without a new profile. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] |
| C-7K.8 — Story-Layer operation records | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): purpose-specific authorization, protected-boundary, TSC and influence-removal restrictions also govern logs; C-SACL — Speaker Access-Control Layer (§25.4): applicable identity/access authorization before use or surfacing. | [V10 §0B] [MAP C-7K] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19] |
| C-7K.8 — Story-Layer operation records | Gated by | C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): purpose-specific authorization, protected-boundary, TSC and influence-removal restrictions also govern logs; C-SACL — Speaker Access-Control Layer (§25.4): applicable identity/access authorization before use or surfacing. | [V10 §0B] [MAP C-7K] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19] |

## Cross-piece TOGETHER continuations for incoming uses

These are the reciprocal uses represented in the current USED BY tables. Their external owners retain their full mechanisms in their assigned pieces.

| Current card supplying use | External using card | Takes in there | Does there | Changes there | Stamp | Source |
|---|---|---|---|---|---|---|
| C-7K — Story Layer (§7K) | C-7L — Person-Boxes (§7L) | Tellings and their perspective/root provenance. | Links the tellings without making a profile or replacing a source. | Organized references in the person's view. | DESIGNED | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [MAP C-7K] |
| C-7K — Story Layer (§7K) | C-7M — Computed View (§7M) | Preserved telling references. | Uses them as source objects while keeping conflicting tellings distinct. | The current picture, not the source history. | DESIGNED | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [MAP C-7K] |
| C-7K — Story Layer (§7K) | C-7D — Living State Web (§7D) | Tellings with direct roots and their inspectable source chain. | Retains their perspective, firmness limits and grounding. | Eligible state source references, not extra evidence weight. | DESIGNED | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [MAP C-7K] |
| C-7K — Story Layer (§7K) | C-ENGINE-C.11 — Theme proposal boundary | The hybrid-theme rules and organized tellings. | Allows proposed themes with roots, telling/reading IDs, proposer, reason, time and uncertainty; only Ness can confirm. | A proposal in the Story Layer without a silent influence on future readings. | DESIGNED | [V10 §7K / HYBRID THEME SYSTEM] |
| C-7K — Story Layer (§7K) | C-LMAC — Live Mechanism Access Coordinator (§26) | An authorized story-layer query. | Returns perspective-owned tellings with clashes preserved and the component's provenance. | The requesting function receives the permitted live result. | DESIGNED | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| C-7K.6.7 — Theme retrieval-influence honesty | C-7F — Context Retrieval (§7F) | A theme used in a context-retrieval operation. | Records its actual influence and why the context was admitted. | An honest retrieval audit trail. | DESIGNED | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| C-7K.7 — Holding through separate linked objects | C-7L — Person-Boxes (§7L) | Separate related objects and perspective-owned tellings. | Holds them by links within the existing architecture. | No profile or second memory store. | DESIGNED | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] |

## Scope, paths and source dispositions

The Story Layer participates in CY-A through the existing C-7B perspective dimension and story-engine interface. Existing C-7B and C-READ uses are reciprocated explicitly; the C-ENGINE-C.11 proposal uses are represented in the root USED BY table. No new story-production pipeline or runtime authorization is inferred.

The telling record and its atomic fields retain the C-READ.10.1 family. The six firmness outcomes, never-force rule, no-numeric rule, revision, repetition and evidence-basis atoms retain C-READ.10.1.11 and C-READ.10.1.12 with their existing children. C-7K.5 writes the complete policy at its Story Layer use, without creating duplicate label-card identities. Telling correspondence, preparation, commits, zero-telling, recovery and semantic eligibility retain the C-READ.10.3–C-READ.10.10 owners. Theme-link provenance and restrictions retain C-READ.10.14.8; new theme records and action events are placed here.

Source discovery searched all pinned permitted accepted/active files by C-7K, Story Layer, telling, theme and firmness. Direct scope is V10 §7K, accepted A2, firmness policy, Bundle 3 §11 and its cross-cutting §§18–20, Bundle 6 policy §4 A3.5, the Bundle 6 §12 query boundary, and A17 §7's possibility boundary. The accepted receipts establish status even though candidate headers remain frozen. The A17 receipt records acceptance of the policy; its own independent receipt-audit condition is not treated as observed PASS.

A1 gold content and benchmark dependencies remain with the existing C-GOLD and C-ENGINE-C cards. A31/B24 validation, B9/B10 reread and B11 storage results retain CH05-a/d and CH03-a ownership. Bundle 2 relevance consumers remain CH06-d/f and CH08-b; the inherited B26 foundation source-scope gap persists. A7/B7/AIC protection and authority remain CH08-a/CH07-c and later security owners. Bundle 6 policy replaces the earlier A3.5 open-question description only within its accepted scope; exact Holding layout remains open. The working A3 record and decision indices are navigation, not additional authority. No content is taken from the recovery ledger or excluded history.

The old open-slot wording does not deny the accepted standalone telling identity, qualitative firmness and theme design. No numeric threshold, runtime mechanism or source-conflict resolution is invented. Theme influence policy and serialization remain open despite the settled audit-trail requirement. Person-Box, view/state and privacy consumers retain their named later ownership; reading affirmation is CH08-f and does not own theme actions.

## Source-to-card coverage added by CH06-b

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

## Additional undecided implementation slots

| Owner | Slot | State |
|---|---|---|
| C-7K — Story Layer (§7K) | Full Story Layer storage/runtime schema beyond the accepted telling and theme design | NOT DECIDED |
| C-7K.2 — Explicit connections across time | Exact serialization and implementation of cross-time navigation links | NOT DECIDED |
| C-7K.3 — Structured perspective in organization | Production migration/materialization choice for legacy v1 entries beyond the accepted first-class telling contract; no migration is authorized by that contract | NOT DECIDED |
| C-7K.5 — Qualitative firmness in the Story Layer | Explicit omitted_no_support token representation on other surfaces whose schemas have not chosen it | NOT DECIDED |
| C-7K.6.1 — Theme record | Theme-record serialization, storage engine and crash/partial-write mechanics | NOT DECIDED |
| C-7K.6.4 — Theme navigation grouping | Concrete similarity-grouping algorithm beyond navigation-only and no-circularity boundaries | NOT DECIDED |
| C-7K.6.6 — Theme action events | Theme-event wire schemas, operation identity and recovery beyond separate append-only events and preserved histories | NOT DECIDED |
| C-7K.6.7 — Theme retrieval-influence honesty | Whether and how themes are admitted to retrieval; honesty of an actual influence does not choose this policy | NOT DECIDED |
| C-7K.7 — Holding through separate linked objects | Exact Holding record/link layout beyond separate existing objects and preserved perspectives | NOT DECIDED |
| C-7K.8 — Story-Layer operation records | Operation-record serialization and storage-failure handling beyond one-record/no-double-evidence rules | NOT DECIDED |

## Appendix A carry-forward — this piece

| Card | Empty field | Occurrence within field | State |
|---|---|---|---|
| C-7K.1 — Telling and ongoing story | Fails closed by | 1 | NOT DECIDED |
| C-7K.1 — Telling and ongoing story | Gated by | 1 | NOT DECIDED |
| C-7K.1 — Telling and ongoing story | Changes | 1 | NOT DECIDED |
| C-7K.2 — Explicit connections across time | Changes | 1 | NOT DECIDED |
| C-7K.3 — Structured perspective in organization | Gated by | 1 | NOT DECIDED |
| C-7K.3 — Structured perspective in organization | Changes | 1 | NOT DECIDED |
| C-7K.4 — First-class telling ownership and reference boundary | Changes | 1 | NOT DECIDED |
| C-7K.5 — Qualitative firmness in the Story Layer | Changes | 1 | NOT DECIDED |
| C-7K.6 — Hybrid theme system | Changes | 1 | NOT DECIDED |
| C-7K.6.1 — Theme record | Changes | 1 | NOT DECIDED |
| C-7K.6.1.1 — theme_id | Fails closed by | 1 | NOT DECIDED |
| C-7K.6.1.1 — theme_id | Gated by | 1 | NOT DECIDED |
| C-7K.6.1.1 — theme_id | Changes | 1 | NOT DECIDED |
| C-7K.6.1.2 — Theme label | Fails closed by | 1 | NOT DECIDED |
| C-7K.6.1.2 — Theme label | Gated by | 1 | NOT DECIDED |
| C-7K.6.1.2 — Theme label | Changes | 1 | NOT DECIDED |
| C-7K.6.1.3 — Theme status | Changes | 1 | NOT DECIDED |
| C-7K.6.1.3.1 — proposed | Gated by | 1 | NOT DECIDED |
| C-7K.6.1.3.1 — proposed | Changes | 1 | NOT DECIDED |
| C-7K.6.1.3.2 — confirmed | Changes | 1 | NOT DECIDED |
| C-7K.6.1.4 — Theme proposer provenance | Fails closed by | 1 | NOT DECIDED |
| C-7K.6.1.4 — Theme proposer provenance | Gated by | 1 | NOT DECIDED |
| C-7K.6.1.4 — Theme proposer provenance | Changes | 1 | NOT DECIDED |
| C-7K.6.1.5 — Theme creation timestamp | Fails closed by | 1 | NOT DECIDED |
| C-7K.6.1.5 — Theme creation timestamp | Gated by | 1 | NOT DECIDED |
| C-7K.6.1.5 — Theme creation timestamp | Changes | 1 | NOT DECIDED |
| C-7K.6.1.6 — Theme version history | Fails closed by | 1 | NOT DECIDED |
| C-7K.6.1.6 — Theme version history | Gated by | 1 | NOT DECIDED |
| C-7K.6.1.6 — Theme version history | Changes | 1 | NOT DECIDED |
| C-7K.6.2 — Theme proposal support | Fails closed by | 1 | NOT DECIDED |
| C-7K.6.2 — Theme proposal support | Gated by | 1 | NOT DECIDED |
| C-7K.6.2 — Theme proposal support | Changes | 1 | NOT DECIDED |
| C-7K.6.2.1 — Theme supporting root IDs | Fails closed by | 1 | NOT DECIDED |
| C-7K.6.2.1 — Theme supporting root IDs | Gated by | 1 | NOT DECIDED |
| C-7K.6.2.1 — Theme supporting root IDs | Changes | 1 | NOT DECIDED |
| C-7K.6.2.2 — Theme supporting telling and reading IDs | Changes | 1 | NOT DECIDED |
| C-7K.6.2.3 — Theme connection reason | Fails closed by | 1 | NOT DECIDED |
| C-7K.6.2.3 — Theme connection reason | Gated by | 1 | NOT DECIDED |
| C-7K.6.2.3 — Theme connection reason | Changes | 1 | NOT DECIDED |
| C-7K.6.2.4 — Theme proposal uncertainty | Fails closed by | 1 | NOT DECIDED |
| C-7K.6.2.4 — Theme proposal uncertainty | Gated by | 1 | NOT DECIDED |
| C-7K.6.2.4 — Theme proposal uncertainty | Changes | 1 | NOT DECIDED |
| C-7K.6.3 — Theme membership links | Changes | 1 | NOT DECIDED |
| C-7K.6.4 — Theme navigation grouping | Changes | 1 | NOT DECIDED |
| C-7K.6.5 — Theme alias record | Fails closed by | 1 | NOT DECIDED |
| C-7K.6.5 — Theme alias record | Gated by | 1 | NOT DECIDED |
| C-7K.6.5 — Theme alias record | Changes | 1 | NOT DECIDED |
| C-7K.6.6 — Theme action events | Changes | 1 | NOT DECIDED |
| C-7K.6.6.2 — reject theme | Fails closed by | 1 | NOT DECIDED |
| C-7K.6.6.2 — reject theme | Changes | 1 | NOT DECIDED |
| C-7K.6.6.3 — rename theme | Fails closed by | 1 | NOT DECIDED |
| C-7K.6.6.3 — rename theme | Changes | 1 | NOT DECIDED |
| C-7K.6.6.4 — merge themes | Fails closed by | 1 | NOT DECIDED |
| C-7K.6.6.4 — merge themes | Changes | 1 | NOT DECIDED |
| C-7K.6.6.5 — split theme | Fails closed by | 1 | NOT DECIDED |
| C-7K.6.6.5 — split theme | Changes | 1 | NOT DECIDED |
| C-7K.6.6.6 — leave theme unresolved | Gated by | 1 | NOT DECIDED |
| C-7K.6.6.6 — leave theme unresolved | Changes | 1 | NOT DECIDED |
| C-7K.6.7 — Theme retrieval-influence honesty | Fails closed by | 1 | NOT DECIDED |
| C-7K.6.7 — Theme retrieval-influence honesty | Gated by | 1 | NOT DECIDED |
| C-7K.7 — Holding through separate linked objects | Fails closed by | 1 | NOT DECIDED |
| C-7K.7 — Holding through separate linked objects | Gated by | 1 | NOT DECIDED |
| C-7K.8 — Story-Layer operation records | Changes | 1 | NOT DECIDED |

## Plain-gate and empty-box review

All current fields and USED BY rows were reviewed for misplaced restrictions, failure outcomes and preconditions. The complete-telling gate's blocked-use result appears on the organization, navigation, identity and semantic-support interfaces. Required attribution remains unresolved when unsupported; absence of firmness remains genuine omission. Theme statuses never acquire a numeric threshold or automatic approval mechanism. Human theme actions remain plain preconditions; no automatic refusal code is invented. Theme proposer and timestamp use their existing theme-record identities instead of duplicated proposal-field cards. Each step/action is connected to its rule owner. Earlier shared cards remain immutable even where the audit findings recorded in the manifest require later correction.

| Card | Plain gate justification |
|---|---|
| C-7K.6 — Hybrid theme system | Ness's response, a human act, is required for confirmation; it is not an automated threshold. |
| C-7K.6.6 — Theme action events | The theme response is Ness's act; no consent is inferred from silence. |
| C-7K.6.6.1 — confirm theme | Explicit Ness confirmation is the source-defined human condition. |
| C-7K.6.6.2 — reject theme | The rejection event records Ness's rejection, not a machine verdict. |
| C-7K.6.6.3 — rename theme | The source action is Ness's requested rename; no extra approval stage is added. |
| C-7K.6.6.4 — merge themes | The source action is Ness's requested theme grouping; the original records remain separate. |
| C-7K.6.6.5 — split theme | The source action is Ness's requested split; no automatic split criterion is invented. |

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

## READ RECORD

All current behavior sources remain pinned to 6a7160ba688ba4e433a31899162815df7e2bab17. Whole-file credit below names only files read in full for this piece. Scoped reopens retain earlier cumulative whole-read credits without creating new ones. Contract §§5–11 and the governing lessons were reopened before writing; §11.3 is reopened after writing. Source lookup by name, part ID and topic precedes the source map; other owners in shared packages remain explicitly outside this piece.

| Source file | Reading scope / whole-file credit | SHA-256 |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: complete §7K; previously read §§0B/7Q and source-defined existing story/pass interfaces reused. | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped: complete C-7K; C-7B/CY-A and Group D interface checks. | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Scoped: SMART machinery and §3G/3H Story Layer status; no additional mechanism derived. | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Scoped: complete §7K for authority comparison. | `cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md` | Whole: all 388 lines including label criteria, evidence, separation, omission, revision and remaining scope. | `f0ee0b07871373eb8dda0c83ab7186a51de35fe7ad0c5299bc41ae00078811b5` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: exact accepted identity, accepted scope and preserved open dependencies. | `88ef2b372ca99fe60b69a6a8891f6956ff6126ee634249bfb86f2f48839ccffa` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md` | Scoped: §§6–9 in full; §3 and §5A existing field/semantic-gate contracts reused with prior atomic owners. | `f91da6426817031cf2c0b14fb467a3e1d97d2ea3c67d27a07d8b1831f9895a55` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md` | Scoped reopen: complete §11 and cross-cutting §§18–21; whole-file credit retained from CH06-a. | `3566cf0f917fb4f7eb329d9089f6e238fe4afbacbae2c73c8b2716e3397e7c2e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Prior whole-file credit retained from CH06-a; accepted source identity reused. | `405717e5528df74b9842dee6da8b3de69b82a738e478d06c2e1025243ae56a16` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Scoped: complete A3.5 in §4; other policy subparts retain their owners. | `b37f965a343dbf86130f96591d58de9288ad0a746a68e8ae8fdd7b66208a63da` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: policy package identity and acceptance; no broad Bundle 6 completion inferred from this scoped receipt. | `4b37668ea3a95463e49bc27ada107be78cd807e3cbf8455a06b912901b4346f6` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped: full §12 query boundary read in CH06-a and reused; full LMAC remains CH08-c. | `bc1095955525fcea56cb4d16057c93bfb15eec42a83a1b644baf0e87a473f64e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md` | Scoped: §§2–7, especially complete §7 story/person/world possibility boundary; no full-file credit. | `1a4d8b9a24f15ce371dd49b28bde7bf9888e0fe114ec4bdab6e6446af495bf8d` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: policy acceptance established; receipt's own independent-audit condition retained as unobserved. | `fe3986416c560d49879d252f21e1c64d0fa3e0b3061d6c8e44d34ab45dba49df` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_CANDIDATE_v1_4.md` | Scoped: firmness accepted-source identity and package-status navigation only. | `5ebddb536201e8d39794297088752ba4c2925a1be706ff29c55e1a45b42ea6fa` |
| `05_ACTIVE_CANDIDATE/02-NH_BUNDLE_6_A3_DECISIONS_WORKING_RECORD_v1-1-.md` | Scoped: A3.5/Holding navigation; accepted policy supplies behavior. | `1bbf4af0f6437255113c7efd32b8c57718a37a8ae379350327463a72e451922f` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Scoped: Story Layer/firmness/theme navigation and dependency ownership; no behavior from the index. | `aad8d1aeee9a331ad6f4d9ddbcfa9c42eae2a94e1ef1bccde7484079181ff7b4` |

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

Round 4A later changed Chapters 0, 1, 2, 3-a to 3-d and 6-a to 6-g; the identities above are those preserved when this chapter was written, and the round 4A identities are listed in the round 4A delivery manifest.

### READ-folder files not yet read whole

68 inherited pending files remain. Scoped reading receives no new whole-file credit.

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
§1.3 no history/actions/roles/workflow in this chapter: PASS — 34 behavior cards reviewed; 0 workflow/advice hits. Delivery metadata remains outside behavior.
§1.4 every gap written as NOT DECIDED: PASS — 63 empty fields match 63 register rows; 10 additional mechanical slots are explicit.
§1.5 conflicts marked, none resolved: PASS — no new source-conflict rule found in the current scope. The accepted A2, firmness and theme designs fill scoped open slots; remaining implementation is not silently closed. Earlier conflicts and the B26 source-scope gap remain in the manifest.
§3 exactly one stamp per line: PASS — 34 headers, 262 populated fields and 91 USED BY rows checked. 1 BUILT field lines name only the existing built reading-record source; no new machinery is stamped BUILT.
§4 every behavior line cited in the exact format: PASS — 41 distinct citations; 41 resolve within the named pinned sections. Populated fields and use rows are cited; the source-to-claim review accompanies mechanical resolution.
§5.4 one name per thing: PASS — 34 unique current IDs without prior collisions; 528 named-card mentions checked. Shared atoms retain their established IDs and names.
§6 all template fields present, in order, for every part: PASS — 34 templates and 325 field lines checked.
§6.3 reciprocity within this chapter: PASS — 72 internal relationship occurrences checked; 46 outgoing and 7 incoming continuation rows name both ends. No missing reciprocal; prior files remain unchanged.
§6.4 every decided detail written in, no citation used in place of content: PASS — 18 source-to-card rows reviewed; 38 expected source-name literals present. Existing atomic owners and remaining scopes are explicit.
§6.5 sub-parts recursed to the bottom: PASS — theme-record fields, proposal-support fields, both derived status states and all six theme actions have templates; existing perspective/firmness/theme-link atoms retain their shared owners. Navigation, identity, Holding, logging and influence boundaries are explicit. 0 current cards have all three TOGETHER fields empty.
§9 coverage matrix rows added for every file used: PASS — all 145 pinned READ-folder file paths remain in the carried inventory; current additions and 17 current READ RECORD fingerprints are present. Shared-package coverage remains partial where stated.
§10.11 no recommendation, no sentence addressed to Ness: PASS — all 34 behavior cards reviewed; no recommendation or addressed instruction.
Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`.

### Computed self-check results

Writer checks and the accompanying manual source/box review returned no unresolved current-file errors. They are not an independent audit or adoption. Plain human/precondition gates are justified in the inventory above.

| Check | Count |
|---|---|
| cards | 34 |
| field_lines | 325 |
| used_by_rows | 91 |
| empty_fields | 63 |
| internal_relationships | 72 |
| external_relationships | 46 |
| distinct_citations | 41 |
| resolved_citations | 41 |
| empty_together_cards | 0 |
| plain_together_lines | 7 |
| formula_hits | 0 |
| wording_hits | 0 |
| errors | 0 |
| named_card_mentions_checked | 528 |
| misfiled_box_fields_scanned | 325 |
| restriction_failure_gate_slots_reviewed | 105 |
| registered_empty_fields | 63 |
| cross_piece_continuations_checked | 46 |
| covered_read_file_paths | 145 |
| read_fingerprints_checked | 17 |
| source_names_checked | 38 |
| source_names_missing | 0 |
| built_field_lines | 1 |
| behavior_workflow_hits | 0 |
| plain_gates_justified | 7 |
| outgoing_continuations | 46 |
| incoming_continuations | 7 |
| registered_fields | 63 |
| additional_gaps | 10 |
| pending_source_paths | 68 |
| source_map_rows | 18 |
| read_record_rows | 17 |

The delivery recount compares these metrics with the finished file.
