# Chapter 4-a — Group B: C-7E

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH04-a.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`

This piece covers Catalog capture and eligibility, the intake envelope, pre-ingest records and lifecycle, speaker and thread resolution, enrichment, held-content boundaries, the accepted root-write handoff and Catalog operation records. The existing envelope-field, speaker-rule, B11, alias and future-schema cards retain their IDs. TSC's complete transactional design belongs to CH04-b. BOP capture internals and reaction-window mechanics belong to CH08-d, and OOP to CH08-e; this piece records their common Catalog entry only.

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Every citation resolves at the pinned commit.

[SOURCE CONFLICT] Decision Defaults §3N permits private TSC inspection through `tsc_inspection:<session_id>`. V10 §7E-TSC §15 explicitly supersedes that mechanism and prohibits inspection, including by Ness. The V10 prohibition governs this piece; the conflicting Defaults text remains recorded.

[SOURCE CONFLICT] V10 §7E's reference to writing a root to the sealed store and V10 §6A's future seal-removal route remain in tension with accepted B11/Bundle 6's never-reopen historical-batch boundary. The existing seal conflict is preserved. The accepted new-root path described here targets B11's separate active writable batch; it does not rewrite V10 or authorize reopening the 5,521-root batch.

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` identifies the exact accepted source filename. Acceptance receipts are listed in READ RECORD. No behavior in this piece is stamped BUILT.

<!-- BEGIN BEHAVIOR -->

### C-7E — Catalog Front Door + pre-ingest holding (§7E)
Stamp: DESIGNED    Source: [V10 §7E] [MAP C-7E]

ALONE
- What it is: DESIGNED — The DUMB Catalog boundary separating raw capture from eligibility for root ingestion. [V10 §7E / TWO GATES] [MAP C-7E]
- Takes in: DESIGNED — Captures from every front door, each with the minimum intake envelope and any reliable source-derived catalog facts already known. [V10 §7E / MINIMUM INTAKE ENVELOPE] [MAP C-7E]
- Does: DESIGNED — Captures and normalizes identifiable material, evaluates catalog completeness, manages resolution and holding, then promotes only eligible material without duplicate roots. [V10 §7E / DESIGN BOUNDARY] [V10 §7E / PRE-INGEST HOLDING AREA]
- Gives out: DESIGNED — Pre-ingest records and, after eligibility is resolved, promoted roots; the pre-ingest record remains as provenance with the resulting `root_id`. [V10 §7E / PRE-INGEST HOLDING AREA]
- Gives out: ACCEPTED — Prepared root payloads and committed upstream evidence references through the B11 active-writable-batch seam, receiving its durable caller outcome and owning `batch_id` [proposed]. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.1] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13]
- Must never: DESIGNED — Interpret meaning, guess missing catalog fields, rewrite raw capture, silently drop malformed material, or destroy raw material merely because a field is unresolved. Excluded content follows the separate privacy-protected boundary. [V10 §7E / TWO GATES] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE] [V10 §7E / D. Semantic interpretation]
- Fails closed by: DESIGNED — Sends a malformed capture to the explicit capture-error path with available material preserved; holds unresolved items without blocking unrelated ready items. [V10 §7E / DESIGN BOUNDARY] [V10 §7E / PRE-INGEST HOLDING AREA]

TOGETHER
- Fed by: DESIGNED — C-14 — Chat Front Door (§14): supplies live-chat captures to the common intake boundary. [MAP C-7E]
- Fed by: DESIGNED — C-8 — Research Pipeline / Knowledge Catcher (§8): supplies eligible research-side captures through its Catalog entry. [MAP C-7E]
- Fed by: DESIGNED — C-9A — Image ingest front door (§9A): supplies image captures with the same minimum envelope. [MAP C-7E]
- Fed by: DESIGNED — C-23 — Mobile App, three modes (§23): supplies mobile front-door captures. [MAP C-7E]
- Fed by: DESIGNED — C-TSC — Temporary Session Cache (§7E-TSC): organizes session-held material inside the shared pre-ingest store and supplies authorized items through the Catalog path. [MAP C-7E] [DD §3N]
- Fed by: ACCEPTED — C-BOP — Behavioral Observation Processing (§25.1/§26): routes authorized observation captures through this single Catalog entry, never through a second root-writing path. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fed by: ACCEPTED — C-OOP — Outcome Observation Processing (§26): routes `outcome_observation` roots through the same Catalog entry. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13]
- Fed by: DESIGNED — C-DETECT — Speaker detector (fallback; investigated, not deployed) (§11): supplies an uncertain candidate only when source attribution is absent. [MAP C-DETECT]
- Fed by: DECIDED-2026-09-24 — C-7B.9.4 — File door: Wonder material submitted for re-entry: receives it only as fresh raw input through the front door. [DR §4] [98/sources/NH_MASTER-14_FINAL.md §7B / Part 6.5] [MAP C-7E]
- Gated by: DESIGNED — C-7E.1 — Separate capture and ingestion gates: raw capture does not establish root eligibility. [V10 §7E / TWO GATES]
- Gated by: DESIGNED — C-7E.2 — Minimum intake envelope: all seven required elements must be present before pre-ingest accepts a capture. [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Gated by: DESIGNED — C-7E.4 — Privacy and exclusion precedence: only eligible non-excluded material remains in the ordinary Catalog path. [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]
- Gated by: DESIGNED — C-7E.9 — Enrichment categories: only source facts, mechanical derivations and explicitly unsettled proposals belong in Catalog. [V10 §7E / FOUR ENRICHMENT CATEGORIES]
- Gated by: DESIGNED — C-7E.11 — Held-content access boundary: held raw content stays outside downstream semantic use. [MAP C-7E]
- Gated by: DESIGNED — C-7E.13 — Catalog operation records: each specified capture, blocker change, promotion, exclusion and capture-error must be recorded. [MAP C-7E]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture exclusions apply before ordinary root storage (P-MAIN step 2). [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE] [V10 §7Q / CAPTURE EXCLUSION — TWO-LAYER SYSTEM]
- Gated by: DESIGNED — C-7B.8.4 — Live catalog exception: permits the catalog to ask Ness for required capture clarification. Unattended unresolved speaker or thread remains held rather than guessed (CY-B). [V10 §7B] [V10 §7E] [MAP CY-B]
- Changes: DESIGNED — C-7E.5 — Unified pre-ingest record: preserves each capture at its stable location while metadata and resolution develop around it. [V10 §7E / PRE-INGEST HOLDING AREA]
- Changes: ACCEPTED — C-STORE — Accretive store & sealed roots (§6B): submits eligible roots only through the shared B11/`append_root()` boundary into its active writable batch. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7A — Universal Filter (§7A) | A front-door capture with source material and catalog information. | Checks catalog eligibility before material enters the continuous reader. | Only eligible promoted material proceeds into semantic reading; unresolved raw content remains held. | [MAP C-7E] [V10 §7E / TWO GATES] |
| 2 · ACCEPTED | C-7B.7.1.5 — Automatic hold handling | New material voluntarily supplied through a governed front door. | Applies normal intake gates; the separate hold-release interface still requires a bound release-evidence record. | New evidence enters through the governed channel without turning holds into a manual review queue. | [04/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md §3] [04/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md §4] |
| 3 · DESIGNED | C-7B.8 — Unfillable-web handling | A live capture requiring speaker or grouping clarification. | May ask Ness under the specific live catalog rules. | Preserves unresolved material until its actual catalog requirement is resolved. | [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] |
| 4 · DESIGNED | C-7B.10.8.5 — TSC blocker condition | TSC-held material with governing authorization and blockers. | Requires those conditions to clear through the normal catalog path before downstream use. | Keeps held material inaccessible to the Meaning Engine, LMAC and context retrieval. | [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY] |
| 5 · ACCEPTED | C-STORE — Accretive store & sealed roots (§6B) | A prepared root payload, committed eligibility/authority/blocker evidence references and stable capture identity. | Supplies them through the B11 ingestion seam after catalog eligibility has been established. | Receives the durable outcome and root identity with owning batch; no sealed historical root is reopened. | [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.1] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13] |
| 6 · ACCEPTED | C-STORE.5.2.10 — Privacy precedence | Held pre-ingest material and its protected-boundary state. | Keeps the held-material boundary binding under privacy-before-relevance operation protections. | No downstream semantic access is gained merely by preserving the material. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| 7 · DESIGNED | C-DETECT — Speaker detector (fallback; investigated, not deployed) (§11) | Role-less source material and the detector's returned candidate. | Invokes the fallback proposer only without source attribution and receives its output as uncertain metadata. | The candidate does not directly write role or clear unresolved-speaker eligibility. | [MAP C-DETECT] [V10 §7E / SPEAKER RESOLUTION RULE] |
| 8 · DESIGNED | C-DETECT.2 — Settled speaker rule | A capture whose speaker may still be unresolved. | Allows raw capture but requires resolved speaker information before root ingestion. | Unresolved material remains in holding. | [V10 §7E / SPEAKER RESOLUTION RULE] |
| 9 · DESIGNED | C-DETECT.2.4 — Unattended speaker hold | Unattended material with unresolved speaker. | Retains the speaker_unresolved hold. | No root ingestion occurs solely on the detector's proposal. | [V10 §7E / SPEAKER RESOLUTION RULE] |
| 10 · DESIGNED | C-DETECT.3 — Speaker proposal contents | Speaker proposal information with provenance, uncertainty and confirmation status. | Keeps proposal metadata around the unchanged raw capture. | The raw source is not rewritten and the candidate is not silently promoted to fact. | [V10 §7E / C. Machine-inferred classifications] [V10 §7E / The raw captured payload] |
| 11 · DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E); P-MAIN (step 1) | Raw front-door material and its source provenance. | Captures the intake envelope and checks catalog completeness, speaker and grouping before root ingestion. | Identifiable captured material awaits only actually unresolved catalog requirements. | [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / TWO GATES] |
| 12 · DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E); P-MAIN (step 3) | Captured material and its remaining blockers. | Holds unresolved material outside the Meaning Engine; only blocker-free material progresses through ready and promoting. | Unrelated ready items keep moving; promoted records retain root_id provenance. | [V10 §7E / PRE-INGEST HOLDING AREA] [V10 §7E / LIFECYCLE STATES] |
| 13 · DESIGNED | C-TSC.5.17 — content_hash | The raw content as captured. | Retains the raw payload whose capture-time hash is recorded. | Nothing in this card. | [V10 §7E-TSC / 2. Relationship to §7E] [V10 §7E-TSC / 5. Contribution Record Schema] |
| 14 · ACCEPTED | C-OOP.8.5 — Unauthorized outcome source refusal | The actual source authorization result. | Gates this place: source/capture admission. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 15 · DESIGNED | C-TSC.10.10 — promoted_root_id | The successful append result. | Returns the successful root identifier through its normal append route. | Nothing in this card. | [V10 §7E-TSC / 17. Exact Promotion Sequence] |
| 16 · DESIGNED | C-TSC.12.2.3 — promoting | An eligible item proceeding through Catalog validation and root append. | Gates this place: intake fields and speaker attribution must resolve before append. | Nothing in this card. | [V10 §7E-TSC / 17. Exact Promotion Sequence] |
| 17 · DESIGNED | C-7O.5.2 — Result root reference | The result material after ordinary root checks. | Gates this place: standard root-ingestion checks govern entry. | Nothing in this card. | [V10 §7O] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.2] |
| 18 · DESIGNED | C-TSC.7.12 — Unresolved-speaker hold | An unresolved speaker and the session fingerprint requirement. | Gates this place: its speaker-resolution rule must clear the remaining hold. | Nothing in this card. | [V10 §7E-TSC / 7. Attribution Certainty and Unresolved-Speaker Handling] |
| 19 · ACCEPTED | C-TSC.28.8 — Unconfirmed Catalog acceptance | The Catalog submission response and original derived capture identity. | Gates this place: owns acceptance and its intake checks. | Nothing in this card. | [V10 §7E-TSC / 17. Exact Promotion Sequence] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §10] |
| 20 · DESIGNED | C-TSC.25.2 — Exclusion after pre-ingest | The privacy exclusion decision and existing pre-ingest record. | Holds the existing capture record retained as handling history. | Nothing in this card. | [V10 §7E-TSC / 25. Privacy, Exclusion, Restriction, Deletion, and Third-Party Handling] |
| 21 · DESIGNED | C-TSC.5.7 — role | NOT DECIDED | Gates this place: its speaker-resolution rule must settle the promoted role before root writing. | Nothing in this card. | [V10 §7E-TSC / 7. Attribution Certainty and Unresolved-Speaker Handling] |
| 22 · DESIGNED | C-13 — Live Loop (§13) | A live conversation turn, captured material, permitted memory and the model layer's search and wording functions. | Supplies capture and pre-ingest holding. | Nothing in this card. | [MAP C-13] |
| 23 · ACCEPTED | C-TSC.17.8.2 — Pre-ingest submission interface | `item_promotion_operation_id` [proposed], `preingest_capture_id`, derived `capture_id`, and accepted structural source metadata. | Gates this place: owns envelope validation and acceptance. | Nothing in this card. | [V10 §7E-TSC / 17. Exact Promotion Sequence] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7] |
| 24 · ACCEPTED | C-TSC.17.8.3 — Root-append interface | `capture_id`, validated root fields and B11 `ingest_operation_id` [proposed]. | Supplies the validated root through its own internal append path. | Nothing in this card. | [V10 §7E-TSC / 29. Integration Boundaries] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7] |
| 25 · ACCEPTED | C-23.5.3 — Mobile root-entry caller contract | Seven-field root payload, eligibility/authorization/blocker-clearance references, stable ingest-identity basis per sync item, and source provenance labels. | Gates this place: owns the sole ordinary intake envelope. | Nothing in this card. | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13] |
| 26 · ACCEPTED | C-STORE.5.2.9 — Single ingest boundary | NOT DECIDED | Gates this place: every root-producing path passes the catalog and the B11 active writable batch, using B11's registry, claim, ownership and fence records unchanged. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| 27 · DESIGNED | C-TSC.10 — N.H output record | `output_id` (uuid4), `session_id` (foreign key), `sequence_position` (integer interleaved with contributions), `produced_at` (timestamp), `output_type` (`text_response`, `voice_response`, `action_result`, `translation_output`, `system_message`), `addressed_to_stream_id` (uuid4 or null), `access_level_at_output` (`top_security`, `recognized_ness`, `known_person`, `guest`), `preingest_capture_id` (uuid4), `item_lifecycle_status` (`held`, `ready`, `promoting`, `promoted`, `excluded`), and `promoted_root_id` (uuid4 or null). | Stores the output's raw payload at its stable capture identity. | Nothing in this card. | [V10 §7E-TSC / 10. N.H Output Preservation] |
| 28 · DESIGNED | C-TSC.9.1.3 — bop_preingest_capture_id | NOT DECIDED | Supplies the existing held observation's capture identity. | Nothing in this card. | [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling] |
| 29 · ACCEPTED | C-LMAC.13.1 — Unpromoted pre-ingest and TSC blocker boundary | The item’s actual lifecycle, active blockers and any safe source-carried metadata. | Supplies lifecycle and blocker ownership. | Nothing in this card. | [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY] [V10 §7G-A / LMAC AND THE CONTINUOUS MECHANISM CONNECTION] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md §9] |
| 30 · ACCEPTED | C-ENROLL.8.2 — Catalog submission interface | `{ frozen capture_ids, provenance }` after committed close/interruption. | Gates this place: owns accepted/rejected/blocked intake truth. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 31 · ACCEPTED | C-STORE.4.12 — Interface and caller/callee wiring matrix | Every producer through its catalog-side path and the read-side structural consumers. | Supplies every producer's prepared root payload and committed upstream evidence through the catalog-side path. | Nothing in this card. | [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13] |
| 32 · ACCEPTED | C-7B.9.7.4.1 — Envelope-only root entry | Selected Wonder material that is to enter a root store. | Gates this place: the §7E envelope is the only entry into root stores. | Nothing in this card. | [04/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md §4] [04/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md §9] |
| 33 · DESIGNED | C-TSC.1 — Session holding boundary | Captured session material already resident in Catalog pre-ingest. | Supplies what this place relies on: the raw captures stay in this shared holding area. | Nothing in this card. | [V10 §7E-TSC / 1. What TSC Is and Is Not] |
| 34 · DESIGNED | C-TSC — Temporary Session Cache (§7E-TSC) | Third-party contributions, Ness's contributions, N.H outputs, links to held BOP observation captures and references to SIA assessment events. | Supplies what this place relies on: raw conversation and BOP payloads live in its pre-ingest records from capture onward, with structural references here. | Nothing in this card. | [V10 §7E-TSC / 2. Relationship to §7E] |
| 35 · DESIGNED | C-9.2.4 — Sensor and front-door handoff | Transcribed input. | Gates this place: ordinary intake acceptance and blockers. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] [V10 §9] |
| 36 · DESIGNED | C-TSC.11 — Blockers and resolution history | `blockers`: `blocker_id` (uuid4), `session_id` (foreign key), `item_id` (uuid4), `item_type` (`contribution`, `nh_output`, `bop_root`, `session`), `blocker_type` (`pending_fingerprint_authorization`, `speaker_unresolved`, `content_under_review`, `technical_hold`), `added_at` (timestamp), `status` (`active`, `resolved`, `waived_by_exclusion`), `resolved_at` (timestamp or null), `resolution_method` (string or null), `resolution_event_ref` (uuid4 or null). | Gates this place: speaker resolution follows its rule and cannot be performed by TSC logic. | Nothing in this card. | [V10 §7E-TSC / 11. Blocker Schema and Blocker-Resolution History] |
| 37 · DESIGNED | C-BOP.6 — observation_quality | Signal quality, its note, per-field completeness and overall completeness. | Gates this place: held/ingestion gates still apply. | Nothing in this card. | [V10 §25.1] |
| 38 · ACCEPTED | C-STORE.4.6.1 — Position of the seam | Seven-field payload. | Supplies the seven-field payload and the committed capture-authorization, exclusion, blocker-clearance, speaker-resolution and catalog-eligibility evidence. | Nothing in this card. | [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.1] |
| 39 · DESIGNED | C-9.2 — Voice input and output pipeline | Microphone input and material intended for spoken output. | Takes this place's change: input uses the normal front door. | Input uses the normal front door. | [MAP C-9] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 40 · DESIGNED | C-BOP — Behavioral Observation Processing (§25.1/§26) | Available authorized voice, confirmed sent text, interface and session events, and explicitly authorized imported content. | Gates this place: capture/ingest gate and held-material boundary. | Nothing in this card. | [V10 §25.1] [V10 §7E] |
| 41 · DESIGNED | C-7L — Person-Boxes (§7L) | Roots where the person appears, is mentioned or quoted, readings and tellings in any perspective role, themes with confirmation status, clashes, relevant Ness response events, other Person-Boxes with proposed or confirmed identity connections, and permitted metadata-only pre-ingest references. | Supplies authorized source references and source-carried attribution. | Nothing in this card. | [MAP C-7B] [MAP CY-A] [MAP C-7L] |
| 42 · ACCEPTED | C-BOP.13 — Accepted single-path observation ingestion | Authorized typed captures with the unchanged legacy subject and stable capture identity. | Gates this place: the one catalog envelope. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 43 · DESIGNED | C-LEARN.6.5.1 — Change logging through the shared observation path | The actual change and its operational evidence. | Supplies the Catalog. | Nothing in this card. | [V10 §26.9] |
| 44 · DESIGNED | C-TSC.17 — Ordered promotion | An authorized session, current security conditions, privacy classifications, blockers and the captured session ordering. | Takes this place's change: clears the authorized fingerprint blocker and supplies structural `source_metadata` before the normal Catalog writer path. | Clears the authorized fingerprint blocker and supplies structural `source_metadata` before the normal Catalog writer path. | [V10 §7E-TSC / 17. Exact Promotion Sequence] |
| 45 · DESIGNED | C-9A.5 — Image Catalog handoff | Stable unique `capture_id`, exact raw payload or stable immutable reference, capture timestamp, front-door/source type, payload format/media type, source-provided metadata without reinterpretation, and traceable capture provenance. | Gates this place: capture completeness, source attribution, exclusion and root eligibility are Catalog's existing conditions. | Nothing in this card. | [MAP C-7E] [MAP C-9A] |
| 46 · DESIGNED | C-BOP.11.2 — Same-capture write retry | The actual captured observation and its unchanged capture_id. | Supplies the single entry route. | Nothing in this card. | [V10 §25.1] |
| 47 · DESIGNED | C-7O.1.1 — Explicit reported result | The reported result material. | Gates this place: the normal intake and root-ingestion gates must pass. | Nothing in this card. | [V10 §7O] |
| 48 · DESIGNED | C-OOP.4 — Shared-store outcome connection | An authorized raw outcome observation. | Gates this place: the one Catalog entry. | Nothing in this card. | [V10 §26.6] [V10 §26.10] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] |
| 49 · ACCEPTED | C-19.21.2 — Selected Wonder intake protection | Selected Wonder material with identity/authorization and source-carried provenance. | Gates this place: retains the ordinary entry boundary. | Nothing in this card. | [04/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md §4] |
| 50 · DESIGNED | C-7B — Meaning Engine Web Chain, Log, Note, and Wonder Boundary (§7B) | A piece against wide accumulated context. | Supplies eligible material from front doors. | Nothing in this card. | [V10 §7B] [MAP C-7B] [V10 §7E] [V10 §7Q] |
| 51 · ACCEPTED | C-7O.9.4 — Outcome-observation normal-entry boundary | Permitted outcome_observation material about what happened after a function acted. | Gates this place: the single intake path and standard root checks apply before evidence use. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §12] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| 52 · DESIGNED | C-TSC.24.2 — Root-writer idempotency | Stable `preingest_capture_id` and its derived Catalog `capture_id`. | Gates this place: only Catalog's internal path calls the root writer. | Nothing in this card. | [V10 §7E-TSC / 29. Integration Boundaries] |
| 53 · ACCEPTED | C-7Q.11.5 — Front-door and TSC privacy interface | New capture, safe/unsafe separation and the protected hold or storage result. | Takes this place's change: protected front-door routing. | Protected front-door routing. | [04/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md §16] [04/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md §4] |
| 54 · DESIGNED | C-TSC.12.2.6 — blocked | `speaker_unresolved` or another remaining blocker after authorization. | Gates this place: its normal resolution rule must clear the blocker before resume. | Nothing in this card. | [V10 §7E-TSC / 17. Exact Promotion Sequence] |
| 55 · DESIGNED | C-TSC.25.5 — Third-party statements | Captured material with the actual speaker attribution. | Gates this place: speaker resolution must succeed before root writing. | Nothing in this card. | [V10 §7E-TSC / 17. Exact Promotion Sequence] |
| 56 · ACCEPTED | C-9.3.7 — Phone recording transfer boundary | Ness's deliberate send choice, the chosen material and current identity/authorization/privacy/provenance/intake facts. | Gates this place: sole ordinary root-entry envelope. | Nothing in this card. | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] |
| 57 · DESIGNED | C-TSC.10.8 — preingest_capture_id | NOT DECIDED | Supplies the output's held capture identity. | Nothing in this card. | [V10 §7E-TSC / 10. N.H Output Preservation] |
| 58 · DESIGNED | C-OOP.5.1 — outcome_observation Catalog source | The actual typed outcome observation. | Takes this place's change: records the source through its normal envelope. | Records the source through its normal envelope. | [V10 §26.6] |
| 59 · DESIGNED | C-TSC.29 — Integration boundaries | BAI token consumption, queried SACL confirmation, SIA-event references and BOP pre-ingest references. | Gates this place: all payload handling and root ingestion remain on its existing path. | Nothing in this card. | [V10 §7E-TSC / 29. Integration Boundaries] |
| 60 · DESIGNED | C-23 — Mobile App, three modes (§23) | Ness's deliberate requests, locally accumulated phone material and available connectivity. | Takes this place's change: receives eligible mobile captures through the ordinary front door. | Receives eligible mobile captures through the ordinary front door. | [MAP C-7E] |
| 61 · ACCEPTED | C-7L.4 — Ness's confirmed Person-Box | The settled fact that the box exists, clear source-identified Ness material, ambiguous references and later identity evidence. | Supplies source and speaker/thread resolution for material attributed to Ness. | Nothing in this card. | [04/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md §9] [V10 §7E] |
| 62 · ACCEPTED | C-19.21 — Wonder interface and selected-transfer boundary | Only specific Wonder material deliberately selected and deliberately submitted by Ness. | Gates this place: retains the sole ordinary root-entry envelope. | Nothing in this card. | [04/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md §4] |
| 63 · DESIGNED | C-TSC.6.8 — identity_status | NOT DECIDED | Gates this place: unresolved source attribution must pass its speaker-resolution rule before promotion. | Nothing in this card. | [V10 §7E-TSC / 7. Attribution Certainty and Unresolved-Speaker Handling] |
| 64 · DESIGNED | C-TSC.17.2 — Per-item promotion loop | Item disposition, prior `promoted_root_id`, stable capture identity and session source metadata. | Gates this place: validates intake and remaining blockers through its own route. | Nothing in this card. | [V10 §7E-TSC / 17. Exact Promotion Sequence] |
| 65 · DESIGNED | C-TSC.5.9 — preingest_capture_id | The stable identifier of the already-held raw capture. | Owns the referenced capture and its raw payload. | Nothing in this card. | [V10 §7E-TSC / 5. Contribution Record Schema] |
| 66 · DESIGNED | C-BOP.10 — Absolute DUMB and text non-inspection boundary | A proposed observation field or event classification. | Gates this place: the enrichment boundary excludes meaning from capture. | Nothing in this card. | [V10 §25.1] [V10 §26.4] |
| 67 · DESIGNED | C-TSC.18.3 — BOP event interleaving | BOP pre-ingest links and their event times. | Gates this place: validates and promotes the linked BOP record through normal intake. | Nothing in this card. | [V10 §7E-TSC / 17. Exact Promotion Sequence] |
| 68 · DESIGNED | C-TSC.9.1 — BOP pre-ingest link record | `link_id` (uuid4), `session_id` (foreign key), `bop_preingest_capture_id` (uuid4), `linked_contribution_id` (uuid4 or null), `occurred_at` (timestamp), `event_type` (string identifying the BOP event type), and `relationship_type` (`concurrent`, `precedes_contribution`, `follows_contribution`, `session_level`). | Supplies the BOP observation's held capture identity. | Nothing in this card. | [V10 §7E-TSC / 9. BOP and SIA Event-Link Handling] |
| 69 · ACCEPTED | C-ENROLL.8 — Closed-session root and reading handoff | Committed observations and a committed session-close or interruption fact. | Gates this place: ordinary intake acceptance. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |
| 70 · ACCEPTED | C-TSC.17.7.4 — After Catalog acceptance | Catalog's own pre-ingest lifecycle and the original derived `capture_id`. | Supplies what this place relies on: its committed pre-ingest lifecycle is the intake truth. | Nothing in this card. | [V10 §7E-TSC / 17. Exact Promotion Sequence] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §5.4] |
| 71 · DESIGNED | C-OOP.2.4 — Correction timing and relationship observation | The correcting message and actual timing/relationship facts. | Takes this place's change: the conversational message and observation each use their normal source path. | The conversational message and observation each use their normal source path. | [V10 §26.6] |
| 72 · DESIGNED | C-LEARN.1 — Shared learning responsibilities and ownership | Authorized-session evidence. | Supplies the only Catalog front door. | Nothing in this card. | [V10 §26.1] |
| 73 · DESIGNED | C-14 — Chat Front Door (§14) | Every live-chat message, including Ness's words and N.H's earlier output with its source-carried speaker. | Gates this place: requires standard Catalog capture, privacy, speaker, grouping and root-ingestion eligibility. | Nothing in this card. | [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] [MAP C-14] |
| 74 · DESIGNED | C-TSC.19 — Partial promotion and idempotency | Each item's stable `preingest_capture_id` and any existing `promoted_root_id`. | Gates this place: all root writes use its internal `append_root()` route and idempotency key. | Nothing in this card. | [V10 §7E-TSC / 29. Integration Boundaries] |
| 75 · DESIGNED | C-7O.1.1.1 — Reported-result normal root-entry boundary | A result report at a normal front door. | Gates this place: ordinary capture/root eligibility and blockers govern entry. | Nothing in this card. | [V10 §7O] |
| 76 · ACCEPTED | C-TSC.17.8.2.2 — Catalog acceptance result | NOT DECIDED | Owns the acceptance decision. | Nothing in this card. | [V10 §7E-TSC / 17. Exact Promotion Sequence] [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7] |
| 77 · DESIGNED | C-TSC.7 — Attribution assessment | `assessment_id` (uuid4), `session_id` and `stream_id` (foreign keys), `contribution_id` (foreign key or null), `assessed_at` (timestamp), `assessed_person_box_id` (uuid4 or null), `assessed_certainty` (float from 0.0 through 1.0), `certainty_dimensions` (JSON object), `uncertainty_flags` (JSON array), `anti_spoofing_suspicion_level` (`none`, `low`, `medium`, `high`), and `sia_assessment_event_id` (uuid4). | Gates this place: only its speaker-resolution rule can clear `speaker_unresolved`; neither another fingerprint nor manual selection of an identity is required by TSC. | Nothing in this card. | [V10 §7E-TSC / 7. Attribution Certainty and Unresolved-Speaker Handling] |
| 78 · ACCEPTED | C-STORE.4.1.4 — Capture and eligibility separation | NOT DECIDED | Gates this place: valid committed upstream capture, eligibility, authorization and blocker evidence is present. | Nothing in this card. | [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.1] |
| 79 · ACCEPTED | C-OOP.8.6 — Outcome held-material and privacy boundary | The current source lifecycle, blockers and authorization. | Supplies source holding lifecycle. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| 80 · DESIGNED | C-TSC.29.4 — BOP reference boundary | `bop_preingest_capture_id` in `bop_preingest_links`. | Holds the linked BOP capture. | Nothing in this card. | [V10 §7E-TSC / 29. Integration Boundaries] |
| 81 · DESIGNED | C-SIA.11.6 — Completed reading path for training | The acoustic root's §7E → §7G processing state. | Supplies normal intake processing. | Nothing in this card. | [V10 §25.3 / Training Eligibility Rules] |
| 82 · DESIGNED | C-TSC.3 — Transactional structural store | Structural rows in `sessions`, `contributions`, `participants`, `attribution_assessments`, `branch_links`, `bop_preingest_links`, `sia_event_links`, `nh_outputs`, `blockers`, `blocker_history`, `lifecycle_events`, `promotion_state` and `security_audit_refs`. | Provides the stable pre-ingest references; raw payloads remain there. | Nothing in this card. | [V10 §7E-TSC / 2. Relationship to §7E] |
| 83 · DESIGNED | C-TSC.29.5 — Catalog promotion boundary | Authorized eligible item, its pre-ingest record and structural source metadata. | Gates this place: owns envelope validation, speaker resolution and the internal append path. | Nothing in this card. | [V10 §7E-TSC / 29. Integration Boundaries] |
| 84 · DESIGNED | C-TSC.17.8.2.1 — Structural source metadata | `sequence_position`, `occurred_at`, `contributor_stream_id`, `session_id` and branch relationship. | Takes this place's change: receives structural data in its pre-ingest source metadata. | Receives structural data in its pre-ingest source metadata. | [V10 §7E-TSC / 17. Exact Promotion Sequence] |
| 85 · DESIGNED | C-14.1 — Automatic live-turn capture | Each message and its actual source metadata. | Takes this place's change: supplies automatic live captures through the ordinary Catalog boundary. | Supplies automatic live captures through the ordinary Catalog boundary. | [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] [MAP C-14] |
| 86 · ACCEPTED | C-8.13 — Research isolation architecture | Outside research material and the source-preservation artifacts. | Takes this place's change: only authorized queue exit reaches Catalog through the normal engine path. | Only authorized queue exit reaches Catalog through the normal engine path. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §5] |
| 87 · DESIGNED | C-TSC.2 — Shared Catalog holding | Catalog records containing `capture_id`, raw payload, capture timestamp, front-door type, source metadata, proposed catalog fields, blockers, resolution history, lifecycle state and a resulting `root_id` when promoted. | Supplies the existing per-item records that the session organization references. | Nothing in this card. | [V10 §7E-TSC / 2. Relationship to §7E] |
| 88 · ACCEPTED | C-ENROLL.15.11 — Recovery after close before Catalog submission | Committed closure and the frozen capture-reference set. | Gates this place: standard intake rules. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 89 · DESIGNED | C-OOP — Outcome Observation Processing (§26) | Authorized post-action-window signals during and immediately after function execution. | Gates this place: actual capture/ingest and holding gates. | Nothing in this card. | [V10 §26.6] |
| 90 · DESIGNED | C-TSC.13.1 — Close observation | Normal session closure. | Gates this place: retains the observation as held pre-ingest material. | Nothing in this card. | [V10 §7E-TSC / 2. Relationship to §7E] |
| 91 · DESIGNED | C-8.1 — Research component flow | Brave raw results and secondary academic-source results. | Takes this place's change: authorized root-producing entry uses the normal Catalog envelope. | Authorized root-producing entry uses the normal Catalog envelope. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §5] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §14] [V10 §8] [MAP C-8] |
| 92 · ACCEPTED | C-TSC.3.2.3.6 — blocked | A remaining non-fingerprint blocker. | Gates this place: its normal resolution rule controls clearance. | Nothing in this card. | [V10 §7E-TSC / 17. Exact Promotion Sequence] [04/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md §5] |
| 93 · DESIGNED | C-8 — Research Pipeline / Knowledge Catcher (§8) | Research topics, raw outside sources and stored information to compare against outside evidence. | Takes this place's change: only authorized review entry supplies research-side captures to the common intake path. | Only authorized review entry supplies research-side captures to the common intake path. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §5] [MAP C-7E] |
| 94 · DESIGNED | C-TSC.5 — Contribution record | `contribution_id` (uuid4), `session_id` (foreign key), `sequence_position` (1-based integer), `occurred_at` (timestamp), `duration_ms` (integer or null), `contributor_stream_id` (foreign key to `participants.stream_id`), `role` (`ness`, `participant`, `nh_output`, `unknown`), `content_type` (`voice`, `text`, `nh_text`, `nh_voice`, `other`), `preingest_capture_id` (uuid4), `word_count` and `character_count` (integer or null), `reply_to_contribution_id` (uuid4 or null), `branch_level` (integer), `item_lifecycle_status` (`held`, `ready`, `promoting`, `promoted`, `excluded`, `blocked`), `promoted_root_id` (uuid4 or null), `exclusion_metadata` (JSON or null), and `content_hash` (SHA-256 of `raw_content` at capture). | Supplies its stable capture identifier links the row to the held payload. | Nothing in this card. | [V10 §7E-TSC / 5. Contribution Record Schema] |

