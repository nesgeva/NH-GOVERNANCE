# Chapter 6-d — Group D: C-7M

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH06-d.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`  

This piece covers Computed View's internal-use boundary, fixed seven-factor ordering, versioned profiles, immutable snapshots, refresh/status records, triggered updates and recovery, its proposed relevance declaration, Bundle 4 operational-record lifecycle, held metadata and provisional-creation influence. Existing telling, clash, Log and provisional-use atoms retain their delivered IDs. Full Current/History presentation remains CH06-e, Living State and world-model structures CH06-f, Connection Capability CH06-g, action mechanisms CH07-a/b, authority CH07-c, privacy/relevance/LMAC CH08-a/b/c and speaker-access mechanics CH09-d; side paths remain CH11.

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; NHD identifiers locate decisions in the pinned index and do not replace behavior citations.

<!-- BEGIN BEHAVIOR -->

### C-7M — Computed View (§7M)
Stamp: DESIGNED    Source: [V10 §7M] [MAP C-7M]

ALONE
- What it is: DESIGNED — The internal present-facing assembly of what N.H currently has reason to use, with alternatives and history preserved. [V10 §7M] [MAP C-7M]
- Takes in: DESIGNED — Permitted roots, readings, tellings, clashes, Ness response events, Person-Box links, themes, Living State and world-model references, and safe metadata-only pre-ingest references; the declared profile/purpose and its authorized trigger. [V10 §7M] [MAP C-7M]
- Does: DESIGNED — Assembles a navigable current picture using disclosed derivation rules. Distinguishes source evidence, engine interpretation, Ness's explicit judgment and unresolved material. Uses the fixed seven-factor order, explains item priority and preserves previous pictures without declaring a winning truth. [V10 §7M] [MAP C-7M]
- Gives out: DESIGNED — A current internal picture and preserved immutable snapshots; the honest outcome no clear current view when support is too weak or conflicted. [V10 §7M] [MAP C-7M]
- Must never: DESIGNED — Rewrite, alter, merge or delete source objects; silently select an authoritative reading; equate frequency or recency with reliability; present inference as settled fact; turn Ness's response into a historical rewrite; suppress conflicts; store new interpretations; decide truth; volunteer the internal picture unprompted. [V10 §7M] [MAP C-7M]
- Fails closed by: ACCEPTED — A missing, invalid, stale or unauthorized profile/declaration produces failed or incomplete refresh status and no snapshot. Failed updates retain the last valid snapshot through later possibly-stale status; no half-built or falsely fresh picture becomes visible. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: BUILT — C-STORE — Accretive store & sealed roots (§6B): immutable direct roots; C-READ — Reading record, validator, writer (§6B): immutable reading records and their root links. [V10 §6A] [V10 §6B]
- Fed by: DESIGNED — C-7K — Story Layer (§7K): perspective-owned tellings; C-7J — Clash Handling (§7J): preserved clashes; C-7J.6 — Ness response as separate event: separate Ness responses; C-7L — Person-Boxes (§7L): person-linked source objects; C-7D — Living State Web (§7D): grounded state and world-model source references, strictly upstream; C-7E.11 — Held-content access boundary: safe held metadata, lifecycle state and blockers; C-7GA.11.7.2 — Step 7B — Process triggered view profiles: triggered internal profile-update requests in CY-A. [MAP C-7M] [V10 §7M] [V10 §7G-A]
- Fed by: ACCEPTED — C-READ.10.14 — Telling-reference handoff: eligible first-class telling references; C-7J.7 — Downstream effects of clashes: conflicted evidence and downstream display limits; C-7L.4 — Ness's confirmed Person-Box: Ness's confirmed person anchor; C-CREATE.8.5 — Provisional influence in Computed View: relevant marked provisional influence within its accepted boundary. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fed by: DESIGNED — C-7M.2 — Computed View seven-factor priority order: the seven factors; C-7M.4 — Computed View update triggers: the three trigger routes. [V10 §7M]
- Fed by: ACCEPTED — C-7M.3 — Computed View ordering-profile record: exact versioned ordering profile; C-7M.5 — Computed View immutable snapshot record: immutable snapshot; C-7M.6 — Computed View refresh-status event: append-only refresh/status event; C-7M.7 — Computed View refresh lifecycle: refresh outcomes; C-7M.8 — Computed View duplicate prevention: duplicate prevention; C-7M.9 — Computed View operation and recovery contract: recovery and operation identity; C-7M.10 — Computed View proposed RM-CV-01 declaration: proposed relevance declaration; C-7M.11 — Computed View operational records and lifecycle: operational record and lifecycle; C-7M.12 — Computed View provisional-creation influence: provisional-status carriage; C-7M.13 — Computed View metadata-only held-content boundary: the held-metadata boundary. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: DESIGNED — C-7M.1 — Computed View internal-use boundary: quiet internal use does not permit unprompted display; C-7A — Universal Filter (§7A): preserve the history of meaning; C-7A.9.3 — Current-use separation: current use never rewrites HISTORY; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): purpose-specific privacy authorization precedes assembly and relevance; C-7R — Attention & Relevance Control (§7R): run only the valid declaration for the purpose; C-7P — Permission & Authority Boundaries (§7P): authority governs action-adjacent uses and operational writes; C-SACL — Speaker Access-Control Layer (§25.4): applicable visible output passes speaker access after privacy. [V10 §7A] [V10 §7M] [V10 §7Q] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5]
- Gated by: ACCEPTED — C-READ.10.10 — Telling-set semantic eligibility: complete-set semantic eligibility must hold before telling-specific view use. [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1]
- Changes: DESIGNED — C-7N — Action Surfacing (§7N): supplies the internal current picture for possible-action surfacing under its own rules; C-7I — View Layer (§7I): supplies disclosed best-supported ordering when a view makes that claim. [V10 §7M] [MAP C-7M]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7GA.11.7.2 — Step 7B — Process triggered view profiles, in CY-A | The triggered profile-update operation and its result. | Requests and tracks each profile update under its operation key. | A checkpointed internal view-update result. | [V10 §7G-A] |
| 2 · ACCEPTED | C-CREATE.8.5 — Provisional influence in Computed View | The current-picture influence boundary. | Carries relevant provisional material with its status and operation record. | No provisional fragment becomes settled through use. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] |
| 3 · DESIGNED | C-7J — Clash Handling (§7J) | The current-use handling of clash-bearing material. | Keeps clashes and responses separate while informing current presentation. | Presentation only, no source mutation. | [V10 §7J] [V10 §7M] |
| 4 · DESIGNED | C-7J.6 — Ness response as separate event | The view's explicit-judgment input. | Allows a response to affect current use without rewriting the clash. | A presentation consequence, not a truth verdict. | [V10 §7J] [V10 §7M] |
| 5 · ACCEPTED | C-7J.7 — Downstream effects of clashes | Current presentation of conflicted support. | Keeps clashes beside items and permits no clear current view. | No forced winner. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] |
| 6 · DESIGNED | C-7K — Story Layer (§7K) | The preserved source-telling interface. | Supplies tellings to the current picture without merging perspectives. | Current navigation, not new story authority. | [V10 §7K] [V10 §7M] |
| 7 · DESIGNED | C-7L — Person-Boxes (§7L) | The person-focused current-picture interface. | Uses linked source objects under the view's derivation rules. | An inspectable current picture without changing the Person-Box. | [V10 §7L] [V10 §7M] |
| 8 · ACCEPTED | C-7L.4 — Ness's confirmed Person-Box | The person-focused assembly rules. | Supplies Ness's anchor without creating a self-profile. | Permitted source links in the current picture. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] |
| 9 · ACCEPTED | C-7L.5 — Seven-section Person-Box view | The seven-factor best-supported ordering. | Delegates a best-supported claim to that ordering. | No recency-only reliability claim. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] |
| 10 · DESIGNED | C-7N — Action Surfacing (§7N) | The current internal picture. | Uses it under its own evidence and authority rules. | Possible-action support, not action permission. | [MAP C-7M] |
| 11 · DESIGNED | C-7I — View Layer (§7I) | Explicit best-supported ordering. | Uses it when making a best-supported presentation claim. | Disclosed current-use presentation. | [MAP C-7I] [V10 §7M] |
| 12 · ACCEPTED | C-7M.6 — Computed View refresh-status event | The current-picture assembly's source-preservation and internal-use boundary. | Supplies refresh status without changing source objects or snapshots. | An honest current picture with intact evidence and history. | [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 13 · ACCEPTED | C-7M.7 — Computed View refresh lifecycle | The current-picture assembly's source-preservation and internal-use boundary. | Supplies the standing-view lifecycle. | An honest current picture with intact evidence and history. | [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 14 · ACCEPTED | C-7M.8 — Computed View duplicate prevention | The current-picture assembly's source-preservation and internal-use boundary. | Prevents repeated attempts from duplicating a picture. | An honest current picture with intact evidence and history. | [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 15 · ACCEPTED | C-7M.9 — Computed View operation and recovery contract | The current-picture assembly's source-preservation and internal-use boundary. | Supplies honest recovery without rewriting a picture. | An honest current picture with intact evidence and history. | [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 16 · ACCEPTED | C-7M.10 — Computed View proposed RM-CV-01 declaration | The current-picture assembly's source-preservation and internal-use boundary. | Supplies the declared relevance contribution to current assembly. | An honest current picture with intact evidence and history. | [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 17 · ACCEPTED | C-7M.11 — Computed View operational records and lifecycle | The current-picture assembly's source-preservation and internal-use boundary. | Keeps view operations inspectable without making their logs evidence. | An honest current picture with intact evidence and history. | [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 18 · ACCEPTED | C-7M.12 — Computed View provisional-creation influence | The current-picture assembly's source-preservation and internal-use boundary. | Supplies permitted provisional influence without making it settled. | An honest current picture with intact evidence and history. | [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 19 · ACCEPTED | C-7M.13 — Computed View metadata-only held-content boundary | The current-picture assembly's source-preservation and internal-use boundary. | Confines held-material assembly to safe metadata. | An honest current picture with intact evidence and history. | [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| 20 · DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A); P-MAIN step 15 | Each triggered view profile after clash detection. | After clash detection completes, process each triggered view profile under internal-use authorization and relevance rules; recover or record its snapshot or no-update result, then account for all triggered profiles. | The view snapshots and no-update results. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 21 · DESIGNED | C-7D — Living State Web (§7D) | Permitted readings, tellings, clashes, Ness-response events and result evidence with root provenance. | Takes this place's change: supplies state/world sources for its seven-factor current picture. | Supplies state/world sources for its seven-factor current picture. | [V10 §7D] [MAP C-7D] [V10 §7O] |
| 22 · DESIGNED | C-AFFIRM — Off-board Affirmation Feedback Seam (§11 item 23) | Ness’s accept/reject response to one or more specific readings through the view/chat surface. | Takes this place's change: may use dismissal to stop resurfacing through current-use rules. | May use dismissal to stop resurfacing through current-use rules. | [V10 §11] [V10 §0] [MAP C-AFFIRM] |
| 23 · ACCEPTED | C-7I.1.4 — Current best-supported delegation | The actual claim being made and Computed View's separate seven-factor results. | Supplies the derived current picture and honest support limitations. | Nothing in this card. | [V10 §7M] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] |
| 24 · DESIGNED | C-19 — Interface / Ness's World (§19) | Eligible views, what the system has reason to show, deliberate commands and verified world-entry confirmation. | Supplies what N.H has reason to show. | Nothing in this card. | [MAP C-19] |
| 25 · ACCEPTED | C-7Q.11.7 — Meaning, derived-store and simulation privacy interface | Authorized inputs, explicit influence-removal scope, third-party separation and any simulation approval. | Takes this place's change: computed View assembly. | Computed View assembly. | [04/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md §16] |
| 26 · DESIGNED | C-OOP.6.1 — Improvement reading before behavioral change | The actual automatically proposed improvement from outcome evidence. | Supplies normal proposal surfacing. | Nothing in this card. | [V10 §26.6] |
| 27 · ACCEPTED | C-AFFIRM.5.1 — Dismissal stops repeated resurfacing | The actual reading dismissal and any valid new trigger. | Gates this place: owns current-use selection and applicable valid triggers. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §17] |
| 28 · ACCEPTED | C-7N.9 — Action-surfacing evidence handoff | Permitted source evidence and the current picture, retaining their different roles. | Supplies downstream current picture. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] |

SUB-PARTS: C-7M.1 — Computed View internal-use boundary; C-7M.2 — Computed View seven-factor priority order; C-7M.3 — Computed View ordering-profile record; C-7M.4 — Computed View update triggers; C-7M.5 — Computed View immutable snapshot record; C-7M.6 — Computed View refresh-status event; C-7M.7 — Computed View refresh lifecycle; C-7M.8 — Computed View duplicate prevention; C-7M.9 — Computed View operation and recovery contract; C-7M.10 — Computed View proposed RM-CV-01 declaration; C-7M.11 — Computed View operational records and lifecycle; C-7M.12 — Computed View provisional-creation influence; C-7M.13 — Computed View metadata-only held-content boundary

### C-7M.1 — Computed View internal-use boundary
Stamp: DESIGNED    Source: [V10 §7M / INTERNAL TOOL ONLY] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: DESIGNED — The distinction between silent internal use and deliberate inspection of the Computed View. [V10 §7M / INTERNAL TOOL ONLY] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: DESIGNED — An authorized internal purpose or Ness's deliberate request to look at the view. [V10 §7M / INTERNAL TOOL ONLY] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Uses the view silently to inform responses. Quiet internal use needs no per-use Ness approval. Makes the view available for inspection only when Ness deliberately asks; a downstream visible result carries materially relevant uncertainty under its own surface rules. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: DESIGNED — Internal response support or explicitly requested inspection. [V10 §7M / INTERNAL TOOL ONLY] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: DESIGNED — Volunteer the whole internal picture, narrate internal knowledge back unprompted or show a summary/profile merely because it exists. [V10 §7M / INTERNAL TOOL ONLY] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: DESIGNED — Without a deliberate inspection request, the view itself remains internal. [V10 §7M / INTERNAL TOOL ONLY] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — Ness's deliberate request is required for inspection of the view itself; it is not required for authorized quiet internal use. [V10 §7M / INTERNAL TOOL ONLY] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M — Computed View (§7M) | The internal-use versus inspection distinction. | Keeps current-picture assembly silent unless inspection is requested. | No unprompted view disclosure. | [V10 §7M] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 2 · ACCEPTED | C-7M.3.9.4 — Computed View profile surfacing rules | The deliberate-request boundary for inspecting the view itself. | The view itself is shown only on Ness's deliberate request. | No unprompted whole-picture display. | [V10 §7M] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-7M.10.9.3 — Computed View relevance surfacing boundary | The deliberate-request boundary for inspecting the view itself. | The existing internal-use/requested-inspection boundary governs view display. | No unprompted whole-picture display. | [V10 §7M] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 4 · DESIGNED | C-7M.4.1 — Computed View opened trigger | Ness's deliberate opening/request for inspection. | Permits the opening trigger within the requested view scope. | No volunteered internal picture. | [V10 §7M] |
| 5 · DESIGNED | C-LEARN.9.3 — No silent behavioral authority or unprompted personal view | A proposed behavioral rule, major learning-period change, wellbeing result or personal Computed View. | Supplies canonical internal-use boundary. | Nothing in this card. | [V10 §26.12] |

SUB-PARTS: NONE

### C-7M.2 — Computed View seven-factor priority order
Stamp: DESIGNED    Source: [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]

ALONE
- What it is: DESIGNED — The fixed explicit ordering of seven distinct considerations, without a hidden truth score. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Takes in: DESIGNED — Ness's current judgment; direct root support; reading acceptance/grounding; relevance to purpose; context quality/provenance; clashes/uncertainty/contrary evidence; recency. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Does: DESIGNED — Applies those factors in that order and states why every surfaced item was prioritized. Direct root support outranks repetition, frequency and model confidence. Carries a clash beside even a strongly supported item; permits no clear current view when support is too weak or conflicted. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Gives out: DESIGNED — Explained current-use priority with alternatives and uncertainty accessible. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Must never: DESIGNED — Collapse evidence, interpretation, judgment and uncertainty into one number; silently reorder factors; treat priority as authoritative truth or recency as more than a limited tie-breaker. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Fails closed by: DESIGNED — Does not force a winner when no clear current view is supportable. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]

TOGETHER
- Fed by: DESIGNED — C-7M.2.1 — Computed View factor 1 — current Ness judgment: current judgment; C-7M.2.2 — Computed View factor 2 — direct root evidence: direct root evidence; C-7M.2.3 — Computed View factor 3 — reading acceptance and grounding: reading status/grounding; C-7M.2.4 — Computed View factor 4 — purpose relevance: purpose relevance; C-7M.2.5 — Computed View factor 5 — context quality and provenance: context/provenance; C-7M.2.6 — Computed View factor 6 — clashes and uncertainty: clashes/uncertainty; C-7M.2.7 — Computed View factor 7 — recency tie-breaker: recency tie-breaker. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M — Computed View (§7M) | The fixed factor order and separate outcomes. | Assembles an explained current picture. | Current-use priority without a truth score. | [V10 §7M] |
| 2 · DESIGNED | C-7M.2.1 — Computed View factor 1 — current Ness judgment | The fixed order and separation of the seven factors. | Supplies the relevant current-judgment factor. | One separately recorded contribution to current ordering. | [V10 §7M] [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] |
| 3 · DESIGNED | C-7M.2.2 — Computed View factor 2 — direct root evidence | The fixed order and separation of the seven factors. | Supplies the direct-evidence factor. | One separately recorded contribution to current ordering. | [V10 §7M] [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] |
| 4 · DESIGNED | C-7M.2.3 — Computed View factor 3 — reading acceptance and grounding | The fixed order and separation of the seven factors. | Supplies reading-status and grounding priority. | One separately recorded contribution to current ordering. | [V10 §7M] [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] |
| 5 · DESIGNED | C-7M.2.4 — Computed View factor 4 — purpose relevance | The fixed order and separation of the seven factors. | Supplies relevance only to factor 4. | One separately recorded contribution to current ordering. | [V10 §7M] [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [V10 §7R] |
| 6 · DESIGNED | C-7M.2.5 — Computed View factor 5 — context quality and provenance | The fixed order and separation of the seven factors. | Supplies the context-quality factor. | One separately recorded contribution to current ordering. | [V10 §7M] [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] |
| 7 · DESIGNED | C-7M.2.6 — Computed View factor 6 — clashes and uncertainty | The fixed order and separation of the seven factors. | Supplies the conflict and uncertainty factor. | One separately recorded contribution to current ordering. | [V10 §7M] [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] |
| 8 · DESIGNED | C-7M.2.7 — Computed View factor 7 — recency tie-breaker | The fixed order and separation of the seven factors. | Supplies the limited recency tie-breaker. | One separately recorded contribution to current ordering. | [V10 §7M] [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] |
| 9 · ACCEPTED | C-7M.3 — Computed View ordering-profile record | The immutable order of the seven factors. | The seven-factor order remains fixed. | No hidden reordering or collapsed score. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] |
| 10 · ACCEPTED | C-7M.3.8 — Computed View fixed-factor profile field | The immutable order of the seven factors. | Supplies the authoritative seven-factor order. | No hidden reordering or collapsed score. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [V10 §7M] |
| 11 · ACCEPTED | C-7M.10.9.1 — Computed View relevance ordering consequences | The immutable order of the seven factors. | Supplies the fixed seven-factor order. | No hidden reordering or collapsed score. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [V10 §7M] |
| 12 · ACCEPTED | C-7I.1.4 — Current best-supported delegation | The actual claim being made and Computed View's separate seven-factor results. | Supplies the fixed seven-factor ordering. | Nothing in this card. | [V10 §7M] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] |

SUB-PARTS: C-7M.2.1 — Computed View factor 1 — current Ness judgment; C-7M.2.2 — Computed View factor 2 — direct root evidence; C-7M.2.3 — Computed View factor 3 — reading acceptance and grounding; C-7M.2.4 — Computed View factor 4 — purpose relevance; C-7M.2.5 — Computed View factor 5 — context quality and provenance; C-7M.2.6 — Computed View factor 6 — clashes and uncertainty; C-7M.2.7 — Computed View factor 7 — recency tie-breaker

### C-7M.2.1 — Computed View factor 1 — current Ness judgment
Stamp: DESIGNED    Source: [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]

ALONE
- What it is: DESIGNED — The first ordering factor: Ness's explicit current judgment when relevant. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Takes in: DESIGNED — Relevant explicit Ness response or judgment events. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Does: DESIGNED — Uses that judgment in current presentation while keeping the response event and underlying evidence separate. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Gives out: DESIGNED — The first factor's disclosed result. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Must never: DESIGNED — Treat a response as a rewrite of history, a machine truth verdict or erasure of a conflicting source. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J.6 — Ness response as separate event: separate response events whose explicit judgments may affect current use. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-7M.2 — Computed View seven-factor priority order: supplies the relevant current-judgment factor. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M.2 — Computed View seven-factor priority order | Relevant explicit judgment. | Places it first without changing historical evidence. | The current-judgment ordering result. | [V10 §7M] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7M.5.6 — Computed View separate ordering-factor results | The explicit current Ness-judgment outcome. | Records it as factor 1 separately from evidence and interpretation. | An inspectable first-factor result. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.2.2 — Computed View factor 2 — direct root evidence
Stamp: DESIGNED    Source: [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]

ALONE
- What it is: DESIGNED — The second ordering factor: strength and directness of supporting root evidence. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Takes in: ACCEPTED — Direct supporting root references and the preserved evidence-family relationships of derivative support. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: DESIGNED — Prioritizes direct root support over repetition, frequency or model confidence. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Does: ACCEPTED — Records this factor's outcome with pointers directly to supporting roots. For independent support, one underlying-event evidence family counts as one unit regardless of how many readings, restatements, copies, derivative references or operational records it contains; every member remains separately preserved and inspectable. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: DESIGNED — A direct-root-grounded factor result with its support chain. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Must never: ACCEPTED — Count same-event derivatives or their logs as independent votes; copy or collapse evidence members; use model confidence as a substitute for root support. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: BUILT — C-STORE — Accretive store & sealed roots (§6B): the immutable supporting roots addressed by their own IDs. [V10 §6A] [V10 §6B]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-7M.2 — Computed View seven-factor priority order: supplies the direct-evidence factor. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M.2 — Computed View seven-factor priority order | Direct root strength and provenance. | Ranks root support above derivative repetition. | The second factor's honest support result. | [V10 §7M] |
| 2 · ACCEPTED | C-7M.5.6 — Computed View separate ordering-factor results | The direct-root-evidence outcome and supporting root pointers. | Records factor 2 with direct reference support and no same-event extra votes. | Inspectable root grounding. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.2.3 — Computed View factor 3 — reading acceptance and grounding
Stamp: DESIGNED    Source: [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]

ALONE
- What it is: DESIGNED — The third ordering factor: reading acceptance status and grounding quality. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Takes in: DESIGNED — The reading's actual acceptance and grounding information. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Does: DESIGNED — Keeps acceptance status and grounded support distinct from whether an interpretation is true. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Gives out: DESIGNED — The third factor's disclosed result. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Must never: DESIGNED — Treat acceptance as a final truth verdict or hide a reading's grounding limits. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): reading acceptance and grounding outcomes. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-7M.2 — Computed View seven-factor priority order: supplies reading-status and grounding priority. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M.2 — Computed View seven-factor priority order | Acceptance and grounded support. | Uses them as the third factor. | A labeled reading-quality result. | [V10 §7M] |
| 2 · ACCEPTED | C-7M.5.6 — Computed View separate ordering-factor results | The reading acceptance and grounding outcome. | Records factor 3 separately without a truth verdict. | Visible reading-support limits. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.2.4 — Computed View factor 4 — purpose relevance
Stamp: DESIGNED    Source: [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [V10 §7R]

ALONE
- What it is: DESIGNED — The fourth ordering factor: relevance to the current question or view purpose. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [V10 §7R]
- Takes in: DESIGNED — The relevance judgment made under the declared current-purpose configuration. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [V10 §7R]
- Does: DESIGNED — Uses relevance only as factor 4, separate from evidence strength, truth, currentness, authority and permission. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [V10 §7R]
- Gives out: DESIGNED — A purpose-scoped factor result. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [V10 §7R]
- Must never: ACCEPTED — Let relevance reorder the seven factors, widen access, become state evidence or supply a hidden truth score. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7M.10 — Computed View proposed RM-CV-01 declaration: the accepted proposed view-assembly declaration and its applicable dimension results. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gated by: DESIGNED — C-7R — Attention & Relevance Control (§7R): the current purpose must have a valid declared and validated relevance mode. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [V10 §7R]
- Changes: DESIGNED — C-7M.2 — Computed View seven-factor priority order: supplies relevance only to factor 4. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [V10 §7R]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M.2 — Computed View seven-factor priority order | Current-purpose relevance. | Keeps it fourth and separate from all other factors. | Purpose-aware priority only. | [V10 §7M] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 2 · ACCEPTED | C-7M.5.6 — Computed View separate ordering-factor results | The fourth factor's current-question/view-purpose role. | Supplies the relevance result. | No relevance override of other factors. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [V10 §7M] |
| 3 · ACCEPTED | C-7M.10 — Computed View proposed RM-CV-01 declaration | The fourth factor's current-question/view-purpose role. | Informs factor 4 only. | No relevance override of other factors. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [V10 §7M] |

SUB-PARTS: NONE

### C-7M.2.5 — Computed View factor 5 — context quality and provenance
Stamp: DESIGNED    Source: [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]

ALONE
- What it is: DESIGNED — The fifth ordering factor: context quality and retrieval provenance. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Takes in: DESIGNED — The context and provenance accompanying the source readings and retrieved material. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Does: DESIGNED — Uses the quality and traceable origin of the actual context rather than silently filling its gaps. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Gives out: DESIGNED — The fifth factor's disclosed result. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Must never: DESIGNED — Hide context limits, erase retrieval provenance or treat a context gap as supplied evidence. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7F — Context Retrieval (§7F): the labeled context channels and their retrieval provenance. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-7M.2 — Computed View seven-factor priority order: supplies the context-quality factor. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M.2 — Computed View seven-factor priority order | Actual context quality and provenance. | Keeps that context basis explicit. | The fifth factor's result. | [V10 §7M] |
| 2 · ACCEPTED | C-7M.5.6 — Computed View separate ordering-factor results | The context-quality and retrieval-provenance outcome. | Records factor 5 with its support limitations. | Explicit context provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.2.6 — Computed View factor 6 — clashes and uncertainty
Stamp: DESIGNED    Source: [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]

ALONE
- What it is: DESIGNED — The sixth factor: active clashes, unresolved uncertainty and contrary evidence beside the item. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Takes in: DESIGNED — The source item's clashes, contrary support and unresolved uncertainty. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Does: ACCEPTED — Surfaces these alongside the item even when direct support is strong. Keeps conflicted material labeled as conflicted; support too weak or conflicted may yield no clear current view. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Gives out: DESIGNED — A visible conflict/uncertainty result. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Must never: DESIGNED — Suppress contrary evidence, silently treat conflicted support as clean or resolve a clash by selecting a winner. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Withholds or clearly labels weak, conflicted, stale or insufficient support rather than silently presenting it as uncontested. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]

TOGETHER
- Fed by: ACCEPTED — C-7J.7 — Downstream effects of clashes: preserved clash effects and qualification rules; C-7J.8 — Clash and named-gap presentation: beside-item clash presentation and response detail. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-7M.2 — Computed View seven-factor priority order: supplies the conflict and uncertainty factor. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M.2 — Computed View seven-factor priority order | Clashes and contrary evidence. | Keeps them beside the affected item. | An honest conflicted current picture. | [V10 §7M] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7M.5.6 — Computed View separate ordering-factor results | The active clashes, uncertainty and contrary evidence. | Supplies the clash/uncertainty result. | No silently clean support. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [V10 §7M] |
| 3 · ACCEPTED | C-7M.5.7 — Computed View snapshot clashes and uncertainty | The active clashes, uncertainty and contrary evidence. | Supplies the conflict/uncertainty factor and beside-item requirement. | No silently clean support. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [V10 §7M] |

SUB-PARTS: NONE

### C-7M.2.7 — Computed View factor 7 — recency tie-breaker
Stamp: DESIGNED    Source: [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]

ALONE
- What it is: DESIGNED — The seventh factor: recency as a limited tie-breaker only. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Takes in: DESIGNED — The candidates' temporal provenance after the earlier factors. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Does: DESIGNED — Uses recency only within the disclosed tie-break rule, never as authority. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Gives out: DESIGNED — A limited temporal ordering result. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Must never: DESIGNED — Treat newest or most frequent as inherently more reliable or override direct support through recency. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-7M.2 — Computed View seven-factor priority order: supplies the limited recency tie-breaker. [V10 §7M / SEVEN-FACTOR PRIORITY ORDER]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M.2 — Computed View seven-factor priority order | Recency in a remaining tie. | Uses it last and without truth authority. | A limited tie-break result. | [V10 §7M] |
| 2 · ACCEPTED | C-7M.5.6 — Computed View separate ordering-factor results | The final recency tie-break outcome. | Records recency separately without upgrading reliability. | No recency-derived truth score. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.3 — Computed View ordering-profile record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — An immutable, versioned record of a Computed View purpose and its disclosed ordering rules. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — view_profile_id; profile_version; profile_purpose_type; optional human-readable purpose label; consuming_component; authorization/privacy basis; eligible source-reference families; seven fixed factors; disclosed factor-specific ordering, tie, omission and surfacing rules; no-hidden-score declaration; Tier-1 and Tier-2 configuration references; refresh triggers; invalidating events; unresolved-dimension handling reference where applicable; derivation_rule_version; created_at; prior/superseded profile-version reference; operational-log reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Binds each refresh and snapshot to the exact profile ID/version. A change creates a new version and preserves all earlier versions. Allows disclosed purpose-specific handling for current situation, person-focused, project-focused, historical review or another declared purpose while keeping the seven factors in their fixed order. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — A preserved, inspectable profile version with alternatives and provenance still reachable. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Edit a committed version, silently reorder factors, turn a factor into hidden truth authority or invent a significance threshold, time, score, weight, model choice or calibration value. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Missing, invalid, stale or unauthorized configuration creates a failed or incomplete refresh-status event and no snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

TOGETHER
- Fed by: ACCEPTED — C-7M.3.1 — Computed View view_profile_id: profile ID; C-7M.3.2 — Computed View profile_version: version; C-7M.3.3 — Computed View profile_purpose_type: purpose type; C-7M.3.4 — Computed View optional purpose label: optional label; C-7M.3.5 — Computed View consuming_component: consumer; C-7M.3.6 — Computed View authorization and privacy basis: authorization/privacy basis; C-7M.3.7 — Computed View eligible source-reference families: eligible families; C-7M.3.8 — Computed View fixed-factor profile field: fixed factors; C-7M.3.9 — Computed View disclosed factor-specific rules: disclosed handling rules; C-7M.3.10 — Computed View no-hidden-score declaration: no-hidden-score declaration; C-7M.3.11 — Computed View Tier-1 configuration reference: Tier-1 reference; C-7M.3.12 — Computed View Tier-2 configuration reference: Tier-2 reference; C-7M.3.13 — Computed View declared refresh triggers: refresh triggers; C-7M.3.14 — Computed View declared invalidating events: invalidating events; C-7M.3.15 — Computed View unresolved-handling reference: unresolved handling; C-7M.3.16 — Computed View derivation_rule_version: derivation version; C-7M.3.17 — Computed View record created_at: creation time; C-7M.3.18 — Computed View prior profile-version reference: preceding version; C-7M.3.19 — Computed View operational-log references: operational-log reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gated by: DESIGNED — C-7M.2 — Computed View seven-factor priority order: the seven-factor order remains fixed; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the profile and its use require their purpose's authorization. [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M — Computed View (§7M) | The exact immutable ordering profile. | Uses its disclosed rules and version for assembly. | A reproducible current picture. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7M.3.1 — Computed View view_profile_id | The versioned profile's required conceptual field contract. | Supplies the ordering-profile identity. | A complete explicit profile whose committed version is never silently edited. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 3 · ACCEPTED | C-7M.3.2 — Computed View profile_version | The versioned profile's required conceptual field contract. | Supplies the immutable profile-version identity. | A complete explicit profile whose committed version is never silently edited. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 4 · ACCEPTED | C-7M.3.3 — Computed View profile_purpose_type | The versioned profile's required conceptual field contract. | Supplies the profile-purpose field. | A complete explicit profile whose committed version is never silently edited. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 5 · ACCEPTED | C-7M.3.4 — Computed View optional purpose label | The versioned profile's required conceptual field contract. | Supplies the optional purpose explanation. | A complete explicit profile whose committed version is never silently edited. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 6 · ACCEPTED | C-7M.3.5 — Computed View consuming_component | The versioned profile's required conceptual field contract. | Supplies the consuming-component identity. | A complete explicit profile whose committed version is never silently edited. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |
| 7 · ACCEPTED | C-7M.3.6 — Computed View authorization and privacy basis | The versioned profile's required conceptual field contract. | Supplies the profile's authorization/privacy references. | A complete explicit profile whose committed version is never silently edited. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] |
| 8 · ACCEPTED | C-7M.3.7 — Computed View eligible source-reference families | The versioned profile's required conceptual field contract. | Supplies the profile's eligible source families. | A complete explicit profile whose committed version is never silently edited. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 9 · ACCEPTED | C-7M.3.8 — Computed View fixed-factor profile field | The versioned profile's required conceptual field contract. | Supplies the fixed factors in the profile. | A complete explicit profile whose committed version is never silently edited. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 10 · ACCEPTED | C-7M.3.9 — Computed View disclosed factor-specific rules | The versioned profile's required conceptual field contract. | Supplies the disclosed factor handling. | A complete explicit profile whose committed version is never silently edited. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 11 · ACCEPTED | C-7M.3.10 — Computed View no-hidden-score declaration | The versioned profile's required conceptual field contract. | Supplies the no-hidden-score declaration. | A complete explicit profile whose committed version is never silently edited. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 12 · ACCEPTED | C-7M.3.11 — Computed View Tier-1 configuration reference | The versioned profile's required conceptual field contract. | Supplies the exact Tier-1 reference. | A complete explicit profile whose committed version is never silently edited. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 13 · ACCEPTED | C-7M.3.12 — Computed View Tier-2 configuration reference | The versioned profile's required conceptual field contract. | Supplies the exact Tier-2 reference. | A complete explicit profile whose committed version is never silently edited. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 14 · ACCEPTED | C-7M.3.13 — Computed View declared refresh triggers | The versioned profile's required conceptual field contract. | Supplies declared refresh triggers. | A complete explicit profile whose committed version is never silently edited. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 15 · ACCEPTED | C-7M.3.14 — Computed View declared invalidating events | The versioned profile's required conceptual field contract. | Supplies the profile's declared invalidating events. | A complete explicit profile whose committed version is never silently edited. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 16 · ACCEPTED | C-7M.3.15 — Computed View unresolved-handling reference | The versioned profile's required conceptual field contract. | Supplies the unresolved-handling reference. | A complete explicit profile whose committed version is never silently edited. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 17 · ACCEPTED | C-7M.3.16 — Computed View derivation_rule_version | The versioned profile's required conceptual field contract. | Supplies the derivation-rule version. | A complete explicit profile whose committed version is never silently edited. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 18 · ACCEPTED | C-7M.3.17 — Computed View record created_at | The versioned profile's required conceptual field contract. | Supplies the profile creation time. | A complete explicit profile whose committed version is never silently edited. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 19 · ACCEPTED | C-7M.3.18 — Computed View prior profile-version reference | The versioned profile's required conceptual field contract. | Supplies the prior-version link. | A complete explicit profile whose committed version is never silently edited. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 20 · ACCEPTED | C-7M.3.19 — Computed View operational-log references | The versioned profile's required conceptual field contract. | Supplies the profile's operational-log reference. | A complete explicit profile whose committed version is never silently edited. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 21 · ACCEPTED | C-7M.5 — Computed View immutable snapshot record | The exact valid authorized profile/version and declared purpose. | The exact profile must be valid, current and authorized. | No snapshot from a missing, invalid, stale or unauthorized profile. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 22 · ACCEPTED | C-7M.10 — Computed View proposed RM-CV-01 declaration | The exact valid authorized profile/version and declared purpose. | Supplies the exact ordering profile. | No snapshot from a missing, invalid, stale or unauthorized profile. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |

SUB-PARTS: C-7M.3.1 — Computed View view_profile_id; C-7M.3.2 — Computed View profile_version; C-7M.3.3 — Computed View profile_purpose_type; C-7M.3.4 — Computed View optional purpose label; C-7M.3.5 — Computed View consuming_component; C-7M.3.6 — Computed View authorization and privacy basis; C-7M.3.7 — Computed View eligible source-reference families; C-7M.3.8 — Computed View fixed-factor profile field; C-7M.3.9 — Computed View disclosed factor-specific rules; C-7M.3.10 — Computed View no-hidden-score declaration; C-7M.3.11 — Computed View Tier-1 configuration reference; C-7M.3.12 — Computed View Tier-2 configuration reference; C-7M.3.13 — Computed View declared refresh triggers; C-7M.3.14 — Computed View declared invalidating events; C-7M.3.15 — Computed View unresolved-handling reference; C-7M.3.16 — Computed View derivation_rule_version; C-7M.3.17 — Computed View record created_at; C-7M.3.18 — Computed View prior profile-version reference; C-7M.3.19 — Computed View operational-log references

### C-7M.3.1 — Computed View view_profile_id
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The stable view_profile_id identifying the ordering profile. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The profile identity used by an ordering record, snapshot or refresh attempt. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Keeps the exact profile identifiable together with its version. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — An inspectable profile reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Silently substitute another profile for the one recorded on an attempt or snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.3 — Computed View ordering-profile record: supplies the ordering-profile identity. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3 — Computed View ordering-profile record | The profile ID. | Identifies the declared ordering profile. | Stable profile identity. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7M.5 — Computed View immutable snapshot record | The exact view_profile_id. | Supplies the profile ID. | No substitution of profile identity. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 3 · ACCEPTED | C-7M.6.2 — Computed View attempted_profile_id_and_version | The exact view_profile_id. | Supplies the profile identity. | No substitution of profile identity. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 4 · ACCEPTED | C-7M.8 — Computed View duplicate prevention | The exact view_profile_id. | Supplies the exact profile ID. | No substitution of profile identity. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7M.3.2 — Computed View profile_version
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The exact profile_version bound to a profile record, snapshot or refresh attempt. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The committed version of the selected profile. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Changes only by creating a new preserved profile version; attempts and snapshots retain the exact version they used. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — A precise version reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Rewrite an earlier version or silently substitute a newer configuration. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — A missing, invalid, stale or unauthorized profile configuration cannot create a snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.3 — Computed View ordering-profile record: supplies the immutable profile-version identity. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3 — Computed View ordering-profile record | The profile version. | Preserves exact version binding. | Versioned profile history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7M.5 — Computed View immutable snapshot record | The exact profile_version. | Supplies the exact profile version. | No silent version replacement. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 3 · ACCEPTED | C-7M.6.2 — Computed View attempted_profile_id_and_version | The exact profile_version. | Supplies the exact version. | No silent version replacement. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 4 · ACCEPTED | C-7M.8 — Computed View duplicate prevention | The exact profile_version. | Supplies the profile version. | No silent version replacement. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7M.3.3 — Computed View profile_purpose_type
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The profile_purpose_type describing the current-picture purpose. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — The profile's declared purpose/current question, under the view_assembly relevance purpose. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Records why the particular view profile assembles this picture. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — A declared, inspectable purpose type. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Guess an unrecognized controlled purpose or invent a private meaning of relevant. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — An unrecognized relevance purpose follows the recorded halt-and-propose path; no mode is improvised. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7R — Attention & Relevance Control (§7R): the controlled purpose must be recognized under its vocabulary/version. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [V10 §7R]
- Changes: ACCEPTED — C-7M.3 — Computed View ordering-profile record: supplies the profile-purpose field. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3 — Computed View ordering-profile record | The declared profile purpose. | Keeps the current picture purpose-bound. | Explicit assembly intent. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 2 · ACCEPTED | C-7M.10.3 — Computed View relevance target | The profile's declared purpose/current question. | Uses that purpose as the relevance target. | No undeclared target substitution. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.3.4 — Computed View optional purpose label
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — An optional human-readable purpose label. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — A plain explanation such as assembling the internal current picture for a view profile. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Explains the declared purpose without becoming a separate behavior rule. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — An optional readable label. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Use the label to change the controlled purpose or widen eligible material. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.3 — Computed View ordering-profile record: supplies the optional purpose explanation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3 — Computed View ordering-profile record | The optional label. | Explains the purpose to inspection. | Readable profile metadata. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 2 · ACCEPTED | C-7M.10.3 — Computed View relevance target | The optional human description of the profile's purpose. | Carries the descriptive target context without changing the controlled purpose. | A human-readable purpose description. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.3.5 — Computed View consuming_component
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1]

ALONE
- What it is: ACCEPTED — The consuming_component identified by the ordering profile. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1]
- Takes in: ACCEPTED — The component that owns and uses the profile's Tier-2 rules. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1]
- Does: ACCEPTED — Keeps component ownership explicit; the relevance owner's Tier 1 and the consumer's Tier 2 remain separate. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1]
- Gives out: ACCEPTED — An accountable consuming-component reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1]
- Must never: ACCEPTED — Let a consumer silently take over Tier-1 validation or let the relevance owner take over Tier 2. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.3 — Computed View ordering-profile record: supplies the consuming-component identity. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3 — Computed View ordering-profile record | The consumer identity. | Records the profile's owner/use context. | Explicit component ownership. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |

SUB-PARTS: NONE

### C-7M.3.6 — Computed View authorization and privacy basis
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The authorization/privacy basis carried by a profile and its use. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Takes in: ACCEPTED — Purpose-specific authorization references for the actual material and operation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Does: ACCEPTED — Binds internal assembly to internal-use authorization and any visible result to its separate disclosure eligibility. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Gives out: ACCEPTED — An inspectable authorization basis. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Must never: ACCEPTED — Use a privacy or authority decision as evidence, weaken third-party/compartment/TSC/influence-removal limits or expand access through a profile. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — Unauthorized configuration does not produce a snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the actual purpose and material must be permitted; C-7P — Permission & Authority Boundaries (§7P): action-adjacent operations remain within authority. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Changes: ACCEPTED — C-7M.3 — Computed View ordering-profile record: supplies the profile's authorization/privacy references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3 — Computed View ordering-profile record | The authorization basis. | Records permitted purpose and scope. | A purpose-bounded profile. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.3.7 — Computed View eligible source-reference families
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The profile's eligible families drawn only from the ten permitted snapshot source families. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — Direct roots, readings, tellings, clashes, Ness response events, Person-Box links, themes, Living State, world model and safe metadata-only pre-ingest references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Declares which of those source families are eligible for the profile and links every object by ID. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — An explicit eligible-family set. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Create an undeclared source family, copy source objects or admit held raw content through a metadata reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Material outside the declared eligible family set fails the object-type gate. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: ACCEPTED — C-7M.5.5 — Computed View snapshot source-reference fields: the ten distinct source-reference fields. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.3 — Computed View ordering-profile record: supplies the profile's eligible source families. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3 — Computed View ordering-profile record | The declared permitted families. | Restricts profile candidates to the selected source scope. | Explicit source eligibility. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 2 · ACCEPTED | C-7M.5.5 — Computed View snapshot source-reference fields | The profile's explicitly eligible source families. | The profile must declare these families eligible. | No unlisted family or held raw content admitted by relevance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-7M.10 — Computed View proposed RM-CV-01 declaration | The profile's explicitly eligible source families. | Supplies the eligible candidate families. | No unlisted family or held raw content admitted by relevance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |
| 4 · ACCEPTED | C-7M.10.4.1 — Computed View object_type_matches gate | The profile's explicitly eligible source families. | Supplies the eligible family set. | No unlisted family or held raw content admitted by relevance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.3.8 — Computed View fixed-factor profile field
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The profile field carrying the seven settled factors in their fixed order. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — Judgment; direct root support; reading acceptance/grounding; purpose relevance; context/provenance; clashes/uncertainty; recency. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Stores the ordered factor contract without changing its precedence. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — An inspectable fixed-factor ordering declaration. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Silently reorder, drop or blend the factors into a score. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7M.2 — Computed View seven-factor priority order: the authoritative seven-factor order. [V10 §7M]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.3 — Computed View ordering-profile record: supplies the fixed factors in the profile. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3 — Computed View ordering-profile record | The seven factors in order. | Binds purpose-specific handling to fixed precedence. | No hidden reordering. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.3.9 — Computed View disclosed factor-specific rules
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The disclosed ordering, tie, omission and surfacing rules specific to each factor and purpose. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The profile's explicit rules for handling the settled factors. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Records purpose-specific handling while keeping alternatives and provenance accessible and preserving fixed factor precedence. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — An inspectable rule set explaining item handling. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Create hidden truth authority or silently substitute undisclosed ordering, tie, omission or surfacing behavior. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7M.3.9.1 — Computed View profile ordering rules: ordering rules; C-7M.3.9.2 — Computed View profile tie rules: tie rules; C-7M.3.9.3 — Computed View profile omission rules: omission rules; C-7M.3.9.4 — Computed View profile surfacing rules: surfacing rules. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.3 — Computed View ordering-profile record: supplies the disclosed factor handling. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3 — Computed View ordering-profile record | The disclosed factor-specific handling. | Makes purpose-specific assembly reviewable. | Transparent profile rules. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7M.3.9.1 — Computed View profile ordering rules | The requirement to disclose factor-specific ordering, tie, omission and surfacing rules. | Supplies disclosed ordering behavior. | No undisclosed choice masquerades as truth authority. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 3 · ACCEPTED | C-7M.3.9.2 — Computed View profile tie rules | The requirement to disclose factor-specific ordering, tie, omission and surfacing rules. | Supplies disclosed tie handling. | No undisclosed choice masquerades as truth authority. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [V10 §7M] |
| 4 · ACCEPTED | C-7M.3.9.3 — Computed View profile omission rules | The requirement to disclose factor-specific ordering, tie, omission and surfacing rules. | Supplies disclosed omission handling. | No undisclosed choice masquerades as truth authority. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 5 · ACCEPTED | C-7M.3.9.4 — Computed View profile surfacing rules | The requirement to disclose factor-specific ordering, tie, omission and surfacing rules. | Supplies the disclosed surfacing boundary. | No undisclosed choice masquerades as truth authority. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: C-7M.3.9.1 — Computed View profile ordering rules; C-7M.3.9.2 — Computed View profile tie rules; C-7M.3.9.3 — Computed View profile omission rules; C-7M.3.9.4 — Computed View profile surfacing rules

### C-7M.3.9.1 — Computed View profile ordering rules
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The profile's disclosed factor-specific ordering rules. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The purpose-specific handling within the fixed seven-factor order. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Records how candidates are ordered without choosing a hidden score or changing factor precedence. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — Inspectable ordering rules. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Silently reorder the settled factors or invent empirical weights. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.3.9 — Computed View disclosed factor-specific rules: supplies disclosed ordering behavior. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3.9 — Computed View disclosed factor-specific rules | The ordering rules. | Keeps them explicit in the profile. | Reviewable candidate order. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.3.9.2 — Computed View profile tie rules
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [V10 §7M]

ALONE
- What it is: ACCEPTED — The profile's disclosed rules for ties. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [V10 §7M]
- Takes in: ACCEPTED — A remaining tie under the prior factors. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [V10 §7M]
- Does: ACCEPTED — Records tie handling while preserving recency as a limited last factor. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [V10 §7M]
- Gives out: ACCEPTED — An inspectable tie rule. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [V10 §7M]
- Must never: ACCEPTED — Let a tie-breaker become authority or override direct root support. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [V10 §7M]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.3.9 — Computed View disclosed factor-specific rules: supplies disclosed tie handling. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [V10 §7M]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3.9 — Computed View disclosed factor-specific rules | The tie-handling rule. | Makes the limited tie-break explicit. | No hidden tie resolution. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.3.9.3 — Computed View profile omission rules
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The profile's disclosed factor-specific omission rules. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — Candidates considered but omitted or set aside and the relevant rule. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Preserves the reason for an omission in the snapshot instead of silently concealing missing support. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — An inspectable omission rule and reason. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Omit a candidate without recording why or turn omission into deletion of its source. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.3.9 — Computed View disclosed factor-specific rules: supplies disclosed omission handling. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3.9 — Computed View disclosed factor-specific rules | The omission rules. | Makes set-aside behavior explicit. | Honest omission provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7M.5.8 — Computed View omitted candidates and reasons | The profile's disclosed omission rules. | Records omitted/set-aside candidates with actual reasons. | Inspectable omission without deleting the source. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.3.9.4 — Computed View profile surfacing rules
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The profile's disclosed surfacing rules within the internal-tool boundary. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — The profile purpose, current picture and any deliberate inspection request. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Keeps the view silent internally; any permitted inspection preserves alternative records, provenance, clash and uncertainty labels. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — Explicit surfacing behavior. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Make a profile authorize unprompted display or widen disclosure permissions. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7M.1 — Computed View internal-use boundary: the view itself is shown only on Ness's deliberate request. [V10 §7M] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Changes: ACCEPTED — C-7M.3.9 — Computed View disclosed factor-specific rules: supplies the disclosed surfacing boundary. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3.9 — Computed View disclosed factor-specific rules | The surfacing rules. | Records when the picture remains internal or is deliberately inspected. | Bounded display behavior. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.3.10 — Computed View no-hidden-score declaration
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The profile's explicit no-hidden-score declaration. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The seven separate ordering factors and their disclosed rules. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — States that their outcomes remain separate and do not collapse into one numerical truth authority. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — An explicit no-hidden-score commitment in the profile. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Hide a score or weight that blends evidence, interpretation, judgment and uncertainty. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.3 — Computed View ordering-profile record: supplies the no-hidden-score declaration. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3 — Computed View ordering-profile record | The no-hidden-score rule. | Makes the prohibition explicit in the profile. | Separated ordering authority. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.3.11 — Computed View Tier-1 configuration reference
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The exact reference to the relevance owner's Tier-1 configuration. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — The proposed RM-CV-01 declaration identity and proposed declaration_version = v1_0 for view_assembly, as validated by the relevance owner. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Records the Tier-1 reference used by the profile and each evaluation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — An inspectable Tier-1 binding. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Let the consumer self-approve Tier 1 or silently substitute another declaration version. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Missing, invalid, stale or unauthorized configuration produces no snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: ACCEPTED — C-7M.10 — Computed View proposed RM-CV-01 declaration: the proposed view-assembly declaration. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gated by: DESIGNED — C-7R — Attention & Relevance Control (§7R): Tier 1 is owned and validated by Attention and Relevance Control. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1]
- Changes: ACCEPTED — C-7M.3 — Computed View ordering-profile record: supplies the exact Tier-1 reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3 — Computed View ordering-profile record | The validated Tier-1 binding. | Preserves the declaration identity/version used. | Traceable relevance configuration. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.3.12 — Computed View Tier-2 configuration reference
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The exact component-owned Tier-2 configuration reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — The current declaration's ordering, fallback, surfacing, unresolved-handling and strictness rules. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Binds the profile to the Tier-2 rules owned and validated by Computed View. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — An inspectable consumer-rule reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Let the relevance owner silently replace consumer Tier 2 or omit its unresolved behavior. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Missing or invalid configuration cannot produce a snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: ACCEPTED — C-7M.10 — Computed View proposed RM-CV-01 declaration: the current declaration's component-owned Tier-2 rules. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.3 — Computed View ordering-profile record: supplies the exact Tier-2 reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3 — Computed View ordering-profile record | The consumer's Tier-2 reference. | Preserves the exact assembly behavior binding. | Inspectable consumer configuration. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.3.13 — Computed View declared refresh triggers
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The refresh triggers declared by the profile. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — Opening, manual refresh and materially relevant events defined for that profile. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Records the relevant triggers without introducing continuous or undeclared pre-computation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — A declared trigger set. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Make unrelated new material force every view to recalculate or add an undeclared scheduled recomputation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7M.4 — Computed View update triggers: the three settled update-trigger routes. [V10 §7M]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.3 — Computed View ordering-profile record: supplies declared refresh triggers. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3 — Computed View ordering-profile record | The profile's triggers. | Makes update admission explicit. | Triggered rather than continuous assembly. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 2 · DESIGNED | C-7M.4.3 — Computed View materially-relevant-event trigger | The profile's declared materially relevant triggers. | Allows only an event relevant to the profile to initiate this route. | No undeclared significance rule. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.3.14 — Computed View declared invalidating events
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The invalidating events declared in the profile configuration. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The profile's explicit invalidation declarations. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Preserves those declarations in the immutable profile version; later status consequences are recorded through new events. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — An inspectable invalidating-event set. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Edit a snapshot or old profile version when a declared invalidating event occurs. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.3 — Computed View ordering-profile record: supplies the profile's declared invalidating events. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3 — Computed View ordering-profile record | The declared invalidation conditions. | Binds them to the exact profile version. | Traceable validity handling. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.3.15 — Computed View unresolved-handling reference
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The unresolved-dimension handling reference carried where applicable by the profile. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — The proposed T2-UNRES-SHARED v1_0 rule selected by the current declaration. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Binds uncertainty handling to the declared identifier and version instead of guessing at a disputed or absent result. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — An inspectable uncertainty-rule reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Silently choose the more confident model result or turn unresolved values into factual, current-state or authority support. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Failed relevance values are not used; unresolved values remain labeled weak internal clues only where the declaration permits them. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: ACCEPTED — C-7M.10 — Computed View proposed RM-CV-01 declaration: the declared current-purpose uncertainty handling. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.3 — Computed View ordering-profile record: supplies the unresolved-handling reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3 — Computed View ordering-profile record | The uncertainty rule and version. | Preserves declared unresolved behavior. | No improvised uncertainty resolution. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.3.16 — Computed View derivation_rule_version
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The derivation_rule_version used by a profile and snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The exact derivation ruleset version. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Preserves which rules produced the current picture so a later version cannot silently alter its explanation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — An inspectable derivation-version reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Rewrite the version on an existing profile or snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.3 — Computed View ordering-profile record: supplies the derivation-rule version. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3 — Computed View ordering-profile record | The ruleset version. | Makes derivation reproducible from its record. | Versioned explanation provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7M.5 — Computed View immutable snapshot record | The derivation_rule_version actually used. | Records that version on the immutable snapshot. | Inspectable derivation provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.3.17 — Computed View record created_at
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The created_at timestamp of a profile, snapshot, refresh/status event or operational lifecycle/status event. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — The creation time of that particular record. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Preserves the record's own temporal provenance without changing earlier timestamps on refresh or supersession. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — A record-specific created_at value. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Make an old record appear newly created by rewriting its timestamp. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.3 — Computed View ordering-profile record: supplies the profile creation time. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3 — Computed View ordering-profile record | The profile's creation time. | Records temporal version provenance. | A preserved profile timestamp. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7M.5 — Computed View immutable snapshot record | The record's actual created_at value. | Supplies the creation time. | No rewritten apparent freshness. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 3 · ACCEPTED | C-7M.6 — Computed View refresh-status event | The record's actual created_at value. | Supplies `created_at`. | No rewritten apparent freshness. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 4 · ACCEPTED | C-7M.11.4 — Bundle 4 operational-record lifecycle-status event | The record's actual created_at value. | Supplies `created_at`. | No rewritten apparent freshness. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 5 · ACCEPTED | C-7D.16.5 — World active-core membership event | membership_event_id, world_object_or_condition_id, operation_id, previous_membership, new_membership, basis_type, basis_reference, purpose_scope, supporting_evidence_references, grounding_status, reason, authorization_reference, created_at, supersedes_or_relates_to_event and operational_log_reference. | Supplies `created_at`. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §6] |
| 6 · ACCEPTED | C-7N.12.1 — Surfacing operational-record content | What was evaluated, used, not used, omitted or set aside and why. | Supplies shared created_at. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.3.18 — Computed View prior profile-version reference
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The reference to the prior or superseded profile version. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The preceding immutable version where one exists. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Links version history while preserving earlier profiles for inspection. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — A prior/superseded version reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Overwrite or hide the earlier profile to make the newer version current. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.3 — Computed View ordering-profile record: supplies the prior-version link. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3 — Computed View ordering-profile record | The preceding profile version. | Keeps the profile history connected. | Append-only version lineage. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.3.19 — Computed View operational-log references
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The operational-log reference or references connecting a view-domain record to its separate operational record. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — The operational record of the profile, snapshot, refresh or status-evaluation operation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Keeps domain records and their required log connected without merging the two record kinds or adding another evidence vote. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — Inspectable operational-log references, including operational_log_reference where the event schema names it. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Use an operational log instead of domain commitment or double-count a domain event and its log as independent evidence. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7M.11 — Computed View operational records and lifecycle: the separate connected operational record. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.3 — Computed View ordering-profile record: supplies the profile's operational-log reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.3 — Computed View ordering-profile record | The profile-operation log. | Links it separately from the profile version. | Inspectable profile creation/versioning provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-7M.5 — Computed View immutable snapshot record | The corresponding operational-log reference. | Supplies the operational-log references. | Traceability without merging record kinds. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 3 · ACCEPTED | C-7M.6 — Computed View refresh-status event | The corresponding operational-log reference. | Supplies `operational_log_reference`. | Traceability without merging record kinds. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 4 · ACCEPTED | C-7M.11.4 — Bundle 4 operational-record lifecycle-status event | The corresponding operational-log reference. | Supplies `operational_log_reference`. | Traceability without merging record kinds. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 5 · ACCEPTED | C-7D.16.5 — World active-core membership event | membership_event_id, world_object_or_condition_id, operation_id, previous_membership, new_membership, basis_type, basis_reference, purpose_scope, supporting_evidence_references, grounding_status, reason, authorization_reference, created_at, supersedes_or_relates_to_event and operational_log_reference. | Supplies `operational_log_reference`. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7M.4 — Computed View update triggers
Stamp: DESIGNED    Source: [V10 §7M / UPDATE TIMING]

ALONE
- What it is: DESIGNED — The three trigger routes for updating a Computed View. [V10 §7M / UPDATE TIMING]
- Takes in: DESIGNED — Ness opening the view, a manual refresh request, or an event materially relevant to the particular profile. [V10 §7M / UPDATE TIMING]
- Does: DESIGNED — Starts an update on the applicable trigger; unrelated new material does not recalculate every view. Updates are triggered, not continuous. [V10 §7M / UPDATE TIMING]
- Gives out: DESIGNED — A profile-specific refresh request with its trigger provenance. [V10 §7M / UPDATE TIMING]
- Must never: DESIGNED — Continuously recompute, infer relevance from every new object or force unrelated views to update. [V10 §7M / UPDATE TIMING]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7M.4.1 — Computed View opened trigger: opened view; C-7M.4.2 — Computed View manual-refresh trigger: manual refresh; C-7M.4.3 — Computed View materially-relevant-event trigger: materially relevant event. [V10 §7M / UPDATE TIMING]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M — Computed View (§7M) | A settled update trigger. | Begins the applicable profile's refresh. | A triggered internal update. | [V10 §7M] |
| 2 · ACCEPTED | C-7M.3.13 — Computed View declared refresh triggers | The opening, requested-refresh and profile-relevant material-event trigger routes. | Supplies the three settled update-trigger routes. | Traceable on-demand assembly timing. | [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-7M.5.3 — Computed View snapshot trigger reference | The opening, requested-refresh and profile-relevant material-event trigger routes. | Supplies the opened, manual or materially relevant event trigger. | Traceable on-demand assembly timing. | [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 4 · ACCEPTED | C-7M.6.3 — Computed View attempted_trigger | The opening, requested-refresh and profile-relevant material-event trigger routes. | Only the settled opening, manual-refresh or materially relevant event routes initiate the attempt. | Traceable on-demand assembly timing. | [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 5 · ACCEPTED | C-7M.10.7 — Computed View relevance evaluation timing | The opening, requested-refresh and profile-relevant material-event trigger routes. | Supplies the permitted triggers. | Traceable on-demand assembly timing. | [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 6 · DESIGNED | C-7M.4.1 — Computed View opened trigger | The three settled update routes. | Supplies the opened-view trigger. | No unrelated global refresh. | [V10 §7M] [V10 §7M / UPDATE TIMING] |
| 7 · DESIGNED | C-7M.4.2 — Computed View manual-refresh trigger | The three settled update routes. | Supplies the manual-refresh trigger. | No unrelated global refresh. | [V10 §7M] [V10 §7M / UPDATE TIMING] |
| 8 · DESIGNED | C-7M.4.3 — Computed View materially-relevant-event trigger | The three settled update routes. | Supplies a materially relevant event trigger. | No unrelated global refresh. | [V10 §7M] [V10 §7M / UPDATE TIMING] |

SUB-PARTS: C-7M.4.1 — Computed View opened trigger; C-7M.4.2 — Computed View manual-refresh trigger; C-7M.4.3 — Computed View materially-relevant-event trigger

### C-7M.4.1 — Computed View opened trigger
Stamp: DESIGNED    Source: [V10 §7M / UPDATE TIMING]

ALONE
- What it is: DESIGNED — The trigger produced when Ness opens the Computed View. [V10 §7M / UPDATE TIMING]
- Takes in: DESIGNED — The deliberate opening and the selected view profile. [V10 §7M / UPDATE TIMING]
- Does: DESIGNED — Requests an update for the opened profile. [V10 §7M / UPDATE TIMING]
- Gives out: DESIGNED — An opened-view refresh trigger. [V10 §7M / UPDATE TIMING]
- Must never: DESIGNED — Treat the trigger as permission to show unrelated internal knowledge. [V10 §7M / UPDATE TIMING]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7M.1 — Computed View internal-use boundary: inspection follows Ness's deliberate opening/request. [V10 §7M / UPDATE TIMING]
- Changes: DESIGNED — C-7M.4 — Computed View update triggers: supplies the opened-view trigger. [V10 §7M / UPDATE TIMING]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M.4 — Computed View update triggers | Ness opening the view. | Starts the opened profile's update. | A recorded update trigger. | [V10 §7M] |

SUB-PARTS: NONE

### C-7M.4.2 — Computed View manual-refresh trigger
Stamp: DESIGNED    Source: [V10 §7M / UPDATE TIMING]

ALONE
- What it is: DESIGNED — The trigger from Ness's manual request to refresh. [V10 §7M / UPDATE TIMING]
- Takes in: DESIGNED — The refresh request and selected profile. [V10 §7M / UPDATE TIMING]
- Does: DESIGNED — Requests a new profile update under its declared rules. [V10 §7M / UPDATE TIMING]
- Gives out: DESIGNED — A manual-refresh trigger. [V10 §7M / UPDATE TIMING]
- Must never: DESIGNED — Treat a failed refresh as successful merely because it was requested. [V10 §7M / UPDATE TIMING]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — Ness's actual refresh request supplies this trigger. [V10 §7M / UPDATE TIMING]
- Changes: DESIGNED — C-7M.4 — Computed View update triggers: supplies the manual-refresh trigger. [V10 §7M / UPDATE TIMING]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M.4 — Computed View update triggers | The manual request. | Begins the requested update. | A recorded manual-refresh attempt. | [V10 §7M] |

SUB-PARTS: NONE

### C-7M.4.3 — Computed View materially-relevant-event trigger
Stamp: DESIGNED    Source: [V10 §7M / UPDATE TIMING]

ALONE
- What it is: DESIGNED — An event explicitly relevant to the particular profile's current picture. [V10 §7M / UPDATE TIMING]
- Takes in: DESIGNED — A new accepted reading, new/changed active clash, Ness response, confirmed theme, identity resolution or another event explicitly defined as relevant by the profile. [V10 §7M / UPDATE TIMING]
- Does: DESIGNED — Requests an update only for the profiles to which the event is materially relevant. [V10 §7M / UPDATE TIMING]
- Gives out: DESIGNED — A profile-specific event trigger. [V10 §7M / UPDATE TIMING]
- Must never: DESIGNED — Let unrelated material force global recalculation or invent significance thresholds. [V10 §7M / UPDATE TIMING]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7M.4.3.1 — Computed View accepted-reading event trigger: accepted reading; C-7M.4.3.2 — Computed View active-clash event trigger: active clash change; C-7M.4.3.3 — Computed View Ness-response event trigger: Ness response; C-7M.4.3.4 — Computed View theme-confirmation trigger: theme confirmation; C-7M.4.3.5 — Computed View identity-resolution trigger: identity resolution; C-7M.4.3.6 — Computed View other declared-event trigger: another explicitly declared event. [V10 §7M / UPDATE TIMING]
- Gated by: ACCEPTED — C-7M.3.13 — Computed View declared refresh triggers: the event must be materially relevant under the profile's declared refresh triggers. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Changes: DESIGNED — C-7M.4 — Computed View update triggers: supplies a materially relevant event trigger. [V10 §7M / UPDATE TIMING]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M.4 — Computed View update triggers | A materially relevant event. | Updates only the applicable profile. | A bounded event-triggered refresh. | [V10 §7M] |
| 2 · DESIGNED | C-7M.4.3.1 — Computed View accepted-reading event trigger | The requirement that the event materially affects this profile. | The reading event must be relevant to the profile. | An eligible profile update without forced unrelated recomputation. | [V10 §7M] [V10 §7M / UPDATE TIMING] |
| 3 · DESIGNED | C-7M.4.3.2 — Computed View active-clash event trigger | The requirement that the event materially affects this profile. | The clash event must be materially relevant to the profile. | An eligible profile update without forced unrelated recomputation. | [V10 §7M] [V10 §7M / UPDATE TIMING] |
| 4 · DESIGNED | C-7M.4.3.3 — Computed View Ness-response event trigger | The requirement that the event materially affects this profile. | The response must be materially relevant to the profile. | An eligible profile update without forced unrelated recomputation. | [V10 §7M] [V10 §7M / UPDATE TIMING] [V10 §7J] |
| 5 · DESIGNED | C-7M.4.3.4 — Computed View theme-confirmation trigger | The requirement that the event materially affects this profile. | The confirmation must be materially relevant to the profile. | An eligible profile update without forced unrelated recomputation. | [V10 §7M] [V10 §7M / UPDATE TIMING] |
| 6 · DESIGNED | C-7M.4.3.5 — Computed View identity-resolution trigger | The requirement that the event materially affects this profile. | The resolution must be materially relevant to the profile. | An eligible profile update without forced unrelated recomputation. | [V10 §7M] [V10 §7M / UPDATE TIMING] [V10 §7L] |
| 7 · DESIGNED | C-7M.4.3.6 — Computed View other declared-event trigger | The requirement that the event materially affects this profile. | The event must be explicitly defined as materially relevant to this profile. | An eligible profile update without forced unrelated recomputation. | [V10 §7M] [V10 §7M / UPDATE TIMING] |

SUB-PARTS: C-7M.4.3.1 — Computed View accepted-reading event trigger; C-7M.4.3.2 — Computed View active-clash event trigger; C-7M.4.3.3 — Computed View Ness-response event trigger; C-7M.4.3.4 — Computed View theme-confirmation trigger; C-7M.4.3.5 — Computed View identity-resolution trigger; C-7M.4.3.6 — Computed View other declared-event trigger

### C-7M.4.3.1 — Computed View accepted-reading event trigger
Stamp: DESIGNED    Source: [V10 §7M / UPDATE TIMING]

ALONE
- What it is: DESIGNED — A new accepted reading that is materially relevant to the profile. [V10 §7M / UPDATE TIMING]
- Takes in: DESIGNED — The accepted reading and its source reference. [V10 §7M / UPDATE TIMING]
- Does: DESIGNED — Allows a profile update when the new reading is materially relevant. [V10 §7M / UPDATE TIMING]
- Gives out: DESIGNED — An accepted-reading trigger reference. [V10 §7M / UPDATE TIMING]
- Must never: DESIGNED — Treat every unrelated reading as a global refresh trigger. [V10 §7M / UPDATE TIMING]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): the new accepted reading. [V10 §7M / UPDATE TIMING]
- Gated by: DESIGNED — C-7M.4.3 — Computed View materially-relevant-event trigger: the reading event must be relevant to the profile. [V10 §7M / UPDATE TIMING]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M.4.3 — Computed View materially-relevant-event trigger | The new accepted reading. | Tests its declared profile relevance. | A relevant reading-triggered update. | [V10 §7M] |

SUB-PARTS: NONE

### C-7M.4.3.2 — Computed View active-clash event trigger
Stamp: DESIGNED    Source: [V10 §7M / UPDATE TIMING]

ALONE
- What it is: DESIGNED — A new or changed active clash relevant to the profile. [V10 §7M / UPDATE TIMING]
- Takes in: DESIGNED — The clash event and its preserved source references. [V10 §7M / UPDATE TIMING]
- Does: DESIGNED — Allows refresh of the affected current picture without resolving the clash. [V10 §7M / UPDATE TIMING]
- Gives out: DESIGNED — An active-clash trigger reference. [V10 §7M / UPDATE TIMING]
- Must never: DESIGNED — Interpret a refresh as closing or deleting the clash. [V10 §7M / UPDATE TIMING]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J — Clash Handling (§7J): the new or changed active-clash information. [V10 §7M / UPDATE TIMING]
- Gated by: DESIGNED — C-7M.4.3 — Computed View materially-relevant-event trigger: the clash event must be materially relevant to the profile. [V10 §7M / UPDATE TIMING]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M.4.3 — Computed View materially-relevant-event trigger | The relevant clash change. | Requests the affected profile's update. | Current presentation of preserved conflict. | [V10 §7M] |

SUB-PARTS: NONE

### C-7M.4.3.3 — Computed View Ness-response event trigger
Stamp: DESIGNED    Source: [V10 §7M / UPDATE TIMING] [V10 §7J]

ALONE
- What it is: DESIGNED — A relevant separate Ness response event. [V10 §7M / UPDATE TIMING] [V10 §7J]
- Takes in: DESIGNED — The response and the object or clash it addresses. [V10 §7M / UPDATE TIMING] [V10 §7J]
- Does: DESIGNED — Allows a profile update reflecting the response without rewriting source history. [V10 §7M / UPDATE TIMING] [V10 §7J]
- Gives out: DESIGNED — A Ness-response trigger reference. [V10 §7M / UPDATE TIMING] [V10 §7J]
- Must never: DESIGNED — Turn the response into a replacement for the original reading or clash. [V10 §7M / UPDATE TIMING] [V10 §7J]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J.6 — Ness response as separate event: the separate preserved response event. [V10 §7M / UPDATE TIMING] [V10 §7J]
- Gated by: DESIGNED — C-7M.4.3 — Computed View materially-relevant-event trigger: the response must be materially relevant to the profile. [V10 §7M / UPDATE TIMING] [V10 §7J]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M.4.3 — Computed View materially-relevant-event trigger | The relevant response event. | Requests current-use reconsideration under the profile. | A response-triggered update. | [V10 §7M] |

SUB-PARTS: NONE

### C-7M.4.3.4 — Computed View theme-confirmation trigger
Stamp: DESIGNED    Source: [V10 §7M / UPDATE TIMING]

ALONE
- What it is: DESIGNED — A theme confirmation materially relevant to the profile. [V10 §7M / UPDATE TIMING]
- Takes in: DESIGNED — The confirmed theme and its confirmation event. [V10 §7M / UPDATE TIMING]
- Does: DESIGNED — Allows the affected profile to update its navigation/current picture. [V10 §7M / UPDATE TIMING]
- Gives out: DESIGNED — A theme-confirmation trigger. [V10 §7M / UPDATE TIMING]
- Must never: DESIGNED — Treat a theme confirmation as a fact about its member material. [V10 §7M / UPDATE TIMING]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7K.6.6.1 — confirm theme: Ness's recorded theme confirmation. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gated by: DESIGNED — C-7M.4.3 — Computed View materially-relevant-event trigger: the confirmation must be materially relevant to the profile. [V10 §7M / UPDATE TIMING]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M.4.3 — Computed View materially-relevant-event trigger | A relevant theme confirmation. | Requests the affected profile's update. | Updated navigation without factual promotion. | [V10 §7M] |

SUB-PARTS: NONE

### C-7M.4.3.5 — Computed View identity-resolution trigger
Stamp: DESIGNED    Source: [V10 §7M / UPDATE TIMING] [V10 §7L]

ALONE
- What it is: DESIGNED — An identity resolution materially relevant to the profile. [V10 §7M / UPDATE TIMING] [V10 §7L]
- Takes in: DESIGNED — The authorized Person-Box resolution and its append-only history. [V10 §7M / UPDATE TIMING] [V10 §7L]
- Does: DESIGNED — Allows the affected current picture to use the resolved identity links while preserving prior references. [V10 §7M / UPDATE TIMING] [V10 §7L]
- Gives out: DESIGNED — An identity-resolution trigger. [V10 §7M / UPDATE TIMING] [V10 §7L]
- Must never: DESIGNED — Rewrite roots, readings or historical person links during the update. [V10 §7M / UPDATE TIMING] [V10 §7L]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7L.3 — Person-Box proposal and identity events: the accepted identity resolution and event history. [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12]
- Gated by: DESIGNED — C-7M.4.3 — Computed View materially-relevant-event trigger: the resolution must be materially relevant to the profile. [V10 §7M / UPDATE TIMING] [V10 §7L]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M.4.3 — Computed View materially-relevant-event trigger | The relevant identity resolution. | Requests an affected-profile update. | Current use of preserved identity links. | [V10 §7M] |

SUB-PARTS: NONE

### C-7M.4.3.6 — Computed View other declared-event trigger
Stamp: DESIGNED    Source: [V10 §7M / UPDATE TIMING]

ALONE
- What it is: DESIGNED — Another event explicitly defined as relevant to the particular view profile. [V10 §7M / UPDATE TIMING]
- Takes in: DESIGNED — The event and the profile rule that declares its relevance. [V10 §7M / UPDATE TIMING]
- Does: DESIGNED — Allows the profile-specific trigger only through that explicit declaration. [V10 §7M / UPDATE TIMING]
- Gives out: DESIGNED — A declared other-event trigger. [V10 §7M / UPDATE TIMING]
- Must never: DESIGNED — Guess a new event class into relevance or treat unrelated material as a trigger. [V10 §7M / UPDATE TIMING]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7M.4.3 — Computed View materially-relevant-event trigger: the event must be explicitly defined as materially relevant to this profile. [V10 §7M / UPDATE TIMING]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M.4.3 — Computed View materially-relevant-event trigger | An explicitly profile-relevant event. | Uses the declared trigger condition. | A bounded additional event route. | [V10 §7M] |

SUB-PARTS: NONE

### C-7M.5 — Computed View immutable snapshot record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The immutable record of a completed current-picture assembly. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — snapshot_id; operation_id; exact view_profile_id/profile_version; trigger type/object; authorization/purpose basis; ten distinct source-reference fields; separate results for all seven ordering factors; visible clashes/uncertainty; omitted candidates and reasons; prior snapshot reference; changed-from-prior description and why; derivation_rule_version; created_at; committed completeness status including no clear current view; privacy/output eligibility references; operational-log references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Commits all-or-nothing at record level and preserves the actual sources, factor outcomes and explanation. Factor 2 points directly to supporting roots and counts same-event evidence families once. Keeps the snapshot forever unchanged after commit. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — One immutable snapshot with inspectable sources, derivation and honest completeness. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Store mutable standing, superseded or possibly-stale status on the snapshot; edit, mark, rewrite, invalidate or alter it after commit; copy source objects; expose partial records; collapse factor outcomes into a score. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — An incomplete, failed or unauthorized assembly never becomes a new visible snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

TOGETHER
- Fed by: ACCEPTED — C-7M.5.1 — Computed View snapshot_id: snapshot ID; C-7M.5.2 — Computed View operation_id: operation identity; C-7M.3.1 — Computed View view_profile_id: profile ID; C-7M.3.2 — Computed View profile_version: exact profile version; C-7M.5.3 — Computed View snapshot trigger reference: trigger reference; C-7M.5.4 — Computed View snapshot authorization-purpose basis: authorization/purpose basis; C-7M.5.5 — Computed View snapshot source-reference fields: ten source-reference fields; C-7M.5.6 — Computed View separate ordering-factor results: separate factor outcomes; C-7M.5.7 — Computed View snapshot clashes and uncertainty: clashes/uncertainty; C-7M.5.8 — Computed View omitted candidates and reasons: omitted candidates/reasons; C-7M.5.9 — Computed View prior snapshot reference: prior snapshot; C-7M.5.10 — Computed View changed-from-prior explanation: change description/reason; C-7M.3.16 — Computed View derivation_rule_version: derivation version; C-7M.3.17 — Computed View record created_at: creation time; C-7M.5.11 — Computed View committed completeness status: committed completeness; C-7M.5.12 — Computed View privacy-output eligibility references: privacy/output eligibility; C-7M.3.19 — Computed View operational-log references: operational-log references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-7M.3 — Computed View ordering-profile record: the exact profile must be valid, current and authorized; C-7M.8 — Computed View duplicate prevention: the operation/source-version identity permits at most one snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M — Computed View (§7M) | The immutable completed snapshot. | Derives its standing view through later status events. | A preserved current-picture record. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7M.5.1 — Computed View snapshot_id | The immutable snapshot's complete field and source-reference contract. | Supplies snapshot identity. | A complete snapshot with no mutable standing or staleness field. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 3 · ACCEPTED | C-7M.5.2 — Computed View operation_id | The immutable snapshot's complete field and source-reference contract. | Supplies the snapshot's operation identity. | A complete snapshot with no mutable standing or staleness field. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 4 · ACCEPTED | C-7M.5.3 — Computed View snapshot trigger reference | The immutable snapshot's complete field and source-reference contract. | Supplies trigger type and object. | A complete snapshot with no mutable standing or staleness field. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 5 · ACCEPTED | C-7M.5.4 — Computed View snapshot authorization-purpose basis | The immutable snapshot's complete field and source-reference contract. | Supplies the snapshot's authorization/purpose basis. | A complete snapshot with no mutable standing or staleness field. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] |
| 6 · ACCEPTED | C-7M.5.5 — Computed View snapshot source-reference fields | The immutable snapshot's complete field and source-reference contract. | Supplies the ten source-reference fields. | A complete snapshot with no mutable standing or staleness field. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 7 · ACCEPTED | C-7M.5.6 — Computed View separate ordering-factor results | The immutable snapshot's complete field and source-reference contract. | Supplies the seven separate factor outcomes. | A complete snapshot with no mutable standing or staleness field. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 8 · ACCEPTED | C-7M.5.7 — Computed View snapshot clashes and uncertainty | The immutable snapshot's complete field and source-reference contract. | Supplies visible clash and uncertainty qualifications. | A complete snapshot with no mutable standing or staleness field. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] |
| 9 · ACCEPTED | C-7M.5.8 — Computed View omitted candidates and reasons | The immutable snapshot's complete field and source-reference contract. | Supplies omitted candidates and their reasons. | A complete snapshot with no mutable standing or staleness field. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 10 · ACCEPTED | C-7M.5.9 — Computed View prior snapshot reference | The immutable snapshot's complete field and source-reference contract. | Supplies the prior snapshot link. | A complete snapshot with no mutable standing or staleness field. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 11 · ACCEPTED | C-7M.5.10 — Computed View changed-from-prior explanation | The immutable snapshot's complete field and source-reference contract. | Supplies the changed-from-prior explanation. | A complete snapshot with no mutable standing or staleness field. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [V10 §7M / UPDATE TIMING] |
| 12 · ACCEPTED | C-7M.5.11 — Computed View committed completeness status | The immutable snapshot's complete field and source-reference contract. | Supplies the immutable completeness result. | A complete snapshot with no mutable standing or staleness field. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 13 · ACCEPTED | C-7M.5.12 — Computed View privacy-output eligibility references | The immutable snapshot's complete field and source-reference contract. | Supplies the privacy/output eligibility references. | A complete snapshot with no mutable standing or staleness field. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] |
| 14 · ACCEPTED | C-7M.7.1 — Computed View successful refresh | The committed snapshot and its immutable provenance. | Supplies the committed immutable snapshot. | A traceable committed picture without source mutation. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 15 · ACCEPTED | C-7M.10.11 — Computed View relevance evaluation record | The committed snapshot and its immutable provenance. | Supplies the snapshot detail. | A traceable committed picture without source mutation. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] |

SUB-PARTS: C-7M.5.1 — Computed View snapshot_id; C-7M.5.2 — Computed View operation_id; C-7M.5.3 — Computed View snapshot trigger reference; C-7M.5.4 — Computed View snapshot authorization-purpose basis; C-7M.5.5 — Computed View snapshot source-reference fields; C-7M.5.6 — Computed View separate ordering-factor results; C-7M.5.7 — Computed View snapshot clashes and uncertainty; C-7M.5.8 — Computed View omitted candidates and reasons; C-7M.5.9 — Computed View prior snapshot reference; C-7M.5.10 — Computed View changed-from-prior explanation; C-7M.5.11 — Computed View committed completeness status; C-7M.5.12 — Computed View privacy-output eligibility references

### C-7M.5.1 — Computed View snapshot_id
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The snapshot_id identifying one committed immutable snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The snapshot's own stable record identity. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Provides the reference used by status events and later snapshot history. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — An exact snapshot reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Use a new ID to duplicate the same completed operation/source-version outcome. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7M.8 — Computed View duplicate prevention: a completed operation and source/version set yield at most one snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Changes: ACCEPTED — C-7M.5 — Computed View immutable snapshot record: supplies snapshot identity. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5 — Computed View immutable snapshot record | The snapshot ID. | Keeps the committed picture individually addressable. | Stable snapshot identity. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7M.6.4 — Computed View standing_snapshot_id | The immutable snapshot identity. | Records the last valid standing snapshot, or the newly standing one on success. | A standing relationship outside the snapshot. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.5.2 — Computed View operation_id
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The stable operation_id carried by a view operation and its resulting records. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Takes in: ACCEPTED — The logical operation identity plus its exact source/version set, including view_profile_id and profile_version. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Does: ACCEPTED — Keeps one operation identifiable across snapshot, refresh/status event, retry and reconciliation records; idempotency is derived from the operation and source/version set. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Gives out: ACCEPTED — A stable operation reference and duplicate-prevention scope. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Must never: ACCEPTED — Treat an attempt, retry or reconciliation as permission to duplicate a committed outcome. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7M.8 — Computed View duplicate prevention: re-runs resolve to the existing committed outcome under the same identity. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Changes: ACCEPTED — C-7M.5 — Computed View immutable snapshot record: supplies the snapshot's operation identity. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5 — Computed View immutable snapshot record | The operation ID. | Binds the snapshot to its single logical assembly. | Operation-attributable snapshot identity. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7M.6 — Computed View refresh-status event | The stable operation_id. | Supplies `operation_id`. | One operation identity without merged record kinds or repeated commitment. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 3 · ACCEPTED | C-7M.8 — Computed View duplicate prevention | The stable operation_id. | Supplies the operation identity. | One operation identity without merged record kinds or repeated commitment. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 4 · ACCEPTED | C-7M.9 — Computed View operation and recovery contract | The stable operation_id. | Supplies the operation identity. | One operation identity without merged record kinds or repeated commitment. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 5 · ACCEPTED | C-7M.11.2 — Computed View domain-log level separation | The stable operation_id. | Supplies the shared operation identity. | One operation identity without merged record kinds or repeated commitment. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.1] |
| 6 · ACCEPTED | C-7M.11.4 — Bundle 4 operational-record lifecycle-status event | The stable operation_id. | Supplies `operation_id`. | One operation identity without merged record kinds or repeated commitment. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 7 · ACCEPTED | C-7N.11.5 — Surfacing partial-completion representation | The actual completed and uncompleted portions. | Supplies what this place relies on: the operation identity whose completed and uncompleted portions are recorded. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 8 · ACCEPTED | C-7N.12.2 — Surfacing domain-operation and log-write levels | The actual domain operation and the append recording it, linked by the same operation identity. | Supplies shared operation identity. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 9 · ACCEPTED | C-7O.10 — Result-return operation integrity | A stable operation identity, source/version set, actual committed records and the action's true effect state. | Supplies shared operation_id. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.2] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 10 · ACCEPTED | C-7D.17 — B6 operation integrity and recordkeeping | Stable identity, source/version set, declared commit boundary and actual committed outcome. | Supplies operation identity. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 11 · ACCEPTED | C-7D.9 — B6 common record contract | Immediate source IDs, direct roots, full derivation and evidence-family identities. | Supplies operation identity. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] |
| 12 · ACCEPTED | C-7N.11.2 — Surfacing record-level commit boundary | The complete record prepared for the operation. | Supplies the stable operation identity to which this record-level commit belongs. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 13 · ACCEPTED | C-7N.11.1 — Surfacing source-version idempotency | The stable operation identity plus its source/version set. | Supplies stable operation_id. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 14 · ACCEPTED | C-7D.17.1 — B6 operation idempotency | Operation identity plus the source/version set. | Supplies stable operation identity. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 15 · ACCEPTED | C-7P.13.1 — Authority-record operation and recovery contract | Stable operation identity, source/version set, commit boundary and existing or interrupted outcome. | Supplies the canonical operation_id. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 16 · ACCEPTED | C-7D.16.5 — World active-core membership event | membership_event_id, world_object_or_condition_id, operation_id, previous_membership, new_membership, basis_type, basis_reference, purpose_scope, supporting_evidence_references, grounding_status, reason, authorization_reference, created_at, supersedes_or_relates_to_event and operational_log_reference. | Supplies `operation_id`. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §6] |
| 17 · ACCEPTED | C-7D.16.6.3 — World membership idempotent evaluation | The same object, basis, purpose and source-version set. | Supplies stable operation identity. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §6] |
| 18 · ACCEPTED | C-7N.11 — Surfacing and presentation operation integrity | A stable operation identity, source/version set and an explicitly bounded operation. | Supplies the shared operation_id. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 19 · ACCEPTED | C-7N.12.1 — Surfacing operational-record content | What was evaluated, used, not used, omitted or set aside and why. | Supplies `operation_id`. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.5.3 — Computed View snapshot trigger reference
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The snapshot's trigger type and trigger object. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The exact update trigger that caused the assembly. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Records both what kind of trigger occurred and the object/request that supplied it. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — Inspectable trigger provenance. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Substitute an unrelated event or omit why the refresh occurred. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7M.4 — Computed View update triggers: the opened, manual or materially relevant event trigger. [V10 §7M]
- Fed by: ACCEPTED — C-7M.5.3.1 — Computed View snapshot trigger type: trigger type; C-7M.5.3.2 — Computed View snapshot trigger object: trigger object or request reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.5 — Computed View immutable snapshot record: supplies trigger type and object. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5 — Computed View immutable snapshot record | The actual trigger. | Preserves what caused the snapshot. | Traceable update provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7M.5.3.1 — Computed View snapshot trigger type | The requirement to preserve both trigger kind and actual triggering reference. | Supplies the trigger-type field. | Complete inspectable trigger provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 3 · ACCEPTED | C-7M.5.3.2 — Computed View snapshot trigger object | The requirement to preserve both trigger kind and actual triggering reference. | Supplies the trigger-object field. | Complete inspectable trigger provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: C-7M.5.3.1 — Computed View snapshot trigger type; C-7M.5.3.2 — Computed View snapshot trigger object

### C-7M.5.3.1 — Computed View snapshot trigger type
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The snapshot field identifying what kind of update triggered assembly. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The actual opening, manual-refresh or materially relevant event kind. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Records the trigger type separately from the object or request that supplied it. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — The snapshot's trigger type. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Substitute an unrelated kind or treat a type label as the triggering object. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.5.3 — Computed View snapshot trigger reference: supplies the trigger-type field. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5.3 — Computed View snapshot trigger reference | The actual update kind. | Preserves what kind of event or request caused this picture. | Typed trigger provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.5.3.2 — Computed View snapshot trigger object
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The snapshot reference identifying the object or request that triggered assembly. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The actual trigger object or request associated with the recorded trigger type. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Preserves that specific reference without replacing it with a later event. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — The snapshot's trigger object reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Omit the actual trigger reference or substitute a generic type label for it. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.5.3 — Computed View snapshot trigger reference: supplies the trigger-object field. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5.3 — Computed View snapshot trigger reference | The actual triggering object or request. | Keeps the update's originating reference inspectable. | Specific trigger provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.5.4 — Computed View snapshot authorization-purpose basis
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The snapshot's authorization/purpose basis, including the internal-use authorization reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Takes in: ACCEPTED — The actual purpose and privacy authorization for assembly. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Does: ACCEPTED — Records the permitted internal-use basis without treating it as evidence or later disclosure permission. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Gives out: ACCEPTED — An inspectable assembly-authorization reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Must never: ACCEPTED — Let an authorization decision validate the contents or widen access through the snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — Unauthorized assembly produces no snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the actual internal-use purpose and material must be authorized before assembly. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Changes: ACCEPTED — C-7M.5 — Computed View immutable snapshot record: supplies the snapshot's authorization/purpose basis. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5 — Computed View immutable snapshot record | The internal-use authorization reference. | Preserves the assembly's permitted scope. | A purpose-bounded snapshot. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.5.5 — Computed View snapshot source-reference fields
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — Ten separate source-reference fields, one per permitted source family. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — Direct root, reading, telling, clash, Ness-response-event, Person-Box-link, theme, Living State, world-model and safe metadata-only pre-ingest references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Links each source object by its own ID without copying it or merging distinct evidence types. Keeps direct roots explicit even when other source objects point to them. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — A fully inspectable source-reference set with ten distinct families. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Copy source payloads, invent a source family, replace direct roots with repetitive derivatives or admit held raw material through metadata. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Telling-specific use remains blocked until complete-set eligibility holds; held raw pre-ingest material stays outside the snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1]

TOGETHER
- Fed by: ACCEPTED — C-7M.5.5.1 — Computed View direct-root references: direct roots; C-7M.5.5.2 — Computed View reading references: readings; C-7M.5.5.3 — Computed View telling references: tellings; C-7M.5.5.4 — Computed View clash references: clashes; C-7M.5.5.5 — Computed View Ness-response references: Ness responses; C-7M.5.5.6 — Computed View Person-Box-link references: Person-Box links; C-7M.5.5.7 — Computed View theme references: themes; C-7M.5.5.8 — Computed View Living-State references: Living State; C-7M.5.5.9 — Computed View world-model references: world model; C-7M.5.5.10 — Computed View safe pre-ingest metadata references: safe pre-ingest metadata. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-7M.3.7 — Computed View eligible source-reference families: the profile must declare these families eligible; C-7M.13 — Computed View metadata-only held-content boundary: held references contain only safe metadata, lifecycle state and blockers. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Changes: ACCEPTED — C-7M.5 — Computed View immutable snapshot record: supplies the ten source-reference fields. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5 — Computed View immutable snapshot record | The linked source objects by family. | Preserves exactly which sources informed the picture. | Inspectable source provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7M.3.7 — Computed View eligible source-reference families | The ten permitted source families. | Limits the profile's eligible-family declaration. | No invented family. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 3 · ACCEPTED | C-7M.5.5.1 — Computed View direct-root references | The ten separately identified source-reference families. | Supplies direct-root source references. | Source-family provenance remains explicit and separate. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 4 · ACCEPTED | C-7M.5.5.2 — Computed View reading references | The ten separately identified source-reference families. | Supplies reading source references. | Source-family provenance remains explicit and separate. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 5 · ACCEPTED | C-7M.5.5.3 — Computed View telling references | The ten separately identified source-reference families. | Supplies telling source references. | Source-family provenance remains explicit and separate. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] |
| 6 · ACCEPTED | C-7M.5.5.4 — Computed View clash references | The ten separately identified source-reference families. | Supplies clash source references. | Source-family provenance remains explicit and separate. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] |
| 7 · ACCEPTED | C-7M.5.5.5 — Computed View Ness-response references | The ten separately identified source-reference families. | Supplies Ness-response source references. | Source-family provenance remains explicit and separate. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] |
| 8 · ACCEPTED | C-7M.5.5.6 — Computed View Person-Box-link references | The ten separately identified source-reference families. | Supplies Person-Box-link source references. | Source-family provenance remains explicit and separate. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 9 · ACCEPTED | C-7M.5.5.7 — Computed View theme references | The ten separately identified source-reference families. | Supplies theme source references. | Source-family provenance remains explicit and separate. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| 10 · ACCEPTED | C-7M.5.5.8 — Computed View Living-State references | The ten separately identified source-reference families. | Supplies Living State source references. | Source-family provenance remains explicit and separate. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] |
| 11 · ACCEPTED | C-7M.5.5.9 — Computed View world-model references | The ten separately identified source-reference families. | Supplies world-model source references. | Source-family provenance remains explicit and separate. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] |
| 12 · ACCEPTED | C-7M.5.5.10 — Computed View safe pre-ingest metadata references | The ten separately identified source-reference families. | Supplies metadata-only pre-ingest references. | Source-family provenance remains explicit and separate. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] |
| 13 · ACCEPTED | C-7M.8 — Computed View duplicate prevention | The exact source-reference set used by assembly. | Includes that set in the operation/source-version identity. | Idempotent resolution without source collapse. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |

SUB-PARTS: C-7M.5.5.1 — Computed View direct-root references; C-7M.5.5.2 — Computed View reading references; C-7M.5.5.3 — Computed View telling references; C-7M.5.5.4 — Computed View clash references; C-7M.5.5.5 — Computed View Ness-response references; C-7M.5.5.6 — Computed View Person-Box-link references; C-7M.5.5.7 — Computed View theme references; C-7M.5.5.8 — Computed View Living-State references; C-7M.5.5.9 — Computed View world-model references; C-7M.5.5.10 — Computed View safe pre-ingest metadata references

### C-7M.5.5.1 — Computed View direct-root references
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The snapshot's distinct direct-root reference field. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — IDs of directly supporting roots. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Preserves direct root pointers, including those supporting factor 2's evidence result. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — Inspectable direct-root references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Copy roots or replace direct support with repeated derivative claims. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: BUILT — C-STORE — Accretive store & sealed roots (§6B): the original immutable roots. [V10 §6A] [V10 §6B]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.5.5 — Computed View snapshot source-reference fields: supplies direct-root source references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5.5 — Computed View snapshot source-reference fields | Original root IDs. | Keeps direct evidence separately addressable. | Direct-source traceability. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.5.5.2 — Computed View reading references
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The snapshot's distinct reading-reference field. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — IDs of the source readings used in assembly. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Preserves reading identity without copying or rewriting the interpretation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — Inspectable reading references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Turn a referenced reading into a new interpretation or a settled fact. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: BUILT — C-READ — Reading record, validator, writer (§6B): immutable reading records and their source links. [V10 §6B]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.5.5 — Computed View snapshot source-reference fields: supplies reading source references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5.5 — Computed View snapshot source-reference fields | Source reading IDs. | Keeps the interpretations separately linked. | Reading provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.5.5.3 — Computed View telling references
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The snapshot's distinct first-class telling-reference field. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]
- Takes in: ACCEPTED — Eligible telling_id values and their parent-reading/root chains. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]
- Does: ACCEPTED — Links the telling where it is stored without copying it or losing perspective and firmness limits. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]
- Gives out: ACCEPTED — Inspectable first-class telling references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]
- Must never: ACCEPTED — Use partial or invalid telling sets for semantic assembly or promote the telling to fact. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Telling-specific assembly is blocked until the complete valid telling-set condition or legitimate zero-telling result holds. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-READ.10.14.4 — Computed View references: the existing Computed View telling-reference interface. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-READ.10.10.12 — Computed View use eligibility: complete-set eligibility before telling-specific Computed View use. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]
- Changes: ACCEPTED — C-7M.5.5 — Computed View snapshot source-reference fields: supplies telling source references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5.5 — Computed View snapshot source-reference fields | Eligible stable telling IDs. | Preserves their original source chains. | Perspective-aware telling provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7M.5.5.4 — Computed View clash references
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The snapshot's distinct clash-reference field. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Takes in: ACCEPTED — Preserved clash record IDs and their source links. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Does: ACCEPTED — Keeps clashes addressable and visibly associated with affected items. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Gives out: ACCEPTED — Inspectable clash references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Must never: ACCEPTED — Resolve, erase or suppress a clash through current-picture assembly. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Conflicted support remains qualified rather than silently treated as clean. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]

TOGETHER
- Fed by: DESIGNED — C-7J — Clash Handling (§7J): preserved clash records. [V10 §7J] [V10 §7M]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.5.5 — Computed View snapshot source-reference fields: supplies clash source references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5.5 — Computed View snapshot source-reference fields | Clash record IDs. | Keeps conflict provenance distinct. | Visible preserved clashes. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.5.5.5 — Computed View Ness-response references
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The snapshot's distinct Ness-response-event reference field. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Takes in: ACCEPTED — IDs of relevant separate Ness response events. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Does: ACCEPTED — Preserves explicit judgment as its own source family, distinct from the roots, readings and clashes it concerns. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Gives out: ACCEPTED — Inspectable response-event references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Must never: ACCEPTED — Treat a response as a rewrite of the original evidence. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7J.6 — Ness response as separate event: separate preserved response events. [V10 §7J] [V10 §7M]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.5.5 — Computed View snapshot source-reference fields: supplies Ness-response source references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5.5 — Computed View snapshot source-reference fields | Response event IDs. | Keeps judgment separate from original material. | Traceable explicit-response support. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.5.5.6 — Computed View Person-Box-link references
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The snapshot's distinct Person-Box-link reference field. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — IDs of person-related links with their actual certainty and provenance. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Preserves person identity organization through references without synthesizing a person profile. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — Inspectable Person-Box-link references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Rewrite identity links or convert the current view into a fixed personality description. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7L — Person-Boxes (§7L): stable identity anchors and provenance-bearing person links. [V10 §7L] [V10 §7M]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.5.5 — Computed View snapshot source-reference fields: supplies Person-Box-link source references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5.5 — Computed View snapshot source-reference fields | Person-link IDs. | Keeps identity provenance inspectable. | Person-focused source navigation. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.5.5.7 — Computed View theme references
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The snapshot's distinct theme-reference field. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Takes in: ACCEPTED — Theme IDs with their proposed or confirmed status and source support. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Does: ACCEPTED — Keeps themes as navigational categories with their actual status. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gives out: ACCEPTED — Inspectable theme references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Must never: ACCEPTED — Confirm a theme through use, frequency or placement in the current picture. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7K.6.1 — Theme record: stable theme records and version/status history. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.5.5 — Computed View snapshot source-reference fields: supplies theme source references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5.5 — Computed View snapshot source-reference fields | Theme IDs and statuses. | Preserves navigation without factual promotion. | Theme provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-7M.5.5.8 — Computed View Living-State references
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The snapshot's distinct Living State reference field. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]
- Takes in: ACCEPTED — Grounded state objects with their recorded currentness and evidence chains. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]
- Does: ACCEPTED — Uses state as an upstream source while preserving the distinction between state evidence and view-derived organization. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]
- Gives out: ACCEPTED — Inspectable Living State references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]
- Must never: ACCEPTED — Return the Computed View to Living State as evidence or let relevance supply currentness. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7D — Living State Web (§7D): grounded state objects and recorded currentness. [V10 §7D] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.5.5 — Computed View snapshot source-reference fields: supplies Living State source references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5.5 — Computed View snapshot source-reference fields | State object IDs. | Keeps the dependency strictly downstream from state to view. | Grounded state context without a feedback vote. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-7M.5.5.9 — Computed View world-model references
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The snapshot's distinct world-model reference field. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]
- Takes in: ACCEPTED — Permitted world-model source objects with their preserved grounding. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]
- Does: ACCEPTED — Links those objects separately from Living State and from the visual world presentation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]
- Gives out: ACCEPTED — Inspectable world-model source references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]
- Must never: ACCEPTED — Treat a visual presentation as a new world fact or let a snapshot validate the model that supplied it. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7D — Living State Web (§7D): the layered world-model source objects under its grounding rules. [MAP C-7D] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §6] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.5.5 — Computed View snapshot source-reference fields: supplies world-model source references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5.5 — Computed View snapshot source-reference fields | World-model object IDs. | Keeps their source family distinct. | Grounded world context without self-validation. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.5.5.10 — Computed View safe pre-ingest metadata references
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The snapshot's safe metadata-only pre-ingest reference field. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]
- Takes in: ACCEPTED — Source-carried safe metadata, lifecycle state and blocker information. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]
- Does: ACCEPTED — Links those permitted metadata references while keeping held raw content outside ranking, interpretation, snapshots and output. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]
- Gives out: ACCEPTED — Inspectable safe metadata/status references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]
- Must never: ACCEPTED — Reveal or reconstruct held content from metadata or introduce any sealed TSC inspection token, mechanism or path. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Held raw material never enters the snapshot or its derivation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]

TOGETHER
- Fed by: DESIGNED — C-7E.11 — Held-content access boundary: safe held metadata with raw content excluded from semantic use. [V10 §7M] [V10 §7E]
- Gated by: ACCEPTED — C-7M.13 — Computed View metadata-only held-content boundary: only safe metadata, lifecycle state and blockers are eligible. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]
- Changes: ACCEPTED — C-7M.5.5 — Computed View snapshot source-reference fields: supplies metadata-only pre-ingest references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5.5 — Computed View snapshot source-reference fields | Safe metadata/status references. | Preserves the held-content boundary. | No indirect route to held raw content. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-7M.13 — Computed View metadata-only held-content boundary | The snapshot's metadata-only pre-ingest reference field. | Allows only safe metadata, lifecycle state and blockers into that field. | No held raw content or sealed-TSC inspection path. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.5.6 — Computed View separate ordering-factor results
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The snapshot's separately recorded result for each of the seven fixed ordering factors. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — Each factor's actual outcome, with direct-root pointers for factor 2. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Records outcomes in fixed factor order without collapsing them into one score; direct-root evidence counts each underlying-event family once. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — Seven distinguishable, explainable factor results. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Hide an aggregate truth score, substitute model confidence for root support or omit factor 2's supporting direct-root references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7M.2.1 — Computed View factor 1 — current Ness judgment: judgment result; C-7M.2.2 — Computed View factor 2 — direct root evidence: direct-root result; C-7M.2.3 — Computed View factor 3 — reading acceptance and grounding: acceptance/grounding result; C-7M.2.4 — Computed View factor 4 — purpose relevance: relevance result; C-7M.2.5 — Computed View factor 5 — context quality and provenance: context/provenance result; C-7M.2.6 — Computed View factor 6 — clashes and uncertainty: clash/uncertainty result; C-7M.2.7 — Computed View factor 7 — recency tie-breaker: limited recency result. [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.5 — Computed View immutable snapshot record: supplies the seven separate factor outcomes. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5 — Computed View immutable snapshot record | The separate factor outcomes. | Preserves why the picture was assembled this way. | Auditable priority without a hidden score. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.5.7 — Computed View snapshot clashes and uncertainty
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The snapshot's visibly carried active clashes and uncertainty. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Takes in: ACCEPTED — Clashes, unresolved uncertainty and contrary evidence associated with used items. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Does: ACCEPTED — Keeps those qualifications beside the affected items, including strongly supported ones. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Gives out: ACCEPTED — Visible conflict and uncertainty in the committed picture. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Must never: ACCEPTED — Suppress conflict, silently resolve a clash or treat conflicted support as uncontested. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Insufficiently clear support may produce no clear current view rather than a forced winner. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]

TOGETHER
- Fed by: DESIGNED — C-7M.2.6 — Computed View factor 6 — clashes and uncertainty: the conflict/uncertainty factor and beside-item requirement. [V10 §7M]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.5 — Computed View immutable snapshot record: supplies visible clash and uncertainty qualifications. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5 — Computed View immutable snapshot record | Active conflicts and uncertainty. | Preserves the actual support limitations. | An honest current picture. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.5.8 — Computed View omitted candidates and reasons
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The snapshot's record of omitted or set-aside candidates and why they were not used. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — Each considered but unused candidate and its omission reason. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Preserves the non-use explanation without deleting or weakening the original object. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — Inspectable omissions with reasons. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Omit the reason, hide a source permanently or invent missing support to avoid recording a gap. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7M.3.9.3 — Computed View profile omission rules: the profile's disclosed omission rules. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.5 — Computed View immutable snapshot record: supplies omitted candidates and their reasons. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5 — Computed View immutable snapshot record | The unused candidates and reasons. | Makes the source selection inspectable. | Honest omission provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.5.9 — Computed View prior snapshot reference
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The reference from a new snapshot to its prior snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The prior immutable picture where one exists. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Links the preserved snapshot history without modifying earlier records. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — A navigable prior-snapshot reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Overwrite the preceding picture or mark it superseded inside its immutable record. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.5 — Computed View immutable snapshot record: supplies the prior snapshot link. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5 — Computed View immutable snapshot record | The prior snapshot ID. | Keeps past pictures accessible. | Connected immutable snapshot history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7M.5.10 — Computed View changed-from-prior explanation | The prior snapshot reference. | Explains what changed from that picture and why. | Traceable comparison without rewriting the prior picture. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.5.10 — Computed View changed-from-prior explanation
Stamp: ACCEPTED    Source: [V10 §7M / UPDATE TIMING] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The snapshot's description of what changed from the prior picture and why. [V10 §7M / UPDATE TIMING] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The prior snapshot, current factor/source results and the differences found. [V10 §7M / UPDATE TIMING] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Records the change and its derivation rather than implying that time alone made the picture truer. [V10 §7M / UPDATE TIMING] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — An inspectable change description and reason. [V10 §7M / UPDATE TIMING] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Claim a successful material change when an update failed or no change was found. [V10 §7M / UPDATE TIMING] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7M.5.9 — Computed View prior snapshot reference: the prior snapshot used for comparison. [V10 §7M / UPDATE TIMING] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.5 — Computed View immutable snapshot record: supplies the changed-from-prior explanation. [V10 §7M / UPDATE TIMING] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5 — Computed View immutable snapshot record | The change and its reason. | Explains how the picture differs from its predecessor. | Traceable current-picture evolution. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.5.11 — Computed View committed completeness status
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The completeness status recorded when the snapshot commits. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The assembly's honest completeness result, including no clear current view. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Records that commit-time result once; later standing, superseded or possibly-stale status is derived from separate events. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — An immutable committed completeness status. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Edit completeness after commit or use a mutable snapshot field for freshness or standing status. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — A partial or incomplete assembly never becomes a visible half-built snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.5 — Computed View immutable snapshot record: supplies the immutable completeness result. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5 — Computed View immutable snapshot record | The commit-time completeness result. | Preserves what the assembly honestly established. | No falsely complete picture. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.5.12 — Computed View privacy-output eligibility references
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The snapshot's references to privacy and output-eligibility decisions. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Takes in: ACCEPTED — The applicable privacy and disclosure eligibility records. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Does: ACCEPTED — Preserves the eligibility basis while every actual use remains bound to current purpose and speaker authorization. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Gives out: ACCEPTED — Inspectable privacy/output references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Must never: ACCEPTED — Treat a historical reference as permission to widen current access or count eligibility as source evidence. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — Protected or unauthorized material remains unavailable to the disallowed purpose. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): actual visible use requires privacy/output eligibility first; C-SACL — Speaker Access-Control Layer (§25.4): applicable speaker access is checked afterward. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5]
- Changes: ACCEPTED — C-7M.5 — Computed View immutable snapshot record: supplies the privacy/output eligibility references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.5 — Computed View immutable snapshot record | The eligibility references. | Keeps permitted use inspectable without granting broader access. | Privacy-bound snapshot provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.6 — Computed View refresh-status event
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The append-only record of a refresh-attempt outcome, separate from the snapshot it references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The attempt's operation, exact profile/version, trigger, outcome, standing snapshot, reason, time, retry information and operational-log reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Appends one outcome event and derives standing and possible staleness from the latest valid applicable events. Reuses shared operation, creation-time and log-reference atoms. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — An immutable refresh/status event; a derived standing-view relationship. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Write standing, superseded or possibly-stale status onto a snapshot; substitute this domain event for the operation log or its lifecycle event. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — An unsuccessful or incomplete attempt records its honest outcome and retains the last valid snapshot without a falsely fresh result. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

TOGETHER
- Fed by: ACCEPTED — C-7M.5.2 — Computed View operation_id: operation_id; C-7M.3.17 — Computed View record created_at: created_at; C-7M.3.19 — Computed View operational-log references: operational_log_reference; C-7M.6.1 — Computed View event_id: event identity; C-7M.6.2 — Computed View attempted_profile_id_and_version: attempted profile/version; C-7M.6.3 — Computed View attempted_trigger: attempted trigger; C-7M.6.4 — Computed View standing_snapshot_id: standing snapshot; C-7M.6.5 — Computed View refresh outcome value: outcome; C-7M.6.6 — Computed View failure_or_incompleteness_reason: failure/incompleteness reason; C-7M.6.7 — Computed View retry_eligibility: retry eligibility; C-7M.6.8 — Computed View retry_attempt_reference: retry-attempt reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-7M.9 — Computed View operation and recovery contract: stable operation and append-only recovery rules govern event commitment. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Changes: DESIGNED — C-7M — Computed View (§7M): supplies refresh status without changing source objects or snapshots. [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M — Computed View (§7M) | Refresh outcomes and their standing-snapshot references. | Derives the standing picture and possible staleness from valid applicable events. | Current status changes only through new events. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7M.7 — Computed View refresh lifecycle | The outcome record. | Expresses each lifecycle result without mutating snapshots. | An honest standing-view relationship. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 3 · ACCEPTED | C-7M.6.1 — Computed View event_id | The append-only refresh/status event's required field contract. | Supplies event_id. | Complete honest attempt history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 4 · ACCEPTED | C-7M.6.2 — Computed View attempted_profile_id_and_version | The append-only refresh/status event's required field contract. | Binds the outcome to its attempted profile version. | Complete honest attempt history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 5 · ACCEPTED | C-7M.6.3 — Computed View attempted_trigger | The append-only refresh/status event's required field contract. | Supplies attempted_trigger. | Complete honest attempt history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 6 · ACCEPTED | C-7M.6.4 — Computed View standing_snapshot_id | The append-only refresh/status event's required field contract. | Supplies the event's standing-snapshot relationship. | Complete honest attempt history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 7 · ACCEPTED | C-7M.6.5 — Computed View refresh outcome value | The append-only refresh/status event's required field contract. | Supplies the typed outcome. | Complete honest attempt history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 8 · ACCEPTED | C-7M.6.6 — Computed View failure_or_incompleteness_reason | The append-only refresh/status event's required field contract. | Supplies the honest unsuccessful-attempt reason. | Complete honest attempt history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 9 · ACCEPTED | C-7M.6.7 — Computed View retry_eligibility | The append-only refresh/status event's required field contract. | Supplies recorded retry eligibility. | Complete honest attempt history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 10 · ACCEPTED | C-7M.6.8 — Computed View retry_attempt_reference | The append-only refresh/status event's required field contract. | Supplies retry-attempt traceability. | Complete honest attempt history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 11 · ACCEPTED | C-7M.10.11 — Computed View relevance evaluation record | The separate refresh/status domain event. | Supplies the attempt/outcome reference. | No record-kind substitution or double-counting. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] |
| 12 · ACCEPTED | C-7M.11.5 — Bundle 4 domain-log-lifecycle separation | The separate refresh/status domain event. | Supplies the refresh/status domain event. | No record-kind substitution or double-counting. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: C-7M.6.1 — Computed View event_id; C-7M.6.2 — Computed View attempted_profile_id_and_version; C-7M.6.3 — Computed View attempted_trigger; C-7M.6.4 — Computed View standing_snapshot_id; C-7M.6.5 — Computed View refresh outcome value; C-7M.6.6 — Computed View failure_or_incompleteness_reason; C-7M.6.7 — Computed View retry_eligibility; C-7M.6.8 — Computed View retry_attempt_reference

### C-7M.6.1 — Computed View event_id
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The identity field of a refresh/status event. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The event being committed. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Identifies that event independently of its operation and standing snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — event_id. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Conflate event identity with snapshot identity. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.6 — Computed View refresh-status event: supplies event_id. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.6 — Computed View refresh-status event | event_id. | Identifies the separate append-only event. | Referenceable outcome history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.6.2 — Computed View attempted_profile_id_and_version
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The exact ordering-profile record and version attempted by a refresh. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The attempted profile ID and version, even when the attempt does not produce a snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Records the exact attempted pair. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — attempted_profile_id_and_version. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Substitute the latest profile for the version actually attempted. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7M.3.1 — Computed View view_profile_id: profile identity; C-7M.3.2 — Computed View profile_version: exact version. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.6 — Computed View refresh-status event: binds the outcome to its attempted profile version. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.6 — Computed View refresh-status event | The exact attempted pair. | Preserves the basis of a successful or unsuccessful attempt. | Version-specific refresh history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.6.3 — Computed View attempted_trigger
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The refresh event's record of the attempted trigger. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The trigger that initiated this attempt. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Preserves the attempted trigger even when no snapshot commits. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — attempted_trigger. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Replace the attempted trigger with an unrelated later event. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7M.4 — Computed View update triggers: only the settled opening, manual-refresh or materially relevant event routes initiate the attempt. [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.6 — Computed View refresh-status event: supplies attempted_trigger. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.6 — Computed View refresh-status event | The attempted trigger. | Explains why this refresh was attempted. | Traceable update timing. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.6.4 — Computed View standing_snapshot_id
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The snapshot reference carried by a refresh/status event. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The last valid standing snapshot; on success, the newly standing snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — References the applicable valid snapshot while standing status is derived from event history. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — standing_snapshot_id. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Create standing status by editing the referenced snapshot or refer to a half-built picture as valid. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Failed refreshes with an older valid snapshot continue to reference that snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

TOGETHER
- Fed by: ACCEPTED — C-7M.5.1 — Computed View snapshot_id: the referenced immutable snapshot identity. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.6 — Computed View refresh-status event: supplies the event's standing-snapshot relationship. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.6 — Computed View refresh-status event | The standing-snapshot reference. | Relates the outcome to the appropriate valid picture. | Standing can change without source or snapshot mutation. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.6.5 — Computed View refresh outcome value
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The single outcome field of a refresh/status event. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The honest result or separately recorded staleness determination. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Records exactly one of success, null_update, failed, incomplete or possibly_stale. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — outcome with one of the five permitted values. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Use a fabricated freshness value or write this outcome onto a snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Failure and incompleteness remain their honest outcome classes. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

TOGETHER
- Fed by: ACCEPTED — C-7M.7 — Computed View refresh lifecycle: the outcome meanings and consequences. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.6 — Computed View refresh-status event: supplies the typed outcome. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.6 — Computed View refresh-status event | The one permitted outcome value. | Records the attempt or staleness result. | Explicit status history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.6.6 — Computed View failure_or_incompleteness_reason
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The refresh event's reason field for failure or incompleteness. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The actual failure or missing completion basis. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Records why the attempt failed or remained incomplete. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — failure_or_incompleteness_reason. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Conceal a partial result as successful completion. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — An incomplete refresh carries its reason and exposes no half-built picture. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.6 — Computed View refresh-status event: supplies the honest unsuccessful-attempt reason. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.6 — Computed View refresh-status event | The recorded reason. | Explains the unsuccessful outcome. | Visible status need not imply a fresh picture. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.6.7 — Computed View retry_eligibility
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The refresh event's technical-retry eligibility field. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Takes in: ACCEPTED — The technical failure and the governing accepted retry rules. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Does: ACCEPTED — Records whether the attempt is eligible for bounded technical retry under the existing mechanics and values. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Gives out: ACCEPTED — retry_eligibility. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Must never: ACCEPTED — Retry for interpretive disagreement or choose new retry limits here. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Only eligible technical failures can proceed to bounded retry. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]

TOGETHER
- Fed by: ACCEPTED — C-7H.9 — B9 retry-state architecture: accepted B9 retry architecture; C-7H.10 — Accepted B9 retry values and episodes: accepted B9 values and episode rules. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.6 — Computed View refresh-status event: supplies recorded retry eligibility; C-7M.9.5 — Computed View bounded technical retry: constrains the technical retry route. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.6 — Computed View refresh-status event | The eligibility result. | Records retry treatment with the outcome. | Inspectable retry basis. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7M.9.5 — Computed View bounded technical retry | Recorded eligibility. | Retries only eligible technical failures under B9. | No improvised retry policy. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7M.6.8 — Computed View retry_attempt_reference
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The reference tying a refresh/status event to its technical retry attempt. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The retry-attempt reference where applicable. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Preserves the attempt relationship alongside eligibility. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — retry_attempt_reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Hide a retry as an unrelated first attempt. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.6 — Computed View refresh-status event: supplies retry-attempt traceability; C-7M.9.5 — Computed View bounded technical retry: supplies the tracked retry reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.6 — Computed View refresh-status event | The retry reference. | Connects the outcome to retry history. | An inspectable attempt chain. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7M.9.5 — Computed View bounded technical retry | The attempt reference. | Tracks bounded technical retries. | No unrecorded retry episode. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.7 — Computed View refresh lifecycle
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The append-only lifecycle of a triggered view refresh. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — One authorized triggered refresh and its honest result. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Produces at most one new immutable snapshot plus refresh/status events. Derives the standing picture from the latest valid applicable events and retains earlier snapshots as history. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — A success, null_update, failed, incomplete or separately recorded possibly_stale event. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Invalidate, mark or rewrite any committed snapshot; expose partial writes; create a new snapshot merely to report no change. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — An unsuccessful attempt preserves the last valid picture and its honest status. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

TOGETHER
- Fed by: ACCEPTED — C-7M.6 — Computed View refresh-status event: refresh/status event; C-7M.7.1 — Computed View successful refresh: success; C-7M.7.2 — Computed View null update: null update; C-7M.7.3 — Computed View failed refresh: failure; C-7M.7.4 — Computed View incomplete refresh: incomplete; C-7M.7.5 — Computed View possible staleness: possible staleness. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-7M.8 — Computed View duplicate prevention: operation/source-version identity prevents duplicates; C-7M.9 — Computed View operation and recovery contract: recovery preserves committed outcomes. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Changes: DESIGNED — C-7M — Computed View (§7M): supplies the standing-view lifecycle. [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M — Computed View (§7M) | The derived standing view and refresh status. | Uses the current picture without altering history. | Honest current-use status. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7M.6.5 — Computed View refresh outcome value | The five lifecycle meanings. | Records the corresponding one outcome value. | An outcome that preserves its defined consequence. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 3 · ACCEPTED | C-7M.7.1 — Computed View successful refresh | The five permitted outcome meanings and append-only standing-view derivation. | Supplies the success transition. | An honest outcome with intact snapshot history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 4 · ACCEPTED | C-7M.7.2 — Computed View null update | The five permitted outcome meanings and append-only standing-view derivation. | Supplies the event-only no-change outcome. | An honest outcome with intact snapshot history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 5 · ACCEPTED | C-7M.7.3 — Computed View failed refresh | The five permitted outcome meanings and append-only standing-view derivation. | Supplies the failed outcome. | An honest outcome with intact snapshot history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 6 · ACCEPTED | C-7M.7.4 — Computed View incomplete refresh | The five permitted outcome meanings and append-only standing-view derivation. | Supplies the incomplete outcome. | An honest outcome with intact snapshot history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 7 · ACCEPTED | C-7M.7.5 — Computed View possible staleness | The five permitted outcome meanings and append-only standing-view derivation. | Supplies possible-staleness handling. | An honest outcome with intact snapshot history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 8 · ACCEPTED | C-7M.10.9.2 — Computed View relevance fallback | The valid null, failure, incomplete and staleness consequences. | Uses them for relevance fallback without silent gap-filling. | An honest limited picture or retained standing snapshot. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: C-7M.7.1 — Computed View successful refresh; C-7M.7.2 — Computed View null update; C-7M.7.3 — Computed View failed refresh; C-7M.7.4 — Computed View incomplete refresh; C-7M.7.5 — Computed View possible staleness

### C-7M.7.1 — Computed View successful refresh
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The success outcome of a completed refresh. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — A committed new snapshot and its success event. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Makes the new snapshot standing through the appended success relationship. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — success referencing the newly standing snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Rewrite or invalidate an older snapshot when the new one stands. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — A committed snapshot whose status write failed is reconciled by a missing-event append, never by rerunning the refresh. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

TOGETHER
- Fed by: ACCEPTED — C-7M.5 — Computed View immutable snapshot record: the committed immutable snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gated by: ACCEPTED — C-7M.9.2 — Computed View committed-outcome reconciliation: committed-but-unrecorded recovery preserves the snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Changes: ACCEPTED — C-7M.7 — Computed View refresh lifecycle: supplies the success transition. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.7 — Computed View refresh lifecycle | A committed snapshot and success relationship. | Derives the new standing view. | Earlier snapshots remain intact history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.7.2 — Computed View null update
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The valid no-change refresh outcome. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — A refresh finding nothing changed and the unchanged standing snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Commits a null_update event referencing that snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — null_update with no new snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Duplicate the standing snapshot or treat a valid no-change result as a failure. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.7 — Computed View refresh lifecycle: supplies the event-only no-change outcome. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.7 — Computed View refresh lifecycle | The no-change event. | Keeps the same picture standing. | A valid completed refresh without snapshot duplication. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.7.3 — Computed View failed refresh
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The failed outcome of a refresh attempt. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The actual failure and the last valid standing snapshot, when one exists. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Appends a failed event pointing to that snapshot; the interface derives possible staleness from the later event. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — failed with the honest reason and retained standing relationship. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Mark the old snapshot, replace it with a partial result or imply the failed attempt refreshed it. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — The last valid picture remains standing and is visibly possibly stale. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.7 — Computed View refresh lifecycle: supplies the failed outcome. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.7 — Computed View refresh lifecycle | The failed event and last valid reference. | Keeps the last valid picture with honest possible staleness. | No falsely fresh snapshot. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.7.4 — Computed View incomplete refresh
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The outcome of a refresh that cannot finish. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The incomplete attempt and its reason. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Commits an incomplete event and exposes no half-built picture. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — incomplete with the reason. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Make partial record writes visible or count incompleteness as success. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Record-level commit remains all-or-nothing and the last valid picture stands. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.7 — Computed View refresh lifecycle: supplies the incomplete outcome. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.7 — Computed View refresh lifecycle | The incomplete event and reason. | Preserves the honest attempt state. | No half-built standing picture. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.7.5 — Computed View possible staleness
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — A derived freshness warning, recorded separately when the staleness determination itself is recorded. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — Valid applicable later refresh/status events concerning the standing snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Derives possibly stale from event history; appends a distinct possibly_stale event where that determination is itself recorded. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — Honest possible-staleness status outside the snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Add or change a staleness field on an immutable snapshot or silently refresh its apparent age. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — When freshness cannot be established, the honest event and visibly aged last valid picture remain. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.7 — Computed View refresh lifecycle: supplies possible-staleness handling. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.7 — Computed View refresh lifecycle | The staleness determination or its event. | Shows the standing picture's honest freshness limitation. | No snapshot mutation. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.8 — Computed View duplicate prevention
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The idempotent commitment rule for a view refresh. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Takes in: ACCEPTED — A stable operation identity and the source/version set, including exact view_profile_id and profile_version. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Does: ACCEPTED — Allows at most one snapshot for one completed operation and source/version set; reruns resolve to the committed outcome. Null, failed and incomplete results create events only. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Gives out: ACCEPTED — One preserved committed outcome without duplicate snapshots. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Must never: ACCEPTED — Remove, hide, merge, overwrite or collapse committed records to deduplicate them; create a falsely fresh snapshot on a failed or no-change attempt. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — A committed outcome missing a later status or operational record receives that missing record by append-only reconciliation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]

TOGETHER
- Fed by: ACCEPTED — C-7M.5.2 — Computed View operation_id: operation identity; C-7M.3.1 — Computed View view_profile_id: exact profile ID; C-7M.3.2 — Computed View profile_version: profile version; C-7M.5.5 — Computed View snapshot source-reference fields: source references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Gated by: ACCEPTED — C-7M.9 — Computed View operation and recovery contract: declared commit and recovery boundaries preserve the outcome. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Changes: DESIGNED — C-7M — Computed View (§7M): prevents repeated attempts from duplicating a picture. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M — Computed View (§7M) | The operation/source-version commitment rule. | Resolves repeated work to its recorded outcome. | No extra snapshot or evidence strength. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7M.7 — Computed View refresh lifecycle | The at-most-one snapshot rule. | Keeps null and unsuccessful outcomes event-only. | No duplicate standing picture. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 3 · ACCEPTED | C-7M.5 — Computed View immutable snapshot record | One completed operation plus one source/version set permits at most one snapshot. | The operation/source-version identity permits at most one snapshot. | No duplicate, edited or falsely fresh snapshot. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 4 · ACCEPTED | C-7M.5.1 — Computed View snapshot_id | One completed operation plus one source/version set permits at most one snapshot. | A completed operation and source/version set yield at most one snapshot. | No duplicate, edited or falsely fresh snapshot. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 5 · ACCEPTED | C-7M.5.2 — Computed View operation_id | One completed operation plus one source/version set permits at most one snapshot. | Re-runs resolve to the existing committed outcome under the same identity. | No duplicate, edited or falsely fresh snapshot. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 6 · ACCEPTED | C-7M.9 — Computed View operation and recovery contract | One completed operation plus one source/version set permits at most one snapshot. | Idempotent commitment. | No duplicate, edited or falsely fresh snapshot. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 7 · ACCEPTED | C-7M.9.5 — Computed View bounded technical retry | One completed operation plus one source/version set permits at most one snapshot. | Supplies the committed-outcome identity. | No duplicate, edited or falsely fresh snapshot. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7M.9 — Computed View operation and recovery contract
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The stable operation, commit, recovery and retry boundary for view work and status evaluation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Takes in: ACCEPTED — The operation identity, exact source/version set, declared record-level commit boundary and observed completion state. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Does: ACCEPTED — Commits once and all-or-nothing at record level; detects in-flight work without an outcome at startup; records honest failure/incompleteness; appends missing status or operational records for already committed outcomes. Treats status evaluation itself as one recorded operation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Gives out: ACCEPTED — A committed honest outcome, recovered append-only relationships and bounded technical retry where eligible. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Must never: ACCEPTED — Assume success after interruption, rerun an already committed outcome, expose silent halves, choose new B9 values or merge a domain operation with its separate Level-2 operational-log write. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Uncertain completion remains honest; uncertain active/cold eligibility preserves previous status and records failed evaluation. An uncertain outside effect, if encountered by an applicable operation, freezes for reconciliation and never retries blindly. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]

TOGETHER
- Fed by: ACCEPTED — C-7M.9.1 — Computed View crash before snapshot commit: precommit crash; C-7M.9.2 — Computed View committed-outcome reconciliation: missing-record reconciliation; C-7M.9.3 — Computed View failure with an older valid snapshot: failure with older snapshot; C-7M.9.4 — Computed View partial-refresh recovery: partial refresh; C-7M.9.5 — Computed View bounded technical retry: bounded technical retry; C-7M.9.6 — Computed View unestablished freshness: freshness uncertainty; C-7M.5.2 — Computed View operation_id: operation identity. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Gated by: ACCEPTED — C-7H.9 — B9 retry-state architecture: accepted B9 mechanics; C-7H.10 — Accepted B9 retry values and episodes: recorded B9 values; C-7M.8 — Computed View duplicate prevention: idempotent commitment; C-7M.11 — Computed View operational records and lifecycle: separate append-only operational record. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Changes: DESIGNED — C-7M — Computed View (§7M): supplies honest recovery without rewriting a picture. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M — Computed View (§7M) | The operation's durable outcome and recovery record. | Uses only committed honest pictures and statuses. | No apparent success manufactured by restart. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-7M.6 — Computed View refresh-status event | The record-level operation contract. | Commits or reconciles an append-only refresh/status event. | A recoverable outcome relationship. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 3 · ACCEPTED | C-7M.7 — Computed View refresh lifecycle | Recovery limits. | Preserves correct lifecycle results across interruption. | No invented standing picture. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 4 · ACCEPTED | C-7M.8 — Computed View duplicate prevention | Stable commitment and reconciliation. | Resolves reruns to the recorded outcome. | No duplicate or destroyed record. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 5 · ACCEPTED | C-7M.9.1 — Computed View crash before snapshot commit | The stable-operation, all-or-nothing commitment and append-only recovery contract. | Supplies precommit-crash recovery. | No assumed success, duplicate snapshot or silent partial result. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 6 · ACCEPTED | C-7M.9.2 — Computed View committed-outcome reconciliation | The stable-operation, all-or-nothing commitment and append-only recovery contract. | Supplies committed-but-unrecorded recovery. | No assumed success, duplicate snapshot or silent partial result. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 7 · ACCEPTED | C-7M.9.3 — Computed View failure with an older valid snapshot | The stable-operation, all-or-nothing commitment and append-only recovery contract. | Supplies the older-valid-picture recovery case. | No assumed success, duplicate snapshot or silent partial result. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 8 · ACCEPTED | C-7M.9.4 — Computed View partial-refresh recovery | The stable-operation, all-or-nothing commitment and append-only recovery contract. | Supplies partial-work recovery. | No assumed success, duplicate snapshot or silent partial result. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 9 · ACCEPTED | C-7M.9.5 — Computed View bounded technical retry | The stable-operation, all-or-nothing commitment and append-only recovery contract. | Supplies bounded technical retry. | No assumed success, duplicate snapshot or silent partial result. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 10 · ACCEPTED | C-7M.9.6 — Computed View unestablished freshness | The stable-operation, all-or-nothing commitment and append-only recovery contract. | Supplies the freshness fail-closed case. | No assumed success, duplicate snapshot or silent partial result. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 11 · ACCEPTED | C-7M.11.3.5 — Computed View uncertain status evaluation | The requirement to record status evaluation as an operation. | Commits failed evaluation while preserving the previous active/cold status. | No silent lifecycle change under uncertainty. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: C-7M.9.1 — Computed View crash before snapshot commit; C-7M.9.2 — Computed View committed-outcome reconciliation; C-7M.9.3 — Computed View failure with an older valid snapshot; C-7M.9.4 — Computed View partial-refresh recovery; C-7M.9.5 — Computed View bounded technical retry; C-7M.9.6 — Computed View unestablished freshness

### C-7M.9.1 — Computed View crash before snapshot commit
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — Recovery for an interrupted attempt before a snapshot committed. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — Startup evidence of an in-flight attempt with no committed snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Appends an incomplete refresh/status event and keeps the last valid snapshot standing. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — An incomplete event; no new snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Assume that an uncommitted picture exists or expose partial writes. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — No snapshot exists for the interrupted attempt; the prior valid picture stands. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.9 — Computed View operation and recovery contract: supplies precommit-crash recovery. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.9 — Computed View operation and recovery contract | An interrupted precommit attempt. | Records incomplete and retains the prior valid picture. | No fabricated commit. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.9.2 — Computed View committed-outcome reconciliation
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — Recovery for an outcome already committed before its expected status or operational record was written. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Takes in: ACCEPTED — A committed snapshot or other outcome and the missing expected record discovered at startup. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Does: ACCEPTED — Appends the missing refresh/status or operational record by reconciliation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Gives out: ACCEPTED — The preserved committed outcome with its missing relationship supplied append-only. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Must never: ACCEPTED — Rerun the operation, edit its committed outcome or create a duplicate snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Recovery repairs only the missing record; the committed snapshot remains exactly as committed. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.9 — Computed View operation and recovery contract: supplies committed-but-unrecorded recovery. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.9 — Computed View operation and recovery contract | The committed outcome and missing-record evidence. | Reconciles by appending the missing record. | No rerun or snapshot mutation. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-7M.7.1 — Computed View successful refresh | A committed snapshot missing success status. | Restores the expected append-only status relationship. | The existing snapshot can stand without being recreated. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.9.3 — Computed View failure with an older valid snapshot
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — Recovery treatment for a failed refresh when an older valid picture exists. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The failed attempt and that valid standing snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Appends failed pointing to the older valid snapshot and derives possible staleness from the event. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — The older standing picture with honest later status. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Mark or edit the old snapshot or replace it with failed work. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — The prior valid picture remains standing, visibly possibly stale. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.9 — Computed View operation and recovery contract: supplies the older-valid-picture recovery case. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.9 — Computed View operation and recovery contract | A failed attempt with prior valid support. | Preserves the valid snapshot and records failure. | No lost history or falsely fresh picture. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.9.4 — Computed View partial-refresh recovery
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — Recovery treatment for partial or incomplete refresh work. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Takes in: ACCEPTED — The partial attempt and its actual incompleteness reason. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Does: ACCEPTED — Records incomplete honestly while the record-level commit boundary remains all-or-nothing. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Gives out: ACCEPTED — An incomplete event with its reason, no visible partial snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Must never: ACCEPTED — Expose partial writes or count them as a completed current picture. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Nothing half-built becomes visible. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.9 — Computed View operation and recovery contract: supplies partial-work recovery. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.9 — Computed View operation and recovery contract | The incomplete work and reason. | Records the honest outcome without publishing a partial record. | No silent half-completion. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.9.5 — Computed View bounded technical retry
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The bounded technical-retry route for a view attempt. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Takes in: ACCEPTED — An eligible technical failure and its recorded retry references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Does: ACCEPTED — Applies the accepted B9 mechanics and recorded values by reference, tracking eligibility and each retry attempt. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Gives out: ACCEPTED — A bounded recorded technical retry or honest non-retry outcome. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Must never: ACCEPTED — Retry interpretive disagreement, invent limits, rerun a committed snapshot or retry an uncertain outside effect. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Ineligible failures do not enter the retry route; uncertain effects freeze for reconciliation under the governing operation contract. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]

TOGETHER
- Fed by: ACCEPTED — C-7M.6.7 — Computed View retry_eligibility: retry_eligibility; C-7M.6.8 — Computed View retry_attempt_reference: retry_attempt_reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Gated by: ACCEPTED — C-7H.9 — B9 retry-state architecture: B9 mechanics; C-7H.10 — Accepted B9 retry values and episodes: accepted values and episodes; C-7M.8 — Computed View duplicate prevention: committed-outcome identity. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]
- Changes: ACCEPTED — C-7M.9 — Computed View operation and recovery contract: supplies bounded technical retry. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.9 — Computed View operation and recovery contract | The eligible technical attempt and tracked references. | Retries under the accepted limits without redefining them. | An honest bounded retry history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-7M.6.7 — Computed View retry_eligibility | The bounded technical-retry episode and its accepted limits. | Constrains the technical retry route. | Traceable technical retries without new policy values. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 3 · ACCEPTED | C-7M.6.8 — Computed View retry_attempt_reference | The bounded technical-retry episode and its accepted limits. | Supplies the tracked retry reference. | Traceable technical retries without new policy values. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7M.9.6 — Computed View unestablished freshness
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The recovery boundary when a fresh current picture cannot be established. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The available inputs, honest attempt event and last valid snapshot. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Keeps the honest event and derives the last valid snapshot as standing, visibly aged. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — The last supported picture with its disclosed freshness limitation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Fabricate a fresher picture than the inputs support or silently refresh the old one. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — The old valid picture remains visibly aged and no unsupported fresh snapshot appears. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.9 — Computed View operation and recovery contract: supplies the freshness fail-closed case. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.9 — Computed View operation and recovery contract | The unestablished freshness and prior valid picture. | Preserves the honest event and last supported snapshot. | No false freshness. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7M.10 — Computed View proposed RM-CV-01 declaration
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The accepted view-assembly relevance declaration with proposed mechanical identity RM-CV-01 and proposed declaration_version v1_0. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — The current view profile and question, authorized eligible candidates, deterministic gates and declared dimension results with producer/version provenance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Runs an A4-valid declaration for view_assembly. Keeps Tier 1 under Attention and Relevance Control and Tier 2 under the consuming view. Supplies factor 4 only, preserving all seven separate factor outcomes and every source-strength, changed-pattern and uncertainty label. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — Purpose-bound relevance for an internal current picture, plus a Decision-12 event for each assembly evaluation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Collapse factors into a score, silently change tier ownership or declaration versions, make the view evidence for itself, feed assembly into Living State, widen access or surface the picture unprompted. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Missing, invalid, stale or unauthorized profile/declaration creates the applicable failed/incomplete event and no snapshot. An unknown purpose halts rather than being guessed. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: ACCEPTED — C-7M.3 — Computed View ordering-profile record: exact ordering profile; C-7M.10.1 — Computed View proposed declaration identity and version: proposed identity/version; C-7M.10.2 — Computed View view_assembly purpose: purpose; C-7M.10.3 — Computed View relevance target: target; C-7M.3.7 — Computed View eligible source-reference families: eligible candidate families; C-7M.10.4 — Computed View deterministic context gates: gates; C-7M.10.5 — Computed View graded-dimension selection: dimensions; C-7M.10.6 — Computed View mouth-authorization boundary: no mouth authorization; C-7M.10.7 — Computed View relevance evaluation timing: timing; C-7M.10.8 — Computed View relevance-mode reason: reason; C-7M.10.9 — Computed View Tier-2 relevance rules: Tier 2; C-7M.10.10 — Computed View relevance allowed-use boundary: allowed use; C-7M.10.11 — Computed View relevance evaluation record: relevance event; C-7M.10.12 — Computed View invalid relevance declaration outcome: fail-closed behavior. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gated by: DESIGNED — C-7R — Attention & Relevance Control (§7R): owns and validates Tier 1 under the settled declaration contract; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): purpose-specific internal-use authorization precedes relevance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5]
- Gated by: ACCEPTED — C-7F.6.14 — A4 eight-field declaration validity: the existing eight-field validity contract applies before this consumer has a mode to run. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1]
- Changes: DESIGNED — C-7M — Computed View (§7M): supplies the declared relevance contribution to current assembly; C-7M.2.4 — Computed View factor 4 — purpose relevance: informs factor 4 only. [V10 §7M] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M — Computed View (§7M) | The declared view-purpose relevance result. | Uses it inside the fixed factor order. | No hidden score or authority increase. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 2 · DESIGNED | C-7M.2.4 — Computed View factor 4 — purpose relevance | Purpose-bound relevance. | Uses it as the fourth factor only. | An explicit factor contribution. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-7M.3.11 — Computed View Tier-1 configuration reference | The Tier-1 declaration reference. | Binds the profile to the declaration and exact version. | Inspectable relevance provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 4 · ACCEPTED | C-7M.3.12 — Computed View Tier-2 configuration reference | The consumer-owned Tier-2 rules. | References the ordering, fallback and surfacing contract. | No silent Tier-2 substitution. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 5 · ACCEPTED | C-7M.3.15 — Computed View unresolved-handling reference | The proposed shared unresolved-handling reference. | Preserves its identifier and version where applicable. | A declared uncertainty rule. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| 6 · ACCEPTED | C-7M.10.1 — Computed View proposed declaration identity and version | The proposed declaration's valid field, ownership and purpose contract. | Identifies the proposed declaration version. | A fully declared factor-4 relevance contribution. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 7 · ACCEPTED | C-7M.10.2 — Computed View view_assembly purpose | The proposed declaration's valid field, ownership and purpose contract. | Supplies the relevance purpose. | A fully declared factor-4 relevance contribution. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 8 · ACCEPTED | C-7M.10.3 — Computed View relevance target | The proposed declaration's valid field, ownership and purpose contract. | Supplies the target. | A fully declared factor-4 relevance contribution. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 9 · ACCEPTED | C-7M.10.4 — Computed View deterministic context gates | The proposed declaration's valid field, ownership and purpose contract. | Supplies the context-gate selection. | A fully declared factor-4 relevance contribution. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 10 · ACCEPTED | C-7M.10.5 — Computed View graded-dimension selection | The proposed declaration's valid field, ownership and purpose contract. | Supplies the declared dimension vector. | A fully declared factor-4 relevance contribution. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] |
| 11 · ACCEPTED | C-7M.10.6 — Computed View mouth-authorization boundary | The proposed declaration's valid field, ownership and purpose contract. | Supplies the explicit no-mouth authorization. | A fully declared factor-4 relevance contribution. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| 12 · ACCEPTED | C-7M.10.7 — Computed View relevance evaluation timing | The proposed declaration's valid field, ownership and purpose contract. | Supplies the declared timing. | A fully declared factor-4 relevance contribution. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 13 · ACCEPTED | C-7M.10.8 — Computed View relevance-mode reason | The proposed declaration's valid field, ownership and purpose contract. | Supplies the declared mode reason. | A fully declared factor-4 relevance contribution. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 14 · ACCEPTED | C-7M.10.9 — Computed View Tier-2 relevance rules | The proposed declaration's valid field, ownership and purpose contract. | Supplies Tier-2 rules. | A fully declared factor-4 relevance contribution. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 15 · ACCEPTED | C-7M.10.10 — Computed View relevance allowed-use boundary | The proposed declaration's valid field, ownership and purpose contract. | Supplies permitted-use limits. | A fully declared factor-4 relevance contribution. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] |
| 16 · ACCEPTED | C-7M.10.11 — Computed View relevance evaluation record | The proposed declaration's valid field, ownership and purpose contract. | Supplies evaluation traceability. | A fully declared factor-4 relevance contribution. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 17 · ACCEPTED | C-7M.10.12 — Computed View invalid relevance declaration outcome | The proposed declaration's valid field, ownership and purpose contract. | Supplies declaration failure behavior. | A fully declared factor-4 relevance contribution. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] |
| 18 · ACCEPTED | C-7R.16.2 — Computed View declaration interface | The profile question/target and declared candidate families under view_assembly. | Supplies the complete canonical proposed RM-CV-01 declaration, candidate families and local rules. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: C-7M.10.1 — Computed View proposed declaration identity and version; C-7M.10.2 — Computed View view_assembly purpose; C-7M.10.3 — Computed View relevance target; C-7M.10.4 — Computed View deterministic context gates; C-7M.10.5 — Computed View graded-dimension selection; C-7M.10.6 — Computed View mouth-authorization boundary; C-7M.10.7 — Computed View relevance evaluation timing; C-7M.10.8 — Computed View relevance-mode reason; C-7M.10.9 — Computed View Tier-2 relevance rules; C-7M.10.10 — Computed View relevance allowed-use boundary; C-7M.10.11 — Computed View relevance evaluation record; C-7M.10.12 — Computed View invalid relevance declaration outcome

### C-7M.10.1 — Computed View proposed declaration identity and version
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The proposed identity RM-CV-01 and proposed declaration_version v1_0, also the Tier-1 mode identity at this conceptual level. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — The declared proposed identifier/version pair. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Preserves that pair; any change creates a new version through the settled Decision-5 proposal-and-confirmation path and preserves prior versions append-only. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — An exact proposed declaration identity/version reference. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Treat proposed serialization or final naming as adopted implementation; silently edit a prior declaration version. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — A missing or invalid declaration supplies no mode to run. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7R — Attention & Relevance Control (§7R): the versioned proposal-and-confirmation path governs changes. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1]
- Changes: ACCEPTED — C-7M.10 — Computed View proposed RM-CV-01 declaration: identifies the proposed declaration version. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10 — Computed View proposed RM-CV-01 declaration | The proposed exact identity/version pair. | References the declared mode without silent revision. | Preserved relevance-mode history. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |

SUB-PARTS: NONE

### C-7M.10.2 — Computed View view_assembly purpose
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The settled relevance-purpose type view_assembly. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — The view-assembly request and an optional human label. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Uses view_assembly; the optional label may describe assembling the internal current picture for a view profile without changing the controlled purpose type. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — view_assembly with an optional descriptive label. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Turn free-text wording into a new purpose type or silently guess an unrecognized purpose. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — An unknown purpose follows the declared halt and mapping/proposal route. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7M.10.12 — Computed View invalid relevance declaration outcome: unknown-purpose handling applies. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Changes: ACCEPTED — C-7M.10 — Computed View proposed RM-CV-01 declaration: supplies the relevance purpose. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10 — Computed View proposed RM-CV-01 declaration | The controlled purpose and optional label. | Runs only the declared current purpose. | Purpose-specific relevance. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.10.3 — Computed View relevance target
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The ordering-profile instance's declared purpose or current question requesting assembly. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — That profile's purpose/current question. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Uses it as the target against which eligible source objects are evaluated. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — The declared view-assembly target. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Substitute an undeclared purpose or use relevance to extend the authorized candidate scope. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — An unauthorized profile or declaration produces no snapshot. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: ACCEPTED — C-7M.3.3 — Computed View profile_purpose_type: the profile purpose; C-7M.3.4 — Computed View optional purpose label: optional human-purpose description. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.10 — Computed View proposed RM-CV-01 declaration: supplies the target. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10 — Computed View proposed RM-CV-01 declaration | The current profile purpose/question. | Evaluates candidates for that target. | Relevance answers the declared assembly need. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.10.4 — Computed View deterministic context gates
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The two selected deterministic gate kinds for view assembly. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — The candidate object type and any explicitly declared profile time range. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Applies object_type_matches and applies within_declared_time_range only when the profile declares a range. Does not select same_thread_or_group or precedes_target_in_same_thread because assembly is not thread-adjacency-bound. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — Declared deterministic gate results. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Add thread adjacency as a universal view gate, invent a time range or let a mouth-produced interpretation act as a gate. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Ineligible or unauthorized material does not become an assembly candidate through relevance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: ACCEPTED — C-7M.10.4.1 — Computed View object_type_matches gate: object-type match; C-7M.10.4.2 — Computed View within_declared_time_range gate: conditional time-range gate. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.10 — Computed View proposed RM-CV-01 declaration: supplies the context-gate selection. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10 — Computed View proposed RM-CV-01 declaration | The deterministic eligibility results. | Evaluates permitted candidates under the declared gates. | No invented thread restriction. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 2 · ACCEPTED | C-7M.10.4.1 — Computed View object_type_matches gate | The declared deterministic gate selection. | Supplies the object-type gate. | A bounded deterministic candidate filter. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-7M.10.4.2 — Computed View within_declared_time_range gate | The declared deterministic gate selection. | Supplies conditional time-range eligibility. | A bounded deterministic candidate filter. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: C-7M.10.4.1 — Computed View object_type_matches gate; C-7M.10.4.2 — Computed View within_declared_time_range gate

### C-7M.10.4.1 — Computed View object_type_matches gate
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The deterministic gate matching a candidate's type to the profile's eligible source families. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — The candidate type and profile-declared family set. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Tests object_type_matches against that set. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — The deterministic object-type gate result. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Admit a family outside the declared eligibility set or copy source content to manufacture an eligible object. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Objects outside declared eligibility are not permitted assembly candidates. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: ACCEPTED — C-7M.3.7 — Computed View eligible source-reference families: the eligible family set. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.10.4 — Computed View deterministic context gates: supplies the object-type gate. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10.4 — Computed View deterministic context gates | The object-type match result. | Applies declared source-family eligibility. | A bounded candidate set. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.10.4.2 — Computed View within_declared_time_range gate
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The deterministic time-range gate selected only when the profile declares a range. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — The candidate's applicable time and the explicitly declared range, when present. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Tests within_declared_time_range only for a declared range. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — The applicable time-range gate result without a newly chosen value. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Invent a default range or apply an undeclared time cutoff. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.10.4 — Computed View deterministic context gates: supplies conditional time-range eligibility. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10.4 — Computed View deterministic context gates | The declared-range result when applicable. | Uses the selected deterministic condition. | No hidden age restriction. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.10.5 — Computed View graded-dimension selection
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The selection of all nine settled relevance dimensions for view assembly, each within its applicability. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — Eligible candidates, the current target and each dimension's actual inputs. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Uses the embedding model only for semantic_similarity and deterministic rules for the other eight dimensions. Preserves producer, rule/model version, index or prompt version as applicable and the produced value. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — Nine separately typed dimension outcomes, including honest absence where a value cannot apply or be produced. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Coerce an inapplicable dimension into a relevance signal, silently blank a missing value or substitute model confidence for evidence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Inapplicable or missing-input cases retain honest not_applicable, not_evaluated or collection_failed outcomes as applicable. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: ACCEPTED — C-7M.10.5.1 — Computed View semantic_similarity selection: semantic similarity; C-7M.10.5.2 — Computed View temporal_distance selection: temporal distance; C-7M.10.5.3 — Computed View positional_distance selection: positional distance; C-7M.10.5.4 — Computed View currentness_status selection: currentness; C-7M.10.5.5 — Computed View explicit_links selection: explicit links; C-7M.10.5.6 — Computed View ness_response_links selection: Ness response links; C-7M.10.5.7 — Computed View proposal_acceptance_outcome selection: proposal acceptance; C-7M.10.5.8 — Computed View reading_context_status selection: reading context; C-7M.10.5.9 — Computed View active_clash_links selection: active clash links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gated by: ACCEPTED — C-7F.6.10.5.5 — Honest dimension absence: the existing honest-absence outcome contract is reused under the proposed shared uncertainty rule. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Changes: ACCEPTED — C-7M.10 — Computed View proposed RM-CV-01 declaration: supplies the declared dimension vector. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10 — Computed View proposed RM-CV-01 declaration | The separate applicable dimension outcomes. | Uses them for declared relevance to the current purpose. | Factor 4 remains explicit and bounded. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 2 · ACCEPTED | C-7M.10.5.1 — Computed View semantic_similarity selection | The nine-dimension selection with strict applicability and producer/version provenance. | Supplies semantic_similarity. | A separate typed dimension without fabricated evidence strength. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-7M.10.5.2 — Computed View temporal_distance selection | The nine-dimension selection with strict applicability and producer/version provenance. | Supplies temporal_distance. | A separate typed dimension without fabricated evidence strength. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 4 · ACCEPTED | C-7M.10.5.3 — Computed View positional_distance selection | The nine-dimension selection with strict applicability and producer/version provenance. | Supplies positional_distance. | A separate typed dimension without fabricated evidence strength. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 5 · ACCEPTED | C-7M.10.5.4 — Computed View currentness_status selection | The nine-dimension selection with strict applicability and producer/version provenance. | Supplies currentness_status. | A separate typed dimension without fabricated evidence strength. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 6 · ACCEPTED | C-7M.10.5.5 — Computed View explicit_links selection | The nine-dimension selection with strict applicability and producer/version provenance. | Supplies explicit_links. | A separate typed dimension without fabricated evidence strength. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 7 · ACCEPTED | C-7M.10.5.6 — Computed View ness_response_links selection | The nine-dimension selection with strict applicability and producer/version provenance. | Supplies ness_response_links. | A separate typed dimension without fabricated evidence strength. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 8 · ACCEPTED | C-7M.10.5.7 — Computed View proposal_acceptance_outcome selection | The nine-dimension selection with strict applicability and producer/version provenance. | Supplies proposal_acceptance_outcome. | A separate typed dimension without fabricated evidence strength. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 9 · ACCEPTED | C-7M.10.5.8 — Computed View reading_context_status selection | The nine-dimension selection with strict applicability and producer/version provenance. | Supplies reading_context_status. | A separate typed dimension without fabricated evidence strength. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 10 · ACCEPTED | C-7M.10.5.9 — Computed View active_clash_links selection | The nine-dimension selection with strict applicability and producer/version provenance. | Supplies active_clash_links. | A separate typed dimension without fabricated evidence strength. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: C-7M.10.5.1 — Computed View semantic_similarity selection; C-7M.10.5.2 — Computed View temporal_distance selection; C-7M.10.5.3 — Computed View positional_distance selection; C-7M.10.5.4 — Computed View currentness_status selection; C-7M.10.5.5 — Computed View explicit_links selection; C-7M.10.5.6 — Computed View ness_response_links selection; C-7M.10.5.7 — Computed View proposal_acceptance_outcome selection; C-7M.10.5.8 — Computed View reading_context_status selection; C-7M.10.5.9 — Computed View active_clash_links selection

### C-7M.10.5.1 — Computed View semantic_similarity selection
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The embedding-produced semantic_similarity dimension selected for view assembly. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — The eligible candidate and current target in the declared embedding context. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Uses the settled embedding producer all-MiniLM-L6-v2 for semantic_similarity and carries its applicable version provenance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — The separate semantic_similarity outcome. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Treat similarity as fact, source strength, a context-gate condition or a collapsed view score. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — An unproducible value retains the honest absence outcome. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.10.5 — Computed View graded-dimension selection: supplies semantic_similarity. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10.5 — Computed View graded-dimension selection | The embedding similarity result. | Keeps it separate from deterministic dimensions and evidence strength. | One purpose-relevance dimension. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.10.5.2 — Computed View temporal_distance selection
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The deterministic temporal_distance dimension selected for view assembly. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — The applicable candidate and target time references. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Carries the deterministic temporal-distance outcome. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — The separate temporal_distance value or honest absence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Convert temporal proximity into reliability or override recency's final tie-break position. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Missing inputs retain an honest absence outcome. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.10.5 — Computed View graded-dimension selection: supplies temporal_distance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10.5 — Computed View graded-dimension selection | The temporal-distance outcome. | Keeps time relevance distinct from support strength. | A separate deterministic dimension. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.10.5.3 — Computed View positional_distance selection
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The deterministic positional_distance dimension where candidate and thread-bound reference share a thread. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — A candidate and a thread-bound reference with a common thread. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Evaluates positional_distance only within that applicability. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — The applicable positional distance or honest absence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Invent shared-thread position for unrelated objects or impose thread adjacency on the whole assembly. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — A non-shared-thread combination records honest inapplicability. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.10.5 — Computed View graded-dimension selection: supplies positional_distance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10.5 — Computed View graded-dimension selection | The applicable positional-distance outcome. | Uses it only within its thread scope. | No fabricated cross-thread position. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.10.5.4 — Computed View currentness_status selection
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The deterministic currentness_status dimension for state-node candidates only. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — A state-node candidate's recorded Living State status. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Carries that recorded status without re-evaluating it as relevance strength. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — The recorded currentness_status or honest inapplicability. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Compute a new state status from relevance, apply this dimension to non-state candidates or feed the view back into Living State. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — A non-state candidate records honest inapplicability. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: DESIGNED — C-7D — Living State Web (§7D): supplies the recorded state-node status strictly upstream. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.10.5 — Computed View graded-dimension selection: supplies currentness_status. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10.5 — Computed View graded-dimension selection | The recorded state status. | Keeps status provenance distinct from relevance strength. | No feedback into state. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.10.5.5 — Computed View explicit_links selection
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The deterministic explicit_links dimension selected for view assembly. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — Applicable explicit source-object links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Carries explicit_links as its own dimension with rule provenance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — The separate explicit_links outcome. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Invent links from semantic resemblance or turn a link into new independent evidence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Missing applicable inputs retain honest absence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.10.5 — Computed View graded-dimension selection: supplies explicit_links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10.5 — Computed View graded-dimension selection | The explicit-link result. | Uses recorded relationships for declared relevance. | No new link authority. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.10.5.6 — Computed View ness_response_links selection
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The deterministic ness_response_links dimension selected for view assembly. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — Applicable recorded Ness response-event links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Carries those links as a distinct relevance dimension. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — The separate ness_response_links outcome. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Rewrite a response as historical truth or conflate its dimension result with the first factor's explicit judgment. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Missing applicable inputs retain honest absence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.10.5 — Computed View graded-dimension selection: supplies ness_response_links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10.5 — Computed View graded-dimension selection | The response-link outcome. | Uses actual event links within purpose relevance. | Separate response provenance. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.10.5.7 — Computed View proposal_acceptance_outcome selection
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The deterministic proposal_acceptance_outcome dimension for reading candidates only. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — A reading candidate's recorded proposal-acceptance outcome. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Carries that outcome separately within its reading-only applicability. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — The proposal_acceptance_outcome value or honest inapplicability. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Apply a reading acceptance outcome to a root, state node or other non-reading object, or treat acceptance as truth. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Non-reading candidates record honest inapplicability. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.10.5 — Computed View graded-dimension selection: supplies proposal_acceptance_outcome. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10.5 — Computed View graded-dimension selection | The reading acceptance outcome. | Preserves the reading-specific applicability. | No invented acceptance signal for other types. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.10.5.8 — Computed View reading_context_status selection
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The deterministic reading_context_status dimension for accepted-reading candidates only. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — An accepted reading's recorded context status. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Carries the recorded context-status value without changing the reading. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — The reading_context_status result or honest inapplicability. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Apply this accepted-reading-only status to another object type or turn context sufficiency into a truth verdict. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — An inapplicable candidate retains honest absence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.10.5 — Computed View graded-dimension selection: supplies reading_context_status. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10.5 — Computed View graded-dimension selection | The accepted-reading context status. | Keeps the source-carried status and its applicability. | No fabricated context signal. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.10.5.9 — Computed View active_clash_links selection
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The deterministic active_clash_links dimension selected for view assembly. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — The candidate's applicable active-clash links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Carries active_clash_links separately while the clash and uncertainty remain attached to view entries. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — The separate active_clash_links outcome. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Hide a clash through relevance ordering or count disagreement as resolved because a candidate ranked highly. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Missing applicable inputs retain honest absence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.10.5 — Computed View graded-dimension selection: supplies active_clash_links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10.5 — Computed View graded-dimension selection | The active-clash-link result. | Preserves disagreement in purpose relevance. | No silent conflict suppression. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.10.6 — Computed View mouth-authorization boundary
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The explicit none value for mouth authorization in this declaration. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — The declaration's producer and authorization fields. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Declares no mouth-produced relevance dimension. Any future such dimension requires a new declaration version, specifically named dimension and contexts, a versioned Tier-2 unresolved-handling reference in Tier 1 and settled independent validation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — Mouth authorization: none. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Omit the field, use a broad mouth-allowed flag, make a mouth value a context gate, allow self-approval or precompute it without explicit declaration and designed independent validation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — No undeclared mouth-produced relevance dimension runs under this version. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7R — Attention & Relevance Control (§7R): the settled version and validation rules govern any future declaration change. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Changes: ACCEPTED — C-7M.10 — Computed View proposed RM-CV-01 declaration: supplies the explicit no-mouth authorization. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10 — Computed View proposed RM-CV-01 declaration | The explicit none value. | Uses only declared deterministic and embedding producers. | No new interpretive producer authority. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.10.7 — Computed View relevance evaluation timing
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — On-demand evaluation at the settled view-update triggers. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — A view opening, Ness's refresh request or a materially relevant event defined by the profile. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Evaluates at those consumer triggers only; declares no triggered pre-computation and no continuous recomputation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — A purpose-bound evaluation for an actual permitted update trigger. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Turn ordinary arrivals into global recomputation or treat consumer-triggered assembly as relevance pre-computation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7M.4 — Computed View update triggers: supplies the permitted triggers. [V10 §7M] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.10 — Computed View proposed RM-CV-01 declaration: supplies the declared timing. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10 — Computed View proposed RM-CV-01 declaration | The permitted on-demand trigger. | Evaluates the current view purpose at that trigger. | No continuous relevance process. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.10.8 — Computed View relevance-mode reason
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The declaration's reason: a defined contribution to factor 4 of the fixed view order. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — The current question or view purpose and broadly permitted current and older material. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Supplies exactly the purpose-relevance contribution without a hidden score. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — An explicit reason for selecting this relevance mode. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Let this mode reorder the seven factors or become the whole view-ranking decision. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.10 — Computed View proposed RM-CV-01 declaration: supplies the declared mode reason. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10 — Computed View proposed RM-CV-01 declaration | The factor-4 purpose. | Keeps the relevance contribution bounded. | No unspoken universal ranking. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.10.9 — Computed View Tier-2 relevance rules
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The view-owned ordering, fallback, surfacing and unresolved-dimension handling tier. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — Declared Tier-1 relevance outcomes and the profile's separate factor results. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Keeps fixed factor order and attached labels; accepts honest incomplete/no-clear-view/null outcomes; remains quiet internally; applies the proposed shared uncertainty rule without turning interpretations into facts. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — Consumer-owned relevance consequences under the exact profile and declaration versions. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Take over Tier-1 validation, collapse dimensions into evidence strength, erase older-pattern labels or silently select the highest-confidence interpretation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Unresolved or failed relevance cannot silently fill a support gap or make an unsupported picture fresh. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: ACCEPTED — C-7M.10.9.1 — Computed View relevance ordering consequences: ordering; C-7M.10.9.2 — Computed View relevance fallback: fallback; C-7M.10.9.3 — Computed View relevance surfacing boundary: surfacing; C-7M.10.9.4 — Computed View proposed shared unresolved handling: proposed unresolved handling. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.10 — Computed View proposed RM-CV-01 declaration: supplies Tier-2 rules. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10 — Computed View proposed RM-CV-01 declaration | The consumer-owned consequence rules. | Applies relevance without changing its authority or evidence meaning. | An honest internal assembly. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 2 · ACCEPTED | C-7M.10.9.1 — Computed View relevance ordering consequences | The consumer-owned Tier-2 consequence contract. | Supplies ordering consequences. | Bounded relevance consequences. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-7M.10.9.2 — Computed View relevance fallback | The consumer-owned Tier-2 consequence contract. | Supplies fallback. | Bounded relevance consequences. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| 4 · ACCEPTED | C-7M.10.9.3 — Computed View relevance surfacing boundary | The consumer-owned Tier-2 consequence contract. | Supplies relevance surfacing behavior. | Bounded relevance consequences. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] |
| 5 · ACCEPTED | C-7M.10.9.4 — Computed View proposed shared unresolved handling | The consumer-owned Tier-2 consequence contract. | Supplies the proposed unresolved-handling contract. | Bounded relevance consequences. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |

SUB-PARTS: C-7M.10.9.1 — Computed View relevance ordering consequences; C-7M.10.9.2 — Computed View relevance fallback; C-7M.10.9.3 — Computed View relevance surfacing boundary; C-7M.10.9.4 — Computed View proposed shared unresolved handling

### C-7M.10.9.1 — Computed View relevance ordering consequences
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The fixed-order consequence of relevance within the seven view factors. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — Each factor's separate result and source-carried uncertainty, changed-pattern and strength labels. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Feeds relevance to factor 4 only; records every factor separately; keeps direct-root support above repetition, frequency and model confidence, with recency a final tie-breaker. Keeps older-pattern entries marked as such. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — Disclosed factor-by-factor ordering with attached source labels. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Silently reorder factors, collapse them into a score or harden an older pattern or interpretation into fact. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Uncertainty and source limitations remain visible on the entry rather than silently removed. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: DESIGNED — C-7M.2 — Computed View seven-factor priority order: the fixed seven-factor order. [V10 §7M] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.10.9 — Computed View Tier-2 relevance rules: supplies ordering consequences. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10.9 — Computed View Tier-2 relevance rules | The bounded factor-4 contribution and retained labels. | Preserves the complete fixed factor order. | No relevance-derived truth score. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.10.9.2 — Computed View relevance fallback
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The honest fallback when relevance-supported assembly cannot complete. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The support limits, refresh outcome and previous valid snapshot. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Allows incomplete, no clear current view and valid null update; a failed update retains the previous valid snapshot with possible staleness derived from later events. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — An honest limited result or retained standing picture. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Silently fill a gap or write a staleness mark onto the immutable snapshot. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — No unsupported fresh or half-built picture is emitted. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

TOGETHER
- Fed by: ACCEPTED — C-7M.7 — Computed View refresh lifecycle: the precise append-only lifecycle consequences. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.10.9 — Computed View Tier-2 relevance rules: supplies fallback. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10.9 — Computed View Tier-2 relevance rules | The honest limited outcome. | Preserves support and freshness limitations. | No manufactured complete picture. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.10.9.3 — Computed View relevance surfacing boundary
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The internal-only surface rule for view relevance and its downstream uncertainty. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — Quiet internal view use or Ness's deliberate request to inspect the picture; a downstream visible result materially relying on uncertainty. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Requires no Ness approval for authorized quiet internal use. Shows the picture only on deliberate request. The downstream visible owner discloses material uncertainty under its own surface rules while the view remains silent. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — Quiet internal support or a deliberately requested inspection; material uncertainty disclosed by the actual visible-result owner. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Volunteer the whole picture because it exists or narrate internal knowledge back unprompted. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — The view itself remains silent unless deliberately requested. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7M.1 — Computed View internal-use boundary: the existing internal-use/requested-inspection boundary governs view display. [V10 §7M] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Changes: ACCEPTED — C-7M.10.9 — Computed View Tier-2 relevance rules: supplies relevance surfacing behavior. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10.9 — Computed View Tier-2 relevance rules | The quiet-use and material-uncertainty rules. | Keeps disclosure with the actual visible owner. | No unprompted view narration. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.10.9.4 — Computed View proposed shared unresolved handling
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — This consumer's use of proposed T2-UNRES-SHARED v1_0, preserving the existing shared outcome atoms. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — Validated, failed, unresolved, disputed or absent dimension outcomes and their recorded provenance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Uses validated values only as interpretations with no rule-detectable error, never a truth guarantee. Does not use failed values. May keep permitted unresolved/disputed results as weak labeled logged clues for checking, retrieval or evaluation; records disagreement and never chooses by greater model confidence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — Declared uncertainty handling with honest not_applicable, not_evaluated or collection_failed outcomes where appropriate. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Let an unresolved/disputed value alone support a factual claim, satisfy current-situation support, change Living State, cause an actual reread, authorize an active suggestion, widen access or grant authority; coerce missing inputs into relevance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Failed values are unused; unresolved limitations remain attached and material uncertainty is disclosed by the downstream visible owner. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: ACCEPTED — C-7F.6.10.5.1 — Validated relevance value: validated interpretation; C-7F.6.10.5.2 — Failed relevance value: unused failed result; C-7F.6.10.5.3 — Unresolved relevance clue: weak unresolved clue; C-7F.6.10.5.4 — Relevance disagreement record handoff: disagreement handoff; C-7F.6.10.5.5 — Honest dimension absence: honest absence. These existing atoms are reused under the proposed shared rule, without changing their canonical names. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gated by: DESIGNED — C-7R — Attention & Relevance Control (§7R): Decision-11 records disagreement and the settled validation contract governs interpretation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Changes: ACCEPTED — C-7M.10.9 — Computed View Tier-2 relevance rules: supplies the proposed unresolved-handling contract. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10.9 — Computed View Tier-2 relevance rules | The labeled uncertainty and absence outcomes. | Uses only the permitted weak or validated contribution. | No fact, action or access authority from unresolved relevance. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |

SUB-PARTS: NONE

### C-7M.10.10 — Computed View relevance allowed-use boundary
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The source, purpose and direction limits of relevance-supported assembly. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Takes in: ACCEPTED — Internally authorized material from the profile's permitted source families. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Does: ACCEPTED — Informs responses internally without becoming new source evidence or changing any underlying record. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Gives out: ACCEPTED — An authorized internal assembly contribution. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Must never: ACCEPTED — Feed the view into Living State, make it evidence for itself, launder interpretation into fact, widen access or introduce a held-raw-content or TSC inspection path. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — Unauthorized or ineligible material cannot influence assembly. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): purpose-specific internal authorization and influence-removal rules apply before relevance. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5]
- Changes: ACCEPTED — C-7M.10 — Computed View proposed RM-CV-01 declaration: supplies permitted-use limits. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10 — Computed View proposed RM-CV-01 declaration | The permitted source and use scope. | Keeps relevance inside the authorized profile. | No evidence or access expansion. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.10.11 — Computed View relevance evaluation record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The Decision-12 relevance event for each assembly evaluation and its links to view records. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Takes in: ACCEPTED — The evaluation, exact profile/declaration versions, source IDs, separate factors, omissions and completeness. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Does: ACCEPTED — Creates one relevance event per assembly evaluation; preserves profile identity/version, Tier-1 reference, source references, factor outcomes, omission reasons and honest completeness in the linked snapshot/refresh record family under its accepted separate schemas. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gives out: ACCEPTED — An append-only immutable evaluation record with traceable view-record references. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Must never: ACCEPTED — Rewrite the evaluation, collapse factors into one score, double-count an event as independent evidence or merge distinct domain and operational records. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — An unsuccessful assembly remains recorded honestly with no snapshot where the profile/declaration is invalid or unauthorized. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

TOGETHER
- Fed by: ACCEPTED — C-7M.5 — Computed View immutable snapshot record: snapshot detail; C-7M.6 — Computed View refresh-status event: attempt/outcome reference; C-7M.11 — Computed View operational records and lifecycle: the separate operational record. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]
- Gated by: DESIGNED — C-7R — Attention & Relevance Control (§7R): owns the settled Decision-12 relevance-event contract. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Changes: ACCEPTED — C-7M.10 — Computed View proposed RM-CV-01 declaration: supplies evaluation traceability. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10 — Computed View proposed RM-CV-01 declaration | The one evaluation event and linked view records. | Keeps relevance and assembly provenance inspectable. | No unlogged or rewritten evaluation. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7M.10.12 — Computed View invalid relevance declaration outcome
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The failed/incomplete or unknown-purpose result when a valid authorized declaration cannot run. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — A missing, invalid, stale or unauthorized profile/declaration, or an unrecognized purpose value. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Creates the applicable failed/incomplete refresh-status event and no snapshot. For an unknown purpose, halts, identifies the value and vocabulary version, preserves the original request, explains plainly and offers mapping or a new-type proposal through Decision 5. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — An honest failed/incomplete event or preserved unknown-purpose request with the declared resolution route. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Improvise a relevance mode, guess the purpose, rewrite or suppress source objects, select a reading as authoritative or surface the internal picture unprompted. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — No snapshot is created from the unusable profile/declaration and the unknown-purpose evaluation does not proceed. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7R — Attention & Relevance Control (§7R): Decision-14 halt and Decision-5 versioned proposal/confirmation govern the unknown-purpose route. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Changes: ACCEPTED — C-7M.10 — Computed View proposed RM-CV-01 declaration: supplies declaration failure behavior. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.10 — Computed View proposed RM-CV-01 declaration | The invalid declaration or unknown-purpose outcome. | Preserves the request and honest failure rather than inventing a mode. | No unsupported assembly. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 2 · ACCEPTED | C-7M.10.2 — Computed View view_assembly purpose | The unknown-purpose halt. | Retains the controlled purpose vocabulary and explicit resolution route. | No guessed type. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |

SUB-PARTS: NONE

### C-7M.11 — Computed View operational records and lifecycle
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The connected append-only operation record and separate active/cold lifecycle for Computed View work, including profile creation/versioning and status evaluation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — Each real operation's evaluated, used, unused, omitted, outcome, retry, recovery, prior-use and resulting-object information. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Creates one connected operational record per real operation, preserves each record separately and records initial and later active/cold status through separate events. Carries an existing evidence-family identity when the logged event already serves as support. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — An authorized retrievable operation record, separate lifecycle events and links to domain outcomes. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Create recursive logs about logging, merge record kinds, collapse or hide records to deduplicate, add evidence strength or count the log as a second vote. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — Uncertain status eligibility preserves the previous active/cold state and records the failed evaluation; no silent cooling, reactivation, hiding or reprioritization follows. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

TOGETHER
- Fed by: ACCEPTED — C-7M.11.1 — Computed View operation-record content: operation content; C-7M.11.2 — Computed View domain-log level separation: separate level accounting; C-7M.11.3 — Computed View operational-record lifecycle: lifecycle; C-7M.11.4 — Bundle 4 operational-record lifecycle-status event: lifecycle/status event fields; C-7M.11.5 — Bundle 4 domain-log-lifecycle separation: three-kind separation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gated by: DESIGNED — C-7B.10.5 — Real-operation and evidence boundaries: one real operation, no recursive logging and no doubled evidence; C-7B.10.8 — Operational-record access boundary: operational-record access remains governed by privacy, authority, identity/security, TSC, compartment and influence-removal rules. [V10 §0B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Changes: DESIGNED — C-7M — Computed View (§7M): keeps view operations inspectable without making their logs evidence. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M — Computed View (§7M) | The connected operation history and separate lifecycle. | Uses and inspects it only under authorization. | Traceability without evidence inflation. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-7M.3.19 — Computed View operational-log references | Operational-log references. | Links profiles, snapshots and status events to their operation records. | Connected provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 3 · ACCEPTED | C-7M.9 — Computed View operation and recovery contract | The append-only operation outcome and recovery record. | Records honest recovery and missing-record reconciliation. | No rerun hidden by absent logging. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 4 · ACCEPTED | C-7M.10.11 — Computed View relevance evaluation record | The separately linked operational record. | Keeps domain relevance events distinct from logging. | No merged or double-counted record kind. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 5 · ACCEPTED | C-7M.11.1 — Computed View operation-record content | The one-connected-record and distinct append-only lifecycle discipline. | Supplies the view operation's content contract. | Inspectable history without recursive logs or evidence inflation. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 6 · ACCEPTED | C-7M.11.2 — Computed View domain-log level separation | The one-connected-record and distinct append-only lifecycle discipline. | Supplies correct log/domain accounting. | Inspectable history without recursive logs or evidence inflation. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.1] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| 7 · ACCEPTED | C-7M.11.3 — Computed View operational-record lifecycle | The one-connected-record and distinct append-only lifecycle discipline. | Supplies append-only lifecycle status. | Inspectable history without recursive logs or evidence inflation. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 8 · ACCEPTED | C-7M.11.4 — Bundle 4 operational-record lifecycle-status event | The one-connected-record and distinct append-only lifecycle discipline. | Supplies the separate lifecycle-event record. | Inspectable history without recursive logs or evidence inflation. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 9 · ACCEPTED | C-7M.11.5 — Bundle 4 domain-log-lifecycle separation | The one-connected-record and distinct append-only lifecycle discipline. | Supplies record-kind separation. | Inspectable history without recursive logs or evidence inflation. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 10 · ACCEPTED | C-7M.12 — Computed View provisional-creation influence | The actual using operation's own connected log. | Carries provisional_material_used with record ID and status at use time. | Traceable, visibly provisional influence. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: C-7M.11.1 — Computed View operation-record content; C-7M.11.2 — Computed View domain-log level separation; C-7M.11.3 — Computed View operational-record lifecycle; C-7M.11.4 — Bundle 4 operational-record lifecycle-status event; C-7M.11.5 — Bundle 4 domain-log-lifecycle separation

### C-7M.11.1 — Computed View operation-record content
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The Bundle 4 content carried by the one connected operation record. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — What was evaluated, used and not used; omission/set-aside reasons; success, failure, retry and crash-recovery outcomes; prior-record use; resulting object IDs. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Records those facts for the actual operation, including profile creation/versioning. Preserves source and result references without copying or strengthening the underlying evidence. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — The operation's complete connected record with outcome and result IDs. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Omit unsuccessful work or prior-record use, count a derivative log as new support, or treat a preview/approval as an outside execution. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — Unsuccessful, incomplete and recovered operations retain their actual outcomes. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

TOGETHER
- Fed by: DECIDED-2026-09-25 — C-7B.10.2 — Operational-record content contract: existing operational-content atoms; C-7B.10.3 — Use and non-use records: existing use/non-use and omission atoms retain their ownership. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.11 — Computed View operational records and lifecycle: supplies the view operation's content contract. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11 — Computed View operational records and lifecycle | The evaluated/use/omission/outcome/recovery/result references. | Writes the one connected record for the real operation. | Inspectable operational history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-7M.11.5 — Bundle 4 domain-log-lifecycle separation | The real operation's connected log content. | Preserves that log as distinct from domain and lifecycle events. | One log for the real operation, not three interchangeable records. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 3 · ACCEPTED | C-7D.17.8 — B6 connected operational record | What was evaluated, used and not used. | Supplies shared operation-record content. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] [MAP C-7D] |

SUB-PARTS: NONE

### C-7M.11.2 — Computed View domain-log level separation
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.1] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The separate authority accounting of a domain operation and its mandatory operational-log append. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.1] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — What the domain operation physically does and the linked log write under the same operation identity. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.1] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Classifies the domain operation by its own effect; records the operational-log append as a separate linked Level-2 internal write. A Level-1 read remains Level 1 even though its mandatory log append is Level 2. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.1] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — Separate domain and log level accounting under one operation identity. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.1] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Reclassify a read because it must be logged, merge the two operations' accounting or count the mandatory log write twice. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.1] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7M.5.2 — Computed View operation_id: the shared operation identity. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.1] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gated by: DESIGNED — C-7P — Permission & Authority Boundaries (§7P): authority levels follow the operation's actual present effect. [V10 §7P] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.1]
- Changes: ACCEPTED — C-7M.11 — Computed View operational records and lifecycle: supplies correct log/domain accounting. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.1] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11 — Computed View operational records and lifecycle | The domain effect and separate log-write level. | Records both without merging or double-counting. | No authority-level inflation from required logging. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-7D.17.8 — B6 connected operational record | What was evaluated, used and not used. | Supplies separate domain/log level accounting. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] [MAP C-7D] |

SUB-PARTS: NONE

### C-7M.11.3 — Computed View operational-record lifecycle
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The accepted active/cold lifecycle for these operational records, consuming the existing general Log-state owners. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — A newly committed record or later authorized cooling/reactivation evaluation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Starts every new record active without exception. Represents initial and later statuses append-only, preserving the original operational record. Uses component-owned fixed declared versioned cooling rules and actual authorized-use/link conditions. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — An active or cold derived operational-record status with preserved lifecycle history. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Mutate the record, invent a third status on failure, cool from the momentary absence of an active protection alone, or let retrieval/similarity alone reactivate it. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — Uncertain eligibility keeps the previous status and records a failed evaluation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

TOGETHER
- Fed by: ACCEPTED — C-7M.11.3.1 — Computed View active-log protection conditions: active protections; C-7M.11.3.2 — Computed View cooling-rule ownership: cooling-rule ownership; C-7M.11.3.3 — Computed View active-to-cold operation: both cooling conditions; C-7M.11.3.4 — Computed View cold-record reactivation: reactivation; C-7M.11.3.5 — Computed View uncertain status evaluation: uncertain evaluation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gated by: DESIGNED — C-7B.10.6 — Active and cold Log lifecycle: existing active/cold state meanings; C-7B.10.7 — Cooling-rule changes: fixed cooling-rule change and evidence/approval requirements. [V10 §0B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Changes: ACCEPTED — C-7M.11 — Computed View operational records and lifecycle: supplies append-only lifecycle status. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11 — Computed View operational records and lifecycle | The status and lifecycle events. | Preserves records while adjusting only authorized presentation/retrieval priority. | No changed evidence or history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-7M.11.4 — Bundle 4 operational-record lifecycle-status event | Initial active and later active/cold transitions. | Records exact permitted statuses and evaluation outcomes. | No mutable status on the operational record. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 3 · ACCEPTED | C-7M.11.3.1 — Computed View active-log protection conditions | The active/cold lifecycle with append-only history and immutable original records. | Supplies active protection. | Only authorized status and retrieval/presentation priority changes. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 4 · ACCEPTED | C-7M.11.3.2 — Computed View cooling-rule ownership | The active/cold lifecycle with append-only history and immutable original records. | Supplies cooling-rule ownership. | Only authorized status and retrieval/presentation priority changes. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 5 · ACCEPTED | C-7M.11.3.3 — Computed View active-to-cold operation | The active/cold lifecycle with append-only history and immutable original records. | Supplies the append-only cooling operation. | Only authorized status and retrieval/presentation priority changes. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 6 · ACCEPTED | C-7M.11.3.4 — Computed View cold-record reactivation | The active/cold lifecycle with append-only history and immutable original records. | Supplies permitted reactivation. | Only authorized status and retrieval/presentation priority changes. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 7 · ACCEPTED | C-7M.11.3.5 — Computed View uncertain status evaluation | The active/cold lifecycle with append-only history and immutable original records. | Supplies status-evaluation failure behavior. | Only authorized status and retrieval/presentation priority changes. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |

SUB-PARTS: C-7M.11.3.1 — Computed View active-log protection conditions; C-7M.11.3.2 — Computed View cooling-rule ownership; C-7M.11.3.3 — Computed View active-to-cold operation; C-7M.11.3.4 — Computed View cold-record reactivation; C-7M.11.3.5 — Computed View uncertain status evaluation

### C-7M.11.3.1 — Computed View active-log protection conditions
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The five conditions keeping an operational record active while any one applies. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — Its operation state, current-chain references, pending recovery/correction need, actual authorized use and valid new links. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Keeps the record active if any protection applies; their momentary absence alone does not establish cooling eligibility. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — Protected active status. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Treat absence of these protections as a sufficient cooling shortcut. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — Cooling still requires both declared age and the no-use/no-valid-new-link condition. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

TOGETHER
- Fed by: ACCEPTED — C-7M.11.3.1.1 — Computed View unresolved-operation log protection: unresolved work; C-7M.11.3.1.2 — Computed View current-chain log protection: current-chain reference; C-7M.11.3.1.3 — Computed View recovery-and-correction log protection: pending recovery/correction; C-7M.11.3.1.4 — Computed View actual-use log protection: actual authorized use; C-7M.11.3.1.5 — Computed View valid-new-link log protection: valid new link. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.11.3 — Computed View operational-record lifecycle: supplies active protection. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11.3 — Computed View operational-record lifecycle | The presence of any active protection. | Keeps the record active under that condition. | No premature cooling. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-7M.11.3.1.1 — Computed View unresolved-operation log protection | Any applicable protection is sufficient to retain active status. | Supplies unresolved-work protection. | No cooling while protected. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 3 · ACCEPTED | C-7M.11.3.1.2 — Computed View current-chain log protection | Any applicable protection is sufficient to retain active status. | Supplies current-chain protection. | No cooling while protected. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 4 · ACCEPTED | C-7M.11.3.1.3 — Computed View recovery-and-correction log protection | Any applicable protection is sufficient to retain active status. | Supplies pending-work protection. | No cooling while protected. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 5 · ACCEPTED | C-7M.11.3.1.4 — Computed View actual-use log protection | Any applicable protection is sufficient to retain active status. | Supplies genuine-use protection. | No cooling while protected. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 6 · ACCEPTED | C-7M.11.3.1.5 — Computed View valid-new-link log protection | Any applicable protection is sufficient to retain active status. | Supplies valid-link protection. | No cooling while protected. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 7 · ACCEPTED | C-7M.11.3.3 — Computed View active-to-cold operation | The requirement to preserve active status while protected. | Does not use momentary protection absence as a cooling shortcut; still requires both settled conditions. | No premature cold transition. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 8 · ACCEPTED | C-7D.17.9 — B6 operational-record active-cold lifecycle | New operational records, actual authorized use, valid new links, protection conditions and the declared rule. | Supplies the five shared protection conditions. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: C-7M.11.3.1.1 — Computed View unresolved-operation log protection; C-7M.11.3.1.2 — Computed View current-chain log protection; C-7M.11.3.1.3 — Computed View recovery-and-correction log protection; C-7M.11.3.1.4 — Computed View actual-use log protection; C-7M.11.3.1.5 — Computed View valid-new-link log protection

### C-7M.11.3.1.1 — Computed View unresolved-operation log protection
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — Active protection for a log belonging to unresolved or in-progress work. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — The associated operation's unresolved or in-progress state. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Keeps the record active while that state applies. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — An active-protection result. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Cool the record while its operation is unresolved or in progress. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.11.3.1 — Computed View active-log protection conditions: supplies unresolved-work protection. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11.3.1 — Computed View active-log protection conditions | Unresolved or in-progress work. | Preserves active status. | The live operation retains its record. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.11.3.1.2 — Computed View current-chain log protection
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — Active protection for a log referenced by a current valid state, view, world-model or action chain. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — A reference from such a current valid chain. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Keeps the referenced record active. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — An active-protection result. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Cool a log while a current valid chain references it. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.11.3.1 — Computed View active-log protection conditions: supplies current-chain protection. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11.3.1 — Computed View active-log protection conditions | The valid current-chain reference. | Retains active status. | Current provenance remains active. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.11.3.1.3 — Computed View recovery-and-correction log protection
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — Active protection for records needed by pending recovery, retry, reconciliation, violation handling or correction. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — The pending operation's need for the record. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Keeps the needed record active while that work remains pending. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — An active-protection result. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Cool a record needed by the pending recovery or correction chain. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.11.3.1 — Computed View active-log protection conditions: supplies pending-work protection. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11.3.1 — Computed View active-log protection conditions | The pending recovery/retry/reconciliation/violation/correction need. | Preserves active status. | Required recovery provenance stays available. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.11.3.1.4 — Computed View actual-use log protection
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — Active protection while an authorized component actually uses the record. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — Actual authorized use of the record. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Keeps it active during that genuine use. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — An active-protection result. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Substitute similarity or mere retrieval for actual use. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.11.3.1 — Computed View active-log protection conditions: supplies genuine-use protection. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11.3.1 — Computed View active-log protection conditions | Actual authorized use. | Preserves active status. | A used record is not cooled through age alone. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.11.3.1.5 — Computed View valid-new-link log protection
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — Active protection while a record receives a valid new link under the governing connection rules. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — The valid new link and its governing rule. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Keeps the record active while the valid link condition applies. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — An active-protection result. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Treat resemblance, co-retrieval or an invalid proposed link as a valid new link. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.11.3.1 — Computed View active-log protection conditions: supplies valid-link protection. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11.3.1 — Computed View active-log protection conditions | The valid new link. | Retains active status under the link condition. | No unsupported connection-based lifecycle change. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.11.3.2 — Computed View cooling-rule ownership
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The consuming component's fixed, declared, versioned operational-record cooling rule. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — Record category and operation/lifecycle status as declared by the rule; a proposed future change and its evidence where applicable. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Owns one explicit versioned rule without a hidden score. A future rule-change proposal requires quantitative evidence and concrete examples; it becomes operative only with Ness's approval. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — A fixed rule identity/version and an approval-bound change route. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Invent empirical time values, silently change cooling policy or make a proposed change operative before Ness approves it. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — Without the required approval a proposed rule change is not operative. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7B.10.7.1 — Fixed declared cooling rules: fixed declaration; C-7B.10.7.2.3 — Quantitative proposal evidence: quantitative evidence; C-7B.10.7.2.4 — Concrete proposal examples: concrete examples; C-7B.10.7.3 — Cooling-change approval: Ness's approval for a change. [V10 §0B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Changes: ACCEPTED — C-7M.11.3 — Computed View operational-record lifecycle: supplies cooling-rule ownership; C-7M.11.4.4 — Bundle 4 cooling_rule_id_and_version: supplies the exact evaluated rule identity/version. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11.3 — Computed View operational-record lifecycle | The fixed rule and authorized changes. | Evaluates age without hidden scores or improvised timing. | Declared lifecycle policy. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-7M.11.4.4 — Bundle 4 cooling_rule_id_and_version | The rule's exact identity and version. | Records which rule was evaluated. | Versioned evaluation provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 3 · ACCEPTED | C-7M.11.3.3 — Computed View active-to-cold operation | The fixed declared versioned cooling rule. | Establishes old-enough status under that rule while separately requiring no genuine use or valid new links. | No improvised age value. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 4 · ACCEPTED | C-7D.17.9 — B6 operational-record active-cold lifecycle | New operational records, actual authorized use, valid new links, protection conditions and the declared rule. | Supplies fixed versioned rule and approval for any future rule change. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.11.3.3 — Computed View active-to-cold operation
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The accepted cooling operation when both settled conditions are established. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — Age under the fixed declared versioned rule, and absence of genuine use and valid new links. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Cools only when both conditions hold, appending a status event. Changes only active/cold presentation and retrieval priority. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — A cold status event with unchanged original record and provenance. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Cool on age alone or inactivity alone; edit, delete, weaken, disconnect, overwrite or replace the record; change evidence, truth, grounding, authority or history; block authorized exact retrieval. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — If eligibility cannot safely be determined, previous status is preserved and failed evaluation is recorded. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

TOGETHER
- Fed by: DESIGNED — C-7B.10.6.1.2.1 — Cooling age condition: declared age condition; C-7B.10.6.1.2.2 — Cooling use and link condition: no genuine use and no valid new links. [V10 §0B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gated by: ACCEPTED — C-7M.11.3.1 — Computed View active-log protection conditions: an active protection prevents cooling; C-7M.11.3.2 — Computed View cooling-rule ownership: the fixed versioned rule governs age. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Changes: ACCEPTED — C-7M.11.3 — Computed View operational-record lifecycle: supplies the append-only cooling operation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11.3 — Computed View operational-record lifecycle | Both established cooling conditions. | Appends cold status while preserving the operational record. | Priority changes only. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-7D.17.9 — B6 operational-record active-cold lifecycle | New operational records, actual authorized use, valid new links, protection conditions and the declared rule. | Supplies both cooling conditions. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.11.3.4 — Computed View cold-record reactivation
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The accepted reactivation operation for actual authorized use or a valid new link to active work. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — Actual authorized operation use, or a new link valid under the governing connection rule. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Appends active status, preserves the cold history and original record, and requires no additional manual approval unless the particular link's governing rule already requires it. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — An active lifecycle event grounded in actual use or a valid active-work link. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Reactivate from retrieval, semantic similarity, resemblance, co-retrieval, ranking proximity, time, model confidence or repetition alone; turn reactivation into new evidence or another vote. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — Uncertain eligibility preserves the prior status and records a failed evaluation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

TOGETHER
- Fed by: DESIGNED — C-7B.10.6.3.1 — Reasoning-use reactivation condition: actual-use condition; C-7B.10.6.3.2 — Valid-link reactivation condition: valid-link condition; C-7B.10.6.2.2 — Semantic cold-retrieval fallback: semantic retrieval remains only a fallback until genuine use or a valid link occurs. [V10 §0B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.11.3 — Computed View operational-record lifecycle: supplies permitted reactivation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11.3 — Computed View operational-record lifecycle | The actual-use or valid-link basis. | Appends active status without changing the original record. | Preserved cold history and evidence strength. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-7D.17.9 — B6 operational-record active-cold lifecycle | New operational records, actual authorized use, valid new links, protection conditions and the declared rule. | Supplies use/link reactivation; gates this place: reactivation requires actual authorized use or a valid new link. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.11.3.5 — Computed View uncertain status evaluation
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The honest outcome when cooling or reactivation eligibility cannot be safely determined. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — The uncertain evaluation and previous active/cold status. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Preserves previous status and records the failed evaluation as its own operation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — A failed-evaluation record with unchanged prior active/cold state. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Invent a third lifecycle status or silently cool, reactivate, hide, drop or reprioritize the record. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — The previous active/cold state remains and no evidence or authority changes. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7M.9 — Computed View operation and recovery contract: the status evaluation is one operation under the stable commit/recovery contract. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Changes: ACCEPTED — C-7M.11.3 — Computed View operational-record lifecycle: supplies status-evaluation failure behavior. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11.3 — Computed View operational-record lifecycle | The undetermined eligibility and prior state. | Preserves status and records failure. | No silent lifecycle change. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-7D.17.9 — B6 operational-record active-cold lifecycle | New operational records, actual authorized use, valid new links, protection conditions and the declared rule. | Supplies uncertain evaluation. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.11.4 — Bundle 4 operational-record lifecycle-status event
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The separate conceptual append-only lifecycle/status event schema for Bundle 4 operational records. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — Lifecycle event and operational-record identities; operation identity; owner; rule/version; previous/new status; reason; triggering use/link; authorization; time; evaluation outcome; failure reason; operational-log reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Records exact active/cold status through events. The first event records active at commitment with previous_status empty because no earlier status exists. Reuses the common operation, creation-time and log-reference fields. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — An immutable lifecycle/status event linked to the separately preserved operational record. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Write lifecycle status onto the original record, merge the event with a domain event, invent a third state on failure or fabricate a previous status for the first event. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — An undetermined status evaluation records failure and preserves the previous state. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

TOGETHER
- Fed by: ACCEPTED — C-7M.11.4.1 — Bundle 4 lifecycle_event_id: lifecycle_event_id; C-7M.11.4.2 — Bundle 4 operational_record_id: operational_record_id; C-7M.5.2 — Computed View operation_id: operation_id; C-7M.11.4.3 — Bundle 4 lifecycle component_owner: component_owner; C-7M.11.4.4 — Bundle 4 cooling_rule_id_and_version: cooling_rule_id_and_version; C-7M.11.4.5 — Bundle 4 lifecycle previous_status: previous_status; C-7M.11.4.6 — Bundle 4 lifecycle new_status: new_status; C-7M.11.4.7 — Bundle 4 lifecycle reason: reason; C-7M.11.4.8 — Bundle 4 triggering_use_or_link_reference: triggering_use_or_link_reference; C-7M.11.4.9 — Bundle 4 lifecycle authorization_reference: authorization_reference; C-7M.3.17 — Computed View record created_at: created_at; C-7M.11.4.10 — Bundle 4 lifecycle evaluation_outcome: evaluation_outcome; C-7M.11.4.11 — Bundle 4 lifecycle failure_reason_if_any: failure_reason_if_any; C-7M.3.19 — Computed View operational-log references: operational_log_reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gated by: ACCEPTED — C-7M.11.3 — Computed View operational-record lifecycle: the active/cold lifecycle supplies permitted transitions and failure preservation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Changes: ACCEPTED — C-7M.11 — Computed View operational records and lifecycle: supplies the separate lifecycle-event record. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11 — Computed View operational records and lifecycle | The separate lifecycle/status events. | Derives operational-record status without mutation. | Preserved status history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-7M.11.4.1 — Bundle 4 lifecycle_event_id | The lifecycle/status event's distinct required field contract. | Supplies lifecycle_event_id. | Complete append-only two-state lifecycle provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 3 · ACCEPTED | C-7M.11.4.2 — Bundle 4 operational_record_id | The lifecycle/status event's distinct required field contract. | Supplies operational_record_id. | Complete append-only two-state lifecycle provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 4 · ACCEPTED | C-7M.11.4.3 — Bundle 4 lifecycle component_owner | The lifecycle/status event's distinct required field contract. | Supplies component_owner. | Complete append-only two-state lifecycle provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 5 · ACCEPTED | C-7M.11.4.4 — Bundle 4 cooling_rule_id_and_version | The lifecycle/status event's distinct required field contract. | Supplies cooling_rule_id_and_version. | Complete append-only two-state lifecycle provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 6 · ACCEPTED | C-7M.11.4.5 — Bundle 4 lifecycle previous_status | The lifecycle/status event's distinct required field contract. | Supplies previous_status. | Complete append-only two-state lifecycle provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 7 · ACCEPTED | C-7M.11.4.6 — Bundle 4 lifecycle new_status | The lifecycle/status event's distinct required field contract. | Supplies new_status. | Complete append-only two-state lifecycle provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 8 · ACCEPTED | C-7M.11.4.7 — Bundle 4 lifecycle reason | The lifecycle/status event's distinct required field contract. | Supplies the lifecycle reason. | Complete append-only two-state lifecycle provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 9 · ACCEPTED | C-7M.11.4.8 — Bundle 4 triggering_use_or_link_reference | The lifecycle/status event's distinct required field contract. | Supplies triggering_use_or_link_reference. | Complete append-only two-state lifecycle provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 10 · ACCEPTED | C-7M.11.4.9 — Bundle 4 lifecycle authorization_reference | The lifecycle/status event's distinct required field contract. | Supplies authorization_reference. | Complete append-only two-state lifecycle provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 11 · ACCEPTED | C-7M.11.4.10 — Bundle 4 lifecycle evaluation_outcome | The lifecycle/status event's distinct required field contract. | Supplies evaluation_outcome. | Complete append-only two-state lifecycle provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 12 · ACCEPTED | C-7M.11.4.11 — Bundle 4 lifecycle failure_reason_if_any | The lifecycle/status event's distinct required field contract. | Supplies failure_reason_if_any. | Complete append-only two-state lifecycle provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 13 · ACCEPTED | C-7M.11.5 — Bundle 4 domain-log-lifecycle separation | The operational-record active/cold event as a third record kind. | Keeps it separate from the operational record and domain refresh event. | No substitution or double-counting. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 14 · ACCEPTED | C-7O.11 — Result-return operational records | Each real operation, evaluated/used/unused material, omissions and reasons, success/failure, retry/recovery, prior-record use and resulting IDs. | Supplies fourteen-field lifecycle-status event. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 15 · ACCEPTED | C-7N.12.3.3 — Surfacing active-to-cold operation | An active record and both established cooling conditions. | Supplies the append-only lifecycle event. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 16 · ACCEPTED | C-7N.12 — Surfacing and presentation operational records | Each real operation, what it evaluated, used, did not use or omitted, its reasons and resulting object IDs. | Supplies the shared fourteen-field lifecycle-status event. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 17 · ACCEPTED | C-7N.12.3.4 — Surfacing cold-record reactivation | One of those two real triggers. | Supplies shared lifecycle-status event. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 18 · ACCEPTED | C-7N.12.3 — Surfacing operational-record active-cold lifecycle | A newly committed record or a governed status evaluation. | Supplies the shared lifecycle event. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 19 · ACCEPTED | C-7P.13.3 — B8 authority-record lifecycle consumption | Every newly committed B8 operational record, actual use, valid new links, the declared cooling rule and recovery/correction needs. | Supplies the fourteen-field lifecycle/status event and initial active event. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 20 · ACCEPTED | C-7N.12.3.5 — Surfacing failed lifecycle-status evaluation | An unsafe or uncertain status evaluation. | Supplies evaluation outcome and failure reason on the shared lifecycle record. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 21 · ACCEPTED | C-7D.17.9 — B6 operational-record active-cold lifecycle | New operational records, actual authorized use, valid new links, protection conditions and the declared rule. | Supplies the fourteen-field lifecycle/status event with initial active and empty previous_status. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: C-7M.11.4.1 — Bundle 4 lifecycle_event_id; C-7M.11.4.2 — Bundle 4 operational_record_id; C-7M.11.4.3 — Bundle 4 lifecycle component_owner; C-7M.11.4.4 — Bundle 4 cooling_rule_id_and_version; C-7M.11.4.5 — Bundle 4 lifecycle previous_status; C-7M.11.4.6 — Bundle 4 lifecycle new_status; C-7M.11.4.7 — Bundle 4 lifecycle reason; C-7M.11.4.8 — Bundle 4 triggering_use_or_link_reference; C-7M.11.4.9 — Bundle 4 lifecycle authorization_reference; C-7M.11.4.10 — Bundle 4 lifecycle evaluation_outcome; C-7M.11.4.11 — Bundle 4 lifecycle failure_reason_if_any

### C-7M.11.4.1 — Bundle 4 lifecycle_event_id
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The identity of an operational-record lifecycle/status event. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — The lifecycle event being committed. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Identifies the event separately from the operational record and domain event. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — lifecycle_event_id. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Conflate lifecycle-event identity with a snapshot or operation identity. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.11.4 — Bundle 4 operational-record lifecycle-status event: supplies lifecycle_event_id. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11.4 — Bundle 4 operational-record lifecycle-status event | The lifecycle-event identity. | Makes the append-only status event referenceable. | Distinct event history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.11.4.2 — Bundle 4 operational_record_id
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The lifecycle event's reference to the operational record whose status is evaluated. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — That preserved operational record's identity. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Links the status event to its subject operational record. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — operational_record_id. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Substitute a domain snapshot or refresh-event identity for the operational record. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.11.4 — Bundle 4 operational-record lifecycle-status event: supplies operational_record_id. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11.4 — Bundle 4 operational-record lifecycle-status event | The subject operational-record ID. | Relates the status evaluation to the correct preserved record. | No record-kind confusion. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.11.4.3 — Bundle 4 lifecycle component_owner
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The consuming component owning the operational record's lifecycle rule. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — The actual rule-owning component. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Records component_owner for this evaluation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — component_owner. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Silently move cooling-rule ownership to another component. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.11.4 — Bundle 4 operational-record lifecycle-status event: supplies component_owner. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11.4 — Bundle 4 operational-record lifecycle-status event | The owning component. | Preserves who owns the evaluated lifecycle policy. | Explicit rule ownership. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.11.4.4 — Bundle 4 cooling_rule_id_and_version
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The exact fixed declared cooling rule and version used by a lifecycle evaluation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — The owning component's operative rule identity/version. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Records the exact evaluated version. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — cooling_rule_id_and_version. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Replace the evaluated version with an unapproved proposal or silently current rule. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7M.11.3.2 — Computed View cooling-rule ownership: fixed rule identity and approved version history. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.11.4 — Bundle 4 operational-record lifecycle-status event: supplies cooling_rule_id_and_version. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11.4 — Bundle 4 operational-record lifecycle-status event | The exact cooling-rule version. | Binds the status evaluation to its policy. | Inspectable version provenance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-7M.11.3.2 — Computed View cooling-rule ownership | The exact cooling-rule identity/version carried by evaluation events. | Keeps component-owned policy versions traceable through their actual evaluations. | No silent rule replacement. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 3 · ACCEPTED | C-7N.12.3.2 — B8 and B27 owned cooling rules | Record category, operation/lifecycle status and the declared rule version. | Supplies shared cooling_rule_id_and_version. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.11.4.5 — Bundle 4 lifecycle previous_status
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The previous active/cold status in a lifecycle event, empty on the first event. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — The prior valid status, if a prior status exists. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Records active or cold when applicable; leaves previous_status empty for the initial active-at-commit event. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — previous_status with the explicit initial-empty case. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Invent a predecessor for a newly committed record or use a third lifecycle state. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — An uncertain evaluation preserves the prior valid status. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.11.4 — Bundle 4 operational-record lifecycle-status event: supplies previous_status. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11.4 — Bundle 4 operational-record lifecycle-status event | The prior status or first-event absence. | Preserves the real lifecycle sequence. | No invented status history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.11.4.6 — Bundle 4 lifecycle new_status
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The resulting operational-record status, exactly active or cold. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — The established lifecycle result; initial commitment always yields active. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Records new_status through an append-only event rather than editing the record. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — new_status: active or cold. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Invent failed, unknown or another third state; start a newly committed record cold. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — Failure to determine eligibility preserves the previous status. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.11.4 — Bundle 4 operational-record lifecycle-status event: supplies new_status. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11.4 — Bundle 4 operational-record lifecycle-status event | The exact permitted resulting status. | Records an initial active or valid later lifecycle result. | Two-state lifecycle integrity. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.11.4.7 — Bundle 4 lifecycle reason
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The reason field explaining a lifecycle/status event. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — The actual evaluation or transition basis. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Records the reason for the event. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — reason. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Present a similarity-only encounter as actual-use or valid-link reactivation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.11.4 — Bundle 4 operational-record lifecycle-status event: supplies the lifecycle reason. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11.4 — Bundle 4 operational-record lifecycle-status event | The actual reason. | Explains the status evaluation without invented support. | Traceable lifecycle consequences. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.11.4.8 — Bundle 4 triggering_use_or_link_reference
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The reference to the actual use or valid link triggering a lifecycle evaluation where applicable. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — The triggering authorized use or governing-rule-valid link. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Preserves its reference separately from the textual reason. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — triggering_use_or_link_reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Manufacture a valid link from co-retrieval, resemblance or ranking proximity. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.11.4 — Bundle 4 operational-record lifecycle-status event: supplies triggering_use_or_link_reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11.4 — Bundle 4 operational-record lifecycle-status event | The triggering-use/link reference. | Keeps the actual trigger inspectable. | No similarity-based reactivation disguised as use. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.11.4.9 — Bundle 4 lifecycle authorization_reference
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The lifecycle event's reference to the applicable authorization basis. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — The authorization governing the evaluation, actual use or link. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Records authorization_reference while existing access rules remain binding. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — authorization_reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Treat a historical reference as wider current access or automatic approval of a proposed link. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — Unauthorized use cannot supply the authorized-use reactivation condition. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7B.10.8 — Operational-record access boundary: existing operational-record access rules remain applicable. [V10 §0B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Changes: ACCEPTED — C-7M.11.4 — Bundle 4 operational-record lifecycle-status event: supplies authorization_reference. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11.4 — Bundle 4 operational-record lifecycle-status event | The applicable authorization reference. | Keeps the use/evaluation basis inspectable. | No lifecycle-derived access grant. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.11.4.10 — Bundle 4 lifecycle evaluation_outcome
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The outcome of the status-evaluation operation, distinct from active/cold status. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — The actual successful or failed evaluation result. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Records evaluation_outcome separately from new_status. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — The honest evaluation_outcome. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Convert evaluation failure into a third lifecycle status or silent reprioritization. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — An unsafe-to-determine evaluation is recorded as failed while previous status remains. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.11.4 — Bundle 4 operational-record lifecycle-status event: supplies evaluation_outcome. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11.4 — Bundle 4 operational-record lifecycle-status event | The actual evaluation outcome. | Distinguishes operation failure from lifecycle state. | No fabricated third status. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.11.4.11 — Bundle 4 lifecycle failure_reason_if_any
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The status-evaluation event's failure reason where a failure occurred. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — The actual reason eligibility could not safely be determined. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Records failure_reason_if_any with the failed evaluation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — The applicable failure reason. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Hide uncertainty by recording a successful transition without established eligibility. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — Previous status remains unchanged when eligibility is not safely determined. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.11.4 — Bundle 4 operational-record lifecycle-status event: supplies failure_reason_if_any. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11.4 — Bundle 4 operational-record lifecycle-status event | The failure reason where applicable. | Explains the preserved-state failed evaluation. | Honest status-evaluation history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |

SUB-PARTS: NONE

### C-7M.11.5 — Bundle 4 domain-log-lifecycle separation
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The separation of domain events, operational records and operational-record lifecycle/status events. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Takes in: ACCEPTED — The domain refresh outcome, its one connected operational log and the log's separate active/cold history. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Does: ACCEPTED — Links the three kinds without merging them. Domain events reference their operational record; lifecycle events concern operational-record status only. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gives out: ACCEPTED — Three distinct, linked record kinds with their own identities and roles. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Must never: ACCEPTED — Treat a refresh/currentness/world-membership/action-result event as an operational log or active/cold event; substitute one kind for another or double-count them. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7M.6 — Computed View refresh-status event: refresh/status domain event; C-7M.11.1 — Computed View operation-record content: operation content; C-7M.11.4 — Bundle 4 operational-record lifecycle-status event: operational-record lifecycle event. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]
- Gated by: NOT DECIDED
- Changes: ACCEPTED — C-7M.11 — Computed View operational records and lifecycle: supplies record-kind separation. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7M.11 — Computed View operational records and lifecycle | The separate domain, operation and lifecycle references. | Preserves each kind and its own meaning. | No merged or doubled history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-7P.13.2 — Authority operational logging and stage honesty | What was evaluated, used, unused, omitted and why. | Supplies separate domain, operational and lifecycle record kinds. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 3 · ACCEPTED | C-7P.13.3 — B8 authority-record lifecycle consumption | Every newly committed B8 operational record, actual use, valid new links, the declared cooling rule and recovery/correction needs. | Supplies domain/log/lifecycle separation. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 4 · ACCEPTED | C-7D.17.9 — B6 operational-record active-cold lifecycle | New operational records, actual authorized use, valid new links, protection conditions and the declared rule. | Supplies separate record kinds. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 5 · ACCEPTED | C-7N.12 — Surfacing and presentation operational records | Each real operation, what it evaluated, used, did not use or omitted, its reasons and resulting object IDs. | Supplies domain/log/lifecycle three-kind separation. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 6 · ACCEPTED | C-7O.11 — Result-return operational records | Each real operation, evaluated/used/unused material, omissions and reasons, success/failure, retry/recovery, prior-record use and resulting IDs. | Supplies the three separate record kinds. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 7 · ACCEPTED | C-7D.17.8 — B6 connected operational record | What was evaluated, used and not used. | Supplies domain event, operational log and lifecycle-event separation. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] [MAP C-7D] |

SUB-PARTS: NONE

### C-7M.12 — Computed View provisional-creation influence
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The permitted current-picture influence of relevant provisional creation material with its status preserved. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Takes in: ACCEPTED — A provisional creation record used by an otherwise authorized view operation, its identity and status at use time. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Does: ACCEPTED — Allows the influence only through an operation whose own record carries provisional_material_used. Keeps the output context explicitly provisional and the operation traceable; does not confirm material through use. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gives out: ACCEPTED — Relevant provisional influence visibly identified as provisional, with record identity and status-at-use in the operation log. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Must never: ACCEPTED — Silently influence the picture or relabel a provisional record as fact, adopted rule, final decision or settled creation; confirm it through repetition, retrieval, elapsed time or model confidence. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — An unverifiable creation status reads as provisional; no untraceable or unmarked provisional influence is permitted. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-CREATE.8.5 — Provisional influence in Computed View: the accepted view-influence interface; C-CREATE.8.1 — provisional_material_used: provisional_material_used; C-CREATE.8.1.1 — Provisional-use record identity: used record identity; C-CREATE.8.1.2 — Creation status at use time: creation status at use time. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7M.11 — Computed View operational records and lifecycle: the actual using operation's own record must carry the provisional-use entry. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]
- Changes: DESIGNED — C-7M — Computed View (§7M): supplies permitted provisional influence without making it settled. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M — Computed View (§7M) | The relevant provisional material with its use/status record. | Preserves provisional context in current assembly. | No silent confirmation or settled-fact claim. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7M.13 — Computed View metadata-only held-content boundary
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The consumer boundary permitting only safe source-carried metadata, lifecycle state and blockers from pre-ingest held material. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Takes in: ACCEPTED — Authorized safe metadata-only references, never held raw content or reconstructed content. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Does: ACCEPTED — Carries only the permitted metadata/state/blocker information into assembly and snapshot references. Keeps raw held material outside ranking, interpretation, output and evidence support. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Gives out: ACCEPTED — A safe metadata-only reference with its actual lifecycle limitations. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Must never: ACCEPTED — Inspect, rank, infer from, reconstruct or snapshot held raw content; introduce a sealed-TSC inspection path or turn protected metadata into a route to underlying content. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — Held raw or unauthorized material cannot influence assembly, regardless of apparent relevance or a requested view inspection. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12]

TOGETHER
- Fed by: DESIGNED — C-7E.11 — Held-content access boundary: the existing DESIGNED safe metadata/lifecycle/blocker source interface. [V10 §7M] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): purpose privacy, compartment and influence-removal authorization remains prior to use; C-TSC — Temporary Session Cache (§7E-TSC): sealed or retained archive material supplies no inspection path. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Changes: DESIGNED — C-7M — Computed View (§7M): confines held-material assembly to safe metadata. [V10 §7M] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Changes: ACCEPTED — C-7M.5.5.10 — Computed View safe pre-ingest metadata references: constrains snapshot metadata-only held references. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7M — Computed View (§7M) | Safe metadata, lifecycle state and blockers. | Uses only the permitted metadata-only interface. | No raw-content influence. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 2 · ACCEPTED | C-7M.5.5.10 — Computed View safe pre-ingest metadata references | The safe metadata boundary. | References permitted held metadata only. | No hidden-content snapshot. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-7M.5.5 — Computed View snapshot source-reference fields | The safe-metadata-only held-material boundary. | Keeps the source-reference collection free of held raw content and TSC inspection paths. | Only safe source-carried metadata, lifecycle state and blockers may be referenced. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece USED BY continuations

These rows add the reciprocal USED BY entries to the named external cards at assembly. They preserve the delivered cards; every row names both ends. The relationship wording is carried from the current TOGETHER field.

| Current card | Field | External card receiving USED BY row | Stamp | Relationship and condition | Source |
|---|---|---|---|---|---|
| C-7M — Computed View (§7M) | Fed by | C-STORE — Accretive store & sealed roots (§6B) | BUILT | C-STORE — Accretive store & sealed roots (§6B): immutable direct roots; C-READ — Reading record, validator, writer (§6B): immutable reading records and their root links. | [V10 §6A] [V10 §6B] |
| C-7M — Computed View (§7M) | Fed by | C-READ — Reading record, validator, writer (§6B) | BUILT | C-STORE — Accretive store & sealed roots (§6B): immutable direct roots; C-READ — Reading record, validator, writer (§6B): immutable reading records and their root links. | [V10 §6A] [V10 §6B] |
| C-7M — Computed View (§7M) | Fed by | C-7K — Story Layer (§7K) | DESIGNED | C-7K — Story Layer (§7K): perspective-owned tellings; C-7J — Clash Handling (§7J): preserved clashes; C-7J.6 — Ness response as separate event: separate Ness responses; C-7L — Person-Boxes (§7L): person-linked source objects; C-7D — Living State Web (§7D): grounded state and world-model source references, strictly upstream; C-7E.11 — Held-content access boundary: safe held metadata, lifecycle state and blockers; C-7GA.11.7.2 — Step 7B — Process triggered view profiles: triggered internal profile-update requests in CY-A. | [MAP C-7M] [V10 §7M] [V10 §7G-A] |
| C-7M — Computed View (§7M) | Fed by | C-7J — Clash Handling (§7J) | DESIGNED | C-7K — Story Layer (§7K): perspective-owned tellings; C-7J — Clash Handling (§7J): preserved clashes; C-7J.6 — Ness response as separate event: separate Ness responses; C-7L — Person-Boxes (§7L): person-linked source objects; C-7D — Living State Web (§7D): grounded state and world-model source references, strictly upstream; C-7E.11 — Held-content access boundary: safe held metadata, lifecycle state and blockers; C-7GA.11.7.2 — Step 7B — Process triggered view profiles: triggered internal profile-update requests in CY-A. | [MAP C-7M] [V10 §7M] [V10 §7G-A] |
| C-7M — Computed View (§7M) | Fed by | C-7J.6 — Ness response as separate event | DESIGNED | C-7K — Story Layer (§7K): perspective-owned tellings; C-7J — Clash Handling (§7J): preserved clashes; C-7J.6 — Ness response as separate event: separate Ness responses; C-7L — Person-Boxes (§7L): person-linked source objects; C-7D — Living State Web (§7D): grounded state and world-model source references, strictly upstream; C-7E.11 — Held-content access boundary: safe held metadata, lifecycle state and blockers; C-7GA.11.7.2 — Step 7B — Process triggered view profiles: triggered internal profile-update requests in CY-A. | [MAP C-7M] [V10 §7M] [V10 §7G-A] |
| C-7M — Computed View (§7M) | Fed by | C-7L — Person-Boxes (§7L) | DESIGNED | C-7K — Story Layer (§7K): perspective-owned tellings; C-7J — Clash Handling (§7J): preserved clashes; C-7J.6 — Ness response as separate event: separate Ness responses; C-7L — Person-Boxes (§7L): person-linked source objects; C-7D — Living State Web (§7D): grounded state and world-model source references, strictly upstream; C-7E.11 — Held-content access boundary: safe held metadata, lifecycle state and blockers; C-7GA.11.7.2 — Step 7B — Process triggered view profiles: triggered internal profile-update requests in CY-A. | [MAP C-7M] [V10 §7M] [V10 §7G-A] |
| C-7M — Computed View (§7M) | Fed by | C-7D — Living State Web (§7D) | DESIGNED | C-7K — Story Layer (§7K): perspective-owned tellings; C-7J — Clash Handling (§7J): preserved clashes; C-7J.6 — Ness response as separate event: separate Ness responses; C-7L — Person-Boxes (§7L): person-linked source objects; C-7D — Living State Web (§7D): grounded state and world-model source references, strictly upstream; C-7E.11 — Held-content access boundary: safe held metadata, lifecycle state and blockers; C-7GA.11.7.2 — Step 7B — Process triggered view profiles: triggered internal profile-update requests in CY-A. | [MAP C-7M] [V10 §7M] [V10 §7G-A] |
| C-7M — Computed View (§7M) | Fed by | C-7E.11 — Held-content access boundary | DESIGNED | C-7K — Story Layer (§7K): perspective-owned tellings; C-7J — Clash Handling (§7J): preserved clashes; C-7J.6 — Ness response as separate event: separate Ness responses; C-7L — Person-Boxes (§7L): person-linked source objects; C-7D — Living State Web (§7D): grounded state and world-model source references, strictly upstream; C-7E.11 — Held-content access boundary: safe held metadata, lifecycle state and blockers; C-7GA.11.7.2 — Step 7B — Process triggered view profiles: triggered internal profile-update requests in CY-A. | [MAP C-7M] [V10 §7M] [V10 §7G-A] |
| C-7M — Computed View (§7M) | Fed by | C-7GA.11.7.2 — Step 7B — Process triggered view profiles | DESIGNED | C-7K — Story Layer (§7K): perspective-owned tellings; C-7J — Clash Handling (§7J): preserved clashes; C-7J.6 — Ness response as separate event: separate Ness responses; C-7L — Person-Boxes (§7L): person-linked source objects; C-7D — Living State Web (§7D): grounded state and world-model source references, strictly upstream; C-7E.11 — Held-content access boundary: safe held metadata, lifecycle state and blockers; C-7GA.11.7.2 — Step 7B — Process triggered view profiles: triggered internal profile-update requests in CY-A. | [MAP C-7M] [V10 §7M] [V10 §7G-A] |
| C-7M — Computed View (§7M) | Fed by | C-READ.10.14 — Telling-reference handoff | ACCEPTED | C-READ.10.14 — Telling-reference handoff: eligible first-class telling references; C-7J.7 — Downstream effects of clashes: conflicted evidence and downstream display limits; C-7L.4 — Ness's confirmed Person-Box: Ness's confirmed person anchor; C-CREATE.8.5 — Provisional influence in Computed View: relevant marked provisional influence within its accepted boundary. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| C-7M — Computed View (§7M) | Fed by | C-7J.7 — Downstream effects of clashes | ACCEPTED | C-READ.10.14 — Telling-reference handoff: eligible first-class telling references; C-7J.7 — Downstream effects of clashes: conflicted evidence and downstream display limits; C-7L.4 — Ness's confirmed Person-Box: Ness's confirmed person anchor; C-CREATE.8.5 — Provisional influence in Computed View: relevant marked provisional influence within its accepted boundary. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| C-7M — Computed View (§7M) | Fed by | C-7L.4 — Ness's confirmed Person-Box | ACCEPTED | C-READ.10.14 — Telling-reference handoff: eligible first-class telling references; C-7J.7 — Downstream effects of clashes: conflicted evidence and downstream display limits; C-7L.4 — Ness's confirmed Person-Box: Ness's confirmed person anchor; C-CREATE.8.5 — Provisional influence in Computed View: relevant marked provisional influence within its accepted boundary. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| C-7M — Computed View (§7M) | Fed by | C-CREATE.8.5 — Provisional influence in Computed View | ACCEPTED | C-READ.10.14 — Telling-reference handoff: eligible first-class telling references; C-7J.7 — Downstream effects of clashes: conflicted evidence and downstream display limits; C-7L.4 — Ness's confirmed Person-Box: Ness's confirmed person anchor; C-CREATE.8.5 — Provisional influence in Computed View: relevant marked provisional influence within its accepted boundary. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| C-7M — Computed View (§7M) | Gated by | C-7A — Universal Filter (§7A) | DESIGNED | C-7M.1 — Computed View internal-use boundary: quiet internal use does not permit unprompted display; C-7A — Universal Filter (§7A): preserve the history of meaning; C-7A.9.3 — Current-use separation: current use never rewrites HISTORY; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): purpose-specific privacy authorization precedes assembly and relevance; C-7R — Attention & Relevance Control (§7R): run only the valid declaration for the purpose; C-7P — Permission & Authority Boundaries (§7P): authority governs action-adjacent uses and operational writes; C-SACL — Speaker Access-Control Layer (§25.4): applicable visible output passes speaker access after privacy. | [V10 §7A] [V10 §7M] [V10 §7Q] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] |
| C-7M — Computed View (§7M) | Gated by | C-7A.9.3 — Current-use separation | DESIGNED | C-7M.1 — Computed View internal-use boundary: quiet internal use does not permit unprompted display; C-7A — Universal Filter (§7A): preserve the history of meaning; C-7A.9.3 — Current-use separation: current use never rewrites HISTORY; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): purpose-specific privacy authorization precedes assembly and relevance; C-7R — Attention & Relevance Control (§7R): run only the valid declaration for the purpose; C-7P — Permission & Authority Boundaries (§7P): authority governs action-adjacent uses and operational writes; C-SACL — Speaker Access-Control Layer (§25.4): applicable visible output passes speaker access after privacy. | [V10 §7A] [V10 §7M] [V10 §7Q] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] |
| C-7M — Computed View (§7M) | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7M.1 — Computed View internal-use boundary: quiet internal use does not permit unprompted display; C-7A — Universal Filter (§7A): preserve the history of meaning; C-7A.9.3 — Current-use separation: current use never rewrites HISTORY; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): purpose-specific privacy authorization precedes assembly and relevance; C-7R — Attention & Relevance Control (§7R): run only the valid declaration for the purpose; C-7P — Permission & Authority Boundaries (§7P): authority governs action-adjacent uses and operational writes; C-SACL — Speaker Access-Control Layer (§25.4): applicable visible output passes speaker access after privacy. | [V10 §7A] [V10 §7M] [V10 §7Q] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] |
| C-7M — Computed View (§7M) | Gated by | C-7R — Attention & Relevance Control (§7R) | DESIGNED | C-7M.1 — Computed View internal-use boundary: quiet internal use does not permit unprompted display; C-7A — Universal Filter (§7A): preserve the history of meaning; C-7A.9.3 — Current-use separation: current use never rewrites HISTORY; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): purpose-specific privacy authorization precedes assembly and relevance; C-7R — Attention & Relevance Control (§7R): run only the valid declaration for the purpose; C-7P — Permission & Authority Boundaries (§7P): authority governs action-adjacent uses and operational writes; C-SACL — Speaker Access-Control Layer (§25.4): applicable visible output passes speaker access after privacy. | [V10 §7A] [V10 §7M] [V10 §7Q] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] |
| C-7M — Computed View (§7M) | Gated by | C-7P — Permission & Authority Boundaries (§7P) | DESIGNED | C-7M.1 — Computed View internal-use boundary: quiet internal use does not permit unprompted display; C-7A — Universal Filter (§7A): preserve the history of meaning; C-7A.9.3 — Current-use separation: current use never rewrites HISTORY; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): purpose-specific privacy authorization precedes assembly and relevance; C-7R — Attention & Relevance Control (§7R): run only the valid declaration for the purpose; C-7P — Permission & Authority Boundaries (§7P): authority governs action-adjacent uses and operational writes; C-SACL — Speaker Access-Control Layer (§25.4): applicable visible output passes speaker access after privacy. | [V10 §7A] [V10 §7M] [V10 §7Q] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] |
| C-7M — Computed View (§7M) | Gated by | C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED | C-7M.1 — Computed View internal-use boundary: quiet internal use does not permit unprompted display; C-7A — Universal Filter (§7A): preserve the history of meaning; C-7A.9.3 — Current-use separation: current use never rewrites HISTORY; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): purpose-specific privacy authorization precedes assembly and relevance; C-7R — Attention & Relevance Control (§7R): run only the valid declaration for the purpose; C-7P — Permission & Authority Boundaries (§7P): authority governs action-adjacent uses and operational writes; C-SACL — Speaker Access-Control Layer (§25.4): applicable visible output passes speaker access after privacy. | [V10 §7A] [V10 §7M] [V10 §7Q] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] |
| C-7M — Computed View (§7M) | Gated by | C-READ.10.10 — Telling-set semantic eligibility | ACCEPTED | C-READ.10.10 — Telling-set semantic eligibility: complete-set semantic eligibility must hold before telling-specific view use. | [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §5A.1] |
| C-7M — Computed View (§7M) | Changes | C-7N — Action Surfacing (§7N) | DESIGNED | C-7N — Action Surfacing (§7N): supplies the internal current picture for possible-action surfacing under its own rules; C-7I — View Layer (§7I): supplies disclosed best-supported ordering when a view makes that claim. | [V10 §7M] [MAP C-7M] |
| C-7M — Computed View (§7M) | Changes | C-7I — View Layer (§7I) | DESIGNED | C-7N — Action Surfacing (§7N): supplies the internal current picture for possible-action surfacing under its own rules; C-7I — View Layer (§7I): supplies disclosed best-supported ordering when a view makes that claim. | [V10 §7M] [MAP C-7M] |
| C-7M.2.1 — Computed View factor 1 — current Ness judgment | Fed by | C-7J.6 — Ness response as separate event | DESIGNED | C-7J.6 — Ness response as separate event: separate response events whose explicit judgments may affect current use. | [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] |
| C-7M.2.2 — Computed View factor 2 — direct root evidence | Fed by | C-STORE — Accretive store & sealed roots (§6B) | BUILT | C-STORE — Accretive store & sealed roots (§6B): the immutable supporting roots addressed by their own IDs. | [V10 §6A] [V10 §6B] |
| C-7M.2.3 — Computed View factor 3 — reading acceptance and grounding | Fed by | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | DESIGNED | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): reading acceptance and grounding outcomes. | [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] |
| C-7M.2.4 — Computed View factor 4 — purpose relevance | Gated by | C-7R — Attention & Relevance Control (§7R) | DESIGNED | C-7R — Attention & Relevance Control (§7R): the current purpose must have a valid declared and validated relevance mode. | [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [V10 §7R] |
| C-7M.2.5 — Computed View factor 5 — context quality and provenance | Fed by | C-7F — Context Retrieval (§7F) | DESIGNED | C-7F — Context Retrieval (§7F): the labeled context channels and their retrieval provenance. | [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] |
| C-7M.2.6 — Computed View factor 6 — clashes and uncertainty | Fed by | C-7J.7 — Downstream effects of clashes | ACCEPTED | C-7J.7 — Downstream effects of clashes: preserved clash effects and qualification rules; C-7J.8 — Clash and named-gap presentation: beside-item clash presentation and response detail. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |
| C-7M.2.6 — Computed View factor 6 — clashes and uncertainty | Fed by | C-7J.8 — Clash and named-gap presentation | ACCEPTED | C-7J.7 — Downstream effects of clashes: preserved clash effects and qualification rules; C-7J.8 — Clash and named-gap presentation: beside-item clash presentation and response detail. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §16] |
| C-7M.3 — Computed View ordering-profile record | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7M.2 — Computed View seven-factor priority order: the seven-factor order remains fixed; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the profile and its use require their purpose's authorization. | [V10 §7M] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] |
| C-7M.3.3 — Computed View profile_purpose_type | Gated by | C-7R — Attention & Relevance Control (§7R) | DESIGNED | C-7R — Attention & Relevance Control (§7R): the controlled purpose must be recognized under its vocabulary/version. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [V10 §7R] |
| C-7M.3.6 — Computed View authorization and privacy basis | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the actual purpose and material must be permitted; C-7P — Permission & Authority Boundaries (§7P): action-adjacent operations remain within authority. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] |
| C-7M.3.6 — Computed View authorization and privacy basis | Gated by | C-7P — Permission & Authority Boundaries (§7P) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the actual purpose and material must be permitted; C-7P — Permission & Authority Boundaries (§7P): action-adjacent operations remain within authority. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] |
| C-7M.3.11 — Computed View Tier-1 configuration reference | Gated by | C-7R — Attention & Relevance Control (§7R) | DESIGNED | C-7R — Attention & Relevance Control (§7R): Tier 1 is owned and validated by Attention and Relevance Control. | [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |
| C-7M.4.3.1 — Computed View accepted-reading event trigger | Fed by | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | DESIGNED | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): the new accepted reading. | [V10 §7M / UPDATE TIMING] |
| C-7M.4.3.2 — Computed View active-clash event trigger | Fed by | C-7J — Clash Handling (§7J) | DESIGNED | C-7J — Clash Handling (§7J): the new or changed active-clash information. | [V10 §7M / UPDATE TIMING] |
| C-7M.4.3.3 — Computed View Ness-response event trigger | Fed by | C-7J.6 — Ness response as separate event | DESIGNED | C-7J.6 — Ness response as separate event: the separate preserved response event. | [V10 §7M / UPDATE TIMING] [V10 §7J] |
| C-7M.4.3.4 — Computed View theme-confirmation trigger | Fed by | C-7K.6.6.1 — confirm theme | ACCEPTED | C-7K.6.6.1 — confirm theme: Ness's recorded theme confirmation. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| C-7M.4.3.5 — Computed View identity-resolution trigger | Fed by | C-7L.3 — Person-Box proposal and identity events | ACCEPTED | C-7L.3 — Person-Box proposal and identity events: the accepted identity resolution and event history. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §7] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §12] |
| C-7M.5.4 — Computed View snapshot authorization-purpose basis | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the actual internal-use purpose and material must be authorized before assembly. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] |
| C-7M.5.5.1 — Computed View direct-root references | Fed by | C-STORE — Accretive store & sealed roots (§6B) | BUILT | C-STORE — Accretive store & sealed roots (§6B): the original immutable roots. | [V10 §6A] [V10 §6B] |
| C-7M.5.5.2 — Computed View reading references | Fed by | C-READ — Reading record, validator, writer (§6B) | BUILT | C-READ — Reading record, validator, writer (§6B): immutable reading records and their source links. | [V10 §6B] |
| C-7M.5.5.3 — Computed View telling references | Fed by | C-READ.10.14.4 — Computed View references | ACCEPTED | C-READ.10.14.4 — Computed View references: the existing Computed View telling-reference interface. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] |
| C-7M.5.5.3 — Computed View telling references | Gated by | C-READ.10.10.12 — Computed View use eligibility | ACCEPTED | C-READ.10.10.12 — Computed View use eligibility: complete-set eligibility before telling-specific Computed View use. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §6] |
| C-7M.5.5.4 — Computed View clash references | Fed by | C-7J — Clash Handling (§7J) | DESIGNED | C-7J — Clash Handling (§7J): preserved clash records. | [V10 §7J] [V10 §7M] |
| C-7M.5.5.5 — Computed View Ness-response references | Fed by | C-7J.6 — Ness response as separate event | DESIGNED | C-7J.6 — Ness response as separate event: separate preserved response events. | [V10 §7J] [V10 §7M] |
| C-7M.5.5.6 — Computed View Person-Box-link references | Fed by | C-7L — Person-Boxes (§7L) | DESIGNED | C-7L — Person-Boxes (§7L): stable identity anchors and provenance-bearing person links. | [V10 §7L] [V10 §7M] |
| C-7M.5.5.7 — Computed View theme references | Fed by | C-7K.6.1 — Theme record | ACCEPTED | C-7K.6.1 — Theme record: stable theme records and version/status history. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] |
| C-7M.5.5.8 — Computed View Living-State references | Fed by | C-7D — Living State Web (§7D) | DESIGNED | C-7D — Living State Web (§7D): grounded state objects and recorded currentness. | [V10 §7D] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] |
| C-7M.5.5.9 — Computed View world-model references | Fed by | C-7D — Living State Web (§7D) | DESIGNED | C-7D — Living State Web (§7D): the layered world-model source objects under its grounding rules. | [MAP C-7D] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §6] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] |
| C-7M.5.5.10 — Computed View safe pre-ingest metadata references | Fed by | C-7E.11 — Held-content access boundary | DESIGNED | C-7E.11 — Held-content access boundary: safe held metadata with raw content excluded from semantic use. | [V10 §7M] [V10 §7E] |
| C-7M.5.12 — Computed View privacy-output eligibility references | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): actual visible use requires privacy/output eligibility first; C-SACL — Speaker Access-Control Layer (§25.4): applicable speaker access is checked afterward. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] |
| C-7M.5.12 — Computed View privacy-output eligibility references | Gated by | C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): actual visible use requires privacy/output eligibility first; C-SACL — Speaker Access-Control Layer (§25.4): applicable speaker access is checked afterward. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] |
| C-7M.6.7 — Computed View retry_eligibility | Fed by | C-7H.9 — B9 retry-state architecture | ACCEPTED | C-7H.9 — B9 retry-state architecture: accepted B9 retry architecture; C-7H.10 — Accepted B9 retry values and episodes: accepted B9 values and episode rules. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| C-7M.6.7 — Computed View retry_eligibility | Fed by | C-7H.10 — Accepted B9 retry values and episodes | ACCEPTED | C-7H.9 — B9 retry-state architecture: accepted B9 retry architecture; C-7H.10 — Accepted B9 retry values and episodes: accepted B9 values and episode rules. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| C-7M.9 — Computed View operation and recovery contract | Gated by | C-7H.9 — B9 retry-state architecture | ACCEPTED | C-7H.9 — B9 retry-state architecture: accepted B9 mechanics; C-7H.10 — Accepted B9 retry values and episodes: recorded B9 values; C-7M.8 — Computed View duplicate prevention: idempotent commitment; C-7M.11 — Computed View operational records and lifecycle: separate append-only operational record. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| C-7M.9 — Computed View operation and recovery contract | Gated by | C-7H.10 — Accepted B9 retry values and episodes | ACCEPTED | C-7H.9 — B9 retry-state architecture: accepted B9 mechanics; C-7H.10 — Accepted B9 retry values and episodes: recorded B9 values; C-7M.8 — Computed View duplicate prevention: idempotent commitment; C-7M.11 — Computed View operational records and lifecycle: separate append-only operational record. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| C-7M.9.5 — Computed View bounded technical retry | Gated by | C-7H.9 — B9 retry-state architecture | ACCEPTED | C-7H.9 — B9 retry-state architecture: B9 mechanics; C-7H.10 — Accepted B9 retry values and episodes: accepted values and episodes; C-7M.8 — Computed View duplicate prevention: committed-outcome identity. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| C-7M.9.5 — Computed View bounded technical retry | Gated by | C-7H.10 — Accepted B9 retry values and episodes | ACCEPTED | C-7H.9 — B9 retry-state architecture: B9 mechanics; C-7H.10 — Accepted B9 retry values and episodes: accepted values and episodes; C-7M.8 — Computed View duplicate prevention: committed-outcome identity. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §13] |
| C-7M.10 — Computed View proposed RM-CV-01 declaration | Gated by | C-7R — Attention & Relevance Control (§7R) | DESIGNED | C-7R — Attention & Relevance Control (§7R): owns and validates Tier 1 under the settled declaration contract; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): purpose-specific internal-use authorization precedes relevance. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] |
| C-7M.10 — Computed View proposed RM-CV-01 declaration | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7R — Attention & Relevance Control (§7R): owns and validates Tier 1 under the settled declaration contract; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): purpose-specific internal-use authorization precedes relevance. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] |
| C-7M.10 — Computed View proposed RM-CV-01 declaration | Gated by | C-7F.6.14 — A4 eight-field declaration validity | ACCEPTED | C-7F.6.14 — A4 eight-field declaration validity: the existing eight-field validity contract applies before this consumer has a mode to run. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |
| C-7M.10.1 — Computed View proposed declaration identity and version | Gated by | C-7R — Attention & Relevance Control (§7R) | DESIGNED | C-7R — Attention & Relevance Control (§7R): the versioned proposal-and-confirmation path governs changes. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |
| C-7M.10.5 — Computed View graded-dimension selection | Gated by | C-7F.6.10.5.5 — Honest dimension absence | ACCEPTED | C-7F.6.10.5.5 — Honest dimension absence: the existing honest-absence outcome contract is reused under the proposed shared uncertainty rule. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| C-7M.10.5.4 — Computed View currentness_status selection | Fed by | C-7D — Living State Web (§7D) | DESIGNED | C-7D — Living State Web (§7D): supplies the recorded state-node status strictly upstream. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] |
| C-7M.10.6 — Computed View mouth-authorization boundary | Gated by | C-7R — Attention & Relevance Control (§7R) | DESIGNED | C-7R — Attention & Relevance Control (§7R): the settled version and validation rules govern any future declaration change. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| C-7M.10.9.4 — Computed View proposed shared unresolved handling | Fed by | C-7F.6.10.5.1 — Validated relevance value | ACCEPTED | C-7F.6.10.5.1 — Validated relevance value: validated interpretation; C-7F.6.10.5.2 — Failed relevance value: unused failed result; C-7F.6.10.5.3 — Unresolved relevance clue: weak unresolved clue; C-7F.6.10.5.4 — Relevance disagreement record handoff: disagreement handoff; C-7F.6.10.5.5 — Honest dimension absence: honest absence. These existing atoms are reused under the proposed shared rule, without changing their canonical names. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| C-7M.10.9.4 — Computed View proposed shared unresolved handling | Fed by | C-7F.6.10.5.2 — Failed relevance value | ACCEPTED | C-7F.6.10.5.1 — Validated relevance value: validated interpretation; C-7F.6.10.5.2 — Failed relevance value: unused failed result; C-7F.6.10.5.3 — Unresolved relevance clue: weak unresolved clue; C-7F.6.10.5.4 — Relevance disagreement record handoff: disagreement handoff; C-7F.6.10.5.5 — Honest dimension absence: honest absence. These existing atoms are reused under the proposed shared rule, without changing their canonical names. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| C-7M.10.9.4 — Computed View proposed shared unresolved handling | Fed by | C-7F.6.10.5.3 — Unresolved relevance clue | ACCEPTED | C-7F.6.10.5.1 — Validated relevance value: validated interpretation; C-7F.6.10.5.2 — Failed relevance value: unused failed result; C-7F.6.10.5.3 — Unresolved relevance clue: weak unresolved clue; C-7F.6.10.5.4 — Relevance disagreement record handoff: disagreement handoff; C-7F.6.10.5.5 — Honest dimension absence: honest absence. These existing atoms are reused under the proposed shared rule, without changing their canonical names. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| C-7M.10.9.4 — Computed View proposed shared unresolved handling | Fed by | C-7F.6.10.5.4 — Relevance disagreement record handoff | ACCEPTED | C-7F.6.10.5.1 — Validated relevance value: validated interpretation; C-7F.6.10.5.2 — Failed relevance value: unused failed result; C-7F.6.10.5.3 — Unresolved relevance clue: weak unresolved clue; C-7F.6.10.5.4 — Relevance disagreement record handoff: disagreement handoff; C-7F.6.10.5.5 — Honest dimension absence: honest absence. These existing atoms are reused under the proposed shared rule, without changing their canonical names. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| C-7M.10.9.4 — Computed View proposed shared unresolved handling | Fed by | C-7F.6.10.5.5 — Honest dimension absence | ACCEPTED | C-7F.6.10.5.1 — Validated relevance value: validated interpretation; C-7F.6.10.5.2 — Failed relevance value: unused failed result; C-7F.6.10.5.3 — Unresolved relevance clue: weak unresolved clue; C-7F.6.10.5.4 — Relevance disagreement record handoff: disagreement handoff; C-7F.6.10.5.5 — Honest dimension absence: honest absence. These existing atoms are reused under the proposed shared rule, without changing their canonical names. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| C-7M.10.9.4 — Computed View proposed shared unresolved handling | Gated by | C-7R — Attention & Relevance Control (§7R) | DESIGNED | C-7R — Attention & Relevance Control (§7R): Decision-11 records disagreement and the settled validation contract governs interpretation. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| C-7M.10.10 — Computed View relevance allowed-use boundary | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): purpose-specific internal authorization and influence-removal rules apply before relevance. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] |
| C-7M.10.11 — Computed View relevance evaluation record | Gated by | C-7R — Attention & Relevance Control (§7R) | DESIGNED | C-7R — Attention & Relevance Control (§7R): owns the settled Decision-12 relevance-event contract. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| C-7M.10.12 — Computed View invalid relevance declaration outcome | Gated by | C-7R — Attention & Relevance Control (§7R) | DESIGNED | C-7R — Attention & Relevance Control (§7R): Decision-14 halt and Decision-5 versioned proposal/confirmation govern the unknown-purpose route. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] |
| C-7M.11 — Computed View operational records and lifecycle | Gated by | C-7B.10.5 — Real-operation and evidence boundaries | DESIGNED | C-7B.10.5 — Real-operation and evidence boundaries: one real operation, no recursive logging and no doubled evidence; C-7B.10.8 — Operational-record access boundary: operational-record access remains governed by privacy, authority, identity/security, TSC, compartment and influence-removal rules. | [V10 §0B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| C-7M.11 — Computed View operational records and lifecycle | Gated by | C-7B.10.8 — Operational-record access boundary | DESIGNED | C-7B.10.5 — Real-operation and evidence boundaries: one real operation, no recursive logging and no doubled evidence; C-7B.10.8 — Operational-record access boundary: operational-record access remains governed by privacy, authority, identity/security, TSC, compartment and influence-removal rules. | [V10 §0B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| C-7M.11.1 — Computed View operation-record content | Fed by | C-7B.10.2 — Operational-record content contract | DECIDED-2026-09-25 | C-7B.10.2 — Operational-record content contract: existing operational-content atoms; C-7B.10.3 — Use and non-use records: existing use/non-use and omission atoms retain their ownership. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| C-7M.11.1 — Computed View operation-record content | Fed by | C-7B.10.3 — Use and non-use records | DECIDED-2026-09-25 | C-7B.10.2 — Operational-record content contract: existing operational-content atoms; C-7B.10.3 — Use and non-use records: existing use/non-use and omission atoms retain their ownership. | [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| C-7M.11.2 — Computed View domain-log level separation | Gated by | C-7P — Permission & Authority Boundaries (§7P) | DESIGNED | C-7P — Permission & Authority Boundaries (§7P): authority levels follow the operation's actual present effect. | [V10 §7P] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.1] |
| C-7M.11.3 — Computed View operational-record lifecycle | Gated by | C-7B.10.6 — Active and cold Log lifecycle | DESIGNED | C-7B.10.6 — Active and cold Log lifecycle: existing active/cold state meanings; C-7B.10.7 — Cooling-rule changes: fixed cooling-rule change and evidence/approval requirements. | [V10 §0B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| C-7M.11.3 — Computed View operational-record lifecycle | Gated by | C-7B.10.7 — Cooling-rule changes | DESIGNED | C-7B.10.6 — Active and cold Log lifecycle: existing active/cold state meanings; C-7B.10.7 — Cooling-rule changes: fixed cooling-rule change and evidence/approval requirements. | [V10 §0B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| C-7M.11.3.2 — Computed View cooling-rule ownership | Gated by | C-7B.10.7.1 — Fixed declared cooling rules | DESIGNED | C-7B.10.7.1 — Fixed declared cooling rules: fixed declaration; C-7B.10.7.2.3 — Quantitative proposal evidence: quantitative evidence; C-7B.10.7.2.4 — Concrete proposal examples: concrete examples; C-7B.10.7.3 — Cooling-change approval: Ness's approval for a change. | [V10 §0B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| C-7M.11.3.2 — Computed View cooling-rule ownership | Gated by | C-7B.10.7.2.3 — Quantitative proposal evidence | DESIGNED | C-7B.10.7.1 — Fixed declared cooling rules: fixed declaration; C-7B.10.7.2.3 — Quantitative proposal evidence: quantitative evidence; C-7B.10.7.2.4 — Concrete proposal examples: concrete examples; C-7B.10.7.3 — Cooling-change approval: Ness's approval for a change. | [V10 §0B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| C-7M.11.3.2 — Computed View cooling-rule ownership | Gated by | C-7B.10.7.2.4 — Concrete proposal examples | DESIGNED | C-7B.10.7.1 — Fixed declared cooling rules: fixed declaration; C-7B.10.7.2.3 — Quantitative proposal evidence: quantitative evidence; C-7B.10.7.2.4 — Concrete proposal examples: concrete examples; C-7B.10.7.3 — Cooling-change approval: Ness's approval for a change. | [V10 §0B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| C-7M.11.3.2 — Computed View cooling-rule ownership | Gated by | C-7B.10.7.3 — Cooling-change approval | DESIGNED | C-7B.10.7.1 — Fixed declared cooling rules: fixed declaration; C-7B.10.7.2.3 — Quantitative proposal evidence: quantitative evidence; C-7B.10.7.2.4 — Concrete proposal examples: concrete examples; C-7B.10.7.3 — Cooling-change approval: Ness's approval for a change. | [V10 §0B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| C-7M.11.3.3 — Computed View active-to-cold operation | Fed by | C-7B.10.6.1.2.1 — Cooling age condition | DESIGNED | C-7B.10.6.1.2.1 — Cooling age condition: declared age condition; C-7B.10.6.1.2.2 — Cooling use and link condition: no genuine use and no valid new links. | [V10 §0B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| C-7M.11.3.3 — Computed View active-to-cold operation | Fed by | C-7B.10.6.1.2.2 — Cooling use and link condition | DESIGNED | C-7B.10.6.1.2.1 — Cooling age condition: declared age condition; C-7B.10.6.1.2.2 — Cooling use and link condition: no genuine use and no valid new links. | [V10 §0B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| C-7M.11.3.4 — Computed View cold-record reactivation | Fed by | C-7B.10.6.3.1 — Reasoning-use reactivation condition | DESIGNED | C-7B.10.6.3.1 — Reasoning-use reactivation condition: actual-use condition; C-7B.10.6.3.2 — Valid-link reactivation condition: valid-link condition; C-7B.10.6.2.2 — Semantic cold-retrieval fallback: semantic retrieval remains only a fallback until genuine use or a valid link occurs. | [V10 §0B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| C-7M.11.3.4 — Computed View cold-record reactivation | Fed by | C-7B.10.6.3.2 — Valid-link reactivation condition | DESIGNED | C-7B.10.6.3.1 — Reasoning-use reactivation condition: actual-use condition; C-7B.10.6.3.2 — Valid-link reactivation condition: valid-link condition; C-7B.10.6.2.2 — Semantic cold-retrieval fallback: semantic retrieval remains only a fallback until genuine use or a valid link occurs. | [V10 §0B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| C-7M.11.3.4 — Computed View cold-record reactivation | Fed by | C-7B.10.6.2.2 — Semantic cold-retrieval fallback | DESIGNED | C-7B.10.6.3.1 — Reasoning-use reactivation condition: actual-use condition; C-7B.10.6.3.2 — Valid-link reactivation condition: valid-link condition; C-7B.10.6.2.2 — Semantic cold-retrieval fallback: semantic retrieval remains only a fallback until genuine use or a valid link occurs. | [V10 §0B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| C-7M.11.4.9 — Bundle 4 lifecycle authorization_reference | Gated by | C-7B.10.8 — Operational-record access boundary | DESIGNED | C-7B.10.8 — Operational-record access boundary: existing operational-record access rules remain applicable. | [V10 §0B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| C-7M.12 — Computed View provisional-creation influence | Fed by | C-CREATE.8.5 — Provisional influence in Computed View | ACCEPTED | C-CREATE.8.5 — Provisional influence in Computed View: the accepted view-influence interface; C-CREATE.8.1 — provisional_material_used: provisional_material_used; C-CREATE.8.1.1 — Provisional-use record identity: used record identity; C-CREATE.8.1.2 — Creation status at use time: creation status at use time. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| C-7M.12 — Computed View provisional-creation influence | Fed by | C-CREATE.8.1 — provisional_material_used | ACCEPTED | C-CREATE.8.5 — Provisional influence in Computed View: the accepted view-influence interface; C-CREATE.8.1 — provisional_material_used: provisional_material_used; C-CREATE.8.1.1 — Provisional-use record identity: used record identity; C-CREATE.8.1.2 — Creation status at use time: creation status at use time. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| C-7M.12 — Computed View provisional-creation influence | Fed by | C-CREATE.8.1.1 — Provisional-use record identity | ACCEPTED | C-CREATE.8.5 — Provisional influence in Computed View: the accepted view-influence interface; C-CREATE.8.1 — provisional_material_used: provisional_material_used; C-CREATE.8.1.1 — Provisional-use record identity: used record identity; C-CREATE.8.1.2 — Creation status at use time: creation status at use time. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| C-7M.12 — Computed View provisional-creation influence | Fed by | C-CREATE.8.1.2 — Creation status at use time | ACCEPTED | C-CREATE.8.5 — Provisional influence in Computed View: the accepted view-influence interface; C-CREATE.8.1 — provisional_material_used: provisional_material_used; C-CREATE.8.1.1 — Provisional-use record identity: used record identity; C-CREATE.8.1.2 — Creation status at use time: creation status at use time. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] |
| C-7M.13 — Computed View metadata-only held-content boundary | Fed by | C-7E.11 — Held-content access boundary | DESIGNED | C-7E.11 — Held-content access boundary: the existing DESIGNED safe metadata/lifecycle/blocker source interface. | [V10 §7M] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| C-7M.13 — Computed View metadata-only held-content boundary | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): purpose privacy, compartment and influence-removal authorization remains prior to use; C-TSC — Temporary Session Cache (§7E-TSC): sealed or retained archive material supplies no inspection path. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| C-7M.13 — Computed View metadata-only held-content boundary | Gated by | C-TSC — Temporary Session Cache (§7E-TSC) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): purpose privacy, compartment and influence-removal authorization remains prior to use; C-TSC — Temporary Session Cache (§7E-TSC): sealed or retained archive material supplies no inspection path. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

## Cross-piece TOGETHER continuations for incoming uses

These are the reciprocal uses represented in the current USED BY tables. Their external owners retain their full mechanisms in their assigned pieces.

| Current card supplying use | External using card | Takes in there | Does there | Changes there | Stamp | Source |
|---|---|---|---|---|---|---|
| C-7M — Computed View (§7M) | C-7GA.11.7.2 — Step 7B — Process triggered view profiles | The triggered profile-update operation and its result. | Requests and tracks each profile update under its operation key. | A checkpointed internal view-update result. | DESIGNED | [V10 §7G-A] |
| C-7M — Computed View (§7M) | C-CREATE.8.5 — Provisional influence in Computed View | The current-picture influence boundary. | Carries relevant provisional material with its status and operation record. | No provisional fragment becomes settled through use. | ACCEPTED | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4] |
| C-7M — Computed View (§7M) | C-7J — Clash Handling (§7J) | The current-use handling of clash-bearing material. | Keeps clashes and responses separate while informing current presentation. | Presentation only, no source mutation. | DESIGNED | [V10 §7J] [V10 §7M] |
| C-7M — Computed View (§7M) | C-7J.6 — Ness response as separate event | The view's explicit-judgment input. | Allows a response to affect current use without rewriting the clash. | A presentation consequence, not a truth verdict. | DESIGNED | [V10 §7J] [V10 §7M] |
| C-7M — Computed View (§7M) | C-7J.7 — Downstream effects of clashes | Current presentation of conflicted support. | Keeps clashes beside items and permits no clear current view. | No forced winner. | ACCEPTED | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §8] |
| C-7M — Computed View (§7M) | C-7K — Story Layer (§7K) | The preserved source-telling interface. | Supplies tellings to the current picture without merging perspectives. | Current navigation, not new story authority. | DESIGNED | [V10 §7K] [V10 §7M] |
| C-7M — Computed View (§7M) | C-7L — Person-Boxes (§7L) | The person-focused current-picture interface. | Uses linked source objects under the view's derivation rules. | An inspectable current picture without changing the Person-Box. | DESIGNED | [V10 §7L] [V10 §7M] |
| C-7M — Computed View (§7M) | C-7L.4 — Ness's confirmed Person-Box | The person-focused assembly rules. | Supplies Ness's anchor without creating a self-profile. | Permitted source links in the current picture. | ACCEPTED | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] |
| C-7M — Computed View (§7M) | C-7L.5 — Seven-section Person-Box view | The seven-factor best-supported ordering. | Delegates a best-supported claim to that ordering. | No recency-only reliability claim. | ACCEPTED | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §13] |
| C-7M — Computed View (§7M) | C-7N — Action Surfacing (§7N) | The current internal picture. | Uses it under its own evidence and authority rules. | Possible-action support, not action permission. | DESIGNED | [MAP C-7M] |
| C-7M — Computed View (§7M) | C-7I — View Layer (§7I) | Explicit best-supported ordering. | Uses it when making a best-supported presentation claim. | Disclosed current-use presentation. | DESIGNED | [MAP C-7I] [V10 §7M] |

## Scope, paths and source dispositions

C-7M participates in CY-A through the already delivered C-7GA.11.7.2 update step. Existing C-7J/C-7K/C-7L inputs, person-focused best-supported delegation, C-READ complete-telling and reference gates, C-7A history constraints, C-CREATE.8.5 provisional influence and C-7E.11 safe held metadata are reciprocated here. All earlier TOGETHER and USED BY relationships pointing to current cards were checked against the current opposite end. Their prior bytes remain unchanged. Full side-path assembly remains CH11.

This piece places V10 §7M, accepted Bundle 4 §8 and the applicable §11–14 operation/logging boundaries, and Bundle 2 §7 with its shared declaration/producer/uncertainty/access rules. Bundle 4's state/world node and evidence-family schemas remain CH06-f; its action stages, authority and presentation remain CH07-a/b/c. Shared Bundle 4 operational-record lifecycle fields are written here once for later consumers to reference. Snapshot/profile/refresh/lifecycle records reuse the same operation_id, created_at and operational-log-reference owners wherever their meanings coincide. Profile ID/version and derivation version likewise retain one owner. Generic Log state, cooling-condition/change and restored operation-content atoms retain C-7B.10 ownership. B9 retry mechanics/values retain C-7H.9/C-7H.10; no values are selected here.

The proposed view declaration retains its proposed qualifier and version. Existing canonical names for shared relevance outcomes are preserved even where the earlier file omitted that qualifier; accompanying current text expressly scopes them to the proposed shared rule. Full Attention and Relevance Control validation, vocabulary and Decision-11/12/14 schemas remain CH08-b. The current consumer's actual consequences and nine dimension applicability rules are written here. The accepted-but-excluded B26 foundation source-scope gap remains open; acceptance is not denied.

Provisional creation has an accepted marked/traced influence route, but its precise representation among the snapshot's fixed source-family fields is not selected by these sources. That representation seam is registered below; no eleventh family or conversion is invented. The held-content obligation is fulfilled through the DESIGNED C-7E.11 source interface and the current accepted consumer restrictions: safe metadata/state/blockers only, never held raw content or a TSC inspection path. Full privacy/LMAC/access owners remain CH08-a/c and CH09-d.

Discovery searched every permitted 04/05 file by C-7M, Computed View, view_profile and snapshot_id. Authority snapshot matches in AIC/B-INT-5/B-INT-7 concern authority/session state rather than a view snapshot; their mechanisms are not imported. Active indices are navigation, the recovery ledger contributes only Appendix B tracking, and accepted receipts establish package identity without claiming their conditional receipt audits were independently observed as PASS. DD/Companion comparison does not override V10; an earlier open B5 slot is completed by its accepted standalone package rather than treated as a new source conflict.

## Source-to-card coverage added by CH06-d

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

## Additional undecided implementation slots

| Owner | Slot | State |
|---|---|---|
| C-7M.3 — Computed View ordering-profile record | Concrete serialization, storage technology and field types beyond the conceptual versioned ordering-profile schema | NOT DECIDED |
| C-7M.3.9 — Computed View disclosed factor-specific rules | Exact empirical significance thresholds, weights, tie calibration or other numeric ordering values beyond fixed disclosed factors | NOT DECIDED |
| C-7M.3.14 — Computed View declared invalidating events | Concrete profile invalidation trigger values beyond the requirement to declare them and preserve versions | NOT DECIDED |
| C-7M.5 — Computed View immutable snapshot record | Concrete snapshot serialization/transaction implementation beyond the accepted immutable all-or-nothing record contract | NOT DECIDED |
| C-7M.6.4 — Computed View standing_snapshot_id | Exact null/absence representation of standing_snapshot_id when no valid snapshot has ever existed | NOT DECIDED |
| C-7M.6 — Computed View refresh-status event | Concrete event wire/storage implementation and ordering of applicable event retrieval beyond the accepted schema and derivation rule | NOT DECIDED |
| C-7M.8 — Computed View duplicate prevention | Concrete idempotency-key encoding and persistence technology | NOT DECIDED |
| C-7M.9 — Computed View operation and recovery contract | Implementation-facing integration of accepted B9 retry machinery and values; no new retry value is selected | NOT DECIDED |
| C-7M.10.1 — Computed View proposed declaration identity and version | Final naming and serialization of proposed declaration identifiers/fields at the source-reserved implementation-facing step | NOT DECIDED |
| C-7M.10.4.2 — Computed View within_declared_time_range gate | Exact profile-declared time-range value where a profile selects the time gate | NOT DECIDED |
| C-7M.11.3.2 — Computed View cooling-rule ownership | Exact empirical time/calibration values of each component-owned cooling rule | NOT DECIDED |
| C-7M.11.4 — Bundle 4 operational-record lifecycle-status event | Concrete serialization and storage-failure implementation for the conceptual append-only lifecycle/status schema | NOT DECIDED |
| C-7M.12 — Computed View provisional-creation influence | Exact carriage of permitted provisional-creation influence within the snapshot's fixed ten source-reference families; no eleventh family or conversion is chosen | NOT DECIDED |

## Appendix A carry-forward — this piece

| Card | Empty field | Occurrence within field | State |
|---|---|---|---|
| C-7M.1 — Computed View internal-use boundary | Fed by | 1 | NOT DECIDED |
| C-7M.1 — Computed View internal-use boundary | Changes | 1 | NOT DECIDED |
| C-7M.2 — Computed View seven-factor priority order | Gated by | 1 | NOT DECIDED |
| C-7M.2 — Computed View seven-factor priority order | Changes | 1 | NOT DECIDED |
| C-7M.2.1 — Computed View factor 1 — current Ness judgment | Fails closed by | 1 | NOT DECIDED |
| C-7M.2.1 — Computed View factor 1 — current Ness judgment | Gated by | 1 | NOT DECIDED |
| C-7M.2.2 — Computed View factor 2 — direct root evidence | Fails closed by | 1 | NOT DECIDED |
| C-7M.2.2 — Computed View factor 2 — direct root evidence | Gated by | 1 | NOT DECIDED |
| C-7M.2.3 — Computed View factor 3 — reading acceptance and grounding | Fails closed by | 1 | NOT DECIDED |
| C-7M.2.3 — Computed View factor 3 — reading acceptance and grounding | Gated by | 1 | NOT DECIDED |
| C-7M.2.4 — Computed View factor 4 — purpose relevance | Fails closed by | 1 | NOT DECIDED |
| C-7M.2.5 — Computed View factor 5 — context quality and provenance | Fails closed by | 1 | NOT DECIDED |
| C-7M.2.5 — Computed View factor 5 — context quality and provenance | Gated by | 1 | NOT DECIDED |
| C-7M.2.6 — Computed View factor 6 — clashes and uncertainty | Gated by | 1 | NOT DECIDED |
| C-7M.2.7 — Computed View factor 7 — recency tie-breaker | Fails closed by | 1 | NOT DECIDED |
| C-7M.2.7 — Computed View factor 7 — recency tie-breaker | Fed by | 1 | NOT DECIDED |
| C-7M.2.7 — Computed View factor 7 — recency tie-breaker | Gated by | 1 | NOT DECIDED |
| C-7M.3 — Computed View ordering-profile record | Changes | 1 | NOT DECIDED |
| C-7M.3.1 — Computed View view_profile_id | Fails closed by | 1 | NOT DECIDED |
| C-7M.3.1 — Computed View view_profile_id | Fed by | 1 | NOT DECIDED |
| C-7M.3.1 — Computed View view_profile_id | Gated by | 1 | NOT DECIDED |
| C-7M.3.2 — Computed View profile_version | Fed by | 1 | NOT DECIDED |
| C-7M.3.2 — Computed View profile_version | Gated by | 1 | NOT DECIDED |
| C-7M.3.3 — Computed View profile_purpose_type | Fed by | 1 | NOT DECIDED |
| C-7M.3.4 — Computed View optional purpose label | Fails closed by | 1 | NOT DECIDED |
| C-7M.3.4 — Computed View optional purpose label | Fed by | 1 | NOT DECIDED |
| C-7M.3.4 — Computed View optional purpose label | Gated by | 1 | NOT DECIDED |
| C-7M.3.5 — Computed View consuming_component | Fails closed by | 1 | NOT DECIDED |
| C-7M.3.5 — Computed View consuming_component | Fed by | 1 | NOT DECIDED |
| C-7M.3.5 — Computed View consuming_component | Gated by | 1 | NOT DECIDED |
| C-7M.3.6 — Computed View authorization and privacy basis | Fed by | 1 | NOT DECIDED |
| C-7M.3.7 — Computed View eligible source-reference families | Gated by | 1 | NOT DECIDED |
| C-7M.3.8 — Computed View fixed-factor profile field | Fails closed by | 1 | NOT DECIDED |
| C-7M.3.8 — Computed View fixed-factor profile field | Gated by | 1 | NOT DECIDED |
| C-7M.3.9 — Computed View disclosed factor-specific rules | Fails closed by | 1 | NOT DECIDED |
| C-7M.3.9 — Computed View disclosed factor-specific rules | Gated by | 1 | NOT DECIDED |
| C-7M.3.9.1 — Computed View profile ordering rules | Fails closed by | 1 | NOT DECIDED |
| C-7M.3.9.1 — Computed View profile ordering rules | Fed by | 1 | NOT DECIDED |
| C-7M.3.9.1 — Computed View profile ordering rules | Gated by | 1 | NOT DECIDED |
| C-7M.3.9.2 — Computed View profile tie rules | Fails closed by | 1 | NOT DECIDED |
| C-7M.3.9.2 — Computed View profile tie rules | Fed by | 1 | NOT DECIDED |
| C-7M.3.9.2 — Computed View profile tie rules | Gated by | 1 | NOT DECIDED |
| C-7M.3.9.3 — Computed View profile omission rules | Fails closed by | 1 | NOT DECIDED |
| C-7M.3.9.3 — Computed View profile omission rules | Fed by | 1 | NOT DECIDED |
| C-7M.3.9.3 — Computed View profile omission rules | Gated by | 1 | NOT DECIDED |
| C-7M.3.9.4 — Computed View profile surfacing rules | Fails closed by | 1 | NOT DECIDED |
| C-7M.3.9.4 — Computed View profile surfacing rules | Fed by | 1 | NOT DECIDED |
| C-7M.3.10 — Computed View no-hidden-score declaration | Fails closed by | 1 | NOT DECIDED |
| C-7M.3.10 — Computed View no-hidden-score declaration | Fed by | 1 | NOT DECIDED |
| C-7M.3.10 — Computed View no-hidden-score declaration | Gated by | 1 | NOT DECIDED |
| C-7M.3.12 — Computed View Tier-2 configuration reference | Gated by | 1 | NOT DECIDED |
| C-7M.3.13 — Computed View declared refresh triggers | Fails closed by | 1 | NOT DECIDED |
| C-7M.3.13 — Computed View declared refresh triggers | Gated by | 1 | NOT DECIDED |
| C-7M.3.14 — Computed View declared invalidating events | Fails closed by | 1 | NOT DECIDED |
| C-7M.3.14 — Computed View declared invalidating events | Fed by | 1 | NOT DECIDED |
| C-7M.3.14 — Computed View declared invalidating events | Gated by | 1 | NOT DECIDED |
| C-7M.3.15 — Computed View unresolved-handling reference | Gated by | 1 | NOT DECIDED |
| C-7M.3.16 — Computed View derivation_rule_version | Fails closed by | 1 | NOT DECIDED |
| C-7M.3.16 — Computed View derivation_rule_version | Fed by | 1 | NOT DECIDED |
| C-7M.3.16 — Computed View derivation_rule_version | Gated by | 1 | NOT DECIDED |
| C-7M.3.17 — Computed View record created_at | Fails closed by | 1 | NOT DECIDED |
| C-7M.3.17 — Computed View record created_at | Fed by | 1 | NOT DECIDED |
| C-7M.3.17 — Computed View record created_at | Gated by | 1 | NOT DECIDED |
| C-7M.3.18 — Computed View prior profile-version reference | Fails closed by | 1 | NOT DECIDED |
| C-7M.3.18 — Computed View prior profile-version reference | Fed by | 1 | NOT DECIDED |
| C-7M.3.18 — Computed View prior profile-version reference | Gated by | 1 | NOT DECIDED |
| C-7M.3.19 — Computed View operational-log references | Fails closed by | 1 | NOT DECIDED |
| C-7M.3.19 — Computed View operational-log references | Gated by | 1 | NOT DECIDED |
| C-7M.4 — Computed View update triggers | Fails closed by | 1 | NOT DECIDED |
| C-7M.4 — Computed View update triggers | Gated by | 1 | NOT DECIDED |
| C-7M.4 — Computed View update triggers | Changes | 1 | NOT DECIDED |
| C-7M.4.1 — Computed View opened trigger | Fails closed by | 1 | NOT DECIDED |
| C-7M.4.1 — Computed View opened trigger | Fed by | 1 | NOT DECIDED |
| C-7M.4.2 — Computed View manual-refresh trigger | Fails closed by | 1 | NOT DECIDED |
| C-7M.4.2 — Computed View manual-refresh trigger | Fed by | 1 | NOT DECIDED |
| C-7M.4.3 — Computed View materially-relevant-event trigger | Fails closed by | 1 | NOT DECIDED |
| C-7M.4.3.1 — Computed View accepted-reading event trigger | Fails closed by | 1 | NOT DECIDED |
| C-7M.4.3.1 — Computed View accepted-reading event trigger | Changes | 1 | NOT DECIDED |
| C-7M.4.3.2 — Computed View active-clash event trigger | Fails closed by | 1 | NOT DECIDED |
| C-7M.4.3.2 — Computed View active-clash event trigger | Changes | 1 | NOT DECIDED |
| C-7M.4.3.3 — Computed View Ness-response event trigger | Fails closed by | 1 | NOT DECIDED |
| C-7M.4.3.3 — Computed View Ness-response event trigger | Changes | 1 | NOT DECIDED |
| C-7M.4.3.4 — Computed View theme-confirmation trigger | Fails closed by | 1 | NOT DECIDED |
| C-7M.4.3.4 — Computed View theme-confirmation trigger | Changes | 1 | NOT DECIDED |
| C-7M.4.3.5 — Computed View identity-resolution trigger | Fails closed by | 1 | NOT DECIDED |
| C-7M.4.3.5 — Computed View identity-resolution trigger | Changes | 1 | NOT DECIDED |
| C-7M.4.3.6 — Computed View other declared-event trigger | Fails closed by | 1 | NOT DECIDED |
| C-7M.4.3.6 — Computed View other declared-event trigger | Fed by | 1 | NOT DECIDED |
| C-7M.4.3.6 — Computed View other declared-event trigger | Changes | 1 | NOT DECIDED |
| C-7M.5 — Computed View immutable snapshot record | Changes | 1 | NOT DECIDED |
| C-7M.5.1 — Computed View snapshot_id | Fails closed by | 1 | NOT DECIDED |
| C-7M.5.1 — Computed View snapshot_id | Fed by | 1 | NOT DECIDED |
| C-7M.5.2 — Computed View operation_id | Fails closed by | 1 | NOT DECIDED |
| C-7M.5.2 — Computed View operation_id | Fed by | 1 | NOT DECIDED |
| C-7M.5.3 — Computed View snapshot trigger reference | Fails closed by | 1 | NOT DECIDED |
| C-7M.5.3 — Computed View snapshot trigger reference | Gated by | 1 | NOT DECIDED |
| C-7M.5.3.1 — Computed View snapshot trigger type | Fails closed by | 1 | NOT DECIDED |
| C-7M.5.3.1 — Computed View snapshot trigger type | Fed by | 1 | NOT DECIDED |
| C-7M.5.3.1 — Computed View snapshot trigger type | Gated by | 1 | NOT DECIDED |
| C-7M.5.3.2 — Computed View snapshot trigger object | Fails closed by | 1 | NOT DECIDED |
| C-7M.5.3.2 — Computed View snapshot trigger object | Fed by | 1 | NOT DECIDED |
| C-7M.5.3.2 — Computed View snapshot trigger object | Gated by | 1 | NOT DECIDED |
| C-7M.5.4 — Computed View snapshot authorization-purpose basis | Fed by | 1 | NOT DECIDED |
| C-7M.5.5.1 — Computed View direct-root references | Fails closed by | 1 | NOT DECIDED |
| C-7M.5.5.1 — Computed View direct-root references | Gated by | 1 | NOT DECIDED |
| C-7M.5.5.2 — Computed View reading references | Fails closed by | 1 | NOT DECIDED |
| C-7M.5.5.2 — Computed View reading references | Gated by | 1 | NOT DECIDED |
| C-7M.5.5.4 — Computed View clash references | Gated by | 1 | NOT DECIDED |
| C-7M.5.5.5 — Computed View Ness-response references | Fails closed by | 1 | NOT DECIDED |
| C-7M.5.5.5 — Computed View Ness-response references | Gated by | 1 | NOT DECIDED |
| C-7M.5.5.6 — Computed View Person-Box-link references | Fails closed by | 1 | NOT DECIDED |
| C-7M.5.5.6 — Computed View Person-Box-link references | Gated by | 1 | NOT DECIDED |
| C-7M.5.5.7 — Computed View theme references | Fails closed by | 1 | NOT DECIDED |
| C-7M.5.5.7 — Computed View theme references | Gated by | 1 | NOT DECIDED |
| C-7M.5.5.8 — Computed View Living-State references | Fails closed by | 1 | NOT DECIDED |
| C-7M.5.5.8 — Computed View Living-State references | Gated by | 1 | NOT DECIDED |
| C-7M.5.5.9 — Computed View world-model references | Fails closed by | 1 | NOT DECIDED |
| C-7M.5.5.9 — Computed View world-model references | Gated by | 1 | NOT DECIDED |
| C-7M.5.6 — Computed View separate ordering-factor results | Fails closed by | 1 | NOT DECIDED |
| C-7M.5.6 — Computed View separate ordering-factor results | Gated by | 1 | NOT DECIDED |
| C-7M.5.7 — Computed View snapshot clashes and uncertainty | Gated by | 1 | NOT DECIDED |
| C-7M.5.8 — Computed View omitted candidates and reasons | Fails closed by | 1 | NOT DECIDED |
| C-7M.5.8 — Computed View omitted candidates and reasons | Gated by | 1 | NOT DECIDED |
| C-7M.5.9 — Computed View prior snapshot reference | Fails closed by | 1 | NOT DECIDED |
| C-7M.5.9 — Computed View prior snapshot reference | Fed by | 1 | NOT DECIDED |
| C-7M.5.9 — Computed View prior snapshot reference | Gated by | 1 | NOT DECIDED |
| C-7M.5.10 — Computed View changed-from-prior explanation | Fails closed by | 1 | NOT DECIDED |
| C-7M.5.10 — Computed View changed-from-prior explanation | Gated by | 1 | NOT DECIDED |
| C-7M.5.11 — Computed View committed completeness status | Fed by | 1 | NOT DECIDED |
| C-7M.5.11 — Computed View committed completeness status | Gated by | 1 | NOT DECIDED |
| C-7M.5.12 — Computed View privacy-output eligibility references | Fed by | 1 | NOT DECIDED |
| C-7M.6.1 — Computed View event_id | Fails closed by | 1 | NOT DECIDED |
| C-7M.6.1 — Computed View event_id | Fed by | 1 | NOT DECIDED |
| C-7M.6.1 — Computed View event_id | Gated by | 1 | NOT DECIDED |
| C-7M.6.2 — Computed View attempted_profile_id_and_version | Fails closed by | 1 | NOT DECIDED |
| C-7M.6.2 — Computed View attempted_profile_id_and_version | Gated by | 1 | NOT DECIDED |
| C-7M.6.3 — Computed View attempted_trigger | Fails closed by | 1 | NOT DECIDED |
| C-7M.6.3 — Computed View attempted_trigger | Gated by | 1 | NOT DECIDED |
| C-7M.6.4 — Computed View standing_snapshot_id | Gated by | 1 | NOT DECIDED |
| C-7M.6.5 — Computed View refresh outcome value | Gated by | 1 | NOT DECIDED |
| C-7M.6.6 — Computed View failure_or_incompleteness_reason | Fed by | 1 | NOT DECIDED |
| C-7M.6.6 — Computed View failure_or_incompleteness_reason | Gated by | 1 | NOT DECIDED |
| C-7M.6.7 — Computed View retry_eligibility | Gated by | 1 | NOT DECIDED |
| C-7M.6.8 — Computed View retry_attempt_reference | Fails closed by | 1 | NOT DECIDED |
| C-7M.6.8 — Computed View retry_attempt_reference | Fed by | 1 | NOT DECIDED |
| C-7M.6.8 — Computed View retry_attempt_reference | Gated by | 1 | NOT DECIDED |
| C-7M.7.2 — Computed View null update | Fails closed by | 1 | NOT DECIDED |
| C-7M.7.2 — Computed View null update | Fed by | 1 | NOT DECIDED |
| C-7M.7.2 — Computed View null update | Gated by | 1 | NOT DECIDED |
| C-7M.7.3 — Computed View failed refresh | Fed by | 1 | NOT DECIDED |
| C-7M.7.3 — Computed View failed refresh | Gated by | 1 | NOT DECIDED |
| C-7M.7.4 — Computed View incomplete refresh | Fed by | 1 | NOT DECIDED |
| C-7M.7.4 — Computed View incomplete refresh | Gated by | 1 | NOT DECIDED |
| C-7M.7.5 — Computed View possible staleness | Fed by | 1 | NOT DECIDED |
| C-7M.7.5 — Computed View possible staleness | Gated by | 1 | NOT DECIDED |
| C-7M.9.1 — Computed View crash before snapshot commit | Fed by | 1 | NOT DECIDED |
| C-7M.9.1 — Computed View crash before snapshot commit | Gated by | 1 | NOT DECIDED |
| C-7M.9.2 — Computed View committed-outcome reconciliation | Fed by | 1 | NOT DECIDED |
| C-7M.9.2 — Computed View committed-outcome reconciliation | Gated by | 1 | NOT DECIDED |
| C-7M.9.3 — Computed View failure with an older valid snapshot | Fed by | 1 | NOT DECIDED |
| C-7M.9.3 — Computed View failure with an older valid snapshot | Gated by | 1 | NOT DECIDED |
| C-7M.9.4 — Computed View partial-refresh recovery | Fed by | 1 | NOT DECIDED |
| C-7M.9.4 — Computed View partial-refresh recovery | Gated by | 1 | NOT DECIDED |
| C-7M.9.6 — Computed View unestablished freshness | Fed by | 1 | NOT DECIDED |
| C-7M.9.6 — Computed View unestablished freshness | Gated by | 1 | NOT DECIDED |
| C-7M.10.1 — Computed View proposed declaration identity and version | Fed by | 1 | NOT DECIDED |
| C-7M.10.2 — Computed View view_assembly purpose | Fed by | 1 | NOT DECIDED |
| C-7M.10.3 — Computed View relevance target | Gated by | 1 | NOT DECIDED |
| C-7M.10.4 — Computed View deterministic context gates | Gated by | 1 | NOT DECIDED |
| C-7M.10.4.1 — Computed View object_type_matches gate | Gated by | 1 | NOT DECIDED |
| C-7M.10.4.2 — Computed View within_declared_time_range gate | Fails closed by | 1 | NOT DECIDED |
| C-7M.10.4.2 — Computed View within_declared_time_range gate | Fed by | 1 | NOT DECIDED |
| C-7M.10.4.2 — Computed View within_declared_time_range gate | Gated by | 1 | NOT DECIDED |
| C-7M.10.5.1 — Computed View semantic_similarity selection | Fed by | 1 | NOT DECIDED |
| C-7M.10.5.1 — Computed View semantic_similarity selection | Gated by | 1 | NOT DECIDED |
| C-7M.10.5.2 — Computed View temporal_distance selection | Fed by | 1 | NOT DECIDED |
| C-7M.10.5.2 — Computed View temporal_distance selection | Gated by | 1 | NOT DECIDED |
| C-7M.10.5.3 — Computed View positional_distance selection | Fed by | 1 | NOT DECIDED |
| C-7M.10.5.3 — Computed View positional_distance selection | Gated by | 1 | NOT DECIDED |
| C-7M.10.5.4 — Computed View currentness_status selection | Gated by | 1 | NOT DECIDED |
| C-7M.10.5.5 — Computed View explicit_links selection | Fed by | 1 | NOT DECIDED |
| C-7M.10.5.5 — Computed View explicit_links selection | Gated by | 1 | NOT DECIDED |
| C-7M.10.5.6 — Computed View ness_response_links selection | Fed by | 1 | NOT DECIDED |
| C-7M.10.5.6 — Computed View ness_response_links selection | Gated by | 1 | NOT DECIDED |
| C-7M.10.5.7 — Computed View proposal_acceptance_outcome selection | Fed by | 1 | NOT DECIDED |
| C-7M.10.5.7 — Computed View proposal_acceptance_outcome selection | Gated by | 1 | NOT DECIDED |
| C-7M.10.5.8 — Computed View reading_context_status selection | Fed by | 1 | NOT DECIDED |
| C-7M.10.5.8 — Computed View reading_context_status selection | Gated by | 1 | NOT DECIDED |
| C-7M.10.5.9 — Computed View active_clash_links selection | Fed by | 1 | NOT DECIDED |
| C-7M.10.5.9 — Computed View active_clash_links selection | Gated by | 1 | NOT DECIDED |
| C-7M.10.6 — Computed View mouth-authorization boundary | Fed by | 1 | NOT DECIDED |
| C-7M.10.7 — Computed View relevance evaluation timing | Fails closed by | 1 | NOT DECIDED |
| C-7M.10.7 — Computed View relevance evaluation timing | Gated by | 1 | NOT DECIDED |
| C-7M.10.8 — Computed View relevance-mode reason | Fails closed by | 1 | NOT DECIDED |
| C-7M.10.8 — Computed View relevance-mode reason | Fed by | 1 | NOT DECIDED |
| C-7M.10.8 — Computed View relevance-mode reason | Gated by | 1 | NOT DECIDED |
| C-7M.10.9 — Computed View Tier-2 relevance rules | Gated by | 1 | NOT DECIDED |
| C-7M.10.9.1 — Computed View relevance ordering consequences | Gated by | 1 | NOT DECIDED |
| C-7M.10.9.2 — Computed View relevance fallback | Gated by | 1 | NOT DECIDED |
| C-7M.10.9.3 — Computed View relevance surfacing boundary | Fed by | 1 | NOT DECIDED |
| C-7M.10.10 — Computed View relevance allowed-use boundary | Fed by | 1 | NOT DECIDED |
| C-7M.10.12 — Computed View invalid relevance declaration outcome | Fed by | 1 | NOT DECIDED |
| C-7M.11.1 — Computed View operation-record content | Gated by | 1 | NOT DECIDED |
| C-7M.11.2 — Computed View domain-log level separation | Fails closed by | 1 | NOT DECIDED |
| C-7M.11.3.1 — Computed View active-log protection conditions | Gated by | 1 | NOT DECIDED |
| C-7M.11.3.1.1 — Computed View unresolved-operation log protection | Fails closed by | 1 | NOT DECIDED |
| C-7M.11.3.1.1 — Computed View unresolved-operation log protection | Fed by | 1 | NOT DECIDED |
| C-7M.11.3.1.1 — Computed View unresolved-operation log protection | Gated by | 1 | NOT DECIDED |
| C-7M.11.3.1.2 — Computed View current-chain log protection | Fails closed by | 1 | NOT DECIDED |
| C-7M.11.3.1.2 — Computed View current-chain log protection | Fed by | 1 | NOT DECIDED |
| C-7M.11.3.1.2 — Computed View current-chain log protection | Gated by | 1 | NOT DECIDED |
| C-7M.11.3.1.3 — Computed View recovery-and-correction log protection | Fails closed by | 1 | NOT DECIDED |
| C-7M.11.3.1.3 — Computed View recovery-and-correction log protection | Fed by | 1 | NOT DECIDED |
| C-7M.11.3.1.3 — Computed View recovery-and-correction log protection | Gated by | 1 | NOT DECIDED |
| C-7M.11.3.1.4 — Computed View actual-use log protection | Fails closed by | 1 | NOT DECIDED |
| C-7M.11.3.1.4 — Computed View actual-use log protection | Fed by | 1 | NOT DECIDED |
| C-7M.11.3.1.4 — Computed View actual-use log protection | Gated by | 1 | NOT DECIDED |
| C-7M.11.3.1.5 — Computed View valid-new-link log protection | Fails closed by | 1 | NOT DECIDED |
| C-7M.11.3.1.5 — Computed View valid-new-link log protection | Fed by | 1 | NOT DECIDED |
| C-7M.11.3.1.5 — Computed View valid-new-link log protection | Gated by | 1 | NOT DECIDED |
| C-7M.11.3.2 — Computed View cooling-rule ownership | Fed by | 1 | NOT DECIDED |
| C-7M.11.3.4 — Computed View cold-record reactivation | Gated by | 1 | NOT DECIDED |
| C-7M.11.3.5 — Computed View uncertain status evaluation | Fed by | 1 | NOT DECIDED |
| C-7M.11.4.1 — Bundle 4 lifecycle_event_id | Fails closed by | 1 | NOT DECIDED |
| C-7M.11.4.1 — Bundle 4 lifecycle_event_id | Fed by | 1 | NOT DECIDED |
| C-7M.11.4.1 — Bundle 4 lifecycle_event_id | Gated by | 1 | NOT DECIDED |
| C-7M.11.4.2 — Bundle 4 operational_record_id | Fails closed by | 1 | NOT DECIDED |
| C-7M.11.4.2 — Bundle 4 operational_record_id | Fed by | 1 | NOT DECIDED |
| C-7M.11.4.2 — Bundle 4 operational_record_id | Gated by | 1 | NOT DECIDED |
| C-7M.11.4.3 — Bundle 4 lifecycle component_owner | Fails closed by | 1 | NOT DECIDED |
| C-7M.11.4.3 — Bundle 4 lifecycle component_owner | Fed by | 1 | NOT DECIDED |
| C-7M.11.4.3 — Bundle 4 lifecycle component_owner | Gated by | 1 | NOT DECIDED |
| C-7M.11.4.4 — Bundle 4 cooling_rule_id_and_version | Fails closed by | 1 | NOT DECIDED |
| C-7M.11.4.4 — Bundle 4 cooling_rule_id_and_version | Gated by | 1 | NOT DECIDED |
| C-7M.11.4.5 — Bundle 4 lifecycle previous_status | Fed by | 1 | NOT DECIDED |
| C-7M.11.4.5 — Bundle 4 lifecycle previous_status | Gated by | 1 | NOT DECIDED |
| C-7M.11.4.6 — Bundle 4 lifecycle new_status | Fed by | 1 | NOT DECIDED |
| C-7M.11.4.6 — Bundle 4 lifecycle new_status | Gated by | 1 | NOT DECIDED |
| C-7M.11.4.7 — Bundle 4 lifecycle reason | Fails closed by | 1 | NOT DECIDED |
| C-7M.11.4.7 — Bundle 4 lifecycle reason | Fed by | 1 | NOT DECIDED |
| C-7M.11.4.7 — Bundle 4 lifecycle reason | Gated by | 1 | NOT DECIDED |
| C-7M.11.4.8 — Bundle 4 triggering_use_or_link_reference | Fails closed by | 1 | NOT DECIDED |
| C-7M.11.4.8 — Bundle 4 triggering_use_or_link_reference | Fed by | 1 | NOT DECIDED |
| C-7M.11.4.8 — Bundle 4 triggering_use_or_link_reference | Gated by | 1 | NOT DECIDED |
| C-7M.11.4.9 — Bundle 4 lifecycle authorization_reference | Fed by | 1 | NOT DECIDED |
| C-7M.11.4.10 — Bundle 4 lifecycle evaluation_outcome | Fed by | 1 | NOT DECIDED |
| C-7M.11.4.10 — Bundle 4 lifecycle evaluation_outcome | Gated by | 1 | NOT DECIDED |
| C-7M.11.4.11 — Bundle 4 lifecycle failure_reason_if_any | Fed by | 1 | NOT DECIDED |
| C-7M.11.4.11 — Bundle 4 lifecycle failure_reason_if_any | Gated by | 1 | NOT DECIDED |
| C-7M.11.5 — Bundle 4 domain-log-lifecycle separation | Fails closed by | 1 | NOT DECIDED |
| C-7M.11.5 — Bundle 4 domain-log-lifecycle separation | Gated by | 1 | NOT DECIDED |

## Plain-gate and empty-box review

Every current ALONE field, TOGETHER field and USED BY row was reviewed with its neighboring boxes. Required immutable record fields carry direct prohibitions where the source establishes them; unspecified per-field storage failures remain empty instead of receiving invented enforcement. Accepted extensions to V10 factor behavior have ACCEPTED lines and their actual sources. The root and other V10 relationship targets retain DESIGNED; only already-built root/reading inputs use BUILT. Every internal endpoint, including each target in a grouped common-rule use row, was checked in both directions. Shared record atoms are reused with explicit field placement. A committed snapshot never receives standing/stale mutations; unsuccessful and null attempts are event-only; a committed-but-unrecorded outcome receives only its missing record. Cooling requires both conditions and cannot follow uncertain evaluation. Proposed declaration names retain the qualifier; preserved earlier canonical names are accompanied by the proposed-rule scope. Earlier aggregate target-stamp and proposed-name omissions are manifest findings, not silent edits. No numeric value, new storage mechanism, source-family conversion or interpretation authority is selected.

| Card | Plain gate justification |
|---|---|
| C-7M.1 — Computed View internal-use boundary | Ness's deliberate request is the human act permitting inspection; quiet authorized internal use requires no such approval. |
| C-7M.4.2 — Computed View manual-refresh trigger | Ness's actual refresh request is the human trigger for this route. |

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

## READ RECORD

Behavior remains pinned to 6a7160ba688ba4e433a31899162815df7e2bab17. Contract §§5–11 and lessons were reopened before drafting; contract §11.3, lessons and run §11 were reopened after writing. Whole credit is limited to the two receipts actually read through their ends for this piece. Other entries state scoped review or preserved earlier credit; no shared-package-wide completion is claimed. Source discovery preceded the card map and its permitted 04/05 matches were reviewed for current or later ownership.

| Source file | Reading scope / whole-file credit | SHA-256 |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: complete §7M; §0B/7A/7G-A/7Q/7R and built source status reused for current interfaces. | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped: complete C-7M and adjoining Group D/CY-A relationships; full later paths remain CH11. | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Scoped: §3G Computed View status and governing priority compared; no override of V10. | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Scoped: complete §7M compared with V10. | `cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` | Scoped: §§1–2, 8, 11–15 in full; §7.2 evidence-family paragraphs and §9.1/10 applicable level/presentation wording; full state/action scopes deferred. | `0c9a201130d5811c838fea0d5655c8a98aac909afdc60024830204a690e77f97` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Whole: acceptance, exact accepted source identity, full conditions and receipt-audit boundary through end. | `ef561aa5037068e1a225157e0382f7155cb91c1948df4347e5236f3a535fbd01` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Scoped: §§4–5.7 and §7 in full; declaration, shared producers/uncertainty/access/logging/failure and view consumer scope. | `b2a5b3fbea75f7123a16c8a45c0fb096f4c4565585a4a0c7b7709e70f27d000e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: full acceptance/source identity, scope, receipt conditions and preserved foundation boundaries through end; no independent receipt-audit PASS claimed. | `faa88d9c991b2e4058081717a4fcbeb5a8e27d62e0f484ae6051fc061a03bac1` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md` | Scoped: complete §3 and applicable §§6/7 authorization/failure boundaries; shared declaration validity retained. | `c754b27e44cdb578e1cc25e7de681c9d2afd68fedc6e974cc45c8aa6c83d553f` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md` | Scoped reopen: §8 conflict effects in full; §§13/16/18–20 current-use and logging boundaries reused from prior whole reading. | `3566cf0f917fb4f7eb329d9089f6e238fe4afbacbae2c73c8b2716e3397e7c2e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Prior whole-file credit retained; accepted identity reused. | `405717e5528df74b9842dee6da8b3de69b82a738e478d06c2e1025243ae56a16` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md` | Scoped: §§5A/6 complete-telling semantic eligibility and first-class Computed View references; existing C-READ atoms retained. | `f91da6426817031cf2c0b14fb467a3e1d97d2ea3c67d27a07d8b1831f9895a55` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Scoped: §4 A13.2 provisional creation wider influence and confirmation boundaries. | `b37f965a343dbf86130f96591d58de9288ad0a746a68e8ae8fdd7b66208a63da` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped: §6 provisional influence, operation-log entry, confirmation/status and no-silent-influence boundaries. | `bc1095955525fcea56cb4d16057c93bfb15eec42a83a1b644baf0e87a473f64e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Scoped: §9 held-pre-ingest source-carried metadata/lifecycle/blocker boundary; other mechanisms retain their owners. | `5797a2ac51328985e479d2bc101f310b96d2d75976acfaf5f066c529b31d309b` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Prior whole-file credit retained; provisional-influence and held-boundary source identity reused. | `e397a787911d72533fa0d6245f6331d8d176ea07a21a306d1296b41593dae9c4` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md` | Scoped: §11 retained archive cannot supply a Computed View query or inspection path. | `46cf463389ea339bb3a908177dda8d1548095e21da6abebcd2efeb6a8a54c0ff` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md` | Scoped: retained-archive isolation and no active/queryable Computed View use. | `1b539f57a7d31daba7c8da15d0dcdf988eba2e560c5d9532e3db42a28bcf96e6` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md` | Scoped: Computed View hiding/output-surface coverage and §15.4 per-surface failure boundary; complete privacy owner CH08-a. | `7fda28e994336a7ea0d17e217025cb71c116ec42ce3ecde3d8c9110783b52aad` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` | Scoped discovery: snapshot references concern enrollment/authority state, not a new Computed View schema; later owner CH09-h. | `184a63cf7dfbefdd73ea84c02506e3478374a48df2d9a2e174ed9a38305cacb6` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` | Scoped discovery: authority/session snapshots and current access boundaries; their full mechanics remain CH09. | `c449728139f732d5aefe5efd7ca1a0d251937c64bd73504ff8527cc3ec01b305` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` | Scoped discovery: authority_snapshot_identity is an authority-control identity rather than a Computed View snapshot; no mechanism imported. | `b39654a60744982d0e2f16c2bc3cd7a33f6ae47ff55b63b5b1dfffada719d709` |
| `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md` | Scoped discovery: Computed View/history comparisons used only to retain Appendix B tracking, not as behavior authority. | `fc014bbab36c87495d534ade8bb78f8de4197efa9408f5abb908743601a21522` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Scoped: full Group 10 restored operation-record laws and three unchanged unresolved questions; existing C-7B.10 atoms retained. | `9f6f9cac1e07ab14f0c6f3ed834b8260265dac6f6a430fa12be5c6e4c3f0b59f` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | Scoped discovery: Computed View/Bundle 4/Bundle 2 navigation matches; not behavior authority. | `457c6f43562a92cd82076640af44a58ea412335284c0e61da3c38f3ba63f24b9` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | Scoped discovery: Computed View/Bundle 4/Bundle 2 navigation matches; not behavior authority. | `3f1b95da77f620597e9ba862568f4247d1eb4d50f73c620888637dfcde03e3c9` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Scoped discovery: Computed View/Bundle 4/Bundle 2 navigation matches; not behavior authority. | `aafc7abe6522f4c7ece23f40560e648866188e1b5401ed6cd298809d15ed0f7b` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Scoped discovery: current Computed View/Bundle 4/Bundle 2 source identity and ownership navigation; not behavior authority. | `aad8d1aeee9a331ad6f4d9ddbcfa9c42eae2a94e1ef1bccde7484079181ff7b4` |

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

Round 4A later changed Chapters 0, 1, 2, 3-a to 3-d and 6-a to 6-g; the identities above are those preserved when this chapter was written, and the round 4A identities are listed in the round 4A delivery manifest.

### READ-folder files not yet read whole

65 inherited pending files remain. Scoped reading receives no new whole-file credit.

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
§1.3 no history/actions/roles/workflow in this chapter: PASS — 149 behavior cards reviewed; 0 workflow/advice hits. Delivery metadata remains outside behavior.
§1.4 every gap written as NOT DECIDED: PASS — 251 empty fields match 251 register rows; 13 additional mechanical slots are explicit.
§1.5 conflicts marked, none resolved: PASS — no conflict resolved. Accepted B5 content fills the earlier open design slot; status is carried by events without snapshot mutation. Provisional influence's unselected fixed-family representation is a named gap, not a fabricated source conflict. All inherited conflicts, restored §0B open questions and the excluded accepted foundation scope remain open.
§3 exactly one stamp per line: PASS — 149 headers, 1099 populated fields and 443 USED BY rows checked. 4 BUILT field lines name only existing built reading/store sources; no new machinery is stamped BUILT.
§4 every behavior line cited in the exact format: PASS — 60 distinct citations; 60 resolve within the named pinned sections. Populated fields and use rows are cited; the source-to-claim review accompanies mechanical resolution.
§5.4 one name per thing: PASS — 149 unique current IDs without prior collisions; 1715 named-card mentions checked. Shared atoms retain their established IDs and names.
§6 all template fields present, in order, for every part: PASS — 149 templates and 1350 field lines checked.
§6.3 reciprocity within this chapter: PASS — 382 internal relationship occurrences checked; 99 outgoing and 11 incoming continuation rows name both ends. No missing reciprocal; prior files remain unchanged.
§6.4 every decided detail written in, no citation used in place of content: PASS — 24 source-to-card rows reviewed; 70 expected source-name literals present. Existing atomic owners and remaining scopes are explicit.
§6.5 sub-parts recursed to the bottom: PASS — seven factors, nineteen profile fields with four disclosed-rule kinds, three trigger routes and six event kinds, snapshot fields including separate trigger type/object and ten source families, eleven refresh-event fields and five outcomes, six recovery cases, all declaration fields/two gates/nine dimensions/Tier-2 consequences, five active protections and fourteen lifecycle-event fields have current templates or explicitly reused atoms. Earlier source owners and later state/action/privacy/relevance mechanisms remain named. 0 current cards have all three TOGETHER fields empty.
§9 coverage matrix rows added for every file used: PASS — all 145 pinned READ-folder file paths remain in the carried inventory; current additions and 28 current READ RECORD fingerprints are present. Shared-package coverage remains partial where stated.
§10.11 no recommendation, no sentence addressed to Ness: PASS — all 149 behavior cards reviewed; no recommendation or addressed instruction.
Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`.

