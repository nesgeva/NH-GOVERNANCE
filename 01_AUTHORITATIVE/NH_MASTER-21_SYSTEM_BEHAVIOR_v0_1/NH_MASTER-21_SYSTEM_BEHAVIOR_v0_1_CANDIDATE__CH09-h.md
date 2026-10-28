# Chapter 9-h — Group G: C-ENROLL

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-h.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`  

This piece covers initial Ness voice-profile enrollment: its explicit beginning, six prerequisites, biometric proof, capture, two lifecycles, ordinary root/read path, segment eligibility, readiness, provisional linkage and profile handoff, coordination records, auditing and recovery. Existing pairing, biometric, observation, Person-Box, privacy, reading and SIA owners retain their authority. Full modes and the remaining voice-pipeline mechanics belong to CH09-i; the durable-operation kernel to CH10-b; side paths to CH11; final registers to CH12. No unspecified sample count, duration, threshold, algorithm, hardware, transport or final serialization is selected.

[SOURCE CONFLICT] Companion embedded security-design §11 prerequisite 3 calls the original QR and temporary pairing secret destroyed. V10 §25.11 requires that they were rendered permanently inert at pairing. The V10 condition is retained, including the earlier sealing boundary; destruction is not adopted. [COMP §11. Initial Ness Voice-Profile Enrollment Bootstrap] [V10 §25.11 / Prerequisites (All Six Must Be True)]

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`.

<!-- BEGIN BEHAVIOR -->

### C-ENROLL — Initial Ness voice-profile enrollment (§25.11)
Stamp: DESIGNED    Source: [V10 §25.11] [MAP C-ENROLL]

ALONE
- What it is: DESIGNED — The authorized bootstrap that collects provisional voice-profile material without claiming the captured voice has been identified as Ness. [V10 §25.11]
- Takes in: DESIGNED — An explicit begin action on the permanently trusted owner phone, all six prerequisites, a purpose-bound biometric token and physical enrollment observations. [V10 §25.11]
- Does: DESIGNED — Rechecks prerequisites before consuming the token, opens the session, collects declared enrollment material, ends capture before normal root ingestion, checks segment eligibility, obtains readings, proposes the provisional Person-Box link and hands linked readings to SIA. [V10 §25.11]
- Gives out: DESIGNED — Preserved observation roots, eligible provisional reading material, a provisional association and a provisional profile under their respective owners, plus the nine enrollment audit events. [V10 §25.11]
- Must never: DESIGNED — Equate authorized provenance with confirmed voice identity, let a rejected segment train the provisional profile, automatically grant recognized_ness or unlock top-security. [V10 §25.11]
- Fails closed by: DESIGNED — Changed prerequisites revoke the unconsumed token and prevent opening; any failed eligibility check excludes that segment from profile use while preserving its roots. [V10 §25.11]

TOGETHER
- Fed by: DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): current finalized trust/recovery/QR/setup facts; C-BAI — Biometric Authorization Interface (§25.6): purpose-bound token and durable consumption truth. [V10 §25.11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]
- Fed by: ACCEPTED — C-PAIR.5 — Enrollment owner-fact boundary: pairing authority remains at its owner; C-PAIR.5.1 — Live prerequisite-owner reads: current owner references, versions and satisfaction; C-PAIR.5.2 — Pairing-owned enrollment safety events: current changes stop affected capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Fed by: ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: owner-returned proposal and committed-link outcomes; C-SIA.20.1 — Eligible enrollment reading input: actual readiness rules and eligible reading constraints; C-SIA.20.2 — Provisional profile commit identity: actual SIA commit or refusal; C-SIA.20.7 — Profile-commit enrollment notification: commitment before the creation event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: DESIGNED — C-SIA.12 — Conservative profile calibration: provisional ceiling and conservative weighting; C-SIA.13 — Protected raw voice and readings: no raw-voice disclosure exception; C-SIA.20.6 — Enrollment association strengthening: later evidence and ordinary rules govern strengthening. [V10 §25.11 / SIA Integration] [V10 §25.11 / What Enrollment Does Not Establish] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]
- Gated by: ACCEPTED — C-SIA.20.8 — Enrollment authority limits: enrollment grants no additional identity, access, mode or action authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture and output privacy; C-SACL — Speaker Access-Control Layer (§25.4): spoofing disqualification and final access; C-9 — Access/authentication model + voice I/O + phone modes (§9): current mode fence and B29 physical capture truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Changes: ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: submits only the proposal and exact frozen references; C-SIA.20 — Provisional enrollment profile handoff: supplies the linked eligible reading set and build identity [proposed] after current committed linkage. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-7L.11 — Provisional enrollment Person-Box link | The exact immutable input references and stable proposal identity. | Owns the proposal outcome and committed provisional link; returns its actual state for recovery. | The coordinator only proposes and cannot approve or merge the association. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |
| 2 · ACCEPTED | C-7L.11.6 — Enrollment proposed input-bundle reference | The immutable enrollment_profile_input_bundle [proposed] reference. | Uses that frozen coordination input rather than an already-created profile. | Linkage can precede SIA profile creation without a second profile store. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] |
| 3 · ACCEPTED | C-7L.11.8 — Enrollment link operation reference | The enrollment operation reference. | Attaches the exact parent identity to the link proposal. | The collection operation remains traceable. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 4 · ACCEPTED | C-7L.11.9 — Enrollment link session reference | The enrollment session reference. | Attaches the actual collection-session identity. | Session provenance stays distinct from parent-operation identity. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 5 · ACCEPTED | C-7L.11.10 — Enrollment link eligible-reading references | The exact eligible accepted reading references. | Preserves the frozen set proposed for linkage. | The later profile handoff uses the same linked material. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 6 · ACCEPTED | C-7L.11.11 — Enrollment link eligibility-decision references | The exact eligibility-decision references. | Keeps every proposed reading traceable to segment eligibility. | A proposal acknowledgment does not establish eligibility by itself. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 7 · ACCEPTED | C-7L.11.12 — Enrollment link prerequisite-evidence references | Prerequisite and authorization evidence references. | Retains their provenance while truth remains with the actual owners. | The link cannot turn coordination into authority or confirmed voice identity. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 8 · ACCEPTED | C-BOP.15.4 — Single enrollment biometric success observation | Actual committed opening truth and its durable BAI proof reference. | Receives BAI's single deterministic biometric-success command at the coordinated time. | No coordinator-fabricated or duplicate success observation is created. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 9 · ACCEPTED | C-BOP.15.5 — Frozen enrollment capture set and normal entry | Committed close/interruption and the actual frozen observation set. | Carries observations through normal Catalog, B11 append and reading entry. | Enrollment owns freeze/eligibility while BOP observations and privacy authority remain separate. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |
| 10 · DESIGNED | C-BAI — Biometric Authorization Interface (§25.6) | The explicit enrollment authorization request. | Issues and consumes only the exact voice_enrollment_ness purpose under its own pending and audit rules. | Enrollment gets bounded proof without biometric identity attribution. | [V10 §25.6] |
| 11 · DESIGNED | C-BAI.3.9.3 — Ness enrollment purpose | The explicit-action-bound enrollment request. | Uses the exact Ness-enrollment purpose. | An enrollment token cannot acquire another purpose's authority. | [V10 §25.11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] |
| 12 · ACCEPTED | C-BAI.19 — Enrollment authorization producer | The enrollment operation, prospective session and checked prerequisites. | Produces purpose-bound authorization and actual durable proof for the separately owned opening. | BAI retains token truth and does not become the enrollment-session owner. | [V10 §25.11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6] |
| 13 · ACCEPTED | C-BAI.19.4 — Enrollment proof binding without new authority | The operation and session needing proof linkage. | Binds actual consumption directly or through the integrity-protected companion reference. | Enrollment can verify the binding without gaining BAI authority. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6] |
| 14 · ACCEPTED | C-BAI.19.5 — Enrollment consumed-proof crash boundary | Actual consumption, opening and capture facts. | Enforces the spent-without-opening and zero/unknown-capture recovery boundary. | The coordinator stops honestly rather than completing missing authority or reopening capture. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6] |
| 15 · ACCEPTED | C-BAI.19.6 — BAI-owned enrollment success observation | Actual committed opening referencing durable consumed proof. | Sends the sole BAI-sourced biometric:result:success fact to BOP. | Enrollment controls timing only and cannot fabricate the physical observation. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 16 · ACCEPTED | C-SIA.20 — Provisional enrollment profile handoff | The linked eligible reading set, immutable input bundle and build identity [proposed]. | Owns provisional-profile creation only after current committed Person-Box linkage. | Its actual commit permits the later enrollment creation event; SACL still owns access. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] |
| 17 · ACCEPTED | C-SIA.20.1 — Eligible enrollment reading input | Frozen eligible-reading references and enrollment_profile_readiness [proposed]. | Applies its readiness rules to counted_reading_refs and per-reading eligibility evidence. | No duplicate count, invented threshold or premature profile is permitted. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] |
| 18 · ACCEPTED | C-SIA.20.2 — Provisional profile commit identity | The stable build identity [proposed] and current linked input set. | Returns an actual idempotent profile commit or refusal. | Enrollment records creation only after SIA commitment. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 19 · ACCEPTED | C-SIA.20.7 — Profile-commit enrollment notification | The enrollment handoff awaiting a profile outcome. | Permits the enrollment creation event after SIA's actual commit. | The parent completes only with both owner commits and both required enrollment events. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18] |
| 20 · ACCEPTED | C-ENROLL.1 — Enrollment coordination boundary | The initial enrollment operation. | Coordinates its owner handoffs and reference history. | No specialist authority transfers to coordination. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §3] |

SUB-PARTS: C-ENROLL.1 — Enrollment coordination boundary; C-ENROLL.2 — Six-owner prerequisite check; C-ENROLL.3 — Explicit enrollment beginning; C-ENROLL.4 — Ordered authorization and opening; C-ENROLL.5 — Capture-control and observation boundary; C-ENROLL.6 — Enrollment process lifecycle; C-ENROLL.7 — Mid-session protective stop; C-ENROLL.8 — Closed-session root and reading handoff; C-ENROLL.9 — Initial-corpus eligibility gate; C-ENROLL.10 — Profile readiness record; C-ENROLL.11 — Provisional link and profile coordination; C-ENROLL.12 — Enrollment authority and privacy limits; C-ENROLL.13 — Enrollment coordination records and identities; C-ENROLL.14 — Enrollment audit-event ownership; C-ENROLL.15 — Enrollment crash recovery; C-ENROLL.16 — Enrollment retry and failure boundary

### C-ENROLL.1 — Enrollment coordination boundary
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The Enrollment Coordinator (EC) [proposed], owner only of enrollment coordination records and enrollment-owned events. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §3]
- Takes in: ACCEPTED — References to facts returned by the actual phone, biometric, identity, privacy, Person-Box, observation, root, reading and profile owners. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §3]
- Does: ACCEPTED — Coordinates their ordered handoffs without acquiring their authority. Trusted-phone binding supplies outer bootstrap authority; the purpose-bound token supplies inner approval. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §3]
- Gives out: ACCEPTED — Reference-bearing coordination history and the enrollment events. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §3]
- Must never: ACCEPTED — Become a BAI session manager, access controller, voice-identity authority, privacy authority, root store, reading queue or profile store, or identify Ness by name from device biometric success. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Blocks and records a contradiction with an actual owner; the owner's record governs. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: DESIGNED — C-ENROLL — Initial Ness voice-profile enrollment (§25.11): the bounded bootstrap operation to coordinate. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §3]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.13 — Enrollment coordination records and identities | The coordinator's limited record ownership. | Keeps append-only reference records beneath one parent. | No specialist authority or evidence weight is duplicated. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |
| 2 · ACCEPTED | C-ENROLL.15.21 — Recovery from coordinator-owner contradiction | The coordinator's non-authoritative standing. | Uses the actual owner's record when records conflict. | The contradiction is recorded and continuation blocked. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §3] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |

SUB-PARTS: NONE

### C-ENROLL.2 — Six-owner prerequisite check
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — The conjunction of exactly six live prerequisites, checked initially and rechecked immediately before token consumption. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Takes in: ACCEPTED — I2 request `{ operation_ref }` and each real owner's `{ owner_ref, owner_version, satisfied }` response. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Reads and references all six facts, including their current versions or event identities, and records a versioned snapshot. Retry and recovery read owners again. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — All six true yields `enrollment_prerequisites_verified`; an unsatisfied prerequisite yields `enrollment_prerequisite_failed`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Treat the recorded snapshot as current authority or re-decide its owners' facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Any missing, stale, contradictory or unverifiable prerequisite prevents the BAI call; changes before consumption prevent opening and cause revocation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-PAIR.5.1 — Live prerequisite-owner reads: supplies the four pairing-owned current facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Fed by: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): supplies spoofing assessment; C-SACL — Speaker Access-Control Layer (§25.4): supplies its Gate 0 effect. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Fed by: ACCEPTED — C-7L.4 — Ness's confirmed Person-Box: supplies confirmed-box truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.2.7 — Versioned prerequisite snapshot | Six current owner responses. | Records their references, versions and satisfaction. | A versioned snapshot exists without becoming authority. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] |
| 2 · ACCEPTED | C-ENROLL.4 — Ordered authorization and opening | Initial and final owner checks. | Requires all six before requesting and before consuming authorization. | Changed prerequisites revoke rather than open. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] |
| 3 · ACCEPTED | C-ENROLL.4.1 — Enrollment BAI request fields | The all-six initial result. | Calls BAI only after the conjunction passes. | Failed prerequisites prevent the request. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 4 · ACCEPTED | C-ENROLL.4.2 — Final owner recheck and revocation | Fresh owner responses after the prompt. | Checks for a changed prerequisite immediately before consumption. | A change revokes the token with no opening. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] |
| 5 · ACCEPTED | C-ENROLL.4.5.7 — Stale-snapshot barrier | Fresh owner responses. | Uses the reread rather than the old snapshot. | Stale recorded satisfaction cannot authorize consumption. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B] |
| 6 · ACCEPTED | C-ENROLL.6.2 — Initial prerequisites verified state | An all-six initial check. | Enters prerequisites_verified_initial [proposed]. | The BAI request may follow, with a later recheck still required. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] |
| 7 · ACCEPTED | C-ENROLL.14.1 — Prerequisites verified enrollment event | An actual all-six result. | Writes enrollment_prerequisites_verified. | The recorded check does not replace later revalidation. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] |
| 8 · ACCEPTED | C-ENROLL.14.6 — Prerequisite failed enrollment event | A failed initial prerequisite. | Writes enrollment_prerequisite_failed. | The BAI request does not proceed. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] |
| 9 · ACCEPTED | C-ENROLL.16.2 — Fresh enrollment-session requirements | Fresh prerequisite checks. | Requires all six owners to hold again. | An old snapshot cannot satisfy a new attempt. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22] |

SUB-PARTS: C-ENROLL.2.1 — Final owner-phone prerequisite; C-ENROLL.2.2 — Completed first-code prerequisite; C-ENROLL.2.3 — Inert initial-material prerequisite; C-ENROLL.2.4 — Finalized setup prerequisite; C-ENROLL.2.5 — Clean current spoofing prerequisite; C-ENROLL.2.6 — Confirmed Ness-box prerequisite; C-ENROLL.2.7 — Versioned prerequisite snapshot; C-ENROLL.2.8 — Prerequisite-check operation reference

### C-ENROLL.2.1 — Final owner-phone prerequisite
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — Prerequisite 1: final permanent trusted-owner phone status, BAI state 4. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Takes in: ACCEPTED — The pairing/BAI owner's hardware-backed keystore binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Does: ACCEPTED — Checks final permanent trust on that binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gives out: ACCEPTED — The first prerequisite's owner-referenced satisfaction. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Must never: ACCEPTED — Substitute provisional trust or an OS device-id field. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Unestablished final trust leaves the six-way conjunction false. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]

TOGETHER
- Fed by: DESIGNED — C-PAIR.1.4.1 — Permanent trusted-owner status: the real final trust fact. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.2.2 — Completed first-code prerequisite
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — Prerequisite 2: the complete first normal recovery-code handover. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Takes in: ACCEPTED — Saved, verified, locally tested and activated status from pairing/recovery. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Does: ACCEPTED — Requires all four completed steps. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gives out: ACCEPTED — The second prerequisite's owner-referenced satisfaction. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Must never: ACCEPTED — Treat saving alone as completion. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Any incomplete step prevents enrollment authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]

TOGETHER
- Fed by: DESIGNED — C-PAIR.2.3 — Normal-code activation handover: the completed handover. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.2.3 — Inert initial-material prerequisite
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — Prerequisite 3: the original QR and temporary pairing secret became permanently inert at pairing. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Takes in: ACCEPTED — Both pairing-owned inertness facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Does: ACCEPTED — Requires both permanent closures. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gives out: ACCEPTED — The third prerequisite's satisfaction. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Must never: ACCEPTED — Replace inertness with destruction or accept an active QR or secret. [V10 §25.11 / Prerequisites (All Six Must Be True)] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Either missing or contradictory closure prevents the conjunction. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: DESIGNED — C-PAIR.1.2.1 — Signed QR inertness: QR closure; C-PAIR.1.2.2 — Temporary pairing-secret inertness: secret closure. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.2.4 — Finalized setup prerequisite
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — Prerequisite 4: original owner setup finalized and its QR path permanently closed. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Takes in: ACCEPTED — The pairing-owned `bai_initial_setup_finalized` fact. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Does: ACCEPTED — Checks the final setup and permanent path closure. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gives out: ACCEPTED — The fourth prerequisite's owner-referenced satisfaction. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Must never: ACCEPTED — Infer finalized setup from an earlier provisional pairing event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Invalid setup or unverified final closure prevents enrollment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: DESIGNED — C-PAIR.1.4.2 — Permanent initial QR-path closure: closed path; C-PAIR.1.6 — Initial-setup finalization audit event: finalized setup reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.2.5 — Clean current spoofing prerequisite
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — Prerequisite 5: no active medium-or-higher acoustic spoofing suspicion in the current session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Takes in: ACCEPTED — SIA's assessment and SACL's Gate 0 disqualifier effect. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Does: ACCEPTED — Reads their current result without reassessing spoofing. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gives out: ACCEPTED — The fifth prerequisite's satisfaction only while the stated suspicion is absent. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Must never: ACCEPTED — Lower the medium-or-higher boundary or substitute coordinator judgment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — A disqualifying or unverifiable result prevents authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): current assessment; C-SACL — Speaker Access-Control Layer (§25.4): current Gate 0 effect. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.2.6 — Confirmed Ness-box prerequisite
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — Prerequisite 6: Ness's Person-Box is confirmed. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Takes in: ACCEPTED — The actual Person-Box owner's confirmed identity reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Does: ACCEPTED — Reads that confirmation as the bootstrap destination prerequisite. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gives out: ACCEPTED — The sixth prerequisite's owner-referenced satisfaction. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Must never: ACCEPTED — Let enrollment create or assert Person-Box confirmation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §3] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Missing or contradictory confirmation prevents enrollment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-7L.4 — Ness's confirmed Person-Box: the confirmed identity fact. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.2.7 — Versioned prerequisite snapshot
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — `enrollment_prerequisite_snapshot` [proposed], a versioned reference record of one six-owner check. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Takes in: ACCEPTED — The six current owner responses and the check time. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Does: ACCEPTED — Records `snapshot_id`, `snapshot_version`, one entry per prerequisite with its owner reference and current owner version/event identity, `taken_at` and boolean `all_six_satisfied`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gives out: ACCEPTED — An inspectable snapshot identity and version. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Must never: ACCEPTED — Become authority for any recorded fact or replace fresh owner reads. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: ACCEPTED — Unverified prerequisites do not produce an all-six success or authorize the BAI call. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.2 — Six-owner prerequisite check: actual current responses. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.2.7.1 — Snapshot identity | The particular snapshot. | Carries its snapshot_id. | The check is referable in the proof chain. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] |
| 2 · ACCEPTED | C-ENROLL.2.7.2 — Snapshot version | The recorded check version. | Preserves snapshot_version. | The exact snapshot version remains identifiable. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] |
| 3 · ACCEPTED | C-ENROLL.2.7.3 — Per-prerequisite owner entry | The six prerequisite slots. | Records each owner's reference, version and result. | Each checked fact remains traceable to its owner. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] |
| 4 · ACCEPTED | C-ENROLL.2.7.4 — Snapshot check time | The check time. | Records taken_at. | The snapshot is temporally attributable. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] |
| 5 · ACCEPTED | C-ENROLL.2.7.5 — All-six satisfaction boolean | All six satisfaction results. | Records the boolean all_six_satisfied. | Only a full conjunction permits verification success. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] |
| 6 · ACCEPTED | C-ENROLL.4.3.7 — Bound prerequisite-snapshot reference | Snapshot identity and owner-version evidence. | References the checks in the durable binding. | Historical evidence remains distinct from live owner authority. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] |
| 7 · ACCEPTED | C-ENROLL.10.5.4 — Bundle prerequisite and authorization evidence | Owner-check references and versions. | Includes prerequisite evidence in the frozen bundle. | The bundle does not acquire prerequisite authority. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] |
| 8 · ACCEPTED | C-ENROLL.15.2 — Recovery after initial checks before BAI | The old check snapshot. | Fails the interrupted pre-BAI operation. | Another attempt rereads actual owners. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |

SUB-PARTS: C-ENROLL.2.7.1 — Snapshot identity; C-ENROLL.2.7.2 — Snapshot version; C-ENROLL.2.7.3 — Per-prerequisite owner entry; C-ENROLL.2.7.4 — Snapshot check time; C-ENROLL.2.7.5 — All-six satisfaction boolean

### C-ENROLL.2.7.1 — Snapshot identity
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — `snapshot_id`, the snapshot identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Takes in: ACCEPTED — The particular six-owner check being recorded. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Does: ACCEPTED — Identifies its reference snapshot. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gives out: ACCEPTED — A snapshot reference usable in the authorization chain. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Must never: ACCEPTED — Treat identity as proof that the referenced facts are still current. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.2.7 — Versioned prerequisite snapshot: the identified record. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.2.7.2 — Snapshot version
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — `snapshot_version`, the version of the prerequisite snapshot. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Takes in: ACCEPTED — The recorded check's version identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Does: ACCEPTED — Keeps the particular snapshot version identifiable. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gives out: ACCEPTED — The version paired with `snapshot_id`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Must never: ACCEPTED — Substitute this version for the current owner versions. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.2.7 — Versioned prerequisite snapshot: the versioned record. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.2.7.3 — Per-prerequisite owner entry
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — One snapshot entry for each of the six prerequisites. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Takes in: ACCEPTED — The owner response's `owner_ref`, `owner_version` and `satisfied`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Preserves the owner's reference and current version/event identity alongside the satisfaction result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — A traceable per-prerequisite check without copying its authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Must never: ACCEPTED — Replace an owner reference with a coordinator assertion. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — An unverifiable entry cannot establish the six-way conjunction. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.2.7 — Versioned prerequisite snapshot: one slot per prerequisite. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.2.7.3.1 — Prerequisite owner reference | The returned owner reference. | Preserves owner_ref by reference only. | The fact's actual owner remains identifiable. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 2 · ACCEPTED | C-ENROLL.2.7.3.2 — Prerequisite owner version | The owner's current version/event identity. | Records owner_version. | The check retains current-at-check provenance. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] |
| 3 · ACCEPTED | C-ENROLL.2.7.3.3 — Prerequisite satisfaction result | The owner's satisfaction response. | Carries satisfied into the conjunction. | A failed response prevents all-six success. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |

SUB-PARTS: C-ENROLL.2.7.3.1 — Prerequisite owner reference; C-ENROLL.2.7.3.2 — Prerequisite owner version; C-ENROLL.2.7.3.3 — Prerequisite satisfaction result

### C-ENROLL.2.7.3.1 — Prerequisite owner reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — `owner_ref` in an I2 prerequisite response. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — The actual fact owner's reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Identifies where prerequisite truth is owned. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gives out: ACCEPTED — A reference-only response field. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Carry the underlying private payload into the snapshot. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.2.7.3 — Per-prerequisite owner entry: the returned owner reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.2.7.3.2 — Prerequisite owner version
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — `owner_version`, the owner's current version or event identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — The version/event identity returned by the actual owner. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Does: ACCEPTED — Records which owner fact was checked. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gives out: ACCEPTED — Current-at-check version provenance. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Must never: ACCEPTED — Treat an old recorded version as a fresh owner read. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.2.7.3 — Per-prerequisite owner entry: the owner's version/event field. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.2.7.3.3 — Prerequisite satisfaction result
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — `satisfied`, the individual owner's prerequisite result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — The actual owner's satisfaction response. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Carries whether that prerequisite holds. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — One input to the six-way conjunction. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Be asserted independently by coordination. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — A failing prerequisite yields `enrollment_prerequisite_failed` and no BAI call. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.2.7.3 — Per-prerequisite owner entry: the per-owner result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.2.7.4 — Snapshot check time
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — `taken_at`, the snapshot's check time. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Takes in: ACCEPTED — The time of the recorded six-owner check. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Does: ACCEPTED — Associates that time with the snapshot. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gives out: ACCEPTED — Temporal check provenance. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.2.7 — Versioned prerequisite snapshot: the timed check. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.2.7.5 — All-six satisfaction boolean
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — `all_six_satisfied`, a boolean. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Takes in: ACCEPTED — The six owner-returned satisfaction results. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Is true only when all six prerequisites hold. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — True permits `enrollment_prerequisites_verified`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Treat a partial conjunction as all-six success. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — Without all six, no BAI request proceeds. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.2.7 — Versioned prerequisite snapshot: the complete set of results. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.2.8 — Prerequisite-check operation reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — I2's `operation_ref` request field. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — The current enrollment operation identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Associates the owner reads with that operation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — A reference-only prerequisite request. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Convey authority merely by naming the operation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §3]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.3.2 — Stable enrollment operation identity: the parent identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.3 — Explicit enrollment beginning
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — I1, the dedicated Owner Setup / Voice Enrollment begin flow on the permanently trusted phone. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — `{ explicit_begin_event_ref, trusted_phone_binding_ref }`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Records the explicit choice durably, reserves one stable operation and one prospective session, and acquires the begin-event-keyed claim. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Gives out: ACCEPTED — `{ enrollment_operation_id [proposed], prospective_session_id }` or refusal; successful reservation grants no authority and opens no session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Initiate through another route or treat a double tap as authorization for two sessions. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Fails closed by: ACCEPTED — A request outside the dedicated permanently trusted-phone flow is refused and recorded; recovery of a reservation opens no session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: DESIGNED — C-PAIR.1.4.1 — Permanent trusted-owner status: the trusted phone on which the explicit choice occurs. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: ACCEPTED — C-ENROLL.3.4 — One-begin coordination claim: one active claim per durable begin identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.3.1 — Durable explicit-begin event | The explicit trusted-phone choice. | Records its durable begin event. | The anti-double-tap identity exists. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] |
| 2 · ACCEPTED | C-ENROLL.3.3 — Prospective enrollment session identity | The claimed begin operation. | Reserves one prospective session identity. | No session authority exists until the opening commit. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] |
| 3 · ACCEPTED | C-ENROLL.4 — Ordered authorization and opening | The recorded choice and prospective identities. | Starts the ordered authorization sequence. | Opening remains conditional on live prerequisites and durable proof. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] |

SUB-PARTS: C-ENROLL.3.1 — Durable explicit-begin event; C-ENROLL.3.2 — Stable enrollment operation identity; C-ENROLL.3.3 — Prospective enrollment session identity; C-ENROLL.3.4 — One-begin coordination claim; C-ENROLL.3.5 — Begin request phone-binding reference

### C-ENROLL.3.1 — Durable explicit-begin event
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]

ALONE
- What it is: ACCEPTED — The durable event for Ness's explicit enrollment choice. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Takes in: ACCEPTED — The actual begin action in the dedicated trusted-phone flow. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Does: ACCEPTED — Gives that action its own durable identity, the anti-double-tap key. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Gives out: ACCEPTED — `explicit_begin_event_ref` for I1 and the later authorization chain. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Must never: ACCEPTED — Treat a historical choice as a new explicit begin after a failed or interrupted capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Fails closed by: ACCEPTED — Before a prerequisite snapshot exists, recovery stays idle with no session or BAI call; a later attempt needs a new begin. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.3 — Explicit enrollment beginning: the actual choice to record. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.3.2 — Stable enrollment operation identity | The durable begin identity. | Keys one stable parent to that choice. | Child work remains under one logical enrollment. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] |
| 2 · ACCEPTED | C-ENROLL.3.4 — One-begin coordination claim | The durable explicit-begin identity. | Keys one active coordination claim to it. | Only one prospective session can be reserved. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B] |
| 3 · ACCEPTED | C-ENROLL.6.1 — Requested process state | The recorded begin event. | Enters requested [proposed]. | No session authority is implied. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] |
| 4 · ACCEPTED | C-ENROLL.15.1 — Recovery before the prerequisite snapshot | Only the durable begin event. | Stays idle after a pre-snapshot crash. | No session or BAI call is inferred. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |
| 5 · ACCEPTED | C-ENROLL.16.2 — Fresh enrollment-session requirements | A new explicit begin event. | Requires a fresh choice for the new session. | Historical intent cannot restart capture. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22] |

SUB-PARTS: NONE

### C-ENROLL.3.2 — Stable enrollment operation identity
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]

ALONE
- What it is: ACCEPTED — `enrollment_operation_id` [proposed], one stable parent per logical enrollment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Takes in: ACCEPTED — The durable explicit-begin event identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Does: ACCEPTED — Keys the parent to that begin and keeps stages, segments, ingestion, readings, profile/link work, retries and recovery attached to one parent. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Gives out: ACCEPTED — A stable coordination identity, initially without session authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Must never: ACCEPTED — Multiply evidence weight by recording child stages or replay. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.3.1 — Durable explicit-begin event: the parent key. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.2.8 — Prerequisite-check operation reference | The parent identity. | Sends operation_ref with the prerequisite request. | Owner reads are associated with the correct operation. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 2 · ACCEPTED | C-ENROLL.4.3.1 — Bound operation identity | The single parent identity. | Binds the consumed proof to that operation. | The proof cannot migrate to another parent. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] |
| 3 · ACCEPTED | C-ENROLL.5.3.1 — Capture operation reference | The current parent identity. | Carries enrollment_operation_ref. | The capture request is attributable to its parent. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 4 · ACCEPTED | C-ENROLL.10.5.3 — Bundle operation and session references | The parent identity. | Preserves it with the session reference. | The bundle remains attributable to its operation. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] |
| 5 · ACCEPTED | C-ENROLL.13.1 — Enrollment parent operation record | The stable parent identity. | Associates all child stages with one operation. | Competing parent truths are excluded. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |

SUB-PARTS: NONE

### C-ENROLL.3.3 — Prospective enrollment session identity
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]

ALONE
- What it is: ACCEPTED — `enrollment_session_id` [proposed], reserved prospectively before authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Takes in: ACCEPTED — One claimed explicit-begin operation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Does: ACCEPTED — Remains prospective until the session-open commit; an opened session has one identity bound to its consumption proof. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Gives out: ACCEPTED — The prospective session reference, authoritative as a session only at opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Must never: ACCEPTED — Authorize capture through reservation or reopen an interrupted session under its old identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Fails closed by: ACCEPTED — Without the opening commit, no session exists. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.3 — Explicit enrollment beginning: the prospective reservation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.4.3.2 — Bound session identity | The reserved session identity. | Binds one proof to that session. | A second session cannot reuse it. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] |
| 2 · ACCEPTED | C-ENROLL.5.3.2 — Capture session reference | The identity of the actually opened session. | Carries enrollment_session_ref. | An old interrupted identity cannot authorize new capture. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] |
| 3 · ACCEPTED | C-ENROLL.10.5.3 — Bundle operation and session references | The actual collection-session identity. | Preserves it with the parent reference. | The bundle names the collection session without new authority. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] |
| 4 · ACCEPTED | C-ENROLL.13.1 — Enrollment parent operation record | The prospective or opened session identity. | Retains its actual status in parent history. | Reservation cannot masquerade as session opening. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |
| 5 · ACCEPTED | C-ENROLL.16.2 — Fresh enrollment-session requirements | A new prospective session identity. | Requires a new identity and its own opening. | The interrupted session cannot be reopened. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22] |

SUB-PARTS: NONE

### C-ENROLL.3.4 — One-begin coordination claim
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]

ALONE
- What it is: ACCEPTED — `enrollment_begin_claim` [proposed], the one-begin-one-session coordination slot. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Takes in: ACCEPTED — The durable explicit-begin event identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Does: ACCEPTED — Allows one active claim and exactly one prospective session for that begin; a repeat tap is absorbed by the claim. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — Serialized reservation without authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Must never: ACCEPTED — Become a second BAI pending record or grant enrollment authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Fails closed by: ACCEPTED — A duplicate begin cannot reserve a second session through the same claim. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.3.1 — Durable explicit-begin event: the claim key. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.3 — Explicit enrollment beginning | The begin-event-keyed claim. | Reserves only its one prospective session. | Repeat taps cannot create another session. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B] |
| 2 · ACCEPTED | C-ENROLL.4.5 — Opening duplicate barriers | The serialized begin reservation. | Uses it alongside the independent BAI/proof barriers. | One begin cannot create competing openings. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B] |
| 3 · ACCEPTED | C-ENROLL.4.5.1 — Duplicate-begin barrier | An existing claim for the same begin. | Absorbs the repeat into its single reservation. | No second prospective session is created. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B] |

SUB-PARTS: NONE

### C-ENROLL.3.5 — Begin request phone-binding reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — `trusted_phone_binding_ref` in I1. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — The permanently trusted phone's binding reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Identifies the phone from which the dedicated begin request comes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — Structural binding provenance without private key material. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Must never: ACCEPTED — Replace hardware-backed binding with an OS device identifier. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — A phone lacking final permanent trust cannot originate a valid I1 request. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: DESIGNED — C-PAIR.1.2.3 — Hardware-backed phone binding: actual cryptographic identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.4 — Ordered authorization and opening
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The exact ten-step enrollment opening sequence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Takes in: ACCEPTED — Explicit trusted-phone begin, prospective operation/session identities and six live prerequisite facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Does: ACCEPTED — Records begin; reserves identities; verifies all six; calls BAI for `voice_enrollment_ness`; lets BAI create its sole pending record and native prompt; receives a matched-success token; rereads all six owners; revokes rather than consumes if any changed; otherwise consumes once, flushes and verifies bound proof, then commits `enrollment_session_opened`; only afterward may capture begin. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Gives out: ACCEPTED — One proof-bound committed opening or a recorded refusal/revocation without opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Must never: ACCEPTED — Treat an OS success as an identified Ness, consume before the final recheck or start the microphone before the opening commit. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Failed initial checks prevent the BAI request; changed final checks revoke with no consumption; absent durable verified proof prevents opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.3 — Explicit enrollment beginning: claimed explicit action and prospective identities; C-ENROLL.2 — Six-owner prerequisite check: initial and immediately rechecked facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Fed by: ACCEPTED — C-BAI.19.1 — Enrollment BAI request interface: BAI-owned pending and token responses; C-BAI.19.3 — Enrollment durable consumption proof: actual flushed proof; C-BAI.19.4 — Enrollment proof binding without new authority: verifiable operation/session binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gated by: ACCEPTED — C-BAI.19.2 — Enrollment prerequisite revalidation: changed prerequisites prohibit consumption. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: C-ENROLL.4.1 — Enrollment BAI request fields; C-ENROLL.4.2 — Final owner recheck and revocation; C-ENROLL.4.3 — Durable authorization chain and binding; C-ENROLL.4.4 — Proof-bound session-open commit; C-ENROLL.4.5 — Opening duplicate barriers; C-ENROLL.4.6 — Spent proof without an opened session; C-ENROLL.4.7 — Opened session with confirmed zero capture

### C-ENROLL.4.1 — Enrollment BAI request fields
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — The enrollment caller's I3 request, using the existing BAI request interface. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — Exactly `purpose = "voice_enrollment_ness"`, `requester`, `operation_ref` and `session_ref`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Supplies the verified operation and prospective session to BAI after all six initial prerequisites hold. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — BAI returns `pending_id` or refusal, then `token_ref` or failure. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Carry a challenge, key or biometric datum across this interface or retry BAI automatically. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: ACCEPTED — A second request while BAI already has a pending record is refused; failure becomes terminal and notifies the requester; restart preserves no token. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-BAI.19.1 — Enrollment BAI request interface: owns the response and one-pending rule. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: ACCEPTED — C-ENROLL.2 — Six-owner prerequisite check: all six initially true before this request. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.4.2 — Final owner recheck and revocation
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The final live-owner check immediately before consuming the enrollment token. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Takes in: ACCEPTED — The issued token and freshly reread six prerequisite owners. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Does: ACCEPTED — If any prerequisite changed, calls BAI to revoke the unconsumed token and records `enrollment_token_revoked_prereq_changed` plus `enrollment_prerequisite_failed`, naming the failing prerequisite by reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Gives out: ACCEPTED — Either permission to continue to consumption or revocation without opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Must never: ACCEPTED — Trust the old snapshot or reveal private prerequisite content in the failure record. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — A changed prerequisite produces neither consumption nor a session opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.2 — Six-owner prerequisite check: fresh actual owner facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Gated by: ACCEPTED — C-BAI.19.2 — Enrollment prerequisite revalidation: BAI's required revalidation boundary. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Changes: DESIGNED — C-BAI.5.4 — Revoked token state: BAI revokes the issued token and owns `bai_token_revoked`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.4.5.5 — Changed-prerequisite consumption barrier | A changed live prerequisite. | Revokes before consumption. | No changed-prerequisite token opens a session. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] |
| 2 · ACCEPTED | C-ENROLL.6.5 — Prerequisites rechecked state | The six owners reread before consumption. | Records prerequisites_rechecked [proposed]. | Changed prerequisites take the revoke path. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] |
| 3 · ACCEPTED | C-ENROLL.14.6 — Prerequisite failed enrollment event | A changed final prerequisite. | Records the failing owner reference. | No token consumption or session opening follows. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] |
| 4 · ACCEPTED | C-ENROLL.14.7 — Prerequisite-change token-revocation enrollment event | The actual change and BAI revocation outcome. | Records the enrollment-side revocation consequence. | BAI retains ownership of bai_token_revoked. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] |
| 5 · ACCEPTED | C-ENROLL.15.5 — Recovery after failed prerequisites or revocation | The actual failed/revoked outcome. | Preserves terminal status. | Another attempt uses a new operation. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |

SUB-PARTS: NONE

### C-ENROLL.4.3 — Durable authorization chain and binding
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]

ALONE
- What it is: ACCEPTED — The verifiable chain from explicit begin to the single session-open commit. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Takes in: ACCEPTED — Begin-event reference, snapshot and owner versions, pending reference, token reference, flushed purpose-specific consumption proof, operation/session identities and opening commit. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Does: ACCEPTED — Binds proof directly or by `enrollment_authorization_binding` [proposed], an append-only integrity-protected companion referencing the BAI event and referenced by that event or the session-open commit. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gives out: ACCEPTED — A durable verifiable relationship after BAI memory vanishes; BAI still owns consumption. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Must never: ACCEPTED — Log biometric data, challenges, private keys or raw token material, or make the companion a second BAI authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Fails closed by: ACCEPTED — If the flushed proof or its binding cannot be verified, the session-open commit is prohibited. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-BAI.19.3 — Enrollment durable consumption proof: the actual flushed event; C-BAI.19.4 — Enrollment proof binding without new authority: direct or companion binding semantics. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.4.3.11 — Bound audit integrity reference | The actual protected authorization chain. | Carries its integrity reference. | Unverifiable linkage cannot satisfy opening. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] |
| 2 · ACCEPTED | C-ENROLL.4.4 — Proof-bound session-open commit | Verified flushed and bound proof. | Commits the single session opening only afterward. | The prospective session becomes an actual opened session. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] |
| 3 · ACCEPTED | C-ENROLL.6.6 — Token durably consumed state | Verified integrity-protected proof binding. | Records token_consumed_durably [proposed] with BAI's flushed fact. | Opening remains a separate commit. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] |
| 4 · ACCEPTED | C-ENROLL.10.5.4 — Bundle prerequisite and authorization evidence | The verified bound authorization chain. | Includes its references without secrets. | Collection provenance remains inspectable. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] |

SUB-PARTS: C-ENROLL.4.3.1 — Bound operation identity; C-ENROLL.4.3.2 — Bound session identity; C-ENROLL.4.3.3 — Bound token reference; C-ENROLL.4.3.4 — Bound pending-record reference; C-ENROLL.4.3.5 — Bound enrollment purpose; C-ENROLL.4.3.6 — Bound hardware phone key reference; C-ENROLL.4.3.7 — Bound prerequisite-snapshot reference; C-ENROLL.4.3.8 — Bound trusted-local timestamps; C-ENROLL.4.3.9 — Bound requester identity; C-ENROLL.4.3.10 — Bound audit schema and version; C-ENROLL.4.3.11 — Bound audit integrity reference

### C-ENROLL.4.3.1 — Bound operation identity
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]

ALONE
- What it is: ACCEPTED — The binding's `enrollment_operation_id` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Takes in: ACCEPTED — The one explicit-begin parent identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Does: ACCEPTED — Ties consumption proof to that operation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gives out: ACCEPTED — A verifiable operation-specific proof reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Must never: ACCEPTED — Repurpose the proof for another enrollment operation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Fails closed by: ACCEPTED — Unverifiable operation binding prevents opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.3.2 — Stable enrollment operation identity: the identity to bind. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.4.3.2 — Bound session identity
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]

ALONE
- What it is: ACCEPTED — The binding's `enrollment_session_id` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Takes in: ACCEPTED — The reserved prospective session identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Does: ACCEPTED — Binds one consumption proof to exactly that session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Gives out: ACCEPTED — A session-specific proof binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Must never: ACCEPTED — Open a second session with the same proof. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Fails closed by: ACCEPTED — A second session referencing the proof is refused. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.3.3 — Prospective enrollment session identity: the reserved identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.4.5.3 — Same-proof second-session barrier | The proof's sole session identity. | Refuses another session referencing that proof. | Consumed authority is not copied. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B] |

SUB-PARTS: NONE

### C-ENROLL.4.3.3 — Bound token reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]

ALONE
- What it is: ACCEPTED — The consumed token reference in the binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Takes in: ACCEPTED — The BAI-owned token identity by reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Does: ACCEPTED — Identifies which token's consumed fact authorizes the single opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gives out: ACCEPTED — A durable token reference without raw token material. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Must never: ACCEPTED — Turn the recorded reference into reusable token authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Fails closed by: ACCEPTED — An unverifiable proof binding prevents opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-BAI.19.3 — Enrollment durable consumption proof: token consumption truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.4.3.4 — Bound pending-record reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]

ALONE
- What it is: ACCEPTED — The BAI pending-record reference in the authorization binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Takes in: ACCEPTED — The pending identity associated with the actual matched biometric result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Does: ACCEPTED — Preserves the authorization chain back to BAI's pending request. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gives out: ACCEPTED — Pending-request provenance after volatile state disappears. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Must never: ACCEPTED — Recreate live BAI pending authority from its history. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: ACCEPTED — An unmatched biometric result is rejected, with `bai_unmatched_result`; it cannot satisfy the chain. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]

TOGETHER
- Fed by: ACCEPTED — C-BAI.19.1 — Enrollment BAI request interface: the original pending identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.4.3.5 — Bound enrollment purpose
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]

ALONE
- What it is: ACCEPTED — The binding's exact purpose, `voice_enrollment_ness`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Takes in: ACCEPTED — BAI's purpose-bound consumption fact. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Does: ACCEPTED — Keeps the proof restricted to initial Ness enrollment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gives out: ACCEPTED — Purpose-specific opening evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Must never: ACCEPTED — Substitute a token for another purpose. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Proof not verifiable for this purpose cannot open the session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]

TOGETHER
- Fed by: DESIGNED — C-BAI.3.9.3 — Ness enrollment purpose: the existing purpose owner. [V10 §25.6] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.4.3.6 — Bound hardware phone key reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]

ALONE
- What it is: ACCEPTED — `app_session_key_ref`, the trusted-phone binding in the proof chain. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Takes in: ACCEPTED — The phone's hardware-backed key reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Does: ACCEPTED — Binds the consumed authorization to that trusted phone. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gives out: ACCEPTED — A reference, never private key material. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Must never: ACCEPTED — Substitute an OS device identifier or log the private key. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Fails closed by: ACCEPTED — An unverifiable binding blocks the opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: DESIGNED — C-BAI.3.8 — App-instance key reference: the hardware-backed phone binding. [V10 §25.6] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.4.3.7 — Bound prerequisite-snapshot reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]

ALONE
- What it is: ACCEPTED — The prerequisite-snapshot reference within the durable binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Takes in: ACCEPTED — The check identity and its owner-version provenance. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Does: ACCEPTED — Connects the proof to the prerequisite checks without replacing the actual owners. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gives out: ACCEPTED — An inspectable prerequisite evidence link. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Must never: ACCEPTED — Use this historical reference instead of the final live-owner recheck. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Unverifiable prerequisite binding prevents opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.2.7 — Versioned prerequisite snapshot: the check identity and versioned entries. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.4.3.8 — Bound trusted-local timestamps
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]

ALONE
- What it is: ACCEPTED — BAI's trusted-local timestamps in the consumption binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Takes in: ACCEPTED — The actual authorization timestamps. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Does: ACCEPTED — Retains the temporal provenance of BAI's proof. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gives out: ACCEPTED — Trusted-local time evidence within the verified chain. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Must never: ACCEPTED — Reconstruct live token validity from historical timestamps after restart. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Fails closed by: ACCEPTED — An unverifiable chain prevents opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]

TOGETHER
- Fed by: ACCEPTED — C-BAI.19.3 — Enrollment durable consumption proof: BAI's actual audit times. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.4.3.9 — Bound requester identity
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]

ALONE
- What it is: ACCEPTED — The requester identity carried in the durable binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Takes in: ACCEPTED — The requester associated with the BAI operation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Does: ACCEPTED — Keeps the proof tied to its actual requesting component. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gives out: ACCEPTED — Verifiable requester provenance. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Must never: ACCEPTED — Treat requester identity as proof of the captured speaker's identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Unverified requester binding cannot satisfy opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: DESIGNED — C-BAI.3.4 — Pending requester: the BAI requester's identity. [V10 §25.6] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.4.3.10 — Bound audit schema and version
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]

ALONE
- What it is: ACCEPTED — The audit schema/version reference in the proof binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Takes in: ACCEPTED — The actual audit record's schema and version identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Does: ACCEPTED — Keeps the durable proof interpretable under its identified audit form. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gives out: ACCEPTED — Audit schema/version provenance without selecting a new serialization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §25]
- Must never: ACCEPTED — Invent final implementation field names or schema encoding here. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §25]
- Fails closed by: ACCEPTED — An unverifiable audit binding prevents opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-BAI.19.3 — Enrollment durable consumption proof: the real audit record. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.4.3.11 — Bound audit integrity reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]

ALONE
- What it is: ACCEPTED — The integrity reference protecting the durable proof binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Takes in: ACCEPTED — The verified BAI event and any append-only companion reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Does: ACCEPTED — Makes the consumption-to-operation/session relationship verifiable after restart. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gives out: ACCEPTED — Integrity-protected proof linkage. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Must never: ACCEPTED — Treat an unverified coordination entry as proof. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Fails closed by: ACCEPTED — Failed verification blocks the opening commit. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.4.3 — Durable authorization chain and binding: the protected chain. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.4.4 — Proof-bound session-open commit
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]

ALONE
- What it is: ACCEPTED — The separate `enrollment_session_opened` commit, keyed to one verified consumed-token proof. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Takes in: ACCEPTED — A flushed `bai_token_consumed` bound to this operation and prospective session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Does: ACCEPTED — Verifies the durable proof and binding before committing opening; only this commit makes the prospective session real. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Gives out: ACCEPTED — One committed opening referenced by subsequent capture and the BAI-sourced success observation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Infer durable authorization from BAI memory, a claim, an OS result or an unflushed event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: ACCEPTED — Missing or unverifiable flushed proof/binding prevents the commit. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.4.3 — Durable authorization chain and binding: verified bound proof. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gated by: ACCEPTED — C-BAI.19.3 — Enrollment durable consumption proof: the BAI-owned event must be flushed and verified. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Changes: ACCEPTED — C-BOP.15.4 — Single enrollment biometric success observation: permits timing coordination after actual opening, with BAI as sole source. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.4.5.2 — Second-proof same-session barrier | The original opening's proof key. | Refuses and records a second different proof. | The session keeps its single original proof binding. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B] |
| 2 · ACCEPTED | C-ENROLL.5 — Capture-control and observation boundary | Current committed opening. | Checks it before capture intent and request. | Opening alone never proves physical capture. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 3 · ACCEPTED | C-ENROLL.5.1 — Current capture preconditions | Actual current session-open truth. | Includes it in the live capture conjunction. | Absent or noncurrent opening prevents capture. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] |
| 4 · ACCEPTED | C-ENROLL.5.3.3 — Capture opening-commit reference | The current opening commit. | References that real commit in I5A. | A reservation cannot stand in for opening. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 5 · ACCEPTED | C-ENROLL.5.7 — Enrollment biometric-observation timing | Opening referencing durable BAI proof. | Coordinates the timing of BAI's single physical success fact. | The coordinator never becomes the observation source. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 6 · ACCEPTED | C-ENROLL.6 — Enrollment process lifecycle | The actual opening commit. | Uses it as the opening-state entry fact. | A reserved identity cannot appear as an opened session. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] |
| 7 · ACCEPTED | C-ENROLL.6.7 — Session opened process state | Committed enrollment_session_opened. | Enters session_opened [proposed]. | The session exists without a claim of microphone start. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] |
| 8 · ACCEPTED | C-ENROLL.14.2 — Session opened enrollment event | The actual proof-bound opening. | Commits enrollment_session_opened. | Prospective identity becomes a real session only here. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] |

SUB-PARTS: NONE

### C-ENROLL.4.5 — Opening duplicate barriers
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]

ALONE
- What it is: ACCEPTED — Eight separate protections around begin, pending state, proof and opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Takes in: ACCEPTED — The begin claim, BAI pending/result, live prerequisites, consumption proof and current session identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Does: ACCEPTED — Serializes the begin, rejects duplicate or mismatched authorization, rereads owners and requires flushed proof before opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Gives out: ACCEPTED — At most one authorized opening for one begin and one proof. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Must never: ACCEPTED — Make coordination a substitute BAI pending or authorization state. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Fails closed by: ACCEPTED — The violating request is refused or the changed-prerequisite token is revoked without opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.3.4 — One-begin coordination claim: serialized reservation; C-BAI.19.3 — Enrollment durable consumption proof: the actual proof. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: C-ENROLL.4.5.1 — Duplicate-begin barrier; C-ENROLL.4.5.2 — Second-proof same-session barrier; C-ENROLL.4.5.3 — Same-proof second-session barrier; C-ENROLL.4.5.4 — Unmatched biometric-result barrier; C-ENROLL.4.5.5 — Changed-prerequisite consumption barrier; C-ENROLL.4.5.6 — Missing durable-proof barrier; C-ENROLL.4.5.7 — Stale-snapshot barrier; C-ENROLL.4.5.8 — Concurrent BAI-pending barrier

### C-ENROLL.4.5.1 — Duplicate-begin barrier
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]

ALONE
- What it is: ACCEPTED — The barrier to one begin opening two sessions. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Takes in: ACCEPTED — A repeated request with the same durable begin identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Does: ACCEPTED — Uses the existing claim's single prospective session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Gives out: ACCEPTED — An absorbed repeat without another reservation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Grant authority from the coordination slot. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Fails closed by: ACCEPTED — The same begin cannot obtain two sessions. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-ENROLL.3.4 — One-begin coordination claim: admits exactly one prospective session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.4.5.2 — Second-proof same-session barrier
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]

ALONE
- What it is: ACCEPTED — The barrier to two tokens successfully opening one session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Takes in: ACCEPTED — A second, different consumption proof for an already-opened session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Does: ACCEPTED — Refuses and records the second proof. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Gives out: ACCEPTED — The original single proof-bound opening remains. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Must never: ACCEPTED — Replace the opening's proof with a later token. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Fails closed by: ACCEPTED — A different second proof cannot reopen or reauthorize that session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.4.4 — Proof-bound session-open commit: its original proof key. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.4.5.3 — Same-proof second-session barrier
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]

ALONE
- What it is: ACCEPTED — The barrier to one token opening two sessions. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Takes in: ACCEPTED — A second session referencing a consumption proof already bound elsewhere. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Does: ACCEPTED — Refuses the second session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Gives out: ACCEPTED — One proof remains bound to exactly one session identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Must never: ACCEPTED — Copy consumed authority into another session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Fails closed by: ACCEPTED — Reuse cannot produce the second opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.4.3.2 — Bound session identity: the proof's sole session binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.4.5.4 — Unmatched biometric-result barrier
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]

ALONE
- What it is: ACCEPTED — The rejection of an old prompt result without a current matching pending record. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Takes in: ACCEPTED — An expired, absent or mismatched BAI pending/result relationship. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Does: ACCEPTED — Leaves rejection to BAI and records `bai_unmatched_result` under BAI ownership. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Gives out: ACCEPTED — No enrollment authorization from the unmatched result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Must never: ACCEPTED — Treat old biometric success as fresh approval. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Fails closed by: ACCEPTED — No matching pending record means no token from that result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]

TOGETHER
- Fed by: ACCEPTED — C-BAI.19.1 — Enrollment BAI request interface: actual pending/result truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.4.5.5 — Changed-prerequisite consumption barrier
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]

ALONE
- What it is: ACCEPTED — The barrier to consuming after a prerequisite changes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Takes in: ACCEPTED — A changed live owner result after the biometric prompt. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Does: ACCEPTED — Revokes the token instead of consuming it. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Gives out: ACCEPTED — Revocation and prerequisite-failure evidence by reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Must never: ACCEPTED — Open on the earlier affirmative snapshot. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Fails closed by: ACCEPTED — No consumption and no opening follow the changed prerequisite. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.4.2 — Final owner recheck and revocation: the detected change and revoke path. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.4.5.6 — Missing durable-proof barrier
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]

ALONE
- What it is: ACCEPTED — The enforced requirement for verified flushed proof before opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Takes in: ACCEPTED — The proposed session-open commit and its consumption reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Does: ACCEPTED — Requires the actual flushed event bound to this operation/session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Gives out: ACCEPTED — An opening only when the durable precondition is met. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Must never: ACCEPTED — Substitute an in-memory success flag. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Fails closed by: ACCEPTED — No verified durable proof means no opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-BAI.19.3 — Enrollment durable consumption proof: actual flushed evidence is required. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.4.5.7 — Stale-snapshot barrier
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]

ALONE
- What it is: ACCEPTED — The barrier to treating a recorded prerequisite snapshot as current authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Takes in: ACCEPTED — Prior snapshot references and current owner access. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Does: ACCEPTED — Rereads the owners immediately before consumption. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Gives out: ACCEPTED — Current prerequisite truth for the final check. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Must never: ACCEPTED — Authorize from snapshot age or prior satisfaction alone. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Fails closed by: ACCEPTED — Unverifiable or changed current facts prevent consumption. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.2 — Six-owner prerequisite check: fresh owner responses. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.4.5.8 — Concurrent BAI-pending barrier
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]

ALONE
- What it is: ACCEPTED — BAI's existing one-pending-record boundary as consumed by enrollment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Takes in: ACCEPTED — An enrollment request while BAI already holds a pending record. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Accepts BAI's refusal rather than creating another pending record. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Gives out: ACCEPTED — A recorded refusal with no concurrent enrollment prompt. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Create enrollment-specific shadow pending authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Fails closed by: ACCEPTED — The second request cannot proceed while one is pending. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-BAI.19.1 — Enrollment BAI request interface: its single-pending rule controls admission. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.4.6 — Spent proof without an opened session
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]

ALONE
- What it is: ACCEPTED — Consumption committed, but the session-open commit did not. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]
- Takes in: ACCEPTED — Verified durable consumed-token proof without an opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]
- Does: ACCEPTED — Leaves the token spent and records `enrollment_aborted_before_capture` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]
- Gives out: ACCEPTED — An honest abort in which no session existed and no capture begins. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]
- Must never: ACCEPTED — Forward-complete the missing opening or use `enrollment_session_closed` to imply a session existed. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]
- Fails closed by: ACCEPTED — A later attempt requires a new explicit begin and fresh token. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]

TOGETHER
- Fed by: ACCEPTED — C-BAI.19.5 — Enrollment consumed-proof crash boundary: actual spent-proof truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.6.14 — Aborted before capture process state | Spent proof without an opening. | Records aborted_before_capture [proposed]. | No session is falsely claimed to have existed. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C] |
| 2 · ACCEPTED | C-ENROLL.6.28 — Separate session and parent lifecycles | The spent-before-opening abort. | Keeps it distinct from actual opened-session closure. | The record does not invent a session. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C] |
| 3 · ACCEPTED | C-ENROLL.14 — Enrollment audit-event ownership | The real spent-without-opening abort. | Keeps its proposed event separate from the settled nine. | No fictitious session-close event is used. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18] |
| 4 · ACCEPTED | C-ENROLL.15.6 — Recovery after consumption before opening | Spent proof without session opening. | Records the proposed pre-capture abort. | No forward-completed opening or capture occurs. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C] |

SUB-PARTS: NONE

### C-ENROLL.4.7 — Opened session with confirmed zero capture
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]

ALONE
- What it is: ACCEPTED — An opened session whose capture is confirmed never to have begun. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Takes in: ACCEPTED — The real opening and confirmed no-start truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Does: ACCEPTED — Closes honestly with zero captured segments and `enrollment_session_closed`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]
- Gives out: ACCEPTED — A closed zero-segment session, no claim of enrollment material. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]
- Must never: ACCEPTED — Infer no-start from missing observations or automatically start the microphone on recovery. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Fails closed by: ACCEPTED — A later capture needs a new explicit session through the full opening flow. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.5.4.2 — Confirmed capture non-start: verified physical non-start. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.5 — Capture-control and observation boundary
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — The separation of authorized opening, capture intent, B29 physical start and committed BOP observations. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Takes in: ACCEPTED — Current open truth, privacy permission, trusted-phone/security validity and no cancellation/stop condition. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Does: ACCEPTED — Checks current permission; flushes intent; requests B29 capture; records the real start result; lets B29 supply its start fact and BOP supply only actual observations. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Gives out: ACCEPTED — `capture_start_result` and committed observation references, with unknown start retained as unknown. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Must never: ACCEPTED — Treat intent, acknowledgment or absent observations as proof that audio was or was not captured. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Fails closed by: ACCEPTED — Invalid current opening/privacy/security or any stop condition prevents capture; restart never reopens the microphone automatically. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.4.4 — Proof-bound session-open commit: current opening; C-BOP.15.1 — B29 capture and BOP observation ownership: actual observed truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture must be privacy-permitted; C-9 — Access/authentication model + voice I/O + phone modes (§9): B29 owns physical activation/deactivation and start/stop results. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: C-ENROLL.5.1 — Current capture preconditions; C-ENROLL.5.2 — Durable capture intent; C-ENROLL.5.3 — Reference-only B29 capture request; C-ENROLL.5.4 — B29 capture-start result; C-ENROLL.5.5 — B29-sourced capture-start fact; C-ENROLL.5.6 — Enrollment physical-observation consumption; C-ENROLL.5.7 — Enrollment biometric-observation timing

### C-ENROLL.5.1 — Current capture preconditions
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]

ALONE
- What it is: ACCEPTED — The current conditions checked before an enrollment capture request. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Takes in: ACCEPTED — Current committed opening, current privacy/capture eligibility, current trusted-phone/security validity and cancellation/stop truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Does: ACCEPTED — Requires all to permit capture at the time of request. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Gives out: ACCEPTED — A permitted request only while the opening remains valid and no stop condition holds. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Must never: ACCEPTED — Use historic permission after a safety or privacy change. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Fails closed by: ACCEPTED — A failed current condition means no capture request. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.4.4 — Proof-bound session-open commit: actual current opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current capture eligibility; C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): current trust/security facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.5.2 — Durable capture intent | Current opening/privacy/security/no-stop permission. | Flushes intent only for a permitted request. | The durable record proves intent, never start. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] |
| 2 · ACCEPTED | C-ENROLL.5.3 — Reference-only B29 capture request | The current capture conjunction. | Requires it before sending the bounded request. | Invalid permission produces no capture. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] |

SUB-PARTS: NONE

### C-ENROLL.5.2 — Durable capture intent
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — `enrollment_capture_intent_event` [proposed], owned by enrollment coordination. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Takes in: ACCEPTED — A currently permitted proposed B29 capture request. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Does: ACCEPTED — Flushes before sending the request and proves only that capture was about to be requested. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Gives out: ACCEPTED — Durable intent history containing references rather than audio. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Must never: ACCEPTED — Assert that the microphone started or that a segment was recorded. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Fails closed by: ACCEPTED — Without durable intent, no request is made; after intent with no provable B29 result, start truth is unknown. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-ENROLL.5.1 — Current capture preconditions: current permission precedes intent and request. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.5.3 — Reference-only B29 capture request | Flushed capture intent. | Sends the reference-only B29 request afterward. | Physical activation remains B29-owned. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] |
| 2 · ACCEPTED | C-ENROLL.6.8 — Capture intent flushed state | Durable enrollment_capture_intent_event [proposed]. | Enters capture_intent_flushed [proposed]. | Only about-to-request intent is established. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] |
| 3 · ACCEPTED | C-ENROLL.14 — Enrollment audit-event ownership | The durable proposed intent event. | Retains its coordinator ownership and intent-only meaning. | The settled catalog is not silently extended. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18] |

SUB-PARTS: NONE

### C-ENROLL.5.3 — Reference-only B29 capture request
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — I5A, the enrollment-to-B29 capture-control request. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — Only operation reference, session reference, current committed opening reference, current privacy/capture-eligibility reference, enrollment provenance references, destination BOP context and current cancellation/stop references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Requests physical capture after durable intent; B29 owns activation/deactivation, device interaction, cleanup, transport and physical start/stop truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — `{ capture_start_result: started | confirmed_not_started | unknown }`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Include raw audio or choose B29 hardware, cleanup algorithms, timeouts, channels or final field names. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: ACCEPTED — Missing current opening, privacy permission or clear stop state prevents capture; recovery never automatically reopens it. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.5.2 — Durable capture intent: flushed pre-request history. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Gated by: ACCEPTED — C-ENROLL.5.1 — Current capture preconditions: the live conjunction. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Changes: DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): hands the bounded request to B29's physical capture owner. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-9.2.1 — Microphone capture stage | Physical microphone input. | Supplies the enrollment request carries only the seven permitted reference classes. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [V10 §9] |
| 2 · ACCEPTED | C-9.2.8 — B29 enrollment capture interface | Only enrollment_operation_ref [proposed], enrollment_session_ref [proposed], current committed session-open reference, current privacy/capture-eligibility reference, enrollment provenance references (role/source_title/authorization_type), destination BOP context and current cancellation/stop references. | Supplies the seven permitted reference classes. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] |
| 3 · DESIGNED | C-9.2 — Voice input and output pipeline | Microphone input and material intended for spoken output. | Supplies the bounded enrollment capture request. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [V10 §9] [MAP C-9] |


SUB-PARTS: C-ENROLL.5.3.1 — Capture operation reference; C-ENROLL.5.3.2 — Capture session reference; C-ENROLL.5.3.3 — Capture opening-commit reference; C-ENROLL.5.3.4 — Capture privacy-decision reference; C-ENROLL.5.3.5 — Capture declared-provenance references; C-ENROLL.5.3.6 — Capture destination observation context; C-ENROLL.5.3.7 — Capture cancellation and stop references

### C-ENROLL.5.3.1 — Capture operation reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — `enrollment_operation_ref` in I5A. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — The current parent operation identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Identifies the operation requesting capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — Structural capture-request provenance. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Grant capture permission by identity alone. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.3.2 — Stable enrollment operation identity: the parent reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.5.3.2 — Capture session reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — `enrollment_session_ref` in I5A. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — The currently opened session identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Binds the capture request to that session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — A session-specific capture reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Resume an old interrupted microphone session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Fails closed by: ACCEPTED — An absent or noncurrent opening cannot support capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.3.3 — Prospective enrollment session identity: the identity made real at opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.5.3.3 — Capture opening-commit reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — I5A's current committed session-open reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — Actual current opening truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — References the commit required before microphone activation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — Verifiable opening evidence in the request. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Substitute a prospective reservation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: ACCEPTED — Without current opening truth, no capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.4.4 — Proof-bound session-open commit: the current commit reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.5.3.4 — Capture privacy-decision reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — I5A's current privacy/capture-eligibility decision reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — The actual privacy owner's current decision. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Carries permission by reference, before capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]
- Gives out: ACCEPTED — Protected capture-eligibility evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Copy protected material into the request merely for checking. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — Capture exclusion prevents capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the actual pre-capture privacy decision. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.5.3.5 — Capture declared-provenance references
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — I5A's enrollment provenance references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — `role="ness"`, `source_title="enrollment:ness:<session_id>"` and `session_authorization.authorization_type="enrollment_declared"`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Carries the enrollment flow's declared attribution into the ordinary observation provenance. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — Declared enrollment references, not an SIA identification. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Convert a declared role or formally adopted vocabulary value into confirmed voice identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [V10 §25.12]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-BOP.15.2 — Enrollment observation provenance: canonical provenance bindings and field owners. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.5.3.6 — Capture destination observation context
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — I5A's destination BOP observation context. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — The authorized observation destination by reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Directs the stream into BOP's protected physical-observation boundary. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — A destination reference without raw audio in coordination. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Create a second observation store or bypass BOP. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Unsafe BOP capture does not proceed. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-BOP.15.1 — B29 capture and BOP observation ownership: the actual observation receiver. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.5.3.7 — Capture cancellation and stop references
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — I5A's current cancellation/stop references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — Actual current stop conditions and owner safety events. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Carries those conditions to the physical capture owner. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — Reference-only stop context. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Continue capture on obsolete permission after a stop condition. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — A current stop condition prevents or ends new capture immediately. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.7 — Mid-session protective stop: actual owner-triggered stop conditions. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.5.4 — B29 capture-start result
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — `capture_start_result`, B29's physical start response. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — The actual outcome of the bounded capture request. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Does: ACCEPTED — Preserves exactly one of `started`, `confirmed_not_started` or `unknown`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — Physical start truth without claiming how much BOP recorded. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Must never: ACCEPTED — Rewrite unknown as a confirmed non-start or infer non-start from absent observations. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Fails closed by: ACCEPTED — Unknown start leads to honest close/interruption, preserved actual observations and no automatic microphone reopening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]

TOGETHER
- Fed by: DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): B29 supplies the physical result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.5.4.1 — Confirmed capture start | B29's started result. | Records confirmed physical start. | Recorded segments still depend on actual BOP commits. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] |
| 2 · ACCEPTED | C-ENROLL.5.4.2 — Confirmed capture non-start | B29's confirmed_not_started result. | Permits honest zero-segment closure. | No start is inferred from absent observations. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] |
| 3 · ACCEPTED | C-ENROLL.5.4.3 — Unknown capture-start reality | Unknown or unprovable B29 outcome. | Preserves uncertainty and actual observations. | Closure does not assert that the microphone never began. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] |
| 4 · ACCEPTED | C-ENROLL.6 — Enrollment process lifecycle | The real B29 start result. | Distinguishes running capture from non-start and uncertainty. | State labels preserve physical-start reality. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] |
| 5 · ACCEPTED | C-ENROLL.7.8 — Application or machine restart safety change | Any provable start result surviving restart. | Preserves unknown when no result is provable. | Restart cannot assert non-start or reopen the microphone. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |
| 6 · ACCEPTED | C-9.2.8 — B29 enrollment capture interface | Only enrollment_operation_ref [proposed], enrollment_session_ref [proposed], current committed session-open reference, current privacy/capture-eligibility reference, enrollment provenance references (role/source_title/authorization_type), destination BOP context and current cancellation/stop references. | Takes this place's change: supplies started/confirmed_not_started/unknown truth. | Supplies started/confirmed_not_started/unknown truth. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |

SUB-PARTS: C-ENROLL.5.4.1 — Confirmed capture start; C-ENROLL.5.4.2 — Confirmed capture non-start; C-ENROLL.5.4.3 — Unknown capture-start reality

### C-ENROLL.5.4.1 — Confirmed capture start
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]

ALONE
- What it is: ACCEPTED — `started`, the confirmed B29 start result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Takes in: ACCEPTED — B29's provable physical-start outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Does: ACCEPTED — Establishes that the pipeline began; BOP separately establishes actual committed observations. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Gives out: ACCEPTED — Start truth, not proof that any particular segment was recorded. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Must never: ACCEPTED — Invent missing audio from a start acknowledgment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Fails closed by: ACCEPTED — A subsequent crash interrupts capture, preserves only actual commits and never resumes the same microphone session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.5.4 — B29 capture-start result: the verified started value. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.6.9 — Capturing process state | B29's provable start. | Enters capturing [proposed] while capture runs. | BOP separately owns observation commitments. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] |

SUB-PARTS: NONE

### C-ENROLL.5.4.2 — Confirmed capture non-start
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]

ALONE
- What it is: ACCEPTED — `confirmed_not_started`, a provable B29 non-start result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Takes in: ACCEPTED — Actual confirmation that capture never began. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Does: ACCEPTED — Permits honest zero-segment closure. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Gives out: ACCEPTED — No claimed enrollment material. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Must never: ACCEPTED — Infer this result solely from missing BOP observations. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Fails closed by: ACCEPTED — No automatic reattempt or microphone activation follows the non-start. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.5.4 — B29 capture-start result: the verified non-start value. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.4.7 — Opened session with confirmed zero capture | Provable B29 non-start truth. | Closes the opened session with zero segments. | No material or automatic microphone reattempt is claimed. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] |

SUB-PARTS: NONE

### C-ENROLL.5.4.3 — Unknown capture-start reality
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]

ALONE
- What it is: ACCEPTED — `unknown`, when durable intent exists without a provable B29 outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Takes in: ACCEPTED — The intent history and any BOP observations that actually committed. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Does: ACCEPTED — Preserves uncertainty and closes or interrupts honestly. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Gives out: ACCEPTED — An unknown-start record with the actual captured set preserved. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Must never: ACCEPTED — Claim the microphone never began or fabricate a start result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Fails closed by: ACCEPTED — Does not reopen the microphone or reconstruct missing audio. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.5.4 — B29 capture-start result: unavailable or unknown physical truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.6.10 — Capture start unknown state | Durable intent with no provable start outcome. | Enters capture_start_unknown [proposed]. | Unknown is not rewritten as never started. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-ENROLL.15.8 — Recovery after intent without a provable start result | Unprovable start after durable intent. | Preserves unknown start and actual observations. | Recovery neither claims non-start nor reopens the microphone. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] |

SUB-PARTS: NONE

### C-ENROLL.5.5 — B29-sourced capture-start fact
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]

ALONE
- What it is: ACCEPTED — `enrollment_capture_started` [proposed interface fact], owned and sourced by B29. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Takes in: ACCEPTED — B29's actual physical pipeline start. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Does: ACCEPTED — Proves only that capture physically began. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Gives out: ACCEPTED — A start reference, separate from enrollment intent and BOP observation commitments. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Must never: ACCEPTED — Become an enrollment-coordinator assertion that a segment exists. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Fails closed by: ACCEPTED — Without provable B29 start truth, no start fact is fabricated. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]

TOGETHER
- Fed by: DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): the B29 source of physical start truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.14 — Enrollment audit-event ownership | B29's proposed start interface fact. | Keeps the physical source separate from enrollment audit ownership. | Start truth is never fabricated by coordination. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18] |
| 2 · ACCEPTED | C-9.2.8 — B29 enrollment capture interface | Only enrollment_operation_ref [proposed], enrollment_session_ref [proposed], current committed session-open reference, current privacy/capture-eligibility reference, enrollment provenance references (role/source_title/authorization_type), destination BOP context and current cancellation/stop references. | Takes this place's change: supplies only a real pipeline start. | Supplies only a real pipeline start. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-ENROLL.5.6 — Enrollment physical-observation consumption
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — Enrollment's consumption of I5B physical observations from the protected B29/BOP boundary. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — BOP-owned committed observations with stable `capture_id`, durable ordering, observation-quality fields and failure observations. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — References actual DUMB observations and their declared provenance; A15 condition notes remain bounded physical context under the receiving owner's rules. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — Observation references available for the later frozen set, never an independent identity or profile-membership decision. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Infer identity, speaker change, spoofing, imitation risk, emotion, intent, meaning, importance, behavioral pattern or causation from acoustic-condition notes alone. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — Unsafe or privacy-excluded capture does not proceed; missing observations do not prove non-start. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-BOP.15.1 — B29 capture and BOP observation ownership: committed stream truth; C-BOP.15.2 — Enrollment observation provenance: declared attribution; C-BOP.12 — Optional acoustic_condition_notes amendment: the existing six-field record and five controlled physical-condition names. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: ACCEPTED — C-BOP.15.6 — Protected raw-voice boundary: minimum necessary protected interface and no raw voice in coordination. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.5.7 — Enrollment biometric-observation timing
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — Timing coordination for I5C's one BAI-to-BOP success observation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — The committed session opening referencing durable consumed-token proof. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Coordinates the moment when BAI supplies `command_identifier="biometric:result:success"` with exactly the session ID and N.H trusted-local timestamp. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — One BAI-sourced observation under deterministic `capture_id` derived from session identity, command identity and the single opening commit. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Fabricate the observation, become its source, include purpose/token ID/biometric data/authorization conclusions or claim Ness was identified. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: ACCEPTED — No actual opening and BAI fact means no success observation; recovery absorbs duplicate identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-BAI.19.6 — BAI-owned enrollment success observation: sole source; C-BOP.15.4 — Single enrollment biometric success observation: idempotent physical receiver. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: ACCEPTED — C-ENROLL.4.4 — Proof-bound session-open commit: actual opening must precede the observation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6 — Enrollment process lifecycle
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — The process states for authorization, capture, roots, readings, linkage and profile creation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — Actual committed facts from each stage's owner. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Advances through the source's states only on their stated entry facts; session termination and parent termination remain distinct. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8A]
- Gives out: ACCEPTED — A truthful process state and at most one winning parent-terminal outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]
- Must never: ACCEPTED — Use a state label to claim that the voice is confirmed as Ness's, infer success from coordination or regress committed facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]
- Fails closed by: ACCEPTED — An unverified owner fact cannot establish the corresponding state; protective conditions block and terminal failures remain terminal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.4.4 — Proof-bound session-open commit: opening truth; C-ENROLL.5.4 — B29 capture-start result: start truth; C-7L.11 — Provisional enrollment Person-Box link: link truth; C-SIA.20.2 — Provisional profile commit identity: profile truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.6.29 — Legal transition and terminal rules | Current states and actual owner commitments. | Applies legal nonterminal transition and absorbing-terminal rules. | Committed facts never regress and only one parent terminal wins. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B] |
| 2 · ACCEPTED | C-ENROLL.13.1 — Enrollment parent operation record | Actual process-state facts. | Records current state and the terminal outcome. | Terminal results remain absorbing. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |
| 3 · ACCEPTED | C-ENROLL.13.1.2 — Parent process-state field | Source-defined state vocabulary and actual entry facts. | Records only an owner-supported state. | Coordinator inference cannot create success. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] |

SUB-PARTS: C-ENROLL.6.1 — Requested process state; C-ENROLL.6.2 — Initial prerequisites verified state; C-ENROLL.6.3 — Biometric pending process state; C-ENROLL.6.4 — Token issued process state; C-ENROLL.6.5 — Prerequisites rechecked state; C-ENROLL.6.6 — Token durably consumed state; C-ENROLL.6.7 — Session opened process state; C-ENROLL.6.8 — Capture intent flushed state; C-ENROLL.6.9 — Capturing process state; C-ENROLL.6.10 — Capture start unknown state; C-ENROLL.6.11 — Closing process state; C-ENROLL.6.12 — Closed process state; C-ENROLL.6.13 — Interrupted process state; C-ENROLL.6.14 — Aborted before capture process state; C-ENROLL.6.15 — Roots pending submission state; C-ENROLL.6.16 — Roots partially committed state; C-ENROLL.6.17 — Roots committed state; C-ENROLL.6.18 — Readings pending state; C-ENROLL.6.19 — Readings partially completed state; C-ENROLL.6.20 — Profile readiness pending state; C-ENROLL.6.21 — Input bundle created state; C-ENROLL.6.22 — Provisional link proposed state; C-ENROLL.6.23 — Provisional link committed state; C-ENROLL.6.24 — Provisional profile created state; C-ENROLL.6.25 — Completed parent state; C-ENROLL.6.26 — Blocked parent state; C-ENROLL.6.27 — Failed parent state; C-ENROLL.6.28 — Separate session and parent lifecycles; C-ENROLL.6.29 — Legal transition and terminal rules

### C-ENROLL.6.1 — Requested process state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `requested` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — Ness's explicit begin recorded through the trusted-phone flow. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Enters the requested state on that recorded choice. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gives out: ACCEPTED — A requested enrollment process, no opened session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Must never: ACCEPTED — Treat a reservation as capture authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — A missing recorded begin cannot establish this state. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.3.1 — Durable explicit-begin event: the actual choice. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.2 — Initial prerequisites verified state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `prerequisites_verified_initial` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — A snapshot whose six owner facts all hold. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Records the successful initial check. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gives out: ACCEPTED — Initial verification before the BAI request. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Must never: ACCEPTED — Treat this state as a substitute for the later live recheck. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — An incomplete conjunction prevents the state and BAI request. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.2 — Six-owner prerequisite check: actual all-six truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.3 — Biometric pending process state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `biometric_pending` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — BAI's single pending record and active OS prompt. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Reflects that actual pending stage. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gives out: ACCEPTED — Pending authorization, no token or capture authority yet. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Must never: ACCEPTED — Create a shadow pending record in enrollment coordination. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]
- Fails closed by: ACCEPTED — A second pending request is refused; restart loses the volatile pending state. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-BAI.19.1 — Enrollment BAI request interface: actual pending status. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.4 — Token issued process state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `token_issued` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — BAI's single-use `voice_enrollment_ness` token. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Reflects BAI's actual issuance. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gives out: ACCEPTED — A token awaiting live recheck and consumption. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Must never: ACCEPTED — Open capture merely because issuance occurred. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — On restart no token survives and no session is opened. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-BAI.19 — Enrollment authorization producer: actual token issuance. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.5 — Prerequisites rechecked state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `prerequisites_rechecked` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — All six owners reread immediately before consumption. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Records the fresh check without promoting the old snapshot to authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Gives out: ACCEPTED — Current prerequisite facts for the consume-or-revoke decision. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Must never: ACCEPTED — Skip the reread after biometric prompting. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Any changed prerequisite revokes the unconsumed token and prevents opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.4.2 — Final owner recheck and revocation: the current check. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.6 — Token durably consumed state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `token_consumed_durably` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — Flushed `bai_token_consumed` and its verified integrity-protected binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Records actual durable consumption, independently of BAI's volatile memory. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Gives out: ACCEPTED — Spent proof, with session opening still a separate commit. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]
- Must never: ACCEPTED — Infer the opening from consumption alone. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]
- Fails closed by: ACCEPTED — Recovery without an opening aborts before capture and leaves the token spent. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]

TOGETHER
- Fed by: ACCEPTED — C-BAI.19.3 — Enrollment durable consumption proof: flushed owner truth; C-ENROLL.4.3 — Durable authorization chain and binding: verified binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.7 — Session opened process state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `session_opened` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — Committed `enrollment_session_opened`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Reflects a real session opened on BAI's durable proof. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gives out: ACCEPTED — Current opening truth for later capture checks. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Must never: ACCEPTED — Claim that opening proves microphone start. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Fails closed by: ACCEPTED — No committed opening means no session and no capture request. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.4.4 — Proof-bound session-open commit: actual opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.8 — Capture intent flushed state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `capture_intent_flushed` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — Durable `enrollment_capture_intent_event` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Records that coordination was about to request capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gives out: ACCEPTED — Intent truth preceding the physical request. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Must never: ACCEPTED — Claim a microphone start from this state. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Without a provable B29 outcome after this point, start remains unknown. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.5.2 — Durable capture intent: the flushed event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.9 — Capturing process state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `capturing` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — B29's `started` result while capture is running. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Reflects physical capture; BOP owns the observations produced. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gives out: ACCEPTED — Active capture state separate from recorded-segment truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Must never: ACCEPTED — Reconstruct an uncommitted segment from this state. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Fails closed by: ACCEPTED — Safety change or restart stops capture and prevents same-session resumption. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.5.4.1 — Confirmed capture start: B29's actual start result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.10 — Capture start unknown state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `capture_start_unknown` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — Durable intent without any provable B29 outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — States the unresolved physical-start reality honestly. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gives out: ACCEPTED — Unknown start and preserved actual observations. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Must never: ACCEPTED — Relabel unknown as never started. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — Closes or interrupts without automatically reopening the microphone. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.5.4.3 — Unknown capture-start reality: unresolved physical truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.11 — Closing process state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `closing` [proposed], one of the source's closing/closed labels. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — Capture stopping and the session-close boundary. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Uses the source's combined condition: capture stopped and `enrollment_session_closed` committed; no separate intermediate commit rule is specified. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gives out: ACCEPTED — The closing-stage label without an invented extra transition. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Must never: ACCEPTED — Submit roots while the session is still active. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Root submission waits for the committed close/interruption fact. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.8 — Closed-session root and reading handoff: actual stop and close truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.12 — Closed process state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `closed` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — Capture stopped and committed `enrollment_session_closed`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Ends the session while allowing the parent to continue through preserved material. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8A]
- Gives out: ACCEPTED — A terminal session and frozen actual observation references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Must never: ACCEPTED — Treat session closure as automatic parent completion. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8A]
- Fails closed by: ACCEPTED — No later capture silently reuses the closed session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.8 — Closed-session root and reading handoff: committed close. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.13 — Interrupted process state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `interrupted` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — A crash or owner safety change that ended the session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Ends capture honestly while retaining actual committed observations. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8A]
- Gives out: ACCEPTED — An interrupted session whose parent may continue with unaffected eligible material. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8A]
- Must never: ACCEPTED — Destroy valid observations or include safety-affected segments in the provisional profile. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — The old capture session never resumes automatically. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.7 — Mid-session protective stop: owner-triggered interruption. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.14 — Aborted before capture process state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]

ALONE
- What it is: ACCEPTED — `aborted_before_capture` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — Spent durable proof and no session-open commit. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]
- Does: ACCEPTED — Records an abort without asserting that any session existed. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]
- Gives out: ACCEPTED — `enrollment_aborted_before_capture` [proposed] and no capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]
- Must never: ACCEPTED — Interpret the source's session-outcome shorthand as a real opened session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]
- Fails closed by: ACCEPTED — Another attempt needs a new explicit begin and fresh token. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.4.6 — Spent proof without an opened session: the actual abort boundary. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.15 — Roots pending submission state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `roots_pending_submission` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — The closed session's frozen observation set. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Records that this immutable set awaits the standard Catalog path. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gives out: ACCEPTED — Pending root-entry work, not committed roots. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Must never: ACCEPTED — Add observations to the frozen set afterward. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — No Catalog acceptance means no root is claimed. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.8.1 — Frozen enrollment capture-set record: immutable actual references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.16 — Roots partially committed state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `roots_partially_committed` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — B11/append truth that some frozen observations have roots and some do not. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Tracks actual partial completion by verified `root_id`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — A resumable remaining set keyed by `capture_id`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Duplicate the already-committed roots. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — Unverified append results do not count as roots. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-BOP.13.1 — BOP consumption of B11 writer protections: actual append/fence outcomes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.17 — Roots committed state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `roots_committed` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — A verified `root_id` for every frozen observation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Records complete root commitment only from B11/append truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gives out: ACCEPTED — Verified roots ready for standard enqueue. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Must never: ACCEPTED — Infer a root from an enrollment checkpoint. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — Any unverified root outcome prevents the complete state. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-BOP.13.1 — BOP consumption of B11 writer protections: verified append outcomes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.18 — Readings pending state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `readings_pending` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — Verified roots enqueued through the standard reading path. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Records that the roots await reading. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gives out: ACCEPTED — Pending queue work without invented readings. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Must never: ACCEPTED — Treat enqueue as acceptance of a reading. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — Only the reading owner's committed outcomes count. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]

TOGETHER
- Fed by: DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): actual enqueue truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.19 — Readings partially completed state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `readings_partially_completed` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — The reading owner's actual partial outcomes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Keeps completed outcomes and resumes remaining queue work without duplicates. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — An honest partial reading set. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Must never: ACCEPTED — Invent missing or `insufficient_context` readings to force profile creation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — Rejected proposals are not counted as valid profile readings. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]

TOGETHER
- Fed by: DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): committed reading outcomes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.20 — Profile readiness pending state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `profile_readiness_pending` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — Eligible accepted readings whose readiness is not yet established. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Waits for the actual profile-integrity rule and verifiable counted set. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Gives out: ACCEPTED — Pending readiness, no link proposal or profile. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Must never: ACCEPTED — Invent a count, duration or confidence threshold. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — Unestablished readiness blocks both proposal and profile. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.10 — Profile readiness record: actual readiness evaluation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.21 — Input bundle created state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `profile_input_bundle_created` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — Established readiness and its immutable input reference bundle. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Does: ACCEPTED — Records coordination-only bundle existence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gives out: ACCEPTED — Exact frozen inputs for the link proposal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Must never: ACCEPTED — Claim that the bundle is a profile or adds identity evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Fails closed by: ACCEPTED — Without readiness, no bundle is created. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.10.5 — Immutable enrollment input bundle: the actual frozen set. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.22 — Provisional link proposed state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `provisional_link_proposed` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — `enrollment_provisional_link_proposed`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Records that enrollment proposed the association; the Person-Box owner decides its result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gives out: ACCEPTED — A proposal awaiting actual committed-link truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Must never: ACCEPTED — Treat acknowledgment as permission for profile creation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Pending, refused or unverified link truth blocks the profile handoff. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

TOGETHER
- Fed by: ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: the owner-returned proposal status. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.23 — Provisional link committed state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `provisional_link_committed` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — Current Person-Box-owned committed link truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Recognizes actual linkage before the SIA profile call. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Gives out: ACCEPTED — The required committed-link fact, not an identity conclusion. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Must never: ACCEPTED — Infer commitment from the coordinator's proposal record. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Refused, pending, stale, contradictory or unverifiable linkage blocks profile creation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

TOGETHER
- Fed by: ACCEPTED — C-7L.11.13.1 — Enrollment current committed-link result: actual owner truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.24 — Provisional profile created state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `provisional_profile_created` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — SIA's committed profile after committed linkage, then `enrollment_provisional_profile_created`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Records profile creation only in that order. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Gives out: ACCEPTED — A real provisional profile and the enrollment owner's post-commit event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Must never: ACCEPTED — Write the event merely because readiness was reached. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Fails closed by: ACCEPTED — No SIA commitment means no creation event or created state. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]

TOGETHER
- Fed by: ACCEPTED — C-SIA.20.7 — Profile-commit enrollment notification: actual commit before event emission. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.25 — Completed parent state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — `completed` [proposed], the successful parent-terminal result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — All four facts: Person-Box-owned committed link, SIA-owned committed profile, `enrollment_provisional_link_proposed` and `enrollment_provisional_profile_created`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Does: ACCEPTED — Completes the parent only with both owner commits and both enrollment events. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Gives out: ACCEPTED — One absorbing successful parent result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]
- Must never: ACCEPTED — Overwrite completion later or convert it into an automatic access grant. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15]
- Fails closed by: ACCEPTED — Missing any of the four facts prevents completion. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]

TOGETHER
- Fed by: ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: link commitment; C-SIA.20.7 — Profile-commit enrollment notification: profile commitment and event ordering. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.26 — Blocked parent state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `blocked` [proposed], a protective parent-terminal result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]
- Takes in: ACCEPTED — The actual owner's protective condition. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Records the block without overriding its owner. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gives out: ACCEPTED — An absorbing blocked result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]
- Must never: ACCEPTED — Overwrite the block with a later convenient success. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]
- Fails closed by: ACCEPTED — The protected continuation does not proceed. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.16 — Enrollment retry and failure boundary: the actual protective failure. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.27 — Failed parent state
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]

ALONE
- What it is: ACCEPTED — `failed` [proposed], terminal failure recorded honestly. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Takes in: ACCEPTED — The real terminal failure outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Terminates the parent without inventing successful continuation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]
- Gives out: ACCEPTED — One preserved failure result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]
- Must never: ACCEPTED — Replace a terminal result or regress committed historical facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]
- Fails closed by: ACCEPTED — Terminal work does not restart as the same successful operation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.16 — Enrollment retry and failure boundary: actual terminal failure. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.28 — Separate session and parent lifecycles
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]

ALONE
- What it is: ACCEPTED — The distinction between capture-session termination and whole-enrollment termination. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8A]
- Takes in: ACCEPTED — Normal closure, interruption or the spent-before-opening abort outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]
- Does: ACCEPTED — Lets a closed or interrupted session's parent continue through roots, readings, eligibility, readiness, link and profile using unaffected valid material; abort before opening asserts no session existed. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]
- Gives out: ACCEPTED — Honest session history alongside independently progressing parent work. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8A]
- Must never: ACCEPTED — Destroy valid committed material because capture was interrupted or reopen the interrupted microphone session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — Safety-affected segments cannot contribute to the provisional profile. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.7 — Mid-session protective stop: the stopped-session facts; C-ENROLL.4.6 — Spent proof without an opened session: the no-session abort. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.6.29 — Legal transition and terminal rules
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]

ALONE
- What it is: ACCEPTED — The lifecycle's transition invariants. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]
- Takes in: ACCEPTED — Current nonterminal state and the next owner's committed fact. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]
- Does: ACCEPTED — Permits only legal nonterminal transitions; preserves historical observations, roots, readings, eligibility decisions, links and profiles; allows at most one winning parent-terminal result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]
- Gives out: ACCEPTED — A monotone committed history and absorbing declared parent terminals. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]
- Must never: ACCEPTED — Overwrite completed, blocked, failed or any other declared parent-terminal result, confuse session and parent terminals, or enter a state by coordinator inference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]
- Fails closed by: ACCEPTED — A transition lacking its actual owner fact does not occur. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.6 — Enrollment process lifecycle: current process and owner facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.7 — Mid-session protective stop
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Immediate protective handling of the eight owner-event groups that can invalidate active capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — Trust loss/replacement/revocation, invalid recovery/setup, QR/secret contradiction, medium-or-higher spoofing, missing/contradictory Person-Box, BAI/session integrity failure, privacy exclusion or restart. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Stops new capture first, before logging; preserves only committed observations exactly; closes or interrupts honestly; prevents affected segments contributing to the profile; records the stop afterward. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — A stopped session and truthful preserved observation set. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Reconstruct missing audio, silently resume that session, or reuse/imitate TSC lifecycle, database or archive authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — A later capture needs an explicit begin, fresh prerequisite check, fresh token and new session identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: ACCEPTED — C-PAIR.5.2 — Pairing-owned enrollment safety events: actual trust/recovery/QR/setup changes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Fed by: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): spoofing changes; C-SACL — Speaker Access-Control Layer (§25.4): Gate 0 effect; C-7L — Person-Boxes (§7L): prerequisite changes; C-BAI — Biometric Authorization Interface (§25.6): security/session integrity events; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture exclusion. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): B29 stops physical capture on the protective request. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.5.3.7 — Capture cancellation and stop references | Current safety-stop conditions. | Carries cancellation/stop references to B29. | Old permission cannot override a new stop. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] |
| 2 · ACCEPTED | C-ENROLL.6.13 — Interrupted process state | The actual crash or safety change. | Records interrupted [proposed]. | Unaffected committed material may still proceed under the parent. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] |
| 3 · ACCEPTED | C-ENROLL.6.28 — Separate session and parent lifecycles | Stopped-session and affected-segment facts. | Separates session termination from parent continuation. | Only unaffected eligible material proceeds after interruption. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C] |
| 4 · ACCEPTED | C-9.2.8 — B29 enrollment capture interface | Only enrollment_operation_ref [proposed], enrollment_session_ref [proposed], current committed session-open reference, current privacy/capture-eligibility reference, enrollment provenance references (role/source_title/authorization_type), destination BOP context and current cancellation/stop references. | Supplies the protective physical-stop request. | Nothing in this card. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] |

SUB-PARTS: C-ENROLL.7.1 — Trusted-phone safety changes; C-ENROLL.7.2 — Invalid recovery or setup safety change; C-ENROLL.7.3 — Initial-material integrity contradiction; C-ENROLL.7.4 — Spoofing safety change; C-ENROLL.7.5 — Person-Box prerequisite safety change; C-ENROLL.7.6 — BAI or session integrity failure; C-ENROLL.7.7 — Privacy capture-exclusion safety change; C-ENROLL.7.8 — Application or machine restart safety change

### C-ENROLL.7.1 — Trusted-phone safety changes
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Trusted-phone loss, replacement or revocation during enrollment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — Actual BAI/pairing trust events. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Treats each named event as a trigger for immediate protective stop. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — No new capture under the invalidated old trust. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Re-decide phone trust inside the coordinator. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Stops before logging, excludes affected segments and does not resume the old session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: ACCEPTED — C-PAIR.5.2 — Pairing-owned enrollment safety events: loss, replacement and revocation truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.7.2 — Invalid recovery or setup safety change
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Recovery or owner-setup state becoming invalid. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — The pairing owner's changed recovery/setup facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Triggers the protective stop on either invalidity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — A stopped capture session with actual committed material retained. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Keep capturing on the initial snapshot. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Affected segments are excluded and a later attempt starts fresh. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: ACCEPTED — C-PAIR.5.2 — Pairing-owned enrollment safety events: actual invalidation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.7.3 — Initial-material integrity contradiction
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — A QR or temporary-secret integrity contradiction during capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — The pairing owner's contradiction event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Stops new capture immediately. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — Honest closure/interruption and preserved committed observations. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Resolve the contradiction in favor of continued enrollment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — No same-session resumption or affected-segment profile use. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: ACCEPTED — C-PAIR.5.2 — Pairing-owned enrollment safety events: the integrity contradiction. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.7.4 — Spoofing safety change
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — Medium-or-higher acoustic spoofing suspicion arising during enrollment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — SIA's assessment and SACL Gate 0 effect. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Stops capture before logging. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — An interrupted/closed session whose affected segments cannot train the provisional profile. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Lower the threshold or reinterpret the assessment inside coordination. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Fails closed by: ACCEPTED — Does not silently resume even if the old token was valid. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): actual suspicion; C-SACL — Speaker Access-Control Layer (§25.4): disqualifier effect. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.7.5 — Person-Box prerequisite safety change
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — The confirmed-box prerequisite becoming missing or contradictory. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — The Person-Box owner's current fact. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Stops capture and closes or interrupts honestly on either condition. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — Preserved actual observations without affected profile contribution. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Reconfirm Ness's box through enrollment coordination. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — New capture requires a fresh explicit enrollment attempt. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: DESIGNED — C-7L — Person-Boxes (§7L): the changed prerequisite truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.7.6 — BAI or session integrity failure
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — A BAI/session integrity failure during capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — The actual security owner's failure event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Stops new capture immediately, then records the failure. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Gives out: ACCEPTED — Honest interruption with only committed observations retained. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Must never: ACCEPTED — Restore authorization from coordination history. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Fails closed by: ACCEPTED — The same session does not silently resume. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: DESIGNED — C-BAI — Biometric Authorization Interface (§25.6): actual security integrity truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.7.7 — Privacy capture-exclusion safety change
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]

ALONE
- What it is: ACCEPTED — A current privacy capture exclusion. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — The actual privacy/B7 exclusion decision. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Does: ACCEPTED — Stops capture before logging and leaves protected-material handling to privacy authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]
- Gives out: ACCEPTED — No further excluded capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]
- Must never: ACCEPTED — Hand sensitive content to ordinary components merely to reject it. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — Exclusion prevents capture and affected-segment profile contribution. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): actual capture exclusion and protected handling. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.7.8 — Application or machine restart safety change
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Application or machine restart while a capture session was active. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]
- Takes in: ACCEPTED — Committed opening, intent/start records and actual BOP commits. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Closes the session as interrupted, retains actual observations and records start reality as unknown if no provable B29 outcome exists. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — A closed capture session whose parent may still process unaffected valid material. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8A]
- Must never: ACCEPTED — Automatically reopen the microphone, reconstruct audio or claim non-start from uncertainty. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — New capture requires a new begin, fresh checks, new pending record, fresh token and new session identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.5.4 — B29 capture-start result: whatever physical truth is provable; C-BOP.15.1 — B29 capture and BOP observation ownership: actual committed observations. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.15.20 — Recovery after restart of an active enrollment session | The actual active-session restart outcome. | Closes interrupted capture and preserves committed material. | Parent processing may continue, but new capture needs a new operation. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |

SUB-PARTS: NONE

### C-ENROLL.8 — Closed-session root and reading handoff
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]

ALONE
- What it is: ACCEPTED — The ten-step handoff from ended capture to ordinary preserved roots and quarantine readings. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Takes in: ACCEPTED — Committed observations and a committed session-close or interruption fact. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Does: ACCEPTED — Stops capture and commits closure; freezes actual references; submits each observation through Catalog; applies B11 global ingestion claim, root-ownership binding and append fence; preserves the sealed 5,521-root batch; uses only `append_root()`; carries `capture_id` end to end; records verified `root_id`; enqueues each committed root through the standard queue; keeps readings in quarantine. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Gives out: ACCEPTED — Preserved roots and ordinary queued readings, including roots of segments later rejected from profile training. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Must never: ACCEPTED — Ingest before session end, append to/reopen/alter the sealed batch, create a second staging/root/profile store or queue, or delete/hide/remove observations because their segment failed profile eligibility. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Privacy capture exclusion retains its own protective effect; failed Catalog acceptance or unverified append truth produces no claimed root. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-BOP.15.5 — Frozen enrollment capture set and normal entry: actual observation references and standard path; C-BOP.13.1 — BOP consumption of B11 writer protections: global claim, ownership and fence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Gated by: DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): ordinary intake acceptance; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture exclusion remains separate from profile rejection. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Changes: DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): committed roots enter its existing queue. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Changes: ACCEPTED — C-READ.11 — Quarantine-to-production promotion seam: enrollment readings remain quarantine unless separately promoted normally. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.6.11 — Closing process state | Actual stopped capture and closure truth. | Uses the source's combined closing/closed condition. | No extra intermediate commit mechanism is invented. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |
| 2 · ACCEPTED | C-ENROLL.6.12 — Closed process state | Committed ended-session truth. | Records closed [proposed]. | The parent may continue without reopening capture. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |
| 3 · ACCEPTED | C-ENROLL.8.1 — Frozen enrollment capture-set record | Committed close or interruption. | Freezes only actual observation references. | The capture set becomes immutable before submission. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |
| 4 · ACCEPTED | C-ENROLL.14.3 — Session closed enrollment event | The real ended-session fact. | Records enrollment_session_closed honestly. | Submission can follow only the actual close boundary. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |

SUB-PARTS: C-ENROLL.8.1 — Frozen enrollment capture-set record; C-ENROLL.8.2 — Catalog submission interface; C-ENROLL.8.3 — B11 append interface; C-ENROLL.8.4 — Root-identity reading enqueue

### C-ENROLL.8.1 — Frozen enrollment capture-set record
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — `enrollment_capture_set` [proposed], the immutable set of actual BOP observation references at close. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Takes in: ACCEPTED — Committed BOP observations under I6 and committed closure/interruption. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Freezes exactly those references once capture ends; BOP owns observation truth and coordination owns the freeze. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — `frozen capture_ids` for I7's standard Catalog request. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Add observations after freezing or reconstruct absent audio. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Recovery submits the same frozen set without adding or losing observations. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-BOP.15.1 — B29 capture and BOP observation ownership: committed physical truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: ACCEPTED — C-ENROLL.8 — Closed-session root and reading handoff: the close/interruption fact precedes the freeze and submission. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.6.15 — Roots pending submission state | The frozen actual observation set. | Records roots_pending_submission [proposed]. | Pending work is not claimed as committed roots. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-ENROLL.8.2 — Catalog submission interface | Frozen capture_ids. | Submits each under the standard Catalog path. | No reference is added during intake replay. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 3 · ACCEPTED | C-ENROLL.9.7 — Immutable enrollment segment identity | Actual segment observation references. | Keeps the immutable segment identity [proposed]. | Eligibility replay refers to the same segment. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |
| 4 · ACCEPTED | C-ENROLL.15.11 — Recovery after close before Catalog submission | The same frozen observation set. | Resumes ordinary Catalog submission. | Recovery adds and loses no observations. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |

SUB-PARTS: NONE

### C-ENROLL.8.2 — Catalog submission interface
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — I7, ended-session material entering the existing Catalog front door. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — `{ frozen capture_ids, provenance }` after committed close/interruption. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Submits each observation under its unchanged `capture_id` and declared enrollment provenance. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — Catalog-owned `accepted`, `rejected` or `blocked`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Interpret submission as acceptance or create another root-writing path. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: ACCEPTED — Failure is recorded with no root; privacy exclusion remains a pre-capture decision. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.8.1 — Frozen enrollment capture-set record: exact capture references; C-BOP.15.2 — Enrollment observation provenance: canonical declared provenance fields. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): owns accepted/rejected/blocked intake truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.8.3 — B11 append interface
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — I8, Catalog to the existing B11/`append_root()` route. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — `capture_id`-derived identity, validated root fields and B11-owned `ingest_operation_id`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Uses B11's active writable batch and fence with append idempotency; never touches the sealed batch. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — `root_id`, `append_duplicate_absorbed`, `rejected` or `indeterminate`, according to the actual append owner. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Infer root success from an enrollment checkpoint or write a duplicate root. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — An unverifiable result cannot count as commitment; recovery looks up the existing `root_id` by idempotency identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-BOP.13.1 — BOP consumption of B11 writer protections: the complete existing writer mechanism; C-STORE.4.6.2.1 — ingest_operation_id [proposed]: B11's operation identity; C-STORE.4.6.2.3 — capture_id: end-to-end duplicate identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: DESIGNED — C-STORE.3.5 — Atomic root append and identity idempotency: the sole append route and duplicate protection. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.8.4 — Root-identity reading enqueue | Verified root_id outcomes. | Enqueues each committed root idempotently. | Only actual roots enter the existing reading queue. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |
| 2 · ACCEPTED | C-ENROLL.15.12 — Recovery during partial root ingestion | Per-item verified append outcomes. | Resumes at the first capture_id without verified root_id. | Already committed roots are not duplicated. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |
| 3 · ACCEPTED | C-ENROLL.15.13 — Recovery after root append before checkpoint | The root owner's idempotency lookup result. | Recovers the existing root_id and writes the missing checkpoint once. | A missing checkpoint never causes a second root. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |

SUB-PARTS: NONE

### C-ENROLL.8.4 — Root-identity reading enqueue
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — I9, root commitment to the standard reading queue. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — `{ root_id }`, verified from the root owner. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Enqueues each committed root idempotently on root identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — `{ enqueued }`; resulting accepted readings remain in quarantine. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Must never: ACCEPTED — Create another queue, duplicate readings or promote directly to production. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Unverified root commitment does not authorize enqueue as a committed root. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.8.3 — B11 append interface: verified root identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): owns enqueue and reading outcomes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.15.14 — Recovery after roots before reading enqueue | Verified root identities and enqueue truth. | Enqueues missing roots idempotently. | No duplicate queue identity is created. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] |

SUB-PARTS: NONE

### C-ENROLL.9 — Initial-corpus eligibility gate
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — I10's six-check gate for contribution to the provisional profile. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Takes in: ACCEPTED — Reading references, root provenance and actual owner facts for each immutable segment identity [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Does: ACCEPTED — Requires one consistent live speaker stream, no medium-or-higher spoofing, no unresolved overlap, allowed completeness, declared authorization linked to durable consumption, and full-segment stream integrity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Gives out: ACCEPTED — Exactly one `enrollment_segment_accepted` or `enrollment_segment_rejected` outcome per segment, with reason and source references on rejection. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Must never: ACCEPTED — Infer who the speaker is from stream consistency, train on a failed segment, copy raw voice into decisions or delete its roots. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Any failed or unavailable owner fact rejects profile contribution; replay recovers the prior decision instead of creating competing membership results. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): spoofing/diarization facts; C-BOP — Behavioral Observation Processing (§25.1/§26): completeness and physical provenance; C-BAI — Biometric Authorization Interface (§25.6): durable token-consumption truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.9.8 — Per-segment eligibility decision record | The six-check result. | Records the segment's sole eligibility outcome. | Failed segments remain preserved but cannot train the profile. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |
| 2 · ACCEPTED | C-ENROLL.14.4 — Segment accepted enrollment event | All six eligibility checks passing. | Writes the sole accepted segment event. | Profile-input eligibility does not confirm identity. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] |

SUB-PARTS: C-ENROLL.9.1 — Consistent live-speaker stream check; C-ENROLL.9.2 — Segment spoofing check; C-ENROLL.9.3 — Overlapping-speaker contamination check; C-ENROLL.9.4 — Allowed observation-completeness check; C-ENROLL.9.5 — Declared authorization and durable-token check; C-ENROLL.9.6 — Full-segment stream-integrity check; C-ENROLL.9.7 — Immutable enrollment segment identity; C-ENROLL.9.8 — Per-segment eligibility decision record

### C-ENROLL.9.1 — Consistent live-speaker stream check
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Eligibility check 1: one consistent live speaker stream for the segment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Takes in: ACCEPTED — The segment's stream-consistency evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Does: ACCEPTED — Requires a single consistent live stream throughout the segment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Gives out: ACCEPTED — Stream eligibility without a named identity conclusion. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Must never: ACCEPTED — Claim that consistency identifies Ness. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — A segment failing this check cannot contribute to the provisional profile. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

TOGETHER
- Fed by: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): actual stream/diarization facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.9.2 — Segment spoofing check
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Eligibility check 2: no medium-or-higher acoustic spoofing suspicion during the segment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Takes in: ACCEPTED — SIA's segment-scoped spoofing assessment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Applies the stated suspicion boundary to that segment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Gives out: ACCEPTED — Spoofing-clean eligibility only when the condition holds. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Must never: ACCEPTED — Ignore suspicion because authorization or phone trust was valid. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Disqualifying or unavailable spoofing truth excludes profile contribution. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): the actual spoofing fact. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.9.3 — Overlapping-speaker contamination check
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Eligibility check 3: no unresolved overlapping-speaker contamination. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Takes in: ACCEPTED — The actual segment overlap assessment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Does: ACCEPTED — Requires overlap contamination to be absent or resolved. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Gives out: ACCEPTED — The overlap condition's result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Must never: ACCEPTED — Admit unresolved overlap as a clean single-speaker segment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Unresolved contamination rejects profile contribution. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

TOGETHER
- Fed by: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): owned speaker-stream assessment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.9.4 — Allowed observation-completeness check
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Eligibility check 4: the permitted `overall_completeness` values. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Takes in: ACCEPTED — BOP's actual completeness field. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Allows exactly `complete` or `partial`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Gives out: ACCEPTED — The completeness contribution to the six-way gate. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Must never: ACCEPTED — Treat another completeness label as eligible. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Any value outside the pair rejects the segment for profile use. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

TOGETHER
- Fed by: DESIGNED — C-BOP.6.4 — overall_completeness: canonical field and actual value. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.9.5 — Declared authorization and durable-token check
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Eligibility check 5, joining declared provenance to actual consumed-token evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Takes in: ACCEPTED — `authorization_type="enrollment_declared"` and the segment's `session_id`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Does: ACCEPTED — Requires that authorization value and a session link to confirmed durable `bai_token_consumed`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Gives out: ACCEPTED — Proven enrollment authorization provenance, without voice recognition. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Must never: ACCEPTED — Replace durable consumption with a biometric-success BOP observation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: ACCEPTED — Missing declaration or missing confirmed consumption link excludes the segment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

TOGETHER
- Fed by: DESIGNED — C-BOP.4.9.1.3 — enrollment_declared: canonical declared authorization meaning. [V10 §25.12]
- Gated by: ACCEPTED — C-BAI.19.3 — Enrollment durable consumption proof: actual durable consumption must be linked to the session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.9.6 — Full-segment stream-integrity check
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Eligibility check 6: all five full-segment stream-integrity conditions. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Takes in: ACCEPTED — Actual diarization confidence, transition, split/merge, second-speaker uncertainty and spoofing evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Does: ACCEPTED — Requires confidence above the bootstrap stream-stability threshold for the full segment; no unresolved transition; no material split/merge; no unresolved possible second speaker; no medium-or-higher spoofing. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Gives out: ACCEPTED — Evidence of one consistent live speaker, not evidence of who that speaker is. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Must never: ACCEPTED — Choose the unspecified threshold value or treat bootstrap consistency as an identity profile. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §25]
- Fails closed by: ACCEPTED — Failure of any condition rejects profile contribution. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

TOGETHER
- Fed by: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): actual diarization and spoofing facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: C-ENROLL.9.6.1 — Full-segment diarization-confidence condition; C-ENROLL.9.6.2 — Resolved speaker-transition condition; C-ENROLL.9.6.3 — No material stream split or merge condition; C-ENROLL.9.6.4 — No unresolved second-speaker uncertainty condition; C-ENROLL.9.6.5 — Stream spoofing-evidence condition

### C-ENROLL.9.6.1 — Full-segment diarization-confidence condition
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The bootstrap stream-stability confidence condition. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Takes in: ACCEPTED — Diarization confidence over the entire segment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Does: ACCEPTED — Requires it to remain above the bootstrap stream-stability threshold for the full segment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Gives out: ACCEPTED — A full-segment confidence result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Must never: ACCEPTED — Substitute an average, a partial interval or an invented numeric threshold. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §25]
- Fails closed by: ACCEPTED — Failure of the full-segment condition excludes profile use. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

TOGETHER
- Fed by: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): diarization facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.9.6.2 — Resolved speaker-transition condition
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The absence of an unresolved speaker-transition event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Takes in: ACCEPTED — Segment transition evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Does: ACCEPTED — Requires no unresolved transition. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Gives out: ACCEPTED — The transition condition's result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Must never: ACCEPTED — Ignore a transition still unresolved. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — An unresolved event rejects the segment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

TOGETHER
- Fed by: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): transition assessment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.9.6.3 — No material stream split or merge condition
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The no-material-split-or-merge condition. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Takes in: ACCEPTED — Segment stream split/merge facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Does: ACCEPTED — Requires both material split and material merge to be absent. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Gives out: ACCEPTED — The structural stream-continuity result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Must never: ACCEPTED — Treat a material split or merge as an uninterrupted single stream. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Either material change rejects profile contribution. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

TOGETHER
- Fed by: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): stream-structure facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.9.6.4 — No unresolved second-speaker uncertainty condition
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The condition excluding unresolved uncertainty that a second speaker entered. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Takes in: ACCEPTED — Actual second-speaker uncertainty. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Does: ACCEPTED — Requires that uncertainty to be absent or resolved. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Gives out: ACCEPTED — A bounded single-stream result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Must never: ACCEPTED — Treat uncertainty as confirmed absence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Unresolved possible entry rejects the segment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

TOGETHER
- Fed by: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): second-speaker assessment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.9.6.5 — Stream spoofing-evidence condition
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — No medium-or-higher spoofing evidence within the full-segment integrity check. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Takes in: ACCEPTED — Actual segment spoofing evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Does: ACCEPTED — Keeps the stated suspicion boundary within stream integrity as well as the separate spoofing check. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Gives out: ACCEPTED — The spoofing condition's integrity result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Must never: ACCEPTED — Infer named identity from passing this condition. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Medium-or-higher evidence rejects profile contribution. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

TOGETHER
- Fed by: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): actual spoofing facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.9.7 — Immutable enrollment segment identity
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — `enrollment_segment` [proposed], carrying the immutable segment identity [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Takes in: ACCEPTED — The particular captured segment's reference identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Does: ACCEPTED — Supplies the stable key for that segment's eligibility decision. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Gives out: ACCEPTED — One immutable segment reference, without audio payload. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Must never: ACCEPTED — Create competing membership results by changing identity on replay. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Replay recovers the recorded decision for that identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.8.1 — Frozen enrollment capture-set record: actual segment observation references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Gated by: ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.9.8 — Per-segment eligibility decision record | The immutable segment key. | Keys the eligibility-decision identity [proposed] to it. | Replay recovers the prior result without competition. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-ENROLL.9.8 — Per-segment eligibility decision record
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — `enrollment_eligibility_decision` [proposed], one record per immutable segment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Takes in: ACCEPTED — The six-check outcome and actual source references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Does: ACCEPTED — Mirrors the owned accepted/rejected enrollment event with a reason and references; the eligibility-decision identity [proposed] is keyed to the segment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Gives out: ACCEPTED — A recoverable prior membership result for replay. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Must never: ACCEPTED — Reevaluate replay into a competing result, add evidence weight or include raw voice payload. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Fails closed by: ACCEPTED — Failed eligibility excludes profile use while roots remain preserved. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.9 — Initial-corpus eligibility gate: actual outcome; C-ENROLL.9.7 — Immutable enrollment segment identity: stable decision key. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Gated by: ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.9.8.1 — Eligibility decision outcome | The owned accepted/rejected decision. | Mirrors it in the segment event outcome. | Profile membership stays stable on replay. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |
| 2 · ACCEPTED | C-ENROLL.9.8.2 — Eligibility decision reason | The actual rejection reason. | Records a structural explanation. | No raw voice or reconstructive failure description is exposed. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |
| 3 · ACCEPTED | C-ENROLL.9.8.3 — Eligibility source references | The actual supporting owner references. | Keeps reference-only provenance. | Recording the references adds no evidence weight. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |
| 4 · ACCEPTED | C-ENROLL.10 — Profile readiness record | Exact eligibility decisions for the readings. | Requires those references in the counted set. | Missing decisions prevent readiness. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] |
| 5 · ACCEPTED | C-ENROLL.10.2 — Per-reading eligibility reference | The actual segment decision identity. | Links each counted reading to its eligibility. | No reading lacking that evidence can establish readiness. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] |
| 6 · ACCEPTED | C-ENROLL.10.5.2 — Bundle eligibility-decision references | Actual eligibility-decision identities. | Freezes their references with the selected readings. | An excluded segment cannot become accepted through bundling. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] |
| 7 · ACCEPTED | C-ENROLL.14.5 — Segment rejected enrollment event | The actual rejected decision and evidence references. | Writes the rejected event with reason and no raw voice. | The segment stays preserved but excluded from training. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] |

SUB-PARTS: C-ENROLL.9.8.1 — Eligibility decision outcome; C-ENROLL.9.8.2 — Eligibility decision reason; C-ENROLL.9.8.3 — Eligibility source references

### C-ENROLL.9.8.1 — Eligibility decision outcome
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — The decision's per-segment accepted or rejected result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — The complete conjunction of six checks. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Does: ACCEPTED — Records exactly one outcome, mirrored by `enrollment_segment_accepted` or `enrollment_segment_rejected`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Gives out: ACCEPTED — Stable profile-membership eligibility. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Must never: ACCEPTED — Turn rejection into root deletion or hiding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — Rejected segments never train the provisional profile. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.9.8 — Per-segment eligibility decision record: the owned outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.9.8.2 — Eligibility decision reason
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — The eligibility record's reason, required for a rejected segment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Takes in: ACCEPTED — The actual failed check or owner fact. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Does: ACCEPTED — Records why profile use was refused. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Gives out: ACCEPTED — An inspectable structural explanation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Must never: ACCEPTED — Include raw voice or a reconstructive description in the failure record. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.9.8 — Per-segment eligibility decision record: the actual decision reason. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.9.8.3 — Eligibility source references
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — The source references carried with an eligibility decision. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Takes in: ACCEPTED — The actual owner evidence behind the segment outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Preserves traceability without copying payloads. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Gives out: ACCEPTED — Reference-only support for the decision. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Must never: ACCEPTED — Add evidence weight merely by recording the references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Fails closed by: ACCEPTED — An unavailable eligibility fact owner cannot be treated as successful evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.9.8 — Per-segment eligibility decision record: its actual source references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.10 — Profile readiness record
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — `enrollment_profile_readiness` [proposed], the bootstrap's sufficient-readings boundary. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Takes in: ACCEPTED — Eligible accepted quarantine readings, each linked to an eligibility decision, and the actual SIA/profile-integrity readiness rule. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Does: ACCEPTED — Records `counted_reading_refs` as a set keyed by reading identity, an eligibility-decision reference for each and the readiness outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Gives out: ACCEPTED — I11 `readiness` or `not-ready`; readiness permits only the immutable input bundle at this stage. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Count a reading twice, invent an `insufficient_context` reading, treat rejected proposals as accepted, build from raw audio/logs or substitute A29 general holding for enrollment readiness. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — Unavailable readiness rule, unverifiable counted set or missing eligibility decision prevents both link proposal and profile creation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.9.8 — Per-segment eligibility decision record: exact eligibility references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Gated by: ACCEPTED — C-SIA.20.1 — Eligible enrollment reading input: actual profile-integrity/SIA rule and values, with no chosen number, duration, score, confidence, calibration or acoustic algorithm here. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.6.20 — Profile readiness pending state | Eligible readings without established readiness. | Records profile_readiness_pending [proposed]. | No link or profile is created yet. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] |
| 2 · ACCEPTED | C-ENROLL.10.1 — Counted reading-reference set | Eligible accepted readings being counted. | Keys counted_reading_refs by reading identity. | A reading cannot be counted twice. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] |
| 3 · ACCEPTED | C-ENROLL.10.4 — Readiness failure classes | The actual failed readiness evaluation. | Distinguishes unavailable rule, unverifiable set and missing decision. | Each leaves linkage and profile creation blocked. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] |
| 4 · ACCEPTED | C-ENROLL.10.5 — Immutable enrollment input bundle | Established readiness. | Creates the one immutable coordination bundle. | No profile or new evidence is created at this stage. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] |

SUB-PARTS: C-ENROLL.10.1 — Counted reading-reference set; C-ENROLL.10.2 — Per-reading eligibility reference; C-ENROLL.10.3 — Readiness outcome; C-ENROLL.10.4 — Readiness failure classes; C-ENROLL.10.5 — Immutable enrollment input bundle

### C-ENROLL.10.1 — Counted reading-reference set
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — `counted_reading_refs`, a set keyed by reading identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Takes in: ACCEPTED — Exactly the eligible accepted readings counted for readiness. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Does: ACCEPTED — Keeps each reading identity once, making duplicate counting structurally impossible. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Gives out: ACCEPTED — The precise counted set and the readiness record's key. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Must never: ACCEPTED — Count a rejected proposal or a duplicated reference as another reading. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — An unverifiable counted set prevents readiness. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.10 — Profile readiness record: the eligible accepted set being assessed. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.10.5.1 — Bundle eligible-reading references | The exact counted eligible set. | Freezes its reading references in the bundle. | Proposal and build retain the same inputs. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] |

SUB-PARTS: NONE

### C-ENROLL.10.2 — Per-reading eligibility reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The eligibility-decision reference required for each counted reading. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Takes in: ACCEPTED — The recorded segment eligibility associated with that reading. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Does: ACCEPTED — Keeps every counted item traceable to its actual accepted eligibility. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Gives out: ACCEPTED — A per-reading decision reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Must never: ACCEPTED — Count an item lacking its eligibility evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — A missing decision reference prevents readiness, linkage proposal and profile creation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.9.8 — Per-segment eligibility decision record: actual decision identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.10.3 — Readiness outcome
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — The recorded readiness result under the actual profile-integrity rule. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Takes in: ACCEPTED — A verifiable eligible accepted reading set and the owner's readiness rule. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Does: ACCEPTED — Returns `readiness` or `not-ready` without choosing empirical values. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — Permission to create the input bundle only on established readiness. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Must never: ACCEPTED — Create a profile or profile-created event at this stage. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — Unestablished readiness permits neither link proposal nor profile creation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-SIA.20.1 — Eligible enrollment reading input: the real readiness rule and its values. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.10.5.5 — Bundle readiness reference | The established readiness result. | References that one outcome. | Replay recovers its same bundle. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] |

SUB-PARTS: NONE

### C-ENROLL.10.4 — Readiness failure classes
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]

ALONE
- What it is: ACCEPTED — The three explicitly named reasons readiness cannot be established. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Takes in: ACCEPTED — Unavailable rule, unverifiable counted set or a missing eligibility decision. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Does: ACCEPTED — Refuses to assert readiness on any one of them. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Gives out: ACCEPTED — No link proposal and no profile. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Must never: ACCEPTED — Fill the gap with a chosen sample count or fabricated reading. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Fails closed by: ACCEPTED — The readiness boundary remains closed until actual readiness can be established. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.10 — Profile readiness record: the actual failed readiness evaluation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.10.5 — Immutable enrollment input bundle
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]

ALONE
- What it is: ACCEPTED — `enrollment_profile_input_bundle` [proposed], one immutable coordination reference set per readiness outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Takes in: ACCEPTED — Only exact eligible accepted reading references, eligibility-decision references, operation/session references, prerequisite/authorization evidence and the readiness reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Does: ACCEPTED — Creates the bundle once readiness is established and freezes it; replay recovers the same bundle identity [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Gives out: ACCEPTED — Exact frozen inputs for the Person-Box proposal, before any SIA profile exists. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Must never: ACCEPTED — Become a profile, a separate store or added identity evidence, or reference an already-created profile as its input. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Fails closed by: ACCEPTED — Without readiness, no bundle; recovery never rebuilds a different input set for the same outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-ENROLL.10 — Profile readiness record: established readiness must precede bundle creation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Changes: ACCEPTED — C-7L.11.6 — Enrollment proposed input-bundle reference: receives the exact immutable bundle reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.6.21 — Input bundle created state | The existing immutable input bundle. | Records profile_input_bundle_created [proposed]. | Bundle existence adds no identity evidence. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] |
| 2 · ACCEPTED | C-ENROLL.11 — Provisional link and profile coordination | Exact immutable input references. | Proposes the provisional link before requesting a profile. | The proposal never points to an already-created profile. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |
| 3 · ACCEPTED | C-ENROLL.15.16 — Recovery after readiness before link proposal | The existing immutable bundle. | Recovers exactly that reference set. | No different input set or premature profile is created. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |

SUB-PARTS: C-ENROLL.10.5.1 — Bundle eligible-reading references; C-ENROLL.10.5.2 — Bundle eligibility-decision references; C-ENROLL.10.5.3 — Bundle operation and session references; C-ENROLL.10.5.4 — Bundle prerequisite and authorization evidence; C-ENROLL.10.5.5 — Bundle readiness reference

### C-ENROLL.10.5.1 — Bundle eligible-reading references
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The bundle's exact eligible accepted reading-reference set. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Takes in: ACCEPTED — The readings whose readiness was established. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Does: ACCEPTED — Freezes those references without payload copying. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Gives out: ACCEPTED — The identical reading set for proposal and later profile handoff. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Must never: ACCEPTED — Substitute a new set on replay. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.10.1 — Counted reading-reference set: the exact eligible set. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.10.5.2 — Bundle eligibility-decision references
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The bundle's exact eligibility-decision references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Takes in: ACCEPTED — Recorded decisions for the selected material. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Does: ACCEPTED — Freezes their identities with the reading inputs. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Gives out: ACCEPTED — Eligibility provenance for the proposal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Must never: ACCEPTED — Recast an excluded segment as accepted through bundling. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Fails closed by: ACCEPTED — Missing eligibility evidence prevents the preceding readiness result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.9.8 — Per-segment eligibility decision record: actual decision references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.10.5.3 — Bundle operation and session references
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The bundle's enrollment operation and session references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Takes in: ACCEPTED — The actual parent and collection-session identities. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Does: ACCEPTED — Keeps both identities attached to the frozen material. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Gives out: ACCEPTED — Operation/session provenance for the link proposal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Must never: ACCEPTED — Turn the identifiers into new authorization or identity evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.3.2 — Stable enrollment operation identity: parent; C-ENROLL.3.3 — Prospective enrollment session identity: the session identity made authoritative at opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.10.5.4 — Bundle prerequisite and authorization evidence
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The bundle's prerequisite and authorization evidence references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Takes in: ACCEPTED — Actual owner checks and bound durable consumption evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Does: ACCEPTED — Preserves that chain as references in the immutable bundle. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Gives out: ACCEPTED — Verifiable collection provenance for the proposal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Must never: ACCEPTED — Become the owner of the referenced facts or expose secrets. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §3] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Fails closed by: ACCEPTED — Unverifiable underlying authority cannot be replaced by the bundle. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.2.7 — Versioned prerequisite snapshot: owner check references; C-ENROLL.4.3 — Durable authorization chain and binding: actual bound proof. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.10.5.5 — Bundle readiness reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]

ALONE
- What it is: ACCEPTED — The bundle's readiness reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Takes in: ACCEPTED — The actual established readiness outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Does: ACCEPTED — Ties this one immutable bundle to that outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Gives out: ACCEPTED — A recoverable readiness-to-bundle identity relationship. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Must never: ACCEPTED — Rebuild a different bundle for replay of the same readiness. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — No established readiness means no bundle reference can be supplied as ready. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.10.3 — Readiness outcome: the established result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.11 — Provisional link and profile coordination
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — The I12-to-I13 handoff, with Person-Box linkage before SIA profile creation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Takes in: ACCEPTED — The immutable input bundle, confirmed Ness Person-Box, operation/session references, exact eligible reading set, eligibility decisions and prerequisite/authorization evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Does: ACCEPTED — Proposes `link_type="enrollment_material_provisional"`, `certainty=enrollment_provisional`, stable `provisional_link_proposal_id` [proposed], and the basis of confirmed `bai_token_consumed` for `voice_enrollment_ness`, owner-phone trust/`bai_initial_setup_finalized` and `authorization_type="enrollment_declared"`. The link states authorized collection, never confirmed voice identity. Waits for current owner-held commitment, then calls SIA with that link, linked readings, input bundle and build identity [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — I12 first returns `proposal recorded`, then committed link truth, refused or pending; I13 returns committed provisional profile or refusal. Only SIA commitment permits `enrollment_provisional_profile_created`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Approve/merge the link itself, proceed on proposal acknowledgment, reference an already-created profile as proposal input or invert the order. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Refused, pending, stale, contradictory or unverifiable linkage blocks profile creation; unavailable Person-Box or SIA authority blocks continuation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.10.5 — Immutable enrollment input bundle: frozen reference inputs; C-7L.11.1 — Enrollment provisional link type: exact type; C-7L.11.2 — Enrollment provisional link certainty: provisional certainty; C-7L.11.3 — Enrollment provisional link proposal ID: stable query identity; C-7L.11.4 — Enrollment provisional link meaning: collection provenance; C-7L.11.5 — Enrollment provisional link basis: actual authorization basis. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fed by: ACCEPTED — C-7L.11.6 — Enrollment proposed input-bundle reference: exact frozen input pointer; C-7L.11.7 — Enrollment confirmed Ness-box reference: confirmed destination; C-7L.11.8 — Enrollment link operation reference: parent; C-7L.11.9 — Enrollment link session reference: collection session; C-7L.11.10 — Enrollment link eligible-reading references: exact reading set; C-7L.11.11 — Enrollment link eligibility-decision references: decisions; C-7L.11.12 — Enrollment link prerequisite-evidence references: owner evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gated by: ACCEPTED — C-7L.11.13 — Enrollment committed-link handoff gate: current committed link required; C-SIA.20 — Provisional enrollment profile handoff: SIA owns actual profile creation under its rules. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.14.8 — Provisional link proposed enrollment event | The actual stable-ID link proposal. | Writes enrollment_provisional_link_proposed. | Proposal history remains distinct from committed linkage. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] |

SUB-PARTS: C-ENROLL.11.1 — Stable link-proposal recovery identity; C-ENROLL.11.2 — Provisional profile-build identity; C-ENROLL.11.3 — Provisional profile constraints consumed by enrollment

### C-ENROLL.11.1 — Stable link-proposal recovery identity
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — The enrollment use of `provisional_link_proposal_id` [proposed], one per operation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Takes in: ACCEPTED — The operation's exact frozen proposal inputs. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Does: ACCEPTED — Reuses the stable identity and queries the Person-Box owner after uncertainty. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — The actual proposal outcome and link state without duplication. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Generate another link from a replay or treat the proposal event as commitment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — No current committed link means no SIA handoff. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

TOGETHER
- Fed by: ACCEPTED — C-7L.11.3 — Enrollment provisional link proposal ID: canonical proposal identity; C-7L.11 — Provisional enrollment Person-Box link: actual query result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.15.16 — Recovery after readiness before link proposal | The stable proposal identity. | Proposes once after recovering the bundle. | Replay cannot create another link. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |

SUB-PARTS: NONE

### C-ENROLL.11.2 — Provisional profile-build identity
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — The provisional-profile build identity [proposed], one per enrollment operation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Takes in: ACCEPTED — The committed link and its exact linked reading set. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Does: ACCEPTED — Keys the build to those inputs and calls SIA idempotently. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Gives out: ACCEPTED — SIA's committed profile or refusal under the same build identity [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Create a duplicate profile, change the linked set on retry or build from logs/raw audio. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — Recovery obtains SIA's existing commit or retries the same build from the same linked set; no event precedes actual commitment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-SIA.20.2 — Provisional profile commit identity: idempotent actual profile result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: ACCEPTED — C-7L.11.13 — Enrollment committed-link handoff gate: current committed linkage before any build. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.15.18 — Recovery after link commit before profile creation | The same committed-link/reading-set build identity [proposed]. | Calls SIA idempotently. | No duplicate profile is created. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |

SUB-PARTS: NONE

### C-ENROLL.11.3 — Provisional profile constraints consumed by enrollment
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]

ALONE
- What it is: ACCEPTED — The SIA-owned profile and access constraints that enrollment preserves after linkage. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Takes in: ACCEPTED — SIA's committed provisional profile, with `profile_status="enrollment_provisional"`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Does: ACCEPTED — Keeps `recognized_ness` as the maximum while provisional regardless of acoustic score; behavioral, branch, session-continuity, timing and wording dimensions outweigh acoustic match until accepted transition to `enrollment_active`; subsequent material obeys ordinary training eligibility. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Gives out: ACCEPTED — Provisional evidence under SIA rules, with actual access decided only by SACL. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Must never: ACCEPTED — Grant recognized_ness automatically or invent the provisional-to-active rule or threshold. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — SIA restart returns identity to unknown and SACL to guest until a valid fresh assessment exists. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]

TOGETHER
- Fed by: ACCEPTED — C-SIA.20.3 — Provisional status and access ceiling: provisional maximum; C-SIA.20.4 — Provisional evidence weighting: the five stronger dimensions; C-SIA.20.5 — Provisional restart boundary: fresh assessment requirement. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Gated by: DESIGNED — C-SIA.11 — Ordinary voice-training eligibility: all later contributions obey ordinary conditions; C-SACL — Speaker Access-Control Layer (§25.4): its gates alone determine access. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.12 — Enrollment authority and privacy limits
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]

ALONE
- What it is: ACCEPTED — The continuing specialist-authority and raw-voice boundary of enrollment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15]
- Takes in: ACCEPTED — Enrollment provenance, references, provisional profile evidence and status/failure output. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]
- Does: ACCEPTED — Checks privacy before capture; retains raw voice inside the minimum necessary protected B29/BOP interface; carries only structural facts/references into coordination; routes every visible status or failure through final privacy-first, SACL-second delivery with current mode-fence revalidation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gives out: ACCEPTED — Bounded coordination and privacy/access-permitted output, without indirect disclosure. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15]
- Must never: ACCEPTED — By enrollment alone prove Ness's voice, grant recognized_ness automatically, exceed its provisional ceiling, grant top-security, create a BAI lease, open Personal Mode, make an observable channel private, replace PIN/fingerprint/SACL/PBR/other accepted factors, make voice a hard lockout or sole identity proof, authorize external actions or bypass B-INT-5/B-INT-6. Ordinary components receive no sensitive payload merely to reject it; logs/failure notices contain neither raw voice nor reconstructive descriptions. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]
- Fails closed by: ACCEPTED — Privacy exclusion follows its actual owner; unavailable or failing output gates prevent disclosure. An enrollment-purpose token cannot satisfy the Personal Mode opening purpose. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16] [04/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md §5B]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-SIA.20.8 — Enrollment authority limits: canonical profile authority constraints; C-BOP.15.6 — Protected raw-voice boundary: protected interface and no raw voice in coordination. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): first final output gate and capture protection; C-SACL — Speaker Access-Control Layer (§25.4): second final output gate; C-9 — Access/authentication model + voice I/O + phone modes (§9): current fence and separate mode-opening authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.13 — Enrollment coordination records and identities
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — The reference-only record family owned by the Enrollment Coordinator [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Takes in: ACCEPTED — Actual stage facts, identities, decisions, audit references and recovery outcomes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Does: ACCEPTED — Maintains one parent operational log with child stage, segment, ingest, reading, profile, link, retry and recovery records; all coordination records are append-only and add no evidence weight. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Gives out: ACCEPTED — The thirteen proposed record kinds: capture intent, input bundle, operation, stage event, begin claim, prerequisite snapshot, authorization binding, capture set, segment, eligibility decision, readiness, recovery event and duplicate-absorbed record. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Must never: ACCEPTED — Create competing parent truths, duplicate an accepted owner's record authority, store payloads in coordination, treat a log as evidence for itself or increase confidence through repetition. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Fails closed by: ACCEPTED — Owner contradictions block; required audit failures prevent reported success. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.1 — Enrollment coordination boundary: bounded record ownership. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected reference handling; C-SACL — Speaker Access-Control Layer (§25.4): applicable access limits on records. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: C-ENROLL.13.1 — Enrollment parent operation record; C-ENROLL.13.2 — Enrollment stage checkpoint; C-ENROLL.13.3 — Enrollment recovery operation and event; C-ENROLL.13.4 — Absorbed enrollment duplicate record

### C-ENROLL.13.1 — Enrollment parent operation record
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — `enrollment_operation` [proposed], the one parent, live-state until terminal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Takes in: ACCEPTED — Operation/session identities, process state, terminal reason and audit references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Does: ACCEPTED — Connects those fields to the one logical enrollment and its child records. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Gives out: ACCEPTED — Inspectable parent coordination history. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Must never: ACCEPTED — Become independent evidence or override actual owner truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Fails closed by: ACCEPTED — A declared terminal result is absorbing; at most one wins. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.3.2 — Stable enrollment operation identity: parent identity; C-ENROLL.3.3 — Prospective enrollment session identity: associated prospective/opened identity; C-ENROLL.6 — Enrollment process lifecycle: actual process state. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Gated by: ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.13.1.1 — Parent identity references | The parent's actual identities. | Carries the operation/session references. | The record identifies the correct enrollment. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |
| 2 · ACCEPTED | C-ENROLL.13.1.3 — Parent terminal reason | The real terminal outcome. | Records its structural reason. | Termination remains explainable without raw payloads. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] |
| 3 · ACCEPTED | C-ENROLL.13.2 — Enrollment stage checkpoint | The single parent association. | Records append-only child checkpoints. | Checkpoints remain history rather than owner truth. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] |

SUB-PARTS: C-ENROLL.13.1.1 — Parent identity references; C-ENROLL.13.1.2 — Parent process-state field; C-ENROLL.13.1.3 — Parent terminal reason; C-ENROLL.13.1.4 — Parent audit references

### C-ENROLL.13.1.1 — Parent identity references
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — The operation record's identities. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Takes in: ACCEPTED — Its stable parent identity and associated prospective or opened session identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Does: ACCEPTED — Preserves which enrollment the record describes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Gives out: ACCEPTED — Structural parent/session references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Must never: ACCEPTED — Convert a reserved identity into an opened session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.13.1 — Enrollment parent operation record: the identified parent record. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.13.1.2 — Parent process-state field
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — The operation record's process-state field. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Takes in: ACCEPTED — One of the source-defined process states [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Does: ACCEPTED — Records the state supported by actual owner facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]
- Gives out: ACCEPTED — Inspectable current or terminal parent state. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Must never: ACCEPTED — Enter a state by coordinator inference or overwrite a declared terminal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]
- Fails closed by: ACCEPTED — Missing owner truth prevents the claimed transition. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8B]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.6 — Enrollment process lifecycle: exact state vocabulary and entry facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.13.1.3 — Parent terminal reason
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — The operation record's terminal reason. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Takes in: ACCEPTED — The actual reason for the recorded terminal outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Does: ACCEPTED — Keeps termination explainable without raw payloads. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Gives out: ACCEPTED — A structural reason attached to the parent. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Must never: ACCEPTED — Include raw voice or reconstructive failure descriptions. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.13.1 — Enrollment parent operation record: the actual terminal result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.13.1.4 — Parent audit references
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — The operation record's audit references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Takes in: ACCEPTED — Actual enrollment and owner audit identities. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Does: ACCEPTED — Links the parent to the events that really occurred. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Gives out: ACCEPTED — Connected audit provenance, not copied authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Must never: ACCEPTED — Replace an unflushed required event with a reference assertion. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — Required audit write/flush failure prevents owner-reported success. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.14 — Enrollment audit-event ownership: actual event references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.13.2 — Enrollment stage checkpoint
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — `enrollment_stage_event` [proposed], an append-only child checkpoint. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Takes in: ACCEPTED — The actual stage's owner-returned outcome and references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Does: ACCEPTED — Records progress beneath the one parent. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Gives out: ACCEPTED — A child checkpoint without a competing parent truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Must never: ACCEPTED — Infer a missing root, reading, link or profile commit from the checkpoint. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — Owner contradiction blocks rather than rewriting owner truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.13.1 — Enrollment parent operation record: the parent association. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Gated by: ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.13.3 — Enrollment recovery operation and event
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — `enrollment_recovery_event` [proposed], with `enrollment_recovery_operation_id` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Takes in: ACCEPTED — The actual crash boundary and surviving committed owner facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Records recovery itself as one operation beneath the enrollment parent, naming the boundary. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Gives out: ACCEPTED — One traceable recovery operation, with the proper stop/resume outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Create competing parent truth or duplicate evidence through replay. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Fails closed by: ACCEPTED — Missing, stale, contradictory or unverifiable authority blocks the affected continuation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.15 — Enrollment crash recovery: the actual boundary and permitted action. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.13.3.1 — Recovery operation identity | One actual recovery operation. | Carries enrollment_recovery_operation_id [proposed]. | Recovery is identifiable without extra evidence weight. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] |

SUB-PARTS: C-ENROLL.13.3.1 — Recovery operation identity; C-ENROLL.13.3.2 — Recovery crash-boundary reference

### C-ENROLL.13.3.1 — Recovery operation identity
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]

ALONE
- What it is: ACCEPTED — `enrollment_recovery_operation_id` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Takes in: ACCEPTED — One real recovery operation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Does: ACCEPTED — Makes recovery individually identifiable while preserving its enrollment-parent relationship. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Gives out: ACCEPTED — A recovery identity with no extra evidence weight. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Must never: ACCEPTED — Count another record of the same recovery as independent support. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.13.3 — Enrollment recovery operation and event: the actual recovery. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.13.3.2 — Recovery crash-boundary reference
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — The named crash boundary in the recovery event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Takes in: ACCEPTED — The actual interruption point and committed truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Identifies which source-defined recovery case applies. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — An inspectable reason for the recovery action. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Must never: ACCEPTED — Collapse unknown capture start into confirmed non-start. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — Unverifiable authority remains blocked rather than inferred. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.15 — Enrollment crash recovery: the applicable actual boundary. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.13.4 — Absorbed enrollment duplicate record
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]

ALONE
- What it is: ACCEPTED — `enrollment_duplicate_absorbed` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Takes in: ACCEPTED — A replay recognized by the relevant stable identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Does: ACCEPTED — Records that the replay was absorbed. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Gives out: ACCEPTED — Duplicate-handling history without another operation result or evidence vote. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Must never: ACCEPTED — Increase identity confidence through repetition. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Fails closed by: ACCEPTED — Replay recovers existing outcomes rather than creating duplicate roots, readings, link proposals or profiles. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.15 — Enrollment crash recovery: actual idempotency/replay outcomes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.14 — Enrollment audit-event ownership
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — The nine settled enrollment-owned events and their separate proposed coordination additions. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Takes in: ACCEPTED — Actual prerequisite, opening, closure, segment, revocation, proposal and profile outcomes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Does: ACCEPTED — Owns `enrollment_prerequisites_verified`, `enrollment_session_opened`, `enrollment_session_closed`, `enrollment_segment_accepted`, `enrollment_segment_rejected`, `enrollment_prerequisite_failed`, `enrollment_token_revoked_prereq_changed`, `enrollment_provisional_link_proposed` and `enrollment_provisional_profile_created`; writes and flushes required events before reporting owner success. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Gives out: ACCEPTED — Enrollment event history, alongside the distinct `enrollment_aborted_before_capture` [proposed], `enrollment_capture_intent_event` [proposed] and B29-sourced `enrollment_capture_started` [proposed interface fact]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Must never: ACCEPTED — Rename existing events, call the combined catalog exactly nine, treat proposed additions as settled vocabulary or take over BAI's `bai_token_consumed`/`bai_token_revoked`. BOP, Catalog, B11, reading, Person-Box, SIA, SACL, privacy and security-audit owners retain their records. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — A required event that cannot be written and flushed prevents reported success; unknown is never success. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.4.6 — Spent proof without an opened session: proposed abort outcome; C-ENROLL.5.2 — Durable capture intent: proposed intent; C-ENROLL.5.5 — B29-sourced capture-start fact: proposed physical-start reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.13.1.4 — Parent audit references | Actual audit event identities. | Links the parent to events that really occurred. | References cannot substitute for missing durable events. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18] |
| 2 · ACCEPTED | C-ENROLL.16.3 — Required-audit durability failure | The actual required audit event and durability failure. | Withholds owner-reported success. | Unflushed history cannot be claimed as a successful result. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18] |

SUB-PARTS: C-ENROLL.14.1 — Prerequisites verified enrollment event; C-ENROLL.14.2 — Session opened enrollment event; C-ENROLL.14.3 — Session closed enrollment event; C-ENROLL.14.4 — Segment accepted enrollment event; C-ENROLL.14.5 — Segment rejected enrollment event; C-ENROLL.14.6 — Prerequisite failed enrollment event; C-ENROLL.14.7 — Prerequisite-change token-revocation enrollment event; C-ENROLL.14.8 — Provisional link proposed enrollment event; C-ENROLL.14.9 — Provisional profile created enrollment event

### C-ENROLL.14.1 — Prerequisites verified enrollment event
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — `enrollment_prerequisites_verified`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Takes in: ACCEPTED — An actual six-owner check with all six satisfied. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Records that verification without owning the checked facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gives out: ACCEPTED — The enrollment-owned verification audit fact. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Must never: ACCEPTED — Substitute the event for a later live recheck. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — A failed prerequisite cannot produce verified success. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.2 — Six-owner prerequisite check: actual conjunction. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.14.2 — Session opened enrollment event
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — `enrollment_session_opened`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Takes in: ACCEPTED — Verified flushed consumption proof and its operation/session binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A]
- Does: ACCEPTED — Commits the actual opening after that proof. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Gives out: ACCEPTED — Opening truth for capture and biometric-observation timing. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Describe a merely reserved session as open. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17]
- Fails closed by: ACCEPTED — Missing verified durable proof prevents the event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.4.4 — Proof-bound session-open commit: the actual opening operation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.14.3 — Session closed enrollment event
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — `enrollment_session_closed`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Takes in: ACCEPTED — A session that actually opened and has stopped or been interrupted. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Does: ACCEPTED — Records honest closure, including zero segments only when capture is confirmed not to have begun. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Gives out: ACCEPTED — Close truth preceding frozen-set submission. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Must never: ACCEPTED — Use this event for consumption without an opening or use it to imply unknown capture never began. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Fails closed by: ACCEPTED — Root entry waits for committed closure/interruption. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.8 — Closed-session root and reading handoff: actual ended-session fact. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.14.4 — Segment accepted enrollment event
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — `enrollment_segment_accepted`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Takes in: ACCEPTED — An immutable segment whose six eligibility checks all pass. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Does: ACCEPTED — Records that segment's sole accepted eligibility outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Gives out: ACCEPTED — Profile-input eligibility, not recognized identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Must never: ACCEPTED — Create a second competing membership event on replay. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Any failed check prevents acceptance. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.9 — Initial-corpus eligibility gate: actual accepted outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.14.5 — Segment rejected enrollment event
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — `enrollment_segment_rejected`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Takes in: ACCEPTED — A failed eligibility result for the immutable segment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Does: ACCEPTED — Records the reason and source references without raw voice. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]
- Gives out: ACCEPTED — A retained rejection that excludes profile contribution while preserving roots. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Must never: ACCEPTED — Delete or hide the observation because of profile rejection. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]
- Fails closed by: ACCEPTED — The rejected segment cannot train the provisional profile. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.9.8 — Per-segment eligibility decision record: actual rejection and references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.14.6 — Prerequisite failed enrollment event
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — `enrollment_prerequisite_failed`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Takes in: ACCEPTED — The actual failed prerequisite by owner reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Does: ACCEPTED — Records failure without private prerequisite payloads. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Gives out: ACCEPTED — A failed-check fact; initial failure prevents the BAI call. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Use a previous passing snapshot to override the failure. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Failure before consumption prevents session opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.2 — Six-owner prerequisite check: failed initial check; C-ENROLL.4.2 — Final owner recheck and revocation: changed final check. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.14.7 — Prerequisite-change token-revocation enrollment event
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — `enrollment_token_revoked_prereq_changed`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Takes in: ACCEPTED — A changed prerequisite and BAI's actual revocation of the issued unconsumed token. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Does: ACCEPTED — Records the enrollment consequence while BAI separately owns `bai_token_revoked`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Gives out: ACCEPTED — Changed-prerequisite revocation history with no consumption. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Must never: ACCEPTED — Fabricate BAI revocation or continue to opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — The revoked token cannot open the session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.4.2 — Final owner recheck and revocation: actual change and BAI outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.14.8 — Provisional link proposed enrollment event
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — `enrollment_provisional_link_proposed`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Takes in: ACCEPTED — The actual stable-ID proposal and exact frozen input references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Does: ACCEPTED — Records that enrollment proposed the provisional association. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gives out: ACCEPTED — Proposal history, one of the two enrollment events required for parent completion. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Must never: ACCEPTED — Assert committed linkage from proposal or acknowledgment alone. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — SIA still waits for current Person-Box-owned committed truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.11 — Provisional link and profile coordination: actual proposal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.14.9 — Provisional profile created enrollment event
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]

ALONE
- What it is: ACCEPTED — `enrollment_provisional_profile_created`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Takes in: ACCEPTED — SIA's actual committed provisional profile after committed linkage. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Does: ACCEPTED — Writes the enrollment event only after SIA commits. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Gives out: ACCEPTED — Creation history and the second enrollment event required for completion. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Must never: ACCEPTED — Emit merely on readiness, bundle creation, proposal existence or acknowledgment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — No SIA commitment means no profile-created event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-SIA.20.7 — Profile-commit enrollment notification: actual commitment must precede this event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.15 — Enrollment crash recovery
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Recovery at all twenty-one source-table boundaries: rows 1–20 and the inserted row 7b. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — The real interruption point and authoritative committed owner facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Recovers only the permitted continuation, under stable identities, while preserving actual observations and later commitments. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — Honest stopped capture and, where allowed, resumed reference-based processing of existing material. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Reconstruct missing audio, replay old microphone capture, create duplicate roots/readings/profiles/link proposals, infer success from coordination or reopen the microphone automatically. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — Missing, stale, contradictory or unverifiable authority blocks the affected continuation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-BOP.15.1 — B29 capture and BOP observation ownership: real observation commits; C-BOP.13.1 — BOP consumption of B11 writer protections: root commitments; C-7L.11 — Provisional enrollment Person-Box link: actual link truth; C-SIA.20.2 — Provisional profile commit identity: actual profile truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.13.3 — Enrollment recovery operation and event | The actual crash boundary and permitted recovery. | Records recovery as one operation. | Its history stays linked to the enrollment parent. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |
| 2 · ACCEPTED | C-ENROLL.13.3.2 — Recovery crash-boundary reference | The applicable interruption point. | Names the crash boundary in the recovery event. | The permitted recovery action is traceable. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |
| 3 · ACCEPTED | C-ENROLL.13.4 — Absorbed enrollment duplicate record | Actual absorbed replays. | Records duplicate handling. | No duplicate result or independent evidence vote is added. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |
| 4 · ACCEPTED | C-ENROLL.16 — Enrollment retry and failure boundary | Stage-specific committed truth and recovery limits. | Determines whether technical continuation is permitted. | Retry never recreates security authority. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] |

SUB-PARTS: C-ENROLL.15.1 — Recovery before the prerequisite snapshot; C-ENROLL.15.2 — Recovery after initial checks before BAI; C-ENROLL.15.3 — Recovery with BAI pending; C-ENROLL.15.4 — Recovery after token issue before final checks; C-ENROLL.15.5 — Recovery after failed prerequisites or revocation; C-ENROLL.15.6 — Recovery after consumption before opening; C-ENROLL.15.7 — Recovery before the biometric system-command observation; C-ENROLL.15.8 — Recovery after intent without a provable start result; C-ENROLL.15.9 — Recovery during confirmed capture; C-ENROLL.15.10 — Recovery after observations before close; C-ENROLL.15.11 — Recovery after close before Catalog submission; C-ENROLL.15.12 — Recovery during partial root ingestion; C-ENROLL.15.13 — Recovery after root append before checkpoint; C-ENROLL.15.14 — Recovery after roots before reading enqueue; C-ENROLL.15.15 — Recovery during partial reading completion; C-ENROLL.15.16 — Recovery after readiness before link proposal; C-ENROLL.15.17 — Recovery after link-proposal submission; C-ENROLL.15.18 — Recovery after link commit before profile creation; C-ENROLL.15.19 — Recovery during SIA profile creation; C-ENROLL.15.20 — Recovery after restart of an active enrollment session; C-ENROLL.15.21 — Recovery from coordinator-owner contradiction

### C-ENROLL.15.1 — Recovery before the prerequisite snapshot
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Crash-table row 1, before the prerequisite snapshot. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — Only the durable begin event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Stays idle. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — No session and no BAI call. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Infer checked prerequisites from the begin event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — A later attempt requires a new begin. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.3.1 — Durable explicit-begin event: the sole surviving fact. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.15.2 — Recovery after initial checks before BAI
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Row 2, after initial prerequisites but before the BAI request. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — The recorded snapshot. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Fails the operation; the snapshot proves a check occurred, not current authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — A failed operation without a session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Authorize on the old snapshot after restart. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — A new attempt rereads the actual owners. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.2.7 — Versioned prerequisite snapshot: historical check evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.15.3 — Recovery with BAI pending
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Row 3, a crash while BAI holds pending state. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — The fact that the pending record was in memory only. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Preserves no live pending authorization across restart. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — No surviving token or session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Reconstruct the pending record as live authority from logs. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — Requires new begin, new pending record and fresh token. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-BAI.19.1 — Enrollment BAI request interface: BAI's volatile pending boundary. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.15.4 — Recovery after token issue before final checks
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Row 4, token creation before the final prerequisite check. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — No durable token authority; BAI's in-memory token is gone. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Leaves no session open. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — A stopped attempt without recovered token authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Reuse historical issuance as a current token. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — A new begin is required. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-BAI.19 — Enrollment authorization producer: volatile token ownership. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.15.5 — Recovery after failed prerequisites or revocation
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Row 5, after prerequisite failure or token revocation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — `enrollment_prerequisite_failed`, `enrollment_token_revoked_prereq_changed` and BAI's `bai_token_revoked` as applicable. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Retains the terminal outcome honestly. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — No session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Turn a terminal failure into a delayed opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — Another attempt is a new operation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.4.2 — Final owner recheck and revocation: actual failed/revoked result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.15.6 — Recovery after consumption before opening
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Row 6, durable consumption without the session-open commit. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — Flushed `bai_token_consumed` and its integrity-protected binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Leaves the token spent and records `enrollment_aborted_before_capture` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — No session opening and no capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Forward-complete the missing opening. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]
- Fails closed by: ACCEPTED — A new begin and fresh token are required. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.4.6 — Spent proof without an opened session: the exact no-session outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.15.7 — Recovery before the biometric system-command observation
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

ALONE
- What it is: ACCEPTED — Row 7, opening committed before the biometric observation was staged. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — Actual `enrollment_session_opened` truth referencing durable BAI proof. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Does: ACCEPTED — Coordinates BAI's one `biometric:result:success` observation under its deterministic capture identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — One BAI-sourced physical fact, never a duplicate. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Fabricate the observation or make the coordinator its source. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Fails closed by: ACCEPTED — Capture still requires a current valid opening and its separate current preconditions; the recovery observation never reopens the microphone. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-BAI.19.6 — BAI-owned enrollment success observation: sole source; C-BOP.15.4 — Single enrollment biometric success observation: deterministic receiver identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.15.8 — Recovery after intent without a provable start result
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Row 7b, durable intent before a provable B29 outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — `enrollment_capture_intent_event` [proposed], proving only about-to-request intent. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Records unknown start reality, preserves any actual BOP commits and closes or interrupts honestly. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — Unknown physical start with preserved observation truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Claim capture never began. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — Does not reopen the microphone. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.5.4.3 — Unknown capture-start reality: the correct unresolved outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.15.9 — Recovery during confirmed capture
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Row 8, crash during capture after B29 reported `started`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — Whatever BOP actually committed. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Stops, preserves those observations exactly and records the gap through BOP failure/interruption roots. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — A truthful interrupted capture history. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Reconstruct the missing interval or resume the same session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — The microphone is not reopened. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-BOP.15.1 — B29 capture and BOP observation ownership: actual durable observations and failure truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.15.10 — Recovery after observations before close
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Row 9, observations committed before session closure. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — The actual committed observation set. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Closes as `interrupted` [proposed] and freezes that set. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — Valid observations with which the parent may continue. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Invent observations to fill the gap. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — Interrupted capture stays ended; only unaffected eligible material may reach the profile. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8A]

TOGETHER
- Fed by: ACCEPTED — C-BOP.15.1 — B29 capture and BOP observation ownership: committed observations. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.15.11 — Recovery after close before Catalog submission
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Row 10, session closed before Catalog submission. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — Committed closure and the frozen capture-reference set. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Resumes standard submission from that same immutable set. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — Remaining ordinary ingestion work. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Add or lose observations during recovery. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — Catalog still decides acceptance; recovery supplies no bypass. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.8.1 — Frozen enrollment capture-set record: immutable references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): standard intake rules. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.15.12 — Recovery during partial root ingestion
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Row 11, partial Catalog/B11 ingestion. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — Per-item Catalog and B11 commitments. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Resumes at the first `capture_id` without a verified `root_id`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — Only remaining unverified root-entry work. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Append a second root for an already committed observation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — Uses append idempotency and never counts an unverified result as a root. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.8.3 — B11 append interface: per-item owner outcomes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.15.13 — Recovery after root append before checkpoint
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Row 12, root exists but its enrollment checkpoint is missing. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — Actual root-store commitment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Looks up the existing `root_id` by idempotency identity and writes the missing checkpoint exactly once. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — Recovered root reference and checkpoint. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Append a replacement root because coordination missed its checkpoint. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — Unverifiable root truth cannot be replaced by a checkpoint assertion. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.8.3 — B11 append interface: root-owner lookup truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.15.14 — Recovery after roots before reading enqueue
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Row 13, committed roots not yet enqueued. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — Verified `root_id` values. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Enqueues only the missing roots under root-identity idempotency. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — Standard queue entries. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Duplicate work under new identities. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — Only verified committed roots enter this recovery step. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.8.4 — Root-identity reading enqueue: canonical enqueue identity and outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.15.15 — Recovery during partial reading completion
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Row 14, some reading outcomes committed and others unfinished. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — The reading owner's actual committed outcomes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Resumes the existing queue. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — Continued ordinary reading work with earlier outcomes retained. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Duplicate or invent a reading. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — Rejected proposals remain rejected and cannot silently become profile input. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12]

TOGETHER
- Fed by: DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): actual queue/read outcomes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.15.16 — Recovery after readiness before link proposal
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Row 15, readiness and input bundle exist before proposal. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — The readiness record and immutable `enrollment_profile_input_bundle` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Recovers the same bundle and proposes once under the stable `provisional_link_proposal_id` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — One proposal from unchanged input references. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Rebuild different inputs or claim a profile already exists. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — No profile is created before actual committed linkage. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.10.5 — Immutable enrollment input bundle: the same frozen set; C-ENROLL.11.1 — Stable link-proposal recovery identity: the one proposal key. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.15.17 — Recovery after link-proposal submission
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Row 16, after the provisional link proposal was submitted. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — `enrollment_provisional_link_proposed` and the stable `provisional_link_proposal_id` [proposed]. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Queries the Person-Box owner using that identity and absorbs replay. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — The actual owner-held proposal/link result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Create a duplicate link or infer commitment from submission. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — Noncommitted or unverifiable linkage still blocks SIA creation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]

TOGETHER
- Fed by: ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: owns the queried outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.15.18 — Recovery after link commit before profile creation
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Row 17, committed Person-Box link before the SIA build. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — The actual committed link and its linked reading set. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Recovers the link and calls SIA idempotently using the same build identity [proposed] and linked set. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — SIA's actual profile result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Must never: ACCEPTED — Create another profile under a new build identity [proposed] for this operation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — A link that is no longer current or verifiable cannot authorize the handoff. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.11.2 — Provisional profile-build identity: the same idempotent build. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: ACCEPTED — C-7L.11.13 — Enrollment committed-link handoff gate: current committed truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.15.19 — Recovery during SIA profile creation
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Row 18, interruption during the SIA-owned provisional-profile build. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — Whatever SIA actually committed. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Recovers an existing committed profile or retries the same build identity [proposed] from the same linked readings; writes the enrollment creation event only after commitment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — One actual profile result and correctly ordered event history. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Build from logs or raw audio, or fabricate a committed profile. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — Without SIA commitment, no `enrollment_provisional_profile_created`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-SIA.20.2 — Provisional profile commit identity: actual recoverable SIA result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.15.20 — Recovery after restart of an active enrollment session
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Row 19, restart while the enrollment session was active. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — Committed observations, opening, intent and any provable B29 result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Closes as `interrupted` [proposed], preserves committed observations exactly and retains unknown start if B29 truth is not provable; the parent may continue through roots, readings, eligibility, readiness, link and profile. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — An ended capture session and separately recoverable parent work. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Reopen the microphone or relabel unknown as never started. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — New capture requires a new explicit operation: new begin, fresh prerequisites, new pending, fresh token and new session identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.7.8 — Application or machine restart safety change: actual restart outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.15.21 — Recovery from coordinator-owner contradiction
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]

ALONE
- What it is: ACCEPTED — Row 20, an enrollment record contradicts its actual owner. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Takes in: ACCEPTED — The conflicting coordination record and the owner's record. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Does: ACCEPTED — Uses the owner's record as truth and records the contradiction. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gives out: ACCEPTED — A blocked continuation with an honest contradiction record. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Must never: ACCEPTED — Resolve the conflict in the coordinator's favor. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Fails closed by: ACCEPTED — Blocks the affected continuation; unknown is never success. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.1 — Enrollment coordination boundary: the limited standing of coordination evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §3] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.16 — Enrollment retry and failure boundary
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

ALONE
- What it is: ACCEPTED — Technical retry and fail-closed handling that preserve the actual authorization boundary. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Takes in: ACCEPTED — Accepted B9 retry classifications/values by reference and the actual stage failure. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Does: ACCEPTED — Reuses the stable parent only for technical work needing neither fresh explicit action nor recreated security authority, such as resubmitting a frozen observation after a transient failure. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Gives out: ACCEPTED — A permitted same-parent technical retry or a stopped/blocked/closed outcome requiring a fresh enrollment attempt. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]
- Must never: ACCEPTED — Reuse expired/revoked/consumed tokens, stale prerequisites, prior biometric results, an old active microphone session, stale SIA/SACL state or failed/interrupted capture as continuing. No retry count, timeout, backoff, duration or sample target is invented. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Fails closed by: ACCEPTED — Stops, blocks or closes honestly for each named failure: bad prerequisite; existing BAI pending; unmatched biometric result; unflushed/unverified consumption; unverifiable binding; changed prerequisite; absent/noncurrent opening; unsafe BOP capture; privacy exclusion; no Catalog acceptance; unverified append result; unavailable eligibility owner; unestablished readiness; unavailable Person-Box or SIA; owner contradiction; required audit write/flush failure. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.15 — Enrollment crash recovery: exact stage-specific stop/resume outcomes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENROLL.6.26 — Blocked parent state | An actual protective condition. | Records blocked [proposed] as a parent terminal. | The block cannot be overwritten by convenient later success. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23] |
| 2 · ACCEPTED | C-ENROLL.6.27 — Failed parent state | The actual terminal failure. | Records failed [proposed]. | The failed parent remains terminal. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23] |
| 3 · ACCEPTED | C-ENROLL.16.1 — Same-parent technical retry conditions | The actual retry class and stage. | Requires no fresh explicit action and no recreated authority. | Only bounded technical work can reuse the parent. | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22] |

SUB-PARTS: C-ENROLL.16.1 — Same-parent technical retry conditions; C-ENROLL.16.2 — Fresh enrollment-session requirements; C-ENROLL.16.3 — Required-audit durability failure

### C-ENROLL.16.1 — Same-parent technical retry conditions
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]

ALONE
- What it is: ACCEPTED — The conjunction permitting reuse of a stable parent for technical retry. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Takes in: ACCEPTED — A technical failure whose retry needs no fresh explicit Ness action and recreates no security authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Does: ACCEPTED — Uses the accepted B9 classification and values for the existing operation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Gives out: ACCEPTED — A bounded technical continuation, such as frozen-set resubmission. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Must never: ACCEPTED — Use retry to restore an expired authorization or resume ended microphone capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Fails closed by: ACCEPTED — If either condition is absent, the same-parent retry cannot recreate authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.16 — Enrollment retry and failure boundary: the actual retry class and stage. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.16.2 — Fresh enrollment-session requirements
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]

ALONE
- What it is: ACCEPTED — The five requirements for every new enrollment session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Takes in: ACCEPTED — A new explicit begin, fresh prerequisite checks, a new BAI pending record, a fresh token and a new session identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Does: ACCEPTED — Requires all five through the settled opening flow. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Gives out: ACCEPTED — A new session only after fresh authorization and its own opening commit. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Must never: ACCEPTED — Reuse a previous capture session or past biometric result to satisfy the new attempt. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Fails closed by: ACCEPTED — Missing any fresh requirement prevents the new session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.3.1 — Durable explicit-begin event: new choice; C-ENROLL.2 — Six-owner prerequisite check: fresh checks; C-BAI.19.1 — Enrollment BAI request interface: new pending and fresh token; C-ENROLL.3.3 — Prospective enrollment session identity: new reserved identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-ENROLL.16.3 — Required-audit durability failure
Stamp: ACCEPTED    Source: [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]

ALONE
- What it is: ACCEPTED — A required audit event cannot be written and flushed. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]
- Takes in: ACCEPTED — The actual owner's audit-write/flush failure. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Does: ACCEPTED — Withholds success for the affected operation and stops, blocks or closes honestly at its stage. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §23]
- Gives out: ACCEPTED — No claimed successful result unsupported by required durable history. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Must never: ACCEPTED — Treat an in-memory event or coordinator assertion as a completed required audit write. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Fails closed by: ACCEPTED — Owner success is not reported before the required event is durable. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]

TOGETHER
- Fed by: ACCEPTED — C-ENROLL.14 — Enrollment audit-event ownership: the actual required event and its owner. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece USED BY continuations

These continuation rows preserve the current TOGETHER relationships at their other endpoint. Earlier files are not edited. Future owners incorporate the rows when written; the register retains both exact endpoint names. Conditions and citations remain in the identified current field.

| USED BY owner | Using card | Current TOGETHER field | Exact current relationship | Disposition |
|---|---|---|---|---|
| C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10) | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | Fed by | DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): current finalized trust/recovery/QR/setup facts; C-BAI — Biometric Authorization Interface (§25.6): purpose-bound token and durable consumption truth. [V10 §25.11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]; ACCEPTED — C-PAIR.5 — Enrollment owner-fact boundary: pairing authority remains at its owner; C-PAIR.5.1 — Live prerequisite-owner reads: current owner references, versions and satisfaction; C-PAIR.5.2 — Pairing-owned enrollment safety events: current changes stop affected capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]; ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: owner-returned proposal and committed-link outcomes; C-SIA.20.1 — Eligible enrollment reading input: actual readiness rules and eligible reading constraints; C-SIA.20.2 — Provisional profile commit identity: actual SIA commit or refusal; C-SIA.20.7 — Profile-commit enrollment notification: commitment before the creation event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BAI — Biometric Authorization Interface (§25.6) | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | Fed by | DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): current finalized trust/recovery/QR/setup facts; C-BAI — Biometric Authorization Interface (§25.6): purpose-bound token and durable consumption truth. [V10 §25.11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]; ACCEPTED — C-PAIR.5 — Enrollment owner-fact boundary: pairing authority remains at its owner; C-PAIR.5.1 — Live prerequisite-owner reads: current owner references, versions and satisfaction; C-PAIR.5.2 — Pairing-owned enrollment safety events: current changes stop affected capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]; ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: owner-returned proposal and committed-link outcomes; C-SIA.20.1 — Eligible enrollment reading input: actual readiness rules and eligible reading constraints; C-SIA.20.2 — Provisional profile commit identity: actual SIA commit or refusal; C-SIA.20.7 — Profile-commit enrollment notification: commitment before the creation event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-PAIR.5 — Enrollment owner-fact boundary | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | Fed by | DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): current finalized trust/recovery/QR/setup facts; C-BAI — Biometric Authorization Interface (§25.6): purpose-bound token and durable consumption truth. [V10 §25.11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]; ACCEPTED — C-PAIR.5 — Enrollment owner-fact boundary: pairing authority remains at its owner; C-PAIR.5.1 — Live prerequisite-owner reads: current owner references, versions and satisfaction; C-PAIR.5.2 — Pairing-owned enrollment safety events: current changes stop affected capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]; ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: owner-returned proposal and committed-link outcomes; C-SIA.20.1 — Eligible enrollment reading input: actual readiness rules and eligible reading constraints; C-SIA.20.2 — Provisional profile commit identity: actual SIA commit or refusal; C-SIA.20.7 — Profile-commit enrollment notification: commitment before the creation event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-PAIR.5.1 — Live prerequisite-owner reads | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | Fed by | DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): current finalized trust/recovery/QR/setup facts; C-BAI — Biometric Authorization Interface (§25.6): purpose-bound token and durable consumption truth. [V10 §25.11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]; ACCEPTED — C-PAIR.5 — Enrollment owner-fact boundary: pairing authority remains at its owner; C-PAIR.5.1 — Live prerequisite-owner reads: current owner references, versions and satisfaction; C-PAIR.5.2 — Pairing-owned enrollment safety events: current changes stop affected capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]; ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: owner-returned proposal and committed-link outcomes; C-SIA.20.1 — Eligible enrollment reading input: actual readiness rules and eligible reading constraints; C-SIA.20.2 — Provisional profile commit identity: actual SIA commit or refusal; C-SIA.20.7 — Profile-commit enrollment notification: commitment before the creation event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-PAIR.5.2 — Pairing-owned enrollment safety events | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | Fed by | DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): current finalized trust/recovery/QR/setup facts; C-BAI — Biometric Authorization Interface (§25.6): purpose-bound token and durable consumption truth. [V10 §25.11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]; ACCEPTED — C-PAIR.5 — Enrollment owner-fact boundary: pairing authority remains at its owner; C-PAIR.5.1 — Live prerequisite-owner reads: current owner references, versions and satisfaction; C-PAIR.5.2 — Pairing-owned enrollment safety events: current changes stop affected capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]; ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: owner-returned proposal and committed-link outcomes; C-SIA.20.1 — Eligible enrollment reading input: actual readiness rules and eligible reading constraints; C-SIA.20.2 — Provisional profile commit identity: actual SIA commit or refusal; C-SIA.20.7 — Profile-commit enrollment notification: commitment before the creation event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-7L.11 — Provisional enrollment Person-Box link | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | Fed by | DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): current finalized trust/recovery/QR/setup facts; C-BAI — Biometric Authorization Interface (§25.6): purpose-bound token and durable consumption truth. [V10 §25.11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]; ACCEPTED — C-PAIR.5 — Enrollment owner-fact boundary: pairing authority remains at its owner; C-PAIR.5.1 — Live prerequisite-owner reads: current owner references, versions and satisfaction; C-PAIR.5.2 — Pairing-owned enrollment safety events: current changes stop affected capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]; ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: owner-returned proposal and committed-link outcomes; C-SIA.20.1 — Eligible enrollment reading input: actual readiness rules and eligible reading constraints; C-SIA.20.2 — Provisional profile commit identity: actual SIA commit or refusal; C-SIA.20.7 — Profile-commit enrollment notification: commitment before the creation event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SIA.20.1 — Eligible enrollment reading input | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | Fed by | DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): current finalized trust/recovery/QR/setup facts; C-BAI — Biometric Authorization Interface (§25.6): purpose-bound token and durable consumption truth. [V10 §25.11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]; ACCEPTED — C-PAIR.5 — Enrollment owner-fact boundary: pairing authority remains at its owner; C-PAIR.5.1 — Live prerequisite-owner reads: current owner references, versions and satisfaction; C-PAIR.5.2 — Pairing-owned enrollment safety events: current changes stop affected capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]; ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: owner-returned proposal and committed-link outcomes; C-SIA.20.1 — Eligible enrollment reading input: actual readiness rules and eligible reading constraints; C-SIA.20.2 — Provisional profile commit identity: actual SIA commit or refusal; C-SIA.20.7 — Profile-commit enrollment notification: commitment before the creation event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SIA.20.2 — Provisional profile commit identity | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | Fed by | DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): current finalized trust/recovery/QR/setup facts; C-BAI — Biometric Authorization Interface (§25.6): purpose-bound token and durable consumption truth. [V10 §25.11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]; ACCEPTED — C-PAIR.5 — Enrollment owner-fact boundary: pairing authority remains at its owner; C-PAIR.5.1 — Live prerequisite-owner reads: current owner references, versions and satisfaction; C-PAIR.5.2 — Pairing-owned enrollment safety events: current changes stop affected capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]; ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: owner-returned proposal and committed-link outcomes; C-SIA.20.1 — Eligible enrollment reading input: actual readiness rules and eligible reading constraints; C-SIA.20.2 — Provisional profile commit identity: actual SIA commit or refusal; C-SIA.20.7 — Profile-commit enrollment notification: commitment before the creation event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SIA.20.7 — Profile-commit enrollment notification | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | Fed by | DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): current finalized trust/recovery/QR/setup facts; C-BAI — Biometric Authorization Interface (§25.6): purpose-bound token and durable consumption truth. [V10 §25.11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6]; ACCEPTED — C-PAIR.5 — Enrollment owner-fact boundary: pairing authority remains at its owner; C-PAIR.5.1 — Live prerequisite-owner reads: current owner references, versions and satisfaction; C-PAIR.5.2 — Pairing-owned enrollment safety events: current changes stop affected capture. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]; ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: owner-returned proposal and committed-link outcomes; C-SIA.20.1 — Eligible enrollment reading input: actual readiness rules and eligible reading constraints; C-SIA.20.2 — Provisional profile commit identity: actual SIA commit or refusal; C-SIA.20.7 — Profile-commit enrollment notification: commitment before the creation event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SIA.12 — Conservative profile calibration | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | Gated by | DESIGNED — C-SIA.12 — Conservative profile calibration: provisional ceiling and conservative weighting; C-SIA.13 — Protected raw voice and readings: no raw-voice disclosure exception; C-SIA.20.6 — Enrollment association strengthening: later evidence and ordinary rules govern strengthening. [V10 §25.11 / SIA Integration] [V10 §25.11 / What Enrollment Does Not Establish] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]; ACCEPTED — C-SIA.20.8 — Enrollment authority limits: enrollment grants no additional identity, access, mode or action authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15]; DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture and output privacy; C-SACL — Speaker Access-Control Layer (§25.4): spoofing disqualification and final access; C-9 — Access/authentication model + voice I/O + phone modes (§9): current mode fence and B29 physical capture truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SIA.13 — Protected raw voice and readings | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | Gated by | DESIGNED — C-SIA.12 — Conservative profile calibration: provisional ceiling and conservative weighting; C-SIA.13 — Protected raw voice and readings: no raw-voice disclosure exception; C-SIA.20.6 — Enrollment association strengthening: later evidence and ordinary rules govern strengthening. [V10 §25.11 / SIA Integration] [V10 §25.11 / What Enrollment Does Not Establish] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]; ACCEPTED — C-SIA.20.8 — Enrollment authority limits: enrollment grants no additional identity, access, mode or action authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15]; DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture and output privacy; C-SACL — Speaker Access-Control Layer (§25.4): spoofing disqualification and final access; C-9 — Access/authentication model + voice I/O + phone modes (§9): current mode fence and B29 physical capture truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SIA.20.6 — Enrollment association strengthening | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | Gated by | DESIGNED — C-SIA.12 — Conservative profile calibration: provisional ceiling and conservative weighting; C-SIA.13 — Protected raw voice and readings: no raw-voice disclosure exception; C-SIA.20.6 — Enrollment association strengthening: later evidence and ordinary rules govern strengthening. [V10 §25.11 / SIA Integration] [V10 §25.11 / What Enrollment Does Not Establish] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]; ACCEPTED — C-SIA.20.8 — Enrollment authority limits: enrollment grants no additional identity, access, mode or action authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15]; DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture and output privacy; C-SACL — Speaker Access-Control Layer (§25.4): spoofing disqualification and final access; C-9 — Access/authentication model + voice I/O + phone modes (§9): current mode fence and B29 physical capture truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SIA.20.8 — Enrollment authority limits | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | Gated by | DESIGNED — C-SIA.12 — Conservative profile calibration: provisional ceiling and conservative weighting; C-SIA.13 — Protected raw voice and readings: no raw-voice disclosure exception; C-SIA.20.6 — Enrollment association strengthening: later evidence and ordinary rules govern strengthening. [V10 §25.11 / SIA Integration] [V10 §25.11 / What Enrollment Does Not Establish] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]; ACCEPTED — C-SIA.20.8 — Enrollment authority limits: enrollment grants no additional identity, access, mode or action authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15]; DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture and output privacy; C-SACL — Speaker Access-Control Layer (§25.4): spoofing disqualification and final access; C-9 — Access/authentication model + voice I/O + phone modes (§9): current mode fence and B29 physical capture truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | Gated by | DESIGNED — C-SIA.12 — Conservative profile calibration: provisional ceiling and conservative weighting; C-SIA.13 — Protected raw voice and readings: no raw-voice disclosure exception; C-SIA.20.6 — Enrollment association strengthening: later evidence and ordinary rules govern strengthening. [V10 §25.11 / SIA Integration] [V10 §25.11 / What Enrollment Does Not Establish] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]; ACCEPTED — C-SIA.20.8 — Enrollment authority limits: enrollment grants no additional identity, access, mode or action authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15]; DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture and output privacy; C-SACL — Speaker Access-Control Layer (§25.4): spoofing disqualification and final access; C-9 — Access/authentication model + voice I/O + phone modes (§9): current mode fence and B29 physical capture truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | Gated by | DESIGNED — C-SIA.12 — Conservative profile calibration: provisional ceiling and conservative weighting; C-SIA.13 — Protected raw voice and readings: no raw-voice disclosure exception; C-SIA.20.6 — Enrollment association strengthening: later evidence and ordinary rules govern strengthening. [V10 §25.11 / SIA Integration] [V10 §25.11 / What Enrollment Does Not Establish] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]; ACCEPTED — C-SIA.20.8 — Enrollment authority limits: enrollment grants no additional identity, access, mode or action authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15]; DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture and output privacy; C-SACL — Speaker Access-Control Layer (§25.4): spoofing disqualification and final access; C-9 — Access/authentication model + voice I/O + phone modes (§9): current mode fence and B29 physical capture truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-9 — Access/authentication model + voice I/O + phone modes (§9) | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | Gated by | DESIGNED — C-SIA.12 — Conservative profile calibration: provisional ceiling and conservative weighting; C-SIA.13 — Protected raw voice and readings: no raw-voice disclosure exception; C-SIA.20.6 — Enrollment association strengthening: later evidence and ordinary rules govern strengthening. [V10 §25.11 / SIA Integration] [V10 §25.11 / What Enrollment Does Not Establish] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]; ACCEPTED — C-SIA.20.8 — Enrollment authority limits: enrollment grants no additional identity, access, mode or action authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15]; DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture and output privacy; C-SACL — Speaker Access-Control Layer (§25.4): spoofing disqualification and final access; C-9 — Access/authentication model + voice I/O + phone modes (§9): current mode fence and B29 physical capture truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-7L.11 — Provisional enrollment Person-Box link | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | Changes | ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: submits only the proposal and exact frozen references; C-SIA.20 — Provisional enrollment profile handoff: supplies the linked eligible reading set and build identity [proposed] after current committed linkage. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | Pending endpoint placement |
| C-SIA.20 — Provisional enrollment profile handoff | C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | Changes | ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: submits only the proposal and exact frozen references; C-SIA.20 — Provisional enrollment profile handoff: supplies the linked eligible reading set and build identity [proposed] after current committed linkage. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | Pending endpoint placement |
| C-PAIR.5.1 — Live prerequisite-owner reads | C-ENROLL.2 — Six-owner prerequisite check | Fed by | ACCEPTED — C-PAIR.5.1 — Live prerequisite-owner reads: supplies the four pairing-owned current facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]; DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): supplies spoofing assessment; C-SACL — Speaker Access-Control Layer (§25.4): supplies its Gate 0 effect. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]; ACCEPTED — C-7L.4 — Ness's confirmed Person-Box: supplies confirmed-box truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] | Pending endpoint placement |
| C-SIA — Speaker Identity Assessment (§25.3) | C-ENROLL.2 — Six-owner prerequisite check | Fed by | ACCEPTED — C-PAIR.5.1 — Live prerequisite-owner reads: supplies the four pairing-owned current facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]; DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): supplies spoofing assessment; C-SACL — Speaker Access-Control Layer (§25.4): supplies its Gate 0 effect. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]; ACCEPTED — C-7L.4 — Ness's confirmed Person-Box: supplies confirmed-box truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-ENROLL.2 — Six-owner prerequisite check | Fed by | ACCEPTED — C-PAIR.5.1 — Live prerequisite-owner reads: supplies the four pairing-owned current facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]; DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): supplies spoofing assessment; C-SACL — Speaker Access-Control Layer (§25.4): supplies its Gate 0 effect. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]; ACCEPTED — C-7L.4 — Ness's confirmed Person-Box: supplies confirmed-box truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] | Pending endpoint placement |
| C-7L.4 — Ness's confirmed Person-Box | C-ENROLL.2 — Six-owner prerequisite check | Fed by | ACCEPTED — C-PAIR.5.1 — Live prerequisite-owner reads: supplies the four pairing-owned current facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]; DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): supplies spoofing assessment; C-SACL — Speaker Access-Control Layer (§25.4): supplies its Gate 0 effect. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4]; ACCEPTED — C-7L.4 — Ness's confirmed Person-Box: supplies confirmed-box truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] | Pending endpoint placement |
| C-PAIR.1.4.1 — Permanent trusted-owner status | C-ENROLL.2.1 — Final owner-phone prerequisite | Fed by | DESIGNED — C-PAIR.1.4.1 — Permanent trusted-owner status: the real final trust fact. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] | Pending endpoint placement |
| C-PAIR.2.3 — Normal-code activation handover | C-ENROLL.2.2 — Completed first-code prerequisite | Fed by | DESIGNED — C-PAIR.2.3 — Normal-code activation handover: the completed handover. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] | Pending endpoint placement |
| C-PAIR.1.2.1 — Signed QR inertness | C-ENROLL.2.3 — Inert initial-material prerequisite | Fed by | DESIGNED — C-PAIR.1.2.1 — Signed QR inertness: QR closure; C-PAIR.1.2.2 — Temporary pairing-secret inertness: secret closure. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] | Pending endpoint placement |
| C-PAIR.1.2.2 — Temporary pairing-secret inertness | C-ENROLL.2.3 — Inert initial-material prerequisite | Fed by | DESIGNED — C-PAIR.1.2.1 — Signed QR inertness: QR closure; C-PAIR.1.2.2 — Temporary pairing-secret inertness: secret closure. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] | Pending endpoint placement |
| C-PAIR.1.4.2 — Permanent initial QR-path closure | C-ENROLL.2.4 — Finalized setup prerequisite | Fed by | DESIGNED — C-PAIR.1.4.2 — Permanent initial QR-path closure: closed path; C-PAIR.1.6 — Initial-setup finalization audit event: finalized setup reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] | Pending endpoint placement |
| C-PAIR.1.6 — Initial-setup finalization audit event | C-ENROLL.2.4 — Finalized setup prerequisite | Fed by | DESIGNED — C-PAIR.1.4.2 — Permanent initial QR-path closure: closed path; C-PAIR.1.6 — Initial-setup finalization audit event: finalized setup reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] | Pending endpoint placement |
| C-SIA — Speaker Identity Assessment (§25.3) | C-ENROLL.2.5 — Clean current spoofing prerequisite | Fed by | DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): current assessment; C-SACL — Speaker Access-Control Layer (§25.4): current Gate 0 effect. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-ENROLL.2.5 — Clean current spoofing prerequisite | Fed by | DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): current assessment; C-SACL — Speaker Access-Control Layer (§25.4): current Gate 0 effect. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] | Pending endpoint placement |
| C-7L.4 — Ness's confirmed Person-Box | C-ENROLL.2.6 — Confirmed Ness-box prerequisite | Fed by | ACCEPTED — C-7L.4 — Ness's confirmed Person-Box: the confirmed identity fact. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] | Pending endpoint placement |
| C-PAIR.1.4.1 — Permanent trusted-owner status | C-ENROLL.3 — Explicit enrollment beginning | Fed by | DESIGNED — C-PAIR.1.4.1 — Permanent trusted-owner status: the trusted phone on which the explicit choice occurs. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-PAIR.1.2.3 — Hardware-backed phone binding | C-ENROLL.3.5 — Begin request phone-binding reference | Fed by | DESIGNED — C-PAIR.1.2.3 — Hardware-backed phone binding: actual cryptographic identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] | Pending endpoint placement |
| C-BAI.19.1 — Enrollment BAI request interface | C-ENROLL.4 — Ordered authorization and opening | Fed by | ACCEPTED — C-ENROLL.3 — Explicit enrollment beginning: claimed explicit action and prospective identities; C-ENROLL.2 — Six-owner prerequisite check: initial and immediately rechecked facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]; ACCEPTED — C-BAI.19.1 — Enrollment BAI request interface: BAI-owned pending and token responses; C-BAI.19.3 — Enrollment durable consumption proof: actual flushed proof; C-BAI.19.4 — Enrollment proof binding without new authority: verifiable operation/session binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] | Pending endpoint placement |
| C-BAI.19.3 — Enrollment durable consumption proof | C-ENROLL.4 — Ordered authorization and opening | Fed by | ACCEPTED — C-ENROLL.3 — Explicit enrollment beginning: claimed explicit action and prospective identities; C-ENROLL.2 — Six-owner prerequisite check: initial and immediately rechecked facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]; ACCEPTED — C-BAI.19.1 — Enrollment BAI request interface: BAI-owned pending and token responses; C-BAI.19.3 — Enrollment durable consumption proof: actual flushed proof; C-BAI.19.4 — Enrollment proof binding without new authority: verifiable operation/session binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] | Pending endpoint placement |
| C-BAI.19.4 — Enrollment proof binding without new authority | C-ENROLL.4 — Ordered authorization and opening | Fed by | ACCEPTED — C-ENROLL.3 — Explicit enrollment beginning: claimed explicit action and prospective identities; C-ENROLL.2 — Six-owner prerequisite check: initial and immediately rechecked facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5]; ACCEPTED — C-BAI.19.1 — Enrollment BAI request interface: BAI-owned pending and token responses; C-BAI.19.3 — Enrollment durable consumption proof: actual flushed proof; C-BAI.19.4 — Enrollment proof binding without new authority: verifiable operation/session binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] | Pending endpoint placement |
| C-BAI.19.2 — Enrollment prerequisite revalidation | C-ENROLL.4 — Ordered authorization and opening | Gated by | ACCEPTED — C-BAI.19.2 — Enrollment prerequisite revalidation: changed prerequisites prohibit consumption. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] | Pending endpoint placement |
| C-BAI.19.1 — Enrollment BAI request interface | C-ENROLL.4.1 — Enrollment BAI request fields | Fed by | ACCEPTED — C-BAI.19.1 — Enrollment BAI request interface: owns the response and one-pending rule. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BAI.19.2 — Enrollment prerequisite revalidation | C-ENROLL.4.2 — Final owner recheck and revocation | Gated by | ACCEPTED — C-BAI.19.2 — Enrollment prerequisite revalidation: BAI's required revalidation boundary. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] | Pending endpoint placement |
| C-BAI.5.4 — Revoked token state | C-ENROLL.4.2 — Final owner recheck and revocation | Changes | DESIGNED — C-BAI.5.4 — Revoked token state: BAI revokes the issued token and owns `bai_token_revoked`. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] | Pending endpoint placement |
| C-BAI.19.3 — Enrollment durable consumption proof | C-ENROLL.4.3 — Durable authorization chain and binding | Fed by | ACCEPTED — C-BAI.19.3 — Enrollment durable consumption proof: the actual flushed event; C-BAI.19.4 — Enrollment proof binding without new authority: direct or companion binding semantics. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] | Pending endpoint placement |
| C-BAI.19.4 — Enrollment proof binding without new authority | C-ENROLL.4.3 — Durable authorization chain and binding | Fed by | ACCEPTED — C-BAI.19.3 — Enrollment durable consumption proof: the actual flushed event; C-BAI.19.4 — Enrollment proof binding without new authority: direct or companion binding semantics. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] | Pending endpoint placement |
| C-BAI.19.3 — Enrollment durable consumption proof | C-ENROLL.4.3.3 — Bound token reference | Fed by | ACCEPTED — C-BAI.19.3 — Enrollment durable consumption proof: token consumption truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] | Pending endpoint placement |
| C-BAI.19.1 — Enrollment BAI request interface | C-ENROLL.4.3.4 — Bound pending-record reference | Fed by | ACCEPTED — C-BAI.19.1 — Enrollment BAI request interface: the original pending identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BAI.3.9.3 — Ness enrollment purpose | C-ENROLL.4.3.5 — Bound enrollment purpose | Fed by | DESIGNED — C-BAI.3.9.3 — Ness enrollment purpose: the existing purpose owner. [V10 §25.6] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] | Pending endpoint placement |
| C-BAI.3.8 — App-instance key reference | C-ENROLL.4.3.6 — Bound hardware phone key reference | Fed by | DESIGNED — C-BAI.3.8 — App-instance key reference: the hardware-backed phone binding. [V10 §25.6] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] | Pending endpoint placement |
| C-BAI.19.3 — Enrollment durable consumption proof | C-ENROLL.4.3.8 — Bound trusted-local timestamps | Fed by | ACCEPTED — C-BAI.19.3 — Enrollment durable consumption proof: BAI's actual audit times. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] | Pending endpoint placement |
| C-BAI.3.4 — Pending requester | C-ENROLL.4.3.9 — Bound requester identity | Fed by | DESIGNED — C-BAI.3.4 — Pending requester: the BAI requester's identity. [V10 §25.6] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] | Pending endpoint placement |
| C-BAI.19.3 — Enrollment durable consumption proof | C-ENROLL.4.3.10 — Bound audit schema and version | Fed by | ACCEPTED — C-BAI.19.3 — Enrollment durable consumption proof: the real audit record. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6A] | Pending endpoint placement |
| C-BAI.19.3 — Enrollment durable consumption proof | C-ENROLL.4.4 — Proof-bound session-open commit | Gated by | ACCEPTED — C-BAI.19.3 — Enrollment durable consumption proof: the BAI-owned event must be flushed and verified. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BOP.15.4 — Single enrollment biometric success observation | C-ENROLL.4.4 — Proof-bound session-open commit | Changes | ACCEPTED — C-BOP.15.4 — Single enrollment biometric success observation: permits timing coordination after actual opening, with BAI as sole source. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BAI.19.3 — Enrollment durable consumption proof | C-ENROLL.4.5 — Opening duplicate barriers | Fed by | ACCEPTED — C-ENROLL.3.4 — One-begin coordination claim: serialized reservation; C-BAI.19.3 — Enrollment durable consumption proof: the actual proof. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B] | Pending endpoint placement |
| C-BAI.19.1 — Enrollment BAI request interface | C-ENROLL.4.5.4 — Unmatched biometric-result barrier | Fed by | ACCEPTED — C-BAI.19.1 — Enrollment BAI request interface: actual pending/result truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BAI.19.3 — Enrollment durable consumption proof | C-ENROLL.4.5.6 — Missing durable-proof barrier | Gated by | ACCEPTED — C-BAI.19.3 — Enrollment durable consumption proof: actual flushed evidence is required. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6B] | Pending endpoint placement |
| C-BAI.19.1 — Enrollment BAI request interface | C-ENROLL.4.5.8 — Concurrent BAI-pending barrier | Gated by | ACCEPTED — C-BAI.19.1 — Enrollment BAI request interface: its single-pending rule controls admission. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BAI.19.5 — Enrollment consumed-proof crash boundary | C-ENROLL.4.6 — Spent proof without an opened session | Fed by | ACCEPTED — C-BAI.19.5 — Enrollment consumed-proof crash boundary: actual spent-proof truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6C] | Pending endpoint placement |
| C-BOP.15.1 — B29 capture and BOP observation ownership | C-ENROLL.5 — Capture-control and observation boundary | Fed by | ACCEPTED — C-ENROLL.4.4 — Proof-bound session-open commit: current opening; C-BOP.15.1 — B29 capture and BOP observation ownership: actual observed truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-ENROLL.5 — Capture-control and observation boundary | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture must be privacy-permitted; C-9 — Access/authentication model + voice I/O + phone modes (§9): B29 owns physical activation/deactivation and start/stop results. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-9 — Access/authentication model + voice I/O + phone modes (§9) | C-ENROLL.5 — Capture-control and observation boundary | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture must be privacy-permitted; C-9 — Access/authentication model + voice I/O + phone modes (§9): B29 owns physical activation/deactivation and start/stop results. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-ENROLL.5.1 — Current capture preconditions | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current capture eligibility; C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): current trust/security facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] | Pending endpoint placement |
| C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10) | C-ENROLL.5.1 — Current capture preconditions | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): current capture eligibility; C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): current trust/security facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6D] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] | Pending endpoint placement |
| C-9 — Access/authentication model + voice I/O + phone modes (§9) | C-ENROLL.5.3 — Reference-only B29 capture request | Changes | DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): hands the bounded request to B29's physical capture owner. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-ENROLL.5.3.4 — Capture privacy-decision reference | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the actual pre-capture privacy decision. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16] | Pending endpoint placement |
| C-BOP.15.2 — Enrollment observation provenance | C-ENROLL.5.3.5 — Capture declared-provenance references | Fed by | ACCEPTED — C-BOP.15.2 — Enrollment observation provenance: canonical provenance bindings and field owners. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] | Pending endpoint placement |
| C-BOP.15.1 — B29 capture and BOP observation ownership | C-ENROLL.5.3.6 — Capture destination observation context | Fed by | ACCEPTED — C-BOP.15.1 — B29 capture and BOP observation ownership: the actual observation receiver. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-9 — Access/authentication model + voice I/O + phone modes (§9) | C-ENROLL.5.4 — B29 capture-start result | Fed by | DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): B29 supplies the physical result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-9 — Access/authentication model + voice I/O + phone modes (§9) | C-ENROLL.5.5 — B29-sourced capture-start fact | Fed by | DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): the B29 source of physical start truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BOP.15.1 — B29 capture and BOP observation ownership | C-ENROLL.5.6 — Enrollment physical-observation consumption | Fed by | ACCEPTED — C-BOP.15.1 — B29 capture and BOP observation ownership: committed stream truth; C-BOP.15.2 — Enrollment observation provenance: declared attribution; C-BOP.12 — Optional acoustic_condition_notes amendment: the existing six-field record and five controlled physical-condition names. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BOP.15.2 — Enrollment observation provenance | C-ENROLL.5.6 — Enrollment physical-observation consumption | Fed by | ACCEPTED — C-BOP.15.1 — B29 capture and BOP observation ownership: committed stream truth; C-BOP.15.2 — Enrollment observation provenance: declared attribution; C-BOP.12 — Optional acoustic_condition_notes amendment: the existing six-field record and five controlled physical-condition names. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BOP.12 — Optional acoustic_condition_notes amendment | C-ENROLL.5.6 — Enrollment physical-observation consumption | Fed by | ACCEPTED — C-BOP.15.1 — B29 capture and BOP observation ownership: committed stream truth; C-BOP.15.2 — Enrollment observation provenance: declared attribution; C-BOP.12 — Optional acoustic_condition_notes amendment: the existing six-field record and five controlled physical-condition names. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §7] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BOP.15.6 — Protected raw-voice boundary | C-ENROLL.5.6 — Enrollment physical-observation consumption | Gated by | ACCEPTED — C-BOP.15.6 — Protected raw-voice boundary: minimum necessary protected interface and no raw voice in coordination. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16] | Pending endpoint placement |
| C-BAI.19.6 — BAI-owned enrollment success observation | C-ENROLL.5.7 — Enrollment biometric-observation timing | Fed by | ACCEPTED — C-BAI.19.6 — BAI-owned enrollment success observation: sole source; C-BOP.15.4 — Single enrollment biometric success observation: idempotent physical receiver. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BOP.15.4 — Single enrollment biometric success observation | C-ENROLL.5.7 — Enrollment biometric-observation timing | Fed by | ACCEPTED — C-BAI.19.6 — BAI-owned enrollment success observation: sole source; C-BOP.15.4 — Single enrollment biometric success observation: idempotent physical receiver. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-7L.11 — Provisional enrollment Person-Box link | C-ENROLL.6 — Enrollment process lifecycle | Fed by | ACCEPTED — C-ENROLL.4.4 — Proof-bound session-open commit: opening truth; C-ENROLL.5.4 — B29 capture-start result: start truth; C-7L.11 — Provisional enrollment Person-Box link: link truth; C-SIA.20.2 — Provisional profile commit identity: profile truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] | Pending endpoint placement |
| C-SIA.20.2 — Provisional profile commit identity | C-ENROLL.6 — Enrollment process lifecycle | Fed by | ACCEPTED — C-ENROLL.4.4 — Proof-bound session-open commit: opening truth; C-ENROLL.5.4 — B29 capture-start result: start truth; C-7L.11 — Provisional enrollment Person-Box link: link truth; C-SIA.20.2 — Provisional profile commit identity: profile truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] | Pending endpoint placement |
| C-BAI.19.1 — Enrollment BAI request interface | C-ENROLL.6.3 — Biometric pending process state | Fed by | ACCEPTED — C-BAI.19.1 — Enrollment BAI request interface: actual pending status. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] | Pending endpoint placement |
| C-BAI.19 — Enrollment authorization producer | C-ENROLL.6.4 — Token issued process state | Fed by | ACCEPTED — C-BAI.19 — Enrollment authorization producer: actual token issuance. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] | Pending endpoint placement |
| C-BAI.19.3 — Enrollment durable consumption proof | C-ENROLL.6.6 — Token durably consumed state | Fed by | ACCEPTED — C-BAI.19.3 — Enrollment durable consumption proof: flushed owner truth; C-ENROLL.4.3 — Durable authorization chain and binding: verified binding. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §8] | Pending endpoint placement |
| C-BOP.13.1 — BOP consumption of B11 writer protections | C-ENROLL.6.16 — Roots partially committed state | Fed by | ACCEPTED — C-BOP.13.1 — BOP consumption of B11 writer protections: actual append/fence outcomes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] | Pending endpoint placement |
| C-BOP.13.1 — BOP consumption of B11 writer protections | C-ENROLL.6.17 — Roots committed state | Fed by | ACCEPTED — C-BOP.13.1 — BOP consumption of B11 writer protections: verified append outcomes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] | Pending endpoint placement |
| C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | C-ENROLL.6.18 — Readings pending state | Fed by | DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): actual enqueue truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | C-ENROLL.6.19 — Readings partially completed state | Fed by | DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): committed reading outcomes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] | Pending endpoint placement |
| C-7L.11 — Provisional enrollment Person-Box link | C-ENROLL.6.22 — Provisional link proposed state | Fed by | ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: the owner-returned proposal status. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Pending endpoint placement |
| C-7L.11.13.1 — Enrollment current committed-link result | C-ENROLL.6.23 — Provisional link committed state | Fed by | ACCEPTED — C-7L.11.13.1 — Enrollment current committed-link result: actual owner truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Pending endpoint placement |
| C-SIA.20.7 — Profile-commit enrollment notification | C-ENROLL.6.24 — Provisional profile created state | Fed by | ACCEPTED — C-SIA.20.7 — Profile-commit enrollment notification: actual commit before event emission. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | Pending endpoint placement |
| C-7L.11 — Provisional enrollment Person-Box link | C-ENROLL.6.25 — Completed parent state | Fed by | ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: link commitment; C-SIA.20.7 — Profile-commit enrollment notification: profile commitment and event ordering. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | Pending endpoint placement |
| C-SIA.20.7 — Profile-commit enrollment notification | C-ENROLL.6.25 — Completed parent state | Fed by | ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: link commitment; C-SIA.20.7 — Profile-commit enrollment notification: profile commitment and event ordering. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | Pending endpoint placement |
| C-PAIR.5.2 — Pairing-owned enrollment safety events | C-ENROLL.7 — Mid-session protective stop | Fed by | ACCEPTED — C-PAIR.5.2 — Pairing-owned enrollment safety events: actual trust/recovery/QR/setup changes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]; DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): spoofing changes; C-SACL — Speaker Access-Control Layer (§25.4): Gate 0 effect; C-7L — Person-Boxes (§7L): prerequisite changes; C-BAI — Biometric Authorization Interface (§25.6): security/session integrity events; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture exclusion. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] | Pending endpoint placement |
| C-SIA — Speaker Identity Assessment (§25.3) | C-ENROLL.7 — Mid-session protective stop | Fed by | ACCEPTED — C-PAIR.5.2 — Pairing-owned enrollment safety events: actual trust/recovery/QR/setup changes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]; DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): spoofing changes; C-SACL — Speaker Access-Control Layer (§25.4): Gate 0 effect; C-7L — Person-Boxes (§7L): prerequisite changes; C-BAI — Biometric Authorization Interface (§25.6): security/session integrity events; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture exclusion. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-ENROLL.7 — Mid-session protective stop | Fed by | ACCEPTED — C-PAIR.5.2 — Pairing-owned enrollment safety events: actual trust/recovery/QR/setup changes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]; DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): spoofing changes; C-SACL — Speaker Access-Control Layer (§25.4): Gate 0 effect; C-7L — Person-Boxes (§7L): prerequisite changes; C-BAI — Biometric Authorization Interface (§25.6): security/session integrity events; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture exclusion. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] | Pending endpoint placement |
| C-7L — Person-Boxes (§7L) | C-ENROLL.7 — Mid-session protective stop | Fed by | ACCEPTED — C-PAIR.5.2 — Pairing-owned enrollment safety events: actual trust/recovery/QR/setup changes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]; DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): spoofing changes; C-SACL — Speaker Access-Control Layer (§25.4): Gate 0 effect; C-7L — Person-Boxes (§7L): prerequisite changes; C-BAI — Biometric Authorization Interface (§25.6): security/session integrity events; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture exclusion. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] | Pending endpoint placement |
| C-BAI — Biometric Authorization Interface (§25.6) | C-ENROLL.7 — Mid-session protective stop | Fed by | ACCEPTED — C-PAIR.5.2 — Pairing-owned enrollment safety events: actual trust/recovery/QR/setup changes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]; DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): spoofing changes; C-SACL — Speaker Access-Control Layer (§25.4): Gate 0 effect; C-7L — Person-Boxes (§7L): prerequisite changes; C-BAI — Biometric Authorization Interface (§25.6): security/session integrity events; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture exclusion. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-ENROLL.7 — Mid-session protective stop | Fed by | ACCEPTED — C-PAIR.5.2 — Pairing-owned enrollment safety events: actual trust/recovery/QR/setup changes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9]; DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): spoofing changes; C-SACL — Speaker Access-Control Layer (§25.4): Gate 0 effect; C-7L — Person-Boxes (§7L): prerequisite changes; C-BAI — Biometric Authorization Interface (§25.6): security/session integrity events; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture exclusion. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] | Pending endpoint placement |
| C-9 — Access/authentication model + voice I/O + phone modes (§9) | C-ENROLL.7 — Mid-session protective stop | Changes | DESIGNED — C-9 — Access/authentication model + voice I/O + phone modes (§9): B29 stops physical capture on the protective request. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-PAIR.5.2 — Pairing-owned enrollment safety events | C-ENROLL.7.1 — Trusted-phone safety changes | Fed by | ACCEPTED — C-PAIR.5.2 — Pairing-owned enrollment safety events: loss, replacement and revocation truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] | Pending endpoint placement |
| C-PAIR.5.2 — Pairing-owned enrollment safety events | C-ENROLL.7.2 — Invalid recovery or setup safety change | Fed by | ACCEPTED — C-PAIR.5.2 — Pairing-owned enrollment safety events: actual invalidation. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] | Pending endpoint placement |
| C-PAIR.5.2 — Pairing-owned enrollment safety events | C-ENROLL.7.3 — Initial-material integrity contradiction | Fed by | ACCEPTED — C-PAIR.5.2 — Pairing-owned enrollment safety events: the integrity contradiction. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] | Pending endpoint placement |
| C-SIA — Speaker Identity Assessment (§25.3) | C-ENROLL.7.4 — Spoofing safety change | Fed by | DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): actual suspicion; C-SACL — Speaker Access-Control Layer (§25.4): disqualifier effect. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-ENROLL.7.4 — Spoofing safety change | Fed by | DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): actual suspicion; C-SACL — Speaker Access-Control Layer (§25.4): disqualifier effect. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] | Pending endpoint placement |
| C-7L — Person-Boxes (§7L) | C-ENROLL.7.5 — Person-Box prerequisite safety change | Fed by | DESIGNED — C-7L — Person-Boxes (§7L): the changed prerequisite truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] | Pending endpoint placement |
| C-BAI — Biometric Authorization Interface (§25.6) | C-ENROLL.7.6 — BAI or session integrity failure | Fed by | DESIGNED — C-BAI — Biometric Authorization Interface (§25.6): actual security integrity truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §9] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-ENROLL.7.7 — Privacy capture-exclusion safety change | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): actual capture exclusion and protected handling. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16] | Pending endpoint placement |
| C-BOP.15.1 — B29 capture and BOP observation ownership | C-ENROLL.7.8 — Application or machine restart safety change | Fed by | ACCEPTED — C-ENROLL.5.4 — B29 capture-start result: whatever physical truth is provable; C-BOP.15.1 — B29 capture and BOP observation ownership: actual committed observations. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] | Pending endpoint placement |
| C-BOP.15.5 — Frozen enrollment capture set and normal entry | C-ENROLL.8 — Closed-session root and reading handoff | Fed by | ACCEPTED — C-BOP.15.5 — Frozen enrollment capture set and normal entry: actual observation references and standard path; C-BOP.13.1 — BOP consumption of B11 writer protections: global claim, ownership and fence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] | Pending endpoint placement |
| C-BOP.13.1 — BOP consumption of B11 writer protections | C-ENROLL.8 — Closed-session root and reading handoff | Fed by | ACCEPTED — C-BOP.15.5 — Frozen enrollment capture set and normal entry: actual observation references and standard path; C-BOP.13.1 — BOP consumption of B11 writer protections: global claim, ownership and fence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] | Pending endpoint placement |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | C-ENROLL.8 — Closed-session root and reading handoff | Gated by | DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): ordinary intake acceptance; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture exclusion remains separate from profile rejection. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-ENROLL.8 — Closed-session root and reading handoff | Gated by | DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): ordinary intake acceptance; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture exclusion remains separate from profile rejection. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] | Pending endpoint placement |
| C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | C-ENROLL.8 — Closed-session root and reading handoff | Changes | DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): committed roots enter its existing queue. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]; ACCEPTED — C-READ.11 — Quarantine-to-production promotion seam: enrollment readings remain quarantine unless separately promoted normally. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] | Pending endpoint placement |
| C-READ.11 — Quarantine-to-production promotion seam | C-ENROLL.8 — Closed-session root and reading handoff | Changes | DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): committed roots enter its existing queue. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10]; ACCEPTED — C-READ.11 — Quarantine-to-production promotion seam: enrollment readings remain quarantine unless separately promoted normally. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] | Pending endpoint placement |
| C-BOP.15.1 — B29 capture and BOP observation ownership | C-ENROLL.8.1 — Frozen enrollment capture-set record | Fed by | ACCEPTED — C-BOP.15.1 — B29 capture and BOP observation ownership: committed physical truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BOP.15.2 — Enrollment observation provenance | C-ENROLL.8.2 — Catalog submission interface | Fed by | ACCEPTED — C-ENROLL.8.1 — Frozen enrollment capture-set record: exact capture references; C-BOP.15.2 — Enrollment observation provenance: canonical declared provenance fields. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | C-ENROLL.8.2 — Catalog submission interface | Gated by | DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): owns accepted/rejected/blocked intake truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BOP.13.1 — BOP consumption of B11 writer protections | C-ENROLL.8.3 — B11 append interface | Fed by | ACCEPTED — C-BOP.13.1 — BOP consumption of B11 writer protections: the complete existing writer mechanism; C-STORE.4.6.2.1 — ingest_operation_id [proposed]: B11's operation identity; C-STORE.4.6.2.3 — capture_id: end-to-end duplicate identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-STORE.4.6.2.1 — ingest_operation_id [proposed] | C-ENROLL.8.3 — B11 append interface | Fed by | ACCEPTED — C-BOP.13.1 — BOP consumption of B11 writer protections: the complete existing writer mechanism; C-STORE.4.6.2.1 — ingest_operation_id [proposed]: B11's operation identity; C-STORE.4.6.2.3 — capture_id: end-to-end duplicate identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-STORE.4.6.2.3 — capture_id | C-ENROLL.8.3 — B11 append interface | Fed by | ACCEPTED — C-BOP.13.1 — BOP consumption of B11 writer protections: the complete existing writer mechanism; C-STORE.4.6.2.1 — ingest_operation_id [proposed]: B11's operation identity; C-STORE.4.6.2.3 — capture_id: end-to-end duplicate identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-STORE.3.5 — Atomic root append and identity idempotency | C-ENROLL.8.3 — B11 append interface | Gated by | DESIGNED — C-STORE.3.5 — Atomic root append and identity idempotency: the sole append route and duplicate protection. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | C-ENROLL.8.4 — Root-identity reading enqueue | Gated by | DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): owns enqueue and reading outcomes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SIA — Speaker Identity Assessment (§25.3) | C-ENROLL.9 — Initial-corpus eligibility gate | Fed by | DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): spoofing/diarization facts; C-BOP — Behavioral Observation Processing (§25.1/§26): completeness and physical provenance; C-BAI — Biometric Authorization Interface (§25.6): durable token-consumption truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BOP — Behavioral Observation Processing (§25.1/§26) | C-ENROLL.9 — Initial-corpus eligibility gate | Fed by | DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): spoofing/diarization facts; C-BOP — Behavioral Observation Processing (§25.1/§26): completeness and physical provenance; C-BAI — Biometric Authorization Interface (§25.6): durable token-consumption truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BAI — Biometric Authorization Interface (§25.6) | C-ENROLL.9 — Initial-corpus eligibility gate | Fed by | DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): spoofing/diarization facts; C-BOP — Behavioral Observation Processing (§25.1/§26): completeness and physical provenance; C-BAI — Biometric Authorization Interface (§25.6): durable token-consumption truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SIA — Speaker Identity Assessment (§25.3) | C-ENROLL.9.1 — Consistent live-speaker stream check | Fed by | DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): actual stream/diarization facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SIA — Speaker Identity Assessment (§25.3) | C-ENROLL.9.2 — Segment spoofing check | Fed by | DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): the actual spoofing fact. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SIA — Speaker Identity Assessment (§25.3) | C-ENROLL.9.3 — Overlapping-speaker contamination check | Fed by | DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): owned speaker-stream assessment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BOP.6.4 — overall_completeness | C-ENROLL.9.4 — Allowed observation-completeness check | Fed by | DESIGNED — C-BOP.6.4 — overall_completeness: canonical field and actual value. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] | Pending endpoint placement |
| C-BOP.4.9.1.3 — enrollment_declared | C-ENROLL.9.5 — Declared authorization and durable-token check | Fed by | DESIGNED — C-BOP.4.9.1.3 — enrollment_declared: canonical declared authorization meaning. [V10 §25.12] | Pending endpoint placement |
| C-BAI.19.3 — Enrollment durable consumption proof | C-ENROLL.9.5 — Declared authorization and durable-token check | Gated by | ACCEPTED — C-BAI.19.3 — Enrollment durable consumption proof: actual durable consumption must be linked to the session. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §11] | Pending endpoint placement |
| C-SIA — Speaker Identity Assessment (§25.3) | C-ENROLL.9.6 — Full-segment stream-integrity check | Fed by | DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): actual diarization and spoofing facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SIA — Speaker Identity Assessment (§25.3) | C-ENROLL.9.6.1 — Full-segment diarization-confidence condition | Fed by | DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): diarization facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SIA — Speaker Identity Assessment (§25.3) | C-ENROLL.9.6.2 — Resolved speaker-transition condition | Fed by | DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): transition assessment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SIA — Speaker Identity Assessment (§25.3) | C-ENROLL.9.6.3 — No material stream split or merge condition | Fed by | DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): stream-structure facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SIA — Speaker Identity Assessment (§25.3) | C-ENROLL.9.6.4 — No unresolved second-speaker uncertainty condition | Fed by | DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): second-speaker assessment. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SIA — Speaker Identity Assessment (§25.3) | C-ENROLL.9.6.5 — Stream spoofing-evidence condition | Fed by | DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): actual spoofing facts. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SIA.20.1 — Eligible enrollment reading input | C-ENROLL.10 — Profile readiness record | Gated by | ACCEPTED — C-SIA.20.1 — Eligible enrollment reading input: actual profile-integrity/SIA rule and values, with no chosen number, duration, score, confidence, calibration or acoustic algorithm here. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] | Pending endpoint placement |
| C-SIA.20.1 — Eligible enrollment reading input | C-ENROLL.10.3 — Readiness outcome | Gated by | ACCEPTED — C-SIA.20.1 — Eligible enrollment reading input: the real readiness rule and its values. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] | Pending endpoint placement |
| C-7L.11.6 — Enrollment proposed input-bundle reference | C-ENROLL.10.5 — Immutable enrollment input bundle | Changes | ACCEPTED — C-7L.11.6 — Enrollment proposed input-bundle reference: receives the exact immutable bundle reference. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Pending endpoint placement |
| C-7L.11.1 — Enrollment provisional link type | C-ENROLL.11 — Provisional link and profile coordination | Fed by | ACCEPTED — C-ENROLL.10.5 — Immutable enrollment input bundle: frozen reference inputs; C-7L.11.1 — Enrollment provisional link type: exact type; C-7L.11.2 — Enrollment provisional link certainty: provisional certainty; C-7L.11.3 — Enrollment provisional link proposal ID: stable query identity; C-7L.11.4 — Enrollment provisional link meaning: collection provenance; C-7L.11.5 — Enrollment provisional link basis: actual authorization basis. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]; ACCEPTED — C-7L.11.6 — Enrollment proposed input-bundle reference: exact frozen input pointer; C-7L.11.7 — Enrollment confirmed Ness-box reference: confirmed destination; C-7L.11.8 — Enrollment link operation reference: parent; C-7L.11.9 — Enrollment link session reference: collection session; C-7L.11.10 — Enrollment link eligible-reading references: exact reading set; C-7L.11.11 — Enrollment link eligibility-decision references: decisions; C-7L.11.12 — Enrollment link prerequisite-evidence references: owner evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Pending endpoint placement |
| C-7L.11.2 — Enrollment provisional link certainty | C-ENROLL.11 — Provisional link and profile coordination | Fed by | ACCEPTED — C-ENROLL.10.5 — Immutable enrollment input bundle: frozen reference inputs; C-7L.11.1 — Enrollment provisional link type: exact type; C-7L.11.2 — Enrollment provisional link certainty: provisional certainty; C-7L.11.3 — Enrollment provisional link proposal ID: stable query identity; C-7L.11.4 — Enrollment provisional link meaning: collection provenance; C-7L.11.5 — Enrollment provisional link basis: actual authorization basis. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]; ACCEPTED — C-7L.11.6 — Enrollment proposed input-bundle reference: exact frozen input pointer; C-7L.11.7 — Enrollment confirmed Ness-box reference: confirmed destination; C-7L.11.8 — Enrollment link operation reference: parent; C-7L.11.9 — Enrollment link session reference: collection session; C-7L.11.10 — Enrollment link eligible-reading references: exact reading set; C-7L.11.11 — Enrollment link eligibility-decision references: decisions; C-7L.11.12 — Enrollment link prerequisite-evidence references: owner evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Pending endpoint placement |
| C-7L.11.3 — Enrollment provisional link proposal ID | C-ENROLL.11 — Provisional link and profile coordination | Fed by | ACCEPTED — C-ENROLL.10.5 — Immutable enrollment input bundle: frozen reference inputs; C-7L.11.1 — Enrollment provisional link type: exact type; C-7L.11.2 — Enrollment provisional link certainty: provisional certainty; C-7L.11.3 — Enrollment provisional link proposal ID: stable query identity; C-7L.11.4 — Enrollment provisional link meaning: collection provenance; C-7L.11.5 — Enrollment provisional link basis: actual authorization basis. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]; ACCEPTED — C-7L.11.6 — Enrollment proposed input-bundle reference: exact frozen input pointer; C-7L.11.7 — Enrollment confirmed Ness-box reference: confirmed destination; C-7L.11.8 — Enrollment link operation reference: parent; C-7L.11.9 — Enrollment link session reference: collection session; C-7L.11.10 — Enrollment link eligible-reading references: exact reading set; C-7L.11.11 — Enrollment link eligibility-decision references: decisions; C-7L.11.12 — Enrollment link prerequisite-evidence references: owner evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Pending endpoint placement |
| C-7L.11.4 — Enrollment provisional link meaning | C-ENROLL.11 — Provisional link and profile coordination | Fed by | ACCEPTED — C-ENROLL.10.5 — Immutable enrollment input bundle: frozen reference inputs; C-7L.11.1 — Enrollment provisional link type: exact type; C-7L.11.2 — Enrollment provisional link certainty: provisional certainty; C-7L.11.3 — Enrollment provisional link proposal ID: stable query identity; C-7L.11.4 — Enrollment provisional link meaning: collection provenance; C-7L.11.5 — Enrollment provisional link basis: actual authorization basis. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]; ACCEPTED — C-7L.11.6 — Enrollment proposed input-bundle reference: exact frozen input pointer; C-7L.11.7 — Enrollment confirmed Ness-box reference: confirmed destination; C-7L.11.8 — Enrollment link operation reference: parent; C-7L.11.9 — Enrollment link session reference: collection session; C-7L.11.10 — Enrollment link eligible-reading references: exact reading set; C-7L.11.11 — Enrollment link eligibility-decision references: decisions; C-7L.11.12 — Enrollment link prerequisite-evidence references: owner evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Pending endpoint placement |
| C-7L.11.5 — Enrollment provisional link basis | C-ENROLL.11 — Provisional link and profile coordination | Fed by | ACCEPTED — C-ENROLL.10.5 — Immutable enrollment input bundle: frozen reference inputs; C-7L.11.1 — Enrollment provisional link type: exact type; C-7L.11.2 — Enrollment provisional link certainty: provisional certainty; C-7L.11.3 — Enrollment provisional link proposal ID: stable query identity; C-7L.11.4 — Enrollment provisional link meaning: collection provenance; C-7L.11.5 — Enrollment provisional link basis: actual authorization basis. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]; ACCEPTED — C-7L.11.6 — Enrollment proposed input-bundle reference: exact frozen input pointer; C-7L.11.7 — Enrollment confirmed Ness-box reference: confirmed destination; C-7L.11.8 — Enrollment link operation reference: parent; C-7L.11.9 — Enrollment link session reference: collection session; C-7L.11.10 — Enrollment link eligible-reading references: exact reading set; C-7L.11.11 — Enrollment link eligibility-decision references: decisions; C-7L.11.12 — Enrollment link prerequisite-evidence references: owner evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Pending endpoint placement |
| C-7L.11.6 — Enrollment proposed input-bundle reference | C-ENROLL.11 — Provisional link and profile coordination | Fed by | ACCEPTED — C-ENROLL.10.5 — Immutable enrollment input bundle: frozen reference inputs; C-7L.11.1 — Enrollment provisional link type: exact type; C-7L.11.2 — Enrollment provisional link certainty: provisional certainty; C-7L.11.3 — Enrollment provisional link proposal ID: stable query identity; C-7L.11.4 — Enrollment provisional link meaning: collection provenance; C-7L.11.5 — Enrollment provisional link basis: actual authorization basis. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]; ACCEPTED — C-7L.11.6 — Enrollment proposed input-bundle reference: exact frozen input pointer; C-7L.11.7 — Enrollment confirmed Ness-box reference: confirmed destination; C-7L.11.8 — Enrollment link operation reference: parent; C-7L.11.9 — Enrollment link session reference: collection session; C-7L.11.10 — Enrollment link eligible-reading references: exact reading set; C-7L.11.11 — Enrollment link eligibility-decision references: decisions; C-7L.11.12 — Enrollment link prerequisite-evidence references: owner evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Pending endpoint placement |
| C-7L.11.7 — Enrollment confirmed Ness-box reference | C-ENROLL.11 — Provisional link and profile coordination | Fed by | ACCEPTED — C-ENROLL.10.5 — Immutable enrollment input bundle: frozen reference inputs; C-7L.11.1 — Enrollment provisional link type: exact type; C-7L.11.2 — Enrollment provisional link certainty: provisional certainty; C-7L.11.3 — Enrollment provisional link proposal ID: stable query identity; C-7L.11.4 — Enrollment provisional link meaning: collection provenance; C-7L.11.5 — Enrollment provisional link basis: actual authorization basis. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]; ACCEPTED — C-7L.11.6 — Enrollment proposed input-bundle reference: exact frozen input pointer; C-7L.11.7 — Enrollment confirmed Ness-box reference: confirmed destination; C-7L.11.8 — Enrollment link operation reference: parent; C-7L.11.9 — Enrollment link session reference: collection session; C-7L.11.10 — Enrollment link eligible-reading references: exact reading set; C-7L.11.11 — Enrollment link eligibility-decision references: decisions; C-7L.11.12 — Enrollment link prerequisite-evidence references: owner evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Pending endpoint placement |
| C-7L.11.8 — Enrollment link operation reference | C-ENROLL.11 — Provisional link and profile coordination | Fed by | ACCEPTED — C-ENROLL.10.5 — Immutable enrollment input bundle: frozen reference inputs; C-7L.11.1 — Enrollment provisional link type: exact type; C-7L.11.2 — Enrollment provisional link certainty: provisional certainty; C-7L.11.3 — Enrollment provisional link proposal ID: stable query identity; C-7L.11.4 — Enrollment provisional link meaning: collection provenance; C-7L.11.5 — Enrollment provisional link basis: actual authorization basis. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]; ACCEPTED — C-7L.11.6 — Enrollment proposed input-bundle reference: exact frozen input pointer; C-7L.11.7 — Enrollment confirmed Ness-box reference: confirmed destination; C-7L.11.8 — Enrollment link operation reference: parent; C-7L.11.9 — Enrollment link session reference: collection session; C-7L.11.10 — Enrollment link eligible-reading references: exact reading set; C-7L.11.11 — Enrollment link eligibility-decision references: decisions; C-7L.11.12 — Enrollment link prerequisite-evidence references: owner evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Pending endpoint placement |
| C-7L.11.9 — Enrollment link session reference | C-ENROLL.11 — Provisional link and profile coordination | Fed by | ACCEPTED — C-ENROLL.10.5 — Immutable enrollment input bundle: frozen reference inputs; C-7L.11.1 — Enrollment provisional link type: exact type; C-7L.11.2 — Enrollment provisional link certainty: provisional certainty; C-7L.11.3 — Enrollment provisional link proposal ID: stable query identity; C-7L.11.4 — Enrollment provisional link meaning: collection provenance; C-7L.11.5 — Enrollment provisional link basis: actual authorization basis. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]; ACCEPTED — C-7L.11.6 — Enrollment proposed input-bundle reference: exact frozen input pointer; C-7L.11.7 — Enrollment confirmed Ness-box reference: confirmed destination; C-7L.11.8 — Enrollment link operation reference: parent; C-7L.11.9 — Enrollment link session reference: collection session; C-7L.11.10 — Enrollment link eligible-reading references: exact reading set; C-7L.11.11 — Enrollment link eligibility-decision references: decisions; C-7L.11.12 — Enrollment link prerequisite-evidence references: owner evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Pending endpoint placement |
| C-7L.11.10 — Enrollment link eligible-reading references | C-ENROLL.11 — Provisional link and profile coordination | Fed by | ACCEPTED — C-ENROLL.10.5 — Immutable enrollment input bundle: frozen reference inputs; C-7L.11.1 — Enrollment provisional link type: exact type; C-7L.11.2 — Enrollment provisional link certainty: provisional certainty; C-7L.11.3 — Enrollment provisional link proposal ID: stable query identity; C-7L.11.4 — Enrollment provisional link meaning: collection provenance; C-7L.11.5 — Enrollment provisional link basis: actual authorization basis. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]; ACCEPTED — C-7L.11.6 — Enrollment proposed input-bundle reference: exact frozen input pointer; C-7L.11.7 — Enrollment confirmed Ness-box reference: confirmed destination; C-7L.11.8 — Enrollment link operation reference: parent; C-7L.11.9 — Enrollment link session reference: collection session; C-7L.11.10 — Enrollment link eligible-reading references: exact reading set; C-7L.11.11 — Enrollment link eligibility-decision references: decisions; C-7L.11.12 — Enrollment link prerequisite-evidence references: owner evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Pending endpoint placement |
| C-7L.11.11 — Enrollment link eligibility-decision references | C-ENROLL.11 — Provisional link and profile coordination | Fed by | ACCEPTED — C-ENROLL.10.5 — Immutable enrollment input bundle: frozen reference inputs; C-7L.11.1 — Enrollment provisional link type: exact type; C-7L.11.2 — Enrollment provisional link certainty: provisional certainty; C-7L.11.3 — Enrollment provisional link proposal ID: stable query identity; C-7L.11.4 — Enrollment provisional link meaning: collection provenance; C-7L.11.5 — Enrollment provisional link basis: actual authorization basis. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]; ACCEPTED — C-7L.11.6 — Enrollment proposed input-bundle reference: exact frozen input pointer; C-7L.11.7 — Enrollment confirmed Ness-box reference: confirmed destination; C-7L.11.8 — Enrollment link operation reference: parent; C-7L.11.9 — Enrollment link session reference: collection session; C-7L.11.10 — Enrollment link eligible-reading references: exact reading set; C-7L.11.11 — Enrollment link eligibility-decision references: decisions; C-7L.11.12 — Enrollment link prerequisite-evidence references: owner evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Pending endpoint placement |
| C-7L.11.12 — Enrollment link prerequisite-evidence references | C-ENROLL.11 — Provisional link and profile coordination | Fed by | ACCEPTED — C-ENROLL.10.5 — Immutable enrollment input bundle: frozen reference inputs; C-7L.11.1 — Enrollment provisional link type: exact type; C-7L.11.2 — Enrollment provisional link certainty: provisional certainty; C-7L.11.3 — Enrollment provisional link proposal ID: stable query identity; C-7L.11.4 — Enrollment provisional link meaning: collection provenance; C-7L.11.5 — Enrollment provisional link basis: actual authorization basis. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13]; ACCEPTED — C-7L.11.6 — Enrollment proposed input-bundle reference: exact frozen input pointer; C-7L.11.7 — Enrollment confirmed Ness-box reference: confirmed destination; C-7L.11.8 — Enrollment link operation reference: parent; C-7L.11.9 — Enrollment link session reference: collection session; C-7L.11.10 — Enrollment link eligible-reading references: exact reading set; C-7L.11.11 — Enrollment link eligibility-decision references: decisions; C-7L.11.12 — Enrollment link prerequisite-evidence references: owner evidence. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Pending endpoint placement |
| C-7L.11.13 — Enrollment committed-link handoff gate | C-ENROLL.11 — Provisional link and profile coordination | Gated by | ACCEPTED — C-7L.11.13 — Enrollment committed-link handoff gate: current committed link required; C-SIA.20 — Provisional enrollment profile handoff: SIA owns actual profile creation under its rules. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | Pending endpoint placement |
| C-SIA.20 — Provisional enrollment profile handoff | C-ENROLL.11 — Provisional link and profile coordination | Gated by | ACCEPTED — C-7L.11.13 — Enrollment committed-link handoff gate: current committed link required; C-SIA.20 — Provisional enrollment profile handoff: SIA owns actual profile creation under its rules. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | Pending endpoint placement |
| C-7L.11.3 — Enrollment provisional link proposal ID | C-ENROLL.11.1 — Stable link-proposal recovery identity | Fed by | ACCEPTED — C-7L.11.3 — Enrollment provisional link proposal ID: canonical proposal identity; C-7L.11 — Provisional enrollment Person-Box link: actual query result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-7L.11 — Provisional enrollment Person-Box link | C-ENROLL.11.1 — Stable link-proposal recovery identity | Fed by | ACCEPTED — C-7L.11.3 — Enrollment provisional link proposal ID: canonical proposal identity; C-7L.11 — Provisional enrollment Person-Box link: actual query result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SIA.20.2 — Provisional profile commit identity | C-ENROLL.11.2 — Provisional profile-build identity | Fed by | ACCEPTED — C-SIA.20.2 — Provisional profile commit identity: idempotent actual profile result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-7L.11.13 — Enrollment committed-link handoff gate | C-ENROLL.11.2 — Provisional profile-build identity | Gated by | ACCEPTED — C-7L.11.13 — Enrollment committed-link handoff gate: current committed linkage before any build. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SIA.20.3 — Provisional status and access ceiling | C-ENROLL.11.3 — Provisional profile constraints consumed by enrollment | Fed by | ACCEPTED — C-SIA.20.3 — Provisional status and access ceiling: provisional maximum; C-SIA.20.4 — Provisional evidence weighting: the five stronger dimensions; C-SIA.20.5 — Provisional restart boundary: fresh assessment requirement. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | Pending endpoint placement |
| C-SIA.20.4 — Provisional evidence weighting | C-ENROLL.11.3 — Provisional profile constraints consumed by enrollment | Fed by | ACCEPTED — C-SIA.20.3 — Provisional status and access ceiling: provisional maximum; C-SIA.20.4 — Provisional evidence weighting: the five stronger dimensions; C-SIA.20.5 — Provisional restart boundary: fresh assessment requirement. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | Pending endpoint placement |
| C-SIA.20.5 — Provisional restart boundary | C-ENROLL.11.3 — Provisional profile constraints consumed by enrollment | Fed by | ACCEPTED — C-SIA.20.3 — Provisional status and access ceiling: provisional maximum; C-SIA.20.4 — Provisional evidence weighting: the five stronger dimensions; C-SIA.20.5 — Provisional restart boundary: fresh assessment requirement. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | Pending endpoint placement |
| C-SIA.11 — Ordinary voice-training eligibility | C-ENROLL.11.3 — Provisional profile constraints consumed by enrollment | Gated by | DESIGNED — C-SIA.11 — Ordinary voice-training eligibility: all later contributions obey ordinary conditions; C-SACL — Speaker Access-Control Layer (§25.4): its gates alone determine access. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-ENROLL.11.3 — Provisional profile constraints consumed by enrollment | Gated by | DESIGNED — C-SIA.11 — Ordinary voice-training eligibility: all later contributions obey ordinary conditions; C-SACL — Speaker Access-Control Layer (§25.4): its gates alone determine access. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | Pending endpoint placement |
| C-SIA.20.8 — Enrollment authority limits | C-ENROLL.12 — Enrollment authority and privacy limits | Gated by | ACCEPTED — C-SIA.20.8 — Enrollment authority limits: canonical profile authority constraints; C-BOP.15.6 — Protected raw-voice boundary: protected interface and no raw voice in coordination. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]; DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): first final output gate and capture protection; C-SACL — Speaker Access-Control Layer (§25.4): second final output gate; C-9 — Access/authentication model + voice I/O + phone modes (§9): current fence and separate mode-opening authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BOP.15.6 — Protected raw-voice boundary | C-ENROLL.12 — Enrollment authority and privacy limits | Gated by | ACCEPTED — C-SIA.20.8 — Enrollment authority limits: canonical profile authority constraints; C-BOP.15.6 — Protected raw-voice boundary: protected interface and no raw voice in coordination. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]; DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): first final output gate and capture protection; C-SACL — Speaker Access-Control Layer (§25.4): second final output gate; C-9 — Access/authentication model + voice I/O + phone modes (§9): current fence and separate mode-opening authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-ENROLL.12 — Enrollment authority and privacy limits | Gated by | ACCEPTED — C-SIA.20.8 — Enrollment authority limits: canonical profile authority constraints; C-BOP.15.6 — Protected raw-voice boundary: protected interface and no raw voice in coordination. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]; DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): first final output gate and capture protection; C-SACL — Speaker Access-Control Layer (§25.4): second final output gate; C-9 — Access/authentication model + voice I/O + phone modes (§9): current fence and separate mode-opening authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-ENROLL.12 — Enrollment authority and privacy limits | Gated by | ACCEPTED — C-SIA.20.8 — Enrollment authority limits: canonical profile authority constraints; C-BOP.15.6 — Protected raw-voice boundary: protected interface and no raw voice in coordination. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]; DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): first final output gate and capture protection; C-SACL — Speaker Access-Control Layer (§25.4): second final output gate; C-9 — Access/authentication model + voice I/O + phone modes (§9): current fence and separate mode-opening authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-9 — Access/authentication model + voice I/O + phone modes (§9) | C-ENROLL.12 — Enrollment authority and privacy limits | Gated by | ACCEPTED — C-SIA.20.8 — Enrollment authority limits: canonical profile authority constraints; C-BOP.15.6 — Protected raw-voice boundary: protected interface and no raw voice in coordination. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §16]; DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): first final output gate and capture protection; C-SACL — Speaker Access-Control Layer (§25.4): second final output gate; C-9 — Access/authentication model + voice I/O + phone modes (§9): current fence and separate mode-opening authority. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §15] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-ENROLL.13 — Enrollment coordination records and identities | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected reference handling; C-SACL — Speaker Access-Control Layer (§25.4): applicable access limits on records. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-ENROLL.13 — Enrollment coordination records and identities | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected reference handling; C-SACL — Speaker Access-Control Layer (§25.4): applicable access limits on records. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Pending endpoint placement |
| C-SIA.20.7 — Profile-commit enrollment notification | C-ENROLL.14.9 — Provisional profile created enrollment event | Gated by | ACCEPTED — C-SIA.20.7 — Profile-commit enrollment notification: actual commitment must precede this event. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | Pending endpoint placement |
| C-BOP.15.1 — B29 capture and BOP observation ownership | C-ENROLL.15 — Enrollment crash recovery | Fed by | ACCEPTED — C-BOP.15.1 — B29 capture and BOP observation ownership: real observation commits; C-BOP.13.1 — BOP consumption of B11 writer protections: root commitments; C-7L.11 — Provisional enrollment Person-Box link: actual link truth; C-SIA.20.2 — Provisional profile commit identity: actual profile truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] | Pending endpoint placement |
| C-BOP.13.1 — BOP consumption of B11 writer protections | C-ENROLL.15 — Enrollment crash recovery | Fed by | ACCEPTED — C-BOP.15.1 — B29 capture and BOP observation ownership: real observation commits; C-BOP.13.1 — BOP consumption of B11 writer protections: root commitments; C-7L.11 — Provisional enrollment Person-Box link: actual link truth; C-SIA.20.2 — Provisional profile commit identity: actual profile truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] | Pending endpoint placement |
| C-7L.11 — Provisional enrollment Person-Box link | C-ENROLL.15 — Enrollment crash recovery | Fed by | ACCEPTED — C-BOP.15.1 — B29 capture and BOP observation ownership: real observation commits; C-BOP.13.1 — BOP consumption of B11 writer protections: root commitments; C-7L.11 — Provisional enrollment Person-Box link: actual link truth; C-SIA.20.2 — Provisional profile commit identity: actual profile truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] | Pending endpoint placement |
| C-SIA.20.2 — Provisional profile commit identity | C-ENROLL.15 — Enrollment crash recovery | Fed by | ACCEPTED — C-BOP.15.1 — B29 capture and BOP observation ownership: real observation commits; C-BOP.13.1 — BOP consumption of B11 writer protections: root commitments; C-7L.11 — Provisional enrollment Person-Box link: actual link truth; C-SIA.20.2 — Provisional profile commit identity: actual profile truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] | Pending endpoint placement |
| C-BAI.19.1 — Enrollment BAI request interface | C-ENROLL.15.3 — Recovery with BAI pending | Fed by | ACCEPTED — C-BAI.19.1 — Enrollment BAI request interface: BAI's volatile pending boundary. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BAI.19 — Enrollment authorization producer | C-ENROLL.15.4 — Recovery after token issue before final checks | Fed by | ACCEPTED — C-BAI.19 — Enrollment authorization producer: volatile token ownership. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] | Pending endpoint placement |
| C-BAI.19.6 — BAI-owned enrollment success observation | C-ENROLL.15.7 — Recovery before the biometric system-command observation | Fed by | ACCEPTED — C-BAI.19.6 — BAI-owned enrollment success observation: sole source; C-BOP.15.4 — Single enrollment biometric success observation: deterministic receiver identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BOP.15.4 — Single enrollment biometric success observation | C-ENROLL.15.7 — Recovery before the biometric system-command observation | Fed by | ACCEPTED — C-BAI.19.6 — BAI-owned enrollment success observation: sole source; C-BOP.15.4 — Single enrollment biometric success observation: deterministic receiver identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-BOP.15.1 — B29 capture and BOP observation ownership | C-ENROLL.15.9 — Recovery during confirmed capture | Fed by | ACCEPTED — C-BOP.15.1 — B29 capture and BOP observation ownership: actual durable observations and failure truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] | Pending endpoint placement |
| C-BOP.15.1 — B29 capture and BOP observation ownership | C-ENROLL.15.10 — Recovery after observations before close | Fed by | ACCEPTED — C-BOP.15.1 — B29 capture and BOP observation ownership: committed observations. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] | Pending endpoint placement |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | C-ENROLL.15.11 — Recovery after close before Catalog submission | Gated by | DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): standard intake rules. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | C-ENROLL.15.15 — Recovery during partial reading completion | Fed by | DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): actual queue/read outcomes. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] | Pending endpoint placement |
| C-7L.11 — Provisional enrollment Person-Box link | C-ENROLL.15.17 — Recovery after link-proposal submission | Fed by | ACCEPTED — C-7L.11 — Provisional enrollment Person-Box link: owns the queried outcome. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] | Pending endpoint placement |
| C-7L.11.13 — Enrollment committed-link handoff gate | C-ENROLL.15.18 — Recovery after link commit before profile creation | Gated by | ACCEPTED — C-7L.11.13 — Enrollment committed-link handoff gate: current committed truth. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Pending endpoint placement |
| C-SIA.20.2 — Provisional profile commit identity | C-ENROLL.15.19 — Recovery during SIA profile creation | Fed by | ACCEPTED — C-SIA.20.2 — Provisional profile commit identity: actual recoverable SIA result. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §21] | Pending endpoint placement |
| C-BAI.19.1 — Enrollment BAI request interface | C-ENROLL.16.2 — Fresh enrollment-session requirements | Fed by | ACCEPTED — C-ENROLL.3.1 — Durable explicit-begin event: new choice; C-ENROLL.2 — Six-owner prerequisite check: fresh checks; C-BAI.19.1 — Enrollment BAI request interface: new pending and fresh token; C-ENROLL.3.3 — Prospective enrollment session identity: new reserved identity. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §22] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-ENROLL.9.7 — Immutable enrollment segment identity | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH08-a. |
| C-SIA — Speaker Identity Assessment (§25.3) | C-ENROLL.9.7 — Immutable enrollment segment identity | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH09-c. |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-ENROLL.9.7 — Immutable enrollment segment identity | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH09-d. |
| C-BAI — Biometric Authorization Interface (§25.6) | C-ENROLL.9.7 — Immutable enrollment segment identity | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH09-e. |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-ENROLL.9.8 — Per-segment eligibility decision record | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH08-a. |
| C-SIA — Speaker Identity Assessment (§25.3) | C-ENROLL.9.8 — Per-segment eligibility decision record | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH09-c. |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-ENROLL.9.8 — Per-segment eligibility decision record | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH09-d. |
| C-BAI — Biometric Authorization Interface (§25.6) | C-ENROLL.9.8 — Per-segment eligibility decision record | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH09-e. |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-ENROLL.13.1 — Enrollment parent operation record | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH08-a. |
| C-SIA — Speaker Identity Assessment (§25.3) | C-ENROLL.13.1 — Enrollment parent operation record | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH09-c. |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-ENROLL.13.1 — Enrollment parent operation record | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH09-d. |
| C-BAI — Biometric Authorization Interface (§25.6) | C-ENROLL.13.1 — Enrollment parent operation record | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH09-e. |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-ENROLL.13.2 — Enrollment stage checkpoint | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH08-a. |
| C-SIA — Speaker Identity Assessment (§25.3) | C-ENROLL.13.2 — Enrollment stage checkpoint | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH09-c. |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-ENROLL.13.2 — Enrollment stage checkpoint | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH09-d. |
| C-BAI — Biometric Authorization Interface (§25.6) | C-ENROLL.13.2 — Enrollment stage checkpoint | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH09-e. |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-ENROLL.13.3 — Enrollment recovery operation and event | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH08-a. |
| C-SIA — Speaker Identity Assessment (§25.3) | C-ENROLL.13.3 — Enrollment recovery operation and event | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH09-c. |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-ENROLL.13.3 — Enrollment recovery operation and event | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH09-d. |
| C-BAI — Biometric Authorization Interface (§25.6) | C-ENROLL.13.3 — Enrollment recovery operation and event | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §17] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH09-e. |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-ENROLL.13.4 — Absorbed enrollment duplicate record | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH08-a. |
| C-SIA — Speaker Identity Assessment (§25.3) | C-ENROLL.13.4 — Absorbed enrollment duplicate record | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH09-c. |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-ENROLL.13.4 — Absorbed enrollment duplicate record | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH09-d. |
| C-BAI — Biometric Authorization Interface (§25.6) | C-ENROLL.13.4 — Absorbed enrollment duplicate record | Gated by | ACCEPTED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q), C-SIA — Speaker Identity Assessment (§25.3), C-SACL — Speaker Access-Control Layer (§25.4), C-BAI — Biometric Authorization Interface (§25.6): the record is used only under §7Q privacy and §25 identity and security authorization. [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §20] | Reciprocal USED BY row added in CH09-e. |

## Cross-piece TOGETHER continuations for current uses

Each row identifies one current USED BY place. Existing reciprocal fields are credited only where inspected; other rows remain explicit continuation obligations, without inventing the future card’s box.

| Current USED BY owner | Using endpoint / path | Current use row | Source | Disposition |
|---|---|---|---|---|
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-7L.11 — Provisional enrollment Person-Box link | 1 · ACCEPTED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | Existing TOGETHER relationship checked in earlier card |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-7L.11.6 — Enrollment proposed input-bundle reference | 2 · ACCEPTED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] | Existing TOGETHER relationship checked in earlier card |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-7L.11.8 — Enrollment link operation reference | 3 · ACCEPTED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Existing TOGETHER relationship checked in earlier card |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-7L.11.9 — Enrollment link session reference | 4 · ACCEPTED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Existing TOGETHER relationship checked in earlier card |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-7L.11.10 — Enrollment link eligible-reading references | 5 · ACCEPTED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Existing TOGETHER relationship checked in earlier card |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-7L.11.11 — Enrollment link eligibility-decision references | 6 · ACCEPTED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Existing TOGETHER relationship checked in earlier card |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-7L.11.12 — Enrollment link prerequisite-evidence references | 7 · ACCEPTED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §13] | Existing TOGETHER relationship checked in earlier card |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-BOP.15.4 — Single enrollment biometric success observation | 8 · ACCEPTED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Existing TOGETHER relationship checked in earlier card |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-BOP.15.5 — Frozen enrollment capture set and normal entry | 9 · ACCEPTED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §10] | Existing TOGETHER relationship checked in earlier card |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-BAI — Biometric Authorization Interface (§25.6) | 10 · DESIGNED | [V10 §25.6] | Existing TOGETHER relationship checked in earlier card |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-BAI.3.9.3 — Ness enrollment purpose | 11 · DESIGNED | [V10 §25.11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §4] | Existing TOGETHER relationship checked in earlier card |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-BAI.19 — Enrollment authorization producer | 12 · ACCEPTED | [V10 §25.11] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §5] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6] | Existing TOGETHER relationship checked in earlier card |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-BAI.19.4 — Enrollment proof binding without new authority | 13 · ACCEPTED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6] | Existing TOGETHER relationship checked in earlier card |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-BAI.19.5 — Enrollment consumed-proof crash boundary | 14 · ACCEPTED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §6] | Existing TOGETHER relationship checked in earlier card |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-BAI.19.6 — BAI-owned enrollment success observation | 15 · ACCEPTED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Existing TOGETHER relationship checked in earlier card |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-SIA.20 — Provisional enrollment profile handoff | 16 · ACCEPTED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12A] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] | Existing TOGETHER relationship checked in earlier card |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-SIA.20.1 — Eligible enrollment reading input | 17 · ACCEPTED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §12] | Existing TOGETHER relationship checked in earlier card |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-SIA.20.2 — Provisional profile commit identity | 18 · ACCEPTED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §19] | Existing TOGETHER relationship checked in earlier card |
| C-ENROLL — Initial Ness voice-profile enrollment (§25.11) | C-SIA.20.7 — Profile-commit enrollment notification | 19 · ACCEPTED | [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §14] [04/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md §18] | Existing TOGETHER relationship checked in earlier card |

## Source-to-card coverage added by CH09-h

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| V10 §25.11; Map C-ENROLL | C-ENROLL retains the exact Map name and DESIGNED status. Full initial enrollment flow is placed through .1–.16; specialist authorities remain separate. All 22 earlier incoming fields across 19 places are reciprocated; all 13 inspected earlier uses receive root relationships. |
| V10 §25.11 / Prerequisites; B-INT-7 v1.1 §4 | C-ENROLL.2 and .2.1–.2.6 place all six conditions. Pairing facts reuse C-PAIR.1.2.1/.1.2.2/.1.4.1/.1.4.2/.1.6/.2.3/.5.1; SIA/SACL own spoofing and Gate 0; C-7L.4 owns confirmed Ness-box truth. |
| B-INT-7 §4 snapshot and §19 I2 | C-ENROLL.2.7 and its children: snapshot_id, snapshot_version, six per-owner entries, owner_ref, owner_version/current event identity, satisfied, taken_at and boolean all_six_satisfied. C-ENROLL.2.8 owns the operation_ref request seam. No snapshot becomes authority; failed initial checks prevent the BAI call. |
| B-INT-7 §3 | C-ENROLL.1 owns coordination only. Phone, recovery, QR, spoofing, box, biometric session, identity/access, privacy, root, queue and profile authority remain at their actual owners; outer trusted-phone binding and inner biometric approval are not named identity. |
| B-INT-7 §5 steps 1–3; §17; §19 I1 | C-ENROLL.3/.3.1–.3.5: dedicated trusted-phone flow, explicit_begin_event_ref, trusted_phone_binding_ref, stable proposed parent and prospective session identities, proposed begin claim, no authority from reservation, anti-double-tap identity and refusal/recovery outcomes. |
| B-INT-7 §5 steps 4–10; §19 I3/I4 | C-ENROLL.4/.4.1/.4.2/.4.4: full ordered request, BAI-only pending/prompt/token, immediately fresh owner recheck, revocation without consumption on change, verified flushed proof then opening then capture. Exact purpose/requester/operation_ref/session_ref and pending_id/refusal/token_ref/failure forms are present. Existing C-BAI.19.1–.19.4 remain canonical authorization/proof owners. |
| B-INT-7 §6A | C-ENROLL.4.3 and eleven field cards carry the complete durable chain and binding: proposed operation/session IDs; separate token/pending refs; exact purpose; app_session_key_ref; snapshot ref; BAI trusted-local timestamps; requester; audit schema/version; integrity reference. The proposed append-only companion references the BAI event and is referenced by that event or opening. No secrets or new biometric authority. |
| B-INT-7 §6B | C-ENROLL.4.5 and eight children place every duplicate barrier: one begin/two sessions, two proofs/one session, one proof/two sessions, old unmatched result, changed prerequisite, absent flushed proof, stale snapshot and concurrent BAI pending. |
| B-INT-7 §6C; receipt §6 wording note 2 | C-ENROLL.4.6/.4.7 and .6.14 preserve no-session spent-proof abort versus an actually opened session with confirmed zero capture. The former uses the proposed abort event, never a fictitious session-close event; both prohibit silent microphone activation. |
| B-INT-7 §6D; §19 I5A | C-ENROLL.5/.5.1–.5.5: current opening/privacy/security/no-stop conjunction; flushed proposed intent before request; seven reference-only request classes, each placed; exact started/confirmed_not_started/unknown results, separately placed; B29-sourced proposed start fact. Intent, start and observations remain distinct, with every stated crash outcome and no inferred non-start. |
| B-INT-7 §7; V10 §25.11 BOP Integration; §25.12; §19 I5B/I5C | C-ENROLL.5.3.5/.5.6/.5.7 consume canonical C-BOP.15 and C-BAI.19.6. role=ness is declared; source_title=enrollment:ness:<session_id>; session_authorization.authorization_type=enrollment_declared is formally adopted. Exactly one BAI-sourced biometric:result:success observation with session ID and trusted-local timestamp; deterministic capture_id from session/opening/command. Canonical C-BOP.15.3.1/.15.3.2 retain the two fields; forbidden purpose/token/biometric/authorization/identity payloads remain absent. |
| B-INT-7 §7 A15 boundary | C-ENROLL.5.6 names C-BOP.12, the already placed six-field/five-name acoustic-condition amendment owner. Those atoms remain there; h preserves physical context only and all ten prohibited conclusions: identity, speaker change, spoofing, imitation risk, emotion, intent, meaning, importance, behavioral pattern and causation. |
| B-INT-7 §8 | C-ENROLL.6.1–.6.27 place all 27 exact proposed state labels, splitting both combined table pairs. Every entry fact, actual owner and outcome is written. The combined closing/closed source condition is preserved without inventing an intermediate commit rule. |
| B-INT-7 §8A/§8B | C-ENROLL.6.28/.6.29: separate capture-session/parent lifecycles; valid unaffected material can continue after closure/interruption; only legal nonterminal transitions; no regression of committed observations/roots/readings/eligibility/link/profile; absorbing parent terminals; at most one winner; no state inferred from coordination. The source's abort shorthand is bounded by §6C and the receipt. |
| B-INT-7 §9 | C-ENROLL.7/.7.1–.7.8 place all eight owner-event groups, explicitly retaining loss/replacement/revocation, recovery/setup and QR/secret alternatives. Stop precedes logging; only committed observations are preserved; no reconstruction or affected-segment training; honest closure/interruption; no same-session resumption; no TSC lifecycle/database/archive authority reuse. |
| B-INT-7 §10; §19 I6–I9 | C-ENROLL.8/.8.1–.8.4 carry all ten close/freeze/Catalog/B11/append/duplicate/root_id/queue/quarantine steps. I6 actual observations to immutable set; I7 frozen capture_ids+provenance and accepted/rejected/blocked; I8 capture_id-derived identity+validated root fields+ingest_operation_id and root_id/append_duplicate_absorbed/rejected/indeterminate; I9 root_id/enqueued. Canonical C-BOP.13.1, C-STORE.3.5/.4.6.2.1/.4.6.2.3, C-7E, C-7GA and C-READ.11 retain their existing schema/fence/queue atoms. No duplicate writer or queue is introduced. |
| B-INT-7 §11; §19 I10 | C-ENROLL.9/.9.1–.9.6 carry all six checks; .9.6.1–.9.6.5 carry every stream-integrity condition, including threshold over the FULL segment. Authorization requires enrollment_declared plus session_id linked to confirmed durable bai_token_consumed. overall_completeness is exactly complete or partial. Stream consistency never establishes who spoke. |
| B-INT-7 §§11/17/20 | C-ENROLL.9.7/.9.8 and field children place proposed immutable segment and eligibility-decision identities, one outcome per segment, accepted/rejected event mirroring, reason and source references without audio. Replay recovers the prior decision; rejection preserves roots and prevents training. |
| B-INT-7 §12; §19 I11 | C-ENROLL.10/.10.1–.10.4: accepted quarantine readings only; counted_reading_refs set keyed by reading identity; each eligibility-decision ref; readiness outcome; unavailable-rule, unverifiable-set and missing-decision failures; no numbers/durations/thresholds/algorithms; no rejected-as-valid or invented insufficient_context reading; no A29 substitution; no link/profile if not ready. |
| B-INT-7 §12A; §17 | C-ENROLL.10.5 and five permitted input classes: exact eligible accepted reading refs, eligibility decisions, operation/session refs, prerequisite/authorization evidence, readiness ref. One proposed immutable bundle per readiness outcome; recover the same bundle on replay. Coordination only, no profile/store/identity evidence. |
| B-INT-7 §13; §19 I12; V10 §25.12 | C-ENROLL.11/.11.1 use all canonical C-7L.11 field owners by exact name: link_type=enrollment_material_provisional, certainty=enrollment_provisional, proposed stable proposal ID, provenance-only meaning, three-part basis, bundle/confirmed box/operation/session/readings/eligibility/prerequisite references. Proposal recorded is separate from committed/refused/pending outcome; current committed link required; refused/pending/stale/contradictory/unverifiable outcomes remain individually owned in C-7L.11.13.1–.13.6. |
| B-INT-7 §14; §17; §19 I13 | C-ENROLL.11.2/.11.3 and canonical C-SIA.20 retain the proposed idempotent build identity keyed to committed link+linked reading set, SIA-owned commitment before creation event, enrollment_provisional status, recognized_ness ceiling without grant, five dimensions weighted above acoustic until enrollment_active, ordinary later training and unknown/guest restart. C-ENROLL.6.25 requires both commits and both enrollment events for completion. |
| B-INT-7 §§15/16; §19 I14; B-INT-5 §5B | C-ENROLL.12 reuses C-SIA.20.8/C-BOP.15.6 and names privacy/SACL/mode gates. All enrollment-alone authority prohibitions are written; privacy precedes capture; minimum protected raw-voice boundary; references/structural facts only; no ordinary-component sensitive payload merely for rejection; no indirect disclosure or reconstructive logs; final privacy-first/access-second/fence-revalidated output. Enrollment purpose never opens Personal Mode. |
| B-INT-7 §17, all 17 identity rows | Proposed parent/session/begin claim .3; BAI pending/token C-BAI.19.1; snapshot .2.7; proposed segment and decision .9.7/.9.8; BOP capture_id and B11 ingest_operation_id .8.3 with canonical owners; queue/read refs .8.4; proposed readiness .10; proposed bundle .10.5; proposed proposal ID .11.1; proposed build identity .11.2; capture-control/intent/start .5; proposed recovery identity .13.3.1. One-parent/many-children/no-extra-weight rule .13. |
| B-INT-7 §18 | C-ENROLL.14 and nine event children preserve every exact settled enrollment event. Additional proposed abort/intent/B29-start names remain separate at .4.6/.5.2/.5.5, not mislabeled settled events. BAI and every other owner keep their events. Required write/flush precedes owner success; .16.3 handles failure. |
| B-INT-7 §20, all 13 proposed record kinds | Intent .5.2; bundle .10.5; parent operation .13.1 with identity/state/terminal reason/audit-ref atoms; stage event .13.2; begin claim .3.4; snapshot .2.7; authorization binding .4.3; capture set .8.1; segment .9.7; eligibility decision .9.8; readiness .10; recovery event .13.3 with identity/boundary atoms; duplicate absorbed .13.4. All are append-only reference-only non-authorities with no evidence weight. |
| B-INT-7 §21, every crash row | C-ENROLL.15.1–.15.7 map source rows 1–7; .15.8 maps inserted row 7b; .15.9–.15.21 map rows 8–20. Every committed-truth and exact recovery action is written. The table has 21 rows despite §20/§26 saying twenty; no row is omitted. I5C preserves BAI as sole recovered biometric-observation source. |
| B-INT-7 §22 | C-ENROLL.16/.16.1/.16.2: same-parent technical retry only when no fresh explicit action and no recreated security authority; all seven prohibited reuse classes; five fresh-session requirements; accepted B9 values consumed by reference with none invented. |
| B-INT-7 §23, all 16 failure groups | Bad prerequisite .2; pending conflict .4.5.8; unmatched result .4.5.4; unflushed proof .4.5.6; unverifiable binding .4.3; changed prerequisite .4.2; absent/current opening .5.1/.5.3.3; unsafe BOP capture .5.3.6/.5.6; privacy exclusion .7.7; Catalog nonacceptance .8.2; unverified append .8.3; unavailable eligibility owner .9; readiness failure .10.4; unavailable Person-Box/SIA .11; owner contradiction .15.21; required audit failure .16.3. Each outcome is explicit in the owning card; .16 retains the complete named list. |
| B-INT-7 §§0–2/24–26 and closure receipt whole | Authority/version/dependency and drafting/implementation instructions are provenance or excluded project workflow. System boundaries from §24 are placed in .1/.5/.8/.9/.11/.12/.13; still-open mechanics in §25 are explicitly assigned to CH09-i or remain unchosen. Receipt's three frozen minor notes and the actual 1066-line count are preserved in delivery records; no source is edited and no independent audit is claimed. |
| Full Bundle 5 consolidation v1.1 | Its enrollment scope and cross-package authority table support explicit begin plus BAI token, actual specialist owners, one-reference recordkeeping and no substituted authority. Other consolidated policy/mechanical details retain canonical earlier C-7Q/C-24/C-TSC/C-SACL/C-BAI/C-PAIR owners; full Personal Mode remains CH09-i. Receipt/history/closeout prose is excluded from behavior. |
| Companion embedded security §§11–12 | Header conflict retains V10 permanent QR/secret inertness instead of Companion destruction. Formally adopted enrollment_declared and enrollment_material_provisional vocabulary is placed through canonical BOP/Person-Box owners, without a second schema or older destructive behavior. |
| 04/05 discovery by C-ENROLL, full name, enrollment and bootstrap topics | All 15 matched paths classified. B-INT-7 and Bundle 5 read whole. B11 bootstrap hits describe historical sealed-batch registration, not enrollment; its root path is consumed through earlier canonical owners. Kernel dependency-list hit adds no new enrollment rule; full kernel CH10-b. Highest decision index v0_11 is navigation; v0_5/v0_6/v0_10 hits are superseded navigation. |
| Active decision/candidate matches | Synthetic-voice decision v0_2 reread whole: selected output voice is distinct from identity/enrollment; speech choices land CH09-i. Recovery buckets Group 6 is bootstrap reading and memory health, not voice capture, with no new archive use here. B16 EEB v1_7 §2.10 cites enrollment as an authority example and changes no enrollment policy; promotion/judgment rules retain earlier ownership. |
| Remaining owners and holes | Complete modes and still-open B29 mechanics CH09-i; full model/B24/kernel CH10-b; side-path assembly CH11; final script-generated registers CH12. No new prompt wording, sample/duration/quality/diarization/spoofing/readiness/activation value, hardware, channel, cleanup algorithm or serialization is selected. Gaps in this piece remain exact NOT DECIDED. |

## Appendix A carry-forward — this piece

| Part | Field |
|---|---|
| C-ENROLL.1 — Enrollment coordination boundary | Gated by |
| C-ENROLL.1 — Enrollment coordination boundary | Changes |
| C-ENROLL.2 — Six-owner prerequisite check | Gated by |
| C-ENROLL.2 — Six-owner prerequisite check | Changes |
| C-ENROLL.2.1 — Final owner-phone prerequisite | Gated by |
| C-ENROLL.2.1 — Final owner-phone prerequisite | Changes |
| C-ENROLL.2.2 — Completed first-code prerequisite | Gated by |
| C-ENROLL.2.2 — Completed first-code prerequisite | Changes |
| C-ENROLL.2.3 — Inert initial-material prerequisite | Gated by |
| C-ENROLL.2.3 — Inert initial-material prerequisite | Changes |
| C-ENROLL.2.4 — Finalized setup prerequisite | Gated by |
| C-ENROLL.2.4 — Finalized setup prerequisite | Changes |
| C-ENROLL.2.5 — Clean current spoofing prerequisite | Gated by |
| C-ENROLL.2.5 — Clean current spoofing prerequisite | Changes |
| C-ENROLL.2.6 — Confirmed Ness-box prerequisite | Gated by |
| C-ENROLL.2.6 — Confirmed Ness-box prerequisite | Changes |
| C-ENROLL.2.7 — Versioned prerequisite snapshot | Gated by |
| C-ENROLL.2.7 — Versioned prerequisite snapshot | Changes |
| C-ENROLL.2.7.1 — Snapshot identity | Fails closed by |
| C-ENROLL.2.7.1 — Snapshot identity | Gated by |
| C-ENROLL.2.7.1 — Snapshot identity | Changes |
| C-ENROLL.2.7.2 — Snapshot version | Fails closed by |
| C-ENROLL.2.7.2 — Snapshot version | Gated by |
| C-ENROLL.2.7.2 — Snapshot version | Changes |
| C-ENROLL.2.7.3 — Per-prerequisite owner entry | Gated by |
| C-ENROLL.2.7.3 — Per-prerequisite owner entry | Changes |
| C-ENROLL.2.7.3.1 — Prerequisite owner reference | Fails closed by |
| C-ENROLL.2.7.3.1 — Prerequisite owner reference | Gated by |
| C-ENROLL.2.7.3.1 — Prerequisite owner reference | Changes |
| C-ENROLL.2.7.3.2 — Prerequisite owner version | Fails closed by |
| C-ENROLL.2.7.3.2 — Prerequisite owner version | Gated by |
| C-ENROLL.2.7.3.2 — Prerequisite owner version | Changes |
| C-ENROLL.2.7.3.3 — Prerequisite satisfaction result | Gated by |
| C-ENROLL.2.7.3.3 — Prerequisite satisfaction result | Changes |
| C-ENROLL.2.7.4 — Snapshot check time | Must never |
| C-ENROLL.2.7.4 — Snapshot check time | Fails closed by |
| C-ENROLL.2.7.4 — Snapshot check time | Gated by |
| C-ENROLL.2.7.4 — Snapshot check time | Changes |
| C-ENROLL.2.7.5 — All-six satisfaction boolean | Gated by |
| C-ENROLL.2.7.5 — All-six satisfaction boolean | Changes |
| C-ENROLL.2.8 — Prerequisite-check operation reference | Fails closed by |
| C-ENROLL.2.8 — Prerequisite-check operation reference | Gated by |
| C-ENROLL.2.8 — Prerequisite-check operation reference | Changes |
| C-ENROLL.3 — Explicit enrollment beginning | Changes |
| C-ENROLL.3.1 — Durable explicit-begin event | Gated by |
| C-ENROLL.3.1 — Durable explicit-begin event | Changes |
| C-ENROLL.3.2 — Stable enrollment operation identity | Fails closed by |
| C-ENROLL.3.2 — Stable enrollment operation identity | Gated by |
| C-ENROLL.3.2 — Stable enrollment operation identity | Changes |
| C-ENROLL.3.3 — Prospective enrollment session identity | Gated by |
| C-ENROLL.3.3 — Prospective enrollment session identity | Changes |
| C-ENROLL.3.4 — One-begin coordination claim | Gated by |
| C-ENROLL.3.4 — One-begin coordination claim | Changes |
| C-ENROLL.3.5 — Begin request phone-binding reference | Gated by |
| C-ENROLL.3.5 — Begin request phone-binding reference | Changes |
| C-ENROLL.4 — Ordered authorization and opening | Changes |
| C-ENROLL.4.1 — Enrollment BAI request fields | Changes |
| C-ENROLL.4.3 — Durable authorization chain and binding | Gated by |
| C-ENROLL.4.3 — Durable authorization chain and binding | Changes |
| C-ENROLL.4.3.1 — Bound operation identity | Gated by |
| C-ENROLL.4.3.1 — Bound operation identity | Changes |
| C-ENROLL.4.3.2 — Bound session identity | Gated by |
| C-ENROLL.4.3.2 — Bound session identity | Changes |
| C-ENROLL.4.3.3 — Bound token reference | Gated by |
| C-ENROLL.4.3.3 — Bound token reference | Changes |
| C-ENROLL.4.3.4 — Bound pending-record reference | Gated by |
| C-ENROLL.4.3.4 — Bound pending-record reference | Changes |
| C-ENROLL.4.3.5 — Bound enrollment purpose | Gated by |
| C-ENROLL.4.3.5 — Bound enrollment purpose | Changes |
| C-ENROLL.4.3.6 — Bound hardware phone key reference | Gated by |
| C-ENROLL.4.3.6 — Bound hardware phone key reference | Changes |
| C-ENROLL.4.3.7 — Bound prerequisite-snapshot reference | Gated by |
| C-ENROLL.4.3.7 — Bound prerequisite-snapshot reference | Changes |
| C-ENROLL.4.3.8 — Bound trusted-local timestamps | Gated by |
| C-ENROLL.4.3.8 — Bound trusted-local timestamps | Changes |
| C-ENROLL.4.3.9 — Bound requester identity | Gated by |
| C-ENROLL.4.3.9 — Bound requester identity | Changes |
| C-ENROLL.4.3.10 — Bound audit schema and version | Gated by |
| C-ENROLL.4.3.10 — Bound audit schema and version | Changes |
| C-ENROLL.4.3.11 — Bound audit integrity reference | Gated by |
| C-ENROLL.4.3.11 — Bound audit integrity reference | Changes |
| C-ENROLL.4.5 — Opening duplicate barriers | Gated by |
| C-ENROLL.4.5 — Opening duplicate barriers | Changes |
| C-ENROLL.4.5.1 — Duplicate-begin barrier | Fed by |
| C-ENROLL.4.5.1 — Duplicate-begin barrier | Changes |
| C-ENROLL.4.5.2 — Second-proof same-session barrier | Gated by |
| C-ENROLL.4.5.2 — Second-proof same-session barrier | Changes |
| C-ENROLL.4.5.3 — Same-proof second-session barrier | Gated by |
| C-ENROLL.4.5.3 — Same-proof second-session barrier | Changes |
| C-ENROLL.4.5.4 — Unmatched biometric-result barrier | Gated by |
| C-ENROLL.4.5.4 — Unmatched biometric-result barrier | Changes |
| C-ENROLL.4.5.5 — Changed-prerequisite consumption barrier | Gated by |
| C-ENROLL.4.5.5 — Changed-prerequisite consumption barrier | Changes |
| C-ENROLL.4.5.6 — Missing durable-proof barrier | Fed by |
| C-ENROLL.4.5.6 — Missing durable-proof barrier | Changes |
| C-ENROLL.4.5.7 — Stale-snapshot barrier | Gated by |
| C-ENROLL.4.5.7 — Stale-snapshot barrier | Changes |
| C-ENROLL.4.5.8 — Concurrent BAI-pending barrier | Fed by |
| C-ENROLL.4.5.8 — Concurrent BAI-pending barrier | Changes |
| C-ENROLL.4.6 — Spent proof without an opened session | Gated by |
| C-ENROLL.4.6 — Spent proof without an opened session | Changes |
| C-ENROLL.4.7 — Opened session with confirmed zero capture | Gated by |
| C-ENROLL.4.7 — Opened session with confirmed zero capture | Changes |
| C-ENROLL.5 — Capture-control and observation boundary | Changes |
| C-ENROLL.5.1 — Current capture preconditions | Changes |
| C-ENROLL.5.2 — Durable capture intent | Fed by |
| C-ENROLL.5.2 — Durable capture intent | Changes |
| C-ENROLL.5.3.1 — Capture operation reference | Fails closed by |
| C-ENROLL.5.3.1 — Capture operation reference | Gated by |
| C-ENROLL.5.3.1 — Capture operation reference | Changes |
| C-ENROLL.5.3.2 — Capture session reference | Gated by |
| C-ENROLL.5.3.2 — Capture session reference | Changes |
| C-ENROLL.5.3.3 — Capture opening-commit reference | Gated by |
| C-ENROLL.5.3.3 — Capture opening-commit reference | Changes |
| C-ENROLL.5.3.4 — Capture privacy-decision reference | Fed by |
| C-ENROLL.5.3.4 — Capture privacy-decision reference | Changes |
| C-ENROLL.5.3.5 — Capture declared-provenance references | Fails closed by |
| C-ENROLL.5.3.5 — Capture declared-provenance references | Gated by |
| C-ENROLL.5.3.5 — Capture declared-provenance references | Changes |
| C-ENROLL.5.3.6 — Capture destination observation context | Gated by |
| C-ENROLL.5.3.6 — Capture destination observation context | Changes |
| C-ENROLL.5.3.7 — Capture cancellation and stop references | Gated by |
| C-ENROLL.5.3.7 — Capture cancellation and stop references | Changes |
| C-ENROLL.5.4 — B29 capture-start result | Gated by |
| C-ENROLL.5.4 — B29 capture-start result | Changes |
| C-ENROLL.5.4.1 — Confirmed capture start | Gated by |
| C-ENROLL.5.4.1 — Confirmed capture start | Changes |
| C-ENROLL.5.4.2 — Confirmed capture non-start | Gated by |
| C-ENROLL.5.4.2 — Confirmed capture non-start | Changes |
| C-ENROLL.5.4.3 — Unknown capture-start reality | Gated by |
| C-ENROLL.5.4.3 — Unknown capture-start reality | Changes |
| C-ENROLL.5.5 — B29-sourced capture-start fact | Gated by |
| C-ENROLL.5.5 — B29-sourced capture-start fact | Changes |
| C-ENROLL.5.6 — Enrollment physical-observation consumption | Changes |
| C-ENROLL.5.7 — Enrollment biometric-observation timing | Changes |
| C-ENROLL.6 — Enrollment process lifecycle | Gated by |
| C-ENROLL.6 — Enrollment process lifecycle | Changes |
| C-ENROLL.6.1 — Requested process state | Gated by |
| C-ENROLL.6.1 — Requested process state | Changes |
| C-ENROLL.6.2 — Initial prerequisites verified state | Gated by |
| C-ENROLL.6.2 — Initial prerequisites verified state | Changes |
| C-ENROLL.6.3 — Biometric pending process state | Gated by |
| C-ENROLL.6.3 — Biometric pending process state | Changes |
| C-ENROLL.6.4 — Token issued process state | Gated by |
| C-ENROLL.6.4 — Token issued process state | Changes |
| C-ENROLL.6.5 — Prerequisites rechecked state | Gated by |
| C-ENROLL.6.5 — Prerequisites rechecked state | Changes |
| C-ENROLL.6.6 — Token durably consumed state | Gated by |
| C-ENROLL.6.6 — Token durably consumed state | Changes |
| C-ENROLL.6.7 — Session opened process state | Gated by |
| C-ENROLL.6.7 — Session opened process state | Changes |
| C-ENROLL.6.8 — Capture intent flushed state | Gated by |
| C-ENROLL.6.8 — Capture intent flushed state | Changes |
| C-ENROLL.6.9 — Capturing process state | Gated by |
| C-ENROLL.6.9 — Capturing process state | Changes |
| C-ENROLL.6.10 — Capture start unknown state | Gated by |
| C-ENROLL.6.10 — Capture start unknown state | Changes |
| C-ENROLL.6.11 — Closing process state | Gated by |
| C-ENROLL.6.11 — Closing process state | Changes |
| C-ENROLL.6.12 — Closed process state | Gated by |
| C-ENROLL.6.12 — Closed process state | Changes |
| C-ENROLL.6.13 — Interrupted process state | Gated by |
| C-ENROLL.6.13 — Interrupted process state | Changes |
| C-ENROLL.6.14 — Aborted before capture process state | Gated by |
| C-ENROLL.6.14 — Aborted before capture process state | Changes |
| C-ENROLL.6.15 — Roots pending submission state | Gated by |
| C-ENROLL.6.15 — Roots pending submission state | Changes |
| C-ENROLL.6.16 — Roots partially committed state | Gated by |
| C-ENROLL.6.16 — Roots partially committed state | Changes |
| C-ENROLL.6.17 — Roots committed state | Gated by |
| C-ENROLL.6.17 — Roots committed state | Changes |
| C-ENROLL.6.18 — Readings pending state | Gated by |
| C-ENROLL.6.18 — Readings pending state | Changes |
| C-ENROLL.6.19 — Readings partially completed state | Gated by |
| C-ENROLL.6.19 — Readings partially completed state | Changes |
| C-ENROLL.6.20 — Profile readiness pending state | Gated by |
| C-ENROLL.6.20 — Profile readiness pending state | Changes |
| C-ENROLL.6.21 — Input bundle created state | Gated by |
| C-ENROLL.6.21 — Input bundle created state | Changes |
| C-ENROLL.6.22 — Provisional link proposed state | Gated by |
| C-ENROLL.6.22 — Provisional link proposed state | Changes |
| C-ENROLL.6.23 — Provisional link committed state | Gated by |
| C-ENROLL.6.23 — Provisional link committed state | Changes |
| C-ENROLL.6.24 — Provisional profile created state | Gated by |
| C-ENROLL.6.24 — Provisional profile created state | Changes |
| C-ENROLL.6.25 — Completed parent state | Gated by |
| C-ENROLL.6.25 — Completed parent state | Changes |
| C-ENROLL.6.26 — Blocked parent state | Gated by |
| C-ENROLL.6.26 — Blocked parent state | Changes |
| C-ENROLL.6.27 — Failed parent state | Gated by |
| C-ENROLL.6.27 — Failed parent state | Changes |
| C-ENROLL.6.28 — Separate session and parent lifecycles | Gated by |
| C-ENROLL.6.28 — Separate session and parent lifecycles | Changes |
| C-ENROLL.6.29 — Legal transition and terminal rules | Gated by |
| C-ENROLL.6.29 — Legal transition and terminal rules | Changes |
| C-ENROLL.7 — Mid-session protective stop | Gated by |
| C-ENROLL.7.1 — Trusted-phone safety changes | Gated by |
| C-ENROLL.7.1 — Trusted-phone safety changes | Changes |
| C-ENROLL.7.2 — Invalid recovery or setup safety change | Gated by |
| C-ENROLL.7.2 — Invalid recovery or setup safety change | Changes |
| C-ENROLL.7.3 — Initial-material integrity contradiction | Gated by |
| C-ENROLL.7.3 — Initial-material integrity contradiction | Changes |
| C-ENROLL.7.4 — Spoofing safety change | Gated by |
| C-ENROLL.7.4 — Spoofing safety change | Changes |
| C-ENROLL.7.5 — Person-Box prerequisite safety change | Gated by |
| C-ENROLL.7.5 — Person-Box prerequisite safety change | Changes |
| C-ENROLL.7.6 — BAI or session integrity failure | Gated by |
| C-ENROLL.7.6 — BAI or session integrity failure | Changes |
| C-ENROLL.7.7 — Privacy capture-exclusion safety change | Fed by |
| C-ENROLL.7.7 — Privacy capture-exclusion safety change | Changes |
| C-ENROLL.7.8 — Application or machine restart safety change | Gated by |
| C-ENROLL.7.8 — Application or machine restart safety change | Changes |
| C-ENROLL.8.1 — Frozen enrollment capture-set record | Changes |
| C-ENROLL.8.2 — Catalog submission interface | Changes |
| C-ENROLL.8.3 — B11 append interface | Changes |
| C-ENROLL.8.4 — Root-identity reading enqueue | Changes |
| C-ENROLL.9 — Initial-corpus eligibility gate | Gated by |
| C-ENROLL.9 — Initial-corpus eligibility gate | Changes |
| C-ENROLL.9.1 — Consistent live-speaker stream check | Gated by |
| C-ENROLL.9.1 — Consistent live-speaker stream check | Changes |
| C-ENROLL.9.2 — Segment spoofing check | Gated by |
| C-ENROLL.9.2 — Segment spoofing check | Changes |
| C-ENROLL.9.3 — Overlapping-speaker contamination check | Gated by |
| C-ENROLL.9.3 — Overlapping-speaker contamination check | Changes |
| C-ENROLL.9.4 — Allowed observation-completeness check | Gated by |
| C-ENROLL.9.4 — Allowed observation-completeness check | Changes |
| C-ENROLL.9.5 — Declared authorization and durable-token check | Changes |
| C-ENROLL.9.6 — Full-segment stream-integrity check | Gated by |
| C-ENROLL.9.6 — Full-segment stream-integrity check | Changes |
| C-ENROLL.9.6.1 — Full-segment diarization-confidence condition | Gated by |
| C-ENROLL.9.6.1 — Full-segment diarization-confidence condition | Changes |
| C-ENROLL.9.6.2 — Resolved speaker-transition condition | Gated by |
| C-ENROLL.9.6.2 — Resolved speaker-transition condition | Changes |
| C-ENROLL.9.6.3 — No material stream split or merge condition | Gated by |
| C-ENROLL.9.6.3 — No material stream split or merge condition | Changes |
| C-ENROLL.9.6.4 — No unresolved second-speaker uncertainty condition | Gated by |
| C-ENROLL.9.6.4 — No unresolved second-speaker uncertainty condition | Changes |
| C-ENROLL.9.6.5 — Stream spoofing-evidence condition | Gated by |
| C-ENROLL.9.6.5 — Stream spoofing-evidence condition | Changes |
| C-ENROLL.9.7 — Immutable enrollment segment identity | Changes |
| C-ENROLL.9.8 — Per-segment eligibility decision record | Changes |
| C-ENROLL.9.8.1 — Eligibility decision outcome | Gated by |
| C-ENROLL.9.8.1 — Eligibility decision outcome | Changes |
| C-ENROLL.9.8.2 — Eligibility decision reason | Fails closed by |
| C-ENROLL.9.8.2 — Eligibility decision reason | Gated by |
| C-ENROLL.9.8.2 — Eligibility decision reason | Changes |
| C-ENROLL.9.8.3 — Eligibility source references | Gated by |
| C-ENROLL.9.8.3 — Eligibility source references | Changes |
| C-ENROLL.10 — Profile readiness record | Changes |
| C-ENROLL.10.1 — Counted reading-reference set | Gated by |
| C-ENROLL.10.1 — Counted reading-reference set | Changes |
| C-ENROLL.10.2 — Per-reading eligibility reference | Gated by |
| C-ENROLL.10.2 — Per-reading eligibility reference | Changes |
| C-ENROLL.10.3 — Readiness outcome | Fed by |
| C-ENROLL.10.3 — Readiness outcome | Changes |
| C-ENROLL.10.4 — Readiness failure classes | Gated by |
| C-ENROLL.10.4 — Readiness failure classes | Changes |
| C-ENROLL.10.5 — Immutable enrollment input bundle | Fed by |
| C-ENROLL.10.5.1 — Bundle eligible-reading references | Fails closed by |
| C-ENROLL.10.5.1 — Bundle eligible-reading references | Gated by |
| C-ENROLL.10.5.1 — Bundle eligible-reading references | Changes |
| C-ENROLL.10.5.2 — Bundle eligibility-decision references | Gated by |
| C-ENROLL.10.5.2 — Bundle eligibility-decision references | Changes |
| C-ENROLL.10.5.3 — Bundle operation and session references | Fails closed by |
| C-ENROLL.10.5.3 — Bundle operation and session references | Gated by |
| C-ENROLL.10.5.3 — Bundle operation and session references | Changes |
| C-ENROLL.10.5.4 — Bundle prerequisite and authorization evidence | Gated by |
| C-ENROLL.10.5.4 — Bundle prerequisite and authorization evidence | Changes |
| C-ENROLL.10.5.5 — Bundle readiness reference | Gated by |
| C-ENROLL.10.5.5 — Bundle readiness reference | Changes |
| C-ENROLL.11 — Provisional link and profile coordination | Changes |
| C-ENROLL.11.1 — Stable link-proposal recovery identity | Gated by |
| C-ENROLL.11.1 — Stable link-proposal recovery identity | Changes |
| C-ENROLL.11.2 — Provisional profile-build identity | Changes |
| C-ENROLL.11.3 — Provisional profile constraints consumed by enrollment | Changes |
| C-ENROLL.12 — Enrollment authority and privacy limits | Fed by |
| C-ENROLL.12 — Enrollment authority and privacy limits | Changes |
| C-ENROLL.13 — Enrollment coordination records and identities | Changes |
| C-ENROLL.13.1 — Enrollment parent operation record | Changes |
| C-ENROLL.13.1.1 — Parent identity references | Fails closed by |
| C-ENROLL.13.1.1 — Parent identity references | Gated by |
| C-ENROLL.13.1.1 — Parent identity references | Changes |
| C-ENROLL.13.1.2 — Parent process-state field | Gated by |
| C-ENROLL.13.1.2 — Parent process-state field | Changes |
| C-ENROLL.13.1.3 — Parent terminal reason | Fails closed by |
| C-ENROLL.13.1.3 — Parent terminal reason | Gated by |
| C-ENROLL.13.1.3 — Parent terminal reason | Changes |
| C-ENROLL.13.1.4 — Parent audit references | Gated by |
| C-ENROLL.13.1.4 — Parent audit references | Changes |
| C-ENROLL.13.2 — Enrollment stage checkpoint | Changes |
| C-ENROLL.13.3 — Enrollment recovery operation and event | Changes |
| C-ENROLL.13.3.1 — Recovery operation identity | Fails closed by |
| C-ENROLL.13.3.1 — Recovery operation identity | Gated by |
| C-ENROLL.13.3.1 — Recovery operation identity | Changes |
| C-ENROLL.13.3.2 — Recovery crash-boundary reference | Gated by |
| C-ENROLL.13.3.2 — Recovery crash-boundary reference | Changes |
| C-ENROLL.13.4 — Absorbed enrollment duplicate record | Changes |
| C-ENROLL.14 — Enrollment audit-event ownership | Gated by |
| C-ENROLL.14 — Enrollment audit-event ownership | Changes |
| C-ENROLL.14.1 — Prerequisites verified enrollment event | Gated by |
| C-ENROLL.14.1 — Prerequisites verified enrollment event | Changes |
| C-ENROLL.14.2 — Session opened enrollment event | Gated by |
| C-ENROLL.14.2 — Session opened enrollment event | Changes |
| C-ENROLL.14.3 — Session closed enrollment event | Gated by |
| C-ENROLL.14.3 — Session closed enrollment event | Changes |
| C-ENROLL.14.4 — Segment accepted enrollment event | Gated by |
| C-ENROLL.14.4 — Segment accepted enrollment event | Changes |
| C-ENROLL.14.5 — Segment rejected enrollment event | Gated by |
| C-ENROLL.14.5 — Segment rejected enrollment event | Changes |
| C-ENROLL.14.6 — Prerequisite failed enrollment event | Gated by |
| C-ENROLL.14.6 — Prerequisite failed enrollment event | Changes |
| C-ENROLL.14.7 — Prerequisite-change token-revocation enrollment event | Gated by |
| C-ENROLL.14.7 — Prerequisite-change token-revocation enrollment event | Changes |
| C-ENROLL.14.8 — Provisional link proposed enrollment event | Gated by |
| C-ENROLL.14.8 — Provisional link proposed enrollment event | Changes |
| C-ENROLL.14.9 — Provisional profile created enrollment event | Fed by |
| C-ENROLL.14.9 — Provisional profile created enrollment event | Changes |
| C-ENROLL.15 — Enrollment crash recovery | Gated by |
| C-ENROLL.15 — Enrollment crash recovery | Changes |
| C-ENROLL.15.1 — Recovery before the prerequisite snapshot | Gated by |
| C-ENROLL.15.1 — Recovery before the prerequisite snapshot | Changes |
| C-ENROLL.15.2 — Recovery after initial checks before BAI | Gated by |
| C-ENROLL.15.2 — Recovery after initial checks before BAI | Changes |
| C-ENROLL.15.3 — Recovery with BAI pending | Gated by |
| C-ENROLL.15.3 — Recovery with BAI pending | Changes |
| C-ENROLL.15.4 — Recovery after token issue before final checks | Gated by |
| C-ENROLL.15.4 — Recovery after token issue before final checks | Changes |
| C-ENROLL.15.5 — Recovery after failed prerequisites or revocation | Gated by |
| C-ENROLL.15.5 — Recovery after failed prerequisites or revocation | Changes |
| C-ENROLL.15.6 — Recovery after consumption before opening | Gated by |
| C-ENROLL.15.6 — Recovery after consumption before opening | Changes |
| C-ENROLL.15.7 — Recovery before the biometric system-command observation | Gated by |
| C-ENROLL.15.7 — Recovery before the biometric system-command observation | Changes |
| C-ENROLL.15.8 — Recovery after intent without a provable start result | Gated by |
| C-ENROLL.15.8 — Recovery after intent without a provable start result | Changes |
| C-ENROLL.15.9 — Recovery during confirmed capture | Gated by |
| C-ENROLL.15.9 — Recovery during confirmed capture | Changes |
| C-ENROLL.15.10 — Recovery after observations before close | Gated by |
| C-ENROLL.15.10 — Recovery after observations before close | Changes |
| C-ENROLL.15.11 — Recovery after close before Catalog submission | Changes |
| C-ENROLL.15.12 — Recovery during partial root ingestion | Gated by |
| C-ENROLL.15.12 — Recovery during partial root ingestion | Changes |
| C-ENROLL.15.13 — Recovery after root append before checkpoint | Gated by |
| C-ENROLL.15.13 — Recovery after root append before checkpoint | Changes |
| C-ENROLL.15.14 — Recovery after roots before reading enqueue | Gated by |
| C-ENROLL.15.14 — Recovery after roots before reading enqueue | Changes |
| C-ENROLL.15.15 — Recovery during partial reading completion | Gated by |
| C-ENROLL.15.15 — Recovery during partial reading completion | Changes |
| C-ENROLL.15.16 — Recovery after readiness before link proposal | Gated by |
| C-ENROLL.15.16 — Recovery after readiness before link proposal | Changes |
| C-ENROLL.15.17 — Recovery after link-proposal submission | Gated by |
| C-ENROLL.15.17 — Recovery after link-proposal submission | Changes |
| C-ENROLL.15.18 — Recovery after link commit before profile creation | Changes |
| C-ENROLL.15.19 — Recovery during SIA profile creation | Gated by |
| C-ENROLL.15.19 — Recovery during SIA profile creation | Changes |
| C-ENROLL.15.20 — Recovery after restart of an active enrollment session | Gated by |
| C-ENROLL.15.20 — Recovery after restart of an active enrollment session | Changes |
| C-ENROLL.15.21 — Recovery from coordinator-owner contradiction | Gated by |
| C-ENROLL.15.21 — Recovery from coordinator-owner contradiction | Changes |
| C-ENROLL.16 — Enrollment retry and failure boundary | Gated by |
| C-ENROLL.16 — Enrollment retry and failure boundary | Changes |
| C-ENROLL.16.1 — Same-parent technical retry conditions | Gated by |
| C-ENROLL.16.1 — Same-parent technical retry conditions | Changes |
| C-ENROLL.16.2 — Fresh enrollment-session requirements | Gated by |
| C-ENROLL.16.2 — Fresh enrollment-session requirements | Changes |
| C-ENROLL.16.3 — Required-audit durability failure | Gated by |
| C-ENROLL.16.3 — Required-audit durability failure | Changes |

## Named review dispositions

The complete behavior was reviewed for misfiled restrictions, failure outcomes and gates, including every USED BY row. Each positive scan hit below is retained for its named reason.

| Card / line | Flag | Reason |
|---|---|---|
| C-ENROLL.2 — Six-owner prerequisite check; line 101 | prerequisite_review / Gated by | The all-six conjunction defines this check itself. Its actual owner inputs are named in Fed by and failure is explicit; no second gating authority is invented from its own checking logic. |
| C-ENROLL.2.2 — Completed first-code prerequisite; line 155 | prerequisite_review / Gated by | Saved/verified/tested/activated are the condition being checked, with the actual handover owner in Fed by. Failure is explicit; a duplicate self-condition is not a TOGETHER gate. |
| C-ENROLL.2.3 — Inert initial-material prerequisite; line 178 | prerequisite_review / Gated by | The two inertness facts define prerequisite 3 and their owners are named. Either missing/contradictory fact already fails closed; no additional gate is sourced. |
| C-ENROLL.3.1 — Durable explicit-begin event; line 534 | prerequisite_review / Gated by | The scan also sees the new-begin requirement in the using fresh-session card. This card owns the actual durable choice event and its pre-snapshot crash outcome; it does not manufacture a separate event gate. |
| C-ENROLL.3.3 — Prospective enrollment session identity; line 588 | prerequisite_review / Gated by | Prospective-versus-opened status is the identity's own meaning. The actual session commit remains C-ENROLL.4.4; Fails closed explicitly states no commit means no session, without turning that definition into a second identity gate. |
| C-ENROLL.4.3 — Durable authorization chain and binding; line 737 | prerequisite_review / Gated by | The proof chain is verified by its own operation, with actual BAI input named. Missing or unverifiable proof/binding already prevents opening; using-card requirements do not add another binding authority. |
| C-ENROLL.4.5 — Opening duplicate barriers; line 1046 | prerequisite_review / Gated by | The card groups the eight source-defined barriers, each separately placed. It names actual claim/proof inputs and explicit refusal/revocation, with no extra outer barrier invented. |
| C-ENROLL.4.6 — Spent proof without an opened session; line 1253 | prerequisite_review / Gated by | New begin and fresh token are requirements for a later attempt, not a gate to recording this already-spent no-session abort. The current stopped outcome is explicit. |
| C-ENROLL.7.5 — Person-Box prerequisite safety change; line 2540 | prerequisite_review / Gated by | Fresh enrollment is required after the Person-Box-triggered stop. The actual owner change is Fed by and stopping is explicit; no gate may delay the protective stop. |
| C-ENROLL.7.8 — Application or machine restart safety change; line 2609 | prerequisite_review / Gated by | Fresh authorization governs later capture, not the immediate restart stop. Actual capture/observation facts are named and no automatic reopening is permitted. |
| C-ENROLL.9 — Initial-corpus eligibility gate; line 2756 | prerequisite_review / Gated by | The six-check conjunction is this gate's own logic. Underlying SIA/BOP/BAI facts are named inputs and every failing/unavailable fact rejects contribution; no second eligibility authority is added. |
| C-ENROLL.9.1 — Consistent live-speaker stream check; line 2780 | prerequisite_review / Gated by | One-stream consistency defines check 1. SIA facts are Fed by and failure excludes the segment; the check's own condition is not repeated as an outer gate. |
| C-ENROLL.9.3 — Overlapping-speaker contamination check; line 2826 | prerequisite_review / Gated by | The overlap condition is the check itself. Actual SIA assessment is named and unresolved overlap rejects contribution; no other gating owner is decided. |
| C-ENROLL.9.6 — Full-segment stream-integrity check; line 2895 | prerequisite_review / Gated by | The five stream-integrity conditions define check 6, with individual child cards and explicit rejection. Actual owner facts are inputs, not a new coordinator authority. |
| C-ENROLL.9.6.1 — Full-segment diarization-confidence condition; line 2918 | prerequisite_review / Gated by | Full-segment confidence above the source's threshold is this condition itself; no value is chosen. Failure is explicit and SIA supplies the facts. |
| C-ENROLL.9.6.2 — Resolved speaker-transition condition; line 2941 | prerequisite_review / Gated by | No unresolved transition is the condition being evaluated. SIA supplies the assessment and failure rejects the segment; no additional gate exists in the source. |
| C-ENROLL.9.6.3 — No material stream split or merge condition; line 2964 | prerequisite_review / Gated by | No material split/merge is the condition itself. Its actual facts and rejection result are written; no independent outer gate is added. |
| C-ENROLL.9.6.4 — No unresolved second-speaker uncertainty condition; line 2987 | prerequisite_review / Gated by | No unresolved second-speaker uncertainty is the condition being checked. Source facts are named and unresolved uncertainty fails closed, with no invented extra authority. |
| C-ENROLL.9.8 — Per-segment eligibility decision record; line 3056 | prerequisite_review / Gated by | The using readiness card requires decision references. This record preserves an already-owned per-segment result and stable key; the readiness requirement is not a new gate on recording the decision. |
| C-ENROLL.15.1 — Recovery before the prerequisite snapshot; line 4041 | prerequisite_review / Gated by | New begin is a later-attempt requirement. Recovery at this boundary stays idle with no BAI call or session; no gate can authorize reconstruction from the sole begin event. |
| C-ENROLL.15.3 — Recovery with BAI pending; line 4087 | prerequisite_review / Gated by | New begin/pending/token requirements concern the later attempt; this recovery case preserves no volatile BAI authority. Refusal to restore is explicit. |
| C-ENROLL.15.7 — Recovery before the biometric system-command observation; line 4179 | prerequisite_review / Gated by | The actual opening/BAI facts trigger the recovered observation under its existing owners. Separate current capture preconditions are stated in Fails closed; this case never reopens capture or invents another observation gate. |
| C-ENROLL.15.19 — Recovery during SIA profile creation; line 4455 | prerequisite_review / Gated by | The actual SIA result is named in Fed by and no commitment means no creation event in Fails closed. This recovery consumes the existing profile gate rather than inventing a new one. |
| C-ENROLL.15.20 — Recovery after restart of an active enrollment session; line 4478 | prerequisite_review / Gated by | Fresh-action/check/pending/token/session requirements are for a new capture operation after the immediate restart closure. The recovery case itself cannot be gated into reopening the old microphone. |
| C-ENROLL.16 — Enrollment retry and failure boundary; line 4524 | prerequisite_review / Gated by | The two same-parent retry conditions define permitted retry and are written in Does/.16.1. Every named fail-closed class has an explicit owning card; no separate retry authority or empirical value is created. |
| C-ENROLL.16.2 — Fresh enrollment-session requirements; line 4572 | prerequisite_review / Gated by | The five fresh requirements are the conjunction being described. Their actual owners appear in Fed by and missing any prevents a session; adding the conjunction as its own external gate would repeat inner logic. |

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


### Source placements carried from CH08-b

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

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH08-c

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §26.2/§26.3/§26.5; Map C-LMAC | Root, .1–.5: whole-mechanism connection before/during/after, single interface for every call, initial relevance-guided query is first not only, no data/copy/cache/accumulated model, current-state responses including mid-pass changes, permission-preserving full reach, no filtering/relevance/privacy ownership/reduced output/caller decision. | C-LMAC source-ordered tree and explicit owner dispositions |
| V10 §26.5; B6 mechanical §12 | .3 target interfaces: §7F, §7R, §7D, §7L, §7K, §7J, §7Q, §7P, §22; each exact request/result, own provenance. BOP-produced roots and pattern readings in shared memory are material reached through retrieval/relevance, not direct BOP/OOP queries. Wellbeing tier solely response calculation, never identity/access. | C-LMAC source-ordered tree and explicit owner dispositions |
| V10 §26.7 | .6: response-time current behavioral readings, state/open-loop/capacity picture, wellbeing tier, authority, privacy, voice/text mode; caller computes actual response with confidence/firmness and whole picture, no stored RBCS. Exact mode-state query transport beyond the listed nine component contracts remains open. Full adaptation CH08-g. | C-LMAC source-ordered tree and explicit owner dispositions |
| B6 mechanical §12 | .7 uniform request: requester, declared purpose, targets, applicable mode/configuration version; whole live result with own provenance. .8 protected Q/P control queries obtain decisions without recursive prerequisite; only minimum requester/purpose/target metadata, no protected payload before return; identity/access/purpose/logging still bind; ordinary queries apply obtained results in order. | C-LMAC source-ordered tree and explicit owner dispositions |
| B6 mechanical §§3/12 | .9 query identity/log: proposed query_operation_id, one logical query/one shared routing record, five routing fields requester/target/purpose/Q authorization kind/outcome ref; transport retries reuse identity, append child details, exactly one terminal parent, new intent/context gets new identity. .10 recovery/technical retry/refusals: no private state recovery; complete interrupted terminal idempotently; component owns recovery; unknown/unauthorized purpose refused and recorded; shared B9 values reused, no semantic interpretation retry invented. | C-LMAC source-ordered tree and explicit owner dispositions |
| B6 mechanical §3/§14; V10 §0B | .11 atomic operation records, structural duplicate prevention, committed checkpoint recovery, partial completion, protective uncertainty, one-log/never log-about-logging/no log as evidence, Q/identity protection; no root-ingest mechanism invented for stateless routing. Existing operation/log/B9 owners reused. | C-LMAC source-ordered tree and explicit owner dispositions |
| V10 §25.4; B24 §6.5; B-INT-6 §§4/10/11/12/14 | .12 output retrieval: SACL level/categories before retrieval, intersection with Q eligibility; generator never receives out-of-scope content or leaks its existence. SACL owns refreshed PBR cache, LMAC keeps none. proposed retrieval_intersection_record stays output-coordinator-owned and references eligibility, scope, admitted identities only. Owner current facts/epochs never restored from history; dead-epoch candidates cannot form output. Cannot honor intersection → halt/withhold. Full output fence/dispatch/delivery lifecycle CH09. | C-LMAC source-ordered tree and explicit owner dispositions |
| V10 §0B/§7G-A/§7E-TSC; B6 closeout §9; B15 §11; A16 §5; A2 §§5A.1/9; B16 §7 | .13 use boundaries: active pre-ingest/TSC blockers, safe metadata-only held references, B-HOLD no new downstream use, quarantine promotion trail, no ordinary TSC archive access or inspection, no prepared/uncommitted telling as semantic context, provisional creation status carried visibly and in canonical provisional_material_used. Sealed WhatsApp archive remains inaccessible; no decryption/promotion path created. | C-LMAC source-ordered tree and explicit owner dispositions |
| B-INT-8 §13A/I7; A25→B10 §7; kernel §V/§W | .14 owner-preserving interfaces: fresh connection current-use resolution per use and current applicable version; reread Q→F→R order regardless assignment, no narrowed context; kernel reference-only carrier cannot create parallel routing or gates. Existing C-24 and C-7H owners retain full mechanics. | C-LMAC source-ordered tree and explicit owner dispositions |
| Earlier chapters | 19 incoming relationship occurrences at 16 places, all to reciprocate one place per row. Five earlier USED BY references to this root require explicit consumption of C-7J/C-7K/C-7L.9/C-7L.13/C-7P. Do not edit earlier bytes. CH08-b root Changes cites V10 §7R for a whole-result LMAC handoff that requires B6 §12 (or V10 §26.5); carry this citation addition for the fix round and use the correct source now. | C-LMAC source-ordered tree and explicit owner dispositions |
| Discovery and status | Four index rows NHD-M26/BU6P/BU6M/BU6. B6 old open wording does not reopen accepted B7/B15/B-INT-8/B26. Final closeout receipt retains its own audit condition; accepted mechanical package is independently closed. Framework/kernel retain owners; inactive memory-fabric contributes intent only. No historical behavior imported or source pin changed. | C-LMAC source-ordered tree and explicit owner dispositions |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH08-d

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §25.1/26.4, Map C-BOP | Root and .1 authorization/classification: directly physical only, all authorized session signals, four source classes, confirmed sent text only; no interpretation/private store/model; OOP owns TTS stop, BOP records timestamp/position. | C-BOP source-ordered tree and explicit boundary dispositions |
| V10 §25.1 event vocabulary | .2 all 22 event values in source order, their decided measurement/payload fields and exact no-interpretation limits; extended registered before first use. | C-BOP source-ordered tree and explicit boundary dispositions |
| V10 §25.1 root/payload/capture identity | .3 seven BOP-specific root bindings, .4 all 19 payload fields/nested authorization/modes/methods, .5 six-input stable capture hash and durable sequence before writes. Reuse built root schema owner without claiming BOP built. participant_record and anchor_record internals genuinely unspecified. | C-BOP source-ordered tree and explicit boundary dispositions |
| V10 §25.1 quality/third party/simultaneous/reconnect/DUMB/recovery | .6 quality and completeness fields/values; .7 all four third-party fields and three handling values; .8 reconstructible one-root-per-channel bundle; .9 optional anchors and ordinary later reread/retrieval; .10 complete DUMB/typing boundary; .11 failure/retry/crash. Below-threshold quality is not an authorization waiver and B11 never writes the old sealed batch. | C-BOP source-ordered tree and explicit boundary dispositions |
| A15 v1.1 §§2–6 and receipt §§3–7 | .12 optional six-field/five-name acoustic notes, scoped certainty, full provenance, downstream physical context permitted but never sufficient alone, no capture widening/schema activation; empirical choices open. Later receipt explicitly settles policy acceptance while old V10/Bundle 6 pending wording remains historical status, not active-schema authority. | C-BOP source-ordered tree and explicit boundary dispositions |
| B6 mechanical §§3/13 | .13 only Catalog→append_root/B11→reading route, atomic record/identity/commit/retry/partial recovery, held boundaries and privacy; existing B11/B9 owners reused. | C-BOP source-ordered tree and explicit boundary dispositions |
| B6 policy A12 and mechanical §13 | .14 imported-item reaction operation: exact start and four first-ending events, active/paused/post-playback segments, finite pause/post bounds, no overlap/one item/one segment, proposed reaction_window_id, duplicate opens, committed-state interruption recovery, no guessed links, capture-child link commit and exactly one parent terminal. Full raw-only facts retained; never merged/causal inference. | C-BOP source-ordered tree and explicit boundary dispositions |
| V10 §§25.6/25.11/25.12, B-INT-7 §§7/10/16/19 | .15 enrollment/biometric interfaces: B29 microphone, BOP observations; enrollment provenance not identity; BAI command seven result forms, safe two-field content; session-open single success command deterministic identity; raw voice protected, frozen set after close, capture ID end-to-end, rejected profile segments still preserved. Full enrollment process CH09. | C-BOP source-ordered tree and explicit boundary dispositions |
| Map C-BOP, V10 §0B | .16 shared logging, one operation/one record, honest failure gaps, access protection; no logs as evidence. | C-BOP source-ordered tree and explicit boundary dispositions |
| Companion BOP Third-Party Flag | Unqualified pre-output-review wording conflicts with V10's purpose-specific internal/visible authorization. Mark in header and affected gate; V10 governs. | C-BOP source-ordered tree and explicit boundary dispositions |
| Earlier chapters | Four incoming places C-7E/C-TSC/C-TSC.9/C-TSC.13.1 reciprocated separately. C-7E stamps the BOP root ACCEPTED; root is DESIGNED under contract §3, accepted wiring separately stamped. Carry earlier status fix without changing bytes. | C-BOP source-ordered tree and explicit boundary dispositions |
| Discovery | Index NHD-M25/M25-BOP-VI/A15/BU6P/BU6M navigation only. Bundle 5 A15 ownership and B6 closeout BOP row preserve owners and status. Inactive Voice/Delivery Director remains INTENT only. Defaults has no BOP-specific match. No archive behavior imported. | C-BOP source-ordered tree and explicit boundary dispositions |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH08-e

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §26.6 | Root and .1 definition/no owned data; .2 seven observed signal categories in source order; correction physical timing/relationship versus separate conversational content; follow-up relation mechanism genuinely unspecified, not an invented meaning classifier. | C-OOP source-ordered tree and explicit gap/owner dispositions |
| V10 §26.6 absence discipline | .3 silence only when BOTH expected signal and observation conditions held; absence recorded as absence, never satisfaction/acceptance. No response may reflect no notice, other activity or session ending; no cause inferred. | C-OOP source-ordered tree and explicit gap/owner dispositions |
| V10 §26.6 connectivity/routes | .4 source type outcome_observation via Catalog/engine/shared-store; .5 readings available to live query, reread, clash, state review, wellbeing tagging. Contradiction preserves original and new reading beside it. No direct configuration/rule/output route. | C-OOP source-ordered tree and explicit gap/owner dispositions |
| V10 §26.6 self-improvement; §26.12 | .6 proposals through Meaning Engine/shared reading/Computed View/authority before change; all automatic changes logged/explainable/evidence-traceable/reversible; explicit protected-core approval. Full learning/threshold mechanics CH08-g. | C-OOP source-ordered tree and explicit gap/owner dispositions |
| V10 §26.4; Map C-OOP/B29/voice-priority chain | .7 immediate TTS stop when Ness begins speaking during voice-mode function execution; BOP records timestamp and stream position. Stop control is distinct from prohibited outcome-to-behavior routing. No pipeline latency/buffering/remainder policy invented. | C-OOP source-ordered tree and explicit gap/owner dispositions |
| B6 mechanical §§3/12/13; closeout §8 OOP row | .8 accepted one-path/no-live-query, stable capture identity, durable sequence before write, atomic state/record, per-item promotion, duplicate structural prevention, retry under existing B9, honest gaps/crash recovery, protective hold/privacy/writer and one-operation-one-log. Reuse exact B11/B9 owners. | C-OOP source-ordered tree and explicit gap/owner dispositions |
| B6 A10/A12 and B-INT-3 | .9 existing authorized-session and imported-reaction interfaces consume C-BOP.1.1 and C-BOP.14 complete mechanics; do not duplicate a reaction window or treat it as the generic post-function window. | C-OOP source-ordered tree and explicit gap/owner dispositions |
| Map C-OOP; V10 §0B | .10 log actual post-action signal, named absence and routes to reread/clash/wellbeing; protected access, no recursive logs or evidence-weight inflation. | C-OOP source-ordered tree and explicit gap/owner dispositions |
| Earlier chapters | Three incoming places: C-7E, C-7O.9.4, C-BOP.2.6. C-7E stamps the OOP root ACCEPTED; carry fix because root remains DESIGNED, accepted mechanical scope has separate cards. Earlier action-result owner stays separate. | C-OOP source-ordered tree and explicit gap/owner dispositions |
| Discovery/status | Index M26/voice-priority/BU6 rows navigation only. Companion/Defaults have no OOP-specific match. Inactive Voice/Delivery Director is intent only. Overbroad discovery returned ledger quotation rows; they supply no behavior and no whole-read credit, and no archive was opened. | C-OOP source-ordered tree and explicit gap/owner dispositions |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH08-f

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §§0/7A/11 item23; Map C-AFFIRM | DESIGNED root: record occurrence of specific-reading accept/reject, dated and weightless in Story Layer; truth judgment stays outside engine; never block, rewrite or supply confidence/evidence/authority. Reuse C-7A.14.3 and current-use separation. | C-AFFIRM source-ordered tree and explicit owner/gap dispositions |
| Bundle3 §17 | .1 accepted record with six fields: target reading ID(s), response accept/reject, timestamp, Ness initiator, explicit weightless marker, stable event ID. Target can plural only when one response addresses those specific readings. No invented snake_case schema fields/types. | C-AFFIRM source-ordered tree and explicit owner/gap dispositions |
| Bundle3 §17 | .2 same response duplicate→one event/one log; .3 no response means/moves/stalls nothing, never consent or engine gate; .4 no changed reading/root/confidence/evidence/firmness/truth, rejection not opposite proof. | C-AFFIRM source-ordered tree and explicit owner/gap dispositions |
| Bundle3 §17 with §§13/15 | .5 only permitted presentation/current-use effects: dismissal can stop resurfacing unless valid new trigger; existing view grouping/labels owners reused; history remains. Exact new-trigger mechanics not invented. .6 changed judgment appends beside old. | C-AFFIRM source-ordered tree and explicit owner/gap dispositions |
| Bundle3 §17; existing C-7J.7.3 | Root consumes canonical separate clash-response/affirmation linkage; no duplicate atom. .7 excludes general telling responses, theme actions, Person-Box events, clash responses and action dispositions, names actual owners; no widened generic feedback bus. | C-AFFIRM source-ordered tree and explicit owner/gap dispositions |
| Bundle3 §§18/19/20; V10 §0B | .8 append-only protected living record, no recursive logging or second evidence vote, exact privacy/identity/access boundaries; no silent operation, no event as authority. | C-AFFIRM source-ordered tree and explicit owner/gap dispositions |
| W1 CH04-a carry; Bundle6 §13; Bundle3 §17 | .9 boundary consuming complete C-BOP.14 reaction operation and C-OOP.3 absence discipline: raw physical/link facts are not accept/reject responses. Reaction mechanics remain canonical in CH08-d, not duplicated inside AFFIRM. Writing1’s CH08-d/f carry-forward is satisfied by full d placement plus f’s narrow seam boundary. | C-AFFIRM source-ordered tree and explicit owner/gap dispositions |
| Prior incoming C-7D; Bundle4 §§11/12 | Root reciprocal carries occurrence pointer only, never state support from accept/reject or its log. Prior C-7D generic Ness-response reference to AFFIRM needs qualification/correction: affirmative occurrence is not a general state self-report. Record fix without changing earlier bytes. | C-AFFIRM source-ordered tree and explicit owner/gap dispositions |
| Existing cross-links | Three incoming places C-7J.7.3, C-7I.4.1, C-7D; one prior USED BY commitment C-7J.7.3 to root consumed. All individual rows. | C-AFFIRM source-ordered tree and explicit owner/gap dispositions |
| Discovery | NHD-M11-23/BU3 navigation. Companion item23/current rule list match scope; Defaults off-board principle only. Other accepted packages use generic response references, not new AFFIRM mechanics. No ledger behavior or archive used. | C-AFFIRM source-ordered tree and explicit owner/gap dispositions |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.

### Source placements added by CH09-a

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| V10 §25.5: SIA responsibility | C-WIS-SEP.1; identity/audio assessment only; no mental or physical diagnosis |
| V10 §25.5: wellbeing responsibility; §22 tiers | C-WIS-SEP.2 and .2.1–.2.5; own baseline, sustained multi-session divergence, four tier consequences, ordinary availability |
| V10 §25.5: SACL responsibility | C-WIS-SEP.3; current identity/security evidence, no wellbeing tier, no acoustic inference from behavioral divergence |
| V10 §25.5: appointment records | C-WIS-SEP.4; calibration and freeze-unlock only; all three forbidden purposes |
| V10 §25.5: temporary divergence; §25.4 Option A | C-WIS-SEP.5; all listed temporary causes, imitation_risk, top_security block, recognized_ness retained; Gate-2 wording conflict marked |
| V10 §25.5: acoustic spoofing | C-WIS-SEP.6; anti_spoofing_assessment, medium/high suspicion_level, guest, relock, private alert, wellbeing uninvolved |
| V10 §25.5: two paths | C-WIS-SEP.7; no merging or conflation |
| MAP C-WIS-SEP | Root and .9; no independent I/O, named consumers, CY-H/CY-I, actual result and producing mechanism, violations, append-only records, no mandatory negative-attestation field |
| A26 §§4.4–4.6; B-INT-5 §§4/8; Bundle 6 mechanical §12 | C-WIS-SEP.8; response-only wellbeing, independent mode/access conditions, ordinary Personal Mode availability, identity-loss output stop. Full mode contracts left to CH09-i; shared query schema remains C-LMAC.3.9 in CH08-c |
| V10 §§26.6/26.11/26.12 | Existing C-OOP.5.5, C-LEARN.8.3 and C-LEARN.9.3 receive reciprocal rows in this root; no repeated learning mechanism |
| COMP §5 / Wellbeing / Identity / Security Separation Rules | Corroborates V10's complete separation section; no additional mechanism or conflict |
| B-INT-4 §7 C2; B-INT-7 source boundary | Identity confirmation is not wellbeing calibration; existing cache owner is CH04-b. Full enrollment mechanics left to CH09-h |
| V10 §25.4 remainder; §25.6; §22 remainder | Full access calculations left to CH09-d, biometric artifacts to CH09-e, calibration/unlock procedure to CH10-c. Only their separation boundaries are placed here |
| DD/CR; DR and active/accepted discovery | No additional separation mechanism imported. DD/CR workflow excluded. Ledger is navigation/Appendix B only; no restored behavior is sourced here |

### Source placements added by CH09-b

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| V10 §25.2 / Core Principle and Protected Rules | C-OTHER root, .1/.2/.3/.4/.5/.8: complete internal mechanism; independent disclosure; privacy and authority; no permission transfer, hidden disclosure, guest private memory, other-speaker changes or protected-core override; claims retain speakers |
| V10 §25.2 / Access Levels | C-OTHER.3 and .3.1–.3.4 carry all four values and this section's conditions. Full Gate 0–3 predicates and assessment records remain CH09-c/d |
| V10 §25.2 / Guest Mode | C-OTHER.4: general response, no Ness-personal shared-store material, no hidden-information acknowledgment |
| V10 §25.2 / Known-Person Permissions | C-OTHER.5: maintenance authority, expressed boundaries and learned evidence, all seven initial category names and open vocabulary. Canonical category field remains C-7L.9.1; PBR read interface remains C-7L.9 |
| V10 §25.2 / Separate Parent Identities | C-OTHER.6: all six independently held identity/context kinds; reuses C-7L.9.4 |
| V10 §25.2 / Parent Translation | C-OTHER.7 and .7.1–.7.5: request requirement; each of the three requests and recipients; uncertainty; no autonomous intervention; scoped adaptation; stored revisable output; authorized private context versus PBR-bounded disclosure |
| V10 §25.2 / Statements About Ness; §7H immutable reread result | C-OTHER.8 and .7.4: TSC → root → reading speaker continuity; later evidence may trigger reread; original records never changed. Full reread mechanics remain CH05-d |
| V10 §25.2 / Person-Box Visibility | C-OTHER.9: every prohibited inspection category, stored-extent and recognition secrecy. Canonical owner C-7L.9.3 |
| V10 §25.2 / Temporary Session Cache | C-OTHER.10: blocker, complete meaningful context, all session states, normal/crash distinction, indefinite waiting, no automatic transitions, separate permanent-seal authorization, no deleted state. Atomic state/transition owners remain C-TSC.12 and descendants in CH04-b |
| V10 §25.2 / Fingerprint-Authorized Batch Promotion | C-OTHER.11 and .11.1–.11.3: later thumbprint, complete relevant session as unit, unrelated caches excluded, remaining blockers respected, no second manual approval, attributed downstream route with both Map conflicts marked |
| V10 §25.2 / Continuous Speaker Security; §25.4 calculation/failure boundaries | C-OTHER.12 and .12.1–.12.3: continuous assessment, immediate recalculation, uncertainty, restart and stale/failure outcomes, medium/high versus spoofing_suspected flag, separate alert rule, imitation_risk not Gate 0, no routine voice challenge. Full failure/recovery objects remain CH09-d |
| B-INT-6 §§3/4/13; §6D consumer gate loop; §14 blocking boundary | C-OTHER.13 and .13.1–.13.3: privacy before relevance, final privacy then access, same answer on both gates, transformed answer rechecked, shared minimum, private owner-confirmed path, PBR/presence at output, no hidden material or mouth-refusal policy inference. Full coordinator identity, payload, fence, claim, dispatch, channel and recovery atoms remain CH09-d, with existing privacy atoms at C-7Q.11.3 |
| MAP C-OTHER / Logging | C-OTHER.14: every listed access/disclosure/PBR/translation/attribution operation is recorded under component privacy/security rules; no invented event names or record schema |
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. Stronger-authorization and minor/vulnerable-default conflicts retained consistently with CH08-a; no new simulation or fixed-profile mechanism |
| B-INT-4 §7 C1–C3; B-INT-5 §§4/8 | Existing session-specific token/receipt/recognition and promotion owners remain CH04-b; mode intersection/reduction belongs CH09-i. A fingerprint does not silently remove those canonical owner requirements |
| B-INT-8 §15; A22 §3 speaker attribution; B-INT-7 source boundary | No connection gives access or lets another speaker accept as Ness; complete connection operation remains CH06-g. Phone-specific intake/door policy remains CH10-d, retaining the same source attribution. Enrollment remains CH09-h |
| Bundle 5 §5 Path 9 and §8 frozen wording; COMP embedded §2 | Bundle 5 confirms the shared third-party scope and preserves its differing authority explanation; not substituted for V10. Companion full other-speaker section corroborates rules; its shorter lifecycle omits later states supplied by V10, with no alternate transition invented |
| Source discovery and receipts | Searches by C-OTHER, full other-speaker/guest/known-person name, PBR/category vocabulary, parent translation and third-party interpretation/simulation identify the packages above. No restored behavior or ledger behavior is imported. B-INT-6 receipt supplies acceptance evidence only; its remaining formal-closeout audit condition is not claimed complete |

### Source placements added by CH09-c

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| V10 complete §25.3; MAP complete C-SIA | C-SIA root and .1–.19: complete SIA records, fields, values, cadence, identity/acoustic separation, profiles, eligibility, protection, responses, linking and compact representation. Source map fixed before drafting; no numerical threshold or algorithm added. |
| V10 §25.3 / Speaker Session State (SSS) | C-SIA.2 and .2.1–.2.7: all seven fields, exact modes/biometric values, list shape, addressed stream, timestamp/null, append-only in-session history and restart loss. |
| V10 §25.3 / Voice Stream Record | C-SIA.3 and .3.1–.3.7: all seven fields, onset root, separate identity/acoustic objects, three activity values, last timestamp and trigger. No unsupported transitions added. |
| V10 §25.3 / Speaker Assessment Object | C-SIA.4 with five outer fields; .4.1/.4.1.1 ranked candidate record, all five candidate fields, seven separate evidence dimensions; both certainty ranges, all profile values, full active-flag vocabulary and all null/separation conditions. |
| V10 §25.3 / Anti-Spoofing Assessment Object | C-SIA.5 and .5.1–.5.4: four fields, four suspicion levels, five exact acoustic bases, source reading IDs and certainty; all excluded conversational/behavioral categories retained. |
| V10 §25.3 / SIA Output Interface and Assessment Update Cadence | C-SIA.6 and three field cards; four audit-only confidence labels with no decision-input use. C-SIA.7 and eight trigger cards preserve exact trigger names and empirical window-size boundary. |
| V10 §25.3 / Diarization, Voice Profile Architecture, Natural Voice Variation | C-SIA.8/.9/.10: independent parallel streams and candidates, shared technical comparison space but independent identity authority, profile range across four named condition kinds and combined-certainty behavior. |
| A15 policy §§2–5/7 and receipt | C-SIA.10.1 consumes all six fields and five names while C-BOP.12 and descendants remain canonical record owners. All ten forbidden stand-alone conclusions, bounded context, full provenance, physical-only certainty and no-recording-authority boundary retained. V10 proposal/accepted status conflict marked. |
| V10 §25.3 / Training Eligibility Rules | C-SIA.11 and six condition cards: all six ordinary eligibility requirements, exact training_eligibility_threshold name, capture-time evidence, no appointment training and no intake/meaning bypass. |
| V10 §25.3 / The 6–10 Month Learning Period and Raw Voice Data Protection | C-SIA.12/.13: conservative thresholds, provisional ceiling, comparative weighting and gradual reduction; Layer 3 storage, protected readings, minimum access and biometric-verified Full Mode tunnel. |
| V10 §25.3 / Identity Uncertain vs. Spoofing Suspected, False Lockout Recovery, Settled Rules | C-SIA.14 plus three response cards and .15: separate uncertainty/low/medium-high responses, natural recovery, no routine challenge, silent medium/high guest/relock/private alert, independent biometric+recognition+no-spoofing requirements. Full access gates remain CH09-d. |
| V10 §25.3 / Multi-Speaker State | C-SIA.16 preserves stream set and addressed stream; SACL owns per-stream access and shared minimum. Full channel/delivery mechanics remain CH09-d and mode references CH09-i. |
| V10 §25.3 / Minimum Evidence for Person-Box Linking and Compact Profile Representation | C-SIA.17 reuses all six C-7L.10.1–.10.6 atoms without duplicating their identities. C-SIA.18 carries every derived/protected/versioned/rebuildable/non-authoritative/invalidation/inference-only property. |
| MAP C-SIA / Logging; V10 §7E-TSC §§6/7/9/29; B15 §5 items 3–7 | C-SIA.19 and root USED BY rows reciprocate existing TSC participant, attribution and event-link cards. Existing assessments are referenced without TSC calling SIA; audit authority, no root promotion, timing references and seven-field root boundary remain explicit. |
| V10 §25.11; B-INT-7 §§11–16/18/19 | C-SIA.20 plus .20.1–.20.8 carry the SIA consumer: eligible accepted readings, honest provisional confidence, one input after committed link, duplicate-free build, conservative status/ceiling/weighting, fresh assessment after restart, later evidence, post-commit enrollment event and authority limits. Existing committed-link failure atoms remain C-7L.11.13 and descendants. |
| B-INT-7 ownership remaining for CH09-h | CH09-h owns full prerequisites, bootstrap six-condition segment gate, trusted-phone/BAI opening, capture, lifecycle, proposed readiness and input-bundle records to their fields, coordinator IDs, events, crash/retry/stop mechanics and owner interfaces. Current SIA consumer lists the bundle/readiness content but creates no duplicate canonical coordination-record IDs. Activation thresholds remain unchosen in source. |
| B-INT-5 §13 and A26 §§4.1–4.3; Bundle 5 §5 Path 7 | Identity evidence never becomes private-mode or output authority. Root privacy and protection consumers use the existing owners. Full mode contracts stay CH09-i, output delivery CH09-d and enrollment CH09-h. No whole-file credit for these scoped reads. |
| Bundle 2 §5.6; Bundle 4 §9.1; Bundle 6 mechanical §§3/12; V10 §0B and component Map entries | Root USED BY continuations complete the existing declaration, authority, logging, control-query, outcome, affirmation and learning identity/security dependencies; assessment evidence does not acquire those consumers' access authority. |
| 05 NH Voice decision record v0_2 §5 | C-SIA.21 carries only the synthetic-output/identity-profile separation at CANDIDATE status. Speech engine/checkpoint/settings and language-input choices remain CH09-i/CH10-d; reported tests are evidence/history, not generalized behavior. Whole record read; one inherited whole-read obligation closed. |
| COMP complete embedded §3; kernel discovery; receipt checks | Companion SIA content corroborates the V10 record boundaries without replacing authority. Kernel matches add no SIA mechanics; whole-file obligation retained. A15 and B-INT-7 receipts are whole rereads establishing acceptance only; no independent closure audit claimed. |

### Source placements added by CH09-d

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| V10 complete §25.4; MAP complete C-SACL; COMP complete embedded §4 | C-SACL root and .1–.17 carry the full speaker-access boundary, state, ordered gates, PBR use, output limits, background authority, failures and protected rules. Companion corroborates the same source conflict; MAP-only logging remains CANDIDATE. |
| V10 §25.4 / SACL-Owned State | C-SACL.2 with all nine session fields and .3 with all seven stream fields. Four access-level value atoms reuse C-OTHER.3 and descendants; in-progress record/material sensitivity live at .10.1/.10.1.1. No unstated schema or field encoding added. |
| V10 §25.4 / Access Level Calculation | C-SACL.4 and .4.1–.4.5 preserve exact Gate 0 → 1 → 2 → 3 → else order. Gate 0 has two alternatives; Gate 1 seven required conditions; Gate 2 five; Gate 3 six. Shared Ness-box, separation and disqualifier predicates reuse the same atoms. Three threshold names remain empirical configuration values without invented numbers. |
| V10 §25.4 / Gate 2 and Option A; §25.5 separation boundary | C-SACL.4.3/.4.3.2/.6 and the header retain the contradictory no-imitation-risk Gate 2 clause and recognized_ness-preserving Option A. Neither clause is silently removed or reconciled. Acoustic Gate 0 remains separate. |
| V10 §25.4 / Fingerprint, Three Mechanisms, Multi-Speaker Sessions | C-SACL.5–.8 and .8.1–.8.3 preserve independent biometric/identity factors, no wellbeing tier input, shared minimum, the private-unobservable exception and simultaneous dependent-stream downgrade. C-WIS-SEP owns the reused separation atoms. |
| V10 §25.4 / Permission Boundary Enforcement | C-SACL.9 and .9.1–.9.3 carry LMAC → Person-Box PBR reads, output-time category checks and refresh on version change; canonical PBR fields and presence condition remain C-7L.9/.9.1/.9.2. |
| V10 §25.4 / Access Changes, Indirect Disclosure, Output Gate, Internal Context, Background | C-SACL.10–.14 carry sensitivity comparison/immediate discard before write, retrieval-time exclusion without existence hints, final privacy then access, internal-context distinction and purpose-specific background authority. Privacy binding atoms remain C-7Q.11.3. |
| V10 §25.4 / Failure and Protected-Core Rules | C-SACL.15 and four failure children preserve restart, stale assessment, SIA failure and PBR-query failure. C-SACL.16 and seven children carry all unconditional protected rules without adding enforcement designs. |
| MAP C-SACL / Logging; V10 §0B | C-SACL.17 and four record children retain candidate access-change, disqualifier, discard and audit records. Root USED BY rows preserve all 115 distinct inspected earlier incoming consumers and their source-specific access limits; later continuations do not edit those files. |
| B-INT-6 complete §§1–5; B-INT-5 §6 and §§13–14; A26 §4 | C-SACL.18 proposed Output Delivery Coordinator and .19 ordered stages preserve independent owners. C-SACL.20 and eighteen handoff facts consume the single current mode/SACL truth, references, category limits, observability, cancellations and delivery fence. Full mode record/state/transaction ownership remains CH09-i. |
| B-INT-6 §6A | C-SACL.21 and three identity atoms keep proposed stable parent, stable request-and-destination duplicate key and per-attempt identity distinct. C-SACL.21.4 consumes seven mutable validation facts using existing owner-field atoms; none enters the stable key. |
| B-INT-6 §6B and §6D | C-SACL.22/.22.1/.22.2 and .25 preserve immutable protected payload references, seven canonical privacy bindings, eight SACL bindings and the transform → new version → privacy → SACL loop. Reused fields have no duplicate canonical identity. |
| B-INT-6 §6C | C-SACL.23 contains all sixteen proposed states; .23.16 has four explicit unknown-result transitions. Positive late confirmation records history without resend; non-delivery proof or verified same-token deduplication only permits freshly checked retry; absent safe facts leaves the parent open. Later restriction never fabricates an outcome. |
| B-INT-6 §6F, §7 and §7C; receipt §6 | C-SACL.24 plus four claim statuses and .27 plus seven dispatch steps preserve fresh immutable claim, flushed pre-contact intent, spent event, accepted handoff and channel-owned outcome. Header preserves older pre-attempt wording alongside the receipt's explicit pre-intent qualification; missing attempt event after intent never proves no contact. |
| B-INT-6 §6E, §7A and §7B | C-SACL.26 preserves owner authority in checkpoints; .28 carries all six per-write rechecks; .29 reuses the two canonical streaming alternatives C-7Q.11.3.10.1/.10.2. A checkpoint is never a substitute gate, fence or permission owner. |
| B-INT-6 §8 | C-SACL.30 reuses all twelve canonical restriction-trigger atoms, carries exact sensitivity comparison and immediate pre-write stop, restriction-before-recording and scoped background cancellation. Unknown channel history and late confirmation remain truthful. |
| B-INT-6 §9; B9 values complete §3 | C-SACL.31 consumes canonical C-7H.10 retry atoms with the actual values written inline: original plus two technical attempts, 10s/30s live or 1min/3min background minimum gaps, 7min/15min elapsed-from-first-failure ceiling, earliest bound, one careful rejection retry, real-change and early-stop rules. Unknown delivery permits at most one safe automatic retry only on proof or verified deduplication. |
| B-INT-6 §10 and §11 recovery-count wording | C-SACL.32 and sixteen crash-row cards cover rows 1–15 plus 11b, each with committed truth and recovery. Runtime restart has fresh epoch, Dry mode, guest access, dead old claims and no old formed-payload replay. The source's stale 'fifteen' count is marked, not used to omit row 11b. |
| B-INT-6 §§6A/6B/6F/7C/11/12 | C-SACL.33 has thirteen proposed coordination records and all newly owned declared field atoms; proposed payload-reference ownership remains .22.1. Existing purpose/destination/mode/privacy/access/material/identity facts are reused. No final serialization, closed code vocabulary or record field is invented. |
| B-INT-6 §12 | C-SACL.34 carries every one of the twenty-two event/logging mappings, including owner record plus coordination reference, claim-state and pre-contact dispatch-intent events, blocked duplicates and unknown outcomes. References-only logs contain no payload, hidden-existence detail or new authority. |
| B-INT-6 §§13–16 | C-SACL.35 retains all disclosure boundaries; .36 contains thirteen own failure-class cards plus canonical .23.16 unknown handling, covering all fourteen source classes; .37 contains runtime prohibitions. Source audit, implementation and adoption workflow is excluded. Open dependencies remain open. |
| B24 complete §6.5; §6.3; §6.4 opening rules and full §6.4-C4 | C-SACL.38 writes all final-output consumer facts inline: governed surfaces, final_gate_evaluation facts and terminals, access reduction invalidation and unknown-outcome honesty. Full B24 records, states, transactions, lookup-first behavior and recovery matrix belong to CH10-b. No complete B24 package claim is made here. |
| B24 §6.4-C4 versus B-INT-6 §6C | Header and C-SACL.38 preserve owner-specific terminal delivery_outcome_unknown / terminal_delivery_outcome_unknown versus proposed nonterminal delivery_unknown. No unified lifecycle mapping is invented. Independent audit/CH10-b must assess the boundary with full B24 ownership. |
| Kernel §C.1, §O DP1–DP5, §T introduction/I-10/I-12, §U, §S.2 DM-11; kernel receipt | C-SACL.39 carries distinct delivery identities, owner-decision references, retained domain states and additional duplicate prevention. Kernel never replaces privacy/SACL/mode/channel authority. Full kernel lifecycle, records and mechanical owner placement remain a later whole-source obligation, to be mapped with CH10-b's durable-operation mechanics rather than invented as a new top-level component. |
| B-INT-4 §7 C2; V10 §7E-TSC §§16/20/28/29 and §17 Phase 1 | C-SACL.40 supplies current recognized-Ness confirmation for the TSC request tuple, reuses four existing response atoms, binds confirmation_id into BAI consumption and confirmed_at into sacl_recognized_ness_confirmed_at, rejects absent/stale/conflicting/unverifiable facts and obtains fresh retry/recovery confirmation. Root rows preserve other existing TSC access consumers. |
| Bundle 5 Path 6 and §§6–8; Bundle 5 receipt | Output order, independent authority, identity separation and frozen wording are checked against C-SACL.18–.39. Receipt establishes package acceptance only; conditional independent closeout audit is not claimed performed. Other bundle paths retain later owners and the whole-file reading obligation. |
| B-INT-8 §15; B-INT-7 §§14–15 | Existing Connection output and enrollment consumers are reciprocated without importing their full owner mechanics. Enrollment remains CH09-h; Connection owners remain as already written; no recognition-to-access or output-gate bypass is added. |
| B16 complete §8 and §11 opening access bullet; B16EEB complete §13.4; AIC complete §15 | Root USED BY rows retain existing promotion, evaluation and authority-integrity consumers' current SACL boundary. The scoped source facts remain with their existing canonical owners; no whole-file reread or new promotion mechanism is claimed. |
| Bundle 2 complete §5.5; Bundle 3 complete §16; Bundle 4 complete §12 and retained §9.1; Bundle 6 retained §12 | Root USED BY rows retain existing declaration, clash, specialist, living-state, logging and control-query consumers with each place's own input/action/change. No grouped using places, added access authority or duplicate behavioral owner. |
| Canonical earlier-card inspection | All 115 earlier incoming IDs inspected. Full C-7Q.11.3 subtree, C-7L.9/.9.1/.9.2, C-LMAC.14.3, relevant C-7H.10 retry cards, C-7Q.6.4 and TSC request/response/confirmation cards checked for reuse. Earlier chapter fingerprints remain preserved; no earlier file changed. |

### Source placements added by CH09-e

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` §25.6, complete | C-BAI and C-BAI.1–15: complete OS/pending/token/lease/state fields; purpose vocabulary; lifecycles; result/failure classes; audit split; protected-core rules. Shared field atoms are referenced, not assigned duplicate IDs. |
| V10 §7E-TSC consumer interfaces and §25.3/25.4 earlier consumers | Earlier canonical TSC/SIA/SACL cards retain ownership; 47 incoming fields across 45 named cards receive current root USED BY rows. C-BAI.10 and .16 state the producer boundary in full. |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` C-BAI; CY-I | Official name, source-discovery scope and record-access boundary retained; CY-I use at C-SACL is one separate root USED BY row. Full cycle belongs to CH11. |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` embedded §6 | Checked against complete V10 §25.6; C-BAI.1–15. Historical/governance narrative excluded under contract §1.3. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md` §4; §7 C1 | C-BAI.16.1–6: one-winner rule, live checks, ten receipt bindings, flush-before-success, no-receipt failure, post-receipt completion and BAI-only blocked-consume event. The C1 request/response atoms, receipt fields and claim/recovery mechanics remain C-TSC.16 and .29, not new BAI subparts. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Acceptance and exact standalone scope support ACCEPTED bridge lines. Formal independent closure review is not claimed. No workflow content enters behavior. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` §5B, §6, §12 record 7, §14, §§17–18 | C-BAI.17–18: exact opening-purpose spellings, operation bindings, consumption-before-activation, dry-after-crash, current dual-owner lease/Gate1 truth, reference-only observations and fallback. Full mode records, field cards, indicator, fences and activation coordinator remain CH09-i; no completed mode-record coverage claimed here. |
| B-INT-5 §6 Reusable? lease label | Marked source-conflict paragraph and C-BAI.6 Does retain V10 repeated queries/never consumed and the differing matrix label; no silent rewriting. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Acceptance/owner guarantees checked; no claim of implementation or later independent formal closure. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` §§4–6, §18, §19 I1–I10, §§22–24; §17 identity table | C-BAI.19.1–7 carries BAI request/result, all six prerequisite facts, owner re-read, revocation, durable proof and complete minimum binding, proof/opening crash boundary, BAI-only I5C and biometric identity limit. Full proposed prerequisite/begin/binding/session/capture records and their field cards, capture lifecycle and eligibility remain CH09-h; no duplicate EC authority. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Acceptance and §6 frozen wording notes checked. C-BAI.19.5 does not close a nonexistent session; .19.6 keeps BAI the sole I5C source. Receipt's conditional formal closure is not treated as independently verified here. |
| `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` §§7.12–7.13 | C-BAI.20.1–4 states conditional BAI producer mechanics, current six-condition check, durable receipt, no-receipt failure and all post-receipt outcomes. Canonical judgment/claim/receipt field and recovery atoms remain CH03-e–CH03-n. NHD-B16EEB-D16 remains open; no purpose or scope selected. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` §§5–6 | Supports ACCEPTED conditional architecture without closing the seventeen open decision slots. Existing C-GOLD.1.11.17 remains the authority-choice card. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` §4 Group 11 and §6 FR-0003 | C-BAI.8 and .8.3 carry restored different BAI keys for different token purposes with DECIDED-2026-09-25 and deciding-record citations on every such line. |
| `98_HISTORICAL_SOURCES_PRE_V10/sources_recovered/NH_SESSION_REFERENCE_June29_2026.md` §3D | Authorized restored-source file read whole; only FR-0003's key-separation text supplies C-BAI.8.3. All other archive behavior and narrative excluded from this piece; nothing else is restored by reading it. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md` §6E and §13 | C-BAI.21 and reciprocal root rows preserve live lease ownership at output handoff/checkpoints; full output mechanics remain frozen CH09-d. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` §F.2 R31, §K.2 TSC owner row, §T I8 | C-BAI.21 preserves actual proof and owner-only audit. Full envelope, retry/recovery and owner-reference interfaces remain CH10-b; bounded rows do not earn whole-file credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` Paths 3/5/6/7; §§6–8 | Cross-checked C-BAI.16–19 owner and durability boundaries, including different TSC/mode/enrollment recovery outcomes. Complete maintenance/device paths remain CH09-f/g; full consolidation coverage remains later owners. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` discovery | Accepted consolidation scope was read whole in CH09-d; current discovery checks only. No new independent whole-read credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md` §4.1–4.4 | C-BAI.17–18 and root privacy consumer rows preserve separate mode and identity/security owners. Full relationship policy belongs to CH09-i. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` discovery | Acceptance/navigation cross-check only; no new BAI mechanism or whole-file read credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` §9.1 | C-7P.2.6 root reciprocal retains specialist BAI/SACL authority and strictest applicable rule. Other action classification/record mechanics remain their earlier owners. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md` §§13–14; §9 discovery | Store-side consumer boundary remains C-TSC; C-BAI.16 does not take B15's transaction ownership. Full B15/recovery remains earlier CH04-b; no new B15 mechanism written. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` discovery | Dependency/accepted-scope check only; complete earlier TSC ownership retained. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` §15 | Applicable biometric authorization over protected records is preserved; canonical control-plane mechanics remain earlier owners. The control plane acquires no BAI authority. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` §31 | Existing SACL/BAI access boundaries preserved only; no new BAI mechanism. Other framework capabilities remain their named later component owners. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md` §1 discovery | Source-list reference only; adds no BAI behavior. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` §7 discovery | Dependency boundary only; adds no new biometric mechanism. |
| Decision-index search hits: v0_11 and older v0_10/v0_6/v0_5 | Navigation only, never behavior. Highest active version controls navigation; older versions receive no behavior citation. |
| `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md` search discovery | EXCLUDED from behavior: contract §10.9 restricts ledger use to Appendix B. FR-0003 behavior comes from the deciding record and authorized archive, never from the ledger. |
| Inherited 145 READ-file inventory plus one authorized archive file | The cumulative matrix remains intact and gains this source placement. Partial discovery does not close inherited pending whole-file reads. |
| Earlier frozen card identities and canonical ownership | No earlier piece is changed. Existing TSC receipt and interface fields, BOP event/field atoms and Gold judgment/claim mechanics retain their IDs. Current source-map deferrals name CH09-f/g/h/i, CH10-b and CH11 explicitly. |

### Source placements added by CH09-f

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` §25.13 / What BGMM Is and Is Not | C-BGMM, .1, .8: sole bounded local maintenance path; no general administrator authority. |
| V10 §25.13 / Protected Material Boundary | C-BGMM.2/.2.1–.2.5 and .3/.3.1–.3.7: five purpose/material scopes, immutable records, recovery-value prohibition, governed appends. |
| V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible) | C-BGMM.4/.4.1–.4.6: all five layers and the exact administrator/physical-attacker guarantee distinction. |
| V10 §25.13 / Signed-Manifest Trust Anchor | C-BGMM.5/.5.1–.5.5.3, .10.5, .12.5: expected hashes/versions, pinned public key, signed provenance and ordered startup/rollback verification. |
| V10 §25.13 / Encrypted Full-Content Rollback Packages | C-BGMM.6 through .6.5: all record fields, per-file fields and metadata categories; session_id reused at .13.1; canonical separated keys C-BAI.8.1/.8.2. |
| V10 §25.13 / Protected Startup Recovery Worker | C-BGMM.7/.7.1–.7.7: boot and integrity conditions, bounded exact scope, successful permanent inaccessibility and three distinct failures. |
| V10 §25.13 / Entering Maintenance Mode | C-BGMM.8/.8.1–.8.6 and .8.5.1–.8.5.3: all six entry steps; the emergency factor conditions are individually placed. |
| V10 §25.13 / Purpose-Specific Authorization | C-BGMM.2/.2.1–.2.5, .8 and .9.2: each exact factor conjunction; emergency device-trust scope; no phone required for device-trust/emergency branches. |
| V10 §25.13 / File Scope Enforcement | C-BGMM.9/.9.1–.9.3 and .13.4: exact token file list; out-of-scope and immutable refusals; emergency override. |
| V10 §25.13 / Change Application | C-BGMM.10/.10.1–.10.8: seven steps in exact source order and immediate post-touch rollback. |
| V10 §25.13 / Automatic Relocking | C-BGMM.11/.11.1–.11.7: all seven triggers, immediate token revocation/event and partial-change rollback. |
| V10 §25.13 / Rollback | C-BGMM.12/.12.1–.12.6: decryption, prior_hash check, exact bytes, signatures/metadata, prior signed manifest and no-write idempotency. |
| V10 §25.13 / BGMM-Owned State | C-BGMM.13/.13.1–.13.11.2: all eleven fields, append-only applied_changes and checkpoint file-list/hash_before references; no invented session_status enumeration. |
| V10 §25.13 / Privacy During Maintenance | C-BGMM.14/.14.1–.14.5: each content-free description/log/audit surface, protected rollback bytes and all sensitive-content classes. |
| V10 §25.13 / Immediate Security Audit Events | C-BGMM.15/.15.1–.15.17: all seventeen names, structural-only content and write/flush before producing-function return; no invented event schemas. |
| V10 §25.13 / Crash, Restart, Offline Behavior | C-BGMM.16/.16.1–.16.4: open-session crash, interrupted rollback, startup integrity failure and fully offline operation. |
| V10 §25.13 / Protected-Core Rules (Unconditional) | C-BGMM.17 reuses the atomic owners .9.3, .4, .11, .9.2 and .3.6 without new authority. |
| V10 §25 / Build-Time Implementation Settings | C-BGMM.18/.18.1/.18.2: empirical timeout and available-hardware key mechanism; values remain open build settings (Map C10), not conceptual Ness decisions. |
| V10 §§2/2A, §0B and §25.6 purpose/key boundaries | C-BGMM root preserves all fifty-one earlier C-2 maintenance-use places through named gates; .15 retains living-record boundaries; canonical BAI purpose/token/key identities are reused. |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` C-BGMM, C-2 and CY-I | Exact root name, governed-append distinction, qualified physical-attacker guarantee, structural-only maintenance privacy, mandatory C-2 gate and the C-PAIR use in CY-I. |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` embedded security-design §13 | Source-conflict paragraph: stale package deletion versus V10 sealing/inaccessibility; no Companion deletion behavior adopted. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` §9.1 | C-BGMM root USED BY C-7P.2.6 reciprocates specialist protected-change authority. General action mechanics remain canonical in CH07-c. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` §§5B/6 and change-summary context | Cross-purpose token boundary checked; no maintenance-purpose token can open Personal Mode. Canonical BAI boundary remains CH09-e; complete modes remain CH09-i. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` dependency paragraph | BGMM mention is the preserved supporting source title, not added maintenance mechanics; complete enrollment remains CH09-h. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` §2.1 | Names governing BGMM law; adds no BGMM internals in the reviewed passage. Full kernel behavior/whole-file obligation remains CH10-b. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` whole | Search hit is protected-file verification prose, excluded from maintenance behavior. Accepted ordinary-chat policy, frozen source status and open boundaries remain for CH10-e. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` whole | Search hit is protected-file verification prose, excluded from maintenance behavior. Accepted room-start policy and preserved open boundaries remain for CH10-e. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` verification/closure context | Protected-file search hit is task verification, excluded under contract §1.3; no maintenance behavior added. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` §6 FR-0003 | Existing restored key-purpose rule remains C-BAI.8.3 in CH09-e; no additional archive behavior imported for this piece. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` NHD-M25 search hit | Navigation only; no behavior and no current-version authority inferred. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` NHD-M25 search hit | Accepted prior navigation index; no behavior used from its row. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` NHD-M25 search hit | Earlier candidate navigation; no behavior used. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` header and NHD-M25 row | Highest current candidate index used only for navigation; v0_6's accepted-prior standing is preserved; no architecture derived. |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` BGMM discovery | The matched TSC provenance pointer adds no maintenance mechanism. V10 governs; whole-file credit is not claimed here. |
| `01_AUTHORITATIVE/cursorrules` BGMM/maintenance discovery | No new BGMM body found by scoped discovery; implementation/workflow text is not inserted into behavior. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_2026-09-24_v0_1_CANDIDATE.md` BGMM/maintenance discovery | No additional maintenance restoration found; no archive expansion authorized or taken. |
| Remaining owners | CH09-g full pairing/recovery material lifecycle; CH09-h full enrollment; CH09-i full modes; CH10-b full kernel; CH10-e interface packages; CH11 side paths; CH12 regenerated final registers. |

### Source placements added by CH09-g

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` §25.7 / Four States | C-PAIR.1 through .1.6: four exact states, every transition/condition, 90-second initial QR, state-2 permanent inertness/sealing, hardware binding, state-3 failure/timeout retry, state-4 four-condition finalization, final trust and permanent closure. |
| V10 §25.7 / What becomes permanently inert when | C-PAIR.1.2.1 signed QR; .1.2.2 temporary secret; .1.4.1 trust upgrade; .2.3.5 recovery-code local copy. The source's four artifact/time rows are all placed. |
| V10 §25.8 / First Recovery Code Creation | C-PAIR.2.1 through .2.1.5: immediate first creation, desktop encryption to phone key, phone-only biometric-approved decryption, phone-only display, no desktop/clipboard exposure, confirmation/10min30s hiding and clipboard clearing, old-valid/new-inactive timeout outcome. |
| V10 §25.8 / Save Verification | C-PAIR.2.2 through .2.2.5: Saved in Bitwarden trigger, exactly four unique random positions, requested order and exact case, three attempts, new positions after failure, local verification, all three unpersisted classes, terminal new-code inertness/old-code preservation/restart. |
| V10 §25.8 / Activation Handover | C-PAIR.2.3 through .2.3.6: all six steps in source order; four individual local-test prohibitions .2.3.2.1–.2.3.2.4; test-before-activation; new-active-before-old-invalid; immediate local-copy inaccessibility/sealing; Bitwarden as sole intended long-term store. |
| V10 §25.8 / Recovery Code Rotation | C-PAIR.2.4 and .3: every successful pairing/re-pairing triggers the same complete handover; old code stays valid until saving, verification, local test and activation all succeed. |
| V10 §25.9 | C-PAIR.3 through .3.4: both normal recovery factors, replacement by default, full pairing/verification before automatic prior-phone revocation, complete re-entry flow for a revoked phone, mandatory normal-code rotation. |
| V10 §25.10 / Required Factors | C-PAIR.4.1 through .4.1.3: four simultaneous factors, emergency code outside Bitwarden, printed sheet physically secure, unconditional remote prohibition. Existing BGMM physical-presence/thumbprint/code/sheet owners are reused by exact name. |
| V10 §25.10 / Intermediate State (Provisional Only) | C-PAIR.4.2 through .4.2.6: all six source invariants separately placed; new trust provisional; every old phone/code/sheet remains valid; no partial revocation. |
| V10 §25.10 / Required Steps Before Final Commit | C-PAIR.4.3 and .4.3.1–.4.3.3: normal code saved/four-character-verified/tested, emergency code saved/verified, printed sheet confirmed saved/verified. Normal-code testing is reused; activation is not pulled forward into preparation. |
| V10 §25.10 / Atomic Final Commit | C-PAIR.4.4 and .4.4.1–.4.4.7: sole new-phone permanent trust, all old phones revoked, each old code/sheet invalidated, simultaneous new-material activation and bai_emergency_reset_finalized in one atomic commit. |
| V10 §25.10 / If Any Step Fails Before Final Commit | C-PAIR.4.5 through .4.5.4.2: safe abort, all new material sealed/inert, provisional pairing cancelled, complete prior-authority preservation, bai_emergency_reset_aborted, failed-step and reason details without invented field names. |
| V10 §25.11 / Prerequisites (All Six Must Be True); §7L Integration | C-PAIR root enrollment use and .1.6: four pairing-owned prerequisites; exact bai_initial_setup_finalized owner-phone trust reference in the provisional link basis. Full enrollment mechanism remains CH09-h; C-7L.11.5 remains the existing provisional-link basis owner. |
| V10 §25.6 / Purpose Binding | C-PAIR.1.2.3 reuses C-BAI.3.8 app_session_key_ref; hardware-backed keystore trust, no OS device-ID substitution. Canonical biometric artifacts remain CH09-e. |
| V10 §25.13 / Protected Material Boundary; Entering Maintenance Mode; Purpose-Specific Authorization | C-PAIR root, .3.1 and .4.1 reuse the exact existing BGMM authorities/factors. Eleven incoming fields from ten earlier cards are reciprocated. Device-trust/emergency authority never extends to emergency code/configuration writes. |
| V10 §§2/2A and §0B | C-PAIR root gates all 51 distinct C-2 interaction/delivery owners; .6 preserves connected permanent operation recording, one-operation-one-log, no double evidence and Level-1 secrecy/access limits. No project workflow is imported. |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` C-PAIR | Exact root name and full handover/replacement/emergency wiring; .6/.6.1–.6.4 place every named audit-operation category and its authorization limits. |
| Map C-2 and CY-I | Root C-2 gate and its 50 subcard reciprocity obligations; ordinary and CY-I BGMM uses are preserved. Complete side-path assembly remains CH11. |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` embedded security-design §§7–10 | Conflict header preserves stale destruction/erasure versus V10 sealing/inertness/inaccessibility at QR pairing, failed save check, activated local copy and aborted provisional emergency material. No older destructive behavior is adopted. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` §§3–5 | C-PAIR.5/.5.1 preserve pairing-owner authority, four prerequisite facts, hardware identity, outer trust versus inner approval, live-owner revalidation and changed-prerequisite refusal/revocation. Full enrollment_prerequisite_snapshot [proposed], its fields and all six-owner coordination remain CH09-h. |
| B-INT-7 v1.1 §9 | C-PAIR.5.2: loss/replacement/revocation, invalid recovery/setup and QR/secret contradiction are actual owner events; enrollment stops before logging, preserves committed observations, excludes affected segments and never silently resumes. Full consumer protection mechanics remain CH09-h. |
| B-INT-7 v1.1 §13 | C-PAIR root USED BY C-7L.11.5 and .1.6 event basis: owner-phone trust is evidence for declared enrollment provenance, never confirmed voice identity. Existing Person-Box link ownership remains CH06-c. |
| B-INT-7 v1.1 §19 I1/I2; bounded §6A/§6D context | C-PAIR.5.1 states operation_ref and per-prerequisite owner_ref/owner_version/satisfied reference-only seam and owner re-reads. Complete I1/I2 schema atoms, snapshot and capture-start consumer records/mechanics remain CH09-h; no pairing owner acquires capture or coordinator authority. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` whole | Acceptance/version provenance checked; candidate filename and [proposed] labels retained. Frozen three wording notes and open implementation/threshold boundaries remain carried, with full enrollment treatment in CH09-h. Receipt prose is not system behavior. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` B-INT-7 consolidation paragraph | Confirms trusted-phone enrollment wiring without adding pairing mechanics; full enrollment B-INT-7 ownership remains CH09-h. No unrelated consolidation scope claimed here. |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` and `01_AUTHORITATIVE/cursorrules` pairing-topic discovery | No additional pairing/recovery mechanism found in scoped topic discovery. No new whole-file read credit; project workflow excluded. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` §9.1 specialist-authority paragraph | Discovery hit retains BGMM for device-trust changes and §25 safeguards; these existing boundaries are consumed through canonical BGMM ownership, not a new pairing mechanism. Full permission/action ownership remains CH07-c. |
| All 04/05 files, by C-PAIR/full-name/pairing/recovery-code/trusted-phone/device-trust/Bitwarden discovery | B-INT-7, Bundle 4 and Bundle 5 consolidation match these scoped topics; no separate later pairing package or recovery decision found. Discovery is not whole-file reading; the restoration ledger is excluded from behavior discovery. |
| Remaining owners | Full enrollment coordinator and schema atoms CH09-h; full modes CH09-i; full durable-operation kernel CH10-b; side-path assembly CH11; script-regenerated final registers CH12. No unstated code format, emergency-check algorithm, QR-expiry regeneration route or crash implementation is selected. |

### Source placements added by CH09-h

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| V10 §25.11; Map C-ENROLL | C-ENROLL retains the exact Map name and DESIGNED status. Full initial enrollment flow is placed through .1–.16; specialist authorities remain separate. All 22 earlier incoming fields across 19 places are reciprocated; all 13 inspected earlier uses receive root relationships. |
| V10 §25.11 / Prerequisites; B-INT-7 v1.1 §4 | C-ENROLL.2 and .2.1–.2.6 place all six conditions. Pairing facts reuse C-PAIR.1.2.1/.1.2.2/.1.4.1/.1.4.2/.1.6/.2.3/.5.1; SIA/SACL own spoofing and Gate 0; C-7L.4 owns confirmed Ness-box truth. |
| B-INT-7 §4 snapshot and §19 I2 | C-ENROLL.2.7 and its children: snapshot_id, snapshot_version, six per-owner entries, owner_ref, owner_version/current event identity, satisfied, taken_at and boolean all_six_satisfied. C-ENROLL.2.8 owns the operation_ref request seam. No snapshot becomes authority; failed initial checks prevent the BAI call. |
| B-INT-7 §3 | C-ENROLL.1 owns coordination only. Phone, recovery, QR, spoofing, box, biometric session, identity/access, privacy, root, queue and profile authority remain at their actual owners; outer trusted-phone binding and inner biometric approval are not named identity. |
| B-INT-7 §5 steps 1–3; §17; §19 I1 | C-ENROLL.3/.3.1–.3.5: dedicated trusted-phone flow, explicit_begin_event_ref, trusted_phone_binding_ref, stable proposed parent and prospective session identities, proposed begin claim, no authority from reservation, anti-double-tap identity and refusal/recovery outcomes. |
| B-INT-7 §5 steps 4–10; §19 I3/I4 | C-ENROLL.4/.4.1/.4.2/.4.4: full ordered request, BAI-only pending/prompt/token, immediately fresh owner recheck, revocation without consumption on change, verified flushed proof then opening then capture. Exact purpose/requester/operation_ref/session_ref and pending_id/refusal/token_ref/failure forms are present. Existing C-BAI.19.1–.19.4 remain canonical authorization/proof owners. |
| B-INT-7 §6A | C-ENROLL.4.3 and eleven field cards carry the complete durable chain and binding: proposed operation/session IDs; separate token/pending refs; exact purpose; app_session_key_ref; snapshot ref; BAI trusted-local timestamps; requester; audit schema/version; integrity reference. The proposed append-only companion references the BAI event and is referenced by that event or opening. No secrets or new biometric authority. |
| B-INT-7 §6B | C-ENROLL.4.5 and eight children place every duplicate barrier: one begin/two sessions, two proofs/one session, one proof/two sessions, old unmatched result, changed prerequisite, absent flushed proof, stale snapshot and concurrent BAI pending. |
| B-INT-7 §6C; receipt §6 wording note 2 | C-ENROLL.4.6/.4.7 and .6.14 preserve no-session spent-proof abort versus an actually opened session with confirmed zero capture. The former uses the proposed abort event, never a fictitious session-close event; both prohibit silent microphone activation. |
| B-INT-7 §6D; §19 I5A | C-ENROLL.5/.5.1–.5.5: current opening/privacy/security/no-stop conjunction; flushed proposed intent before request; seven reference-only request classes, each placed; exact started/confirmed_not_started/unknown results, separately placed; B29-sourced proposed start fact. Intent, start and observations remain distinct, with every stated crash outcome and no inferred non-start. |
| B-INT-7 §7; V10 §25.11 BOP Integration; §25.12; §19 I5B/I5C | C-ENROLL.5.3.5/.5.6/.5.7 consume canonical C-BOP.15 and C-BAI.19.6. role=ness is declared; source_title=enrollment:ness:<session_id>; session_authorization.authorization_type=enrollment_declared is formally adopted. Exactly one BAI-sourced biometric:result:success observation with session ID and trusted-local timestamp; deterministic capture_id from session/opening/command. Canonical C-BOP.15.3.1/.15.3.2 retain the two fields; forbidden purpose/token/biometric/authorization/identity payloads remain absent. |
| B-INT-7 §7 A15 boundary | C-ENROLL.5.6 names C-BOP.12, the already placed six-field/five-name acoustic-condition amendment owner. Those atoms remain there; h preserves physical context only and all ten prohibited conclusions: identity, speaker change, spoofing, imitation risk, emotion, intent, meaning, importance, behavioral pattern and causation. |
| B-INT-7 §8 | C-ENROLL.6.1–.6.27 place all 27 exact proposed state labels, splitting both combined table pairs. Every entry fact, actual owner and outcome is written. The combined closing/closed source condition is preserved without inventing an intermediate commit rule. |
| B-INT-7 §8A/§8B | C-ENROLL.6.28/.6.29: separate capture-session/parent lifecycles; valid unaffected material can continue after closure/interruption; only legal nonterminal transitions; no regression of committed observations/roots/readings/eligibility/link/profile; absorbing parent terminals; at most one winner; no state inferred from coordination. The source's abort shorthand is bounded by §6C and the receipt. |
| B-INT-7 §9 | C-ENROLL.7/.7.1–.7.8 place all eight owner-event groups, explicitly retaining loss/replacement/revocation, recovery/setup and QR/secret alternatives. Stop precedes logging; only committed observations are preserved; no reconstruction or affected-segment training; honest closure/interruption; no same-session resumption; no TSC lifecycle/database/archive authority reuse. |
| B-INT-7 §10; §19 I6–I9 | C-ENROLL.8/.8.1–.8.4 carry all ten close/freeze/Catalog/B11/append/duplicate/root_id/queue/quarantine steps. I6 actual observations to immutable set; I7 frozen capture_ids+provenance and accepted/rejected/blocked; I8 capture_id-derived identity+validated root fields+ingest_operation_id and root_id/append_duplicate_absorbed/rejected/indeterminate; I9 root_id/enqueued. Canonical C-BOP.13.1, C-STORE.3.5/.4.6.2.1/.4.6.2.3, C-7E, C-7GA and C-READ.11 retain their existing schema/fence/queue atoms. No duplicate writer or queue is introduced. |
| B-INT-7 §11; §19 I10 | C-ENROLL.9/.9.1–.9.6 carry all six checks; .9.6.1–.9.6.5 carry every stream-integrity condition, including threshold over the FULL segment. Authorization requires enrollment_declared plus session_id linked to confirmed durable bai_token_consumed. overall_completeness is exactly complete or partial. Stream consistency never establishes who spoke. |
| B-INT-7 §§11/17/20 | C-ENROLL.9.7/.9.8 and field children place proposed immutable segment and eligibility-decision identities, one outcome per segment, accepted/rejected event mirroring, reason and source references without audio. Replay recovers the prior decision; rejection preserves roots and prevents training. |
| B-INT-7 §12; §19 I11 | C-ENROLL.10/.10.1–.10.4: accepted quarantine readings only; counted_reading_refs set keyed by reading identity; each eligibility-decision ref; readiness outcome; unavailable-rule, unverifiable-set and missing-decision failures; no numbers/durations/thresholds/algorithms; no rejected-as-valid or invented insufficient_context reading; no A29 substitution; no link/profile if not ready. |
| B-INT-7 §12A; §17 | C-ENROLL.10.5 and five permitted input classes: exact eligible accepted reading refs, eligibility decisions, operation/session refs, prerequisite/authorization evidence, readiness ref. One proposed immutable bundle per readiness outcome; recover the same bundle on replay. Coordination only, no profile/store/identity evidence. |
| B-INT-7 §13; §19 I12; V10 §25.12 | C-ENROLL.11/.11.1 use all canonical C-7L.11 field owners by exact name: link_type=enrollment_material_provisional, certainty=enrollment_provisional, proposed stable proposal ID, provenance-only meaning, three-part basis, bundle/confirmed box/operation/session/readings/eligibility/prerequisite references. Proposal recorded is separate from committed/refused/pending outcome; current committed link required; refused/pending/stale/contradictory/unverifiable outcomes remain individually owned in C-7L.11.13.1–.13.6. |
| B-INT-7 §14; §17; §19 I13 | C-ENROLL.11.2/.11.3 and canonical C-SIA.20 retain the proposed idempotent build identity keyed to committed link+linked reading set, SIA-owned commitment before creation event, enrollment_provisional status, recognized_ness ceiling without grant, five dimensions weighted above acoustic until enrollment_active, ordinary later training and unknown/guest restart. C-ENROLL.6.25 requires both commits and both enrollment events for completion. |
| B-INT-7 §§15/16; §19 I14; B-INT-5 §5B | C-ENROLL.12 reuses C-SIA.20.8/C-BOP.15.6 and names privacy/SACL/mode gates. All enrollment-alone authority prohibitions are written; privacy precedes capture; minimum protected raw-voice boundary; references/structural facts only; no ordinary-component sensitive payload merely for rejection; no indirect disclosure or reconstructive logs; final privacy-first/access-second/fence-revalidated output. Enrollment purpose never opens Personal Mode. |
| B-INT-7 §17, all 17 identity rows | Proposed parent/session/begin claim .3; BAI pending/token C-BAI.19.1; snapshot .2.7; proposed segment and decision .9.7/.9.8; BOP capture_id and B11 ingest_operation_id .8.3 with canonical owners; queue/read refs .8.4; proposed readiness .10; proposed bundle .10.5; proposed proposal ID .11.1; proposed build identity .11.2; capture-control/intent/start .5; proposed recovery identity .13.3.1. One-parent/many-children/no-extra-weight rule .13. |
| B-INT-7 §18 | C-ENROLL.14 and nine event children preserve every exact settled enrollment event. Additional proposed abort/intent/B29-start names remain separate at .4.6/.5.2/.5.5, not mislabeled settled events. BAI and every other owner keep their events. Required write/flush precedes owner success; .16.3 handles failure. |
| B-INT-7 §20, all 13 proposed record kinds | Intent .5.2; bundle .10.5; parent operation .13.1 with identity/state/terminal reason/audit-ref atoms; stage event .13.2; begin claim .3.4; snapshot .2.7; authorization binding .4.3; capture set .8.1; segment .9.7; eligibility decision .9.8; readiness .10; recovery event .13.3 with identity/boundary atoms; duplicate absorbed .13.4. All are append-only reference-only non-authorities with no evidence weight. |
| B-INT-7 §21, every crash row | C-ENROLL.15.1–.15.7 map source rows 1–7; .15.8 maps inserted row 7b; .15.9–.15.21 map rows 8–20. Every committed-truth and exact recovery action is written. The table has 21 rows despite §20/§26 saying twenty; no row is omitted. I5C preserves BAI as sole recovered biometric-observation source. |
| B-INT-7 §22 | C-ENROLL.16/.16.1/.16.2: same-parent technical retry only when no fresh explicit action and no recreated security authority; all seven prohibited reuse classes; five fresh-session requirements; accepted B9 values consumed by reference with none invented. |
| B-INT-7 §23, all 16 failure groups | Bad prerequisite .2; pending conflict .4.5.8; unmatched result .4.5.4; unflushed proof .4.5.6; unverifiable binding .4.3; changed prerequisite .4.2; absent/current opening .5.1/.5.3.3; unsafe BOP capture .5.3.6/.5.6; privacy exclusion .7.7; Catalog nonacceptance .8.2; unverified append .8.3; unavailable eligibility owner .9; readiness failure .10.4; unavailable Person-Box/SIA .11; owner contradiction .15.21; required audit failure .16.3. Each outcome is explicit in the owning card; .16 retains the complete named list. |
| B-INT-7 §§0–2/24–26 and closure receipt whole | Authority/version/dependency and drafting/implementation instructions are provenance or excluded project workflow. System boundaries from §24 are placed in .1/.5/.8/.9/.11/.12/.13; still-open mechanics in §25 are explicitly assigned to CH09-i or remain unchosen. Receipt's three frozen minor notes and the actual 1066-line count are preserved in delivery records; no source is edited and no independent audit is claimed. |
| Full Bundle 5 consolidation v1.1 | Its enrollment scope and cross-package authority table support explicit begin plus BAI token, actual specialist owners, one-reference recordkeeping and no substituted authority. Other consolidated policy/mechanical details retain canonical earlier C-7Q/C-24/C-TSC/C-SACL/C-BAI/C-PAIR owners; full Personal Mode remains CH09-i. Receipt/history/closeout prose is excluded from behavior. |
| Companion embedded security §§11–12 | Header conflict retains V10 permanent QR/secret inertness instead of Companion destruction. Formally adopted enrollment_declared and enrollment_material_provisional vocabulary is placed through canonical BOP/Person-Box owners, without a second schema or older destructive behavior. |
| 04/05 discovery by C-ENROLL, full name, enrollment and bootstrap topics | All 15 matched paths classified. B-INT-7 and Bundle 5 read whole. B11 bootstrap hits describe historical sealed-batch registration, not enrollment; its root path is consumed through earlier canonical owners. Kernel dependency-list hit adds no new enrollment rule; full kernel CH10-b. Highest decision index v0_11 is navigation; v0_5/v0_6/v0_10 hits are superseded navigation. |
| Active decision/candidate matches | Synthetic-voice decision v0_2 reread whole: selected output voice is distinct from identity/enrollment; speech choices land CH09-i. Recovery buckets Group 6 is bootstrap reading and memory health, not voice capture, with no new archive use here. B16 EEB v1_7 §2.10 cites enrollment as an authority example and changes no enrollment policy; promotion/judgment rules retain earlier ownership. |
| Remaining owners and holes | Complete modes and still-open B29 mechanics CH09-i; full model/B24/kernel CH10-b; side-path assembly CH11; final script-generated registers CH12. No new prompt wording, sample/duration/quality/diarization/spoofing/readiness/activation value, hardware, channel, cleanup algorithm or serialization is selected. Gaps in this piece remain exact NOT DECIDED. |

## READ RECORD

Contract §§5–11 and lessons §§1–11 reopened for this piece; contract §11.3 reopened after writing. Bounded source reads do not receive whole-file credit. The following scopes describe actual reading; downloaded files are not treated as read. Earlier whole-read credits are inherited without claiming to have repeated them.

| Source file | Reading scope / whole-file credit | SHA-256 |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Whole scoped §§25.11 and 25.12, including all prerequisite, BOP, eligibility, link, SIA, audit and authority-limit subsections. Prior whole-file credit inherited; no new whole-file reread claimed. | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Whole C-ENROLL entry and fixed name checked; source discovery remains scoped. No new whole-file credit. | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Embedded security-design §§11–12 body read whole; prerequisite 3 destruction wording compared with V10 inertness. No new whole-file credit. | `cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` | WHOLE file, lines 1–1066, read in four untruncated bounded outputs before drafting; selected tables and §§24–25 reread during reconciliation. New whole-file credit. Every behavior section, 27 state labels, 17 identity rows, 16 interfaces, 13 record kinds and 21 crash rows reconciled to current or canonical earlier owners. | `184a63cf7dfbefdd73ea84c02506e3478374a48df2d9a2e174ed9a38305cacb6` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | WHOLE file reread. Accepted v1.1 identity, actual 1066-line count, three frozen minor wording notes and still-open boundaries checked; no new whole-file credit and no independent audit claimed. | `df028286c89b7c0a4bea3bb1403d910b11f993bac010d03320f55eeec71d636a` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | WHOLE file, lines 1–853, read in two untruncated bounded outputs. New whole-file credit. Consolidated enrollment/authority boundaries used; other policies retain earlier canonical owners and full modes CH09-i; provenance and closeout workflow excluded. | `b20d4ee944d5a575b307d70485e5c074c4b298f43a3082ddd760159aa61d924d` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Bounded current read of non-substitution, frozen-wording and still-open dependency passages. Earlier whole-file credit inherited; no fresh whole-file reread claimed. | `d62ec6e4d61495147729241331733f81982792440148f624551fe64d9346fa44` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` | Scoped cross-purpose prohibition and factor-matrix passages read, including enrollment-purpose tokens never opening Personal Mode. Full mode mechanics remain CH09-i; no whole-file credit here. | `c449728139f732d5aefe5efd7ca1a0d251937c64bd73504ff8527cc3ec01b305` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | Enrollment/bootstrap topic discovery: 48 bootstrap hits, no enrollment-text hit. These concern historical batch registration/coverage. Existing canonical C-STORE/C-BOP mechanisms consumed; no new whole-file reread claimed. | `baca06e562027a080dab4384943bfb87947c6f598b36776f1016fa8472384a87` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Bounded sealed historical-batch and bootstrap-coverage passage read; confirms bootstrap naming is distinct from voice enrollment. No new whole-file credit. | `cf95a4f8622487a4a254435fd05471572cf0a9ef1886c6bee3352ed7d45621f1` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` | Bounded dependency-list context around the B-INT-7/Bundle 5 reference read. No additional enrollment mechanism is claimed; full kernel remains CH10-b. | `1f9ea714f1a182c0857e80399850a3aeebcf4a50a32d5a200fce57a5d5f47ae3` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md` | WHOLE file reread. Synthetic output selection remains distinct from enrollment identity and does not change B-INT-7 or A15; complete speech selection belongs CH09-i. Prior whole-file credit retained. | `af3c531803f8988f8131061d4d61f8856f1156c2e83dc95dc65dd4597a779cfd` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Scoped Groups 6–8 context read to classify bootstrap-reading search hits. No voice-enrollment restoration and no new archive opening. No whole-file reread claimed. | `9f6f9cac1e07ab14f0c6f3ed834b8260265dac6f6a430fa12be5c6e4c3f0b59f` |
| `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` | Whole §2.10 and bounded §2.8/§2.9/§3 context read. Enrollment explicit-begin-plus-BAI example changes no enrollment authority; its separate evaluation-judgment gap retains earlier ownership. No whole-file reread claimed. | `04dd5abc42e59afb61b4d280a0bb69d647d187fd0da385bc5c567eddbca81a41` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Scoped NHD-BINT7 and adjacent Bundle 5 rows read as navigation. Earlier index versions were discovery hits only, not behavior sources; no whole-file reread claimed. | `aad8d1aeee9a331ad6f4d9ddbcfa9c42eae2a94e1ef1bccde7484079181ff7b4` |

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
| CH05-e | `e526f830db5a71a0a60c7c7e0a50ef0344f81f46bce4355e1a27480d6d0076cd` |
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
| CH08-b | `6bb46d5f30d1e67d7a27f252d656118a89b86f3a46a820542010f8599b169fa0` |
| CH08-c | `30824515b3c0d90a694118848113c4695434b1203ff1c8d5267e4dee5d456bbf` |
| CH08-d | `775c59f45dfc8fd1b8befe3e735062cfff5fab76c479afd8cfb2da34f9eaef5f` |
| CH08-e | `ac9be126cbff22a1eb34ce7fa8b881feae05aa39a2deb6510ac9de5a196bdfd5` |
| CH08-f | `d3d86da7a5e786b5449bb54a48afb476d076a9bbd9f35efd770f6368f8ed8385` |
| CH08-g | `ebf122c638aeece6e97816efc417a01e03c4140fd0d7131b18d6e80a6b8a24a3` |
| CH09-a | `22af523cc67cd0328b30cbcd7d09822d92f98e9e4b964fbd04b77bc565b08aea` |
| CH09-b | `283706c41b3d9e18751a24ee20f2406b52f9af043e675d1f838542a47aeb2f2d` |
| CH09-c | `5a61d0c9956317dc544fb818bfb8ffcd08c6ebde710cf9c264b45e38f2b41e50` |
| CH09-d | `8877df31acb4ac15c45d2687f5e82c2fb5a5541fef57fb6f475ca7694c01d338` |
| CH09-e | `370aed5b7efa49a861e39ff2bad7e1d21bed31826f001bd77cde46382cf509ad` |
| CH09-f | `0b06b8fc0a819d6844c8e1a638afa615e24bc59663daab8cb3d19434f8fd69b7` |
| CH09-g | `93002da16c0c48625e63d808f07e2c7a8414e349c56e98476a6ff867f3c9d8d1` |

### Instruction and carry-forward identities

| Artifact | SHA-256 |
|---|---|
| Build contract v1_0 | `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1` |
| Lessons v0_4 | `e60b950df06fd4ac62961b194e416d2fba682ab02436c2ade131a8cd6f3f7bf8` |
| Run instructions v0_5 | `f0d9c411ee1bceda4c3527e58b1b1c60631304200a802fdb246edba31ded77d3` |
| Route v0_4 | `a83d9c1451d25bed3da95e7dcb83aa399abbed600d79d9da0c0e910275ffa97d` |
| Writing 2 manifest | `5f435a441ed31a3f14c05c2ae1c58d904e8ea7a5a680fcc433308b1196511160` |

### READ-folder files not yet read whole

46 inherited pending files remain after the explicitly credited whole reads. Scoped discovery does not close these obligations.

- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md`
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

## CONTRACT CHECK

CONTRACT CHECK (against the cloned contract, SHA-256 e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1)

§1.3 no history/actions/roles/workflow in this chapter: PASS — All 194 behavior cards and 160 use rows reviewed against their source scopes. Project acceptance, audit, implementation and writing instructions remain outside system behavior. Box sentences were handwritten; scripts format citations, structural tables, indexes and checks only.

§1.4 every gap written as NOT DECIDED: PASS — All 367 empty fields use the exact marker and are individually registered. Restrictions, failure outcomes and actual gates were reviewed across all 1,757 field lines and all use rows; all 26 positive prerequisite-review hits have named card/line/reason dispositions. No triage derivation fills a gap.

§1.5 conflicts marked, none resolved: PASS — The header marks Companion §11 destruction wording against V10's permanent QR/secret inertness. V10 behavior is retained. The frozen receipt notes and the 21-versus-twenty crash-count wording variation are recorded without editing sources or dropping a recovery case.

§3 exactly one stamp per line: PASS — All field lines and use rows checked against canonical target stamps. The root remains DESIGNED and accepted mechanics remain ACCEPTED. No new BUILT claim or DECIDED line occurs. Source-proposed records, states, events and identities keep their qualifier in current behavior and use rows.

§4 every behavior line cited in the exact format: PASS — All non-gap fields and use rows carry exact citations; all 40 distinct citation locations resolve at the pin and were checked against the relevant content. The temporary authoring citation abbreviation is fully expanded and does not occur in the delivered file.

§5.4 one name per thing: PASS — The exact Map root name, 194 unique current IDs and every named endpoint match the fixed naming sources and earlier cards. Canonical names containing a colon are checked in full. No new top-level ID is introduced.

§6 all template fields present, in order, for every part: PASS — Every card has the full ordered ALONE/TOGETHER fields, six-column single-place USED BY table and own-child-only SUB-PARTS. No card lists itself.

§6.3 reciprocity within this chapter: PASS — All 135 internal relationships have individually authored reciprocal use rows. The 160 total rows include 19 earlier using places, covering all 22 inspected incoming fields, and 6 back-link rows added in the cleanup round. All 13 earlier enrollment use rows receive matching root relationships. The 206 outgoing relationship occurrences are answered by the 206 rows of the cross-piece USED BY continuation table; of the 25 external uses, 19 are answered by 19 TOGETHER continuation rows and the 6 back-link rows by the using cards' own TOGETHER lines, without editing earlier chapters.

§6.4 every decided detail written in, no citation used in place of content: PASS — The 35-row source map reconciles 113 selected exact literals; all six prerequisites, the ten opening steps, eight duplicate barriers, binding fields, seven capture-request classes and three start outcomes, 27 state labels, eight safety groups, ten root/read steps, six eligibility checks with five stream-integrity conditions, complete readiness/bundle/link/profile order, 17 identity rows, 16 interfaces, 13 coordination record kinds, nine settled plus three proposed event names, every one of the 21 crash rows and all 16 named failure groups are placed. Existing biometric, BOP/A15, Person-Box, SIA, B11 and queue field owners are named and reused, not replaced by summary citations.

§6.5 sub-parts recursed to the bottom: PASS — Snapshot fields and per-owner entry fields, explicit-action identities, proof-binding fields, duplicate barriers, capture-request references and outcome values, every process state, safety classes, segment checks and stream-integrity conditions, eligibility reason/reference/outcome fields, readiness fields, all five bundle reference classes, parent fields, recovery identity/boundary, each settled event and every crash case are placed at their owning level. Already defined specialist atoms retain their canonical owners. No empirical value or unprovided implementation field is invented.

§9 coverage matrix rows added for every file used: PASS — The cumulative matrix retains all 146 pinned paths. The 35 source-map rows classify every current scope, including all 15 discovery matches and explicit later owners. All 15 READ RECORD files match expected SHA-256, pinned Git blob and byte length. Two newly read whole files reduce inherited pending obligations from 48 to 46; bounded discovery and partial reads receive no whole-file credit.

§10.11 no recommendation, no sentence addressed to Ness: PASS — The complete behavior block and use rows contain system behavior, with no recommendation or direct instruction to Ness. All 53 preceding chapter fingerprints remain unchanged.

Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` and `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` (new whole-file credits); `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` and `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md` (whole rereads, prior credits retained). All other actual scopes are stated in READ RECORD.

Finished-file verification: 194 cards; 1,757 field lines; 160 single-place use rows; 367 registered gaps; 135 reciprocal internal relationships; 225 cross-piece continuations; 40 resolved citation locations; 113 selected literals present; 15 matching current source fingerprints; 53 preserved preceding chapter identities; 35 source-map rows; 146 carried inventory paths; 46 pending whole files. All 26 positive flags are named prerequisite-review cases; there are no empty-TOGETHER or plain-TOGETHER flags. Zero structural/reciprocal/name, formula, workflow or wording errors; zero new BUILT assertions. All twelve contract entries are PASS. These are writer checks; independent audit remains pending.