SUB-PARTS: C-7E.1 — Separate capture and ingestion gates; C-7E.2 — Minimum intake envelope; C-7E.3 — Capture-error path; C-7E.4 — Privacy and exclusion precedence; C-7E.5 — Unified pre-ingest record; C-7E.6 — Pre-ingest lifecycle; C-7E.7 — Catalog speaker resolution; C-7E.8 — Source-title and thread resolution; C-7E.9 — Enrichment categories; C-7E.10 — Catalog boundary tests; C-7E.11 — Held-content access boundary; C-7E.12 — Accepted root-write handoff; C-7E.13 — Catalog operation records

### C-7E.1 — Separate capture and ingestion gates
Stamp: DESIGNED    Source: [V10 §7E / TWO GATES] [V10 §7E / DESIGN BOUNDARY]

ALONE
- What it is: DESIGNED — Two separate decisions: acceptance of an identifiable raw capture and eligibility to ingest a root. [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Takes in: DESIGNED — Raw material, its intake envelope and the catalog fields whose resolution root ingestion requires. [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Does: DESIGNED — Leaves capture/normalization with the front door and completeness evaluation/resolution with the pre-ingest Catalog. [V10 §7E / DESIGN BOUNDARY]
- Gives out: DESIGNED — A captured item that may remain held until all root-ingestion requirements are resolved. [V10 §7E / TWO GATES] [V10 §7E / PRE-INGEST HOLDING AREA]
- Must never: DESIGNED — Treat capture as permission to ingest, guess a missing field to complete handoff, or destroy raw material because a required field remains unresolved. [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Fails closed by: DESIGNED — Keeps root ingestion blocked until the required catalog fields are resolved. [V10 §7E / TWO GATES]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7E.1.1 — Raw-capture gate: accepting a capture requires the minimum identifiable envelope. [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Gated by: DESIGNED — C-7E.1.2 — Root-ingestion gate: all required catalog fields and blockers must be resolved before root admission. [V10 §7E / TWO GATES] [V10 §7E / PRE-INGEST HOLDING AREA]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E) | Raw material, its intake envelope and the catalog fields whose resolution root ingestion requires. | raw capture does not establish root eligibility. | A captured item that may remain held until all root-ingestion requirements are resolved. | [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / PRE-INGEST HOLDING AREA] |

SUB-PARTS: C-7E.1.1 — Raw-capture gate; C-7E.1.2 — Root-ingestion gate

### C-7E.1.1 — Raw-capture gate
Stamp: DESIGNED    Source: [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY]

ALONE
- What it is: DESIGNED — Acceptance of a front-door capture into the pre-ingest store. [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Takes in: DESIGNED — Raw material with the complete minimum intake envelope. [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Does: DESIGNED — Accepts an identifiable capture without requiring its speaker or every future root field to be resolved already. [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / SPEAKER RESOLUTION RULE]
- Gives out: DESIGNED — Captured material ready for catalog completeness evaluation and resolution. [V10 §7E / DESIGN BOUNDARY]
- Must never: DESIGNED — Accept an unidentifiable blob or guess missing values to make handoff appear complete. [V10 §7E / DESIGN BOUNDARY] [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Fails closed by: DESIGNED — Routes a capture that cannot meet the envelope to an explicit capture-error path, preserving available material. [V10 §7E / DESIGN BOUNDARY]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7E.2 — Minimum intake envelope: all seven elements are required before acceptance. [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Changes: DESIGNED — C-7E.3 — Capture-error path: receives malformed captures that fail the minimum envelope. [V10 §7E / DESIGN BOUNDARY]
- Changes: DESIGNED — C-7E.5 — Unified pre-ingest record: accepted captures become identifiable held items for resolution. [V10 §7E / PRE-INGEST HOLDING AREA]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.1 — Separate capture and ingestion gates | Raw material with the complete minimum intake envelope. | accepting a capture requires the minimum identifiable envelope. | Captured material ready for catalog completeness evaluation and resolution. | [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] |
| 2 · DESIGNED | C-7E.2 — Minimum intake envelope | Raw material with the complete minimum intake envelope. | the complete envelope is a prerequisite for acceptance, not a later guessed repair. | Captured material ready for catalog completeness evaluation and resolution. | [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] |
| 3 · DESIGNED | C-BOP.1 — Authorized physical-observation boundary | A permitted signal and its actual session/import authorization. | Gates this place: actual raw-capture gate. | Nothing in this card. | [V10 §25.1] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §A10] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-7E.1.2 — Root-ingestion gate
Stamp: DESIGNED    Source: [V10 §7E / TWO GATES] [V10 §7E / PRE-INGEST HOLDING AREA]

ALONE
- What it is: DESIGNED — The catalog-eligibility gate before a captured item can become a root. [V10 §7E / TWO GATES]
- Takes in: DESIGNED — An identified capture, its catalog fields and remaining blockers. [V10 §7E / TWO GATES] [V10 §7E / CONCEPTUAL RECORD SHAPE]
- Does: DESIGNED — Requires all necessary fields to be resolved; a blocker is removed only when its actual requirement is resolved. [V10 §7E / TWO GATES] [DD §3C]
- Gives out: DESIGNED — Root-eligible material after catalog resolution, kept distinct from merely captured material. [V10 §7E / TWO GATES]
- Must never: DESIGNED — Ingest an unresolved speaker, guess uncertain grouping, or let one blocked item prevent unrelated ready items from progressing. [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] [V10 §7E / PRE-INGEST HOLDING AREA]
- Fails closed by: DESIGNED — Holds the item while a catalog requirement remains unresolved. [V10 §7E / PRE-INGEST HOLDING AREA]

TOGETHER
- Fed by: DESIGNED — C-7E.5 — Unified pre-ingest record: supplies the capture, proposed fields and blocker state for eligibility evaluation. [V10 §7E / CONCEPTUAL RECORD SHAPE]
- Gated by: DESIGNED — C-7E.7 — Catalog speaker resolution: root ingestion requires a resolved source-grounded speaker. [V10 §7E / SPEAKER RESOLUTION RULE]
- Gated by: DESIGNED — C-7E.8 — Source-title and thread resolution: genuinely uncertain grouping remains blocked rather than guessed. [V10 §7E / SOURCE TITLE RULE]
- Gated by: DESIGNED — C-7E.4 — Privacy and exclusion precedence: excluded material cannot follow ordinary root storage. [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]
- Gated by: ACCEPTED — C-7E.12 — Accepted root-write handoff: eligible roots still require the shared B11 boundary and its committed upstream evidence. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.1]
- Changes: DESIGNED — C-7E.6 — Pre-ingest lifecycle: blocker-free eligible items may progress through ready and promoting to promoted. [V10 §7E / PRE-INGEST HOLDING AREA] [V10 §7E / LIFECYCLE STATES]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.1 — Separate capture and ingestion gates | An identified capture, its catalog fields and remaining blockers. | all required catalog fields and blockers must be resolved before root admission. | Root-eligible material after catalog resolution, kept distinct from merely captured material. | [V10 §7E / TWO GATES] [V10 §7E / PRE-INGEST HOLDING AREA] [V10 §7E / CONCEPTUAL RECORD SHAPE] |
| 2 · DESIGNED | C-7E.5.2 — Blocker list | An identified capture, its catalog fields and remaining blockers. | every required catalog condition must be resolved before ingestion. | Root-eligible material after catalog resolution, kept distinct from merely captured material. | [V10 §7E / TWO GATES] [V10 §7E / CONCEPTUAL RECORD SHAPE] |
| 3 · DESIGNED | C-7E.6 — Pre-ingest lifecycle | An identified capture, its catalog fields and remaining blockers. | unresolved requirements block progression into root ingestion. | Root-eligible material after catalog resolution, kept distinct from merely captured material. | [V10 §7E / TWO GATES] [V10 §7E / CONCEPTUAL RECORD SHAPE] |
| 4 · DESIGNED | C-7E.6.2 — ready | An identified capture, its catalog fields and remaining blockers. | all catalog requirements must be resolved before readiness for ingestion. | Root-eligible material after catalog resolution, kept distinct from merely captured material. | [V10 §7E / TWO GATES] [V10 §7E / CONCEPTUAL RECORD SHAPE] |
| 5 · DESIGNED | C-7E.12 — Accepted root-write handoff | An identified capture, its catalog fields and remaining blockers. | supplies catalog-eligible material only after its required fields and blockers are resolved. | Root-eligible material after catalog resolution, kept distinct from merely captured material. | [V10 §7E / TWO GATES] [V10 §7E / CONCEPTUAL RECORD SHAPE] |

SUB-PARTS: NONE

### C-7E.2 — Minimum intake envelope
Stamp: DESIGNED    Source: [V10 §7E / MINIMUM INTAKE ENVELOPE]

ALONE
- What it is: DESIGNED — The seven-element minimum that every front door must supply before pre-ingest acceptance. [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Takes in: DESIGNED — One stable unique `capture_id`; the exact raw payload or stable immutable reference; capture timestamp; front-door/source type; payload format/media type; source-provided metadata preserved without reinterpretation; and provenance sufficient to trace how and where capture occurred. [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Does: DESIGNED — Carries that common envelope, allowing additional reliable source-derived catalog fields already known to the front door. [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Gives out: DESIGNED — An identifiable capture with its original source metadata and provenance intact. [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Must never: DESIGNED — Guess missing values, substitute a mutable reference for the required immutable payload reference, or reinterpret source-provided metadata. [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Fails closed by: DESIGNED — A malformed capture unable to meet this minimum enters the explicit capture-error path, with available material preserved. [V10 §7E / DESIGN BOUNDARY]

TOGETHER
- Fed by: ACCEPTED — C-STORE.5.5.8.1 — capture_id: carries the stable unique capture identity preserved by the accepted handoff. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10] [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Fed by: ACCEPTED — C-STORE.5.5.8.2 — raw payload or immutable reference: carries the exact payload or its stable immutable reference. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10] [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Fed by: ACCEPTED — C-STORE.5.5.8.3 — capture timestamp: carries the capture time in the unchanged envelope. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10] [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Fed by: ACCEPTED — C-STORE.5.5.8.4 — front-door/source type: identifies the capture's front door or source type. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10] [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Fed by: ACCEPTED — C-STORE.5.5.8.5 — payload format/media type: identifies the payload's format or media type. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10] [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Fed by: ACCEPTED — C-STORE.5.5.8.6 — source-provided metadata: preserves source metadata without reinterpretation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10] [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Fed by: ACCEPTED — C-STORE.5.5.8.7 — capture provenance: traces how and where the capture occurred. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10] [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Gated by: DESIGNED — C-7E.1.1 — Raw-capture gate: the complete envelope is a prerequisite for acceptance, not a later guessed repair. [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E) | One stable unique `capture_id`; the exact raw payload or stable immutable reference; capture timestamp; front-door/source type; payload format/media type; source-provided metadata preserved without reinterpretation; and provenance sufficient to trace how and where capture occurred. | all seven required elements must be present before pre-ingest accepts a capture. | An identifiable capture with its original source metadata and provenance intact. | [V10 §7E / MINIMUM INTAKE ENVELOPE] |
| 2 · DESIGNED | C-7E.1.1 — Raw-capture gate | One stable unique `capture_id`; the exact raw payload or stable immutable reference; capture timestamp; front-door/source type; payload format/media type; source-provided metadata preserved without reinterpretation; and provenance sufficient to trace how and where capture occurred. | all seven elements are required before acceptance. | An identifiable capture with its original source metadata and provenance intact. | [V10 §7E / MINIMUM INTAKE ENVELOPE] |
| 3 · DESIGNED | C-7E.3 — Capture-error path | One stable unique `capture_id`; the exact raw payload or stable immutable reference; capture timestamp; front-door/source type; payload format/media type; source-provided metadata preserved without reinterpretation; and provenance sufficient to trace how and where capture occurred. | failure to meet this minimum requires the explicit error path. | An identifiable capture with its original source metadata and provenance intact. | [V10 §7E / DESIGN BOUNDARY] [V10 §7E / MINIMUM INTAKE ENVELOPE] |
| 4 · DESIGNED | C-7E.5 — Unified pre-ingest record | One stable unique `capture_id`; the exact raw payload or stable immutable reference; capture timestamp; front-door/source type; payload format/media type; source-provided metadata preserved without reinterpretation; and provenance sufficient to trace how and where capture occurred. | supplies the identifiable raw capture, original metadata and provenance. | An identifiable capture with its original source metadata and provenance intact. | [V10 §7E / MINIMUM INTAKE ENVELOPE] |
| 5 · ACCEPTED | C-14.5.5 — Live-label envelope condition | A live capture and its provenance label. | Gates this place: includes the live label in the shared envelope verification. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] |
| 6 · ACCEPTED | C-9A.7.1.2 — SQLite extraction stage | Source messages, sender metadata, media items and exact source timestamp fields. | Gates this place: all seven intake elements must be present without guessing. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 7 · ACCEPTED | C-9A.7.5.7 — WhatsApp capture-error outcome | An extracted message with missing or invalid required capture information. | Gates this place: an extracted message must satisfy the complete intake envelope. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 8 · DESIGNED | C-14.1 — Automatic live-turn capture | Each message and its actual source metadata. | Gates this place: requires all seven minimum intake-envelope elements before pre-ingest acceptance. | Nothing in this card. | [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] |
| 9 · DESIGNED | C-9A.5 — Image Catalog handoff | Stable unique `capture_id`, exact raw payload or stable immutable reference, capture timestamp, front-door/source type, payload format/media type, source-provided metadata without reinterpretation, and traceable capture provenance. | Supplies the complete seven-element minimum envelope contract. | Nothing in this card. | [MAP C-7E] |

SUB-PARTS: NONE

### C-7E.3 — Capture-error path
Stamp: DESIGNED    Source: [V10 §7E / DESIGN BOUNDARY]

ALONE
- What it is: DESIGNED — The explicit path for malformed captures that cannot satisfy the minimum envelope. [V10 §7E / DESIGN BOUNDARY]
- Takes in: DESIGNED — The malformed capture and whatever material is available. [V10 §7E / DESIGN BOUNDARY]
- Does: DESIGNED — Preserves available material in the explicit capture-error path. [V10 §7E / DESIGN BOUNDARY]
- Gives out: DESIGNED — A preserved capture-error case instead of an unidentifiable accepted blob or silent drop. [V10 §7E / DESIGN BOUNDARY]
- Must never: DESIGNED — Silently discard the capture or present an unidentifiable blob as accepted intake. [V10 §7E / DESIGN BOUNDARY]
- Fails closed by: DESIGNED — Keeps the failed capture outside normal acceptance and preserves the available material. [V10 §7E / DESIGN BOUNDARY]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7E.2 — Minimum intake envelope: failure to meet this minimum requires the explicit error path. [V10 §7E / DESIGN BOUNDARY]
- Gated by: DESIGNED — C-7E.4 — Privacy and exclusion precedence: preservation still applies only to eligible material within the proper protected boundary. [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]
- Changes: DESIGNED — C-7E.13.6 — Capture-error record: supplies the capture-error event that must be recorded. [MAP C-7E]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.1.1 — Raw-capture gate | The malformed capture and whatever material is available. | receives malformed captures that fail the minimum envelope. | A preserved capture-error case instead of an unidentifiable accepted blob or silent drop. | [V10 §7E / DESIGN BOUNDARY] |
| 2 · DESIGNED | C-14.1 — Automatic live-turn capture | Each message and its actual source metadata. | Takes this place's change: sends malformed captures to the explicit preserved error path. | Sends malformed captures to the explicit preserved error path. | [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] |
| 3 · ACCEPTED | C-14.5.5 — Live-label envelope condition | A live capture and its provenance label. | Takes this place's change: supplies missing-label failures to the capture-error path. | Supplies missing-label failures to the capture-error path. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] [V10 §7E / TWO GATES] [V10 §7E / MINIMUM INTAKE ENVELOPE] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] |

SUB-PARTS: NONE

### C-7E.4 — Privacy and exclusion precedence
Stamp: DESIGNED    Source: [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]

ALONE
- What it is: DESIGNED — The privacy boundary that overrides ordinary Catalog preservation. [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]
- Takes in: DESIGNED — Capture material subject to live-credential, non-negotiable-secret, Ness-configured exclusion, redaction, deletion or mixed-content-separation rules. [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]
- Does: DESIGNED — Keeps only the safe permitted remainder and non-reconstructive exclusion metadata in active Catalog, active TSC, ordinary pre-ingest, normal memory and retained TSC archives; sends excluded raw content to separate sealed protected storage under the applicable protection level. [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]
- Gives out: DESIGNED — A safe permitted remainder with non-reconstructive metadata, while excluded content remains preserved outside the active Catalog and normal memory. [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]
- Must never: DESIGNED — Keep excluded raw content in the ordinary Catalog or memory path, reconstruct it from exclusion metadata, or treat protected preservation as destruction. [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]
- Fails closed by: DESIGNED — Excludes the protected raw content from ordinary catalog retention and semantic memory use; only the safe remainder may continue there. [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): its exclusion, separation and protection-level rules override Catalog's general preservation rule. [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]
- Changes: DESIGNED — C-7E.5 — Unified pre-ingest record: retains only safe permitted material and non-reconstructive exclusion metadata in the ordinary record. [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]
- Changes: DESIGNED — C-7E.13.5 — Exclusion record: supplies the exclusion operation for recording. [MAP C-7E]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E) | Capture material subject to live-credential, non-negotiable-secret, Ness-configured exclusion, redaction, deletion or mixed-content-separation rules. | only eligible non-excluded material remains in the ordinary Catalog path. | A safe permitted remainder with non-reconstructive metadata, while excluded content remains preserved outside the active Catalog and normal memory. | [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE] |
| 2 · DESIGNED | C-7E.1.2 — Root-ingestion gate | Capture material subject to live-credential, non-negotiable-secret, Ness-configured exclusion, redaction, deletion or mixed-content-separation rules. | excluded material cannot follow ordinary root storage. | A safe permitted remainder with non-reconstructive metadata, while excluded content remains preserved outside the active Catalog and normal memory. | [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE] |
| 3 · DESIGNED | C-7E.3 — Capture-error path | Capture material subject to live-credential, non-negotiable-secret, Ness-configured exclusion, redaction, deletion or mixed-content-separation rules. | preservation still applies only to eligible material within the proper protected boundary. | A safe permitted remainder with non-reconstructive metadata, while excluded content remains preserved outside the active Catalog and normal memory. | [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE] |
| 4 · DESIGNED | C-7E.5 — Unified pre-ingest record | Capture material subject to live-credential, non-negotiable-secret, Ness-configured exclusion, redaction, deletion or mixed-content-separation rules. | ordinary records cannot retain excluded raw content. | A safe permitted remainder with non-reconstructive metadata, while excluded content remains preserved outside the active Catalog and normal memory. | [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE] |
| 5 · DESIGNED | C-7E.6 — Pre-ingest lifecycle | Capture material subject to live-credential, non-negotiable-secret, Ness-configured exclusion, redaction, deletion or mixed-content-separation rules. | excluded raw content follows the separate protected-storage route. | A safe permitted remainder with non-reconstructive metadata, while excluded content remains preserved outside the active Catalog and normal memory. | [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE] |
| 6 · DESIGNED | C-7E.6.6 — excluded | Capture material subject to live-credential, non-negotiable-secret, Ness-configured exclusion, redaction, deletion or mixed-content-separation rules. | exclusion follows the governing privacy protection level and safe-remainder rule. | A safe permitted remainder with non-reconstructive metadata, while excluded content remains preserved outside the active Catalog and normal memory. | [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE] |
| 7 · DESIGNED | C-7E.13.5 — Exclusion record | Capture material subject to live-credential, non-negotiable-secret, Ness-configured exclusion, redaction, deletion or mixed-content-separation rules. | ordinary records retain only non-reconstructive exclusion metadata and any safe remainder. | A safe permitted remainder with non-reconstructive metadata, while excluded content remains preserved outside the active Catalog and normal memory. | [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE] |

SUB-PARTS: NONE

### C-7E.5 — Unified pre-ingest record
Stamp: DESIGNED    Source: [V10 §7E / PRE-INGEST HOLDING AREA] [V10 §7E / CONCEPTUAL RECORD SHAPE]

ALONE
- What it is: DESIGNED — One record per item in one unified pre-ingest store: one `capture_id`, one stable location, unchanged raw payload and a list of blockers. [V10 §7E / PRE-INGEST HOLDING AREA]
- Takes in: DESIGNED — At minimum `capture_id`, raw payload or stable reference, capture timestamp, front-door type, source metadata, proposed catalog fields, blocker list, proposal provenance and uncertainty, resolution history, lifecycle state and resulting `root_id` if promoted. [V10 §7E / CONCEPTUAL RECORD SHAPE]
- Does: DESIGNED — Preserves raw capture while metadata and resolution develop around it; material may remain held indefinitely, and one blocked item does not block unrelated ready items. [V10 §7E / PRE-INGEST HOLDING AREA] [V10 §7E / The raw captured payload]
- Gives out: DESIGNED — A traceable held or progressed item; after promotion the record remains as provenance with the resulting `root_id` recorded. [V10 §7E / PRE-INGEST HOLDING AREA]
- Must never: DESIGNED — Rewrite raw payload, silently delete a held item, or create duplicate roots through repeated processing. [V10 §7E / PRE-INGEST HOLDING AREA]
- Fails closed by: DESIGNED — Keeps unresolved material held and outside the Meaning Engine while unrelated eligible items continue. [V10 §7E / PRE-INGEST HOLDING AREA]

TOGETHER
- Fed by: DESIGNED — C-7E.2 — Minimum intake envelope: supplies the identifiable raw capture, original metadata and provenance. [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Fed by: DESIGNED — C-7E.5.1 — Proposed catalog fields: supplies proposed values around the unchanged capture. [V10 §7E / CONCEPTUAL RECORD SHAPE]
- Fed by: DESIGNED — C-7E.5.2 — Blocker list: records every unresolved requirement for this item. [V10 §7E / PRE-INGEST HOLDING AREA]
- Fed by: DESIGNED — C-7E.5.3 — Proposal provenance and uncertainty: preserves the basis and uncertainty of catalog proposals. [V10 §7E / CONCEPTUAL RECORD SHAPE]
- Fed by: DESIGNED — C-7E.5.4 — Resolution history: retains how catalog resolution developed. [V10 §7E / CONCEPTUAL RECORD SHAPE]
- Fed by: DESIGNED — C-7E.5.5 — Lifecycle state: records the item's current lifecycle state. [V10 §7E / CONCEPTUAL RECORD SHAPE]
- Fed by: DESIGNED — C-7E.5.6 — Resulting root_id: records the root identity when promotion succeeds. [V10 §7E / PRE-INGEST HOLDING AREA]
- Gated by: DESIGNED — C-7E.4 — Privacy and exclusion precedence: ordinary records cannot retain excluded raw content. [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]
- Gated by: DESIGNED — C-7E.11 — Held-content access boundary: held raw content remains unavailable to downstream semantic analysis. [MAP C-7E]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E) | At minimum `capture_id`, raw payload or stable reference, capture timestamp, front-door type, source metadata, proposed catalog fields, blocker list, proposal provenance and uncertainty, resolution history, lifecycle state and resulting `root_id` if promoted. | preserves each capture at its stable location while metadata and resolution develop around it. | A traceable held or progressed item; after promotion the record remains as provenance with the resulting `root_id` recorded. | [V10 §7E / PRE-INGEST HOLDING AREA] [V10 §7E / CONCEPTUAL RECORD SHAPE] |
| 2 · DESIGNED | C-7E.1.1 — Raw-capture gate | At minimum `capture_id`, raw payload or stable reference, capture timestamp, front-door type, source metadata, proposed catalog fields, blocker list, proposal provenance and uncertainty, resolution history, lifecycle state and resulting `root_id` if promoted. | accepted captures become identifiable held items for resolution. | A traceable held or progressed item; after promotion the record remains as provenance with the resulting `root_id` recorded. | [V10 §7E / PRE-INGEST HOLDING AREA] [V10 §7E / CONCEPTUAL RECORD SHAPE] |
| 3 · DESIGNED | C-7E.1.2 — Root-ingestion gate | At minimum `capture_id`, raw payload or stable reference, capture timestamp, front-door type, source metadata, proposed catalog fields, blocker list, proposal provenance and uncertainty, resolution history, lifecycle state and resulting `root_id` if promoted. | supplies the capture, proposed fields and blocker state for eligibility evaluation. | A traceable held or progressed item; after promotion the record remains as provenance with the resulting `root_id` recorded. | [V10 §7E / CONCEPTUAL RECORD SHAPE] [V10 §7E / PRE-INGEST HOLDING AREA] |
| 4 · DESIGNED | C-7E.4 — Privacy and exclusion precedence | At minimum `capture_id`, raw payload or stable reference, capture timestamp, front-door type, source metadata, proposed catalog fields, blocker list, proposal provenance and uncertainty, resolution history, lifecycle state and resulting `root_id` if promoted. | retains only safe permitted material and non-reconstructive exclusion metadata in the ordinary record. | A traceable held or progressed item; after promotion the record remains as provenance with the resulting `root_id` recorded. | [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE] [V10 §7E / CONCEPTUAL RECORD SHAPE] [V10 §7E / PRE-INGEST HOLDING AREA] |
| 5 · DESIGNED | C-7E.5.1 — Proposed catalog fields | At minimum `capture_id`, raw payload or stable reference, capture timestamp, front-door type, source metadata, proposed catalog fields, blocker list, proposal provenance and uncertainty, resolution history, lifecycle state and resulting `root_id` if promoted. | proposed catalog fields are retained around the original raw item, not written into it. | A traceable held or progressed item; after promotion the record remains as provenance with the resulting `root_id` recorded. | [V10 §7E / CONCEPTUAL RECORD SHAPE] [V10 §7E / The raw captured payload] [V10 §7E / PRE-INGEST HOLDING AREA] |
| 6 · DESIGNED | C-7E.6 — Pre-ingest lifecycle | At minimum `capture_id`, raw payload or stable reference, capture timestamp, front-door type, source metadata, proposed catalog fields, blocker list, proposal provenance and uncertainty, resolution history, lifecycle state and resulting `root_id` if promoted. | supplies the preserved item and its recorded resolution state. | A traceable held or progressed item; after promotion the record remains as provenance with the resulting `root_id` recorded. | [V10 §7E / CONCEPTUAL RECORD SHAPE] [V10 §7E / PRE-INGEST HOLDING AREA] |
| 7 · DESIGNED | C-7E.9 — Enrichment categories | At minimum `capture_id`, raw payload or stable reference, capture timestamp, front-door type, source metadata, proposed catalog fields, blocker list, proposal provenance and uncertainty, resolution history, lifecycle state and resulting `root_id` if promoted. | develops metadata around the unchanged capture. | A traceable held or progressed item; after promotion the record remains as provenance with the resulting `root_id` recorded. | [V10 §7E / The raw captured payload] [V10 §7E / CONCEPTUAL RECORD SHAPE] [V10 §7E / PRE-INGEST HOLDING AREA] |

SUB-PARTS: C-7E.5.1 — Proposed catalog fields; C-7E.5.2 — Blocker list; C-7E.5.3 — Proposal provenance and uncertainty; C-7E.5.4 — Resolution history; C-7E.5.5 — Lifecycle state; C-7E.5.6 — Resulting root_id

### C-7E.5.1 — Proposed catalog fields
Stamp: DESIGNED    Source: [V10 §7E / CONCEPTUAL RECORD SHAPE] [V10 §7E / C. Machine-inferred classifications]

ALONE
- What it is: DESIGNED — Proposed catalog values carried around the unchanged raw capture. [V10 §7E / CONCEPTUAL RECORD SHAPE] [V10 §7E / The raw captured payload]
- Takes in: DESIGNED — Proposed values for unresolved catalog information. [V10 §7E / C. Machine-inferred classifications]
- Does: DESIGNED — Retains the proposals with their provenance, uncertainty and confirmation status. [V10 §7E / C. Machine-inferred classifications]
- Gives out: DESIGNED — Explicit proposals available to catalog resolution. [V10 §7E / C. Machine-inferred classifications]
- Must never: DESIGNED — Silently settle a machine inference or rewrite raw capture to install a proposed value. [V10 §7E / C. Machine-inferred classifications] [V10 §7E / The raw captured payload]
- Fails closed by: DESIGNED — Keeps the value proposed until source evidence, Ness or an explicitly authorized resolution rule confirms it. [V10 §7E / C. Machine-inferred classifications]

TOGETHER
- Fed by: DESIGNED — C-7E.9.3 — Machine-inferred proposals: supplies classifications under the proposal-only contract. [V10 §7E / C. Machine-inferred classifications]
- Gated by: DESIGNED — C-7E.5 — Unified pre-ingest record: proposed catalog fields are retained around the original raw item, not written into it. [V10 §7E / CONCEPTUAL RECORD SHAPE] [V10 §7E / The raw captured payload]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.5 — Unified pre-ingest record | Proposed values for unresolved catalog information. | supplies proposed values around the unchanged capture. | Explicit proposals available to catalog resolution. | [V10 §7E / CONCEPTUAL RECORD SHAPE] [V10 §7E / C. Machine-inferred classifications] |

SUB-PARTS: NONE

### C-7E.5.2 — Blocker list
Stamp: DESIGNED    Source: [V10 §7E / PRE-INGEST HOLDING AREA] [DD §3C] [DD §3N]

ALONE
- What it is: DESIGNED — The item's list of unresolved catalog requirements. [V10 §7E / PRE-INGEST HOLDING AREA]
- Takes in: DESIGNED — Blockers such as `speaker_unresolved`, `thread_unresolved`, or both; TSC items additionally carry `pending_fingerprint_authorization`. [V10 §7E / PRE-INGEST HOLDING AREA] [DD §3N]
- Does: DESIGNED — Keeps the requirements independent and removes a blocker only when its actual requirement is resolved. Clearing TSC fingerprint authorization does not resolve speaker attribution. [DD §3C] [DD §3N]
- Gives out: DESIGNED — The remaining blocker list used to decide whether the item may progress. [V10 §7E / PRE-INGEST HOLDING AREA]
- Must never: DESIGNED — Clear an unresolved requirement because another blocker cleared, or demand a new fingerprint merely to resolve a speaker within an already authorized TSC. [DD §3N]
- Fails closed by: DESIGNED — Holds the item while required blockers remain; no root is written with unresolved speaker information. [V10 §7E / SPEAKER RESOLUTION RULE] [DD §3N]

TOGETHER
- Fed by: DESIGNED — C-DETECT.2.4 — Unattended speaker hold: identifies the unresolved-speaker condition for unattended material. [V10 §7E / SPEAKER RESOLUTION RULE]
- Fed by: DESIGNED — C-7E.8.4 — Uncertain grouping: identifies `thread_unresolved` when unattended grouping cannot be established. [V10 §7E / SOURCE TITLE RULE]
- Gated by: DESIGNED — C-7E.1.2 — Root-ingestion gate: every required catalog condition must be resolved before ingestion. [V10 §7E / TWO GATES]
- Gated by: DESIGNED — C-TSC — Temporary Session Cache (§7E-TSC): its fingerprint blocker clears only through the purpose-bound token and fresh recognized-Ness authorization at consumption. [DD §3N]
- Changes: DESIGNED — C-7E.13.2 — Blocker-set record: provides each blocker addition and its reason for logging. [MAP C-7E]
- Changes: DESIGNED — C-7E.13.3 — Blocker-clear record: provides each actual blocker clearance and its reason for logging. [MAP C-7E]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.5 — Unified pre-ingest record | Blockers such as `speaker_unresolved`, `thread_unresolved`, or both; TSC items additionally carry `pending_fingerprint_authorization`. | records every unresolved requirement for this item. | The remaining blocker list used to decide whether the item may progress. | [V10 §7E / PRE-INGEST HOLDING AREA] [DD §3N] |
| 2 · DESIGNED | C-7E.6.1 — held | Blockers such as `speaker_unresolved`, `thread_unresolved`, or both; TSC items additionally carry `pending_fingerprint_authorization`. | supplies the unresolved requirements for this item. | The remaining blocker list used to decide whether the item may progress. | [V10 §7E / PRE-INGEST HOLDING AREA] [DD §3N] |
| 3 · DESIGNED | C-7E.7 — Catalog speaker resolution | Blockers such as `speaker_unresolved`, `thread_unresolved`, or both; TSC items additionally carry `pending_fingerprint_authorization`. | retains the unresolved-speaker blocker until the speaker is actually resolved. | The remaining blocker list used to decide whether the item may progress. | [V10 §7E / SPEAKER RESOLUTION RULE] [DD §3C] [V10 §7E / PRE-INGEST HOLDING AREA] [DD §3N] |
| 4 · DESIGNED | C-7E.11 — Held-content access boundary | Blockers such as `speaker_unresolved`, `thread_unresolved`, or both; TSC items additionally carry `pending_fingerprint_authorization`. | supplies blocker information eligible for that restricted reference. | The remaining blocker list used to decide whether the item may progress. | [MAP C-7E] [V10 §7E / PRE-INGEST HOLDING AREA] [DD §3N] |
| 5 · DESIGNED | C-7E.13.3 — Blocker-clear record | Blockers such as `speaker_unresolved`, `thread_unresolved`, or both; TSC items additionally carry `pending_fingerprint_authorization`. | clearance requires actual resolution of that blocker, independently of other blockers. | The remaining blocker list used to decide whether the item may progress. | [DD §3C] [DD §3N] [V10 §7E / PRE-INGEST HOLDING AREA] |

SUB-PARTS: NONE

### C-7E.5.3 — Proposal provenance and uncertainty
Stamp: DESIGNED    Source: [V10 §7E / CONCEPTUAL RECORD SHAPE] [V10 §7E / C. Machine-inferred classifications]

ALONE
- What it is: DESIGNED — The provenance and uncertainty required alongside proposed catalog information. [V10 §7E / CONCEPTUAL RECORD SHAPE]
- Takes in: DESIGNED — Producer/model/rule, evidence, confidence, timestamp and confirmation status for a proposed classification. [V10 §7E / C. Machine-inferred classifications]
- Does: DESIGNED — Preserves that information with the proposed value. [V10 §7E / C. Machine-inferred classifications]
- Gives out: DESIGNED — A traceable proposal whose confirmation status remains distinct from its existence. [V10 §7E / C. Machine-inferred classifications]
- Must never: DESIGNED — Drop the proposal's provenance or uncertainty, or present a machine classification as settled without confirmation. [V10 §7E / CONCEPTUAL RECORD SHAPE] [V10 §7E / C. Machine-inferred classifications]
- Fails closed by: DESIGNED — Leaves unconfirmed information in proposal form. [V10 §7E / C. Machine-inferred classifications]

TOGETHER
- Fed by: DESIGNED — C-7E.9.3 — Machine-inferred proposals: supplies the required proposal information. [V10 §7E / C. Machine-inferred classifications]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.5 — Unified pre-ingest record | Producer/model/rule, evidence, confidence, timestamp and confirmation status for a proposed classification. | preserves the basis and uncertainty of catalog proposals. | A traceable proposal whose confirmation status remains distinct from its existence. | [V10 §7E / CONCEPTUAL RECORD SHAPE] [V10 §7E / C. Machine-inferred classifications] |

SUB-PARTS: NONE

### C-7E.5.4 — Resolution history
Stamp: DESIGNED    Source: [V10 §7E / CONCEPTUAL RECORD SHAPE]

ALONE
- What it is: DESIGNED — The catalog-resolution history in the pre-ingest record. [V10 §7E / CONCEPTUAL RECORD SHAPE]
- Takes in: DESIGNED — The item's resolution history. [V10 §7E / CONCEPTUAL RECORD SHAPE]
- Does: DESIGNED — Retains it as part of the conceptual record around the unchanged raw capture. [V10 §7E / CONCEPTUAL RECORD SHAPE] [V10 §7E / The raw captured payload]
- Gives out: DESIGNED — Resolution history available with the preserved item. [V10 §7E / CONCEPTUAL RECORD SHAPE]
- Must never: DESIGNED — Omit resolution history from the record or rewrite raw capture to represent later clarification. [V10 §7E / CONCEPTUAL RECORD SHAPE] [V10 §7E / The raw captured payload]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.5 — Unified pre-ingest record | The item's resolution history. | retains how catalog resolution developed. | Resolution history available with the preserved item. | [V10 §7E / CONCEPTUAL RECORD SHAPE] |

SUB-PARTS: NONE

### C-7E.5.5 — Lifecycle state
Stamp: DESIGNED    Source: [V10 §7E / CONCEPTUAL RECORD SHAPE] [V10 §7E / LIFECYCLE STATES]

ALONE
- What it is: DESIGNED — The pre-ingest record's lifecycle-state value. [V10 §7E / CONCEPTUAL RECORD SHAPE]
- Takes in: DESIGNED — One of the conceptual states `held`, `ready`, `promoting`, `promoted`, `rejected`, `excluded` or `error`. [V10 §7E / LIFECYCLE STATES]
- Does: DESIGNED — Records the item's place in the pre-ingest lifecycle. [V10 §7E / CONCEPTUAL RECORD SHAPE]
- Gives out: DESIGNED — The lifecycle state carried with the item. [V10 §7E / CONCEPTUAL RECORD SHAPE]
- Must never: DESIGNED — Treat rejected, excluded or failed processing as a successful promotion, or destroy material merely because processing failed. [V10 §7E / LIFECYCLE STATES]
- Fails closed by: DESIGNED — Failed processing is recorded as `error` with material preserved. [V10 §7E / LIFECYCLE STATES]

TOGETHER
- Fed by: DESIGNED — C-7E.6 — Pre-ingest lifecycle: supplies the permitted state and its conceptual transition boundary. [V10 §7E / LIFECYCLE STATES]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.5 — Unified pre-ingest record | One of the conceptual states `held`, `ready`, `promoting`, `promoted`, `rejected`, `excluded` or `error`. | records the item's current lifecycle state. | The lifecycle state carried with the item. | [V10 §7E / CONCEPTUAL RECORD SHAPE] [V10 §7E / LIFECYCLE STATES] |
| 2 · DESIGNED | C-7E.11 — Held-content access boundary | One of the conceptual states `held`, `ready`, `promoting`, `promoted`, `rejected`, `excluded` or `error`. | supplies the lifecycle information eligible for a metadata-only reference. | The lifecycle state carried with the item. | [MAP C-7E] [V10 §7E / LIFECYCLE STATES] [V10 §7E / CONCEPTUAL RECORD SHAPE] |
| 3 · ACCEPTED | C-TSC.17.8.2 — Pre-ingest submission interface | `item_promotion_operation_id` [proposed], `preingest_capture_id`, derived `capture_id`, and accepted structural source metadata. | Supplies Catalog's actual lifecycle state in the acceptance response. | Nothing in this card. | [04/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7E.5.6 — Resulting root_id
Stamp: DESIGNED    Source: [V10 §7E / CONCEPTUAL RECORD SHAPE] [V10 §7E / PRE-INGEST HOLDING AREA]

ALONE
- What it is: DESIGNED — The resulting `root_id` recorded in the pre-ingest item after promotion. [V10 §7E / PRE-INGEST HOLDING AREA]
- Takes in: DESIGNED — The identity of the root produced by successful promotion. [V10 §7E / PRE-INGEST HOLDING AREA]
- Does: DESIGNED — Records that identity while retaining the pre-ingest record as provenance. [V10 §7E / PRE-INGEST HOLDING AREA]
- Gives out: DESIGNED — The preserved pre-ingest-to-root provenance link. [V10 §7E / PRE-INGEST HOLDING AREA]
- Must never: DESIGNED — Delete the pre-ingest record after promotion or invent a resulting root identity before a root exists. [V10 §7E / PRE-INGEST HOLDING AREA] [V10 §7E / CONCEPTUAL RECORD SHAPE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-7E.12 — Accepted root-write handoff: supplies the existing or newly committed root identity from the durable B11 outcome. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.5] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13]
- Gated by: DESIGNED — C-7E.6.4 — promoted: the resulting `root_id` belongs to an item that has actually been promoted. [V10 §7E / CONCEPTUAL RECORD SHAPE]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.5 — Unified pre-ingest record | The identity of the root produced by successful promotion. | records the root identity when promotion succeeds. | The preserved pre-ingest-to-root provenance link. | [V10 §7E / PRE-INGEST HOLDING AREA] |

SUB-PARTS: NONE

### C-7E.6 — Pre-ingest lifecycle
Stamp: DESIGNED    Source: [V10 §7E / LIFECYCLE STATES] [V10 §7E / PRE-INGEST HOLDING AREA]

ALONE
- What it is: DESIGNED — The conceptual progression `held` → `ready` → `promoting` → `promoted`, with `rejected`, `excluded` and `error` alternatives. [V10 §7E / LIFECYCLE STATES]
- Takes in: DESIGNED — A preserved captured item, its blocker list and resolution state. [V10 §7E / PRE-INGEST HOLDING AREA]
- Does: DESIGNED — Holds unresolved material, permits resolved items to progress, performs atomic promotion and retains the original pre-ingest record as provenance. [V10 §7E / PRE-INGEST HOLDING AREA] [V10 §7E / LIFECYCLE STATES]
- Gives out: DESIGNED — A promoted root reference or an honestly retained held, rejected, excluded or failed item. [V10 §7E / LIFECYCLE STATES] [V10 §7E / PRE-INGEST HOLDING AREA]
- Must never: DESIGNED — Silently delete material, create duplicate roots on repeated processing, or let a blocked item obstruct unrelated ready items. [V10 §7E / PRE-INGEST HOLDING AREA]
- Fails closed by: DESIGNED — Preserves unresolved material in holding and failed processing in `error`; failure does not destroy the captured material. [V10 §7E / PRE-INGEST HOLDING AREA] [V10 §7E / LIFECYCLE STATES]

TOGETHER
- Fed by: DESIGNED — C-7E.5 — Unified pre-ingest record: supplies the preserved item and its recorded resolution state. [V10 §7E / CONCEPTUAL RECORD SHAPE]
- Gated by: DESIGNED — C-7E.1.2 — Root-ingestion gate: unresolved requirements block progression into root ingestion. [V10 §7E / TWO GATES]
- Gated by: DESIGNED — C-7E.4 — Privacy and exclusion precedence: excluded raw content follows the separate protected-storage route. [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]
- Changes: DESIGNED — C-7E.6.1 — held: preserves items whose catalog requirements remain unresolved. [V10 §7E / PRE-INGEST HOLDING AREA]
- Changes: DESIGNED — C-7E.6.2 — ready: marks resolved items ready to progress. [V10 §7E / TWO GATES] [V10 §7E / LIFECYCLE STATES]
- Changes: DESIGNED — C-7E.6.3 — promoting: carries the atomic promotion step. [V10 §7E / PRE-INGEST HOLDING AREA] [V10 §7E / LIFECYCLE STATES]
- Changes: DESIGNED — C-7E.6.4 — promoted: records successful promotion and the resulting root reference. [V10 §7E / PRE-INGEST HOLDING AREA]
- Changes: DESIGNED — C-7E.6.5 — rejected: records an intentional rejection with its reason. [V10 §7E / LIFECYCLE STATES]
- Changes: DESIGNED — C-7E.6.6 — excluded: records intentional exclusion with its reason under privacy precedence. [V10 §7E / LIFECYCLE STATES] [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]
- Changes: DESIGNED — C-7E.6.7 — error: records failed processing with material preserved. [V10 §7E / LIFECYCLE STATES]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.1.2 — Root-ingestion gate | A preserved captured item, its blocker list and resolution state. | blocker-free eligible items may progress through ready and promoting to promoted. | A promoted root reference or an honestly retained held, rejected, excluded or failed item. | [V10 §7E / PRE-INGEST HOLDING AREA] [V10 §7E / LIFECYCLE STATES] |
| 2 · DESIGNED | C-7E.5.5 — Lifecycle state | A preserved captured item, its blocker list and resolution state. | supplies the permitted state and its conceptual transition boundary. | A promoted root reference or an honestly retained held, rejected, excluded or failed item. | [V10 §7E / LIFECYCLE STATES] [V10 §7E / PRE-INGEST HOLDING AREA] |
| 3 · DESIGNED | C-7E.6.1 — held | A preserved captured item, its blocker list and resolution state. | progression requires actual resolution; remaining held is permitted indefinitely. | A promoted root reference or an honestly retained held, rejected, excluded or failed item. | [V10 §7E / PRE-INGEST HOLDING AREA] [DD §3C] [V10 §7E / LIFECYCLE STATES] |
| 4 · DESIGNED | C-7E.6.3 — promoting | A preserved captured item, its blocker list and resolution state. | promotion must be atomic and idempotent. | A promoted root reference or an honestly retained held, rejected, excluded or failed item. | [V10 §7E / PRE-INGEST HOLDING AREA] [V10 §7E / LIFECYCLE STATES] |
| 5 · DESIGNED | C-7E.6.4 — promoted | A preserved captured item, its blocker list and resolution state. | promoted follows completed atomic promotion, with the pre-ingest record retained. | A promoted root reference or an honestly retained held, rejected, excluded or failed item. | [V10 §7E / PRE-INGEST HOLDING AREA] [V10 §7E / LIFECYCLE STATES] |

SUB-PARTS: C-7E.6.1 — held; C-7E.6.2 — ready; C-7E.6.3 — promoting; C-7E.6.4 — promoted; C-7E.6.5 — rejected; C-7E.6.6 — excluded; C-7E.6.7 — error

### C-7E.6.1 — held
Stamp: DESIGNED    Source: [V10 §7E / PRE-INGEST HOLDING AREA] [V10 §7E / LIFECYCLE STATES]

ALONE
- What it is: DESIGNED — The pre-ingest state for material awaiting resolution of its requirements. [V10 §7E / PRE-INGEST HOLDING AREA]
- Takes in: DESIGNED — The preserved item and its remaining blockers. [V10 §7E / PRE-INGEST HOLDING AREA]
- Does: DESIGNED — Keeps it held, potentially indefinitely, while unrelated ready items continue. [V10 §7E / PRE-INGEST HOLDING AREA]
- Gives out: DESIGNED — Preserved held material; after actual blocker resolution it may move to `ready`. [V10 §7E / LIFECYCLE STATES] [DD §3C]
- Must never: DESIGNED — Remove blockers without resolving their requirements, silently delete held material, or block unrelated ready items. [DD §3C] [V10 §7E / PRE-INGEST HOLDING AREA]
- Fails closed by: DESIGNED — Retains the hold while required catalog information is unresolved. [V10 §7E / TWO GATES] [V10 §7E / PRE-INGEST HOLDING AREA]

TOGETHER
- Fed by: DESIGNED — C-7E.5.2 — Blocker list: supplies the unresolved requirements for this item. [V10 §7E / PRE-INGEST HOLDING AREA]
- Gated by: DESIGNED — C-7E.6 — Pre-ingest lifecycle: progression requires actual resolution; remaining held is permitted indefinitely. [V10 §7E / PRE-INGEST HOLDING AREA] [DD §3C]
- Gated by: DESIGNED — C-7E.11 — Held-content access boundary: holding does not grant downstream semantic access. [MAP C-7E]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.6 — Pre-ingest lifecycle | The preserved item and its remaining blockers. | preserves items whose catalog requirements remain unresolved. | Preserved held material; after actual blocker resolution it may move to `ready`. | [V10 §7E / PRE-INGEST HOLDING AREA] [V10 §7E / LIFECYCLE STATES] [DD §3C] |

SUB-PARTS: NONE

### C-7E.6.2 — ready
Stamp: DESIGNED    Source: [V10 §7E / LIFECYCLE STATES] [V10 §7E / TWO GATES]

ALONE
- What it is: DESIGNED — The resolved pre-ingest state preceding promotion. [V10 §7E / LIFECYCLE STATES] [V10 §7E / TWO GATES]
- Takes in: DESIGNED — An item whose required catalog fields and blockers have actually been resolved. [V10 §7E / TWO GATES] [DD §3C]
- Does: DESIGNED — Makes that item eligible to progress to `promoting` without waiting for unrelated blocked items. [V10 §7E / LIFECYCLE STATES] [V10 §7E / PRE-INGEST HOLDING AREA]
- Gives out: DESIGNED — An item ready for the root-ingestion path. [V10 §7E / LIFECYCLE STATES]
- Must never: DESIGNED — Call unresolved material ready for root ingestion or require unrelated held items to become ready first. [V10 §7E / TWO GATES] [V10 §7E / PRE-INGEST HOLDING AREA]
- Fails closed by: DESIGNED — Unresolved required fields prevent root-ingestion eligibility. [V10 §7E / TWO GATES]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7E.1.2 — Root-ingestion gate: all catalog requirements must be resolved before readiness for ingestion. [V10 §7E / TWO GATES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.6 — Pre-ingest lifecycle | An item whose required catalog fields and blockers have actually been resolved. | marks resolved items ready to progress. | An item ready for the root-ingestion path. | [V10 §7E / TWO GATES] [V10 §7E / LIFECYCLE STATES] [DD §3C] |
| 2 · DESIGNED | C-7E.6.3 — promoting | An item whose required catalog fields and blockers have actually been resolved. | supplies a catalog-resolved item for promotion. | An item ready for the root-ingestion path. | [V10 §7E / LIFECYCLE STATES] [V10 §7E / TWO GATES] [DD §3C] |

SUB-PARTS: NONE

### C-7E.6.3 — promoting
Stamp: DESIGNED    Source: [V10 §7E / LIFECYCLE STATES] [V10 §7E / PRE-INGEST HOLDING AREA]

ALONE
- What it is: DESIGNED — The promotion-in-progress state between `ready` and `promoted`. [V10 §7E / LIFECYCLE STATES]
- Takes in: DESIGNED — A ready, catalog-eligible item. [V10 §7E / TWO GATES] [V10 §7E / LIFECYCLE STATES]
- Does: DESIGNED — Promotes atomically into the root store with idempotent processing. [V10 §7E / PRE-INGEST HOLDING AREA]
- Gives out: DESIGNED — Successful promotion with resulting `root_id`, or the preserved failure state when processing fails. [V10 §7E / PRE-INGEST HOLDING AREA] [V10 §7E / LIFECYCLE STATES]
- Must never: DESIGNED — Create duplicate roots from repeated processing or silently discard the source item on failure. [V10 §7E / PRE-INGEST HOLDING AREA] [V10 §7E / LIFECYCLE STATES]
- Fails closed by: DESIGNED — Failed processing retains the material in `error`. [V10 §7E / LIFECYCLE STATES]

TOGETHER
- Fed by: DESIGNED — C-7E.6.2 — ready: supplies a catalog-resolved item for promotion. [V10 §7E / LIFECYCLE STATES]
- Gated by: DESIGNED — C-7E.6 — Pre-ingest lifecycle: promotion must be atomic and idempotent. [V10 §7E / PRE-INGEST HOLDING AREA]
- Gated by: ACCEPTED — C-7E.12 — Accepted root-write handoff: root writing must pass B11's mechanical checks and durable outcome boundary. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.1] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.4]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.6 — Pre-ingest lifecycle | A ready, catalog-eligible item. | carries the atomic promotion step. | Successful promotion with resulting `root_id`, or the preserved failure state when processing fails. | [V10 §7E / PRE-INGEST HOLDING AREA] [V10 §7E / LIFECYCLE STATES] [V10 §7E / TWO GATES] |

SUB-PARTS: NONE

### C-7E.6.4 — promoted
Stamp: DESIGNED    Source: [V10 §7E / LIFECYCLE STATES] [V10 §7E / PRE-INGEST HOLDING AREA]

ALONE
- What it is: DESIGNED — The state after successful promotion into the root store. [V10 §7E / LIFECYCLE STATES]
- Takes in: DESIGNED — The completed promotion and resulting root identity. [V10 §7E / PRE-INGEST HOLDING AREA]
- Does: DESIGNED — Keeps the pre-ingest record as provenance and records the resulting `root_id`. [V10 §7E / PRE-INGEST HOLDING AREA]
- Gives out: DESIGNED — A preserved pre-ingest record linked to its promoted root. [V10 §7E / PRE-INGEST HOLDING AREA]
- Must never: DESIGNED — Delete the pre-ingest provenance after promotion or produce another root from repeated processing of the same item. [V10 §7E / PRE-INGEST HOLDING AREA]
- Fails closed by: ACCEPTED — Withholds success acknowledgement until the matching parent terminal record is durable, while preserving any root already committed at WB2. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.4]

TOGETHER
- Fed by: ACCEPTED — C-7E.12 — Accepted root-write handoff: supplies the durably acknowledged root identity and owning batch. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.4] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.5]
- Gated by: DESIGNED — C-7E.6 — Pre-ingest lifecycle: promoted follows completed atomic promotion, with the pre-ingest record retained. [V10 §7E / PRE-INGEST HOLDING AREA] [V10 §7E / LIFECYCLE STATES]
- Changes: DESIGNED — C-7E.13.4 — Promotion record: supplies the promotion event for logging. [MAP C-7E]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.5.6 — Resulting root_id | The completed promotion and resulting root identity. | the resulting `root_id` belongs to an item that has actually been promoted. | A preserved pre-ingest record linked to its promoted root. | [V10 §7E / CONCEPTUAL RECORD SHAPE] [V10 §7E / PRE-INGEST HOLDING AREA] |
| 2 · DESIGNED | C-7E.6 — Pre-ingest lifecycle | The completed promotion and resulting root identity. | records successful promotion and the resulting root reference. | A preserved pre-ingest record linked to its promoted root. | [V10 §7E / PRE-INGEST HOLDING AREA] |

SUB-PARTS: NONE

### C-7E.6.5 — rejected
Stamp: DESIGNED    Source: [V10 §7E / LIFECYCLE STATES]

ALONE
- What it is: DESIGNED — Intentional rejection in the pre-ingest lifecycle. [V10 §7E / LIFECYCLE STATES]
- Takes in: DESIGNED — An intentionally rejected item and its reason. [V10 §7E / LIFECYCLE STATES]
- Does: DESIGNED — Records the rejected disposition with that reason. [V10 §7E / LIFECYCLE STATES]
- Gives out: DESIGNED — An item in `rejected`, distinguished from processing failure or successful promotion. [V10 §7E / LIFECYCLE STATES]
- Must never: DESIGNED — Omit the reason for intentional rejection or silently delete raw material. [V10 §7E / LIFECYCLE STATES] [V10 §7E / PRE-INGEST HOLDING AREA]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.6 — Pre-ingest lifecycle | An intentionally rejected item and its reason. | records an intentional rejection with its reason. | An item in `rejected`, distinguished from processing failure or successful promotion. | [V10 §7E / LIFECYCLE STATES] |

SUB-PARTS: NONE

### C-7E.6.6 — excluded
Stamp: DESIGNED    Source: [V10 §7E / LIFECYCLE STATES] [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]

ALONE
- What it is: DESIGNED — Intentional exclusion in the pre-ingest lifecycle, recorded with a reason. [V10 §7E / LIFECYCLE STATES]
- Takes in: DESIGNED — Material subject to exclusion and the reason for that disposition. [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE] [V10 §7E / LIFECYCLE STATES]
- Does: DESIGNED — Applies exclusion while keeping only safe remainder and non-reconstructive metadata in the ordinary record; excluded raw content remains in separate sealed protected storage. [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]
- Gives out: DESIGNED — The excluded disposition and safe ordinary metadata, without excluded raw content in normal memory. [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]
- Must never: DESIGNED — Omit the exclusion reason, retain excluded raw content in the active Catalog or TSC archive, or destroy it. [V10 §7E / LIFECYCLE STATES] [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]
- Fails closed by: DESIGNED — Keeps excluded raw content outside the ordinary catalog and memory path. [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7E.4 — Privacy and exclusion precedence: exclusion follows the governing privacy protection level and safe-remainder rule. [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.6 — Pre-ingest lifecycle | Material subject to exclusion and the reason for that disposition. | records intentional exclusion with its reason under privacy precedence. | The excluded disposition and safe ordinary metadata, without excluded raw content in normal memory. | [V10 §7E / LIFECYCLE STATES] [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE] |

SUB-PARTS: NONE

### C-7E.6.7 — error
Stamp: DESIGNED    Source: [V10 §7E / LIFECYCLE STATES]

ALONE
- What it is: DESIGNED — The pre-ingest processing-failure state. [V10 §7E / LIFECYCLE STATES]
- Takes in: DESIGNED — An item whose processing failed. [V10 §7E / LIFECYCLE STATES]
- Does: DESIGNED — Records `error` while preserving the material. [V10 §7E / LIFECYCLE STATES]
- Gives out: DESIGNED — A preserved failed item, not a success claim. [V10 §7E / LIFECYCLE STATES]
- Must never: DESIGNED — Destroy the material because processing failed or present that failure as promotion. [V10 §7E / LIFECYCLE STATES]
- Fails closed by: DESIGNED — Retains the item and its error state. [V10 §7E / LIFECYCLE STATES]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.6 — Pre-ingest lifecycle | An item whose processing failed. | records failed processing with material preserved. | A preserved failed item, not a success claim. | [V10 §7E / LIFECYCLE STATES] |

SUB-PARTS: NONE

### C-7E.7 — Catalog speaker resolution
Stamp: DESIGNED    Source: [V10 §7E / SPEAKER RESOLUTION RULE] [MAP C-DETECT]

ALONE
- What it is: DESIGNED — Resolution of the speaker needed for a source-grounded root `role`. [V10 §7E / SPEAKER RESOLUTION RULE]
- Takes in: DESIGNED — Source-carried attribution, or an uncertain detector candidate where the source supplies none. [V10 §7E / SPEAKER RESOLUTION RULE] [MAP C-DETECT]
- Does: DESIGNED — Carries the source speaker without guessing; in live use asks Ness when a necessary speaker cannot be identified, and in unattended use holds the item as `speaker_unresolved`. [V10 §7E / SPEAKER RESOLUTION RULE]
- Gives out: DESIGNED — Resolved speaker information, or a proposal awaiting Ness or strong source evidence under an authorized rule. [MAP C-DETECT]
- Must never: DESIGNED — Guess `role`, silently turn a detector proposal into it, or write a root with `role = "unknown"`. [V10 §7E / SPEAKER RESOLUTION RULE] [DD §3N]
- Fails closed by: DESIGNED — Keeps unresolved unattended material held and refuses root ingestion without resolved speaker information. [V10 §7E / SPEAKER RESOLUTION RULE]

TOGETHER
- Fed by: DESIGNED — C-DETECT — Speaker detector (fallback; investigated, not deployed) (§11): may supply an uncertain candidate only for a role-less source. [MAP C-DETECT]
- Gated by: DESIGNED — C-DETECT.2 — Settled speaker rule: source attribution wins; fallback candidates require authorized confirmation and never write role directly. [MAP C-DETECT]
- Changes: DESIGNED — C-7E.5.2 — Blocker list: retains the unresolved-speaker blocker until the speaker is actually resolved. [V10 §7E / SPEAKER RESOLUTION RULE] [DD §3C]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.1.2 — Root-ingestion gate | Source-carried attribution, or an uncertain detector candidate where the source supplies none. | root ingestion requires a resolved source-grounded speaker. | Resolved speaker information, or a proposal awaiting Ness or strong source evidence under an authorized rule. | [V10 §7E / SPEAKER RESOLUTION RULE] [MAP C-DETECT] |
| 2 · DESIGNED | C-7E.9.3 — Machine-inferred proposals | Source-carried attribution, or an uncertain detector candidate where the source supplies none. | a suspected-speaker proposal additionally obeys source priority and the no-guessed-role rule. | Resolved speaker information, or a proposal awaiting Ness or strong source evidence under an authorized rule. | [V10 §7E / SPEAKER RESOLUTION RULE] [MAP C-DETECT] |

SUB-PARTS: NONE

### C-7E.8 — Source-title and thread resolution
Stamp: DESIGNED    Source: [V10 §7E / SOURCE TITLE RULE]

ALONE
- What it is: DESIGNED — The grouping rule for `source_title`, used by Engine B's positional context retrieval. [V10 §7E / SOURCE TITLE RULE]
- Takes in: DESIGNED — A real source thread identifier, provable same-session grouping without a title, an isolated item, or genuinely uncertain grouping. [V10 §7E / SOURCE TITLE RULE]
- Does: DESIGNED — Carries a real thread identifier exactly; assigns one unique non-semantic capture-session placeholder to provably grouped untitled material; assigns a unique singleton placeholder to an isolated item; asks Ness live or holds unattended material when grouping is uncertain. [V10 §7E / SOURCE TITLE RULE]
- Gives out: DESIGNED — Source-grounded or mechanically unique grouping information, or `thread_unresolved` while grouping remains uncertain. [V10 §7E / SOURCE TITLE RULE]
- Must never: DESIGNED — Use a machine-generated topic, summary or semantic label as `source_title`, rewrite a sealed root, or guess uncertain grouping. [V10 §7E / SOURCE TITLE RULE] [MAP C-7E]
- Fails closed by: DESIGNED — Holds unattended uncertain grouping as `thread_unresolved`; live use asks Ness rather than inventing a group. [V10 §7E / SOURCE TITLE RULE]

TOGETHER
- Fed by: DESIGNED — C-7E.8.1 — Source thread identifier: supplies the identifier exactly when the source provides one. [V10 §7E / SOURCE TITLE RULE]
- Fed by: DESIGNED — C-7E.8.2 — Untitled capture-session grouping: supplies one unique non-semantic placeholder for provably grouped material. [V10 §7E / SOURCE TITLE RULE]
- Fed by: DESIGNED — C-7E.8.3 — Singleton grouping: supplies a unique singleton placeholder for an isolated item. [V10 §7E / SOURCE TITLE RULE]
- Gated by: DESIGNED — C-7E.8.4 — Uncertain grouping: genuine uncertainty requires live clarification or unattended holding. [V10 §7E / SOURCE TITLE RULE]
- Gated by: ACCEPTED — C-STORE.5.4 — B20 — source_title alias/correction layer: later label clarification is append-only beside the original; aliases never change canonical thread identity or membership. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §9]
- Gated by: ACCEPTED — C-STORE.5.5 — B21 — Future root schema and pre-ingest schemas: the future stable non-semantic `thread_id` remains separate from optional `display_label`; no live v1 field is activated or renamed by the design. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.1.2 — Root-ingestion gate | A real source thread identifier, provable same-session grouping without a title, an isolated item, or genuinely uncertain grouping. | genuinely uncertain grouping remains blocked rather than guessed. | Source-grounded or mechanically unique grouping information, or `thread_unresolved` while grouping remains uncertain. | [V10 §7E / SOURCE TITLE RULE] |
| 2 · DESIGNED | C-7GA.8.1.8.1 — source_title_type | The root's existing source_title and its established source grouping. | Derives classification using the existing source-title/grouping rule. | Nothing in this card. | [V10 §7G-A / MODE-ASSIGNMENT RULE:] |

SUB-PARTS: C-7E.8.1 — Source thread identifier; C-7E.8.2 — Untitled capture-session grouping; C-7E.8.3 — Singleton grouping; C-7E.8.4 — Uncertain grouping

### C-7E.8.1 — Source thread identifier
Stamp: DESIGNED    Source: [V10 §7E / SOURCE TITLE RULE]

ALONE
- What it is: DESIGNED — The grouping case where the source provides a real thread identifier. [V10 §7E / SOURCE TITLE RULE]
- Takes in: DESIGNED — That source-provided thread identifier. [V10 §7E / SOURCE TITLE RULE]
- Does: DESIGNED — Carries it exactly as the grouping value. [V10 §7E / SOURCE TITLE RULE]
- Gives out: DESIGNED — The unchanged source thread identifier. [V10 §7E / SOURCE TITLE RULE]
- Must never: DESIGNED — Replace the source identifier with a generated topic or summary. [V10 §7E / SOURCE TITLE RULE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.8 — Source-title and thread resolution | That source-provided thread identifier. | supplies the identifier exactly when the source provides one. | The unchanged source thread identifier. | [V10 §7E / SOURCE TITLE RULE] |

SUB-PARTS: NONE

### C-7E.8.2 — Untitled capture-session grouping
Stamp: DESIGNED    Source: [V10 §7E / SOURCE TITLE RULE]

ALONE
- What it is: DESIGNED — The grouping case for untitled items that provably belong together. [V10 §7E / SOURCE TITLE RULE]
- Takes in: DESIGNED — Source material lacking a title but with provable common capture-session grouping. [V10 §7E / SOURCE TITLE RULE]
- Does: DESIGNED — Uses one unique non-semantic placeholder per capture session, such as `untitled:paste:<capture-session-id>` or `untitled:voice:<capture-session-id>`. [V10 §7E / SOURCE TITLE RULE]
- Gives out: DESIGNED — A shared capture-session grouping placeholder without a topic interpretation. [V10 §7E / SOURCE TITLE RULE]
- Must never: DESIGNED — Apply shared grouping without evidence that the items belong together, or use a semantic summary as the placeholder. [V10 §7E / SOURCE TITLE RULE]
- Fails closed by: DESIGNED — Genuinely uncertain grouping requires live clarification or unattended `thread_unresolved` holding. [V10 §7E / SOURCE TITLE RULE]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.8 — Source-title and thread resolution | Source material lacking a title but with provable common capture-session grouping. | supplies one unique non-semantic placeholder for provably grouped material. | A shared capture-session grouping placeholder without a topic interpretation. | [V10 §7E / SOURCE TITLE RULE] |

SUB-PARTS: NONE

### C-7E.8.3 — Singleton grouping
Stamp: DESIGNED    Source: [V10 §7E / SOURCE TITLE RULE]

ALONE
- What it is: DESIGNED — The unique grouping placeholder for an isolated item. [V10 §7E / SOURCE TITLE RULE]
- Takes in: DESIGNED — An isolated source item. [V10 §7E / SOURCE TITLE RULE]
- Does: DESIGNED — Assigns a unique singleton placeholder. [V10 §7E / SOURCE TITLE RULE]
- Gives out: DESIGNED — A grouping identity that keeps this item a singleton. [V10 §7E / SOURCE TITLE RULE]
- Must never: DESIGNED — Replace the placeholder with a machine-generated topic or summary. [V10 §7E / SOURCE TITLE RULE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.8 — Source-title and thread resolution | An isolated source item. | supplies a unique singleton placeholder for an isolated item. | A grouping identity that keeps this item a singleton. | [V10 §7E / SOURCE TITLE RULE] |

SUB-PARTS: NONE

### C-7E.8.4 — Uncertain grouping
Stamp: DESIGNED    Source: [V10 §7E / SOURCE TITLE RULE]

ALONE
- What it is: DESIGNED — The unresolved-grouping case in Catalog title resolution. [V10 §7E / SOURCE TITLE RULE]
- Takes in: DESIGNED — Material whose grouping is genuinely uncertain. [V10 §7E / SOURCE TITLE RULE]
- Does: DESIGNED — Asks Ness in live use; holds unattended material as `thread_unresolved`. [V10 §7E / SOURCE TITLE RULE]
- Gives out: DESIGNED — A live clarification request or an unresolved-thread hold. [V10 §7E / SOURCE TITLE RULE]
- Must never: DESIGNED — Guess grouping to satisfy root-ingestion requirements or remove the blocker without resolving its actual condition. [V10 §7E / SOURCE TITLE RULE] [DD §3C]
- Fails closed by: DESIGNED — Leaves unattended material held while grouping is unresolved. [V10 §7E / SOURCE TITLE RULE]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.5.2 — Blocker list | Material whose grouping is genuinely uncertain. | identifies `thread_unresolved` when unattended grouping cannot be established. | A live clarification request or an unresolved-thread hold. | [V10 §7E / SOURCE TITLE RULE] |
| 2 · DESIGNED | C-7E.8 — Source-title and thread resolution | Material whose grouping is genuinely uncertain. | genuine uncertainty requires live clarification or unattended holding. | A live clarification request or an unresolved-thread hold. | [V10 §7E / SOURCE TITLE RULE] |

SUB-PARTS: NONE

### C-7E.9 — Enrichment categories
Stamp: DESIGNED    Source: [V10 §7E / FOUR ENRICHMENT CATEGORIES]

ALONE
- What it is: DESIGNED — The four Catalog enrichment categories: source-carried facts, deterministic mechanical derivations, machine-inferred proposals and forbidden semantic interpretation. [V10 §7E / FOUR ENRICHMENT CATEGORIES]
- Takes in: DESIGNED — Source metadata, mechanically derived metadata and machine-inferred classification proposals around raw capture. [V10 §7E / FOUR ENRICHMENT CATEGORIES]
- Does: DESIGNED — Accepts source-carried facts with provenance, permits separately recorded mechanical derivations, keeps inferences proposed until confirmation, and excludes semantic interpretation from Catalog. [V10 §7E / FOUR ENRICHMENT CATEGORIES]
- Gives out: DESIGNED — Enrichment metadata around unchanged raw payload; the exact schemas, field names and derived values entering a future root schema remain undesigned in the Catalog specification. [V10 §7E / The raw captured payload]
- Must never: DESIGNED — Rewrite raw capture, substitute normalization for its original source value, silently settle inference, or perform semantic interpretation in Catalog. [V10 §7E / FOUR ENRICHMENT CATEGORIES] [V10 §7E / The raw captured payload]
- Fails closed by: DESIGNED — A derivation failure preserves the capture; an unconfirmed inference stays a proposal. [V10 §7E / B. Deterministic mechanical derivations] [V10 §7E / C. Machine-inferred classifications]

TOGETHER
- Fed by: DESIGNED — C-7E.9.1 — Source-carried facts: supplies source facts with each fact's provenance. [V10 §7E / A. Source-carried facts]
- Fed by: DESIGNED — C-7E.9.2 — Deterministic derivations: supplies separately held mechanical values with method and version. [V10 §7E / B. Deterministic mechanical derivations]
- Fed by: DESIGNED — C-7E.9.3 — Machine-inferred proposals: supplies uncertain classifications with confirmation information. [V10 §7E / C. Machine-inferred classifications]
- Gated by: DESIGNED — C-7E.9.4 — Semantic-interpretation prohibition: meaning, interpretation and judgment do not belong in Catalog. [V10 §7E / D. Semantic interpretation]
- Gated by: DESIGNED — C-7E.10 — Catalog boundary tests: material-description and interpretation checks determine the boundary with semantic work. [V10 §7E / BOUNDARY TESTS]
- Changes: DESIGNED — C-7E.5 — Unified pre-ingest record: develops metadata around the unchanged capture. [V10 §7E / The raw captured payload]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E) | Source metadata, mechanically derived metadata and machine-inferred classification proposals around raw capture. | only source facts, mechanical derivations and explicitly unsettled proposals belong in Catalog. | Enrichment metadata around unchanged raw payload; the exact schemas, field names and derived values entering a future root schema remain undesigned in the Catalog specification. | [V10 §7E / FOUR ENRICHMENT CATEGORIES] [V10 §7E / The raw captured payload] |
| 2 · DESIGNED | C-7E.9.1 — Source-carried facts | Source metadata, mechanically derived metadata and machine-inferred classification proposals around raw capture. | this category accepts source-carried facts, not machine-inferred replacements for them. | Enrichment metadata around unchanged raw payload; the exact schemas, field names and derived values entering a future root schema remain undesigned in the Catalog specification. | [V10 §7E / FOUR ENRICHMENT CATEGORIES] [V10 §7E / The raw captured payload] |
| 3 · DESIGNED | C-7E.9.2 — Deterministic derivations | Source metadata, mechanically derived metadata and machine-inferred classification proposals around raw capture. | only mechanical derivation belongs here; interpretation belongs outside Catalog. | Enrichment metadata around unchanged raw payload; the exact schemas, field names and derived values entering a future root schema remain undesigned in the Catalog specification. | [V10 §7E / FOUR ENRICHMENT CATEGORIES] [V10 §7E / The raw captured payload] |
| 4 · DESIGNED | C-7E.9.3 — Machine-inferred proposals | Source metadata, mechanically derived metadata and machine-inferred classification proposals around raw capture. | machine inference belongs only in the proposal category until authorized confirmation. | Enrichment metadata around unchanged raw payload; the exact schemas, field names and derived values entering a future root schema remain undesigned in the Catalog specification. | [V10 §7E / C. Machine-inferred classifications] [V10 §7E / FOUR ENRICHMENT CATEGORIES] [V10 §7E / The raw captured payload] |

SUB-PARTS: C-7E.9.1 — Source-carried facts; C-7E.9.2 — Deterministic derivations; C-7E.9.3 — Machine-inferred proposals; C-7E.9.4 — Semantic-interpretation prohibition

### C-7E.9.1 — Source-carried facts
Stamp: DESIGNED    Source: [V10 §7E / A. Source-carried facts]

ALONE
- What it is: DESIGNED — Enrichment category A: source-carried information accepted as catalog facts. [V10 §7E / A. Source-carried facts]
- Takes in: DESIGNED — Source-carried sender/speaker, source role, original timestamp, thread/conversation identifier, platform name, source title, message ordering, filename, attachment identifier and source media type. [V10 §7E / A. Source-carried facts]
- Does: DESIGNED — Accepts these source facts while recording the provenance of each fact. [V10 §7E / A. Source-carried facts]
- Gives out: DESIGNED — Catalog facts traceable to their source. [V10 §7E / A. Source-carried facts]
- Must never: DESIGNED — Omit a fact's provenance or reinterpret source metadata while carrying it. [V10 §7E / A. Source-carried facts] [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-STORE.5.5.8.6 — source-provided metadata: supplies the unchanged source information in the intake envelope. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10] [V10 §7E / MINIMUM INTAKE ENVELOPE]
- Gated by: DESIGNED — C-7E.9 — Enrichment categories: this category accepts source-carried facts, not machine-inferred replacements for them. [V10 §7E / FOUR ENRICHMENT CATEGORIES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.9 — Enrichment categories | Source-carried sender/speaker, source role, original timestamp, thread/conversation identifier, platform name, source title, message ordering, filename, attachment identifier and source media type. | supplies source facts with each fact's provenance. | Catalog facts traceable to their source. | [V10 §7E / A. Source-carried facts] |

SUB-PARTS: NONE

### C-7E.9.2 — Deterministic derivations
Stamp: DESIGNED    Source: [V10 §7E / B. Deterministic mechanical derivations]

ALONE
- What it is: DESIGNED — Enrichment category B: permitted deterministic mechanical derivations. [V10 §7E / B. Deterministic mechanical derivations]
- Takes in: DESIGNED — Source values from which content length, file size, checksum/hash, image dimensions, audio/video duration, encoding, normalized format, ordering index or normalized timestamp can be mechanically derived. [V10 §7E / B. Deterministic mechanical derivations]
- Does: DESIGNED — Preserves the original source value, stores each derived value separately, and records the derivation's method and version. [V10 §7E / B. Deterministic mechanical derivations]
- Gives out: DESIGNED — Separate derived metadata with method/version provenance, while the original source remains intact. [V10 §7E / B. Deterministic mechanical derivations]
- Must never: DESIGNED — Replace an original with its normalized form or alter or destroy a capture because derivation failed. [V10 §7E / B. Deterministic mechanical derivations]
- Fails closed by: DESIGNED — Derivation failure leaves the capture unaltered and preserved. [V10 §7E / B. Deterministic mechanical derivations]

TOGETHER
- Fed by: DESIGNED — C-7E.9.2.1 — Original source value: supplies the preserved source value that must remain intact. [V10 §7E / B. Deterministic mechanical derivations]
- Fed by: DESIGNED — C-7E.9.2.2 — Separate derived value: supplies the mechanically produced value held beside the original. [V10 §7E / B. Deterministic mechanical derivations]
- Fed by: DESIGNED — C-7E.9.2.3 — Derivation method: identifies how the value was derived. [V10 §7E / B. Deterministic mechanical derivations]
- Fed by: DESIGNED — C-7E.9.2.4 — Derivation version: identifies the recorded derivation version. [V10 §7E / B. Deterministic mechanical derivations]
- Gated by: DESIGNED — C-7E.9 — Enrichment categories: only mechanical derivation belongs here; interpretation belongs outside Catalog. [V10 §7E / FOUR ENRICHMENT CATEGORIES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.9 — Enrichment categories | Source values from which content length, file size, checksum/hash, image dimensions, audio/video duration, encoding, normalized format, ordering index or normalized timestamp can be mechanically derived. | supplies separately held mechanical values with method and version. | Separate derived metadata with method/version provenance, while the original source remains intact. | [V10 §7E / B. Deterministic mechanical derivations] |
| 2 · DESIGNED | C-7E.9.2.2 — Separate derived value | Source values from which content length, file size, checksum/hash, image dimensions, audio/video duration, encoding, normalized format, ordering index or normalized timestamp can be mechanically derived. | derived values require separate storage with method and version. | Separate derived metadata with method/version provenance, while the original source remains intact. | [V10 §7E / B. Deterministic mechanical derivations] |

SUB-PARTS: C-7E.9.2.1 — Original source value; C-7E.9.2.2 — Separate derived value; C-7E.9.2.3 — Derivation method; C-7E.9.2.4 — Derivation version

### C-7E.9.2.1 — Original source value
Stamp: DESIGNED    Source: [V10 §7E / B. Deterministic mechanical derivations]

ALONE
- What it is: DESIGNED — The original source value preserved alongside mechanical derivation. [V10 §7E / B. Deterministic mechanical derivations]
- Takes in: DESIGNED — The source's original value. [V10 §7E / B. Deterministic mechanical derivations]
- Does: DESIGNED — Retains that value without replacement by a normalized form. [V10 §7E / B. Deterministic mechanical derivations]
- Gives out: DESIGNED — The preserved original, distinct from derived metadata. [V10 §7E / B. Deterministic mechanical derivations]
- Must never: DESIGNED — Overwrite the original with a derived or normalized value. [V10 §7E / B. Deterministic mechanical derivations]
- Fails closed by: DESIGNED — Failed derivation does not alter or destroy the capture. [V10 §7E / B. Deterministic mechanical derivations]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.9.2 — Deterministic derivations | The source's original value. | supplies the preserved source value that must remain intact. | The preserved original, distinct from derived metadata. | [V10 §7E / B. Deterministic mechanical derivations] |

SUB-PARTS: NONE

### C-7E.9.2.2 — Separate derived value
Stamp: DESIGNED    Source: [V10 §7E / B. Deterministic mechanical derivations]

ALONE
- What it is: DESIGNED — The mechanically derived metadata value stored separately from its source value. [V10 §7E / B. Deterministic mechanical derivations]
- Takes in: DESIGNED — The result of a permitted deterministic derivation. [V10 §7E / B. Deterministic mechanical derivations]
- Does: DESIGNED — Stores the result separately rather than replacing its original. [V10 §7E / B. Deterministic mechanical derivations]
- Gives out: DESIGNED — Derived metadata distinguishable from the original source value. [V10 §7E / B. Deterministic mechanical derivations]
- Must never: DESIGNED — Use the derived value to overwrite the original. [V10 §7E / B. Deterministic mechanical derivations]
- Fails closed by: DESIGNED — An unsuccessful derivation leaves the original capture unchanged. [V10 §7E / B. Deterministic mechanical derivations]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7E.9.2 — Deterministic derivations: derived values require separate storage with method and version. [V10 §7E / B. Deterministic mechanical derivations]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.9.2 — Deterministic derivations | The result of a permitted deterministic derivation. | supplies the mechanically produced value held beside the original. | Derived metadata distinguishable from the original source value. | [V10 §7E / B. Deterministic mechanical derivations] |

SUB-PARTS: NONE

### C-7E.9.2.3 — Derivation method
Stamp: DESIGNED    Source: [V10 §7E / B. Deterministic mechanical derivations]

ALONE
- What it is: DESIGNED — The method recorded for a deterministic derivation. [V10 §7E / B. Deterministic mechanical derivations]
- Takes in: DESIGNED — The method used to derive the metadata value. [V10 §7E / B. Deterministic mechanical derivations]
- Does: DESIGNED — Records that method with the derivation. [V10 §7E / B. Deterministic mechanical derivations]
- Gives out: DESIGNED — Method provenance for the separate derived value. [V10 §7E / B. Deterministic mechanical derivations]
- Must never: DESIGNED — Omit the derivation method. [V10 §7E / B. Deterministic mechanical derivations]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.9.2 — Deterministic derivations | The method used to derive the metadata value. | identifies how the value was derived. | Method provenance for the separate derived value. | [V10 §7E / B. Deterministic mechanical derivations] |

SUB-PARTS: NONE

### C-7E.9.2.4 — Derivation version
Stamp: DESIGNED    Source: [V10 §7E / B. Deterministic mechanical derivations]

ALONE
- What it is: DESIGNED — The version recorded with a deterministic derivation. [V10 §7E / B. Deterministic mechanical derivations]
- Takes in: DESIGNED — The version of the derivation used. [V10 §7E / B. Deterministic mechanical derivations]
- Does: DESIGNED — Records the version alongside the method and derived result. [V10 §7E / B. Deterministic mechanical derivations]
- Gives out: DESIGNED — Version provenance for the derivation. [V10 §7E / B. Deterministic mechanical derivations]
- Must never: DESIGNED — Omit the derivation version. [V10 §7E / B. Deterministic mechanical derivations]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.9.2 — Deterministic derivations | The version of the derivation used. | identifies the recorded derivation version. | Version provenance for the derivation. | [V10 §7E / B. Deterministic mechanical derivations] |

SUB-PARTS: NONE

### C-7E.9.3 — Machine-inferred proposals
Stamp: DESIGNED    Source: [V10 §7E / C. Machine-inferred classifications]

ALONE
- What it is: DESIGNED — Enrichment category C: classifications kept as proposals rather than settled catalog facts. [V10 §7E / C. Machine-inferred classifications]
- Takes in: DESIGNED — Inferences such as detected language, suspected speaker, probable thread membership, probable duplicate, quoted-text detection and possible continuation. [V10 §7E / C. Machine-inferred classifications]
- Does: DESIGNED — Stores each classification only as a proposal carrying proposed value, producer/model/rule, evidence, confidence, timestamp and confirmation status. [V10 §7E / C. Machine-inferred classifications]
- Gives out: DESIGNED — A traceable proposal that can become settled only through source evidence, Ness or an explicitly authorized resolution rule. [V10 §7E / C. Machine-inferred classifications]
- Must never: DESIGNED — Turn machine inference into a settled catalog fact without that confirmation. [V10 §7E / C. Machine-inferred classifications]
- Fails closed by: DESIGNED — Retains proposal status while confirmation is absent. [V10 §7E / C. Machine-inferred classifications]

TOGETHER
- Fed by: DESIGNED — C-7E.9.3.1 — Inferred proposed value: supplies the value under consideration. [V10 §7E / C. Machine-inferred classifications]
- Fed by: DESIGNED — C-7E.9.3.2 — Producer/model/rule: identifies the proposal's producer. [V10 §7E / C. Machine-inferred classifications]
- Fed by: DESIGNED — C-7E.9.3.3 — Inference evidence: carries the proposal's evidence. [V10 §7E / C. Machine-inferred classifications]
- Fed by: DESIGNED — C-7E.9.3.4 — Inference confidence: carries confidence as proposal information. [V10 §7E / C. Machine-inferred classifications]
- Fed by: DESIGNED — C-7E.9.3.5 — Inference timestamp: carries the required timestamp. [V10 §7E / C. Machine-inferred classifications]
- Fed by: DESIGNED — C-7E.9.3.6 — Inference confirmation status: distinguishes confirmation from the existence of an inference. [V10 §7E / C. Machine-inferred classifications]
- Gated by: DESIGNED — C-7E.9 — Enrichment categories: machine inference belongs only in the proposal category until authorized confirmation. [V10 §7E / C. Machine-inferred classifications]
- Gated by: DESIGNED — C-7E.7 — Catalog speaker resolution: a suspected-speaker proposal additionally obeys source priority and the no-guessed-role rule. [V10 §7E / SPEAKER RESOLUTION RULE]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.5.1 — Proposed catalog fields | Inferences such as detected language, suspected speaker, probable thread membership, probable duplicate, quoted-text detection and possible continuation. | supplies classifications under the proposal-only contract. | A traceable proposal that can become settled only through source evidence, Ness or an explicitly authorized resolution rule. | [V10 §7E / C. Machine-inferred classifications] |
| 2 · DESIGNED | C-7E.5.3 — Proposal provenance and uncertainty | Inferences such as detected language, suspected speaker, probable thread membership, probable duplicate, quoted-text detection and possible continuation. | supplies the required proposal information. | A traceable proposal that can become settled only through source evidence, Ness or an explicitly authorized resolution rule. | [V10 §7E / C. Machine-inferred classifications] |
| 3 · DESIGNED | C-7E.9 — Enrichment categories | Inferences such as detected language, suspected speaker, probable thread membership, probable duplicate, quoted-text detection and possible continuation. | supplies uncertain classifications with confirmation information. | A traceable proposal that can become settled only through source evidence, Ness or an explicitly authorized resolution rule. | [V10 §7E / C. Machine-inferred classifications] |
| 4 · DESIGNED | C-7E.9.3.3 — Inference evidence | Inferences such as detected language, suspected speaker, probable thread membership, probable duplicate, quoted-text detection and possible continuation. | evidence is required, and settlement still requires authorized confirmation. | A traceable proposal that can become settled only through source evidence, Ness or an explicitly authorized resolution rule. | [V10 §7E / C. Machine-inferred classifications] |
| 5 · DESIGNED | C-7E.9.3.4 — Inference confidence | Inferences such as detected language, suspected speaker, probable thread membership, probable duplicate, quoted-text detection and possible continuation. | confidence is required metadata, and its presence does not remove the confirmation requirement. | A traceable proposal that can become settled only through source evidence, Ness or an explicitly authorized resolution rule. | [V10 §7E / C. Machine-inferred classifications] |
| 6 · DESIGNED | C-7E.9.3.6 — Inference confirmation status | Inferences such as detected language, suspected speaker, probable thread membership, probable duplicate, quoted-text detection and possible continuation. | settlement requires one of the expressly permitted confirmation routes. | A traceable proposal that can become settled only through source evidence, Ness or an explicitly authorized resolution rule. | [V10 §7E / C. Machine-inferred classifications] |

SUB-PARTS: C-7E.9.3.1 — Inferred proposed value; C-7E.9.3.2 — Producer/model/rule; C-7E.9.3.3 — Inference evidence; C-7E.9.3.4 — Inference confidence; C-7E.9.3.5 — Inference timestamp; C-7E.9.3.6 — Inference confirmation status

### C-7E.9.3.1 — Inferred proposed value
Stamp: DESIGNED    Source: [V10 §7E / C. Machine-inferred classifications]

ALONE
- What it is: DESIGNED — The proposed value of a machine-inferred catalog classification. [V10 §7E / C. Machine-inferred classifications]
- Takes in: DESIGNED — An inferred classification value. [V10 §7E / C. Machine-inferred classifications]
- Does: DESIGNED — Stores the value as proposed rather than settled. [V10 §7E / C. Machine-inferred classifications]
- Gives out: DESIGNED — The value being considered for confirmation. [V10 §7E / C. Machine-inferred classifications]
- Must never: DESIGNED — Become a settled catalog fact without source evidence, Ness or an explicitly authorized resolution rule confirming it. [V10 §7E / C. Machine-inferred classifications]
- Fails closed by: DESIGNED — Remains proposed in the absence of confirmation. [V10 §7E / C. Machine-inferred classifications]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.9.3 — Machine-inferred proposals | An inferred classification value. | supplies the value under consideration. | The value being considered for confirmation. | [V10 §7E / C. Machine-inferred classifications] |

SUB-PARTS: NONE

### C-7E.9.3.2 — Producer/model/rule
Stamp: DESIGNED    Source: [V10 §7E / C. Machine-inferred classifications]

ALONE
- What it is: DESIGNED — The production provenance required for a machine-inferred catalog proposal. [V10 §7E / C. Machine-inferred classifications]
- Takes in: DESIGNED — The producer/model/rule that supplied the inference. [V10 §7E / C. Machine-inferred classifications]
- Does: DESIGNED — Records it with the proposed value. [V10 §7E / C. Machine-inferred classifications]
- Gives out: DESIGNED — Traceable producer/model/rule information for the proposal. [V10 §7E / C. Machine-inferred classifications]
- Must never: DESIGNED — Leave the proposal's producer/model/rule unrecorded. [V10 §7E / C. Machine-inferred classifications]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.9.3 — Machine-inferred proposals | The producer/model/rule that supplied the inference. | identifies the proposal's producer. | Traceable producer/model/rule information for the proposal. | [V10 §7E / C. Machine-inferred classifications] |

SUB-PARTS: NONE

### C-7E.9.3.3 — Inference evidence
Stamp: DESIGNED    Source: [V10 §7E / C. Machine-inferred classifications]

ALONE
- What it is: DESIGNED — Evidence attached to a machine-inferred catalog proposal. [V10 §7E / C. Machine-inferred classifications]
- Takes in: DESIGNED — The evidence for the proposed classification. [V10 §7E / C. Machine-inferred classifications]
- Does: DESIGNED — Records that evidence with the proposal. [V10 §7E / C. Machine-inferred classifications]
- Gives out: DESIGNED — Evidence available for the stated confirmation routes. [V10 §7E / C. Machine-inferred classifications]
- Must never: DESIGNED — Omit evidence or treat an unconfirmed inference as settled merely because evidence information is present. [V10 §7E / C. Machine-inferred classifications]
- Fails closed by: DESIGNED — An inference without authorized confirmation stays a proposal; it is never settled because evidence is present. [V10 §7E / C. Machine-inferred classifications]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7E.9.3 — Machine-inferred proposals: evidence is required, and settlement still requires authorized confirmation. [V10 §7E / C. Machine-inferred classifications]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.9.3 — Machine-inferred proposals | The evidence for the proposed classification. | carries the proposal's evidence. | Evidence available for the stated confirmation routes. | [V10 §7E / C. Machine-inferred classifications] |

SUB-PARTS: NONE

### C-7E.9.3.4 — Inference confidence
Stamp: DESIGNED    Source: [V10 §7E / C. Machine-inferred classifications]

ALONE
- What it is: DESIGNED — Confidence information carried with the inferred classification. [V10 §7E / C. Machine-inferred classifications]
- Takes in: DESIGNED — The proposal's confidence. [V10 §7E / C. Machine-inferred classifications]
- Does: DESIGNED — Records confidence alongside the value, provenance, evidence and confirmation status. [V10 §7E / C. Machine-inferred classifications]
- Gives out: DESIGNED — Confidence as proposal metadata. [V10 §7E / C. Machine-inferred classifications]
- Must never: DESIGNED — Substitute confidence for the source-evidence, Ness or explicitly authorized-rule confirmation needed for settlement. [V10 §7E / C. Machine-inferred classifications]
- Fails closed by: DESIGNED — Keeps the classification proposed until confirmation supports settlement. [V10 §7E / C. Machine-inferred classifications]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7E.9.3 — Machine-inferred proposals: confidence is required metadata, and its presence does not remove the confirmation requirement. [V10 §7E / C. Machine-inferred classifications]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.9.3 — Machine-inferred proposals | The proposal's confidence. | carries confidence as proposal information. | Confidence as proposal metadata. | [V10 §7E / C. Machine-inferred classifications] |

SUB-PARTS: NONE

### C-7E.9.3.5 — Inference timestamp
Stamp: DESIGNED    Source: [V10 §7E / C. Machine-inferred classifications]

ALONE
- What it is: DESIGNED — The timestamp recorded with a catalog inference proposal. [V10 §7E / C. Machine-inferred classifications]
- Takes in: DESIGNED — The proposal's timestamp information. [V10 §7E / C. Machine-inferred classifications]
- Does: DESIGNED — Stores the timestamp alongside the proposal. [V10 §7E / C. Machine-inferred classifications]
- Gives out: DESIGNED — Timestamp information in the proposal record. [V10 §7E / C. Machine-inferred classifications]
- Must never: DESIGNED — Omit the required timestamp from a stored proposal. [V10 §7E / C. Machine-inferred classifications]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.9.3 — Machine-inferred proposals | The proposal's timestamp information. | carries the required timestamp. | Timestamp information in the proposal record. | [V10 §7E / C. Machine-inferred classifications] |

SUB-PARTS: NONE

### C-7E.9.3.6 — Inference confirmation status
Stamp: DESIGNED    Source: [V10 §7E / C. Machine-inferred classifications]

ALONE
- What it is: DESIGNED — The confirmation-status information retained with a catalog inference. [V10 §7E / C. Machine-inferred classifications]
- Takes in: DESIGNED — Whether source evidence, Ness or an explicitly authorized resolution rule confirms the proposal. [V10 §7E / C. Machine-inferred classifications]
- Does: DESIGNED — Records confirmation status separately from the proposed value and its confidence. [V10 §7E / C. Machine-inferred classifications]
- Gives out: DESIGNED — The proposal's stated confirmation condition. [V10 §7E / C. Machine-inferred classifications]
- Must never: DESIGNED — Manufacture confirmation from the existence, repetition or confidence of an unconfirmed machine inference. [V10 §7E / C. Machine-inferred classifications]
- Fails closed by: DESIGNED — Keeps an unconfirmed inference proposed rather than settled. [V10 §7E / C. Machine-inferred classifications]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7E.9.3 — Machine-inferred proposals: settlement requires one of the expressly permitted confirmation routes. [V10 §7E / C. Machine-inferred classifications]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.9.3 — Machine-inferred proposals | Whether source evidence, Ness or an explicitly authorized resolution rule confirms the proposal. | distinguishes confirmation from the existence of an inference. | The proposal's stated confirmation condition. | [V10 §7E / C. Machine-inferred classifications] |

SUB-PARTS: NONE

### C-7E.9.4 — Semantic-interpretation prohibition
Stamp: DESIGNED    Source: [V10 §7E / D. Semantic interpretation]

ALONE
- What it is: DESIGNED — Category D, which excludes semantic interpretation from Catalog. [V10 §7E / D. Semantic interpretation]
- Takes in: DESIGNED — A proposed operation concerning topic, intent, emotion, motive, psychological state, importance, relevance, meaning, relationship interpretation, truth judgment, summary, inferred life event or what someone “really meant.” [V10 §7E / D. Semantic interpretation]
- Does: DESIGNED — Keeps that work outside Catalog, with the Meaning Engine, reading layer, Story Layer or later systems. [V10 §7E / D. Semantic interpretation]
- Gives out: DESIGNED — The boundary reserving interpretation to its semantic owner. [V10 §7E / D. Semantic interpretation]
- Must never: DESIGNED — Perform any of those interpretations in Catalog or disguise them as source facts or mechanical enrichment. [V10 §7E / D. Semantic interpretation]
- Fails closed by: DESIGNED — Does not admit semantic interpretation as Catalog enrichment. [V10 §7E / D. Semantic interpretation]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7E.10 — Catalog boundary tests: an operation that interprets meaning belongs outside Catalog. [V10 §7E / BOUNDARY TESTS]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.9 — Enrichment categories | A proposed operation concerning topic, intent, emotion, motive, psychological state, importance, relevance, meaning, relationship interpretation, truth judgment, summary, inferred life event or what someone “really meant.” | meaning, interpretation and judgment do not belong in Catalog. | The boundary reserving interpretation to its semantic owner. | [V10 §7E / D. Semantic interpretation] |
| 2 · DESIGNED | C-7E.10 — Catalog boundary tests | A proposed operation concerning topic, intent, emotion, motive, psychological state, importance, relevance, meaning, relationship interpretation, truth judgment, summary, inferred life event or what someone “really meant.” | semantic work must remain outside Catalog. | The boundary reserving interpretation to its semantic owner. | [V10 §7E / D. Semantic interpretation] |

SUB-PARTS: NONE

### C-7E.10 — Catalog boundary tests
Stamp: DESIGNED    Source: [V10 §7E / BOUNDARY TESTS]

ALONE
- What it is: DESIGNED — The two checks distinguishing physical/source description from interpretation. [V10 §7E / BOUNDARY TESTS]
- Takes in: DESIGNED — A proposed Catalog description or enrichment. [V10 §7E / BOUNDARY TESTS]
- Does: DESIGNED — Asks whether it describes what the material physically/source-wise is or explains what it means, and whether reasonable readers could disagree because they interpret the content differently. [V10 §7E / BOUNDARY TESTS]
- Gives out: DESIGNED — An outside-Catalog placement when the second test identifies interpretive disagreement. [V10 §7E / BOUNDARY TESTS]
- Must never: DESIGNED — Keep interpretation inside Catalog merely by presenting it as metadata. [V10 §7E / D. Semantic interpretation] [V10 §7E / BOUNDARY TESTS]
- Fails closed by: DESIGNED — Treats a yes to the interpretive-disagreement test as outside Catalog. [V10 §7E / BOUNDARY TESTS]

TOGETHER
- Fed by: DESIGNED — C-7E.10.1 — Source-description test: distinguishes description of material from an explanation of meaning. [V10 §7E / BOUNDARY TESTS]
- Fed by: DESIGNED — C-7E.10.2 — Interpretive-disagreement test: identifies disagreement caused by interpreting the content. [V10 §7E / BOUNDARY TESTS]
- Gated by: DESIGNED — C-7E.9.4 — Semantic-interpretation prohibition: semantic work must remain outside Catalog. [V10 §7E / D. Semantic interpretation]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.9 — Enrichment categories | A proposed Catalog description or enrichment. | material-description and interpretation checks determine the boundary with semantic work. | An outside-Catalog placement when the second test identifies interpretive disagreement. | [V10 §7E / BOUNDARY TESTS] |
| 2 · DESIGNED | C-7E.9.4 — Semantic-interpretation prohibition | A proposed Catalog description or enrichment. | an operation that interprets meaning belongs outside Catalog. | An outside-Catalog placement when the second test identifies interpretive disagreement. | [V10 §7E / BOUNDARY TESTS] |
| 3 · DESIGNED | C-7E.10.1 — Source-description test | A proposed Catalog description or enrichment. | Catalog work must remain on the physical/source-description side of the boundary. | An outside-Catalog placement when the second test identifies interpretive disagreement. | [V10 §7E / BOUNDARY TESTS] |

SUB-PARTS: C-7E.10.1 — Source-description test; C-7E.10.2 — Interpretive-disagreement test

### C-7E.10.1 — Source-description test
Stamp: DESIGNED    Source: [V10 §7E / BOUNDARY TESTS]

ALONE
- What it is: DESIGNED — The check for physical/source description versus explanation of meaning. [V10 §7E / BOUNDARY TESTS]
- Takes in: DESIGNED — The proposed description of captured material. [V10 §7E / BOUNDARY TESTS]
- Does: DESIGNED — Asks whether it describes what the material physically/source-wise is or explains what the material means. [V10 §7E / BOUNDARY TESTS]
- Gives out: DESIGNED — The distinction between material description and interpretation. [V10 §7E / BOUNDARY TESTS]
- Must never: DESIGNED — Treat an explanation of meaning as Catalog's physical/source description. [V10 §7E / D. Semantic interpretation] [V10 §7E / BOUNDARY TESTS]
- Fails closed by: DESIGNED — Keeps semantic interpretation outside Catalog. [V10 §7E / D. Semantic interpretation]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7E.10 — Catalog boundary tests: Catalog work must remain on the physical/source-description side of the boundary. [V10 §7E / BOUNDARY TESTS]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.10 — Catalog boundary tests | The proposed description of captured material. | distinguishes description of material from an explanation of meaning. | The distinction between material description and interpretation. | [V10 §7E / BOUNDARY TESTS] |

SUB-PARTS: NONE

### C-7E.10.2 — Interpretive-disagreement test
Stamp: DESIGNED    Source: [V10 §7E / BOUNDARY TESTS]

ALONE
- What it is: DESIGNED — The check for disagreement caused by interpreting content differently. [V10 §7E / BOUNDARY TESTS]
- Takes in: DESIGNED — A proposed classification or description of the material. [V10 §7E / BOUNDARY TESTS]
- Does: DESIGNED — Asks whether two reasonable readers could disagree because they interpret the content differently. [V10 §7E / BOUNDARY TESTS]
- Gives out: DESIGNED — An outside-Catalog determination when the answer is yes. [V10 §7E / BOUNDARY TESTS]
- Must never: DESIGNED — Retain such interpretive work in Catalog after a yes to this test. [V10 §7E / BOUNDARY TESTS]
- Fails closed by: DESIGNED — Places that work outside Catalog. [V10 §7E / BOUNDARY TESTS]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.10 — Catalog boundary tests | A proposed classification or description of the material. | identifies disagreement caused by interpreting the content. | An outside-Catalog determination when the answer is yes. | [V10 §7E / BOUNDARY TESTS] |

SUB-PARTS: NONE

### C-7E.11 — Held-content access boundary
Stamp: DESIGNED    Source: [MAP C-7E] [V10 §7L / LINKABLE OBJECT TYPES] [V10 §7M / OBJECT TYPES USED]

ALONE
- What it is: DESIGNED — The boundary that keeps held pre-ingest raw content outside downstream semantic analysis. [MAP C-7E]
- Takes in: DESIGNED — Held material, safe source-carried metadata, lifecycle state and blocker information. [MAP C-7E]
- Does: DESIGNED — Permits metadata-only references to those three safe information classes while excluding held raw content from Person-Box semantic analysis and Computed View ranking, interpretation and output. [V10 §7L / LINKABLE OBJECT TYPES] [V10 §7M / OBJECT TYPES USED] [MAP C-7E]
- Gives out: DESIGNED — Safe metadata-only references that never reveal or reconstruct the held content. [MAP C-7E]
- Must never: DESIGNED — Expose or reconstruct held content through metadata references, treat mere preservation as access authorization, or extend any future generic inspection mode to a sealed TSC. Sealed-TSC inspection is prohibited entirely: no person, token, mode or authorized inspection path exists. [MAP C-7E] [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY] [V10 §7E-TSC / 15. TSC INSPECTION]
- Fails closed by: DESIGNED — Holds raw content outside the Meaning Engine, LMAC, context retrieval and downstream use until governing authorization and blockers clear through normal Catalog rules. [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY]

TOGETHER
- Fed by: ACCEPTED — C-STORE.5.5.8.6 — source-provided metadata: supplies source metadata whose permitted safe portion may be referenced without reinterpretation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10] [MAP C-7E]
- Fed by: DESIGNED — C-7E.5.5 — Lifecycle state: supplies the lifecycle information eligible for a metadata-only reference. [MAP C-7E]
- Fed by: DESIGNED — C-7E.5.2 — Blocker list: supplies blocker information eligible for that restricted reference. [MAP C-7E]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): internal use and visible output remain subject to privacy, protection levels, compartments and influence-removal instructions. [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY]
- Gated by: DESIGNED — C-TSC — Temporary Session Cache (§7E-TSC): a sealed TSC has no inspection exception, even for Ness. [V10 §7E-TSC / 15. TSC INSPECTION]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E) | Held material, safe source-carried metadata, lifecycle state and blocker information. | held raw content stays outside downstream semantic use. | Safe metadata-only references that never reveal or reconstruct the held content. | [MAP C-7E] |
| 2 · DESIGNED | C-7E.5 — Unified pre-ingest record | Held material, safe source-carried metadata, lifecycle state and blocker information. | held raw content remains unavailable to downstream semantic analysis. | Safe metadata-only references that never reveal or reconstruct the held content. | [MAP C-7E] |
| 3 · DESIGNED | C-7E.6.1 — held | Held material, safe source-carried metadata, lifecycle state and blocker information. | holding does not grant downstream semantic access. | Safe metadata-only references that never reveal or reconstruct the held content. | [MAP C-7E] |
| 4 · DESIGNED | C-7L — Person-Boxes (§7L) | Safe source-carried metadata, lifecycle state and blocker information for a held item. | Permits metadata-only Person-Box references without exposing held content to semantic analysis. | No held raw content is revealed or reconstructed. | [V10 §7L / LINKABLE OBJECT TYPES] [MAP C-7E] |
| 5 · DESIGNED | C-7M — Computed View (§7M) | Safe metadata, lifecycle state and blockers for a held item. | Permits metadata-only references while excluding raw held content from ranking, interpretation and output. | Held content remains outside semantic use until the governing conditions clear. | [V10 §7M / OBJECT TYPES USED] [MAP C-7E] |
| 6 · DESIGNED | C-7D — Living State Web (§7D) | Permitted readings, tellings, clashes, Ness-response events and result evidence with root provenance. | Gates this place: any permitted pre-ingest reference is safe metadata only—source-carried safe metadata, lifecycle state and blockers; held raw content remains excluded. | Nothing in this card. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] [V10 §7D] [MAP C-7D] [V10 §7O] |
| 7 · DESIGNED | C-7L.8 — Person-Box held-material metadata boundary | Safe source-carried metadata, lifecycle state and blocker information from held records. | Supplies safe source-carried held metadata, lifecycle state and blockers, with raw content unavailable to this semantic consumer. | Nothing in this card. | [V10 §7L] [V10 §7E] |
| 8 · ACCEPTED | C-7M.5.5.10 — Computed View safe pre-ingest metadata references | Source-carried safe metadata, lifecycle state and blocker information. | Supplies safe held metadata with raw content excluded from semantic use. | Nothing in this card. | [V10 §7M] [V10 §7E] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §8] [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §11] |
| 9 · ACCEPTED | C-7M.13 — Computed View metadata-only held-content boundary | Authorized safe metadata-only references, never held raw content or reconstructed content. | Supplies the existing DESIGNED safe metadata/lifecycle/blocker source interface. | Nothing in this card. | [V10 §7M] [04/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7E.12 — Accepted root-write handoff
Stamp: ACCEPTED    Source: [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The mandatory Catalog-to-B11 handoff before the shared `append_root()` commit boundary, targeting the active writable batch. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.1] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — A prepared seven-field payload conforming to `schema_compat_ref`; committed capture-authorization, exclusion-result, blocker-clearance, speaker-resolution and catalog-eligibility evidence references; stable caller-domain ingest identity based on `capture_id`; and provenance labels. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.1] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.2] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Resolves the root write through B11, whose checks are mechanical: shape, committed evidence-reference existence, identity/idempotency and target state. Catalog retains eligibility meaning, pre-ingest holding and blocker policy. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Uses the proposed `ingest_idempotency_key` bound only to authoritative `capture_id` and root-ingestion operation type, globally and independently of epoch. `schema_version` is not part of that key; a schema change cannot silently create a second root for the capture. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.2]
- Does: ACCEPTED — Preserves separate source Origins and source/import/record-creation time families. The proposed `root_schema_v2` design carries `thread_id`, optional `display_label`, typed `source_times`, `imported_at` and `record_created_at`; proposed `origin_relationship_record` links are separate, append-only and written only after both endpoints durably exist. These designs do not activate fields on live v1 roots. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3.2] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3.3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10]
- Gives out: ACCEPTED — B11's proposed caller outcomes: `committed` returns the durable root and owning `batch_id` [proposed]; `duplicate_absorbed` returns the existing root/batch without another commit; `rejected(reason)` is a mechanical refusal; `interrupted` has durable evidence of non-commit and permits lookup-first technical retry under the same key; `indeterminate` means commit status is unknowable and requires lookup-first resolution without blind retry. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.5]
- Gives out: ACCEPTED — A terminal acknowledgement only after the matching parent terminal operation record is durable. Root durability is established at WB2; later log/index failure never uncommits it. Rebuildable PR registrations do not gate acknowledgement, which carries honest coverage if they are incomplete. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.4]
- Must never: ACCEPTED — Bypass the single shared B11/§7E boundary, write directly to a root file, reopen or append to the sealed 5,521-root batch, let B11 decide upstream eligibility, or claim success before the permanent operation record exists. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.4] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Refuses admission when required evidence references, schema compatibility, root identity, historical ownership coverage or target state cannot be validated. An indeterminate result gets no blind retry; committed roots remain preserved and no sealed batch is used as fallback. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §12]