### Computed self-check results

Writer checks and the accompanying manual source/box review returned no unresolved current-file errors. They are not an independent audit or adoption. Plain human/precondition gates are justified in the inventory above.

| Check | Count |
|---|---|
| cards | 149 |
| field_lines | 1350 |
| used_by_rows | 443 |
| empty_fields | 251 |
| internal_relationships | 382 |
| external_relationships | 99 |
| distinct_citations | 60 |
| resolved_citations | 60 |
| empty_together_cards | 0 |
| plain_together_lines | 2 |
| formula_hits | 0 |
| wording_hits | 0 |
| errors | 0 |
| named_card_mentions_checked | 1715 |
| misfiled_box_fields_scanned | 1350 |
| restriction_failure_gate_slots_reviewed | 449 |
| registered_empty_fields | 251 |
| cross_piece_continuations_checked | 99 |
| covered_read_file_paths | 145 |
| read_fingerprints_checked | 28 |
| source_names_checked | 70 |
| source_names_missing | 0 |
| built_field_lines | 4 |
| behavior_workflow_hits | 0 |
| plain_gates_justified | 2 |
| outgoing_continuations | 99 |
| incoming_continuations | 11 |
| registered_fields | 251 |
| additional_gaps | 13 |
| pending_source_paths | 65 |
| source_map_rows | 24 |
| read_record_rows | 28 |

The delivery recount compares these metrics with the finished file.
