# Chapter 8-b — Group F: C-7R

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH08-b.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`  

This piece owns all fourteen §7R decisions, the shared output/configuration/vocabulary/validation and record contracts, A4’s mandatory declaration policy, and the shared side of the five accepted consumer declarations. Existing consumer-local settings, retry rules, currentness statuses, reading acceptance and shared uncertainty handling retain their earlier canonical owners. Full routing and query recovery remain CH08-c; BOP/OOP/affirmation/adaptation remain CH08-d–g; identity/security and phone mechanisms remain CH09; visual interfaces CH10-e; connected side paths CH11; register regeneration CH12. Proposed identifiers remain proposed. No numerical tuning, final mouth/validator selection, serialization or runtime implementation is inferred.

[SOURCE CONFLICT] `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` §7R describes one prior “privacy and deletion eligibility gate” and already-eligible material. V10 §7R instead explicitly distinguishes visible-output eligibility from internal-use authorization for the exact purpose, and says visible removal does not itself remove internal influence. V10 governs. The older unqualified prerequisite wording is retained here as the losing wording; it is not used to turn visible removal into an internal-use ban.

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; NHD identifiers locate decisions in the pinned index and do not replace behavior citations.

<!-- BEGIN BEHAVIOR -->

### C-7R — Attention & Relevance Control (§7R)
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The conceptually designed, not built, owner of explicit, auditable judgments about what is worth showing, retrieving or acting on for a particular purpose. [V10 §7R]
- Takes in: DESIGNED — Already-authorized candidates, targets, a recognized purpose and the applicable versioned declaration. Visible presentation, exports, external sharing, notifications and visible responses require visible-output eligibility; internal retrieval, relevance evaluation, reasoning, clash detection and Computed View assembly require internal-use authorization. [V10 §7R]
- Does: DESIGNED — Applies named categorical gates, then produces named graded dimensions with their own provenance for passing candidates; each consumer uses them under its own declared local rules. [V10 §7R]
- Gives out: DESIGNED — Purpose-scoped judgments, completed-evaluation events, disagreement records and separately recorded corrections, overrides, mode versions and unknown-purpose halts. [V10 §7R]
- Must never: DESIGNED — Determine truth, evidence strength, causation, authority, permission to act or Ness’s final judgment; merge Person-Boxes; resolve clashes or choose their correct side; rewrite, reorder or suppress roots, readings, tellings or clashes; own, rerun or redefine privacy eligibility; write directly into Living State Web; or guess an unknown purpose. Hiding, restriction, redaction, sealed isolation and deletion-from-view do not automatically remove internal influence; stopping internal use requires a separate explicit influence-removal instruction. [V10 §7R]
- Fails closed by: DESIGNED — Runs no evaluation for an unknown purpose or invalid declaration; gate-excluded candidates receive no graded judgment, and uncertain or failed values follow the declared owner’s honest handling. [V10 §7R]

TOGETHER
- Fed by: DESIGNED — C-7R.1 — Two-layer relevance judgment: two-layer output; C-7R.2 — Per-dimension producer selection: producers; C-7R.3 — Evaluation timing: timing; C-7R.4 — Two-tier configuration contract: two-tier contract; C-7R.5 — Ness inspection, correction and configuration changes: Ness inspection and changes; C-7R.6 — Mouth-produced dimension validation: mouth validation; C-7R.7 — Minimum shared relevance vocabulary: shared vocabulary; C-7R.8 — Living State Web relevance boundary: state boundary; C-7R.9 — Tier 1 structured purpose: purposes; C-7R.10 — Tier-boundary unresolved-rule reference: unresolved-rule reference; C-7R.11 — Relevance disagreement record: disagreements; C-7R.12 — Completed relevance event record: evaluation events; C-7R.13 — Per-judgment override pattern observation: override patterns; C-7R.14 — Unrecognized purpose-type halt: unknown-purpose halt. [V10 §7R]
- Fed by: ACCEPTED — C-7R.15 — Mandatory per-task relevance declaration policy: mandatory declaration policy; C-7R.16 — Accepted five-consumer relevance declarations: accepted consumer declarations and shared handling; C-7R.17 — Live relevance query interface: live-query interface; C-7B.7 — Hold-until-enough: recorded hold fact excludes held material from new surfacing. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] [04/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md §6]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): authorization for the exact current purpose precedes candidates; Level 1 protected-boundary rules, TSC blockers and explicit compartment restrictions still apply regardless of purpose. [SOURCE CONFLICT] V10’s purpose-specific authorization governs over Companion §7R’s unqualified privacy/deletion-eligibility wording; C-7R.4 — Two-tier configuration contract: Tier 1 must be valid; C-7R.14 — Unrecognized purpose-type halt: an unrecognized purpose halts before evaluation. [V10 §7R]
- Changes: DESIGNED — C-7D — Living State Web (§7D): may receive an emitted relevance event only as a possible authorized review trigger, never as currentness evidence or a direct state write; C-LMAC — Live Mechanism Access Coordinator (§26): receives the component’s whole live judgment with provenance. [V10 §7R] [V10 §26 / What LMAC Coordinates]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-13.3.2 — Authorized relevance evaluation | Declared judgments over prior-authorized material. | Uses relevance in the live context. | Privacy remains an earlier prerequisite. | [V10 §7R / EXTERNAL PREREQUISITE] [MAP C-13] |
| 2 · ACCEPTED | C-14.6.2 — Declared reference reliability | The declared Tier-1/Tier-2 reliability condition. | Uses earlier context only under the consuming mode. | Earlier material gains no automatic eligibility. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |
| 3 · DESIGNED | C-7F — Context Retrieval (§7F) | The valid current-purpose relevance judgment. | Selects retrieval context within its local declaration. | Relevance follows privacy and creates no access. | [MAP C-7F] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |
| 4 · ACCEPTED | C-7F.6.10.5.4 — Relevance disagreement record handoff | The shared disagreement-record contract. | Preserves producer-validator conflict through the shared owner. | No confidence winner silently replaces disagreement. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] |
| 5 · ACCEPTED | C-7F.6.12 — RM-CR-01 [proposed] logging contract | The distinct relevance-event contract. | Records the evaluation separately from retrieval audit. | One event does not replace the other owner’s record. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 6 · ACCEPTED | C-7F.6.14 — A4 eight-field declaration validity | The shared two-tier validation contract. | Runs only a valid current-purpose declaration. | A missing declaration cannot be improvised. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |
| 7 · DESIGNED | C-7A — Universal Filter (§7A) | Relevance after privacy authorization. | Keeps reading governance inside both boundaries. | Confidence cannot replace authorization or relevance. | [V10 §7A] [MAP C-7A] [V10 §0] [V10 §0A] |
| 8 · DESIGNED | C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B) | Purpose-specific relevance for derived operations. | Applies it after capture/use authorization. | Memory permanence is not a permission or truth grant. | [V10 §7B] [MAP C-7B] [V10 §0B] |
| 9 · ACCEPTED | C-7B.9.9 — Accepted Wonder surfacing | Genuine relevance of an accepted wonder-origin reading. | Allows ordinary-use surfacing under the established relevance owner. | Acceptance does not imply universal relevance. | [04/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md §6] |
| 10 · ACCEPTED | C-7B.9.9.1 — Relevant ordinary-use surfacing | The purpose-scoped relevance judgment. | Surfaces accepted wonder-origin material only on genuine relevance. | Origin and authority boundaries remain intact. | [04/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md §6] |
| 11 · ACCEPTED | C-7H.3.3 — RR2 — Instruction and context snapshot | Relevance after prior authorization. | Keeps reread retrieval inside the proper declared purpose. | Relevance does not supply authorization. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |
| 12 · DESIGNED | C-7GA.11.7.2 — Step 7B — Process triggered view profiles | The view-assembly relevance mode. | Uses that declaration during worker view assembly. | Worker completion cannot invent view relevance. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 13 · ACCEPTED | C-CREATE.10.9 — Creation access ordering | Relevance over already eligible creation material. | Keeps relevance behind privacy. | Creation status does not bypass authorization. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [MAP C-CREATE] |
| 14 · DESIGNED | C-7M — Computed View (§7M) | A valid declaration for the current view purpose. | Uses relevance within the full view priority order. | Selection does not become truth or state evidence. | [V10 §7A] [V10 §7M] [V10 §7Q] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] |
| 15 · DESIGNED | C-7M.2.4 — Computed View factor 4 — purpose relevance | Purpose-scoped relevance in the fourth priority factor. | Uses only the validated declaration. | Relevance does not collapse the seven-factor order. | [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [V10 §7R] |
| 16 · ACCEPTED | C-7M.3.3 — Computed View profile_purpose_type | The recognized controlled purpose and vocabulary version. | Binds the snapshot’s declared purpose. | An unknown type cannot be guessed. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [V10 §7R] |
| 17 · ACCEPTED | C-7M.3.11 — Computed View Tier-1 configuration reference | Tier-1 ownership and validation. | Keeps shared configuration with relevance control. | Tier 2 remains view-owned. | [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |
| 18 · ACCEPTED | C-7M.10 — Computed View proposed RM-CV-01 declaration | The valid shared declaration contract. | Uses the existing view-specific declaration after privacy. | No consumer silently takes over Tier 1. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] |
| 19 · ACCEPTED | C-7M.10.1 — Computed View proposed declaration identity and version | The versioned proposal-and-confirmation boundary. | Changes a reusable mode only through that path. | Prior declaration versions remain intact. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |
| 20 · ACCEPTED | C-7M.10.6 — Computed View mouth-authorization boundary | The declared-change and mouth-validation rules. | Keeps present mouth authorization at none. | Future interpretation requires an explicit new declaration. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| 21 · ACCEPTED | C-7M.10.9.4 — Computed View proposed shared unresolved handling | Validation and disagreement handling. | Retains uncertainty under the shared rule. | Confidence cannot silently settle the result. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| 22 · ACCEPTED | C-7M.10.11 — Computed View relevance evaluation record | The complete relevance-event schema. | Records the view’s completed relevance evaluation. | The event does not replace individual judgments. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 23 · ACCEPTED | C-7M.10.12 — Computed View invalid relevance declaration outcome | Unknown-purpose halt and confirmed change paths. | Stops invalid evaluation without guessing. | The request survives for explicit mapping or proposal. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] |
| 24 · DESIGNED | C-7D — Living State Web (§7D) | Review-trigger relevance only. | Keeps triggering separate from state currency evidence. | No relevance value establishes currentness. | [V10 §7D] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] |
| 25 · ACCEPTED | C-7D.14 — State-currentness review | Permitted review suggestions/events under the declaration. | Uses relevance only within its authorized review boundary. | The state owner keeps review authority. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §4B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10] |
| 26 · ACCEPTED | C-7D.14.1.1 — Review relevance-event reference | Emitted relevance events. | Receives an event as a possible review trigger. | The event is not evidence of the review outcome. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §7] |
| 27 · ACCEPTED | C-7D.14.2.12 — State-review evaluation logging | The settled relevance-event contract. | Records the evaluation separately from state review. | No relevance record rewrites state. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10] |
| 28 · ACCEPTED | C-7D.16 — Evidence-linked world model | Purpose-specific selection. | Uses relevance without converting it into truth or currency. | World-model support stays evidence-linked. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §4D] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §6] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §7] |
| 29 · ACCEPTED | C-24.2.1 — Accepted-connection retrieval route | The current purpose’s relevance configuration. | Keeps connection use purpose-bound after authorization. | A connection does not define its own relevance policy. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A] |
| 30 · ACCEPTED | C-24.19.7 — Connection I7 accepted-use interface | The accepted purpose/relevance configuration. | Uses the retrieval owner and stateless router under that configuration. | Routing gains no relevance authority. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 31 · ACCEPTED | C-7N.13.1 — Proposed RM-AS-01 identity and version | The confirmed version-change path. | Preserves the action declaration’s prior versions. | Reusable changes cannot arise silently. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] |
| 32 · ACCEPTED | C-7N.13.12 — Action-surfacing relevance audit contract | The complete evaluation and disagreement record contracts. | Records actual relevance work and conflict. | Possibility history stays separate from relevance history. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] |
| 33 · ACCEPTED | C-7N.13.13.4 — Action-surfacing unrecognized-purpose failure | Unknown-purpose halt and versioned new-type handling. | Refuses guessed purpose substitution. | The original request remains preserved. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] |
| 34 · ACCEPTED | C-7P.13.4 — Authority records privacy and non-evidence boundary | Purpose and selection relevance. | Keeps it separate from action authority and truth. | Relevance grants no permission. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| 35 · DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | The already-authorized candidate boundary. | Admits only purpose-authorized material to relevance. | Relevance cannot rerun or redefine privacy. | [V10 §7Q] |
| 36 · DESIGNED | C-7Q.6.2 — Layer 1 — Pre-retrieval visible-output eligibility | The purpose-authorized candidate space. | Limits relevance to the obtained privacy decision. | Possession does not imply eligibility. | [V10 §7Q] |
| 37 · ACCEPTED | C-7Q.11.6 — Retrieval, relevance and authorization-query boundary | The authorized candidate-space query result. | Keeps retrieval and relevance inside the privacy owner’s decision. | Stateless routing cannot widen permission. | [04/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md §16] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 38 · ACCEPTED | C-AFFIRM.8 — Protected append-only affirmation living record | The actual occurrence, target links and access/use operations. | Gates this place: relevance only after authorization. | Nothing in this card. | [V10 §0B] [MAP C-AFFIRM] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §19] [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §20] |
| 39 · ACCEPTED | C-LMAC.14.2 — Reread context routing order | The assignment and broadest safely available clearly relevant context. | Gates this place: declared relevance follows. | Nothing in this card. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §7] |
| 40 · ACCEPTED | C-OOP.8.7 — OOP is not an LMAC query target | A request for behavioral context. | Supplies purpose-scoped relevance. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 41 · ACCEPTED | C-7N.9 — Action-surfacing evidence handoff | Permitted source evidence and the current picture, retaining their different roles. | Gates this place: privacy, relevance and authority govern this handoff and are never evidence. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] |
| 42 · DESIGNED | C-LMAC.3.11 — Shared response-pattern reading access | The stored pattern readings produced by the Meaning Engine. | Supplies purpose-scoped relevance. | Nothing in this card. | [V10 §26.5] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 43 · ACCEPTED | C-NEW-UDOK.1.12 — E12 — Relevance-owner result reference [proposed] | The relevance owner's record after privacy has run. | Supplies its own relevance evaluation. | Nothing in this card. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §A.2] |
| 44 · ACCEPTED | C-OOP.8.6 — Outcome held-material and privacy boundary | The current source lifecycle, blockers and authorization. | Gates this place: later declared relevance, never an access grant. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| 45 · ACCEPTED | C-16.10.8 — Capture authorization_refs [proposed] | The §7Q and §7R authorizations applying to the contribution. | Supplies applicable relevance authorization. | Nothing in this card. | [04/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md §2.11] |
| 46 · DESIGNED | C-8 — Research Pipeline / Knowledge Catcher (§8) | Research topics, raw outside sources and stored information to compare against outside evidence. | Gates this place: purpose relevance operates within the already permitted material. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [V10 §8] [MAP C-8] |
| 47 · DESIGNED | C-AFFIRM — Off-board Affirmation Feedback Seam (§11 item 23) | Ness’s accept/reject response to one or more specific readings through the view/chat surface. | Gates this place: later relevance supplies no truth or authority. | Nothing in this card. | [V10 §11] [V10 §0] [MAP C-AFFIRM] |
| 48 · DESIGNED | C-LMAC.3.10 — Shared behavioral observation-root access | The permitted stored observation roots. | Supplies the declared relevance judgment. | Nothing in this card. | [V10 §26.5] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 49 · DESIGNED | C-LEARN — Personal Learning and Adaptation (§26, cross-cutting) | Authorized behavioral/outcome observations, their shared readings and the current live mechanism during function execution. | Gates this place: relevance does not grant access or truth. | Nothing in this card. | [V10 §26.1] [V10 §26.9] [MAP C-LEARN] |
| 50 · ACCEPTED | C-NEW-UDOK.4.6 — P6 — Relevance result | The relevance owner's record after privacy. | Owns the relevance evaluation. | Nothing in this card. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §D.2] |
| 51 · ACCEPTED | C-19.21.4 — Accepted Wonder surfacing | Properly accepted Wonder material, genuine relevance or Ness's explicit request. | Gates this place: governs relevance without creating truth or authority. | Nothing in this card. | [04/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md §6] |
| 52 · ACCEPTED | C-NEW-UDOK.13.12 — I-12 — Routing, privacy, access, authority and relevance reference interface [proposed] | Their routing and gate-decision references. | Supply their routing and gate-decision references. | Nothing in this card. | [04/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md §T] |

SUB-PARTS: C-7R.1 — Two-layer relevance judgment; C-7R.2 — Per-dimension producer selection; C-7R.3 — Evaluation timing; C-7R.4 — Two-tier configuration contract; C-7R.5 — Ness inspection, correction and configuration changes; C-7R.6 — Mouth-produced dimension validation; C-7R.7 — Minimum shared relevance vocabulary; C-7R.8 — Living State Web relevance boundary; C-7R.9 — Tier 1 structured purpose; C-7R.10 — Tier-boundary unresolved-rule reference; C-7R.11 — Relevance disagreement record; C-7R.12 — Completed relevance event record; C-7R.13 — Per-judgment override pattern observation; C-7R.14 — Unrecognized purpose-type halt; C-7R.15 — Mandatory per-task relevance declaration policy; C-7R.16 — Accepted five-consumer relevance declarations; C-7R.17 — Live relevance query interface

### C-7R.1 — Two-layer relevance judgment
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The structured output after external privacy authorization. [V10 §7R]
- Takes in: DESIGNED — A candidate and its declared task context. [V10 §7R]
- Does: DESIGNED — Runs the categorical layer first and grades only passing candidates. [V10 §7R]
- Gives out: DESIGNED — Named boolean gate results and, where eligible, named dimensions with values and provenance. [V10 §7R]
- Must never: DESIGNED — Collapse dimensions into a hidden aggregate or grade a gate-excluded candidate. [V10 §7R]
- Fails closed by: DESIGNED — Excludes a candidate that fails any required context gate without producing its graded judgment. [V10 §7R]

TOGETHER
- Fed by: DESIGNED — C-7R.1.1 — Context-specific boolean gate: categorical membership; C-7R.1.2 — Graded named dimensions: graded output. [V10 §7R]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): eligibility is established before this judgment; C-7R.4 — Two-tier configuration contract: the mode must declare its gates and dimensions. [V10 §7R]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R — Attention & Relevance Control (§7R) | The two distinct layers. | Uses categorical inclusion before graded interpretation. | The output remains explicit and purpose-bound. | [V10 §7R] |

SUB-PARTS: C-7R.1.1 — Context-specific boolean gate; C-7R.1.2 — Graded named dimensions

### C-7R.1.1 — Context-specific boolean gate
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Layer 1: cheap, categorical, deterministic membership in the current task. [V10 §7R]
- Takes in: DESIGNED — Each named required gate condition declared for the consuming context. [V10 §7R]
- Does: DESIGNED — Evaluates the declared conditions as readable boolean rules. [V10 §7R]
- Gives out: DESIGNED — Pass results or exclusion from this context. [V10 §7R]
- Must never: DESIGNED — Use an undeclared gate, a mouth interpretation as a categorical gate, or a failed candidate’s graded values. [V10 §7R]
- Fails closed by: DESIGNED — Any failed required condition excludes the candidate and prevents graded judgment. [V10 §7R]

TOGETHER
- Fed by: DESIGNED — C-7R.7.1 — Shared deterministic gate vocabulary: minimum shared deterministic gate vocabulary. [V10 §7R]
- Gated by: DESIGNED — C-7R.6.4 — Mouth dimensions cannot be categorical gates: interpretive mouth output cannot serve as a gate. [V10 §7R]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.1 — Two-layer relevance judgment | The candidate’s categorical membership. | Grades only candidates passing every required condition. | Excluded candidates remain ungraded. | [V10 §7R] |
| 2 · DESIGNED | C-7R.1.2 — Graded named dimensions | All required gate results. | Produces dimensions only after every required condition passes. | A failed gate stops grading. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.1.2 — Graded named dimensions
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Layer 2: separately named, provenance-bearing values. [V10 §7R]
- Takes in: DESIGNED — A gate-passing candidate, target and declared dimensions. [V10 §7R]
- Does: DESIGNED — Produces each dimension separately and preserves its source or method. [V10 §7R]
- Gives out: DESIGNED — The dimension name, its value and its provenance, without a single hidden score. [V10 §7R]
- Must never: DESIGNED — Collapse dimensions or treat a relevance value as truth, evidence strength, causation, authority or permission. [V10 §7R]
- Fails closed by: DESIGNED — Produces no graded judgment when any required context gate fails. [V10 §7R]

TOGETHER
- Fed by: DESIGNED — C-7R.1.2.1 — Dimension name: name; C-7R.1.2.2 — Dimension value: value; C-7R.1.2.3 — Dimension source or method: source or method; C-7R.2 — Per-dimension producer selection: declared producer per dimension. [V10 §7R]
- Gated by: DESIGNED — C-7R.1.1 — Context-specific boolean gate: every required gate must pass. [V10 §7R]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.1 — Two-layer relevance judgment | The separate graded values and provenance. | Returns an inspectable structured judgment. | Consumer-local use remains explicit. | [V10 §7R] |

SUB-PARTS: C-7R.1.2.1 — Dimension name; C-7R.1.2.2 — Dimension value; C-7R.1.2.3 — Dimension source or method

### C-7R.1.2.1 — Dimension name
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The explicit name of one graded dimension. [V10 §7R]
- Takes in: DESIGNED — The name declared in the mode. [V10 §7R]
- Does: DESIGNED — Identifies which dimension a value belongs to. [V10 §7R]
- Gives out: DESIGNED — A named value rather than an anonymous score. [V10 §7R]
- Must never: DESIGNED — Hide several dimensions behind one unspecified score. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.1.2 — Graded named dimensions | The declared dimension name. | Keeps the value individually identifiable. | Interpretation is traceable to a declared dimension. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.1.2.2 — Dimension value
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The separately preserved result for one named dimension. [V10 §7R]
- Takes in: DESIGNED — The value its assigned producer computed. [V10 §7R]
- Does: DESIGNED — Retains that value under its own dimension identity. [V10 §7R]
- Gives out: DESIGNED — An individual graded result. [V10 §7R]
- Must never: DESIGNED — Replace the separate result with a hidden composite. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.1.2 — Graded named dimensions | The produced value. | Returns it beside its name and provenance. | No aggregate erases the individual result. | [V10 §7R] |
| 2 · DESIGNED | C-7R.2.4 — Common dimension producer provenance | The actual produced value. | Retains it with producer and version provenance. | The value remains separately inspectable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.1.2.3 — Dimension source or method
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The provenance of an individual graded value. [V10 §7R]
- Takes in: DESIGNED — The source or method producing that value. [V10 §7R]
- Does: DESIGNED — Preserves how the value was obtained. [V10 §7R]
- Gives out: DESIGNED — Inspectable provenance beside the named value. [V10 §7R]
- Must never: DESIGNED — Present an untraceable graded value. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.2.4 — Common dimension producer provenance: required producer and version provenance. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.1.2 — Graded named dimensions | The source or method. | Carries provenance with every named result. | The consumer can inspect the derivation. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.2 — Per-dimension producer selection
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Selection of an appropriate producer for each named dimension individually. [V10 §7R]
- Takes in: DESIGNED — The dimension’s structural, semantic or specifically interpretive task. [V10 §7R]
- Does: DESIGNED — Uses reproducible rules where reliable, embedding similarity for semantic/thematic proximity, and a declaration-authorized mouth only for interpretation neither alternative can reliably produce. [V10 §7R]
- Gives out: DESIGNED — Each dimension with its own producer and provenance. [V10 §7R]
- Must never: DESIGNED — Assign the mouth indiscriminately, let it self-approve, or use embeddings for dimensions rules reliably compute. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.2.1 — Deterministic dimension producer: deterministic rules; C-7R.2.2 — Embedding dimension producer: embedding model; C-7R.2.3 — Declared interpretive mouth producer: declared mouth role; C-7R.2.4 — Common dimension producer provenance: common provenance. [V10 §7R]
- Gated by: DESIGNED — C-7R.4 — Two-tier configuration contract: the assigned producer must be declared; C-7R.6 — Mouth-produced dimension validation: mouth-produced values require deterministic validation. [V10 §7R]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R — Attention & Relevance Control (§7R) | Producer-specific named results. | Preserves the method behind every dimension. | Model confidence gains no authority. | [V10 §7R] |
| 2 · DESIGNED | C-7R.1.2 — Graded named dimensions | The individually assigned producers. | Produces each declared value through its proper method. | Provenance stays separate by dimension. | [V10 §7R] |
| 3 · DESIGNED | C-7R.4.1.6 — Tier 1 dimensions and producers | The producer-selection boundary. | Declares the appropriate producer for each dimension. | Rule-computable results do not default to a model. | [V10 §7R] |

SUB-PARTS: C-7R.2.1 — Deterministic dimension producer; C-7R.2.2 — Embedding dimension producer; C-7R.2.3 — Declared interpretive mouth producer; C-7R.2.4 — Common dimension producer provenance

### C-7R.2.1 — Deterministic dimension producer
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Rules for structural, temporal, currency, count and other directly computable dimensions. [V10 §7R]
- Takes in: DESIGNED — The declared source facts and rule version. [V10 §7R]
- Does: DESIGNED — Computes a reproducible result from the same inputs with no model involved. [V10 §7R]
- Gives out: DESIGNED — A rule-produced value and provenance. [V10 §7R]
- Must never: DESIGNED — Use a model where the dimension is reliably rule-computable. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.2 — Per-dimension producer selection | A directly computable dimension. | Selects its reproducible deterministic rule. | No model is needed for the calculation. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.2.2 — Embedding dimension producer
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The all-MiniLM-L6-v2 embedding role for semantic similarity and thematic proximity. [V10 §7R]
- Takes in: DESIGNED — The declared candidate and target or query representation. [V10 §7R]
- Does: DESIGNED — Produces only the semantic/thematic dimensions assigned to embeddings. [V10 §7R]
- Gives out: DESIGNED — Embedding-derived values with model and index versions. [V10 §7R]
- Must never: DESIGNED — Produce dimensions that deterministic rules can reliably compute. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.2.4 — Common dimension producer provenance: the actual producer, model and index provenance required for the dimension. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.2 — Per-dimension producer selection | Semantic or thematic proximity. | Uses the embedding producer for that dimension. | Similarity remains a provenance-bearing value. | [V10 §7R] |
| 2 · DESIGNED | C-7R.7.2.1 — semantic_similarity | The all-MiniLM-L6-v2 embedding role. | Produces semantic similarity with model/index provenance. | Similarity remains separate from structural context. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.2.3 — Declared interpretive mouth producer
Stamp: DESIGNED    Source: [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]

ALONE
- What it is: DESIGNED — The dolphin-llama3 mouth role named in V10 for specifically declared interpretive dimensions; accepted formal declarations use no mouth dimensions and leave final mouth/provider choices open. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Takes in: DESIGNED — A named interpretive dimension and context authorized by its relevance mode. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Does: DESIGNED — Uses the mouth only where rules and embedding similarity cannot reliably produce the dimension; mode declaration authorizes calls without Ness approving each invocation. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Gives out: DESIGNED — A scoped interpretive value awaiting the required validation. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Must never: DESIGNED — Use a broad mouth flag, operate outside the named dimensions or contexts, or self-approve the result. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Fails closed by: DESIGNED — No mouth dimension runs outside its declared scope. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]

TOGETHER
- Fed by: DESIGNED — C-7R.4.1.7 — Tier 1 scoped mouth authorization: named-dimension/context authorization. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Gated by: DESIGNED — C-7R.6 — Mouth-produced dimension validation: validation remains required; C-7R.6.4 — Mouth dimensions cannot be categorical gates: a mouth interpretation cannot be a categorical gate. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.2 — Per-dimension producer selection | A specifically authorized interpretive dimension. | Selects the mouth only within the declaration. | No per-call approval queue or model authority is created. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.2.4 — Common dimension producer provenance
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Provenance required for every dimension, regardless of producer. [V10 §7R]
- Takes in: DESIGNED — The actual producer, applicable rule/model/index/prompt versions and result. [V10 §7R]
- Does: DESIGNED — Preserves each production binding alongside the value. [V10 §7R]
- Gives out: DESIGNED — Producer identity, relevant versions and the produced value. [V10 §7R]
- Must never: DESIGNED — Omit provenance because a dimension was deterministic. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.2.4.1 — Dimension producer identity: producer; C-7R.2.4.2 — Dimension rule or model version: rule or model version; C-7R.2.4.3 — Dimension index or prompt version: index or prompt version; C-7R.1.2.2 — Dimension value: value. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.2 — Per-dimension producer selection | Complete producer/version/value provenance. | Keeps every selected method auditable. | No producer is exempt. | [V10 §7R] |
| 2 · DESIGNED | C-7R.1.2.3 — Dimension source or method | The exact production bindings. | Retains how the dimension arose. | The source/method account is inspectable. | [V10 §7R] |
| 3 · DESIGNED | C-7R.11.5 — Disagreement producer identity and version | The original dimension’s production bindings. | Records the mouth model, prompt and configuration provenance. | Disagreement remains bound to its actual producer. | [V10 §7R] |
| 4 · DESIGNED | C-7R.2.2 — Embedding dimension producer | The embedding producer’s required model/index provenance. | Preserves the actual versions with the value. | Embedding similarity remains auditable. | [V10 §7R] |
| 5 · DESIGNED | C-7R.3.3.4 — Precomputed production versions | All applicable production identities and versions. | Preserves them in the precomputed judgment. | A later producer change cannot masquerade as the old computation. | [V10 §7R] |

SUB-PARTS: C-7R.2.4.1 — Dimension producer identity; C-7R.2.4.2 — Dimension rule or model version; C-7R.2.4.3 — Dimension index or prompt version

### C-7R.2.4.1 — Dimension producer identity
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The identity of the producer that generated a value. [V10 §7R]
- Takes in: DESIGNED — The actual rule, embedding or mouth producer. [V10 §7R]
- Does: DESIGNED — Records which producer generated the dimension. [V10 §7R]
- Gives out: DESIGNED — A producer identity attached to that result. [V10 §7R]
- Must never: DESIGNED — Replace the actual producer with a generic confidence claim. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.2.4 — Common dimension producer provenance | The generating producer. | Associates the value with its origin. | Production can be audited. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.2.4.2 — Dimension rule or model version
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The applicable version of the generating rule or model. [V10 §7R]
- Takes in: DESIGNED — The rule version or model version used. [V10 §7R]
- Does: DESIGNED — Preserves the version actually applied. [V10 §7R]
- Gives out: DESIGNED — A version-bound production result. [V10 §7R]
- Must never: DESIGNED — Silently attribute an old result to a newer producer version. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.2.4 — Common dimension producer provenance | The applied rule/model version. | Binds provenance to the actual producer configuration. | Later producer changes remain distinguishable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.2.4.3 — Dimension index or prompt version
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The index or prompt version where applicable to the producer. [V10 §7R]
- Takes in: DESIGNED — The actual index version or prompt version used. [V10 §7R]
- Does: DESIGNED — Preserves the applicable production context. [V10 §7R]
- Gives out: DESIGNED — Versioned index/prompt provenance when relevant. [V10 §7R]
- Must never: DESIGNED — Omit an applicable index or prompt binding. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.2.4 — Common dimension producer provenance | The applicable index/prompt version. | Retains the concrete production context. | The result remains attributable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.3 — Evaluation timing
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — On-demand relevance by default, with optional declared latency-sensitive precomputation. [V10 §7R]
- Takes in: DESIGNED — A consumer request for specific candidates in a specific context, or a declared trigger. [V10 §7R]
- Does: DESIGNED — Computes relevance at the request moment unless the context explicitly permits triggered precomputation. [V10 §7R]
- Gives out: DESIGNED — Context-bound judgments with validity maintained under declared rules. [V10 §7R]
- Must never: DESIGNED — Create a continuously maintained global relevance state or make a cached result permanently relevant everywhere. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.3.1 — On-demand evaluation: on-demand evaluation; C-7R.3.2 — Declared triggered precomputation: triggered precomputation; C-7R.3.3 — Precomputed judgment bindings: precomputed bindings; C-7R.3.4 — Context-bound reuse and invalidation: reuse and invalidation; C-7R.3.5 — Mouth precomputation prerequisites: mouth precomputation conditions. [V10 §7R]
- Gated by: DESIGNED — C-7R.4 — Two-tier configuration contract: timing and applicable triggers must be declared. [V10 §7R]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R — Attention & Relevance Control (§7R) | The declared timing for this context. | Computes relevance as a contextual judgment. | No global background truth is maintained. | [V10 §7R] |

SUB-PARTS: C-7R.3.1 — On-demand evaluation; C-7R.3.2 — Declared triggered precomputation; C-7R.3.3 — Precomputed judgment bindings; C-7R.3.4 — Context-bound reuse and invalidation; C-7R.3.5 — Mouth precomputation prerequisites

### C-7R.3.1 — On-demand evaluation
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The default computation at the moment a consumer requests relevance. [V10 §7R]
- Takes in: DESIGNED — A specific candidate or set of candidates and specific context. [V10 §7R]
- Does: DESIGNED — Computes the requested judgment at that moment. [V10 §7R]
- Gives out: DESIGNED — A judgment bound to the actual request. [V10 §7R]
- Must never: DESIGNED — Treat an earlier unrelated judgment as globally valid. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.3 — Evaluation timing | The current request. | Uses on-demand timing unless precomputation is explicitly declared. | The default follows the current context. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.3.2 — Declared triggered precomputation
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Optional precomputation for specifically declared latency-sensitive contexts. [V10 §7R]
- Takes in: DESIGNED — The declared trigger and context configuration. [V10 §7R]
- Does: DESIGNED — Computes only within the enabled context and preserves its complete bindings. [V10 §7R]
- Gives out: DESIGNED — A precomputed judgment with explicit validity or staleness. [V10 §7R]
- Must never: DESIGNED — Enable precomputation globally or silently extend it to another context. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.3.3 — Precomputed judgment bindings: the precomputed record bindings. [V10 §7R]
- Gated by: DESIGNED — C-7R.3.4 — Context-bound reuse and invalidation: reuse requires matching context and validity; C-7R.3.5 — Mouth precomputation prerequisites: mouth precomputation has two additional prerequisites. [V10 §7R]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.3 — Evaluation timing | An explicitly enabled latency-sensitive trigger. | Permits only that context’s optional precomputation. | No global relevance state results. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.3.3 — Precomputed judgment bindings
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The preserved context and production identity of every precomputed result. [V10 §7R]
- Takes in: DESIGNED — The exact context, consumer configuration, candidate/target, production versions, trigger, time and validity. [V10 §7R]
- Does: DESIGNED — Retains all seven field groups with the result. [V10 §7R]
- Gives out: DESIGNED — A fully context-bound precomputed judgment. [V10 §7R]
- Must never: DESIGNED — Reuse a result stripped of its context or validity. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.3.3.1 — Precomputed context or purpose identifier: context/purpose; C-7R.3.3.2 — Precomputed consuming mode and configuration version: consuming mode/configuration version; C-7R.3.3.3 — Precomputed candidate and target identifiers: candidate/target identifiers; C-7R.3.3.4 — Precomputed production versions: production versions; C-7R.3.3.5 — Precomputed trigger: trigger; C-7R.3.3.6 — Precomputed production time: production time; C-7R.3.3.7 — Precomputed validity or staleness state: validity/staleness. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.3 — Evaluation timing | The complete precomputed bindings. | Keeps precomputation specific to its origin. | Cached relevance cannot become permanent. | [V10 §7R] |
| 2 · DESIGNED | C-7R.3.2 — Declared triggered precomputation | All seven binding groups. | Records the exact precomputation. | Later reuse has an explicit basis. | [V10 §7R] |
| 3 · DESIGNED | C-7R.3.4 — Context-bound reuse and invalidation | The saved context and validity bindings. | Compares them with current reuse conditions. | Mismatched cached results cannot remain silently valid. | [V10 §7R] |

SUB-PARTS: C-7R.3.3.1 — Precomputed context or purpose identifier; C-7R.3.3.2 — Precomputed consuming mode and configuration version; C-7R.3.3.3 — Precomputed candidate and target identifiers; C-7R.3.3.4 — Precomputed production versions; C-7R.3.3.5 — Precomputed trigger; C-7R.3.3.6 — Precomputed production time; C-7R.3.3.7 — Precomputed validity or staleness state

### C-7R.3.3.1 — Precomputed context or purpose identifier
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The context or purpose identity of the precomputation. [V10 §7R]
- Takes in: DESIGNED — The identifier for the exact context or purpose. [V10 §7R]
- Does: DESIGNED — Preserves that identity with the result. [V10 §7R]
- Gives out: DESIGNED — An explicit context/purpose binding. [V10 §7R]
- Must never: DESIGNED — Treat a different purpose as the same context. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.3.3 — Precomputed judgment bindings | The context/purpose identifier. | Retains the result’s scope. | A result cannot silently cross contexts. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.3.3.2 — Precomputed consuming mode and configuration version
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The consuming mode and configuration version used. [V10 §7R]
- Takes in: DESIGNED — The actual mode and configuration version. [V10 §7R]
- Does: DESIGNED — Records the configuration under which computation occurred. [V10 §7R]
- Gives out: DESIGNED — A version-bound mode reference. [V10 §7R]
- Must never: DESIGNED — Attribute a cached result to a changed configuration. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.3.3 — Precomputed judgment bindings | The consuming mode and version. | Preserves the evaluation configuration. | Version changes can invalidate reuse. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.3.3.3 — Precomputed candidate and target identifiers
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The candidate and target identities evaluated. [V10 §7R]
- Takes in: DESIGNED — The exact candidate and target identifiers. [V10 §7R]
- Does: DESIGNED — Retains both sides of the judgment. [V10 §7R]
- Gives out: DESIGNED — Identified candidates and targets. [V10 §7R]
- Must never: DESIGNED — Substitute another object while retaining the old result. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.3.3 — Precomputed judgment bindings | Candidate/target identifiers. | Binds the result to the evaluated objects. | Object scope remains exact. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.3.3.4 — Precomputed production versions
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The producer, rule, model, index and prompt versions used by precomputation. [V10 §7R]
- Takes in: DESIGNED — The actual applicable production identities and versions. [V10 §7R]
- Does: DESIGNED — Preserves every applicable producer/version binding. [V10 §7R]
- Gives out: DESIGNED — Reproducible production provenance. [V10 §7R]
- Must never: DESIGNED — Silently reuse a result as if computed by a changed producer. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.2.4 — Common dimension producer provenance: the canonical per-dimension production provenance. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.3.3 — Precomputed judgment bindings | All applicable production versions. | Retains how the cached result was produced. | A producer change is detectable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.3.3.5 — Precomputed trigger
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The trigger that caused computation. [V10 §7R]
- Takes in: DESIGNED — The actual triggering event. [V10 §7R]
- Does: DESIGNED — Preserves the cause of this precomputation. [V10 §7R]
- Gives out: DESIGNED — A traceable trigger binding. [V10 §7R]
- Must never: DESIGNED — Invent an unrelated trigger after computation. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.3.3 — Precomputed judgment bindings | The computation trigger. | Records why the result was produced. | Precomputation remains attributable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.3.3.6 — Precomputed production time
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The time the precomputed result was produced. [V10 §7R]
- Takes in: DESIGNED — The actual production time. [V10 §7R]
- Does: DESIGNED — Preserves when computation occurred. [V10 §7R]
- Gives out: DESIGNED — A production timestamp. [V10 §7R]
- Must never: DESIGNED — Replace production time with later reuse time. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.3.3 — Precomputed judgment bindings | The production time. | Retains the age of the computation. | Reuse does not make an old result newly computed. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.3.3.7 — Precomputed validity or staleness state
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The current validity or staleness of the precomputed judgment. [V10 §7R]
- Takes in: DESIGNED — The declared validity conditions and invalidating events. [V10 §7R]
- Does: DESIGNED — Keeps whether the result remains valid explicit. [V10 §7R]
- Gives out: DESIGNED — A validity/staleness state. [V10 §7R]
- Must never: DESIGNED — Silently present a stale result as currently valid. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.3.3 — Precomputed judgment bindings | The current validity/staleness state. | Carries the condition needed for safe reuse. | Staleness is visible. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.3.4 — Context-bound reuse and invalidation
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The restriction on reusing cached or precomputed judgments. [V10 §7R]
- Takes in: DESIGNED — The saved context/validity and changes in purpose, source material, configuration, producer version, a relevant Ness response event or another declared invalidating event. [V10 §7R]
- Does: DESIGNED — Reuses a result only while its context and declared validity conditions still match; marks it stale or recomputes when any listed invalidator changes. [V10 §7R]
- Gives out: DESIGNED — A valid context-matching reuse, or staleness/recomputation. [V10 §7R]
- Must never: DESIGNED — Silently treat a stale or differently scoped result as permanent relevance. [V10 §7R]
- Fails closed by: DESIGNED — A context or validity mismatch prevents reuse of the result as valid. [V10 §7R]

TOGETHER
- Fed by: DESIGNED — C-7R.3.3 — Precomputed judgment bindings: exact saved bindings. C-7R.3.4.1 — Changed-purpose invalidation: purpose change; C-7R.3.4.2 — Changed-source invalidation: source change; C-7R.3.4.3 — Changed-configuration invalidation: configuration change; C-7R.3.4.4 — Changed-producer-version invalidation: producer-version change; C-7R.3.4.5 — Relevant Ness-response invalidation: relevant Ness response; C-7R.3.4.6 — Other declared invalidating event: other declared invalidator. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.3 — Evaluation timing | Context and validity checks. | Keeps reused judgments context-specific. | Changed inputs cannot silently inherit an old result. | [V10 §7R] |
| 2 · DESIGNED | C-7R.3.2 — Declared triggered precomputation | The current reuse conditions. | Retains precomputation only while those conditions match. | Invalidated results become stale or are recomputed. | [V10 §7R] |
| 3 · DESIGNED | C-7R.4.1.9 — Tier 1 precomputation triggers and invalidators | The context-bound reuse and invalidation rules. | Declares the triggers and events needed by the mode. | Precomputation has explicit validity limits. | [V10 §7R] |

SUB-PARTS: C-7R.3.4.1 — Changed-purpose invalidation; C-7R.3.4.2 — Changed-source invalidation; C-7R.3.4.3 — Changed-configuration invalidation; C-7R.3.4.4 — Changed-producer-version invalidation; C-7R.3.4.5 — Relevant Ness-response invalidation; C-7R.3.4.6 — Other declared invalidating event

### C-7R.3.4.1 — Changed-purpose invalidation
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Invalidation when the purpose changes. [V10 §7R]
- Takes in: DESIGNED — The saved and current purpose. [V10 §7R]
- Does: DESIGNED — Marks the old result stale or recomputes when the purpose changes. [V10 §7R]
- Gives out: DESIGNED — Staleness or a newly computed context-specific result. [V10 §7R]
- Must never: DESIGNED — Reuse the old purpose’s result as valid for the new purpose. [V10 §7R]
- Fails closed by: DESIGNED — The changed purpose prevents valid old-result reuse. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.3.4 — Context-bound reuse and invalidation | A purpose change. | Invalidates or recomputes the saved result. | Relevance cannot cross purposes silently. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.3.4.2 — Changed-source invalidation
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Invalidation when source material changes. [V10 §7R]
- Takes in: DESIGNED — The source material used and the changed source. [V10 §7R]
- Does: DESIGNED — Marks the result stale or recomputes. [V10 §7R]
- Gives out: DESIGNED — Staleness or a recomputed result. [V10 §7R]
- Must never: DESIGNED — Present an old-source result as if based on changed material. [V10 §7R]
- Fails closed by: DESIGNED — The change prevents unchanged valid reuse. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.3.4 — Context-bound reuse and invalidation | A source-material change. | Invalidates or recomputes. | The result remains bound to its real inputs. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.3.4.3 — Changed-configuration invalidation
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Invalidation when the configuration changes. [V10 §7R]
- Takes in: DESIGNED — The saved and current configuration. [V10 §7R]
- Does: DESIGNED — Marks the result stale or recomputes under the changed configuration. [V10 §7R]
- Gives out: DESIGNED — Staleness or a new configuration-bound result. [V10 §7R]
- Must never: DESIGNED — Attribute the old result to the new configuration. [V10 §7R]
- Fails closed by: DESIGNED — The mismatch prevents valid reuse. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.3.4 — Context-bound reuse and invalidation | A configuration change. | Invalidates or recomputes the result. | Versions remain distinct. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.3.4.4 — Changed-producer-version invalidation
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Invalidation when the producer version changes. [V10 §7R]
- Takes in: DESIGNED — The producing version and current version. [V10 §7R]
- Does: DESIGNED — Marks the earlier result stale or recomputes. [V10 §7R]
- Gives out: DESIGNED — Staleness or a result produced under the new version. [V10 §7R]
- Must never: DESIGNED — Pretend the old value was produced by the new version. [V10 §7R]
- Fails closed by: DESIGNED — Version mismatch prevents valid reuse. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.3.4 — Context-bound reuse and invalidation | A producer-version change. | Invalidates or recomputes. | Production provenance remains honest. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.3.4.5 — Relevant Ness-response invalidation
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Invalidation from a relevant Ness response event. [V10 §7R]
- Takes in: DESIGNED — The relevant recorded response and cached context. [V10 §7R]
- Does: DESIGNED — Marks the result stale or recomputes when that event changes the applicable context. [V10 §7R]
- Gives out: DESIGNED — Staleness or a recomputed result. [V10 §7R]
- Must never: DESIGNED — Ignore a relevant response while claiming the old result remains valid. [V10 §7R]
- Fails closed by: DESIGNED — The invalidating response prevents unchanged valid reuse. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.3.4 — Context-bound reuse and invalidation | A relevant Ness response event. | Invalidates or recomputes the affected result. | Contextual correction is not silently ignored. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.3.4.6 — Other declared invalidating event
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — An additional invalidator explicitly declared by the mode. [V10 §7R]
- Takes in: DESIGNED — The declared event and its actual occurrence/change. [V10 §7R]
- Does: DESIGNED — Marks the affected result stale or recomputes. [V10 §7R]
- Gives out: DESIGNED — Staleness or recomputation under the declaration. [V10 §7R]
- Must never: DESIGNED — Silently invent an invalidator or ignore an applicable declared one. [V10 §7R]
- Fails closed by: DESIGNED — An applicable declared invalidator prevents valid old-result reuse. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.3.4 — Context-bound reuse and invalidation | The actual declared invalidating event. | Applies the declared invalidation rule. | Cache validity stays explicit. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.3.5 — Mouth precomputation prerequisites
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Two simultaneous prerequisites for precomputing mouth-produced dimensions. [V10 §7R]
- Takes in: DESIGNED — Explicit context-configuration authorization and an independently designed validation mechanism for that specific mode. [V10 §7R]
- Does: DESIGNED — Permits such precomputation only when both exist. [V10 §7R]
- Gives out: DESIGNED — Only the explicitly declared and independently validated precomputation scope. [V10 §7R]
- Must never: DESIGNED — Treat ordinary mouth authorization alone as precomputation permission. [V10 §7R]
- Fails closed by: DESIGNED — Does not precompute a mouth dimension when either prerequisite is absent. [V10 §7R]

TOGETHER
- Fed by: DESIGNED — C-7R.4.1.7 — Tier 1 scoped mouth authorization: exact mouth scope; C-7R.6 — Mouth-produced dimension validation: the required validation design. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.3 — Evaluation timing | The two mouth-specific prerequisites. | Retains both before precomputation. | Optional timing never bypasses validation. | [V10 §7R] |
| 2 · DESIGNED | C-7R.3.2 — Declared triggered precomputation | The declared scope and designed independent validation. | Blocks unauthorized mouth precomputation. | Both conditions remain necessary. | [V10 §7R] |
| 3 · ACCEPTED | C-7R.16.7 — Future mouth-dimension declaration boundary | The two additional mouth-precomputation prerequisites. | Requires declared scope and a designed independent validation mechanism. | Future mouth use does not silently enable caching. | [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |

SUB-PARTS: NONE

### C-7R.4 — Two-tier configuration contract
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Shared Tier 1 and consumer-local Tier 2 with separate owners and validators. [V10 §7R]
- Takes in: DESIGNED — A versioned declared mode and the local settings that particular mode needs. [V10 §7R]
- Does: DESIGNED — Validates Tier 1 in relevance control; leaves Tier 2 content and validation with its consumer. [V10 §7R]
- Gives out: DESIGNED — A mode with an explicit shared contract and only its required local settings. [V10 §7R]
- Must never: DESIGNED — Silently take over the other tier or require all consumers’ complete Tier 2 designs before any particular mode can run. [V10 §7R]
- Fails closed by: DESIGNED — A specific mode requires valid Tier 1 and the consumer-validated local fields it actually needs. [V10 §7R]

TOGETHER
- Fed by: DESIGNED — C-7R.4.1 — Tier 1 shared required contract: shared minimum fields; C-7R.4.2 — Tier 2 component-local settings: local settings and versioning. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R — Attention & Relevance Control (§7R) | The shared/local contract. | Evaluates only the declared valid mode. | Ownership remains separate. | [V10 §7R] |
| 2 · DESIGNED | C-7R.1 — Two-layer relevance judgment | Declared gates and dimensions. | Applies only the mode’s named output contract. | No hidden relevance rule is substituted. | [V10 §7R] |
| 3 · DESIGNED | C-7R.2 — Per-dimension producer selection | Producer assignments. | Uses the producer declared for each dimension. | Producer selection remains auditable. | [V10 §7R] |
| 4 · DESIGNED | C-7R.3 — Evaluation timing | Declared evaluation timing. | Uses only on-demand or expressly enabled triggered timing. | Precomputation cannot enable itself. | [V10 §7R] |
| 5 · ACCEPTED | C-7R.15 — Mandatory per-task relevance declaration policy | The shared/local tier ownership contract. | Keeps Tier 1 with relevance control and Tier 2 with the consumer. | Neither owner silently validates the other’s content. | [V10 §7R] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |
| 6 · ACCEPTED | C-7R.15.3 — Declaration Selected relevance mode | The shared/local tier ownership contract. | Keeps Tier 1 with relevance control and Tier 2 with the consumer. | Neither owner silently validates the other’s content. | [V10 §7R] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |
| 7 · ACCEPTED | C-7R.16 — Accepted five-consumer relevance declarations | The shared/local tier ownership contract. | Keeps Tier 1 with relevance control and Tier 2 with the consumer. | Neither owner silently validates the other’s content. | [V10 §7R] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |

SUB-PARTS: C-7R.4.1 — Tier 1 shared required contract; C-7R.4.2 — Tier 2 component-local settings

### C-7R.4.1 — Tier 1 shared required contract
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The minimum shared declaration owned and validated by relevance control. [V10 §7R]
- Takes in: DESIGNED — The mode identity/version, purpose, consumer, object types, gates/producers, dimensions/producers, scoped mouth authorization, timing, conditional triggers and conditional unresolved-rule reference. [V10 §7R]
- Does: DESIGNED — Checks the required shared declaration without assuming ownership of local Tier 2 content. [V10 §7R]
- Gives out: DESIGNED — A validated shared mode contract or an invalid declaration. [V10 §7R]
- Must never: DESIGNED — Replace named mouth scope with a broad authorization flag or inspect the local uncertainty rule as if relevance control owned it. [V10 §7R]
- Fails closed by: DESIGNED — Does not accept a mode missing the applicable required declaration. [V10 §7R]

TOGETHER
- Fed by: DESIGNED — C-7R.4.1.1 — Tier 1 mode identity and version: identity/version; C-7R.9 — Tier 1 structured purpose: purpose form; C-7R.4.1.3 — Tier 1 consuming component: consumer; C-7R.4.1.4 — Tier 1 candidate and target object types: candidate/target types; C-7R.4.1.5 — Tier 1 gate conditions and producers: gates/producers; C-7R.4.1.6 — Tier 1 dimensions and producers: dimensions/producers; C-7R.4.1.7 — Tier 1 scoped mouth authorization: mouth scope; C-7R.4.1.8 — Tier 1 evaluation timing declaration: timing; C-7R.4.1.9 — Tier 1 precomputation triggers and invalidators: precomputation conditions; C-7R.10 — Tier-boundary unresolved-rule reference: conditional Tier-2 reference. [V10 §7R]
- Gated by: DESIGNED — C-7R.14 — Unrecognized purpose-type halt: unknown purpose prevents acceptance and evaluation. [V10 §7R]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.4 — Two-tier configuration contract | The complete shared declaration. | Validates its own tier. | Local settings remain consumer-owned. | [V10 §7R] |

SUB-PARTS: C-7R.4.1.1 — Tier 1 mode identity and version; C-7R.4.1.3 — Tier 1 consuming component; C-7R.4.1.4 — Tier 1 candidate and target object types; C-7R.4.1.5 — Tier 1 gate conditions and producers; C-7R.4.1.6 — Tier 1 dimensions and producers; C-7R.4.1.7 — Tier 1 scoped mouth authorization; C-7R.4.1.8 — Tier 1 evaluation timing declaration; C-7R.4.1.9 — Tier 1 precomputation triggers and invalidators

### C-7R.4.1.1 — Tier 1 mode identity and version
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — A stable mode identifier with a version. [V10 §7R]
- Takes in: DESIGNED — The identifier and version for this declaration. [V10 §7R]
- Does: DESIGNED — Identifies the exact shared configuration. [V10 §7R]
- Gives out: DESIGNED — An auditable mode/version pair. [V10 §7R]
- Must never: DESIGNED — Silently alter a version’s content. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.4.1.1.1 — Tier 1 stable mode identifier: identifier; C-7R.4.1.1.2 — Tier 1 mode version: version. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.4.1 — Tier 1 shared required contract | Stable mode identity and version. | Binds the evaluation to its declared configuration. | Versions remain distinguishable. | [V10 §7R] |
| 2 · DESIGNED | C-7R.12.2 — Evaluation mode identifier and version | The actual declared mode identifier and version. | Records the configuration used by the evaluation. | Later configuration changes cannot rewrite provenance. | [V10 §7R] |

SUB-PARTS: C-7R.4.1.1.1 — Tier 1 stable mode identifier; C-7R.4.1.1.2 — Tier 1 mode version

### C-7R.4.1.1.1 — Tier 1 stable mode identifier
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The stable identity of a relevance mode. [V10 §7R]
- Takes in: DESIGNED — The declared mode identifier. [V10 §7R]
- Does: DESIGNED — Retains which mode the contract describes. [V10 §7R]
- Gives out: DESIGNED — A stable mode reference. [V10 §7R]
- Must never: DESIGNED — Substitute another mode without an explicit declaration. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.4.1.1 — Tier 1 mode identity and version | The stable identifier. | Names the mode independently of its version. | Mode identity remains explicit. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.4.1.1.2 — Tier 1 mode version
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The version of the declared relevance mode. [V10 §7R]
- Takes in: DESIGNED — The specific configuration version used. [V10 §7R]
- Does: DESIGNED — Binds the shared declaration to that version. [V10 §7R]
- Gives out: DESIGNED — An explicit version reference. [V10 §7R]
- Must never: DESIGNED — Overwrite an earlier mode version. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.4.1.1 — Tier 1 mode identity and version | The version. | Distinguishes successive configurations. | Historical configuration remains inspectable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.4.1.3 — Tier 1 consuming component
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The declared component using the relevance mode. [V10 §7R]
- Takes in: DESIGNED — The consuming component identity. [V10 §7R]
- Does: DESIGNED — Preserves the owner of local settings and use. [V10 §7R]
- Gives out: DESIGNED — A named consumer. [V10 §7R]
- Must never: DESIGNED — Silently transfer Tier 2 ownership to relevance control. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.4.1 — Tier 1 shared required contract | The declared consumer. | Identifies the local-setting owner. | Shared validation does not take over local use. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.4.1.4 — Tier 1 candidate and target object types
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The declared types of candidates and targets. [V10 §7R]
- Takes in: DESIGNED — The candidate and target object-type declarations. [V10 §7R]
- Does: DESIGNED — States what kind of objects this mode evaluates and against what. [V10 §7R]
- Gives out: DESIGNED — An explicit candidate/target type boundary. [V10 §7R]
- Must never: DESIGNED — Use an undeclared type as if it belonged to the mode. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.4.1.4.1 — Tier 1 candidate object types: candidate type; C-7R.4.1.4.2 — Tier 1 target object types: target type. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.4.1 — Tier 1 shared required contract | Candidate and target types. | Keeps the evaluation inside its declared object scope. | Types are auditable. | [V10 §7R] |

SUB-PARTS: C-7R.4.1.4.1 — Tier 1 candidate object types; C-7R.4.1.4.2 — Tier 1 target object types

### C-7R.4.1.4.1 — Tier 1 candidate object types
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The object types declared as candidates for a mode. [V10 §7R]
- Takes in: DESIGNED — The candidate-type declaration. [V10 §7R]
- Does: DESIGNED — Preserves eligible candidate types. [V10 §7R]
- Gives out: DESIGNED — Explicit candidate types. [V10 §7R]
- Must never: DESIGNED — Silently add another candidate type. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.4.1.4 — Tier 1 candidate and target object types | The candidate types. | Retains the evaluated-object scope. | Candidate eligibility remains declared. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.4.1.4.2 — Tier 1 target object types
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The object types declared as targets for a mode. [V10 §7R]
- Takes in: DESIGNED — The target-type declaration. [V10 §7R]
- Does: DESIGNED — Preserves eligible target types. [V10 §7R]
- Gives out: DESIGNED — Explicit target types. [V10 §7R]
- Must never: DESIGNED — Silently substitute another target type. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.4.1.4 — Tier 1 candidate and target object types | The target types. | Retains the comparison-object scope. | Target scope remains declared. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.4.1.5 — Tier 1 gate conditions and producers
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The named context gates and the producer assigned to each. [V10 §7R]
- Takes in: DESIGNED — Each declared categorical condition and its deterministic rule producer. [V10 §7R]
- Does: DESIGNED — Records gate meaning and production individually. [V10 §7R]
- Gives out: DESIGNED — Named, producer-bound boolean conditions. [V10 §7R]
- Must never: DESIGNED — Use a mouth-produced interpretation as a categorical gate. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.7.1 — Shared deterministic gate vocabulary: shared gate vocabulary. [V10 §7R]
- Gated by: DESIGNED — C-7R.6.4 — Mouth dimensions cannot be categorical gates: the deterministic-gate boundary. [V10 §7R]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.4.1 — Tier 1 shared required contract | Each gate and its assigned producer. | Validates an explicit categorical contract. | No undeclared gate appears. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.4.1.6 — Tier 1 dimensions and producers
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The named graded dimensions with an assigned producer for each. [V10 §7R]
- Takes in: DESIGNED — Each dimension declaration and producer. [V10 §7R]
- Does: DESIGNED — Retains the separate dimension/producer assignments. [V10 §7R]
- Gives out: DESIGNED — A named graded-output contract. [V10 §7R]
- Must never: DESIGNED — Use an undeclared dimension or obscure several dimensions in one score. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.7.2 — Shared named dimension vocabulary: shared graded vocabulary; C-7R.2 — Per-dimension producer selection: producer-selection rules. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.4.1 — Tier 1 shared required contract | Each dimension/producer pair. | Validates the declared graded output. | Every value has a named role. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.4.1.7 — Tier 1 scoped mouth authorization
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Authorization limited to specific named interpretive dimensions and contexts. [V10 §7R]
- Takes in: DESIGNED — The exact named dimensions and contexts where mouth production is declared. [V10 §7R]
- Does: DESIGNED — Keeps authorization scoped to those declarations. [V10 §7R]
- Gives out: DESIGNED — A bounded mouth-use declaration, or no declared mouth dimensions. [V10 §7R]
- Must never: DESIGNED — Replace scope with one broad authorization flag or require separate approval for each authorized call. [V10 §7R]
- Fails closed by: DESIGNED — Provides no mouth authority outside the declared dimensions and contexts. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.4.1 — Tier 1 shared required contract | The exact mouth scope. | Validates explicit authorization within the mode. | Mouth use stays bounded. | [V10 §7R] |
| 2 · DESIGNED | C-7R.2.3 — Declared interpretive mouth producer | Named dimensions and contexts. | Uses the mouth only within that scope. | A broad model capability is not authority. | [V10 §7R] |
| 3 · DESIGNED | C-7R.3.5 — Mouth precomputation prerequisites | The explicit precomputation scope. | Requires the declared context before mouth precomputation. | Ordinary mouth availability does not enable precomputation. | [V10 §7R] |
| 4 · ACCEPTED | C-7R.16.7 — Future mouth-dimension declaration boundary | The exact future mouth dimension/context scope. | Requires explicit named authorization. | Current mouth-free declarations grant no mouth role. | [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |

SUB-PARTS: NONE

### C-7R.4.1.8 — Tier 1 evaluation timing declaration
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Whether the mode runs on demand or allows triggered precomputation. [V10 §7R]
- Takes in: DESIGNED — The mode’s declared timing. [V10 §7R]
- Does: DESIGNED — Preserves the enabled evaluation form. [V10 §7R]
- Gives out: DESIGNED — An explicit timing declaration. [V10 §7R]
- Must never: DESIGNED — Turn optional precomputation into a global default. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.4.1 — Tier 1 shared required contract | The declared timing. | Checks the mode’s permitted evaluation form. | Timing cannot change silently. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.4.1.9 — Tier 1 precomputation triggers and invalidators
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Declared triggers and invalidating events when precomputation is enabled. [V10 §7R]
- Takes in: DESIGNED — The specific triggering and invalidating events for that context. [V10 §7R]
- Does: DESIGNED — Retains when to compute and when a result ceases to be reusable. [V10 §7R]
- Gives out: DESIGNED — The conditional precomputation contract. [V10 §7R]
- Must never: DESIGNED — Enable cached reuse without its declared invalidation conditions. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.3.4 — Context-bound reuse and invalidation: context and validity reuse rules. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.4.1 — Tier 1 shared required contract | Triggers and invalidators for an enabled precomputation mode. | Validates the conditional timing contract. | Cache validity remains explicit. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.4.2 — Tier 2 component-local settings
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Local settings owned and validated by the consuming component. [V10 §7R]
- Takes in: DESIGNED — The component-specific thresholds, ordering or weighting, fallback, surfacing, unresolved-dimension handling and other local settings needed by this mode. [V10 §7R]
- Does: DESIGNED — Uses only the local fields this particular mode needs; later additions produce a new configuration version. [V10 §7R]
- Gives out: DESIGNED — Consumer-validated local behavior under a versioned configuration. [V10 §7R]
- Must never: DESIGNED — Make relevance control own or validate Tier 2 content, or wait for every consumer’s complete Tier 2 design before running a sufficiently declared mode. [V10 §7R]
- Fails closed by: DESIGNED — A mode lacks its required local contract until its consuming component validates the fields that mode needs. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7R.5.4 — Reusable mode change: reusable configuration changes use preview, confirmation and a new version. [V10 §7R]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.4 — Two-tier configuration contract | The consumer-validated required local settings. | Keeps shared and local ownership separate. | Later additions remain versioned. | [V10 §7R] |
| 2 · DESIGNED | C-7R.7.2.2 — temporal_distance | The consumer’s local normalization, scaling and thresholds. | Leaves those transformations outside the raw shared dimension. | Raw distance and local use remain separate. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.5 — Ness inspection, correction and configuration changes
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The distinct direct judgment-level actions and governed reusable changes. [V10 §7R]
- Takes in: DESIGNED — A judgment to inspect or correct, a contextual override, or a requested reusable configuration change. [V10 §7R]
- Does: DESIGNED — Preserves direct inspection/correction/override while requiring consequence preview and confirmation for permanent mode changes. [V10 §7R]
- Gives out: DESIGNED — Inspectable judgments, separate linked responses, separate scoped overrides and new configuration versions. [V10 §7R]
- Must never: DESIGNED — Rewrite originals, silently propagate a contextual override, veto a confirmed valid mode choice, or delete earlier versions. [V10 §7R]
- Fails closed by: DESIGNED — Without that confirmation, the configuration stays as it was; inspection, per-judgment correction and contextual overrides still apply directly. [V10 §7R]

TOGETHER
- Fed by: DESIGNED — C-7R.5.1 — Full relevance inspection: inspection; C-7R.5.2 — Direct per-judgment correction: correction; C-7R.5.3 — Context-scoped per-judgment override: override; C-7R.5.4 — Reusable mode change: reusable change; C-7R.5.5 — Invalid configuration request handling: invalid request; C-7R.5.6 — Append-only relevance change history: append-only preservation. [V10 §7R]
- Gated by: DESIGNED — A reusable configuration change takes effect only after its consequence preview and Ness's confirmation. [V10 §7R]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R — Attention & Relevance Control (§7R) | The appropriate judgment or mode-change path. | Keeps contextual responses separate from permanent policy. | Ness remains the decider. | [V10 §7R] |
| 2 · ACCEPTED | C-7R.15.7 — Declaration Logging / audit requirement | Inspection, direct correction, scoped override and versioned permanent change. | Keeps those paths available without making inspection a routine operational gate. | The audit record remains append-only. | [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] |

SUB-PARTS: C-7R.5.1 — Full relevance inspection; C-7R.5.2 — Direct per-judgment correction; C-7R.5.3 — Context-scoped per-judgment override; C-7R.5.4 — Reusable mode change; C-7R.5.5 — Invalid configuration request handling; C-7R.5.6 — Append-only relevance change history

### C-7R.5.1 — Full relevance inspection
Stamp: DESIGNED    Source: [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]

ALONE
- What it is: DESIGNED — Always-available, unrestricted Ness inspection of a relevance judgment and its configuration. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Takes in: DESIGNED — The judgment’s gate results, graded dimensions, producer provenance, mode identifier/version and full Tier 1/Tier 2 configuration. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Does: DESIGNED — Makes the full production and configuration account inspectable; existing privacy/access rules still govern the records themselves. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Gives out: DESIGNED — The complete relevance account, not merely a confidence label. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Must never: DESIGNED — Hide a dimension, provenance or tier configuration behind a summary; turn inspection into routine per-judgment approval.  [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): record protection remains applicable; C-SACL — Speaker Access-Control Layer (§25.4): applicable visible inspection follows the privacy-first output order. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.5 — Ness inspection, correction and configuration changes | The full judgment and both tiers. | Supports inspection without a mode-change procedure. | Transparency creates no new disclosure route. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.5.2 — Direct per-judgment correction
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — A lightweight Ness response that a specific judgment is wrong, too high, too low or misdirected. [V10 §7R]
- Takes in: DESIGNED — The specific judgment and Ness’s correction. [V10 §7R]
- Does: DESIGNED — Appends a separate linked Ness response event without proposal and confirmation. [V10 §7R]
- Gives out: DESIGNED — The original judgment and separate correction coexisting. [V10 §7R]
- Must never: DESIGNED — Rewrite the original or require a permanent-mode proposal for a local correction. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.5 — Ness inspection, correction and configuration changes | The direct correction event. | Preserves the correction beside the judgment. | Original and response remain distinct. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.5.3 — Context-scoped per-judgment override
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — A direct override of how one judgment is used in the current context. [V10 §7R]
- Takes in: DESIGNED — The judgment, the current context and Ness’s override. [V10 §7R]
- Does: DESIGNED — Explicitly scopes and records the override as its own event. [V10 §7R]
- Gives out: DESIGNED — A separate contextual override. [V10 §7R]
- Must never: DESIGNED — Silently propagate the override into a permanent mode change. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.5 — Ness inspection, correction and configuration changes | The explicitly scoped override. | Changes only the current judgment use. | Reusable configuration remains unchanged. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.5.4 — Reusable mode change
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The consequence-preview and Ness-confirmation path for reusable mode or configuration changes. [V10 §7R]
- Takes in: DESIGNED — A proposed change and the gates, dimensions, consumers, precomputed results and other mode versions it would affect. [V10 §7R]
- Does: DESIGNED — Shows all affected consequences, receives Ness’s confirmation, creates a new configuration version and retains the prior version. [V10 §7R]
- Gives out: DESIGNED — A confirmed new version with unchanged prior history. [V10 §7R]
- Must never: DESIGNED — Use the proposal step to veto Ness’s confirmed valid decision, silently commit a change or overwrite the old version. [V10 §7R]
- Fails closed by: DESIGNED — Does not commit the reusable change without Ness’s confirmation; invalid configurations follow the exact-conflict path. [V10 §7R]

TOGETHER
- Fed by: DESIGNED — C-7R.5.4.1 — Mode-change consequence preview: consequence preview; C-7R.5.4.2 — New configuration version preservation: new-version preservation. [V10 §7R]
- Gated by: DESIGNED — Ness’s confirmation after the consequence preview is required; C-7R.5.5 — Invalid configuration request handling: technical or protected-boundary invalidity must be identified and translated into a valid proposal. [V10 §7R]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.5 — Ness inspection, correction and configuration changes | A confirmed reusable change. | Creates a new configuration version. | The old version remains available. | [V10 §7R] |
| 2 · DESIGNED | C-7R.4.2 — Tier 2 component-local settings | The confirmed versioned local change. | Adds or changes reusable local settings by new version. | Tier 2 history remains intact. | [V10 §7R] |
| 3 · DESIGNED | C-7R.13 — Per-judgment override pattern observation | The permanent-mode consequence-preview and confirmation path. | Does not apply an observed pattern as an automatic configuration change. | Only an explicitly confirmed new version changes reusable policy. | [V10 §7R] |
| 4 · DESIGNED | C-7R.14.6 — New-purpose proposal path | The confirmed versioned vocabulary-change path. | Adds a controlled purpose only after preview and confirmation. | A label or close match cannot create a new purpose. | [V10 §7R] |
| 5 · DESIGNED | C-7R.9.4 — Controlled-purpose vocabulary change | The confirmed versioned vocabulary-change path. | Adds a controlled purpose only after preview and confirmation. | A label or close match cannot create a new purpose. | [V10 §7R] |
| 6 · ACCEPTED | C-7R.16 — Accepted five-consumer relevance declarations | The permanent configuration-change path. | Requires a confirmed new declaration version and preserves the prior version. | Accepted current declarations cannot change silently. | [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| 7 · ACCEPTED | C-7R.16.7 — Future mouth-dimension declaration boundary | The permanent configuration-change path. | Requires a confirmed new declaration version and preserves the prior version. | Accepted current declarations cannot change silently. | [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| 8 · DESIGNED | C-7R.7.4 — Local dimension and shared-vocabulary extension | The proposal/confirmation/versioning process. | Promotes a local dimension to shared vocabulary only through that process. | Cross-component use alone does not change shared policy. | [V10 §7R] |

SUB-PARTS: C-7R.5.4.1 — Mode-change consequence preview; C-7R.5.4.2 — New configuration version preservation

### C-7R.5.4.1 — Mode-change consequence preview
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The required account of what a reusable change would affect. [V10 §7R]
- Takes in: DESIGNED — Affected gate conditions, graded dimensions, consuming components, precomputed results and other mode versions. [V10 §7R]
- Does: DESIGNED — Surfaces all five consequence groups before commitment. [V10 §7R]
- Gives out: DESIGNED — An inspectable preview of the change’s reach. [V10 §7R]
- Must never: DESIGNED — Hide consequences or use the preview as a veto. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.5.4.1.1 — Preview affected gate conditions: gates; C-7R.5.4.1.2 — Preview affected graded dimensions: dimensions; C-7R.5.4.1.3 — Preview affected consuming components: consumers; C-7R.5.4.1.4 — Preview affected precomputed results: precomputed results; C-7R.5.4.1.5 — Preview affected other mode versions: other mode versions. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.5.4 — Reusable mode change | The five affected-consequence groups. | Presents them before confirmation. | Ness can confirm the actual change. | [V10 §7R] |

SUB-PARTS: C-7R.5.4.1.1 — Preview affected gate conditions; C-7R.5.4.1.2 — Preview affected graded dimensions; C-7R.5.4.1.3 — Preview affected consuming components; C-7R.5.4.1.4 — Preview affected precomputed results; C-7R.5.4.1.5 — Preview affected other mode versions

### C-7R.5.4.1.1 — Preview affected gate conditions
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The gates affected by a proposed reusable change. [V10 §7R]
- Takes in: DESIGNED — The specific affected gate conditions. [V10 §7R]
- Does: DESIGNED — Shows which gates would change or be touched. [V10 §7R]
- Gives out: DESIGNED — An explicit gate-consequence account. [V10 §7R]
- Must never: DESIGNED — Hide affected categorical conditions. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.5.4.1 — Mode-change consequence preview | The affected gates. | Includes their consequences before confirmation. | Categorical effects remain visible. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.5.4.1.2 — Preview affected graded dimensions
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The dimensions affected by the proposed change. [V10 §7R]
- Takes in: DESIGNED — The affected named dimensions. [V10 §7R]
- Does: DESIGNED — Shows which dimensions would be touched. [V10 §7R]
- Gives out: DESIGNED — An explicit dimension-consequence account. [V10 §7R]
- Must never: DESIGNED — Conceal a change behind a hidden score. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.5.4.1 — Mode-change consequence preview | The affected dimensions. | Includes their consequences in the preview. | Graded effects remain inspectable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.5.4.1.3 — Preview affected consuming components
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The consumers touched by the proposed reusable change. [V10 §7R]
- Takes in: DESIGNED — The affected component identities. [V10 §7R]
- Does: DESIGNED — Shows which components would be affected. [V10 §7R]
- Gives out: DESIGNED — An explicit consumer-consequence account. [V10 §7R]
- Must never: DESIGNED — Silently extend the change to another consumer. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.5.4.1 — Mode-change consequence preview | The affected consumers. | Shows the change’s component reach. | Cross-component effects are visible before confirmation. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.5.4.1.4 — Preview affected precomputed results
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The precomputed results touched by the proposed change. [V10 §7R]
- Takes in: DESIGNED — The affected cached/precomputed judgments. [V10 §7R]
- Does: DESIGNED — Shows the consequences for those results. [V10 §7R]
- Gives out: DESIGNED — An explicit precomputation-consequence account. [V10 §7R]
- Must never: DESIGNED — Leave affected cached results out of the preview. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.5.4.1 — Mode-change consequence preview | The affected precomputed results. | Includes their consequences. | Cache effects cannot remain hidden. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.5.4.1.5 — Preview affected other mode versions
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Other mode versions touched by the proposed change. [V10 §7R]
- Takes in: DESIGNED — The affected mode/version references. [V10 §7R]
- Does: DESIGNED — Shows the version-level consequences. [V10 §7R]
- Gives out: DESIGNED — An explicit affected-version account. [V10 §7R]
- Must never: DESIGNED — Overwrite prior versions or hide cross-version effects. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.5.4.1 — Mode-change consequence preview | The affected other versions. | Includes them in the consequence preview. | Version reach remains explicit. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.5.4.2 — New configuration version preservation
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The append-only result of a confirmed reusable change. [V10 §7R]
- Takes in: DESIGNED — The confirmed configuration and prior version. [V10 §7R]
- Does: DESIGNED — Creates a new version while retaining the prior one unchanged. [V10 §7R]
- Gives out: DESIGNED — Distinct new and prior configurations. [V10 §7R]
- Must never: DESIGNED — Overwrite or delete the prior version. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.5.4 — Reusable mode change | The confirmed versioned configuration. | Commits a new historical version. | Earlier decisions remain inspectable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.5.5 — Invalid configuration request handling
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The handling of a technically invalid request or one that violates a protected architectural boundary. [V10 §7R]
- Takes in: DESIGNED — Ness’s original request and the precise technical or architectural conflict. [V10 §7R]
- Does: DESIGNED — Identifies the exact conflict, preserves the original request and helps translate the intended change into a valid proposed configuration. [V10 §7R]
- Gives out: DESIGNED — A plain exact-conflict explanation and a valid proposal path without erasing the request. [V10 §7R]
- Must never: DESIGNED — Silently apply invalid configuration or dismiss the request without explanation. [V10 §7R]
- Fails closed by: DESIGNED — Withholds the invalid configuration while preserving and explaining the request. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.5 — Ness inspection, correction and configuration changes | The exact conflict and preserved request. | Keeps invalidity distinct from a discretionary veto. | The intended change receives an explained valid path. | [V10 §7R] |
| 2 · DESIGNED | C-7R.5.4 — Reusable mode change | A precise invalidity finding. | Does not commit an invalid mode. | The original request survives unchanged. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.5.6 — Append-only relevance change history
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Preservation of original judgments, corrections, overrides and mode versions. [V10 §7R]
- Takes in: DESIGNED — The original object and any later response or configuration change. [V10 §7R]
- Does: DESIGNED — Keeps corrections as linked events, overrides as separate scoped events and new modes as new versions. [V10 §7R]
- Gives out: DESIGNED — Coexisting original and later records. [V10 §7R]
- Must never: DESIGNED — Rewrite a relevance judgment or delete an earlier mode version. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.5 — Ness inspection, correction and configuration changes | The separate historical objects. | Preserves every stage without rewriting. | A later correction does not erase its origin. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.6 — Mouth-produced dimension validation
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Required deterministic validation of every mouth-produced relevance dimension, with optional declared independent model validation. [V10 §7R]
- Takes in: DESIGNED — The produced value, declared schema/bounds, provenance, candidate, target, context and permitted inputs. [V10 §7R]
- Does: DESIGNED — Runs all six deterministic checks and records the appropriate outcome; an optional model validator adds its own provenance and disagreement handling. [V10 §7R]
- Gives out: DESIGNED — Validated, Failed or Unresolved, with any separate model disagreement record. [V10 §7R]
- Must never: DESIGNED — Treat validation as substantive truth, self-approve a mouth result, use confidence to settle disagreement, or grant a second model final authority. [V10 §7R]
- Fails closed by: DESIGNED — Failed values are not validated; structurally grounded but independently unverified interpretation remains Unresolved. [V10 §7R]

TOGETHER
- Fed by: DESIGNED — C-7R.6.1 — Six deterministic validation checks: six required checks; C-7R.6.2 — Three mouth validation outcomes: three outcomes; C-7R.6.3 — Optional declared model-based validation: optional model validation; C-7R.6.4 — Mouth dimensions cannot be categorical gates: categorical-gate prohibition. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R — Attention & Relevance Control (§7R) | The validation state and disagreement provenance. | Keeps interpretation uncertainty explicit. | Validation never establishes truth. | [V10 §7R] |
| 2 · DESIGNED | C-7R.2 — Per-dimension producer selection | Required validation for mouth production. | Does not allow the producer to approve itself. | Every mouth value retains the boundary. | [V10 §7R] |
| 3 · DESIGNED | C-7R.2.3 — Declared interpretive mouth producer | The required checks and resulting state. | Submits the scoped interpretation to validation. | A generated value is not self-approved. | [V10 §7R] |
| 4 · DESIGNED | C-7R.3.5 — Mouth precomputation prerequisites | The validation mechanism designed for the mode. | Requires it before mouth precomputation. | Timing cannot bypass validation. | [V10 §7R] |
| 5 · ACCEPTED | C-7R.15.5 — Declaration Uncertainty behavior | Six deterministic checks, three outcomes and the optional independent-validator boundary. | Preserves validation and uncertainty without making a second AI mandatory. | A generated interpretation never self-approves. | [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.4] |
| 6 · ACCEPTED | C-7R.16.7 — Future mouth-dimension declaration boundary | Six deterministic checks, three outcomes and the optional independent-validator boundary. | Preserves validation and uncertainty without making a second AI mandatory. | A generated interpretation never self-approves. | [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.4] |

SUB-PARTS: C-7R.6.1 — Six deterministic validation checks; C-7R.6.2 — Three mouth validation outcomes; C-7R.6.3 — Optional declared model-based validation; C-7R.6.4 — Mouth dimensions cannot be categorical gates

### C-7R.6.1 — Six deterministic validation checks
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The mandatory structural and grounding checks for each mouth dimension. [V10 §7R]
- Takes in: DESIGNED — Its schema/bounds, provenance, candidate/target/context and declared inputs. [V10 §7R]
- Does: DESIGNED — Checks all six predicates rather than model confidence. [V10 §7R]
- Gives out: DESIGNED — The deterministic check results used to assign a validation outcome. [V10 §7R]
- Must never: DESIGNED — Skip a check because a model sounds certain. [V10 §7R]
- Fails closed by: DESIGNED — A structural or grounding defect yields Failed; remaining unverifiable interpretation can remain Unresolved. [V10 §7R]

TOGETHER
- Fed by: DESIGNED — C-7R.6.1.1 — Schema and bounds validation: schema/bounds; C-7R.6.1.2 — Required provenance validation: provenance; C-7R.6.1.3 — Declared grounding check: grounding; C-7R.6.1.4 — Out-of-scope detection: input scope; C-7R.6.1.5 — Direct structural contradiction check: structural contradiction; C-7R.6.1.6 — Grounding-relative certainty check: certainty. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6 — Mouth-produced dimension validation | All six check results. | Assigns an honest validation outcome. | Confidence cannot substitute for checks. | [V10 §7R] |

SUB-PARTS: C-7R.6.1.1 — Schema and bounds validation; C-7R.6.1.2 — Required provenance validation; C-7R.6.1.3 — Declared grounding check; C-7R.6.1.4 — Out-of-scope detection; C-7R.6.1.5 — Direct structural contradiction check; C-7R.6.1.6 — Grounding-relative certainty check

### C-7R.6.1.1 — Schema and bounds validation
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The value-presence, type and declared-bounds check. [V10 §7R]
- Takes in: DESIGNED — The produced value and declared schema/bounds. [V10 §7R]
- Does: DESIGNED — Checks that the value is present, has the correct type and lies within declared bounds. [V10 §7R]
- Gives out: DESIGNED — A schema/bounds check result. [V10 §7R]
- Must never: DESIGNED — Accept missing, mistyped or out-of-bounds values. [V10 §7R]
- Fails closed by: DESIGNED — Such defects prevent a Validated outcome. [V10 §7R]

TOGETHER
- Fed by: DESIGNED — C-7R.6.1.1.1 — Validation value present: present value; C-7R.6.1.1.2 — Validation value correct type: correct type; C-7R.6.1.1.3 — Validation value within declared bounds: declared bounds. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.1 — Six deterministic validation checks | Presence, type and bounds results. | Includes the schema check in required validation. | Invalid structure is detectable. | [V10 §7R] |

SUB-PARTS: C-7R.6.1.1.1 — Validation value present; C-7R.6.1.1.2 — Validation value correct type; C-7R.6.1.1.3 — Validation value within declared bounds

### C-7R.6.1.1.1 — Validation value present
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The value-presence predicate. [V10 §7R]
- Takes in: DESIGNED — The produced dimension field. [V10 §7R]
- Does: DESIGNED — Checks that a value is present. [V10 §7R]
- Gives out: DESIGNED — A presence check result. [V10 §7R]
- Must never: DESIGNED — Treat a missing value as a populated dimension. [V10 §7R]
- Fails closed by: DESIGNED — Missing value fails the required structural check. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.1.1 — Schema and bounds validation | Whether the value is present. | Includes presence in schema validation. | Absence cannot pass as a value. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.6.1.1.2 — Validation value correct type
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The declared-type predicate. [V10 §7R]
- Takes in: DESIGNED — The value and its required type. [V10 §7R]
- Does: DESIGNED — Checks the actual value type. [V10 §7R]
- Gives out: DESIGNED — A type check result. [V10 §7R]
- Must never: DESIGNED — Accept the wrong type as valid structure. [V10 §7R]
- Fails closed by: DESIGNED — Wrong type fails the required structural check. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.1.1 — Schema and bounds validation | Whether the value has the required type. | Includes type in schema validation. | Structural validity remains explicit. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.6.1.1.3 — Validation value within declared bounds
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The declared-bounds predicate. [V10 §7R]
- Takes in: DESIGNED — The value and its declared bounds. [V10 §7R]
- Does: DESIGNED — Checks that the value lies inside those bounds. [V10 §7R]
- Gives out: DESIGNED — A bounds check result. [V10 §7R]
- Must never: DESIGNED — Silently widen the declared range. [V10 §7R]
- Fails closed by: DESIGNED — Out-of-bounds values fail the required check. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.1.1 — Schema and bounds validation | Whether the value lies within declared bounds. | Includes bounds in validation. | A mode cannot silently expand its value range. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.6.1.2 — Required provenance validation
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The check that all required provenance fields are present and populated. [V10 §7R]
- Takes in: DESIGNED — The dimension’s required provenance. [V10 §7R]
- Does: DESIGNED — Checks both presence and populated content. [V10 §7R]
- Gives out: DESIGNED — A provenance-completeness result. [V10 §7R]
- Must never: DESIGNED — Treat empty provenance as complete. [V10 §7R]
- Fails closed by: DESIGNED — Missing required provenance prevents a Validated outcome. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.1 — Six deterministic validation checks | Required provenance completeness. | Rejects missing or empty provenance. | Untraceable output cannot pass. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.6.1.3 — Declared grounding check
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Traceability to the declared candidate, target and context. [V10 §7R]
- Takes in: DESIGNED — The value and its declared grounding references. [V10 §7R]
- Does: DESIGNED — Checks that the value is traceable to those inputs. [V10 §7R]
- Gives out: DESIGNED — A grounding result. [V10 §7R]
- Must never: DESIGNED — Treat an invented grounding claim as support. [V10 §7R]
- Fails closed by: DESIGNED — Untraceable or invented grounding prevents a Validated outcome. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.1 — Six deterministic validation checks | Candidate/target/context traceability. | Checks the result against its actual task. | A value cannot float free of its inputs. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.6.1.4 — Out-of-scope detection
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The check against reliance on undeclared inputs. [V10 §7R]
- Takes in: DESIGNED — The value’s supporting material and the declared input scope. [V10 §7R]
- Does: DESIGNED — Detects material outside that scope. [V10 §7R]
- Gives out: DESIGNED — A scoped-input check result. [V10 §7R]
- Must never: DESIGNED — Permit undeclared material to ground the value. [V10 §7R]
- Fails closed by: DESIGNED — Reliance on undeclared inputs yields Failed. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.1 — Six deterministic validation checks | Whether all relied-on material is declared. | Detects scope escape. | Undeclared input cannot pass as grounding. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.6.1.5 — Direct structural contradiction check
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The check against contradiction of directly verifiable structural facts. [V10 §7R]
- Takes in: DESIGNED — The produced value and directly verifiable structural facts. [V10 §7R]
- Does: DESIGNED — Detects structural contradiction without deciding interpretive truth. [V10 §7R]
- Gives out: DESIGNED — A structural-consistency result. [V10 §7R]
- Must never: DESIGNED — Use this check to decide which interpretive side of a clash is true. [V10 §7R]
- Fails closed by: DESIGNED — A directly verifiable contradiction yields Failed. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.1 — Six deterministic validation checks | Structural consistency. | Detects rule-verifiable contradiction. | Interpretive authority is not created. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.6.1.6 — Grounding-relative certainty check
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The check that claimed strength or certainty does not exceed grounding. [V10 §7R]
- Takes in: DESIGNED — The value’s claim of strength/certainty and its support. [V10 §7R]
- Does: DESIGNED — Detects stronger claims than the grounding supports. [V10 §7R]
- Gives out: DESIGNED — A certainty-versus-support result. [V10 §7R]
- Must never: DESIGNED — Treat model confidence as extra evidence. [V10 §7R]
- Fails closed by: DESIGNED — Unsupported certainty prevents a Validated outcome. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.1 — Six deterministic validation checks | Claimed certainty relative to support. | Checks for overstatement. | Confidence cannot expand grounding. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.6.2 — Three mouth validation outcomes
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The three settled validation outcomes. [V10 §7R]
- Takes in: DESIGNED — The required check results and whether interpretive correctness can be independently established deterministically. [V10 §7R]
- Does: DESIGNED — Distinguishes no rule-detectable error, actual failure and grounded but unresolved interpretation. [V10 §7R]
- Gives out: DESIGNED — Validated, Failed or Unresolved. [V10 §7R]
- Must never: DESIGNED — Equate Validated with substantive correctness or silently convert Unresolved to certainty. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.6.2.1 — Validated relevance dimension: Validated; C-7R.6.2.2 — Failed relevance dimension: Failed; C-7R.6.2.3 — Unresolved relevance dimension: Unresolved. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6 — Mouth-produced dimension validation | The exact validation outcome. | Returns its stated limited meaning. | The outcome does not grant truth or authority. | [V10 §7R] |

SUB-PARTS: C-7R.6.2.1 — Validated relevance dimension; C-7R.6.2.2 — Failed relevance dimension; C-7R.6.2.3 — Unresolved relevance dimension

### C-7R.6.2.1 — Validated relevance dimension
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The outcome when a value is structurally valid and grounded and all deterministic checks pass. [V10 §7R]
- Takes in: DESIGNED — The passing deterministic check results. [V10 §7R]
- Does: DESIGNED — States only that no rule-detectable error was found. [V10 §7R]
- Gives out: DESIGNED — Validated. [V10 §7R]
- Must never: DESIGNED — Claim the interpretation is substantively correct. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.2 — Three mouth validation outcomes | A structurally valid grounded value with all checks passed. | Labels it Validated within that limit. | Interpretive truth remains unestablished. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.6.2.2 — Failed relevance dimension
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The outcome for invented, structurally invalid, contradictory, out-of-bounds, provenance-missing or undeclared-input-dependent values. [V10 §7R]
- Takes in: DESIGNED — Any of the six stated defect classes. [V10 §7R]
- Does: DESIGNED — Preserves the failure rather than a usable validated value. [V10 §7R]
- Gives out: DESIGNED — Failed. [V10 §7R]
- Must never: DESIGNED — Conceal the defect or call the evaluation valid. [V10 §7R]
- Fails closed by: DESIGNED — Does not treat the failed value as validated. [V10 §7R]

TOGETHER
- Fed by: DESIGNED — C-7R.6.2.2.1 — Invented dimension failure: invented; C-7R.6.2.2.2 — Structurally invalid dimension failure: structurally invalid; C-7R.6.2.2.3 — Contradictory dimension failure: contradictory; C-7R.6.2.2.4 — Out-of-bounds dimension failure: outside bounds; C-7R.6.2.2.5 — Missing-provenance dimension failure: missing provenance; C-7R.6.2.2.6 — Undeclared-input dimension failure: undeclared inputs. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.2 — Three mouth validation outcomes | A detected failure class. | Retains Failed and its reason. | Failure is not smoothed into a score. | [V10 §7R] |

SUB-PARTS: C-7R.6.2.2.1 — Invented dimension failure; C-7R.6.2.2.2 — Structurally invalid dimension failure; C-7R.6.2.2.3 — Contradictory dimension failure; C-7R.6.2.2.4 — Out-of-bounds dimension failure; C-7R.6.2.2.5 — Missing-provenance dimension failure; C-7R.6.2.2.6 — Undeclared-input dimension failure

### C-7R.6.2.2.1 — Invented dimension failure
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Failure for an invented dimension value. [V10 §7R]
- Takes in: DESIGNED — The detected invention. [V10 §7R]
- Does: DESIGNED — Assigns Failed to that value. [V10 §7R]
- Gives out: DESIGNED — Failed with the invention retained as the reason. [V10 §7R]
- Must never: DESIGNED — Treat invention as grounded interpretation. [V10 §7R]
- Fails closed by: DESIGNED — The invented value does not become validated. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.2.2 — Failed relevance dimension | An invented result. | Keeps the Failed outcome. | Invention cannot be smoothed into relevance. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.6.2.2.2 — Structurally invalid dimension failure
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Failure for invalid result structure. [V10 §7R]
- Takes in: DESIGNED — The detected structural defect. [V10 §7R]
- Does: DESIGNED — Assigns Failed. [V10 §7R]
- Gives out: DESIGNED — Failed with the structural defect. [V10 §7R]
- Must never: DESIGNED — Treat malformed output as validated. [V10 §7R]
- Fails closed by: DESIGNED — The invalid value cannot pass required validation. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.2.2 — Failed relevance dimension | A structurally invalid result. | Keeps the Failed outcome. | Malformed output is not accepted silently. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.6.2.2.3 — Contradictory dimension failure
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Failure for a rule-detectable contradiction. [V10 §7R]
- Takes in: DESIGNED — The directly verifiable contradiction. [V10 §7R]
- Does: DESIGNED — Assigns Failed without deciding interpretive truth. [V10 §7R]
- Gives out: DESIGNED — Failed with the contradiction recorded. [V10 §7R]
- Must never: DESIGNED — Use the check to choose a side in an interpretive clash. [V10 §7R]
- Fails closed by: DESIGNED — The contradictory value cannot pass validation. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.2.2 — Failed relevance dimension | A detected contradiction. | Keeps the Failed outcome. | A structural check remains distinct from truth authority. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.6.2.2.4 — Out-of-bounds dimension failure
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Failure for a value outside declared bounds. [V10 §7R]
- Takes in: DESIGNED — The value and violated declared bounds. [V10 §7R]
- Does: DESIGNED — Assigns Failed. [V10 §7R]
- Gives out: DESIGNED — Failed with the bounds defect. [V10 §7R]
- Must never: DESIGNED — Silently widen bounds to accept the result. [V10 §7R]
- Fails closed by: DESIGNED — The out-of-bounds value cannot pass. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.2.2 — Failed relevance dimension | A bounds violation. | Keeps the Failed outcome. | Declared bounds remain effective. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.6.2.2.5 — Missing-provenance dimension failure
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Failure when required provenance is missing. [V10 §7R]
- Takes in: DESIGNED — The missing or unpopulated required provenance. [V10 §7R]
- Does: DESIGNED — Assigns Failed. [V10 §7R]
- Gives out: DESIGNED — Failed with the provenance defect. [V10 §7R]
- Must never: DESIGNED — Invent provenance to complete the record. [V10 §7R]
- Fails closed by: DESIGNED — Untraceable output cannot pass. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.2.2 — Failed relevance dimension | Missing required provenance. | Keeps the Failed outcome. | Provenance cannot be fabricated. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.6.2.2.6 — Undeclared-input dimension failure
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Failure when a value relies on undeclared inputs. [V10 §7R]
- Takes in: DESIGNED — The out-of-scope supporting material. [V10 §7R]
- Does: DESIGNED — Assigns Failed. [V10 §7R]
- Gives out: DESIGNED — Failed with the scope violation. [V10 §7R]
- Must never: DESIGNED — Retroactively treat the undeclared material as authorized grounding. [V10 §7R]
- Fails closed by: DESIGNED — The out-of-scope value cannot pass. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.2.2 — Failed relevance dimension | Reliance on undeclared inputs. | Keeps the Failed outcome. | Declared input boundaries remain binding. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.6.2.3 — Unresolved relevance dimension
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The outcome for grounded structurally valid interpretation whose correctness cannot be independently established by deterministic means. [V10 §7R]
- Takes in: DESIGNED — A structurally grounded result with unresolved interpretive correctness. [V10 §7R]
- Does: DESIGNED — Preserves that uncertainty. [V10 §7R]
- Gives out: DESIGNED — Unresolved. [V10 §7R]
- Must never: DESIGNED — Promote structural validity into established interpretation. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.2 — Three mouth validation outcomes | A grounded but independently unverified interpretation. | Labels it Unresolved. | The consumer follows its declared uncertainty handling. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.6.3 — Optional declared model-based validation
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Additional model validation required only for specifically declared dimensions or contexts. [V10 §7R]
- Takes in: DESIGNED — A Tier-1 declaration naming the validator model/configuration and why it is required. [V10 §7R]
- Does: DESIGNED — Uses declared meaningful independence, records a separate provenance-bearing result and handles disagreement through the declared uncertainty rule. [V10 §7R]
- Gives out: DESIGNED — A separate validation result and, when contradicted, a disagreement record. [V10 §7R]
- Must never: DESIGNED — Treat a repeated same-model same-setup call as independent or make the validator final authority. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.6.3.1 — Model-validator declaration: validator declaration; C-7R.6.3.2 — Declared validator independence: independence; C-7R.6.3.3 — Separate model-validation result: own result; C-7R.6.3.4 — Producer-validator disagreement handling: disagreement handling. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6 — Mouth-produced dimension validation | The declared independent validation result. | Adds it without replacing deterministic checks. | No second-model authority is created. | [V10 §7R] |

SUB-PARTS: C-7R.6.3.1 — Model-validator declaration; C-7R.6.3.2 — Declared validator independence; C-7R.6.3.3 — Separate model-validation result; C-7R.6.3.4 — Producer-validator disagreement handling

### C-7R.6.3.1 — Model-validator declaration
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Tier 1’s name/configuration and reason for a required model validator. [V10 §7R]
- Takes in: DESIGNED — The specific validator model or configuration and the reason it is required for the dimension/context. [V10 §7R]
- Does: DESIGNED — Preserves both identity and rationale in the declaration. [V10 §7R]
- Gives out: DESIGNED — An explicitly declared additional validator. [V10 §7R]
- Must never: DESIGNED — Require an undeclared model validator silently. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.3 — Optional declared model-based validation | Named validator/configuration and reason. | Runs the additional validation only as declared. | The extra model is not a hidden requirement. | [V10 §7R] |
| 2 · DESIGNED | C-7R.11.6 — Disagreement validator identity and independence | The actual declared validator model/configuration. | Preserves its identity and version in the conflict record. | Validator provenance stays separate. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.6.3.2 — Declared validator independence
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The mode’s stated mechanism for meaningful independence. [V10 §7R]
- Takes in: DESIGNED — How independence from the producer is increased. [V10 §7R]
- Does: DESIGNED — Requires an explicit independence mechanism. [V10 §7R]
- Gives out: DESIGNED — A declared independent-validation basis. [V10 §7R]
- Must never: DESIGNED — Count the same mouth model called again with the same setup as independent. [V10 §7R]
- Fails closed by: DESIGNED — That repeated identical setup does not satisfy independence. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.3 — Optional declared model-based validation | The declared independence mechanism. | Keeps the optional validator meaningfully separate. | A duplicate call gains no independent status. | [V10 §7R] |
| 2 · DESIGNED | C-7R.11.6 — Disagreement validator identity and independence | The declared independence mechanism. | Records how independence was increased. | An identical repeated model call cannot claim independence. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.6.3.3 — Separate model-validation result
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The validator’s own provenance-bearing output. [V10 §7R]
- Takes in: DESIGNED — The declared validator’s actual validation result and provenance. [V10 §7R]
- Does: DESIGNED — Records that result separately from the producer value. [V10 §7R]
- Gives out: DESIGNED — An independently attributable validator result. [V10 §7R]
- Must never: DESIGNED — Merge the two outputs into one untraceable result or grant the validator final authority. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.3 — Optional declared model-based validation | The separate provenance-bearing validation output. | Retains both producer and validator records. | Their origins stay distinguishable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.6.3.4 — Producer-validator disagreement handling
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The response when a declared model validator contradicts a mouth-produced dimension. [V10 §7R]
- Takes in: DESIGNED — The two separate results and the mode’s declared uncertainty behavior. [V10 §7R]
- Does: DESIGNED — Records the disagreement and applies that declared behavior. [V10 §7R]
- Gives out: DESIGNED — A disagreement record and the resulting dimension state. [V10 §7R]
- Must never: DESIGNED — Silently select the result with greater model confidence. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.11 — Relevance disagreement record: the complete disagreement record; C-7R.10 — Tier-boundary unresolved-rule reference: the required local-rule reference. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6.3 — Optional declared model-based validation | The conflict and uncertainty rule. | Preserves the disagreement rather than choosing a confidence winner. | Uncertainty stays inspectable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.6.4 — Mouth dimensions cannot be categorical gates
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The permanent deterministic context-gate boundary unless a later explicit protected exception is designed. [V10 §7R]
- Takes in: DESIGNED — A proposed use of a mouth-produced interpretive dimension. [V10 §7R]
- Does: DESIGNED — Allows graded ranking or explanation while forbidding categorical context-gate use. [V10 §7R]
- Gives out: DESIGNED — Interpretive contribution confined to graded output. [V10 §7R]
- Must never: DESIGNED — Make a mouth-produced dimension a categorical gate or invent the later exception. [V10 §7R]
- Fails closed by: DESIGNED — Blocks the prohibited gate use. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.6 — Mouth-produced dimension validation | The deterministic-gate boundary. | Confines interpretation to graded output. | Validation never turns interpretation into a gate. | [V10 §7R] |
| 2 · DESIGNED | C-7R.1.1 — Context-specific boolean gate | A proposed categorical condition. | Excludes mouth-produced interpretation from gate conditions. | Gates remain deterministic. | [V10 §7R] |
| 3 · DESIGNED | C-7R.2.3 — Declared interpretive mouth producer | The mouth output’s permitted role. | Keeps it in grading or explanation. | The producer cannot exclude candidates categorically. | [V10 §7R] |
| 4 · DESIGNED | C-7R.4.1.5 — Tier 1 gate conditions and producers | The declared gate producer. | Requires a deterministic condition. | No mouth gate enters Tier 1. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7 — Minimum shared relevance vocabulary
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Four shared boolean gate conditions and nine shared named dimensions. [V10 §7R]
- Takes in: DESIGNED — The vocabulary entries chosen by a declared mode. [V10 §7R]
- Does: DESIGNED — Preserves their exact meanings, provenance and applicability while keeping retrieval-channel metadata and privacy prerequisites separate. [V10 §7R]
- Gives out: DESIGNED — Shared, explicit relevance language. [V10 §7R]
- Must never: DESIGNED — Merge retrieval channels, redefine privacy as a relevance gate or let a local vocabulary silently become shared. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.7.1 — Shared deterministic gate vocabulary: four gates; C-7R.7.2 — Shared named dimension vocabulary: nine dimensions; C-7R.7.3 — Retrieval-channel provenance boundary: channel distinction; C-7R.7.4 — Local dimension and shared-vocabulary extension: local/shared extension. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R — Attention & Relevance Control (§7R) | The common gate/dimension vocabulary. | Uses declared terms with stable meanings. | Consumers do not acquire hidden relevance dialects. | [V10 §7R] |

SUB-PARTS: C-7R.7.1 — Shared deterministic gate vocabulary; C-7R.7.2 — Shared named dimension vocabulary; C-7R.7.3 — Retrieval-channel provenance boundary; C-7R.7.4 — Local dimension and shared-vocabulary extension

### C-7R.7.1 — Shared deterministic gate vocabulary
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The minimum four categorical, rule-produced gate conditions. [V10 §7R]
- Takes in: DESIGNED — The candidate, target and declared context. [V10 §7R]
- Does: DESIGNED — Uses the individually declared gate conditions with their exact meanings. [V10 §7R]
- Gives out: DESIGNED — Named boolean gate results. [V10 §7R]
- Must never: DESIGNED — Infer semantic membership from a deterministic structural gate. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.7.1.1 — same_thread_or_group: same_thread_or_group; C-7R.7.1.2 — precedes_target_in_same_thread: precedes_target_in_same_thread; C-7R.7.1.3 — within_declared_time_range: within_declared_time_range; C-7R.7.1.4 — object_type_matches: object_type_matches. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7 — Minimum shared relevance vocabulary | Four shared gate definitions. | Keeps the categorical language common. | A condition has the same defined meaning across modes. | [V10 §7R] |
| 2 · DESIGNED | C-7R.1.1 — Context-specific boolean gate | Declared shared conditions. | Evaluates deterministic context membership. | No model interpretation becomes categorical. | [V10 §7R] |
| 3 · DESIGNED | C-7R.4.1.5 — Tier 1 gate conditions and producers | The exact gate definitions. | Names the selected gates and producers. | The declaration remains explicit. | [V10 §7R] |

SUB-PARTS: C-7R.7.1.1 — same_thread_or_group; C-7R.7.1.2 — precedes_target_in_same_thread; C-7R.7.1.3 — within_declared_time_range; C-7R.7.1.4 — object_type_matches

### C-7R.7.1.1 — same_thread_or_group
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Whether candidate and target belong to the same recorded thread or grouping. [V10 §7R]
- Takes in: DESIGNED — Their recorded thread/group membership. [V10 §7R]
- Does: DESIGNED — Compares recorded membership; current implementation may derive it from source_title without making that legacy field a permanent vocabulary dependency. [V10 §7R]
- Gives out: DESIGNED — A deterministic same-group boolean. [V10 §7R]
- Must never: DESIGNED — Treat source_title as a permanent architectural requirement or infer sameness from thematic similarity. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.1 — Shared deterministic gate vocabulary | Recorded thread/group membership. | Evaluates same_thread_or_group. | Structural grouping remains separate from similarity. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.1.2 — precedes_target_in_same_thread
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Whether the candidate root precedes the target root within the same recorded thread or grouping. [V10 §7R]
- Takes in: DESIGNED — The two roots’ positions and shared grouping. [V10 §7R]
- Does: DESIGNED — Checks actual preceding position in that grouping. [V10 §7R]
- Gives out: DESIGNED — A deterministic preceding-root boolean. [V10 §7R]
- Must never: DESIGNED — Use semantic similarity to satisfy positional precedence. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.1 — Shared deterministic gate vocabulary | Shared grouping and root positions. | Evaluates precedes_target_in_same_thread. | Later or differently grouped material cannot masquerade as preceding context. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.1.3 — within_declared_time_range
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Whether the candidate falls in a time range explicitly declared in Tier 1. [V10 §7R]
- Takes in: DESIGNED — The candidate’s time and the declared range. [V10 §7R]
- Does: DESIGNED — Tests membership in that range. [V10 §7R]
- Gives out: DESIGNED — A deterministic time-range boolean. [V10 §7R]
- Must never: DESIGNED — Invent an undeclared time cutoff. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.1 — Shared deterministic gate vocabulary | Candidate time and declared range. | Evaluates within_declared_time_range. | Time filtering remains explicit. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.1.4 — object_type_matches
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Whether the candidate’s object type matches the eligible types declared for this context. [V10 §7R]
- Takes in: DESIGNED — The candidate type and declared eligible types. [V10 §7R]
- Does: DESIGNED — Compares them deterministically. [V10 §7R]
- Gives out: DESIGNED — An object-type boolean. [V10 §7R]
- Must never: DESIGNED — Treat an undeclared object type as eligible. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.1 — Shared deterministic gate vocabulary | The candidate and eligible types. | Evaluates object_type_matches. | Type membership remains a declared rule. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.2 — Shared named dimension vocabulary
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Nine named graded dimensions with producer and applicability boundaries. [V10 §7R]
- Takes in: DESIGNED — The passing candidate, target/query and available recorded provenance. [V10 §7R]
- Does: DESIGNED — Preserves each selected value without converting metadata into truth or combining dimensions into a hidden score. [V10 §7R]
- Gives out: DESIGNED — The applicable declared dimensions with their own provenance. [V10 §7R]
- Must never: DESIGNED — Create links, resolve clashes or infer currentness while merely reading these dimensions. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.7.2.1 — semantic_similarity: semantic_similarity; C-7R.7.2.2 — temporal_distance: temporal_distance; C-7R.7.2.3 — positional_distance: positional_distance; C-7R.7.2.4 — currentness_status: currentness_status; C-7R.7.2.5 — explicit_links: explicit_links; C-7R.7.2.6 — ness_response_links: ness_response_links; C-7R.7.2.7 — proposal_acceptance_outcome: proposal_acceptance_outcome; C-7R.7.2.8 — reading_context_status: reading_context_status; C-7R.7.2.9 — active_clash_links: active_clash_links. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7 — Minimum shared relevance vocabulary | Nine shared dimension definitions. | Uses their exact names and limitations. | A dimension remains a purpose-specific input. | [V10 §7R] |
| 2 · DESIGNED | C-7R.4.1.6 — Tier 1 dimensions and producers | The selected shared dimensions. | Declares their individual producers. | No implicit dimension is added. | [V10 §7R] |

SUB-PARTS: C-7R.7.2.1 — semantic_similarity; C-7R.7.2.2 — temporal_distance; C-7R.7.2.3 — positional_distance; C-7R.7.2.4 — currentness_status; C-7R.7.2.5 — explicit_links; C-7R.7.2.6 — ness_response_links; C-7R.7.2.7 — proposal_acceptance_outcome; C-7R.7.2.8 — reading_context_status; C-7R.7.2.9 — active_clash_links

### C-7R.7.2.1 — semantic_similarity
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Embedding similarity between a candidate and target or declared query representation. [V10 §7R]
- Takes in: DESIGNED — Their embedding representations and model/index versions. [V10 §7R]
- Does: DESIGNED — Uses the embedding model to compute similarity. [V10 §7R]
- Gives out: DESIGNED — A semantic_similarity value with model version and index version. [V10 §7R]
- Must never: DESIGNED — Treat similarity as positional evidence or truth. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.2.2 — Embedding dimension producer: the embedding producer. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2 — Shared named dimension vocabulary | Embedding similarity with both versions. | Carries the semantic dimension separately. | Similarity retains its limited meaning. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.2.2 — temporal_distance
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The deterministic raw time distance between candidate and target timestamps. [V10 §7R]
- Takes in: DESIGNED — The two timestamps and their time unit. [V10 §7R]
- Does: DESIGNED — Computes raw distance and preserves the unit; normalization, scaling and thresholds belong to Tier 2. [V10 §7R]
- Gives out: DESIGNED — A raw temporal_distance with its unit. [V10 §7R]
- Must never: DESIGNED — Hide scaling or thresholds in the shared dimension. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.4.2 — Tier 2 component-local settings: consumer-owned scaling, normalization and threshold use. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2 — Shared named dimension vocabulary | Raw time distance and unit. | Returns the temporal dimension without hidden scaling. | Local use remains consumer-owned. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.2.3 — positional_distance
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The deterministic count of positions or turns between candidate and target in their shared thread/group. [V10 §7R]
- Takes in: DESIGNED — The recorded positions within that grouping. [V10 §7R]
- Does: DESIGNED — Counts the positional distance. [V10 §7R]
- Gives out: DESIGNED — A positional_distance value. [V10 §7R]
- Must never: DESIGNED — Convert semantic similarity into positional distance. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2 — Shared named dimension vocabulary | The recorded position/turn distance. | Keeps positional proximity distinct. | Semantic similarity cannot repair it. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.2.4 — currentness_status
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The candidate state node’s recorded Living State Web currentness category. [V10 §7R]
- Takes in: DESIGNED — A state-node candidate and its recorded status. [V10 §7R]
- Does: DESIGNED — Reads the recorded category deterministically; it does not determine relevance strength or recompute currentness. [V10 §7R]
- Gives out: DESIGNED — The recorded currentness_status, applicable when the candidate is a state node. [V10 §7R]
- Must never: DESIGNED — Use it as evidence that the state is current or infer relevance strength directly from the category. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7D.10 — State currentness: canonical six-state currentness vocabulary and recorded category: current, possibly_current, stale, currentness_unknown, ended_by_evidence, superseded_by_evidence. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §5]
- Gated by: DESIGNED — C-7R.8 — Living State Web relevance boundary: currentness and relevance remain separate and circular support is forbidden. [V10 §7R]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2 — Shared named dimension vocabulary | The recorded state-node category. | Carries it as a dimension without changing it. | Relevance grants no currentness update. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.2.5 — explicit_links
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — A deterministic multi-valued list of recorded structural links between candidate and target. [V10 §7R]
- Takes in: DESIGNED — Existing store links, each with type, status and provenance. [V10 §7R]
- Does: DESIGNED — Surfaces only links already recorded. [V10 §7R]
- Gives out: DESIGNED — Separate explicit_links entries. [V10 §7R]
- Must never: DESIGNED — Create or confirm a link through relevance evaluation. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.7.2.5.1 — Explicit-link type: link type; C-7R.7.2.5.2 — Explicit-link status: link status; C-7R.7.2.5.3 — Explicit-link provenance: link provenance. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2 — Shared named dimension vocabulary | Existing structural links. | Returns their types, states and provenance. | A proposed link never becomes confirmed by relevance. | [V10 §7R] |

SUB-PARTS: C-7R.7.2.5.1 — Explicit-link type; C-7R.7.2.5.2 — Explicit-link status; C-7R.7.2.5.3 — Explicit-link provenance

### C-7R.7.2.5.1 — Explicit-link type
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The recorded type of each explicit structural link. [V10 §7R]
- Takes in: DESIGNED — The recorded relationship between candidate and target. [V10 §7R]
- Does: DESIGNED — Preserves the applicable link type. [V10 §7R]
- Gives out: DESIGNED — same Person-Box, same confirmed theme, same proposed theme, same derived_from chain, or shared root IDs in a telling. [V10 §7R]
- Must never: DESIGNED — Conflate proposed and confirmed themes or derive a new relationship merely from similarity. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.7.2.5.1.1 — same Person-Box link: same Person-Box; C-7R.7.2.5.1.2 — same confirmed theme link: same confirmed theme; C-7R.7.2.5.1.3 — same proposed theme link: same proposed theme; C-7R.7.2.5.1.4 — same derived_from chain link: same derived_from chain; C-7R.7.2.5.1.5 — shared root IDs in a telling link: shared roots in a telling. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2.5 — explicit_links | The recorded structural type. | Retains what the link actually says. | Different link types remain distinct. | [V10 §7R] |

SUB-PARTS: C-7R.7.2.5.1.1 — same Person-Box link; C-7R.7.2.5.1.2 — same confirmed theme link; C-7R.7.2.5.1.3 — same proposed theme link; C-7R.7.2.5.1.4 — same derived_from chain link; C-7R.7.2.5.1.5 — shared root IDs in a telling link

### C-7R.7.2.5.1.1 — same Person-Box link
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Recorded same-Person-Box structural linkage. [V10 §7R]
- Takes in: DESIGNED — An existing shared Person-Box link. [V10 §7R]
- Does: DESIGNED — Preserves that recorded link type. [V10 §7R]
- Gives out: DESIGNED — same Person-Box. [V10 §7R]
- Must never: DESIGNED — Merge identities through relevance. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2.5.1 — Explicit-link type | The existing shared-box link. | Labels its recorded type. | Relevance performs no identity merge. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.2.5.1.2 — same confirmed theme link
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Recorded linkage through the same confirmed theme. [V10 §7R]
- Takes in: DESIGNED — The existing confirmed-theme link. [V10 §7R]
- Does: DESIGNED — Preserves the confirmed-theme type. [V10 §7R]
- Gives out: DESIGNED — same confirmed theme. [V10 §7R]
- Must never: DESIGNED — Infer confirmation merely from similarity. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2.5.1 — Explicit-link type | The confirmed-theme link. | Retains its recorded type. | Confirmation remains prior recorded status. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.2.5.1.3 — same proposed theme link
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Recorded linkage through the same proposed theme. [V10 §7R]
- Takes in: DESIGNED — The existing proposed-theme link. [V10 §7R]
- Does: DESIGNED — Preserves its proposed standing. [V10 §7R]
- Gives out: DESIGNED — same proposed theme. [V10 §7R]
- Must never: DESIGNED — Promote it to confirmed theme through relevance. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2.5.1 — Explicit-link type | The proposed-theme link. | Retains the proposed type. | Proposal is not confirmation. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.2.5.1.4 — same derived_from chain link
Stamp: DESIGNED    Source: [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]

ALONE
- What it is: DESIGNED — Recorded membership in the same derived_from chain. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Takes in: DESIGNED — The existing derivation-chain references. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Does: DESIGNED — Preserves that structural relationship. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Gives out: DESIGNED — same derived_from chain. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Must never: DESIGNED — Treat shared derivation as independent corroboration. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2.5.1 — Explicit-link type | The existing derivation-chain link. | Retains its recorded type. | Common derivation does not create independent evidence. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.2.5.1.5 — shared root IDs in a telling link
Stamp: DESIGNED    Source: [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]

ALONE
- What it is: DESIGNED — Recorded linkage through shared root IDs in a telling. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Takes in: DESIGNED — The telling’s existing root references. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Does: DESIGNED — Preserves the shared-root relationship. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Gives out: DESIGNED — shared root IDs in a telling. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Must never: DESIGNED — Treat repeated root references as new independent evidence. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2.5.1 — Explicit-link type | The recorded shared roots. | Retains the structural link type. | Shared evidence is not multiplied. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.2.5.2 — Explicit-link status
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The existing status of one recorded structural link. [V10 §7R]
- Takes in: DESIGNED — That link’s recorded status. [V10 §7R]
- Does: DESIGNED — Carries the status without promoting or changing it. [V10 §7R]
- Gives out: DESIGNED — A status-bearing link entry. [V10 §7R]
- Must never: DESIGNED — Promote proposed linkage to confirmation through relevance. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2.5 — explicit_links | The existing link status. | Preserves its actual standing. | Ranking does not confirm a link. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.2.5.3 — Explicit-link provenance
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The provenance of a recorded structural link. [V10 §7R]
- Takes in: DESIGNED — The link’s stored provenance. [V10 §7R]
- Does: DESIGNED — Preserves the source of the relationship. [V10 §7R]
- Gives out: DESIGNED — A traceable link entry. [V10 §7R]
- Must never: DESIGNED — Surface a newly invented relationship as recorded provenance. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2.5 — explicit_links | The recorded link provenance. | Keeps the relationship auditable. | The source remains distinguishable from relevance use. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.2.6 — ness_response_links
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Deterministically read Ness response events pointing to the candidate. [V10 §7R]
- Takes in: DESIGNED — Recorded linked response events. [V10 §7R]
- Does: DESIGNED — Carries each event’s response type, scope, target identifier and timestamp. [V10 §7R]
- Gives out: DESIGNED — Separate ness_response_links entries. [V10 §7R]
- Must never: DESIGNED — Rewrite a response or turn a relevance judgment into a Ness response. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.7.2.6.1 — Response-link type: response type; C-7R.7.2.6.2 — Response-link scope: scope; C-7R.7.2.6.3 — Response-link target identifier: target; C-7R.7.2.6.4 — Response-link timestamp: timestamp. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2 — Shared named dimension vocabulary | Recorded Ness response links. | Preserves their full scope and origin. | Responses remain separate evidence events. | [V10 §7R] |

SUB-PARTS: C-7R.7.2.6.1 — Response-link type; C-7R.7.2.6.2 — Response-link scope; C-7R.7.2.6.3 — Response-link target identifier; C-7R.7.2.6.4 — Response-link timestamp

### C-7R.7.2.6.1 — Response-link type
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The recorded type of the linked Ness response. [V10 §7R]
- Takes in: DESIGNED — The event’s response type. [V10 §7R]
- Does: DESIGNED — Retains what kind of response occurred. [V10 §7R]
- Gives out: DESIGNED — An explicit response type. [V10 §7R]
- Must never: DESIGNED — Infer a different response from model interpretation. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2.6 — ness_response_links | The recorded response type. | Keeps the event meaning explicit. | The response is not reinterpreted as consent. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.2.6.2 — Response-link scope
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The scope of the linked Ness response. [V10 §7R]
- Takes in: DESIGNED — The event’s recorded scope. [V10 §7R]
- Does: DESIGNED — Preserves where the response applies. [V10 §7R]
- Gives out: DESIGNED — An explicit scope. [V10 §7R]
- Must never: DESIGNED — Expand a contextual response into a permanent instruction. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2.6 — ness_response_links | The actual response scope. | Limits use to what was recorded. | Context is not silently widened. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.2.6.3 — Response-link target identifier
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The target identified by the Ness response event. [V10 §7R]
- Takes in: DESIGNED — The recorded target identifier. [V10 §7R]
- Does: DESIGNED — Retains which object the response concerns. [V10 §7R]
- Gives out: DESIGNED — An exact target reference. [V10 §7R]
- Must never: DESIGNED — Transfer the response to a different object. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2.6 — ness_response_links | The response target. | Links the event to its actual object. | Identity remains traceable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.2.6.4 — Response-link timestamp
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — When the recorded Ness response occurred. [V10 §7R]
- Takes in: DESIGNED — The event timestamp. [V10 §7R]
- Does: DESIGNED — Preserves the original response time. [V10 §7R]
- Gives out: DESIGNED — A timestamped response link. [V10 §7R]
- Must never: DESIGNED — Replace event time with retrieval time. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2.6 — ness_response_links | The response timestamp. | Retains the event’s temporal provenance. | Later use does not make the response new. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.2.7 — proposal_acceptance_outcome
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The recorded Reading Proposal Acceptance Check outcome for a candidate reading. [V10 §7R]
- Takes in: DESIGNED — The actual acceptance outcome and exact rejection reason when it failed. [V10 §7R]
- Does: DESIGNED — Reads the outcome deterministically, only for reading candidates. [V10 §7R]
- Gives out: DESIGNED — proposal_acceptance_outcome with the exact failure reason where applicable. [V10 §7R]
- Must never: DESIGNED — Treat relevance as acceptance or erase the rejection reason. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7G.5 — Rejection and genuine insufficiency remain separate: distinct acceptance rejection and genuine insufficiency. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2 — Shared named dimension vocabulary | The recorded reading acceptance outcome. | Preserves acceptance and exact failure reason. | Relevance cannot reverse acceptance. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.2.8 — reading_context_status
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Whether a candidate accepted reading is marked context-limited or insufficient_context. [V10 §7R]
- Takes in: DESIGNED — The accepted reading’s recorded context status. [V10 §7R]
- Does: DESIGNED — Reads the marker deterministically, only for accepted-reading candidates. [V10 §7R]
- Gives out: DESIGNED — reading_context_status, separate from proposal_acceptance_outcome. [V10 §7R]
- Must never: DESIGNED — Conflate insufficient context with acceptance rejection. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7G.5 — Rejection and genuine insufficiency remain separate: acceptance versus insufficiency separation. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2 — Shared named dimension vocabulary | The accepted reading’s context marker. | Keeps contextual limitation distinct from acceptance. | A valid reading can remain context-limited. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.2.9 — active_clash_links
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Deterministically read active clashes, contrary evidence or unresolved conflicts associated with the candidate. [V10 §7R]
- Takes in: DESIGNED — The linked recorded conflicts. [V10 §7R]
- Does: DESIGNED — Surfaces each link with clash record identifier, type and detection mode. [V10 §7R]
- Gives out: DESIGNED — Separate active_clash_links entries. [V10 §7R]
- Must never: DESIGNED — Resolve a clash, choose its correct side or suppress contrary evidence. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.7.2.9.1 — Clash-link record identifier: clash identifier; C-7R.7.2.9.2 — Clash-link type: type; C-7R.7.2.9.3 — Clash-link detection mode: detection mode; C-7J — Clash Handling (§7J): existing clash records. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2 — Shared named dimension vocabulary | Recorded clash/contrary/unresolved links. | Carries them without resolution. | Conflict remains visible. | [V10 §7R] |

SUB-PARTS: C-7R.7.2.9.1 — Clash-link record identifier; C-7R.7.2.9.2 — Clash-link type; C-7R.7.2.9.3 — Clash-link detection mode

### C-7R.7.2.9.1 — Clash-link record identifier
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The exact clash record referenced by a dimension entry. [V10 §7R]
- Takes in: DESIGNED — The recorded clash identifier. [V10 §7R]
- Does: DESIGNED — Preserves which clash is linked. [V10 §7R]
- Gives out: DESIGNED — An identifiable conflict reference. [V10 §7R]
- Must never: DESIGNED — Replace the actual clash with a generic conflict claim. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2.9 — active_clash_links | The clash record identifier. | Keeps the conflict traceable. | The original clash remains the owner record. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.2.9.2 — Clash-link type
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The recorded type of the linked clash. [V10 §7R]
- Takes in: DESIGNED — The clash record’s type. [V10 §7R]
- Does: DESIGNED — Carries that classification without choosing a winner. [V10 §7R]
- Gives out: DESIGNED — An explicit clash type. [V10 §7R]
- Must never: DESIGNED — Treat type as proof of which side is correct. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2.9 — active_clash_links | The clash type. | Preserves the recorded distinction. | Classification is not resolution. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.2.9.3 — Clash-link detection mode
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The mode through which the linked clash was detected. [V10 §7R]
- Takes in: DESIGNED — Its recorded detection mode. [V10 §7R]
- Does: DESIGNED — Retains detection provenance. [V10 §7R]
- Gives out: DESIGNED — An explicit detection-mode reference. [V10 §7R]
- Must never: DESIGNED — Hide how the conflict was found. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7.2.9 — active_clash_links | The detection mode. | Preserves conflict provenance. | The link is auditable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.3 — Retrieval-channel provenance boundary
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Mandatory positional-versus-semantic channel identity in the retrieval record. [V10 §7R]
- Takes in: DESIGNED — Each retrieved item’s channel metadata. [V10 §7R]
- Does: DESIGNED — Preserves the channel distinction as provenance, not as a relevance dimension. [V10 §7R]
- Gives out: DESIGNED — Labeled separate retrieval channels. [V10 §7R]
- Must never: DESIGNED — Merge the channels or use semantic context to replace positional evidence. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7F.4.6.1 — Supplied-item retrieval type: canonical supplied-item retrieval type. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7 — Minimum shared relevance vocabulary | The mandatory channel identity. | Keeps it separate from graded dimensions. | Channel provenance survives relevance evaluation. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.7.4 — Local dimension and shared-vocabulary extension
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The declared local-extension and later shared-promotion path. [V10 §7R]
- Takes in: DESIGNED — A new local dimension or one used across multiple components. [V10 §7R]
- Does: DESIGNED — Allows a consumer to declare a local dimension when designing its mode; later shared promotion uses proposal, confirmation and versioning. [V10 §7R]
- Gives out: DESIGNED — A declared local dimension or confirmed new shared-vocabulary version. [V10 §7R]
- Must never: DESIGNED — Silently promote local use into a shared rule. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7R.5.4 — Reusable mode change: shared promotion requires consequence preview, confirmation and versioning. [V10 §7R]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.7 — Minimum shared relevance vocabulary | A proposed vocabulary extension. | Keeps local declaration distinct from shared promotion. | The shared vocabulary changes explicitly. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.8 — Living State Web relevance boundary
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The separation between relevance records and state-currentness authority. [V10 §7R]
- Takes in: DESIGNED — A purpose-scoped relevance event and any independently valid state evidence. [V10 §7R]
- Does: DESIGNED — Emits relevance records into its own record space; only an explicitly designed state-owner rule may use an event as a review trigger. [V10 §7R]
- Gives out: DESIGNED — A possible review trigger, never a direct state write or evidence of the review’s outcome. [V10 §7R]
- Must never: DESIGNED — Write directly into Living State Web or use relevance to prove currentness. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.8.1 — Review trigger is not review evidence: trigger versus evidence; C-7R.8.2 — Relevance and currentness are separate properties: property separation; C-7R.8.3 — Separate Ness currentness-evidence event: separate Ness evidence; C-7R.8.4 — Forbidden relevance-currentness feedback chain: forbidden feedback chain. [V10 §7R]
- Gated by: DESIGNED — C-7D — Living State Web (§7D): only its explicitly designed review rule can authorize a relevance event as a trigger. [V10 §7R]
- Changes: DESIGNED — C-7D — Living State Web (§7D): may receive a provenance-bearing event for authorized review, without receiving a currentness determination. [V10 §7R]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R — Attention & Relevance Control (§7R) | The relevance/state boundary. | Emits only its own relevance records. | No relevance judgment writes state. | [V10 §7R] |
| 2 · DESIGNED | C-7R.7.2.4 — currentness_status | The prohibition on relevance/currentness circularity. | Reads the recorded category without updating it. | The dimension cannot prove currentness. | [V10 §7R] |
| 3 · ACCEPTED | C-7R.16.5 — State-review declaration interface | The state-owned review-trigger authority and no-evidence boundary. | Uses relevance only as a possible review signal. | The result cannot determine currentness. | [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10] |

SUB-PARTS: C-7R.8.1 — Review trigger is not review evidence; C-7R.8.2 — Relevance and currentness are separate properties; C-7R.8.3 — Separate Ness currentness-evidence event; C-7R.8.4 — Forbidden relevance-currentness feedback chain

### C-7R.8.1 — Review trigger is not review evidence
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — A relevance event can cause an authorized review but cannot supply its outcome evidence. [V10 §7R]
- Takes in: DESIGNED — A relevance event and independently valid root evidence, a separate Ness response event or another explicitly authorized evidence source. [V10 §7R]
- Does: DESIGNED — Leaves actual currentness updates to the state owner using independent valid evidence. [V10 §7R]
- Gives out: DESIGNED — An authorized review with independent support, where the state-owner rule exists. [V10 §7R]
- Must never: DESIGNED — Count a relevance event alone as evidence that a state is current. [V10 §7R]
- Fails closed by: DESIGNED — No state-currentness conclusion follows from relevance alone. [V10 §7R]

TOGETHER
- Fed by: ACCEPTED — C-7D.14 — State-currentness review: state-owned review; C-7D.14.2 — Proposed RM-LS-01 state-review declaration: the accepted proposed RM-LS-01 declaration and its trigger-only limits. [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.8 — Living State Web relevance boundary | The review/evidence distinction. | Keeps trigger authority with the state owner. | The event cannot decide the outcome. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.8.2 — Relevance and currentness are separate properties
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The permanent distinction between relevance for a purpose and a state’s currentness. [V10 §7R]
- Takes in: DESIGNED — Historical, ended, uncertain, contradicted or under-review material that may still matter to the current purpose. [V10 §7R]
- Does: DESIGNED — Allows such material to be relevant without changing its recorded currentness. [V10 §7R]
- Gives out: DESIGNED — A relevance judgment independent of whether the state is current. [V10 §7R]
- Must never: DESIGNED — Infer currentness from high relevance or infer ending from low relevance. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.8 — Living State Web relevance boundary | Relevant material with its actual currentness. | Preserves both properties separately. | Historical relevance cannot revive a state. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.8.3 — Separate Ness currentness-evidence event
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — A Ness statement that itself supplies currentness evidence during an interaction. [V10 §7R]
- Takes in: DESIGNED — The actual statement and its own provenance. [V10 §7R]
- Does: DESIGNED — Records the statement as a separate Ness response event. [V10 §7R]
- Gives out: DESIGNED — Independently attributable Ness evidence. [V10 §7R]
- Must never: DESIGNED — Embed the evidence inside the relevance judgment or derive it from that judgment. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.8 — Living State Web relevance boundary | The separate response event. | Keeps Ness evidence independent of relevance. | A judgment does not manufacture evidence. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.8.4 — Forbidden relevance-currentness feedback chain
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The prohibition on currentness supporting itself through relevance. [V10 §7R]
- Takes in: DESIGNED — A relevance result partly dependent on recorded currentness_status. [V10 §7R]
- Does: DESIGNED — Prevents the chain currentness_status → relevance judgment → currency update → currentness_status from serving as support. [V10 §7R]
- Gives out: DESIGNED — No circular currentness justification. [V10 §7R]
- Must never: DESIGNED — Make a state current because it was relevant when that relevance partly depended on its currentness. [V10 §7R]
- Fails closed by: DESIGNED — The circular result supplies no valid currentness evidence. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.8 — Living State Web relevance boundary | The proposed support chain. | Rejects circular currentness support. | A state cannot bootstrap its own currency. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.9 — Tier 1 structured purpose
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The purpose/context object: a required controlled type and optional explanatory string label. [V10 §7R]
- Takes in: DESIGNED — The controlled type and any human-readable label. [V10 §7R]
- Does: DESIGNED — Validates the type before accepting the configuration; uses it for Tier-1 validation and cross-mode comparison while giving the label no behavioral effect. [V10 §7R]
- Gives out: DESIGNED — A recognized purpose with optional explanation. [V10 §7R]
- Must never: DESIGNED — Let label wording alter validation, routing or evaluation, or guess an unknown type. [V10 §7R]
- Fails closed by: DESIGNED — An unknown controlled type halts before evaluation. [V10 §7R]

TOGETHER
- Fed by: DESIGNED — C-7R.9.1 — Required controlled purpose type: controlled type; C-7R.9.2 — Optional explanatory purpose label: optional label; C-7R.9.3 — Five controlled purpose values: five starting values; C-7R.9.4 — Controlled-purpose vocabulary change: vocabulary change. [V10 §7R]
- Gated by: DESIGNED — C-7R.14 — Unrecognized purpose-type halt: the exact unknown-type path. [V10 §7R]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R — Attention & Relevance Control (§7R) | The recognized purpose and optional inert label. | Keeps relevance task-specific. | Labels cannot change policy. | [V10 §7R] |
| 2 · DESIGNED | C-7R.4.1 — Tier 1 shared required contract | The structured purpose. | Validates the required controlled value. | Configuration cannot use an unrecognized purpose. | [V10 §7R] |
| 3 · DESIGNED | C-7R.12.3 — Evaluation purpose type and label | The actual controlled type and optional explanatory label. | Records the purpose without granting the label behavioral meaning. | Evaluation remains purpose-bound. | [V10 §7R] |
| 4 · ACCEPTED | C-7R.15.2 — Declaration Task or purpose | The required known type and optional inert string. | Declares the actual task purpose. | No free-form label substitutes for controlled vocabulary. | [V10 §7R] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] |
| 5 · DESIGNED | C-LEARN.5.1 — Personalization domain guides query purpose | The personalization domain and current shared material. | Supplies the controlled purpose contract. | Nothing in this card. | [V10 §26.8] [V10 §7R] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 6 · ACCEPTED | C-LMAC.7.1.2 — Query declared purpose | The request’s actual purpose. | Supplies the controlled relevance-purpose contract. | Nothing in this card. | [V10 §7R] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |

SUB-PARTS: C-7R.9.1 — Required controlled purpose type; C-7R.9.2 — Optional explanatory purpose label; C-7R.9.3 — Five controlled purpose values; C-7R.9.4 — Controlled-purpose vocabulary change

### C-7R.9.1 — Required controlled purpose type
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — One required value from the controlled purpose vocabulary. [V10 §7R]
- Takes in: DESIGNED — The declared purpose type. [V10 §7R]
- Does: DESIGNED — Supplies the value used for shared validation and cross-mode comparison. [V10 §7R]
- Gives out: DESIGNED — An explicit controlled type. [V10 §7R]
- Must never: DESIGNED — Replace it with an informal label or silently substitute a close match. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.9 — Tier 1 structured purpose | The controlled purpose value. | Checks membership in the current vocabulary. | A free-form label cannot authorize evaluation. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.9.2 — Optional explanatory purpose label
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — An optional human-readable string describing the consumer’s particular use. [V10 §7R]
- Takes in: DESIGNED — The explanatory label, if supplied. [V10 §7R]
- Does: DESIGNED — Carries explanation only. [V10 §7R]
- Gives out: DESIGNED — An optional descriptive string with no semantic weight in validation, routing or evaluation. [V10 §7R]
- Must never: DESIGNED — Use label wording to change system behavior. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.9 — Tier 1 structured purpose | The optional string. | Preserves explanation without behavioral effect. | A label is not a new purpose type. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.9.3 — Five controlled purpose values
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The starting shared purpose vocabulary. [V10 §7R]
- Takes in: DESIGNED — The declared task type. [V10 §7R]
- Does: DESIGNED — Distinguishes reading-context selection, view assembly, action surfacing, condition-based reread evaluation and state-review trigger evaluation. [V10 §7R]
- Gives out: DESIGNED — One of the five exact controlled values. [V10 §7R]
- Must never: DESIGNED — Conflate a review-trigger evaluation with determining state currentness. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.9.3.1 — retrieval_context_selection: retrieval_context_selection; C-7R.9.3.2 — view_assembly: view_assembly; C-7R.9.3.3 — action_surfacing: action_surfacing; C-7R.9.3.4 — reread_trigger_evaluation: reread_trigger_evaluation; C-7R.9.3.5 — state_review_trigger_evaluation: state_review_trigger_evaluation. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.9 — Tier 1 structured purpose | The exact controlled vocabulary. | Validates the type’s declared meaning. | Each purpose retains its boundary. | [V10 §7R] |

SUB-PARTS: C-7R.9.3.1 — retrieval_context_selection; C-7R.9.3.2 — view_assembly; C-7R.9.3.3 — action_surfacing; C-7R.9.3.4 — reread_trigger_evaluation; C-7R.9.3.5 — state_review_trigger_evaluation

### C-7R.9.3.1 — retrieval_context_selection
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Evaluation of candidates for context in a reading pass. [V10 §7R]
- Takes in: DESIGNED — Candidates for that reading’s context. [V10 §7R]
- Does: DESIGNED — Names the reading-context selection purpose. [V10 §7R]
- Gives out: DESIGNED — The retrieval_context_selection type. [V10 §7R]
- Must never: DESIGNED — Treat context relevance as truth or reading acceptance. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.9.3 — Five controlled purpose values | The context-selection task. | Identifies its controlled purpose. | Reading context remains a declared use. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.9.3.2 — view_assembly
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Evaluation for inclusion or ordering in a Computed View snapshot or View Layer presentation. [V10 §7R]
- Takes in: DESIGNED — Candidates for that snapshot or presentation. [V10 §7R]
- Does: DESIGNED — Names the view-assembly purpose. [V10 §7R]
- Gives out: DESIGNED — The view_assembly type. [V10 §7R]
- Must never: DESIGNED — Treat view priority as rewritten history or truth. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.9.3 — Five controlled purpose values | The view inclusion/ordering task. | Identifies its controlled purpose. | View use remains purpose-specific. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.9.3.3 — action_surfacing
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Evaluation of candidates supporting a possible action surfaced to Ness. [V10 §7R]
- Takes in: DESIGNED — Candidate support for a possibility. [V10 §7R]
- Does: DESIGNED — Names the action-surfacing purpose. [V10 §7R]
- Gives out: DESIGNED — The action_surfacing type. [V10 §7R]
- Must never: DESIGNED — Grant permission to execute from relevance. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.9.3 — Five controlled purpose values | Support for a possible action. | Identifies its controlled purpose. | Relevance remains separate from authority. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.9.3.4 — reread_trigger_evaluation
Stamp: DESIGNED    Source: [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]

ALONE
- What it is: DESIGNED — Evaluation of materially relevant new information for a condition-based reread trigger. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Takes in: DESIGNED — New information and the possible reread relationship. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Does: DESIGNED — Names the trigger-evaluation purpose. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Gives out: DESIGNED — The reread_trigger_evaluation type. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Must never: DESIGNED — Treat the relevance result alone as a reread or apply it as a blanket gate to Ness’s explicit manual reread. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.9.3 — Five controlled purpose values | A condition-based trigger evaluation. | Identifies its controlled purpose. | Evaluation stays separate from reread authority. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.9.3.5 — state_review_trigger_evaluation
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Evaluation of whether a relevance signal warrants a Living State Web currency review. [V10 §7R]
- Takes in: DESIGNED — The possible relevance-based review signal. [V10 §7R]
- Does: DESIGNED — Names review-trigger evaluation without determining whether the state is current. [V10 §7R]
- Gives out: DESIGNED — The state_review_trigger_evaluation type. [V10 §7R]
- Must never: DESIGNED — Use the type as a currentness determination. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.9.3 — Five controlled purpose values | A possible currency-review trigger. | Identifies its controlled purpose. | The review’s evidence remains independent. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.9.4 — Controlled-purpose vocabulary change
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The difference between changing an explanatory label and adding a controlled type. [V10 §7R]
- Takes in: DESIGNED — A new label or proposed new purpose type. [V10 §7R]
- Does: DESIGNED — Allows label changes without a vocabulary-version change; a new type uses proposal, confirmation and a new version. [V10 §7R]
- Gives out: DESIGNED — An inert label change or a confirmed versioned controlled type. [V10 §7R]
- Must never: DESIGNED — Create a new type by merely relabeling an old mode. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7R.5.4 — Reusable mode change: new controlled types use the full consequence-preview and confirmation path. [V10 §7R]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.9 — Tier 1 structured purpose | The proposed purpose change. | Keeps explanatory text distinct from vocabulary authority. | New behavior requires versioned confirmation. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.10 — Tier-boundary unresolved-rule reference
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The Tier-1 reference to the consumer-owned Tier-2 unresolved-dimension rule when mouth dimensions are declared. [V10 §7R]
- Takes in: DESIGNED — The handling-rule identifier and version. [V10 §7R]
- Does: DESIGNED — Checks that the reference is present, nonempty and current; does not inspect, parse or validate the rule’s content. [V10 §7R]
- Gives out: DESIGNED — A valid rule reference or a missing/stale-reference finding. [V10 §7R]
- Must never: DESIGNED — Take ownership of the Tier-2 rule or impose this obligation on a mode with no mouth-produced dimensions. [V10 §7R]
- Fails closed by: DESIGNED — A missing, empty or mismatched required reference fails Tier-1 validation. [V10 §7R]

TOGETHER
- Fed by: DESIGNED — C-7R.10.1 — Unresolved-rule identifier reference: rule identifier; C-7R.10.2 — Unresolved-rule version reference: rule version; C-7R.10.3 — Local-rule change and stale-reference handling: version-change propagation. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R — Attention & Relevance Control (§7R) | The consumer-rule reference. | Checks the shared obligation without interpreting local rules. | Tier ownership remains separate. | [V10 §7R] |
| 2 · DESIGNED | C-7R.4.1 — Tier 1 shared required contract | The conditional identifier/version reference. | Requires it whenever mouth dimensions are declared. | Mouth-free modes have no such obligation. | [V10 §7R] |
| 3 · DESIGNED | C-7R.6.3.4 — Producer-validator disagreement handling | The version-bound uncertainty-rule reference. | Uses the declared handling on disagreement. | No confidence winner replaces the rule. | [V10 §7R] |
| 4 · DESIGNED | C-7R.11.7 — Disagreement uncertainty behavior rule | The declared uncertainty-rule identifier and version. | Records the rule actually governing disagreement. | The resulting state remains attributable. | [V10 §7R] |
| 5 · ACCEPTED | C-7R.15.5 — Declaration Uncertainty behavior | The required consumer-rule identifier/version for a mouth dimension. | Keeps the reference explicit without taking over local rule content. | Tier ownership and version matching remain intact. | [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| 6 · ACCEPTED | C-7R.16.7 — Future mouth-dimension declaration boundary | The required consumer-rule identifier/version for a mouth dimension. | Keeps the reference explicit without taking over local rule content. | Tier ownership and version matching remain intact. | [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |

SUB-PARTS: C-7R.10.1 — Unresolved-rule identifier reference; C-7R.10.2 — Unresolved-rule version reference; C-7R.10.3 — Local-rule change and stale-reference handling

### C-7R.10.1 — Unresolved-rule identifier reference
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The identifier of the Tier-2 handling rule. [V10 §7R]
- Takes in: DESIGNED — The nonempty rule identifier carried by Tier 1. [V10 §7R]
- Does: DESIGNED — Identifies the consumer-owned uncertainty rule. [V10 §7R]
- Gives out: DESIGNED — A specific rule reference. [V10 §7R]
- Must never: DESIGNED — Replace it with an unspecified promise to handle uncertainty. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.10 — Tier-boundary unresolved-rule reference | The rule identifier. | Checks the required reference exists. | The rule remains separately owned. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.10.2 — Unresolved-rule version reference
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The version of the Tier-2 rule referenced by Tier 1. [V10 §7R]
- Takes in: DESIGNED — The nonempty declared rule version. [V10 §7R]
- Does: DESIGNED — Binds the reference to the actual local rule version. [V10 §7R]
- Gives out: DESIGNED — A version-specific handling-rule reference. [V10 §7R]
- Must never: DESIGNED — Silently apply another rule version. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.10 — Tier-boundary unresolved-rule reference | The referenced rule version. | Checks the current binding. | Local rule changes remain detectable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.10.3 — Local-rule change and stale-reference handling
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The version relationship when the consumer changes its uncertainty rule. [V10 §7R]
- Takes in: DESIGNED — A new consumer-owned Tier-2 rule version and the existing Tier-1 reference. [V10 §7R]
- Does: DESIGNED — Requires a new Tier-2 version and an updated Tier-1 reference; detects mismatch if Tier 1 still points to the old version. [V10 §7R]
- Gives out: DESIGNED — An updated binding or a stale-reference validation result. [V10 §7R]
- Must never: DESIGNED — Silently let a changed rule inherit the old reference. [V10 §7R]
- Fails closed by: DESIGNED — A mismatch is detected by Tier-1 validation. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.10 — Tier-boundary unresolved-rule reference | The actual and referenced rule versions. | Detects staleness across the tier boundary. | Rule changes cannot remain hidden. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.11 — Relevance disagreement record
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The append-only record when a declared model validator contradicts a mouth-produced dimension. [V10 §7R]
- Takes in: DESIGNED — The separate producer and validator results, their provenance and the declared uncertainty rule. [V10 §7R]
- Does: DESIGNED — Records all nine field groups and links to both original result records. [V10 §7R]
- Gives out: DESIGNED — A stable disagreement event with its resulting dimension state. [V10 §7R]
- Must never: DESIGNED — Copy full interpretive content into this record, overwrite it, or silently choose a confidence winner. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.11.1 — Disagreement stable identifier: identifier; C-7R.11.2 — Disagreement producer-result pointer: producer-result pointer; C-7R.11.3 — Disagreement validator-result pointer: validator-result pointer; C-7R.11.4 — Disagreement type vocabulary: disagreement type; C-7R.11.5 — Disagreement producer identity and version: producer identity/version; C-7R.11.6 — Disagreement validator identity and independence: validator identity/version/independence; C-7R.11.7 — Disagreement uncertainty behavior rule: uncertainty-rule identity/version; C-7R.11.8 — Disagreement resulting dimension state: resulting state; C-7R.11.9 — Disagreement timestamp: timestamp. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R — Attention & Relevance Control (§7R) | The durable disagreement record. | Preserves the conflict without merging results. | Both outputs remain independently inspectable. | [V10 §7R] |
| 2 · DESIGNED | C-7R.6.3.4 — Producer-validator disagreement handling | The exact producer/validator conflict. | Records it before applying the declared uncertainty behavior. | Disagreement remains visible. | [V10 §7R] |
| 3 · DESIGNED | C-7R.12.12 — Evaluation disagreement presence and pointers | The separately recorded disagreements. | Carries their presence and exact references. | The evaluation event does not copy their interpretive content. | [V10 §7R] |
| 4 · ACCEPTED | C-7R.15.7 — Declaration Logging / audit requirement | The complete disagreement record contract. | Requires the separate immutable conflict record. | Auditability does not erase disagreement. | [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] |

SUB-PARTS: C-7R.11.1 — Disagreement stable identifier; C-7R.11.2 — Disagreement producer-result pointer; C-7R.11.3 — Disagreement validator-result pointer; C-7R.11.4 — Disagreement type vocabulary; C-7R.11.5 — Disagreement producer identity and version; C-7R.11.6 — Disagreement validator identity and independence; C-7R.11.7 — Disagreement uncertainty behavior rule; C-7R.11.8 — Disagreement resulting dimension state; C-7R.11.9 — Disagreement timestamp

### C-7R.11.1 — Disagreement stable identifier
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The stable identifier unique to this disagreement event. [V10 §7R]
- Takes in: DESIGNED — This disagreement’s identity. [V10 §7R]
- Does: DESIGNED — Preserves its unique reference. [V10 §7R]
- Gives out: DESIGNED — An addressable disagreement event. [V10 §7R]
- Must never: DESIGNED — Conflate distinct disagreement events. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.11 — Relevance disagreement record | The stable event identifier. | Identifies this recorded disagreement. | Other records can point to it exactly. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.11.2 — Disagreement producer-result pointer
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The exact pointer to the mouth-produced dimension-value record, including its provenance. [V10 §7R]
- Takes in: DESIGNED — The original producer result reference. [V10 §7R]
- Does: DESIGNED — Links to the separate producer record without copying its full interpretive body. [V10 §7R]
- Gives out: DESIGNED — An exact producer-result pointer. [V10 §7R]
- Must never: DESIGNED — Replace the original result with a copied paraphrase. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.11 — Relevance disagreement record | The producer’s original result reference. | Preserves the first side of the disagreement. | Its full content stays in its own record. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.11.3 — Disagreement validator-result pointer
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The exact pointer to the model validator’s output record, including provenance. [V10 §7R]
- Takes in: DESIGNED — The original validator-result reference. [V10 §7R]
- Does: DESIGNED — Links to the separate validator output. [V10 §7R]
- Gives out: DESIGNED — An exact validator-result pointer. [V10 §7R]
- Must never: DESIGNED — Merge validator and producer provenance. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.11 — Relevance disagreement record | The validator’s original output reference. | Preserves the second side separately. | Its full content stays in its own record. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.11.4 — Disagreement type vocabulary
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The declared structural nature of the conflict. [V10 §7R]
- Takes in: DESIGNED — A type from the starting vocabulary or another declared type. [V10 §7R]
- Does: DESIGNED — Classifies the conflict without deciding interpretive truth. [V10 §7R]
- Gives out: DESIGNED — value out of bounds, grounding claim contradicted, certainty exceeds support, or another declared type. [V10 §7R]
- Must never: DESIGNED — Invent an undeclared extension or use the type as final truth. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.11.4.1 — value out of bounds: value out of bounds; C-7R.11.4.2 — grounding claim contradicted: grounding claim contradicted; C-7R.11.4.3 — certainty exceeds support: certainty exceeds support. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.11 — Relevance disagreement record | The declared disagreement type. | Records the structural nature of the conflict. | Classification remains auditable. | [V10 §7R] |

SUB-PARTS: C-7R.11.4.1 — value out of bounds; C-7R.11.4.2 — grounding claim contradicted; C-7R.11.4.3 — certainty exceeds support

### C-7R.11.4.1 — value out of bounds
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The starting disagreement type for a value outside its declared bounds. [V10 §7R]
- Takes in: DESIGNED — The conflicting value and bounds. [V10 §7R]
- Does: DESIGNED — Identifies the bounds conflict. [V10 §7R]
- Gives out: DESIGNED — value out of bounds. [V10 §7R]
- Must never: DESIGNED — Treat this label as a judgment of substantive truth. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.11.4 — Disagreement type vocabulary | The bounds conflict. | Uses the declared starting type. | The structural reason remains explicit. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.11.4.2 — grounding claim contradicted
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The starting disagreement type for a contradicted grounding claim. [V10 §7R]
- Takes in: DESIGNED — The claimed grounding and the validator’s contradiction. [V10 §7R]
- Does: DESIGNED — Identifies the grounding conflict. [V10 §7R]
- Gives out: DESIGNED — grounding claim contradicted. [V10 §7R]
- Must never: DESIGNED — Silently resolve the conflict by greater model confidence. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.11.4 — Disagreement type vocabulary | The grounding contradiction. | Uses the declared starting type. | The disagreement is retained. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.11.4.3 — certainty exceeds support
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The starting disagreement type for certainty beyond grounding support. [V10 §7R]
- Takes in: DESIGNED — The certainty claim and support. [V10 §7R]
- Does: DESIGNED — Identifies the overstatement conflict. [V10 §7R]
- Gives out: DESIGNED — certainty exceeds support. [V10 §7R]
- Must never: DESIGNED — Treat confidence as additional grounding. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.11.4 — Disagreement type vocabulary | The certainty/support conflict. | Uses the declared starting type. | Unsupported strength remains visible. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.11.5 — Disagreement producer identity and version
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The mouth model, prompt version and configuration that produced the original value. [V10 §7R]
- Takes in: DESIGNED — The actual producer’s identity and production-version bindings. [V10 §7R]
- Does: DESIGNED — Retains model, prompt and configuration provenance. [V10 §7R]
- Gives out: DESIGNED — A producer identity/version account. [V10 §7R]
- Must never: DESIGNED — Attribute the value to a later or different configuration. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.2.4 — Common dimension producer provenance: canonical production identity and version provenance. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.11 — Relevance disagreement record | The original mouth model, prompt and configuration. | Identifies how the producer result arose. | The conflict is tied to the actual production setup. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.11.6 — Disagreement validator identity and independence
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The validator model/configuration, version and declared independence mechanism. [V10 §7R]
- Takes in: DESIGNED — The validator actually used and how independence was declared. [V10 §7R]
- Does: DESIGNED — Preserves identity, version and independence provenance. [V10 §7R]
- Gives out: DESIGNED — A validator-specific provenance account. [V10 §7R]
- Must never: DESIGNED — Treat an identical repeated mouth call as independent. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.6.3.1 — Model-validator declaration: declared validator/configuration; C-7R.6.3.2 — Declared validator independence: declared independence mechanism. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.11 — Relevance disagreement record | The validator identity/version and independence mechanism. | Records the actual second-result basis. | Independence is explicit rather than assumed. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.11.7 — Disagreement uncertainty behavior rule
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The identifier and version of the declared uncertainty rule from Tier 1. [V10 §7R]
- Takes in: DESIGNED — The mode’s exact uncertainty-behavior rule reference. [V10 §7R]
- Does: DESIGNED — Preserves which rule governed the response to disagreement. [V10 §7R]
- Gives out: DESIGNED — A version-bound rule reference. [V10 §7R]
- Must never: DESIGNED — Substitute an undeclared confidence-selection rule. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.10 — Tier-boundary unresolved-rule reference: the identifier/version boundary reference. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.11 — Relevance disagreement record | The uncertainty-rule identifier and version. | Records the declared handling basis. | The resulting state remains attributable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.11.8 — Disagreement resulting dimension state
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The dimension’s state after the declared uncertainty behavior was applied. [V10 §7R]
- Takes in: DESIGNED — The actual resulting dimension state. [V10 §7R]
- Does: DESIGNED — Records the outcome of that handling. [V10 §7R]
- Gives out: DESIGNED — An explicit resulting state. [V10 §7R]
- Must never: DESIGNED — Invent a resolved state merely to conceal disagreement. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.11 — Relevance disagreement record | The state after uncertainty handling. | Preserves the actual consequence. | The record reports what occurred. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.11.9 — Disagreement timestamp
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — When the disagreement was recorded. [V10 §7R]
- Takes in: DESIGNED — The actual recording timestamp. [V10 §7R]
- Does: DESIGNED — Preserves event time. [V10 §7R]
- Gives out: DESIGNED — A timestamped disagreement. [V10 §7R]
- Must never: DESIGNED — Replace the recording time with a later inspection time. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.11 — Relevance disagreement record | The disagreement timestamp. | Places the event in append-only history. | Later inspection does not rewrite it. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.12 — Completed relevance event record
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The durable append-only trace of a completed relevance evaluation. [V10 §7R]
- Takes in: DESIGNED — The actual mode/purpose/context, targets/candidates, timing, outcome counts, judgment and disagreement references. [V10 §7R]
- Does: DESIGNED — Records all thirteen field groups when the evaluation completes. [V10 §7R]
- Gives out: DESIGNED — A stable completed-evaluation event with pointers to individual results. [V10 §7R]
- Must never: DESIGNED — Overwrite the event, copy full judgments into it or create a completed-evaluation record for an evaluation that never ran. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.12.1 — Evaluation stable identifier: identifier; C-7R.12.2 — Evaluation mode identifier and version: mode/version; C-7R.12.3 — Evaluation purpose type and label: purpose/label; C-7R.12.4 — Evaluation consuming component: consumer; C-7R.12.5 — Evaluation exact context or request identifier: context/request; C-7R.12.6 — Evaluation target objects: targets; C-7R.12.7 — Evaluation candidate object type: candidate type; C-7R.12.8 — Evaluation mode: evaluation mode; C-7R.12.9 — Evaluation trigger identifier: conditional trigger; C-7R.12.10 — Evaluation outcome summary counts: five counts; C-7R.12.11 — Individual relevance-judgment pointers: judgment pointers; C-7R.12.12 — Evaluation disagreement presence and pointers: disagreement presence/pointers; C-7R.12.13 — Evaluation completion timestamp: completion timestamp. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R — Attention & Relevance Control (§7R) | The completed evaluation trace. | Preserves the durable evaluation history. | The event links to rather than replaces individual results. | [V10 §7R] |
| 2 · ACCEPTED | C-7R.15.7 — Declaration Logging / audit requirement | The completed evaluation’s full record contract. | Requires the append-only event with declaration/version and result pointers. | A completed evaluation remains traceable. | [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] |

SUB-PARTS: C-7R.12.1 — Evaluation stable identifier; C-7R.12.2 — Evaluation mode identifier and version; C-7R.12.3 — Evaluation purpose type and label; C-7R.12.4 — Evaluation consuming component; C-7R.12.5 — Evaluation exact context or request identifier; C-7R.12.6 — Evaluation target objects; C-7R.12.7 — Evaluation candidate object type; C-7R.12.8 — Evaluation mode; C-7R.12.9 — Evaluation trigger identifier; C-7R.12.10 — Evaluation outcome summary counts; C-7R.12.11 — Individual relevance-judgment pointers; C-7R.12.12 — Evaluation disagreement presence and pointers; C-7R.12.13 — Evaluation completion timestamp

### C-7R.12.1 — Evaluation stable identifier
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The stable identifier unique to this evaluation event. [V10 §7R]
- Takes in: DESIGNED — The completed evaluation’s identity. [V10 §7R]
- Does: DESIGNED — Preserves its unique reference. [V10 §7R]
- Gives out: DESIGNED — An addressable evaluation event. [V10 §7R]
- Must never: DESIGNED — Conflate distinct evaluations. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12 — Completed relevance event record | The unique evaluation identifier. | Identifies the completed event. | The trace is individually addressable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.12.2 — Evaluation mode identifier and version
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The Tier-1 mode under which the evaluation ran. [V10 §7R]
- Takes in: DESIGNED — The actual mode identifier and version. [V10 §7R]
- Does: DESIGNED — Records the configuration used. [V10 §7R]
- Gives out: DESIGNED — An exact mode/version binding. [V10 §7R]
- Must never: DESIGNED — Attribute the result to another configuration. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.4.1.1 — Tier 1 mode identity and version: the declared mode identity/version. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12 — Completed relevance event record | The applied mode and version. | Binds the event to its real configuration. | Later changes cannot rewrite its origin. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.12.3 — Evaluation purpose type and label
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The controlled purpose type and optional label from Tier 1. [V10 §7R]
- Takes in: DESIGNED — The actual purpose object used. [V10 §7R]
- Does: DESIGNED — Retains both the controlled value and any explanatory label. [V10 §7R]
- Gives out: DESIGNED — An explicit purpose record. [V10 §7R]
- Must never: DESIGNED — Let the label acquire routing or validation authority. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.9 — Tier 1 structured purpose: controlled purpose and inert optional label. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12 — Completed relevance event record | The actual purpose type and label. | Records the evaluation’s declared task. | The event remains purpose-bound. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.12.4 — Evaluation consuming component
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The component that requested or declared the evaluation. [V10 §7R]
- Takes in: DESIGNED — The actual consumer identity. [V10 §7R]
- Does: DESIGNED — Records who used this mode. [V10 §7R]
- Gives out: DESIGNED — An explicit consuming-component reference. [V10 §7R]
- Must never: DESIGNED — Transfer local-rule ownership through the event. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12 — Completed relevance event record | The requesting/declaring component. | Records the consumer. | The local owner remains identifiable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.12.5 — Evaluation exact context or request identifier
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The identifier of the specific context or request instance. [V10 §7R]
- Takes in: DESIGNED — The actual request/context identity. [V10 §7R]
- Does: DESIGNED — Binds the event to that instance. [V10 §7R]
- Gives out: DESIGNED — An exact context/request reference. [V10 §7R]
- Must never: DESIGNED — Use only a generic mode label in place of the actual instance. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12 — Completed relevance event record | The exact request or context identifier. | Retains the instance evaluated. | The result cannot silently become global. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.12.6 — Evaluation target objects
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The target object or objects against which candidates were evaluated. [V10 §7R]
- Takes in: DESIGNED — Each target’s object type and identifier. [V10 §7R]
- Does: DESIGNED — Preserves type and identity for every target. [V10 §7R]
- Gives out: DESIGNED — Typed target references. [V10 §7R]
- Must never: DESIGNED — Copy a target’s full content into this field or substitute another identity. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.12.6.1 — Evaluation target object type: target type; C-7R.12.6.2 — Evaluation target object identifier: target identifier. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12 — Completed relevance event record | Every target’s type and identifier. | Records the comparison targets. | Object references remain exact. | [V10 §7R] |

SUB-PARTS: C-7R.12.6.1 — Evaluation target object type; C-7R.12.6.2 — Evaluation target object identifier

### C-7R.12.6.1 — Evaluation target object type
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The type of each target recorded by the evaluation. [V10 §7R]
- Takes in: DESIGNED — The actual target’s object type. [V10 §7R]
- Does: DESIGNED — Preserves that type beside its identifier. [V10 §7R]
- Gives out: DESIGNED — A typed target reference. [V10 §7R]
- Must never: DESIGNED — Strip type from the object reference. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12.6 — Evaluation target objects | The target type. | Records each target’s kind. | The reference remains typed. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.12.6.2 — Evaluation target object identifier
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The identifier of each target recorded by the evaluation. [V10 §7R]
- Takes in: DESIGNED — The exact target identity. [V10 §7R]
- Does: DESIGNED — Preserves that identity beside its type. [V10 §7R]
- Gives out: DESIGNED — An exact target reference. [V10 §7R]
- Must never: DESIGNED — Replace identity with a content summary. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12.6 — Evaluation target objects | The target identifier. | Records the actual evaluated target. | The comparison object remains traceable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.12.7 — Evaluation candidate object type
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The declared type of candidates evaluated. [V10 §7R]
- Takes in: DESIGNED — The mode’s candidate-type declaration. [V10 §7R]
- Does: DESIGNED — Records that type in the evaluation event. [V10 §7R]
- Gives out: DESIGNED — A candidate object-type field. [V10 §7R]
- Must never: DESIGNED — Pretend undeclared candidate types were evaluated under the declaration. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12 — Completed relevance event record | The declared candidate type. | Preserves the evaluation scope. | Type scope remains auditable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.12.8 — Evaluation mode
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Whether this evaluation ran on demand or through triggered precomputation. [V10 §7R]
- Takes in: DESIGNED — The actual evaluation form. [V10 §7R]
- Does: DESIGNED — Records which of those two forms occurred. [V10 §7R]
- Gives out: DESIGNED — on demand or triggered pre-computation. [V10 §7R]
- Must never: DESIGNED — Describe a triggered cached calculation as a fresh on-demand result. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12 — Completed relevance event record | The actual evaluation form. | Preserves its timing provenance. | Precomputation remains distinguishable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.12.9 — Evaluation trigger identifier
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The trigger-event identifier when triggered precomputation was used. [V10 §7R]
- Takes in: DESIGNED — The actual triggering event reference, conditional on that evaluation form. [V10 §7R]
- Does: DESIGNED — Records the trigger for precomputed evaluations. [V10 §7R]
- Gives out: DESIGNED — A trigger identifier where applicable. [V10 §7R]
- Must never: DESIGNED — Invent a trigger for an ordinary on-demand evaluation. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12 — Completed relevance event record | The applicable trigger-event identifier. | Records why precomputation occurred. | Conditional provenance remains honest. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.12.10 — Evaluation outcome summary counts
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Five candidate-count summaries of the completed evaluation. [V10 §7R]
- Takes in: DESIGNED — The actual gate results, dimension states and disagreement records. [V10 §7R]
- Does: DESIGNED — Counts candidates by each stated outcome; the unresolved/failed/disagreement categories mean one or more such results for the candidate. [V10 §7R]
- Gives out: DESIGNED — Five separate counts, not a hidden score. [V10 §7R]
- Must never: DESIGNED — Replace candidate counts with dimension counts or hide an unresolved/failed category. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.12.10.1 — Gate-passed candidate count: gate-passed; C-7R.12.10.2 — Gate-excluded candidate count: gate-excluded; C-7R.12.10.3 — Unresolved-dimension candidate count: unresolved; C-7R.12.10.4 — Failed-dimension candidate count: failed; C-7R.12.10.5 — Disagreement-producing candidate count: disagreement-producing. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12 — Completed relevance event record | The five actual candidate counts. | Summarizes outcomes without replacing judgments. | Uncertainty and exclusion remain visible. | [V10 §7R] |

SUB-PARTS: C-7R.12.10.1 — Gate-passed candidate count; C-7R.12.10.2 — Gate-excluded candidate count; C-7R.12.10.3 — Unresolved-dimension candidate count; C-7R.12.10.4 — Failed-dimension candidate count; C-7R.12.10.5 — Disagreement-producing candidate count

### C-7R.12.10.1 — Gate-passed candidate count
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The number of candidates that passed the context gate. [V10 §7R]
- Takes in: DESIGNED — Actual candidate gate outcomes. [V10 §7R]
- Does: DESIGNED — Counts candidates passing the required gate. [V10 §7R]
- Gives out: DESIGNED — A passed-candidate count. [V10 §7R]
- Must never: DESIGNED — Count a gate-excluded candidate as passing. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12.10 — Evaluation outcome summary counts | The passed-candidate count. | Records the passing population. | Gate outcome remains explicit. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.12.10.2 — Gate-excluded candidate count
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The number of candidates excluded by the context gate. [V10 §7R]
- Takes in: DESIGNED — Actual candidate exclusions. [V10 §7R]
- Does: DESIGNED — Counts excluded candidates. [V10 §7R]
- Gives out: DESIGNED — An excluded-candidate count. [V10 §7R]
- Must never: DESIGNED — Hide exclusions in a lower aggregate score. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12.10 — Evaluation outcome summary counts | The excluded-candidate count. | Records categorical exclusions. | Ungraded exclusions remain visible. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.12.10.3 — Unresolved-dimension candidate count
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The number of candidates with one or more unresolved dimensions. [V10 §7R]
- Takes in: DESIGNED — The candidate-linked dimension states. [V10 §7R]
- Does: DESIGNED — Counts candidates having at least one Unresolved dimension. [V10 §7R]
- Gives out: DESIGNED — An unresolved-candidate count. [V10 §7R]
- Must never: DESIGNED — Count each unresolved dimension as a separate candidate. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12.10 — Evaluation outcome summary counts | Candidates with at least one unresolved dimension. | Records the unresolved population. | The count measures candidates. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.12.10.4 — Failed-dimension candidate count
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The number of candidates with one or more failed dimensions. [V10 §7R]
- Takes in: DESIGNED — The candidate-linked dimension failures. [V10 §7R]
- Does: DESIGNED — Counts candidates having at least one Failed dimension. [V10 §7R]
- Gives out: DESIGNED — A failed-candidate count. [V10 §7R]
- Must never: DESIGNED — Conceal failed dimensions by omitting the candidate category. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12.10 — Evaluation outcome summary counts | Candidates with at least one failed dimension. | Records the failed population. | Failure remains inspectable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.12.10.5 — Disagreement-producing candidate count
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The number of candidates producing one or more disagreement records. [V10 §7R]
- Takes in: DESIGNED — The candidate-linked disagreement events. [V10 §7R]
- Does: DESIGNED — Counts each candidate with at least one disagreement. [V10 §7R]
- Gives out: DESIGNED — A disagreement-candidate count. [V10 §7R]
- Must never: DESIGNED — Substitute disagreement-record count for candidate count. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12.10 — Evaluation outcome summary counts | Candidates with one or more disagreements. | Records the affected population. | The count retains its stated unit. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.12.11 — Individual relevance-judgment pointers
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — One pointer for each individual relevance judgment produced. [V10 §7R]
- Takes in: DESIGNED — The exact judgment-record references. [V10 §7R]
- Does: DESIGNED — Links each produced judgment; full judgment content remains in its own record. [V10 §7R]
- Gives out: DESIGNED — One pointer per judgment. [V10 §7R]
- Must never: DESIGNED — Copy full judgment bodies into the evaluation event. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12 — Completed relevance event record | All individual judgment pointers. | Links to the full results separately. | The event does not duplicate their content. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.12.12 — Evaluation disagreement presence and pointers
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Whether any disagreement records were created, with their pointers when present. [V10 §7R]
- Takes in: DESIGNED — The actual disagreement presence and exact references. [V10 §7R]
- Does: DESIGNED — Records the presence fact and links to every applicable disagreement. [V10 §7R]
- Gives out: DESIGNED — A disagreement indication with references if present. [V10 §7R]
- Must never: DESIGNED — Hide existing disagreement or fabricate one. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.11 — Relevance disagreement record: separately owned disagreement records. C-7R.12.12.1 — Evaluation disagreement-presence fact: disagreement presence; C-7R.12.12.2 — Evaluation disagreement-record pointers: conditional references. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12 — Completed relevance event record | Disagreement presence and references. | Preserves the evaluation’s uncertainty trace. | Separate conflicts remain inspectable. | [V10 §7R] |

SUB-PARTS: C-7R.12.12.1 — Evaluation disagreement-presence fact; C-7R.12.12.2 — Evaluation disagreement-record pointers

### C-7R.12.12.1 — Evaluation disagreement-presence fact
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Whether any disagreement records were created. [V10 §7R]
- Takes in: DESIGNED — The actual presence or absence of disagreement records. [V10 §7R]
- Does: DESIGNED — Preserves that fact explicitly. [V10 §7R]
- Gives out: DESIGNED — A disagreement-presence indication. [V10 §7R]
- Must never: DESIGNED — Hide a created disagreement. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12.12 — Evaluation disagreement presence and pointers | Whether disagreements exist. | Records the presence fact. | The event cannot conceal conflict. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.12.12.2 — Evaluation disagreement-record pointers
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Pointers to disagreement records when they exist. [V10 §7R]
- Takes in: DESIGNED — The exact applicable disagreement references. [V10 §7R]
- Does: DESIGNED — Links to those separate records. [V10 §7R]
- Gives out: DESIGNED — Conditional disagreement pointers. [V10 §7R]
- Must never: DESIGNED — Replace the records with an unsupported conflict summary. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12.12 — Evaluation disagreement presence and pointers | The actual disagreement references. | Retains their separate identities. | Full conflicts remain inspectable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.12.13 — Evaluation completion timestamp
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — When the relevance evaluation completed. [V10 §7R]
- Takes in: DESIGNED — The actual completion time. [V10 §7R]
- Does: DESIGNED — Records completion rather than request or later inspection time. [V10 §7R]
- Gives out: DESIGNED — A completion timestamp. [V10 §7R]
- Must never: DESIGNED — Claim completion for an evaluation that did not run. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.12 — Completed relevance event record | The evaluation completion time. | Dates the completed event. | The timestamp reflects the actual completed work. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.13 — Per-judgment override pattern observation
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — A possible mode-change observation permitted only when three pattern conditions hold together. [V10 §7R]
- Takes in: DESIGNED — Recorded overrides for one mode/version, one gate/dimension/outcome target and a consistent correction direction. [V10 §7R]
- Does: DESIGNED — Shows the exact pattern and a mode change as one possibility; explicitly permits treating each correction as a correct contextual response rather than systematic mode error. [V10 §7R]
- Gives out: DESIGNED — An observation remaining open until Ness explicitly acts or dismisses it. [V10 §7R]
- Must never: DESIGNED — Recommend the change as required, infer dismissal from silence or automatically change the mode. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.13.1 — Three simultaneous override-pattern conditions: simultaneous conditions; C-7R.13.2 — Override-pattern presentation limits: complete presentation; C-7R.13.3 — Override observation remains open: open state; C-7R.13.4 — Explicit dismissal and qualified resurfacing: dismissal and resurfacing. [V10 §7R]
- Gated by: DESIGNED — C-7R.5.4 — Reusable mode change: any permanent change still requires full consequence preview and confirmation. [V10 §7R]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R — Attention & Relevance Control (§7R) | An explicitly qualified override pattern. | Keeps the observation distinct from mode policy. | No automatic adaptation follows. | [V10 §7R] |

SUB-PARTS: C-7R.13.1 — Three simultaneous override-pattern conditions; C-7R.13.2 — Override-pattern presentation limits; C-7R.13.3 — Override observation remains open; C-7R.13.4 — Explicit dismissal and qualified resurfacing

### C-7R.13.1 — Three simultaneous override-pattern conditions
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The conjunctive conditions required before surfacing the observation. [V10 §7R]
- Takes in: DESIGNED — The recorded overrides’ mode/version, target and correction direction. [V10 §7R]
- Does: DESIGNED — Requires all three conditions at once. [V10 §7R]
- Gives out: DESIGNED — A qualifying pattern only where all three match. [V10 §7R]
- Must never: DESIGNED — Surface the mode-change observation from an unrelated mixture of overrides. [V10 §7R]
- Fails closed by: DESIGNED — The observation is not permitted when a required condition is absent. [V10 §7R]

TOGETHER
- Fed by: DESIGNED — C-7R.13.1.1 — Same override mode and version: same mode/version; C-7R.13.1.2 — Same override target: same target; C-7R.13.1.3 — Same correction direction: same direction. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.13 — Per-judgment override pattern observation | All three pattern predicates. | Surfaces only a qualifying observation. | Unrelated corrections do not become a mode-error claim. | [V10 §7R] |

SUB-PARTS: C-7R.13.1.1 — Same override mode and version; C-7R.13.1.2 — Same override target; C-7R.13.1.3 — Same correction direction

### C-7R.13.1.1 — Same override mode and version
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The requirement that the overrides concern one mode identifier and version. [V10 §7R]
- Takes in: DESIGNED — Their exact mode/version references. [V10 §7R]
- Does: DESIGNED — Checks equality of both identity and version. [V10 §7R]
- Gives out: DESIGNED — A same-mode/version predicate. [V10 §7R]
- Must never: DESIGNED — Combine different versions as if they were the same configuration. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.13.1 — Three simultaneous override-pattern conditions | The mode/version match. | Requires it alongside the other two predicates. | Configuration scope remains exact. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.13.1.2 — Same override target
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The requirement that the overrides concern the same gate condition, dimension or outcome type. [V10 §7R]
- Takes in: DESIGNED — Their recorded correction targets. [V10 §7R]
- Does: DESIGNED — Checks that target identity is the same. [V10 §7R]
- Gives out: DESIGNED — A same-target predicate. [V10 §7R]
- Must never: DESIGNED — Blend different targets into a systematic pattern. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.13.1 — Three simultaneous override-pattern conditions | The target match. | Requires it with matching mode/version and direction. | The observed pattern concerns one target. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.13.1.3 — Same correction direction
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The requirement that the overrides consistently point in the same direction of correction. [V10 §7R]
- Takes in: DESIGNED — Their actual directions. [V10 §7R]
- Does: DESIGNED — Checks directional consistency. [V10 §7R]
- Gives out: DESIGNED — A same-direction predicate. [V10 §7R]
- Must never: DESIGNED — Treat opposing directions as one consistent correction pattern. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.13.1 — Three simultaneous override-pattern conditions | The direction match. | Requires consistent correction. | A mixed pattern does not qualify. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.13.2 — Override-pattern presentation limits
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The complete required wording boundary for a qualifying observation. [V10 §7R]
- Takes in: DESIGNED — The exact observed pattern and its possible implications. [V10 §7R]
- Does: DESIGNED — Shows the pattern; presents a mode change only as a possibility; states that the individual corrections may be correct contextual responses without indicating systematic error. [V10 §7R]
- Gives out: DESIGNED — An optional mode-change possibility with the contextual alternative explicit. [V10 §7R]
- Must never: DESIGNED — Turn the observation into a recommendation or a conclusion that the mode is wrong. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.13 — Per-judgment override pattern observation | The qualified observation and contextual alternative. | Surfaces the exact pattern without prescribing change. | Ness retains interpretation and choice. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.13.3 — Override observation remains open
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The state before Ness explicitly acts on or dismisses the observation. [V10 §7R]
- Takes in: DESIGNED — A surfaced observation and any silence or lack of immediate action. [V10 §7R]
- Does: DESIGNED — Keeps it open until an explicit act or dismissal. [V10 §7R]
- Gives out: DESIGNED — An open observation. [V10 §7R]
- Must never: DESIGNED — Interpret silence or no immediate action as dismissal. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.13 — Per-judgment override pattern observation | The absence of explicit disposition. | Retains open status. | Non-response does not decide the observation. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.13.4 — Explicit dismissal and qualified resurfacing
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Closure by explicit dismissal and the limited condition for later resurfacing. [V10 §7R]
- Takes in: DESIGNED — Ness’s explicit dismissal and any later new overrides or material change to the evidence base. [V10 §7R]
- Does: DESIGNED — Closes the observation; does not surface the same pattern again unless new overrides appear or the evidence materially changes. [V10 §7R]
- Gives out: DESIGNED — A closed observation, with resurfacing permitted only under the stated new condition. [V10 §7R]
- Must never: DESIGNED — Treat unchanged repetition as a new pattern or automatically change the mode. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.13 — Per-judgment override pattern observation | The explicit dismissal and any genuinely changed evidence. | Suppresses unchanged resurfacing. | Only a new qualifying basis can reopen attention. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.14 — Unrecognized purpose-type halt
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Correct fail-closed behavior when the declared type is absent from the current controlled vocabulary. [V10 §7R]
- Takes in: DESIGNED — The unknown type, checked vocabulary version and full original configuration/context. [V10 §7R]
- Does: DESIGNED — Halts immediately, identifies the exact unknown value/version, preserves the request, explains plainly and offers confirmed mapping or a versioned new-type proposal. [V10 §7R]
- Gives out: DESIGNED — A separate append-only halt event, not a completed relevance-evaluation event. [V10 §7R]
- Must never: DESIGNED — Evaluate gates or dimensions, guess a purpose, substitute a close match or claim an evaluation ran. [V10 §7R]
- Fails closed by: DESIGNED — Runs no evaluation until an explicitly confirmed valid purpose path permits it. [V10 §7R]

TOGETHER
- Fed by: DESIGNED — C-7R.14.1 — Unknown-purpose immediate stop: immediate stop; C-7R.14.2 — Unknown-purpose exact diagnosis: exact diagnosis; C-7R.14.3 — Unknown-purpose original-request preservation: request preservation; C-7R.14.4 — Unknown-purpose plain explanation: explanation; C-7R.14.5 — Explicitly confirmed existing-purpose mapping: confirmed mapping; C-7R.14.6 — New-purpose proposal path: new-type proposal; C-7R.14.7 — Unknown-purpose halt event: halt event. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R — Attention & Relevance Control (§7R) | The unknown controlled type. | Stops evaluation without guessing. | A correct halt leaves an honest separate event. | [V10 §7R] |
| 2 · DESIGNED | C-7R.4.1 — Tier 1 shared required contract | An unrecognized purpose in the declaration. | Withholds mode acceptance and evaluation. | No label silently supplies a replacement. | [V10 §7R] |
| 3 · DESIGNED | C-7R.9 — Tier 1 structured purpose | The failed vocabulary membership check. | Uses the explicit halt path. | The original request is retained. | [V10 §7R] |
| 4 · ACCEPTED | C-7R.15 — Mandatory per-task relevance declaration policy | An unrecognized controlled purpose. | Halts without gates, dimensions or a false completion event. | The request is preserved for explicit mapping or a new-type proposal. | [V10 §7R] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §5] |
| 5 · ACCEPTED | C-7R.15.2 — Declaration Task or purpose | An unrecognized controlled purpose. | Halts without gates, dimensions or a false completion event. | The request is preserved for explicit mapping or a new-type proposal. | [V10 §7R] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §5] |
| 6 · ACCEPTED | C-7R.15.8 — Declaration Fail-closed behavior when relevance cannot be safely determined | An unrecognized controlled purpose. | Halts without gates, dimensions or a false completion event. | The request is preserved for explicit mapping or a new-type proposal. | [V10 §7R] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §5] |
| 7 · ACCEPTED | C-7R.17 — Live relevance query interface | The unrecognized purpose in a live request. | Refuses and records it without guessing a mapping. | The router cannot invent relevance authority. | [V10 §7R] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 8 · ACCEPTED | C-LMAC.10.5 — Unrecognized-purpose refusal | The unknown purpose supplied by the caller. | Supplies the canonical full unknown-relevance-purpose halt and explicit resolution paths. | Nothing in this card. | [V10 §7R] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 9 · DESIGNED | C-LEARN.5.1 — Personalization domain guides query purpose | The personalization domain and current shared material. | Supplies unrecognized-purpose handling. | Nothing in this card. | [V10 §26.8] [V10 §7R] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |

SUB-PARTS: C-7R.14.1 — Unknown-purpose immediate stop; C-7R.14.2 — Unknown-purpose exact diagnosis; C-7R.14.3 — Unknown-purpose original-request preservation; C-7R.14.4 — Unknown-purpose plain explanation; C-7R.14.5 — Explicitly confirmed existing-purpose mapping; C-7R.14.6 — New-purpose proposal path; C-7R.14.7 — Unknown-purpose halt event

### C-7R.14.1 — Unknown-purpose immediate stop
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The no-evaluation boundary at an unrecognized purpose. [V10 §7R]
- Takes in: DESIGNED — The failed controlled-vocabulary membership check. [V10 §7R]
- Does: DESIGNED — Halts before gates and dimension computation. [V10 §7R]
- Gives out: DESIGNED — No gate result, dimension computation or completed relevance-event record for the unrun evaluation. [V10 §7R]
- Must never: DESIGNED — Pretend a halted evaluation completed. [V10 §7R]
- Fails closed by: DESIGNED — Stops immediately; the separate halt event records the refusal to evaluate. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.14 — Unrecognized purpose-type halt | The unknown type. | Stops all evaluation work immediately. | Only halt history is created. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.14.2 — Unknown-purpose exact diagnosis
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The exact value and vocabulary version that failed recognition. [V10 §7R]
- Takes in: DESIGNED — The unknown type and checked vocabulary version. [V10 §7R]
- Does: DESIGNED — Names both precisely. [V10 §7R]
- Gives out: DESIGNED — An exact diagnosis of the mismatch. [V10 §7R]
- Must never: DESIGNED — Guess a close-match substitute. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.14 — Unrecognized purpose-type halt | The unknown value and checked version. | Explains the precise mismatch. | The rejected configuration remains identifiable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.14.3 — Unknown-purpose original-request preservation
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — Retention of the full original configuration and the context that produced the request. [V10 §7R]
- Takes in: DESIGNED — The original request and its context. [V10 §7R]
- Does: DESIGNED — Preserves both without modification. [V10 §7R]
- Gives out: DESIGNED — The complete original request/context. [V10 §7R]
- Must never: DESIGNED — Rewrite the request to match an approved purpose silently. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.14 — Unrecognized purpose-type halt | The unchanged request and originating context. | Preserves what was actually requested. | A later mapping cannot erase the original. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.14.4 — Unknown-purpose plain explanation
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The required plain-language account of the halt. [V10 §7R]
- Takes in: DESIGNED — The unrecognized type and its effect on evaluation. [V10 §7R]
- Does: DESIGNED — States that the type is not recognized, what that means and why evaluation cannot proceed. [V10 §7R]
- Gives out: DESIGNED — An understandable halt explanation. [V10 §7R]
- Must never: DESIGNED — Dismiss the request without explanation. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.14 — Unrecognized purpose-type halt | The exact halt reason. | Explains the problem plainly. | The stop remains reviewable. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.14.5 — Explicitly confirmed existing-purpose mapping
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The path that maps the request to an existing approved controlled type. [V10 §7R]
- Takes in: DESIGNED — A proposed existing-type mapping and Ness’s explicit confirmation. [V10 §7R]
- Does: DESIGNED — Uses the mapped type only after that confirmation. [V10 §7R]
- Gives out: DESIGNED — An explicitly authorized mapping before evaluation. [V10 §7R]
- Must never: DESIGNED — Treat a close match as permission to substitute. [V10 §7R]
- Fails closed by: DESIGNED — No evaluation runs under the mapping before explicit confirmation. [V10 §7R]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — Ness’s explicit confirmation of the specific mapping is required before evaluation. [V10 §7R]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.14 — Unrecognized purpose-type halt | The approved existing type and explicit mapping confirmation. | Permits the mapped evaluation only afterward. | No silent purpose substitution occurs. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.14.6 — New-purpose proposal path
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The path proposing a new controlled purpose type. [V10 §7R]
- Takes in: DESIGNED — The intended new type and its consequences. [V10 §7R]
- Does: DESIGNED — Uses consequence preview, Ness confirmation and vocabulary versioning. [V10 §7R]
- Gives out: DESIGNED — A confirmed new controlled type in a new version, where approved. [V10 §7R]
- Must never: DESIGNED — Add a type by informal label or silent guess. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7R.5.4 — Reusable mode change: the full versioned reusable-change process. [V10 §7R]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.14 — Unrecognized purpose-type halt | The versioned new-type proposal. | Retains the controlled-vocabulary change process. | New evaluation authority is explicit. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.14.7 — Unknown-purpose halt event
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The separate append-only trace of a correctly halted evaluation request. [V10 §7R]
- Takes in: DESIGNED — The unknown type, preserved original request and timestamp. [V10 §7R]
- Does: DESIGNED — Records those three fields without pretending the evaluation ran. [V10 §7R]
- Gives out: DESIGNED — An immutable halt event. [V10 §7R]
- Must never: DESIGNED — Treat the halt as component failure or as a completed relevance evaluation. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.14.7.1 — Halt-event unknown type: unknown type; C-7R.14.7.2 — Halt-event preserved request: preserved request; C-7R.14.7.3 — Halt-event timestamp: timestamp. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.14 — Unrecognized purpose-type halt | The exact halt trace. | Preserves the correct refusal to evaluate. | History distinguishes halt from completed evaluation. | [V10 §7R] |

SUB-PARTS: C-7R.14.7.1 — Halt-event unknown type; C-7R.14.7.2 — Halt-event preserved request; C-7R.14.7.3 — Halt-event timestamp

### C-7R.14.7.1 — Halt-event unknown type
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The unrecognized type recorded by the halt event. [V10 §7R]
- Takes in: DESIGNED — The exact supplied type value. [V10 §7R]
- Does: DESIGNED — Preserves the unknown value. [V10 §7R]
- Gives out: DESIGNED — An explicit unknown-type field. [V10 §7R]
- Must never: DESIGNED — Replace it with a guessed approved value. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.14.7 — Unknown-purpose halt event | The exact unknown type. | Records what could not be evaluated. | The original mismatch survives. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.14.7.2 — Halt-event preserved request
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — The original request retained with the halt event. [V10 §7R]
- Takes in: DESIGNED — The full preserved configuration and originating context. [V10 §7R]
- Does: DESIGNED — Retains that unchanged request. [V10 §7R]
- Gives out: DESIGNED — An auditable original request. [V10 §7R]
- Must never: DESIGNED — Erase it after later mapping or proposal. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.14.7 — Unknown-purpose halt event | The preserved request. | Records the original context of the halt. | Later action cannot rewrite the request. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.14.7.3 — Halt-event timestamp
Stamp: DESIGNED    Source: [V10 §7R]

ALONE
- What it is: DESIGNED — When the unknown-purpose halt occurred. [V10 §7R]
- Takes in: DESIGNED — The actual halt timestamp. [V10 §7R]
- Does: DESIGNED — Preserves event time. [V10 §7R]
- Gives out: DESIGNED — A timestamped halt. [V10 §7R]
- Must never: DESIGNED — Substitute the time of a later successful evaluation. [V10 §7R]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R.14.7 — Unknown-purpose halt event | The halt timestamp. | Dates the separate event. | Halt and later evaluation remain distinct. | [V10 §7R] |

SUB-PARTS: NONE

### C-7R.15 — Mandatory per-task relevance declaration policy
Stamp: ACCEPTED    Source: [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §1] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §2] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — Accepted Option C: one shared relevance language and a mandatory declaration for every consuming component’s relevance-using task. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §1] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §2] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Takes in: ACCEPTED — The component, task, selected mode, reason, uncertainty behavior, use boundary, audit requirement and fail-closed behavior. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §1] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §2] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Does: ACCEPTED — Requires all eight policy fields, binds them to the settled two-tier contract and preserves each declaration as a versioned append-only record. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §1] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §2] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Gives out: ACCEPTED — A valid per-task declaration or no relevance mode to run. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §1] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §2] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Must never: ACCEPTED — Invent a private relevance meaning, omit the recorded reason, silently edit a declaration or make Ness approve routine individual judgments. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §1] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §2] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — A missing required field or invalid current-purpose declaration means no mode runs; the owner follows its honest failure path. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §1] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §2] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]

TOGETHER
- Fed by: ACCEPTED — C-7R.15.1 — Declaration Component name / id: component/version; C-7R.15.2 — Declaration Task or purpose: task/purpose; C-7R.15.3 — Declaration Selected relevance mode: selected mode; C-7R.15.4 — Declaration Reason for that mode: reason; C-7R.15.5 — Declaration Uncertainty behavior: uncertainty behavior; C-7R.15.6 — Declaration Allowed retrieval/use boundary: allowed use; C-7R.15.7 — Declaration Logging / audit requirement: audit; C-7R.15.8 — Declaration Fail-closed behavior when relevance cannot be safely determined: honest fail-closed behavior. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §1] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §2] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Gated by: DESIGNED — C-7R.4 — Two-tier configuration contract: settled tier ownership; C-7R.14 — Unrecognized purpose-type halt: unknown-purpose halt. [V10 §7R] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §2]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R — Attention & Relevance Control (§7R) | The complete valid current-purpose declaration. | Runs only the declared relevance mode. | No component improvises a missing mode. | [V10 §7R] |

SUB-PARTS: C-7R.15.1 — Declaration Component name / id; C-7R.15.2 — Declaration Task or purpose; C-7R.15.3 — Declaration Selected relevance mode; C-7R.15.4 — Declaration Reason for that mode; C-7R.15.5 — Declaration Uncertainty behavior; C-7R.15.6 — Declaration Allowed retrieval/use boundary; C-7R.15.7 — Declaration Logging / audit requirement; C-7R.15.8 — Declaration Fail-closed behavior when relevance cannot be safely determined

### C-7R.15.1 — Declaration Component name / id
Stamp: ACCEPTED    Source: [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The stably identified component with the declaration’s own version. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Takes in: ACCEPTED — The component name/id and declaration version. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Does: ACCEPTED — Records which consumer owns the declaration and its exact version. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Gives out: ACCEPTED — A versioned component declaration identity. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Must never: ACCEPTED — Let another component inherit the declaration silently. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7R.15 — Mandatory per-task relevance declaration policy | The component identity and declaration version. | Requires the policy field. | The consumer remains stably identified. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7R.15.2 — Declaration Task or purpose
Stamp: ACCEPTED    Source: [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The controlled task type with an optional behaviorally inert explanatory label. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Takes in: ACCEPTED — One recognized purpose type and optional label. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Does: ACCEPTED — Declares the task under the settled shared vocabulary. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Gives out: ACCEPTED — A task-specific purpose binding. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Must never: ACCEPTED — Guess an unknown purpose or give label wording behavioral force. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.9 — Tier 1 structured purpose: exact purpose structure and five values. [V10 §7R]
- Gated by: DESIGNED — C-7R.14 — Unrecognized purpose-type halt: unrecognized type follows the halt path. [V10 §7R]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7R.15 — Mandatory per-task relevance declaration policy | The task’s controlled purpose. | Requires its explicit declaration. | Task scope cannot be improvised. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7R.15.3 — Declaration Selected relevance mode
Stamp: ACCEPTED    Source: [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The selected mode identifier/version under the two-tier contract. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Takes in: ACCEPTED — The Tier-1 declaration and consumer-owned Tier-2 rules. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Does: ACCEPTED — Retains shared relevance validation of Tier 1 and consumer validation of Tier 2. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Gives out: ACCEPTED — A mode/version with both owners intact. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Must never: ACCEPTED — Move either tier’s validation silently to the other owner. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.4 — Two-tier configuration contract: the settled shared/local contract. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7R.15 — Mandatory per-task relevance declaration policy | The selected mode and its two-tier ownership. | Requires a properly bound mode. | No unspecified relevance policy runs. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7R.15.4 — Declaration Reason for that mode
Stamp: ACCEPTED    Source: [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — A plain recorded statement of why the selected mode fits the task. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Takes in: ACCEPTED — The actual mode-selection reason. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Does: ACCEPTED — Preserves that reason as a required declaration field. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Gives out: ACCEPTED — An inspectable task/mode rationale. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Must never: ACCEPTED — Treat a declaration without a reason as valid. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — A missing reason makes the declaration invalid. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7R.15 — Mandatory per-task relevance declaration policy | The plain recorded reason. | Requires an explicit mode/task rationale. | Selection is auditable. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7R.15.5 — Declaration Uncertainty behavior
Stamp: ACCEPTED    Source: [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The consumer’s declared treatment of excluded candidates, unresolved or failed dimensions and producer-validator disagreement. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Takes in: ACCEPTED — Those outcomes and the consumer-owned uncertainty rule. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Does: ACCEPTED — States what happens to each; whenever mouth dimensions are declared, carries the required Tier-2 rule identifier/version in Tier 1. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Gives out: ACCEPTED — Recorded uncertainty handling, never silent smoothing. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Must never: ACCEPTED — Hide uncertainty or substitute an undeclared handling rule. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.6 — Mouth-produced dimension validation: settled validation outcomes; C-7R.10 — Tier-boundary unresolved-rule reference: conditional identifier/version reference. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7R.15 — Mandatory per-task relevance declaration policy | The declared uncertainty handling. | Requires explicit outcomes for uncertain relevance. | Uncertainty remains governed by its owner. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7R.15.6 — Declaration Allowed retrieval/use boundary
Stamp: ACCEPTED    Source: [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The eligible source scope and use limits for the declared purpose. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §4]
- Takes in: ACCEPTED — The prior purpose-specific privacy authorization and consumer’s settled boundaries. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §4]
- Does: ACCEPTED — Narrows the material the mode may reach and use; never expands eligibility. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §4]
- Gives out: ACCEPTED — An explicit narrower use boundary. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §4]
- Must never: ACCEPTED — Make ineligible material eligible, reveal withheld material or signal that it exists. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): correct internal-use or visible-output authorization precedes candidates; C-SACL — Speaker Access-Control Layer (§25.4): visible output retains privacy first and speaker access second. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7R.15 — Mandatory per-task relevance declaration policy | The permitted source/use scope. | Keeps declarations within prior authorization. | Relevance cannot widen access. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7R.15.7 — Declaration Logging / audit requirement
Stamp: ACCEPTED    Source: [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]

ALONE
- What it is: ACCEPTED — Auditability of the declaration and every evaluation under it. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Takes in: ACCEPTED — The actual declaration identity/version, evaluation and disagreement events. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Does: ACCEPTED — Uses append-only records and the one-real-operation/one-log rule; preserves declaration versions and governs changes by consequence preview and confirmation. The Log surface stays look-don’t-touch. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Gives out: ACCEPTED — Inspectable declaration and evaluation history. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Must never: ACCEPTED — Silently edit a declaration, treat logs as truth evidence, double-count derived support or make routine inspection mandatory. Repetition adds no certainty, and derived material is not independent evidence for the interpretation that produced it. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7R.11 — Relevance disagreement record: disagreement fields; C-7R.12 — Completed relevance event record: completed-event fields; C-7R.5 — Ness inspection, correction and configuration changes: inspection/correction/override/version paths; C-7B.10.5.1 — One real operation one log: one real operation one log. [V10 §7R] [V10 §0B] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): all record access remains authorized; C-SIA — Speaker Identity Assessment (§25.3): applicable identity/security authorization remains in force. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7R.15 — Mandatory per-task relevance declaration policy | The declaration and actual evaluation history. | Requires auditable append-only records. | History does not become evidence of truth. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] |

SUB-PARTS: NONE

### C-7R.15.8 — Declaration Fail-closed behavior when relevance cannot be safely determined
Stamp: ACCEPTED    Source: [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]

ALONE
- What it is: ACCEPTED — The owner-governed honest path for unknown purpose, invalid/missing declaration, incomplete evaluation or unresolved disagreement. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Takes in: ACCEPTED — The exact failure or uncertainty and the owning component’s settled rules. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Does: ACCEPTED — Records it and halts or proceeds explicitly degraded only where that owner’s rules allow; marks degraded, context-limited or insufficient outcomes honestly. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Gives out: ACCEPTED — An honest stopped or expressly allowed degraded result. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Must never: ACCEPTED — Guess, lower a threshold silently, substitute unrelated material or pretend success. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Fails closed by: ACCEPTED — Uses only the owner-authorized stop/degraded path; retrieval-system failure has the stricter terminal-stop rule. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]

TOGETHER
- Fed by: ACCEPTED — C-7R.15.8.1 — Retrieval-system failure boundary: retrieval system failure; C-7R.15.8.2 — Genuine-empty context boundary: genuine empty result. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Gated by: DESIGNED — C-7R.14 — Unrecognized purpose-type halt: an unknown purpose always stops evaluation immediately. [V10 §7R]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7R.15 — Mandatory per-task relevance declaration policy | The owner’s honest failure disposition. | Requires an explicit safe outcome. | Missing relevance cannot be concealed. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] |

SUB-PARTS: C-7R.15.8.1 — Retrieval-system failure boundary; C-7R.15.8.2 — Genuine-empty context boundary

### C-7R.15.8.1 — Retrieval-system failure boundary
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]

ALONE
- What it is: ACCEPTED — The accepted B26 failure behavior consumed by the relevance declarations. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Takes in: ACCEPTED — A retrieval-system failure, bounded B9 attempts and the terminal outcome. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Does: ACCEPTED — Uses bounded retry; after exhaustion stops safely, commits the terminal failure state, states the reason, retains the record and saves unfinished state for the real-change exception. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Gives out: ACCEPTED — An honest terminal failure and preserved unfinished state. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Must never: ACCEPTED — Continue with degraded retrieval after exhausted retry absent a separate later approved rule, or portray system failure as genuine empty context. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Fails closed by: ACCEPTED — Stops the affected retrieval path after bounded retry. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]

TOGETHER
- Fed by: ACCEPTED — C-7F.7.3 — Accepted B26 stop-after-retry policy: canonical B26 stop-after-retry policy; C-7H.9 — B9 retry-state architecture: B9 retry mechanics; C-7H.10 — Accepted B9 retry values and episodes: accepted retry values and real-change boundary. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7R.15.8 — Declaration Fail-closed behavior when relevance cannot be safely determined | The retrieval-system failure disposition. | Keeps the stricter terminal stop. | Generic degraded handling cannot bypass B26. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] |

SUB-PARTS: NONE

### C-7R.15.8.2 — Genuine-empty context boundary
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]

ALONE
- What it is: ACCEPTED — An honestly empty retrieval result from an otherwise healthy run. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Takes in: ACCEPTED — A genuine empty result, distinct from retrieval-system failure. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Does: ACCEPTED — Permits the bare target with context-limited/revisable marking under the retrieval owner’s rule. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Gives out: ACCEPTED — A normal empty-context outcome. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Must never: ACCEPTED — Mislabel broken retrieval as a healthy empty result. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7F.4.8 — Retrieval empty-versus-failure marker: the canonical empty-versus-failure audit distinction. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7R.15.8 — Declaration Fail-closed behavior when relevance cannot be safely determined | The healthy empty result. | Preserves the allowed honest bare-context path. | Empty is not a failed retrieval disguised as success. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] |

SUB-PARTS: NONE

### C-7R.16 — Accepted five-consumer relevance declarations
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The accepted formal declarations for Context Retrieval, Computed View, Action Surfacing, Reread Lifecycle and Living State Web. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10]
- Takes in: ACCEPTED — The five consumer-owned declaration trees and their shared Tier-1 contract. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10]
- Does: ACCEPTED — Uses their proposed mode identities with proposed declaration_version = v1_0; declaration identity and Tier-1 mode identity are the same at this conceptual level. All five use on-demand evaluation, no triggered precomputation and explicit mouth authorization none. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10]
- Gives out: ACCEPTED — Five formally declared consumer modes with local validation remaining at each consumer. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10]
- Must never: ACCEPTED — Treat proposed names as final serialization, add a mouth dimension or precomputation implicitly, or use acceptance as implementation authority. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — A declaration missing required fields has no mode to run; exact failure behavior stays with its owning consumer. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10]

TOGETHER
- Fed by: ACCEPTED — C-7R.16.1 — Retrieval declaration interface: retrieval; C-7R.16.2 — Computed View declaration interface: view; C-7R.16.3 — Action Surfacing declaration interface: action surfacing; C-7R.16.4 — Condition-based reread declaration interface: reread; C-7R.16.5 — State-review declaration interface: state review; C-7R.16.6 — Shared uncertainty-rule consumer interface: shared uncertainty handling; C-7R.16.7 — Future mouth-dimension declaration boundary: future mouth additions; C-7R.16.8 — Quiet automatic relevance use and material disclosure: quiet automatic use. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10]
- Gated by: DESIGNED — C-7R.5.4 — Reusable mode change: later changes require consequence preview, confirmation and a new version; C-7R.4 — Two-tier configuration contract: each tier keeps its owner. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R — Attention & Relevance Control (§7R) | The five accepted consumer declarations. | Validates their shared contracts and returns structured results. | Each consumer retains its local rules. | [V10 §7R] |

SUB-PARTS: C-7R.16.1 — Retrieval declaration interface; C-7R.16.2 — Computed View declaration interface; C-7R.16.3 — Action Surfacing declaration interface; C-7R.16.4 — Condition-based reread declaration interface; C-7R.16.5 — State-review declaration interface; C-7R.16.6 — Shared uncertainty-rule consumer interface; C-7R.16.7 — Future mouth-dimension declaration boundary; C-7R.16.8 — Quiet automatic relevance use and material disclosure

### C-7R.16.1 — Retrieval declaration interface
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The shared-owner interface for proposed RM-CR-01 with proposed declaration_version = v1_0. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Root candidates and a target reading context under retrieval_context_selection. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Uses the existing complete consumer declaration: deterministic type gates, positional same-group/preceding gates, time range only when declared; six applicable dimensions; separate positional and semantic provenance; no mouth and on-demand only. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — A shared-contract judgment for the retrieval owner’s local selection rules. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Admit readings as root candidates, merge retrieval channels or choose untested numeric parameters. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — proposed C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration: the complete canonical proposed RM-CR-01 declaration and local fields. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): internal-use authorization precedes returned roots. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7R.16 — Accepted five-consumer relevance declarations | The retrieval consumer’s declared mode. | Retains shared validation and consumer-local selection. | The existing declaration keeps its identity. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7R.16.2 — Computed View declaration interface
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — The shared-owner interface for proposed RM-CV-01 with proposed declaration_version = v1_0. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — The profile question/target and declared candidate families under view_assembly. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Uses the canonical declaration’s object-type gate and optional declared time range, nine dimensions where applicable, on-demand timing and no mouth; consumer-local relevance remains only one factor in the seven-factor priority order. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — A purpose-bound view judgment with local ordering retained. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Use a hidden aggregate, let relevance outrank stronger source factors, make recency more than its tie-break role or use Computed View as state evidence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7M.10 — Computed View proposed RM-CV-01 declaration: the complete canonical proposed RM-CV-01 declaration, candidate families and local rules. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7R.16 — Accepted five-consumer relevance declarations | The view consumer’s declared mode. | Preserves shared validation and local priority rules. | Existing view atoms are reused. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7R.16.3 — Action Surfacing declaration interface
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The shared-owner interface for proposed RM-AS-01 with proposed declaration_version = v1_0. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — A present situation and candidate support under action_surfacing. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Uses the existing object_type_matches gate, nine applicable dimensions, on-demand timing and no mouth; keeps historical material available and current-situation support distinct from mere same-thread/time proximity. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8]
- Gives out: ACCEPTED — A relevance judgment for the owner’s gentle-protective versus active/outward support rules. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8]
- Must never: ACCEPTED — Treat old weak support as sufficient for active outward suggestions or equate relevance with action permission. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7N.13 — Proposed RM-AS-01 action-surfacing declaration: the complete canonical proposed RM-AS-01 declaration, weak-echo handling and failure rules. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7R.16 — Accepted five-consumer relevance declarations | The action consumer’s declared mode. | Keeps support limits with the surfacing owner. | Relevance creates no permission. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7R.16.4 — Condition-based reread declaration interface
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The shared-owner interface for proposed RM-RR-01 with proposed declaration_version = v1_0. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §11]
- Takes in: ACCEPTED — New information and a prior reading/root under reread_trigger_evaluation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §11]
- Does: ACCEPTED — Uses the existing type gate and optional declared time range, six applicable dimensions, on-demand timing and no mouth; evaluates only possible condition-based relevance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §11]
- Gives out: ACCEPTED — A trigger-evaluation judgment, separate from actual reread and A25 mode assignment. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §11]
- Must never: ACCEPTED — Gate an explicit manual reread by relevance, manufacture an assignment or treat a weak clue alone as a real reread reason. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — proposed C-7H.11 — RM-RR-01 [proposed] reread relevance declaration: the complete canonical proposed RM-RR-01 declaration and manual/condition-based boundary. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7R.16 — Accepted five-consumer relevance declarations | The condition-based reread declaration. | Preserves its limited evaluation role. | The assignment producer and actual trigger remain separate. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-7R.16.5 — State-review declaration interface
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The shared-owner interface for proposed RM-LS-01 with proposed declaration_version = v1_0. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10]
- Takes in: ACCEPTED — A tracked state and new or changed evidence under state_review_trigger_evaluation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10]
- Does: ACCEPTED — Uses the existing type gate and optional time range, six applicable dimensions deliberately excluding currentness_status, on-demand timing and no mouth; emits only a possible review event under the state owner’s rule. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10]
- Gives out: ACCEPTED — A review signal without currentness evidence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10]
- Must never: ACCEPTED — Use the currentness dimension to close a feedback loop, infer freshness from failed evaluation or use relevance as the review’s evidence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7D.14.2 — Proposed RM-LS-01 state-review declaration: the complete canonical proposed RM-LS-01 declaration and event-only limits. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10]
- Gated by: DESIGNED — C-7R.8 — Living State Web relevance boundary: exact review authorization remains with Living State Web. [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7R.16 — Accepted five-consumer relevance declarations | The state-review declaration. | Preserves purpose-scoped evaluation without currency authority. | No state is made current by relevance. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7R.16.6 — Shared uncertainty-rule consumer interface
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]

ALONE
- What it is: ACCEPTED — The proposed T2-UNRES-SHARED v1_0 handling referenced by all five accepted declarations, including their explicit mouth-free versions. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Takes in: ACCEPTED — The actual validation or absence outcome and consumer’s permitted use. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Does: ACCEPTED — Reuses the canonical shared rule: validated remains interpretation; failed is unused; unresolved/disputed may remain a labeled logged weak internal clue, may prompt checking and requires visible uncertainty where material. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Gives out: ACCEPTED — Consumer-governed handling with honest absence markers. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Must never: ACCEPTED — Use uncertainty alone as factual support, current-situation support, Living State change, actual reread, active-suggestion authority, broader access or action authority. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — proposed C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling: the existing shared handling owner; C-7F.6.10.5.1 — Validated relevance value: validated; C-7F.6.10.5.2 — Failed relevance value: failed; C-7F.6.10.5.3 — Unresolved relevance clue: unresolved clue; C-7F.6.10.5.4 — Relevance disagreement record handoff: disagreement; C-7F.6.10.5.5 — Honest dimension absence: honest not_applicable / not_evaluated / collection_failed absence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7R.16 — Accepted five-consumer relevance declarations | The shared rule under its existing identity. | Leaves content validation with each consumer. | The same rule is reused without creating another owner. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |

SUB-PARTS: NONE

### C-7R.16.7 — Future mouth-dimension declaration boundary
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.4]

ALONE
- What it is: ACCEPTED — The conditions for later adding an interpretive mouth dimension to a consumer. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.4]
- Takes in: ACCEPTED — A specifically named dimension/context and proposed new declaration version. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.4]
- Does: ACCEPTED — Requires the new version, named scope, Tier-2 handling identifier/version in Tier 1 and all six deterministic checks; preserves optional model validation only where declared with meaningful independence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.4]
- Gives out: ACCEPTED — A properly declared future mouth role, if confirmed. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.4]
- Must never: ACCEPTED — Infer mouth authorization from the current five declarations, create a mandatory second AI or choose final validator/provider/Interactive Translator implementation here. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.4]
- Fails closed by: ACCEPTED — No new mouth dimension runs through a silent change. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.4]

TOGETHER
- Fed by: DESIGNED — C-7R.5.4 — Reusable mode change: confirmed new version; C-7R.4.1.7 — Tier 1 scoped mouth authorization: named scope; C-7R.10 — Tier-boundary unresolved-rule reference: handling reference; C-7R.6 — Mouth-produced dimension validation: full validation; C-7R.3.5 — Mouth precomputation prerequisites: additional precomputation conditions. [V10 §7R]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7R.16 — Accepted five-consumer relevance declarations | The explicit future-change conditions. | Keeps current mouth authorization at none. | A live speaking architecture is not a relevance validator choice. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.4] |

SUB-PARTS: NONE

### C-7R.16.8 — Quiet automatic relevance use and material disclosure
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The accepted automatic internal use of connections without making Ness a routine approval clerk. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4]
- Takes in: ACCEPTED — A recorded connection and the relevance declaration governing its use. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4]
- Does: ACCEPTED — Permits quiet internal searching, understanding and response preparation; discloses uncertainty when it materially changes a visible claim, interpretation, recommendation, withholding decision, action possibility or conclusion under that result’s owner rules. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4]
- Gives out: ACCEPTED — Useful internal work and appropriately qualified visible results. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4]
- Must never: ACCEPTED — Narrate every small internal connection, promote uncertain links into truth/causation/authority/current-state evidence/access or hand routine gap completion to Ness. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Affected operations halt honestly where their rules require; that halt is not a demand for manual machinery operation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4]

TOGETHER
- Fed by: ACCEPTED — C-24.14 — Connection current-use resolution: canonical current-use rules for connections. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7R.16 — Accepted five-consumer relevance declarations | Automatic use and material-uncertainty limits. | Keeps relevance useful without routine approval work. | Ness remains informed where the visible result changes. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7R.17 — Live relevance query interface
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The accepted relevance component’s contract exposed through the stateless live router. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12]
- Takes in: ACCEPTED — Requesting function identity, declared purpose, target references and applicable mode/configuration version; the relevance instance receives Tier-1 mode id/version, purpose and candidates. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12]
- Does: ACCEPTED — Applies the obtained purpose-correct privacy and authority decisions before ordinary routing, then returns its own current live result whole with provenance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12]
- Gives out: ACCEPTED — Gate results and graded dimensions with provenance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12]
- Must never: ACCEPTED — Let the router filter, summarize, cache between queries, decide relevance, add rules or use BOP/OOP processors as direct query targets. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — Unauthorized or unrecognized purpose is refused and recorded; no guessed purpose mapping. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12]

TOGETHER
- Fed by: DESIGNED — C-LMAC — Live Mechanism Access Coordinator (§26): the live request through its protected-control/ordinary-query routing contract. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): obtained authorization of the correct internal-use or visible-output kind; C-7P — Permission & Authority Boundaries (§7P): the obtained authority decision; C-7R.14 — Unrecognized purpose-type halt: unknown purpose remains a relevance-owned halt. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] [V10 §7R]
- Changes: DESIGNED — C-LMAC — Live Mechanism Access Coordinator (§26): receives the whole component result; behavioral context comes from already stored observation roots and pattern readings through retrieval/relevance, never a direct processor query. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7R — Attention & Relevance Control (§7R) | The authorized live request. | Produces its own live judgment under the declared mode. | The router gains no relevance ownership. | [V10 §7R] |
| 2 · ACCEPTED | C-LMAC.3.2 — Attention and Relevance query contract | Tier-1 mode identifier/version, purpose and candidates. | Supplies the canonical complete relevance-side interface. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |

SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece USED BY continuations

These rows add the reciprocal USED BY entries to the named external cards at assembly. They preserve the delivered cards; every row names both ends. The relationship wording is carried from the current TOGETHER field.

| Current card | Field | External card receiving USED BY row | Stamp | Relationship and condition | Source |
|---|---|---|---|---|---|
| C-7R — Attention & Relevance Control (§7R) | Fed by | C-7B.7 — Hold-until-enough | ACCEPTED | C-7R.15 — Mandatory per-task relevance declaration policy: mandatory declaration policy; C-7R.16 — Accepted five-consumer relevance declarations: accepted consumer declarations and shared handling; C-7R.17 — Live relevance query interface: live-query interface; C-7B.7 — Hold-until-enough: recorded hold fact excludes held material from new surfacing. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] [04/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md §6] |
| C-7R — Attention & Relevance Control (§7R) | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): authorization for the exact current purpose precedes candidates; Level 1 protected-boundary rules, TSC blockers and explicit compartment restrictions still apply regardless of purpose. [SOURCE CONFLICT] V10’s purpose-specific authorization governs over Companion §7R’s unqualified privacy/deletion-eligibility wording; C-7R.4 — Two-tier configuration contract: Tier 1 must be valid; C-7R.14 — Unrecognized purpose-type halt: an unrecognized purpose halts before evaluation. | [V10 §7R] |
| C-7R — Attention & Relevance Control (§7R) | Changes | C-7D — Living State Web (§7D) | DESIGNED | C-7D — Living State Web (§7D): may receive an emitted relevance event only as a possible authorized review trigger, never as currentness evidence or a direct state write; C-LMAC — Live Mechanism Access Coordinator (§26): receives the component’s whole live judgment with provenance. | [V10 §7R] |
| C-7R — Attention & Relevance Control (§7R) | Changes | C-LMAC — Live Mechanism Access Coordinator (§26) | DESIGNED | C-7D — Living State Web (§7D): may receive an emitted relevance event only as a possible authorized review trigger, never as currentness evidence or a direct state write; C-LMAC — Live Mechanism Access Coordinator (§26): receives the component’s whole live judgment with provenance. | [V10 §7R] |
| C-7R.1 — Two-layer relevance judgment | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): eligibility is established before this judgment; C-7R.4 — Two-tier configuration contract: the mode must declare its gates and dimensions. | [V10 §7R] |
| C-7R.5.1 — Full relevance inspection | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): record protection remains applicable; C-SACL — Speaker Access-Control Layer (§25.4): applicable visible inspection follows the privacy-first output order. | [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] |
| C-7R.5.1 — Full relevance inspection | Gated by | C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): record protection remains applicable; C-SACL — Speaker Access-Control Layer (§25.4): applicable visible inspection follows the privacy-first output order. | [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] |
| C-7R.7.2.4 — currentness_status | Fed by | C-7D.10 — State currentness | ACCEPTED | C-7D.10 — State currentness: canonical six-state currentness vocabulary and recorded category: current, possibly_current, stale, currentness_unknown, ended_by_evidence, superseded_by_evidence. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §5] |
| C-7R.7.2.7 — proposal_acceptance_outcome | Fed by | C-7G.5 — Rejection and genuine insufficiency remain separate | DESIGNED | C-7G.5 — Rejection and genuine insufficiency remain separate: distinct acceptance rejection and genuine insufficiency. | [V10 §7R] |
| C-7R.7.2.8 — reading_context_status | Fed by | C-7G.5 — Rejection and genuine insufficiency remain separate | DESIGNED | C-7G.5 — Rejection and genuine insufficiency remain separate: acceptance versus insufficiency separation. | [V10 §7R] |
| C-7R.7.2.9 — active_clash_links | Fed by | C-7J — Clash Handling (§7J) | DESIGNED | C-7R.7.2.9.1 — Clash-link record identifier: clash identifier; C-7R.7.2.9.2 — Clash-link type: type; C-7R.7.2.9.3 — Clash-link detection mode: detection mode; C-7J — Clash Handling (§7J): existing clash records. | [V10 §7R] |
| C-7R.7.3 — Retrieval-channel provenance boundary | Fed by | C-7F.4.6.1 — Supplied-item retrieval type | ACCEPTED | C-7F.4.6.1 — Supplied-item retrieval type: canonical supplied-item retrieval type. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |
| C-7R.8 — Living State Web relevance boundary | Gated by | C-7D — Living State Web (§7D) | DESIGNED | C-7D — Living State Web (§7D): only its explicitly designed review rule can authorize a relevance event as a trigger. | [V10 §7R] |
| C-7R.8 — Living State Web relevance boundary | Changes | C-7D — Living State Web (§7D) | DESIGNED | C-7D — Living State Web (§7D): may receive a provenance-bearing event for authorized review, without receiving a currentness determination. | [V10 §7R] |
| C-7R.8.1 — Review trigger is not review evidence | Fed by | C-7D.14 — State-currentness review | ACCEPTED | C-7D.14 — State-currentness review: state-owned review; C-7D.14.2 — Proposed RM-LS-01 state-review declaration: the accepted proposed RM-LS-01 declaration and its trigger-only limits. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10] |
| C-7R.8.1 — Review trigger is not review evidence | Fed by | C-7D.14.2 — Proposed RM-LS-01 state-review declaration | ACCEPTED | C-7D.14 — State-currentness review: state-owned review; C-7D.14.2 — Proposed RM-LS-01 state-review declaration: the accepted proposed RM-LS-01 declaration and its trigger-only limits. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10] |
| C-7R.15.6 — Declaration Allowed retrieval/use boundary | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): correct internal-use or visible-output authorization precedes candidates; C-SACL — Speaker Access-Control Layer (§25.4): visible output retains privacy first and speaker access second. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] |
| C-7R.15.6 — Declaration Allowed retrieval/use boundary | Gated by | C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): correct internal-use or visible-output authorization precedes candidates; C-SACL — Speaker Access-Control Layer (§25.4): visible output retains privacy first and speaker access second. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] |
| C-7R.15.7 — Declaration Logging / audit requirement | Fed by | C-7B.10.5.1 — One real operation one log | DESIGNED | C-7R.11 — Relevance disagreement record: disagreement fields; C-7R.12 — Completed relevance event record: completed-event fields; C-7R.5 — Ness inspection, correction and configuration changes: inspection/correction/override/version paths; C-7B.10.5.1 — One real operation one log: one real operation one log. | [V10 §7R] [V10 §0B] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] |
| C-7R.15.7 — Declaration Logging / audit requirement | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): all record access remains authorized; C-SIA — Speaker Identity Assessment (§25.3): applicable identity/security authorization remains in force. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] |
| C-7R.15.7 — Declaration Logging / audit requirement | Gated by | C-SIA — Speaker Identity Assessment (§25.3) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): all record access remains authorized; C-SIA — Speaker Identity Assessment (§25.3): applicable identity/security authorization remains in force. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] |
| C-7R.15.8.1 — Retrieval-system failure boundary | Fed by | C-7F.7.3 — Accepted B26 stop-after-retry policy | ACCEPTED | C-7F.7.3 — Accepted B26 stop-after-retry policy: canonical B26 stop-after-retry policy; C-7H.9 — B9 retry-state architecture: B9 retry mechanics; C-7H.10 — Accepted B9 retry values and episodes: accepted retry values and real-change boundary. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] |
| C-7R.15.8.1 — Retrieval-system failure boundary | Fed by | C-7H.9 — B9 retry-state architecture | ACCEPTED | C-7F.7.3 — Accepted B26 stop-after-retry policy: canonical B26 stop-after-retry policy; C-7H.9 — B9 retry-state architecture: B9 retry mechanics; C-7H.10 — Accepted B9 retry values and episodes: accepted retry values and real-change boundary. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] |
| C-7R.15.8.1 — Retrieval-system failure boundary | Fed by | C-7H.10 — Accepted B9 retry values and episodes | ACCEPTED | C-7F.7.3 — Accepted B26 stop-after-retry policy: canonical B26 stop-after-retry policy; C-7H.9 — B9 retry-state architecture: B9 retry mechanics; C-7H.10 — Accepted B9 retry values and episodes: accepted retry values and real-change boundary. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] |
| C-7R.15.8.2 — Genuine-empty context boundary | Fed by | C-7F.4.8 — Retrieval empty-versus-failure marker | ACCEPTED | C-7F.4.8 — Retrieval empty-versus-failure marker: the canonical empty-versus-failure audit distinction. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] |
| C-7R.16.1 — Retrieval declaration interface | Fed by | C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration | ACCEPTED | proposed C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration: the complete canonical proposed RM-CR-01 declaration and local fields. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| C-7R.16.1 — Retrieval declaration interface | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): internal-use authorization precedes returned roots. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| C-7R.16.2 — Computed View declaration interface | Fed by | C-7M.10 — Computed View proposed RM-CV-01 declaration | ACCEPTED | C-7M.10 — Computed View proposed RM-CV-01 declaration: the complete canonical proposed RM-CV-01 declaration, candidate families and local rules. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| C-7R.16.3 — Action Surfacing declaration interface | Fed by | C-7N.13 — Proposed RM-AS-01 action-surfacing declaration | ACCEPTED | C-7N.13 — Proposed RM-AS-01 action-surfacing declaration: the complete canonical proposed RM-AS-01 declaration, weak-echo handling and failure rules. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] |
| C-7R.16.4 — Condition-based reread declaration interface | Fed by | C-7H.11 — RM-RR-01 [proposed] reread relevance declaration | ACCEPTED | proposed C-7H.11 — RM-RR-01 [proposed] reread relevance declaration: the complete canonical proposed RM-RR-01 declaration and manual/condition-based boundary. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §11] |
| C-7R.16.5 — State-review declaration interface | Fed by | C-7D.14.2 — Proposed RM-LS-01 state-review declaration | ACCEPTED | C-7D.14.2 — Proposed RM-LS-01 state-review declaration: the complete canonical proposed RM-LS-01 declaration and event-only limits. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10] |
| C-7R.16.6 — Shared uncertainty-rule consumer interface | Fed by | C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling | ACCEPTED | proposed C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling: the existing shared handling owner; C-7F.6.10.5.1 — Validated relevance value: validated; C-7F.6.10.5.2 — Failed relevance value: failed; C-7F.6.10.5.3 — Unresolved relevance clue: unresolved clue; C-7F.6.10.5.4 — Relevance disagreement record handoff: disagreement; C-7F.6.10.5.5 — Honest dimension absence: honest not_applicable / not_evaluated / collection_failed absence. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| C-7R.16.6 — Shared uncertainty-rule consumer interface | Fed by | C-7F.6.10.5.1 — Validated relevance value | ACCEPTED | proposed C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling: the existing shared handling owner; C-7F.6.10.5.1 — Validated relevance value: validated; C-7F.6.10.5.2 — Failed relevance value: failed; C-7F.6.10.5.3 — Unresolved relevance clue: unresolved clue; C-7F.6.10.5.4 — Relevance disagreement record handoff: disagreement; C-7F.6.10.5.5 — Honest dimension absence: honest not_applicable / not_evaluated / collection_failed absence. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| C-7R.16.6 — Shared uncertainty-rule consumer interface | Fed by | C-7F.6.10.5.2 — Failed relevance value | ACCEPTED | proposed C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling: the existing shared handling owner; C-7F.6.10.5.1 — Validated relevance value: validated; C-7F.6.10.5.2 — Failed relevance value: failed; C-7F.6.10.5.3 — Unresolved relevance clue: unresolved clue; C-7F.6.10.5.4 — Relevance disagreement record handoff: disagreement; C-7F.6.10.5.5 — Honest dimension absence: honest not_applicable / not_evaluated / collection_failed absence. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| C-7R.16.6 — Shared uncertainty-rule consumer interface | Fed by | C-7F.6.10.5.3 — Unresolved relevance clue | ACCEPTED | proposed C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling: the existing shared handling owner; C-7F.6.10.5.1 — Validated relevance value: validated; C-7F.6.10.5.2 — Failed relevance value: failed; C-7F.6.10.5.3 — Unresolved relevance clue: unresolved clue; C-7F.6.10.5.4 — Relevance disagreement record handoff: disagreement; C-7F.6.10.5.5 — Honest dimension absence: honest not_applicable / not_evaluated / collection_failed absence. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| C-7R.16.6 — Shared uncertainty-rule consumer interface | Fed by | C-7F.6.10.5.4 — Relevance disagreement record handoff | ACCEPTED | proposed C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling: the existing shared handling owner; C-7F.6.10.5.1 — Validated relevance value: validated; C-7F.6.10.5.2 — Failed relevance value: failed; C-7F.6.10.5.3 — Unresolved relevance clue: unresolved clue; C-7F.6.10.5.4 — Relevance disagreement record handoff: disagreement; C-7F.6.10.5.5 — Honest dimension absence: honest not_applicable / not_evaluated / collection_failed absence. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| C-7R.16.6 — Shared uncertainty-rule consumer interface | Fed by | C-7F.6.10.5.5 — Honest dimension absence | ACCEPTED | proposed C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling: the existing shared handling owner; C-7F.6.10.5.1 — Validated relevance value: validated; C-7F.6.10.5.2 — Failed relevance value: failed; C-7F.6.10.5.3 — Unresolved relevance clue: unresolved clue; C-7F.6.10.5.4 — Relevance disagreement record handoff: disagreement; C-7F.6.10.5.5 — Honest dimension absence: honest not_applicable / not_evaluated / collection_failed absence. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| C-7R.16.8 — Quiet automatic relevance use and material disclosure | Fed by | C-24.14 — Connection current-use resolution | ACCEPTED | C-24.14 — Connection current-use resolution: canonical current-use rules for connections. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] |
| C-7R.17 — Live relevance query interface | Fed by | C-LMAC — Live Mechanism Access Coordinator (§26) | DESIGNED | C-LMAC — Live Mechanism Access Coordinator (§26): the live request through its protected-control/ordinary-query routing contract. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| C-7R.17 — Live relevance query interface | Gated by | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): obtained authorization of the correct internal-use or visible-output kind; C-7P — Permission & Authority Boundaries (§7P): the obtained authority decision; C-7R.14 — Unrecognized purpose-type halt: unknown purpose remains a relevance-owned halt. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] [V10 §7R] |
| C-7R.17 — Live relevance query interface | Gated by | C-7P — Permission & Authority Boundaries (§7P) | DESIGNED | C-7Q — Privacy, Deletion, Sensitive-data (§7Q): obtained authorization of the correct internal-use or visible-output kind; C-7P — Permission & Authority Boundaries (§7P): the obtained authority decision; C-7R.14 — Unrecognized purpose-type halt: unknown purpose remains a relevance-owned halt. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] [V10 §7R] |
| C-7R.17 — Live relevance query interface | Changes | C-LMAC — Live Mechanism Access Coordinator (§26) | DESIGNED | C-LMAC — Live Mechanism Access Coordinator (§26): receives the whole component result; behavioral context comes from already stored observation roots and pattern readings through retrieval/relevance, never a direct processor query. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |

## Cross-piece TOGETHER continuations for incoming uses

These are the reciprocal uses represented in the current USED BY tables. Their external owners retain their full mechanisms in their assigned pieces.

| Current card supplying use | External using card | Takes in there | Does there | Changes there | Stamp | Source |
|---|---|---|---|---|---|---|
| C-7R — Attention & Relevance Control (§7R) | C-13.3.2 — Authorized relevance evaluation | Declared judgments over prior-authorized material. | Uses relevance in the live context. | Privacy remains an earlier prerequisite. | DESIGNED | [V10 §7R / EXTERNAL PREREQUISITE] [MAP C-13] |
| C-7R — Attention & Relevance Control (§7R) | C-14.6.2 — Declared reference reliability | The declared Tier-1/Tier-2 reliability condition. | Uses earlier context only under the consuming mode. | Earlier material gains no automatic eligibility. | ACCEPTED | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |
| C-7R — Attention & Relevance Control (§7R) | C-7F — Context Retrieval (§7F) | The valid current-purpose relevance judgment. | Selects retrieval context within its local declaration. | Relevance follows privacy and creates no access. | DESIGNED | [MAP C-7F] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |
| C-7R — Attention & Relevance Control (§7R) | C-7F.6.10.5.4 — Relevance disagreement record handoff | The shared disagreement-record contract. | Preserves producer-validator conflict through the shared owner. | No confidence winner silently replaces disagreement. | ACCEPTED | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] |
| C-7R — Attention & Relevance Control (§7R) | C-7F.6.12 — RM-CR-01 [proposed] logging contract | The distinct relevance-event contract. | Records the evaluation separately from retrieval audit. | One event does not replace the other owner’s record. | ACCEPTED | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| C-7R — Attention & Relevance Control (§7R) | C-7F.6.14 — A4 eight-field declaration validity | The shared two-tier validation contract. | Runs only a valid current-purpose declaration. | A missing declaration cannot be improvised. | ACCEPTED | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |
| C-7R — Attention & Relevance Control (§7R) | C-7A — Universal Filter (§7A) | Relevance after privacy authorization. | Keeps reading governance inside both boundaries. | Confidence cannot replace authorization or relevance. | DESIGNED | [V10 §7A] [MAP C-7A] [V10 §0] [V10 §0A] |
| C-7R — Attention & Relevance Control (§7R) | C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B) | Purpose-specific relevance for derived operations. | Applies it after capture/use authorization. | Memory permanence is not a permission or truth grant. | DESIGNED | [V10 §7B] [MAP C-7B] [V10 §0B] |
| C-7R — Attention & Relevance Control (§7R) | C-7B.9.9 — Accepted Wonder surfacing | Genuine relevance of an accepted wonder-origin reading. | Allows ordinary-use surfacing under the established relevance owner. | Acceptance does not imply universal relevance. | ACCEPTED | [04/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md §6] |
| C-7R — Attention & Relevance Control (§7R) | C-7B.9.9.1 — Relevant ordinary-use surfacing | The purpose-scoped relevance judgment. | Surfaces accepted wonder-origin material only on genuine relevance. | Origin and authority boundaries remain intact. | ACCEPTED | [04/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md §6] |
| C-7R — Attention & Relevance Control (§7R) | C-7H.3.3 — RR2 — Instruction and context snapshot | Relevance after prior authorization. | Keeps reread retrieval inside the proper declared purpose. | Relevance does not supply authorization. | ACCEPTED | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |
| C-7R — Attention & Relevance Control (§7R) | C-7GA.11.7.2 — Step 7B — Process triggered view profiles | The view-assembly relevance mode. | Uses that declaration during worker view assembly. | Worker completion cannot invent view relevance. | DESIGNED | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| C-7R — Attention & Relevance Control (§7R) | C-CREATE.10.9 — Creation access ordering | Relevance over already eligible creation material. | Keeps relevance behind privacy. | Creation status does not bypass authorization. | ACCEPTED | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [MAP C-CREATE] |
| C-7R — Attention & Relevance Control (§7R) | C-7M — Computed View (§7M) | A valid declaration for the current view purpose. | Uses relevance within the full view priority order. | Selection does not become truth or state evidence. | DESIGNED | [V10 §7A] [V10 §7M] [V10 §7Q] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] |
| C-7R — Attention & Relevance Control (§7R) | C-7M.2.4 — Computed View factor 4 — purpose relevance | Purpose-scoped relevance in the fourth priority factor. | Uses only the validated declaration. | Relevance does not collapse the seven-factor order. | DESIGNED | [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] [V10 §7R] |
| C-7R — Attention & Relevance Control (§7R) | C-7M.3.3 — Computed View profile_purpose_type | The recognized controlled purpose and vocabulary version. | Binds the snapshot’s declared purpose. | An unknown type cannot be guessed. | ACCEPTED | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [V10 §7R] |
| C-7R — Attention & Relevance Control (§7R) | C-7M.3.11 — Computed View Tier-1 configuration reference | Tier-1 ownership and validation. | Keeps shared configuration with relevance control. | Tier 2 remains view-owned. | ACCEPTED | [V10 §7R] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |
| C-7R — Attention & Relevance Control (§7R) | C-7M.10 — Computed View proposed RM-CV-01 declaration | The valid shared declaration contract. | Uses the existing view-specific declaration after privacy. | No consumer silently takes over Tier 1. | ACCEPTED | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] |
| C-7R — Attention & Relevance Control (§7R) | C-7M.10.1 — Computed View proposed declaration identity and version | The versioned proposal-and-confirmation boundary. | Changes a reusable mode only through that path. | Prior declaration versions remain intact. | ACCEPTED | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |
| C-7R — Attention & Relevance Control (§7R) | C-7M.10.6 — Computed View mouth-authorization boundary | The declared-change and mouth-validation rules. | Keeps present mouth authorization at none. | Future interpretation requires an explicit new declaration. | ACCEPTED | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| C-7R — Attention & Relevance Control (§7R) | C-7M.10.9.4 — Computed View proposed shared unresolved handling | Validation and disagreement handling. | Retains uncertainty under the shared rule. | Confidence cannot silently settle the result. | ACCEPTED | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| C-7R — Attention & Relevance Control (§7R) | C-7M.10.11 — Computed View relevance evaluation record | The complete relevance-event schema. | Records the view’s completed relevance evaluation. | The event does not replace individual judgments. | ACCEPTED | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| C-7R — Attention & Relevance Control (§7R) | C-7M.10.12 — Computed View invalid relevance declaration outcome | Unknown-purpose halt and confirmed change paths. | Stops invalid evaluation without guessing. | The request survives for explicit mapping or proposal. | ACCEPTED | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] |
| C-7R — Attention & Relevance Control (§7R) | C-7D — Living State Web (§7D) | Review-trigger relevance only. | Keeps triggering separate from state currency evidence. | No relevance value establishes currentness. | DESIGNED | [V10 §7D] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] |
| C-7R — Attention & Relevance Control (§7R) | C-7D.14 — State-currentness review | Permitted review suggestions/events under the declaration. | Uses relevance only within its authorized review boundary. | The state owner keeps review authority. | ACCEPTED | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §4B] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10] |
| C-7R — Attention & Relevance Control (§7R) | C-7D.14.1.1 — Review relevance-event reference | Emitted relevance events. | Receives an event as a possible review trigger. | The event is not evidence of the review outcome. | ACCEPTED | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §7] |
| C-7R — Attention & Relevance Control (§7R) | C-7D.14.2.12 — State-review evaluation logging | The settled relevance-event contract. | Records the evaluation separately from state review. | No relevance record rewrites state. | ACCEPTED | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10] |
| C-7R — Attention & Relevance Control (§7R) | C-7D.16 — Evidence-linked world model | Purpose-specific selection. | Uses relevance without converting it into truth or currency. | World-model support stays evidence-linked. | ACCEPTED | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §4D] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §6] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §7] |
| C-7R — Attention & Relevance Control (§7R) | C-24.2.1 — Accepted-connection retrieval route | The current purpose’s relevance configuration. | Keeps connection use purpose-bound after authorization. | A connection does not define its own relevance policy. | ACCEPTED | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A] |
| C-7R — Attention & Relevance Control (§7R) | C-24.19.7 — Connection I7 accepted-use interface | The accepted purpose/relevance configuration. | Uses the retrieval owner and stateless router under that configuration. | Routing gains no relevance authority. | ACCEPTED | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| C-7R — Attention & Relevance Control (§7R) | C-7N.13.1 — Proposed RM-AS-01 identity and version | The confirmed version-change path. | Preserves the action declaration’s prior versions. | Reusable changes cannot arise silently. | ACCEPTED | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] |
| C-7R — Attention & Relevance Control (§7R) | C-7N.13.12 — Action-surfacing relevance audit contract | The complete evaluation and disagreement record contracts. | Records actual relevance work and conflict. | Possibility history stays separate from relevance history. | ACCEPTED | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] |
| C-7R — Attention & Relevance Control (§7R) | C-7N.13.13.4 — Action-surfacing unrecognized-purpose failure | Unknown-purpose halt and versioned new-type handling. | Refuses guessed purpose substitution. | The original request remains preserved. | ACCEPTED | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] |
| C-7R — Attention & Relevance Control (§7R) | C-7P.13.4 — Authority records privacy and non-evidence boundary | Purpose and selection relevance. | Keeps it separate from action authority and truth. | Relevance grants no permission. | ACCEPTED | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §14] |
| C-7R — Attention & Relevance Control (§7R) | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | The already-authorized candidate boundary. | Admits only purpose-authorized material to relevance. | Relevance cannot rerun or redefine privacy. | DESIGNED | [V10 §7Q] |
| C-7R — Attention & Relevance Control (§7R) | C-7Q.6.2 — Layer 1 — Pre-retrieval visible-output eligibility | The purpose-authorized candidate space. | Limits relevance to the obtained privacy decision. | Possession does not imply eligibility. | DESIGNED | [V10 §7Q] |
| C-7R — Attention & Relevance Control (§7R) | C-7Q.11.6 — Retrieval, relevance and authorization-query boundary | The authorized candidate-space query result. | Keeps retrieval and relevance inside the privacy owner’s decision. | Stateless routing cannot widen permission. | ACCEPTED | [04/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md §16] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |

## Scope, paths and source dispositions

All fourteen V10 §7R decisions are placed in their original order. The root preserves the complete purpose-specific privacy prerequisite, including visible versus internal purposes, the separate influence-removal instruction, Level 1, TSC and explicit compartments. The Companion’s older unqualified privacy/deletion-eligibility wording is marked as a source conflict in the header and affected gate; V10 governs. No shared relevance gate takes over privacy, identity, permission, truth, evidence strength, causation, clash resolution or state-currentness authority.

The two output layers, individually chosen producers, complete production provenance, on-demand default and optional context-bound precomputation are explicit. The precomputed record carries every stated context/configuration/object/version/trigger/time/validity group. All six invalidation classes and both mouth-precomputation prerequisites are retained. Tier 1 has every minimum field and Tier 2 retains its local owner; a mode needs its own required local fields, not completion of every other consumer’s design. Inspection, direct correction, scoped override, consequence preview, confirmation, new versions and exact invalid-configuration handling remain separate. The five preview-consequence groups each have a card.

Mouth validation preserves all six checks, the schema check’s three predicates, all three outcome meanings and all six stated failure classes. The optional model-validator contract includes identity/configuration, reason, declared meaningful independence, separate provenance, disagreement and no final authority; repeated same-model/same-setup calls do not create independence. No mouth dimension becomes a categorical gate. V10’s dolphin-llama3 producer role is retained with the accepted formal declaration’s explicit distinction between the test model and the still-open final adopted mouth/Interactive Translator choices. No mandatory second AI is created.

All four gate names, nine dimension names, structural-link entry fields and five link types, Ness-response fields and clash-link fields are explicit. Recorded currentness consumes the already canonical six-status tree at C-7D.10, and reading acceptance/context distinctions consume C-7G.5. Channel identity remains mandatory retrieval provenance under the existing retrieval-type owner, never a dimension. Local dimension declaration and later shared promotion remain distinct. The five controlled purpose types and their exact meanings retain an optional inert string label; a new type requires confirmation/versioning while a new label does not.

The Tier-2 unresolved reference carries identifier and version, with reference-only validation and stale-version detection. The disagreement record retains all nine field groups and three starting conflict types plus the declared-extension slot. Producer and validator results remain separate originals. The completed-evaluation event retains all thirteen groups, five candidate counts, conditional trigger, typed target identity, one pointer per judgment, disagreement presence/pointers and completion time. Unknown purpose produces no false completed event: it immediately halts, preserves exact value/vocabulary/configuration/context, explains the problem and offers only explicitly confirmed mapping or a versioned new-type proposal. Its separate halt event retains all three fields.

Override-pattern observation requires all three simultaneous conditions, exact pattern presentation, a possibility rather than a recommendation, and the explicit contextual-correction alternative. Silence is not dismissal. Explicit dismissal closes the observation and prevents unchanged resurfacing until new overrides or material evidence change; no permanent mode change occurs automatically. Relevance records remain in their own record space. A state review uses independently valid evidence, a separate Ness currentness statement is its own response event, and the currentness→relevance→currency→currentness support loop remains forbidden. Accepted generic state-review triggers do not settle the remaining exact relevance-event authorization rules.

A4’s full eight-field policy and declaration-invalidity rule are placed. The five accepted consumer declaration trees are reused at C-7F.6, C-7M.10, C-7N.13, C-7H.11 and C-7D.14.2; shared proposed T2-UNRES-SHARED handling stays at C-7F.6.10.5 and its five children. Proposed identifiers and proposed declaration_version = v1_0 retain their qualifier. Every current mode is on demand, permits no precomputation and explicitly declares mouth authorization none. Numeric parameters, consumer-local order/fallback/surfacing and all candidate-specific schemas remain under their existing owners. Current accepted conceptual declarations settle the older open declaration list without implying implementation.

Failure retains the owner’s honest stop/degraded choice where allowed, but exhausted retrieval-system retry has the stricter accepted B26 stop, terminal record, reason and preserved unfinished state. Genuine empty retrieval alone follows the normal bare-target context-limited/revisable path. One operation/one log, no log-as-truth, no double evidence, look-don’t-touch log access, privacy/security authorization and append-only declaration/evaluation history remain intact. Quiet automatic internal connection use creates no routine Ness approval queue; visible material uncertainty stays with the result’s owner.

The live relevance interface returns gate results and graded dimensions with provenance for the actual Tier-1 mode/version, purpose and candidates. The router obtains privacy and authority decisions through its own non-recursive control path before ordinary routing; it owns no relevance rule. BOP roots and pattern readings are reached through the shared store, never by querying BOP/OOP processors. Complete router query identity, retry and lifecycle mechanics remain CH08-c. Main-path retrieval, derived-view, action and state-review uses retain their existing component ownership; full side-path assembly remains CH11.

Discovery searched the part ID, Attention/Relevance names, mode declarations, judgments and events across the accepted/active packages and decision records. The full A4 policy/receipt and formal Bundle 2 declaration/receipt chain were read. A2 and B11 identity/manifest rules preserve semantic ownership; A17’s ordinary-use wonder rule consumes relevance; B-INT-8, the authority control plane and operation kernel preserve owner decisions. The framework additions and live speaking-model concept choose no relevance validator. Thought-branch intent and inactive memory-fabric references add no accepted mechanics. Recovery-ledger title/status discovery supplies no behavioral text; earlier restored operational laws remain at their canonical logging owners.

All 37 earlier incoming C-7R places are reciprocated individually. The earlier C-7B.7 USED BY row that stamps the C-7R root ACCEPTED remains a carried defect. Two additional CH02 Gated-by occurrences, C-7B.9.9 and C-7B.9.9.1, also stamp the root ACCEPTED; the root remains DESIGNED and those earlier bytes are unchanged. The previously reported CH05-a root-name discrepancy and earlier proposed-name defects remain in the manifest. No earlier card is renamed or rewritten.

The accepted Bundle 2 foundation body remains excluded under the READ boundary; its absence from the allowed corpus is a source-scope gap, not absence of an accepted design. The foundation acceptance receipt and full formal v1.1 supply their own usable content. The July-12 closure receipt records explicit formal-package acceptance while retaining its own independent-audit condition for formal PACKAGE_COMPLETE standing; no broader completion is inferred from its title. Empirical values, final model/provider/validator mechanisms, exact field types/storage/indexing/serialization, visual drawer mechanics, exact state-review authorization, operational B9/B26 integration and B-CYCLE-8 remain open. Full observation/affirmation/adaptation follows in CH08-d–g, identity/security CH09, visual interface CH10-e and regenerated registers CH12.

## Source-to-card coverage added by CH08-b

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §7R introduction and external prerequisite; A4 §4 | C-7R root: purpose-only judgment; no truth/strength/causation/authority/permission, merging, clash resolution, rewriting/reordering/suppression, privacy ownership, state writing or purpose guessing. Prior purpose-specific C-7Q authorization; held-material boundary retained. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 1 | .1: two-layer object; categorical deterministic gate excludes without grading; named value/source/method dimensions only after passing, no hidden aggregate. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 2 | .2: producer per dimension; reproducible deterministic structural/temporal/currency/count, all-MiniLM-L6-v2 semantic/thematic, declaration-limited dolphin-llama3 interpretive role; no per-call approval/self-approval; producer/version/index/prompt/value provenance. Final mouth selection remains open in accepted B2. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 3 | .3: on-demand default; optional latency-specific precomputation, no global relevance; seven field groups; exact context/validity reuse; six invalidation classes; mouth precomputation requires declaration plus independently designed validation. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 4 | .4: Tier 1 owner/validation and ten minimum declaration groups; Tier 2 consumer-local thresholds/order/weights/fallback/surfacing/unresolved fields as needed, versioned additions; no cross-tier ownership. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 5 | .5: unrestricted Ness inspection under existing record protection; direct correction, context override, consequence preview plus confirmation and new version; no veto; invalid-configuration exact-conflict explanation and preserved request; append-only all objects. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 6 | .6: six deterministic checks; Validated/Failed/Unresolved and exact meanings; optional declared validator model/config/reason/independence/provenance/disagreement handling; no model final authority or mouth gate. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 7 | .7: four exact gate names; nine exact dimensions; all link-entry fields and five explicit-link types; Ness-response entry fields; clash entry fields. Existing C-7D.10 owns six currentness statuses; C-7G owns acceptance/context status. Channel identity stays mandatory retrieval provenance. Local/shared extension path. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 8; B2 §10; B4 §5 | .8: own relevance record space; state review requires state-owned authorization; event is a trigger possibility not evidence; independent evidence, separate Ness response, relevance/currentness separation and exact forbidden feedback chain. Exact trigger authorization remains open. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 9 | .9: required controlled type and optional inert string label; all five purpose values and meanings; new type requires confirmation/versioning, new label does not. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 10 | .10: conditional Tier-2 rule identifier/version reference; present/nonempty/current validation only; consumer owns content; changed Tier 2 requires updated Tier 1 reference; no obligation for mouth-free mode. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 11 | .11: disagreement record and nine field groups, exact producer/validator pointers, three starting conflict types plus declared extension, producer model/prompt/config, validator identity/version/independence, uncertainty-rule reference, resulting state and timestamp; no copied interpretive body. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 12 | .12: completed evaluation event, all thirteen field groups; five separate candidate summary counts; conditional trigger, one pointer per judgment, disagreement flag/pointers, completion time; no event for unrun evaluation. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 13 | .13: three simultaneous pattern predicates; exact observed pattern and optional mode change, no recommendation; corrections may be contextual; open until explicit action/dismissal; dismissal suppresses unchanged pattern until new overrides/material change; no automatic configuration change. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 14 | .14: immediate halt, no gate/dimension/completion event; exact unknown value/vocabulary version, preserved original full configuration/context, plain explanation; confirmed mapping or versioned new type; close match not authority; separate halt event unknown/request/time. | C-7R source-ordered tree and the explicit scope dispositions |
| A4 §§1–5; B2 §§4/5 | .15: Option C shared language plus mandatory versioned declarations, all eight policy fields, invalid/missing declaration no mode; honest owner-specific stop/degraded handling; genuine empty vs system failure; no hidden relevance dialect or per-judgment clerk work. | C-7R source-ordered tree and the explicit scope dispositions |
| B2 complete §§5–10 | .16: accepted five declarations; all on demand, no precomputation, explicit mouth none, six vs nine dimension applicability, controlled purposes and canonical consumer owner references; proposed names always qualified. Proposed T2-UNRES-SHARED reuses C-7F.6.10.5 and its children, no second shared rule. Future mouth mode requires version/change/validation, not mandatory second AI. | C-7R source-ordered tree and the explicit scope dispositions |
| B2 §§5.6/5.7/11/12; B1 §5; A4 §§4/5 | .16: one-operation/one-log, evaluation/disagreement/declaration history, ordinary inspection not approval queue; B26 failure after bounded B9 stops and preserves unfinished work, no degraded continuation; genuine empty alone permits honest bare context; numeric empirical values, provider/validator choices/serialization/UI and full-cycle wiring remain open. | C-7R source-ordered tree and the explicit scope dispositions |
| B6 mechanical §12 | .17: exact relevance query Tier-1 mode id/version + purpose + candidates; uniform requester/targets/config; obtained purpose-correct privacy and authority decisions before route; own whole provenance-bearing result; router never owns rules, processors not direct targets; query identity/retry belongs CH08-c. | C-7R source-ordered tree and the explicit scope dispositions |
| Earlier delivered pieces | 37 incoming uses, one place each; C-7B.7 old USED BY root stamp is wrong and remains carried. CH02 C-7B.9.9 and .9.9.1 also incorrectly stamp C-7R ACCEPTED; add fix note, no old-byte edit. C-7R root DESIGNED. Existing root-name discrepancy, proposed qualifiers and all other earlier defects remain carried. | C-7R source-ordered tree and the explicit scope dispositions |

## Additional undecided implementation slots

| Owner | Slot | State |
|---|---|---|
| C-7R.12 — Completed relevance event record | Exact implementation field types, storage formats, serialization and indexing beyond the settled conceptual schemas | NOT DECIDED |
| C-7R.16 — Accepted five-consumer relevance declarations | Empirical limits, thresholds, weights, budgets, spans, ceiling values and gold-material tuning; accepted conceptual declarations remain settled | NOT DECIDED |
| C-7R.6.3 — Optional declared model-based validation | Exact future validator model, provider, program and independence implementation; no mandatory second AI or final Interactive Translator selected | NOT DECIDED |
| C-7R.11.4 — Disagreement type vocabulary | Disagreement-type vocabulary extensions beyond the three starting types; other types require explicit declaration | NOT DECIDED |
| C-7R.7.4 — Local dimension and shared-vocabulary extension | Future local dimensions and shared-vocabulary promotions beyond the settled minimum | NOT DECIDED |
| C-7R.8 — Living State Web relevance boundary | Exact state-owner authorization of relevance events as currency-review triggers beyond accepted generic new/changed-evidence review | NOT DECIDED |
| C-7R.16 — Accepted five-consumer relevance declarations | Final mechanical names and serialization for proposed mode identities and proposed declaration_version | NOT DECIDED |
| C-7R.16 — Accepted five-consumer relevance declarations | Side-drawer visual/interaction mechanics, later operational B9/B26 consumer wiring and B-CYCLE-8 composition | NOT DECIDED |

## Appendix A carry-forward — this piece

| Card | Empty field | Occurrence within field | State |
|---|---|---|---|
| C-7R.1 — Two-layer relevance judgment | Changes | 1 | NOT DECIDED |
| C-7R.1.1 — Context-specific boolean gate | Changes | 1 | NOT DECIDED |
| C-7R.1.2 — Graded named dimensions | Changes | 1 | NOT DECIDED |
| C-7R.1.2.1 — Dimension name | Fails closed by | 1 | NOT DECIDED |
| C-7R.1.2.1 — Dimension name | Fed by | 1 | NOT DECIDED |
| C-7R.1.2.1 — Dimension name | Gated by | 1 | NOT DECIDED |
| C-7R.1.2.1 — Dimension name | Changes | 1 | NOT DECIDED |
| C-7R.1.2.2 — Dimension value | Fails closed by | 1 | NOT DECIDED |
| C-7R.1.2.2 — Dimension value | Fed by | 1 | NOT DECIDED |
| C-7R.1.2.2 — Dimension value | Gated by | 1 | NOT DECIDED |
| C-7R.1.2.2 — Dimension value | Changes | 1 | NOT DECIDED |
| C-7R.1.2.3 — Dimension source or method | Fails closed by | 1 | NOT DECIDED |
| C-7R.1.2.3 — Dimension source or method | Gated by | 1 | NOT DECIDED |
| C-7R.1.2.3 — Dimension source or method | Changes | 1 | NOT DECIDED |
| C-7R.2 — Per-dimension producer selection | Fails closed by | 1 | NOT DECIDED |
| C-7R.2 — Per-dimension producer selection | Changes | 1 | NOT DECIDED |
| C-7R.2.1 — Deterministic dimension producer | Fails closed by | 1 | NOT DECIDED |
| C-7R.2.1 — Deterministic dimension producer | Fed by | 1 | NOT DECIDED |
| C-7R.2.1 — Deterministic dimension producer | Gated by | 1 | NOT DECIDED |
| C-7R.2.1 — Deterministic dimension producer | Changes | 1 | NOT DECIDED |
| C-7R.2.2 — Embedding dimension producer | Fails closed by | 1 | NOT DECIDED |
| C-7R.2.2 — Embedding dimension producer | Gated by | 1 | NOT DECIDED |
| C-7R.2.2 — Embedding dimension producer | Changes | 1 | NOT DECIDED |
| C-7R.2.3 — Declared interpretive mouth producer | Changes | 1 | NOT DECIDED |
| C-7R.2.4 — Common dimension producer provenance | Fails closed by | 1 | NOT DECIDED |
| C-7R.2.4 — Common dimension producer provenance | Gated by | 1 | NOT DECIDED |
| C-7R.2.4 — Common dimension producer provenance | Changes | 1 | NOT DECIDED |
| C-7R.2.4.1 — Dimension producer identity | Fails closed by | 1 | NOT DECIDED |
| C-7R.2.4.1 — Dimension producer identity | Fed by | 1 | NOT DECIDED |
| C-7R.2.4.1 — Dimension producer identity | Gated by | 1 | NOT DECIDED |
| C-7R.2.4.1 — Dimension producer identity | Changes | 1 | NOT DECIDED |
| C-7R.2.4.2 — Dimension rule or model version | Fails closed by | 1 | NOT DECIDED |
| C-7R.2.4.2 — Dimension rule or model version | Fed by | 1 | NOT DECIDED |
| C-7R.2.4.2 — Dimension rule or model version | Gated by | 1 | NOT DECIDED |
| C-7R.2.4.2 — Dimension rule or model version | Changes | 1 | NOT DECIDED |
| C-7R.2.4.3 — Dimension index or prompt version | Fails closed by | 1 | NOT DECIDED |
| C-7R.2.4.3 — Dimension index or prompt version | Fed by | 1 | NOT DECIDED |
| C-7R.2.4.3 — Dimension index or prompt version | Gated by | 1 | NOT DECIDED |
| C-7R.2.4.3 — Dimension index or prompt version | Changes | 1 | NOT DECIDED |
| C-7R.3 — Evaluation timing | Fails closed by | 1 | NOT DECIDED |
| C-7R.3 — Evaluation timing | Changes | 1 | NOT DECIDED |
| C-7R.3.1 — On-demand evaluation | Fails closed by | 1 | NOT DECIDED |
| C-7R.3.1 — On-demand evaluation | Fed by | 1 | NOT DECIDED |
| C-7R.3.1 — On-demand evaluation | Gated by | 1 | NOT DECIDED |
| C-7R.3.1 — On-demand evaluation | Changes | 1 | NOT DECIDED |
| C-7R.3.2 — Declared triggered precomputation | Fails closed by | 1 | NOT DECIDED |
| C-7R.3.2 — Declared triggered precomputation | Changes | 1 | NOT DECIDED |
| C-7R.3.3 — Precomputed judgment bindings | Fails closed by | 1 | NOT DECIDED |
| C-7R.3.3 — Precomputed judgment bindings | Gated by | 1 | NOT DECIDED |
| C-7R.3.3 — Precomputed judgment bindings | Changes | 1 | NOT DECIDED |
| C-7R.3.3.1 — Precomputed context or purpose identifier | Fails closed by | 1 | NOT DECIDED |
| C-7R.3.3.1 — Precomputed context or purpose identifier | Fed by | 1 | NOT DECIDED |
| C-7R.3.3.1 — Precomputed context or purpose identifier | Gated by | 1 | NOT DECIDED |
| C-7R.3.3.1 — Precomputed context or purpose identifier | Changes | 1 | NOT DECIDED |
| C-7R.3.3.2 — Precomputed consuming mode and configuration version | Fails closed by | 1 | NOT DECIDED |
| C-7R.3.3.2 — Precomputed consuming mode and configuration version | Fed by | 1 | NOT DECIDED |
| C-7R.3.3.2 — Precomputed consuming mode and configuration version | Gated by | 1 | NOT DECIDED |
| C-7R.3.3.2 — Precomputed consuming mode and configuration version | Changes | 1 | NOT DECIDED |
| C-7R.3.3.3 — Precomputed candidate and target identifiers | Fails closed by | 1 | NOT DECIDED |
| C-7R.3.3.3 — Precomputed candidate and target identifiers | Fed by | 1 | NOT DECIDED |
| C-7R.3.3.3 — Precomputed candidate and target identifiers | Gated by | 1 | NOT DECIDED |
| C-7R.3.3.3 — Precomputed candidate and target identifiers | Changes | 1 | NOT DECIDED |
| C-7R.3.3.4 — Precomputed production versions | Fails closed by | 1 | NOT DECIDED |
| C-7R.3.3.4 — Precomputed production versions | Gated by | 1 | NOT DECIDED |
| C-7R.3.3.4 — Precomputed production versions | Changes | 1 | NOT DECIDED |
| C-7R.3.3.5 — Precomputed trigger | Fails closed by | 1 | NOT DECIDED |
| C-7R.3.3.5 — Precomputed trigger | Fed by | 1 | NOT DECIDED |
| C-7R.3.3.5 — Precomputed trigger | Gated by | 1 | NOT DECIDED |
| C-7R.3.3.5 — Precomputed trigger | Changes | 1 | NOT DECIDED |
| C-7R.3.3.6 — Precomputed production time | Fails closed by | 1 | NOT DECIDED |
| C-7R.3.3.6 — Precomputed production time | Fed by | 1 | NOT DECIDED |
| C-7R.3.3.6 — Precomputed production time | Gated by | 1 | NOT DECIDED |
| C-7R.3.3.6 — Precomputed production time | Changes | 1 | NOT DECIDED |
| C-7R.3.3.7 — Precomputed validity or staleness state | Fails closed by | 1 | NOT DECIDED |
| C-7R.3.3.7 — Precomputed validity or staleness state | Fed by | 1 | NOT DECIDED |
| C-7R.3.3.7 — Precomputed validity or staleness state | Gated by | 1 | NOT DECIDED |
| C-7R.3.3.7 — Precomputed validity or staleness state | Changes | 1 | NOT DECIDED |
| C-7R.3.4 — Context-bound reuse and invalidation | Gated by | 1 | NOT DECIDED |
| C-7R.3.4 — Context-bound reuse and invalidation | Changes | 1 | NOT DECIDED |
| C-7R.3.4.1 — Changed-purpose invalidation | Fed by | 1 | NOT DECIDED |
| C-7R.3.4.1 — Changed-purpose invalidation | Gated by | 1 | NOT DECIDED |
| C-7R.3.4.1 — Changed-purpose invalidation | Changes | 1 | NOT DECIDED |
| C-7R.3.4.2 — Changed-source invalidation | Fed by | 1 | NOT DECIDED |
| C-7R.3.4.2 — Changed-source invalidation | Gated by | 1 | NOT DECIDED |
| C-7R.3.4.2 — Changed-source invalidation | Changes | 1 | NOT DECIDED |
| C-7R.3.4.3 — Changed-configuration invalidation | Fed by | 1 | NOT DECIDED |
| C-7R.3.4.3 — Changed-configuration invalidation | Gated by | 1 | NOT DECIDED |
| C-7R.3.4.3 — Changed-configuration invalidation | Changes | 1 | NOT DECIDED |
| C-7R.3.4.4 — Changed-producer-version invalidation | Fed by | 1 | NOT DECIDED |
| C-7R.3.4.4 — Changed-producer-version invalidation | Gated by | 1 | NOT DECIDED |
| C-7R.3.4.4 — Changed-producer-version invalidation | Changes | 1 | NOT DECIDED |
| C-7R.3.4.5 — Relevant Ness-response invalidation | Fed by | 1 | NOT DECIDED |
| C-7R.3.4.5 — Relevant Ness-response invalidation | Gated by | 1 | NOT DECIDED |
| C-7R.3.4.5 — Relevant Ness-response invalidation | Changes | 1 | NOT DECIDED |
| C-7R.3.4.6 — Other declared invalidating event | Fed by | 1 | NOT DECIDED |
| C-7R.3.4.6 — Other declared invalidating event | Gated by | 1 | NOT DECIDED |
| C-7R.3.4.6 — Other declared invalidating event | Changes | 1 | NOT DECIDED |
| C-7R.3.5 — Mouth precomputation prerequisites | Gated by | 1 | NOT DECIDED |
| C-7R.3.5 — Mouth precomputation prerequisites | Changes | 1 | NOT DECIDED |
| C-7R.4 — Two-tier configuration contract | Gated by | 1 | NOT DECIDED |
| C-7R.4 — Two-tier configuration contract | Changes | 1 | NOT DECIDED |
| C-7R.4.1 — Tier 1 shared required contract | Changes | 1 | NOT DECIDED |
| C-7R.4.1.1 — Tier 1 mode identity and version | Fails closed by | 1 | NOT DECIDED |
| C-7R.4.1.1 — Tier 1 mode identity and version | Gated by | 1 | NOT DECIDED |
| C-7R.4.1.1 — Tier 1 mode identity and version | Changes | 1 | NOT DECIDED |
| C-7R.4.1.1.1 — Tier 1 stable mode identifier | Fails closed by | 1 | NOT DECIDED |
| C-7R.4.1.1.1 — Tier 1 stable mode identifier | Fed by | 1 | NOT DECIDED |
| C-7R.4.1.1.1 — Tier 1 stable mode identifier | Gated by | 1 | NOT DECIDED |
| C-7R.4.1.1.1 — Tier 1 stable mode identifier | Changes | 1 | NOT DECIDED |
| C-7R.4.1.1.2 — Tier 1 mode version | Fails closed by | 1 | NOT DECIDED |
| C-7R.4.1.1.2 — Tier 1 mode version | Fed by | 1 | NOT DECIDED |
| C-7R.4.1.1.2 — Tier 1 mode version | Gated by | 1 | NOT DECIDED |
| C-7R.4.1.1.2 — Tier 1 mode version | Changes | 1 | NOT DECIDED |
| C-7R.4.1.3 — Tier 1 consuming component | Fails closed by | 1 | NOT DECIDED |
| C-7R.4.1.3 — Tier 1 consuming component | Fed by | 1 | NOT DECIDED |
| C-7R.4.1.3 — Tier 1 consuming component | Gated by | 1 | NOT DECIDED |
| C-7R.4.1.3 — Tier 1 consuming component | Changes | 1 | NOT DECIDED |
| C-7R.4.1.4 — Tier 1 candidate and target object types | Fails closed by | 1 | NOT DECIDED |
| C-7R.4.1.4 — Tier 1 candidate and target object types | Gated by | 1 | NOT DECIDED |
| C-7R.4.1.4 — Tier 1 candidate and target object types | Changes | 1 | NOT DECIDED |
| C-7R.4.1.4.1 — Tier 1 candidate object types | Fails closed by | 1 | NOT DECIDED |
| C-7R.4.1.4.1 — Tier 1 candidate object types | Fed by | 1 | NOT DECIDED |
| C-7R.4.1.4.1 — Tier 1 candidate object types | Gated by | 1 | NOT DECIDED |
| C-7R.4.1.4.1 — Tier 1 candidate object types | Changes | 1 | NOT DECIDED |
| C-7R.4.1.4.2 — Tier 1 target object types | Fails closed by | 1 | NOT DECIDED |
| C-7R.4.1.4.2 — Tier 1 target object types | Fed by | 1 | NOT DECIDED |
| C-7R.4.1.4.2 — Tier 1 target object types | Gated by | 1 | NOT DECIDED |
| C-7R.4.1.4.2 — Tier 1 target object types | Changes | 1 | NOT DECIDED |
| C-7R.4.1.5 — Tier 1 gate conditions and producers | Fails closed by | 1 | NOT DECIDED |
| C-7R.4.1.5 — Tier 1 gate conditions and producers | Changes | 1 | NOT DECIDED |
| C-7R.4.1.6 — Tier 1 dimensions and producers | Fails closed by | 1 | NOT DECIDED |
| C-7R.4.1.6 — Tier 1 dimensions and producers | Gated by | 1 | NOT DECIDED |
| C-7R.4.1.6 — Tier 1 dimensions and producers | Changes | 1 | NOT DECIDED |
| C-7R.4.1.7 — Tier 1 scoped mouth authorization | Fed by | 1 | NOT DECIDED |
| C-7R.4.1.7 — Tier 1 scoped mouth authorization | Gated by | 1 | NOT DECIDED |
| C-7R.4.1.7 — Tier 1 scoped mouth authorization | Changes | 1 | NOT DECIDED |
| C-7R.4.1.8 — Tier 1 evaluation timing declaration | Fails closed by | 1 | NOT DECIDED |
| C-7R.4.1.8 — Tier 1 evaluation timing declaration | Fed by | 1 | NOT DECIDED |
| C-7R.4.1.8 — Tier 1 evaluation timing declaration | Gated by | 1 | NOT DECIDED |
| C-7R.4.1.8 — Tier 1 evaluation timing declaration | Changes | 1 | NOT DECIDED |
| C-7R.4.1.9 — Tier 1 precomputation triggers and invalidators | Fails closed by | 1 | NOT DECIDED |
| C-7R.4.1.9 — Tier 1 precomputation triggers and invalidators | Gated by | 1 | NOT DECIDED |
| C-7R.4.1.9 — Tier 1 precomputation triggers and invalidators | Changes | 1 | NOT DECIDED |
| C-7R.4.2 — Tier 2 component-local settings | Fed by | 1 | NOT DECIDED |
| C-7R.4.2 — Tier 2 component-local settings | Changes | 1 | NOT DECIDED |
| C-7R.5 — Ness inspection, correction and configuration changes | Changes | 1 | NOT DECIDED |
| C-7R.5.1 — Full relevance inspection | Fails closed by | 1 | NOT DECIDED |
| C-7R.5.1 — Full relevance inspection | Fed by | 1 | NOT DECIDED |
| C-7R.5.1 — Full relevance inspection | Changes | 1 | NOT DECIDED |
| C-7R.5.2 — Direct per-judgment correction | Fails closed by | 1 | NOT DECIDED |
| C-7R.5.2 — Direct per-judgment correction | Fed by | 1 | NOT DECIDED |
| C-7R.5.2 — Direct per-judgment correction | Gated by | 1 | NOT DECIDED |
| C-7R.5.2 — Direct per-judgment correction | Changes | 1 | NOT DECIDED |
| C-7R.5.3 — Context-scoped per-judgment override | Fails closed by | 1 | NOT DECIDED |
| C-7R.5.3 — Context-scoped per-judgment override | Fed by | 1 | NOT DECIDED |
| C-7R.5.3 — Context-scoped per-judgment override | Gated by | 1 | NOT DECIDED |
| C-7R.5.3 — Context-scoped per-judgment override | Changes | 1 | NOT DECIDED |
| C-7R.5.4 — Reusable mode change | Changes | 1 | NOT DECIDED |
| C-7R.5.4.1 — Mode-change consequence preview | Fails closed by | 1 | NOT DECIDED |
| C-7R.5.4.1 — Mode-change consequence preview | Gated by | 1 | NOT DECIDED |
| C-7R.5.4.1 — Mode-change consequence preview | Changes | 1 | NOT DECIDED |
| C-7R.5.4.1.1 — Preview affected gate conditions | Fails closed by | 1 | NOT DECIDED |
| C-7R.5.4.1.1 — Preview affected gate conditions | Fed by | 1 | NOT DECIDED |
| C-7R.5.4.1.1 — Preview affected gate conditions | Gated by | 1 | NOT DECIDED |
| C-7R.5.4.1.1 — Preview affected gate conditions | Changes | 1 | NOT DECIDED |
| C-7R.5.4.1.2 — Preview affected graded dimensions | Fails closed by | 1 | NOT DECIDED |
| C-7R.5.4.1.2 — Preview affected graded dimensions | Fed by | 1 | NOT DECIDED |
| C-7R.5.4.1.2 — Preview affected graded dimensions | Gated by | 1 | NOT DECIDED |
| C-7R.5.4.1.2 — Preview affected graded dimensions | Changes | 1 | NOT DECIDED |
| C-7R.5.4.1.3 — Preview affected consuming components | Fails closed by | 1 | NOT DECIDED |
| C-7R.5.4.1.3 — Preview affected consuming components | Fed by | 1 | NOT DECIDED |
| C-7R.5.4.1.3 — Preview affected consuming components | Gated by | 1 | NOT DECIDED |
| C-7R.5.4.1.3 — Preview affected consuming components | Changes | 1 | NOT DECIDED |
| C-7R.5.4.1.4 — Preview affected precomputed results | Fails closed by | 1 | NOT DECIDED |
| C-7R.5.4.1.4 — Preview affected precomputed results | Fed by | 1 | NOT DECIDED |
| C-7R.5.4.1.4 — Preview affected precomputed results | Gated by | 1 | NOT DECIDED |
| C-7R.5.4.1.4 — Preview affected precomputed results | Changes | 1 | NOT DECIDED |
| C-7R.5.4.1.5 — Preview affected other mode versions | Fails closed by | 1 | NOT DECIDED |
| C-7R.5.4.1.5 — Preview affected other mode versions | Fed by | 1 | NOT DECIDED |
| C-7R.5.4.1.5 — Preview affected other mode versions | Gated by | 1 | NOT DECIDED |
| C-7R.5.4.1.5 — Preview affected other mode versions | Changes | 1 | NOT DECIDED |
| C-7R.5.4.2 — New configuration version preservation | Fails closed by | 1 | NOT DECIDED |
| C-7R.5.4.2 — New configuration version preservation | Fed by | 1 | NOT DECIDED |
| C-7R.5.4.2 — New configuration version preservation | Gated by | 1 | NOT DECIDED |
| C-7R.5.4.2 — New configuration version preservation | Changes | 1 | NOT DECIDED |
| C-7R.5.5 — Invalid configuration request handling | Fed by | 1 | NOT DECIDED |
| C-7R.5.5 — Invalid configuration request handling | Gated by | 1 | NOT DECIDED |
| C-7R.5.5 — Invalid configuration request handling | Changes | 1 | NOT DECIDED |
| C-7R.5.6 — Append-only relevance change history | Fails closed by | 1 | NOT DECIDED |
| C-7R.5.6 — Append-only relevance change history | Fed by | 1 | NOT DECIDED |
| C-7R.5.6 — Append-only relevance change history | Gated by | 1 | NOT DECIDED |
| C-7R.5.6 — Append-only relevance change history | Changes | 1 | NOT DECIDED |
| C-7R.6 — Mouth-produced dimension validation | Gated by | 1 | NOT DECIDED |
| C-7R.6 — Mouth-produced dimension validation | Changes | 1 | NOT DECIDED |
| C-7R.6.1 — Six deterministic validation checks | Gated by | 1 | NOT DECIDED |
| C-7R.6.1 — Six deterministic validation checks | Changes | 1 | NOT DECIDED |
| C-7R.6.1.1 — Schema and bounds validation | Gated by | 1 | NOT DECIDED |
| C-7R.6.1.1 — Schema and bounds validation | Changes | 1 | NOT DECIDED |
| C-7R.6.1.1.1 — Validation value present | Fed by | 1 | NOT DECIDED |
| C-7R.6.1.1.1 — Validation value present | Gated by | 1 | NOT DECIDED |
| C-7R.6.1.1.1 — Validation value present | Changes | 1 | NOT DECIDED |
| C-7R.6.1.1.2 — Validation value correct type | Fed by | 1 | NOT DECIDED |
| C-7R.6.1.1.2 — Validation value correct type | Gated by | 1 | NOT DECIDED |
| C-7R.6.1.1.2 — Validation value correct type | Changes | 1 | NOT DECIDED |
| C-7R.6.1.1.3 — Validation value within declared bounds | Fed by | 1 | NOT DECIDED |
| C-7R.6.1.1.3 — Validation value within declared bounds | Gated by | 1 | NOT DECIDED |
| C-7R.6.1.1.3 — Validation value within declared bounds | Changes | 1 | NOT DECIDED |
| C-7R.6.1.2 — Required provenance validation | Fed by | 1 | NOT DECIDED |
| C-7R.6.1.2 — Required provenance validation | Gated by | 1 | NOT DECIDED |
| C-7R.6.1.2 — Required provenance validation | Changes | 1 | NOT DECIDED |
| C-7R.6.1.3 — Declared grounding check | Fed by | 1 | NOT DECIDED |
| C-7R.6.1.3 — Declared grounding check | Gated by | 1 | NOT DECIDED |
| C-7R.6.1.3 — Declared grounding check | Changes | 1 | NOT DECIDED |
| C-7R.6.1.4 — Out-of-scope detection | Fed by | 1 | NOT DECIDED |
| C-7R.6.1.4 — Out-of-scope detection | Gated by | 1 | NOT DECIDED |
| C-7R.6.1.4 — Out-of-scope detection | Changes | 1 | NOT DECIDED |
| C-7R.6.1.5 — Direct structural contradiction check | Fed by | 1 | NOT DECIDED |
| C-7R.6.1.5 — Direct structural contradiction check | Gated by | 1 | NOT DECIDED |
| C-7R.6.1.5 — Direct structural contradiction check | Changes | 1 | NOT DECIDED |
| C-7R.6.1.6 — Grounding-relative certainty check | Fed by | 1 | NOT DECIDED |
| C-7R.6.1.6 — Grounding-relative certainty check | Gated by | 1 | NOT DECIDED |
| C-7R.6.1.6 — Grounding-relative certainty check | Changes | 1 | NOT DECIDED |
| C-7R.6.2 — Three mouth validation outcomes | Fails closed by | 1 | NOT DECIDED |
| C-7R.6.2 — Three mouth validation outcomes | Gated by | 1 | NOT DECIDED |
| C-7R.6.2 — Three mouth validation outcomes | Changes | 1 | NOT DECIDED |
| C-7R.6.2.1 — Validated relevance dimension | Fails closed by | 1 | NOT DECIDED |
| C-7R.6.2.1 — Validated relevance dimension | Fed by | 1 | NOT DECIDED |
| C-7R.6.2.1 — Validated relevance dimension | Gated by | 1 | NOT DECIDED |
| C-7R.6.2.1 — Validated relevance dimension | Changes | 1 | NOT DECIDED |
| C-7R.6.2.2 — Failed relevance dimension | Gated by | 1 | NOT DECIDED |
| C-7R.6.2.2 — Failed relevance dimension | Changes | 1 | NOT DECIDED |
| C-7R.6.2.2.1 — Invented dimension failure | Fed by | 1 | NOT DECIDED |
| C-7R.6.2.2.1 — Invented dimension failure | Gated by | 1 | NOT DECIDED |
| C-7R.6.2.2.1 — Invented dimension failure | Changes | 1 | NOT DECIDED |
| C-7R.6.2.2.2 — Structurally invalid dimension failure | Fed by | 1 | NOT DECIDED |
| C-7R.6.2.2.2 — Structurally invalid dimension failure | Gated by | 1 | NOT DECIDED |
| C-7R.6.2.2.2 — Structurally invalid dimension failure | Changes | 1 | NOT DECIDED |
| C-7R.6.2.2.3 — Contradictory dimension failure | Fed by | 1 | NOT DECIDED |
| C-7R.6.2.2.3 — Contradictory dimension failure | Gated by | 1 | NOT DECIDED |
| C-7R.6.2.2.3 — Contradictory dimension failure | Changes | 1 | NOT DECIDED |
| C-7R.6.2.2.4 — Out-of-bounds dimension failure | Fed by | 1 | NOT DECIDED |
| C-7R.6.2.2.4 — Out-of-bounds dimension failure | Gated by | 1 | NOT DECIDED |
| C-7R.6.2.2.4 — Out-of-bounds dimension failure | Changes | 1 | NOT DECIDED |
| C-7R.6.2.2.5 — Missing-provenance dimension failure | Fed by | 1 | NOT DECIDED |
| C-7R.6.2.2.5 — Missing-provenance dimension failure | Gated by | 1 | NOT DECIDED |
| C-7R.6.2.2.5 — Missing-provenance dimension failure | Changes | 1 | NOT DECIDED |
| C-7R.6.2.2.6 — Undeclared-input dimension failure | Fed by | 1 | NOT DECIDED |
| C-7R.6.2.2.6 — Undeclared-input dimension failure | Gated by | 1 | NOT DECIDED |
| C-7R.6.2.2.6 — Undeclared-input dimension failure | Changes | 1 | NOT DECIDED |
| C-7R.6.2.3 — Unresolved relevance dimension | Fails closed by | 1 | NOT DECIDED |
| C-7R.6.2.3 — Unresolved relevance dimension | Fed by | 1 | NOT DECIDED |
| C-7R.6.2.3 — Unresolved relevance dimension | Gated by | 1 | NOT DECIDED |
| C-7R.6.2.3 — Unresolved relevance dimension | Changes | 1 | NOT DECIDED |
| C-7R.6.3 — Optional declared model-based validation | Fails closed by | 1 | NOT DECIDED |
| C-7R.6.3 — Optional declared model-based validation | Gated by | 1 | NOT DECIDED |
| C-7R.6.3 — Optional declared model-based validation | Changes | 1 | NOT DECIDED |
| C-7R.6.3.1 — Model-validator declaration | Fails closed by | 1 | NOT DECIDED |
| C-7R.6.3.1 — Model-validator declaration | Fed by | 1 | NOT DECIDED |
| C-7R.6.3.1 — Model-validator declaration | Gated by | 1 | NOT DECIDED |
| C-7R.6.3.1 — Model-validator declaration | Changes | 1 | NOT DECIDED |
| C-7R.6.3.2 — Declared validator independence | Fed by | 1 | NOT DECIDED |
| C-7R.6.3.2 — Declared validator independence | Gated by | 1 | NOT DECIDED |
| C-7R.6.3.2 — Declared validator independence | Changes | 1 | NOT DECIDED |
| C-7R.6.3.3 — Separate model-validation result | Fails closed by | 1 | NOT DECIDED |
| C-7R.6.3.3 — Separate model-validation result | Fed by | 1 | NOT DECIDED |
| C-7R.6.3.3 — Separate model-validation result | Gated by | 1 | NOT DECIDED |
| C-7R.6.3.3 — Separate model-validation result | Changes | 1 | NOT DECIDED |
| C-7R.6.3.4 — Producer-validator disagreement handling | Fails closed by | 1 | NOT DECIDED |
| C-7R.6.3.4 — Producer-validator disagreement handling | Gated by | 1 | NOT DECIDED |
| C-7R.6.3.4 — Producer-validator disagreement handling | Changes | 1 | NOT DECIDED |
| C-7R.6.4 — Mouth dimensions cannot be categorical gates | Fed by | 1 | NOT DECIDED |
| C-7R.6.4 — Mouth dimensions cannot be categorical gates | Gated by | 1 | NOT DECIDED |
| C-7R.6.4 — Mouth dimensions cannot be categorical gates | Changes | 1 | NOT DECIDED |
| C-7R.7 — Minimum shared relevance vocabulary | Fails closed by | 1 | NOT DECIDED |
| C-7R.7 — Minimum shared relevance vocabulary | Gated by | 1 | NOT DECIDED |
| C-7R.7 — Minimum shared relevance vocabulary | Changes | 1 | NOT DECIDED |
| C-7R.7.1 — Shared deterministic gate vocabulary | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.1 — Shared deterministic gate vocabulary | Gated by | 1 | NOT DECIDED |
| C-7R.7.1 — Shared deterministic gate vocabulary | Changes | 1 | NOT DECIDED |
| C-7R.7.1.1 — same_thread_or_group | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.1.1 — same_thread_or_group | Fed by | 1 | NOT DECIDED |
| C-7R.7.1.1 — same_thread_or_group | Gated by | 1 | NOT DECIDED |
| C-7R.7.1.1 — same_thread_or_group | Changes | 1 | NOT DECIDED |
| C-7R.7.1.2 — precedes_target_in_same_thread | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.1.2 — precedes_target_in_same_thread | Fed by | 1 | NOT DECIDED |
| C-7R.7.1.2 — precedes_target_in_same_thread | Gated by | 1 | NOT DECIDED |
| C-7R.7.1.2 — precedes_target_in_same_thread | Changes | 1 | NOT DECIDED |
| C-7R.7.1.3 — within_declared_time_range | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.1.3 — within_declared_time_range | Fed by | 1 | NOT DECIDED |
| C-7R.7.1.3 — within_declared_time_range | Gated by | 1 | NOT DECIDED |
| C-7R.7.1.3 — within_declared_time_range | Changes | 1 | NOT DECIDED |
| C-7R.7.1.4 — object_type_matches | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.1.4 — object_type_matches | Fed by | 1 | NOT DECIDED |
| C-7R.7.1.4 — object_type_matches | Gated by | 1 | NOT DECIDED |
| C-7R.7.1.4 — object_type_matches | Changes | 1 | NOT DECIDED |
| C-7R.7.2 — Shared named dimension vocabulary | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2 — Shared named dimension vocabulary | Gated by | 1 | NOT DECIDED |
| C-7R.7.2 — Shared named dimension vocabulary | Changes | 1 | NOT DECIDED |
| C-7R.7.2.1 — semantic_similarity | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.1 — semantic_similarity | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.1 — semantic_similarity | Changes | 1 | NOT DECIDED |
| C-7R.7.2.2 — temporal_distance | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.2 — temporal_distance | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.2 — temporal_distance | Changes | 1 | NOT DECIDED |
| C-7R.7.2.3 — positional_distance | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.3 — positional_distance | Fed by | 1 | NOT DECIDED |
| C-7R.7.2.3 — positional_distance | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.3 — positional_distance | Changes | 1 | NOT DECIDED |
| C-7R.7.2.4 — currentness_status | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.4 — currentness_status | Changes | 1 | NOT DECIDED |
| C-7R.7.2.5 — explicit_links | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.5 — explicit_links | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.5 — explicit_links | Changes | 1 | NOT DECIDED |
| C-7R.7.2.5.1 — Explicit-link type | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.5.1 — Explicit-link type | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.5.1 — Explicit-link type | Changes | 1 | NOT DECIDED |
| C-7R.7.2.5.1.1 — same Person-Box link | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.5.1.1 — same Person-Box link | Fed by | 1 | NOT DECIDED |
| C-7R.7.2.5.1.1 — same Person-Box link | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.5.1.1 — same Person-Box link | Changes | 1 | NOT DECIDED |
| C-7R.7.2.5.1.2 — same confirmed theme link | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.5.1.2 — same confirmed theme link | Fed by | 1 | NOT DECIDED |
| C-7R.7.2.5.1.2 — same confirmed theme link | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.5.1.2 — same confirmed theme link | Changes | 1 | NOT DECIDED |
| C-7R.7.2.5.1.3 — same proposed theme link | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.5.1.3 — same proposed theme link | Fed by | 1 | NOT DECIDED |
| C-7R.7.2.5.1.3 — same proposed theme link | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.5.1.3 — same proposed theme link | Changes | 1 | NOT DECIDED |
| C-7R.7.2.5.1.4 — same derived_from chain link | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.5.1.4 — same derived_from chain link | Fed by | 1 | NOT DECIDED |
| C-7R.7.2.5.1.4 — same derived_from chain link | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.5.1.4 — same derived_from chain link | Changes | 1 | NOT DECIDED |
| C-7R.7.2.5.1.5 — shared root IDs in a telling link | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.5.1.5 — shared root IDs in a telling link | Fed by | 1 | NOT DECIDED |
| C-7R.7.2.5.1.5 — shared root IDs in a telling link | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.5.1.5 — shared root IDs in a telling link | Changes | 1 | NOT DECIDED |
| C-7R.7.2.5.2 — Explicit-link status | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.5.2 — Explicit-link status | Fed by | 1 | NOT DECIDED |
| C-7R.7.2.5.2 — Explicit-link status | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.5.2 — Explicit-link status | Changes | 1 | NOT DECIDED |
| C-7R.7.2.5.3 — Explicit-link provenance | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.5.3 — Explicit-link provenance | Fed by | 1 | NOT DECIDED |
| C-7R.7.2.5.3 — Explicit-link provenance | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.5.3 — Explicit-link provenance | Changes | 1 | NOT DECIDED |
| C-7R.7.2.6 — ness_response_links | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.6 — ness_response_links | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.6 — ness_response_links | Changes | 1 | NOT DECIDED |
| C-7R.7.2.6.1 — Response-link type | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.6.1 — Response-link type | Fed by | 1 | NOT DECIDED |
| C-7R.7.2.6.1 — Response-link type | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.6.1 — Response-link type | Changes | 1 | NOT DECIDED |
| C-7R.7.2.6.2 — Response-link scope | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.6.2 — Response-link scope | Fed by | 1 | NOT DECIDED |
| C-7R.7.2.6.2 — Response-link scope | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.6.2 — Response-link scope | Changes | 1 | NOT DECIDED |
| C-7R.7.2.6.3 — Response-link target identifier | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.6.3 — Response-link target identifier | Fed by | 1 | NOT DECIDED |
| C-7R.7.2.6.3 — Response-link target identifier | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.6.3 — Response-link target identifier | Changes | 1 | NOT DECIDED |
| C-7R.7.2.6.4 — Response-link timestamp | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.6.4 — Response-link timestamp | Fed by | 1 | NOT DECIDED |
| C-7R.7.2.6.4 — Response-link timestamp | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.6.4 — Response-link timestamp | Changes | 1 | NOT DECIDED |
| C-7R.7.2.7 — proposal_acceptance_outcome | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.7 — proposal_acceptance_outcome | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.7 — proposal_acceptance_outcome | Changes | 1 | NOT DECIDED |
| C-7R.7.2.8 — reading_context_status | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.8 — reading_context_status | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.8 — reading_context_status | Changes | 1 | NOT DECIDED |
| C-7R.7.2.9 — active_clash_links | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.9 — active_clash_links | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.9 — active_clash_links | Changes | 1 | NOT DECIDED |
| C-7R.7.2.9.1 — Clash-link record identifier | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.9.1 — Clash-link record identifier | Fed by | 1 | NOT DECIDED |
| C-7R.7.2.9.1 — Clash-link record identifier | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.9.1 — Clash-link record identifier | Changes | 1 | NOT DECIDED |
| C-7R.7.2.9.2 — Clash-link type | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.9.2 — Clash-link type | Fed by | 1 | NOT DECIDED |
| C-7R.7.2.9.2 — Clash-link type | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.9.2 — Clash-link type | Changes | 1 | NOT DECIDED |
| C-7R.7.2.9.3 — Clash-link detection mode | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.2.9.3 — Clash-link detection mode | Fed by | 1 | NOT DECIDED |
| C-7R.7.2.9.3 — Clash-link detection mode | Gated by | 1 | NOT DECIDED |
| C-7R.7.2.9.3 — Clash-link detection mode | Changes | 1 | NOT DECIDED |
| C-7R.7.3 — Retrieval-channel provenance boundary | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.3 — Retrieval-channel provenance boundary | Gated by | 1 | NOT DECIDED |
| C-7R.7.3 — Retrieval-channel provenance boundary | Changes | 1 | NOT DECIDED |
| C-7R.7.4 — Local dimension and shared-vocabulary extension | Fails closed by | 1 | NOT DECIDED |
| C-7R.7.4 — Local dimension and shared-vocabulary extension | Fed by | 1 | NOT DECIDED |
| C-7R.7.4 — Local dimension and shared-vocabulary extension | Changes | 1 | NOT DECIDED |
| C-7R.8 — Living State Web relevance boundary | Fails closed by | 1 | NOT DECIDED |
| C-7R.8.1 — Review trigger is not review evidence | Gated by | 1 | NOT DECIDED |
| C-7R.8.1 — Review trigger is not review evidence | Changes | 1 | NOT DECIDED |
| C-7R.8.2 — Relevance and currentness are separate properties | Fails closed by | 1 | NOT DECIDED |
| C-7R.8.2 — Relevance and currentness are separate properties | Fed by | 1 | NOT DECIDED |
| C-7R.8.2 — Relevance and currentness are separate properties | Gated by | 1 | NOT DECIDED |
| C-7R.8.2 — Relevance and currentness are separate properties | Changes | 1 | NOT DECIDED |
| C-7R.8.3 — Separate Ness currentness-evidence event | Fails closed by | 1 | NOT DECIDED |
| C-7R.8.3 — Separate Ness currentness-evidence event | Fed by | 1 | NOT DECIDED |
| C-7R.8.3 — Separate Ness currentness-evidence event | Gated by | 1 | NOT DECIDED |
| C-7R.8.3 — Separate Ness currentness-evidence event | Changes | 1 | NOT DECIDED |
| C-7R.8.4 — Forbidden relevance-currentness feedback chain | Fed by | 1 | NOT DECIDED |
| C-7R.8.4 — Forbidden relevance-currentness feedback chain | Gated by | 1 | NOT DECIDED |
| C-7R.8.4 — Forbidden relevance-currentness feedback chain | Changes | 1 | NOT DECIDED |
| C-7R.9 — Tier 1 structured purpose | Changes | 1 | NOT DECIDED |
| C-7R.9.1 — Required controlled purpose type | Fails closed by | 1 | NOT DECIDED |
| C-7R.9.1 — Required controlled purpose type | Fed by | 1 | NOT DECIDED |
| C-7R.9.1 — Required controlled purpose type | Gated by | 1 | NOT DECIDED |
| C-7R.9.1 — Required controlled purpose type | Changes | 1 | NOT DECIDED |
| C-7R.9.2 — Optional explanatory purpose label | Fails closed by | 1 | NOT DECIDED |
| C-7R.9.2 — Optional explanatory purpose label | Fed by | 1 | NOT DECIDED |
| C-7R.9.2 — Optional explanatory purpose label | Gated by | 1 | NOT DECIDED |
| C-7R.9.2 — Optional explanatory purpose label | Changes | 1 | NOT DECIDED |
| C-7R.9.3 — Five controlled purpose values | Fails closed by | 1 | NOT DECIDED |
| C-7R.9.3 — Five controlled purpose values | Gated by | 1 | NOT DECIDED |
| C-7R.9.3 — Five controlled purpose values | Changes | 1 | NOT DECIDED |
| C-7R.9.3.1 — retrieval_context_selection | Fails closed by | 1 | NOT DECIDED |
| C-7R.9.3.1 — retrieval_context_selection | Fed by | 1 | NOT DECIDED |
| C-7R.9.3.1 — retrieval_context_selection | Gated by | 1 | NOT DECIDED |
| C-7R.9.3.1 — retrieval_context_selection | Changes | 1 | NOT DECIDED |
| C-7R.9.3.2 — view_assembly | Fails closed by | 1 | NOT DECIDED |
| C-7R.9.3.2 — view_assembly | Fed by | 1 | NOT DECIDED |
| C-7R.9.3.2 — view_assembly | Gated by | 1 | NOT DECIDED |
| C-7R.9.3.2 — view_assembly | Changes | 1 | NOT DECIDED |
| C-7R.9.3.3 — action_surfacing | Fails closed by | 1 | NOT DECIDED |
| C-7R.9.3.3 — action_surfacing | Fed by | 1 | NOT DECIDED |
| C-7R.9.3.3 — action_surfacing | Gated by | 1 | NOT DECIDED |
| C-7R.9.3.3 — action_surfacing | Changes | 1 | NOT DECIDED |
| C-7R.9.3.4 — reread_trigger_evaluation | Fails closed by | 1 | NOT DECIDED |
| C-7R.9.3.4 — reread_trigger_evaluation | Fed by | 1 | NOT DECIDED |
| C-7R.9.3.4 — reread_trigger_evaluation | Gated by | 1 | NOT DECIDED |
| C-7R.9.3.4 — reread_trigger_evaluation | Changes | 1 | NOT DECIDED |
| C-7R.9.3.5 — state_review_trigger_evaluation | Fails closed by | 1 | NOT DECIDED |
| C-7R.9.3.5 — state_review_trigger_evaluation | Fed by | 1 | NOT DECIDED |
| C-7R.9.3.5 — state_review_trigger_evaluation | Gated by | 1 | NOT DECIDED |
| C-7R.9.3.5 — state_review_trigger_evaluation | Changes | 1 | NOT DECIDED |
| C-7R.9.4 — Controlled-purpose vocabulary change | Fails closed by | 1 | NOT DECIDED |
| C-7R.9.4 — Controlled-purpose vocabulary change | Fed by | 1 | NOT DECIDED |
| C-7R.9.4 — Controlled-purpose vocabulary change | Changes | 1 | NOT DECIDED |
| C-7R.10 — Tier-boundary unresolved-rule reference | Gated by | 1 | NOT DECIDED |
| C-7R.10 — Tier-boundary unresolved-rule reference | Changes | 1 | NOT DECIDED |
| C-7R.10.1 — Unresolved-rule identifier reference | Fails closed by | 1 | NOT DECIDED |
| C-7R.10.1 — Unresolved-rule identifier reference | Fed by | 1 | NOT DECIDED |
| C-7R.10.1 — Unresolved-rule identifier reference | Gated by | 1 | NOT DECIDED |
| C-7R.10.1 — Unresolved-rule identifier reference | Changes | 1 | NOT DECIDED |
| C-7R.10.2 — Unresolved-rule version reference | Fails closed by | 1 | NOT DECIDED |
| C-7R.10.2 — Unresolved-rule version reference | Fed by | 1 | NOT DECIDED |
| C-7R.10.2 — Unresolved-rule version reference | Gated by | 1 | NOT DECIDED |
| C-7R.10.2 — Unresolved-rule version reference | Changes | 1 | NOT DECIDED |
| C-7R.10.3 — Local-rule change and stale-reference handling | Fed by | 1 | NOT DECIDED |
| C-7R.10.3 — Local-rule change and stale-reference handling | Gated by | 1 | NOT DECIDED |
| C-7R.10.3 — Local-rule change and stale-reference handling | Changes | 1 | NOT DECIDED |
| C-7R.11 — Relevance disagreement record | Fails closed by | 1 | NOT DECIDED |
| C-7R.11 — Relevance disagreement record | Gated by | 1 | NOT DECIDED |
| C-7R.11 — Relevance disagreement record | Changes | 1 | NOT DECIDED |
| C-7R.11.1 — Disagreement stable identifier | Fails closed by | 1 | NOT DECIDED |
| C-7R.11.1 — Disagreement stable identifier | Fed by | 1 | NOT DECIDED |
| C-7R.11.1 — Disagreement stable identifier | Gated by | 1 | NOT DECIDED |
| C-7R.11.1 — Disagreement stable identifier | Changes | 1 | NOT DECIDED |
| C-7R.11.2 — Disagreement producer-result pointer | Fails closed by | 1 | NOT DECIDED |
| C-7R.11.2 — Disagreement producer-result pointer | Fed by | 1 | NOT DECIDED |
| C-7R.11.2 — Disagreement producer-result pointer | Gated by | 1 | NOT DECIDED |
| C-7R.11.2 — Disagreement producer-result pointer | Changes | 1 | NOT DECIDED |
| C-7R.11.3 — Disagreement validator-result pointer | Fails closed by | 1 | NOT DECIDED |
| C-7R.11.3 — Disagreement validator-result pointer | Fed by | 1 | NOT DECIDED |
| C-7R.11.3 — Disagreement validator-result pointer | Gated by | 1 | NOT DECIDED |
| C-7R.11.3 — Disagreement validator-result pointer | Changes | 1 | NOT DECIDED |
| C-7R.11.4 — Disagreement type vocabulary | Fails closed by | 1 | NOT DECIDED |
| C-7R.11.4 — Disagreement type vocabulary | Gated by | 1 | NOT DECIDED |
| C-7R.11.4 — Disagreement type vocabulary | Changes | 1 | NOT DECIDED |
| C-7R.11.4.1 — value out of bounds | Fails closed by | 1 | NOT DECIDED |
| C-7R.11.4.1 — value out of bounds | Fed by | 1 | NOT DECIDED |
| C-7R.11.4.1 — value out of bounds | Gated by | 1 | NOT DECIDED |
| C-7R.11.4.1 — value out of bounds | Changes | 1 | NOT DECIDED |
| C-7R.11.4.2 — grounding claim contradicted | Fails closed by | 1 | NOT DECIDED |
| C-7R.11.4.2 — grounding claim contradicted | Fed by | 1 | NOT DECIDED |
| C-7R.11.4.2 — grounding claim contradicted | Gated by | 1 | NOT DECIDED |
| C-7R.11.4.2 — grounding claim contradicted | Changes | 1 | NOT DECIDED |
| C-7R.11.4.3 — certainty exceeds support | Fails closed by | 1 | NOT DECIDED |
| C-7R.11.4.3 — certainty exceeds support | Fed by | 1 | NOT DECIDED |
| C-7R.11.4.3 — certainty exceeds support | Gated by | 1 | NOT DECIDED |
| C-7R.11.4.3 — certainty exceeds support | Changes | 1 | NOT DECIDED |
| C-7R.11.5 — Disagreement producer identity and version | Fails closed by | 1 | NOT DECIDED |
| C-7R.11.5 — Disagreement producer identity and version | Gated by | 1 | NOT DECIDED |
| C-7R.11.5 — Disagreement producer identity and version | Changes | 1 | NOT DECIDED |
| C-7R.11.6 — Disagreement validator identity and independence | Fails closed by | 1 | NOT DECIDED |
| C-7R.11.6 — Disagreement validator identity and independence | Gated by | 1 | NOT DECIDED |
| C-7R.11.6 — Disagreement validator identity and independence | Changes | 1 | NOT DECIDED |
| C-7R.11.7 — Disagreement uncertainty behavior rule | Fails closed by | 1 | NOT DECIDED |
| C-7R.11.7 — Disagreement uncertainty behavior rule | Gated by | 1 | NOT DECIDED |
| C-7R.11.7 — Disagreement uncertainty behavior rule | Changes | 1 | NOT DECIDED |
| C-7R.11.8 — Disagreement resulting dimension state | Fails closed by | 1 | NOT DECIDED |
| C-7R.11.8 — Disagreement resulting dimension state | Fed by | 1 | NOT DECIDED |
| C-7R.11.8 — Disagreement resulting dimension state | Gated by | 1 | NOT DECIDED |
| C-7R.11.8 — Disagreement resulting dimension state | Changes | 1 | NOT DECIDED |
| C-7R.11.9 — Disagreement timestamp | Fails closed by | 1 | NOT DECIDED |
| C-7R.11.9 — Disagreement timestamp | Fed by | 1 | NOT DECIDED |
| C-7R.11.9 — Disagreement timestamp | Gated by | 1 | NOT DECIDED |
| C-7R.11.9 — Disagreement timestamp | Changes | 1 | NOT DECIDED |
| C-7R.12 — Completed relevance event record | Fails closed by | 1 | NOT DECIDED |
| C-7R.12 — Completed relevance event record | Gated by | 1 | NOT DECIDED |
| C-7R.12 — Completed relevance event record | Changes | 1 | NOT DECIDED |
| C-7R.12.1 — Evaluation stable identifier | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.1 — Evaluation stable identifier | Fed by | 1 | NOT DECIDED |
| C-7R.12.1 — Evaluation stable identifier | Gated by | 1 | NOT DECIDED |
| C-7R.12.1 — Evaluation stable identifier | Changes | 1 | NOT DECIDED |
| C-7R.12.2 — Evaluation mode identifier and version | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.2 — Evaluation mode identifier and version | Gated by | 1 | NOT DECIDED |
| C-7R.12.2 — Evaluation mode identifier and version | Changes | 1 | NOT DECIDED |
| C-7R.12.3 — Evaluation purpose type and label | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.3 — Evaluation purpose type and label | Gated by | 1 | NOT DECIDED |
| C-7R.12.3 — Evaluation purpose type and label | Changes | 1 | NOT DECIDED |
| C-7R.12.4 — Evaluation consuming component | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.4 — Evaluation consuming component | Fed by | 1 | NOT DECIDED |
| C-7R.12.4 — Evaluation consuming component | Gated by | 1 | NOT DECIDED |
| C-7R.12.4 — Evaluation consuming component | Changes | 1 | NOT DECIDED |
| C-7R.12.5 — Evaluation exact context or request identifier | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.5 — Evaluation exact context or request identifier | Fed by | 1 | NOT DECIDED |
| C-7R.12.5 — Evaluation exact context or request identifier | Gated by | 1 | NOT DECIDED |
| C-7R.12.5 — Evaluation exact context or request identifier | Changes | 1 | NOT DECIDED |
| C-7R.12.6 — Evaluation target objects | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.6 — Evaluation target objects | Gated by | 1 | NOT DECIDED |
| C-7R.12.6 — Evaluation target objects | Changes | 1 | NOT DECIDED |
| C-7R.12.6.1 — Evaluation target object type | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.6.1 — Evaluation target object type | Fed by | 1 | NOT DECIDED |
| C-7R.12.6.1 — Evaluation target object type | Gated by | 1 | NOT DECIDED |
| C-7R.12.6.1 — Evaluation target object type | Changes | 1 | NOT DECIDED |
| C-7R.12.6.2 — Evaluation target object identifier | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.6.2 — Evaluation target object identifier | Fed by | 1 | NOT DECIDED |
| C-7R.12.6.2 — Evaluation target object identifier | Gated by | 1 | NOT DECIDED |
| C-7R.12.6.2 — Evaluation target object identifier | Changes | 1 | NOT DECIDED |
| C-7R.12.7 — Evaluation candidate object type | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.7 — Evaluation candidate object type | Fed by | 1 | NOT DECIDED |
| C-7R.12.7 — Evaluation candidate object type | Gated by | 1 | NOT DECIDED |
| C-7R.12.7 — Evaluation candidate object type | Changes | 1 | NOT DECIDED |
| C-7R.12.8 — Evaluation mode | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.8 — Evaluation mode | Fed by | 1 | NOT DECIDED |
| C-7R.12.8 — Evaluation mode | Gated by | 1 | NOT DECIDED |
| C-7R.12.8 — Evaluation mode | Changes | 1 | NOT DECIDED |
| C-7R.12.9 — Evaluation trigger identifier | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.9 — Evaluation trigger identifier | Fed by | 1 | NOT DECIDED |
| C-7R.12.9 — Evaluation trigger identifier | Gated by | 1 | NOT DECIDED |
| C-7R.12.9 — Evaluation trigger identifier | Changes | 1 | NOT DECIDED |
| C-7R.12.10 — Evaluation outcome summary counts | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.10 — Evaluation outcome summary counts | Gated by | 1 | NOT DECIDED |
| C-7R.12.10 — Evaluation outcome summary counts | Changes | 1 | NOT DECIDED |
| C-7R.12.10.1 — Gate-passed candidate count | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.10.1 — Gate-passed candidate count | Fed by | 1 | NOT DECIDED |
| C-7R.12.10.1 — Gate-passed candidate count | Gated by | 1 | NOT DECIDED |
| C-7R.12.10.1 — Gate-passed candidate count | Changes | 1 | NOT DECIDED |
| C-7R.12.10.2 — Gate-excluded candidate count | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.10.2 — Gate-excluded candidate count | Fed by | 1 | NOT DECIDED |
| C-7R.12.10.2 — Gate-excluded candidate count | Gated by | 1 | NOT DECIDED |
| C-7R.12.10.2 — Gate-excluded candidate count | Changes | 1 | NOT DECIDED |
| C-7R.12.10.3 — Unresolved-dimension candidate count | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.10.3 — Unresolved-dimension candidate count | Fed by | 1 | NOT DECIDED |
| C-7R.12.10.3 — Unresolved-dimension candidate count | Gated by | 1 | NOT DECIDED |
| C-7R.12.10.3 — Unresolved-dimension candidate count | Changes | 1 | NOT DECIDED |
| C-7R.12.10.4 — Failed-dimension candidate count | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.10.4 — Failed-dimension candidate count | Fed by | 1 | NOT DECIDED |
| C-7R.12.10.4 — Failed-dimension candidate count | Gated by | 1 | NOT DECIDED |
| C-7R.12.10.4 — Failed-dimension candidate count | Changes | 1 | NOT DECIDED |
| C-7R.12.10.5 — Disagreement-producing candidate count | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.10.5 — Disagreement-producing candidate count | Fed by | 1 | NOT DECIDED |
| C-7R.12.10.5 — Disagreement-producing candidate count | Gated by | 1 | NOT DECIDED |
| C-7R.12.10.5 — Disagreement-producing candidate count | Changes | 1 | NOT DECIDED |
| C-7R.12.11 — Individual relevance-judgment pointers | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.11 — Individual relevance-judgment pointers | Fed by | 1 | NOT DECIDED |
| C-7R.12.11 — Individual relevance-judgment pointers | Gated by | 1 | NOT DECIDED |
| C-7R.12.11 — Individual relevance-judgment pointers | Changes | 1 | NOT DECIDED |
| C-7R.12.12 — Evaluation disagreement presence and pointers | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.12 — Evaluation disagreement presence and pointers | Gated by | 1 | NOT DECIDED |
| C-7R.12.12 — Evaluation disagreement presence and pointers | Changes | 1 | NOT DECIDED |
| C-7R.12.12.1 — Evaluation disagreement-presence fact | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.12.1 — Evaluation disagreement-presence fact | Fed by | 1 | NOT DECIDED |
| C-7R.12.12.1 — Evaluation disagreement-presence fact | Gated by | 1 | NOT DECIDED |
| C-7R.12.12.1 — Evaluation disagreement-presence fact | Changes | 1 | NOT DECIDED |
| C-7R.12.12.2 — Evaluation disagreement-record pointers | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.12.2 — Evaluation disagreement-record pointers | Fed by | 1 | NOT DECIDED |
| C-7R.12.12.2 — Evaluation disagreement-record pointers | Gated by | 1 | NOT DECIDED |
| C-7R.12.12.2 — Evaluation disagreement-record pointers | Changes | 1 | NOT DECIDED |
| C-7R.12.13 — Evaluation completion timestamp | Fails closed by | 1 | NOT DECIDED |
| C-7R.12.13 — Evaluation completion timestamp | Fed by | 1 | NOT DECIDED |
| C-7R.12.13 — Evaluation completion timestamp | Gated by | 1 | NOT DECIDED |
| C-7R.12.13 — Evaluation completion timestamp | Changes | 1 | NOT DECIDED |
| C-7R.13 — Per-judgment override pattern observation | Fails closed by | 1 | NOT DECIDED |
| C-7R.13 — Per-judgment override pattern observation | Changes | 1 | NOT DECIDED |
| C-7R.13.1 — Three simultaneous override-pattern conditions | Gated by | 1 | NOT DECIDED |
| C-7R.13.1 — Three simultaneous override-pattern conditions | Changes | 1 | NOT DECIDED |
| C-7R.13.1.1 — Same override mode and version | Fails closed by | 1 | NOT DECIDED |
| C-7R.13.1.1 — Same override mode and version | Fed by | 1 | NOT DECIDED |
| C-7R.13.1.1 — Same override mode and version | Gated by | 1 | NOT DECIDED |
| C-7R.13.1.1 — Same override mode and version | Changes | 1 | NOT DECIDED |
| C-7R.13.1.2 — Same override target | Fails closed by | 1 | NOT DECIDED |
| C-7R.13.1.2 — Same override target | Fed by | 1 | NOT DECIDED |
| C-7R.13.1.2 — Same override target | Gated by | 1 | NOT DECIDED |
| C-7R.13.1.2 — Same override target | Changes | 1 | NOT DECIDED |
| C-7R.13.1.3 — Same correction direction | Fails closed by | 1 | NOT DECIDED |
| C-7R.13.1.3 — Same correction direction | Fed by | 1 | NOT DECIDED |
| C-7R.13.1.3 — Same correction direction | Gated by | 1 | NOT DECIDED |
| C-7R.13.1.3 — Same correction direction | Changes | 1 | NOT DECIDED |
| C-7R.13.2 — Override-pattern presentation limits | Fails closed by | 1 | NOT DECIDED |
| C-7R.13.2 — Override-pattern presentation limits | Fed by | 1 | NOT DECIDED |
| C-7R.13.2 — Override-pattern presentation limits | Gated by | 1 | NOT DECIDED |
| C-7R.13.2 — Override-pattern presentation limits | Changes | 1 | NOT DECIDED |
| C-7R.13.3 — Override observation remains open | Fails closed by | 1 | NOT DECIDED |
| C-7R.13.3 — Override observation remains open | Fed by | 1 | NOT DECIDED |
| C-7R.13.3 — Override observation remains open | Gated by | 1 | NOT DECIDED |
| C-7R.13.3 — Override observation remains open | Changes | 1 | NOT DECIDED |
| C-7R.13.4 — Explicit dismissal and qualified resurfacing | Fails closed by | 1 | NOT DECIDED |
| C-7R.13.4 — Explicit dismissal and qualified resurfacing | Fed by | 1 | NOT DECIDED |
| C-7R.13.4 — Explicit dismissal and qualified resurfacing | Gated by | 1 | NOT DECIDED |
| C-7R.13.4 — Explicit dismissal and qualified resurfacing | Changes | 1 | NOT DECIDED |
| C-7R.14 — Unrecognized purpose-type halt | Gated by | 1 | NOT DECIDED |
| C-7R.14 — Unrecognized purpose-type halt | Changes | 1 | NOT DECIDED |
| C-7R.14.1 — Unknown-purpose immediate stop | Fed by | 1 | NOT DECIDED |
| C-7R.14.1 — Unknown-purpose immediate stop | Gated by | 1 | NOT DECIDED |
| C-7R.14.1 — Unknown-purpose immediate stop | Changes | 1 | NOT DECIDED |
| C-7R.14.2 — Unknown-purpose exact diagnosis | Fails closed by | 1 | NOT DECIDED |
| C-7R.14.2 — Unknown-purpose exact diagnosis | Fed by | 1 | NOT DECIDED |
| C-7R.14.2 — Unknown-purpose exact diagnosis | Gated by | 1 | NOT DECIDED |
| C-7R.14.2 — Unknown-purpose exact diagnosis | Changes | 1 | NOT DECIDED |
| C-7R.14.3 — Unknown-purpose original-request preservation | Fails closed by | 1 | NOT DECIDED |
| C-7R.14.3 — Unknown-purpose original-request preservation | Fed by | 1 | NOT DECIDED |
| C-7R.14.3 — Unknown-purpose original-request preservation | Gated by | 1 | NOT DECIDED |
| C-7R.14.3 — Unknown-purpose original-request preservation | Changes | 1 | NOT DECIDED |
| C-7R.14.4 — Unknown-purpose plain explanation | Fails closed by | 1 | NOT DECIDED |
| C-7R.14.4 — Unknown-purpose plain explanation | Fed by | 1 | NOT DECIDED |
| C-7R.14.4 — Unknown-purpose plain explanation | Gated by | 1 | NOT DECIDED |
| C-7R.14.4 — Unknown-purpose plain explanation | Changes | 1 | NOT DECIDED |
| C-7R.14.5 — Explicitly confirmed existing-purpose mapping | Fed by | 1 | NOT DECIDED |
| C-7R.14.5 — Explicitly confirmed existing-purpose mapping | Changes | 1 | NOT DECIDED |
| C-7R.14.6 — New-purpose proposal path | Fails closed by | 1 | NOT DECIDED |
| C-7R.14.6 — New-purpose proposal path | Fed by | 1 | NOT DECIDED |
| C-7R.14.6 — New-purpose proposal path | Changes | 1 | NOT DECIDED |
| C-7R.14.7 — Unknown-purpose halt event | Fails closed by | 1 | NOT DECIDED |
| C-7R.14.7 — Unknown-purpose halt event | Gated by | 1 | NOT DECIDED |
| C-7R.14.7 — Unknown-purpose halt event | Changes | 1 | NOT DECIDED |
| C-7R.14.7.1 — Halt-event unknown type | Fails closed by | 1 | NOT DECIDED |
| C-7R.14.7.1 — Halt-event unknown type | Fed by | 1 | NOT DECIDED |
| C-7R.14.7.1 — Halt-event unknown type | Gated by | 1 | NOT DECIDED |
| C-7R.14.7.1 — Halt-event unknown type | Changes | 1 | NOT DECIDED |
| C-7R.14.7.2 — Halt-event preserved request | Fails closed by | 1 | NOT DECIDED |
| C-7R.14.7.2 — Halt-event preserved request | Fed by | 1 | NOT DECIDED |
| C-7R.14.7.2 — Halt-event preserved request | Gated by | 1 | NOT DECIDED |
| C-7R.14.7.2 — Halt-event preserved request | Changes | 1 | NOT DECIDED |
| C-7R.14.7.3 — Halt-event timestamp | Fails closed by | 1 | NOT DECIDED |
| C-7R.14.7.3 — Halt-event timestamp | Fed by | 1 | NOT DECIDED |
| C-7R.14.7.3 — Halt-event timestamp | Gated by | 1 | NOT DECIDED |
| C-7R.14.7.3 — Halt-event timestamp | Changes | 1 | NOT DECIDED |
| C-7R.15 — Mandatory per-task relevance declaration policy | Changes | 1 | NOT DECIDED |
| C-7R.15.1 — Declaration Component name / id | Fails closed by | 1 | NOT DECIDED |
| C-7R.15.1 — Declaration Component name / id | Fed by | 1 | NOT DECIDED |
| C-7R.15.1 — Declaration Component name / id | Gated by | 1 | NOT DECIDED |
| C-7R.15.1 — Declaration Component name / id | Changes | 1 | NOT DECIDED |
| C-7R.15.2 — Declaration Task or purpose | Fails closed by | 1 | NOT DECIDED |
| C-7R.15.2 — Declaration Task or purpose | Changes | 1 | NOT DECIDED |
| C-7R.15.3 — Declaration Selected relevance mode | Fails closed by | 1 | NOT DECIDED |
| C-7R.15.3 — Declaration Selected relevance mode | Gated by | 1 | NOT DECIDED |
| C-7R.15.3 — Declaration Selected relevance mode | Changes | 1 | NOT DECIDED |
| C-7R.15.4 — Declaration Reason for that mode | Fed by | 1 | NOT DECIDED |
| C-7R.15.4 — Declaration Reason for that mode | Gated by | 1 | NOT DECIDED |
| C-7R.15.4 — Declaration Reason for that mode | Changes | 1 | NOT DECIDED |
| C-7R.15.5 — Declaration Uncertainty behavior | Fails closed by | 1 | NOT DECIDED |
| C-7R.15.5 — Declaration Uncertainty behavior | Gated by | 1 | NOT DECIDED |
| C-7R.15.5 — Declaration Uncertainty behavior | Changes | 1 | NOT DECIDED |
| C-7R.15.6 — Declaration Allowed retrieval/use boundary | Fails closed by | 1 | NOT DECIDED |
| C-7R.15.6 — Declaration Allowed retrieval/use boundary | Fed by | 1 | NOT DECIDED |
| C-7R.15.6 — Declaration Allowed retrieval/use boundary | Changes | 1 | NOT DECIDED |
| C-7R.15.7 — Declaration Logging / audit requirement | Fails closed by | 1 | NOT DECIDED |
| C-7R.15.7 — Declaration Logging / audit requirement | Changes | 1 | NOT DECIDED |
| C-7R.15.8 — Declaration Fail-closed behavior when relevance cannot be safely determined | Changes | 1 | NOT DECIDED |
| C-7R.15.8.1 — Retrieval-system failure boundary | Gated by | 1 | NOT DECIDED |
| C-7R.15.8.1 — Retrieval-system failure boundary | Changes | 1 | NOT DECIDED |
| C-7R.15.8.2 — Genuine-empty context boundary | Fails closed by | 1 | NOT DECIDED |
| C-7R.15.8.2 — Genuine-empty context boundary | Gated by | 1 | NOT DECIDED |
| C-7R.15.8.2 — Genuine-empty context boundary | Changes | 1 | NOT DECIDED |
| C-7R.16 — Accepted five-consumer relevance declarations | Changes | 1 | NOT DECIDED |
| C-7R.16.1 — Retrieval declaration interface | Fails closed by | 1 | NOT DECIDED |
| C-7R.16.1 — Retrieval declaration interface | Changes | 1 | NOT DECIDED |
| C-7R.16.2 — Computed View declaration interface | Fails closed by | 1 | NOT DECIDED |
| C-7R.16.2 — Computed View declaration interface | Gated by | 1 | NOT DECIDED |
| C-7R.16.2 — Computed View declaration interface | Changes | 1 | NOT DECIDED |
| C-7R.16.3 — Action Surfacing declaration interface | Fails closed by | 1 | NOT DECIDED |
| C-7R.16.3 — Action Surfacing declaration interface | Gated by | 1 | NOT DECIDED |
| C-7R.16.3 — Action Surfacing declaration interface | Changes | 1 | NOT DECIDED |
| C-7R.16.4 — Condition-based reread declaration interface | Fails closed by | 1 | NOT DECIDED |
| C-7R.16.4 — Condition-based reread declaration interface | Gated by | 1 | NOT DECIDED |
| C-7R.16.4 — Condition-based reread declaration interface | Changes | 1 | NOT DECIDED |
| C-7R.16.5 — State-review declaration interface | Fails closed by | 1 | NOT DECIDED |
| C-7R.16.5 — State-review declaration interface | Changes | 1 | NOT DECIDED |
| C-7R.16.6 — Shared uncertainty-rule consumer interface | Fails closed by | 1 | NOT DECIDED |
| C-7R.16.6 — Shared uncertainty-rule consumer interface | Gated by | 1 | NOT DECIDED |
| C-7R.16.6 — Shared uncertainty-rule consumer interface | Changes | 1 | NOT DECIDED |
| C-7R.16.7 — Future mouth-dimension declaration boundary | Gated by | 1 | NOT DECIDED |
| C-7R.16.7 — Future mouth-dimension declaration boundary | Changes | 1 | NOT DECIDED |
| C-7R.16.8 — Quiet automatic relevance use and material disclosure | Gated by | 1 | NOT DECIDED |
| C-7R.16.8 — Quiet automatic relevance use and material disclosure | Changes | 1 | NOT DECIDED |

## Plain-gate and empty-box review

All nine fields and each USED BY row were checked against the source-first outline. Actual evaluation, configuration validation, change authorization and uncertain-result handling name their real owners. Pure fields, vocabulary values, predicates and prohibitions may have empty TOGETHER boxes; their parents consume them explicitly. Presence of a field is not invented as a gate. The fully plain gate is the explicit human confirmation of an existing-purpose mapping; reusable mode change also states its human confirmation beside the real invalid-configuration owner. No card is stamped BUILT. Shared currentness, acceptance, channel provenance, retry and uncertainty atoms keep their previous identities. Every use row names one using place, and all incoming places are represented. Proposed identifiers are qualified even where an immutable earlier canonical card name omitted the qualifier.

| Card | Plain gate justification |
|---|---|
| C-7R.14.5 — Explicitly confirmed existing-purpose mapping | V10 explicitly requires Ness’s confirmation of the specific mapping before evaluation. This human act is not a separately named system mechanism. |

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


### Source placements carried from CH06-g

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

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH07-a

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §7N; MAP C-7N; DD §3G; Companion §7N | Gentle question, single invitation, decline/ignore/no-response closure and personal reopening; conflicting Map new-trigger summary retained | C-7N/.1/.1.1–.1.3; header conflict |
| V10 §7N | Permission-controlled hybrid; explicit request always permitted; authorized proactive rule; settings may disable entirely | C-7N.2/.2.1–.2.3 |
| V10 §7N; B4 §10 | All three required forms and all three prohibited instruction forms, as exact source examples | C-7N.3/.3.1/.3.2 and six bottom-level form cards |
| V10 §7N; B4 §9.2; formal B2 §8 | Five possibility fields, support references, per-item labels, current-label provenance, stable record identity; separate later action; new-record L2 versus pure-read/display L1 | C-7N.4 and nine field cards; shared stage contract |
| V10 §7N; B4 §9.2 | All six states and exact consequences: separate accepted action, rejection event, modified basis, optional postponement reason, ignored exception, new alternatives pass | C-7N.5/.5.1–.5.6 |
| V10 §7N; B4 §9.1; formal B2 §8 | Weak/conflicted/stale/insufficient support, impact-based stronger review, protective/active lanes and current-support asymmetry | C-7N.6/.6.1/.6.2; prior A31 reused |
| B4 §9.2 | Five separate common stage/level fields, exact three stage values, current physical operation versus prospective level/categories and advancement requirements | C-7N.7, five field cards and three stage-value cards; later CH07-b/c consume them |
| B4 §10 | Four required display facts, approval/attempt/effect/result distinctions and all thirteen illustrative canonical forms | C-7N.8/.8.1 four facts/.8.2 distinctions/.8.3–.8.15 forms |
| B4 §§11/12 | Downstream source/picture/surfacing/normal-return wiring; privacy before SACL, governors never evidence, evidence families and less-claiming grounding | C-7N.9/.10; established C-7D/C-7M/C-7G.8/C-24.14 boundaries reused |
| B4 §13 | Stable identity and source-version key, record-level atomic commit, startup unfinished work, missing-record reconciliation, partials, technical-only B9, stage integrity and uncertain-effect freeze | C-7N.11/.11.1–.11.7; prior operation and external-effect atoms reused |
| B4 §14 | One connected operation log, content and level separation, five active protections, owned versioned rules, both cooling conditions, valid reactivation, failed-evaluation preservation and three separate record kinds | C-7N.12/.12.1–.12.3, five protection atoms, two cooling conditions; shared fourteen-field lifecycle event retained |
| Formal B2 §§4/5.1; §8 items 1–4 | Quiet automatic evaluation, proposed identity/version, tier ownership, controlled purpose, target and all candidate families | C-7N.13/.13.1–.13.4 with identity/version and target/pool atoms |
| Formal B2 §8 item 5 | Only object_type_matches is categorical; three other gates not selected; present-context label consumed from live or current positional provenance, never thread/time inferred | C-7N.13.5/.13.5.1; existing object-type and item-provenance atoms |
| Formal B2 §8 items 6–9 | Nine dimensions with embedding versus deterministic producers, state/reading-only applicability, response/clash handling, no mouth, on-demand timing/settings, no pre-computation and reason | C-7N.13.6 with nine atoms; .13.7/.13.8/.13.9 |
| Formal B2 §§5.3/5.7; §8 item 10 | Both support lanes, label ordering, weak-support fallback, empty/failure difference, clean main answer and support-kind side-drawer warning; proposed T2-UNRES-SHARED | C-7N.13.10/.13.10.1–.13.10.4; existing shared uncertainty/empty/failure atoms |
| Formal B2 §§5.5/5.6; §8 items 11–13; A4 §§2–6 | Authorized-use boundary, one Decision-12 event, Decision-11 disagreements, all support labels/provenance, questions asked/dropped and response exception; four failure classes; eight-field validity | C-7N.13.11/.13.12/.13.13 and four failure atoms; prior validity/log owners |
| B4 acceptance record §7; B2 closure; four active indices | Accepted scope, corrected current-stage level wording, proposed mechanical carriage and remaining open implementation/calibration slots | READ RECORD and source dispositions; no audit workflow imported |
| Recovery ledger scoped FR rows; Bundle 3 B-AFFIRM boundary | Restoration-only navigation and distinction between reading affirmation and possibility disposition | Appendix B carry; later CH08-f ownership, no historical behavior imported |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH07-b

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §7O; MAP C-7O; DD §3G; Companion §7O | Two result types, normal report intake/label, detected possible link and no direct system access to reality | C-7O/.1/.1.1/.1.2 and report entry/label atoms |
| V10 §7O; B4 §9.2 | All seven proposal fields and stable action identity, without final new field serialization | C-7O.2/.2.1–.2.7 |
| V10 §7O; B4 §9.2 | Confirm, reject, modify, unresolved indefinitely; separate connection-response event; no loss from three-name B8 summary | C-7O.3/.3.1–.3.4; .9.1 |
| V10 §7O | Timing/similarity prohibitions and connection-confirmation versus causal-explanation distinction | C-7O.4/.4.1–.4.3 |
| V10 §7O; B4 §9.2 | Separate action/root/connection and event/relationship/meaning; result root referenced not copied; existing five stage fields reused | C-7O.5/.5.1–.5.6; .9.3; existing C-7N.7 |
| V10 §7O; MAP C-7O/CY-E | Conditional reread/state/open-loop/other explicitly designed use; detection may be disabled/restricted | C-7O.6/.6.1–.6.4 and .7 |
| V10 §7O | Success confirmed only by Ness versus revisable apparent consistency, separate facts and no causal proof | C-7O.8.1/.8.1.1/.8.1.2 |
| V10 §7O | Partial success confirmed versus interpreted; achieved/unmet portions separate; no automatic retry | C-7O.8.2 with four children |
| V10 §7O | Failure confirmed versus interpreted; no automatic retry/resuggestion; Ness decides next | C-7O.8.3 and two branches |
| V10 §7O | Cancellation trigger, reason, action state, actual partial effects and intended effects; authorized stop types | C-7O.8.4 and five field children |
| V10 §7O | No/unknown result, exact result-unknown marker, active uncertain state/open loop, no time-only result | C-7O.8.5 and three children |
| V10 §7O; B4 §9.2 | Wrong/contested/contradicted linkage, rejected event, corrected proposal and unchanged action/root | C-7O.8.6 and two children |
| B4 §9.2; §§10/13 | Separate B8 response and assessment records; current/prospective stage carriage; before-effect non-execution versus after-possible-effect unknown/frozen/no-retry; exact preview/authority retained | C-7O.9/.10 and both crash cases; C-7N.7/.8 and existing operation atoms; full execution owner CH07-c |
| B4 §§11/12/14 | Normal source-return path; privacy/gates never evidence; A31 and evidence family; one real-operation log, domain/log levels, B8 active/cold and fourteen-field lifecycle event | C-7O.11/.12 with canonical shared owners |
| B6 mechanical §§12/13; closeout §8 Path 4 | Outcome observations only through §7E to roots/readings; no OOP live query target; absence is not confirmation; no reconstructed capture gap | C-7O.9.4 consumer boundary; full capture/schema owners CH08 |
| B-INT-8 §12C | Fresh current-use resolution for any accepted connection, append-only correction history, no new result authority | C-7O.5.3 conditional owner gate, existing C-24.14 |
| Durable kernel §§U/V.2/W/X; framework addition §§9–11 | Reference-only coordination, component identities/terminals unchanged, no completed B-CYCLE or chosen result | C-7O.13; general kernel mechanics remain outside current scope |
| B4 receipt; active indices; recovery ledger; B15/formal B2/future-search discovery | Accepted scope and remaining open slots; navigation/restoration-only or later-owner dispositions | READ RECORD and scoped dispositions, with no historical behavior imported |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH07-c

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 complete §7P; Companion §7P; Map C-7P; Defaults §3G | Helper/actor boundary and all nine must-never rules | C-7P root |
| V10 §7P; B4 §9.2 | Three states with distinct authority; canonical stage values reused | C-7P.1 and .1.1–.1.3; C-7N.7.1 |
| V10 §7P; B4 §9.1 | Four levels, actual present effect, separate future level and separate Level-2 log | C-7P.2/.2.1–.2.5; C-7N.7 and .12.2 |
| B4 §9.1 | Strictest rule and specialist maintenance/privacy/promotion/TSC/identity owners; permission is not evidence | C-7P.2.6/.2.7 and existing owner cards |
| V10 §7P | Standing ability and exact moment approval; silence/previous permission/preparation never consent | C-7P.3/.3.1/.3.2 |
| V10 §7P; B4 §§9.1/9.2 | Narrow recurring object, all eight explicit scope fields plus audit/notification and pause/revocation state | C-7P.4 and ten children |
| V10 §7P; B4 §9.1 | Seven heightened categories, specific per-instance confirmation, not Level 5 or universal irreversibility | C-7P.5 and seven category children |
| V10 §7P; B4 §§9.1/9.2 | Changed/ambiguous/expired/unexpected stop conditions at every layer/level; access reduction | C-7P.6 and five stop cases |
| V10 §7P | Five immediate stop-and-surface steps; full seven event groups; known/unknown/still-changing subfields | C-7P.7, .7.1–.7.5 and full .7.3 field tree |
| V10 §7P | Correction is a new action; all real-world correction examples require approval; no assumed restoration or technical-success resolution | C-7P.8/.8.1/.8.2 |
| V10 §7P; B4 §9.2 | Five linked separate objects and additional explicit corrective-execution stage | C-7P.9/.9.1–.9.3; C-7P.7.3; existing C-7O.5.1; .11.5 |
| V10 §7P | Five simultaneous emergency predicates and every prohibited completed-world reversal example | C-7P.10 and five condition cards |
| B4 §9.2 | Prepared record’s six object fields and all shared stage/level metadata | C-7P.11.1 and six fields; C-7N.7; C-7O.2.1 |
| B4 §9.2 | Exact approval binding: prepared identity, content/version, endpoint, tool, level, categories, conditions/expiry/scope, basis/time | C-7P.11.2 and nine field cards |
| B4 §9.2 | Dated attempt under one Action ID, bound authorization and exact preview; attempt is not effect | C-7P.11.3/.11.3.1; existing Action ID and preview/authorization owners |
| B4 §9.2 | Actual authorized outside effect only, post-record of change/time/channel/authority/preview; corrective execution distinct | C-7P.11.4 and three field cards; .11.5; shared stage/identity/preview/authority |
| B4 §9.2; V10 §7P | Dated emergency record: conditions met, what stopped, what not reversed and date | C-7P.11.6 and four children |
| B4 §9.2 | Stable chain identity, no double execution, live authority, exact preview and all six invalidating changes | C-7P.12.1–.12.4 |
| B4 §§9.2/13; V10 §7O | Mandatory post-record, honest partial changed/unchanged effects, frozen unknown/no retry, cancellation, both crash positions | C-7P.12.5–.12.8; existing C-7O.10.1.1/.10.1.2 and .8.4 |
| B4 §13 | Operation ID/key, atomic record commit, no duplicate outcome, startup recovery, missing-record reconciliation, partial/technical retry/stage integrity | C-7P.13.1; shared C-7M.5.2, C-7N.11.1–.11.7 and C-7H.9/.10 |
| B4 §14; restored Group 10 operational-record laws | One operation/log, complete content/use/non-use, domain/log levels, honest stage, evidence family and three record kinds | C-7P.13.2; existing C-7B.10.2/.10.3 and Bundle 4 owners |
| B4 §14 | Initial active, five protections, owned cooling rule, two cooling conditions, actual-use/link reactivation, failure preserves prior status, fourteen-field event | C-7P.13.3 with existing C-7N.12.3/.12.3.2 and C-7M.11.4/.11.5 |
| B4 §§11/12/14 | Purpose-specific privacy, §7Q then SACL, protected/TSC/compartment/influence restrictions, no circular/double support | C-7P.13.4 with canonical A31/evidence-family and privacy owners |
| B6 mechanical complete §12 | Protected minimum-metadata §7P query obtains authority decision, no recursion/no early payload release | C-7P.14.1; full query mechanics CH08-c |
| B-INT-8 §5C/§7C/I5 | Existing exact narrow rule and authority provenance; CCR cannot create/widen rule | C-7P.14.2; existing C-24.4.3/.9.3 |
| AIC §15; kernel §§U/V.2/W | Recorded-state and reference-only coordination never own action authority | C-7P.14.3; existing C-7O.13 |
| A19 room-start §6; A22 §5 | Narrow room-start confirmation scope; full five-condition phone emergency boundary | C-7P.14.4/.14.5; full room and phone owners later |
| Accepted package/active candidate/decision discovery | Owner-preserving boundaries, navigation, restoration tracking and deliberately deferred detailed scopes | Scope dispositions and READ RECORD; no historical behavior imported |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH08-a

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
| A7 full primary and full closure receipt | .7 natural-language pause/reopening, one-short-question ambiguity rule, actual-words scope, independent visible/internal controls and truthful transformation. .5 preserves compatible interpretation labels, full/detailed simulation scope and prior approval, normal longitudinal use without a new volume threshold; .6 preserves private/default and explanation-without-disclosure. No mandatory command language or implementation policy invented. | C-7Q source-ordered tree and the scope dispositions above |
| B7 full primary and full closure receipt; Bundle 5 §§3/4/5/8 scoped | .8 all thirteen proposed mechanisms: PIP, PDE, PEB, SPS, XDS, MCS, VRE, DDE, VER, BVH, IRR, PGC, PIS, plus their common enforcement-contract layer. Names remain proposed on every mention. PIP normalization vocabulary and six steps; PDE ordering/inputs; PEB minimum output; SPS identity/protection/inert credentials; detector registry and method versions; mixed capture; discovery adapters and coverage; independent verification; backup modes/restore replay; complete influence lifecycle; stricter-only person/group configuration and inspection. | C-7Q source-ordered tree and the scope dispositions above |
| B7 §14 complete | .9 common record identity/schema/operation/time/protection/append-history discipline and all twenty-six schemas, with fields recursed. The already introduced .4.4 exclusion event and .6.9 privacy-decision record retain their first identities; §14's corresponding rows extend those records rather than duplicate them. History at .3.7 is reused by deletion_case. Record-specific identities remain distinct; references do not copy private content. | C-7Q source-ordered tree and the scope dispositions above |
| B7 §15 complete, including bold §§15.0–15.9 | .10 shared atomic/idempotent/restart/logging/B9 spine, then nine contracts in source order: topic pause, exclusion, sealed isolation, hiding, restriction, redaction, deletion, influence removal and restoration/supersession. Preserve request/result, operation identity, key, scope, every state/transition, terminal versus protective status, checkpoint, partial recovery, retryable/terminal failure, derivative handling, verification and restoration. Six sealed-transfer steps preserve raw content before removing ordinary exposure. All thirteen hiding surfaces and ten restriction elements are explicit. | C-7Q source-ordered tree and the scope dispositions above |
| B7 §16; A26 complete §§2–4; B-INT-5 complete §§3/4/12A/12B/13 | .11 owner-preserving interfaces: all front doors; retrieval/relevance; engine/derived stores; simulations; output; TSC; backup; independently established private-mode/access facts. A26 defaults are consumed only inside the established private context. Full factor verification, mode-session/fence schemas and identity/access mechanics remain CH09-i, CH09-c/d/e. | C-7Q source-ordered tree and the scope dispositions above |
| B-INT-6 complete §§3/4/5/6B/6D/6E/7A/7B/8/13/14/15/16 | .11 exact privacy-owned payload binding, transformation loop, immediate revalidation/restriction, two stream alternatives and no-signal output. Full proposed ODC identity, claim/dispatch/attempt/receipt records, state/recovery machinery and output-channel contract remain CH09-d; CH11 assembles the whole path. Privacy never owns SACL or delivery reality. | C-7Q source-ordered tree and the scope dispositions above |
| A2 complete §5A.2/§9; prior canonical C-READ.10.11 | .11 governance discovery must find manifests, partial/blocked/integrity-failed cards, checkpoints and indexes independently of semantic eligibility. Reuse C-READ.10.11; do not make discovery semantic evidence. Protection inheritance and side-channel limits apply. | C-7Q source-ordered tree and the scope dispositions above |
| A4 complete §4; retained formal Bundle 2 and B1 scope; B6 mechanical complete §12 | .11 privacy precedes relevance, router does not re-evaluate privacy, protected minimum-metadata authorization query obtains its own decision without recursion. Full LMAC contracts are CH08-c; relevance CH08-b. | C-7Q source-ordered tree and the scope dispositions above |
| B15 complete §4; retained B-INT-4/TSC source readings; B-INT-8 whole reading retained | TSC only stores safe structural references after exclusion; no inspection/authorization token opens L1 content. Connection current-use authorization stays distinct from original acceptance, with no repeated endorsement or authority creation. Existing C-TSC/C-24 owners are reused. Full identity/token wiring remains CH09 and CH11. | C-7Q source-ordered tree and the scope dispositions above |
| B9, B10, B-HOLD, B11, B16, B24 and evaluation-evidence bridge; prior complete owner readings | Existing operation/retry/hold/promotion/model-boundary owners remain canonical. A privacy refusal is not retryable around the gate; a genuinely changed recorded authorization permits a new admission. No model validation, stored status, log or durable coordination record grants access. | C-7Q source-ordered tree and the scope dispositions above |
| AIC complete §15; durable kernel retained owner/fence sections | .11 recorded permission is descriptive; gate ownership and owner-prescribed fences remain external to coordination. No invented control-plane/kernel part identity; their full packages remain later placement. | C-7Q source-ordered tree and the scope dispositions above |
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
| A17, A19 room/chat/world, A22, framework additions, future-feature/dual-model/candor source topic matches | Preserve already established privacy ownership; rooms, tools, outward transfer, private surfaces and provider changes cannot grant authorization. Detailed interface/world/model/phone/future-tool bodies remain their named CH09/CH10/CH11 owners. Inactive sources remain named intents only. No historical narrative imported. | C-7Q source-ordered tree and the scope dispositions above |
| Sept25 buckets record §4 Group 11 and §6 FR-0108; authorized historical preservation file F9, read whole | .12 explicit influence-removal instruction requires scope, affected components and start time. DECIDED-2026-09-25; only this restored passage supplies behavior from the historical file. Its full pinned blob was verified before reading. No other archive catalogue content imported. | C-7Q source-ordered tree and the scope dispositions above |
| Four active indices NHD-M7Q/NHD-A7/NHD-B7/NHD-BU5 rows; recovery ledger title/status tracking | Navigation and Appendix B only. The ledger supplies no behavior. Earlier versions of packages remain superseded where accepted highest versions exist. | C-7Q source-ordered tree and the scope dispositions above |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.

## READ RECORD

Pinned source commit remains 6a7160ba688ba4e433a31899162815df7e2bab17. Contract §§5–11 were reopened before this piece and §11.3 again after writing. Full lessons/run/route readings are retained; lessons §10.1 and run §§10/11 were reopened during final review. Five complete files receive whole-file credit below. Other entries are scoped current or retained prior reads and receive no new whole-file credit. Original and prior Writing 2 fingerprints remain preserved.

| Source file | Reading scope / whole-file credit | SHA-256 |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: complete §7R, all fourteen decisions and open list; complete purpose-specific external prerequisite reopened again during final review. | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Scoped: complete §7R; the initially truncated middle was reopened in full. Older unqualified privacy prerequisite is retained as a source conflict. | `cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb` |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Scoped: complete §3H; source-declared mouth/provider openness retained through the formal Bundle 2 body. | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped: complete C-7R card plus A4/B-INT-1 relevance entries; canonical name and root DESIGNED standing retained. | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md` | Whole: complete 391-line accepted policy, read before drafting and §3/§4 reopened during final review. | `c754b27e44cdb578e1cc25e7de681c9d2afd68fedc6e974cc45c8aa6c83d553f` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md` | Whole: complete 152-line receipt; acceptance chain and scope retained. | `f9d3fe049d2a77b19039f498b1f611159355a3bb60acbf083b72fe3368044e62` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Whole: complete 1156-line formal declarations file, read in sequential nontruncated ranges before drafting; §§4/5 reopened during final review. | `b2a5b3fbea75f7123a16c8a45c0fb096f4c4565585a4a0c7b7709e70f27d000e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Whole: complete 149-line foundation acceptance receipt; the excluded foundation body was not opened. | `0b2f0ecfd121423ed2c3dfe833d9ca922f3b366e64353f94bcaf59aa109e6db6` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: complete 357-line closure receipt; formal-package acceptance and the receipt’s own conditional audit gate both retained. | `faa88d9c991b2e4058081717a4fcbeb5a8e27d62e0f484ae6051fc061a03bac1` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md` | Scoped: complete §5, §4 ceiling boundary and §6 B26 separation; earlier canonical retrieval audit reading retained. No empirical values chosen. | `da0aa4d22d6bc6554196c15b2c81b5541018a1e01bfbce367d7cf8e623b6a753` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` | Prior complete state/view/action scopes retained from CH06/07; currentness vocabulary, review and no-relevance-as-evidence boundaries checked through existing owners. | `0c9a201130d5811c838fea0d5655c8a98aac909afdc60024830204a690e77f97` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped: complete §12 relevance/live-query contract reopened; §3 creation and §8 earlier-context references retained for incoming uses. | `bc1095955525fcea56cb4d16057c93bfb15eec42a83a1b644baf0e87a473f64e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md` | Prior whole reading retained from CH06-g; §13A/§18 current-purpose owner references retained for existing connection uses. | `6a3b7cf71546ed237507b34b1a24a759d34ca683216b255c91ac4add679b1bfd` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md` | Scoped: §6 ordinary-use relevance and §9 unresolved thresholds/ranking; no new wonder admission or origin rule. | `1a4d8b9a24f15ce371dd49b28bde7bf9888e0fe114ec4bdab6e6446af495bf8d` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md` | Prior scoped §6 hold-use restriction retained; held material is excluded from new surfacing through its existing owner. | `406ab00f640eaae013902782e9ec6ca652ea680c10b0f68699d56391a9e1efce` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md` | Prior complete reread-identity/recovery scope retained; §5 authorization-before-relevance used by the earlier incoming reread card. | `215b74841321656a8b7fb1cbf4b9ac9b43259315864cd9f85f5ce86b43d10001` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md` | Prior whole reading retained from CH08-a; §16 authorized-candidate query boundary reused without a second privacy mechanism. | `7fda28e994336a7ea0d17e217025cb71c116ec42ce3ecde3d8c9110783b52aad` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md` | Scoped: identity/semantic owner references and complete §9 preserved boundary list; telling relevance does not imply truth, permission or clash resolution. | `f91da6426817031cf2c0b14fb467a3e1d97d2ea3c67d27a07d8b1831f9895a55` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | Scoped discovery: §2 semantic-authority prohibition and manifest no-relevance-content boundary; no additional relevance behavior imported. | `baca06e562027a080dab4384943bfb87947c6f598b36776f1016fa8472384a87` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` | Prior complete §15 owner-preserving scope retained; recorded state is descriptive and cannot replace relevance or privacy authority. | `b39654a60744982d0e2f16c2bc3cd7a33f6ae47ff55b63b5b1dfffada719d709` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` | Prior complete owner/fence §§U/V/W/X and P4/AF-4 scope retained; references do not replace live owner decisions or complete a cycle. | `1f9ea714f1a182c0857e80399850a3aeebcf4a50a32d5a200fce57a5d5f47ae3` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` | Scoped: complete preserved-architecture and kernel must-never sections; relevance owner cannot be bypassed or replaced by the framework. | `1386091a0977ac79588f22a9f85213579203637e493dbb2d75be3d893326aa28` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md` | Scoped: live-sequence and meaning-preservation sections; speaking roles do not choose a relevance validator. Formal Bundle 2 §5.4 explicitly preserves that boundary. | `024a81aeb2c7104e99ceaa3b881a024e38cf700169e37179ac0fb1f358b0d46e` |
| `05_ACTIVE_CANDIDATE/Thought_Branches_and_Simulation_Intent.md` | Scoped: opening intent and branch-navigation distinction; no accepted relevance mode is inferred. | `91c4bc2ec40812491dcfc45a397c5a0812b45858c11d2ced7f604dfd8a2f2f92` |
| `05_INACTIVE_CANDIDATE/NH_PROVENANCE_FIRST_MULTI_INDEX_MEMORY_FABRIC_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped discovery: relevance owner, channel, purpose and declaration references only; inactive INTENT slot, no mechanics imported. | `84eee68e6a5dfd00d675797640937e960d99ff721ae255563ac7241b2c78780d` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Scoped discovery: relevance references and existing operational-law restoration; no new historical passage opened or imported. | `9f6f9cac1e07ab14f0c6f3ed834b8260265dac6f6a430fa12be5c6e4c3f0b59f` |
| `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md` | Scoped title/status discovery for relevance and routing; no behavior imported and no whole-file credit. Broad truncated output is not claimed as a full read. | `fc014bbab36c87495d534ade8bb78f8de4197efa9408f5abb908743601a21522` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | Scoped: full NHD-M7R/NHD-A4/NHD-BU2 rows; navigation only, behavior read from governing bodies. | `457c6f43562a92cd82076640af44a58ea412335284c0e61da3c38f3ba63f24b9` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | Scoped: full NHD-M7R/NHD-A4/NHD-BU2 rows; navigation only, behavior read from governing bodies. | `3f1b95da77f620597e9ba862568f4247d1eb4d50f73c620888637dfcde03e3c9` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Scoped: full NHD-M7R/NHD-A4/NHD-BU2 rows; navigation only, behavior read from governing bodies. | `aafc7abe6522f4c7ece23f40560e648866188e1b5401ed6cd298809d15ed0f7b` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Scoped: full NHD-M7R/NHD-A4/NHD-BU2 rows; navigation only, behavior read from governing bodies. | `aad8d1aeee9a331ad6f4d9ddbcfa9c42eae2a94e1ef1bccde7484079181ff7b4` |

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
| CH06-g | `4a8168002eac965e248d35fc761feb51232a813b0406e2df9e0851f6b42bf676` |
| CH07-a | `9ac2415acd8c58390c651a2ad4ec2ba38b16509bffae3816e68b3d5a69cfd2cd` |
| CH07-b | `7f36823b65c8523b456d93e827b0456d97dc429c9bb3ee35ff9d9fb8f778761a` |
| CH07-c | `563b84b894c3bc5022f087a356fb412a3a99eaa8a629f7cc5e26965f409055e8` |
| CH08-a | `08d9a00db55c7b18091e1942e792c8e21886525c1cf0db3dc07112dcab58838f` |

### READ-folder files not yet read whole

60 inherited pending files remain. Scoped reading receives no new whole-file credit.

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
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
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
§1.3 no history/actions/roles/workflow in this chapter: PASS — 218 behavior cards reviewed; 0 workflow/advice hits. Delivery metadata remains outside behavior.
§1.4 every gap written as NOT DECIDED: PASS — 698 empty fields match 698 register rows; 8 additional mechanical slots are explicit.
§1.5 conflicts marked, none resolved: PASS — the Companion’s unqualified privacy/deletion prerequisite is marked in the header and C-7R gate; V10’s purpose-specific authorization governs. Earlier conflicts remain carried and none is silently reconciled.
§3 exactly one stamp per line: PASS — 218 headers, 1265 populated fields and 342 USED BY rows checked. 0 BUILT field lines name only existing built reading/store sources; no new machinery is stamped BUILT.
§4 every behavior line cited in the exact format: PASS — 72 distinct citations; 72 resolve within the named pinned sections. Populated fields and use rows are cited; the source-to-claim review accompanies mechanical resolution.
§5.4 one name per thing: PASS — 218 unique current IDs without prior collisions; 1368 named-card mentions checked. Shared atoms retain their established IDs and names.
§6 all template fields present, in order, for every part: PASS — 218 templates and 1963 field lines checked.
§6.3 reciprocity within this chapter: PASS — 287 internal relationship occurrences checked; 42 outgoing and 37 incoming continuation rows name both ends. No missing reciprocal; prior files remain unchanged.
§6.4 every decided detail written in, no citation used in place of content: PASS — 20 source-to-card rows reviewed; 46 expected source-name literals present. Existing atomic owners and remaining scopes are explicit.
§6.5 sub-parts recursed to the bottom: PASS — all fourteen decisions, ten Tier-1 groups, eight policy fields, four gates, nine dimensions, entry fields and link types, six validation checks and failure classes, three outcomes, seven precomputation groups, six invalidators, five preview groups, nine disagreement groups, thirteen event groups and five counts, three pattern predicates, two explicit purpose-resolution paths and three halt-event fields are present. Existing canonical atoms are reused without new owners. 128 current cards have all three TOGETHER fields empty.
§9 coverage matrix rows added for every file used: PASS — all 145 pinned READ-folder file paths remain in the carried inventory; current additions and 31 current READ RECORD fingerprints are present. Shared-package coverage remains partial where stated.
§10.11 no recommendation, no sentence addressed to Ness: PASS — all 218 behavior cards reviewed; no recommendation or addressed instruction.
Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`.

### Computed self-check results

Writer checks and the accompanying manual source/box review returned no unresolved current-file errors. They are not an independent audit or adoption. Plain human/precondition gates are justified in the inventory above.

| Check | Count |
|---|---|
| cards | 218 |
| field_lines | 1963 |
| used_by_rows | 342 |
| empty_fields | 698 |
| internal_relationships | 287 |
| external_relationships | 42 |
| distinct_citations | 72 |
| resolved_citations | 72 |
| empty_together_cards | 128 |
| plain_together_lines | 2 |
| formula_hits | 0 |
| wording_hits | 0 |
| errors | 0 |
| named_card_mentions_checked | 1368 |
| misfiled_box_fields_scanned | 1963 |
| restriction_failure_gate_slots_reviewed | 654 |
| registered_empty_fields | 698 |
| cross_piece_continuations_checked | 42 |
| covered_read_file_paths | 145 |
| read_fingerprints_checked | 31 |
| source_names_checked | 46 |
| source_names_missing | 0 |
| built_field_lines | 0 |
| behavior_workflow_hits | 0 |
| plain_gates_justified | 1 |
| outgoing_continuations | 42 |
| incoming_continuations | 37 |
| registered_fields | 698 |
| additional_gaps | 8 |
| pending_source_paths | 60 |
| source_map_rows | 20 |
| read_record_rows | 31 |

The delivery recount compares these metrics with the finished file.