TOGETHER
- Fed by: DESIGNED — C-7E.1.2 — Root-ingestion gate: supplies catalog-eligible material only after its required fields and blockers are resolved. [V10 §7E / TWO GATES]
- Gated by: ACCEPTED — C-STORE.4 — B11 — Active Writable-Batch / Sealed Multi-Box Architecture: all root writes must pass its accepted selection, global-claim, ownership, fence, historical-coverage, recovery and fail-closed contracts. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gated by: ACCEPTED — C-STORE.4.12.1 — C-7E catalog / pre-ingest promotion: the caller must supply its payload, evidence references, stable identity basis and provenance labels for the mechanical checks. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13]
- Gated by: ACCEPTED — C-STORE.4.6.4 — Acknowledgement rule: the matching parent terminal record must be durable before the caller receives its terminal outcome. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.4]
- Gated by: ACCEPTED — C-STORE.5.1 — Origin preservation policy: separate source items and separate time families must be preserved without deciding meaning. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3]
- Gated by: ACCEPTED — C-STORE.5.2 — Bundle 6 operation protections: Bundle 6 operations retain stable identities, atomic records, structural idempotency, bounded retry, committed-state recovery and one-operation/one-log protection. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gated by: ACCEPTED — C-STORE.5.5 — B21 — Future root schema and pre-ingest schemas: an item must satisfy its declared schema; future fields require the gated activation route and never silently migrate existing roots. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10]
- Changes: ACCEPTED — C-STORE.4.6 — Root-write targeting, transaction boundaries, and outcome contract: submits the eligible root through the defined WB0–WB4 boundaries and receives the proposed outcome vocabulary. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7E.1.2 — Root-ingestion gate | A prepared seven-field payload conforming to `schema_compat_ref`; committed capture-authorization, exclusion-result, blocker-clearance, speaker-resolution and catalog-eligibility evidence references; stable caller-domain ingest identity based on `capture_id`; and provenance labels. | eligible roots still require the shared B11 boundary and its committed upstream evidence. | B11's proposed caller outcomes: `committed` returns the durable root and owning `batch_id` [proposed]; `duplicate_absorbed` returns the existing root/batch without another commit; `rejected(reason)` is a mechanical refusal; `interrupted` has durable evidence of non-commit and permits lookup-first technical retry under the same key; `indeterminate` means commit status is unknowable and requires lookup-first resolution without blind retry. A terminal acknowledgement only after the matching parent terminal operation record is durable. Root durability is established at WB2; later log/index failure never uncommits it. Rebuildable PR registrations do not gate acknowledgement, which carries honest coverage if they are incomplete. | [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.1] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.2] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.5] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.4] |
| 2 · ACCEPTED | C-7E.5.6 — Resulting root_id | A prepared seven-field payload conforming to `schema_compat_ref`; committed capture-authorization, exclusion-result, blocker-clearance, speaker-resolution and catalog-eligibility evidence references; stable caller-domain ingest identity based on `capture_id`; and provenance labels. | supplies the existing or newly committed root identity from the durable B11 outcome. | B11's proposed caller outcomes: `committed` returns the durable root and owning `batch_id` [proposed]; `duplicate_absorbed` returns the existing root/batch without another commit; `rejected(reason)` is a mechanical refusal; `interrupted` has durable evidence of non-commit and permits lookup-first technical retry under the same key; `indeterminate` means commit status is unknowable and requires lookup-first resolution without blind retry. A terminal acknowledgement only after the matching parent terminal operation record is durable. Root durability is established at WB2; later log/index failure never uncommits it. Rebuildable PR registrations do not gate acknowledgement, which carries honest coverage if they are incomplete. | [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.5] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.1] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.2] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.4] |
| 3 · ACCEPTED | C-7E.6.3 — promoting | A prepared seven-field payload conforming to `schema_compat_ref`; committed capture-authorization, exclusion-result, blocker-clearance, speaker-resolution and catalog-eligibility evidence references; stable caller-domain ingest identity based on `capture_id`; and provenance labels. | root writing must pass B11's mechanical checks and durable outcome boundary. | B11's proposed caller outcomes: `committed` returns the durable root and owning `batch_id` [proposed]; `duplicate_absorbed` returns the existing root/batch without another commit; `rejected(reason)` is a mechanical refusal; `interrupted` has durable evidence of non-commit and permits lookup-first technical retry under the same key; `indeterminate` means commit status is unknowable and requires lookup-first resolution without blind retry. A terminal acknowledgement only after the matching parent terminal operation record is durable. Root durability is established at WB2; later log/index failure never uncommits it. Rebuildable PR registrations do not gate acknowledgement, which carries honest coverage if they are incomplete. | [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.1] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.4] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.2] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.5] |
| 4 · ACCEPTED | C-7E.6.4 — promoted | A prepared seven-field payload conforming to `schema_compat_ref`; committed capture-authorization, exclusion-result, blocker-clearance, speaker-resolution and catalog-eligibility evidence references; stable caller-domain ingest identity based on `capture_id`; and provenance labels. | supplies the durably acknowledged root identity and owning batch. | B11's proposed caller outcomes: `committed` returns the durable root and owning `batch_id` [proposed]; `duplicate_absorbed` returns the existing root/batch without another commit; `rejected(reason)` is a mechanical refusal; `interrupted` has durable evidence of non-commit and permits lookup-first technical retry under the same key; `indeterminate` means commit status is unknowable and requires lookup-first resolution without blind retry. A terminal acknowledgement only after the matching parent terminal operation record is durable. Root durability is established at WB2; later log/index failure never uncommits it. Rebuildable PR registrations do not gate acknowledgement, which carries honest coverage if they are incomplete. | [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.4] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.5] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.1] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.2] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13] |
| 5 · ACCEPTED | C-9A.7.1.5 — Engine and Catalog ingest stage | Eligible captured material after the applicable image and privacy boundaries. | Gates this place: the accepted root-write handoff and active-batch write conditions must hold. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| 6 · ACCEPTED | C-9A.7.7 — Consumed Bundle 6 operation contract | Stable operation identity, deterministic duplicate key, durable checkpoints, purpose authorization and root-write eligibility where relevant. | Gates this place: any root write must satisfy the accepted active-batch handoff. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| 7 · ACCEPTED | C-14.7 — Shared capture and reference-operation protections | A real operation, stable operation identity, deterministic duplicate key, committed state and its applicable authority. | Gates this place: requires root-producing work to use the accepted B11 Catalog handoff. | Nothing in this card. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-7E.13 — Catalog operation records
Stamp: DESIGNED    Source: [MAP C-7E] [V10 §0B / ONE REAL OPERATION, ONE LOG]

