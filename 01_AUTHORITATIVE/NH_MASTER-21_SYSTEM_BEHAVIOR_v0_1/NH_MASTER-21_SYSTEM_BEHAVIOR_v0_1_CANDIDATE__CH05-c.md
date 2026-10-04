# Chapter 5-c — Group C: C-7F

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH05-c.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`

This piece covers C-7F — Context Retrieval (§7F), with all its sub-parts. It leaves C-7H to CH05-d, C-CREATE to CH05-e, every path except P-MAIN to CH11, and the appendices to CH12.

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Every citation resolves at the pinned commit.

<!-- BEGIN BEHAVIOR -->

### C-7F — Context Retrieval (§7F)
Stamp: DESIGNED    Source: [V10 §7F] [MAP C-7F]

ALONE
- What it is: DESIGNED — The bounded supplier of wide context for a target reading, with positional and semantic evidence kept distinct. [V10 §7F] [MAP C-7F]
- Takes in: DESIGNED — A target root and an explicitly declared reading mode requested through LMAC. [V10 §7F] [MAP C-7F]
- Does: DESIGNED — Retrieves authorized context under the mode's own parameters, preserves item provenance, and supplies separately labeled prompt sections. [V10 §7F] [MAP C-7F]
- Gives out: DESIGNED — A labeled context package and an audit trail, or an honest empty/failure outcome. [V10 §7F] [MAP C-7F]
- Must never: DESIGNED — Merge channels, treat similarity as proof of relevance, or claim a failed retrieval succeeded. [V10 §7F] [MAP C-7F]
- Fails closed by: DESIGNED — Distinguishes genuine emptiness from index, service and timing failures; the source leaves exact failure fallback undesigned. [V10 §7F] [MAP C-7F]

TOGETHER
- Fed by: DESIGNED — C-7F.1 — Two separate retrieval channels: Preserves the two evidence channels. [V10 §7F]
- Fed by: DESIGNED — C-7F.2 — Conceptual channel combinations: Uses the declared channel combination. [V10 §7F]
- Fed by: DESIGNED — C-STORE — Accretive store & sealed roots (§6B): supplies the positional context channel separately from semantic context (CY-A); supplies material for the separate semantic context channel (CY-A). [V10 §7F / TWO CHANNELS, ALWAYS SEPARATE]
- Fed by: DECIDED-2026-09-25 — C-7A.6 — R4 — Meaning from wide context: supplies the wide context required for reading meaning. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 9] [98/sources/NH_Universal_Filter_RULES.md §RULE 4 — MEANING COMES FROM WIDE CONTEXT, NOT LOCAL WORDS] [MAP C-7A]
- Fed by: ACCEPTED — C-7B.7 — Hold-until-enough: provides the hold state of a held item encountered for retrieval to the governing privacy/relevance gates. [04/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7F.3 — B1 mode configuration record: Requires a valid mode configuration. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Gated by: ACCEPTED — C-7F.5 — B1 hard safety-ceiling mechanism: Cannot exceed hard ceilings. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration: Applies the concrete retrieval relevance declaration. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: DESIGNED — C-7F.7 — Retrieval outcome separation: Separates empty from failed retrieval. [V10 §7F]
- Gated by: DESIGNED — C-7F.8 — Retrieval empirical-value discipline: Leaves parameter defaults unlocked until empirical testing. [V10 §7F]
- Gated by: DESIGNED — C-LMAC — Live Mechanism Access Coordinator (§26): Requests internal-use authorization before receiving roots. [MAP C-7F] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): Receives only purpose-authorized material. [MAP C-7F] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Gated by: DECIDED-2026-09-24 — C-7B.9.5 — Eyes door: excludes Wonder scratch from default context-building reads. [DR §4] [98/sources/NH_MASTER-14_FINAL.md §7B / Part 6.5] [MAP C-7F]
- Gated by: DESIGNED — C-7R — Attention & Relevance Control (§7R): Uses relevance after prior privacy authorization. [MAP C-7F] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1]
- Changes: ACCEPTED — C-7F.4 — B1 retrieval audit record: Records each actual run. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.8 — Retrieval empirical-value discipline | Candidate parameters. | Tests before locking. | No universal n=3 assumption. | [V10 §7F] |
| 2 · DESIGNED | C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | Target and authorized context. | Supplies bounded context with provenance. | No blend of roots and interpretations. | [MAP C-ENGINE-C] |
| 3 · DESIGNED | C-ENGINE-C.2.1 — Root evidence channel | Root evidence. | Supplies authorized roots through separate retrieval channels. | Direct evidence remains distinct. | [MAP C-ENGINE-C] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 4 · DESIGNED | C-ENGINE-C.2.2 — Prior reading context channel | Separately supplied prior-reading context. | Preserves its interpretive channel and the unresolved exact retrieval-mode seam. | No prior reading enters RM-CR-01 [proposed]'s root pool. | [MAP C-ENGINE-C] |
| 5 · BUILT | C-INDEX.1.2 — Cosine distance | Meaning-distance matches. | Prevents semantic override of positional context. | No similarity-as-adjacency claim. | [V10 §7F] |
| 6 · DESIGNED | C-INDEX.5 — Semantic retrieval interface | Ranked index neighbors. | Applies the retrieval mode and provenance contract. | Bounded auditable semantic context. | [MAP C-INDEX] [V10 §7F] |
| 7 · DESIGNED | C-13.3 — Silent memory pull | Current purpose and target. | Provides labeled internal context. | No direct retrieval narration. | [MAP C-13] |
| 8 · ACCEPTED | C-14.6.3 — Reliable reference into retrieval | Reliability-qualified earlier-reference provenance. | Uses the consuming mode's declared boundary. | Uncertain references are not treated as resolved. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |
| 9 · DESIGNED | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | Target, mode and context. | Builds the pass input with distinct evidence. | No hidden channel mixing. | [MAP C-7G] |
| 10 · DESIGNED | C-7GA.11.2 — Step 2 — Retrieve context through LMAC | Worker target and declared mode. | Retrieves through LMAC and preserves provenance. | Context assembly remains inside the worker's mode restriction. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 11 · DESIGNED | C-LMAC — Live Mechanism Access Coordinator (§26); P-MAIN step 9 | Step 9: the target root and assigned mode, through LMAC after internal-use authorization. | Assembles bounded context with distinct positional/semantic provenance. | The reading pass receives honest context or an explicitly empty/failed outcome. | [V10 §7F] [MAP C-7F] |
| 12 · DESIGNED | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A); CY-A | The worker context-assembly step with bare/local-context restriction. | Retrieves eligible preceding material or honestly returns none. | The downstream pass keeps actual context provenance and technical failure separate. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |
| 13 · DESIGNED | C-13 — Live Loop (§13); CY-B | The live turn needing a silent authorized memory pull. | Supplies internal context without direct narration. | The reply can consume permitted context; full async synchronization remains separately open. | [MAP C-13] |
| 14 · DESIGNED | C-7A — Universal Filter (§7A) | Material admitted by the capture-exclusion, internal-use-authorization, root-ingestion and blocker gates. | Uses the wide context this card supplies. | Nothing in this card. | [V10 §7A] [MAP C-7A] [V10 §0] [V10 §0A] |
| 15 · ACCEPTED | C-7H.3.3 — RR2 — Instruction and context snapshot | A committed claim and valid reread_mode_ref [proposed]. | Retrieves authorized context before relevance consumption. | Nothing in this card. | [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §5] |
| 16 · ACCEPTED | C-7K.6.7 — Theme retrieval-influence honesty | The actual theme use and the context admitted for a future pass. | Takes this place's change: any actual theme admission into context retains the retrieval audit-trail influence; this honesty rule chooses no retrieval-influence policy. | Any actual theme admission into context retains the retrieval audit-trail influence; this honesty rule chooses no retrieval-influence policy. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §11] [04/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md §7] |
| 17 · ACCEPTED | C-CREATE.8.2 — Provisional influence in retrieval | A permitted provisional creation and retrieval operation. | Gates this place: existing retrieval declaration controls candidate scope. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §6] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A13] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 18 · DESIGNED | C-7N — Action Surfacing (§7N) | An explicit request or authorized proactive occasion, permitted source support, a current picture and the recorded response history. | Supplies authorized retrieved support. | Nothing in this card. | [V10 §7N] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §12] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] |
| 19 · DESIGNED | C-READ.3.7.3 — Retrieval audit carriage | The §7F retrieval audit. | Supplies the §7F retrieval audit. | Nothing in this card. | [V10 §7G-A / Step 5 — Write the reading record] |
| 20 · ACCEPTED | C-LMAC.3.1 — Context Retrieval query contract | Target and mode. | Supplies the actual retrieval operation and two-channel result. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 21 · ACCEPTED | C-24.2.1 — Accepted-connection retrieval route | The exact accepted ID/version, purpose and scope, current-use result, certainty, source types and accepted relevance configuration. | Supplies the actual retrieval operation. | Nothing in this card. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §13A] |
| 22 · ACCEPTED | C-16.9.12.11 — source_provenance_label [proposed] | The label from the retrieval channel. | Provides retrieval provenance with the item. | Nothing in this card. | [04/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md §1.5] |
| 23 · DESIGNED | C-LMAC.3.10 — Shared behavioral observation-root access | The permitted stored observation roots. | Supplies retrieval from shared memory. | Nothing in this card. | [V10 §26.5] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 24 · DESIGNED | C-LMAC.3.11 — Shared response-pattern reading access | The stored pattern readings produced by the Meaning Engine. | Supplies retrieval of shared readings. | Nothing in this card. | [V10 §26.5] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 25 · DESIGNED | C-24 — Connection Capability (§24) | Preserved endpoints, direct recorded relationships, explicit Ness confirmation or a narrowly authorized rule. | Takes this place's change: provides bounded relationship context and investigation guidance without creating a retrieval-side acceptance authority. | Provides bounded relationship context and investigation guidance without creating a retrieval-side acceptance authority. | [V10 §24] [MAP C-24] |
| 26 · DESIGNED | C-7M.2.5 — Computed View factor 5 — context quality and provenance | The context and provenance accompanying the source readings and retrieved material. | Supplies the labeled context channels and their retrieval provenance. | Nothing in this card. | [V10 §7M / SEVEN-FACTOR PRIORITY ORDER] |
| 27 · ACCEPTED | C-24.19.7 — Connection I7 accepted-use interface | Accepted ID/version and purpose. | Supplies retrieval owner. | Nothing in this card. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 28 · ACCEPTED | C-24.19.2 — Connection I2 candidate-report interface | Exact immutable source refs, how encountered, endpoint refs and apparent type/direction. | As the caller, supplies the encountered source references. | Nothing in this card. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 29 · ACCEPTED | C-24.19.6 — Connection I6 investigation-guidance interface | Proposal ID/version, endpoints, type, certainty and explicit proposed investigation_only_pending_connection marker. | Owns the actual retrieval investigation. | Nothing in this card. | [04/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md §18] |
| 30 · DESIGNED | C-BOP.9 — connection_anchors and later reconnection | Any available structural connection anchors. | Supplies semantic retrieval. | Nothing in this card. | [V10 §25.1] |
| 31 · DESIGNED | C-16 — Model Layer (§16) | Retrieved context and governing evidence before wording. | Provides context before generation. | Nothing in this card. | [V10 §16] [MAP C-16] |
| 32 · ACCEPTED | C-LMAC.14.2 — Reread context routing order | The assignment and broadest safely available clearly relevant context. | Gates this place: actual context retrieval. | Nothing in this card. | [04/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md §7] |
| 33 · ACCEPTED | C-7Q.11.6 — Retrieval, relevance and authorization-query boundary | The actual purpose, requesting component and target material references. | Takes this place's change: eligibility before retrieval/ranking. | Eligibility before retrieval/ranking. | [04/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md §16] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 34 · ACCEPTED | C-OOP.8.7 — OOP is not an LMAC query target | A request for behavioral context. | Supplies shared material through normal retrieval. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 35 · DESIGNED | C-24.2 — Connection retrieval role | Accepted connections or pending investigation hints and the current retrieval purpose. | Gates this place: its own retrieval rules remain binding. | Nothing in this card. | [V10 §24] |

SUB-PARTS: C-7F.1 — Two separate retrieval channels; C-7F.2 — Conceptual channel combinations; C-7F.3 — B1 mode configuration record; C-7F.4 — B1 retrieval audit record; C-7F.5 — B1 hard safety-ceiling mechanism; C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration; C-7F.7 — Retrieval outcome separation; C-7F.8 — Retrieval empirical-value discipline

### C-7F.1 — Two separate retrieval channels
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — Two evidentially different ways to select context. [V10 §7F]
- Takes in: DESIGNED — Recorded thread positions and potentially related stored material. [V10 §7F]
- Does: DESIGNED — Preserves adjacency as positional provenance and similarity as a fallible association. [V10 §7F]
- Gives out: DESIGNED — Separately identifiable positional and semantic context. [V10 §7F]
- Must never: DESIGNED — Make a semantic match appear to be a preceding turn. [V10 §7F]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7F.1.1 — Positional context: Receives recorded adjacency. [V10 §7F]
- Fed by: DESIGNED — C-7F.1.2 — Semantic context: Receives possible similarity relations. [V10 §7F]
- Gated by: DESIGNED — C-7F.1.3 — Separate prompt sections: Keeps presentation separate. [V10 §7F]
- Gated by: DESIGNED — C-7F.1.4 — Context conflict preservation: Preserves disagreements between channels. [V10 §7F]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F — Context Retrieval (§7F) | Position and similarity inputs. | Supplies distinct context. | No blended evidence. | [V10 §7F] |
| 2 · DESIGNED | C-7F.1.1 — Positional context | Preceding material. | Keeps adjacency distinct. | Honest positional provenance. | [V10 §7F] |
| 3 · DESIGNED | C-7F.1.2 — Semantic context | Similarity matches. | Keeps them interpretive. | No adjacency claim. | [V10 §7F] |
| 4 · DESIGNED | C-7F.1.3 — Separate prompt sections | Both channel outputs. | Separates their sections. | Distinct evidence presentation. | [V10 §7F] |
| 5 · DESIGNED | C-7F.1.4 — Context conflict preservation | Inconsistent contexts. | Preserves both. | Visible unresolved conflict. | [V10 §7F] |

SUB-PARTS: C-7F.1.1 — Positional context; C-7F.1.2 — Semantic context; C-7F.1.3 — Separate prompt sections; C-7F.1.4 — Context conflict preservation

### C-7F.1.1 — Positional context
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — Material immediately preceding the target in the same thread. [V10 §7F]
- Takes in: DESIGNED — The target's recorded thread position. [V10 §7F]
- Does: DESIGNED — Selects preceding material by position under the declared bound. [V10 §7F]
- Gives out: DESIGNED — Context about what happened immediately before the root. [V10 §7F]
- Must never: DESIGNED — Accept an unrelated semantic match as recorded adjacency. [V10 §7F]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7F.1 — Two separate retrieval channels: Retains the positional evidence boundary. [V10 §7F]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.1 — Two separate retrieval channels | Thread positions. | Selects preceding roots. | Positional context. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.1.2 — Semantic context
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — Stored material selected because it may relate to the target. [V10 §7F]
- Takes in: DESIGNED — The target and eligible material evaluated for similarity. [V10 §7F]
- Does: DESIGNED — Supplies bounded matches while retaining their distinct time, person, event and situation provenance. [V10 §7F]
- Gives out: DESIGNED — Possible associations, never proof that the matched material belongs to the target's direct context. [V10 §7F]
- Must never: DESIGNED — Override or silently repair positional context. [V10 §7F]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7F.1 — Two separate retrieval channels: Retains the semantic evidence boundary. [V10 §7F]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.1 — Two separate retrieval channels | Eligible matches. | Supplies semantic candidates. | Semantic context. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.1.3 — Separate prompt sections
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — The structural presentation boundary between the channels. [V10 §7F]
- Takes in: DESIGNED — Both channels when the mode supplies both. [V10 §7F]
- Does: DESIGNED — Places their contents in separate labeled sections of the downstream prompt. [V10 §7F]
- Gives out: DESIGNED — A prompt in which semantic matches remain distinguishable from preceding turns. [V10 §7F]
- Must never: DESIGNED — Blend the channels into one apparent conversation sequence. [V10 §7F]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7F.1 — Two separate retrieval channels: Implements permanent channel separation. [V10 §7F]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.1 — Two separate retrieval channels | Both channels. | Labels distinct prompt sections. | No false adjacency. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.1.4 — Context conflict preservation
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — The rule for inconsistent positional and semantic material. [V10 §7F]
- Takes in: DESIGNED — A conflict between the two channels. [V10 §7F]
- Does: DESIGNED — Surfaces the conflict without silently resolving it. [V10 §7F]
- Gives out: DESIGNED — Both conflicting contexts remain visible to the reading process as distinct evidence. [V10 §7F]
- Must never: DESIGNED — Select the semantic version to repair the positional record. [V10 §7F]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7F.1 — Two separate retrieval channels: Applies the shared separation rule to conflict. [V10 §7F]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.1 — Two separate retrieval channels | Conflicting context. | Surfaces the conflict. | No silent repair. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.2 — Conceptual channel combinations
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — Four conceptual categories rather than final mode names or empirical settings. [V10 §7F]
- Takes in: DESIGNED — The explicitly designed reading mode. [V10 §7F]
- Does: DESIGNED — Permits neither channel, positional only, semantic only, or both separately. [V10 §7F]
- Gives out: DESIGNED — The declared combination supplied to the engine. [V10 §7F]
- Must never: DESIGNED — Treat these categories as permission for every trigger to use every combination. [V10 §7F]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7F.2.1 — Bare retrieval category: Includes the no-context category. [V10 §7F]
- Fed by: DESIGNED — C-7F.2.2 — Local-context retrieval category: Includes the positional-only category. [V10 §7F]
- Fed by: DESIGNED — C-7F.2.3 — Associative retrieval category: Includes the semantic-only category. [V10 §7F]
- Fed by: DESIGNED — C-7F.2.4 — Combined retrieval category: Includes both channels separately. [V10 §7F]
- Gated by: DESIGNED — C-7GA.10 — thread_membership_v1: New-root use still follows the job's mode restrictions. [V10 §7G-A / MODE-ASSIGNMENT RULE:]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F — Context Retrieval (§7F) | Reading mode. | Chooses permitted channels. | An explicit input combination. | [V10 §7F] |

SUB-PARTS: C-7F.2.1 — Bare retrieval category; C-7F.2.2 — Local-context retrieval category; C-7F.2.3 — Associative retrieval category; C-7F.2.4 — Combined retrieval category

### C-7F.2.1 — Bare retrieval category
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — The conceptual no-context category. [V10 §7F]
- Takes in: DESIGNED — The target root. [V10 §7F]
- Does: DESIGNED — Supplies neither retrieval channel. [V10 §7F]
- Gives out: DESIGNED — Target-only input. [V10 §7F]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.2 — Conceptual channel combinations | Bare mode. | Supplies neither channel. | Target-only input. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.2.2 — Local-context retrieval category
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — The conceptual positional-only category. [V10 §7F]
- Takes in: DESIGNED — The target and its immediate thread surroundings. [V10 §7F]
- Does: DESIGNED — Supplies positional context only. [V10 §7F]
- Gives out: DESIGNED — A positional context section without semantic context. [V10 §7F]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.2 — Conceptual channel combinations | Local-context mode. | Supplies preceding context. | Positional-only input. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.2.3 — Associative retrieval category
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — The conceptual semantic-only category. [V10 §7F]
- Takes in: DESIGNED — The target and eligible similarity matches. [V10 §7F]
- Does: DESIGNED — Supplies semantic context only. [V10 §7F]
- Gives out: DESIGNED — A semantic context section without positional context. [V10 §7F]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.2 — Conceptual channel combinations | Associative mode. | Supplies similarity context. | Semantic-only input. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.2.4 — Combined retrieval category
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — The conceptual category supplying both channels. [V10 §7F]
- Takes in: DESIGNED — Positional and semantic material. [V10 §7F]
- Does: DESIGNED — Supplies both while keeping their sections and provenance separate. [V10 §7F]
- Gives out: DESIGNED — Two distinct context sections. [V10 §7F]
- Must never: DESIGNED — Merge the channel contents or their evidential claims. [V10 §7F]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.2 — Conceptual channel combinations | Combined mode. | Supplies two sections. | Distinct positional and semantic input. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.3 — B1 mode configuration record
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — A versioned proposed mechanical record for one retrieval mode's settings and bindings. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Takes in: ACCEPTED — Mode identity, purpose, consumer, declaration, bounded quantities, authorized scope, ceiling set and provenance. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Does: ACCEPTED — Records the required structure append-only; each change creates a new version while every empirical quantity remains open. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Gives out: ACCEPTED — An auditable mode configuration whose final field naming and serialization remain open. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Must never: ACCEPTED — Silently edit a prior configuration or invent a numeric default. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fails closed by: ACCEPTED — A missing required field, invalid A4 reference or ceiling excess makes the configuration invalid and prevents its execution. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]

TOGETHER
- Fed by: ACCEPTED — C-7F.3.1 — B1 mode identity: Binds stable mode identity and version. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fed by: ACCEPTED — C-7F.3.2 — B1 purpose_type [proposed]: Declares the settled purpose. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fed by: ACCEPTED — C-7F.3.3 — B1 consuming_component [proposed]: Names the running component. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fed by: ACCEPTED — C-7F.3.5 — B1 positional_context_limit [proposed]: Declares its positional quantity. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fed by: ACCEPTED — C-7F.3.6 — B1 semantic_result_limit [proposed]: Declares its semantic quantity. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fed by: ACCEPTED — C-7F.3.7 — B1 ranking_or_threshold_rule [proposed]: References the declared selection rule. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fed by: ACCEPTED — C-7F.3.8 — B1 token_size_budget [proposed]: Declares the context size envelope. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fed by: ACCEPTED — C-7F.3.9 — B1 time_range [proposed]: Carries an optional explicit time range. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fed by: ACCEPTED — C-7F.3.12 — B1 insufficient_context_fallback_behavior [proposed]: Declares genuine-empty fallback only. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fed by: ACCEPTED — C-7F.3.13 — B1 configuration_version [proposed]: Carries the actual configuration revision. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fed by: ACCEPTED — C-7F.3.14 — B1 configuration provenance: Preserves configuration change provenance. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Gated by: ACCEPTED — C-7F.3.4 — B1 a4_declaration_ref [proposed]: Requires a valid declaration reference. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Gated by: ACCEPTED — C-7F.3.10 — B1 eligible_source_scope [proposed]: Narrows eligible sources within authorization. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Gated by: ACCEPTED — C-7F.3.11 — B1 safety_ceiling_ref [proposed]: Requires the governing ceiling reference. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-7F.3.15 — B1 configuration validity rule: Rejects structurally invalid modes. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F — Context Retrieval (§7F) | Versioned settings. | Checks structural validity. | No undeclared retrieval. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] |
| 2 · ACCEPTED | C-7F.3.15 — B1 configuration validity rule | Configuration content. | Checks required fields and bindings. | Invalid modes cannot run. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] |

SUB-PARTS: C-7F.3.1 — B1 mode identity; C-7F.3.2 — B1 purpose_type [proposed]; C-7F.3.3 — B1 consuming_component [proposed]; C-7F.3.4 — B1 a4_declaration_ref [proposed]; C-7F.3.5 — B1 positional_context_limit [proposed]; C-7F.3.6 — B1 semantic_result_limit [proposed]; C-7F.3.7 — B1 ranking_or_threshold_rule [proposed]; C-7F.3.8 — B1 token_size_budget [proposed]; C-7F.3.9 — B1 time_range [proposed]; C-7F.3.10 — B1 eligible_source_scope [proposed]; C-7F.3.11 — B1 safety_ceiling_ref [proposed]; C-7F.3.12 — B1 insufficient_context_fallback_behavior [proposed]; C-7F.3.13 — B1 configuration_version [proposed]; C-7F.3.14 — B1 configuration provenance; C-7F.3.15 — B1 configuration validity rule

### C-7F.3.1 — B1 mode identity
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — The proposed mode_id and mode_version identity pair. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Takes in: ACCEPTED — The configured retrieval mode and its revision. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Does: ACCEPTED — Binds a stable mode to an immutable version; changes produce a new version. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Gives out: ACCEPTED — The exact mode identity used for a run. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Must never: ACCEPTED — Reuse the same version for changed configuration content. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7F.3.1.1 — B1 mode_id [proposed]: Identifies the mode. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fed by: ACCEPTED — C-7F.3.1.2 — B1 mode_version [proposed]: Identifies the revision. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3 — B1 mode configuration record | Mode revision. | Records the identity pair. | Versioned configuration. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] |
| 2 · ACCEPTED | C-7F.4.2 — B1 applied configuration bindings | Mode ID/version. | Copies its reference into the audit. | Correct mode provenance. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: C-7F.3.1.1 — B1 mode_id [proposed]; C-7F.3.1.2 — B1 mode_version [proposed]

### C-7F.3.1.1 — B1 mode_id [proposed]
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — The proposed stable mode identifier. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Takes in: ACCEPTED — The retrieval mode being configured. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Does: ACCEPTED — Identifies that mode across its versions. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Gives out: ACCEPTED — mode_id [proposed]. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3.1 — B1 mode identity | Stable ID. | Records mode_id [proposed]. | Stable mode reference. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] |

SUB-PARTS: NONE

### C-7F.3.1.2 — B1 mode_version [proposed]
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — The proposed version of a mode. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Takes in: ACCEPTED — The exact configuration revision. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Does: ACCEPTED — Distinguishes this immutable revision from earlier and later ones. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Gives out: ACCEPTED — mode_version [proposed]. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Must never: ACCEPTED — Silently reuse a prior version after changing the mode. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3.1 — B1 mode identity | Immutable version. | Records mode_version [proposed]. | Exact mode revision. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] |

SUB-PARTS: NONE

### C-7F.3.2 — B1 purpose_type [proposed]
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — The mode's purpose drawn from the settled five-value relevance vocabulary. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Takes in: ACCEPTED — One settled purpose type and an optional explanatory label. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Does: ACCEPTED — Binds the mode to its purpose; the optional label carries no system behavior. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Gives out: ACCEPTED — purpose_type [proposed]. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Must never: ACCEPTED — Invent a private relevance purpose through the label. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3 — B1 mode configuration record | Controlled purpose value. | Binds purpose. | No private meaning. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] |

SUB-PARTS: NONE

### C-7F.3.3 — B1 consuming_component [proposed]
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — The proposed field identifying which component runs this mode. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Takes in: ACCEPTED — The consuming component's identity. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Does: ACCEPTED — Records that identity with the configuration. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Gives out: ACCEPTED — consuming_component [proposed]. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3 — B1 mode configuration record | Consumer identity. | Records the consumer. | Attributable use. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] |
| 2 · ACCEPTED | C-7F.6.14 — A4 eight-field declaration validity | Consumer identity. | Carries the component field. | First mandatory declaration field. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.3.4 — B1 a4_declaration_ref [proposed]
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — A proposed reference to the consuming component's A4 declaration by identifier and version. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — A valid declaration for the current purpose. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Binds by reference without duplicating or redefining its relevance meaning. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — a4_declaration_ref [proposed]. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Run a mode without a valid declaration for its purpose. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — A missing or invalid referenced declaration prevents the retrieval mode from running. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.6.14 — A4 eight-field declaration validity: Applies the mandatory declaration contract. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3 — B1 mode configuration record | Declaration ID/version. | Binds the accepted declaration. | A valid mode or no execution. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-7F.3.5 — B1 positional_context_limit [proposed]
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [V10 §7F]

ALONE
- What it is: ACCEPTED — The proposed bound on immediately preceding material supplied. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [V10 §7F]
- Takes in: ACCEPTED — A per-mode positional bound whose empirical value remains open. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [V10 §7F]
- Does: ACCEPTED — Limits the amount of positional material in this mode. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [V10 §7F]
- Gives out: ACCEPTED — positional_context_limit [proposed]. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [V10 §7F]
- Must never: ACCEPTED — Treat the built Engine B experiment's n=3 as a universal future value. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [V10 §7F]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3 — B1 mode configuration record | Open empirical bound. | Limits preceding context. | Bounded positional input. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] |

SUB-PARTS: NONE

### C-7F.3.6 — B1 semantic_result_limit [proposed]
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — The proposed bound on semantic matches supplied. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Takes in: ACCEPTED — A per-mode semantic quantity whose empirical value remains open. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Does: ACCEPTED — Limits this mode's semantic result count. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Gives out: ACCEPTED — semantic_result_limit [proposed]. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Must never: ACCEPTED — Request unlimited matches. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3 — B1 mode configuration record | Open empirical bound. | Limits semantic results. | Bounded semantic input. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] |

SUB-PARTS: NONE

### C-7F.3.7 — B1 ranking_or_threshold_rule [proposed]
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — A proposed reference to the mode's ranking or threshold rule by identifier and version. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Takes in: ACCEPTED — A declared rule reference; rule content and threshold values remain open. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Does: ACCEPTED — Binds selection and ordering to the declared rule. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Gives out: ACCEPTED — ranking_or_threshold_rule [proposed]. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Must never: ACCEPTED — Lower a threshold silently; any change requires a new configuration version. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3 — B1 mode configuration record | Rule identity/version. | Binds ranking or threshold. | Traceable selection. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] |

SUB-PARTS: NONE

### C-7F.3.8 — B1 token_size_budget [proposed]
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — The proposed size envelope for the assembled context package. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Takes in: ACCEPTED — The mode's explicit budget; its value remains open. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Does: ACCEPTED — Bounds the supplied context size. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Gives out: ACCEPTED — token_size_budget [proposed]. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Must never: ACCEPTED — Supply unbounded material. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3 — B1 mode configuration record | Open size budget. | Bounds assembly. | Finite supplied material. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] |

SUB-PARTS: NONE

### C-7F.3.9 — B1 time_range [proposed]
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — An optional explicit and recorded temporal range. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Takes in: ACCEPTED — A declared range when the mode uses one; its span value remains open. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Does: ACCEPTED — Records and applies that range rather than implying an undeclared temporal cutoff. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Gives out: ACCEPTED — time_range [proposed] when present. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3 — B1 mode configuration record | Declared temporal range. | Records its use. | No hidden cutoff. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] |

SUB-PARTS: NONE

### C-7F.3.10 — B1 eligible_source_scope [proposed]
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The source scope a mode may use inside prior purpose-specific authorization. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Takes in: ACCEPTED — Material already authorized by Privacy, Deletion, Sensitive-data through LMAC. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Does: ACCEPTED — Narrows use to the declared eligible source scope. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Gives out: ACCEPTED — An authorized, potentially narrower candidate scope. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Must never: ACCEPTED — Widen access or reveal or signal withheld material. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — No unauthorized root is returned. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): Authorization precedes source narrowing. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3 — B1 mode configuration record | Authorized scope. | Limits source use. | No widened access. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] |

SUB-PARTS: NONE

### C-7F.3.11 — B1 safety_ceiling_ref [proposed]
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — A mandatory proposed reference to the versioned ceiling set governing this mode. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The applicable ceiling identity and version. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Binds the mode to the hard bounds above its own settings. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — safety_ceiling_ref [proposed]. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Let a mode select limits beyond its governing ceiling set. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — A required ceiling reference cannot be omitted from a runnable configuration. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.5 — B1 hard safety-ceiling mechanism: References a versioned external ceiling set. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3 — B1 mode configuration record | Ceiling identity/version. | Binds external maxima. | No unrestricted setting. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7F.3.12 — B1 insufficient_context_fallback_behavior [proposed]
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The proposed configuration field for the healthy genuine-empty outcome only. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — A retrieval that honestly finds no relevant context. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Declares bare continuation marked context-limited and revisable. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — insufficient_context_fallback_behavior [proposed]. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Use this field to authorize continuation after a system failure. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — System failure is handled by B26 rather than relabeled genuine emptiness. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7F.7.1 — Genuine empty-result handling: Uses only the healthy empty route. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3 — B1 mode configuration record | Healthy no-context outcome. | Specifies marked bare use. | Failure stays separate. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] |

SUB-PARTS: NONE

### C-7F.3.13 — B1 configuration_version [proposed]
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — The proposed exact configuration-version field. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Takes in: ACCEPTED — The revision actually used. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Does: ACCEPTED — Carries the configuration identity into the audit trail alongside mode identity. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Gives out: ACCEPTED — configuration_version [proposed]. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Must never: ACCEPTED — Silently alter the referenced configuration. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3 — B1 mode configuration record | Configuration version. | Records exact settings identity. | Reproducible provenance. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] |
| 2 · ACCEPTED | C-7F.4.2 — B1 applied configuration bindings | Configuration revision. | Records its reference. | Correct setting provenance. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7F.3.14 — B1 configuration provenance
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — The change provenance attached to a mode configuration. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Takes in: ACCEPTED — Who changed it, when, and what changed. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Does: ACCEPTED — Preserves change provenance and prior versions. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Gives out: ACCEPTED — An attributable append-only configuration history. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Must never: ACCEPTED — Erase prior versions by rewriting them. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7F.3.14.1 — Configuration change actor: Carries the change actor. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fed by: ACCEPTED — C-7F.3.14.2 — Configuration change time: Carries the change time. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Fed by: ACCEPTED — C-7F.3.14.3 — Configuration change content: Carries the actual difference. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3 — B1 mode configuration record | Who, when and what changed. | Records the change. | Attributable history. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] |

SUB-PARTS: C-7F.3.14.1 — Configuration change actor; C-7F.3.14.2 — Configuration change time; C-7F.3.14.3 — Configuration change content

### C-7F.3.14.1 — Configuration change actor
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — The actor element of configuration provenance. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Takes in: ACCEPTED — Who made the configuration change. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Does: ACCEPTED — Records the change actor. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Gives out: ACCEPTED — Attributable change identity. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3.14 — B1 configuration provenance | Who changed it. | Records actor provenance. | Attributable configuration. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] |

SUB-PARTS: NONE

### C-7F.3.14.2 — Configuration change time
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — The temporal element of configuration provenance. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Takes in: ACCEPTED — When the configuration changed. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Does: ACCEPTED — Records that time. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Gives out: ACCEPTED — Change timestamp provenance. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3.14 — B1 configuration provenance | When it changed. | Records temporal provenance. | Dated configuration. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] |

SUB-PARTS: NONE

### C-7F.3.14.3 — Configuration change content
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — The difference element of configuration provenance. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Takes in: ACCEPTED — What changed from the preserved prior configuration. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Does: ACCEPTED — Records the change itself. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Gives out: ACCEPTED — Traceable configuration differences. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3.14 — B1 configuration provenance | What changed. | Records content provenance. | Traceable revisions. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] |

SUB-PARTS: NONE

### C-7F.3.15 — B1 configuration validity rule
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The fail-closed structural admission rule for a retrieval mode. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — All required fields, the referenced A4 declaration and the governing ceiling set. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Rejects any missing required field, invalid declaration reference or setting above a ceiling before running the mode. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — Either a structurally valid bounded configuration or a recorded invalid condition. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Repair invalidity with silent defaults or run despite ceiling excess. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — The invalid mode never runs; failure-event handling remains with the honest B26 path. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.3 — B1 mode configuration record: Enforces the mode-record contract. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2]
- Gated by: ACCEPTED — C-7F.5 — B1 hard safety-ceiling mechanism: Rejects any ceiling excess. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3 — B1 mode configuration record | Required fields and references. | Validates completeness and ceilings. | No invalid execution. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7F.4 — B1 retrieval audit record
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — Exactly one append-only audit record for each retrieval run. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — The exact configuration, channels, applied parameters, versions, supplied roots, cuts and outcome. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Records what actually happened, including every ceiling event and the downstream reading pointer. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — A protected audit trail that makes hidden channel mixing, substitution and over-retrieval detectable. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: ACCEPTED — Rewrite prior audit records or count repetition as additional certainty or evidence. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Empty-result and failure outcomes remain explicitly distinct. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]

TOGETHER
- Fed by: ACCEPTED — C-7F.4.1 — B1 audit_record_id: Identifies the retrieval audit. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fed by: ACCEPTED — C-7F.4.2 — B1 applied configuration bindings: Records the applied bindings. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fed by: ACCEPTED — C-7F.4.3 — B1 channels queried: Records channel queries separately. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fed by: ACCEPTED — C-7F.4.4 — B1 parameters applied and ceiling events: Records applied bounds and interventions. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fed by: ACCEPTED — C-7F.4.5 — B1 retrieval version provenance: Records retrieval implementation versions. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fed by: ACCEPTED — C-7F.4.6 — Supplied-root item provenance: Records the exact supplied items. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fed by: ACCEPTED — C-7F.4.7 — Retrieval exclusions and truncation: Records every bound-caused cut. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fed by: ACCEPTED — C-7F.4.8 — Retrieval empty-versus-failure marker: Records honest empty/failure status. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fed by: ACCEPTED — C-7F.4.9 — Retrieval reading audit-trail pointer: Connects retrieval to its reading use. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fed by: ACCEPTED — C-7F.4.10 — B1 audit_config_version: Records governing audit/ceiling configuration. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fed by: DESIGNED — C-7F.4.12 — Retrieval execution timestamp: Preserves execution time in the reading audit. [V10 §7F] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gated by: ACCEPTED — C-7F.4.11 — Retrieval audit protection and one-log rule: Applies one-log and record-protection rules. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F — Context Retrieval (§7F) | Run inputs and outcomes. | Appends its audit. | Traceable retrieval. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |
| 2 · ACCEPTED | C-7F.4.11 — Retrieval audit protection and one-log rule | One real run. | Leaves one record. | No duplicate operation log. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |
| 3 · ACCEPTED | C-7F.6.12 — RM-CR-01 [proposed] logging contract | Actual run. | Records items, versions, cuts and outcome. | Full retrieval provenance. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: C-7F.4.1 — B1 audit_record_id; C-7F.4.2 — B1 applied configuration bindings; C-7F.4.3 — B1 channels queried; C-7F.4.4 — B1 parameters applied and ceiling events; C-7F.4.5 — B1 retrieval version provenance; C-7F.4.6 — Supplied-root item provenance; C-7F.4.7 — Retrieval exclusions and truncation; C-7F.4.8 — Retrieval empty-versus-failure marker; C-7F.4.9 — Retrieval reading audit-trail pointer; C-7F.4.10 — B1 audit_config_version; C-7F.4.11 — Retrieval audit protection and one-log rule; C-7F.4.12 — Retrieval execution timestamp

### C-7F.4.1 — B1 audit_record_id
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The proposed stable identity for the retrieval run's audit record. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — The actual retrieval run. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Identifies its single audit record. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — audit_record_id. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: ACCEPTED — Duplicate an operation's log. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.4 — B1 retrieval audit record | Run identity. | Records stable ID. | One identifiable audit. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7F.4.2 — B1 applied configuration bindings
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The exact mode_id [proposed], mode_version [proposed] and configuration_version [proposed] actually used. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — The run's resolved configuration bindings. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Records the applied identities, rather than a later current configuration. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — Reproducible configuration provenance for the run. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: ACCEPTED — Substitute a different configuration version into the historical audit. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7F.3.1 — B1 mode identity: Uses the exact applied mode identity. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fed by: ACCEPTED — C-7F.3.13 — B1 configuration_version [proposed]: Uses the exact applied configuration version. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.4 — B1 retrieval audit record | Mode/configuration versions. | Preserves exact versions. | Reproducible run provenance. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7F.4.3 — B1 channels queried
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The record of which retrieval channels were queried. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — The run's positional and semantic query activity. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Records each queried channel separately. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — Distinct channel audit entries. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: ACCEPTED — Merge channel identities. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.4 — B1 retrieval audit record | Actual channel activity. | Preserves channel identities. | No blended audit. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7F.4.4 — B1 parameters applied and ceiling events
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The run's actual retrieval parameters and any ceiling enforcement. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — Applied settings and runtime clamp or enforcement events. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Records both what was applied and every ceiling intervention. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — Visible parameter and enforcement provenance. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Silently enforce, expand or substitute a bound without recording the event. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.4 — B1 retrieval audit record | Parameters and ceiling events. | Logs actual enforcement. | No hidden clamping. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |
| 2 · ACCEPTED | C-7F.5.6 — B1 runtime ceiling defense | Actual intervention. | Adds it to the run audit. | Visible clamping. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7F.4.5 — B1 retrieval version provenance
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — Version provenance for all three retrieval producers and services named by B1. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — Embedding-model, index and retrieval-system versions. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Preserves the exact versions used for the run. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — A three-part version record. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7F.4.5.1 — Retrieval embedding-model version: Preserves the embedding revision. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fed by: ACCEPTED — C-7F.4.5.2 — Retrieval index version: Preserves the index revision. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fed by: ACCEPTED — C-7F.4.5.3 — Retrieval system version: Preserves the retrieval-system revision. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.4 — B1 retrieval audit record | Model/index/system versions. | Preserves their provenance. | Exact run versions. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: C-7F.4.5.1 — Retrieval embedding-model version; C-7F.4.5.2 — Retrieval index version; C-7F.4.5.3 — Retrieval system version

### C-7F.4.5.1 — Retrieval embedding-model version
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The embedding-model version used for semantic retrieval. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — The actual embedding model revision. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Records that revision. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — Embedding-model version provenance. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.4.5 — B1 retrieval version provenance | Model version. | Records it. | Semantic producer provenance. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7F.4.5.2 — Retrieval index version
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The index version used for retrieval. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — The actual queried index revision. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Records that revision. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — Index version provenance. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.4.5 — B1 retrieval version provenance | Index version. | Records it. | Index provenance. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7F.4.5.3 — Retrieval system version
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The retrieval-system version executing the run. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — The actual system revision. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Records that revision. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — Retrieval-system version provenance. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.4.5 — B1 retrieval version provenance | System version. | Records it. | Execution-system provenance. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7F.4.6 — Supplied-root item provenance
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The exact roots supplied, recorded separately per channel with each item's selection provenance. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — A supplied root's type, admission reason, source root/thread, timestamp and score or position. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Preserves the evidence needed to distinguish position from similarity and to explain any theme influence. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — Per-item provenance accompanying supplied roots. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Convert retrieval presence or repeated selection into evidence of truth. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7F.4.6.1 — Supplied-item retrieval type: Carries channel type. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fed by: ACCEPTED — C-7F.4.6.2 — Supplied-item admission reason: Carries actual selection reasons. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-7F.4.6.3 — Supplied-item source root: Carries the source root identity. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fed by: ACCEPTED — C-7F.4.6.4 — Supplied-item thread or grouping: Carries source grouping. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fed by: ACCEPTED — C-7F.4.6.5 — Supplied-item timestamp: Carries source time. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fed by: ACCEPTED — C-7F.4.6.6 — Supplied-item score or position: Carries channel-appropriate score or position. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.4 — B1 retrieval audit record | Per-channel source roots. | Preserves per-item provenance. | Traceable context. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |
| 2 · ACCEPTED | C-7N.13.5.1 — Action-surfacing current-situation provenance test | Actual live/present material of the ongoing exchange or current positional context from the positional channel with honest present-context provenance. | Supplies supplied-item provenance, preserving the positional-channel basis where applicable. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] |

SUB-PARTS: C-7F.4.6.1 — Supplied-item retrieval type; C-7F.4.6.2 — Supplied-item admission reason; C-7F.4.6.3 — Supplied-item source root; C-7F.4.6.4 — Supplied-item thread or grouping; C-7F.4.6.5 — Supplied-item timestamp; C-7F.4.6.6 — Supplied-item score or position

### C-7F.4.6.1 — Supplied-item retrieval type
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The item's positional or semantic retrieval identity. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — The channel that selected the item. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Carries that identity as provenance. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — Retrieval type. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: ACCEPTED — Treat channel identity as a relevance dimension. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.4.6 — Supplied-root item provenance | Selecting channel. | Records type. | Distinct evidence class. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |
| 2 · DESIGNED | C-7R.7.3 — Retrieval-channel provenance boundary | Each retrieved item’s channel metadata. | Supplies canonical supplied-item retrieval type. | Nothing in this card. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [V10 §7R] |

SUB-PARTS: NONE

### C-7F.4.6.2 — Supplied-item admission reason
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The explanation of why an item was supplied. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — The admitting rule, score or position and any theme or pattern influence. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Records the actual reason, including every theme-guided search influence. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — Why-admitted provenance. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Hide theme influence or treat a theme as proof of a connection. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.4.6 — Supplied-root item provenance | Rule, score, position and theme influence. | Records why admitted. | Explained selection. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7F.6.10.2 — Retrieval theme and pattern influence | Theme-guided selection. | Writes why admitted. | Honest retrieval influence trail. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.4.6.3 — Supplied-item source root
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The exact source root identifier of a supplied item. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — The admitted root. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Preserves its root identity. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — A source root pointer. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.4.6 — Supplied-root item provenance | Admitted root ID. | Records the exact pointer. | Source traceability. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7F.4.6.4 — Supplied-item thread or grouping
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The supplied root's source thread or grouping provenance. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — Its recorded source grouping. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Carries that grouping with the item. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — Source-thread provenance. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: ACCEPTED — Imply that a semantic match belongs to the target's thread when it does not. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.4.6 — Supplied-root item provenance | Source thread. | Records grouping provenance. | No fabricated adjacency. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7F.4.6.5 — Supplied-item timestamp
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The source timestamp carried with a retrieved item. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — The item's source time provenance. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Preserves that timestamp with the supplied root. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — Item timestamp provenance. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.4.6 — Supplied-root item provenance | Item timestamp. | Records it. | Temporal source provenance. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7F.4.6.6 — Supplied-item score or position
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The selection score or position where relevant to the item's channel. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — The actual retrieval score or recorded position. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Records the channel-appropriate selection value. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — A score or position tied to the supplied root. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: ACCEPTED — Use a similarity score as proof of direct adjacency. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.4.6 — Supplied-root item provenance | Selection value. | Records the actual value. | Selection traceability. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7F.4.7 — Retrieval exclusions and truncation
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The record of material cut by declared bounds. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — What was excluded or truncated and the limit or ceiling responsible. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Records both the cut and its cause. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — Auditable exclusion and truncation provenance. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: ACCEPTED — Silently alter the supplied context by hiding cuts. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.4 — B1 retrieval audit record | Exclusions and truncation. | Names the responsible bound. | Honest context reduction. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7F.4.8 — Retrieval empty-versus-failure marker
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The audit slot distinguishing healthy emptiness from a system failure. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Takes in: ACCEPTED — The actual retrieval outcome. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Does: ACCEPTED — Preserves genuine empty results as normal and failures as failures. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Gives out: ACCEPTED — An honest outcome marker whose failure-state mechanics belong to B26. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Must never: ACCEPTED — Claim retrieval succeeded after it failed. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Failure cannot take the genuine-empty bare-fallback route. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7F.7 — Retrieval outcome separation: Preserves the settled outcome distinction. [V10 §7F] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.4 — B1 retrieval audit record | Actual outcome. | Keeps the two distinct. | No false success. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |
| 2 · ACCEPTED | C-7R.15.8.2 — Genuine-empty context boundary | A genuine empty result, distinct from retrieval-system failure. | Supplies the canonical empty-versus-failure audit distinction. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] |

SUB-PARTS: NONE

### C-7F.4.9 — Retrieval reading audit-trail pointer
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The downstream linkage between retrieval audit and reading provenance. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — The consuming reading's audit-trail linkage. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Connects the supplied context to its reading use. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — A reading audit-trail pointer. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.4 — B1 retrieval audit record | Reading linkage. | Records the pointer. | Downstream audit continuity. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7F.4.10 — B1 audit_config_version
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The proposed audit/ceiling configuration version in force for the run. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The actual audit configuration and ceiling-set reference. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Records the versioned governing configuration with the audit. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — audit_config_version and traceable ceiling-set provenance. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Substitute a later ceiling version for the one actually used. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.4 — B1 retrieval audit record | Actual version bindings. | Preserves them. | Traceable enforcement context. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7F.4.11 — Retrieval audit protection and one-log rule
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The append-only, access-controlled protection of retrieval audit records. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Takes in: ACCEPTED — One actual retrieval operation and its record. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Does: ACCEPTED — Applies purpose-specific privacy/access and applicable identity/security authorization to the record. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gives out: ACCEPTED — One protected operation log. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Must never: ACCEPTED — Rewrite logs, create double evidence, or increase certainty through repetition. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Record access remains subject to authorization. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.4 — B1 retrieval audit record: Applies the audit owner's append-only rule. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): Protects audit access. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.4 — B1 retrieval audit record | Operation and authorization. | Protects append-only logging. | No duplicate evidence. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7F.4.12 — Retrieval execution timestamp
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — The time of retrieval execution in the eventual reading audit trail. [V10 §7F]
- Takes in: DESIGNED — The retrieval execution time. [V10 §7F]
- Does: DESIGNED — Preserves that timestamp with the mode, supplied roots, parameters and versions. [V10 §7F]
- Gives out: DESIGNED — Execution timestamp provenance. [V10 §7F]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.4 — B1 retrieval audit record | Actual execution timestamp. | Records when retrieval ran. | Temporal audit provenance. | [V10 §7F] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7F.5 — B1 hard safety-ceiling mechanism
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — A versioned boundary above all mode-level retrieval quantities. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — A mode's settings and the referenced ceiling set. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Applies the lower of setting and ceiling, rejects excess configurations, and independently enforces runtime ceilings. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — Bounded retrieval with every enforcement event recorded. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Let a mode grant itself more retrieval or change ceilings as a runtime side effect. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Configurations above a ceiling are invalid and rejected; runtime never exceeds the ceiling regardless of configuration state. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: ACCEPTED — C-7F.5.1 — B1 ceiling_set_id: Names the ceiling set. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7F.5.2 — B1 ceiling-set version: Names its immutable revision. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7F.5.3 — B1 bounded-quantity maxima: Includes every bounded quantity. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-7F.5.4 — B1 minimum-precedence rule: Applies the lower effective limit. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-7F.5.5 — B1 configuration-time rejection: Rejects excess before execution. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-7F.5.6 — B1 runtime ceiling defense: Enforces ceilings at runtime independently. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gated by: ACCEPTED — C-7F.5.7 — B1 versioned ceiling change: Changes ceilings only through a new authorized version. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F — Context Retrieval (§7F) | Mode quantities. | Enforces external bounds. | Bounded material. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4] |
| 2 · ACCEPTED | C-7F.3.11 — B1 safety_ceiling_ref [proposed] | Ceiling binding. | Applies its bounds. | Bounded configuration. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4] |
| 3 · ACCEPTED | C-7F.3.15 — B1 configuration validity rule | Settings and maxima. | Compares each bound. | Recorded invalidity. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4] |
| 4 · ACCEPTED | C-7F.5.4 — B1 minimum-precedence rule | Mode and ceiling bounds. | Keeps the minimum. | Bounded retrieval. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4] |
| 5 · ACCEPTED | C-7F.5.5 — B1 configuration-time rejection | Excess configuration. | Rejects and records. | No invalid execution. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4] |
| 6 · ACCEPTED | C-7F.5.6 — B1 runtime ceiling defense | Retrieval quantities. | Prevents excess. | Audited ceiling protection. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4] |
| 7 · ACCEPTED | C-7F.5.7 — B1 versioned ceiling change | Authorized ceiling decision. | Creates a new revision. | Prior runs retain their bounds. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: C-7F.5.1 — B1 ceiling_set_id; C-7F.5.2 — B1 ceiling-set version; C-7F.5.3 — B1 bounded-quantity maxima; C-7F.5.4 — B1 minimum-precedence rule; C-7F.5.5 — B1 configuration-time rejection; C-7F.5.6 — B1 runtime ceiling defense; C-7F.5.7 — B1 versioned ceiling change

### C-7F.5.1 — B1 ceiling_set_id
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The proposed stable identifier of a ceiling set. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The ceiling set governing a mode. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Identifies that set independently from individual mode settings. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — ceiling_set_id. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.5 — B1 hard safety-ceiling mechanism | Set identity. | Records its ID. | Stable ceiling binding. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7F.5.2 — B1 ceiling-set version
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The version of the ceiling set in force. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The selected immutable ceiling revision. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Preserves that revision in references and the audit trail. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — Versioned ceiling identity. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Change the meaning of an already-recorded ceiling revision. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.5 — B1 hard safety-ceiling mechanism | Set version. | Records its version. | Exact ceiling binding. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7F.5.3 — B1 bounded-quantity maxima
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — Hard maxima for positional quantity, semantic quantity, token/size budget, time-range span and any later declared bounded quantity. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The bounded quantities declared by a mode. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Gives every such quantity a ceiling above its per-mode setting; every ceiling value remains open. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — A complete bound structure without invented numeric values. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Leave a declared bounded quantity unlimited. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.5 — B1 hard safety-ceiling mechanism | Declared bound categories. | Defines their maxima. | No unbounded quantity. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7F.5.4 — B1 minimum-precedence rule
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The effective-limit rule for each bounded quantity. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — The mode setting and its corresponding ceiling. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Uses the minimum of the two; a mode may set itself lower but never higher. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — An effective bound no greater than the ceiling. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Interpret minimum-precedence as permission to accept an excess configuration. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Excess configuration is still rejected before execution. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.5 — B1 hard safety-ceiling mechanism: Uses the owner's precedence rule. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.5 — B1 hard safety-ceiling mechanism | Setting and ceiling. | Computes the minimum. | Effective bound within ceiling. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7F.5.5 — B1 configuration-time rejection
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The pre-execution check for ceiling excess. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — A proposed configuration and its referenced ceiling set. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Rejects and records any setting above the relevant ceiling. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — A recorded configuration rejection. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Silently clamp an invalid configuration into apparent validity. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — The rejected configuration does not run. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.5 — B1 hard safety-ceiling mechanism: Implements pre-execution rejection. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.5 — B1 hard safety-ceiling mechanism | Configuration bounds. | Records rejection. | Invalid mode cannot run. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7F.5.6 — B1 runtime ceiling defense
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — Independent ceiling enforcement during execution. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — Runtime retrieval activity regardless of configuration state. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Prevents ceiling excess and records every enforcement event in the run's audit. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — Bounded runtime activity with visible enforcement provenance. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Exceed a hard ceiling or hide its enforcement. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Runtime remains within the ceiling even if the configuration state is faulty. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.5 — B1 hard safety-ceiling mechanism: Implements independent runtime enforcement. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Changes: ACCEPTED — C-7F.4.4 — B1 parameters applied and ceiling events: Records every enforcement event. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.5 — B1 hard safety-ceiling mechanism | Runtime quantities. | Bounds and records enforcement. | No runtime excess. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7F.5.7 — B1 versioned ceiling change
Stamp: ACCEPTED    Source: [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The rule that a ceiling change requires a separately versioned authorized change. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Takes in: ACCEPTED — A later authorized ceiling-setting decision. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Does: ACCEPTED — Creates a new version while retaining the version used by each earlier run. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Gives out: ACCEPTED — A new ceiling version without changing prior audits. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Must never: ACCEPTED — Change ceilings as a mode's runtime side effect. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.5 — B1 hard safety-ceiling mechanism: Implements version-only change. [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.5 — B1 hard safety-ceiling mechanism | Authorized revision. | Preserves past versions. | No silent expansion. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Context Retrieval's complete accepted purpose-scoped Tier 1/Tier 2 declaration, using proposed mechanical identifiers. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — A target root, authorized root candidates and the applicable B1 configuration. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Selects context under the declared gates, dimensions, ordering, uncertainty, audit and fail-closed rules. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — A purpose-relevant separate-channel root package for the requesting reading pass. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Invent a private relevance meaning or treat relevance as truth, authority, current-state evidence or action permission. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Missing required declaration fields, invalid configuration, ceiling violation or unauthorized candidates prevent the mode from running. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-7F.6.1 — RM-CR-01 [proposed] declaration identity: Carries its exact declaration identity. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-7F.6.2 — Retrieval-context-selection purpose: Declares retrieval_context_selection. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-7F.6.3 — RM-CR-01 [proposed] target: Selects for the requested root. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-7F.6.4 — RM-CR-01 [proposed] candidate roots: Accepts authorized roots only. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-7F.6.6 — RM-CR-01 [proposed] graded dimensions: Uses its selected graded dimensions. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-7F.6.9 — RM-CR-01 [proposed] reason: Carries the explicit wide-context reason. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7F.6.5 — RM-CR-01 [proposed] deterministic context gates: Applies the channel's categorical conditions. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7F.6.7 — RM-CR-01 [proposed] mouth authorization: Authorizes no mouth dimension. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7F.6.8 — RM-CR-01 [proposed] on-demand evaluation timing: Runs only on demand in this version. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7F.6.10 — RM-CR-01 [proposed] Tier 2 rules: Applies the consumer's Tier-2 rules. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7F.6.11 — RM-CR-01 [proposed] allowed-use boundary: Restricts package use to this authorized pass. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7F.6.13 — RM-CR-01 [proposed] fail-closed rule: Stops invalid or unsafe operation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7F.6.14 — A4 eight-field declaration validity: Satisfies the mandatory eight fields. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7F.6.15 — Quiet relevance use and material uncertainty: Uses uncertain connections quietly within declared limits. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: ACCEPTED — C-7F.6.12 — RM-CR-01 [proposed] logging contract: Records evaluation, retrieval and failed attempts distinctly. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F — Context Retrieval (§7F) | Authorized root candidates. | Applies per-channel selection. | Purpose-specific context. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7F.6.8 — RM-CR-01 [proposed] on-demand evaluation timing | Reading-pass request. | Runs on demand. | No precomputed result. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-7F.6.12 — RM-CR-01 [proposed] logging contract | Completed evaluation and attempts. | Records the required identities. | Auditable use. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 4 · ACCEPTED | C-7F.6.13 — RM-CR-01 [proposed] fail-closed rule | Invalidity and failure. | Halts unsafe operation. | No improvised mode. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 5 · ACCEPTED | C-7F.6.15 — Quiet relevance use and material uncertainty | Possible internal connection. | Uses only declared permissions. | Quiet revisable use. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 6 · ACCEPTED | C-7R.16.1 — Retrieval declaration interface | Root candidates and a target reading context under retrieval_context_selection. | Supplies the complete canonical proposed RM-CR-01 declaration and local fields. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: C-7F.6.1 — RM-CR-01 [proposed] declaration identity; C-7F.6.2 — Retrieval-context-selection purpose; C-7F.6.3 — RM-CR-01 [proposed] target; C-7F.6.4 — RM-CR-01 [proposed] candidate roots; C-7F.6.5 — RM-CR-01 [proposed] deterministic context gates; C-7F.6.6 — RM-CR-01 [proposed] graded dimensions; C-7F.6.7 — RM-CR-01 [proposed] mouth authorization; C-7F.6.8 — RM-CR-01 [proposed] on-demand evaluation timing; C-7F.6.9 — RM-CR-01 [proposed] reason; C-7F.6.10 — RM-CR-01 [proposed] Tier 2 rules; C-7F.6.11 — RM-CR-01 [proposed] allowed-use boundary; C-7F.6.12 — RM-CR-01 [proposed] logging contract; C-7F.6.13 — RM-CR-01 [proposed] fail-closed rule; C-7F.6.14 — A4 eight-field declaration validity; C-7F.6.15 — Quiet relevance use and material uncertainty

### C-7F.6.1 — RM-CR-01 [proposed] declaration identity
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Proposed identity RM-CR-01 with declaration_version v1_0; declaration and Tier-1 mode share the identifier at this level. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — This concrete Context Retrieval declaration. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Versions the declaration append-only; later changes require a new version. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — RM-CR-01 [proposed], v1_0. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Silently edit the existing declaration version. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration | RM-CR-01 [proposed] v1_0. | Records the binding. | Versioned declaration. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7F.6.14 — A4 eight-field declaration validity | RM-CR-01 [proposed] v1_0. | Carries the mode binding. | Third mandatory declaration field. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.2 — Retrieval-context-selection purpose
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The settled purpose retrieval_context_selection. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — A reading pass selecting its context. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Assigns this purpose with the optional label selecting context for a reading pass; the label has no behavior. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — A purpose-scoped relevance evaluation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Substitute a different purpose without its valid declaration. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Unknown purposes follow the shared halt-and-propose rule. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration | Reading-context task. | Scopes relevance. | Purpose-specific evaluation. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7F.6.14 — A4 eight-field declaration validity | retrieval_context_selection. | Carries the purpose field. | Second mandatory declaration field. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.3 — RM-CR-01 [proposed] target
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The target root of the requesting reading pass. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — That root and any query representation explicitly declared by its B1 configuration. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Uses the declared target representation for context selection. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — A root-bound retrieval target. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Invent an undeclared query representation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration | Target and declared query. | Binds the target. | Root-specific context. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.4 — RM-CR-01 [proposed] candidate roots
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Only roots authorized for the current internal purpose through either retrieval channel. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Purpose-authorized root candidates. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Keeps root evidence separate from prior-reading context. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — The declaration's authorized root candidate pool. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Include prior readings as candidates of RM-CR-01 [proposed]. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Unauthorized candidates prevent this mode from running. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the declaration receives only prior purpose-authorized roots. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration | Root candidates. | Excludes prior-reading candidate types. | Evidence/context separation. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.5 — RM-CR-01 [proposed] deterministic context gates
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The channel-specific required categorical conditions. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Authorized candidate roots and the mode's optional time-range declaration. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Applies object type on both channels, thread/precedence only on positional context, and time range only when declared. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — Candidates satisfying the applicable deterministic gate set. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Turn channel identity into a gate or dimension, or use mouth-produced gate judgments. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — A failed required gate excludes its candidate. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.6.5.1 — Retrieval object_type_matches gate: Requires root type on both channels. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7F.6.5.2 — Retrieval same_thread_or_group gate: Requires same grouping for positional context. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7F.6.5.3 — Retrieval precedes_target_in_same_thread gate: Requires preceding position for positional context. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7F.6.5.4 — Retrieval within_declared_time_range gate: Applies time range only when declared. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration | Candidate facts. | Checks deterministic gates. | Eligible candidates only. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7F.6.5.1 — Retrieval object_type_matches gate | Candidate type. | Checks root eligibility. | Categorical type exclusion. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-7F.6.5.2 — Retrieval same_thread_or_group gate | Group identities. | Checks shared grouping. | Honest adjacency scope. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 4 · ACCEPTED | C-7F.6.5.3 — Retrieval precedes_target_in_same_thread gate | Positions. | Checks actual order. | Honest predecessor relation. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 5 · ACCEPTED | C-7F.6.5.4 — Retrieval within_declared_time_range gate | Declared range. | Applies it when present. | Conditional temporal exclusion. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: C-7F.6.5.1 — Retrieval object_type_matches gate; C-7F.6.5.2 — Retrieval same_thread_or_group gate; C-7F.6.5.3 — Retrieval precedes_target_in_same_thread gate; C-7F.6.5.4 — Retrieval within_declared_time_range gate

### C-7F.6.5.1 — Retrieval object_type_matches gate
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The root-type condition required on both channels. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — A candidate object's type. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Checks that the candidate is a root. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — The deterministic object-type gate result. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Admit a prior reading as a root candidate. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — A type mismatch excludes the candidate. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.6.5 — RM-CR-01 [proposed] deterministic context gates: Uses the declaration's channel-specific gate set. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.5 — RM-CR-01 [proposed] deterministic context gates | Candidate type. | Applies object_type_matches. | Nonroots excluded. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7D.14.2.5 — State-review deterministic context gates | Candidate object type and a declared time range where present. | Supplies object_type_matches condition. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10] |
| 3 · ACCEPTED | C-7N.13.5 — Action-surfacing deterministic context gate | The candidate's object type and the declared eligible families. | Supplies the shared object_type_matches condition. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7F.6.5.2 — Retrieval same_thread_or_group gate
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The same-group condition required only for positional retrieval. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Candidate and target thread/group membership. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Requires the positional candidate to share the target's recorded grouping. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — A deterministic same-group result. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Require same-thread membership of every semantic candidate. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — A positional grouping mismatch excludes the candidate. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.6.5 — RM-CR-01 [proposed] deterministic context gates: Uses only the positional requirement. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.5 — RM-CR-01 [proposed] deterministic context gates | Thread/group facts. | Applies same_thread_or_group. | Positional scope preserved. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.5.3 — Retrieval precedes_target_in_same_thread gate
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The recorded-precedence condition required only for positional retrieval. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Candidate and target positions in their shared thread. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Requires the candidate to precede the target. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — A deterministic preceding-position result. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Use similarity as proof that a candidate preceded the target. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — A nonpreceding positional candidate is excluded. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.6.5 — RM-CR-01 [proposed] deterministic context gates: Uses only the positional precedence requirement. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.5 — RM-CR-01 [proposed] deterministic context gates | Recorded order. | Applies precedes_target_in_same_thread. | No future turn as predecessor. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.5.4 — Retrieval within_declared_time_range gate
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The temporal condition used only when the B1 mode declares a time range. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — A declared time range and candidate time provenance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Checks the candidate against that declared range; the range value remains open. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — The applicable deterministic temporal gate result. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Impose a time gate when the mode declares no range. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — A candidate failing an applicable time-range gate is excluded. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.6.5 — RM-CR-01 [proposed] deterministic context gates: Uses the optional range requirement. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.5 — RM-CR-01 [proposed] deterministic context gates | Optional range and candidate time. | Checks within_declared_time_range. | No hidden time gate. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7D.14.2.5 — State-review deterministic context gates | Candidate object type and a declared time range where present. | Supplies within_declared_time_range condition. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10] |

SUB-PARTS: NONE

### C-7F.6.6 — RM-CR-01 [proposed] graded dimensions
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Six selected provenance-bearing dimensions with their settled producers. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Gate-eligible root candidates and recorded structural, temporal and similarity information. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Produces the named dimensions separately, preserving producer and rule/model/index/prompt versions as applicable. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — Graded values without a collapsed hidden score. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Make relevance into truth or use an unselected reading/state dimension as a root signal. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Missing or inapplicable values retain honest absence status rather than invented numbers. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-7F.6.6.1 — Retrieval semantic_similarity: Receives semantic-channel similarity. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-7F.6.6.2 — Retrieval positional_distance: Receives positional distance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-7F.6.6.3 — Retrieval temporal_distance: Receives temporal distance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-7F.6.6.4 — Retrieval explicit_links: Receives recorded structural links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-7F.6.6.5 — Retrieval ness_response_links: Receives Ness-response links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-7F.6.6.6 — Retrieval active_clash_links: Receives active clash links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7F.6.6.7 — Root-dimension applicability boundary: Excludes reading/state-only dimensions. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration | Eligible candidates. | Preserves named producer-bearing values. | No hidden score. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: C-7F.6.6.1 — Retrieval semantic_similarity; C-7F.6.6.2 — Retrieval positional_distance; C-7F.6.6.3 — Retrieval temporal_distance; C-7F.6.6.4 — Retrieval explicit_links; C-7F.6.6.5 — Retrieval ness_response_links; C-7F.6.6.6 — Retrieval active_clash_links; C-7F.6.6.7 — Root-dimension applicability boundary

### C-7F.6.6.1 — Retrieval semantic_similarity
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The semantic channel's embedding-produced dimension. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — An eligible semantic candidate and target representation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Uses the settled all-MiniLM-L6-v2 embedding producer for semantic similarity only. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — semantic_similarity with model and index provenance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Treat the similarity value as evidence that a connection is true. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.6 — RM-CR-01 [proposed] graded dimensions | Embedding result. | Carries semantic_similarity. | Provenance-bearing association. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.6.2 — Retrieval positional_distance
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — A deterministic positional-channel dimension. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Candidate and target positions. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Produces their positional distance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — positional_distance with rule-version provenance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Assign a semantic match a fabricated preceding position. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.6 — RM-CR-01 [proposed] graded dimensions | Recorded positions. | Carries positional_distance. | Positional dimension. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.6.3 — Retrieval temporal_distance
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — A deterministic temporal dimension. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Candidate and target time provenance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Produces their temporal distance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — temporal_distance with rule-version provenance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.6 — RM-CR-01 [proposed] graded dimensions | Recorded times. | Carries temporal_distance. | Temporal dimension. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.6.4 — Retrieval explicit_links
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — A deterministic dimension derived only from already-recorded structural links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Same Person-Box, confirmed theme, proposed theme, derived_from chain or shared telling-root links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Uses recorded link structure while preserving each link's evidential status. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — explicit_links with rule provenance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Turn a proposed or confirmed theme into proof or silently accept a new connection. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7F.6.6.4.1 — Retrieval same Person-Box link: Uses an existing shared Person-Box link. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-7F.6.6.4.2 — Retrieval confirmed-theme link: Uses an existing confirmed-theme link. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-7F.6.6.4.3 — Retrieval proposed-theme link: Uses an existing proposed-theme clue. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-7F.6.6.4.4 — Retrieval derived_from-chain link: Uses a recorded derived_from chain. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-7F.6.6.4.5 — Retrieval shared telling-root link: Uses shared telling-root IDs. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.6 — RM-CR-01 [proposed] graded dimensions | Existing link records. | Carries explicit_links. | No invented connection. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: C-7F.6.6.4.1 — Retrieval same Person-Box link; C-7F.6.6.4.2 — Retrieval confirmed-theme link; C-7F.6.6.4.3 — Retrieval proposed-theme link; C-7F.6.6.4.4 — Retrieval derived_from-chain link; C-7F.6.6.4.5 — Retrieval shared telling-root link

### C-7F.6.6.4.1 — Retrieval same Person-Box link
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — An already-recorded shared Person-Box structural link. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Candidate and target Person-Box references. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Supplies that structural relationship to explicit_links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — Shared Person-Box link provenance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Infer an unrecorded identity merge. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.6.4 — Retrieval explicit_links | Person-Box references. | Records structural overlap. | Person-link provenance. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.6.4.2 — Retrieval confirmed-theme link
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — An already-recorded shared confirmed-theme link. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Recorded confirmed-theme references. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Supplies that structural link without treating confirmation as proof of a connection. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — Confirmed-theme provenance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Promote theme membership into truth evidence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.6.4 — Retrieval explicit_links | Theme references. | Retains confirmed status. | Theme provenance without proof. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.6.4.3 — Retrieval proposed-theme link
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — An already-recorded proposed-theme link usable as a weak revisable clue. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Proposed-theme references with their status intact. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Supports internal searching and records the influence in why-admitted provenance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — A labeled weak theme-guided clue. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Silently turn a proposed theme into an accepted structural connection. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.6.4 — Retrieval explicit_links | Proposed links. | Retains weak revisable status. | No silent acceptance. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.6.4.4 — Retrieval derived_from-chain link
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — An already-recorded shared derived_from relationship chain. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Recorded derivation links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Supplies derivational structure to explicit_links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — Derivation-link provenance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Treat derived material as independent evidence for its originating interpretation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.6.4 — Retrieval explicit_links | Derivation references. | Carries structural lineage. | No independent-evidence inflation. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.6.4.5 — Retrieval shared telling-root link
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The already-recorded relationship of shared root IDs in a telling. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Exact root references carried by a telling. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Supplies their structural overlap to explicit_links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — Shared-root link provenance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Replace source roots with a telling's interpretation as direct evidence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.6.4 — Retrieval explicit_links | Root pointers. | Carries exact overlap. | Source-root traceability. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.6.5 — Retrieval ness_response_links
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — A deterministic dimension based on recorded Ness-response links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Existing linked Ness-response records. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Supplies their structural relation with deterministic-rule provenance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — ness_response_links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.6 — RM-CR-01 [proposed] graded dimensions | Response references. | Carries ness_response_links. | Recorded response relation. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.6.6 — Retrieval active_clash_links
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — A deterministic dimension based on active linked clashes. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Existing active clash references. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Carries the clash relationships while keeping clashes surfaced and unresolved. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — active_clash_links. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Resolve a clash through relevance selection. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.6 — RM-CR-01 [proposed] graded dimensions | Clash references. | Carries active_clash_links. | Unresolved clashes visible. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.6.7 — Root-dimension applicability boundary
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The explicit exclusion of three dimensions belonging to reading or state-node candidates. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — The root-only candidate type of RM-CR-01 [proposed]. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Does not select currentness_status, proposal_acceptance_outcome or reading_context_status for these roots. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — An honest dimension selection without relabeling another object type's properties. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Coerce those unselected dimensions into root relevance signals. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Inapplicability remains recorded rather than invented. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.6 — RM-CR-01 [proposed] graded dimensions | Root candidate type. | Preserves applicability. | No coerced values. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.7 — RM-CR-01 [proposed] mouth authorization
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The explicit declaration value none for mouth-produced relevance dimensions. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — The settled deterministic and embedding-produced dimension vocabulary. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Authorizes no mouth-produced relevance dimension in this declaration. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — A present authorization field with value none. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Omit the field, use a broad mouth-allowed flag, let a mouth self-approve, or use a mouth-produced context gate. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Any future authorization requires a new declaration naming the dimension, contexts, Tier-2 unresolved-rule identifier/version and the settled validation boundary. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration | Proposed producer use. | Enforces none. | No undeclared interpretation producer. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.8 — RM-CR-01 [proposed] on-demand evaluation timing
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Context selection requested at the reading pass's context-assembly stage through LMAC. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — An on-demand request from the reading pass. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Evaluates at RR-equivalent context-assembly time; declares no triggered pre-computation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — An on-demand context evaluation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Invent precompute triggers or invalidating events for v1_0. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Later pre-computation requires a new version with explicit triggers and invalidators. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration: Obeys this version's timing declaration. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration | Reading-pass request. | Evaluates at assembly time. | No undeclared precompute. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.9 — RM-CR-01 [proposed] reason
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The recorded reason for selecting context through this mode. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — The reading pass's need to see both its surroundings and potentially related material. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Supplies permitted wide context so the pass is not blind while preserving the different kinds of claim. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — A declared reason tied to the Universal Filter's wide-context rule. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Merge the evidential claims to satisfy the context requirement. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — A declaration without its required reason is invalid. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration | Task rationale. | Records why the mode fits. | Valid declared rationale. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7F.6.14 — A4 eight-field declaration validity | Wide-context rationale. | Carries the reason field. | Fourth mandatory declaration field. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.10 — RM-CR-01 [proposed] Tier 2 rules
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The consumer-owned ordering, fallback, surfacing, uncertainty and strictness rules. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Gate/dimension results and B1 settings for this Context Retrieval use. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Applies the concrete consumer rules without taking ownership of the shared Tier-1 contract. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — A bounded context package carrying status and provenance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Silently take over the other tier's validation or ownership. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — The declared failure paths apply when safe evaluation cannot complete. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-7F.6.10.2 — Retrieval theme and pattern influence: Admits permitted weak theme clues with labels. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7F.6.10.1 — RM-CR-01 [proposed] channel-specific ordering: Orders each channel separately. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7F.6.10.3 — RM-CR-01 [proposed] fallback: Separates empty fallback from failure stop. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7F.6.10.4 — RM-CR-01 [proposed] surfacing boundary: Carries labels without direct surfacing. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling: Uses the explicit unresolved rule. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration | Relevance output. | Orders and handles uncertainty/fallback. | Bounded honest context. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7F.6.10.1 — RM-CR-01 [proposed] channel-specific ordering | Per-channel results. | Applies bounded ordering. | Separate ranked channels. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-7F.6.10.2 — Retrieval theme and pattern influence | Theme or pattern clue. | Keeps it weak and logged. | No connection acceptance. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 4 · ACCEPTED | C-7F.6.10.4 — RM-CR-01 [proposed] surfacing boundary | Labeled context. | Passes it internally. | Output ownership remains downstream. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: C-7F.6.10.1 — RM-CR-01 [proposed] channel-specific ordering; C-7F.6.10.2 — Retrieval theme and pattern influence; C-7F.6.10.3 — RM-CR-01 [proposed] fallback; C-7F.6.10.4 — RM-CR-01 [proposed] surfacing boundary; C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling

### C-7F.6.10.1 — RM-CR-01 [proposed] channel-specific ordering
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Separate positional and similarity-based ordering under the mode's declared rule reference. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Each channel's eligible candidates and ranking_or_threshold_rule [proposed]. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Orders positional material by position and semantic material by similarity, with effective quantities bounded by the lower of settings and ceilings. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — Two independently ordered, bounded channel outputs. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Jointly rank channels or silently lower a threshold. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Invalid settings or ceiling violations prevent the mode from running. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.6.10 — RM-CR-01 [proposed] Tier 2 rules: Uses the owning Tier-2 ordering rule. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.10 — RM-CR-01 [proposed] Tier 2 rules | Eligible channel candidates. | Applies its declared ordering rule. | No joint ranking. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.10.2 — Retrieval theme and pattern influence
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Automatic internal searching guided by possible patterns and revisable meaning-connections. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Recorded proposed-theme links or semantic search clues and the mode's permitted use settings. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Uses uncertain or below-threshold matches only where configuration allows, always labeled maybe related, weak echo, one similar old memory or older pattern, and logs every influence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — Weak labeled clues for searching and understanding without a per-judgment approval requirement. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Treat a clue as proof, causation, authority, current-state evidence, access permission or an accepted connection. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Configuration cannot be bypassed by a theme; uncertainty that materially changes a visible result must be disclosed by its owning surface. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.6.10 — RM-CR-01 [proposed] Tier 2 rules: Uses only configuration-permitted influence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: ACCEPTED — C-7F.4.6.2 — Supplied-item admission reason: Records every influence in item admission provenance. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.10 — RM-CR-01 [proposed] Tier 2 rules | Possible connections. | Guides search and logs influence. | Revisable context selection. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.10.3 — RM-CR-01 [proposed] fallback
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The retrieval declaration's distinct healthy-empty and technical-failure paths. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — The actual empty or failed retrieval outcome. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Proceeds bare and marked for genuine emptiness; for technical failure uses bounded B9 retry by reference and then stops safely while preserving work. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — A context-limited/revisable reading opportunity or an honest terminal failure. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Continue degraded after exhausted technical retry without a separately authorized rule. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Exhausted retry stops, records its reason and terminal state, and preserves unfinished work for the real-change exception. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7F.7.1 — Genuine empty-result handling: Uses bare fallback only for healthy emptiness. [V10 §7F] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7F.7.3 — Accepted B26 stop-after-retry policy: Uses accepted stop-after-retry for failure. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.10 — RM-CR-01 [proposed] Tier 2 rules | Retrieval outcome. | Uses the permitted path. | Honest context status. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.10.4 — RM-CR-01 [proposed] surfacing boundary
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Retrieval's absence of a direct visible-output role. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Supplied items with their channel, strength and status labels. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Carries those labels downstream so the receiving surface can apply its own rules. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — Labeled internal context, with no direct retrieval narration. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Talk directly to the user or treat internal retrieval permission as visible-output permission. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Downstream surfacing remains subject to its separate output gates. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.6.10 — RM-CR-01 [proposed] Tier 2 rules: Obeys the declaration's no-direct-surfacing rule. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.10 — RM-CR-01 [proposed] Tier 2 rules | Internal context package. | Passes provenance downstream. | No direct narration. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The proposed shared unresolved-dimension handling rule T2-UNRES-SHARED v1_0, consumed by RM-CR-01. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — A dimension's validation state, producer/validator agreement and applicability. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Distinguishes validated interpretation, failed values, weak unresolved clues and honest absence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — Labeled and logged values with explicit limits on use. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Choose the result with greater model confidence or equate validation with substantive truth. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Disagreements outside declared handling take the honest fail-closed path. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-7F.6.10.5.1 — Validated relevance value: Handles validated values as interpretation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Fed by: ACCEPTED — C-7F.6.10.5.3 — Unresolved relevance clue: Handles unresolved clues within limits. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Gated by: ACCEPTED — C-7F.6.10.5.2 — Failed relevance value: Excludes failed values. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Gated by: ACCEPTED — C-7F.6.10.5.5 — Honest dimension absence: Keeps missing values honest. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Changes: ACCEPTED — C-7F.6.10.5.4 — Relevance disagreement record handoff: Records actual disagreements. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.10 — RM-CR-01 [proposed] Tier 2 rules | Validation state. | Preserves status-specific use limits. | No hidden certainty. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7F.6.10.5.2 — Failed relevance value | Failed value. | Excludes relevance use. | Honest failure. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| 3 · ACCEPTED | C-7F.6.10.5.3 — Unresolved relevance clue | Weak clue. | Restricts consequential use. | No promoted certainty. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| 4 · ACCEPTED | C-7F.6.10.5.4 — Relevance disagreement record handoff | Disputed result. | Records and handles uncertainty. | No silent model winner. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| 5 · ACCEPTED | C-7F.6.10.5.5 — Honest dimension absence | Unavailable input. | Records absence state. | No fabricated signal. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| 6 · ACCEPTED | C-7F.6.14 — A4 eight-field declaration validity | T2-UNRES-SHARED [proposed] v1_0. | Declares unresolved handling. | Fifth mandatory declaration field. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 7 · ACCEPTED | C-7H.11.9 — Reread relevance use and uncertainty | The evaluation's dimensions and uncertainty state. | Gates this place: reuses T2-UNRES-SHARED [proposed] with reread-specific consequences. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §9] |
| 8 · ACCEPTED | C-7R.16.6 — Shared uncertainty-rule consumer interface | The actual validation or absence outcome and consumer’s permitted use. | Supplies the existing shared handling owner. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| 9 · ACCEPTED | C-7N.13.10.4 — Action-surfacing proposed shared unresolved handling | Validated, failed, unresolved, disagreement or honestly absent dimension values. | Supplies the existing proposed T2-UNRES-SHARED handling and its atomic outcomes. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] |
| 10 · ACCEPTED | C-7D.14.2.10 — State-review Tier 2 consequences | The selected relevance results and their actual validation/uncertainty state. | Supplies proposed T2-UNRES-SHARED v1_0 handling; validated, failed, unresolved, disagreement and honest-absence cases retain their existing owners. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5] |

SUB-PARTS: C-7F.6.10.5.1 — Validated relevance value; C-7F.6.10.5.2 — Failed relevance value; C-7F.6.10.5.3 — Unresolved relevance clue; C-7F.6.10.5.4 — Relevance disagreement record handoff; C-7F.6.10.5.5 — Honest dimension absence

### C-7F.6.10.5.1 — Validated relevance value
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]

ALONE
- What it is: ACCEPTED — A value with no rule-detectable error found. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Takes in: ACCEPTED — The validated outcome under the settled validation rule. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Does: ACCEPTED — Permits use according to the declaration while retaining interpretive status. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Gives out: ACCEPTED — A usable interpretation, not a fact certificate. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Must never: ACCEPTED — Treat validated as substantively correct. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling | Validated result. | Permits declared use. | No fact certificate. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| 2 · ACCEPTED | C-7M.10.9.4 — Computed View proposed shared unresolved handling | Validated, failed, unresolved, disputed or absent dimension outcomes and their recorded provenance. | Supplies validated interpretation. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-7R.16.6 — Shared uncertainty-rule consumer interface | The actual validation or absence outcome and consumer’s permitted use. | Supplies the validated outcome: use is permitted according to the declaration, with interpretive status retained. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |

SUB-PARTS: NONE

### C-7F.6.10.5.2 — Failed relevance value
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]

ALONE
- What it is: ACCEPTED — A dimension value with failed validation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Takes in: ACCEPTED — The failed validation outcome. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Does: ACCEPTED — Excludes the value from relevance-result use. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Gives out: ACCEPTED — No usable relevance result from that value. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Must never: ACCEPTED — Use the failed value as a relevance result. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Fails closed by: ACCEPTED — The failed value is not used. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling: Follows the shared failed-state prohibition. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling | Failed validation. | Prevents use. | No failed relevance signal. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| 2 · ACCEPTED | C-7R.16.6 — Shared uncertainty-rule consumer interface | The actual validation or absence outcome and consumer’s permitted use. | Supplies the failed outcome: the value is excluded from relevance-result use. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| 3 · ACCEPTED | C-7M.10.9.4 — Computed View proposed shared unresolved handling | Validated, failed, unresolved, disputed or absent dimension outcomes and their recorded provenance. | Supplies unused failed result. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7F.6.10.5.3 — Unresolved relevance clue
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]

ALONE
- What it is: ACCEPTED — An unresolved or disputed value that may remain a weak internal clue where declared handling permits. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Takes in: ACCEPTED — An unresolved outcome or producer/validator disagreement. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Does: ACCEPTED — Keeps the value labeled and logged for further searching, checking or evaluation only within the declaration's permissions. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Gives out: ACCEPTED — A revisable clue with no independent consequential authority. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Must never: ACCEPTED — By itself support a factual claim, satisfy current-situation support, change Living State, cause an actual reread, authorize an active suggestion, widen access or grant authority. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Fails closed by: ACCEPTED — A material effect on a visible result requires explicit uncertainty disclosure under the owning surface's rules. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling: Follows the unresolved-state use limits. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling | Unresolved result. | Permits weak internal evaluation only. | No consequential authority. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| 2 · ACCEPTED | C-7M.10.9.4 — Computed View proposed shared unresolved handling | Validated, failed, unresolved, disputed or absent dimension outcomes and their recorded provenance. | Supplies weak unresolved clue. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-7R.16.6 — Shared uncertainty-rule consumer interface | The actual validation or absence outcome and consumer’s permitted use. | Supplies unresolved clue. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |

SUB-PARTS: NONE

### C-7F.6.10.5.4 — Relevance disagreement record handoff
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]

ALONE
- What it is: ACCEPTED — The connection from a producer/validator disagreement to the settled separate disagreement record. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Takes in: ACCEPTED — The actual disagreement and the declared uncertainty rule. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Does: ACCEPTED — Records the disagreement once and uses declared handling without choosing by confidence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Gives out: ACCEPTED — An append-only disagreement record and an honest uncertainty outcome. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Must never: ACCEPTED — Silently select whichever model is more confident. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]
- Fails closed by: ACCEPTED — If declared rules cannot resolve safe use, the owning component follows its fail-closed path. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling: Uses declared disagreement handling. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Changes: DESIGNED — C-7R — Attention & Relevance Control (§7R): Uses the shared disagreement-record owner. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling | Producer/validator disagreement. | Preserves a linked record. | No confidence-based selection. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| 2 · ACCEPTED | C-7M.10.9.4 — Computed View proposed shared unresolved handling | Validated, failed, unresolved, disputed or absent dimension outcomes and their recorded provenance. | Supplies disagreement handoff. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 3 · ACCEPTED | C-7R.16.6 — Shared uncertainty-rule consumer interface | The actual validation or absence outcome and consumer’s permitted use. | Records the disagreement once and uses declared handling without choosing by confidence. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |

SUB-PARTS: NONE

### C-7F.6.10.5.5 — Honest dimension absence
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]

ALONE
- What it is: ACCEPTED — Explicit absence when a dimension is inapplicable or its input cannot be produced. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Takes in: ACCEPTED — Missing input or a candidate type to which the dimension does not apply. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Does: ACCEPTED — Records the appropriate settled absence vocabulary, including not_applicable, not_evaluated or collection_failed. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Gives out: ACCEPTED — Honest absence rather than a fabricated value or silent blank. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Must never: ACCEPTED — Convert missing or inapplicable input into a relevance signal. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Fails closed by: ACCEPTED — The absent value is not invented. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling: Uses honest absence instead of coercion. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling | Missing or inapplicable input. | Records absence vocabulary. | No invented dimension. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| 2 · ACCEPTED | C-7R.16.6 — Shared uncertainty-rule consumer interface | The actual validation or absence outcome and consumer’s permitted use. | Supplies honest not_applicable / not_evaluated / collection_failed absence. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] |
| 3 · ACCEPTED | C-7M.10.9.4 — Computed View proposed shared unresolved handling | Validated, failed, unresolved, disputed or absent dimension outcomes and their recorded provenance. | Supplies what this place relies on: honest absence. These existing atoms are reused under the proposed shared rule, without changing their canonical names. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |
| 4 · ACCEPTED | C-7M.10.5 — Computed View graded-dimension selection | Eligible candidates, the current target and each dimension's actual inputs. | Gates this place: the existing honest-absence outcome contract is reused under the proposed shared uncertainty rule. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7F.6.11 — RM-CR-01 [proposed] allowed-use boundary
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — Root context confined to the current purpose, prior authorization and the requesting reading pass. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Already-authorized roots within eligible_source_scope [proposed]. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Narrows candidate use without widening access, merging channels or exporting the package to another purpose. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — Context for the requesting pass only. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Reveal withheld material, signal its existence, or treat retrieval presence as proof of truth or connection. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Privacy and deletion eligibility remain prerequisites outside relevance ownership. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): Receives only prior-authorized roots. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration | Authorized source scope. | Narrows use. | No purpose expansion. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7F.6.14 — A4 eight-field declaration validity | Current purpose and source scope. | Narrows allowed use. | Sixth mandatory declaration field. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.12 — RM-CR-01 [proposed] logging contract
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The distinct records of relevance evaluation, retrieval execution and failure attempts. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — One completed relevance evaluation, its retrieval run and any failure attempts. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Writes one settled relevance event per evaluation plus one B1 audit per run; records failures under B26 bound to the same operation identity. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — Linked append-only records including declaration identity/version, exact supplied roots and theme influence. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Count these different record roles as independent truth evidence or duplicate a real operation's log. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Record access obeys privacy and applicable identity/security authorization. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration: Implements the declaration's logging requirement. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: ACCEPTED — C-7F.4 — B1 retrieval audit record: Leaves the distinct retrieval-run audit. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: DESIGNED — C-7R — Attention & Relevance Control (§7R): Leaves the distinct relevance event. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration | Actual operations. | Leaves the required records. | Full audit continuity. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7F.6.14 — A4 eight-field declaration validity | Evaluation/run records. | Requires the declared logging. | Seventh mandatory declaration field. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.13 — RM-CR-01 [proposed] fail-closed rule
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The concrete declaration's invalidity and unsafe-evaluation boundary. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Missing or invalid declarations/configuration, ceiling violation, unauthorized candidates, unknown purpose or retrieval failure. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Prevents invalid modes from running; unknown purpose halts, preserves the request, identifies the value and vocabulary version, and offers mapping or a new-type proposal without guessing. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — A recorded honest halt or the separately permitted genuine-empty result. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Guess silently, lower thresholds, substitute unrelated material, merge channels or claim success on failure. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — System failure follows bounded retry then safe stop, with no unauthorized degraded continuation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration: Enforces the owning declaration. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7F.7.3 — Accepted B26 stop-after-retry policy: Uses failure stop after bounded retry. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration | Invalidity or failure. | Applies honest closure. | No silent guess. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7F.6.14 — A4 eight-field declaration validity | Unsafe or invalid evaluation. | Prevents invented success. | Eighth mandatory declaration field. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-7F.6.14 — A4 eight-field declaration validity
Stamp: ACCEPTED    Source: [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The required structure satisfied by the concrete retrieval declaration. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — Component/version, task/purpose, selected mode/version, reason, uncertainty behavior, allowed-use boundary, logging/audit and fail-closed behavior. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Requires all eight fields; Tier 1 is owned and validated by Attention and Relevance Control and Tier 2 by the consuming component. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — A valid purpose-specific declaration or no mode to run. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Invent a private relevance meaning or omit reason or uncertainty handling. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — A missing required field makes the declaration invalid. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: ACCEPTED — C-7F.3.3 — B1 consuming_component [proposed]: Identifies the consuming component as Context Retrieval. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-7F.6.2 — Retrieval-context-selection purpose: Declares the task's controlled purpose. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-7F.6.1 — RM-CR-01 [proposed] declaration identity: Selects the exact mode and version. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-7F.6.9 — RM-CR-01 [proposed] reason: States why the selected mode fits the task. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: DESIGNED — C-7R — Attention & Relevance Control (§7R): Binds the shared two-tier validity contract. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1]
- Gated by: ACCEPTED — C-7F.6.10.5 — T2-UNRES-SHARED [proposed] retrieval handling: Carries explicit uncertainty behavior. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7F.6.11 — RM-CR-01 [proposed] allowed-use boundary: Carries authorized-use limits. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gated by: ACCEPTED — C-7F.6.13 — RM-CR-01 [proposed] fail-closed rule: Carries honest invalidity and failure behavior. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: ACCEPTED — C-7F.6.12 — RM-CR-01 [proposed] logging contract: Carries explicit audit requirements. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3.4 — B1 a4_declaration_ref [proposed] | Purpose-specific declaration. | Checks all required meaning fields. | No declaration, no mode. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5] [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] |
| 2 · ACCEPTED | C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration | Full declaration. | Validates completeness. | No missing-field mode. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 3 · ACCEPTED | C-7D.14.2 — Proposed RM-LS-01 state-review declaration | A tracked state node's currentness question and authorized new/changed source items referenced by identity. | Gates this place: the eight required declaration fields must be valid before evaluation. C-7D.14.2.5 — State-review deterministic context gates: object_type_matches always applies, with within_declared_time_range only when declared. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §10] |
| 4 · ACCEPTED | C-7N.13 — Proposed RM-AS-01 action-surfacing declaration | The candidate possibility, permitted support and the action_surfacing purpose. | Gates this place: all eight declaration fields, including reason and uncertainty behavior, must be present. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] |
| 5 · ACCEPTED | C-7N.13.13.1 — Action-surfacing missing-or-invalid declaration failure | A missing or invalid proposed mode declaration. | Supplies the declaration-validity result establishes the missing/invalid-declaration failure. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] |
| 6 · ACCEPTED | C-7M.10 — Computed View proposed RM-CV-01 declaration | The current view profile and question, authorized eligible candidates, deterministic gates and declared dimension results with producer/version provenance. | Gates this place: the existing eight-field validity contract applies before this consumer has a mode to run. | Nothing in this card. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |

SUB-PARTS: NONE

### C-7F.6.15 — Quiet relevance use and material uncertainty
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — Automatic, recorded use of possible connections for internal search, understanding and response preparation. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4]
- Takes in: ACCEPTED — An uncertain connection and its effect on the contemplated use. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4]
- Does: ACCEPTED — Uses permitted internal clues quietly; records gaps and reveals uncertainty when it materially changes a visible claim, interpretation, recommendation, withholding decision, possibility or conclusion. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4]
- Gives out: ACCEPTED — Revisable internal assistance and honestly qualified visible effects. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4]
- Must never: ACCEPTED — Make every internal connection an approval task, turn the Log into an approval queue, or promote uncertainty into proof or authority. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Fail-closed halts affect the operation without turning missing machinery into mandatory manual work. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration: Stays inside the retrieval declaration. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6 — RM-CR-01 [proposed] retrieval relevance declaration | Possible connection. | Records and qualifies material visible effects. | No approval queue. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7N.13 — Proposed RM-AS-01 action-surfacing declaration | The candidate possibility, permitted support and the action_surfacing purpose. | Supplies quiet relevance use and material uncertainty. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §4] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-7F.7 — Retrieval outcome separation
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — The distinction between no relevant context and failure to retrieve correctly. [V10 §7F]
- Takes in: DESIGNED — The real result of a retrieval attempt. [V10 §7F]
- Does: DESIGNED — Allows target-only continuation for healthy emptiness while retaining system failure as a different outcome. [V10 §7F]
- Gives out: DESIGNED — Honest context availability and execution status. [V10 §7F]
- Must never: DESIGNED — Invent context, silently lower thresholds or substitute unrelated memories. [V10 §7F]
- Fails closed by: DESIGNED — A system failure is never reported as successful retrieval. [V10 §7F]

TOGETHER
- Fed by: DESIGNED — C-7F.7.1 — Genuine empty-result handling: Recognizes healthy emptiness. [V10 §7F]
- Fed by: DESIGNED — C-7F.7.2 — Retrieval system-failure classes: Recognizes execution failure. [V10 §7F]
- Gated by: ACCEPTED — C-7F.7.3 — Accepted B26 stop-after-retry policy: Carries the accepted failure policy separately from V10's open mechanics. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F — Context Retrieval (§7F) | Actual outcome. | Preserves honest status. | No false success. | [V10 §7F] |
| 2 · ACCEPTED | C-7F.4.8 — Retrieval empty-versus-failure marker | Run outcome. | Separates absence from failure. | Honest audit status. | [V10 §7F] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |
| 3 · DESIGNED | C-7F.7.1 — Genuine empty-result handling | Genuine absence. | Distinguishes it from failure. | Honest bare fallback. | [V10 §7F] |
| 4 · ACCEPTED | C-7F.7.3 — Accepted B26 stop-after-retry policy | Technical failure. | Prevents empty fallback. | Honest failed retrieval. | [V10 §7F] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] |

SUB-PARTS: C-7F.7.1 — Genuine empty-result handling; C-7F.7.2 — Retrieval system-failure classes; C-7F.7.3 — Accepted B26 stop-after-retry policy

### C-7F.7.1 — Genuine empty-result handling
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — Normal absence of relevant context, such as the first root in a thread or no semantic result above threshold. [V10 §7F]
- Takes in: DESIGNED — A healthy retrieval returning no relevant material. [V10 §7F]
- Does: DESIGNED — Proceeds with the target root only and records the empty channel, reason, bare fallback and context-limited/revisable status. [V10 §7F]
- Gives out: DESIGNED — A marked target-only reading opportunity. [V10 §7F]
- Must never: DESIGNED — Treat healthy emptiness as a system failure or manufacture replacement context. [V10 §7F]
- Fails closed by: DESIGNED — No unrelated memory or silently lowered threshold may fill the empty channel. [V10 §7F]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7F.7 — Retrieval outcome separation: Requires a healthy empty result. [V10 §7F]
- Changes: DESIGNED — C-7F.7.1.1 — Empty-channel identity: Records which channel was empty. [V10 §7F]
- Changes: DESIGNED — C-7F.7.1.2 — Empty-context reason: Records why context was absent. [V10 §7F]
- Changes: DESIGNED — C-7F.7.1.3 — Recorded bare fallback: Records bare fallback use. [V10 §7F]
- Changes: DESIGNED — C-7F.7.1.4 — Context-limited and revisable marking: Marks limitation and revisability. [V10 §7F]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.3.12 — B1 insufficient_context_fallback_behavior [proposed] | Genuine absence. | Proceeds bare and marked. | Honest limited context. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §2] |
| 2 · ACCEPTED | C-7F.6.10.3 — RM-CR-01 [proposed] fallback | Genuine no-context result. | Marks limitation and revisability. | Honest target-only use. | [V10 §7F] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 3 · DESIGNED | C-7F.7 — Retrieval outcome separation | No relevant context. | Allows marked bare continuation. | Normal context limitation. | [V10 §7F] |
| 4 · ACCEPTED | C-7N.13.10.2 — Action-surfacing weak-support and retrieval fallback | Support limitations, genuine empty retrieval or actual retrieval-system failure. | Supplies genuine empty-result handling permits bare context-limited/revisable continuation. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] |

SUB-PARTS: C-7F.7.1.1 — Empty-channel identity; C-7F.7.1.2 — Empty-context reason; C-7F.7.1.3 — Recorded bare fallback; C-7F.7.1.4 — Context-limited and revisable marking

### C-7F.7.1.1 — Empty-channel identity
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — Which retrieval channel returned no relevant material. [V10 §7F]
- Takes in: DESIGNED — The empty channel's actual identity. [V10 §7F]
- Does: DESIGNED — Records the positional or semantic absence distinctly. [V10 §7F]
- Gives out: DESIGNED — Channel-specific empty-result provenance. [V10 §7F]
- Must never: DESIGNED — Merge the two channels' outcomes. [V10 §7F]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.7.1 — Genuine empty-result handling | Channel identity. | Preserves it. | Specific empty provenance. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.7.1.2 — Empty-context reason
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — Why the healthy retrieval returned no relevant context. [V10 §7F]
- Takes in: DESIGNED — The actual reason, such as first-in-thread or no above-threshold match. [V10 §7F]
- Does: DESIGNED — Records that reason in the reading trail. [V10 §7F]
- Gives out: DESIGNED — An honest explanation of absence. [V10 §7F]
- Must never: DESIGNED — Invent a reason when retrieval actually failed. [V10 §7F]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.7.1 — Genuine empty-result handling | Actual reason. | Preserves the reason. | Honest absence explanation. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.7.1.3 — Recorded bare fallback
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — The explicit record that target-only fallback was used. [V10 §7F]
- Takes in: DESIGNED — A genuine empty result and bare continuation. [V10 §7F]
- Does: DESIGNED — Records the fallback actually taken. [V10 §7F]
- Gives out: DESIGNED — Visible bare-fallback provenance in the reading record. [V10 §7F]
- Must never: DESIGNED — Hide the lack of contextual input. [V10 §7F]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.7.1 — Genuine empty-result handling | Actual target-only continuation. | Marks the fallback. | No hidden input gap. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.7.1.4 — Context-limited and revisable marking
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — The status carried by a reading made after genuine empty retrieval. [V10 §7F]
- Takes in: DESIGNED — The reading's actual context limitation. [V10 §7F]
- Does: DESIGNED — Marks it context-limited and revisable. [V10 §7F]
- Gives out: DESIGNED — An honest limit on interpretation. [V10 §7F]
- Must never: DESIGNED — Present the reading as if missing context had been supplied. [V10 §7F]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.7.1 — Genuine empty-result handling | Missing relevant context. | Qualifies the reading. | No false context sufficiency. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.7.2 — Retrieval system-failure classes
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — Index error, stale/incomplete index, timeout and unreachable service. [V10 §7F]
- Takes in: DESIGNED — Evidence that retrieval could not execute correctly. [V10 §7F]
- Does: DESIGNED — Distinguishes these execution failures from a healthy empty result. [V10 §7F]
- Gives out: DESIGNED — Honest failure status. [V10 §7F]
- Must never: DESIGNED — Claim retrieval succeeded when it failed. [V10 §7F]
- Fails closed by: DESIGNED — Exact fallback mechanics remain undesigned in V10 itself. [V10 §7F]

TOGETHER
- Fed by: DESIGNED — C-7F.7.2.1 — Retrieval index error: Includes index errors. [V10 §7F]
- Fed by: DESIGNED — C-7F.7.2.2 — Stale or incomplete retrieval index: Includes stale/incomplete index conditions. [V10 §7F]
- Fed by: DESIGNED — C-7F.7.2.3 — Retrieval timeout: Includes timeouts. [V10 §7F]
- Fed by: DESIGNED — C-7F.7.2.4 — Unreachable retrieval service: Includes unreachable services. [V10 §7F]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.7 — Retrieval outcome separation | Index/service/timing failure. | Keeps failure distinct. | No pretend success. | [V10 §7F] |
| 2 · ACCEPTED | C-7N.13.10.2 — Action-surfacing weak-support and retrieval fallback | Support limitations, genuine empty retrieval or actual retrieval-system failure. | Supplies retrieval system-failure classes and their governed terminal handling. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §8] |

SUB-PARTS: C-7F.7.2.1 — Retrieval index error; C-7F.7.2.2 — Stale or incomplete retrieval index; C-7F.7.2.3 — Retrieval timeout; C-7F.7.2.4 — Unreachable retrieval service

### C-7F.7.2.1 — Retrieval index error
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — A failure in the retrieval index. [V10 §7F]
- Takes in: DESIGNED — An index error during retrieval. [V10 §7F]
- Does: DESIGNED — Classifies it as a system failure. [V10 §7F]
- Gives out: DESIGNED — Index-failure status. [V10 §7F]
- Must never: DESIGNED — Relabel it a healthy no-match result. [V10 §7F]
- Fails closed by: DESIGNED — Retrieval success cannot be claimed. [V10 §7F]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.7.2 — Retrieval system-failure classes | Index fault. | Classifies failure. | No false empty result. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.7.2.2 — Stale or incomplete retrieval index
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — An index that cannot truthfully support complete current retrieval. [V10 §7F]
- Takes in: DESIGNED — Staleness or incompleteness of the queried index. [V10 §7F]
- Does: DESIGNED — Treats that condition as system failure rather than proof no relevant material exists. [V10 §7F]
- Gives out: DESIGNED — An honest index-quality failure. [V10 §7F]
- Must never: DESIGNED — Infer genuine emptiness from an incomplete or stale index. [V10 §7F]
- Fails closed by: DESIGNED — Retrieval success cannot be claimed. [V10 §7F]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.7.2 — Retrieval system-failure classes | Index-quality fault. | Classifies failure. | No false completeness. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.7.2.3 — Retrieval timeout
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — Retrieval failing to complete within its applicable timeout. [V10 §7F]
- Takes in: DESIGNED — The timed-out attempt. [V10 §7F]
- Does: DESIGNED — Classifies the timeout as a system failure. [V10 §7F]
- Gives out: DESIGNED — Timeout status; the exact timeout value remains open. [V10 §7F]
- Must never: DESIGNED — Pretend a timeout was successful empty retrieval. [V10 §7F]
- Fails closed by: DESIGNED — Retrieval success cannot be claimed. [V10 §7F]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.7.2 — Retrieval system-failure classes | Timed-out retrieval. | Classifies failure. | Honest timeout. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.7.2.4 — Unreachable retrieval service
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — A retrieval service that cannot be reached. [V10 §7F]
- Takes in: DESIGNED — An unreachable-service condition. [V10 §7F]
- Does: DESIGNED — Preserves it as system failure. [V10 §7F]
- Gives out: DESIGNED — Service-failure status. [V10 §7F]
- Must never: DESIGNED — Substitute unrelated context to conceal the outage. [V10 §7F]
- Fails closed by: DESIGNED — Retrieval success cannot be claimed. [V10 §7F]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.7.2 — Retrieval system-failure classes | Reachability failure. | Classifies failure. | Honest outage. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.7.3 — Accepted B26 stop-after-retry policy
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — The retrieval failure policy repeated in the permitted accepted formal-declarations source. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Takes in: ACCEPTED — A technical system failure and the accepted B9 retry mechanics and values by reference. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Does: ACCEPTED — Uses bounded retry; after failure exhaustion commits terminal failure, records the reason, retains the record and saves unfinished state for the real-change exception. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Gives out: ACCEPTED — A safely stopped failed retrieval with preserved work. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Must never: ACCEPTED — Continue with degraded context after exhausted retry absent a separate later authorized rule. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Fails closed by: ACCEPTED — Stops without pretending success or substituting unrelated material; operational B9/B26 integration remains open. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7F.7 — Retrieval outcome separation: Preserves the governing empty/failure distinction. [V10 §7F] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7]
- Gated by: DESIGNED — C-7H — Reread Lifecycle (§7H): Consumes the shared B9 retry owner rather than inventing retrieval-specific budgets. [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7F.6.10.3 — RM-CR-01 [proposed] fallback | Technical failure. | Preserves work and stops on exhaustion. | No unauthorized degradation. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| 2 · ACCEPTED | C-7F.6.13 — RM-CR-01 [proposed] fail-closed rule | Technical failure. | Retains terminal state and work. | Honest failure closure. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] |
| 3 · DESIGNED | C-7F.7 — Retrieval outcome separation | Failed retrieval. | Retries boundedly then stops. | Preserved failed work. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] |
| 4 · ACCEPTED | C-7H.5.11 — B10 recovery 11 — Retrieval failure | The actual retrieval failure. | Gates this place: accepted retrieval policy governs bounded retry then stop. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md §7] |
| 5 · ACCEPTED | C-7R.15.8.1 — Retrieval-system failure boundary | A retrieval-system failure, bounded B9 attempts and the terminal outcome. | Supplies canonical B26 stop-after-retry policy. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] |

SUB-PARTS: NONE

### C-7F.8 — Retrieval empirical-value discipline
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — The requirement to test each mode's parameters before locking defaults. [V10 §7F]
- Takes in: DESIGNED — Candidate limits, thresholds, ranking rules, budgets, eligible scope and time ranges evaluated against gold material. [V10 §7F]
- Does: DESIGNED — Examines reading quality, relevant retrieval, irrelevant intrusion, channel confusion, reproducibility, latency, cost and sensitivity to changed limits. [V10 §7F]
- Gives out: DESIGNED — Evidence for later per-mode settings; no universal constant is inferred from the built Engine B experiment. [V10 §7F]
- Must never: DESIGNED — Lock defaults without empirical testing or promote n=3 to a universal future limit. [V10 §7F]
- Fails closed by: DESIGNED — Every retrieval remains bounded under hard safety ceilings even while exact values remain open. [V10 §7F]

TOGETHER
- Fed by: DESIGNED — C-7F.8.1 — Retrieval reading-quality test: Requires reading-quality evidence. [V10 §7F]
- Fed by: DESIGNED — C-7F.8.2 — Relevant-context retrieval test: Requires relevant-context evidence. [V10 §7F]
- Fed by: DESIGNED — C-7F.8.3 — Irrelevant-context intrusion test: Requires irrelevant-intrusion evidence. [V10 §7F]
- Fed by: DESIGNED — C-7F.8.4 — Semantic-versus-direct-context test: Requires channel-confusion evidence. [V10 §7F]
- Fed by: DESIGNED — C-7F.8.5 — Retrieval reproducibility test: Requires reproducibility evidence. [V10 §7F]
- Fed by: DESIGNED — C-7F.8.6 — Retrieval latency test: Requires latency evidence. [V10 §7F]
- Fed by: DESIGNED — C-7F.8.7 — Retrieval cost test: Requires cost evidence. [V10 §7F]
- Fed by: DESIGNED — C-7F.8.8 — Retrieval limit-sensitivity test: Requires limit-sensitivity evidence. [V10 §7F]
- Gated by: DESIGNED — C-7F — Context Retrieval (§7F): Keeps empirical selection within the governing retrieval boundary. [V10 §7F]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F — Context Retrieval (§7F) | Candidate settings. | Requires the full test dimensions. | No invented universal values. | [V10 §7F] |
| 2 · DESIGNED | C-7F.8.1 — Retrieval reading-quality test | Candidate settings. | Tests reading quality. | No quality-free default lock. | [V10 §7F] |
| 3 · DESIGNED | C-7F.8.2 — Relevant-context retrieval test | Candidate settings. | Tests relevant context retrieval. | No untested coverage assumption. | [V10 §7F] |
| 4 · DESIGNED | C-7F.8.3 — Irrelevant-context intrusion test | Candidate settings. | Tests irrelevant intrusion. | No hidden contamination assumption. | [V10 §7F] |
| 5 · DESIGNED | C-7F.8.4 — Semantic-versus-direct-context test | Candidate settings. | Tests channel confusion. | No untested adjacency assumption. | [V10 §7F] |
| 6 · DESIGNED | C-7F.8.5 — Retrieval reproducibility test | Candidate settings. | Tests reproducibility. | No untested repeatability assumption. | [V10 §7F] |
| 7 · DESIGNED | C-7F.8.6 — Retrieval latency test | Candidate settings. | Tests latency. | No invented performance limit. | [V10 §7F] |
| 8 · DESIGNED | C-7F.8.7 — Retrieval cost test | Candidate settings. | Tests cost. | No invented resource budget. | [V10 §7F] |
| 9 · DESIGNED | C-7F.8.8 — Retrieval limit-sensitivity test | Candidate settings. | Tests limit sensitivity. | No untested parameter stability. | [V10 §7F] |

SUB-PARTS: C-7F.8.1 — Retrieval reading-quality test; C-7F.8.2 — Relevant-context retrieval test; C-7F.8.3 — Irrelevant-context intrusion test; C-7F.8.4 — Semantic-versus-direct-context test; C-7F.8.5 — Retrieval reproducibility test; C-7F.8.6 — Retrieval latency test; C-7F.8.7 — Retrieval cost test; C-7F.8.8 — Retrieval limit-sensitivity test

### C-7F.8.1 — Retrieval reading-quality test
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — The reading-quality dimension of empirical parameter testing. [V10 §7F]
- Takes in: DESIGNED — Readings produced with candidate retrieval settings against gold material. [V10 §7F]
- Does: DESIGNED — Examines how the settings affect reading quality. [V10 §7F]
- Gives out: DESIGNED — Reading-quality evidence for later parameter selection. [V10 §7F]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7F.8 — Retrieval empirical-value discipline: Belongs to the required pre-default empirical evaluation. [V10 §7F]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.8 — Retrieval empirical-value discipline | Gold-set readings. | Examines quality. | Quality-informed settings. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.8.2 — Relevant-context retrieval test
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — The check that useful relevant context was actually retrieved. [V10 §7F]
- Takes in: DESIGNED — Candidate retrieval results and gold-set context expectations. [V10 §7F]
- Does: DESIGNED — Examines whether relevant context was supplied. [V10 §7F]
- Gives out: DESIGNED — Retrieval-coverage evidence. [V10 §7F]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7F.8 — Retrieval empirical-value discipline: Belongs to the required pre-default empirical evaluation. [V10 §7F]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.8 — Retrieval empirical-value discipline | Retrieved context. | Examines relevant coverage. | Coverage-informed settings. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.8.3 — Irrelevant-context intrusion test
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — The check for irrelevant material introduced by retrieval settings. [V10 §7F]
- Takes in: DESIGNED — Supplied context under candidate settings. [V10 §7F]
- Does: DESIGNED — Examines whether unrelated material entered the reading input. [V10 §7F]
- Gives out: DESIGNED — Irrelevant-intrusion evidence. [V10 §7F]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7F.8 — Retrieval empirical-value discipline: Belongs to the required pre-default empirical evaluation. [V10 §7F]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.8 — Retrieval empirical-value discipline | Supplied material. | Examines contamination. | Intrusion-informed settings. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.8.4 — Semantic-versus-direct-context test
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — The check for semantic matches being mistaken for direct context. [V10 §7F]
- Takes in: DESIGNED — Readings and their separately labeled supplied channels. [V10 §7F]
- Does: DESIGNED — Examines whether the reading confused similarity with preceding conversation. [V10 §7F]
- Gives out: DESIGNED — Channel-confusion evidence. [V10 §7F]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7F.8 — Retrieval empirical-value discipline: Belongs to the required pre-default empirical evaluation. [V10 §7F]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.8 — Retrieval empirical-value discipline | Readings and channels. | Examines false adjacency. | Separation-informed settings. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.8.5 — Retrieval reproducibility test
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — The reproducibility dimension of parameter testing. [V10 §7F]
- Takes in: DESIGNED — Repeated comparable retrieval evaluations and their recorded configuration provenance. [V10 §7F]
- Does: DESIGNED — Examines reproducibility. [V10 §7F]
- Gives out: DESIGNED — Reproducibility evidence for later settings. [V10 §7F]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7F.8 — Retrieval empirical-value discipline: Belongs to the required pre-default empirical evaluation. [V10 §7F]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.8 — Retrieval empirical-value discipline | Comparable runs. | Examines reproducibility. | Reproducibility-informed settings. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.8.6 — Retrieval latency test
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — The latency dimension of empirical testing. [V10 §7F]
- Takes in: DESIGNED — Retrieval timing under candidate settings. [V10 §7F]
- Does: DESIGNED — Examines latency. [V10 §7F]
- Gives out: DESIGNED — Timing evidence without an invented acceptable threshold. [V10 §7F]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7F.8 — Retrieval empirical-value discipline: Belongs to the required pre-default empirical evaluation. [V10 §7F]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.8 — Retrieval empirical-value discipline | Run timings. | Examines latency. | Timing-informed settings. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.8.7 — Retrieval cost test
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — The cost dimension of empirical testing. [V10 §7F]
- Takes in: DESIGNED — Retrieval resource cost under candidate settings. [V10 §7F]
- Does: DESIGNED — Examines cost. [V10 §7F]
- Gives out: DESIGNED — Cost evidence without a selected budget value. [V10 §7F]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7F.8 — Retrieval empirical-value discipline: Belongs to the required pre-default empirical evaluation. [V10 §7F]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.8 — Retrieval empirical-value discipline | Resource costs. | Examines cost. | Cost-informed settings. | [V10 §7F] |

SUB-PARTS: NONE

### C-7F.8.8 — Retrieval limit-sensitivity test
Stamp: DESIGNED    Source: [V10 §7F]

ALONE
- What it is: DESIGNED — The check for sensitivity to changes in retrieval limits. [V10 §7F]
- Takes in: DESIGNED — Comparable evaluations under varied candidate bounds. [V10 §7F]
- Does: DESIGNED — Examines how changing limits affects retrieval and reading. [V10 §7F]
- Gives out: DESIGNED — Sensitivity evidence for later per-mode settings. [V10 §7F]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7F.8 — Retrieval empirical-value discipline: Belongs to the required pre-default empirical evaluation. [V10 §7F]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7F.8 — Retrieval empirical-value discipline | Varied bounds. | Examines changes. | Sensitivity-informed settings. | [V10 §7F] |

SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece USED BY continuations

| Owner whose USED BY is continued | Used in | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| C-LMAC — Live Mechanism Access Coordinator (§26) | DESIGNED — C-7F — Context Retrieval (§7F) | Target and purpose. | Coordinates authorized retrieval. | No unauthorized root returned. | [MAP C-7F] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED — C-7F — Context Retrieval (§7F) | Candidate access request. | Applies internal-use authorization first. | An authorized pool. | [MAP C-7F] [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5] |
| C-7R — Attention & Relevance Control (§7R) | DESIGNED — C-7F — Context Retrieval (§7F) | Authorized candidates and declaration. | Validates the shared Tier-1 contract. | Purpose-scoped dimensions. | [MAP C-7F] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |
| C-7GA.10 — thread_membership_v1 | DESIGNED — C-7F.2 — Conceptual channel combinations | New-root assignment. | Limits this trigger to bare or local-context. | No associative/combined bypass. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | ACCEPTED — C-7F.3.10 — B1 eligible_source_scope [proposed] | Purpose and candidates. | Authorizes internal use first. | No access expansion. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §5] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | ACCEPTED — C-7F.4.11 — Retrieval audit protection and one-log rule | Record access request. | Applies purpose authorization. | Protected provenance. | [04/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md §3] |
| C-7R — Attention & Relevance Control (§7R) | ACCEPTED — C-7F.6.10.5.4 — Relevance disagreement record handoff | Disagreement details. | Appends the settled record. | Cross-component audit continuity. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | ACCEPTED — C-7F.6.11 — RM-CR-01 [proposed] allowed-use boundary | Current purpose and candidate access. | Applies authorization first. | No withheld-material signaling. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| C-7R — Attention & Relevance Control (§7R) | ACCEPTED — C-7F.6.12 — RM-CR-01 [proposed] logging contract | Completed evaluation. | Appends the shared event schema. | Relevance audit trail. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.6] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| C-7R — Attention & Relevance Control (§7R) | ACCEPTED — C-7F.6.14 — A4 eight-field declaration validity | Declaration and purpose. | Validates Tier 1; consumer owns Tier 2. | Explicit ownership. | [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §3] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.1] |
| C-7H — Reread Lifecycle (§7H) | ACCEPTED — C-7F.7.3 — Accepted B26 stop-after-retry policy | Technical failure and accepted retry references. | Uses bounded admission and real-change rules. | No unauthorized further attempt. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | ACCEPTED — C-7F.6.4 — RM-CR-01 [proposed] candidate roots | Purpose-authorized root candidates. | Proceeds only when the declaration receives only prior purpose-authorized roots. | Nothing in this card. | [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |

## Scope and path placement

C-7F owns retrieval-channel separation, per-mode settings, provenance, audit structure, safety ceilings and the concrete RM-CR-01 relevance declaration. Its root has separate use rows for P-MAIN step 9, CY-A and CY-B; all descendants inherit those placements through the sub-part tree. Retrieval itself has no visible surface. The complete chat-response synchronization and assembled cycle paths remain their separate owners.

The B1 mode and audit structures are accepted designs with proposed field names and final serialization open. Every bound and ceiling value remains empirical and open. The four conceptual channel categories do not override the new-root worker's permanent bare/local-context restriction. Engine B n=3 is not a general default. A4's eight required fields are concretely supplied by the declaration's component identity, purpose, selected mode, reason, uncertainty behavior, allowed use, audit and fail-closed rules; shared structure retains the same current IDs where reused.


## Cross-piece TOGETHER continuations for incoming uses

| Using card | Field | Current owner | Condition / handoff | Source |
|---|---|---|---|---|
| C-ENGINE-C — Engine C: story-layer reading [NOT BUILT; GATED] (§7C, §7K) | Fed by | C-7F — Context Retrieval (§7F) | DESIGNED — Receives story-pass context while preserving root evidence versus prior-reading context as distinct channels. | [MAP C-ENGINE-C] |
| C-ENGINE-C.2.1 — Root evidence channel | Fed by | C-7F — Context Retrieval (§7F) | DESIGNED — Receives source roots for the story-reading pass. | [MAP C-ENGINE-C] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] |
| C-ENGINE-C.2.2 — Prior reading context channel | Fed by | C-7F — Context Retrieval (§7F) | DESIGNED — Retains the earlier broad story-context handoff; RM-CR-01 does not select prior readings as root candidates. | [MAP C-ENGINE-C] |
| C-INDEX.1.2 — Cosine distance | Gated by | C-7F — Context Retrieval (§7F) | DESIGNED — Similarity retains its distinct provenance. | [V10 §7F] |
| C-INDEX.5 — Semantic retrieval interface | Changes | C-7F — Context Retrieval (§7F) | DESIGNED — Supplies ranked neighbors to the bounded semantic channel; the retrieval owner sets parameters and records runs. | [MAP C-INDEX] [V10 §7F] |
| C-13.3 — Silent memory pull | Fed by | C-7F — Context Retrieval (§7F) | DESIGNED — Supplies the live turn's silent context pull under authorization. | [MAP C-13] |
| C-14.6.3 — Reliable reference into retrieval | Changes | C-7F — Context Retrieval (§7F) | DESIGNED — Supplies only reliable references as provenance-bearing context through normal channels. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §8] |
| C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | Fed by | C-7F — Context Retrieval (§7F) | DESIGNED — Receives positional and semantic context separately. | [MAP C-7G] |
| C-7GA.11.2 — Step 2 — Retrieve context through LMAC | Fed by | C-7F — Context Retrieval (§7F) | DESIGNED — Receives authorized preceding context or an honest empty outcome under the new-root mode rule. | [V10 §7G-A / WORKER PASS SEQUENCE — PRIMARY STEPS WITH CHECKPOINT SUBSTEPS] |


## Source conflicts and explicit source-scope differences

| Kind | Sources and exact difference | Preserved treatment |
|---|---|---|
| Accepted source outside permitted folders | Both permitted Bundle 2 receipts identify foundation v1_0 (SHA-256 9c761e590afbbd372d7152b2bf19e54f7487d6e8dab30588aad54b2819f07da8) as accepted. Its sole path at the pin is in 99_HISTORICAL_CANDIDATES, which contract §2.4 prohibits reading. [04/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md §2] [04/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md §3] | The file was not read. Status evidence is retained. B26 behavior repeated directly in the permitted formal-declarations §§5.7 and 6 is placed; undisclosed foundation-specific state, identity, duplicate and crash mechanics are source-scope gaps, not a claim that no accepted design exists. No receipt summary is expanded into invented architecture. |
| Accepted design versus earlier open slots | V10, Map and B1/A4 text leave actual relevance declarations and B26 policy open. The later accepted formal-declarations source supplies RM-CR-01 and explicitly repeats bounded retry then terminal stop, with no degraded continuation after exhaustion. [V10 §7F] [MAP C-7F] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] | Both levels remain visible: DESIGNED governing retrieval and ACCEPTED standalone structures/content. No empirical value, operational B9/B26 integration or runtime readiness is inferred. The closure receipt retains its own receipt-audit condition; no independent receipt PASS is invented. |
| Broad story-context handoff versus concrete candidate scope | Map C-ENGINE-C has root evidence plus separate prior-reading context and names C-7F upstream. RM-CR-01 expressly selects roots only and excludes prior readings as its candidate type. [MAP C-ENGINE-C] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §6] | The earlier C-ENGINE-C.2.2 handoff remains recorded, with the exact prior-reading retrieval-mode integration left open. Prior readings do not enter RM-CR-01 as roots. No contradictory new candidate type is invented. |
| Abstract combinations versus trigger permission | V10 §7F names four conceptual combinations. The new-root thread_membership_v1 rule permanently prohibits associative/combined and falls back to bare with an implementation-error record if either is produced. [V10 §7F] [V10 §7G-A / MODE-ASSIGNMENT RULE:] | The four categories remain conceptual; the worker-specific restriction continues unchanged under C-7GA.10. No semantic retrieval is enabled for that trigger by this chapter. |
| General honest degradation versus retrieval-specific stop | A4 allows halt or marked degradation according to the owning component's settled rules; RM-CR-01 specifically prohibits degraded continuation after exhausted technical retry absent a separate later authorized rule. [04/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md §5] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §5.7] | The generic statement is not a retrieval fallback permission. Genuine emptiness remains a normal bare continuation; exhausted failure stops. |

No direct contradictory behavior was silently reconciled in this piece. These rows preserve acceptance chronology, source availability and scope distinctions without manufacturing a [SOURCE CONFLICT] where a later accepted design merely fills an earlier opening.

## Explicit remaining scope

- **CH05-d, C-7H:** the shared B9 retry architecture, values, episode/real-change records, B10 reread identity and A25 mode connections. C-7F.7.3 is a consumer boundary, not a duplicate retry state machine. B9 integration into the retrieval source seam remains explicitly open.
- **CH08-b, C-7R:** the complete shared relevance vocabulary, two-tier validation, six deterministic validation checks, full Decision-11 disagreement and Decision-12 relevance-event schemas, unknown-purpose and version-change mechanisms. Current RM-CR-01 content and the complete shared uncertainty behavior it consumes are present here. A4 shared policy is read whole; its consumer-specific realization here does not claim all consumers are placed.
- **Other formal declarations:** RM-RR-01 belongs to CH05-d/C-7H; RM-CV-01 to CH06-d/C-7M; RM-AS-01 to CH07-a/C-7N; RM-LS-01 to CH06-f/C-7D. Their sections were not counted as read for this piece. The source remains pending for whole-file reading.
- **CH08-a/C-7Q and CH08-c/C-LMAC:** complete privacy and access-coordination mechanics. Current authorization-before-relevance and no-withheld-material signaling conditions are explicit. **CH06-b/C-7K and CH06-g/C-24:** full theme and connection acceptance; retrieval uses recorded links and never accepts a connection itself.
- **B26 foundation source-scope gap:** its accepted identity and exclusion are recorded above. Only behavior directly repeated in permitted READ sources is placed. Detailed foundation-only field names, failure-state transitions, duplicate/recovery cases and exact operation-identity binding cannot receive source-completeness credit without an authorized READ placement. This is retained for assembly/audit and does not authorize opening the excluded file.
- **CH11 and CH12:** complete cycle assembly and cumulative gap/conflict/coverage reconciliation. This piece does not activate retrieval, tune values or implement storage.

## Additional undecided implementation slots

| Slot | Value | Boundary / owner |
|---|---|---|
| Empirical positional and semantic result limits | NOT DECIDED | Per-mode and gold-set tested; n=3 remains experiment-specific. |
| Ranking-rule content and semantic thresholds | NOT DECIDED | Versioned references exist; values cannot be silently chosen. |
| Token/size budget and optional time-range span | NOT DECIDED | Every actual value remains open. |
| Hard ceiling values for every bounded quantity | NOT DECIDED | The ceiling mechanism exists as accepted design; maxima are not chosen. |
| Final mode/audit/ceiling serialization and field naming | NOT DECIDED | B1 identifiers remain proposed. |
| Exact source-operation timeout | NOT DECIDED | A system-failure class exists; no timeout duration is supplied here. |
| Operational B9/B26 integration | NOT DECIDED | Accepted policy and generic retry machinery do not supply an implemented retrieval seam. |
| Prior-reading retrieval mode serving the story-context channel | NOT DECIDED | RM-CR-01's candidate type remains roots only. |
| Foundation-only detailed B26 identity/state/recovery mapping under permitted sources | NOT DECIDED | Accepted source is excluded by contract §2.4 at this pin; not asserted undesigned. |
| Later precompute triggers and invalidators | NOT DECIDED | This declaration explicitly authorizes on-demand evaluation only. |
| Side-drawer visual/interaction mechanics and future mouth/validator technology | NOT DECIDED | Outside the accepted retrieval declaration's settled operational content. |

## Review of plain gates and empty boxes

Every populated relationship names its actual source field, rule or connected owner. Channel assembly, invalidity checks, ceiling enforcement, categorical gates, ordering, uncertainty handling, logging and failure steps connect to their governing rules. Atomic identifiers, version fields, timestamps and recorded dimension values do not acquire invented independent failure mechanisms. Empty restrictions and gates were checked against the whole owning source section and the corresponding USED BY cells.

One meaning is preserved per ID. The B1 mode identity and configuration version are reused in the audit binding; per-item provenance has one identity reused by channel presentation and logging. RM-CR-01's four gate conditions, six selected dimensions, five explicit-link types, three excluded dimensions, none mouth authorization and all 13 declaration items are explicit. The four strength labels are carried as source-stated labels; this chapter does not invent a threshold-to-label mapping. Current-source reading scope is stated exactly; no full B26 or full formal-declarations read is claimed.

## Appendix A carry-forward — this piece

| Part | Field or cell | Value |
|---|---|---|
| C-7F.1 | Fails closed by | NOT DECIDED |
| C-7F.1 | Changes | NOT DECIDED |
| C-7F.1.1 | Fails closed by | NOT DECIDED |
| C-7F.1.1 | Fed by | NOT DECIDED |
| C-7F.1.1 | Changes | NOT DECIDED |
| C-7F.1.2 | Fails closed by | NOT DECIDED |
| C-7F.1.2 | Fed by | NOT DECIDED |
| C-7F.1.2 | Changes | NOT DECIDED |
| C-7F.1.3 | Fails closed by | NOT DECIDED |
| C-7F.1.3 | Fed by | NOT DECIDED |
| C-7F.1.3 | Changes | NOT DECIDED |
| C-7F.1.4 | Fails closed by | NOT DECIDED |
| C-7F.1.4 | Fed by | NOT DECIDED |
| C-7F.1.4 | Changes | NOT DECIDED |
| C-7F.2 | Fails closed by | NOT DECIDED |
| C-7F.2 | Changes | NOT DECIDED |
| C-7F.2.1 | Must never | NOT DECIDED |
| C-7F.2.1 | Fails closed by | NOT DECIDED |
| C-7F.2.1 | Fed by | NOT DECIDED |
| C-7F.2.1 | Gated by | NOT DECIDED |
| C-7F.2.1 | Changes | NOT DECIDED |
| C-7F.2.2 | Must never | NOT DECIDED |
| C-7F.2.2 | Fails closed by | NOT DECIDED |
| C-7F.2.2 | Fed by | NOT DECIDED |
| C-7F.2.2 | Gated by | NOT DECIDED |
| C-7F.2.2 | Changes | NOT DECIDED |
| C-7F.2.3 | Must never | NOT DECIDED |
| C-7F.2.3 | Fails closed by | NOT DECIDED |
| C-7F.2.3 | Fed by | NOT DECIDED |
| C-7F.2.3 | Gated by | NOT DECIDED |
| C-7F.2.3 | Changes | NOT DECIDED |
| C-7F.2.4 | Fails closed by | NOT DECIDED |
| C-7F.2.4 | Fed by | NOT DECIDED |
| C-7F.2.4 | Gated by | NOT DECIDED |
| C-7F.2.4 | Changes | NOT DECIDED |
| C-7F.3 | Changes | NOT DECIDED |
| C-7F.3.1 | Fails closed by | NOT DECIDED |
| C-7F.3.1 | Gated by | NOT DECIDED |
| C-7F.3.1 | Changes | NOT DECIDED |
| C-7F.3.1.1 | Must never | NOT DECIDED |
| C-7F.3.1.1 | Fails closed by | NOT DECIDED |
| C-7F.3.1.1 | Fed by | NOT DECIDED |
| C-7F.3.1.1 | Gated by | NOT DECIDED |
| C-7F.3.1.1 | Changes | NOT DECIDED |
| C-7F.3.1.2 | Fails closed by | NOT DECIDED |
| C-7F.3.1.2 | Fed by | NOT DECIDED |
| C-7F.3.1.2 | Gated by | NOT DECIDED |
| C-7F.3.1.2 | Changes | NOT DECIDED |
| C-7F.3.2 | Fails closed by | NOT DECIDED |
| C-7F.3.2 | Fed by | NOT DECIDED |
| C-7F.3.2 | Gated by | NOT DECIDED |
| C-7F.3.2 | Changes | NOT DECIDED |
| C-7F.3.3 | Must never | NOT DECIDED |
| C-7F.3.3 | Fails closed by | NOT DECIDED |
| C-7F.3.3 | Fed by | NOT DECIDED |
| C-7F.3.3 | Gated by | NOT DECIDED |
| C-7F.3.3 | Changes | NOT DECIDED |
| C-7F.3.4 | Fed by | NOT DECIDED |
| C-7F.3.4 | Changes | NOT DECIDED |
| C-7F.3.5 | Fails closed by | NOT DECIDED |
| C-7F.3.5 | Fed by | NOT DECIDED |
| C-7F.3.5 | Gated by | NOT DECIDED |
| C-7F.3.5 | Changes | NOT DECIDED |
| C-7F.3.6 | Fails closed by | NOT DECIDED |
| C-7F.3.6 | Fed by | NOT DECIDED |
| C-7F.3.6 | Gated by | NOT DECIDED |
| C-7F.3.6 | Changes | NOT DECIDED |
| C-7F.3.7 | Fails closed by | NOT DECIDED |
| C-7F.3.7 | Fed by | NOT DECIDED |
| C-7F.3.7 | Gated by | NOT DECIDED |
| C-7F.3.7 | Changes | NOT DECIDED |
| C-7F.3.8 | Fails closed by | NOT DECIDED |
| C-7F.3.8 | Fed by | NOT DECIDED |
| C-7F.3.8 | Gated by | NOT DECIDED |
| C-7F.3.8 | Changes | NOT DECIDED |
| C-7F.3.9 | Must never | NOT DECIDED |
| C-7F.3.9 | Fails closed by | NOT DECIDED |
| C-7F.3.9 | Fed by | NOT DECIDED |
| C-7F.3.9 | Gated by | NOT DECIDED |
| C-7F.3.9 | Changes | NOT DECIDED |
| C-7F.3.10 | Fed by | NOT DECIDED |
| C-7F.3.10 | Changes | NOT DECIDED |
| C-7F.3.11 | Fed by | NOT DECIDED |
| C-7F.3.11 | Changes | NOT DECIDED |
| C-7F.3.12 | Fed by | NOT DECIDED |
| C-7F.3.12 | Changes | NOT DECIDED |
| C-7F.3.13 | Fails closed by | NOT DECIDED |
| C-7F.3.13 | Fed by | NOT DECIDED |
| C-7F.3.13 | Gated by | NOT DECIDED |
| C-7F.3.13 | Changes | NOT DECIDED |
| C-7F.3.14 | Fails closed by | NOT DECIDED |
| C-7F.3.14 | Gated by | NOT DECIDED |
| C-7F.3.14 | Changes | NOT DECIDED |
| C-7F.3.14.1 | Must never | NOT DECIDED |
| C-7F.3.14.1 | Fails closed by | NOT DECIDED |
| C-7F.3.14.1 | Fed by | NOT DECIDED |
| C-7F.3.14.1 | Gated by | NOT DECIDED |
| C-7F.3.14.1 | Changes | NOT DECIDED |
| C-7F.3.14.2 | Must never | NOT DECIDED |
| C-7F.3.14.2 | Fails closed by | NOT DECIDED |
| C-7F.3.14.2 | Fed by | NOT DECIDED |
| C-7F.3.14.2 | Gated by | NOT DECIDED |
| C-7F.3.14.2 | Changes | NOT DECIDED |
| C-7F.3.14.3 | Must never | NOT DECIDED |
| C-7F.3.14.3 | Fails closed by | NOT DECIDED |
| C-7F.3.14.3 | Fed by | NOT DECIDED |
| C-7F.3.14.3 | Gated by | NOT DECIDED |
| C-7F.3.14.3 | Changes | NOT DECIDED |
| C-7F.3.15 | Fed by | NOT DECIDED |
| C-7F.3.15 | Changes | NOT DECIDED |
| C-7F.4 | Changes | NOT DECIDED |
| C-7F.4.1 | Fails closed by | NOT DECIDED |
| C-7F.4.1 | Fed by | NOT DECIDED |
| C-7F.4.1 | Gated by | NOT DECIDED |
| C-7F.4.1 | Changes | NOT DECIDED |
| C-7F.4.2 | Fails closed by | NOT DECIDED |
| C-7F.4.2 | Gated by | NOT DECIDED |
| C-7F.4.2 | Changes | NOT DECIDED |
| C-7F.4.3 | Fails closed by | NOT DECIDED |
| C-7F.4.3 | Fed by | NOT DECIDED |
| C-7F.4.3 | Gated by | NOT DECIDED |
| C-7F.4.3 | Changes | NOT DECIDED |
| C-7F.4.4 | Fails closed by | NOT DECIDED |
| C-7F.4.4 | Fed by | NOT DECIDED |
| C-7F.4.4 | Gated by | NOT DECIDED |
| C-7F.4.4 | Changes | NOT DECIDED |
| C-7F.4.5 | Must never | NOT DECIDED |
| C-7F.4.5 | Fails closed by | NOT DECIDED |
| C-7F.4.5 | Gated by | NOT DECIDED |
| C-7F.4.5 | Changes | NOT DECIDED |
| C-7F.4.5.1 | Must never | NOT DECIDED |
| C-7F.4.5.1 | Fails closed by | NOT DECIDED |
| C-7F.4.5.1 | Fed by | NOT DECIDED |
| C-7F.4.5.1 | Gated by | NOT DECIDED |
| C-7F.4.5.1 | Changes | NOT DECIDED |
| C-7F.4.5.2 | Must never | NOT DECIDED |
| C-7F.4.5.2 | Fails closed by | NOT DECIDED |
| C-7F.4.5.2 | Fed by | NOT DECIDED |
| C-7F.4.5.2 | Gated by | NOT DECIDED |
| C-7F.4.5.2 | Changes | NOT DECIDED |
| C-7F.4.5.3 | Must never | NOT DECIDED |
| C-7F.4.5.3 | Fails closed by | NOT DECIDED |
| C-7F.4.5.3 | Fed by | NOT DECIDED |
| C-7F.4.5.3 | Gated by | NOT DECIDED |
| C-7F.4.5.3 | Changes | NOT DECIDED |
| C-7F.4.6 | Fails closed by | NOT DECIDED |
| C-7F.4.6 | Gated by | NOT DECIDED |
| C-7F.4.6 | Changes | NOT DECIDED |
| C-7F.4.6.1 | Fails closed by | NOT DECIDED |
| C-7F.4.6.1 | Fed by | NOT DECIDED |
| C-7F.4.6.1 | Gated by | NOT DECIDED |
| C-7F.4.6.1 | Changes | NOT DECIDED |
| C-7F.4.6.2 | Fails closed by | NOT DECIDED |
| C-7F.4.6.2 | Fed by | NOT DECIDED |
| C-7F.4.6.2 | Gated by | NOT DECIDED |
| C-7F.4.6.2 | Changes | NOT DECIDED |
| C-7F.4.6.3 | Must never | NOT DECIDED |
| C-7F.4.6.3 | Fails closed by | NOT DECIDED |
| C-7F.4.6.3 | Fed by | NOT DECIDED |
| C-7F.4.6.3 | Gated by | NOT DECIDED |
| C-7F.4.6.3 | Changes | NOT DECIDED |
| C-7F.4.6.4 | Fails closed by | NOT DECIDED |
| C-7F.4.6.4 | Fed by | NOT DECIDED |
| C-7F.4.6.4 | Gated by | NOT DECIDED |
| C-7F.4.6.4 | Changes | NOT DECIDED |
| C-7F.4.6.5 | Must never | NOT DECIDED |
| C-7F.4.6.5 | Fails closed by | NOT DECIDED |
| C-7F.4.6.5 | Fed by | NOT DECIDED |
| C-7F.4.6.5 | Gated by | NOT DECIDED |
| C-7F.4.6.5 | Changes | NOT DECIDED |
| C-7F.4.6.6 | Fails closed by | NOT DECIDED |
| C-7F.4.6.6 | Fed by | NOT DECIDED |
| C-7F.4.6.6 | Gated by | NOT DECIDED |
| C-7F.4.6.6 | Changes | NOT DECIDED |
| C-7F.4.7 | Fails closed by | NOT DECIDED |
| C-7F.4.7 | Fed by | NOT DECIDED |
| C-7F.4.7 | Gated by | NOT DECIDED |
| C-7F.4.7 | Changes | NOT DECIDED |
| C-7F.4.8 | Fed by | NOT DECIDED |
| C-7F.4.8 | Changes | NOT DECIDED |
| C-7F.4.9 | Must never | NOT DECIDED |
| C-7F.4.9 | Fails closed by | NOT DECIDED |
| C-7F.4.9 | Fed by | NOT DECIDED |
| C-7F.4.9 | Gated by | NOT DECIDED |
| C-7F.4.9 | Changes | NOT DECIDED |
| C-7F.4.10 | Fails closed by | NOT DECIDED |
| C-7F.4.10 | Fed by | NOT DECIDED |
| C-7F.4.10 | Gated by | NOT DECIDED |
| C-7F.4.10 | Changes | NOT DECIDED |
| C-7F.4.11 | Fed by | NOT DECIDED |
| C-7F.4.11 | Changes | NOT DECIDED |
| C-7F.4.12 | Must never | NOT DECIDED |
| C-7F.4.12 | Fails closed by | NOT DECIDED |
| C-7F.4.12 | Fed by | NOT DECIDED |
| C-7F.4.12 | Gated by | NOT DECIDED |
| C-7F.4.12 | Changes | NOT DECIDED |
| C-7F.5 | Changes | NOT DECIDED |
| C-7F.5.1 | Must never | NOT DECIDED |
| C-7F.5.1 | Fails closed by | NOT DECIDED |
| C-7F.5.1 | Fed by | NOT DECIDED |
| C-7F.5.1 | Gated by | NOT DECIDED |
| C-7F.5.1 | Changes | NOT DECIDED |
| C-7F.5.2 | Fails closed by | NOT DECIDED |
| C-7F.5.2 | Fed by | NOT DECIDED |
| C-7F.5.2 | Gated by | NOT DECIDED |
| C-7F.5.2 | Changes | NOT DECIDED |
| C-7F.5.3 | Fails closed by | NOT DECIDED |
| C-7F.5.3 | Fed by | NOT DECIDED |
| C-7F.5.3 | Gated by | NOT DECIDED |
| C-7F.5.3 | Changes | NOT DECIDED |
| C-7F.5.4 | Fed by | NOT DECIDED |
| C-7F.5.4 | Changes | NOT DECIDED |
| C-7F.5.5 | Fed by | NOT DECIDED |
| C-7F.5.5 | Changes | NOT DECIDED |
| C-7F.5.6 | Fed by | NOT DECIDED |
| C-7F.5.7 | Fails closed by | NOT DECIDED |
| C-7F.5.7 | Fed by | NOT DECIDED |
| C-7F.5.7 | Changes | NOT DECIDED |
| C-7F.6.1 | Fails closed by | NOT DECIDED |
| C-7F.6.1 | Fed by | NOT DECIDED |
| C-7F.6.1 | Gated by | NOT DECIDED |
| C-7F.6.1 | Changes | NOT DECIDED |
| C-7F.6.2 | Fed by | NOT DECIDED |
| C-7F.6.2 | Gated by | NOT DECIDED |
| C-7F.6.2 | Changes | NOT DECIDED |
| C-7F.6.3 | Fails closed by | NOT DECIDED |
| C-7F.6.3 | Fed by | NOT DECIDED |
| C-7F.6.3 | Gated by | NOT DECIDED |
| C-7F.6.3 | Changes | NOT DECIDED |
| C-7F.6.4 | Fed by | NOT DECIDED |
| C-7F.6.4 | Changes | NOT DECIDED |
| C-7F.6.5 | Fed by | NOT DECIDED |
| C-7F.6.5 | Changes | NOT DECIDED |
| C-7F.6.5.1 | Fed by | NOT DECIDED |
| C-7F.6.5.1 | Changes | NOT DECIDED |
| C-7F.6.5.2 | Fed by | NOT DECIDED |
| C-7F.6.5.2 | Changes | NOT DECIDED |
| C-7F.6.5.3 | Fed by | NOT DECIDED |
| C-7F.6.5.3 | Changes | NOT DECIDED |
| C-7F.6.5.4 | Fed by | NOT DECIDED |
| C-7F.6.5.4 | Changes | NOT DECIDED |
| C-7F.6.6 | Changes | NOT DECIDED |
| C-7F.6.6.1 | Fails closed by | NOT DECIDED |
| C-7F.6.6.1 | Fed by | NOT DECIDED |
| C-7F.6.6.1 | Gated by | NOT DECIDED |
| C-7F.6.6.1 | Changes | NOT DECIDED |
| C-7F.6.6.2 | Fails closed by | NOT DECIDED |
| C-7F.6.6.2 | Fed by | NOT DECIDED |
| C-7F.6.6.2 | Gated by | NOT DECIDED |
| C-7F.6.6.2 | Changes | NOT DECIDED |
| C-7F.6.6.3 | Must never | NOT DECIDED |
| C-7F.6.6.3 | Fails closed by | NOT DECIDED |
| C-7F.6.6.3 | Fed by | NOT DECIDED |
| C-7F.6.6.3 | Gated by | NOT DECIDED |
| C-7F.6.6.3 | Changes | NOT DECIDED |
| C-7F.6.6.4 | Fails closed by | NOT DECIDED |
| C-7F.6.6.4 | Gated by | NOT DECIDED |
| C-7F.6.6.4 | Changes | NOT DECIDED |
| C-7F.6.6.4.1 | Fails closed by | NOT DECIDED |
| C-7F.6.6.4.1 | Fed by | NOT DECIDED |
| C-7F.6.6.4.1 | Gated by | NOT DECIDED |
| C-7F.6.6.4.1 | Changes | NOT DECIDED |
| C-7F.6.6.4.2 | Fails closed by | NOT DECIDED |
| C-7F.6.6.4.2 | Fed by | NOT DECIDED |
| C-7F.6.6.4.2 | Gated by | NOT DECIDED |
| C-7F.6.6.4.2 | Changes | NOT DECIDED |
| C-7F.6.6.4.3 | Fails closed by | NOT DECIDED |
| C-7F.6.6.4.3 | Fed by | NOT DECIDED |
| C-7F.6.6.4.3 | Gated by | NOT DECIDED |
| C-7F.6.6.4.3 | Changes | NOT DECIDED |
| C-7F.6.6.4.4 | Fails closed by | NOT DECIDED |
| C-7F.6.6.4.4 | Fed by | NOT DECIDED |
| C-7F.6.6.4.4 | Gated by | NOT DECIDED |
| C-7F.6.6.4.4 | Changes | NOT DECIDED |
| C-7F.6.6.4.5 | Fails closed by | NOT DECIDED |
| C-7F.6.6.4.5 | Fed by | NOT DECIDED |
| C-7F.6.6.4.5 | Gated by | NOT DECIDED |
| C-7F.6.6.4.5 | Changes | NOT DECIDED |
| C-7F.6.6.5 | Must never | NOT DECIDED |
| C-7F.6.6.5 | Fails closed by | NOT DECIDED |
| C-7F.6.6.5 | Fed by | NOT DECIDED |
| C-7F.6.6.5 | Gated by | NOT DECIDED |
| C-7F.6.6.5 | Changes | NOT DECIDED |
| C-7F.6.6.6 | Fails closed by | NOT DECIDED |
| C-7F.6.6.6 | Fed by | NOT DECIDED |
| C-7F.6.6.6 | Gated by | NOT DECIDED |
| C-7F.6.6.6 | Changes | NOT DECIDED |
| C-7F.6.6.7 | Fed by | NOT DECIDED |
| C-7F.6.6.7 | Gated by | NOT DECIDED |
| C-7F.6.6.7 | Changes | NOT DECIDED |
| C-7F.6.7 | Fed by | NOT DECIDED |
| C-7F.6.7 | Gated by | NOT DECIDED |
| C-7F.6.7 | Changes | NOT DECIDED |
| C-7F.6.8 | Fed by | NOT DECIDED |
| C-7F.6.8 | Changes | NOT DECIDED |
| C-7F.6.9 | Fed by | NOT DECIDED |
| C-7F.6.9 | Gated by | NOT DECIDED |
| C-7F.6.9 | Changes | NOT DECIDED |
| C-7F.6.10 | Changes | NOT DECIDED |
| C-7F.6.10.1 | Fed by | NOT DECIDED |
| C-7F.6.10.1 | Changes | NOT DECIDED |
| C-7F.6.10.2 | Fed by | NOT DECIDED |
| C-7F.6.10.3 | Fed by | NOT DECIDED |
| C-7F.6.10.3 | Changes | NOT DECIDED |
| C-7F.6.10.4 | Fed by | NOT DECIDED |
| C-7F.6.10.4 | Changes | NOT DECIDED |
| C-7F.6.10.5.1 | Fails closed by | NOT DECIDED |
| C-7F.6.10.5.1 | Fed by | NOT DECIDED |
| C-7F.6.10.5.1 | Gated by | NOT DECIDED |
| C-7F.6.10.5.1 | Changes | NOT DECIDED |
| C-7F.6.10.5.2 | Fed by | NOT DECIDED |
| C-7F.6.10.5.2 | Changes | NOT DECIDED |
| C-7F.6.10.5.3 | Fed by | NOT DECIDED |
| C-7F.6.10.5.3 | Changes | NOT DECIDED |
| C-7F.6.10.5.4 | Fed by | NOT DECIDED |
| C-7F.6.10.5.5 | Fed by | NOT DECIDED |
| C-7F.6.10.5.5 | Changes | NOT DECIDED |
| C-7F.6.11 | Fed by | NOT DECIDED |
| C-7F.6.11 | Changes | NOT DECIDED |
| C-7F.6.12 | Fed by | NOT DECIDED |
| C-7F.6.13 | Fed by | NOT DECIDED |
| C-7F.6.13 | Changes | NOT DECIDED |
| C-7F.6.15 | Fed by | NOT DECIDED |
| C-7F.6.15 | Changes | NOT DECIDED |
| C-7F.7 | Changes | NOT DECIDED |
| C-7F.7.1 | Fed by | NOT DECIDED |
| C-7F.7.1.1 | Fails closed by | NOT DECIDED |
| C-7F.7.1.1 | Fed by | NOT DECIDED |
| C-7F.7.1.1 | Gated by | NOT DECIDED |
| C-7F.7.1.1 | Changes | NOT DECIDED |
| C-7F.7.1.2 | Fails closed by | NOT DECIDED |
| C-7F.7.1.2 | Fed by | NOT DECIDED |
| C-7F.7.1.2 | Gated by | NOT DECIDED |
| C-7F.7.1.2 | Changes | NOT DECIDED |
| C-7F.7.1.3 | Fails closed by | NOT DECIDED |
| C-7F.7.1.3 | Fed by | NOT DECIDED |
| C-7F.7.1.3 | Gated by | NOT DECIDED |
| C-7F.7.1.3 | Changes | NOT DECIDED |
| C-7F.7.1.4 | Fails closed by | NOT DECIDED |
| C-7F.7.1.4 | Fed by | NOT DECIDED |
| C-7F.7.1.4 | Gated by | NOT DECIDED |
| C-7F.7.1.4 | Changes | NOT DECIDED |
| C-7F.7.2 | Gated by | NOT DECIDED |
| C-7F.7.2 | Changes | NOT DECIDED |
| C-7F.7.2.1 | Fed by | NOT DECIDED |
| C-7F.7.2.1 | Gated by | NOT DECIDED |
| C-7F.7.2.1 | Changes | NOT DECIDED |
| C-7F.7.2.2 | Fed by | NOT DECIDED |
| C-7F.7.2.2 | Gated by | NOT DECIDED |
| C-7F.7.2.2 | Changes | NOT DECIDED |
| C-7F.7.2.3 | Fed by | NOT DECIDED |
| C-7F.7.2.3 | Gated by | NOT DECIDED |
| C-7F.7.2.3 | Changes | NOT DECIDED |
| C-7F.7.2.4 | Fed by | NOT DECIDED |
| C-7F.7.2.4 | Gated by | NOT DECIDED |
| C-7F.7.2.4 | Changes | NOT DECIDED |
| C-7F.7.3 | Fed by | NOT DECIDED |
| C-7F.7.3 | Changes | NOT DECIDED |
| C-7F.8 | Changes | NOT DECIDED |
| C-7F.8.1 | Must never | NOT DECIDED |
| C-7F.8.1 | Fails closed by | NOT DECIDED |
| C-7F.8.1 | Fed by | NOT DECIDED |
| C-7F.8.1 | Changes | NOT DECIDED |
| C-7F.8.2 | Must never | NOT DECIDED |
| C-7F.8.2 | Fails closed by | NOT DECIDED |
| C-7F.8.2 | Fed by | NOT DECIDED |
| C-7F.8.2 | Changes | NOT DECIDED |
| C-7F.8.3 | Must never | NOT DECIDED |
| C-7F.8.3 | Fails closed by | NOT DECIDED |
| C-7F.8.3 | Fed by | NOT DECIDED |
| C-7F.8.3 | Changes | NOT DECIDED |
| C-7F.8.4 | Must never | NOT DECIDED |
| C-7F.8.4 | Fails closed by | NOT DECIDED |
| C-7F.8.4 | Fed by | NOT DECIDED |
| C-7F.8.4 | Changes | NOT DECIDED |
| C-7F.8.5 | Must never | NOT DECIDED |
| C-7F.8.5 | Fails closed by | NOT DECIDED |
| C-7F.8.5 | Fed by | NOT DECIDED |
| C-7F.8.5 | Changes | NOT DECIDED |
| C-7F.8.6 | Must never | NOT DECIDED |
| C-7F.8.6 | Fails closed by | NOT DECIDED |
| C-7F.8.6 | Fed by | NOT DECIDED |
| C-7F.8.6 | Changes | NOT DECIDED |
| C-7F.8.7 | Must never | NOT DECIDED |
| C-7F.8.7 | Fails closed by | NOT DECIDED |
| C-7F.8.7 | Fed by | NOT DECIDED |
| C-7F.8.7 | Changes | NOT DECIDED |
| C-7F.8.8 | Must never | NOT DECIDED |
| C-7F.8.8 | Fails closed by | NOT DECIDED |
| C-7F.8.8 | Fed by | NOT DECIDED |
| C-7F.8.8 | Changes | NOT DECIDED |

## Retained plain-gate inventory

All populated TOGETHER lines name an owning or connected card; no plain gate remains.

## Source coverage added by CH05-c

| Source | Scope read | Landing / exclusion |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: §7F complete; §7G-A mode/worker rules consumed through current CH05-b ownership and their exact source headings. | C-7F, C-7F.1 through C-7F.2, C-7F.7 through C-7F.8 and shared worker restriction; empty/failure distinction and eight test dimensions. |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped: Complete C-7F, C-INDEX, C-ENGINE-C, C-7G, C-7GA, C-13 entries and CY-A/CY-B sequences. | Root flow and nine incoming continuations; path use and exact component boundaries. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md` | Whole: Complete B1 file, structural fields, ceilings, boundaries and opens; workflow/self-audit excluded. | C-7F.3–5 and shared per-item provenance; all configuration/audit fields, ceiling identity/rules and validity. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md` | Whole: Complete A4 policy, mandatory fields, authorization, honest failure and open boundaries. | C-7F.6.14 and authorization/honest-failure consumption; complete shared vocabulary and records remain C-7R CH08-b. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Scoped: §§0–6 and 13–14 complete, including every RM-CR-01 item and shared declaration/uncertainty/logging/failure framework. Other consumer declarations and remaining sections not credited. | C-7F.6 and C-7F.7.3: complete retrieval declaration and shared uncertainty consumed; other four declarations have explicit later owners. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md` | Whole: Complete status/identity receipt only. | Acceptance/identity evidence only; no new behavior from receipt. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md` | Whole: Complete status/identity receipt only. | Acceptance/identity evidence only; no new behavior from receipt. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Whole: Complete receipt; accepted foundation identity and scope evidence only, not a substitute for excluded foundation mechanics. | Foundation accepted identity and excluded-location finding; no new architecture from receipt. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: Complete receipt, source identities, accepted formal-declaration status and its own conditional audit gate; no unobserved receipt PASS inferred. | Accepted declaration identity and receipt-audit scope; integration/open distinctions outside behavior. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped: §8 B18 complete for the existing reliable-reference incoming seam only; full records remain CH04-d. | Existing C-14.6.3 reliable-reference use into retrieval; original mechanism retained in CH04-d. |

## Coverage matrix — cumulative carried inventory








The following inventory retains the preceding pieces’ placements and read status. This piece’s additional placements and deferrals are in the source-scope table above; inherited notes are not fresh whole-read claims.
### File coverage

| Row | Source | Read scope | Placement |
|---|---|---|---|
| F001 | `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped read in CH04-b: §0B; §6A SCHEMA CONSTRAINTS; §6B schema/status boundary; full §7E-TSC §§1–31. Prior read credits retained. | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.1; C-STORE.2; C-STORE.3; CY-A Chapter 3-b: C-READ and its v1 record, validator, writer, quarantine, production-boundary and operation-record sub-parts; CY-A/CY-F reading-write interfaces. Chapter 3-c: governing checks for C-READ.10; A2/firmness additions stay ACCEPTED, never BUILT. Chapter 3-d: source-status and no-production-write boundaries; governing operational living-memory rule at C-READ.11.9.4.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.3, C-ENGINE-C.3.1, C-ENGINE-C.3.2, C-ENGINE-C.3.3, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.11.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1, C-ENGINE-AB.1.1, C-ENGINE-AB.1.2, C-ENGINE-AB.1.3, C-ENGINE-AB.2, C-ENGINE-AB.2.1, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.1, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.2.4, C-ENGINE-AB.3, C-ENGINE-AB.4, C-ENGINE-AB.5, C-ENGINE-AB.6, C-ENGINE-AB.8, C-ENGINE-AB.9.; CH03-k: C-INDEX, C-INDEX.1, C-INDEX.1.1, C-INDEX.1.2, C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.1, C-INDEX.4.2, C-INDEX.4.3, C-INDEX.4.4, C-INDEX.4.5, C-INDEX.4.7, C-INDEX.4.8, C-INDEX.5, C-INDEX.6.; CH03-l: C-GOLD, C-GOLD.2, C-GOLD.2.1, C-GOLD.3, C-GOLD.3.1, C-GOLD.6, C-GOLD.6.1, C-GOLD.6.2, C-GOLD.6.3, C-GOLD.7, C-GOLD.7.4.; CH03-o: C-INGEST, C-INGEST.1, C-INGEST.2, C-INGEST.3, C-INGEST.4, C-INGEST.4.1, C-INGEST.4.2, C-INGEST.4.3, C-INGEST.4.4, C-INGEST.4.5, C-INGEST.4.6, C-INGEST.4.7, C-INGEST.4.8, C-INGEST.4.8.1, C-INGEST.4.8.2, C-INGEST.4.8.3, C-INGEST.4.8.4, C-INGEST.4.9, C-INGEST.6.; CH03-p: C-DETECT, C-DETECT.1, C-DETECT.1.1, C-DETECT.1.3, C-DETECT.2, C-DETECT.2.1, C-DETECT.2.2, C-DETECT.2.3, C-DETECT.2.4, C-DETECT.2.5, C-DETECT.3, C-DETECT.3.1, C-DETECT.3.2, C-DETECT.3.3, C-DETECT.3.4, C-DETECT.3.5, C-DETECT.3.6, C-DETECT.4.1.; CH04-a: C-7E, C-7E.1, C-7E.1.1, C-7E.1.2, C-7E.2, C-7E.3, C-7E.4, C-7E.5, C-7E.5.1, C-7E.5.2, C-7E.5.3, C-7E.5.4, C-7E.5.5, C-7E.5.6, C-7E.6, C-7E.6.1, C-7E.6.2, C-7E.6.3, C-7E.6.4, C-7E.6.5, C-7E.6.6, C-7E.6.7, C-7E.7, C-7E.8, C-7E.8.1, C-7E.8.2, C-7E.8.3, C-7E.8.4, C-7E.9, C-7E.9.1, C-7E.9.2, C-7E.9.2.1, C-7E.9.2.2, C-7E.9.2.3, C-7E.9.2.4, C-7E.9.3, C-7E.9.3.1, C-7E.9.3.2, C-7E.9.3.3, C-7E.9.3.4, C-7E.9.3.5, C-7E.9.3.6, C-7E.9.4, C-7E.10, C-7E.10.1, C-7E.10.2, C-7E.11, C-7E.12, C-7E.13, C-7E.13.1, C-7E.13.4, C-7E.13.5, C-7E.13.6. CH04-b: see the exact source-scope and landing table above.  CH04-c: scoped read; exact scope and placement in the current source table.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F002 | `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Scoped read in CH04-b: §3N; inspection conflict. Prior read credits retained. | EXCLUDED: interaction/workflow guidance under §1.3 and §2.4. NOT PLACED: remaining behavior belongs to other component groups.; Chapter 3-a: C-STORE.2.3 Chapter 3-b: C-READ.1 confidence semantics and C-READ.2 uncertainty-preserving shape gate; remaining scope retained. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.2, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.8.; CH03-l: C-GOLD, C-GOLD.2, C-GOLD.2.1, C-GOLD.3, C-GOLD.3.1, C-GOLD.4, C-GOLD.4.1, C-GOLD.4.2, C-GOLD.4.3, C-GOLD.4.4, C-GOLD.4.5, C-GOLD.4.6, C-GOLD.5, C-GOLD.6, C-GOLD.6.1, C-GOLD.6.3, C-GOLD.8.3, C-GOLD.8.5.10, C-GOLD.8.5.11.; CH04-a: C-7E, C-7E.1.2, C-7E.5.2, C-7E.6.1, C-7E.6.2, C-7E.7, C-7E.8.4, C-7E.13.3. CH04-b: see the exact source-scope and landing table above. |
| F003 | `01_AUTHORITATIVE/cursorrules` | Scoped reread for CH03-o; prior whole-read credit retained where previously recorded | EXCLUDED: coding-process rules under §1.3. NOT PLACED: built-code boundaries belong to store, reader and code-boundary groups. Chapter 3-b: C-READ.1.12 per-store/global-key conflict and C-READ.3 shared write boundary; workflow remains excluded. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB.5.; CH03-k: C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.6.; CH03-l: C-GOLD, C-GOLD.9.; CH03-o: C-INGEST, C-INGEST.4, C-INGEST.4.7, C-INGEST.6. |
| F004 | `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Scoped read in CH04-b: Embedded TSC §§15–16; conflicting inspection and failed-authorization text. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. CH04-b: see the exact source-scope and landing table above. |
| F005 | `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped read in CH04-b: C-TSC and CY-D; component naming and path ownership. Prior read credits retained. | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.3.4; CY-A Chapter 3-b: C-READ component name, operation logging and consumer/caller relationships; CY-A/CY-F interfaces. Chapter 3-c: component ownership/names and Group A/D boundary; accepted A2 supplies behavior. Chapter 3-d: names, Group A ownership and per-reading seam versus full CY-G boundary.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.9.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1.1, C-ENGINE-AB.1.3, C-ENGINE-AB.2.1, C-ENGINE-AB.2.4, C-ENGINE-AB.4, C-ENGINE-AB.6, C-ENGINE-AB.6.1.; CH03-k: C-INDEX, C-INDEX.2, C-INDEX.3, C-INDEX.5, C-INDEX.6, C-INDEX.6.1, C-INDEX.6.2, C-INDEX.6.3, C-INDEX.6.4, C-INDEX.6.5, C-INDEX.6.6.; CH03-l: C-GOLD, C-GOLD.4, C-GOLD.4.6, C-GOLD.6, C-GOLD.6.2, C-GOLD.7, C-GOLD.7.1, C-GOLD.7.2, C-GOLD.7.3, C-GOLD.7.4.; CH03-o: C-INGEST, C-INGEST.4.4, C-INGEST.4.7, C-INGEST.5, C-INGEST.5.1, C-INGEST.5.2, C-INGEST.5.3, C-INGEST.5.4, C-INGEST.6.; CH03-p: C-DETECT, C-DETECT.1, C-DETECT.1.1, C-DETECT.1.2, C-DETECT.1.3, C-DETECT.2, C-DETECT.2.1, C-DETECT.2.2, C-DETECT.2.3, C-DETECT.2.4, C-DETECT.2.5, C-DETECT.3, C-DETECT.3.1, C-DETECT.3.3, C-DETECT.3.4, C-DETECT.3.6, C-DETECT.4, C-DETECT.4.1, C-DETECT.4.1.1, C-DETECT.4.1.2, C-DETECT.4.2.; CH04-a: C-7E, C-7E.3, C-7E.4, C-7E.5, C-7E.5.2, C-7E.6.1, C-7E.6.4, C-7E.7, C-7E.8, C-7E.11, C-7E.13, C-7E.13.1, C-7E.13.2, C-7E.13.3, C-7E.13.4, C-7E.13.5, C-7E.13.6, C-7E.13.7. CH04-b: see the exact source-scope and landing table above.  CH04-c: scoped read; exact scope and placement in the current source table.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
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
| F024 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F025 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F026 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F027 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F028 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F029 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F030 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F031 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
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
| F046 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F047 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
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
| F061 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-b: exact read scope and placement in the current source table; prior credits retained. |
| F062 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained. |
| F063 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained. |
| F064 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1 and cited sub-parts; C-7B.7.4.7 and cited sub-parts; C-7B.7.5.3 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained. |
| F065 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F066 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F067 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3.  CH05-b: exact read scope and placement in the current source table; prior credits retained. |
| F068 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1.6 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.  CH05-b: exact read scope and placement in the current source table; prior credits retained. |
| F069 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F070 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_CANDIDATE_v1_4.md` | Carried through Chapter 3-a: Not yet read; whole file newly read in Chapter 3-b | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-b: EXCLUDED: status/consolidation and workflow narrative under §1.3. Used for locating later accepted owners only; it supplies no behavior in this piece.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F071 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F072 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F073 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F074 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F075 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F076 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F077 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F078 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F079 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | Scoped read in CH04-b: §5 paths 3–4; authority owner/limit cross-check. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F080 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F081 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-d: exact read scope and placement in the current source table; prior credits retained. |
| F082 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-d: exact read scope and placement in the current source table; prior credits retained. |
| F083 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for Bundle 6 mechanics; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained. |
| F084 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped read in CH04-b: §3 held/sealed restrictions and privacy precedence. Prior read credits retained. | Chapter 3-a: C-STORE.5 / operation protections, B17, B20, B21; other component scopes NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: C-7E, C-7E.2, C-7E.8, C-7E.9.1, C-7E.11, C-7E.12. CH04-b: see the exact source-scope and landing table above.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F085 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for Origin policy; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained. |
| F086 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Scoped reread for CH04-a; prior whole-read credit retained where previously recorded | Chapter 3-a: C-STORE.5 / Origin preservation policy; A3.4–A3.5 and other components NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: Navigation excerpt only; no new behavior sourced in this piece.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.7, C-ENGINE-AB.8.; CH04-a: C-7E.12.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
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
| V10-H033 | ### §7G CREATION-AWARE MODE  [SETTLED CONCEPT — NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-d: C-14 and explicit shared/deferred owners.  CH05-a: C-7G and explicit shared/deferred owners. |
| V10-H034 | ## 7H. REREAD LIFECYCLE  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ reread output relationship; detailed orchestration remains with C-7H. |
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
| V10-H072 | ## 14. THE CHAT FRONT DOOR  [PARTIALLY SETTLED, PARTIALLY OPEN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading.  CH04-c: live-loop surface and model boundary in C-13; remaining chat/model internals retain their later owners.  CH04-d: C-14 and explicit shared/deferred owners. |
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
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: §7F complete; §7G-A mode/worker rules consumed through current CH05-b ownership and their exact source headings. | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped: Complete C-7F, C-INDEX, C-ENGINE-C, C-7G, C-7GA, C-13 entries and CY-A/CY-B sequences. | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md` | Whole: Complete B1 file, structural fields, ceilings, boundaries and opens; workflow/self-audit excluded. | `da0aa4d22d6bc6554196c15b2c81b5541018a1e01bfbce367d7cf8e623b6a753` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md` | Whole: Complete A4 policy, mandatory fields, authorization, honest failure and open boundaries. | `c754b27e44cdb578e1cc25e7de681c9d2afd68fedc6e974cc45c8aa6c83d553f` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Scoped: §§0–6 and 13–14 complete, including every RM-CR-01 item and shared declaration/uncertainty/logging/failure framework. Other consumer declarations and remaining sections not credited. | `b2a5b3fbea75f7123a16c8a45c0fb096f4c4565585a4a0c7b7709e70f27d000e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md` | Whole: Complete status/identity receipt only. | `6c21ea024a7202fbb8182e52c2cf8dbe71e6491b8b2813288b4631ee0206677c` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md` | Whole: Complete status/identity receipt only. | `f9d3fe049d2a77b19039f498b1f611159355a3bb60acbf083b72fe3368044e62` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Whole: Complete receipt; accepted foundation identity and scope evidence only, not a substitute for excluded foundation mechanics. | `0b2f0ecfd121423ed2c3dfe833d9ca922f3b366e64353f94bcaf59aa109e6db6` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: Complete receipt, source identities, accepted formal-declaration status and its own conditional audit gate; no unobserved receipt PASS inferred. | `faa88d9c991b2e4058081717a4fcbeb5a8e27d62e0f484ae6051fc061a03bac1` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped: §8 B18 complete for the existing reliable-reference incoming seam only; full records remain CH04-d. | `bc1095955525fcea56cb4d16057c93bfb15eec42a83a1b644baf0e87a473f64e` |

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

### READ-folder files not yet read whole

75 inherited pending files remain. Scoped reads do not remove whole-file obligations; previous read credits and source placements remain.

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
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md`
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
§1.3 no history/actions/roles/workflow in this chapter: PASS — 125 behavior cards reviewed; 0 project/workflow hits. Source-status and scope notes are outside the behavior cards.
§1.4 every gap written as NOT DECIDED: PASS — 391 empty fields/cells exactly match the register; 11 additional implementation slots are explicit.
§1.5 conflicts marked, none resolved: PASS — 0 explicit conflict-register rows. No direct contradictory current behavior was silently resolved. Explicit scope distinctions retain the accepted-but-excluded foundation location, earlier open slots versus accepted declaration content, roots-only RM-CR-01 versus broad prior-reading context handoff, new-root trigger restrictions versus four conceptual categories, and generic degradation versus retrieval-specific stop. The receipt's own conditional audit gate is preserved without an invented receipt PASS.
§3 exactly one stamp per line: PASS — 125 headers, 845 populated fields and 246 USED BY rows checked; 0 BUILT field lines. Relationship stamps follow the named card.
§4 every behavior line cited in the exact format: PASS — 66 distinct current citations resolve at the pin; all populated fields and relationship rows are cited. Claims were reviewed against the mapped source sections.
§5.4 one name per thing: PASS — 125 current IDs checked for duplicates, prior collisions and exact official names; shared atoms retain their previous names.
§6 all template fields present, in order, for every part: PASS — 125 templates and 1236 field lines checked.
§6.3 reciprocity within this chapter: PASS — 181 internal lines cover 181 reciprocal pairs; 12 external-use continuations and 9 incoming continuations name both endpoints; 4 further outgoing lines are answered directly by the named cards' own USED BY rows.
§6.4 every decided detail written in, no citation used in place of content: PASS — All permitted mapped retrieval content is written: both channel meanings and conflict/prompt separation; four conceptual combinations; every B1 configuration field and provenance element, required declaration binding and validity; every per-run audit field and per-item provenance element; ceiling identity/version, bounded quantity coverage, minimum precedence, configuration rejection, runtime enforcement and version-only change; all thirteen RM-CR-01 declaration items, four gates, six dimensions and producers, five recorded link types, three excluded dimensions, no mouth authorization, on-demand timing, channel-specific ordering, four strength labels, theme influence, uncertainty states, logging, use and fail-closed boundaries; four failure classes, full genuine-empty record requirements and eight empirical-test dimensions. The exact B26 foundation mechanics unavailable under the contract's source-folder rule are explicitly excluded from completeness credit, not called undesigned. General B9 and shared relevance schemas have precise later owners.
§6.5 sub-parts recursed to the bottom: PASS — 124 declared child/shared references and 125 owned cards checked; 37 explicit steps have 0 empty TOGETHER cases. Identity, configuration, provenance and audit structures recurse to named fields; gates and dimension/link types are distinct; healthy-empty provenance and failure classes have separate cards; all eight test dimensions are distinct. The mode identity/configuration version and eight declaration-field owners are reused through explicit shared references rather than duplicated meanings. Labels with no further supplied mechanism remain literal values; no threshold-to-label mapping is invented.
§9 coverage matrix rows added for every file used: PASS — 10 current source identities, 145 READ-folder inventory rows and 107 V10 heading rows checked; 145 named source paths exist at the pin. Earlier credits and placements remain cumulative.
§10.11 no recommendation, no sentence addressed to Ness: PASS — the behavior was reviewed as system operation and boundaries; 0 formula phrases and 0 project/workflow hits.
Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`.

Computed self-check output:

| Check | Count |
|---|---|
| cards | 125 |
| field_lines | 1236 |
| populated_fields | 845 |
| not_decided_boxes | 391 |
| not_decided_fields_and_cells | 391 |
| used_by_rows | 246 |
| relationships | 197 |
| internal_relationships | 181 |
| external_relationships | 16 |
| internal_use_pairs | 181 |
| external_use_pairs | 16 |
| used_by_continuation_rows | 12 |
| incoming_continuation_rows | 9 |
| plain_gates | 0 |
| step_cards_with_empty_together | 0 |
| explicit_step_cards_checked | 37 |
| unique_citations | 66 |
| resolved_citations | 66 |
| named_source_paths_checked | 145 |
| source_identities | 10 |
| whole_read_files | 6 |
| earlier_identities | 26 |
| pending_source_paths | 75 |
| built_field_lines | 0 |
| misfiled_scan_fields | 1236 |
| misfiled_scan_used_by_cells | 738 |
| empty_restriction_failure_gate_boxes | 170 |
| formula_hits | 0 |
| wording_hits | 2 |
| wording_verbatim_exceptions | 2 |
| wording_actionable_hits | 0 |
| project_workflow_hits | 0 |
| path_use_rows | 3 |
| path_covered_cards | 125 |
| subpart_references_checked | 124 |
| v10_heading_rows_checked | 107 |
| read_folder_files_covered | 145 |
| source_names_checked | 39 |
| errors | 0 |
| additional_undecided_slots | 11 |
| explicit_source_conflict_records | 0 |

The 1,236 fields and 738 USED BY cells were reviewed against the full mapped source sections, including 170 empty restriction/failure/gate boxes. Operational channel, gate, ceiling, ordering, uncertainty, failure and test steps link their actual governing rules. Atomic identity/timestamp/value carriers retain empty independent recovery where none is supplied. No BUILT line is asserted. All three root path placements and the nine existing incoming uses are explicit. The prior-reading incoming seam is recorded without admitting prior readings to the root-only declaration. The accepted B26 policy is taken from the permitted formal-declaration text, not reconstructed from receipt summaries.

Two source-verbatim wording exceptions remain in inherited coverage: the A29 closure filename has a space before its extension (line 3611), and V10 heading 15 contains the literal dot-prefixed cursorrules name (line 3734). No actionable wording flags remain.

All 26 earlier completed fingerprints were rechecked and are listed in full. The final count table is compared against a recount after this block is appended. No earlier chapter, repository source or runtime code is changed.