ALONE
- What it is: DESIGNED — The Catalog's required operation records. [MAP C-7E]
- Takes in: DESIGNED — Each capture, blocker set and clear with reason, promotion, exclusion and capture-error. [MAP C-7E]
- Does: DESIGNED — Records each real operation once; record creation does not recursively produce another log about logging. [MAP C-7E] [V10 §0B / ONE REAL OPERATION, ONE LOG]
- Gives out: DESIGNED — Catalog operation records under privacy/access and applicable identity/security authorization. [MAP C-7E]
- Must never: DESIGNED — Skip a required event, omit a blocker-change reason, create a second operational log for the same real operation, or let records bypass access rules. [MAP C-7E] [V10 §0B / ONE REAL OPERATION, ONE LOG]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7E.13.1 — Capture record: supplies each capture event. [MAP C-7E]
- Fed by: DESIGNED — C-7E.13.2 — Blocker-set record: supplies each blocker set with its reason. [MAP C-7E]
- Fed by: DESIGNED — C-7E.13.3 — Blocker-clear record: supplies each blocker clear with its reason. [MAP C-7E]
- Fed by: DESIGNED — C-7E.13.4 — Promotion record: supplies each promotion event. [MAP C-7E]
- Fed by: DESIGNED — C-7E.13.5 — Exclusion record: supplies each exclusion event. [MAP C-7E]
- Fed by: DESIGNED — C-7E.13.6 — Capture-error record: supplies each capture-error event. [MAP C-7E]
- Gated by: DESIGNED — C-7B.10.5.1 — One real operation one log: a real operation produces one log without recursive log creation. [V10 §0B / ONE REAL OPERATION, ONE LOG]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): records remain subject to privacy/access and authorization rules. [MAP C-7E]
- Gated by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): applicable identity/security authorization governs record access. [MAP C-7E] [MAP C-SACL]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E) | Each capture, blocker set and clear with reason, promotion, exclusion and capture-error. | each specified capture, blocker change, promotion, exclusion and capture-error must be recorded. | Catalog operation records under privacy/access and applicable identity/security authorization. | [MAP C-7E] |
| 2 · DESIGNED | C-7E.13.1 — Capture record | Each capture, blocker set and clear with reason, promotion, exclusion and capture-error. | each real capture requires one record under the applicable access rules. | Catalog operation records under privacy/access and applicable identity/security authorization. | [MAP C-7E] [V10 §0B / ONE REAL OPERATION, ONE LOG] |
| 3 · DESIGNED | C-7E.13.4 — Promotion record | Each capture, blocker set and clear with reason, promotion, exclusion and capture-error. | each promotion requires its record under one-operation/one-log and access rules. | Catalog operation records under privacy/access and applicable identity/security authorization. | [MAP C-7E] [V10 §0B / ONE REAL OPERATION, ONE LOG] |
| 4 · DESIGNED | C-7E.13.6 — Capture-error record | Each capture, blocker set and clear with reason, promotion, exclusion and capture-error. | every capture-error requires a record under the applicable access rules. | Catalog operation records under privacy/access and applicable identity/security authorization. | [MAP C-7E] |

SUB-PARTS: C-7E.13.1 — Capture record; C-7E.13.2 — Blocker-set record; C-7E.13.3 — Blocker-clear record; C-7E.13.4 — Promotion record; C-7E.13.5 — Exclusion record; C-7E.13.6 — Capture-error record; C-7E.13.7 — Blocker-change reason

### C-7E.13.1 — Capture record
Stamp: DESIGNED    Source: [MAP C-7E]

ALONE
- What it is: DESIGNED — The record of each Catalog capture. [MAP C-7E]
- Takes in: DESIGNED — A capture event. [MAP C-7E]
- Does: DESIGNED — Records the capture under the Catalog logging requirement. [MAP C-7E]
- Gives out: DESIGNED — A permanent operation record for that real capture. [MAP C-7E] [V10 §0B / ONE REAL OPERATION, ONE LOG]
- Must never: DESIGNED — Leave a capture unrecorded or produce duplicate operational logs for the same capture. [MAP C-7E] [V10 §0B / ONE REAL OPERATION, ONE LOG]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7E.13 — Catalog operation records: each real capture requires one record under the applicable access rules. [MAP C-7E] [V10 §0B / ONE REAL OPERATION, ONE LOG]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.13 — Catalog operation records | A capture event. | supplies each capture event. | A permanent operation record for that real capture. | [MAP C-7E] [V10 §0B / ONE REAL OPERATION, ONE LOG] |
| 2 · ACCEPTED | C-14.5.4 — Label inside the capture transaction | The capture, proposed typed label and source attribution fields. | Takes this place's change: includes assignment in the existing capture record, never a separate label log. | Includes assignment in the existing capture record, never a separate label log. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §7] |

SUB-PARTS: NONE

### C-7E.13.2 — Blocker-set record
Stamp: DESIGNED    Source: [MAP C-7E]

ALONE
- What it is: DESIGNED — The record of a blocker being set on an item. [MAP C-7E]
- Takes in: DESIGNED — The blocker-set event and its reason. [MAP C-7E]
- Does: DESIGNED — Records each blocker set with the reason. [MAP C-7E]
- Gives out: DESIGNED — The recorded blocker addition and its basis. [MAP C-7E]
- Must never: DESIGNED — Omit the blocker-set event or its reason. [MAP C-7E]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7E.13.7 — Blocker-change reason: supplies the reason that must accompany the set event. [MAP C-7E]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.5.2 — Blocker list | The blocker-set event and its reason. | provides each blocker addition and its reason for logging. | The recorded blocker addition and its basis. | [MAP C-7E] |
| 2 · DESIGNED | C-7E.13 — Catalog operation records | The blocker-set event and its reason. | supplies each blocker set with its reason. | The recorded blocker addition and its basis. | [MAP C-7E] |

SUB-PARTS: NONE

### C-7E.13.3 — Blocker-clear record
Stamp: DESIGNED    Source: [MAP C-7E]

ALONE
- What it is: DESIGNED — The record of a blocker actually being cleared. [MAP C-7E]
- Takes in: DESIGNED — The blocker-clear event and its reason. [MAP C-7E]
- Does: DESIGNED — Records each clearance with its reason. [MAP C-7E]
- Gives out: DESIGNED — The recorded blocker clearance and its basis. [MAP C-7E]
- Must never: DESIGNED — Omit a clearance or its reason, or clear a blocker before its actual requirement is resolved. [MAP C-7E] [DD §3C]
- Fails closed by: DESIGNED — Keeps an unresolved requirement blocked instead of claiming it cleared. [DD §3C]

TOGETHER
- Fed by: DESIGNED — C-7E.13.7 — Blocker-change reason: supplies the required reason for the clearance. [MAP C-7E]
- Gated by: DESIGNED — C-7E.5.2 — Blocker list: clearance requires actual resolution of that blocker, independently of other blockers. [DD §3C] [DD §3N]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.5.2 — Blocker list | The blocker-clear event and its reason. | provides each actual blocker clearance and its reason for logging. | The recorded blocker clearance and its basis. | [MAP C-7E] |
| 2 · DESIGNED | C-7E.13 — Catalog operation records | The blocker-clear event and its reason. | supplies each blocker clear with its reason. | The recorded blocker clearance and its basis. | [MAP C-7E] |

SUB-PARTS: NONE

### C-7E.13.4 — Promotion record
Stamp: DESIGNED    Source: [MAP C-7E]

ALONE
- What it is: DESIGNED — The Catalog operation record for a promotion. [MAP C-7E]
- Takes in: DESIGNED — A promotion event. [MAP C-7E]
- Does: DESIGNED — Records each promotion as a real operation. [MAP C-7E] [V10 §0B / ONE REAL OPERATION, ONE LOG]
- Gives out: DESIGNED — The promotion's operation record. [MAP C-7E]
- Must never: DESIGNED — Leave a promotion unrecorded or create a second parent operational record for the same real operation. [MAP C-7E] [V10 §0B / ONE REAL OPERATION, ONE LOG]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7E.13 — Catalog operation records: each promotion requires its record under one-operation/one-log and access rules. [MAP C-7E] [V10 §0B / ONE REAL OPERATION, ONE LOG]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.6.4 — promoted | A promotion event. | supplies the promotion event for logging. | The promotion's operation record. | [MAP C-7E] |
| 2 · DESIGNED | C-7E.13 — Catalog operation records | A promotion event. | supplies each promotion event. | The promotion's operation record. | [MAP C-7E] |

SUB-PARTS: NONE

### C-7E.13.5 — Exclusion record
Stamp: DESIGNED    Source: [MAP C-7E]

ALONE
- What it is: DESIGNED — The Catalog record of an exclusion operation. [MAP C-7E]
- Takes in: DESIGNED — An exclusion event. [MAP C-7E]
- Does: DESIGNED — Records each exclusion. [MAP C-7E]
- Gives out: DESIGNED — An exclusion operation record subject to the privacy boundary. [MAP C-7E] [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]
- Must never: DESIGNED — Skip an exclusion record or reconstruct excluded raw content in ordinary exclusion metadata. [MAP C-7E] [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]
- Fails closed by: DESIGNED — Keeps excluded raw content out of ordinary records; only the safe remainder and non-reconstructive exclusion metadata stay there. [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7E.4 — Privacy and exclusion precedence: ordinary records retain only non-reconstructive exclusion metadata and any safe remainder. [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.4 — Privacy and exclusion precedence | An exclusion event. | supplies the exclusion operation for recording. | An exclusion operation record subject to the privacy boundary. | [MAP C-7E] [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE] |
| 2 · DESIGNED | C-7E.13 — Catalog operation records | An exclusion event. | supplies each exclusion event. | An exclusion operation record subject to the privacy boundary. | [MAP C-7E] [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE] |

SUB-PARTS: NONE

### C-7E.13.6 — Capture-error record
Stamp: DESIGNED    Source: [MAP C-7E]

ALONE
- What it is: DESIGNED — The Catalog record of each capture-error event. [MAP C-7E]
- Takes in: DESIGNED — A capture-error event from the explicit failure path. [MAP C-7E] [V10 §7E / DESIGN BOUNDARY]
- Does: DESIGNED — Records the event while the capture-error path preserves available material. [MAP C-7E] [V10 §7E / DESIGN BOUNDARY]
- Gives out: DESIGNED — The capture-error operation record. [MAP C-7E]
- Must never: DESIGNED — Leave a capture-error event unrecorded or silently drop the available capture. [MAP C-7E] [V10 §7E / DESIGN BOUNDARY]
- Fails closed by: DESIGNED — Preserves the available material in the explicit capture-error path and records the error instead of silently dropping it. [V10 §7E / DESIGN BOUNDARY] [MAP C-7E]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7E.13 — Catalog operation records: every capture-error requires a record under the applicable access rules. [MAP C-7E]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.3 — Capture-error path | A capture-error event from the explicit failure path. | supplies the capture-error event that must be recorded. | The capture-error operation record. | [MAP C-7E] [V10 §7E / DESIGN BOUNDARY] |
| 2 · DESIGNED | C-7E.13 — Catalog operation records | A capture-error event from the explicit failure path. | supplies each capture-error event. | The capture-error operation record. | [MAP C-7E] [V10 §7E / DESIGN BOUNDARY] |

SUB-PARTS: NONE

### C-7E.13.7 — Blocker-change reason
Stamp: DESIGNED    Source: [MAP C-7E]

ALONE
- What it is: DESIGNED — The reason required for each blocker set or clear. [MAP C-7E]
- Takes in: DESIGNED — Why the blocker was set or cleared. [MAP C-7E]
- Does: DESIGNED — Records the reason with the corresponding blocker change. [MAP C-7E]
- Gives out: DESIGNED — A blocker-change record carrying its reason. [MAP C-7E]
- Must never: DESIGNED — Leave the reason absent from a blocker set or clear. [MAP C-7E]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7E.13.2 — Blocker-set record | Why the blocker was set or cleared. | supplies the reason that must accompany the set event. | A blocker-change record carrying its reason. | [MAP C-7E] |
| 2 · DESIGNED | C-7E.13.3 — Blocker-clear record | Why the blocker was set or cleared. | supplies the required reason for the clearance. | A blocker-change record carrying its reason. | [MAP C-7E] |

SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece continuation entries

Both endpoints are named together; the earlier files remain unchanged.

| Using card | Defining or supplying card | Reciprocal entry | Source |
|---|---|---|---|
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | C-14 — Chat Front Door (§14) | DESIGNED — USED BY continuation for Fed by: supplies live-chat captures to the common intake boundary. | [MAP C-7E] |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | C-8 — Research Pipeline / Knowledge Catcher (§8) | DESIGNED — USED BY continuation for Fed by: supplies eligible research-side captures through its Catalog entry. | [MAP C-7E] |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | C-9A — Image ingest front door (§9A) | DESIGNED — USED BY continuation for Fed by: supplies image captures with the same minimum envelope. | [MAP C-7E] |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | C-23 — Mobile App, three modes (§23) | DESIGNED — USED BY continuation for Fed by: supplies mobile front-door captures. | [MAP C-7E] |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | C-TSC — Temporary Session Cache (§7E-TSC) | DESIGNED — USED BY continuation for Fed by: organizes session-held material inside the shared pre-ingest store and supplies authorized items through the Catalog path. | [MAP C-7E] [DD §3N] |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | C-BOP — Behavioral Observation Processing (§25.1/§26) | ACCEPTED — USED BY continuation for Fed by: routes authorized observation captures through this single Catalog entry, never through a second root-writing path. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | C-OOP — Outcome Observation Processing (§26) | ACCEPTED — USED BY continuation for Fed by: routes `outcome_observation` roots through the same Catalog entry. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §13] |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | C-DETECT — Speaker detector (fallback; investigated, not deployed) (§11) | DESIGNED — USED BY continuation for Fed by: supplies an uncertain candidate only when source attribution is absent. | [MAP C-DETECT] |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | C-STORE — Accretive store & sealed roots (§6B) | ACCEPTED — USED BY continuation for Changes: submits eligible roots only through the shared B11/`append_root()` boundary into its active writable batch. | [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13] |
| C-7E.2 — Minimum intake envelope | C-STORE.5.5.8.1 — capture_id | ACCEPTED — USED BY continuation for Fed by: carries the stable unique capture identity preserved by the accepted handoff. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10] [V10 §7E / MINIMUM INTAKE ENVELOPE] |
| C-7E.2 — Minimum intake envelope | C-STORE.5.5.8.2 — raw payload or immutable reference | ACCEPTED — USED BY continuation for Fed by: carries the exact payload or its stable immutable reference. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10] [V10 §7E / MINIMUM INTAKE ENVELOPE] |
| C-7E.2 — Minimum intake envelope | C-STORE.5.5.8.3 — capture timestamp | ACCEPTED — USED BY continuation for Fed by: carries the capture time in the unchanged envelope. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10] [V10 §7E / MINIMUM INTAKE ENVELOPE] |
| C-7E.2 — Minimum intake envelope | C-STORE.5.5.8.4 — front-door/source type | ACCEPTED — USED BY continuation for Fed by: identifies the capture's front door or source type. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10] [V10 §7E / MINIMUM INTAKE ENVELOPE] |
| C-7E.2 — Minimum intake envelope | C-STORE.5.5.8.5 — payload format/media type | ACCEPTED — USED BY continuation for Fed by: identifies the payload's format or media type. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10] [V10 §7E / MINIMUM INTAKE ENVELOPE] |
| C-7E.2 — Minimum intake envelope | C-STORE.5.5.8.6 — source-provided metadata | ACCEPTED — USED BY continuation for Fed by: preserves source metadata without reinterpretation. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10] [V10 §7E / MINIMUM INTAKE ENVELOPE] |
| C-7E.2 — Minimum intake envelope | C-STORE.5.5.8.7 — capture provenance | ACCEPTED — USED BY continuation for Fed by: traces how and where the capture occurred. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10] [V10 §7E / MINIMUM INTAKE ENVELOPE] |
| C-7E.4 — Privacy and exclusion precedence | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED — USED BY continuation for Gated by: its exclusion, separation and protection-level rules override Catalog's general preservation rule. | [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE] |
| C-7E.5.2 — Blocker list | C-DETECT.2.4 — Unattended speaker hold | DESIGNED — USED BY continuation for Fed by: identifies the unresolved-speaker condition for unattended material. | [V10 §7E / SPEAKER RESOLUTION RULE] |
| C-7E.5.2 — Blocker list | C-TSC — Temporary Session Cache (§7E-TSC) | DESIGNED — USED BY continuation for Gated by: its fingerprint blocker clears only through the purpose-bound token and fresh recognized-Ness authorization at consumption. | [DD §3N] |
| C-7E.7 — Catalog speaker resolution | C-DETECT — Speaker detector (fallback; investigated, not deployed) (§11) | DESIGNED — USED BY continuation for Fed by: may supply an uncertain candidate only for a role-less source. | [MAP C-DETECT] |
| C-7E.7 — Catalog speaker resolution | C-DETECT.2 — Settled speaker rule | DESIGNED — USED BY continuation for Gated by: source attribution wins; fallback candidates require authorized confirmation and never write role directly. | [MAP C-DETECT] |
| C-7E.8 — Source-title and thread resolution | C-STORE.5.4 — B20 — source_title alias/correction layer | ACCEPTED — USED BY continuation for Gated by: later label clarification is append-only beside the original; aliases never change canonical thread identity or membership. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §9] |
| C-7E.8 — Source-title and thread resolution | C-STORE.5.5 — B21 — Future root schema and pre-ingest schemas | ACCEPTED — USED BY continuation for Gated by: the future stable non-semantic `thread_id` remains separate from optional `display_label`; no live v1 field is activated or renamed by the design. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10] |
| C-7E.9.1 — Source-carried facts | C-STORE.5.5.8.6 — source-provided metadata | ACCEPTED — USED BY continuation for Fed by: supplies the unchanged source information in the intake envelope. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10] [V10 §7E / MINIMUM INTAKE ENVELOPE] |
| C-7E.11 — Held-content access boundary | C-STORE.5.5.8.6 — source-provided metadata | ACCEPTED — USED BY continuation for Fed by: supplies source metadata whose permitted safe portion may be referenced without reinterpretation. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10] [MAP C-7E] |
| C-7E.11 — Held-content access boundary | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED — USED BY continuation for Gated by: internal use and visible output remain subject to privacy, protection levels, compartments and influence-removal instructions. | [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY] |
| C-7E.11 — Held-content access boundary | C-TSC — Temporary Session Cache (§7E-TSC) | DESIGNED — USED BY continuation for Gated by: a sealed TSC has no inspection exception, even for Ness. | [V10 §7E-TSC / 15. TSC INSPECTION] |
| C-7E.12 — Accepted root-write handoff | C-STORE.4 — B11 — Active Writable-Batch / Sealed Multi-Box Architecture | ACCEPTED — USED BY continuation for Gated by: all root writes must pass its accepted selection, global-claim, ownership, fence, historical-coverage, recovery and fail-closed contracts. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| C-7E.12 — Accepted root-write handoff | C-STORE.4.12.1 — C-7E catalog / pre-ingest promotion | ACCEPTED — USED BY continuation for Gated by: the caller must supply its payload, evidence references, stable identity basis and provenance labels for the mechanical checks. | [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13] |
| C-7E.12 — Accepted root-write handoff | C-STORE.4.6.4 — Acknowledgement rule | ACCEPTED — USED BY continuation for Gated by: the matching parent terminal record must be durable before the caller receives its terminal outcome. | [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.4] |
| C-7E.12 — Accepted root-write handoff | C-STORE.5.1 — Origin preservation policy | ACCEPTED — USED BY continuation for Gated by: separate source items and separate time families must be preserved without deciding meaning. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3] |
| C-7E.12 — Accepted root-write handoff | C-STORE.5.2 — Bundle 6 operation protections | ACCEPTED — USED BY continuation for Gated by: Bundle 6 operations retain stable identities, atomic records, structural idempotency, bounded retry, committed-state recovery and one-operation/one-log protection. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| C-7E.12 — Accepted root-write handoff | C-STORE.5.5 — B21 — Future root schema and pre-ingest schemas | ACCEPTED — USED BY continuation for Gated by: an item must satisfy its declared schema; future fields require the gated activation route and never silently migrate existing roots. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §10] |
| C-7E.12 — Accepted root-write handoff | C-STORE.4.6 — Root-write targeting, transaction boundaries, and outcome contract | ACCEPTED — USED BY continuation for Changes: submits the eligible root through the defined WB0–WB4 boundaries and receives the proposed outcome vocabulary. | [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7] |
| C-7E.13 — Catalog operation records | C-7B.10.5.1 — One real operation one log | DESIGNED — USED BY continuation for Gated by: a real operation produces one log without recursive log creation. | [V10 §0B / ONE REAL OPERATION, ONE LOG] |
| C-7E.13 — Catalog operation records | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED — USED BY continuation for Gated by: records remain subject to privacy/access and authorization rules. | [MAP C-7E] |
| C-7E.13 — Catalog operation records | C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED — USED BY continuation for Gated by: applicable identity/security authorization governs record access. | [MAP C-7E] [MAP C-SACL] |
| C-7A — Universal Filter (§7A) | C-7E — Catalog Front Door + pre-ingest holding (§7E) | DESIGNED — Reciprocates the existing CH02 C-7A Fed by entry for catalog-eligible material. | [MAP C-7E] [V10 §7E / TWO GATES] |
| C-7B.7.1.5 — Automatic hold handling | C-7E — Catalog Front Door + pre-ingest holding (§7E) | ACCEPTED — Reciprocates CH02's automatic-hold-handling gate; no hold-release rule is reassigned to Catalog. | [04/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md §3] [04/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md §4] |
| C-7B.8 — Unfillable-web handling | C-7E — Catalog Front Door + pre-ingest holding (§7E) | DESIGNED — Reciprocates the existing CH02 live-catalog exception in unfillable-web handling. | [V10 §7E / SPEAKER RESOLUTION RULE] [V10 §7E / SOURCE TITLE RULE] |
| C-7B.10.8.5 — TSC blocker condition | C-7E — Catalog Front Door + pre-ingest holding (§7E) | DESIGNED — Reciprocates CH02's TSC blocker condition. | [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY] |
| C-STORE — Accretive store & sealed roots (§6B) | C-7E — Catalog Front Door + pre-ingest holding (§7E) | ACCEPTED — Reciprocates CH03-a's C-STORE Fed by link to Catalog. | [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.1] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13] |
| C-STORE.5.2.10 — Privacy precedence | C-7E — Catalog Front Door + pre-ingest holding (§7E) | ACCEPTED — Reciprocates the existing CH03-a privacy-precedence gate. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| C-DETECT — Speaker detector (fallback; investigated, not deployed) (§11) | C-7E — Catalog Front Door + pre-ingest holding (§7E) | DESIGNED — Reciprocates both the CH03-p detector Fed by and Changes entries for its Catalog handoff. | [MAP C-DETECT] [V10 §7E / SPEAKER RESOLUTION RULE] |
| C-DETECT.2 — Settled speaker rule | C-7E — Catalog Front Door + pre-ingest holding (§7E) | DESIGNED — Reciprocates CH03-p's settled-speaker-rule gate to Catalog. | [V10 §7E / SPEAKER RESOLUTION RULE] |
| C-DETECT.2.4 — Unattended speaker hold | C-7E — Catalog Front Door + pre-ingest holding (§7E) | DESIGNED — Reciprocates CH03-p's unattended-speaker-hold Changes entry. | [V10 §7E / SPEAKER RESOLUTION RULE] |
| C-DETECT.3 — Speaker proposal contents | C-7E — Catalog Front Door + pre-ingest holding (§7E) | DESIGNED — Reciprocates CH03-p's speaker-proposal metadata Changes entry. | [V10 §7E / C. Machine-inferred classifications] [V10 §7E / The raw captured payload] |
| C-7L — Person-Boxes (§7L) | C-7E.11 — Held-content access boundary | DESIGNED — The metadata-only held-content use continues to CH06-c; that chapter must reciprocate this entry. | [V10 §7L / LINKABLE OBJECT TYPES] [MAP C-7E] |
| C-7M — Computed View (§7M) | C-7E.11 — Held-content access boundary | DESIGNED — The metadata-only held-content use continues to CH06-d; that chapter must reciprocate this entry. | [V10 §7M / OBJECT TYPES USED] [MAP C-7E] |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED — USED BY continuation for Gated by: capture exclusions apply before ordinary root storage (P-MAIN step 2). | [V10 §7E / PRIVACY AND EXCLUSION PRECEDENCE] [V10 §7Q / CAPTURE EXCLUSION — TWO-LAYER SYSTEM] |

## Appendix A carry-forward — this piece

| Part | Field | Occurrence | Value |
|---|---|---|---|
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | USED BY row 21 / Takes in there | 1 | NOT DECIDED |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | USED BY row 26 / Takes in there | 1 | NOT DECIDED |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | USED BY row 28 / Takes in there | 1 | NOT DECIDED |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | USED BY row 57 / Takes in there | 1 | NOT DECIDED |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | USED BY row 63 / Takes in there | 1 | NOT DECIDED |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | USED BY row 76 / Takes in there | 1 | NOT DECIDED |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | USED BY row 78 / Takes in there | 1 | NOT DECIDED |
| C-7E.1 — Separate capture and ingestion gates | Fed by | 1 | NOT DECIDED |
| C-7E.1 — Separate capture and ingestion gates | Changes | 1 | NOT DECIDED |
| C-7E.1.1 — Raw-capture gate | Fed by | 1 | NOT DECIDED |
| C-7E.2 — Minimum intake envelope | Changes | 1 | NOT DECIDED |
| C-7E.3 — Capture-error path | Fed by | 1 | NOT DECIDED |
| C-7E.4 — Privacy and exclusion precedence | Fed by | 1 | NOT DECIDED |
| C-7E.5 — Unified pre-ingest record | Changes | 1 | NOT DECIDED |
| C-7E.5.1 — Proposed catalog fields | Changes | 1 | NOT DECIDED |
| C-7E.5.3 — Proposal provenance and uncertainty | Changes | 1 | NOT DECIDED |
| C-7E.5.3 — Proposal provenance and uncertainty | Gated by | 1 | NOT DECIDED |
| C-7E.5.4 — Resolution history | Fails closed by | 1 | NOT DECIDED |
| C-7E.5.4 — Resolution history | Fed by | 1 | NOT DECIDED |
| C-7E.5.4 — Resolution history | Changes | 1 | NOT DECIDED |
| C-7E.5.4 — Resolution history | Gated by | 1 | NOT DECIDED |
| C-7E.5.5 — Lifecycle state | Changes | 1 | NOT DECIDED |
| C-7E.5.5 — Lifecycle state | Gated by | 1 | NOT DECIDED |
| C-7E.5.6 — Resulting root_id | Fails closed by | 1 | NOT DECIDED |
| C-7E.5.6 — Resulting root_id | Changes | 1 | NOT DECIDED |
| C-7E.6.1 — held | Changes | 1 | NOT DECIDED |
| C-7E.6.2 — ready | Fed by | 1 | NOT DECIDED |
| C-7E.6.2 — ready | Changes | 1 | NOT DECIDED |
| C-7E.6.3 — promoting | Changes | 1 | NOT DECIDED |
| C-7E.6.5 — rejected | Fails closed by | 1 | NOT DECIDED |
| C-7E.6.5 — rejected | Fed by | 1 | NOT DECIDED |
| C-7E.6.5 — rejected | Changes | 1 | NOT DECIDED |
| C-7E.6.5 — rejected | Gated by | 1 | NOT DECIDED |
| C-7E.6.6 — excluded | Fed by | 1 | NOT DECIDED |
| C-7E.6.6 — excluded | Changes | 1 | NOT DECIDED |
| C-7E.6.7 — error | Fed by | 1 | NOT DECIDED |
| C-7E.6.7 — error | Changes | 1 | NOT DECIDED |
| C-7E.6.7 — error | Gated by | 1 | NOT DECIDED |
| C-7E.8 — Source-title and thread resolution | Changes | 1 | NOT DECIDED |
| C-7E.8.1 — Source thread identifier | Fails closed by | 1 | NOT DECIDED |
| C-7E.8.1 — Source thread identifier | Fed by | 1 | NOT DECIDED |
| C-7E.8.1 — Source thread identifier | Changes | 1 | NOT DECIDED |
| C-7E.8.1 — Source thread identifier | Gated by | 1 | NOT DECIDED |
| C-7E.8.2 — Untitled capture-session grouping | Fed by | 1 | NOT DECIDED |
| C-7E.8.2 — Untitled capture-session grouping | Changes | 1 | NOT DECIDED |
| C-7E.8.2 — Untitled capture-session grouping | Gated by | 1 | NOT DECIDED |
| C-7E.8.3 — Singleton grouping | Fails closed by | 1 | NOT DECIDED |
| C-7E.8.3 — Singleton grouping | Fed by | 1 | NOT DECIDED |
| C-7E.8.3 — Singleton grouping | Changes | 1 | NOT DECIDED |
| C-7E.8.3 — Singleton grouping | Gated by | 1 | NOT DECIDED |
| C-7E.8.4 — Uncertain grouping | Fed by | 1 | NOT DECIDED |
| C-7E.8.4 — Uncertain grouping | Changes | 1 | NOT DECIDED |
| C-7E.8.4 — Uncertain grouping | Gated by | 1 | NOT DECIDED |
| C-7E.9.1 — Source-carried facts | Fails closed by | 1 | NOT DECIDED |
| C-7E.9.1 — Source-carried facts | Changes | 1 | NOT DECIDED |
| C-7E.9.2 — Deterministic derivations | Changes | 1 | NOT DECIDED |
| C-7E.9.2.1 — Original source value | Fed by | 1 | NOT DECIDED |
| C-7E.9.2.1 — Original source value | Changes | 1 | NOT DECIDED |
| C-7E.9.2.1 — Original source value | Gated by | 1 | NOT DECIDED |
| C-7E.9.2.2 — Separate derived value | Fed by | 1 | NOT DECIDED |
| C-7E.9.2.2 — Separate derived value | Changes | 1 | NOT DECIDED |
| C-7E.9.2.3 — Derivation method | Fails closed by | 1 | NOT DECIDED |
| C-7E.9.2.3 — Derivation method | Fed by | 1 | NOT DECIDED |
| C-7E.9.2.3 — Derivation method | Changes | 1 | NOT DECIDED |
| C-7E.9.2.3 — Derivation method | Gated by | 1 | NOT DECIDED |
| C-7E.9.2.4 — Derivation version | Fails closed by | 1 | NOT DECIDED |
| C-7E.9.2.4 — Derivation version | Fed by | 1 | NOT DECIDED |
| C-7E.9.2.4 — Derivation version | Changes | 1 | NOT DECIDED |
| C-7E.9.2.4 — Derivation version | Gated by | 1 | NOT DECIDED |
| C-7E.9.3 — Machine-inferred proposals | Changes | 1 | NOT DECIDED |
| C-7E.9.3.1 — Inferred proposed value | Fed by | 1 | NOT DECIDED |
| C-7E.9.3.1 — Inferred proposed value | Changes | 1 | NOT DECIDED |
| C-7E.9.3.1 — Inferred proposed value | Gated by | 1 | NOT DECIDED |
| C-7E.9.3.2 — Producer/model/rule | Fails closed by | 1 | NOT DECIDED |
| C-7E.9.3.2 — Producer/model/rule | Fed by | 1 | NOT DECIDED |
| C-7E.9.3.2 — Producer/model/rule | Changes | 1 | NOT DECIDED |
| C-7E.9.3.2 — Producer/model/rule | Gated by | 1 | NOT DECIDED |
| C-7E.9.3.3 — Inference evidence | Fed by | 1 | NOT DECIDED |
| C-7E.9.3.3 — Inference evidence | Changes | 1 | NOT DECIDED |
| C-7E.9.3.4 — Inference confidence | Fed by | 1 | NOT DECIDED |
| C-7E.9.3.4 — Inference confidence | Changes | 1 | NOT DECIDED |
| C-7E.9.3.5 — Inference timestamp | Fails closed by | 1 | NOT DECIDED |
| C-7E.9.3.5 — Inference timestamp | Fed by | 1 | NOT DECIDED |
| C-7E.9.3.5 — Inference timestamp | Changes | 1 | NOT DECIDED |
| C-7E.9.3.5 — Inference timestamp | Gated by | 1 | NOT DECIDED |
| C-7E.9.3.6 — Inference confirmation status | Fed by | 1 | NOT DECIDED |
| C-7E.9.3.6 — Inference confirmation status | Changes | 1 | NOT DECIDED |
| C-7E.9.4 — Semantic-interpretation prohibition | Fed by | 1 | NOT DECIDED |
| C-7E.9.4 — Semantic-interpretation prohibition | Changes | 1 | NOT DECIDED |
| C-7E.10 — Catalog boundary tests | Changes | 1 | NOT DECIDED |
| C-7E.10.1 — Source-description test | Fed by | 1 | NOT DECIDED |
| C-7E.10.1 — Source-description test | Changes | 1 | NOT DECIDED |
| C-7E.10.2 — Interpretive-disagreement test | Fed by | 1 | NOT DECIDED |
| C-7E.10.2 — Interpretive-disagreement test | Changes | 1 | NOT DECIDED |
| C-7E.10.2 — Interpretive-disagreement test | Gated by | 1 | NOT DECIDED |
| C-7E.11 — Held-content access boundary | Changes | 1 | NOT DECIDED |
| C-7E.13 — Catalog operation records | Fails closed by | 1 | NOT DECIDED |
| C-7E.13 — Catalog operation records | Changes | 1 | NOT DECIDED |
| C-7E.13.1 — Capture record | Fails closed by | 1 | NOT DECIDED |
| C-7E.13.1 — Capture record | Fed by | 1 | NOT DECIDED |
| C-7E.13.1 — Capture record | Changes | 1 | NOT DECIDED |
| C-7E.13.2 — Blocker-set record | Fails closed by | 1 | NOT DECIDED |
| C-7E.13.2 — Blocker-set record | Changes | 1 | NOT DECIDED |
| C-7E.13.2 — Blocker-set record | Gated by | 1 | NOT DECIDED |
| C-7E.13.3 — Blocker-clear record | Changes | 1 | NOT DECIDED |
| C-7E.13.4 — Promotion record | Fails closed by | 1 | NOT DECIDED |
| C-7E.13.4 — Promotion record | Fed by | 1 | NOT DECIDED |
| C-7E.13.4 — Promotion record | Changes | 1 | NOT DECIDED |
| C-7E.13.5 — Exclusion record | Fed by | 1 | NOT DECIDED |
| C-7E.13.5 — Exclusion record | Changes | 1 | NOT DECIDED |
| C-7E.13.6 — Capture-error record | Fed by | 1 | NOT DECIDED |
| C-7E.13.6 — Capture-error record | Changes | 1 | NOT DECIDED |
| C-7E.13.7 — Blocker-change reason | Fails closed by | 1 | NOT DECIDED |
| C-7E.13.7 — Blocker-change reason | Fed by | 1 | NOT DECIDED |
| C-7E.13.7 — Blocker-change reason | Changes | 1 | NOT DECIDED |
| C-7E.13.7 — Blocker-change reason | Gated by | 1 | NOT DECIDED |

## Source coverage and explicit deferrals

| Source scope | Card or later piece | Coverage boundary |
|---|---|---|
| V10 §7E, entire parent section before the TSC detailed-design subsection; MAP C-7E, whole card | C-7E and descendants | All gates, envelope elements, capture-error behavior, exclusion precedence, conceptual record contents, seven states, speaker/title rules, enrichment categories and boundary tests. |
| V10 §7E MINIMUM INTAKE ENVELOPE; Bundle 6 mechanics §10 pre-ingest handoff | C-7E.2; existing C-STORE.5.5.8.1–.7 | The seven already-defined envelope atoms retain their existing IDs. Their complete required contents are also stated in the envelope card. |
| V10 §7E SPEAKER RESOLUTION RULE; MAP C-DETECT whole card | C-7E.7; existing C-DETECT.2 and descendants | The source-attribution, uncertain-fallback, live-question, unattended-hold and authorized-confirmation rules reuse CH03-p's cards. |
| V10 §7E SOURCE TITLE RULE; Bundle 6 mechanics §9 and §10 read in full | C-7E.8 and four cases; existing C-STORE.5.4 and C-STORE.5.5 | Four grouping cases, exact placeholder forms, no semantic titles, later alias clarification and future grouping/display separation. Full alias and future-schema records remain in CH03-a; no second copies of those cards. |
| V10 §7E FOUR ENRICHMENT CATEGORIES and BOUNDARY TESTS | C-7E.9 and descendants; C-7E.10 | Every source-fact and derivation kind; original/derived separation, method/version, all six proposal contents and all named inference examples; every forbidden interpretation and both boundary questions. |
| V10 §7L LINKABLE OBJECT TYPES; §7M OBJECT TYPES USED; §7E-TSC §15; MAP C-7E | C-7E.11; full Person-Box and Computed View behavior left for CH06-c/CH06-d; TSC for CH04-b | Only safe source metadata, lifecycle state and blockers may be referenced before promotion; held content cannot be reconstructed or used semantically; no sealed-TSC inspection exception. |
| Decision Defaults §3N whole subsection; V10 §0B ACCESS AND AUTHORIZATION BOUNDARY | C-7E.5.2 blocker list and C-7E.11; full TSC design left for CH04-b | Fingerprint and speaker blockers are independent. The stale Defaults inspection permission is marked as a source conflict; V10's explicit prohibition controls. |
| B11 §7.1–§7.5, §12 and §13 read in full | C-7E.12; existing C-STORE.4.6 and C-STORE.4.12.1 | Prepared payload, five evidence-reference kinds, stable capture identity, mechanical-only B11 checks, proposed caller outcomes and durable acknowledgement. B11's full states, fields, fences, recovery and failure matrix remain in their existing CH03-a cards. |
| Bundle 6 policy §4 A3, whole subsection; mechanics §3, §9, §10 and §13 read in full | C-7E.12; existing C-STORE.5.1, .5.2, .5.4, .5.5; BOP/OOP details left for CH08-d/CH08-e | Separate Origins and time families, common protection spine, unchanged catalog envelope and the single BOP/OOP ingestion route. Full reaction-window/observation mechanics remain for CH08-d; output observations for CH08-e. A3.4 belongs to CH05-a, A3.5 to CH06-c. |
| MAP C-7E operational-record paragraph | C-7E.13 and descendants | Every capture, blocker set/clear with reason, promotion, exclusion and capture-error is recorded under access rules. No invented event-name vocabulary or serialization. |
| Existing CH00 P-MAIN steps 1 and 3; earlier C-7E TOGETHER references | C-7E USED BY and continuation entries | Both path uses and every earlier incoming link are carried without changing earlier chapters. |
| A29 §§3 and 4, complete sections; existing C-7B.7.1.5 | C-7E incoming use for voluntary new material; full hold lifecycle stays in CH02 | Catalog accepts voluntary new evidence through governed channels; it does not substitute for the hold's evidence-bound release interface. |
| B11 and Bundle 6 policy/mechanical closure records, read whole | Status/provenance only | Acceptance supports ACCEPTED stamps within each frozen standalone design scope; none authorizes implementation or overrides V10 build status. |
| Decision Defaults §3C, whole subsection; MAP C-SACL, whole card | C-7E.1.2, .5.2, .6.1, .13.3; C-7E.13 access-owner link | Only actual blocker resolution and applicable access authorization are used here. The known seal/destruction drift remains in the source-conflict register; other store and SACL mechanics stay with their own cards. |

## Review of plain gates

| Card | Reason no other card is named |
|---|---|

## Coverage matrix — carried source inventory

The following inventory retains the preceding pieces’ placements and read status. This piece’s additional placements and deferrals are in the source-scope table above; inherited notes are not fresh whole-read claims.
### File coverage

| Row | Source | Read scope | Placement |
|---|---|---|---|
| F001 | `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped reread for CH04-a; prior whole-read credit retained where previously recorded | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.1; C-STORE.2; C-STORE.3; CY-A Chapter 3-b: C-READ and its v1 record, validator, writer, quarantine, production-boundary and operation-record sub-parts; CY-A/CY-F reading-write interfaces. Chapter 3-c: governing checks for C-READ.10; A2/firmness additions stay ACCEPTED, never BUILT. Chapter 3-d: source-status and no-production-write boundaries; governing operational living-memory rule at C-READ.11.9.4.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.3, C-ENGINE-C.3.1, C-ENGINE-C.3.2, C-ENGINE-C.3.3, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.11.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1, C-ENGINE-AB.1.1, C-ENGINE-AB.1.2, C-ENGINE-AB.1.3, C-ENGINE-AB.2, C-ENGINE-AB.2.1, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.1, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.2.4, C-ENGINE-AB.3, C-ENGINE-AB.4, C-ENGINE-AB.5, C-ENGINE-AB.6, C-ENGINE-AB.8, C-ENGINE-AB.9.; CH03-k: C-INDEX, C-INDEX.1, C-INDEX.1.1, C-INDEX.1.2, C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.1, C-INDEX.4.2, C-INDEX.4.3, C-INDEX.4.4, C-INDEX.4.5, C-INDEX.4.7, C-INDEX.4.8, C-INDEX.5, C-INDEX.6.; CH03-l: C-GOLD, C-GOLD.2, C-GOLD.2.1, C-GOLD.3, C-GOLD.3.1, C-GOLD.6, C-GOLD.6.1, C-GOLD.6.2, C-GOLD.6.3, C-GOLD.7, C-GOLD.7.4.; CH03-o: C-INGEST, C-INGEST.1, C-INGEST.2, C-INGEST.3, C-INGEST.4, C-INGEST.4.1, C-INGEST.4.2, C-INGEST.4.3, C-INGEST.4.4, C-INGEST.4.5, C-INGEST.4.6, C-INGEST.4.7, C-INGEST.4.8, C-INGEST.4.8.1, C-INGEST.4.8.2, C-INGEST.4.8.3, C-INGEST.4.8.4, C-INGEST.4.9, C-INGEST.6.; CH03-p: C-DETECT, C-DETECT.1, C-DETECT.1.1, C-DETECT.1.3, C-DETECT.2, C-DETECT.2.1, C-DETECT.2.2, C-DETECT.2.3, C-DETECT.2.4, C-DETECT.2.5, C-DETECT.3, C-DETECT.3.1, C-DETECT.3.2, C-DETECT.3.3, C-DETECT.3.4, C-DETECT.3.5, C-DETECT.3.6, C-DETECT.4.1.; CH04-a: C-7E, C-7E.1, C-7E.1.1, C-7E.1.2, C-7E.2, C-7E.3, C-7E.4, C-7E.5, C-7E.5.1, C-7E.5.2, C-7E.5.3, C-7E.5.4, C-7E.5.5, C-7E.5.6, C-7E.6, C-7E.6.1, C-7E.6.2, C-7E.6.3, C-7E.6.4, C-7E.6.5, C-7E.6.6, C-7E.6.7, C-7E.7, C-7E.8, C-7E.8.1, C-7E.8.2, C-7E.8.3, C-7E.8.4, C-7E.9, C-7E.9.1, C-7E.9.2, C-7E.9.2.1, C-7E.9.2.2, C-7E.9.2.3, C-7E.9.2.4, C-7E.9.3, C-7E.9.3.1, C-7E.9.3.2, C-7E.9.3.3, C-7E.9.3.4, C-7E.9.3.5, C-7E.9.3.6, C-7E.9.4, C-7E.10, C-7E.10.1, C-7E.10.2, C-7E.11, C-7E.12, C-7E.13, C-7E.13.1, C-7E.13.4, C-7E.13.5, C-7E.13.6. |
| F002 | `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Scoped reread for CH04-a; prior whole-read credit retained where previously recorded | EXCLUDED: interaction/workflow guidance under §1.3 and §2.4. NOT PLACED: remaining behavior belongs to other component groups.; Chapter 3-a: C-STORE.2.3 Chapter 3-b: C-READ.1 confidence semantics and C-READ.2 uncertainty-preserving shape gate; remaining scope retained. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.2, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.8.; CH03-l: C-GOLD, C-GOLD.2, C-GOLD.2.1, C-GOLD.3, C-GOLD.3.1, C-GOLD.4, C-GOLD.4.1, C-GOLD.4.2, C-GOLD.4.3, C-GOLD.4.4, C-GOLD.4.5, C-GOLD.4.6, C-GOLD.5, C-GOLD.6, C-GOLD.6.1, C-GOLD.6.3, C-GOLD.8.3, C-GOLD.8.5.10, C-GOLD.8.5.11.; CH04-a: C-7E, C-7E.1.2, C-7E.5.2, C-7E.6.1, C-7E.6.2, C-7E.7, C-7E.8.4, C-7E.13.3. |
| F003 | `01_AUTHORITATIVE/cursorrules` | Scoped reread for CH03-o; prior whole-read credit retained where previously recorded | EXCLUDED: coding-process rules under §1.3. NOT PLACED: built-code boundaries belong to store, reader and code-boundary groups. Chapter 3-b: C-READ.1.12 per-store/global-key conflict and C-READ.3 shared write boundary; workflow remains excluded. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB.5.; CH03-k: C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.6.; CH03-l: C-GOLD, C-GOLD.9.; CH03-o: C-INGEST, C-INGEST.4, C-INGEST.4.7, C-INGEST.6. |
| F004 | `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; Chapter 3-c focused rule/boundary searches and excerpts, no new whole-read claim | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. |
| F005 | `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped reread for CH04-a; prior whole-read credit retained where previously recorded | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.3.4; CY-A Chapter 3-b: C-READ component name, operation logging and consumer/caller relationships; CY-A/CY-F interfaces. Chapter 3-c: component ownership/names and Group A/D boundary; accepted A2 supplies behavior. Chapter 3-d: names, Group A ownership and per-reading seam versus full CY-G boundary.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.9.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1.1, C-ENGINE-AB.1.3, C-ENGINE-AB.2.1, C-ENGINE-AB.2.4, C-ENGINE-AB.4, C-ENGINE-AB.6, C-ENGINE-AB.6.1.; CH03-k: C-INDEX, C-INDEX.2, C-INDEX.3, C-INDEX.5, C-INDEX.6, C-INDEX.6.1, C-INDEX.6.2, C-INDEX.6.3, C-INDEX.6.4, C-INDEX.6.5, C-INDEX.6.6.; CH03-l: C-GOLD, C-GOLD.4, C-GOLD.4.6, C-GOLD.6, C-GOLD.6.2, C-GOLD.7, C-GOLD.7.1, C-GOLD.7.2, C-GOLD.7.3, C-GOLD.7.4.; CH03-o: C-INGEST, C-INGEST.4.4, C-INGEST.4.7, C-INGEST.5, C-INGEST.5.1, C-INGEST.5.2, C-INGEST.5.3, C-INGEST.5.4, C-INGEST.6.; CH03-p: C-DETECT, C-DETECT.1, C-DETECT.1.1, C-DETECT.1.2, C-DETECT.1.3, C-DETECT.2, C-DETECT.2.1, C-DETECT.2.2, C-DETECT.2.3, C-DETECT.2.4, C-DETECT.2.5, C-DETECT.3, C-DETECT.3.1, C-DETECT.3.3, C-DETECT.3.4, C-DETECT.3.6, C-DETECT.4, C-DETECT.4.1, C-DETECT.4.1.1, C-DETECT.4.1.2, C-DETECT.4.2.; CH04-a: C-7E, C-7E.3, C-7E.4, C-7E.5, C-7E.5.2, C-7E.6.1, C-7E.6.4, C-7E.7, C-7E.8, C-7E.11, C-7E.13, C-7E.13.1, C-7E.13.2, C-7E.13.3, C-7E.13.4, C-7E.13.5, C-7E.13.6, C-7E.13.7. |
| F006 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F007 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F008 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F009 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F010 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F011 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.9 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F012 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F013 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
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
| F036 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md` | Scoped reread for CH03-j; prior whole-read credit retained where previously recorded | C-READ.10 and all A2-cited descendants: §§1–10 identity, card/preparation/event ownership, acceptance/correspondence, commit/recovery, legacy mapping, lifecycle, semantic/safety boundaries, references/rereading and logging. EXCLUDED: source revision history, acts of acceptance, implementation workflow and self-audit claims under §1.3. Other consumer mechanics remain with their owning groups.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards.; CH03-j: C-ENGINE-C, C-ENGINE-C.3.3, C-ENGINE-C.4, C-ENGINE-C.5, C-ENGINE-C.6, C-ENGINE-C.9, C-ENGINE-C.11. |
| F037 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_PACKAGE_COMPLETE_RECORD_v1_0.md` | Read whole for CH03-j | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker. |
| F038 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F039 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F040 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F041 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F042 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F043 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F044 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F045 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F046 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F047 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F048 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for C-STORE.4; receipt narrative excluded under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker. |
| F049 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | Scoped reread for CH04-a; prior whole-read credit retained where previously recorded | Chapter 3-a: C-STORE.4 and all descendants. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: §10 cross-batch reading reread for boundary check; no new B11 behavior written here, Chapter 3-a placement retained.; CH04-a: C-7E, C-7E.1.2, C-7E.5.6, C-7E.6.3, C-7E.6.4, C-7E.12. |
| F050 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F051 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F052 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH03-n | Status/identity checked for NHD-B16EEB; globally unique slot identifiers retained; acceptance narrative EXCLUDED by §1.3; CH03-l: Status/provenance only; no behavior from this receipt or historical blocker.; CH03-m: C-GOLD.1.8.1.5.1.; CH03-n: C-GOLD.1.10, C-GOLD.1.11, C-GOLD.1.11.1, C-GOLD.1.11.2, C-GOLD.1.11.3, C-GOLD.1.11.4, C-GOLD.1.11.5, C-GOLD.1.11.6, C-GOLD.1.11.7, C-GOLD.1.11.8, C-GOLD.1.11.9, C-GOLD.1.11.10, C-GOLD.1.11.11, C-GOLD.1.11.12, C-GOLD.1.11.13, C-GOLD.1.11.14, C-GOLD.1.11.15, C-GOLD.1.11.16, C-GOLD.1.11.17, C-GOLD.1.12, C-GOLD.1.12.1, C-GOLD.1.12.2, C-GOLD.1.12.3, C-GOLD.1.12.4, C-GOLD.1.12.5. |
| F053 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | §§2–6 establish exact accepted standalone scope and source identity. EXCLUDED from behavior: receipt history/roles/process; no mechanism sourced from receipt. |
| F054 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | C-READ.11 and every descendant: complete §§1–11 seam; §13 traces checked against the same rules. §12 external ownership and unspecified details recorded separately. EXCLUDED under §1.3: source status/history/process, self-audit and delivery narrative (§§14–15). |
| F055 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F056 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F057 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md` | Scoped reread for CH03-m; prior whole-read credit retained where previously recorded | C-READ.7.2 and its reciprocal C-READ.7 link: ACCEPTED guard from §1.2 (NHD-B24), matching FR-0608 CARRIED. Remaining B24 behavior NOT PLACED: belongs to later owning templates; no other B24 mechanism added here. Chapter 3-c C-READ.10.3.8.8 and source-conflict register: structural-disposition difference retained against A2; no new retry policy.; CH03-m: C-GOLD.1.8.1.5.2, C-GOLD.1.8.1.5.2.1, C-GOLD.1.8.1.5.2.2, C-GOLD.1.8.1.5.2.3, C-GOLD.1.8.4.3.1, C-GOLD.1.8.4.5, C-GOLD.1.8.4.8. |
| F058 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_PACKAGE_COMPLETE_RECORD_v1_0.md` | Newly read whole for this correction, all 132 lines; pinned Git blob verified | §§2–3, 5 and 12 establish the accepted standalone status and exact v7 identity used for C-READ.7.2; no behavior sourced from this receipt. EXCLUDED: closure history/process under §1.3; no implementation or integration claimed. |
| F059 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F060 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F061 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F062 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F063 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F064 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1 and cited sub-parts; C-7B.7.4.7 and cited sub-parts; C-7B.7.5.3 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F065 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F066 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F067 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F068 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1.6 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F069 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F070 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_CANDIDATE_v1_4.md` | Carried through Chapter 3-a: Not yet read; whole file newly read in Chapter 3-b | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-b: EXCLUDED: status/consolidation and workflow narrative under §1.3. Used for locating later accepted owners only; it supplies no behavior in this piece. |
| F071 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F072 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F073 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F074 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F075 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F076 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F077 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F078 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F079 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F080 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F081 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F082 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F083 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for Bundle 6 mechanics; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker. |
| F084 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped reread for CH04-a; prior whole-read credit retained where previously recorded | Chapter 3-a: C-STORE.5 / operation protections, B17, B20, B21; other component scopes NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: C-7E, C-7E.2, C-7E.8, C-7E.9.1, C-7E.11, C-7E.12. |
| F085 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for Origin policy; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker. |
| F086 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Scoped reread for CH04-a; prior whole-read credit retained where previously recorded | Chapter 3-a: C-STORE.5 / Origin preservation policy; A3.4–A3.5 and other components NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: Navigation excerpt only; no new behavior sourced in this piece.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.7, C-ENGINE-AB.8.; CH04-a: C-7E.12. |
| F087 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F088 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F089 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F090 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F091 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F092 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F093 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F094 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F095 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F096 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F097 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F098 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
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
| F113 | `05_ACTIVE_CANDIDATE/NH_B24_REJECTION_CATEGORY_DECISION_2026-09-23_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F114 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F115 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read whole; NHD-B24 row searched for this correction; Chapter 3-c NHD-A2/NHD-SLF and dependency navigation searches, not a whole-file read; Chapter 3-d NHD-B16/NHD-B16EEB navigation only | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; Chapter 3-a: Navigation only: NHD-B11 and NHD-BU1; no behavior sourced from the index; this correction: NHD-B24 navigation for C-READ.7.2 Chapter 3-c: NHD-A2/NHD-SLF navigation only. Chapter 3-d: navigation only, no behavior sourced from index. |
| F116 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F117 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F118 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F119 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F120 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F121 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F122 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
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
| F137 | `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | C-7A.6 and cited sub-parts; C-7A.13 and cited sub-parts; C-7A.15 and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. Chapter 3-b: C-READ.7 (excluding the ACCEPTED C-READ.7.2 guard) and C-READ.8 (FR-0125–FR-0133); C-READ.1.12.1 (FR-0123); C-READ.9 (FR-0136). |
| F138 | `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH00.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | Naming/path continuity only; no Chapters 0–2 (carried placement) behavior sourced from this chapter. |

### V10 heading coverage

| Row | V10 heading | Placement / remaining scope |
|---|---|---|
| V10-H001 | ### This is `NH_MASTER-20_CORRECTED_v10.md`, a corrected candidate in the Master 20 lineage. It is NOT YET ADOPTED. `NH_MASTER-19_CORRECTED_v7_1.md` (SHA-256: `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf`) remains the authoritative immutable Master until Ness explicitly adopts the corrected Master 20. | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H002 | ### Historical provenance (Master 19 lineage): | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H003 | ## 0. THE PREMISE — NEVER DECIDE FACTS (NEVER CLOSE THE BOOK)  [DESIGNED — the floor under every rule] | Partial placement: C-7A and cited sub-parts; C-7B.9.3. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ interpretation remains revisable. |
| V10-H004 | ## 0A. THE TWO MACHINERIES — DUMB vs SMART (psychologics)  [DESIGNED — top-level frame] | Partial placement: C-7A and cited sub-parts; C-7B.1 and cited sub-parts; C-7B.2.5; C-7B.3.2; C-7B.3.3; C-7B.9 and cited sub-parts; C-7B.11 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ record-carriage boundary; no new interpretation by the writer. |
| V10-H005 | ## 0B. FULL-TRANSPARENCY AND LIVING-RECORD LAW  [DESIGNED — foundational operating rule] | C-7A.16 and cited sub-parts; C-7A.17 and cited sub-parts; C-7B and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. Chapter 3-b: C-READ.6 operation records and health-check operation recording.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim. |
| V10-H006 | ## 1. WHAT N.H IS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H007 | ## 1A. THE INPUT-AGNOSTIC PRINCIPLE — ONE ENGINE, MANY FRONT DOORS  [DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
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
| V10-H018 | ### SCHEMA CONSTRAINTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1 and C-READ.2. |
| V10-H019 | ### PRODUCTION READINGS AUTHORIZATION | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.5 and its protections. |
| V10-H020 | ### PROTECTED FILES AND STORES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.4/C-READ.5 destination separation; edit workflow excluded. |
| V10-H021 | ### DRY-RUN PROTOCOL | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H022 | ### §12 INCOMING — CURRENT STATUS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H023 | ## 6B. THE ACCRETIVE STORE — SCHEMA + STATE  [BUILT & VERIFIED] | Partial placement: C-7A.8 and cited sub-parts; C-7B.2.8.4 and cited sub-parts; C-7B.10.1.3; C-7B.11 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ.1 twelve-field representation; C-READ.2; C-READ.3; C-READ.4.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim. |
| V10-H024 | ## 7. THE BIG DESIGN — UNIVERSAL FILTER + MEANING ENGINE  [engines A + B BUILT; §§7E–7P core-conceptually designed S17; §§7D and 7Q partially conceptually designed] | C-7A and C-7B detailed subsections follow. NOT PLACED: engine implementation behavior belongs to Group A. |
| V10-H025 | ### 7A — THE UNIVERSAL FILTER (operating rules): | C-7A and cited sub-parts; C-7B.3 and cited sub-parts; C-7B.11 and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. Chapter 3-b: C-READ reciprocal Universal Filter use; principles retained from Chapter 2. |
| V10-H026 | ### 7B — THE MEANING ENGINE (mechanism): | C-7B and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. |
| V10-H027 | ### 7C — THE FORCED BUILD ORDER (never re-fought): | EXCLUDED: forced build order under §1.3. NOT PLACED: engine implementations belong to Group A. |
| V10-H028 | ## 7D. THE LIVING STATE WEB — PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ grounded reading consumer relationship. |
| V10-H029 | ## 7E. CATALOG FRONT DOOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H030 | ### §7E-TSC DETAILED DESIGN  [ACCEPTED DESIGN WITH LATER CORRECTIONS — NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H031 | ## 7F. CONTEXT RETRIEVAL  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1.9 retrieval audit and genuine no-context audit; retrieval machinery remains with C-7F. |
| V10-H032 | ## 7G. MEANING ENGINE INTERIOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ acceptance/shape distinction and caller relationship; C-READ.3 new-root write handoff also cites the nested §7G-A subsection.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H033 | ### §7G CREATION-AWARE MODE  [SETTLED CONCEPT — NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H034 | ## 7H. REREAD LIFECYCLE  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ reread output relationship; detailed orchestration remains with C-7H. |
| V10-H035 | ## 7I. VIEW LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ history/current-view use; view machinery remains with C-7I. |
| V10-H036 | ## 7J. CONTRADICTION AND CLASH HANDLING  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ clash-consumer relationship; clash machinery remains with C-7J. |
| V10-H037 | ## 7K. STORY LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7A.8.3; C-7B.3.1; C-7B.3.3 and cited sub-parts; C-7B.3.4. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ.1.5/1.6 speaker/perspective and embedded-v1-telling boundaries; future telling identity remains for its accepted package.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H038 | ## 7L. PERSON-BOXES  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.4. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ Person-Box consumer relationship. |
| V10-H039 | ## 7M. COMPUTED VIEW  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ current-use consumer relationship. |
| V10-H040 | ## 7N. ACTION SURFACING  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H041 | ## 7O. ACTION-RESULT RETURN PATH  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H042 | ## 7P. PERMISSION AND AUTHORITY BOUNDARIES  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H043 | ## 7Q. PRIVACY, DELETION, AND SENSITIVE-DATA HANDLING  [PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
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
| V10-H066 | ## 9A. IMAGE INGEST — FIRST WORKED FRONT-DOOR EXAMPLE  [DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H067 | ## 10. ORIGINALITY (honest calibration) | Partial placement: C-7B.9.3. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H068 | ## 11. WHAT'S OPEN / NEXT (priority order) | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ foundation status and quarantine/production boundary; restored details use the decision record plus named archive, not the compressed V10 line. |
| V10-H069 | ## 11-SETTLED. (condensed) | EXCLUDED: condensed decision/session narrative under §1.3; repeated runtime rules are represented by their detailed owning sections. |
| V10-H070 | ## 12. SESSION 6 — THE DATA-RESCUE OPERATION  [recovery done; ingest FROZEN] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H071 | ## 13. THE LIVE LOOP  [DESIGNED — not built] | Partial placement: C-7B.9; C-7B.10.1 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H072 | ## 14. THE CHAT FRONT DOOR  [PARTIALLY SETTLED, PARTIALLY OPEN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H073 | ## 15. SESSION 10 — BOOT HYGIENE + SIGN-IN + .CURSORRULES  [housekeeping done] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H074 | ## 16. THE MODEL LAYER — THE BORROWED MOUTH + THE SEARCH MODEL  [DESIGNED + partly on disk] | Partial placement: C-7B.6. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
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

### Detailed source landing map

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

The source files below match their Git blobs at `6a7160ba688ba4e433a31899162815df7e2bab17`. The source map gives the complete scoped passages reopened for this piece. The three B11/Bundle 6 closure records were read whole and establish status only. The full TSC subsection and other chapters' source sections are explicitly assigned to their owners; no new whole-read credit is claimed for V10, Defaults, the Map, A29 or either Bundle 6 design file. Contract §§5–11 were reopened before writing; §11.3 is reopened after writing for the checks below. The lessons sheet and run instructions were read in full.

| Source file | SHA-256 |
|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | `baca06e562027a080dab4384943bfb87947c6f598b36776f1016fa8472384a87` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | `cf95a4f8622487a4a254435fd05471572cf0a9ef1886c6bee3352ed7d45621f1` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | `b37f965a343dbf86130f96591d58de9288ad0a746a68e8ae8fdd7b66208a63da` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | `4b37668ea3a95463e49bc27ada107be78cd807e3cbf8455a06b912901b4346f6` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | `bc1095955525fcea56cb4d16057c93bfb15eec42a83a1b644baf0e87a473f64e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | `c5e379f508f3d2c498dfcecfe567db20db4362872de4feff4c7da57d4ff7de79` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md` | `31d5a12455d1532effe7df2216223942da1a555f38910929ff4b6761d0015d65` |

Instruction fingerprints:
- `NH_MASTER-21_SYSTEM_BEHAVIOR_BUILD_CONTRACT_FOR_CHATGPT_v1_0.md` — SHA-256 `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1`.
- `NH_MASTER-21_WRITER_LESSONS_FROM_AUDITS_v0_1.md` — SHA-256 `635be95b861c181efb3b7bc1b2a8405ab706f864068a0b88f31fb91971adf3e6`.
- `NH_MASTER-21_WRITER_RUN_INSTRUCTIONS_v0_2.md` — SHA-256 `93431167c0fb03fe1216ebbc12655ac640d71bcb7a59659cd123f51e72a54611`.

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

### READ-folder files not yet read whole

The pending list contains 93 files after the whole-read updates recorded for this piece. Scoped rereads do not remove a pending entry; the ledger retains its Stage-2-only exception.

- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md`
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
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md`
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
- `05_ACTIVE_CANDIDATE/NH_B24_REJECTION_CATEGORY_DECISION_2026-09-23_v0_1_CANDIDATE.md`
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
§1.3 no history/actions/roles/workflow in this chapter: PASS — all 56 behavior cards reviewed; delivery and source-status records remain outside behavior boxes.
§1.4 every gap written as NOT DECIDED: PASS — 116 empty fields/cells and exactly matching register entries.
§1.5 conflicts marked, none resolved: PASS — 1 new conflicts; earlier conflict records unchanged.
§3 exactly one stamp per line: PASS — 56 headers, 479 populated fields and 228 USED BY rows checked; empty boxes use only NOT DECIDED.
§4 every behavior line cited in the exact format: PASS — 106 distinct citations resolve in pinned sections; all populated fields and USED BY rows cited; support reviewed manually.
§5.4 one name per thing: PASS — 56 non-colliding IDs, official names and established sub-part names checked.
§6 all template fields present, in order, for every part: PASS — 56 templates and 588 field lines checked.
§6.3 reciprocity within this chapter: PASS — 114 internal links reciprocated; 38 outward links and 12 documented incoming uses covered by 50 rows naming both ends; 2 further outgoing lines are answered directly by the named cards' own USED BY rows.
§6.4 every decided detail written in, no citation used in place of content: PASS — All seven envelope members, eleven conceptual pre-ingest contents, seven lifecycle states with stated transitions, four title cases, all source-fact and deterministic-derivation kinds, original/derived/method/version separation, six inference-proposal contents, six inference examples, every forbidden semantic category, both boundary tests and six event categories with blocker reasons are present. The source-fact and derivation lists enumerate allowed kinds, not an invented required schema. B11/B20/B21 atom cards are reused; no new serialization, timing, readiness transaction, speaker threshold, singleton format or runtime schema is invented. Full TSC, BOP/OOP and downstream semantic mechanics remain assigned to named later pieces.
§6.5 sub-parts recursed to the bottom: PASS — 56 cards; source-map scope and reuse of established atomic cards manually reviewed.
§9 coverage matrix rows added for every file used: PASS — 10 pinned source identities and corresponding coverage entries checked; current placement/deferral table included.
§10.11 no recommendation, no sentence addressed to Ness: PASS — all behavior boxes reviewed; source-defined approval conditions are descriptions of the system boundary.
Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`. The lessons sheet and run instructions were read in full; contract §§5–11 were reopened before writing and §11.3 afterward. Other source reads are the scoped sections in the source map, without a new whole-file claim.

Computed self-check output:

| Check | Count |
|---|---|
| cards | 56 |
| field_lines | 588 |
| populated_fields | 479 |
| not_decided_fields_and_cells | 116 |
| used_by_rows | 228 |
| relationships | 154 |
| internal_relationships | 114 |
| external_relationships | 40 |
| continuation_rows | 50 |
| plain_gates | 0 |
| step_cards | 31 |
| source_names_checked | 72 |
| unique_citations | 106 |
| source_identities | 10 |
| earlier_identities | 19 |
| pending_source_paths | 93 |
| built_field_lines | 0 |
| misfiled_scan_fields | 588 |
| empty_restriction_failure_gate_boxes_reviewed | 33 |
| formula_hits | 0 |
| wording_hits | 0 |
| errors | 0 |
| path_use_rows | 2 |
| subpart_references_checked | 55 |

Manual review accompanying the mechanical scan:

- All V10/Map/Defaults behavior remains DESIGNED; only accepted B11/Bundle 6 contracts receive ACCEPTED. No BUILT line appears on Catalog or its links. Proposed root_schema_v2, origin_relationship_record, ingest_idempotency_key and B11 caller outcomes remain marked proposed. The seven old envelope atoms and the detector speaker rule are reused by identity, with the full relevant content stated in the new parent cards.
- Reviewed every ALONE and TOGETHER field and every USED BY cell, including all empty-failure candidates. Filled the durable-acknowledgement protection on promoted, safe-exclusion outcome on exclusion records and preserved-material outcome on capture-error records. Remaining empty failure boxes belong to record members, already-selected grouping cases, intentional rejection or logging operations with no separate failure mechanism specified; their explicit requirements are in Must never/Gated by. Every process step names its governing card.
- All seven envelope members, eleven conceptual pre-ingest contents, seven lifecycle states with stated transitions, four title cases, all source-fact and deterministic-derivation kinds, original/derived/method/version separation, six inference-proposal contents, six inference examples, every forbidden semantic category, both boundary tests and six event categories with blocker reasons are present. The source-fact and derivation lists enumerate allowed kinds, not an invented required schema. B11/B20/B21 atom cards are reused; no new serialization, timing, readiness transaction, speaker threshold, singleton format or runtime schema is invented. Full TSC, BOP/OOP and downstream semantic mechanics remain assigned to named later pieces.
- Direct prohibitions preserve no guessing, no raw rewrite, no destruction, no sealed-batch reopening, no direct role write and no semantic work in Catalog. Source-required Ness interactions remain behavioral facts. No Master-21 workflow occurs in behavior boxes and no formula restrictions are used.
- P-MAIN steps 1 and 3 each have a separate USED BY row. Earlier incoming Catalog links and the detector relationships are reciprocated; future metadata-only uses identify their continuation chapters. Receipt whole-read claims are limited to the three complete closure records. No new runtime verification or source-pin change is claimed. Counts are computed from the finished file.

All named source paths were checked at the fixed pin. Runtime/store names are checked against source documentation; this is not a live N.H filesystem check. C-7E records both P-MAIN step 1 and step 3 uses. Side-path assembly remains for CH11. The wording scan covers the whole file. The count table is compared with a final recount after this block is appended.
